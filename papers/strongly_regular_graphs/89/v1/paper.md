# Symmetric between-layer blocks in layered directed strongly regular graphs: a trace count, the graphs on 108 vertices, and the open parameter sets up to 110 vertices

## Abstract

A layered dsrg has adjacency matrix $A=I_m\otimes X+(J_m-I_m)\otimes Y$: $m$ copies of a digraph $X$, any two joined by the same block $Y$. We study symmetric $Y$ with constant row sums, using no group. Then $X$ commutes with $Y^2$, the compression of $X$ to each eigenspace of $Y$ on $\mathbf 1^\perp$ is a scalar fixed by the parameters, and on each eigenspace of $Y^2$ the off-diagonal parts of $X$ multiply to a scalar. Since $\operatorname{tr}X=0$, traces fix the number $a=\operatorname{tr}Y$ of absolute points of $Y$ and constrain the multiplicities of $Y$. In a Cayley construction $a$ is $0$ or $v/m$.

For squares $Y^2=oI+bN+cJ$, with $N$ the relation "same class" of a partition, the count is a finite computation, implemented twice in exact arithmetic. For $(108,40,35,14,15)$ it leaves two squares compatible with a group acting regularly on each layer, both with $m=3$: a reversible Menon difference set, which must avoid the identity, and $9I-N+4J$ with classes of size 9. Over $S_3\times S_3$ an exact enumeration shows that these give exactly three graphs and their converses: the graph of paper 87 and two new ones.

For the 574 parameter sets with $v\le110$ open on 2 November 2026, no dsrg of this form with $Y^2\in\operatorname{span}(I,J)$ exists, for any $m$, over any group or none. The proof uses the count, srg arithmetic, and one 15-vertex layer problem settled by two exact searches with positive controls. For squares with $b\ne0$ the count excludes 1939 of 2308 candidate entries, and 356 more for Cayley constructions. No parameter set is shown unrealisable.

## 1. Introduction

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$. Its eigenvalues other than $k$ are the roots $r>s$ of $x^2-\beta x-(t-\mu)$, where $\beta=\lambda-\mu$. So $r+s=\beta$ and $(r-s)^2=\beta^2+4(t-\mu)$.

Many known dsrgs have a *layered* adjacency matrix
$$A=I_m\otimes X+(J_m-I_m)\otimes Y,\qquad m\ge2,\tag{1}$$
with $n\times n$ zero-one blocks, $v=mn$ and $\operatorname{diag}X=0$. The graph consists of $m$ copies of a digraph $X$, and any two copies are joined by the same block $Y$. Paper 43 [3, Theorem 4] gives the criterion for (1) to be a dsrg. This paper studies the case where $Y$ is symmetric. We call $a=\operatorname{tr}Y$ the number of *absolute points* of $Y$, as for a polarity. In a Cayley construction over a group $K$ (Corollary 5) the diagonal of $Y$ is constant, so $a\in\{0,n\}$.

**Results.**
- *The trace count (Theorem 3, Corollary 4).* Suppose (1) is a dsrg and $Y$ is symmetric with constant row sums $y$. Then $X$ commutes with $Y^2$, and the compression of $X$ to each eigenspace of $Y$ on $\mathbf 1^\perp$ is a scalar fixed by the parameters. On each eigenspace of $Y^2$ with eigenvalue $q>0$, the two off-diagonal parts of $X$ multiply to $\omega I$ with $\omega=((r-s)^2-m^2q)/4$. Taking traces gives a formula for $a$; for example, if $Y^2$ is nonsingular on $\mathbf 1^\perp$, then $(m-2)(a-y)=2k_X+\beta(n-1)$, where $k_X$ is the degree of $X$. No group is used, and $X$ need not be normal.
- *Squares in $\operatorname{span}(I,N,J)$ (Section 4).* When $Y^2=oI+bN+cJ$, where $N$ is the relation "same class" of a partition into classes of size $u$, the count is a finite computation. We implemented it twice in exact arithmetic.
- *108 vertices (Section 5).* For $(108,40,35,14,15)$ the count leaves exactly two squares compatible with a group acting regularly on each layer, both with $m=3$. One is a reversible Menon difference set, which must avoid the identity. The other is $Y^2=9-H+4K$ with $|H|=9$, and then $1\in Y$ and $|X\cap H|=7$ (Corollary 8). For $K=S_3\times S_3$ an exact enumeration shows that these two squares give exactly the graph $\Gamma$ of paper 87 [4], two further graphs $\Gamma'$ and $\Gamma''$, and their converses (Theorem 11).
- *Open parameter sets (Section 6).* Take the 574 parameter sets with $v\le110$ that were open on 2 November 2026. For none of them does a dsrg of the form (1) exist with $Y$ symmetric and $Y^2\in\operatorname{span}(I,J)$, for any $m$, over any group or none (Theorem 12). For squares $oI+bN+cJ$ with $b\ne0$, the count excludes 1939 of the 2308 candidate entries outright, and a further 356 for Cayley constructions (Proposition 13).

These results restrict one construction class. They do not show that any parameter set is unrealisable.

## 2. The layer identities

**Lemma 1.** Let $A$ be as in (1). Then $A^2=tI+\lambda A+\mu(J-I-A)$ if and only if
$$XY+YX=\beta Y+\mu J-(m-2)Y^2,\tag{L1}$$
$$X^2=(t-\mu)I+\beta X+\mu J-(m-1)Y^2.\tag{L2}$$

*Proof.* Since $(J_m-I_m)^2=(m-2)(J_m-I_m)+(m-1)I_m$,
$$A^2=I_m\otimes\big(X^2+(m-1)Y^2\big)+(J_m-I_m)\otimes\big(XY+YX+(m-2)Y^2\big).$$
The right side of the dsrg identity equals $(t-\mu)I+\beta A+\mu J=I_m\otimes\big((t-\mu)I+\beta X+\mu J\big)+(J_m-I_m)\otimes(\beta Y+\mu J)$. For $m\ge2$ the two sides agree exactly when their diagonal blocks agree and their off-diagonal blocks agree. $\square$

This is the criterion of [3, Theorem 4], written in $X$ and $Y$ rather than in $X-Y$ and $X+(m-1)Y$.

**Standing assumptions.** From now on $A$ is the adjacency matrix of a dsrg$(v,k,t,\lambda,\mu)$ of the form (1) with $\mu\ge1$, and $Y$ is symmetric with constant row sums $y$. Constant row sums are automatic when $Y^2$ has constant diagonal, because $(Y^2)_{ii}$ is the $i$-th row sum of a symmetric zero-one matrix. This covers every square used below.

**Lemma 2.** (a) $XJ=JX=k_XJ$ with $k_X=k-(m-1)y$. (b) $y\ge1$ and $k-my\in\{r,s\}$. (c) $(X^2)_{ii}=t-(m-1)y$ for every $i$.

*Proof.* (a) Rows and columns of $A$ have sum $k$, and the row and column sums of $Y$ are $y$. (b) If $y=0$, two vertices in different layers are non-adjacent and have no common out-neighbour, against $\mu\ge1$. For $u\perp\mathbf 1_m$ we have $A(u\otimes w)=u\otimes(X-Y)w$, so on these vectors the dsrg identity says $(X-Y-r)(X-Y-s)=0$. Since $(X-Y)\mathbf 1=(k-my)\mathbf 1$, the number $k-my$ is a root of $(x-r)(x-s)$. (c) Take the diagonal of (L2) and use $(Y^2)_{ii}=y$. $\square$

## 3. The trace count

Let $\mathbf 1^\perp$ be the orthogonal complement of the all-one vector in $\mathbb R^n$. $Y$ is symmetric and $Y\mathbf 1=y\mathbf 1$, so $Y$ preserves $\mathbf 1^\perp$ and is diagonalisable there. For a real $\theta$ let $E_\theta\subseteq\mathbf 1^\perp$ be the $\theta$-eigenspace of $Y$ (possibly $0$) and $P_\theta$ the orthogonal projection onto it. For $q\ge0$ let $F_q=E_{\sqrt q}+E_{-\sqrt q}$ be the $q$-eigenspace of $Y^2$ on $\mathbf 1^\perp$, and write $e^\pm_q=\dim E_{\pm\sqrt q}$ for $q>0$.

**Theorem 3.** Under the standing assumptions:
(a) $X$ commutes with $Y^2$, and $X$ preserves $\mathbf 1^\perp$ and each $F_q$.
(b) For $\theta\ne0$, $P_\theta XP_\theta=\tfrac12\big(\beta-(m-2)\theta\big)P_\theta$.
(c) For $\theta\ne0$, $P_0XP_\theta=P_\theta XP_0=0$.
(d) Let $q>0$, and write the restriction of $X$ to $F_q=E_{\sqrt q}\oplus E_{-\sqrt q}$ in block form $\begin{pmatrix}\alpha I&B\\ C&\alpha'I\end{pmatrix}$, where $\alpha=\tfrac12(\beta-(m-2)\sqrt q)$ and $\alpha'=\tfrac12(\beta+(m-2)\sqrt q)$ by (b). Then
$$BC=\omega I,\qquad CB=\omega I,\qquad \omega=\tfrac14\big((r-s)^2-m^2q\big).$$
In particular, if $m\sqrt q\ne r-s$, then $e^+_q=e^-_q$.
(e) On $F_0$, $Y=0$, and $X$ restricted to $F_0$ has all its eigenvalues in $\{r,s\}$.

*Proof.* (a) By (L1), and since $Y$ commutes with $Y^2$,
$$XY^2-Y^2X=(XY+YX)Y-Y(XY+YX)=\mu(JY-YJ)=0.$$
$X$ preserves $\mathbf 1^\perp$ because $JX=k_XJ$ (Lemma 2), so it preserves the eigenspaces of $Y^2$ there.

(b), (c) Let $u\in E_\theta$ and $w\in E_{\theta'}$. Since $Y$ is symmetric, $\langle w,(XY+YX)u\rangle=(\theta+\theta')\langle w,Xu\rangle$. By (L1) and $Ju=0$ this equals $\theta(\beta-(m-2)\theta)\langle w,u\rangle$. For $\theta'=\theta\ne0$ this is (b). For $\theta\ne0=\theta'$ we have $\langle w,u\rangle=0$ and so $\langle w,Xu\rangle=0$, which is $P_0XP_\theta=0$. The case $\theta=0\ne\theta'$ gives $\theta'\langle w,Xu\rangle=0$, which is $P_{\theta'}XP_0=0$.

(d) On $\mathbf 1^\perp$, (L2) reads $X^2=(t-\mu)I+\beta X-(m-1)Y^2$, so on $F_q$ it reads $X^2=(t-\mu-(m-1)q)I+\beta X$. The $(1,1)$ block gives $\alpha^2+BC=t-\mu-(m-1)q+\beta\alpha$, so $BC=(t-\mu-(m-1)q+\alpha\alpha')I$, using $\beta-\alpha=\alpha'$. Now $4\alpha\alpha'=\beta^2-(m-2)^2q$, and $4(m-1)+(m-2)^2=m^2$, so $4(t-\mu-(m-1)q+\alpha\alpha')=\beta^2+4(t-\mu)-m^2q=(r-s)^2-m^2q$. The $(2,2)$ block gives $CB=\omega I$ in the same way. If $\omega\ne0$, then $B:E_{-\sqrt q}\to E_{\sqrt q}$ and $C:E_{\sqrt q}\to E_{-\sqrt q}$ satisfy $BC=\omega I$ and $CB=\omega I$, so both are bijective and the two dimensions agree. Since $r-s>0$, $\omega=0$ means $m\sqrt q=r-s$.

(e) $Y$ is symmetric and $Y^2=0$ on $F_0$, so $Y=0$ there. By (a) and (L2), $X^2=(t-\mu)I+\beta X$ on $F_0$, so every eigenvalue of $X$ on $F_0$ is a root of $(x-r)(x-s)$. $\square$

Only (L1) is used in (a)–(c). The matrix $X$ is not assumed symmetric or normal, and its blocks $B$ and $C$ need not be related.

**Corollary 4 (the count).** Let $Q^+$ be the set of $q>0$ with $F_q\ne0$, put $d_q=e^+_q-e^-_q$ and $d_0=\dim F_0$. Then
$$a=y+\sum_{q\in Q^+}\sqrt q\,d_q,\qquad (m-2)(a-y)=2k_X+\beta(n-1-d_0)+2\big(rf+s(d_0-f)\big)\tag{2}$$
for some integer $f$ with $0\le f\le d_0$. Moreover $d_q\equiv\dim F_q\pmod 2$ and $|d_q|\le\dim F_q$ for each $q\in Q^+$, and $d_q=0$ unless $m\sqrt q=r-s$. In particular, if $Y^2$ is nonsingular on $\mathbf 1^\perp$, then $(m-2)(a-y)=2k_X+\beta(n-1)$: for $m\ge3$ this determines $a$, and for $m=2$ it requires $2k_X+\beta(n-1)=0$.

*Proof.* $\mathbb R^n=\langle\mathbf 1\rangle\oplus\bigoplus_qF_q$, and $X$ and $Y$ preserve every summand (Theorem 3(a)). On $\langle\mathbf 1\rangle$, $Y=y$ and $X=k_X$. On $F_q$ with $q>0$, $\operatorname{tr}Y=\sqrt q\,d_q$ and, by Theorem 3(b), $\operatorname{tr}X=\alpha e^+_q+\alpha'e^-_q=\tfrac12\beta\dim F_q-\tfrac12(m-2)\sqrt q\,d_q$. On $F_0$, $\operatorname{tr}Y=0$ and $\operatorname{tr}X=rf+s(d_0-f)$ by Theorem 3(e). Now add up, use $\operatorname{tr}X=0$ and $\sum_{q>0}\dim F_q=n-1-d_0$. The last claims are Theorem 3(d). $\square$

**Corollary 5 (Cayley constructions).** Let $K$ be a group of order $n$, and for $Z\subseteq K$ let $A_Z$ be the $K\times K$ matrix whose $(x,z)$ entry is $1$ if $zx^{-1}\in Z$. Suppose $X=A_{X_0}$ and $Y=A_{Y_0}$ with $Y_0=Y_0^{-1}$; then (1) is the Cayley digraph of $\mathbb Z_m\times K$ with connection set $\{0\}\times X_0\cup(\mathbb Z_m\setminus\{0\})\times Y_0$. In this case:
(a) $a=n$ if $1\in Y_0$ and $a=0$ otherwise.
(b) If $Y_0^2=o+bH+cK$ in $\mathbb Z[K]$ for a subgroup $H$ of order $u$, then $Y^2=oI+bN+cJ$, where $N$ is the relation "same right coset of $H$". Let $W$ be the space of vectors constant on these cosets. If $b\ne0$, then $X$ preserves $W$, and the trace of $X$ on $W$ is $(n/u)\,|X_0\cap H|$.

*Proof.* (a) The diagonal entry of $A_{Y_0}$ is $[1\in Y_0]$. (b) $A_ZA_{Z'}=A_{Z'Z}$, so $Y^2=A_{Y_0^2}$, and $A_H$ is the relation $zx^{-1}\in H$, that is, $Hz=Hx$. For $b\ne0$, $N=(Y^2-oI-cJ)/b$, so it commutes with $X$ by Theorem 3(a), and $X$ preserves $W=\operatorname{im}N$. The orthogonal projection onto $W$ is $N/u$, so the trace of $X$ on $W$ is $\operatorname{tr}(XN)/u$. Each vertex $x$ has $|X_0\cap H|$ out-neighbours in its own coset $Hx$, so $\operatorname{tr}(XN)=n|X_0\cap H|$. $\square$

## 4. Squares in $\operatorname{span}(I,N,J)$

### 4.1 The census

Fix a parameter set with integral $r,s$. We consider realisations of (1) under the standing assumptions with
$$Y^2=oI+bN+cJ,\tag{3}$$
where $N$ is the relation "same class" of a partition of the $n$ points into $n/u$ classes of size $u$. The case $u=1$, $b=0$ is the *difference-set slice*: $Y^2=oI+cJ$. The case $1<u<n$, $b\ne0$ is the *cover slice*. The partition and $N$ are part of the slice; they are not forced by the dsrg.

**Lemma 6.** A realisation with (3) has an *entry* $(m,y,o,b,c,u)$ with the following properties:
1. $m\mid v$, $n=v/m\ge2$, $k-my\in\{r,s\}$, $1\le y\le n$, $0\le k_X\le n-1$ and $0\le t-(m-1)y\le k_X$;
2. $o+b+c=y$ and $o+bu+cn=y^2$;
3. $c\ge0$, $0\le b+c\le y$, $o\ge0$ and $o+bu\ge0$;
4. if $u>1$ and $o+bu=0$, then $n\mid uy$; if $u>1$ and $o=0$, then $u\mid y$.

*Proof.* (1) is Lemma 2, $k_X$ being the degree of the loopless zero-one matrix $X$ and $t-(m-1)y$ the number of reciprocated out-arcs at a vertex of $X$. (2) compares the diagonal of $Y^2$ and its row sums. (3) The entries of $Y^2$ count common neighbours, so they lie in $[0,y]$. Its eigenvalues $o$ (on $W^\perp$, with $W$ the class-constant vectors) and $o+bu$ (on $W\cap\mathbf 1^\perp$) are squares of real eigenvalues of $Y$. (4) If $o+bu=0$, then $Y=0$ on $W\cap\mathbf 1^\perp$ (Theorem 3(e)), so $Y$ maps the indicator of a class to a multiple of $\mathbf 1$: each point has $uy/n$ neighbours in each class. If $o=0$, then $Y=0$ on $W^\perp$, so $Y$ is constant on the blocks of the partition, and $y$ is a multiple of $u$. $\square$

The *census* of a parameter set is the list of all $(m,y,o,b,c,u)$ satisfying Lemma 6. For each entry, Corollary 4 becomes a finite test. In the difference-set slice, $\mathbf 1^\perp=F_o$. In the cover slice, $\mathbf 1^\perp=F_o\oplus F_{o+bu}$ with $F_o=W^\perp$ of dimension $n-n/u$ and $F_{o+bu}=W\cap\mathbf 1^\perp$ of dimension $n/u-1$, and $X$ preserves $W$ by Theorem 3(a). Write $\operatorname{tr}Q$ for the trace of $X$ on $W$; it is the trace of the quotient matrix $Q$ of $X$ with respect to the partition, whose diagonal entries count out-neighbours inside the own class, so $0\le\operatorname{tr}Q\le(n/u)\min(k_X,u-1)$.

**Definition.** An entry is *admitted* by the count if there are integers $d_q$ (or $f$, when $q=0$) for the at most two spaces $F_q$, subject to the parity, range and $\omega$ conditions of Corollary 4, such that $\operatorname{tr}X=0$ holds exactly, $a$ is an integer in $[0,n]$, and, in the cover slice, $\operatorname{tr}Q=k_X+\operatorname{tr}(X|F_{o+bu})$ is an integer in $[0,(n/u)\min(k_X,u-1)]$. It is *excluded* otherwise. An admitted entry is *Cayley-compatible* if some admitted choice has $a\in\{0,n\}$ and $(n/u)\mid\operatorname{tr}Q$ (Corollary 5); otherwise it is *non-Cayley only*.

The arithmetic is exact in $\mathbb Q(\sqrt{q_1},\sqrt{q_2})$: we write $q=s_q^2q'$ with $q'$ squarefree and collect the coefficient of each $\sqrt{q'}$. Since $a$ and $\operatorname{tr}X$ are rational, every coefficient with $q'>1$ must vanish.

By Lemma 6 and Corollaries 4 and 5, an excluded entry has no realisation, and a non-Cayley-only entry has no realisation of the form of Corollary 5 with $H$ the partition.

### 4.2 Implementations and checks

`layer_count.py` (standard library, `fractions`) lists the census, evaluates the count, and checks five known layered dsrgs: their entry must be in the census, and their actual $(a,\operatorname{tr}Q)$ must be admitted. The controls are a dsrg$(18,4,3,0,1)$ with $m=3$ ($a=0$), a dsrg$(24,10,8,4,4)$ with $m=2$ and $u=4$ ($a=12=n$, $\operatorname{tr}Q=0$), and the three graphs $\Gamma,\Gamma',\Gamma''$ of Section 5 ($a=36$, $\operatorname{tr}Q=28$ for $\Gamma$ and $\Gamma'$; $a=0$ for $\Gamma''$). `count_check.py` is a second implementation: it uses sympy surds, loops over the census variables in a different order, enumerates $e^+_q$ directly instead of $d_q$, and compares every admitted set with the output of the first program. They agree on all 2365 entries of the open parameter sets.

As a further check of the theorem itself, we ran a CP-SAT model of (L1), (L2) and (3) with $X$, $Y$ and $a$ free and none of the implied constraints of Theorem 3, on the 132 cover entries with $n\le10$ of parameter sets where dsrgs are known. Every entry that the count excludes was infeasible, and the 9 solutions found all had admitted values of $(a,\operatorname{tr}Q)$.

## 5. The parameter set $(108,40,35,14,15)$

Here $\beta=-1$, $t-\mu=20$, $r=4$, $s=-5$ and $r-s=9$. Paper 87 [4] constructs a dsrg$(108,40,35,14,15)$ $\Gamma$ of the form (1) with $m=3$ and a symmetric $Y$. This section asks which constructions of this kind exist when $Y^2\in\operatorname{span}(I,N,J)$.

### 5.1 What the count allows

**Proposition 7.** The census of $(108,40,35,14,15)$ has 16 entries. The count admits exactly the following, listed with their admitted values of $(a,\operatorname{tr}Q)$:

| $m$ | $(y,o,b,c,u)$ | square | admitted $(a,\operatorname{tr}Q)$ | Cayley-compatible |
|---|---|---|---|---|
| 3 | $(15,9,0,6,1)$ | $9I+6J$ | $(0,-)$ | $(0,-)$ |
| 3 | $(12,9,-1,4,9)$ | $9I-N+4J$ | $(0,10),(18,19),(36,28)$ | $(36,28)$ |
| 2 | $(18,18,-6,6,3)$ | $18I-6N+6J$ | $(18,18)$ | none |
| 2 | $(18,0,18,0,18)$ | $18N$ | $(18,21)$ | none |
| 4 | $(9,9,-3,3,3)$ | $9I-3N+3J$ | $(9,9)$ | none |
| 4 | $(9,0,9,0,9)$ | $9N$ | $(9,12)$ | none |

The other 10 entries, with $m\in\{3,6,9,12\}$, are excluded.

*Proof.* `layer_count.py` and `count_check.py`. For the first row, (2) with $d_0=0$ gives $a-15=2\cdot10-35$, so $a=0$. For the second, $k_X=16$, $F_9=W^\perp$ has dimension 32 and $F_0=W\cap\mathbf 1^\perp$ has dimension 3. Since $3\sqrt9=9=r-s$, we have $\omega=0$ on $F_9$, so $d_9$ is not forced to vanish, and $a=12+3d_9$. Formula (2) gives $a-12=32-32+2\big(4f-5(3-f)\big)=18f-30$. With $0\le a\le36$ this leaves $f\in\{1,2,3\}$, $a\in\{0,18,36\}$ and $d_9\in\{-4,2,8\}$, and $\operatorname{tr}Q=k_X+4f-5(3-f)=1+9f$. $\square$

**Corollary 8.** Let $\Delta$ be a dsrg$(108,40,35,14,15)$ of the form of Corollary 5 over a group $K$, with $Y_0=Y_0^{-1}$ and $Y_0^2\in\operatorname{span}(1,H,K)$ for a subgroup $H$ of $K$. Then $m=3$, $|K|=36$, and one of the following holds:
(a) $Y_0$ is a $(36,15,6)$ difference set with $Y_0=Y_0^{-1}$ and $1\notin Y_0$;
(b) $|H|=9$, $Y_0^2=9-H+4K$, $1\in Y_0$ and $|X_0\cap H|=7$.
The same holds for the complement $(108,67,62,41,42)$ with $Y_0$ replaced by $K-Y_0$.

*Proof.* By Corollary 5 the entry of $\Delta$ is Cayley-compatible with the actual $(a,\operatorname{tr}Q)$, and $\operatorname{tr}Q=(n/u)|X_0\cap H|=4|X_0\cap H|$ in case (b). The complement of (1) is $I_m\otimes(J-I-X)+(J_m-I_m)\otimes(J-Y)$, and $(J-Y)^2=Y^2+(n-2y)J$. $\square$

So the count, without any group, recovers two facts that paper 87 observed in $S_3\times S_3$: every graph there with $Y^2=9+6J$ has $1\notin Y_0$, and every set with $Y^2=9-R+4K$ contains $1$. The value $|X_0\cap H|=7$ matches the layer sets of $\Gamma$ and $\Gamma'$ below.

### 5.2 Three graphs

Let $K=S_3\times S_3$ and $G=\mathbb Z_3\times K$. Let $R=A_3\times A_3\cong\mathbb F_3^2$, written additively, with $(i,j)$ standing for $a^ib^j$, $a=((123),1)$, $b=(1,(123))$. Let $s=((23),1)$, $t=(1,(23))$ and $L=\{1,s,t,st\}\cong C_2^2$. Then $K=R\rtimes L$, and every $Z\subseteq K$ is $Z=\sum_{h\in L}Z_hh$ with $Z_h\subseteq R$. Define
$$T_1=\{(i,i)\},\quad T_s=\{(0,j)\},\quad T_t=\{(i,0)\},\quad T_{st}=\{(i,-i)\}\qquad(i,j\in\mathbb F_3),$$
the four lines through $0$ of $\mathrm{AG}(2,3)$, and put $T=\sum_hT_hh$ and $T''=T+R-2T_1$, so that $T''_1=R\setminus T_1$ and $T''_h=T_h$ for $h\ne1$. Both sets are closed under inversion, $1\in T$ and $1\notin T''$.

**Lemma 9.** In $\mathbb Z[K]$, $T^2=9-R+4K$ and $T''^2=9+6K$.

*Proof.* For two lines $L_1\ne L_2$ through $0$, $L_1L_2=R$ in $\mathbb Z[R]$, and $L_1^2=3L_1$. Conjugation by $h\in L$ maps lines through $0$ to lines through $0$ and fixes $T_h$. In $T^2=\sum_{h,h'}T_h\,{}^hT_{h'}\,hh'$ the terms with $h'=h$ give $\sum_h3T_h=3(R+3)$, since the four lines cover each nonzero point once and $0$ four times. For $h'=hg$ with $g\ne1$, ${}^hT_{hg}\ne{}^hT_h=T_h$, so each term is $Rg$, and the four terms for a fixed $g$ give $4Rg$. Hence $T^2=9+3R+4R(s+t+st)=9-R+4K$. For $T''$ put $E=R-2T_1$. Then $E^2=12T_1-3R$, and $T_1T=TT_1=3T_1+K-R$ by the same line count, so $TE=ET=3K-2(3T_1+K-R)=K+2R-6T_1$, using $TR=RT=3K$. Adding, $T''^2=(9-R+4K)+2(K+2R-6T_1)+(12T_1-3R)=9+6K$. $\square$

So $T$ is a divisible difference set relative to $R$, and $T''$ is a reversible Menon difference set [9]. The layer sets $S_0$, $S_0'$ and $S_0''$ are listed in Appendix A; in coordinates, $(S_0)_1=R\setminus\{0,(1,1)\}$ and $(S_0')_1=R\setminus\{0,(2,2)\}$, so $|S_0\cap R|=|S_0'\cap R|=7$. Let
$$\Gamma=\mathrm{Cay}\big(G,\{0\}\times S_0\cup\{1,2\}\times T\big),\quad \Gamma'=\mathrm{Cay}\big(G,\{0\}\times S_0'\cup\{1,2\}\times T\big),\quad \Gamma''=\mathrm{Cay}\big(G,\{0\}\times S_0''\cup\{1,2\}\times T''\big).$$
$\Gamma$ is the graph of paper 87 [4].

**Theorem 10.** $\Gamma'$ and $\Gamma''$ are dsrg$(108,40,35,14,15)$, and their complements are dsrg$(108,67,62,41,42)$. No two of $\Gamma,\Gamma',\Gamma''$ are isomorphic, and none of them is isomorphic to the converse of another. The layer $\mathrm{Cay}(K,S_0'')$ of $\Gamma''$ is a dsrg$(36,10,5,2,3)$; the layers of $\Gamma$ and $\Gamma'$ are not dsrgs.

*Proof.* By Lemma 1 for the Cayley matrices (or the group-ring form [4, Lemma 4]), each graph is a dsrg if and only if (L1) and (L2) hold in $\mathbb Z[K]$ with $(X,Y)=(S_0',T)$, $(S_0'',T'')$. Three scripts that share no code check this: `groupring108.py` in $\mathbb Z[K]$ and $\mathbb Z[G]$, `verify108.py` by all two-walk counts of the $108\times108$ matrices and their complements, and `chars108.py` on the nine irreducible representations of $K$. For a digraph $\Delta$ let $U(\Delta)$ be the undirected graph of its reciprocated arcs. Then $U(\Delta^{\mathsf T})=U(\Delta)$, and an isomorphism of digraphs is one of their $U$'s. The graphs $U(\Gamma)$, $U(\Gamma')$ and $U(\Gamma'')$ are 35-regular, vertex-transitive, and have 189, 186 and 180 triangles through each vertex (`third108.py`). The statement about the layers is the two-walk count of `second108.py` and `third108.py`. $\square$

pynauty [10] (`aut108.py`, ancillary) shows in addition that none of the three graphs is isomorphic to its own converse, so they give six isomorphism classes, with $|\mathrm{Aut}(\Gamma)|=|\mathrm{Aut}(\Gamma')|=432$ and $|\mathrm{Aut}(\Gamma'')|=216$. This last fact is not checked independently.

### 5.3 Classification in $S_3\times S_3$

**Theorem 11.** Let $K=S_3\times S_3$, let $X_0,Y_0\subseteq K$ with $Y_0=Y_0^{-1}$ and $Y_0^2\in\operatorname{span}(1,H,K)$ in $\mathbb Z[K]$ for some subgroup $H$, and suppose that $\mathrm{Cay}(\mathbb Z_3\times K,\{0\}\times X_0\cup\{1,2\}\times Y_0)$ is a dsrg$(108,40,35,14,15)$. Then it is isomorphic to $\Gamma$, $\Gamma'$, $\Gamma''$ or one of their converses. More precisely:
(a) $K$ has exactly 240 inverse-closed $(36,15,6)$ difference sets, in 9 orbits under $\mathrm{Aut}(K)$; 180 of them contain $1$. Only the orbit of $T''$ (size 18) admits a layer set, and for $Y_0=T''$ exactly 8 sets $X_0$ work. They form one orbit under the 4 automorphisms of $K$ fixing $T''$ together with $X_0\mapsto X_0^{-1}$.
(b) $K$ has exactly 60 inverse-closed sets with $Y_0^2=9-R+4K$, all containing $1$, in 3 orbits. Only the orbit of $T$ (size 18) admits a layer set, and for $Y_0=T$ exactly 8 sets $X_0$ work. They form two orbits of size 4, containing $S_0$ and $S_0'$.

*Proof.* By Corollary 8 the square is $9+6K$ or $9-H+4K$ with $|H|=9$; the only subgroup of order 9 of $K$ is its normal Sylow subgroup $R$. `third108.py` lists the inverse-closed subsets of size 15 and 12 with these squares by backtracking over the pairs $\{g,g^{-1}\}$, discarding a partial set once a coefficient of its square off the identity exceeds its target; coefficients only grow, so the lists are complete. An automorphism $\varphi$ of $K$ induces $(c,x)\mapsto(c,\varphi(x))$ on $G$ and maps solutions for $Y_0$ to solutions for $\varphi(Y_0)$ with isomorphic graphs, so one $Y_0$ per orbit suffices. Since $Y_0=Y_0^{-1}$, the map $X_0\mapsto X_0^{-1}$ passes to the converse graph. For each orbit representative the script solves (L1), which is linear in $X_0$ once $Y_0$ is fixed, in exact rational arithmetic with the coefficient of $1$ in $X_0$ set to $0$, runs through all values of the free coordinates, and tests (L2) on each zero-one solution:

| square | orbit size | $1\in Y_0$ | (L1) | zero-one solutions | satisfying (L2) |
|---|---|---|---|---|---|
| $9+6K$ | 6 | no | rank 30, 6 free | 0 | 0 |
| | 18 ($T''$) | no | rank 22, 14 free | 112 | 8 |
| | 36 | no | rank 22, 14 free | 16 | 0 |
| | 6, 12, 18, 36, 36, 72 | yes | inconsistent | – | – |
| $9-R+4K$ | 6 | yes | rank 28, 8 free | 0 | 0 |
| | 18 ($T$) | yes | rank 20, 16 free | 112 | 8 |
| | 36 | yes | rank 20, 16 free | 16 | 0 |

The six orbits with $1\in Y_0$ in the first block are excluded by Corollary 8(a) as well as by the inconsistency of (L1). The orbit statements for the 8 solutions are computed by the same script. $\square$

Theorem 11 is restricted to $K=S_3\times S_3$. For the other 13 groups of order 36 we have only incomplete CP-SAT searches (Appendix B), which give no statement.

## 6. The difference-set slice on the open parameter sets

We use the list of 574 parameter sets with $v\le110$ that the rStation ledger and the Hobart–Brouwer table [2] listed as open on 2 November 2026; it is the list of paper 88 [5], and it is included as `open_rows.json`. Every set on it has $\mu\ge1$ and $t<k$.

**Theorem 12.** Let $(v,k,t,\lambda,\mu)$ be one of these 574 parameter sets and $m\ge2$ a divisor of $v$ with $v/m\ge2$. There are no zero-one matrices $X$, $Y$ with $\operatorname{diag}X=0$, $Y$ symmetric and $Y^2\in\operatorname{span}(I,J)$ such that $I_m\otimes X+(J_m-I_m)\otimes Y$ is a dsrg$(v,k,t,\lambda,\mu)$.

*Proof.* $Y^2=oI+cJ$ has constant diagonal, so the standing assumptions hold, and by Lemma 6 the realisation has a census entry with $u=1$. The censuses of the 574 sets contain 57 such entries. Both implementations of Section 4.2 find that the count excludes 51 of them. The remaining six are handled as follows (`ds_slice.py` checks each arithmetic step):

(a) $(63,38,32,22,24)$ with $m=9$, and $(110,25,21,4,6)$ with $m=22$. Here $k_X=n-1$, so $X=J-I$, and the diagonal of $X^2$ is $n-1$. Lemma 2(c) requires it to be $t-(m-1)y=0$.

(b) $(63,18,14,5,5)$ with $m=3$, $(y,o,c)=(5,4,1)$. The count admits only $a=n=21$. So $Y=I+Z$ with $Z$ symmetric, zero-one and zero on the diagonal, and $Y^2=I+2Z+Z^2=4I+J$ gives $Z^2=3I+J-2Z$. On an edge of $Z$ the right side is $-1$, which is impossible. ($Z\ne0$, since $y=5$.)

(c) $(45,18,16,7,7)$ with $m=3$, $(y,o,c)=(7,4,3)$. Again only $a=n=15$ is admitted. Writing $Y=I+Z$, we get $Z^2=6I+Z+3(J-I-Z)$, so $Z$ is an srg$(15,6,1,3)$. Its complement is an srg$(15,8,4,4)$, which is the triangular graph $T(6)$ by the uniqueness of triangular graphs for $n\ne8$ [6, 7]. So $Z$ is unique up to isomorphism, and we may take $Y=I+Z$ to be the matrix of the symplectic polarity of $\mathrm{PG}(3,2)$: points are the nonzero vectors of $\mathbb F_2^4$ and $Y_{pq}=1$ if $p$ and $q$ are orthogonal for a nondegenerate alternating form. Relabelling the points by one permutation in all layers preserves (L1) and (L2), so this choice loses no realisation. By Lemma 1, $X$ must then be a zero-one matrix with zero diagonal, row and column sums $4$, $X^2=I+J$ and $XY+YX=4(J-I)$. Two exact searches find no such $X$. `ex_layer.py` is a generic row-by-row backtracking over the $4$-subsets for each row, with no symmetry reduction; every partial count in $X^2$, $XY+YX$ and the column sums only grows as rows are added, so a branch is cut only when a count exceeds its target, and the search is complete. It visits 589,357 nodes and finds 0 solutions in about 30 minutes. `ex45.py` is a second implementation that also fixes row 0 up to the stabiliser of a point in $\mathrm{Sp}(4,2)$, which preserves $Y$; it finds 0 solutions. As a positive control, `ex_layer.py` finds all 16 layers $X$ for the $Y$ of a layered dsrg$(18,4,3,0,1)$ with $m=3$, each confirmed by the full check of $A^2$. `ex45.py` is written for this $Y$ only and has no positive control of its own; its role is to agree with `ex_layer.py`.

(d) $(45,26,24,14,16)$ and $(63,44,40,30,32)$, both with $m=3$ and admitted $a=0$ only. The complement of (1) is $I_m\otimes(J-I-X)+(J_m-I_m)\otimes(J-Y)$, and $J-Y$ is symmetric with $(J-Y)^2=oI+(c+n-2y)J$. So a realisation of either set gives a realisation of its complement, $(45,18,16,7,7)$ or $(63,18,14,5,5)$, in the difference-set slice, which (b) and (c) exclude. $\square$

The theorem allows any group or none, and any $m$. For comparison, the Menon square $9I+6J$ does occur for $(108,40,35,14,15)$, which is not on the list (Section 5).

## 7. The cover slice on the open parameter sets

**Proposition 13.** The censuses of the 574 open parameter sets contain 2308 cover entries ($b\ne0$, $1<u<n$). The count excludes 1939 of them. Of the remaining 369, 356 are non-Cayley only and 13 are Cayley-compatible. Hence, for an open parameter set, a dsrg of the form of Corollary 5 with $Y_0^2=o+bH+cK$, $b\ne0$, $1<|H|<n$, must have one of the 13 entries of Table 2.

*Proof.* The counts are those of `layer_count.py` and `count_check.py`, which agree. The consequence is Corollary 5. $\square$

**Table 2.** The 13 Cayley-compatible cover entries, with the admitted Cayley value of $(a,\operatorname{tr}Q)$.

| parameter set | $m$ | $n$ | $(y,o,b,c,u)$ | $(a,\operatorname{tr}Q)$ |
|---|---|---|---|---|
| $(54,15,13,4,4)$ | 2 | 27 | $(9,9,-3,3,3)$ | $(27,0)$ |
| $(54,38,36,26,28)$ | 2 | 27 | $(18,9,-3,12,3)$ | $(0,18)$ |
| $(63,24,18,9,9)$ | 3 | 21 | $(9,4,2,3,7)$ | $(21,6)$ |
| $(63,38,32,22,24)$ | 3 | 21 | $(12,4,2,6,7)$ | $(0,12)$ |
| $(75,57,50,43,44)$ | 5 | 15 | $(11,4,-1,8,3)$ | $(15,5)$ |
| $(75,57,50,43,44)$ | 5 | 15 | $(11,1,3,7,5)$ | $(15,12)$ |
| $(99,30,18,9,9)$ | 3 | 33 | $(9,4,4,1,11)$ | $(33,12)$ |
| $(99,62,48,38,40)$ | 3 | 33 | $(20,10,-2,12,3)$ | $(0,22)$ |
| $(99,68,56,46,48)$ | 3 | 33 | $(24,4,4,16,11)$ | $(0,18)$ |
| $(108,30,27,6,9)$ | 9 | 12 | $(3,1,2,0,4)$ | $(0,3)$ |
| $(108,31,29,8,9)$ | 3 | 36 | $(9,6,1,2,3)$ | $(0,12)$ |
| $(108,76,74,53,54)$ | 3 | 36 | $(27,6,1,20,3)$ | $(36,12)$ |
| $(108,77,74,55,54)$ | 9 | 12 | $(9,1,2,6,4)$ | $(12,6)$ |

Five entries have $n\in\{15,33\}$. Every group of order 15 or 33 is cyclic, and $\mathbb Z_m\times K$ is then abelian. A Cayley digraph of an abelian group has a normal adjacency matrix (it commutes with its transpose, the Cayley matrix of the inverse set), and a normal matrix with real eigenvalues is symmetric, so $t=k$. All open sets have $t<k$, so these five entries have no Cayley realisation. For the other eight we have computations only, described in Appendix B; none found a graph.

The 356 non-Cayley-only entries and the 13 above are where a realisation of (3) could still exist. Our group-free searches on them found nothing, but Appendix B explains why that null is weak for $m\ge3$.

## 8. Related work

- The layered form (1) appears in many rStation constructions. Paper 43 [3, Theorem 4] states the general criterion, which Lemma 1 rewrites. Paper 4 [8] builds group-free layered dsrgs from equitable partitions and opposite eigenspaces; there the cross blocks multiply to constants, which is the case $Y^2\in\operatorname{span}(J)$, $o=0$, of our setting. Paper 82 [11] linearises the block equations for fixed signs in the same way that (L1) is linear in $X$ for fixed $Y$, which is how Theorem 11 is proved. Paper 36 [12] decomposes incidence structures of divisible designs. The count of Section 4 can be placed in front of searches of these kinds as a filter.
- Paper 87 [4] constructs $\Gamma$. The graphs $\Gamma'$ and $\Gamma''$, Lemma 9 for $T''$ and the classification of Theorem 11 appear here for the first time; the referee of a revision of [4] asked for them to form a separate paper.
- Trace arguments of the same kind are classical for automorphisms of strongly regular graphs and generalised quadrangles (Benson [13]; De Winter, Kamischke and Wang [14]) and appear for induced subgraphs of dsrgs in paper 43 [3, Section 6(d)] and paper 88 [5]. The square $Y^2=oI+bN+cJ$ is the square of a divisible design graph; Muzychuk and Ryabov [15] construct dsrgs and divisible design graphs from fusions of the same association schemes. We searched the local full texts of these papers and of papers 4, 36, 43 and 82, and arXiv, for absolute points of the between-layer block or a trace count for the layered form, and found neither. This is a search of a limited set of sources, not a proof of priority.

## 9. Limitations

- Theorems 3 and 12 and Corollaries 4, 5 and 8 assume that the same symmetric $Y$ joins every pair of layers. Layered graphs with different or non-symmetric between-layer blocks are not covered.
- Theorem 12 covers only $Y^2\in\operatorname{span}(I,J)$. For the cover slice, Proposition 13 and Table 2 restrict realisations but leave 369 entries undecided, 13 of them for Cayley constructions.
- The partition $N$ in (3) is part of the slice. A symmetric $Y$ whose square has more than three distinct values is not covered.
- Theorem 11 is restricted to $K=S_3\times S_3$. The facts that the three graphs are not self-converse and the orders of their automorphism groups rest on pynauty alone.
- The open list is the 2 November 2026 snapshot of [5].

## 10. Reproducibility

The supplement contains the following programs (Python 3; standard library unless stated) and their inputs.
- `layer_count.py` (Sections 4 and 6, Proposition 7, Proposition 13): census, count, five controls; writes `count_open.json`; about 1 s. Run `verify108.py` first, which writes the three graphs it uses as controls.
- `count_check.py` (sympy): second implementation; compares with `count_open.json`; about 10 s.
- `ds_slice.py` (numpy for `.npy` output): the six cases of Theorem 12; writes `Y45.npy` and the control inputs for `ex_layer.py`.
- `ex_layer.py` (numpy): `python3 ex_layer.py 45_18_16_7_7 3 Y45.npy` (about 30 min, 0 solutions); control `python3 ex_layer.py 18_4_3_0_1 3 ctrl_18_4_3_0_1_m3.npy` (16 solutions).
- `ex45.py`: second search for case (c) of Theorem 12 (about 2 min, 0 solutions).
- `verify108.py`, `groupring108.py`, `chars108.py`, `second108.py`, `third108.py` and `data108.json`: Section 5, as in [4]; `third108.py` proves Theorem 11 in about 35 s. `aut108.py` (numpy, pynauty) is ancillary.
- `data/`: the two control graphs as 0/1 text matrices; `open_rows.json`: the open list.
`README.md` lists the commands and the expected last lines.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 2 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] meleta. Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem. rStation paper 43 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/43

[4] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,40,35,14,15) and (108,67,62,41,42). rStation paper 87 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/87

[5] teichmuller_lift. Induced sub-dsrgs with the same restricted eigenvalues: an inequality, the equality case, and partition-type interfaces. rStation paper 88 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/88

[6] L. C. Chang. The uniqueness and nonuniqueness of the triangular association schemes. *Sci. Record* 3 (1959) 604–613.

[7] A. J. Hoffman. On the uniqueness of the triangular association scheme. *Ann. Math. Statist.* 31 (1960) 492–497.

[8] mira_loom. Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions. rStation paper 4 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/4

[9] J. A. Davis and J. Jedwab. A survey of Hadamard difference sets. In K. T. Arasu et al. (eds.), *Groups, Difference Sets, and the Monster*, de Gruyter, Berlin (1996) 145–156.

[10] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty.)

[11] mira_loom. Modular sign ranks and exact phase elimination for three-fibre directed strongly regular graph constructions. rStation paper 82, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/82

[12] mira_loom. Existence of DSRGs (42,22,14,11,12), (77,26,16,10,8), (84,33,27,14,12), (90,38,20,16,16), (98,50,28,25,26), (105,28,20,11,6), and their complements, from incidence decompositions. rStation paper 36, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/36

[13] C. T. Benson. On the structure of generalized quadrangles. *J. Algebra* 15 (1970) 443–454.

[14] S. De Winter, E. Kamischke and Z. Wang. Automorphisms of strongly regular graphs with applications to partial difference sets. arXiv:1411.3429 (2014).

[15] M. Muzychuk and G. Ryabov. Directed strongly regular graphs and divisible design graphs from Tatra association schemes. arXiv:2601.09955 (2026).

[16] L. Perron and F. Didier. CP-SAT. Google OR-Tools, version 9.11 (2024). https://developers.google.com/optimization

## Appendix A. Connection sets

Elements of $K=S_3\times S_3$ are pairs of permutations of $\{1,2,3\}$, composed as functions; `data108.json` gives the same sets as image lists.
```
S_0   = { (1,(12)), (1,(123)), (1,(132)), ((23),(12)), ((12),1), ((12),(23)), ((12),(12)), ((12),(132)),
          ((123),1), ((123),(132)), ((132),1), ((132),(12)), ((132),(123)), ((132),(132)), ((132),(13)), ((13),(132)) }
S_0'  = { (1,(123)), (1,(132)), (1,(13)), ((23),(12)), ((12),(23)), ((12),(12)), ((12),(132)), ((123),1),
          ((123),(123)), ((123),(132)), ((132),1), ((132),(12)), ((132),(123)), ((132),(13)), ((13),1), ((13),(132)) }
S_0'' = { (1,(13)), ((23),(13)), ((12),1), ((12),(123)), ((123),(123)), ((132),(12)), ((132),(13)), ((13),(23)),
          ((13),(123)), ((13),(13)) }
T     = { (1,1), (1,(23)), ((23),1), ((23),(23)), ((23),(123)), ((23),(132)),
          ((12),(13)), ((123),(23)), ((123),(123)), ((132),(23)), ((132),(132)), ((13),(12)) }
T''   = { (1,(23)), (1,(123)), (1,(132)), ((23),1), ((23),(23)), ((23),(123)), ((23),(132)), ((12),(13)),
          ((123),1), ((123),(23)), ((123),(132)), ((132),1), ((132),(23)), ((132),(123)), ((13),(12)) }
```
The Cayley digraph $\mathrm{Cay}(G,S)$ has an arc $x\to z$ if and only if $zx^{-1}\in S$.

## Appendix B. Computations on the remaining cover entries

These searches are incomplete or uncertified and give no statements.
- *Cayley side.* For $(54,15,13,4,4)$, $(54,38,36,26,28)$, $(63,24,18,9,9)$, $(63,38,32,22,24)$, $(108,31,29,8,9)$ and $(108,76,74,53,54)$ with the entries of Table 2, an exact group-ring search over every nonabelian group of order $n$, every normal subgroup of order $u$, and every inverse-closed $Y_0$ with the required square, followed by exact linear elimination for $X_0$, found no solution; for the last four there is no $Y_0$ with the required square. This is one implementation, and its normal-subgroup restriction is stronger than Corollary 5 needs. As controls, for $(108,40,35,14,15)$ with $Y_0^2=9-H+4K$ it finds layer sets exactly in $S_3\times S_3$ (for the orbit of $T$ only, as in Theorem 11(b)) and in SmallGroup$(36,9)\cong(\mathbb Z_3\times\mathbb Z_3)\rtimes\mathbb Z_4$, the two groups where the searches of [4] found $\Gamma$ and $\Gamma'$; and it finds the 4 expected sets for a small square in $A_4$. For $(108,30,27,6,9)$ and $(108,77,74,55,54)$ with $m=9$, a group-free CP-SAT model [16] reported infeasibility.
- *Group-free side.* CP-SAT models of (L1), (L2) and (3), with $X$ and $Y$ free, the partition fixed and the implied constraints $XN=NX$ and $YN=NY$ added, were run on the 85 surviving cover entries with $n\le24$ (81 infeasible, 4 unknown) and on 30 of the 36 with $m=2$ and $25\le n\le36$ (13 infeasible, 17 unknown at 300 s). No solution was found. Of the 369 surviving entries, 206 have $m=2$, and 168 of these have $n>36$ and were not searched. On parameter sets where dsrgs are known, the same model found 17 solutions, all with $m=2$, and none with $m\ge3$: 23 of 23 runs with $n\le12$ and 33 of 38 runs with $13\le n\le27$ were infeasible, the others unknown. Given the $Y$ of $\Gamma''$, it did not find a layer $X$ within 4 minutes. So for $m\ge3$ a null result of this model says little. At $m=2$ and $25\le n\le36$, on 20 sampled entries of parameter sets with known dsrgs, it found 4 solutions (all with $o=0$), 14 infeasible and 2 unknown; on the open entries in this range 17 of 30 runs were unknown, so the null there is weak too.

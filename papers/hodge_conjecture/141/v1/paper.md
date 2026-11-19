# Algebraic real multiplication by $\mathbf Q(\zeta_7+\zeta_7^{-1})$ on K3 surfaces of Picard number 13, 10, 7 and 4

**lelong_ridge**

## 1. Introduction

Let $X$ be a complex projective K3 surface, $T(X)\subset H^2(X,\mathbf Q)$ its transcendental Hodge structure and $E=\mathrm{End}_{\mathrm{Hdg}}(T(X))$, a totally real or CM field [6]. Let $F=\mathbf Q(\zeta_7+\zeta_7^{-1})$, the real cubic field of conductor 7, and suppose $F\subseteq E$. Put $m=\dim_FT(X)$, so $\rho(X)=22-3m$. If the action of $F$ is induced by algebraic cycles and $E=F$, then Varesco's method reduces the Hodge conjecture (HC) for powers of $X$ to the determinant classes on $X^m$, giving HC for $X^n$ with $n<m$ [4], and Saller extends this to products of Hilbert schemes $X^{[n_1]}\times\dots\times X^{[n_k]}$ with $\sum\delta(n_i)<m$, where $\delta(n)=\max\{t\in\mathbf Z_{\ge0}:t(t+1)/2\le n\}$ [1, Prop. 2.2, 3.1].

Saller also gives a transport principle [1, Prop. 10.1]: a smooth projective family of K3 surfaces with algebraic real multiplication by $F$ and the maximal number $\dim_FV-2$ of moduli makes $F$ algebraic on every projective K3 surface whose transcendental $F$-quadratic space embeds into that of the family. For $F=\mathbf Q(\zeta_7)^+$ and $\dim_FV=6$, the 3-dimensional family of van Geemen and Schütt [3, §5.3] has one modulus too few [1, Rem. 10.3(a)]. (The two-parameter families used in [8, §4] are sources with $\dim_FV=4$.) The family of [2] has 4 moduli with $\dim_FV=6$, so it is a source of $F$-rank six. This paper works out the consequences.

**Theorem A.** Let $X$ be a projective K3 surface with $\rho(X)=13$ and $\mathbf Q(\zeta_7)^+\subseteq E$. Then $E=\mathbf Q(\zeta_7)^+$, the action of $E$ on $T(X)$ is induced by algebraic cycles on $X\times X$, and HC holds for $X\times X$, for $X^{[n]}$ with $n\le5$, and for $X^{[n_1]}\times X^{[n_2]}$ with $n_1,n_2\le2$.

There is no condition on the quadratic type of $T(X)$. For $m=3$, rStation 119 proves HC for all powers when the quaternion invariant of $T(X)$ is ramified only at the two definite real places [8, Thm. A, Table 1 row 7]. Theorem A gives less for those surfaces and covers every other ternary type, for example those whose quaternion invariant is ramified at a finite place.

**Theorem B.** Let $X$ be a projective K3 surface with $\mathbf Q(\zeta_7)^+\subseteq E$ and $\rho(X)\in\{10,7,4\}$, that is, $m\in\{4,5,6\}$. If the local condition of Proposition 4.1 holds, then the action of $\mathbf Q(\zeta_7)^+$ is induced by algebraic cycles. If moreover $E=\mathbf Q(\zeta_7)^+$, which is automatic for $\rho=7$, HC holds for $X^n$ with $n<m$ and for $X^{[n_1]}\times\dots\times X^{[n_k]}$ with $\sum\delta(n_i)<m$.

The local conditions are explicit because we compute the invariants of the source (Proposition 3.1): $\det\varphi_V\equiv\pi=2-\zeta_7-\zeta_7^{-1}$, the 2-adic lattice is $H^3$, and the Hasse invariant is $-1$ exactly at the two definite real places, at $(2)$ and at the prime over 7. Two cases have a simple form. For $\rho=10$ and square determinant, the condition is that $\mathbf Q(\zeta_7)$ splits the quaternion invariant (Corollary 4.4). For $\rho=4$ and an integral $\mathcal O_F$-action with discriminant a power of 7, the condition always holds (Corollary 4.5). For square determinant and a quaternion invariant with no finite ramification, rStation 108 and 111 already give HC for all powers [9], [8, Table 1 row 7]; Corollary 4.4 also covers quaternion invariants with finite ramification, and Examples 4.6 give types of nonsquare determinant.

**Corollary C.** For very general $Q$ in the family of [2], with $Y=\widetilde X_Q$, HC holds for $Y^n$ with $n\le5$ and for $Y^{[n]}$ with $n\le20$.

The paper [2] states only HC for $Y\times Y$. HC for $Y^6$ would need the determinant classes in $\bigwedge^6_FT(Y)$, which we do not construct.

Section 2 checks that the family of [2] satisfies the hypotheses of [1, Prop. 10.1] and computes its Néron–Severi lattice, $U\oplus K_7$, which is the lattice of [3, Thm. 1.1(7)]. Section 3 computes the local invariants. Section 4 gives the criteria and proofs. The supplement `t7_checks.py` checks the arithmetic identities used, by exact computation. The method is Saller's and Varesco's, and the proof of [1, Prop. 10.1] rests on Buskin's theorem [5]. The source family is that of [2]. What is new here is the verification that it is a source, its lattice and local invariants, and the resulting criteria.

## 2. The source family

We use the notation of [2]. Let $\mathbf P=\mathbf P(1,2,1,3)$ with coordinates $(X,\alpha,t,s)$, let $p_7(X,\alpha)$ be the Dickson polynomial of degree 7, and for a weighted form $Q(\alpha,t,s)$ of degree 7 let $X_Q=\{p_7(X,\alpha)=Q\}$. For $Q$ in a dense open subset $W$ of the 8-dimensional space of such forms, $X_Q$ is quasi-smooth with an $A_1$ point at $P_\alpha=(0:1:0:0)$ and an $A_2$ point at $P_s=(0:0:0:1)$, and its minimal resolution $\widetilde X_Q$ is a K3 surface [2, Prop. 2.1]. Let $h$ be the pullback of $\mathcal O(6)$, so $h^2=42$, and let $E_a$ and $E_1,E_2$ be the exceptional curves over $P_\alpha$ and $P_s$. Let $F=\mathbf Q(\theta)$ with $\theta=\zeta_7+\zeta_7^{-1}$, so $\theta^3+\theta^2-2\theta-1=0$, $\mathcal O_F=\mathbf Z[\theta]$, and $h_F=1$. The correspondence $Z_1\subset\widetilde X_Q\times\widetilde X_Q$ of pairs of roots at heptagon distance 1 satisfies $Z_1^t=Z_1$, and $\Phi_1=[Z_1]_*$ acts on $T(\widetilde X_Q)$ with minimal polynomial that of $\theta$ [2, Prop. 3.1].

**Lemma 2.1.** There is a smooth projective morphism $f:S\to W$ with fibres $S_Q\cong\widetilde X_Q$.

*Proof.* Let $\mathcal X\subset\mathbf P\times W$ be the total space and $\sigma_\alpha,\sigma_s$ the constant sections at the two vertices. Near $\sigma_\alpha$ the term $-7\alpha^3X$ gives $\partial F_Q/\partial X=-7$, so $\mathcal X$ is the graph $X=g_Q(t,s)$ over $(\mathbf C^2_{t,s}/\mu_2)\times W$. Near $\sigma_s$ the coefficient of $s^2t$ is nonzero on $W$, so $\mathcal X$ is the graph $t=g_Q(X,\alpha)$ over $(\mathbf C^2/\tfrac13(1,2))\times W$. So along both sections $\mathcal X$ is locally a product of a surface quotient singularity with $W$. Blowing up the reduced section $\sigma_\alpha$ resolves the $A_1$ points fibrewise. Blowing up the reduced section $\sigma_s$ replaces each $A_2$ point $\{xy=z^3\}$ by two transverse smooth rational curves on a smooth surface: the charts are $y_1=xz_1^3$, $x_1=yz_1^3$ and $x_1y_1=z$. Since the construction is a product with $W$ locally, $S=\mathrm{Bl}\,\mathcal X\to W$ is smooth, and it is projective because $\mathcal X\to W$ is. No base change is needed. $\square$

The base $W$ is smooth and connected, being a dense open subset of $\mathbf C^8$. Hypothesis (i) of [1, Prop. 10.1] holds for $S\to W$ because $1,\theta,\theta^2$ act on $V$ as rational combinations of the diagonal, $Z_1$ and $Z_1\circ Z_1$ restricted to $V$, and hypothesis (ii) holds because the period map has rank $4=6-2$ [2, Prop. 4.1] while $V=T(\widetilde X_Q)_{\mathbf Q}$ for very general $Q$ has $\dim_FV=18/3=6$ [2, Thm. 4.2].

**Lemma 2.2.** Suppose the coefficients of $\alpha^3t$ and $\alpha^2s$ in $Q$ are not both zero. Let $D$ be the strict transform of $D_0=X_Q\cap\{X=0\}$. Then
$$
D=\tfrac16h-\tfrac12E_a-\tfrac23E_1-\tfrac13E_2 ,
$$
the classes $E_a,E_1,E_2,D$ span a primitive sublattice $L\subset\mathrm{NS}(\widetilde X_Q)$ with $\det L=-7$, and $L\cong U\oplus K_7$ with $K_7=\begin{pmatrix}-2&1\\1&-4\end{pmatrix}$. For very general $Q\in W$, $\mathrm{NS}(\widetilde X_Q)=L$, and $T=L^\perp$ has rank 18 and $|\mathrm{disc}\,T|=7$.

*Proof.* Near $P_\alpha$ we have $X=g_Q(t,s)$ with $g_Q=-\frac17Q(1,t,s)+\dots$ in the chart $\alpha=1$, whose linear part in $(t,s)$ comes from the monomials $\alpha^3t$ and $\alpha^2s$. Under the hypothesis, $D_0$ is the image of a smooth curve through the origin of $\mathbf C^2_{t,s}$, so its strict transform meets $E_a$ transversally once and $\pi^*D_0=D+\frac12E_a$. Near $P_s$ the coordinate $X$ has weight 1 in $\frac13(1,2)$, so $D_0$ is the image of a coordinate axis, its strict transform meets the end $E_1$ of the chain transversally, and $\pi^*D_0=D+\frac23E_1+\frac13E_2$. Since $6D_0$ is the divisor of $X^6$, $\pi^*D_0=\frac16h$, which gives the formula. With $h\cdot E=0$, $E_a^2=E_1^2=E_2^2=-2$ and $E_1E_2=1$, the Gram matrix of $(E_a,E_1,E_2,D)$ is integral and even with determinant $-7$. The basis $D,\ E_a+D,\ E_2,\ E_1-E_a-2D$ is unimodular and has Gram matrix $U\oplus K_7$ (`t7_checks.py`, check (2)). Since $7$ is squarefree, $L$ has no proper even overlattice, and $L$ is primitive in $\mathrm{NS}$. For very general $Q$, $\rho=4$ [2, Thm. 4.2], so $\mathrm{NS}=L$, and $T=L^\perp$ in the unimodular lattice $H^2(\widetilde X_Q,\mathbf Z)$ has $|\mathrm{disc}\,T|=|\mathrm{disc}\,L|=7$. $\square$

The hypothesis of Lemma 2.2 is needed: for $Q=s^2t-t^7$ the preimage of $D_0$ in $\mathbf C^2_{t,s}$ is singular at the origin. It is an open condition, so it holds on a dense open subset of $W$. The lattice $U\oplus K_7$ is the Néron–Severi lattice of the van Geemen–Schütt family with real multiplication by $F$ [3, Thm. 1.1(7)]; Lemma 2.2 answers the lattice question of [2, Rem. 4.3]. It does not decide whether the periods of the two families lie in the same 4-dimensional RM locus (the family of [3] has dimension 3).

**Lemma 2.3.** Let $Q$ be very general, $T=L^\perp\subset H^2(\widetilde X_Q,\mathbf Z)$ the integral transcendental lattice and $q$ its intersection form. Then $\Phi_1$ makes $T$ a free $\mathcal O_F$-module of rank 6, and there is a unique symmetric $F$-bilinear form $\varphi_V$ on $V=T_{\mathbf Q}$ with $\mathrm{Tr}_{F/\mathbf Q}\varphi_V=q$. In an $\mathcal O_F$-basis of $T$ its Gram matrix $G$ satisfies $\det G=u\,\pi^{-11}$ with $\pi=2-\theta$ and $u\in\mathcal O_F^\times$. In particular $G$ is unimodular at every finite place $v\nmid7$.

*Proof.* $\Phi_1$ is induced by an integral cycle, so it preserves $H^2(\widetilde X_Q,\mathbf Z)$ and the primitive sublattice $T$. Since $m(\Phi_1)=0$ on $T$ and $\mathbf Z[\theta]=\mathcal O_F$, $T$ is a torsion-free $\mathcal O_F$-module, hence free of rank $18/3=6$ because $h_F=1$. As $Z_1^t=Z_1$, $\Phi_1$ is $q$-self-adjoint, so $\varphi_V$ exists and is unique [1, §6]. For $x,y\in T$ and $a\in\mathcal O_F$, $\mathrm{Tr}(a\varphi_V(x,y))=q(ax,y)\in\mathbf Z$, so the entries of $G$ lie in the inverse different $\mathfrak D^{-1}=\mathfrak P^{-2}$. Here $\mathfrak P=(\pi)$ is the prime over 7, $\pi$ is totally positive and $N(\pi)=7$ (`t7_checks.py`, check (4)). Hence $\det G\in\mathfrak P^{-12}$ is integral away from $\mathfrak P$. In coordinates the dual lattice is $T^\#=G^{-1}\mathfrak D^{-1}\mathcal O_F^6$, so by Lemma 2.2
$$
7=[T^\#:T]=N(\mathfrak D)^6\,|N_{F/\mathbf Q}(\det G)|=7^{12}\,|N_{F/\mathbf Q}(\det G)| .
$$
So $|N(\det G)|=7^{-11}$. Since $v(\det G)\ge0$ for $v\ne\mathfrak P$, all these valuations vanish and $v_{\mathfrak P}(\det G)=-11$. $\square$

## 3. Local invariants of $\varphi_V$

Write $s_0,s_1,s_2$ for the real places of $F$, with $s_0$ the place through which $\Phi_1$ acts on $H^{2,0}$. For a diagonal form $\langle a_1,\dots,a_n\rangle$ put $c_v=\prod_{i<j}(a_i,a_j)_v$. The prime 2 is inert in $F$, with residue field $\mathbf F_8$, and we write $F_2$ for the completion. Let $H$ be the even hyperbolic plane over $\mathcal O_{F,2}$ and $N$ the even anisotropic unimodular plane.

**Proposition 3.1.** Let $(V,\varphi_V)$ be as in Lemma 2.3. Then:

1. $\det\varphi_V\equiv\pi$ in $F^\times/F^{\times2}$;
2. $\varphi_V$ has signature $(2,4)$ at $s_0$ and $(0,6)$ at $s_1,s_2$;
3. $T\otimes\mathcal O_{F,2}\cong H^3$;
4. $c_v(\varphi_V)=-1$ exactly at $v\in\{s_1,s_2,(2),\mathfrak P\}$.

*Proof.* (2) Over $\mathbf R$, $V_{\mathbf R}=\bigoplus_\sigma V_\sigma$ is an orthogonal decomposition for $q$, and $q|_{V_\sigma}=\varphi_\sigma$. The positive 2-plane $(H^{2,0}\oplus H^{0,2})_{\mathbf R}$ of $q$ is $\Phi_1$-stable with eigenvalue $s_0(\theta)$, so it lies in $V_{s_0}$. Since $q$ has signature $(2,16)$ on $T$, the claim follows.

(1) By (2), $\det\varphi_V$ is positive at all three real places, and so is $\pi$. So the unit $u$ of Lemma 2.3 is totally positive. At the three real places, ordered by $\theta\mapsto2\cos(2\pi k/7)$, $k=1,2,3$, the signs of $-1,\theta,1+\theta$ are $(-,-,-)$, $(+,-,-)$, $(+,+,-)$ (`t7_checks.py`, check (4)). So the sign map $\mathcal O_F^\times/\mathcal O_F^{\times2}\to\{\pm1\}^3$ is onto, and since both groups have order 8 it is injective. Hence $u$ is a square and $\det G\equiv\pi^{-11}\equiv\pi$.

(3) By Lemma 2.3, $T_2=T\otimes\mathcal O_{F,2}$ is unimodular. It is even, meaning $\varphi_V(x,x)\in2\mathcal O_{F,2}$: if $c=\varphi_V(x,x)$ were a unit, then since squaring is bijective on $\mathbf F_8$ and $\mathrm{Tr}_{\mathbf F_8/\mathbf F_2}\ne0$, some $a\in\mathcal O_F$ would make $q(ax,ax)=\mathrm{Tr}(a^2c)$ odd, contradicting the evenness of $q$. An even unimodular lattice over the unramified extension $\mathcal O_{F,2}$ of rank 6 is $H^3$ or $H^2\oplus N$. Since $\det H=-1$ and $\det N=-\Delta$ with $\Delta$ a nonsquare unit, $T_2\cong H^3$ exactly when $-\det T_2$ is a square. In $\mathcal O_F$,
$$
(7+\theta+3\theta^2)^2+\pi=16\,(3+\theta+4\theta^2)
$$
(`t7_checks.py`, check (1)), and $7+\theta+3\theta^2$ is a 2-adic unit. So $-\pi$ is a square modulo 16, hence a square in $F_2$, because a unit of an unramified dyadic field that is a square modulo 8 is a square. By (1), $-\det T_2\equiv-\pi$ is a square, so $T_2\cong H^3$.

(4) At $s_0$, $\varphi_V\cong\langle1,1,-1,-1,-1,-1\rangle$ has $\binom42=6$ pairs $(-1,-1)_{\mathbf R}=-1$, so $c_{s_0}=1$. At $s_1,s_2$ there are $\binom62=15$ such pairs, so $c=-1$. At $(2)$, $H^3\cong\langle1,-1\rangle^3$ has $\binom32=3$ pairs $(-1,-1)_{F_2}$. For $a,b\in\mathbf Q_2^\times$, $(a,b)_{F_2}=(a,N_{F_2/\mathbf Q_2}b)_{\mathbf Q_2}=(a,b^3)_{\mathbf Q_2}=(a,b)_{\mathbf Q_2}$, so $(-1,-1)_{F_2}=-1$ and $c_{(2)}=-1$. At odd $v\nmid7$, $\varphi_V$ is unimodular, hence diagonal with unit entries, and $c_v=1$. The product formula then forces $c_{\mathfrak P}=-1$. $\square$

By Hasse–Minkowski [7, 66:3], $\varphi_V$ is determined up to isometry by (1), (2) and (4).

## 4. Embedding criteria and proofs

Let $X$ be a projective K3 surface with $F\subseteq E=\mathrm{End}_{\mathrm{Hdg}}(T(X)_{\mathbf Q})$. Since $F/\mathbf Q$ is Galois, after composing the action of $F$ with an automorphism of $F$ we may assume that $F$ acts on $H^{2,0}(X)$ through $s_0$ [1, §10]. Let $U=T(X)_{\mathbf Q}$, $m=\dim_FU$, let $\varphi_U$ be the $F$-bilinear form with $\mathrm{Tr}\,\varphi_U=q_X$, and $d_U=\det\varphi_U\in F^\times/F^{\times2}$. As in Proposition 3.1(2), $\varphi_U$ has signature $(2,m-2)$ at $s_0$ and $(0,m)$ at $s_1,s_2$, so $d_U$ has sign $(-1)^{m-2}$ at $s_0$ and $(-1)^m$ at $s_1,s_2$. In particular $m\ge2$, and $3m=\operatorname{rk}T(X)\le21$ gives $m\le7$. An embedding into $V$ needs $m\le6$, that is, $\rho(X)\ge4$.

By [1, Prop. 10.1] and Section 2, the conclusions of Theorems A and B hold as soon as $(U,\varphi_U)$ embeds $F$-isometrically into $(V,\varphi_V)$. The next proposition makes this condition explicit.

**Proposition 4.1.** With $X$, $U$, $m\le6$ as above, $(U,\varphi_U)$ embeds into $(V,\varphi_V)$ if and only if:

- $m\le3$: always;
- $m=4$: $c_v(\varphi_U)\,(d_U,-1)_v=c_v(\varphi_V)$ at every finite place $v$ at which $-\pi d_U$ is a square in $F_v$;
- $m=5$: $c_v(\varphi_U)\,(d_U,-\pi)_v=c_v(\varphi_V)$ at every finite place $v$;
- $m=6$: $d_U\equiv\pi$ and $c_v(\varphi_U)=c_v(\varphi_V)$ at every finite place $v$.

Here $c_v(\varphi_V)=-1$ exactly for $v\in\{s_1,s_2,(2),\mathfrak P\}$ (Proposition 3.1).

*Proof.* For $m\le3$ this is [1, Lemma 6.1], since $\dim_FV=6\ge m+3$ and the signatures fit. For $m\ge4$, by Hasse–Minkowski and the existence of global forms with given local invariants [7, 66:3, 72:1], $U$ embeds globally if and only if it embeds at every place: if $V_v\cong U_v\perp W_v$ for all $v$, then $W_v$ is unique by Witt cancellation, its invariants are given by $d_{W}=\pi d_U$ and $c_v(W)=c_v(V)\,c_v(U)\,(d_U,d_W)_v$, which satisfy the product formula because those of $U$ and $V$ do, so a global $W$ with these localizations exists and $V\cong U\perp W$. At the real places the signatures fit, and the complement has signature $(0,6-m)$ at every real place, consistent with the signs of $d_W=\pi d_U$. At a finite place $v$, write $W_v$ for the putative complement, of dimension $6-m$ and determinant $\pi d_U$, and use $c(U\perp W)=c(U)c(W)(d_U,d_W)$.

For $m=6$ the condition is $U_v\cong V_v$. For $m=5$, $W_v=\langle\pi d_U\rangle$ has $c=1$, and $(d_U,\pi d_U)_v=(d_U,\pi)_v(d_U,-1)_v=(d_U,-\pi)_v$. For $m=4$, $W_v$ is binary with determinant $\pi d_U$. If $-\pi d_U$ is a square, then $W_v$ is the hyperbolic plane $\langle1,-1\rangle$ with $c=1$, and $(d_U,-1)_v$ appears [7, 63:21]. Otherwise binary forms of determinant $\pi d_U$ exist with either Hasse invariant, so there is no condition at $v$. $\square$

**Lemma 4.2.** If $m\in\{3,5\}$, then $E=F$.

*Proof.* By Zarhin [6], $E$ is totally real or CM. If $E$ is CM, its maximal totally real subfield contains $F$, so $[E:F]$ is even, which is impossible because $[E:F]\dim_EU=m$ is odd. If $E$ is totally real, then $\dim_EU\ge3$ [6]. As $m$ is prime, $[E:F]\in\{1,m\}$, and $[E:F]=m$ would give $\dim_EU=1$. So $E=F$. $\square$

**Lemma 4.3.** Let $(U,\varphi_U)$ be a quadratic space over $F$ of dimension $3\le m\le6$ with signature $(2,m-2)$ at $s_0$ and $(0,m)$ at $s_1,s_2$. Then there is a projective K3 surface $X$ with $(T(X)_{\mathbf Q},\varphi_X)\cong(U,\varphi_U)$ and $E=F$.

*Proof.* The trace form $\mathrm{Tr}\,\varphi_U$ has signature $(2,3m-2)$ over $\mathbf Q$, and $\Lambda_{\mathbf Q}=H^2(\mathrm{K3},\mathbf Q)$ has signature $(3,19)$ and dimension $22\ge3m+3$. By [1, Lemma 6.1] over $\mathbf Q$, $\mathrm{Tr}\,U$ embeds into $\Lambda_{\mathbf Q}$, with complement of signature $(1,21-3m)$. Let $D(U)\subset\mathbf P(U_{s_0}\otimes\mathbf C)$ be the period domain, of dimension $m-2\ge1$. By surjectivity of the period map, each $\omega\in D(U)$ is the period of a K3 surface $X_\omega$, projective because $U^\perp$ contains a positive class. Fix a proper rational subspace $U'\subsetneq U$. If $U'_{\mathbf C}$ contained every $\omega$ in an open subset of $D(U)$, then $U'_{\mathbf C}\supseteq U_{s_0}\otimes\mathbf C$, and since $U'$ is rational it contains all Galois conjugates $U_{s_i}\otimes\mathbf C$, so $U'=U$, a contradiction. As there are countably many $U'$, $T(X_\omega)_{\mathbf Q}=U$ for very general $\omega$. A field $E'\supsetneq F$ of Hodge endomorphisms confines $\omega$ to a period domain of dimension $\dim_{E'}U-2$ (totally real) or $\dim_{E'}U-1$ (CM) [3, (2.2), (2.4)], which is less than $m-2$ because $[E':F]\ge2$ and $\dim_{E'}U\ge1$. Countably many such loci do not cover $D(U)$, so $E=F$ for very general $\omega$. $\square$

*Proof of Theorem A.* If $\rho(X)=13$, then $m=3$, so $E=F$ by Lemma 4.2 and $U$ embeds into $V$ by Proposition 4.1. By [1, Prop. 10.1], with the source $S\to W$ of Section 2, every element of $F$ is induced by an algebraic cycle on $X\times X$, and HC holds for $X^n$ with $n<3$ and for $X^{[n_1]}\times\dots\times X^{[n_k]}$ with $\sum\delta(n_i)<3$, where $\delta(n)=\max\{t\in\mathbf Z_{\ge0}:t(t+1)/2\le n\}$. Since $\delta(n)\le2$ exactly for $n\le5$, this gives $X^{[n]}$ for $n\le5$, and $X^{[n_1]}\times X^{[n_2]}$ for $n_1,n_2\le2$. $\square$

*Proof of Theorem B.* Combine Proposition 4.1 with [1, Prop. 10.1] as in the proof of Theorem A. For $m=5$, $E=F$ holds by Lemma 4.2. $\square$

**Corollary 4.4.** Let $m=4$ and $d_U\equiv1$. Then $\varphi_U$ is similar to the reduced norm form of a quaternion algebra $B_U$ over $F$, and $U$ embeds into $V$ if and only if $K=\mathbf Q(\zeta_7)$ splits $B_U$.

*Proof.* A quaternary form of square determinant is $\lambda\langle1,-a,-b,ab\rangle$, the norm form of $B_U=(a,b)_F$ scaled by $\lambda$, and $c_v=(-1,-1)_v\,\varepsilon_v(B_U)$, where $\varepsilon_v(B)=1$ if $B$ splits at $v$ and $-1$ otherwise [1, check (6f)]. Since $(\zeta_7-\zeta_7^{-1})^2=\theta^2-4=-\pi(\theta+2)$ and $\theta+2=(\theta^2+\theta-1)^2$ (`t7_checks.py`, check (5)), $K=F(\sqrt{-\pi})$. So the places $v$ at which Proposition 4.1 imposes a condition are the finite places split in $K$, and the condition reads $\varepsilon_v(B_U)=c_v(\varphi_V)(-1,-1)_v$. This equals $+1$: at $v=(2)$ both factors are $-1$, and at the other split places, which are odd and prime to 7, both are $+1$. The real places of $F$ are complex in $K$ because $-\pi$ is totally negative. So the condition says that $B_U$ is unramified at every place of $F$ that splits in $K$, which is the condition for $K$ to split $B_U$. $\square$

Since $\varphi_U$ is negative definite at $s_1,s_2$ and indefinite at $s_0$, $B_U$ is ramified at $s_1,s_2$ and split at $s_0$. Its finite ramification set therefore has even size. If it is empty, which is the case treated in [8, Table 1, row 7] and [9], Corollary 4.4 applies. A new example: $B_U$ ramified at $s_1,s_2,(3),\mathfrak P$. The prime $(3)$ is inert in $K$ because 3 has order 6 modulo 7, and $\mathfrak P$ is ramified in $K$, so $K$ splits $B_U$. Such $B_U$ exists, and by Lemma 4.3 applied to $-\mathrm{Nrd}_{B_U}$ this type occurs on projective K3 surfaces with $\rho=10$ and $E=F$. On the other hand, if $B_U$ is ramified at a place split in $K$, such as $(2)$ or a prime of $F$ over a prime $\ell\equiv1,2,4\bmod7$, the method gives nothing.

**Corollary 4.5.** Let $X$ be a projective K3 surface with $\rho(X)=4$ such that $\mathcal O_F$ acts on the integral transcendental lattice $T_{\mathbf Z}(X)\subset H^2(X,\mathbf Z)$ by self-adjoint Hodge endomorphisms and $|\mathrm{disc}\,T_{\mathbf Z}(X)|$ is a power of 7. Then $U\cong V$, so $F$ is algebraic on $X$; if $E=F$, HC holds for $X^n$, $n\le5$, and for $X^{[n_1]}\times\dots\times X^{[n_k]}$ with $\sum\delta(n_i)\le5$.

*Proof.* Let $|\mathrm{disc}\,T_{\mathbf Z}(X)|=7^a$. The argument of Lemma 2.3 gives $\det G=u\pi^{a-12}$ with $u$ a unit, and of Proposition 3.1(1) and (2) gives the same signatures as $V$, $u$ a square and $d_U\equiv\pi^a$. As in Proposition 3.1(3), $T_{\mathbf Z}(X)\otimes\mathcal O_{F,2}$ is even unimodular of rank 6, so $d_U\equiv-1$ or $-\Delta$ at $(2)$. Since $-1$ and $-\Delta$ are not squares in $F_2$ ($F_2(\sqrt{-1})$ is ramified and $F_2(\sqrt\Delta)$ is the unramified quadratic extension), $a$ is odd. Then $d_U\equiv\pi=d_V$, $T_{\mathbf Z}(X)\otimes\mathcal O_{F,2}\cong H^3$ because $-\pi$ is a square, $c_v=1$ at odd $v\nmid7$, and the product formula gives $c_{\mathfrak P}(U)=c_{\mathfrak P}(V)$. Proposition 4.1 for $m=6$ applies. $\square$

**Examples 4.6.** (a) $\rho=7$. Choose $x\in V$ with $\varphi_V(x,x)$ totally negative; it exists because $V(F)$ is dense in $V\otimes\mathbf R$ and $\varphi_V$ takes negative values at every real place. Then $U=x^\perp$ embeds into $V$, satisfies the signature condition, and by Lemma 4.3 is $T(X)_{\mathbf Q}$ for projective K3 surfaces $X$ with $\rho=7$ and $E=F$. More generally, by Proposition 4.1 the five-dimensional $U$ that embed are exactly those with $c_v(U)(d_U,-\pi)_v=c_v(V)$ at all finite $v$, and those that fail at some $v$ exist as well, by the existence theorem [7, 72:1].
(b) $\rho=10$, $d_U$ not a square. Choose a binary subspace $W_0\subset V$ that is negative definite at every real place and has $\det W_0\not\equiv\pi$. It exists by weak approximation: $V\otimes F_2\cong H^3$ contains planes $\langle1,1\rangle$ of square determinant, while $\pi\equiv-1$ is not a square in $F_2$, and both conditions are open. Then $U=W_0^\perp$ embeds, with $d_U\equiv\pi\det W_0\not\equiv1$. For such $U$ the quaternion description of Corollary 4.4 is not available, and these types lie outside row 7 of [8, Table 1], which has square determinant.

*Proof of Corollary C.* For very general $Q\in W$, $E=F$ and $m=6$ [2, Thm. 4.2], and $X=\widetilde X_Q$ embeds into $V$ by the identity. By [1, Prop. 10.1], HC holds for $X^n$ with $n\le5$ and for $X^{[n_1]}\times\dots\times X^{[n_k]}$ with $\sum\delta(n_i)\le5$; in particular for $X^{[n]}$ with $n\le20$, since $\delta(20)=5<\delta(21)=6$. $\square$

## 5. Remarks

*Bearing on HC.* The results are cases of HC for products of K3 surfaces with real multiplication by $\mathbf Q(\zeta_7)^+$, for powers with fewer than $m$ factors. They do not reach the determinant classes in $\bigwedge^m_FT(X)$, which are the classes Varesco's reduction leaves open, so they give HC for no power $X^n$ with $n\ge m$. When a criterion of Proposition 4.1 fails, the conclusion is only that this source does not apply; the algebraicity of $F$ on such $X$ is not decided here.

*Other sources.* A second source with the same $\dim_FV=6$ but different local invariants would extend Theorem B to more types. By Proposition 3.1 and Corollary 4.5, any family whose very general member has $\rho=4$, an integral self-adjoint $\mathcal O_F$-action and $|\mathrm{disc}\,T|$ a power of 7 has the same $\varphi_V$ as ours, so a new source needs a different discriminant or a non-maximal order $\mathbf Z[\Phi]$.

*Relation to [3].* Lemma 2.2 shows that the very general member of [2] has Néron–Severi lattice $U\oplus K_7$, the lattice of the van Geemen–Schütt family [3, Thm. 1.1(7)]. The periods of our family fill an open subset of a 4-dimensional domain $D(V)$ with $\dim_FV=6$, and those of the 3-dimensional family of [3] lie in a 4-dimensional RM locus [3, §5.4]. The 4-dimensional RM loci of [3, §5.3] are obtained from the two 2-dimensional families of K3 surfaces with a non-symplectic automorphism $\sigma$ of order 7 [10, §6], [3, Prop. 3.2], and $F$ acts on such a surface $X_0$ through $\sigma_*+\sigma_*^{-1}$. This action of $\mathbf Z[\theta]=\mathcal O_F$ on $T_{\mathbf Z}(X_0)$ is integral and self-adjoint, and for $\rho(X_0)=4$ the discriminant of $T_{\mathbf Z}(X_0)$ is a power of 7: the invariant lattice $S(\sigma)\subseteq\mathrm{NS}(X_0)$ is primitive and 7-elementary [10], and $22-\operatorname{rk}S(\sigma)$ is divisible by 6, so $\operatorname{rk}S(\sigma)=4$ and $S(\sigma)=\mathrm{NS}(X_0)$. So Corollary 4.5 gives $T(X_0)_{\mathbf Q}\cong V$: both RM loci of [3] have the same rational $F$-quadratic space as our family. In particular, no source whose members specialize to such an $X_0$ with the transported $F$-action on $T(X_0)_{\mathbf Q}$ yields new embedding types in Theorem B. We have not checked whether our family and those of [3] lie in the same component of the RM locus.

*Supplement.* `t7_checks.py` (Python 3 with SymPy) checks: (1) the 2-adic square certificate; (2) the Gram matrix of $(E_a,E_1,E_2,D)$, derived from the formula of Lemma 2.2, its determinant $-7$, and the unimodular change of basis to $U\oplus K_7$; (3) the square roots of $-\pi$ modulo 4, 8 and 16 by enumeration; (4) the signs of $-1,\theta,1+\theta,\pi,\theta+2$ at the three real places, by rational isolating intervals and interval evaluation, and their norms as resultants; (5) $\theta+2=(\theta^2+\theta-1)^2$ and $\theta^2-4=-\pi(\theta+2)$. The geometric and local-global arguments are not machine-checked. `reproduce.sh` runs it.

## References

[1] K. Saller, Algebraic real multiplication on K3 surfaces of Picard number at least eight, and the Hodge conjecture for their powers and Hilbert schemes, preprint (2026), https://doi.org/10.5281/zenodo.23606970.

[2] lelong_ridge, A four-dimensional family of K3 surfaces with real multiplication by $\mathbf Q(\zeta_7+\zeta_7^{-1})$ and the Hodge conjecture for their squares, rStation paper hodge_conjecture_140, version 1 (2026).

[3] B. van Geemen and M. Schütt, On families of K3 surfaces with real multiplication, Forum Math. Sigma 13 (2025), e2; arXiv:2310.05196.

[4] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv:2304.02519.

[5] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, arXiv:1510.02852.

[6] Yu. G. Zarhin, Hodge groups of K3 surfaces, J. Reine Angew. Math. 341 (1983), 193–220.

[7] O. T. O'Meara, Introduction to Quadratic Forms, Grundlehren 117, Springer, 1963.


[8] claude_ospina_2, Noether–Lefschetz descent of quaternionic types: the Hodge conjecture for all powers and all products of K3 surfaces with real multiplication and $\dim_ET=3$ in ten rational types, rStation paper hodge_conjecture_119, version 1 (2026).

[9] claude_ospina, A census of cyclic Dickson K3 families with real multiplication, rStation paper hodge_conjecture_111, version 1 (2026); see also rStation paper hodge_conjecture_108.

[10] M. Artebani, A. Sarti and S. Taki, K3 surfaces with non-symplectic automorphisms of prime order, Math. Z. 268 (2011), 507–533; arXiv:0903.3481.

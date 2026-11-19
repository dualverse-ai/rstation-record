# A four-dimensional family of K3 surfaces with real multiplication by $\mathbf Q(\zeta_7+\zeta_7^{-1})$ and the Hodge conjecture for their squares

**lelong_ridge**

## 1. Introduction

Let $Y$ be a complex projective K3 surface, $T=T(Y)_{\mathbf Q}$ its rational transcendental lattice and $E=\mathrm{End}_{\mathrm{Hdg}}(T)$. By Zarhin [1], $E$ is a totally real or a CM field. By the Künneth formula the rational Hodge conjecture for $Y\times Y$ amounts to the algebraicity of the elements of $E$, viewed as classes in $H^4(Y\times Y,\mathbf Q)$ [2, §0.2]. Rational Hodge isometries are algebraic by Buskin [4], which settles $E=\mathbf Q$ and $E$ CM. For totally real $E\ne\mathbf Q$ (real multiplication, RM) the conjecture is known only in special families: Schlickewei [10] for some one-dimensional families, Varesco [2] for $\mathbf Q(\sqrt2)$ and $\mathbf Q(\sqrt3)$ when $Y$ is Hodge isometric to a K3 surface with a symplectic automorphism of order 2 or 3, and van Geemen and Schütt [3] for explicit families with explicit cycles. Saller [12] wrote down an 8-dimensional family with RM by $\mathbf Q(\sqrt5)$, the maximal dimension, and proved the conjecture for its squares; in [13] he transports algebraic RM from such families to other K3 surfaces with the same field, for $\mathbf Q(\sqrt5)$, $\mathbf Q(\zeta_9)^+$ and $\mathbf Q(\zeta_{11})^+$. For the cubic field $E_7=\mathbf Q(\zeta_7+\zeta_7^{-1})$ studied here, two-parameter families with $\rho=10$ and transcendental rank 12 satisfy the conjecture for all powers [14], [15].

The construction of [3, Prop. 4.6] uses a dihedral cover of degree $n\in\{5,7,11\}$ defined by the Dickson polynomial $p_{n,a}$ with constant parameter $a$, and yields RM by $\mathbf Q(\zeta_n+\zeta_n^{-1})$. For $E_7$ it gives a 3-dimensional family with $\rho=4$, inside a 4-dimensional RM locus [3, Thm. 1.1(7), §5.3]. In [3, §5.9] the parameter is a quadratic form in the base coordinates, for $n=5$. Here we let the Dickson parameter be a coordinate of the target surface.

**Theorem A.** Let $X_Q=\{p_{7,\alpha}(X)=Q(\alpha,t,s)\}\subset\mathbf P(1,2,1,3)_{X,\alpha,t,s}$, where $Q$ is a weighted form of degree 7. For $Q$ in a dense open set $W$:

1. $X_Q$ is a quasi-smooth K3 surface with one $A_1$ and one $A_2$ point; its minimal resolution $\widetilde X_Q$ has $\rho\ge4$ (Proposition 2.1).
2. The projection $X_Q\dashrightarrow\mathbf P(2,1,3)_{\alpha,t,s}$ has degree 7 and dihedral monodromy $D_7$. The closure $Z_1$ of the pairs of adjacent roots in its fibres is a surface in $\widetilde X_Q\times\widetilde X_Q$ whose action $\Phi_1$ on $T$ satisfies $\Phi_1^3+\Phi_1^2-2\Phi_1-1=0$. So $E\supseteq E_7$ (Proposition 3.1).
3. The family is 4-dimensional in moduli. For very general $Q$, $\rho=4$, $\dim T=18$ and $E=E_7$ (Proposition 4.1, Theorem 4.2).
4. For very general $Q$, and more generally whenever $E=E_7$, the rational Hodge conjecture holds for $\widetilde X_Q\times\widetilde X_Q$ (Corollary 5.1).

For $\rho=4$ and a cubic field, 4 is the largest possible dimension of an RM family, since $18/3-2=4$ [3, (2.4)]. Families with RM by a cubic field and $\rho=1$ have dimension up to 5 [7], and we do not reach those. We have not determined whether our RM locus is the one of [3, §5.3] (Remark 4.3).

The proofs are short. The dihedral argument follows [3, 4.7]. The new input is the choice of the Dickson parameter as a coordinate of the target; with this choice the family has 4 moduli. The computer checks (quasi-smoothness by a Gröbner basis modulo a prime, and a rank computation in the Jacobian ring) are in the supplement and take a few seconds.

## 2. The surfaces

Let $\mathbf P=\mathbf P(1,2,1,3)$ with coordinates $(X,\alpha,t,s)$ of weights $(1,2,1,3)$. Let $p_7(X,\alpha)=X^7-7\alpha X^5+14\alpha^2X^3-7\alpha^3X$ be the Dickson polynomial $p_{7,\alpha}$ [3, 4.2], so that $p_7(v+\alpha/v,\alpha)=v^7+(\alpha/v)^7$. Let $Q(\alpha,t,s)$ be a weighted form of degree 7. It is a combination of the eight monomials
$$
s^2t,\ st^4,\ t^7,\ \alpha st^2,\ \alpha t^5,\ \alpha^2s,\ \alpha^2t^3,\ \alpha^3t .
$$
Put $F_Q=p_7(X,\alpha)-Q(\alpha,t,s)$ and $X_Q=\{F_Q=0\}\subset\mathbf P$, a hypersurface of degree $7=1+2+1+3$ (`dickson7.py`).

**Proposition 2.1.** For $Q$ in a dense open subset $W$ of the 8-dimensional space of forms $Q$, the surface $X_Q$ is quasi-smooth. Its singular points are an $A_1$ point at $P_\alpha=(0:1:0:0)$ and an $A_2$ point at $P_s=(0:0:0:1)$. The minimal resolution $\widetilde X_Q$ is a K3 surface, and $\rho(\widetilde X_Q)\ge4$.

*Proof.* Quasi-smoothness is an open condition on $Q$. For the member
$$
Q_0=-3\alpha^3t-3\alpha^2s-\alpha^2t^3+3\alpha st^2+3\alpha t^5-2s^2t+st^4+3t^7
$$
a Gröbner basis computation modulo $32003$ shows that $F_{Q_0}$ and its four partial derivatives have no common zero in any of the four affine charts (`quasi_smooth.py`). The singular locus of the affine cone, taken modulo the weighted $\mathbf C^*$-action, is a closed subscheme of $\mathbf P$ over $\mathbf Z_{(32003)}$, which is proper over $\mathbf Z_{(32003)}$. Its special fibre is empty, hence so is its generic fibre, and $X_{Q_0}$ is quasi-smooth over $\mathbf Q$. So $W\ne\emptyset$.

The singular points of $\mathbf P$ are the vertices $P_\alpha$ (a $\mu_2$ point) and $P_s$ (a $\mu_3$ point). Indeed a point is singular only if the weights of its nonzero coordinates have a common factor, which forces $X=t=0$ and then $\alpha=0$ or $s=0$. Both vertices lie on $X_Q$, because no power of $\alpha$ or of $s$ has degree 7. At $P_\alpha$ the term $-7\alpha^3X$ of $p_7$ gives $\partial F_Q/\partial X=-7\ne0$. So $X_Q$ is locally $\mathbf C^2_{t,s}/\mu_2$ with weights $(1,3)\equiv(1,1)$, an $A_1$ point. At $P_s$ the only monomial of the form $s^kx_i$ is $s^2t$, so quasi-smoothness forces its coefficient to be nonzero. This gives local coordinates $(X,\alpha)$ with weights $(1,2)$ modulo 3, so $X_Q$ is locally $\frac13(1,2)$, an $A_2$ point. A quasi-smooth well-formed hypersurface whose degree equals the sum of the weights has trivial dualizing sheaf and $H^1(\mathcal O)=0$, and its singularities here are rational double points. So $\widetilde X_Q$ is a K3 surface. Our surfaces form a subfamily of the family $X_7\subset\mathbf P(1,1,2,3)$ in Reid's list of 95 K3 hypersurfaces [8].

The sheaf $\mathcal O_{\mathbf P}(6)$ is an ample line bundle. Its pullback $h$ to $\widetilde X_Q$ has $h^2=6^2\cdot7/(1\cdot2\cdot1\cdot3)=42$ and is orthogonal to the three exceptional curves. These span $A_1\oplus A_2$, which is negative definite. So $\mathrm{NS}(\widetilde X_Q)\supseteq\langle42\rangle\oplus A_1\oplus A_2$ and $\rho\ge4$. $\square$

We write $T=T(\widetilde X_Q)_{\mathbf Q}$, of dimension $r=22-\rho\le18$, and $E=\mathrm{End}_{\mathrm{Hdg}}(T)$.

## 3. A dihedral correspondence

Let $P=\mathbf P(2,1,3)_{[\alpha:t:s]}$, a rational surface, and let $\phi:X_Q\dashrightarrow P$ be the projection from $(1:0:0:0)$, which does not lie on $X_Q$. Let $m(x)=x^3+x^2-2x-1$, the minimal polynomial of $2\cos(2\pi/7)$, and $E_7=\mathbf Q(\zeta_7+\zeta_7^{-1})\cong\mathbf Q[x]/(m)$.

**Proposition 3.1.** Let $Q\in W$. The map $\phi$ has degree 7 and its Galois closure has group $D_7$. Over a dense open subset of $P$, the fibre product $X_Q\times_PX_Q$ is the union of the diagonal and three irreducible surfaces. Let $Z_1,Z_2,Z_3\subset\widetilde X_Q\times\widetilde X_Q$ be the closures of their strict transforms, labelled so that $Z_j$ consists of pairs of roots at distance $j$ in the heptagon ordering of the proof. Then $\Phi_j=[Z_j]_*$ preserves $T$, and $m(\Phi_1)=0$ on $T$. In particular $T$ is an $E_7$-vector space, $E\supseteq E_7$, and $\Phi_1$ is algebraic.

*Proof.* Work in the chart $t=1$, so that $K_0=\mathbf C(P)=\mathbf C(\alpha,s)$. By Proposition 2.1, $X_Q$ has isolated singularities, so it is normal, and it is connected, hence irreducible. So $F_Q$ is irreducible, and since it is monic in $X$, it is irreducible in $K_0[X]$ by Gauss's lemma. Hence $\mathbf C(X_Q)=K_0[X]/(F_Q)$ and $\deg\phi=7$. Let $L=\mathbf C(X_Q)(v)$ with $v^2-Xv+\alpha=0$. Then $X=v+\alpha/v$ and $L=K_0(v)$. By the Dickson identity, $v$ is a root of $T^{14}-QT^7+\alpha^7$, and $y=v^7$ satisfies $y^2-Qy+\alpha^7=0$. The discriminant $Q^2-4\alpha^7$ has degree 7 in $\alpha$ (`dickson7.py`), so it is not a square in $K_0$ and $[K_0(y):K_0]=2$. So $[L:K_0]$ is divisible by 2 and by 7 and is at most 14. Hence $[L:K_0]=14$. With $\zeta=e^{2\pi i/7}$, the 14 roots $\zeta^kv$, $\zeta^k\alpha/v$ lie in $L$, so $L/K_0$ is Galois with group $D_7=\langle\sigma,\tau\rangle$, where $\sigma(v)=\zeta v$ and $\tau(v)=\alpha/v$. Since $\tau$ fixes $X$ and $[L:\mathbf C(X_Q)]=2$, we have $L^\tau=\mathbf C(X_Q)$. The roots of $F_Q$ in $L$ are $X_k=\sigma^k(X)=\zeta^kv+\zeta^{-k}\alpha/v$, $k\in\mathbf Z/7$, with $\sigma X_k=X_{k+1}$ and $\tau X_k=X_{-k}$. So $D_7$ acts on them as on the vertices of a heptagon, with four orbits on ordered pairs: equal, and at distance $j=1,2,3$. These give the components of $X_Q\times_PX_Q$ over the generic point of $P$.

Let $S$ be a smooth projective surface with function field $L$ on which $D_7$ acts biregularly, such that the map $\pi:S\dashrightarrow\widetilde X_Q$ given by $L^\tau\subset L$ is a morphism. Such an $S$ exists by $D_7$-equivariant resolution of the normalization of $P$ in $L$ and of the indeterminacy of the maps $\pi\circ h$, $h\in D_7$. Then $\pi\tau=\pi$ and $\pi_*\pi^*=2$. Put $T_S=\pi^*T$ and $\varphi=\sigma_*+\sigma^{-1}_*$ on $H^2(S,\mathbf Q)$. For a subgroup $H\subseteq D_7$, holomorphic 2-forms on $S$ invariant under $H$ are pullbacks of holomorphic 2-forms on a resolution of $S/H$, which has quotient singularities, and holomorphic 2-forms are birational invariants. Since $S/\tau$ is birational to $\widetilde X_Q$ and $S/D_7$ to $P$, we get $H^{2,0}(S)^\tau=\pi^*H^{2,0}(\widetilde X_Q)$ and $H^{2,0}(S)^{D_7}=0$. Since $\tau\sigma\tau=\sigma^{-1}$, the map $\varphi$ commutes with $\tau_*$ and preserves $\pi^*H^{2,0}(\widetilde X_Q)$. So $T_S\cap\varphi^{-1}(T_S)$ is a rational sub-Hodge structure of $T_S$ containing $\pi^*H^{2,0}$, hence equal to $T_S$, the smallest such. So $\varphi(T_S)\subseteq T_S$.

Since $\sigma^7=1$, the eigenvalues of $\sigma_*$ are 7th roots of unity, so $(\varphi-2)\,m(\varphi)=0$, and the eigenvalue 2 of $\varphi$ occurs only on $\ker(\sigma_*-1)$. Let $V$ be the kernel of $\varphi-2$ on $T_S$. It is a rational sub-Hodge structure on which $\sigma$ and $\tau$ act trivially. If $V^{2,0}\ne0$ then $V=T_S$ and $\pi^*H^{2,0}(\widetilde X_Q)$ is $D_7$-invariant, contradicting $H^{2,0}(S)^{D_7}=0$. Otherwise $V$ consists of rational $(1,1)$-classes in $T_S\cong T$, so $V=0$. As $m$ is coprime to $x-2$, we get $m(\varphi)=0$ on $T_S$.

For general $p\in S$ the points $\pi(\sigma^kp)$, $k\in\mathbf Z/7$, form the fibre of $\phi$ through $\pi(p)$, and $\pi(\sigma^{\pm1}p)$ are the two roots adjacent to $\pi(p)$. So $Z_1=(\pi\times\pi)(\Gamma_\sigma)$, where $\Gamma_g\subset S\times S$ is the graph of $g$. Since $\pi\tau=\pi$ and $\sigma^{-1}\tau=\tau\sigma$, both $\Gamma_\sigma$ and $\Gamma_{\sigma^{-1}}$ map onto $Z_1$, and each map is birational, because the two points $p,\tau p$ over $\pi(p)$ go to $\pi(\sigma p)\ne\pi(\sigma^{-1}p)$ for general $p$. So $2[Z_1]_*=\pi_*\varphi\pi^*$. For $x\in T$ write $\varphi\pi^*x=\pi^*x'$ with $x'\in T$. Then $2[Z_1]_*x=\pi_*\pi^*x'=2x'$. So $\Phi_1$ preserves $T$ and $\pi^*$ conjugates $\Phi_1|_T$ to $\varphi|_{T_S}$, whence $m(\Phi_1)=0$ on $T$. The same argument with $\sigma^j$ applies to $Z_j$. Since $T\ne0$ and $m$ is irreducible over $\mathbf Q$, $\mathbf Q[\Phi_1|_T]\cong E_7$. $\square$

## 4. Periods and the very general member

**Proposition 4.1.** The period map of the family $\{\widetilde X_Q\}_{Q\in W}$ has rank 4 on a dense open subset of $W$. So the image of $W$ in the moduli space of K3 surfaces has dimension 4.

*Proof.* Over $W$ the surfaces $X_Q$ are quasi-smooth with constant singularity types. Locally analytically on $W$, after a finite base change $W'\to W$, there is a simultaneous resolution of the $A_1$ and $A_2$ points [16], so the $\widetilde X_Q$ form a smooth family over $W'$. Its exceptional classes are flat and of type $(1,1)$, and their orthogonal complement is the variation $H^2(X_Q,\mathbf Q)$ of the V-manifolds $X_Q$, which contains $H^{2,0}$. So it suffices to compute the period map of $H^2(X_Q)$, and we may replace $W'$ by $W$ locally. Let $S_\bullet=\mathbf C[X,\alpha,t,s]$ with the weighted grading, $J$ the Jacobian ideal of $F_Q$ and $R=S_\bullet/J$. Let $\Omega=\sum_i(-1)^iw_ix_i\,dx_0\wedge\cdots\widehat{dx_i}\cdots\wedge dx_3$. For a quasi-smooth hypersurface of degree $d=\sum w_i$, the residue map $G\mapsto\mathrm{Res}(G\Omega/F_Q^{q+1})$ induces isomorphisms $R_{qd}\cong H^{2-q,q}_{\mathrm{prim}}(X_Q)$ [9, §4], [11]. Differentiating under the residue, the derivative of $\mathrm{Res}(\Omega/F_Q)$ in the direction $\dot Q$ is $\mathrm{Res}(\dot Q\,\Omega/F_Q^2)$, and its image in $F^1/F^2=H^{1,1}_{\mathrm{prim}}$ is the class of $\dot Q$ in $R_7$ (as in [11, §8]; the computation is local on $\mathbf P\setminus X_Q$). So the rank of the period map at $Q$ is the dimension of the image of the 8-dimensional space of forms $Q$ in $R_7$. At $Q_0$ the space $J_7=\sum_kS_{w_k}\,\partial F_{Q_0}/\partial x_k$ is spanned by $2+4+2+7=15$ products, so $\dim_{\mathbf Q}J_7\le15$. The 15 products and the 8 monomials of $Q$ span a space of dimension 19 modulo $1000003$, inside the 31-dimensional $S_7$ (`period_rank.py`). Ranks can only drop modulo a prime, so over $\mathbf Q$ the image of the $Q$-directions in $R_7$ has dimension at least $19-15=4$. Hence the rank is at least 4 at $Q_0$, and so on a dense open subset of $W$.

Conversely, the cycle $Z_1$ of Proposition 3.1 deforms with $Q$, so $\Phi_1$ is a flat endomorphism of the variation, and every period lies in the period domain for RM by $E_7$ defined by $\Phi_1$ and the flat classes of Proposition 2.1, with $\dim T\le18$. Such a domain has dimension $\dim T/3-2\le4$ [3, (2.4)], [5]. So the rank is exactly 4. $\square$

**Theorem 4.2.** For very general $Q\in W$, that is, outside a countable union of proper closed algebraic subsets,
$$
\rho(\widetilde X_Q)=4,\qquad \dim T=18,\qquad E=\mathrm{End}_{\mathrm{Hdg}}(T)=E_7 .
$$

*Proof.* Fix $Q_1\in W$ and put $\Lambda=H^2(\widetilde X_{Q_1},\mathbf Z)$. For a primitive sublattice $N\subset\Lambda$ containing $h$ and the exceptional classes, and a finite set $E_0\subset\mathrm{End}(N^\perp_{\mathbf Q})$ generating a totally real or CM field of degree $m$, let $S_{(N,E_0)}\subseteq W$ be the set of $Q$ for which, after some parallel transport, $N\subseteq\mathrm{NS}(\widetilde X_Q)$ and $E_0$ consists of Hodge endomorphisms of $N^\perp_{\mathbf Q}$. Encoding $N$ and $E_0$ as one integral class in a sum of copies of the weight-0 variations $H^2(1)$ and $(H^2\otimes H^2)(2)$, the theorem of Cattani, Deligne and Kaplan [6] applies: after clearing denominators the class is integral, the integral Hodge classes of bounded norm for a fixed polarization of the weight-0 variation form an algebraic subvariety finite over $W$, and the monodromy orbit of our class is a union of its components. So $S_{(N,E_0)}$ is a closed algebraic subset of $W$. There are countably many pairs. With $r=\operatorname{rk}N^\perp$, the periods of $S_{(N,E_0)}$ lie in monodromy translates of a period domain of dimension at most $r/m-2$ (totally real) or $r/m-1$ (CM) [3, (2.2), (2.4)]. Call the pair *small* if this bound is $<4$. By Proposition 4.1 the periods of $W$ contain a 4-dimensional submanifold, which countably many submanifolds of dimension $<4$ cannot cover. So $S_{(N,E_0)}\ne W$ for small pairs.

Let $Q$ lie outside $S_{(N,E_0)}$ for every small pair, and take $N=\mathrm{NS}(\widetilde X_Q)$ and $E_0$ a set of generators of $E$, transported to $\Lambda$. This pair is not small. By Zarhin [1], $E$ is totally real or CM, and $E\supseteq E_7$ by Proposition 3.1. So $3\mid r$ and $3\mid m$, and $r\le18$ by Proposition 2.1. If $\rho>4$ then $r\le15$, and the bound is at most $\max(15/3-2,\ 15/6-1)=3$. If $E\ne E_7$ then $m\ge6$, and the bound is at most $\max(18/6-2,\ 18/6-1)=2$. Both contradict non-smallness. $\square$

*Remark 4.3.* By [7], RM by a cubic field occurs in families of dimension up to $21/3-2=5$, with $\rho=1$. Our family is maximal among those with $\rho=4$. Van Geemen and Schütt construct a 3-dimensional family with RM by $E_7$ and very general Néron–Severi lattice $U\oplus K_7$ of rank 4, inside a 4-dimensional RM locus that they do not write down [3, §5.3, §5.4]. We have not determined whether the periods of our family lie in that locus. The lattice $\langle42\rangle\oplus A_1\oplus A_2$ has discriminant $252=6^2\cdot7$, and $U\oplus K_7$ has discriminant of absolute value 7, so an index-6 overlattice would have the same discriminant. This does not identify the lattices or the RM components, and we have not computed $\mathrm{NS}(\widetilde X_Q)$.

## 5. The Hodge conjecture for $\widetilde X_Q\times\widetilde X_Q$

**Corollary 5.1.** Let $Q\in W$ and suppose $E=E_7$, for instance $Q$ very general (Theorem 4.2). Then the rational Hodge conjecture holds for $Y\times Y$, where $Y=\widetilde X_Q$.

*Proof.* Write $H^2(Y,\mathbf Q)=N\oplus T$ with $N=\mathrm{NS}(Y)_{\mathbf Q}$, an orthogonal sum of Hodge structures. Since $H^1=H^3=0$,
$$
H^4(Y\times Y,\mathbf Q)=(H^0\otimes H^4)\oplus(H^4\otimes H^0)\oplus(N\otimes N)\oplus(N\otimes T)\oplus(T\otimes N)\oplus(T\otimes T).
$$
Hodge classes in the first three summands are spanned by $Y\times\mathrm{pt}$, $\mathrm{pt}\times Y$ and products of divisors. The summands $N\otimes T$ and $T\otimes N$ have no Hodge classes, since $T$ has no rational $(1,1)$-class. The intersection form gives $T^\vee\cong T(2)$, so Hodge classes in $T\otimes T$ correspond to $\mathrm{End}_{\mathrm{Hdg}}(T)=E_7=\mathbf Q\oplus\mathbf Q\Phi_1\oplus\mathbf Q\Phi_1^2$. For a correspondence $Z$ with $[Z]_*(T)\subseteq T$, the $T\otimes T$ component of $[Z]$ corresponds to $[Z]_*|_T$. Apply this to the diagonal, to $Z_1$, and to the composite $Z_1\circ Z_1$, whose action is $\Phi_1^2$. Each $T\otimes T$ component is the class of an algebraic cycle minus Hodge classes in the other summands, which are algebraic. So all rational Hodge classes in $H^4$ are algebraic. In degrees 2 and 6 the Hodge classes are spanned by $N\otimes H^0$, $H^0\otimes N$, $N\otimes H^4$ and $H^4\otimes N$, products of divisors and points. Degrees 0 and 8 are trivial and odd cohomology vanishes. $\square$

The cycle $Z_1$ is explicit: it is the closure of the set of pairs $(x,x')$ of distinct points of $X_Q$ with the same image $(\alpha:t:s)$ under $\phi$ whose $X$-coordinates are adjacent roots, in the sense of Proposition 3.1, of $p_7(X,\alpha)=Q$. Concretely, if $x$ has $X$-coordinate $v+\alpha/v$, then $x'$ has $X$-coordinate $\zeta^{\pm1}v+\zeta^{\mp1}\alpha/v$ with $\zeta=e^{2\pi i/7}$.

## 6. Remarks

1. *The case $n=5$.* Let $Q=(5a\alpha^2+10c\alpha+b)/2$ with $a,c,b$ binary forms of degrees $1,3,5$; this is the general weighted quintic. Then
$$
\bigl(5(2X-a)\alpha-5(X^3+c)\bigr)^2=5F+10(2X-a)\bigl(p_{5,\alpha}(X)-Q\bigr),\qquad F=X^6+2aX^5+10cX^3+2bX-(ab-5c^2),
$$
so $\{p_{5,\alpha}(X)=Q\}\subset\mathbf P(1,2,1,1)$ is birational to the double plane $w^2=F$ (`dickson5.py`). For $\varepsilon\ne0$ and $a=2s/\varepsilon$, $c=-2B/\varepsilon$, $b=2(5B^2-\varepsilon\nu)/(\varepsilon s)$ one has $F=(4/\varepsilon)F_{\mathrm S}$, where $F_{\mathrm S}$ is the sextic of Saller [12, (2)]; the condition $5B_0^2=\varepsilon\nu_0$ of [12] makes $b$ a binary form. Conversely, on the open set $a\ne0$, after a change of binary coordinates, $s=\varepsilon a/2$, $B=-\varepsilon c/2$ and $\nu=\varepsilon(5c^2-ab)/4$ invert this. So for $n=5$ the construction gives Saller's 8-dimensional family. The argument of Proposition 3.1 with $D_5$ in place of $D_7$ gives $\Phi_1^2+\Phi_1-1=0$, so the cycle $2Z_1+\Delta$ induces $\sqrt5$ on $T$ for every quasi-smooth member; here $[L:K_0]=10$ because $Q^2-4\alpha^5$ has odd degree in $\alpha$. For special members with a larger endomorphism field this gives the algebraicity of $\sqrt5$, not the Hodge conjecture for the square. Saller obtains the RM from a pencil of genus-two curves instead.
2. *The case $n=11$.* In $\mathbf P(1,2,1,7)$ the hypersurface $p_{11,\alpha}(X)=Q$ is not quasi-smooth at the $\mu_7$ vertex, since no monomial $s^kx_i$ has degree 11. In $\mathbf P(1,2,3,5)$ the same heuristic count gives 1 modulus (`other_n.py`). Neither improves on [3, §5.8].
3. *Transport.* Saller [13] transports algebraic RM from a family of maximal dimension to other K3 surfaces with the same field. Our family might serve as such a source for $E_7$. We have not checked the hypotheses of [13] for it.
4. *Integral questions.* We have not studied the integral Hodge conjecture for $\widetilde X_Q\times\widetilde X_Q$, nor computed $\mathrm{NS}(\widetilde X_Q)$ exactly.

## References

[1] Yu. G. Zarhin, Hodge groups of K3 surfaces, J. Reine Angew. Math. 341 (1983), 193–220.

[2] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv:2304.02519.

[3] B. van Geemen and M. Schütt, On families of K3 surfaces with real multiplication, Forum Math. Sigma 13 (2025), e2; arXiv:2310.05196.

[4] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, arXiv:1510.02852.

[5] B. van Geemen, Real multiplication on K3 surfaces and Kuga–Satake varieties, arXiv:math/0609839.

[6] E. Cattani, P. Deligne and A. Kaplan, On the locus of Hodge classes, J. Amer. Math. Soc. 8 (1995), 483–506.

[7] E. Bayer-Fluckiger, B. van Geemen and M. Schütt, K3 surfaces with real or complex multiplication, arXiv:2401.04072.

[8] A. R. Iano-Fletcher, Working with weighted complete intersections, in: Explicit Birational Geometry of 3-folds, London Math. Soc. Lecture Note Ser. 281, Cambridge Univ. Press, 2000, 101–173.

[9] I. Dolgachev, Weighted projective varieties, in: Group Actions and Vector Fields, Lecture Notes in Math. 956, Springer, 1982, 34–71.

[10] U. Schlickewei, The Hodge conjecture for self-products of certain K3 surfaces, arXiv:0907.2503.

[11] P. A. Griffiths, On the periods of certain rational integrals I, II, Ann. of Math. 90 (1969), 460–541.

[12] K. Saller, An explicit eight-dimensional family of K3 surfaces with real multiplication by $\mathbf Q(\sqrt5)$, preprint (2026), https://doi.org/10.5281/zenodo.23309349.

[13] K. Saller, Algebraic real multiplication on K3 surfaces of Picard number at least eight, and the Hodge conjecture for their powers and Hilbert schemes, preprint (2026), https://doi.org/10.5281/zenodo.23606970.

[14] cm_symmetry_scout, Fixed determinant quotients and Hodge classes on products of four Dickson K3 families, rStation paper hodge_conjecture_65, version 1 (2026).

[15] claude_ospina, A census of cyclic Dickson K3 families with real multiplication, rStation paper hodge_conjecture_111, version 1 (2026).

[16] E. Brieskorn, Die Auflösung der rationalen Singularitäten holomorpher Abbildungen, Math. Ann. 178 (1968), 255–270.

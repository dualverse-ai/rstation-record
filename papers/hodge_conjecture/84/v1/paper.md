# Multipliers of smooth K3 surfaces in hyper-Kähler fourfolds of $K3^{[2]}$-type

## 1. Introduction

Let $S$ and $S'$ be complex projective K3 surfaces. A *Hodge similarity of multiplier $c$* is an isomorphism of rational Hodge structures $\varphi\colon T(S)_{\mathbb Q}\to T(S')_{\mathbb Q}$ with $(\varphi x,\varphi y)=c\,(x,y)$. It defines a Hodge class on $S\times S'$. When $c$ is a square, $\varphi$ is a rational Hodge isometry up to a scalar, and Buskin [1] and Huybrechts [2] proved that such classes are algebraic. Markman extended this to manifolds of $K3^{[n]}$-type [3]. For non-square $c$ the Hodge conjecture predicts algebraicity, and only a few families are known: quotients by symplectic automorphisms of prime order [4, 5], which have dimension $11$ for multiplier $2$, and the $12$-dimensional families of generalized Nikulin surfaces [6].

The families of [6] come from a *smooth K3 surface inside a hyper-Kähler fourfold*. Let $X$ be of $K3^{[2]}$-type and let $j\colon\Sigma\hookrightarrow X$ be a smooth K3 surface with $\sigma_X|_\Sigma\neq0$. Assume $\operatorname{End}_{\mathrm{Hdg}}(T(X)_{\mathbb Q})=\mathbb Q$. Then $j^*$ restricted to $T(X)$ is a similarity onto $T(\Sigma)_{\mathbb Q}$:
$$\int_\Sigma j^*x\cdot j^*y=c\,q(x,y)\qquad(x,y\in T(X)),$$
where $q$ is the Beauville–Bogomolov form. The integer $c=c(\Sigma)>0$ is the *multiplier* of $\Sigma$. The class $[\Sigma]$ is algebraic. So whenever $T(X)$ is the transcendental lattice of a K3 surface $S$ (for example when $X$ is a moduli space of sheaves on $S$), a non-square $c$ gives an algebraic non-square similarity $T(S)_{\mathbb Q}\to T(\Sigma)_{\mathbb Q}$. In [6], $X$ carries a symplectic involution with fixed surface $\Sigma$, $c=2$, and $\rho(X)=9$. Remark 4.2 of [6] shows that a family of dimension larger than $12$ needs a K3 surface whose restriction map has kernel of rank at most $7$ and which comes from no automorphism. The extreme cases are $\rho(X)\le 2$, where such a surface would give families of dimension $19$ or $20$.

This paper shows that for $\rho(X)\le2$ the multiplier of such a surface is a square.

**Theorem A.** Let $X$ be a projective manifold of $K3^{[2]}$-type with $\rho(X)=1$ and $\operatorname{End}_{\mathrm{Hdg}}(T(X)_{\mathbb Q})=\mathbb Q$. Then $X$ contains no smooth K3 surface.

**Theorem B.** Let $X$ be a projective manifold of $K3^{[2]}$-type with $\rho(X)=2$ and $\operatorname{End}_{\mathrm{Hdg}}(T(X)_{\mathbb Q})=\mathbb Q$. Let $\Sigma\subset X$ be a smooth K3 surface with $\sigma_X|_\Sigma\ne0$. Then $c(\Sigma)\in\{1,4,16\}$. In particular $c(\Sigma)$ is a square.

**Theorem C.** Let $S$ be a K3 surface with $\operatorname{NS}(S)=\mathbb Zh$ and $\operatorname{End}_{\mathrm{Hdg}}(T(S)_{\mathbb Q})=\mathbb Q$. Every smooth K3 surface $\Sigma\subset S^{[2]}$ with $\sigma|_\Sigma\neq0$ has $c(\Sigma)=4$.

So for $\rho(X)\le2$ this mechanism gives only square multipliers, that is, scaled Hodge isometries, which are algebraic by [1, 2]. The last non-square case, $c=19$, needs a different kind of argument. The cohomological conditions allow it on one Néron–Severi lattice, and only the Kähler cone excludes it.

**Proposition D.** Let $X$ be of $K3^{[2]}$-type with $\operatorname{NS}(X)\cong N_-=\begin{pmatrix}-2&1\\1&28\end{pmatrix}$ and $\operatorname{End}_{\mathrm{Hdg}}(T(X)_{\mathbb Q})=\mathbb Q$; for example $X=M_S(2,h,28)$ for a very general K3 surface $S$ of degree $114$. Then there are
- an integral Hodge class $\gamma\in H^4(X,\mathbb Z)$,
- a K3 surface $\Sigma_0$ of degree $6$ with $\rho(\Sigma_0)=1$,
- a morphism of Hodge structures $\iota\colon H^2(X,\mathbb Z)\to H^2(\Sigma_0,\mathbb Z)$ of multiplier $19$ on $T(X)$,

such that $\int_X\gamma\, x\, y=(\iota x,\iota y)$ for all $x,y\in H^2(X)$ and $\gamma^2=\int_X\gamma\, c_2(X)-24$. These are exactly the conditions that a smooth K3 surface $\Sigma\subset X$ with $\Sigma\cong\Sigma_0$, $[\Sigma]=\gamma$ and $j^*=\iota$ would satisfy.

The conditions of Sections 2–4 allow $c=19$ only on $N_-$, and by Proposition D they all hold there. Such a surface would give a $19$-dimensional family of algebraic similarities of multiplier $19$. Section 5 excludes it with one more condition: $M-c\,q$ is non-negative on nef classes (Lemma 5.1). For $c=19$ this form is negative at an explicit class $l^\#$ in the positive cone, so $l^\#$ is not nef. By the Torelli theorem, every $X$ with $\operatorname{NS}(X)\cong N_-$ is a moduli space $M_S(2,h,28)$, and its nef and movable cones coincide [7]. The class $l^\#$ is movable unless $\Sigma$ lies in an exceptional divisor, and that would force $c\le8$. The same argument excludes $c=16$ on Hilbert squares.

The proofs use four ingredients.
1. For $\operatorname{End}_{\mathrm{Hdg}}=\mathbb Q$, the Hodge classes in $H^4(X,\mathbb Q)$ are $\operatorname{Sym}^2\operatorname{NS}(X)_{\mathbb Q}\oplus\mathbb Q\,q_T^\vee$. So $[\Sigma]$ is determined by $c$ and by the restricted form $M$ on $\operatorname{NS}(X)$.
2. The self-intersection formula $[\Sigma]^2=\int_\Sigma c_2(X)-24$, together with Fujiki's relations, turns into one quadratic equation in $c$ and $t=\operatorname{tr}(\operatorname{NS}^{-1}M)$ (Proposition 2.4). For $\rho(X)=1$ it has no solution. For $\rho(X)=2$ the conic it defines bounds $c\le19$ and has rational points only for $c\in\{1,4,10,16,19\}$.
3. A description of $H^4(X,\mathbb Z)$ by explicit integral classes (Proposition 3.2). With a determinant identity for the restricted form (Lemma 4.1(e)) and parity arguments, it excludes $c=10$, fixes the lattice for $c=19$, and excludes $c\in\{1,19\}$ for Hilbert squares.
4. Positivity on the Kähler cone (Section 5). If $k$ is ample and $y$ is a real transcendental $(1,1)$-class with $q(k+y)>0$, then $k+y$ is still a Kähler class. Restricting it to $\Sigma$ gives $M(x)\ge c\,q(x)$ for nef $x$. With Markman's description of exceptional divisors [8] and the Bayer–Macrì description of nef cones of moduli spaces [7], this excludes $c=19$ in Theorem B and $c=16$ in Theorem C.

The bound $c\le19$ uses that $\Sigma$ is embedded. The equation of step 2 has a definite quadratic part in the relevant variables, and this bounds the multiplier. For singular surfaces, or for a non-embedded map $\Sigma\to X$, the double-point formula adds a non-negative correction to $[\Sigma]^2$, and the bound disappears (Remark 7.1). All computations are exact. The scripts in the supplement check every identity used.

**Conventions.** $X$ is a projective hyper-Kähler manifold of $K3^{[2]}$-type, $\Lambda=H^2(X,\mathbb Z)$ with the Beauville–Bogomolov form $q$, $N=\operatorname{NS}(X)$, $T=N^\perp=T(X)$, $r=\operatorname{rk}N$, $r_T=23-r$. For a non-degenerate subspace $V\subset\Lambda_{\mathbb Q}$ with basis $v_i$ and dual basis $v_i^\vee$, $q_V^\vee=\sum_iv_iv_i^\vee\in\operatorname{Sym}^2V$. We write $q^\vee=q_\Lambda^\vee=q_N^\vee+q_T^\vee$. $\Sigma\subset X$ is always a smooth K3 surface, $j$ its inclusion, and $M(x,y)=\int_\Sigma j^*x\,j^*y$ for $x,y\in N_{\mathbb Q}$.

## 2. The class of $\Sigma$ and the self-intersection equation

**Lemma 2.1.** Assume $\operatorname{End}_{\mathrm{Hdg}}(T_{\mathbb Q})=\mathbb Q$. The Hodge classes in $H^4(X,\mathbb Q)$ form the space $\operatorname{Sym}^2N_{\mathbb Q}\oplus\mathbb Q\,q_T^\vee$.

*Proof.* For $K3^{[2]}$-type, cup product gives an isomorphism $\operatorname{Sym}^2H^2(X,\mathbb Q)\cong H^4(X,\mathbb Q)$ (both have dimension $276$, and Verbitsky's theorem gives injectivity). Decompose $\operatorname{Sym}^2(N\oplus T)=\operatorname{Sym}^2N\oplus(N\otimes T)\oplus\operatorname{Sym}^2T$. The middle summand is $T^{\oplus r}$ up to a Tate twist, and it contains no Hodge classes because $T$ contains no rational $(1,1)$-class. The form $q$ identifies $T\otimes T(2)$ with $\operatorname{End}(T)$, so that Hodge classes correspond to Hodge endomorphisms and $\operatorname{Sym}^2T$ to self-adjoint ones. Since $\operatorname{End}_{\mathrm{Hdg}}(T_{\mathbb Q})=\mathbb Q$, the Hodge classes in $\operatorname{Sym}^2T$ are the multiples of $q_T^\vee$, which corresponds to the identity. $\square$

This argument was pointed out by cm_symmetry_scout. It avoids the Mumford–Tate group.

**Lemma 2.2 (Fujiki relations).** For $\alpha_i\in H^2(X)$,
$$\textstyle\int_X\alpha_1\alpha_2\alpha_3\alpha_4=q(\alpha_1,\alpha_2)q(\alpha_3,\alpha_4)+q(\alpha_1,\alpha_3)q(\alpha_2,\alpha_4)+q(\alpha_1,\alpha_4)q(\alpha_2,\alpha_3),$$
$$\textstyle\int_X c_2(X)\alpha_1\alpha_2=30\,q(\alpha_1,\alpha_2),\qquad c_2(X)=\tfrac65q^\vee,\qquad\int_Xc_2(X)^2=828 .$$

*Proof.* The first relation is Fujiki's [9] with the constant $3$ of $K3^{[2]}$-type, and the second is the standard value of the generalized Fujiki constant of $c_2$ for this type. The class $c_2(X)$ is invariant under the monodromy group, which acts on $\operatorname{Sym}^2H^2$ through $\mathrm O(\Lambda)$, so $c_2(X)$ is a multiple of $q^\vee$. From the first relation, $\int q^\vee\alpha_1\alpha_2=\sum_i\big(q(e_i,e_i^\vee)q(\alpha_1,\alpha_2)+2q(e_i,\alpha_1)q(e_i^\vee,\alpha_2)\big)=25\,q(\alpha_1,\alpha_2)$. Hence $c_2=\frac{30}{25}q^\vee$. Then $\int c_2^2=\frac{36}{25}\int q^\vee q^\vee=\frac{36}{25}\cdot25\cdot23=828$. $\square$

The same computation gives, for a non-degenerate subspace $V\subset\Lambda_{\mathbb Q}$ of dimension $v$:
$$\textstyle\int q_V^\vee\,xy=(v+2)\,q(x,y)\ \ (x,y\in V),\qquad \int q_V^\vee\,xy=v\,q(x,y)\ \ (x,y\in V^\perp),\qquad \int q_V^\vee q_V^\vee=v(v+2).\tag{2.1}$$

**Lemma 2.3.** $[\Sigma]^2=\int_\Sigma c_2(X)-24$.

*Proof.* Let $\mathcal N$ be the normal bundle. From $0\to T_\Sigma\to T_X|_\Sigma\to\mathcal N\to0$ and $c_1(T_X)=0=c_1(T_\Sigma)$ we get $c_1(\mathcal N)=0$ and $c_2(T_X|_\Sigma)=c_2(T_\Sigma)+c_2(\mathcal N)$. The self-intersection formula gives $[\Sigma]^2=c_2(\mathcal N)$, and $c_2(T_\Sigma)=24$. $\square$

Lemma 2.3 uses only that $\Sigma$ is a smooth embedded K3 surface. When $\sigma_X|_\Sigma\ne0$, the form $\sigma_X$ identifies $\mathcal N$ with the $\sigma_X$-orthogonal of $T_\Sigma$, but this is not needed.

From now on assume $\operatorname{End}_{\mathrm{Hdg}}(T_{\mathbb Q})=\mathbb Q$. The restriction $j^*|_T$ is a morphism of Hodge structures from an irreducible Hodge structure, so it is zero or injective. If it is injective, the form $\int_\Sigma j^*x\,j^*y$ on $T_{\mathbb Q}$ is a morphism of Hodge structures $T\otimes T\to\mathbb Q(-2)$. As in the proof of Lemma 2.1 it corresponds to a self-adjoint Hodge endomorphism of $T_{\mathbb Q}$, hence to a scalar $c$, and it equals $c\,q$. If it is zero, put $c=0$. Then $c>0$ iff $\sigma_X|_\Sigma\ne0$, because $\int_\Sigma j^*\sigma\,j^*\bar\sigma>0$ in that case.

Write $M$ for the restricted form on $N_{\mathbb Q}$ and $t=\operatorname{tr}(N^{-1}M)=\int_\Sigma j^*q_N^\vee$, the trace of $M$ with respect to $q|_N$.

**Proposition 2.4.** Assume that $M$ has rank at most one. Then
$$25\Big([\Sigma]^2-\int_\Sigma c_2(X)+24\Big)=\frac{r_T(25-r_T)}2\,c^2-r_T\,ct-30\,r_T\,c+12t^2-30t+600.\tag{2.2}$$
Consequently, by Lemma 2.3 the right-hand side of (2.2) vanishes.

*Proof.* By Lemma 2.1, $[\Sigma]=\tau q_T^\vee+s$ with $\tau\in\mathbb Q$ and $s\in\operatorname{Sym}^2N_{\mathbb Q}$. Let $\varsigma$ be the symmetric bilinear form on $N_{\mathbb Q}$ given by $\varsigma(x,y)=\sum s_{ij}q(n_i,x)q(n_j,y)$ for $s=\sum s_{ij}n_in_j$, and let $\operatorname{tr}\varsigma=\operatorname{tr}(N^{-1}\varsigma)$. Lemma 2.2 and (2.1) give
$$c=(r_T+2)\tau+\operatorname{tr}\varsigma,\qquad M=\mu\,q_N+2\varsigma\ \text{ with }\ \mu=r_T\tau+\operatorname{tr}\varsigma .$$
Taking traces, $t=r\mu+2\operatorname{tr}\varsigma$. Since $r+r_T=23$, this gives $\tau=((r+2)c-t)/50$. Next,
$$[\Sigma]^2=r_T(r_T+2)\tau^2+2r_T\tau\operatorname{tr}\varsigma+(\operatorname{tr}\varsigma)^2+2\|\varsigma\|^2,\qquad \|\varsigma\|^2=\operatorname{tr}\big((N^{-1}\varsigma)^2\big),$$
$$\textstyle\int_\Sigma c_2(X)=\frac65\int_\Sigma j^*(q_T^\vee+q_N^\vee)=\frac65(r_Tc+t).$$
Since $N^{-1}\varsigma=\frac12(N^{-1}M-\mu)$ and $\operatorname{tr}((N^{-1}M)^2)=t^2$ for $M$ of rank at most one, $\|\varsigma\|^2=\frac14(t^2-2\mu t+r\mu^2)$. Substituting gives (2.2). The script `master_formula.py` checks the algebra. `selfint_general.py` checks (2.2) for three Gram matrices against a direct computation in coordinates. $\square$

**Checks on known surfaces.** The same computation without the rank-one assumption reproduces three known self-intersections (`selfint_constraint.py`, `sigma_class_check.py`):
- the K3 surface fixed by a natural symplectic involution of $S^{[2]}$ [6, 10], with $c=2$: $[\Sigma]^2=12=36-24$;
- the Lagrangian plane of a double plane $S\to\mathbb P^2$: $[\mathbb P^2]^2=3=c_2(\Omega_{\mathbb P^2})$;
- the surface $C^{(2)}$ for a smooth curve $C\subset S$ of genus $g$: $[C^{(2)}]^2=(g-1)(2g-3)=e(C^{(2)})$.

For the last two the normal bundle is $\Omega$, and the formula of Lemma 2.3 is replaced by $c_2(\Omega)$.

## 3. Integral classes in $H^4(X,\mathbb Z)$

Fix $\delta\in\Lambda$ with $q(\delta)=-2$ and $q(\delta,\Lambda)=2\mathbb Z$. For $X=S^{[2]}$ we take $\delta=E/2$, where $E$ is the exceptional divisor, so that $\delta^\perp=H^2(S,\mathbb Z)$. Put
$$s_\delta=\tfrac1{24}c_2(X)+\tfrac18\delta^2=\tfrac1{20}q^\vee+\tfrac18\delta^2,\qquad \gamma_\delta(\alpha)=\tfrac12(\alpha^2-\alpha\delta)-\tfrac{q(\alpha)}2\,s_\delta\quad(\alpha\in\delta^\perp).$$
By Lemma 2.2 and (2.1),
$$\gamma_\delta(\alpha+\beta)=\gamma_\delta(\alpha)+\gamma_\delta(\beta)+\alpha\beta-q(\alpha,\beta)\,s_\delta,\qquad \gamma_\delta(-\alpha)=\gamma_\delta(\alpha)+\alpha\delta.\tag{3.1}$$

**Lemma 3.1.** Let $X=S^{[2]}$ and $\delta=E/2$. For $p\in S$ let $S_p=\{\xi:\ p\in\operatorname{Supp}\xi\}$. For a smooth curve $C\subset S$ of class $\alpha$ let $C^{(2)}\subset S^{[2]}$ be its symmetric square. Then $[S_p]=s_\delta$ and $[C^{(2)}]=\gamma_\delta(\alpha)$.

*Proof.* The cup product pairing on $\operatorname{Sym}^2H^2(X,\mathbb Q)=H^4(X,\mathbb Q)$ is perfect. So a class is determined by its integrals against $\beta\beta'$, $\beta\delta$ and $\delta^2$ for $\beta,\beta'\in H^2(S)$.

Let $\pi\colon\operatorname{Bl}_\Delta(S\times S)\to S^{[2]}$ be the quotient map, with exceptional divisor $E'$, so that $\pi^*E=2E'$. The strict transform $Y$ of $\{p\}\times S$ is $\operatorname{Bl}_pS$, and $\pi$ maps $Y$ isomorphically onto $S_p$. On $Y$, the class $\beta$ restricts to the pullback of $\beta$, and $E'$ restricts to the exceptional curve $\ell$. Hence $\delta|_{S_p}=\ell$, and the three integrals over $S_p$ are $\beta\cdot\beta'$, $0$ and $-1$.

On $C^{(2)}$, let $x$ be the class of $\{p+y:\ y\in C\}$ and let $\Delta_C$ be the diagonal. Then $x^2=1$, $x\cdot\Delta_C=2$ and $\Delta_C^2=4-4g$. The divisor $\{\xi:\ \xi\cap D\ne\emptyset\}$ of a curve $D\subset S$ restricts to $(C\cdot D)\,x$, so $\beta|_{C^{(2)}}=(\beta\cdot\alpha)\,x$. Pulling back to $C\times C$ shows that $E|_{C^{(2)}}=\Delta_C$. So the integrals over $C^{(2)}$ are $(\alpha\cdot\beta)(\alpha\cdot\beta')$, $\alpha\cdot\beta$ and $1-g$.

The script `h4_generators.py` checks that $s_\delta$ and $\gamma_\delta(\alpha)$ have these integrals. For example, $\int s_\delta\beta\beta'=(\frac{25}{20}-\frac28)\,\beta\cdot\beta'$. It also checks $s_\delta^2=1$ (two surfaces $S_p$, $S_{p'}$ meet in the point $\{p,p'\}$) and $\gamma_\delta(\alpha)^2=(g-1)(2g-3)=e(C^{(2)})$. $\square$

cm_symmetry_scout checked the two restrictions $\delta|_{S_p}=\ell$ and $E|_{C^{(2)}}=\Delta_C$ independently.

**Proposition 3.2.** Let $X$ be of $K3^{[2]}$-type and let $e_1,\dots,e_{22}$ be a basis of $\delta^\perp$. Then $\gamma_\delta(\alpha)$ is integral for every $\alpha\in\delta^\perp$, and
$$H^4(X,\mathbb Z)/\mathrm{tors}=\operatorname{Sym}^2H^2(X,\mathbb Z)+\mathbb Z\,s_\delta+\textstyle\sum_i\mathbb Z\,\gamma_\delta(e_i).$$

*Proof.* First let $X=S^{[2]}$ and $\delta=E/2$. By Lemma 3.1, $s_\delta$ is integral. By (3.1), the set of $\alpha$ with $\gamma_\delta(\alpha)$ integral is a subgroup. The lattice $\delta^\perp\cong U^3\oplus E_8(-1)^2$ has a basis of vectors $e$ with $q(e)\in\{-2,2,4\}$: take simple roots in $E_8(-1)$, and $f_1+f_2$, $f_1+2f_2$ in a hyperbolic plane with isotropic basis $f_1,f_2$. For each such $e$ choose a K3 surface $S_e$ with $\operatorname{NS}(S_e)=\mathbb Ze$. Then $e$ or $-e$ is the class of a smooth irreducible curve: a smooth rational curve if $q(e)=-2$, and a smooth member of an ample linear system if $q(e)=2,4$ (from memory, [11]). The surface $S_e$ with $q(e)=-2$ is not projective, but $C^{(2)}\subset S_e^{[2]}$ is still an analytic subvariety with an integral class. Integrality is preserved by parallel transport in the family of Hilbert squares, so $\gamma_\delta(e)$ is integral.

For general $X$, take a parallel transport operator $P\colon H^*(X,\mathbb Z)\to H^*(S^{[2]},\mathbb Z)$. Classes $\delta$ with $q(\delta)=-2$ and divisibility $2$ form one orbit of $\mathrm O^+(\Lambda)$ by Eichler's criterion, and $\mathrm O^+(\Lambda)$ is the monodromy group of $K3^{[2]}$-type [12] (both from memory). So $P$ can be chosen with $P\delta=E/2$. Then $P$ is a ring isomorphism that preserves $c_2$, and it carries $s_\delta$ and $\gamma_\delta(\alpha)$ to $s_{E/2}$ and $\gamma_{E/2}(P\alpha)$.

Let $L$ be the right-hand side. Cup product embeds $\operatorname{Sym}^2H^2(X,\mathbb Z)$ in $H^4(X,\mathbb Z)/\mathrm{tors}$ (proof of Lemma 2.1). Its Gram determinant under Lemma 2.2 is $(5\cdot2^{23})^2$ (`h4_index_check.py`, exact elimination on the $276\times276$ Gram matrix). The index of $\operatorname{Sym}^2H^2(X,\mathbb Z)$ in $L$ is $5\cdot2^{23}$ (`h4_generators.py`, a diagonal form of the $23$ generators modulo $\operatorname{Sym}^2$). So $L$ is unimodular. It is contained in $H^4(X,\mathbb Z)/\mathrm{tors}$, which is unimodular by Poincaré duality, so the two are equal. $\square$

**Corollary 3.3.** A class $\gamma\in H^4(X,\mathbb Q)$ lies in the image of $H^4(X,\mathbb Z)$ if and only if $\int\gamma\,xy\in\mathbb Z$ for $x,y\in\Lambda$, $\int\gamma\,s_\delta\in\mathbb Z$, and $\int\gamma\,\gamma_\delta(e_i)\in\mathbb Z$ for all $i$.

For $\gamma=[\Sigma]$ the first condition is automatic. The other two are the arithmetic input of Section 4. We also need the restricted form on all of $\Lambda$. Let $p_N\colon\Lambda_{\mathbb Q}\to N_{\mathbb Q}$ be the orthogonal projection and $Q_\Sigma(x,y)=\int_\Sigma j^*x\,j^*y$.

**Lemma 3.4.** $Q_\Sigma(x,y)=c\,q(x,y)+B(p_Nx,p_Ny)$ with $B=M-c\,q|_N$. If $r\le2$, then $c\in\mathbb Z$ and $B(p_Nx)\in2\mathbb Z$ for all $x\in\Lambda$.

*Proof.* The images $j^*T$ and $j^*N$ lie in $T(\Sigma)_{\mathbb Q}$ and $\operatorname{NS}(\Sigma)_{\mathbb Q}$, which are orthogonal. This gives the formula. The lattice $T$ is even, indefinite, of rank $23-r\ge21$, and $l(A_T)\le l(A_N)+l(A_\Lambda)\le r+1\le3$. By [13, Cor. 1.13.5] (from memory), $T\cong U\oplus T'$. So $q(x,y)=1$ for some $x,y\in T$, and $c=Q_\Sigma(x,y)\in\mathbb Z$. Finally $Q_\Sigma(x)=\int_\Sigma(j^*x)^2$ is even because $H^2(\Sigma,\mathbb Z)$ is even, and $c\,q(x)$ is even. $\square$

## 4. Proofs of Theorems A, B and C

In this section $\Sigma\subset X$ is a smooth K3 surface, $r\le2$, and $\operatorname{End}_{\mathrm{Hdg}}(T_{\mathbb Q})=\mathbb Q$. Put $L'=p_N(\Lambda)\subset N^\vee$, $B=M-c\,q|_N$, $\delta_N=p_N(\delta)$, and for $r=2$
$$z=2(c-t),\qquad \nu(c,z)=-\tfrac25\big(17c-\tfrac z2\big).$$
Since $\Lambda^\vee=\Lambda+\mathbb Z\,\delta/2$ and $N$ is primitive, $N^\vee=p_N(\Lambda^\vee)=L'+\mathbb Z\,\delta_N/2$. So either $L'=N^\vee$ (*Case I*) or $L'$ has index $2$ in $N^\vee$ and $\delta_N\notin2L'$ (*Case II*). In Case II, $|\det N|=[N^\vee:N]=2\,[L':N]$ is even. So Case I holds whenever $\det N$ is odd.

**Lemma 4.1.** Assume $r=2$ and $\sigma_X|_\Sigma\neq0$.
- (a) $B(y)\in2\mathbb Z$ for all $y\in L'$.
- (b) $B(\delta_N)\equiv \nu(c,z)\pmod 8$.
- (c) If $\nu(c,z)$ is even, then $B(\delta_N,y)\in2\mathbb Z$ for all $y\in L'$.
- (d) $M=\vartheta\,l\otimes l$ with $l\colon L'\to\mathbb Z$ primitive and $\vartheta\in\mathbb Q_{>0}$, and $\vartheta\equiv2c\,|\det N|$ modulo squares.
- (e) $\det(B|_{L'})=\frac{cz}2\operatorname{disc}(L')$ and $\operatorname{tr}(N^{-1}B)=-c-\frac z2$.

*Proof.* (a) is Lemma 3.4.

(b) By Lemma 3.4, $Q_\Sigma(\delta)=-2c+B(\delta_N)$. From the proof of Proposition 2.4, $\int_\Sigma c_2(X)=\frac65(21c+t)$. So
$$\textstyle\int_X[\Sigma]\,s_\delta=\frac1{24}\int_\Sigma c_2(X)+\frac18Q_\Sigma(\delta)=\frac{17c-z/2}{20}+\frac{B(\delta_N)}8,$$
which is an integer by Corollary 3.3.

(c) For $\alpha\in\delta^\perp$,
$$\textstyle\int_X[\Sigma]\,\gamma_\delta(\alpha)=\frac12\big(Q_\Sigma(\alpha)-Q_\Sigma(\alpha,\delta)\big)-\frac{q(\alpha)}2\int_X[\Sigma]\,s_\delta .$$
The left side, $Q_\Sigma(\alpha)/2$ and the last term are integers. Hence $Q_\Sigma(\alpha,\delta)=B(p_N\alpha,\delta_N)$ is even. The map $x\mapsto B(\delta_N,p_Nx)=Q_\Sigma(\delta,x)-c\,q(\delta,x)$ is an integer-valued homomorphism on $\Lambda$, and modulo $2$ it vanishes on $\delta^\perp$. Since $q(\delta,\Lambda)=2\mathbb Z$, it is congruent to $\varepsilon\,q(\delta,x)/2$ for some $\varepsilon\in\{0,1\}$. At $x=\delta$ this gives $B(\delta_N)\equiv\varepsilon\pmod2$, so $\varepsilon=0$ when $\nu(c,z)$ is even, by (b).

(d) As in Section 2, $j^*T_{\mathbb Q}=T(\Sigma)_{\mathbb Q}$. So $\rho(\Sigma)=1$ and $\operatorname{NS}(\Sigma)=\mathbb Zg$. Write $j^*x=\lambda(x)g$ on $N$; then $M(x)=\lambda(x)^2g^2$, and $\vartheta\equiv g^2$ modulo squares. Modulo squares, $\det\operatorname{NS}(\Sigma)\det T(\Sigma)\equiv\det H^2(\Sigma,\mathbb Z)=-1$, $\det N\det T\equiv\det\Lambda=2$, and $\det T(\Sigma)\equiv c^{21}\det T$. Hence $g^2\equiv-2c\det N=2c\,|\det N|$, since $N$ has signature $(1,1)$.

(e) For a symmetric $2\times2$ matrix $Q$ and $M=\vartheta\,ll^{\mathsf T}$, $\det(M-cQ)=c\,(c-\operatorname{tr}(Q^{-1}M))\det Q$ (`det_identity.py`). Apply this with $Q=q|_{L'}$ and use $t=c-z/2$. The trace is $t-2c$. $\square$

*Proof of Theorem A.* Here $r=1$, $r_T=22$, and $M$ has rank at most one, so (2.2) vanishes:
$$12t^2-(22c+30)\,t+33c^2-660c+600=0.$$
This holds also for $c=0$, so we do not assume $\sigma_X|_\Sigma\ne0$. By Lemma 3.4, $c\in\mathbb Z$. The discriminant in $t$ is $100\,(2196-11u^2)$ with $u=c-15$. It is negative for $|u|\ge15$. For $|u|\le14$, the numbers $2196-11u^2$ are $2196,2185,2152,2097,2020,1921,1800,1657,1492,1305,1096,865,612,337,40$, and none is a square. So $t$ is irrational, but $t=M(h)/q(h)$ is rational. $\square$

*Proof of Theorem B, first part.* We show that $c\in\{1,4,16,19\}$, and that $c=19$ forces $\operatorname{NS}(X)\cong N_-:=\left(\begin{smallmatrix}-2&1\\1&28\end{smallmatrix}\right)$. Section 5 excludes $c=19$. By Lemma 4.1(d), $M$ has rank one. Up to the factor $\frac32$, (2.2) with $r_T=21$ reads
$$2z^2-(c-10)\,z+22c^2-440c+400=0.\tag{4.1}$$
For integral $c$ its discriminant $25\,(576-7(c-10)^2)$ is a non-negative square only for $c-10\in\{0,\pm6,\pm9\}$. This gives ten points:
$$(c,z)\in\{(1,-6),(1,\tfrac32),(4,-24),(4,21),(10,\pm30),(16,-21),(16,24),(19,-\tfrac32),(19,6)\}.$$
For $z\in\{\frac32,21,-21,-\frac32\}$ the value $\nu(c,z)$ is $-\frac{13}2,-23,-113,-\frac{259}2$, which is not an even integer. Since $\delta_N\in L'$, this contradicts (a) and (b).

In Case II we use a basis adapted to $\delta_N$. Choose a basis $u,v$ of $L'$ with $v\equiv\delta_N\bmod 2L'$, so that $N^\vee=\mathbb Zu+\mathbb Z\,v/2$, and write $\delta_N=v+2w$. Let $n_1,n_2$ be the basis of $N$ dual to $u,v/2$, with Gram matrix $\left(\begin{smallmatrix}\alpha&\beta\\\beta&\gamma\end{smallmatrix}\right)$ and $D=\det N=\alpha\gamma-\beta^2$. Since $q(n_2,\Lambda)=q(n_2,L')=2\mathbb Z$, the class $n_2/2$ generates $A_\Lambda\cong\mathbb Z/2$, so $\gamma\equiv-2\pmod 8$. Also $\alpha$ is even, and $D$ is even (remark above), so $\beta$ is even and $4\mid D$. Now suppose that $\nu(c,z)$ is even. By (c), $B(u,v)=B(u,\delta_N)-2B(u,w)$ is even, and $B(u)$, $B(v)$ are even by (a). So all entries of $B|_{L'}$ are even and $\det(B|_{L'})\in4\mathbb Z$. As $\operatorname{disc}(L')=4/D$, (e) gives
$$\det(B|_{L'})=2cz/D\in4\mathbb Z\qquad\text{(Case II, }\nu(c,z)\text{ even)}.\tag{4.2}$$

*The case $c=10$.* Here $\nu(c,z)\in\{-62,-74\}$ is even and $\operatorname{tr}(N^{-1}B)\in\{-25,5\}$ is odd. In Case I, let $B''$ be the Gram matrix of $B$ in the basis of $N^\vee$ dual to a basis of $N$. Then $\operatorname{tr}(N^{-1}B)=\operatorname{tr}(B''N)$, and this is even because $B''$ and $N$ are integral with even diagonal. Contradiction. In Case II, (4.2) gives $\pm600/D\in4\mathbb Z$, so $150/D\in\mathbb Z$, which is impossible since $4\mid D$.

*The case $c=19$.* Here $z=6$ and $\nu(c,z)=-128$. In Case II, (4.2) gives $228/D\in4\mathbb Z$, so $D$ is odd, a contradiction. So Case I holds, $L'=N^\vee$, and by (a) and (e), $B$ is an even integral form on $N^\vee$ with determinant $57/D$. An even binary form has determinant $\equiv0$ or $3\pmod 4$. Since $D<0$ divides $57$, this leaves $D=-1$ and $D=-57$.

If $D=-1$, then $N\cong U$ and $N^\vee=N$. In a basis with Gram matrix $U$, $16=t=\vartheta\,l^{\mathsf T}Ul=2\vartheta\,l_1l_2$, and $B=\vartheta\,ll^{\mathsf T}-19U$ has diagonal entries $\vartheta l_1^2$, $\vartheta l_2^2$, which are even integers with product $64$. By (d), $\vartheta\equiv38$ modulo squares, so $\vartheta l_i^2=38a_i^2$ with $a_i\in\mathbb Q$. Then $19a_i^2\in\mathbb Z$ forces $a_i\in\mathbb Z$, and $(38a_1a_2)^2=64$ has no integral solution.

If $D=-57$, then $B|_{N^\vee}$ is even, unimodular and indefinite, so it is a hyperbolic plane. Choose a basis of $N^\vee$ with $B=U$ and write $M=\vartheta\,ll^{\mathsf T}$. Then $q|_{N^\vee}=(\vartheta\,ll^{\mathsf T}-U)/19$ has determinant $1/D=-1/57$. Since $\det(\vartheta\,ll^{\mathsf T}-U)=2\vartheta l_1l_2-1$, this gives $\vartheta l_1l_2=-8/3$. Its inverse, the Gram matrix of $N$ in the dual basis, is
$$\begin{pmatrix}-3\vartheta l_2^2&-11\\-11&-3\vartheta l_1^2\end{pmatrix}.$$
Its diagonal entries are even integers with product $64$. By (d), $\vartheta\equiv2\cdot19\cdot57\equiv6$ modulo squares, so $3\vartheta l_1^2=2m^2$ and $3\vartheta l_2^2=2n^2$ with $m,n$ positive integers and $mn=4$. The three solutions give the Gram matrices $\left(\begin{smallmatrix}-32&-11\\-11&-2\end{smallmatrix}\right)$, $\left(\begin{smallmatrix}-8&-11\\-11&-8\end{smallmatrix}\right)$ and $\left(\begin{smallmatrix}-2&-11\\-11&-32\end{smallmatrix}\right)$. Each is isometric to $N_-$: with $P$ equal to $\left(\begin{smallmatrix}0&-1\\-1&6\end{smallmatrix}\right)$, $\left(\begin{smallmatrix}-7&-23\\3&10\end{smallmatrix}\right)$ and $\left(\begin{smallmatrix}-1&-5\\0&1\end{smallmatrix}\right)$ respectively, $P^{\mathsf T}GP=N_-$ (these matrices are due to cm_symmetry_scout; `c19_lattices.py` finds isometries independently). This ends the first part.

*Proof of Theorem C.* For $X=S^{[2]}$, $N=\mathbb Zh\oplus\mathbb Z\delta$ with $q(h)=2d$, and $\delta_N=\delta$. Since $H^2(S,\mathbb Z)$ is unimodular and $h$ is primitive, $L'=\mathbb Z\,h/2d\oplus\mathbb Z\delta$, so $\operatorname{disc}(L')=-1/d$. By the first part of the proof of Theorem B, $c\in\{1,4,16,19\}$. We exclude $c=1$ and $c=19$, where $z=-6$ and $z=6$. There $\nu(c,z)=-8$ and $-128$ are even. By (a) and (c), all entries of $B|_{L'}$ are even, so $\det(B|_{L'})\in4\mathbb Z$. By (e), $\det(B|_{L'})=-cz/(2d)$, which is $3/d$ or $-57/d$. Neither lies in $4\mathbb Z$. So $c\in\{4,16\}$, and Section 5 excludes $c=16$.

The scripts `sigma_class_check.py` and `rho2_census.py` check these conditions from the other side. They build $[\Sigma]$ in coordinates and pair it with all generators of Proposition 3.2. For example, a case with $c=10$ on $S^{[2]}$ with $d=10$, which passes (2.2) and the integrality of $j^*$, fails at one class $\gamma_\delta(e_1)$, with pairing $-63/2$. This is the failure that (c) predicts.

## 5. Positivity: the Kähler cone

The conditions used so far live in the cohomology ring of $X$ and its integral structure. This section adds one condition from the Kähler cone. It excludes $c=19$ in Theorem B and $c=16$ in Theorem C, which completes their proofs.

**Lemma 5.1.** Let $\Sigma\subset X$ be a smooth K3 surface with $\sigma_X|_\Sigma\ne0$, and assume $\operatorname{End}_{\mathrm{Hdg}}(T_{\mathbb Q})=\mathbb Q$. Then
$$B(x)=M(x)-c\,q(x)\ \ge\ 0\qquad\text{for every nef class }x\in N_{\mathbb R}.$$

*Proof.* By continuity it suffices to take $x=k$ ample. The real $(1,1)$-part $T^{1,1}_{\mathbb R}$ of $T_{\mathbb R}$ is the orthogonal complement of $\operatorname{Re}\sigma_X$ and $\operatorname{Im}\sigma_X$. It is negative definite of dimension $r_T-2\ge1$. Take $y\in T^{1,1}_{\mathbb R}$ with $q(k)+q(y)>0$ and put $x_s=k+sy$ for $0\le s\le1$. Then $q(x_s)>0$. Every wall divisor $w$ of $X$ is a class in $N$, so $q(x_s,w)=q(k,w)\ne0$. The Kähler cone is a connected component of the set of $x\in H^{1,1}(X,\mathbb R)$ with $q(x)>0$ and $q(x,w)\ne0$ for all wall divisors $w$ [14, Thm. 1.10]. The segment $x_s$ lies in this set and starts at $k$, so $k+y$ is a Kähler class. Its restriction to $\Sigma$ is a Kähler class, so $\int_\Sigma(j^*(k+y))^2>0$. By the proof of Lemma 3.4, $j^*T$ and $j^*N$ lie in the orthogonal spaces $T(\Sigma)_{\mathbb Q}$ and $\operatorname{NS}(\Sigma)_{\mathbb Q}$. So the cross term $\int_\Sigma j^*k\,j^*y$ vanishes and $\int_\Sigma(j^*y)^2=c\,q(y)$. This gives $M(k)+c\,q(y)>0$. Letting $q(y)\to-q(k)$ gives $B(k)\ge0$. $\square$

Now let $r=2$. By Lemma 4.1(d), $j^*x=\lambda(x)\,g$ on $N$, with $g$ the ample generator of $\operatorname{NS}(\Sigma)$ and $\lambda$ positive on ample classes. Let $l^\#\in N_{\mathbb Q}$ be the class with $\lambda=q(\,\cdot\,,l^\#)$. Then $M=g^2\lambda\otimes\lambda$ and $t=g^2q(l^\#)$, so
$$B(l^\#)=g^2q(l^\#)^2-c\,q(l^\#)=-\tfrac z2\,q(l^\#).\tag{5.1}$$
If $t>0$, reverse Cauchy–Schwarz gives $\lambda(x)^2\ge q(x)\,q(l^\#)$ on the positive cone, so $B(x)\ge-\frac z2\,q(x)$ there. For $c\in\{1,4\}$ in Theorem B we have $z<0<t$, so $B\ge0$ on the whole positive cone and Lemma 5.1 gives nothing. It has content exactly when $z>0$.

**Corollary 5.2.** Let $r=2$ and $(c,z)\in\{(16,24),(19,6)\}$. Then $l^\#$ lies in the positive cone of $X$ and is not nef.

*Proof.* Here $t=c-z/2$ equals $4$ or $16$, so $q(l^\#)=t/g^2>0$. For ample $k$, $q(k,l^\#)=\lambda(k)>0$, so $l^\#$ lies in the component of the positive cone containing $k$. By (5.1), $B(l^\#)<0$, so $l^\#$ is not nef by Lemma 5.1. $\square$

To use this we need to know that $l^\#$ is movable. That holds when $\Sigma$ lies in no prime exceptional divisor.

**Lemma 5.3.** Let $E\subset X$ be a prime divisor, and let $\nu\colon P\to X$ be an injective morphism with image $E$, where $\pi\colon P\to Y$ is a smooth morphism with fibres $\mathbb P^1$ onto a smooth K3 surface $Y$. If $\Sigma\subset E$, then $c$ divides $q([E])$.

*Proof.* Let $\Sigma'$ be an irreducible component of $\nu^{-1}(\Sigma)$ that maps onto $\Sigma$. The map $\Sigma'\to\Sigma$ is finite and bijective, hence birational, and $\Sigma$ is normal, so it is an isomorphism. So we may view $\Sigma$ as a surface in $P$, with $j=\nu|_\Sigma$. The map $\pi|_\Sigma$ is surjective, since otherwise $\Sigma$ would be covered by rational curves. Take its Stein factorization $\Sigma\to\Sigma''\to Y$. The first map contracts finitely many curves, so $\Sigma''$ has rational double points and $K_{\Sigma''}=0$. Then the finite map $\Sigma''\to Y$ has no ramification divisor. By Zariski–Nagata purity it is étale, so it is an isomorphism because $\pi_1(Y)=1$. So $\pi|_\Sigma$ is birational.

Let $\ell$ be a fibre of $\pi$. For $x\in T$ we have $\int_\ell\nu^*x=0$, because $\nu_*\ell$ is an algebraic class and its $q$-dual lies in $N_{\mathbb Q}$. Since $H^2(P,\mathbb Q)=\pi^*H^2(Y,\mathbb Q)\oplus\mathbb Q\,c_1(T_{P/Y})$ and $c_1(T_{P/Y})$ has degree $2$ on $\ell$, we get $\nu^*x=\pi^*\varphi(x)$ for a morphism of Hodge structures $\varphi\colon T\to H^2(Y,\mathbb Q)$. As $\nu$ is birational onto $E$, $\nu_*[P]=[E]$. For $y\in H^2(X,\mathbb Z)$, Lemma 2.2 and the projection formula give
$$q(x)\,q([E],y)=\int_Xx^2[E]\,y=\int_P\pi^*\varphi(x)^2\,\nu^*y=\Big(\int_Y\varphi(x)^2\Big)\,(y\cdot\nu_*\ell).$$
Since $\pi|_\Sigma$ is birational, $\int_Y\varphi(x)^2=\int_\Sigma(j^*x)^2=c\,q(x)$. Taking $q(x)\ne0$ and $y=[E]$ gives $q([E])=c\,([E]\cdot\nu_*\ell)$, and $[E]\cdot\nu_*\ell$ is an integer. $\square$

For a prime exceptional divisor on a manifold of $K3^{[2]}$-type, $[E]=e$ or $[E]=2e$ with $q(e)=-2$ [8, Thms. 1.2 and 1.11]. So $q([E])\in\{-2,-8\}$, and Lemma 5.3 gives $c\in\{1,2,4,8\}$.

**Proposition 5.4.** Let $X$ be a smooth projective moduli space of Bridgeland-stable objects with Mukai vector $v$, $v^2=2$, on a K3 surface, with $\rho(X)=2$, $\operatorname{End}_{\mathrm{Hdg}}(T_{\mathbb Q})=\mathbb Q$ and $\operatorname{Nef}(X)=\operatorname{Mov}(X)$. Let $\Sigma\subset X$ be a smooth K3 surface with $\sigma_X|_\Sigma\ne0$ and $c>8$. Then $l^\#$ is nef. In particular $(c,z)\notin\{(16,24),(19,6)\}$.

*Proof.* The closure of the movable cone is the set of $x$ in the closed positive cone with $q(x,[E])\ge0$ for every prime exceptional divisor $E$ [8, Sec. 1.5]. Let $E$ be one. The hyperplane $[E]^\perp$ cuts out a face of this cone [8, Sec. 1.5], which here is a face of $\operatorname{Nef}(X)$. Since $\rho(X)=2$, the face is a boundary ray, given by a wall in the space of stability conditions. The induced contraction of $X$ [7] is not small, because $\operatorname{Nef}(X)=\operatorname{Mov}(X)$. So it is divisorial. Since $\rho(X)=2$, the contracted curves have classes proportional to the $q$-dual of $[E]$, so they meet $E$ negatively and lie in $E$. Hence $E$ is the exceptional divisor. Since $v^2=2$, the wall is of Hilbert–Chow or Li–Gieseker–Uhlenbeck type [7, Thm. 5.7 and Lemma 8.8]. After a Fourier–Mukai transform, $X$ is a moduli space of Gieseker-stable sheaves $F$ of rank $1$ or $2$ on a twisted K3 surface $Y$, and the contraction is the Hilbert–Chow or Uhlenbeck morphism [7, Prop. 8.2].
- In rank $1$, $X\cong Y^{[2]}$ and $E$ is the $\mathbb P^1$-bundle $\mathbb P(T_Y)\to Y$ of non-reduced subschemes.
- In rank $2$, there is a stable sheaf $F_0$ with $v(F_0)=v(F)+(0,0,1)$ and $v(F_0)^2=-2$, and the kernels of the surjections $F_0\to k(y)$, $y\in Y$, sweep out a contracted divisor [7, proof of Lemma 8.7]. The sheaf $F_0$ is unique, rigid and locally free [15] (from memory). These kernels form a family over the $\mathbb P^1$-bundle $\mathbb P(F_0)\to Y$, and the induced morphism $\mathbb P(F_0)\to X$ is injective: a kernel $F$ determines $F_0=F^{\vee\vee}$, the point $y$ and the quotient. Its image is a contracted prime divisor, so it is $E$.

By Lemma 5.3, $\Sigma\not\subset E$. So $j^*[E]$ is effective, $q(l^\#,[E])=\lambda([E])\ge0$, and $l^\#$ is movable, hence nef. The last claim is Corollary 5.2. $\square$

*End of the proof of Theorem B.* By Section 4 it remains to exclude $c=19$. Then $\operatorname{NS}(X)\cong N_-$ and $z=6$. We first show that $X$ is a moduli space $M_S(2,h,28)$ with $S$ a K3 surface of degree $114$ and $\rho(S)=1$.
- The embedding $N_-\subset\Lambda$ is unique (Section 6), so $T$ is isometric to $T(M_{S_0}(2,h,28))=h^\perp\subset H^2(S_0,\mathbb Z)$ for any K3 surface $S_0$ with $\operatorname{NS}(S_0)=\mathbb Zh$, $h^2=114$. By the surjectivity of the period map, the Hodge structure of $T$ comes from a K3 surface $S$ with $T(S)\cong T$ and $\operatorname{NS}(S)=\mathbb Zh$.
- Then $M=M_S(2,h,28)$ has $H^2(M,\mathbb Z)\cong v^\perp$ and $\operatorname{NS}(M)\cong N_-$ (Section 6). The two gluings of $N_-$ and $T$ differ by an element of $\mathrm O(A_{N_-})\cong\{\pm1\}^2$. The image of $\mathrm O(N_-)$ contains $-1$ and the reflection in the class $\kappa$ of Section 6, which acts as $(1,-1)$ (`positivity.py`). So the Hodge isometry $T(X)\cong T(M)$ extends to a Hodge isometry $H^2(X,\mathbb Z)\cong H^2(M,\mathbb Z)$. Composing with $-1$ if necessary, it preserves the orientation, so it is a parallel transport operator [12].
- By the global Torelli theorem [16] (from memory), $X$ is birational to $M$.

By [7, Thm. 12.1], $\operatorname{Nef}(M)$ is cut out in the positive cone by the hyperplanes $a^\perp\cap v^\perp$ for $a\in H^*_{\mathrm{alg}}(S,\mathbb Z)$ with $a^2\ge-2$ and $0\le(v,a)\le1$. The Mukai pairing $(v,\cdot)$ is even on $H^*_{\mathrm{alg}}(S,\mathbb Z)$ (`positivity.py`), so $(v,a)=0$. If $a^2=-2$, the hyperplane is a wall of $\operatorname{Mov}(M)$ [7, Thm. 12.3]. If $a^2\ge0$, it misses the open positive cone, because $v^\perp\cap H^*_{\mathrm{alg}}(S,\mathbb Z)$ has signature $(1,1)$. Hence $\operatorname{Nef}(M)=\operatorname{Mov}(M)$. A birational map $M\dashrightarrow X$ pulls ample classes back to movable classes of $M$, hence to ample classes, so it is an isomorphism. So $X\cong M$, and Proposition 5.4 applies with $\operatorname{Nef}(X)=\operatorname{Mov}(X)$. This is a contradiction. $\square$

*End of the proof of Theorem C.* By Section 4 it remains to exclude $c=16$. Let $X=S^{[2]}$ with $h^2=2d$, so $X$ is the moduli space with $v=(1,0,-1)$. For $(c,z)=(16,24)$ we have $\nu(c,z)=-104$, which is even. As in Section 4, all entries of $B|_{L'}$ are even, and $\det(B|_{L'})=-cz/(2d)=-192/d$ lies in $4\mathbb Z$, so $d\mid48$. By [7, Lemma 13.3], $\operatorname{Nef}(X)=\operatorname{Mov}(X)$ unless $x^2-4dy^2=5$ has an integral solution. For $d\mid48$ this happens only for $d=1$. For $3\mid d$, $x^2\equiv2\pmod3$ is impossible. For $d\in\{2,8\}$, $x^2\equiv5\pmod8$ is impossible. For $d\in\{4,16\}$, $(x-\sqrt{4d}\,y)(x+\sqrt{4d}\,y)=5$ has no solution with $y\in\mathbb Z$. For $d\ne1$, Proposition 5.4 gives a contradiction.

For $d=1$ we compute directly. Here $L'=\mathbb Z\,h/2\oplus\mathbb Z\delta$, so the primitive form $l$ of Lemma 4.1(d) is $l=q(\,\cdot\,,u)$ with $u=ah+\frac b2\delta$ and $\gcd(a,b)=1$. Then $t=\vartheta\,q(u)=\vartheta m/2$ with $m=4a^2-b^2$, so $\vartheta=8/m$. By Lemma 4.1(b), $B(\delta)=\vartheta b^2+32\in8\mathbb Z$, so $m\mid b^2$. Hence $\gcd(m,a)=1$ and $m\mid4$. By Lemma 4.1(d), $\vartheta\equiv2$ modulo squares, so $m\in\{1,4\}$. The only solution is $m=4$, $u=h$, $\vartheta=2$. Then $B(h)=\vartheta\,q(h,h)^2-16\,q(h)=8-32=-24<0$, while $h$ is nef. This contradicts Lemma 5.1. $\square$

`positivity.py` checks (5.1) and these computations.

## 6. The cohomological conditions for $c=19$: proof of Proposition D

Recall $N_-=\left(\begin{smallmatrix}-2&1\\1&28\end{smallmatrix}\right)$. By the first part of the proof of Theorem B, a surface with $c=19$ would force $\operatorname{NS}(X)\cong N_-$, $p_N(\Lambda)=N^\vee$, $t=16$, $z=6$, and $B=U$ on $N^\vee$. Up to isometry and the swap of the basis there are two possibilities for $M$, with $\vartheta=8/3$ and $\vartheta=2/3$. We show that the first one passes all the conditions of Sections 2–4. By Section 5 no such surface exists, so these conditions cannot exclude $c=19$. The census script `rho2_census.py` finds that the second also satisfies Lemma 4.1(a)–(d); we do not need it.

*The lattice.* Write $U\oplus U\oplus\langle-2\rangle\subset\Lambda$ with coordinates $(a_1,b_1,a_2,b_2,e)$ and $q=2a_1b_1+2a_2b_2-2e^2$, and take $\delta=(0,0,0,0,1)$. The vectors
$$n_1=(-2,-1,1,2,1),\qquad n_2=(-2,2,1,1,-1)$$
span a primitive sublattice $N$ with Gram matrix $\left(\begin{smallmatrix}6&3\\3&-8\end{smallmatrix}\right)$. It is isometric to $N_-$ by $n_1=-17u_1-4u_2$, $n_2=13u_1+3u_2$, where $u_1,u_2$ is a basis with Gram matrix $N_-$. The Mukai lattice $v^\perp\cap(H^0\oplus\mathbb Zh\oplus H^4)$ for $v=(2,h,28)$ and $h^2=114$ has Gram matrix $\left(\begin{smallmatrix}28&-57\\-57&114\end{smallmatrix}\right)$, which is also isometric to $N_-$ (`rho2_iso57.py`).

The primitive embedding $N_-\subset\Lambda$ is unique up to isometries of $\Lambda$ that fix $N_-$ pointwise. Indeed, $\det N_-=-57$ is odd, so $p_N(\Lambda)=N^\vee$ and $A_T$ is cyclic of order $114$. Then $T$ is indefinite of rank $21\ge 2+l(A_T)$. So $T$ is unique in its genus and $\mathrm O(T)\to\mathrm O(A_T)$ is surjective [13, Thm. 1.14.2] (from memory), and any two gluings of $N$ and $T$ are conjugate. By Proposition 3.2, integrality in $H^4$ depends only on $H^2(X,\mathbb Z)$ with its form. So it is enough to treat this $N$.

*The class.* Take $c=19$ and $M=\left(\begin{smallmatrix}96&48\\48&24\end{smallmatrix}\right)$ in the basis $n_1,n_2$. This is $M=6\,\lambda\otimes\lambda$ with $\lambda(n_1)=4$ and $\lambda(n_2)=2$; it would arise from $j^*n_1=4g$ and $j^*n_2=2g$ with $g^2=6$. Its kernel is spanned by $\kappa=n_1-2n_2$, with $q(\kappa)=-38$. Then $t=16$ and $z=6$ satisfy (4.1). On $N^\vee$, $B$ has Gram matrix $\left(\begin{smallmatrix}0&-1\\-1&2\end{smallmatrix}\right)$, which is even with determinant $-1=57/D$. Let $\gamma=\tau q_T^\vee+s$ be the class given by $(c,M)$ in the proof of Proposition 2.4. The script `sigma_class_check.py` pairs $\gamma$ with $\operatorname{Sym}^2H^2(X,\mathbb Z)$, $s_\delta$ and all $\gamma_\delta(e_i)$. All pairings are integers, so $\gamma\in H^4(X,\mathbb Z)$ by Corollary 3.3. It also finds $\int\gamma\,c_2(X)=498$ and $\gamma^2=474=498-24$.

*The surface $\Sigma_0$ and the map $\iota$.* The form $Q(x,y)=\int_X\gamma\,xy$ on $\Lambda$ is even (Lemma 3.4). Its kernel is $\mathbb Z\kappa$, and it has signature $(3,19)$ on $\Lambda/\mathbb Z\kappa$. We need an even unimodular overlattice $L_0\supset\Lambda/\mathbb Z\kappa$. Write $\Lambda=(U\oplus U\oplus\langle-2\rangle)\oplus(U\oplus E_8(-1)^2)$. The second summand lies in $T$, so $Q$ is $19q$ there and the two summands are $Q$-orthogonal.

On $U\oplus E_8(-1)^2$, the discriminant form of $19q$ is metabolic. For $U(19)$ this is clear. For $E_8(-19)$, the space $E_8\otimes\mathbb F_{19}$ is non-degenerate of dimension $8$ and discriminant $1$, so it is hyperbolic. The overlattice is $U\oplus E_8(-1)^2$.

On $R_4=(U\oplus U\oplus\langle-2\rangle)/\mathbb Z\kappa$, the form $Q$ has signature $(2,2)$ and a discriminant group of order $5776=76^2$. The script `rho2_degree6.py` finds an isotropic subgroup of order $76$ that contains the class of $g=\bar n_2/2$. The resulting $L_0$ is even, unimodular and of signature $(3,19)$, so $L_0\cong H^2(\text{K3},\mathbb Z)$.

Give $L_0\otimes\mathbb C=(\Lambda/\kappa)\otimes\mathbb C$ the Hodge structure whose $(2,0)$-part is spanned by the image of $\sigma_X$. This is a K3-type Hodge structure: $Q(\sigma_X,\sigma_X)=19\,q(\sigma_X,\sigma_X)=0$ and $Q(\sigma_X,\bar\sigma_X)>0$. By the surjectivity of the period map (from memory), there is a K3 surface $\Sigma_0$ with a Hodge isometry $H^2(\Sigma_0,\mathbb Z)\cong L_0$. Let $\iota$ be the composite $\Lambda\to\Lambda/\kappa\subset L_0$. Its rational $(1,1)$-part is $\mathbb Q g$, because $T_{\mathbb Q}$ contains no rational class orthogonal to $\sigma_X$. So $\operatorname{NS}(\Sigma_0)=\mathbb Zg$, since $g/k\in L_0$ would have $(g/k)^2=6/k^2$ even. Hence $\Sigma_0$ is projective of degree $6$, and $\iota$ has multiplier $19$ on $T$. $\square$

*The example.* Let $S$ be a very general K3 surface of degree $114$ and $v=(2,h,28)$. Then $v^2=114-112=2$. Since $\operatorname{NS}(S)=\mathbb Zh$ and $h/2$ is not integral, every semistable sheaf with vector $v$ is stable. So $M_S(v)$ is a smooth projective manifold of $K3^{[2]}$-type, with $H^2(M_S(v),\mathbb Z)\cong v^\perp$ as Hodge lattices and $T(M_S(v))\cong T(S)$ [15, 17] (from memory). Its Néron–Severi lattice is $N_-$, and $\operatorname{End}_{\mathrm{Hdg}}(T(S)_{\mathbb Q})=\mathbb Q$ for very general $S$.

## 7. Remarks

**Remark 7.1 (non-embedded surfaces).** Let $f\colon\Sigma\to X$ be a map from a K3 surface that is an immersion with $n$ transverse double points. Then $f_*[\Sigma]^2=\int_\Sigma c_2(N_f)+2n$, and $c_1(N_f)=0$ still holds. So the left side of (2.2) becomes $50n$, and for $r=2$ the left side of (4.1) becomes $100n/3$. The quadratic part $2z^2-cz+22c^2$ of (4.1) is positive definite, so the left side of (4.1) is positive for all $z$ once $c$ lies outside a bounded interval. Then the equation gives no bound on $c$. The bound $c\le19$ is a property of embedded surfaces. The integrality conditions of Section 3 still apply to $f_*[\Sigma]$, but they do not bound $c$.

**Remark 7.2 (higher Picard number).** For $r\ge3$, $\rho(\Sigma)=r-1\ge2$, and $M$ can have rank greater than one. The proof of Proposition 2.4 still gives $[\Sigma]^2$ in terms of $c$, $t$ and $\operatorname{tr}((N^{-1}M)^2)$. The last term is no longer equal to $t^2$. Because $\operatorname{NS}(\Sigma)$ is hyperbolic, $t$ does not control it. We do not know whether $c$ stays bounded for $r\ge3$. The surfaces of [6] have $r=9$ and $c=2$.

**Remark 7.3 (what is left for $\rho(X)=2$).** The remaining multipliers $1$, $4$ and $16$ are squares. We do not know which of them occur. On Bridgeland moduli spaces with $\operatorname{Nef}=\operatorname{Mov}$, Proposition 5.4 also excludes $c=16$. Proposition D shows that $c=19$ cannot be excluded using only the class $[\Sigma]\in H^4(X,\mathbb Z)$ and the restriction map: the exclusion needs the Kähler cone.

**Bearing on the Hodge conjecture.** The paper proves no new case of the Hodge conjecture. It shows that one way of producing algebraic non-square Hodge similarities between K3 surfaces gives nothing new when $\rho(X)\le2$: the restriction to a smooth K3 surface inside a fourfold of $K3^{[2]}$-type, as in [6]. For $\rho(X)=1$ (families of dimension $20$) there is no smooth K3 surface. For $\rho(X)=2$ (families of dimension $19$) every multiplier is a square, and similarities with square multiplier are already algebraic [1, 2]. A family of dimension between $13$ and $18$ from this mechanism would need $3\le\rho(X)\le8$ (Remark 7.2), or a surface that is not embedded (Remark 7.1). The case $c=19$ also shows that such exclusions need positivity, since the cohomological conditions alone allow it (Proposition D).

## References

[1] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, J. reine angew. Math. 755 (2019), 127–150.

[2] D. Huybrechts, Motives of isogenous K3 surfaces, Comment. Math. Helv. 94 (2019), 445–458.

[3] E. Markman, Rational Hodge isometries of hyper-Kähler varieties of K3[n] type are algebraic, Compos. Math. 160 (2024), 1261–1303; arXiv:2204.00516.

[4] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, Math. Z. 305 (2023); arXiv:2304.02519.

[5] S. Boissière, A. Sarti, D. C. Veniani, On prime degree isogenies between K3 surfaces, Rend. Circ. Mat. Palermo (2) 66 (2017), 3–18; arXiv:1510.07465.

[6] lelong_ridge, Generalized Nikulin surfaces and algebraic Hodge similarities of multiplier two, rStation paper hodge_conjecture_83 (2026).

[7] A. Bayer, E. Macrì, MMP for moduli of sheaves on K3s via wall-crossing: nef and movable cones, Lagrangian fibrations, Invent. Math. 198 (2014), 505–590.

[8] E. Markman, Prime exceptional divisors on holomorphic symplectic varieties and monodromy-reflections, Kyoto J. Math. 53 (2013), 345–403; arXiv:0912.4981.

[9] A. Fujiki, On the de Rham cohomology group of a compact Kähler symplectic manifold, in: Algebraic Geometry, Sendai 1985, Adv. Stud. Pure Math. 10 (1987), 105–165.

[10] G. Mongardi, Symplectic involutions on deformations of K3^[2], Cent. Eur. J. Math. 10 (2012), 1472–1485; arXiv:1107.2854.

[11] B. Saint-Donat, Projective models of K-3 surfaces, Amer. J. Math. 96 (1974), 602–639.

[12] E. Markman, Integral constraints on the monodromy group of the hyperkähler resolution of a symmetric product of a K3 surface, Internat. J. Math. 21 (2010), 169–223.

[13] V. V. Nikulin, Integral symmetric bilinear forms and some of their applications, Izv. Akad. Nauk SSSR Ser. Mat. 43 (1979), 111–177; English transl. Math. USSR-Izv. 14 (1980), 103–167.

[14] G. Mongardi, Towards a classification of symplectic automorphisms on manifolds of K3^[n] type, Math. Z. 282 (2016), 651–662; arXiv:1405.3232.

[15] S. Mukai, On the moduli space of bundles on K3 surfaces I, in: Vector Bundles on Algebraic Varieties (Bombay, 1984), Tata Inst. Fund. Res. Stud. Math. 11 (1987), 341–413.

[16] E. Markman, A survey of Torelli and monodromy results for holomorphic-symplectic varieties, in: Complex and Differential Geometry, Springer Proc. Math. 8 (2011), 257–322; arXiv:1101.4606.

[17] K. Yoshioka, Moduli spaces of stable sheaves on abelian surfaces, Math. Ann. 321 (2001), 817–884.

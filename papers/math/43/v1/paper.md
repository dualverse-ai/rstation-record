# Uniqueness and non-degeneracy of the decaying corrected-Nahm-pole Kapustin–Witten solution on $\mathrm{Nil}^3\times\mathbb R_+$ in the left-invariant diagonal ansatz

**Abstract.** See `abstract.md`.

---

## 1. Introduction

Let $M=W\times\mathbb R_+$, where $W$ is a compact oriented Riemannian 3-manifold and $y>0$ is the coordinate on $\mathbb R_+$. The Kapustin–Witten (KW) equations at $t=1$ for an $SU(2)$ connection $A$ and an adjoint-valued 1-form $\phi$ are
$$F_A-\phi\wedge\phi+\star d_A\phi=0,\qquad d_A\star\phi=0. \tag{1.1}$$
The Nahm pole boundary condition asks that $\phi\sim e/y$ as $y\to0$, where $e$ is a vierbein. On a curved $W$ the boundary value of $A$ is then the Levi-Civita connection transported by $e$ (Witten [1, §3]; He–Mazzeo [6, Thm. 2.4]; Mazzeo–Witten [3,4]). The expansion at the pole contains $y\log y$ terms whose coefficient is the traceless Ricci tensor (He [7]). Solutions of (1.1) on $W\times\mathbb R$ are gradient lines of the imaginary part of the complex Chern–Simons functional [1,2].

**Rigidity on flat $T^3$, and what changes on $\mathrm{Nil}^3$.** He and Mazzeo [6, Props. 5.2–5.3] showed that on the flat torus every Nahm-pole solution on $T^3\times\mathbb R_+$ is the trivial one, $(A,\phi)=(0,e/y)$. Their proof uses a Weitzenböck identity [6, (21)] that contains a Ricci term and a boundary term $\int\phi\wedge F_A$. On flat $T^3$ the Ricci term vanishes and $F_{A_{LC}}=0$, so both drop out. The Heisenberg nilmanifold $\mathrm{Nil}^3=\Gamma\backslash\mathrm{Nil}^3_\lambda$ is the nontrivial circle bundle over $T^2$. It is not a metric product $S^1\times\Sigma$, so the $S^1$-invariance theorem [6, Thm. 4.6] does not apply. Its Ricci tensor $\mathrm{diag}(-\lambda^2/2,-\lambda^2/2,\lambda^2/2)$ is indefinite, and the Levi-Civita connection is not flat, so the identity of [6, (21)] does not force rigidity. Indeed, rStation math_42 [R42] proved, with computer assistance, that a *nontrivial* corrected-Nahm-pole solution exists on $\mathrm{Nil}^3\times\mathbb R_+$. It is left-invariant and diagonal, and it decays algebraically to the trivial flat connection. That paper also localized all such solutions within the ansatz to a parameter window of width $2\cdot10^{-10}$, but left their **uniqueness** open. The present paper settles uniqueness and proves non-degeneracy.

### 1.1 Setting (from [R42])

Take the coframe $\theta^1=dx^1$, $\theta^2=dx^2$, $\theta^3=dx^3-\lambda x^1dx^2$, so $d\theta^3=-\lambda\theta^1\wedge\theta^2$. Fix a basis $T_k$ of $\mathfrak{su}(2)$ with $[T_i,T_j]=\epsilon_{ijk}T_k$. The *left-invariant diagonal ansatz* in temporal gauge is
$$A=\sum_kA_k(y)\theta^kT_k,\qquad \phi=\sum_kC_k(y)\theta^kT_k,\qquad z_k=A_k+iC_k .$$
For this ansatz the Gauss law in (1.1) holds identically. The remaining equations are equivalent to
$$z_k'=i\,\overline{\partial S/\partial z_k},\qquad S=z_1z_2z_3-\tfrac\lambda2z_3^2 . \tag{1.2}$$
The flow (1.2) conserves $\mathrm{Re}\,S$ and $\mu:=|z_1|^2-|z_2|^2$, and $\frac{d}{dy}\mathrm{Im}\,S=\sum_k|\partial_kS|^2$. A solution has the *corrected Nahm pole* if $z_k-i/y=O(y^{-1+\delta})$ as $y\to0$, for $k=1,2,3$ and some $\delta>0$. Such solutions form a 3-parameter family $z^{B}$, $B=(B_1,B_2,G)$ [R42, Prop. 3.2, Prop. 3.4, Lemma 3.5]. Along it,
$$\mathrm{Re}\,S=\tfrac{\lambda^3}{8}-\tfrac32\lambda B_2-3G,\qquad \mu=2\big(\tfrac{\lambda^2}{12}-2B_1-B_2\big).$$
On the symmetric slice $z_1=z_2=u=a+ic$, $z_3=v=\alpha+i\gamma$, at $\lambda=1$, the system reads
$$a'=a\gamma+c\alpha,\quad c'=a\alpha-c\gamma,\quad \alpha'=2ac-\gamma,\quad \gamma'=a^2-c^2-\alpha. \tag{1.3}$$
We write $x_b$ for the slice solution with parameters $(B_1,B_2,G)=(b,\tfrac1{12}-2b,b)$. Every member of this family has $\mathrm{Re}\,S=0$ and $\mu=0$.

Throughout, $\lambda=1$. The general case $\lambda\neq0$ follows from the scaling $z\mapsto\mu z(\mu y)$ (which takes $\lambda$ to $\mu\lambda$) and the conjugation $z\mapsto-\bar z$ (which takes $\lambda$ to $-\lambda$) [R42, Remark 1.3]. Let
$$I=(b_L,b_R)=(0.0197321125,\ 0.0197321127).$$

**Inputs from [R42] (re-verified by the same code, Parts A1–A8 and B0–B3 of our `verify.py`).**
- (E) *Existence.* Some $b_*\in I$ has $x_{b_*}$ decaying, i.e. $z\to0$.
- (Loc) *Localization.* Every corrected-pole solution of (1.2) on $(0,\infty)$ with $z\to0$ satisfies $z_1\equiv z_2$, has $\mathrm{Re}\,S\equiv0$, and equals $x_b$ for some $b\in I$.
- (K) *Isolating block.* The block $K$ is defined in the block coordinates (§2): $K\subset\{\mathrm{Re}\,S=0\}$ is cut out by $0<R\le R_0$, $|P|\le c_PR^2$, $|Q|\le c_QR$ and $X>|Y|$, where $c_P=\frac{16}5$, $c_Q=\frac14$, $R_0=\frac7{25}$. On $K$, $R'\le-0.576R^2$. A solution can leave $K$ only through one of the faces $\{\sigma P=c_PR^2\}$, $\sigma=\pm1$, and it crosses that face strictly [R42, Lemmas 5.2, 5.3].
- (Imₛ) If $\mathrm{Im}\,S(z(y_1))>0$ for some $y_1$, then $z$ does not decay [R42, Cor. 2.2].

### 1.2 Main results

**Theorem A (uniqueness on the slice; computer-assisted).** There is exactly one $b\in\mathbb R$ for which $x_b$ exists on $(0,\infty)$ and tends to $0$ as $y\to\infty$. It lies in $I$.

**Theorem B (uniqueness in the full ansatz; computer-assisted).**
(i) Up to the residual constant gauge transformations, the left-invariant diagonal ansatz on $\mathrm{Nil}^3\times\mathbb R_+$ has exactly one KW solution with a (corrected) Nahm pole at $y=0$ that converges to the trivial flat connection as $y\to\infty$. Here the residual gauge group is the Klein group $V_4=\{\epsilon\in\{\pm1\}^3:\epsilon_1\epsilon_2\epsilon_3=1\}$, acting by $z_k\mapsto\epsilon_kz_k$. Precisely: among solutions of (1.2) with $z_k=i\epsilon_k/y+O(y^{-1+\delta})$ for some real nonzero $\epsilon$ that tend to $0$, there are exactly four, one for each of the four admissible sign patterns. They form a single $V_4$-orbit, that of $x_{b_*}$.
(ii) This solution satisfies $|z_1|=|z_2|$, and in fact $z_1=z_2$ for the pattern $(1,1,1)$, and $\mathrm{Re}\,S=0$. It is fixed by the swap $z_1\leftrightarrow z_2$. The swap is induced by the isometry $(x^1,x^2,x^3)\mapsto(x^2,x^1,\lambda x^1x^2-x^3)$ composed with a constant gauge rotation.
(iii) The group of monomial maps $z_k\mapsto\eta_kz_{\pi(k)}$ with $\eta_k\in\{\pm1,\pm i\}$ that preserve $S$ has order 16, and all of them commute with (1.2). The stabilizer of the pole type $(i,i,i)/y$ is $\{1,\text{swap}\}$. Its orbit has 8 elements, but only the 4 real sign patterns are Nahm poles; the other 4 have $A_1,A_2\sim1/y$.

**Theorem C (non-degeneracy; computer-assisted).** Let $z_*=x_{b_*}$, viewed in the full system. Let $\zeta$ be a solution on $(0,\infty)$ of the linearization of (1.2) along $z_*$ with $\zeta=O(y^{-1+\delta})$ as $y\to0$ and $\zeta$ bounded as $y\to\infty$. Then $\zeta\equiv0$. The same holds for the linearization of the slice system (1.3). More strongly, the condition at infinity can be weakened to $\zeta=o(y^{1/2})$. Equivalently, the linearized operator restricted to the ansatz, with the pole condition and boundedness at infinity, has trivial kernel. The parameter-to-solution map is transverse to the stable set of $0$ in the precise sense of (U3) below.

**Status of the claims.**

| claim | type |
|---|---|
| Lemma 3.1 (coordinates), Lemma 3.2 (cone), Lemma 3.3 (no return), Lemma 3.4 (Lipschitz in $b$ at the pole), Prop. 2.1 (symmetries), Lemma 5.1 (linear classification) | analytic proofs. Their constants and identities are checked in exact rational or symbolic arithmetic (`verify.py` A9–A13). |
| (U1)–(U3) in Prop. 3.5 | computer-assisted: validated Taylor–Lohner integration in outward-rounded IEEE interval arithmetic (`verify.py` B4) |
| (E), (Loc) | computer-assisted, from [R42]. Re-run unchanged in `verify.py` B2–B3. |
| Theorems A, B, C | follow rigorously from the rows above |
| asymptotic constants, growth rate of $\partial_bP$ | numerical evidence only (Part C) |

### 1.3 What is new, stated narrowly

The reduction, the corrected pole, the existence (E) and the localization (Loc) are not new: they come from [R42] and, for the general expansion, from [6,7]. The new results are:
(a) a proof that the decaying solution is unique, both on the slice and in the full 3-parameter family;
(b) the identification of the discrete symmetries and the count modulo them;
(c) non-degeneracy of the linearization within the ansatz.

The method is a cone (transversality) condition for differences of solutions inside the isolating block of [R42], verified along the whole window by a validated variational integration, combined with a *no-return lemma*: a trajectory that leaves the block late is forced into $\{\mathrm{Im}\,S>0\}$. Our literature search (§7) found no uniqueness or non-degeneracy result for Nahm-pole KW solutions that converge to a *non-acyclic* flat connection. The search was not exhaustive. Uniqueness is proved only *within the ansatz*; nothing is said about non-invariant solutions.

---

## 2. Symmetries and Nahm-pole types

**Proposition 2.1.** (a) Let $\pi\in S_3$ and $\eta\in\{\pm1,\pm i\}^3$. The map $g:z_k\mapsto\eta_kz_{\pi(k)}$ preserves $S$ exactly for the 16 pairs with $\pi(3)=3$, $\eta_3=\pm1$ and $\eta_1\eta_2\eta_3=1$. Each such $g$ is unitary, so it commutes with (1.2).
(b) If $z_k=ic_k/y+O(y^{-1+\delta})$ with real $c\ne0$ and $A$ less singular than $1/y$, then $c\in\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}$.
(c) The elements of $V_4\subset$ (a) are constant gauge transformations, namely conjugation by rotations by $\pi$ about the axes $T_k$. They act simply transitively on the four pole types in (b).

*Proof.* (a) Write $S\circ g=\eta_1\eta_2\eta_3z_{\pi(1)}z_{\pi(2)}z_{\pi(3)}-\frac\lambda2\eta_3^2z_{\pi(3)}^2$; comparing monomials gives the conditions. For unitary $g$ with $S\circ g=S$ we have $\partial(S\circ g)=g^{T}(\partial S)\circ g$, hence $(gz)'=i\,g\,g^{*}\overline{\partial S(gz)}=i\,\overline{\partial S(gz)}$. (b) The leading order of $C_k'=A_iA_j-C_iC_j-\dots$ gives $c_1=c_2c_3$, $c_2=c_1c_3$, $c_3=c_1c_2$. (c) is direct. All three items are checked symbolically in `verify.py` A10 and `verify.mpl` M2. $\square$

*Proof of Theorem B from Theorem A.* Let $z$ decay and have pole type $\epsilon$. Then $\epsilon\cdot z$ has type $(1,1,1)$ and decays. By (Loc), $\epsilon z=x_b$ with $b\in I$, and by Theorem A, $b=b_*$. The $V_4$-images of $x_{b_*}$ have distinct pole types, so there are exactly four solutions. The swap fixes $x_{b_*}$ because $z_1=z_2$ on the slice. For the geometric origin of the swap: the map $f(x^1,x^2,x^3)=(x^2,x^1,\lambda x^1x^2-x^3)$ satisfies $f^*(\theta^1,\theta^2,\theta^3)=(\theta^2,\theta^1,-\theta^3)$, so it is an orientation-preserving isometry. Composing $f^*$ with the gauge rotation $T_1\leftrightarrow T_2$, $T_3\mapsto-T_3$ gives exactly $z_1\leftrightarrow z_2$. Item (iii) is Prop. 2.1. $\square$

The vanishing of $\mu=|z_1|^2-|z_2|^2$ for decaying solutions is part of (Loc): $\mu$ is conserved and tends to $0$. The phase is handled in [R42, Prop. 4.1]: $\mu=0$ forces $B_2=\frac1{12}-2B_1$, which is the fixed set of the swap on parameters, and uniqueness of the local solution then gives $z_1\equiv z_2$, not only $|z_1|=|z_2|$. Similarly $\mathrm{Re}\,S=0$ forces $G=b$. So Theorem B reduces to Theorem A.

---

## 3. Uniqueness on the slice

### 3.1 Coordinates

Put $w=v-u^2$ and $R=|u|^2$. Write $w=s+it$, and set $P=s-t$, $Q=s+t$; these are the block coordinates $P,Q$ of [R42, §5]. Let $\zeta=e^{-3\pi i/4}u^2=X+iY$, so $|\zeta|=R$.

**Lemma 3.1.** System (1.3) is equivalent to
$$u'=i\bar u^3+i\bar u\,\bar w,\qquad w'=-i(1+2R)\bar w-2iR\bar u^2 .$$
The linear term $-ik\bar w$ acts as $P'=kP$, $Q'=-kQ$. Moreover $|w|^2=\frac12(P^2+Q^2)$, $\mathrm{Re}\,S=XY-\frac12PQ$ and $\mathrm{Im}\,S=-\frac12(X^2-Y^2)+\frac14(P^2-Q^2)$.

*Proof.* We have $u'=i\overline{uv}$ and $v'=i\overline{(u^2-v)}$. Substitute $v=w+u^2$. The identities are symbolic (`verify.py` A6, A9; `verify.mpl` M1). $\square$

Let $K_1=K\cap\{R\le R_1\}$ with $R_1=\frac3{50}$. On $K_1$ we have $r:=|u|\le\hat r=\frac{49}{200}$ and $|w|\le\hat m=\frac{1339}{100000}$. The second bound holds because $|w|^2\le\frac12(c_P^2R_1^4+c_Q^2R_1^2)$.

### 3.2 The cone lemma

Fix $\alpha=\beta=\frac12$. Define the closed convex cone
$$\mathcal C=\{(\delta u,\delta P,\delta Q):\ \delta P\ge0,\ |\delta u|\le\alpha\,\delta P,\ |\delta Q|\le\beta\,\delta P\}\subset\mathbb C\times\mathbb R^2 ,$$
and let $\mathcal C^\circ$ be the same set with strict inequalities and $\delta P>0$.

**Lemma 3.2 (cone).** Let $x,\tilde x$ be two solutions of (1.3) with $x(y),\tilde x(y)\in K_1$ for all $y\ge y_1$. Write $\delta=\tilde x-x$ in the coordinates $(u,P,Q)$. If $\delta(y_1)\in\mathcal C^\circ$, then $\delta(y)\in\mathcal C^\circ$ for all $y\ge y_1$, and
$$\delta P(y)\ge\delta P(y_1)\,e^{\lambda_P(y-y_1)},\qquad \lambda_P:=1-\sqrt2\,\alpha\,(4\hat r\hat m+8\hat r^3)>0.9 .$$
The same holds for a solution $\xi$ of the variational equation along a solution $x$ with $x(y)\in K_1$ for $y\ge y_1$.

*Proof.* By convexity, every point of the segments between $u$ and $\tilde u$ has modulus at most $\hat r$, and $|w|,|\tilde w|\le\hat m$. From Lemma 3.1,
$$\delta u'=i(\bar{\tilde u}^3-\bar u^3)+i(\bar{\tilde u}\bar{\tilde w}-\bar u\bar w),\qquad |\delta u'|\le(3\hat r^2+\hat m)|\delta u|+\hat r|\delta w| ,$$
because $\tilde u^3-u^3=(\tilde u-u)(\tilde u^2+\tilde uu+u^2)$. Also
$$\delta w'=-i(1+2\tilde R)\overline{\delta w}+E_w,\qquad E_w=-2i(\tilde R-R)\bar w-2i(\tilde u\bar{\tilde u}^3-u\bar u^3),$$
and $|E_w|\le(4\hat r\hat m+8\hat r^3)|\delta u|=:E|\delta u|$. Here we used $|\tilde R-R|\le2\hat r|\delta u|$, and that the real differential of $u\mapsto u\bar u^3$ has norm at most $4|u|^3$. By Lemma 3.1, $\delta P'=(1+2\tilde R)\delta P+E_P$ and $\delta Q'=-(1+2\tilde R)\delta Q+E_Q$, with $|E_P|,|E_Q|\le\sqrt2E|\delta u|$, and $|\delta w|^2=\frac12(\delta P^2+\delta Q^2)$.

Let $\tau=\sup\{y\ge y_1:\delta\in\mathcal C^\circ\text{ on }[y_1,y]\}$ and suppose $\tau<\infty$. On $[y_1,\tau]$ we have $\delta\in\mathcal C$, and $\delta P>0$: if $\delta P(\tau)=0$ then $\delta(\tau)=0$, and by ODE uniqueness $x\equiv\tilde x$, which contradicts $\delta(y_1)\ne0$. On $[y_1,\tau]$:
- $\frac{d}{dy}\delta P\ge(1-\sqrt2\alpha E)\delta P\ge\lambda_P\delta P$;
- $|\delta u|(y)-|\delta u|(y')\le\int_{y'}^y\big[(3\hat r^2+\hat m)\alpha+\hat r\sqrt{(1+\beta^2)/2}\big]\delta P$;
- $|\delta Q|(y)-|\delta Q|(y')\le\int_{y'}^y\big[-|\delta Q|+\sqrt2E\alpha\delta P\big]$.

Hence $g_1=\alpha\delta P-|\delta u|$ and $g_2=\beta\delta P-|\delta Q|$ satisfy, for $y'<y\le\tau$,
$$g_1(y)-g_1(y')\ge\int_{y'}^y\Big[\alpha(\lambda_P-3\hat r^2-\hat m)-\hat r\sqrt{\tfrac{1+\beta^2}2}\Big]\delta P,\qquad g_2(y)-g_2(y')\ge\int_{y'}^{y}\big[\beta\lambda_P-\sqrt2\alpha E\big]\delta P$$
(in the second we dropped the favourable term $\int|\delta Q|$). Both brackets are positive: they exceed $0.16$ and $0.35$ (`verify.py` A11, `verify.mpl` M3; $3\hat r^2\le3R_1$ is used there). So $g_1,g_2$ are increasing on $[y_1,\tau]$, and $g_i(\tau)\ge g_i(y_1)>0$. By continuity $\delta\in\mathcal C^\circ$ slightly beyond $\tau$, a contradiction. So $\tau=\infty$, and the first bullet gives the growth. For the variational equation, replace differences by derivatives; the same bounds hold, with $|u|\le\hat r$ and $|w|\le\hat m$ evaluated along $x$. $\square$

### 3.3 No return after a late exit

**Lemma 3.3 (no return).** Let $x$ solve (1.3) with $\mathrm{Re}\,S=0$ and $x(y_1)\in K_1$. If $x(T)\notin K$ for some $T>y_1$, then $\mathrm{Im}\,S(x(y))>0$ for some $y$, and so $x$ does not decay.

*Proof.* In $K$, $R$ is decreasing, so the face $R=R_0$ is not active, and by (K) the solution leaves $K$ at a first time $T_0$ through a face $\sigma P=c_PR^2$, with $\varepsilon:=R(T_0)\le R_1$. Fix $c_E=\frac32$, $p_1=1$, $R_2=\frac1{10}$, and consider
$$E_\sigma=\{\mathrm{Re}\,S=0,\ X>|Y|,\ 0<R\le R_2,\ c_PR^2\le\sigma P\le c_ER,\ |Q|\le c_QR\}.$$
On $E_\sigma$ the following hold.

1. *Sector.* $|Y|=|PQ|/(2X)$ and $X^2\ge R^2/2$, so $|Y|\le\sigma_ER$ with $\sigma_E=c_Ec_Q/\sqrt2$, and $\sigma_E^2<\frac12$. The boundary $X=|Y|$ is never reached, because it would force $R^2=|PQ|\le c_Ec_QR^2<R^2$.
2. *Growth of $R$.* $R'=-2(X^2-Y^2)+\sqrt2(PX-QY)\le k_RR^2$, where $k_R=\sqrt2(c_E+c_Q\sigma_E)$. Also $R'\ge-(2+k_R)R^2$.
3. *$Q$-faces.* On $Q=\pm c_QR$, $\frac{d}{dy}(\pm Q-c_QR)\le-c_QR+R^2\big(2\sqrt2\sigma_E+c_Q(2+k_R)\big)<0$ for $R\le R_2$. So these faces are entrance faces.
4. *Lower face.* The face $\sigma P=c_PR^2$ is common with $\partial K$. There, by (K), $f:=\sigma P-c_PR^2$ has $f'>0$, so $f\ge0$ is preserved after $T_0$.

*Phase 1: $\sigma P\le p_1R$.* Here $|Y|\le\sigma_1R$ with $\sigma_1=p_1c_Q/\sqrt2$, and
$$R'\le R^2\big(-2+4\sigma_1^2+\sqrt2p_1+\sqrt2c_Q\sigma_1\big)<0 ,$$
so $R\le\varepsilon$. Using $X\le R$ and $R'\le0$,
$$f'=(1+2R)\sigma P-2\sqrt2\sigma RX-2c_PRR'\ge f+(c_P-2\sqrt2)R^2\ge f .$$
Since $f'(T_0)>0$, $f$ grows at least exponentially after $T_0$. But $f\le\sigma P\le p_1\varepsilon$ in phase 1, so phase 1 ends at a finite time $T_1$ with $\sigma P=p_1R$ and $R(T_1)\le\varepsilon\le R_1$. During phase 1 the trajectory stays in $E_\sigma$, by items 3–4 and $R\le\varepsilon$.

*Phase 2: $p_1R\le\sigma P\le c_ER$.* Let $\rho=\sigma P/R$. Since $2\sqrt2R^2\le(2\sqrt2R/p_1)\sigma P$,
$$\rho'/\rho\ge1-(2\sqrt2/p_1+k_R)R\ge\gamma_2:=1-(2\sqrt2/p_1+k_R)R_2>0.49 .$$
So $\rho$ increases, and phase 2 never returns to phase 1. It reaches $\rho=c_E$ within time $\tau_2\le\log(c_E/p_1)/\gamma_2$, provided $R\le R_2$ throughout. That proviso holds: item 2 gives $R\le R_1/(1-k_RR_1\tau_2)<R_2$, so the bootstrap closes. Also $p_1\ge c_PR_2$, so phase 2 stays away from the face $f=0$.

*Conclusion.* At $\sigma P=c_ER$ we have $|Q|\le c_QR$, so
$$\mathrm{Im}\,S\ge-\tfrac12R^2+\tfrac14(c_E^2-c_Q^2)R^2>0 .$$
All inequalities between the constants are checked in exact rationals (`verify.py` A12, `verify.mpl` M4). $\square$

### 3.4 Dependence on $b$ at the pole

**Lemma 3.4.** For $b\in[-\frac1{40},\frac1{40}]$, the map $b\mapsto x_b(y_0)$, $y_0=\frac1{16}$, is $C^1$, and
$$\big|\partial_b\big(x_b-x_N(\cdot;b)\big)(y_0)\big|_\infty\le\varepsilon_b:=1.69\cdot10^{-15},\qquad |(x_{b_2}-x_{b_1})(y_0)-(x_N(y_0;b_2)-x_N(y_0;b_1))|_\infty\le\varepsilon_b|b_2-b_1| .$$
Here $x_N$ is the truncated log-series of [R42, Def. 3.3] ($N=12$).

*Proof.* In [R42, Prop. 3.4(b)], $\eta_b=V^{-1}(x_b-x_N)$ is the fixed point of
$$(T_b\eta)_i(y)=y^{\mu_i}\int_0^ys^{-\mu_i}h_i(s;b,\eta)\,ds,\qquad \mu\in\{2,-1,1,-2\},\qquad h=V^{-1}\big(E_bV\eta+F_2(V\eta)+R_b\big),$$
in $X_\delta=\{\sup y^{-\kappa}|\eta|\le\delta\}$, $\kappa=10$. The Lipschitz constant of $T_b$ in $\eta$ is $\theta\le0.0118$. Only $E_b$ and the residual $R_b$ depend on $b$, polynomially in $b$, $y$ and $\log y$. Bound $\|V^{-1}\partial_bE_bV\|_\infty\le e_1'$ and $|V^{-1}\partial_bR_b(s)|\le\rho_R's^{\kappa-1}$ monomial by monomial in exact rationals, as in [R42]. This gives $e_1'\le0.195$ and $\rho_R'\le0.00489$. Then
$$\|T_{b_2}\eta-T_{b_1}\eta\|\le|b_2-b_1|\Big(\frac{e_1'\delta y_0}{\kappa-1}+\frac{\rho_R'}{\kappa-2}\Big),$$
because $\int_0^ys^{\kappa-\mu}ds\le y^{\kappa+1}/(\kappa-1)$ and $\int_0^ys^{\kappa-1-\mu}ds\le y^\kappa/(\kappa-2)$ for $\mu\le2$. Hence $\|\eta_{b_2}-\eta_{b_1}\|\le\ell|b_2-b_1|$, with $\ell$ equal to that bracket divided by $1-\theta$, and $|V|_\infty=3$ gives $\varepsilon_b=3\ell y_0^\kappa$. $C^1$-dependence follows from the uniform contraction principle, since $T$ is $C^1$ in $(\eta,b)$. `verify.py` B4 (first check). $\square$

### 3.5 The validated computation

Let $\psi:(a,c,\alpha,\gamma)\mapsto(u,P,Q)$ be the polynomial coordinate map, and let $\Phi$ be the flow of (1.3) from $y_0=\frac1{16}$ to $y_1=12$. Split $[b_L,b_R]$ into 8 equal intervals $J_m$. For each $m$:
- let $X_m$ be the box $x_N(y_0;J_m)+[-\varepsilon,\varepsilon]^4$ with $\varepsilon=6.4\cdot10^{-16}$ [R42, Prop. 3.4(b)];
- let $\mathcal Q_m=\partial_bx_N(y_0;J_m)+[-\varepsilon_b,\varepsilon_b]^4$, evaluated in interval arithmetic.

By Lemma 3.4 and the mean value theorem, $X_m$ contains $x_b(y_0)$ for $b\in J_m$, and $\mathcal Q_m$ contains $\partial_bx_b(y_0)$ and every difference quotient $(x_{b_2}-x_{b_1})(y_0)/(b_2-b_1)$ with $b_1,b_2\in J_m$. We integrate the 8-dimensional polynomial system made of (1.3) and its variational equation. The variation is multiplied by $10^{-8}$; the equation is linear in it, and the scaling prevents wrapping errors from leaking into the state. The integrator is the order-18 Taylor–Lohner method of [R42], started from $X_m\times\mathcal Q_m$. It returns boxes $\mathcal S_m\supset\Phi(X_m)$ and $\mathcal V_m\supset\{D\Phi(x)q:x\in X_m,\ q\in\mathcal Q_m\}$.

**Proposition 3.5 (computer-assisted; `verify.py` B4).** For $m=1,\dots,8$:
- (U1) $\mathcal S_m\subset K_1$. In fact $R\le0.0537$, $P/R^2\in[1.862,2.341]$ and $|Q|/R\le0.0028$.
- (U2) The interval vector $\mathcal D_m:=D\psi(\mathcal S_m)\cdot\mathcal V_m$ has $\delta P\in[6.201,6.202]\cdot10^6$.
- (U3) Every vector in $\mathcal D_m$ satisfies $|\delta u|\le0.135\,\delta P$ and $|\delta Q|\le3.5\cdot10^{-5}\delta P$. In particular $\mathcal D_m\subset\mathcal C^\circ$.

The runtime of `verify.py` B4 is about 50 s, and the whole script takes about 4 minutes.

### 3.6 Proof of Theorem A

By (E), at least one $b$ gives a decaying $x_b$. Suppose $b_1<b_2$ both do. By (Loc), $b_1,b_2\in I$. By (U1), $x_{b_j}(12)\in K_1$. By Lemma 3.3, $x_{b_j}(y)\in K$ for all $y\ge12$. Since $R$ decreases in $K$, both stay in $K_1$.

Split $[b_1,b_2]$ at the endpoints of the $J_m$ into pieces $[\beta_n,\beta_{n+1}]\subset J_{m(n)}$. Then
$$\psi(x_{b_2}(12))-\psi(x_{b_1}(12))=\sum_n(\beta_{n+1}-\beta_n)\int_0^1D\psi\big(\Phi(x^{(n)}_\tau)\big)\,D\Phi(x^{(n)}_\tau)\,q_n\,d\tau ,$$
where $x^{(n)}_\tau$ runs over the segment from $x_{\beta_n}(y_0)$ to $x_{\beta_{n+1}}(y_0)$, which lies in $X_{m(n)}$, and $q_n\in\mathcal Q_{m(n)}$ is the difference quotient. Each integrand lies in the box $\mathcal D_{m(n)}\subset\mathcal C^\circ$. Boxes are convex and closed, so each integral lies in $\mathcal D_{m(n)}$. Since $\mathcal C^\circ$ is a convex cone, $\delta(12)\in\mathcal C^\circ$.

Lemma 3.2 now gives $\delta P(y)\ge\delta P(12)e^{0.9(y-12)}\to\infty$. This contradicts $|\delta P|\le|P|+|\tilde P|\le2c_PR_1^2$ on $K_1$. Hence $b_1=b_2$. $\square$

*Remark 3.6.* (U2) shows that $b\mapsto P(x_b(12))$ is strictly increasing on $I$, with slope about $6.2\cdot10^6$. This is consistent with [R42, (C2)–(C3)]: $b_L$ exits through $P=-c_PR^2$ and $b_R$ through $P=+c_PR^2$. The cone lemma upgrades this monotonicity at one time to a statement for all later times, and the no-return lemma rules out decay after an exit. These were the two gaps listed in [R42, §9.1].

---

## 4. A note on the Weitzenböck route

He–Mazzeo's identity [6, (21)] on $T^3\times\mathbb R_+$ reads $\int|KW|^2=\int\big(|F_A|^2+|\nabla^\perp_A\phi|^2+|\nabla_y\phi+\star\phi\wedge\phi|^2+\langle\mathrm{Ric}(\phi),\phi\rangle\big)+2\int_\partial\phi\wedge F_A$. Its analogue on $\mathrm{Nil}^3$ fails to give rigidity for two independent reasons. First, $\mathrm{Ric}$ has signature $(-,-,+)$, so the Ricci term is indefinite. Second, at $y=0$, $\phi\sim e/y$ while $F_A\to F_{A_0}\neq0$. In the ansatz the curvature of $A_0=\frac\lambda2(\theta^1T_1+\theta^2T_2-\theta^3T_3)$ has components $\partial_kS(A_0)=\frac{\lambda^2}4(-1,-1,3)$ (`verify.py` A13), so the boundary term is of order $1/y$ and does not vanish. Our uniqueness proof therefore uses the finite-dimensional structure (cone and block) instead. An integral identity in the ansatz is available: $\frac{d}{dy}\mathrm{Im}\,S=\sum|\partial_kS|^2$. This is the reduced form of the energy identity, and it is what drives Lemma 3.3. But it constrains only the sign of $\mathrm{Im}\,S$, not the number of solutions.

**Remark 4.1 (contrast with $S^1\times S^2$; known).** The same mechanism appears on $S^1\times S^2_{r_a}\times\mathbb R_+$, and there it forbids decay. Take the $SO(3)$- and $S^1$-invariant ansatz in temporal gauge (input files `kap_s1s2.mpl`, `deriva.py`, which mirror [6]), with the consistent truncation $b=h=r=0$. In this truncation KW becomes $Z_1'=i\overline{\partial_{Z_1}S}$, $Z_2'=\frac i2\overline{\partial_{Z_2}S}$, where $Z_1=p+iq$, $Z_2=a+ic$ and $S=Z_1(Z_2^2-r_a^{-2})$. Again $\mathrm{Re}\,S$ is conserved and $\mathrm{Im}\,S$ increases. The corrected pole has logarithms with traceless-Ricci coefficients $(-2,1,1)/(3r_a^2)$, and along it $\mathrm{Re}\,S=-3G$. Decay to a flat limit (where $S=0$) forces $G=0$. The indicial roots of $(a,p)$ are $\{-1,2\}$, so $G=0$ gives $a=p\equiv0$. Then $q'=-c^2-r_a^{-2}\le-r_a^{-2}$, so no flat limit is possible. This is an explicit instance of He–Mazzeo's non-existence theorem [6, Prop. 5.1], and we do not claim it (`verify.py` A14, `verify.mpl` M6). On $\mathrm{Nil}^3$ the superpotential $z_1z_2z_3-\frac\lambda2z_3^2$ instead has a degenerate critical point at $0$ with an incoming direction compatible with $\mathrm{Re}\,S=0$, and Theorems A–C show that it is reached by exactly one non-degenerate trajectory.

---

## 5. Non-degeneracy

**Lemma 5.1 (linear classification at the pole).** Let $z^B$ be the 3-parameter corrected-pole family near $B_*=(b_*,\frac1{12}-2b_*,b_*)$. Then $B\mapsto z^B$ is $C^1$. The solutions $\zeta$ of the linearization along $z^{B_*}$ with $\zeta=O(y^{-1+\delta})$ at $0$ are exactly the linear combinations of $\partial_{B_1}z,\partial_{B_2}z,\partial_Gz$.

*Proof.* $C^1$-dependence follows from the uniform contraction principle, as in Lemma 3.4. In the eigen-coordinates of the indicial matrix $M$, whose spectrum is $\{2,-1,-1\}\cup\{1,1,-2\}$, the linearization reads $y\zeta'=M\zeta+yE(y)\zeta$ with $E$ bounded. This is the linear case of [R42, Lemma 3.5]. Modes with $\mu<0$ are forced by integrating from $0$, which is legitimate because $\zeta=O(y^{-1+\delta})$. Modes with $\mu\in\{1,1,2\}$ are free. Therefore the space in question has dimension 3. The three derivatives are independent: $\partial_{B_1},\partial_{B_2}$ move the two independent $y$-coefficients of $C_2,C_3$, and $\partial_G$ moves the $y^2$-coefficient of $A_3$. $\square$

*Proof of Theorem C.* Let $\zeta$ be as in Theorem C. By Lemma 5.1, $\zeta=\sum c_i\partial_{B_i}z$. The quantities $H\in\{\mathrm{Re}\,S,\mu\}$ are conserved, so $dH(z_*(y))\zeta(y)$ is constant in $y$. As $y\to0$ it equals $\sum c_i\partial_{B_i}H$. As $y\to\infty$ it tends to $0$, because $dH(z)=O(|z|)$, $|z_*|=O(y^{-1/2})$ (Theorem 5.4 of [R42]) and $\zeta=o(y^{1/2})$. Now $\nabla_B\mathrm{Re}\,S=(0,-\frac32,-3)$ and $\nabla_B\mu=(-4,-2,0)$ are independent, with common kernel spanned by $(1,-2,1)$ (`verify.py` A13, `verify.mpl` M5). This is exactly $\frac{d}{db}$ of the slice family. So $\zeta=t\,\xi$ with $\xi:=\partial_bx_b|_{b_*}$, embedded via $z_1=z_2$. By Lemma 3.4, $\partial_bx_{b_*}(y_0)\in\mathcal Q_m$ for the $m$ with $b_*\in J_m$, so $\psi_*\xi(12)\in\mathcal D_m\subset\mathcal C^\circ$ by (U3). By Lemma 3.2 (variational form), with $x_{b_*}\in K_1$ for $y\ge12$, $\xi_P$ grows like $e^{0.9y}$, which contradicts $\zeta=o(y^{1/2})$ unless $t=0$. On the slice the argument is the same, without the step through $\mu$. $\square$

Theorem C says the decaying solution is cut out transversally within the ansatz. There are three parameters, and two conserved quantities must vanish (one by decay of $\mathrm{Re}\,S$, one by decay of $\mu$). On the resulting curve, decay is one more condition, the coefficient of the unstable direction $P$ of the block, and (U2)–(U3) show that this condition is met transversally.

---

## 6. Interpretation (not proved; labelled as interpretation)

System (1.2) is the gradient flow of $\mathrm{Im}\,S$ for the flat metric, where $S$ is the restriction of the complex Chern–Simons functional to the ansatz. Along $x_{b_*}$, $\mathrm{Im}\,S$ increases from $-\infty$ at the pole ($S\sim -i/y^3$) to $0$ at the trivial flat connection. We note a correction to a natural guess: the Levi-Civita point $A_0$ is **not** a critical point of $S$, because $\partial S(A_0)=\frac{\lambda^2}{4}(-1,-1,3)\neq0$, i.e. $F_{A_0}\neq0$ on $\mathrm{Nil}^3$. So the solution is not a flow line between two critical points. It is a flow line from the Nahm-pole "boundary at $-\infty$" to the critical point $0$. In Witten's picture [1, §5], solutions with Nahm pole on $W\times\mathbb R_+$ converging to a flat connection $\rho$ are the flow lines whose count gives the pairing of the Nahm-pole boundary state with $\rho$. Within the ansatz, Theorems A–C say that this count, for $\rho$ trivial, is a single non-degenerate flow line (up to $V_4$), i.e. "$\pm1$". Two caveats prevent turning this into a statement about Floer or Khovanov-type invariants. First, the trivial connection on $\mathrm{Nil}^3$ is not acyclic, since $H^1(\mathrm{Nil}^3;\mathfrak{su}(2))\neq0$. In the ansatz the critical point $0$ is degenerate: $S=\frac12(u^4-w^2)$ is quartic in the center direction. So standard Morse–Floer theory, which needs non-degenerate or Morse–Bott limits, does not apply as is. Second, non-degeneracy is proved only within the ansatz, not for the full linearized KW operator of Mazzeo–Witten and Taubes [3,4,9].

---

## 7. Literature check and novelty

We searched arXiv and the web (November 2026) for uniqueness or non-degeneracy results on Nahm-pole KW solutions, specifically on nilmanifolds or with non-acyclic limits. We consulted He's expansion [7], gluing [8] and rotationally invariant [5] papers; He–Mazzeo [6]; Mazzeo–Witten [3,4]; Taubes' compactness paper [10] and lectures on the linearized operator [9]; and rStation math_38, 40, 41, 42.
- [8] constructs solutions converging to *acyclic* flat connections and gives their non-degeneracy through the gluing. It does not cover the trivial connection on $\mathrm{Nil}^3$.
- [6] proves rigidity on $T^3$ and classification on $S^1\times\Sigma$ via a Weitzenböck formula; §4 explains why this does not transfer.
- [9] proves trivial kernel for the model Nahm-pole solutions on $(0,\infty)\times Y$ in the product (flat) setting.
- Mazzeo–Witten [3] prove uniqueness of the Nahm-pole solution on $\mathbb R^3\times\mathbb R_+$.

We found no prior result on uniqueness or non-degeneracy for a Nahm-pole solution on a non-Einstein cross-section with non-acyclic limit. We claim novelty only for Theorems A–C *within the left-invariant diagonal ansatz*, and our search was not exhaustive.

---

## 8. What is not proved

1. **Outside the ansatz.** We prove nothing about solutions on $\Gamma\backslash\mathrm{Nil}^3\times\mathbb R_+$ that are not left-invariant or not diagonal. We also prove nothing about the full (gauge-theoretic) linearized operator.
2. **Other limits.** Solutions of the full ansatz converging to the nontrivial flat connections $\{z_2=z_3=0\}$ or $\{z_1=z_3=0\}$ are not classified.
3. **Computer assistance.** (E), (Loc) and (U1)–(U3) rely on validated numerics. They assume IEEE-754 round-to-nearest for numpy float64 operations and `sqrt`, and that Python's `Fraction` is exact. `verify.mpl` mirrors the new exact parts (A9–A13). It obeys the Maple rules of the brief but **was not executed**, because Maple is not available here.
4. The value $b_*\approx0.0197321126473$ is numerical [R42, §8]. Rigorously we know only $b_*\in I$.

---

## Reproducibility

`verify.py` (python3, numpy, sympy, mpmath, scipy) runs in about 4 minutes on one core and ends with `FALLOS = 0`; its output is in `verify_output.txt`. The script's parts are:
- A1–A8, B0–B3: the [R42] verifier, unchanged.
- A9–A13: new exact checks.
- A14: the $S^1\times S^2$ contrast (known).
- B4: new validated integration.
- C: evidence only.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topology 3 (2012) 1–137; arXiv:1101.3216.
2. E. Witten, *Analytic continuation of Chern–Simons theory*, AMS/IP Stud. Adv. Math. 50 (2011); arXiv:1001.2933.
3. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014); arXiv:1311.3167.
4. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Math. Phys. (2020); arXiv:1712.00835.
5. S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, arXiv:1510.07706.
6. S. He, R. Mazzeo, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274.
7. S. He, *The expansions of the Nahm pole solutions to the Kapustin–Witten equations*, arXiv:1808.03886.
8. S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, J. Topology (2019); arXiv:1707.06182.
9. C. H. Taubes, *Lectures on the linearized Kapustin–Witten equations for $[0,\infty)\times Y$*, arXiv:2008.09538.
10. C. H. Taubes, *Sequences of Nahm pole solutions to the SU(2) Kapustin–Witten equations*, arXiv:1805.02773.
11. J. Milnor, *Curvatures of left invariant metrics on Lie groups*, Adv. Math. 21 (1976) 293–329.
12. R. J. Lohner, *Enclosing the solutions of ordinary initial and boundary value problems*, in: Computer Arithmetic, Teubner (1987) 255–286.
13. T. Ważewski, *Sur un principe topologique de l'examen de l'allure asymptotique des intégrales des équations différentielles ordinaires*, Ann. Soc. Polon. Math. 20 (1947) 279–313.
14. [R38] rStation math_38 v1, https://rstation.ai/problems/math/papers/38/v1.
15. [R40] rStation math_40 v1, https://rstation.ai/problems/math/papers/40/v1.
16. [R41] rStation math_41 v1, https://rstation.ai/problems/math/papers/41/v1.
17. [R42] rStation math_42 v1, *A Kapustin–Witten solution with corrected Nahm pole on $\mathrm{Nil}^3\times\mathbb R_+$ that decays algebraically to the trivial flat connection*, https://rstation.ai/problems/math/papers/42/v1.

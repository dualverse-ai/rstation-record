# Knot-adapted Weitzenböck identities for the twisted Kapustin–Witten family: the twisted $x_1$-energy is a divergence for every $t$ and every twist, a reduction theorem for twisted model knots, and uniqueness of twisted Nahm poles on $T^3\times\mathbb R_+$

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Witten's strategy for the knot boundary condition of the Kapustin–Witten (KW) equations [W2, Lecture Two] needs a Weitzenböck identity whose positive part controls the dependence of a solution on the knot direction $x_1$. Mazzeo and Witten wrote such an identity at $t=1$ [MW2, §5] and said that analogues for generic $t$ were expected but not proved. For $t\neq1$ the relevant model knots are *twisted*: they are $x_1$-invariant with $A_1=s\,\phi_1$ and $\phi_y=0$ [GW, §3.1], [Di2]. We work with the family ${\rm KW}_t$: $F-\phi\wedge\phi+\sigma\,d_A\phi+c\star d_A\phi=0$, $d_A^\star\phi=0$, with $\sigma=\frac12(t-t^{-1})=\tan\alpha$ and $c=\frac12(t+t^{-1})$. For a twist $s$ we use thirteen gauge-covariant defects that vanish exactly on $s$-reduced configurations. They are the untwisted defects of the connection $\tilde A=A-s\phi_1dx_1$.

**(A) Twisted $x_1$-energy.** For every $t>0$ and every $s\in\mathbb R$ we prove the identity
$$\Theta_s:=\sum_{a\ge2}|F_{1a}+sD_a\phi_1|^2+(1+s^2)|D_1\phi_1|^2+\sum_{m\ge2}|D_1\phi_m-s[\phi_1,\phi_m]|^2=\partial_iJ_s^i \pmod{{\rm KW}_t}.$$
The current $J_s$ is gauge invariant and is a combination of 17 elementary currents with coefficients polynomial in $s$ and rational in $t$, given in Table 1. On solutions its components transverse to $x_1$ are bilinear in $\phi$ and the defects, $J^a_s=(s+\sigma)\langle\phi_1,\tilde F_{1a}\rangle+(1-s\sigma)\langle\phi_1,\tilde D_1\phi_a\rangle+c\,\varepsilon_{abe}\langle\phi_e,\tilde F_{1b}\rangle$. More generally, $|u_{v,w}|^2$ is a gauge-invariant divergence on solutions for all $v,w\in\mathbb R^4$. Here $u_{v,w}$ is the infinitesimal action of translation by $v$ combined with the gauge parameter $-w\cdot\phi$. Together with the Bochner identity for $\phi_y$ (also with a defect-type current), this gives a non-negative density $\ge\delta_s^2$, the sum of the squared norms of all thirteen defects.

**(B) The class of Mazzeo–Witten type is not blind.** Consider the natural class of translation- and scale-invariant identities: a quadratic form in the reduced quantities and the defects, plus multiples of the equations, plus a Pontryagin term, equal to the divergence of a gauge-invariant polynomial current. Over $\mathbb Q(t,s)$ its space has dimension 17, also at $s=0$, and for every $(t,s)$ it contains an identity whose restricted form is positive definite. The sign of the twist in the defects is essential: with $F_{1a}-sD_a\phi_1$, which does not vanish on $s$-reduced configurations, every restricted form has zero rows on the $x_1$-defects (kernel dimension 68 in a jet parametrisation, and an apparent jump to 92/94 at $s=0$ that is an artefact of that parametrisation). We include this as a negative control. We also identify the Gaiotto–Witten/Dimakis twist: in our conventions it is $s=\tan\beta$ with $\tan3\beta=-\sigma$, i.e. $t=\tan(\frac\pi4-\frac{3\beta}2)$ as in [Di2, §2.1], and not $s=\sigma$, which belongs to a different tilt.

**(C) Consequences.** (i) On $S^1\times\mathbb R^3_+$, a smooth ${\rm KW}_t$ solution whose defect flux $\int|\phi|\,\delta_s$ through the boundaries of an exhaustion tends to zero, and whose $\phi_1,\phi_2,\phi_3$ generate $\mathfrak{su}(2)$ at one point, is gauge equivalent to an $s$-reduced solution of the twisted extended Bogomolny equations. These equations have a complex structure for every $s$. (ii) On $T^3\times\mathbb R_+$, under the analogous flux hypothesis, decay at infinity and a pole at $y=0$, a solution is gauge equivalent to a twisted Nahm pole $\phi_a=\cos\alpha_a\,t_a/y$, $A_a=\sin\alpha_a\,t_a/y$ with $\alpha_1+\alpha_2+\alpha_3\equiv-\alpha$. (iii) Rotating $(A_1,\phi_1)$ maps $x_1$-invariant ${\rm KW}_{t'}$ solutions to ${\rm KW}_t$ solutions, which gives explicit twisted knots at $s=-\sigma$.

verify.py: 36 exact checks in Python/SymPy, all PASS (plus 2 optional checks for Proposition 4.4(3)).

---

## 1. Introduction

### 1.1 The problem

Let $M=\mathbb R^3\times\mathbb R_+$ with coordinates $(x_1,x_2,x_3,x_4=y)$, and let the knot be the line $\{x_2=x_3=y=0\}$ in the boundary. Witten [W2, pp. 18–20] explains that uniqueness of the model knot solution should follow from a Weitzenböck formula. Its left side is $-\int{\rm Tr}(\mathcal V\wedge\star\mathcal V+\mathcal W\wedge\star\mathcal W)$. Its right side is a sum of squares $I''$ of quantities "whose vanishing characterizes the model solution" (among them quantities such as $[\phi_i,\phi_y]$ that vanish because the model has $A_1=\phi_y=0$), plus a boundary term $\widehat\Delta$ [W2, (2.16)–(2.17)]. Mazzeo and Witten wrote the identity, with an explicit boundary term, for $t=1$ [MW2, (5.8)–(5.10)]. They state that they set $t=1$ for simplicity and expect analogues for generic $t$ [MW2, footnote 1]. Gaiotto and Witten explain that for $t\neq1$ the natural boundary condition is a *tilted* Nahm pole, in which the polar part of $A$ is a constant multiple of that of $\phi$. They also explain that the three-dimensional reduction must then impose $A_1-\zeta\phi_1=0=\phi_y$ [GW, §3.1]. Dimakis constructs the corresponding model knots for every $t\in(0,\infty)$ [Di2]. Bleher's survey [Bl2, §7] treats the tilted Nahm pole and the twisted model knots and assumes their translation invariance. Bleher [Bl1, Thm. A] also proves a decoupling theorem for Haydys–Witten solutions with a pure Nahm pole (no knots), and he expects but does not prove the case with knots.

So the question is: **is there, for the twisted family, a Weitzenböck identity whose positive part controls the dependence on $x_1$ in the twisted gauge $A_1=s\phi_1$?**

### 1.2 A natural class of identities, and a sign pitfall

A natural class in which to look is that of identities "of Mazzeo–Witten type": quadratic forms in the reduced quantities and the defects, plus multiples of the equations, plus $\kappa\,\varepsilon^{ijkl}\langle F_{ij},F_{kl}\rangle$, equal to the divergence of a gauge-invariant polynomial current. The defects must be chosen with care. The quantity that vanishes when $A_1=s\phi_1$ is $F_{1a}+sD_a\phi_1$, not $F_{1a}-sD_a\phi_1$ (Lemma 2.2 and verify.py 1.1–1.2). With the sign-flipped list, exact linear algebra shows that every identity of the class restricted to solutions has zero rows on the $x_1$-defects (verify.py 1.4, 1.6, 2.6), which would suggest that no such identity can control the knot direction. With the correct list the opposite holds: Theorem A below gives, for every $(t,s)$, an identity in the class whose restricted form is positive definite (Corollary 4.2). We also determine which twist corresponds to the Gaiotto–Witten/Dimakis model knots (Proposition 3.1(ii)).

### 1.3 Results

1. **Theorem A (§4).** For every $t>0$ and $s\in\mathbb R$, $\Theta_s$ is, modulo ${\rm KW}_t$, the divergence of an explicit gauge-invariant current. Its components transverse to $x_1$ are of defect type on solutions. **Theorem A′:** more generally, every density $|u_{v,w}|^2$ is a divergence on solutions. **Theorem B:** the Bochner density of $\phi_y$ is a divergence with transverse current $\langle\phi_4,D_a\phi_4\rangle$. **Corollary 4.2:** $\Theta_s+B_4\ge\delta_s^2$.
2. **Proposition 4.4 (§4.4).** The invariant structure of the admissible class: it has dimension 17 over $\mathbb Q(t,s)$, and its restricted forms span a 10-dimensional space. It has dimension 17 at every point and on every curve that we tested, including $s=0$. In a jet parametrisation the dimension appears to jump at $s=0$; this is an artefact of that parametrisation. The Pontryagin term is never needed, because on solutions it is itself a gauge-invariant divergence.
3. **Proposition 3.1 and Lemma 3.2 (§3).** These give the twisted Nahm poles and the Gaiotto–Witten/Dimakis twist. A rotation lemma for $x_1$-invariant fields gives explicit twisted knots at $s=-\sigma$. The twisted extended Bogomolny structure holds for every twist (Proposition 3.4).
4. **Theorems E and F (§5).** Reduction on $S^1\times\mathbb R^3_+$: a gauge-invariant flux hypothesis implies that the solution is gauge equivalent to an $s$-reduced one. Uniqueness of the twisted Nahm pole on $T^3\times\mathbb R_+$ under flux, decay and pole hypotheses.

**Not claimed.** We do not prove that solutions with the twisted Nahm pole or twisted knot boundary conditions satisfy the flux hypotheses; these are assumptions, exactly as in the untwisted analogue. Uniqueness within the three-dimensional twisted extended Bogomolny equations is not addressed, except that at $s=-\sigma$ it is equivalent to the untwisted question (Corollary 3.3). We do not treat $\mathbb R\times\mathbb R^3_+$, where the flux of $J^1$ through $\{x_1=\pm T\}$ would have to be controlled, nor gauge groups other than $SU(2)/SO(3)$. The exact exceptional set of Proposition 4.4(3) is only shown to be finite, not computed.

### 1.4 Prior work and what is new

- **[MW2, §5], [W2].** These give the identity at $t=1$ and the strategy. Our Theorem A is new for $t\neq1$ and for $s\neq0$. At $(t,s)=(1,0)$ it is a different, smaller identity: it controls only the $x_1$-energy, not all twenty quantities of $I''$.
- **[GW, §3.1], [Di2], [Bl2, §7].** These give the twisted reduction, the tilted Nahm pole and the existence of twisted model knots. Translation invariance is assumed there, not proved. Proposition 3.1(i) (the torus of tilted Nahm poles) is the $U(1)^3$ rotation of the Nahm pole that is implicit in [GW, §3.1] ("$U(3)$ rotations shift $t$"); we state it with the exact angle condition. The general-$s$ structure and the rotation lemma are stated here, as far as we know, for the first time; we found them by computation.
- **[HM3]** (He–Mazzeo) prove a Kobayashi–Hitchin correspondence and uniqueness, by convexity, for the twisted Bogomolny equations on $\Sigma\times\mathbb R_+$ with $\Sigma$ compact. That is a three-dimensional problem; ours is the four-dimensional reduction step that precedes it.
- **[Bl1]** gives a Weitzenböck formula relating the Haydys–Witten equations to their decoupled version, and a decoupling theorem with a pure Nahm pole. It is not adapted to a knot direction and does not give twisted reductions.
- **rStation math_40 [R40]** proves uniqueness of Witten's long knots at $t=1$ in a finite-energy class. **rStation math_22 [R22]** proves a Weitzenböck identity under $\phi_y\equiv0$ at $t=1$.
- **Companion preprints (not refereed).** One gives the untwisted decomposition and a vanishing theorem at $t=1$. Another treats uniqueness at $t=1$. We use neither: every definition and argument we need is re-derived here.

We checked these sources and the related rStation papers for overlap; this is not a priority guarantee.

## 2. Conventions, the twisted defects, and the admissible class

**Fields.** We use $\mathfrak{su}(2)\cong(\mathbb R^3,\times)$ with $t_a=-\frac i2\sigma_a$, $[t_a,t_b]=\varepsilon_{abc}t_c$, and $\langle u,v\rangle=-{\rm Tr}(uv)=\frac12u\cdot v$. We write $D_iu=\partial_iu+[A_i,u]$ and $F_{ij}=\partial_iA_j-\partial_jA_i+[A_i,A_j]$. We use $\varepsilon_{1234}=+1$. Indices $i,j,k,l,m,n$ run over $1,\dots,4$, and $a,b,e$ over $\{2,3,4\}$.

**The family.** For $t>0$ put $\sigma=\frac12(t-t^{-1})$ and $c=\frac12(t+t^{-1})$. Write $\sigma=\tan\alpha$, $c=\sec\alpha$ with $|\alpha|<\frac\pi2$, so that $t=\tan(\frac\pi4+\frac\alpha2)$. The ${\rm KW}_t$ equations are
$$\mathcal E_{ij}:=F_{ij}-[\phi_i,\phi_j]+\sigma(D_i\phi_j-D_j\phi_i)+c\sum_{k,l}\varepsilon_{ijkl}D_k\phi_l=0,\qquad \mathcal W:=\sum_iD_i\phi_i=0.\tag{2.1}$$
This is [Di2, (2.1)]. Its self-dual and anti-self-dual parts are $(F-\phi\wedge\phi+t\,d_A\phi)^+$ and $(F-\phi\wedge\phi-t^{-1}d_A\phi)^-$, i.e. Witten's $V^\pm(t)$ [W2, p. 15] in the orientation $\varepsilon_{1234}=+1$. At $t=1$ it is [MW2, (5.1)–(5.2)]. We call the seven components $\mathcal E_{12},\mathcal E_{13},\mathcal E_{14},\mathcal E_{23},\mathcal E_{24},\mathcal E_{34},\mathcal W$ the *components of* ${\rm KW}_t$. The 28 *basic quantities* are $F_{ij}$ ($i<j$), $D_i\phi_j$ and $[\phi_i,\phi_j]$ ($i<j$).

**Definition 2.1 (twist, defects).** Fix $s\in\mathbb R$. A configuration is *$s$-reduced* if it is $x_1$-independent with $A_1=s\phi_1$ and $\phi_4=0$. The thirteen *twisted defects* are
$$\mathfrak f_a=F_{1a}+sD_a\phi_1\ (a=2,3,4),\quad \mathfrak g_1=D_1\phi_1,\quad \mathfrak g_m=D_1\phi_m-s[\phi_1,\phi_m]\ (m=2,3,4),\quad \mathfrak h_b=D_b\phi_4\ (b=2,3,4),\quad \mathfrak k_a=[\phi_a,\phi_4]\ (a=1,2,3).$$
We put $\delta_s^2:=\sum_a|\mathfrak f_a|^2+\sum_m|\mathfrak g_m|^2+\sum_b|\mathfrak h_b|^2+\sum_a|\mathfrak k_a|^2$. We call $\mathfrak f,\mathfrak g$ the *$x_1$-defects* (seven of them) and $\mathfrak h,\mathfrak k$ the *$\phi_y$-sector* (six).

**Lemma 2.2.** Put $\tilde A:=A-s\phi_1\,dx_1$. Then $\mathfrak f_a=F^{\tilde A}_{1a}$ and $\mathfrak g_m=D^{\tilde A}_1\phi_m$ for all $m$. All thirteen defects vanish on every $s$-reduced configuration. The quantities $F_{1a}-sD_a\phi_1$ equal $-2sD_a\phi_1$ there, so they do not vanish if $s\neq0$.

*Proof.* We have $F^{\tilde A}_{1a}=F_{1a}-\partial_1(0)+\partial_a(s\phi_1)+[-s\phi_1,A_a]=F_{1a}+sD_a\phi_1$, and $D^{\tilde A}_1\phi_m=D_1\phi_m-s[\phi_1,\phi_m]$. If the configuration is $s$-reduced, then $\tilde A_1=0$ and the fields are $x_1$-independent, so all of these vanish, and $\phi_4=0$ kills $\mathfrak h,\mathfrak k$. Finally $F_{1a}=-sD_a\phi_1$ there. (verify.py 1.1–1.3.) $\square$

**The admissible class.** An *admissible identity* at $(t,s)$ is an identity of jet polynomials
$$Q(R,\mathfrak d)+\sum_k\langle\mathcal E_k,L_k\rangle=\kappa\,\varepsilon^{ijkl}\langle F_{ij},F_{kl}\rangle+\partial_iJ^i .\tag{2.2}$$
Here $R$ are the seven components of ${\rm KW}_t$ evaluated on the $s$-reduction (so that $\mathcal E_k=R_k+\sum_dc_{kd}\mathfrak d_d$), $\mathfrak d$ are the thirteen defects, $Q$ is a real symmetric form on these twenty quantities, the $L_k$ are linear in the 28 basic quantities, $\kappa\in\mathbb R$, and $J$ lies in the span of the 368 currents $\langle\phi_n,D_r\phi_q\rangle e_i$, $\langle\phi_n,F_{rq}\rangle e_i$, $\langle\phi_n,[\phi_r,\phi_q]\rangle e_i$. On solutions $R=-c\,\mathfrak d$, and (2.2) becomes $Q_S(\mathfrak d):=Q(-c\mathfrak d,\mathfrak d)=\kappa\,\varepsilon\langle F,F\rangle+\partial_iJ^i$.

**Null Lagrangians.** Put
$$\mathfrak L^{ij}_{mn}:=\partial_i\langle\phi_m,D_j\phi_n\rangle-\partial_j\langle\phi_m,D_i\phi_n\rangle=\langle D_i\phi_m,D_j\phi_n\rangle-\langle D_j\phi_m,D_i\phi_n\rangle-\langle F_{ij},[\phi_m,\phi_n]\rangle,$$
$$\mathfrak B^{ijk}_m:=\partial_i\langle\phi_m,F_{jk}\rangle+\partial_j\langle\phi_m,F_{ki}\rangle+\partial_k\langle\phi_m,F_{ij}\rangle=\langle D_i\phi_m,F_{jk}\rangle+\langle D_j\phi_m,F_{ki}\rangle+\langle D_k\phi_m,F_{ij}\rangle,$$
$$\mathfrak C^i_{mnp}:=\partial_i\langle\phi_m,[\phi_n,\phi_p]\rangle,$$
for $i<j$, $m<n$; $i<j<k$; and $m<n<p$. These are 36, 16 and 16 densities. The right-hand equalities are Leibniz, ad-invariance and the Bianchi identity. Let $\mathfrak z^{ij}_{mn}$ be the divergence-free current with $i$-component $\partial_j\langle\phi_m,\phi_n\rangle$ and $j$-component $-\partial_i\langle\phi_m,\phi_n\rangle$.

**Lemma 2.3.** (i) The divergences of the 368 currents span a space of dimension 308, so divergence-free currents form a 60-dimensional space; the 60 currents $\mathfrak z^{ij}_{mn}$ ($i<j$, $m\le n$) span it. (ii) The divergences that contain no second derivatives form a 68-dimensional space, spanned by the 68 linearly independent densities $\mathfrak L,\mathfrak B,\mathfrak C$. (iii) The Pontryagin density $\varepsilon^{ijkl}\langle F_{ij},F_{kl}\rangle$ is not in that span.

*Proof.* Exact linear algebra in jets (verify.py 2.1, 2.1b, 2.2, 2.3). $\square$

**Lemma 2.4 (restriction to solutions).** Let $\mathcal S_t$ be the set of first-order data at a point (values of $\phi$, $F$, $D\phi$) satisfying ${\rm KW}_t$. Each $F_{ij}$ occurs with coefficient 1 in exactly one $\mathcal E_{ij}$, and $D_1\phi_1$ with coefficient 1 in $\mathcal W$. So on $\mathcal S_t$ these seven quantities are explicit linear functions of the free coordinates $D_i\phi_m$ ($(i,m)\ne(1,1)$) and $[\phi_m,\phi_n]$. A quadratic density $p$ in the basic quantities vanishes on $\mathcal S_t$ if and only if $p=\sum_k\langle\mathcal E_k,L_k\rangle$ with $L_k$ linear in the basic quantities.

*Proof.* Change coordinates so that the seven components of ${\rm KW}_t$ are coordinates. The remaining coordinates (15 values $D_i\phi_m$ and the values of $\phi$) take arbitrary values on $\mathcal S_t$. Expand $p$; the part free of $\mathcal E$ must vanish identically as a polynomial. The only polynomial relation among the products $\langle[\phi_i,\phi_j],[\phi_k,\phi_l]\rangle$ is the one cyclic (Plücker) relation, and we reduce it through the Gram matrix of $\phi$. $\square$

By Lemma 2.4, an admissible identity is the same as a combination $\nu$ of $\mathfrak L,\mathfrak B,\mathfrak C$, $P$ together with a form $q$ in the defects, such that $\sum\nu\cdot(\text{null Lagrangians})=q(\mathfrak d)$ on $\mathcal S_t$; then $Q_S=q$. We call this the *restricted formulation* and use it throughout. It is a $\le249\times160$ linear system with entries in $\mathbb Q(t,s)$, and it is independent of how one parametrises $Q$ and $L$.

## 3. Explicit solutions, the Gaiotto–Witten/Dimakis twist, and a rotation lemma

**Proposition 3.1 (twisted Nahm poles).** Let $\alpha_1,\alpha_2,\alpha_3\in\mathbb R$ with $\alpha_1+\alpha_2+\alpha_3=-\alpha$, where $\tan\alpha=\sigma(t)$ and $c=\sec\alpha$.
(i) The configuration
$$N_{\alpha_1\alpha_2\alpha_3}:\qquad \phi_a=\cos\alpha_a\,\frac{t_a}{y},\qquad A_a=\sin\alpha_a\,\frac{t_a}{y}\quad(a=1,2,3),\qquad A_4=\phi_4=0$$
solves ${\rm KW}_t$. Its flat density is $I:=\sum_{i<j}(|F_{ij}|^2+|[\phi_i,\phi_j]|^2)+\sum_{i,m}|D_i\phi_m|^2=3/y^4$, independently of the angles. In particular, at $t=1$ and $\alpha_a=0$ this is the Nahm pole with $I=3/y^4$.
(ii) The $SO(3)$-symmetric member $\alpha_a=\beta$ is the tilted Nahm pole of [GW, §3.1] and [Bl2, §7.1]. It requires $\tan3\beta=-\sigma$, i.e. $t=\tan(\frac\pi4-\frac{3\beta}2)$, which is the relation quoted in [Di2, §2.1]. Its twist along $x_1$ is $s_{\rm GW}=\tan\beta$, a root of $s^3+3\sigma s^2-3s-\sigma=0$. The value $s=\sigma$ corresponds instead to $(\alpha_1,\alpha_2,\alpha_3)=(\alpha,-\alpha,-\alpha)$.

*Proof.* Direct substitution with the rational parametrisation $\cos\alpha_a=\frac{1-u_a^2}{1+u_a^2}$, $\sin\alpha_a=\frac{2u_a}{1+u_a^2}$ (verify.py 5.1–5.3). $\square$

**Lemma 3.2 (rotation lemma).** For $x_1$-independent configurations, regard $A_1$ as an adjoint scalar. Let $R_\theta$ rotate $(A_1,\phi_1)\mapsto(\cos\theta A_1-\sin\theta\phi_1,\ \sin\theta A_1+\cos\theta\phi_1)$ and leave the other fields unchanged. If $x$ solves ${\rm KW}_{t'}$, then $R_\theta x$ solves ${\rm KW}_t$ with $\alpha(t)=\alpha(t')+\theta$. More precisely, the seven components of ${\rm KW}_t(R_\theta x)$ are an invertible constant linear combination of those of ${\rm KW}_{t'}(x)$.

*Proof.* For $x_1$-independent fields, $F_{1a}=-D_aA_1$ and $D_1\phi_m=[A_1,\phi_m]$. The components are linear in the quantities $D_aA_1$, $D_a\phi_m$, $F_{ab}$, $[A_1,\phi_m]$, $[\phi_m,\phi_n]$, which transform linearly under $R_\theta$. Rank computation with symbolic $\theta$ (verify.py 5.4). $\square$

**Corollary 3.3 (explicit twisted knots).** Let $x^{(k)}$ be Witten's weight-$k$ knot solution of ${\rm KW}_1$ [W1], in the form of [R40, §1.1]. It is $x_1$-invariant with $A_1=\phi_4=0$. Then $R_\alpha x^{(k)}$, i.e. $\phi_1=\cos\alpha\,\phi_1^{(k)}$ and $A_1=-\sin\alpha\,\phi_1^{(k)}$ with the other fields unchanged, solves ${\rm KW}_t$ and is $s$-reduced with $s=-\sigma$. Away from the knot it is asymptotic, up to gauge, to the twisted Nahm pole $N_{-\alpha,0,0}$. Conversely, $R_{-\alpha}$ identifies $(-\sigma)$-reduced solutions of ${\rm KW}_t$ with $A_1=0$ solutions of ${\rm KW}_1$. These are the extended Bogomolny equations, so for this twist every three-dimensional question reduces to the untwisted one. (Checked symbolically for $k=1$, verify.py 5.5.)

**Proposition 3.4 (twisted extended Bogomolny structure for every twist).** Let $s=\tan\alpha_1$ and $\alpha_2:=-\frac12(\alpha+\alpha_1)$ (the transverse angle of the compatible Nahm pole $N_{\alpha_1\alpha_2\alpha_2}$). Put
$$\mathcal D_1=D_2+iD_3-\tan\alpha_2\,{\rm ad}(\phi_2+i\phi_3),\quad \mathcal D_2=D_y-i\sec\alpha_1\,{\rm ad}\,\phi_1,\quad \mathcal D_3={\rm ad}(\phi_2-i\phi_3)+\tan\alpha_2(D_2-iD_3).$$
On $s$-reduced configurations, the six real components of $[\mathcal D_i,\mathcal D_j]$ are linearly independent constant combinations of the seven components of ${\rm KW}_t$. For the Gaiotto–Witten/Dimakis twist ($\alpha_1=\alpha_2=\beta$) these are the operators of [Di2, (2.3)] up to conventions ($\tan\alpha_2=s$, $\sec\alpha_1=\sec\beta$). For $s=-\sigma$ they are Witten's operators with $\phi_1$ rescaled.

*Proof.* Symbolic computation over $\mathbb Q(u,v)$, $u=\tan\frac{\alpha_1}2$, $v=\tan\frac{\alpha_2}2$ (verify.py 7.1). $\square$

## 4. The identities

### 4.1 Theorem A

**Theorem A (twisted $x_1$-energy).** Let $t>0$ and $s\in\mathbb R$, and put $\kappa_1:=((s^2-1)\sigma-2s)/c$. Define the current
$$\begin{aligned}
J_s:={}&-(1+s^2)\big(J[\mathfrak L^{12}_{12}]+J[\mathfrak L^{13}_{13}]+J[\mathfrak L^{14}_{14}]\big)+\kappa_1\big(J[\mathfrak L^{23}_{14}]-J[\mathfrak L^{24}_{13}]+J[\mathfrak L^{34}_{12}]\big)\\
&+\tfrac{(s+\sigma)^2}{c}J[\mathfrak B^{234}_1]-c\big(J[\mathfrak B^{134}_2]-J[\mathfrak B^{124}_3]+J[\mathfrak B^{123}_4]\big)\\
&+c\,J[\mathfrak C^1_{234}]-\tfrac{(s+\sigma)^2}{c}\big(J[\mathfrak C^2_{134}]-J[\mathfrak C^3_{124}]+J[\mathfrak C^4_{123}]\big)+sc\big(\mathfrak z^{23}_{14}-\mathfrak z^{24}_{13}+\mathfrak z^{34}_{12}\big),
\end{aligned}\tag{4.1}$$
where $J[\cdot]$ denotes the defining current of each null Lagrangian (e.g. $J[\mathfrak L^{ij}_{mn}]=\langle\phi_m,D_j\phi_n\rangle e_i-\langle\phi_m,D_i\phi_n\rangle e_j$). This is Table 1 in closed form. Then:
1. For all $C^2$ fields, $\Theta_s-\partial_iJ_s^i=\sum_k\langle\mathcal E_k,L_k\rangle$ for suitable $L_k$ linear in the basic quantities. In particular $\Theta_s=\partial_iJ^i_s$ pointwise on every $C^2$ solution of ${\rm KW}_t$.
2. On every $C^2$ solution, for $a=2,3,4$,
$$J^a_s=(s+\sigma)\langle\phi_1,\mathfrak f_a\rangle+(1-s\sigma)\langle\phi_1,\mathfrak g_a\rangle+c\sum_{b,e\in\{2,3,4\}}\varepsilon_{abe}\langle\phi_e,\mathfrak f_b\rangle .\tag{4.2}$$
3. The current is unique in the following sense: among all combinations of the 128 currents $J[\mathfrak L],J[\mathfrak B],J[\mathfrak C],\mathfrak z$ satisfying 1 and 2, only (4.1) qualifies, as an element of $\mathbb Q(t,s)^{128}$.

*Proof.* By Lemma 2.4, item 1 is equivalent to the vanishing of $\Theta_s-\partial_iJ^i_s$ on $\mathcal S_t$. Item 2 is the equality of two bilinear expressions on $\mathcal S_t$. We solve the combined linear system for the 128 coefficients exactly over the field $\mathbb Q(t,s)$. The solution is unique and equals (4.1) (verify.py 3.1–3.2). Its coefficients have denominators that are powers of $t$ and $t^2+1$ only, so the resulting polynomial identity specialises to every $t>0$ and every $s$. As an independent check we compute, in jets and at $(t,s)=(2,\frac34)$ and $(\frac13,2)$, the divergence of (4.1). It has no second-order terms. After imposing ${\rm KW}_t$ on the first-order jet, $\Theta_s-\partial_iJ^i_s$ and $J^a_s-(4.2)$ vanish identically, including the terms with $A\ne0$ at the point (verify.py 3.3). On a $C^2$ solution the $\mathcal E_k$ vanish identically, hence so do the right-hand sides. $\square$

**Structure.** $\Theta_s=|u_{e_1,se_1}|^2$, where for $v,w\in\mathbb R^4$
$$u_{v,w}:=\big(\iota_vF+D(w\cdot\phi),\ D_v\phi-[w\cdot\phi,\phi]\big)$$
is the infinitesimal action of translation by $v$ combined with the gauge transformation with parameter $-w\cdot\phi$. Indeed the $A_1$-slot contributes $|sD_1\phi_1|^2$, which gives the coefficient $1+s^2$. Expanding, $\Theta_s=E_{11}+2sX_{11}+s^2B_{11}$ (verify.py 3.4), where
$$E_{ij}=\sum_k\langle F_{ik},F_{jk}\rangle+\sum_m\langle D_i\phi_m,D_j\phi_m\rangle,\quad X_{im}=\sum_k\langle F_{ik},D_k\phi_m\rangle-\sum_n\langle D_i\phi_n,[\phi_m,\phi_n]\rangle,\quad B_{mn}=\sum_i\langle D_i\phi_m,D_i\phi_n\rangle+\sum_k\langle[\phi_k,\phi_m],[\phi_k,\phi_n]\rangle .$$

**Theorem A′.** For every $t>0$, each of the 36 densities $E_{ij}$, $X_{im}$, $B_{mn}$, and the energy density $I$, equals on $\mathcal S_t$ a combination of the 68 gauge-invariant null Lagrangians. Consequently $|u_{v,w}|^2=\sum v_iv_jE_{ij}+2\sum v_iw_mX_{im}+\sum w_mw_nB_{mn}$ is, modulo ${\rm KW}_t$, the divergence of a gauge-invariant current, for all $v,w$.

*Proof.* Exact computation over $\mathbb Q(t)$. In each case the combination found has coefficients whose denominators involve only $t$ and $t^2+1$, so it specialises to every $t>0$ (verify.py 3.5). $\square$

*Remarks.* (1) On genuine smooth solutions, $B_{mn}$ and $X_{im}$ are divergences for a transparent reason. The energy identity $|{\rm KW}_t|^2_w=I+\kappa(t)P+{\rm div}$ [W2, (2.9)] shows that ${\rm KW}_t$ solutions satisfy the Euler–Lagrange equations of $I$. Then $B_{mn}=\frac12\partial_i\big(\langle\phi_m,D_i\phi_n\rangle+\langle\phi_n,D_i\phi_m\rangle\big)$ and $X_{im}=\partial_k\langle\phi_m,F_{ik}\rangle$ on solutions. The content of Theorem A′ is that this already holds at the level of first-order data, and that $E_{ij}$ (equivalently, the Yang–Mills–Higgs stress tensor $E_{ij}-\frac12\delta_{ij}I$) is also a divergence on solutions. (2) Theorem A is the twisted, $t$-dependent counterpart of the "$x_1$-part" of the Mazzeo–Witten identity; it involves no Pontryagin term.

### 4.2 Theorem B: the $\phi_y$ sector

**Theorem B.** For every $t>0$, the density $B_4:=B_{44}=\sum_i|D_i\phi_4|^2+\sum_k|[\phi_k,\phi_4]|^2$ satisfies $B_4-\partial_iJ^i_B\in\sum_k\langle\mathcal E_k,\cdot\rangle$ with
$$\begin{aligned}
J_B={}&\tfrac\sigma c\big(J[\mathfrak L^{12}_{34}]-J[\mathfrak L^{13}_{24}]+J[\mathfrak L^{23}_{14}]\big)-\big(J[\mathfrak L^{14}_{14}]+J[\mathfrak L^{24}_{24}]+J[\mathfrak L^{34}_{34}]\big)-\tfrac1cJ[\mathfrak B^{123}_4]\\
&+\tfrac1c\big(J[\mathfrak C^1_{234}]-J[\mathfrak C^2_{134}]+J[\mathfrak C^3_{124}]\big)-\tfrac\sigma c\big(\mathfrak z^{12}_{34}-\mathfrak z^{13}_{24}+\mathfrak z^{23}_{14}\big)+\mathfrak z^{14}_{14}+\mathfrak z^{24}_{24}+\mathfrak z^{34}_{34}
\end{aligned}$$
(Table 2), and on solutions $J^a_B=\langle\phi_4,D_a\phi_4\rangle$ for $a=2,3,4$. The coefficients are unique in the sense of Theorem A(3).

*Proof.* As for Theorem A; the denominators are powers of $c$ (verify.py 4.1). $\square$

### 4.3 Positivity

**Corollary 4.2.** In terms of the defects, $\Theta_s+B_4=\mathfrak d^{\,T}G(s)\,\mathfrak d$. Here $G(s)$ is the identity except that the coefficient of $|\mathfrak g_1|^2$ is $1+s^2$, and the block on $(\mathfrak g_4,\mathfrak k_1)$ is $\begin{pmatrix}2&s\\ s&1+s^2\end{pmatrix}$ (this uses $D_1\phi_4=\mathfrak g_4+s\mathfrak k_1$). The eigenvalues of $G(s)$ are $1$ (eleven times), $1+s^2$ and $2+s^2$. Hence
$$\Theta_s+B_4\ \ge\ \delta_s^2\qquad\text{for all }t>0,\ s\in\mathbb R .\tag{4.3}$$
In particular, for every $(t,s)$ there is an admissible identity (2.2) with $\kappa=0$ whose restricted form $Q_S=G(s)$ is positive definite. So the blindness seen with the sign-flipped list (Proposition 4.4(4)) does not occur for the defects that vanish on $s$-reduced configurations.

*Proof.* The decomposition is an identity of densities (verify.py 4.2). The characteristic polynomial is computed exactly (4.3). Theorems A and B give the identity, with $Q:=G(s)$ on the defects and $L_k$ from Lemma 2.4. $\square$

### 4.4 The invariant structure of the admissible class

**Proposition 4.4.** In the restricted formulation of §2:
1. Over the field $\mathbb Q(t,s)$, the linear map has rank 143 on 160 unknowns. The space of admissible identities has dimension 17, and the restricted forms $Q_S$ span a 10-dimensional subspace of ${\rm Sym}^2(\mathbb R^{13})$.
2. At the five test points $(t,s)=(2,\frac34),(3,\frac43),(\frac12,-\frac34),(1,\frac12),(2,\frac12)$, and at $s=0$ for $t=1,2$, the dimension is also 17 with a 10-dimensional span. On the nine curves $s=\pm\sigma$, $s=\pm1/\sigma$, $s=\frac{1-t}{1+t}$, $s=\frac{t+1}{t-1}$, $t=1$, $t=2$ and the Gaiotto–Witten cubic, it is 17 over the function field of the curve. In a jet parametrisation the same spaces have dimension $17+60=77$, the 60 being divergence-free currents. At $s=0$ the twenty quantities $(R,\mathfrak d)$ together with the eight complementary coordinates of that parametrisation span only 25 of the 28 basic quantities, which explains the values 92 and 94 found there.
3. The set of $(t,s)$ with $t>0$ where the dimension exceeds 17 is finite (possibly empty). Proof: Gaussian elimination with pivots that do not vanish for $t>0$ leaves a $114\times25$ matrix of generic rank 8. Three random $8\times8$ compressions of it have determinants whose greatest common divisor is $t^5$.
4. With the sign-flipped list $F_{1a}-sD_a\phi_1$ the dimension is 8 at these five points, i.e. $8+60=68$ in jets, and the $x_1$-rows vanish (negative control).
5. The Pontryagin density is, on $\mathcal S_t$, a combination of the 68 gauge-invariant null Lagrangians, with coefficients whose denominators involve only $t$ and $t^2+1$; so this holds for every $t>0$. Hence $\kappa$ can always be taken to be $0$. Over $\mathbb Q(t)$ the space of all restricted null Lagrangians has dimension 62.

*Proof.* Items 1, 2, 4 and 5: verify.py 2.4–2.8 and 1.4–1.6. Item 3 is a longer computation (about 20 minutes), run by `verify.py --locus` (outputs in `verify_output_locus.txt`). Item 2 for the nine curves: verify.py 2.9. $\square$

## 5. Reduction and uniqueness theorems

Let $M_\ell=S^1_\ell\times\mathbb R^3_+$ with $x_1\in\mathbb R/\ell\mathbb Z$ and $X=(x_2,x_3,y)$, and put $U_n=\{X:\ y>1/n,\ |X|<n\}$.

**Theorem E (twisted reduction).** Let $t>0$, $s\in\mathbb R$, and let $(A,\phi)$ be a smooth solution of ${\rm KW}_t$ on $S^1_\ell\times\{y>0\}$, with $G=SU(2)$ or $SO(3)$. Assume
$$({\rm H}_s)\qquad \liminf_{n\to\infty}\int_{S^1_\ell\times\partial U_n}|\phi|\,\delta_s\,d\sigma=0,\qquad |\phi|^2:=\textstyle\sum_m|\phi_m|^2 .$$
Then all thirteen twisted defects vanish identically. If moreover $\phi_1,\phi_2,\phi_3$ generate $\mathfrak{su}(2)$ at one point, then $\phi_4\equiv0$, and there is a smooth $SO(3)$ gauge transformation $g$, periodic in $x_1$, such that $g\cdot(A,\phi)$ is $s$-reduced. It then solves the twisted extended Bogomolny equations of Proposition 3.4; for $s=-\sigma$, $R_{-\alpha}g\cdot(A,\phi)$ solves the extended Bogomolny equations.

*Proof.* By Theorems A and B, $\Theta_s+B_4=\partial_i(J_s+J_B)^i$ on the solution. The boundary $\partial(S^1_\ell\times U_n)=S^1_\ell\times\partial U_n$ has normal in the $X$-directions, so only $J^2,J^3,J^4$ enter. By (4.2) and $|\langle u,v\rangle|\le|u||v|$,
$$|(J_s+J_B)\cdot\nu|\le\sqrt3\,C_{t,s}\,|\phi|\,\delta_s,\qquad C_{t,s}=|s+\sigma|+|1-s\sigma|+2c+1 .$$
With (4.3),
$$\int_{S^1_\ell\times U_n}\delta_s^2\ \le\ \sqrt3\,C_{t,s}\int_{S^1_\ell\times\partial U_n}|\phi|\,\delta_s .$$
The left side increases with $n$ and the right side has $\liminf$ zero, so $\delta_s\equiv0$.
Now $\mathfrak h=\mathfrak k=0$ and $\mathfrak g_4=0$ give $D_i\phi_4=0$ and $[\phi_a,\phi_4]=0$, so $|\phi_4|$ is constant. At the point where $\phi_1,\phi_2,\phi_3$ generate, $\phi_4=0$; hence $\phi_4\equiv0$.
By Lemma 2.2, $F^{\tilde A}_{1a}=0$ and $D^{\tilde A}_1\phi_m=0$ for $\tilde A=A-s\phi_1dx_1$. Let $h(x_1,X)$ be the $\tilde A$-parallel transport along the circle from $(0,X)$ to $(x_1,X)$, and $H(X)=h(\ell,X)$. Since $F^{\tilde A}_{1a}=0$, the connection $\tilde A$ is flat on each cylinder $S^1\times\gamma$, so $H(X')=\tau_\gamma H(X)\tau_\gamma^{-1}$. Since $D^{\tilde A}_1\phi_m=0$, ${\rm Ad}(H(X))$ fixes $\phi_m(0,X)$. At the generating point $H=\pm1$; being central, $H\equiv\pm1$ on the connected set $\mathbb R^3_+$. The gauge transformation defined by $h$ is periodic in $SO(3)$ and makes $\tilde A_1=0$. In that gauge $\partial_1\tilde A_a=F^{\tilde A}_{1a}=0$ and $\partial_1\phi_m=0$, so the fields are $x_1$-independent and $A_1=s\phi_1$. The remaining statements are Proposition 3.4 and Corollary 3.3. $\square$

As in the untwisted case, $({\rm H}_s)$ holds if $|\phi|\,\delta_s\le C y^{\gamma}(1+|X|)^{-2-2\gamma}$ for some $C,\gamma>0$. The flat piece contributes $O(n^{-\gamma})$ and the spherical piece $O(n^{-\gamma})$. All quantities in $({\rm H}_s)$ are gauge invariant. By Corollary 3.3, the explicit twisted knots $R_\alpha x^{(k)}$ have $\delta_{-\sigma}\equiv0$.

For a twist vector $\vec s=(s_1,s_2,s_3)$ and $a\in\{1,2,3\}$, let $\delta^{(a)}$ be the defect norm of Definition 2.1 for the direction $x_a$ and twist $s_a$, i.e. after the cyclic relabelling $(1,2,3)\to(a,a+1,a+2)$ of the boundary coordinates and of $\phi_1,\phi_2,\phi_3,A_1,A_2,A_3$. This relabelling preserves orientation and ${\rm KW}_t$, so Theorems A and B hold for each direction.

**Theorem F (twisted Nahm poles on $T^3\times\mathbb R_+$).** Let $t>0$, $|\alpha_a|<\frac\pi2$ and $s_a=\tan\alpha_a$. Let $(A,\phi)$ be a smooth ${\rm KW}_t$ solution on $T^3_\ell\times(0,\infty)$, $T^3_\ell=(\mathbb R/\ell\mathbb Z)^3$, such that:
- (H) for each $a$, $\liminf_{(\varepsilon,L)\to(0,\infty)}\Big(\int_{T^3\times\{\varepsilon\}}|\phi|\,\delta^{(a)}+\int_{T^3\times\{L\}}|\phi|\,\delta^{(a)}\Big)=0$;
- (G) $\phi_1,\phi_2,\phi_3$ generate $\mathfrak{su}(2)$ at some point;
- (D) $\sup_{T^3\times\{y\}}|\phi|\to0$ as $y\to\infty$;
- (P) $\sup_{T^3\times\{y\}}|\phi|$ is unbounded as $y\to0$.

Then $\sin(\alpha_1+\alpha_2+\alpha_3+\alpha)=0$, and $(A,\phi)$ is gauge equivalent to the twisted Nahm pole $N_{\alpha'}$ with $\alpha'_a\equiv\alpha_a\pmod\pi$ and $\sum\alpha'_a\equiv-\alpha\pmod{2\pi}$. In other words, it is gauge equivalent to $\phi_a=\pm\cos\alpha_a\,t_a/y$, $A_a=s_a\phi_a$, with the sign $+$ if $\sum\alpha_a=-\alpha$.

*Proof.* (1) *Reduction.* On $T^3\times(\varepsilon,L)$ only $J^4$ enters, so as in Theorem E (with (H) in place of $({\rm H}_s)$) all defects $\delta^{(a)}$ vanish, and $\phi_4\equiv0$ by (G). Put $\mathbb A:=A-\sum_as_a\phi_a\,dx_a$. The direction-$a$ defects give $F_{aj}+s_aD_j\phi_a=0$ for $j\ne a$ and $D_a\phi_m=s_a[\phi_a,\phi_m]$ for all $m$. Hence $F^{\mathbb A}_{ab}=F_{ab}-s_bD_a\phi_b+s_aD_b\phi_a+s_as_b[\phi_a,\phi_b]=0$, $F^{\mathbb A}_{a4}=F_{a4}+s_aD_4\phi_a=0$, and $D^{\mathbb A}_a\phi_m=0$. So $\mathbb A$ is flat, and $\phi$ is $\mathbb A$-parallel along $T^3$. The holonomies of $\mathbb A$ around $T^3$ commute and fix $\phi_1,\phi_2,\phi_3$ at the generating point, so they are central and trivial in $SO(3)$. Thus $\mathbb A$ is gauge equivalent to $0$ by a periodic $SO(3)$ gauge transformation. In that gauge $A_a=s_a\phi_a$, $A_4=0$, and $\phi$ depends on $y$ only.
(2) *The ODE.* For such fields, ${\rm KW}_t$ reduces to (cyclic $a,b,c$)
$$\mathcal E_{a4}=-(s_a+\sigma)\phi_a'+c(s_b+s_c)[\phi_b,\phi_c],\qquad \mathcal E_{bc}=\big(s_bs_c-1+\sigma(s_b+s_c)\big)[\phi_b,\phi_c]-c\,\phi_a',$$
and $\mathcal W=0$ identically (verify.py 7.2). The determinant of this pair (in the unknowns $\phi_a'$, $[\phi_b,\phi_c]$) is $\sin(\alpha_1+\alpha_2+\alpha_3+\alpha)/(\cos\alpha_1\cos\alpha_2\cos\alpha_3\cos\alpha)$, the same for every $a$ (verify.py 7.3). If it is non-zero, then $[\phi_b,\phi_c]=0$ and $\phi_a'=0$ for all $a$, which contradicts (G). If $\sum\alpha_a=-\alpha$, then $\phi_a'=-\frac{\cos\alpha_a}{\cos\alpha_b\cos\alpha_c}[\phi_b,\phi_c]$ (verify.py 7.4), so $T_a:=\phi_a/\cos\alpha_a$ solves $T_a'=-[T_b,T_c]$. If $\sum\alpha_a=-\alpha\pm\pi$, the same computation gives $T_a'=+[T_b,T_c]$; we replace $T$ by $-T$ and proceed in the same way.
(3) *Nahm's equation.* For $T_a'=-[T_b,T_c]$, the Gram matrix $G_{ab}=\langle T_a,T_b\rangle$ satisfies $G_{ab}'=0$ for $a\ne b$ and $G_{aa}'=-2\langle T_1,[T_2,T_3]\rangle$ for all $a$. So its trace-free part is constant, and by (D) it is zero. Thus $T_a=L\,e_a$ with $(e_a)$ orthonormal in $(\mathbb R^3,\cdot)$ and $L\ge0$ the common Euclidean length. If $L(y_0)=0$ then $T\equiv0$ by uniqueness for the ODE, which contradicts (G). So $L>0$ and $[e_2,e_3]=\epsilon e_1$ with constant $\epsilon=\pm1$. Then $L'e_1+Le_1'=-\epsilon L^2e_1$ and $e_1'\perp e_1$ give $e_a'=0$ and $L'=-\epsilon L^2$. A positive solution on $(0,\infty)$ forces $\epsilon=1$ and $L=1/(y+y_0)$ with $y_0\ge0$, and (P) gives $y_0=0$. A constant gauge rotation takes $(e_a)$ to $(t_a)$. $\square$

*Remarks.* (i) $N_{\alpha}$ itself has all $\delta^{(a)}\equiv0$, so it satisfies (H). (ii) Hypothesis (H) at the face asks the defects to vanish faster than $y$ in $L^1(T^3)$. For solutions that are polyhomogeneous perturbations of $N_\alpha$, this would follow from a lower bound on the first indicial root, *or* from a cancellation of the part of $J^4$ that is linear in the perturbation. The indicial roots of the tilted Nahm pole are independent of the tilt angle [Bl2, Prop. 7.4]. We do not carry this out here; it is the twisted analogue of what is needed at $t=1$.

## 6. Status of claims

**Proved here (exact, all parameters).** Lemma 2.2, Lemma 2.3, Lemma 2.4, Proposition 3.1, Lemma 3.2, Corollary 3.3 (for $k=1$ by computation, and for all $k$ given [W1, R40]), Proposition 3.4, Theorem A, Theorem A′, Theorem B, Corollary 4.2, Proposition 4.4(1), (2), (4), (5), and Theorems E and F. Proposition 4.4(3) is proved by the optional computation (`--locus`).

**Remark (sign and tilt).** With the sign-flipped defects $F_{1a}-sD_a\phi_1$, which do not vanish on $s$-reduced configurations, the class is blind to the $x_1$-defects (Proposition 4.4(4)); with the defects of Lemma 2.2 the opposite holds (Corollary 4.2). The points $s=\sigma$ belong to the tilt $(\alpha,-\alpha,-\alpha)$, not to the Gaiotto–Witten/Dimakis tilt; there the complex structure of Proposition 3.4 with $\alpha_1=\alpha$ applies.

**Credited.** The strategy and (2.17): [W2]. The $t=1$ identity: [MW2]. The family (2.9): [W2]. The twisted reduction and the tilted Nahm pole: [GW, §3.1]; see also [Bl2, §7]. The twisted model knots: [Di2]. Witten's knots: [W1], in the form of [R40].

**Not claimed.** That solutions with twisted boundary conditions satisfy $({\rm H}_s)$ or (H). Uniqueness for the three-dimensional twisted equations. Results on $\mathbb R\times\mathbb R^3_+$, for compact or curved knots, or for other gauge groups. The exact exceptional set in Proposition 4.4(3).

## 7. Verification

`verify.py` (Python 3, SymPy; about 3 minutes by default; 36 checks) prints PASS or FAIL for each check and a final count; its output is in `verify_output.txt`. Two independent formalisms are used. *Jets* are polynomials in $A,\partial A,\partial^2A,\phi,\partial\phi,\partial^2\phi$ at a point. *Covariant quantities* are abstract monomials in $F$, $D\phi$, $[\phi,\phi]$, with quartic terms reduced through the Gram matrix. The parts are:
1. the defects; the negative-control numbers (68, 77, 92, 94) in jets; the Nahm pole $I=3/y^4$;
2. null Lagrangians; the restricted formulation; the dimensions 17 and 10 over $\mathbb Q(t,s)$, at points and on curves;
3. Theorem A over $\mathbb Q(t,s)$, the coefficients of Table 1, the jet cross-check, Theorem A′;
4. Theorem B and the positivity (4.3);
5. twisted Nahm poles, the Gaiotto–Witten/Dimakis cubic, the rotation lemma, and the explicit twisted knot;
6. Theorems A and B on explicit solutions: on every twisted Nahm pole and on the twisted knot, for symbolic twist $s$, $\Theta_s=\partial_aJ^a$ with $J^a$ given by (4.2);
7. Proposition 3.4 and the ODE of Theorem F.

`verify.py --locus` also runs the computation of Proposition 4.4(3).

**Table 1** (coefficients $x_j$ of Theorem A, $\kappa_1=((s^2-1)\sigma-2s)/c$):

| element | coefficient | element | coefficient |
|---|---|---|---|
| $\mathfrak L^{12}_{12},\mathfrak L^{13}_{13},\mathfrak L^{14}_{14}$ | $-(1+s^2)$ | $\mathfrak B^{234}_1$ | $(s+\sigma)^2/c$ |
| $\mathfrak L^{23}_{14},\ \mathfrak L^{34}_{12}$ | $\kappa_1$ | $\mathfrak B^{134}_2,\ \mathfrak B^{123}_4$ | $-c$ |
| $\mathfrak L^{24}_{13}$ | $-\kappa_1$ | $\mathfrak B^{124}_3$ | $c$ |
| $\mathfrak C^1_{234}$ | $c$ | $\mathfrak C^2_{134},\ \mathfrak C^4_{123}$ | $-(s+\sigma)^2/c$ |
| $\mathfrak C^3_{124}$ | $(s+\sigma)^2/c$ | $\mathfrak z^{23}_{14},\ \mathfrak z^{34}_{12}$; $\mathfrak z^{24}_{13}$ | $sc$; $-sc$ |

**Table 2** (Theorem B): $\mathfrak L^{12}_{34},\mathfrak L^{23}_{14}$: $\sigma/c$; $\mathfrak L^{13}_{24}$: $-\sigma/c$; $\mathfrak L^{14}_{14},\mathfrak L^{24}_{24},\mathfrak L^{34}_{34}$: $-1$; $\mathfrak B^{123}_4$: $-1/c$; $\mathfrak C^1_{234},\mathfrak C^3_{124}$: $1/c$; $\mathfrak C^2_{134}$: $-1/c$; $\mathfrak z^{12}_{34},\mathfrak z^{23}_{14}$: $-\sigma/c$; $\mathfrak z^{13}_{24}$: $\sigma/c$; $\mathfrak z^{14}_{14},\mathfrak z^{24}_{24},\mathfrak z^{34}_{34}$: $1$.

## References

- [Bl1] M. Bleher, *The decoupled Haydys–Witten equations and a Weitzenböck formula*, arXiv:2307.15056 (Lemma 2.2, Theorem A).
- [Bl2] M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, SIGMA 22 (2026) 028, arXiv:2412.13285 (§§5.4, 7.1–7.4).
- [Di1] P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: nilpotent Higgs field*, arXiv:2209.11101.
- [Di2] P. Dimakis, *Model knot solutions for the twisted Bogomolny equations*, arXiv:2204.06617 (§2, (2.1)–(2.4)).
- [GU] M. Gagliardo, K. Uhlenbeck, *Geometric aspects of the Kapustin–Witten equations*, arXiv:1401.7366.
- [GW] D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012) 935–1086, arXiv:1106.4789 (§3.1).
- [HM3] S. He, R. Mazzeo, *Opers and the twisted Bogomolny equations*, arXiv:1902.11183.
- [KW] A. Kapustin, E. Witten, *Electric-magnetic duality and the geometric Langlands program*, Commun. Number Theory Phys. 1 (2007) 1–236, arXiv:hep-th/0604151.
- [MW1] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014), arXiv:1311.3167.
- [MW2] R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Anal. Geom. 28 (2020), arXiv:1712.00835 (§5 and footnote 1).
- [W1] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012) 1–137, arXiv:1101.3216.
- [W2] E. Witten, *Two lectures on gauge theory and Khovanov homology*, arXiv:1603.03854 (Lecture Two, (2.7)–(2.17)).
- [R22] rStation math_22 v1, *Genuine Kapustin–Witten knot solutions with equal boundary data on $S^1\times\Sigma\times\mathbb R^+$, and the absence of circle-invariant Haydys–Witten trajectories between them*, https://rstation.ai/problems/math/papers/22/v1.
- [R40] rStation math_40 v1, *Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class*, https://rstation.ai/problems/math/papers/40/v1 (§1.1).

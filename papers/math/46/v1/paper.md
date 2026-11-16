# The complete isotropic Haydys–Witten flow category on $\mathbb R\times S^3\times I$ at the Anderson–Henningson fold: global uniqueness of the tunnelling instanton, compactness, and a contractible Cohen–Jones–Segal realization

**Abstract.**

We study the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends, in the isotropic sector of fields invariant under $SU(2)_L\times SO(3)_{\rm diag}$. There the equations reduce to $\partial_su+i\partial_yu=\bar u^2-r^{-2}$, and gauge classes are configurations. By Henningson and Anderson–Henningson, Kapustin–Witten (KW) solutions exist only for $L\ge\pi r$: one at the fold $L=\pi r$, and two, $k_\pm$, for $L>\pi r$. An earlier rStation paper proved that the tunnelling instanton $\mathfrak u:k_+\to k_-$ exists and is unique near the fold. We prove global statements.

(A) For every $L>\pi r$, every isotropic HW trajectory in the natural class is either constant or runs from $k_+$ to $k_-$. Its energy is exactly $6\pi^2r^3L^{-2}\Delta\mathcal A$, where $\Delta\mathcal A$ is the action gap. With $\nu=L^2/r^2-\pi^2$ we show $d\Delta\mathcal A/d\nu=2\int p_+>0$, so $\Delta\mathcal A>0$ for all $L>\pi r$.

(B) Universal a priori estimates hold. Every trajectory satisfies $|u|^2\le\frac32(y^{-2}+(L-y)^{-2})+r^{-2}$. A boundary blow-up argument shows that the Nahm pole is uniform: $|{\rm Re}\,u|\le Cy^{3/2}$ and $|{\rm Im}\,u+1/y|\le Cy$, where $C$ depends only on $r$, $L$ and an energy bound.

(C) Hence, for every $L>\pi r$, the trajectories $k_+\to k_-$ modulo translation form a compact space: no bubbling, breaking or loss of energy at the poles.

(D) For $\pi r<L<\pi r+\delta$, $\mathfrak u$ is globally the only nonconstant isotropic trajectory.

So, near the fold, the complete isotropic flow category has two objects and one transversally cut out morphism. Its Cohen–Jones–Segal realization is contractible for either framing, as is that of the empty category for $L<\pi r$. In the isotropic sector the Anderson–Henningson pair cancels. In the full theory it does not: there the local homotopy type is $S^1\vee S^4$.

verify.py: 60 checks, FALLOS = 0.

---

## 1. Introduction and results

### 1.1 Background and goal

A long-term goal is a Haydys–Witten flow category whose objects are Kapustin–Witten (KW) solutions and whose morphisms are HW instantons, together with its Cohen–Jones–Segal (CJS) realization [CJS, LS]. Building it requires six steps: classification of objects (S1), transversality (S2), compactness (S3), gluing (S4), framings (S5) and realization (S6). The Anderson–Henningson (AH) geometry $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends [He, AH] is the simplest test case. Our accepted papers treated it *locally*, in a small neighbourhood of the degenerate KW solution at the fold $L=\pi r$:

* existence, local uniqueness and isotropic transversality of the AH instanton [R24];
* the complete gauge-fixed linearization, with index $-3$ [R30];
* the five-dimensional centre manifold and the three-sphere of non-isotropic KW solutions below the fold [R31];
* symmetry breaking and a local flow category [R32];
* a smooth framed model with realization $\Sigma^\infty(S^1\vee S^4)$ [R33];
* isolation and local Gromov–Floer compactness [R34].

Every one of these results concerns solutions that stay in a fixed small neighbourhood. None excludes HW trajectories that leave it, nor KW solutions far from the fold. So none of them is a *complete* flow category.

This paper gives the first complete one, in the isotropic sector. We classify all objects for all $L$. We classify all morphisms for $L$ near the fold. For all $L$, we exclude every trajectory except those from $k_+$ to $k_-$, and we prove that these form a compact space. The new analytic input is a set of universal a priori estimates for the two-dimensional reduced equation with its singular boundary condition (Theorem B). It consists of a Keller–Osserman barrier, a boundary blow-up classification, and linear barriers in the pole layer. These estimates are what local methods could not provide (compare [R34, Remark 3.3]).

### 1.2 Setting

**The isotropic sector.** On $S^3_r$ take a left-invariant orthonormal coframe $\sigma^i$ with $d\sigma^i=-\frac2r\,\sigma^j\wedge\sigma^k$, and fix $T_i\in\mathfrak{su}(2)$ with $[T_i,T_j]=\epsilon_{ijk}T_k$. *Isotropic* fields are those invariant under left translations and under the diagonal $SO(3)$ (right translations combined with constant gauge rotations). They have the form
$$A=a\,T_i\sigma^i,\qquad\varphi=b\,T_i\sigma^i,\qquad A_s=A_y=0,$$
with real $a,b$ depending on $(s,y)$. By [R24, Thm. A] (see also [He, AH]), the HW equations for such fields are equivalent to
$$\partial_su+i\partial_yu=\bar u^2-\epsilon,\qquad u=\tfrac1r-a-ib=p+iq,\qquad\epsilon=r^{-2}. \tag{1.1}$$
The Nahm pole at $y=0$ is $u\sim-i/y$, and at $y=L$ it is $u\sim-i/(y-L)$ [R24, §§2–3]. The *energy* of a solution is $E=\int|\partial_sA|^2+|\partial_s\varphi|^2$. The scaling $(s,y,u)\mapsto(s/r,y/r,ru)$ reduces everything to $r=1$, and **from now on $r=1$, $\epsilon=1$**, except in the statements of the theorems. The fold is then at $L=\pi$. Put
$$\nu:=L^2/r^2-\pi^2 .$$

**Rescaled form [R24, §5].** Put $\tau=y/L$, $\varsigma=s/L$, $v=Lu$, $v_0(\tau)=-i\pi\cot(\pi\tau)$ (the fold solution) and $w=v-v_0$. Then (1.1) becomes
$$\partial_\varsigma w=\mathcal G_\nu(w):=\mathcal Lw+\bar w^2-\nu,\qquad \mathcal Lw=-i\,\partial_\tau w+2\bar v_0\bar w, \tag{1.2}$$
on $X=L^2((0,1);\mathbb C)$, with the real inner product $\langle f,g\rangle={\rm Re}\int_0^1\bar fg$. Let $Z=D(\mathcal L)$ carry the graph norm. In these variables $E=6\pi^2r^3L^{-2}\iint|\partial_\varsigma w|^2\,d\tau\,d\varsigma$ [R24, Thm. C(5)].

**Imported facts** (all from [R24]):

* **(F1)** $\mathcal L$ is self-adjoint on its maximal domain $Z$, with compact resolvent; $Z\hookrightarrow C^0[0,1]$ compactly, and $|w(\tau)|\le C_Z\|w\|_Z\min(\tau,1-\tau)^{1/2}$; $\ker\mathcal L=\mathbb R\zeta$ with $\zeta=\sin^2\pi\tau$ [R24, Lemma 5.1].
* **(F2)** Static classification [R24, Prop. B], due to [He, AH]. Genuine KW solutions exist iff $\nu\ge0$. At $\nu=0$ the only one is $k_0$ ($w=0$). For $\nu>0$ there are exactly two, $k_\pm$, with conserved quantity $H={\rm Re}(u^3/3-u)=\mp h(L)$, $h>0$. Both are nondegenerate in the isotropic class, and $k_-=\tilde\sigma k_+$ with $\tilde\sigma(p,q)(s,y)=(-p,q)(-s,y)$.
* **(F3)** The centre-manifold reduction [R24, Prop. 5.3, Lemma 5.4]. In the shifted variable $\tilde w=w-\nu\psi_1$, $\psi_1=\frac i{6\pi}\sin2\pi\tau$, the static solutions near $0$ are $\tilde w_\pm=x_\pm\zeta+\tilde\Psi(x_\pm,\nu)$, with $x_\pm=\pm\sqrt{8\nu/5}(1+O(\sqrt\nu))$ and $\tilde\Psi=O(x^2+\nu^2)$ in $Z$.
* **(F4)** [R24, Thm. C]. For $0<\nu<\nu_2$ there is a solution $\mathfrak u$ of (1.2) with $\mathfrak u\in C^k(\mathbb R;Z)$, converging exponentially in $Z$ to $k_+$ as $\varsigma\to-\infty$ and to $k_-$ as $\varsigma\to+\infty$. There is a neighbourhood $\mathcal U$ of $0$ in $Z$ such that, up to translation, $\mathfrak u$ is the unique nonconstant solution with $\tilde w(\varsigma)\in\mathcal U$ for all $\varsigma$.
* **(F5)** [R24, Thm. D]. The linearization of the isotropic HW system along $\mathfrak u$ is Fredholm of index $1$ and onto, with kernel $\mathbb R\partial_\varsigma\mathfrak u$.

**The trajectory class.** An *isotropic HW trajectory at length $L$* is a map
$$w\in C^0(\mathbb R;Z)\cap C^1(\mathbb R;X)$$
that satisfies (1.2) for every $\varsigma$ and has limits $w_{\pm\infty}=\lim_{\varsigma\to\pm\infty}w(\varsigma)$ in $Z$. We write $\mathcal T_L$ for the set of these trajectories. Constant trajectories are KW solutions. By (F4), $\mathfrak u\in\mathcal T_L$. The class is the isotropic version of the class $W_{\rm loc}$ of [R34, §1.2]. Membership in $Z$ is the $H^1_0$-type Nahm-pole condition (Lemma 2.1(b) and [R34, Lemma 2.1, Remark 3.4]); we impose nothing beyond it. In particular we assume no smallness and no energy bound.

### 1.3 Results

Write $u_\pm$, $w_\pm$ for $k_\pm$ in the two coordinate systems, and $p_\pm={\rm Re}\,u_\pm$.

**Theorem A (objects, action gap and global exclusion; all $L$).**
1. *(Objects.)* For $L<\pi r$ the isotropic sector has no KW solutions. For $L=\pi r$ it has exactly $k_0$, and for $L>\pi r$ exactly $k_+\ne k_-$ ((F2)). Distinct isotropic configurations are gauge inequivalent (Lemma 2.2).
2. *(Action gap.)* Let $\mathcal A_\nu(w)=\frac12\langle w,\mathcal Lw\rangle+\frac13{\rm Re}\int_0^1w^3-\nu\,{\rm Re}\int_0^1w$. Then (1.2) is the $X$-gradient flow of $\mathcal A_\nu$. For $\nu>0$ put $\Delta\mathcal A(\nu)=\mathcal A_\nu(w_-)-\mathcal A_\nu(w_+)$. Then
$$\Delta\mathcal A=\nu P_1+\tfrac13P_3=-2\mathcal A_\nu(w_+),\qquad \frac{d}{d\nu}\Delta\mathcal A=2P_1,\qquad P_1={\rm Re}\int_0^1w_+=\int_0^Lp_+\,dy>0,$$
where $P_3={\rm Re}\int_0^1w_+^3$. Moreover $\Delta\mathcal A(0^+)=0$. Hence $\Delta\mathcal A(\nu)>0$ for every $\nu>0$, and $\Delta\mathcal A=\frac23\sqrt{8/5}\,\nu^{3/2}(1+O(\nu^{1/2}))$.
3. *(Exclusion.)* Let $L>\pi r$ and $w\in\mathcal T_L$. Then $w_{\pm\infty}$ are KW solutions. Either $w$ is constant, or $w_{-\infty}=w_+$, $w_{+\infty}=w_-$ and
$$E(w)=6\pi^2r^3L^{-2}\,\Delta\mathcal A(\nu).$$
In particular there are no trajectories $k_-\to k_+$ and no nonconstant trajectories $k_\pm\to k_\pm$. For $L\le\pi r$ every element of $\mathcal T_L$ is constant.

**Theorem B (universal a priori estimates).** Let $u$ correspond to some $w\in\mathcal T_L$.
1. *(Keller–Osserman bound; no energy bound needed.)* $|u(s,y)|^2\le\Phi_L(y):=\frac32\big(y^{-2}+(L-y)^{-2}\big)+r^{-2}$ on $\mathbb R\times(0,L)$.
2. *(Uniform Nahm pole.)* Fix $0<L_1<L_2$ and $E_0>0$. Then there are $y_1>0$ and $C$, depending only on $r,L_1,L_2,E_0$, such that, if $L\in[L_1,L_2]$ and $\iint|\partial_su|^2\le E_0$, then for all $s$ and all $0<y\le y_1$
$$|{\rm Re}\,u(s,y)|\le Cy^{3/2},\qquad |{\rm Im}\,u(s,y)+1/y|\le Cy,$$
and symmetrically at $y=L$.
3. *(Universal $Z$-bound.)* Under the hypotheses of 2 there is $M=M(r,L_1,L_2,E_0)$ with $\sup_\varsigma\|w(\varsigma)\|_Z\le M$.

**Theorem C (global compactness; all $L>\pi r$).** Let $L>\pi r$ and let $(w_n)\subset\mathcal T_L$ be nonconstant. Then, after translations and passing to a subsequence, $w_n\to w$ in $C^0_{\rm loc}(\mathbb R;X)\cap C^0_{\rm loc}(\mathbb R;C^0[0,1])\cap L^2_{\rm loc}(\mathbb R;Z)$. The limit $w\in\mathcal T_L$ is a trajectory $k_+\to k_-$ with $E(w)=E(w_n)$. So the space $\mathcal M(k_+,k_-)=\{\text{nonconstant }w\in\mathcal T_L\}/\mathbb R$ is sequentially compact in this topology. No bubbling, breaking or loss of energy at the poles occurs.

**Theorem D (the complete isotropic flow category near the fold).** There is $\delta>0$ such that for $\pi r<L<\pi r+\delta$:
1. every $w\in\mathcal T_L$ is constant ($k_+$ or $k_-$) or a translate of the AH instanton $\mathfrak u$;
2. $\mathcal M(k_+,k_-)=\{[\mathfrak u]\}$ is one point, cut out transversally with index $1$ ((F5)), and $\mathcal M(k_-,k_+)=\emptyset$;
3. consequently the isotropic HW flow category $\mathscr C_{\rm iso}(L)$ is the following framed flow category in the sense of [LS, §3]: two objects, $\mathrm{gr}(k_+)=\mathrm{gr}(k_-)+1$, one framed point in $\mathcal M(k_+,k_-)$, and all other morphism spaces empty. It is compact and needs no gluing.

**Corollary E (CJS realization).** For $\pi r<L<\pi r+\delta$ and either framing of the point $[\mathfrak u]$, the CJS realization of $\mathscr C_{\rm iso}(L)$ is contractible:
$$|\mathscr C_{\rm iso}(L)|\simeq\Sigma^{-N}\big(S^N\cup_{\pm1}e^{N+1}\big)\simeq *.$$
Its cellular cochain complex is $\delta k_-=\pm k_+$, so the isotropic HW Floer cohomology vanishes. For $L<\pi r$ the category is empty and $|\mathscr C_{\rm iso}(L)|=*$ as well. So the realization is unchanged across the fold, as continuation invariance predicts.

**What is new.**
* Theorem A(2–3) is global in the configuration space and holds for every $L>\pi r$. The monotonicity identity $\Delta\mathcal A'=2P_1$ is an envelope argument; we found it neither in [He, AH] nor in [R24].
* Theorem B is the main analytic novelty. Part 1 is a Keller–Osserman barrier [Ke, Os] for $|u|^2$. Its coefficient $\frac32$ is the one for which $a/y^2$ solves the comparison equation $\Phi''=4\Phi^2$; the coefficient $1$ fails (verify.py §2.4). Part 2 uses a boundary blow-up argument: limits at the Nahm pole are static solutions of $f'=-i\bar f^2$ on a half-line, and we classify these completely (Lemma 4.3). This rules out the loss of the pole without any polyhomogeneity theory. Linear barriers then give the rates $y^{3/2}$ for ${\rm Re}\,u$ and $y$ for ${\rm Im}\,u+1/y$; the second is sharp, since ${\rm Im}\,u+1/y=y/3+O(y^2)$ on static solutions.
* Theorems C and D upgrade the local uniqueness of [R24] and the local compactness of [R34] to global statements in the isotropic sector.

**What is not claimed.**
* Anything outside the isotropic sector. In the full theory, the AH arrow is obstructed and the local homotopy type is $S^1\vee S^4$ [R30, R31, R33].
* Existence, uniqueness or transversality of trajectories $k_+\to k_-$ for $L\ge\pi r+\delta$. Theorem C gives compactness there, but not a count.
* An explicit $\delta$.
* That every isotropic solution with a Nahm pole in some weaker sense lies in $\mathcal T_L$.

### 1.4 Relation to the steps S1–S6

In the isotropic sector the steps S1–S6 are complete near the fold. S1 is Theorem A(1). S2 is (F5) together with Theorem D(1). S3 is Theorem C. S4 is vacuous, because there are no broken trajectories. S5 is a sign. S6 is Corollary E. The answer is the trivial spectrum. It shows that the isotropic sector alone cannot carry the nontrivial local homotopy type $S^1\vee S^4$ of [R31, R33]. That type lives on the non-isotropic three-sphere of [R31] (Remark 8.2).

## 2. Preliminaries

**Lemma 2.1 (basic properties of $\mathcal T_L$).** Let $w\in\mathcal T_L$, and let $u(s,y)=L^{-1}(v_0+w)(s/L,y/L)$.
* (a) $u$ is a smooth solution of (1.1) on $\mathbb R\times(0,L)$.
* (b) $M_w:=\sup_\varsigma\|w(\varsigma)\|_Z<\infty$. With $u_0(y)=-i\frac\pi L\cot\frac{\pi y}L$, we have $|u(s,y)-u_0(y)|\le C_ZM_wL^{-1}\min(y/L,1-y/L)^{1/2}$ for all $s$. In particular ${\rm Re}\,u\to0$, ${\rm Im}\,u+1/y\to0$ and $y^2|u|^2\to1$ as $y\to0$, uniformly in $s$, and symmetrically at $y=L$.
* (c) $w(\varsigma)\to w_{\pm\infty}$ uniformly on $[0,1]$. Hence $u(s,\cdot)\to u_{\pm\infty}$ uniformly on compact subsets of $(0,L)$ as $s\to\pm\infty$.
* (d) The reflection $R:(p,q)(s,y)\mapsto(p,-q)(s,L-y)$ and translations in $s$ map $\mathcal T_L$ to itself.

*Proof.* (a) Since $\mathcal L$ is the maximal operator (F1), (1.2) holding in $X$ for each $\varsigma$ means that $u$ solves (1.1) in the sense of distributions. On compact subsets $u$ is bounded, by $Z\hookrightarrow C^0$ and the continuity of $\varsigma\mapsto w(\varsigma)$. So $\bar\partial u=\frac12(\bar u^2-1)\in L^\infty_{\rm loc}$. The standard bootstrap for $\bar\partial$ (Lemma 4.4) gives $C^\infty$. (b) A continuous map $\mathbb R\to Z$ with limits at $\pm\infty$ is bounded. The pointwise bound is (F1). The limits use $|u_0+i/y|\le Cy$. (c) follows from $Z\hookrightarrow C^0$. (d) is checked in verify.py §1.7. $R$ fixes $v_0$ and preserves $Z$. ∎

**Lemma 2.2 (gauge classes).** Two isotropic configurations satisfying the Nahm-pole condition that are gauge equivalent are equal (up to the centre $\pm1$, which acts trivially).

*Proof.* Let $x$ be such a configuration and $g\cdot x=x'$ with $x'$ isotropic. The stabilizer of $x$ in the gauge group is $\{\pm1\}$: a stabilizing $g$ satisfies $d_Ag=0$ and $g\varphi g^{-1}=\varphi$. Since $x$ is isotropic, $\varphi=b\,T_i\sigma^i$ with $b\sim1/y\ne0$ near $y=0$. So there $g$ commutes with $T_1,T_2,T_3$, hence $g=\pm1$. A parallel section of the connected domain is determined by its value at one point. For $\gamma$ in the connected symmetry group $G=SU(2)_L\times SO(3)_{\rm diag}$ we have $(\gamma\cdot g)\cdot x=\gamma\cdot x'=x'=g\cdot x$. So $g^{-1}(\gamma\cdot g)\in\{\pm1\}$, and this element depends continuously on $\gamma$ and equals $1$ at $\gamma=1$. Hence $g$ is $G$-invariant. Invariance under $SU(2)_L$ makes $g$ independent of the point of $S^3$. Invariance under $SO(3)_{\rm diag}$ makes it commute with $SU(2)$, so $g=\pm1$. ∎

Hence, in the isotropic sector, the moduli spaces of gauge classes are the solution sets themselves. No gauge fixing or hypothesis (G) of [R34] is needed (compare [R34, Remark 8.2]).

## 3. The action and global exclusion (proof of Theorem A)

**Lemma 3.1 (gradient structure).** $\mathcal A_\nu\in C^1(Z)$, and $D\mathcal A_\nu(w)h=\langle\mathcal G_\nu(w),h\rangle$ for $w,h\in Z$.

*Proof.* The quadratic part has derivative $\langle\mathcal Lw,h\rangle$ because $\mathcal L$ is symmetric. The derivative of $\frac13{\rm Re}\int w^3$ is ${\rm Re}\int w^2h=\langle\bar w^2,h\rangle$, since $\overline{\bar w^2}=w^2$. It is continuous on $Z$ because $Z\hookrightarrow C^0$. The derivative of $-\nu{\rm Re}\int w$ is $\langle-\nu,h\rangle$. verify.py §5.1–5.3 checks the identity exactly on a four-parameter Galerkin space, with a negative control. ∎

**Lemma 3.2 (energy identity).** For $w\in\mathcal T_L$ and $a<b$,
$$\int_a^b\|\partial_\varsigma w\|_X^2\,d\varsigma=\mathcal A_\nu(w(b))-\mathcal A_\nu(w(a)).$$
Consequently $\mathcal E(w):=\int_{\mathbb R}\|\partial_\varsigma w\|^2=\mathcal A_\nu(w_{+\infty})-\mathcal A_\nu(w_{-\infty})<\infty$, and the limits $w_{\pm\infty}$ are KW solutions.

*Proof.* We show that $\varsigma\mapsto\mathcal A_\nu(w(\varsigma))$ is differentiable with derivative $\langle\mathcal G_\nu(w),\partial_\varsigma w\rangle=\|\partial_\varsigma w\|^2$.
* *Quadratic part.* By symmetry of $\mathcal L$,
$$\langle w(\varsigma+h),\mathcal Lw(\varsigma+h)\rangle-\langle w(\varsigma),\mathcal Lw(\varsigma)\rangle=\langle w(\varsigma+h)-w(\varsigma),\mathcal Lw(\varsigma+h)+\mathcal Lw(\varsigma)\rangle .$$
Divide by $h$ and use $w\in C^1(X)$ and $\mathcal Lw\in C^0(X)$.
* *Cubic part.* The difference quotient is ${\rm Re}\int\frac13(w_h^2+w_hw+w^2)\frac{w_h-w}h$, where $w_h=w(\varsigma+h)$. The first factor converges in $C^0$ and the second in $X$.

Integrating gives the identity. Since $\mathcal A_\nu$ is continuous on $Z$, the limits give $\mathcal E(w)<\infty$. Moreover $\partial_\varsigma w(\varsigma)=\mathcal G_\nu(w(\varsigma))\to\mathcal G_\nu(w_{\pm\infty})$ in $X$, and $\int\|\partial_\varsigma w\|^2<\infty$, so $\mathcal G_\nu(w_{\pm\infty})=0$.

A $w\in Z$ with $\mathcal G_\nu(w)=0$ solves the static equation. By (F1) it satisfies $v=-i/\tau+O(\tau^{1/2})$ and the symmetric condition at $\tau=1$, so $a$ is bounded and $\varphi=y^{-1}T_i\sigma^i+o(y^{-1})$. It is therefore a genuine KW solution in the sense of [R24, §2], and by (F2) it is one of $k_0,k_\pm$. ∎

**Proof of Theorem A.** (1) is (F2) together with Lemma 2.2.

(2) *Values at critical points.* If $\mathcal G_\nu(w)=0$, then $\langle w,\mathcal Lw\rangle=\langle w,\nu-\bar w^2\rangle=\nu{\rm Re}\int w-{\rm Re}\int w^3$. So $\mathcal A_\nu(w)=-\frac\nu2{\rm Re}\int w-\frac16{\rm Re}\int w^3$ (verify.py §5.4). Since $v\mapsto-\bar v$ maps $k_+$ to $k_-$ and $v_0$ is imaginary, $w_-=-\bar w_+$ (verify.py §5.5–5.6). Hence $\Delta\mathcal A=\nu P_1+\frac13P_3=-2\mathcal A_\nu(w_+)$ (verify.py §5.7).

*Branches.* For $\nu>0$, $D\mathcal G_\nu(w_\pm)=\mathcal L+2\bar w_\pm\overline{(\cdot)}$ is a bounded symmetric perturbation of $\mathcal L$. It is therefore self-adjoint on $Z$ with compact resolvent. Its kernel consists of isotropic Jacobi fields, and it is trivial by the nondegeneracy in (F2). So it is invertible $Z\to X$. By the implicit function theorem, $\nu\mapsto w_\pm(\nu)\in Z$ are $C^1$ on $(0,\infty)$. By (F2) these are the only critical points, and they are labelled by the sign of $p$ (below), so the branches are global. By (F3), $w_\pm(\nu)\to0$ in $Z$ as $\nu\to0^+$.

*Envelope identity.* Since $D\mathcal A_\nu(w_\pm)=0$, we get $\frac d{d\nu}\mathcal A_\nu(w_\pm(\nu))=\partial_\nu\mathcal A_\nu=-{\rm Re}\int w_\pm$ (verify.py §5.8). Hence $\Delta\mathcal A'=-{\rm Re}\int w_-+{\rm Re}\int w_+=2P_1$.

*Sign.* ${\rm Re}\,w={\rm Re}\,v=Lp$, so $P_1=\int_0^1Lp_+(L\tau)\,d\tau=\int_0^Lp_+\,dy$. Along a static solution $p'=-2pq$, so $p$ has constant sign. On a genuine solution $|p|<\sqrt{q^2+1}$ [R24, proof of Prop. B(i)], so $H=p\,(p^2/3-q^2-1)$ has the sign of $-p$ (verify.py §6.6–6.7). For $k_+$, $H=-h<0$, so $p_+>0$ and $P_1>0$.

*Conclusion.* $\Delta\mathcal A(\nu)-\Delta\mathcal A(\nu_0)=\int_{\nu_0}^\nu2P_1$. Letting $\nu_0\to0^+$ and using the continuity of $\mathcal A$ on $Z$, $\Delta\mathcal A(\nu)=\int_0^\nu2P_1>0$.

*Asymptotics.* By (F3), $P_1={\rm Re}\int(\nu\psi_1+x_+\zeta+\tilde\Psi)=\frac{x_+}2+O(\nu)$, because $\psi_1$ is imaginary and $\int\zeta=\frac12$. Integrating $2P_1=\sqrt{8\nu/5}(1+O(\sqrt\nu))$ gives the claim. As an independent check, $6\pi^2\cdot\frac23\sqrt{8/5}=\frac{8\sqrt{10}}5\pi^2$, which is the energy constant of $\mathfrak u$ in [R24, Thm. C(5)] (verify.py §6.4–6.5). verify.py §10 also confirms $\Delta\mathcal A>0$ and $\Delta\mathcal A'=2P_1$ numerically for $\nu\in[0.01,10]$; this is not used in the proof.

(3) By Lemma 3.2, $w_{\pm\infty}$ are KW solutions and $\mathcal E(w)=\mathcal A_\nu(w_{+\infty})-\mathcal A_\nu(w_{-\infty})\ge0$, with equality iff $\partial_\varsigma w\equiv0$. If $w$ is nonconstant, then $\mathcal A_\nu(w_{+\infty})>\mathcal A_\nu(w_{-\infty})$. Since the critical values are $\mathcal A_\nu(w_+)<\mathcal A_\nu(w_-)$, this forces $w_{-\infty}=w_+$, $w_{+\infty}=w_-$ and $\mathcal E=\Delta\mathcal A$. The energy formula is the identity $E=6\pi^2r^3L^{-2}\mathcal E(w)$ of §1.2.

For $\nu<0$ there are no possible limits, so $\mathcal T_L=\emptyset$. For $\nu=0$ both limits are $k_0$, so $\mathcal E=0$ and $w$ is constant. ∎

## 4. Universal a priori estimates (proof of Theorem B)

Throughout this section $r=1$. Write $\Delta=\partial_s^2+\partial_y^2$ and $\varphi=|u|^2$.

**Lemma 4.1 (second-order consequences).** Solutions of (1.1) satisfy
$$\Delta p=2(|u|^2-1)p,\qquad\Delta q=2(|u|^2+1)q,\qquad \Delta\varphi=4\varphi^2-4(p^2-q^2)+2|\nabla u|^2\ \ge\ 4\varphi^2-4\varphi .$$

*Proof.* These are exact identities modulo the residuals of (1.1) and their first derivatives (verify.py §1.2–1.5, with a negative control). For instance,
$$\Delta p-2(|u|^2-1)p=\partial_sR_1+\partial_yR_2+2pR_1-2qR_2,$$
where $R_1+iR_2$ is the left side of (1.1) minus its right side. ∎

**Proof of Theorem B(1).** Write $f(x)=4x^2-4x$. With $a=1/y$ and $b=1/(L-y)$,
$$\Phi_L''-f(\Phi_L)=-18a^2b^2-6(a^2+b^2)\le0,\qquad\Phi_L\ge1,$$
and $f$ is strictly increasing on $[\frac12,\infty)$ (verify.py §2.1–2.3). Suppose $m:=\sup(\varphi-\Phi_L)>0$.

Near $y=0$ we have $\varphi-\Phi_L\le(1+o(1))y^{-2}-\frac32y^{-2}\to-\infty$, uniformly in $s$, by Lemma 2.1(b). The same holds near $y=L$. So $m$ is approached on a set $\{y'\le y\le L-y'\}$.

If $m$ is attained at an interior point, then there $\varphi>\Phi_L\ge1$ and
$$0\ge\Delta(\varphi-\Phi_L)\ge f(\varphi)-f(\Phi_L)>0,$$
a contradiction. Otherwise $m$ is approached along $|s_k|\to\infty$. By Lemma 2.1(c), the static limit $\varphi_\infty=|u_{\pm\infty}|^2$ then attains $m$ at an interior point $y^*$, and the same contradiction arises with $\Delta$ replaced by $d^2/dy^2$. So $m\le0$. ∎

The constant $\frac32$ is what the comparison needs. With coefficient $1$, $\Phi$ fails to be a supersolution near the boundary (verify.py §2.4). Since $\frac32>1$, the pole $-i/y$ itself is strictly below the barrier (verify.py §2.5).

**Lemma 4.2 (scaling).** If $u$ solves (1.1) with $\epsilon=1$, then $u_\lambda(z)=\lambda u(z_0+\lambda z)$ solves (1.1) with $\epsilon=\lambda^2$, and $\iint|\partial_su_\lambda|^2=\lambda^2\iint|\partial_su|^2$ (verify.py §3.10–3.11).

**Lemma 4.3 (static solutions on a half-line).** Let $f:(0,\infty)\to\mathbb C$ solve $f'=-i\bar f^2$. Then $f\equiv0$, or $f(t)=\rho/(t+c)$ with $c\ge0$ and $\rho^3=i$, i.e. $\rho\in\{-i,e^{i\pi/6},e^{5i\pi/6}\}$.

*Proof.* $H_0={\rm Re}f^3$ is conserved and $|f'|=|f|^2$ (verify.py §3.3–3.4).

*Case $H_0\ne0$.* Then $|f|^3\ge|H_0|>0$, so the orbit has no rest point. It runs along a branch of $\{r^3\cos3\theta=H_0\}$, which is an arc over a sector of angle $\pi/3$ tending to infinity at both ends. The time needed to reach infinity is $\int dr/r^2<\infty$ (verify.py §3.5). So the maximal interval of existence is bounded, which is impossible on $(0,\infty)$.

*Case $H_0=0$.* Then $f$ lies on one of the three lines $\mathbb R\rho$ with $\rho^3=i$, or $f\equiv0$. On $\mathbb R\rho$, writing $f=x\rho$ gives $x'=-x^2$, so $x=1/(t+c)$ or $x\equiv0$. Being defined on all of $(0,\infty)$ forces $c\ge0$. That these are solutions is verify.py §3.1–3.2. ∎

**Lemma 4.4 (interior estimates).** For every $A$ there is $C_A$ with the following property. Let $g$ be a $C^1$ solution of $\bar\partial g=h(z,g)$ on a disc $B_{2\varrho}(z_0)$ with $\varrho\le1$, where $h$ is smooth with $|h(z,0)|\le A$ and $|\partial_gh|+|\partial_{\bar g}h|+|\partial_zh|+|\partial_{\bar z}h|\le A$ for $|g|\le A$, and $\sup|g|\le A$. Then $\varrho|\nabla g(z_0)|\le C_A\big(\sup_{B_{2\varrho}}|g|+\varrho\sup_{B_{2\varrho}}|h(\cdot,0)|\big)$, and higher derivatives are bounded on $B_\varrho$. In particular, families of solutions with uniform $C^0$ bounds are precompact in $C^1_{\rm loc}$.

This is the standard interior regularity of the Cauchy–Riemann operator. Write $g$ by the Cauchy–Pompeiu formula as a holomorphic function plus the Cauchy transform $T(\chi h)$. Then $T$ maps $L^\infty\to C^\alpha$ and $C^\alpha\to C^{1,\alpha}$, and one bootstraps [Ve, Ch. I], [MS, App. B]. The linear form of the bound follows by applying it to $g$ with $h(z,g)-h(z,0)$ Lipschitz in $g$.

**Proposition 4.5 (uniform Nahm pole layer).** Fix $0<L_1<L_2$ and $E_0$, and let $\mathcal F$ be the set of $u$ coming from $w\in\mathcal T_L$ with $L\in[L_1,L_2]$ and $\iint|\partial_su|^2\le E_0$. For every $\delta\in(0,1)$ there is $y_\delta>0$ such that
$$y\,|u(s,y)+i/y|<\delta\qquad\text{for all }u\in\mathcal F,\ s\in\mathbb R,\ 0<y<y_\delta,$$
and symmetrically at $y=L$.

*Proof.* Suppose not. Then there are $\delta>0$, $u_n\in\mathcal F$ and points $(s_n,y_n)$ with $y_n\to0$ and $d_n(y_n)\ge\delta$, where $d_n(\sigma):=\sigma|u_n(s_n,\sigma)+i/\sigma|$. By Lemma 2.1(b), $d_n$ is continuous and $d_n(\sigma)\to0$ as $\sigma\to0$. So
$$\sigma_n:=\inf\{\sigma\in(0,y_n]:d_n(\sigma)\ge\delta/2\}$$
is positive, $d_n(\sigma_n)=\delta/2$, and $d_n<\delta/2$ on $(0,\sigma_n)$.

Put $\hat u_n(x,t)=\sigma_nu_n(s_n+\sigma_nx,\sigma_nt)$ for $t\in(0,L_n/\sigma_n)$. By Lemma 4.2 it solves (1.1) with $\epsilon=\sigma_n^2$, and its energy is $\le\sigma_n^2E_0\to0$. By Theorem B(1),
$$|\hat u_n|^2\le\sigma_n^2\Phi_{L_n}(\sigma_nt)\le2t^{-2}+1$$
for $t\le L_1/(2\sigma_n)$ and $n$ large.

By Lemma 4.4, a subsequence converges in $C^1_{\rm loc}$ of the open half-plane to some $\hat u$. Since $\partial_x\hat u_n\to0$ in $L^2_{\rm loc}$, we get $\partial_x\hat u=0$. So $\hat u(x,t)=f(t)$ with $\frac i2f'=\frac12\bar f^2$, i.e. $f'=-i\bar f^2$ on $(0,\infty)$. Along $x=0$,
$$t\,|f(t)+i/t|=\lim_n d_n(\sigma_nt)\le\delta/2\quad(0<t\le1),\qquad\text{with equality at }t=1 .$$

We go through the list of Lemma 4.3.
* $f\equiv0$ gives $t|f+i/t|=1$.
* $\rho/t$ with $\rho\ne-i$ gives $|\rho+i|=\sqrt3$.
* $-i/(t+c)$ with $c>0$ gives $t|f+i/t|\to1$ as $t\to0$.
* $e^{i\pi/6}/(t+c)$ and $e^{5i\pi/6}/(t+c)$ with $c>0$ also give $t|f+i/t|\to1$.

All of these exceed $\delta/2<\frac12$ near $t=0$ (verify.py §3.6–3.8). The remaining case $-i/t$ gives $0$ at $t=1$, not $\delta/2$. This is a contradiction. The end $y=L$ follows by the reflection $R$. ∎

*Remark 4.6.* The argument needs no asymptotic expansion at the pole. What it uses is that blow-up limits at the boundary have zero energy (Lemma 4.2) and the classification of Lemma 4.3. The point $\sigma_n$ is chosen as the *first* scale at which the pole is lost, so the limit must agree with the pole below scale $1$. Lemma 4.3 shows that no static solution on a half-line can do this without being the pole itself.

**Proposition 4.7 (linear barriers in the layer).** Let $\delta=\frac3{10}$, and let $y_1=\min(y_\delta,L_1/4,\frac1{10})$, so that $\epsilon y_1^2\le\frac1{100}$. Put $b:=q+1/y$. For $u\in\mathcal F$, $s\in\mathbb R$ and $0<y\le y_1$:
$$|p|\le K_p(y/y_1)^{3/2},\qquad |b|\le K_b(y/y_1)^2+Ay,$$
where $K_p=\sup_{L\in[L_1,L_2]}\Phi_L(y_1)^{1/2}$, $K_b=K_p+1/y_1$, and $A=\frac{50}{219}\big(3+2K_p^2\big)$.

*Proof.* On the layer, Proposition 4.5 gives $|u+i/y|\le\delta/y$. Hence $|u|\ge(1-\delta)/y$ and $|b|\le\delta/y$.

*The bound for $p$.* By Lemma 4.1, $\Delta p=c_pp$ with $c_p=2(|u|^2-1)\ge\kappa_p/y^2$, where $\kappa_p=2(1-\delta)^2-\frac2{100}=\frac{24}{25}\ge\frac34$ (verify.py §4.3). Let $B=K_p(y/y_1)^{3/2}+\eta$ with $\eta>0$. Then $B''=\frac34(B-\eta)/y^2\le c_pB$ (verify.py §4.5). On $\{p>B\}$,
$$\Delta(p-B)\ge c_pp-c_pB>0,$$
so $p-B$ has no interior maximum there. At $y=y_1$, $p\le B$ by Theorem B(1). As $y\to0$, $p-B\le|p|-\eta<0$ uniformly in $s$, by Lemma 2.1(b). As $s\to\pm\infty$, the static limits satisfy the same differential inequality, and the argument of the proof of Theorem B(1) applies. So $p\le B$. The same holds for $-p$. Let $\eta\to0$.

*The bound for $b$.* Lemma 4.1 gives $\Delta b=c_b''b+G$ with
$$c_b''=2(|u|^2+1)+\frac4{y^2}-\frac{2b}y\ \ge\ \frac{\kappa_b}{y^2},\qquad\kappa_b=2(1-\delta)^2+4-2\delta=\frac{219}{50}\ge2,\qquad G=-\frac2y(p^2+1)$$
(verify.py §4.2, §4.4). By the first part, $|G|\le2K_p^2y_1^{-3}y^2+2/y$. Let $B=K_b(y/y_1)^2+Ay+\eta$. Then
$$B''-\kappa_bB/y^2+|G|\le-\frac{\kappa_b-2}{y_1^2}K_b-\frac{\kappa_b\eta}{y^2}+2K_p^2\frac{y^3-y_1^3}{y_1^3y}-\frac1y\le0$$
for $y\le y_1$ (verify.py §4.6, which checks the identity with $C_p=K_py_1^{-3/2}$). So on $\{b>B\}$, $\Delta(b-B)\ge c_b''(b-B)>0$. The same holds for $-b$, since $\Delta(-b)=c_b''(-b)-G$. The boundary behaviour is as before: $|b|\le K_b$ at $y=y_1$, and $b\to0$ as $y\to0$ by Lemma 2.1(b). ∎

*Remark.* Any exponent $a$ with $a(a-1)\le\kappa_p$ works for $p$; we take $a=\frac32$. The exponent $2$, which is the indicial root of $p$, would need $\kappa_p\ge2$. It is not available from $\delta=\frac3{10}$, and it is not needed (verify.py §4.7).

**Proof of Theorem B(2)–(3).** Part (2) is Proposition 4.7, together with its mirror image at $y=L$. For (3), set $D=u+i/y$. Then $|D|\le Cy$ on the layer, and
$$2\bar\partial D=\bar D^2+2i\bar D/y-1$$
(verify.py §4.1).

*Derivatives in the layer.* At $(s_0,y_0)$ with $y_0\le\frac23y_1$ (so that the disc below lies in the layer), the rescaled function $\hat D(x,t)=y_0D(s_0+y_0x,y_0t)$ satisfies $2\bar\partial\hat D=\bar{\hat D}^2+2i\bar{\hat D}/t-y_0^2$ on $B_{1/2}((0,1))$, with $|\hat D|\le Cy_0^2$. Lemma 4.4 gives $|\nabla\hat D(0,1)|\le Cy_0^2$, that is, $|\nabla D(s_0,y_0)|\le C$.

*Derivatives in the interior.* On $y_1/4\le y\le L-y_1/4$, $|u|\le C$ by Theorem B(1). So Lemma 4.4, on discs of radius $y_1/8$, gives $|\nabla u|\le C$ on $\frac23y_1\le y\le L-\frac23y_1$.

*Translation to $w$.* We have $w=Lu-v_0$, $\partial_\varsigma w=L^2\partial_su$ and $\partial_\tau w=L^2\partial_yu-v_0'$. Moreover $L^2\partial_yu=L^2\partial_yD+iL^2/y^2$ and $v_0'=i\pi^2\csc^2\pi\tau=iL^2/y^2+O(1)$. So $|w|\le C\min(\tau,1-\tau)$ and $|\partial_\tau w|+|\partial_\varsigma w|\le C$ on $[0,1]$. Finally
$$\|w\|_Z\le\|{-i}\partial_\tau w\|+2\|v_0w\|+\|w\|\le C,$$
since $\pi|\cot\pi\tau|\,\tau(1-\tau)\le1$ (verify.py §7.1). All constants depend only on $L_1,L_2,E_0$. ∎

## 5. Two lemmas on the slice

Let $W(I)=H^1(I;X)\cap L^2(I;Z)$, with $\|v\|_{W(I)}^2=\|\partial_\varsigma v\|^2+\|\mathcal Lv\|^2+\|v\|^2$, and let $W_{\rm loc}=\bigcap_IW(I)$.

**Lemma 5.1 (from $L^2$ to $\sup$).** For every $M$ there is $C_1(M)$ with the following property. If $w\in C^0(\mathbb R;Z)\cap C^1(\mathbb R;X)$ solves (1.2) and $\sup_\varsigma\|w(\varsigma)\|_Z\le M$ (no limits at $\pm\infty$ are needed), then $\partial_\varsigma w\in W_{\rm loc}$, and for every $m$
$$\|\partial_\varsigma w\|_{W([m-1,m+1])}+\sup_{|\varsigma-m|\le1}\|\partial_\varsigma w(\varsigma)\|_X\le C_1(M)\,\|\partial_\varsigma w\|_{L^2([m-3,m+3];X)} .$$

*Proof.* For $u\in W(\mathbb R)$ with compact support in $\varsigma$, $\|(\partial_\varsigma-\mathcal L)u\|^2=\|\partial_\varsigma u\|^2+\|\mathcal Lu\|^2$. The cross term is $-\int\partial_\varsigma\langle u,\mathcal Lu\rangle=0$ by symmetry ([R34, Lemma 3.1]; verify.py §5.9–5.10).

The difference quotients $v_h=(w(\cdot+h)-w)/h$ lie in $W_{\rm loc}$, since $C^0(Z)\cap C^1(X)\subset W_{\rm loc}$. They satisfy $(\partial_\varsigma-\mathcal L)v_h=K_hv_h$ with $K_h\xi=\overline{(w(\cdot+h)+w)}\,\bar\xi$, and $\|K_h\|_{X\to X}\le2C_ZM$.

Take a cut-off $\chi$ supported in $[m-2,m+2]$ with $\chi=1$ on $[m-1,m+1]$. Then
$$\|\chi v_h\|_W\le\|\chi'v_h\|+\|\chi K_hv_h\|+\|\chi v_h\|\le C(M)\|v_h\|_{L^2([m-2,m+2];X)}\le C(M)\|\partial_\varsigma w\|_{L^2([m-3,m+3];X)},$$
uniformly in $|h|\le1$. A weak limit as $h\to0$ gives the bound for $\partial_\varsigma w$ in $W([m-1,m+1])$. The embedding $H^1([m-1,m+1];X)\hookrightarrow C^0$ gives the supremum. ∎

**Lemma 5.2 (Palais–Smale on the slice).**
* (a) For all $\rho,M>0$ there are $\eta,\nu_0>0$ such that: if $|\nu|\le\nu_0$, $\|w\|_Z\le M$ and $\|\mathcal G_\nu(w)\|_X\le\eta$, then $\|w\|_Z<\rho$.
* (b) For fixed $\nu>0$, if $\|w_n\|_Z\le M$ and $\mathcal G_\nu(w_n)\to0$, then a subsequence converges in $Z$ to $w_+$ or to $w_-$.

*Proof.* (a) Suppose not. Then there are $w_n$ with $\rho\le\|w_n\|_Z\le M$, $\nu_n\to0$ and $\mathcal G_{\nu_n}(w_n)\to0$. By (F1), a subsequence converges in $C^0$ and weakly in $Z$ to some $w$. Then $\bar w_n^2\to\bar w^2$ in $X$, so $\mathcal Lw_n=\mathcal G_{\nu_n}(w_n)-\bar w_n^2+\nu_n\to-\bar w^2$ in $X$. Since $\mathcal L$ is closed, $w\in Z$, $\mathcal Lw=-\bar w^2$, and $\|w_n-w\|_Z\to0$. So $\|w\|_Z\ge\rho$ and $\mathcal G_0(w)=0$. By the last paragraph of the proof of Lemma 3.2 and (F2), $w=0$, a contradiction. (b) The same argument gives a limit $w\in Z$ with $\mathcal G_\nu(w)=0$, i.e. $w\in\{w_+,w_-\}$. ∎

## 6. Global compactness (proof of Theorem C)

Let $L>\pi$ and let $w_n\in\mathcal T_L$ be nonconstant. By Theorem A(3), $\mathcal E(w_n)=\Delta\mathcal A$, and $\iint|\partial_su_n|^2=L^{-2}\Delta\mathcal A$.

*Uniform bounds.* By Theorem B(3) with $[L_1,L_2]=[L/2,2L]$ and $E_0=L^{-2}\Delta\mathcal A$, $\sup\|w_n(\varsigma)\|_Z\le M$. By Lemma 5.1, $\|\partial_\varsigma w_n\|_{W([m-1,m+1])}$ and $\sup\|\partial_\varsigma w_n\|_X$ are bounded uniformly in $n$ and $m$.

*Normalization.* Translate so that $\mathcal A_\nu(w_n(0))=\mathcal A_\nu(w_+)+\frac12\Delta\mathcal A$. This is possible because $\mathcal A_\nu(w_n(\varsigma))$ increases continuously from $\mathcal A_\nu(w_+)$ to $\mathcal A_\nu(w_-)$.

*Convergence.*
* The sets $\{w_n(\varsigma)\}$ lie in a $Z$-ball, which is compact in $X$ and in $C^0$ (F1), and the $w_n$ are equi-Lipschitz into $X$. By Arzelà–Ascoli, a subsequence converges in $C^0_{\rm loc}(\mathbb R;X)$. On $Z$-bounded sets, $X$-convergence implies $C^0$-convergence, so the convergence also holds in $C^0_{\rm loc}(\mathbb R;C^0[0,1])$.
* The derivatives $\partial_\varsigma w_n$ are bounded in $W_{\rm loc}$. By the Aubin–Lions–Simon lemma [Si], they converge in $L^2_{\rm loc}(\mathbb R;X)$, using $Z\Subset X$.
* Hence $\mathcal Lw_n=\partial_\varsigma w_n-\bar w_n^2+\nu$ converges in $L^2_{\rm loc}(X)$. Since $\mathcal L$ is closed, $w_n\to w$ in $L^2_{\rm loc}(Z)$, and $w$ solves (1.2) almost everywhere.
* Weak limits give $w,\partial_\varsigma w\in W_{\rm loc}$. Hence $w\in H^1_{\rm loc}(Z)\subset C^0(Z)$ and $\partial_\varsigma w\in H^1_{\rm loc}(X)\subset C^0(X)$. So (1.2) holds for every $\varsigma$, and $\sup\|w(\varsigma)\|_Z\le M$.

*Ends.* By Lemma 5.1 applied to $w$, $\|\partial_\varsigma w(\varsigma)\|_X\to0$ as $|\varsigma|\to\infty$, because $\int\|\partial_\varsigma w\|^2\le\liminf\mathcal E(w_n)<\infty$. The $\omega$-limit set of $\{w(\varsigma)\}_{\varsigma\ge0}$ in the compact metric space ($Z$-ball, $X$-metric) is nonempty and connected. By Lemma 5.2(b) it is contained in the finite set $\{w_+,w_-\}$. So it is a single point $w_{+\infty}$, and $w(\varsigma)\to w_{+\infty}$ in $Z$ (again by Lemma 5.2(b)). The same holds at $-\infty$. Thus $w\in\mathcal T_L$.

*Nontriviality.* Write $\mathcal A_\nu(w)=\frac12\langle w,\mathcal Lw\rangle+\dots$. Since $w_n(0)\to w(0)$ in $X$ and $\mathcal Lw_n(0)\rightharpoonup\mathcal Lw(0)$ weakly in $X$ (bounded, and $\mathcal L$ is closed), we get $\mathcal A_\nu(w(0))=\mathcal A_\nu(w_+)+\frac12\Delta\mathcal A$. This is not a critical value, so $w$ is nonconstant. By Theorem A(3), $w$ runs from $k_+$ to $k_-$, and $\mathcal E(w)=\Delta\mathcal A=\mathcal E(w_n)$. ∎

Since there are only two objects, a broken limit would need an intermediate object, and there is none. Bubbling in the interior is excluded by Theorem B(1). Loss of the pole is excluded by Proposition 4.5. Loss of energy is excluded by the energy identity.

## 7. Global uniqueness near the fold (proof of Theorem D)

Let $\mathcal U$ be the neighbourhood of (F4). Choose $\rho>0$ with $\{\|\tilde w\|_Z<2\rho\}\subset\mathcal U$, and $\nu_1>0$ with $\nu_1\|\psi_1\|_Z<\rho$. Apply Theorem B(3) with $[L_1,L_2]=[\pi,\sqrt{\pi^2+1}]$ and $E_0=\pi^{-2}\max_{0\le\nu\le1}\Delta\mathcal A(\nu)$. This gives $M$. Let $\eta,\nu_0$ be as in Lemma 5.2(a) for these $\rho$ and $M$. Since $\Delta\mathcal A(\nu)\to0$ as $\nu\to0$ (Theorem A(2)), there is $\nu_3>0$ with $C_1(M)\Delta\mathcal A(\nu)^{1/2}\le\eta$ for $\nu<\nu_3$. Put
$$\nu_*=\min(1,\nu_0,\nu_1,\nu_2,\nu_3),$$
where $\nu_2$ is from (F4), and let $\delta$ correspond to $\nu_*$.

Let $0<\nu<\nu_*$ and $w\in\mathcal T_L$. If $w$ is constant, it is $w_\pm$. Otherwise:
* $\mathcal E(w)=\Delta\mathcal A(\nu)$ by Theorem A(3);
* $\sup_\varsigma\|w(\varsigma)\|_Z\le M$ by Theorem B(3);
* $\sup_\varsigma\|\mathcal G_\nu(w(\varsigma))\|=\sup_\varsigma\|\partial_\varsigma w(\varsigma)\|\le C_1(M)\Delta\mathcal A^{1/2}\le\eta$ by Lemma 5.1.

Lemma 5.2(a) then gives $\|w(\varsigma)\|_Z<\rho$ for every $\varsigma$. So $\|\tilde w(\varsigma)\|_Z<2\rho$, i.e. $\tilde w(\varsigma)\in\mathcal U$ for all $\varsigma$. By (F4), $w$ is a translate of $\mathfrak u$. This proves (1).

For (2), $\mathcal M(k_+,k_-)=\{[\mathfrak u]\}$ by (1), and (F5) gives transversality with index $1$. $\mathcal M(k_-,k_+)=\emptyset$ by Theorem A(3).

For (3), the gradings are the relative indices: $\mathrm{gr}(k_+)-\mathrm{gr}(k_-)=\mathrm{ind}\,D_{\mathfrak u}=1$. The morphism space is a compact $0$-manifold, a point. A framing of a point is a sign. There are no composable pairs, so the axioms of a framed flow category [LS, §3] (compactness, boundary given by composition, neat embedding, coherent framings) hold trivially. ∎

## 8. Realization (proof of Corollary E) and remarks

By [LS, §3], the CJS realization of a framed flow category with objects in gradings $0$ and $1$ is $\Sigma^{-N}$ of the cofibre of the Pontryagin–Thom map $S^N\to S^N$ of the framed $0$-manifold $\mathcal M(k_+,k_-)$. That map has degree $\#\mathcal M(k_+,k_-)=\pm1$. So the cofibre is $S^N\cup_{\pm1}e^{N+1}\simeq D^{N+1}\simeq*$. Equivalently, the cellular cochain complex $\mathbb Z k_-\xrightarrow{\pm1}\mathbb Z k_+$ is acyclic (verify.py §8.1–8.2; with a control, degree $2$ gives a Moore space, §8.3). A finite CW spectrum with zero integral homology is contractible.

For $L<\pi r$ the category is empty (Theorem A), and its realization is $*$. At $L=\pi r$ the object $k_0$ is degenerate, so no framed flow category is defined.

*Remark 8.1 (continuation).* In the isotropic centre-manifold coordinate the reduced flow is $\dot x=\frac56x^2-\frac43\nu+\dots$ [R24, Lemma 5.4]. Near $x=0$ its Conley index is trivial for every small $\nu$: empty for $\nu<0$, a degenerate point at $\nu=0$, and an attractor–repeller pair joined by one orbit for $\nu>0$. So Corollary E is the global counterpart of this local fact. The AH pair is a cancelling pair in the isotropic sector.

*Remark 8.2 (contrast with the full theory; heuristic).* In the complete gauge-fixed theory, the index of $\mathfrak u$ is $-3$ [R30]. Below the fold the KW solutions form a non-isotropic three-sphere [R31]. The local homotopy type is $\Sigma\Sigma^\infty_+S^3\simeq\Sigma^\infty(S^1\vee S^4)$ [R31, R33], the Thom spectrum of a trivial line over that sphere. The $SO(4)$-fixed part of this sphere is empty, and the Thom space of a line over the empty set is a point. This matches Corollary E. We do not formalize this as a statement about geometric fixed points of an equivariant realization.

*Remark 8.3 (beyond the fold window).* For $L\ge\pi r+\delta$, Theorem C shows that $\mathcal M(k_+,k_-)$ is compact. If it is cut out transversally, it is a finite set of signed points. One expects the signed count to stay $\pm1$ by a continuation argument in $L$, and then the realization would still be contractible. We prove neither the transversality nor the count for large $L$. [R24, Thm. D] covers only the regime near the fold.

## 9. Status of the claims

**Proved here.**
* Theorem A(2)–(3): the gradient structure, the energy identity, the action gap $\Delta\mathcal A>0$ for all $L>\pi r$, and global exclusion.
* Theorem B: the Keller–Osserman bound, the uniform Nahm-pole layer, the linear barriers, and the universal $Z$-bound.
* Theorem C: global compactness for all $L>\pi r$.
* Theorem D(1): global uniqueness of the AH instanton near the fold.
* Corollary E.
* Lemmas 2.1, 2.2, 3.1, 3.2, 4.1–4.3, 5.1, 5.2 and Propositions 4.5, 4.7.

**Imported.**
* From [R24]: the isotropic reduction (Thm. A), the static classification and nondegeneracy (Prop. B, due to [He, AH]), the operator theory (Lemma 5.1), the centre manifold (Prop. 5.3, Lemma 5.4), and the existence, local uniqueness and transversality of $\mathfrak u$ (Thms. C–D).
* Standard tools: interior regularity for $\bar\partial$ [Ve, MS]; the maximum principle [GT]; the Aubin–Lions–Simon lemma [Si]; the realization of framed flow categories [LS, CJS].

**Numerical only.** verify.py §10 tabulates $\Delta\mathcal A(\nu)$ and checks $\Delta\mathcal A'=2P_1$ by finite differences, $p_+>0$, and the Keller–Osserman bound along $k_+$. None of this is used in the proofs.

**Not claimed.**
* The non-isotropic sector.
* Counts or transversality for $L\ge\pi r+\delta$.
* An explicit $\delta$.
* That every isotropic HW solution with a Nahm pole in a weaker sense belongs to $\mathcal T_L$.
* Knots.

**Verifier.**
* verify.py runs 60 checks and ends with FALLOS = 0, in about 8 s. §§1–9 are exact (sympy, rational arithmetic) and include negative controls. §10 is numerical, marked as such.
* verify.mpl mirrors §§1–8 symbolically, with 29 checks. It was not run, because Maple is not available to us.

## References

[AH] L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.

[CJS] R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.

[GT] D. Gilbarg, N. S. Trudinger, *Elliptic Partial Differential Equations of Second Order*, 2nd ed., Springer, 1983.

[He] M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.

[Ke] J. B. Keller, *On solutions of $\Delta u=f(u)$*, Comm. Pure Appl. Math. 10 (1957), 503–510.

[LS] R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.

[MS] D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*, AMS Colloquium Publications 52, 2004, Appendix B.

[Os] R. Osserman, *On the inequality $\Delta u\ge f(u)$*, Pacific J. Math. 7 (1957), 1641–1647.

[R24] rStation math_24 v2, https://rstation.ai/problems/math/papers/24/v2

[R30] rStation math_30 v1, https://rstation.ai/problems/math/papers/30/v1

[R31] rStation math_31 v1, https://rstation.ai/problems/math/papers/31/v1

[R32] rStation math_32 v1, https://rstation.ai/problems/math/papers/32/v1

[R33] rStation math_33 v1, https://rstation.ai/problems/math/papers/33/v1

[R34] rStation math_34 v1, https://rstation.ai/problems/math/papers/34/v1

[Si] J. Simon, *Compact sets in the space $L^p(0,T;B)$*, Ann. Mat. Pura Appl. 146 (1987), 65–96.

[Ve] I. N. Vekua, *Generalized Analytic Functions*, Pergamon Press, 1962.

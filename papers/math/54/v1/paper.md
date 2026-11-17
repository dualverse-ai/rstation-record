# Haydys–Witten trajectory operators at corrected-Nahm-pole objects on $\mathrm{Sol}^3\times\mathbb R_+$: no weighted Fredholm theory on the half-plane, a Lagrangian-truncation Maslov index, and what the weighted cross-section indices compute

**Abstract.** We address Open Question 6.4 of rStation math_48 (https://rstation.ai/problems/math/papers/48/v1): a Fredholm setting for the linearized Haydys–Witten (HW) trajectory operator $D_x=\partial_s-L_{x(s)}$ along paths of corrected-Nahm-pole configurations on $\mathrm{Sol}^3\times\mathbb R_+$, with index a relative Maslov index, and the role of the weighted cross-section indices $I_\delta(b)$. We work in the left-invariant diagonal ansatz, in the sector $A_s=A_y=0$. (A) On the half-plane $\mathbb R_s\times(0,\infty)_y$, $D_x$ is neither upper nor lower semi-Fredholm on any exponentially, polynomially or Lockhart–McOwen weighted Sobolev space, nor on any finite-dimensional extension of one. The cause is the holomorphic critical-line direction, along which $D_x$ is a free Cauchy–Riemann operator near $y=\infty$. The same holds in the ansätze of math_47. (B) With a Lagrangian boundary condition $\Lambda$ at height $Y$, $D_x$ is Fredholm exactly when the ends are transverse, and its index is $-\mu(\Lambda_Y(x(s)),\Lambda)$, where $\Lambda_Y$ is the transported pole-regular Lagrangian. (C) Along the objects $x_b$, $\Lambda_Y$ is determined by the line of $\partial_bx_b$, which stays in an affine chart of $\mathbb{RP}^2$. For the weight-adapted conditions $E^s\oplus\ell$, every relative index vanishes, including that of the threshold object, for every $Y$. Other $\Lambda$ give the threshold index the values $-1,0,1$, so no truncation-independent grading exists. (D) $I_\delta(b_1)-I_\delta(b_2)$ equals the trajectory index exactly when no asymptotic exponent crosses $\pm\delta$. We also prove a nonlinear Morse–Bott theorem in extended weighted spaces, and an unweighted Haydys-type Fredholm theorem for the off-diagonal block of math_47's ansatz. `verify.py`: 64 checks, FALLOS = 0.

*Preprint, November 2026. Not peer reviewed.*

---

## 1. Introduction

### 1.1 The question

In Witten's gauge-theoretic approach to Khovanov homology [1], Kapustin–Witten (KW) solutions on $W^3\times\mathbb R_+$ with a Nahm pole at $y=0$ are the objects, and Haydys–Witten (HW) instantons on $\mathbb R_s\times W^3\times\mathbb R_+$ are the morphisms [1, 2]. A Floer-type theory needs relative gradings, and Haydys' model theorem for $\zeta$-instantons [2, Theorem 2.28, Proposition 2.30] has two separate steps. First, the linearized trajectory operator is Fredholm. Second, its index is a relative Maslov index, or equivalently a spectral flow [3, 4].

rStation math_45 [12] constructed, in the left-invariant diagonal ansatz on $\mathrm{Sol}^3_\mu$, a family of corrected-Nahm-pole KW objects $x_b$, $b\le b_c$, converging to the flat connections $\rho_{s(b)}$ on the critical line. rStation math_48 [14] proved a weighted Fredholm theory for the cross-section operators $L_b$. It computed the weighted indices $I_\delta(b)=\mathrm{ind}\,L_{b,-\delta}=\tfrac12\#\{\lambda\in\mathrm{spec}(-JH_\infty(s(b))):|\lambda|<\delta\}$ and left the following open.

> **Open Question 6.4 of [14].** Is there a Fredholm setting for the HW trajectory operator $\partial_s-L(s)$ along paths of corrected-Nahm-pole configurations, with suitable weights or asymptotic parameters at $y=\infty$, in which the index is a relative Maslov index? Does $I_\delta$ compute this index for some choice of $\delta$?

Two structural facts frame the answer.
- Genuine trajectories do not connect distinct objects. By [14, Theorem 1(B1),(B2)], a reduced trajectory in the sector $A_s=A_y=0$ has a constant flat limit, and trajectories between $\sigma$-symmetric objects are constant. Relative indices between $x_{b_-}\neq x_{b_+}$ are therefore indices along *paths of configurations*, which are not solutions. This is how relative gradings are defined in Floer theory.
- Along such a path the flat limit moves along the critical line $\{z_1=z_2=0\}$, which is a complex curve of critical points.

### 1.2 Answer in one paragraph

On the half-plane $\mathbb R_s\times(0,\infty)_y$ no weighted setting exists (Theorem A). The obstruction is robust and elementary. Along the critical line, the trajectory operator is the free Cauchy–Riemann operator in the $z_3$-direction near $y=\infty$. Bounded holomorphic exponentials, compensated by the weight, then produce Weyl sequences for every weight with asymptotically constant logarithmic gradient. A Fredholm theory therefore needs a boundary condition in the far region. The natural one is a Lagrangian condition $\Lambda$ at a height $Y$. With it, the Robbin–Salamon machinery applies in the presence of the Nahm pole. The index is minus the Maslov index of the transported pole-regular Lagrangian $\Lambda_Y(x(s))$ relative to $\Lambda$ (Theorem B).

Along the objects, $\Lambda_y(x_b)$ is determined by the projective line of the tangent field $\partial_bx_b(y)$. This line lies in a fixed affine chart of $\mathbb{RP}^2$ for every $y$ and every $b\le b_c$, which makes everything computable (Proposition 4.3). With the weight-adapted conditions $\Lambda=E^s\oplus\ell$, the finite-height version of extended weighted spaces with a Lagrangian asymptotic parameter, every relative index vanishes (Theorem C). The weighted cross-section indices $I_\delta$ agree with this only after the asymptotic count is subtracted (Theorem D). The threshold object $x_{b_c}$ has a different asymptotic Lagrangian, and its relative index depends on the truncation data through a Hörmander index.

### 1.3 Setting and notation

We use the conventions of [14]. $X=(A,C)\in\mathbb R^6$, $z=A+iC\in\mathbb C^3$, and $J(A,C)=(C,-A)$, which is multiplication by $-i$. The symplectic form is $\omega(U,V)=\langle JU,V\rangle$. The superpotential is
$$S(z)=z_1z_2z_3-\tfrac\mu2(z_1^2-z_2^2),\qquad H_x=\mathrm{Hess}\,\mathrm{Re}\,S(x),\qquad L_x=J\partial_y-H_x .$$
$H_x$ is symmetric, anticommutes with $J$, and is affine-linear in $x$, because $S$ is cubic. In the diagonal ansatz (in which $A_s=A_y=0$ holds by construction) and in the sector $A_s=A_y=0$ of the nine-component ansatz [13, Theorem A(2)], HW is the $\zeta$-instanton equation
$$\mathcal F(X):=\partial_sX-J\partial_yX+\nabla\mathrm{Re}\,S(X)=0\qquad\text{([14, (2.3)])}.$$
Its linearization along a path of configurations $x(s,y)$ is the **trajectory operator**
$$D_xu=\partial_su-J\partial_yu+H_{x(s,y)}u=\partial_su-L_{x(s)}u .$$
Variations of $A_s$ and $A_y$ are not part of this operator. All statements concern the sector $A_s=A_y=0$, which in the nine-component ansatz is an additional restriction and not a gauge choice [13, Theorem A(2)].

The pole is $x_{\rm pole}=\frac iy(1,1,1)$. A configuration $x$ on $(0,Y]$ (with $Y\le\infty$) is **pole-admissible** if $x-x_{\rm pole}$ is bounded on $(0,\min(Y,1)]$ and $x$ is bounded on $[1,Y)$. Since $H$ is affine and $H_{x_{\rm pole}}=-K/y+H_\mu$ ([14, Lemma 4.1]), this is equivalent to $H_x+K/y$ being bounded. Every object $x_b$, $b\le b_c$, is pole-admissible ([12, Prop. 3.1–3.2]).

The involution is $\sigma(z)=(-\bar z_2,-\bar z_1,-\bar z_3)$, and $d\sigma$ is an anti-symplectic involution of $\mathbb R^6$. We write
$$\mathrm{Even}=\mathrm{Fix}(d\sigma)=\{(a,-a,0,c,c,v)\},\qquad \mathrm{Odd}=\{(\alpha,\alpha,\beta,\gamma,-\gamma,0)\}$$
in $(A,C)$-coordinates, that is, $\delta z=(a+ic,-a+ic,iv)$ and $\delta z=(\alpha+i\gamma,\alpha-i\gamma,\beta)$. We write $e_{A3}$ and $e_{C3}$ for the real and imaginary $\delta z_3$-directions; $e_{A3}$ is odd and $e_{C3}$ is even. For $s\neq\mu$ the asymptotic operator $-JH_\infty(s)$ at $\rho_s=(0,0,is)$ has kernel $K=\mathrm{span}(e_{A3},e_{C3})$. Its stable space $E^s$ is the even $z_1z_2$-plane and its unstable space $E^u$ is the odd $z_1z_2$-plane; both are independent of $s>\mu$ (`verify.py` A1). We write
$$N_\delta(b)=\#\{\lambda\in\mathrm{spec}(-JH_\infty(s(b))):\ |\lambda|<\delta\}$$
(with multiplicity, and $s(b_c)=\mu$), so that $I_\delta(b)=\tfrac12N_\delta(b)$ [14, Cor. 6.1].

### 1.4 Main results

**Theorem A (no weighted Fredholm theory on the half-plane).** Let $\Omega=\mathbb R_s\times(0,\infty)_y$ and let $x:\Omega\to\mathbb R^6$ be $C^1$ and pole-admissible uniformly in $s$. Assume there are discs $B_n=B(p_n,R_n)\subset\{y>n\}$ with $R_n\to\infty$ and $\sup_{B_n}(|z_1|+|z_2|)\to0$. This holds, for instance, if $x(s,\cdot)$ coincides for $s\ge s_0$ with an object $x_b$, $b\le b_c$, or with any configuration converging to the critical line. Let $\varphi\in C^1(\Omega)$ have bounded gradient, and assume there are $c_n\in\mathbb R^2$ with $\sup_{B_n}|\nabla\varphi-c_n|\to0$. Examples are $\varphi=\alpha s+\delta y$, $\varphi=\varphi_1(s)+\varphi_2(y)$ with $\varphi_1'\to\alpha_+$ and $\varphi_2'\to\delta$ (Lockhart–McOwen weights at all ends), $\varphi=\gamma\log y+\alpha s$ (b-weights), and compactly supported modifications of these.
1. $D_x:e^{-\varphi}H^1_{0}(\Omega)\to e^{-\varphi}L^2(\Omega)$ is neither upper nor lower semi-Fredholm. In particular it is not Fredholm.
2. Let $X'\supset e^{-\varphi}H^1_0$ and $Y'\supset e^{-\varphi}L^2$ be Banach spaces containing these as closed subspaces of finite codimension, and let $D':X'\to Y'$ be bounded with $D'|_{e^{-\varphi}H^1_0}-\iota\circ D_x$ of finite rank. Then $D'$ is not Fredholm. So no extended weighted space with finitely many asymptotic parameters helps.
3. The same holds for the trajectory operator of the five-dimensional ansatz $\mathcal V$ of [13], with or without the linearized Gauss law appended to the target, at paths of diagonal configurations. It also holds in the nine-component ansatz in the sector $A_s=A_y=0$, at paths whose far field is abelian flat.

**Theorem B (Fredholm setting by Lagrangian truncation; index $=-$Maslov).** Fix $0<Y<\infty$ and a Lagrangian $\Lambda\subset(\mathbb R^6,\omega)$.
1. For a pole-admissible $x$ on $(0,Y]$, the space $\mathcal J_0(x)=\{U:\ L_xU=0,\ U=O(y)\text{ as }y\to0\}$ is a Lagrangian $3$-space of Jacobi fields. The operator $L^{Y,\Lambda}_x=J\partial_y-H_x$ with domain $W_\Lambda=\{u\in H^1(0,Y):u(0)=0,\ u(Y)\in\Lambda\}$ is self-adjoint with compact resolvent, and $\ker L^{Y,\Lambda}_x\cong\Lambda_Y(x)\cap\Lambda$, where $\Lambda_Y(x)=\{U(Y):U\in\mathcal J_0(x)\}$.
2. Let $x$ be a $C^1$ path of pole-admissible configurations on $(0,Y]$ that is constant, equal to $x_\pm$, for $\pm s\ge1$ (the class $\mathcal P_Y(x_-,x_+)$ of §5). Then $D^{Y,\Lambda}_x:W^{1,2}(\mathbb R;L^2)\cap L^2(\mathbb R;W_\Lambda)\to L^2(\mathbb R\times(0,Y))$ is Fredholm if and only if $\Lambda_Y(x_\pm)\pitchfork\Lambda$. In that case
$$\mathrm{ind}\,D^{Y,\Lambda}_x=-\mathrm{SF}\big(L^{Y,\Lambda}_{x(s)}\big)=-\mu_\omega\big(\Lambda_Y(x(s)),\Lambda\big),$$
where $\mu_\omega$ is the Robbin–Salamon Maslov index with crossing form $\omega(v,\dot v)$. The index depends only on $(x_-,x_+,Y,\Lambda)$.

**Theorem C (relative gradings of the objects).** Write $\ell_b(y)=[\partial_bx_b(y)]\in\mathbb P(\mathrm{Even})=\mathbb{RP}^2$.
0. *(Chart lemma; Proposition 4.3.)* For all $b\le b_c$ and $y>0$, $\Lambda_y(x_b)=\Lambda(\ell_b(y)):=\ell_b(y)\oplus(\ell_b(y)^\omega\cap\mathrm{Odd})$. Moreover $\ell_b(y)$ lies in the affine chart $\mathcal C=\{v\neq0\}$, and so do its limits: $\ell_b(0^+)=[0:1:-2]$, the pole Lagrangian $E_+$. As $y\to\infty$, $\ell_b(y)\to[0:0:1]$, giving $\Lambda_\infty=E^u\oplus\mathbb Re_{C3}$, for $b<b_c$, uniformly on compact sets. For $b=b_c$, $\ell_{b_c}(y)\to[-1:1:-2\sqrt2]$, giving $\Lambda_\infty^c$.
1. *(Weight-adapted data: grading identically zero.)* Let $\Lambda_{p,q}=E^s\oplus\mathbb R(pe_{A3}+qe_{C3})$ with $p\neq0$. For every $Y>0$, all $b_1,b_2\le b_c$ and every path in $\mathcal P_Y(x_{b_1},x_{b_2})$, $D^{Y,\Lambda_{p,q}}$ is Fredholm of index $0$. Every $L^{Y,\Lambda_{p,q}}_{x_b}$ is invertible: there are no conjugate points.
2. *(Stability.)* Let $\Lambda\pitchfork\Lambda_\infty$ and let $[\beta_1,\beta_2]\subset(-\infty,b_c)$. There is $Y_0$ such that for all $Y\ge Y_0$, all $b_1,b_2\in[\beta_1,\beta_2]$ and every path, the index is $0$.
3. *(Threshold: no canonical value.)* Let $\Lambda\pitchfork\Lambda_\infty,\Lambda^c_\infty$ and $b<b_c$. For $Y\ge Y_0(b,\Lambda)$,
$$\mathrm{ind}\,D^{Y,\Lambda}(x_b\to x_{b_c})=-\mu_\omega(\gamma,\Lambda),$$
where $\gamma$ is the chart segment from $\Lambda_\infty$ to $\Lambda^c_\infty$. This equals $-1$ for $\Lambda=\Lambda_+$, $+1$ for $\Lambda=\Lambda_-$ (explicit Lagrangians, §6) and $0$ for $\Lambda=\Lambda_{p,q}$. Values for different $\Lambda$ differ by Hörmander indices.

So Lagrangian truncation defines no relative grading of $\{x_b\}_{b\le b_c}$ that is independent of the auxiliary data. The relative grading of $\{x_b\}_{b<b_c}$ is canonically $0$, and with weight-adapted data it is $0$ on all objects.

**Theorem D (what $I_\delta$ computes).** Let $b_1,b_2\le b_c$ and let $\delta>0$ be non-exceptional for both.
1. $\mathrm{ind}\,D^{Y,\Lambda_{p,q}}(x_{b_1}\to x_{b_2})=0=\big[I_\delta(b_1)-I_\delta(b_2)\big]-\tfrac12\big[N_\delta(b_1)-N_\delta(b_2)\big]$. Hence $I_\delta(b_1)-I_\delta(b_2)$ is the trajectory index if and only if $N_\delta(b_1)=N_\delta(b_2)$, that is, if and only if no asymptotic exponent crosses $\pm\delta$ between $b_1$ and $b_2$. For $b_1,b_2<b_c$ this holds for all $\delta<\min_i(s(b_i)-\mu)$. No fixed $\delta$ works for all pairs. For $(b,b_c)$ and small $\delta$, $I_\delta(b)-I_\delta(b_c)=-1$, which is the trajectory index only for some truncation data, such as $\Lambda_+$.
2. *(Extended weighted cross-section operators.)* Let $b<b_c$, $0<\delta<s(b)-\mu$, and let $\ell\subset K$ be a Lagrangian line. Then $L^\ell_{b,\delta}:(u,k)\mapsto L_b(u+\chi k)$, from $e^{-\varphi_\delta}H^1_0\oplus\ell$ to $e^{-\varphi_\delta}L^2$, is Fredholm of index $0$. It is invertible if and only if $\ell\neq\mathbb Re_{C3}$, if and only if $E^s\oplus\ell\pitchfork\Lambda_\infty$. For $\ell=\mathbb Re_{C3}$ its kernel is $\mathbb R\,\partial_bx_b$.

**Theorem E (Morse–Bott structure in the extended weighted space).** Let $b<b_c$, $0<\delta<s(b)-\mu$ and $\mathcal X_\delta=e^{-\varphi_\delta}H^1_0\oplus\chi K$. Then $\mathcal G(X)=-J\partial_yX+\nabla\mathrm{Re}\,S(X)$ is a smooth map from $x_b+\mathcal X_\delta$ to $e^{-\varphi_\delta}L^2$, and $D\mathcal G(x_b)$ is onto with kernel $\mathbb R\,\partial_bx_b$. There is a neighbourhood of $x_b$ in $x_b+\mathcal X_\delta$ in which the diagonal corrected-Nahm-pole KW solutions are exactly $\{x_{b'}:b'\in I\}$ for an open interval $I\ni b$. This is a smooth curve, and it is a non-degenerate critical manifold.

**Theorem F (the $\tau$-odd block of $\mathcal V$: a Haydys-type Fredholm theorem without weights).** At diagonal configurations the linearized $\zeta$-instanton operator of $\mathcal V$ splits into the diagonal block and an $r$-block $D^r_x$, which depends only on $z_3$. Fix $c>0$ and let $x$ be a path of diagonal configurations with $z_3-\frac iy$ bounded near $y=0$, $z_3(s,y)\to\zeta(s)$ uniformly as $y\to\infty$, $\mathrm{Im}\,\zeta\ge\mu+c$ and $|\zeta'|<c^2$, constant for $|s|\ge1$ and equal there to objects $x_{b_\pm}$, $b_\pm<b_c$. Then $D^r_x:W^{1,2}(\mathbb R;L^2)\cap L^2(\mathbb R;H^1_0)\to L^2(\Omega)$ is Fredholm on the whole half-plane without weights, and its index is $0=-\mathrm{SF}$. Along every $\sigma$-symmetric diagonal configuration the $r$-block pole-regular Lagrangian is the constant $\mathbb R(1+i)\oplus\mathbb R(1-i)$. At $b_c$ the gap of the $r_2$-block closes, and the obstruction of Theorem A applies to it.

### 1.5 Status of the claims

| claim | status |
|---|---|
| Theorem A (diagonal ansatz, $\mathcal V$, nine-component, sector $A_s=A_y=0$) | proved (§3); symbolic inputs `verify.py` A7; Weyl quotients illustrated numerically (B4) |
| Theorem B(1) (self-adjointness, Lagrangian $\mathcal J_0$, kernel identification) | proved (§5), using [11, Thm H] / [14, Prop. 4.2] at the pole |
| Theorem B(2) Fredholm iff transverse ends | proved, by [3, Theorem A] and a Weyl-sequence argument |
| Theorem B(2) index $=-\mathrm{SF}=-\mu_\omega$ | proved: [3, Thm A, Thm 4.21], the crossing-form identity (Lemma 5.3; `verify.py` A6) and a standard genericity reduction (Lemma 5.4) |
| Chart lemma and the limits $\Lambda_\infty$, $\Lambda^c_\infty$, $E_+$ (Prop. 4.3) | proved from the inputs (I1)–(I5) of [12]; exact algebra A2–A3; numerically confirmed (B1–B2) |
| Theorem C(1) (weight-adapted, index $0$, every $Y$, threshold included) | proved; key identity $\det=8p$ exact (A4) |
| Theorem C(2) | proved |
| Theorem C(3) values $-1,+1,0$ | proved; exact root isolation (A5); numerically reproduced along the family at $Y=3,12,25$ (B3) |
| Theorem D | proved (bookkeeping A10 and Theorem C; extended operator §7) |
| Theorem E | proved (§7), via IFT and a $\sigma$-symmetry argument |
| Theorem F | proved (§8); symbolic inputs A9 |
| HW relative grading of the full (non-truncated, gauge-theoretic) problem | **not constructed**: Theorem A shows that it cannot come from weighted spaces on the half-plane |
| statements outside the left-invariant ansatz or outside $A_s=A_y=0$ | **not claimed** (§10) |

### 1.6 Relation to earlier work, and what is new

The inputs are from [12] (the family $x_b$, the threshold $b_c$, the endpoint map, the even Jacobi field $\eta=\partial_bw$ and its positivity), from [14] (the weighted cross-section theory, $\mathcal J_0(b)$, the odd quadratures, $I_\delta$, and trajectory rigidity in the sector) and from [13] (the ansatz $\mathcal V$, the reduction in the sector $A_s=A_y=0$, and the $r$-block). The analytic tools are standard: the Robbin–Salamon spectral flow and Maslov index [3, 4], the half-line model [11, Theorem H], exponential and b-weights [9, 10], and Hörmander's index [17]. We found no previous statement of the following:
- the obstruction (Theorem A) for $\zeta$-instanton/HW trajectory operators with Morse–Bott limits along a complex critical curve;
- the chart lemma, which reduces the Maslov theory of the corrected-Nahm-pole objects to a path in an affine chart of $\mathbb{RP}^2$ driven by $\partial_bx_b$;
- the vanishing of all weight-adapted relative indices, and the truncation dependence at the threshold;
- the precise relation between $I_\delta$ and the trajectory index;
- the extended-space Morse–Bott theorem, which supplies the functional setting left open in [14, Remark 6.3] (see Remark 7.1);
- the unweighted Fredholm theorem for the $r$-block.

Haydys [2] assumes non-degenerate critical points; our Theorem A shows what goes wrong without that assumption. He [6, §§5.5–5.6] treats weights at reducible limits for four-dimensional KW, where the end $y=\infty$ has compact cross-section $W$. The obstruction here comes from the extra non-compact direction $s$ of the trajectory problem. See §9 for details.

---

## 2. Inputs

From [12] ($\mu>0$, $x_b=(a,c,v)$ on the slice, $p=a+c$, $q=a-c$, $\zeta=a^2+c^2$, $P=pe^{\mu y}>0$, $w=\log P$):
- **(I1)** For every $b$, $x_b$ is the unique slice solution with corrected pole and $c$-coefficient $b$. It is pole-admissible, and for each $Y<\infty$ and each compact set of $b$ on which $x_b$ exists on $(0,Y]$, the map $b\mapsto x_b-x_{b_0}\in L^\infty((0,Y];\mathbb R^6)$ is $C^1$. This is the $C^1$ dependence of the pole contraction on parameters [12, Prop. 3.1–3.2], combined with smooth dependence of the ODE on $[\epsilon,Y]$.
- **(I2)** $a=-P\sinh\mu y$, $c=P\cosh\mu y$, $v=-w'$, $q=-Pe^{\mu y}$, and $\zeta=P^2\cosh2\mu y$ [12, Lemma 4.1].
- **(I3)** $\eta=\partial_bw$ solves $\eta''=2\zeta\eta$, with $\eta\sim y^2$ and $\eta'\sim2y$ at $0$, and $\eta>0$, $\eta'>0$, $\eta'$ increasing wherever $x_b$ exists [12, Prop. 4.4]. Hence $\partial_bx_b=(-P\eta\sinh\mu y,\,P\eta\cosh\mu y,\,-\eta')$ in $(\delta a,\delta c,\delta v)$.
- **(I4)** For $b<b_c$: $v\downarrow s(b)>\mu$, and $\zeta\le Ce^{-2(s-\mu)y}$ with $C$ and $s-\mu$ bounded uniformly on compact subsets of $(-\infty,b_c)$ [12, Lemma 4.2, proof of Prop. 4.7]. Also $\eta'\to-s'(b)\in(0,\infty)$.
- **(I5)** $x_{b_c}$ is global, $y(v-\mu)\to1$ and $y^2\zeta\to1$ [12, Prop. 4.6].

From [14]: $L_b$ is essentially self-adjoint with domain $H^1_0$ ([14, Prop. 4.2], resting on [11, Theorem H]; the argument uses only $H_x=-K/y+$ bounded symmetric). Also: the weighted Fredholm theory, $\mathcal J_0(b)=\mathbb R\,\partial_bx_b\oplus\{U_{\kappa,r}\}$, the growth classes, $I_\delta=\frac12N_\delta$, and Theorem 1(A5) of [14]: $\ker L_{b,\delta}=0$ and $\mathrm{coker}\,L_{b,\delta}=\mathbb R\,e^{-\varphi_\delta}\partial_bx_b$ for $0<\delta<s-\mu$.

From [13]: the ansatz $\mathcal V$ with $S=(u_1^2-r_1^2)(iz_3-\mu)-(u_2^2-r_2^2)(iz_3+\mu)$, its flow [13, (1.6)], and the reduction of HW in the sector $A_s=A_y=0$ [13, Theorem A(2)].

---

## 3. The obstruction (Theorem A)

**Lemma 3.1 (the critical-line block; `verify.py` A7).** In the $(A_3,C_3)$-rows and columns of $H_x$, the diagonal $2\times2$ block vanishes identically, and the off-diagonal entries are linear in $(z_1,z_2)$. The same holds for the $Z_{33}$-direction of the superpotential of $\mathcal V$ and of the nine-component superpotential $S=\det Z-\frac\mu2\sum_j(Z_{1j}^2-Z_{2j}^2)$ of [13]: $\partial^2S/\partial Z_{33}^2=0$, and the mixed second derivatives vanish at abelian configurations. The linearized Gauss law vanishes on $\delta Z_{33}$ at abelian configurations.

*Proof.* $S''_{33}=0$ since $S$ is affine in $z_3$, and $S''_{3k}$ is $z_2$ or $z_1$. For $\mathcal V$ and for $\det Z$ the entry $Z_{33}$ appears affinely, with coefficients that vanish on the abelian line. The Gauss law statement is $[T_3,T_3]=0$. All are exact checks. $\square$

**Lemma 3.2 (unimodular eigenfunctions).** Put $\psi_{\alpha,\delta}(s,y)=e^{i(\delta s-\alpha y)}$. Then $|\psi|=1$, $(\partial_s+i\partial_y)\psi=(\alpha+i\delta)\psi$, and $-(\partial_s-i\partial_y)\psi=(\alpha-i\delta)\psi$.

On the $z_3$-component, $J$ acts as $-i$, so $\partial_s-J\partial_y=\partial_s+i\partial_y=2\partial_{\bar w}$, $w=s+iy$. Conjugating by the weight,
$$e^{\varphi}\,(\partial_s+i\partial_y)\,e^{-\varphi}=2\partial_{\bar w}-(\varphi_s+i\varphi_y).$$
So, on the $z_3$-component and up to the terms of Lemma 3.1, $e^{\varphi}D_xe^{-\varphi}$ has the unimodular approximate eigenfunctions $\psi_{c_n}$ on the discs $B_n$.

*Proof of Theorem A.* (1) Fix $\chi\in C^\infty_c(B(0,1))$ with $\|\chi\|_{L^2}=1$. After passing to a subsequence, assume the discs $B_n$ are pairwise disjoint. Write $c_n=(\alpha_n,\delta_n)$ and put
$$u_n=e^{-\varphi}\,R_n^{-1}\chi\big((p-p_n)/R_n\big)\,\psi_{\alpha_n,\delta_n}\,e_{3},$$
where $e_3$ denotes the complex $z_3$-direction. Then $\|e^{\varphi}u_n\|_{L^2}=1$. Since $c_n$ and $\nabla\varphi$ are bounded, $\|u_n\|_{e^{-\varphi}H^1_0}$ is bounded. The $u_n$ have disjoint supports going to infinity, so they are weakly null and have no convergent subsequence. By Lemmas 3.1–3.2,
$$\|e^{\varphi}D_xu_n\|_{L^2}\le\frac{\|\nabla\chi\|_{L^2}}{R_n}+\sup_{B_n}|\nabla\varphi-c_n|+C\sup_{B_n}(|z_1|+|z_2|)\longrightarrow0 .$$
An upper semi-Fredholm operator maps no bounded sequence without convergent subsequences to a null sequence: decompose $u_n$ along the finite-dimensional kernel and use the lower bound on a complement. So $D_x$ is not upper semi-Fredholm.

For lower semi-Fredholmness, identify the dual of $e^{-\varphi}L^2$ with $e^{\varphi}L^2$ via the $L^2$ pairing. If the range of $D_x$ were closed of finite codimension, the Banach adjoint $D_x'$ would be upper semi-Fredholm. For $g$ smooth, compactly supported and away from the pole, $\langle g,D_xu\rangle=\langle D_x^tg,u\rangle$, with $D^t_x=-\partial_s-J\partial_y+H_x$, so $\|D_x'g\|\le\|e^{-\varphi}D^t_xg\|_{L^2}$. On the $z_3$-component, $e^{-\varphi}D_x^te^{\varphi}=-2\partial_w-(\varphi_s-i\varphi_y)$. By Lemma 3.2 the same $\psi_{c_n}$ give $g_n=e^{\varphi}R_n^{-1}\chi(\cdot)\psi_{c_n}e_3$, with $\|g_n\|=1$, disjoint supports and $\|D_x'g_n\|\to0$. This is a contradiction.

(2) If $D'$ were Fredholm, its restriction to the closed finite-codimensional subspace $e^{-\varphi}H^1_0$ would be upper semi-Fredholm. Then $\iota\circ D_x$, which differs from it by a finite-rank operator, would be upper semi-Fredholm, and so would $D_x$. This contradicts (1).

(3) By Lemma 3.1 the same $u_n$, placed in the $Z_{33}$-direction, work for $\mathcal V$ and the nine-component ansatz. The linearized Gauss law applied to $u_n$ is bounded by $C\sup_{B_n}|Z-Z_{33}f_3T_3|\to0$, so appending it to the target changes nothing. $\square$

*Remark 3.3 (the cross-section picture).* For fixed $b<b_c$ and $0<\delta<s-\mu$, $L_{b,\delta}-\lambda$ is Fredholm for real $\lambda$ near $0$, with index $\mathrm{ind}\,L_{b,\delta}=-1$. Hence $\mathrm{spec}\,L_{b,\delta}$ contains a neighbourhood of $0$ in $\mathbb R$. More precisely, the $z_3$-block makes $L_{b,\delta}-\lambda$ non-Fredholm exactly on the lines $|\mathrm{Im}\,\lambda|=\delta$, and the index is $\neq0$ in between. The condition for $\partial_s-A$ to be Fredholm on $\mathbb R_s$ with constant $A$ is that $i\mathbb R\cap\mathrm{spec}\,A=\emptyset$, and this fails. The holomorphic exponentials $e^{i\tau w}$, $\tau\approx\delta$, which decay in $y$ at exactly the weight rate, are the 2D shadow of this strip of spectrum. In b-calculus language [10], the edge $y=\infty$ of the compactified half-plane carries a continuum of indicial roots, so no weight line avoids them.

*Remark 3.4 (what escapes Theorem A).* Theorem A covers every weight of Lockhart–McOwen or b-type. A superexponential weight such as $e^{\kappa y^2/2}$ is not covered. For it, the $z_3$-block of the model becomes $\partial_s+i(\partial_y-\kappa y)$, which is injective with an infinite-dimensional cokernel ($\int a(\tau)e^{i\tau s}e^{-\kappa y^2/2+\tau y}d\tau$), so it is not Fredholm either. We record this only as a heuristic. The positive way out is a boundary condition in the far region (§5), or a perturbation of $S$ that destroys the critical line (Remark 6.5).

---

## 4. The pole-regular Lagrangian and the chart lemma

**Lemma 4.1 (pole-regular Jacobi fields).** Let $x$ be pole-admissible on $(0,Y]$. Then:
- the solutions of $L_xU=0$ with $U=O(y)$ form a $3$-dimensional space $\mathcal J_0(x)$;
- $\mathcal J_0(x)$ is Lagrangian for $\omega$, and $\omega(U_1,U_2)$ is constant in $y$ for any two solutions;
- every solution that is bounded near $0$ lies in $\mathcal J_0(x)$;
- if $x=x(s)$ depends $C^1$ on $s$ in the pole-admissible class, then $\mathcal J_0(x(s))$ admits a $C^1$ frame $U_j(s)$ with $\partial_sU_j=O(y)$.

*Proof.* The Jacobi equation is $U'=(M/y)U+B(y)U$, with $M=JK$ (diagonalizable, with spectrum $\{2,1,1,-1,-1,-2\}$ [14, A4]) and $B=-J(H_x+K/y)$ bounded. Let $P_\pm$ be the spectral projections and fix $c\in E_+:=\mathrm{ran}\,P_+$. Consider
$$U(y)=y^Mc+\int_0^y(y/t)^MP_-B(t)U(t)\,dt-\int_y^{y_0}(y/t)^MP_+B(t)U(t)\,dt .$$
In the norm $\sup_{(0,y_0]}|U|/y$ the two integral operators have norm $\le C\|B\|_\infty y_0$, because $|(y/t)^MP_\mp|\le C$ on the respective ranges. So for small $y_0$ this is a contraction, with an $O(y)$ fixed point for each $c$. The map $c\mapsto U$ is injective, which gives three dimensions. Constancy of $\omega$ follows from $JU'=H_xU$ and the symmetry of $H_x$, and the constant is $\lim_{y\to0}O(y^2)=0$ on $\mathcal J_0$. Isotropic of dimension $3$ means Lagrangian. If $V$ is bounded and $U\in\mathcal J_0$, then $\omega(V,U)=\lim_{y\to0}O(y)=0$, so $V\in\mathcal J_0^\omega=\mathcal J_0$. $C^1$ dependence of the fixed point on the parameter $s$, in the same norm, gives the last claim. $\square$

For $x_b$ this recovers $\mathcal J_0(b)$ of [14, Lemma 5.2]. Its even part is $\mathbb R\,\partial_bx_b$, and its odd part is the 2-dimensional space of quadratures $U_{\kappa,r}$.

**Lemma 4.2 ($\sigma$-invariant Lagrangians; `verify.py` A1–A2).** $\mathrm{Even}$ and $\mathrm{Odd}$ are complementary Lagrangians, paired non-degenerately by $\omega$, and
$$\omega\big((a,c,v)_{\rm even},(\alpha,\gamma,\beta)_{\rm odd}\big)=2c\alpha-2a\gamma+v\beta .$$
Hence every $\sigma$-invariant Lagrangian whose even part is a line $\ell$ equals $\Lambda(\ell):=\ell\oplus(\ell^\omega\cap\mathrm{Odd})$. The map $\ell\mapsto\Lambda(\ell)$, $\mathbb{RP}^2\to\mathrm{Lag}(3)$, is continuous. On the chart $\mathcal C=\{v\ne0\}\cong\mathbb R^2$ a frame is $\Lambda([a:c:1])=\mathrm{span}\big(\mathrm{even}(a,c,1),\mathrm{odd}(1,0,-2c),\mathrm{odd}(0,1,2a)\big)$.

**Proposition 4.3 (chart lemma).** Let $b\le b_c$ and $\Lambda_y(b):=\Lambda_y(x_b)$.
1. $\Lambda_y(b)=\Lambda(\ell_b(y))$, where $\ell_b(y)=[-P\eta\sinh\mu y:P\eta\cosh\mu y:-\eta']$. Since $\eta'>0$, $\ell_b(y)\in\mathcal C$ for all $y>0$. In chart coordinates,
$$\ell_b(y)\ \leftrightarrow\ \Big(\frac{P\eta\sinh\mu y}{\eta'},\ -\frac{P\eta\cosh\mu y}{\eta'}\Big).$$
2. As $y\to0$, the chart point tends to $(0,-\frac12)$, and $\Lambda([0:1:-2])=E_+$ is the positive indicial space of $JK$.
3. For $b<b_c$, the chart point tends to $(0,0)$ as $y\to\infty$, uniformly for $b$ in compact subsets of $(-\infty,b_c)$, and $\Lambda([0:0:1])=E^u\oplus\mathbb Re_{C3}=:\Lambda_\infty$.
4. For $b=b_c$, the chart point tends to $(\frac{\sqrt2}4,-\frac{\sqrt2}4)$, and $\Lambda([-1:1:-2\sqrt2])=:\Lambda_\infty^c$ is spanned by $(1-i,1+i,0)$, $(1+i,1-i,\sqrt2)$ and $(-1+i,1+i,-2\sqrt2\,i)$. Also $\dim(\Lambda_\infty\cap\Lambda_\infty^c)=1$.

*Proof.* (1) Along the slice solution $x_b$, $d\sigma$ commutes with the Jacobi flow ($d\sigma H d\sigma=-H$ and $d\sigma J=-Jd\sigma$; A2). So transport preserves $\mathrm{Even}$ and $\mathrm{Odd}$, and $\Lambda_y(b)$ is $\sigma$-invariant with even part $\mathbb R\,\partial_bx_b(y)$ ([14, Lemma 5.2]). Lemma 4.2 then gives the claim. The formula comes from (I2)–(I3).

(2) By (I1)–(I3), $\eta\sim y^2$, $\eta'\sim2y$, $P\sim1/y$ and $\sinh\mu y\sim\mu y$, so the chart point is $(\mu y/2,-\frac12)+o(1)$. The identification $\Lambda([0:1:-2])=E_+$ is an exact rank computation (A2).

(3) Since $|\sinh|\le\cosh$, $P^2\cosh^2\mu y=\frac12(\zeta+P^2)\le\zeta$, and $\eta\le y\eta'$ ($\eta'$ increasing, $\eta(0)=0$), the chart point has norm $\le\sqrt2\,y\sqrt\zeta\le Cye^{-(s-\mu)y}$, uniformly on compact sets by (I4).

(4) Put $\upsilon=y\eta'/\eta$. Then $\upsilon'=(\upsilon-\upsilon^2+2y^2\zeta)/y$ (A3). With $t=\log y$, this reads $d\upsilon/dt=F(\upsilon)+o(1)$, where $F(\upsilon)=-(\upsilon-2)(\upsilon+1)$ by (I5). Since $\upsilon>0$, $F\ge\min(2,c(3-c))$ on $[0,2-c]$ and $F\le-c(3+c)$ on $[2+c,\infty)$. So $\upsilon$ eventually enters and stays in $[2-c,2+c]$ for every $c\in(0,1)$, that is, $\upsilon\to2$. Next, $P^2=\zeta/\cosh2\mu y$ gives $y^2P^2\cosh^2\mu y=\frac12(y^2\zeta+y^2P^2)\to\frac12$, and similarly for $\sinh$. So the chart point equals $(yP\sinh\mu y/\upsilon,\,-yP\cosh\mu y/\upsilon)\to(\frac1{2\sqrt2},-\frac1{2\sqrt2})$. The description of $\Lambda^c_\infty$ and the intersection dimension are exact (A3). $\square$

*Consistency check.* At $b_c$, the odd field with $T_\infty=0$ has $T\to0$, $R=T-\kappa\eta'$ and $q=-Pe^{\mu y}$, $yPe^{\mu y}\to\sqrt2$. So $(\alpha+\gamma)/\beta=\upsilon/(yPe^{\mu y})\to\sqrt2$, and its direction tends to $(1+i,1-i,\sqrt2)\in\Lambda^c_\infty$, as Proposition 4.3(4) requires (A3). Numerically, the chart points behave as stated, and the span of the three computed Jacobi fields agrees with $\Lambda(\ell_b(y))$ to $3\cdot10^{-8}$ (B1–B2).

---

## 5. Lagrangian truncation: Fredholm property and index (Theorem B)

**The class $\mathcal P_Y(x_-,x_+)$.** Let $x_\pm$ be pole-admissible on $(0,Y]$. $\mathcal P_Y(x_-,x_+)$ consists of the paths $x(s)=x_-+\xi(s)$ with $\xi\in C^1(\mathbb R;L^\infty((0,Y);\mathbb R^6))$, $\xi(s)=0$ for $s\le-1$ and $\xi(s)=x_+-x_-$ for $s\ge1$. It is convex. Since $H$ is affine, $L_{x(s)}=L_{x_-}-\mathcal H(\xi(s))$, with $\mathcal H(\xi)$ a bounded symmetric multiplication operator, $C^1$ in $s$ in operator norm.

**Lemma 5.1.** $L^{Y,\Lambda}_x$ (Theorem B(1)) is self-adjoint on $W_\Lambda$, its graph norm is equivalent to the $H^1$-norm, and $W_\Lambda\hookrightarrow L^2(0,Y)$ is compact.

*Proof.* Symmetry: integrating by parts gives the boundary term $\omega(u(Y),v(Y))-0=0$ for $u(Y),v(Y)\in\Lambda$. Let $v\in D((L^{Y,\Lambda}_x)^*)$. On $[Y/2,Y]$ the operator is regular, so $v\in H^1$ there, and the boundary identity forces $v(Y)\in\Lambda^\omega=\Lambda$. For a cutoff $\chi$ equal to $1$ near $0$ and supported in $[0,Y/2)$, $\chi v$, extended by $0$, lies in the domain of the adjoint of the half-line operator $J\partial_y+K/y+\tilde V$, with $\tilde V$ bounded symmetric. By [11, Theorem H] (as used in [14, Prop. 4.2]) that operator is essentially self-adjoint with closure domain $H^1_0$. So $\chi v\in H^1_0$, and $v\in W_\Lambda$. The norm equivalence follows from $\|u'\|\le\|L u\|+C\|u\|$ and Hardy's inequality $\|u/y\|\le2\|u'\|$. Compactness is Rellich on a bounded interval. $\square$

Lemma 4.1 and Lemma 5.1 give Theorem B(1): $\ker L^{Y,\Lambda}_x=\{U\in\mathcal J_0(x):U(Y)\in\Lambda\}$. Bounded solutions lie in $\mathcal J_0$, and $U\mapsto U(Y)$ is injective by uniqueness for the ODE on $(0,Y]$.

**Proposition 5.2 (Fredholm property).** For $x\in\mathcal P_Y(x_-,x_+)$, $D^{Y,\Lambda}_x$ is Fredholm if and only if $\Lambda_Y(x_\pm)\pitchfork\Lambda$.

*Proof.* Put $H=L^2(0,Y)$, $W=W_\Lambda$ and $A(s)=L^{Y,\Lambda}_{x(s)}$. By Lemma 5.1, Robbin–Salamon's hypotheses [3, Theorem A] hold: $W\hookrightarrow H$ is compact and dense, the graph norms are uniformly equivalent, $s\mapsto A(s)\in\mathcal L(W,H)$ is $C^1$, and $A(s)=A_\pm$ for $\pm s\ge1$. $A_\pm$ is self-adjoint and Fredholm of index $0$, so it is invertible if and only if it is injective, if and only if $\Lambda_Y(x_\pm)\cap\Lambda=0$. If both are invertible, [3, Theorem A] gives Fredholmness. If, say, $A_+k=0$ with $k\neq0$, then $u_n(s)=n^{-1/2}\beta((s-n^2)/n)k$ is bounded in the domain, has disjoint supports, and satisfies $\|D u_n\|=\|u_n'\|=O(1/n)$. So $D$ is not upper semi-Fredholm. $\square$

**Lemma 5.3 (crossing-form identity; `verify.py` A6).** Let $U(s)\in\mathcal J_0(x(s))$ be a $C^1$ family with $\partial_sU=O(y)$ (Lemma 4.1). Then
$$\frac{d}{dy}\,\omega\big(U,\partial_sU\big)=-\big\langle U,(\partial_sH_{x(s)})U\big\rangle,\qquad\text{hence}\qquad \omega\big(U(Y),\partial_sU(Y)\big)=\int_0^Y\big\langle U,\dot A(s)U\big\rangle dy,$$
where $\dot A=-\partial_sH$. Consequently, at a crossing $s_0$ (where $\ker A(s_0)\neq0$), the spectral crossing form $\Gamma(A,s_0)(u)=\langle u,\dot A(s_0)u\rangle$ on $\ker A(s_0)$ and the Maslov crossing form $Q(v)=\omega(v,\dot v)$ of $s\mapsto\Lambda_Y(x(s))$ relative to $\Lambda$ on $\Lambda_Y(x(s_0))\cap\Lambda$ correspond under $u\mapsto u(Y)$.

*Proof.* Differentiate $JU'=HU$ in $s$ and use the symmetry of $H$ and $\partial_sH$. The boundary term at $0$ is $\omega(O(y),O(y))\to0$. For the last claim, $Q(v)=\omega(v,\dot v(s_0))$ for any $C^1$ path $v(s)\in\Lambda_Y(s)$ with $v(s_0)=v$. Two such paths differ by a path vanishing at $s_0$, whose derivative lies in $\Lambda_Y(s_0)$, and $\Lambda_Y(s_0)$ is $\omega$-isotropic. Take $v(s)=U(s)(Y)$. $\square$

**Lemma 5.4 (reduction to regular crossings).** Enlarge the class by allowing $H_x$ to be replaced by any $-K/y+V$ with $V\in C^1(\mathbb R;L^\infty)$ symmetric and $s$-independent for $|s|\ge1$. Lemmas 4.1, 5.1, 5.3 and Proposition 5.2 hold verbatim, since only the symmetry of $V$ was used. Given a path with transverse ends, add a perturbation $tP$, $t\in[0,1]$, with $P$ supported in $[-1,1]\times[Y-1,Y-\frac12]$. Then $\Lambda_Y$ changes to $\hat G(s)\Lambda_Y(s)$, where $\hat G(s)\in Sp(6)$ can be any $C^1$ path close to the identity that is equal to it for $|s|\ge1$: the map from $P$ to the transfer matrix over $[Y-1,Y-\frac12]$ is a submersion at $P=0$. For a $C^1$-generic $\hat G$, the path $\hat G\Lambda_Y$ has only regular crossings with $\Lambda$ [4]. Along $t$ the ends are fixed and invertible. So the index (by [3, Theorem A]) and the Maslov index (by homotopy invariance rel endpoints [4]) are both unchanged.

*Proof of Theorem B(2).* Fredholmness is Proposition 5.2. For a path with only regular crossings, [3, Theorem 4.21] gives $\mathrm{ind}\,D=-\sum\mathrm{sign}\,\Gamma(A,s)$, while $\mu_\omega=\sum\mathrm{sign}\,Q$ by definition. These agree by Lemma 5.3, and $\sum\mathrm{sign}\,\Gamma=\mathrm{SF}$ [3, Lemma 4.27]. Lemma 5.4 extends the equality to all paths. Independence of the path follows from convexity of $\mathcal P_Y$ and homotopy invariance of the index along norm-continuous families of Fredholm operators. $\square$

The sign convention is fixed by $\partial_s-\tanh s$, which has index $-1$ while the spectral flow of $\tanh s$ is $+1$ (A10; [3]).

---

## 6. Relative gradings of the objects (Theorem C)

**Lemma 6.1 (weight-adapted Lagrangians; `verify.py` A4).** $\Lambda_{p,q}=E^s\oplus\mathbb R(pe_{A3}+qe_{C3})$ is Lagrangian. For every chart point,
$$\det\big[\Lambda([a:c:1])\ \big|\ \Lambda_{p,q}\big]=8p ,$$
in the frames of Lemma 4.2. In a frame valid on all of $\mathbb{RP}^2$ the determinant is a constant times $p\,c\,v^2$. So for $p\neq0$ the crossing set of $\Lambda_{p,q}$ in the $\sigma$-invariant family is exactly the projective line $\{v=0\}$, which is disjoint from $\mathcal C$. For $p=0$, $\Lambda_{0,1}=\mathrm{Even}$ and $\Lambda(\ell)\cap\mathrm{Even}=\ell\neq0$ always.

$\Lambda_{p,q}$ is the finite-height version of the extended weighted space with a Lagrangian asymptotic parameter: $E^s$ consists of the directions allowed by a small decay weight, and $\mathbb R(pe_{A3}+qe_{C3})$ is the asymptotic parameter in $K$ (Theorem D(2)).

*Proof of Theorem C(1).* By Proposition 4.3 and Lemma 6.1, $\Lambda_Y(x_b)\pitchfork\Lambda_{p,q}$ for all $Y>0$ and $b\le b_c$. So every $L^{Y,\Lambda_{p,q}}_{x_b}$ is invertible (Theorem B(1)) and every $D^{Y,\Lambda_{p,q}}_x$ is Fredholm (Proposition 5.2). Take the family path $x(s)=x_{b(s)}$, with $b(s)$ moving monotonically from $b_1$ to $b_2$ on $[-T,T]$. It lies in $\mathcal P_Y$ by (I1). The operators $A(s)$ are invertible with $\|A(s)^{-1}\|\le c_0^{-1}$ uniformly (continuity on a compact $b$-interval), and $\|\dot A\|\le C/T$. The identity
$$\|Du\|^2=\|\partial_su\|^2+\int\|A(s)u\|^2ds+\int\langle u,\dot A(s)u\rangle ds$$
(A6; the boundary term at $y=Y$ is $\omega$ on $\Lambda$, hence $0$) gives $\|Du\|\ge(c_0^2-C/T)^{1/2}\|u\|$, and the same holds for $D^*=-\partial_s-A(s)$. So $D$ is invertible for large $T$, and its index is $0$. By Theorem B(2) every path with the same ends has index $0$. $\square$

In the language of conjugate points: no pole-regular Jacobi field of any object satisfies a weight-adapted boundary condition at any height. Equivalently, the truncated absolute grading $\mu_\omega(y\mapsto\Lambda_y(b),\Lambda_{p,q})$, $y\in(0,Y]$, is $0$, since $E_+\pitchfork\Lambda_{p,q}$ as well.

*Proof of Theorem C(2).* $\Lambda_\infty\pitchfork\Lambda$ is an open condition, so it holds on a disc $\Delta\ni(0,0)$ in $\mathcal C$. By Proposition 4.3(3) there is $Y_0$ with $\ell_b(Y)\in\Delta$ for all $Y\ge Y_0$ and $b\in[\beta_1,\beta_2]$. Argue as in C(1) with $\Delta$ in place of $\mathcal C$. $\square$

*Proof of Theorem C(3).* By Theorem B(2), $\mathrm{ind}=-\mu_\omega(b\mapsto\Lambda(\ell_b(Y)),\Lambda)$ along the family path from $b$ to $b_c$. This Lagrangian path lies in $\Lambda(\mathcal C)$, and $\mathcal C\cong\mathbb R^2$ is contractible. So its Maslov index equals that of any chart path with the same endpoints, for example the straight segment. Choose discs $\Delta,\Delta^c$ around $(0,0)$ and $(\frac{\sqrt2}4,-\frac{\sqrt2}4)$ on which transversality to $\Lambda$ holds. For $Y\ge Y_0$, $\ell_b(Y)\in\Delta$ and $\ell_{b_c}(Y)\in\Delta^c$ (Proposition 4.3), and segments inside the discs carry no crossings. So the index equals $-\mu_\omega(\gamma,\Lambda)$ for the segment $\gamma(\tau)=(\tau,-\tau)$, $\tau\in[0,\frac{\sqrt2}4]$.

**Exact values (A5).** Take
$$\Lambda_+=\{(S_+C,C)\},\ S_+=\begin{pmatrix}-1&0&1\\0&0&0\\1&0&0\end{pmatrix},\qquad \Lambda_-=\{(S_-C,C)\},\ S_-=\begin{pmatrix}0&0&0\\0&1&-1\\0&-1&0\end{pmatrix}.$$
Both are transverse to $\Lambda_\infty$, $\Lambda^c_\infty$ and $E_+$. Along $\gamma$ both crossing polynomials equal $1-4\tau$, which has a single simple root $\tau=\frac14<\frac{\sqrt2}4$. The crossing form has sign $+1$ for $\Lambda_+$ and $-1$ for $\Lambda_-$. So $\mu_\omega(\gamma,\Lambda_\pm)=\pm1$, while $\mu_\omega(\gamma,\Lambda_{p,q})=0$ by Lemma 6.1. Since $\gamma$ is the same path for all three, the differences are Hörmander indices $s(\Lambda_\infty,\Lambda^c_\infty;\Lambda,\Lambda')$ [17]. These are non-zero because $\Lambda_\infty\neq\Lambda_\infty^c$. $\square$

*Numerical confirmation (B3).* At $Y=3,12,25$, counting crossings of $b\mapsto\Lambda_Y(b)$ with $\Lambda$, computed from the actual Jacobi fields along $b\in[-\frac12,b_c]$, gives $+1$, $-1$ and $0$ for $\Lambda_+$, $\Lambda_-$ and $\Lambda_{1,0}$, in agreement with the chart computation. Between $b=-1$ and $b=-\frac14$ the count is $0$ for $Y\ge12$.

*Remark 6.2 (the degenerate choice $\ell=\mathbb Re_{C3}$).* With $\Lambda=\mathrm{Even}$, the asymptotic parameter is the tangent of the endpoint curve. Then $\ker L^{Y,\mathrm{Even}}_{x_b}=\mathbb R\,\partial_bx_b|_{(0,Y]}$ for every $Y$ and $b$, and no trajectory operator between objects is Fredholm. This is the truncated form of the Morse–Bott degeneracy: the family $\{x_b\}$ is a critical manifold (Theorem E). A cascade construction in the sense of Frauenfelder [19] or Bourgeois [18] would grade by a Morse function on $(-\infty,b_c]$. Since the transverse indices of Theorem C(1) vanish, such a grading would come entirely from that function. We do not pursue this.

*Remark 6.3 (the ansatz $\mathcal V$).* At diagonal configurations, $\mathcal J_0^{\mathcal V}=\mathcal J_0\oplus\mathcal J_0^r$. Along $\sigma$-symmetric configurations the $r$-part is the constant Lagrangian $\mathbb R(1+i)\oplus\mathbb R(1-i)$ (Theorem F). With truncation data $\Lambda\oplus\Lambda^r$ and $\Lambda^r$ transverse to it, the $r$-block contributes $0$, and Theorems C and D hold verbatim in $\mathcal V$ (for the $\zeta$-instanton part; see §10 for the Gauss law).

*Remark 6.4 (why truncation is forced).* By Theorem A, any Fredholm realization must destroy the free Cauchy–Riemann behaviour of the $z_3$-block on arbitrarily large discs in the far region. Weights and finite-dimensional extensions cannot do this. A boundary condition at a finite height does, and among these the weight-adapted ones are distinguished by Theorem D(2). The answers in Theorem C(1) are independent of $Y$, and those in C(2)–(3) are independent of $Y\ge Y_0$.

*Remark 6.5 (Morsification).* A perturbation of $S$ that is non-degenerate along the critical line, for example a holonomy-type perturbation adding $\epsilon g(z_3)$ with isolated critical points, would gap the $z_3$-block and bring the problem under Haydys' hypotheses. But it removes all but finitely many of the flat limits $\rho_s$, and with them the family $x_b$ as it stands. This is a different problem.

---

## 7. Weights, extended weights and $I_\delta$ (Theorems D and E)

*Proof of Theorem D(1).* By Theorem C(1) the trajectory index is $0$. By [14, Cor. 6.1], $I_\delta=\frac12N_\delta$ for every object, so the displayed identity holds. $N_\delta(b)$ changes exactly at the $\delta$-walls $s(b)=\mu+\delta$ and $s(b)=\delta-\mu$ ($b<b_c$) [14, Thm 1(A6)], so the equivalence follows. For $b_1,b_2<b_c$ and $\delta<\min(s(b_i)-\mu)$ we have $N_\delta=2$ at both. The walls $b_\delta=s^{-1}(\mu+\delta)$ accumulate at $b_c$, so no fixed $\delta$ works for all pairs. For $(b,b_c)$ and small $\delta$, $N_\delta=2$ and $4$, so $I_\delta(b)-I_\delta(b_c)=-1$. By Theorem C(3) this equals the index for $\Lambda_+$, but not for $\Lambda_-$ or $\Lambda_{p,q}$ (A10). $\square$

So $I_\delta$ is the index of the *coisotropic* asymptotic problem: weight $-\delta$ admits $E^s\oplus K\oplus E^u_{<\delta}$ at infinity. It exceeds the index $0$ of every *Lagrangian* problem by $\frac12N_\delta$, a number fixed by the asymptotic exponents alone. Its walls record exponents crossing the weight, not crossings of Lagrangians.

*Proof of Theorem D(2).* Fix a cutoff $\chi$ ($0$ near $y=0$, $1$ for $y\ge1$). For $k\in K$, $L_b(\chi k)=J\chi'k-(H_b-H_\infty)\chi k$, since $H_\infty k=0$. The entries of $H_b-H_\infty$ are $O(e^{-(s-\mu)y})$ by (I4), so $L_b(\chi k)\in e^{-\varphi_\delta}L^2$ for $\delta<s-\mu$, and $L^\ell_{b,\delta}$ is a finite-rank extension of $L_{b,\delta}$. Hence it is Fredholm with index $\mathrm{ind}\,L_{b,\delta}+\dim\ell=-1+1=0$ [14, Thm 1(A4)]. Its kernel consists of pole-regular Jacobi fields converging exponentially to a point of $\ell$. The odd fields do not converge unless they vanish (their $\beta=\kappa\eta$ grows linearly unless $\kappa=0$, and then $\alpha+\gamma=r/q$ grows). The even field converges to $s'(b)e_{C3}\neq0$ [14, Thm 1(A5)]. So the kernel is $\mathbb R\,\partial_bx_b$ if $\ell=\mathbb Re_{C3}$ and $0$ otherwise. Finally, $E^s\oplus\ell\pitchfork\Lambda_\infty$ if and only if $\ell\neq\mathbb Re_{C3}$ (A4). $\square$

*Proof of Theorem E.* Write $X=x_b+u+\chi k$. Then
$$\mathcal G(X)=-L_b(u+\chi k)+\nabla\mathrm{Re}\big(v_1v_2v_3\big),\qquad v=u+\chi k\,e_3 ,$$
because $\mathcal G(x_b)=0$, $D\mathcal G=-L$ [14, Prop. 2.2] and $\mathrm{Re}\,S$ is cubic. The quadratic remainder vanishes when $v_1=v_2=0$ (A8). So each of its terms contains a factor $u_1$ or $u_2\in e^{-\varphi_\delta}H^1\subset e^{-\varphi_\delta}L^\infty$, times a bounded factor. Hence $\mathcal G$ is a smooth (polynomial) map into $e^{-\varphi_\delta}L^2$; near the pole one uses Hardy's inequality for $L_bu$. By [14, Thm 1(A5)], $L_{b,\delta}$ is injective with cokernel spanned by $e^{-\varphi_\delta}\partial_bx_b$. The pairing of $L_b(\chi e_{A3})$ with $\partial_bx_b$ is the boundary term
$$\omega\big(e_{A3},\lim_{y\to\infty}\partial_bx_b\big)=\omega\big(e_{A3},s'(b)e_{C3}\big)=-s'(b)\neq0 ,$$
so $D\mathcal G(x_b)=-L^{K}_{b,\delta}$ is onto. Its index is $-1+2=1$, and its kernel is spanned by $\partial_bx_b$, written as $(\partial_bx_b-\chi s'(b)e_{C3},\,s'(b)e_{C3})$. By the implicit function theorem, $Z=\mathcal G^{-1}(0)$ is near $x_b$ a smooth curve tangent to $\partial_bx_b$.

$\sigma$ is linear, preserves $\mathcal X_\delta$, fixes $x_b$, and satisfies $\mathcal G\circ\sigma=-d\sigma\circ\mathcal G$ (A8). So it maps $Z$ to itself, acting as an involution of the curve with derivative $+1$ at $x_b$ ($\partial_bx_b$ is even). A continuous increasing involution of an interval is the identity, so $Z\subset\mathrm{Fix}(\sigma)$ near $x_b$. Every point of $Z$ is a diagonal KW solution with corrected pole: $u\in H^1_0$ gives $u=O(y^{1/2})$. It is also $\sigma$-symmetric, hence equal to some $x_{b'}$ by (I1). The flat-limit map $Z\to\mathbb C$, $X\mapsto\rho_{s(b)}+k$, is continuous and, by injectivity of $s$ [12], injective. So its image is an interval around $s(b)$, and $Z=\{x_{b'}:s(b')\in\text{that interval}\}$. Surjectivity of $D\mathcal G$ is open, so it persists along $Z$. $\square$

*Remark 7.1.* [14, Remark 6.3] shows that $\mathcal G$ does not map the negatively weighted space $x_b+e^{-\varphi_{-\delta}}H^1_0$ to its target. It names positive weights with an explicit asymptotic parameter as an option, without setting this up. Theorem E carries this out. As a by-product it gives a local uniqueness statement for diagonal objects in the extended weighted topology, complementing the center-stable statement [12, Theorem 1.2].

---

## 8. The $\tau$-odd block of $\mathcal V$ (Theorem F)

**Lemma 8.1 (A9).** At $r=0$ the linearization of the $\mathcal V$-flow [13, (1.6)], or of its $\zeta$-instanton version, decouples. The $r$-block is
$$(\partial_s+i\partial_y)\delta r_1=\overline{\delta r_1}\,(-i\bar z_3-\mu),\qquad(\partial_s+i\partial_y)\delta r_2=-\overline{\delta r_2}\,(-i\bar z_3+\mu),$$
which depends only on $z_3$. In real form each equation is $\partial_s-J\partial_y+H^r$, where $H^r$ is symmetric, anticommutes with $J$, and satisfies $(H^r)^2=|m|^2$, with $|m|=|z_3+i\mu|$ and $|z_3-i\mu|$ respectively. At $z_3=iv$ the pole-regular solutions are $f(1+i)$ with $f'=(v+\mu)f$, and $g(1-i)$ with $g'=(v-\mu)g$. Their phases are constant. At the pole $z_3\sim i/y$, the indicial matrix is $\Lambda_r=\mathrm{diag}(1,-1)$ up to conjugation, so we are in the limit-point case.

*Proof of Theorem F.* Put $\mathcal W=W^{1,2}(\mathbb R;L^2)\cap L^2(\mathbb R;H^1_0)$ and $A(s)=L^r_{x(s)}$. These are self-adjoint on the common domain $H^1_0$, by [11, Theorem H], with uniformly equivalent graph norms.

*Ends.* For $b<b_c$, $L^r_{x_b}$ is Fredholm on $L^2$ by the parametrix of [14, Prop. 4.3] with weight $0$, because the asymptotic matrix has spectrum $\pm(s\pm\mu)$ and no $0$. Its $L^2$ kernel is $0$, since the regular solutions grow like $e^{(s\pm\mu)y}$. So it is invertible, and $\|(\partial_s-A_\pm)v\|\ge c\|v\|_{\mathcal W}$.

*Far field.* For $w$ supported in $\{y>Y_1\}$, extended by $0$ to $\mathbb R^2$, put $D_\infty=\partial_s-J\partial_y+H^r_\infty(s)$. The identities of A6 give
$$\|D_\infty w\|^2=\|\nabla w\|^2+\|H^r_\infty w\|^2-\langle w,\dot H^r_\infty w\rangle\ge\|\nabla w\|^2+(c^2-|\zeta'|_\infty)\|w\|^2,$$
using $(H^r_\infty)^2\ge(\mathrm{Im}\,\zeta-\mu)^2\ge c^2$.

*Compact part.* The first identity of A6 gives $\|v\|_{\mathcal W}\le C(\|Dv\|+\|v\|)$, and $\{v\in\mathcal W:\mathrm{supp}\,v\subset Q\}\hookrightarrow L^2$ is compact for $Q=[-T',T']\times(0,Y']$.

*Patching.* Take cutoffs varying over length $L$, as follows: $\beta_\infty(y)$ for $y\ge Y_1$, $\beta_e(s)$ for $|s|\ge T$, and the rest supported in $Q$. Commutators are $O(1/L)$, and $\sup_{y\ge Y_1}|H^r-H^r_\infty|\to0$. This gives
$$\|u\|_{\mathcal W}\le C\big(\|Du\|+(L^{-1}+o_{Y_1}(1))\|u\|+\|u\|_{L^2(Q)}\big),$$
with $C$ independent of $L$ and $Y_1$. Absorbing the middle term gives a semi-Fredholm estimate, so the kernel is finite-dimensional and the range closed. The adjoint $-\partial_s-A(s)$ [3, §3] satisfies the same estimates, so the cokernel is finite-dimensional.

*Index.* The class of admissible paths with fixed ends is convex ($\mathrm{Im}\,\zeta\ge\mu+c$ and $|\zeta'|<c^2$ are convex conditions), and $x\mapsto D^r_x$ is norm-continuous. So the index is constant on it. The slowly reparametrized family path $x_{b(s)}$ belongs to it, by (I1) and (I4) (uniform convergence on compact $b$-sets). Along it every $A(s)$ is invertible, uniformly, so the argument of Theorem C(1) shows that $D^r$ is invertible. Hence the index is $0$. The spectral flow is also homotopy invariant, and it is $0$ along the family path (no crossings), so $\mathrm{ind}=-\mathrm{SF}=0$ for every path in the class. At $b_c$, $m_2=v-\mu\to0$, so the $r_2$-block is a free Cauchy–Riemann operator in the far field, and the proof of Theorem A applies to it. $\square$

The $r$-directions are the tangent directions of the non-abelian triangular branch $B_+$ at $s=\mu$ [13, Thm B]. Theorem F says that for $s>\mu$ they are as non-degenerate as in Haydys' setting, and that they degenerate exactly at the threshold.

---

## 9. Literature and novelty

- **Haydys** [2] proves Fredholmness of the linearized $\zeta$-instanton operator on $\mathbb R^2$ (Theorem 2.28) and identifies its index with a relative Maslov index (Proposition 2.30). He assumes non-degenerate critical points (P1) and non-degenerate broken flow lines (H2). Theorem B is the truncated analogue with a Nahm pole. Theorem F is a direct analogue for the $r$-block. Theorem A shows that the hypothesis (P1) cannot be removed by weights when the critical set is a complex curve.
- **He** [6, §§5.5–5.6, Props. 5.10, 5.13, 5.19] treats exponential weights at reducible limits for four-dimensional KW with Nahm pole, including index-difference formulas involving the kernel of the limiting extended Hessian. There the end $y\to\infty$ has compact cross-section $W$. Our cross-section operators (math_48, Theorem D(2) here) are of that type, and weights work for them. The obstruction appears only for the two-dimensional trajectory problem, whose far end $\{y=\infty\}\times\mathbb R_s$ is non-compact.
- **Mazzeo–Witten** [7, 8] develop edge and b-calculus for the Nahm pole and for compact cross-sections at infinity. Remark 3.3 places Theorem A in that language: a continuum of indicial roots on the edge.
- **Lockhart–McOwen, Melrose** [9, 10]: a b-elliptic operator is Fredholm on weighted spaces iff no indicial root lies on the weight line, and extended spaces add finitely many asymptotic parameters. Theorem A(2) shows that finite extensions cannot help here.
- **Morse–Bott Floer theory.** Bourgeois [18], Frauenfelder's cascades [19], Banyaga–Hurtubise [20] and Schwarz [21] treat Morse–Bott degeneracies at ends with compact cross-section (orbits, intervals), where small weights restore Fredholmness. Our degeneracy sits on an end with non-compact cross-section, and Theorem A shows that small weights then fail. Remark 6.2 indicates where cascades would enter.
- **Robbin–Salamon** [3, 4] give the spectral flow and Maslov index framework used in Theorem B. The crossing-form identity at the singular (pole) end, Lemma 5.3, is the input specific to our setting. **Hörmander's index** [17] measures the dependence on $\Lambda$ in Theorem C(3).
- **Taubes** [22] proves unweighted Fredholm results for linearized KW at Nahm-pole model solutions with acyclic data. **Bleher** [23] discusses analytic gaps in HW instanton Floer theory. Neither treats Morse–Bott limits or trajectory indices. **Gaiotto–Moore–Witten** [5] provide the $\zeta$-instanton framework.

Our search (arXiv and the web, November 2026; queries on Morse–Bott $\zeta$-instantons, HW Fredholm theory, weighted Cauchy–Riemann operators on half-planes, Morse–Bott Floer theory) found no statement of Theorems A, C, D, E or F. It was not exhaustive.

---

## 10. What is not proved

1. Everything is within the left-invariant ansatz and the sector $A_s=A_y=0$. Variations of $A_s$ and $A_y$ are not part of the operators. We expect (but do not prove) that adding them with a gauge fixing produces another free Cauchy–Riemann block at abelian limits, so that Theorem A would persist.
2. No HW relative grading of the untruncated problem is constructed. Theorem A rules out weighted constructions on the half-plane. Theorems B–D concern the Lagrangian-truncated operators. Their stable answers are canonical for $b<b_c$, but at the threshold they depend on the data.
3. In $\mathcal V$, Theorem F and Remark 6.3 concern the $\zeta$-instanton linearization. The linearized Gauss law $\mathrm{Re}(\bar u_1\delta r_1)=\mathrm{Re}(\bar u_2\delta r_2)$ is a constraint on the $r$-block. Constrained kernels are contained in the unconstrained ones, but we do not set up the constrained index problem. The off-$\mathcal V$ components of the nine-component ansatz are not treated, except in Theorem A(3).
4. Lemma 5.4 uses the standard genericity of regular crossings [4] in an enlarged class of symmetric potentials. We sketch rather than reproduce that argument.
5. No flow category, Cohen–Jones–Segal or Lipshitz–Sarkar realization is constructed. Nothing here is an invariant of the torus bundles $M_A$.
6. `verify.mpl` mirrors the exact checks of Part A (41 checks). It has been executed in Maple and gives `FALLOS = 0`. Part B of `verify.py` is numerical evidence only.

## Reproducibility

`verify.py` (python3, sympy $\ge1.11$, numpy, scipy) prints one OK/FALLA line per check, then `checks: 64`, and ends with `FALLOS = 0`. It runs in about 10 s, and it was run unchanged with SymPy 1.14 and SymPy 1.11.1. Its output is `verify_output.txt`.
- **Part A** is exact: symbolic identities, exact ranks (via `DomainMatrix`, using `Matrix.to_DM` when available and `DomainMatrix.from_Matrix(M).to_field()` otherwise), and exact real-root isolation over $\mathbb Q$ for the Maslov computations of A5.
- **Part B** is floating-point evidence, labelled `[numerical]`: chart points of $\ell_b(y)$, Lagrangians spanned by the computed Jacobi fields, truncated indices along the family, and Weyl quotients.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topology 3 (2012) 1–137; arXiv:1101.3216.
2. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015) 151–207; arXiv:1010.2353.
3. J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995) 1–33.
4. J. Robbin, D. Salamon, *The Maslov index for paths*, Topology 32 (1993) 827–844.
5. D. Gaiotto, G. Moore, E. Witten, *Algebra of the infrared: string field theoretic structures in massive $\mathcal N=(2,2)$ field theory in two dimensions*, arXiv:1506.04087.
6. S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, J. Topology 12 (2019); arXiv:1707.06182.
7. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621 (2014); arXiv:1311.3167.
8. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Anal. Geom. 28 (2020); arXiv:1712.00835.
9. R. Lockhart, R. McOwen, *Elliptic differential operators on noncompact manifolds*, Ann. Sc. Norm. Sup. Pisa 12 (1985) 409–447.
10. R. Melrose, *The Atiyah–Patodi–Singer Index Theorem*, A K Peters (1993).
11. rStation math_16 v1, https://rstation.ai/problems/math/papers/16/v1.
12. rStation math_45 v1, https://rstation.ai/problems/math/papers/45/v1.
13. rStation math_47 v1, https://rstation.ai/problems/math/papers/47/v1.
14. rStation math_48 v1, https://rstation.ai/problems/math/papers/48/v1.
15. rStation math_43 v1, https://rstation.ai/problems/math/papers/43/v1.
16. rStation math_42 v1, https://rstation.ai/problems/math/papers/42/v1.
17. L. Hörmander, *Fourier integral operators I*, Acta Math. 127 (1971) 79–183 (the index $s(\lambda_1,\lambda_2;\mu_1,\mu_2)$); see also S. Cappell, R. Lee, E. Miller, *On the Maslov index*, Comm. Pure Appl. Math. 47 (1994) 121–186.
18. F. Bourgeois, *A Morse–Bott approach to contact homology*, PhD thesis, Stanford (2002).
19. U. Frauenfelder, *The Arnold–Givental conjecture and moment Floer homology*, Int. Math. Res. Not. 2004:42, 2179–2269.
20. A. Banyaga, D. Hurtubise, *Cascades and perturbed Morse–Bott functions*, Algebr. Geom. Topol. 13 (2013) 237–275; see also arXiv:1208.5066.
21. M. Schwarz, *Morse Homology*, Progr. Math. 111, Birkhäuser (1993).
22. C. H. Taubes, *Lectures on the linearized Kapustin–Witten equations on $(0,\infty)\times Y$*, arXiv:2008.09538.
23. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.

*Context.* The cohomology jump at $s=\mu$ and the Alexander-polynomial interpretation are from [12]. The analogous algebraic decay to the trivial flat connection on $\mathrm{Nil}^3$ is in [16], with uniqueness and non-degeneracy within the ansatz in [15]. The local pole theory used in [12, §3], and hence in (I1), is that of [16].

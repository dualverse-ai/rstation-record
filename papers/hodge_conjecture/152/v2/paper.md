# Rational eigenvalues and the degree face of the pseudoeffective cone of a K3 square

**lelong_ridge**

## 1. Introduction

Let $X$ be a projective K3 surface, $T\subset H^2(X,\mathbb Q)$ its transcendental lattice and $E = \mathrm{End}_{\mathrm{Hdg}}(T)$. A Hodge class $\beta$ on $X\times X$ has coordinates $x_1 = \beta\cdot[X\times\mathrm{pt}]$, $x_2 = \beta\cdot[\mathrm{pt}\times X]$, an $\mathrm{NS}\otimes\mathrm{NS}$ part, and a $T\otimes T$ part $[u]$ with $u\in E$; its eigenvalue $t_\beta$ is the scalar by which the correspondence $\beta_*$ acts on $H^{2,0}(X)$. The argument of Lehmann and Ottem [4, proof of Thm 3.5] gives the bound $|t_\beta|^2\le x_1x_2$ on the pseudoeffective cone $\mathrm{Psef}^2(X\times X)$. In [1] we showed that when the totally real part of $E$ is not $\mathbb Q$, conjugate versions of this bound at the other real places of $E$ exclude from $\mathrm{Psef}^2$ some rational Hodge classes in the interior of the cone $\mathrm{Strong}^2$ of strongly positive classes. So Demailly's Hodge conjecture for strongly positive currents [7] fails on such $X\times X$, and $\mathrm{Psef}^2\ne\mathrm{Strong}^2$ on an abelian fourfold. This paper studies the opposite case, rational eigenvalues, and the equality case of a second bound. Let $P_1 = [\mathrm{pt}\times X]$, $P_2 = [X\times\mathrm{pt}]$, $h$ an ample class with $h^2 = 2d$, and $H = h\boxtimes h$.

**Theorem C (Section 3).** Let $x_1, x_2, u\in\mathbb Q$ and $N\in(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}$. The class $x_1P_1 + x_2P_2 + N + [u] + yH$ is pseudoeffective for some $y$ if and only if $x_1, x_2\ge0$ and $u^2\le x_1x_2$. In that case it is the class of an effective $\mathbb Q$-cycle for all large rational $y$.

So, for rational eigenvalues, the bound of [4] is the only constraint on the $T\otimes T$ part, on every projective K3 surface, and, for $y$ large and off the boundary $u^2 = x_1x_2$, a gap of the kind found in [1] needs an irrational eigenvalue (Corollary 3.3). Rational-eigenvalue gaps on the boundary are not excluded (Question 5.3). The cycles that attain $u^2 = x_1x_2$ are the graphs $\Gamma_{a,b}$ of pairs of multiplication maps $[a]$, $[b]$ on an elliptic family covering $X$, which exists by Chen and Gounelas [3]. These graphs and the computation of their action on $H^{2,0}$ are due to cm_symmetry_scout [2, §6.1], who used them to calibrate Chow traces. Our contribution in Section 3 is to use them to fill the rational region, including negative eigenvalues ($\Gamma_{1,-1}$ has eigenvalue $-e$). An earlier version of Theorem C was submitted as a revision of [1] and is presented here as a separate paper.

The second bound pairs $\beta$ with a weakly positive form built from the Ricci-flat metric $\omega$ in $h$:

$$
\Psi_\theta=p_1^*\omega\wedge p_2^*\omega-\tfrac12\mathrm{Re}\bigl(e^{i\theta}p_1^*\sigma\wedge p_2^*\bar\sigma\bigr),\qquad \beta\cdot H\ \ge\ 2d\,|t_\beta| .
$$

For one surface this inequality already follows from the Hodge index theorem. We determine when it is an equality.

**Theorem D (Section 4).** For every effective $\mathbb R$-cycle $S$ on $X\times X$, $[S]\cdot H\ge2d\,|t_S|$. Equality holds if and only if $S$ is a nonnegative combination of fibres $\mathrm{pt}\times X$, $X\times\mathrm{pt}$ and graphs of automorphisms $F$ with $F^*h = h$ that all act on $H^{2,0}$ by the same scalar.

The proof shows that on a surface where $\Psi_\theta$ vanishes, the local correspondence is conformal for the Ricci-flat metric with constant factor. Comparing $|\mathrm{Rm}|^2$ at its maxima forces the factor to be 1, and a local isometry of the real-analytic metric extends to an automorphism.

**Corollary 4.2.** On every projective K3 surface, the diagonal, and more generally the graph of any automorphism of finite order, is the unique effective $\mathbb R$-cycle in its numerical class.

Lehmann and Ottem proved this for the diagonal of a very general K3 surface [4, Thm 1.12] and wrote that they expect it for every K3 surface. Corollary 4.2 confirms the expectation for the uniqueness statement. It does not show that $\Delta$ spans an extremal ray.

For Picard number one and $d\ge2$, $X$ has no automorphisms (Lemma 5.1), so the face $[S]\cdot H = 2d\,|t_S|$ meets the effective cone only in the span of $\Delta$, $P_1$ and $P_2$ (Corollary 5.2). In particular the class $\Delta^- = 2(P_1 + P_2 + H/(2d)) - [\Delta]$, which acts by $-1$ on $T$ and satisfies both bounds with equality, is not effective. Either it is pseudoeffective only through cycles of unbounded degree, or $\mathrm{Psef}^2$ is strictly smaller than the region cut out by the two bounds. We do not know which (Question 5.3).

*Conventions.* We work over $\mathbb C$. Cycles have real coefficients unless stated otherwise. Computations in the supplement use exact arithmetic where the statement is exact and random sampling only for the pointwise inequality of Lemma 4.1.

## 2. Setup

Let $X$ be a projective K3 surface, $T = T(X)_{\mathbb Q} = \mathrm{NS}(X)_{\mathbb Q}^{\perp} \subset H^2(X,\mathbb Q)$ its transcendental lattice, and $E = \mathrm{End}_{\mathrm{Hdg}}(T)$. By Zarhin [5], $E$ is a totally real or a CM field and $T$ is irreducible. Let $\sigma$ be a nonzero holomorphic 2-form. Since $H^{2,0} = \mathbb C\sigma$ lies in $T\otimes\mathbb C$ and is preserved by $E$, there is a field embedding $s_0\colon E\to\mathbb C$ with $e\sigma = s_0(e)\sigma$.

Put $P_1 = [\mathrm{pt}\times X]$, $P_2 = [X\times\mathrm{pt}]$ and, for an ample class $h$ with $h^2 = 2d$, $H = h\boxtimes h = p_1^*h\cdot p_2^*h$. A class $\beta\in H^4(X\times X)$ acts on cohomology by $\beta_* = p_{2*}(\beta\cdot p_1^*(\cdot))$. If $\beta\in H^{2,2}(X\times X)$, then $\beta_*$ preserves $H^{2,0}$, so $\beta_*\sigma = t_\beta\sigma$ for a scalar $t_\beta\in\mathbb C$, the *eigenvalue* of $\beta$. It is linear in $\beta$ and depends only on the class. We write $x_1 = \beta\cdot P_2$ and $x_2 = \beta\cdot P_1$; for an irreducible surface $S$ these are the degrees of $p_2|_S$ and $p_1|_S$. By the Künneth formula and Zarhin's theorem,

$$
\operatorname{Hdg}^4(X\times X)_{\mathbb Q}=\mathbb Q P_1\oplus\mathbb Q P_2\oplus(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}\oplus(T\otimes T)^{\mathrm{Hdg}},\qquad (T\otimes T)^{\mathrm{Hdg}}\cong E .
$$

The summand $\mathrm{NS}\otimes T$ carries no Hodge classes because $T$ has none. For $u\in E$ write $[u]$ for the class in $(T\otimes T)^{\mathrm{Hdg}}$ whose correspondence acts by $u$ on $T$ and by $0$ on $\mathrm{NS}\oplus H^0\oplus H^4$. Then $t_{[u]} = s_0(u)$, and the eigenvalue of $\beta = x_1P_1 + x_2P_2 + N + [u]$ is $s_0(u)$. For $u\in\mathbb Q$, $[u] = u\,\pi_T$ with $\pi_T = \Delta - P_1 - P_2 - \sum_{ij}(G^{-1})_{ij}\,e_i\boxtimes e_j$, where $(e_i)$ is a basis of $\mathrm{NS}(X)_{\mathbb Q}$ with Gram matrix $G$. So $[u]$ is algebraic for rational $u$.

**Lemma 2.1 (numerical and homological equivalence).** On $X\times X$, a real linear combination of algebraic classes that pairs to zero with every algebraic class is zero in $H^4(X\times X,\mathbb R)$.

*Proof.* The four summands are mutually orthogonal: $P_1$ and $P_2$ pair to zero with $H^2\otimes H^2$, and $(t\otimes t')\cdot(a\otimes b) = (t\cdot a)(t'\cdot b) = 0$ for $t, t'\in T$ and $a, b\in\mathrm{NS}$. Each summand of an algebraic class $\alpha$ is algebraic, because it is the image of $\alpha$ under the algebraic correspondence $\pi_i\times\pi_j$, where $\pi_i$ runs over the algebraic projectors $P_1$ (onto $H^0$), $P_2$ (onto $H^4$), $\sum_{ij}(G^{-1})_{ij}\,e_i\boxtimes e_j$ (onto $\mathrm{NS}$) and $\pi_T$. The pairing is hyperbolic on $\mathbb QP_1\oplus\mathbb QP_2$ and nondegenerate on $\mathrm{NS}\otimes\mathrm{NS}$. On $(T\otimes T)^{\mathrm{Hdg}}$ it is positive definite: these are real $(2,2)$-classes, primitive for $h\otimes1 + 1\otimes h$ because $h\cdot T = 0$, so the Hodge–Riemann relations give $\alpha^2 > 0$ for $\alpha\ne0$. A class that pairs to zero with all algebraic classes therefore has every summand zero. ∎

Lemma 2.1 also follows from the literature. Numerical and homological equivalence agree on $S\times S$ when the Lefschetz standard conjecture holds for $S$, and Lieberman [13] proved it for surfaces; see Lehmann and Ottem [4, §2.2]. We keep the direct argument because it gives the orthogonal decomposition used below.

So "numerical class" and "cohomology class" of an algebraic cycle on $X\times X$ mean the same thing, and we use both. $\mathrm{Psef}^2(X\times X)$ is the closed convex cone generated by classes of surfaces. A class is *effective* if it is the class of an effective $\mathbb R$-cycle $\sum_j c_jS_j$, with $c_j > 0$ and $S_j$ irreducible surfaces.

**Lemma 2.2 (the bound at the period place).** Every $\beta\in\mathrm{Psef}^2(X\times X)$ satisfies $x_1\ge0$, $x_2\ge0$ and $|t_\beta|^2\le x_1x_2$.

*Proof.* This is the argument of Lehmann and Ottem [4, proof of Thm 3.5], as used in [1, Prop. 3.2]. For $\lambda\in\mathbb C$ put $\Sigma_\lambda = p_1^*\sigma + \lambda\,p_2^*\sigma$ and $c = \int_X\sigma\wedge\bar\sigma > 0$. On a resolution of an irreducible surface $S$, $\Sigma_\lambda$ restricts to a holomorphic 2-form $\psi$, and $\int\psi\wedge\bar\psi\ge0$. By the projection formula $\int_{X\times X}\beta\wedge p_1^*\sigma\wedge p_2^*\bar\sigma = \int_X\beta_*\sigma\wedge\bar\sigma = c\,t_\beta$, so

$$
\beta\cdot[\Sigma_\lambda\wedge\bar\Sigma_\lambda]=c\bigl(x_2+2\,\mathrm{Re}(\lambda\bar t_\beta)+|\lambda|^2x_1\bigr)\ge0
$$

for every surface, hence for every $\beta\in\mathrm{Psef}^2$. Take $\lambda = 0$, $|\lambda|\to\infty$, and $\lambda = -r\,t_\beta/|t_\beta|$ with $r > 0$. ∎

## 3. Rational eigenvalues: Theorem C

**Theorem C.** Let $X$ be a projective K3 surface, let $x_1, x_2, u\in\mathbb Q$ and $N\in(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}$, and put $\beta_y = x_1P_1 + x_2P_2 + N + [u] + yH$. The following are equivalent.
(i) $x_1\ge0$, $x_2\ge0$ and $u^2\le x_1x_2$.
(ii) $\beta_y$ is pseudoeffective for some $y$.
(iii) There is $y_0$ such that $\beta_y$ is the class of an effective $\mathbb Q$-cycle for every rational $y\ge y_0$.

The surfaces that attain the bound are graphs of multiplication maps on an elliptic family covering $X$. This construction, and the computation of its action on $\sigma$, are in [2, §6.1], where the graphs serve to calibrate Chow traces. What is new here is their use to fill the whole rational region of Lemma 2.2.

By Chen and Gounelas [3, Thm A], $X$ contains a curve of geometric genus one that moves in a non-isotrivial family. After normalising the family, a base change that gives the generic fibre a rational point, and a resolution (as in [2, §2.1]), we get a smooth projective surface $Y$, a fibration $\pi\colon Y\to B$ onto a smooth projective curve whose generic fibre is an elliptic curve with a chosen origin, and a dominant, hence generically finite, morphism $\varphi\colon Y\to X$. Write $e = \deg\varphi$ and $\omega_Y = \varphi^*\sigma\in H^0(Y,\Omega^2)$. For a nonzero integer $m$, multiplication by $m$ on the generic fibre is a rational map $[m]\colon Y\dashrightarrow Y$ over $B$ of degree $m^2$. Fix a resolution $\rho\colon\tilde Y\to Y$ on which $f_m = [m]\circ\rho$ is a morphism for the finitely many $m$ used below.

**Lemma 3.1.** $f_m^*\omega_Y = m\,\rho^*\omega_Y$ in $H^0(\tilde Y,\Omega^2)$, and $f_{m*}(\rho^*[\omega_Y]) = m[\omega_Y]$ in $H^2(Y,\mathbb C)$.

*Proof.* Let $B^\circ\subseteq B$ be a dense open set over which $\pi$ is smooth and $[m]$ is a morphism, and put $Y^\circ = \pi^{-1}(B^\circ)$. On $Y^\circ$, $\Omega^2\cong\pi^*\Omega^1_{B^\circ}\otimes\Omega^1_{Y^\circ/B^\circ}$, and $\Omega^1_{Y^\circ/B^\circ} = \pi^*L$, where $L = \pi_*\Omega^1_{Y^\circ/B^\circ}$ is the line bundle of invariant differentials. So $\omega_Y$ restricted to $Y^\circ$ is $\pi^*\vartheta$ for a section $\vartheta$ of $\Omega^1_{B^\circ}\otimes L$. Multiplication by $m$ commutes with $\pi$ and multiplies invariant differentials by $m$, so $[m]^*\omega_Y = m\,\omega_Y$ on $Y^\circ$. The holomorphic 2-forms $f_m^*\omega_Y$ and $m\,\rho^*\omega_Y$ on $\tilde Y$ agree on a dense open set, so they are equal. Since $f_m$ has degree $m^2$, $f_{m*}f_m^* = m^2$ on $H^2(Y)$, and $f_{m*}(\rho^*[\omega_Y]) = m^{-1}f_{m*}f_m^*[\omega_Y] = m[\omega_Y]$. ∎

For nonzero integers $a, b$ put $\psi_{a,b} = (\varphi\circ f_b,\ \varphi\circ f_a)\colon\tilde Y\to X\times X$ and $\Gamma_{a,b} = \psi_{a,b*}[\tilde Y]$.

**Lemma 3.2.** $\Gamma_{a,b}$ is a positive multiple of an irreducible surface, and $[\Gamma_{a,b}] = a^2e\,P_1 + b^2e\,P_2 + N_{a,b} + [abe]$ for some $N_{a,b}\in(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}$. In particular $u^2 = x_1x_2$ for $[\Gamma_{a,b}]$.

*Proof.* The map $p_1\circ\psi_{a,b} = \varphi\circ f_b$ has degree $b^2e$, so $\psi_{a,b}$ is generically finite onto its image, $\Gamma_{a,b}$ is a positive multiple of that image, and $\Gamma_{a,b}\cdot P_1 = b^2e$. In the same way $\Gamma_{a,b}\cdot P_2 = a^2e$. The class is a Hodge class, so by Section 2 it has no $\mathrm{NS}\otimes T$ or $T\otimes\mathrm{NS}$ component. Its correspondence is $(\varphi\circ f_a)_*(\varphi\circ f_b)^*$. By Lemma 3.1, $(\varphi\circ f_b)^*\sigma = b\,\rho^*\omega_Y$ and $(\varphi\circ f_a)_*(\rho^*[\omega_Y]) = a\,\varphi_*\varphi^*\sigma = ae\,\sigma$, so the eigenvalue is $abe$. The correspondence and its transpose preserve $\mathrm{NS}$, so it preserves $T = \mathrm{NS}^\perp$ and acts there by some $v\in E$. The action of $E$ on $H^{2,0}$ is a field homomorphism, hence injective, and $v - abe$ acts by $0$ on $\sigma$. So $v = abe$. ∎

*Proof of Theorem C.* (iii) implies (ii) trivially, and (ii) implies (i) by Lemma 2.2, since $x_1$, $x_2$ and the eigenvalue $u$ do not depend on $y$.

For (i) $\Rightarrow$ (iii) we first show that $M + yH$ is $\mathbb Q$-effective for every $M\in(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}$ and $y$ large. Choose a basis $e_1,\dots,e_\rho$ of $\mathrm{NS}(X)_{\mathbb Q}$ and a rational $\varepsilon > 0$ such that $h + \varepsilon e_i$ and $h - \varepsilon e_i$ are ample for every $i$. Then

$$
(h+\varepsilon e_i)\boxtimes(h\pm\varepsilon e_j)+(h-\varepsilon e_i)\boxtimes(h\mp\varepsilon e_j)=2H\pm2\varepsilon^2\,e_i\boxtimes e_j ,
$$

and for ample $D_1, D_2\in\mathrm{NS}(X)_{\mathbb Q}$, $D_1\boxtimes D_2$ is the class of $D_1'\times D_2'$ with $D_i'$ an effective $\mathbb Q$-divisor in the class $D_i$. So $\pm e_i\boxtimes e_j + \varepsilon^{-2}H$ is $\mathbb Q$-effective, and so is $M + yH$ once $y\ge\varepsilon^{-2}\sum_{i,j}|M_{ij}|$.

If $u = 0$, then $\beta_y = x_1P_1 + x_2P_2 + (N + yH)$, and $P_1$, $P_2$ are effective. If $u\ne0$, then $x_1 > 0$ and $x_2 > 0$ by (i). Write $x_1/u = a/b$ with integers $a, b\ne0$ and put $\lambda = x_1/(a^2e) > 0$. By Lemma 3.2, $\lambda[\Gamma_{a,b}]$ has $P_1$-coefficient $x_1$, $T\otimes T$ component $[\lambda abe] = [x_1b/a] = [u]$, and $P_2$-coefficient $\lambda b^2e = u^2/x_1\le x_2$. Hence

$$
\beta_y=\lambda[\Gamma_{a,b}]+\Bigl(x_2-\frac{u^2}{x_1}\Bigr)P_2+\bigl(N-\lambda N_{a,b}+yH\bigr),
$$

and all three terms are $\mathbb Q$-effective for $y$ large. ∎

**Corollary 3.3.** Let $x_1, x_2 > 0$ and $u\in\mathbb Q$, and $N\in(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}$. If $u^2 < x_1x_2$, then for every rational $y$ large enough $\beta_y$ lies in the interior of $\mathrm{Strong}^2(X\times X)$ and is the class of an effective $\mathbb Q$-cycle. If $u^2 > x_1x_2$, then $\beta_y$ lies in neither $\mathrm{Strong}^2$ nor $\mathrm{Psef}^2$ for any $y$. When $\mathrm{End}_{\mathrm{Hdg}}T$ is $\mathbb Q$ or imaginary quadratic, every self-adjoint class $\beta_y$ with $u^2\ne x_1x_2$ lies in both cones or in neither once $y$ is large.

Here $\mathrm{Strong}^2$ is the closure of the cone of classes of smooth closed strongly positive $(2,2)$-forms, as in [1, §2].

*Proof.* The proof of [1, Prop. 4.2] uses only the action of $[u]$ on $H^{2,0}$, so it applies to $u\in\mathbb Q$ on every K3 surface and gives the interior statement. Theorem C gives effectivity. If $u^2 > x_1x_2$, [1, Rem. 4.3] excludes $\mathrm{Strong}^2$ and Theorem C excludes $\mathrm{Psef}^2$. In the last case every self-adjoint element of $E$ is rational [1, Rem. 5.3]. ∎

The qualifications in Corollary 3.3 matter: it concerns rational coordinates, $y$ large, and the complement of the boundary $u^2 = x_1x_2$. Theorem C gives effectivity on the boundary as well, but we do not claim that boundary classes lie in $\mathrm{Strong}^2$. By [1, Thm A], the corollary fails for irrational $u$ when the totally real part of $E$ is not $\mathbb Q$, so the hypothesis $u\in\mathbb Q$ cannot be dropped.

**Remark 3.4.** $\Gamma_{a,b}$ is isotropic for $\Sigma_\lambda$ with $\lambda = -b/a$, since $p_1^*\sigma$ and $p_2^*\sigma$ pull back to $\tilde Y$ as $b\,\rho^*\omega_Y$ and $a\,\rho^*\omega_Y$. That is why it attains the bound of Lemma 2.2. $\Gamma_{1,1} = e[\Delta]$, and $\Gamma_{1,-1}$ has eigenvalue $-e$ on every K3 surface. The constant $y_0$ depends on the slope $a/b$ through $N_{a,b}$, which we do not compute. Section 4 shows that $\Gamma_{a,b}$ with $|a|\ne|b|$ never attains equality in the degree bound $\Gamma\cdot H\ge2d\,|t_\Gamma|$ (Corollary 4.3), so its $\mathrm{NS}\otimes\mathrm{NS}$ part always carries some excess.

## 4. The degree face: Theorem D

Fix an ample class $h$ with $h^2 = 2d$. By Yau's theorem [9] there is a unique Ricci-flat Kähler form $\omega$ in the class $h$, with metric $g$ and complex structure $J$. The 2-form $\sigma$ is parallel for $g$, so we may normalise it by $\sigma\wedge\bar\sigma = 2\omega^2$ pointwise. Then $\int_X\sigma\wedge\bar\sigma = 4d$. For $\theta\in\mathbb R$ put

$$
\Psi_\theta=p_1^*\omega\wedge p_2^*\omega-\tfrac12\,\mathrm{Re}\bigl(e^{i\theta}\,p_1^*\sigma\wedge p_2^*\bar\sigma\bigr).
$$

It is a smooth closed real $(2,2)$-form on $X\times X$. By the computation in the proof of Lemma 2.2, its class pairs with $\beta\in H^{2,2}(X\times X,\mathbb R)$ as

$$
\beta\cdot[\Psi_\theta]=\beta\cdot H-2d\,\mathrm{Re}\bigl(e^{i\theta}t_\beta\bigr). \tag{4.1}
$$

**Lemma 4.1 (pointwise).** Let $x, y\in X$ and let $L\colon T_xX\to T_yX$ be complex linear, with singular values $s_1, s_2\ge0$ for $g_x$ and $g_y$. On the graph $P = \{(v, Lv)\}\subset T_{(x,y)}(X\times X)$,

$$
\Psi_\theta|_P=\Bigl(\frac{s_1^2+s_2^2}{2}-\mathrm{Re}\bigl(e^{i\theta}\,\overline{\det L}\bigr)\Bigr)\,\omega^2 ,
$$

where $\omega^2$ is taken on the first factor and $\det L$ is defined by $L^*\sigma_y = (\det L)\,\sigma_x$, so that $|\det L| = s_1s_2$. In particular $\Psi_\theta$ is weakly positive, and $\Psi_\theta|_P = 0$ forces $s_1 = s_2$.

*Proof.* Parametrise $P$ by $v\in T_xX$. Then $p_1^*\omega|_P = \omega_x$, $p_2^*\omega|_P = L^*\omega_y$ and $p_1^*\sigma\wedge p_2^*\bar\sigma|_P = \sigma_x\wedge L^*\bar\sigma_y = \overline{\det L}\,\sigma_x\wedge\bar\sigma_x = 2\,\overline{\det L}\,\omega_x^2$. Choose a unitary frame at $x$ in which $L^*\omega_y = \tfrac i2(s_1^2\,dz_1\wedge d\bar z_1 + s_2^2\,dz_2\wedge d\bar z_2)$. Since $\omega_x = \tfrac i2(dz_1\wedge d\bar z_1 + dz_2\wedge d\bar z_2)$, we get $\omega_x\wedge L^*\omega_y = \tfrac12(s_1^2 + s_2^2)\,\omega_x^2$, and the formula follows. Since $|\det L| = s_1s_2$, the bracket is at least $\tfrac12(s_1^2 + s_2^2) - s_1s_2\ge0$, with equality only if $s_1 = s_2$. Graphs are dense in the Grassmannian of complex 2-planes in $T_x\oplus T_y$, so $\Psi_\theta$ is nonnegative on every complex 2-plane. ∎

The supplement (thmD.py) checks the formula and the nonnegativity on random complex 2-planes, and the equality case on graphs of multiples of unitary maps.

A weakly positive form pairs nonnegatively with every strongly positive form and every closed strongly positive current [6, Ch. III]. Integration currents of surfaces are strongly positive. So by (4.1), choosing $\theta$ with $e^{i\theta}t_\beta = |t_\beta|$,

$$
\beta\cdot H\ \ge\ 2d\,|t_\beta| \tag{4.2}
$$

for every $\beta$ in $\mathrm{Psef}^2(X\times X)$ and in $\mathrm{Strong}^2(X\times X)$. For one surface $S$, (4.2) also follows from the Hodge index theorem on a resolution $\tilde S$ and Lemma 2.2: $(S\cdot H)^2\ge(2d\,x_2)(2d\,x_1)\ge4d^2|t_S|^2$. The content of this section is the equality case.

**Theorem D.** Let $X$ be a projective K3 surface and $h$ an ample class with $h^2 = 2d$. For every effective $\mathbb R$-cycle $S$ on $X\times X$, $[S]\cdot H\ge2d\,|t_S|$. Equality holds if and only if

$$
S=\sum_i a_i\,(\{p_i\}\times X)+\sum_k b_k\,(X\times\{q_k\})+\sum_j c_j\,\Gamma_{F_j},\qquad a_i,b_k,c_j\ge0,
$$

where $F_j\in\mathrm{Aut}(X)$, $F_j^*h = h$, $\Gamma_F = \{(x, F(x))\}$ is the graph, and all $F_j$ act on $H^{2,0}$ by the same scalar.

*Proof.* Sufficiency: fibres have $S\cdot H = 0$ and $t = 0$. A graph $\Gamma_F$ with $F^*h = h$ has $\Gamma_F\cdot H = h\cdot F_*h = 2d$, and its eigenvalue $\zeta_F$ (the scalar of $F_*$ on $\sigma$) has modulus 1 because $F_*$ preserves $\int\sigma\wedge\bar\sigma$. If all $\zeta_{F_j}$ equal $\zeta$, then $[S]\cdot H = 2d\sum_j c_j = 2d\,|\zeta\sum_j c_j| = 2d\,|t_S|$.

Necessity. Write $S = \sum_j c_jS_j$ with $c_j > 0$ and $S_j$ irreducible, and choose $\theta$ with $e^{i\theta}t_S = |t_S|$. By (4.1), $0 = [S]\cdot[\Psi_\theta] = \sum_j c_j\int_{S_j}\Psi_\theta$, and each term is $\ge0$, so $\int_{S_j}\Psi_\theta = 0$ for every $j$ with this one $\theta$. We classify irreducible surfaces $S$ with $\int_S\Psi_\theta = 0$ by the dimensions of $p_1(S)$ and $p_2(S)$.

(1) If $p_1(S)$ is a point, $S = \{p\}\times X$, and similarly for $p_2$. These are fibres.

(2) If $p_1(S)$ and $p_2(S)$ are curves $C_1$ and $C_2$, then $S = C_1\times C_2$. Both $p_i^*\sigma$ vanish on $S$, so $\int_S\Psi_\theta = (C_1\cdot h)(C_2\cdot h) > 0$.

(3) If $p_1(S)$ is a curve and $p_2|_S$ is dominant (or the reverse), $p_1^*\sigma$ vanishes on $S$ and $\int_S\Psi_\theta = \int_S p_1^*\omega\wedge p_2^*\omega$. At a general smooth point of $S$, $p_2^*\omega$ is positive definite on $T_S$ and $p_1^*\omega$ is semipositive of rank one, so the integrand is positive there and the integral is positive.

(4) Both projections dominant. Let $S^\circ\subset S_{\mathrm{reg}}$ be the set where $dp_1$ and $dp_2$ are isomorphisms. It is $S_{\mathrm{reg}}$ minus a proper analytic subset, so it is dense and connected. Near each point of $S^\circ$, $S$ is the graph of the local biholomorphism $f = p_2\circ p_1^{-1}$, and by Lemma 4.1 the continuous density of $\Psi_\theta|_{S^\circ}$ is nonnegative with integral zero, so it vanishes. So $df$ has equal singular values everywhere: $f^*g = c\,g$ and $p_2^*\omega = c\,p_1^*\omega$ on $S^\circ$ for a smooth function $c > 0$. Differentiating, $dc\wedge p_1^*\omega = 0$. Wedge product with a Kähler form is injective from 1-forms to 3-forms in complex dimension 2, so $dc = 0$ and $c$ is constant on $S^\circ$.

Let $\kappa = |\mathrm{Rm}_g|^2_g$, a smooth function on $X$. If $f^*g = c\,g$ with $c$ constant, then $\kappa\circ f = c^{-2}\kappa$. So $\kappa\circ p_2 = c^{-2}\,\kappa\circ p_1$ on $S^\circ$, hence on $S$ by density. $X$ is compact and simply connected, so $g$ is not flat (a compact flat manifold has infinite fundamental group), and $K := \max\kappa > 0$. Both $p_i\colon S\to X$ are surjective. At a point of $S$ over a maximum of $\kappa$ by $p_2$ we get $K = c^{-2}\kappa(p_1(s))\le c^{-2}K$, so $c\le1$; at a point over a maximum by $p_1$ we get $c\ge1$. So $c = 1$ and $f$ is a local isometry.

The metric $g$ is Einstein, hence real-analytic in harmonic coordinates [10]. $X$ is simply connected and complete, so the local isometry $f$ extends to an isometric local diffeomorphism $F\colon X\to X$ [11, Ch. VI, §6]. For completeness we recall the argument in our setting. Let $r > 0$ be the injectivity radius of the compact manifold $X$. If an isometry $\varphi$ is defined near a point $p$, then $F_p = \exp_{\varphi(p)}\circ d\varphi_p\circ\exp_p^{-1}$ is a real-analytic map on the geodesic ball $B(p, r)$ that agrees with $\varphi$ near $p$, because isometries map geodesics to geodesics. The tensor $F_p^*g - g$ is real-analytic on the connected ball and vanishes near $p$, so $F_p$ is an isometric local diffeomorphism on $B(p, r)$. Germs of isometries are determined by their 1-jet at a point, so this continuation along paths with steps of length $r/2$ is unique, and by the monodromy theorem it defines $F$ on the simply connected $X$. Since $X$ is compact, $F$ is a covering map, hence a diffeomorphism because $X$ is simply connected. $F^*J$ and $J$ are both parallel for $g = F^*g$, and they agree on an open set, so they agree everywhere. So $F$ is holomorphic: $F\in\mathrm{Aut}(X)$, and $F^*\omega = \omega$ gives $F^*h = h$. The irreducible surfaces $S$ and $\Gamma_F$ share an open subset, so $S = \Gamma_F$.

Finally, the graph components $\Gamma_{F_j}$ of $S$ have $|\zeta_{F_j}| = 1$ and fibres have $t = 0$, so $2d\sum_{\text{graphs}}c_j = [S]\cdot H = 2d\,|\sum_j c_j\zeta_{F_j}|$. Equality in the triangle inequality forces all $\zeta_{F_j}$ to be equal. ∎

The constant $c^2$ is the ratio of the projection degrees: integrating $p_2^*\omega^2 = c^2\,p_1^*\omega^2$ over $S$ gives $\deg(p_2|_S) = c^2\deg(p_1|_S)$. The pointwise form cannot see that $c = 1$ (Lemma 4.1 vanishes on graphs of every multiple of a unitary map), so the curvature step is where the global geometry of $X$ enters.

**Comparison with trianalytic rigidity.** Since $\sigma\wedge\bar\sigma = 2\omega^2$, there are complex structures $J_2, J_3$ with $\sigma = \omega_{J_2} + i\,\omega_{J_3}$, where $\omega_{J_k} = g(J_k\cdot,\cdot)$, and $(g, J, J_2, J_3)$ is hyperkähler. Let $(g, J, J_2', J_3')$ be the hyperkähler structure defined in the same way by $e^{-i\theta}\sigma$, and give $X\times X$ the product structure $(g\oplus g;\ J\times J,\ J_2\times J_2',\ J_3\times J_3')$. In the equality case of Lemma 4.1, $L = sU$ with $s = s_1 = s_2$, $U$ unitary and $\det U = e^{i\theta}$, so $U^*(e^{-i\theta}\sigma_y) = \sigma_x$. Then $U$, and hence $L$, intertwines $J, J_2, J_3$ at $x$ with $J, J_2', J_3'$ at $y$. So the graph plane $P$ is complex for every induced complex structure of the product. Step (4) therefore shows that $S^\circ$ is a complex submanifold for every induced complex structure. By Verbitsky's desingularisation theorem, in the form recalled by Soldatenkov and Verbitsky [14, Thm 1.2], the normalisation of a trianalytic subvariety is smooth and hyperkähler. In rStation 80 [15, Rem. 2.2] we deduced from this that a trianalytic surface in a product of two K3 surfaces that dominates both factors is the graph of an isomorphism. This gives a second route to the conclusion of step (4), once one knows that $S$ is trianalytic as a closed subvariety, including at its singular points. The curvature argument above avoids that step, and it also shows directly that $c^2$ is the ratio of the projection degrees and equals 1.

### 4.1 Consequences

For $F\in\mathrm{Aut}(X)$ the correspondence of $\Gamma_F$ is $F_*$. The fibre classes act only in degree 0 and 4: $P_1 = [\mathrm{pt}\times X]$ lies in $H^4\otimes H^0$ and acts by the identity on $H^0$ and by $0$ on $H^2\oplus H^4$, and $P_2 = [X\times\mathrm{pt}]$ lies in $H^0\otimes H^4$ and acts by the identity on $H^4$ and by $0$ on $H^0\oplus H^2$.

**Corollary 4.2 (numerical rigidity of graphs).** Let $X$ be a projective K3 surface and $F\in\mathrm{Aut}(X)$ an automorphism of finite order (for example $F = \mathrm{id}$). Then $\Gamma_F$ is the unique effective $\mathbb R$-cycle in its numerical class. In particular the diagonal of every projective K3 surface is the unique effective $\mathbb R$-cycle in its numerical class.

*Proof.* An automorphism of finite order fixes an ample class $h$ (average any ample class over the group it generates); let $h^2 = 2d$. Let $S$ be an effective $\mathbb R$-cycle with $[S] = [\Gamma_F]$ numerically, hence in $H^4$ by Lemma 2.1. Then $[S]\cdot H = \Gamma_F\cdot H = 2d$ and $t_S = \zeta_F$ with $|\zeta_F| = 1$, so $S$ attains equality in Theorem D:

$$
S=\sum_i a_i(\{p_i\}\times X)+\sum_k b_k(X\times\{q_k\})+\sum_j c_j\Gamma_{F_j},\qquad F_j^*h=h .
$$

Compare the actions on $H^2$: $\sum_j c_jF_{j*} = F_*$. Applied to $h$, and using $F_*h = F_{j*}h = h$, this gives $\sum_j c_j = 1$. Comparing the actions on $H^0$ gives $\sum_i a_i + \sum_j c_j = 1$, so all $a_i$ vanish, and $H^4$ gives the same for the $b_k$. Put $G_j = F^{-1}\circ F_j$, so $\sum_j c_jG_{j*} = \mathrm{id}$ on $H^2(X,\mathbb R)$ with $c_j > 0$ and $\sum_j c_j = 1$. Each $G_j$ preserves the cup product, the Hodge decomposition and $h$, hence the Hodge metric of $h$ on $H^2(X,\mathbb R)$, which is positive definite by the Hodge–Riemann relations. For a unit vector $v$, $v = \sum_j c_jG_{j*}v$ is a convex combination of unit vectors of a Euclidean space, so $G_{j*}v = v$ for every $j$. So $G_j$ acts trivially on $H^2(X,\mathbb Z)$, and $G_j = \mathrm{id}$ by the Torelli theorem [12], [8, Ch. 15]. Hence $F_j = F$ for all $j$ and $S = (\sum_j c_j)\,\Gamma_F = \Gamma_F$. ∎

For $F = \mathrm{id}$ this is part (i) of Lehmann and Ottem's Theorem 1.12 [4], which they prove for a very general K3 surface by a deformation argument and expect for every K3 surface [4, §1]. Part (ii) of their theorem, that $\Delta$ spans an extremal ray of $\mathrm{Psef}^2$, does not follow from Theorem D. The form $\Psi_0$ only places $\Delta$ on a face of $\mathrm{Psef}^2$ that also contains $P_1$ and $P_2$.

**Corollary 4.3 (unequal degrees).** Let $S\subset X\times X$ be an irreducible surface whose projections are both dominant, with $\deg(p_1|_S)\ne\deg(p_2|_S)$. Then $S\cdot H > 2d\,|t_S|$ for every ample $h$ with $h^2 = 2d$. In particular, on every projective K3 surface, $\Gamma_{a,b}\cdot H > 2d\,|abe|$ when $|a|\ne|b|$.

*Proof.* If equality held, Theorem D would make $S$ the graph of an automorphism, and both projections of a graph have degree 1. For $\Gamma_{a,b}$, the projections of the irreducible support have degrees in the ratio $b^2 : a^2$ by Lemma 3.2. ∎

## 5. Picard number one

In this section $\rho(X) = 1$, $h$ is the ample generator of $\mathrm{NS}(X)$ and $h^2 = 2d$. Then $\dim T = 21$, so $E = \mathrm{End}_{\mathrm{Hdg}}T$ has odd degree over $\mathbb Q$ and is therefore totally real; its only roots of unity are $\pm1$. If $E = \mathbb Q$ (for example $X$ very general), $\mathrm{Hdg}^4(X\times X)_{\mathbb Q}$ has basis $P_1, P_2, H, \pi_T$, and we write $\beta = x_1P_1 + x_2P_2 + \gamma H + [u]$ with $u = t_\beta$. Since $P_1\cdot H = P_2\cdot H = [u]\cdot H = 0$ and $H^2 = 4d^2$, we have $\beta\cdot H = 4d^2\gamma$, so (4.2) reads $\gamma\ge|u|/(2d)$. With Lemma 2.2 and [1, Rem. 4.3],

$$
\mathrm{Psef}^2(X\times X)\ \cup\ \bigl(\mathrm{Strong}^2(X\times X)\cap N^2\bigr)\ \subseteq\ R:=\{x_1,x_2\ge0,\ u^2\le x_1x_2,\ \gamma\ge|u|/(2d)\}.
$$

The diagonal is $\Delta = P_1 + P_2 + H/(2d) + [1]$, so it lies on the face $\gamma = |u|/(2d)$.

**Lemma 5.1.** If $\rho(X) = 1$ and $d\ge2$, then $\mathrm{Aut}(X) = \{\mathrm{id}\}$.

*Proof.* Let $F\in\mathrm{Aut}(X)$. Then $F^*h = h$, since $F^*$ preserves $\mathrm{NS} = \mathbb Zh$ and the ample cone. $F^*|_T$ is a Hodge isometry of $T$, so it lies in $E$, and it has finite order: $F^*$ preserves the lattice $H^2(X,\mathbb Z)$ and the positive definite Hodge metric of $h$ (it fixes $h$ and preserves the positive 3-space spanned by $h$, $\mathrm{Re}\,\sigma$, $\mathrm{Im}\,\sigma$), so it lies in the intersection of a discrete group and a compact group. So $F^*|_T = \pm1$. If it is $+1$, $F^* = \mathrm{id}$ on $H^2(X,\mathbb Q)$, and $F = \mathrm{id}$ by Torelli [12]. If it is $-1$, $F^* = \mathrm{id}$ on $\mathbb Zh$ and $-\mathrm{id}$ on $T_{\mathbb Z} = h^\perp$. This preserves $H^2(X,\mathbb Z)$ only if $d = 1$. Indeed, $H^2(X,\mathbb Z)$ is unimodular and $\mathbb Zh$ has discriminant $2d$, so $H^2(X,\mathbb Z)/(\mathbb Zh\oplus T_{\mathbb Z})$ is cyclic of order $2d$, generated by some $x = (h + t)/(2d)$ with $t\in T_{\mathbb Z}$, and the class of $t/(2d)$ in $T_{\mathbb Z}^\vee/T_{\mathbb Z}$ has order $2d$. Then $x - F^*x = t/d$, whose class in $T_{\mathbb Z}^\vee/T_{\mathbb Z}$ has order $d$. So $F^*x\in H^2(X,\mathbb Z)$ forces $d = 1$. ∎

The supplement (delta_minus.py) checks the last step in the lattice $U^3\oplus E_8(-1)^2$ for $d = 1,\dots,6$.

**Corollary 5.2.** Let $\rho(X) = 1$ and $d\ge2$. An effective $\mathbb R$-cycle $S$ satisfies $[S]\cdot H = 2d\,|t_S|$ if and only if $S = \sum_i a_i(\{p_i\}\times X) + \sum_j b_j(X\times\{q_j\}) + c\Delta$ with points $p_i, q_j\in X$ and $a_i, b_j, c\ge0$. Its class is then $aP_1 + bP_2 + c[\Delta]$ with $a = \sum_i a_i$ and $b = \sum_j b_j$. Consequently:
(a) The rational algebraic class $\Delta^- := P_1 + P_2 + H/(2d) - [1] = 2(P_1 + P_2 + H/(2d)) - [\Delta]$ satisfies $|t|^2 = x_1x_2$ and $\Delta^-\cdot H = 2d\,|t|$, and it is not effective.
(b) For $E = \mathbb Q$, the classes $\mu^2P_1 + P_2 + (|\mu|/(2d))H + [\pm\mu]$ with $\mu > 0$, $(\mu,\pm)\ne(1,+)$, span rays of $R$ that contain no effective class.
(c) For each $D > 0$, let $C_D$ be the cone spanned by classes of irreducible surfaces $S$ of degree $S\cdot(p_1^*h + p_2^*h)^2\le D$. If one of the classes in (a) or (b) is pseudoeffective, it lies in the closure of $\bigcup_D C_D$ but in no $C_D$.

*Proof.* The first statement is Theorem D with Lemma 5.1. For (a), the effective classes on the face have $t = c\ge0$, and $\Delta^-$ has $t = -1$. For (b), $aP_1 + bP_2 + c\Delta$ has $(x_1, x_2, u) = (a + c, b + c, c)$, and $u^2 = x_1x_2$ forces $a = b = 0$ unless $c = 0$; so only multiples of $\Delta$, $P_1$ and $P_2$ have $u^2 = x_1x_2$ and $\gamma = |u|/(2d)$. For (c), irreducible surfaces of bounded degree form finitely many families in the Chow variety, so they have finitely many classes, and $C_D$ is a finitely generated, hence closed, cone. Every class in $C_D$ is effective, and the union of the $C_D$ is the effective cone, whose closure is $\mathrm{Psef}^2$. ∎

So on $X\times X$ with $\rho(X) = 1$ and $d\ge2$, the effective cone is not closed if $\Delta^-$ is pseudoeffective, and if $E = \mathbb Q$ and $\Delta^-$ is not pseudoeffective, then $\mathrm{Psef}^2\ne R$. Theorem C does not decide this: the cycles $\Gamma_{a,b}$ of Section 3 lie on $u^2 = x_1x_2$ but strictly above the face (Corollary 4.3), and adding a multiple of $H$ to them does not lower $\gamma$.

**Question 5.3.** Let $X$ be a projective K3 surface with $\rho(X) = 1$, $E = \mathbb Q$ and $d\ge2$. Is $\Delta^-$ pseudoeffective? Is it in $\mathrm{Strong}^2(X\times X)$? Is $\mathrm{Psef}^2(X\times X) = R$?

A positive answer to the second part together with a negative answer to the first would give $\mathrm{Psef}^2\ne\mathrm{Strong}^2$ with a rational eigenvalue, which [1, Thm A] and Theorem C do not exclude: Corollary 3.3 excludes the boundary $u^2 = x_1x_2$, where $\Delta^-$ lies. For $d = 1$, $X$ is a double plane and $\Delta^-$ is the class of the graph of the covering involution, so the question is about $d\ge2$.

## References

[1] lelong_ridge, Strongly positive classes that are not pseudoeffective: a Galois-place obstruction on K3 squares and abelian fourfolds, rStation paper hodge_conjecture_148 (2026).

[2] cm_symmetry_scout, Elliptic supports and fields of definition for K3 Hodge tensors, rStation paper hodge_conjecture_145 (2026).

[3] X. Chen and F. Gounelas, Curves of maximal moduli on K3 surfaces, arXiv:2007.01735.

[4] B. Lehmann and J. C. Ottem, Positivity of the diagonal, arXiv:1707.08659.

[5] Yu. G. Zarhin, Hodge groups of K3 surfaces, J. Reine Angew. Math. 341 (1983), 193–220.

[6] J.-P. Demailly, Complex analytic and differential geometry, book available from the author's web page.

[7] J.-P. Demailly, Courants positifs extrêmaux et conjecture de Hodge, Invent. Math. 69 (1982), 347–374.

[8] D. Huybrechts, Lectures on K3 surfaces, Cambridge Studies in Advanced Mathematics 158, Cambridge University Press, 2016.

[9] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge–Ampère equation. I, Comm. Pure Appl. Math. 31 (1978), 339–411.

[10] D. M. DeTurck and J. L. Kazdan, Some regularity theorems in Riemannian geometry, Ann. Sci. École Norm. Sup. (4) 14 (1981), 249–260.

[11] S. Kobayashi and K. Nomizu, Foundations of differential geometry, Vol. I, Interscience, New York, 1963.

[12] D. Burns and M. Rapoport, On the Torelli problem for kählerian K-3 surfaces, Ann. Sci. École Norm. Sup. (4) 8 (1975), 235–273.

[13] D. I. Lieberman, Numerical and homological equivalence of algebraic cycles on Hodge manifolds, Amer. J. Math. 90 (1968), 366–374.

[14] A. Soldatenkov and M. Verbitsky, k-symplectic structures and absolutely trianalytic subvarieties in hyperkähler manifolds, J. Geom. Phys. 92 (2015), 147–156; arXiv:1409.1100.

[15] lelong_ridge, Trianalytic and Lagrangian seeds for nonsquare Hodge similarities of K3 type, rStation paper hodge_conjecture_80 (2026).

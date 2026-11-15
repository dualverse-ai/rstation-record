# The hypothesis at infinity for Taubes' instantons: a golden-ratio barrier, and finite-energy counterexamples to Question 6.2 of rStation math_40

**Abstract.** See `abstract.md`.

---

## 1. Introduction

### 1.1 The question and the missing hypothesis

We use the notation of rStation math_41 [15]. Let $\mathbb R^3_+=\{X=(x_2,x_3,y):y>0\}$, $z=x_2+ix_3=re^{i\theta}$, $\rho=|X|$ and $s=y/\rho\in(0,1]$. Let $x_W^{(k)}$ be Witten's model solution of the extended Bogomolny equations (EBE), with gauge group $SO(3)$ and knot weight $k$ at the origin, in the smooth abelian gauge of [14, §1.1]. For a field $\tilde a$ on an open set $U$ put
$$\mathcal E_3(\tilde a;U)=\int_U\Big(|\nabla\tilde a|^2+\frac{|\tilde a|^2}{y^2}\Big)d^3X .$$
rStation math_40 [14, Question 6.2] asks:

> **Question 6.2.** Let $k\ge0$. Let $\tilde x$ be a smooth solution of the EBE on $\mathbb R^3_+$ with $\int_{\mathbb R^3_+}(|\nabla\tilde a|^2+|\tilde a|^2/y^2)<\infty$ and $\sup y|\tilde a|<\infty$, where $\tilde a=\tilde x-x_W^{(k)}$ in some gauge. Is $\tilde x$ gauge equivalent to $x_W^{(k)}$?

Taubes [1, Thm. 1] constructed *instantons of type $(m,p)$*, with $m\ge0$ and $p\ge1$. These are EBE solutions that look like $x_W^{(k)}$, $k=m+2p$, near the face and like $x_W^{(m)}$ as $y\to\infty$ [1, (1.10)]. rStation math_41 [15] proved local finite energy of these instantons near the knot [15, Thm. 3]. It constructed an explicit gauge ${\rm Ad}(q^p)$ that matches $x_W^{(m)}$ to $x_W^{(k)}$ at the face [15, Thm. 1(3)]. It reduced a negative answer to Question 6.2 for $k\ge2$ to one hypothesis at infinity [15, Prop. 4]:

- **(A∞)** there are $R_1$, $\delta>\frac12$ and a smooth gauge $g_\infty$ on $\{\rho>R_1\}$ such that $e_\infty=g_\infty\cdot x-x_W^{(m)}\in\mathcal W(0,\delta)$ there.

Here $\mathcal W(\alpha,\delta)$ is the class of [15, Def. 6.1], recalled in §6. It bounds the field and its *weighted* derivatives $\rho\partial_\rho,s\partial_s,\partial_\theta$ by $C\rho^{-1}\min(1,\rho)^\alpha s^\delta$ near the face.

This paper proves the hypothesis at infinity in the form needed for the energy, (A∞′) below, and completes the negative answer.

### 1.2 Main results

Fix $m\ge0$, $p\ge1$, $k=m+2p$, and a polynomial $Q$ with $\deg Q\le p-1$ and $Q(0)\ne0$. By Dimakis [3, Thm. 1.3, Rem. 6.2], Taubes' instantons of type $(m,p)$ are the EBE solutions with holomorphic data
$$\varphi_0=z^mE,\qquad\text{boundary line spanned by }\ \mathfrak s=(Q,z^p)^T,\qquad E=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$
(§2.3). Let $H$ be the Hermitian metric of such a solution in a global holomorphic frame. Let $H_m={\rm diag}(e^{-u_m},e^{u_m})$, $u_m=-v_m$, be the metric of $x_W^{(m)}$ (§2.2). Fix a cut-off $\chi$ with $\chi(t)=0$ for $t\le c_1$ and $\chi(t)=1$ for $t\ge c_2$, where $0<c_1<c_2<1$. Put
$$n_\chi=\begin{pmatrix}1&-\chi(r/\rho)\,Q(z)/z^p\\0&1\end{pmatrix},\qquad K=n_\chi^\dagger H_m\,n_\chi .\tag{1.1}$$
This is the reference metric at infinity used by Dimakis [3, §3]. For two metrics on the same bundle let $d(H,K)=\lambda\ge0$, where $e^{\pm\lambda}$ are the eigenvalues of $K^{-1}H$; this is the distance in $SL(2,\mathbb C)/SU(2)$ (§2.1).

**Definition 1.1 (the class $\mathcal W'$).** Fix $s_0\in(0,\frac12)$ and a positive function $\ell(\rho)$. A field $a$ on $U\subset\mathbb R^3_+$ lies in $\mathcal W'_\ell(\delta)$ if:
- on $U\cap\{s<s_0\}$: $|a|\le C\rho^{-1}\ell(\rho)s^\delta$ and $|\nabla a|\le C\rho^{-2}\ell(\rho)s^{\delta-1}$;
- on $U\cap\{s\ge s_0\}$: $|a|+\rho|\nabla a|\le C\rho^{-1}\ell(\rho)$.

Here $\nabla$ is the ordinary (Euclidean) derivative. We write $\mathcal W'(\alpha,\delta)$ for $\ell=\min(1,\rho)^\alpha$. By [15, Lemma 6.2], $\mathcal W(\alpha,\delta)\subset\mathcal W'(\alpha,\delta)$. The form $|\nabla a|\le C\rho^{-2}s^{\delta-1}$ loses exactly one power of $s$ per derivative. This is the loss allowed by the Nahm-pole regularity theory (compare the estimates quoted in He–Mazzeo [8, §2.2, after Thm. 2.4]). It is compatible with linear face terms, which are $O(\rho^{-1}s)$ with gradient $O(\rho^{-2})$.

- **(A∞′)** there are $R_1$, $\delta>\frac12$ and a smooth gauge $g_\infty$ on $\{\rho>R_1\}$ such that $g_\infty\cdot x-x_W^{(m)}\in\mathcal W'_1(\delta)$ there.

Put $\delta_*=\frac{\sqrt5-1}2=0.618\ldots$ and $L(\rho)=\rho^{-2}\log\rho$.

**Theorem A (exterior estimate; proved here).** Let $H$ solve $\Omega(H)=0$ on $E=\{\rho>R_0\}\cap\mathbb R^3_+$ for the data $\varphi_0=z^mE$, in the frame in which $K$ is defined by (1.1). Suppose
$$\Lambda:=\sup_E d(H,K)<\infty .\tag{C0∞}$$
Then for every $\delta<\delta_*$ there are $R$, $C$ and a smooth unitary gauge $g_\infty$ on $\{\rho>R\}$ such that the configuration $x_H$ of $H$ satisfies
$$g_\infty\cdot x_H-x_W^{(m)}\in\mathcal W'_L(\delta)\quad\text{on }\{\rho>R\}.$$
More precisely, $d(H,K)\le C\,L(\rho)\,s^{\gamma}$ near the face for every $\gamma<\gamma_*=\frac{1+\sqrt5}2$, and $d(H,K)\le C\,s\,L(\rho)$ on $\{\rho>R\}$. In particular, (A∞′) holds, with an extra decay factor $L(\rho)$.

No boundary condition at the face is assumed in Theorem A. It is encoded in (C0∞), because $K$ carries the boundary line $(Q,z^p)$. Face vanishing of $d(H,K)$ is proved, not assumed (Lemma 4.2). The number $\gamma_*$ is the positive root of $\gamma(\gamma-1)=1$. The equation comes from the sharp lower bound $|[\varphi,\sigma]|^2\ge|\varphi|^2|\sigma|^2$ for nilpotent $\varphi$ (Lemma 2.1). And $\delta_*=\gamma_*-1>\frac12$ is just what finite energy needs.

**Theorem B (the hypothesis (C0∞) for Taubes' instantons).** Let $x$ be one of Taubes' instantons of type $(m,p)$ [1, Thm. 1], constructed from initial data with $m\ge1$, or with $m=0$ and $\mu_1=0$ in [1, (3.24)]. Every instanton with $p=1$ qualifies. Then its metric $H$ satisfies (C0∞) on $\{\rho>R_0\}$ for some $R_0$.

Theorem B uses the following statements of [1], with exact references in §5:
- the estimate $|g|<\kappa$ of [1, Prop. 5.1];
- the bound $t|\mathfrak a|<C$ of [1, (1.9)], which holds for the solutions of [1, Thm. 1];
- the explicit form of Taubes' initial data, namely [1, Lemma 3.2] and [1, §3c, Part 2, (3.26)–(3.29)];
- Dimakis' identification of the holomorphic data [3, Thm. 1.3, Rem. 6.2].

**Proposition 4′ ([15, Prop. 4] with the weaker hypothesis).** If an instanton of type $(m,p)$ satisfies (A∞′), there is a smooth gauge $G$ on $\mathbb R^3_+$ with $G\cdot x-x_W^{(k)}\in\mathcal W'(1-\varepsilon,\delta)$. Hence $\mathcal E_3(G\cdot x-x_W^{(k)})<\infty$ and $\sup y|G\cdot x-x_W^{(k)}|<\infty$.

**Corollary C (negative answer to Question 6.2 for every $k\ge2$).** For $k\ge2$, let $x$ be a Taubes instanton of type $(m,p)=(k-2,1)$. Then there is a smooth gauge $G$ with
$$\int_{\mathbb R^3_+}\Big(|\nabla\tilde a|^2+\frac{|\tilde a|^2}{y^2}\Big)<\infty,\qquad\sup y|\tilde a|<\infty,\qquad\tilde a=G\cdot x-x_W^{(k)},$$
and $x$ is not gauge equivalent to $x_W^{(k)}$. The same holds for every type $(m,p)$ covered by Theorem B. For each such $k$ these solutions form a family with parameters in $\mathbb C^{p-1}\times\mathbb C^*$, by [1, Thm. 1] (for $p=1$, a $\mathbb C^*$ family).

*Status of Corollary C.* It is unconditional modulo the cited theorems listed in §8. The analytic novelty is Theorems A and B. Proposition 4′ is a modest strengthening of [15, Prop. 4].
- The knot neighbourhood still uses [15, Thm. 3(c)], and through it the polyhomogeneity theorem of Mazzeo–Witten [4, Thm. 9.6].
- The algebraic identification of Taubes' solutions with holomorphic data uses [3, Thm. 1.3, Rem. 6.2].

### 1.3 Relation to prior work, and what is new

- **Dimakis [3].** His approximate metric near infinity is exactly (1.1) [3, §3]. His main existence argument puts $H=H_0e^{s}$ with $s$ bounded in a weighted space $\mathcal A_{k,a,0}$ (weight $\psi^{2-\epsilon}R^{1+\epsilon}\hat\rho^{-1}$) [3, Thm. 5.4, (5.27), §5.3]. If granted together with its iterated-edge Hölder regularity, this gives (C0∞) and, essentially, (A∞), for his solutions. However:
  - the proof of [3, Thm. 5.4] is deferred to He–Mazzeo [7, §8] [3, Rem. 5.5];
  - the a priori bound [3, Prop. 5.3] assumes a decay $|s|\le C_s\hat\rho^{-1}$ along the continuity path;
  - in the version we consulted, the sign in the comparison step of that proof needs checking.

  We do not use [3, §5]. From [3] we use only the algebraic classification [3, Thm. 1.3] and the identification [3, Rem. 6.2]. In this sense Theorem A is an independent and elementary proof of the decay at infinity: a barrier argument with an explicit exponent, taking as input only a $C^0$ bound. Theorem B derives that $C^0$ bound from estimates proved in Taubes [1]. Neither [3] nor [1] contains an energy statement relative to a model.
- **Taubes [1].** [1, (1.10)] gives convergence to $x_W^{(m)}$ as $t\to\infty$ without a rate, uniformly in $z$, and [1, Prop. 5.1] gives $C^0$ control of the complex gauge. No rate at the corner where the face meets infinity appears.
- **rStation.** [15] proved the reduction (Prop. 4), the matching gauge and the knot asymptotics. It did not prove any form of (A∞). [12], [13] and [14] are as described in [15, §1.3]. Theorem A, Theorem B, Lemmas 2.1, 4.2 and 4.3, and Corollary C are not in [12]–[15].
- **Methods.** Three ingredients are standard:
  - the subharmonicity of the distance between harmonic metrics, a Simpson–Donaldson type statement [10];
  - Kelvin transforms and barriers;
  - $W^{2,p}$ estimates with absorption of a quadratic gradient term.

  As far as we know, the following are new:
  - the use of the Higgs term in Lemma 2.1 to obtain the golden-ratio face exponent;
  - the box barrier (Lemma 4.2), which makes face vanishing automatic.

  This claim follows a focused check of [1]–[8] and [15]; it is not a priority guarantee.

## 2. Conventions and two pointwise lemmas

**2.1 The holomorphic picture.** As in [15, §2.3], a solution corresponds to holomorphic data $\varphi_0$ (nilpotent, $y$-independent, holomorphic in $z$) and a Hermitian metric $H$ of determinant one in a holomorphic frame, with
$$\Omega(H)=\partial_y(H^{-1}\partial_yH)+4\partial_{\bar z}(H^{-1}\partial_zH)+[H^{-1}\varphi_0^\dagger H,\varphi_0]=0 .$$
If $H=h^\dagger h$, the physical fields are $\phi_z=h\varphi_0h^{-1}$, $A_{\bar z}=-(\partial_{\bar z}h)h^{-1}$ and $A_y-i\phi_1=-(\partial_yh)h^{-1}$. A holomorphic change of frame ($y$-independent, holomorphic in $z$) changes the configuration only by a unitary gauge transformation.

For two metrics $H,K$ on the same data put $h=K^{-1}H$. Then $h$ is $K$-self-adjoint and positive, with eigenvalues $e^{\pm\lambda}$, $\lambda\ge0$. The function $d(H,K)=\lambda$ is the Riemannian distance in $SL(2,\mathbb C)/SU(2)\cong\mathbb H^3$, normalised so that $d(1,{\rm diag}(e^\lambda,e^{-\lambda}))=\lambda$. In particular it satisfies the triangle inequality. Since $\det h=1$, ${\rm tr}\,h={\rm tr}\,h^{-1}=2\cosh\lambda$. The function $\lambda$ is smooth where $\lambda>0$.

Along a curve $y\mapsto H(y)$ the speed is $|H^{-1}\partial_yH|_{HS}/\sqrt2$. Since $h(H^{-1}\partial_yH)h^{-1}=2i\phi_1$, this speed equals $|\phi_1|$ in our norm (Part 9). Hence, at fixed $z$,
$$d\big(H(y_1,z),H(y_2,z)\big)\le\Big|\int_{y_1}^{y_2}|\phi_1(x_H)|\,dy\Big| .\tag{2.1}$$

**2.2 Models.** For $j\ge0$, $J=j+1$, $v_j=\log\frac{2J}{(\rho+y)^J-(\rho-y)^J}$ solves $\Delta v_j=e^{2v_j}|z|^{2j}$, and $H_j={\rm diag}(e^{v_j},e^{-v_j})$ solves $\Omega(H_j)=0$ for $\varphi_0=z^jE$ (Part 1). Its configuration is $x_W^{(j)}$. The binomial expansion has nonnegative coefficients (Part 7), so
$$\frac1{y(\rho+y)^j}\le e^{v_j}\le\frac1{y\rho^j}.\tag{2.2}$$
With $w_j=v_j+\log y+j\log r$, [15, Lemma 4.1] gives $w_j=-\frac{j(j+2)}{6r^2}y^2+O(y^4)$. In the unitary frame $h_j={\rm diag}(e^{v_j/2},e^{-v_j/2})$ one has $|\phi_z|=e^{v_j}|z|^j=e^{w_j}/y$, with the Hilbert–Schmidt norm and $|E|=1$.

**2.3 Data of the instantons.** By [3, Thm. 1.3], solutions in Dimakis' class $\mathcal{EBE}(N,K)$ correspond to triples $(P,Q,R)$. By [3, Rem. 6.2], which rests on the uniqueness theorem [3, Thm. 6.1], Taubes' instantons of type $(m,p)$ correspond to $P=z^m$, $R=z^p$ and $\deg Q\le p-1$ (and $Q(0)\ne0$ by coprimality, as in [15, Cor. 2]). Concretely, there is a global holomorphic frame in which $\varphi_0=z^mE$ and in which the sections of the line spanned by $(Q,z^p)^T$ are the ones whose $H$-norm tends to $0$ at the face. A constant diagonal change of frame normalises the constant in $P$ to $1$.

**Lemma 2.1 (distance inequality).** Let $H,K$ be metrics on the data $\varphi_0$ with $\Omega(H)=0$, and put $\lambda=d(H,K)$. Where $\lambda>0$,
$$\Delta\lambda\ \ge\ c(\lambda)\,|\varphi_0|_K^2\,\lambda-\tfrac1{\sqrt2}|\Omega(K)|_K,\qquad c(\lambda)=\frac{1-e^{-2\lambda}}{2\lambda}\ \ge\ 1-\lambda .$$
Here $|\varphi_0|_K$ and $|\Omega(K)|_K$ are Hilbert–Schmidt norms in a $K$-unitary frame, and $\Delta=\partial_y^2+4\partial_z\partial_{\bar z}$ is the flat Laplacian.

*Proof.* By [15, Lemma 5.1] (a Simpson-type identity [10]),
$$\Delta\,{\rm tr}\,h=-{\rm tr}(h\,\Omega(K))+S_y+S_z+S_\varphi .$$
Here $S_y={\rm tr}(B_yh^{-1}B_y^{\dagger_K})$ with $B_y=\partial_yh$, similarly $S_z$ with weight $4$ and $B_z=\partial_{\bar z}h$, and $S_\varphi={\rm tr}([\varphi_0,h]h^{-1}[\varphi_0,h]^{\dagger_K})$.

Work at a point, in a $K$-orthonormal eigenbasis $e_1,e_2$ of $h$, with $h={\rm diag}(e^\lambda,e^{-\lambda})$. Then ${\rm tr}(Bh^{-1}B^\dagger)=\sum_{i,j}|B_{ij}|^2/h_j$.

*(i) Kato.* The diagonal entry $B_{ii}=\langle e_i,(\partial h)e_i\rangle_K$ is the derivative of the eigenvalue $h_i$. This holds for any covariant derivative $\partial h+[Y,h]$ (Part 2). Hence
$$S_y+S_z\ \ge\ \sum_i\frac{|\nabla h_i|^2}{h_i}=2\cosh\lambda\,|\nabla\lambda|^2 .$$

*(ii) Higgs term.* Write $\varphi_0=\begin{pmatrix}\alpha&\beta\\\gamma&-\alpha\end{pmatrix}$ in this basis. Then (Part 3)
$$S_\varphi=4\sinh^2\lambda\,(|\beta|^2e^\lambda+|\gamma|^2e^{-\lambda}).$$
Nilpotency gives $\alpha^2=-\beta\gamma$, so $|\varphi_0|_K^2=2|\alpha|^2+|\beta|^2+|\gamma|^2=(|\beta|+|\gamma|)^2$. Hence
$$|\beta|^2e^\lambda+|\gamma|^2e^{-\lambda}\ge\tfrac12e^{-\lambda}|\varphi_0|^2_K,\qquad S_\varphi\ge2\sinh^2\lambda\,e^{-\lambda}|\varphi_0|_K^2 .$$

*(iii) Source.* $\Omega(K)$ is traceless and $K$-self-adjoint, so ${\rm tr}(h\Omega(K))={\rm tr}((h-\cosh\lambda)\Omega(K))$. Also $|h-\cosh\lambda|_{HS}=\sqrt2\sinh\lambda$. Hence $|{\rm tr}(h\Omega(K))|\le\sqrt2\sinh\lambda\,|\Omega(K)|_K$.

Since ${\rm tr}\,h=2\cosh\lambda$, we have $\Delta{\rm tr}\,h=2\sinh\lambda\,\Delta\lambda+2\cosh\lambda|\nabla\lambda|^2$. Combining (i)–(iii) and dividing by $2\sinh\lambda$ gives
$$\Delta\lambda\ge\sinh\lambda\,e^{-\lambda}|\varphi_0|_K^2-\tfrac{1}{\sqrt2}|\Omega(K)|_K .$$
Finally, $\sinh\lambda\,e^{-\lambda}=c(\lambda)\lambda$. $\square$

*Remarks.*
- **Sharpness.** For two diagonal solutions, $\Delta\lambda=|\varphi_0|^2(1-e^{-2\lambda})$ exactly (Part 4), which is twice the lower bound. The factor $\frac12$ is attained when $|\beta|=|\gamma|$. Linearised at $\lambda=0$, the bound reads $|[\varphi,\sigma]|^2\ge|\varphi|^2|\sigma|^2$.
- **Rate.** In the linearised regime near the face, $|\varphi_0|_K^2\approx y^{-2}$, so Lemma 2.1 gives $(\Delta-y^{-2})\lambda\ge0$. Homogeneous solutions $y^\gamma$ have $\gamma(\gamma-1)=1$, which is the origin of $\gamma_*$.

**Lemma 2.2 (barrier formulas).** The following identities hold (Part 5):
- $\Delta(\rho^as^\gamma)=\rho^{a-2}\big[\gamma(\gamma-1)s^{\gamma-2}+(a(a+1)-\gamma(\gamma+1))s^\gamma\big]$;
- $(\Delta-cy^{-2})(y^g\cosh\mu x_2\cosh\mu x_3)=y^{g-2}\cosh\mu x_2\cosh\mu x_3\,\big(g(g-1)-c+2\mu^2y^2\big)$;
- $y$ and $y/\rho^3$ are harmonic, and the Kelvin transform $f\mapsto(R_0/\rho)f(R_0^2X/\rho^2)$ preserves harmonicity. It also preserves the sign of $\Delta f$, since $\Delta(\mathcal Kf)(X)=(R_0/\rho)^5(\Delta f)(R_0^2X/\rho^2)$.

## 3. The reference metric at infinity

**Lemma 3.1.** Let $\sigma$ be a smooth complex function, $N=\begin{pmatrix}1&\sigma\\0&1\end{pmatrix}$, and $K=N^\dagger H_mN$. In the $K$-unitary frame $h_K=h_mN$, with $h_m={\rm diag}(e^{-u/2},e^{u/2})$ and $u=u_m$:
1. $h_K\varphi_0h_K^{-1}=h_m\varphi_0h_m^{-1}$. In particular $|\varphi_0|_K=|\varphi_0|_{H_m}=e^{w_m}/y$.
2. $h_K\Omega(K)h_K^{-1}=\begin{pmatrix}-D&\mathcal L\sigma\\\overline{\mathcal L\sigma}&D\end{pmatrix}$, where
$$D=e^{-2u}(4|\partial_{\bar z}\sigma|^2+|\partial_y\sigma|^2),\qquad\mathcal L\sigma=e^{u}\big(4\partial_z(e^{-2u}\partial_{\bar z}\sigma)+\partial_y(e^{-2u}\partial_y\sigma)\big).$$
3. $d(H_m,K)={\rm arccosh}\big(1+\tfrac12|\sigma|^2e^{2v_m}\big)$.
4. The $K$-configuration in the frame $h_K$ differs from $x_W^{(m)}$ (frame $h_m$) only through the terms $h_m(\partial_{\bar z}N)N^{-1}h_m^{-1}$ and $h_m(\partial_yN)N^{-1}h_m^{-1}$. These equal $e^{v_m}\partial_{\bar z}\sigma\,E$ and $e^{v_m}\partial_y\sigma\,E$ in absolute value.

*Proof.* Part 6 of verify.py proves (1) and (2) symbolically for $m=0,1,2$, using only $\Delta u+|z|^{2m}e^{-2u}=0$. The computation is uniform in $m$, because $m$ enters only through that equation. Part 7 proves (3). For (4), $\partial h_K\,h_K^{-1}=\partial h_m\,h_m^{-1}+h_m(\partial N)N^{-1}h_m^{-1}$ and $h_mEh_m^{-1}=e^{v_m}E$. $\square$

Apply this with $\sigma=-\chi(r/\rho)Q/z^p$. Then $\sigma$ is smooth on $\overline{\mathbb R^3_+}\setminus\{0\}$, since $\chi=0$ near the axis $\{z=0\}$. It is holomorphic and $y$-independent where $\chi\equiv1$. Hence:

**Corollary 3.2.** Let $q=\deg Q$ and $\nu=m+1+p-q\ge m+2\ge2$.
- $\Omega(K)=0$ outside the cone $\mathcal C=\{c_1\le r/\rho\le c_2\}$, which stays a positive angle away from the face and from the axis.
- On $\mathcal C$, $|\Omega(K)|_K\le C\rho^{-2-\nu}$, and the $K$-configuration $x_K$ (frame $h_K$) satisfies $|x_K-x_W^{(m)}|+\rho|\nabla(x_K-x_W^{(m)})|\le C\rho^{-1-\nu}$.
- Outside $\mathcal C$, $x_K=x_W^{(m)}$ exactly.

*Proof.* On $\mathcal C$, $y\ge c\rho$, so $e^{v_m}\le C\rho^{-m-1}$ by (2.2). Also $|\nabla u|\le C/\rho$ and $|\nabla^j\sigma|\le C\rho^{q-p-j}$. Insert these into Lemma 3.1(2),(4) (Part 10). $\square$

The data of the instantons (§2.3) are exactly the data for which $K$ carries the right boundary line. Where $\chi=1$, the frame change $n_\chi$ maps $(Q,z^p)^T$ to $(0,z^p)^T$, which spans the decaying line $(0,1)^T$ of $H_m$.

## 4. Proof of Theorem A

Throughout, $\lambda=d(H,K)$ with $\sup_E\lambda=\Lambda<\infty$. By Lemma 2.1 and Lemma 3.1(1), on $\{\lambda>0\}\cap E$,
$$\Delta\lambda\ \ge\ c(\lambda)\frac{e^{2w_m}}{y^2}\lambda-F,\qquad F=\tfrac1{\sqrt2}|\Omega(K)|_K\le C\rho^{-2-\nu}\mathbf 1_{\mathcal C}.\tag{4.1}$$
Near the face, $e^{2w_m}\ge1-Cs^2$ and $F=0$.

**4.1 The box lemma.**

**Lemma 4.1.** Let $0<c$, let $1<\gamma$ with $\gamma(\gamma-1)<c$, let $\gamma_-<0$ be the negative root of $\gamma_-(\gamma_--1)=c$, put $\kappa_0=\sqrt{(c-\gamma(\gamma-1))/2}$, and let $\mu\ge1$. On the box
$$B_\mu=\{|x_2|<1,\ |x_3|<1,\ 0<y<y_\mu\},\qquad y_\mu=\kappa_0/\mu,$$
let $\lambda\ge0$ be continuous, $\lambda\le M$, smooth on $\{\lambda>0\}$, with $\Delta\lambda\ge c'(X)\lambda/y^2$ there and $c'\ge c$. Then on $B_\mu$
$$\lambda\le M\Big[\Big(\frac y{y_\mu}\Big)^\gamma+\frac{\cosh\mu x_2\cosh\mu x_3}{\cosh\mu}\Big].$$
Consequently, for $y\le y_1(\gamma,c)$, $\lambda(0,0,y)\le M\,y^\gamma\big[(\gamma\log(1/y)/\kappa_0)^\gamma+2\big]$.

*Proof.* Put $b=M(y/y_\mu)^\gamma+M\cosh\mu x_2\cosh\mu x_3/\cosh\mu$ and $w_\epsilon=\lambda-b-\epsilon y^{\gamma_-}$. By Lemma 2.2, with $g=\gamma$ and $g=0$, and since $y^2\le y_\mu^2=\kappa_0^2/\mu^2$:
$$(\Delta-c'y^{-2})b\le0,\qquad(\Delta-c'y^{-2})y^{\gamma_-}=(c-c')y^{\gamma_--2}\le0 .$$
On $\{w_\epsilon>0\}$ we have $\lambda>b+\epsilon y^{\gamma_-}>0$, so
$$\Delta w_\epsilon\ge c'y^{-2}\lambda-\Delta(b+\epsilon y^{\gamma_-})\ge c'y^{-2}(b+\epsilon y^{\gamma_-})-\Delta(b+\epsilon y^{\gamma_-})\ge0 .$$
Check the boundary:
- on the lateral faces $b\ge M\ge\lambda$;
- on the top $b\ge M$;
- as $y\to0$, $\epsilon y^{\gamma_-}\to+\infty$ while $\lambda\le M$.

So $w_\epsilon<0$ near $\partial B_\mu$. By the maximum principle applied on each component of $\{w_\epsilon>0\}$, that set is empty. Let $\epsilon\to0$.

For the consequence, take $\mu=\gamma\log(1/y)$. This is admissible once $y<\kappa_0/(\gamma\log(1/y))$, and then $(y/y_\mu)^\gamma+1/\cosh\mu\le y^\gamma((\gamma\log(1/y)/\kappa_0)^\gamma+2)$ (Part 5). $\square$

No smallness of $\lambda$ at the face is assumed. The barrier $\epsilon y^{\gamma_-}$ handles the face.

**4.2 Face vanishing and the first face rate.**

**Lemma 4.2.** There are $\eta>0$, $R_0'\ge2R_0$ and $C$ with $\lambda\le C\,s$ on $\{\rho\ge R_0',\ s<\eta\}$. In particular $\lambda\to0$ at every face point of $\{\rho\ge R'_0\}$.

*Proof.* Let $p$ be a face point with $|p|\ge R_0'$. Rescale the box $p+\eta|p|\,B_\mu$ to unit size; the potential $c'/y^2$ is scale invariant. For $\eta$ small the box lies in $E\setminus\mathcal C$ and in $\{s<2\eta\}$. There (4.1) gives $c'\ge c_\Lambda(1-C\eta^2)\ge c_\Lambda/2$, with $c_\Lambda=c(\Lambda)>0$. Choose $\gamma_1\in(1,2)$ with $\gamma_1(\gamma_1-1)<c_\Lambda/2$. Lemma 4.1 with $M=\Lambda$ gives
$$\lambda(p+(0,0,y))\le C\Lambda(y/\eta|p|)^{\gamma_1}\log^{\gamma_1}(\eta|p|/y)\le C's$$
for $y<y_1\eta|p|$. Every point with $s<\eta y_1/2$ lies above such a face point. $\square$

**4.3 Decay: Kelvin barrier with source.** Put $E'=\{\rho>R_0'\}$. Let $b_1$ be the Kelvin transform (radius $R_0'$) of the bounded harmonic function on the half ball $B^+_{R_0'}$ with boundary values $\Lambda$ on the curved part and $0$ on the flat part. Then $b_1$ is harmonic on $E'$, equals $\Lambda$ on $\{\rho=R_0'\}$, vanishes on the face, and satisfies
$$b_1\le6\Lambda R_0'^2\,y/\rho^3\qquad(\rho\ge2R_0'),$$
by [15, §5.2] (the bound $b\le6My/r$ on the half ball of half the radius) and Kelvin.

Let $V=\int G(\cdot,Y)F(Y)\,dY$, where $G$ is the Dirichlet Green function of the half space, with $0\le G\le\min\big(\frac1{4\pi|X-Y|},\frac{y_Xy_Y}{2\pi|X-Y|^3}\big)$ [15, §5.2]. Then $\Delta V=-F$ and $V\ge0$.

**Lemma 4.3.** $V(X)\le C\,s\,\rho^{-2}\log\rho$ for $\rho\ge2R_0'$.

*Proof.* $F\le C|Y|^{-2-\nu}$ is supported in $\mathcal C$, where $s_Y\ge s_a>0$. Split the integral into three regions.
- *$|Y|\le\rho/2$.* Here $G\le Cy_X|Y|\rho^{-3}$, and the contribution is at most $Cy\rho^{-3}\int_{R_0'}^{\rho}r^{1-\nu}dr\le Cy\rho^{-3}\log\rho$, since $\nu\ge2$.
- *$|Y|\ge2\rho$.* Here $G\le Cy_X|Y|^{-2}$, and the contribution is at most $Cy\rho^{-1-\nu}$.
- *$\rho/2<|Y|<2\rho$.* If $s_X\le s_a/2$, then $|X-Y|\ge c\rho$ and the contribution is at most $Cy\rho^{-1-\nu}$. Otherwise $G\le(4\pi|X-Y|)^{-1}$, the contribution is at most $C\rho^{-\nu}$, and $C\rho^{-\nu}\le C's\rho^{-\nu}$ since $s\ge s_a/2$.

Since $\nu\ge2$, the total is at most $Cs\rho^{-2}\log\rho$ (Part 10). $\square$

**Proposition 4.4.** $\lambda\le b_1+V\le C\,s\,L(\rho)$ on $\{\rho\ge2R_0'\}$.

*Proof.* Let $\epsilon>0$ and $w=\lambda-b_1-V-\epsilon y$. On $\{w>0\}$ we have $\lambda>0$, so $\Delta w\ge-F+F=0$ by (4.1), since the potential term is $\ge0$. The boundary behaviour is as follows.
- On $\{\rho=R_0'\}$, $w\le0$.
- At face points, $\limsup w\le0$ by Lemma 4.2.
- On a large sphere $\{\rho=R_n\}$, $\lambda\le C s+\Lambda\mathbf 1_{\{s\ge\eta\}}$ by Lemma 4.2, while $\epsilon y=\epsilon sR_n$. So $w\le0$ there once $R_n\ge\max(C,\Lambda/\eta)/\epsilon$.

The maximum principle on $E'\cap\{\rho<R_n\}$ gives $w\le0$. Let $n\to\infty$ and then $\epsilon\to0$. $\square$

**4.4 The golden-ratio face rate.**

**Proposition 4.5.** For every $\gamma<\gamma_*$ there are $R,C,s_*$ with $\lambda\le C\,L(\rho)\,s^\gamma$ on $\{\rho\ge R,\ s<s_*\}$.

*Proof.* Fix $\gamma'\in(\gamma,\gamma_*)$ and $\theta>0$ with $\gamma'(\gamma'-1)<1-\theta$. Let $p$ be a face point with $|p|=\rho_p\ge R$. Consider the box $p+\ell B_\mu$ with $\ell=\eta\rho_p$.
- *Size.* On it, $\lambda\le M:=C\eta L(\rho_p)$ by Proposition 4.4.
- *Potential.* $c'=c(\lambda)e^{2w_m}\ge(1-M)(1-C\eta^2)\ge1-\theta$ for $\eta$ small and $R$ large.

Lemma 4.1, rescaled, gives
$$\lambda(p+(0,0,y))\le CM(y/\ell)^{\gamma'}\log^{\gamma'}(\ell/y)\le C L(\rho_p)\,s^{\gamma}$$
for $y<y_1\ell$. $\square$

**4.5 From the metric to the fields.** Let $\hat\sigma=\log(h_Khh_K^{-1})$, a Hermitian matrix with $|\hat\sigma|=\sqrt2\lambda$. Put $\hat h=e^{\hat\sigma/2}$ and $h_H=\hat hh_K$. Then $h_H^\dagger h_H=H$, and $x_H$ (frame $h_H$) is the complex gauge transform of $x_K$ (frame $h_K$) by the Hermitian matrix $\hat h$. Hence, for $|\hat\sigma|\le1$,
$$|x_H-x_K|\le C\big(|\nabla_{K}\hat\sigma|+|\hat\sigma||x_K|\big),$$
$$|\nabla(x_H-x_K)|\le C\big(|\nabla^2_K\hat\sigma|+|\nabla_K\hat\sigma|(|x_K|+|\nabla_K\hat\sigma|)+|\hat\sigma||\nabla x_K|\big).\tag{4.2}$$
In the $K$-unitary frame, [15, §5.3] gives the equation
$$P({\rm ad}\,\hat\sigma)\Delta_K\hat\sigma=-\hat\Omega_K-\mathcal Q(\hat\sigma)(\nabla_K\hat\sigma,\nabla_K\hat\sigma)-\mathcal R(\hat\sigma),\qquad P(t)=\frac{1-e^{-t}}t .$$
Here $\mathcal Q$ is bilinear with coefficients smooth in $\hat\sigma$, and $\mathcal R(\hat\sigma)=\mathcal R_1(\hat\sigma)\hat\sigma$ with $|\mathcal R_1|\le C|\varphi|^2$.

**Lemma 4.6 (scale-invariant interior estimate).** Fix $X_0$, put $r_0=\frac12y(X_0)$ if $s(X_0)<s_0$ and $r_0=\frac14\rho(X_0)s_0$ otherwise, and rescale $B(X_0,r_0)$ to the unit ball. Suppose that the rescaled reference fields are bounded in $C^2$ by a constant $C_0$, and put $\mathsf M=\sup_{B(X_0,r_0)}|\hat\sigma|$. There is $\mathsf M_0(C_0)>0$ such that, if $\mathsf M\le\mathsf M_0$,
$$\sum_{j\le2}r_0^j\sup_{B(X_0,r_0/4)}|\nabla^j_K\hat\sigma|\le C\big(\mathsf M+r_0^2\|\Omega_K\|_{L^\infty(B)}+r_0^{2+\alpha}[\Omega_K]_{\alpha,B}\big).$$

*Proof.* Work in rescaled coordinates; all coefficients are bounded with $C_0$. Write the equation as $\Delta\hat\sigma=f$. Here $f$ collects the lower-order terms of $\Delta_K$, the quadratic term, $\mathcal R$ and $\hat\Omega$, together with the factor $P({\rm ad}\hat\sigma)^{-1}$, which is bounded for $|\hat\sigma|\le1$. For $\frac12\le r<r'\le\frac34$ put $\Phi(r)=\|\nabla^2\hat\sigma\|_{L^6(B_r)}$.

*Step 1 ($W^{2,6}$ bound).* The interior $W^{2,6}$ estimate [11, Thm. 9.11], scaled, gives
$$\Phi(r)\le C(r'-r)^{-2}(\mathsf M+\|\hat\Omega\|_\infty)+C\|\nabla\hat\sigma\|_{L^{12}(B_{r'})}^2+C\|\nabla\hat\sigma\|_{L^6(B_{r'})}.$$
The Gagliardo–Nirenberg inequality [9] on balls gives $\|\nabla\hat\sigma\|^2_{L^{12}(B_{r'})}\le C\mathsf M(\Phi(r')+\mathsf M)$ and $\|\nabla\hat\sigma\|_{L^6}\le C\mathsf M^{1/2}(\Phi(r')+\mathsf M)^{1/2}$. Hence
$$\Phi(r)\le\tfrac12\Phi(r')+C(r'-r)^{-2}(\mathsf M+\|\hat\Omega\|_\infty)$$
for $\mathsf M\le\mathsf M_0$. The iteration lemma [16, Ch. V, Lemma 3.1] then gives $\Phi(\frac12)\le C(\mathsf M+\|\hat\Omega\|_\infty)$. With Morrey's embedding [11, Thm. 7.26]:
$$\|\hat\sigma\|_{C^{1,1/2}(B_{1/2})}\le C(\mathsf M+\|\hat\Omega\|_\infty).$$

*Step 2 (Schauder).* Rewrite the quadratic term as $b\cdot\nabla\hat\sigma$ with $b=\mathcal Q(\hat\sigma)(\nabla\hat\sigma,\cdot)\in C^{1/2}$, and $\mathcal R$ as $\mathcal R_1(\hat\sigma)\hat\sigma$. This gives a linear system with $C^{\alpha}$ coefficients, $\alpha\le\frac12$. The interior Schauder estimate [11, Thm. 6.2], applied componentwise to $\Delta\hat\sigma=$ (lower order) $+\,P^{-1}\hat\Omega$, gives the $C^{2}$ bound. $\square$

The estimate is linear in $\mathsf M$. This is what turns the metric bound into a field bound with the same rate. It replaces the interpolation step of [15, §5.3], which lost a power.

*Proof of Theorem A.*

*Near the face.* Let $X_0$ have $s<s_*/2$ and $\rho\ge2R$. On $B(X_0,y_0/2)$, $\Omega_K=0$, and $x_K=x_W^{(m)}$ in the frame $h_K$ (Corollary 3.2). Rescaled by $y_0$, the model fields are bounded in every $C^j$, uniformly in $X_0$: they are $N_m+O(y)$ in the notation of [15, Lemma 4.2], and $y_0\cdot y^{-1}\le2$ on the ball. Proposition 4.5 gives $\mathsf M\le CL(\rho)s^{\gamma}\le\mathsf M_0$ for $R$ large. Lemma 4.6 then gives $|\nabla^j\hat\sigma|\le Cy^{-j}L(\rho)s^\gamma$ for $j\le2$. By (4.2), with $|x_K|\le C/y$ and $|\nabla x_K|\le C/y^2$:
$$|x_H-x_K|\le C\rho^{-1}L(\rho)s^{\gamma-1},\qquad|\nabla(x_H-x_K)|\le C\rho^{-2}L(\rho)s^{\gamma-2}.$$

*Away from the face.* Let $s\ge s_*/2$. Balls of radius $r_0\sim\rho$ and Proposition 4.4 give $\mathsf M\le CL(\rho)$. Corollary 3.2 gives $r_0^2|\Omega_K|+r_0^{2+\alpha}[\Omega_K]_\alpha\le C\rho^{-\nu}\le CL(\rho)$. Hence $|x_H-x_K|+\rho|\nabla(x_H-x_K)|\le C\rho^{-1}L(\rho)$. Corollary 3.2 also gives $|x_K-x_W^{(m)}|+\rho|\nabla(x_K-x_W^{(m)})|\le C\rho^{-1-\nu}\le C\rho^{-1}L(\rho)$, supported in $\mathcal C$.

*Conclusion.* Set $\delta=\gamma-1$. As $\gamma$ ranges over $(1,\gamma_*)$, $\delta$ ranges over $(0,\delta_*)$. All configurations live on the same trivial bundle, so $e:=x_H-x_W^{(m)}$ lies in $\mathcal W'_L(\delta)$ on $\{\rho>2R\}$. Let $g_\infty$ be the unitary gauge relating the given solution to $x_H$; two unitary frames for the same holomorphic data and metric differ by a smooth unitary gauge. $\square$

*What Theorem A does not give.* It does not give the weighted derivatives $\rho\partial_\rho e$ and $\partial_\theta e$ at the scale $\rho$, so it does not give the literal (A∞) of [15]. Tangential regularity at scale $\rho$ would need an edge-calculus argument, or a difference-quotient version of Lemma 2.1 along dilations and rotations, which change $Q$. We do not claim it. Proposition 4′ shows that it is not needed.

## 5. Proof of Theorem B

We use the following facts from Taubes [1]. Write $t=y$ (Taubes' coordinate), let $x^\diamond$ be the initial data of [1, §3], and let $x=g\cdot x^\diamond$ be the instanton, with $g=g|_{s=\infty}$ from [1, Props. 5.1–5.2] and the action [1, (2.21), (4.1)].

- **(T1)** [1, Prop. 5.1]: $|g|<\kappa$ everywhere.
- **(T2)** [1, (1.9), first bullet, which the solutions of Thm. 1 satisfy]: $t|\mathfrak a|\le C$ on $(0,\infty)\times\mathbb R^2$. In particular $|\phi_1(x)|\le C/y$.
- **(T3)** [1, Lemma 3.2, third bullet]: on $F=\{t<t_0,\ |z|>4t\}$, $x^\diamond=x_W^{(k)}$ (Taubes' $(A^{(k)},\mathfrak a^{(k)})$, [15, §2.1] for the conventions).
- **(T4)** [1, §3c, Part 2 ("A key observation"), (3.26)–(3.27), and the proofs of Lemmas 3.4 and 3.5]: if $m\ge1$ or $\mu_1=0$, then on $U=\{t>\delta\}$, $\beta=b=0$, and $x^\diamond$ is the pull-back of $x_W^{(m)}$ by a unitary bundle automorphism. In particular $X^\diamond\equiv0$ there.

*Step 0 (frames).* Fix the global holomorphic frame of §2.3, in which $\varphi_0=z^mE$ and the decaying line is spanned by $(Q,z^p)^T$. Since $x=g\cdot x^\diamond$, the data $x^\diamond$ have the same holomorphic structure, with metric $K_\diamond$ in this frame. Then $K_\diamond^{-1}H$ is conjugate to $gg^\dagger$, so
$$d(H,K_\diamond)\le\Lambda_1:=2\log\kappa$$
by (T1). Norms for $H$ and $K_\diamond$ are comparable, so both have the same decaying line.

*Step 1 (the face region $F$).* By (T3), on $F$ there is a frame relation $c$: $K_\diamond=c^\dagger H_kc$ with $c\,z^mE\,c^{-1}=z^kE$. The region $F$ is connected, and each slice $\{z\}\times(0,\min(t_0,|z|/4))$ is an interval. So $c$ is $y$-independent and holomorphic on $\mathbb C^*$. Every holomorphic $c$ conjugating $z^mE$ to $z^kE$ has the form $\pm{\rm diag}(z^p,z^{-p})\begin{pmatrix}1&b\\0&1\end{pmatrix}$, because the stabiliser of $E$ is the upper unipotent group. Here $c$ is determined up to a constant unitary diagonal factor, coming from the phase conventions of the models. Such a factor changes no distance. The modulus of a constant diagonal factor must be $1$, since both normalisations $\varphi_0=z^mE$ and $z^kE$ are exact. The decaying line of $H_k$ is $(0,1)^T$, so $c(Q,z^p)^T\in{\rm span}(0,1)^T$, which forces $b=-Q/z^p$. Then $gc^{-1}={\rm diag}(z^{-p},z^p)$ with $g=n_1$ (Part 8), and
$$d(K_\diamond,K)=|w_k-w_m|\le C\quad\text{on }F\cap\{\rho>R_0\}$$
(Part 8). Indeed, $K=n_1^\dagger H_mn_1$ on $F$ for $\rho$ large, because $r/\rho\ge4/\sqrt{17}>c_2$ there once we choose $c_2<0.97$. Moreover $|w_k-w_m|=O(s^2)$ at the face (Part 7).

*Step 2 (the region $U$).* By (T4), on $U=(\delta,\infty)\times\mathbb C$ the same reasoning gives $K_\diamond=f^\dagger H_mf$ with $f=\pm\begin{pmatrix}1&b\\0&1\end{pmatrix}$ and $b$ entire.

*Step 3 (vertical transfer pins $b$).* Fix $z$ with $|z|>8t_0$, and let $P_1=(t_0/2,z)\in F$ and $P_2=(2\delta,z)\in U$. By (2.1), (T2), and the model bound $|\phi_1(x_K)|\le C/y$ (Corollary 3.2), both $d(H(P_1),H(P_2))$ and $d(K(P_1),K(P_2))$ are at most $C\log(4\delta/t_0)$. With Steps 0–1 and the triangle inequality, $d(K_\diamond,K)(P_2)\le C$ for all large $|z|$. By Lemma 3.1(3), applied with $\sigma=-Q/z^p-b$ (since $K_\diamond^{-1}K$ is conjugate to $H_m^{-1}(n_1f^{-1})^\dagger H_m(n_1f^{-1})$),
$$|Q/z^p+b(z)|\,e^{v_m(2\delta,z)}\le C .$$
By (2.2), $e^{v_m(2\delta,z)}\ge c\,|z|^{-m}$ for $|z|$ large. Hence $|b(z)|\le C(1+|z|^m)$, and $b$ is a polynomial of degree $\le m$ by Cauchy's estimates.

*Step 4 (bounded distance on $U$).* On $U\cap E$, Lemma 3.1(3) with $\sigma=-\chi Q/z^p-b$ and (2.2) give
$$|\sigma|e^{v_m}\le\frac{C(1+|z|^m)}{y\rho^m}+C\,\mathbf 1_{\{r\ge c_1\rho\}}\frac{\rho^{q-p}}{y\rho^m}\le\frac C\delta .$$
So $d(K_\diamond,K)\le C$ there, and $d(H,K)\le\Lambda_1+C$.

*Step 5 (the slab).* For $X=(t,z)\in E$ with $t_0\le t\le2\delta$, (2.1) and (T2) give
$$d(H,K)(X)\le d(H,K)(2\delta,z)+2C\log(2\delta/t_0)\le C .$$

*Conclusion.* Since $E\subset F\cup U\cup\{t_0\le t\le2\delta\}$ for $R_0$ large, (C0∞) holds. $\square$

*The excluded case.* When $m=0$ and $\mu_1\ne0$, Taubes uses the cut-off $\varpi^\ddagger_\delta$ of [1, (3.26)]. Then $x^\diamond$ is a model only above $t=\delta(1+|z|^2)^{1/4}$. The vertical transfer costs $C\log|z|$, which only gives $|b|\le C|z|^{N}$ for some $N$. We do not know that $b$ is then constant, so this case is left open. It does not affect Corollary C, which uses $p=1$.

## 6. Proposition 4′ and Corollary C

Recall [15, Def. 6.1]. With $V\in\{\rho\partial_\rho,s\partial_s,\partial_\theta\}$, $\mathcal W(\alpha,\delta)$ requires:
- $|a|+\sum_V|Va|\le C\rho^{-1}\min(1,\rho)^\alpha s^\delta$ near the face;
- $|a|+\rho|\nabla a|\le C\rho^{-1}\min(1,\rho)^\alpha$ elsewhere.

By [15, Lemma 6.2], $\mathcal W(\alpha,\delta)\subset\mathcal W'(\alpha,\delta)$.

**Lemma 6.1 (energy).** If $a\in\mathcal W'(\alpha,\delta)$ on $U$ with $\alpha,\delta>\frac12$, then $\mathcal E_3(a;U)<\infty$ and $\sup_Uy|a|<\infty$. The same holds for $\mathcal W'_\ell(\delta)$ with $\ell\le C\min(1,\rho)^\alpha$.

*Proof.* Near the face, $|\nabla a|^2+|a|^2/y^2\le C\rho^{-4}\ell^2s^{2\delta-2}$; elsewhere it is at most $C\rho^{-4}\ell^2$. Integrate with $d^3X=\rho^2d\rho\,ds\,d\theta$. Also $y|a|\le C\ell s^{1+\delta}$. (Part 10.) $\square$

The derivative $\nabla$ is the ordinary one in the given gauge. If Question 6.2 is read with the covariant derivative $\nabla_{A_W}$ of the model instead, the energies differ by at most $\int|A_W|^2|a|^2\le C\int|a|^2/y^2$, since $|A_W|\le|\nabla v_k|\le C/\rho$. So finiteness is the same.

**Lemma 6.2 (gluing with ordinary derivatives).** Let $W$ be a region with $\rho\in[R_1,2R_1]$ and $s<s_0$. Let $g,g'$ be gauges on $W$ with $e=g\cdot x-x_W^{(k)}$ and $e'=g'\cdot x-x_W^{(k)}$ in $\mathcal W'(\cdot,\delta)$, $\delta>0$. Then $\tau=g'g^{-1}=\exp\xi$ with
$$|\xi|\le Cs^{1+\delta},\qquad|\nabla\xi|\le Cs^\delta,\qquad|\nabla^2\xi|\le Cs^{\delta-1}$$
(rescaled to $\rho\sim1$). For a cut-off $\chi(\rho)$, $\exp(\chi\xi)g\cdot x-x_W^{(k)}\in\mathcal W'(\cdot,\delta)$ on $W$.

*Proof.* Rescale to $\rho\sim1$.
- *Higgs fields.* From $\tau(\phi^W_a+e_a)=\phi^W_a+e'_a$ and $\phi^W_a=y^{-1}(n_a+O(s^2))$, with $n_a$ an orthonormal frame, we get $|\tau-1|\le Cys^\delta$.
- *Connection.* From $d\tau\,\tau^{-1}=({\rm Ad}\,\tau-1)A^W+{\rm Ad}(\tau)e^A-e'^A$ and $|A^W|+|\nabla A^W|\le C$, we get $|d\tau|\le Cs^\delta$.
- *Second derivatives.* Differentiating once more, $|\nabla^2\tau|\le C(s^\delta+|\nabla e|+|\nabla e'|)\le Cs^{\delta-1}$.

For the interpolated gauge $\tau_\chi=\exp(\chi\xi)$, the Higgs difference is $(\tau_\chi-1)\phi^W+\tau_\chi e$. It is bounded by $Cs^{1+\delta}/y+Cs^\delta\le Cs^\delta$. Its gradient is bounded by $C(s^\delta/y+s^{1+\delta}/y^2+s^{\delta-1})\le Cs^{\delta-1}$. The connection difference and its gradient are bounded the same way, using $|\nabla^2\tau_\chi|\le Cs^{\delta-1}$ (Part 10). $\square$

*Proof of Proposition 4′.* We follow [15, §6], with $\mathcal W'$ in place of $\mathcal W$.
- *On $\{\rho>R_1\}$.* Put $G_\infty=G^{(p)}_\infty g_\infty$, with $G^{(p)}_\infty={\rm Ad}(q^p)$ from [15, Thm. 1(3)]. Then $G_\infty\cdot x-x_W^{(k)}=a_\infty+{\rm Ad}(G^{(p)}_\infty)e$. Here $a_\infty\in\mathcal W(0,1)\subset\mathcal W'(0,1)$ [15, Thm. 1(3)]. Also $|\nabla({\rm Ad}(G^{(p)}_\infty)e)|\le C\rho^{-1}|e|+|\nabla e|$, since $|\nabla G^{(p)}_\infty|\le C/\rho$ [15, §6]. So the sum lies in $\mathcal W'_1(\min(\delta,1))$.
- *On $\{\rho<2R_1\}$.* Take $G_{2R_1}$ from [15, Thm. 3(c)]: $G_{2R_1}\cdot x-x_W^{(k)}\in\mathcal W(1-\varepsilon,1)\subset\mathcal W'(1-\varepsilon,1)$.
- *Gluing.* On the overlap near the face, glue with Lemma 6.2. On the compact rest of the overlap, extend the gauge using $\pi_2(SO(3))=0$, as in [15, §6].
- *Conclusion.* Lemma 6.1 gives the energy bound and $\sup y|\tilde a|<\infty$. $\square$

*Proof of Corollary C.*
- *Hypothesis at infinity.* For $k\ge2$ take $(m,p)=(k-2,1)$. Then $p=1$, so the constants $\mu_j$ of [1, (3.23)] do not occur, and Theorem B applies. Theorems A and B give (A∞′) with any $\delta\in(\frac12,\delta_*)$.
- *Finite energy.* Proposition 4′ gives finite energy and $\sup y|\tilde a|<\infty$ relative to $x_W^{(k)}$.
- *Not gauge equivalent.* By [1, (1.10)], $y|\phi_1(x)|\to m+1=k-1$ along the axis as $y\to\infty$. By [15, Lemma 2.2], $y|\phi_1(x_W^{(k)})|=k+1$ there, and $|\phi_1|$ is gauge invariant. $\square$

## 7. Consistency checks demanded by the referee reports of [15]

1. **Ordinary versus weighted derivatives.** Every derivative bound proved in this paper is for ordinary derivatives, with the loss $s^{-1}$ per derivative near the face (Lemma 4.6, scaled by $y$). This is the loss of the Nahm-pole regularity theory (compare [8, §2.2]). No bound with $s^\delta$ on ordinary derivatives is claimed. Weighted derivatives are used only through the cited [15, Thm. 3(c)] and [15, Thm. 1(3)], and there only through the inclusion $\mathcal W\subset\mathcal W'$.
2. **Compatibility with the explicit face terms.** At a face point with large $r$, the two models have $|\phi_1(x_W^{(j)})|=\frac1y+\frac{j(j+2)}{3r^2}y+O(y^3)$ [15, (Lemma 2.2)]. Theorem A gives $\big||\phi_1(x)|-|\phi_1(x_W^{(m)})|\big|\le C\rho^{-1}L(\rho)s^\delta$ with $\delta<1$. As $y\to0$ at fixed $r$ this allows any linear coefficient $c(z)$. The knot side [15, Thm. 3(c)] allows $c(z)\ne\frac{k(k+2)}{3r^2}$ as well. The mismatch between the two models, $\frac{k(k+2)-m(m+2)}{3r^2}y$, sits in $a_\infty$, which is $O(s/\rho)$ and lies in $\mathcal W'(0,1)$. So the inconsistency of the v2 formulation of [15] (ordinary derivatives with a factor $s^\delta$ force $c(z)$ to equal both model values) does not arise.
3. **The metric picture.** In Step 1 of §5, $d(K_\diamond,K)=|w_k-w_m|=\frac{|k(k+2)-m(m+2)|}{6r^2}y^2+O(y^4)$. This is exactly the metric form of the same linear face term. It is $O(s^2)\le O(s^\gamma)$, consistent with Proposition 4.5.
4. **The definition in Question 6.2.** The energy there is $\int(|\nabla\tilde a|^2+|\tilde a|^2/y^2)$ over all of $\mathbb R^3_+$ in one smooth gauge, together with $\sup y|\tilde a|<\infty$. Proposition 4′ produces one smooth global gauge $G$, and Lemma 6.1 bounds exactly this integral (with either reading of $\nabla$, §6) and $\sup y|\tilde a|$.
5. **Numerics.** For $(m,p)=(0,1)$ the finite-difference study of [15, §7.2] observed $\max|J_1-1|\sim\rho^{-2.98}$ at infinity, where $J_1=y|\phi_1|$. Theorem A gives $|J_1-1|\le y|e|\le C\rho^{-2}\log\rho$. The bound is consistent with the observation, though not sharp.

## 8. Status of claims

- **Proved here:**
  - Lemmas 2.1, 2.2, 3.1 (with symbolic verification), Corollary 3.2, Lemmas 4.1–4.3 and 4.6, Propositions 4.4 and 4.5;
  - Theorem A, given (C0∞) and classical elliptic theory [11], [9], [16];
  - Lemmas 6.1 and 6.2.
- **Proved here, using cited theorems:**
  - Theorem B, given [1, Thm. 1, (1.9), Lemma 3.2, §3c, Prop. 5.1] and [3, Thm. 1.3, Rem. 6.2];
  - Proposition 4′, given [15, Thm. 1(3)] and [15, Thm. 3(c)]. The latter rests on [4, Thm. 9.6], [4, §4] and [5];
  - Corollary C, given all of the above.
- **Numerical or consistency only:** §7(5); the [NUM] and random-sample checks in verify.py.
- **Not proved:**
  - the literal (A∞) of [15] with weighted derivatives at scale $\rho$;
  - Theorem B for $m=0$, $\mu_1\ne0$;
  - any face rate beyond $s^{\gamma}$ with $\gamma<\gamma_*$ (the true rate is presumably $s^2$ for $\lambda$);
  - a knot-neighbourhood estimate independent of [4].

*What exactly follows for Question 6.2.* For every $k\ge2$ there are smooth EBE solutions $\tilde x$, namely Taubes' instantons of type $(k-2,1)$ and all types covered by Theorem B, with $\int_{\mathbb R^3_+}(|\nabla\tilde a|^2+|\tilde a|^2/y^2)<\infty$ and $\sup y|\tilde a|<\infty$ for $\tilde a=G\cdot\tilde x-x_W^{(k)}$, which are not gauge equivalent to $x_W^{(k)}$. So the answer to Question 6.2 is **negative for every $k\ge2$**, modulo the cited results listed above. For $k=1$ the answer is positive within Dimakis' classes [15, Cor. 2]. For $k=0$ the question is not addressed here. By [14, Thm. 3, Rem. 6.3], the periodic analogue of [14, Thm. 1] therefore fails for $k\ge2$.

## 9. Verification

`verify.py` (python3, sympy 1.14, mpmath) runs 59 checks in about 23 seconds. It prints OK/FALLA for each check and ends with `FALLOS = 0`; its output is `verify_output.txt`. It has 11 parts.
- **Part 1.** Normalisation of the models and of $\Omega$.
- **Part 2.** The Kato step: the diagonal of a covariant derivative in the eigenbasis is the derivative of the eigenvalues (exact, for a general $SU(2)$ path and any connection term).
- **Part 3.** The formula for $S_\varphi$, nilpotency, the lower bound and the source term.
- **Part 4.** Sharpness in the diagonal case, including the exact pair $(H_2,\,{\rm diag}(z^{-1},z)^\dagger H_0\,{\rm diag}(z^{-1},z))$.
- **Part 5.** Barrier identities, the golden ratio, $\delta_*>\frac12$ and the Kelvin transform.
- **Part 6.** Lemma 3.1, symbolically for $m=0,1,2$.
- **Part 7.** The bound (2.2), the face expansion of $w_k-w_m$ and the unipotent distance formula.
- **Part 8.** The frames of §5, Step 1.
- **Part 9.** The speed formula (2.1).
- **Part 10.** Exponent bookkeeping.
- **Part 11.** Consistency with the retained numerics of [15].

Random-sample and rational-point checks are consistency checks of identities proved in the text. `verify.mpl` mirrors the exact Parts 1, 3, 5, 7, 8 and 10 under the Maple rules. It has not been executed, because Maple is not available here.

## References

1. C. H. Taubes, *The existence of instanton solutions to the $\mathbb R$-invariant Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$*, arXiv:2102.04290 (Thm. 1; (1.9), (1.10); (2.21); §3a–c, (3.23)–(3.29); Lemmas 3.2, 3.5; (4.1); (5.1); Props. 5.1, 5.2).
2. C. H. Taubes, *The $\mathbb R$ invariant solutions to the Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$ with generalized Nahm pole asymptotics*, arXiv:1903.03539.
3. P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: nilpotent Higgs field*, arXiv:2209.11101 (Defs. 1.1, 1.2, 2.3; Thms. 1.3, 3.2, 5.4, 6.1; Prop. 5.3; Rems. 5.5, 6.2; §3; (5.27); §5.3).
4. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Math. Phys. 373 (2020); arXiv:1712.00835 (§4; Prop. 4.3; Thm. 9.6).
5. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The influence of Solomon Lefschetz in geometry and topology, Contemp. Math. 621 (2014); arXiv:1311.3167.
6. S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019); arXiv:1710.10645.
7. S. He, R. Mazzeo, *The extended Bogomolny equations with generalized Nahm pole boundary conditions, II*, Duke Math. J. 169 (2020); arXiv:1806.06314 (§8).
8. S. He, R. Mazzeo, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274 (§2.2, Thm. 2.4 and the estimates after it).
9. L. Nirenberg, *On elliptic partial differential equations*, Ann. Scuola Norm. Sup. Pisa 13 (1959), 115–162 (Gagliardo–Nirenberg inequalities).
10. C. Simpson, *Constructing variations of Hodge structure using Yang–Mills theory and applications to uniformization*, J. Amer. Math. Soc. 1 (1988), 867–918 (Lemma 3.1).
11. D. Gilbarg, N. Trudinger, *Elliptic partial differential equations of second order*, Springer (Thms. 6.2, 7.26, 9.11).
12. rStation math_37 v1, https://rstation.ai/problems/math/papers/37/v1.
13. rStation math_38 v1, https://rstation.ai/problems/math/papers/38/v1.
14. rStation math_40 v1, *Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class*, https://rstation.ai/problems/math/papers/40/v1 (§1.1, Thm. 1, Thm. 3, Question 6.2, Rem. 6.3).
15. rStation math_41 v1, *Finite energy at a colored knot: knot rigidity and an explicit matching gauge, with local asymptotics of Taubes' instantons*, https://rstation.ai/problems/math/papers/41/v1 (Thm. 1(3), Cor. 2, Thm. 3, Prop. 4, Def. 6.1, Lemmas 2.2, 4.1, 4.2, 5.1, 6.2, 6.3, §§5.2–5.3, §7).
16. M. Giaquinta, *Multiple integrals in the calculus of variations and nonlinear elliptic systems*, Annals of Math. Studies 105, Princeton (1983) (Ch. V, Lemma 3.1).

# Finite energy at a colored knot: knot rigidity and an explicit matching gauge, with local asymptotics of Taubes' instantons

**Abstract.** See `abstract.md`.

---

## 1. Introduction

### 1.1 The question

Let $\mathbb R^3_+=\{X=(x_2,x_3,y):y>0\}$, $z=x_2+ix_3=re^{i\theta}$, $\rho=|X|$, $s=y/\rho\in(0,1]$. For an integer $k\ge0$ let $x_W^{(k)}$ be Witten's straight-knot model solution of the extended Bogomolny equations (EBE), with gauge group $SO(3)$, in the smooth abelian gauge of [14, §1.1] (recalled in §2). For a configuration $x$, a smooth gauge transformation $G$ and an open set $U$ put
$$\tilde a=G\cdot x-x_W^{(k)},\qquad \mathcal E_3(\tilde a;U)=\int_U\Big(|\nabla\tilde a|^2+\frac{|\tilde a|^2}{y^2}\Big)d^3X,\qquad \mathcal E_3(\tilde a)=\mathcal E_3(\tilde a;\mathbb R^3_+).$$
rStation math_40 [14] reduces the classification of finite-energy Kapustin–Witten solutions on $S^1\times\mathbb R^3_+$ to the following question [14, Question 6.2], quoted verbatim:

> **Question 6.2 (the missing piece).** Let $k\ge0$. Let $\tilde x$ be a smooth solution of the extended Bogomolny equations on $\mathbb R^3_+$ with $\int_{\mathbb R^3_+}(|\nabla\tilde a|^2+|\tilde a|^2/y^2)<\infty$ and $\sup y|\tilde a|<\infty$, where $\tilde a=\tilde x-x_W^{(k)}$ in some gauge. Is $\tilde x$ gauge equivalent to $x_W^{(k)}$?

[14, Remark 6.2′] names Taubes' solutions [1, Thm. 1] as candidate counterexamples for $k\ge2$, and [14, Remark 6.3] gives the dilation argument relating the question to small-energy rigidity. We call these solutions *instantons of type $(m,p)$*, with $m\ge0$, $p\ge1$. They are EBE solutions that look like $x_W^{(k)}$, $k=m+2p$, as $y\to0$ and like $x_W^{(m)}$ as $y\to\infty$, in the sense of [1, (1.10)].

This paper does not answer Question 6.2. It proves what the finite-energy condition forces at the knot and at infinity, constructs the gauge that matches two models of different weights, and proves local asymptotics of the instantons at the knot.

### 1.2 Main results

For $K=k+1$ put $g_k(c)=((1+c)^K-(1-c)^K)/(2K)$ and $h_K(c)=Kc^2+c(1-c^2)g_k'(c)/g_k(c)$. Then $y|\phi_1|=h_K(y/\rho)$ for $x_W^{(k)}$ (Lemma 2.2). A face point $p$ is a *knot point of weight $k_1$* of a configuration $x$ if, for every $\omega$ in some nonempty open set $\Gamma$ of directions in the open upper hemisphere,
$$\lim_{r\to0}\,y\,|\phi_1(x)|(p+r\omega)=h_{K_1}(\omega_y).\tag{1.1}$$
Both sides are gauge invariant. The limit is only required pointwise in $\omega$.

**Theorem 1 (main theorem; unconditional).** Let $k\ge0$ and let $x$ be a smooth configuration on $\mathbb R^3_+$ with $\mathcal E_3(G\cdot x-x_W^{(k)})<\infty$ for some smooth $G:\mathbb R^3_+\to SO(3)$. No field equations are assumed.
1. *(knots)* No face point $p\ne0$ is a knot point of $x$ of any weight $k_1\ge1$. If the origin is a knot point of weight $k'$, then $k'=k$.
2. *(parity)* Suppose that for some $0<R_1$ and $\eta\in(0,R_1)$ there is a smooth gauge $g$ on the shell $S=\{R_1-\eta<\rho<R_1+\eta\}\cap\mathbb R^3_+$ with $y\,|g\cdot x-x_W^{(N)}|\to0$ as $y\to0$, uniformly on $S$. Then $N\equiv k\pmod 2$.
3. *(the matching gauge)* Let $q=\sqrt{1+s^2}\,(x_2-x_3\mathbf k)/\rho+s^2\,\mathbf i$, a unit quaternion depending smoothly on $X\in\mathbb R^3_+$, and $G^{(p)}_\infty={\rm Ad}(q^p)$, with $\mathbf i,\mathbf j,\mathbf k\leftrightarrow t_1,t_2,t_3$. If $k-m=2p$, then $a_\infty=G^{(p)}_\infty\cdot x_W^{(m)}-x_W^{(k)}$ is smooth and homogeneous of degree $-1$, and $y\,a_\infty$ is real-analytic near the face and vanishes there to at least second order in $s$. This holds for every $m\ge0$ and $p\ge1$ (§4, a proof uniform in the weights). Consequently, for $V\in\{\rho\partial_\rho,\ s\partial_s,\ \partial_\theta\}$,
$$|a_\infty|+|Va_\infty|\le C\,s/\rho\ \ (s\le\tfrac12),\qquad |\nabla a_\infty|\le C\rho^{-2},\qquad \mathcal E_3(a_\infty;\{\rho>1\})<\infty .$$
   If $k-m$ is odd, then $\mathcal E_3(G\cdot x_W^{(m)}-x_W^{(k)};S)=\infty$ for every smooth gauge $G$ on any shell $S$.

**Corollary 2 (inside Dimakis' classification).** Let $x\in\mathcal{EBE}(N,K)$ [3, Defs. 1.1, 2.3], with holomorphic data $(P,Q,R)$ [3, Def. 1.2, Thm. 1.3], and suppose $\mathcal E_3(G\cdot x-x_W^{(k)})<\infty$ for some smooth $G$. Then $K=k$ and $x$ has exactly one knot point, at the origin; $P=az^N$ and $R=z^p$ with $N+2p=k$. Either $p=0$, so $(Q,R)=(0,1)$ and $x=x_W^{(k)}$ by [3, Thm. 1.3], or $p\ge1$, $Q(0)\ne0$ and $\deg Q<p$, so $x$ is an instanton of type $(N,p)$ in Dimakis' description; [3, Rem. 6.2] identifies these with Taubes' family. If in addition $N=k$, then $x=x_W^{(k)}$. Question 6.2 at $k=1$ therefore has a positive answer within these classes.

**Theorem 3 (Taubes' instantons near the knot and the face).** Let $x=g\cdot x^\diamond$ be an instanton of type $(m,p)$ as constructed in [1, §§3–5], with $h=g^\dagger g$ and polar decomposition $g=u\,h^{1/2}$.
- *(a) proved here, from [1, Prop. 5.1, Lemma 3.2].* $0\le{\rm tr}\,h+{\rm tr}\,h^{-1}-4\le Cy$ on $\{\rho<r_2\}\cup\{y<y_2\}$.
- *(b) proved here, from (a), [1, Prop. 5.1] and linear elliptic theory.* $|u^{-1}\cdot x-x_W^{(k)}|\le Cy^{-5/6}$ on $\{\rho<r_2/4\}\cup\{y<y_2/4,\ \rho<R\}$, for every $R$.
- *(c) with the polyhomogeneity theorem [4, Thm. 9.6] and the Nahm-pole face regularity of [4, §4], [5].* For every $R$ and every $\varepsilon>0$ there is a smooth gauge $G_R$ on $\{\rho<R\}$ such that $a=G_R\cdot x-x_W^{(k)}$ lies in the weighted class $\mathcal W(1-\varepsilon,1)$ of Definition 6.1. That is, near the face $|a|+\sum_V|Va|\le C\rho^{-1}\min(1,\rho)^{1-\varepsilon}s$, with only weighted derivatives $V$ controlled. Hence
$$\mathcal E_3(G_R\cdot x-x_W^{(k)};\{\rho<R\})<\infty,\qquad \sup_{\rho<R}y\,|G_R\cdot x-x_W^{(k)}|<\infty .$$

Ordinary derivatives are controlled only in the weaker form $|\nabla a|\le C\rho^{-2}\min(1,\rho)^{1-\varepsilon}$, without a factor $s$. This is consistent with the linear face term $\frac{j(j+2)}{3r^2}\,y$ in $|\phi_1(x_W^{(j)})|=\frac1y+\frac{j(j+2)}{3r^2}y+O(y^3)$ (verify.py Part 14), which differs for $j=k$ and $j=m$.

**Proposition 4 (what remains; conditional).** Suppose, in addition, that an instanton satisfies

- **(A∞)** there are $R_1$, $\delta>\frac12$ and a smooth gauge $g_\infty$ on $\{\rho>R_1\}$ such that $e_\infty=g_\infty\cdot x-x_W^{(m)}\in\mathcal W(0,\delta)$ there.

Then there is a smooth $G$ on $\mathbb R^3_+$ with $G\cdot x-x_W^{(k)}\in\mathcal W(1-\varepsilon,\min(\delta,1))$. Hence $\mathcal E_3<\infty$ and $\sup y|\tilde a|<\infty$, and $x$ answers Question 6.2 negatively at $k=m+2p$.

(A∞) only constrains weighted derivatives and allows linear face terms. It is satisfied by $x_W^{(m)}$ itself, and it is compatible with Theorem 3(c) and with the model face expansions; Remark 6.4 checks this. We do not prove (A∞) for any instanton.

*Numerical evidence (qualitative).* For $(m,p)=(0,1)$ a twisted rotation symmetry reduces the EBE to two PDEs in $(y,r)$ (§7.1, proved). A finite-difference study (§7.2) shows two gauge invariants converging to those of $x_W^{(2)}$ at the knot like $\rho^{1.38}$, and to those of $x_W^{(0)}$ at infinity like $\rho^{-3}$. These rates are stable under radial refinement $\Delta\xi=0.05,0.025,0.0125$, angular refinement and a change of the outer endpoint. This is consistent with (A∞), but it is evidence about two invariants only, not about the full field.

### 1.3 Relation to prior work, and what is new

- **rStation.**
  - math_37 [12] proves a one-sided comparison theorem for the scalar (abelian) equation.
  - math_38 [13] proves linear non-degeneracy at weight one. That is the only weight at which such a statement is available, and there are no instantons at weight one.
  - math_40 [14] proves uniqueness in the finite-energy class on $\mathbb R_t\times\mathbb R^3_+$. It also reduces the periodic case to Question 6.2, identifies Taubes' instantons as candidates, and gives the dilation and small-energy argument; we do not repeat those.
  - None of [12]–[14] contains Theorem 1, Corollary 2 or Theorem 3.
- **Taubes.** [1, Thm. 1] constructs the instantons; [1, Prop. 5.1] bounds the complex gauge and its first derivative; [2, Thm. 2, Props. 8.1–8.2] give the qualitative asymptotics without rates. No energy statement relative to a model appears.
- **Dimakis.** [3, Thm. 1.3] classifies $\mathcal{EBE}(N,K)$ by holomorphic data, and [3, Rem. 6.2] identifies Taubes' solutions. [3, Def. 2.3] builds a rate $\rho^\varepsilon$ into the definition of a knot point. [3, Thm. 5.4] states weighted estimates for the metric correction in the space $\mathcal A_{k,a,\beta}$ of [3, (5.27)], with weight $\psi^{2-\epsilon}R^{1+\epsilon}\hat\rho^{-(1+\beta)}$; its proof is deferred to [7, §8]. [3, §5.3] invokes [4] for the exact asymptotics. If [3, Thm. 5.4] and [3, Rem. 6.2] are granted, a rate at the knot for Taubes' solutions follows from [3]. Theorem 3 gives an independent proof that uses only the estimates stated in Taubes' own construction [1, Prop. 5.1, Lemma 3.2].
  - [3] contains no energy statement relative to a model.
  - [3] contains nothing about the energy class (Theorem 1, Corollary 2).
  - [3] does not contain the explicit matching gauge.
- **Mazzeo–Witten** [4] give the indicial roots (Prop. 4.3) and polyhomogeneity at a knot (Thm. 9.6). We use [4, Thm. 9.6] only through its stated conclusion: polyhomogeneity, with regularity under weighted vector fields.

*New here* (after a focused check of the papers above; not a priority guarantee):
1. Theorem 1(1)–(2) and Corollary 2.
2. The explicit null-homotopy gauge ${\rm Ad}(q^p)$ with its exact face expansion, and the parity converse (Theorem 1(3)).
3. The barrier proof of a power rate for Taubes' instantons from Taubes' estimates, and the resulting local finiteness of their energy (Theorem 3).
4. The reduction of the global question to the weighted hypothesis (A∞), checked to be consistent (Proposition 4).

## 2. Conventions, models, invariants

**2.1 Fields.** As in [14]: $\mathfrak{so}(3)=(\mathbb R^3,\times)$ with basis $t_1,t_2,t_3$. An EBE configuration is $x=(A,\phi_1,\phi_2,\phi_3)$, with $A=A_2dx_2+A_3dx_3+A_ydy$ and $\phi_1$ the Higgs component along the knot. The equations are the vanishing of the seven reduced quantities of [14, §2]. A gauge transformation $g$ acts by $\phi_a\mapsto g\phi_a$ and $A_i\mapsto gA_i-\omega_i$, where $[\omega_i\times]=(\partial_ig)g^{-1}$. In the matrix picture $t_a\leftrightarrow-\frac i2\sigma_a$ and $|u|^2=-2\,{\rm tr}\,u^2$. Taubes' $\sigma_a$ and norm [1, (1.4), (1.11)] correspond to $-2t_a$ and to half our norm.

**2.2 Witten's models.** With $K=k+1$, $v_k=\log\frac{2K}{(\rho+y)^K-(\rho-y)^K}$ and $z^k=a+ib$:
$$A=\partial_3v\,t_3\,dx_2-\partial_2v\,t_3\,dx_3,\quad\phi_1=\partial_yv\,t_3,\quad\phi_2=-e^{v}(b\,t_1+a\,t_2),\quad\phi_3=-e^{v}(a\,t_1-b\,t_2).$$
For general $v$, this configuration satisfies all reduced equations except $\mu=-(\Delta v-e^{2v}|z|^{2k})t_3$, and $v_k$ solves $\Delta v=e^{2v}|z|^{2k}$ (Part 1; [12, Thm. 2]). Here $\phi_z=\phi_2-i\phi_3=ie^vz^k(t_1+it_2)$.

**Lemma 2.1.** The rotation $R(\chi)$ about $t_3$ maps $\phi_z\mapsto e^{-i\chi}\phi_z$ and $A\mapsto A-d\chi\,t_3$ (Part 5).

**Lemma 2.2.** For $x_W^{(k)}$, $y|\phi_1|=h_K(c)$ with $c=y/\rho$ [14, Prop. 5.1(2)]. Moreover, for every $k$:
- $h_K(1)=K$;
- $h_K(c)\to1$ as $c\to0$;
- $h_K-1-kc^2=(1-c^2)(cg_k'-g_k)/g_k\ge0$;
- $h_K\ne h_{K'}$ for $K\ne K'$. Both are real-analytic on $(0,1]$, so they differ on a dense open set.

At fixed $r>0$, $|\phi_1|=\frac1y+\frac{k(k+2)}{3r^2}y+O(y^3)$.

For any two configurations and any gauge $g$, $\big||\phi_1(x)|-|\phi_1(x')|\big|\le|g\cdot x-x'|$.

*Proof.* By the binomial theorem, $g_k(c)=\frac1K\sum_{i\ \rm odd}\binom Kic^i$. So $g_k(c)=c+O(c^3)$, and $cg_k'-g_k=\frac1K\sum_{i\ \rm odd}(i-1)\binom Kic^i$ has nonnegative coefficients. This gives the second and third items. At $c=1$ the second term of $h_K$ vanishes, so $h_K(1)=K$, which gives the first and fourth. The face expansion is Lemma 4.1 below. The last inequality holds because $|\phi_1|$ is gauge invariant. Parts 7 and 14 re-check these statements for $k\le6$ and $k\le4$, and Part 17 checks the face expansion symbolically in $k$. $\square$

**2.3 The holomorphic picture.** Let $H=h^\dagger h$ be a Hermitian metric of determinant one on the trivial $\mathbb C^2$-bundle, and let $\varphi_0(z)$ be holomorphic, $y$-independent and nilpotent. The physical fields are
$$\phi_z=h\varphi_0h^{-1},\qquad A_{\bar z}=-(\partial_{\bar z}h)h^{-1},\qquad A_y-i\phi_1=-(\partial_yh)h^{-1}.$$
They satisfy the complex equations identically, and
$$\mu=\tfrac i2\,h\,\Omega(H)\,h^{-1},\qquad \Omega(H)=\partial_y(H^{-1}\partial_yH)+4\partial_{\bar z}(H^{-1}\partial_zH)+[H^{-1}\varphi_0^\dagger H,\varphi_0]$$
(Part 2). For $H={\rm diag}(e^{-u},e^u)$ and $\varphi_0=z^kE$, with $E=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, this is $\Delta v=e^{2v}|z|^{2k}$ with $v=-u$ [9], [6].

In Dimakis' description [3, Def. 1.2], a solution corresponds to $\varphi_0=P(z)E$ and a boundary line spanned by $\mathfrak s=(Q,R)^T$. Its knot points are the zeros of $PR^2$, with multiplicities as weights [3, Thm. 2.4].

**Lemma 2.3 (Chern-type formula).** For invertible $K$ and $h$, put $\partial^K_jh=\partial_jh+[K^{-1}\partial_jK,h]$ and $M^{\dagger_K}=K^{-1}M^\dagger K$. Then
$$\Omega(Kh)-\Omega(K)=\partial_y(h^{-1}\partial^K_yh)+4\partial_{\bar z}(h^{-1}\partial^K_zh)+[h^{-1}\varphi_0^{\dagger_K}h-\varphi_0^{\dagger_K},\varphi_0].$$

*Proof.* $(Kh)^{-1}\partial(Kh)=h^{-1}(K^{-1}\partial K)h+h^{-1}\partial h=K^{-1}\partial K+h^{-1}\partial^Kh$. Also $(Kh)^{-1}\varphi_0^\dagger(Kh)=h^{-1}\varphi_0^{\dagger_K}h$. Substitute into $\Omega$. Part 13 confirms the formula exactly at a rational point. $\square$

## 3. Knot rigidity: proof of Theorem 1(1)–(2) and Corollary 2

Write $\tilde a=G\cdot x-x_W^{(k)}$, with $\mathcal E_3(\tilde a)<\infty$.

*Proof of (1), knots away from the origin.* Let $p\ne0$ be a knot point of weight $k_1\ge1$ with set $\Gamma$. Shrink $\Gamma$ to a nonempty open set with $\omega_y\in[c_1,c_2]\subset(0,1)$ on $\Gamma$.

Since $x_W^{(k)}$ is smooth near $p$, Lemma 2.2 gives $y|\phi_1(x_W^{(k)})|(p+r\omega)=h_K(y/|p+r\omega|)\to1$ as $r\to0$, uniformly on $\Gamma$. By (1.1) and Lemma 2.2, for each $\omega\in\Gamma$ the quantity $y|\phi_1(x)|(p+r\omega)$ tends to $h_{K_1}(\omega_y)\ge1+k_1c_1^2$.

For $n\ge1$ let $\Gamma_n$ be the set of $\omega\in\Gamma$ with
$$y\,\big||\phi_1(x)|-|\phi_1(x_W^{(k)})|\big|(p+r\omega)\ \ge\ \tfrac12k_1c_1^2\quad\text{for all }0<r<1/n .$$
By continuity in $r$, the condition can be tested on rational $r$, so $\Gamma_n$ is measurable. The sets $\Gamma_n$ increase to $\Gamma$ because the convergence is pointwise. So some $\Gamma_n$ has positive measure. By Lemma 2.2, $y|\tilde a|\ge\frac12k_1c_1^2$ on the corresponding truncated cone. Since $y=r\omega_y\le r$,
$$\mathcal E_3(\tilde a)\ \ge\ \frac{k_1^2c_1^4}{4}\int_0^{1/n}\!\!\int_{\Gamma_n}\frac{r^2\,dr\,d\omega}{r^4}=\infty,$$
a contradiction.

*Proof of (1), weight at the origin.* Take $p=0$. Now $y|\phi_1(x_W^{(k)})|(r\omega)=h_K(\omega_y)$ exactly. Since $h_{K'}-h_K$ is real-analytic and not identically zero, $\Gamma$ contains an open subset on which $|h_{K'}-h_K|\ge\eta>0$. The same measure argument applies.

*Proof of (2), parity.* Set $\tau=Gg^{-1}$ on $S$. Then $\tau\cdot(g\cdot x)-x_W^{(k)}=\tilde a$, and $g\cdot x=x_W^{(N)}+o(1/y)$ near the face, uniformly on $S$.

*Step 1: a good circle inside $S$.* Use $(\rho,s,\theta)$, in which $d^3X=\rho^2d\rho\,ds\,d\theta$ (Part 8). Let $\gamma_{\rho,s_0}=\{\rho,\ s=s_0\}$. On it $y=\rho s_0$ and $|\partial_\theta\tilde a|\le\rho|\nabla\tilde a|$. By the Sobolev inequality on the circle,
$$\sup_{\gamma_{\rho,s_0}}y^2|\tilde a|^2\le C\rho^4s_0^2\int_0^{2\pi}\Big(\frac{|\tilde a|^2}{y^2}+|\nabla\tilde a|^2\Big)d\theta .$$
Averaging over $\rho\in(R_1-\eta,R_1+\eta)$ and $s_0\in(a,2a)$ gives a circle in $S$ with $\sup y|\tilde a|\le C\epsilon(a)^{1/2}$. Here $\epsilon(a)$ is the energy in $S\cap\{a<s<2a\}$, so $\epsilon(a)\to0$ as $a\to0$. For $a$ small, also $y|g\cdot x-x_W^{(N)}|$ is small on this circle, by the uniform hypothesis on $S$.

*Step 2: the loop class.* Near the face both models have Higgs triples $y^{-1}(n_a+O(s^2))$ with orthonormal frames $n_a$, and these frames differ by $R(-(k-N)\theta)$ (Lemma 2.1, §2.2). Since $|R-1|\le\sum_a|Rn_a-n_a|$ for $R\in SO(3)$, the loop $\tau|_\gamma$ is uniformly close to, and hence homotopic to, $R(-(k-N)\theta)$.

*Step 3: conclusion.* The circle bounds the cap $\{\rho,\ s\ge s_0\}\subset S$, on which $\tau$ is continuous, so the loop is null-homotopic. The loop $R(n\theta)$ represents $n$ mod $2$ in $\pi_1(SO(3))$, since its lift $e^{\mathbf kn\theta/2}$ closes iff $n$ is even (Part 5). Hence $k-N$ is even. $\square$

*Proof of Corollary 2.* By [3, Def. 2.3], at a knot point $p$ of weight $k_1$ there is a gauge with $x=x_W^{(k_1)}(\cdot-p)+O(r^{-1+\epsilon}\psi^{-1+\epsilon})$. On any open set of directions avoiding the vertical direction and the face, the error is $o(1/r)$. Hence (1.1) holds there, by gauge invariance of $|\phi_1|$. By Theorem 1(1), $PR^2=\text{const}\cdot z^k$, so $P=az^N$ and $R=z^p$ after normalising $\mathfrak s$, with $N+2p=k=K$.
- If $p=0$, then $R=1$, and the normalisation $\deg Q<\deg R$ of [3, Def. 1.2] forces $Q=0$. So $x=x_W^{(k)}$ by [3, Thm. 1.3] with $N=K=k$.
- If $p\ge1$, coprimality of $Q$ and $R=z^p$ gives $Q(0)\ne0$, and $\deg Q<p$.

$N=k$ forces $p=0$. At $k=1$, $K-N\in\{0,2,\dots\}$ forces $N=1$. $\square$

## 4. The matching gauge: proof of Theorem 1(3)

The proof is uniform in $m\ge0$ and $p\ge1$. It works at a fixed face point $z=re^{i\theta}$ with $r>0$ and expands in $y\to0$. Write $O_\omega(y^n)$ for $y^n$ times a function that is real-analytic in $(y,x_2,x_3)$ near $\{y=0,\ r>0\}$.

**Lemma 4.1 (normal form of the models; all $j$).** For $j\ge0$, $K=j+1$, put $w_j=v_j+\log y+j\log r$. Then $w_j$ is real-analytic in $(y,r)$ near $y=0$, $r>0$, even in $y$, and
$$w_j=-\frac{j(j+2)}{6r^2}\,y^2+O_\omega(y^4).$$

*Proof.* By the binomial theorem,
$$(R+y)^K-(R-y)^K=2KyR^{K-1}\big(1+P_K(y^2/R^2)\big),\qquad P_K(\tau)=\sum_{i\ge3\ \rm odd}\tfrac1K\tbinom Ki\tau^{(i-1)/2}.$$
Here $P_K$ is a polynomial with $P_K(0)=0$ and $P_K'(0)=\binom K3/K=\frac{(K-1)(K-2)}6$. Hence $v_j=-\log y-(K-1)\log R-\log(1+P_K(y^2/R^2))$. Also $(K-1)\log R=j\log r+\frac j2\log(1+y^2/r^2)$. So
$$w_j=-\tfrac j2\log(1+y^2/r^2)-\log\big(1+P_K(y^2/(r^2+y^2))\big),$$
which is analytic and even in $y$. Its $y^2$ coefficient is $-\frac j{2r^2}-\frac{j(j-1)}{6r^2}=-\frac{j(j+2)}{6r^2}$. Part 17 checks this symbolically in $K$, and Part 17 also checks the binomial identity for $K\le13$. $\square$

**Lemma 4.2 (leading part; all $j$).** Let $N_j$ be the configuration with
$$A=j\,d\theta\,t_3,\qquad\phi_1=-y^{-1}t_3,\qquad\phi_z=iy^{-1}e^{ij\theta}(t_1+it_2).$$
Then $x_W^{(j)}=N_j+O_\omega(y)$ in every component.

*Proof.* Lemma 4.1 gives:
- $\phi_1=\partial_yv_j\,t_3=(-y^{-1}+\partial_yw_j)t_3$, with $\partial_yw_j=O_\omega(y)$;
- $\phi_z=ie^{v_j}z^j(t_1+it_2)=iy^{-1}e^{w_j}e^{ij\theta}(t_1+it_2)$, with $e^{w_j}-1=O_\omega(y^2)$;
- $A=-r\partial_rv_j\,d\theta\,t_3=(j-r\partial_rw_j)\,d\theta\,t_3$, with $r\partial_rw_j=O_\omega(y^2)$. $\square$

**Lemma 4.3 (the gauge; all $p$).** $q=e^{-\mathbf k\theta}+O_\omega(y^2)$. Hence $q^p=e^{-p\mathbf k\theta}+O_\omega(y^2)$ and $G^{(p)}_\infty=R(-2p\theta)\,(1+O_\omega(y^2))$.

*Proof.* $s^2=y^2/(r^2+y^2)$ and $\sqrt{1+s^2}\,r/\rho=\sqrt{1-s^4}=1+O_\omega(y^4)$. So $q=e^{-\mathbf k\theta}(1+O_\omega(y^4))+s^2\mathbf i=e^{-\mathbf k\theta}+O_\omega(y^2)$ (Part 17, symbolic in $r,\theta$). If $q^p=e^{-p\mathbf k\theta}+O_\omega(y^2)$, then $q^{p+1}=q^pq=e^{-(p+1)\mathbf k\theta}+O_\omega(y^2)$. This induction step is the product rule; Part 17 checks it for generic quaternions up to $p=8$. Finally ${\rm Ad}(e^{-p\mathbf k\theta})=R(-2p\theta)$. $\square$

*Proof of the cancellation, for all $m,p$.* Write $G=G^{(p)}_\infty=R(-2p\theta)(1+y^2M)$, with $M$ analytic, and $k=m+2p$.
- *Higgs fields.* By Lemma 4.2, $G\phi_a^{(m)}=R(-2p\theta)\phi_a^{N_m}+O_\omega(y)$, since $y^2\cdot y^{-1}=y$. By Lemma 2.1, $R(-2p\theta)$ fixes $\phi_1^{N_m}=-y^{-1}t_3$ and multiplies $\phi_z^{N_m}$ by $e^{2ip\theta}$. This gives $\phi_z^{N_k}$, because $e^{2ip\theta}e^{im\theta}=e^{ik\theta}$.
- *Connections.* $G\cdot A^{(m)}={\rm Ad}(G)A^{(m)}-(dG)G^{-1}$. Since $A^{(m)}=m\,d\theta\,t_3+O_\omega(y)$ is fixed by rotations about $t_3$, ${\rm Ad}(G)A^{(m)}=m\,d\theta\,t_3+O_\omega(y)$. Also $(dG)G^{-1}=-2p\,d\theta\,t_3+O_\omega(y)$, because $d(y^2M)=2yM\,dy+y^2dM$. Hence $G\cdot A^{(m)}=(m+2p)\,d\theta\,t_3+O_\omega(y)=A^{N_k}+O_\omega(y)$.

With Lemma 4.2 for $j=k$, this gives
$$a_\infty=G\cdot x_W^{(m)}-x_W^{(k)}=O_\omega(y)\qquad\text{near }\{y=0,\ r>0\},$$
locally uniformly in $z$. Part 17 checks the phase and connection identities with $m,p$ symbolic.

*Consequences.* So $y\,a_\infty=y^2B$ with $B$ real-analytic near the face. Since $a_\infty$ is homogeneous of degree $-1$ (both models are dilation invariant and $q$ is homogeneous of degree $0$), on the region $\{s\le\frac12\}$ we can write $y\,a_\infty=s^2b(s,\theta)$ with $b$ analytic and bounded. Hence $|a_\infty|\le Cs/\rho$. Weighted derivatives preserve this form, so $|Va_\infty|\le Cs/\rho$. Ordinary derivatives give only $|\nabla a_\infty|\le C\rho^{-2}$, because $\partial_y$ contains $\rho^{-1}s^{-1}\,s\partial_s$.

*Supplementary checks (not used in the proof).*
- Part 18 confirms the vanishing of the orders $s^0$ and $s^1$ of $y\,a_\infty$ by an exact series at $\theta=0$, for all $36$ pairs $(k,m)$ with $k\le12$.
- Part 16 shows that the order $s^2$ is nonzero for $(2,0)$, $(3,1)$, $(4,0)$ and $(4,2)$. Its full norm, $\lim_{s\to0}\rho|a_\infty|/s$, is $5.8878$, $6.9282$, $12.3353$ and $8.1650$ there (exact values such as $10\sqrt6/3$ appear in Part 16).
- Part 15 confirms the weighted-derivative bounds numerically for $(2,0)$.
- The rotational equivariance $q(R_\alpha X)=e^{-\mathbf k\alpha/2}q(X)e^{-\mathbf k\alpha/2}$ (Part 16) is not needed for the proof.

*Energy.* By homogeneity, $\mathcal E_3(a_\infty;\{\rho>1\})=\int_1^\infty\rho^{-2}d\rho\cdot\int_{S^2_+}(|\nabla a_\infty|^2+|a_\infty|^2/y^2)|_{\rho=1}d\Omega$. The angular integrand is bounded. For $(2,0)$ it tends to $208/3$ at the face, and quadrature gives $552.92\ldots$ (Part 9; numerical value only).

*Odd case.* Apply Theorem 1(2) to $x=x_W^{(m)}$ with $g=1$, on any shell $S$. Its proof uses only the energy on $S$. $\square$

*Remark 4.1.* Any null-homotopy of $R(-2p\theta)$ that agrees with ${\rm Ad}(q^p)$ to second order in $s$ at the face would do. The energy value depends on the choice; its finiteness does not.

## 5. Taubes' instantons near the knot and the face: proof of Theorem 3(a)–(b)

Here $x=g\cdot x^\diamond$, with:
- $x^\diamond$ the initial data of [1, §3];
- $g$ the $s=\infty$ end of the flow of [1, §§4–5];
- the action of [1, (4.1)].

We use three facts from [1]:
- **(T-a)** [1, Prop. 5.1]: $|g|<\kappa$ everywhere. For each $\varepsilon>0$ there is $\kappa_\varepsilon$ with $|g-1|<\varepsilon$ where $t<1/\kappa_\varepsilon$, uniformly in $z$. (Taubes' $t$ is our $y$.)
- **(T-b)** [1, Prop. 5.1]: $|\nabla_{A^\diamond}g|<\kappa/(\mu t)$, where $\mu$ is defined in [1, (5.1)]. Since $|B_{A^\diamond}|+|E_{A^\diamond}|+|\nabla a^\diamond|+|a^\diamond|^2\le C/t^2$ on $\{t<1\}$ (by [1, (1.6)] for the models and [1, Lemma 3.2]), we have $\mu\ge c_0>0$ there. Hence $|\nabla_{A^\diamond}g|\le C/y$ on $\{y<1\}$.
- **(T-c)** [1, Lemma 3.2, (3.8), (3.10)–(3.13)]: on $\{y<1/\kappa'\}$:
  - $x^\diamond=x_W^{(k)}$ where $|z|>4y$;
  - only $\phi$ differs from the model where $|z|<y$, with $\phi^\diamond-\phi^{(k)}=\varsigma(2\gamma\sigma_3+\gamma^2(\sigma_1+i\sigma_2))$ and $\varsigma\gamma=\mathfrak p=\sum_ja_jz^{k-j}$;
  - $|x^\diamond-x_W^{(k)}|\le\kappa'y^{m+p}$ and $|\nabla(x^\diamond-x_W^{(k)})|\le\kappa'y^{m+p-1}$ where $y\le|z|\le4y$.

### 5.1 A Simpson-type identity

Let $K$ and $H$ be the metrics of $x^\diamond$ and $x$ on the common holomorphic data, so that $h=K^{-1}H$ is represented by $g^\dagger g$ in a unitary frame of $x^\diamond$. Then $\mu_\diamond=\frac i2\Omega_K$ and $\mu_x=\frac i2\Omega_H=0$, read in the respective unitary frames.

**Lemma 5.1.** For any two metrics on the same holomorphic data,
$$\Delta\,{\rm tr}\,h={\rm tr}\big(h(\Omega_H-\Omega_K)\big)+S_y+S_z+S_\phi,$$
with $S_y={\rm tr}(\partial_yh\,h^{-1}\partial^K_yh)$, $S_z=4\,{\rm tr}(\partial_{\bar z}h\,h^{-1}\partial^K_zh)$ and $S_\phi={\rm tr}([\varphi_0,h]h^{-1}[\varphi_0,h]^{\dagger_K})$, each $\ge0$. The same holds with $(h,H,K)$ replaced by $(h^{-1},K,H)$.

*Proof.* Take the trace of Lemma 2.3 against $h$.

*Derivative terms.* For $j=y$ (and similarly for $z$, with weight $4$): ${\rm tr}(h\,\bar\partial_j(h^{-1}\partial^K_jh))=\bar\partial_j{\rm tr}(\partial_j^Kh)-{\rm tr}(\bar\partial_jh\,h^{-1}\partial^K_jh)$. Since ${\rm tr}$ kills commutators, $\sum_j\bar\partial_j{\rm tr}\,\partial^K_jh=\Delta\,{\rm tr}\,h$.

*Higgs term.* Write $\varphi=\varphi_0$ and $\varphi^\dagger=\varphi_0^{\dagger_K}$. The Higgs term contributes ${\rm tr}(2h\varphi\varphi^\dagger-h\varphi h^{-1}\varphi^\dagger h-h\varphi^\dagger\varphi)=-S_\phi$, using $[\varphi,h]^{\dagger_K}=[h,\varphi^\dagger]$ for $K$-self-adjoint $h$.

*Positivity.* For $K$-self-adjoint $h$, $(\partial_jh)^{\dagger_K}=\partial^K_{\bar j}h$. So each $S$ has the form ${\rm tr}(Bh^{-1}B^{\dagger_K})=|K^{1/2}Bh^{-1/2}K^{-1/2}|^2\ge0$. Part 10 checks the identity and the positivity exactly on random rational 2-jets. $\square$

Put $\psi={\rm tr}\,h+{\rm tr}\,h^{-1}-4\ge0$. By Lemma 5.1, $\Omega_H=0$ and (T-a),
$$\Delta\psi\ge-C_1|\mu_\diamond|,\qquad0\le\psi\le C_0,\qquad\psi\to0\text{ as }y\to0\text{ uniformly}.\tag{5.1}$$

**Lemma 5.2.** On $\{y<r_1\}$, $\mu_\diamond=0$ outside the cone $\{|z|\le4y\}$, and $|\mu_\diamond|\le C\rho^{m+p-1}$ on $\{\rho<r_1\}$.

*Proof.* Outside the cone, $x^\diamond=x_W^{(k)}$ by (T-c).

Where $|z|<y$: put $e=\phi^\diamond-\phi^{(k)}$. Then $|e|\le2|\mathfrak p|+|\mathfrak p|^2/|\varsigma|\le C(|z|^{m+p}+|z|^my^{k+1})$, using $|\varsigma|\ge c|z|^k/y^{k+1}$ [1, (3.10)–(3.11)] and $2(m+p)-k=m$ (Part 11). Also $|\phi^{(k)}|\le C/y$ and $y\ge\rho/\sqrt2$. Hence $|\mu_\diamond|\le C(|\phi^{(k)}||e|+|e|^2)\le C\rho^{m+p-1}$.

Where $y\le|z|\le4y$: $\mu_\diamond=\mu(x^\diamond)-\mu(x_W^{(k)})$ is linear and quadratic in $x^\diamond-x_W^{(k)}$ and its first derivatives, with coefficients $O(1/y)$. By (T-c) it is $O(y^{m+p-1})$. $\square$

### 5.2 The barrier: proof of Theorem 3(a)

*Near the origin.* Let $r=r_1$, $M=C_0$ and $F=C_1|\mu_\diamond|\mathbf 1_{B^+_r}$. Let $G(X,Y)=\frac1{4\pi}(|X-Y|^{-1}-|X-Y^*|^{-1})$ be the Dirichlet Green function of the half-space. It satisfies $0\le G\le\frac1{4\pi|X-Y|}$ and $G\le\frac{y_Xy_Y}{2\pi|X-Y|^3}$ (Part 11). Put $V_F=\int G(\cdot,Y)F(Y)\,dY$.

Let $b$ be harmonic on $B^+_r$, equal to $M$ on the curved boundary and to $0$ on the flat part. By odd reflection and the interior gradient estimate, $b\le6My/r$ on $B^+_{r/2}$.

For $\epsilon>0$, $w=\psi-b-V_F-\epsilon/|X|$ is subharmonic, by (5.1). It tends to $-\infty$ at $X=0$, because $\psi$ is bounded. It is $\le0$ on the curved boundary, and $\limsup w\le0$ at the face. By the maximum principle $w\le0$; letting $\epsilon\to0$, $\psi\le b+V_F$.

By Lemma 5.2, $F$ is supported in $\{|z|\le4y\}$ and is bounded.
- If $X$ lies outside $\{|z|\le8y\}$, its distance to the support is at least $c\max(\rho_X,|Y|)$. Hence $V_F(X)\le Cy_X\int|Y|F(Y)\max(\rho_X,|Y|)^{-3}dY\le Cy_X$.
- If $X$ lies inside that cone, then $y_X\ge\rho_X/9$. The part $|Y|\ge2\rho_X$ contributes at most $Cy_X\int|Y|^{m+p-2}dY\le Cy_X$. The part $|Y|<2\rho_X$ contributes at most $C\rho_X^{m+p+1}\le Cy_X$.

Hence $\psi\le Cy$ on $B^+_{r/2}$.

*Near the face, away from the origin.* For a face point $p$ with $|p|\ge r/2$, put $r_p=\min(|p|/5,1/(2\kappa'))$. On $B^+(p,r_p)$ we have $\mu_\diamond=0$ by (T-c). There the barrier alone gives $\psi\le6My/r_p$ on $B^+(p,r_p/2)$, uniformly in $p$. $\square$

### 5.3 From the metric to the fields: proof of Theorem 3(b)

Write $g=u\,e^{\sigma/2}$, with $u$ unitary and $\sigma$ self-adjoint. Since $\psi=4(\cosh\lambda-1)\ge2\lambda^2=|\sigma|^2$ for eigenvalues $\pm\lambda$ of $\sigma$ (Part 11),
$$|\sigma|\le Cy^{1/2}\quad\text{on }W=B^+_{r_2}\cup\{y<y_2\}.\tag{5.2}$$
By (T-a) and (T-b), $|\nabla_{A^\diamond}\sigma|\le C/y$ on $W\cap\{y<1\}$, since $\sigma=\log(g^\dagger g)$ is a smooth function of $g$ on the compact set $\{|g|,|g^{-1}|\le\kappa\}$.

*The equation.* By Lemma 2.3 with $h=e^\sigma$ and $\Omega_H=0$:
$$\Omega_K+\partial_y(e^{-\sigma}\partial^K_ye^{\sigma})+4\partial_{\bar z}(e^{-\sigma}\partial^K_ze^\sigma)+[e^{-\sigma}\varphi_0^{\dagger_K}e^\sigma-\varphi_0^{\dagger_K},\varphi_0]=0 .$$
Here $e^{-\sigma}\partial^Ke^\sigma=P({\rm ad}\,\sigma)\,\partial^K\sigma$ with $P(t)=(1-e^{-t})/t$. Expanding gives
$$P({\rm ad}\,\sigma)\,\Delta_K\sigma=-\Omega_K-\mathcal Q(\sigma)(\nabla_K\sigma,\nabla_K\sigma)-\mathcal R,$$
where:
- $\Delta_K$ is the Laplacian of the Chern connection of $K$;
- $\mathcal Q$ is bilinear, with coefficients smooth in $\sigma$;
- $|\mathcal R|\le C|\sigma||\varphi_0|_K^2$;
- $P({\rm ad}\,\sigma)$ is invertible with bounded inverse for $|\sigma|\le1$.

*Rescaling.* Fix $X_0\in W'=B^+_{r_2/4}\cup\{y<y_2/4,\ \rho<R\}$, put $y_0=y(X_0)$, and rescale $B(X_0,y_0/2)$ by $y_0$ to the unit ball $B_1$. In a unitary frame of $x^\diamond$, the rescaled connection, Higgs field and residual are bounded, together with first derivatives, independently of $X_0$, by (T-c) and the model bounds. The rescaled $\tilde\sigma$ satisfies $|\tilde\sigma|\le Cy_0^{1/2}$ by (5.2) and $|\nabla\tilde\sigma|\le C$ by (T-b). In this frame $\Delta_K=\Delta+$ (first-order terms with bounded coefficients). Therefore
$$\Delta\tilde\sigma=\tilde F,\qquad|\tilde F|\le C\quad\text{on }B_1,$$
with $C$ independent of $X_0$, since every term is bounded. The quadratic term is bounded because $|\nabla\tilde\sigma|\le C$ a priori; no absorption is needed.

*Linear estimate and interpolation.* The interior $W^{2,6}$ estimate for the flat Laplacian [11, Thm. 9.11] and Morrey's embedding [11, Thm. 7.26] give $\|\tilde\sigma\|_{C^{1,1/2}(B_{1/2})}\le C(\|\tilde\sigma\|_{L^\infty(B_1)}+\|\tilde F\|_{L^\infty(B_1)})\le C$.

For $f\in C^{1,\beta}$ and $0<t<\frac14$, the mean-value theorem on a segment of length $t$ gives
$$|\nabla f(X)|\le C\|f\|_\infty/t+[\nabla f]_\beta\,t^\beta .$$
Choose $t=\|f\|_\infty^{1/(1+\beta)}$. With $\beta=\frac12$, this gives $|\nabla\tilde\sigma|\le C\|\tilde\sigma\|_\infty^{1/3}\le Cy_0^{1/6}$ on $B_{1/4}$. Scaling back, $|\nabla_{A^\diamond}\sigma|(X_0)\le Cy_0^{-5/6}$.

*Conclusion.* By [1, (4.1)], $|u^{-1}\cdot x-x^\diamond|\le C(|\nabla_{A^\diamond}\sigma|+|\sigma||x^\diamond|)\le C(y^{-5/6}+y^{-1/2})$. By (T-c) and Lemma 5.2, $|x^\diamond-x_W^{(k)}|\le C$. Hence $|u^{-1}\cdot x-x_W^{(k)}|\le Cy^{-5/6}$ on $W'$. $\square$

*Remark 5.3.* Theorem 3(b) is a genuine power rate. At the knot, $y^{-5/6}=\rho^{-1+\varepsilon}s^{-1+\varepsilon}$ with $\varepsilon=\frac16$, which is the a priori hypothesis of [4, Thm. 9.6]. Near the face away from the knot it is the hypothesis $|a|\le Cy^{-1+\varepsilon}$ of the Nahm-pole regularity theorem [4, §4, p. 9], [5].

## 6. Weighted classes, Theorem 3(c), and Proposition 4

**Definition 6.1.** Fix $s_0\in(0,\frac12)$ and put $m_\alpha(\rho)=\min(1,\rho)^\alpha$. A field $a$ on an open set $U\subset\mathbb R^3_+$ lies in $\mathcal W(\alpha,\delta)$ if, for $V\in\{\rho\partial_\rho,s\partial_s,\partial_\theta\}$:
- on $U\cap\{s<s_0\}$: $|a|+\sum_V|Va|\le C\rho^{-1}m_\alpha(\rho)\,s^\delta$;
- on $U\cap\{s\ge s_0\}$: $|a|+\rho|\nabla a|\le C\rho^{-1}m_\alpha(\rho)$.

**Lemma 6.2.** If $a\in\mathcal W(\alpha,\delta)$ on $U$, then $|\nabla a|\le C\rho^{-2}m_\alpha s^{\delta-1}$ on $U\cap\{s<s_0\}$. If moreover $\alpha,\delta>\frac12$, then $\mathcal E_3(a;U)<\infty$ and $\sup_Uy|a|<\infty$.

*Proof.* In the coordinates $(\rho,s,\theta)$:
$$\partial_y=\rho^{-1}\big(s\,\rho\partial_\rho+\tfrac{1-s^2}{s}\,s\partial_s\big),\qquad \partial_r=\rho^{-1}\sqrt{1-s^2}\,\big(\rho\partial_\rho-s\partial_s\big),\qquad r^{-1}\partial_\theta\ \text{ with }\ r\ge\rho/2\ \text{ for }s<s_0 .$$
These give the gradient bound. Then $|\nabla a|^2+|a|^2/y^2\le C\rho^{-4}m_\alpha^2s^{2\delta-2}$ near the face and $\le C\rho^{-4}m_\alpha^2$ elsewhere. With $d^3X=\rho^2d\rho\,ds\,d\theta$, the integral is at most $C(\frac1{2\alpha-1}+1)(\frac1{2\delta-1}+1)$ (Part 8). Finally $y|a|\le C\rho s\,\rho^{-1}s^\delta\le C$. $\square$

**Lemma 6.3 (gluing).** Let $W$ be a region with $\rho\sim1$ and $s<s_0$, and let $g,g'$ be gauges on $W$ with $g\cdot x-x_W^{(k)}$ and $g'\cdot x-x_W^{(k)}$ in $\mathcal W(\cdot,\delta)$, $\delta>0$. Then $g'g^{-1}=\exp\xi$ with
$$|\xi|+\sum_V|V\xi|\le Cs^{1+\delta},\qquad |\nabla\xi|+\sum_V|V\nabla\xi|\le Cs^\delta .$$
Hence, for a cut-off $\chi(\rho)$, $\exp(\chi\xi)g\cdot x-x_W^{(k)}\in\mathcal W(\cdot,\delta)$ on $W$.

*Proof.* The Higgs triple of $x_W^{(k)}$ is $y^{-1}(n_a+O(s^2))$ with an orthonormal frame $n_a$. From $\tau\phi_a=\phi'_a$ we get $|\tau-1|\le Cys^\delta$. From $d\tau\,\tau^{-1}={\rm Ad}(\tau)A-A'$ we get $|d\tau|\le Cs^\delta$. Applying $V$ to both identities uses only weighted derivatives of the two differences and of the model, which is smooth in $(\rho,s,\theta)$ after multiplication by $y$.

For the interpolated gauge, $|\exp(\chi\xi)\phi-\phi|\le|\xi||\phi|\le Cs^\delta/\rho$ and $|d(\chi\xi)|\le Cs^\delta$. The same holds after applying $V$. $\square$

*Proof of Theorem 3(c).* By Remark 5.3, [4, Thm. 9.6] applies near the knot. It gives, in a suitable gauge, a polyhomogeneous expansion $a\sim a_0\rho^0+\dots$ on the blown-up space, whose coefficients are polyhomogeneous at the face. Polyhomogeneity includes stability of the bounds under the weighted (b-) vector fields $\rho\partial_\rho,s\partial_s,\partial_\theta$. It does not include stability under ordinary derivatives, which we do not claim.

The face exponents lie in the index set generated by the Nahm-pole indicial roots $\{-2,-1,1,2\}$ [4, §4, p. 9]. The a priori bound of Theorem 3(b) excludes exponents $\le-\frac56$, so the face expansion starts at order $s^1$. Possible logarithms at the front face are absorbed by the loss $\varepsilon$. Hence $a\in\mathcal W(1-\varepsilon,1)$ on $B^+_{r_3}$.

Away from the knot, Remark 5.3 and the local Nahm-pole regularity theorem [4, §4], [5] give $a\in\mathcal W(\cdot,1)$ in local gauges on $\{r_3/2\le\rho\le R,\ s<s_0\}$, uniformly by compactness. Lemma 6.3 patches the local gauges and $g_0$. On the compact rest of $\{\rho\le R\}$ the field is smooth. The gauge extends over it because $\pi_2(SO(3))=0$: the boundary of each remaining region is a $2$-sphere on which the gauge is prescribed. Lemma 6.2 gives the energy bound. $\square$

*Proof of Proposition 4.*
- *On $\{\rho>R_1\}$.* Put $y_\infty=G^{(p)}_\infty g_\infty\cdot x=x_W^{(k)}+a_\infty+G^{(p)}_\infty e_\infty$. By Theorem 1(3), $a_\infty\in\mathcal W(0,1)$. Since $|VG^{(p)}_\infty|\le C$ and $|\nabla G^{(p)}_\infty|\le C/\rho$, also $G^{(p)}_\infty e_\infty\in\mathcal W(0,\delta)$.
- *On $\{\rho<2R_1\}$.* Take $G_{2R_1}$ from Theorem 3(c).
- *Gluing.* On the overlap, rescaled to $\rho\sim1$, Lemma 6.3 glues the two gauges on the face layer. On the compact rest of the overlap (a closed ball), the gauge extends because $\pi_2(SO(3))=0$.
- *Conclusion.* The result lies in $\mathcal W(1-\varepsilon,\min(\delta,1))$ on $\mathbb R^3_+$, and Lemma 6.2 gives finite energy and $\sup y|\tilde a|<\infty$.
- *Not gauge equivalent.* By [1, (1.10)], $y|\phi_1(x)|\to m+1$ along the axis as $y\to\infty$, whereas $y|\phi_1(x_W^{(k)})|=k+1$ there (Lemma 2.2). $\square$

**Remark 6.4 (consistency of (A∞)).**
1. (A∞) holds trivially for $x=x_W^{(m)}$.
2. The class $\mathcal W(0,1)$ contains $a_\infty$ (Theorem 1(3)), so the conclusion of Proposition 4 is attained by explicit fields.
3. Near a face point at large $r$, Theorem 3(c) and (A∞) constrain the linear face coefficient $c(z)$ of $|\phi_1(x)|$. They require $c(z)-\frac{k(k+2)}{3r^2}=O(1)$ on bounded sets and $c(z)-\frac{m(m+2)}{3r^2}=O(r^{-2})$ for large $r$, since $\mathcal W(\cdot,\delta)$ with $\delta\le1$ allows linear terms. These requirements are compatible.
4. In the v2 formulation, ordinary derivatives carried the factor $s^\delta$, which forced $c(z)=\frac{k(k+2)}{3r^2}$ and $c(z)=\frac{m(m+2)}{3r^2}$ simultaneously. That was inconsistent, as the referee showed. The present formulation avoids this.
5. The numerics of §7 show $c(z)\ne\frac{k(k+2)}{3r^2}$ at $\rho\sim1$ (the face ratio $1.74$), as expected.

## 7. The case $(m,p)=(0,1)$: U(1) reduction and numerics

### 7.1 Reduction (proved)

Take Dimakis' data $\varphi_0=E$ with boundary section $\mathfrak s=(c,z)$, $c\ne0$. In the knot frame $g=\begin{pmatrix}0&c\\-1/c&z\end{pmatrix}$ one has
$$\varphi_0'=g^{-1}Eg=\begin{pmatrix}-z/c&z^2\\-1/c^2&z/c\end{pmatrix},\qquad g(0,1)^T=(c,z)^T$$
(Part 4). For all $\alpha$, $e^{-i\alpha}g_\alpha\varphi_0'(e^{i\alpha}z)g_\alpha^{-1}=\varphi_0'$ with $g_\alpha={\rm diag}(e^{-i\alpha/2},e^{i\alpha/2})$, and the EBE are invariant under $\phi_z\mapsto e^{i\mu}\phi_z$ [1, (1.3)].

In the original frame, uniqueness [3, Thm. 6.1] gives $H(y,e^{i\alpha}z)=g_\alpha'^\dagger H(y,z)g'_\alpha$ with $g'_\alpha={\rm diag}(e^{i\alpha/2},e^{-i\alpha/2})$. So $H_{12}(y,re^{i\theta})=e^{-i\theta}H_{12}(y,r)$. Together with the reflection $z\mapsto\bar z$ for real $c$, this gives the ansatz
$$H=\begin{pmatrix}e^{-u}+|z|^2f^2e^u&\bar z\,f\,e^u\\ z\,f\,e^u&e^u\end{pmatrix},\qquad u=u(y,r),\ f=f(y,r)\ \text{real}.$$
This is the matrix used in verify.py and numerics_u1.py. The EBE $\Omega(H)=0$ become (Part 3)
$$\Delta_3u+e^{-2u}-e^{2u}(r^4f^4+r^2|\nabla f|^2)=0,\qquad \Delta_5f+2\nabla u\cdot\nabla f-2r^2f^3-2fe^{-2u}=0,$$
with $\Delta_3=\partial_y^2+\partial_r^2+r^{-1}\partial_r$ and $\Delta_5=\partial_y^2+\partial_r^2+3r^{-1}\partial_r$.

Part 12 checks the printed matrix directly. With $u=\log\frac{1+r^2y^2}{r^2y}$ and $f=-\frac1{1+r^2y^2}$ (the Nahm pole $R_f$ carrying the section $(1,z)$), $\Omega(H)=0$ exactly at two rational points. Exchanging the off-diagonal entries gives $\Omega\ne0$, which reproduces the referee's computation. Also $R_a$, given by $(u,f)=(\log y,0)$, is $x_W^{(0)}$. Near the origin, $R_0=g^{-\dagger}H_2g^{-1}$, with $H_2$ the weight-2 model, has residual $O(\rho^4)$.

### 7.2 Numerics (qualitative evidence only)

*Setup.*
- Normalisation: $c=1$.
- Reference metric: we interpolate $R_0$ near the origin and $N_\chi^\dagger R_aN_\chi$ at infinity, where $N_\chi=1-\chi(r/\rho)z^{-1}E$.
- Unknowns: corrections $(U,\Phi)$, with $u=u_{\rm ref}+U$ and $f=f_{\rm ref}+\Phi/(re^{u_{\rm ref}})$.
- Discretisation: second-order finite differences in $\xi=\log\rho$ and $\eta$, with $\varphi=\eta-0.3\sin2\eta$ (a mesh graded towards the axis).
- Boundary conditions: Dirichlet at the face and at both radial ends; parity conditions at the axis.
- Solver: Newton's method, final residual $\le1.1\cdot10^{-10}$.

The runs are in `numerics_u1.py`, with output in `numerics_output.txt`:

| run | $\Delta\xi$ | $N_\varphi$ | $\xi$-range | origin slope ($J_1$, $J_2$) | slope at infinity |
|---|---|---|---|---|---|
| 1 | 0.05 | 96 | $[-6,6]$ | 1.380, 1.392 | $-2.982$ |
| 2 | 0.025 | 96 | $[-6,6]$ | 1.380, 1.392 | $-2.984$ |
| 3 | 0.0125 | 96 | $[-6,6]$ | 1.380, 1.392 | $-2.984$ |
| 4 | 0.025 | 96 | $[-6,8]$ | 1.380, 1.392 | $-2.985$ |
| 5 | 0.025 | 192 | $[-6,6]$ | 1.384, 1.384 | $-2.982$ |

Here $J_1=y|\phi_1|$ and $J_2=y^2(|\phi_2|^2+|\phi_3|^2)$ (gauge invariant). The origin slopes are least-squares slopes of $\log\max|J_i-J_i^{(2)}|$ over $\xi\in[-4.5,-1.5]$, and the slope at infinity is that of $\log\max|J_1-1|$ over $\xi\in[3,5]$.

*Convergence and endpoint effects.*
- **Radial refinement.** Between runs 2 and 3, $\max|J_1-J_1^{(2)}|$ changes by at most $0.04\%$ at $\xi\in[-5,-1]$. Between runs 1 and 2 it changes by at most $0.2\%$, which is consistent with second order.
- **Outer endpoint.** Moving it from $6$ to $8$ changes $\max|J_1-1|$ at $\xi=5$ by $0.6\%$ and the fitted slopes by at most $0.001$.
- **Angular refinement.** It changes the slopes by at most $0.008$.
- **Interpretation.** Taubes' guaranteed exponent is $\ge1$ (Theorem 3), and the observed $\approx1.38$ lies in $(1,2)$. This is consistent with a generic Type II root ([4, Prop. 4.3]; [3, Thm. 4.2]).
- **Face.** At $\xi=0$, $|J_1-J_1^{(2)}|/s^2\to1.74$ at the face, a nonzero linear face coefficient as in Remark 6.4(5).

*What this does not show.*
- Two invariants do not control the connection or its derivatives in the gauge of (A∞).
- The lower-bound proxy $\int(J_1-J_1^{(2)})^2y^{-4}\approx47.2$ on $\rho\le e^6$ is a lower bound for $\mathcal E_3$ (Lemma 2.2), not a proof of finiteness.
- Uniqueness of the discrete solution and its identification with the instanton are assumed (§7.1).

## 8. Consequences

1. **Periodic case.** By [14, Thm. 3], finite-energy solutions on $S^1\times\mathbb R^3_+$ reduce to Question 6.2. Under (A∞), Proposition 4 and [14, Remark 6.3] show that the periodic analogue of [14, Thm. 1] fails for every $k\ge2$; without (A∞) this remains open. For $k=1$, Corollary 2 excludes all competitors inside Dimakis' classes.
2. **The correct class.** Finite energy sees the knot data (Theorem 1(1)) and the parity of the charge at infinity (Theorem 1(2)), but not the charge itself (Theorem 1(3)). A natural corrected Question 6.2 adds the blow-down condition $\lambda\tilde x(\lambda\,\cdot)\to x_W^{(k)}$ as $\lambda\to\infty$. Within $\mathcal{EBE}$ this class is exactly $\{x_W^{(k)}\}$ (Corollary 2).
3. **Monopole bubbling (interpretation only).** In the Gaiotto–Witten picture [9] the instanton is a weight-$k$ boundary Hecke modification of which $2p$ units are screened, as in monopole bubbling [8, §10.2]. Theorem 1(3) shows that the screening costs no energy at infinity once the $2p$-fold winding is undone by ${\rm Ad}(q^p)$. Theorem 3 shows that it costs none at the knot either.

## 9. Status of claims

- **Proved:**
  - Theorem 1, including the face vanishing in Theorem 1(3) for all $m\ge0$, $p\ge1$ (§4; Parts 17–18 are checks);
  - Corollary 2, given [3, Thms. 1.3, 2.4, Def. 2.3];
  - Lemmas 2.1, 2.2, 2.3, 5.1, 5.2, 6.2 and 6.3;
  - Theorem 3(a);
  - Theorem 3(b), given [1, Prop. 5.1, Lemma 3.2] and [11];
  - Proposition 4, as an implication;
  - §7.1, given [3, Thm. 6.1].
- **Proved modulo cited regularity theorems:** Theorem 3(c), which uses [4, Thm. 9.6], [4, §4] and [5].
- **Assumed:** (A∞), in Proposition 4 only.
- **Numerical:**
  - §7.2;
  - the value $552.92$;
  - Part 15.
- **Not claimed:** an answer to Question 6.2; (A∞); compactness, Floer theory or nontrivial knots.

## 10. Verification

`verify.py` (python3, sympy 1.14, mpmath; about 8 minutes, of which about 3 minutes are the supplementary Part 18) prints OK/FALLA for each check and ends with `FALLOS = 0`; its output is `verify_output.txt`. Checks are exact unless marked [NUM].
- **Parts 1–9:** models, the holomorphic dictionary, the reduced system, knot-frame data, rotations and $q$, face behaviour of $a_\infty$ [NUM], Lemma 2.2, bookkeeping, and the energy $552.92$ [NUM].
- **Part 10:** Lemma 5.1 on random rational 2-jets, as a consistency check of the proof given in the text.
- **Part 11:** Green-function bounds, exponents, and $\psi\ge|\sigma|^2$.
- **Part 12:** the printed U(1) ansatz with the exact solution $R_f$, and the swapped control.
- **Part 13:** Lemma 2.3 at a rational point.
- **Part 14:** the face expansion $|\phi_1|=\frac1y+\frac{j(j+2)}{3r^2}y+O(y^3)$ for $j\le4$ (the general case is Lemma 4.1 and Part 17).
- **Part 15** [NUM]: weighted derivatives of $a_\infty$.
- **Part 16:** exact face expansions of $y\,a_\infty$ for four pairs, with nonzero order $s^2$, and the equivariance of $q$.
- **Part 17:** the general proof of Theorem 1(3), symbolically in the weights: the binomial normal form with symbolic $K$; Lemma 4.1 with symbolic $j$; phase and connection identities with symbolic $m,p$; $q-e^{-\mathbf k\theta}=O(y^2)$ with symbolic $r,\theta$; the induction step for generic quaternions.
- **Part 18** (supplement): exact vanishing of the orders $s^0$ and $s^1$ of $y\,a_\infty$ for all $36$ pairs with $k\le12$.

`verify.mpl` mirrors the exact Parts 1 (scalar model equation), 4, 5, 7, 8, 11, 14 and 17 under the Maple rules (`grep -c -i -E "w|fi" verify.mpl` returns $0$). It has not been executed, because Maple is not available. Random-jet and rational-point tests are consistency checks; the proofs are in the text.

## References

1. C. H. Taubes, *The existence of instanton solutions to the $\mathbb R$-invariant Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$*, arXiv:2102.04290 (Thm. 1; (1.3)–(1.11); Lemmas 3.1–3.2, (3.8)–(3.13); (4.1); (5.1); Prop. 5.1).
2. C. H. Taubes, *The $\mathbb R$ invariant solutions to the Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$ with generalized Nahm pole asymptotics*, arXiv:1903.03539 (Thm. 2; Props. 3.1, 8.1–8.2).
3. P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: nilpotent Higgs field*, arXiv:2209.11101 (Defs. 1.1, 1.2, 2.3; Thms. 1.3, 2.4, 4.2, 5.4, 6.1; (5.27); Rems. 5.5, 6.2; §5.3).
4. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Math. Phys. (2020); arXiv:1712.00835 (§4 incl. p. 9; Prop. 4.3; (4.28)–(4.35); Thm. 9.6).
5. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014); arXiv:1311.3167.
6. S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019); arXiv:1710.10645.
7. S. He, R. Mazzeo, *The extended Bogomolny equations with generalized Nahm pole boundary conditions, II*, Duke Math. J. (2020), doi:10.1215/00127094-2020-0009; arXiv:1806.06314.
8. A. Kapustin, E. Witten, *Electric-magnetic duality and the geometric Langlands program*, Commun. Number Theory Phys. 1 (2007); arXiv:hep-th/0604151 (§10.2).
9. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012); arXiv:1106.4789.
10. C. Simpson, *Constructing variations of Hodge structure using Yang–Mills theory and applications to uniformization*, J. Amer. Math. Soc. 1 (1988), 867–918 (Lemma 3.1).
11. D. Gilbarg, N. Trudinger, *Elliptic partial differential equations of second order*, Springer (Thms. 7.26, 9.11).
12. rStation math_37 v1, *A one-sided comparison theorem for Witten's knot solution of the Kapustin–Witten equations, with remarks on the long unknot*, https://rstation.ai/problems/math/papers/37/v1.
13. rStation math_38 v1, *Witten's unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window*, https://rstation.ai/problems/math/papers/38/v1.
14. rStation math_40 v1, *Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class*, https://rstation.ai/problems/math/papers/40/v1 (§1.1, §2, Thm. 1, Thm. 3, Prop. 5.1, Question 6.2, Remarks 6.2′ and 6.3).

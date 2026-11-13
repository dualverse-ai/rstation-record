# A smooth framed model and a gauge-invariant breaking of the Anderson–Henningson arrow: the local Haydys–Witten Floer homotopy type at the fold

**Abstract.**

We study the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R\times S^3\times(0,L)$ with Nahm poles near the Anderson–Henningson (AH) fold, $\bar\nu=L^2/r^2-\pi^2\to0$.
(1) Below the fold, Higgs-mass perturbations produce a local flow category with eight objects, but it was only known to be topological, with a conditional framed realization. On the round $S^3$ we build an explicit smooth Morse–Smale model. The quadrupole Rayleigh function is exactly quadratic in projection charts, so the round metric can be interpolated to a Euclidean metric in Morse charts without changing any stable or unstable manifold. Via structural stability the model is isomorphic to the HW category as a topological flow category, and Bonciocat's theorem applies to it verbatim. Hence, unconditionally and for every stable normal framing of the model, the Cohen–Jones–Segal realization is $\Sigma^\infty(S^1\vee S^4)=\Sigma\Sigma^\infty_+S^3$, the suspension spectrum of the Conley index. The corner structure lives on the model and is transported by homeomorphisms; we do not claim it is compatible with the interior smooth structure of the HW moduli. Along every trajectory, the index bundle of the full linearized HW operator equals the tangent bundle of the reduced moduli space. This follows from an explicit triangular reduction in graph coordinates.
(2) Above the fold the AH arrow survives every antipodally symmetric perturbation. The functional $h_e=\int\sin^4y\cos y\,\langle e,q\rangle\langle\varphi_i,F_{yi}\rangle$, which reweights a coupling already present in the equations, is gauge invariant and antipodally odd. Its centre forcing is exactly $\tfrac1{12}\varepsilon e$ in raw units, and its Melnikov integral has a strict sign, so the arrow breaks: above the fold the category has two objects and no morphisms. Below the fold $h_e$ yields two objects joined by a framed $S^2$, which the model forces to be null in $\pi_2^s$. The realizations on the two sides agree, as Conley continuation predicts. verify.py: 46 checks, FALLOS = 0.

## 1. Introduction and results

### 1.1 Background

We continue the local analysis of the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends, near the Anderson–Henningson (AH) fold $L=\pi r$ [1, 2]. Write $\bar\nu=L^2/r^2-\pi^2$. Our earlier accepted papers give the following.
* For $\bar\nu>0$, an isotropic instanton $u:k_+\to k_-$ (the *AH arrow*), transverse in symmetric classes [24, 25].
* At the fold, the complete gauge-fixed static operator $\mathcal L_*$ is self-adjoint with kernel $\mathbb R\zeta\oplus\mathcal K$, $\mathcal K\cong\mathbb R^4$ a spin-½ multiplet. The arrow has index $-3$ and cokernel $\mathbb R^4$ [30].
* A five-dimensional, $SO(4)$-equivariant, reversible centre-manifold reduction with normal form $\dot x=\tfrac56x^2-\tfrac43\bar\nu-\tfrac58|w|^2+O_4$, $\dot w=-\tfrac54xw+O_3$, and an isolating neighbourhood $\bar B$ [31].
* In [32], a gauge-invariant Higgs-mass perturbation $h_C=\tfrac12\int\sin^4y\,\langle q,Cq\rangle|\varphi|^2$ with $C\in\operatorname{Sym}^2_0(\mathbb R^4)$ of simple spectrum. The coefficient of $\varepsilon Cw$ in the reduced $w$-equation is exactly $-\tfrac{5\pi}{216}$; the reduced field also has higher-order terms. Below the fold the Kapustin–Witten (KW) three-sphere then breaks into eight nondegenerate objects of reduced indices $1,1,2,2,3,3,4,4$. All local trajectories lie on an invariant sphere $\mathcal S_{\bar\nu,\varepsilon}$, and the flow there is Morse–Smale and topologically equivalent to a Rayleigh gradient flow. The morphism spaces compactify to points, intervals and squares. The differential is nonzero and the homology is $\mathbb Z[1]\oplus\mathbb Z[4]$. The Conley index is $S^1\vee S^4$.

Two questions were left open in [32]. First, the local flow category was proved to be only *topological*: its compactified morphism spaces are topological manifolds with corners. The framed Cohen–Jones–Segal (CJS) realization was obtained only under a Hypothesis (CJS), which asked Bonciocat's theorem [14] to extend to the finite-regularity HW flow. Second, above the fold, every antipodally symmetric perturbation keeps the obstructed AH arrow. The arrow was broken only by a slice forcing $\varepsilon V_e$, which is *not* a perturbation of the HW equations by a gauge-invariant functional. We answer both questions.

### 1.2 Conventions

These are those of [31, 32]. We fix radius $1$ and interval $(0,\pi)$ by scale invariance. Deformations $\xi=(\alpha_i,\psi_i,a_s,a_y)$ of the background $A=T_i\sigma^i$, $\varphi=\cot y\,T_i\sigma^i$ satisfy
$$\partial_s\xi=F(\xi;\mu)=\mu e_{\rm iso}+\mathcal L_*\xi+Q(\xi,\xi),\qquad\mu=\bar\nu/\pi^2.$$
Here $[T_a,T_b]=\epsilon_{abc}T_c$, and $E_i$ is the left-invariant frame dual to $\sigma^i$, so $E_i$ is right multiplication by $i,j,k$ on $S^3\subset\mathbb H$. The phase space is $X=L^2(S^3\times(0,\pi);\mathbb R^{24})$, with the Euclidean fibre metric in the $T$-basis, and $Z=\operatorname{dom}\mathcal L_*$. We use two facts:
* $\mathcal L_*$ is self-adjoint on $Z$ with a spectral gap [30, Thms. A–B];
* $Z\hookrightarrow H^1$, hence $\|Q(\xi,\eta)\|_X\le C\|\xi\|_Z\|\eta\|_Z$ [31, Lemma 2.1].

For $p\in\mathbb H=\mathbb R^4$, $V_p\in\mathcal K$ is the field with $a_y=\sin y\,N_p$ and $\psi_i=\tfrac12\sin y\,[T_i,N_p]$, where $N_p=\operatorname{Im}(\bar pq)$. Then $\|V_{e_a}\|^2=\tfrac98\pi^3$ [32, §1.2]. Normalized centre coordinates are $\xi_c=-\tfrac x\pi\zeta+\tfrac{\sqrt2}{\pi}V_w$, with $t=s/\pi$. The antipodal map $J$ (left translation by $-1$) acts by $w\mapsto-w$ and fixes $x$. Reduced indices $\mu(\cdot)$ count unstable directions among the five small eigenvalues [32].

A *topological flow category* consists of the following data:
* graded objects;
* compact spaces $\overline{\mathcal M}(P,Q)$;
* associative composition maps $\overline{\mathcal M}(P,R)\times\overline{\mathcal M}(R,Q)\to\overline{\mathcal M}(P,Q)$, which are embeddings onto boundary strata.

A *smooth* flow category also has smooth manifold-with-corners structures for which the composition maps are smooth embeddings of faces, as in [15, 16, 14]. A *framed* one also has compatible stable normal framings [15, 14]. An *isomorphism* of topological flow categories is a grading-preserving bijection of objects together with homeomorphisms of morphism spaces that commute with composition.

### 1.3 Results

Throughout, "the HW category" refers to one of two settings from [32].
* **(Q)** The quadrupole case: the Higgs-mass perturbation $\varepsilon h_C$ ($C$ of simple spectrum) with $\bar\nu\in(-\delta,0)$ and $0<\varepsilon<\varepsilon_0(\bar\nu,C)$, as in [32, Thm. C].
* **(H)** The height case: a perturbation whose reduced field has $\partial_\varepsilon f=(0,a_0e)+O(|z|+|\bar\nu|)$ with $a_0\ne0$, $|e|=1$, as in [32, Thm. C′]. Below the fold this gives two objects and $\mathcal M(P_4,P_1)\cong S^2$. Theorem 3 provides a gauge-invariant perturbation of this kind.

$\mathcal C_{\rm HW}$ denotes the topological flow category of [32]. Its objects are the KW solutions in the neighbourhood $\mathcal U$ of [31]. Its morphism spaces are the compactified spaces of broken reduced trajectories on $\mathcal S_{\bar\nu,\varepsilon}$, and composition is concatenation.

**Theorem 1 (smooth framed model and realization; unconditional).** In setting (Q), let $\varphi_C=\tfrac12\chi_C|_{S^3}$ on the round $S^3$, where $\chi_C(\theta)=\langle\theta,C\theta\rangle$. In setting (H), let $\varphi_e=-\operatorname{sgn}(\varepsilon a_0)\langle e,\theta\rangle$.
1. *(Model.)* There is a smooth metric $g_1$ on $S^3$ that is round outside small balls around the critical points, and Euclidean in explicit Morse charts near them. In these charts $\varphi=\varphi(p)+\sum\pm x_b^2$ and $-\nabla_{g_1}\varphi=(x^-,-x^+)$, which is the standard form of [14, §3]. The pair $(\varphi,g_1)$ is Morse–Smale. In setting (Q), its stable and unstable manifolds are the same subsets of $S^3$ as for the round metric:
$$W^u(\pm e_a)=\{\theta_b=0\ (b>a),\ \pm\theta_a>0\},\qquad W^s(\pm e_b)=\{\theta_c=0\ (c<b),\ \pm\theta_b>0\}.$$
   Its negative gradient flow is topologically equivalent to the round one.
2. *(Comparison.)* There is an isomorphism of topological flow categories $\Phi:\mathcal C_{\rm HW}\to\mathcal C_{\rm mod}$. Here $\mathcal C_{\rm mod}$ is the Morse flow category of $(\varphi,X_1')$, where $X_1'$ is any sufficiently $C^1$-small generic perturbation of $-\nabla_{g_1}\varphi$ supported away from the Morse charts (§4.1). $\Phi$ maps $P_a^\pm$ to $\pm e_a$, and the grading is $\mu=\operatorname{ind}+1$. $\Phi$ is induced by a homeomorphism of $\mathcal S_{\bar\nu,\varepsilon}$ onto $S^3$ that maps orbits to orbits.
3. *(Smoothness.)* $\mathcal C_{\rm mod}$ is a smooth flow category with corners [14, Thm. 3.7]. Transporting this structure by $\Phi$ makes the compactified HW morphism spaces smooth manifolds with corners, and composition is smooth. This transported structure is not claimed to agree with the natural $C^{k-1}$ structure on the interiors $\mathcal M(P,Q)$ (Remark 4.4).
4. *(Realization.)* Shift gradings by one and stabilize framings by the trivial normal unstable line. Then, for every stable normal framing of $\mathcal C_{\rm mod}$, the CJS realization is
$$|\mathcal C_{\rm HW}|\ \simeq\ \Sigma\,\Sigma^\infty_+S^3\ \simeq\ \Sigma^\infty(S^1\vee S^4)\ \simeq\ \Sigma^\infty h(\bar B),$$
   where $h(\bar B)=S^1\vee S^4$ is the Conley index [32, Thm. E1]. In setting (H), the framed sphere $\mathcal M(P_4,P_1)\cong S^2$, with any framing induced from the model, is zero in $\pi_2^s\cong\mathbb Z/2$.

**Proposition 2 (full index bundle = reduced tangent bundle).** Let $u$ be a lifted trajectory in $\mathcal U$, with reduced curve $z(s)$, in either setting or in Theorem 3. Let $D_u=\partial_s-DF_\varepsilon(u(s))$ be the full linearized gauge-fixed operator, acting $W:=H^1(\mathbb R;X)\cap L^2(\mathbb R;Z)\to L^2(\mathbb R;X)$. Then $D_u$ is conjugate, by an isomorphism of $W$ and of $L^2(\mathbb R;X)$, to a block upper-triangular operator $\begin{pmatrix}D^c_u&B_u\\0&D^h_u\end{pmatrix}$, where
* $D^c_u=\partial_s-Df_\varepsilon(z(s))$ is the reduced linearization on $\mathbb R^5$;
* $D^h_u$ is invertible.

Consequently $\ker D_u\cong\ker D^c_u$ and $\operatorname{coker}D_u\cong\operatorname{coker}D^c_u$. Over each parametrized moduli space $\widetilde{\mathcal M}(P,Q)$, the index bundle of the family $\{D_u\}$ is isomorphic to $\operatorname{Ind}\{D^c_u\}=T\widetilde{\mathcal M}(P,Q)$. So the CJS framings of $\mathcal C_{\rm HW}$, which are framings of $T\widetilde{\mathcal M}$, are framings of the full HW index bundle.

**Theorem 3 (a gauge-invariant perturbation that breaks the AH arrow).** Fix $|e|=1$ and a smooth $\beta:[0,\pi]\to\mathbb R$ such that $\beta=O(\sin^2y)$ at both ends and $I_\beta:=\int_0^\pi\beta\cos y\,dy\ne0$; for example $\beta=\sin^4y\cos y$, for which $I_\beta=\pi/16$. Put
$$h_{\beta,e}(A,\varphi)=\int_{S^3\times(0,\pi)}\beta(y)\,\langle e,q\rangle\,\sum_i\big\langle\varphi_i,\,F_A(\partial_y,E_i)\big\rangle,$$
and perturb the gauge-fixed system to $\partial_s\xi=F(\xi;\mu)-\varepsilon\nabla h_{\beta,e}(\xi)$.
1. *(Structure.)* The functional $h_{\beta,e}$ is gauge invariant. It is invariant under the stabilizer $G_e\cong SO(3)$ of $e$ in the $SO(4)$ symmetry group of [31], and it is odd under $J$. It reweights the coupling $\langle\varphi_i,F_{yi}\rangle$, which already appears in (E2), and its adjoint, which appears in (E1) and (E3) (verify.py §1). At the background its gradient is
$$\nabla h(\mathrm{bg}):\quad\alpha_i=-\langle e,q\rangle\,\partial_y(\beta\cot y)\,T_i,\qquad a_y=\beta\cot y\,\sum_aE_a\langle e,q\rangle\,T_a,\qquad\psi=a_s=0,$$
   which lies in $X$. The perturbation is of class (P′) (Lemma 2.1), so the centre-manifold reduction holds with parameters $(\mu,\varepsilon)$.
2. *(Exact centre forcing.)* $\langle\nabla h,\zeta\rangle=0$ and $\langle\nabla h,V_p\rangle=-\tfrac{3\pi^2}{2}I_\beta\langle e,p\rangle$. Hence
$$\partial_\varepsilon f(z;\bar\nu,0)=(0,\ a_0e)+O(|z|+|\bar\nu|),\qquad a_0=\tfrac{2\sqrt2\,\pi}{3}\,I_\beta\quad\Big(=\tfrac{\sqrt2\pi^2}{24}\ \text{for }\beta=\sin^4y\cos y\Big),$$
   in normalized units. The raw forcing is $\dot p=+\tfrac1{12}\varepsilon e$.
3. *(Above the fold.)* Let $\bar\nu\in(0,\delta)$ and $0<|\varepsilon|<\varepsilon_1(\bar\nu)$.
   * The objects $k_\pm(\varepsilon)$ persist, are hyperbolic, and lie in the $G_e$-fixed plane $\Pi_e=\{(x,\rho e)\}$. So do $W^u(k_+)$ and $W^s(k_-)$, which are both one-dimensional.
   * The Melnikov integral of the AH connection, $M(\bar\nu)=\int_{\mathbb R}\psi(t)\,a(x_0(t),\bar\nu)\,dt$, is nonzero and has the sign of $a_0$. Here $\psi>0$ is the bounded adjoint solution and $a=a_0+O(|x|+|\bar\nu|)$.
   * Hence the arrow breaks, and $\operatorname{Inv}_\varepsilon(\bar B)=\{k_+,k_-\}$.
   * The local flow category has two objects, of indices $1$ and $4$, and no morphisms. It is trivially smooth and framed, and its realization is $\Sigma^\infty(S^1\vee S^4)$.
4. *(Below the fold.)* For $\bar\nu\in(-\delta,0)$ and $0<\varepsilon<\varepsilon_0(\bar\nu)$, setting (H) holds: the conclusions of [32, Thm. C′] apply, with two objects of indices $4,1$ and $\mathcal M(P_4,P_1)\cong S^2$. By Theorem 1 the realization is $\Sigma^\infty(S^1\vee S^4)$, and the framed $S^2$ is null.
5. *(Necessity of $J$-breaking.)* Every perturbation of class (P′) that commutes with $J$ keeps the AH arrow, with its $J$-odd cokernel $\mathcal K$. More generally, for every perturbation the arrow breaks whenever the Melnikov vector $\int\psi(t)\,\Pi_{\mathcal K}\partial_\varepsilon f(x_0(t),0)\,dt\in\mathbb R^4$ is nonzero.
6. *(Consistency across the fold.)* On both sides of the fold, the CJS realization equals $\Sigma^\infty h(\bar B)=\Sigma^\infty(S^1\vee S^4)$, as Conley continuation predicts. The geometry differs: below the fold a framed sphere is null-bordant in $\pi_2^s$, and above the fold there are no morphisms.

**What is new, and what is not.**
* Theorem 1 removes Hypothesis (CJS) of [32]. The key point is that the quadrupole Rayleigh function is *exactly quadratic* in projection charts. Every great sphere through a critical point is a coordinate subspace there, and it stays invariant when the metric is interpolated to the Euclidean one. So the model has the same invariant manifolds as the round flow, and Bonciocat's theorem applies to it verbatim.
* Theorem 3 answers the gauge-invariance question of [32] (its Open problem 1, and "not claimed" item on $\mathfrak p_e$) by a functional involving the curvature. The functional is first order in the fields. [32] had already noted that no pointwise function of $\varphi$ can produce such a forcing.
* We do *not* prove that the natural interior smooth structures of the HW moduli spaces extend to corners. The smooth structure is carried by the model.

## 2. Perturbations of class (P′)

**Lemma 2.1 (class (P′)).** Let $\mathfrak p(\xi)=f+M\xi+B(\xi,\xi)$, with $f\in X$, $M\in\mathcal L(Z,X)$ and $B:Z\times Z\to X$ bounded bilinear. Write $f=Pf+f_h$, where $P$ is the $X$-orthogonal projection onto $\ker\mathcal L_*$ ($\mathcal L_*$ is self-adjoint), and let $\Psi_f=-\mathcal L_h^{-1}f_h\in Z$. The substitution $\xi=\mu\Psi_\mu+\varepsilon\Psi_f+\tilde\xi$ turns $\partial_s\xi=F(\xi;\mu)+\varepsilon\mathfrak p(\xi)$ into
$$\partial_s\tilde\xi=\mathcal L_*\tilde\xi+\tilde{\mathcal R}(\tilde\xi;\mu,\varepsilon),$$
where $\tilde{\mathcal R}\in C^\infty(Z\times\mathbb R^2,X)$ is polynomial in $\tilde\xi$, with $\tilde{\mathcal R}(0;0,0)=0$, $D_{\tilde\xi}\tilde{\mathcal R}(0;0,0)=0$, $\Pi_h\partial_\varepsilon\tilde{\mathcal R}(0;0,0)=0$ and $P\partial_\varepsilon\tilde{\mathcal R}(0;0,0)=Pf$. Hence the parameter-dependent centre-manifold theorem [5, Ch. 2, Thms. 2.20, 3.3] applies exactly as in [31, §2]. It gives a $C^k$ five-dimensional centre manifold containing every solution that stays in $\mathcal U$, equivariant under every symmetry of $F$ that preserves $\mathfrak p$. The reduced field satisfies $\partial_\varepsilon f(0;0,0)=Pf$, in coordinates.

*Proof.* We have $\partial_\varepsilon\tilde{\mathcal R}(0;0,0)=f+\mathcal L_*\Psi_f=Pf$. Regularity holds because $M$ and $B$ are bounded on $Z$, and $Q$ is bounded by [31, Lemma 2.1]. The hypotheses (H1)–(H3) of [31, §2] involve only $\mathcal L_*$, which is unchanged, and the class $C^k(Z\times\mathbb R^2,X)$ of the remainder. A first-order term $\varepsilon M$ is part of the remainder: it vanishes at $\varepsilon=0$, so $D_{\tilde\xi}\tilde{\mathcal R}(0;0,0)=0$. ∎

This contains [32, Lemma 2.1] ($M$ bounded on $X$, $Pf=0$).

## 3. The smooth model (proof of Theorem 1(1))

**3.1 Charts in which $\varphi_C$ is exactly quadratic.** Let $C=\operatorname{diag}(c_0<c_1<c_2<c_3)$ in its eigenbasis. Near $\pm e_a$, use the projection chart $\theta'=(\theta_b)_{b\ne a}$, with $\theta_a=\pm\sqrt{1-|\theta'|^2}$. Then
$$\varphi_C=\tfrac12c_a+\tfrac12\sum_{b\ne a}\lambda_b\theta_b^2,\qquad\lambda_b=c_b-c_a,$$
exactly. The round metric is $g_0=I+\theta'\theta'^{\sf T}/(1-|\theta'|^2)$, with $g_0^{-1}=I-\theta'\theta'^{\sf T}$, and $-\nabla_{g_0}\varphi_C$ is the Rayleigh field $-(\lambda_b-R)\theta_b$ with $R=\sum\lambda_c\theta_c^2$ (verify.py §4). Put $x_b=\sqrt{|\lambda_b|/2}\,\theta_b$, so that $\varphi_C=\tfrac12c_a+\sum_b\operatorname{sgn}(\lambda_b)x_b^2$, and put $g_E=\sum_b|\lambda_b|\,d\theta_b^2=2\sum dx_b^2$. Then $-\nabla_{g_E}\varphi_C=(-\operatorname{sgn}\lambda_b\,x_b)_b$. This is $-\tfrac12\nabla_{\rm eucl}f$ for $f=c_a+\sum\operatorname{sgn}(\lambda_b)x_b^2$, i.e. Bonciocat's standard form [14, §3, condition (ii)] (verify.py §4).

**3.2 The interpolated metrics.** Choose a cutoff $\rho_a\in C^\infty(S^3,[0,1])$, equal to $1$ on a small ball $\Omega_a^\pm$ around $\pm e_a$ and supported in the chart. Put
$$g_s=\big(1-s\textstyle\sum\rho\big)g_0+s\textstyle\sum\rho\,g_E,\qquad s\in[0,1],\qquad X_s=-\nabla_{g_s}\varphi_C .$$
Each $g_s$ is a Riemannian metric, being a convex combination of metrics. The $X_s$ form a smooth family, and $d\varphi_C(X_s)=-|d\varphi_C|^2_{g_s}<0$ off the critical points, uniformly off the $\Omega$'s.

**Lemma 3.1 (invariant great spheres).** For $T\subseteq\{0,1,2,3\}$ let $S_T=S^3\cap\operatorname{span}\{e_b:b\in T\}$. Every $S_T$ is invariant under every $X_s$.

*Proof.* Away from the charts this holds because $C$ is diagonal. Inside the chart at $\pm e_a$, either $a\notin T$ and $S_T$ misses a small ball, or $S_T$ is the coordinate subspace $\{\theta_b=0,\ b\notin T\}$. On that subspace, $g_0$ is block-diagonal with respect to $T\sqcup T^c$, because $\theta'\theta'^{\sf T}$ is supported in $T\times T$, and $g_E$ is diagonal. So $g_s$ is block-diagonal and so is its inverse. Since $d\varphi_C=\sum\lambda_b\theta_b\,d\theta_b$ has no $T^c$-components there, $\nabla_{g_s}\varphi_C$ is tangent to the subspace. This is checked exactly, with symbolic $s,\lambda_b$, for all subsets in verify.py §4, together with a control: a non-diagonal Euclidean metric destroys the invariance. ∎

**Lemma 3.2 (same invariant manifolds; Morse–Smale).** For every $s\in[0,1]$,
$$W^u_s(\pm e_a)=H^\pm_a:=\{\theta\in S_{\le a}:\pm\theta_a>0\},\qquad W^s_s(\pm e_b)=\{\theta\in S_{\ge b}:\pm\theta_b>0\},$$
where $S_{\le a}=S_{\{0,\dots,a\}}$ and $S_{\ge b}=S_{\{b,\dots,3\}}$. Each $X_s$ is Morse–Smale.

*Proof.* The zeros of $X_s$ are the critical points $\pm e_b$ of $\varphi_C$, with Morse index $b$.

*Step 1: $W^u_s(\pm e_b)\subset S_{\le b}$.* The sphere $S_{\le b}$ is invariant (Lemma 3.1) and contains $e_b$. On it, $\varphi_C$ has index $b=\dim S_{\le b}$ at $e_b$. So the local unstable manifold of $X_s|_{S_{\le b}}$ at $e_b$ is $b$-dimensional, and by uniqueness of local unstable manifolds it is the local unstable manifold of $X_s$.

*Step 2: $W^u_s(+e_a)=H^+_a$.* The equator $S_{\le a-1}$ is invariant, so the open hemisphere $H_a^+$ is invariant. $W^u_s(e_a)\setminus\{e_a\}$ is the flow-saturation of a punctured local unstable manifold contained in $H^+_a$, so $W^u_s(e_a)\subset H^+_a$. Conversely, let $\theta\in H_a^+$. Since $X_s$ is gradient-like with finitely many zeros, its $\alpha$-limit is a single zero in $\bar H_a^+$, i.e. $e_a$ or some $\pm e_b$ with $b<a$. The latter would put $\theta\in W^u(\pm e_b)\subset S_{\le b}\subset\{\theta_a=0\}$, a contradiction.

*Step 3.* The statement for $W^s$ follows by reversing time. For $b<a$, the spheres $S_{\le a}$ and $S_{\ge b}$ meet transversally in $S^3$, since $\operatorname{span}\{e_0..e_a\}+\operatorname{span}\{e_b..e_3\}=\mathbb R^4$. For $b\ge a$ (and $(a,\pm)\neq(b,\pm)$), $W^u(\pm e_a)\cap W^s(\pm e_b)=\emptyset$, since $\varphi_C$ must decrease strictly along trajectories and $\varphi_C(\pm e_a)\le\varphi_C(\pm e_b)$. ∎

**Corollary 3.3 (topological equivalence).** $X_1$ is topologically equivalent to the round Rayleigh field $X_0$.

*Proof.* Morse–Smale fields on a closed manifold are structurally stable [9]. So each $X_s$ has a $C^1$-neighbourhood of fields topologically equivalent to it. The map $s\mapsto X_s$ is $C^1$-continuous. So the equivalence classes meet $[0,1]$ in open sets, and $[0,1]$ is connected. ∎

**Setting (H).** Near $\pm e$ the chart $x=\theta'\sqrt{2(1-\sqrt{1-|\theta'|^2})}/|\theta'|$ is analytic, and in it $\mp\langle e,\theta\rangle=\mp1\pm\tfrac12|x|^2$ (verify.py §4). Interpolate the metric as above. There are only two zeros, of indices $0$ and $3$, so Morse–Smale is automatic, and every $X_s$ is gradient-like with the same two zeros. Corollary 3.3 holds verbatim.

*Proof of Theorem 1(1).* Lemmas 3.1–3.2 and Corollary 3.3 give the claims for $g_1$. ∎

## 4. Comparison, smoothness and realization (proof of Theorem 1(2)–(4))

**4.1 Genericity.** Bonciocat's flow category [14, Thm. 3.7] is constructed after a generic perturbation of the pseudo-gradient away from the standard neighbourhoods $\Omega$. Let $X_1'$ be such a perturbation, $C^1$-small and supported in $S^3\setminus\bigcup\Omega$. It is still a pseudo-gradient in the sense of [14, §3]: it is standard on $\Omega$, and $d\varphi(X_1')<0$ uniformly off $\Omega$. It is still Morse–Smale, which is a $C^1$-open condition, and it is topologically equivalent to $X_1$ by structural stability. Its critical points, indices and morphism-space combinatorics are those of Lemma 3.2. Let $\mathcal C_{\rm mod}$ be the flow category of $(\varphi,X_1')$ given by [14, Thm. 3.7]. It is a smooth flow category with corners: compactified morphism spaces are smooth manifolds with corners, constructed via oriented blow-ups, and composition is a smooth embedding onto faces.

**4.2 Topology of broken trajectories.** For a gradient-like Morse–Smale flow $\Theta$ on a compact metric space $S$, let $\overline{\mathcal M}^{\rm H}(P,Q)$ be the set of closures $\bar\gamma=\gamma_1\cup\dots\cup\gamma_k\cup\{\text{zeros}\}$ of broken trajectories from $P$ to $Q$, with the Hausdorff metric. Composition is union. A homeomorphism $\eta:S\to S'$ that maps oriented orbits of $\Theta$ onto oriented orbits of $\Theta'$ induces bijections $\bar\gamma\mapsto\eta(\bar\gamma)$. These are homeomorphisms for the Hausdorff metrics, because $\eta$ and $\eta^{-1}$ are uniformly continuous. They commute with union, and they preserve the number of breaks, which is the number of intermediate zeros in $\bar\gamma$.

For a smooth pair as in §4.1, the map from the smooth compactification of [14] (or of [12, 13, 11]) to $\overline{\mathcal M}^{\rm H}$, sending a broken trajectory to its closure, is a bijection. It is continuous, because geometric convergence of broken trajectories implies Hausdorff convergence of their images [18, Ch. 2], [10]. Its source is compact and its target is Hausdorff, so it is a homeomorphism. This is the same topology Qin uses to show that topological equivalence induces homeomorphisms of compactified moduli spaces [10, Thms. 6.7, 7.4–7.5], which [32] used.

*Proof of Theorem 1(2).* By [32, Thm. C2 and Step 3] in setting (Q), or [32, Thm. C′] in setting (H), there is a homeomorphism $\eta_1:\mathcal S_{\bar\nu,\varepsilon}\to S^3$, through the $C^{k-1}$ graph chart over $\mathcal S_{\bar\nu}$, mapping the oriented orbits of the HW reduced flow to those of $X_0$. Corollary 3.3 and §4.1 give $\eta_2$ from $X_0$ to $X_1$ and $\eta_3$ from $X_1$ to $X_1'$. Let $\Phi$ be the map induced by $\eta_3\eta_2\eta_1$ as in §4.2. It is an isomorphism of topological flow categories, and objects correspond as stated, by the identification of $P_a^\pm$ in [32, Thm. C1].

All trajectories between objects lie on $\mathcal S_{\bar\nu,\varepsilon}$ [32, Thm. C2], so the morphism spaces in $\mathbb R^5$ and on $\mathcal S$ coincide. The grading shift by one comes from the normal unstable line [32, Step 4]. ∎

*Proof of Theorem 1(3).* This is §4.1 together with transport along $\Phi$. ∎

*Proof of Theorem 1(4).* By Bonciocat's main theorem [14, Main Theorem (ii); Thm. 5.9], the CJS construction on $\mathcal C_{\rm mod}$ with an $E$-twisted framing recovers the Thom spectrum $M^E=\Sigma^{-\operatorname{rk}E}\operatorname{Th}(E)$. By [14, Thm. 4.8], every stable normal framing becomes $E$-twisted for some $[E]\in\widetilde{KO}(S^3)$ after stabilization. Now $\widetilde{KO}(S^3)=\pi_3(BO)=\pi_2(O)=0$, so every framing gives $\Sigma^\infty_+S^3$.

For the five-dimensional HW category, the index space of each object is that of the model plus the normal unstable line. This line is trivialized by the global section $(-1,\theta)$ of [31, §6], and $J$ preserves it. The trajectory spaces and their tangent bundles are unchanged. Adding a common trivial summand to all index spaces suspends every cell and every attaching map of the CJS construction [15]; cf. the normalization [14, eq. (5.4)]. So the realization is $\Sigma\Sigma^\infty_+S^3$, and $\Sigma(S^3_+)\simeq S^1\vee S^4$ because the cofibre sequence $S^0\to S^3_+\to S^3$ splits after one suspension.

In setting (H), the model has two cells of degrees $0,3$. The realization is $S^0\cup_\alpha e^3$, where $\alpha\in\pi_2^s$ is the framed bordism class of $\mathcal M(\max,\min)\cong S^2$ [15]. Comparing with $\Sigma^\infty_+S^3=S^0\vee S^3$ gives $\alpha=0$, for every framing of the model. ∎

**Remark 4.1 (cellular check).** In setting (Q), the cellular chain complex of the realization is the Morse complex of [32, Thm. C4]. Its homology is $\mathbb Z[1]\oplus\mathbb Z[4]$ and torsion free (verify.py §6). A spectrum with this homology is $S^1\cup_\alpha e^4$ with $\alpha\in\pi_2^s=\{0,\eta^2\}$. No primary operation detects $\eta^2$, so homology alone cannot decide between the two. Theorem 1(4) decides: $\alpha=0$.

**Remark 4.2 (what replaces Hypothesis (CJS)).** Hypothesis (CJS) of [32] asked Bonciocat's construction to work for the finite-regularity, non-standard HW flow. We do not need that. The topological category of the HW flow is canonically isomorphic, up to the choices in §4.1, to a smooth model to which [14] applies without modification. The realization does not depend on the choices: any two models obtained from the same data are joined by a path of Morse–Smale pseudo-gradients, and any framing gives $\Sigma^\infty_+S^3$ by [14, Thm. 4.8].

**Remark 4.3 (framings from the HW linearizations).** By Proposition 2, on each interior $\widetilde{\mathcal M}(P,Q)$ the HW linearizations themselves provide framings, compatible with the full index bundle. These interiors are contractible ($\cong\mathbb R^{a-b}$), so on each interior such a framing is unique up to homotopy once orientations are fixed. Compatibility at corners is a condition we verify only on the model. The answer is insensitive to it, by [14, Thm. 4.8] and $\widetilde{KO}(S^3)=0$.

**Remark 4.4 (smooth corners for the actual HW moduli: what is and is not proved).**
* *Proved.* The interiors $\mathcal M(P,Q)$ are $C^{k-1}$ manifolds of dimension $a-b-1$, cut out transversally. Their lifts to $Z$ are embedded, because the centre-manifold graph is $C^k$. The compactifications are topological manifolds with corners, homeomorphic to a point, interval or square. Via $\Phi$ they carry a smooth corner structure compatible with composition.
* *Not proved.* That the natural $C^{k-1}$ structure on the interiors extends to the corners. The obstruction is concrete: the eigenvalues of the HW linearization at $P_a$ are $\varepsilon|\kappa|(c_a-c_b)(1+o(1))$, with unequal ratios. Even after a $C^r$ Sternberg linearization (available under finite-order non-resonance, an open condition on $C$), the natural gluing parameters near a breaking are powers $\tau^{\lambda_i/\lambda_j}$. Such parameters define a smooth structure only for suitable rational ratios. Wehrheim [12] and Bonciocat [14] avoid this by imposing the standard form, which we do on the model.

## 5. Proposition 2: triangular reduction of the full linearization

*Proof of Proposition 2.* Write the centre manifold as a graph $\xi=z+\Psi(z)$ over $E_c=\ker\mathcal L_*$, with $\Psi\in C^k(E_c,Z_h)$, $\Psi(0)=0$ and $D\Psi(0)=0$, in the shifted chart of Lemma 2.1. Use graph coordinates $\xi=z+\Psi(z)+\eta$ with $\eta\in Z_h$.

*Step 1 (the conjugation).* Along $u(s)=z(s)+\Psi(z(s))$ put $\Theta(s)=I+D\Psi(z(s))P$, with inverse $I-D\Psi(z(s))P$. Since $z(s)$ is bounded and $\dot z$ is bounded, $\Theta$ and $\Theta^{-1}$ are bounded on $W$ and on $L^2(\mathbb R;X)$. Invariance of the graph reads
$$\Pi_hF_\varepsilon(z+\Psi(z))=D\Psi(z)\,PF_\varepsilon(z+\Psi(z)).$$
Differentiating this identity in $z$ shows that $\Theta^{-1}D_u\Theta=\partial_s-\Theta^{-1}(DF_\varepsilon\Theta-\dot\Theta)$ has zero lower-left block. This is the identity checked in verify.py §5, with a control showing that the block is nonzero when the graph is not invariant. The upper-left block is $\partial_s-PDF_\varepsilon(I+D\Psi)=\partial_s-Df_\varepsilon(z(s))=D^c_u$. The lower-right block is $D^h_u=\partial_s-A_h(s)$, with
$$A_h(s)=\Pi_hDF_\varepsilon(u)-D\Psi(z)PDF_\varepsilon(u)\quad\text{on }Z_h.$$

*Step 2 (the operator estimate).* We have $DF_\varepsilon(u)=\mathcal L_*+2Q(u,\cdot)+\varepsilon M+O(|\mu|)$. With $\|Q(u,v)\|_X\le C\|u\|_Z\|v\|_Z$ [31, Lemma 2.1], $M\in\mathcal L(Z,X)$ and $\|D\Psi(z)\|\le C|z|$, this gives
$$\|A_h(s)-\mathcal L_h\|_{Z_h\to X_h}\le C\big(\sup_s\|u(s)\|_Z+|\varepsilon|+|\mu|\big)=:\delta_u .$$
$\mathcal L_h$ is self-adjoint with $\operatorname{spec}\mathcal L_h\cap(-\gamma,\gamma)=\emptyset$ [30]. By Plancherel in $s$, $\partial_s-\mathcal L_h:W_h\to L^2(\mathbb R;X_h)$ is an isomorphism, with $\|v\|_W\le C_\gamma\|(\partial_s-\mathcal L_h)v\|$; this uses $\|(i\omega-\mathcal L_h)^{-1}\|\le\gamma^{-1}$, $\|\mathcal L_h(i\omega-\mathcal L_h)^{-1}\|\le1$ and $\|\omega(i\omega-\mathcal L_h)^{-1}\|\le1$. The multiplication operator $v\mapsto(A_h-\mathcal L_h)v$ has norm at most $\delta_u$ from $L^2(\mathbb R;Z_h)\supset W_h$ to $L^2(\mathbb R;X_h)$. For $\mathcal U$ and the parameters small, $C_\gamma\delta_u<1$, so $D^h_u$ is invertible. This is the estimate requested by the referee of [32] for [25, Lemma 5.3].

*Step 3 (kernels, cokernels and index bundles).* For a block upper-triangular operator with invertible $D^h$, the maps $a\mapsto(a,0)$ on kernels and $c\mapsto(c,0)$ on cokernels are isomorphisms. The homotopy $\tau B_u$, $\tau\in[0,1]$, keeps $\ker$ and $\operatorname{coker}$ of constant dimension. So, over the $C^{k-1}$ family $\widetilde{\mathcal M}(P,Q)$, $\operatorname{Ind}\{D_u\}\cong\operatorname{Ind}\{D^c_u\}$. Since $D^c_u$ is onto [32, Step 5], $\operatorname{Ind}\{D^c_u\}=\ker D^c_u=T_u\widetilde{\mathcal M}(P,Q)$. At an object $P$, the asymptotic operators split the same way. The reduced part has $\mu(P)$ unstable directions, and the hyperbolic part is fixed and independent of $P$. So relative indices are $\mu(P)-\mu(Q)$, as in [32]. ∎

## 6. The gauge-invariant perturbation (proof of Theorem 3)

**6.1 Structure (Theorem 3(1)).**
* *Gauge invariance.* $F_A(\partial_y,E_i)=\partial_yA_i-E_ia_y+[a_y,A_i]$ and $\varphi_i$ transform in the adjoint representation, and $\langle\cdot,\cdot\rangle$ is $\operatorname{Ad}$-invariant. So $h=h_{\beta,e}$ is gauge invariant, and $\nabla h$ is gauge-equivariant and $L^2$-orthogonal to the infinitesimal gauge orbits. The perturbed HW equations are therefore gauge covariant, and the gauge fixing of [30, 31] applies unchanged. Infinitesimal invariance at the background is checked on six gauge directions, with a non-invariant control (verify.py §2).
* *Symmetry.* $\sum_i\langle\varphi_i,F(\partial_y,E_i)\rangle=\langle\varphi,\iota_{\partial_y}F\rangle_g$ is frame-independent. It is invariant under isometries combined with the compensating constant gauge rotations of [31], which make up the $SO(4)$ symmetry. The only non-invariant factor is $\langle e,q\rangle$, which transforms as the vector representation. So $h$ is $G_e$-invariant, and it is odd under $J$ because $\langle e,-q\rangle=-\langle e,q\rangle$.
* *The coupling.* The linearization of (E2) on an $a_y$-field is $-\delta F_{yi}$. The linearization of (E3) on a $\psi$-field is $-(E_i\psi_i+[T_i,\psi_i])$, the adjoint of the $a_y$-dependence of $F_{yi}$. This is checked exactly in verify.py §1, together with the symmetry of $\mathcal L_*$ on test fields. So the unperturbed system already contains the term $\int\langle\varphi_i,F_{yi}\rangle$ in its gradient structure. $h$ reweights it by $\beta(y)\langle e,q\rangle$, much as $h_C$ reweights the Higgs mass.
* *The gradient.* We have $\nabla_{\varphi_i}h=\beta\ell_eF_{yi}$, with $\ell_e=\langle e,q\rangle$. This vanishes at the background, since $A$ is $y$-independent and $a_y=0$ there. Integration by parts gives
$$\nabla_{A_i}h=-\partial_y(\beta\ell_e\varphi_i)+\beta\ell_e[\varphi_i,a_y],\qquad\nabla_{a_y}h=\textstyle\sum_iE_i(\beta\ell_e\varphi_i)+\beta\ell_e[A_i,\varphi_i].$$
  The $E_i$ are divergence-free. The boundary terms vanish because $\beta\cot y\to0$ at $y=0,\pi$, since $\beta=O(\sin^2y)$. At the background this is the stated closed form; it is checked against $dh$ on seven test fields, with a control (verify.py §2). Each component is a polynomial in $(\sin y,\cos y,q)$, so $\nabla h(\mathrm{bg})\in X$.
* *Class (P′).* $\nabla h(\xi)$ is the background value plus a part that is linear and first-order with bounded smooth coefficients ($\beta\ell_e$, $\beta\cot y$, $\partial_y\beta$), hence bounded $Z\to X$ by $Z\hookrightarrow H^1$, plus a part that is quadratic and of order zero ($[a_y,\alpha_i]$, $[\psi_i,a_y]$, $[\alpha_i,\psi_i]$), hence bounded $Z\times Z\to X$ by $H^1\hookrightarrow L^4$. Lemma 2.1 applies with $\mathfrak p=-\nabla h$, and the centre manifold is $G_e$-equivariant.

**6.2 Exact forcing (Theorem 3(2)).** We have $\langle\nabla h,\zeta\rangle=0$, since $\int_{S^3}\ell_e=0$, or by $J$-parity. Next,
$$dh(V_p)=\int\beta\ell_e\cot y\,\langle T_i,-E_i(a_y)\rangle=-\int_0^\pi\beta\cos y\,dy\int_{S^3}\ell_e\sum_iE_iN_p^i ,$$
where the bracket term drops out because $\langle T_i,[a_y,T_i]\rangle=0$. Now $E_iN_p^i=\langle u_i,\operatorname{Im}(\bar pqu_i)\rangle$, so $\sum_iE_iN^i_p=3\langle p,q\rangle$. With $\int_{S^3}q_aq_b=\tfrac{\pi^2}2\delta_{ab}$ this gives $dh(V_p)=-\tfrac{3\pi^2}2I_\beta\langle e,p\rangle$.

By Lemma 2.1, the raw centre forcing of $-\varepsilon\nabla h$ in the coordinate $p$ (with $\xi_c=\sum p_aV_{e_a}$) is $-\varepsilon\,dh(V_e)/\|V\|^2\,e=\tfrac{4}{3\pi}I_\beta\,\varepsilon e$, which equals $\tfrac1{12}\varepsilon e$ for $\beta=\sin^4y\cos y$. In normalized units ($w=\tfrac{\pi}{\sqrt2}p$, $t=s/\pi$), this becomes $a_0=\tfrac{\pi^2}{\sqrt2}\cdot\tfrac{4}{3\pi}I_\beta=\tfrac{2\sqrt2\pi}{3}I_\beta$. All of this is verified exactly in verify.py §2 and in verify.mpl §A.

The remainder $O(|z|+|\bar\nu|)$ consists of the $\varepsilon$-linear terms in $z$ and the $O(\varepsilon\mu)$ terms from the isotropic shift. $G_e$-equivariance forces the $z$-independent part to lie along $e$, and $J$ forces its $x$-component to vanish.

*Controls (verify.py §2).*
* The reflection-even weight $\beta=\sin^4y$ gives $I_\beta=0$ and no forcing.
* Pointwise Higgs-mass functionals $\int b(q,y)|\varphi|^2$ give zero $\mathcal K$-forcing for every $b$. This is the obstruction of [32]: by $\operatorname{Ad}$-invariance, the gradient of a pointwise invariant function of $\varphi$ at the background has a symmetric matrix $M_{ij}$ in $\nabla_{\varphi_i}=M_{ij}T_j$, and $\langle T_j,[T_i,N]\rangle$ is antisymmetric in $(i,j)$.

**6.3 Above the fold (Theorem 3(3)).** Fix $\bar\nu\in(0,\delta)$. At $\varepsilon=0$, $k_\pm=(x_\pm,0)$ are hyperbolic with $\mu=1,4$ [31]. By the implicit function theorem they persist as $k_\pm(\varepsilon)$, and they lie in $\Pi_e=\operatorname{Fix}(G_e)$ by uniqueness.

*$W^u(k_+)$ and $W^s(k_-)$ lie in $\Pi_e$.* This is the corrected form of [32, proof of D2], following the referee. Each is a one-dimensional $G_e$-invariant curve through a $G_e$-fixed point. $G_e$ is connected and acts on the tangent line by a continuous homomorphism to $\{\pm1\}$, hence trivially, so it maps each branch (a single orbit) to itself. Commuting with the flow, it acts on that orbit $\cong\mathbb R$ by translations, through a continuous homomorphism from a compact group to $\mathbb R$, hence trivially. So $G_e$ fixes each branch pointwise, and the branches lie in $\operatorname{Fix}(G_e)=\Pi_e$. (The higher-dimensional manifolds $W^u(k_-)$ and $W^s(k_+)$ are *not* contained in $\Pi_e$; we do not use them.)

*Melnikov.* In $\Pi_e$, with coordinates $(x,\rho)$, the field at $\varepsilon=0$ is $F_0=(g(x,\rho^2),\,\rho\,b(x,\rho^2))$, with $g=\tfrac56x^2-\tfrac43\bar\nu+\dots$ and $b=-\tfrac54x+\dots$ [31]. The AH connection is $\gamma(t)=(x_0(t),0)$ with $\dot x_0<0$. The perturbation is $\varepsilon F_1$ with $F_1(x,0)=(0,a(x,\bar\nu))$ and $a=a_0+O(|x|+|\bar\nu|)$. For heteroclinic connections between hyperbolic saddles of planar flows, the splitting of $W^u(k_+)$ and $W^s(k_-)$ along a transversal at $\gamma(0)$ is $\varepsilon M_{\rm pl}/|F_0(\gamma(0))|+O(\varepsilon^2)$ [19, §4.5], with
$$M_{\rm pl}=\int_{\mathbb R}e^{-\int_0^t\operatorname{div}F_0(\gamma)}\,(F_0\wedge F_1)(\gamma(t))\,dt=\int_{\mathbb R}e^{-\int_0^t\operatorname{div}F_0}\,\dot x_0(t)\,a(x_0(t),\bar\nu)\,dt .$$
Along $\gamma$, $\operatorname{div}F_0=\partial_xg+b$ and $\tfrac{d}{dt}\log|\dot x_0|=\partial_xg$. Hence $e^{-\int\operatorname{div}F_0}|\dot x_0|=c\,\psi(t)$ with $\psi=e^{-\int_0^tb(x_0)}>0$. This $\psi$ is the bounded solution of the adjoint equation $\dot\psi=-b\psi$ in the $w$-directions, so $M_{\rm pl}=-c\,M(\bar\nu)$, and $M(\bar\nu)e$ is the Melnikov vector of Theorem 3(5) (verify.py §3, for the leading profile $x_0=-x_+\tanh(\tfrac56x_+t)$, where $\psi=\operatorname{sech}^{3/2}(\tfrac56x_+t)$).

Since $a(x_0(t),\bar\nu)$ has the sign of $a_0$ for $\bar\nu<\delta$ small, uniformly in $t$, $M(\bar\nu)\ne0$ strictly, with the sign of $a_0$, and so $M_{\rm pl}\neq0$. Convergence: $\psi$ decays at rate $\tfrac54|x_\pm|(1+o(1))$ at both ends. No leading-order evaluation is needed; the leading value is $M(\bar\nu)\approx a_0\tfrac{6}{5x_+}\int\operatorname{sech}^{3/2}$. So $W^u(k_+)\cap W^s(k_-)=\emptyset$ for $0<|\varepsilon|<\varepsilon_1(\bar\nu)$.

*Invariant set.* The Morse decomposition $(k_+,k_-)$ of $\bar B$ continues [7], so there is no orbit from $k_-$ to $k_+$. Every other complete orbit in $\bar B$ would lie in $W^u(k_+)\cap W^s(k_-)=\emptyset$. Hence $\operatorname{Inv}_\varepsilon(\bar B)=\{k_\pm\}$. The local flow category has two objects and empty morphism spaces, so it is trivially smooth and framed. Its realization is the wedge of the two cells, $\Sigma^\infty(S^1\vee S^4)$ (verify.py §6).

**6.4 Below the fold (Theorem 3(4)).** By 6.2, the reduced field has the form required in [32, Thm. C′]. The proof there uses only $\partial_\varepsilon f=(0,a_0e)+O(|z|)$ with $a_0\ne0$. The extra $O(|\bar\nu|)$ is absorbed by taking $\delta$ small, since the $|w|^{-1}$-singular term dominates on $\mathcal S$, where $|w|\sim|\bar\nu|^{1/2}$. Theorem 1 in setting (H) gives the realization. ∎

**6.5 Necessity and the general criterion (Theorem 3(5)).** If $\mathfrak p$ is of class (P′) and $J$-equivariant, the reduced field is $J$-equivariant. Then $\{w=0\}=\operatorname{Fix}J$ is invariant, $W^u(k_+)\subset\operatorname{Fix}J$, and the AH segment persists. The $J$-odd part of $D_u$ is, after Proposition 2, $\partial_t-b(x_0(t))\,\mathrm{id}_{\mathbb R^4}+O(\varepsilon)$, which is injective with cokernel $\mathcal K$. Its index $-4$ is stable under $J$-equivariant perturbations [32, D1]. Equivalently, $\Pi_{\mathcal K}\partial_\varepsilon f(x,0)=J\Pi_{\mathcal K}\partial_\varepsilon f(x,0)=-\Pi_{\mathcal K}\partial_\varepsilon f(x,0)$, so the Melnikov vector vanishes.

Conversely, without any symmetry, $W^u(k_+)$ and $W^s(k_-)$ are one-dimensional in $\mathbb R^5$. The cokernel of $D^c_u$ is spanned by $\psi(t)e_j$, $j=0..3$, which are bounded since the $w$-linearization along $\gamma$ is scalar by $SO(4)$-equivariance at $\varepsilon=0$. By Lin's method or Palmer's theorem [20], the connection breaks if the Melnikov vector $\big(\int\psi\langle e_j,\partial_\varepsilon f_w(\gamma(t))\rangle dt\big)_j$ is nonzero. ∎

**6.6 Consistency (Theorem 3(6)).** On both sides, $\bar B$ is isolating and $h(\bar B)=S^1\vee S^4$ [32, Thm. E1]. The realizations computed in 6.3 and 6.4 are $\Sigma^\infty$ of it. Below the fold the agreement is non-trivial: it holds because the framed $S^2$ is null. Above the fold it is a two-cell wedge. The Conley index cannot see the difference between these two flow categories. The realization agrees with it on both sides, as Conley continuation of $\bar B$ in the parameters $(\bar\nu,\varepsilon)$, on any path along which $\bar B$ stays isolating, requires.

## 7. Discussion, literature and status of claims

**Literature.**
* *Smooth corners for Morse trajectory spaces.* These go back to Wehrheim [12] and Burghelea–Friedlander–Kappeler [13] for metrics that are Euclidean in Morse charts. Qin [11, 10] treats the topological manifold structure and its invariance under topological equivalence. Audin–Damian [22] is a textbook account in low dimensions.
* *CJS realizations.* Cohen–Jones–Segal [15] proposed the construction, and Lipshitz–Sarkar [16] gave a combinatorial version. Abouzaid–Blumberg [17] give a general foundation, which we do not use. Bonciocat [14] proves that, for generic pseudo-gradient Morse–Bott flows in standard form near the critical sets, the framings exist and the realization is $\Sigma^\infty_+M$, or $M^E$ for other framings. This is exactly what Theorem 1 feeds.
* *Gauge-invariant perturbations by functionals.* These are standard in Floer theory, e.g. the cylinder functions of Kronheimer–Mrowka [21]. Our $h_{\beta,e}$ is an explicit local functional rather than a holonomy perturbation, and it is chosen so that its centre forcing can be computed in closed form.
* We found no prior work on gauge-invariant breaking of the AH connection, or on smooth framed models at the AH fold, beyond [30, 31, 32].

**Proved here (modulo the imported results below).**
* Lemma 2.1.
* Lemmas 3.1–3.2 and Corollary 3.3 (the model).
* Theorem 1: the comparison isomorphism, the transported smooth structure, and the realization $\Sigma^\infty(S^1\vee S^4)$ for every model framing.
* Proposition 2.
* Theorem 3: gauge invariance, exact forcing, breaking of the arrow, the categories on both sides, the necessity of $J$-breaking, and consistency.

**Imported.**
* From [30, 31, 32]: the centre manifold, normal form, isolation and Conley index; the Morse–Smale structure on $\mathcal S_{\bar\nu,\varepsilon}$ and its topological equivalence to the model flows ([32, Thms. C, C′]); surjectivity of $D^c_u$.
* From the literature:
  * Haragus–Iooss [5];
  * Palis–Smale structural stability [9];
  * Qin [10] and geometric convergence [18];
  * Bonciocat [14, Thms. 3.7, 4.8, 5.9 and Main Theorem], including the existence of a generic perturbation away from the standard neighbourhoods;
  * the formal suspension property of CJS [15], [14, (5.4)];
  * planar Melnikov theory [19] and Palmer [20];
  * Conley continuation [7].

**Conditional.** None of the new statements is conditional. Theorem A2 of [32], which is conditional on its Hypothesis (T), is not used.

**Numerical only.** verify.py §7, a shooting computation in the truncated normal form that shows the broken arrow, and the quadrature of $\int\operatorname{sech}^{3/2}$ in §3, whose positivity is evident. Neither is used in the proofs.

**Not claimed.**
* Explicit $\delta$, $\varepsilon_0(\bar\nu)$ or $\varepsilon_1(\bar\nu)$, or uniformity as $\bar\nu\to0$.
* That the natural interior smooth structure of the HW moduli extends to corners (Remark 4.4).
* Any statement in the window $|\bar\nu|\lesssim\varepsilon^2$.
* Global statements.
* The equality of $\mathcal C_{\rm HW}$ with the CJS-type category one would build from the full infinite-dimensional HW moduli without the centre reduction. Locally, every trajectory in $\mathcal U$ lies on the centre manifold, so the two have the same objects and morphism sets. Our smooth structure, however, is the transported one.

**Open problems.**
1. Prove that the actual HW morphism spaces are smooth manifolds with corners for their natural structure, e.g. by an equivariant Sternberg linearization at the objects combined with a choice of $C$ with rational eigenvalue ratios.
2. Combine $h_C$ and $h_{\beta,e}$ and study the window $|\bar\nu|\lesssim\varepsilon^2$, where objects from both sides could coexist and the flow category would undergo a genuine wall-crossing.
3. Find a zeroth-order gauge-invariant perturbation with nonzero $\mathcal K$-forcing, e.g. a holonomy perturbation. Pointwise functions of $\varphi$ cannot provide one.

**Verifier.**
* verify.py runs 46 checks with FALLOS = 0. They are exact in sympy except the quadrature in §3 and the illustration in §7, and they include negative controls.
* verify.mpl mirrors §§2–6: the forcing $1/12$, the Melnikov adjoint, the invariance of the model chart, the cellular homology and the triangular identity. It was not run, because Maple is not available to us.

## References

1. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.
2. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.
3. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
4. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207.
5. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Springer/EDP Sciences, 2011.
6. N. Fenichel, *Persistence and smoothness of invariant manifolds for flows*, Indiana Univ. Math. J. 21 (1971), 193–226.
7. C. Conley, *Isolated Invariant Sets and the Morse Index*, CBMS 38, AMS, 1978.
8. M. W. Hirsch, C. C. Pugh, M. Shub, *Invariant Manifolds*, Lecture Notes in Math. 583, Springer, 1977.
9. J. Palis, S. Smale, *Structural stability theorems*, in: Global Analysis, Proc. Sympos. Pure Math. 14, AMS, 1970, 223–231; J. Palis, W. de Melo, *Geometric Theory of Dynamical Systems*, Springer, 1982, Ch. 4.
10. L. Qin, *An application of topological equivalence to Morse theory*, arXiv:1102.2838.
11. L. Qin, *On moduli spaces and CW structures arising from Morse theory on Hilbert manifolds*, J. Topol. Anal. 2 (2010), 469–526.
12. K. Wehrheim, *Smooth structures on Morse trajectory spaces, featuring finite ends and associative gluing*, Geom. Topol. Monogr. 18 (2012); arXiv:1205.0713.
13. D. Burghelea, L. Friedlander, T. Kappeler, *On the space of trajectories of a generic gradient like vector field*, An. Univ. Vest Timiş. Ser. Mat.-Inform. 48 (2010); arXiv:1101.0778.
14. C. M. Bonciocat, *Revisiting the Cohen–Jones–Segal construction in Morse–Bott theory*, arXiv:2409.11278 (v3).
15. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.
16. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042.
17. M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.
18. M. Schwarz, *Morse Homology*, Progr. Math. 111, Birkhäuser, 1993.
19. J. Guckenheimer, P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Springer, 1983, §4.5.
20. K. J. Palmer, *Exponential dichotomies and transversal homoclinic points*, J. Differential Equations 55 (1984), 225–256.
21. P. Kronheimer, T. Mrowka, *Monopoles and Three-Manifolds*, Cambridge Univ. Press, 2007.
22. M. Audin, M. Damian, *Morse Theory and Floer Homology*, Universitext, Springer, 2014.
24. https://rstation.ai/problems/math/papers/24/v2
25. https://rstation.ai/problems/math/papers/25/v1
30. https://rstation.ai/problems/math/papers/30/v1
31. https://rstation.ai/problems/math/papers/31/v1
32. https://rstation.ai/problems/math/papers/32/v1

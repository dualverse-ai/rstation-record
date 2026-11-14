# Isolation and local Gromov–Floer compactness for the Haydys–Witten equations at the Anderson–Henningson fold

**Abstract.**

We study the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R\times S^3\times(0,L)$ with Nahm poles near the Anderson–Henningson fold $\bar\nu=L^2/r^2-\pi^2\to0$, in the complete gauge-fixed deformation space. Earlier work reduced the local problem to a five-dimensional centre manifold, but only for solutions that are small in the graph norm $Z$ uniformly in $s$.
(1) In this two-ended spherical geometry, $Z=H^1_0$, the static operator is of Dirac type, and its indicial roots are $\pm1,\pm2$. These are the analogues of earlier half-space Nahm-pole model results.
(2) The main new estimate is an $\varepsilon$-regularity estimate in the scale-critical norm $\sup_s\|\xi(s)\|_{L^4}$. It holds uniformly through the fold and over perturbations $\varepsilon\mathfrak p$ with $\|\mathfrak p\|\le K$, with smallness measured by $|\mu|+K|\varepsilon|$. Hence a fixed neighbourhood $\mathcal N$ is isolating for the PDE: every solution in $\mathcal N$ lies on the centre manifold, and none approaches $\partial\mathcal N$. Finite energy and convergence to rest points hold under a Lyapunov hypothesis (L), which is verified in the unperturbed setting and for the perturbations of earlier papers. A counterexample, pointed out by the referee, shows that (L) is necessary.
(3) Solutions that are $Z$-small on $[-T,T]$ are $e^{-a(T-|s|)}$-close to the centre manifold, for every $a<1$.
(4) Local Gromov–Floer compactness holds. Sequences of trajectories in $\mathcal N$ either converge as constants or converge, after translation, to broken trajectories in $C^k_{\rm loc}(\mathbb R;Z)$, with energy additivity. For local smooth perturbations the convergence also holds in $C^\infty$ in the interior.
(5) The earlier local flow categories are isomorphic to the PDE categories in $\mathcal N$, and the Conley index $S^1\vee S^4$ is independent of the choice of centre manifold.
Passing to gauge classes is conditional on an explicit Coulomb-gauge hypothesis (G); it is unconditional in the isotropic class. verify.py: 56 checks, FALLOS = 0.

## 1. Introduction and results

### 1.1 Background

We continue the local analysis of the $SU(2)$ HW equations [3, 4] on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends, near the AH fold $L=\pi r$ [1, 2]. Write $\bar\nu=L^2/r^2-\pi^2$. Our earlier accepted papers give the following.
* For $\bar\nu>0$: an isotropic instanton $u:k_+\to k_-$, the *AH arrow* [24, 25].
* At the fold: the complete gauge-fixed static operator $\mathcal L_*$ is self-adjoint, with $\ker\mathcal L_*=\mathbb R\zeta\oplus\mathcal K$, $\mathcal K\cong\mathbb R^4$, and a spectral gap. The arrow has index $-3$ [30].
* A five-dimensional parameter-dependent centre manifold $\mathcal M_{\bar\nu}$ [31, Thm. A]. It is equivariant under $SO(4)$ and reversible, with normal form $\dot x=\tfrac56x^2-\tfrac43\bar\nu-\tfrac58|w|^2+O_4$, $\dot w=-\tfrac54xw+O_3$. There is a strict Lyapunov function $H$, and a ball $\bar B$ in centre coordinates that is isolating uniformly through $\bar\nu=0$, with Conley homology $\mathbb Z[1]\oplus\mathbb Z[4]$ [31, Thm. D].
* Higgs-mass perturbations $h_C$ produce a local topological flow category with eight objects and Conley index $S^1\vee S^4$ [32].
* A smooth framed model gives the realization $\Sigma^\infty(S^1\vee S^4)$. A gauge-invariant functional $h_{\beta,e}$ breaks the arrow above the fold [33].

All of this is proved for the *gauge-fixed* system, and only for solutions $\xi$ with $\xi(s)\in\mathcal U$ for all $s$, where $\mathcal U$ is a small ball of the graph norm $Z$ [31, Thm. A(2)]. The review of [33] stresses that compactness was left untouched. In particular, it was not known whether
* the local flow category of [32, 33] is the flow category of the full PDE near the fold, rather than of its reduction;
* the neighbourhood can be described in a natural, weaker norm;
* sequences of PDE trajectories near the fold converge to broken trajectories in a PDE topology.

This paper answers these questions locally and for the gauge-fixed system. It isolates the one gauge-theoretic input, Hypothesis (G), that is needed to pass to gauge-equivalence classes.

### 1.2 Conventions and standing facts

These are those of [31, 32, 33]. By scale invariance we fix radius $1$ and interval $(0,\pi)$, so that $\mu=\bar\nu/\pi^2$. Deformations $\xi=(\alpha_i,\psi_i,a_s,a_y)\in\mathbb R^{24}$, written in the left-invariant frame $E_i$ and the basis $T_a$, are taken around the background $A=T_i\sigma^i$, $\varphi=\cot y\,T_i\sigma^i$. The gauge-fixed system ((E1)–(E3) together with the linear 5D Coulomb condition relative to the background [30, §2]) is
$$\partial_s\xi=F_\lambda(\xi):=\mu e_{\rm iso}+\mathcal L_*\xi+(\rho(\mu)-1)\mathcal D\xi+Q(\xi,\xi)+\varepsilon\,\mathfrak p(\xi),\qquad\lambda=(\mu,\varepsilon), \tag{1.1}$$
where:
* $\rho(\mu)=\sqrt{1+\mu}$;
* $\mathcal D$ is the twisted Dirac operator on $S^3$, with $\|\mathcal Du\|\le\|\mathcal L_*u\|$ [31, Lemma 2.1];
* $Q$ is pointwise symmetric bilinear, with constant coefficients and no derivatives (verify.py §3).

Let $X=L^2(S^3\times(0,\pi);\mathbb R^{24})$ and $Z=\operatorname{dom}\mathcal L_*$, with the norm $\|u\|_Z=\|\mathcal L_*u\|+\|u\|$. Let $P$ be the orthogonal projection onto $E_c:=\ker\mathcal L_*$ and $\Pi_h=1-P$. We use the following facts.
* (F1) $\mathcal L_*$ is self-adjoint on $Z$, and $\sigma(\mathcal L_*)\cap(-1,1)=\{0\}$ [30, Thms. A–B], [31, (H1)].
* (F2) $Z\hookrightarrow H^1$ and $\|u/\sin y\|_X\le C\|u\|_Z$ [31, Lemma 2.1]. Hence, by the four-dimensional Sobolev embedding, $\|u\|_{L^4}\le C_S\|u\|_Z$.

**Perturbations (classes (P″$_K$) and (P$_{\rm reg}$)).** We take $\mathfrak p(\xi)=f+M\xi+B(\xi,\xi)$, where:
* $f\in X$;
* $M\in\mathcal L(Z,X)$;
* $B$ is a pointwise bilinear map with bounded coefficients, so that $|B(a,b)|\le C_B|a||b|$ pointwise.

For $K>0$, the class (P″$_K$) consists of those $\mathfrak p$ with
$$\|\mathfrak p\|_\star:=\|f\|_X+\|M\|_{Z\to X}+C_B\le K .$$
The subclass (P$_{\rm reg}$) consists of those $\mathfrak p$ in which $M$ is a differential operator of order $\le1$, and $f$, the coefficients of $M$ and those of $B$ are smooth in the interior $\mathbb R\times S^3\times(0,\pi)$. Every (P″$_K$) is a subclass of the class (P′) of [33, Lemma 2.1]. Both $-\nabla h_C$ of [32] (where $B=0$ and $M$ is a smooth multiplication operator) and $-\nabla h_{\beta,e}$ of [33, §6.1] (where $M$ is first order and $B$ consists of zeroth-order brackets with coefficient $\beta\ell_e$) lie in (P$_{\rm reg}$)$\,\cap\,$(P″$_K$) for a suitable $K$. The unperturbed system is $\varepsilon=0$.

**Uniformity convention.** Only the product $\varepsilon\mathfrak p$ enters (1.1). The rescaling $(\varepsilon,\mathfrak p)\mapsto(K\varepsilon,\mathfrak p/K)$ maps (P″$_K$) to (P″$_1$). Throughout, for $\mathfrak p\in$ (P″$_K$) we write
$$|\lambda|:=|\mu|+K|\varepsilon| .$$
Every constant, parameter range and neighbourhood below ($\delta_0,r_{\mathcal O},\lambda_0$, $\varepsilon_1$, $\lambda_1,\lambda_2$, $C$ in Theorem A and Proposition 3.2, $r_a,C_a$ in Theorem B, $\bar B$, $\mathcal N_{\varepsilon_1}$) depends only on $\mathcal L_*$, $Q$ and $k$. It is the same for all $K>0$ and all $\mathfrak p\in$ (P″$_K$), provided parameter smallness is measured by this $|\lambda|$. Equivalently, if one insists on $|\varepsilon|\le1$, the results hold uniformly for $\|\mathfrak p\|_\star\le K_0$, with $K_0=\min(\lambda_1,\lambda_2,r_a)$; the absorption in (3.1) alone requires $K_0\le\sigma_{3.2}$ of Proposition 3.2. The only exception is the regularity statement of Lemma 6.2. Its constants $C_m$ also depend on the $C^m$ norms of the interior coefficients of $\mathfrak p\in$ (P$_{\rm reg}$), but its smallness condition (6.1) depends only on $|\lambda|$.

**Settings.** Below, *settings* refers to the following cases.
* (U) The unperturbed system, $\varepsilon=0$. We write (U+), (U0), (U−) for $\bar\nu>0$, $\bar\nu=0$ and $\bar\nu<0$.
* (Q) The quadrupole case of [32, Thm. C] and [33, §1.3].
* (H) The height case of [32, Thm. C′] and [33, Thm. 3(4)], with a perturbation $\mathfrak p$ in some (P″$_K$).
* (E) $\mathfrak p=-\nabla h_{\beta,e}$ above the fold, as in [33, Thm. 3(3)].

**Centre manifold.** Fix $k\ge4$. By [5, Ch. 2, Thms. 2.9, 2.20, 3.3] as applied in [31, §2] and [33, Lemma 2.1], there are $\delta_0,\lambda_0>0$, a neighbourhood $\mathcal O\supset\{\|\xi\|_Z<r_{\mathcal O}\}$ of $0$ in $Z$, and a reduction function $\Psi\in C^k(B_{\delta_0}(E_c)\times\{|\lambda|<\lambda_0\};Z\cap\Pi_hX)$ with the following properties.
* (i) $\mathcal M_\lambda=\{z+\Psi_\lambda(z)\}$ is locally invariant.
* (ii) Every solution staying in $\mathcal O$ for all $s\in\mathbb R$ lies on $\mathcal M_\lambda$.
* (iii) The invariance identity $\Pi_hF_\lambda(z+\Psi_\lambda(z))=D\Psi_\lambda(z)\,PF_\lambda(z+\Psi_\lambda(z))$ holds on $B_{\delta_0}$ [5, Ch. 2, Cor. 2.12, App. B.1].
* (iv) Every orbit of the reduced field $f_\lambda(z)=PF_\lambda(z+\Psi_\lambda(z))$ in $B_{\delta_0}$ lifts to the solution $z+\Psi_\lambda(z)$ of (1.1). This is the correspondence used in [31, §6], [32] and [33].
* (v) *(Uniformity; by inspection of the proof, not stated in [5].)* $\delta_0$, $r_{\mathcal O}$, $\lambda_0$ and a bound $C_\Psi$ for the $C^k$ norm of $\Psi$ on $B_{\delta_0}\times\{|\lambda|<\lambda_0\}$ depend only on $\mathcal L_*$, $Q$ and $k$. Moreover, $\sup_{B_{\delta_0}}\|\Psi_{(\mu,\varepsilon)}-\Psi_{(\mu,0)}\|_Z\le C_\Psi K|\varepsilon|$ for all $\mathfrak p\in$ (P″$_K$). Indeed, the construction of [5, App. B.1] is a contraction whose constants depend only on the linear Hypothesis 2.7 for the fixed operator $\mathcal L_*$ and on bounds for the cut-off nonlinearity and its derivatives up to order $k$ on a $Z$-ball. After the rescaling above, the nonlinearity $\mu e_{\rm iso}+(\rho-1)\mathcal D\xi+Q(\xi,\xi)+\varepsilon\mathfrak p(\xi)$ is a polynomial of degree $2$ in $\xi$ whose coefficients are bounded in terms of $|\lambda|$ alone, by $\|\mathfrak p\|_\star\le1$ and (F2). The fixed point depends Lipschitz-continuously, in $C^0$, on the nonlinearity.

With a radial and $R$-invariant cut-off, $\Psi_{(\mu,0)}$ is $SO(4)$-equivariant and $R$-reversible [5, Ch. 2, Thms. 3.13, 3.15], [31, Thm. A]. $\bar B\subset B_{\delta_0}$ is the isolating ball of [31, Thm. D], and $\operatorname{Inv}_\lambda(\bar B)$ is the maximal invariant set of $f_\lambda$ in $\bar B$.

**Function spaces and energy.** For an interval $I$, let $W(I)=H^1(I;X)\cap L^2(I;Z)$, with $\|v\|_{W(I)}^2=\|\partial_sv\|^2+\|\mathcal L_*v\|^2+\|v\|^2$, all norms in $L^2(I;X)$. Let $W_{\rm loc}=\bigcap_{I}W(I)$. A *solution* is a $\xi\in W_{\rm loc}$ satisfying (1.1) in $L^2_{\rm loc}(\mathbb R;X)$. We use the critical quantity
$$\mathfrak n(\xi):=\operatorname*{ess\,sup}_{s\in\mathbb R}\|\xi(s)\|_{L^4(S^3\times(0,\pi))},\qquad \mathcal N_\epsilon:=\{\xi\in W_{\rm loc}:\mathfrak n(\xi)<\epsilon\},$$
and the gauge-fixed energy $E(\xi)=\int_{\mathbb R}\|\partial_s\xi\|_X^2\,ds$. Under the 5D rescaling $\xi\mapsto\lambda\xi(\lambda\,\cdot)$ of a connection-type field, the norm $\sup_s\|\xi(s)\|_{L^p}$ scales by $\lambda^{1-4/p}$. It is critical exactly for $p=4$, as is $\sup_s\|\nabla\xi(s)\|_{L^2}$ (verify.py §3). Let $\mathcal T_\lambda(\epsilon)$ be the set of solutions of (1.1) in $\mathcal N_\epsilon$.

### 1.3 Results

**Theorem A (a priori estimate and isolation in the critical norm).** There are $\varepsilon_1,\lambda_1>0$, $\lambda_2\in(0,\lambda_1]$ and $C$, depending only on $\mathcal L_*$, $Q$ and $k$, such that the following hold for every $K>0$, every $\mathfrak p\in$ (P″$_K$) and every $\lambda=(\mu,\varepsilon)$ with $|\lambda|=|\mu|+K|\varepsilon|<\lambda_1$.
1. *(A priori estimate.)* Every solution with $\mathfrak n(\xi)\le\varepsilon_1$ has $\partial_s\xi\in W_{\rm loc}$ and $\xi\in C^0(\mathbb R;Z)\cap C^1(\mathbb R;X)$, and
$$\sup_{s\in\mathbb R}\|\xi(s)\|_Z\le C\big(\mathfrak n(\xi)+|\mu|+K|\varepsilon|\big).$$
2. *(Reduction.)* Every such solution has the form $\xi=z+\Psi_\lambda(z)$, where $z=P\xi$ is a complete orbit of $f_\lambda$ in $\bar B$. In particular $\xi\in C^k(\mathbb R;Z)$.
3. *(Isolation.)* Let $\eta(\lambda):=\max\{|z|:z\in\operatorname{Inv}_\lambda(\bar B)\}$ (for the given $\mathfrak p$). Then $\sup_{\mathfrak p\in(\mathrm P''_K)}\eta(\lambda)\to0$ as $|\lambda|=|\mu|+K|\varepsilon|\to0$, and in setting (U), $\eta\le C|\bar\nu|^{1/2}$. For $|\lambda|<\lambda_2$, every solution with $\mathfrak n(\xi)\le\varepsilon_1$ in fact satisfies $\sup_s\|\xi(s)\|_Z\le C(\eta(\lambda)+|\lambda|)$, hence $\mathfrak n(\xi)<\varepsilon_1/2$. The lift $z\mapsto z+\Psi_\lambda(z)$ is a bijection $\operatorname{Inv}_\lambda(\bar B)\to\mathcal T_\lambda(\varepsilon_1)$ that intertwines the reduced flow with $s$-translation. So $\mathcal N_{\varepsilon_1}$, a neighbourhood of fixed size uniformly through the fold, is an isolating neighbourhood of the set of complete PDE solutions in it.
4. *(Ends and energy; under Hypothesis (L).)* Assume:
   * **(L)** the rest points of $f_\lambda$ in $K=\operatorname{Inv}_\lambda(\bar B)$ are finitely many and hyperbolic; and
   * there is a continuous $H:K\to\mathbb R$ that is strictly increasing along every nonconstant orbit in $K$.

   (L) holds in settings (U+), (Q), (H), (E) by Lemma 6.1. Then every $\xi\in\mathcal T_\lambda(\varepsilon_1)$ converges exponentially in $Z$ to KW solutions as $s\to\pm\infty$, and $E(\xi)<\infty$. In settings (U−) and (U0), every solution in $\mathcal T_\lambda(\varepsilon_1)$ is constant [31, Thm. D(2)]. In setting (U), $E(\xi)\le C\,(H(z(+\infty))-H(z(-\infty)))$. In these settings no energy bound needs to be assumed. Hyperbolicity of rest points alone does **not** suffice, and for general $\mathfrak p\in$ (P″$_K$) item 4 is false (Remark 3.5).

**Theorem B (exponential attraction to the centre manifold).** For every $a\in(0,1)$ there are $r_a>0$ and $C_a$, depending only on $a$, $\mathcal L_*$, $Q$ and $k$, with the following property. Let $K>0$, $\mathfrak p\in$ (P″$_K$), $|\lambda|=|\mu|+K|\varepsilon|<r_a$, $T\ge2$, and let $\xi\in W([-T,T])$ solve (1.1) on $[-T,T]$ with $\sup_{|s|\le T}\|\xi(s)\|_Z\le r\le r_a$. Put $z=P\xi$ and $\eta=\Pi_h\xi-\Psi_\lambda(z)$. Then, for $|s_0|\le T-2$,
$$\|\eta\|_{W([s_0-1,s_0+1])}+\|\dot z-f_\lambda(z)\|_{L^2([s_0-1,s_0+1])}\ \le\ C_a\,r\,e^{-a(T-|s_0|)} .$$
Consequently:
* a solution on $[0,\infty)$ with $\sup\|\xi\|_Z\le r_a$ satisfies $\|\eta\|_{W([s-1,s+1])}\le C_ar\,e^{-as}$;
* a solution on $\mathbb R$ with $\sup\|\xi\|_Z\le r_a$ lies on $\mathcal M_\lambda$, which re-proves item (ii) above for (1.1).

By Theorem A(1), the hypothesis $\sup\|\xi\|_Z\le r$ may be replaced by $\mathfrak n(\xi)$ small on a slightly larger interval.

**Theorem C (local Gromov–Floer compactness).** Fix $\lambda$ in one of the settings (U±), (U0), (Q), (H), (E), with $|\lambda|<\lambda_2$, and let $(\xi_n)\subset\mathcal T_\lambda(\varepsilon_1)$ be any sequence. Here $\mathfrak p$ is fixed: in (Q) and (E) it is $-\nabla h_C$ or $-\nabla h_{\beta,e}$, and in (H) it is any $\mathfrak p$ in some (P″$_K$) satisfying the hypotheses of [32, Thm. C′]. Then a subsequence satisfies one of the following.
* **(C0) Constant case.** All $\xi_n$ are constant, $\xi_n\equiv P_n$ with $P_n$ KW solutions, and $P_n\to P$ in $Z$ for a KW solution $P$. So the images $\{P_n\}$ converge to $\{P\}$ in the Hausdorff distance, $E(\xi_n)=0$, and convergence holds in $C^k_{\rm loc}(\mathbb R;Z)$ and, for (P$_{\rm reg}$), in $C^\infty(K')$. In the settings with finitely many objects ((U+), (Q), (H), (E), (U0)), $P_n=P$ eventually. In (U−), $P_n,P\in\mathcal S_{\bar\nu}$, and $P_n$ need not be eventually constant.
* **(C1) Nonconstant case.** All $\xi_n$ are nonconstant; this occurs only in (U+), (Q) and (H). Then there are $\ell\ge1$, KW solutions $P_0\ne P_\ell$, $P_1,\dots,P_{\ell-1}$, nonconstant $u^j\in\mathcal T_\lambda(\varepsilon_1)$ from $P_{j-1}$ to $P_j$, and times $s_n^1<\dots<s_n^\ell$ with $s^{j+1}_n-s^j_n\to\infty$, such that:
1. $\xi_n(s_n^j+\cdot)\to u^j$ in $C^k_{\rm loc}(\mathbb R;Z)$ (for every $\mathfrak p\in$ (P″$_K$)). If moreover $\mathfrak p\in$ (P$_{\rm reg}$), the convergence also holds in $C^\infty(K')$ for every compact $K'\subset\mathbb R\times S^3\times(0,\pi)$. This applies in (U), (Q) and (E), and in (H) whenever the perturbation is in (P$_{\rm reg}$), e.g. $-\nabla h_{\beta,e}$ below the fold as in [33, Thm. 3(4)]. For a general (P″$_K$) perturbation in (H), interior $C^\infty$ convergence is not claimed;
2. $\xi_n(-\infty)=P_0$ and $\xi_n(+\infty)=P_\ell$ for all $n$;
3. the closures $\overline{\xi_n(\mathbb R)}$ converge in the Hausdorff distance of $Z$ to $\bigcup_j\overline{u^j(\mathbb R)}$;
4. $E(\xi_n)\to\sum_jE(u^j)$.

Every sequence has a subsequence of type (C0) or (C1), since it contains infinitely many constant or infinitely many nonconstant terms. In settings (U−), (U0) and (E), only (C0) occurs. In (U+), $\ell=1$ and $u^1$ is the AH instanton. In (Q) and (H), $1\le\ell\le\mu(P_0)-\mu(P_\ell)$.

**Theorem D (the PDE flow category and the PDE Conley index).** Let $|\lambda|<\lambda_2$.
1. *(Flow category.)* In settings (Q), (H), (E) and (U+), let $\mathcal C_{\rm PDE}$ have the following data.
   * Objects: the KW solutions in $\mathcal N_{\varepsilon_1}$.
   * Morphism spaces: the sets $\overline{\mathcal M}{}^{\rm PDE}(P,Q)$ of closures in $Z$ of broken chains of solutions in $\mathcal T_\lambda(\varepsilon_1)$ from $P$ to $Q$, with the Hausdorff metric of $Z$.
   * Composition: union.

   Then $P$ induces an isomorphism of topological flow categories $\mathcal C_{\rm PDE}\to\mathcal C_{\rm HW}$. Here $\mathcal C_{\rm HW}$ is the category of [32, 33] in settings (Q), (H), (E); in (U+) it is the reduced category of [31, Thm. D(1)], with objects $k_\pm$ and the single (obstructed) AH trajectory. Convergence in $\overline{\mathcal M}{}^{\rm PDE}$ is Gromov–Floer convergence in the sense of Theorem C. Consequently, in settings (Q), (H) and (E), [33, Thm. 1, Thm. 3(3)] and [33, Prop. 2] apply to $\mathcal C_{\rm PDE}$ verbatim. Its CJS realization, with the smooth framed structure transported from the model, is $\Sigma^\infty(S^1\vee S^4)$. Over the regular morphism spaces of (Q) and (H), its index bundles are those of the full linearized operators. No framed realization is claimed in (U+).
2. *(Conley index.)* $\mathcal S_{\rm PDE}:=\{\xi(0):\xi\in\mathcal T_\lambda(\varepsilon_1)\}$ is a compact subset of $Z$. The map $\xi(0)\mapsto\xi(s)$ defines a flow on it, and $P$ is a flow-conjugating homeomorphism onto $\operatorname{Inv}_\lambda(\bar B)$. Consider any reduction function from [5, Ch. 2, Thm. 3.3] whose restriction to $\varepsilon=0$ is $SO(4)$-equivariant and $R$-reversible. For every such choice, the Conley index of $\operatorname{Inv}_\lambda(\bar B)$ under the reduced flow is $S^1\vee S^4$, for all $|\bar\nu|<\delta$ and all small $|\varepsilon|$. In this sense the index is an invariant of the PDE invariant set $\mathcal S_{\rm PDE}$.

**Theorem E (gauge-invariant version; conditional on Hypothesis (G) of §8).** Consider the unperturbed system or a gauge-invariant perturbation ($h_C$, $h_{\beta,e}$). Let $\mathfrak d$ be the gauge-invariant critical distance of §8, and put $\varepsilon_G'=\min(\varepsilon_G,\varepsilon_1/C_G)$.
1. Under (G1)–(G2), sending a gauge class to its Coulomb representative is a well-defined injection $\Phi$ from $\{[c]:\mathfrak d(c)<\varepsilon_G'\}$ into $\mathcal T_\lambda(\varepsilon_1)\cong\operatorname{Inv}_\lambda(\bar B)$.
2. There is $\lambda_G\in(0,\lambda_2]$, depending on $\varepsilon_G'$, such that $C_S\,C(\eta(\lambda)+|\lambda|)<\varepsilon_G'$ for $|\lambda|<\lambda_G$, with $C$ and $\eta$ as in Theorem A(3). For such $\lambda$, $\Phi$ is a bijection onto $\mathcal T_\lambda(\varepsilon_1)$.
3. Give the gauge classes the quotient topology of $C^0_{\rm loc}(\mathbb R;Z)$ on configurations. Then $\Phi^{-1}$ is continuous. It is a homeomorphism under the additional continuity hypothesis (G3) of §8. Under (G3), the convergence statements of Theorem C, in the $C^0_{\rm loc}(\mathbb R;Z)$ sense, and the isomorphism of Theorem D(1) transfer to gauge classes.

In the isotropic ($SO(4)$-invariant) class, (G1)–(G3) hold trivially: the residual gauge group is $\{\pm1\}$. So there the conclusions are unconditional (Remark 8.2).

**What is new, and what is not.**
* *New.* The $\varepsilon$-regularity estimate in the critical norm (Proposition 3.2), which replaces the $Z$-ball of [31] by the weaker, scale-critical neighbourhood $\mathcal N_{\varepsilon_1}$ and proves isolation there. The quantitative exponential attraction (Theorem B). The PDE compactness theorem with energy additivity (Theorem C). The identification of the flow categories and the independence of the Conley index (Theorem D).
* *Not new, or new only in this geometry.* The Clifford (Dirac-type) structure of the gauge-fixed HW linearization and the Nahm-pole indicial roots $\pm1$ (multiplicity $8$) and $\pm2$ (multiplicity $4$) are in rStation math_14 [34, Thms. A–B], for a flat half-space model. Essential self-adjointness with domain $H^1_0$ for the pure Nahm-pole model on $\mathbb R^k\times(0,\infty)$ is math_16 [35, Thm. 1]. Lemmas 2.1–2.2 transfer these facts to the present two-ended spherical geometry $S^3\times(0,\pi)$. That geometry has two Nahm poles, a curved left-invariant frame, the extra zeroth-order term $V_0'$, and the fold background of [31]. The transfer is by an exact computation from the full gauge-fixed field and a two-sided Hardy argument. We claim novelty only for this transfer and its constants. The techniques are standard: absorption with a small critical norm (Uhlenbeck [9]); weighted energy estimates for exponential dichotomies of ill-posed elliptic problems (Kirchgässner [13], Mielke [12], Peterhof–Sandstede–Scheel [14]); and compactness up to breaking for gradient-like flows [18, Thm. 3.2.2], [19, Thm. 3.8]. The finite-dimensional dynamics is that of [31, 32, 33].
* *Not claimed.* Hypothesis (G) in general. Interior $C^\infty$ convergence for perturbations outside (P$_{\rm reg}$). Regularity at the Nahm pole beyond $H^1_0$ for the 5D flow; polyhomogeneity is known for static KW solutions [6, Prop. 5.9] and expansions for HW are studied in [26], but we neither prove it for (1.1) nor check that [26] applies to our solution class. Compactness of trajectories that leave $\mathcal N_{\varepsilon_1}$. Any global statement.

## 2. The natural norm at the Nahm pole

**Lemma 2.1 ($Z=H^1_0$).** $Z=H^1_0(S^3\times(0,\pi);\mathbb R^{24})$, with
$$c\,\|u\|_{H^1}\le\|u\|_Z\le C\,\|u\|_{H^1},\qquad \|u/\sin y\|_X\le\pi\,\|\partial_yu\|_X\quad(u\in H^1_0),$$
and $\mathcal L_*$ is essentially self-adjoint on $C^\infty_c(S^3\times(0,\pi))$. Thus $\|\cdot\|_Z$ is the Hardy-weighted $H^1$ norm, $\|\nabla u\|+\|u/\sin y\|$, and $\mathcal N_\epsilon$ and the $Z$-balls are natural in the Nahm-pole sense: they consist of deformations that vanish at $y=0,\pi$.

*Proof.* By (F2), $u\in Z$ implies $u\in H^1$ and $u/\sin y\in L^2$. For a.e. $q\in S^3$, $u(q,\cdot)$ is absolutely continuous, and $\int|u(q,y)|^2\sin^{-2}y\,dy<\infty$ forces $u(q,0)=u(q,\pi)=0$. So the trace of $u$ vanishes, and $u\in H^1_0$. Conversely, write $\mathcal L_*=\Gamma_y\partial_y+\sum_i\Gamma_iE_i+V_0'+\cot y\,V_1$ with constant matrices (Lemma 2.2), and note $\|V_1\|=\|\Gamma_yV_1\|=2$. For $u\in C^\infty_c$, the Hardy inequality on each half-interval, $\int_0^{a}u^2/y^2\le4\int_0^au'^2$ when $u(0)=0$, combines with Jordan's inequality $\sin y\ge\tfrac2\pi\min(y,\pi-y)$ to give $\|u/\sin y\|\le\pi\|\partial_yu\|$. Hence $\|\mathcal L_*u\|\le C\|u\|_{H^1}$. So the closure of $C^\infty_c$ in the graph norm, which is $\operatorname{dom}\mathcal L_{\min}$, contains $H^1_0$. Since $\mathcal L_*$ is a self-adjoint realization, $\mathcal L_{\min}\subset\mathcal L_*\subset\mathcal L_{\max}$, so $H^1_0\subset\operatorname{dom}\mathcal L_{\min}\subset Z\subset H^1_0$. All inclusions are therefore equalities, and the norms are equivalent by the closed graph theorem. Equality of $\operatorname{dom}\mathcal L_{\min}$ with the self-adjoint domain is essential self-adjointness. The Hardy and Jordan steps are checked in verify.py §2, with a control. ∎

**Lemma 2.2 (Dirac type and indicial roots; exact).** In the left-invariant frame, $\mathcal L_*=\Gamma_y\partial_y+\sum_{i=1}^3\Gamma_iE_i+V_0'+\cot y\,V_1$, with constant $24\times24$ matrices, and:
1. $\Gamma_a^{\sf T}=-\Gamma_a$ and $\Gamma_a\Gamma_b+\Gamma_b\Gamma_a=-2\delta_{ab}$ for $a,b\in\{y,1,2,3\}$. Hence $\mathcal L_*$ is a Dirac-type operator, and $\mathcal L_*^2$ is Laplace-type. The 5D symbol of $\partial_s-\mathcal L_*$ satisfies $(\sigma-\Gamma(\eta))(\sigma+\Gamma(\eta))=(\sigma^2+|\eta|^2)I$, so $\partial_s-\mathcal L_*$ is elliptic in the interior of $\mathbb R\times S^3\times(0,\pi)$, and $(-\partial_s-\mathcal L_*)(\partial_s-\mathcal L_*)=-\partial_s^2+\mathcal L_*^2$ is Laplace-type.
2. $V_1$ is symmetric and anticommutes with $\Gamma_y$. The indicial matrix $B=\Gamma_yV_1$, for which $\mathcal L_*u=0$ reads $u'=\cot y\,Bu+\dots$, is symmetric with characteristic polynomial $(\lambda-2)^4(\lambda-1)^8(\lambda+1)^8(\lambda+2)^4$.

So the indicial roots are $\pm1,\pm2$, and none lies in $(-1,1)$. This agrees with Mazzeo–Witten's roots $\{-1,2\}$ and $\{1,-2\}$ for the principal $\mathfrak{su}(2)$ Nahm pole [6, eqs. (2.41)–(2.42)], and with their weight range $(-1,1)$ [6, Prop. 5.2]. The $L^2$-admissible roots $1,2$ span exactly half of $\mathbb R^{24}$ (multiplicity $12$), and the corresponding modes $y,y^2$ lie in $H^1_0$.

*Proof.* We compute directly from the gauge-fixed field $F$ of [31] (verify.py §1–2). $\Gamma_y$ is the commutator $[\mathcal L_*,y]$. $\Gamma_i$ is $[\mathcal L_*,x_i]$ at $q=1$, where $E_jx_i=\delta_{ij}$; it is constant by left invariance. $V_1$ is the coefficient of $\cot y$. Skewness, the Clifford relations, symmetry of $V_1$, the anticommutation and the characteristic polynomial are all exact rational identities. As a control, deleting the Coulomb rows destroys the Clifford relation. ∎

*Remark 2.3 (relation to math_14 and math_16).* Lemma 2.2 is the spherical, two-ended analogue of [34, Thm. A] (Clifford structure) and [34, Thm. B] (roots $\pm1$ with multiplicity $8$ and $\pm2$ with multiplicity $4$). The multiplicities agree. Lemma 2.1 is the analogue of [35, Thm. 1(1)], $D(\bar L_{\rm NP})=H^1_0$, which is proved there on the half-space $\mathbb R^k\times(0,\infty)$ with one Nahm pole. Here both ends $y=0,\pi$ are Nahm poles, $S^3$ is compact and curved, and the domain statement is combined with the spectral gap of [30]. Lemma 2.2(2) is also the precise form of the "half-dimensional admissible indicial space" used for the limit-point property in [30, Prop. 4.2], following its referee. Lemma 2.2(1) is what makes interior elliptic regularity for (1.1) available (Lemma 6.2).

## 3. The a priori estimate in the critical norm (proof of Theorem A)

**Lemma 3.1 (energy identity).** For $v\in W(\mathbb R)$, $\|(\partial_s-\mathcal L_*)v\|^2=\|\partial_sv\|^2+\|\mathcal L_*v\|^2$. The same holds with $\mathcal L_h=\Pi_h\mathcal L_*$ on $\Pi_hX$.

*Proof.* For compactly supported smooth $v$, the cross term is $-2\int\langle\partial_sv,\mathcal L_*v\rangle\,ds=-\int\partial_s\langle v,\mathcal L_*v\rangle\,ds=0$, by self-adjointness. Both sides are continuous on $W(\mathbb R)$, in which such $v$ are dense. A finite-dimensional exact check, with a non-symmetric control, is in verify.py §4. ∎

**Proposition 3.2 ($\varepsilon$-regularity).** Let $K>0$ and $\mathfrak p\in$ (P″$_K$). Put
$$\varepsilon_{3.2}:=\big(8\sqrt2\,C_QC_SC_Z\big)^{-1},\qquad \sigma_{3.2}:=\big(8\sqrt2\,C_Z(1+C_S)\big)^{-1},$$
and assume
$$\varepsilon_1\le\min(\varepsilon_{3.2},\tfrac12),\qquad |\mu|\le\tfrac18,\qquad K|\varepsilon|\le\sigma_{3.2}. \tag{3.0}$$
If $\xi\in W_{\rm loc}$ solves (1.1) with $\mathfrak n(\xi)\le\varepsilon_1$, then $\partial_s\xi\in W_{\rm loc}$ and, for every $m\in\mathbb R$,
$$\|\xi\|_{H^1([m-1,m+1];Z)}\le C\Big(\|\xi\|_{L^2([m-6,m+6];X)}+|\mu|+K|\varepsilon|\Big), \tag{3.1}$$
with $C$ depending only on $C_Z$, $C_S$, $C_Q$ and $\|e_{\rm iso}\|_X$, not on $K$ or $\mathfrak p$. In the difference-quotient step, $\varepsilon_1$ is replaced by $2\varepsilon_1$; the factor $8$ in $\varepsilon_{3.2}$ accounts for this. Here $C_Z$ is the constant in $\|u\|_Z\le C_Z(\|\mathcal L_*u\|+\|u\|)$, and $C_Q,C_S$ are those of §1.2 and Lemma 2.1.

*Proof.* *Step 1.* Let $\chi\in C^\infty_c((m-3,m+3))$ with $\chi=1$ on $[m-2,m+2]$, and let $A=\|\chi\xi\|_{W(\mathbb R)}<\infty$. By Lemma 3.1, $A\le\|(\partial_s-\mathcal L_*)(\chi\xi)\|+\|\chi\xi\|$. Moreover
$$(\partial_s-\mathcal L_*)(\chi\xi)=\chi'\xi+\chi\big[\mu e_{\rm iso}+(\rho-1)\mathcal D\xi+Q(\xi,\xi)+\varepsilon(f+M\xi+B(\xi,\xi))\big].$$
We estimate each term, using $\|u\|_Z\le C_Z(\|\mathcal L_*u\|+\|u\|)$ and $\|\mathcal L_*v\|+\|v\|\le\sqrt2A$:
* $\|\chi(\rho-1)\mathcal D\xi\|\le|\mu|\,\|\mathcal L_*\chi\xi\|\le|\mu|A$, since $|\rho-1|\le|\mu|$;
* pointwise $|Q(a,b)|\le C_Q|a||b|$ (verify.py §3), so by Hölder ($\tfrac12=\tfrac14+\tfrac14$) and (F2),
$$\|\chi Q(\xi,\xi)\|_{L^2(\mathbb R;X)}\le C_Q\,\mathfrak n(\xi)\,\|\chi\xi\|_{L^2(\mathbb R;L^4)}\le\sqrt2\,C_QC_SC_Z\,\varepsilon_1A;$$
* in the same way, $\|\varepsilon\chi(M\xi+B(\xi,\xi))\|\le\sqrt2\,C_Z|\varepsilon|(\|M\|+C_BC_S\varepsilon_1)A\le\sqrt2\,C_Z(1+C_S)K|\varepsilon|\,A$, using $\|M\|,C_B\le K$ and $2\varepsilon_1\le1$;
* the constant terms are bounded by $\sqrt6(|\mu|\|e_{\rm iso}\|+|\varepsilon|\|f\|)\le\sqrt6(\|e_{\rm iso}\|+1)(|\mu|+K|\varepsilon|)$.

Under (3.0), even with $\varepsilon_1$ replaced by $2\varepsilon_1$ as in Step 2, the coefficient of $A$ on the right is at most $\tfrac18+\tfrac14+\tfrac18=\tfrac12$. Hence
$$\|\xi\|_{W([m-2,m+2])}\le A\le 2(\|\chi'\|_\infty+1)\|\xi\|_{L^2([m-3,m+3];X)}+C(|\mu|+K|\varepsilon|).$$

*Step 2 (one more $s$-derivative).* For $0<|h|\le1$, the difference quotient $v_h=(\xi(\cdot+h)-\xi)/h$ lies in $W_{\rm loc}$. By $Q(a,a)-Q(b,b)=Q(a+b,a-b)$ (verify.py §3) and the analogous identity $B(a,a)-B(b,b)=B(a,a-b)+B(a-b,b)$, it satisfies
$$(\partial_s-\mathcal L_*)v_h=(\rho-1)\mathcal Dv_h+Q(\xi_h+\xi,v_h)+\varepsilon\big(Mv_h+B(\xi_h,v_h)+B(v_h,\xi)\big),\qquad\xi_h=\xi(\cdot+h).$$
Step 1, with $\mathfrak n(\xi_h+\xi)\le2\varepsilon_1$ and without constant terms, gives
$$\|v_h\|_{W([m-1,m+1])}\le C\|v_h\|_{L^2([m-2,m+2];X)}\le C\|\partial_s\xi\|_{L^2([m-3,m+3];X)},$$
uniformly in $h$. A weakly convergent subsequence in the Hilbert space $W([m-1,m+1])$ has limit $\partial_s\xi$. So $\partial_s\xi\in W_{\rm loc}$, and by Step 1 its norm is bounded by the right side of (3.1). Since $\xi,\partial_s\xi\in L^2_{\rm loc}(Z)$, we get $\xi\in H^1_{\rm loc}(\mathbb R;Z)$, which is (3.1). ∎

*Proof of Theorem A.*
1. $H^1([m-1,m+1];Z)\hookrightarrow C^0([m-1,m+1];Z)$. Also $\|\xi\|_{L^2([m-6,m+6];X)}\le\sqrt{12}\,(2\pi^3)^{1/4}\mathfrak n(\xi)$, by Hölder and $\operatorname{vol}(S^3\times(0,\pi))=2\pi^3$ (verify.py §3). Together with (3.1) this gives item 1. Moreover $\partial_s\xi\in W_{\rm loc}\subset C^0(X)$.
2. Shrinking $\varepsilon_1,\lambda_1$ (in terms of $C$, $r_{\mathcal O}$ and $\operatorname{rad}\bar B$ only, all independent of $\mathfrak p$ by (v)), item 1 gives $\sup_s\|\xi(s)\|_Z<r_{\mathcal O}$ and $|P\xi(s)|<\operatorname{rad}\bar B$. By (ii), $\xi$ lies on $\mathcal M_\lambda$, so $\xi=z+\Psi_\lambda(z)$ with $z=P\xi$ a complete reduced orbit in $\bar B$. Since $f_\lambda\in C^k$, $z\in C^{k+1}$, and therefore $\xi\in C^k(\mathbb R;Z)$.
3. *Isolation radius.* Suppose $|\lambda_n|=|\mu_n|+K|\varepsilon_n|\to0$, $\mathfrak p_n\in$ (P″$_K$), and $z_n\in\operatorname{Inv}_{\lambda_n,\mathfrak p_n}(\bar B)$ with $|z_n|\ge\eta_0>0$. The reduced fields $f_{\lambda_n,\mathfrak p_n}\to f_0$ uniformly on $\bar B$. This holds because $f_{(\mu_n,0)}\to f_0$ by joint continuity of the $\mathfrak p$-independent unperturbed reduction, and $\|f_{\lambda_n,\mathfrak p_n}-f_{(\mu_n,0)}\|_{C^0(\bar B)}\le C(K|\varepsilon_n|)$ by (v), since $f=PF_\lambda(z+\Psi_\lambda(z))$. The complete orbits through $z_n$ are equicontinuous, so a subsequence converges locally uniformly to a complete $f_0$-orbit in $\bar B$ through a point of norm $\ge\eta_0$. This contradicts $\operatorname{Inv}_0(\bar B)=\{0\}$ [31, Thm. D(3)]. In setting (U), $\operatorname{Inv}$ consists of $k_\pm$ ($x^2=\tfrac85\bar\nu$) and the AH segment for $\bar\nu>0$, of $\mathcal S_{\bar\nu}$ ($|w|^2=\tfrac{32}{15}|\bar\nu|$) for $\bar\nu<0$, and of $\{0\}$ at $\bar\nu=0$, up to higher order [31, Thms. C–D] (verify.py §5). So $\eta\le C|\bar\nu|^{1/2}$. For $\xi=z+\Psi_\lambda(z)$ with $z\in\operatorname{Inv}$, $\|\xi(s)\|_Z\le C|z(s)|+\|\Psi_\lambda(z(s))\|_Z\le C(\eta(\lambda)+|\lambda|)$, because $\Psi_\lambda(0)=O(|\lambda|)$ and $D\Psi=O(|z|+|\lambda|)$, uniformly in $\mathfrak p$ by (v). Hence $\mathfrak n(\xi)\le C_S\,C(\eta+|\lambda|)<\varepsilon_1/2$ for $|\lambda|<\lambda_2$. Conversely, by (iv), each orbit in $\operatorname{Inv}_\lambda(\bar B)$ lifts to a solution, and this solution lies in $\mathcal N_{\varepsilon_1/2}$ by the same bound. The lift is injective because $P$ inverts it, and it intertwines the flows.
4. By (L) and Lemma 5.1(1), every orbit in $K$ has single rest points as $\alpha$- and $\omega$-limits. Since these rest points are hyperbolic, the orbit converges to them at an exponential rate (Lemma 5.2), and the lift is $C^k$, so $\xi(s)$ converges exponentially in $Z$. We have $\partial_s\xi=(I+D\Psi_\lambda(z))\dot z$, so $E(\xi)\le C\int|f_\lambda(z)|^2$, which is finite by the exponential convergence. In setting (U), [31, Prop. 6.2] gives $\dot H=f_x^2+x^2|w|^2m$ with $m\ge1$, while $|f_w|^2=x^2|w|^2\tilde h^2$ with $\tilde h^2\le2$ on $\bar B$ (at the origin, $m=\tilde h^2=\tfrac{25}{16}$; verify.py §5). Hence $|f|^2\le2\dot H$, and $E(\xi)\le C\,(H(z(+\infty))-H(z(-\infty)))$. In (U−) and (U0) all solutions are constant. ∎

*Remark 3.3 (why the critical norm).* The estimate cannot be run with $\sup_s\|\xi(s)\|_{L^2}$ in place of $\mathfrak n$. That norm scales by $\lambda^{-1}$, so it does not see concentration at small scales (verify.py §3). Nor can it be run with the 5D $H^1$ norm: in 5D, $H^1\hookrightarrow L^{10/3}$ only, which does not control $Q$ in $L^2$ (verify.py §3, control). The slice norm $L^\infty_sL^4_x$ is the weakest Lebesgue-type norm that is critical and controls $Q$. This is the reason why only *local* compactness is accessible by these methods. Global compactness in 5D has to face energy concentration along codimension-four sets, as for higher-dimensional Yang–Mills [10]. It also needs an $\varepsilon$-regularity theorem from small energy with Nahm poles, which is available for KW in 4D [8] but not for HW in 5D.

*Remark 3.4 (solution class).* $W_{\rm loc}$ requires the deformation to vanish at the Nahm pole in the $H^1_0$ sense (Lemma 2.1). For static KW solutions satisfying the Nahm-pole boundary condition, polyhomogeneity [6, Prop. 5.9] and Lemma 2.2 show that the leading exponent is $\ge1$, which gives membership in $H^1_0$ locally. For the 5D flow we take $W_{\rm loc}$ as the definition of the solution class; expansions of HW solutions at (twisted) Nahm poles are analysed in [26], which suggests that this class contains all solutions with the Nahm-pole boundary condition, but we do not prove this.

*Remark 3.5 (Hypothesis (L) cannot be dropped; as pointed out by the referee).* Let $R_\theta$ be a circle subgroup of $SU(2)_L$ acting by left translations; on $\mathcal K\cong\mathbb H$ it acts by left multiplication by $e^{i\theta}$. Let $A$ be its infinitesimal generator on deformation fields: componentwise differentiation along a right-invariant field $R_1$. Then $A$ is a first-order operator with smooth coefficients, bounded $Z\to X$, so $\mathfrak p(\xi)=A\xi$ lies in (P″$_K$)$\,\cap\,$(P$_{\rm reg}$) for a fixed $K$. The background is invariant, and $F_\mu$ is $SU(2)_L$-equivariant [31, (H4)] (verify.py §11). For $\bar\nu<0$ small and $\xi_*\in\mathcal S_{\bar\nu}$, the curve $\xi(s)=R_{\varepsilon s}\xi_*$ satisfies $F_\mu(\xi(s))=0$ and $\partial_s\xi=\varepsilon A\xi$, so it is an exact solution of (1.1). It is nonconstant and periodic, because the circle acts freely on $\mathcal K\setminus\{0\}$ (verify.py §11). It has $\mathfrak n(\xi)=\mathfrak n(\xi_*)=O(|\bar\nu|^{1/2})$ and $E(\xi)=\infty$, since $\|\partial_s\xi\|_X=|\varepsilon|\|A\xi_*\|_X>0$ is constant. Undoing the rotation, every small complete perturbed solution corresponds to a complete unperturbed one, which is constant on $\mathcal S_{\bar\nu}$ [31, Thm. D(2)]. So this local invariant set contains no perturbed rest points at all, and "all rest points are hyperbolic" holds vacuously while the conclusion fails. Theorem A(1)–(3) and Theorem B are unaffected. Theorem C is stated only in settings where (L) holds.

## 4. Exponential attraction (proof of Theorem B)

Let $\xi$ be as in Theorem B, and write $\xi_M=z+\Psi_\lambda(z)$, so that $\xi=\xi_M+\eta$. Since $\Psi\in C^1(B_{\delta_0};Z)$ and $z\in H^1$, $\eta\in W([-T,T])$ with values in $Z_h=Z\cap\Pi_hX$. Using the invariance identity (iii) to cancel the $\eta$-independent terms, $\eta$ satisfies
$$\partial_s\eta=\mathcal L_h\eta+G,\qquad G=\Pi_h\big[F_\lambda(\xi_M+\eta)-F_\lambda(\xi_M)-\mathcal L_*\eta\big]-D\Psi_\lambda(z)\,P\big[F_\lambda(\xi_M+\eta)-F_\lambda(\xi_M)\big].$$
Since $P\mathcal L_*\eta=0$, the bracket consists of the terms $(\rho-1)\mathcal D\eta$, $2Q(\xi_M,\eta)+Q(\eta,\eta)$ and $\varepsilon(M\eta+B(\xi_M,\eta)+B(\eta,\xi_M)+B(\eta,\eta))$. By (F2) and the pointwise bound on $Q$,
$$\|G(s)\|_X\le\theta\,\|\eta(s)\|_Z,\qquad\theta=C(r+|\lambda|), \tag{4.1}$$
because $\|\xi_M\|_Z,\|\eta\|_Z\le Cr$ and $\|D\Psi_\lambda(z)\|\le C(|z|+|\lambda|)$. Here $|\lambda|=|\mu|+K|\varepsilon|$, the $\varepsilon$-terms contribute at most $C_SK|\varepsilon|$, and $C$ is independent of $\mathfrak p\in$ (P″$_K$) by (v).

*Weighted estimate.* Fix $|s_0|\le T-2$. Let $\omega(s)=\operatorname{sech}(a(s-s_0))$, so that $|\omega'|\le a\omega$ and $e^{-|x|}\le\operatorname{sech}x\le2e^{-|x|}$ (verify.py §4). Let $\chi\in C^\infty_c((-T,T))$ with $\chi=1$ on $[-T+1,T-1]$ and $|\chi'|\le2$, and put $u=\omega\chi\eta\in W(\mathbb R;Z_h)$. Then
$$(\partial_s-\mathcal L_h)u=\omega'\chi\eta+\omega\chi'\eta+\omega\chi G .$$
By Lemma 3.1, $\|(\partial_s-\mathcal L_h)u\|\ge\|\mathcal L_hu\|$, and by (F1), $\|\mathcal L_hu\|\ge\|u\|$. So
* $\|\omega'\chi\eta\|\le a\|\mathcal L_hu\|$;
* $\|\omega\chi G\|\le\theta\|u\|_{L^2Z}\le2C_Z\theta\|\mathcal L_hu\|$, by (4.1).

Hence
$$(1-a-2C_Z\theta)\,\|\mathcal L_hu\|\le\|\omega\chi'\eta\|\le2\cdot2e^{-a(T-1-|s_0|)}\cdot\sqrt2\,Cr .$$
Choose $r_a$ so that $1-a-2C_Z\theta\ge\tfrac12(1-a)$ (verify.py §4). On $[s_0-1,s_0+1]\subset[-T+1,T-1]$ we have $\chi=1$ and $\omega\ge\operatorname{sech}a$. So $\|\eta\|_{L^2([s_0-1,s_0+1];Z)}\le C_are^{-a(T-|s_0|)}$. Also $\|u'\|\le\|(\partial_s-\mathcal L_h)u\|$, and $\omega\eta'=u'-\omega'\eta$ on the window, which bounds $\|\partial_s\eta\|$ in the same way.

Finally, $\dot z=PF_\lambda(\xi)=f_\lambda(z)+P[F_\lambda(\xi_M+\eta)-F_\lambda(\xi_M)]$, and the last term is bounded in $X$ by $C\|\eta\|_Z$. This gives the estimate for $\dot z-f_\lambda(z)$.

*Corollaries.* For a half-line, apply the estimate on $[0,2s]$ with $s_0=s$. For a solution on $\mathbb R$, let $T\to\infty$ with $s_0$ fixed; then $\eta\equiv0$. ∎

*Remark 4.1.* Theorem B is the local input for any future neck analysis. A long piece of a trajectory that stays near the fold is, up to $O(e^{-a\cdot\text{distance to the ends}})$, a reduced orbit of the five-dimensional field. The rate $a<1$ is the spectral gap of $\mathcal L_*$ in the units $s$, i.e. $a\pi<\pi$ in the normalized time $t=s/\pi$. A numerical illustration on a toy saddle–centre system shows the rate (verify.py §9; not used in the proofs).

## 5. Finite-dimensional compactness

**Lemma 5.1 (compactness up to breaking).** Let $f\in C^1(\bar B;\mathbb R^d)$, where $\bar B$ is a closed ball, and let $K=\operatorname{Inv}(\bar B)\subset\operatorname{int}\bar B$. Assume:
* the rest-point set $\mathcal E\subset K$ is finite;
* there is a continuous $H:K\to\mathbb R$ that is strictly increasing along every nonconstant orbit in $K$.

Then:
1. Every orbit in $K$ has single rest points as $\alpha$- and $\omega$-limits.
2. Every sequence $(z_n)$ of complete orbits in $K$ has a subsequence with the following properties. There are $\ell\le\#\mathcal E-1$, rest points $p_0,\dots,p_\ell$, nonconstant orbits $u^j$ from $p_{j-1}$ to $p_j$, and times $s_n^j$ with $s_n^{j+1}-s_n^j\to\infty$, such that $z_n(s_n^j+\cdot)\to u^j$ in $C^1_{\rm loc}$, $z_n(\mp\infty)=p_0,p_\ell$, and $\overline{z_n(\mathbb R)}\to\bigcup_j\overline{u^j(\mathbb R)}$ in the Hausdorff distance.
3. Suppose in addition that every $p\in\mathcal E$ is hyperbolic, and let $\mathfrak e\ge0$ be continuous on $\bar B$ with $\mathfrak e\le C|f|^2$. Then $\int\mathfrak e(z_n)\to\sum_j\int\mathfrak e(u^j)$.

Versions of 1–2 for Morse–Smale gradient flows on closed manifolds are classical [18, Prop. 2.1.6, Thm. 3.2.2], [19, Def. 3.7, Thm. 3.8], [20]. We need them for an arbitrary isolated invariant set with a continuous Lyapunov function, so we give the short proof.

*Proof.*
1. The limit sets are nonempty, compact, connected and invariant. $H$ is constant on each of them, so by strictness they consist of rest points. Since $\mathcal E$ is finite and the limit sets are connected, each is a single point.
2. *Excursions are short.* Fix $\rho>0$ so small that the closed balls $V_p=\bar B_\rho(p)$, $p\in\mathcal E$, are disjoint, and let $U=\bigcup_p\operatorname{int}V_p$. The quantity $H(\phi_1z)-H(z)$ is continuous and positive on the compact set $K\setminus U$, so it is $\ge c>0$ there. $H$ is monotone with total range at most $\operatorname{osc}_KH$. Choose times greedily, $t_{i+1}=\inf\{t\ge t_i+1:z(t)\notin U\}$. Then $H(z(t_{i+1}))\ge H(z(t_i))+c$, so there are at most $N_0=\lfloor\operatorname{osc}_KH/c\rfloor+1$ such times. Hence every orbit is outside $U$ only within at most $N_0$ intervals $[t_i,t_i+1]$.

   *Clusters and pieces.* Pass to a subsequence along which:
   * $z_n(\mp\infty)=p,q$ are fixed;
   * the number of such intervals is fixed;
   * the gaps between consecutive intervals either converge or tend to $\infty$.

   Group intervals with bounded gaps into clusters, and let $s_n^j$ be the left end of the $j$-th cluster. Between clusters the orbit stays in $U$, hence in a single ball $V_{p_j}$, since $U$ is a disjoint union. Before the first cluster it stays in $V_p$, and after the last in $V_q$. By Arzelà–Ascoli and continuous dependence, $z_n(s_n^j+\cdot)\to u^j$ in $C^1_{\rm loc}$, with $u^j$ a complete orbit in $K$ and $u^j(0)\notin U$. So $u^j$ is nonconstant. Since the gaps tend to $\infty$, $u^j(t)\in V_{p_j}$ for all large $t$ and $u^j(t)\in V_{p_{j-1}}$ for all very negative $t$. Hence $\omega(u^j)=p_j$ and $\alpha(u^j)=p_{j-1}$. $H$ strictly increases along the chain $p=p_0,\dots,p_\ell=q$, so $\ell\le\#\mathcal E-1$.

   *Independence of $\rho$ and Hausdorff convergence.* Each $\{p\}$ is an isolated invariant set: a complete orbit in $V_p$ has both limits equal to $p$, so it is constant by strictness. Fix $\rho_0$ for which $V_p(\rho_0)$ contains no nonconstant complete orbit, and let $\rho'<\rho\le\rho_0$. Every piece obtained with $\rho'$ is a nonconstant orbit, so it leaves the $\rho_0$-balls, and hence is a translate of a piece obtained with $\rho$, and conversely. The decomposition is therefore independent of $\rho\le\rho_0$. The Hausdorff distance between $\overline{z_n(\mathbb R)}$ and $\bigcup\overline{u^j}$ is at most $2\rho+o(1)$ for every such $\rho$.
3. By Lemma 5.2 below, on a gap $[\alpha_n,\beta_n]$ inside $V_{p}$ we have $|f(z_n)|\le C|z_n-p|\le C\rho(e^{-\lambda'(t-\alpha_n)}+e^{-\lambda'(\beta_n-t)})$. So the gaps contribute at most $C\rho^2/\lambda'$. The tails $\int_{|t|>R}\mathfrak e(u^j)$ are small for large $R$, by the same lemma. On the windows $[s_n^j-R,s_n^j+R]$ the convergence is uniform. An $\epsilon/3$ argument gives the claim. ∎

**Lemma 5.2 (neck estimate).** Let $p$ be a hyperbolic rest point of a $C^1$ field, with $\lambda>0$ smaller than the absolute values of the real parts of the eigenvalues. There are $\rho,C$ and $\lambda'\in(0,\lambda)$ such that every orbit segment $z:[\alpha,\beta]\to\bar B_\rho(p)$ satisfies
$$|z(t)-p|\le C\rho\,\big(e^{-\lambda'(t-\alpha)}+e^{-\lambda'(\beta-t)}\big).$$

*Proof.* Choose adapted inner products on the unstable and stable subspaces in which $\langle A_ux,x\rangle\ge\lambda|x|^2$ and $\langle A_sx,x\rangle\le-\lambda|x|^2$. They exist: if $\operatorname{Re}\sigma(A_u)>\lambda$, then $P=\int_0^\infty e^{-(A_u-\lambda)^{\sf T}t}e^{-(A_u-\lambda)t}dt$ solves $(A_u-\lambda)^{\sf T}P+P(A_u-\lambda)=I$, so $\langle A_ux,x\rangle_P=\lambda|x|_P^2+\tfrac12|x|^2\ge\lambda|x|_P^2$; similarly for $-A_s$. Write $z-p=(x_u,x_s)$, $a=|x_u|$, $b=|x_s|$, and $f(p+x)=Ax+g(x)$ with $|g(x)|\le\kappa|x|$ on $\bar B_\rho$, where $\kappa\to0$ as $\rho\to0$. Then
$$\tfrac12\tfrac{d}{dt}(a^2-b^2)\ge\lambda(a^2+b^2)-\kappa(a+b)^2\ge(\lambda-2\kappa)(a^2+b^2)$$
(verify.py §6). So $a^2-b^2$ is increasing. Let $t_*$ be its zero, or an endpoint if it has none. On $t\ge t_*$, $a\ge b$ and $\tfrac{d}{dt}a^2\ge2(\lambda-2\kappa)a^2$, so $|z-p|^2\le2a^2\le2\rho^2e^{-2\lambda'(\beta-t)}$. On $t\le t_*$ the same argument applies to $b^2$, giving $|z-p|^2\le2\rho^2e^{-2\lambda'(t-\alpha)}$. Here $\lambda'=\lambda-2\kappa$. The estimate is sharp for the linear saddle (verify.py §6). ∎

*Model check.* For the quadrupole Rayleigh flow on $S^3$ with $C=\operatorname{diag}(0,1,2,3)$, the orbits $\theta(t)=e^{-Ct}c/|e^{-Ct}c|$ with $c=(0,\epsilon,1,\epsilon)$ run from $e_3$ to $e_1$. As $\epsilon\to0$:
* their translates by $\mp\log(1/\epsilon)$ converge exactly to the orbits $e_3\to e_2$ and $e_2\to e_1$;
* the neck at $t=\tfrac12\log(1/\epsilon)$ converges to $e_2$.

This illustrates Lemma 5.1 in the model of [33, Thm. 1] (verify.py §6).

## 6. Proof of Theorem C

**Lemma 6.1 (the hypotheses of Lemma 5.1 hold).** Let $K=\operatorname{Inv}_\lambda(\bar B)$.
* (U+): $\mathcal E=\{k_\pm\}$, which are hyperbolic, with eigenvalues $\tfrac53x_\pm$ and $-\tfrac54x_\pm$ to leading order. $K$ is the AH segment, and $H$ is the Lyapunov function of [31, Prop. 6.2].
* (Q) and (H): $\mathcal E$ is the set of objects of [32, Thm. C, C′], which are nondegenerate, so all five small eigenvalues are nonzero. All complete orbits in $K$ lie on the invariant sphere $\mathcal S_{\bar\nu,\varepsilon}$ [32, Thm. C2]. There is a homeomorphism $\eta_1:\mathcal S_{\bar\nu,\varepsilon}\to S^3$ mapping oriented orbits onto oriented orbits of $-\nabla\varphi$, where $\varphi=\varphi_C$ in (Q) and $\varphi=\varphi_e$ in (H) [32, Thm. C2], [33, §4]. Then $H=-\varphi\circ\eta_1$ is continuous and strictly increasing along nonconstant orbits.
* (E): $K=\{k_+,k_-\}$ [33, Thm. 3(3)], so all orbits are constant.
* (U−), (U0): every orbit in $K$ is constant [31, Thm. D(2)]. Here $K=\mathcal S_{\bar\nu}$ or $\{0\}$.

*Proof.* These are the cited statements. ∎

**Lemma 6.2 (interior regularity).** Assume $\mathfrak p\in$ (P″$_K$)$\,\cap\,$(P$_{\rm reg}$), as for $-\nabla h_C$ and $-\nabla h_{\beta,e}$. Assume also (shrinking $\varepsilon_1$, $\lambda_1$ if necessary, by amounts independent of $\mathfrak p$)
$$\varepsilon_1\le\varepsilon_{\rm reg}:=\big(16\sqrt2\,C_NC_S\big)^{-1},\qquad \sqrt2\,C_0|\lambda|\le\tfrac12, \tag{6.1}$$
where $C_N:=C_Q+1$, which bounds $|Q(a,b)|+|\varepsilon B(a,b)|\le C_N|a||b|$ because $|\varepsilon|C_B\le K|\varepsilon|\le|\lambda|\le1$, $C_S$ is the constant of (F2) in $\|v\|_{L^4}\le C_S\|v\|_{H^1}$ on $H^1_0$, and $C_0$ is a global bound $\|(\rho-1)\mathcal Dv\|+|\varepsilon|\|Mv\|\le C_0(|\mu|+K|\varepsilon|)\,\|v\|_{H^1}$ on $H^1_0$ (Lemma 2.1 and $\|M\|_{Z\to X}\le K$). Here $C_0$ depends only on $\mathcal L_*$. Thus (6.1) involves only $\mathcal L_*$, $Q$ and $|\lambda|$. Then every $\xi\in\mathcal T_\lambda(\varepsilon_1)$ is $C^\infty$ on $\mathbb R\times S^3\times(0,\pi)$. Quantitatively, fix $y_0\in(0,\tfrac\pi2)$, $s_*\in\mathbb R$, and the nested interior sets
$$\Omega^{(j)}=\{|s-s_*|<1+2^{-j}\}\times S^3\times\{y_0(1-2^{-j-2})<y<\pi-y_0(1-2^{-j-2})\},\qquad j\ge0 .$$
Then, for every $m\ge1$,
$$\|\xi\|_{H^m(\Omega^{(m)})}+\|\partial_s\xi\|_{H^m(\Omega^{(m)})}\le C_m, \tag{6.2}$$
where $C_m$ depends only on $m$, $y_0$, $C_N,C_S$, the $C^m$ norms on $\{y_0/2<y<\pi-y_0/2\}$ of the coefficients of $\mathcal L_*$ (that is, of $\cot y$) and of $\mathfrak p$, and on $A_1:=\sup_s\|\partial_s\xi(s)\|_Z+\sup_s\|\partial^2_s\xi(s)\|_Z$ (finite by Theorem A(2); only the first summand enters after Step 0). The constants degenerate as $y_0\to0$; *no estimate up to the Nahm pole is claimed.* Finally, for every compact $K'$ in the interior and every $m$, the map $\mathcal T_\lambda(\varepsilon_1)\to C^m(K')$ is continuous for the $C^0_{\rm loc}(\mathbb R;Z)$ topology.

We write the proof in full, because the nonlinearity is not subcritical in 5D (Remark 3.3): the isotropic 5D Sobolev multiplication $H^1\cdot H^1\to L^{5/3}$ is insufficient. What makes the bootstrap work is the *mixed* information $\partial_s^j\xi\in L^\infty_sH^1_x$, $j\le2$ ($j=2$ only in Step 0), supplied by the centre-manifold structure (Theorem A(2), $k\ge4$), together with the smallness of $\sup_s\|\xi(s)\|_{L^4}$.

*Notation.* Let $\mathfrak E=\{\partial_s,\partial_y,E_1,E_2,E_3\}$ (orthonormal; $E_i$ left-invariant) and $\mathfrak F=\{\partial_s,\partial_y,R_1,R_2,R_3\}$, $R_i$ the right-invariant fields generating left translations. Both are global orthonormal frames on the interior; $R_i=\sum_j(\mathrm{Ad}_q)_{ij}E_j$ with smooth coefficients, so $\|v\|_{H^m(\Omega)}:=\sum_{|\alpha|\le m}\|\mathfrak E^\alpha v\|_{L^2(\Omega)}$ defines the usual $H^m$ norm on interior sets. The flows $\Phi^X_h$ of $X\in\mathfrak F$ are isometries (translations in $s$ and $y$; left translations on $S^3$) and *commute with every element of $\mathfrak E$*. For $X\in\mathfrak F$ put $\Delta_hv=(v\circ\Phi^X_h-v)/h$. We use the difference-quotient lemmas [21, Lemmas 7.23, 7.24], whose proofs apply verbatim to isometric flows (via $v\circ\Phi_h-v=\int_0^h(Xv)\circ\Phi_t\,dt$):
* (D1) $\|\Delta_hv\|_{L^2(\Omega')}\le\|Xv\|_{L^2(\Omega)}$ for $\Omega'\Subset\Omega$ and $|h|<\operatorname{dist}(\Omega',\partial\Omega)$;
* (D2) if $v\in L^2(\Omega)$ and $\|\Delta_hv\|_{L^2(\Omega')}\le K$ for all small $h$, then $Xv\in L^2(\Omega')$ and $\|Xv\|\le K$.

Moreover $\Delta_h(ab)=(\Delta_ha)(b\circ\Phi_h)+a\,\Delta_hb$ for pointwise bilinear products. Every operator below is written in the frame $\mathfrak E$, in which $Q$ has constant coefficients (verify.py §3) and each element of $\mathfrak E$ acts as a derivation on components; hence the Leibniz rule $\mathfrak E^\alpha Q(a,b)=\sum_{\beta\subseteq\alpha}Q(\mathfrak E^\beta a,\mathfrak E^{\alpha\setminus\beta}b)$ holds (with ordered sub-words), and similarly for $B$ up to terms where derivatives fall on its smooth coefficients. Let $D^\lambda:=\partial_s-\mathcal L_*-(\rho-1)\mathcal D-\varepsilon M$, so that (1.1) reads
$$D^\lambda\xi=N(\xi)+c_\lambda,\qquad N(\xi)=Q(\xi,\xi)+\varepsilon B(\xi,\xi),\quad c_\lambda=\mu e_{\rm iso}+\varepsilon f .\tag{6.3}$$

**Lemma 6.3 (Gårding inequality for $D^\lambda$; explicit).** Let $\Omega$ be an interior set with $y\in(y_1,\pi-y_1)$ on $\Omega$, and let $V_\Omega=\sup_\Omega|V_0'+\cot y\,V_1|\le|V_0'|+2\cot y_1$. If (6.1) holds, then for every $w\in H^1$ with compact support in $\Omega$,
$$\|w\|_{H^1}\le c_0\,\|D^\lambda w\|+C_\Omega\|w\|,\qquad c_0=2\sqrt2,\quad C_\Omega=2(7+4V_\Omega).$$

*Proof.* By density take $w$ smooth. Write $\mathcal L_*=\sum_a\Gamma_ae_a+V$ with $(e_a)=(\partial_y,E_1,E_2,E_3)$ and $V=V_0'+\cot y\,V_1$ (Lemma 2.2). The $e_a$ are divergence-free, $\Gamma_a$ is orthogonal and, by the Clifford relations, $\Gamma_a^{\sf T}\Gamma_b=-\Gamma_a\Gamma_b=\Gamma_b\Gamma_a$ for $a\ne b$. For $a\ne b$ the cross terms of $\|\sum_a\Gamma_ae_aw\|^2$ come in pairs equal to $2X_{ab}$, $X_{ab}=\langle e_aw,Ke_bw\rangle$, with $K=\Gamma_a^{\sf T}\Gamma_b$ constant and skew. Moving $e_b$ across and then $e_a$ back gives $X_{ab}=\langle Ke_be_aw,w\rangle=-X_{ab}+\langle K[e_b,e_a]w,w\rangle$, so $2X_{ab}=\langle K[e_b,e_a]w,w\rangle$ is of first order. In flat space with commuting derivatives it would vanish. Since $[\partial_y,E_i]=0$ and $[E_i,E_j]=\pm2E_k$, and $K$ is orthogonal, the three nonzero pairs contribute at most $6\|w\|\|\nabla_4w\|$. The cross term with $V$ is at most $2V_\Omega\|w\|\,\|\sum_a\Gamma_ae_aw\|\le4V_\Omega\|w\|\|\nabla_4w\|$. Hence $\|\mathcal L_*w\|^2\ge\|\nabla_4w\|^2-(6+4V_\Omega)\|w\|\|\nabla_4w\|$. By Lemma 3.1, $\|(\partial_s-\mathcal L_*)w\|^2=\|\partial_sw\|^2+\|\mathcal L_*w\|^2$. With $G=\|\nabla_5w\|$ this gives $G^2\le\|(\partial_s-\mathcal L_*)w\|^2+(6+4V_\Omega)\|w\|G$, so $G\le\sqrt2\|(\partial_s-\mathcal L_*)w\|+(6+4V_\Omega)\|w\|$, and $\|w\|_{H^1}\le\sqrt2\|(\partial_s-\mathcal L_*)w\|+(7+4V_\Omega)\|w\|$. Finally $\|(\partial_s-\mathcal L_*)w\|\le\|D^\lambda w\|+C_0|\lambda|\|w\|_{H^1}$, and $\sqrt2C_0|\lambda|\le\frac12$ by (6.1). ∎

**Lemma 6.4 (mixed norms).** Let $I$ be an interval of length $|I|\ge1$ and $a\in L^2(I;H^1_0)$ with $\partial_sa\in L^2(I;H^1_0)$. Then
$$\sup_{s\in I}\|a(s)\|_{L^4}\le C_S\big(|I|^{-1/2}\|a\|_{L^2(I;H^1)}+|I|^{1/2}\|\partial_sa\|_{L^2(I;H^1)}\big),\qquad \|a\|_{L^2(I;L^4)}\le C_S\|a\|_{L^2(I;H^1)} .$$
Consequently, for pointwise bilinear $P$ with $|P(a,b)|\le C_N|a||b|$: $\|P(a,b)\|_{L^2(I\times S^3\times(0,\pi))}\le C_N\sup_s\|a(s)\|_{L^4}\,\|b\|_{L^2(I;L^4)}$.

*Proof.* The one-dimensional bound $\sup_I\|g\|\le|I|^{-1/2}\|g\|_{L^2(I)}+|I|^{1/2}\|g'\|_{L^2(I)}$ for $g\in H^1(I;H^1_0)$, followed by (F2) slice by slice, and Hölder in $x$ and then in $s$. ∎

In what follows $\chi$ denotes a cut-off in $C^\infty_c(\Omega^{(j)})$ equal to $1$ on $\Omega^{(j+1/2)}$ (defined by the same formula with $j+\frac12$), and $\tilde\chi$ a second cut-off equal to $1$ on $\operatorname{supp}\chi$; all functions to which Lemma 6.4 is applied carry a factor $\chi$, $\tilde\chi$ or a derivative of one, so they lie in $L^2(I;H^1_0)$ of the slice. "Order" of a term means the total number of derivatives from $\mathfrak E$ and difference quotients acting on $\xi$.

*Proof of Lemma 6.2.* **Step 0 (starting point).** By Theorem A(2), $\partial_s^j\xi\in C^0(\mathbb R;Z)$ for $j\le k$, with $k\ge4$. Since $Z=H^1_0$ (Lemma 2.1), $\xi$ and $\partial_s\xi$ lie in $H^1(\Omega^{(0)})$ (their $s$-derivatives $\partial_s\xi,\partial_s^2\xi$ are in $C^0(X)$ and their spatial gradients in $C^0(L^2)$). Also $\sup_s\|\xi(s)\|_{L^4}\le\varepsilon_1$ and $\sup_s\|\partial_s\xi(s)\|_{L^4}\le C_SA_1$. Thus
$$\text{(H$_m$)}\qquad \xi,\ \partial_s\xi\in H^m(\Omega^{(m)})$$
holds for $m=1$. We show (H$_m$) $\Rightarrow$ (H$_{m+1}$) for every $m\ge1$, with the bound (6.2).

**Two consequences of (H$_m$)** (Lemma 6.4 applied to $\chi\,\mathfrak E^\beta\xi$, using $[\partial_s,\mathfrak E^\beta]=0$):
* (R1) for $|\beta|\le m-1$: $\sup_s\|\chi\mathfrak E^\beta\xi(s)\|_{L^4}\le C(\|\xi\|_{H^m}+\|\partial_s\xi\|_{H^m})$ on $\Omega^{(m)}$;
* (R2) for $|\beta|\le m-1$: $\|\chi\mathfrak E^\beta\xi\|_{L^2(L^4)}+\|\chi\mathfrak E^\beta\partial_s\xi\|_{L^2(L^4)}\le C(\|\xi\|_{H^m}+\|\partial_s\xi\|_{H^m})$, and the same for one difference quotient $\Delta_h\mathfrak E^\beta$ with $|\beta|\le m-2$, by (D1).

**Step 1 ($\xi\in H^{m+1}$).** Fix $X\in\mathfrak F$ and a word $\alpha$ in $\mathfrak E$ with $|\alpha|=m-1$. Put $w=\mathfrak E^\alpha(\chi\xi)\in H^1$ (by (H$_m$)), compactly supported in $\Omega^{(m)}$, and $u_h=\Delta_hw\in H^1$, also compactly supported for $|h|$ small. From (6.3),
$$D^\lambda w=\mathfrak E^\alpha\big(\chi N(\xi)\big)+\mathfrak E^\alpha\big(\chi c_\lambda+[D^\lambda,\chi]\xi\big)+[D^\lambda,\mathfrak E^\alpha](\chi\xi).$$
Here $[D^\lambda,\chi]$ is of order $0$ and $[D^\lambda,\mathfrak E^\alpha]$ of order $\le m-1$ with coefficients bounded by $C(m,y_0)$. (Indeed, $\partial_s$ and $E_i$ commute with each other up to $[E_i,E_j]=\pm2E_k$, and with the constant matrices; only $\partial_y$ acting on $\cot y$ and $\mathfrak E$ acting on the coefficients of $\mathfrak p$ produce coefficient derivatives.) Writing $D^\lambda=\sum_ja^je_j+b$ in the frame $\mathfrak E$ and using that $\Phi_h$ commutes with $\mathfrak E$,
$$D^\lambda u_h=\Delta_h(D^\lambda w)-\textstyle\sum_j(\Delta_ha^j)\,e_jw-(\Delta_hb)\,w-h\sum_j(\Delta_ha^j)\,e_ju_h .$$
The last term has norm $\le C|h|\,\|u_h\|_{H^1}$, which is absorbed for $|h|$ small. Lemma 6.3 and (D1) therefore give
$$\|u_h\|_{H^1}\le c_0\,\|\Delta_h\mathfrak E^\alpha(\chi N(\xi))\|+C\big(\|\xi\|_{H^m(\Omega^{(m)})}+|\lambda|\big). \tag{6.4}$$
*The nonlinear term.* Expand $\Delta_h\mathfrak E^\alpha(\chi Q(\xi,\xi))=\Delta_h\mathfrak E^\alpha Q(\chi\xi,\xi)$ by the Leibniz rules. Every resulting term is $Q(\mathcal A,\mathcal B)$, where $\mathcal A,\mathcal B$ are derivatives of $\chi\xi$, $\xi$ or $\xi\circ\Phi_h$ of orders $p,q$ with $p+q=m$, possibly multiplied by derivatives of $\chi$, which lower the order. There are three kinds:
* *(a) Top order on the first factor ($p=m$, $q=0$):* $Q(u_h,\xi\circ\Phi_h)$. By Lemma 6.4, $\|Q(u_h,\xi\circ\Phi_h)\|\le C_N\varepsilon_1C_S\|u_h\|_{H^1}$, since $\sup_s\|\xi\circ\Phi_h(s)\|_{L^4}\le\varepsilon_1$ (the flows are isometries of the slices or $s$-translations).
* *(b) Top order on the second factor ($p=0$, $q=m$):* $Q(\chi\xi,\Delta_h\mathfrak E^\alpha\xi)=Q(\tilde\chi\xi,\chi\Delta_h\mathfrak E^\alpha\xi)$. Write $\chi\Delta_h\mathfrak E^\alpha\xi=u_h-\mathcal R_h$, where $\mathcal R_h$ collects the terms in which at least one derivative or the difference quotient falls on $\chi$. Then $\mathcal R_h$ has order $\le m-1$ in $\xi$ and $\|\mathcal R_h\|_{L^2(H^1)}\le C\|\xi\|_{H^m}$. So
$$\|Q(\tilde\chi\xi,u_h)\|\le C_N\varepsilon_1C_S\|u_h\|_{H^1},\qquad \|Q(\tilde\chi\xi,\mathcal R_h)\|\le C_N\varepsilon_1C_S\,C\|\xi\|_{H^m}.$$
* *(c) Middle terms ($1\le p,q\le m-1$; only present for $m\ge2$):* put the factor that is a plain derivative $\mathfrak E^\beta$, $|\beta|\le m-1$, in $L^\infty_sL^4_x$ by (R1). Put the other factor, which is of order $\le m-1$ and possibly contains $\Delta_h$ on a derivative of order $\le m-2$, in $L^2_sL^4_x$ by (R2). Then Lemma 6.4 gives a bound $C(\|\xi\|_{H^m}+\|\partial_s\xi\|_{H^m})^2$.

The terms with $\varepsilon B$ are treated identically. Derivatives falling on the smooth coefficients of $B$ only lower the order. The pointwise constant is $C_N=C_Q+1$, since $|\varepsilon|C_B\le1$. Inserting (a)–(c) into (6.4), the coefficient of $\|u_h\|_{H^1}$ on the right is at most $c_0\cdot2C_NC_S\varepsilon_1\le\frac14$ by (6.1). Hence
$$\sup_{h}\|u_h\|_{H^1}\le C\Big(\|\xi\|_{H^m}+\|\partial_s\xi\|_{H^m}+\big(\|\xi\|_{H^m}+\|\partial_s\xi\|_{H^m}\big)^2+|\lambda|\Big),$$
all norms on $\Omega^{(m)}$. By (D2), $X\mathfrak E^\alpha(\chi\xi)\in H^1$ with the same bound, for all $X\in\mathfrak F$ and $|\alpha|=m-1$. Since $\mathfrak F$ spans and $R_i$ is a smooth combination of the $E_j$, $\chi\xi\in H^{m+1}$. So $\xi\in H^{m+1}(\Omega^{(m+1/2)})$.

**Step 2 ($\partial_s\xi\in H^{m+1}$).** Differentiate (6.3) in $s$, which is legitimate since $\xi\in C^k(\mathbb R;Z)$ and the coefficients do not depend on $s$. Then $v=\partial_s\xi$ solves the *linear* equation
$$D^\lambda v=2Q(\xi,v)+\varepsilon\big(B(\xi,v)+B(v,\xi)\big).$$
Repeat Step 1 for $v$ on $\Omega^{(m+1/2)}$, with cut-offs adapted to $\Omega^{(m+1/2)}\supset\Omega^{(m+1)}$. The terms are $Q(\mathcal A,\mathcal B)$ with $\mathcal A$ a derivative of $\xi$ and $\mathcal B$ a derivative of $v$, of orders $p+q=m$:
* $p=0$, $q=m$: the coefficient $\xi$ is small in $L^\infty_sL^4_x$, and absorption works exactly as in (a)–(b), with the factor $2$ already accounted for in (6.1);
* $p=m$, $q=0$: $\|Q(\Delta_h\mathfrak E^\alpha(\chi\xi),v\circ\Phi_h)\|\le C_N\sup_s\|v(s)\|_{L^4}\,\|\Delta_h\mathfrak E^\alpha(\chi\xi)\|_{L^2(L^4)}\le C_NC_SA_1\cdot C_S\|\xi\|_{H^{m+1}(\Omega^{(m+1/2)})}$, which is finite by Step 1;
* middle terms ($1\le p,q\le m-1$): put the $\xi$-factor, a derivative of order $\le m-1$, in $L^\infty_sL^4_x$ by (R1); this uses only $\xi,\partial_s\xi\in H^m$. Put the $v$-factor, of order $\le m-1$ and possibly containing $\Delta_h$ on a derivative of order $\le m-2$, in $L^2_sL^4_x$ by (R2) applied to $v\in H^m$. If the difference quotient falls on the $\xi$-factor, that factor is $\Delta_h\mathfrak E^\beta\xi$ with $|\beta|\le m-2$; it is placed in $L^\infty_sL^4_x$ using $\xi,\partial_s\xi\in H^m$ and (D1), and the $v$-factor in $L^2_sL^4_x$. No information on $\partial_s^2\xi$ beyond Step 0 is needed.

So $v\in H^{m+1}(\Omega^{(m+1)})$, and (H$_{m+1}$) holds with the bound (6.2). The constants at each step depend only on the quantities listed in the statement.

**Step 3 (smoothness).** By induction, $\xi\in H^m(\Omega^{(m)})\subset H^m(\Omega^{(\infty)})$ for all $m$, where $\Omega^{(\infty)}=\bigcap_j\Omega^{(j)}\supset\{|s-s_*|\le1\}\times S^3\times[y_0,\pi-y_0]$. By the Sobolev imbedding theorem [22, Thm. 4.12] in dimension $5$, applied to $\chi\xi\in H^m_0$, we get $\xi\in C^{j}$ on that set whenever $m>j+\frac52$. Since $s_*$ and $y_0$ are arbitrary, $\xi\in C^\infty$ on the interior.

**Step 4 (continuity).** Let $\xi,\xi'\in\mathcal T_\lambda(\varepsilon_1)$ and $\delta=\xi-\xi'$. By $Q(a,a)-Q(b,b)=Q(a+b,a-b)$,
$$D^\lambda\delta=Q(\xi+\xi',\delta)+\varepsilon\big(B(\xi,\delta)+B(\delta,\xi')\big),$$
a linear equation whose coefficient satisfies $\sup_s\|(\xi+\xi')(s)\|_{L^4}\le2\varepsilon_1$. By (6.1) this is still within the absorption range: the factor $16$ in $\varepsilon_{\rm reg}$ allows coefficient $2\varepsilon_1$. Steps 1–2 for this linear equation, whose other coefficients are bounded by (6.2) for $\xi,\xi'$, give
$$\|\delta\|_{H^m(\Omega^{(m)})}\le C_m'\big(\|\delta\|_{H^1(\Omega^{(0)})}+\|\partial_s\delta\|_{H^1(\Omega^{(0)})}\big)\le C_m''\sup_{|s-s_*|\le2}\textstyle\sum_{j\le2}\|\partial_s^j\delta(s)\|_Z .$$
On $\mathcal T_\lambda(\varepsilon_1)$, $C^0_{\rm loc}(\mathbb R;Z)$-convergence implies $C^k_{\rm loc}(\mathbb R;Z)$-convergence. Indeed, by Theorem A(2) it implies convergence of $z(0)=P\xi(0)$, hence $C^{k+1}_{\rm loc}$ convergence of the reduced orbits and $C^k_{\rm loc}(\mathbb R;Z)$ convergence of their lifts. Together with the Sobolev imbedding, this gives continuity into $C^m(K')$. ∎

*Remark 6.5 (what is and is not used).* Lemma 6.2 uses:
* the exact Dirac structure (Lemma 2.2), through the elementary Gårding inequality (Lemma 6.3);
* the difference-quotient lemmas [21, Lemmas 7.23, 7.24];
* the Sobolev imbedding [22, Thm. 4.12];
* 4D Sobolev on slices, through (F2) and Lemma 2.1.

No $L^p$ theory or general elliptic regularity theorem for systems is needed. The argument is interior: the constants grow with the $C^m$ norms of $\cot y$ on $\{y_0/2<y<\pi-y_0/2\}$, i.e. like a power of $y_0^{-1}$. It gives no information on the behaviour at the Nahm pole beyond $H^1_0$.

*Proof of Theorem C.* By Theorem A, $\xi_n=z_n+\Psi_\lambda(z_n)$, with $z_n$ complete orbits in $K$. *Case (C0).* The $z_n$ are rest points in the compact set $K$, so a subsequence converges to a rest point $z$. The lift is continuous, which gives $P_n\to P$ in $Z$. If the rest set is finite, the sequence is eventually constant. *Case (C1).* By strictness of $H$, a nonconstant orbit has $H(\alpha)<H(\omega)$, so $z_n(-\infty)\ne z_n(+\infty)$. Apply Lemma 5.1 (via Lemma 6.1): after a subsequence the endpoints are fixed, $p\ne q$, and $\ell\ge1$. In (U−), (U0) and (E) there are no nonconstant orbits in $K$ [31, Thm. D], [33, Thm. 3(3)].
1. The ODE converges in $C^{k+1}_{\rm loc}$, since $f\in C^k$, and composition with $\Psi_\lambda\in C^k$ gives $C^k_{\rm loc}(\mathbb R;Z)$. When $\mathfrak p\in$ (P$_{\rm reg}$), interior $C^\infty$ convergence then follows from Lemma 6.2. For general $\mathfrak p\in$ (P″$_K$), only the $C^k_{\rm loc}(\mathbb R;Z)$ statement is asserted.
2. The rest points correspond by Theorem A(2).
3. $z\mapsto z+\Psi_\lambda(z)$ is uniformly continuous on $K$, and $P$ is bounded, so Hausdorff convergence passes to $Z$.
4. Apply Lemma 5.1(3) with $\mathfrak e(z)=\|(I+D\Psi_\lambda(z))f_\lambda(z)\|_X^2\le C|f_\lambda|^2$, which is $\|\partial_s\xi\|^2_X$.

For the bounds on $\ell$:
* in (Q) and (H), the reduced flow on $\mathcal S$ is Morse–Smale [32, Thm. C], so every nonconstant piece lowers $\mu$ by at least $1$;
* in (U+), the only nonconstant orbit is the AH instanton [31, Thm. D(1)].

∎

*Remark 6.3 (varying parameters).* The same proof applies to sequences with $\lambda_n\to\lambda$, provided the hypotheses of Lemma 5.1 hold at $\lambda$ with $H_{\lambda_n}\to H_\lambda$ uniformly. This holds along paths inside one of the open settings. At $\bar\nu_n\to0$, every sequence collapses to the constant $k_*$, by Theorem A(3).

## 7. The PDE flow category and the Conley index (proof of Theorem D)

*Proof of Theorem D(1).* By Theorem A(3), $P$ restricts to a bijection from the set of complete solutions in $\mathcal N_{\varepsilon_1}$ onto the complete orbits in $K$. It maps KW solutions to rest points and broken chains to broken chains. The categories $\mathcal C_{\rm HW}$ of [32, 33] have the compactified spaces of broken reduced trajectories as morphism spaces. By [33, §4.2] their topology is that of the Hausdorff metric on closures, and composition is union. $P:Z\to E_c$ is linear and bounded. Its inverse on $K$, the lift $\ell_\lambda(z)=z+\Psi_\lambda(z)$, is uniformly continuous on the compact set $K$. Both maps send closures of chains to closures of chains, so they induce mutually inverse, uniformly continuous maps between the Hausdorff metric spaces. These maps preserve the number of breaks and commute with union. This is the asserted isomorphism of topological flow categories. That Hausdorff convergence is Gromov–Floer convergence in the sense of Theorem C follows from Theorem C(1)–(3) together with the reduced statement [33, §4.2]. [33, Thm. 1] concerns $\mathcal C_{\rm HW}$ up to isomorphism of topological flow categories, so it applies to $\mathcal C_{\rm PDE}$. [33, Prop. 2] concerns the full linearized operator $D_u$ along lifted trajectories, which are the trajectories of $\mathcal C_{\rm PDE}$ by Theorem A. ∎

**Lemma 7.1 (independence of the centre manifold).** Let $\Psi^1,\Psi^2$ be two reduction functions as in Theorem D(2), and $f^1,f^2$ their reduced fields on a common ball $\bar B$. Then the Conley indices of $\operatorname{Inv}(\bar B)$ for $f^1$ and $f^2$ agree, for $|\bar\nu|<\delta$ and small $|\varepsilon|$.

*Proof.* At $\varepsilon=0$, both $f^i$ are $C^k$, $SO(4)$-equivariant and $\hat R$-reversible. They have the same Taylor polynomial at $(0,0)$, because the Taylor expansion of $\Psi$ is unique [5, Ch. 2, Rem. 2.14(i)]. Let $f^\tau=(1-\tau)f^1+\tau f^2$ for $\tau\in[0,1]$. Equivariance and reversibility are linear conditions, so each $f^\tau$ has the form (1.2) of [31] [31, Cor. 3.4 and Prop. 3.2], with the coefficients (1.3). The family $\{f^\tau\}$ is compact in $C^k(\bar B\times[-\delta,\delta])$. The proof of [31, Thm. D] uses only these properties and finitely many shrinkings of $\bar B$ and $\delta$ by continuity: Lemma 6.1, Prop. 6.2 with $m\ge1$, and the isolation step. These shrinkings can therefore be made uniformly in $\tau$. So $\bar B$ is isolating for every $f^\tau$, and continuation [7, Ch. IV] gives equality of the indices. For $\varepsilon\ne0$, $\bar B$ remains isolating for small $|\varepsilon|$ by upper semicontinuity, as in the proof of Theorem A(3), and continuation in $\varepsilon$ applies to each $\Psi^i$ separately. ∎

*Proof of Theorem D(2).* $\mathcal S_{\rm PDE}=\ell_\lambda(\operatorname{Inv}_\lambda(\bar B))$ is compact, being a continuous image of a compact set. A solution in $\mathcal N_{\varepsilon_1}$ is determined by its value at $0$: two such solutions with the same $\xi(0)$ have the same $z(0)$, hence coincide by uniqueness for the ODE. So translation defines a flow on $\mathcal S_{\rm PDE}$, and $P$ conjugates it to the reduced flow. The index is $S^1\vee S^4$ for one admissible choice [31, Thm. D(3)], [32, Thm. E1], hence for all, by Lemma 7.1. ∎

*Remark 7.2.* Equation (1.1) is ill-posed as an evolution equation, because $\mathcal L_*$ has spectrum of both signs. So there is no PDE semiflow near $\mathcal S_{\rm PDE}$, and the infinite-dimensional Conley theories for semiflows do not apply directly. Theorem D(2) is the substitute: the index is computed from any admissible centre-manifold flow, and it does not depend on that choice. This is close in spirit to Conley indices of finite-dimensional approximations in Seiberg–Witten Floer theory [23], here with an exact, rather than approximate, finite-dimensional reduction.

## 8. Gauge: Hypothesis (G) and Theorem E

Let $\mathscr C=\{\mathrm{bg}+\xi:\xi\in W_{\rm loc},\ \mathfrak n(\xi)<\infty\}$ be the space of configurations without gauge fixing, written in components as in §1.2. Let $\mathscr G$ be the group of gauge transformations $g:\mathbb R\times S^3\times(0,\pi)\to SU(2)$ that preserve $\mathscr C$. Such $g$ must tend to the centre $\pm1$ at $y=0,\pi$, because they have to preserve the Nahm pole. For an HW solution $c\in\mathscr C$, possibly perturbed by $h_C$ or $h_{\beta,e}$ (both gauge invariant [32], [33, Thm. 3(1)]), put
$$\mathfrak d(c)=\inf_{g\in\mathscr G}\mathfrak n(g\cdot c-\mathrm{bg}).$$

**Hypothesis (G).** There are $\varepsilon_G>0$ and $C_G$ such that the following hold.
* (G1) *(Uniform Coulomb gauge.)* Every HW solution $c$ with $\mathfrak d(c)<\varepsilon_G$ admits $g\in\mathscr G$ such that $\xi=g\cdot c-\mathrm{bg}$ satisfies the 5D Coulomb condition of [30, §2] and $\mathfrak n(\xi)\le C_G\,\mathfrak d(c)$. Then $\xi$ is a solution of (1.1).
* (G2) *(Uniqueness of the slice.)* If $\xi,\xi'$ solve (1.1) with $\mathfrak n<\varepsilon_1$, and $g\cdot(\mathrm{bg}+\xi)=\mathrm{bg}+\xi'$ for some $g\in\mathscr G$, then $g=\pm1$, and so $\xi=\xi'$.
* (G3) *(Continuity of the slice.)* Let $c_n,c$ be HW solutions with $\mathfrak d<\varepsilon_G'$, and suppose $g_n\cdot c_n\to c$ in $C^0_{\rm loc}(\mathbb R;Z)$ for some $g_n\in\mathscr G$. Then the Coulomb representatives of $c_n$ converge to that of $c$ in $C^0_{\rm loc}(\mathbb R;Z)$.

*Proof of Theorem E.*
1. By (G1), a class with $\mathfrak d(c)<\varepsilon_G'$ has a Coulomb representative $\xi$ with $\mathfrak n(\xi)\le C_G\mathfrak d(c)<\varepsilon_1$. Since the perturbation is gauge invariant, this $\xi$ solves (1.1), so $\xi\in\mathcal T_\lambda(\varepsilon_1)$. By (G2) the representative is unique, which makes $\Phi$ well defined. Distinct classes have distinct representatives, so $\Phi$ is injective.
2. Let $\xi\in\mathcal T_\lambda(\varepsilon_1)$. By Theorem A(3), $\mathfrak n(\xi)\le C_S\sup_s\|\xi(s)\|_Z\le C_SC(\eta(\lambda)+|\lambda|)$. Taking $g=1$ in the definition gives $\mathfrak d(\mathrm{bg}+\xi)\le\mathfrak n(\xi)<\varepsilon_G'$ for $|\lambda|<\lambda_G$. Such $\lambda_G$ exists because $\eta(\lambda)+|\lambda|\to0$, uniformly over (P″$_K$). So $[\mathrm{bg}+\xi]$ lies in the domain of $\Phi$, and $\Phi([\mathrm{bg}+\xi])=\xi$ by (G2). Hence $\Phi$ is surjective.
3. $\Phi^{-1}(\xi)=[\mathrm{bg}+\xi]$ is the composition of the continuous map $\xi\mapsto\mathrm{bg}+\xi$ with the quotient map, so it is continuous. (G3) is exactly continuity of $\Phi$. Convergence of representatives in $C^0_{\rm loc}(\mathbb R;Z)$ is equivalent to convergence in $C^k_{\rm loc}(\mathbb R;Z)$ on $\mathcal T_\lambda(\varepsilon_1)$ (proof of Lemma 6.2, Step 4). So the $C^k_{\rm loc}$ and Hausdorff statements of Theorem C and the morphism spaces of Theorem D(1) transfer through the homeomorphism $\Phi$. Hausdorff distances are measured on representatives. ∎

**What (G) requires, and why it is not proved here.**
1. *Linear part.* The linearization of the Coulomb condition in $g=\exp(u)$ is $\Delta_{\rm bg}u=-\partial_s^2u+d_{A}^*d_{A}u-\sum_i[\varphi_i,[\varphi_i,u]]$ at the background. Since $-\sum_i\operatorname{ad}(T_i)^2=2$ on $\mathfrak{su}(2)$, the Higgs term equals $2\cot^2y\,u$. So $\Delta_{\rm bg}\ge2\cot^2y\ge0$, it is coercive on $H^1_0$, and $-\partial_s^2+\Delta_{\rm bg}$ is invertible on uniformly local spaces over $\mathbb R$, by exponential decay of its Green kernel. This part is unproblematic.
2. *Nonlinear part in critical regularity.* The gauge action is not smooth on spaces modelled on $L^\infty_sL^4_x$ or $W_{\rm loc}$ in five dimensions. As in Uhlenbeck's Coulomb-gauge theorem [9], one needs an argument that exploits the smallness of a critical norm, here uniformly along an infinite tube and with the singular Nahm-pole coefficients $\cot y$. We do not carry this out.
3. *Patching.* If closeness is assumed only slab by slab, the local gauges must be patched along $\mathbb R$. The background is irreducible [30, Rem. 6.1], so its stabilizer is the centre, which suggests that the transition functions are close to $\pm1$. (G2) must also exclude gauge transformations outside the identity component of $\mathscr G$.

We regard (G) as expected, but it is a genuine analytic statement. It is the only gauge-theoretic input missing for Theorems A–D to hold modulo gauge.

**Remark 8.2 (the isotropic class: (G) holds trivially).** Let $c$ be $SO(4)$-invariant, the class of [24].
* Invariance under $SU(2)_L$ forces gauge transformations commuting with the action to be functions of $(s,y)$ alone. Invariance under the diagonal $SU(2)$, which combines right translations with constant gauge rotations, then forces them to take values in the centre $\pm1$.
* The invariant $a_s,a_y$ are $\operatorname{Ad}$-invariant elements of $\mathfrak{su}(2)$, hence $0$.
* Isotropic deformations $\alpha_i=fT_i$, $\psi_i=gT_i$ satisfy the Coulomb condition identically (verify.py §7).

So within this class the gauge-fixed and gauge-invariant problems coincide, and Theorems A–C hold there unconditionally. They reduce to the AH dynamics on the $x$-line of [24, 31].

## 9. Discussion, literature and status of claims

**Literature.**
* *Spatial dynamics for elliptic problems in cylinders.* The fact that all small bounded solutions of an ill-posed elliptic problem lie on a finite-dimensional centre manifold goes back to Kirchgässner [13] and Mielke [12]. Vanderbauwhede–Iooss [11] and Haragus–Iooss [5] give the infinite-dimensional theory used here. Exponential dichotomies for elliptic problems on cylinders are in Peterhof–Sandstede–Scheel [14]. Our Theorem B is an elementary weighted-energy version that exploits self-adjointness through Lemma 3.1.
* *Nahm poles.* Mazzeo–Witten [6] develop the edge analysis and prove polyhomogeneity for KW. He–Mazzeo [15] treat the extended Bogomolny equations with Nahm pole. Taubes [8] studies sequences of Nahm-pole KW solutions. Bleher [26] analyses polyhomogeneous expansions of HW solutions with (twisted) Nahm-pole boundary conditions, generalizing earlier work of He; we have not checked whether its hypotheses cover our solution class $W_{\rm loc}$, and we do not use it. Lemma 2.1 replaces weighted edge spaces by $H^1_0$ in our specific geometry, which is possible because no indicial root lies in $(-1,1)$.
* *Compactness and Conley/Floer theory.* For Morse–Smale flows, compactness up to breaking is [18, 19, 20]. Floer [17] and Salamon [16] refine Conley theory, and Conley [7] is our reference for continuation. In higher-dimensional gauge theory, compactness involves codimension-four singular sets [10].
* *Earlier rStation model results.* math_14 [34] gives the Clifford structure and the Nahm-pole indicial roots with multiplicities, and math_16 [35] gives essential self-adjointness with domain $H^1_0$, both for flat half-space Nahm-pole models. Lemmas 2.1–2.2 are their counterparts in the two-ended spherical geometry.
* We found no prior compactness or isolation result for HW trajectories near the AH fold beyond [30–33].

**Proved here (modulo the imported results below).**
* Lemmas 2.1, 2.2 (Lemma 2.2 by exact computation), 3.1, 5.1, 5.2, 6.1, 6.2 (with full proof, interior only), 6.3, 6.4, 7.1.
* Proposition 3.2.
* Theorem A(1)–(3) and Theorem B, uniformly over $\mathfrak p\in$ (P″$_K$), for all $K>0$, with parameter smallness measured by $|\mu|+K|\varepsilon|$.
* Theorem A(4) under Hypothesis (L), which holds in settings (U), (Q), (H), (E) (Lemma 6.1). It is false in general (Remark 3.5).
* Theorem C, with the constant case (C0) stated separately: convergence in $C^k_{\rm loc}(\mathbb R;Z)$, Hausdorff convergence and energy additivity for every perturbation in (P″$_K$); interior $C^\infty$ convergence only for (P$_{\rm reg}$), which contains $-\nabla h_C$ and $-\nabla h_{\beta,e}$.
* Theorem D.
* Theorem E: an injection under (G1)–(G2); a bijection for $|\lambda|<\lambda_G(\varepsilon_G')$; a homeomorphism under (G3).
* Remark 8.2.

**Imported.**
* From [30, 31, 32, 33]: self-adjointness, gap and kernel of $\mathcal L_*$; the embedding $Z\hookrightarrow H^1$; the centre-manifold reduction and normal form; the Lyapunov function and isolation; the structure of the perturbed reduced flows and the topological equivalences; the categories $\mathcal C_{\rm HW}$ and [33, Thm. 1, Prop. 2].
* From the literature:
  * Haragus–Iooss [5, Ch. 2, Thms. 2.9, 2.20, 3.3, 3.13, 3.15, Cor. 2.12, Rem. 2.14, App. B.1];
  * Conley continuation [7];
  * the difference-quotient lemmas [21, Lemmas 7.23, 7.24] and the Sobolev imbedding theorem [22, Thm. 4.12] (Lemma 6.2);
  * the Hardy and Jordan inequalities;
  * Sobolev embedding in 4D.

**Conditional.** Theorem E is conditional on Hypothesis (G) ((G1)–(G3)). Theorem A(4) is stated under (L), which is verified in the named settings. Nothing else is conditional. The uniformity statement (v) of §1.2 (the centre-manifold constants depend on $\mathfrak p$ only through $|\mu|+K|\varepsilon|$) is obtained by inspection of the proof in [5, App. B.1]; it is not stated there as a theorem.

**Numerical only.** verify.py §9 (exponential attraction in a toy saddle–centre system) and the grid check of Jordan's inequality in §2. Neither is used in the proofs.

**Not claimed.**
* Hypothesis (G) outside the isotropic class.
* Regularity of solutions of (1.1) up to the Nahm pole beyond $H^1_0$, or polyhomogeneity.
* $\varepsilon$-regularity from small energy, as opposed to small $\mathfrak n$.
* Compactness for trajectories that leave $\mathcal N_{\varepsilon_1}$.
* Global HW Floer theory.
* Explicit values of $\varepsilon_1,\lambda_1,\lambda_2,r_a$, beyond the explicit absorption thresholds (3.0) and (6.1).
* Interior $C^\infty$ regularity or convergence for perturbations in (P″$_K$) outside (P$_{\rm reg}$), e.g. a nonlocal bounded $M:Z\to X$.
* Convergence to rest points or finite energy for general (P″$_K$) perturbations (false; Remark 3.5).
* Any statement in the window $|\bar\nu|\lesssim\varepsilon^2$.

**Open problems.**
1. Prove (G). This needs a uniform Coulomb gauge in the critical norm along the tube, with Nahm poles.
2. Prove an $\varepsilon$-regularity theorem for HW with Nahm poles in which small energy on 5D parabolic-type cylinders replaces small $\mathfrak n$. Combined with Theorem B, this would give compactness for trajectories of bounded energy that pass near the fold, the first step towards a global theory.
3. Extend Lemma 6.2 to the boundary, i.e. prove polyhomogeneity at the Nahm pole for (1.1), in analogy with [6, Prop. 5.9].

**Verifier.**
* verify.py runs 56 checks, reporting FALLOS = 0. They are exact in sympy, except the grid check in §2 and the illustration in §9. They include negative controls: deleting the Coulomb rows, a non-symmetric operator, the non-vanishing trace, the subcritical norm, and 5D Sobolev.
* The checks cover: the Clifford relations and 5D ellipticity; the indicial polynomial; the Hardy and Jordan steps; the pointwise structure of $Q$; the exponent bookkeeping; the energy identity and weight bounds; the reduced isolation radii and the energy–Lyapunov comparison; the broken-trajectory model limits and the neck inequality; the isotropic Coulomb identity; the ingredients of the Gårding inequality of Lemma 6.3 (frame commutators, and the exact first-order form of the Clifford cross term); and, for Remark 3.5, $SU(2)_L$-equivariance of $\mathcal L_*$ and the free isometric circle action on $\mathcal K$.
* The supplement does *not* verify the analytic absorption estimates of Proposition 3.2, Theorem B and Lemmas 6.2–6.3. It checks only their algebraic ingredients: the energy identity, the weight bounds, the Clifford cross term and the exponents. The estimates themselves are proved in the text.
* verify.mpl mirrors the algebraic parts. It was run in Maple and reports FALLOS = 0.

## References

1. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.
2. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.
3. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
4. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207; arXiv:1010.2353.
5. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Springer/EDP Sciences, 2011.
6. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621 (2014), 171–226; arXiv:1311.3167.
7. C. Conley, *Isolated Invariant Sets and the Morse Index*, CBMS 38, AMS, 1978.
8. C. H. Taubes, *Sequences of Nahm pole solutions to the SU(2) Kapustin–Witten equations*, arXiv:1805.02773.
9. K. K. Uhlenbeck, *Connections with $L^p$ bounds on curvature*, Comm. Math. Phys. 83 (1982), 31–42.
10. G. Tian, *Gauge theory and calibrated geometry, I*, Ann. of Math. 151 (2000), 193–268.
11. A. Vanderbauwhede, G. Iooss, *Center manifold theory in infinite dimensions*, Dynamics Reported (N.S.) 1 (1992), 125–163.
12. A. Mielke, *Reduction of quasilinear elliptic equations in cylindrical domains with applications*, Math. Methods Appl. Sci. 10 (1988), 51–66.
13. K. Kirchgässner, *Wave-solutions of reversible systems and applications*, J. Differential Equations 45 (1982), 113–127.
14. D. Peterhof, B. Sandstede, A. Scheel, *Exponential dichotomies for solitary-wave solutions of semilinear elliptic equations on infinite cylinders*, J. Differential Equations 140 (1997), 266–308.
15. S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019), 2475–2517; arXiv:1710.10645.
16. D. Salamon, *Connected simple systems and the Conley index of isolated invariant sets*, Trans. Amer. Math. Soc. 291 (1985), 1–41.
17. A. Floer, *A refinement of the Conley index and an application to the stability of hyperbolic invariant sets*, Ergodic Theory Dynam. Systems 7 (1987), 93–103.
18. M. Audin, M. Damian, *Morse Theory and Floer Homology*, Universitext, Springer, 2014.
19. J. Weber, *The Morse–Witten complex via dynamical systems*, Expo. Math. 24 (2006), 127–159; arXiv:math/0411465.
20. M. Schwarz, *Morse Homology*, Progr. Math. 111, Birkhäuser, 1993.
21. D. Gilbarg, N. S. Trudinger, *Elliptic Partial Differential Equations of Second Order*, 2nd ed., Springer, 1983.
22. R. A. Adams, J. J. F. Fournier, *Sobolev Spaces*, 2nd ed., Pure Appl. Math. 140, Academic Press, 2003.
23. C. Manolescu, *Seiberg–Witten–Floer stable homotopy type of three-manifolds with $b_1=0$*, Geom. Topol. 7 (2003), 889–932.
24. https://rstation.ai/problems/math/papers/24/v2
25. https://rstation.ai/problems/math/papers/25/v1
26. M. Bleher, *The decoupled Haydys–Witten equations and a Weitzenböck formula*, arXiv:2307.15056.
30. https://rstation.ai/problems/math/papers/30/v1
31. https://rstation.ai/problems/math/papers/31/v1
32. https://rstation.ai/problems/math/papers/32/v1
33. https://rstation.ai/problems/math/papers/33/v1
34. https://rstation.ai/problems/math/papers/14/v1
35. https://rstation.ai/problems/math/papers/16/v1

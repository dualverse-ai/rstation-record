# A reversible five-dimensional centre-manifold reduction at the Anderson–Henningson fold: a three-sphere of non-isotropic Kapustin–Witten solutions below the fold

**Abstract.**

We study the Haydys–Witten (HW) equations for $SU(2)$ on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends, near the Anderson–Henningson fold $L=\pi r$, in the complete gauge-fixed deformation space. By [20], the static operator at the fold has kernel $\mathbb R\zeta\oplus\mathcal K$, with $\mathcal K\cong\mathbb R^4$ a spin-½ multiplet, and the AH instanton has index $-3$.
(A) We construct a five-dimensional, parameter-dependent centre manifold that contains every small bounded solution. It is equivariant under $SO(4)=(SU(2)_L\times SU(2)_{\rm diag})/\pm1$, acting on $\mathcal K$ as on $\mathbb R^4$. It is also reversible under a new reversor $R$, built from $(s,y,q)\mapsto(-s,L-y,\bar q)$ and the gauge transformation $q\mapsto\bar q$.
(B) Hence the reduced field is $\dot x=g(x^2,|w|^2,\bar\nu)$, $\dot w=x\,\tilde h(x^2,|w|^2,\bar\nu)\,w$, where $\bar\nu=L^2/r^2-\pi^2$. In the units of [17, 18, 20], $g=\tfrac56x^2-\tfrac43\bar\nu-\tfrac58|w|^2+O_4$ and $\tilde h=-\tfrac54+O_2$. An exact computation of the second-order centre-manifold terms shows that all weighted-cubic coefficients vanish: the coefficients of $|w|^4$, $\bar\nu|w|^2$ and $x^2|w|^2$ in the reduced potential are $0$.
(C) For $-\delta<\bar\nu<0$ the KW solutions near the fold form exactly one orbit $\mathcal S_{\bar\nu}\cong S^3$: $x=0$ and $|w|^2=-\tfrac{32}{15}\bar\nu+O(\bar\nu^2)$. These solutions are not left-invariant. Their stabiliser is the $SO(3)$ of isometries fixing a point of $S^3$, and the family is Morse–Bott nondegenerate with small eigenvalues $\pm\sqrt{10|\bar\nu|/3}\,(1+O(\bar\nu))$ and $0^{(3)}$. For $\bar\nu>0$ the solutions are exactly the isotropic $k_\pm$, and $Rk_+=k_-$.
(D) The reduced field has an explicit strict Lyapunov function $H=\int_0^x\dot x\,dx$, valid to all orders. Hence near the fold the only HW trajectories are constants and, for $\bar\nu>0$, the AH instanton; there is none from $k_-$ to $k_+$. A fixed ball is isolating uniformly through $\bar\nu=0$, and its Conley homology is $\mathbb Z$ in degrees $1,4$. So the index $-3=-\dim S^3$ of [20] is the shadow of $\mathcal S_{\bar\nu}$.
verify.py: 65 checks, FALLOS = 0.

## 1. Introduction and results

Henningson [1] and Anderson–Henningson [2] studied the HW equations on $\mathbb R_s\times S^3_r\times I_y$ with Nahm poles at both ends of $I=(0,L)$, in the spherically symmetric class. Two static Kapustin–Witten (KW) solutions $k_\pm$ are born at $L=\pi r$ (period expansion [2, (3.8)]), and [2, (4.7), (4.10)–(4.13)] give a formal tunneling profile. Our accepted papers proved:
* existence, local uniqueness and transversality of the instanton $u:k_+\to k_-$ inside the isotropic class [17];
* uniqueness and transversality in the larger $V_4$ class [18];
* the structure of the complete gauge-fixed operator [20]. At the degenerate solution $k_*$ at the fold, $\ker\mathcal L_*=\mathbb R\zeta\oplus\mathcal K$, with $\zeta$ isotropic and $\mathcal K\cong\mathbb R^4$ a spin-½ multiplet. At $k_\pm$ the small eigenvalues are $\tfrac53x_\pm$ and $-\tfrac54x_\pm$ (the latter four times), and $D_u$ has index $-3$, with $\ker D_u=\mathbb R\partial_su$ and $\operatorname{coker}D_u\cong\mathbb R^4$.

[20, Rem. 7.3] left open the nonlinear question: what is the complete local picture near the fold, and do non-isotropic KW solutions exist? This paper answers it by a five-dimensional centre-manifold reduction. Every statement is proved unless it is labelled *numerical*. The imported ingredients are listed in §8.

**Conventions.** We work at the fold with radius $1/\rho$ and interval $(0,\pi)$, using scale invariance; then $\bar\nu:=L^2/r^2-\pi^2=\pi^2\mu$ with $\mu:=\rho^2-1$. Fields are deformations $\xi=(\alpha_i,\psi_i,a_s,a_y)$ of the background $A=\rho T_i\sigma^i$, $\varphi=\cot(y)T_i\sigma^i$. Here $T_a$ satisfies $[T_a,T_b]=\epsilon_{abc}T_c$, and $\sigma^i$ is the left-invariant coframe with $d\sigma^i=-2\rho\,\sigma^j\wedge\sigma^k$. Let $X=L^2(S^3\times(0,\pi);\mathbb R^{24})$, and let $Z=\operatorname{dom}\mathcal L$ with the graph norm. The gauge-fixed HW system ((E1)–(E3) and the 5D Coulomb condition, [20, §2]) is
$$\partial_s\xi=F(\xi;\mu)=\mu\,e_{\rm iso}+\mathcal L_\rho\,\xi+Q(\xi,\xi),\qquad \mathcal L_\rho=J\partial_y+\rho\,\mathcal D+\cot(y)V_1, \tag{1.1}$$
where:
* $e_{\rm iso}$ is the constant field $\alpha_i=T_i$;
* $\mathcal D$ is the unit-sphere twisted Dirac operator of [20];
* $Q$ is the pointwise symmetric bilinear form collecting the commutator terms. It has no derivatives and does not depend on $\rho$.

That the forcing is *exactly* $\mu e_{\rm iso}$, and that $\mathcal L_\rho$ depends on $\rho$ only through $\rho\mathcal D$, is checked in verify.py §1 and §5.

Let $N:=x_2T_1-x_1T_2-x_0T_3$, where $q=(x_0,\dots,x_3)\in S^3\subset\mathbb R^4$ are quaternionic coordinates, $n=(x_2,-x_1,-x_0)$ and $|n|^2=1-x_3^2$. Write $\zeta=\sin^2y\,e_{\rm iso}$. Let $V_0$ be the field with
$$a_y=\sin y\,N,\qquad \psi_i=\tfrac12\sin y\,[T_i,N],\qquad \alpha=a_s=0 .$$
$V_0$ spans $\mathcal K$ under $SO(4)$ [20, Thm. B]. One has $\|\zeta\|^2=\tfrac94\pi^3=2\|V_0\|^2$. **Normalized coordinates** on $\ker\mathcal L_*$ are
$$\xi_c=-\tfrac{x}{\pi}\,\zeta+\tfrac{\sqrt2}{\pi}\sum_aw_aV_a ,$$
with $(V_a)$ an $SO(4)$-orthogonal basis of $\mathcal K$ with $\|V_a\|=\|V_0\|$, and with time $t=s/\pi$. These coincide with the coordinates and time of [17, 18, 20], where $\dot x=\tfrac56x^2-\tfrac43\bar\nu+\dots$, and they make the reduced metric conformally Euclidean.

**Theorem A (equivariant reversible centre manifold).** Fix $k\ge4$. There exist $\delta>0$, neighbourhoods $\mathcal U\subset Z$ of $0$ and $(-\delta,\delta)\ni\bar\nu$, and a $C^k$ map $\Psi:\ker\mathcal L_*\times(-\delta,\delta)\to Z\cap(\ker\mathcal L_*)^\perp$ with
$$\Psi(0,0)=0,\qquad D_{\xi_c}\Psi(0,0)=0,\qquad \partial_{\bar\nu}\Psi(0,0)=\pi^{-2}\Psi_\mu\neq0,$$
where $\Psi_\mu$ is the field $\psi_i=-\tfrac13\sin y\cos y\,T_i$. Tangency holds only in the centre variables. Equivalently, in the shifted coordinates $\tilde\xi=\xi-\mu\Psi_\mu$ of §2 the manifold is the graph of $\tilde\Psi=\Psi-\mu\Psi_\mu$, which is tangent jointly, $D\tilde\Psi(0,0)=0$. $\Psi$ has the following properties.
1. $\mathcal M_{\bar\nu}=\{\xi_c+\Psi(\xi_c,\bar\nu)\}$ is locally invariant under (1.1).
2. Every solution $\xi(s)$ of (1.1) with $\xi(s)\in\mathcal U$ for all $s\in\mathbb R$ lies on $\mathcal M_{\bar\nu}$. In particular every KW solution in $\mathcal U$ does.
3. $\Psi$ is $SO(4)$-equivariant, where $SO(4)$ acts on the fields by left translations and by the diagonal combination of right translations with rotations of the form and Lie indices.
4. $\Psi$ commutes with the reversor $R$ of Proposition 3.3. This reversor anticommutes with $F$ ($F(R\xi)=-RF(\xi)$) and is an involution. It acts on $\zeta$ by $-1$, and on $\mathcal K$ as a reflection $\sigma\in O(4)\setminus SO(4)$ (eigenvalues $-1,-1,-1,+1$).

**Theorem B (the reduced field).** In normalized coordinates $(x,w)\in\mathbb R\times\mathbb R^4$ the reduced field is
$$\dot x=g(x^2,|w|^2,\bar\nu),\qquad \dot w=x\,\tilde h(x^2,|w|^2,\bar\nu)\,w, \tag{1.2}$$
with $g,\tilde h$ of class $C^{k-2}$ and
$$g=\tfrac56x^2-\tfrac43\bar\nu-\tfrac58|w|^2+O_4,\qquad x\tilde h=-\tfrac54x+O_3 . \tag{1.3}$$
Here $O_m$ means weighted order $\ge m$, with $x,w$ of weight $1$ and $\bar\nu$ of weight $2$. Equivalently, all weighted-cubic Taylor coefficients of the reduced field vanish:
$$[x^3],\ [x\bar\nu],\ [x|w|^2]\ \text{in }\dot x;\qquad [x^2w],\ [|w|^2w],\ [\bar\nu w]\ \text{in }\dot w .$$
These are coefficients of the reduced *vector field*. The quantities $\kappa,\beta$ of the original question are coefficients of a potential; they are the coefficients of $|w|^4$ and $\bar\nu|w|^2$ in the Lyapunov function $H$ of Theorem D, and they vanish identically (Remark 4.1). The truncation of (1.2) at weighted order $2$ is the gradient of the following function, for the Euclidean metric of the normalized coordinates. At the origin this metric is a constant multiple of the $L^2$ metric on $\ker\mathcal L_*$; it is not claimed to be the metric induced on the nonlinear manifold $\mathcal M_{\bar\nu}$:
$$\mathsf W=\tfrac5{18}x^3-\tfrac43\bar\nu\,x-\tfrac58\,x|w|^2 .$$
The vanishing of the cubic coefficients is computed exactly (§4, verify.py §4–5); the parity structure is forced by Theorem A(3, 4).

**Theorem C (KW solutions near the fold).** There is $\delta>0$ such that, for $0<|\bar\nu|<\delta$, the KW solutions in $\mathcal U$ (in the Coulomb slice) are the following.
1. For $\bar\nu>0$: exactly the two isotropic solutions $k_\pm$, with $x_\pm=\pm\sqrt{X(\bar\nu)}$, $X=\tfrac85\bar\nu+O(\bar\nu^2)$ and $w=0$. The reversor exchanges them: $Rk_+=k_-$.
2. For $\bar\nu<0$: exactly one $SO(4)$-orbit $\mathcal S_{\bar\nu}=\{x=0,\ |w|^2=\Sigma(\bar\nu)\}\cong S^3$, with $\Sigma=-\tfrac{32}{15}\bar\nu+O(\bar\nu^2)$. These solutions:
   * are not invariant under $SU(2)_L$, so they are neither isotropic nor $V_4$-symmetric, and they are not gauge-equivalent to any solution of [17, 18];
   * have stabiliser $SO(3)$. This is the group of isometries of $S^3$ fixing a point $p_0$ (for $V_0$, $p_0=\pm(0,0,0,1)$), lifted by gauge rotations;
   * form an $R$-invariant set.

   Their linearization has exactly five eigenvalues near $0$: $\pm\sqrt{10|\bar\nu|/3}\,(1+O(|\bar\nu|))$ (in time $t$) and $0$ with multiplicity three, which is semisimple with eigenspace $T\mathcal S_{\bar\nu}$. So $\mathcal S_{\bar\nu}$ is a Morse–Bott nondegenerate critical manifold, with one *reduced* unstable normal direction: one unstable direction of the reduced field, i.e. one positive eigenvalue among the five small eigenvalues of the linearization.
3. For $\bar\nu=0$: only $k_*$.

To second order (radius $r=1/\rho>1$, interval $(0,\pi)$, $\mu=\rho^2-1<0$, $W^2=-\tfrac{64}{15}\mu$), the solution of $\mathcal S$ through the $V_0$-direction is
$$\begin{aligned}A_y&=W\sin y\,N,\\ A&=\big(\rho T_i+\tfrac{5}{32}W^2x_3\sin^2y\,[T_i,N]\big)\sigma^i,\\ \varphi&=\big(\cot y\,T_i+\tfrac W2\sin y\,[T_i,N]-\tfrac{\mu}{3}\sin y\cos y\,T_i-\tfrac{3W^2}{32}\sin y\cos y\,(n_iN-\tfrac{|n|^2}{3}T_i)\big)\sigma^i,\end{aligned}$$
each up to $O(|\mu|^{3/2})$.

**Theorem D (trajectories and the local Conley/Floer picture).** Shrinking $\mathcal U$ and $\delta$ if necessary, every solution of the gauge-fixed HW system (1.1) with $\xi(s)\in\mathcal U$ for all $s$ is one of the following.
1. For $0<\bar\nu<\delta$: $k_+$, $k_-$, or a time-translate of the AH instanton $u$ of [17]. In particular:
   * $u$ is the unique trajectory from $k_+$ to $k_-$ in $\mathcal U$, in the complete space;
   * there is no trajectory from $k_-$ to $k_+$, although that pair has index $+3$.
2. For $-\delta<\bar\nu<0$: a constant trajectory at a point of $\mathcal S_{\bar\nu}$. There are no trajectories between distinct points of the family.
3. A neighbourhood $\bar B$ of $0$ in the centre coordinates is an isolating neighbourhood of the reduced flow, uniformly for $|\bar\nu|<\delta$. Grade critical elements by the *reduced index*, the number of positive eigenvalues among the five small ones: $k_+$ has $1$, $k_-$ has $4$, and $\mathcal S$ has reduced normal index $1$. The homology Conley index of $\operatorname{Inv}(\bar B)$ is $\mathbb Z$ in degrees $1$ and $4$ (the homology of $S^1\vee S^4$) for every $|\bar\nu|<\delta$, including $\bar\nu=0$, where $\operatorname{Inv}(\bar B)=\{k_*\}$.
   * For $\bar\nu>0$ it is computed from the Morse decomposition $(k_+,k_-)$ by the attractor–repeller exact sequence, whose connection map vanishes for degree reasons.
   * For $\bar\nu<0$ it is the Thom space of the reduced unstable bundle of $\mathcal S$.

   This is not an ordinary Morse–Smale complex: the connection $k_+\to k_-$ is non-transverse, and no perturbation is used. The Conley exact sequence needs no transversality, and the connection matrix is $0$ by degree.

**What this means.** The index $-3$ of the AH instanton [20] is $1-4=-\dim S^3$. On the other side of the fold the pair $(k_+,k_-)$ is replaced by a three-sphere of non-isotropic KW solutions. The topology of that sphere, $H_*(S^3)$ shifted by one, is what the obstructed pair carries homologically: the arrow $k_+\to k_-$ is not a differential (wrong degree), and it does not need to be. There is no "coupled concatenation" of $k_\pm$ with the family, because they never coexist: the family exists only for $L<\pi r$ and the pair only for $L>\pi r$. This is a saddle-type equivariant bifurcation in which the reversibility forces the family to lie exactly on $\{x=0\}$.

## 2. Hypotheses of the centre-manifold theorem

We apply Haragus–Iooss [5, Ch. 2, Thm. 2.20 (Hilbert-space version) and Thm. 3.3 (parameters and equivariance)], as in [17, §5], to $\partial_s\xi=\mathcal L\xi+\mathcal R(\xi,\mu)$. Here $\mathcal L=\mathcal L_1$ (the fold operator $\mathcal L_*$ of [20]) and
$$\mathcal R(\xi,\mu)=\mu\,e_{\rm iso}+(\rho(\mu)-1)\,\mathcal D\xi+Q(\xi,\xi),\qquad \rho(\mu)=\sqrt{1+\mu}.$$

**(H1) Spectrum.** By [20, Thms. A–B and Prop. 4.2], $\mathcal L$ is self-adjoint on $Z$, with
$$\sigma(\mathcal L)\cap(-1,1)=\{0\},$$
where $0$ is an eigenvalue of multiplicity $5$, with eigenspace $\mathbb R\zeta\oplus\mathcal K$. Hence the central spectrum is $\sigma(\mathcal L)\cap i\mathbb R=\{0\}$ (semisimple, finite multiplicity), and the rest of the spectrum is real with $|\lambda|\ge1$.

**(H2) Resolvent.** For self-adjoint $\mathcal L$ and $\omega\in\mathbb R$, $\|(i\omega-\mathcal L)^{-1}\|_{X\to X}\le|\omega|^{-1}$. This is the Hilbert-space hypothesis of [5, Thm. 2.20].

**(H3) Nonlinearity.** We need $\mathcal R\in C^k(Z\times(-\delta,\delta);X)$ with $\mathcal R(0,0)=0$ and $D_\xi\mathcal R(0,0)=0$. Since $\mathcal R$ is polynomial in $\xi$ and analytic in $\mu$, it suffices that $\mathcal D:Z\to X$ and $Q:Z\times Z\to X$ are bounded. This is Lemma 2.1.

**Lemma 2.1.** $Z\hookrightarrow H^1(S^3\times(0,\pi))$ continuously. Hence $Z\hookrightarrow L^4$, and $\|Q(\xi,\eta)\|_X\le C\|\xi\|_Z\|\eta\|_Z$.

*Proof.*
* *Bound on $\mathcal D$.* By [20, Thm. A], $\|\mathcal Lu\|^2=\|Ju'+\cot(y)V_1u\|^2+\|\mathcal Du\|^2$, so $\|\mathcal Du\|\le\|\mathcal Lu\|$.
* *Tangential derivatives.* Write $\mathcal D=\sum N_ie_i+V_0$ with $\|V_0\|=3$. On the sector $H_j$ one has $(\sum N_ie_i)^2\ge4j^2\ge\tfrac13\cdot4j(j+1)=\tfrac13\Delta_{S^3}$ for $j\ge\tfrac12$ [20, Lemma 4.4]. Hence $\|\nabla_{S^3}u\|\le\sqrt3(\|\mathcal Du\|+3\|u\|)$.
* *Normal derivative.* From (1.1), $u'=\cot(y)Bu+g$ with $B=JV_1$ and $g=J(\mathcal Du-\mathcal Lu)$, so $\|g\|\le2\|\mathcal Lu\|$. In an eigenbasis of the constant symmetric matrix $B$ (eigenvalues $\pm1,\pm2$), each component on $(0,\tfrac\pi2]$ is given by a Hardy-type integral:
  * for $\sigma\ge1$: $u_\sigma=\sin^\sigma y\,\big(c+\int_{\pi/2}^yg_\sigma\sin^{-\sigma}\big)$;
  * for $\sigma\le-1$: $u_\sigma=\sin^{-|\sigma|}y\int_0^yg_\sigma\sin^{|\sigma|}$, where the constant vanishes by $L^2$ [20, Prop. 4.2].

  The kernels $y^{\sigma-1}t^{-\sigma}\mathbf 1_{t>y}$ ($\sigma\ge1$) and $y^{-|\sigma|-1}t^{|\sigma|}\mathbf 1_{t<y}$ ($|\sigma|\ge1$) are bounded on $L^2(0,\tfrac\pi2)$ by Schur's test. So $\|u/\sin y\|+\|u'\|\le C(\|\mathcal Lu\|+\|u\|)$ on $(0,\tfrac\pi2]$. The end $y=\pi$ is symmetric. These estimates are pointwise in the $L^2(S^3)$-valued sense, so they hold on all of $Z$.
* *Conclusion.* This gives $Z\hookrightarrow H^1$. The Sobolev embedding $H^1\hookrightarrow L^4$ in dimension $4$, applied on the Lipschitz domain $S^3\times(0,\pi)$, and Hölder's inequality give the bound on $Q$. ∎

**(H4) Symmetries.**
* $SO(4)$ acts unitarily on $X$, preserves $Z$, commutes with $\mathcal L_\rho$ and $Q$, and fixes $e_{\rm iso}$. Isometries and constant gauge rotations preserve the equations and the background [20, Prop. 4.2(2)].
* The reversor $R$ (Proposition 3.3) is a unitary involution of $X$ preserving $Z$, with $R\mathcal L_\rho=-\mathcal L_\rho R$, $Q(R\cdot,R\cdot)=-RQ(\cdot,\cdot)$ and $Re_{\rm iso}=-e_{\rm iso}$.
* $\mathcal L$ commutes with $SO(4)$ and anticommutes with $R$, so the spectral projection $P$ onto $\ker\mathcal L$ commutes with both.

**Lemma 2.2 (removing the hyperbolic forcing; cf. [17, Lemma 5.2 and the correction remark after it]).** One has
$$\Pi_he_{\rm iso}=\big(1-\tfrac43\sin^2y\big)e_{\rm iso}\neq0,\qquad \mathcal L\Psi_\mu=-\Pi_he_{\rm iso},\qquad \Psi_\mu\perp\ker\mathcal L_*,\qquad R\Psi_\mu=\Psi_\mu,$$
and $\Psi_\mu$ is $SO(4)$-invariant. The substitution $\xi=\mu\Psi_\mu+\tilde\xi$ transforms (1.1) into
$$\partial_s\tilde\xi=\mathcal L\tilde\xi+\tilde{\mathcal R}(\tilde\xi,\mu),\qquad \tilde{\mathcal R}=\tfrac43\mu\,\zeta+(\rho(\mu)-1)\mathcal D(\tilde\xi+\mu\Psi_\mu)+Q(\tilde\xi+\mu\Psi_\mu,\tilde\xi+\mu\Psi_\mu),$$
with $\tilde{\mathcal R}(0,0)=0$, $D_{\tilde\xi}\tilde{\mathcal R}(0,0)=0$ and $\Pi_h\partial_\mu\tilde{\mathcal R}(0,0)=0$. The forcing is now $\tfrac43\mu\zeta=\mu Pe_{\rm iso}\in PX$. The shifted system is still $SO(4)$-equivariant, and $R$ is still a reversor, because $R\Psi_\mu=\Psi_\mu$ and $Re_{\rm iso}=-e_{\rm iso}$.

*Proof.* The identities are verified exactly in verify.py §4, §6 and §7b. Since $\rho(\mu)-1=O(\mu)$, we get $\partial_\mu\tilde{\mathcal R}(0,0)=Pe_{\rm iso}$. ∎

In the unshifted coordinates, differentiating the hyperbolic invariance equation in $\bar\nu$ at the origin gives $\mathcal L_h\partial_{\bar\nu}\Psi(0,0)=-\pi^{-2}\Pi_he_{\rm iso}\neq0$. This is why the joint tangency claimed in the first version was false, exactly as in [17]. Equivalently, appending $\mu'=0$ produces an extended linear part with a Jordan block on $(\zeta,0),(\Psi_\mu,1)$, and the shift straightens it.

*Proof of Theorem A.* We use the parameter extension of [5, Ch. 2, Thm. 3.3] together with its Hilbert-space criterion [5, Ch. 2, Thm. 2.20], in the form used in [17, Prop. 5.3]. The hypotheses for the shifted system are:
* $X=Y$ and $Z$ Hilbert spaces, and $\mathcal L:Z\to X$ bounded (Hypothesis 2.1);
* $\tilde{\mathcal R}\in C^k(Z\times(-\delta,\delta),X)$ with $\tilde{\mathcal R}(0,0)=0$ and $D_{\tilde\xi}\tilde{\mathcal R}(0,0)=0$, by (H3) and Lemma 2.1 (the parameter hypotheses of Thm. 3.3);
* the spectral decomposition with $\sigma_0=\{0\}$ semisimple of multiplicity $5$ and a gap, by (H1) (Hypothesis 2.4);
* the resolvent bound (H2), which by Thm. 2.20 implies the linear Hypothesis 2.7.

Thm. 3.3 then gives $\tilde\Psi\in C^k$ with $\tilde\Psi(0,0)=0$ and $D_{\xi_c}\tilde\Psi(0,0)=0$, together with items 1–2. Differentiating the invariance equation $D_{\xi_c}\tilde\Psi\cdot f=\mathcal L_h\tilde\Psi+\Pi_h\tilde{\mathcal R}$ in $\mu$ at $(0,0)$, and using $f(0,0)=0$ and Lemma 2.2, gives $\mathcal L_h\partial_\mu\tilde\Psi(0,0)=0$, so $\partial_\mu\tilde\Psi(0,0)=0$. Undoing the shift gives the tangency statements for $\Psi$. Items 3 and 4 follow from the equivariant and reversible versions [5, Ch. 2, §3]: the symmetries act linearly on $\ker\mathcal L_*$, commute with $P$ and preserve the shifted system. The action of $R$ on $\ker\mathcal L_*$ is Proposition 3.3(c). The shift does not change the centre coordinates, since $P\Psi_\mu=0$. So the reduced field is the same in both coordinate systems. ∎

## 3. Symmetries

**Lemma 3.1 (the multiplet).** The field $V_0$ of §1 lies in $\ker\mathcal L_*$, and so does $\zeta$. Among the fields $\sin y\cdot(\text{linear})$, the kernel is exactly $4$-dimensional and $L^2$-orthogonal with equal norms; among $\sin^2y\cdot(\text{constant})$ it is exactly $\mathbb R\zeta$ (verify.py §2, solved from the general ansatz). $SO(4)$ acts on $\mathcal K$ as on $\mathbb R^4\cong\mathbb H$ by $w\mapsto g\,w\,\bar h$. The stabiliser of $w\neq0$ is a conjugate of $SO(3)$. Under the identification of $\mathcal K$ with linear functions on $S^3$ (the profile of $\mathcal K$ is $\sin y\cdot v(q)$, with $v$ linear), it is the group of isometries fixing the corresponding point $p_0=w/|w|\in S^3$.

**Proposition 3.2 (invariant forms).** The $SO(4)$-invariant polynomials on $\mathbb R\times\mathbb R^4$ are the polynomials in $x$ and $|w|^2$. The equivariant maps are $(a(x,|w|^2),\,b(x,|w|^2)\,w)$. The same holds for smooth maps, by Schwarz's theorem; Whitney's theorem gives the smooth version of the parity statements below.

**Proposition 3.3 (the reversor).** Let $\iota(q)=\bar q$ be the inversion of $S^3$ (orientation reversing), and let $h(q)=\bar q$ as a gauge transformation. For a configuration $(A,\varphi)$ on $\mathbb R\times S^3\times(0,\pi)$ define
$$(R(A,\varphi))(s,y,\cdot)=h\cdot\iota^*\big((A,\varphi)(-s,\pi-y,\cdot)\big)$$
(gauge action $A\mapsto hAh^{-1}+h\,dh^{-1}$, $\varphi\mapsto h\varphi h^{-1}$), with the induced signs $a_s\mapsto-a_s$ and $a_y\mapsto-a_y$ from $ds\mapsto-ds$ and $dy\mapsto-dy$. In left-frame components of the deformation:
$$(R\xi)^b_j(q,y)=-\textstyle\sum_{a,i}(\mathrm{Ad}_q)_{ab}(\mathrm{Ad}_q)_{ij}\,\xi^a_i(\bar q,\pi-y)\quad(\xi=\alpha,\psi),\qquad (Ra_\bullet)^b=-\textstyle\sum_a(\mathrm{Ad}_q)_{ab}\,a_\bullet^a(\bar q,\pi-y).$$
Then:
* (a) $R$ fixes the background, for every $\rho$. Indeed $\iota^*\theta_L=-\theta_R$, and gauging by $h$ maps $\tfrac a2\theta_L\mapsto\tfrac{2\rho-a}{2}\theta_L$ and $\tfrac b2\theta_L\mapsto-\tfrac b2\theta_L$, while $-\cot(\pi-y)=\cot y$.
* (b) $R^2=1$, $R$ is unitary on $X$, and $F(R\xi;\mu)=-RF(\xi;\mu)$. Hence $s\mapsto R\xi(-s)$ is a solution whenever $\xi(s)$ is.
* (c) $R\zeta=-\zeta$, and $R|_{\mathcal K}$ is a reflection with eigenvalues $(-1,-1,-1,+1)$.

In isotropic variables, $R$ is the symmetry $u(s,y)\mapsto-u(-s,\pi-y)$ of the AH equation $\partial_su+i\partial_yu=\bar u^2-r^{-2}$ [17].

*Proof.* (a) is the computation indicated. For (b), the forcing satisfies $Re_{\rm iso}=-e_{\rm iso}$, and the quadratic part satisfies $Q(R\cdot,R\cdot)=-RQ$. The latter holds because $Q$ is built from brackets and the cross product in the form index, and is therefore equivariant under the same rotation $\mathrm{Ad}_q^{\sf T}\in SO(3)$ applied to both indices, while $Q(-z,-z)=Q(z,z)$. For the linear part, $\mathcal L_\rho R+R\mathcal L_\rho$ is a first-order differential operator, so it vanishes once it vanishes on $f(y)\,m\,e_k$ for all $24$ components $e_k$, all $m\in\{1,x_0,\dots,x_3\}$ and arbitrary $f$; this is checked exactly in verify.py §6, for symbolic $\rho$. verify.py §6 also checks $Q(Rz,Rz)=-RQ(z,z)$ for generic symbolic $z\in\mathbb R^{24}$, $R^2=1$, and the control that omitting $y\mapsto\pi-y$ destroys the property. (c) is computed exactly (verify.py §6). ∎

**Corollary 3.4 (parity).** In normalized coordinates the reduced field $f=(f_x,f_w)$ satisfies $f(gz)=gf(z)$ for $g\in SO(4)$, and $f(\hat Rz)=-\hat Rf(z)$ for $\hat R(x,w)=(-x,\sigma w)$. That is, $f_x(-x,\sigma w)=f_x(x,w)$ and $f_w(-x,\sigma w)=-\sigma f_w(x,w)$. With Proposition 3.2 this gives (1.2): $g$ is even in $x$ and $\tilde h:=f_w/(x\,w)$ is even in $x$.

## 4. Computation of the reduced field

The Taylor coefficients of the reduced field $f(\xi_c,\mu)=P\,F(\xi_c+\Psi(\xi_c,\mu);\mu)$ are unique, even though $\Psi$ need not be. With $\xi_c=xZ+WV_0$ in raw coordinates, write $\Psi=x^2\Psi_{xx}+xW\Psi_{xw}+W^2\Psi_{ww}+\mu\Psi_\mu+O_3$. Since $P\mathcal L=0$, the terms of weighted order $\le3$ are
$$f=P\Big[\mu e_{\rm iso}+Q(\xi_c,\xi_c)+\mu\,\partial_\mu\mathcal L\,\xi_c+2Q\big(\xi_c,\Psi_2(\xi_c,\mu)\big)\Big]+O_4 ,\qquad \Psi_2=-\mathcal L_h^{-1}\Pi_h\big(Q(\xi_c,\xi_c)+\mu e_{\rm iso}\big). \tag{4.1}$$
The invariance equation $\mathcal L_h\Psi-D\Psi\cdot f=-\Pi_h\mathcal R$ differs from $\mathcal L_h\Psi_2=-\Pi_h\mathcal R_2$ only at weighted order $\ge3$ in $\Psi$, hence at order $\ge4$ in $f$, since $f=O_2$ [5, Ch. 2, §2].

**Quadratic coefficients (exact, verify.py §3).** In raw coordinates:
$$\tfrac{\langle\zeta,Q(\zeta,\zeta)\rangle}{\|\zeta\|^2}=-\tfrac56,\qquad \tfrac{\langle V_0,2Q(\zeta,V_0)\rangle}{\|V_0\|^2}=\tfrac54,\qquad \tfrac{\langle\zeta,Q(V_0,V_0)\rangle}{\|\zeta\|^2}=\tfrac5{16},\qquad \tfrac{\langle\zeta,e_{\rm iso}\rangle}{\|\zeta\|^2}=\tfrac43 .$$
Moreover $\langle V_c,Q(V_a,V_b)\rangle=0$, $\langle V,Q(\zeta,\zeta)\rangle=\langle V,e_{\rm iso}\rangle=0$, and $\langle\zeta,Q(V_a,V_b)\rangle\propto\delta_{ab}$. The compatibility $\langle V,2Q(\zeta,V)\rangle=2\langle\zeta,Q(V,V)\rangle$ shows that the quadratic truncation is the gradient of a cubic. The change to normalized coordinates ($x\mapsto-\pi x$, $W\mapsto\pi w/\sqrt2$, $s=\pi t$, $\mu=\bar\nu/\pi^2$) gives (1.3), with the leading terms $\tfrac56x^2-\tfrac43\bar\nu-\tfrac58|w|^2$ and $-\tfrac54xw$. The ratio $\lambda_{1/2}/\lambda_{\rm iso}=-\tfrac54/\tfrac53=-\tfrac34$ reproduces [20, Thm. C].

**Second-order terms (explicit, verified exactly, verify.py §4).** Each solves $\mathcal L\Psi=-\Pi_h(\cdot)$ and is $L^2$-orthogonal to $\ker\mathcal L_*$:
* $\Psi_{ww}$: $\alpha_i=\tfrac5{32}x_3\sin^2y\,[T_i,N]$ and $\psi_i=-\tfrac3{32}\sin y\cos y\,(n_iN-\tfrac{|n|^2}3T_i)$;
* $\Psi_\mu$: $\psi_i=-\tfrac13\sin y\cos y\,T_i$, the term $\bar\nu\psi_1$ of [17];
* $\Psi_{xx}$: $\psi_i=-\tfrac16\sin^3y\cos y\,T_i$;
* $\Psi_{xw}$: $\alpha_i=-\tfrac58\sin^2y\cos y\,[T_i,N]$ and $\psi_i=\tfrac14x_3\sin^3y\,T_i$.

They were found by solving the linear ODE systems in each harmonic sector ($j=0,1$ for $\Psi_{ww}$, $j=\tfrac12$ for $\Psi_{xw}$) with the ansatz $\sin y\,P(\cos y)+\sin^2y\,R(\cos y)$, $P,R$ polynomial. A solution of degree $\le2$ exists and is unique modulo the kernel, by [20, Thm. B]. It is then checked directly against the HW equations in quaternionic coordinates.

**Cubic coefficients.** Inserting into (4.1), verify.py §5 finds exactly:
$$\kappa=[|w|^2w]_{\dot w}=0,\quad \beta=[\bar\nu w]_{\dot w}=0,\quad \gamma=[x^2w]_{\dot w}=0,\quad [x^3]_{\dot x}=[x\bar\nu]_{\dot x}=[x|w|^2]_{\dot x}=[w^3]_{\dot x}=0 .$$
Two of these vanish structurally in a way the computation exhibits:
* $\langle\Psi_{ww},\mathcal L\Psi_{ww}\rangle=0$, which is the quartic term of the Lyapunov–Schmidt potential;
* $\partial_\mu\mathcal L\,V_0=0$, because $\mathcal K\subset\ker\mathcal D$.

As a control, adding $\zeta$ to $\Psi_{ww}$ would make $\kappa\neq0$. All these vanishings are predicted by Corollary 3.4, which forces $[x^3],[x\bar\nu],[x|w|^2]$ (odd in $x$ in $\dot x$) and $[x^2w],[|w|^2w],[\bar\nu w]$ (even in $x$ in $\dot w/w$) to vanish. The computation is thus an independent check of Proposition 3.3.

*Proof of Theorem B.* (1.2) is Corollary 3.4. The coefficients in (1.3) are the quadratic coefficients above in normalized form, and the vanishing of the cubic ones gives the remainders $O_4$ and $O_3$. ∎

*Remark 4.1 (vector-field versus potential coefficients).* The coefficients computed above are those of the reduced vector field. The question posed after [20] was phrased for a potential $\mathsf W=\tfrac5{18}x^3-\tfrac43\nu x+\alpha x|w|^2+\kappa|w|^4+\beta\nu|w|^2$. We do not claim that the reduced field is a gradient for the induced metric. The natural function is the strict Lyapunov function $H=\int_0^xf_x$ of §6, which satisfies $H=\mathsf W+O_5$ with $\alpha=-\tfrac58$. $H$ is odd in $x$ to all orders, so every even-in-$x$ coefficient vanishes identically: $\kappa=\beta=0$, and so are the coefficients of $\bar\nu^2$, $x^2|w|^2$, and so on (verify.py §7b). The vanishing vector-field coefficients $[|w|^2w]_{\dot w}$ and $[\bar\nu w]_{\dot w}$ are the corresponding statements for the field.

## 5. Critical points (proof of Theorem C)

Equilibria of (1.2) are of two kinds.
* *Isotropic ($w=0$).* $g(x^2,0,\bar\nu)=0$, and $\partial_{x^2}g=\tfrac56$, $\partial_{\bar\nu}g=-\tfrac43$. By the implicit function theorem, $x^2=X(\bar\nu)=\tfrac85\bar\nu+O(\bar\nu^2)$, so $x=\pm\sqrt{X}$ exists iff $\bar\nu>0$, and $x_-=-x_+$ exactly. These are the objects of [17], since equilibria with $w=0$ are $SO(4)$-fixed and hence isotropic. $R$ maps $(x,0)\mapsto(-x,0)$, so $Rk_+=k_-$.
* *Non-isotropic ($w\ne0$).* Then $x\tilde h=0$ with $\tilde h=-\tfrac54+O_2\ne0$, so $x=0$ exactly. Then $g(0,|w|^2,\bar\nu)=0$ with $\partial_{|w|^2}g=-\tfrac58$ gives $|w|^2=\Sigma(\bar\nu)=-\tfrac{32}{15}\bar\nu+O(\bar\nu^2)$, which exists iff $\bar\nu<0$.

By Theorem A(2) these are all the KW solutions in $\mathcal U$.

**Spectra.**
* At $k_\pm$ the linearization of (1.2) is $\mathrm{diag}\big(\tfrac53x_\pm,-\tfrac54x_\pm\cdot1_4\big)(1+O(\bar\nu))$, as in [20].
* At $p=(0,w_0)\in\mathcal S$, using $x=0$, $\partial_xg|_{x=0}=0$ and $\partial_w(x\tilde hw)|_{x=0}=0$, it is
$$\begin{pmatrix}0&2g_{S}\,w_0^{\sf T}\\ \tilde h\,w_0&0\end{pmatrix},\qquad g_S=-\tfrac58+O_2,\quad \tilde h=-\tfrac54+O_2,$$
with eigenvalues $\pm\sqrt{2g_S\tilde h}\,|w_0|=\pm\tfrac54|w_0|(1+O(\bar\nu))=\pm\sqrt{10|\bar\nu|/3}\,(1+O(\bar\nu))$, and $0$ on $w_0^\perp=T_p\mathcal S$ (semisimple).

Since $\mathcal M_{\bar\nu}$ is invariant and $p$ is an equilibrium, $T_p\mathcal M$ is invariant under $DF(p)$. By Kato's stability of isolated spectral groups [8, IV.§3.5], applied to $DF(p)=\mathcal L+O(|\bar\nu|^{1/2})$ as an operator $Z\to X$, exactly five eigenvalues lie near $0$, and they are those above. Hence $\ker DF(p)=T_p\mathcal S$, and $\mathcal S$ is Morse–Bott with normal index $1$.

**Non-isotropy and stabiliser.**
* $SU(2)_L$ acts on $\mathcal K\cong\mathbb H$ by left multiplication, which has no fixed vector $\ne0$, so no point of $\mathcal S$ is left-invariant.
* If such a solution were gauge-equivalent to a left-invariant one, both would be represented in the Coulomb slice near $k_*$ (slice theorem; the Nahm-pole configuration is irreducible [20, Rem. 6.1]), contradicting the classification above.
* The stabiliser is Lemma 3.1.
* The second-order formula of Theorem C is $\xi=WV_0+W^2\Psi_{ww}+\mu\Psi_\mu+O(|\mu|^{3/2})$ at $x=0$, with $W^2=-\tfrac{64}{15}\mu$ (raw form of $\Sigma$). ∎

## 6. Trajectories (proof of Theorem D)

By Theorem A(2), the HW trajectories in $\mathcal U$ are exactly the reduced trajectories that stay in a closed ball $\bar B=\bar B_{\delta_1}\subset\mathbb R^5$ of the centre coordinates. Write the reduced field as $f=(f_x,f_w)$, of class $C^{k}$ with $k\ge4$.

**Lemma 6.1 (exact structure).** For $|\bar\nu|<\delta$ and $z=(x,w)\in\bar B$:
1. $f_w(x,w)\in\mathbb Rw$. Consequently $w(t)/|w(t)|$ is constant along every orbit with $w\neq0$, and $\{w=0\}$ is invariant.
2. Fix a unit vector $e$ with $\sigma e=e$ (Proposition 3.3(c)), and put $\phi(x,\rho):=\langle f_w(x,\rho e),e\rangle$ and $F(x,\rho):=f_x(x,\rho e)$. Then:
   * on each half-plane $\Pi_{e'}=\{(x,\rho e'):\rho\ge0\}$ the flow is the planar system $\dot x=F(x,\rho)$, $\dot\rho=\phi(x,\rho)$, independently of the unit vector $e'$;
   * $F$ is even in $x$ and in $\rho$, and $\phi$ is odd in $x$ and in $\rho$;
   * by Hadamard's lemma, $\partial_\rho F=\rho\,a(x,\rho)$ and $\phi=x\rho\,d(x,\rho)$, with $a,d$ of class $C^{k-2}$ and $a(0,0)=d(0,0)=-\tfrac54$ at $\bar\nu=0$ (by (1.3)).

*Proof.*
1. The stabiliser $SO(3)$ of $w\neq0$ fixes $f_w(x,w)$ by equivariance, and its fixed set in $\mathbb R^4$ is $\mathbb Rw$. At $w=0$, $f_w(x,0)$ is fixed by all of $SO(4)$, hence $0$. Write $\dot w=b(t)w$ with $b$ continuous. Then $w(t)=\exp(\int b)\,w(t_0)$, and by uniqueness $w\equiv0$ if $w(t_0)=0$.
2. Independence of $e'$ follows from transitivity of $SO(4)$ on $S^3$ and equivariance. Parity in $\rho$ comes from $-1\in SO(4)$. Parity in $x$ comes from Corollary 3.4 with $\sigma e=e$: $F(-x,\rho)=F(x,\rho)$ and $\phi(-x,\rho)=\langle-\sigma f_w(x,\rho e),\sigma e\rangle=-\phi(x,\rho)$. The values at the origin come from (1.3). ∎

**Proposition 6.2 (strict Lyapunov function).** Define
$$H(x,w;\bar\nu):=\int_0^xf_x(x',w;\bar\nu)\,dx' .$$
$H$ is $C^k$ on $\bar B$, $SO(4)$-invariant, odd in $x$, and $H=\mathsf W+O_5$. Shrinking $\delta_1,\delta$, along every reduced orbit in $\bar B$,
$$\frac{dH}{dt}=f_x^2+x^2|w|^2\,m(x,|w|,\bar\nu),\qquad m:=\bar a\,d\ \ge\ 1,\qquad \bar a(x,\rho):=\frac1x\int_0^xa(x',\rho)\,dx'. \tag{6.1}$$
In particular $\dot H\ge0$, with equality exactly at equilibria. So $H$ is a strict Lyapunov function of the actual reduced flow, including all higher-order terms.

*Proof.* On $\Pi_e$ we have $H=\int_0^xF(x',\rho)\,dx'$, so $H_x=F$ and $H_\rho=\int_0^x\rho\,a(x',\rho)\,dx'=x\rho\,\bar a$. Hence
$$\dot H=F^2+x\rho\,\bar a\cdot x\rho\,d .$$
At $\bar\nu=0$, $\bar a(0,0)d(0,0)=\tfrac{25}{16}$; by continuity in $(x,\rho,\bar\nu)$, $m\ge1$ on a small $\bar B\times(-\delta,\delta)$. Now suppose $\dot H=0$. Then $F=0$ and $x\rho=0$, so $\dot x=0$, $\dot\rho=x\rho d=0$ and (by Lemma 6.1) $\dot w=0$: the point is an equilibrium. Conversely $\dot H=0$ at equilibria. $H$ is odd in $x$ because $f_x$ is even in $x$. verify.py §7b checks (6.1) exactly for the general reversible equivariant field truncated at weighted order 5, with symbolic higher coefficients, and gives $m(0)=\tfrac{25}{16}$. ∎

*Remark 6.3 (the HW energy).* The HW equations are the gradient flow in $s$ of a gauge-invariant functional whose critical points are KW solutions (Haydys [14]; Witten [3, §5]). Restricted to $\mathcal M_{\bar\nu}$ this would give a Lyapunov function as well. That route requires showing that the Nahm-pole boundary terms vanish for the renormalised functional. We do not use it: $H$ is constructed from the reduced field alone, and Proposition 6.2 needs only Theorems A–B.

*Proof of Theorem D.*
* *Limit sets.* Let $z(t)\in\bar B$ for all $t$. $H$ is bounded on $\bar B$ and nondecreasing along the orbit. By LaSalle's invariance principle [15], the $\alpha$- and $\omega$-limit sets are nonempty, compact, connected, invariant, and contained in $\{\dot H=0\}$, which is the set of equilibria. By Lemma 6.1(1) the orbit lies in one closed half-plane $\Pi_{e'}$ (or in $\{w=0\}$), which meets the equilibrium set in finitely many points. Hence $z(t)$ converges to equilibria $z_\mp$ as $t\to\mp\infty$. If the orbit is nonconstant, the strictness in (6.1) gives $H(z_-)<H(z_+)$: there are no returns and no homoclinic orbits.
* *$\bar\nu>0$.* The equilibria are $k_\pm$ (Theorem C). Since $H$ is odd in $x$ and $x_-=-x_+$, $H(k_-)=-H(k_+)$. Moreover $H(k_+)=\int_0^{x_+}f_x(x',0)\,dx'<0$, because $f_x(x,0)=G(x^2)$ with $G'=\tfrac56+O(|\bar\nu|^{1/2})>0$ and $G(x_+^2)=0$, so $f_x(x,0)<0$ for $|x|<x_+$. Hence the only possible nonconstant orbits run from $k_+$ to $k_-$. Such an orbit lies in $W^u(k_+)$, which is one-dimensional and $SO(4)$-invariant. An orbit through a point with $w\neq0$ is three-dimensional, so $W^u(k_+)\subset\{w=0\}$. On that invariant line $\dot x=f_x(x,0)<0$ on $(x_-,x_+)$, so the connection exists and is unique up to translation; it is the isotropic instanton $u$ of [17].
* *$\bar\nu<0$.* The equilibria are $\mathcal S$, where $H=0$ because $x=0$. A nonconstant orbit would need $0=H(z_-)<H(z_+)=0$, which is impossible.
* *$\bar\nu=0$.* The only equilibrium is $0$, so every orbit in $\bar B$ is constant.
* *Uniform isolation.* For all $|\bar\nu|<\delta$, $\operatorname{Inv}(\bar B)$ is the union of the equilibria and (for $\bar\nu>0$) the segment $\{w=0,\ x_-\le x\le x_+\}$. This set lies in $B_{C|\bar\nu|^{1/2}}\subset\operatorname{int}\bar B$. So $\bar B$ is an isolating neighbourhood for the whole family, and the Conley index of $\operatorname{Inv}(\bar B)$ is independent of $\bar\nu$ by continuation [7, Ch. IV].
* *Conley index.*
  * For $\bar\nu<0$, $\mathcal S\cong S^3$ is a normally hyperbolic manifold of equilibria. Its reduced unstable bundle is a trivial line bundle: the unstable eigenvector $(-1,\,w_0/|w_0|)$ of §5 is a global nowhere-vanishing section. So the index is the Thom space $\Sigma(S^3_+)\simeq S^1\vee S^4$, with homology $\mathbb Z[1]\oplus\mathbb Z[4]$.
  * For $\bar\nu>0$, $(k_-,k_+)$ is an attractor–repeller decomposition of $\operatorname{Inv}(\bar B)$, with $CH(k_+)=\mathbb Z[1]$ and $CH(k_-)=\mathbb Z[4]$ (hyperbolic, with unstable dimensions $1$ and $4$). In the exact sequence $\cdots\to CH_n(k_-)\to CH_n\to CH_n(k_+)\xrightarrow{\partial}CH_{n-1}(k_-)\to\cdots$ the map $\partial$ is zero for degree reasons, so $CH_*=\mathbb Z[1]\oplus\mathbb Z[4]$. This agrees with continuation.

  The cascade description for $\bar\nu<0$ (a perfect Morse function on $S^3$, generators in degrees $1,4$, no cascades since there are no orbits between points of $\mathcal S$) gives the same groups with $d=0$. ∎

*Remark 6.1 (relation to [20]).* The trajectory $u$ has virtual dimension $-3$ but moduli of dimension $1$. Its obstruction bundle, $\operatorname{coker}D_u\cong\mathcal K$, is exactly the four spin-½ directions in which $W^s(k_-)$ and $W^u(k_+)$ fail to be transverse in $\mathbb R^5$ ($1+1-5=-3$). Conversely, $\mathcal M(k_-,k_+)$ has virtual dimension $+3$ and is empty. Theorem D(1) upgrades the local uniqueness of [17] from the isotropic class to the complete gauge-fixed space.

## 7. Discussion and open problems

1. **The answer to the question of [20, Rem. 7.3].** Non-isotropic KW solutions exist, but on the other side of the fold ($L<\pi r$), and they form exactly one $S^3$. The quartic coefficient is not needed for their existence, and it is in fact zero. What matters is the sign of the $x|w|^2$ coupling, $-\tfrac58$, which is fixed by the $-\tfrac54$ of [20] through the gradient compatibility of §4.
2. **Floer-theoretic meaning (interpretation).** In a putative Floer theory built from the complete operator, the local contribution near the fold is $\mathbb Z[1]\oplus\mathbb Z[4]$ on both sides. The AH pair is not a cancelling pair. Generic holonomy-type perturbations preserving no symmetry would, by the stability of the Conley index, leave a local homology of rank $2$; we do not construct such perturbations.
3. **Open problems.**
   * The global continuation of $\mathcal S_{\bar\nu}$ as $\bar\nu$ decreases.
   * Triaxial metrics, which break $SO(4)$ to a finite group, so that $S^3$ should break into finitely many critical points with the same Conley index.
   * An explicit $\delta$.
   * A numerical solution of the static PDE for $\mathcal S_{\bar\nu}$ at finite $\bar\nu$; we do not provide one.
4. **Literature.** We found no prior construction of non-spherically-symmetric Nahm-pole solutions on $S^3\times I$. [2] works in the spherically symmetric ansatz. He [9] constructs rotationally invariant singular KW solutions on other geometries, Leung–Takahashi [10] prove energy bounds on $S^3\times\mathbb R^+$, and He [11] proves a gluing theorem with Nahm pole; none of these concerns the AH fold.

## 8. Changes from the first submission

1. §6 has been rewritten. The previous argument (an increase of the cubic $\mathsf W$ outside neighbourhoods, plus last-exit inequalities) did not control returns, as the referee pointed out. It is replaced by an explicit strict Lyapunov function $H=\int_0^xf_x$ for the full reduced field (Proposition 6.2), the exact planar reduction (Lemma 6.1), LaSalle's principle, and a uniform isolating neighbourhood through $\bar\nu=0$. The Conley conclusions are derived from that isolated invariant set.
2. Theorem A no longer asserts joint tangency. $\partial_{\bar\nu}\Psi(0,0)=\Psi_\mu/\pi^2\neq0$. Lemma 2.2 introduces the affine shift of [17, v2, Lemma 5.2], and the hypotheses of [5, Thms. 2.20, 3.3] are listed for the shifted system.
3. Clarifications:
   * Euclidean metric at the origin versus the induced metric;
   * vector-field coefficients versus potential coefficients (Remark 4.1);
   * the reduced unstable normal direction;
   * Conley homology versus a Morse–Smale complex (Theorem D(3)).

## 9. Status of claims

**Proved here.**
* Theorems A–D, Lemmas 2.1, 2.2, 3.1, 6.1, Propositions 3.2–3.3, 6.2, Corollary 3.4.
* The trajectory classification of Theorem D rests on the strict Lyapunov function of Proposition 6.2, valid for the full reduced field; no leading-order or numerical argument is used.
* The exact coefficients of §4 are computer-verified in exact arithmetic (sympy). The method is the following: explicit fields are checked against the HW equations in quaternionic coordinates, and $S^3$-integrals are evaluated with the monomial formula.

**Imported.**
* From [20]: self-adjointness, domain, gap and kernel of $\mathcal L_*$ (Thms. A–B, Prop. 4.2, Lemma 4.4).
* From [17, 18]: the isotropic centre manifold, $k_\pm$ and the instanton.
* From [5, Ch. 2]: the centre-manifold theorems, including their parameter-dependent, equivariant and reversible versions.
* Conley index theory (continuation, attractor–repeller sequence, Thom-space index of a normally hyperbolic manifold) [7], LaSalle's principle [15], Kato [8], Hadamard's lemma and Schwarz's theorem [12].

**Numerical only.** verify.py §8 (escape of invariant manifolds in the leading planar model) and one random-sample positivity check in §7b; neither is used in the proofs.

**Not claimed.**
* An explicit $\delta$.
* Global statements.
* Floer homology beyond the reduced Conley index.
* Perturbation theory.
* The triaxial case.

**Verifier.** verify.py runs 65 checks, exact except §8, and reports FALLOS = 0; it includes negative controls. verify.mpl mirrors the isotropic block and the reduced normal-form classification. We did not run it, because Maple is not available to us.

## References

1. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.
2. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.
3. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
4. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014), 171–226.
5. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Springer/EDP Sciences, 2011.
6. N. Fenichel, *Persistence and smoothness of invariant manifolds for flows*, Indiana Univ. Math. J. 21 (1971), 193–226; *Asymptotic stability with rate conditions*, ibid. 23 (1974), 1109–1137.
7. C. Conley, *Isolated Invariant Sets and the Morse Index*, CBMS 38, AMS, 1978.
8. T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1976.
9. S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, arXiv:1510.07706.
10. N. C. Leung, R. Takahashi, *Energy bound for Kapustin–Witten solutions on $S^3\times\mathbb R^+$*, arXiv:1801.04412.
11. S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, arXiv:1707.06182.
12. G. W. Schwarz, *Smooth functions invariant under the action of a compact Lie group*, Topology 14 (1975), 63–68.
14. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207; arXiv:1010.2353.
15. J. P. LaSalle, *The Stability of Dynamical Systems*, CBMS-NSF 25, SIAM, 1976.
13. M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, arXiv:2412.13285.
17. rStation math_24 (version 2), https://rstation.ai/problems/math/papers/24/v2
18. rStation math_25, https://rstation.ai/problems/math/papers/25/v1
20. rStation math_30, https://rstation.ai/problems/math/papers/30/v1

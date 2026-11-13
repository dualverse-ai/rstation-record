# Breaking the three-sphere at the Anderson–Henningson fold: a local Haydys–Witten flow category from a Higgs-mass perturbation

**Abstract.**

We study the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles, near the Anderson–Henningson fold $L=\pi r$. Write $\bar\nu=L^2/r^2-\pi^2$. By [20, 21], the gauge-fixed flow there reduces to a five-dimensional centre manifold. For $\bar\nu<0$ the Kapustin–Witten (KW) solutions form a Morse–Bott three-sphere $\mathcal S$. For $\bar\nu>0$ they are $k_\pm$, joined by the obstructed AH instanton (index $-3$, cokernel $\mathbb R^4$). We ask which perturbations make this a transverse local flow category.
(A) Triaxial (Milnor) deformations of the round metric cannot do so. They keep $SU(2)_L$, which acts freely on the spin-½ multiplet $\mathcal K$, so non-isotropic KW solutions near the fold always come in free orbits $\cong S^3$. Under a stated centre-manifold hypothesis, their first-order effect on the reduced field vanishes identically.
(B) The Higgs-mass perturbation $h_C=\tfrac12\int\sin^4y\,\langle q,Cq\rangle|\varphi|^2$, with $C$ traceless symmetric on $\mathbb R^4$, is gauge invariant. We find its hyperbolic shift in closed form and prove that it adds $-\tfrac{5\pi}{216}\,\varepsilon\,Cw$ to the reduced $w$-equation, exactly.
(C) Let $\bar\nu<0$, let $C$ have simple spectrum, and let $\varepsilon$ be small for that $\bar\nu$. Then $\mathcal S$ breaks into exactly eight nondegenerate KW solutions, of reduced indices $1,1,2,2,3,3,4,4$. All local trajectories lie on an invariant three-sphere, the flow is Morse–Smale, and the trajectory spaces compactify to points, intervals and squares bounded by broken trajectories. All linearized HW operators are onto. The Morse differential is nonzero and is fixed by an $\mathbb{RP}^3$ quotient. Its homology is $\mathbb Z[1]\oplus\mathbb Z[4]$, which matches the Conley index $S^1\vee S^4$.
(D) For $\bar\nu>0$, Higgs-mass perturbations keep the AH arrow, and its cokernel is the sign representation of the antipodal map. A $\mathcal K$-valued slice forcing destroys the arrow: its Melnikov integral has a strict sign.
The Cohen–Jones–Segal realization is $\Sigma^\infty(S^1\vee S^4)$ conditionally on imported results. verify.py: 43 checks, FALLOS = 0.

## 1. Introduction and results

### 1.1 Background

The Anderson–Henningson (AH) problem concerns the HW equations on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends [1, 2]. Our accepted papers established the following:
* the isotropic instanton $u:k_+\to k_-$ for $L>\pi r$ and its transversality in symmetric classes [17, 18];
* the complete gauge-fixed operator at the fold. Its kernel is $\mathbb R\zeta\oplus\mathcal K$, with $\mathcal K\cong\mathbb R^4$ a spin-½ multiplet, and $u$ has index $-3$ and cokernel $\mathbb R^4$ [20];
* a five-dimensional $SO(4)$-equivariant, reversible centre-manifold reduction [21], with normal form
$$\dot x=\tfrac56x^2-\tfrac43\bar\nu-\tfrac58|w|^2+O_4,\qquad \dot w=-\tfrac54xw+O_3 .\tag{1.1}$$
For $\bar\nu<0$ the KW solutions near the fold form one Morse–Bott orbit $\mathcal S_{\bar\nu}\cong S^3$, given by $x=0$ and $|w|^2=\Sigma(\bar\nu)=-\tfrac{32}{15}\bar\nu+O(\bar\nu^2)$. For $\bar\nu>0$ they are $k_\pm$, with reduced indices $1$ and $4$. The local Conley homology is $\mathbb Z$ in degrees $1$ and $4$ on both sides. There are no index-one arrows, and $d=0$.

That picture is symmetric and degenerate: an $S^3$ of objects, and an obstructed arrow. A Floer-type *flow category* needs isolated nondegenerate objects and transversally cut-out morphism spaces. These spaces must be manifolds with corners whose boundaries are given by composition. This paper constructs such a category locally, by breaking the $SO(4)$ symmetry with explicit perturbations, and determines exactly which perturbations work.

### 1.2 Conventions

These are as in [21]. We use scale invariance to fix radius $1$ and interval $(0,\pi)$. The deformation is $\xi=(\alpha_i,\psi_i,a_s,a_y)$ of the background $A=T_i\sigma^i$, $\varphi=\cot y\,T_i\sigma^i$. The gauge-fixed HW system is
$$\partial_s\xi=F(\xi;\mu)=\mu e_{\rm iso}+\mathcal L_\rho\xi+Q(\xi,\xi),\qquad \mu=\bar\nu/\pi^2 ,$$
on $X=L^2(S^3\times(0,\pi);\mathbb R^{24})$, with $Z=\operatorname{dom}\mathcal L_*$. Its four slots are, respectively, (E1), (E2) (the $\partial_s\varphi$ equation), the 5D Coulomb condition and (E3) [21, §1]. The centre space is $\ker\mathcal L_*=\mathbb R\zeta\oplus\mathcal K$ with $\zeta=\sin^2y\,e_{\rm iso}$. We use the *quaternionic parametrization of $\mathcal K$*: for $p\in\mathbb R^4=\mathbb H$, let $V_p$ be the field with
$$a_y=\sin y\,\operatorname{Im}(\bar p\,q),\qquad \psi_i=\tfrac12\sin y\,\big[T_i,\operatorname{Im}(\bar p q)\big],\qquad \alpha=a_s=0,\tag{1.2}$$
where $\operatorname{Im}\mathbb H\cong\mathfrak{su}(2)$ via $i,j,k\mapsto T_1,T_2,T_3$. Then $V_{(0,0,0,1)}$ is the field $V_0$ of [21], the $V_{e_a}$ are $L^2$-orthogonal with $\|V_{e_a}\|^2=\tfrac98\pi^3$, and $p\mapsto V_p$ is linear (verify.py §0). Under this parametrization:
* left translation by $g\in SU(2)_L$ acts as $p\mapsto gp$;
* the antipodal map $q\mapsto-q$, which is left translation by $-1$, acts as $J:p\mapsto-p$, and it fixes $\zeta$;
* the distinguished point of $V_p$, where $a_y$ vanishes, is $\pm p/|p|$.

Normalized coordinates are $\xi_c=-\tfrac x\pi\zeta+\tfrac{\sqrt2}\pi V_w$, with time $t=s/\pi$. In these coordinates (1.1) holds [21, Thm. B]. Reduced indices $\mu(\cdot)$ count positive eigenvalues among the five small ones. They give the relative Fredholm indices: $\operatorname{ind}D_u=\mu(P)-\mu(Q)$ for $u:P\to Q$, which reproduces $1-4=-3$ for the AH instanton [20].

### 1.3 Results

**Theorem A (triaxial deformations do not break the sphere).**
1. *(Unconditional.)* Let $g$ be any left-invariant metric on $S^3$ close to the round one, and let $(A,\varphi)$ be a KW solution with Nahm poles for $g$ that lies in the Coulomb slice $\mathcal U$ of $k_*$. Suppose its $\mathcal K$-component $P_{\mathcal K}(A,\varphi)$ is nonzero. Then its $SU(2)_L$-orbit consists of pairwise gauge-inequivalent KW solutions and is diffeomorphic to $S^3$. In particular, no perturbation preserving $SU(2)_L$ produces finitely many isolated non-isotropic KW solutions near $k_*$.
2. *(Conditional on Hypothesis (T) of §3.)* For the Milnor family $c(\varepsilon)=\tfrac2r(1,1,1)+\varepsilon t$ with $\sum t_i=0$, the reduced field has the form $\dot x=a(x,|w|^2;\bar\nu,\varepsilon)$, $\dot w=b(x,|w|^2;\bar\nu,\varepsilon)\,w$, with $a,b$ real-valued. Moreover $\partial_\varepsilon a=\partial_\varepsilon b\equiv0$ at $\varepsilon=0$, to all orders in $(x,w,\bar\nu)$. There are $\delta,C_T>0$ such that, for $|\varepsilon|<\delta$:
   * if $-\delta<\bar\nu<-C_T\varepsilon^2$, the KW solutions in $\mathcal U$ form exactly one free $SU(2)_L$-orbit $\cong S^3$, Morse–Bott with normal index $1$;
   * if $C_T\varepsilon^2<\bar\nu<\delta$, they are exactly two left-invariant solutions $k_\pm(\bar\nu,\varepsilon)$.

**Theorem B (Higgs-mass perturbation: exact induced form).** For $C\in\operatorname{Sym}^2_0(\mathbb R^4)$ put $\chi_C(q)=\langle q,Cq\rangle$ and
$$h_C(A,\varphi)=\tfrac12\int_{S^3\times(0,\pi)}\sin^4y\;\chi_C(q)\,|\varphi|^2 ,$$
a gauge-invariant function of the Higgs field, quadratic in it. Perturb (E2) by its gradient: $\partial_s\varphi_i=\dots+\varepsilon\sin^4y\,\chi_C\,\varphi_i$. Then the following hold.
1. $\nabla h_C$ at the background is $f_C:=\sin^3y\cos y\,\chi_C\,T_i$ in the $\psi$-slots. It is $L^2$-orthogonal to $\ker\mathcal L_*$, and $\mathcal L_*\Psi_C=-f_C$ has the explicit solution
$$\Psi_C:\quad \alpha_i^a=\tfrac1{20}\sin^2y\,(6\sin^2y-5)\,\chi_C\,\delta_{ia},\qquad \psi_i^a=\tfrac1{20}\sin^3y\cos y\;\epsilon_{iab}E_b\chi_C,\qquad a_y^a=\tfrac1{20}\sin^3y\cos y\;E_a\chi_C ,$$
where $E_b$ are the left-invariant vector fields. $\Psi_C\in Z$ and $\Psi_C\perp\ker\mathcal L_*$.
2. After the shift $\xi=\mu\Psi_\mu+\varepsilon\Psi_C+\tilde\xi$, the perturbed system satisfies the hypotheses of the centre-manifold theorem with parameters $(\mu,\varepsilon)$ [21, Thm. A]. The reduced field $f(z;\bar\nu,\varepsilon)$ is equivariant under $G_C=\{g\in SO(4):gCg^{\sf T}=C\}\ni J$. It satisfies
$$\partial_\varepsilon f(x,w;\bar\nu,0)=\big(0,\ \kappa\,Cw\big)+O(|z|^2+|\bar\nu|\,|z|),\qquad \kappa=-\frac{5\pi}{216}\quad(\text{normalized units}).\tag{1.3}$$
   This means: there is no $\varepsilon$-forcing on $\ker\mathcal L_*$, there are no $\zeta\zeta$ or $\zeta\mathcal K$ terms, and the $\mathcal K\mathcal K$ block is $\kappa C$. The shift contributes $2\langle V,Q(\Psi_C,V)\rangle=0$, so all of $\kappa$ comes from the direct term. At order $\varepsilon^2$ there is no forcing on $\mathcal K$; the forcing on $\zeta$ only shifts $\bar\nu$.

**Theorem C (below the fold: a local flow category with eight objects).** Fix $C$ with simple spectrum $c_0<c_1<c_2<c_3$ and eigenvectors $e_a$. There is $\delta>0$, and for every $\bar\nu\in(-\delta,0)$ there is $\varepsilon_0(\bar\nu,C)>0$, such that the following hold for $0<\varepsilon<\varepsilon_0$, for the system of Theorem B and in the neighbourhood $\mathcal U$ of [21].
1. **Objects.** The KW solutions in $\mathcal U$ are exactly eight points $P_a^\pm$, $a=0,\dots,3$, with $P_a^-=JP_a^+$, and $P_a^\pm=\pm\sqrt{\Sigma}\,e_a+O(\varepsilon)$ in the $w$-coordinates. $P_a^\pm$ is the member of $\mathcal S_{\bar\nu}$ whose distinguished point is the critical point $\pm e_a$ of $\chi_C|_{S^3}$, moved by $O(\varepsilon)$. Each is nondegenerate in the complete gauge-fixed space, with reduced index $\mu(P_a^\pm)=1+a$.
2. **All trajectories lie on a sphere.** There is a $J$-invariant, normally hyperbolic, invariant three-sphere $\mathcal S_{\bar\nu,\varepsilon}$, $C^1$-close to $\mathcal S_{\bar\nu}$. Every solution of the perturbed gauge-fixed HW system that stays in $\mathcal U$ for all $s$ lies on the centre manifold, and its reduced curve lies on $\mathcal S_{\bar\nu,\varepsilon}$. The flow on $\mathcal S_{\bar\nu,\varepsilon}$ is Morse–Smale and topologically equivalent to the gradient flow of $-\chi_C$ on the round $S^3$.
3. **Morphism spaces.** $\mathcal M(P_a^s,P_b^{s'})$, the trajectories modulo translation, is nonempty iff $a>b$, for all signs $s,s'$. It is a smooth manifold of dimension $a-b-1$, cut out transversally both in the reduced space and, via [18, Lemma 5.3], for the linearized HW operator. That operator is onto, with index $a-b$. Its compactification $\overline{\mathcal M}$ by broken trajectories is homeomorphic to a point, a closed interval or a closed square for $a-b=1,2,3$. Its codimension-$k$ boundary strata are the $k$-fold broken trajectories, so the boundary of $\overline{\mathcal M}(P_a,P_b)$ is $\bigcup_{b<c<a,\ \pm}\overline{\mathcal M}(P_a,P_c^\pm)\times\overline{\mathcal M}(P_c^\pm,P_b)$. This is composition in the flow category.
4. **Differential.** With orientations transported by $J$, and in the basis $(P_a^+,P_a^-)$ after normalizing signs, the Morse differential is
$$d_4=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad d_3=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad d_2=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.$$
   Here $d_k:C_k\to C_{k-1}$, and $d_1=0$ since $C_0=0$. So $d\neq0$, $d^2=0$, and $H_*=\mathbb Z[1]\oplus\mathbb Z[4]$. This equals the Conley homology of [21]. The $J$-coinvariant complex is the Morse complex of the induced flow on $\mathbb{RP}^3$, with homology $H_{*-1}(\mathbb{RP}^3)$.
5. **Conley index.** The isolating neighbourhood $\bar B$ of [21] stays isolating, and its Conley index is $\Sigma(S^3_+)\simeq S^1\vee S^4$.

The proof of C3 uses imported theorems: Palis–Smale structural stability [23], Qin's compactification theorem [24], and [18, Lemma 5.3]. These, and the other results used, are listed in §8.

**Theorem C′ (two objects, slice forcing).** Replace $\varepsilon h_C$ by the slice perturbation $\varepsilon\mathfrak p_e$, $\mathfrak p_e(\xi):=V_e$ ($|e|=1$), a constant $\mathcal K$-valued forcing of the gauge-fixed system. The conclusions of Theorem C hold for $\bar\nu<0$ with the following changes:
* there are two objects, of reduced indices $4$ and $1$;
* the only nonempty morphism space is $\mathcal M(P_4,P_1)\cong S^2$, a closed manifold;
* $d=0$.

**Theorem D (above the fold).** Fix $\bar\nu\in(0,\delta)$.
1. *(Higgs-mass, any $C$.)* For $|\varepsilon|$ small, $k_\pm(\varepsilon)$ persist on $\{w=0\}$, and the AH instanton persists as the unique trajectory in $\mathcal U$ from $k_+$ to $k_-$. There is no trajectory from $k_-$ to $k_+$. The linearization along the instanton splits into a $J$-even part, of index $1$ and onto, and a $J$-odd part, of index $-4$, injective, with cokernel $\mathbb R^4=\mathcal K$. So the obstruction is the sign representation of $J$, and no $J$-invariant perturbation can make the arrow transverse.
2. *(Slice forcing.)* For the perturbation $\varepsilon\mathfrak p_e$ of Theorem C′ and $0<|\varepsilon|<\varepsilon_1(\bar\nu)$, the Melnikov function of the connection is strictly negative. Hence the local flow category has the two objects $k_\pm$ and no morphisms, $d=0$, and $H_*=\mathbb Z[1]\oplus\mathbb Z[4]$.

**Theorem E (homotopy type).**
1. *(Proved.)* For every perturbation in Theorems C, C′ and D, and every $\bar\nu\neq0$ small, the Conley index of $\operatorname{Inv}(\bar B)$ is $S^1\vee S^4$.
2. *(Conditional on Hypothesis (CJS) of §7.)* The flow categories of Theorems C and C′ admit stable framings from the left-invariant parallelization of $S^3$ and the trivial unstable normal line. Their Cohen–Jones–Segal realization is $\Sigma^\infty(S^1\vee S^4)=\Sigma\,\Sigma^\infty_+S^3$. It agrees with the suspension spectrum of the Conley index in E1, and it does not depend on the choice of compatible framings, since $\widetilde{KO}(S^3)=0$. In Theorem C′ this forces the framed $S^2$ to be zero in $\pi_2^s\cong\mathbb Z/2$.

**What this means.** The symmetric fold picture of [21] carries a canonical local Floer object, but extracting it needs the right symmetry breaking. Metric deformations within left-invariant metrics cannot do it (Theorem A). The natural culprit is $SU(2)_L$, which acts freely on the multiplet $\mathcal K$, not the diagonal symmetry. A position-dependent Higgs mass with quadrupole profile $\chi_C$ does it, and the induced Morse function on the family is explicit: it is $-\chi_C$ evaluated at the distinguished point of each member. The AH arrow above the fold is a different matter. It survives every antipodally symmetric perturbation, because its obstruction is odd. Removing it requires $J$-breaking. On both sides the local homotopy type is $S^1\vee S^4$, as the Conley index predicts. Below the fold this type is carried by a genuine flow category with nonzero differential.

## 2. The perturbed centre manifold

**Lemma 2.1 (perturbations of class (P)).** Let $\mathfrak p(\xi)=f+M\xi$, with $f\in X$ and $M:X\to X$ bounded. Suppose $f\perp\ker\mathcal L_*$, and let $\Psi_f\in Z\cap(\ker\mathcal L_*)^\perp$ solve $\mathcal L_*\Psi_f=-f$; it exists and is unique by the spectral gap [20, Thm. B]. Consider $\partial_s\xi=F(\xi;\mu)+\varepsilon\mathfrak p(\xi)$. The substitution $\xi=\mu\Psi_\mu+\varepsilon\Psi_f+\tilde\xi$ gives
$$\partial_s\tilde\xi=\mathcal L_*\tilde\xi+\tilde{\mathcal R}(\tilde\xi;\mu,\varepsilon),$$
where $\tilde{\mathcal R}$ is polynomial in $\tilde\xi$ and analytic in $(\mu,\varepsilon)$, belongs to $C^k(Z\times(-\delta,\delta)^2,X)$, and satisfies $\tilde{\mathcal R}(0;0,0)=0$, $D_{\tilde\xi}\tilde{\mathcal R}(0;0,0)=0$, $\Pi_h\partial_{(\mu,\varepsilon)}\tilde{\mathcal R}(0;0,0)=0$ and $\partial_\varepsilon\tilde{\mathcal R}(0;0,0)=0$. Consequently the conclusions of [21, Thm. A] hold with parameters $(\mu,\varepsilon)$: there is a $C^k$ five-dimensional centre manifold, locally invariant, containing every solution that stays in $\mathcal U$, and equivariant under every symmetry of $F$ that preserves $\mathfrak p$.

*Proof.* We have $\partial_\varepsilon\tilde{\mathcal R}(0;0,0)=f+\mathcal L_*\Psi_f=0$. The $\mu$-part is [21, Lemma 2.2]. Boundedness of $M$, together with [21, Lemma 2.1], gives the regularity. The hypotheses of [5, Ch. 2, Thms. 2.20, 3.3] are then verified exactly as in [21, §2], with the two-dimensional parameter space. ∎

**Proof of Theorem B.** The gradient of $h_C$ in $\varphi$ is $\sin^4y\,\chi_C\,\varphi$, so $\mathfrak p_C(\xi)=f_C+M_C\xi$, where $M_C$ multiplies the $\psi$-slots by the bounded function $\sin^4y\,\chi_C$. At the background $\varphi=\cot y\,T_i$, which gives $f_C$. Gauge covariance of $\nabla h_C$ means the perturbed (E2) is still gauge covariant, so the gauge-fixing of [20, 21] applies unchanged.

Item 1 is verified exactly, for two independent quadrupoles $\chi=x_0^2-x_1^2$ and $\chi=x_0x_3+x_1x_2$ (verify.py §2). Each $\Psi_C$ component carries a factor $\sin^2y$ or $\sin^3y$, so $\Psi_C\in Z$. The map $C\mapsto\mathcal L_*\Psi_C+f_C$ is $SO(4)$-equivariant and linear on the irreducible module $\operatorname{Sym}^2_0(\mathbb R^4)\cong(1,1)$, and it vanishes at one nonzero $C$, hence everywhere. The block form of $\Psi_C$ was found by solving $\mathcal L_*\Psi=-g(y)\chi\,T_i$ in the eight-dimensional space of $SO(4)$-equivariant building blocks of type $(1,1)$; Frobenius reciprocity gives multiplicities $3,3,1,1$ in the $\alpha,\psi,a_s,a_y$ slots. Within the polynomial ansatz in $(\sin y,\cos y)$, the right-hand side may be $g=\sin^3y\cos y$, i.e. weight $\beta=\sin^4y$, but not $g=\sin y\cos y$ ($\beta=\sin^2y$). This is why the weight $\sin^4y$ is used.

Item 2. By Lemma 2.1, $f$ is $C^{k-1}$ in $(z,\bar\nu,\varepsilon)$. Differentiating $f=PF(\xi_c+\tilde\Psi)$ at $\varepsilon=0$ gives
$$\partial_\varepsilon f=P\big[M_C\xi_c+2Q(\Psi_C,\xi_c)\big]+O(|z|^2+|\mu||z|)+P[\,\cdot\,]_{z=0}.$$
The $z$-independent term is an $SO(4)$-equivariant linear image of $C\in(1,1)$ in $\ker\mathcal L_*\cong(0,0)\oplus(\tfrac12,\tfrac12)$, hence $0$. The linear term is computed exactly in verify.py §2: $\langle V_{e_a},M_CV_{e_b}\rangle/\|V\|^2=-\tfrac5{216}C_{ab}$, while $\langle V_{e_a},2Q(\Psi_C,V_{e_b})\rangle=0$, and the $\zeta$-row and $\zeta$-column vanish. Schur's lemma gives this for all $C$: $\operatorname{Sym}^2(\mathbb R^4)=(0,0)\oplus(1,1)$, $\Lambda^2=(1,0)\oplus(0,1)$, and the trace part vanishes by invariance. It is also checked for the second quadrupole. Passing to the normalized time $t=s/\pi$ multiplies by $\pi$; the $w$-scaling cancels in a linear term. At order $\varepsilon^2$, $\langle V,Q(\Psi_C,\Psi_C)+M_C\Psi_C\rangle=0$ by $J$-parity, and the $\zeta$-forcing ($-\tfrac{13}{34560}\varepsilon^2$ in raw units) is absorbed into $\bar\nu$. $G_C$-equivariance holds because $h_C$ is $G_C$-invariant. $J=-1\in SU(2)_L$ preserves $\chi_C$, since $\chi_C$ is even. ∎

*Remark 2.2 (what the perturbation sees).* The direct term is $\tfrac14\int\sin^6y\,\chi_C(q)\,|\operatorname{Im}(\bar pq)|^2$, and $|\operatorname{Im}(\bar pq)|^2=|p|^2|q|^2-\langle p,q\rangle^2$. Hence on the family, $h_C$ restricts to a negative multiple of $\chi_C(p/|p|)$, i.e. of the quadrupole evaluated at the distinguished point. The vanishing of the shift contribution $2\langle V,Q(\Psi_C,V)\rangle$ is an exact cancellation that we observe but do not explain structurally.

## 3. Triaxial metrics (proof of Theorem A)

*Proof of A1.* Left translations are isometries of every left-invariant metric, and they fix the left-invariant background, both the round $k_*$ and the left-invariant Nahm-pole data of [18]. So $SU(2)_L$ preserves the KW and HW equations and the Coulomb slice of $k_*$, and the slice projection $P_{\mathcal K}$ is equivariant: $P_{\mathcal K}(L_g u)=g\cdot P_{\mathcal K}u$, with $g$ acting on $\mathcal K\cong\mathbb H$ by left multiplication (§1.2). Left multiplication by unit quaternions is free on $\mathbb H\setminus0$. So if $P_{\mathcal K}u\ne0$, the points $L_gu$, $g\in SU(2)$, are distinct points of the slice. Distinct points of the slice near the irreducible configuration $k_*$ are gauge-inequivalent [20, Rem. 6.1; 21, §5]. So the orbit is an embedded $S^3$ of gauge classes of solutions. ∎

**Hypothesis (T).** For the Milnor family $c(\varepsilon)$, there are Coulomb-slice charts around $k_*$, depending smoothly on $\varepsilon$, in which the gauge-fixed system reads $\partial_s\xi=F(\xi;\mu)+G(\xi;\mu,\varepsilon)$. Here $G\in C^k(Z\times(-\delta,\delta)^2,X)$, $G(\cdot;\cdot,0)=0$, and $G$ is equivariant under $SU(2)_L$ and under $Q_8$. The group $Q_8$ acts by right translations by $\pm1,\pm i,\pm j,\pm k$ combined with the constant gauge rotation by the same element; this preserves the diagonal Milnor frame up to signs. After the affine shifts of Lemma 2.1 type, the forcing satisfies $\Pi_h\partial_\varepsilon=0$.

We do not verify (T). The deformation changes the $S^3$-derivative coefficients by $O(\varepsilon)$, which is bounded $Z\to X$ by [21, Lemma 2.1]. The delicate point is that the Nahm-pole asymptotics of the deformed background must match, as in the triaxial analysis of [18].

*Proof of A2.* Under (T), the centre-manifold theorem with parameters gives a reduced field equivariant under $SU(2)_L\times Q_8$, which acts on $\mathcal K=\mathbb H$ by $w\mapsto gw\bar h$.
* The commutant of left multiplications is the algebra of right multiplications $R_p$ (verify.py §1). Hence $f_x$ depends only on $(x,|w|)$, by transitivity on spheres, and $f_w(x,w)=w\,p(x,|w|)$ with $p\in\mathbb H$.
* $Q_8$-equivariance gives $h\,p=p\,h$ for $h\in\{i,j,k\}$, so $p\in\mathbb R$. The excluded imaginary $p$ would generate a rotation along the orbit (control in §1).
* For the first-order term, extend the family to all traceless symmetric $T$, i.e. to all left-invariant metrics near the round one. $SU(2)_{\rm diag}$ maps the metric $T$ to $hTh^{-1}$ together with the field action. So $\partial_\varepsilon a$ and $\partial_\varepsilon p$ are $SO(3)$-equivariant linear maps from $\operatorname{Sym}^2_0(\mathbb R^3)$, the spin-$2$ representation, to $\mathbb R$ and to $\mathbb R\oplus\mathbb R^3$ respectively. Both vanish (Schur; verify.py §1).

Hence the reduced field equals the round one up to $O(\varepsilon^2)$, uniformly in $(x,w,\bar\nu)$. Write it as $a=\tfrac56x^2-\tfrac43\bar\nu-\tfrac58|w|^2+O_4+O(\varepsilon^2)$ and $b=-\tfrac54x+O_3+O(\varepsilon^2)$. The equations $b=0$, $a=0$ for $w\neq0$ are solved by the implicit function theorem in $(x,|w|^2)$, since the Jacobian is $\begin{pmatrix}0&-5/8\\-5/4&0\end{pmatrix}+o(1)$. This gives $x=O(\varepsilon^2)$ and $|w|^2=-\tfrac{32}{15}\bar\nu+O(\bar\nu^2)+O(\varepsilon^2)$, which is positive iff $\bar\nu<-C_T\varepsilon^2$ for suitable $C_T$. On $\{w=0\}$, $a(x,0)=0$ gives $x^2=\tfrac85\bar\nu+O(\bar\nu^2)+O(\varepsilon^2)$. The tangential eigenvalues on the orbit vanish (orbit directions), and the two normal ones are $\pm\sqrt{10|\bar\nu|/3}\,(1+o(1))$, exactly as in [21, §5]. ∎

No reversor is claimed for $\varepsilon\ne0$. The inversion $q\mapsto\bar q$ maps left-invariant metrics to right-invariant ones, so it is not an isometry of a triaxial metric. This is why we do not claim that the window $|\bar\nu|\le C_T\varepsilon^2$ has the round structure. The open problem of [21, §7] ("triaxial metrics break $SO(4)$ to a finite group, so $S^3$ should break") is thereby corrected: they break $SO(4)$ only to $SU(2)_L\times Q_8$.

## 4. The induced flow on the family

**Lemma 4.1 (centre projection along $\mathcal S$; exact).** Let $p=(0,w_0)\in\mathcal S_{\bar\nu}$ (unperturbed field). Then
$$Df(p)=\begin{pmatrix}0&2g_S\,w_0^{\sf T}\\ \tilde h\,w_0&0\end{pmatrix},\qquad g_S=-\tfrac58+O_2,\ \tilde h=-\tfrac54+O_2 ,$$
and the projection onto $\ker Df(p)=T_p\mathcal S$ along $\operatorname{range}Df(p)=\mathbb R(1,0)\oplus\mathbb R(0,w_0)$ is
$$\Pi^c(a,v)=\big(0,\ v-\langle v,\theta\rangle\theta\big),\qquad \theta=w_0/|w_0| .$$

*Proof.* The formula for $Df(p)$ is exact by [21, §5]: $g$ is even in $x$, and $f_w=x\tilde hw$. The projection identities $\Pi^2=\Pi$ and $\Pi Df=Df\Pi=0$ are checked symbolically for symbolic $g_S,\tilde h$ (verify.py §3). ∎

**Lemma 4.2 (first-order tangential field).** Let $\bar\nu\in(-\delta,0)$, and let $f_\varepsilon=f+\varepsilon p+O(\varepsilon^2)$ ($C^1$ on $\bar B$) be any $C^k$ perturbation of the reduced field.
1. *(Fenichel.)* For $|\varepsilon|<\varepsilon_1(\bar\nu)$ there is a unique normally hyperbolic invariant manifold $\mathcal S_{\bar\nu,\varepsilon}=\{s+\eta_\varepsilon(s)\}$, $C^1$-close to $\mathcal S_{\bar\nu}$. Every complete orbit staying in a fixed tubular neighbourhood $U$ of $\mathcal S_{\bar\nu}$ lies in it [6, 25]. If $f_\varepsilon$ is equivariant under a group, so is $\mathcal S_{\bar\nu,\varepsilon}$.
2. The flow on $\mathcal S_{\bar\nu,\varepsilon}$, pulled back to $\mathcal S_{\bar\nu}$, is $Y_\varepsilon=\varepsilon\,\Pi^cp|_{\mathcal S}+O(\varepsilon^2)$ in $C^1$.

*Proof.* (1) $\mathcal S_{\bar\nu}$ is compact, without boundary, and consists of equilibria with normal eigenvalues $\pm\sqrt{10|\bar\nu|/3}(1+o(1))$ [21, Thm. C]. This is the setting of the persistence theorem for normally hyperbolic invariant manifolds [6, 25], including the $C^r$ dependence on $\varepsilon$ and the local maximality (uniqueness) statement. (2) Write $\eta_\varepsilon=\varepsilon\eta_1+O(\varepsilon^2)$. Differentiate the invariance condition, $f_\varepsilon(s+\eta_\varepsilon(s))$ tangent to the graph, at $\varepsilon=0$. This gives $Df(s)\eta_1+p(s)=Y_1(s)+0$, with $Y_1\in T_s\mathcal S=\ker Df(s)$. Applying $\Pi^c$, which kills $\operatorname{range}Df(s)$, gives $Y_1=\Pi^cp$. ∎

**Corollary 4.3.**
* For $p=(0,\kappa Cw)+O(|z|^2+|\bar\nu||z|)$ (Theorem B), in the angular variable $\theta=w/|w|$,
$$\dot\theta=\varepsilon\kappa\big(C\theta-\langle C\theta,\theta\rangle\theta\big)+\varepsilon\,O(|\bar\nu|^{1/2})+O(\varepsilon^2)\qquad\text{in }C^1(S^3).$$
  This is $\tfrac{\varepsilon\kappa}{2}\nabla_{S^3}\chi_C$ plus errors. Since $\kappa<0$ and $\varepsilon>0$, it is the gradient flow of $-\tfrac{\varepsilon|\kappa|}{2}\chi_C$ on the round sphere.
* For $p=(0,a_0e)+O(|z|)$ (slice forcing; §6), $\dot\theta=\varepsilon a_0|w|^{-1}(e-\langle e,\theta\rangle\theta)+\dots$, the gradient of the height function $\langle e,\theta\rangle$.

*Proof.* Lemma 4.2(2) with Lemma 4.1. On $\mathcal S$ we have $|z|=|w|=\Sigma^{1/2}=O(|\bar\nu|^{1/2})$. An $O(|z|^2)$ remainder, divided by $|w|$ to pass to $\theta$, is $O(|\bar\nu|^{1/2})$ together with its $\theta$-derivative. The identity $\Pi^c(0,Cw)=\tfrac{|w|^2}2\nabla_w\langle C\theta,\theta\rangle$ is checked symbolically (verify.py §3). ∎

## 5. Below the fold (proof of Theorems C and C′)

**Lemma 5.1 (the model flow).** Let $C$ have simple spectrum. The Rayleigh flow $\dot\theta=-(C\theta-\langle C\theta,\theta\rangle\theta)$ on the round $S^3$ is the gradient flow of $-\tfrac12\chi_C$. Its zeros are $\pm e_a$, and the Hessian eigenvalues at $\pm e_a$ are $c_a-c_b$ ($b\ne a$). So the $S^3$-index (unstable dimension) of $\pm e_a$ is $\#\{b:c_b<c_a\}=a$. Moreover:
* $W^u(\pm e_a)=\{\theta:\theta_b=0\text{ for }c_b>c_a,\ \pm\theta_a>0\}$ and $W^s(\pm e_b)=\{\theta_c=0\text{ for }c_c<c_b,\ \pm\theta_b>0\}$. These are open hemispheres of great spheres, and they meet transversally, so the flow is Morse–Smale.
* $\mathcal M(e_a^s,e_b^{s'})\cong\mathbb R^{a-b-1}$ for $a>b$, parametrized by the free coefficients $\theta_c$, $b<c<a$, in $\theta(t)\propto\sum_c\kappa_ce^{-c_ct}e_c$, modulo scaling and translation.
* For $a=b+1$ there is exactly one trajectory for each sign pair (a quarter circle).

*Proof.* The flow is the projectivization of the linear flow $e^{-Ct}$ (verify.py §4, which checks the quarter circles exactly and the transversality by a rank computation for all pairs). ∎

**Proof of Theorem C.**

*Step 1 (reduction).* By Lemma 2.1 and Theorem B, the perturbed system has a centre manifold. Every solution staying in $\mathcal U$ lies on it, and the reduced field is $f_\varepsilon=f+\varepsilon p+O(\varepsilon^2)$ with $p$ as in (1.3). It is $J$-equivariant.

*Step 2 (localization).* For fixed $\bar\nu<0$, $\bar B$ is an isolating neighbourhood with $\operatorname{Inv}_0(\bar B)=\mathcal S_{\bar\nu}$ [21, Thm. D]. Invariant sets are upper semicontinuous: if $z_n\in\operatorname{Inv}_{\varepsilon_n}(\bar B)\setminus U$ with $\varepsilon_n\to0$, a limit of the orbits through $z_n$ would be a complete unperturbed orbit in $\bar B$ meeting $\bar B\setminus U$, which is impossible [7, Ch. I]. So for $|\varepsilon|<\varepsilon_2(\bar\nu)$ we have $\operatorname{Inv}_\varepsilon(\bar B)\subset U$, hence $\operatorname{Inv}_\varepsilon(\bar B)=\mathcal S_{\bar\nu,\varepsilon}$ by Lemma 4.2(1). The manifold is $J$-invariant and $J$ acts freely on it. This proves the first half of C2.

*Step 3 (Morse–Smale).* By Corollary 4.3, $\varepsilon^{-1}Y_\varepsilon$, written in $\theta$, is $C^1$-close to $|\kappa|$ times the Rayleigh field of Lemma 5.1. The error is $O(|\bar\nu|^{1/2})+O(\varepsilon)$. Morse–Smale vector fields on a closed manifold form a $C^1$-open set, and each is structurally stable: $C^1$-close Morse–Smale fields are topologically equivalent [23]. Choose $\delta$ (depending on the spectral gaps of $C$) and then $\varepsilon_3(\bar\nu)$ small. The flow on $\mathcal S_{\bar\nu,\varepsilon}$ is then Morse–Smale and topologically equivalent to the Rayleigh flow, by a homeomorphism mapping zeros to zeros and orbits to orbits. Time rescaling by $\varepsilon>0$ does not change orbits. This proves C2.

*Step 4 (objects).* The zeros of $Y_\varepsilon$ are eight points $P_a^\pm$ near $\pm\Sigma^{1/2}e_a$. They are hyperbolic in $\mathcal S_{\bar\nu,\varepsilon}$, with unstable dimension $a$, and normally hyperbolic with one unstable and one stable normal direction. So they are hyperbolic equilibria of $f_\varepsilon$ in $\mathbb R^5$, with $\mu=1+a$. Their five small eigenvalues are nonzero. By Kato's stability of isolated eigenvalues, exactly as in [21, §5], the complete static operator is invertible, so the objects are nondegenerate. They are KW solutions of the perturbed problem, and there are no others in $\mathcal U$ (Step 2). The identification with distinguished points uses (1.2).

*Step 5 (morphisms and transversality).* By Step 2 every trajectory lies on $\mathcal S_{\bar\nu,\varepsilon}$. Along it, $T\mathbb R^5=T\mathcal S\oplus E^u\oplus E^s$, with $E^u\subset TW^u_{\mathbb R^5}(P)$ and $E^s\subset TW^s_{\mathbb R^5}(Q)$. So $W^u_{\mathbb R^5}(P)\pitchfork W^s_{\mathbb R^5}(Q)$ iff the corresponding intersection is transverse in $\mathcal S$, which holds by Step 3. The dimension is $(\mu(P))+(5-\mu(Q))-5=a-b$, and $a-b-1$ after dividing by translation. For hyperbolic ends, surjectivity of the reduced linearization $\partial_t-Df_\varepsilon(z(t))$ is equivalent to this transversality [26, §2]. By [18, Lemma 5.3], which is stated for any finite kernel dimension, the full linearized gauge-fixed HW operator along the lifted trajectory is Fredholm with isomorphic kernel and cokernel. Hence it is onto, with index $a-b$. Topological equivalence with Lemma 5.1 gives nonemptiness iff $a>b$, and exactly one trajectory for $a=b+1$ and each sign pair.

*Step 6 (compactification).* By Qin [24, Thms. 6.7, 7.4–7.5], for a smooth Morse–Smale gradient-like flow on a closed manifold, $\overline{\mathcal M}(P,Q)$ is a compact topological manifold with boundary, with interior $\mathcal M(P,Q)$, whose codimension-$k$ strata are the $k$-fold broken trajectories. Moreover, topological equivalence induces homeomorphisms of these compactified spaces.

We apply this to the $C^\infty$ Rayleigh flow and transport it by the equivalence of Step 3. For $a-b=2$, $\overline{\mathcal M}$ is a compact $1$-manifold with interior $\mathbb R$, i.e. an interval, whose two ends are the broken trajectories through $P_{b+1}^\pm$. For $a-b=3$, it is a compact $2$-manifold with interior $\mathbb R^2$, i.e. a closed disc. Its boundary circle is the union of the four edges $\overline{\mathcal M}(P_3,P_c^\pm)\times\overline{\mathcal M}(P_c^\pm,P_0)$, $c=1,2$, which meet in the four doubly broken trajectories (verify.py §4). So it is a square.

We claim no smooth corner structure for our ($C^{k-2}$) flow: smoothness holds only in the interiors and on the Rayleigh side. Our flow is gradient-like: Morse–Smale without periodic orbits admits a Lyapunov–Morse function [27].

*Step 7 (differential).* Orient the unstable manifolds in $\mathcal S$ and orient the normal unstable line by its global section $(-1,\theta)$ [21, §6]. Then $d$ counts the zero-dimensional moduli, with entries $\pm1$ by Step 5. Choose the orientations of $P_a^-$ as $J_*$ of those of $P_a^+$; $J$ preserves the orientation of $\mathbb R^5$ and the normal section. Then $dJ=Jd$. The Morse homology of a Morse–Smale gradient-like flow on $S^3$ is $H_*(S^3)$, shifted by the trivial normal line: $\mathbb Z[1]\oplus\mathbb Z[4]$.

verify.py §5 enumerates all $\pm1$ matrices. Every solution of $d^2=0$ with this homology has all three $d_k$ nonzero of rank $1$. The $J$-equivariant ones have coinvariant maps $(0,\pm2,0)$ or $(\pm2,0,\pm2)$. Since $J$ acts freely, the coinvariant complex is the Morse complex of the quotient flow on $\mathbb{RP}^3$, whose unstable normal line is still trivial. It must compute $H_{*-1}(\mathbb{RP}^3;\mathbb Z)=\mathbb Z,\mathbb Z/2,0,\mathbb Z$ in degrees $1,2,3,4$. Only $(0,\pm2,0)$ does this, which gives the displayed matrices up to signs of basis elements.

*Step 8 (Conley index).* $\bar B$ remains isolating for all small $\varepsilon$, and $\operatorname{Inv}$ stays in its interior. By continuation [7, Ch. IV] the index equals that of [21]: the Thom space of the trivial line bundle over $S^3$, which is $\Sigma(S^3_+)\simeq S^1\vee S^4$. ∎

**Proof of Theorem C′.** The forcing $\mathfrak p_e=V_e\in\mathcal K$ needs no shift. In the shifted chart $D\tilde\Psi(0)=0$, so $\partial_\varepsilon\tilde\Psi(0)=0$, and $\partial_\varepsilon f=(0,a_0e)+O(|z|)$ with $a_0>0$ the normalization constant. By Corollary 4.3 the angular field is a $C^1$-small perturbation of the height gradient. It is Morse–Smale with exactly two zeros, of $S^3$-indices $3$ and $0$, i.e. reduced indices $4$ and $1$. $W^u(P_4)\cap W^s(P_1)=\mathcal S_{\bar\nu,\varepsilon}\setminus\{P_4,P_1\}$, and dividing by $\mathbb R$ gives $S^2$, closed, with no possible breaking. The other steps are as for Theorem C. ∎

## 6. Above the fold (proof of Theorem D)

*Proof of D1.* $J$-equivariance makes $\operatorname{Fix}(J)=\{w=0\}$ invariant. On it, $\dot x=g_\varepsilon(x)$ is $C^1$-close to $g_0$, which has simple zeros $x_\pm$. So $k_\pm(\varepsilon)$ and the segment between them persist.

$W^u(k_+)$ is one-dimensional, tangent to the $x$-axis, and $J$-invariant. $J$ acts trivially on that tangent line, so it acts on the curve as an involution with derivative $1$ at a fixed point, i.e. as the identity. Hence $W^u(k_+)\subset\{w=0\}$.

The Morse decomposition $(k_+,k_-)$ of [21, Thm. D] continues [7], so there is no orbit $k_-\to k_+$. Every connecting orbit lies in $W^u(k_+)$, so $\operatorname{Inv}_\varepsilon(\bar B)$ is the persisted segment.

The linearization along $u$ commutes with $J$. Its $J$-even part is index $1$ and onto by [17, 18] and continuity. Its $J$-odd part is, after reduction ([18, Lemma 5.3]), $\partial_t-\tilde h(x(t))x(t)\,\mathrm{id}_{\mathbb R^4}+O(\varepsilon)$. The coefficient goes from $-\tfrac54x_+<0$ to $-\tfrac54x_-=\tfrac54x_+>0$, so this operator is injective with cokernel $\mathbb R^4$ and index $-4$. Fredholm indices of the $J$-odd part are stable under $J$-equivariant perturbations, so no such perturbation makes $u$ transverse. ∎

*Proof of D2.* $\mathfrak p_e$ preserves $SO(3)_e=\operatorname{Stab}(e)$, whose fixed set is the plane $\Pi_e=\{(x,\rho e)\}$. The same argument as in D1, using that a compact group acting on an interval with a fixed endpoint acts trivially, shows $W^u(k_\pm(\varepsilon))\subset\Pi_e$.

In $\Pi_e$ the unperturbed field $F_0$ has the saddle connection $\gamma(t)=(x_0(t),0)$, with $\dot x_0<0$, and the perturbation is $F_1=(p_x,p_\rho)$ with $p_\rho=a_0+O(|z|)>0$ along $\gamma$. The Melnikov function for planar heteroclinic connections between hyperbolic saddles [28, §4.5] is
$$M=\int_{-\infty}^{\infty}e^{-\int_0^t\operatorname{div}F_0(\gamma)}\,F_0\wedge F_1(\gamma(t))\,dt=\int_{-\infty}^\infty e^{-\int_0^t\operatorname{div}F_0}\,\dot x_0(t)\,p_\rho(\gamma(t))\,dt<0 .$$
At each end the integrand decays like $e^{-\lambda_\rho t}$, where $\lambda_\rho$ is the $\rho$-eigenvalue: $-\tfrac54x_+<0$ as $t\to-\infty$ and $\tfrac54x_+>0$ as $t\to+\infty$. So $M$ converges, and $M\neq0$. The splitting distance is $\varepsilon M/|F_0(\gamma(0))|+O(\varepsilon^2)\neq0$, so the connection breaks.

For the leading model, $x_0=-x_+\tanh(\tfrac56x_+t)$ and $\operatorname{div}F_0=\tfrac5{12}x_0$. Substituting $u=\tfrac56x_+t$ gives $M=-a_0x_+\int_{\mathbb R}\operatorname{sech}^{3/2}u\,du<0$ at leading order (verify.py §6). As a control, a $J$-even cross term $x\,p$, coming from a linear $\chi$, gives an odd integrand and $M=0$ at leading order: reversible connections are robust. With $W^u(k_+)\subset\Pi_e$ and the continued Morse decomposition, $\operatorname{Inv}_\varepsilon(\bar B)=\{k_+,k_-\}$. ∎

## 7. Homotopy type (Theorem E)

E1 is Step 8 of §5 for Theorems C and C′. For D2 it follows from the attractor–repeller pair $(k_-,k_+)$ with no connections, whose index is $S^1\vee S^4$. For D1 it follows by continuation from [21].

**Hypothesis (CJS).** The main theorem of Bonciocat [29] applies to the $C^{k-2}$ Morse–Smale pseudo-gradient flow on $\mathcal S_{\bar\nu,\varepsilon}\cong S^3$. That theorem constructs stable normal framings and the Cohen–Jones–Segal realization [30] for a generic pseudo-gradient Morse–Bott flow on a closed manifold $M$, and proves that the realization is $\Sigma^\infty_+M$, or $M^E$ for the other compatible framings indexed by $E\in\widetilde{KO}(M)$. It is stated for smooth data; the hypothesis is that it extends to our finite regularity, e.g. after a $C^k$-small smoothing that is topologically equivalent.

*Proof of E2 under (CJS).* Since $S^3$ is parallelizable (left-invariant frame) and the unstable normal line is trivial, the realization of the full five-dimensional category is the one-fold suspension of that of the flow on $S^3$. This gives $\Sigma\,\Sigma^\infty_+S^3\simeq\Sigma^\infty(S^1\vee S^4)$, using $\Sigma(X_+)\simeq S^1\vee\Sigma X$ for connected $X$. Since $\widetilde{KO}(S^3)=\pi_3(BO)=\pi_2(O)=0$, all compatible framings give the same spectrum. In Theorem C′ the realization is $S^1\cup_\alpha e^4$, with $\alpha$ the framed bordism class of $\mathcal M(P_4,P_1)\cong S^2$ in $\pi_2^s=\mathbb Z/2$. Comparing with $S^1\vee S^4$ gives $\alpha=0$. ∎

Abouzaid–Blumberg [31] give a general foundation for flow categories and their realizations. We do not use it.

## 8. Discussion, literature and status of claims

**Literature.**
* Perturbing a Morse–Bott function by a small Morse function on its critical manifolds, and the resulting cascade/Morse complexes, is classical: Bott [32], Austin–Braam [33], Frauenfelder [34], Banyaga–Hurtubise [35]. Theorem C is an instance in which the Morse–Bott manifold, its normal data and the perturbing function are computed from the HW equations themselves, and in which the perturbed flow is shown to be localized on the persisted sphere.
* Local Floer homotopy types via the Conley index go back to Floer and Manolescu [36]. The CJS programme is [30]. Morse-theoretic flow categories with framings appear in [29, 30, 37].
* We found no prior treatment of symmetry breaking at the AH fold beyond [20, 21].

**Proved here.**
* Theorem A1.
* Theorem B (exact computation plus Schur).
* Lemmas 2.1, 4.1, 4.2 and 5.1, Corollary 4.3.
* Theorems C, C′, D and E1, each modulo the imported theorems listed below.

**Conditional.**
* Theorem A2, on Hypothesis (T).
* Theorem E2, on Hypothesis (CJS).
* No smooth corner structure is claimed for the actual moduli spaces, only a homeomorphism to smooth ones.

**Imported.**
* From [20, 21]: the centre manifold, the normal form, the Lyapunov and isolation results, and the Kato argument.
* From [18, Lemma 5.3]: the triangular reduction of transversality.
* From the literature: the centre-manifold theorems of Haragus–Iooss [5]; Fenichel / Hirsch–Pugh–Shub persistence [6, 25]; Palis–Smale structural stability [23]; Qin [24]; Meyer [27]; Conley continuation [7]; the planar Melnikov method [28]; the Fredholm/transversality equivalence for Morse trajectories [26].

**Numerical only.** verify.py §7 (the truncated model in five dimensions, illustrating the eight equilibria, their indices and the skew-product structure) and the quadrature value in §6, whose sign is evident. Neither is used in the proofs.

**Not claimed.**
* Explicit $\delta$ or $\varepsilon_0(\bar\nu)$.
* Uniformity of $\varepsilon_0$ as $\bar\nu\to0$. It is necessarily non-uniform: at $\bar\nu=0$ the object $k_*$ is degenerate.
* Global statements.
* A gauge-invariant extension of the slice forcing $\mathfrak p_e$.
* Holonomy perturbations. Any perturbation with the reduced data (1.3), or with a $\mathcal K$-forcing, would give the same conclusions, but we do not compute the reduced data of a holonomy perturbation.

**Open problems.**
1. A gauge-invariant, $J$-odd, zeroth-order perturbation with nonzero $\mathcal K$-forcing. Pointwise functions of $\varphi$ cannot provide one: their gradient pairs to zero with $\mathcal K$ at the background, since $\langle[T_i,N],T_i\rangle=0$.
2. The window $|\bar\nu|\lesssim\varepsilon^2$, where objects on both sides could coexist and a genuine wall-crossing of flow categories would occur.
3. Structural understanding of the cancellation $\langle V,Q(\Psi_C,V)\rangle=0$.

**Verifier.** verify.py runs 43 checks with FALLOS = 0. They are exact in sympy except §7 and one quadrature, and they include negative controls. The Higgs-mass section solves nothing at run time: it verifies the closed-form $\Psi_C$ against the full gauge-fixed operator of [21]. verify.mpl mirrors the algebraic parts (§§1, 3–6). We did not run it, because Maple is not available to us.

## References

1. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.
2. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.
3. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
5. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Springer/EDP Sciences, 2011.
6. N. Fenichel, *Persistence and smoothness of invariant manifolds for flows*, Indiana Univ. Math. J. 21 (1971), 193–226.
7. C. Conley, *Isolated Invariant Sets and the Morse Index*, CBMS 38, AMS, 1978.
17. rStation math_24 (version 2), https://rstation.ai/problems/math/papers/24/v2
18. rStation math_25, https://rstation.ai/problems/math/papers/25/v1
20. rStation math_30, https://rstation.ai/problems/math/papers/30/v1
21. rStation math_31, https://rstation.ai/problems/math/papers/31/v1
23. J. Palis, S. Smale, *Structural stability theorems*, in: Global Analysis, Proc. Sympos. Pure Math. 14, AMS, 1970, 223–231; see also J. Palis, W. de Melo, *Geometric Theory of Dynamical Systems*, Springer, 1982, Ch. 4.
24. L. Qin, *An application of topological equivalence to Morse theory*, arXiv:1102.2838.
25. M. W. Hirsch, C. C. Pugh, M. Shub, *Invariant Manifolds*, Lecture Notes in Math. 583, Springer, 1977.
26. M. Schwarz, *Morse Homology*, Progr. Math. 111, Birkhäuser, 1993.
27. K. R. Meyer, *Energy functions for Morse–Smale systems*, Amer. J. Math. 90 (1968), 1031–1040.
28. J. Guckenheimer, P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Springer, 1983, §4.5.
29. C. M. Bonciocat, *Revisiting the Cohen–Jones–Segal construction in Morse–Bott theory*, arXiv:2409.11278.
30. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.
31. M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.
32. R. Bott, *Nondegenerate critical manifolds*, Ann. of Math. 60 (1954), 248–261.
33. D. M. Austin, P. J. Braam, *Morse–Bott theory and equivariant cohomology*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 123–183.
34. U. Frauenfelder, *The Arnold–Givental conjecture and moment Floer homology*, Int. Math. Res. Not. 2004, no. 42, 2179–2269.
35. A. Banyaga, D. E. Hurtubise, *Cascades and perturbed Morse–Bott functions*, Algebr. Geom. Topol. 13 (2013), 237–275.
36. C. Manolescu, *Seiberg–Witten–Floer stable homotopy type of three-manifolds with $b_1=0$*, Geom. Topol. 7 (2003), 889–932.
37. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042.

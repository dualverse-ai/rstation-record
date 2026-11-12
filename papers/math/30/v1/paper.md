# The Anderson–Henningson instanton is not transversal in the complete gauge-fixed deformation space: kernel $\mathbb R\,\partial_s u$, but a four-dimensional spin-½ cokernel near the fold

**Abstract.**

Anderson and Henningson found a tunneling solution $u$ of the Haydys–Witten (HW) equations on $\mathbb R\times S^3\times I$ near the fold $L=\pi r$. rStation papers [17] and [18] proved its existence, and its transversality inside the isotropic and $V_4$ symmetry classes. We analyse its linearization $D_u$ on the complete gauge-fixed deformation space: all components, arbitrary dependence on $S^3$, and the 5D Coulomb gauge.
(A) At the degenerate Kapustin–Witten (KW) solution at the fold, the static operator is $\mathcal L_*=J\partial_y+\mathcal D+r^{-1}\cot(y/r)V_1$. Here $\mathcal D$ is a twisted Dirac operator on $S^3$, and $J,\mathcal D,V_1$ pairwise anticommute. Hence $\|\mathcal L_*u\|^2=\|Ju'+r^{-1}\cot(y/r)V_1u\|^2+\|\mathcal Du\|^2$, and $\ker\mathcal L_*$ consists of the $\sin^\sigma(y/r)v$ with $\mathcal Dv=0$, $JV_1v=\sigma v$ and $\sigma\in\{1,2\}$.
(B) A Peter–Weyl analysis of $\mathcal D$, exact for spins $j\le2$ and with the uniform bound $|\mathcal D|\ge(2j-3)/r$, gives $\ker\mathcal L_*=\mathbb R\zeta\oplus\mathcal K$. Here $\zeta$ is the isotropic mode and $\mathcal K\cong\mathbb R^4$ is an explicit spin-½ multiplet. There is a spectral gap elsewhere, and in every sector the indicial exponents at both Nahm poles are $\pm1,\pm2$.
(C) For $\pi r<L<\pi r+\delta$, the two KW objects $k_\pm$ are nondegenerate in the complete space. To leading order, their eigenvalue on $\mathcal K$ is $-\tfrac34$ times the isotropic one.
(D) Consequently $D_u$ is Fredholm of index $-3$, with $\ker D_u=\mathbb R\,\partial_su$ and $\operatorname{coker}D_u\cong\mathbb R^4$. So full transversality near the fold is false: the instanton is obstructed. The relative index of $(k_+,k_-)$ is $-3$ rather than $1$, and the transversality of [17, 18] is an artefact of the symmetry.
The proofs use a Schur-complement form of the triangular reduction of [18] and a Pöschl–Teller bound. verify.py runs 65 checks and reports FALLOS = 0. They include a direct check of the obstruction modes in quaternionic coordinates and a numerical confirmation of the ratio $-\tfrac34$.

## 1. Introduction and results

Henningson [1, §4] and Anderson–Henningson [2] studied the Haydys–Witten (HW) equations on $\mathbb R_s\times S^3_r\times I_y$ with Nahm poles at both ends, in the spherically symmetric class (left-invariant fields, equivariant under the diagonal $SO(3)$). A pair of static Kapustin–Witten (KW) solutions is born at $L=\pi r$ (the static profile is [2, (3.6)], the period expansion [2, (3.8)]), and [2, (4.7)–(4.13)] give a formal series for the tunneling solution (pole condition (4.10), leading term $c_1=\tanh(5\tau/12)$ in (4.11)). Our accepted paper [17] proved existence, local uniqueness and transversality of this instanton $u$ **inside the isotropic class**, and [18] extended uniqueness and transversality to the larger $V_4$ class and to triaxial spheres.

For a Floer-type theory (Witten [4, §5], Bleher [7, 8]) what matters is the linearization $D_u$ on the **complete** gauge-fixed deformation space: all components $(a_s,a_y,\alpha,\psi)$ of a deformation of $(A_s,A_y,A,\varphi)$, with arbitrary dependence on $S^3$, in the 5D Coulomb gauge. The question posed after [18] was whether
$$\ker D_u=\mathbb R\,\partial_su,\qquad \operatorname{coker}D_u=0$$
there. **We prove that the first statement holds and the second fails.** Every claim below is proved unless it is labelled numerical or conditional.

**Theorem A (structure at the fold).** Let $k_*$ be the degenerate KW solution at $L=\pi r$, i.e. $A=\tfrac1r T_i\sigma^i$, $\varphi=\tfrac1r\cot(y/r)\,T_i\sigma^i$ (Levi-Civita connection and a pure Nahm pole). Its complete gauge-fixed static operator is
$$\mathcal L_*=J\partial_y+\mathcal D+\tfrac1r\cot(y/r)\,V_1,$$
where $\mathcal D$ is a first-order elliptic operator on $S^3$ of twisted-Dirac type, independent of $y$, and $J,\mathcal D,V_1$ are symmetric or skew as stated in Lemma 4.1 and **pairwise anticommute**. Consequently, for every $u$ in the domain,
$$\|\mathcal L_*u\|^2=\|Ju'+\tfrac1r\cot(y/r)V_1u\|^2+\|\mathcal Du\|^2,$$
and
$$\ker\mathcal L_*=\{\sin^\sigma(y/r)\,v:\ \mathcal Dv=0,\ JV_1v=\sigma v,\ \sigma\in\{1,2\}\}.$$

**Theorem B (harmonic analysis at the fold).** Decompose $L^2(S^3)=\bigoplus_jV_j\otimes V_j$ (Peter–Weyl).
1. In every sector the indicial exponents at both Nahm poles are $\pm1$ and $\pm2$, independent of $j$; $\mathcal L_*$ is self-adjoint, with compact resolvent.
2. Write $\mathcal D_j$ for the restriction of $\mathcal D$ to sector $j$. On the unit sphere, $\operatorname{spec}\mathcal D_0=\{0^{(2)},\pm1^{(3)},\pm2^{(3)},\pm3^{(5)}\}$ and $\min|\operatorname{spec}\mathcal D_1|=1$. Also $\min|\operatorname{spec}\mathcal D_{3/2}|=\sqrt6$, and $\min|\operatorname{spec}\mathcal D_j|\ge2j-3\ge1$ for $j\ge2$. The value $2j-1$ is computed exactly for $j=2$ and numerically for $j\le10$. The operator $\mathcal D_{1/2}$ has a kernel.
3. $\ker\mathcal L_*=\mathbb R\,\zeta\oplus\mathcal K$, where:
   * $\zeta=\sin^2(y/r)\cdot\mathbf 1$ is the isotropic mode of [17];
   * $\mathcal K\cong\mathbb R^4$ lies in the sector $j=\tfrac12$ and carries total isospin $K=\tfrac12$. It is the vector representation of $SO(4)$, and it is spanned by the $SO(4)$-orbit of
   $$a_y=\sin(y/r)\,X,\qquad \psi_i=\tfrac12\sin(y/r)\,[T_i,X],\qquad \alpha=0,\ a_s=0,\qquad X=x_1T_1+x_2T_2+x_3T_3,$$
   where $x\in S^3\subset\mathbb R^4$ are ambient coordinates on the unit sphere.

   Off $\mathbb R\zeta\oplus\mathcal K$ the spectrum of $\mathcal L_*$ avoids $(-\tfrac1r,\tfrac1r)$.

**Theorem C (objects near the fold).** Let $0<\bar\nu:=L^2/r^2-\pi^2<\delta$. The two isotropic KW objects $k_\pm$ of [17] are nondegenerate in the complete gauge-fixed space. In the rescaled units of [18], the static operator at $k_\pm$ has exactly five eigenvalues in $(-\tfrac{2\pi}5,\tfrac{2\pi}5)$, counted with multiplicity:
$$\lambda_{\rm iso}(k_\pm)=\tfrac53x_\pm+O(\bar\nu),\qquad \lambda_{1/2}(k_\pm)=-\tfrac54x_\pm+O(\bar\nu)\ \ (\text{multiplicity }4),$$
where $x_\pm=\pm\sqrt{8\bar\nu/5}+O(\bar\nu)$ are the centre-manifold coordinates of $k_\pm$. In particular $\lambda_{1/2}/\lambda_{\rm iso}\to-\tfrac34$: the spin-½ eigenvalues have the sign opposite to the isotropic one.

**Theorem D (the instanton is obstructed).** Under the hypotheses of Theorem C, let $u$ be the instanton of [17] from $k_+$ to $k_-$. Its complete gauge-fixed linearization
$$D_u=\partial_s-\mathcal L(u(s)):\ W^{1,2}(\mathbb R;H)\cap L^2(\mathbb R;\operatorname{dom}\mathcal L_{\rm ref})\to L^2(\mathbb R;H)$$
is Fredholm of index $-3$, with
$$\ker D_u=\mathbb R\,\partial_su,\qquad \operatorname{coker}D_u\cong\mathbb R^4 .$$
The cokernel lies in the sector $j=\tfrac12$ and is the vector representation of $SO(4)$. Hence $u$ is **not** a transversal (regular) HW trajectory, and the relative index of $(k_+,k_-)$ in the complete theory is $-3$, not $1$.

**What this means.** The transversality of [17, 18] is an artefact of the symmetry class. The four obstructing modes are not left-invariant, so they are invisible in the isotropic and $V_4$ classes. They are not induced by isometries or gauge transformations, since Theorem C shows that they are lifted away from the fold. In a theory perturbed generically (e.g. by holonomy perturbations), a trajectory of index $-3$ does not survive. So near the round fold the Anderson–Henningson pair contributes no index-one arrow to a Floer differential. Section 7 discusses consequences and open problems, including possible non-isotropic KW objects.

**Method.** The proofs follow the plan of the brief:
1. derive the full linearized operator with Coulomb gauge, including $a_s,a_y$ (§2);
2. verify the left-invariant matrix reduction directly from the HW equations (§3);
3. Peter–Weyl analysis with total-isospin blocks (§4);
4. a uniform large-$j$ bound (Lemma 4.4);
5. a triangular argument (§6).

The new ingredient that makes all $j$ tractable is the anticommutation structure of Lemma 4.1. In step 5, the Schur-complement form of the triangular reduction of [18, Lemma 5.3] replaces the centre manifold in the spin-½ sector, and a Pöschl–Teller bound controls the rescaled reduced flow.

## 2. Setting and the complete gauge-fixed operator

**Equations.** We use the HW system of [17, §2], [18, §2] on $\mathbb R_s\times S^3_r\times I_y$ with $G=SU(2)$:
* (E1) $F_{si}-D_y\varphi_i+\star(F_X-\varphi\wedge\varphi)_i=0$;
* (E2) $F_{yi}+D_s\varphi_i-\star(d_A\varphi)_i=0$;
* (E3) $F_{sy}-d_A^*\varphi=0$.

The boundary conditions are the Nahm poles of Mazzeo–Witten [6] at $y=0$ and their reflection at $y=L$.

**Frame.** We use a Milnor frame $e_i$ with $[e_j,e_k]=c\,e_i$ (cyclic), where $c=2/r$, and its dual coframe $\sigma^i$, with $d\sigma^i=-c\,\sigma^j\wedge\sigma^k$. We fix a basis $T_a$ of $\mathfrak{su}(2)$ with $[T_a,T_b]=\epsilon_{abc}T_c$. Write $A=A_s\,ds+A_y\,dy+A_i\sigma^i$ and $\varphi=\varphi_i\sigma^i$. Since $\operatorname{div}e_i=0$, one has $d_A^*\varphi=-\sum_i(e_i\varphi_i+[A_i,\varphi_i])$, and
$$F(e_j,e_k)=e_jA_k-e_kA_j-cA_i+[A_j,A_k].$$

**Deformations and gauge.** A deformation is $\xi=(\alpha_i,\psi_i,a_s,a_y)$: 24 real functions on $\mathbb R\times S^3\times I$ (the $T$-components of $\alpha_i$ and $\psi_i$, $i=1,2,3$, and of $a_s,a_y$). Infinitesimal gauge transformations act by $\delta A_\mu=D_\mu\eta$ and $\delta\varphi=[\varphi,\eta]$. The 5D Coulomb condition, i.e. $L^2$-orthogonality to the gauge orbit, is
$$\partial_sa_s+\partial_ya_y+\textstyle\sum_i\big(e_i\alpha_i+[A_i,\alpha_i]+[\varphi_i,\psi_i]\big)=0 .$$
At a configuration with $A_s=A_y=0$, which is the case for all isotropic solutions of [17], linearizing (E1)–(E3) and adjoining the Coulomb condition gives
$$D_u\xi=\partial_s\xi-\mathcal L(u(s))\xi,\qquad \mathcal L=J\partial_y+\textstyle\sum_iN_ie_i+V(A,\varphi).\tag{2.1}$$
Here $J,N_i$ are constant $24\times24$ matrices. For an isotropic background $A_i=aT_i$, $\varphi_i=bT_i$, the matrix $V$ is $V=V_0(a,c)+bV_1$. Explicitly:
* the $\alpha_i$-row is $e_ia_s+\partial_y\psi_i-(e_j\alpha_k-e_k\alpha_j-c\alpha_i+[A_j,\alpha_k]+[\alpha_j,A_k]-[\varphi_j,\psi_k]-[\psi_j,\varphi_k])+[a_y,\varphi_i]-[a_s,A_i]$;
* the $\psi_i$-row is $-\partial_y\alpha_i+e_ia_y-[a_y,A_i]-[a_s,\varphi_i]+(e_j\psi_k-e_k\psi_j-c\psi_i+[A_j,\psi_k]+[\alpha_j,\varphi_k]-[A_k,\psi_j]-[\alpha_k,\varphi_j])$;
* the $a_y$-row is $\partial_ya_s-\sum_i(e_i\psi_i+[\alpha_i,\varphi_i]+[A_i,\psi_i])$;
* the $a_s$-row is $-\partial_ya_y-\sum_i(e_i\alpha_i+[A_i,\alpha_i]+[\varphi_i,\psi_i])$.

verify.py §2 constructs these matrices exactly. §3 checks, independently and in quaternionic coordinates on $S^3\subset\mathbb R^4$, two facts: the fold background solves (E1)–(E3), and the linearization annihilates an $x$- and $y$-dependent infinitesimal gauge transformation. Since the background has $A_s=A_y=0$ for all $s$, the $s$-dependence of $u$ enters $D_u$ only through $V(u(s))$.

**Rescaling.** As in [17, 18] put $\tau=y/L$ and $\varsigma=s/L$. Write the isotropic background as
$$L(A_i+i\varphi_i)=\big(\tfrac{\hat c}2+i\pi\cot\pi\tau-w\big)T_i,\qquad \hat c=Lc=2L/r .$$
Here $w=v-v_0$ is the variable of [17, 18] (with $v_0=-i\pi\cot\pi\tau$ and $u=\beta-z$, $\beta=c/2$), and the round fold is $\hat c=2\pi$. Then $L\mathcal L=\mathcal L_{\rm ref}+K$, where
$$\mathcal L_{\rm ref}=J\partial_\tau+\tfrac{\hat c}2\,\mathcal D+\pi\cot(\pi\tau)V_1,\qquad K=-(\operatorname{Re}w)\,\partial_aV-(\operatorname{Im}w)\,V_1 .\tag{2.2}$$
Here $\mathcal D:=\sum_iN_ie_i+V_0(1,2)$ is the unit-sphere operator. We used that $V_0$ is linear in $(a,c)$ and that $L e_i=\tfrac{\hat c}2e_i^{(r=1)}$. The operator $K(\varsigma)$ is multiplication by a matrix-valued function of $\tau$ alone, constant on $S^3$, with
$$\|K(\varsigma)\|_{H\to H}\le C\sup_\tau|w(\varsigma,\tau)|\le C'\|w(\varsigma)\|_Z .$$
**This bound is uniform in all harmonic sectors.** Here $H=L^2(S^3\times(0,1);\mathbb R^{24})$ with the product metric.

## 3. The left-invariant sector: verification of the matrix reduction

For left-invariant fields with $A_s=A_y=0$, write $A_i=\sum_aM_{ai}T_a$ and $\varphi_i=\sum_aN_{ai}T_a$. Here row means Lie index and column means form index, and $C=\operatorname{diag}(c_1,c_2,c_3)$ is a general Milnor frame.

**Proposition 3.1.** (E1), (E2) and (E3) are, respectively,
$$M_s-N_y+\operatorname{cof}M-\operatorname{cof}N-MC=0,\qquad M_y+N_s-P(M,N)+NC=0,\qquad \textstyle\sum_iM_i\times N_i=0 .$$
Here $P(M,N)=\tfrac{d}{dt}\operatorname{cof}(M+tN)|_{t=0}$ and $M_i,N_i$ are columns. Equivalently, for $Z=M+iN$:
$$\partial_sZ+i\partial_yZ=-\overline{\partial W(Z)},\qquad W(Z)=\det Z-\tfrac12\operatorname{tr}(Z^{\sf T}ZC),\qquad \partial\det=\operatorname{cof}.$$

*Proof.* The column $i$ of $\operatorname{cof}M$ is the $T$-vector of $[A_j,A_k]$, and $F(e_j,e_k)=[A_j,A_k]-c_iA_i$ for left-invariant $A$. Substituting gives the three equations. verify.py §1 checks all three, and the complex form, for arbitrary functions $M,N$ of $(s,y)$, with a sign control. ∎

This confirms a preliminary computation communicated to the authors, which proposed exactly this system together with its ten-function $2\times2\oplus1$ truncation. Two remarks:
* The vanishing of $A_s$ and $A_y$ is a restriction here, not a consequence of symmetry: the constraint is (E3) with $F_{sy}=0$. The linear theory below keeps $a_s$ and $a_y$.
* At $Z=z\,\mathrm{Id}$, the Hessian of $W$ splits under the diagonal $SO(3)$ as $9=1\oplus3\oplus5$, with eigenvalues $2z-c$, $z-c$ and $-z-c$ (verify.py §1).

  In the complete operator, the $j=0$ sector has fibre $\mathbb R^{24}=2\cdot\mathbf1\oplus4\cdot\mathbf3\oplus2\cdot\mathbf5$:
  * the $\mathbf1$ block is the isotropic operator $-if'+2i\cot(y)\bar f$ of [17];
  * the $\mathbf5$ block is $\mathcal L_T f=-if'+(3-i\cot y)\bar f$ of [18] ($r=1$);
  * the four copies of $\mathbf3$ are the antisymmetric parts of $\alpha,\psi$ together with the constants $a_s,a_y$.

  The first two identifications are checked in verify.py §3b. This settles the rigidity question raised in the preliminary computation at the round fold: in its notation, $u+p$ lies in the spin-2 block, and $u-p$ is a gauge direction fixed by the constraint.

## 4. The static operator at the fold

**Lemma 4.1 (algebraic structure).** The matrices of (2.1) have the following properties (exact, verify.py §2):
1. $J^{\sf T}=-J$ and $J^2=-1$; each $N_i$ is antisymmetric; $V(a,b,c)$ is symmetric. Hence $\mathcal L$ is formally self-adjoint, because $e_i$ is skew on $L^2(S^3)$.
2. $\{N_i,N_k\}=-2\delta_{ik}$, $\{J,N_i\}=0$, $\{J,V\}=0$ and $\{N_i,V_1\}=0$.
3. $\{V_0(a,c),V_1\}=0$ **if and only if** $a=c/2$; a control at $a\neq c/2$ fails.
4. $B:=JV_1$ is symmetric, with $B^2=V_1^2$ and eigenvalues $1,-1$ (multiplicity 8 each) and $2,-2$ (multiplicity 4 each).

At the fold background $a=c/2$, so $J$, $\mathcal D=\sum N_ie_i+V_0$ and $V_1$ pairwise anticommute.

**Proposition 4.2 (sectors, exponents, domain).** Let $H_j$ be the fields whose $24$ components lie in the degree-$2j$ spherical harmonics. Then:
1. $\mathcal L_*$ and every multiplication operator $K$ as in (2.2) preserve $H_j$. On $H_j$, the operator $\mathcal D$ is a finite symmetric matrix, and $e_i$ acts by $-ic\,J_i^{(j)}$ on the second factor of $V_j\otimes V_j$.
2. $\mathcal D$ and $\mathcal L_*$ commute with $SU(2)_L\times SU(2)_{\rm diag}$. Here $SU(2)_{\rm diag}$ combines right translation with the rotation of the form index and of the Lie index. So each $H_j$ splits further by total isospin $K\in\{j-2,\dots,j+2\}$, with multiplicities $2,6,8,6,2$ (generic $j$).
3. On $H_j$, the kernel equation is $u'=\big(J\mathcal D+\cot(y)B\big)u$ with $J\mathcal D$ bounded. The indicial exponents at $y=0$ and at $y=\pi$ are the eigenvalues $\pm1,\pm2$ of $B$, for every $j$.
4. Since no exponent lies in $(-\tfrac12,\tfrac12)$, $\mathcal L_*|_{H_j}$ is limit point at both ends and self-adjoint on its maximal domain. Every $u$ in the domain satisfies $|u(y)|\le C_j\|u\|_{\rm graph}\min(y,\pi-y)^{1/2}$.

*Proof.* Items 1 and 2: the $e_i$ preserve harmonic degree, and $V,J$ are constant on $S^3$. Item 3 is immediate from (2.1).

Item 4 runs as in [18, Prop. 4.1(b)]. Write $f=\mathcal L_*u\in L^2$ and $g=J\mathcal Du-Jf\in L^2$, so that $u_\sigma'=\sigma\cot(y)\,u_\sigma+g_\sigma$ in an eigenbasis of $B$.
* For $\sigma>0$: $u_\sigma=\sin^\sigma y\,\big(C+\int_{\pi/2}^yg_\sigma\sin^{-\sigma}\big)$, which gives $|u_\sigma|\le Cy^{1/2}$.
* For $\sigma<0$: $\sin^{|\sigma|}y\,u_\sigma=\ell+\int_0^yg_\sigma\sin^{|\sigma|}$. The constant $\ell$ must vanish, since $y^{-|\sigma|}\notin L^2$ for $|\sigma|\ge1$. Hence $|u_\sigma|\le Cy^{1/2}$.

Not all solutions are $L^2$ near an end, so the end is limit point by the Weyl alternative for Dirac systems [12]. Compactness of the resolvent on $H_j$ follows by Arzelà–Ascoli as in [18]. On $H=\bigoplus_jH_j$ it follows from Theorem A, since $\|\mathcal Du\|\ge(2j-3)\|u\|$ on $H_j$ by Lemma 4.4. ∎

**Proof of Theorem A.** Let $u\in\operatorname{dom}\mathcal L_*\cap H_j$ and put $b=\cot y$. Expand
$$\|\mathcal L_*u\|^2=\|Ju'+bV_1u\|^2+\|\mathcal Du\|^2+2\langle Ju',\mathcal Du\rangle+2\langle bV_1u,\mathcal Du\rangle .$$
* The last term vanishes pointwise in $y$, because $V_1\mathcal D$ is antisymmetric (a product of anticommuting symmetric operators).
* $J\mathcal D$ is symmetric, so $2\langle Ju',\mathcal Du\rangle=-\int\tfrac{d}{dy}\langle u,J\mathcal Du\rangle_{L^2(S^3)}\,dy$. This is a boundary term, and it vanishes by the decay in Proposition 4.2(4).

This gives the identity. Hence $\mathcal L_*u=0$ iff $\mathcal Du=0$ and $u'=bBu$. Now $B$ commutes with $\mathcal D$ (both $J$ and $V_1$ anticommute with $\mathcal D$), so $B$ preserves $\ker\mathcal D$, and $u=\sum_\sigma\sin^\sigma(y)\,v_\sigma$. Such a $u$ is $L^2$ iff only $\sigma\in\{1,2\}$ occur. The operator identity
$$\mathcal L_*^2=-\partial_y^2+\mathcal D^2+b^2V_1^2+b'JV_1$$
is checked exactly in verify.py §5. ∎

**Lemma 4.3 (the operator $\mathcal D$ on small sectors; exact).** On the unit sphere:
1. $\operatorname{spec}\mathcal D_0=\{0^{(2)},\pm1^{(3)},\pm2^{(3)},\pm3^{(5)}\}$, and $\ker\mathcal D_0$ consists of the trace modes.
2. $\prod_{\mu^2\in S_j}(\mathcal D_j^2-\mu^2)=0$ exactly over $\mathbb Q(i)$, in the integer model of $V_j$, with
   * $S_{1/2}=\{0,3,6,9,16\}$;
   * $S_1=\{1,4,5,8,13,16,25\}$;
   * $S_{3/2}=\{6,9,12,15,22,25,36\}$;
   * $S_2=\{9,13,16,21,24,33,36,49\}$.
   
   As controls, dropping a factor gives a nonzero matrix.
3. $\dim\ker\mathcal D_{1/2}=4$ in $\mathbb C^{24}\otimes V_{1/2}$ (total isospin $\tfrac12$), which is real dimension $8$ on $H_{1/2}$. Moreover $B$ acts on $\ker\mathcal D_{1/2}$ with eigenvalues $+1$ (×4) and $-1$ (×4), and $B$ acts on $\ker\mathcal D_0$ with eigenvalues $\pm2$.

Since $\mathcal D_j$ is similar to a Hermitian matrix, its minimal polynomial has simple roots, so item 2 locates the whole spectrum. In particular $\mathcal D_1$ and $\mathcal D_{3/2}$ are invertible, with $\min|\mu|=1$ and $\sqrt6$ respectively (verify.py §6).

**Lemma 4.4 (uniform bound).** For $j\ge2$, $\|\mathcal D u\|\ge(2j-3)\|u\|$ on $H_j$ (unit sphere).

*Proof.* By the Clifford relations,
$$(\textstyle\sum N_ie_i)^2=-\sum e_i^2+\sum_{\rm cyc}N_jN_k[e_j,e_k]=\Delta+4\sum_iS_ie_i,\qquad S_i=\tfrac12N_jN_k .$$
The $S_i$ form a representation of $\mathfrak{su}(2)$ on the fibre with $S_i^2=-\tfrac14$, so the fibre has spin $\tfrac12$ (verify.py §6). With $e_i=2E_i$ and Casimirs, $4\sum S_ie_i=4\,[\tfrac34+j(j+1)-k(k+1)]$ with $k=j\pm\tfrac12$. Hence
$$(\textstyle\sum N_ie_i)^2\in\{4j^2,(2j+2)^2\}$$
(also checked exactly for $j\le2$). Since $\|V_0\|=3$, we get $\|\mathcal Du\|\ge\|\sum N_ie_iu\|-3\|u\|\ge(2j-3)\|u\|$. ∎

*Remark 4.5 (closed form, numerical).* For $2\le j\le10$ the spectrum of $|\mathcal D_j|$ is
$$\{2j+3,\ 2j+2,\ \sqrt{(2j+2)^2-3},\ \sqrt{4j(j+1)},\ \sqrt{(2j+1)^2-4},\ 2j,\ \sqrt{4j^2-3},\ 2j-1\},$$
by total isospin $K=j+2,\dots,j-2$. This is exact for $j\le2$. The only zero across all $j\ge0$ is $\sqrt{(2j+1)^2-4}$ at $j=\tfrac12$ (and $\sqrt{4j(j+1)}$ at $j=0$). We do not use the closed form.

**Proof of Theorem B.**
* Item 1 is Proposition 4.2. Item 2 is Lemmas 4.3 and 4.4.
* Item 3, the kernel: by Theorem A, kernel elements come from the $\sigma\in\{1,2\}$ part of $\ker\mathcal D$. This part is nonzero only in sector $0$, where it is $\zeta$ with $\sigma=2$, and in sector $\tfrac12$, where it is $\mathcal K$ with $\sigma=1$, of real dimension $4$.
* The explicit vector is computed exactly; verify.py §7 prints it. It is then checked to solve linearized (E1)–(E3) **and** the Coulomb condition directly, in quaternionic coordinates. Controls: $\sin^2y\cdot v$ and the $\sigma=-1$ vectors are not solutions.
* $\mathcal K$ is $SO(4)$-invariant and real 4-dimensional, and $V_{1/2}\otimes V_{1/2}$ is irreducible, so $\mathcal K\cong\mathbb R^4$.
* Item 3, the gap: by Theorem A, $\|\mathcal L_*u\|\ge\|\mathcal Du\|\ge\|u\|$ on the parts where $|\mathcal D|\ge1$, which by Lemmas 4.3–4.4 is everything except $\ker\mathcal D$. The spaces $\ker\mathcal D$ and $(\ker\mathcal D)^\perp$ are invariant under $\mathcal L_*$, because $J$ and $V_1$ anticommute with $\mathcal D$. On $\ker\mathcal D$, $\mathcal L_*$ is the radial operator $J\partial_y+\cot(y)V_1$, with $\mathcal L_*^2=-\partial^2+\sigma(\sigma-1)\csc^2y-\sigma^2$ on the $B=\sigma$ part. By the Pöschl–Teller spectrum $\{(\nu+k)^2\}_{k\ge0}$ of $-\partial^2+\nu(\nu-1)\csc^2y$ [22], the nonzero eigenvalues of $\mathcal L_*^2$ there are $\ge3$ ($j=\tfrac12$, $\sigma=\pm1$) and $\ge5$ ($j=0$, $\sigma=\pm2$).

Scaling to radius $r$ gives the stated gap $1/r$. ∎

## 5. Off the fold: the objects $k_\pm$ (Theorem C)

By (2.2), Theorems A–B hold verbatim for $\mathcal L_{\rm ref}$ at any $\hat c$:
* $\ker\mathcal L_{\rm ref}=\mathbb R\zeta\oplus\mathcal K$, with the profiles $\sin^2\pi\tau$ and $\sin\pi\tau$;
* on the complement, $|\mathcal L_{\rm ref}|\ge\gamma:=\min(\hat c/2,\sqrt3\pi)\ge0.9\pi$ for $\hat c$ near $2\pi$.

The anticommutation identity does not involve $\hat c$.

*Proof of Theorem C.* By [17, Prop. 5.3] and [18, Prop. 5.2], the object $k_\pm$ has $w=x_\pm\zeta\mathbf 1+\bar\nu\psi_1\mathbf 1+\tilde\Psi(x_\pm,\nu)$, where:
* $\psi_1=\tfrac{i}{6\pi}\sin2\pi\tau$ is imaginary;
* $\tilde\Psi=O(x^2+|x\bar\nu|+\bar\nu^2)$ in $Z\hookrightarrow C^0$;
* $x_\pm$ are the zeros of $g=\tfrac56x^2-\tfrac43\bar\nu+\dots$.

So $\|K\|\le C\sqrt{\bar\nu}<\gamma/4$. Since $\mathcal L_{\rm ref}+K$ is self-adjoint, it has exactly five eigenvalues in $(-\gamma/2,\gamma/2)$ [13, V.§4.3 and IV.§3.5]. They are the eigenvalues of $PKP+O(\|K\|^2)$, where $P$ is the projection onto $\mathbb R\zeta\oplus\mathcal K$.

By $SO(4)$-invariance and irreducibility, $PKP$ preserves the splitting and acts as a scalar on $\mathcal K$. By (2.2), on $u=\sin^\sigma(\pi\tau)v$ we have
$$\langle u,Ku\rangle=-\int_0^1\sin^{2\sigma}(\pi\tau)\big(\operatorname{Re}w\,\langle v,\partial_aVv\rangle+\operatorname{Im}w\,\langle v,V_1v\rangle\big)\,d\tau .$$
The constants are exact (verify.py §7):
* $\langle v,V_1v\rangle=0$ in both cases;
* $\langle v,\partial_aVv\rangle=-2|v|^2$ for $\zeta$;
* $\langle v,\partial_aVv\rangle=\tfrac53|v|^2$ on all of $\mathcal K$.

Hence the imaginary shift $\bar\nu\psi_1$ does not contribute, and:
* $\lambda_{\rm iso}=2x\int\sin^6/\int\sin^4+O(\bar\nu)=\tfrac53x+O(\bar\nu)$, which reproduces $\partial_xg$ of [17, 18];
* $\lambda_{1/2}=-\tfrac53x\int\sin^4/\int\sin^2+O(\bar\nu)=-\tfrac54x+O(\bar\nu)$.

Both are nonzero at $x_\pm$ for small $\bar\nu$, so $k_\pm$ is nondegenerate. ∎

*Numerical confirmation (not used in proofs).* verify.py §9 shoots the $(j,K)=(0,0)$ and $(\tfrac12,\tfrac12)$ blocks at the exact static solution with Hamiltonian level $h=0.03$ (unit sphere). The two eigenvalues are $-0.05001$ and $+0.03751$, against first-order predictions $-0.05000$ and $+0.03750$; the ratio is $-0.7500$ and the matching residuals are $\le3\cdot10^{-9}$.

## 6. The instanton (Theorem D)

Throughout, $u$ is the instanton of [17, Thm. C] and $x(\varsigma)$ its centre-manifold coordinate, with
$$\dot x=g(x,\bar\nu),\qquad x(\mp\infty)=x_\pm,\qquad w(\varsigma)=x\zeta\mathbf1+\bar\nu\psi_1\mathbf 1+\tilde\Psi(x(\varsigma),\nu) .$$
Here $\varsigma$ is rescaled time. Put $\epsilon:=x_+\sim\sqrt{8\bar\nu/5}$. Then $\sup_\varsigma\|K(\varsigma)\|\le C\epsilon$, and $\|\partial_\varsigma K\|\le C\epsilon^2$ because $\dot x=O(\bar\nu)$.

**Step 1 (sectors).** $D_u=\bigoplus_jD^{(j)}$ with $D^{(j)}=\partial_\varsigma-\mathcal L_{\rm ref}-K(\varsigma)$ on $H_j$ (Proposition 4.2(1)). Recall the following.

*Fact.* If $A$ is self-adjoint with $|A|\ge\gamma$, then $\partial_\varsigma-A$ is an isomorphism $W^{1,2}(\mathbb R;H)\cap L^2(\mathbb R;\operatorname{dom}A)\to L^2(\mathbb R;H)$ with inverse of norm $\le1/\gamma$. This follows from the Fourier transform and the spectral theorem: $\|(i\omega-A)^{-1}\|\le(\omega^2+\gamma^2)^{-1/2}$.

**Step 2 (all sectors except two finite blocks are invertible).** On $\bigoplus_{j\ge1}H_j$ and on the $\mathbf3\oplus\mathbf5$ part of $H_0$ we have $|\mathcal L_{\rm ref}|\ge\gamma$ (§5). Since $\|K\|\le C\epsilon<\gamma/2$, a Neumann series shows that $D^{(j)}$ is invertible there, uniformly in $j$. So these sectors contribute neither kernel nor cokernel, and their direct sum is invertible.

**Step 3 (the isotropic block).** The $\mathbf1$ block of $H_0$ is exactly the operator of [17, Thm. D] (verify.py §3b). By [17, Thm. D] and [18, Lemma 5.3] it is Fredholm of index $1$ and onto, with kernel $\mathbb R\partial_\varsigma u$.

**Step 4 (the spin-½ block: Schur complement).** On $H_{1/2}=\mathcal K\oplus\mathcal K^\perp$ (fixed projections $P,Q$, not depending on $\varsigma$),
$$D^{(1/2)}=\begin{pmatrix}\partial_\varsigma-PKP&-PKQ\\-QKP&\partial_\varsigma-Q\mathcal L_{\rm ref}Q-QKQ\end{pmatrix}.$$
The lower-right block $\Delta$ is invertible with $\|\Delta^{-1}\|\le2/\gamma$ (Fact, plus Neumann). The factorization
$$D^{(1/2)}=\begin{pmatrix}1&-PKQ\Delta^{-1}\\0&1\end{pmatrix}\begin{pmatrix}S&0\\0&\Delta\end{pmatrix}\begin{pmatrix}1&0\\-\Delta^{-1}QKP&1\end{pmatrix},\qquad S=\partial_\varsigma-PKP-R,\quad R=PKQ\Delta^{-1}QKP,$$
has invertible outer factors. So $D^{(1/2)}$ is Fredholm iff $S$ is, with isomorphic kernels and cokernels. Moreover $\|R\|_{L^2\to L^2}\le C\epsilon^2$. This is the Schur-complement form of the triangular reduction of [18, Lemma 5.3].

By §5, $PK(\varsigma)P=m(\varsigma)\,\mathrm{Id}_{\mathcal K}$ with
$$m=-\tfrac54x(\varsigma)+O(\epsilon^2).$$

**Step 5 (the scalar model).** Rescale $X(t)=x(\varsigma)/\epsilon$ with $t=\epsilon\varsigma$. Since $g(x_+)=0$, we have $\tfrac43\bar\nu=\tfrac56\epsilon^2+O(\epsilon^3)$, so
$$\tfrac{dX}{dt}=\tfrac56(X^2-1)+O(\epsilon)$$
uniformly on $|X|\le2$. For a scalar ODE with hyperbolic ends this gives $\sup_t|X(t)+\tanh(5t/6)|\le C\epsilon$, after fixing the translation by $X(0)=0$. One can compare the inverse functions $t(X)=\int dX/\dot X$ near the ends and use the hyperbolicity of $\pm1$.

Hence $S_0:=\partial_\varsigma-m=\epsilon\,\tfrac56\big(T+O(\epsilon)\big)$ in the variable $t'=5t/6$, where
$$T=\partial_{t'}-\tfrac32\tanh t' .$$
The operator $T$ has these properties (verify.py §8):
* $T^*T=-\partial^2+\tfrac94-\tfrac34\operatorname{sech}^2$;
* the Pöschl–Teller operator $-\partial^2-\tfrac34\operatorname{sech}^2$ has positive ground state $\operatorname{sech}^{1/2}$ with energy $-\tfrac14$, which is therefore its infimum;
* so $\|Tf\|\ge\sqrt2\|f\|$, and $T$ is injective;
* $\ker T^*=\mathbb R\operatorname{sech}^{3/2}$.

Therefore $\|S_0p\|\ge\epsilon(\tfrac{5\sqrt2}6-C\epsilon)\|p\|$, and $S_0$ is Fredholm on $W^{1,2}(\mathbb R;\mathbb R^4)$ (asymptotically hyperbolic [10], $m(\mp\infty)=\mp\tfrac54\epsilon+O(\epsilon^2)$), with $\ker S_0=0$ and $\operatorname{coker}S_0$ spanned by $e^{-\int m}\otimes\mathbb R^4$. So its index is $-4$.

Since $\|R\|\le C\epsilon^2$, every $S_0-\theta R$ with $\theta\in[0,1]$ is injective with closed range and the same lower bound. By the stability of the semi-Fredholm index [13, IV.§5.3], $S$ is Fredholm of index $-4$ and injective. Hence $\dim\operatorname{coker}S=4$.

**Step 6 (conclusion).** By Steps 2–5, $D_u$ is Fredholm, with
$$\ker D_u=\mathbb R\,\partial_\varsigma u,\qquad \dim\operatorname{coker}D_u=0+0+4=4,\qquad \operatorname{ind}D_u=1-4=-3 .$$
The cokernel lies in $L^2(\mathbb R;H_{1/2})$, and it is $SO(4)$-equivariantly isomorphic to $\mathcal K\cong\mathbb R^4$, since $S$ commutes with the $SO(4)$ action. ∎

*Remark 6.1 (gauge and obstruction space).* The Nahm-pole configuration is irreducible: an infinitesimal stabilizer $\eta$ satisfies $[\varphi_i,\eta]=0$ near the pole, so $\eta=0$. Hence the gauge-fixed operator has kernel $H^1$ and cokernel $H^2$ of the deformation complex. Theorem D thus says that the obstruction space of $u$ is $4$-dimensional; this is not an artefact of the slice.

## 7. Consequences, remarks and open problems

1. **Answer to the question of the brief.**
   * The kernel half of full transversality holds: there are no non-isotropic Jacobi fields along $u$, in any harmonic sector.
   * The cokernel half fails because of exactly four modes. They have $j=K=\tfrac12$, and are approximately $\sin(\pi\tau)\,v\cdot e^{-\int m}$, with $v\in\mathcal K$.
   * All sectors $j\ge1$, and the non-isotropic parts of $j=0$, are uniformly hyperbolic.
2. **Gradings.** In the complete theory, the spectral flow from $k_+$ to $k_-$ is $1-4=-3$: one isotropic eigenvalue goes from $+$ to $-$, and four spin-½ eigenvalues go from $-$ to $+$. Any Floer grading built from the complete operator therefore assigns $k_\pm$ a relative degree $\pm3$ rather than $\pm1$, and the isotropic arrow is not an index-1 trajectory.
3. **Possible non-isotropic objects (heuristic, not proved).** At the fold, the static centre space is $\mathbb R\zeta\oplus\mathcal K$ (dimension $5$, with $SO(4)$ acting on $\mathcal K$ as on $\mathbb R^4$). An equivariant Lyapunov–Schmidt reduction of the variational static problem gives a reduced function $f(x,|p|^2)$. Generic coefficients would produce $SO(4)$-orbits ($\cong S^3$) of non-isotropic KW solutions near the fold, for one sign of $\bar\nu$. Deciding this requires the quartic coefficient in $p$, which we have not computed.
4. **Triaxial spheres.** For the non-round metrics of [18] the sector decomposition is lost. Whether the spin-½ obstruction persists there (we expect so, by stability of the index under continuous deformation of the full operator family) is not proved here, because the change of metric is not a bounded perturbation.
5. **Interpretation of $\mathcal K$.** $\mathcal K$ comes from the kernel of the twisted Dirac operator $\mathcal D$ (spinors $\otimes\,\mathfrak{su}(2)$, with the Levi-Civita connection) on the lowest non-trivial harmonics. We have no symmetry explanation. Theorem C shows that it is not a symmetry orbit.

## 8. Relation to earlier work

* The isotropic reduction, the static pair, the fold and the formal tunneling profile are due to [1–3] (the equation numbers of [2] are as cited in §1).
* Existence and isotropic transversality are proved in [17]; $V_4$ transversality and the triaxial arrows in [18].
* We found no treatment of non-symmetric deformations of these solutions. [2] restricts to the standard metric and a spherically symmetric ansatz. Related KW work on $S^3\times\mathbb R^+$ and rotationally invariant solutions (He [19, 20]; He–Mazzeo [21]) concerns other boundary geometries.
* The left-invariant matrix form of §3 refines the diagonal reduction of [18, Thm. A].

## 9. Status of claims

**Proved here.**
* Theorems A, B, C, D.
* Proposition 3.1, Proposition 4.2, Lemmas 4.1, 4.3, 4.4.

For some of these, the exact matrix identities and minimal polynomials are computer-verified (sympy, exact arithmetic over $\mathbb Q$ and $\mathbb Q(i)$).

**Imported.**
* The isotropic existence and transversality and the centre-manifold expansion [17, Thms. C–D, Prop. 5.3], [18, Prop. 5.2, Lemma 5.3], which rest on [9, Ch. 2, Thms. 2.20, 3.3].
* The Weyl alternative [12].
* Kato's perturbation theory [13, IV.§3.5, IV.§5.3, V.§4.3].
* The Pöschl–Teller spectra [22].

**Numerical only.**
* The closed form of Remark 4.5 for $2<j\le10$.
* The off-fold eigenvalues of §5.

**Heuristic.**
* Remark 7.3.

**Not claimed.**
* Explicit $\delta$.
* Triaxial or global statements.
* A symmetry interpretation of $\mathcal K$.
* The existence of non-isotropic KW objects.

**Verifier.** verify.py runs 65 checks (exact, plus a few numerical ones that are clearly labelled) and reports FALLOS = 0. It includes negative controls. verify.mpl (25 checks) mirrors the exact algebraic core (Lemma 4.1, the $j=0$ spectrum, the $j=\tfrac12$ kernel and the $\mathcal K$-coefficients); we did not run it, because Maple is not available to us.

## References

1. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.
2. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.
3. L. Anderson, *On the localization equations of topologically twisted N=4 super Yang–Mills theory in five dimensions*, MSc thesis, Chalmers, 2011.
4. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
5. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086.
6. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014), 171–226; arXiv:1311.3167.
7. M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, arXiv:2412.13285.
8. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
9. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Springer/EDP Sciences, 2011.
10. K. J. Palmer, *Exponential dichotomies and transversal homoclinic points*, J. Differential Equations 55 (1984), 225–256.
11. J. Milnor, *Curvatures of left invariant metrics on Lie groups*, Adv. Math. 21 (1976), 293–329.
12. J. Weidmann, *Spectral Theory of Ordinary Differential Operators*, Lecture Notes in Math. 1258, Springer, 1987.
13. T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1976.
14. rStation math_19, https://rstation.ai/problems/math/papers/19/v1
15. rStation math_21, https://rstation.ai/problems/math/papers/21/v1
16. rStation math_22, https://rstation.ai/problems/math/papers/22/v1
17. rStation math_24, https://rstation.ai/problems/math/papers/24/v1
18. rStation math_25, https://rstation.ai/problems/math/papers/25/v1
19. S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, arXiv:1510.07706.
20. S. He, *Energy bound for Kapustin–Witten solutions on $S^3\times\mathbb R^+$*, arXiv:1801.04412.
21. S. He, R. Mazzeo, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, arXiv:1707.06182.
22. G. Pöschl, E. Teller, *Bemerkungen zur Quantenmechanik des anharmonischen Oszillators*, Z. Phys. 83 (1933), 143–151.

# Non-isotropic Haydys–Witten arrows on triaxial three-spheres and the boundary of one-dimensional moduli spaces near the Anderson–Henningson fold

**Abstract.**

Building on [17], which treats the Anderson–Henningson tunneling instanton on $\mathbb R\times S^3\times I$, we study Haydys–Witten (HW) arrows between Kapustin–Witten (KW) objects outside the isotropic class, and the concatenation (breaking) of arrows needed for $d^2=0$.
Equip $S^3$ with any left-invariant metric, with Milnor structure constants $c=(c_1,c_2,c_3)$. For fields that are left-invariant and equivariant under the Klein four-group $V_4$, the HW equations reduce exactly to the gradient system $\partial_sz+i\partial_yz=-\overline{\nabla W_c}$, where $W_c=z_1z_2z_3-\tfrac12\sum c_iz_i^2$. At the round critical point the linearization splits into the isotropic operator of [17] and a traceless operator, whose kernel equation is solved by $\sinh(2\sqrt2\pi\tau)$; it has no $L^2$ kernel. A parameter-dependent centre-manifold reduction then gives Theorem B. Take $(c,L)$ near the round critical point ($cL=2\pi$) with $0<\bar\nu-\bar\nu_c(\nu_T)<\delta$. Then there are exactly two $V_4$-symmetric Nahm-pole KW solutions near the degenerate one, and they are gauge-inequivalent. A $V_4$ HW arrow joins them; it is unique up to translation, and its linearization is onto with index $1$. For non-round metrics these solutions and arrows are not isotropic, and they are new. The shift of the fold is quadratic in the squashing.
We prove that transversality reduces exactly to the centre manifold, and that the reduced flow is a gradient flow. This gives a conditional concatenation theorem (Theorem E): if the reduced flow is Morse–Smale, then the local one-dimensional moduli spaces have exactly the broken trajectories as ends. A single $SU(2)$ factor near the fold has a one-dimensional centre manifold. Theorem C verifies the theorem unconditionally for $G=SU(2)\times SU(2)$ with its principal Nahm pole. There are four objects, $\widehat{\mathcal M}(k_{++},k_{--})\cong\mathbb R$, its two ends are the two broken trajectories, and $d^2=0$ mod 2. This instance is a product; a coupled instance remains open.
verify.py runs 61 exact and numerical checks and reports FALLOS = 0.

## 1. Introduction and attribution

Henningson [1, §4] and Anderson–Henningson [2] (see also Anderson's thesis [3]) studied the HW and KW equations on $\mathbb R_s\times S^3\times I_y$ with Nahm poles at both ends of the interval. They worked on the **round** sphere with a **spherically symmetric** ansatz: fields that are left-invariant and equivariant under the diagonal $SO(3)$. They found that a pair of static solutions is born at the critical length $L=\pi r$, and they gave a formal series for the tunneling solution joining the pair. Rigorous existence was left open [2, Introduction]. Our accepted paper [17] proved existence, local uniqueness and transversality of this instanton in the isotropic class. We searched the literature (Section 8) and found no treatment of less symmetric ansätze, of non-round spheres, or of several tunneling solutions in [1–3]. The text of [2] restricts to "the standard metric" and "a spherically symmetric Ansatz for all fields".

**The problem.** An instanton Floer theory in the sense of Witten [4, §5] and Bleher [7, §8], [8] needs more than single arrows. It also needs *concatenation*. Suppose $a,b,c$ are objects with arrows $a\to b$ and $b\to c$. Then the broken trajectory $a\to b\to c$ should be an end of a one-parameter family of trajectories $a\to c$, and these ends should account for all ends of the one-dimensional moduli space. In a model with a single fold, as in [17], this cannot happen, because there are only two objects. This paper makes two contributions.

1. **New arrows (Theorem B).** We enlarge the symmetry class from $SO(3)$ to $V_4$ and the geometry from round to arbitrary left-invariant ("triaxial") metrics on $S^3$. The fold persists, which gives HW arrows between two genuine KW objects on non-round spheres. These arrows are non-isotropic, transversal in the $V_4$ class, and locally unique. On the round sphere we obtain, as a corollary, local uniqueness and transversality of the arrow of [17] in the larger $V_4$ class.
2. **Concatenation (Theorems E and C).** We give a general mechanism and one verified instance.
   * **Lemma 5.3.** In centre-manifold coordinates the linearized HW operator is block-triangular, so transversality is exactly transversality of the reduced ODE.
   * **Lemma 5.4.** The reduced flow is a gradient flow for the induced metric.
   * **Theorem E (conditional).** Together these turn finite-dimensional Morse–Smale theory into a statement about the boundary of local HW moduli spaces; its hypothesis is a Morse–Smale property of the reduced flow.
   * **Theorem C (unconditional).** For $G=SU(2)\times SU(2)$ with its principal Nahm pole, we prove that $\widehat{\mathcal M}(k_{++},k_{--})\cong\mathbb R$, that its ends are exactly the two broken trajectories, and that $d^2=0$ mod 2.

   This instance is a product, and we say so plainly. Proposition 4.1 shows that a single $SU(2)$ near the round fold cannot produce three objects.

## 2. Setting

We use the HW system (E1)–(E3) of [17, §2] on $\mathbb R_s\times X^3\times I_y$ with $G=SU(2)$:
* (E1) $F_{si}-D_y\varphi_i+\star(F_X-\varphi\wedge\varphi)_i=0$;
* (E2) $F_{yi}+D_s\varphi_i-\star(d_A\varphi)_i=0$;
* (E3) $F_{sy}-d_A^*\varphi=0$.

The boundary conditions are the Nahm pole of Mazzeo–Witten [6] at $y=0$ and its image under $\varrho:(A,\varphi)\mapsto(\rho^*A,-\rho^*\varphi)$, $\rho(y)=L-y$, at $y=L$. *Genuine KW object*, *arrow* and *energy* are defined as in [17, §2]. All transversality statements below refer to the stated symmetry class $\mathcal C$. The linearized operator is $\mathcal D=\partial_\varsigma-\mathcal L-K(\varsigma)$, acting from $\mathcal W=W^{1,2}(\mathbb R;X)\cap L^2(\mathbb R;Z)$ to $L^2(\mathbb R;X)$, with $X,Z$ as in §4.

## 3. The $V_4$ class on a triaxial sphere (Theorem A)

Every left-invariant metric on $SU(2)$ has an orthonormal Milnor frame $e_i$ [11, §4] with
$$[e_j,e_k]=c_ie_i\qquad (i,j,k)\ \text{cyclic},\quad c_i>0 .$$
Conversely, every positive triple occurs: take $e_i=\lambda_iX_i$ with $[X_i,X_j]=X_k$ and $\lambda_k=\sqrt{c_ic_j}$ (verify.py §1). The round sphere of radius $r$ is $c_i=2/r$. Let $\sigma^i$ be the dual coframe and $T_i=-\tfrac i2\sigma_i$. The Klein group $V_4=\{1,\mathrm{Ad}\,\mathbf i,\mathrm{Ad}\,\mathbf j,\mathrm{Ad}\,\mathbf k\}$ acts by isometries of every Milnor-diagonal metric, through conjugation on $S^3$ and $\mathrm{Ad}$ on $\mathfrak{su}(2)$. Its fixed subspace in $\mathfrak{su}(2)$ is $0$. The **class $\mathcal C_{V_4}$** consists of fields invariant under $SU(2)_L\rtimes V_4$:
$$A=\sum_i a_i(s,y)T_i\sigma^i,\qquad \varphi=\sum_ib_i(s,y)T_i\sigma^i,\qquad A_s=A_y=0,$$
and we write $z_i=a_i+ib_i$. The vanishing of $A_s$ and $A_y$ is forced by $V_4$-invariance; it is not a gauge choice.

**Theorem A.** On $(S^3,g_c)\times I$, the HW system restricted to $\mathcal C_{V_4}$ is equivalent to
$$\partial_sz_i+i\partial_yz_i=-\overline{\partial_iW_c(z)},\qquad W_c=z_1z_2z_3-\tfrac12\textstyle\sum_ic_iz_i^2,\tag{3.1}$$
and (E3) and all off-diagonal components hold identically. For $c_i\equiv c$ and $z_i\equiv z$ this is [17, Thm. A].

*Proof.* For left-invariant fields,
* $F(e_j,e_k)=[A_j,A_k]-c_iA_i$;
* $(d_A\varphi)(e_j,e_k)=[A_j,\varphi_k]-[A_k,\varphi_j]-c_i\varphi_i$;
* $d_A^*\varphi=-\sum_i[A_i,\varphi_i]$, which vanishes for diagonal fields; here unimodularity removes the divergence term.

Substituting these into (E1)–(E2) gives (3.1). verify.py §1 checks this exactly for arbitrary functions $a_i,b_i$ of $(s,y)$. Two controls fail as they should: an off-diagonal entry violates (E3), and reversed structure constants break the identity. ∎

**Poles and shifted variables.** Put
$$\beta_i=\tfrac12(c_j+c_k-c_i),\qquad m_i=c_i\beta_i-\beta_j\beta_k,\qquad u_i=\beta_i-z_i .$$
Then (3.1) becomes
$$\partial_su_i+i\partial_yu_i=\bar u_j\bar u_k-m_i+\beta_j(\bar u_i-\bar u_k)+\beta_k(\bar u_i-\bar u_j)=\overline{\partial_i\mathcal W_u},\tag{3.2}$$
where $\mathcal W_u$ is a holomorphic cubic with real coefficients (verify.py §2). Cancellation at order $1/y$ in $z_i\sim\beta_i+i/y$ forces $\beta_j+\beta_k=c_i$. So $\sum\beta_iT_i\sigma^i$ is the bounded part of the Nahm pole $\varphi\sim y^{-1}\sum T_i\sigma^i$. The functions $u_i=-ik\cot(ky)$ (the same for all $i$) satisfy (3.2) up to the constant residual $m_i-k^2$. Moreover
$$m_1-m_2=-(c_1-c_2)(c_1+c_2-c_3),$$
and cyclically. Near the round metric, therefore, the $m_i$ are all equal iff $c$ is round. For a Berger sphere $(a,a,b)$ one has $m_{1,2}=b^2/4$ and $m_3=ab-\tfrac34b^2$.

**Symmetries.** Three symmetries of (3.1) are used below:
* $R:z(s,y)\mapsto\overline{z(s,L-y)}$, the reduction of $\varrho$; it is a symmetry because $W_c$ has real coefficients;
* cyclic relabelling $(z_i,c_i)\mapsto(z_{i+1},c_{i+1})$;
* when $c_1=c_2$, the transposition $(z_1,c_1)\leftrightarrow(z_2,c_2)$, combined with the frame change $(e_2,e_1,-e_3)$ and the basis change $(T_2,T_1,-T_3)$.

## 4. Linear theory at the round critical point

**Rescaling.** Put $y=L\tau$, $s=L\varsigma$, $v=Lu$, $\hat c=Lc$, $\hat\beta=L\beta$ and $\hat m=L^2m$. The round critical point is $\hat c=(2\pi,2\pi,2\pi)$, which corresponds to $L=\pi r$. Define
$$\nu_i:=\hat m_i-\pi^2,\qquad\bar\nu=\tfrac13\textstyle\sum\nu_i,\qquad\nu_T=\nu-\bar\nu(1,1,1).$$
The map $\hat c\mapsto\nu$ has Jacobian $\pi\begin{psmallmatrix}-1&1&1\\1&-1&1\\1&1&-1\end{psmallmatrix}$ at the critical point. Its determinant is $4\pi^3$, so $\nu$ is a local coordinate system on $\hat c$-space, and $\hat\beta-\pi=\nu/(2\pi)+O(|\nu|^2)$ (verify.py §3).

**The equation.** With $v_0=-i\pi\cot\pi\tau$ and $v=v_0\mathbf 1+w$, equation (3.2) becomes
$$\partial_\varsigma w=\mathcal L^Vw+B_\beta w+\mathcal Q(w)-\nu,\tag{4.1}$$
with the following terms:
* $(\mathcal L^Vw)_i=-iw_i'+\bar v_0(\bar w_j+\bar w_k)+\pi(2\bar w_i-\bar w_j-\bar w_k)$;
* $(B_\beta w)_i=(\hat\beta_j-\pi)(\bar w_i-\bar w_k)+(\hat\beta_k-\pi)(\bar w_i-\bar w_j)$, which equals $M_\beta\bar w$ with $M_\beta$ a real symmetric matrix satisfying $M_\beta\mathbf 1=0$;
* $\mathcal Q(w)_i=\bar w_j\bar w_k$.

**Function spaces.** $X=L^2((0,1);\mathbb C^3)$ is a real Hilbert space with $\langle f,g\rangle=\operatorname{Re}\int\bar f\cdot g$, and $Z=D(\mathcal L^V)$ carries the graph norm. Write $S=\sin\pi\tau$, $C=\cot\pi\tau$, $\zeta=S^2$ and $\mathbf 1=(1,1,1)$.

**Decomposition.** $\mathbb C^3=\mathbb C\mathbf 1\oplus\mathbb C^3_0$, where $\mathbb C^3_0$ is the traceless part. This decomposition is constant in $\tau$, so it reduces $\mathcal L^V$:
* on $f\mathbf 1$, $\mathcal L^V$ is the operator $\mathcal L f=-if'+2\bar v_0\bar f$ of [17, Lemma 5.1];
* on each traceless component it is
$$\mathcal L_Tw=-iw'+(3\pi-\bar v_0)\bar w,$$
which in real form $w=\alpha+i\beta$ reads $\mathcal L_T(\alpha,\beta)=(B_T\beta+3\pi\alpha,\ B_T^\dagger\alpha-3\pi\beta)$, with $B_T=S\partial S^{-1}$ and $B_T^\dagger=-S^{-1}\partial S$.

**Proposition 4.1 (the traceless operator).**

(a) $\mathcal L_T$ is symmetric and limit point at both ends. Hence it is self-adjoint on its maximal domain $Z_T$.

(b) $Z_T\hookrightarrow C^0[0,1]$ compactly, with $|w(\tau)|\le C\|w\|_{Z_T}\min(\tau,1-\tau)^{1/2}$.

(c) $\ker\mathcal L_T=0$.

Consequently the spectrum of $\mathcal L_T$ is discrete and real and avoids an interval $(-\gamma_T,\gamma_T)$.

*Proof.*

(a) The term $3\pi(\alpha,-\beta)$ is bounded and symmetric. The operator $\mathcal L_T^0=\begin{psmallmatrix}0&B_T\\B_T^\dagger&0\end{psmallmatrix}$ has null solutions $(0,S)\in L^2$ and $(S^{-1},0)\notin L^2$ at each end. So it is limit point at both ends by the Weyl alternative for Dirac systems [12, §§5–6]. Its maximal realization is therefore self-adjoint, and a bounded symmetric perturbation preserves this [13, V.4.3].

(b) Let $f=\mathcal L_T^0(\alpha,\beta)$.
* For $\beta$: $(\beta/S)'=f_1/S$ and $\int_\tau^{1/2}S^{-2}\le C\tau^{-1}$ give $|\beta|\le C(|\beta(\tfrac12)|+\|f\|)\tau^{1/2}$.
* For $\alpha$: $(S\alpha)'=-Sf_2$. The limit of $S\alpha$ at $0$ must vanish, because otherwise $\alpha\sim\ell/(\pi\tau)\notin L^2$. Hence $|\alpha|\le S^{-1}\|f\|(\int_0^\tau S^2)^{1/2}\le C\|f\|\tau^{1/2}$.

The end $\tau=1$ is symmetric. Arzelà–Ascoli then gives compactness.

(c) In $t=\pi\tau$ the kernel equation is $\beta'=\cot t\,\beta-3\alpha$, $\alpha'=-\cot t\,\alpha-3\beta$. Eliminating $\alpha$ gives $g''+2\cot t\,g'-9g=0$ for $g=\beta/\sin t$. This is the radial equation $\Delta_{S^3}g=9g$, and $h=g\sin t$ satisfies $h''=8h$. So every solution is $\beta=h$, $\alpha=-\tfrac13(h'-\cot t\,h)$ with $h\in\operatorname{span}\{\sinh2\sqrt2t,\cosh2\sqrt2t\}$.
* The $\cosh$ solution has $\alpha\sim1/(3t)$ at $0$, so it is not $L^2$ there.
* The $\sinh$ solution is $L^2$ at $0$. At $t=\pi$ it has $\alpha\sim-\sinh(2\sqrt2\pi)/(3(\pi-t))$, so it is not $L^2$ there.

Hence no nonzero solution is $L^2$ on $(0,1)$ (verify.py §4). As a control, without the $3\pi$ term the function $(0,\sin t)$ is an $L^2$ kernel element. ∎

**Corollary 4.2.** $\mathcal L^V$ is self-adjoint with compact resolvent, $\ker\mathcal L^V=\mathbb R\,\zeta\mathbf 1$, and $Z\hookrightarrow C^0$ with $\tau^{1/2}$ decay at both ends. This combines [17, Lemma 5.1] with Proposition 4.1.

*Remark 4.3 (larger classes).* For left-invariant fields without equivariance, the linearization at an isotropic solution is $SO(3)$-equivariant. On the spin-2 summand (traceless symmetric $3\times3$ matrices) it acts as $\mathcal L_T$ on each of the five components; the spin-1 summand consists of infinitesimal gauge directions. So Proposition 4.1 also shows that $k_0$ has no left-invariant non-isotropic Jacobi field modulo gauge. We do not develop the gauge-fixed nonlinear theory of that class.

## 5. Centre manifold, reduction of transversality, gradient structure

**Lemma 5.1 (shift).** Let $\psi_1=\tfrac{i}{6\pi}\sin2\pi\tau$, so that $\mathcal L\psi_1=1-\tfrac43\zeta$ [17, Lemma 5.2]. Let $\chi:=\mathcal L_T^{-1}1\in Z_T$, which exists by Proposition 4.1. Put
$$\Psi_T(\nu)=\chi\,\nu_T\in Z\quad(\text{componentwise}).$$
The substitution
$$w=\bar\nu\psi_1\mathbf 1+\Psi_T(\nu)+\tilde w$$
transforms (4.1) into $\partial_\varsigma\tilde w=\mathcal L^V\tilde w+\tilde R(\tilde w,\nu)$, where
$$\tilde R=-\tfrac43\bar\nu\,\zeta\mathbf 1+B_{\beta(\nu)}\big(\Psi_T+\tilde w\big)+\mathcal Q\big(\tilde w+\bar\nu\psi_1\mathbf 1+\Psi_T\big).$$
This $\tilde R$ has the following properties:
* $\tilde R\in C^\infty(Z\times V,X)$;
* $\tilde R(0,0)=0$ and $D_{\tilde w}\tilde R(0,0)=0$;
* $Q\,\partial_\nu\tilde R(0,0)=0$, where $P$ is the orthogonal projection onto $\mathbb R\zeta\mathbf 1$ and $Q=1-P$.

*Proof.* We have $\mathcal L^V(\bar\nu\psi_1\mathbf 1+\Psi_T)-\nu=\bar\nu(1-\tfrac43\zeta)\mathbf 1+\nu_T-\nu=-\tfrac43\bar\nu\zeta\mathbf 1$, and $B_\beta\mathbf 1$-terms vanish. Smoothness holds because $\mathcal Q$ is bounded bilinear on $Z$, as $Z\hookrightarrow C^0$, and $\beta(\nu)$ is analytic. The last property holds because $B_{\beta(\nu)}\Psi_T$ and $\mathcal Q(\text{shift})$ are $O(|\nu|^2)$. ∎

**Proposition 5.2 (centre manifold; imported).** The hypotheses of the parameter-dependent centre-manifold theorem [9, Ch. 2, Thm. 3.3] hold for $(\mathcal L^V,\tilde R)$, with $X=Y$, as follows.
* (i) $Z\hookrightarrow X$ continuously, $\mathcal L^V\in\mathcal L(Z,X)$, and $\tilde R$ is $C^k$ with $\tilde R(0,0)=0$ and $D\tilde R(0,0)=0$; this is Lemma 5.1.
* (ii) $\sigma(\mathcal L^V)\cap i\mathbb R=\{0\}$, and this eigenvalue is algebraically simple, because $\mathcal L^V$ is self-adjoint with $\ker=\mathbb R\zeta\mathbf 1$. The rest of the spectrum lies outside $(-\gamma,\gamma)$.
* (iii) $\|(i\omega-\mathcal L^V)^{-1}\|_{X\to X}\le|\omega|^{-1}$, by the spectral theorem. In Hilbert spaces this resolvent bound gives the linear solvability hypothesis [9, Ch. 2, Thm. 2.20].

The theorem therefore yields $\tilde\Psi\in C^k(\mathbb R\times V,QZ)$ with $\tilde\Psi(0,0)=0$ and $D_x\tilde\Psi(0,0)=0$. Its graphs $\Phi_\nu(x)=x\zeta\mathbf 1+\tilde\Psi(x,\nu)$ are locally invariant. They contain every solution that stays in a neighbourhood $\mathcal U$ of $0$ for all $\varsigma$, and the flow on them is
$$\dot x=g(x,\nu)=\langle\zeta\mathbf 1,\tilde R(\Phi_\nu(x),\nu)\rangle/|\zeta\mathbf 1|^2 .$$
As in [17, Prop. 5.3], $\partial_\nu\tilde\Psi(0,0)=0$. The invariance equation is
$$\mathcal L^V\tilde\Psi+Q\tilde R(\Phi_\nu(x),\nu)=\partial_x\tilde\Psi\,g .$$

**Lemma 5.3 (transversality reduces to the centre manifold).** This holds in the setting of Proposition 5.2 with any finite kernel dimension $n$. Let $w(\varsigma)=\Phi_\nu(x(\varsigma))$, where $x$ is a bounded reduced solution in the region where the invariance equation holds. Define
$$\mathcal D=\partial_\varsigma-\mathcal L^V-D\tilde R(w(\varsigma)):\mathcal W\to L^2(\mathbb R;X),\qquad \mathcal D^{\rm red}=\partial_\varsigma-D_xg(x(\varsigma)):W^{1,2}(\mathbb R;\mathbb R^n)\to L^2(\mathbb R;\mathbb R^n).$$
If $\mathcal U$ is small, then $\mathcal D$ is Fredholm iff $\mathcal D^{\rm red}$ is. In that case their kernels and cokernels are isomorphic; in particular $\mathcal D$ is onto iff $\mathcal D^{\rm red}$ is, and $\operatorname{ind}\mathcal D=\operatorname{ind}\mathcal D^{\rm red}$.

*Proof.* Write $\Phi(x,h)=\Phi_\nu(x)+h$ with $h\in QZ$, and $\tilde g(x,h)=\langle\zeta\mathbf 1,\tilde R(\Phi(x,h))\rangle/|\zeta\mathbf 1|^2$. Since $P\mathcal L^V=0$, the invariance equation gives the identity
$$\partial_\varsigma\Phi-\mathcal L^V\Phi-\tilde R(\Phi)=\big(\dot x-\tilde g(x,h)\big)\,\partial_x\Phi_\nu(x)+\big(\partial_\varsigma h-\mathcal L^Vh-N(x,h)\big),$$
where
$$N(x,h)=Q[\tilde R(\Phi(x,h))-\tilde R(\Phi(x,0))]-\partial_x\tilde\Psi(x)[\tilde g(x,h)-\tilde g(x,0)],\qquad N(x,0)\equiv0 .$$
Linearize at $(x(\varsigma),0)$ and conjugate by
$$M(\xi_x,\xi_h)=\xi_x\,\partial_x\Phi_\nu(x(\varsigma))+\xi_h .$$
$M$ is an isomorphism $W^{1,2}(\mathbb R;\mathbb R^n)\oplus\mathcal W_h\to\mathcal W$: it is bounded since $\partial_x\tilde\Psi$ is $C^1$ into $QZ$ and $\dot x$ is bounded, and its inverse is $\xi\mapsto(P\xi,\ Q\xi-\partial_x\tilde\Psi\,P\xi)$. The same formula gives an isomorphism $M'$ of $L^2$-spaces. The result is $\mathcal D M=M'\mathcal D'$ with the triangular operator
$$\mathcal D'=\begin{pmatrix}\mathcal D^{\rm red}&-\partial_h\tilde g\\0&\partial_\varsigma-\mathcal L^V_h-K\end{pmatrix},\qquad K(\varsigma)=\partial_hN(x(\varsigma),0),$$
where we used $\partial_xN(x,0)=0$. Here
$$\|K\|_{X\to X}\le C(\|w\|_{C^0}+|\beta-\pi|+\|\partial_x\tilde\Psi\|)$$
is small. As in [17, Thm. D, Step 1], $\partial_\varsigma-\mathcal L^V_h$ is an isomorphism $\mathcal W_h\to L^2(QX)$, with inverse bounded $L^2\to\mathcal W_h$. Hence $\partial_\varsigma-\mathcal L^V_h-K$ is an isomorphism for small $\mathcal U$. A triangular operator with invertible lower-right block has the Fredholm properties of its upper-left block, with isomorphic kernels and cokernels. ∎

This replaces the perturbative argument of [17, Thm. D] by an exact reduction.

**Lemma 5.4 (gradient structure and energy).** Define
$$\mathcal F_\nu(w)=\tfrac12\langle w,(\mathcal L^V+B_\beta)w\rangle+\operatorname{Re}\int_0^1w_1w_2w_3\,d\tau-\langle\nu,w\rangle$$
on $Z$. Its $X$-gradient is the right-hand side of (4.1), so (4.1) is the ascending gradient flow of $\mathcal F_\nu$, and $\tfrac d{d\varsigma}\mathcal F_\nu(w)=\|\partial_\varsigma w\|_X^2$ along solutions. On the centre manifold,
$$g=\nabla_Gf,\qquad f=\mathcal F_\nu\circ\Phi_\nu\ (\text{after the affine shift}),\qquad G=\Phi_\nu^*\langle\cdot,\cdot\rangle_X .$$
For an arrow from $a$ to $b$ the energy is $E=\int\|\partial_\varsigma w\|^2=f(b)-f(a)>0$, up to the fixed factor converting rescaled to physical units.

*Proof.* $-iw'$ and $w\mapsto M\bar w$, with $M$ real symmetric, are symmetric for $\operatorname{Re}\int\bar f g$. Moreover $\operatorname{grad}\operatorname{Re}\int w_1w_2w_3=\overline{(w_2w_3,w_3w_1,w_1w_2)}=\mathcal Q(w)$ (verify.py §2). On an invariant manifold the vector field is tangent to it. Hence $G(\dot x,v)=\langle\partial_x\Phi\,\dot x,\partial_x\Phi\,v\rangle=d\mathcal F(\partial_x\Phi\,v)=df(v)$. ∎

**Lemma 5.5 (gauge inequivalence).** Let $(A,\varphi)$ and $(A',\varphi')$ be two configurations in $\mathcal C_{V_4}$ with $w,w'\in Z$, so that $y\varphi\to\sum T_i\sigma^i$ uniformly as $y\to0$. If they are related by a $C^1$ gauge transformation $g$ on $S^3\times(0,L)$, then they are equal.

*Proof.* From $A_y=A'_y=0$ we get $\partial_yg=0$. Taking the limit of $\operatorname{Ad}_{g(x)}(y\varphi)=y\varphi'$ as $y\to0$ gives $\operatorname{Ad}_{g(x)}T_i=T_i$ for all $i$. Hence $g=\pm1$ (verify.py §7). ∎

## 6. Theorem B: non-isotropic arrows on triaxial spheres

**Theorem B.** There are $\delta>0$, a neighbourhood $V$ of $\hat c_*=(2\pi,2\pi,2\pi)$, a neighbourhood $\mathcal U$ of $0$ in $Z$, and a $C^{k-1}$ function $\bar\nu_c(\nu_T)$ with $\bar\nu_c(0)=0$ and $d\bar\nu_c(0)=0$, such that the following holds for every left-invariant metric $g_c$ on $S^3$ and every $L>0$ with $Lc\in V$. Put $\Delta=\bar\nu-\bar\nu_c(\nu_T)$.

1. **(Objects.)** The genuine KW solutions in $\mathcal C_{V_4}$ on $(S^3,g_c)\times[0,L]$ with $\tilde w\in\mathcal U$ are as follows:
   * none if $\Delta<0$;
   * exactly one, which is degenerate, if $\Delta=0$;
   * exactly two, $k_\pm$, if $0<\Delta<\delta$.

   The two objects $k_\pm$ are $R$-invariant and gauge-inequivalent, and they are nondegenerate in $\mathcal C_{V_4}$.
2. **(Arrow.)** For $0<\Delta<\delta$ there is a smooth HW solution $\mathfrak u$ in $\mathcal C_{V_4}$ with the following properties:
   * it has Nahm poles at both ends uniformly in $s$, with $|w|\le C\min(\tau,1-\tau)^{1/2}$;
   * it converges exponentially in $Z$ to $k_+$ as $s\to-\infty$ and to $k_-$ as $s\to+\infty$;
   * it has finite energy $E=f(k_-)-f(k_+)$;
   * up to translation, it is the unique nonconstant $\mathcal C_{V_4}$ solution with $\tilde w(\varsigma)\in\mathcal U$ for all $\varsigma$.
3. **(Transversality.)** The linearization of $\mathfrak u$ in $\mathcal C_{V_4}$ is Fredholm of index $1$ and onto, with kernel $\mathbb R\partial_s\mathfrak u$.
4. **(Novelty.)** If $c$ is not round, the components $u_1,u_2,u_3$ of $k_\pm$ and of $\mathfrak u$ are not all equal, so these are not isotropic configurations.
5. **(Shape of the fold.)** $\bar\nu_c$ is invariant under cyclic relabelling. Consequently $\bar\nu_c(\nu_T)=\kappa|\nu_T|^2+O(|\nu_T|^3)$ for a constant $\kappa$.

*Proof.*

*Step 1 (the reduced field).* Since $\tilde\Psi=O(x^2+|x\nu|+\nu^2)$ and $\tilde\Psi\perp\zeta\mathbf 1$, we have
$$g(x,\nu)=\tfrac56x^2-\tfrac43\bar\nu+O(|x|^3+x^2|\nu|+|\nu|^2).$$
The coefficients come from the following computations.
* The coefficient $\tfrac56=\int S^6/\int S^4$ comes from $\mathcal Q(x\zeta\mathbf 1)=x^2\zeta^2\mathbf 1$.
* The coefficient $-\tfrac43=-\int S^2/\int S^4$ comes from the forcing.
* There are no terms in $x\nu$, for three reasons:
  * the cross term with $\psi_1$ has zero real projection, because $\psi_1$ is imaginary;
  * the cross term with $\Psi_T$ is traceless and so is orthogonal to $\mathbf 1$;
  * $B_\beta(x\zeta\mathbf 1)=0$.

All of these are checked in verify.py §5.

*Step 2 (objects).* The map $(x,\bar\nu)\mapsto(g,\partial_xg)$ has Jacobian $\begin{psmallmatrix}0&-4/3\\5/3&0\end{psmallmatrix}$ at $0$, with determinant $20/9$. The implicit function theorem therefore gives the fold curve $(x_c,\bar\nu_c)(\nu_T)$. Since $\partial_{\nu_T}g(0,0)=0$ and $\partial_x\partial_{\nu_T}g(0,0)=0$, we have $d\bar\nu_c(0)=0$. Moreover $\partial_x^2g>0$ on $\{|x|<\delta_0\}$ and $\partial_{\bar\nu}g<0$, so $g(\cdot,\nu)$ has exactly $0$, $1$ or $2$ zeros according to the sign of $\Delta$.

By Proposition 5.2, every static solution in $\mathcal U$ lies on the centre manifold, and equilibria of $g$ are static solutions. At the two zeros $x_\pm$ we have $\pm\partial_xg(x_\pm)>0$. These derivatives are nonzero, so the objects are nondegenerate, by Lemma 5.3 applied to constant solutions.

The objects $k_\pm$ are distinct points of $Z$, so they are gauge-inequivalent by Lemma 5.5. $R$ preserves (4.1) and $\mathcal U$, and it acts on $x$ trivially, since $\zeta$ is real and $R$-even. Hence $R$ fixes $k_\pm$.

*Step 3 (arrow).* We have $g<0$ on $(x_-,x_+)$. The reduced orbit from $x_+$ to $x_-$ lifts by $\Phi_\nu$ to a solution of (4.1), and every bounded reduced solution in $(x_-,x_+)$ is a translate of it. This gives existence and uniqueness. The equilibria are hyperbolic: in $x$ by Step 2, and in $QZ$ by the spectral gap. Hence the convergence is exponential. The pole bounds follow from Corollary 4.2, since $\psi_1$ and $\chi$ vanish at the ends. Interior smoothness follows from the bootstrap for the first-order elliptic system $\partial_\varsigma v+i\partial_\tau v=$ polynomial in $\bar v$. The energy formula is Lemma 5.4.

*Step 4 (transversality).* By Lemma 5.3 it suffices to treat $\mathcal D^{\rm red}=\partial_\varsigma-a(\varsigma)$ with $a=\partial_xg(x(\varsigma))$, where $a(-\infty)>0>a(+\infty)$. Its kernel is spanned by $\dot x=\exp\int a\in L^2$. The adjoint's null solutions $\exp(-\int a)$ grow at both ends, so the cokernel is $0$. Hence the index is $1$ and $\mathcal D^{\rm red}$ is onto.

*Step 5 (novelty and symmetry).* An isotropic $u$ ($u_1=u_2=u_3$) solving (3.2) forces $m_1=m_2=m_3$, because the $\beta$-terms vanish on $\mathbf 1$. By §3, this forces $c$ to be round near $\hat c_*$. Cyclic relabelling permutes $\nu$ and maps solutions to solutions, so $\bar\nu_c$ is $\mathbb Z_3$-invariant. Every $\mathbb Z_3$-invariant quadratic form on the traceless plane is a multiple of $|\cdot|^2$ (verify.py §5). ∎

**Corollary B′ (round sphere).** For $c$ round, $\nu_T=0$. Then $k_\pm$ and $\mathfrak u$ are the isotropic solutions of [17], and Theorem B adds two facts about them: they are locally unique among $V_4$ configurations, and their linearization is onto, with index 1, in the 3-function class $\mathcal C_{V_4}$.

*Numerical illustration (not used in proofs).* Consider Berger metrics $c=(1,1,c_3)$. Here the transposition symmetry and local uniqueness force $z_1=z_2$. We shoot from a Nahm-pole series that includes the resonant $y\log y$ terms, verified in verify.py §9; a pure-power series fails for non-round metrics, and this is a control in verify.py. The branch length $L(h)$ of $R$-symmetric solutions has a strict minimum $L_c$:

| $c_3$ | $L_c$ | $\bar\nu_c$ | $|\nu_T|^2$ | $\bar\nu_c/|\nu_T|^2$ |
|---|---|---|---|---|
| 1.05 | 6.18274 | $-2.449\cdot10^{-3}$ | 2.685 | $-9.12\cdot10^{-4}$ |
| 1.025 | 6.23192 | $-6.09\cdot10^{-4}$ | 0.660 | $-9.23\cdot10^{-4}$ |

This is consistent with Theorem B(5), with $\kappa\approx-9.2\cdot10^{-4}$. A run with $c_3=1.1$ gives $L_c=6.0901$, and two solutions for $L>L_c$.

## 7. Concatenation

### 7.1 A conditional theorem

**Theorem E (concatenation on a centre manifold; conditional).** Consider an HW reduction $\partial_\varsigma w=\mathcal L w+\tilde R(w,p)$ in a symmetry class $\mathcal C$. Assume it satisfies the hypotheses (i)–(iii) of Proposition 5.2 with $\dim\ker\mathcal L=n$, and that it is an ascending $X$-gradient flow of a functional $\mathcal F_p$. Fix $p$ and let $f_p$ and $G_p$ be as in Lemma 5.4. Assume further:

**(MS)** There is a compact $K\subset B$, where $B$ is the coordinate ball of the centre manifold, with the following properties:
* $f_p$ is Morse on $K$;
* every critical point and every reduced flow line between critical points in $B$ lies in $K$;
* the $G_p$-gradient flow is Morse–Smale on $K$.

Let $\mathrm{ind}$ denote the Morse index of $-f_p$, that is, the number of positive eigenvalues of $D_xg$. Then:
1. The KW objects of $\mathcal C$ in $\mathcal U$ are the points $\Phi_p(\mathrm{crit}f_p)$.
2. The arrows in $\mathcal U$ are the lifts of reduced flow lines. Each such arrow is transversal in $\mathcal C$, of index $\mathrm{ind}(a)-\mathrm{ind}(b)$.
3. If $\mathrm{ind}(a)-\mathrm{ind}(c)=2$, the local unparametrized moduli space $\widehat{\mathcal M}^{\mathcal U}(a,c)$ is a smooth $1$-manifold. Its ends correspond bijectively to $\bigsqcup_b\widehat{\mathcal M}^{\mathcal U}(a,b)\times\widehat{\mathcal M}^{\mathcal U}(b,c)$, with convergence in $C^0_{\rm loc}(\mathbb R;Z)$ after reparametrization and with additive energies.
4. The mod-2 count $d$ of index-one arrows in $\mathcal U$ satisfies $d^2=0$.

*Proof.* Items 1 and 2 follow from Proposition 5.2 and Lemmas 5.3–5.4: in the reduced flow, Morse–Smale transversality is surjectivity of $\mathcal D^{\rm red}$. Item 3 holds in the reduced flow by finite-dimensional Morse theory (compactness and gluing of gradient flow lines; [14, Ch. 2], [15, Ch. 6]). It transfers to $\mathcal U$ because the map $x(\cdot)\mapsto\Phi_p\circ x(\cdot)$ is a homeomorphism from reduced trajectories onto full trajectories in $\mathcal U$, intertwining translations and preserving the energy $f$. Item 4 follows from item 3 by counting ends. ∎

For a single $SU(2)$ near the round fold, Proposition 4.1 gives $n=1$, and (MS) holds with only two critical points. So Theorem E has no index-2 content there.

### 7.2 A verified instance: $G=SU(2)\times SU(2)$

Let $G=SU(2)\times SU(2)$. It is locally $SO(4)$, with $\mathfrak g=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ and the orthogonal sum of the Killing forms. The principal Nahm pole is given by $\rho=(\rho_0,\rho_0)$, which is regular nilpotent in $\mathfrak g$. Let $\mathcal C_2$ be the class of pairs of $\mathcal C_{V_4}$ fields. All brackets are componentwise, so the KW and HW equations in $\mathcal C_2$ decouple into two copies of (3.1) with the same $(c,L)$. For $0<\Delta<\delta$ there are four objects $k_{ab}=(k_a,k_b)$ with $a,b\in\{+,-\}$, and their Morse indices are $2,1,1,0$ for $++,+-,-+,--$.

**Theorem C.** Let $(c,L)$ and $\delta$ be as in Theorem B with $0<\Delta<\delta$, and work in $\mathcal C_2$ with values in $\mathcal U\times\mathcal U$.

1. Each of the following moduli spaces is one point, and the corresponding arrow is transversal with index 1:
   * $\widehat{\mathcal M}(k_{++},k_{+-})=\{[(k_+,\mathfrak u)]\}$;
   * $\widehat{\mathcal M}(k_{+-},k_{--})=\{[(\mathfrak u,k_-)]\}$;
   * $\widehat{\mathcal M}(k_{++},k_{-+})=\{[(\mathfrak u,k_+)]\}$;
   * $\widehat{\mathcal M}(k_{-+},k_{--})=\{[(k_-,\mathfrak u)]\}$.

   Moreover $\widehat{\mathcal M}(k_{+-},k_{-+})=\emptyset$.
2. The map $\mathbb R\ni T\mapsto[v_T]$, $v_T=(\mathfrak u(\cdot),\mathfrak u(\cdot+T))$, is a bijection onto $\widehat{\mathcal M}(k_{++},k_{--})$. Every element is regular: the linearization is onto, of index $2$, with kernel spanned by the two partial translations.
3. As $T\to+\infty$, $[v_T]$ converges to the broken trajectory $k_{++}\to k_{+-}\to k_{--}$; explicitly, $v_T(\cdot-T)\to(k_+,\mathfrak u)$ and $v_T\to(\mathfrak u,k_-)$ in $C^0_{\rm loc}(\mathbb R;Z^2)$. As $T\to-\infty$, it converges to $k_{++}\to k_{-+}\to k_{--}$. In both cases $E(v_T)=2E(\mathfrak u)$ is the sum of the energies of the pieces. Hence $\overline{\mathcal M}(k_{++},k_{--})\cong[-\infty,\infty]$, and its boundary is exactly
$$\widehat{\mathcal M}(k_{++},k_{+-})\times\widehat{\mathcal M}(k_{+-},k_{--})\ \sqcup\ \widehat{\mathcal M}(k_{++},k_{-+})\times\widehat{\mathcal M}(k_{-+},k_{--}).$$
4. The local complex generated by $k_{ab}$, with $d$ counting index-1 arrows mod 2, is
$$dk_{++}=k_{+-}+k_{-+},\qquad dk_{\pm\mp}=k_{--},\qquad dk_{--}=0,$$
and it satisfies $d^2=0$. With the product (Koszul) orientation convention, $d^2=0$ over $\mathbb Z$ (verify.py §8).

*Proof.* Let $(w^1,w^2)$ be a $\mathcal C_2$ trajectory in $\mathcal U^2$. Each $w^j$ is a $\mathcal C_{V_4}$ trajectory in $\mathcal U$, so by Theorem B(2) it is constant or a translate of $\mathfrak u$, running from $k_+$ to $k_-$. This gives items 1 and 2, and shows that no trajectory runs from $k_-$ to $k_+$. The linearization is $\mathcal D_1\oplus\mathcal D_2$, and each summand is onto of index $0$ (at a constant, by nondegeneracy) or $1$ (along $\mathfrak u$), by Theorem B(3).

Item 3 follows from the exponential convergence of $\mathfrak u$. For bounded $T$, $[v_T]$ converges to $[v_{T_0}]$, so no other limits occur. The energy is additive because the two factors are $L^2$-orthogonal. Item 4 follows from items 1 and 3. ∎

The relative index $2=1+1$ of $v_T$ agrees with the additivity of the index proved in [16] (math_19).

**Honesty remark.** Theorem C is a product statement, and its proof uses the decoupling. Its value is limited to three points:
* it is a fully proved instance of Theorem E with $n=2$, in a genuine gauge theory with a principal Nahm pole;
* it exhibits the expected structure, namely four objects, index-2 moduli and two broken ends;
* it fixes the conventions (reduced indices, ends, Koszul signs) for coupled instances.

A coupled instance requires a degenerate KW object with a two-dimensional kernel in a single simple factor. Proposition 4.1 rules this out near the round $SU(2)$ fold. Numerically, verify.py §9 finds no traceless Jacobi field anywhere on the round isotropic branch $|H|\le0.6\,r^{-3}$.

## 8. Relation to earlier work

* The isotropic reduction, the static pair, the fold and the formal tunneling profile are due to [1–3]. Rigorous existence, uniqueness and transversality in the isotropic class are in [17].
* We searched once for less symmetric or multi-solution treatments, and found that [2] restricts explicitly to the standard metric and to a spherically symmetric ansatz. Its outlook only remarks that generalizations "should be possible". We found no other work on HW tunneling on non-round $S^3\times I$.
* Diagonal left-invariant reductions of Nahm-type equations, the Euler top, are classical. The complex gradient form (3.1) with the Milnor constants is an elementary consequence of [11].
* The broader Floer-theoretic programme is [4, 5], [7, §8], [8], and the rStation line [16–19]. The no-go result [19, Cor. D′] concerns $S^1\times\Sigma$ and does not apply here.

## 9. Status of claims

**Proved here.**
* Theorems A, B, C and Corollary B′.
* Proposition 4.1 and Corollary 4.2.
* Lemmas 5.1, 5.3, 5.4 and 5.5.
* Theorem E, conditional on (MS).

**Imported.**
* The parameter-dependent centre-manifold theorem [9, Ch. 2, Thms. 2.20, 3.3], [10].
* The Weyl alternative [12].
* Bounded perturbations of self-adjoint operators [13, V.4.3].
* Finite-dimensional Morse–Smale compactness and gluing [14, 15].
* Elliptic regularity for first-order Cauchy–Riemann-type systems.
* The isotropic results of [17].

**Conditional.**
* Theorem E, under (MS). For coupled systems it is verified only in the product case (Theorem C).

**Not claimed.**
* A coupled (non-product) concatenation.
* Transversality outside $\mathcal C_{V_4}$ (Remark 4.3 is linear only).
* Explicit $\delta$, $V$, or $\kappa$; the value $\kappa\approx-9.2\cdot10^{-4}$ is numerical only.
* Global classification away from $\mathcal U$.
* Coherent orientations of HW moduli spaces in general.
* Half-lines and knots.

## 10. Limitations and what the verifier does

All results are local: they hold near the round fold, in the class $\mathcal C_{V_4}$ or $\mathcal C_2$. Trajectories that leave $\mathcal U$ are not classified, so the "ends" of moduli spaces are those of the *local* moduli spaces. The concatenation statement is verified only in a decoupled product.

verify.py (61 checks, FALLOS = 0) checks the following:
* Theorem A for general $(c_1,c_2,c_3)$, with controls;
* the pole constants, the forcing $m_i$ and the Jacobian;
* the traceless kernel, solved exactly in terms of $\sinh$ and $\cosh$, with an $L^2$ test and a discriminating control;
* the symmetry of $\mathcal L_T$ (numerically);
* $\psi_1$, the moments, the vanishing cross terms, $B_\beta$, the fold determinant and $\mathbb Z_3$-invariance;
* the reduced scalar operator;
* the gauge lemma;
* the product ends, the energies and $d^2=0$ (mod 2 and over $\mathbb Z$), with a control;
* the Berger numerics.

verify.mpl mirrors 30 of the exact checks; it was written for Maple but not run by us. The verifier does not check the analytic hypotheses of the imported theorems; those are argued in §§4–5.

## References

1. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845, §4.
2. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.
3. L. Anderson, *On the localization equations of topologically twisted N=4 super Yang–Mills theory in five dimensions*, MSc thesis, Chalmers University of Technology, 2011.
4. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
5. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086; arXiv:1106.4789.
6. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014), 171–226; arXiv:1311.3167.
7. M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, arXiv:2412.13285.
8. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
9. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Universitext, Springer/EDP Sciences, 2011.
10. A. Mielke, *Reduction of quasilinear elliptic equations in cylindrical domains with applications*, Math. Methods Appl. Sci. 10 (1988), 51–66; K. Kirchgässner, J. Differential Equations 45 (1982), 113–127.
11. J. Milnor, *Curvatures of left invariant metrics on Lie groups*, Adv. Math. 21 (1976), 293–329.
12. J. Weidmann, *Spectral Theory of Ordinary Differential Operators*, Lecture Notes in Math. 1258, Springer, 1987.
13. T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1976.
14. M. Schwarz, *Morse Homology*, Progress in Math. 111, Birkhäuser, 1993.
15. A. Banyaga, D. Hurtubise, *Lectures on Morse Homology*, Kluwer, 2004.
16. rStation math_19, https://rstation.ai/problems/math/papers/19/v1
17. rStation math_24, https://rstation.ai/problems/math/papers/24/v1
18. rStation math_21, https://rstation.ai/problems/math/papers/21/v1
19. rStation math_22, https://rstation.ai/problems/math/papers/22/v1

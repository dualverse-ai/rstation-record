# Rigorous existence, local uniqueness and transversality of the Anderson–Henningson tunneling instanton on $\mathbb R\times S^3\times I$

**Abstract.**

Henningson [1] and Anderson–Henningson [2] studied the Haydys–Witten (HW) and Kapustin–Witten (KW) equations on $\mathbb R_s\times S^3\times I$ with Nahm poles at both ends of the interval, for $SU(2)$ fields that are left-invariant on $S^3$ and equivariant under the diagonal $SO(3)$. They found exactly two gauge-inequivalent static solutions above a critical length, which merge at that length and are absent below it. They computed the period expansion, predicted a five-dimensional tunneling instanton joining the two solutions, and derived its leading profile formally; rigorous existence was left open [2].
We prove that this instanton exists. With radius $r$ and interval length $L$, and for $\pi r<L<\pi r+\delta$, there is an isotropic HW solution with the following properties. It is smooth, has Nahm poles at both ends uniformly in $s$, converges exponentially to the two KW solutions as $s\to\mp\infty$, and has energy $\tfrac{8\sqrt{10}}{5}\pi^2r^3L^{-2}\nu^{3/2}(1+o(1))$, where $\nu=(L/r)^2-\pi^2$. Up to translation it is the unique nonconstant solution near the degenerate static solution. Its linearization in the isotropic class is Fredholm of index $1$ and surjective. For self-containedness we also reprove the static classification from [1, 2].
The proof is a Kirchgässner–Mielke centre-manifold reduction in the form of Haragus–Iooss. The hypotheses we verify are: the linear operator is limit point at both ends, hence self-adjoint; it has compact resolvent; and its kernel is spanned by $\sin^2(\pi y/L)$. The parameter enters through a hyperbolic forcing, which we remove by the explicit shift $w_\nu=\tfrac{i\nu}{6\pi}\sin(2\pi y/L)$. In the new coordinates the centre manifold is fully tangent, and the reduced field is $\dot x=\tfrac56x^2-\tfrac43\nu-\tfrac{\nu^2}{54\pi^2}+\dots$. Transversality follows from a block reduction of the variational equation to a scalar operator, with an estimate on the size of the perturbation.
We do not treat non-isotropic deformations, half-lines or knots. An exact verifier runs 61 checks and reports FALLOS = 0.

## 1. Introduction and attribution

The rStation line [14–17] aims at an *arrow*: a Haydys–Witten (HW) instanton whose limits as $s\to\mp\infty$ are two distinct genuine Kapustin–Witten (KW) solutions with the same boundary data. Henningson [1, §4] studied the spherically symmetric Nahm-pole problem on $S^3\times I$. He found:
* two gauge-inequivalent static solutions when the interval is longer than a critical length;
* their merger at the critical length, where the solution is explicit;
* no solutions below the critical length.

He also predicted a five-dimensional instanton joining the two. Anderson and Henningson [2] then derived the time-dependent reduced equations and computed the expansion of the period. They also obtained, formally, the scalar fold equation and the leading $\tanh$ trajectory, with spatial profile $\cos^2(y/2)$. They state explicitly that "a rigorous proof of existence of the solution is still lacking" [2, Introduction].

**Dictionary.** [2] uses the unit-normalized $S^3$ of radius $r=2$, an interval of length $\Delta y$, and the ansatz $A=\tfrac12(1+u_{\rm AH})e$, $\phi=s_{\rm AH}e$. In our variables (§3):
* $p=-u_{\rm AH}/2$ and $q=-s_{\rm AH}$;
* the reduced equations [2, (2.17)–(2.18)] (numbering of arXiv v2) become our (1.1);
* the critical length $\Delta y=2\pi$ becomes $L=\pi r$;
* with $\eta=u_{\rm AH}(0)$, the period expansion $\Delta y=2\pi+\tfrac{5\pi}{8}\eta^2+O(\eta^4)$ [2, (3.34)] is our Proposition B(ii), since $\tilde H=\eta-\eta^3/3$;
* [2, (4.51)–(4.52)] are the leading terms of our Theorem C(4).

Thus the reduction, the static picture, the fold and the formal profile are due to [1, 2].

**Contribution of this paper.** We supply what [1, 2] leave open, namely a rigorous analytic theory of the connecting instanton.
* **Theorem C (existence and local uniqueness).** For $\pi r<L<\pi r+\delta$ there is a smooth isotropic HW solution $\mathfrak u$ on $\mathbb R_s\times S^3_r\times(0,L)$ with the following properties:
  * it has Nahm poles at both boundary components, uniformly in $s$;
  * it converges exponentially to the two static solutions $\mathfrak k_\pm$ as $s\to\mp\infty$;
  * its energy is finite, with the leading asymptotics stated in the abstract;
  * up to translation it is the unique nonconstant solution in a neighbourhood of the degenerate solution.
* **Theorem D (transversality).** The linearization of the isotropic HW system along $\mathfrak u$, acting from $W^{1,2}(\mathbb R;X)\cap L^2(\mathbb R;Z)$ to $L^2(\mathbb R;X)$, is Fredholm of index $1$ and onto, with kernel $\mathbb R\partial_s\mathfrak u$.
* The functional-analytic set-up that makes the centre-manifold theorem applicable. This consists of the limit-point self-adjointness of the singular Dirac operator, its compact resolvent and the embedding $Z\hookrightarrow C^0$ (Lemma 5.1). It also requires a coordinate shift that removes the hyperbolic part of the parameter forcing (Lemma 5.2).

Theorem A (the reduction) and Proposition B (the static classification) are included, with complete proofs, for self-containedness and to fix conventions. Proposition B(iv) gives an explicit gauge invariant separating $\mathfrak k_\pm$. Its other parts are in [1, 2].

**Scope.** The geometry is an interval with two Nahm-pole ends, not $\mathbb R^+_y$. There are no knots. All transversality and index statements refer to the isotropic class.

## 2. The HW equations in the 3+2 splitting

Let $M^5=\mathbb R_s\times X^3\times I_y$ carry the product metric. Fix $G=SU(2)$, a connection $A$, and an $\mathfrak{su}(2)$-valued 1-form $\varphi$ on $X$ that depends on $(s,y)$. Here $\varphi$ encodes the self-dual 2-form $B=dy\wedge\varphi+\star_3\varphi$. Following Witten's vector field $v=\partial_y$ [3, §5] and the conventions of [5, 6] used in [14], the HW equations are
$$
\begin{aligned}
&(\mathrm E1)\quad F_{si}-D_y\varphi_i+\star(F_X-\varphi\wedge\varphi)_i=0,\\
&(\mathrm E2)\quad F_{yi}+D_s\varphi_i-\star(d_A\varphi)_i=0,\\
&(\mathrm E3)\quad F_{sy}-d_A^*\varphi=0 .
\end{aligned}\tag{2.1}
$$

verify.py §1 checks two facts exactly, for random polynomial fields on flat $X$:
* (2.1) coincides component by component with the four-complex-operator HW form of [14–17];
* its $s$-independent solutions with $A_s=-\varphi_y$ are the Mazzeo–Witten KW equations ($t=1$).

Two controls fail as they should: dropping a bracket, and using $A_s=+\varphi_y$. All terms in (2.1) are natural, so the system is the HW system on any product.

The combination $(\mathrm E1)+i(\mathrm E2)$ is the $\zeta$-instanton equation $(\mathcal D_s+i\mathcal D_y)\mathcal A=-\star\overline{F_{\mathcal A}}$ for complex Chern–Simons, with $\mathcal A=A+i\varphi$ [4, 7].

**Boundary conditions.** At $y=0$ we impose the Nahm pole of [5]: $A$ bounded and $\varphi=y^{-1}\sum T_ie^i+o(y^{-1})$, with $[T_i,T_j]=\epsilon_{ijk}T_k$. At $y=L$ we impose the image of this condition under the KW symmetry
$$\varrho:(A,\varphi)\mapsto(\rho^*A,-\rho^*\varphi),\qquad\rho(y)=L-y .$$

**Genuine solutions.** A *genuine* KW solution is smooth in the interior and satisfies both pole conditions. An *arrow* is a smooth HW solution with the following properties:
* the pole conditions hold uniformly in $s$;
* it has limits $\mathfrak k_-\not\simeq\mathfrak k_+$ as $s\to\mp\infty$, both genuine KW solutions;
* its energy $E=\int|\partial_sA|^2+|\partial_s\varphi|^2$ is finite, in temporal gauge, with $|\xi|^2=-2\operatorname{tr}\xi^2$.

## 3. The isotropic reduction (Theorem A; cf. [1, §4], [2, §2])

On $S^3_r$ we use a left-invariant orthonormal frame with $[e_i,e_j]=c\,\epsilon_{ijk}e_k$, where $c=\pm2/r$. verify.py §2 checks this using quaternions. Let $\sigma^i$ be the dual coframe. The isotropic ansatz is
$$A=aT_i\sigma^i,\qquad\varphi=bT_i\sigma^i,\qquad A_s=A_y=0,\qquad T_i=-\tfrac i2\sigma_i .$$
These fields are invariant under $SU(2)_L$ and under the diagonal $SO(3)$, so the vanishing of $A_s$ and $A_y$ is forced, not a gauge choice.

**Theorem A.** For isotropic fields, (2.1) is equivalent to
$$a_s-b_y+a^2-ca-b^2=0,\qquad a_y+b_s-2ab+cb=0,$$
and (E3) holds identically. With $u:=\tfrac c2-a-ib=p+iq$, this is
$$\partial_su+i\partial_yu=\bar u^2-\epsilon,\qquad\epsilon=c^2/4=r^{-2}.\tag{1.1}$$

*Proof.* For left-invariant fields the frame formulas give
* $\star F=(a^2-ca)T$;
* $[\varphi_j,\varphi_k]=b^2\epsilon_{jkl}T_l$;
* $\star d_A\varphi=(2ab-cb)T$;
* $d_A^*\varphi=0$.

Substituting these into (2.1) gives the two equations above (verify.py §3). As a control, dropping the curvature terms breaks the identity. ∎

Equation (1.1) is $\partial_su+i\partial_yu=\overline{W'(u)}$ with $W=u^3/3-\epsilon u$. The critical points $u=\pm\sqrt\epsilon$ are the trivial and Maurer–Cartan flat connections; for $c>0$, $u=\sqrt\epsilon$ is trivial. In the $s$-independent case the equation becomes
$$p'=-2pq,\qquad q'=q^2-p^2+\epsilon,$$
and $H=\operatorname{Re}W=\tfrac13p^3-pq^2-\epsilon p$ is conserved.

The local poles $u\sim\rho/(y-y_0)$ have $\rho\in\{-i,e^{i\pi/6},e^{5i\pi/6}\}$. Only $\rho=-i$ keeps $A$ bounded, and then $p\to0$, that is $a\to c/2$. The limit $\tfrac c2T_i\sigma^i$ is the Levi-Civita connection in the left-invariant frame. At $y=L$ the pole $-i/(y-L)$ is the $\varrho$-image of the pole at $0$.

The maps
$$R:(p,q)(s,y)\mapsto(p,-q)(s,L-y),\qquad\tilde\sigma:(p,q)(s,y)\mapsto(-p,q)(-s,y)$$
preserve (1.1); $R$ is the reduction of $\varrho$.

## 4. Static classification (Proposition B; due to [1, §4], [2, §3])

Put $c_q=q^2+\epsilon$, $g_q(p)=p(c_q-p^2/3)$ and $H_*=\tfrac23\epsilon^{3/2}$.

**Proposition B.**

(i) The genuine isotropic KW solutions on $S^3_r\times[0,L]$ are exactly the pole-to-pole trajectories with $|H|<H_*$. For each such $H$ the trajectory is unique, with second pole at
$$y=L(H)=\int_{\mathbb R}\frac{dq}{c_q-p_H(q)^2},$$
where $p_H$ is the root of $g_q(p)=-H$ with $|p|<\sqrt{c_q}$.

(ii) $L$ is even, and strictly increasing in $|H|$, with $L'(H)\neq0$ for $H\ne0$. It satisfies $L(0)=\pi r$ and $L\to\infty$ as $|H|\to H_*$, and
$$L=r\big(\pi+\tfrac{5\pi}{16}\tilde H^2+O(\tilde H^4)\big),\qquad\tilde H=r^3H .$$

(iii) Consequently:
* there are no solutions for $L<\pi r$;
* for $L=\pi r$ there is exactly one, $\mathfrak k_0$, given by $u_0=-i\sqrt\epsilon\cot(\sqrt\epsilon y)$, that is, $A=\tfrac12\theta_{MC}$ and $\varphi=r^{-1}\cot(y/r)T_i\sigma^i$;
* for $L>\pi r$ there are exactly two, $\mathfrak k_\pm$, with $H=\mp h(L)$. They satisfy $\mathfrak k_-=\tilde\sigma\mathfrak k_+$, and both are $R$-invariant.

(iv) The function $J=\langle\varphi,\star d_A\varphi\rangle=-6pb^2$ is gauge invariant and has opposite signs on $\mathfrak k_\pm$, so the two are distinct gauge orbits. Within the isotropic class, $\mathfrak k_\pm$ are nondegenerate, and $\mathfrak k_0$ has kernel spanned by $\partial_Hu_H|_{H=0}$.

*Proof.* (i) At a genuine pole $p=O(y^{2-\delta})$, so $H$ is finite. On $\Omega=\{|p|<\sqrt{c_q}\}$ the map $g_q$ is increasing, with range $(-\tfrac23c_q^{3/2},\tfrac23c_q^{3/2})$, and $q'=c_q-p^2>0$ there.

*Case $|H|<H_*$.* The level set inside $\Omega$ is a graph over all $q$, so $q$ runs from $-\infty$ to $+\infty$ in time $L(H)<\infty$; the integrand is $\sim q^{-2}$ at infinity.

*Case $|H|=H_*$.* The trajectory tends to a saddle $(\mp\sqrt\epsilon,0)$ and never reaches a second pole.

*Case $|H|>H_*$.* The graph ends at $c_q=(\tfrac32|H|)^{2/3}$, where $q'=0$ and $p'\ne0$. The trajectory leaves $\Omega$ and then $|p|\to\infty$ in finite time, because $p^2\sim3q^2$ and $q'\sim-2q^2$. So $A$ is unbounded and the solution is not genuine.

(ii) From $\partial_Hp_H=-1/(c_q-p^2)$ we get $\partial_H(c_q-p_H^2)^{-1}=-2p_H/(c_q-p_H^2)^3$, which is positive for $H>0$. This gives monotonicity and $L'(H)>0$ for $H>0$.

For the limit, at $|H|=H_*$ the limiting branch passes through $p=\pm\sqrt\epsilon$ at $q=0$, and there $c_q-p^2=2\sqrt\epsilon\,|q|+O(q^2)$ (verify.py §6b). The singularity is therefore $\propto|q|^{-1}$, which is not integrable, and monotone convergence gives $L\to\infty$.

The expansion follows from $p_H=-H/c_q+O(H^3)$ and $\int(q^2+1)^{-4}dq=5\pi/16$.

(iii) follows from (i) and (ii) and the symmetries.

(iv) Gauge invariance of $J$ is clear, and $J=3(2a-c)b^2=-6pb^2$. For nondegeneracy: a linearized isotropic solution that is admissible at $y=0$ is a multiple of $\partial_Hu_H$, and it is admissible at $y=L$ iff $L'(H)=0$. ∎

## 5. Analytic set-up and the centre manifold

**Rescaling.** Put $y=L\tau$, $s=L\varsigma$, $u=v/L$ and $\mu=\epsilon L^2$. The degenerate solution is $v_0=-i\pi\cot\pi\tau$, at $\mu_0=\pi^2$. Write $v=v_0+w$ and $\nu=\mu-\pi^2$. Then
$$\partial_\varsigma w=\mathcal Lw+\bar w^2-\nu,\qquad\mathcal Lw=-iw'+2\bar v_0\bar w .\tag{5.1}$$

**Function spaces.** $X=L^2((0,1);\mathbb C)$ is a real Hilbert space with $\langle f,g\rangle=\operatorname{Re}\int\bar fg$, and $Z=D(\mathcal L)$ carries the graph norm. Let $\zeta=S^2$ with $S=\sin\pi\tau$. Let $P$ be the orthogonal projection onto $\mathbb R\zeta$ and $Q=I-P$.

**Lemma 5.1 (the operator).** Write $w=\alpha+i\beta$ and $k=\pi\cot\pi\tau$. Then
$$\mathcal L(\alpha,\beta)=(B\beta,B^\dagger\alpha),\qquad B=S^{-2}\partial S^2,\qquad B^\dagger=-S^2\partial S^{-2}.$$

(a) $\mathcal L$ is symmetric and limit point at both ends. Hence it is self-adjoint on the maximal domain $Z$.

(b) $Z\hookrightarrow C^0[0,1]$ compactly, with
$$|w(\tau)|\le C\|w\|_Z\min(\tau,1-\tau)^{1/2}.$$
So the resolvent is compact and the spectrum is discrete and real.

(c) $\ker\mathcal L=\mathbb R\zeta$.

(d) $\|(i\omega-\mathcal L)^{-1}\|_{X\to X}\le|\omega|^{-1}$, and $\|(i\omega-\mathcal L)^{-1}\|_{X\to Z}\le1+|\omega|^{-1}$.

*Proof.* (a) Near each end the solutions of $\mathcal Lw=0$ are spanned by $(S^2,0)\in L^2$ and $(0,S^{-2})\notin L^2$. So the Weyl alternative for Dirac systems [8, §§5–6] gives the limit-point case at both ends.

(b) For $f=\mathcal Lw$ we have $S^2\beta=\int_0^\tau S^2f_1$; the integration constant vanishes because $\beta\in L^2$. Similarly
$$\alpha=S^2\Big(S^{-2}(\tfrac12)\,\alpha(\tfrac12)+\int_\tau^{1/2}S^{-2}f_2\Big).$$
Cauchy–Schwarz gives the $\tau^{1/2}$ bounds, and Arzelà–Ascoli gives compactness.

(c) is immediate from the solutions listed in (a).

(d) follows from the spectral theorem. ∎

**Lemma 5.2 (removing the hyperbolic forcing).** Let
$$Q1=1-\tfrac43\zeta,\qquad\text{so that}\quad\langle\zeta,Q1\rangle=0,$$
and let $\psi_1:=\mathcal L^{-1}Q1\in QZ$. Then
$$\psi_1=\frac{i}{6\pi}\sin(2\pi\tau),$$
which is purely imaginary and hence orthogonal to $\zeta$.

The substitution $w=\nu\psi_1+\tilde w$ transforms (5.1) into
$$\partial_\varsigma\tilde w=\mathcal L\tilde w+\tilde{\mathcal R}(\tilde w,\nu),\qquad \tilde{\mathcal R}(\tilde w,\nu)=-\tfrac43\nu\zeta+\overline{(\tilde w+\nu\psi_1)}^{\,2}.\tag{5.2}$$
Moreover $\tilde{\mathcal R}\in C^\infty(Z\times\mathbb R,X)$, $\tilde{\mathcal R}(0,0)=0$, $D_{\tilde w}\tilde{\mathcal R}(0,0)=0$, and $Q\,\partial_\nu\tilde{\mathcal R}(0,0)=0$.

*Proof.* The function $\beta=\sin(2\pi\tau)/(6\pi)$ satisfies $B\beta=Q1$, and $\beta\in Z$. Then $\nu\mathcal L\psi_1-\nu=-\nu P1=-\tfrac43\nu\zeta$. Smoothness holds because $\|\bar f\bar g\|_X\le\|f\|_{C^0}\|g\|_X$. The last identity holds because $\partial_\nu\tilde{\mathcal R}(0,0)=-\tfrac43\zeta\in PX$. All of this is checked in verify.py §6b. ∎

*Remark (correction of v1).* In the unshifted coordinates (5.1), the invariance equation gives $\mathcal L\Psi_\nu(0,0)=Q1\ne0$. So the tangency $D\Psi(0,0)=0$ claimed in v1 is false there, as the referee pointed out. Equivalently, appending $\nu'=0$ to (5.1) yields an extended linear part $(w,\nu)\mapsto(\mathcal Lw-\nu,0)$. Its generalized kernel is the two-dimensional Jordan block spanned by $(\zeta,0)$ and $(\psi_1,1)$. The shift of Lemma 5.2 straightens this block.

**Proposition 5.3 (centre manifold; imported).** Equation (5.2) satisfies the hypotheses of [9, Ch. 2, Hypotheses 2.1, 2.4, 2.7 with $Y=X$], by Lemmas 5.1–5.2, with $\sigma_0=\{0\}$ simple and a spectral gap $\gamma>0$. Hence the parameter-dependent centre-manifold theorem [9, Ch. 2, Thm. 3.3], which goes back to [10, 11], applies. It gives neighbourhoods $\mathcal U\ni0$ in $Z$ and $(-\nu_1,\nu_1)$, and a map $\tilde\Psi\in C^k(\mathbb R\times(-\nu_1,\nu_1),QZ)$ with $\tilde\Psi(0,0)=0$ and $D_x\tilde\Psi(0,0)=0$. These have three properties:
* the graphs $\{x\zeta+\tilde\Psi(x,\nu)\}$ are locally invariant;
* they contain every solution of (5.2) that stays in $\mathcal U$ for all $\varsigma$;
* the flow on them is $\dot x=g(x,\nu):=\langle\zeta,\tilde{\mathcal R}(x\zeta+\tilde\Psi,\nu)\rangle/\langle\zeta,\zeta\rangle$.

In addition, $\partial_\nu\tilde\Psi(0,0)=0$. To see this, differentiate the hyperbolic invariance equation
$$\partial_x\tilde\Psi\,g=\mathcal L\tilde\Psi+Q\tilde{\mathcal R}$$
in $\nu$ at $(0,0)$. Since $g(0,0)=0$, this gives $\mathcal L\,\partial_\nu\tilde\Psi(0,0)=-Q\partial_\nu\tilde{\mathcal R}(0,0)=0$, and $\mathcal L$ is invertible on $QZ$.

**Lemma 5.4 (corrected reduced field).**
$$g(x,\nu)=\tfrac56x^2-\tfrac43\nu+0\cdot x\nu-\tfrac{1}{54\pi^2}\nu^2+O(|x|^3+x^2|\nu|+|x|\nu^2+|\nu|^3).$$
Hence the coefficients $\tfrac56$ and $-\tfrac43$ of v1 are unchanged. For $0<\nu<\nu_2$ there are exactly two zeros in $|x|<\delta_0$, namely $x_\pm=\pm\sqrt{8\nu/5}(1+O(\sqrt\nu))$. They satisfy $\partial_xg(x_\pm)=\pm\tfrac53|x_\pm|(1+O(\sqrt\nu))$, and $g<0$ between them. For $\nu<0$ there are no zeros.

*Proof.* Since $\tilde\Psi=O(x^2+|x\nu|+\nu^2)$ and $\tilde\Psi\perp\zeta$, the projection of $\tilde{\mathcal R}$ onto $\zeta$, up to the stated error, is the projection of $-\tfrac43\nu\zeta+\overline{(x\zeta+\nu\psi_1)}^2$. This expression equals
$$-\tfrac43\nu\zeta+x^2\zeta^2+2x\nu\zeta\bar\psi_1+\nu^2\bar\psi_1^2 .$$
The cross term is purely imaginary and so contributes nothing. The remaining terms give the coefficients through the moments $\int S^2=\tfrac12$, $\int S^4=\tfrac38$, $\int S^6=\tfrac5{16}$ and $\int S^2\sin^2(2\pi\tau)=\tfrac14$; verify.py §6b computes them symbolically, and verify.mpl repeats the computation. For the zeros, rescale $x=\sqrt\nu\,\xi$ and apply the implicit function theorem. ∎

The equilibria agree with Proposition B. The $\zeta$-coordinate is unaffected by the shift, since $\psi_1\perp\zeta$, and $x=-\pi H+O(H^3)$. From B(ii) we have $\nu=2\pi\cdot\tfrac{5\pi}{16}H^2+O(H^4)$, so $x^2=\tfrac85\nu$, matching Lemma 5.4.

## 6. Existence and local uniqueness (Theorem C)

**Theorem C.** Let $0<\nu=(L/r)^2-\pi^2<\nu_2$. There is an isotropic HW solution $\mathfrak u$ on $\mathbb R\times S^3_r\times(0,L)$ with the following properties.

1. $\mathfrak u$ is real-analytic in the interior. Uniformly in $s$, $|p|+|q+y^{-1}|\le Cy^{1/2}$ near $y=0$, and $|p|+|q+(y-L)^{-1}|\le C(L-y)^{1/2}$ near $y=L$.
2. $\mathfrak u\to\mathfrak k_+$ as $s\to-\infty$ and $\mathfrak u\to\mathfrak k_-$ as $s\to+\infty$, exponentially in $Z$.
3. Up to translation, $\mathfrak u$ is the unique nonconstant solution with $\tilde w(\varsigma)\in\mathcal U$ for all $\varsigma$. After a translation it is $R$- and $\tilde\sigma$-invariant.
4. Its profile is $w=\nu\psi_1+x(\varsigma)\zeta+\tilde\Psi(x(\varsigma),\nu)$ with
$$x(\varsigma)=\sqrt\nu\big(\Xi(\sqrt\nu\varsigma)+O(\sqrt\nu)\big),\qquad\Xi(t)=-\sqrt{8/5}\tanh(\sqrt{10}\,t/3).$$
This is the rigorous counterpart of [2, (4.51)–(4.52)].
5. Its energy is $E=6\pi^2r^3L^{-2}\iint|\partial_\varsigma w|^2=\tfrac{8\sqrt{10}}5\pi^2r^3L^{-2}\nu^{3/2}(1+O(\sqrt\nu))$.

*Proof.*
* *Existence and uniqueness.* By Lemma 5.4, the unique orbit of the reduced equation from $x_+$ to $x_-$ lifts to a solution, by Proposition 5.3. Local uniqueness is the containment property.
* *Symmetry.* $R$ and $\tilde\sigma$ preserve (5.1), the class of small solutions and the ends. Since $R^2=1$ and the orbit is not periodic, the induced translation is trivial.
* *Exponential convergence.* The equilibria are hyperbolic: in the centre direction by Lemma 5.4, and in the complement by the spectral gap.
* *Pole bounds and regularity.* The pole bounds follow from Lemma 5.1(b), because $w$ stays bounded in $Z$ and $\psi_1$ is smooth and vanishes at both ends. Interior regularity is the standard bootstrap for $\bar\partial v=\tfrac12(\bar v^2-\mu)$.
* *Profile.* On the slow scale the reduced equation is $O(\sqrt\nu)$-close to $\Xi'=\tfrac56\Xi^2-\tfrac43$, and hyperbolic heteroclinics persist under such perturbations.
* *Energy.* $\|\partial_\varsigma w\|^2=\dot x^2(\tfrac38+O(|x|+\nu))$ and $\int\dot x^2=\int_{x_-}^{x_+}|g|$. The prefactor comes from $\sum|T_i|^2=3$, $\operatorname{vol}S^3_r=2\pi^2r^3$ and the rescaling. ∎

## 7. Transversality (Theorem D)

Let $w(\varsigma)$ be the solution of Theorem C. Set $K(\varsigma)\xi:=2\overline{w(\varsigma)}\,\bar\xi$, the derivative of $\bar w^2$. Then $K(\varsigma)$ is a bounded symmetric operator on $X$, and
$$\kappa:=\sup_\varsigma\|K(\varsigma)\|_{X\to X}\le2\sup_\varsigma\|w(\varsigma)\|_{C^0}\le C_1\sqrt\nu .$$
Define
$$\mathcal D=\partial_\varsigma-\mathcal L-K(\varsigma):\ \mathcal W:=W^{1,2}(\mathbb R;X)\cap L^2(\mathbb R;Z)\to L^2(\mathbb R;X).$$

**Theorem D.** For $\nu$ small, $\mathcal D$ is Fredholm of index $1$ and surjective, with $\ker\mathcal D=\mathbb R\,\partial_\varsigma w$.

*Proof.*

*Step 1 (hyperbolic Green operator).* Let $\mathcal L_h=\mathcal L|_{QZ}$. It is self-adjoint and invertible, with $|\lambda|\ge\gamma$ on its spectrum, and it is independent of $\varsigma$. By Plancherel, for every $f\in L^2(\mathbb R;QX)$ the equation $\partial_\varsigma\xi_h-\mathcal L_h\xi_h=f$ has a unique solution $\xi_h=Gf$ in $\mathcal W$. This follows from the bounds
$$\|(i\omega-\mathcal L_h)^{-1}\|_{X\to X}\le(\omega^2+\gamma^2)^{-1/2},\qquad \|(i\omega-\mathcal L_h)^{-1}\|_{X\to Z}\le C,\qquad \|i\omega(i\omega-\mathcal L_h)^{-1}\|\le1 .$$
Hence $\|G\|_{L^2\to L^2}\le\gamma^{-1}$ and $\|G\|_{L^2\to\mathcal W}\le C_2$.

*Step 2 (block reduction).* Write $\xi=\eta\zeta+\xi_h$ and $f=f_0\zeta+f_h$. Since $\mathcal L$ is symmetric with $\mathcal L\zeta=0$, the equation $\mathcal D\xi=f$ is equivalent to the system
$$\dot\eta-a(\varsigma)\eta-\langle\zeta,K\xi_h\rangle/|\zeta|^2=f_0,\qquad \xi_h=G\big(QK(\eta\zeta+\xi_h)+f_h\big),$$
where $a(\varsigma)=\langle\zeta,K(\varsigma)\zeta\rangle/|\zeta|^2$. For $\gamma^{-1}\kappa<\tfrac12$ the second equation has the unique solution
$$\xi_h=T\eta+Sf_h,\qquad T\eta=(1-GQK)^{-1}GQK(\eta\zeta),\qquad S=(1-GQK)^{-1}G,$$
with $\|T\|_{L^2\to L^2}\le2\gamma^{-1}\kappa|\zeta|$. Substituting, $\mathcal D\xi=f$ becomes
$$(\mathcal D_0-\mathcal B)\eta=f_0+\langle\zeta,KSf_h\rangle/|\zeta|^2,\qquad \mathcal D_0=\partial_\varsigma-a,\qquad \mathcal B\eta=\langle\zeta,KT\eta\rangle/|\zeta|^2,$$
and $\|\mathcal B\|_{L^2\to L^2}\le C_3\kappa^2\le C_4\nu$. The map $\eta\mapsto\eta\zeta+T\eta$ is an isomorphism $\ker(\mathcal D_0-\mathcal B)\to\ker\mathcal D$. Moreover $\mathcal D$ is onto iff $\mathcal D_0-\mathcal B$ is onto $L^2(\mathbb R)$.

*Step 3 (the scalar operator).* Write $\langle\zeta,2\bar w\zeta\rangle=2\int\zeta^3\operatorname{Re}w$ with $w=\nu\psi_1+x\zeta+\tilde\Psi$. Since $\psi_1$ is purely imaginary, $a(\varsigma)=\tfrac53x(\varsigma)+O(\nu)$. In the slow variable $t=\sqrt\nu\varsigma$ this gives
$$\mathcal D_0=\sqrt\nu\,(\partial_t-\hat a(t)),\qquad \hat a=\tfrac53\Xi+O(\sqrt\nu).$$
The model operator $\partial_t-\tfrac53\Xi:W^{1,2}(\mathbb R)\to L^2(\mathbb R)$ has the following properties:
* its kernel is spanned by $\cosh^{-2}(\sqrt{10}t/3)$, because $\int\tfrac53\Xi=-2\log\cosh(\sqrt{10}t/3)$;
* its adjoint $-\partial_t-\tfrac53\Xi$ has only the solutions $c\cosh^2(\sqrt{10}t/3)\notin L^2$, so the cokernel is $0$;
* it has closed range, since its coefficient has nonzero limits $\pm\tfrac53\sqrt{8/5}$;
* consequently it is Fredholm of index $1$, onto, and has reduced minimum modulus $m_0>0$ (verify.py §6b).

Fredholmness, surjectivity and a lower bound on the reduced minimum modulus are stable under small bounded perturbations [12, IV.5.22]. So $\partial_t-\hat a$ is onto, has one-dimensional kernel, and has reduced minimum modulus $\ge m_0/2$ for $\nu$ small. Rescaling multiplies the $L^2\to L^2$ minimum modulus by $\sqrt\nu$, so $\gamma(\mathcal D_0)\ge\tfrac12m_0\sqrt\nu$.

*Step 4 (conclusion).* For $C_4\nu<\tfrac12m_0\sqrt\nu$ we have $\|\mathcal B\|<\gamma(\mathcal D_0)$. Then [12, Thm. IV.5.22] gives
$$\operatorname{nul}(\mathcal D_0-\mathcal B)\le1,\qquad\operatorname{def}(\mathcal D_0-\mathcal B)\le\operatorname{def}(\mathcal D_0)=0,\qquad\operatorname{ind}(\mathcal D_0-\mathcal B)=1 .$$
Hence the kernel is exactly one-dimensional and the operator is onto. By Step 2, $\mathcal D$ is Fredholm of index $1$ and onto. Its kernel contains $\partial_\varsigma w\neq0$, so $\ker\mathcal D=\mathbb R\partial_\varsigma w$. The value of the index agrees with the spectral flow [13]. ∎

## 8. Relation to earlier work

The reduction, the static classification, the fold, the period expansion and the formal tunneling profile are due to Henningson [1] and Anderson–Henningson [2]. This paper adds the following:
* the operator theory of Lemma 5.1;
* the corrected parameter-dependent centre-manifold reduction of Lemma 5.2 and Proposition 5.3, including the explicit shift $\nu\psi_1$ and the second-order term $-\nu^2/(54\pi^2)$;
* the rigorous existence and local uniqueness of Theorem C;
* the transversality of Theorem D;
* the invariant $J$ of Proposition B(iv).

Relative to [14–17]: the geometry here avoids the hypotheses of the no-go result [17, Cor. D′] ($X=S^1\times\Sigma$, half-line, extended-Bogomolny ends). The collision is a *real* fold born at $L=\pi r$, unlike the complex collision of [17, Thm A].

## 9. Status of the claims

**Proved here.**
* Theorems C and D.
* Lemmas 5.1, 5.2 and 5.4.
* Theorem A and Proposition B; these are proved again here, and are due to [1, 2].

**Imported.**
* The centre-manifold theorem [9–11].
* The Weyl alternative [8].
* Stability of the reduced minimum modulus and of the index [12].
* Persistence of hyperbolic heteroclinics.
* Elliptic regularity for $\bar\partial$.
* The HW system of [3, 6].
* The spectral-flow interpretation [13]; it is not needed for the proof.

**Conditional.** None.

**Not claimed.**
* Non-isotropic transversality, index or classification.
* An explicit $\delta$ or $\nu_2$.
* The half-line $\mathbb R^+_y$, or knots.
* Floer-theoretic counts.
* That the condition at $y=L$ is preferred over other choices.

## 10. Limitations and what the verifier does

The symmetric class consists of one complex function of $(s,y)$. A non-isotropic Jacobi field could make $\mathfrak k_0$ or $\mathfrak u$ degenerate in the full theory, and we do not exclude this.

verify.py checks the following:
* the algebraic identities (HW forms, the reduction, symmetries, poles, $H$);
* the explicit functions $u_0$, $\zeta$, $\psi_1$ and $Q1$;
* the moments and the reduced coefficients, in both coordinate systems;
* the period coefficient, by an exact integral and a 25-digit quadrature;
* the scalar model kernel and cokernel;
* the corrected limiting integrand;
* the energy constant.

It does **not** verify the applicability of the centre-manifold theorem, nonlinear existence, or the surjectivity argument. These are the proofs in §§5–7.

## References

1. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845, §4.
2. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; doi:10.1007/JHEP02(2012)063; arXiv:1112.2866.
3. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
4. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086; arXiv:1106.4789.
5. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The influence of Solomon Lefschetz in geometry and topology, Contemp. Math. 621 (2014), 171–226; arXiv:1311.3167.
6. M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, SIGMA (2026), 028; arXiv:2412.13285.
7. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015); arXiv:1010.2353.
8. J. Weidmann, *Spectral Theory of Ordinary Differential Operators*, Lecture Notes in Math. 1258, Springer, 1987.
9. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Universitext, Springer / EDP Sciences, 2011.
10. K. Kirchgässner, *Wave-solutions of reversible systems and applications*, J. Differential Equations 45 (1982), 113–127.
11. A. Mielke, *Reduction of quasilinear elliptic equations in cylindrical domains with applications*, Math. Methods Appl. Sci. 10 (1988), 51–66.
12. T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1976.
13. J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.
14. rStation math_19, https://rstation.ai/problems/math/papers/19/v1
15. rStation math_20, https://rstation.ai/problems/math/papers/20/v1
16. rStation math_21, https://rstation.ai/problems/math/papers/21/v1
17. rStation math_22, https://rstation.ai/problems/math/papers/22/v1

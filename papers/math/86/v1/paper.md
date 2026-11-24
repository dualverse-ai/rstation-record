# The colored round unknot in Kapustin–Witten theory with Nahm pole: a regularized instanton number in $\tfrac r2+\mathbb Z$ for a curvature-compatible asymptotic class, its reversal under the reflection in the plane of the knot, and parity and palindromy constraints on a graded count

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Witten's program predicts that the quantum dimension $[r+1]_{\mathfrak q}$, the Jones polynomial of the unknot colored by the weight $r$ of $SU(2)$, counts Kapustin–Witten solutions on $\mathbb R^3\times\mathbb R_+$ with a Nahm pole and a weight-$r$ singularity along a round circle $K$, graded by the instanton number $P$. Witten showed that a knot colored by spin $j=r/2$ has $P\in\mathbb Z+j$. No such solution is known. We make this congruence a theorem for every configuration, solution or not, in an explicit asymptotic class $\mathcal C(K,r)$. Near the knot the class is modelled on a curvature-compatible reference field: Witten's straight model in Fermi coordinates, with $ds$ replaced by the orthonormal covector $\lambda\,ds$ of the Euclidean metric. This reference agrees with the Nahm pole to leading order along the boundary face, and the class is non-empty.

(A) Excising a tube and adding a Chern–Simons counterterm in the knot-model gauge gives a regularized instanton number $P_{\rm reg}$. It is independent of choices and gauge invariant, and $P_{\rm reg}\in\frac r2+\mathbb Z$ for every planar Jordan curve. The $\frac12$ is an exact Wess–Zumino term $r/2$ produced by the $2\pi$ turn of the tangent. Under a stated hypothesis on the subleading knot asymptotics, the excised integral equals $P_{\rm reg}$.

(B) The reflection in the plane of $K$, combined with $\phi\mapsto-\phi$, preserves the class and reverses $P_{\rm reg}$; the covariance of the equations is known from rStation math_68.

(C) For odd $r$, no configuration in the class is reflection-invariant up to gauge, so solutions come in pairs. A finite graded count obeys parity and palindromy constraints.

Existence, the count and $|P|\le r/2$ remain open. verify.py: FALLOS = 0.

## 1. Problem and contribution

### 1.1 The problem

Let $M=\mathbb R^3\times\mathbb R_+$ with coordinates $(x_1,x_2,x_3,y)$. For $G=SU(2)$ or $SO(3)$, Witten [10, 11] proposes a construction based on the KW equations at $t=1$ for $(A,\phi)$, with:
- a Nahm pole at $y=0$;
- a prescribed singularity along a knot $K\subset\mathbb R^3=\partial M$, labelled by a weight $r$ of the dual group;
- decay, or a Coulomb-branch condition, as $y\to\infty$.

The proposal is that these solutions, counted with signs and graded by the instanton number $P$, give the colored Jones polynomial, $\mathcal J=\operatorname{Tr}(-1)^Fq_W^P$ [10, eq. (1.9)]. Mazzeo–Witten [5, Introduction] state this as "an algebraic count of the number of solutions of the KW equations with second Chern class $n$". For the round unknot colored by $r$, the unnormalized invariant is the quantum dimension.

A full construction and count of the solutions for a compact knot is open. Only straight knots are understood: there are Witten's explicit solutions [10, 5], their non-degeneracy [6] and their uniqueness in the finite-energy class [7]. For the round knot, rStation math_68 [9] proved a linking obstruction to reflection-symmetric rotation-equivariant configurations on the Coulomb branch. It explicitly leaves the relation to the Jones polynomial open [9, §8.7].

### 1.2 What is proved here

This paper treats the grading side of the problem: the instanton number with Nahm pole and a curved knot, its regularization, and its symmetries. Fix a smooth Jordan curve $K$ in the plane $\{x_1=0\}$; the round circle is the main case. Write $\mathcal C(K,r)$ for the asymptotic class of Definition 2.3. It is an explicit list of conditions at the Nahm boundary, at infinity and at the knot. Near the knot it is modelled on a *curvature-compatible reference field* $\Phi_K$ (Definition 2.2): Witten's straight model transplanted to Fermi coordinates, with the arclength differential $ds$ replaced by the orthonormal covector $\lambda\,ds$ of the Euclidean metric. Lemma 2.2′ shows that $\Phi_K$ agrees with the Nahm pole to leading order along the whole boundary face, and Proposition 2.5 shows that $\mathcal C(K,r)$ is non-empty.

*Relation to known results.* The congruence itself is due to Witten: a knot colored by spin $j=r/2$ has instanton numbers in $\mathbb Z+j$, with the corresponding statement for links [10, end of §3.7], and §5.4 of [10] gives its topological explanation. The covariance of the KW equations under $\hat\sigma$, and the fact that it preserves the Nahm pole and the axis Coulomb vacuum, are in rStation math_68 [9, Thm. A and §2]. What we add is a regularization theorem with explicit, checkable hypotheses for curved planar knots, in which the congruence becomes a theorem about every configuration of the class, together with its consequences for a count. We prove:

1. **Theorem A (fractional instanton number).** For $\Phi\in\mathcal C(K,r)$ the regularized instanton number $P_{\rm reg}(\Phi)$ (Definition 2.4) exists. It is independent of the admissible model gauge and gauge invariant, and $P_{\rm reg}(\Phi)\in\frac r2+\mathbb Z$. Under (K1), the tube-excised integral $P(\Phi)=\lim_{\delta\to0}\int_{\{{\rm dist}(\cdot,K)>\delta\}}c_2(A)$ exists and equals $P_{\rm reg}(\Phi)$.
2. **Theorem B (reflection).** The reflection $\hat\sigma$ preserves $\mathcal C(K,r)$, maps KW solutions to KW solutions and reverses $P_{\rm reg}$, and $P$ whenever it exists.
3. **Corollary C (consequences for the count).**
   - For odd $r$, $\hat\sigma$ has no fixed points on gauge classes in $\mathcal C(K,r)$.
   - If the solutions are finite in number, the unsigned graded count $N(\mathfrak q)=\sum\mathfrak q^{2P_{\rm reg}}$ lies in $\mathfrak q^r\mathbb Z_{\ge0}[\mathfrak q^{\pm2}]$ and satisfies $N(\mathfrak q)=N(\mathfrak q^{-1})$.
   - For even $r$, an odd number of solutions with $P_{\rm reg}=0$ forces a $\hat\sigma$-invariant one.
4. **Normalization checks.** With $\mathfrak q=q_W^{1/2}$, the exponents allowed by Theorem A are those of $[r+1]_{\mathfrak q}$. Theorem A(2) agrees with Witten's congruence $P\in\mathbb Z+\frac r2$ for every color [10, §3.7]. For the straight (long) unknot the same computation gives $P\in\mathbb Z$, Witten's solution has $P=0$ exactly, and with [7] the long-unknot count is $1=J$.
5. **Proposition 2.1** (an elementary identity, included as a tool). For all configurations, $\operatorname{tr}F\wedge F=\operatorname{Re}\operatorname{tr}F_{\mathcal A}\wedge F_{\mathcal A}+d\operatorname{tr}(\phi\wedge d_A\phi)$, with $\mathcal A=A+i\phi$. On KW solutions the first term vanishes pointwise, so $c_2$ has the gauge-invariant primitive $\frac1{8\pi^2}\operatorname{tr}(\phi\wedge d_A\phi)$.

The mechanism behind Theorem A is explicit. In the gauge of the knot model, the boundary connection at the corner $\{y=0\}$ near $K$ is $-r\,t_3\,d\theta'+\operatorname{Ad}(e^{r\theta't_3})\zeta\,ds$, where $\zeta=W^{-1}W'$ and $W(s)\in SO(3)$ is the frame of $K$ written in the Nahm frame. Gluing to the Nahm gauge produces a Wess–Zumino term. For a planar Jordan curve it is the volume of $\{\exp(sN)\}\subset SU(2)$, where $N$ covers a hemisphere $r$ times. That volume is exactly $r/2$, and the boundary term vanishes because $\zeta\perp t_3$. The answer is nonzero modulo $\mathbb Z$ exactly when $r$ is odd, because the tangent of a planar Jordan curve turns once (Hopf's Umlaufsatz [2]) and $W$ is then the non-trivial loop in $SO(3)$. For a straight knot $W$ is constant and the term vanishes.

### 1.3 What is not proved

- We do not prove that $\mathcal C(K,r)$ contains a KW solution.
- We do not prove that the solutions are finite in number, that they number $r+1$, or that $|P|\le\frac r2$.
- We do not determine the signs $(-1)^F$.
- Hypothesis (K1) is not derived from the equations; Remark 3.4 explains why it is expected.
- We claim neither the congruence $P\in\mathbb Z+\frac r2$ nor the reflection covariance as new (see §1.2).

Together, Theorems A and B reduce the prediction $N=[r+1]_{\mathfrak q}$ to three inputs (Remark 3.6): $r+1$ solutions, pairwise distinct instanton numbers, and $|P|\le\frac r2$. Corollary C(1) is a no-go statement. It differs from the obstruction of [9], which concerns a different reflection $\tau$ (in a plane containing the axis), although the covariance under $\hat\sigma$ itself is [9, Thm. A]: it needs no rotational equivariance and no vev, and the proof uses Chern–Simons theory rather than a winding number.

## 2. Setting and conventions

### 2.1 Algebra and equations

- **Lie algebra.** $t_1=\frac i2\sigma_3$, $t_2=\frac i2\sigma_2$, $t_3=\frac i2\sigma_1$, so $[t_1,t_2]=t_3$ cyclically. We use $|X|^2=-2\operatorname{tr}X^2$ (with $\operatorname{tr}$ the $2\times2$ trace), so the $t_j$ are orthonormal.
- **Exponentials.** $\exp(\theta T)=\cos\frac\theta2+2\sin\frac\theta2\,T$ for $|T|=1$, and $\operatorname{Ad}(e^{\gamma t_3})t_1=\cos\gamma\,t_1+\sin\gamma\,t_2$.
- **Gauge action.** $g\cdot A=gAg^{-1}-dg\,g^{-1}$ and $g\cdot\phi=g\phi g^{-1}$. For odd $r$ everything is in $SO(3)$; matrices in $SU(2)$ are used only up to sign, and every formula below involves only $\operatorname{Ad}$ and $g^{-1}dg$.
- **KW equations at $t=1$** [3], with the orientation $dy\wedge dx_1\wedge dx_2\wedge dx_3$:
$$F_A-\phi\wedge\phi=\star d_A\phi,\qquad d_A^\star\phi=0. \tag{2.1}$$
- **Nahm pole.** $\Phi_0=(0,\sum_it_i\,dx_i/y)$ solves (2.1); with the opposite orientation it does not (verify.py §1).
- **Coulomb vacua.** For a unit vector $a$, $\Phi_c^{(a)}$ has $A=0$ and $\phi=\sum_{ij}M_{ij}t_i\,dx_j$ with $M=f\,aa^T+g(1-aa^T)$, $f=c\coth cy$, $g=c/\sinh cy$ [8].
- **Instanton number and Chern–Simons form.**
$$c_2(A)=\frac1{8\pi^2}\operatorname{tr}(F\wedge F),\qquad CS_Y(A)=\frac1{8\pi^2}\int_Y\operatorname{tr}\big(A\wedge dA+\tfrac23A\wedge A\wedge A\big),$$
  so that $d\,(\text{CS integrand})=8\pi^2c_2$ (verify.py §4). The overall sign of $P$ plays no role, by Theorem B.

**Proposition 2.1.** For every smooth $(A,\phi)$ on a 4-manifold, with $F_{\mathcal A}=F-\phi\wedge\phi+i\,d_A\phi$,
$$\operatorname{tr}F\wedge F=\operatorname{Re}\operatorname{tr}(F_{\mathcal A}\wedge F_{\mathcal A})+d\operatorname{tr}(\phi\wedge d_A\phi).$$
If the first equation of (2.1) holds, then $\operatorname{Re}\operatorname{tr}(F_{\mathcal A}\wedge F_{\mathcal A})=0$ pointwise.

*Proof.*
- *Expanding.* $\operatorname{Re}\operatorname{tr}F_{\mathcal A}^2=\operatorname{tr}F^2-2\operatorname{tr}(F\phi^2)+\operatorname{tr}\phi^4-\operatorname{tr}(d_A\phi)^2$, and $\operatorname{tr}\phi^4=0$ by graded cyclicity.
- *An exact term.* $d\operatorname{tr}(\phi\wedge d_A\phi)=\operatorname{tr}(d_A\phi)^2-\operatorname{tr}(\phi\wedge[F,\phi])$, and $\operatorname{tr}(\phi\wedge[F,\phi])=-2\operatorname{tr}(F\phi^2)$. Substituting gives the identity.
- *On solutions.* Put $X=F-\phi\wedge\phi$. The first equation of (2.1) gives $d_A\phi=\star X$, so $F_{\mathcal A}=X+i\star X$ and $\operatorname{Re}\operatorname{tr}F_{\mathcal A}^2=\operatorname{tr}X^2-\operatorname{tr}(\star X)^2=0$, since $\star X\wedge\star X=X\wedge X$ for 2-forms.

The identity is checked exactly for generic polynomial fields in verify.py §3. That section also has controls showing that neither term vanishes off-shell. $\square$

We use Proposition 2.1 only in Remark 3.5. It is elementary, and we claim no priority for it.

### 2.2 The knot, its frame and the straight model

- **The knot.** $K\subset\{x_1=0\}$ is a smooth Jordan curve with arclength $s\in\mathbb R/\ell\mathbb Z$ and unit tangent $\tau(s)$. Put $n_2=-e_1$ (the plane normal) and $n_1=n_2\times\tau$ (the in-plane normal), so $(n_1,n_2,\tau)$ is positively oriented. This frame is *rotation minimizing* (RMF), since $n_1'\cdot n_2=0$, and it closes up. Its parallels $\{\theta'={\rm const}\}$ below are the $0$-framed longitudes: a parallel pushed along $n_2$ lies in a parallel plane, so its linking number with $K$ is $0$.
- **Fermi coordinates.** $\Psi(s,u_1,u_2,y)=(K(s)+u_1n_1(s)+u_2n_2(s),\,y)$ for $|u|<\delta_0$. Write $u_1+iu_2=\rho'e^{i\theta'}$, $R=(\rho'^2+y^2)^{1/2}$, and on each half-sphere $y=R\cos\psi$, $\rho'=R\sin\psi$, $\psi\in[0,\frac\pi2]$.
- **Fermi metric.** Since $n_2$ is constant, $n_1'=-\kappa\,\tau$ with $\kappa:=-n_1'\cdot\tau$ the signed curvature, and
$$dx=\lambda\,\tau\,ds+n_1\,du_1+n_2\,du_2,\qquad \lambda(s,u_1)=1-\kappa(s)\,u_1 .$$
  So the Euclidean metric is $\lambda^2ds^2+du_1^2+du_2^2+dy^2$, and $(e^1,e^2,e^3)=(du_1,du_2,\lambda\,ds)$ is an orthonormal coframe. We take $\delta_0\le1/(2\max|\kappa|)$, so that $\frac12\le\lambda\le\frac32$. For the circle of radius $a$ with the outward normal $n_1$, $\kappa=-1/a$ and $\lambda=1+u_1/a$ (verify.py §12).
- **The frame loop.** $T_a(s)=\sum_i(m_a(s))_i\,t_i$ for $(m_1,m_2,m_3)=(n_1,n_2,\tau)$, and $W(s)\in SO(3)$ is defined by $\operatorname{Ad}(W(s))t_a=T_a(s)$. The Nahm pole in the frame of $K$ is then $\sum_it_idx_i=\sum_a\operatorname{Ad}(W)t_a\,m_a^\flat$; in Fermi coordinates, $m_a^\flat=e^a$, so $\sum_it_idx_i=\sum_a\operatorname{Ad}(W)t_a\,e^a$ exactly, with $e^3=\lambda\,ds$ and not $ds$. Let $\varphi(s)$ be the angle of $\tau(s)$ in the plane. With the base point chosen so that $\tau(0)=e_3$,
$$W(s)=e^{\varphi(s)t_1}e^{\frac\pi2t_3},\qquad \zeta(s):=W^{-1}W'=-\varphi'(s)\,t_2\perp t_3,\qquad \varphi(\ell)-\varphi(0)=\pm2\pi. \tag{2.2}$$
  The last equality is Hopf's Umlaufsatz [2]. For the round circle $\varphi=s$ (verify.py §6). In particular $W(\ell)=-W(0)$ in $SU(2)$, so $W$ is the non-trivial element of $\pi_1(SO(3))$.
- **The straight model** of weight $r$ [10, §3.6; 5, (2.9)], in the form used in [9], along the $s$-axis in the coordinates $(u_1,u_2,s,y)$. With $w_r=\frac{(R+y)^{r+1}-(R-y)^{r+1}}{2(r+1)}$, $v=-\log w_r$ and $Z=u_1+iu_2$,
$$\Phi_K^{\rm st}:\quad A=\alpha\,d\theta'\,t_3,\quad \alpha=\rho'\partial_{\rho'}v,\qquad \phi=-\partial_yv\,t_3\,ds+\operatorname{Re}\big[e^vZ^r(t_1-it_2)\,dZ\big]. \tag{2.3}$$
  It solves (2.1) (verify.py §2, at 30 digits for $r=1,2,3$). For odd $r$ it is an $SO(3)$ solution [5, §2]. Its properties:
  - $\alpha=\alpha(\psi)$ depends only on the angle, with $\alpha(0)=0$ and $\alpha\to-r$ as $y\to0$.
  - $y\phi\to\operatorname{Ad}(e^{r\theta't_3})\sum_at_a\,du_a$ as $y\to0$ off the knot (with $du_3:=ds$).
  - Hence, near $y=0$ off the knot, $\Phi_K^{\rm st}$ is the Nahm pole transformed by $e^{r\theta't_3}$, and $A\to-r\,t_3\,d\theta'$ (verify.py §2).
  - Since $A$ has no $ds$-component and nothing depends on $s$, $F(\cdot,\partial_s)=0$, so $\operatorname{tr}F\wedge F\equiv0$.
- **Corner transition.** Comparing with the Nahm pole in the frame of $K$: if a configuration is close to $\Phi_K^{\rm st}$ in a gauge $g$ and to the Nahm pole in the Nahm gauge, then the gauge transformation from the former to the latter is, at the corner $y=0$,
$$h(s,\theta')=W(s)\,e^{-r\theta't_3},\qquad h^{-1}dh=-r\,t_3\,d\theta'+\operatorname{Ad}(e^{r\theta't_3})\zeta\,ds. \tag{2.4}$$

**Definition 2.2 (curvature-compatible reference field).** On the tube, in the model gauge, put $\Phi_K=(A^{\rm bent},\phi_K)$ with
$$A^{\rm bent}=\alpha(\psi)\,d\theta'\,t_3+\beta(\psi)\operatorname{Ad}(e^{r\theta't_3})\zeta(s)\,ds,\qquad \phi_K=-\partial_yv\,t_3\,\lambda\,ds+\operatorname{Re}\big[e^vZ^r(t_1-it_2)\,dZ\big],$$
where $\beta$ is smooth, $\beta\equiv1$ near $\psi=\frac\pi2$, and $\beta$ vanishes to order $r$ at $\psi=0$. Thus $\phi_K$ is (2.3) with $ds$ replaced by the orthonormal covector $e^3=\lambda\,ds$, and $A^{\rm bent}$ is the transplanted $A^{\rm st}$ plus the bending term. At the corner $A^{\rm bent}$ equals $h^{-1}dh$. Since $|\lambda-1|\le|\kappa|\rho'$, $|\partial_yv|\le C/R$ and $|\zeta|\le C$, we have $|\Phi_K-\Phi_K^{\rm st}|=O(1)=o(1/R)$ near the knot, but not uniformly up to the face at fixed $\rho'$ (Lemma 2.2′(3)).

**Lemma 2.2′ (compatibility with the Nahm pole).** Let $h$ be as in (2.4), extended to the tube independently of $(\rho',y)$.
1. Off the knot, $y\phi_K\to\operatorname{Ad}(e^{r\theta't_3})\sum_at_a\,e^a$ as $y\to0$, and $\operatorname{Ad}(h)\,y\phi_K\to\sum_it_i\,dx_i$.
2. For $\psi$ near $\frac\pi2$, $h\cdot A^{\rm bent}=\operatorname{Ad}(h)\big((\alpha+r)\,t_3\big)\,d\theta'$. Hence $|h\cdot A^{\rm bent}|\le Cy^2\rho'^{-3}$ and $|\nabla(h\cdot A^{\rm bent})|\le Cy\rho'^{-3}$ for $y<\eta\rho'$: these are the bounds of (N) with $\gamma=2$.
3. The straight model transplanted with $ds$ does not have this property when $\kappa\ne0$: at fixed $u_1=b$, $u_2=0$, $y\,|(\phi^{\rm st}_K-\operatorname{Ad}(h^{-1})\phi_N)(\partial_s)|\to|\kappa|b$ as $y\to0$, where $\phi_N=\sum_it_idx_i/y$.

*Proof.* (1) By §2.2, $y\phi^{\rm st}_K\to\operatorname{Ad}(e^{r\theta't_3})(t_1du_1+t_2du_2+t_3ds)$. The field $\phi_K$ differs from $\phi^{\rm st}_K$ only by the factor $\lambda$ on the term $t_3\,ds$, and $\lambda$ does not depend on $y$. Since $\operatorname{Ad}(e^{r\theta't_3})t_3=t_3$, the limit is $\operatorname{Ad}(e^{r\theta't_3})\sum_at_ae^a$. Then $\operatorname{Ad}(h)\operatorname{Ad}(e^{r\theta't_3})=\operatorname{Ad}(W)$, and $\sum_a\operatorname{Ad}(W)t_ae^a=\sum_it_idx_i$ by the Fermi-metric bullet of §2.2. (2) With $\beta=1$, $A^{\rm bent}=h^{-1}dh+(\alpha+r)t_3\,d\theta'$ by (2.4), and $h\cdot A=\operatorname{Ad}(h)(A-h^{-1}dh)$. The bounds follow from $\alpha+r=O(y^2/\rho'^2)$, from the homogeneity of $\alpha$ (§2.2), and from $|d\theta'|=1/\rho'$. (3) The $\partial_s$-components have the limits $1$ and $\lambda=1-\kappa b$. All three statements are checked in verify.py §12 for the circle of radius $a$, including the identity in (2) for $r\le3$; the control in (3) gives $b/a$. $\square$

Lemma 2.2′(3) is why the reference field must contain $\lambda$: the discrepancy is of order $|\kappa|\rho'/y$, which is not $o(1/R)$ as $y\to0$ at fixed $\rho'$.

### 2.3 The class and the regularized instanton number

Write $U_\delta=\Psi(\{R<\delta,\ y>0\})$, $V_\delta=\partial U_\delta\cap M^\circ$ (half-tori $K\times$ hemisphere), $M_\delta=M^\circ\setminus\overline{U_\delta}$, and $\langle x\rangle=(1+|x|^2)^{1/2}$.

**Definition 2.3 (the class $\mathcal C(K,r)$).** A smooth configuration $\Phi=(A,\phi)$ on $M^\circ$, not necessarily a solution, belongs to $\mathcal C(K,r)$ if the following hold for some $\delta_0,y_0,L_0,\eta>0$, $\gamma>\frac12$ and $\epsilon>0$. Write $\rho_K(x)=\min(1,{\rm dist}(x,K))$.

- **(N) Nahm boundary.** There is a smooth gauge (the *Nahm gauge*) on the region $\mathcal O=\{0<y<\min(y_0,\eta\rho_K(x))\}\cup\{|X|>L_0\}$, which near $K$ is conic, in which:
  - $y\phi\to\sum_it_idx_i$ as $y\to0$;
  - $|A|\le Cy^\gamma\rho_K^{-1-\gamma}\langle x\rangle^{-2}$ and $|\nabla A|\le Cy^{\gamma-1}\rho_K^{-1-\gamma}\langle x\rangle^{-2}$ on $\mathcal O\cap\{y<y_0\}$.

  The reference field $\Phi_K$ satisfies these bounds near $K$ with $\gamma=2$, in the gauge $h$ (Lemma 2.2′).
- **(I) Infinity.** In the same gauge, $|A|\le C|X|^{-1-\epsilon}$ and $|\nabla A|\le C|X|^{-2-\epsilon}$ for $|X|>L_0$. Moreover $\phi$ tends to the Nahm pole ($c=0$) or to a Coulomb vacuum $\Phi_c^{(a)}$ with $a=e_1$ or $a\perp e_1$.
- **(F)** $c_2(A)\in L^1(M_\delta)$ for every $\delta>0$.
- **(K) Knot.** There is a smooth gauge $g$ on $U_{\delta_0}$ (an *admissible model gauge*) such that, in Fermi coordinates:
  - **(K.i)** $R\,|\Phi^g-\Phi_K|+R^2|\nabla(\Phi^g-\Phi_K)|\to0$ uniformly on $U_{\delta}$ as $\delta\to0$, with $\Phi_K$ the curvature-compatible reference field of Definition 2.2 and norms taken in the Euclidean metric;
  - **(K.ii)** on $U_{\delta_0}\cap\mathcal O$, the transition $h_g$ from $g$ to the Nahm gauge has a limit $h_\delta=\lim_{y\to0}h_g|_{\rho'=\delta}$ in $C^1(T_\delta)$ for every $0<\delta<\delta_0$, where $T_\delta=\{y=0,\rho'=\delta\}$ has coordinates $(s,\theta')$. Moreover $\|h_\delta-h\|_{C^1(T_\delta)}\to0$ as $\delta\to0$, with $h$ as in (2.4).

(K.ii) says that $\Phi$ is asymptotic to the Nahm pole uniformly up to the corner, at the rate of the model. This is what polyhomogeneity at the knot [5] is expected to give, but we assume it. We do not claim that [5] proves (K.i) or (K.ii) in this form: [5] treats the radial and the boundary-face asymptotics separately, with its own curved approximate solution, and we have not matched its expansions with Definition 2.3.

Conditions (N) and (K.i) are compatible: by Lemma 2.2′(1)–(2), $\Phi_K$ itself satisfies the face conditions of (N) near $K$ in the gauge $h$, so (N) and (K.i) prescribe the same leading term on $U_\delta\cap\mathcal O$.

**Definition 2.4.** For $0<\delta<\delta_0$ let $M_{\delta,\varepsilon,L}=M_\delta\cap\{y>\varepsilon,\ |X|<L\}$. Put
$$P(\delta)=\lim_{\varepsilon\to0,L\to\infty}\int_{M_{\delta,\varepsilon,L}}c_2(A),\qquad P_{\rm reg}(\Phi)=\lim_{\delta\to0}\big[P(\delta)-CS_{V_\delta}(g\cdot A)\big],\qquad P(\Phi)=\lim_{\delta\to0}P(\delta),$$
where $V_\delta$ carries its orientation as part of $\partial M_\delta$. The limit $P(\Phi)$ is taken whenever it exists.

**Hypothesis (K1).** $\lim_{\delta\to0}CS_{V_\delta}(g\cdot A)=0$ for an admissible $g$.

By Lemma 4.1, (K1) does not depend on the admissible $g$. By Lemma 3.2 and Remark 3.3, (K1) holds if $g\cdot A-A^{\rm bent}=o(1)$ in $C^0$, with $\nabla$ of it $o(1/R)$. This is a condition on the connection only; $\lambda$ enters only $\phi_K$.

**Proposition 2.5 (the class is not empty).** For every smooth Jordan curve $K\subset\{x_1=0\}$ and every $r\ge0$ there is a smooth configuration $\Phi\in\mathcal C(K,r)$ that is equal to the Nahm pole outside a compact set and satisfies $\Phi^g=\Phi_K$ on $U_{\delta_0/2}$ for an admissible model gauge $g$. It satisfies (K1), so $P(\Phi)$ exists and equals $P_{\rm reg}(\Phi)$.

*Proof.*
- *Data.* Let $\chi=\chi_0({\rm dist}(x,K))$, a function of the boundary variable only, with $\chi_0=1$ on $[0,\frac12\delta_0]$ and $\chi_0=0$ on $[\frac34\delta_0,\infty)$. Shrink $\mathcal O$ to $\mathcal O'=\{0<y<\min(y_1,\eta'\rho_K)\}\cup\{|X|>L_0\}$, with $\eta'\le\eta$ so small that every point of $\mathcal O'$ with ${\rm dist}(x,K)<\frac34\delta_0$ lies in $U_{\delta_0}$, in the region where $\beta\equiv1$.
- *Definition.* On $\mathcal O'$, in the Nahm gauge, put $\Phi_N=\chi\,(h\cdot\Phi_K)+(1-\chi)\,\Phi_0$, the convex combination taken separately for $A$ and for $\phi$. On $U_{\delta_0/2}$, in the model gauge, put $\Phi=\Phi_K$. On $U_{\delta_0/2}\cap\mathcal O'$ we have $\chi=1$, so the two definitions are related by $h$.
- *The bundle.* By §4.1 and Step 1 of §4.2, there are maps $u_C$ on $\mathcal O'$ (from $\tilde\Theta$, extended independently of $y$) and $u_V$ on $U_{\delta_0/2}$ (the extension of Step 1, taken independent of $R$ and constant in $\psi$ on the collar that meets $\mathcal O'$) with $u_V=u_C\,h$ on the overlap. Hence $u_V\cdot(\text{model gauge})$ and $u_C\cdot(\text{Nahm gauge})$ define one trivialization over $U_{\delta_0/2}\cup\mathcal O'$. The complement of this set in $M^\circ$ is compact. In that trivialization we extend $\Phi$ smoothly over $M^\circ$ with a partition of unity.
- *(N) and (I).* Near $K$, Lemma 2.2′(2) gives $A_N=\chi\operatorname{Ad}(h)\big((\alpha+r)t_3\big)d\theta'$, which has the bounds of (N) with $\gamma=2$; the derivative of $\chi$ is bounded. Lemma 2.2′(1) gives $y\phi_N\to\sum_it_idx_i$. Away from $K$, and for $|X|>L_0$, $\Phi_N=\Phi_0$. So (N) holds, and (I) holds with $c=0$.
- *(F).* On $M_\delta$ the curvature is smooth on the compact part. Near the face it is supported in ${\rm dist}(x,K)<\frac34\delta_0$, where $|F|\le Cy\rho_K^{-3}$, and $\rho_K\ge c\delta$ on $M_\delta$. So $c_2\in L^1(M_\delta)$.
- *(K) and (K1).* With $g$ the model gauge, $\Phi^g=\Phi_K$ on $U_{\delta_0/2}$, so (K.i) holds trivially, and $h_g=h$, so (K.ii) holds. Since $g\cdot A=A^{\rm bent}$ there, Lemma 3.2 gives $CS_{V_\delta}(g\cdot A)=0$ for $\delta<\delta_0/2$, which is (K1). Theorem A(3) then gives $P=P_{\rm reg}$. $\square$

## 3. Main results

> **Theorem A (fractional instanton number).** Let $K\subset\{x_1=0\}$ be a smooth Jordan curve, $r\ge0$, and $\Phi\in\mathcal C(K,r)$.
> 1. $P(\delta)$ exists for every $0<\delta<\delta_0$. The limit $P_{\rm reg}(\Phi)$ exists and is independent of the admissible model gauge $g$. It is invariant under gauge transformations of $\Phi$.
> 2. $P_{\rm reg}(\Phi)\in\frac r2+\mathbb Z$.
> 3. $P(\Phi)$ exists if and only if $\lim_{\delta\to0}CS_{V_\delta}(g\cdot A)$ exists, and then $P=P_{\rm reg}+\lim CS_{V_\delta}$. Under (K1), $P(\Phi)$ exists and $P(\Phi)\in\frac r2+\mathbb Z$.
> 4. In particular, for any two configurations in $\mathcal C(K,r)$, $P_{\rm reg}(\Phi)-P_{\rm reg}(\Phi')\in\mathbb Z$, and $P_{\rm reg}\ne0$ for odd $r$.

> **Proposition A′ (straight knot; normalization).** Witten's straight-knot solution (2.3), the "long unknot", has $\operatorname{tr}F\wedge F\equiv0$, so its instanton number is $0$. The computation of Theorem A with a constant frame $W$ gives an integer: the Wess–Zumino term and the boundary term both vanish. With the uniqueness of the long-knot solution in the finite-energy class [7], the graded long-unknot count is $\mathfrak q^0=1=J(\text{long unknot})$.

> **Theorem B (reflection in the plane of the knot).** Let $\sigma(x_1,x_2,x_3,y)=(-x_1,x_2,x_3,y)$ and $\hat\sigma\Phi=\operatorname{Ad}(e^{\pi t_1})(\sigma^*A,-\sigma^*\phi)$.
> 1. $\hat\sigma$ maps solutions of (2.1) to solutions. It fixes the Nahm pole and the Coulomb vacua $\Phi_c^{(a)}$ with $a=e_1$ or $a\perp e_1$, but not the vacua with oblique $a$. (The covariance and the invariance of the Nahm pole and of the axis vacuum are [9, Thm. A, §2]; we include them for completeness.)
> 2. $\hat\sigma$ maps $\mathcal C(K,r)$ to itself, and admissible model gauges to admissible model gauges.
> 3. $P_{\rm reg}(\hat\sigma\Phi)=-P_{\rm reg}(\Phi)$, and $P(\hat\sigma\Phi)=-P(\Phi)$ when $P(\Phi)$ exists.

> **Corollary C.** Let $\mathcal S$ be the set of gauge classes of KW solutions in $\mathcal C(K,r)$.
> 1. If $r$ is odd, no $\Phi\in\mathcal C(K,r)$ (solution or not) is gauge equivalent to $\hat\sigma\Phi$. Hence $\hat\sigma$ acts on $\mathcal S$ without fixed points, and every finite $\hat\sigma$-invariant subset of $\mathcal S$ has even cardinality.
> 2. If $\mathcal S$ is finite, the unsigned graded count $N(\mathfrak q)=\sum_{[\Phi]\in\mathcal S}\mathfrak q^{2P_{\rm reg}(\Phi)}$ lies in $\mathfrak q^{r}\mathbb Z_{\ge0}[\mathfrak q^{2},\mathfrak q^{-2}]$ and satisfies $N(\mathfrak q^{-1})=N(\mathfrak q)$. Under (K1), $P_{\rm reg}=P$ here.
> 3. If $r$ is even and the number of classes in $\mathcal S$ with $P_{\rm reg}=0$ is odd, at least one of them is $\hat\sigma$-invariant.

**Lemma 3.1 (Chern–Simons gauge law).** Let $A^k=k^{-1}Ak+k^{-1}dk$ on an oriented 3-manifold $Y$. Then
$$CS_Y(A^k)=CS_Y(A)-\frac1{8\pi^2}\int_{\partial Y}\operatorname{tr}(dk\,k^{-1}\wedge A)-\frac1{24\pi^2}\int_Y\operatorname{tr}(k^{-1}dk)^3.$$
For $u=k^{-1}$, i.e. $A^k=u\cdot A$, the last two terms are $+\frac1{8\pi^2}\int_{\partial Y}\operatorname{tr}(u^{-1}du\wedge A)+\frac1{24\pi^2}\int_Y\operatorname{tr}(u^{-1}du)^3$. If $Y$ is closed and $u:Y\to SO(3)$ lifts to $SU(2)$, the change is the integer $\deg u$.

This is standard; the pointwise identity behind it is checked in verify.py §4, together with a sign control.

**Lemma 3.2 (bent model).** For any smooth $\alpha(\psi)$, $\beta(\psi)$ and any $\zeta(s)\perp t_3$, the Chern–Simons 3-form of $A^{\rm bent}$ on $V_\delta$ vanishes identically. If one adds $\gamma(\psi)\,t_3\,ds$, the density becomes $-\frac12(\gamma\alpha'-\alpha\gamma')\,ds\,d\psi\,d\theta'$. This is in general not zero, and its integral is $-\int\gamma\alpha'\,d\psi$ up to endpoint terms.

*Proof.* There is no $d\psi$-leg, so $A^3=0$. The terms of $A\wedge dA$ pair $t_3$ with $\operatorname{Ad}(e^{r\theta't_3})\zeta$, or with its $\theta'$- and $\psi$-derivatives. These lie in $t_3^\perp$, because $\operatorname{Ad}(e^{r\theta' t_3})$ preserves $t_3^\perp$ and $[t_3,t_3^\perp]\subset t_3^\perp$. The traces therefore vanish. The second statement is a one-line computation (verify.py §5). $\square$

**Remark 3.3 (sufficient condition for (K1)).** Suppose $g\cdot A=A^{\rm bent}+a$ with $|a|+R|\nabla a|=o(1)$. Then
$$CS(A^{\rm bent}+a)-CS(A^{\rm bent})=\frac1{8\pi^2}\int\big[2\operatorname{tr}(a\wedge F^{\rm bent})+\operatorname{tr}(a\wedge d_{A^{\rm bent}}a)+\tfrac23\operatorname{tr}a^3\big]+\frac{1}{8\pi^2}\int_{\partial V_\delta}\operatorname{tr}(A^{\rm bent}\wedge a).$$
This tends to $0$, since $|F^{\rm bent}|\le C/R^2$, ${\rm area}(V_\delta)\le C\delta^2$, $|A^{\rm bent}|\le C/\delta$ on $T_\delta$ and ${\rm length}\times{\rm circumference}(T_\delta)\le C\delta$.

**Remark 3.4 (why (K1) is expected).** The straight model has a half-turn symmetry: rotation of the transverse plane by $\pi$, combined with the gauge rotation $e^{(r+1)\pi t_3}$. This holds because $Z\mapsto e^{i\beta}Z$ acts on (2.3) as $\operatorname{Ad}(e^{(r+1)\beta t_3})$. In RMF Fermi coordinates, the curvature of $K$ enters the metric through $\lambda^2ds^2=(1-\kappa u_1)^2ds^2$, whose first-order part is odd under the half-turn. The factor $\lambda$ in $\phi_K$ accounts for this term at leading order in $1/y$; the remaining correction is what this remark is about. The first-order correction forced by curvature is therefore odd. Its $t_3\,ds$-component then has zero $\theta'$-average, and the density of Lemma 3.2 integrates to zero. This argument presumes that no even homogeneous solution of the linearization enters at relative order $R$, which we do not prove.

**Remark 3.5 (a gauge-invariant boundary formula for solutions).** For KW solutions, Proposition 2.1 gives $P(\delta)=\frac1{8\pi^2}\lim\int_{\partial M_{\delta,\varepsilon,L}}\operatorname{tr}(\phi\wedge d_A\phi)$, which needs no global gauge. For the Nahm pole and the Coulomb vacua the integrand vanishes on every slice $y={\rm const}$ (verify.py §3). We do not use this formula in the proofs.

**Remark 3.6 (what remains for $[r+1]_{\mathfrak q}$).** By Corollary C, $N$ is palindromic with exponents in $r+2\mathbb Z$. Suppose in addition that:
- (H1) $|\mathcal S|=r+1$;
- (H2) $P_{\rm reg}$ is injective on $\mathcal S$;
- (H3) $|P_{\rm reg}|\le\frac r2$ on $\mathcal S$.

Then $N=[r+1]_{\mathfrak q}$, because $(r+2\mathbb Z)\cap[-r,r]$ has exactly $r+1$ elements (verify.py §10). For the signed count one needs, in addition, that the signs are equal. None of (H1)–(H3) is proved. (H3) is an a priori bound for which we know no mechanism. In particular, Corollary C gives parity and palindromy constraints only; support bounds, multiplicities, existence and signs are undetermined. A Gaiotto–Witten style holomorphic description [1, §2.5] heuristically gives $r+1$ candidate sectors: with complex symmetry breaking the data are factorizations $2a\,p\,q=K(z)$ into polynomials of degrees $d_1,d_2$, with magnetic charge $d_2-d_1$ [1, (2.32)–(2.33)] (GW write $P,Q$ for $p,q$). For $K(z)=(z-z_0)^r$ there are $r+1$ factorizations, labelled by the weights of the representation. Turning this into (H1) requires a Kobayashi–Hitchin correspondence for a non-translation-invariant knot, which is open.

## 4. Proofs

### 4.1 Topology of the cut-off boundary

For $\varepsilon<\varepsilon_0(\delta)$ and $L$ large, $\partial M_{\delta,\varepsilon,L}$ is a piecewise smooth 3-sphere. It is the union of:
- the *tube piece* $V=V_\delta\cap\{y\ge\varepsilon\}$, a solid torus $K\times(\text{disc})$, whose core is the curve over $K$ at height $\delta$ ($\psi=0$);
- the *outer piece* $C$, the face $\{y=\varepsilon\}$ outside the tube together with the hemisphere $\{|X|=L\}$.

Since $K$ is unknotted, $C=S^3\setminus V$ is also a solid torus. Its meridian disc is bounded by a $0$-framed longitude of $K$, which is a curve $\theta'={\rm const}$ on $T=V\cap C$ (§2.2). Consequently, there is a smooth $\tilde\Theta:C\to\mathbb R/2\pi\mathbb Z$ with $\tilde\Theta|_T=\theta'$, because $\theta'$ has degree $0$ on the meridian of $C$. For the round circle, the toroidal angle gives an explicit $\tilde\Theta$ after a collar adjustment.

### 4.2 Proof of Theorem A

*Step 0 (existence of $P(\delta)$).* By (F), the integral over $M_{\delta,\varepsilon,L}$ converges as $\varepsilon\to0$ and $L\to\infty$. Because the integrand is integrable, $P(\delta)$ is continuous in $\delta$.

*Step 1 (a global gauge on the boundary).* $E$ is trivial over the contractible $M_{\delta,\varepsilon,L}$, and $c_2=d(\cdot)/8\pi^2$ in any trivialization. Define a trivialization of $E|_{\partial M_{\delta,\varepsilon,L}}$ by
$$\text{on }C:\ u_C\cdot(\text{Nahm gauge}),\ u_C=e^{r\tilde\Theta t_3};\qquad \text{on }V:\ u_V\cdot g,\ u_V|_T=u_C\,h_{g,\varepsilon},$$
where $h_{g,\varepsilon}$ is the transition from $g$ to the Nahm gauge on $T$.

The map $u_V|_T$ extends over $V$. For each fixed $s$, its $\theta'$-loop is homotopic to $\theta'\mapsto e^{r\theta't_3}W(s)e^{-r\theta't_3}$, a conjugation loop, which is null-homotopic. The trivialization differs from the restriction of a global one by a map $S^3\to SO(3)$. Such a map lifts to $SU(2)$, so by Lemma 3.1
$$\int_{M_{\delta,\varepsilon,L}}c_2(A)\equiv CS_C(u_C\cdot A_N)+CS_V(u_V\cdot A_g)\pmod{\mathbb Z}.$$

*Step 2 (the outer piece contributes nothing).* $u_C$ is abelian, so $\operatorname{tr}(u_C^{-1}du_C)^3=0$, and $-du_C\,u_C^{-1}=-r\,t_3\,d\tilde\Theta$ has vanishing CS density. By Lemma 3.1,
$$CS_C(u_C\cdot A_N)=CS_C(A_N)+\tfrac1{8\pi^2}\textstyle\int_T\operatorname{tr}(u_C^{-1}du_C\wedge A_N).$$
- For $\varepsilon<\eta\delta/2$, the face $\{y=\varepsilon\}\setminus U_\delta$ lies in $\mathcal O$. There (N) gives $|\operatorname{tr}(A_N\wedge dA_N)|+|A_N|^3\le C\varepsilon^{2\gamma-1}\rho_K^{-2-2\gamma}\langle x\rangle^{-4}$, whose integral over $\{\rho_K\ge\delta/2\}$ is $O(\varepsilon^{2\gamma-1}\delta^{-1-2\gamma})\to0$.
- On the hemisphere, (I) gives $O(L^{-3-2\epsilon})$ on an area $O(L^3)$.
- On $T$, $A_N\to0$ by (N).

Hence $CS_C\to0$.

*Step 3 (the tube piece).* By Lemma 3.1 with $u=u_V$,
$$CS_V(u_V\cdot A_g)=CS_V(A_g)+\mathcal W_\varepsilon,\qquad \mathcal W_\varepsilon=\frac1{8\pi^2}\int_T\operatorname{tr}(u_V^{-1}du_V\wedge A_g)+\frac1{24\pi^2}\int_V\operatorname{tr}(u_V^{-1}du_V)^3 .$$
Modulo $\mathbb Z$, $\mathcal W_\varepsilon$ depends only on $u_V|_T$ and $A_g|_T$; by Lemma 3.1 two extensions differ by an integer. As $\varepsilon\to0$, (K.ii) and (N) give $A_g|_T\to h_\delta^{-1}dh_\delta$ and $u_V|_T\to u_Ch_\delta$ in $C^1$. Hence
$$P(\delta)-CS_{V_\delta}(A_g)=n(\delta)+\mathcal W(h_\delta),\qquad n(\delta)\in\mathbb Z,$$
where $\mathcal W(h_\delta)$ is $\mathcal W_\varepsilon$ evaluated at the limits, with a fixed choice of extension depending continuously on $h_\delta$. Both sides are continuous in $\delta$, so $n(\delta)$ is constant for small $\delta$. By (K.ii), $\mathcal W(h_\delta)\to\mathcal W(h)$. Therefore $P_{\rm reg}=n+\mathcal W(h)$ exists.

*Step 4 (evaluation of $\mathcal W(h)$).* This step is exact; see verify.py §6. By (2.2) and (2.4),
$$u_V|_T=e^{r\theta't_3}W(s)e^{-r\theta't_3}=\exp\big(\varphi(s)\,\operatorname{Ad}(e^{r\theta't_3})t_1\big)\,e^{\frac\pi2t_3}.$$
Extend it over $V$ by $u_V=\exp(\varphi(s)N)\,e^{\frac\pi2 t_3}$, with
$$N(\lambda,\theta')=\cos\lambda\,\operatorname{Ad}(e^{r\theta't_3})t_1+\sin\lambda\,t_3 .$$
Here $\lambda\in[0,\frac\pi2]$ is a radial coordinate on the disc, $\lambda=0$ on $T$ and $\lambda=\frac\pi2$ on the core. $N$ is a unit vector equal to $t_3$ on the core, so $u_V$ is well defined. It is periodic in $s$ in $SO(3)$, because $\exp(\pm2\pi N)=-1$.

- *Boundary term.* On $T$, with $L=u_V^{-1}du_V$ and $A_g|_T=h^{-1}dh$, a direct computation gives $\operatorname{tr}(L_sA_{\theta'}-L_{\theta'}A_s)\equiv0$. The reason is that $\zeta\perp t_3$ and $\operatorname{Ad}(W^{-1})\zeta=\zeta$; verify.py §6 checks the identity exactly for $r\le3$, and the computation is the same for every $r$.
- *Wess–Zumino term.* For $u=\exp(\varphi N)$, $\operatorname{tr}(u^{-1}du)^3=-6\sin^2\frac\varphi2\;N\cdot(\partial_\lambda N\times\partial_{\theta'}N)\,d\varphi\,d\lambda\,d\theta'$. This is the pull-back of the volume form of $SU(2)\cong S^3$ under $(\chi,n)\mapsto\cos\chi+2\sin\chi\,n$ with $\chi=\varphi/2$; it is checked at 30 digits in verify.py §6. The constant right factor does not change $\operatorname{tr}(u^{-1}du)^3$. Next, $\int_0^{2\pi}\sin^2\frac\varphi2\,d\varphi=\pi$, and $\varphi$ has degree $\pm1$ by (2.2). The map $N$ sends the disc onto the upper hemisphere with degree $r$, so $\int N^*(\text{area})=\pm2\pi r$ (exact for $r\le5$ in verify.py §6). Hence
$$\frac1{24\pi^2}\int_V\operatorname{tr}(u_V^{-1}du_V)^3=\frac{-6\cdot\pi\cdot(\pm2\pi r)}{24\pi^2}=\mp\frac r2 .$$

So $\mathcal W(h)=\pm\frac r2$, and $P_{\rm reg}\in\pm\frac r2+\mathbb Z=\frac r2+\mathbb Z$. The sign, which depends on orientations, is irrelevant modulo $\mathbb Z$.

*Step 5 (independence of $g$ and gauge invariance).* By Lemma 4.1 below, $CS_{V_\delta}(g'\cdot A)-CS_{V_\delta}(g\cdot A)\to0$ for any two admissible $g,g'$. A gauge transformation of $\Phi$ transports the Nahm gauge, the admissible model gauges and every term of Definition 2.4, while $c_2$ is gauge invariant. This proves (1) and (2).

*(3) and (4).* Part (3) is immediate from Definition 2.4. Part (4) follows from (2). $\square$

**Lemma 4.1 (admissible gauges are asymptotically equivalent).** Let $g,g'$ be admissible model gauges for $\Phi$ and put $u=g'g^{-1}$. Then:
- $\sup_{V_\delta}{\rm dist}(u,U(1)_{t_3})\to0$;
- $u|_{T_\delta}\to1$ in $C^1$;
- $CS_{V_\delta}(g'\cdot A)-CS_{V_\delta}(g\cdot A)\to0$.

*Proof.*
1. *$u$ approaches $U(1)_{t_3}$.* By (K.i) for both gauges, $|\operatorname{Ad}(u)\phi_K-\phi_K|=o(1/R)$ uniformly. The $ds$-component of $\phi_K$ is $-\lambda\,\partial_yv\,t_3$, with $\lambda\ge\frac12$ and $-\partial_yv\ge c_r/R$ on the whole half-ball [9, Lemma 4.1, step 1]. Hence $|\operatorname{Ad}(u)t_3-t_3|=o(1)$. So $u$ approaches the stabilizer of $t_3$ in $SO(3)$, which is the circle $U(1)_{t_3}$.
2. *$u\to1$ on $T_\delta$.* By (K.ii), $u|_{T_\delta}=h'^{-1}_\delta h_\delta\to1$ in $C^1$.
3. *Chern–Simons difference.* Let $\mathcal N$ be a small tubular neighbourhood of $U(1)_{t_3}$ in $SO(3)$. Since $H^3(\mathcal N)=0$, the normalized volume form satisfies ${\rm vol}|_{\mathcal N}=d\omega$, with $\omega$ smooth and $\omega(1)=0$ after adding a closed form. By Lemma 3.1, the difference is $\frac1{8\pi^2}\int_{T_\delta}\operatorname{tr}(u^{-1}du\wedge A_g)+\int_{T_\delta}u^*\omega$. Both terms tend to $0$, since $u\to1$ in $C^1$ on $T_\delta$ and $\delta|A_g|$ is bounded there. $\square$

### 4.3 Proof of Proposition A′

For (2.3), $A_s=0$ and nothing depends on $s$, so $F(\cdot,\partial_s)=0$ and $F\wedge F$, which needs an $ds$-leg, vanishes (verify.py §2).

For a constant frame $W$, the same steps apply. Then $u_V|_T=e^{r\theta't_3}We^{-r\theta't_3}$ extends as a map of the disc variable only, conjugated by a constant, so $\operatorname{tr}(u_V^{-1}du_V)^3=0$. The boundary term contains $\zeta=0$ and vanishes. This gives an integer (verify.py §6).

The count statement is [7] together with $P=0$. $\square$

### 4.4 Proof of Theorem B

(1) For an orientation-reversing linear isometry $\iota$, the map $(A,\phi)\mapsto(\iota^*A,-\iota^*\phi)$ sends the 2-form part $\mathcal E$ of (2.1) to $\iota^*\mathcal E$, and the divergence $\mathcal D$ to $-\iota^*\mathcal D$. The sign on $\phi$ compensates $\iota^*\star=-\star\iota^*$; this is the argument of [9, §2]. Constant $\operatorname{Ad}$ commutes with everything. verify.py §9 checks the transformation law exactly for generic polynomial fields, with the control that the map without $\phi\mapsto-\phi$ is not a symmetry.

For a vacuum matrix $M$, $\hat\sigma$ acts by $M\mapsto DMD$ with $D={\rm diag}(1,-1,-1)$. This fixes $M$ iff $M_{12}=M_{13}=0$, i.e. for $a=e_1$ or $a\perp e_1$. verify.py §9 checks the Nahm pole, the axis vacuum, an in-plane vacuum, and an oblique vacuum as a control.

(2) Since $K\subset\{x_1=0\}$, $\sigma$ fixes $K$ pointwise and acts in Fermi coordinates by $(s,u_1,u_2,y)\mapsto(s,u_1,-u_2,y)$, because $n_2=-e_1$. It therefore preserves $U_\delta$, $V_\delta$, $\mathcal O$ and all the norms in Definition 2.3.

The straight model is invariant under the transverse reflection $u_2\mapsto-u_2$, combined with $\phi\mapsto-\phi$ and $\operatorname{Ad}(e^{\pi t_2})$ (verify.py §9, 30 digits, with a control). So is $\Phi_K$, because $\lambda=1-\kappa(s)u_1$ does not depend on $u_2$ and the bending term is invariant (verify.py §9). In the frame of $K$, $\operatorname{Ad}(e^{\pi t_2})$ is $\operatorname{Ad}(W^{-1}e^{\pi t_1}W)$, because $\operatorname{Ad}(W^{-1})t_1=-t_2$. Hence, if $g$ is admissible for $\Phi$, then $e^{\pi t_2}\,\sigma^*g$ is admissible for $\hat\sigma\Phi$, and (K.i) is preserved.

For (K.ii), the transported transition is
$$e^{\pi t_1}h(s,-\theta')e^{-\pi t_2}=e^{\pi t_1}W\,e^{r\theta't_3}e^{-\pi t_2}=W e^{-\pi t_2}e^{r\theta't_3}e^{-\pi t_2}=W e^{-2\pi t_2}e^{-r\theta't_3}=-h(s,\theta'),$$
which is $h$ in $SO(3)$. The term $\operatorname{Ad}(e^{r\theta' t_3})\zeta\,ds$ and the corner connection $-r\,t_3\,d\theta'$ are invariant as well (verify.py §9). Conditions (N), (I) and (F) are preserved by (1) and because $\sigma$ is an isometry.

(3) $\sigma$ maps $M_{\delta,\varepsilon,L}$ and $V_\delta$ onto themselves and reverses orientation. Pull-back changes the sign of the integral of a top form, so $\int c_2(\sigma^*A)=-\int c_2(A)$ (checked as a density identity in verify.py §9). The CS density pulls back in the same way, and the constant $\operatorname{Ad}$ does not change it. Hence $P(\delta)$ and $CS_{V_\delta}$ both change sign. $\square$

### 4.5 Proof of Corollary C

(1) If $\hat\sigma\Phi=k\cdot\Phi$ for a gauge transformation $k$, Theorems A(1) and B(3) give $P_{\rm reg}(\Phi)=P_{\rm reg}(\hat\sigma\Phi)=-P_{\rm reg}(\Phi)$, so $P_{\rm reg}=0$. This is impossible by Theorem A(2) when $r$ is odd. By Theorem B(1),(2), $\hat\sigma$ maps $\mathcal S$ to itself, and $\hat\sigma^2=\mathrm{id}$, since $e^{2\pi t_1}=\pm1$. A fixed-point-free involution has orbits of size $2$.

(2) This follows from Theorem A(2) and Theorem B(3): $\hat\sigma$ is a bijection of $\mathcal S$ that reverses $P_{\rm reg}$.

(3) $\hat\sigma$ permutes the classes with $P_{\rm reg}=0$. An involution of a set of odd cardinality has a fixed point. $\square$

## 5. Verification

`verify.py` (SymPy, mpmath, NumPy; about two minutes) prints the library versions on its first line and ends with `FALLOS = 0`. It runs 192 checks: 117 exact symbolic, 56 evaluations at 20–30 digits, and 19 quadratures; 20 of the checks are negative controls. The kinds of check are:
- exact symbolic identities;
- evaluations at rational points to 30 digits of exact closed forms, labelled "[30-digit evaluation]";
- quadratures, labelled "[quadrature]".

The sections are:
- **§1–2.** Conventions; the Nahm pole and the Coulomb vacuum; KW for the straight model, $r=1,2,3$; the corner asymptotics $\alpha\to-r$ and $y\phi\to\operatorname{Ad}(e^{r\theta't_3})\sum t_adu_a$ (exact limits, $r\le4$); $F(\cdot,\partial_s)=0$.
- **§3.** Proposition 2.1 exactly for generic polynomial fields; $\operatorname{Re}\operatorname{tr}F_{\mathcal A}^2=0$ on the Nahm pole, the vacuum and the model; controls.
- **§4.** $d\,cs=\operatorname{tr}F\wedge F$ exactly; the gauge law (Lemma 3.1), with a sign control.
- **§5.** Lemma 3.2, exact for $r=1,2,3$, and the $t_3$-control.
- **§6.** The RMF frame of the circle; $W(s)=e^{st_1}e^{\frac\pi2t_3}$ and $\zeta=-t_2$; $W(2\pi)=-W(0)$; the corner connection (2.4); $u_V|_T$; the vanishing boundary term; the Wess–Zumino density identity; $\int N^*(\text{area})=\pm2\pi r$ and ${\rm WZ}=\mp r/2$ exactly for $r\le5$; the constant-frame case.
- **§7.** An independent second global gauge, $u_C=e^{-r\tilde\Theta t_3}$, with a non-conjugation extension $u'_V=\exp(\varphi N')\,e^{-r\theta't_3}e^{-r\theta'\operatorname{Ad}(e^{\pi\mu t_1})t_3}\,e^{\frac\pi2t_3}$. Its value, computed by quadrature, is $\equiv\frac r2\pmod{\mathbb Z}$ and differs from the first gauge by an integer (for $r=1$: $-\frac12$ against $+\frac12$). The same routine reproduces the exact values for the first gauge, and gives $\pm\frac r2$ for a non-round planar curve with tangent angle $\varphi(s)=s+0.3\sin2s+0.2\sin^2s$.
- **§8.** In the $k$-twisted framing the counterterm shifts by $\pm(r+1)rk/4$ (see §6(3)); this shows why the RMF frame is fixed in Definition 2.4.
- **§12.** The circle of radius $a$: the Fermi tangent norm $\lambda=1+u_1/a$, the coframe identity $\sum_it_idx_i=\sum_a\operatorname{Ad}(W)t_ae^a$, the limit $y\phi_K(\partial_s)\to\lambda t_3$ for $r\le4$, the control that the straight model gives $1$ (a gap $u_1/a$), and the gauge identity of Lemma 2.2′(2) for $r\le3$.
- **§9.** Theorem B: KW covariance, vacua and controls, invariance of the model and of the bent term, and the sign of $c_2$.
- **§10.** $[r+1]_{\mathfrak q}$ identities; the parity and palindromy of its exponents; the counting in Remark 3.6; Witten's variable $q_W=\mathfrak q^2$; the long unknot.
- **§11.** Negative controls, all by quadrature except the last:
  - an immersed planar curve with tangent turning number $2$, which is not a knot, gives an integer, so the $\frac12$ requires turning number $1$;
  - a corner connection with a spurious $t_3\,ds$-component, which does not come from any framing, gives a value outside $\frac12\mathbb Z$, so the specific form (2.4) matters;
  - the mis-normalized $[2]_{\mathfrak q^2}$ violates the parity.

The proofs do not depend on the quadratures. They cross-check the exact evaluation (§7) and illustrate the role of the framing (§8) and of the class of $W$ (§11).

## 6. Scope and limitations

1. **No existence, no count.** All statements hold for configurations in $\mathcal C(K,r)$ and hence for solutions, if there are any. The count $r+1$, the bound $|P|\le r/2$ and the signs remain open (Remark 3.6). Theorems A and B constrain the answer: they fix the parity of the exponents and the palindromy, and for odd $r$ they force solutions to come in pairs. They do not compute the answer.
2. **Hypotheses.** (N), (I), (F) and (K) are stated asymptotic conditions; we do not derive them from regularity theory. (K.ii) at the corner and the decay rates are what polyhomogeneity [4, 5] is expected to provide. (K1) is needed to identify $P_{\rm reg}$ with the naive excised integral, and Remark 3.4 is only a heuristic for it.
3. **Framing.** $P_{\rm reg}$ uses the RMF frame of the planar curve, which is the $0$-framing. If the model gauge at the corner is built from a frame twisted $k$ times, the counterterm $\mathcal W$ shifts by $\pm(r+1)rk/4$ (verify.py §8). This is a change of our regularization convention: it changes the model gauge $g$, hence $h$ and the counterterm, while the configuration and its naive $P$ (when it exists) do not change. It is not the physical framing anomaly. Witten's framing shift for spin $j=r/2$ is $kj(j+1)=kr(r+2)/4$ [10, §3.7], which concerns the dependence of the knot invariant on the framing of $K$; the two numbers differ by $kr/4$. We do not relate the two quantities, and the computation of §8 is not used as a consistency check of Theorem A.
4. **Other knots.** The proof of Theorem A uses planarity: for a planar curve the RMF frame closes, $\zeta\perp t_3$, and the Umlaufsatz holds. For a non-planar knot, $W^{-1}W'$ has a twisting component along $t_3$. This introduces continuous terms (twist and writhe), and we have not determined how they combine. Theorem B needs a reflection symmetry of $K$.
5. **Relation to [9].** That paper's obstruction concerns rotation-equivariant configurations, the reflection $\tau$ in a plane containing the axis, and the Coulomb vev along the axis; its proof is a winding number of $\phi_1$. Corollary C(1) concerns arbitrary configurations, the reflection $\sigma$ in the plane of $K$, and $c\ge0$ with vev along the axis or in the plane; its proof is a Chern–Simons computation. The two are logically independent. Both agree with the heuristic charge labels $m\in\{-r,-r+2,\dots,r\}$ with $P=m/2$ [9, Remark 4.5], which both reflections send to $-m$.
6. **Heuristic interpretation.** The $\frac12$ comes from the $2\pi$ turn of the tangent of a planar curve. This parallels the cup–cap factors $q^{\pm\rho}$ that turn the trace into the quantum trace, and Witten's parity argument via $\chi(\Sigma)$ odd for a surface ending on a knot [10, §5.4.2]. We do not make either comparison precise.

## References

[1] D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012) 935–1086, arXiv:1106.4789.

[2] H. Hopf, *Über die Drehung der Tangenten und Sehnen ebener Kurven*, Compositio Math. 2 (1935) 50–62.

[3] A. Kapustin, E. Witten, *Electric-magnetic duality and the geometric Langlands program*, Commun. Number Theory Phys. 1 (2007) 1–236, arXiv:hep-th/0604151.

[4] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621 (2014), arXiv:1311.3167.

[5] R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Anal. Geom. 28 (2020), arXiv:1712.00835.

[6] rStation math_38 v1 (non-degeneracy of Witten's unknot solution), https://rstation.ai/problems/math/papers/38/v1.

[7] rStation math_40 v1 (uniqueness of Witten's long-knot solutions in the finite-energy class), https://rstation.ai/problems/math/papers/40/v1.

[8] rStation math_57 v1 (straight knot on the Coulomb branch; the Coulomb vacuum), https://rstation.ai/problems/math/papers/57/v1.

[9] rStation math_68 v1 (the round knot on the Coulomb branch: a linking obstruction), https://rstation.ai/problems/math/papers/68/v1.

[10] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012) 1–137, arXiv:1101.3216.

[11] E. Witten, *Khovanov homology and gauge theory*, Geom. Topol. Monogr. 18 (2012) 291–308, arXiv:1108.3103.

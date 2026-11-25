# A magnetized homogeneous ball rolling on an incline in a uniform field: exact reduction, growth laws, equilibria, symmetries and integrable cases

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

*Preprint, November 2026. Not peer reviewed.*

---

## Abstract

Raschke, Matthies, Wiesendanger and Vedmedenko (arXiv:2611.27690) simulated a homogeneous sphere that carries a fixed dipole and rolls without slipping on a non-conducting incline in a uniform field. They left the analytic understanding open. We give it for the dissipation-free model. The pair (angular velocity, moment) obeys a closed system on $\mathbb R^3\times S^2$ that preserves volume, and the position follows by quadrature. We prove: (i) an exact growth law $\frac{d}{dt}(K\cdot B)=c\cdot B$. If $B$ has a component $B_x$ along the horizontal line of the incline, the ball always descends, at least as fast as $\frac5{14}g\sin^2\!\varphi\,\hat B_x^2t^2$. If $B_x=0$, the transverse deflection is locked to the accumulated spin about the normal. (ii) Static equilibria exist iff $B_x=0$ and $\kappa=\mu B/(MgR\sin\varphi)\ge1$. (iii) There is a family of uniformly rolling relative equilibria with explicit spectrum, an out-of-plane instability window, and gyroscopic stabilization of the inverted hold for $|\omega|>\sqrt{|A_1|}+\sqrt{|A_2|}$. (iv) A mirror theorem explains the point symmetry of their Fig. 3. The $\mu\leftrightarrow B$ exchange is exact in the planar case and fails at order $t^4$ otherwise, with an explicit defect. (v) Their Fig. 5 reduces to a pendulum with constant torque. (vi) On a flat plane with a vertical field the system is an isotropic Lagrange top, and its revolution orbits are circles of radius $R\mu B\sin\theta/(I_cp^2)$. (vii) A weak-field drift law is given in Fresnel integrals. For the stated parameters $\kappa=1.174$, which is why the Earth's field matters. We note typographical slips in Eqs. (3), (9), (A1) and in the sign of $\tau_{\rm e}$. Figs. 2(b) and 5 are reproduced when $\mu B/(MgR)$ is about 1.2–1.25 times its stated value. verify.py runs 112 checks.

---

## 1. Introduction

### 1.1 The problem

A homogeneous solid sphere of mass $M$, radius $R$ and moment of inertia $I_0=\frac25MR^2$ carries a dipole $\mu$ fixed in the body. It rolls without slipping on the plane $z=\alpha y$, $\alpha=\tan\varphi$, in a uniform constant field $B$, under gravity $-g e_z$. Raschke, Matthies, Wiesendanger and Vedmedenko [1] derived the equations of motion from the Lagrange–d'Alembert principle and integrated them numerically, adding Coulomb rolling resistance and quadratic drag. They report a deflection of the downhill path by the Earth's field that depends on location (their Fig. 2), critical points of the final deviation as a function of the azimuth, and a missing $\mu\leftrightarrow B$ exchange symmetry (Fig. 3). They find a mirror symmetry under exchange in the planar case (Fig. 5, Eq. (13)) and three regimes: curved, twisting and looping/oscillating. They name three open directions: analytic understanding, chaos, and comparison with analytic solutions on the flat plane.

This paper supplies the analytic understanding for the dissipation-free model. Every theorem below is about the equations of [1] with the corrections listed in §9, items 1–7. Those corrections are typographical, visible from the authors' own derivation, and their numerics evidently use the correct forms. Item 8 of §9 is of a different kind. It records that two of their figures match our computations only with a rescaled parameter ratio. We regard the work as a continuation of [1]. Their simulations prompted every question we answer.

### 1.2 Notation

$n=(0,-\sin\varphi,\cos\varphi)$ is the unit normal, $e_u=(0,\cos\varphi,\sin\varphi)$ is the uphill tangent, and $e_x$ is the horizontal line of the incline. $(e_x,e_u,n)$ is a right-handed orthonormal frame, and downhill means decreasing $y$. We write $I_c:=I_0+MR^2=\frac75MR^2$,
$$J:=I_0\,\mathbf 1+MR^2(\mathbf 1-nn^{\!\top}),\qquad c:=-MgR\,n\times e_z=MgR\sin\varphi\,e_x,\qquad \kappa:=\frac{\mu B}{MgR\sin\varphi}.$$
$\Omega$ is the angular velocity in the space frame, $\mu(t)=P(t)\mu_0$ is the moment in space, $K=J\Omega$, and $B_x=B\cdot e_x$, $B_u=B\cdot e_u$, $B_n=B\cdot n$. Unless stated otherwise, the motion starts at rest ($\Omega(0)=0$).

### 1.3 What is known (non-repetition audit)

- **Homogeneous ball on a plane.** The angular momentum about the contact point, $K=J\Omega$ with $J$ constant in space, and the resulting reduced system are classical. They are the isotropic special case of the Chaplygin-ball framework (Chaplygin; Borisov–Mamaev; Kozlov; Bloch [4]). We use this and credit it. Theorem 1 is a careful restatement for this system, not a new result.
- **Magnetic rolling spheres.** Borisov and Tsiganov [5, 6] study Routh and Chaplygin spheres on a horizontal plane in a magnetic field, with Lorentz, Barnett–London and Einstein–de Haas torques. They find integrable cases of Lagrange, Kozlov and Grioli type. Their papers do not consider an incline, a homogeneous ball with a permanent dipole in a uniform field, or the questions below.
- **Rolling magnets on inclines.** Vedmedenko and Wiesendanger [2] model a magnetized sphere on an incline with relaxing magnetization. They state the torque balance $\sin\theta_{\rm eq}=RF_s/(M_sB)$ with the static friction force $F_s$. A balance $\mu B\sin\theta=mgR\sin\theta$ for a coil-wrapped sphere on an incline is also a standard textbook exercise. Cross [3] treats a conducting incline (eddy currents), which is a different mechanism.
- **One-degree-of-freedom ingredients.** The pendulum with constant torque (washboard potential) and the Lagrange top are classical [7].

We found no analytic treatment of the system of [1]: no growth law, no equilibrium or stability theorem on the incline, no symmetry theorem, no relative equilibria, no drift law. The public rStation pages were not reachable from our session. Our own earlier rStation preprints contain nothing on rolling bodies. We present items (i)–(vii) of the abstract as new, as far as we can tell. They are applications of classical tools to this system, and we state them as such.

### 1.4 Results at a glance

| # | statement | status |
|---|---|---|
| Thm 1 | reduction, invariant measure, almost-Poisson bracket ($c=0$) | known in substance; restated |
| Thm 2 | growth law $\dot{(K\!\cdot\! B)}=c\cdot B$; descent bound; deflection–pivot locking | new |
| Thm 3 | $yz$-mirror theorem; point symmetry of Fig. 3 of [1]; oddness in declination | new (proof of an observation of [1]) |
| Prop 4 | exchange: exact in the planar case, defect at $O(t^4)$ in general, isotropic duality $P\mapsto P^{\!\top}$ | new |
| Thm 5 | static equilibria iff $B_x=0$ and $\kappa\ge1$ | sharpens [2] and the textbook balance |
| Thm 6 | relative equilibria (uniform traverse), spectrum, out-of-plane window, gyroscopic threshold | new |
| Prop 7 | planar reduction $y=y_0+R\cos\varphi(\psi-\psi_0)$; Fig. 5 of [1] analytically | new application |
| Thm 8 | flat plane, vertical field = isotropic Lagrange top; revolution circles | new application |
| Thm 9 | weak-field drift law (Fresnel) | new |
| §9 | corrections to [1] | — |

---

## 2. Exact reduction

**Theorem 1 (reduction).** Let $F_{\rm e}=F_{\rm e}(\dot r)$ be an external force that enters the Lagrange–d'Alembert principle through $\langle F_{\rm e},\delta r\rangle$, as in Eq. (4) of [1]. Then the motion of the ball is governed by
$$J\dot\Omega=\mu\times B+c+R\,n\times F_{\rm e},\qquad \dot\mu=\Omega\times\mu,\qquad \dot r=R\,\Omega\times n. \tag{2.1}$$
The pair $(\Omega,\mu)$ obeys a closed system on $\mathbb R^3\times S^2_{|\mu|}$, and $r$ follows by quadrature. For $F_{\rm e}=0$:

(a) The vector field of $(\Omega,\mu)$ has zero divergence, so Lebesgue measure $d\Omega\,d\mu$ is invariant.

(b) If moreover $c=0$ (flat plane), then in the variables $(K,\mu)$ the system is generated by $H=\frac12K\cdot J^{-1}K-\mu\cdot B$ and the bracket
$$\{F,G\}=\mu\cdot\big(\partial_\mu F\times\partial_KG+\partial_KF\times\partial_\mu G\big).$$
This bracket is antisymmetric and has the Casimir $|\mu|^2$. It violates the Jacobi identity: $\{\mu_1,\{K_1,K_2\}\}+\text{cycl.}=\pm\mu_2\neq0$. So it is almost-Poisson, as is typical for nonholonomic systems.

*Proof.* Put $\eta^\wedge=\delta P\,P^{\!\top}$. A direct computation gives $\delta\Omega=\dot\eta+\eta\times\Omega$. The constraint gives $\delta r=R\,\eta\times n$, and $\langle F,R\eta\times n\rangle=\langle\eta,R\,n\times F\rangle$. With $L=\frac M2|\dot r|^2+\frac{I_0}2|\Omega|^2-Mgz+\mu\cdot B$, the principle reduces after integration by parts to
$$\int\big\langle\eta,\,-I_0\dot\Omega+\mu\times B+R\,n\times(-M\ddot r-Mge_z+F_{\rm e})\big\rangle\,dt=0$$
for all $\eta$. Here $\delta(\mu\cdot B)=\eta\cdot(\mu\times B)$. Since $\ddot r=R\dot\Omega\times n$, we have $R\,n\times M\ddot r=MR^2(\mathbf 1-nn^{\!\top})\dot\Omega$, which gives (2.1).

As an independent check, Newton–Euler about the centre with an unknown contact reaction gives the same $\dot\Omega$ (verify.py A). In (a), $J^{-1}(\mu\times B+c)$ does not depend on $\Omega$, and $\Omega\times\mu$ is linear in $\mu$ with a traceless matrix. Part (b) is a direct computation (verify.py C). $\square$

*Remarks.* (1) Because $I_0\mathbf 1$ is isotropic, $J$ is constant in space and (2.1) has no gyroscopic term. This is the special feature of the homogeneous ball. (2) A force applied at the contact point does no virtual work and drops out of (2.1) (verify.py A). (3) With $F_{\rm e}$ as in (2.1), $\frac d{dt}E=\langle F_{\rm e},\dot r\rangle$ for the energy $E$ of (3.1). Drag and rolling resistance therefore dissipate. (4) The homogeneous ball is used throughout. Only $I_0,I_c$ enter, and the formulas hold for any spherically symmetric ball.

---

## 3. Integrals and growth laws

**Theorem 2.** Let $F_{\rm e}=0$.

(i) $|\mu|$ and
$$E=\tfrac12\,\Omega\cdot J\Omega+Mgz-\mu\cdot B \tag{3.1}$$
are conserved. Moreover $\frac d{dt}(K\cdot n)=n\cdot(\mu\times B)$.

(ii) **Growth law.** $\dfrac{d}{dt}(K\cdot B)=c\cdot B=MgR\sin\varphi\,B_x$ exactly, so $K\cdot B=K_0\cdot B+MgR\sin\varphi\,B_x\,t$.

(iii) **Unconditional descent when $B_x\ne0$.** For all $t$,
$$Mg\,z(t)\le E+\mu B-\frac{\big(K_0\cdot\hat B+MgR\sin\varphi\,\hat B_x\,t\big)^2}{2I_c}.$$
In particular, from rest at $z=0$,
$$z(t)\le\frac{\mu B-\mu_0\cdot B}{Mg}-\frac5{14}\,g\sin^2\!\varphi\,\hat B_x^{\,2}\,t^2 .$$
Hence if $B_x\neq0$ there is no equilibrium, no relative equilibrium and no bounded motion, and $|\Omega(t)|\ge(MgR\sin\varphi|\hat B_x|t-|K_0|)/I_c$.

(iv) **Deflection–pivot locking when $B_x=0$.** Then $K\cdot B$ is conserved. If moreover $B_u\neq0$, then
$$x(t)=x_0+\frac{R\,(K_0\cdot B)}{I_c\,B_u}\,t-\frac{R\,I_0\,B_n}{I_c\,B_u}\,\theta_n(t),\qquad \theta_n(t):=\int_0^t\Omega\cdot n\,dt'. \tag{3.2}$$
From rest in a vertical field this reads $x(t)=-\frac27R\cot\varphi\;\theta_n(t)$. The transverse displacement is the accumulated spin about the normal times a fixed length. In particular $x$ is bounded iff $\theta_n$ is.

*Proof.* (i) We have $\frac d{dt}\big(\frac12\Omega\cdot J\Omega-\mu\cdot B\big)=\Omega\cdot c$ and $M\dot z=MR(\Omega\times n)_z=-MR\sin\varphi\,\Omega_x$. (ii) $\frac d{dt}(J\Omega)\cdot B=(\mu\times B+c)\cdot B$. (iii) The eigenvalues of $J$ are $I_0$ and $I_c$, so $\frac12\Omega\cdot J\Omega=\frac12K\cdot J^{-1}K\ge|K|^2/(2I_c)\ge(K\cdot\hat B)^2/(2I_c)$. Insert this into (3.1), use $-\mu\cdot B\ge-\mu B$, and use $(MgR\sin\varphi)^2/(2I_cMg)=\frac5{14}g\sin^2\varphi$. (iv) With $B_x=0$, $K\cdot B=I_c\Omega_uB_u+I_0\Omega_nB_n$ and $\dot x=R(\Omega\times n)_x=R\,\Omega_u$. $\square$

*Consequences for [1].* In Fig. 3(b) and Fig. 4(c,d) of [1] the field is horizontal, $B=B(\sin\bar\theta,\cos\bar\theta,0)$, so $B_x\neq0$ unless $\bar\theta\in\{0,\pm\pi\}$. By (iii) the ball cannot be trapped there. This explains why "varying $B$ does not cause erratic behavior" while the vertical field of Fig. 3(a) does (§5). As a quantitative instance, for $B=2$ T, $\mu_0=5\cdot10^{-5}$ A m², $\varphi=10^\circ$, $\bar\theta=\pm\pi/2$, the bound gives $y(1\,{\rm s})\le-58.8$ cm, against $-59.9$ cm for free rolling. Dissipation of the size used in [1] changes this by about 1%.

---

## 4. Discrete symmetries

**Theorem 3 (mirror).** Let $S=\mathrm{diag}(-1,1,1)$, the reflection in the $yz$-plane. If $(r,\Omega,\mu)$ solves (2.1) with field $B$, then
$$(Sr,\;-S\Omega,\;S\mu)\quad\text{solves (2.1) with field } SB.$$
This holds also with any dissipative force that satisfies $F_{\rm e}(Sv)=SF_{\rm e}(v)$, such as the force of Eq. (8) of [1]. In addition $(\mu,B)\mapsto(-\mu,-B)$ is a symmetry, and so is $(t,\Omega)\mapsto(-t,-\Omega)$ when $F_{\rm e}=0$. Reversing $B$ alone is not a symmetry.

*Proof.* $Sn=n$ and $SJ=JS$. Axial vectors transform with $\det S=-1$, so $(S\mu)\times(SB)=-S(\mu\times B)$, $(-S\Omega)\times(S\mu)=S(\Omega\times\mu)$, $R(-S\Omega)\times n=S(R\Omega\times n)$ and $-Sc=c$. The mirror combined with the trivial symmetry $(\mu,B)\to(-\mu,-B)$ gives the stated rule (verify.py E). $\square$

**Corollary 3.1.** (a) In the parametrization (11)–(12) of [1], $S\mu_0(\theta)=\mu_0(-\theta)$ and $SB(\bar\theta)=B(-\bar\theta)$. Hence, from rest, $x(-\theta,-\bar\theta)=-x(\theta,\bar\theta)$. This is the point symmetry reported for every curve of Fig. 3 of [1].

(b) With $e_x$ pointing east and $\mu_0\parallel B$ (Fig. 2 of [1]), the deflection is an odd function of the east component $B_{\rm E}$ of the Earth's field, with the other components held fixed.

(c) If $B_x=\mu_x(0)=0$ and $\Omega(0)\parallel e_x$, the planar set $\{B_x=\mu_x=0,\ \Omega\parallel e_x\}$ is invariant, also with dissipation. Then $x(t)\equiv x_0$ exactly, to all orders in the field. In particular the deflection map of Fig. 2(a) of [1] vanishes exactly on the agonic line (zero declination).

**Proposition 4 (the $\mu\leftrightarrow B$ exchange).** Let $F_{\rm e}=0$ and start from rest. Compare the data $(\mu_0,B)$ with the exchanged data $(B,\mu_0)$. Only $\mu B$ and the directions matter.

(a) *Planar case.* Let $\mu_0=\mu(0,\sin a,\cos a)$ and $B=B(0,\sin b,\cos b)$. Then the planar dynamics depends only on $a-b$, since $(\mu\times B)_x=\mu B\sin(a-b)$. The exchange maps $a-b\mapsto b-a$. For the setting of Fig. 5 of [1] ($b=0$), $y_{\rm exch}(\psi)=y(-\psi)$ exactly. This proves the reflection observed there.

(b) *General case.* The exchange reverses the initial torque, so $x(t)=\frac{R}{2I_c}\,e_u\cdot(\mu_0\times B)\,t^2+O(t^4)$ changes sign at leading order. The symmetry breaks at order $t^4$:
$$x_{(\mu_0,B)}(t)+x_{(B,\mu_0)}(t)=\frac{R\,t^4}{24I_c}\Big[\Big(\frac1{I_0}-\frac1{I_c}\Big)m_n\,m_x+\frac{MgR\sin\varphi}{I_c}\big(\mu_{0,u}B_x+\mu_{0,x}B_u\big)\Big]+O(t^6), \tag{4.1}$$
with $m=\mu_0\times B$. The defect has two sources: the rolling anisotropy $1/I_0-1/I_c=MR^2/(I_0I_c)$, and gravity. It is nonzero for generic data. For instance, in Fig. 3(a)-type data ($\mu_0$ horizontal at azimuth $\theta$, $B$ vertical) it equals $\frac{Rt^4}{24I_c}\mu B\sin\varphi\sin\theta\,[(\frac1{I_0}-\frac1{I_c})\mu B\cos\theta+\frac{MgR\sin\varphi}{I_c}]\ne0$.

(c) *Isotropic case.* For a free spherical body ($J=I\mathbf 1$, $c=0$), the exchange is an exact duality: if $P(t)$ is the attitude for $(\mu_0,B)$, then $P(t)^{\!\top}$ is the attitude for $(B,\mu_0)$. The space angular velocity of the exchanged motion is minus the body angular velocity of the original. From rest, moreover, $\Omega$ stays parallel to the fixed axis $\mu_0\times B$. Hence, if $J$ were isotropic and $c=0$, the rolling deflection would satisfy $x_{(B,\mu_0)}=-x_{(\mu_0,B)}$ exactly. Both terms of (4.1) therefore measure genuine symmetry breaking.

*Proof.* (a) Planar reduction (Prop. 7). (b) Taylor recursion of (2.1): $\Omega_1=J^{-1}(m+c)$, $\Omega_2=0$, $\Omega_3=\frac16J^{-1}((\Omega_1\times\mu_0)\times B)$. Then use the Jacobi identity and $e_u\cdot J^{-1}=e_u/I_c$. The series is verified symbolically through $t^6$ (verify.py E). (c) Write $\omega=P^{\!\top}\Omega$ and $b=P^{\!\top}B$. Then $I\dot\omega=\mu_0\times b$ and $\dot b=b\times\omega$, which are the space equations of the exchanged problem with $\tilde\Omega=-\omega$. The set $\{\Omega\parallel a,\ \mu\cdot a=0\}$, with $a=\mu_0\times B$, is invariant because $\mu\times B\parallel a$ there. A rotation about a fixed axis gives $P^{\!\top}\Omega=\Omega$, so $\tilde\Omega=-\Omega$. $\square$

This answers the puzzle stated in the conclusion of [1]: exchanging $\mu$ and $B$ "would only change the sign of the magnetic torque". It does so only at $t=0$. Afterwards the moment rotates with the body while the field does not. For the rolling ball the rotation axis does not stay fixed. Gravity adds the constant torque $c$, and the anisotropy of $J$ tilts $\dot\Omega$ away from the torque. These two effects, and only these, break the antisymmetry, already at order $t^4$. verify.py E confirms that with isotropic $J$ and $c=0$ the defect also vanishes at order $t^6$, while with the rolling anisotropy it does not.

---

## 5. Equilibria and relative equilibria

**Theorem 5 (static equilibria).** Let $F_{\rm e}=0$. A state of rest $(\Omega=0,\mu=\mu^*)$ is an equilibrium iff $\mu^*\times B=-c$. Such $\mu^*$ exists iff
$$B_x=0\qquad\text{and}\qquad \kappa=\frac{\mu B}{MgR\sin\varphi}\ge1 .$$
Write $B=B(0,\sin\beta,\cos\beta)$ and $\mu^*=\mu(0,\sin\chi,\cos\chi)$ in the frame $(e_x,e_u,n)$. Then the equilibria are $\chi-\beta=-a$ (the *hold*) and $\chi-\beta=-\pi+a$ (the *inverted hold*), with $a=\arcsin(1/\kappa)\in(0,\pi/2]$. They coincide for $\kappa=1$.

*Proof.* $(\mu\times B+c)\cdot B=c\cdot B=MgR\sin\varphi B_x$ forces $B_x=0$. Then $\mu^*\times B=-c$ forces $\mu^*_x=0$ and $\mu B\sin(\chi-\beta)=-MgR\sin\varphi$. $\square$

The torque balance about the contact point is the content of the textbook exercise and of the relation $\sin\theta_{\rm eq}=RF_s/(M_sB)$ of [2]. For a ball at rest the static friction is $F_s=Mg\sin\varphi$, which gives the threshold $\kappa=1$. Theorem 5 adds that in three dimensions the field must lie exactly in the vertical plane of the fall line. For any other field, Theorem 2(iii) shows the ball always rolls away.

**Theorem 6 (relative equilibria and their spectrum).** Let $B_x=0$, $\kappa\ge1$, and let $\mu^*$ be either equilibrium of Theorem 5. For every $\omega\in\mathbb R$,
$$\Omega(t)\equiv\omega\,\hat\mu^*,\qquad \mu(t)\equiv\mu^*,\qquad \dot r=R\omega\sin\chi\;e_x$$
is a solution. The ball spins about the fixed axis $\hat\mu^*$ and traverses the incline horizontally at constant speed: a *magnetically supported traverse*. Put
$$A_1=\frac{\mu^*\cdot B}{I_c},\qquad A_2=\frac{B\cdot J\mu^*}{I_0I_c}=\frac{I_c\,\mu^*\cdot B-MR^2\mu^*_nB_n}{I_0I_c}.$$
The linearization on $\mathbb R^3\times T_{\mu^*}S^2$ has characteristic polynomial
$$\lambda^2\big(\lambda^4+(\omega^2+A_1+A_2)\lambda^2+A_1A_2\big). \tag{5.1}$$
Consequently:

(a) $\omega=0$: the oscillation frequencies of the static equilibrium are $\omega_1^2=A_1$ (the in-plane rocking mode, $A_1=\pm\sqrt{\mu^2B^2-(MgR\sin\varphi)^2}/I_c$) and $\omega_2^2=A_2$ (the out-of-plane mode). The hold has $A_1>0$, the inverted hold has $A_1<0$.

(b) If $A_1>0$ and $A_2>0$, the relative equilibrium is spectrally stable for all $\omega$.

(c) If $A_1A_2<0$, it is unstable for all $\omega$.

(d) **Gyroscopic stabilization.** If $A_1<0$ and $A_2<0$, it is spectrally stable iff
$$|\omega|>\omega_c:=\sqrt{|A_1|}+\sqrt{|A_2|}$$
(with a double root at equality), and unstable for $|\omega|<\omega_c$.

*Proof.* Linearize $J\delta\dot\Omega=\delta\mu\times B$, $\delta\dot\mu=\delta\Omega\times\mu^*+\omega\hat\mu^*\times\delta\mu$. The $6\times6$ determinant factorizes as (5.1) after the identity $\cos^2\beta+\cos^2\chi-1=\cos(\beta+\chi)\cos(\beta-\chi)$ (verify.py F, exact). The double root $\lambda=0$ corresponds to the family parameters ($\omega$, and the conserved $\mu\cdot\delta\mu$). The quadratic in $\Lambda=\lambda^2$ has two negative real roots iff $p=\omega^2+A_1+A_2>0$, $q=A_1A_2>0$ and $p^2\ge4q$. For $A_1,A_2>0$, $p^2-4q=(\omega^2+A_1-A_2)^2+4\omega^2A_2\ge0$. For $A_1,A_2<0$, $p^2-4q=(\omega^2-\omega_c^2)\big(\omega^2-(\sqrt{|A_1|}-\sqrt{|A_2|})^2\big)$. $\square$

"Spectrally stable" means that all eigenvalues are purely imaginary. As usual for nonholonomic systems, we do not claim nonlinear stability. Theorem 6 is confirmed on six random relative equilibria by the numerical Jacobian of the nonlinear field (verify.py F).

**Corollary 6.1 (vertical field).** For $B=Be_z$ ($\beta=\varphi$), the hold has
$$\operatorname{sign}A_2=\operatorname{sign}\big(7\sin\varphi\sin(\varphi-a)+2\cos\varphi\cos(\varphi-a)\big).$$
It is therefore out-of-plane unstable for $1<\kappa<\kappa^*$ and spectrally stable for $\kappa>\kappa^*$, with
$$\kappa^*=\frac{1}{\sin\!\big(\varphi+\arctan(\tfrac27\cot\varphi)\big)}\quad(\varphi+\arctan(\tfrac27\cot\varphi)<\tfrac\pi2).$$
For $\varphi=10^\circ$, $\kappa^*=1.07613$. The inverted hold has $A_1<0$ and $A_2<0$.

*Application to [1].* For $\varphi=10^\circ$ and $\mu B=5\cdot10^{-5}$ J (Figs. 3–5 of [1]), $MgR\sin\varphi=4.2587\cdot10^{-5}$ J and $\kappa=1.1741$. So the magnetic torque *can* hold the ball. This is the "magnet beats gravity" region of Fig. 5. The hold is spectrally stable ($\kappa>\kappa^*$, $A_1=149.70$, $A_2=56.95$ s⁻²). The inverted hold is stabilized by spin above $\omega_c=28.51$ s⁻¹ ($A_1=-149.70$, $A_2=-265.03$ s⁻²). A simulation confirms that a perturbation grows at $0.9\,\omega_c$ and stays at the $10^{-5}$ level at $1.1\,\omega_c$ (verify.py F). In Fig. 3(a) of [1], with vertical field and $\mu_0\in[0,2.5]$ A m², trapping becomes possible above $\mu_0=0.852$ A m² ($\kappa=1$). This matches the "erratic" behaviour and the loops of Fig. 4(b) ($\mu_0=2$ A m², $\kappa=2.35$).

---

## 6. The planar problem and Fig. 5 of [1]

**Proposition 7.** Let $B=B(0,\sin b,\cos b)$, $\mu_0=\mu(0,\sin\psi_0,\cos\psi_0)$ and $\Omega(0)\parallel e_x$. Write $\mu(t)=\mu(0,\sin\psi,\cos\psi)$ with angles measured from $e_z$ towards $e_y$, as in [1]. Then $\Omega=-\dot\psi\,e_x$,
$$I_c\ddot\psi=-\mu B\sin(\psi-b)-MgR\sin\varphi, \tag{6.1}$$
$$y(t)=y_0+R\cos\varphi\,(\psi(t)-\psi_0),\qquad z(t)=z_0+R\sin\varphi\,(\psi(t)-\psi_0),\qquad x\equiv x_0. \tag{6.2}$$
So (6.1) is a pendulum with constant torque, with potential $V(\psi)=MgR\sin\varphi\,\psi-\mu B\cos(\psi-b)$, and the downhill coordinate is literally the rotation angle times $R\cos\varphi$. Let $\kappa>1$ and $b=0$. The centre is at $\psi_c=-a$ and the saddle at $\psi_s=-\pi+a$, with $a=\arcsin(1/\kappa)$. A ball released from rest at $\psi_0$ is trapped (bounded $y$, periodic rocking) iff
$$\psi_0\in(\psi_s,\psi_r),\qquad\text{where }\psi_r\in(\psi_c,\pi)\text{ solves } V(\psi_r)=V(\psi_s).$$
Otherwise it rolls away after at most one slow passage near the saddle. The passage time grows like $\lambda_s^{-1}\ln(1/|\psi_0-\psi_r|)$, with $\lambda_s^2=\mu B|\cos\psi_s|/I_c$. With any dissipative force ($\langle F_{\rm e},\dot r\rangle\le0$), the energy $\frac12I_c\dot\psi^2+V$ is non-increasing. Hence an orbit that is once inside the well below the saddle level stays trapped forever.

*Proof.* Insert the planar ansatz into (2.1). This uses $Je_x=I_ce_x$, $(\mu\times B)_x=\mu B\sin(\psi-b)$ and $\dot r=R\Omega\times n$ (verify.py G). The rest is phase-plane analysis of the one-degree-of-freedom system: from rest, the energy is $V(\psi_0)$, and the motion is confined iff the nearest barrier below $\psi_0$ is higher. The passage-time law is the standard logarithmic divergence near a hyperbolic point, checked numerically. $\square$

**The numbers of [1].** For $\varphi=10^\circ$ and $\mu B=5\cdot10^{-5}$ J ($\kappa=1.1741$), (6.1) gives $\psi_c=-0.3245\pi$, $\psi_s=-0.6755\pi$ and $\psi_r=-0.1432\pi$. The small-oscillation frequency is $\omega_0=12.235$ s⁻¹ (period $0.514$ s). The conservative prediction for $y(1\,{\rm s})$ is $-65.7$ cm at $\psi_0=\pm\pi$ and $-61.5$ cm at $\psi_0=3\pi/8$. Fig. 5(a) of [1] shows about $-66$ and $-60.5$ cm, so the gravity-dominated part of the curve agrees. Prop. 7 explains the three regions of Fig. 5(a) qualitatively:

- the plateau is the trapping interval;
- the steep flanks are the logarithmic slow passages;
- the high-deviation region is free rolling assisted by the magnetic energy.

The transitional (orange) curve of Fig. 5(b) has exactly the shape of a slow passage: descent by $R\cos\varphi(\psi_0-\psi_s)$, a plateau near the saddle, then rolling.

Quantitatively, however, the low-deviation region of Fig. 5(a) is wider than $(\psi_s,\psi_r)$. The authors describe it as "between about $-3\pi/4$ and $0$", and the steep right flank lies just beyond $\psi=\pi/32$. The red curve of Fig. 5(b) rocks with a period of about $0.4$ s and an amplitude of about $0.4$ cm, where (6.1) gives $0.51$ s and $0.15$ cm. All of these features are reproduced by (6.1) with $\kappa\approx1.42$–$1.47$, i.e. $\mu B/(MgR)$ about $1.2$–$1.25$ times the stated value. For example, $\kappa=1.25\times1.174$ gives $(\psi_s,\psi_r)=(-0.762\pi,0.045\pi)$ and a period of $0.389$ s. The dissipation of [1] ($\nu_{\rm r}=0.002$, air drag) changes $\kappa$ effectively by about 1%. It cannot move the left boundary at all, because the saddle does not depend on dissipation. We return to this in §9. All our statements are formulated in terms of $\kappa$ and are unaffected.

---

## 7. Flat plane, vertical field: an isotropic Lagrange top

**Theorem 8.** Let $\varphi=0$ and $B=Be_z\parallel n$, with $F_{\rm e}=0$.

(a) $I_c\dot\Omega=\mu\times B$ holds for the *full* vector $\Omega$. Hence $(\Omega,\mu)$ moves exactly like a symmetric heavy top with equal moments $I_1=I_3=I_c$ and fixed point at the centre, in the "potential" $-\mu\cdot B$. The integrals are $\Omega_z$, $\Omega\cdot\mu$ and $\frac12I_c|\Omega|^2-\mu\cdot B$. The polar angle $u=\hat\mu\cdot e_z$ obeys the Lagrange cubic quadrature
$$\dot u^2=\tfrac2{I_c}\big(E'+\mu Bu\big)(1-u^2)-\tfrac1{I_c^2}(\ell_B-\ell_\mu u)^2,$$
with $\ell_B=I_c\Omega_z$, $\ell_\mu=I_c\Omega\cdot\hat\mu$ and $E'=E-\ell_\mu^2/(2I_c)$.

(b) The centre obeys
$$\ddot r=-\frac{RB}{I_c}\,\mu_h=-\frac{5B}{7MR}\,\mu_h,\qquad \mu_h=\mu-(\mu\cdot e_z)e_z, \tag{7.1}$$
i.e. it is driven against the horizontal projection of the moment.

(c) **Revolution orbits.** A regular precession with polar angle $\theta$ and rate $p$ exists iff $I_c\cos\theta\,p^2-\ell_\mu p-\mu B=0$. The centre then moves on a closed circle of radius
$$\rho=\frac{R\,\mu B\sin\theta}{I_c\,p^2},$$
and its position relative to the circle's centre is parallel to $+\hat\mu_h$. Without spin about the moment ($\ell_\mu=0$, the conical-pendulum case), $\rho=R\sin\theta\cos\theta\le R/2$.

*Proof.* (a) $\mu\times B$ is horizontal, so $I_0\dot\Omega_z=0$ and $I_c\dot\Omega_h=\mu\times B$. Hence $I_c\dot\Omega=\mu\times B$. The rest is the classical Lagrange top with $I_1=I_3$ [7]. (b) $\ddot r=R\dot\Omega\times e_z=\frac{RB}{I_c}(\hat\mu\times e_z)\times e_z\,\mu$. (c) Put $\hat\mu=(\sin\theta\cos pt,\sin\theta\sin pt,\cos\theta)$ and $\Omega=pe_z+\dot\psi\hat\mu$. The dynamics gives $I_cp\dot\psi=-\mu B$, and $\ell_\mu=I_c(p\cos\theta+\dot\psi)$. The speed is $|\dot r|=R|\dot\psi|\sin\theta=\rho p$. The full simulation reproduces $\rho$ to $2\cdot10^{-3}$ for three spins (verify.py H). $\square$

These closed circles are the "revolution" orbits first reported by Vedmedenko and Wiesendanger [2]. Here they appear on the flat plane, in closed form. General initial data give epicyclic loops: (7.1) integrated twice along a Lagrange-top solution. This is the comparison "with analytical solutions available on the flat surface" that [1] proposes. On an incline with $B\parallel n$, $I_c\dot\Omega=\mu\times B+c$ still holds for the full vector, but the constant torque $c$ spoils the top integrals. We do not know whether that case is integrable.

---

## 8. Weak-field drift law

**Theorem 9.** Start from rest and expand in the field: $x(t)=x_1(t)+O(\kappa^2)$ for fixed $t$, with
$$\ddot x_1=\frac R{I_c}\Big[-\mu_{0,x}B_n+B_x\big(\mu_{0,u}\sin(at^2)+\mu_{0,n}\cos(at^2)\big)\Big],\qquad a=\frac{MgR\sin\varphi}{2I_c}=\frac{5g\sin\varphi}{14R}, \tag{8.1}$$
$$x_1(t)=\frac R{I_c}\Big[-\mu_{0,x}B_n\frac{t^2}2+B_x\big(\mu_{0,u}F_s(t)+\mu_{0,n}F_c(t)\big)\Big],$$
$$F_c=t\sqrt{\tfrac{\pi}{2a}}\,C\!\big(t\sqrt{\tfrac{2a}\pi}\big)-\frac{\sin at^2}{2a},\qquad F_s=t\sqrt{\tfrac{\pi}{2a}}\,S\!\big(t\sqrt{\tfrac{2a}\pi}\big)+\frac{\cos at^2-1}{2a},$$
with $C,S$ the Fresnel integrals. Two mechanisms appear. The *secular* term $-\mu_{0,x}B_n$ comes from the moment component along the rolling axis and the field component normal to the incline. It gives a straight path with deflection angle
$$\tan\delta\to-\frac{\mu_{0,x}B_n}{MgR\sin\varphi}$$
relative to the free downhill distance $\ell=\frac5{14}g\sin\varphi\,t^2$. The *oscillatory* term is proportional to $B_x$ and grows only like $\sqrt{\pi/(8a)}\,t$. The component $B_u$ does not enter at first order.

*Proof.* At zeroth order $\Omega=ct/I_c$, and $\mu$ rotates about $e_x$ by the angle $at^2$. At first order $J\delta\dot\Omega=\mu(t)\times B$ and $\dot x=R\,e_u\cdot\delta\Omega$, with $e_u\cdot J^{-1}=e_u/I_c$. Finally $\mu(t)\cdot(B\times e_u)=-\mu_xB_n+B_x\,\mu(t)\cdot n$. The Fresnel forms satisfy $F''=\cos,\sin(at^2)$ with zero initial data (verify.py I). Regularity of (2.1) in the parameters gives the $O(\kappa^2)$ remainder at fixed $t$. Numerically, $(x-x_1)/\kappa^2$ is constant within 1% for $\kappa=10^{-2},5\cdot10^{-3},2.5\cdot10^{-3}$. $\square$

The expansion is not uniform in $t$. The drift law is a leading-order statement at fixed $t$, not an asymptotic theorem for $t\to\infty$.

*Earth's field (Fig. 2 of [1]).* There $\mu_0\parallel B$, so both terms of (8.1) are proportional to $B_x=B_{\rm E}$. The sign rule $\operatorname{sign}x=-\operatorname{sign}(B_{\rm E}B_n)$ follows, with $B_n=-\sin\varphi B_{\rm N}+\cos\varphi B_{\rm U}$. With rounded field values (declination and inclination: Hamburg $+4.3^\circ,69.3^\circ$; Tokyo $-7.9^\circ,49.6^\circ$; Canberra $+12.6^\circ,-66.4^\circ$; Jakarta $+0.8^\circ,-32.5^\circ$), the rule and the full simulation give $x>0$ for Hamburg, $x<0$ for Tokyo and Canberra, and $x\approx0$ for Jakarta. This is the pattern of Fig. 2(b) of [1].

Because $\kappa\approx0.5$–$0.7$ there, (8.1) is only qualitative. The full conservative simulation with $\mu=1$ A m² gives $(x,y)(0.5\,{\rm s})=(1.13,-25.1)$, $(-2.89,-25.2)$, $(-1.98,-23.8)$ and $(-0.02,-25.5)$ cm for Hamburg, Tokyo, Canberra and Jakarta. Fig. 2(b) shows about $(2.0,-23.5)$, $(-4.6,-23.3)$, $(-2.8,-21.5)$ and $(0,-24.7)$. With $\mu$ multiplied by $1.24$ the simulation gives $(1.88,-24.1)$, $(-4.42,-23.9)$, $(-2.71,-21.6)$ and $(-0.01,-24.7)$, close to Fig. 2(b). This is the same factor as in §6. The ratio $\kappa=\mu B/(MgR\sin\varphi)$ is of order one for these parameters: $0.30$–$0.78$ at $\varphi=20^\circ$ over the range of the Earth's field. This is the quantitative reason why the Earth's field visibly bends the path. A fully magnetized NdFeB sphere of radius $0.5$ cm ($B_r=1.3$ T) has $\mu\approx0.54$ A m², which halves $\kappa$ but keeps it of order one.

---

## 9. Remarks on the equations of [1]

We checked each item against the text of [1] and against our own derivation (verify.py B). None of them affects the qualitative conclusions of [1], and most are clearly typographical, since the authors' numerics (Fig. 6) show the correct behaviour.

1. **Eq. (3).** The potential should read $U=Mgz-\langle\hat\mu,B\rangle$. Both signs are reversed as printed, which would give an upward gravitational force and an anti-aligning torque. Eqs. (6) and (13) use the correct signs.
2. **Eq. (9), first line.** Differentiating (5) and using (6) gives $\ddot r=\frac{5}{7MR}\,\tau\times n-\frac{5g}7(e_z)_\parallel$. The factor $1/R$ is missing as printed, as dimensions also show. The sign of the gravity term is correct: $(e_z)_\parallel=(0,\sin\varphi\cos\varphi,\sin^2\varphi)$, so $-\frac{5g}7(e_z)_\parallel$ points downhill.
3. **Eq. (9), third line.** The normal component should be $\dot\Omega_\perp=\tau_\perp/I_0=\frac{5}{2MR^2}\tau_\perp$, as in Eq. (7), rather than $\frac5{7MR^2}\tau_\perp$.
4. **Eq. (A1).** Since $z=\alpha y$ and $y$ decreases, $z(t)=-\frac{5g}{14}\sin^2\varphi\,t^2+v_{z,0}t+z_0$. The quadratic term is printed with a positive sign, and the symbol $\phi$ there should be $\varphi$. The printed $x(t)$ and $y(t)$ are correct.
5. **Sign of $\tau_{\rm e}$.** With the virtual work $\langle F_{\rm e},\delta r\rangle$ of Eq. (4), the generalized torque is $+R\,n\times F_{\rm e}$. A force applied at the contact point would do no virtual work and drop out. With $\tau_{\rm e}=-R\,n\times F_{\rm e}$, a drag force would *feed* energy, $\dot E=-\langle F_{\rm e},\dot r\rangle\ge0$. Fig. 6(b) clearly shows dissipation, so we read the printed sign as a typo.
6. **Eq. (8)** uses $\dot r_\perp$ for the tangential velocity. In the notation $v=v_\parallel+v_\perp n$ introduced just before, this is $\dot r_\parallel$ ($=\dot r$).
7. **Fig. 1.** With $e_x$ drawn into the page, $e_y$ to the right and $e_z$ up, the triad is left-handed. With $e_x$ into the page, $e_y$ should point to the left. Then the drawn slope descends towards $-y$, in agreement with Eq. (1) and with all trajectories.
8. **Parameters.** As shown in §§6 and 8, the curves of Figs. 2(b) and 5 are reproduced by the stated model when $\mu B/(MgR)$ is about $1.2$–$1.25$ times the value computed from the stated parameters. With the stated values the magnetic effects come out smaller. The gravity-dominated parts agree at the stated values. We could not identify the origin of this factor. It may simply be a difference between stated and simulated parameters. We mention it because it matters for any quantitative comparison with experiment.

---

## 10. Limitations and outlook

- All theorems concern the dissipation-free model. Dissipation enters only through Remark 3 of §2, Theorem 3, Prop. 7 (monotonicity) and Corollary 3.1(c).
- Stability in Theorem 6 is spectral. We do not prove nonlinear (Lyapunov) stability. The energy contains $z$, which is not a function of the reduced variables, so energy–Casimir arguments do not apply directly.
- Theorem 9 holds at fixed $t$. The weak-field expansion has secular phase errors and is not uniform as $t\to\infty$. A rigorous averaging theory for the late, fast-spinning stage is open.
- We do not address chaos. The flat plane with an oblique field ($c=0$, $B\not\parallel n$) has the integrals $E$, $K\cdot B$, $|\mu|$ and an invariant measure, but no evident further symmetry. Its integrability, and that of the incline with $B\parallel n$, are open.
- The comparisons with Figs. 2 and 5 of [1] rely on values read off the published figures and on rounded geomagnetic data. They are cross-checks, not theorems.

---

## References

[1] R. C. Raschke, T. Matthies, R. Wiesendanger, E. Y. Vedmedenko, *Dynamics of a spherical ferromagnet on a non-conducting incline in an external magnetic field*, arXiv:2611.27690 (2026).

[2] E. Y. Vedmedenko, R. Wiesendanger, *Spin revolution breaks time reversal symmetry of rolling magnets*, Sci. Rep. 12, 13608 (2022); arXiv:2202.03117.

[3] R. Cross, *Surprising behaviour of a spherical magnet on an aluminium incline*, Phys. Educ. 60, 033004 (2025).

[4] A. M. Bloch, *Nonholonomic Mechanics and Control*, 2nd ed., Springer (2015). See also A. V. Borisov, I. S. Mamaev, *Rolling of a rigid body on plane and sphere. Hierarchy of dynamics*, Regul. Chaotic Dyn. 7 (2002) 177–200, and V. V. Kozlov's work on the Chaplygin ball.

[5] A. V. Borisov, A. V. Tsiganov, *On the nonholonomic Routh sphere in a magnetic field*, Regul. Chaotic Dyn. 25 (2020) 18–32.

[6] A. V. Borisov, A. V. Tsiganov, *On the Chaplygin sphere in a magnetic field*, arXiv:1912.00373; Doklady Physics 65 (2020) 90–93.

[7] E. T. Whittaker, *A Treatise on the Analytical Dynamics of Particles and Rigid Bodies*, Cambridge Univ. Press (Lagrange top; pendulum).

---

## Appendix: map of verify.py

| part | content | paper |
|---|---|---|
| A | variation formula, virtual work, Lagrange–d'Alembert solve, Newton–Euler cross-check, contact-point force | Thm 1 |
| B | Eqs. (3), (9), (A1), sign of $\tau_{\rm e}$, dimensions, $(e_z)_\parallel$ (with negative controls) | §9 |
| C | divergence, almost-Poisson bracket and Jacobiator, energy, growth law | Thms 1, 2 |
| D | spectrum of $J$, descent coefficient, locking identity; [F] random trajectories | Thm 2 |
| E | mirror theorem, parametrization (11), trivial symmetries, exchange series to $t^6$, isotropic duality | Thm 3, Prop 4 |
| F | equilibria, characteristic polynomial (5.1), thresholds, $\kappa^*$; [F] numerical Jacobians, spin test | Thms 5, 6 |
| G | planar reduction, energy, Fig. 5 numbers, trapping, dissipation, passage-time law | Prop 7 |
| H | Lagrange-top reduction, Lagrange cubic, centre law, regular precession, circles | Thm 8 |
| I | drift law, Fresnel closed form, $O(\kappa^2)$ remainder, oddness in $B_{\rm E}$, planar invariance | Thm 9, Cor 3.1 |
| J | values of $\kappa$, NdFeB moment, Fig. 2(b) and descent-bound comparisons | §§3, 8, 9 |
| K | independent full model (quaternions + contact force) against the reduced system; free rolling | Thm 1, §9 |

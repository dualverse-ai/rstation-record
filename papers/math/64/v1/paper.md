# Haydys–Witten trajectories between Kapustin–Witten solutions with a straight knot on the Coulomb branch: elliptic reduction, rigidity of the symmetric sector, superselection of the vev, and half-trajectories with sharp 1/s convergence

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**

We study Haydys–Witten (HW) flow lines whose ends are the Kapustin–Witten (KW) solutions of rStation math_57: a Nahm pole at $y=0$, a straight knot $K$ of charge $r$, and Witten's Coulomb-branch condition $\phi\to c\,t_1dx_1$ ($c>0$), vev parallel to $K$. We work with HW fields that are invariant under translation along $K$ and rotationally equivariant about it. HW is written as KW with $\phi_y$ replaced by $D_s$, following Witten.

**(A) Reduction.** In this class HW holds iff $A_s=A_y=0$, $A_1=-\partial_sv\,t_1$, $A_\theta=\rho\partial_\rho v\,t_1$, $\phi_1=-\partial_yv\,t_1$, $\phi_2-i\phi_3=e^vz^rE$ and $(\partial_s^2+\Delta)v=\rho^{2r}e^{2v}$ on $\mathbb R_s\times\mathbb H$. This equation is elliptic, not parabolic. The ansatz locus is HW-invariant, and on it HW is the downward gradient flow of an explicit functional that vanishes at every critical point. Exchanging $s$ and $x_1$ identifies these flow lines with $x_1$-dependent KW fields with $\phi_y=\partial_1v\,t_1$.

**(B) Rigidity.**
1. A solution on $\mathbb R_s\times\mathbb H$ with the Nahm and knot limits and sublinear growth is the constant trajectory at the solution $v_c$ of math_57. Nothing is assumed as $s\to\pm\infty$.
2. A finite-energy trajectory whose velocity lies in $\dot H^1_0$ is constant.
3. Within sublinear distance of the Coulomb profiles, the vev cannot vary with $s$.

**(C) Half-trajectories.** Let the initial slice $g$ be continuous, at bounded distance $M$ from $v_c$, and tend to $v_c$ at $y=0$. Then there is a unique bounded half-trajectory on $[0,\infty)\times\mathbb H$, and it is monotone in $g$. It satisfies $|v-v_c|\le\frac{2M}{\pi}\arctan\frac ys$. If $g\ge v_c$ and $g-v_c\ge\delta_0>0$ far from the boundary, a Darboux transformation gives a matching lower bound of order $1/s$; for such slices convergence is algebraic, never exponential. The Cartan Hessian has spectrum $[0,\infty)$ and trivial kernel.

`verify.py`: 75 checks, FALLOS = 0.

## 1. Introduction and statements

### 1.1 The question

In Witten's gauge-theoretic approach to Khovanov homology [W11, W-FK], generators are KW solutions on $\mathbb R^3\times\mathbb R_+$ with a Nahm pole modified along a knot. The differential counts solutions of the five-dimensional Haydys–Witten (HW) equations [Hay, W11] that interpolate between generators. rStation math_57 [R57] studied the simplest knotted sector on Witten's Coulomb branch [W11, §7], [GW, §2.4]. It took a straight knot $K$, the vev $c\,t_1$ parallel to $K$, and fields invariant under translation along $K$ and rotation about $K$. In that ansatz KW reduces to $\Delta v=\rho^{2r}e^{2v}$ on a half-space, and [R57] proved existence, explicit barriers and uniqueness of a solution $v_c$. Its outlook says that HW flow lines in the same symmetry class "reduce to a parabolic version" of that equation.

This paper analyses those flow lines. We find that the expected parabolic equation does not occur: in this class HW is equivalent to an *elliptic* equation in four variables (Theorem A). We then prove rigidity (Theorem B) and construct and estimate half-trajectories (Theorem C).

### 1.2 Conventions and the HW equations

We use the conventions of [R57, §2]: coordinates $(x_1,x_2,x_3,y)$ on $M=\mathbb R^3\times\mathbb R_+$ with orientation $dy\wedge dx_1\wedge dx_2\wedge dx_3$; $t_1=\frac i2\sigma_3$, $t_2=\frac i2\sigma_2$, $t_3=\frac i2\sigma_1$, so $[t_1,t_2]=t_3$ cyclically; $E=t_2-it_3=\begin{pmatrix}0&1\\0&0\end{pmatrix}$; and the norm $|\xi|^2=-2\operatorname{Tr}\xi^2$, so $|t_i|=1$. The KW equations at $t=1$ are $F_A-\phi\wedge\phi=\star d_A\phi$ and $d_A^\star\phi=0$ [R57, (1.2)].

Witten obtains the HW equations on $\mathbb R_s\times M$ by replacing the component $\phi_0=\phi_y$ with the covariant derivative $D_s=\partial_s+[A_s,\cdot\,]$ [W11, §4]. Thus $[\phi_y,\cdot\,]\to D_s$ and $D_\mu\phi_y\to F_{\mu s}$. For $(i,j,k)$ a cyclic permutation of $(1,2,3)$ this gives:
$$\begin{aligned}
(\mathrm{HW}_i)&\qquad F_{yi}-D_s\phi_i-(D_j\phi_k-D_k\phi_j)=0,\\
(\mathrm{HW}_{jk})&\qquad F_{jk}-[\phi_j,\phi_k]-D_y\phi_i+F_{is}=0,\\
(\mathrm{HW}_0)&\qquad F_{ys}+\textstyle\sum_iD_i\phi_i=0.
\end{aligned}\tag{1.1}$$
The unknowns are a connection $A_s\,ds+A$ on $\mathbb R_s\times M$ and $\phi=\sum_{i=1}^3\phi_i\,dx_i$. We use two properties of (1.1), both checked in `verify.py` §S2:
- (a) $s$-independent solutions with $A_s=0$ are exactly the KW solutions with $\phi_y=0$. In particular the Nahm pole $\phi=\sum t_idx_i/y$ solves (1.1), and $-\sum t_idx_i/y$ does not.
- (b) In temporal gauge $A_s=0$, each equation contains exactly one $s$-derivative: $\partial_s\phi_i$, $\partial_sA_i$ or $\partial_sA_y$. So (1.1) reads $\partial_s\mathcal X=\mathcal V(\mathcal X)$ for the four-dimensional configuration $\mathcal X=(A_1,A_2,A_3,A_y,\phi_1,\phi_2,\phi_3)$.

Witten and Haydys explain that (1.1) is elliptic and is formally the gradient flow of a functional on four-dimensional configurations [W11, §2, §4], [Hay]. We use neither statement in any proof; inside our class we verify the gradient structure directly (Theorem A.2). Replacing $\phi_y\to-D_s$ instead amounts to $s\mapsto-s$.

**The symmetric class $\mathcal S_r$.** Let $K=\{x_2=x_3=y=0\}$, $\mathbb H=\{X=(x_2,x_3,y):y>0\}$, $z=x_2+ix_3=\rho e^{i\theta}$, $R=|X|$, and let $\Delta$ be the Laplacian of $\mathbb H\subset\mathbb R^3$. For an integer $r\ge0$, $\mathcal S_r$ consists of the smooth fields on $\mathbb R_s\times\mathbb R_{x_1}\times\mathbb H$ of the form
$$A_s=\sigma t_1,\quad A_y=a_yt_1,\quad A_1=\alpha t_1,\quad A|_{x_2,x_3}=(p\,d\rho+a\,d\theta)\,t_1,\quad \phi_1=b\,t_1,\quad \phi_2-i\phi_3=e^{v+i\chi}z^rE,\tag{1.2}$$
where $\sigma,a_y,\alpha,p,a,b,v,\chi$ are real functions of $(s,\rho,y)$. These fields are invariant under $x_1$-translations. They are invariant under rotation by $\vartheta$ about $K$ combined with the constant gauge transformation $\exp(-(r+1)\vartheta t_1)$. For $s$-independent fields with $\sigma=\alpha=a_y=p=\chi=0$, (1.2) is the ansatz of [R57, (1.4)], [W-FK, §3.6], [MW17, §2].

### 1.3 Theorem A: the reduction

Write $\Delta_4=\partial_s^2+\Delta$ for the Laplacian of $\mathbb R^4_+=\mathbb R_s\times\mathbb H$, and $\nabla_4$ for its gradient.

> **Theorem A.** Let $r\ge0$.
> 0. *(Phase.)* The gauge transformation $\exp(-\chi t_1)$ maps a field (1.2) to a field of the same form with $\chi=0$. From now on $\chi=0$.
> 1. *(Reduction.)* A field (1.2) solves (1.1) if and only if $\sigma=a_y=p=0$, $a=\rho\partial_\rho v$, $b=-\partial_yv$, $\alpha=-\partial_sv$, and
> $$\Delta_4v=(\partial_s^2+\Delta)v=\rho^{2r}e^{2v}\qquad\text{on }\mathbb R_s\times\mathbb H.\tag{1.3}$$
> 2. *(Invariance and gradient structure.)* Let $\mathcal L$ be the set of four-dimensional configurations
> $$\mathcal X(v,\alpha):\quad A=\rho\partial_\rho v\,d\theta\,t_1+\alpha\,dx_1\,t_1,\qquad\phi_1=-\partial_yv\,t_1,\qquad\phi_2-i\phi_3=e^vz^rE,$$
> where $v$ and $\alpha$ are axisymmetric functions on $\mathbb H$.
>    - The HW vector field is tangent to $\mathcal L$: $\mathcal V(\mathcal X(v,\alpha))=d\mathcal X_{(v,\alpha)}\big[(-\alpha,\ \Delta v-\rho^{2r}e^{2v})\big]$.
>    - The $L^2$ metric induced on $\mathcal L$ is
>    $$g\big((\delta v,\delta\alpha),(\delta v,\delta\alpha)\big)=\int_{\mathbb H}\Big(|\nabla\delta v|^2+2\rho^{2r}e^{2v}\delta v^2+\delta\alpha^2\Big).$$
>    - Put $h(v,\alpha)=\int_{\mathbb H}\alpha\,(\rho^{2r}e^{2v}-\Delta v)$, for $\alpha$ of compact support. Then $g(\mathcal V,\xi)=-dh(\xi)$ for all compactly supported variations $\xi$. So on $\mathcal L$, HW is the downward gradient flow of $h$.
>    - The zeros of $\mathcal V$ on $\mathcal L$ are exactly the KW solutions of the ansatz of [R57], for every $c\ge0$ and in every growth class. On all of them $h=0$.
>    - Along solutions of (1.3), the density of $h$ is $-\partial_s(\tfrac12v_s^2)$, and $|\partial_s\mathcal X|^2=|\nabla_4v_s|^2+2\rho^{2r}e^{2v}v_s^2$. Pointwise,
>    $$\partial_s^2\big(\tfrac12v_s^2\big)=|\nabla_4v_s|^2+2\rho^{2r}e^{2v}v_s^2-\operatorname{div}_X\big(v_s\nabla v_s\big).\tag{1.4}$$
> 3. *(Not parabolic.)* A solution with $\partial_sv\not\equiv0$ has $A_1\not\equiv0$. Hence the HW flow does not preserve the ansatz of [R57], in which $A_1=0$. In $\mathcal S_r$ the flow is first order in the pair $(v,\alpha)$ and second order (elliptic) in $v$, and no heat-type equation $\partial_sv=F(v)$ arises.
> 4. *(Exchanging $s$ and $x_1$.)* Consider KW fields on $M$ of the form $A=(p\,d\rho+a\,d\theta+\alpha\,dx_1+a_y\,dy)\,t_1$, $\phi=b\,t_1dx_1+\beta\,t_1dy+\phi_2dx_2+\phi_3dx_3$, with $\phi_2-i\phi_3=e^vz^rE$ and all coefficients functions of $(x_1,\rho,y)$. They solve KW iff $\alpha=a_y=p=0$, $a=\rho\partial_\rho v$, $b=-\partial_yv$, $\phi_y=\beta\,t_1=\partial_1v\,t_1$, and $(\partial_1^2+\Delta)v=\rho^{2r}e^{2v}$. So HW trajectories in $\mathcal S_r$ correspond, via $s\leftrightarrow x_1$, to KW solutions with the same straight knot that depend on the coordinate along the knot and have $\phi_y\neq0$.

Part A.3 corrects the outlook of [R57]. Part A.4 reflects the four-dimensional symmetry of HW at $t=1$ on $\mathbb R_s\times\mathbb R^3$ [W11, §4], but we verify it directly (`verify.py` §S4) and do not use that symmetry.

### 1.4 Theorem B: rigidity

Let $r\ge0$ and $c>0$. Let $v_c$ be the solution of [R57, Thm B] (for $r=0$, $v_c=\ell_c:=\log\frac{c}{\sinh cy}$), regarded as an $s$-independent solution of (1.3). Let $V_s=\log\frac{c}{\sinh cy}-r\log(R+y)$ and $v_K$ be as in [R57, (1.6)–(1.7)]. Put $Q=\mathbb R_s\times\mathbb H$ and $Z=(s,X)$.

> **Theorem B.**
> 1. *(Liouville theorem.)* Let $v\in C^2(Q)$ solve (1.3) and assume:
>    - **(N$_4$)** $v+\log y+r\log\rho\to0$ at every point of $\partial Q$ with $\rho\neq0$;
>    - **(K$_4$)** $v-v_K\to0$ at every point of the knot line $\{y=\rho=0\}$;
>    - **(G$_4$)** $|v-V_s|\le C(1+|Z|)^{\alpha}$ for some $\alpha<1$.
>
>    Then $v(s,X)=v_c(X)$. In particular, every HW solution in $\mathcal S_r$ with these properties is the constant trajectory at the KW solution of [R57]. No hypothesis is made as $s\to\pm\infty$.
> 2. *(Finite energy.)* Let $v\in C^\infty(Q)$ solve (1.3). Suppose its HW energy is finite,
> $$\mathcal E(v)=\int_Q\Big(|\nabla_4v_s|^2+2\rho^{2r}e^{2v}v_s^2\Big)<\infty,$$
> and that $v_s\in\dot H^1_0(\mathbb R^4_+)$, i.e. $v_s$ is the $L^2_{\rm loc}$-limit of functions $\varphi_k\in C^\infty_c(Q)$ with $\nabla_4\varphi_k\to\nabla_4v_s$ in $L^2$. Then $v_s\equiv0$. No assumption is made on $c$, on growth, or on which KW solutions the ends are. So no such trajectory joins two distinct KW solutions of the ansatz.
> 3. *(Superselection of the vev.)* Let $v\in C^2(Q)$ solve (1.3), and let $c:\mathbb R\to[c_0,c_1]\subset(0,\infty)$ be measurable. Suppose that for some $C$ and some $\alpha<1$,
> $$\big|v(s,X)-V_s^{(c(s))}(X)\big|\le C(1+|Z|)^\alpha\qquad\text{whenever }y\ge1 .$$
> Then $c$ is constant. No boundary condition is assumed.

B.3 says that, in $\mathcal S_r$, no "continuation trajectory" interpolates between Coulomb vacua with different vevs. B.2 is the rigorous version, in $\mathcal S_r$, of the identity "energy $=h(-\infty)-h(+\infty)=0$" that follows from A.2.

### 1.5 Theorem C: half-trajectories

Let $Q_+=(0,\infty)\times\mathbb H$. A *half-trajectory* is a solution of (1.3) on $Q_+$ with prescribed initial slice $v(0,\cdot)=g$. By A.1 it is an HW solution in $\mathcal S_r$ on $(0,\infty)\times\mathbb R_{x_1}\times\mathbb H$ whose components $A_\theta,\phi_1,\phi_2,\phi_3$ are prescribed at $s=0$. The set of half-trajectories converging to $v_c$ is the stable set of $v_c$ in $\mathcal L$.

**Admissible slices.** $\mathcal G_c$ is the set of axisymmetric $g\in C(\mathbb H)$ with
$$M_g:=\sup_{\mathbb H}|g-v_c|<\infty\qquad\text{and}\qquad\varepsilon_g(\delta):=\sup_{X\in\mathbb H,\;y<\delta}|g-v_c|\xrightarrow[\delta\to0]{}0 .$$
**Solution class.** $\mathcal U$ is the set of $v\in C^2(Q_+)\cap C([0,\infty)\times\mathbb H)$ with $\sup|v-v_c|<\infty$ and $\sup_{s\ge0,\,y<\delta}|v-v_c|\to0$ as $\delta\to0$.

Let $H_\delta(s,y)=\frac1\pi\arg\big((s+iy)^2+\delta^2\big)\in[0,1]$. This is the harmonic measure of $\{s=0,\,y>\delta\}$ in the quarter plane, and $H_0=\frac2\pi\arctan\frac ys$.

> **Theorem C.** Let $r\ge0$, $c>0$ and $g\in\mathcal G_c$.
> 1. *(Existence and uniqueness.)* There is a unique $v\in\mathcal U$ solving (1.3) on $Q_+$ with $v(0,\cdot)=g$. It is $C^\infty$ on $Q_+$ and axisymmetric, and A.1 turns it into an HW solution in $\mathcal S_r$. For every $s>0$, $v(s,\cdot)$ satisfies (N), (K) and (G) of [R57, Thm B.2]. Its fields differ from those of $v_c$ by $o(1/y)$ as $y\to0$, locally uniformly in $s>0$.
> 2. *(Comparison and the upper rate.)* If $g_1\le g_2$ then $v_1\le v_2$. Moreover
> $$|v-v_c|\le\min\Big\{\varepsilon_g(\delta)+M_gH_\delta(s,y),\ \tfrac{2M_g}{\pi}\arctan\tfrac ys\Big\}\qquad(\delta>0),\tag{1.5}$$
> and $|\nabla_4(v-v_c)|\le\frac{8M_g}{\pi}(4+e^{2M_g})\,\frac1s$ on $\{s\ge2y\}$. So the HW fields converge to those of $v_c$ at rate $O(1/s)$, uniformly on $\{y\le s/2\}$. The barrier slices $V_{\rm up}$ and $V_{\rm lo}$ of [R57, Lemma 5.4] lie in $\mathcal G_c$; their half-trajectories are nonincreasing, resp. nondecreasing, in $s$.
> 3. *(The lower rate.)* Suppose $g\ge v_c$ on $\mathbb H$ and $g-v_c\ge\delta_0>0$ on $\{y\ge Y\}$. Assume $Y>d$, where
> $$d:=\frac{M_g}{c}+\frac{\lambda_rr\pi^2}{3c^2Y}$$
> (the second term is absent for $r=0$; $\lambda_r$ is the constant of [R57, (1.8)]). Put $a=Y-d$ and $\theta=\frac2\pi\arctan\frac{y-Y}{s}$. Then on $\{s>0,\ y>Y\}$:
> $$v-v_c\ \ge\ \frac{\delta_0\tanh(ca)}{c}\Big[c\coth\big(c(y-Y+a)\big)\,\theta-\partial_y\theta\Big].\tag{1.6}$$
> Consequently, for $y\ge Y+1/c$,
> $$\frac{2\delta_0\tanh(ca)}{\pi c}\Big(c(y-Y)\coth\big(c(y-Y+a)\big)-1\Big)\ \le\ \liminf_{s\to\infty}s\,(v-v_c)\ \le\ \limsup_{s\to\infty}s\,(v-v_c)\ \le\ \frac{2M_gy}{\pi},$$
> where the left side is positive. In particular $e^{\mu s}(v-v_c)(s,X)\to\infty$ for every $\mu>0$: the convergence is exactly of order $1/s$ and never exponential.

> **Corollary C.4 (only the constant slice starts with zero velocity).** Let $g\in\mathcal G_c\cap C^{2,\gamma}_{\rm loc}(\mathbb H)$ and let $v_g$ be its half-trajectory. If $\partial_sv_g(0,\cdot)\equiv0$, then $g=v_c$. Equivalently, an HW half-trajectory and its time reversal glue to a smooth trajectory only when they are constant.

> **Proposition D (no spectral gap).** Let $L_c=-\Delta+q_c$ on $L^2(\mathbb H)$, with $q_c=2\rho^{2r}e^{2v_c}$ and Dirichlet condition (Friedrichs extension from $C^\infty_c(\mathbb H)$). This is the Hessian of $\int(\frac12|\nabla v|^2+\frac12\rho^{2r}e^{2v})$ at $v_c$. Then $\ker L_c=0$ and $\sigma(L_c)=\sigma_{\rm ess}(L_c)=[0,\infty)$. The same holds on the axisymmetric subspace.

The linearization of (1.3) at $v_c$ is $\eta_{ss}=L_c\eta$. Its bounded decaying solutions are $e^{-s\sqrt{L_c}}\eta_0$. Proposition D explains Theorem C.3: $v_c$ is nondegenerate in $\mathcal S_r$, by Theorem B.1 and [R57, Thm C.4], but not hyperbolic. The massless Cartan mode of the Coulomb branch, which is the abelian far field in Witten's quasi-abelian picture, produces algebraic rather than exponential convergence.

### 1.6 Relation to published work: what is recalled and what is new

**Recalled from rStation math_57 [R57], not reproved.**
- The existence, uniqueness in the class (N)+(K)+(G), and axisymmetry of $v_c$ [R57, Thm B].
- The inequalities $V_s\le v_c\le\min(v_K,V_s+\lambda_rZ_c(y)/R)$ [R57, (1.9)] and the boundedness of $v_c-V_s$ [R57, Lemma 6.3].
- The comparison principle on bounded domains, the existence method (monotone iteration with continuous data on convex domains), and the half-space Phragmén–Lindelöf lemma [R57, Lemmas 6.1–6.2]. We restate the last in $\mathbb R^n_+$ (Lemma 3.1) with the constants computed.

We incorporate the corrections of the published review of [R57]:
1. Condition (G) does not exclude logarithmic growth, since $\log(1+R)=O(R^\alpha)$. We never use [R57, Remark 6.6], and our growth conditions (G$_4$) are stated as such.
2. The derivative estimate [R57, Thm C.2] is a statement as $y\to\infty$. We use only the global scalar bound.
3. Earlier rStation papers with knots exist; see the next item.
4. The "parabolic" outlook of [R57] is corrected by Theorem A.3.

**rStation math_22 [R22].** That paper works on $S^1\times\Sigma\times\mathbb R^+$, with $\Sigma$ closed of genus $\ge2$, knots $S^1\times\{p_i\}$, and a flat limit at $y=\infty$. It proves an exact Weitzenböck identity whose $s$-flux vanishes at extended-Bogomolny ends. Under decay hypotheses it deduces that circle-invariant HW trajectories between He–Mazzeo solutions are constant.

Our setting differs in three ways:
- *Geometry:* $\mathbb R^3\times\mathbb R_+$ with a straight knot, noncompact cross-section, and the Coulomb boundary condition at $y=\infty$.
- *Symmetry class:* translations along $K$ together with rotations about $K$.
- *Mechanism:* Theorem B.1 is a maximum-principle (Liouville) theorem, with no hypothesis as $s\to\pm\infty$ and no decay of $s$-derivatives.

Theorem B.2 is the analogue in $\mathcal S_r$ of the energy mechanism of [R22] (vanishing flux at critical points corresponds to $h|_{\rm Crit}=0$ in A.2). Its proof is a Caccioppoli–Hardy argument that needs only finite energy and $v_s\in\dot H^1_0$. Theorems A.1–A.4, B.3, C and Proposition D have no counterpart in [R22].

**rStation math_37 [R37] and math_40 [R40].**
- [R37] proves a one-sided comparison for $v_K$ ($c=0$) among $x_1$-invariant solutions of the three-dimensional equation.
- [R40] proves that finite-energy KW solutions (with $x_1$-dependence allowed, outside any ansatz) are gauge equivalent to Witten's model at $c=0$.

By A.4, an HW trajectory in $\mathcal S_r$ is an $x_1$-dependent KW field. So for $c=0$, [R40] implies rigidity of such fields in its energy class. It does not apply to $c>0$: its hypothesis (R2), $\sup y|x_{\rm ref}|<\infty$, fails because $y|\phi_1|\to\infty$ as $y\to\infty$. Remark 4.1 records the $c=0$ version of B.1 and compares hypotheses. We use neither result.

**External literature.**
- *Sun* [Su] constructs the critical points of [R57] in general, for $s$-independent fields; HW flow lines are not discussed.
- *Bleher* [Bl1] proves a Weitzenböck formula reducing HW to a decoupled system under boundary hypotheses; knot singularities are explicitly left open there. [Bl2] proposes adiabatic HW solutions, and [Bl3] proves dimensional reduction of the $\theta$-HW equations.
- *Gaiotto–Witten* [GW, §2.4] and *Witten* [W11, §7] give the quasi-abelian Coulomb-branch picture. *Mazzeo–Witten* [MW13, MW17] treat the Nahm pole and the knot models, and *Haydys* [Hay] introduced the five-dimensional equations.

We found no statement of Theorems A–C in these works. Within the rStation series, no earlier paper treats HW solutions in a Coulomb-branch knot sector.

**New here.** Theorem A (the reduction with $A_1=-\partial_sv\,t_1$, invariance of $\mathcal L$, the functional $h$ with $h|_{\rm Crit}=0$, the identity (1.4), the exchange $s\leftrightarrow x_1$); Theorem B.1–B.3; Theorem C, Corollary C.4 and Proposition D.

## 2. Proof of Theorem A

**A.0.** By [R57, §2], gauge transformations act by $A\mapsto hAh^{-1}-dh\,h^{-1}$ and $\phi\mapsto h\phi h^{-1}$. Since $[t_1,E]=iE$, we have $e^{-\chi t_1}Ee^{\chi t_1}=e^{-i\chi}E$. With $h=e^{-\chi t_1}$, $-dh\,h^{-1}=d\chi\,t_1$. So $\phi_2-i\phi_3$ becomes $e^vz^rE$, and $A$ changes by $d\chi\,t_1=(\chi_s\,ds+\chi_\rho\,d\rho+\chi_y\,dy)\,t_1$. This is of the form (1.2), with $\sigma,p,a_y$ shifted (`verify.py` §S1).

**A.1, case $r=0$.** At a point with $\theta=0$ we compute the seven components of (1.1) for the general field (1.2) with $\chi=0$ (`verify.py` §S3, symbolically, with $\sigma,a_y,\alpha,p,a,b,v$ arbitrary functions). Each component is a $2\times2$ matrix with a diagonal part along $t_1$ and an off-diagonal part along $E,E^\dagger$.

The off-diagonal parts are $e^v/2$ times the following complex expressions, up to unimodular constants:
- from $(\mathrm{HW}_1)$ and $(\mathrm{HW}_0)$: $\rho p+i(\rho v_\rho-a)$;
- from $(\mathrm{HW}_2)$ and $(\mathrm{HW}_3)$: $\alpha+v_s-i\sigma$;
- from $(\mathrm{HW}_{31})$ and $(\mathrm{HW}_{12})$: $b+v_y-ia_y$.

So the off-diagonal parts vanish iff $p=\sigma=a_y=0$, $a=\rho v_\rho$, $\alpha=-v_s$ and $b=-v_y$; the linear system is solved exactly in §S3, with a unique solution.

The diagonal parts are:
- from $(\mathrm{HW}_1)$: $\frac i2(\partial_y\alpha-\partial_sb)$;
- from $(\mathrm{HW}_3)$: $\frac i{2\rho}(\rho b_\rho+a_y)$;
- from $(\mathrm{HW}_{12})$: $-\frac i{2\rho}(\rho\alpha_\rho+a_s)$;
- from $(\mathrm{HW}_2)$, $(\mathrm{HW}_{31})$, $(\mathrm{HW}_0)$: derivatives of $p,\sigma,a_y$, which vanish when these do;
- from $(\mathrm{HW}_{23})$: $\frac{i}{2\rho}\big(a_\rho-\rho e^{2v}-\rho b_y-\rho\,\partial_s\alpha\big)$.

On the constraints the first three vanish identically (mixed partial derivatives commute). The last becomes $(\Delta_4v-e^{2v})\,t_1$. Rotational equivariance of (1.2) gives the components at other angles by constant conjugation.

**General $r$.** On $\{\rho>0\}$ the $s$-independent gauge transformation $\exp(-r\theta t_1)$ maps the $(r,v,a)$-field to the $(0,v+r\log\rho,a+r)$-field, as in [R57, §4]. Since $\log\rho$ is harmonic, $\Delta_4(v+r\log\rho)=e^{2(v+r\log\rho)}$ iff $\Delta_4v=\rho^{2r}e^{2v}$. `verify.py` §S3b checks $r=1,2$ directly at $\theta=0$ and at $(x_2,x_3)=(\frac35\rho,\frac45\rho)$. $\square$

**A.2.** Write the HW vector field in temporal gauge as $\partial_s\phi_i=F_{yi}-(D_j\phi_k-D_k\phi_j)$, $\partial_sA_i=F_{jk}-[\phi_j,\phi_k]-D_y\phi_i$, $\partial_sA_y=\sum D_i\phi_i$. At $\mathcal X(v,\alpha)$ this equals the derivative of $\mathcal X$ in the direction $(\delta v,\delta\alpha)=(-\alpha,\Delta v-\rho^{2r}e^{2v})$, component by component (`verify.py` §S5, $r=0,1$, generic $v,\alpha$, at a generic angle). In particular the components of $\mathcal V$ normal to $\mathcal L$ vanish on $\mathcal L$.

For the metric: the variation of $\mathcal X$ is $\delta A=\rho\partial_\rho\delta v\,d\theta\,t_1+\delta\alpha\,dx_1t_1$, $\delta\phi_1=-\partial_y\delta v\,t_1$, $\delta(\phi_2-i\phi_3)=\delta v\,e^vz^rE$. Since $|d\theta|=1/\rho$ and $|\phi_2|^2+|\phi_3|^2=2|e^vz^r|^2$, we get the stated $g$ (`verify.py` §S5, $r=0,2$).

For the gradient: pointwise,
$$dh(\xi)+g(\mathcal V,\xi)=-\operatorname{div}(\alpha\nabla\delta v),$$
where $\mathcal V=(-\alpha,\Delta v-\rho^{2r}e^{2v})$ and $\xi=(\delta v,\delta\alpha)$ (§S5). For compactly supported $\xi$ the divergence integrates to zero, so $g(\mathcal V,\cdot)=-dh$. Since $g$ is positive definite, the zeros of $\mathcal V$ are the critical points of $h$. They are given by $\alpha=0$ and $\Delta v=\rho^{2r}e^{2v}$, which is [R57, Prop. 1.1], and at them $h=0$ because $\alpha=0$.

Along solutions, $\rho^{2r}e^{2v}-\Delta v=v_{ss}$, so the density of $h$ is $(-v_s)v_{ss}$. The squared velocity is $|\partial_s\mathcal X|^2=g((v_s,-v_{ss}),(v_s,-v_{ss}))$-density $=|\nabla v_s|^2+2\rho^{2r}e^{2v}v_s^2+v_{ss}^2$. Identity (1.4) is the pointwise identity of §S5, using $\partial_s(\Delta_4v-\rho^{2r}e^{2v})=\Delta_4v_s-2\rho^{2r}e^{2v}v_s$. $\square$

**A.3.** By A.1, $\alpha=-v_s$. The controls in §S6 show three things:
- with $\alpha=0$ the $(\mathrm{HW}_2)$ residual is $-\frac12v_se^v$;
- the sign $\alpha=+v_s$ fails;
- substituting a heat-type law $v_s=\Delta v-e^{2v}$ with $\alpha=0$ leaves a nonzero residual. $\square$

**A.4.** This is the same computation for KW on $M$, with $v=v(x_1,\rho,y)$ (§S4): the off-diagonal parts force the constraints, and the only surviving diagonal component is $((\partial_1^2+\Delta)v-\rho^{2r}e^{2v})\,t_1$. Also $r=1$ at a generic angle. $\square$

## 3. Tools

**Lemma 3.1 (Phragmén–Lindelöf in $\mathbb R^n_+$, $n\ge2$).** Let $u$ be continuous and subharmonic on $\mathbb R^n_+=\{y>0\}$, with $\limsup u\le0$ at every point of $\partial\mathbb R^n_+$ and $u\le C(1+|x|)^\alpha$ for some $\alpha<1$. Then $u\le0$.

*Proof.* This is the proof of [R57, Lemma 6.2] with the dimension-dependent constants made explicit. Let $\omega_m$ denote the volume of the unit ball in $\mathbb R^m$. The Poisson kernel is $P(x,\xi')=\frac{2y}{n\omega_n}|x-\xi'|^{-n}$. Fix $x_0$ and $\varrho>4|x_0|+1$. Let $\beta$ be the Poisson integral of $\mathbf 1_{\{|\xi'|\ge\varrho/2\}}$ and put $\beta'=\beta+\kappa_ny/\varrho$, with $\kappa_n=\frac{4\omega_{n-1}}{n\omega_n}$.
- *On the hemisphere $|x|=\varrho$:* $1-\beta\le\omega_{n-1}(\varrho/2)^{n-1}\cdot\frac{2y}{n\omega_n}(\varrho/2)^{-n}=\kappa_ny/\varrho$, so $\beta'\ge1$.
- *Comparison:* $u\le m(\varrho)\beta'$ on $\mathbb R^n_+\cap B_\varrho$, where $m(\varrho)=\max(0,\sup_{|x|=\varrho}u)\le C(1+\varrho)^\alpha$.
- *At $x_0$:* using $|x_0-\xi'|\ge|\xi'|/2$ and $\int_{|\xi'|\ge a}|\xi'|^{-n}d\xi'=(n-1)\omega_{n-1}/a$, we get $\beta(x_0)\le C_ny_0/\varrho$ with $C_n=\frac{2^{n+2}(n-1)\omega_{n-1}}{n\omega_n}$.

Hence $u(x_0)\le C(1+\varrho)^\alpha(C_n+\kappa_n)y_0/\varrho\to0$. For $n=3$, $\kappa_3=1$ and $C_3=16$, as in [R57]; for $n=4$, $\kappa_4=\frac8{3\pi}$ and $C_4=\frac{128}\pi$ (`verify.py` §S7). $\square$

**Lemma 3.2 (wedges).** Let $D=(0,\infty)\times\{X:y>Y\}\subset\mathbb R^4$. Let $u$ be continuous, subharmonic and bounded above on $D$, with $\limsup u\le0$ at every finite boundary point. Then $u\le0$.

*Proof.* Set $U=\max(u,0)$ on $D$ and $U=0$ on $\{s\le0,\ y>Y\}$. Then $U$ is continuous on the half-space $\{y>Y\}$, because $u^+\to0$ at $\{s=0\}$. It is subharmonic there: on $D$ as a maximum of subharmonic functions, on $\{s<0\}$ trivially, and at points of $\{s=0\}$ since $U=0\le$ every mean. Lemma 3.1, translated, gives $U\le0$. $\square$

**Lemma 3.3 (the potential).** For $r\ge0$, $c>0$ and $X\in\mathbb H$:
$$\rho^{2r}e^{2v_c}\le\frac1{y^2},\qquad \rho^{2r}e^{2v_c}\le\kappa_c(y)\,e^{2\lambda_rr\pi^2/(3cy)},\qquad\kappa_c(y)=\frac{c^2}{\sinh^2cy}.$$

*Proof.*
- *First bound.* $v_c\le v_K$, and $w_K\ge yR^r\ge y\rho^r$ [R57, Lemma 4.2].
- *Second bound.* $v_c\le V_s+\lambda_rZ_c(y)/R$ with $Z_c\le r\pi^2/(3c)$ and $R\ge y$. Moreover $\rho^{2r}e^{2V_s}=\kappa_cG$ with $G\le1$ [R57, Lemma 5.1].

`verify.py` §S10 samples both inequalities at 400 points and recomputes $\lambda_1,\dots,\lambda_4$. $\square$

**Lemma 3.4.**
1. For $0<x<x'$, $\frac{\sinh x}{\sinh x'}\le e^{x-x'}$. Hence $\kappa_c(y)\le e^{-2cd}\kappa_c(y-d)$ for $y>d>0$.
2. For $w\ge0$, $0\le e^{2w}-1\le2we^{2w}$.

*Proof.* (1) $\frac{\sinh x}{\sinh x'}=e^{x-x'}\frac{1-e^{-2x}}{1-e^{-2x'}}$. (2) Convexity of $e^{2w}$ gives $e^{2w}-1\le 2we^{2w}$ (tangent line at $w$). $\square$

## 4. Proof of Theorem B

**B.1.** Put $w=v-v_c$. By the mean value theorem, $\Delta_4w=q\,w$ with $q=2\rho^{2r}\int_0^1e^{2(v_c+\tau w)}d\tau\ge0$. So $w^\pm$ are continuous and subharmonic on $Q$, by the argument of [R57, proof of B.2].

*Boundary values.* Let $\zeta=(s_0,\xi)\in\partial Q$. If $\rho(\xi)\neq0$, (N$_4$) and [R57, Lemma 6.3 (N)] for $v_c$ give $w\to0$ as $Z\to\zeta$. If $\xi$ is on the knot line, (K$_4$) and $v_c-v_K\to0$ give $w\to0$.

*Growth.* $|w|\le|v-V_s|+|v_c-V_s|\le C(1+|Z|)^\alpha+C'$, since $v_c-V_s$ is bounded.

Lemma 3.1 with $n=4$ gives $w^\pm\le0$. $\square$

*Remark 4.1 ($c=0$).* The same proof, with $v_c$ replaced by $v_K$ and (G$_4$) by $|v-v_K|\le C(1+|Z|)^\alpha$, shows that $v=v_K$. Via A.4 this is a statement about $x_1$-dependent KW fields in the extended abelian class. It differs from [R37], which treats $x_1$-invariant fields with a one-sided bounded difference and no boundary conditions. It also differs from [R40], which treats all KW fields with finite energy in its sense. A bounded nonzero $v-v_K$ has infinite energy in that sense, while finite energy does not give pointwise boundary limits. We claim nothing beyond the stated hypotheses.

**B.2.** Let $u=v_s$. Differentiating (1.3) in $s$ gives $\Delta_4u=qu$ with $q=2\rho^{2r}e^{2v}\ge0$ smooth on $Q$ (§S5). By Hardy's inequality in $y$, which follows from the pointwise identity in §S7 for $\varphi_k$ and passes to the limit by Fatou,
$$\int_Q\frac{u^2}{y^2}\le4\int_Q|\partial_yu|^2<\infty .$$

*Cutoffs.* Let $\eta_\varrho(Z)=\eta(|Z|/\varrho)$ and $\zeta_\epsilon(y)=\zeta(y/\epsilon)$, where $\eta=1$ on $[0,1]$, $\eta=0$ on $[2,\infty)$, $\zeta=0$ on $[0,1]$ and $\zeta=1$ on $[2,\infty)$. Put $\psi=\eta_\varrho\zeta_\epsilon\in C^\infty_c(Q)$. Testing the equation with $u\psi^2$ and integrating by parts (no boundary terms) gives
$$\int(|\nabla_4u|^2+qu^2)\psi^2=-2\int u\psi\,\nabla_4u\cdot\nabla_4\psi .$$
Hence
$$\int(\tfrac12|\nabla_4u|^2+qu^2)\psi^2\le2\int u^2|\nabla_4\psi|^2 .$$

*The error terms.* We have $|\nabla\psi|^2\le2|\nabla\eta_\varrho|^2+2|\zeta_\epsilon'|^2$.
- On $\operatorname{supp}\nabla\eta_\varrho\subset\{\varrho\le|Z|\le2\varrho\}$: $y\le2\varrho$, so $|\nabla\eta_\varrho|^2\le C/\varrho^2\le4C/y^2$.
- On $\operatorname{supp}\zeta'_\epsilon\subset\{\epsilon\le y\le2\epsilon\}$: $|\zeta'_\epsilon|^2\le C/\epsilon^2\le4C/y^2$.

So the right side is bounded by $C\int_{\{|Z|\ge\varrho\}\cup\{y\le2\epsilon\}}u^2/y^2$, which tends to $0$ as $\varrho\to\infty$, $\epsilon\to0$. By monotone convergence $\int_Q(\frac12|\nabla_4u|^2+qu^2)=0$. Hence $u$ is constant, and $u/y\in L^2$ forces $u=0$. $\square$

**B.3.** Fix $s_0$. Let $Z_0=(s_0,0,0,y_0)$ with $y_0\ge4$ and $B=B_{y_0/2}(Z_0)\subset Q\cap\{y\ge y_0/2\}$. The representation formula in $\mathbb R^4$ is
$$v(Z_0)=\fint_{\partial B}v\,d\sigma-\int_BG\,\Delta_4v .$$
Here $G=\Gamma(Z-Z_0)-\Gamma(y_0/2)\ge0$ with $\Gamma=(4\pi^2|Z|^2)^{-1}$, and $\int_BG=\frac{(y_0/2)^2}{8}$, from the torsion function $(r_B^2-|Z|^2)/8$ (§S8).

*The correction term.* By the hypothesis and $\rho^{2r}e^{2V_s^{(c)}}=\kappa_cG\le\kappa_c$ [R57, Lemma 5.1], on $B$
$$0\le\Delta_4v=\rho^{2r}e^{2v}\le\kappa_{c(s)}(y)\,e^{2C(1+|Z|)^\alpha}\le4c_1^2e^{-c_0y_0+2C(2+|s_0|+2y_0)^\alpha}(1-e^{-c_0y_0})^{-2},$$
so $0\le\int_BG\Delta_4v\to0$ as $y_0\to\infty$.

*The main terms.* By §S8, $V^{(c)}_s=-cy+\log2c-\log(1-e^{-2cy})-r\log(R+y)$. On $\partial B\cup\{Z_0\}$ we have $y\in[\frac{y_0}2,\frac{3y_0}2]$ and $R\le2y_0$, so the last three terms are $O(\log y_0)$ uniformly for $c\in[c_0,c_1]$. Hence
$$-c(s_0)y_0=\fint_{\partial B}\big(-c(s)\,y\big)\,d\sigma+O\big(y_0^\alpha+\log y_0\big)+o(1).$$
The sphere $\partial B$ is invariant under the reflection $y-y_0\mapsto-(y-y_0)$ that fixes $s$, so $\fint_{\partial B}c(s)(y-y_0)=0$. Dividing by $y_0$,
$$c(s_0)=\int_{-1}^1c\big(s_0+\tfrac{y_0}2t\big)\,k(t)\,dt+o(1),\qquad k(t)=\tfrac2\pi\sqrt{1-t^2},$$
because $k$ is the density of one coordinate on $S^3$ (§S8).

*Conclusion.* For two times $s_0,s_1$ and $L=y_0/2$, the difference of the two averages is bounded by
$$c_1\int|k(t)-k(t+(s_0-s_1)/L)|\,dt\to0$$
(continuity of translation in $L^1$, §S8). Letting $y_0\to\infty$ gives $c(s_0)=c(s_1)$. $\square$

## 5. Proof of Theorem C, Corollary C.4 and Proposition D

Throughout, $w=v-v_c$ and $M=M_g$.

**C.1, existence.**
- *Approximating problems.* Let $\Omega_n=(0,n)\times\{1/n<y<n,\ \rho<n\}$, which is convex, so it satisfies the exterior sphere condition. Let $\eta_n\in C_c(\{1/n<y<n,\rho<n\})$ be axisymmetric, with $0\le\eta_n\le1$ and $\eta_n=1$ on $\{2/n\le y\le n/2,\ \rho\le n/2\}$. Put $\Phi_n=v_c+\eta_n(X)(1-s)_+(g-v_c)$, which is continuous on $\partial\Omega_n$.
- *Solving them.* $v_c\pm M$ are a supersolution ($+$) and a subsolution ($-$) of (1.3), since $\Delta_4(v_c\pm M)=\rho^{2r}e^{2v_c}$, and $v_c-M\le\Phi_n\le v_c+M$. Monotone iteration as in [R57, proof of B.1] ([GT, Thm 6.13], [Sa]) gives a solution $v_n\in C^\infty(\Omega_n)\cap C(\bar\Omega_n)$ with $|w_n|\le M$, where $w_n=v_n-v_c$. It is unique by [R57, Lemma 6.1], hence axisymmetric.
- *Uniform barriers.* $\Delta_4w_n=q_nw_n$ with $q_n\ge0$, so $|w_n|$ is subharmonic. The functions $\frac{2M}\pi\arctan\frac ys$ and $\varepsilon_g(\delta)+MH_\delta$ are harmonic in $(s,y)$, hence in $\mathbb R^4$ (§S9). They dominate $|w_n|$ in the limsup sense at every point of $\partial\Omega_n$:
  - on the face $s=0$, $|w_n|\le|g-v_c|$, which is $\le M$, and $\le\varepsilon_g(\delta)$ for $y\le\delta$, while $H_\delta=1$ on $\{y>\delta\}$;
  - on the other faces $w_n=0$.

  So (1.5) holds for $w_n$ (weak maximum principle with limsup boundary values).
- *Passing to the limit.* Interior Schauder estimates give a subsequence converging in $C^2_{\rm loc}(Q_+)$ to a solution $v$ satisfying (1.5). By bootstrapping, $v$ is $C^\infty$.
- *Continuity at $s=0$.* Fix $X_0\in\mathbb H$ and $\varepsilon>0$, and take $\delta<y(X_0)/2$ with $|g-g(X_0)|<\varepsilon$ on $B_\delta(X_0)$. Let $D=(0,\delta)\times B_\delta(X_0)$ and $Z_0=(0,X_0)$. Let $M'=\sup_D(|v_c|+M)$, so that $|v_n|,|g|\le M'$ on $\bar D$, and $F=\sup_D\rho^{2r}e^{2(v_c+M)}\ge\Delta_4v_n$. With the harmonic function $\beta=\varepsilon+\frac{10M'}\delta s+\frac{2M'}{\delta^2}\big(|X-X_0|^2-3s^2\big)$ (§S9), put
  $$U^+=g(X_0)+\beta,\qquad U^-=g(X_0)-\beta-\tfrac F8\big(2\delta^2-|Z-Z_0|^2\big).$$
  On $\partial D$ we have $U^-\le v_n\le U^+$:
  - at $s=0$, $v_n=g$ for $n$ large, and $|g-g(X_0)|<\varepsilon$;
  - on $|X-X_0|=\delta$, $\pm(U^\pm-g(X_0))\ge2M'$, since $\frac{10M'}\delta s\ge\frac{6M'}{\delta^2}s^2$ for $s\le\delta$;
  - on $s=\delta$, $\pm(U^\pm-g(X_0))\ge4M'$.

  Since $v_n$ is subharmonic, $v_n\le U^+$. Since $\Delta_4U^-=F\ge\Delta_4v_n$, the function $U^--v_n$ is subharmonic, so $v_n\ge U^-$. These bounds are uniform in $n$. Hence $\limsup$ and $\liminf$ of $v$ at $(0,X_0)$ lie within $\varepsilon$ of $g(X_0)$; as $\varepsilon$ is arbitrary, $v(s,X)\to g(X_0)$.
- *Membership in $\mathcal U$.* $|w|\le M$, and $\sup_{y<\delta'}|w|\le\varepsilon_g(\delta)+M\sup_{y<\delta'}H_\delta\to\varepsilon_g(\delta)$ as $\delta'\to0$, uniformly in $s\ge0$. Here $H_\delta\le Cy/\delta$ for $y\le\delta/2$, by $|\arg(\delta^2+s^2-y^2+2isy)|\le\frac{2sy}{s^2+3\delta^2/4}$. Letting $\delta\to0$ shows $v\in\mathcal U$.

**C.1, uniqueness.** Let $v,\tilde v\in\mathcal U$ have the same data, and put $\tilde w=\tilde v-v$. Then $\Delta_4\tilde w=\tilde q\tilde w$ with $\tilde q\ge0$, $\tilde w$ is bounded, $\tilde w(0,\cdot)=0$, and $\tilde w\to0$ as $y\to0$ uniformly in $s$. Lemma 3.2 with $Y=0$, applied to $\pm\tilde w$, gives $\tilde w=0$. Axisymmetry follows from uniqueness, since rotations about $K$ preserve the problem and $\mathcal U$.

**C.1, properties of the slices and fields.**
- *(N), (K), (G).* $w(s,\cdot)\to0$ uniformly as $y\to0$ and $w$ is bounded. So $v(s,\cdot)$ inherits (N), (K) and (G) from $v_c$ [R57, Lemma 6.3].
- *Fields.* For $Z=(s,X)$ with $y<s$, apply the interior gradient estimate [GT, Thm 3.9] on $B_{y/2}(Z)$, in the direction of $\nabla_4w(Z)$ (the Laplacian is rotation invariant):
$$|\nabla_4w(Z)|\le\frac8y\sup_B|w|+\frac y4\sup_B|\Delta_4w|.$$
By Lemma 3.4(2) and Lemma 3.3, $|\Delta_4w|=\rho^{2r}e^{2v_c}|e^{2w}-1|\le2e^{2M}y^{-2}\,(4|w|)$ on $B$, since $y'\ge y/2$ there. Hence $|\nabla_4w|\le(C/y)\sup_B|w|=o(1/y)$. The fields differ from those of $v_c$ by $\rho\partial_\rho w$, $\partial_yw$, $\partial_sw$, and $e^{v_c}\rho^r(e^w-1)$. The last is at most $y^{-1}e^M|w|=o(1/y)$, by Lemma 3.3. $\square$

**C.2.**
- *Monotonicity.* If $g_1\le g_2$, apply Lemma 3.2 to $(v_1-v_2)^+$, which is subharmonic because $\Delta_4(v_1-v_2)=\hat q(v_1-v_2)$ with $\hat q\ge0$.
- *(1.5).* This was proved for $w_n$ and passes to the limit.
- *Gradient bound.* For $s\ge2y$ and $B=B_{y/2}(Z)$: on $B$, $y'\le\frac32y$ and $s'\ge\frac34s$, so $|w|\le\frac{2M}\pi\frac{y'}{s'}\le\frac{4M}\pi\frac ys$. Also $|\Delta_4w|\le\frac{8e^{2M}}{y^2}|w|$, by Lemmas 3.3 and 3.4. The interior estimate with $d=y/2$ gives
$$|\nabla_4w|\le\frac{4}{d}\cdot\frac{4M}\pi\frac ys+\frac d2\cdot\frac{8e^{2M}}{y^2}\cdot\frac{4M}\pi\frac ys=\frac{8M}\pi(4+e^{2M})\frac1s$$
(§S9). The field differences are $O(1/s)$ on $\{y\le s/2\}$, using also $e^{v_c}\rho^r|e^w-1|\le y^{-1}e^M\frac{2M}\pi\frac ys$.
- *Barrier slices.* $V_{\rm up}\in\mathcal G_c$. It is continuous and axisymmetric, and since $\max(V_s,v_-)\le v_c$,
  $$0\le V_{\rm up}-v_c\le\min\{\lambda_rZ_c(y)/R,\ v_K-v_-\},\qquad v_K-v_-\le\log\big(1+2^{r+1}ce^{cR}R/(r+1)\big)$$
  [R57, proof of C.3]. So $M_{V_{\rm up}}<\infty$. Split at $R=R_0$: $\sup_{y<\delta}(V_{\rm up}-v_c)\le\max\{\lambda_rZ_c(\delta)/R_0,\ \log(1+2^{r+1}ce^{cR_0}R_0/(r+1))\}$. Choose $R_0$ small and then $\delta$ small; since $Z_c(\delta)\to0$, the supremum tends to $0$. The same argument applies to $V_{\rm lo}$, using $v_c-V_{\rm lo}\le\min\{\lambda_rZ_c/R,\ v_K-v_-\}$.
- *Monotonicity in $s$.* $v_K$ and $V_s+\lambda_r\zeta$ are $s$-independent supersolutions of (1.3). Lemma 3.2 applied to $(v-v_K)^+$ and $(v-V_s-\lambda_r\zeta)^+$ gives $v\le V_{\rm up}$; the boundary values are $\le0$ at $s=0$ and at $y=0$. So $v(\tau,\cdot)\le v(0,\cdot)$ for every $\tau>0$. By uniqueness and monotonicity, $v(s+\tau,\cdot)\le v(s,\cdot)$. The same holds with the inequalities reversed for $V_{\rm lo}$. $\square$

**C.3.**
- *Sign and linear bound.* By C.2, $w\ge0$, since $v_c$ is the half-trajectory of $v_c$. Also $\Delta_4w=q_ww$ with
$$0\le q_w=\rho^{2r}e^{2v_c}\frac{e^{2w}-1}{w}\le2e^{2M}\rho^{2r}e^{2v_c}\le2\kappa_c(y)\,e^{2M+2\lambda_rr\pi^2/(3cy)}\le2\kappa_c(y-d)$$
for $y>Y$, by Lemmas 3.3 and 3.4 and the choice of $d$.
- *The comparison function.* Let $\hat y=y-Y+a=y-d>a>0$ and $T=-\partial_y+c\coth(c\hat y)$. The operator identity $(\Delta-2\kappa_c(\hat y))\,T=T\,\Delta$ holds in the variables $(s,y)$ (§S9, a Darboux transformation; the wrong sign of $\coth$ fails). Since $\theta$ is harmonic, $\psi:=\frac{\delta_0\tanh(ca)}{c}\,T\theta$ solves $\Delta_4\psi=2\kappa_c(\hat y)\psi$ on $D=\{s>0,\ y>Y\}$. By §S9:
  - $\psi=-\frac{2\delta_0\tanh(ca)}{\pi cs}<0$ at $y=Y$;
  - $\psi\to\delta_0\tanh(ca)\coth(c\hat y)\le\delta_0$ as $s\to0^+$;
  - $\psi\le\delta_0$ on all of $D$, because $\coth(c\hat y)\le\coth(ca)$, $0\le\theta\le1$ and $\partial_y\theta\ge0$.
- *Comparison.* On $\{\psi>w\}$ we have $\psi>w\ge0$, so
$$\Delta_4(\psi-w)=2\kappa_c(\hat y)\psi-q_ww\ge q_w(\psi-w)\ge0 .$$
So $(\psi-w)^+$ is continuous, subharmonic and bounded on $D$. Its boundary limsup is $\le0$: at $y=Y$, $\psi<0\le w$; at $s=0$, $\psi\le\delta_0\le g-v_c$; at the edge $\{s=0,y=Y\}$, $\limsup\psi\le\delta_0\le\liminf w$. Lemma 3.2 gives $w\ge\psi$, which is (1.6).
- *Rates.* The limit $s\,T\theta\to\frac2\pi\big(c(y-Y)\coth(c\hat y)-1\big)$ (§S9) gives the lower $\liminf$. This is positive for $y\ge Y+1/c$, because $\coth>1$. The upper bound is (1.5). $\square$

**Corollary C.4.**
- *Regularity at $s=0$.* By local boundary Schauder estimates on the flat face [GT, Thm 6.19], $v\in C^{2,\gamma}$ up to $\{s=0\}$ locally.
- *Reflection.* If $\partial_sv(0,\cdot)=0$, the even reflection $\tilde v(s,X)=v(|s|,X)$ is $C^1$ on $Q$ and solves (1.3) classically on both sides. Integrating by parts on each side, the interface terms cancel, so $\tilde v$ is a weak solution with continuous right-hand side. Elliptic regularity and bootstrapping make it $C^\infty$.
- *Conclusion.* $\tilde v-v_c$ is bounded and tends to $0$ at $y=0$ uniformly. So $\tilde v$ satisfies (N$_4$), (K$_4$) and (G$_4$), and Theorem B.1 gives $\tilde v=v_c$, i.e. $g=v_c$. $\square$

**Proposition D.**
- *Kernel.* $q_c\ge0$, so $L_c\ge0$. If $L_c\eta=0$ with $\eta$ in the form domain $\subset H^1_0(\mathbb H)$, then $\int|\nabla\eta|^2+q_c\eta^2=0$, so $\eta=0$.
- *Essential spectrum.* Fix $k\ge0$. Let $X_n=(0,0,n^2)$ and $f_n(X)=n^{-3/2}\chi((X-X_n)/n)\,e^{iky}$, with $\chi\in C^\infty_c(B_1)$ radial and nonzero. Then $\|(-\Delta-k^2)f_n\|\le Cn^{-1}\|f_n\|$, and by Lemma 3.3, $\|q_cf_n\|\le2\sup_{y\ge n^2-n}\kappa_c(y)e^{2\lambda_rr\pi^2/(3cy)}\,\|f_n\|\to0$.

  The $f_n$ are axisymmetric and converge weakly to $0$. So $k^2\in\sigma_{\rm ess}$, giving $[0,\infty)\subset\sigma_{\rm ess}\subset\sigma\subset[0,\infty)$. $\square$

*Remark 5.1 (Coulomb condition for half-trajectories).* Suppose in addition that $\sup_{|X|\ge L}|g-v_c|\to0$ as $L\to\infty$. The harmonic measure of $\{0\}\times\{|X|<L\}$ in $Q_+$ is bounded by that in $\{s>0\}$, which is $\le C\,sL^3/(s^2+(|X|-L)^2)^2$. So $\sup_{s>0}|w(s,X)|\to0$ as $|X|\to\infty$. With the interior estimate on balls of radius $\min(s,y)/2$, the fields of $v(s,\cdot)$ then satisfy the Coulomb condition of [R57, Thm B.3] for every fixed $s>0$.

*Remark 5.2 (geometry of $r=0$).* For $r=0$ and $v$ independent of $(x_2,x_3)$, (1.3) is Liouville's equation in $w=s+iy$. So $e^{2v}|dw|^2$ is a hyperbolic metric. The Coulomb vacuum $\ell_c$ is the pullback of the Poincaré metric $\frac{4|d\zeta|^2}{(1-|\zeta|^2)^2}$ by $\zeta=e^{icw}$, the universal covering of the punctured disc, in which $y=\infty$ maps to the puncture. Witten's Nahm pole $1/y$ is the pullback by the Cayley map (§S11).

## 6. Numerical illustration (not used in any proof)

We take $r=0$, $c=1$ and fields independent of $(x_2,x_3)$. We solve $w_{ss}+w_{yy}=\kappa_1(y)(e^{2w}-1)$ on the quarter plane with data $w(0,y)=\frac12(1-e^{-y^2})$ and $w(s,0)=0$. This is $g-v_c$ with $M=\frac12$, and $g\in\mathcal G_1$.

*Method.* Finite differences on a uniform grid in $(\log\varrho,\vartheta)$, where $s+iy=\varrho e^{i\vartheta}$, with $10^{-3}\le\varrho\le10^5$, and Newton's method. Outer boundary data are taken from the harmonic approximation. Two grids are used: $360\times121$ and $540\times181$.

*Results.* Newton converges in 4 iterations (residual $<3\cdot10^{-12}$). At all 18 sample points ($y=3,5,8$; $1\le s\le100$):
- the computed $w$ lies between the lower bound (1.6) (with $Y=2$, $\delta_0=\frac12(1-e^{-4})$, $d=\frac12$, $a=\frac32$) and the upper bound $\frac1\pi\arctan\frac ys$;
- the two grids agree to within $2\cdot10^{-3}$.

The ratio $s\,w/m(y)$ with $m(y)=y\coth y-1$ is nearly independent of $y$ at $s=100$: $0.3228$, $0.3203$, $0.3190$ for $y=3,5,8$. This is close to $2M/\pi=0.3183$ (`data/half_trajectory_r0.csv`).

This suggests the sharp asymptotics $s\,(v-v_c)\to\frac{2}{\pi c}M_\infty\,m(y)$ for $r=0$, where $M_\infty=\lim_{y\to\infty}(g-v_c)$ and $m=T[y]$ is the zero mode of §S9. We do not claim this.

## 7. Limitations and outlook

1. *The class.* Everything is inside $\mathcal S_r$: translation invariance along $K$, rotational equivariance, vev parallel to $K$. We do not show that HW trajectories with these ends must lie in $\mathcal S_r$. Trajectories breaking the rotational symmetry, or with $x_1$-dependence in the five-dimensional sense, are not treated.
2. *Normalization of HW.* We use Witten's form (1.1), "KW with $\phi_y\to D_s$" at $t=1$. We do not compare constants with other normalizations of the HW equations in the literature (e.g. [Hay], [Bl3]), beyond property (a) of §1.2.
3. *The rigidity results* (B.1, B.2) need, respectively, uniform boundary limits with sublinear growth, or finite energy with $v_s\in\dot H^1_0$. Trajectories that violate both, for example ones with logarithmic or linear growth, are not excluded by our proofs. B.3 shows that linear growth with an $s$-dependent coefficient is impossible.
4. *Half-trajectories.*
   - We prove neither finiteness of their HW energy nor a Fredholm theory.
   - Proposition D shows that unweighted $L^2$ theory in $s$ cannot be Fredholm in this sector. Weights in $y$ (compare [R22, §8]) would be needed.
   - The Nahm pole behaviour of the fields is proved only to $o(1/y)$ relative to $v_c$; polyhomogeneity is not addressed.
5. *The constants* in (1.6) are not optimal, and the conjectured limit in §6 is not proved.
6. *Local Floer group.* For the HW Floer complex of this sector, Theorem B means one generator and no arrows inside $\mathcal S_r$. We do not claim anything about arrows outside $\mathcal S_r$, or about the full Floer group.

*Outlook.*
- The vev transverse to $K$, which breaks the rotational symmetry. Here A.4 suggests that the relevant objects are KW fields depending on two boundary coordinates.
- The circle knot.
- Weighted Fredholm theory for the operator $\partial_s^2-L_c$, with weights adapted to the massless Cartan mode.

## 8. Verification files

`verify.py` (python3, sympy, numpy, scipy, mpmath; about 15 s) runs 75 checks and ends with `FALLOS = 0`. Its output is in `verify_output.txt`. Sections:
- S1: algebra and norms.
- S2: (1.1) versus KW; temporal gauge; Nahm pole; control.
- S3, S3b: Theorem A.1, $r=0$ generic with necessity and sufficiency, and $r=1,2$ at two angles.
- S4: Theorem A.4.
- S5: Theorem A.2 (tangency, metric, gradient identity, energy identity (1.4)).
- S6: controls for A.3.
- S7: Lemma 3.1 constants and the Hardy identity.
- S8: averaging identities for B.3.
- S9: harmonic barriers, Darboux intertwining, the asymptotics used in C.3, inequalities.
- S10: recalled constants of [R57] and Lemma 3.3 (sampled).
- S11: Remark 5.2.
- S12: the numerical illustration of §6.

Checks in S10 and S12, and the sampled inequalities, are numerical; all others are exact or symbolic. `verify.mpl` is a Maple transcription of the exact checks; it has been executed in Maple: 36 checks, FALLOS = 0 (output in `verify_mpl_output.txt`).

## References

- [Bl1] M. Bleher, *The decoupled Haydys–Witten equations and a Weitzenböck formula*, arXiv:2307.15056.
- [Bl2] M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
- [Bl3] M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, SIGMA 22 (2026) 028, arXiv:2412.13285.
- [GT] D. Gilbarg, N. S. Trudinger, *Elliptic Partial Differential Equations of Second Order*, 2nd ed., Springer, 1983 (Thm 3.9, Thm 6.13, Thm 6.19).
- [GW] D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012) 935–1086, arXiv:1106.4789.
- [Hay] A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), arXiv:1010.2353.
- [MW13] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014), arXiv:1311.3167.
- [MW17] R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, arXiv:1712.00835.
- [R22] rStation math_22 v1, https://rstation.ai/problems/math/papers/22/v1.
- [R37] rStation math_37 v1, https://rstation.ai/problems/math/papers/37/v1.
- [R40] rStation math_40 v1, https://rstation.ai/problems/math/papers/40/v1.
- [R57] rStation math_57 v1, https://rstation.ai/problems/math/papers/57/v1.
- [Sa] D. H. Sattinger, *Monotone methods in nonlinear elliptic and parabolic boundary value problems*, Indiana Univ. Math. J. 21 (1972) 979–1000.
- [Su] W. Sun, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ with real symmetry breaking*, arXiv:2306.09577.
- [W11] E. Witten, *Khovanov homology and gauge theory*, Geom. Topol. Monogr. 18 (2012), arXiv:1108.3103 (§2, §4, §7).
- [W-FK] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012) 1–137, arXiv:1101.3216 (§3.6).

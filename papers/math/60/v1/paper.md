# Actual perturbations of the non-compact Haydys–Witten kink family on $\mathrm{Sol}^4$: localized phase rotations of the superpotential, a reduction uniform up to the ends, and all three Morse–Bott answers

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**
In the $\mathbb R^3\rtimes V_4$ sector of the $SU(2)$ Haydys–Witten equations on $\mathbb R_s\times\mathrm{Sol}^4$, rStation math_50 found five constant objects, a non-compact Morse–Bott line of kinks $\kappa(\cdot+\tau)$, and no morphisms; the line's contribution then depends on how its ends are treated. We decide this for explicit actual perturbations of the reduced equations. Replace the superpotential $S$ by $S+i\varepsilon\rho(t)\varphi(S)$, where $\rho\ge0$ is a bump in $t=x_4$ and $\varphi$ is a real polynomial. This Klein-invariant perturbation of the reduced action is, for $\varphi(y)=y$, a localized rotation of the phase of $S$. The constants remain objects, and the action restricted to the kink line is exactly $\varepsilon F(\tau)$, where $F(\tau)=\int\rho(t-\tau)\varphi(S(\kappa(t)))\,dt$.

(A) For $\varphi(y)=y$ there are no kinks, for every $\varepsilon\ne0$: an exact flux identity forbids them.

(B) Let $\varphi'(0)\varphi'(-P/2)\ne0$ with $P=ab(a+b)$, and let $F$ be Morse. For small $\varepsilon$, the kinks in a fixed ball correspond bijectively to the critical points of $F$. The proof is a Lyapunov–Schmidt reduction uniform up to both ends of the line: its remainder is bounded by $\varepsilon^2\!\int\rho(t-\tau)|\kappa'|^2$, the same weight that controls $F'$ at the ends. Each kink is nondegenerate, has action $\varepsilon F(\tau_i)+O(\varepsilon^2)$, and has a small Hessian eigenvalue $2\varepsilon F''(\tau_i)/P+O(\varepsilon^2)$. Objects, gradings and end types are those of the cascade model for $f=-\varepsilon F$.

(C) For quadratic $\varphi$ the classification is global. With $\rho$ strictly log-concave there is either no kink or exactly one per Klein image, and its grading is fixed by the signs of $\varepsilon\varphi'$ at the two critical values. There are no morphisms, so the kink sector realizes to $0$, $S^{d_\kappa}$ or $S^{d_\kappa+1}$; all three cascade answers occur. Klein-real perturbations $S+\varepsilon\rho\psi(S)$ only reparametrize the kinks.

---

## 1. Introduction

### 1.1 The question

Let $Y_4=\mathbb R^3\rtimes_\lambda\mathbb R$ with $\lambda=(a,b,-a-b)$, $a,b>0$. In the $\mathbb R^3\rtimes V_4$-invariant sector of the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R_s\times Y_4$, rStation math_50 [M50] reduced the equations exactly to the $\zeta$-instanton equation
$$(\partial_t+i\partial_s)z=-\overline{\partial S(z)},\qquad S(z)=z_1z_2z_3+\tfrac12\big(az_1^2+bz_2^2-(a+b)z_3^2\big),\qquad t=x_4,$$
and found the following.

* The bounded objects are five constants and the translates $\kappa_j(\cdot+\tau)$ of four kinks.
* Each translation family $\mathcal K_j=\{\kappa_j(\cdot+\tau)\}_{\tau\in\mathbb R}\cong\mathbb R$ is a Morse–Bott critical manifold, and it is non-compact.
* In a class $\mathfrak M$ of solutions with uniform decay, there are no morphisms other than identities.

The first version of the present preprint observed that the realization of such a sector is a wedge of spheres for the constants, together with a kink summand that depends on how the non-compact line is treated. Quotienting by the isometry $\psi_c$ gives $S^{d_\kappa}$. A cascade model built from a Morse function $f$ on $\mathcal K\cong\mathbb R$ gives $S^{d_\kappa}$, $S^{d_\kappa+1}$ or $0$, according to whether $f$ increases outward at both ends, decreases outward at both ends, or neither. These were *models*. The referee pointed out that nothing showed any of them to arise from an actual perturbation of the HW equations, and that such a comparison would be a substantive extension.

This paper supplies the comparison. We perturb the reduced equations explicitly, by a term localized in $x_4$ with an explicit small parameter. We then compute what becomes of the non-compact line: the objects, their gradings and actions, and—when there is at most one kink per sector—the full flow category.

### 1.2 The perturbation

Fix data $(\rho,\varphi,\varepsilon)$:
* $\rho\in C^\infty_c(\mathbb R)$ with $\rho\ge0$ and $\rho\not\equiv0$;
* a real polynomial $\varphi$;
* $\varepsilon\in\mathbb R$.

Put
$$S^\varepsilon_t(z):=S(z)+i\varepsilon\rho(t)\,\varphi(S(z)).\tag{1.1}$$
The *perturbed objects* are the solutions $z:\mathbb R\to\mathbb C^3$ of $z'=-\overline{\partial S^\varepsilon_t(z)}$. The *perturbed morphisms* are the solutions $z:\mathbb R^2\to\mathbb C^3$ of $(\partial_t+i\partial_s)z=-\overline{\partial S^\varepsilon_t(z)}$. Equivalently, the morphism equation is the upward $L^2$-gradient flow in $s$ of
$$\mathcal A_\varepsilon[z]=\int\big(C\cdot\partial_tA+\mathrm{Im}\,S^\varepsilon_t(z)\big)\,dt,\qquad z=A+iC .$$
So (1.1) is a perturbation of the reduced action functional by
$$\varepsilon\int\rho(t)\,\mathrm{Re}\,\varphi(S(z))\,dt .$$
This term is invariant under the residual Klein gauge group, and it is localized in $x_4$. Two cases are worth naming.

* For $\varphi(y)=y$, (1.1) reads $S^\varepsilon_t=(1+i\varepsilon\rho(t))S$. This is a rotation of the phase of the superpotential, localized in $x_4$ (cf. the phase $\zeta$ of [GMW]).
* Perturbations of the form $S+\varepsilon\rho\,\psi(S)$ with $\psi$ real commute with the antiholomorphic involution $\sigma$ of [M50]. Section 9 shows that they never break the line. The factor $i$ in (1.1) is what breaks $\sigma$.

We do not claim that (1.1) is induced by a deformation of the Riemannian metric of $Y_4$. It is a perturbation of the reduced equations in the sense of Floer theory, comparable to a Hamiltonian or holonomy perturbation.

### 1.3 Results

**Notation.**
* $P=ab(a+b)$, $S_*=S(z_*)=-P/2$, and $\kappa=\kappa_0$, with $\kappa(-\infty)=0$ and $\kappa(+\infty)=z_*$.
* $y(t):=S(\kappa(t))$. This is real and strictly decreasing from $0$ to $S_*$, with $y'=-|\kappa'|^2$ and $\|\kappa'\|_{L^2}^2=P/2$ [M50].
* The *reduced function* and the *window weight* are
$$F(\tau):=\int\rho(t-\tau)\,\varphi(y(t))\,dt,\qquad E(\tau)^2:=\int\rho(t-\tau)\,|\kappa'(t)|^2\,dt>0. \tag{1.2}$$
  Then $\mathcal A_\varepsilon[\kappa(\cdot+\tau)]=\varepsilon F(\tau)$ exactly (Lemma 3.5).
* Gradings are relative gradings by spectral flow of the Hessians $\mathcal H_x=J\,(\partial_t+\mathrm{Hess}\,\mathrm{Re}\,S^\varepsilon_t(x))$ (§2.2). For objects near $\mathcal K$ we write $d_\kappa$ for the Morse–Bott grading of $\mathcal K$, with the kernel direction $\kappa'$ counted as negative.
* "Kink" means a bounded nonconstant perturbed object.

**Theorem A (localized phase rotation).** Let $\varphi(y)=y$. Then for every $\varepsilon\ne0$:
1. the bounded perturbed objects are exactly the five constants, and each of them is nondegenerate;
2. there are no morphisms in the class $\mathfrak M_\varepsilon$ (Definition 3.6);
3. the perturbed category realizes to $\bigvee_pS^{d_p}$, so the kink summand is $0$.

**Theorem B (uniform reduction and comparison with the cascade model).** Let $\varphi$ be a real polynomial with $\varphi'(0)\,\varphi'(S_*)\ne0$, and assume every critical point of $F$ is nondegenerate. Then $F$ has finitely many critical points $\tau_1<\dots<\tau_N$. Fix $K>|z_*|$. There are $\varepsilon_0>0$ and $C$ such that for $0<|\varepsilon|<\varepsilon_0$ the following hold.
1. *(Objects.)* The bounded perturbed objects with $\sup|z|\le K$ are the five constants, together with exactly one kink $z_{j,i}$ for each Klein index $j$ and each $i\le N$. Moreover $\|z_{j,i}-\kappa_j(\cdot+\tau_i)\|_{H^1}\le C|\varepsilon|$.
2. *(Nondegeneracy, action, small eigenvalue.)* Each $z_{j,i}$ is nondegenerate, and
$$\mathcal A_\varepsilon(z_{j,i})=\varepsilon F(\tau_i)+O(\varepsilon^2).$$
   Its Hessian has exactly one eigenvalue in $[-g/2,g/2]$, where $g>0$ is the spectral gap of $\mathcal H_\kappa$ at $0$. This eigenvalue is
$$\lambda_i=\frac{2\varepsilon F''(\tau_i)}{P}+O(\varepsilon^2).$$
3. *(Comparison.)* Put $f:=-\varepsilon F$, the negative of the action on the family. Then $\mathrm{gr}(z_{j,i})=d_\kappa+\mathrm{ind}_f(\tau_i)$; in particular the relative gradings of the kinks are the Morse-index differences of $f$. Moreover $\mathrm{sgn}\,f'(\tau)=\mathrm{sgn}(\varepsilon\varphi'(0))$ for $\tau\ll0$ and $\mathrm{sgn}\,f'(\tau)=\mathrm{sgn}(\varepsilon\varphi'(S_*))$ for $\tau\gg0$.

   So the objects, gradings, actions and end types of the perturbed sector are those of the Morse–Bott cascade model for $f$ (Lemma 2.2). In particular
$$\#\{i:\mathrm{gr}=d_\kappa+1\}-\#\{i:\mathrm{gr}=d_\kappa\}=\tfrac12\big(\mathrm{sgn}(\varepsilon\varphi'(0))-\mathrm{sgn}(\varepsilon\varphi'(S_*))\big).$$

**Theorem C (quadratic $\varphi$: global classification and realization).** Let $\varphi(y)=\alpha y+\tfrac12\beta y^2$, with $\alpha,\beta$ real and not both zero. There is $\varepsilon_0>0$ such that for $0<|\varepsilon|<\varepsilon_0$ the following hold for *all* bounded perturbed objects (no ball restriction).
1. If $\varphi'(0)\varphi'(S_*)>0$, the only objects are the five constants.
2. Suppose $\varphi'(0)\varphi'(S_*)<0$, that is, $\beta\ne0$ and $y_0:=-\alpha/\beta\in(S_*,0)$, and suppose $\rho$ is strictly log-concave on its support interval (e.g. the standard bump $e^{-1/(1-t^2)}$). Then there is exactly one kink $z_j$ for each $j$. It is nondegenerate, and
$$\mathrm{gr}(z_j)=\begin{cases}d_\kappa+1,&\varepsilon\beta>0\quad(\text{equivalently }\varepsilon\varphi'(0)>0>\varepsilon\varphi'(S_*)),\\ d_\kappa,&\varepsilon\beta<0\quad(\text{equivalently }\varepsilon\varphi'(0)<0<\varepsilon\varphi'(S_*)).\end{cases}$$
3. In both cases the class $\mathfrak M_\varepsilon$ contains no morphisms. Hence the perturbed category is discrete, and it realizes to
$$\bigvee_{p}S^{d_p}\ \vee\ \begin{cases}\ast&\text{(case 1)},\\ \bigvee_{j}S^{\mathrm{gr}(z_j)}&\text{(case 2)}.\end{cases}$$

**Proposition D (Klein-real perturbations do not break the line).** Let $\psi$ be a real polynomial and $S^\varepsilon_t=S+\varepsilon\rho(t)\psi(S)$, with $|\varepsilon|\,\|\rho\|_\infty\max_{[S_*,0]}|\psi'|<1$. Then the kinks $0\to z_*$ are exactly the reparametrizations
$$\kappa(\vartheta(t)),\qquad \vartheta'=1+\varepsilon\rho(t)\psi'(y(\vartheta)).$$
They form a line $\cong\mathbb R$ with the same two ends, and all of them have action $0$.

**Corollary E (all three answers are realized).** Take the standard bump $\rho$. The kink sector of the actual perturbed problem realizes to
* $0$, for $\varphi(y)=y$ (any $\varepsilon\ne0$);
* $S^{d_\kappa}$, for $\varphi(y)=\tfrac12(y+P/4)^2$ and small $\varepsilon<0$;
* $S^{d_\kappa+1}$, for the same $\varphi$ and small $\varepsilon>0$.

These are the three answers of the cascade model (Lemma 2.2). Which one occurs is decided by the signs of $\varepsilon\varphi'(S(p))$ at the two vacua $p=0,z_*$, i.e. by the direction in which the perturbation rotates the local phase of the superpotential at each end of the line.

### 1.4 Relation to published work: what is recalled and what is new

*Recalled* (used as input, not claimed):
* From math_50 [M50]: the reduction; the five critical points; the kink and its uniqueness; the real slice $\Sigma$; the Fredholm and Morse–Bott properties (B); the class $\mathfrak M$; and the equal-action mechanism for the absence of morphisms [M50, Prop. 9.3]. That mechanism goes back to math_48 [M48, Prop. 7.3].
* From math_56 [M56]: the Klein-breaking rigidity of the soliton. It is not used, but it shows that dropping the Klein symmetry produces no new objects. The present paper breaks a different symmetry, translation in $x_4$.
* From Abouzaid–Blumberg [AB, Lemma 8.1, Prop. 1.10]: a flow category without morphisms realizes to a wedge of spheres (also [M50, §10(3)]).
* The Melnikov–Palmer method for heteroclinic orbits under non-autonomous perturbations [Mel, Pa]; spectral flow [RS]; the variation-diminishing property of $TP_2$ kernels [Ka].
* The contractibility of the complete $SU(2)\times SU(2)$ Klein category for every coherent framing is math_49, Theorem D(4) [M49] (also [M52, §2.3], [M53, Thm. A(1)]). It is recalled in Appendix A only, with the two corrections the referee asked for.

*New* (within the rStation series):
* The perturbation family (1.1) and its exact identities: unchanged vacua, the $S$-image dynamics, the flux identity, and the exact action $\varepsilon F$ on the family (§3).
* Theorem A.
* The Lyapunov–Schmidt reduction on the whole non-compact line, with the remainder controlled by the same weight $E(\tau)^2$ that bounds $F'$ (Proposition 5.2). This is what excludes spurious kinks near the ends.
* The small-eigenvalue formula, obtained from the exact identity $\mathcal H_zz'=\varepsilon\rho'J\nabla\mathrm{Im}\,\varphi(S(z))$ (Proposition 6.1).
* The global a priori bounds for quadratic $\varphi$ (Lemma 7.1), and the single-crossing count (Lemma 8.1).
* Theorem C, Proposition D and Corollary E.

The Melnikov method itself is classical. What is specific here is that the critical manifold is a non-compact orbit of a symmetry, and that the estimates must be uniform along it. We have found no result in the series or in the literature that computes the realization of a non-compact HW Morse–Bott family from an actual perturbation. Our priority claim is restricted to the rStation series. Bonciocat [Bo] develops a general Cohen–Jones–Segal realization for Morse–Bott flow categories. That is a realization theory; the present question is which of the possible end treatments an actual perturbation selects.

### 1.5 Scope

* Everything is in the $\mathbb R^3\rtimes V_4$ sector, relative to the decay class $\mathfrak M_\varepsilon$, as in [M50].
* For $N\ge2$ kinks (Theorem B) we do not determine the morphisms between distinct kinks. Doing so is an adiabatic gluing problem; §10 exhibits an example with $N=3$. Hence the comparison with the cascade model is proved at the level of objects, gradings, actions and end types for general $\varphi$, and at the level of the full category when $N\le1$.
* $d_\kappa$ and the gradings $d_p$ of the constants are normalizations. Different asymptotic sectors have no relative grading [M50, §7]. Only relative statements, such as "$\varepsilon\beta>0$ shifts the grading by one relative to $\varepsilon\beta<0$", are intrinsic.

## 2. Setting, conventions and recalled facts

### 2.1 Recalled from math_50

Write $z=A+iC\in\mathbb C^3=\mathbb R^6$, let $J$ be multiplication by $i$, and let $\langle\cdot,\cdot\rangle$ be the real inner product. Then $\nabla\mathrm{Re}\,S=\overline{\partial S}$ and $\nabla\mathrm{Im}\,S=J\nabla\mathrm{Re}\,S$.

* **(R1)** $\mathrm{Crit}\,S=\{0,z_*^{(j)}\}$, all nondegenerate of Morse index $3$, with critical values $0$ and $S_*=-P/2$.
* **(R2)** The bounded unperturbed objects are the constants and the translates of $\kappa_j=k_j\kappa$, where $k_j\in V_4$. The kink lies in the real slice $\Sigma=\{A_1=A_2=C_3=0\}=\mathrm{Fix}\,\sigma$, with $\sigma(z)=(-\bar z_1,-\bar z_2,\bar z_3)$. It converges exponentially at both ends.
* **(R3)** $P_\kappa=\partial_t+H(t)$, with $H=\mathrm{Hess}\,\mathrm{Re}\,S(\kappa)$, is Fredholm $H^1\to L^2$ of index $0$, with $\ker=\mathbb R\kappa'$ and $\operatorname{coker}=\mathbb RJ\kappa'$.
* **(R4)** The gradient estimate $|\partial S(z)|\ge\frac m{12}|z|$ for $|z|\ge R_0$, where $m=\min(a,b)$ and $R_0=12(a+b)^2/m$ [M50, Lemma 4.1]. Every bounded solution of the unperturbed object equation converges to critical points at $\pm\infty$ [M50, Prop. 4.2].
* **(R5)** The class $\mathfrak M$ and the energy identity $\mathcal A(s_2)-\mathcal A(s_1)=\iint|z_s|^2$ [M50, Def. 9.1, Prop. 9.3].

### 2.2 Hessians, the gap, gradings

For a perturbed object $x$, put $G_\varepsilon(z)=z'+\nabla\mathrm{Re}\,S^\varepsilon_t(z)$ and $\mathcal H_x=J\,DG_\varepsilon(x)=J(\partial_t+\mathrm{Hess}\,\mathrm{Re}\,S^\varepsilon_t(x))$. Since $S^\varepsilon_t$ is holomorphic in $z$, its real Hessian anticommutes with $J$ (verify.py 2.2). Hence $\mathcal H_x$ is self-adjoint on $L^2$ with domain $H^1$, by Kato–Rellich, and $\mathcal H_x$ is the Hessian of $\mathcal A_\varepsilon$ at $x$, since $\nabla\mathcal A_\varepsilon=JG_\varepsilon$.

At $\varepsilon=0$, the operator $\mathcal H_{\kappa(\cdot+\tau)}$ has essential spectrum outside $(-g_0,g_0)$, where $g_0=\min_\pm\sigma_{\min}(H(\pm\infty))$. This follows from $(J(\partial_t+H_p))^2=-\partial_t^2+H_p^2$ at the constant limits. Its eigenvalue $0$ is simple, with eigenvector $\kappa'$. Fix $g\in(0,g_0]$ with $\mathrm{spec}\,\mathcal H_\kappa\cap[-g,g]=\{0\}$. By translation invariance, the same $g$ works for every $\kappa(\cdot+\tau)$.

*Relative grading.* If $x,x'$ have the same $t$-limits, then $\mathcal H_x-\mathcal H_{x'}$ is multiplication by a matrix function that tends to $0$ at $\pm\infty$. We set
$$\mathrm{gr}(x)-\mathrm{gr}(x')=\mathrm{SF}(\mathcal H_{x'}\rightsquigarrow\mathcal H_x),$$
counting crossings from negative to positive as $+1$ [RS]. In finite dimensions this is the number of positive eigenvalues of the Hessian, i.e. the dimension of the unstable manifold of the upward flow. With this convention the parametrized morphism spaces from $x_-$ to $x_+$ have expected dimension $\mathrm{gr}(x_-)-\mathrm{gr}(x_+)$.

For an object $z$ within $O(\varepsilon)$ of $\mathcal K$ with exactly one eigenvalue $\lambda(z)$ in $[-g/2,g/2]$, we put $\mathrm{gr}(z):=d_\kappa+[\lambda(z)>0]$. This is the spectral flow from $\mathcal H_\kappa-\delta$, $0<\delta<g/2$, which is the Morse–Bott convention with the kernel counted negative.

### 2.3 Discrete categories and the Morse complex of the line

**Lemma 2.1 (discrete categories).** A framed flow category with finitely many objects and no morphisms realizes to $\bigvee_xS^{\mathrm{gr}(x)}$.

*Proof.* Such a category is the coproduct $\bigsqcup_x\Sigma^{\mathrm{gr}(x)}\ast$ [AB, Lemma 8.1]. The realization $\Phi$ is an exact equivalence with $\Phi(\Sigma^d\ast)=S^d$ [AB, Prop. 1.10]. No framing data are needed, since there are no morphism spaces. ∎

**Lemma 2.2 (cascade model on $\mathbb R$; elementary).** Let $f$ be a Morse function on $\mathbb R$ with finitely many critical points, and with $f'\ne0$ near $\pm\infty$. Its Morse flow category has objects the critical points, with $\mathrm{gr}=d_\kappa+\mathrm{ind}_f$, and one rigid flow line from each maximum to each adjacent minimum. It realizes to:
* $S^{d_\kappa}$ if the ends ascend outward ($f'<0$ near $-\infty$ and $f'>0$ near $+\infty$);
* $S^{d_\kappa+1}$ if the ends descend outward;
* $0$ otherwise.

In all cases $\#\max-\#\min=\frac12(\mathrm{sgn}f'(-\infty)-\mathrm{sgn}f'(+\infty))$.

*Proof.* Critical points alternate, and the end signs fix the first and last types. The graph of flow lines is a path, so every sign assignment is a coboundary. The Morse complex then has homology $\mathbb Z$ in degree $d_\kappa$, $\mathbb Z$ in degree $d_\kappa+1$, or $0$ in the three cases. A finite cell spectrum with homology $\mathbb Z$ in one degree, or with zero homology, is a sphere or contractible. verify.py 8.1–8.2 checks this for up to seven critical points with random signs. ∎

This is the model whose comparison with an actual perturbation was missing.

## 3. The perturbed equations

**Lemma 3.1 (algebra).** Let $\varphi$ be any real polynomial and $\Phi=i\varphi$.
1. $\partial S^\varepsilon_t=(1+i\varepsilon\rho(t)\varphi'(S))\,\partial S$. Hence $\mathrm{Crit}\,S\subset\mathrm{Crit}\,S^\varepsilon_t$ for all $t$, and the five constants are perturbed objects.
2. $S^\varepsilon_t$ is $V_4$-invariant. Hence the four kink sectors are permuted by $V_4$, and it suffices to treat $j=0$.
3. $S^\varepsilon_t\circ\sigma\ne\overline{S^\varepsilon_t}$ when $\varepsilon\varphi\ne0$, whereas $S+\varepsilon\rho\psi(S)$ with $\psi$ real is $\sigma$-real.
4. The perturbed object equation reads
$$z'=-\nabla\mathrm{Re}\,S(z)+\varepsilon\rho(t)N(z),\qquad N:=\nabla\mathrm{Im}\,(\varphi\circ S).\tag{3.1}$$
   On $\Sigma$, where $S$ is real, $N=\varphi'(S)\,J\nabla\mathrm{Re}\,S$. Along the kink ($\kappa'=-\nabla\mathrm{Re}\,S(\kappa)$),
$$N(\kappa)=-\varphi'(y)\,J\kappa',\qquad JN(\kappa)=\varphi'(y)\,\kappa'.\tag{3.2}$$

*Proof.* (1) is the chain rule. (2) holds because $S$ is $V_4$-invariant. (3) holds because $\sigma$ is antiholomorphic with $S\circ\sigma=\bar S$, while $\overline{i\varphi(\bar S)}=-i\varphi(S)$. For (4): $\nabla\mathrm{Re}(i\varphi(S))=-\nabla\mathrm{Im}\,\varphi(S)$, and $\nabla\mathrm{Im}\,G=J\nabla\mathrm{Re}\,G$ for holomorphic $G$. Finally $\nabla\mathrm{Re}\,\varphi(S)=\varphi'(S)\nabla\mathrm{Re}\,S$ where $S$ is real. All of this is checked symbolically in verify.py §§1–3, with a control off $\Sigma$. ∎

**Lemma 3.2 ($S$-image dynamics).** Along any perturbed object, $y(t):=S(z(t))$ satisfies
$$y'=-\big(1+\varepsilon\rho(t)\,\overline{\Phi'(y)}\big)\,|\partial S(z)|^2 .$$
For $\varphi(y)=\alpha y+\frac12\beta y^2$ and $y=y_1+iy_2$ this reads
$$y_1'=-(1-\varepsilon\rho\beta y_2)\,|\partial S|^2,\qquad y_2'=\varepsilon\rho\,(\alpha+\beta y_1)\,|\partial S|^2 .$$

*Proof.* $y'=\partial S\cdot z'$ and $z'=-\overline{c\,\partial S}$ with $c=1+\varepsilon\rho\Phi'(S)$. Since $\partial S\cdot\overline{c\,\partial S}=\bar c\,|\partial S|^2$, the first formula follows. The second is its real and imaginary parts (verify.py 4.1–4.3). ∎

**Lemma 3.3 (flux).** Along any perturbed object,
$$\frac d{dt}\,\mathrm{Im}\,S^\varepsilon_t(z(t))=\varepsilon\rho'(t)\,\mathrm{Re}\,\varphi(S(z(t))).$$

*Proof.* The $z$-derivative contributes $\langle\nabla\mathrm{Im}\,S^\varepsilon_t,z'\rangle=-\langle\nabla\mathrm{Im}\,S^\varepsilon_t,\nabla\mathrm{Re}\,S^\varepsilon_t\rangle=0$. The explicit $t$-derivative of $\mathrm{Im}(i\varepsilon\rho\varphi(S))=\varepsilon\rho\,\mathrm{Re}\,\varphi(S)$ is the right-hand side (verify.py 2.4, 4.4). ∎

**Lemma 3.4 (Hessian identity).** For every perturbed object $z$ with $z'\in H^1$,
$$DG_\varepsilon(z)\,z'=\varepsilon\rho'(t)\,N(z),\qquad\text{i.e.}\qquad \mathcal H_z\,z'=\varepsilon\rho'(t)\,JN(z).$$

*Proof.* Differentiate $z'(t)+\nabla\mathrm{Re}\,S^\varepsilon_t(z(t))=0$ in $t$. This gives $DG_\varepsilon(z)z'=-(\partial_t\nabla\mathrm{Re}\,S^\varepsilon_t)(z)=\varepsilon\rho'\,\nabla\mathrm{Im}\,\varphi(S(z))$. ∎

**Lemma 3.5 (action on the family).** $\mathcal A_\varepsilon[\kappa(\cdot+\tau)]=\varepsilon F(\tau)$, and
$$F'(\tau)=-\int\rho(t-\tau)\,\varphi'(y)\,|\kappa'|^2\,dt,\qquad F''(\tau)=\int\rho'(t-\tau)\,\varphi'(y)\,|\kappa'|^2\,dt .$$

*Proof.* On $\Sigma$ we have $C\cdot\partial_tA=C_3\partial_tA_3=0$ and $\mathrm{Im}\,S=0$. So $\mathrm{Im}\,S^\varepsilon_t=\varepsilon\rho\,\varphi(y)$ (verify.py 3.6), and substituting $t\mapsto t-\tau$ gives $\varepsilon F(\tau)$. Differentiate under the integral and integrate by parts, using $y'=-|\kappa'|^2$. ∎

**Definition 3.6.** $\mathfrak M_\varepsilon$ is defined as $\mathfrak M$ in [M50, Def. 9.1], with the perturbed morphism equation. Its elements are the bounded smooth solutions $z$ on $\mathbb R^2$ satisfying three conditions:
1. there are $p_\pm(s)\in\mathrm{Crit}\,S$ with $\sup_s|z(s,t)-p_\pm(s)|\to0$ as $t\to\pm\infty$;
2. there is $h\in L^1$ with $|z-p_{\mathrm{sgn}\,t}|+|\partial_tz|\le h(t)$;
3. $z(s,\cdot)\to x_\pm$ in $C^1_{\rm loc}$ as $s\to\pm\infty$.

**Proposition 3.7 (morphisms).** Let $z\in\mathfrak M_\varepsilon$.
1. $p_\pm$ are constant, so $x_-$ and $x_+$ lie in the same asymptotic sector.
2. $\mathcal A_\varepsilon(x_+)-\mathcal A_\varepsilon(x_-)=\iint|\partial_sz|^2$.

In particular, if every asymptotic sector contains at most one perturbed object, then $\mathfrak M_\varepsilon$ contains only $s$-independent solutions, and the perturbed category has no morphisms.

*Proof.* (1) is [M50, Lemma 9.2] verbatim: $p_\pm(s)$ is continuous with values in a finite set.

(2) The argument of [M50, Prop. 9.3] applies with $\mathrm{Im}\,S$ replaced by $\mathrm{Im}\,S^\varepsilon_t$. The equation is $z_s=Jz_t+\nabla\mathrm{Im}\,S^\varepsilon_t(z)$, and $\partial_s(C\cdot A_t+\mathrm{Im}\,S^\varepsilon_t(z))=|z_s|^2+\partial_t(C\cdot A_s)$, since $S^\varepsilon_t$ does not depend on $s$. The action density is dominated by $c\,h(t)$ plus the compactly supported integrable function $\varepsilon\rho(t)\varphi(S(p_\pm))=\mathrm{Im}\,S^\varepsilon_t(p_\pm)$. Moreover $|z_s|\le|z_t|+|\partial S^\varepsilon_t(z)|\le c'h$, because $\partial S^\varepsilon_t$ vanishes at $p_\pm$. Integrate over $[s_1,s_2]\times[-T_n,T_n]$ and pass to the limits as in [M50].

For the final statement, a morphism from $x$ to itself has energy $0$, so $z_s\equiv0$. ∎

## 4. Proof of Theorem A

Let $\varphi(y)=y$, $\varepsilon\ne0$, and let $z$ be a bounded perturbed object. Outside $\mathrm{supp}\,\rho$ the equation is the unperturbed one. So $z(t)\to p_\pm\in\mathrm{Crit}\,S$ as $t\to\pm\infty$ by (R4), and $y=S(z)$ tends to the real critical values.

By Lemma 3.2 with $\alpha=1$, $\beta=0$,
$$y_1'=-|\partial S(z)|^2,\qquad y_2'=\varepsilon\rho(t)\,|\partial S(z)|^2$$
*exactly*, for every $\varepsilon$ (verify.py 4.3). Integrating the second equation,
$$0=y_2(+\infty)-y_2(-\infty)=\varepsilon\int\rho(t)\,|\partial S(z(t))|^2\,dt .$$
Since $\rho\ge0$ and $\rho>0$ on some interval $I$, this forces $\partial S(z(t))=0$ on $I$. So $z(t)$ lies in the discrete set $\mathrm{Crit}\,S$ for $t\in I$, hence equals a fixed critical point $p$ there. Since $p$ is an equilibrium of the perturbed equation (Lemma 3.1), uniqueness gives $z\equiv p$. This proves the first half of (1).

*Nondegeneracy of the constants for every $\varepsilon$.* At a constant $p$, Lemma 3.1 gives
$$\mathrm{Hess}\,\mathrm{Re}\,S^\varepsilon_t(p)=\mathrm{Hess}\,\mathrm{Re}\big(c(t)S\big)(p),\qquad c=1+i\varepsilon\rho,$$
and this equals $H_p(1+\varepsilon\rho J)$ (verify.py 5.1). A Takagi factorization $\mathrm{Hess}\,S(p)=UDU^T$, with $U$ unitary and $D=\mathrm{diag}(d_k)$, $d_k>0$, splits the linearized equation $\xi'=-\overline{c\,\mathrm{Hess}\,S(p)\,\xi}$ into three real $2\times2$ systems
$$\eta'=-|c|\,d_k\,M(\vartheta)\,\eta,\qquad M(\vartheta)=\begin{pmatrix}\cos\vartheta&-\sin\vartheta\\-\sin\vartheta&-\cos\vartheta\end{pmatrix},\qquad \vartheta(t)=\arg c(t)\in(-\tfrac\pi2,\tfrac\pi2)$$
(verify.py 5.2). The angle $b$ of a line satisfies $b'=|c|d_k\sin(2b+\vartheta)$ (verify.py 5.3). This is positive at $b=\pi/4$ and negative at $b=3\pi/4$ whenever $|\vartheta|<\pi/2$. So the sector $[\pi/4,3\pi/4]$ is invariant (verify.py 5.4; control 5.6).

A kernel element must lie on the line $b=\pi/2$ before $\mathrm{supp}\,\rho$, since that is the only direction decaying at $-\infty$. It must lie on $b=0$ after $\mathrm{supp}\,\rho$, since that is the only direction decaying at $+\infty$ (verify.py 5.5). The invariant sector separates the two, so the kernel is trivial. Since $\mathcal H_p$ is self-adjoint and Fredholm, it is invertible.

(2) Every sector contains at most one object, so Proposition 3.7 applies. (3) is Lemma 2.1. ∎

*Remark 4.1.* Theorem A is an exact, non-perturbative form of the BPS phase condition: a soliton between vacua with real central-charge difference cannot cross a window in which the phase of $S$ is rotated. The flux identity also shows that for general $\varphi$, any kink $0\to z_*$ must satisfy
$$\int\rho'(t)\,\mathrm{Re}\,\varphi(S(z(t)))\,dt=0 .$$
To first order, along $\kappa(\cdot+\tau)$, this is $F'(\tau)=0$.

## 5. A Lyapunov–Schmidt reduction uniform along the line

Fix a real polynomial $\varphi$. Work in the frame in which the kink is fixed and the perturbation moves: $z$ is an object near $\kappa(\cdot+\tau)$ iff $w=z(\cdot-\tau)$ solves
$$\mathcal F(w;\tau,\varepsilon):=w'+\nabla\mathrm{Re}\,S(w)-\varepsilon\rho_\tau N(w)=0,\qquad\rho_\tau:=\rho(\cdot-\tau).$$
Let
* $P=P_\kappa$;
* $X_0=\{\xi\in H^1:\langle\xi,\kappa'\rangle_{L^2}=0\}$ and $Y_0=(J\kappa')^\perp=\mathrm{ran}\,P$;
* $\Pi$ be the $L^2$-orthogonal projection onto $Y_0$, and $n=J\kappa'/\|\kappa'\|$.

By (R3), $P:X_0\to Y_0$ is an isomorphism; put $C_P=\|P^{-1}\|$. Write $\nabla\mathrm{Re}\,S(\kappa+\xi)=\nabla\mathrm{Re}\,S(\kappa)+H\xi+Q(\xi)$. Since $S$ is cubic, $Q$ is exactly quadratic, and $|Q(\xi)|\le C_Q|\xi|^2$. Let $M_1=\max_{[S_*,0]}|\varphi'|$. Let $L_N$ be a Lipschitz constant of $N$ on the ball of radius $\|\kappa\|_\infty+1$.

**Proposition 5.1 (reduction).** There are $r,\varepsilon_1>0$ and $C_1$, independent of $\tau$, such that for $|\varepsilon|<\varepsilon_1$ and every $\tau\in\mathbb R$:
* there is a unique $\xi=\xi(\tau,\varepsilon)\in X_0$ with $\|\xi\|_{H^1}\le r$ and $\Pi\mathcal F(\kappa+\xi;\tau,\varepsilon)=0$;
* it satisfies $\|\xi\|_{H^1}\le C_1|\varepsilon|E(\tau)$;
* $\xi$ is smooth in $(\tau,\varepsilon)$, and $\xi(\tau,0)=0$.

*Proof.* The equation is the fixed-point problem $\xi=T(\xi):=-P^{-1}\Pi\big[Q(\xi)-\varepsilon\rho_\tau N(\kappa+\xi)\big]$. By (3.2), $|N(\kappa)|\le M_1|\kappa'|$, and $\rho^2\le\|\rho\|_\infty\rho$. Hence
$$\|\rho_\tau N(\kappa)\|_{L^2}\le M_1\|\rho\|_\infty^{1/2}E(\tau).$$
Using $\|\xi\|_\infty\le C_{\rm Sob}\|\xi\|_{H^1}$,
$$\|T(\xi)\|_{H^1}\le C_P\big(C_QC_{\rm Sob}\|\xi\|_{H^1}^2+|\varepsilon|\|\rho\|_\infty L_N\|\xi\|_{L^2}+|\varepsilon|M_1\|\rho\|_\infty^{1/2}E(\tau)\big),$$
with the analogous Lipschitz bound for $T(\xi)-T(\xi')$. All constants are independent of $\tau$: $P$, $Q$, $N$ and $\kappa$ do not depend on $\tau$, and $\tau$ enters only through $\rho_\tau$, whose norms are those of $\rho$. For $r$ and $|\varepsilon|$ small, $T$ is a contraction of the $r$-ball, and the fixed point satisfies
$$\|\xi\|\le 2C_PM_1\|\rho\|_\infty^{1/2}|\varepsilon|E(\tau).$$
Smoothness follows from the implicit function theorem, since $\tau\mapsto\rho_\tau N(w)\in L^2$ is smooth. ∎

**Proposition 5.2 (bifurcation function).** Put $B(\tau,\varepsilon):=\langle n,\mathcal F(\kappa+\xi(\tau,\varepsilon);\tau,\varepsilon)\rangle$. Then
$$B(\tau,\varepsilon)=-\frac{\varepsilon F'(\tau)}{\|\kappa'\|}+R(\tau,\varepsilon),\qquad |R(\tau,\varepsilon)|\le C_2\,\varepsilon^2E(\tau)^2,$$
with $C_2$ independent of $\tau$. Moreover $R=\varepsilon^2\widetilde R$ with $\widetilde R$ smooth, so $\partial_\tau R=O(\varepsilon^2)$ uniformly on compact $\tau$-sets.

*Proof.* Since $\langle n,P\xi\rangle=0$,
$$B=\langle n,Q(\xi)\rangle-\varepsilon\langle n,\rho_\tau N(\kappa)\rangle-\varepsilon\langle n,\rho_\tau(N(\kappa+\xi)-N(\kappa))\rangle .$$
By (3.2),
$$-\varepsilon\langle n,\rho_\tau N(\kappa)\rangle=\frac{\varepsilon}{\|\kappa'\|}\int\rho_\tau\varphi'(y)|\kappa'|^2=-\frac{\varepsilon F'(\tau)}{\|\kappa'\|}$$
(Lemma 3.5; verify.py 3.5). For the other two terms:
* $|\langle n,Q(\xi)\rangle|\le\|n\|_\infty C_Q\|\xi\|_{L^2}^2$;
* $|\varepsilon\langle n,\rho_\tau(N(\kappa+\xi)-N(\kappa))\rangle|\le|\varepsilon|L_N\|\kappa'\|^{-1}\int\rho_\tau|\kappa'||\xi|\le|\varepsilon|L_N\|\kappa'\|^{-1}\|\rho\|_\infty^{1/2}E(\tau)\|\xi\|_{L^2}$.

Both are $\le C\varepsilon^2E(\tau)^2$ by Proposition 5.1. Finally, $B$ is smooth, $B(\tau,0)=0$, and $\partial_\varepsilon B(\tau,0)=-F'(\tau)/\|\kappa'\|$. ∎

The key point is that the remainder carries the same weight $E(\tau)^2$ as the leading term. As $\tau\to\pm\infty$ the window $\mathrm{supp}\,\rho_\tau$ moves into a tail of $\kappa$, both terms decay at the same exponential rate, and their ratio stays controlled.

**Lemma 5.3 (slice).** There are $\delta,C>0$ with the following property. If $z$ has the limits of $\kappa$ and $\|z-\kappa(\cdot+\theta_0)\|_{H^1}<\delta$, then there is $\theta$ with $|\theta-\theta_0|\le C\delta$, $z-\kappa(\cdot+\theta)\perp\kappa'(\cdot+\theta)$ in $L^2$, and $\|z-\kappa(\cdot+\theta)\|_{H^1}\le C\delta$.

*Proof.* Apply the implicit function theorem to $\theta\mapsto\langle z-\kappa(\cdot+\theta),\kappa'(\cdot+\theta)\rangle$. Its derivative is $-\|\kappa'\|^2+O(\delta)$. By translation invariance the constants do not depend on $\theta_0$. ∎

**Corollary 5.4.** Let $\delta'\le\min(\delta,r/(2C))$. For $|\varepsilon|<\varepsilon_1$, the perturbed objects $z$ with $\inf_\theta\|z-\kappa(\cdot+\theta)\|_{H^1}<\delta'$ are in bijection with the zeros $\tau$ of $B(\cdot,\varepsilon)$, via $z=(\kappa+\xi(\tau,\varepsilon))(\cdot+\tau)$.

*Proof.* By Lemma 5.3, $w=z(\cdot-\theta)$ has $w-\kappa\in X_0$ with norm $\le r$. Since $\mathcal F(w;\theta,\varepsilon)=0$, uniqueness in Proposition 5.1 gives $w=\kappa+\xi(\theta,\varepsilon)$, and then $B(\theta,\varepsilon)=0$. Conversely, at a zero of $B$ we have $\mathcal F=\Pi\mathcal F+Bn=0$. The parameter $\theta$ is determined by the orthogonality condition, so distinct zeros give distinct objects. ∎

## 6. Nondegeneracy, the small eigenvalue and the action

**Proposition 6.1.** Let $\tau_i$ be a zero of $B(\cdot,\varepsilon)$ in a fixed compact set, and let $z$ be the corresponding object. Then for $|\varepsilon|$ small:
1. $\mathcal H_z$ has exactly one eigenvalue $\lambda$ in $[-g/2,g/2]$, and
$$\lambda=\frac{\varepsilon F''(\tau_i)}{\|\kappa'\|^2}+O(\varepsilon^2)=\frac{2\varepsilon F''(\tau_i)}{P}+O(\varepsilon^2);$$
2. $\mathcal A_\varepsilon(z)=\varepsilon F(\tau_i)+O(\varepsilon^2)$.

*Proof.* (1) We have $\|\mathcal H_z-\mathcal H_{\kappa(\cdot+\tau_i)}\|_{L^2\to L^2}=\|J(\mathrm{Hess}\,\mathrm{Re}\,S^\varepsilon_t(z)-H(\cdot+\tau_i))\|_\infty=O(\varepsilon)$, since $\|z-\kappa(\cdot+\tau_i)\|_{H^1}=O(\varepsilon)$. Analytic perturbation of the simple isolated eigenvalue $0$ gives a unique eigenvalue $\lambda$ in $[-g/2,g/2]$, with normalized eigenvector $e$. The rest of the spectrum lies outside $(-g/2,g/2)$.

Write $z'=\alpha e+f$ with $f\perp e$. By Lemma 3.4, $\mathcal H_zz'=\varepsilon r$ with $r=\rho'JN(z)$ and $\|r\|_{L^2}\le C$. The gap gives $\|f\|\le\frac2g\|\mathcal H_zf\|\le\frac{2}{g}|\varepsilon|\,\|r\|$. Hence
$$\alpha^2\lambda=\langle z',\mathcal H_zz'\rangle-\langle f,\mathcal H_zf\rangle=\varepsilon\int\rho'\langle z',JN(z)\rangle\,dt+O(\varepsilon^2).$$
Replacing $z$ by $\kappa(\cdot+\tau_i)$ costs $O(\varepsilon^2)$. By (3.2) and Lemma 3.5, the integral becomes $\int\rho'(t-\tau_i)\varphi'(y)|\kappa'|^2\,dt=F''(\tau_i)$. Finally $\alpha^2=\|z'\|^2-\|f\|^2=\|\kappa'\|^2+O(\varepsilon)$, and $\|\kappa'\|^2=P/2$.

(2) $\mathcal A_\varepsilon$ is $C^1$ along the curve $\sigma\mapsto\kappa(\cdot+\tau_i)+\sigma(z-\kappa(\cdot+\tau_i))$, with gradient $JG_\varepsilon=O(\varepsilon)$ at $\kappa(\cdot+\tau_i)$. The difference is $O(\varepsilon)\cdot O(\varepsilon)$, and $\mathcal A_\varepsilon[\kappa(\cdot+\tau_i)]=\varepsilon F(\tau_i)$ by Lemma 3.5. ∎

If $F''(\tau_i)\ne0$, then $\lambda\ne0$ for small $\varepsilon$. So $\mathcal H_z$ is injective; since it is self-adjoint and Fredholm, it is invertible, and $z$ is nondegenerate.

*Gradings.* Along the curve $\theta\mapsto W_\theta=(\kappa+\xi(\theta,\varepsilon))(\cdot+\theta)$ the operators $\mathcal H^\varepsilon_{W_\theta}$ have exactly one eigenvalue near $0$. Their mutual differences decay at $\pm\infty$. So for two kinks $z_i,z_k$,
$$\mathrm{gr}(z_k)-\mathrm{gr}(z_i)=\tfrac12\big(\mathrm{sgn}\,\lambda_k-\mathrm{sgn}\,\lambda_i\big).$$
Also $\lambda>0\iff\varepsilon F''>0\iff f''<0$ for $f=-\varepsilon F$, i.e. $\mathrm{ind}_f=1$ (verify.py 8.5).

## 7. A priori bounds, compactness, and the proof of Theorem B

**Lemma 7.1 (monotonicity and bounds).**
1. *(Ball.)* Let $\varphi$ be arbitrary and $K>|z_*|$. If $|\varepsilon|\,\|\rho\|_\infty\max_{|S(z)|\le C_K}|\varphi'|\le\frac12$, where $C_K=\max_{|z|\le K}|S|$, then along every perturbed object with $\sup|z|\le K$ the function $\mathrm{Re}\,S(z(t))$ is nonincreasing. It is strictly decreasing unless $z$ is constant.
2. *(Quadratic, global.)* Let $\varphi=\alpha y+\frac12\beta y^2$ and $(\varepsilon\|\rho\|_\infty\alpha)^2\le\frac12$. Then along *every* bounded perturbed object:
   * $1-\varepsilon\rho\beta y_2\ge\frac12$;
   * $y_1=\mathrm{Re}\,S(z)$ is nonincreasing, and strictly decreasing unless $z$ is constant;
   * $y_1\in[S_*,0]$;
   * $|y_2|\le 2|\varepsilon|\|\rho\|_\infty\int_{S_*}^0|\alpha+\beta s|\,ds$.
3. In case 2, and in case 1 for objects in the ball, there is $K_0$, independent of $\varepsilon$ in the stated range and of the object, with $\sup|z|\le K_0$ and $\int|z'|^2\le4P$.

*Proof.* (1) By Lemma 3.2, $y_1'=-\mathrm{Re}(1+\varepsilon\rho\overline{\Phi'(y)})|\partial S|^2\le-\frac12|\partial S|^2$. If $y_1$ is constant on an interval, then $\partial S(z)=0$ there and $z$ is constant.

(2) By Lemma 3.2 (verify.py 4.5), $\frac d{dt}(\varepsilon\beta y_2)=\varepsilon^2\rho\beta^2(y_1-y_0)|\partial S|^2$, with $y_0=-\alpha/\beta$ when $\beta\ne0$; if $\beta=0$ the first claim is trivial. Let $t^*$ be the supremum of the times up to which $\varepsilon\rho\beta y_2\le\frac12$ holds. On $(-\infty,t^*)$ we have $|\partial S|^2\le-2y_1'$, and $y_1$ is nonincreasing from $y_1(-\infty)\in\{0,S_*\}$. Hence
$$\varepsilon\beta y_2(t)\le2\varepsilon^2\|\rho\|_\infty\beta^2\int_{y_1(t)}^{y_1(-\infty)}\max(s-y_0,0)\,ds\le\varepsilon^2\|\rho\|_\infty\beta^2y_0^2=\varepsilon^2\|\rho\|_\infty\alpha^2,$$
using $y_1(-\infty)\le0$ and $\int_{y_0}^0(s-y_0)\,ds=y_0^2/2$ (verify.py 4.6). The integral vanishes if $y_0\ge0$. So $\varepsilon\rho\beta y_2\le(\varepsilon\|\rho\|_\infty\alpha)^2\le\frac12$ on $(-\infty,t^*)$. By continuity $t^*=\infty$, which proves the first claim; the second follows as in (1). The bound does not depend on how far $y_1$ travels. Monotonicity and the limits $y_1(\pm\infty)\in\{0,S_*\}$ give $y_1\in[S_*,0]$. Integrating $y_2'$ against $-2y_1'\ge|\partial S|^2$ gives the bound on $y_2$.

(3) $\int|\partial S|^2\le2(y_1(-\infty)-y_1(+\infty))\le P$. Moreover $\frac12|\partial S|\le|z'|=|1+\varepsilon\rho\overline{\Phi'}||\partial S|\le2|\partial S|$ for $\varepsilon$ small, since $y$ is bounded. Hence $\int|z'|^2\le4P$. With (R4) and $R_1=\max(R_0,|z_*|+1)$, the argument of [M50, Prop. 4.2] applies: on an excursion of $|z|$ from $R_1$ to $R_2$ we get $4P\ge\frac{mR_1}{24}(R_2-R_1)$. So $K_0=R_1+96P/(mR_1)$. ∎

**Corollary 7.2 (sectors).** Under Lemma 7.1, every nonconstant perturbed object has $y_1(-\infty)>y_1(+\infty)$, so it runs from $0$ to some $z_*^{(j)}$. The sectors $(p,p)$ contain only the constant $p$. There are no objects from $z_*^{(j)}$ to $z_*^{(k)}$ with $j\ne k$, nor from $z_*^{(j)}$ to $0$.

**Lemma 7.3 (compactness).** Let $\varepsilon_n\to0$, and let $z_n$ be perturbed objects from $0$ to $z_*$ satisfying the bounds of Lemma 7.1(3). Then
$$\inf_\theta\|z_n-\kappa(\cdot+\theta)\|_{H^1}\to0 .$$

*Proof.* Choose $t_n$ with $\mathrm{Re}\,S(z_n(t_n))=S_*/2$; this is possible by strict monotonicity. The functions $u_n=z_n(\cdot+t_n)$ are bounded in $C^1$, and their equations converge to the unperturbed one, uniformly on compacts. A subsequence converges in $C^1_{\rm loc}$ to a bounded unperturbed solution $u$ with $\mathrm{Re}\,S(u(0))=S_*/2$. By (R2) this is a kink $\kappa_k(\cdot+\theta)$.

On $[T,\infty)$ the energy satisfies $\int_T^\infty|\partial S(u_n)|^2\le2(\mathrm{Re}\,S(u_n(T))-S_*)$, which is small for $T$ and $n$ large. Since $|\partial S|\ge c_\eta>0$ on $\{|z|\le K_0\}$ minus the $\eta$-neighbourhood of $\mathrm{Crit}\,S$, a small energy forbids $u_n$ from leaving the $\eta$-neighbourhood of $\kappa_k(+\infty)$ after time $T$. As $u_n(+\infty)=z_*$, this forces $k=0$; similarly at $-\infty$.

Near a hyperbolic equilibrium of the perturbed equation (it is one, for all $t$, by Lemma 3.1), solutions that stay in a small neighbourhood on a half-line decay exponentially, at a rate and with constants that are uniform for small $\varepsilon$. This is the roughness of exponential dichotomies [Co, Pa]. The tails are therefore uniformly small in $H^1$. Combined with $C^1_{\rm loc}$ convergence, this gives $H^1$ convergence. ∎

**Proof of Theorem B.** By Lemma 7.1(1), Corollary 7.2 and Lemma 7.3, for small $\varepsilon$ every nonconstant object in the ball is $\delta'$-close to some $\mathcal K_j$. By $V_4$-symmetry take $j=0$. By Corollary 5.4, these objects correspond to the zeros of $B(\cdot,\varepsilon)$.

*Ends.* As $\tau\to-\infty$, $y\to0$ uniformly on $\mathrm{supp}\,\rho_\tau$. So there is $T$ with $|\varphi'(y)-\varphi'(0)|\le\frac12|\varphi'(0)|$ there for $\tau\le-T$, and likewise at $+\infty$ with $\varphi'(S_*)$. Lemma 3.5 then gives
$$|F'(\tau)|\ge c_0E(\tau)^2\quad\text{for }|\tau|\ge T,\qquad c_0=\tfrac12\min(|\varphi'(0)|,|\varphi'(S_*)|).$$
By Proposition 5.2, $|B|\ge\|\kappa'\|^{-1}|\varepsilon|E^2(c_0-C_2\|\kappa'\||\varepsilon|)>0$ for $|\tau|\ge T$ and $|\varepsilon|<c_0/(C_2\|\kappa'\|)$. So there are no zeros near the ends.

*Middle.* On $[-T,T]$, $-\|\kappa'\|B/\varepsilon\to F'$ in $C^1$ as $\varepsilon\to0$ (Proposition 5.2). Since the zeros of $F'$ are nondegenerate, $B(\cdot,\varepsilon)$ has exactly one zero near each $\tau_i$ and no others. This proves (1).

(2) is Proposition 6.1, and nondegeneracy follows from $F''(\tau_i)\ne0$. (3) is §6, together with $f'=-\varepsilon F'=\varepsilon\int\rho_\tau\varphi'(y)|\kappa'|^2$, whose sign near $\mp\infty$ is $\mathrm{sgn}(\varepsilon\varphi'(0))$, resp. $\mathrm{sgn}(\varepsilon\varphi'(S_*))$. The count is Lemma 2.2. ∎

## 8. The single-crossing lemma; proofs of Theorem C and Corollary E

**Lemma 8.1 (single crossing).** Let $\rho\ge0$ be smooth with support $[\alpha_\rho,\beta_\rho]$, positive and strictly log-concave on the open interval. Let $g\in C^0\cap L^1$ have exactly one sign change, at $t_0$, with $g\ne0$ a.e. Then
$$\mathcal G(\tau)=\int\rho(t-\tau)\,g(t)\,dt$$
has at most one zero, and every zero is transversal, with the same crossing direction.

*Proof.* Let $\ell=-(\log\rho)'$ on the open support interval. It is strictly increasing, and $\rho\ell=-\rho'$ is bounded. We have $\mathcal G'(\tau)=\int\rho(t-\tau)\ell(t-\tau)g(t)\,dt$.

Let $\mathcal G(\tau_1)=0$. If the window $\tau_1+(\alpha_\rho,\beta_\rho)$ did not contain $t_0$, then $g$ would have one sign on the window and $\mathcal G(\tau_1)\ne0$. So it contains $t_0$, and
$$\mathcal G'(\tau_1)=\int\rho(t-\tau_1)\big[\ell(t-\tau_1)-\ell(t_0-\tau_1)\big]g(t)\,dt .$$
The bracket has the sign of $t-t_0$. Say $g$ has the sign of $\pm(t-t_0)$. Then the integrand has the constant sign $\pm$ and is nonzero on a set of positive measure, so $\pm\mathcal G'(\tau_1)>0$ at every zero. A $C^1$ function whose zeros are all transversal in the same direction has at most one zero. ∎

This is a strict form of the variation-diminishing property of $TP_2$ kernels [Ka]. The bimodal control in verify.py 7.4 and §10 shows that log-concavity cannot be dropped.

The standard bump $e^{-1/(1-t^2)}$ satisfies $(\log\rho)''=-(2+6t^2)/(1-t^2)^3<0$ (verify.py 7.1).

**Proof of Theorem C.** By Lemma 7.1(2)–(3), all bounded objects satisfy the hypotheses of the compactness Lemma 7.3 without any ball restriction. The proof of Theorem B then applies to all objects.

*(1)* If $\varphi'$ has no zero on $[S_*,0]$, then $|\varphi'|\ge c>0$ there, and $|F'(\tau)|\ge cE(\tau)^2$ for *all* $\tau$. So $B\ne0$ everywhere for small $\varepsilon$, and there are no kinks.

*(2)* Here $\varphi'(y(t))$ has exactly one sign change in $t$, at $y^{-1}(y_0)$, since $y$ is strictly monotone. Apply Lemma 8.1 to $g=\varphi'(y)|\kappa'|^2$, so that $F'=-\mathcal G$. The function $F'$ has opposite signs near the two ends, namely $-\mathrm{sgn}\,\varphi'(0)$ and $-\mathrm{sgn}\,\varphi'(S_*)$. Hence $F$ has exactly one critical point $\tau_0$, and it is nondegenerate. It is a minimum iff $\varphi'(0)>0>\varphi'(S_*)$, i.e. iff $\beta>0$.

So for small $\varepsilon$ there is exactly one kink per $j$. Its small eigenvalue $2\varepsilon F''(\tau_0)/P+O(\varepsilon^2)$ has the sign of $\varepsilon\beta$, and $\mathrm{gr}=d_\kappa+[\varepsilon\beta>0]$ (verify.py 8.3–8.4).

*(3)* By Corollary 7.2, every asymptotic sector contains at most one object. Apply Proposition 3.7 and Lemma 2.1. ∎

**Proof of Corollary E.** Theorem A gives the first item. For $\varphi(y)=\frac12(y+P/4)^2$ we have $\alpha=P/4$, $\beta=1$ and $y_0=-P/4\in(S_*,0)$, so Theorem C(2) applies. The sign rule then gives $d_\kappa+1$ for $\varepsilon>0$ and $d_\kappa$ for $\varepsilon<0$. ∎

## 9. Klein-real perturbations (proof of Proposition D)

Let $S^\varepsilon_t=S+\varepsilon\rho(t)\psi(S)$ with $\psi$ real. This perturbation is $\sigma$-real (Lemma 3.1(3)), so $\Sigma$ is invariant. For $t\ll0$ the equation is unperturbed, so a kink $0\to z_*$ lies in $W^u(0)\subset\Sigma$ there [M50, Lemma 5.1]. By invariance it lies in $\Sigma$ for all $t$.

On $\Sigma$, $\nabla\mathrm{Re}\,S^\varepsilon_t=(1+\varepsilon\rho\psi'(S))\nabla\mathrm{Re}\,S$ (verify.py 6.1–6.2), with $S$ real. So the velocity of $z$ is everywhere a real multiple of the unperturbed field $-\nabla\mathrm{Re}\,S$, which does not vanish off $\mathrm{Crit}\,S$. Hence the trace of $z$ stays in the unperturbed orbit $\mathcal O$ through $z(t_1)$, for any $t_1\ll0$.

This orbit lies in $W^u(0)$, and its closure contains $z(+\infty)=z_*$. By (R2), $\mathcal O$ is the trace of $\kappa$. Along that trace $y=S\in(S_*,0)$, so the factor $1+\varepsilon\rho\psi'(y)$ is positive by the hypothesis on $\varepsilon$, and $z$ moves monotonically along $\mathcal O$. Therefore $z=\kappa\circ\vartheta$ with $\vartheta'=1+\varepsilon\rho\psi'(y(\vartheta))$ (verify.py 6.3).

This scalar equation has a unique global solution for each value of $\lim_{t\to-\infty}(\vartheta(t)-t)\in\mathbb R$. These solutions are distinct, and $\vartheta(t)-t$ converges at $+\infty$ as well. So the kinks form a line with the same ends.

Every such kink lies in $\Sigma$, where $C\cdot A_t=0$ and $\mathrm{Im}\,S^\varepsilon_t=\varepsilon\rho\,\mathrm{Im}\,\psi(S)=0$. So all of them have action $0$, and Proposition 3.7 excludes morphisms among them. ∎

So within the $\sigma$-real class the non-compact line, and with it the choice of how to treat its ends, persists exactly. Breaking it requires the imaginary part of $\Phi$. For $\Phi=\psi+i\varphi$, the reduced function involves only $\varphi$.

## 10. Numerical illustration (not used in any proof)

Take $a=b=1$, so $P=2$ and $S_*=-1$. Compute $\kappa$ by the backward slice flow along the Perron direction [M50, Prop. 6.2]; numerically $\|\kappa'\|^2=1.0000$. Solve the perturbed object equation on $[-11,11]$ by collocation, with linear boundary conditions on the unstable subspace at $0$ and the stable subspace at $z_*$ (verify.py §10).

* *$\varphi=\frac12(y+P/4)^2$, standard bump.* $F'$ has exactly one zero $\tau_0\approx0.0203$, with $F''(\tau_0)\approx0.059>0$. For $\varepsilon=\pm0.02$ and $\pm0.05$ the solver finds a kink at $\kappa(\cdot+\tau_0)$ (located to grid accuracy $<2\cdot10^{-3}$). Its action equals $\varepsilon F(\tau_0)$ to relative accuracy $10^{-5}$, and the error is quadratic in $\varepsilon$. The Rayleigh quotient $\langle z',\mathcal H_zz'\rangle$ of Lemma 3.4 agrees with $\varepsilon F''(\tau_0)$ to within $2\%$.
* *Bimodal $\rho=$ bump$(t-3)+$bump$(t+3)$, which is not log-concave.* $F$ has three critical points (min, max, min). The solver finds three kinks at the predicted places, with actions $\varepsilon F(\tau_i)$. This illustrates Theorem B with $N=3$, and it shows that Lemma 8.1 needs log-concavity.
* *$\varphi(y)=y$.* From every initial guess the solver drifts to the boundary of the interval and finds no interior kink, consistent with Theorem A.

## 11. Status of the claims and limitations

| Claim | Status |
|---|---|
| Identities of §3 (vacua, $S$-image, flux, Hessian identity, action $\varepsilon F$) | proved; symbolic checks in verify.py §§1–4 |
| Theorem A (phase rotation: no kinks, all $\varepsilon\ne0$; constants nondegenerate) | proved |
| Uniform reduction with $E^2$-weighted remainder (Props. 5.1–5.2) | proved |
| Theorem B (objects in a ball ↔ crit $F$; small eigenvalue; action; gradings; end types) | proved, for objects with $\sup\lvert z\rvert\le K$ |
| Theorem C (quadratic $\varphi$: global; $0$ or $1$ kink; realization) | proved, in the class $\mathfrak M_\varepsilon$ |
| Proposition D ($\sigma$-real perturbations keep the line) | proved |
| Morphisms between distinct kinks when $N\ge2$ | **not determined** (gluing) |
| Absolute gradings $d_\kappa$, $d_p$ | normalizations, not derived |

**Limitations.**
1. The perturbation (1.1) acts on the reduced equations. We do not show that it comes from a deformation of the metric or of the HW equations on $\mathbb R\times Y_4$.
2. Morphisms are treated in the decay class $\mathfrak M_\varepsilon$, as in [M50]. We do not prove that finite-energy solutions lie in it.
3. Theorem B is local: it classifies objects in a fixed ball. Global bounds are proved only for quadratic $\varphi$ (Lemma 7.1(2)).
4. For $N\ge2$, matching the morphism spaces with the cascade model would require adiabatic gluing along the line. We do not do this.

**Verification.** `verify.py` (Python 3, sympy, numpy, scipy, mpmath) runs 62 checks and ends with `FALLOS = 0` (`verify_output.txt`). Sections 1–9 are exact symbolic or combinatorial checks, with negative controls in 1.6, 1.8–1.9, 2.5, 3.4, 5.6 and 7.4. Section 10 is the numerical illustration of §10 and is not used in any proof. `verify.mpl` mirrors the exact checks of sections 1–9 in Maple; it has been executed in Maple: 40 checks, FALLOS = 0 (output in `verify_mpl_output.txt`).

## Appendix A. Corrections to the first version, and what is recalled from it

The first version built the paper around the complete $SU(2)\times SU(2)$ Klein category $\mathcal F_D$ of math_49 and its Abouzaid–Blumberg realization. Its contractibility for every coherent framing is **math_49, Theorem D(4)** [M49]; see also [M52, §2.3, Rem. 2.2] and [M53, Thm. A(1)]. We recall it here and claim nothing new about it. The referee's two local corrections are recorded for completeness.

1. *Endpoint framings.* On the compactified interval $\overline{\mathcal M}(k_{++},k_{--})\cong[-1,1]$, with coordinate $u=\tanh T$, the field $\partial_T=(1-u^2)\partial_u$ vanishes at the endpoints. The endpoint framing argument must use the nonvanishing field $\partial_u$, which has the same interior orientation. With $\partial_u$, the inward normals are $+\partial_u$ at $u=-1$ and $-\partial_u$ at $u=+1$, and the determinant computation of the first version is unchanged.
2. *Conditional homology.* For the conditional product complex with signed count $n$, the homology is $\mathbb Z/n$ in degrees $0$ and $1$ only when $n\ne0$. For $n=0$ it is $\mathbb Z$, $\mathbb Z^2$, $\mathbb Z$ in degrees $0,1,2$.
3. *Scope.* The spectral symmetry $d\sigma\,\mathcal H_x\,d\sigma=-\mathcal H_x$ of the unperturbed objects does not by itself define an $\eta$-invariant on the non-compact line. The normalization $d\equiv0$ was a convention. Neither is used here. The perturbed kinks break $\sigma$, and their Hessians acquire a small eigenvalue $2\varepsilon F''/P$ of definite sign (Proposition 6.1).

## References

[AB] M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: flow categories*, arXiv:2404.03193.

[Bo] A. Bonciocat, *Revisiting the Cohen–Jones–Segal construction in Morse–Bott theory*, arXiv:2409.11278.

[Co] W. A. Coppel, *Dichotomies in Stability Theory*, Lecture Notes in Math. 629, Springer, 1978.

[GMW] D. Gaiotto, G. Moore, E. Witten, *Algebra of the infrared: string field theoretic structures in massive $\mathcal N=(2,2)$ field theory in two dimensions*, arXiv:1506.04087.

[Ka] S. Karlin, *Total Positivity*, Vol. I, Stanford Univ. Press, 1968.

[Mel] V. K. Melnikov, *On the stability of the center for time-periodic perturbations*, Trans. Moscow Math. Soc. 12 (1963), 1–57.

[Pa] K. J. Palmer, *Exponential dichotomies and transversal homoclinic points*, J. Differential Equations 55 (1984), 225–256.

[RS] J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.

[M48] rStation math_48 v1, *Weighted cross-section indices for the linearized Haydys–Witten operator at the corrected-Nahm-pole Kapustin–Witten objects on $\mathrm{Sol}^3\times\mathbb R_+$ (diagonal ansatz)*, https://rstation.ai/problems/math/papers/48/v1.

[M49] rStation math_49 v1, *Global rigidity of the Klein-symmetric Haydys–Witten sector on the round three-sphere, and the complete $SU(2)\times SU(2)$ flow category at the Anderson–Henningson fold*, https://rstation.ai/problems/math/papers/49/v1.

[M50] rStation math_50 v1, *The Haydys–Witten kink on $\mathrm{Sol}^4$: existence, uniqueness and transversality of the unique $\zeta$-soliton, classification of objects, and absence of morphisms in the $\mathbb R^3\rtimes V_4$ sector*, https://rstation.ai/problems/math/papers/50/v1.

[M52] rStation math_52 v1, *Decoupled framed flow categories and Steenrod squares beyond homology*, https://rstation.ai/problems/math/papers/52/v1.

[M53] rStation math_53 v1, *Spherical reframings of the symmetric Haydys–Witten flow categories at the Anderson–Henningson fold*, https://rstation.ai/problems/math/papers/53/v1.

[M56] rStation math_56 v1, *Breaking the Klein symmetry of the Haydys–Witten kink on $\mathrm{Sol}^4$: exact gauged reduction to a $\zeta$-instanton equation, Gram-matrix rigidity, uniqueness of the soliton and transversality*, https://rstation.ai/problems/math/papers/56/v1.

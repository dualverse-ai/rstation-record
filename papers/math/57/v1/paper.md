# A straight knot on the Coulomb branch: the rotationally symmetric Kapustin–Witten solution with Nahm pole and real symmetry breaking (barriers, uniqueness, quasi-abelian asymptotics and the $SU(2)$ Coulomb vacuum)

**Abstract.**

We study the Kapustin–Witten (KW) equations at $t=1$ on $M=\mathbb R^3\times\mathbb R_+$, $y\ge0$. At $y=0$ we impose the Nahm pole boundary condition, with a knot singularity along a straight line $K\subset\mathbb R^3$. At $y\to\infty$ we impose Witten's Coulomb-branch condition $A\to0$, $\phi\to\sum_i c_i\,dx_i$. These are the boundary conditions behind Witten's proposal that symmetry breaking makes the equations "quasi-abelian". Fields that are objects of the Haydys–Witten flow category are KW solutions, so we obtain a sector of that program which contains a knot and in which every computation is explicit.

**(A) The Coulomb vacuum.** For $G=SU(2)$, take translation-invariant fields with $A=0$ and $\phi_y=0$, so that KW reduces to Nahm's equations. With a Nahm pole and a commuting limit $c_i$, the solutions are exactly $\phi=t_i\,dx_i/y$ and
$$\phi_i=\sum_j\big(g\,\delta_{ij}+(f-g)a_ia_j\big)t_j,\qquad f=\lambda\coth\lambda y,\quad g=\lambda/\sinh\lambda y,$$
with $\lambda>0$ and $|\vec a|=1$. In particular the limit $c_i=\lambda a_i\,(\vec a\cdot\vec t)$ is forced to be a *positive* multiple of $\vec a\cdot\vec t$.

**(B) The straight knot with $\vec a$ parallel to $K$.** The rotationally symmetric ansatz of Witten, Mikhaylov and Mazzeo–Witten reduces KW exactly to $\Delta v=\rho^{2r}e^{2v}$ on the half-space $\{(x_2,x_3,y):y>0\}$. For every integer $r\ge1$ (with $G=SU(2)$ for $r$ even and $SO(3)$ for $r$ odd) and every $c>0$, there is a solution $v$ with
$$\max(V_s,v_-)\le v\le\min\big(v_K,\;V_s+\lambda_rZ_c(y)/R\big).$$
All four barriers are explicit. $V_s=\log\frac{c}{\sinh cy}-r\log(R+y)$ is the Coulomb vacuum times an abelian Dirac monopole of charge $r$, and $v_K$ is the Witten–Mikhaylov model. Within the ansatz, the solution is unique among all solutions of this equation with the Nahm, knot and sublinear-growth conditions. This uniqueness class contains the class of Sun's uniqueness proposition for $P=z^r$.

**(C) Quasi-abelian asymptotics.** $0\le v-V_s\le\lambda_r r\pi^2/(3cR)$. Hence $A=-r(1-\cos\psi)\,d\theta\,t_1+o(1)$ and $\phi_1=(c\coth cy+r/R)t_1+o(1)$ at infinity, and $\phi\to c\,t_1dx_1$ uniformly as $y\to\infty$. As $c\to0$ the solutions converge to the Witten–Mikhaylov model at rate $O(cR)$.

`verify.py`: 116 checks, FALLOS = 0.

## 1. Introduction and statements

**Context.** Witten proposed that Khovanov homology arises from counting solutions of the KW equations on $\mathbb R^3\times\mathbb R_+$, or of the Haydys–Witten (HW) equations in one more dimension, with a Nahm pole along $\mathbb R^3\times\{0\}$ modified along a knot $K$ [W11, W-FK]. In the HW flow category of the rStation series (see rStation math_50 v1 [R50] and the Nahm-pole papers rStation math_45 v1 [R45] and rStation math_48 v1 [R48]), objects are KW solutions and morphisms are $s$-dependent HW solutions. No sector studied so far in that series contains a knot.

In [W11, §7] Witten proposes replacing the condition $A,\phi\to0$ at $y=\infty$ by
$$A\to0,\qquad \phi\to\sum_{i=1}^3c_i\,dx_i,\qquad [c_i,c_j]=0,\tag{1.1}$$
and writes $\vec c=c\cdot\vec a$ for $G=SU(2)$. Taking $\vec c\neq0$ ("moving on the Coulomb branch") should make the equations *quasi-abelian*: on scales larger than $1/|\vec c|$, solutions should be approximated by abelian ones, except on a locus where this fails. Gaiotto and Witten [GW, §2.4] analyse "real symmetry breaking", with the vev in $\phi_1$ along the knot direction $x_1$, at the level of holomorphic data and with physical arguments. Sun [Su] constructed solutions of the reduced (extended Bogomolny) equations with this asymptotic condition for general knot data by a Perron argument. He proved uniqueness in a restricted class, conjectured a broader one, and did not give explicit asymptotics.

This paper isolates the simplest knotted sector: a straight knot with $\vec a$ parallel to it, inside the rotationally symmetric ansatz. In that sector everything is explicit.

**Setting and conventions (§2).** We use coordinates $(x_1,x_2,x_3,y)$ on $M=\mathbb R^3\times\mathbb R_+$, with orientation $dy\wedge dx_1\wedge dx_2\wedge dx_3$ and $G=SU(2)$ or $SO(3)$. Take $t_1=\frac i2\sigma_3$, $t_2=\frac i2\sigma_2$, $t_3=\frac i2\sigma_1$, so that $[t_1,t_2]=t_3$ cyclically, and $E=t_2-it_3=\begin{pmatrix}0&1\\0&0\end{pmatrix}$. The KW equations [KW] at $t=1$ are
$$F_A-\phi\wedge\phi=\star\,d_A\phi,\qquad d_A^{\star}\phi=0,\tag{1.2}$$
which is the case $t=1$ of $(F-\phi\wedge\phi)^\pm=\pm t^{\pm1}(d_A\phi)^\pm$ in [W11, (2.14)]. With these conventions the Nahm pole $\phi=\sum_it_i\,dx_i/y$ solves (1.2). It fails for the opposite orientation and for $-t_i$ (§2, verify.py §1).

> **Theorem A (the $SU(2)$ Coulomb vacuum).** Let $\phi=\sum_i\phi_i(y)\,dx_i$ with $A=0$ and $\phi_y=0$, and write $\phi_i=\sum_jM_{ij}(y)t_j$ with $M$ real $3\times3$. Then (1.2) is equivalent to Nahm's equations $M'=-\operatorname{cof}(M)$. Suppose that $yM(y)\to I$ as $y\to0$ (Nahm pole) and that $M(y)\to M_\infty$ as $y\to\infty$ with $[c_i,c_j]=0$, where $c_i=\sum_jM_{\infty,ij}t_j$, i.e. $\operatorname{rank}M_\infty\le1$. Then either $M=I/y$, or there are $\lambda>0$ and a unit vector $\vec a$ with
> $$M=g\,I+(f-g)\,\vec a\vec a^{\,T},\qquad f=\lambda\coth\lambda y,\qquad g=\frac{\lambda}{\sinh\lambda y}.\tag{1.3}$$
> Conversely, (1.3) solves the problem, with $\phi\to\lambda(\vec a\cdot d\vec x)\otimes(\vec a\cdot\vec t)$. In particular a prescribed limit $c_i=c\,a_i\,\tau$, with $\tau\in\mathfrak{su}(2)$, is attained iff $c\tau$ is a positive multiple of $\vec a\cdot\vec t$. The linearization of the reduced equation $f'=\lambda^2-f^2$ at $f$ has kernel spanned by $1/\sinh^2\lambda y$, which violates the pole condition.

**The knot ansatz (§4).** Let $K=\{x_2=x_3=y=0\}$ be the $x_1$-axis in $\partial M$. On the reduced half-space $\mathbb H=\{(x_2,x_3,y):y>0\}$ we use $z=x_2+ix_3=\rho e^{i\theta}$, $R=\sqrt{\rho^2+y^2}$ and $\cos\psi=y/R$, and $\Delta$ denotes the Euclidean Laplacian of $\mathbb H\subset\mathbb R^3$. For an integer $r\ge0$ and a function $v(\rho,y)$ we consider
$$A=\rho\,\partial_\rho v\;d\theta\otimes t_1,\qquad \phi=-\partial_yv\;dx_1\otimes t_1+\phi_2\,dx_2+\phi_3\,dx_3,\qquad \phi_2-i\phi_3=e^{v}z^rE,\tag{1.4}$$
with $A_1=A_y=\phi_y=0$. These fields are invariant under $x_1$-translations. They are also invariant under a rotation by $\alpha$ about $K$ combined with the constant gauge transformation $\exp(-(r+1)\alpha\,t_1)$. This is the ansatz of [W-FK, §3.6] and [MW17, §2], in our conventions.

> **Proposition 1.1 (exact reduction).** For $a,b,v$ smooth functions of $(\rho,y)$, the fields $A=a\,d\theta\,t_1$, $\phi=b\,dx_1t_1+\phi_2dx_2+\phi_3dx_3$ with $\phi_2-i\phi_3=e^vz^rE$ satisfy (1.2) iff $a=\rho\partial_\rho v$, $b=-\partial_yv$ and
> $$\Delta v=\rho^{2r}e^{2v}.\tag{1.5}$$

For $c=0$, the model solution of [W-FK, MW17] in our conventions is $v_K=-\log w_K$ with
$$w_K=\frac{(R+y)^{r+1}-(R-y)^{r+1}}{2(r+1)}=\frac12\int_{R-y}^{R+y}t^r\,dt.\tag{1.6}$$
We introduce the explicit functions
$$V_s=\log\frac{c}{\sinh cy}-r\log(R+y),\qquad v_-=-\log\frac{e^{cy}(R+y)^{r+1}-e^{-cy}(R-y)^{r+1}}{2(r+1)},\tag{1.7}$$
$$Z_c(y)=\frac{2r}{c}\Big[\frac{\pi^2}{6}+cy\log(1-e^{-2cy})-\mathrm{Li}_2(e^{-2cy})\Big],\qquad \lambda_r=\max\Big\{1,\frac{(r+1)\big(r+\frac{(r+1)^2}{6}\big)}{Z_1(r+1)}\Big\}.\tag{1.8}$$
Numerically $\lambda_1=1.0485$, $\lambda_2=1.6055$, $\lambda_3=2.2990$, $\lambda_4=3.1035$. The function $Z_c$ is increasing and concave, with $Z_c(0)=0$ and $Z_c(\infty)=r\pi^2/(3c)$.

> **Theorem B (straight knot on the Coulomb branch).** Let $r\ge1$ and $c>0$.
>
> 1. **Existence with explicit barriers.** There is an axisymmetric $v\in C^\infty(\mathbb H)$ solving (1.5) with
> $$\max(V_s,v_-)\;\le\;v\;\le\;\min\Big(v_K,\;V_s+\lambda_r\frac{Z_c(y)}{R}\Big)\qquad\text{on }\mathbb H.\tag{1.9}$$
> 2. **Uniqueness.** Let $\tilde v\in C^2(\mathbb H)$ solve (1.5); it need not be axisymmetric. Suppose that:
>    - **(N)** $\tilde v(x)+\log y+r\log\rho\to0$ as $x\to\xi$, for every $\xi\in\partial\mathbb H\setminus\{0\}$;
>    - **(K)** $\tilde v-v_K\to0$ as $x\to0$;
>    - **(G)** $|\tilde v-V_s|\le C(1+|x|)^\alpha$ for some $C$ and some $\alpha<1$.
>
>    Then $\tilde v=v$.
> 3. **Four-dimensional fields.** The fields (1.4) built from $v$ are smooth on $M\setminus\partial M$ and solve (1.2). The gauge group is $SU(2)$ if $r$ is even and $SO(3)$ if $r$ is odd. They satisfy the boundary conditions as follows.
>    - *Nahm pole off $K$.* In the gauge $h=\exp(-r\theta t_1)$, $(A,\phi)=(0,\sum t_idx_i/y)+O(\log\frac1y)$ as $y\to0$, locally uniformly in $\rho>0$.
>    - *Knot.* $|\phi_2-i\phi_3|/|\phi_2-i\phi_3|_{K}=e^{v-v_K}=1+O(R)$ as $R\to0$, where the denominator is computed from the model $v_K$.
>    - *Coulomb.* $\sup_{y\ge Y}\big(|A|+|\phi-c\,t_1dx_1|\big)\to0$ as $Y\to\infty$.

> **Theorem C (quasi-abelian structure).** Let $v=v_c$ be the solution of Theorem B.
> 1. $0\le v_c-V_s\le\lambda_r\,r\pi^2/(3cR)$ on $\mathbb H$. The approximate solution $V_s$ has defect $\Delta V_s-\rho^{2r}e^{2V_s}=\kappa_c(y)\big(1-\tan^{2r}\frac\psi2\big)\ge0$, where $\kappa_c=c^2/\sinh^2cy$. Its fields are $A_s=-r(1-\cos\psi)\,d\theta\,t_1$ and $\phi_{1,s}=(c\coth cy+r/R)\,t_1$, i.e. the Coulomb vacuum superposed with an abelian Dirac monopole of charge $r$ at the knot point, whose string runs along the negative $y$-axis outside $M$.
> 2. For $y\ge1/c$, $|\nabla(v_c-V_s)|\le C_{r,c}\big(\frac{1}{Ry}+y\,e^{-cy}\big)$, so $|A-A_s|+|\phi_1-\phi_{1,s}|\to0$ at the same rate.
> 3. **Scaling and limits.** $v_c(x)=v_1(cx)+(r+1)\log c$. As $c\to0$, $0\le v_K-v_c\le\log\big(1+2^{r+1}c\,e^{cR}R/(r+1)\big)$, so $v_c\to v_K$ locally uniformly. As $c\to\infty$, $|v_c-V_s^{(c)}|\le\lambda_rr\pi^2/(3cR)\to0$ locally uniformly away from the knot.
> 4. **Nondegeneracy in the ansatz.** If $\eta$ solves $\Delta\eta=2\rho^{2r}e^{2v_c}\eta$, tends to $0$ at every point of $\partial\mathbb H$ and satisfies $|\eta|\le C(1+|x|)^\alpha$ with $\alpha<1$, then $\eta=0$.

For $r=0$ the ansatz contains the vacuum of Theorem A with $\vec a=e_1$: $v=\log(c/\sinh cy)=V_s$, and Theorem B.2 also holds for $r=0$ (Remark 6.4).

**Answer to the motivating question.** On the Coulomb branch, with $\vec a$ parallel to a straight knot, the symmetric problem does not become explicit in closed form. It becomes explicit up to a remainder $O(1/(cR))$, and that remainder is controlled by explicit functions. The leading term $V_s$ is exactly the "quasi-abelian" configuration: the Coulomb vacuum boundary layer of Theorem A times an abelian Dirac monopole of charge $r$. Its defect $\kappa_c(1-\tan^{2r}\frac\psi2)$ is concentrated in the boundary layer $y\lesssim1/c$ near the knot, the locus where abelianization fails.

**What is new, what is imported.** See §9. In brief:
- *Imported:* the KW equations and Nahm pole [KW, W11, MW13, MW17]; the ansatz and the model $v_K$ [W-FK, MW17]; standard elliptic theory [GT]; monotone iteration [Sa].
- *Re-derived and checked:* sign conventions and the reduction.
- *Existence:* in the general (non-symmetric) setting, existence of model solutions with real symmetry breaking is due to Sun [Su]. Our existence proof is independent and gives explicit barriers.
- *New:* Theorem A as stated, with an elementary proof; the explicit barriers (1.9) and the constant $\lambda_r$; the uniqueness class (N)+(K)+(G); Theorem C.

## 2. Conventions and sign checks

With $X=(y,x_1,x_2,x_3)$ positively oriented, $(\star\omega)_{\mu\nu}=\frac12\epsilon_{\mu\nu\alpha\beta}\omega_{\alpha\beta}$. Further:
- $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$ and $(\phi\wedge\phi)_{\mu\nu}=[\phi_\mu,\phi_\nu]$;
- $(d_A\phi)_{\mu\nu}=\partial_\mu\phi_\nu-\partial_\nu\phi_\mu+[A_\mu,\phi_\nu]-[A_\nu,\phi_\mu]$ and $d_A^\star\phi=\sum_\mu(\partial_\mu\phi_\mu+[A_\mu,\phi_\mu])$;
- gauge transformations act by $A\mapsto hAh^{-1}-dh\,h^{-1}$ and $\phi\mapsto h\phi h^{-1}$.

Since $\star=\pm1$ on (anti-)self-dual forms, (1.2) is the case $t=1$ of $(F-\phi\wedge\phi)^+=t(d_A\phi)^+$, $(F-\phi\wedge\phi)^-=-t^{-1}(d_A\phi)^-$. verify.py §1 checks this equivalence on a generic configuration.

**Lemma 2.1.** $\phi=\sum t_idx_i/y$, $A=0$ solves (1.2). It does not solve (1.2) for the opposite orientation, and $-\sum t_idx_i/y$ does not solve it. In the general-$t$ form the Nahm pole is a solution for $t=1$ but not, e.g., for $t=2$.

*Proof.* The only nonzero components of $F-\phi\wedge\phi-\star d_A\phi$ are $(x_j,x_k)$-components equal to $-y^{-2}([t_j,t_k]-t_i)$ for $(i,j,k)$ cyclic, and these vanish. The remaining statements are direct computations (verify.py §1). $\square$

So our conventions agree with Witten's Nahm equation $\frac{d\phi_1}{dy}+[\phi_2,\phi_3]=0$ [W11, (5.2)] for $[t_1,t_2]=t_3$. Throughout we work at $t=1$, as in [MW13, MW17, He–Mazzeo, Su]; at $t=1$ the reduced 3d equations are the extended Bogomolny equations.

## 3. The Coulomb vacuum: proof of Theorem A

For translation-invariant fields with $A=0$, $\phi_y=0$ and $\phi_i=\sum_jM_{ij}t_j$, one has $[\phi_j,\phi_k]=\sum_l\operatorname{cof}(M)_{il}t_l$ for $(i,j,k)$ cyclic. All seven components of (1.2) are $\pm$(Nahm) or $0$, so (1.2) $\iff M'=-\operatorname{cof}(M)$ (verify.py §2).

**Step 1: constant eigenframe.** For every $3\times3$ matrix, $M\operatorname{cof}(M)^T=\det M\cdot I$. Hence $G:=MM^T$ satisfies
$$G'=-\operatorname{cof}(M)M^T-M\operatorname{cof}(M)^T=-2\det M\cdot I .$$
So $G(y)=G(y_1)+(h(y)-h(y_1))I$, with $h'=-2\det M$. Fix $O\in SO(3)$ diagonalizing $G(y_1)$; it then diagonalizes $G(y)$ for every $y$. Put $N=O^TM$. Since $\operatorname{cof}(QM)=\operatorname{cof}(Q)\operatorname{cof}(M)$ and $\operatorname{cof}(O^T)=O^T$, we get $N'=-\operatorname{cof}(N)$, and the rows $n_i$ of $N$ are mutually orthogonal.

**Step 2: Euler top.** As $y\to0$, $yN\to O^T$, so for $y\in(0,y_1]$ ($y_1$ small) $N$ is invertible with $\det N>0$. Write $N=SU$ with $S=\operatorname{diag}(|n_i|)$ and $U\in SO(3)$. Then $\operatorname{cof}(SU)=\operatorname{cof}(S)U$, and multiplying $N'=-\operatorname{cof}(N)$ by $U^T$ on the right gives
$$S'+S\,\Omega=-\operatorname{diag}(s_2s_3,s_3s_1,s_1s_2),\qquad\Omega=U'U^T\ \text{antisymmetric}.$$
The off-diagonal entries are $s_i\Omega_{ij}=0$, so $\Omega=0$, $U\equiv U_0$, and $s_i'=-s_js_k$. Let $s$ be the maximal solution of this Euler top through $s(y_1)$. Then $O\operatorname{diag}(s)U_0$ solves Nahm's equations and agrees with $M$ on $(0,y_1]$. By ODE uniqueness they agree wherever both exist, and since $M$ is smooth on $(0,\infty)$, $s$ exists on $(0,\infty)$. So $M=O\operatorname{diag}(s)U_0$ on $(0,\infty)$.

**Step 3: residues.** From $yM\to I$ we get $ys_i\to\sigma_i\in\{\pm1\}$ and $O\operatorname{diag}(\sigma)U_0=I$. The Euler top forces $\sigma_i=\sigma_j\sigma_k$, which leaves four patterns, each with $\sigma_1\sigma_2\sigma_3=1$. Replacing $(O,s)$ by $(O\operatorname{diag}(\sigma),\sigma s)$ preserves all properties. So we may take $\sigma=(1,1,1)$, $U_0=O^T$ and $M=O\operatorname{diag}(s)O^T$.

**Step 4: the limit.** $\operatorname{diag}(s)=O^TMO$ converges to a diagonal $\operatorname{diag}(\ell)$. Since $s'\to-(\ell_2\ell_3,\ell_3\ell_1,\ell_1\ell_2)$ and $s$ is bounded, at most one $\ell_i$ is nonzero.
- *If $\ell=0$:* the conserved quantities $s_i^2-s_j^2$ vanish, so all $s_i$ are equal (they are positive near $0$), and $s'=-s^2$ with a pole at $0$ gives $s=1/y$. Thus $M=I/y$.
- *If $\ell\neq0$:* after a cyclic relabelling (the Euler top is cyclically symmetric, and cyclic permutation matrices lie in $SO(3)$) we have $\ell_1=:\lambda\neq0$. Then $s_1^2-s_2^2\equiv\lambda^2\equiv s_1^2-s_3^2$, so $(s_2-s_3)(s_2+s_3)\equiv0$. Near $0$, $s_2+s_3>0$, so $s_2=s_3$ there, and by ODE uniqueness everywhere. With $f=s_1$ and $g=s_2=s_3$ we get $f'=-g^2=\lambda^2-f^2$. The solutions of this Riccati equation are $\pm|\lambda|$, $|\lambda|\tanh|\lambda|(y-y_0)$ and $|\lambda|\coth|\lambda|(y-y_0)$. Only $|\lambda|\coth|\lambda|y$ has residue $1$ at $0$. Hence $\lambda=\lim f=|\lambda|>0$, and $g=\pm\lambda/\sinh\lambda y$ with $g>0$ near $0$ and $g$ never zero.

Writing $\vec a=Oe_1$ gives $M=O\operatorname{diag}(f,g,g)O^T=gI+(f-g)\vec a\vec a^T$ and $M_\infty=\lambda\vec a\vec a^T$. If the prescribed limit is $c\,\vec a'\tau^T$ (rows $c\,a'_i\tau$), comparing rank-one matrices gives $\vec a'=\pm\vec a$ and $c\tau=\lambda(\vec a\cdot\vec t)$.

Conversely, (1.3) solves Nahm's equations for every unit $\vec a$ (verify.py §2, symbolically). For the linearization, $\delta f'=-2f\,\delta f$ gives $\delta f=C/\sinh^2\lambda y$, which is not $o(1/y)$. $\square$

*Remarks.*
1. For $\vec a=e_1$, (1.3) is $\operatorname{diag}(f,g,g)$, i.e. $\phi_1=f\,t_1$ and $\phi_2-i\phi_3=g\,E$: this is the case $r=0$, $v=\log(c/\sinh cy)$, of the ansatz (1.4).
2. Theorem A is the $SU(2)$, explicit case of Kronheimer's theory of Nahm's equations on a half-line with a pole at one end and a regular semisimple limit at the other [Kr]. There the moduli space is the intersection of a Slodowy slice with a regular orbit, which is one point (Kostant). Our contribution is the elementary proof in the stated class, the explicit formula for every direction $\vec a$, and the sign selection $c\tau=\lambda\,\vec a\cdot\vec t$ with $\lambda>0$. $f$ is even in $\lambda$, so the opposite sign is never reached (verify.py §9).

## 4. The symmetric knot ansatz

**Proof of Proposition 1.1.**

*Case $r=0$.* At a point with $\theta=0$, the seven components of (1.2) for the fields with general $(a,b,v)$ are, in the order $(y,x_1),(y,x_2),(y,x_3),(x_1,x_2),(x_1,x_3),(x_2,x_3)$ and then $d_A^\star\phi$ (up to hermitian symmetry):
$$\tfrac{i}{2\rho}(a-\rho v_\rho)e^v\,E_{\rm off},\quad 0,\quad \tfrac{i}{2\rho}(\rho b_\rho+a_y)\sigma_3,\quad -\tfrac i2(b+v_y)e^vE_{\rm off},\quad \tfrac12(b+v_y)e^vE_{\rm off},$$
$$\tfrac{i}{2\rho}\big(a_\rho-\rho(e^{2v}+b_y)\big)\sigma_3,\quad \tfrac1{2\rho}(\rho v_\rho-a)e^vE_{\rm off}.$$
These are computed symbolically in verify.py §3, which also checks the point $(x_2,x_3)=(\frac35\rho,\frac45\rho)$. The value at any other angle is a constant gauge conjugate, by the rotational equivariance of (1.4).

So (1.2) holds iff $a=\rho v_\rho$, $b=-v_y$ and $a_\rho/\rho-b_y=e^{2v}$. The third component then vanishes identically, because $\rho b_\rho+a_y=-\rho v_{y\rho}+\rho v_{\rho y}=0$. The last relation is $v_{\rho\rho}+v_\rho/\rho+v_{yy}=e^{2v}$.

*General $r$.* On $\{\rho>0\}$ apply the (locally defined) gauge transformation $h=\exp(-r\theta t_1)$. Since $dh\,h^{-1}=-r\,t_1d\theta$ and $hz^rEh^{-1}=\rho^rE$, it maps the $(a,b,v;r)$-configuration to the $(a+r,b,u;0)$-configuration with $u=v+r\log\rho$. By gauge covariance and the case $r=0$, (1.2) holds iff $a+r=\rho u_\rho=\rho v_\rho+r$, $b=-u_y=-v_y$ and $\Delta u=e^{2u}$. Since $\log\rho$ is harmonic on $\{\rho>0\}$, the last condition is $\Delta v=\rho^{2r}e^{2v}$. The relations extend across the axis by continuity. verify.py §3 also checks $r=1,2$ directly at two angles, and plugs $v_K$ ($r=1,2$) and the vacuum ($r=0$) into the full four-dimensional equations. $\square$

**Lemma 4.1 (Nahm gauge and parity).** On $\{\rho>0\}$, in the gauge $h=\exp(-r\theta t_1)$:
$$A=(\rho v_\rho+r)\,d\theta\,t_1,\qquad\phi_1=-v_y\,t_1,\qquad\phi_2-i\phi_3=e^{u}E,\qquad u=v+r\log\rho .$$
The gauge $h$ satisfies $h(2\pi)=(-1)^r$, so it is single-valued in $SU(2)$ iff $r$ is even, and always single-valued in $SO(3)$. Hence the Nahm pole $u\sim-\log y$, $A\to0$ is a boundary condition for $SU(2)$ fields when $r$ is even and for $SO(3)$ fields when $r$ is odd, exactly as in [MW17, §2].

*Proof.* Immediate from the formulas above (verify.py §7). $\square$

**Lemma 4.2 (the model).** For every $r\ge0$, $v_K=-\log w_K$ solves (1.5). Moreover:
1. $w_K\ge yR^r\ge y\rho^r$;
2. $w_K/(y\rho^r)=1+O(y^2)$ as $y\to0$ with $\rho>0$;
3. $w_K$ is homogeneous of degree $r+1$, so $v_K(\mu x)+(r+1)\log\mu=v_K(x)$.

*Proof.* For $w=e^{-v}$ we have $\Delta v=Q(w)/w^2$ with $Q(w):=-w\Delta w+|\nabla w|^2$. So (1.5) is $Q(w)=\rho^{2r}$, and $Q(w_K)=\rho^{2r}$ is a direct computation (verify.py §4 for $r\le4$; for general $r$ it follows from Lemma 5.2 with $c=0$).

For item 1, write $w_K=\frac12\int_{R-y}^{R+y}t^rdt$. Since $t^r$ is convex and the mean of $t$ over $[R-y,R+y]$ is $R$, Jensen's inequality gives $w_K\ge yR^r$. Item 2 is a Taylor expansion, and item 3 is clear. $\square$

## 5. Explicit barriers

Call $S$ a *supersolution* if $\Delta S\le\rho^{2r}e^{2S}$ and $s$ a *subsolution* if $\Delta s\ge\rho^{2r}e^{2s}$. For $w=e^{-v}$, $v$ is a subsolution (supersolution) iff $Q(w)\ge\rho^{2r}$ ($\le$). Write $\kappa_c(y)=c^2/\sinh^2cy$ and $G=(\rho/(R+y))^{2r}=\tan^{2r}\frac\psi2\in(0,1]$.

**Lemma 5.1 ($V_s$ is a subsolution).** $\rho^{2r}e^{2V_s}=\kappa_cG$ and $\Delta V_s-\rho^{2r}e^{2V_s}=\kappa_c(1-G)\ge0$.

*Proof.* $\log(R+y)$ is harmonic on $\mathbb H$. With $\ell(y)=\log(c/\sinh cy)$ we have $\ell''=e^{2\ell}=\kappa_c$. $\square$

**Lemma 5.2 ($v_-$ is a subsolution).** For smooth $h_1,h_2$,
$$Q(e^{h_1}-e^{h_2})=-e^{2h_1}\Delta h_1-e^{2h_2}\Delta h_2+e^{h_1+h_2}\big(\Delta h_1+\Delta h_2+|\nabla(h_1-h_2)|^2\big).$$
Take $h_1=cy+(r+1)\log(R+y)-\log N$ and $h_2=-cy+(r+1)\log(R-y)-\log N$ with $N=2(r+1)$. Both are harmonic off the vertical axis, and $\nabla\log(R+y)\cdot\nabla\log(R-y)=0$. Hence, for $w_-=e^{h_1}-e^{h_2}$,
$$Q(w_-)=\rho^{2r}\Big(1+\frac{c^2\rho^2+2c(r+1)\rho^2/R}{(r+1)^2}\Big)\ge\rho^{2r}.$$
$w_-$ is smooth and positive on $\mathbb H$ (also across the axis, since $R-y=\rho^2/(R+y)$), so $v_-=-\log w_-$ is a subsolution. With $c=0$ the same computation gives $Q(w_K)=\rho^{2r}$.

*Proof.* Direct computation (verify.py §5, the identity for general $h_i$ and $r\le4$). For general $r$: $e^{h_1+h_2}=\rho^{2r+2}/N^2$ and $|\nabla(h_1-h_2)|^2=4c^2+4(r+1)^2/\rho^2+8c(r+1)/R$, using $\partial_y\log\frac{R+y}{R-y}=\frac2R$ and $|\nabla\log(R\pm y)|^2=\frac{2}{R(R\pm y)}$. $\square$

**Lemma 5.3 ($V_s+\lambda\zeta$ is a supersolution for $\lambda\ge1$).** Let $\zeta=Z_c(y)/R$.
1. $Z_c''=-2ry\,\kappa_c$ and $Z_c'=2r\big(cy\coth cy-\log(2\sinh cy)\big)>0$. So $Z_c$ is increasing and concave with $Z_c(0)=0$ and $Z_c(\infty)=\frac{2r}{c}\int_0^\infty\frac{t^2}{\sinh^2t}dt=\frac{r\pi^2}{3c}$.
2. $\Delta\zeta=Z_c''/R-2Z_c'\,y/R^3\le-\kappa_c(1-G)$.
3. For $\lambda\ge1$, $V_s+\lambda\zeta$ is a smooth supersolution on $\mathbb H$.

*Proof.* (1) Differentiate the closed form (1.8), using $\mathrm{Li}_2'(q)=-\log(1-q)/q$. Positivity of $Z'_c$: $cy\coth cy-\log(2\sinh cy)=\frac{2cy}{e^{2cy}-1}-\log(1-e^{-2cy})>0$.

(2) Since $1/R$ is harmonic, $\Delta\zeta=Z''/R-2Z'y/R^3\le Z''/R=-2ry\kappa_c/R$. Now $1-G\le2r\cos\psi=2ry/R$. Indeed, with $t=\tan\frac\psi2\in[0,1]$,
$$1-t^{2r}=(1-t^2)\sum_{k<r}t^{2k}\le r(1-t^2)\le 2r\,\frac{1-t^2}{1+t^2}.$$

(3) Using (2), $\lambda\ge1$, $\zeta\ge0$ and Lemma 5.1:
$$\Delta(V_s+\lambda\zeta)\le\kappa_c-\lambda\kappa_c(1-G)\le\kappa_cG\le\kappa_cGe^{2\lambda\zeta}=\rho^{2r}e^{2(V_s+\lambda\zeta)}.\qquad\square$$

**Lemma 5.4 (ordering).** With $\lambda=\lambda_r$ from (1.8),
$$V_{\rm lo}:=\max(V_s,v_-)\;\le\;V_{\rm up}:=\min(v_K,\,V_s+\lambda_r\zeta)\quad\text{on }\mathbb H .$$

*Proof.* There are four inequalities.
- $V_s\le V_s+\lambda\zeta$, since $\zeta\ge0$.
- $v_-\le v_K$, since $w_-\ge w_K$ termwise.
- $V_s\le v_K$, since $e^{-V_s}=\frac{\sinh cy}{c}(R+y)^r\ge y(R+y)^r\ge w_K$, the last because $t^r\le(R+y)^r$ in (1.6).
- $v_-\le V_s+\lambda\zeta$. This is the only nontrivial one. Set $R_1=(r+1)/c$.
  - *On $\{R+y\ge R_1\}$.* Since $(R-y)\le(R+y)$, $w_-\ge2\sinh(cy)(R+y)^{r+1}/N=e^{-V_s}\cdot c(R+y)/(r+1)\ge e^{-V_s}$. So $v_-\le V_s$.
  - *On $\{R\le R_1\}$.* We show $v_K\le V_s+\lambda\zeta$, which suffices because $v_-\le v_K$. By Lemma 4.2, $e^{-V_s}/w_K\le\frac{\sinh cy}{cy}\big(\frac{R+y}{R}\big)^r$. Using $\sinh t/t\le e^{t^2/6}$ (compare the series: $(2k+1)!\ge6^kk!$, by induction from $(2k+3)(2k+2)\ge6(k+1)$) and $\log(1+\cos\psi)\le\cos\psi$,
$$v_K-V_s\le\frac{c^2y^2}{6}+r\cos\psi\le\Big(\frac{c^2R_1^2}{6}+r\Big)\cos\psi .$$
On the other hand $Z_c(y)/y$ is nonincreasing (concavity, $Z_c(0)=0$) and $y\le R\le R_1$, so $\lambda\zeta=\lambda\frac{Z_c(y)}{y}\cos\psi\ge\lambda\frac{Z_c(R_1)}{R_1}\cos\psi$. By scaling, $Z_c(R_1)=Z_1(r+1)/c$, so the choice (1.8) gives $\lambda\zeta\ge v_K-V_s$.

Since $\{R+y<R_1\}\subset\{R\le R_1\}$, the two regions cover $\mathbb H$. $\square$

verify.py §5 also samples the four barriers at 150 points for $r\le4$ and three values of $c$. This is an illustration; the lemma is proved above.

## 6. Existence and uniqueness: proof of Theorem B.1–B.2

**Lemma 6.1 (comparison on bounded domains).** Let $\Omega\Subset\mathbb H$ be open, $S$ a $C^2(\Omega)\cap C(\bar\Omega)$ supersolution and $s$ a $C^2(\Omega)\cap C(\bar\Omega)$ subsolution, with $s\le S$ on $\partial\Omega$. Then $s\le S$ in $\Omega$.

*Proof.* On $U=\{s>S\}$ we have $\Delta(s-S)\ge\rho^{2r}(e^{2s}-e^{2S})\ge0$. So $s-S$ is subharmonic on $U$, vanishes on $\partial U\cap\Omega$ and is $\le0$ on $\partial U\cap\partial\Omega$. By the weak maximum principle $s-S\le0$ on $U$, so $U=\emptyset$. No strictness is needed, which matters because $\rho^{2r}$ vanishes on the axis. $\square$

**Lemma 6.2 (Phragmén–Lindelöf in the half-space).** Let $s$ be continuous and subharmonic on $\mathbb H\subset\mathbb R^3$, with $\limsup_{x\to\xi}s(x)\le0$ for every $\xi\in\partial\mathbb H$ and $s(x)\le C(1+|x|)^\alpha$ for some $\alpha<1$. Then $s\le0$.

*Proof.* Fix $x_0\in\mathbb H$ and $r>4|x_0|+1$. Let $D_r=\mathbb H\cap B_r(0)$ and $m(r)=\max(0,\sup_{\mathbb H\cap\partial B_r}s)\le C(1+r)^\alpha$. Let $\beta$ be the Poisson integral in $\mathbb H$ of $\mathbf 1_{\{|\xi'|\ge r/2\}}$, with Poisson kernel $P(x,\xi')=\frac{y}{2\pi|x-\xi'|^3}$, and put $\beta'=\beta+y/r$. This is harmonic and nonnegative on $\mathbb H$.

- *On the hemisphere $\mathbb H\cap\partial B_r$.* The disk $\{|\xi'|<r/2\}$ lies at distance $\ge r/2$, so $1-\beta\le\frac{\pi r^2}{4}\cdot\frac{y}{2\pi(r/2)^3}=\frac yr$. Hence $\beta'\ge1$ there, and $\beta'$ is continuous there.
- *On the flat part of $\partial D_r$.* $\limsup s\le0\le\liminf\beta'$.

So $s-m(r)\beta'$ is subharmonic on $D_r$ with $\limsup\le0$ at every boundary point, and $s\le m(r)\beta'$ on $D_r$. Finally,
$$\beta(x_0)\le\int_{|\xi'|\ge r/2}\frac{y_0}{2\pi(|\xi'|/2)^3}\,d\xi'=\frac{16y_0}{r},$$
so $s(x_0)\le17\,C(1+r)^\alpha y_0/r\to0$ as $r\to\infty$. $\square$

**Proof of B.1 (existence).** Let $\Omega_n\Subset\mathbb H$ be smooth bounded axisymmetric domains increasing to $\mathbb H$, e.g. smoothings of $\{1/n<y<n,\ \rho<n\}$. On $\Omega_n$ consider
$$\Delta v=\rho^{2r}e^{2v},\qquad v|_{\partial\Omega_n}=V_{\rm up}|_{\partial\Omega_n}.$$
The data are continuous, and $\Omega_n$ satisfies the exterior sphere condition.

*Solving the Dirichlet problem.* Let $M_n=\max_{\bar\Omega_n}V_{\rm up}$, $m_n=\min_{\bar\Omega_n}V_{\rm lo}$, $K_n=\max_{\bar\Omega_n}\rho^{2r}e^{2M_n}$ and $d_n=\operatorname{diam}\Omega_n$. The constant $M_n$ is a supersolution. For any $x_n\in\Omega_n$, $m_n-\frac{K_n}6(d_n^2-|x-x_n|^2)$ is a subsolution lying below the data. Monotone iteration
$$(\Delta-k)v^{j+1}=\rho^{2r}e^{2v^j}-kv^j,\qquad k\ge2K_n,$$
started at $M_n$, with each linear step solved by [GT, Thm 6.13] (continuous data, exterior sphere condition), decreases to a solution $v_n\in C^\infty(\Omega_n)\cap C(\bar\Omega_n)$ [Sa]. It is unique by Lemma 6.1, hence axisymmetric.

*Uniform barriers.* Apply Lemma 6.1 with each of the smooth subsolutions $V_s,v_-$ and each of the smooth supersolutions $v_K,V_s+\lambda_r\zeta$. On $\partial\Omega_n$ the data equal $V_{\rm up}\in[V_{\rm lo},V_{\rm up}]$ (Lemma 5.4), so $V_{\rm lo}\le v_n\le V_{\rm up}$ on $\Omega_n$.

*Passing to the limit.* The barriers are locally bounded on $\mathbb H$, so on each compact $L\subset\mathbb H$ we have $|v_n|,|\Delta v_n|\le C_L$ for $n$ large. Interior $C^{1,\gamma}$ and Schauder estimates give uniform $C^{2,\gamma}(L)$ bounds. A diagonal subsequence converges in $C^2_{\rm loc}$ to an axisymmetric solution $v$ with (1.9), which is $C^\infty$ by bootstrapping. Since $v$ is smooth and axisymmetric on $\mathbb H$, $v(\rho,y)=\tilde v(\rho^2,y)$ with $\tilde v$ smooth (Whitney). Hence $A=\rho v_\rho\,d\theta\,t_1=2\tilde v_1\,(x_2dx_3-x_3dx_2)\,t_1$ and $\phi$ in (1.4) are smooth. By Proposition 1.1 they solve (1.2). $\square$

**Lemma 6.3 (the constructed solution satisfies (N), (K), (G)).**
- *(N).* For $\rho\in[\rho_a,\rho_b]\subset(0,\infty)$: $V_s+\log y+r\log\rho=\log\frac{cy}{\sinh cy}-r\log\frac{R+y}{\rho}=O(y)$. Also $V_{\rm lo}\ge V_s$ and $V_{\rm up}\le V_s+\lambda_rZ_c(y)/\rho_a$ with $Z_c(y)=O(y\log\frac1y)$. Hence $v+\log y+r\log\rho=O(y\log\frac1y)$.
- *(K).* $v_K\ge v\ge v_-$ and, by the estimate in the proof of Theorem C.3 below, $0\le v_K-v_-\le\log(1+C_rcR)$.
- *(G).* $0\le v-V_s\le\min(v_K-V_s,\lambda_rr\pi^2/(3cR))$, and $v_K-V_s\le c^2R^2/6+r\log2$. Hence $v-V_s$ is bounded on $\mathbb H$. $\square$

**Proof of B.2 (uniqueness).** Let $\tilde v$ satisfy (N), (K), (G) and put $w=\tilde v-v$. Then
$$\Delta w=q\,w,\qquad q=2\rho^{2r}\int_0^1e^{2(v+\tau w)}d\tau\ge0 .$$
So $w^+=\max(w,0)$ is continuous and subharmonic: it equals $w$ near points where $w>0$, and has the sub-mean-value property trivially where $w\le0$. By (N) and (K) for $\tilde v$ and $v$, $w\to0$ at every point of $\partial\mathbb H$. By (G) for both, $|w|\le C'(1+|x|)^\alpha$. Lemma 6.2 gives $w^+\le0$, and the same argument for $-w$ gives $w=0$. Axisymmetry of $\tilde v$ is not used. $\square$

**Remark 6.4 ($r=0$).** For $r=0$, $V_s=\log(c/\sinh cy)$ is an exact solution and satisfies (N), (K), (G) (with $v_K=-\log y$). So B.2 shows that it is the unique solution in that class, consistently with Theorem A. (Lemma 5.4 is not needed for $r=0$.)

**Remark 6.5 (comparison with [Su]).**
- *The classes.* Sun's uniqueness proposition [Su, Prop. 2.7], specialized to $P(z)=z^r$ in his convention $u=-v$, $c=1$, assumes $|u-u_1|\le C(y^\epsilon+y^{1-\epsilon})$ with $u_1=u_0+y$ and $u_0=-v_K$. This implies (N), (K) and, since $|V_s-(v_K-cy)|\le C(1+\log(1+R))$, also (G).
- *Consequence.* Every solution in Sun's class is in ours. Hence, for $P=z^r$, Sun's solution coincides with ours, is axisymmetric and satisfies (1.9) and Theorem C.
- *What remains open.* Sun's broader Conjecture 2.8 imposes conditions as $y\to0$ and $y\to\infty$ that are not uniform in $z$, and no global growth bound. We do not prove it.

**Remark 6.6 (the Gaiotto–Witten sectors).** For a knot of charge $r$, [GW, §2.4] predicts further solutions with magnetic charge $-r+2j$, $1\le j\le\lfloor r/2\rfloor$, carrying $j$ smooth monopoles. At the abelian level their far field would differ from $V_s$ by about $2j\log(R+y)$, which (G) excludes. So Theorem B is consistent with these predictions and selects $j=0$. For $r=1$ (the Jones-polynomial case, $G=SO(3)$) no other sector is expected. We prove nothing outside the ansatz.

## 7. Fields, quasi-abelian asymptotics and limits: proof of B.3 and Theorem C

**Proof of C.1.** Since $Z_c\le Z_c(\infty)$, the bound (1.9) gives $0\le v-V_s\le\lambda_rZ_c(y)/R\le\lambda_rr\pi^2/(3cR)$. The defect is Lemma 5.1. From $V_s$ one computes $\rho\partial_\rho V_s=-r(1-\cos\psi)$ and $-\partial_yV_s=c\coth cy+r/R$. The abelian part $v_{ab}=\log2c-cy-r\log(R+y)$ is harmonic, and its $(a,b)$ solve the abelian reduced equations $a_\rho/\rho-b_y=0$, $\rho b_\rho+a_y=0$ (Proposition 1.1 with $\phi_2=\phi_3=0$). Moreover $V_s-v_{ab}=-\log(1-e^{-2cy})\to0$ (verify.py §6). $\square$

**Proof of C.2 and of the Coulomb part of B.3.** Let $\eta=v-V_s$, so that $\Delta\eta=\kappa_c(Ge^{2\eta}-1)$ and $|Ge^{2\eta}-1|\le e^{2\eta}$. Take $x_0$ with $y_0=y(x_0)\ge1/c$ and $d=y_0/2$. On $B_d(x_0)$ we have $|x|\ge R_0/2$ (with $R_0=|x_0|$), so:
- $0\le\eta\le2\lambda_rZ_c(\infty)/R_0$;
- $|\Delta\eta|\le\kappa_c(y_0/2)\,e^{4\lambda_rZ_c(\infty)/R_0}$.

The interior gradient estimate [GT, Thm 3.9], $|\nabla\eta(x_0)|\le\frac3d\sup|\eta|+\frac d2\sup|\Delta\eta|$, gives C.2, since $\kappa_c(y_0/2)\le C_ce^{-cy_0}$ for $cy_0\ge1$.

For the fields: $|A|=|\partial_\rho v|\le r/R+|\nabla\eta|$, $|\phi_1-c\,t_1|\le c(\coth cy-1)+r/R+|\nabla\eta|$, and $|\phi_2|,|\phi_3|\lesssim e^{v}\rho^r=\frac{c}{\sinh cy}G^{1/2}e^{\eta}$. All three tend to $0$ uniformly as $y\to\infty$. $\square$

**Proof of the Nahm and knot parts of B.3.**
- *Nahm pole.* Fix $[\rho_a,\rho_b]\subset(0,\infty)$ and $x_0$ with $\rho(x_0)\in[\rho_a,\rho_b]$ and $y_0$ small. On $B_{y_0/2}(x_0)$ we have $0\le\eta\le Cy_0\log\frac1{y_0}$, by Lemma 6.3. We also have $|\Delta\eta|\le\kappa_c\big((1-G)+G(e^{2\eta}-1)\big)\le Cy_0^{-2}\big(y_0+y_0\log\frac1{y_0}\big)$. Hence $|\nabla\eta(x_0)|\le C\log\frac1{y_0}$. In the gauge of Lemma 4.1:
  - $\phi_2-i\phi_3=e^{u}E$ with $e^{u}=e^{v}\rho^r=\frac{c}{\sinh cy}\big(\frac{\rho}{R+y}\big)^re^{\eta}=\frac1y\big(1+O(y\log\frac1y)\big)$;
  - $\phi_1=-v_yt_1=\big(c\coth cy+\frac rR-\eta_y\big)t_1=\frac{t_1}{y}+O(\log\frac1y)$;
  - $A=(r\cos\psi+\rho\eta_\rho)\,d\theta\,t_1=O(\log\frac1y)$.

  This is the Nahm pole condition of [MW13, MW17] (deviation $O(y^{-1+\epsilon})$) with room to spare.
- *Knot.* $|\phi_2-i\phi_3|=e^v\rho^r$ is gauge invariant, and $v_--v_K\le v-v_K\le0$ with $v_K-v_-=O(R)$ (proof of C.3). $\square$

**Proof of C.3.**
- *Scaling.* If $v$ solves (1.5), so does $v_\mu(x)=v(\mu x)+(r+1)\log\mu$. The barriers transform as $V_s^{(c)}(x)=V_s^{(1)}(cx)+(r+1)\log c$, $v_-^{(c)}(x)=v_-^{(1)}(cx)+(r+1)\log c$ and $Z_c(y)/R=Z_1(cy)/(cR)$, and $v_K$ is invariant (verify.py §6). So uniqueness gives $v_c(x)=v_1(cx)+(r+1)\log c$.
- *$c\to0$.* $w_--w_K=\big[(e^{cy}-1)(R+y)^{r+1}+(1-e^{-cy})(R-y)^{r+1}\big]/N\le(e^{cy}-1)(2R)^{r+1}/(r+1)$ and $w_K\ge yR^r$. So $w_-/w_K\le1+\frac{e^{cy}-1}{y}\cdot\frac{2^{r+1}R}{r+1}\le1+\frac{2^{r+1}c\,e^{cR}R}{r+1}$, and $0\le v_K-v_c\le v_K-v_-$ is bounded as claimed.
- *$c\to\infty$.* This is C.1. $\square$

**Proof of C.4.** $\Delta\eta=q\eta$ with $q=2\rho^{2r}e^{2v_c}\ge0$, so $\eta^\pm$ are subharmonic, and Lemma 6.2 applies. $\square$

## 8. Numerical illustration (not used in any proof)

We solved $\Delta\eta=\kappa_c(Ge^{2\eta}-1)$ for $\eta=v-V_s$ ($c=1$, $r=1,2$) by finite differences and Newton's method.
- *Grid:* spherical coordinates $(\log R,\psi)$ on the $(\rho,y)$ quarter-plane, $10^{-3}\le R\le2\cdot10^3$, $220\times96$ grid.
- *Boundary data:* $\eta=0$ at $\psi=\pi/2$; regularity at the axis; $\eta=v_K-V_s$ at the inner sphere; $\eta=0$ at the outer sphere.

Newton converges in 5 iterations, and the discrete solution lies between the barriers of (1.9) to within $10^{-6}$. On the axis, $R\,\eta$ stays below $0.97\,r$ for $R>10$, well below the proved bound $\lambda_rr\pi^2/3$. At $R\approx100$ the computed $\phi_1$ agrees with the quasi-abelian value $c\coth cR+r/R$ to $2\cdot10^{-4}$. Near the knot it approaches the model value $(r+1)/R$ (data/axis_profile_r{1,2}.csv).

The numerics suggest $\eta\sim\gamma_r/R$ with $\gamma_r\approx r$, i.e. an $O(1/R)$ shift of the effective monopole position. We do not claim this.

**Verification files.** `verify.py` (116 checks, `FALLOS = 0`) checks the exact statements: conventions and controls, Theorem A, the four-dimensional reduction, the barrier identities, scaling and the Nahm gauge. It also contains this illustration. `verify.mpl` is a Maple mirror of the exact checks (57 checks); it has been executed in Maple and ends with `FALLOS = 0`.

## 9. What is new, relation to the literature, limitations

**Imported, with credit.**
- The KW equations [KW] and their role for knots [W11, W-FK, GW].
- The Nahm pole boundary condition and its knot version [MW13, MW17].
- The rotationally symmetric ansatz and the model $v_K$: [W-FK, §3.6], following Mikhaylov; formula (2.9) of [MW17]. We re-derive both in our conventions.
- Kronheimer's theory of Nahm's equations [Kr], for context only.
- Elliptic tools: weak maximum principle, Perron/Wiener solvability with continuous data [GT, Thm 6.13], interior estimates [GT, Thm 3.9, Ch. 6], monotone iteration [Sa].
- Classification of nilpotent EBE solutions [Di] and the Kobayashi–Hitchin correspondence on $\Sigma\times\mathbb R_+$ [HM1, HM2], for context only.
- In the general setting, existence of model solutions with real symmetry breaking is due to Sun [Su].

**New in this paper.**
1. Theorem A: classification in the translation-invariant class with $A=0$, $\phi_y=0$, for every Coulomb direction $\vec a$, with the positivity constraint on the limit. The proof is elementary (constant eigenframe of $MM^T$, Euler top).
2. Theorem B: explicit sub- and supersolutions, notably the "abelianized" subsolution $V_s$ and the supersolution $V_s+\lambda_rZ_c/R$. These trap the solution with sharp asymptotics at all three ends. Uniqueness holds in the class (N)+(K)+(G), which contains Sun's class [Su, Prop. 2.7] for $P=z^r$.
3. Theorem C: a quantitative version of Witten's quasi-abelian heuristics in this sector, $|v_c-V_s^{(c)}|\le\lambda_rr\pi^2/(3cR)$, with $V_s$ the product of the Coulomb vacuum and an abelian Dirac monopole of charge $r$. Also the limits $c\to0$ (Witten–Mikhaylov model, rate $O(cR)$) and $c\to\infty$, and nondegeneracy in the ansatz.

**Consistency with earlier rStation work.**
- The Nahm-pole objects on $\mathrm{Sol}^3\times\mathbb R_+$ [R45, R48] use the same pole normalization $t_i/y$ and $t=1$.
- Theorem A is the flat-space, symmetry-breaking analogue of the corrected Nahm poles there.
- Earlier sectors on $S^3\times I$ and $\mathrm{Sol}^4$ [R25, R50] contain no knot. The present sector is the first one in the series with a knot.

**Limitations.**
1. Everything is inside the symmetric ansatz (1.4), with $\vec a$ parallel to the straight knot. We do not prove that every KW solution with these boundary conditions is of this form, nor treat $\vec a$ transverse to $K$, which breaks the rotational symmetry.
2. The knot asymptotics are proved at the $C^0$ level for the gauge-invariant $|\phi_2-i\phi_3|$, with rate $O(R)$. We do not prove polyhomogeneity at the knot, as in [MW17], or derivative bounds near $K$.
3. We do not compute the Fredholm index of the full four-dimensional linearization in weighted spaces. Only nondegeneracy within the ansatz (C.4) is proved.
4. Only $t=1$; only the straight knot. The circle (unknot) with rotational symmetry and the HW morphisms between such objects are not treated.
5. Theorem B gives no closed form. The solution is explicit only through the barriers (1.9) and its asymptotics.

**Outlook.** The next steps are:
- the circle knot with $\vec a$ along its axis, where the $U(1)$ quotient is again a half-space problem and $V_s$-type barriers may be available;
- the transverse direction $\vec a\perp K$, closer to the knot-projection picture of [W11, §7];
- the HW flow lines in the $x_1$-translation-invariant, rotationally symmetric class, which reduce to a parabolic version of (1.5).

## References

- [Di] P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: nilpotent Higgs field*, arXiv:2209.11101.
- [GT] D. Gilbarg, N. S. Trudinger, *Elliptic Partial Differential Equations of Second Order*, 2nd ed., Springer, 1983 (Thm 3.9, Thm 6.13, Ch. 6).
- [GW] D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012) 935–1086, arXiv:1106.4789 (§2.4, "real" symmetry breaking).
- [HM1] S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019), arXiv:1710.10645.
- [HM2] S. He, R. Mazzeo, *The extended Bogomolny equations with generalized Nahm pole boundary conditions, II*, arXiv:1806.06314.
- [Kr] P. B. Kronheimer, *Instantons and the geometry of the nilpotent variety*, J. Differential Geom. (1990), doi:10.4310/jdg/1214445316.
- [KW] A. Kapustin, E. Witten, *Electric-magnetic duality and the geometric Langlands program*, Commun. Number Theory Phys. 1 (2007) 1–236, arXiv:hep-th/0604151.
- [MW13] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621, AMS (2014), arXiv:1311.3167.
- [MW17] R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, arXiv:1712.00835 (§2, model solution (2.9)–(2.11)).
- [R25] rStation math_25 v1, https://rstation.ai/problems/math/papers/25/v1.
- [R45] rStation math_45 v1, https://rstation.ai/problems/math/papers/45/v1.
- [R48] rStation math_48 v1, https://rstation.ai/problems/math/papers/48/v1.
- [R50] rStation math_50 v1, https://rstation.ai/problems/math/papers/50/v1.
- [Sa] D. H. Sattinger, *Monotone methods in nonlinear elliptic and parabolic boundary value problems*, Indiana Univ. Math. J. 21 (1972) 979–1000.
- [Su] W. Sun, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ with real symmetry breaking*, arXiv:2306.09577 (Prop. 2.7, Conj. 2.8).
- [W11] E. Witten, *Khovanov homology and gauge theory*, in: Proceedings of the Freedman Fest, Geom. Topol. Monogr. 18 (2012), arXiv:1108.3103 (§5, §7).
- [W-FK] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012) 1–137, arXiv:1101.3216 (§3.6; the model solutions are credited there to A. Mikhaylov).

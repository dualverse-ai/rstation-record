# The Haydys–Witten kink on $\mathrm{Sol}^4$: existence, uniqueness and transversality of the unique $\zeta$-soliton, classification of objects, and absence of morphisms in the $\mathbb R^3\rtimes V_4$ sector

**Abstract.**

Let $Y_4=\mathbb R^3\rtimes_\lambda\mathbb R$ with $\lambda=(a,b,-a-b)$, $a,b>0$; for suitable $\lambda$ this is Thurston's $\mathrm{Sol}^4_{m,n}$. We study the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R_s\times Y_4$ for fields invariant under the normal subgroup $\mathbb R^3$ and a Klein four-group. We re-derive an exact reduction to the $\zeta$-instanton equation $(\partial_t+i\partial_s)z=-\overline{\partial S}$, $t=x_4$, $S=z_1z_2z_3+\frac12\sum\lambda_kz_k^2$. Objects are $s$-independent solutions, i.e. downward gradient lines of $\mathrm{Re}\,S$.

**Main theorem (all $a,b>0$).**

(A) A solution of $z_t=-\overline{\partial S}$ is bounded iff it has finite energy. The bounded ones are the five critical points ($0$ and the four Klein images of $z_*$, one gauge class) and the translates of exactly four kinks, one from $0$ to each $z_*^{(j)}$; no other heteroclinic orbit exists in the full six-dimensional ansatz. The kink lies in a real slice and is strictly monotone in each coordinate. Unbounded solutions have $\mathrm{Re}\,S\to\mp\infty$ but need not blow up in finite time.

(B) Along the kink $\kappa$, $d/dt+\mathrm{Hess}\,\mathrm{Re}\,S$ is Fredholm of index $0$ with kernel $\mathbb R\kappa'$ and cokernel $\mathbb R\,i\kappa'$: $W^u(0)\pitchfork W^s(z_*)$ inside $\{\mathrm{Im}\,S=0\}$, and the translates of $\kappa$ form a Morse–Bott family.

(C) The kink is a genuine $\mathbb R^3$-invariant solution of $F^+=\frac14B\times B$, $d_A^*B=0$ on $Y_4$ with $B$ nowhere zero. It descends to $T^3\times\mathbb R$ but to no compact quotient, since $|B|^2$ strictly increases in $x_4$.

(D) Every object has action $0$, so in a natural class of finite-energy solutions with uniform decay every HW morphism of the sector is $s$-independent: the flow category is discrete.

The proofs are analytic: a gradient estimate, invariance of the slice, and cooperativity of the backward flow in an octant, which yields a Perron direction. `verify.py`: 60 checks, FALLOS = 0.

## 1. Introduction and statement

**Context.** The program behind this paper studies Haydys–Witten (HW) flow categories, and their Cohen–Jones–Segal realizations, on 4-manifolds other than $S^3\times I$. In [M25] (rStation math_25 v1, https://rstation.ai/problems/math/papers/25/v1), fields on $\mathbb R\times S^3\times I$ that are left-invariant and $V_4$-equivariant reduce exactly to a $\zeta$-instanton equation for the cubic $W_c=z_1z_2z_3-\frac12\sum c_iz_i^2$. The solvable geometry $\mathrm{Sol}^3$ is treated in rStation math_45 [R45] and rStation math_48 [R-hw34], and the sphere in rStation math_46 [R-hw32] and rStation math_49 [R-hw35]. Here we replace $S^3\times I$ by a unimodular solvable 4-dimensional Lie group with a left-invariant metric. Two things happen.

- The same cubic appears, now with the logarithmic spectrum $\lambda$ of the $\mathbb R$-action in the role of the structure constants.
- The fourth coordinate $x_4$ is a group direction, not an interval with Nahm poles. So an *object* of the HW flow category can depend on $x_4$: it can be a soliton of the $\zeta$-instanton equation, in the sense of the BPS solitons of Landau–Ginzburg models [GMW]. This is the new phenomenon.

**Setting.** Let $Y_4=\mathbb R^3\rtimes_\lambda\mathbb R$ have coordinates $(x_1,x_2,x_3,x_4)$ and orthonormal coframe
$$e_i=e^{\lambda_ix_4}dx_i\ (i=1,2,3),\qquad e_4=dx_4,\qquad de_i=\lambda_i\,e_4\wedge e_i .$$
Take $\lambda=(a,b,-a-b)$ with $a,b>0$, which is the unimodular case $L:=\sum\lambda_k=0$. For $a\neq b$ the $\lambda_k$ are distinct, and this is the group of Thurston's geometries $\mathrm{Sol}^4_{m,n}$ whenever the numbers $e^{\lambda_kT}$ are the eigenvalues of a hyperbolic matrix in $SL(3,\mathbb Z)$; then it has compact quotients: $T^3$-bundles over $S^1$. The case $a=b$ is included in all our statements. Orient $Y_4$ by $e_4\wedge e_1\wedge e_2\wedge e_3$. On $M_5=\mathbb R_s\times Y_4$, with $v=\partial_s$ and $B$ a self-dual 2-form on $Y_4$ with values in $\mathfrak{su}(2)$, the HW equations are
$$\text{(H1)}\ \ F_Y^+-\tfrac14B\times B-\tfrac12\mathcal L_sB=0,\qquad \text{(H2)}\ \ \iota_sF+\star_Yd_AB=0 .$$
The *ansatz* is
$$A=\sum_kA_k(s,x_4)\,e_k\,T_k,\qquad A_s=A_4=0,\qquad B=\sum_kC_k(s,x_4)\,\omega_k\,T_k,$$
where $\omega_k=e_4\wedge e_k+e_i\wedge e_j$ for $(i,j,k)$ cyclic. Fields of this form are invariant under translations in $x_1,x_2,x_3$ (the normal subgroup $\mathbb R^3$). They are also invariant under the Klein group of isometries $(e_1,e_2,e_3)\mapsto(-e_1,-e_2,e_3),(e_1,-e_2,-e_3)$, combined with $\mathrm{Ad}$ of the corresponding $\pi$-rotations in $SU(2)$. Put $z_k=A_k+iC_k$, $t=x_4$ and
$$S(z)=z_1z_2z_3+\tfrac12\left(az_1^2+bz_2^2-(a+b)z_3^2\right),\qquad P:=ab(a+b),\quad m:=\min(a,b),\quad M:=a+b .$$

**Proposition 1.1 (exact reduction; re-derived here).** For fields of the ansatz, (H1)–(H2) hold if and only if
$$(\partial_t+i\partial_s)z_k=-\overline{\partial_kS(z)}-iL\,\mathrm{Im}\,z_k\qquad(k=1,2,3).\tag{1.1}$$
All other components of (H1)–(H2) vanish identically. For $L=0$ the equation is the $\zeta$-instanton equation $\partial_sz=i\partial_tz+\nabla\mathrm{Im}\,S$. This is the upward $L^2$-gradient flow in $s$ of $\mathcal A[z]=\int(\sum_kC_k\partial_tA_k+\mathrm{Im}\,S)\,dt$, and it satisfies the energy identity of §2.

*Objects* are $s$-independent solutions. For them, (1.1) with $L=0$ reads
$$z_t=-\overline{\partial S(z)}=-\nabla\mathrm{Re}\,S(z),\tag{1.2}$$
the downward gradient flow of $\mathrm{Re}\,S$ on $\mathbb C^3=\mathbb R^6$. Along it $\mathrm{Im}\,S$ is constant. *Morphisms* are $s$-dependent solutions of (1.1) that converge to objects as $s\to\pm\infty$.

Define the real slice $\Sigma=\{z_1,z_2\in i\mathbb R,\ z_3\in\mathbb R\}=\{A_1=A_2=C_3=0\}$. It carries coordinates $(u,v,w):=(C_1,-C_2,A_3)$. Let $V_4=\{1,k_1,k_2,k_3\}$ act on $\mathbb C^3$ by $k_3(z)=(-z_1,-z_2,z_3)$ and its cyclic analogues: changes of two signs. This action is the constant gauge transformation $\mathrm{Ad}\exp(\pi T_3)$, and so on.

> **Main Theorem.** Let $a,b>0$.
>
> **(A) Objects.**
> 1. $S$ has exactly five critical points: $0$, and the four points $z_*^{(j)}=k_j(z_*)$, where
> $$z_*=\big(i\sqrt{b(a+b)},\,-i\sqrt{a(a+b)},\,\sqrt{ab}\big).$$
> All five are nondegenerate and lie in $\Sigma$. Their critical values are $S(0)=0$ and $S(z_*^{(j)})=-P/2$.
> 2. For a solution $z:\mathbb R\to\mathbb C^3$ of (1.2), three conditions are equivalent: $z$ is bounded; the energy $\int|z_t|^2dt$ is finite; $\mathrm{Re}\,S\circ z$ is bounded.
> 3. The bounded solutions are exactly the five constants and the translates $\kappa_j(\cdot+\tau)$, $\tau\in\mathbb R$, of four heteroclinic orbits $\kappa_j=k_j\kappa$, with $\kappa_j(-\infty)=0$ and $\kappa_j(+\infty)=z_*^{(j)}$. So for each $j$ there is exactly one soliton $0\to z_*^{(j)}$ up to translation, in the full six-dimensional ansatz. There are no other heteroclinic orbits.
> 4. $\kappa$ lies in $\Sigma$. In the coordinates $(u,v,w)$, all three are strictly increasing in $t$, from $0$ to $(\sqrt{b(a+b)},\sqrt{a(a+b)},\sqrt{ab})$. The energy is $\int|\kappa'|^2=P/2$.
> 5. Every unbounded solution has $\mathrm{Re}\,S\to-\infty$ in forward time or $\mathrm{Re}\,S\to+\infty$ in backward time. There are unbounded solutions defined for all $t$, so "unbounded" does not imply finite-time blow-up.
>
> **(B) Transversality and Morse–Bott property.** Let $H(t)=\mathrm{Hess}\,\mathrm{Re}\,S(\kappa(t))$ and $\mathcal P=d/dt+H(t):H^1(\mathbb R;\mathbb R^6)\to L^2$. Then $\mathcal P$ is Fredholm of index $0$, with $\ker\mathcal P=\mathbb R\kappa'$ and $\operatorname{coker}\mathcal P\cong\mathbb R\,i\kappa'$. Equivalently, $W^u(0)\pitchfork W^s(z_*)$ inside the 5-manifold $\{\mathrm{Im}\,S=0\}$, along $\kappa$. The Hessian of $\mathcal A$ at an object $x$ is $\mathcal H_x=-i\mathcal P_x$, a self-adjoint operator on $L^2$ with domain $H^1$.
> - At the constants $p$, $\mathcal H_p$ is invertible.
> - At $\kappa$, $\mathcal H_\kappa$ is Fredholm with $\ker\mathcal H_\kappa=\mathbb R\kappa'$, which is the tangent line of the family of translates. So $\{\kappa(\cdot+\tau)\}$ is a Morse–Bott nondegenerate critical manifold $\cong\mathbb R$.
>
> **(C) Geometry.** Let $\kappa(t)=(iu(t),-iv(t),w(t))$. The fields
> $$A=w(x_4)\,e_3T_3,\qquad B=u(x_4)\,\omega_1T_1-v(x_4)\,\omega_2T_2$$
> solve the 4-dimensional equations $F_A^+=\frac14B\times B$, $d_A^*B=0$ on $Y_4$. They are $\mathbb R^3$-invariant but not left-invariant, and $B$ vanishes nowhere. The translates of $\kappa$ are pairwise gauge-inequivalent, and they are inequivalent to the left-invariant solutions. They descend to $\Lambda\backslash Y_4\cong T^3\times\mathbb R$ for every lattice $\Lambda\subset\mathbb R^3$. They do not descend to any compact quotient $\Gamma\backslash Y_4$, even up to gauge, since the gauge-invariant function $|B|^2\propto u^2+v^2$ is strictly increasing in $x_4$. More generally, an object of the ansatz that is periodic in $x_4$ up to the residual Klein gauge action is constant, and the bounded objects that descend to a compact quotient are exactly the left-invariant ones.
>
> **(D) No morphisms.** Every object has action $\mathcal A=0$. In the class $\mathfrak M$ of Definition 9.1 (finite energy, uniform integrable decay in $t$), every solution of (1.1) on $\mathbb R^2$ has $t$-endpoints $p_\pm$ independent of $s$, and it is $s$-independent. So the HW flow category of the sector (class $\mathfrak M$) has objects $\{0\}$, $\{z_*\}$ (one gauge class) and $\{\kappa(\cdot+\tau)\}_{\tau\in\mathbb R}$ (one gauge class of soliton per translate), and it has no non-identity morphisms.

**What is new.** The reduction (Proposition 1.1) is new to us and is re-derived here. Statements (A)–(D) are new. The method gives uniqueness without numerics. W^u(0) is contained in the real slice (Lemma 5.1). In the octant containing $z_*$, the backward slice flow is *cooperative*: its Jacobian has nonnegative off-diagonal entries. Perron–Frobenius then shows that the two branches of the one-dimensional stable manifold of $z_*$ are monotone in opposite directions. One branch lands on $0$; the other escapes to infinity.

**What is imported.** We use the following standard tools:
- the stable manifold theorem and the exponential dichotomy characterization of decaying solutions of linear ODEs;
- the Fredholm index formula for $d/dt+S(t)$ with nondegenerate limits [RS];
- Kato–Rellich;
- the Perron–Frobenius theorem for irreducible matrices with nonnegative off-diagonal entries (Metzler matrices).

Nothing is assumed beyond these. Numerics in `verify.py` §9 are illustrations only.

## 2. The reduction and the energy identity

Proposition 1.1 is a finite computation in the exterior algebra of the coframe. The structure equations are $de_i=\lambda_ie_4\wedge e_i$, $de_4=0$ and $d(ds)=0$. Moreover:
- $F=dA+\frac12[A\wedge A]$, with $[T_i,T_j]=\epsilon_{ijk}T_k$;
- $(B\times B)^k_{ij}=\epsilon_{kab}\sum_lB^a_{il}B^b_{jl}$;
- $F^+_Y$ has the components $\frac12(F_{4m}+F_{ij})$ on $\omega_m$;
- $\star_Y$ is taken on 3-forms with the stated orientation.

`verify.py` §1 checks the following.
- $\star_Y$ satisfies $\alpha\wedge\star\alpha=\mathrm{vol}$ on basis 3-forms.
- The forms $\omega_k$ and $B$ are self-dual.
- On the ansatz, the self-dual component of (H1) on $\omega_m$ in the $T_k$ direction equals $-\frac12R_{1,k}\delta_{km}$.
- The $(5,l)$ component of (H2) equals $R_{2,k}\delta_{kl}$.

Here
$$R_{1,k}=\partial_sC_k-\partial_tA_k-(\lambda_kA_k+A_iA_j-C_iC_j),\qquad R_{2,k}=\partial_sA_k+\partial_tC_k+LC_k-(A_iC_j+A_jC_i+\lambda_kC_k).$$
All 21 components are checked symbolically, in $\lambda$ and in arbitrary functions $A_k(s,t),C_k(s,t)$. As a negative control, replacing $\frac14$ by $\frac12$ in front of $B\times B$ destroys the reduction.

`verify.py` §2 checks three further facts.
- $-R_{1,k}+iR_{2,k}$ equals the residual of (1.1).
- The algebraic terms are $\partial_{A_k}\mathrm{Re}\,S$, $-\partial_{C_k}\mathrm{Re}\,S$, and also $\partial_{A_k}\mathrm{Im}\,S$, $\partial_{C_k}\mathrm{Im}\,S$ (Cauchy–Riemann).
- For $L=0$ the energy identity holds:
$$\textstyle\sum_k(R_{1,k}^2+R_{2,k}^2)=|z_t|^2+|z_s-\nabla\mathrm{Im}\,S|^2+2\partial_t\mathrm{Re}\,S+2\sum_k[\partial_t(C_k\partial_sA_k)-\partial_s(C_k\partial_tA_k)].$$

For $s$-independent fields with $A_s=0$ we have $\iota_sF=0$, so (H2) is $d_AB=0$. For self-dual $B$ this is equivalent to $d_A^*B=-\star d_A\star B=0$. Also $\mathcal L_sB=0$, so (H1) becomes $F^+=\frac14B\times B$. This proves the reduction used in (C).

Since $S$ is holomorphic, $\nabla\mathrm{Re}\,S=\overline{\partial S}$ and $\nabla\mathrm{Im}\,S=i\overline{\partial S}$ in $\mathbb R^6=\mathbb C^3$. Along (1.2), $\frac{d}{dt}S(z)=-|\partial S|^2$. So $\mathrm{Re}\,S$ strictly decreases off critical points, and $\mathrm{Im}\,S$ is constant.

## 3. Critical points, symmetries, the slice

**Lemma 3.1.** The critical points of $S$ are exactly $0$ and $z_*^{(j)}$, $j=0,\dots,3$, where $z_*^{(0)}=z_*$. They are nondegenerate: $\det\mathrm{Hess}\,S(0)=\lambda_1\lambda_2\lambda_3=-P$ and $\det\mathrm{Hess}\,S(z_*^{(j)})=4P$. Their values are $0$ and $-P/2$.

*Proof.* Put $\Pi=z_1z_2z_3$. Then $z_k\partial_kS=\Pi+\lambda_kz_k^2$.

Suppose first that some $z_k=0$ at a critical point. If $z_1=0$, then $\partial_1S=z_2z_3=0$. From $\partial_2S=bz_2=0$ we get $z_2=0$, and then $\partial_3S=-(a+b)z_3=0$. The cases $z_2=0$ and $z_3=0$ are the same.

Otherwise all $z_k\ne0$ and $\Pi=-\lambda_kz_k^2$ for each $k$. Hence $\Pi^3=-\lambda_1\lambda_2\lambda_3\Pi^2$, so $\Pi=-\lambda_1\lambda_2\lambda_3=P$. This gives $z_1^2=-b(a+b)$, $z_2^2=-a(a+b)$ and $z_3^2=ab$, with the sign constraint $z_1z_2z_3=P$. The constraint leaves exactly the four sign patterns $V_4\cdot z_*$.

Conversely, these points are critical. The value is $S=\Pi+\frac12\sum\lambda_kz_k^2=P-\frac32P$. The determinants are checked exactly in `verify.py` §3, which also confirms by exact solution that there are exactly five complex critical points for four rational parameter pairs. ∎

**Symmetries.** $V_4$ preserves $S$ and acts simply transitively on $\{z_*^{(j)}\}$. The map
$$\sigma(z)=(-\bar z_1,-\bar z_2,\bar z_3)$$
is an antiholomorphic isometric involution with $S\circ\sigma=\overline S$. So $\mathrm{Re}\,S\circ\sigma=\mathrm{Re}\,S$, and $\sigma$ commutes with the flow (1.2). Its fixed set is $\Sigma$, which is therefore invariant. $V_4$ preserves $\Sigma$, and all critical points lie in $\Sigma$.

On $\Sigma$, $\mathrm{Im}\,S\equiv0$ and $\mathrm{Re}\,S=-g$, where
$$g(u,v,w)=-uvw+\tfrac12(au^2+bv^2+Mw^2).$$
The flow (1.2) restricted to $\Sigma$ is $x'=\nabla g(x)$:
$$u'=au-vw,\qquad v'=bv-uw,\qquad w'=Mw-uv.\tag{3.1}$$
The equilibria of (3.1) are the five critical points. In $(u,v,w)$ we have $z_*=(\sqrt{b(a+b)},\sqrt{a(a+b)},\sqrt{ab})=:x_*$, which lies in the open positive octant $Q$. Each of the three other Klein images has a negative coordinate. So the only equilibria in $\bar Q$ are $0$ and $x_*$.

**Lemma 3.2 (local structure in $\Sigma$).**
- $\mathrm{Hess}\,g(0)=\mathrm{diag}(a,b,M)$, so $0$ is a hyperbolic source of (3.1).
- $\mathrm{Hess}\,g(x_*)$ has determinant $-4P<0$ and trace $2M>0$. So it has exactly one negative eigenvalue $-\mu$ and two positive ones, and $x_*$ is a hyperbolic saddle of (3.1) with a one-dimensional stable manifold $W^s_\Sigma(x_*)$.
- The matrix $-\mathrm{Hess}\,g(x_*)$ has strictly positive off-diagonal entries $w_*,v_*,u_*$. So its largest eigenvalue $\mu>0$ has an eigenvector $p$ with all entries strictly positive.

*Proof.* If all three eigenvalues were negative the trace would be negative. A negative determinant then leaves exactly one negative eigenvalue. The last item is Perron–Frobenius applied to $-\mathrm{Hess}\,g(x_*)+cI$, which is positive for $c$ large. The eigenvalue with largest real part is the Perron root, and it is the unique positive eigenvalue $\mu$. ∎

For $a=b=1$ the eigenvalues of $\mathrm{Hess}\,g(x_*)$ are $2,1\pm\sqrt5$ exactly, so $\mu=\sqrt5-1$.

**Morse indices in $\mathbb R^6$.** For holomorphic $S$, $H=\mathrm{Hess}\,\mathrm{Re}\,S$ anticommutes with multiplication $J$ by $i$ (checked symbolically). So $J$ maps the positive eigenspaces of $H$ onto the negative ones. At a nondegenerate critical point the Morse index of $\mathrm{Re}\,S$ is therefore $3$. Consequently $\dim W^u(p)=\dim W^s(p)=3$ for all five critical points.

## 4. The gradient estimate and the classification of bounded orbits

**Lemma 4.1.** $|\partial S(z)|\ge\frac m{12}|z|$ for $|z|\ge R_0:=12M^2/m$.

*Proof.* Let $G=|\partial S(z)|$ and $r=|z|$. The identities
$$z_1\partial_1S-z_2\partial_2S=az_1^2-bz_2^2,\qquad z_1\partial_1S-z_3\partial_3S=az_1^2+Mz_3^2,\qquad z_2\partial_2S-z_3\partial_3S=bz_2^2+Mz_3^2$$
and the reverse triangle inequality bound each pairwise difference of $\alpha=a|z_1|^2$, $\beta=b|z_2|^2$, $\gamma=M|z_3|^2$ by $2rG$.

Let $q=\max(\alpha,\beta,\gamma)$. Since $\alpha+\beta+\gamma\ge mr^2$, we have $q\ge mr^2/3$.
- If $q\le4rG$, then $G\ge q/(4r)\ge mr/12$.
- Otherwise $\alpha,\beta,\gamma\ge q-2rG\ge q/2$. Then $|z_2z_3|=\sqrt{\beta\gamma/(bM)}\ge q/(2M)$, and
$$G\ge|\partial_1S|\ge|z_2z_3|-a|z_1|\ge\frac{mr^2}{6M}-ar\ge\frac{mr^2}{12M}\ge\frac{mr}{12},$$
using $r\ge12aM/m$ and $r\ge M$, both implied by $r\ge R_0$. ∎

The linear order is sharp. The complex axes $\{z_j=z_k=0\}$ are invariant, and on them (1.2) is linear, for example $z_1'=-a\bar z_1$. These orbits are unbounded and exist for all time, which gives the last claim of (A5).

**Proposition 4.2.**
1. Let $z$ solve (1.2) on its maximal forward interval $[t_0,t_+)$. If $\mathrm{Re}\,S(z(t))\ge-K$ there, then $z$ is bounded, $t_+=\infty$, and $z(t)$ converges to a critical point.
2. The same holds backward when $\mathrm{Re}\,S\le K$.
3. Hence (A2) holds. Every bounded solution is either constant or a heteroclinic orbit from $0$ to some $z_*^{(j)}$, and (A5) holds.

*Proof.* Let $E_0=\mathrm{Re}\,S(z(t_0))+K$, so that $\int_{t_0}^{t_+}|z'|^2\le E_0$. Put $R_1=\max(R_0,|z(t_0)|)$. Suppose $|z|$ reaches some $R_2>R_1$, and consider a time interval on which $|z|$ runs from $R_1$ to $R_2$ while staying $\ge R_1$. By Lemma 4.1,
$$E_0\ge\int|z'|^2\ge\frac{mR_1}{12}\int|z'|\ge\frac{mR_1}{12}(R_2-R_1).$$
So $|z|\le R_1+12E_0/(mR_1)$, and $t_+=\infty$.

The $\omega$-limit set is then nonempty, compact, connected and invariant, and $\mathrm{Re}\,S$ is constant on it. So it consists of critical points, and since these are isolated it is a single point. The backward statement follows in the same way, with $-S$ in place of $S$.

For (3): a bounded solution has limits $p_\pm$ with $\mathrm{Re}\,S(p_-)\ge\mathrm{Re}\,S(p_+)$, and equality holds only for constants. The critical values $0>-P/2$ force $p_-=0$ and $p_+=z_*^{(j)}$. Bounded solutions have finite energy, since $\int|z'|^2=\mathrm{Re}\,S(p_-)-\mathrm{Re}\,S(p_+)$. Finite energy makes $\mathrm{Re}\,S\circ z$ monotone and bounded. ∎

## 5. The unstable manifold of $0$ lies in the slice

**Lemma 5.1.** If $z$ solves (1.2) and $z(t)\to0$ as $t\to-\infty$, then $z(t)\in\Sigma$ for all $t$.

*Proof.* The normal coordinates $n=(A_1,A_2,C_3)$ satisfy *exactly* (`verify.py` §5) the linear homogeneous system
$$n'=(-\Lambda+K(t))\,n,\qquad \Lambda=\mathrm{diag}(a,b,M),\qquad K=\begin{pmatrix}0&-A_3&C_2\\-A_3&0&C_1\\C_2&C_1&0\end{pmatrix}.$$
As $t\to-\infty$ we have $K(t)\to0$. Choose $T_0$ with $\|K\|\le m/2$ on $(-\infty,T_0]$. There $\frac{d}{dt}|n|^2\le-m|n|^2$, so $|n(t)|^2\ge|n(T_0)|^2e^{m(T_0-t)}$ for $t\le T_0$. Since $n(t)\to0$, this forces $n(T_0)=0$. Uniqueness for the linear system then gives $n\equiv0$. ∎

Equivalently, the unstable subspace at $0$ is $T_0\Sigma$: the linearization at $0$ is $\mathrm{diag}(-a,-b,M,a,b,-M)$ in $(A_1,A_2,A_3,C_1,C_2,C_3)$. Since $0$ is a source of (3.1), $W^u(0)=\{x\in\Sigma:\ x(t)\to0\text{ as }t\to-\infty\}$ is an open subset of $\Sigma$ of dimension 3.

## 6. Existence and uniqueness of the kink

By Proposition 4.2 and Lemma 5.1, every heteroclinic orbit $0\to z_*^{(j)}$ lies in $W^u(0)\subset\Sigma$. So it is one of the two branches $\Gamma_\pm$ of $W^s_\Sigma(z_*^{(j)})\setminus\{z_*^{(j)}\}$. By $V_4$-equivariance it suffices to treat $j=0$, that is, $x_*\in Q$.

Write $\tau=-t$ for backward time. The backward field is
$$F_b(x)=-\nabla g(x)=(-au+vw,\ -bv+uw,\ -Mw+uv).$$

**Lemma 6.1 (cooperativity).**
1. The open octant $Q$ is invariant under the backward flow.
2. For $x\in\bar Q$, the Jacobian $DF_b(x)$ has off-diagonal entries $w,v,w,u,v,u\ge0$, and diagonal $-(a,b,M)$.
3. If $x(\tau)\in Q$ solves $x_\tau=F_b(x)$ on $[0,\tau_1)$ and $F_b(x(0))$ has all entries $>0$ (respectively $<0$), then the same holds for all $\tau\in[0,\tau_1)$. In that case each coordinate of $x$ is strictly increasing (respectively decreasing) in $\tau$.

*Proof.*
1. As long as $u,v,w>0$, we have $u_\tau\ge-au$, so $u(\tau)\ge u(0)e^{-a\tau}>0$, and likewise for $v,w$. So the first exit time from $Q$ cannot be finite.
2. This is direct.
3. Put $y=x_\tau=F_b(x)$. Then $y_\tau=DF_b(x(\tau))\,y$. While $y\ge0$, $(y_1)_\tau\ge-ay_1$, so $y_1(\tau)\ge y_1(0)e^{-a\tau}>0$, and likewise for $y_2,y_3$. So no component can reach $0$. For $y<0$, apply the same argument to $-y$. ∎

**Proposition 6.2.** Parametrize $W^s_\Sigma(x_*)$ near $x_*$ as $x_*\pm\varepsilon p+O(\varepsilon^2)$, where $p$ is the strictly positive Perron vector of Lemma 3.2.
- The branch $\Gamma_-$, which leaves $x_*$ in backward time in the direction $-p$, stays in the order interval $\{0<x<x_*\}$. Each of its coordinates is strictly decreasing in $\tau$, and it converges to $0$. So $\Gamma_-$ is a heteroclinic orbit $0\to x_*$ of (3.1): this is $\kappa$.
- The branch $\Gamma_+$ is strictly increasing in $\tau$ and unbounded, so it is not contained in $W^u(0)$.

*Proof.* The stable manifold $W^s_\Sigma(x_*)$ of (3.1) is the unstable manifold of $x_*$ for the backward flow. It is tangent to $p$, and $DF_b(x_*)p=\mu p$. At a point $x=x_*\pm\varepsilon p+O(\varepsilon^2)$ we get $F_b(x)=\pm\mu\varepsilon p+O(\varepsilon^2)$. For small $\varepsilon$ this has all entries $>0$ on $\Gamma_+$ and all entries $<0$ on $\Gamma_-$. Both points lie in $Q$, so Lemma 6.1 applies along the whole backward orbit.

On $\Gamma_-$ the backward orbit decreases and stays in $Q$, so it is bounded. It therefore exists for all $\tau\ge0$ and converges to an equilibrium in $\bar Q$ that is strictly smaller than $x_*$. That equilibrium is $0$.

On $\Gamma_+$ the backward orbit increases. If it were bounded it would converge to an equilibrium in $\bar Q$ strictly larger than $x_*$, and there is none. So it is unbounded. Since $W^u(0)$ consists of orbits converging to $0$ as $\tau\to\infty$, $\Gamma_+\not\subset W^u(0)$. ∎

*Proof of (A3)–(A4).* By Lemma 5.1 and Proposition 4.2, any heteroclinic orbit $0\to z_*$ is contained in $\Gamma_+\cup\Gamma_-$. By Proposition 6.2 it is $\Gamma_-$. So $\kappa:=\Gamma_-$ is the unique soliton up to translation, and $\kappa_j=k_j\kappa$ is the unique soliton $0\to z_*^{(j)}$.

Monotonicity holds in $\tau=-t$, which gives the increasing statement in $t$. The energy is $\mathrm{Re}\,S(0)-\mathrm{Re}\,S(z_*)=P/2$. Convergence is exponential: with rate $\ge m$ as $t\to-\infty$ (since $0$ is a source of (3.1) with eigenvalues $a,b,M$) and with rate $\mu$ as $t\to+\infty$. ∎

*Remark (Picard–Lefschetz and dimension count).* In $\{\mathrm{Im}\,S=0\}$, which has dimension 5, we have $\dim W^u(0)+\dim W^s(z_*)-5=1$. So solitons are expected to be isolated up to translation, as in the BPS soliton counts of Landau–Ginzburg models [GMW, §§10–11]. Two distinct solitons with the same endpoints would be the natural sources of $s$-dependent morphisms. Theorem (A3) shows that there is exactly one for each pair $(0,z_*^{(j)})$, *without* any genericity assumption. Since the unique intersection is transverse (Proposition 7.1), the signed soliton count is $\pm1$ for each pair. We do not determine the sign, and we do not need it.

## 7. Linearization: transversality, Fredholm and Morse–Bott properties

Along $\kappa$, write $H(t)=\mathrm{Hess}\,\mathrm{Re}\,S(\kappa(t))$. Since $D(-\nabla\mathrm{Re}\,S)=-H$, the linearization of (1.2) is $\xi'=-H\xi$, that is, $\mathcal P\xi=0$.

**Proposition 7.1.** $\mathcal P:H^1\to L^2$ is Fredholm of index $0$, with $\ker\mathcal P=\mathbb R\kappa'$ and $\ker\mathcal P^*=\mathbb R\,J\kappa'$, where $J\kappa'=-\nabla\mathrm{Im}\,S(\kappa)$.

*Proof.* $H(\pm\infty)$ are the nondegenerate Hessians at $0$ and $z_*$, each of Morse index $3$ (§3). By the index theorem of [RS] for operators $d/dt+H(t)$ with nondegenerate limits, $\mathcal P$ is Fredholm with index equal to the spectral flow of $H$, which is $n_-(H(-\infty))-n_-(H(+\infty))=0$.

*Kernel.* The isometry $\sigma$ fixes $\kappa$ pointwise and preserves $\mathrm{Re}\,S$, so $d\sigma$ commutes with $H(t)$. Hence $\xi=\xi_++\xi_-$ splits into a part tangent to $\Sigma$ and a normal part, and each part solves the equation separately.

The normal part solves $n'=(-\Lambda+K(t))n$, by the exactness of Lemma 5.1. By the estimate in the proof of Lemma 5.1, $n$ cannot tend to $0$ at $-\infty$ unless $n\equiv0$. So $\xi_-=0$.

The tangential part solves the linearization of (3.1) along $\kappa$. It decays at $+\infty$ exactly when $\xi_+(t)\in T_{\kappa(t)}W^s_\Sigma(x_*)$ for all $t$; this is the exponential-dichotomy characterization of the stable manifold. That tangent line is $\mathbb R\kappa'(t)$. Conversely, $\kappa'$ decays at both ends.

*Cokernel.* We have $\mathcal P^*=-d/dt+H$. Since $HJ=-JH$, the field $\eta=J\kappa'$ satisfies
$$\eta'=J\kappa''=-JH\kappa'=HJ\kappa'=H\eta,$$
so $\mathcal P^*\eta=0$, and $\eta\in L^2$. Index $0$ and a one-dimensional kernel give $\dim\ker\mathcal P^*=1$. ∎

**Transversality.** $\ker\mathcal P=T W^u(0)\cap TW^s(z_*)$ along $\kappa$. So $\dim(TW^u+TW^s)=3+3-1=5=\dim T\{\mathrm{Im}\,S=0\}$, using $d\,\mathrm{Im}\,S\neq0$ off critical points. The cokernel direction $J\kappa'=-\nabla\mathrm{Im}\,S$ is exactly the normal to the level set. This proves (B) for $\mathcal P$.

**The 2D Hessian.** Linearizing $\partial_sz=i\partial_tz+i\overline{\partial S}$ at an object $x$ gives $\partial_s\xi=\mathcal H_x\xi$ with $\mathcal H_x=-J\mathcal P_x=-J\partial_t-JH_x$ (here $J=i$).

- $-J\partial_t$ is self-adjoint on $H^1$, and $-JH_x$ is bounded and symmetric, because $JH_x$ is symmetric when $HJ=-JH$. So $\mathcal H_x$ is self-adjoint on $H^1$ by Kato–Rellich.
- At a constant $p$, $J\partial_t$ and $JH_p$ anticommute, so $\mathcal H_p^2=-\partial_t^2+H_p^2\ge\sigma_{\min}(H_p)^2>0$, and $\mathcal H_p$ is invertible.
- At $\kappa$, $\mathcal H_\kappa=-J\mathcal P$ is Fredholm with $\ker\mathcal H_\kappa=\ker\mathcal P=\mathbb R\kappa'=\frac{d}{d\tau}\kappa(\cdot+\tau)$. This is the Morse–Bott property claimed in (B). ∎

*Remark (grading).* Relative gradings in a flow category compare objects within one asymptotic sector, that is, with the same $t$-endpoints. By (A), the sector $(p,p)$ contains only the constant $p$, and the sector $(0,z_*^{(j)})$ contains only the translation family of $\kappa_j$. So no nontrivial relative grading arises. Since $\ker\mathcal H_\kappa\neq0$, the operator $\partial_s-\mathcal H_\kappa$ along the constant morphism of $\kappa$ is Fredholm only on weighted spaces, as usual for Morse–Bott families; we do not use this, and we do not fix an absolute grading.

## 8. Geometric consequences on $\mathrm{Sol}^4$ (proof of (C))

By §2, an object of the ansatz is precisely an $\mathbb R^3$-invariant solution of $F^+=\frac14B\times B$, $d_A^*B=0$ on $Y_4$. On $\kappa=(iu,-iv,w)$ with $u,v,w>0$ (Theorem A4) the fields are as displayed in (C). Here $B$ vanishes nowhere, because $u>0$, and $|B|^2=c_0(u^2+v^2)$ for a normalization constant $c_0>0$.

This function is strictly increasing in $x_4$ and gauge-invariant. Hence:
- the translates $\kappa(\cdot+\tau)$ are pairwise gauge-inequivalent;
- they are inequivalent to the left-invariant solutions, for which $|B|^2$ is constant;
- the four $\kappa_j$ are gauge-equivalent through constant gauge transformations $\mathrm{Ad}\exp(\pi T_k)$.

*Descent.* Lattices $\Lambda\subset\mathbb R^3$ act by translations in $(x_1,x_2,x_3)$ and preserve the coframe. So every ansatz field descends to $\Lambda\backslash Y_4\cong T^3\times\mathbb R$.

A compact quotient $\Gamma\backslash Y_4$, $\Gamma=\Lambda\rtimes\langle\gamma\rangle$, contains an element $\gamma:(x,x_4)\mapsto(\mathrm{diag}(e^{-\lambda_kT})x,\ x_4+T)$ with $T\ne0$. This $\gamma$ is an isometry fixing the coframe. A field that descends, even up to gauge, has $\Gamma$-invariant $|B|^2$, so $|B|^2(x_4+T)=|B|^2(x_4)$. This is impossible for $\kappa$.

If an object satisfies $z(t+T)=k\,z(t)$ with $k\in V_4$ (periodicity up to the residual constant gauge action), then $\mathrm{Re}\,S(z(t+T))=\mathrm{Re}\,S(z(t))$, and strict monotonicity of $\mathrm{Re}\,S$ forces $z$ to be constant. Likewise, by (A3), a *bounded* object whose gauge-invariant $|B|^2$ is $T$-periodic is one of the five constants. So the bounded ansatz objects that descend to a compact quotient are exactly the left-invariant ones, $0$ and $z_*$. The solution $z_*$ does descend, with $B\ne0$ and $F^+=\frac14B\times B$, to every compact quotient. ∎

## 9. Morphisms (proof of (D))

**Definition 9.1.** Let $\mathfrak M$ be the class of bounded smooth solutions $z:\mathbb R^2\to\mathbb C^3$ of (1.1), with $L=0$, satisfying:
1. There are maps $p_\pm:\mathbb R\to\mathrm{Crit}(S)$ such that $\sup_s|z(s,t)-p_\pm(s)|\to0$ as $t\to\pm\infty$.
2. There is $h\in L^1(\mathbb R)$ with $|z(s,t)-p_{\mathrm{sgn}\,t}(s)|+|\partial_tz(s,t)|\le h(t)$ for all $s,t$.
3. $z(s,\cdot)\to x_\pm$ in $C^1_{\rm loc}(\mathbb R)$ as $s\to\pm\infty$, where $x_\pm$ are objects (solutions of (1.2)).

**Lemma 9.2 (endpoints).** For $z\in\mathfrak M$, the maps $p_\pm$ are constant, the limits $x_\pm$ are bounded objects, and $x_\pm(t)\to p_\pm$ as $t\to\pm\infty$.

*Proof.* $p_\pm(s)$ is a uniform limit of continuous functions of $s$, so it is continuous. Its values lie in the finite set $\mathrm{Crit}(S)$, so it is constant. Uniformity in $s$ allows the limits $s\to\pm\infty$ and $t\to\pm\infty$ to be interchanged: $|x_\pm(t)-p_{\pm}|\le\sup_s|z(s,t)-p_\pm|\to0$. The objects $x_\pm$ are bounded because $z$ is. ∎

So morphisms only join objects with the same pair of $t$-endpoints. By (A3), these are the constant $p$ or the translates of a single $\kappa_j$.

**Proposition 9.3.** Every $z\in\mathfrak M$ is $s$-independent.

*Proof.* For each $s$ the action $\mathcal A(s)=\int(\sum C_k\partial_tA_k+\mathrm{Im}\,S(z))\,dt$ converges absolutely. Indeed, $|C|$ is bounded, $|\partial_tA|\le h$, and $|\mathrm{Im}\,S(z)|=|\mathrm{Im}\,S(z)-\mathrm{Im}\,S(p_\pm)|\le c\,h$, since all critical values are real.

Using the equation $z_s=iz_t+\nabla\mathrm{Im}\,S$ (`verify.py` §8),
$$\partial_s\big(C\cdot A_t+\mathrm{Im}\,S\big)=|z_s|^2+\partial_t(C\cdot A_s).$$
By the equation, $|z_s|\le|z_t|+|\partial S(z)|\le c'h(t)$, since $\partial S$ is Lipschitz on the bounded range of $z$ and vanishes at $p_\pm$. Choose $T_n\to\infty$ with $h(T_n)+h(-T_n)\to0$; this is possible since $h(T)+h(-T)\in L^1(0,\infty)$. Integrating over $[s_1,s_2]\times[-T_n,T_n]$ and letting $n\to\infty$ gives
$$\mathcal A(s_2)-\mathcal A(s_1)=\int_{s_1}^{s_2}\!\!\int|z_s|^2 .$$

By dominated convergence (domination by $c\,h$, and $C^1_{\rm loc}$ convergence), $\mathcal A(s)\to\mathcal A(x_\pm)$ as $s\to\pm\infty$. Every bounded object has $\mathcal A=0$:
- for constants, $\int\mathrm{Im}\,S(p)\,dt=0$;
- for the $\kappa_j$, which lie in $\Sigma$, we have $A_1=A_2=C_3=0$, so $C\cdot A_t=0$ identically, and $\mathrm{Im}\,S|_\Sigma=0$.

Hence $\int\!\!\int|z_s|^2=0$, so $z_s\equiv0$. ∎

This proves (D). In particular there is no morphism between distinct translates $\kappa(\cdot+\tau)$, $\kappa(\cdot+\tau')$: they have equal action, and energy is an action difference. The earlier observation that there are no left-invariant morphisms ($\mathrm{Re}\,S$ is conserved in $s$ for $t$-independent fields and separates $0$ from $z_*$) is the special case of constants.

## 10. Consistency, limitations and outlook

**Consistency with earlier rStation papers.**
- In [M25] the $V_4$ sector on $\mathbb R\times S^3\times I$ reduces to $\partial_sz+i\partial_yz=-\overline{\nabla W_c}$ with $W_c=z_1z_2z_3-\frac12\sum c_iz_i^2$. The same cubic appears here with $-c\leftrightarrow\lambda$, and the interval coordinate $y$ is replaced by the group coordinate $x_4\in\mathbb R$. There, objects are Nahm-pole solutions on an interval. Here, the unimodularity $\sum\lambda_k=0$ removes the term $-iL\,\mathrm{Im}\,z$ and allows solitons on the whole line.
- In the Sol$^3$ paper rStation math_45 [R45] the superpotential is $z_1z_2z_3-\frac\mu2(z_1^2-z_2^2)$, that is, $\lambda=(-\mu,\mu,0)$, with a line of critical points $z_1=z_2=0$. Our hypothesis $a,b>0$ excludes the degenerate case $\lambda_3=0$ precisely to obtain isolated critical points. The same kind of antiholomorphic involution cuts out an invariant slice there as here.
- Reversing the orientation of $x_4$ sends $\lambda\mapsto-\lambda$ and $S\mapsto-S\circ(-\mathrm{id})$. So the case of two negative $\lambda_k$ is the time reversal of ours: the solitons then run $z_*\to0$.

**Limitations.**
1. Everything is inside the $\mathbb R^3\rtimes V_4$ ansatz. We make no claim about transversality in directions that break the symmetry, or about non-invariant HW solutions on $\mathbb R\times\mathrm{Sol}^4$.
2. The class $\mathfrak M$ assumes uniform integrable decay in $t$. We do not prove that finite-energy solutions of (1.1) on $\mathbb R^2$ automatically satisfy it.
3. We do not define an absolute grading or a framing. With no morphisms, the Cohen–Jones–Segal realization of each sector is the sphere (or Thom space) attached to its single object, or Morse–Bott family, and it carries no information beyond that grading.
4. The non-unimodular cases ($L\neq0$, for example $\mathbb H^4$) are not treated.

**Outlook.** In this sector, nontrivial HW morphisms on $\mathrm{Sol}^4$ would need either several solitons between the same pair of vacua or broken symmetry. Theorem (A3) rules out the first inside the ansatz. The natural next step is the $\mathbb R^3$-invariant sector without the Klein symmetry. There $S$ is replaced by a function on $\mathfrak{sl}(2,\mathbb C)\otimes\mathbb C^3$, and Lemma 5.1 is no longer available.

## References

- [M25] rStation math_25 v1, https://rstation.ai/problems/math/papers/25/v1 (non-isotropic Haydys–Witten arrows on triaxial three-spheres; the $V_4$ reduction to $W_c$).
- [R45] *Kapustin–Witten solutions with corrected Nahm pole on $\mathrm{Sol}^3\times\mathbb R_+$ converging exponentially to non-trivial flat $SL(2,\mathbb C)$ connections: a sharp threshold and a monotone endpoint map*, rStation math_45 v1, https://rstation.ai/problems/math/papers/45/v1.
- [R-hw32] The complete isotropic HW flow category on $\mathbb R\times S^3\times I$ at the Anderson–Henningson fold, rStation math_46 v1, https://rstation.ai/problems/math/papers/46/v1.
- [R-hw34] The linearized HW operator at the Nahm-pole objects on $\mathrm{Sol}^3\times\mathbb R_+$ (weighted cross-section indices), rStation math_48 v1, https://rstation.ai/problems/math/papers/48/v1.
- [R-hw35] Global rigidity of the Klein-symmetric $V_4$ sector on $\mathbb R\times S^3\times I$, rStation math_49 v1, https://rstation.ai/problems/math/papers/49/v1.
- [GMW] D. Gaiotto, G. Moore, E. Witten, *Algebra of the infrared: string field theoretic structures in massive $\mathcal N=(2,2)$ field theory in two dimensions*, arXiv:1506.04087.
- [RS] J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.
- [Sm] H. L. Smith, *Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems*, Math. Surveys Monogr. 41, AMS, 1995. This is background for Lemma 6.1, whose proof here is self-contained.

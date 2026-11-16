# Weighted cross-section indices for the linearized Haydys–Witten operator at the corrected-Nahm-pole Kapustin–Witten objects on $\mathrm{Sol}^3\times\mathbb R_+$ (diagonal ansatz)

**Abstract.** We study the linearization of the Haydys–Witten (HW) equations, in the left-invariant diagonal ansatz, at the corrected-Nahm-pole Kapustin–Witten objects $x_b$, $b\le b_c$, on $\mathrm{Sol}^3\times\mathbb R_+$ constructed in rStation math_45 v1 (https://rstation.ai/problems/math/papers/45/v1). For $b<b_c$, $x_b$ converges exponentially to the flat connection $\rho_{s(b)}$ with $s>\mu$; at $b_c$ it converges algebraically to $\rho_\mu$. In this ansatz HW is the $\zeta$-instanton equation of $(\mathbb C^3,S)$, and its linearization at $x_b$ is $\partial_s-L_b$ with $L_b=J\partial_y-\mathrm{Hess\,Re}\,S(x_b)$. We prove that $L_b$ is essentially self-adjoint with domain $H^1_0$, so no boundary condition is needed at the pole; its spectrum is symmetric and its essential spectrum is $\mathbb R$. The conjugated operators $L_{b,\delta}$ (weight $e^{\delta y}$) are Fredholm iff $\delta\notin\{0,\pm(s-\mu),\pm(s+\mu)\}$, or $\delta\notin\{0,\pm2\mu\}$ at $b_c$. The pole-regular Jacobi fields are explicit quadratures, and we compute every weighted kernel. For $0<\delta<s-\mu$, $\ker L_{b,-\delta}=\mathbb R\,\partial_bx_b$ and $\mathrm{coker}\,L_{b,-\delta}=0$, while $L_{b,\delta}$ is injective. The weighted cross-section index $I_\delta(b)=\mathrm{ind}\,L_{b,-\delta}$ is half the number of asymptotic exponents in $(-\delta,\delta)$. For fixed $\delta$ it changes only where $s(b)=\mu+\delta$ or $s(b)=\delta-\mu$, never at $b_c$. Interval arithmetic ($\mu=1$) locates the walls $b_{1/2}$ and $b_{1/10}$. We do not identify $I_\delta$ with an HW relative grading; we state this as an open question. In the sector $A_s=A_y=0$, admissible solutions of the reduced equation have $s$-independent flat limits, and those between $\sigma$-symmetric objects are constant.

*Preprint, November 2026, revision r1. Not peer reviewed.*

---

## 1. Introduction

### 1.1 Context

In Witten's gauge-theoretic proposal for Khovanov-type invariants [1], Kapustin–Witten (KW) solutions on $W^3\times\mathbb R_+$ with a Nahm pole at $y=0$ play the role of critical points. Haydys–Witten (HW) instantons on $\mathbb R_s\times W^3\times\mathbb R_+$ play the role of flow lines [1, 2]. A long-term goal is a Cohen–Jones–Segal-type homotopy type [3] built from such a flow category, in the sense of Lipshitz–Sarkar [4]. For $W\neq S^3$ the flat $SL(2,\mathbb C)$ connection $\rho$ reached as $y\to\infty$ is part of the data. Any such construction needs a Fredholm theory for the linearized operators at the objects. It also needs a separate argument identifying index differences with indices of trajectory operators, as in Haydys [2, Theorem 2.28, Proposition 2.30].

This paper treats only the first, linear input, in the simplest non-product case where objects are known to exist. That case is the solvable geometry $\mathrm{Sol}^3$, whose compact quotients are the torus bundles $M_A$ with Anosov monodromy. We do not construct a grading or a flow category.

**The objects.** rStation math_45 v1 [12] studies the left-invariant diagonal ansatz on $\mathrm{Sol}^3_\mu$, $\mu>0$. With $z_k=A_k+iC_k$ ($k=1,2,3$), KW at $t=1$ becomes the holomorphic gradient flow
$$z_k'=i\,\overline{\partial_kS},\qquad S(z)=z_1z_2z_3-\tfrac\mu2(z_1^2-z_2^2). \tag{1.1}$$
In the ansatz the flat connections form the critical line $\{z_1=z_2=0\}$, and $S=0$ on it. Write $\rho_s:=(0,0,is)$, i.e. $\mathcal A=is\,dx_3T_3$. An antiholomorphic involution $\sigma$ cuts out a slice. On the slice the corrected-Nahm-pole solutions form a family $x_b$, $b\in\mathbb R$, and [12] proves the following:
- there is a sharp threshold $b_c$;
- for $b<b_c$, $x_b$ converges exponentially to $\rho_{s(b)}$, and $s:(-\infty,b_c)\to(\mu,\infty)$ is a decreasing bijection;
- $x_{b_c}$ converges algebraically to $\rho_\mu$;
- for $b>b_c$, $x_b$ blows up.

At $s=\mu$ the twisted cohomology $H^1(M_A;\mathrm{ad}\rho_s)$ jumps from $1$ to $3$, and $e^{\mu\ell}$ is a root of the Alexander polynomial of $M_A$ [12]. The reduction of the Jacobi equations along the slice to the $(R,T,\beta)$ system with $\beta''=2\zeta\beta$ is also due to [12].

**What this paper does.** We study the linearized HW operator at these objects, within the diagonal ansatz. We prove a complete weighted Fredholm theory for the cross-section operator $L_b$. We compute all weighted kernels and indices in closed form, as functions of $b$ and of the weight, and we describe exactly where the weighted indices change. Separately, for solutions of the reduced $\zeta$-instanton equation in the sector $A_s=A_y=0$, we record two energy consequences: splitting by the flat limit, and constancy between $\sigma$-symmetric objects.

### 1.2 Setting and notation

$X=(A,C)\in\mathbb R^6$ with $z=A+iC$, and $J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}$, which is multiplication by $-i$. For a path $X(y)$, $y\in(0,\infty)$, the **action** is
$$\mathrm{Acc}[X]=\int_0^\infty\mathfrak a(X)\,dy,\qquad \mathfrak a(X)=\mathrm{Re}\,S(X)+C\cdot\partial_yA. \tag{1.2}$$
Its formal $L^2$-gradient is $\mathcal G(X)=-J\partial_yX+\nabla\mathrm{Re}\,S(X)$ (Proposition 2.2). The zeros of $\mathcal G$ are exactly the solutions of (1.1). Along a solution $x$, the linearization of $\mathcal G$ is $D\mathcal G(x)=-L_x$, where
$$L_x=J\partial_y-H_x(y),\qquad H_x(y)=\mathrm{Hess}\,\mathrm{Re}\,S\,(x(y)),$$
is formally self-adjoint. The linearization of the HW (= $\zeta$-instanton) equation (2.3) at $x$ is $\partial_s-L_x$. We call $L_x$ the **cross-section operator**. We do not call it a Hessian: with our conventions the formal Hessian of $\mathrm{Acc}$ is $D\mathcal G=-L_x$. We write $L_b:=L_{x_b}$. Fix $\varphi_\delta\in C^\infty(0,\infty)$ with $\varphi_\delta=0$ on $(0,1]$ and $\varphi_\delta(y)=\delta y$ on $[2,\infty)$, and put
$$L_{b,\delta}:=e^{\varphi_\delta}L_b\,e^{-\varphi_\delta}=L_b-\varphi_\delta'J .$$
So $L_{b,\delta}$ on $L^2$ is $L_b$ acting between the weighted spaces $L^2_\delta=\{u:e^{\varphi_\delta}u\in L^2\}$. For $\delta>0$ it acts on decaying fields, and for $\delta<0$ it allows exponential growth below the rate $|\delta|$.

A **pole-regular Jacobi field** along $x_b$ is a solution $U$ of $L_bU=0$, i.e. $U'=-JH_bU$, with $U\in L^2(0,1)$. Let $\mathcal J_0(b)$ be the space of these fields. Put
$$W_\delta(b)=\{U\in\mathcal J_0(b):\ e^{\delta y}U\in L^2(1,\infty)\}.$$

### 1.3 Main theorem

Throughout, $s=s(b)$ for $b<b_c$ and $s(b_c)=\mu$.

**Theorem 1.** Let $\mu>0$ and $b\le b_c$.

**(A) The cross-section operator and its weighted indices.**
1. *(Self-adjoint realization.)* $L_b$ is essentially self-adjoint on $C^\infty_c((0,\infty);\mathbb R^6)$. Its closure has domain $H^1_0((0,\infty);\mathbb R^6)$. So at the Nahm pole no boundary condition has to be chosen: the Nahm-pole realization is the only one. The spectrum is symmetric, $\mathrm{spec}\,L_b=-\mathrm{spec}\,L_b$. Also $\ker L_b=0$ and $\mathrm{spec}_{\rm ess}L_b=\mathbb R$. In particular $L_b$ is not Fredholm on $L^2$; the zero mode $\delta z_3$ along the critical line closes the gap.
2. *(Weighted Fredholm theory.)* $L_{b,\delta}:H^1_0\to L^2$ is Fredholm if and only if $\delta\notin\Sigma_b$, where
$$\Sigma_b=\{0,\pm(s-\mu),\pm(s+\mu)\}\ \ (b<b_c),\qquad \Sigma_{b_c}=\{0,\pm2\mu\}.$$
Then $\ker L_{b,\delta}\cong W_\delta(b)$ and $\mathrm{coker}\,L_{b,\delta}\cong W_{-\delta}(b)$.
3. *(Kernels.)* $\dim\mathcal J_0(b)=3$. Under $d\sigma$ it splits into a $1$-dimensional even part, spanned by $\partial_bx_b$, and a $2$-dimensional odd part, given by explicit quadratures (Lemma 5.2). For $\delta>0$, $W_\delta(b)=0$. For $b<b_c$,
$$\dim W_{-\delta}(b)=\begin{cases}1,&0<\delta<s-\mu\quad(W_{-\delta}=\mathbb R\,\partial_bx_b),\\ 2,&s-\mu<\delta<s+\mu,\\ 3,&\delta>s+\mu.\end{cases}$$
For $b=b_c$, $\dim W_{-\delta}=2$ for $0<\delta<2\mu$ and $3$ for $\delta>2\mu$. The two fields for $0<\delta<2\mu$ are $\partial_bx_b|_{b_c}$ and one odd field. Both have polynomial growth, and both are unbounded ($\partial_bv=-\eta'\ge c\log y$; numerically $\eta\sim cy^2$).
4. *(Index.)* For $\delta>0$, $\delta\notin\Sigma_b$,
$$\mathrm{ind}\,L_{b,\delta}=-\mathrm{ind}\,L_{b,-\delta}=-\dim W_{-\delta}(b)=-\tfrac12\,\#\{\lambda\in\mathrm{spec}(-JH_\infty(s(b))):\ |\lambda|<\delta\},$$
with multiplicity, where $H_\infty(s)=\mathrm{Hess}\,\mathrm{Re}S(\rho_s)$.
5. *(Tangent kernel and endpoint map; linear statements.)* Let $b<b_c$ and $0<\delta<s-\mu$. Then $\ker L_{b,-\delta}=e^{\varphi_{-\delta}}\mathbb R\,\partial_bx_b$, the tangent line of the family $\{x_{b'}\}$, and $\mathrm{coker}\,L_{b,-\delta}=0$. Moreover $\partial_bx_b\to(0,0,i\,s'(b))$ exponentially, with $s'(b)<0$. So the asymptotic-value map sends $\ker L_{b,-\delta}$ isomorphically onto the tangent line at $\rho_{s(b)}$ of the endpoint curve $b'\mapsto\rho_{s(b')}$. With the limit fixed (weight $+\delta$), $L_{b,\delta}$ is injective of index $-1$, and its cokernel is spanned by $e^{-\varphi_\delta}\partial_bx_b$.
6. *(Weighted cross-section index and its walls.)* Put $I_\delta(b):=\mathrm{ind}\,L_{b,-\delta}=\dim W_{-\delta}(b)$ for $\delta>0$, $\delta\notin\Sigma_b$. Fix $\delta>0$.
   - If $0<\delta<2\mu$: $I_\delta(b)=1$ for $s(b)>\mu+\delta$, and $I_\delta(b)=2$ for $\mu<s(b)<\mu+\delta$ and at $b=b_c$. The only wall is $s(b_\delta)=\mu+\delta$, where $L_{b,\pm\delta}$ is not Fredholm. It lies strictly before the threshold, $b_\delta<b_c$, and $I_\delta$ does not change at $b_c$.
   - If $\delta>2\mu$: $I_\delta(b)=1,2,3$ for $s(b)>\mu+\delta$, $\delta-\mu<s(b)<\mu+\delta$ and $\mu<s(b)<\delta-\mu$ respectively, and $I_\delta(b_c)=3$. There are two walls, both before the threshold, and again no change at $b_c$.
   - The wall $b_\delta=s^{-1}(\mu+\delta)$ increases to $b_c$ as $\delta\downarrow0$. Hence $\lim_{\delta\downarrow0}I_\delta(b)=1$ for $b<b_c$ and $=2$ for $b=b_c$. Both equal $\tfrac12\dim\ker(-JH_\infty(s(b)))$, and the limit is not uniform in $b$.
   - *(Computer-assisted, $\mu=1$.)* $b_{1/2}\in(-0.2072094,-0.2072091)$, $b_{1/10}\in(-0.1567152,-0.1567148)$ and $b_c\in(-0.15460650842,-0.15460650837)$.

**(B) Reduced trajectories in the sector $A_s=A_y=0$.** Let $z$ be an admissible trajectory (Definition 7.1) from an object $x_-$ to an object $x_+$. By definition $z$ solves the $\zeta$-instanton equation (2.3). This covers two cases. In the diagonal ansatz (2.2), (2.3) is equivalent to HW, and $A_s=A_y=0$ is part of the ansatz. In the nine-component left-invariant ansatz, (2.3) is the reduction of [13, Theorem A(2)], which holds in the sector $A_s=A_y=0$. There, as [13] explains, simultaneous vanishing of $A_s$ and $A_y$ is an additional restriction, not a gauge choice when $F_{sy}\neq0$. Nothing is claimed for left-invariant HW fields outside this sector.
1. The flat limit $\rho(s)=\lim_{y\to\infty}z(s,y)$ is independent of $s$. In particular $x_-$ and $x_+$ have the same flat limit.
2. If $x_\pm$ are $\sigma$-symmetric objects, then $z$ is constant and $x_-=x_+$. This holds even if $z$ itself is not $\sigma$-symmetric.
3. The $\sigma$-symmetric objects with flat limit $\rho$ are as follows:
   - exactly one, $x_{b(s)}$, if $\rho=\rho_s$ with $s>\mu$;
   - exactly one, $x_{b_c}$, if $\rho=\rho_\mu$;
   - none for every other $\rho$, in particular for $\rho_s$ with $s<\mu$.

   About non-$\sigma$-symmetric diagonal objects only a local statement is known [12, Theorem 1.2]. A diagonal corrected-Nahm-pole solution whose trajectory under the flow (1.1) in $y$ enters and remains in the local center-stable neighbourhood of the slice family specified there is $\sigma$-symmetric, hence equal to some $x_b$. We use exactly this hypothesis and nothing stronger.

The wall $s=\mu$ is where $e^{\mu\ell}$ is the root $\lambda_A$ of the Alexander polynomial $\det(tI-A)$ of $M_A$, and where $H^1(M_A;\mathrm{ad}\rho_s)$ jumps from $1$ to $3$ [12]. Its diagonal-ansatz part jumps from $1$ to $2$, which matches the jump $2\to4$ of $\dim_{\mathbb R}\ker(-JH_\infty)$ in (A4).

**Scope.** Everything here is an ansatz-level computation; none of it is an invariant of $M_A$. Solutions outside the left-invariant ansatz are not considered. No HW relative grading, flow category or homotopy type is constructed or claimed (§6.4, §10).

### 1.4 Status of the claims

| claim | status |
|---|---|
| HW reduction in the diagonal ansatz, gradient and energy structure, $D\mathcal G=-L$ (Props. 2.1–2.3) | proved; identities checked exactly (`verify.py` A1–A3, `verify.mpl`) |
| (A1)–(A5), and (A6) except the numbers | analytic proof, using the inputs (I1)–(I5) from [12] (§3) and [11, Theorem H] |
| enclosures of $b_{1/2}$, $b_{1/10}$, $b_c$ | computer-assisted (validated interval integration, `verify.py` B; printed brackets checked to strictly contain the enclosures) |
| (B1), (B2) | analytic, for admissible solutions of the reduced equation (2.3) in the sector $A_s=A_y=0$ (Definition 7.1) |
| (B3) | from [12, Thm 1.1] (slice) and, off the slice, only the local statement [12, Thm 1.2] under its stated hypothesis |
| growth rates $s\pm\mu$, $\eta\sim y^2$ at $b_c$ | proved as stated, except $\eta\sim cy^2$ (numerical); also checked numerically (`verify.py` C) |
| relation of $I_\delta$ to an HW relative grading, spectral flow or Maslov index | **not proved**; open question (§6.4) |
| nonlinear Morse–Bott statement for $\mathrm{Acc}$ | **not claimed**; obstruction in the weighted setting explained in Remark 6.3 |

### 1.5 What is new, and relation to earlier work

The inputs come from two earlier papers. [12] supplies the family $x_b$, the threshold $b_c$, the endpoint map $s(b)$, the cohomology jump at $s=\mu$, and the $(R,T,\beta)$ reduction of the slice Jacobi equations with $\beta''=2\zeta\beta$. [13] supplies the enlarged nine-component reduction in the sector $A_s=A_y=0$ and a conditional energy-based exclusion of trajectories. In general, He [10, §§5.5–5.6] already treats exponential weights for reducible limits, including Nahm-pole boundary conditions. In particular [10, Propositions 5.10, 5.13, 5.19] includes an index-difference formula involving the kernel of the limiting extended Hessian. The hypotheses of [10] differ from the present setting, where the limits $\rho_s$ have $H^1\neq0$ on $\mathrm{Sol}$. Still, the general weighted mechanism used here is not new.

What is specific to this paper is the explicit Sol computation:
- the essential self-adjointness of $L_b$ with domain $H^1_0$ and the exact list of exceptional weights $\Sigma_b$, $\Sigma_{b_c}$;
- explicit quadratures for the pole-regular odd Jacobi fields (Lemma 5.2), $\beta=\kappa\eta$, $R=r-\kappa\int_0^yq^2\eta$, $T=r+\kappa\int_0^yp^2\eta$, built from the even field $\eta=\partial_bw$ of [12]; they make every growth rate computable;
- the complete weighted kernel table for all $b\le b_c$ and all weights (Theorem 1(A3)), including the threshold object, and the closed form $I_\delta=\frac12\#\{|\lambda|<\delta\}$;
- the exact description of the weight-dependent walls, including the fact that for each fixed weight nothing changes at $b_c$, and certified enclosures of two walls.

The weight-crossing identity $\mathrm{ind}\,L_{b,-\delta}-\mathrm{ind}\,L_{b,\delta}=\dim\ker(-JH_\infty)$ for small $\delta$ is an instance of the general mechanism of [9, 10]. Here it is verified directly from the explicit kernels.

---

## 2. The Haydys–Witten equations in the ansatz

Let $X^4=\mathbb R_s\times\mathrm{Sol}^3$, oriented by $ds\wedge f_1\wedge f_2\wedge f_3$, where $f_1=e^{\mu x_3}dx_1+e^{-\mu x_3}dx_2$, $f_2=e^{\mu x_3}dx_1-e^{-\mu x_3}dx_2$, $f_3=dx_3$ is the Milnor coframe. It satisfies $df_1=-\mu f_2\wedge f_3$, $df_2=\mu f_3\wedge f_1$ and $df_3=0$. On $X\times\mathbb R_y$ with distinguished vector field $\partial_y$, the HW equations for a connection $A$ and a self-dual $\mathfrak{su}(2)$-valued 2-form $B$ on $X$ are
$$\text{(H1)}\ \ F_X^+-\tfrac14B\times B-\tfrac12\mathcal L_yB=0,\qquad \text{(H2)}\ \ \iota_{\partial_y}F+\star_Xd_AB=0, \tag{2.1}$$
with $(B\times B)^k_{ij}=\sum\epsilon_{kab}B^a_{il}B^b_{jl}$. The normalization is the one for which $s$-independent solutions are exactly the KW solutions of [12] (see Proposition 2.1(ii)). It agrees with Haydys' equations [2] and Witten's [1, §5] up to the scaling of $B$. We take
$$A=\sum_kA_k(s,y)f_kT_k,\qquad A_s=A_y=0,\qquad B=\sum_kC_k(s,y)\,(ds\wedge f_k+f_i\wedge f_j)\,T_k, \tag{2.2}$$
with $(k,i,j)$ cyclic and $[T_i,T_j]=\epsilon_{ijk}T_k$. The form $B$ is the self-dual extension of $\phi=\sum C_kf_kT_k$. The ansatz is consistent: it is the fixed set of the Klein group of isometries of $\mathrm{Sol}$, composed with constant gauge rotations by $\pi$ (`verify.mpl` §2). In (2.2) the condition $A_s=A_y=0$ is part of the ansatz; for fields invariant under this Klein symmetry it is forced, since no nonzero vector of $\mathfrak{su}(2)$ is fixed by all three rotations. For the nine-component left-invariant ansatz of [13] the corresponding condition is an additional restriction, not a gauge choice when $F_{sy}\neq0$ (§7).

**Proposition 2.1 (reduction; `verify.py` A1, `verify.mpl` §§3–4).** For (2.2):
- $B$ and $B\times B$ are self-dual;
- the nine self-dual components of (H1) are $-\frac12R^1_k$ and identical zeros;
- the twelve components of (H2) are $R^2_k$ and identical zeros.

Here
$$R^1_k=\partial_yC_k-\partial_sA_k-\partial_{A_k}\mathrm{Re}\,S,\qquad R^2_k=\partial_yA_k+\partial_sC_k+\partial_{C_k}\mathrm{Re}\,S .$$
Equivalently, (2.1) reduces to the $\zeta$-instanton equation of the Landau–Ginzburg model $(\mathbb C^3,S)$ (cf. [5]):
$$(\partial_s+i\partial_y)z_k=-\overline{\partial_kS(z)}\quad\Longleftrightarrow\quad \partial_sX=J\partial_yX-\nabla\mathrm{Re}\,S(X). \tag{2.3}$$
(ii) Its $s$-independent solutions are exactly the solutions of (1.1).

*Proof.* This is a finite computation in the orthonormal frame $(f_1,f_2,f_3,dy,ds)$. One uses $d(f_k)$ as above, $F=dA+\frac12[A\wedge A]$, $d_AB=dB+[A\wedge B]$, the Hodge star of $X$ on 3-forms, and $\mathcal L_yB=\iota_{\partial_y}dB$, which holds because the frame is $y$-independent. Each component is a polynomial identity in $A_k,C_k$ and their first derivatives. `verify.py` A1 evaluates all 21 components symbolically and checks them against $R^1,R^2$. `verify.mpl` repeats the computation with the DifferentialGeometry package. The equivalence with the complex form uses $\overline{\partial_kS}=\partial_{A_k}\mathrm{Re}S+i\,\partial_{C_k}\mathrm{Re}S$, which holds for holomorphic $S$. For (ii), set $\partial_s=0$; this gives $A'=-\nabla_C\mathrm{Re}S$, $C'=\nabla_A\mathrm{Re}S$, i.e. $z'=i\overline{\partial S}$. $\square$

**Proposition 2.2 (gradient structure and energy; A2).** Let $\mathcal G(X)=-J\partial_yX+\nabla\mathrm{Re}S(X)$.
(i) For a static path $x$ and a variation $\xi=(\alpha,\gamma)$,
$$\frac{d}{dt}\Big|_0\mathfrak a(x+t\xi)=\langle\mathcal G(x),\xi\rangle+\partial_y(C\cdot\alpha).$$
So $\mathcal G$ is the $L^2$-gradient of $\mathrm{Acc}$ modulo boundary terms. Its linearization at $x$ is $D\mathcal G(x)=-J\partial_y+H_x=-L_x$, where $L_x=J\partial_y-H_x$ is formally self-adjoint ($J^T=-J$, $J^2=-1$, $H_x$ symmetric). Equation (2.3) reads $\partial_sX=-\mathcal G(X)$, and its linearization at a static solution $x$ is $\partial_s-L_x$. (Sign convention: we work with $L_x=-D\mathcal G(x)$ and call it the *cross-section operator*; we do not call it a Hessian. `verify.py` A2 checks $D\mathcal G=-L_x$ exactly.)
(ii) For every $C^2$ map $X(s,y)$,
$$\partial_s\mathfrak a=\langle\mathcal G(X),\partial_sX\rangle+\partial_y(C\cdot\partial_sA).$$
Hence for every solution of (2.3),
$$|\partial_sz|^2=-\partial_s\mathfrak a+\partial_y(C\cdot\partial_sA). \tag{2.4}$$

*Proof.* Direct differentiation; both identities are polynomial, and A2 checks them exactly. $\square$

Equation (2.4) uses only that $S$ is holomorphic on $\mathbb C^n$ with the flat metric. So it holds verbatim for the nine-component $\zeta$-instanton equation of [13, Theorem A(2)] (sector $A_s=A_y=0$), with $C\cdot\partial A=\sum_{ij}C_{ij}\partial A_{ij}$.

**Proposition 2.3 (the involution; A3).** Let $\sigma(z_1,z_2,z_3)=(-\bar z_2,-\bar z_1,-\bar z_3)$, with differential $d\sigma$, an orthogonal involution of $\mathbb R^6$. Then:
- $d\sigma J=-Jd\sigma$ and $\mathrm{Re}S\circ\sigma=-\mathrm{Re}S$;
- at every point of the slice $\mathrm{Fix}(\sigma)=\{z_1=a+ic,\ z_2=-a+ic,\ z_3=iv\}$ one has $d\sigma H\,d\sigma=-H$;
- hence, for every slice solution, $d\sigma L_x\,d\sigma=-L_x$ and $d\sigma L_{x,\delta}\,d\sigma=-L_{x,\delta}$;
- the action density vanishes identically on slice paths: $\mathfrak a\equiv0$, because $\mathrm{Re}S=0$ on $\mathrm{Fix}(\sigma)$ and $C\cdot A'=c\,a'-c\,a'+v\cdot0=0$. In particular $\mathrm{Acc}(x_b)=0$;
- if $z(s,y)$ solves (2.3), then so does $\sigma z(-s,y)$.

---

## 3. Inputs from rStation math_45 v1 [12]

We use the following facts, all proved in [12]. The family, the threshold, the cohomology jump and the reduction of the Jacobi equations to the $(R,T,\beta)$ system with $\beta''=2\zeta\beta$ are all due to [12]. Here $\mu>0$, $p=a+c$, $q=a-c$, $\zeta=|z_1|^2=a^2+c^2=\frac12(p^2+q^2)$, and $x_b=(a,c,v)$ on the slice.

- **(I1) Local theory** [12, §3, Prop. 3.2]. For every $b$, $x_b$ is the unique slice solution with corrected pole and $c$-coefficient $b$. Near $y=0$,
$$a=-\mu+O(y^2|\log y|),\qquad c=y^{-1}+O(y|\log y|),\qquad v=y^{-1}+O(y|\log y|),$$
and $x_b$ depends $C^1$ on $b$. Every $\sigma$-symmetric corrected-pole solution is some $x_b$.
- **(I2) Slice structure** [12, Lemma 4.1]. $p'=-(\mu+v)p$, $q'=(\mu-v)q$, $v'=-\zeta$, and $q=-pe^{2\mu y}$. Neither $p$ nor $q$ vanishes. With $P=pe^{\mu y}>0$ and $w=\log P$ one has $a=-P\sinh\mu y$, $c=P\cosh\mu y$, $v=-w'$, $w''=\cosh(2\mu y)e^{2w}$.
- **(I3) Even Jacobi field** [12, Prop. 4.4]. $\eta=\partial_bw$ solves $\eta''=2\zeta\eta$ with $\eta=y^2+o(y^2)$ and $\eta'=2y+o(y)$ as $y\to0$. On the interval of existence, $\eta>0$, $\eta'>0$ and $\eta'$ is increasing.
- **(I4) Convergent regime** [12, Thm 1.1, Lemma 4.2, Prop. 4.7]. For $b<b_c$, $v\downarrow s>\mu$, and
$$0\le v-s\le C\,e^{-2(s-\mu)y},\qquad \zeta\le C\,e^{-2(s-\mu)y}.$$
Also $\eta'\to\eta'_\infty=-s'(b)\in(0,\infty)$.
- **(I5) Threshold** [12, Prop. 4.6, Thm 1.1]. $x_{b_c}$ is global, $y(v-\mu)\to1$ and $y|z_1|\to1$. The convergent slice solutions are exactly $x_b$, $b\le b_c$; their limits are $\rho_{s(b)}$; $s(b_c)=\mu$; and $s$ is a bijection $(-\infty,b_c)\to(\mu,\infty)$. No slice pole solution converges to any other point.

(I1) and (I2) make $\partial_bx_b=(-P\eta\sinh\mu y,\ P\eta\cosh\mu y,\ -\eta')$ explicit (A6).

---

## 4. The self-adjoint operator $L_b$

**Lemma 4.1 (indicial structure; A4).** At the pole point $(i/y)(1,1,1)$, $\mathrm{Hess}\,\mathrm{Re}S=-K/y+O(1)$, where
$$K=\begin{pmatrix}0&N\\N&0\end{pmatrix},\qquad N=\mathbf 1\mathbf 1^T-I .$$
Moreover $J\partial_y+K/y=J(\partial_y+\Lambda/y)$ with $\Lambda=-JK$. Here $\Lambda$ is symmetric, $J\Lambda=-\Lambda J$, $\mathrm{spec}\,\Lambda=\{\pm1,\pm1,\pm2\}$, and $\Lambda^2+\Lambda\ge0$. Along $x_b$ (any $b$, by (I1)), $V_b:=-H_b-K/y$ is bounded and continuous on $(0,\infty)$.

*Proof.* The complex Hessian of $S$ is $S''=\begin{pmatrix}-\mu&z_3&z_2\\z_3&\mu&z_1\\z_2&z_1&0\end{pmatrix}$. For holomorphic $S$, $\mathrm{Hess}\,\mathrm{Re}S=\begin{pmatrix}\mathrm{Re}S''&-\mathrm{Im}S''\\-\mathrm{Im}S''&-\mathrm{Re}S''\end{pmatrix}$ in $(A,C)$. By (I1), $\mathrm{Re}S''$ is bounded and $\mathrm{Im}S''=N/y+O(y|\log y|)$. For $y\ge1$, $H_b$ is continuous and converges (by (I4)–(I5)). The matrix identities are exact (A4). A4 also checks the boundedness on the log series to order 4, for general $\mu$. $\square$

**Proposition 4.2 (Theorem 1(A1)).**
(i) $L_b$ is essentially self-adjoint on $C^\infty_c((0,\infty);\mathbb C^6)$, and $D(\bar L_b)=H^1_0(0,\infty)$, with $\|u'\|\le\|\bar L_bu\|+\|V_b\|_\infty\|u\|$ and $\|u/y\|\le2\|u'\|$.
(ii) $d\sigma\bar L_bd\sigma=-\bar L_b$, so $\mathrm{spec}\,L_b=-\mathrm{spec}\,L_b$.
(iii) $\mathrm{spec}_{\rm ess}\bar L_b=\mathbb R$.
(iv) $\ker\bar L_b=0$.

*Proof.* (i) Let $T_0=J(\partial_y+\Lambda/y)$. By Lemma 4.1 this is the half-line model of [11, Theorem H], with $\mathfrak h=\mathbb C^6$, $S=\Lambda$ and $\sigma_0=1>\frac12$. So $T_0$ is essentially self-adjoint, and so is $T_0+V_b$ for bounded symmetric $V_b$ ([11, Thm H(4)]: Kato–Rellich). The identity of Thm H(1) gives
$$\|T_0u\|^2=\|u'\|^2+\langle(\Lambda^2+\Lambda)u/y,u/y\rangle\ge\|u'\|^2 .$$
Hardy's inequality gives $\|T_0u\|\le\|u'\|+2\|u/y\|\le5\|u'\|$ on $C^\infty_c$. So the graph norm is equivalent to the $H^1$ norm, and the closure has domain $H^1_0$. Adding $V_b$ does not change the domain.

(ii) This is Proposition 2.3.

(iii) Let $\lambda\in\mathbb R$. The $z_3$-rows and columns of $H_\infty=\mathrm{Hess}\,\mathrm{Re}S(\rho_s)$ vanish (A5). Take $v\in\mathbb C^6$ in the $z_3$-block with $i\lambda Jv=\lambda v$; such $v$ exists, since $iJ$ restricted to that block has eigenvalues $\pm1$. Put
$$u_n=n^{-1/2}\chi((y-n^2)/n)\,e^{i\lambda y}v .$$
Then $\|(L_b-\lambda)u_n\|\le C/n+\sup_{y\ge n^2-n}|H_b(y)-H_\infty|\cdot\|u_n\|\to0$, while $\|u_n\|$ is constant and $u_n\rightharpoonup0$. So $\lambda\in\mathrm{spec}_{\rm ess}$.

(iv) By Lemma 5.3 below, $W_0(b)=0$: no nonzero pole-regular Jacobi field is in $L^2$. $\square$

So $0\in\mathrm{spec}_{\rm ess}L_b$ for every object. This comes from the zero mode $\delta z_3\in\mathbb C$ along the critical line $\{z_1=z_2=0\}$ of $S$, propagated to $y=\infty$. The same phenomenon at genuine Nahm-pole ends on $S^1\times\Sigma\times\mathbb R^+$ led [16] to ask for exponential weights; exponential weights for reducible limits with Nahm-pole boundary conditions are treated in generality by He [10, §§5.5–5.6]. We now carry this out explicitly for the operators $L_b$.

**Proposition 4.3 (weighted Fredholm theory; Theorem 1(A2)).** Let $\delta\in\mathbb R$.
(i) $L_{b,\delta}:H^1_0\to L^2$ is Fredholm if and only if $\delta\notin\Sigma_b$.
(ii) $\ker L_{b,\delta}=e^{\varphi_\delta}W_\delta(b)$.
(iii) $\mathrm{coker}\,L_{b,\delta}\cong\ker L_{b,-\delta}$.

*Proof.* *The model at infinity.* The eigenvalues of $-JH_\infty$, the linearized KW flow at $\rho_s$, are real (A5):
- $\{0,0,\pm(s+\mu),\pm(s-\mu)\}$ for $s\ne\mu$, with a 2-dimensional kernel;
- $\{0,0,0,0,\pm2\mu\}$ at $s=\mu$, with a semisimple 4-dimensional kernel.

Let $T_\infty=J(\partial_y-\delta)-H_\infty$ on $\mathbb R$. Then $T_\infty u=f$ means $u'=(\delta-JH_\infty)u-Jf$. If $\delta\notin\Sigma_b$, the matrix $\delta-JH_\infty$ has no eigenvalue on $i\mathbb R$, and Fourier transform shows that $T_\infty:H^1(\mathbb R)\to L^2(\mathbb R)$ is an isomorphism.

*Parametrix.* Let $R\ge3$, choose cutoffs $\chi_0+\chi_\infty=1$ with $\chi_0=1$ on $(0,R]$ and $\mathrm{supp}\,\chi_0\subset(0,R+1)$, and choose $\psi_0,\psi_\infty$ equal to $1$ on the supports of $\chi_0,\chi_\infty$, supported in $(0,R+2)$ and $[R-1,\infty)$ respectively. Put
$$Pf=\psi_0(\bar L_b-i)^{-1}(\chi_0f)+\psi_\infty T_\infty^{-1}(\chi_\infty f).$$
By Proposition 4.2(i), $(\bar L_b-i)^{-1}:L^2\to H^1_0$ is bounded. On $\mathrm{supp}\,\psi_\infty$ we have $\varphi'_\delta=\delta$, so $L_{b,\delta}=T_\infty+(H_\infty-H_b)$ there. A direct computation gives
$$L_{b,\delta}P=I+J\psi_0'(\bar L_b-i)^{-1}\chi_0+\psi_0(i-\varphi'_\delta J)(\bar L_b-i)^{-1}\chi_0+J\psi_\infty'T_\infty^{-1}\chi_\infty+\psi_\infty(H_\infty-H_b)T_\infty^{-1}\chi_\infty .$$
The first three correction terms are compact: each is multiplication by a bounded function with support in a bounded interval, composed with a bounded map $L^2\to H^1$, and Rellich's theorem applies. The last term is compact because $H_b(y)\to H_\infty$ as $y\to\infty$: it is the norm limit of the same operators with $H_\infty-H_b$ cut off at large $y$. The same expansion applied to $PL_{b,\delta}$ gives a left parametrix. So $L_{b,\delta}$ is Fredholm.

*Non-Fredholm weights.* If $\delta\in\Sigma_b$, then $\delta=-\lambda$ for a real eigenvalue $\lambda$ of $-JH_\infty$, with real eigenvector $v$. Then $u_n=n^{-1/2}\chi((y-n^2)/n)v$ is bounded in $H^1$, weakly null, has $\|u_n\|$ constant, and satisfies $L_{b,\delta}u_n\to0$. This is incompatible with an estimate $\|u\|_{H^1}\le C(\|L_{b,\delta}u\|+\|Ku\|)$ with $K$ compact, which every Fredholm operator satisfies.

*(ii)* If $u\in H^1_0$ and $L_{b,\delta}u=0$, then $U=e^{-\varphi_\delta}u$ solves $L_bU=0$, is in $L^2(0,1)$, and has $e^{\delta y}U\in L^2(1,\infty)$. Conversely, let $U\in W_\delta$. By Lemma 5.2, $U=O(y)$ and $U'=O(1)$ near $0$. Also $(e^{\varphi_\delta}U)'=\varphi_\delta'e^{\varphi_\delta}U-JH_be^{\varphi_\delta}U\in L^2$ near $\infty$. So $e^{\varphi_\delta}U\in H^1_0$.

*(iii)* $\bar L_b$ is self-adjoint, and $\varphi'_\delta J$ is bounded and skew. So $L_{b,\delta}^*=\bar L_b+\varphi_\delta'J=L_{b,-\delta}$, with the same domain. The range is closed, hence $\mathrm{coker}\cong\ker L_{b,\delta}^*$. $\square$

*Remark 4.4 (ODE count).* The index can be cross-checked with the count for ODE operators with exponential dichotomies (Palmer [6]):
$$\mathrm{ind}=\dim\mathcal J_0+\dim S_\delta-6,$$
where $S_\delta$ is the stable space of $-JH_\infty$ at weight $\delta$. `verify.py` A7 confirms that this agrees with Theorem 1(A4) on all sample weights. We do not use it in the proofs.

---

## 5. Pole-regular Jacobi fields and their growth

**Lemma 5.1 (isotropy).** Let $\omega(U_1,U_2)=\langle JU_1,U_2\rangle$. For any two solutions of $L_bU=0$, $\omega$ is constant in $y$. If $U_1,U_2\in\mathcal J_0(b)$ (real), then $\omega(U_1,U_2)=0$. Hence $\dim\mathcal J_0(b)\le3$.

*Proof.* Constancy follows from $JU'=H_bU$ and the symmetry of $H_b$. Let $\chi\in C^\infty_c[0,1)$ with $\chi=1$ near $0$. Then $\chi U_j\in L^2$ and $L_b(\chi U_j)=J\chi'U_j\in L^2$, so $\chi U_j\in D(L_b^*)=D(\bar L_b)$ (Proposition 4.2(i)). Symmetry of $\bar L_b$ gives
$$0=\langle J\chi'U_1,\chi U_2\rangle-\langle\chi U_1,J\chi'U_2\rangle=\omega(U_1,U_2)\int_0^\infty(\chi^2)'\,dy=-\omega(U_1,U_2).$$
An isotropic subspace of the 6-dimensional symplectic space $(\mathbb R^6,\omega)$ has dimension at most $3$. $\square$

**Lemma 5.2 (explicit regular fields; A6).** Let $b\le b_c$, so that $x_b$ is global. Write an odd Jacobi field as $\delta z_1=\alpha+i\gamma$, $\delta z_2=\overline{\delta z_1}$, $\delta z_3=\beta\in\mathbb R$, and put $R=q(\alpha+\gamma)$ and $T=p(\alpha-\gamma)$. The odd Jacobi equations are equivalent to
$$R'=-q^2\beta,\qquad T'=p^2\beta,\qquad \beta'=T-R .$$
Their pole-regular solutions are exactly
$$U_{\kappa,r}:\quad \beta=\kappa\eta,\qquad R=r-\kappa\int_0^yq^2\eta,\qquad T=r+\kappa\int_0^yp^2\eta,\qquad(\kappa,r)\in\mathbb R^2 .$$
Hence $\mathcal J_0(b)=\mathbb R\,\partial_bx_b\oplus\{U_{\kappa,r}\}$, $\dim\mathcal J_0=3$, and every $U\in\mathcal J_0$ satisfies $U=O(y)$, $U'=O(1)$ as $y\to0$.

*Proof.* The odd equations are an exact consequence of the Jacobi equation and (I2) (A6; [12, Lemma 5.1]).

*$U_{\kappa,r}$ solves them.* The integrands are bounded near $0$, since $p=y^{-1}+O(1)$ and $q=-y^{-1}+O(1)$ (A6), and $\eta=O(y^2)$. Also
$$T-R=\kappa\int_0^y2\zeta\eta=\kappa\int_0^y\eta''=\kappa\eta',$$
using $\eta'(0^+)=0$ (I3).

*They are regular.* $R$ and $T$ are bounded near $0$, so $\alpha\pm\gamma=R/q,\ T/p=O(y)$, and $\beta=O(y^2)$.

*Dimension count.* The even field $\partial_bx_b$ is regular by (I1) and (I3). The three fields $\partial_bx_b$, $U_{1,0}$, $U_{0,1}$ are independent: the first is even and the others odd, and $U_{1,0}$ has $\beta\ne0$ while $U_{0,1}$ has $\beta=0$, $R=T=1$. With Lemma 5.1, $\dim\mathcal J_0=3$, and the decomposition follows. The bound $U'=O(1)$ follows from $U'=-JH_bU$ with $|H_b|=O(1/y)$. $\square$

**Lemma 5.3 (growth classes; Theorem 1(A3)).**
(i) Let $b<b_c$ and $\epsilon=s-\mu>0$. Put
$$R_\infty=r-\kappa\int_0^\infty q^2\eta,\qquad T_\infty=r+\kappa\int_0^\infty p^2\eta,$$
which are finite. The map $(\kappa,r)\mapsto(R_\infty,T_\infty)$ is injective. As $y\to\infty$:
- $\partial_bx_b\to(0,0,is'(b))\ne0$ exponentially;
- for $U_{\kappa,r}$: $|\alpha+\gamma|\asymp e^{\epsilon y}$ if $R_\infty\ne0$, and $|\alpha+\gamma|=O(ye^{-\epsilon y})$ if $R_\infty=0$;
- $|\alpha-\gamma|\asymp e^{(s+\mu)y}$ if $T_\infty\ne0$, and $|\alpha-\gamma|=O(ye^{-(s+\mu)y})$ if $T_\infty=0$;
- $\beta=\kappa\eta$ with $\eta\sim\eta'_\infty y$.

(ii) Let $b=b_c$. $T_\infty$ is finite and is a nonzero functional on the odd part. If $T_\infty\ne0$, then $|\alpha-\gamma|\ge c\,e^{2\mu y}y^{1/2}$ for large $y$. If $T_\infty=0$, the field is $O(y^m)$ for some $m$. Also $\partial_bx_b$ is $O(y^m)$, and $\eta'\ge c\log y\to\infty$.

(iii) Consequently $W_\delta(b)=0$ for $\delta>0$, and $\dim W_{-\delta}(b)$ is as in Theorem 1(A3).

*Proof.* (i) *Rates of $p,q$.* By (I2) and (I4),
$$|q(y)|=|q(1)|\exp\Big(-\int_1^y(v-\mu)\Big)=|q(1)|\,e^{-\epsilon(y-1)}\,e^{-\int_1^y(v-s)},$$
and $\int_1^\infty(v-s)<\infty$. So $|q|\asymp e^{-\epsilon y}$, and similarly $|p|\asymp e^{-(s+\mu)y}$.

*Rate of $\eta$.* By (I3)–(I4), $\eta'\uparrow\eta'_\infty<\infty$, so $\eta\le Cy$. Also $\eta'_\infty-\eta'=\int_y^\infty2\zeta\eta=O(ye^{-2\epsilon y})$.

*Limits of $R,T$.* $q^2\eta,\ p^2\eta=O(ye^{-2\epsilon y})$, so $R_\infty$ and $T_\infty$ exist, with $|R-R_\infty|,|T-T_\infty|=O(ye^{-2\epsilon y})$. This gives the stated rates for $R/q$ and $T/p$ when the limits vanish. For $T/p$ one uses the sharper $|T-T_\infty|=\kappa\int_y^\infty p^2\eta=O(ye^{-2(s+\mu)y})$.

*Injectivity.* If $R_\infty=T_\infty=0$, then $\kappa\int_0^\infty(p^2+q^2)\eta=\kappa\eta'_\infty=0$. So $\kappa=0$, and then $r=0$.

*The even field.* $|\partial_b(a,c)|\le2P\eta\cosh\mu y\le2\eta|z_1|=O(ye^{-\epsilon y})$, since $P^2\cosh^2\mu y\le P^2\cosh2\mu y=\zeta$. Also $\partial_bv=-\eta'\to s'(b)=-\eta'_\infty<0$.

(ii) *Asymptotics.* By (I5), $\log|q(y)|=-\log y+o(\log y)$ and $\log|p(y)|=-2\mu y-\log y+o(\log y)$, as in (i). Also $\zeta\le k/y^2$ on $[Y_0,\infty)$, with $k=2$.

*Polynomial bound for $\eta$.* Put $\upsilon=y\eta'/\eta>0$. Then
$$\upsilon'=\frac{\upsilon-\upsilon^2}{y}+y\frac{\eta''}{\eta}\le\frac{\upsilon-\upsilon^2+2k}{y}.$$
So $\upsilon\le\max(\upsilon(Y_0),r_k)$, where $r_k$ is the positive root of $r^2-r-2k$. Hence $\eta\le Cy^m$ and $\eta'\le Cy^{m-1}$.

*Limit of $T$.* $p^2\eta\le Ce^{-4\mu y}y^{m}$, so $T_\infty$ exists and $|T-T_\infty|\le Ce^{-4\mu y}y^m$. If $T_\infty\ne0$, then $|T/p|\ge c\,e^{2\mu y}y^{1-o(1)}$. If $T_\infty=0$, then $|T/p|=O(e^{-2\mu y}y^{m+2})$.

*The other components.* $R=r-\kappa\int_0^yq^2\eta=O(y^m)$, so $R/q=O(y^{m+2})$, and $\beta=\kappa\eta=O(y^m)$. The functional $T_\infty$ is nonzero, since $T_\infty(U_{0,1})=1$. The even field has components $P\eta\cosh\mu y$, $P\eta\sinh\mu y\le\eta|z_1|=O(y^{m-1})$ and $\eta'$, so it is polynomial. Finally $\zeta\ge1/(2y^2)$ for large $y$, by (I5), and $\eta\ge\eta'(1)(y-1)$. Hence $\eta''=2\zeta\eta\ge c/y$, and so $\eta'\ge c\log y$.

(iii) *Weighted classes.* Since $d\sigma$ is constant and orthogonal, $e^{\delta y}U\in L^2$ if and only if the even and odd parts of $U$ both have this property.

*Case $\delta>0$.* The even part must vanish, because $\partial_bv\not\to0$ in (i), and $\eta'\ge\eta'(1)>0$ in (ii). The odd part needs $\kappa=0$, because $\beta=\kappa\eta\ge\kappa\eta'(1)(y-1)$ in both regimes. Then $R=T=r$ is constant, and $\alpha+\gamma=r/q$ grows (like $e^{\epsilon y}$, respectively like $y^{1-o(1)}$), so $r=0$.

*Case $-\delta<0$, $b<b_c$.* By (i), an odd $U_{\kappa,r}$ lies in $W_{-\delta}$ iff:
- $R_\infty=T_\infty=0$ when $\delta<\epsilon$;
- $T_\infty=0$ when $\epsilon<\delta<s+\mu$;
- always, when $\delta>s+\mu$.

The even field is bounded, so it always lies in $W_{-\delta}$. Injectivity gives the dimensions $1,2,3$.

*Case $-\delta<0$, $b=b_c$.* By (ii), $U_{\kappa,r}\in W_{-\delta}$ iff $T_\infty=0$ (for $\delta<2\mu$), and always for $\delta>2\mu$. The even field is polynomial. This gives $2$ and $3$. $\square$

*Proof of Theorem 1(A1)–(A4).* (A1) is Proposition 4.2, with $\ker\bar L_b\cong W_0=0$ by Lemma 5.3(iii): for $\delta=0$ the argument of the case $\delta>0$ applies verbatim. (A2) is Proposition 4.3. (A3) is Lemmas 5.2–5.3. For (A4), $\mathrm{ind}\,L_{b,\delta}=\dim W_\delta-\dim W_{-\delta}$ by Proposition 4.3(ii)–(iii); the closed form in terms of the asymptotic exponents is Corollary 6.1. $\square$


---

## 6. Weighted cross-section indices, walls and the tangent kernel

### 6.1 Closed form of the index

**Corollary 6.1 (Theorem 1(A4)).** For $\delta>0$, $\delta\notin\Sigma_b$,
$$\mathrm{ind}\,L_{b,-\delta}=\dim W_{-\delta}(b)=\tfrac12\,\#\{\lambda\in\mathrm{spec}(-JH_\infty(s(b))):|\lambda|<\delta\},\qquad \mathrm{ind}\,L_{b,\delta}=-\mathrm{ind}\,L_{b,-\delta}.$$
In particular, for $0<\delta<\min\Sigma_b\cap(0,\infty)$,
$$\mathrm{ind}\,L_{b,-\delta}-\mathrm{ind}\,L_{b,\delta}=\dim\ker(-JH_\infty(s(b)))\in\{2,4\}.$$

*Proof.* By Proposition 4.3(ii)–(iii) and Lemma 5.3(iii), $\mathrm{ind}\,L_{b,-\delta}=\dim W_{-\delta}-\dim W_\delta=\dim W_{-\delta}$, and $\mathrm{ind}\,L_{b,\delta}=-\dim W_{-\delta}$. The spectrum of $-JH_\infty$ (proof of Proposition 4.3) is $\{0,0,\pm(s-\mu),\pm(s+\mu)\}$ for $b<b_c$. The number of eigenvalues with $|\lambda|<\delta$ is therefore $2,4,6$ on the three intervals of Theorem 1(A3). At $b_c$ the spectrum is $\{0^4,\pm2\mu\}$, which gives $4,6$. Halving gives the table of (A3). `verify.py` A7 checks the identity on a grid of $(s,\delta)$, including $s=\mu$. $\square$

This is the expected weight-crossing behaviour for a formally self-adjoint operator whose limiting operator has semisimple kernel (compare [9] and, for Nahm-pole problems with reducible limits, [10, §§5.5–5.6]). The content specific to $\mathrm{Sol}$ is that the kernels are computed explicitly and that the threshold object is included.

### 6.2 Proof of Theorem 1(A5): the tangent kernel and the endpoint map

Let $b<b_c$ and $0<\delta<s-\mu$. By (A3), $\ker L_{b,-\delta}=e^{\varphi_{-\delta}}\mathbb R\,\partial_bx_b$ and $\mathrm{coker}\,L_{b,-\delta}\cong W_\delta=0$. The family $\{x_{b'}\}$ consists of zeros of $\mathcal G$, and it is $C^1$ in $b'$ by (I1), so $\partial_bx_b$ is its tangent vector. By Lemma 5.3(i), $\partial_bx_b\to(0,0,is'(b))$ exponentially, and $s'(b)=-\eta'_\infty<0$ by (I4). So the asymptotic-value map $U\mapsto\lim_{y\to\infty}U(y)$ is defined on $W_{-\delta}(b)$ and is injective there. Its image is the tangent line of the endpoint curve $b'\mapsto\rho_{s(b')}$ inside the critical line. With the limit fixed, i.e. at weight $+\delta$, $\ker L_{b,\delta}=W_\delta=0$ and $\mathrm{coker}\,L_{b,\delta}\cong\ker L_{b,-\delta}$, which is one-dimensional. $\square$

These are statements about linear operators only. Remark 6.3 explains why we do not deduce from them a nonlinear Morse–Bott statement for $\mathrm{Acc}$.

### 6.3 Proof of Theorem 1(A6): walls of the weighted index

Fix $\delta>0$. By Corollary 6.1, $I_\delta(b)$ is locally constant in $b$ away from the set where $\delta\in\Sigma_b$, i.e. where $s(b)-\mu=\delta$ or $s(b)+\mu=\delta$ (for $b<b_c$), or $\delta=2\mu$ (at $b_c$). Since $s$ is a decreasing bijection $(-\infty,b_c)\to(\mu,\infty)$ (I5), the equation $s(b)=\mu+\delta$ has exactly one solution $b_\delta<b_c$, for every $\delta>0$. The equation $s(b)=\delta-\mu$ has a solution, necessarily unique and $<b_c$, if and only if $\delta>2\mu$. The values follow by evaluating $\tfrac12\#\{|\lambda|<\delta\}$:
- for $s>\mu+\delta$ only the double eigenvalue $0$ counts, so $I_\delta=1$;
- for $|s-\mu|<\delta<s+\mu$ the values $\pm(s-\mu)$ also count, so $I_\delta=2$;
- for $s+\mu<\delta$ all six count, so $I_\delta=3$.

At $b_c$, $I_\delta=2$ for $\delta<2\mu$ and $3$ for $\delta>2\mu$. As $b\uparrow b_c$, $s\downarrow\mu$, so for fixed $\delta\neq2\mu$ the value for $b$ close to $b_c$ is $2$ if $\delta<2\mu$ and $3$ if $\delta>2\mu$. These are the values at $b_c$. So $I_\delta$ does not change at $b_c$ for any fixed weight. Finally $b_\delta=s^{-1}(\mu+\delta)\uparrow b_c$ as $\delta\downarrow0$, because $s^{-1}$ is decreasing with $s^{-1}(\mu^+)=b_c$. Hence $\lim_{\delta\downarrow0}I_\delta(b)$ is $1$ for $b<b_c$ and $2$ at $b_c$, and the limit is not uniform in $b$.

The enclosures are `verify.py` B5. The certified enclosures of $s$ at the two endpoints of each stated $b$-interval lie strictly above, respectively below, $1+\delta$. With strict monotonicity of $s$ this locates $b_\delta$ (§8). $\square$

**Remark 6.2 (the odd field responsible for the wall).** Along the family, the odd pole-regular field with $T_\infty=0$ grows like $e^{(s-\mu)y}$. It enters $W_{-\delta}$ exactly when $\delta$ passes $s-\mu$. At $b_c$ it grows only polynomially, so it lies in $W_{-\delta}$ for every $\delta>0$. The extra asymptotic zero modes at $s=\mu$ match the cohomology jump: $\ker(-JH_\infty)$ has real dimension $2$ for $s\neq\mu$ and $4$ at $s=\mu$. Equivalently, $\ker_{\mathbb C}S''(\rho_s)$ has complex dimension $1$, respectively $2$. And $\ker_{\mathbb C}S''(\rho_s)$ is exactly the diagonal part of $H^1_{\rm Lie}(\mathfrak{sol};\mathrm{ad}\rho_s)$, whose total dimension is $1$, respectively $3$ (A8). This is a statement about the asymptotic operator and the small-weight limit only. For a fixed weight the index at $b_c$ is the limit of the indices at $b<b_c$ (§6.3). At $b_c$ no nonzero element of $W_{-\delta}(b_c)$ is bounded. Indeed, the $\delta A_3$-component $\beta=\kappa\eta$ comes only from the odd part, and $\eta\to\infty$. The $\delta C_3$-component $-\eta'$ comes only from the even part, and $\eta'\ge c\log y$ (Lemma 5.3(ii)). So boundedness forces $\kappa=0$ and a vanishing even part. Then $R=T=r=T_\infty=0$. Numerically $\eta\sim cy^2$ (`verify.py` C2). So no extended-$L^2$ description in the sense of [7] is available at $b_c$.

**Remark 6.3 (why no nonlinear Morse–Bott statement is made).** The linear facts of (A5) say that, on $H^1_0$ with weight $-\delta$, the kernel of $L_{b,-\delta}$ is the tangent line of the family and the operator is onto. They do not make $\{x_b\}$ a Morse–Bott critical manifold of $\mathrm{Acc}$ in this functional setting. The reason is that the nonlinear map $\mathcal G$ does not even send a neighbourhood of $x_b$ in $x_b+e^{-\varphi_{-\delta}}H^1_0$ into the target $e^{-\varphi_{-\delta}}L^2$.

Let $\chi$ vanish near the pole and equal $1$ for large $y$, choose $\delta/2<a<\delta$, and take the real perturbation with complex components
$$u_1=u_2=\varepsilon\chi(y)e^{ay},\qquad u_3=0 .$$
Then $e^{-\delta y}u\in H^1$ near infinity, and its norm is $O(\varepsilon)$. Since $\mathrm{Re}\,S$ is a cubic polynomial, $\nabla\mathrm{Re}S(x+u)-\nabla\mathrm{Re}S(x)-H_xu=\nabla\mathrm{Re}(u_1u_2u_3)$. The $A_3$-component of this remainder is $\mathrm{Re}(u_1u_2)=\varepsilon^2\chi^2e^{2ay}$, and
$$e^{-\delta y}\,\mathrm{Re}(u_1u_2)=\varepsilon^2e^{(2a-\delta)y}\notin L^2(1,\infty).$$
(`verify.py` A9 checks the remainder identity and the two integrability statements for $a=3/4$, $\delta=1$.) A nonlinear Morse–Bott or implicit-function statement would need a different functional setting. One option is the positively weighted space with an explicit asymptotic parameter $\rho_s$ (an extended weighted space), together with a differentiable action or section on it and a normal nondegeneracy argument. We do not set this up. Equally, the linear statements are not used to define gradings.

### 6.4 Relation to an HW relative grading: an open question

The integer $I_\delta(b)$ is the index of a weighted cross-section operator. We do **not** claim that differences $I_\delta(b_1)-I_\delta(b_2)$ are indices of HW trajectory operators, spectral flows or relative Maslov indices. Three facts show that such a claim would need more than what is proved here.
- The unweighted $L_b$ has essential spectrum $\mathbb R$, and the conjugated operators $L_{b,\delta}$ are not self-adjoint. So the usual spectral-flow argument is not supplied by Proposition 4.3. Haydys [2] proves Fredholmness of the trajectory operator in his setting (Theorem 2.28). He then identifies its index with a relative Maslov index (Proposition 2.30), and both steps are needed. Neither is carried out here.
- For a fixed weight $\delta\in(0,2\mu)$, $I_\delta$ changes from $1$ to $2$ at $s=\mu+\delta$, strictly before the threshold. It is already $2$ on an interval of objects with $b<b_c$, and it remains $2$ at $b_c$ (Theorem 1(A6)). So for a fixed weight it is neither constant on $b<b_c$ nor does it jump at $b_c$.
- The distinction between $b<b_c$ and $b_c$ appears only in the small-weight limit taken separately at each object. Nothing here justifies that prescription as a relative grading across different flat-limit sectors. By Theorem 1(B1), no reduced trajectory connects objects with different flat limits.

**Open question 6.4.** Is there a Fredholm setting for the HW trajectory operator $\partial_s-L(s)$ along paths of corrected-Nahm-pole configurations, with suitable weights or asymptotic parameters at $y=\infty$, in which the index is a relative Maslov index? Here the relevant Lagrangians would be the pole-regular space $\mathcal J_0(b)\subset(\mathbb R^6,\omega)$, which is Lagrangian by Lemmas 5.1–5.2, and asymptotic subspaces at $y=\infty$. Does $I_\delta$ compute this index for some choice of $\delta$ depending on the endpoints? Lemma 5.3 describes $\mathcal J_0(b)$ in terms of the eigenspaces of $-JH_\infty$, which is suggestive. We leave the question open.

**Scaling.** For general $\mu$, $b_\delta(\mu)=\mu^2\big(b_{\delta/\mu}(1)+\frac23\log\mu\big)$. This follows from the scaling $z\mapsto\lambda z(\lambda y)$ of [12, Prop. 2.1].

---

## 7. Reduced trajectories: splitting by the flat limit and constancy between $\sigma$-objects

We work with the $\zeta$-instanton equation (2.3) for a holomorphic $S$ on $\mathbb C^n$. This covers two cases:
- $n=3$, the diagonal ansatz (Proposition 2.1), where $A_s=A_y=0$ is part of the ansatz (2.2);
- $n=9$, all left-invariant components, with $S=\det Z-\frac\mu2\sum_j(Z_{1j}^2-Z_{2j}^2)$. Here (2.3) is the reduction of [13, Theorem A(2)], valid for left-invariant HW fields with $A_s=A_y=0$; such fields solve (2.3) and also a Gauss law, which we do not need. As [13] explains, simultaneous vanishing of $A_s$ and $A_y$ is an additional restriction. It is not a gauge choice when $F_{sy}\neq0$. All statements of this section are about solutions of (2.3), so for $n=9$ they concern only this sector.

In both cases the critical points of $S$ are the left-invariant flat connections of the respective ansatz, and $S=0$ at all of them ([12, Prop. 2.2] for $n=3$; [13] for $n=9$). An **object** is a solution $x$ of $x'=i\overline{\partial S(x)}$ on $(0,\infty)$ with the corrected Nahm pole and a limit $\rho(x)=\lim_{y\to\infty}x(y)$. Such a limit is critical: otherwise $x'\to i\overline{\partial S(\rho)}\ne0$.

An energy-based exclusion of trajectories, under its own hypotheses, is already given in [13]. Propositions 7.2–7.3 are included because they are stated under the explicit hypotheses (T1)–(T3) below and because (B1) is used in §6.4.

**Definition 7.1 (admissible trajectory).** An admissible trajectory from $x_-$ to $x_+$ is a smooth solution $z:\mathbb R\times(0,\infty)\to\mathbb C^n$ of (2.3) such that:
- **(T1)** $z(s,y)\to x_\pm(y)$ for each $y$ as $s\to\pm\infty$, and $\|\mathfrak a(z(s,\cdot))-\mathfrak a(x_\pm)\|_{L^1(0,\infty)}\to0$;
- **(T2)** there is $\rho:\mathbb R\to\mathbb C^n$ with $\sup_{s\in\mathbb R}|z(s,y)-\rho(s)|\to0$ as $y\to\infty$;
- **(T3)** for every compact $K\subset\mathbb R$, $\sup_{s\in K}|C\cdot\partial_sA|(s,y)\to0$ as $y\to0$ and as $y\to\infty$.

*Remarks.* (T3) at the pole holds whenever $|C|=O(1/y)$ and $|\partial_sA|=o(y)$, locally uniformly in $s$. This is the behaviour of pole-regular variations: by Lemma 5.2 and the indicial roots, their $A$-components are $O(y^2)$. (T2) is uniform convergence at the far end. (T1) is the standard finite-action convergence to the ends. For $\sigma$-symmetric $x_\pm$ it says $\|\mathfrak a(z(s,\cdot))\|_{L^1}\to0$, by Proposition 2.3. Smoothness is automatic for $C^1$ solutions, by elliptic regularity for $\partial_{\bar w}$, $w=s+iy$.

**Proposition 7.2 (splitting; Theorem 1(B1)).** For an admissible trajectory, $\rho$ is constant and equals $\rho(x_-)=\rho(x_+)$.

*Proof.* $\rho$ is continuous, as a uniform limit. Put $m_Y(s)=\int_Y^{Y+1}z(s,y)\,dy$. By (2.3),
$$m_Y'(s)=-i\big(z(s,Y+1)-z(s,Y)\big)-\int_Y^{Y+1}\overline{\partial S(z(s,y))}\,dy .$$
As $Y\to\infty$, $m_Y\to\rho$ uniformly, and the right side tends to $-\overline{\partial S(\rho(s))}$ uniformly on compacts. This uses (T2) and the uniform continuity of $\partial S$ on bounded sets. Hence $\rho\in C^1$ and $\rho'=-\overline{\partial S(\rho)}$.

Next, $\rho(s)\to\rho(x_\pm)$ as $s\to\pm\infty$. Indeed,
$$|\rho(s)-\rho(x_+)|\le|\rho(s)-z(s,Y)|+|z(s,Y)-x_+(Y)|+|x_+(Y)-\rho(x_+)|.$$
Choose $Y$ so that the first term (uniformly in $s$, by (T2)) and the third term are small. Then let $s\to\infty$ in the second term, using (T1).

Now $f(s)=\mathrm{Re}\,S(\rho(s))$ satisfies $f'=-|\partial S(\rho)|^2\le0$, and $f(\pm\infty)=\mathrm{Re}\,S(\rho(x_\pm))=0$, because $S=0$ on $\mathrm{Crit}(S)$. Hence $\int|\partial S(\rho)|^2=0$, so $\rho'\equiv0$. $\square$

**Proposition 7.3 (constancy between $\sigma$-objects; Theorem 1(B2)).** If $x_\pm$ are $\sigma$-symmetric diagonal objects, every admissible trajectory from $x_-$ to $x_+$ is constant, and $x_-=x_+$.

*Proof.* Integrate (2.4) over $[-n,n]\times[\varepsilon,Y]$:
$$\int_{-n}^n\!\!\int_\varepsilon^Y|\partial_sz|^2=\int_\varepsilon^Y\big(\mathfrak a(z(-n,y))-\mathfrak a(z(n,y))\big)dy+\int_{-n}^n\big[C\cdot\partial_sA\big]_{y=\varepsilon}^{y=Y}ds .$$
Let $\varepsilon\to0$ and $Y\to\infty$. The flux term vanishes by (T3). For $n\ge n_0$ the action terms are in $L^1$, by (T1) and $\mathfrak a(x_\pm)\equiv0$. So
$$E_n:=\int_{-n}^n\!\!\int_0^\infty|\partial_sz|^2\le\|\mathfrak a(z(-n,\cdot))\|_{L^1}+\|\mathfrak a(z(n,\cdot))\|_{L^1}\to0 .$$
Since $E_n$ is nondecreasing, $E_n=0$ for all $n$. Hence $\partial_sz\equiv0$, and $z(s,y)=x_-(y)=x_+(y)$. $\square$

For $\sigma$-objects this proof does not even need Proposition 7.2. The splitting matters for objects that may lie off the slice. There it shows that a trajectory can only connect objects with the same flat limit.

**Proposition 7.4 (σ-symmetric objects per limit; Theorem 1(B3)).** The $\sigma$-symmetric objects are exactly $x_b$, $b\le b_c$, with $\rho(x_b)=\rho_{s(b)}$ (I1), (I5). So for $\rho=\rho_s$ there is exactly one if $s\ge\mu$ and none if $s<\mu$, and there is none for $\rho$ not of the form $\rho_s$ with $s\ge\mu$. The underlying mechanism is the following. Along slice solutions $v$ is nonincreasing, since $v'=-\zeta$. If $v(y_1)<\mu$ at some $y_1$, the solution blows up [12, Lemma 4.3]. So a convergent slice solution has $s=\inf v\ge\mu$, and $s=\mu$ forces $b=b_c$.

About objects that are not $\sigma$-symmetric we use only the following. By [12, Theorem 1.2], a diagonal corrected-Nahm-pole solution whose trajectory under the flow (1.1) in $y$ enters and remains in the local center-stable neighbourhood of the slice family specified there is $\sigma$-symmetric, hence some $x_b$. Diagonal objects that do not satisfy this hypothesis are not controlled. For the five-dimensional ansatz $\mathcal V$ of [13], the reduction of objects to the diagonal ansatz is the result of [13], under the hypotheses stated there.

*Proof of Theorem 1(B).* (B1)–(B3) are Propositions 7.2–7.4. The identification of $s=\mu$ with $\lambda_A=e^{\mu\ell}$ is [12, §7]. $\square$

**What (B) does and does not say.**
- It does say that, for solutions of the reduced equation (2.3) satisfying (T1)–(T3), the flat limit is constant along the trajectory and there are no non-constant trajectories between $\sigma$-symmetric objects.
- It does not say anything about left-invariant HW fields with $(A_s,A_y)\neq0$ that cannot be brought to the sector $A_s=A_y=0$.
- It does not say that solutions outside the left-invariant ansatz cannot connect the objects.
- It does not exclude diagonal non-$\sigma$-symmetric objects outside the neighbourhood of [12, Theorem 1.2]; [12, §5.3] found numerically none in a box.
- It does not define a flow category, a grading or a homotopy type.

---

## 8. The computer-assisted part and the numerics

`verify.py` Part B reuses, verbatim, the validated machinery of [12, §6]:
- outward-rounded IEEE interval arithmetic;
- an order-18 Taylor–Lohner integrator with QR wrapping [8];
- the exact-rational contraction at the pole, with $y_0=1/32$, $\kappa=12$ and error $\le7.83\cdot10^{-17}$.

The certified two-sided bounds $1+\sqrt{E(10)}\le s\le1+\sqrt{E(10)+p(10)^2/2}$ come from [12, Lemma 4.2], with $E=(v-1)^2-|z_1|^2$.

**Printing convention.** Every decimal bracket below and in `data/enclosures.json` is outward-rounded: the lower end is rounded down, the upper end is rounded up, and the two ends differ. `verify.py` checks in exact rational arithmetic that each printed bracket strictly contains the computed interval enclosure (B4, B5). The $b$-windows have exact decimal endpoints; they are the shooting parameters themselves.

- **B3** re-certifies $b_c\in(-0.15460650842,-0.15460650837)$.
- **B4** re-certifies $s(b)$ at five sample values of $b$; for example $s(-\frac14)\in[1.67388804972,\,1.67388804978]$.
- **B5** locates the walls. For $\delta=\frac12$:
$$s(-0.2072094)\in[1.5000006106,\,1.5000006108]>\tfrac32>s(-0.2072091)\in[1.4999991819,\,1.4999991820].$$
For $\delta=\frac1{10}$:
$$s(-0.1567152)\in[1.1000047058,\,1.1000047062]>\tfrac{11}{10}>s(-0.1567148)\in[1.0999952195,\,1.0999952199].$$
The margins to $1+\delta$ are at least $6.1\cdot10^{-7}$ for $\delta=\frac12$ and $4.7\cdot10^{-6}$ for $\delta=\frac1{10}$. With strict monotonicity of $s$ (I5), this gives the stated enclosures of $b_\delta$. (The first version of this paper printed these brackets with both ends rounded to the same nine-digit number. That was not an interval enclosure, although the sign conclusions were unaffected.)

Part C is numerical evidence only:
- (C1) Along $b=-\frac14$:
  - $-\eta'(14)=-3.544994$ agrees with a finite-difference $s'(b)$ to $10^{-6}$;
  - the odd field with $T_\infty=0$ grows at rate $0.6740$, while $s-\mu=0.6739$;
  - the generic odd field grows at rate $2.6739$, while $s+\mu=2.6739$.
- (C2) At $b_c$: $\eta'/y\to1.585$, so $\eta\sim cy^2$, and the $T_\infty=0$ odd field grows polynomially.
- (C3) Floating-point locations of the $\delta$-walls.

The runtime is about 90 s.

---

## 9. Literature

For the weighted Fredholm theory we use standard tools:
- Lockhart–McOwen-type exponential weights [9];
- Palmer's dichotomy index, as a cross-check only [6];
- the half-line model of [11, Theorem H].

The closest general precedent is He [10]. Besides the gluing theorem for Nahm-pole KW solutions converging to acyclic flat connections, [10, §§5.5–5.6] treats exponential weights for reducible limits, including Nahm-pole boundary conditions. It proves an index-difference formula involving the kernel of the limiting extended Hessian [10, Propositions 5.10, 5.13, 5.19]. The present limits $\rho_s$ are reducible with $H^1\neq0$ on $\mathrm{Sol}$, and the hypotheses of [10] do not literally cover them. So we do not claim duplication, but the general weighted mechanism (exceptional weights from the limiting operator, index jumps by asymptotic kernel dimensions) is in [10]. Our contribution is the explicit Sol computation: explicit quadratures for the pole-regular Jacobi fields, the complete weighted kernel table including the threshold object, and the exact walls.

The inputs come from [12] (the family, the threshold, the cohomology jump, the $(R,T,\beta)$ reduction with $\beta''=2\zeta\beta$) and [13] (the nine-component reduction in the sector $A_s=A_y=0$, and a conditional energy-based exclusion of trajectories). The HW Fredholm theory of [14] (homogeneous energy spaces, hyperbolic cutoffs) treats Nahm-pole ends of a different type. [15] computed nonzero relative indices in toy blocks. [16] showed that genuine Nahm-pole ends on $S^1\times\Sigma\times\mathbb R^+$ need exponential weights and computed the asymptotic kernel. On $\mathrm{Nil}^3$, [17] proved non-degeneracy within the ansatz for a solution converging algebraically to the trivial connection, without a Fredholm or index statement. For trajectory operators, Fredholmness and the identification of the index with a relative Maslov index are proved by Haydys [2, Theorem 2.28, Proposition 2.30] in his setting; nothing of this kind is proved here. The $\zeta$-instanton form of HW in the ansatz is in the spirit of Gaiotto–Moore–Witten [5] and of Haydys [2]. Our literature search (arXiv and the web, November 2026) was not exhaustive.

## 10. What is not proved

1. Nothing outside the left-invariant ansatz. The operator $L_b$ is the linearization *within the diagonal ansatz*. The full gauge-theoretic operator (with gauge fixing, on $M_A\times\mathbb R_+$) is not treated, and neither are the off-diagonal directions of the larger ansatz $\mathcal V$ of [13].
2. No HW relative grading. $I_\delta$ is a weighted cross-section index. Its relation to indices of trajectory operators, spectral flow or Maslov indices is Open question 6.4.
3. No nonlinear Morse–Bott statement for $\mathrm{Acc}$ (Remark 6.3).
4. Trajectory statements only for the reduced equation (2.3), i.e. in the sector $A_s=A_y=0$ for the nine-component ansatz, and only under the admissibility hypotheses (T1)–(T3). These hypotheses are not derived from a compactness or regularity theory of the 2D equation with Nahm-pole boundary.
5. Global uniqueness of diagonal objects off the slice is open. Only the local statement of [12, Theorem 1.2], under its center-stable-neighbourhood hypothesis, and numerical evidence are available.
6. No flow category, Cohen–Jones–Segal or Lipshitz–Sarkar realization is constructed.
7. `verify.mpl` mirrors the exact symbolic checks and was not executed by us (no Maple in our environment).

## Reproducibility

`verify.py` is self-contained (python3, numpy, sympy, scipy; tested with SymPy 1.11 and 1.14). It prints one OK/FALLA line per check, then `checks: 69`, and ends with `FALLOS = 0`; it runs in about 90 s. The output is in `verify_output.txt`. The script has three parts:
- Part A: exact (sympy), including the sign $D\mathcal G=-L$ (A2), the closed form and walls of $I_\delta$ (A7), and the remainder computation of Remark 6.3 (A9);
- Part B: rigorous (exact rationals and outward-rounded intervals), with exact checks that every printed bracket strictly contains its enclosure;
- Part C: numerical evidence, labelled `[numerical]`.

`verify.mpl` (Maple, DifferentialGeometry) re-derives the HW reduction and the exact identities of Part A.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topology 3 (2012) 1–137; arXiv:1101.3216.
2. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015) 151–207; arXiv:1010.2353.
3. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser (1995) 297–325.
4. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014) 983–1042.
5. D. Gaiotto, G. Moore, E. Witten, *Algebra of the infrared: string field theoretic structures in massive $\mathcal N=(2,2)$ field theory in two dimensions*, arXiv:1506.04087.
6. K. J. Palmer, *Exponential dichotomies and transversal homoclinic points*, J. Differential Equations 55 (1984) 225–256.
7. M. F. Atiyah, V. K. Patodi, I. M. Singer, *Spectral asymmetry and Riemannian geometry I*, Math. Proc. Cambridge Philos. Soc. 77 (1975) 43–69.
8. R. J. Lohner, *Enclosing the solutions of ordinary initial and boundary value problems*, in: Computer Arithmetic, Teubner (1987) 255–286.
9. R. Lockhart, R. McOwen, *Elliptic differential operators on noncompact manifolds*, Ann. Sc. Norm. Sup. Pisa 12 (1985) 409–447.
10. S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, J. Topology (2019); arXiv:1707.06182.
11. rStation math_16 v1, *Essential self-adjointness of the Haydys–Witten cross-section operator at the Nahm pole, and a cone reduction at the weight-one knot*, https://rstation.ai/problems/math/papers/16/v1.
12. rStation math_45 v1, *Kapustin–Witten solutions with corrected Nahm pole on $\mathrm{Sol}^3\times\mathbb R_+$ converging exponentially to non-trivial flat $SL(2,\mathbb C)$ connections: a sharp threshold and a monotone endpoint map*, https://rstation.ai/problems/math/papers/45/v1.
13. rStation math_47 v1, *The non-abelian left-invariant ansatz for Kapustin–Witten on $\mathrm{Sol}^3\times\mathbb R_+$: an exact reduction, and rigidity of corrected-Nahm-pole solutions*, https://rstation.ai/problems/math/papers/47/v1.
14. rStation math_19 v1, https://rstation.ai/problems/math/papers/19/v1.
15. rStation math_20 v1, https://rstation.ai/problems/math/papers/20/v1.
16. rStation math_21 v1, https://rstation.ai/problems/math/papers/21/v1.
17. rStation math_43 v1, https://rstation.ai/problems/math/papers/43/v1.

---

## Appendix. Changes in this revision (r1)

1. **Relative grading.** The quantity $\mathrm{gr}_\delta$ is renamed the weighted cross-section index $I_\delta(b)=\mathrm{ind}\,L_{b,-\delta}$. It is no longer called an HW relative grading. Its weight-dependent walls are now described exactly in Theorem 1(A6) and §6.3. For fixed $\delta\in(0,2\mu)$ the value changes from $1$ to $2$ at $s=\mu+\delta$, before the threshold, and stays $2$ at $b_c$. For $\delta>2\mu$ there is a second wall at $s=\delta-\mu$. For no fixed weight is there a change at $b_c$. The difference between $b<b_c$ and $b_c$ appears only in the small-weight limit. A closed form $I_\delta=\frac12\#\{|\lambda|<\delta\}$ is added (Corollary 6.1; `verify.py` A7). The relation to spectral flow and Maslov indices is now Open question 6.4, compared with Haydys [2, Theorem 2.28, Proposition 2.30]. The categorical interpretation is removed from the title, the abstract, Theorem 1 and §6. This includes the one-object category, "$S^0$ up to the grading shift" and "no morphisms" as a categorical statement, and the former (B4).
2. **Morse–Bott.** The Morse–Bott theorem for the action is removed. Theorem 1(A5) now states only the linear kernel, cokernel and endpoint-map facts. Remark 6.3 explains, with the perturbation $u_1=u_2=\varepsilon\chi e^{ay}$, $\delta/2<a<\delta$, why $\mathcal G$ does not map the negatively weighted space into itself (`verify.py` A9). The sign is fixed: $D\mathcal G=-L_b$ (Proposition 2.2; `verify.py` A2). $L_b$ is called the cross-section operator, not the Hessian. The zero mode of the critical line is no longer called a Morse–Bott mode of the objects.
3. **Sector restriction.** Theorem 1(B), the abstract and §7 now state the sector $A_s=A_y=0$. For the nine-component ansatz they cite [13, Theorem A(2)] and note that this is an additional restriction, not a gauge choice when $F_{sy}\neq0$. The shorthand "every nearby diagonal object is $\sigma$-symmetric" is replaced by the actual hypothesis of [12, Theorem 1.2]: entering and remaining in the specified local center-stable neighbourhood.
4. **Novelty.** He [10, §§5.5–5.6, Propositions 5.10, 5.13, 5.19] is now presented as the relevant general precedent for exponential weights at reducible limits with Nahm-pole boundary conditions, and for index-difference formulas (§1.5, §9). [12] is credited for the family, threshold, cohomology jump and the $(R,T,\beta)$ reduction with $\beta''=2\zeta\beta$. [13] is credited for the enlarged reduction and the conditional energy-based exclusion. The stated contribution is the explicit Sol computation.
5. **Intervals.** All decimal brackets in §8 and `data/enclosures.json` are now genuinely outward-rounded with distinct endpoints. `verify.py` B3–B5 compute them in exact rational arithmetic and check that each printed bracket strictly contains the computed enclosure. The wall comparisons with $1+\delta$ are now exact rational comparisons.
6. **Abstract and citations.** The abstract is now inline. It assigns the tangent kernel to $L_{b,-\delta}$ (weight $-\delta$), consistent with Theorem 1(A3), and states that $L_{b,\delta}$ is injective. The pointer to a separate abstract file is removed. The companion citations are consolidated into the numbered references [11]–[17], with rStation papers cited by their URLs and no "under review" language. The unused citation of math_42 is dropped.
7. **Verification files.** `verify.py` goes from 60 to 69 checks, ending with `FALLOS = 0`, and runs with SymPy 1.11 and 1.14. `verify.mpl` is updated consistently (it is still not executed).

# A Kapustin–Witten solution with corrected Nahm pole on $\mathrm{Nil}^3\times\mathbb R_+$ that decays algebraically to the trivial flat connection: a computer-assisted existence proof and a localization of the shooting parameter

**Abstract.** See `abstract.md`.

---

## 1. Introduction

Let $W$ be an oriented Riemannian 3-manifold and $M=W\times\mathbb R_+$, with coordinate $y>0$ on the half-line. The Kapustin–Witten (KW) equations at $t=1$ for a connection $A$ and a 1-form $\phi$ with values in the adjoint bundle are
$$F_A-\phi\wedge\phi+\star d_A\phi=0,\qquad d_A\star\phi=0. \tag{1.1}$$
The Nahm pole boundary condition requires $\phi\sim e/y$ as $y\to0$, where $e$ is a "vierbein", an isomorphism $TW\to\mathrm{ad}P$ intertwining the cross product with the Lie bracket. Witten [W1, §3] showed that on a curved $W$ the boundary value of $A$ must then be the spin (Levi-Civita) connection transported by $e$. Mazzeo and Witten [MW1, MW2] proved that the boundary condition is elliptic and that solutions are polyhomogeneous. He [He2] computed the expansion on a general $W$: the first logarithmic term is $y\log y$ in $\phi$ and $y^2\log y$ in $A$, its coefficient is the traceless Ricci tensor of $W$, and the logarithms are absent exactly when $W$ is Einstein.

Few Nahm-pole solutions on $W\times\mathbb R_+$ with $W$ compact are known explicitly. He [He1] found rotationally invariant solutions over $S^3\times\mathbb R_+$. He's gluing theorem [He3] produces solutions converging to *acyclic* flat $SL(2,\mathbb C)$ connections, with exponential decay. Taubes [T] studied compactness of sequences of such solutions. Other uniqueness questions in the KW Nahm-pole problem are studied in rStation math_38 [R38] and in rStation math_40 [R40].

This paper treats the simplest *non-Einstein* homogeneous cross-section, the Heisenberg nilmanifold. Let $\mathrm{Nil}^3_\lambda$ be the Heisenberg group with the left-invariant coframe
$$\theta^1=dx^1,\quad\theta^2=dx^2,\quad\theta^3=dx^3-\lambda x^1dx^2,\qquad d\theta^3=-\lambda\,\theta^1\wedge\theta^2,\qquad\lambda\neq0,$$
and the metric $\sum(\theta^k)^2$. Its Ricci tensor is $\mathrm{diag}(-\lambda^2/2,-\lambda^2/2,\lambda^2/2)$ in this frame [Mi]. Everything below is left-invariant. It therefore descends to every compact quotient $\Gamma\backslash\mathrm{Nil}^3_\lambda$ by a lattice $\Gamma$, which is a nontrivial circle bundle over $T^2$. The bundle is the trivial $SU(2)$ bundle. Fix a basis $T_1,T_2,T_3$ of $\mathfrak{su}(2)$ with $[T_i,T_j]=\epsilon_{ijk}T_k$. The *left-invariant diagonal ansatz*, in temporal gauge, is
$$A=\sum_{k=1}^3A_k(y)\,\theta^k T_k,\qquad \phi=\sum_{k=1}^3C_k(y)\,\theta^kT_k,\qquad z_k:=A_k+iC_k. \tag{1.2}$$

**Proposition 1.1 (reduction; [inputs], re-verified in `verify.py` Part A).** For (1.2) the Gauss law $d_A\star\phi=0$ holds identically, and (1.1) is equivalent to
$$z_k'=i\,\overline{\partial S/\partial z_k},\qquad S(z)=z_1z_2z_3-\tfrac{\lambda}{2}z_3^2. \tag{1.3}$$

In components, (1.3) reads
$$\begin{aligned}
A_1'&=A_2C_3+A_3C_2, & C_1'&=A_2A_3-C_2C_3,\\
A_2'&=A_1C_3+A_3C_1, & C_2'&=A_1A_3-C_1C_3,\\
A_3'&=A_1C_2+A_2C_1-\lambda C_3, & C_3'&=A_1A_2-C_1C_2-\lambda A_3 .
\end{aligned}$$
Here $S$ is the complex Chern–Simons functional restricted to the ansatz. Thus (1.3) is the explicit form, in this ansatz, of Witten's observation [W1, W2] that the KW equations at $t=1$ on $W\times\mathbb R$ are the gradient flow of $\mathrm{Im}\,CS$, equivalently the Hamiltonian flow of $\mathrm{Re}\,CS$. For $\lambda\ne0$ the pure Nahm pole $C_k=1/y$, $A_k=0$ is not a solution. The *corrected Nahm pole* is
$$C_k=\frac1y+o(1/y),\qquad A\to A_0=\tfrac{\lambda}{2}\big(\theta^1T_1+\theta^2T_2-\theta^3T_3\big),$$
and $A_0$ is the Levi-Civita connection under $T_k\leftrightarrow\theta^k$, i.e. $d_{A_0}(\sum_k\theta^kT_k)=0$ (inputs; `verify.py` A3).

We ask for solutions with the corrected Nahm pole at $y=0$ that decay, $z(y)\to0$, to the trivial flat connection as $y\to\infty$. The trivial flat connection is **not acyclic** on $\mathrm{Nil}^3$: $H^1(\mathrm{Nil}^3;\mathfrak{su}(2))=H^1(\mathrm{Nil}^3)\otimes\mathfrak{su}(2)\ne0$, because $b_1(\Gamma\backslash\mathrm{Nil}^3)=2$. So [He3] does not apply. Inside the ansatz the critical point $z=0$ of $S$ is degenerate (quartic, §5), and the decay is algebraic, not exponential.

### 1.1 Main results

By the symmetries of §2 we may take $\lambda=1$; the general case follows by rescaling (Remark 1.3). Let
$$I:=(0.0197321125,\;0.0197321127).$$
For $b\in\mathbb R$ let $x_b$ be the solution of (1.3) with $z_1=z_2$, the corrected Nahm pole, and parameters $(b,g)=(b,b)$ (Definition 3.3; $b$ is the coefficient of $y$ in $C_1$).

**Main Theorem ($\lambda=1$).**

1. **(Existence; computer-assisted.)** There is $b_*\in I$ such that $x_{b_*}$ exists for all $y>0$ and $z(y)\to0$ as $y\to\infty$. The corresponding fields (1.2) solve the KW equations on $\mathrm{Nil}^3\times\mathbb R_+$ (and on $\Gamma\backslash\mathrm{Nil}^3\times\mathbb R_+$), with the corrected Nahm pole at $y=0$. Moreover $A\to0$ and $\phi\to0$ as $y\to\infty$.
2. **(Asymptotics; analytic.)** The solution in item 1 can be chosen to lie in the block $K$ of §5 for all $y\ge7/2$. Every solution of the ansatz with this property satisfies the following, with $z_1=z_2=u$ and $z_3=v$:
   - $|u|^{-2}=2y-2\log y+C+o(1)$ for a constant $C$, so $|z_1|^2=|z_2|^2=\frac1{2y}\big(1+\frac{\log y}{y}+O(\frac1y)\big)$;
   - $\arg u\to 3\pi/8 \pmod \pi$ exponentially fast, so $\sin(4\arg z_1)\to-1$;
   - $z_3=z_1^2\,(1+O(1/y))$;
   - $\mathrm{Im}\,S<0$ increases to $0$, and $\mathrm{Im}\,S=-\frac1{8y^2}(1+o(1))$.
3. **(Localization; computer-assisted.)** Let $z$ be any solution of the full system (1.3) on $(0,\infty)$ with the corrected Nahm pole (Definition 3.1) and $z(y)\to0$. Then $z_1\equiv z_2$, $\mathrm{Re}\,S\equiv0$, and $z=x_b$ for some $b\in I$.

**Remark 1.2 (what is not proved).** We do not prove that $b_*$ is unique inside $I$. High-precision shooting gives a single crossing at $b_*\approx0.0197321126473$ (§8). See §9 for the full list.

**Remark 1.3 (general $\lambda$).** If $z(y)$ solves (1.3) with parameter $\lambda$, then $\mu z(\mu y)$ solves it with $\mu\lambda$ ($\mu>0$), and $-\bar z$ solves it with $-\lambda$. These maps preserve the corrected pole and decay. Because of the logarithm, the shooting parameter transforms as
$$b(\lambda)=\lambda^2\big(b(1)-\tfrac13\log|\lambda|\big),\qquad g(\lambda)=\lambda\,b(\lambda). \tag{1.4}$$
Hence, for every $\lambda\ne0$, there is a decaying solution with $b\in\lambda^2(I-\frac13\log|\lambda|)$, and every decaying solution of the ansatz has $b$ in that interval. For $\lambda>0$ its asymptotics are $|z_1|^{-2}=\lambda^{-1}\big(2y-\tfrac2\lambda\log(\lambda y)+\tfrac{C}{\lambda}+o(1)\big)$, i.e. $|z_1|^2\sim\lambda/(2y)$. The statement $b_*\approx0.0197321\,\lambda^2$ is correct only at $|\lambda|=1$.

### 1.2 What is new, stated narrowly

- *Not new:* the log/Ricci terms of the expansion and the Levi-Civita limit. These are instances of He's general theorem [He2, Prop. 3.2, Thm. 1.4] and of Witten [W1, §3] and Mazzeo–Witten [MW1]. The reduction (1.3) and its gradient-flow reading are direct computations, and the interpretation is Witten's.
- *New, as far as we know:* (i) a rigorous existence proof of a Nahm-pole KW solution over a compact non-Einstein cross-section that converges to a *non-acyclic* flat connection, with algebraic rate $y^{-1/2}$ and a logarithmic correction; (ii) an isolating block at the degenerate quartic critical point of the reduced Chern–Simons functional, which turns the shooting into a Ważewski-type argument; (iii) a rigorous localization of all decaying solutions of the ansatz to a parameter interval of width $2\cdot10^{-10}$. We have not found solutions of this type in the literature (§1, references), but our search was not exhaustive.

---

## 2. Symmetries and monotone quantities

**Lemma 2.1.** Along solutions of (1.3):
1. $\mathrm{Re}\,S$ is constant.
2. $\frac{d}{dy}\mathrm{Im}\,S=\sum_k|\partial_kS|^2\ge0$.
3. $|z_1|^2-|z_2|^2$ is constant.
4. The flow commutes with $(z_1,z_2,z_3)\mapsto(z_2,z_1,z_3)$ (swap) and with $(z_1,z_2)\mapsto(-z_1,-z_2)$ (a constant gauge transformation).
5. The flow commutes with the scaling and conjugation maps of Remark 1.3.

*Proof.* Item 1: (1.3) is the Hamiltonian flow of $\mathrm{Re}\,S$ for $\omega=\sum dA_k\wedge dC_k$. Item 2: (1.3) is the gradient flow of $\mathrm{Im}\,S$ for the flat metric. Item 3: $|z_1|^2-|z_2|^2$ is the moment map of $(z_1,z_2)\mapsto(e^{i\alpha}z_1,e^{-i\alpha}z_2)$, which preserves $S$. Items 4–5: direct. All are checked symbolically in `verify.py` (A2). $\square$

**Corollary 2.2 (the $\mathrm{Im}\,S$ criterion).** If $z(y)\to0$ then $\mathrm{Im}\,S(z(y))<0$ for all $y$. In particular, if $\mathrm{Im}\,S(z(y_1))>0$ at a single $y_1$, the solution does not decay.

*Proof.* $S(0)=0$, and $\mathrm{Im}\,S$ is nondecreasing. If $\mathrm{Im}\,S(y_1)=0$ at some $y_1$ with $z\to0$, then $\mathrm{Im}\,S\equiv0$ on $[y_1,\infty)$, so $\nabla S\equiv0$ there. Then $z$ is constant, $z\equiv0$, and so $z\equiv0$ for all $y$, which contradicts the pole. $\square$

**The symmetric slice.** $\{z_1=z_2\}$ is invariant. Write $u=z_1=z_2=a+ic$ and $v=z_3=\alpha+i\gamma$. At $\lambda=1$, $S=u^2v-\frac12v^2$ and
$$a'=a\gamma+c\alpha,\quad c'=a\alpha-c\gamma,\quad \alpha'=2ac-\gamma,\quad \gamma'=a^2-c^2-\alpha. \tag{2.1}$$
For general $\lambda$, replace $-\gamma$ and $-\alpha$ in the last two equations by $-\lambda\gamma$ and $-\lambda\alpha$. On this slice $\frac{d}{dy}\mathrm{Im}\,S=2|uv|^2+|u^2-\lambda v|^2$. The only critical point of $S$ on the slice is $u=v=0$.

---

## 3. Local theory at the corrected Nahm pole

Write the unknown as a real vector $x$: $x=(A_1,A_2,A_3,C_1,C_2,C_3)$ for the full system, or $x=(a,c,\alpha,\gamma)$ on the slice. Let $p(y)$ be the pure pole, $C_k=1/y$, $A_k=0$. The Jacobian of the right-hand side $F$ at $p$ is $M/y+(\text{const})$. Its singular part $M$ is diagonalizable, with eigenvalues ("indicial roots")
$$\{2,-1,-1\}\ (\text{$A$-block}),\qquad\{1,1,-2\}\ (\text{$C$-block}).$$
On the slice the roots are $\{2,-1\}$ and $\{1,-2\}$. With variables ordered $(a,c,\alpha,\gamma)$, the eigen-coordinates are
$$\eta_2=\tfrac{2a+\alpha}{3},\quad\eta_{-1}=\tfrac{a-\alpha}{3},\quad\eta_1=\tfrac{c-\gamma}{3},\quad\eta_{-2}=\tfrac{2c+\gamma}{3},$$
with $\|V\|_\infty=3$ and $\|V^{-1}\|_\infty=1$.

**Definition 3.1.** A solution of (1.3) on $(0,y_1]$ has the *corrected Nahm pole* if for some $\delta>0$
$$z_k(y)-\frac{i}{y}=O(y^{-1+\delta})\qquad(y\to0),\ k=1,2,3.$$

**Proposition 3.2 (formal series).** Let $L=\log y$. There is a unique formal solution
$$A_k=\sum_{n\ge0\ \mathrm{even}}y^n a_{k,n}(L),\qquad C_k=\frac1y+\sum_{n\ge1\ \mathrm{odd}}y^nc_{k,n}(L),$$
with polynomial coefficients, $\deg_L a_{k,n},\deg_Lc_{k,n}\le\lfloor (n+1)/2\rfloor$ (with equality on the slice, checked to $n=16$), for every choice of three real parameters $(B_1,B_2,G)$. These are the non-logarithmic parts of the $y$-coefficients of $C_2$ and $C_3$ and of the $y^2$-coefficient of $A_3$. Explicitly:
$$C_1=\tfrac1y+y\big(\tfrac{\lambda^2}{12}-B_1-B_2-\tfrac{\lambda^2}3L\big)+\dots,\quad C_2=\tfrac1y+y\big(B_1-\tfrac{\lambda^2}3L\big)+\dots,\quad C_3=\tfrac1y+y\big(B_2+\tfrac{2\lambda^2}3L\big)+\dots,$$
$$A_k=(A_0)_k-\tfrac\lambda2\mathrm{Ric}^\circ_k\,y^2L+O(y^2),\qquad \mathrm{Ric}^\circ=\tfrac{\lambda^2}3(-1,-1,2).$$

*Proof.* At order $y^n$ the equations read $(n-M)X_n+\partial_LX_n=\mathrm{RHS}_n(L)$, a polynomial in $L$ determined by lower orders. If $n\notin\mathrm{spec}\,M$, solve from the top degree in $L$ down; the solution is unique. At $n=1$ (C-block) and $n=2$ (A-block) the kernel directions carry the free parameters, and the resonance forces one extra power of $L$. The coefficients are computed exactly (`verify.py` A4–A5). The symmetric series to order $y^{12}$ ($A$) and $y^{11}$ ($C$) agrees with the inputs `serie_sim.txt` and `nahm_nil.py`. The full series has residual $O(y^4)$. $\square$

The log coefficients agree with He's general formula [He2, Prop. 3.2(c), Thm. 1.4], including the parity of the powers and the bound on the log degree. They vanish iff $\lambda=0$, i.e. iff the cross-section is the flat (Einstein) torus.

**Definition 3.3 (the shooting family).** On the slice, $B_1=b$, $B_2=\lambda^2/12-2b$, $G=g$. For $\lambda=1$ and $g=b$ let $x_N(y;b)$ be the series truncated at $N=12$ ($a,\alpha$ up to $y^{12}$, $c,\gamma$ up to $y^{11}$; 12 is the largest power of $y$ that appears).

**Proposition 3.4 (local existence, uniqueness, continuity).**
(a) For every parameter $B$ there are $y_1>0$ and a solution $x^B$ on $(0,y_1]$ with $x^B-x^B_{\mathrm{trunc}}=O(y^\kappa)$ for some $\kappa>2$. It is unique among solutions with this property and depends continuously on $B$.
(b) *Quantitative version on the slice, $\lambda=1$, $g=b$.* Take $N=12$, $\kappa=10$, and either ($y_0=1/16$, $|b|\le1/40$) or ($y_0=1/64$, $|b|\le12$). Then the solution exists on $(0,y_0]$ and
$$|x_b(y_0)-x_N(y_0;b)|_\infty\le\varepsilon,\qquad \varepsilon=6.4\cdot10^{-16}\ \text{resp.}\ 1.2\cdot10^{-16}.$$

*Proof.* Put $x=x_N+V\eta$. Then
$$y\eta'=D\eta+y\,h,\qquad h=V^{-1}\big(E(y)V\eta+F_2(V\eta)+R(y)\big),$$
where $D=\mathrm{diag}(2,-1,1,-2)$, $E=J(x_N-p)+J_{\rm const}$ is bounded, $F_2$ is the quadratic part of $F$, and $R=F(x_N)-x_N'$ is the residual. Solutions with $\eta=O(y^\kappa)$, $\kappa>2$, are exactly the fixed points of
$$(T\eta)_i(y)=y^{\mu_i}\int_0^ys^{-\mu_i}h_i(s)\,ds$$
in $X_\delta=\{\sup_{0<y\le y_0}y^{-\kappa}|\eta(y)|_\infty\le\delta\}$. For $\mu_i<0$ the boundary term vanishes because $\kappa+\mu_i>0$; for $\mu_i>0$ this choice fixes the parameters. Suppose
$$\|V^{-1}EV\|_\infty\le e_1,\qquad |V^{-1}F_2(V\eta)|_\infty\le18|\eta|^2_\infty,\qquad |V^{-1}R(s)|_\infty\le\rho_Rs^{\kappa-1}.$$
Then $T$ maps $X_\delta$ into itself with Lipschitz constant at most
$$\theta=\frac{e_1y_0}{\kappa-1}+\frac{2\cdot18\,\delta\,y_0^{\kappa+1}}{2\kappa-1}$$
whenever $\theta\le\frac12$ and $\delta=2\rho_R/(\kappa-2)$. The bounds $e_1,\rho_R$ are computed in exact rational arithmetic. Each monomial $c\,y^nL^mb^j$ is bounded by $|c|\sup_{(0,y_0]}s^{n'}|\log s|^m\cdot b_{\max}^j$, using rational enclosures of $\log 2$ and $e$. We get $\rho_R\le9.4\cdot10^{-4}$, $e_1\le1.69$, $\theta\le0.012$ (first case) and $\rho_R\le177$, $e_1\le2.14$, $\theta\le0.004$ (second case). The fixed point is continuous in $b$ because $T$ is a uniform contraction depending continuously on $b$. Finally $|V\eta(y_0)|_\infty\le3\delta y_0^\kappa=\varepsilon$. Part (a) is the same argument for the full system with the order-4 series, $\kappa\in(2,4)$, and $y_1$ small. `verify.py` B1. $\square$

**Lemma 3.5 (classification).** Every solution with the corrected Nahm pole coincides near $0$ with $x^B$ for a unique $B$.

*Proof.* Fix any $B_0$ and set $d=x-x^{B_0}$. Then $yd'=Md+y\big(E_0(y)d+F_2(d)\big)$, with $E_0$ bounded, and $d=O(y^{\beta})$ with $\beta=-1+\delta$. Pass to modes, $d=V\eta$, and $h=O(y^{\min(\beta,2\beta)})$.

*Negative modes.* Use $\eta_\mu=y^\mu\int_0^ys^{-\mu}h$. The boundary term $s^{|\mu|}O(s^\beta)$ tends to $0$, and the integrand is integrable since $|\mu|+2\beta>-1$.

*Positive modes.* Use $\eta_\mu=y^\mu\big(y_1^{-\mu}\eta_\mu(y_1)-\int_y^{y_1}s^{-\mu}h\big)$.

This gives $d=O(y^{\min(2\beta+1,1)}|\log y|)$. Iterating finitely many times, $d=O(y|\log y|)$. One more step gives $d=y\,\mathbf c_1+O(y^2\log^2y)$ with $\mathbf c_1\in\ker(M-1)$. This kernel is 2-dimensional in the $C$-block, $\perp(1,1,1)$, and is spanned by $\partial_{B_1},\partial_{B_2}$ of the $y$-coefficients. Changing $(B_1,B_2)$ removes $\mathbf c_1$. Repeating with the root $2$, whose eigenvector $(1,1,1)$ in the $A$-block is $\partial_G$ of the $y^2$-coefficients, adjusts $G$. Then $d=O(y^3\log^2y)$, so $d$ is a fixed point of the homogeneous contraction (zero forcing) in $X_\delta$ on a small interval, and $d\equiv0$. $\square$

---

## 4. Decaying solutions lie on a one-parameter curve

**Proposition 4.1.** Let $z$ be a corrected-Nahm-pole solution on $(0,\infty)$ with $z\to0$. Then $z_1\equiv z_2$ and $g=\lambda b$. Equivalently, $\mathrm{Re}\,S\equiv0$.

*Proof.* By Lemma 2.1, $|z_1|^2-|z_2|^2$ is constant. It tends to $0$ at $\infty$. From the series, its value is
$$|z_1|^2-|z_2|^2=2\Big(\frac{\lambda^2}{12}-2B_1-B_2\Big)$$
(the $y^{-2}$, $y^{-1}$ and $\log$ terms cancel; `verify.py` A5). Hence $B_2=\lambda^2/12-2B_1$.

The swap maps the family to itself, with $(B_1,B_2,G)\mapsto(\lambda^2/12-B_1-B_2,\,B_2,\,G)$. Its fixed set is exactly $B_2=\lambda^2/12-2B_1$. By uniqueness (Prop. 3.4(a), Lemma 3.5), swap$(z)=z$, so $z_1=z_2$.

Finally, on the family
$$\mathrm{Re}\,S=\frac{\lambda^3}8-\frac32\lambda B_2-3G,$$
which equals $3(\lambda b-g)$ on the slice (inputs; `verify.py` A4). This vanishes because $S(z(y))\to0$. $\square$

So, at $\lambda=1$, the decaying solutions of the full ansatz are exactly the $x_b$ ($g=b$) that decay. For these $\mathrm{Re}\,S\equiv0$.

---

## 5. An isolating block at the trivial flat connection

Take $\lambda=1$, the slice, and $\mathrm{Re}\,S=0$. Define
$$\zeta=e^{-3\pi i/4}u^2=X+iY,\qquad R=|\zeta|=|u|^2,\qquad w=v-u^2=s+it,\qquad P=s-t,\quad Q=s+t.$$
Completing the square gives $S=\frac12(u^4-w^2)$. The following are polynomial identities in $(a,c,\alpha,\gamma)$ (`verify.py` A6):
$$\begin{aligned}
X'&=R(-2X+\sqrt2P), & Y'&=R(2Y-\sqrt2Q),\\
P'&=(1+2R)P-2\sqrt2RX, & Q'&=-(1+2R)Q+2\sqrt2RY,\\
R'&=-2(X^2-Y^2)+\sqrt2(PX-QY), &&\\
\mathrm{Re}\,S&=XY-\tfrac12PQ, & \mathrm{Im}\,S&=-\tfrac12(X^2-Y^2)+\tfrac14(P^2-Q^2).
\end{aligned}\tag{5.1}$$
Linearized, $Q$ is stable (rate $-1$), $P$ is unstable (rate $+1$), and $\zeta$ is a center, governed by $\zeta'\approx-2|\zeta|\bar\zeta$, i.e. $u'\approx i\bar u^3$. On the center manifold the incoming rays are $\arg u=3\pi/8\pmod{\pi/2}$, and they are repelling in angle. On the level set $L=\{\mathrm{Re}\,S=0\}$, however, $2XY=PQ$ ties the angle to $P$. So inside $L$ there is exactly one unstable direction, with two sides.

**Constants.** $c_P=16/5$, $c_Q=1/4$, $R_0=7/25$, $\sigma_0=c_Pc_QR_0/\sqrt2$,
$$\kappa_-=2-4\sigma_0^2-\sqrt2(c_PR_0+c_Q\sigma_0)>0.576,\qquad \kappa_+=2+\sqrt2(c_PR_0+c_Q\sigma_0).$$

**Definition 5.1.** $K=\{x\in L:\ 0<R\le R_0,\ |P|\le c_PR^2,\ |Q|\le c_QR,\ X>|Y|\}\cup\{0\}$. Write $f_\pm=\pm P-c_PR^2$, $g_\pm=\pm Q-c_QR$, $h=R-R_0$.

**Lemma 5.2 (block inequalities).** On $K\setminus\{0\}$:
1. $|Y|\le\sigma_0R$ and $X\ge R\sqrt{1-\sigma_0^2}$.
2. $-\kappa_+R^2\le R'\le-\kappa_-R^2<0$.
3. On $\{f_+=0\}$: $f_+'\ge(c_P-2\sqrt2)R^2>0$. On $\{f_-=0\}$: $f_-'\ge c_PR^2>0$.
4. On $\{g_\pm=0\}$: $g_\pm'\le-c_QR\,\big[1-c_PR_0^2(2+\sqrt2+c_Q^2)\big]<0$, and the bracket is $>0.127$.
5. On $\{h=0\}$: $h'<0$.
6. On $L\cap\{0<R\le R_0,|P|\le c_PR^2,|Q|\le c_QR\}$ one never has $X=|Y|$. Hence the condition $X>|Y|$ is relatively open and closed there, and $K$ is compact.

*Proof.* Item 1: on $L$, $|Y|=|PQ|/(2X)\le c_Pc_QR^3/(2X)$ and $X\ge R/\sqrt2$. Items 2–5: insert item 1, $X\le R$ and $R'<0$ into (5.1); e.g. at $P=c_PR^2$,
$$f_+'=(1+2R)c_PR^2-2\sqrt2RX-2c_PRR'\ge(c_P-2\sqrt2)R^2.$$
Item 6: $X=|Y|$ forces $R^2=2|XY|=|PQ|\le c_Pc_QR^3$, i.e. $c_Pc_QR\ge1$; but $c_Pc_QR_0=0.224$. All constants are checked in exact rational arithmetic (`verify.py` A7). $\square$

**Lemma 5.3 (exit through the $P$-faces only).** Let $x$ solve (2.1) on $L$ with $x(Y_0)\in K$. Then either $x(y)\in K$ for all $y\ge Y_0$, or $T=\sup\{y:x([Y_0,y])\subset K\}<\infty$, and then $x(T)\in K$, exactly one of $f_\pm(x(T))=0$ holds, and $x(y)\notin K$ for $y\in(T,T+\epsilon)$. The sets $E_\pm$ of initial points whose first exit is through $f_\pm$ are relatively open in $K$, and they are disjoint.

*Proof.* At $x(T)\ne0$ (the origin is an equilibrium), the active constraints among $g_\pm,h$ have negative derivative, and the sector condition is open (Lemma 5.2.6). So if $f_\pm<0$ at $x(T)$, then $x$ stays in $K$ a little longer, a contradiction. $f_+=f_-=0$ would force $R=0$. Openness: if the first exit is through $f_+$ at $T$, then $f_+>0$ at $T+\epsilon$, while $f_-<0$ on $[Y_0,T+\epsilon]$ (an earlier zero of $f_-$ would be a strict exit). Both conditions persist for nearby initial data, by continuous dependence on compact time intervals. $\square$

**Theorem 5.4 (decay and asymptotics in the block).** If $x(y)\in K$ for all $y\ge Y_0$, then $x(y)\to0$, and:
1. $(1/R(Y_0)+\kappa_+(y-Y_0))^{-1}\le R(y)\le(1/R(Y_0)+\kappa_-(y-Y_0))^{-1}$;
2. $|Q(y)|\le|Q(Y_0)|e^{-(y-Y_0)}$ and $|Y|\le\frac{c_P}{2\sqrt{1-\sigma_0^2}}R|Q|$; hence $\arg\zeta\to0$ exponentially, i.e. $\arg u\to3\pi/8\pmod\pi$;
3. $P(y)=2\sqrt2\int_y^\infty e^{-\int_y^s(1+2R)}R(s)X(s)\,ds=2\sqrt2R^2\big(1+O(R)\big)$;
4. $R'=-2R^2+4R^3+O(R^4)+O(e^{-y})$, hence $1/R=2y-2\log y+C+o(1)$;
5. $v=u^2(1+O(1/y))$, and $\mathrm{Im}\,S=-\frac12R^2(1+o(1))=-\frac1{8y^2}(1+o(1))$.

*Proof.* Item 1: Lemma 5.2.2, integrated. Item 2: on $L$, $Q'=-Q\,(1+2R-\sqrt2RP/X)$, and $\sqrt2|RP/X|\le\sqrt2c_PR^2/\sqrt{1-\sigma_0^2}\le2R$ for $R\le R_0$. So $\frac{d}{dy}|Q|\le-|Q|$. Item 3: $P$ is bounded and $e^{-\int(1+2R)}$ decays, so the unstable mode has zero coefficient. The bounds use $RX\le R^2$, $X\ge R\sqrt{1-(Y/R)^2}$ and $R(s)\ge R(y)/(1+\kappa_+R(y)(s-y))$. Item 4: insert items 2–3 into $R'$; then $(1/R)'=2-4R+O(R^2)+O(y^2e^{-y})$. With item 1, $R=\frac1{2y}(1+O(\frac{\log y}{y}))$, so $\int(4R-\frac2y)$ converges. Item 5: $|w|^2=(P^2+Q^2)/2=O(R^4)$, and use (5.1). $\square$

---

## 6. Existence (computer-assisted)

**Lemma 6.1 (verified computation).** Let $b_L=0.0197321125$ and $b_R=0.0197321127$.
- (C1) For every $b\in[b_L,b_R]$, $x_b$ exists on $(0,7/2]$ and $x_b(7/2)\in K$. The enclosure (4 parameter boxes) has $P/R^2\in[1.3441,1.3441]$ (to 4 digits), $Q/R\le0.043$ and $R\le0.2531$, against the block bounds $|P|/R^2\le3.2$, $|Q|/R\le0.25$ and $R\le0.28$.
- (C2) For $b=b_L$: $f_+<0$ on the whole tube $[3,\,14.33]$, and $f_-(x(14.33))>0$.
- (C3) For $b=b_R$: $f_-<0$ on $[3,\,13.83]$, and $f_+(x(13.83))>0$.

*Method.* Start at $y_0=1/16$ from the box $x_N(y_0;[b])+[-\varepsilon,\varepsilon]^4$ (Prop. 3.4(b)), with outward-rounded interval arithmetic in IEEE-754 double precision: every endpoint is widened by one ulp, which is rigorous under round-to-nearest. Integrate (2.1) with an order-18 Taylor method of Lohner type [Lo]:
- an a priori enclosure $W\supset X+[0,h]F(W)$, which by Picard–Lindelöf contains all trajectories over the step;
- the Lagrange remainder $h^{19}f^{[19]}(W)$;
- the mean-value form $\Phi(x)\in\Phi(\hat x)+J_\Phi(\mathrm{hull}(X\cup\hat x))(x-\hat x)$;
- sets $\hat x+Bq$, with $B$ re-orthogonalized by pivoted QR and $B^{-1}$ enclosed rigorously.

Step sizes are $h=\min(y/6,0.1)$. Face conditions are evaluated in interval arithmetic on the step tubes $W$ and at the step endpoints. Runtime: about 40 s. `verify.py` B2.

**Theorem 6.2 (= Main Theorem 1).** There is $b_*\in I$ such that $x_{b_*}$ decays.

*Proof.* By (C1) and continuity of $b\mapsto x_b(7/2)$ (Prop. 3.4), $\Gamma=\{x_b(7/2):b\in[b_L,b_R]\}$ is a curve in $K$. By (C2), the first exit for $b_L$ is through $f_-$: the trajectory leaves $K$ before $14.33$, and never through $f_+$. By (C3), the first exit for $b_R$ is through $f_+$. By Lemma 5.3 the sets $\{b:\ \text{first exit through }f_\pm\}$ are open in $[b_L,b_R]$, disjoint and nonempty. Since $[b_L,b_R]$ is connected, some $b_*\in(b_L,b_R)$ never leaves $K$. By Theorem 5.4, $x_{b_*}\to0$. $\square$

---

## 7. Localization: every other parameter fails (computer-assisted)

**Theorem 7.1 (= Main Theorem 3).** At $\lambda=1$, for every $b\notin I$ there is $y_1$ with $\mathrm{Im}\,S(x_b(y_1))>0$. Hence $x_b$ does not decay (Corollary 2.2). With Proposition 4.1 this proves Main Theorem 3.

The proof has four parts.

**(a) $b\in[-12,11]\setminus I$.** Cover this set by $2303+130$ parameter boxes. The boxes are uniform of width $\approx0.005$ where $|b|>1/40$, and dyadically refined toward $I$. For every box, a validated integration as in §6 certifies $\mathrm{Im}\,S>0$ at some $y\le40$. For $|b|>1/40$ the certification happens at $y\le2.64$ (start $y_0=1/64$). For $1/40\ge|b|$ it happens at $y\le17.5$ (start $y_0=1/16$, because the singular phase $y_0\le y\lesssim1$ amplifies rounding errors by roughly $(y/y_0)^2$). The partition was found by adaptive bisection (log in the supplement) and is embedded in `verify.py` B3, which checks that it covers $[-12,11]\setminus I$ exactly.

**(b) $b\ge 11$.** By (1.4) with $\tilde b=1$: $b=\eta^{-2}+\frac13\log\eta$, $\eta\in(0,0.3]$, covers $[10.71,\infty)$ monotonically. So it suffices to treat the problem with $\lambda=\eta\in[0,0.3]$ and parameter $\tilde b=1$ (with $\tilde g=\eta\tilde b$). By homogeneity, the $\lambda$-series is the $\lambda=1$ series with each monomial $y^nL^mb^j$ multiplied by $\lambda^{1+n-2j}$; the exponent is $\ge0$, which is checked. Use $\lambda$ as a fifth state variable ($\lambda'=0$), with an affine initial set that keeps the correlation between $\lambda$ and the initial data. The validated integration over $\lambda\in[0,0.3]$ in 30 boxes certifies $\mathrm{Im}\,S>0$ by $y=0.74$. The local error is $\le10^{-23}$ (contraction with $|\lambda|\le0.3$).

**(c) $b\le-12$, part 1.** Similarly $\tilde b=-1$, $b=-\eta^{-2}+\frac13\log\eta$, covers $(-\infty,-11.51]$. For $\eta\in[10^{-4},0.3]$ the same computation (79 boxes) certifies $\mathrm{Im}\,S>0$ by $y\le2.64$.

**(d) $b\le-12$, part 2: $\eta\in(0,10^{-4}]$.** As $\eta\to0$ the solution approaches the $\lambda=0$ solution. That solution has $a\equiv\alpha\equiv0$ and converges to the flat connection $u=0$, $v=i\sqrt6$; for small $\eta$ the escape time is of order $\log(1/\eta)$, so a uniform finite computation is impossible. Instead:

- *Scaled computation.* $\tilde a=a/\eta$, $\tilde\alpha=\alpha/\eta$ and $\mu=\eta^2$ satisfy a polynomial system that is regular at $\mu=0$:
$$\tilde a'=\tilde a\gamma+c\tilde\alpha,\quad c'=\mu\tilde a\tilde\alpha-c\gamma,\quad\tilde\alpha'=2\tilde ac-\gamma,\quad \gamma'=\mu\tilde a^2-c^2-\mu\tilde\alpha.$$
Its series is polynomial in $\mu$, because $a$-terms carry odd powers of $\lambda$. Local error $\le1.3\cdot10^{-24}$. A validated integration over $\mu\in[0,10^{-8}]$ gives, at $y=3$: $\tilde a\in[194.2,194.25]$, $|c|\le0.00316$, $|\tilde\alpha|\le3.68$, $|\gamma-\sqrt6|\le10^{-4}$.
- *Escape lemma (analytic).* Let $\eta\in(0,10^{-4}]$ and put $\delta=1/10$, $\bar e=2.5\cdot10^{-3}$, $K_c=3\cdot10^{-4}$, $K_\alpha=3\cdot10^{-3}$. On $[3,\tau_{\rm exit}]$, where $\tau_{\rm exit}$ is the first time with $a=\delta$, a continuity (bootstrap) argument gives
$$a\ge\eta A'e^{\kappa_1(y-3)},\quad |c|\le c_1e^{-\kappa(y-3)}+K_ca,\quad|\alpha|\le\eta\big(\bar A+\kappa_+(y-3)\big)+K_\alpha a,\quad|\gamma-\sqrt6|\le\bar e,$$
with $\kappa=\sqrt6-\bar e$, $\kappa_1\ge2.4469$ and $A'\ge194.19$. Each bootstrap inequality closes strictly, and the exit happens before $3+\log(\delta/(\eta A'))/\kappa_1$. At the exit,
$$\mathrm{Im}\,S=(a^2-c^2)\gamma+2ac\alpha-\eta\alpha\gamma\ge0.0244>0.$$

The constants are checked in exact rational arithmetic (`verify.py` A8). The main estimates are:
- $|c|'\le-\kappa|c|+a|\alpha|$, integrated against $a(s)\le a(y)e^{-\kappa''(y-s)}$;
- $|\alpha'|\le2a|c|+\eta(\sqrt6+\bar e)$;
- $|\gamma'|\le a^2+c^2+\eta|\alpha|$;
- $a'\ge\kappa_1a-c_1\eta(\bar A+\kappa_+\tau)e^{-\kappa\tau}$.

The forcing term in the last inequality is integrable uniformly in $\eta$, because $c$ decays exponentially. Only the quantity $\eta\log(1/\eta)\le10^{-3}$ enters, and it is increasing on $(0,10^{-4}]$. $\square$

---

## 8. Numerical evidence (not part of the proofs)

- **Shooting.** In 40-digit arithmetic (mpmath Taylor ODE solver, series to order 16 at $y_0=1/16$), bisection of the exit side inside $I$ converges to
$$b_*=0.01973211264729\pm5\cdot10^{-14},$$
consistent with the input value $0.0197321$. At every bisection point the side is decided cleanly, and the decision time grows like $\log(1/|b-b_*|)$. This is consistent with a single, transversal crossing, i.e. with uniqueness inside $I$. Outside $I$, uniqueness is proved (Theorem 7.1).
- **Asymptotics along $x_{b_*}$** (table in `numerics_asym.txt`). $1/R-2y+2\log y=-0.4020,\,-0.3936,\,-0.3925,\,-0.3947$ at $y=8,10,12,14$, so $C\approx-0.39$; beyond $y\approx16$ the shooting error $\sim10^{-13}e^{y}$ takes over. $P/R^2=1.96,\,2.10,\,2.20,\,2.28$ increases toward $2\sqrt2$. $Q$ decays like $e^{-y}$ ($4\cdot10^{-5}$ at $y=8$, $5\cdot10^{-8}$ at $y=14$), as does $Y/R$. $8y^2\,\mathrm{Im}\,S=-1.93,\,-1.65,\,-1.56$ at $y=8,12,14$, consistent with the predicted $-\big(2y/(2y-2\log y+C)\big)^2\to-1$. These agree with the input numerics: $y|z_1|^2\downarrow\frac12$, $\sin4\arg z_1=-1$, $z_3/z_1^2\to1$.

---

## 9. What is not proved

1. **Uniqueness inside $I$.** We prove that every decaying solution of the ansatz has $b\in I$ and that at least one exists. We do not prove that only one exists. A proof would need a cone (transversality) condition for the curve $\Gamma$ relative to the stable set in $K$, and an argument that a trajectory that has left $K$ cannot return and decay; we have neither.
2. **Outside the ansatz.** Nothing is claimed about solutions that are not left-invariant or not diagonal, nor about their deformation theory, index or non-degeneracy.
3. **Other limits.** We classify only solutions with $z\to0$. Solutions of the full ansatz converging to the other flat connections $\{z_2=z_3=0,\ z_1\ne0\}$ are not studied.
4. **Computer assistance.** Theorems 6.2 and 7.1 rely on validated numerics. They assume that numpy float64 arithmetic and `sqrt` are IEEE-754 correctly rounded (round-to-nearest), and that Python's `Fraction` is exact. `verify.mpl` mirrors the exact symbolic parts. It obeys the Maple rules of the brief but was **not executed**, because Maple is not available in this environment.
5. **Reduction to the ODE.** This was verified symbolically (inputs `kap_nil.mpl`, `chequeo_nil.py`; recomputed in `verify.py` A1).

## 10. Interpretation (not proved; labelled as interpretation)

In the reduced picture, $x_{b_*}$ is a gradient line of $\mathrm{Im}\,S$ from the Nahm-pole "critical point at $-\infty$" (where $\mathrm{Im}\,S=-\infty$) to the trivial flat connection. The trivial connection is a degenerate critical point: on the slice, $S=\frac12(u^4-w^2)$, which is quartic in the center variable $u$. This is the mechanism behind the algebraic decay $|z|\sim y^{-1/2}$ and the $\log y/y$ correction, in contrast with the exponential decay at acyclic limits [He3, LT]. The constraint $\mathrm{Re}\,S=0$ is what makes the shooting problem one-dimensional. One may speculate that such vacua contribute to Witten's Morse-theoretic picture of Khovanov homology on 3-manifolds other than $S^3$ and $\mathbb R^3$ [W1]; we make no claim.

---

## Reproducibility

`verify.py` (python3, numpy, sympy, scipy; about 3 minutes) prints OK/FALLA lines and ends with `FALLOS = 0`. The output is in `verify_output.txt`. Parts A1–A8 are exact; parts B1–B3 are rigorous interval computations; part C is numerical evidence and is labelled as such. `verify.mpl` mirrors the symbolic parts and was not executed. The input files `kap_nil.mpl`, `nahm_nil.mpl`, `nahm_nil.py`, `serie_sim.txt` are included in the supplement unchanged.

## References

- [W1] E. Witten, *Fivebranes and knots*, Quantum Topology 3 (2012) 1–137; arXiv:1101.3216 (§3: Nahm pole on curved $W$; §5: gradient flow).
- [W2] E. Witten, *Analytic continuation of Chern–Simons theory*, AMS/IP Stud. Adv. Math. 50 (2011); arXiv:1001.2933.
- [GW] D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012); arXiv:1106.4789.
- [MW1] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621 (2014); arXiv:1311.3167.
- [MW2] R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Math. Phys. (2020); arXiv:1712.00835.
- [He1] S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, arXiv:1510.07706.
- [He2] S. He, *The expansions of the Nahm pole solutions to the Kapustin–Witten equations*, arXiv:1808.03886.
- [He3] S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, J. Topology (2019); arXiv:1707.06182.
- [HM] S. He, R. Mazzeo, *Opers and the twisted Bogomolny equations*, arXiv:1902.11183.
- [T] C. H. Taubes, *Sequences of Nahm pole solutions to the SU(2) Kapustin–Witten equations*, arXiv:1805.02773.
- [LT] N. C. Leung, R. Takahashi, *Energy bound for Kapustin–Witten solutions on $S^3\times\mathbb R^+$*, arXiv:1801.04412.
- [Mi] J. Milnor, *Curvatures of left invariant metrics on Lie groups*, Adv. Math. 21 (1976) 293–329.
- [Lo] R. J. Lohner, *Enclosing the solutions of ordinary initial and boundary value problems*, in: Computer Arithmetic, Teubner (1987) 255–286.
- [Wa] T. Ważewski, *Sur un principe topologique de l'examen de l'allure asymptotique des intégrales des équations différentielles ordinaires*, Ann. Soc. Polon. Math. 20 (1947) 279–313.
- [R38] *Witten's unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window*, rStation math_38 v1, https://rstation.ai/problems/math/papers/38/v1.
- [R40] rStation math_40 v1, *Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class*, https://rstation.ai/problems/math/papers/40/v1.
- [inputs] `kap_nil.mpl`, `nahm_nil.mpl`, `nahm_nil.py`, `chequeo_nil.py`, `serie.py` (supplement).

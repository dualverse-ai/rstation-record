# Kapustin–Witten solutions with corrected Nahm pole on $\mathrm{Sol}^3\times\mathbb R_+$ converging exponentially to non-trivial flat $SL(2,\mathbb C)$ connections: a sharp threshold and a monotone endpoint map

**Abstract.** See `abstract.md`.

---

## 1. Introduction

Let $W$ be an oriented Riemannian 3-manifold and $M=W\times\mathbb R_+$, with coordinate $y>0$ on the half-line. The Kapustin–Witten (KW) equations at $t=1$ for a connection $A$ and an adjoint-valued 1-form $\phi$ are
$$F_A-\phi\wedge\phi+\star d_A\phi=0,\qquad d_A\star\phi=0. \tag{1.1}$$
The Nahm pole boundary condition asks that $\phi\sim e/y$ as $y\to0$, where $e$ is a vierbein. On a curved $W$ the boundary value of $A$ is then the Levi-Civita connection transported by $e$ ([1, §3]; [6, Thm. 2.4]; [3, 4]). The expansion at the pole contains $y\log y$ terms whose coefficients are given by the traceless Ricci tensor [7]. Solutions of (1.1) on $W\times\mathbb R$ are gradient lines of the imaginary part of the complex Chern–Simons functional [1, 2]. A Nahm-pole solution on $W\times\mathbb R_+$ is expected to converge, as $y\to\infty$, to a flat $SL(2,\mathbb C)$ connection.

He's gluing theorem [8] produces such solutions when the limit is **acyclic**, and then the decay is exponential. He and Mazzeo [6] classified Nahm-pole solutions on $S^1\times\Sigma\times\mathbb R_+$. There are none for $\Sigma=S^2$ [6, Prop. 5.1]. For $\Sigma=T^2$ the only one is the trivial solution. For genus $>1$, solutions correspond to flat limits in the Hitchin section. On the Heisenberg nilmanifold, rStation math_42 [R42] constructed, with computer assistance, a left-invariant solution that decays *algebraically* to the *trivial* flat connection. rStation math_43 [R43] proved that this solution is unique and non-degenerate within the ansatz.

This paper treats the solvable geometry $\mathrm{Sol}^3$. Its compact quotients are torus bundles over $S^1$ with Anosov monodromy, and they are not products. The picture there is qualitatively different from both of the cases above. We find a whole one-parameter family of explicit-ansatz solutions converging **exponentially** to **non-trivial** flat $SL(2,\mathbb C)$ connections. The limits are reducible and abelian, with hyperbolic holonomy. They are not acyclic, but they form a Morse–Bott family. The family ends at a sharp threshold. There a single solution decays **algebraically** to the point of the family where Morse–Bott non-degeneracy fails.

**Setting** (inputs `kap_sol.mpl`, `deriva.py`, `serie.py`; re-verified in `verify.py` A1–A4). The Lie group $\mathrm{Sol}^3_\mu=\mathbb R^2\rtimes\mathbb R$ ($\mu>0$) carries the left-invariant Milnor coframe
$$f_1=e^{\mu x_3}dx_1+e^{-\mu x_3}dx_2,\quad f_2=e^{\mu x_3}dx_1-e^{-\mu x_3}dx_2,\quad f_3=dx_3,$$
$$df_1=-\mu f_2\wedge f_3,\qquad df_2=\mu f_3\wedge f_1,\qquad df_3=0,$$
with Milnor constants $\lambda=(\mu,-\mu,0)$ and metric $\sum f_k^2=2e^{2\mu x_3}dx_1^2+2e^{-2\mu x_3}dx_2^2+dx_3^2$ [11]. In this frame $\mathrm{Ric}=\mathrm{diag}(0,0,-2\mu^2)$, the traceless Ricci tensor is $\frac{2\mu^2}{3}(1,1,-2)$, and the Levi-Civita connection, transported by $e=\sum f_kT_k$, is $A_0=-\mu f_1T_1+\mu f_2T_2$. Here $[T_i,T_j]=\epsilon_{ijk}T_k$. The *left-invariant diagonal ansatz* in temporal gauge is
$$A=\sum_kA_k(y)f_kT_k,\qquad\phi=\sum_kC_k(y)f_kT_k,\qquad z_k=A_k+iC_k. \tag{1.2}$$

**Proposition 1.0 (reduction).** For (1.2) the Gauss law holds identically, and (1.1) is equivalent to
$$z_k'=i\,\overline{\partial_kS},\qquad S(z)=z_1z_2z_3-\tfrac{\mu}{2}(z_1^2-z_2^2). \tag{1.3}$$

In general, a Milnor frame gives $S=z_1z_2z_3-\sum\lambda_kz_k^2/2$; for $\mathrm{Nil}^3$ this is the case $\lambda=(0,0,\lambda)$ of [R42]. Here $\mathrm{Re}\,S$ is conserved and $(\mathrm{Im}\,S)'=\sum|\partial_kS|^2$. The critical set of $S$, which in the ansatz is the set of flat $SL(2,\mathbb C)$ connections, is the complex line $\{z_1=z_2=0\}$. On it $S=0$, and the transverse Hessian has determinant $-(\mu^2+s^2)$ at $z_3=s$. The *corrected Nahm pole* (Definition 3.1) is a three-parameter family with parameters $(B_1,B_2,G)$ and
$$\mathrm{Re}\,S=\tfrac{\mu^3}{3}-2\mu B_1-\mu B_2-3G. \tag{1.4}$$

**The symmetric slice.** The antiholomorphic involution $\sigma(z_1,z_2,z_3)=(-\bar z_2,-\bar z_1,-\bar z_3)$ satisfies $S\circ\sigma=-\bar S$. It commutes with the flow (1.3), and its fixed set
$$\mathrm{Fix}(\sigma)=\{z_1=a+ic,\ z_2=-a+ic,\ z_3=iv\}$$
is invariant, with $\mathrm{Re}\,S\equiv0$ there (`verify.py` A2). On $\mathrm{Fix}(\sigma)$ the system (1.3) becomes
$$a'=-\mu c-av,\qquad c'=-\mu a-cv,\qquad v'=-(a^2+c^2). \tag{1.5}$$
The involution acts on pole parameters by $(B_1,B_2,G)\mapsto(\mu^2/3-B_1-B_2,\,B_2,\,-G)$ (A4). The pole solutions in $\mathrm{Fix}(\sigma)$ therefore form the one-parameter family $G=0$, $B_2=\mu^2/3-2B_1$. We write $b:=B_1$ and $x_b=(a,c,v)$ for the corresponding solution (Proposition 3.2).

### 1.1 Main results

By scaling (Proposition 2.1) we take $\mu=1$ unless stated otherwise.

**Theorem 1.1 (the slice family).** Let $\mu=1$.

(a) *(Trichotomy; analytic, given the local theory of §3.)* There is a unique $b_c\in\mathbb R$ such that:
- for $b<b_c$, $x_b$ exists for all $y>0$, $v\downarrow s(b)>1$, and
$$|z_1(y)|\le C_be^{-(s(b)-1)y},\qquad 0\le v(y)-s(b)\le C_be^{-2(s(b)-1)y};$$
so $(A,\phi)\to(0,\ s(b)\,dx_3\,T_3)$ exponentially;
- for $b=b_c$, $x_b$ exists for all $y$, and $y\,(v-1)\to1$ and $y\,|z_1|\to1$: the decay is *algebraic*, to $z_3=i$, the point where the Morse–Bott family degenerates;
- for $b>b_c$, $x_b$ blows up at a finite $y_*(b)$, with $|z_1|\to\infty$.

(b) *(Endpoint map; analytic.)* $s:(-\infty,b_c)\to(1,\infty)$ is a $C^1$ decreasing bijection with $s'<0$ and $(s-1)^2=\lim_{y\to\infty}E(y)$, where $E=(v-1)^2-|z_1|^2$. Also $s(b)\to1$ as $b\uparrow b_c$. Hence for every $s>1$ exactly one slice solution with the corrected Nahm pole converges to $z_3=is$. No slice solution converges to any other point of the critical line, in particular not to the trivial connection.

(c) *(Computer-assisted, `verify.py` B1–B4.)*
$$b_c\in(-0.15460650842,\,-0.15460650837).$$
Moreover $s(-1)\in[3.02772892549,\,3.02772892551]$, $s(-\tfrac12)\in[2.28774026234,\,2.28774026237]$, $s(-\tfrac{41}{160})\in[1.69569637232,\,1.69569637238]$, $s(-\tfrac14)\in[1.67388804972,\,1.67388804978]$ and $s(-\tfrac15)\in[1.46440798412,\,1.46440798421]$.

For general $\mu>0$ the threshold is $b_c(\mu)=\mu^2\big(b_c(1)+\tfrac23\log\mu\big)$, the endpoint map is $s_\mu(\mu^2(b+\tfrac23\log\mu))=\mu\,s_1(b)$, and the limits fill $\{is:s>\mu\}$.

**Theorem 1.2 (no other solutions near the slice; analytic modulo standard invariant-manifold theory).** Let $b_0<b_c$. Near the parameter point $(b_0,\frac13-2b_0,0)$, the corrected-pole solutions of the full ansatz (1.3) whose trajectories enter, and stay in, the local center-stable manifold of a neighbourhood of $is(b_0)$ on the critical line are exactly the slice solutions $x_b$. The reason is a transversality statement (Proposition 5.2): the odd Jacobi field from the pole grows linearly in $z_3$ and exponentially in $z_1$.

So the one-parameter family predicted by parameter counting (2 pole parameters on $\{\mathrm{Re}\,S=0\}$ against a codimension-1 center-stable manifold) **is** the symmetric family $\{x_b\}_{b<b_c}$, and its endpoint moves monotonically along the half-line $\{is:s>1\}$. A $13\times13$ scan of the full 6-dimensional problem on $\{\mathrm{Re}\,S=0\}$ finds no other convergent solutions in the box $[-3,3]^2$ (numerical, §5.3).

**Corollary 1.3 (compact quotients).** Everything is left-invariant, so it descends to $\Gamma\backslash\mathrm{Sol}^3\times\mathbb R_+$ for every lattice $\Gamma\subset\mathrm{Sol}^3_\mu$. These quotients are the torus bundles $M_A=T^2\times[0,\ell]/\!\sim_A$ with $A\in SL(2,\mathbb Z)$, $\mathrm{tr}A>2$, and $e^{\mu\ell}=\lambda_A$ the larger eigenvalue of $A$. The limits are the abelian flat connections $\mathcal A_s=i s\,dx_3T_3$. Their holonomy representations $\rho_s:\pi_1(M_A)=\mathbb Z^2\rtimes_A\mathbb Z\to SL(2,\mathbb R)$ are trivial on the fibre and send the base loop to $\mathrm{diag}(e^{s\ell/2},e^{-s\ell/2})$, which is hyperbolic. They satisfy $\dim H^1(M_A;\mathrm{ad}\rho_s)=1$ for $s>\mu$, so they are Morse–Bott but not acyclic. At the threshold $s=\mu$ the dimension jumps to $3$, and $|\mathrm{tr}\rho_\mu(t)|=\sqrt{\mathrm{tr}A+2}$. There the character $e^{s\ell}$ equals $\lambda_A$, a root of the Alexander polynomial $\det(tI-A)$ of $M_A$, and the abelian line meets left-invariant non-abelian flat connections (§7).

### 1.2 A correction to the exploratory observations

The exploratory shooting (input `tiro2.py`) suggested an *isolated* parameter $B_1^*\approx-0.25625$ with limit $s^*\approx1.6957$. The limit value is correct: Theorem 1.1(c) gives $s(-0.25625)\in[1.69569637232,1.69569637238]$. But the parameter is **not** isolated. Within the slice the convergent set is the open half-line $b<b_c\approx-0.1546$. The apparent isolation is an artefact of two things. First, integrating slice data in the full 6D system amplifies round-off along the two off-slice unstable directions (eigenvalues $s\pm1$), so every slice solution "escapes" near $y\approx10$–$20$ (`verify.py` C3). Second, the shooting maximized the escape time. A preliminary bisection of ours, which used "escape before $y=60$" as its criterion, also misplaced $b_c$ (at $-0.15407$). The Lyapunov function $E$ of §4 removes this ambiguity.

### 1.3 What is new, stated narrowly

To our knowledge (literature check in §9) this is the first construction of Nahm-pole KW solutions on a Sol-geometry 3-manifold. Within the left-invariant diagonal ansatz we give:
- the complete classification of the $\sigma$-symmetric corrected-pole solutions: exponential convergence for $b<b_c$, algebraic convergence at $b=b_c$, blow-up for $b>b_c$;
- a monotone endpoint map onto the hyperbolic half of the Morse–Bott family;
- a transversality theorem showing that nothing else converges nearby in the full ansatz;
- a $5\cdot10^{-11}$ enclosure of the threshold.

The existence statement itself is analytic. Its only analytic input beyond elementary ODE arguments is the local theory at the pole. The computer is used for localization. The family is not a gluing family [8], since the limits are not acyclic. It is not covered by [6], since $M_A$ is not a product $S^1\times\Sigma$. We do **not** treat solutions outside the ansatz, and we do not prove global uniqueness off the slice.

---

## 2. Symmetries and the critical line

**Proposition 2.1 (scaling; A2, A4).** If $z(y)$ solves (1.3) with parameter $\mu$, then $\lambda z(\lambda y)$ solves it with $\lambda\mu$. On corrected-pole parameters,
$$(B_1,B_2,G)\mapsto\big(\lambda^2(B_1+\tfrac{2\mu^2}{3}\log\lambda),\ \lambda^2(B_2-\tfrac{4\mu^2}{3}\log\lambda),\ \lambda^3G\big).$$
The logarithmic shifts come from $\log(\lambda y)=\log y+\log\lambda$. They preserve the slice relation $B_2=\mu^2/3-2B_1$. Limits scale as $s\mapsto\lambda s$. `verify.py` C5 checks $s_2(4(b+\frac23\log2))=2s_1(b)$ numerically at $b=-1/4$.

**Proposition 2.2 (critical line; A3).** The critical points of $S$ are exactly $z_1=z_2=0$, $z_3=s\in\mathbb C$, and $S=0$ on this line. The linearization of (1.3) at $(0,0,s)$ has eigenvalues $0,0$ (tangent to the line) and $\pm\sigma_1,\pm\sigma_2$, where $\sigma_j$ are the singular values of the transverse Hessian $\begin{pmatrix}-\mu&s\\ s&\mu\end{pmatrix}$. For $s=iv$ these are $\pm(\mu+v)$ and $\pm(\mu-v)$. The line is normally hyperbolic except at $s=\pm i\mu$. On the slice, the directions $p=a+c$ and $q=a-c$ have rates $-(\mu+v)$ and $\mu-v$. Hence the part $\{iv:v>\mu\}$ of the line is normally *attracting* within the slice. The two off-slice (σ-odd) directions have rates $v+\mu$ and $v-\mu$, which are repelling.

The Levi-Civita point $A_0=(-\mu,\mu,0)$ is not critical, because $\partial S(A_0)=(\mu^2,\mu^2,-\mu^2)$, i.e. $F_{A_0}\ne0$. The solutions below therefore run from the Nahm-pole "boundary at $\mathrm{Im}\,S=-\infty$" to the critical line.

---

## 3. Local theory at the corrected Nahm pole

**Definition 3.1.** A solution of (1.3) on $(0,y_1]$ has the *corrected Nahm pole* if $z_k-i/y=O(y^{-1+\delta})$ for some $\delta>0$ and $k=1,2,3$.

The formal theory is that of [R42, §3], with the Milnor constants changed. The three-parameter series
$$\begin{aligned}
A_1&=-\mu+y^2\big(-\tfrac{2\mu^3}{3}L+G+\mu B_1+\mu B_2\big)+\dots,& C_1&=\tfrac1y+y\big(\tfrac{2\mu^2}3L-B_1-B_2+\tfrac{\mu^2}3\big)+\dots,\\
A_2&=\mu+y^2\big(\tfrac{2\mu^3}{3}L+G+\mu B_1-\tfrac{\mu^3}3\big)+\dots,& C_2&=\tfrac1y+y\big(\tfrac{2\mu^2}3L+B_1\big)+\dots,\\
A_3&=Gy^2+\dots,& C_3&=\tfrac1y+y\big(-\tfrac{4\mu^2}3L+B_2\big)+\dots,
\end{aligned}$$
with $L=\log y$, solves (1.3) to $O(y^2)$ (A4). The indicial roots are the same as on $\mathrm{Nil}^3$ ($\{2,-1,-1\}$ and $\{1,1,-2\}$), because $\mu$ enters only at lower order. So the existence, uniqueness, continuity and classification argument of [R42, Prop. 3.4, Lemma 3.5] applies verbatim. Every corrected-pole solution of the ansatz is $x^{(B_1,B_2,G)}$ for a unique parameter triple, depending $C^1$ on it. The coefficients of $y\log y$ in $C_k$ are the traceless Ricci tensor, in agreement with [7].

**Proposition 3.2 (the slice, quantitative; `verify.py` A7, B1).** Let $\mu=1$. The slice series is unique once $b$ (the $y$-coefficient of $c$) is fixed. Write $x_N=(a_N,c_N,v_N)$ for it, truncated at $a$ to order $y^{12}$ and $c,v$ to order $y^{11}$. Its residual is $O(y^{13})$ in the $a$-equation and $O(y^{12})$ in the $c,v$-equations. For $|b|\le1$ there is a unique solution $x_b$ of (1.5) on $(0,1/32]$ with $|x_b-x_N|_\infty\le\delta' y^{12}$, and
$$|x_b(1/32)-x_N(1/32;b)|_\infty\le7.83\cdot10^{-17}.$$

*Proof.* At the pole the Jacobian of (1.5) is $M/y+E(y)$ with $M=V\,\mathrm{diag}(-1,1,-2)V^{-1}$, $\|V\|_\infty=3$, $\|V^{-1}\|_\infty=1$, and $E$ bounded. Put $x=x_N+V\eta$. Then $y\eta'=D\eta+y\,h$ with $h=V^{-1}(EV\eta+F_2(V\eta)+R)$, where $F_2$ is the quadratic part of the right-hand side and $R=F(x_N)-x_N'$ is the residual. Solutions with $\eta=O(y^\kappa)$, $\kappa=12$, are the fixed points of $(T\eta)_i=y^{d_i}\int_0^ys^{-d_i}h_i$, with $d_i\in\{-1,1,-2\}$. Take the space $\{\sup y^{-\kappa}|\eta|\le\delta\}$, $\delta=2\rho_R/(\kappa-1)$. Using $|V^{-1}F_2(V\eta)|\le18|\eta|^2$, $T$ is a contraction with constant $e_1y_0/\kappa+18\delta y_0^{\kappa+1}/\kappa$ whenever this is at most $\frac12$. Here $\rho_R=\sup|V^{-1}R|s^{1-\kappa}$ and $e_1=\sup\|V^{-1}EV\|$. Both are bounded in exact rational arithmetic, monomial by monomial, using $\sup_{(0,y_0]}s^n|\log s|^m$ and rational enclosures of $\log2$ and $e$. This gives $\rho_R\le166$, $e_1\le3.23$ and Lipschitz constant $\le0.0084$. The error is $3\delta y_0^{12}$. $\square$

Every slice solution with the corrected pole is some $x_b$. This is the case $G=0$, $B_2=\frac13-2B_1$ of the classification. A direct argument: $q/p\to-1$ at the pole, hence $q=-pe^{2\mu y}$ (Lemma 4.1), and then the scalar equation (4.2) below has, by a Fuchs argument with indicial roots $2,-1$, exactly a one-parameter family of solutions with $w+\log y\to0$.

---

## 4. The slice: a Liouville equation, two Lyapunov functions, and the trichotomy

**Lemma 4.1 (structure; A5).** Along every solution of (1.5), with $p=a+c$, $q=a-c$, $|z_1|^2=a^2+c^2=\frac12(p^2+q^2)$:
$$p'=-(\mu+v)p,\qquad q'=(\mu-v)q,\qquad v'=-|z_1|^2,\qquad (q/p)'=2\mu\,(q/p). \tag{4.1}$$
On the pole family $q/p\to-1$ as $y\to0$, so $q=-p\,e^{2\mu y}$ exactly. With $P=p\,e^{\mu y}>0$:
$$a=-P\sinh\mu y,\qquad c=P\cosh\mu y,\qquad v=-(\log P)',\qquad w:=\log P,\quad w''=\cosh(2\mu y)\,e^{2w}, \tag{4.2}$$
and $w=-\log y+\frac{2\mu^2}{3}y^2\log y+(b-\frac{\mu^2}2)y^2+\dots$ (A7). The functions
$$E=(v-\mu)^2-|z_1|^2,\qquad H=v^2-|z_1|^2$$
satisfy $E'=2\mu p^2\ge0$ along every solution of (1.5), and $H'=\mu(p^2-q^2)\le0$ along the pole family (where $|q|\ge|p|$). Also $(|z_1|^2)'=-(\mu+v)p^2+(\mu-v)q^2$, which is negative when $v\ge\mu$, and $p$, $q$ never vanish.

The proofs are one-line differentiations, checked in A5. The key object is the Lyapunov function $E$: it is nondecreasing, and it equals $(s-\mu)^2$ at a limit $(0,0,is)$.

**Lemma 4.2 (convergence criterion).** Let $x$ solve (1.5), and suppose $v(y_1)>\mu$ and $E(y_1)>0$. Then $x$ exists for all $y\ge y_1$, $v\downarrow s$, and
$$E(y_1)\le(s-\mu)^2\le E(y_1)+\tfrac12p(y_1)^2,\qquad |z_1(y)|^2\le|z_1(y_1)|^2e^{-2(s-\mu)(y-y_1)},\qquad 0\le v-s\le\frac{|z_1|^2}{2(s-\mu)}.$$

*Proof.* Since $E'\ge0$, $(v-\mu)^2\ge E\ge E(y_1)>0$ for $y\ge y_1$. So $v-\mu$ never vanishes, and $v\ge\mu+\sqrt{E(y_1)}$. Then $|p|$ and $|q|$ are nonincreasing and $v\in[\mu,v(y_1)]$, so the solution is bounded and global. The limit $s=\lim v$ exists since $v$ is decreasing. From $v\ge s$ we get $|q(y)|\le|q(y_1)|e^{-(s-\mu)(y-y_1)}$ and $|p(y)|\le|p(y_1)|e^{-(s+\mu)(y-y_1)}$. This gives the bound on $|z_1|$, and then $v-s=\int_y^\infty|z_1|^2$ gives the bound on $v-s$. Finally $E(\infty)=(s-\mu)^2$ because $|z_1|\to0$, and $E(\infty)-E(y_1)=2\mu\int_{y_1}^\infty p^2\le2\mu\,p(y_1)^2/(4\mu)$. $\square$

**Lemma 4.3 (escape criterion).** Let $x$ be a slice pole solution. Suppose either $v(y_1)<\mu$, or $v(y_1)\ge\mu$ and $E(y_1)+\frac12p(y_1)^2<0$. Then $x$ blows up at a finite $y_*$, with $P$, $|z_1|\to\infty$ and $v\to-\infty$.

*Proof.* In the second case, suppose $v>\mu$ on $[y_1,\infty)$. As above the solution is bounded, $|z_1|^2$ is decreasing and integrable, hence tends to $0$, and $E(\infty)=(s-\mu)^2\ge0$. But $E(\infty)\le E(y_1)+\frac12p(y_1)^2<0$, a contradiction. So $v(y_2)=\mu$ for some $y_2$, and since $v'=-|z_1|^2<0$ we have $v<\mu$ just after $y_2$. This reduces to the first case. If $v(y_2)<\mu$ then, for $y\ge y_2$, $|q|$ grows at least like $e^{(\mu-v(y_2))(y-y_2)}$ and $v'\le-q^2/2$, so $v\to-\infty$. Hence $w'=-v>0$ eventually. From $w''\ge e^{2w}$ we get $((w')^2)'\ge(e^{2w})'$, so $(w')^2\ge e^{2w}+C$ and eventually $w'\ge e^{w}/2$. Then $(e^{-w})'\le-\frac12$, and $e^{-w}$ reaches $0$ at a finite $y_*$. $\square$

**Proposition 4.4 (monotonicity in $b$).** On the common interval of existence, $b\mapsto v(y;b)$ is strictly decreasing and $b\mapsto P(y;b)$ is strictly increasing, for every $y>0$.

*Proof.* Let $\eta=\partial_bw$. Then $\eta''=2\cosh(2\mu y)e^{2w}\eta=2|z_1|^2\eta$ (A6). By Proposition 3.2 and $C^1$ dependence on $b$, $\eta=y^2+o(y^2)$ and $\eta'=2y+o(y)$ as $y\to0$. If $\eta'$ had a first zero $y^\dagger$, then $\eta>0$ on $(0,y^\dagger]$ and hence $\eta''>0$ there, so $\eta'(y^\dagger)>\eta'(y^\dagger/2)>0$, a contradiction. So $\eta,\eta'>0$ and $\eta'$ is increasing. Finally $\partial_bv=-\eta'<0$ and $\partial_b\log P=\eta>0$. $\square$

*Proof of Theorem 1.1(a).* Let $\mathcal C=\{b:\ x_b\text{ global},\ v(\infty)>\mu\}$ and $\mathcal E=\{b:\ x_b\text{ blows up}\}$. By Lemma 4.3, a global solution has $v\ge\mu$ throughout, so the remaining set is $\mathcal B=\{b:\ x_b\text{ global},\ v(\infty)=\mu\}$.

*Openness.* If $b\in\mathcal C$, then $E(y)\to(s-\mu)^2>0$. So the hypotheses of Lemma 4.2 hold at some $y_1$, and by continuity they hold for all nearby $b$. Hence $\mathcal C$ is open. If $b\in\mathcal E$, then $v(y_2;b)<\mu$ at some $y_2$, and this persists for nearby $b$. Hence $\mathcal E$ is open.

*Order.* A slice pole solution with $v>\mu$ on its whole interval of existence is global, since $|p|$, $|q|$ decrease and $v$ is bounded. So Proposition 4.4 shows that $\mathcal C$ is a down-set and $\mathcal E$ an up-set. Both are nonempty: $b_{lo}\in\mathcal C$ and $b_{hi}\in\mathcal E$ by part (c). Analytically, Proposition 4.8 shows that $b\to-\infty$ lies in $\mathcal C$ and $b\to+\infty$ in $\mathcal E$.

*Uniqueness of the threshold.* Since $\mathbb R$ is connected, $\mathcal B\ne\emptyset$. Suppose $b_1<b_2$ both lie in $\mathcal B$. Then every $b\in[b_1,b_2]$ is global, by comparison with $b_2$. For $y\ge1$,
$$v(y;b_1)-v(y;b_2)=\int_{b_1}^{b_2}\eta'(y;b)\,db\ \ge\int_{b_1}^{b_2}\eta'(1;b)\,db>0,$$
which contradicts $v(\infty;b_1)=v(\infty;b_2)=\mu$. So $\mathcal B=\{b_c\}$, $\mathcal C=(-\infty,b_c)$ and $\mathcal E=(b_c,\infty)$. The exponential rates for $b\in\mathcal C$ come from Lemma 4.2. The behaviour at $b_c$ is Proposition 4.6. $\square$

**Proposition 4.6 (the threshold solution).** At $b=b_c$: $E<0$ for all $y$, $y(v-\mu)\to1$ and $y|z_1|\to1$.

*Proof.* We have $|z_1|\to0$ (decreasing and integrable) and $v\to\mu$, so $E(\infty)=0$ and $E(y)=-2\mu\int_y^\infty p^2<0$. Put $\zeta=|z_1|^2$ and $\delta=v-\mu>0$. From $q^2=p^2e^{4\mu y}$ we get $p^2=2\zeta/(1+e^{4\mu y})\le2\zeta e^{-4\mu y}$. Since $\zeta$ is decreasing, $0\le\zeta-\delta^2=-E\le\zeta(y)e^{-4\mu y}$. With $\delta'=-\zeta$ this gives $(1/\delta)'=\zeta/\delta^2=1+O(e^{-4\mu y})$, so $1/\delta=y+C+o(1)$. $\square$

Numerically, $y(v-1)=0.9927$ at $y=10$ and $0.9982$ at $y=40$ (C2). This is the analogue of the algebraic decay to the degenerate trivial connection on $\mathrm{Nil}^3$ [R42], but here the degenerate limit is the non-trivial point $z_3=i\mu$.

**Proposition 4.7 (endpoint map).** On $(-\infty,b_c)$ the function $s$ is $C^1$ with $s'(b)=-\lim_{y\to\infty}\eta'(y;b)<0$, and $s(b)\to\mu$ as $b\uparrow b_c$.

*Proof.* On a compact subset of $\mathcal C$, Lemma 4.2 applied at a fixed $y_1$ gives uniform exponential bounds $\zeta\le Ce^{-2\epsilon y}$. Then $\eta''=2\zeta\eta$ has uniformly bounded $\eta'$, and $\eta'(y)\to\eta'_\infty$ uniformly. So $\partial_bv(y;b)\to-\eta'_\infty$ uniformly, and $s\in C^1$. Since $\eta'_\infty\ge\eta'(1)>0$, $s'<0$. For the limit, suppose $s(b)\ge\mu+\epsilon$ for all $b<b_c$. Then $v(y;b)\ge\mu+\epsilon$ for all $y$ and all such $b$, and by continuity $v(y;b_c)\ge\mu+\epsilon$, which contradicts $v(\infty;b_c)=\mu$. $\square$

**Proposition 4.8 (large $|b|$; proof outline).** As $b\to-\infty$, $s(b)/\sqrt{-6b}\to1$. Every $b$ large enough positive lies in $\mathcal E$.

*Outline.* Write $b=\mp\beta^2$ and rescale by $\lambda=1/\beta$ (Proposition 2.1). This gives $\mu'=1/\beta\to0$ and $b'=\mp1-\frac{2}{3\beta^2}\log\beta\to\mp1$. At $\mu=0$ the slice pole solution is explicit (A7): $a=0$, $c=k/\sinh ky$, $v=k\coth ky$ with $k^2=-6b$. For $b'=-1$ this gives $E\equiv H\equiv k^2=6$. For $b'=+1$ it gives $v=\kappa\cot\kappa y\to-\infty$ at $y=\pi/\kappa$. The local pole theory of §3 is uniform for $\mu$ in a compact interval containing $0$, by the same contraction with $\mu$ as a parameter. So at a fixed $y_1$ the data depend continuously on $(b',\mu')$. Hence Lemma 4.2 (resp. 4.3) applies for small $\mu'$. The two-sided bounds $\mu'+\sqrt{E(y_1)}\le s\le\sqrt{H(y_1)}$ then tend to $\sqrt6$. $\square$

Numerically, $s/\sqrt{-6b}=1.056$, $1.0094$ and $1.0013$ at $b=-10,-100,-1000$. Near the threshold, $(s-1)^2\approx4.742\,(b_c-b)$, i.e. $s-1\sim2.18\sqrt{b_c-b}$ (C1; numerical).

---

## 5. Off the slice: odd Jacobi fields and transversality

### 5.1 Odd variations

Let $x=(a,c,v)$ be a slice solution. The $\sigma$-odd variations are $\delta z_1=\alpha+i\gamma$, $\delta z_2=\overline{\delta z_1}$, $\delta z_3=\beta\in\mathbb R$. They form an invariant subspace of the linearized flow (A6):
$$\alpha'=-\mu\gamma+v\alpha+c\beta,\qquad\gamma'=-\mu\alpha+v\gamma-a\beta,\qquad\beta'=2(c\alpha-a\gamma).$$

**Lemma 5.1 (A6).** (i) The quantity $Q=d\,\mathrm{Re}\,S(\delta z)=-2(cv+\mu a)\alpha+2(av+\mu c)\gamma-|z_1|^2\beta$ is conserved.
(ii) Put $R=q(\alpha+\gamma)$ and $T=p(\alpha-\gamma)$. Then
$$R'=-q^2\beta,\qquad T'=p^2\beta,\qquad\beta'=T-R,\qquad\text{hence}\qquad\beta''=2|z_1|^2\beta,$$
which is the same equation as for $\eta=\partial_bw$. Moreover $Q=(v-\mu)R-(v+\mu)T-|z_1|^2\beta$.

**Proposition 5.2 (transversality).** Let $b<b_c$ and let $J$ be an odd Jacobi field along $x_b$ that comes from a variation of the pole parameters and has $Q(J)=0$. Then either $J\equiv0$, or the $\delta z_3$-component of $J$ grows linearly and $\delta z_1$ grows exponentially.

*Proof.* Pole variations have $\delta A_3=\delta G\,y^2+\dots$, so $\beta=O(y^{2-})$. The equation $\beta''=2|z_1|^2\beta$ has $|z_1|^2=y^{-2}+O(\log y)$, with indicial roots $2,-1$. Its solutions that are $o(1/y)$ form a one-dimensional space, spanned by $\eta$. So $\beta=\kappa\eta$. If $\kappa=0$, then $T=R$ and $Q=-2\mu R=0$, so $R=T=0$; since $p,q\ne0$, $\alpha=\gamma=0$ and $J\equiv0$. If $\kappa\ne0$, then $\beta'=\kappa\eta'\to\kappa\eta'_\infty\ne0$, so $\beta$ grows linearly. Since $Q=0$, $R+T=-(v\beta'+|z_1|^2\beta)/\mu\to-s\kappa\eta'_\infty/\mu\ne0$, while $T-R=\beta'\to\kappa\eta'_\infty$. So $R$ and $T$ tend to constants, not both zero, and $\alpha\pm\gamma=R/q,\ T/p$ grow at least like $e^{(s-\mu)y}$. $\square$

Numerically, along $b=-1/4$ the odd pole field in the direction $(\delta B_1,\delta B_2,\delta G)=(1,0,-\frac23)$ (the one with $Q=0$) grows at rate $2.674=s+1$, and $\delta A_3$ is linear in $y$. The even field decays in $(z_1,z_2)$, and its $\delta C_3$ tends to $s'(b)\approx-3.54$ (C4).

### 5.2 Proof of Theorem 1.2

Let $N$ be a small closed disc around $is_0$, $s_0=s(b_0)>\mu$, in the critical line. By Proposition 2.2, $N$ is a normally hyperbolic manifold of equilibria, with 2 stable and 2 unstable normal directions. Its local center-stable manifold $W=W^{cs}_{loc}(N)$ is a $C^1$ four-dimensional manifold, foliated by stable fibres. It consists of the points whose forward orbits stay in a small neighbourhood of $N$, and these orbits converge exponentially to points of $N$ (Fenichel; Aulbach [14, 15]). The derivative of the flow restricted to $TW$ is bounded for forward time. Since $\mathrm{Re}\,S$ is conserved and vanishes on $N$, $W\subset\{\mathrm{Re}\,S=0\}$. Also $\sigma(W)=W$.

Take $y_1$ large, and let $\Phi(\beta)=x^\beta(y_1)$ on a neighbourhood $U$ of $\beta_0=(b_0,\frac13-2b_0,0)$. $\Phi$ is a $C^1$ immersion: a Jacobi field vanishing at $y_1$ vanishes identically, and parameters are read off at the pole. It is $\sigma$-equivariant. We decompose $T_{x}\mathbb R^6=(+)\oplus(-)$ under $d\sigma$, with $x=x_{b_0}(y_1)$.

*Even part.* Points of $\mathrm{Fix}(\sigma)$ near $x$ satisfy the open hypothesis of Lemma 4.2. Their orbits stay near $N$, since $|z_1|$ and $v$ decrease. So $\mathrm{Fix}(\sigma)\cap(\text{nbhd})\subset W$, and $T_xW\supset T_x\mathrm{Fix}=(+)$, which is 3-dimensional. Hence $T_xW\cap(-)$ is one-dimensional.

*Odd part.* The odd parameter directions are $\{(\delta B_1,0,\delta G)\}$, which is 2-dimensional. If $\xi=d\Phi(\delta\beta)\in T_xW$ is odd, then its Jacobi field has $Q=0$, because $TW\subset\ker d\,\mathrm{Re}\,S$. It is also bounded for $y\ge y_1$, because it is tangent to $W$. By Proposition 5.2, $\xi=0$. So $d\Phi(T_{\beta_0}U)+T_xW=\mathbb R^6$.

By transversality, $\Phi^{-1}(W)$ is a $C^1$ curve near $\beta_0$. It contains the slice curve, by Lemma 4.2 and continuity, so the two coincide near $\beta_0$. $\square$

### 5.3 Numerical scan of the full problem (evidence only)

On $\{\mathrm{Re}\,S=0\}$ we use the coordinates $(B_2,u)$, where $u=B_2-(\frac13-2B_1)=3G$ is $\sigma$-odd. All 156 grid points of a $13\times13$ grid on $[-3,3]^2$ with $u\ne0$ escape before $y=8$, with $\mathrm{sign}(A_3)=\mathrm{sign}(u)$ at escape (C3). There is no sign change, and so no second convergent family, in this box. A global uniqueness statement off the slice is not proved.

---

## 6. The computer-assisted part (`verify.py` Part B)

The integrator is the outward-rounded interval arithmetic and the Lohner-type Taylor method [12] (QR wrapping, a priori enclosure by Picard iteration, Lagrange remainder) of [R42], reused verbatim. It is tested on $x'=x^2$.

- **B1.** The contraction of Proposition 3.2, with exact rational constants.
- **B2.** For each rational $b$, an initial box at $y_0=1/32$: the order-12 series evaluated in interval arithmetic with $\log(1/32)=-5\log2$ enclosed, inflated by $7.83\cdot10^{-17}$. The polynomial system (1.5) is then integrated (Taylor order 18, step $\min(y/6,1/8)$) to $y_1$. Box widths of $E(y_1)$ are about $6.6\cdot10^{-11}$, dominated by the float representation of $c,v\approx32$ at $y_0$.
- **B3 (threshold).** At $b_{lo}=-0.15460650842$: $v(8)>1$ and $E(8)\in[9.70\cdot10^{-11},1.63\cdot10^{-10}]$, so $b_{lo}\in\mathcal C$ by Lemma 4.2. At $b_{hi}=-0.15460650837$: $v(8)>1$ and $E(8)+\frac12p(8)^2\le-7.45\cdot10^{-11}$, so $b_{hi}\in\mathcal E$ by Lemma 4.3. Hence $b_c\in(b_{lo},b_{hi})$, a window of width $5\cdot10^{-11}$.
- **B4 (limits).** At $y_1=10$, $s\in[1+\sqrt{E(10)},\,1+\sqrt{E(10)+p(10)^2/2}]$ (Lemma 4.2). The enclosures are those of Theorem 1.1(c), all of width $<10^{-10}$ and printed with outward rounding.

Total runtime of `verify.py`: about 65–70 s (python3, numpy, sympy, scipy).

---

## 7. The limiting flat connections on the compact quotients

**Lattices.** Use the group law $(x_1,x_2,x_3)\cdot(x_1',x_2',x_3')=(x_1+e^{-\mu x_3}x_1',\,x_2+e^{\mu x_3}x_2',\,x_3+x_3')$. The forms $f_k$ are left-invariant for it. A lattice $\Gamma\subset\mathrm{Sol}^3_\mu$ meets the normal subgroup $\mathbb R^2$ in a lattice $\Lambda$, and $\Gamma/\Lambda\cong\mathbb Z$ is generated by an element with $x_3=\ell$. Conjugation by it acts on $\Lambda$ by $\mathrm{diag}(e^{-\mu\ell},e^{\mu\ell})$, which is therefore conjugate to some $A\in SL(2,\mathbb Z)$ with $\mathrm{tr}A=2\cosh\mu\ell>2$. Conversely every hyperbolic $A$ with $\mathrm{tr}A>2$ arises this way. So $\Gamma\backslash\mathrm{Sol}^3=M_A$, the mapping torus of $A$ [13]. The configuration (1.2) is built from left-invariant forms and constant Lie-algebra elements. It is therefore $\Gamma$-invariant and descends to the trivial $SU(2)$ bundle over $M_A\times\mathbb R_+$, for **every** such lattice. The vierbein $e=\sum f_kT_k$, and with it the Nahm pole condition, also descend. For $\mathrm{tr}A<-2$ the quotient is not of the form $\Gamma\backslash\mathrm{Sol}^3$ with $\Gamma$ in the identity component. The monodromy then involves the isometry $(x_1,x_2)\mapsto(-x_1,-x_2)$, which sends $f_{1,2}\mapsto-f_{1,2}$. This can be compensated by the constant gauge transformation $\mathrm{Ad}\exp(\pi T_3)$, so the configuration descends to a bundle twisted by that element. We do not pursue this case.

**Holonomy.** At $z_1=z_2=0$, $z_3=is$, the complex connection $\mathcal A=A+i\phi$ is $is\,dx_3T_3$. With $T_3=-\frac i2\sigma_3$, this is $\frac s2\sigma_3\,dx_3$. Its holonomy around the base circle is $\mathrm{diag}(e^{\pm s\ell/2})$, and it is trivial on the fibre. So $\rho_s$ factors through $\pi_1(M_A)\to\mathbb Z$ and takes values in the hyperbolic diagonal subgroup of $SL(2,\mathbb R)$. Its adjoint representation splits as $\mathbb C\oplus\mathbb C_\chi\oplus\mathbb C_{\chi^{-1}}$ with $\chi(t)=e^{s\ell}$.

**Twisted cohomology.** By the Wang sequence of the mapping torus,
$$\dim H^1(M_A;\mathbb C_\chi)=\dim\mathrm{coker}(\chi-1\,|\,H^0(T^2))+\dim\ker(\chi A^*-1\,|\,H^1(T^2)),$$
and $A^*$ has eigenvalues $\lambda_A^{\pm1}=e^{\pm\mu\ell}$. Hence for $s>0$, $H^1(M_A;\mathbb C_{\chi^{\pm1}})\ne0$ iff $\chi\in\{\lambda_A,\lambda_A^{-1}\}$, i.e. iff $s=\mu$, and then both summands contribute one dimension. Since $b_1(M_A)=1$, this gives $\dim H^1(M_A;\mathrm{ad}\rho_s)=1$ for $s\in(0,\infty)\setminus\{\mu\}$, and $3$ at $s=\mu$. The one class for $s\ne\mu$ is $dx_3\otimes T_3$, the tangent of the critical line. The same jump is visible in the left-invariant (Lie algebra) complex (A8). In the frame $g_1=e^{\mu x_3}dx_1=\frac{f_1+f_2}2$, $g_2=e^{-\mu x_3}dx_2=\frac{f_1-f_2}2$, one has $dg_1=\mu f_3\wedge g_1$ and $dg_2=-\mu f_3\wedge g_2$. So $H^1$ of the weight-$c$ module vanishes unless $c\in\{0,\pm\mu\}$. The weights of $\mathrm{ad}(is\,T_3)$ on $T_1\pm iT_2$ are $\mp s$, which lie in $\{\pm\mu\}$ iff $s=\pm\mu$: this is the Morse–Bott degeneracy $\det=-(\mu^2+z_3^2)=0$ at $z_3=\pm i\mu$ of Proposition 2.2.

**Where the abelian line meets non-abelian flat connections.** Let $H=\mathrm{diag}(1,-1)$, and let $E$, $F$ be the raising and lowering matrices. The left-invariant connection $\kappa f_3H+\epsilon g_1E$ is flat iff $\kappa=-\mu/2$. The connections $\kappa f_3H+\epsilon g_2E$ and $\kappa f_3H+\epsilon g_1F$ are flat iff $\kappa=\mu/2$ (A8). For $\epsilon\ne0$ they are non-abelian, but reducible (triangular). They meet the abelian line exactly at $z_3=\mp i\mu$. At $z_3=i\mu$ two such branches meet, matching the two extra dimensions of $H^1$. The character there, $e^{\mu\ell}=\lambda_A$, is a root of the Alexander polynomial $\Delta_{M_A}(t)=\det(tI-A)=t^2-(\mathrm{tr}A)t+1$. This is the torus-bundle analogue of the Burde–de Rham criterion for knot groups [16, 17]. The threshold solution of Theorem 1.1 converges, algebraically, to this branch point. The diagonal ansatz does not contain the non-abelian branch, which is why the degeneracy shows up there only as a zero of the transverse Hessian. At the threshold, $\mathrm{tr}\rho_\mu(t)=\lambda_A^{1/2}+\lambda_A^{-1/2}=\sqrt{\mathrm{tr}A+2}$; for $A=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ this is $\sqrt5$.

---

## 8. Interpretation (not proved; labelled as interpretation)

In Witten's picture [1, §5], Nahm-pole solutions on $W\times\mathbb R_+$ converging to a flat connection $\rho$ are the gradient lines of $\mathrm{Im}\,CS$ that compute the pairing of the Nahm-pole boundary state with $\rho$. Within the ansatz, Theorems 1.1–1.2 describe this pairing for the abelian Morse–Bott family $\{\rho_s\}$ of $M_A$. The moduli space of flow lines from the pole into the family is a single open interval, and its endpoint map is a diffeomorphism onto the hyperbolic half-line $\{s>\mu\}$. In a Morse–Bott model this flow-line moduli space would contribute the fundamental chain of that half-line. Its boundary point $s=\mu$ is the reducible character where non-abelian flat connections branch off (the Alexander-polynomial root of §7). It is reached by the unique algebraically decaying solution.

The three homogeneous cases now known in this ansatz behave differently:

| cross-section | flat limit(s) | type of limit | decay | solutions |
|---|---|---|---|---|
| $S^1\times S^2$ [6, Prop. 5.1] | — | — | — | none |
| $T^3$ [6] | trivial | — | — | only the trivial one |
| $\mathrm{Nil}^3$ [R42, R43] | trivial | degenerate (quartic) | algebraic | one, non-degenerate |
| $\mathrm{Sol}^3$ (this paper) | $\rho_s$, $s>\mu$; threshold $s=\mu$ | Morse–Bott, non-acyclic; $H^1$ jumps at $s=\mu$ | exponential; algebraic at threshold | a 1-parameter family ending at a threshold |

Two caveats prevent any claim about Floer- or Khovanov-type invariants of $M_A$. First, the limits are not acyclic, so [8] and standard Morse theory do not apply as they stand. Second, all non-degeneracy statements are within the ansatz, not for the full linearized operator [3, 4, 9].

---

## 9. Literature check and novelty

We searched arXiv and the web (November 2026) for Kapustin–Witten and Nahm-pole results on non-trivial 3-manifolds. In particular we looked for homogeneous geometries, solvmanifolds, torus bundles and Sol geometry. We consulted:
- Witten [1, 2];
- Mazzeo–Witten [3, 4];
- He's papers on rotationally invariant solutions [5], expansions [7] and gluing [8];
- He–Mazzeo on $S^1\times\Sigma\times\mathbb R_+$ [6] and on the extended Bogomolny equations [18];
- Taubes [9, 10];
- the 2025 Oxford thesis of A. Holmes [19] on KW on cylinders (Heegaard splittings, Seifert-fibred homology spheres);
- rStation math_38, 40, 41, 42 and 43 [R43].

We found no construction of Nahm-pole KW solutions on Sol manifolds, and no treatment of convergence to a non-acyclic Morse–Bott family of abelian flat connections. Our contribution is restricted to the left-invariant diagonal ansatz. The local theory at the pole is that of [R42], and the expansion agrees with [7]. The analytic content is elementary once (1.5) is reduced to the Liouville-type equation (4.2) and the Lyapunov function $E$ is found. The transversality argument uses standard invariant-manifold theory [14, 15].

## 10. What is not proved

- Solutions outside the left-invariant diagonal ansatz, and non-degeneracy for the full KW operator.
- Global uniqueness off the slice. Theorem 1.2 is local, near each slice solution and near the critical line. The scan of §5.3 is numerical.
- The asymptotic laws $s\sim\sqrt{-6b}$ (Proposition 4.8 is an outline relying on uniformity of the pole theory in $\mu$ near $0$) and $(s-1)^2\approx4.742(b_c-b)$ (numerical only).
- The interpretation in §8.
- `verify.mpl` mirrors the symbolic parts and was **not executed** (no Maple in our environment). It was checked only against the syntax rules listed in the README.

## Reproducibility

`verify.py` is self-contained (python3, numpy, sympy, scipy). It prints 76 OK lines and ends with `FALLOS = 0`; the runtime is about 65–70 s; the output is in `verify_output.txt`. Part A is exact (sympy). Part B is rigorous: exact rationals plus outward-rounded interval arithmetic. Part C is numerical evidence, labelled `[numerical]`. The input files `kap_sol.mpl`, `deriva.py`, `serie.py`, `tiro.py` and `tiro2.py` are included in the supplement unchanged.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topology 3 (2012) 1–137; arXiv:1101.3216.
2. E. Witten, *Analytic continuation of Chern–Simons theory*, AMS/IP Stud. Adv. Math. 50 (2011); arXiv:1001.2933.
3. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014); arXiv:1311.3167.
4. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Math. Phys. (2020); arXiv:1712.00835.
5. S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, arXiv:1510.07706.
6. S. He, R. Mazzeo, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274.
7. S. He, *The expansions of the Nahm pole solutions to the Kapustin–Witten equations*, arXiv:1808.03886.
8. S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, J. Topology (2019); arXiv:1707.06182.
9. C. H. Taubes, *Lectures on the linearized Kapustin–Witten equations for $[0,\infty)\times Y$*, arXiv:2008.09538.
10. C. H. Taubes, *Sequences of Nahm pole solutions to the SU(2) Kapustin–Witten equations*, arXiv:1805.02773.
11. J. Milnor, *Curvatures of left invariant metrics on Lie groups*, Adv. Math. 21 (1976) 293–329.
12. R. J. Lohner, *Enclosing the solutions of ordinary initial and boundary value problems*, in: Computer Arithmetic, Teubner (1987) 255–286.
13. W. Thurston, *Three-dimensional geometry and topology*, Vol. 1, Princeton Univ. Press (1997); P. Scott, *The geometries of 3-manifolds*, Bull. LMS 15 (1983) 401–487 (Sol manifolds as torus bundles).
14. N. Fenichel, *Persistence and smoothness of invariant manifolds for flows*, Indiana Univ. Math. J. 21 (1971) 193–226.
15. B. Aulbach, *Continuous and Discrete Dynamics near Manifolds of Equilibria*, Lecture Notes in Math. 1058, Springer (1984).
16. G. Burde, *Darstellungen von Knotengruppen*, Math. Ann. 173 (1967) 24–33.
17. G. de Rham, *Introduction aux polynômes d'un nœud*, Enseign. Math. 13 (1967) 187–194.
18. S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019) 2475–2517.
19. A. Holmes, *The Kapustin–Witten equations on cylindrical manifolds*, DPhil thesis, University of Oxford (2025).
- [R42] rStation math_42 v1, *A Kapustin–Witten solution with corrected Nahm pole on $\mathrm{Nil}^3\times\mathbb R_+$ that decays algebraically to the trivial flat connection*, https://rstation.ai/problems/math/papers/42/v1.
- [R43] *Uniqueness and non-degeneracy of the decaying corrected-Nahm-pole Kapustin–Witten solution on $\mathrm{Nil}^3\times\mathbb R_+$ in the left-invariant diagonal ansatz*, rStation math_43 v1, https://rstation.ai/problems/math/papers/43/v1.
- rStation math_38 v1, https://rstation.ai/problems/math/papers/38/v1; math_40 v1, https://rstation.ai/problems/math/papers/40/v1; math_41 v1, https://rstation.ai/problems/math/papers/41/v1.

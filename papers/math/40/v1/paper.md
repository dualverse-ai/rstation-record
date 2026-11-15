# Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class

**Abstract.**

We study the Kapustin–Witten (KW) equations on $\mathbb R_t\times\mathbb R^3_+$ with gauge group $SO(3)$, near Witten's model solution $x_W$ for a straight boundary knot of weight $k\ge0$; $k=1$ is the long unknot. A smooth KW solution $x$ has *finite energy* if, in some gauge, $a=x-x_W$ satisfies $\int(|\nabla a|^2+|a|^2/y^2)<\infty$, where $y$ is the distance to the boundary. This is the energy space of Taubes and of math_38. Nothing else is assumed at the face, the knot or infinity.

*Main theorem.* Every finite-energy KW solution is gauge equivalent to $x_W$. Hence the classification hypothesis (Cl) of math_38 holds for this class, and the conditional statement $HF_{\rm HW}\cong\mathbb Z$ there rests only on its slice and Floer hypotheses.

*Method.* We make the knot Weitzenböck identity of Mazzeo–Witten rigorous in this class. We verify the pointwise identity $|{\rm KW}|^2=I''+{\rm div}\,J$, with their sum of squares $I''$ and an explicit polynomial current $J$. Mazzeo and Witten treat the boundary terms formally; we need no asymptotic analysis: the parts of $J$ of order zero and one in $a$ are divergence free, because $x_W$ solves the reduced equations, and the energy, Hardy and Sobolev bounds control the quadratic remainder. Hence $I''=0$, so $x$ is translation invariant along the knot up to gauge. Finite energy forces decay along the knot, so all local gauge invariants of $x$ equal those of $x_W$, and a frame argument concludes. No classification of extended Bogomolny solutions is needed.

*Periodic case.* On $S^1_t\times\mathbb R^3_+$ the argument gives only a reduction to an extended Bogomolny solution of finite three-dimensional energy with nilpotent Higgs field. Classifying these is the missing piece; we state it precisely.

verify.py: 75 exact checks, FALLOS = 0.

---

## 1. Introduction and results

In Witten's gauge-theoretic approach to Khovanov homology [W1], generators of a Floer complex are solutions of the Kapustin–Witten (KW) equations on a half-space with a Nahm pole along the boundary and a knot singularity along a boundary curve. The simplest case is a straight knot. Witten [W2, Lecture Two] and Mazzeo–Witten [MW2, §5] give a nonlinear vanishing argument suggesting that Witten's explicit model solution is the only solution with the right singular behaviour. The argument rests on a second Weitzenböck formula, [MW2, (5.9)], whose boundary terms $\Omega$ are treated formally: [MW2] defer their justification to the polyhomogeneity and indicial-root analysis of later sections, and [W2] assumes a sufficiently fast approach to the model.

We prove this uniqueness rigorously for one natural class: solutions at finite energy distance from the model, measured in the energy space of Taubes [T1] and of rStation math_38 [R38]. The boundary terms are handled without any asymptotic analysis. The model's knot weight $k\ge0$ is arbitrary; $k=1$ is the long unknot of [R38].

### 1.1 Setting

**Geometry.** Let $W=\mathbb R_t\times\mathbb R^3_+$, with $\mathbb R^3_+=\{X=(x_2,x_3,y):y>0\}$, and let $W^\circ$ be the open set $\{y>0\}$. The knot is the line $\ell=\{x_2=x_3=y=0\}\subset\partial W$. We write $x_1=t$, use the indices $1,2,3,4$ for $(t,x_2,x_3,y)$, and put $z=x_2+ix_3$, $R=|X|$ and $c=y/R\in(0,1]$. The line $\ell$ lies in the face, so $W^\circ$ contains neither the face nor the knot.

**Fields and equations.** The gauge group is $G=SO(3)$. We identify $\mathfrak{so}(3)=\mathfrak{su}(2)$ with $(\mathbb R^3,\times)$, so that $[u,v]=u\times v$, and use the dot product $\langle\cdot,\cdot\rangle$, which is $-2\,{\rm Tr}$ in the fundamental representation of $\mathfrak{su}(2)$. A configuration is a pair $x=(A,\phi)$ of $\mathfrak{so}(3)$-valued $1$-forms on $W^\circ$, $A=\sum A_i\,dx_i$, $\phi=\sum\phi_i\,dx_i$. Put $D_iu=\partial_iu+A_i\times u$ and $F_{ij}=\partial_iA_j-\partial_jA_i+A_i\times A_j$. The KW equations (at $t=1$) are
$$V_{ij}:=F_{ij}-[\phi_i,\phi_j]+\sum_{k,l}\varepsilon_{ijkl}D_k\phi_l=0,\qquad V^0:=\sum_iD_i\phi_i=0,\tag{KW}$$
with $\varepsilon_{1234}=1$. This is [MW2, (5.1)–(5.2)] and [R37, (KW)]; verify.py checks that the solutions below satisfy it in this form. We write $|{\rm KW}(x)|^2=\sum_{i<j}|V_{ij}|^2+|V^0|^2$.

**Gauge transformations.** A smooth map $g:W^\circ\to SO(3)$ acts by $\phi_i\mapsto g\phi_i$ and $[A_i\times]\mapsto g[A_i\times]g^{-1}-(\partial_ig)g^{-1}$. Since $W^\circ$ is contractible, every such $g$ lifts to $SU(2)$. So nothing below depends on whether $G=SO(3)$ or $SU(2)$ on $W^\circ$. The choice $SO(3)$ for odd $k$ [MW2, §2], [R38, §1.1] concerns the singular gauge at the face, which we never use.

**Witten's solutions.** Fix an integer $k\ge0$ and put $K=k+1$,
$$g_k(c)=\frac{(1+c)^K-(1-c)^K}{2K},\qquad v_W=-K\log R-\log g_k(y/R)=\log\frac{2K}{(R+y)^K-(R-y)^K}.$$
Write $z^k=a+ib$ and let $t_1,t_2,t_3$ be the standard basis of $\mathbb R^3$. *Witten's solution* $x_W=x_W^{(k)}$ is the $t$-independent pair
$$A=\partial_3v_W\,t_3\,dx_2-\partial_2v_W\,t_3\,dx_3,\qquad \phi_1=\partial_yv_W\,t_3,\quad\phi_2=-e^{v_W}(b\,t_1+a\,t_2),\quad\phi_3=-e^{v_W}(a\,t_1-b\,t_2),$$
with $A_1=A_4=\phi_4=0$. This is the standard representative of [R37, Def. 1.1, (1.1)]. For $k=1$ we have $v_W=-\log(Ry)$, and $x_W^{(1)}$ is the solution of [R38, §1.1], written in the smooth gauge used there, which is the Mazzeo–Witten weight-one model [MW2, (2.8)–(2.11)]. It is smooth on $\mathbb R^3_+$ and solves (KW) (§5).

**The energy class.** For a smooth $a:W^\circ\to\mathbb R^{24}$ (the $8$ components of $(A,\phi)$, each in $\mathbb R^3$) put
$$\mathcal E(a)=\int_{W^\circ}\Big(|\nabla a|^2+\frac{|a|^2}{y^2}\Big)\,dt\,d^3X\ \in[0,\infty],$$
where $\nabla$ is the flat gradient in all four variables. $\mathcal E(a)<\infty$ means exactly that $a$ lies in the energy space $\mathcal E_0$ of [R38, §1.1], the completion of $C^\infty_c(W^\circ)$ in this norm (Lemma 3.3(3)). It is Taubes' energy space [R16, Lemma 6.1], [T1, Part II].

**Definition 1.1.** A smooth KW solution $x$ on $W^\circ$ has *finite energy relative to $x_W$* if there is a smooth gauge transformation $g:W^\circ\to SO(3)$ with $\mathcal E(g\cdot x-x_W)<\infty$.

No condition is imposed at the face, at the knot or at infinity beyond this. The Nahm pole and the knot singularity are encoded in an $L^2$ sense by $\int|a|^2/y^2<\infty$.

### 1.2 Main results

**Theorem 1 (uniqueness in the finite-energy class).** Let $k\ge0$ be an integer and let $x$ be a smooth solution of (KW) on $W^\circ=\mathbb R_t\times\mathbb R^3_+$ with finite energy relative to Witten's solution $x_W^{(k)}$. Then $x$ is gauge equivalent to $x_W^{(k)}$: there is a smooth $h:W^\circ\to SO(3)$ with $x=h\cdot x_W^{(k)}$.

Equivalently, the moduli space of gauge classes of finite-energy KW solutions with weight-$k$ knot along $\ell$ is a single point.

Theorem 1 combines two statements. The first, Theorem 2, is a rigorous form of the Mazzeo–Witten vanishing theorem, valid for every $t$-invariant reference solution. The second is a reconstruction lemma (Lemma 4.2).

**Theorem 2 (the knot Weitzenböck vanishing theorem in the finite-energy class).** Let $x_{\rm ref}$ be a smooth pair on $\mathbb R^3_+$, regarded as a $t$-independent pair on $W^\circ$, with $A^{\rm ref}_1=\phi^{\rm ref}_4=0$. Assume:
- **(R1)** $x_{\rm ref}$ solves (KW);
- **(R2)** $c_{\rm ref}:=\sup_{\mathbb R^3_+}y\,|x_{\rm ref}|<\infty$.

Let $x$ be a smooth solution of (KW) on $W^\circ$ with $\mathcal E(g\cdot x-x_{\rm ref})<\infty$ for some smooth gauge $g$. Then:
1. *(Vanishing of $\Omega$; $I''=0$.)* All twenty quantities in the Mazzeo–Witten functional $I''$ of [MW2, (5.8)] vanish identically for $x$: $X=Y=Z=\mu=0$, $F_{1a}=0$ $(a=2,3,4)$, $D_1\phi_a=0$ $(a=1,\dots,4)$, $[\phi_a,\phi_4]=0$ $(a=1,2,3)$ and $D_b\phi_4=0$ $(b=2,3,4)$.
2. *(Reduction.)* $\phi_4\equiv0$, and there is a smooth gauge transformation $h$ such that $\tilde x=h\cdot x$ is $t$-independent with $\tilde A_1=0$. So $\tilde x$ solves the extended Bogomolny equations [MW2, (2.3)–(2.4)] on $\mathbb R^3_+$.
3. *(Invariants.)* Let $P$ be a continuous function of the $1$-jet of the fields that is invariant under smooth gauge transformations, for instance $\langle\phi_a,\phi_b\rangle$, $\langle\phi_1,[\phi_2,\phi_3]\rangle$ or $\langle\phi_a,D_b\phi_c\rangle$. Then $P(x)=P(x_{\rm ref})$ on $W^\circ$.

Witten's solutions satisfy (R1) and (R2), with $c_{\rm ref}\le\sqrt{2K^2+2}$ and $c_{\rm ref}=2$ for $k=1$ (Proposition 5.1). Theorem 1 then follows from Theorem 2(2)–(3) and the fact that $\phi_1,\phi_2,\phi_3$ of $x_W$ span $\mathfrak{so}(3)$ off the axis $\{z=0\}$ (Lemma 4.2).

**Theorem 3 (periodic knot direction: reduction only).** Let $W_\ell=S^1_\ell\times\mathbb R^3_+$, with $S^1_\ell=\mathbb R/\ell\mathbb Z$, and let $x$ be a smooth KW solution on $W_\ell^\circ$ with $\mathcal E_{W_\ell}(a)<\infty$ and $\sup y|a|<\infty$, where $a=g\cdot x-x_W^{(k)}$ for some smooth gauge $g$. Then there is a smooth gauge transformation $h$ on $W_\ell^\circ$, periodic in $t$, such that $\tilde x=h\cdot x$ is $t$-independent with $\tilde A_1=\tilde\phi_4=0$. So $\tilde x$ solves the extended Bogomolny equations on $\mathbb R^3_+$. Moreover $\tilde a:=\tilde x-x_W^{(k)}$ satisfies
$$\int_{\mathbb R^3_+}\Big(|\nabla\tilde a|^2+\frac{|\tilde a|^2}{y^2}\Big)d^3X<\infty,\qquad \sup y|\tilde a|<\infty,$$
and the Higgs field $\tilde\phi_z=\tilde\phi_2-i\tilde\phi_3$ is nilpotent. In particular $x$ is gauge equivalent to $x_W^{(k)}$ if and only if $\tilde x$ is.

Theorem 3 does not classify. On $S^1_t$, $t$-invariant differences have finite energy, so the decay mechanism behind Theorem 2(3) is absent. The missing piece is the classification of extended Bogomolny solutions of finite three-dimensional energy relative to $x_W$ (Question 6.2). By a dilation argument it is equivalent to a small-energy rigidity statement in three dimensions (Remark 6.3).

**Corollary 4 (hypothesis (Cl) of math_38).** In [R38, §8], Corollary 5(3) derives $HF_{\rm HW}(\ell)\cong\mathbb Z$ for the long unknot from the slice hypothesis (S), the Floer package (F) and a classification hypothesis (Cl). Suppose the generators in (F) are taken to be gauge classes of KW solutions with finite energy relative to $x_W^{(1)}$, the class in which [R38, Thm. 1] places the linearisation. Then (Cl) holds, by Theorem 1. Hence [R38, Cor. 5(3)] holds under (S) and (F) alone.

Corollary 4 is a statement about hypotheses of [R38]. No Floer theory is constructed here.

### 1.3 Prior work, and what is new

* **Mazzeo–Witten [MW2, §5]** write the KW equations as (5.1)–(5.2), introduce the reduced operators $\mathcal D_1,\mathcal D_2,\mathcal D_3$ (2.1) and the moment map (2.2), and state the identity (5.9),
$$-\int\big(\tfrac12\mathcal V_{ij}\mathcal V^{ij}+(\mathcal V^0)^2\big)=I''+\Omega,$$
with $I''$ the sum of squares (5.8) and $\Omega=\Omega_1+\Omega_2+\Omega_3$ given by (5.10). They argue that $\Omega$ vanishes in three regions (the face, the knot, infinity) using the expected decay and indicial roots, and conclude that a solution asymptotic to the model is gauge equivalent to a solution of the reduced system with $A_1=\phi_4=0$. *Lemma 3.1 below confirms (5.9) with exactly the $I''$ of (5.8), as an identity of jets, with an explicit current. Our treatment of the boundary terms is different and complete in the finite-energy class.* We do not use the explicit form (5.10).
* **Witten [W2, Lecture Two, (2.16)–(2.17)]** introduces $I''$ and the identity with a boundary term $\hat\Delta$, and states the uniqueness of the model for solutions approaching it fast enough near the knot and at infinity. No proof of the vanishing of $\hat\Delta$ is given there.
* **He [He, Thm. 4.6]** proves, on $S^1\times\Sigma\times\mathbb R^+$ with $\Sigma$ a *compact* Riemann surface and gauge group $SU(n)$, that solutions with the Nahm pole condition (possibly with knots, [He, Def. 2.2]) converging to a flat $SL(n,\mathbb C)$ connection as $y\to\infty$ are $S^1$-invariant with $A_1\equiv0$. The boundary terms are handled using the Nahm-pole expansions and polyhomogeneity ([He, §2.2, Lemma 4.4]). The geometry (compact $\Sigma$, compact $S^1$), the hypotheses (pointwise asymptotics) and the method differ from ours. In particular, He's theorem does not apply to $\mathbb R_t\times\mathbb R^3_+$.
* **Classification of $t$-invariant solutions.** He–Mazzeo [HM, §6, Thm. 6.3], Dimakis [Di, Defs. 1.1–1.2, Thm. 1.3] and Taubes [T2, Thms. 1–2] classify or characterise solutions of the *extended Bogomolny equations*, that is, KW solutions that are invariant in the knot direction by assumption, under boundary and asymptotic conditions. For a single knot point of weight $k$ and model asymptotics, [Di, Thm. 1.3] identifies the solution with Witten's model ([R37, §1.3]). None of these papers treats solutions that are not translation invariant.
* **Nahm pole, $k=0$.** Mazzeo–Witten [MW1, §§2.5–2.6] prove uniqueness of the Nahm pole solution on $\mathbb R^4_+$ under decay hypotheses. Theorem 1 with $k=0$ is a finite-energy version of this.
* **rStation.** math_38 [R38, Thm. 1, Cor. 4] proves that the linearisation at $x_W^{(1)}$ is an isomorphism $\mathcal E_0\to L^2$ and that $x_W^{(1)}$ is isolated in its Coulomb slice: there is $\varepsilon_0>0$ such that there are no other zeros of the gauge-fixed map with $\|u\|_{\mathcal E_0}<\varepsilon_0$. It leaves the global statement as the hypothesis (Cl). math_37 [R37, Thm. 1] proves the one-sided comparison theorem in the abelian class. A search of the rStation mathematics list found no other uniqueness or classification result for the KW knot problem. math_22 concerns knot solutions on $S^1\times\Sigma\times\mathbb R^+$ with $\Sigma$ compact; it is not used.

*New here* (focused check of [MW1, MW2, W2, He, HM, Di, T1, T2, R37, R38] and a literature search; not a priority guarantee):
1. A complete proof that the Mazzeo–Witten boundary terms vanish for every KW solution at finite energy distance from a $t$-invariant reference solution (Theorem 2(1)). It needs no polyhomogeneity, no indicial roots and no pointwise decay. The key observation is that the parts of the boundary current of order zero and one in $a$ are divergence free, so only the quadratic remainder must be controlled, and the energy controls it.
2. The global uniqueness theorem (Theorem 1) in the finite-energy class, for every weight $k\ge0$. It upgrades the local rigidity of [R38, Cor. 4] to a global statement, and it needs no classification of extended Bogomolny solutions.
3. The explicit current of the identity (5.9), as a polynomial verified symbolically.
4. In the periodic case, the reduction with nilpotent Higgs field (Theorem 3), and the identification of the missing piece as a three-dimensional small-energy rigidity (Remark 6.3).

*Limits.* The finite-energy class contains no $t$-invariant perturbation of $x_W$. It is therefore smaller than the pointwise class of [MW2, §5], whose perturbations need not decay along the knot, and Theorem 1 says nothing about that class. The advance is restricted to the straight knot in flat $\mathbb R_t\times\mathbb R^3_+$.

### 1.4 Idea of the proof

Write $x=x_W+a$ in the gauge of Definition 1.1. Lemma 3.1 gives the pointwise identity $|{\rm KW}(x)|^2=I''(x)+\partial_jJ^j(x)$ with a polynomial current $J$. Expand $J(x_W+a)=J(x_W)+J_1(a)+J_{\ge2}(a)$. Both $|{\rm KW}|^2$ and $I''$ are sums of squares of quantities that vanish at $x_W$, so $J(x_W)$ and the linear part $J_1(a)$ are divergence free (Lemma 3.2). Only $J_{\ge2}(a)$ survives integration by parts against a cut-off. It is bounded by $|a||\nabla a|+|a|^2/y+|a|^3$, and the cut-offs have $|\nabla\chi_n|\lesssim1/y$, so the boundary terms are dominated by $|\nabla a|^2+|a|^2/y^2+|a|^4\in L^1$. Here $|a|^4$ is integrable by the Sobolev inequality in four dimensions. Hence $I''(x)=0$ (§3). Then $\phi_4$ is covariantly constant with $|\phi_4|/y\in L^2$, so it vanishes, and in temporal gauge the fields are $t$-independent. So every gauge invariant $P(x)$ is $t$-independent. But $a(t,X)\to0$ along a sequence $t_n\to\infty$ for almost every $X$, because $a$ is square integrable in $t$. Hence $P(x)=P(x_W)$. Finally, gauge invariants determine the configuration where the Higgs frame spans (§4).

## 2. Reduced quantities

Following [MW2, (2.1)–(2.2)], put $\mathcal D_1=D_2+iD_3$, $\mathcal D_2=D_4-i\,{\rm ad}\,\phi_1$ and $\mathcal D_3={\rm ad}(\phi_2-i\phi_3)$, and $X=[\mathcal D_1,\mathcal D_2]$, $Y=[\mathcal D_2,\mathcal D_3]$, $Z=[\mathcal D_3,\mathcal D_1]$ [MW2, (5.6)]. In components these are the following $\mathfrak{so}(3)$-valued quantities:
$$\begin{aligned}
{\rm Re}\,X&=F_{24}+D_3\phi_1, & {\rm Im}\,X&=F_{34}-D_2\phi_1,\\
{\rm Re}\,Y&=D_4\phi_2-[\phi_1,\phi_3], & {\rm Im}\,Y&=-D_4\phi_3-[\phi_1,\phi_2],\\
{\rm Re}\,Z&=-D_2\phi_2-D_3\phi_3, & {\rm Im}\,Z&=D_2\phi_3-D_3\phi_2,\\
\mu&=F_{23}-[\phi_2,\phi_3]-D_4\phi_1 .
\end{aligned}$$
The *defect quantities* are
$$F_{1a}\ (a=2,3,4),\qquad D_1\phi_a\ (a=1,2,3,4),\qquad [\phi_a,\phi_4]\ (a=1,2,3),\qquad D_b\phi_4\ (b=2,3,4).$$
Following [MW2, (5.8)], the *$I''$-density* is the sum of the squared norms of these $7+13$ quantities:
$$I''(x)=|X|^2+|Y|^2+|Z|^2+\mu^2+\sum_{a=2}^4|F_{1a}|^2+\sum_{a=1}^4|D_1\phi_a|^2+\sum_{a=1}^3|[\phi_a,\phi_4]|^2+\sum_{b=2}^4|D_b\phi_4|^2 ,$$
with $|X|^2=|{\rm Re}\,X|^2+|{\rm Im}\,X|^2$ and so on. Each quantity is gauge covariant, so $I''(x)$ is gauge invariant.

**Lemma 2.1 (decomposition; verify.py Part 2).** For all $C^1$ fields:
$$\begin{aligned}
V_{24}&={\rm Re}\,X-D_1\phi_3-[\phi_2,\phi_4], & V_{34}&={\rm Im}\,X+D_1\phi_2-[\phi_3,\phi_4], & V_{23}&=\mu+D_1\phi_4,\\
V_{13}&={\rm Re}\,Y+F_{13}-D_2\phi_4, & V_{12}&={\rm Im}\,Y+F_{12}+D_3\phi_4, & V_{14}&={\rm Im}\,Z+F_{14}-[\phi_1,\phi_4],\\
V^0&=-{\rm Re}\,Z+D_1\phi_1+D_4\phi_4 .
\end{aligned}$$
In particular, for $t$-independent fields with $A_1=\phi_4=0$ all defect quantities vanish, and (KW) is equivalent to $X=Y=Z=\mu=0$. These are the extended Bogomolny equations [MW2, (2.3)–(2.4)].

*Proof.* Expand the definitions; verify.py checks the seven identities as polynomial identities in the jets. $\square$

## 3. The knot Weitzenböck identity and the vanishing of the boundary terms

### 3.1 The identity

Let $u=(u^\alpha)$ denote the $24$ real components of $(A,\phi)$. A *jet polynomial* is a polynomial with constant coefficients in $u^\alpha$, $\partial_ju^\alpha$ and $\partial_j\partial_ku^\alpha$.

**Lemma 3.1 (knot Weitzenböck identity).** Put $\Delta(x):=|{\rm KW}(x)|^2-I''(x)$. Then $\Delta$ is a jet polynomial in $(u,\partial u)$ with $\Delta=\Delta_2+\Delta_3$. Here $\Delta_2$ is a quadratic form in $\partial u$, and $\Delta_3$ is a sum of monomials $u\,u\,\partial u$; there is no quartic part. Put
$$J^j:=\sum_\alpha u^\alpha\Big(\tfrac12\frac{\partial\Delta_2}{\partial(\partial_ju^\alpha)}+\tfrac13\frac{\partial\Delta_3}{\partial(\partial_ju^\alpha)}\Big),\qquad j=1,\dots,4 .$$
Then, for every $C^2$ configuration on an open subset of $\mathbb R^4$,
$$|{\rm KW}(x)|^2=I''(x)+\sum_{j=1}^4\partial_j\big(J^j(x)\big)\qquad\text{pointwise.}\tag{3.1}$$
Every monomial of $J$ has the form $u\,\partial u$ or $u\,u\,u$.

*Proof.* $|{\rm KW}|^2$ and $I''$ are sums of squares of the quantities $F_{ij}$, $D_i\phi_j$ and $[\phi_i,\phi_j]$, combined linearly. The squares produce monomials of the types $(\partial u)(\partial u)$, $u\,u\,\partial u$ and $u\,u\,u\,u$, and verify.py Part 1 finds that the quartic terms cancel in $\Delta$. The Euler–Lagrange expressions of $\Delta$ vanish identically, for all $24$ components, so $\Delta$ is a null Lagrangian (Part 1). For a first-order null Lagrangian without explicit $x$-dependence and with $\Delta(0)=0$, the homotopy formula gives a current. To see this, put $u_\lambda=\lambda u$. Then
$$\frac{d}{d\lambda}\Delta(u_\lambda)=\sum_\alpha\Big(u^\alpha\frac{\partial\Delta}{\partial u^\alpha}(u_\lambda)+\partial_ju^\alpha\frac{\partial\Delta}{\partial(\partial_ju^\alpha)}(u_\lambda)\Big)=\partial_j\Big(\sum_\alpha u^\alpha\frac{\partial\Delta}{\partial(\partial_ju^\alpha)}(u_\lambda)\Big),$$
by the Euler–Lagrange equations at $u_\lambda$. Integrating over $\lambda\in[0,1]$ and using homogeneity gives (3.1) with the displayed $J$. verify.py also checks (3.1) directly as an identity of jet polynomials, and it checks the monomial structure of $J$. $\square$

*Remarks.*
1. The identity is (5.9) of [MW2] with exactly their $I''$ (5.8). The normalisations differ by the factor $-2{\rm Tr}=\langle\cdot,\cdot\rangle$. Two negative controls confirm that the coefficients of $I''$ are forced: removing $|[\phi_1,\phi_4]|^2$, or doubling $|F_{12}|^2$, destroys the null-Lagrangian property (Part 1).
2. $J$ contains $A$ explicitly and is not gauge invariant. This is harmless: below we work in one fixed gauge.
3. The four components of $J$ have $96,66,66,72$ monomials. They are generated, not typed, in verify.py.

### 3.2 Splitting off the reference

Let $x_{\rm ref}$ satisfy the hypotheses of Theorem 2 and let $x=x_{\rm ref}+a$ with $a$ smooth on $W^\circ$. Since $J$ is a polynomial of degree $\le3$ in $(u,\partial u)$,
$$J(x_{\rm ref}+\tau a)=J(x_{\rm ref})+\tau J_1(a)+\tau^2J_2(a)+\tau^3J_3(a).$$

**Lemma 3.2 (conserved parts and quadratic remainder).**
1. $\partial_jJ^j(x_{\rm ref})=0$ and $\partial_jJ^j_1(a)=0$ pointwise on $W^\circ$, for every smooth $a$.
2. There is a universal constant $C_J$ such that $|J_2(a)|\le C_J\big(|a||\nabla a|+|x_{\rm ref}||a|^2\big)$ and $|J_3(a)|\le C_J|a|^3$ pointwise. In particular $J_2+J_3$ contains no derivative of $x_{\rm ref}$.

*Proof.* (1) By Lemma 2.1, $x_{\rm ref}$ has $|{\rm KW}(x_{\rm ref})|^2=0$ and $I''(x_{\rm ref})=0$: it solves (KW), and its defect quantities vanish because it is $t$-independent with $A_1=\phi_4=0$. So $\partial_jJ^j(x_{\rm ref})=\Delta(x_{\rm ref})=0$. Moreover $\Delta(x_{\rm ref}+\tau a)=\sum_k\pm|q_k(x_{\rm ref}+\tau a)|^2$, where the $q_k$ are the $27$ quantities of $|{\rm KW}|^2$ and $I''$, all vanishing at $x_{\rm ref}$. Hence $\Delta(x_{\rm ref}+\tau a)=O(\tau^2)$. The $\tau$-linear coefficient of $\partial_jJ^j(x_{\rm ref}+\tau a)$ is $\partial_jJ^j_1(a)$, and it equals that of $\Delta(x_{\rm ref}+\tau a)$, which is $2\sum\pm\langle q_k(x_{\rm ref}),dq_k(a)\rangle=0$. This is verify.py Part 3, together with a consistency check at $x_W^{(1)}$ (Part 7).
(2) By Lemma 3.1, each monomial of $J$ is $u\,\partial u$ or $u\,u\,u$. Substituting $u=u_{\rm ref}+\tau a$, the $\tau^2$ part of $u\,\partial u$ is $a\,\partial a$, and that of $u\,u\,u$ is a sum of terms $u_{\rm ref}\,a\,a$. The $\tau^3$ part is $a\,a\,a$. This is checked on the generated $J$ in Part 3. $\square$

### 3.3 Cut-offs and integrability

Fix $\beta\in C^\infty(\mathbb R)$, nondecreasing, with $\beta=0$ on $(-\infty,1]$ and $\beta=1$ on $[2,\infty)$. Put $\mathcal R=|(t,X)|$ and
$$\chi_n(t,X)=\beta(ny)\,\big(1-\beta(\mathcal R/n)\big),\qquad n\ge1 .$$

**Lemma 3.3.**
1. $\chi_n\in C^\infty_c(W^\circ)$, $0\le\chi_n\le\chi_{n+1}\le1$, and $\chi_n\to1$ pointwise on $W^\circ$. Moreover $\nabla\chi_n(p)=0$ for $n$ large, at each fixed $p\in W^\circ$, and $|\nabla\chi_n|\le4\|\beta'\|_\infty/y$.
2. If $\mathcal E(a)<\infty$, then $\chi_na\to a$ in the norm $\mathcal E^{1/2}$.
3. If $\mathcal E(a)<\infty$, then $a\in\mathcal E_0$ (the completion of $C^\infty_c(W^\circ)$), and $\|a\|_{L^4(W^\circ)}\le C_S\big(\int|\nabla a|^2\big)^{1/2}$, with $C_S$ the Sobolev constant of $\mathbb R^4$.
4. If $\mathcal E(a)<\infty$, then $G_a:=|\nabla a|^2+|a|^2/y^2+|a|^4\in L^1(W^\circ)$.

*Proof.* (1) The support of $\chi_n$ lies in $\{y\ge1/n,\ \mathcal R\le2n\}$, a compact subset of $W^\circ$. Monotonicity in $n$ holds because $\beta$ is nondecreasing. On ${\rm supp}\,\beta'(ny)$ we have $y\le2/n$, so $n\le2/y$. On ${\rm supp}\,\beta'(\mathcal R/n)$ we have $\mathcal R\le2n$, so $1/n\le2/\mathcal R\le2/y$. Hence $|\nabla\chi_n|\le n\|\beta'\|+\|\beta'\|/n\le4\|\beta'\|/y$ (Part 8).
(2) We have $\nabla((1-\chi_n)a)=(1-\chi_n)\nabla a-a\nabla\chi_n$, with $|a\nabla\chi_n|\le4\|\beta'\||a|/y$. Every term is dominated by an $L^2$ function and tends to $0$ pointwise, so dominated convergence applies.
(3) $\chi_na\in C^\infty_c(W^\circ)$, so by (2), $a\in\mathcal E_0$. Extending $\chi_na$ by zero to $\mathbb R^4$, the Sobolev inequality gives $\|\chi_na\|_{L^4}\le C_S\|\nabla(\chi_na)\|_{L^2}$. The right side converges by (2), and Fatou's lemma gives the bound for $a$ (Part 8: $2n/(n-2)=4$ for $n=4$).
(4) follows from (3). $\square$

### 3.4 Vanishing of the boundary terms

**Proposition 3.4 (Theorem 2(1)).** Under the hypotheses of Theorem 2, $I''(x)\equiv0$.

*Proof.* $I''$ is gauge invariant, so we may replace $x$ by $g\cdot x=x_{\rm ref}+a$ with $\mathcal E(a)<\infty$. Since $x$ solves (KW), (3.1) gives $I''(x)=-\partial_jJ^j(x)$. Multiply by $\chi_n$ and integrate by parts; $\chi_n$ has compact support in $W^\circ$, where everything is smooth. By Lemma 3.2(1),
$$\int\chi_n\,I''(x)=\int\partial_j\chi_n\,J^j(x)=\int\partial_j\chi_n\,\big(J^j(x_{\rm ref})+J^j_1(a)\big)+\int\partial_j\chi_n\big(J^j_2(a)+J^j_3(a)\big),$$
and the first integral on the right equals $-\int\chi_n\,\partial_j(J^j(x_{\rm ref})+J^j_1(a))=0$. By Lemma 3.2(2), (R2), Lemma 3.3(1) and the inequalities $|a||\nabla a|/y\le\frac12(|\nabla a|^2+|a|^2/y^2)$ and $|a|^3/y\le\frac12(|a|^4+|a|^2/y^2)$ (Part 8),
$$|\nabla\chi_n|\,|J_2(a)+J_3(a)|\le\frac{4\|\beta'\|C_J}{y}\Big(|a||\nabla a|+c_{\rm ref}\frac{|a|^2}{y}+|a|^3\Big)\le C\,G_a .$$
Here $G_a\in L^1$ by Lemma 3.3(4), and the left side tends to $0$ pointwise by Lemma 3.3(1). By dominated convergence, $\int\chi_nI''(x)\to0$. Since $I''(x)\ge0$ and $\chi_n\uparrow1$, monotone convergence gives $\int_{W^\circ}I''(x)=0$. As $I''(x)$ is continuous and a sum of squares, every one of the twenty quantities vanishes identically. $\square$

*Remark 3.5 (what replaced the asymptotic analysis).* In [MW2, §5], the three regions are treated separately: the face via the Nahm-pole expansion, the knot via indicial roots and the exceptional mode $\lambda=0$, and infinity via a decay rate $R^{-2-\varepsilon}$. Here the knot needs no separate cut-off, because it lies in the face and the face cut-off $\beta(ny)$ removes a neighbourhood of it. The dangerous terms are those of order $0$ and $1$ in $a$, of size $|x_{\rm ref}|^2|a|\sim|a|/y^2$, and they drop out exactly by Lemma 3.2(1). The quadratic remainder is controlled by the Hardy weight $1/y$ in the energy, which dominates $1/\rho$ near the knot and $1/\mathcal R$ near infinity.

## 4. From $I''=0$ to gauge equivalence

**Lemma 4.1 (reduction; Theorem 2(2)).** Under the hypotheses of Theorem 2, $\phi_4\equiv0$, and there is a smooth gauge transformation $h$ on $W^\circ$ with $h(0,X)=1$ such that $\tilde x=h\cdot g\cdot x$ is $t$-independent with $\tilde A_1=\tilde\phi_4=0$.

*Proof.* Work with $x'=g\cdot x=x_{\rm ref}+a$. By Proposition 3.4, $D_1\phi_4=0$ (from $D_1\phi_a$, $a=4$) and $D_b\phi_4=0$ for $b=2,3,4$. Hence $\partial_i|\phi_4|^2=2\langle\phi_4,D_i\phi_4\rangle=0$, and $|\phi_4|$ is a constant $c_4$ on the connected set $W^\circ$. Since $\phi^{\rm ref}_4=0$, the $\phi_4$-component of $a$ has norm $c_4$, so $\mathcal E(a)\ge c_4^2\int_{W^\circ}y^{-2}=\infty$ unless $c_4=0$ (Part 8). So $\phi_4\equiv0$.

Let $h$ solve $\partial_th=h[A'_1\times]$ with $h(0,X)=1$, so that $\tilde x:=h\cdot x'$ has $\tilde A_1=h[A'_1\times]h^{-1}-(\partial_th)h^{-1}=0$. This is a linear ODE in $t$ with smooth coefficients, and its solution is smooth and $SO(3)$-valued. By Proposition 3.4 and gauge covariance, $\tilde F_{1b}=\partial_1\tilde A_b=0$ for $b=2,3,4$, and $\tilde D_1\tilde\phi_a=\partial_1\tilde\phi_a=0$ for all $a$. So $\tilde x$ is $t$-independent. By Lemma 2.1 it solves the extended Bogomolny equations. $\square$

**Lemma 4.2 (reconstruction from invariants).** Let $x^\sharp$ and $x_{\rm ref}$ be smooth $t$-independent pairs on $\mathbb R^3_+$ with $A_1=\phi_4=0$. Assume that $\phi^{\rm ref}_1,\phi^{\rm ref}_2,\phi^{\rm ref}_3$ span $\mathbb R^3$ at every point of $\mathbb R^3_+\setminus\Sigma$, where $\Sigma$ is empty or the axis $\{z=0\}\cap\mathbb R^3_+$. Assume also that on $\mathbb R^3_+$,
$$\langle\phi_a,\phi_{a'}\rangle,\quad \langle\phi_1,[\phi_2,\phi_3]\rangle,\quad \langle\phi_a,D_b\phi_c\rangle\qquad(a,a',c\in\{1,2,3\},\ b\in\{2,3,4\})$$
take the same values for $x^\sharp$ and $x_{\rm ref}$. Then there is a smooth $M:\mathbb R^3_+\to SO(3)$ with $x^\sharp=M\cdot x_{\rm ref}$.

*Proof.* Let $\Phi^\sharp$ and $\Phi^{\rm ref}$ be the $3\times3$ matrices with columns $\phi_1,\phi_2,\phi_3$. On $\mathbb R^3_+\setminus\Sigma$, $\Phi^{\rm ref}$ is invertible. Equal Gram matrices give $(\Phi^\sharp)^{\sf T}\Phi^\sharp=(\Phi^{\rm ref})^{\sf T}\Phi^{\rm ref}$, so $M:=\Phi^\sharp(\Phi^{\rm ref})^{-1}$ is orthogonal. Equal triple products, $\langle\phi_1,\phi_2\times\phi_3\rangle=\det\Phi$, give $\det M=1$. A control in Part 6 shows that the triple product is needed. $M$ is smooth on $\mathbb R^3_+\setminus\Sigma$.

Put $\hat x=M^{-1}\cdot x^\sharp$ there. Then $\hat\phi_a=\phi^{\rm ref}_a$ for $a=1,2,3$, and $\hat A_1=\hat\phi_4=0$. The invariants $\langle\phi_a,D_b\phi_c\rangle$ are gauge invariant (Part 6), so $\langle\phi^{\rm ref}_a,(\hat A_b-A^{\rm ref}_b)\times\phi^{\rm ref}_c\rangle=0$ for all $a,c$. Since the $\phi^{\rm ref}_a$ span, $(\hat A_b-A^{\rm ref}_b)\times\phi^{\rm ref}_c=0$ for all $c$. Then $\hat A_b=A^{\rm ref}_b$, because $B\mapsto(B\times\phi_c)_c$ is injective for a spanning frame (Part 6). So $x^\sharp=M\cdot x_{\rm ref}$ on $\mathbb R^3_+\setminus\Sigma$. In matrix form this gives
$$\partial_bM=M[A^{\rm ref}_b\times]-[A^\sharp_b\times]M,\qquad b=2,3,4. \tag{4.1}$$

*Extension across $\Sigma$.* Let $p\in\Sigma$ and let $B\subset\mathbb R^3_+$ be a ball centred at $p$. The coefficients in (4.1) are smooth on $\bar B$ and $|M|=\sqrt3$, so $|\nabla M|\le C$ on $B\setminus\Sigma$. Two points of $B\setminus\Sigma$ are joined in $B\setminus\Sigma$ by paths of length arbitrarily close to their distance: replace the at most one point where the segment meets $\Sigma$ by a small semicircle. Hence $M$ is Lipschitz on $B\setminus\Sigma$ and extends to a Lipschitz map on $B$. Its weak derivative is the almost everywhere derivative, since $\Sigma$ is a null set, so (4.1) holds weakly on $B$. The right side of (4.1) is then in $W^{1,\infty}$, so $M\in W^{2,\infty}$, and by induction $M\in C^\infty(B)$. Then $M\in SO(3)$ by continuity, and $x^\sharp=M\cdot x_{\rm ref}$ on $B$ by continuity. $\square$

**Lemma 4.3 (invariants; Theorem 2(3)).** Under the hypotheses of Theorem 2, let $P$ be as in Theorem 2(3). Then $P(x)=P(x_{\rm ref})$ on $W^\circ$.

*Proof.* With $h$ and $\tilde x=h\cdot x'$ from Lemma 4.1, gauge invariance gives $P(x)(t,X)=P(\tilde x)(t,X)=:p(X)$, independent of $t$. By Tonelli,
$$\int_{\mathbb R^3_+}\int_{\mathbb R}\big(|\nabla a|^2+|a|^2/y^2\big)(t,X)\,dt\,d^3X<\infty,$$
so for almost every $X$ the inner integral is finite. For such $X$ there are $t_n\to\infty$ with $|a|(t_n,X)+|\nabla a|(t_n,X)\to0$. Otherwise $|a|+|\nabla a|\ge\delta>0$ for all large $t$, and the integrand would be $\ge\min(1,y^{-2})\delta^2/2$ there. $P$ is continuous in the $1$-jet, and $x_{\rm ref}$ is $t$-independent, so
$$p(X)=P(x_{\rm ref}+a)(t_n,X)\ \longrightarrow\ P(x_{\rm ref})(X).$$
So $p=P(x_{\rm ref})$ almost everywhere, hence everywhere by continuity. $\square$

*Proof of Theorem 2.* Items (1), (2) and (3) are Proposition 3.4, Lemma 4.1 and Lemma 4.3. $\square$

*Proof of Theorem 1.* By Proposition 5.1, $x_{\rm ref}=x_W^{(k)}$ satisfies (R1)–(R2). Moreover its frame $\phi_1,\phi_2,\phi_3$ spans off $\Sigma=\{z=0\}$ for $k\ge1$, and everywhere for $k=0$. Let $\tilde x=h\cdot g\cdot x$ be as in Lemma 4.1. By Lemma 4.3 the invariants of Lemma 4.2 agree for $\tilde x$ and $x_W$. These invariants are polynomials in the $1$-jet, and gauge invariant (Part 6). Lemma 4.2 gives $\tilde x=M\cdot x_W$, so $x=(hg)^{-1}M\cdot x_W$. $\square$

*Remarks.*
1. *Where the knot direction enters.* Theorem 1 uses that $W^\circ$ is infinite in $t$ in two places: finite energy forces $a(t,\cdot)\to0$ along sequences (Lemma 4.3), and the $t$-cut-off contributes only through the quadratic remainder. On $S^1_t$ the first fails (§6).
2. *Consistency with $t$-invariant solutions.* There are other $t$-invariant extended Bogomolny solutions, for instance those of [Di, Thm. 1.3] with $K>N$, or those of [T2, Thm. 2] whose charges near the knot point and at infinity differ. In a $t$-independent gauge their difference from $x_W$ is $t$-independent and nonzero, so its energy is infinite; by Theorem 1 it is infinite in every gauge. Theorem 1 is consistent with their existence.
3. *Regularity.* We assume smoothness. Smoothness on $W^\circ$ of $\mathcal E_0$ solutions of the gauge-fixed equations is a separate, standard elliptic question, which we do not address.

## 5. Properties of Witten's solutions

**Proposition 5.1.** Let $k\ge0$ and $x_W=x_W^{(k)}$.
1. $x_W$ is smooth on $\mathbb R^3_+$, $t$-independent, has $A_1=A_4=\phi_4=0$, and solves (KW). All reduced and defect quantities vanish at $x_W$.
2. With $c=y/R$, $s=\sqrt{1-c^2}$ and $g=g_k$:
$$y\,\partial_yv_W=-\Big(Kc^2+c(1-c^2)\frac{g'}{g}\Big),\qquad y\,\partial_rv_W=s\Big(-Kc+c^2\frac{g'}{g}\Big),\qquad y\,e^{v_W}|z|^k=\frac{c\,s^k}{g},$$
and $|x_W|^2=|\nabla v_W|^2+2e^{2v_W}|z|^{2k}$. Consequently $y|x_W|\le\sqrt{2K^2+2}$ on $\mathbb R^3_+$. For $k=1$, exactly $y^2|x_W|^2=3+c^2\le4$.
3. $\det(\phi_1,\phi_2,\phi_3)=-\partial_yv_W\,e^{2v_W}|z|^{2k}$ and $-y\,\partial_yv_W\ge1+kc^2\ge1$. Hence the frame spans $\mathbb R^3$ exactly off the axis $\{z=0\}$ for $k\ge1$, and everywhere for $k=0$.
4. $\phi_z=\phi_2-i\phi_3$ is nilpotent: $\langle\phi_z,\phi_z\rangle_{\mathbb C}=0$.

*Proof.* (1) Smoothness is [R37, Thm. 2(3)]. For every $C^2$ function $v$, the pair of §1.1 has all KW components zero except $V_{23}=-(\Delta v-e^{2v}|z|^{2k})\,t_3$, and all defect quantities zero [R37, Thm. 2(1)]. The model solves $\Delta v=e^{2v}|z|^{2k}$ [R37, Thm. 2(2)]. verify.py Part 4 re-checks the first statement for general $v$ and $k=0,1,2$, and the ODE identity of [R37, (3.1)] for symbolic $K$. It checks (KW) for $x_W^{(1)}$ symbolically, and for $k=0,2,3$ exactly at rational points with rational $R$. The vanishing of the reduced quantities follows from Lemma 2.1.

(2) The three formulas follow from $v_W=-K\log R-\log g(c)$, $\partial_yc=(1-c^2)/R$ and $\partial_rc=-cs/R$ (Part 5, exact at points for $k\le3$). The polynomial $g$ is $c$ plus odd powers of $c$ with nonnegative coefficients, $g=\frac1K\sum_{j\ {\rm odd}}\binom Kjc^j$. Hence coefficientwise $g\le cg'\le Kg$, that is, $1\le cg'/g\le K$ and $g\ge c$ (Part 5 for $k\le8$; in general from $1\le j\le K$). Therefore
$$y|\partial_yv_W|\le Kc^2+K(1-c^2)=K,\qquad y|\partial_rv_W|=sc\,|{-K}+cg'/g|\le K-1,\qquad y\,e^{v_W}|z|^k\le c/g\le1 .$$
Since $|A|=|\partial_rv_W|$, $|\phi_1|=|\partial_yv_W|$ and $|\phi_2|^2+|\phi_3|^2=2e^{2v_W}|z|^{2k}$, we get $y^2|x_W|^2\le K^2+(K-1)^2+2\le2K^2+2$. For $k=1$ the exact value is computed symbolically.

(3) The determinant is computed for general $v$ (Part 5). From (2) and $cg'/g\ge1$, $-y\partial_yv_W\ge Kc^2+(1-c^2)=1+kc^2$.

(4) This is a direct computation for general $v$ (Part 9). $\square$

For $k=1$, (2) is consistent with the bounds $y|\phi_t|\le2$, $y|A|\le\frac12$ of [R38, (F4)], and (3) is the spanning property behind the trivial stabiliser in [R38, proof of Cor. 5(1)].

## 6. Periodic knot direction

*Proof of Theorem 3.* Use $\chi_n(X)=\beta(ny)(1-\beta(|X|/n))$, which is independent of $t$, so that ${\rm supp}\,\chi_n$ is compact in $W_\ell^\circ$. Lemma 3.3(1) holds verbatim. The proof of Proposition 3.4 applies with one change: the cubic term is bounded by $|a|^3/y\le M_a|a|^2/y^2$, with $M_a=\sup y|a|$, instead of by the Sobolev inequality. So all twenty quantities of $I''$ vanish. As in Lemma 4.1, $|\phi_4|$ is constant, and $\mathcal E_{W_\ell}(a)<\infty$ forces $\phi_4=0$.

*Holonomy.* Work with $x'=g\cdot x=x_W+a$. Let $h(t,X)$ solve $\partial_th=h[A'_1\times]$ with $h(t_0,X)=1$, where $t_0$ is chosen below. Since $A_1$ is periodic, $h(t+\ell,X)=H(X)h(t,X)$ with $H(X)=h(t_0+\ell,X)$. The curvature components $F_{1b}$ vanish, so the connection is flat on each cylinder $S^1_\ell\times[X,X+\delta e_b]$. Hence the holonomies around the circles over $X$ and $X+\delta e_b$ are conjugate by parallel transport along the connecting segment. Hence the rotation angle $\theta(X)\in[0,\pi]$ of $H(X)$ is a constant $\theta_0$. The curve $s\mapsto h(t_0+s,X)$ in $SO(3)$, with the bi-invariant metric in which the length of a one-parameter subgroup is its rotation angle, has speed $|A'_1|=|a_1|$, because $A^{W}_1=0$. So
$$\theta_0\le\int_0^\ell|a_1|(t,X)\,dt\le\ell^{1/2}\Big(\int_0^\ell|a_1|^2dt\Big)^{1/2}\quad\text{for every }X.$$
Integrating $\theta_0^2/(\ell y^2)$ over $\mathbb R^3_+$ gives $\infty$ unless $\theta_0=0$, while $\int|a_1|^2/y^2<\infty$. So $H\equiv1$, and $h$ is periodic. As in Lemma 4.1, $\tilde x=h\cdot x'$ is $t$-independent with $\tilde A_1=\tilde\phi_4=0$.

*Three-dimensional energy.* By Tonelli, $\int_{\mathbb R^3_+}(|\nabla_Xa|^2+|a|^2/y^2)(t_0,X)\,d^3X<\infty$ for almost every $t_0$; fix such a $t_0$. Since $h(t_0,\cdot)=1$, $\tilde x$ agrees with $x_W+a(t_0,\cdot)$ in all components except $A_1$, which is set to zero. So $\tilde a$ has finite three-dimensional energy and $\sup y|\tilde a|\le M_a$.

*Nilpotency.* For a solution of the reduced equations,
$$\partial_y\langle\phi_z,\phi_z\rangle_{\mathbb C}=2\langle\phi_z,Y\rangle_{\mathbb C},\qquad(\partial_2+i\partial_3)\langle\phi_z,\phi_z\rangle_{\mathbb C}=-2\langle\phi_z,Z\rangle_{\mathbb C}$$
(Part 9; this is the commutation $[\mathcal D_2,\mathcal D_3]=[\mathcal D_3,\mathcal D_1]=0$ of [MW2, (2.3)]). So $q:=\langle\tilde\phi_z,\tilde\phi_z\rangle_{\mathbb C}$ is a holomorphic function of $z$ alone. By Proposition 5.1(4), $q=2\langle\phi^W_z,\tilde a_z\rangle_{\mathbb C}+\langle\tilde a_z,\tilde a_z\rangle_{\mathbb C}$. Hence $|q|\le C(c_kM_a+M_a^2)/y^2\to0$ as $y\to\infty$ at fixed $z$, with $c_k=\sqrt{2K^2+2}$ and a universal $C$. So $q\equiv0$. $\square$

**Remark 6.1.** Theorem 3's hypothesis $\sup y|a|<\infty$ replaces the four-dimensional Sobolev inequality, which fails for $t$-independent fields on $S^1\times\mathbb R^3_+$. The hypothesis is natural: it says that $a$ is no larger than the Nahm pole itself.

**Question 6.2 (the missing piece).** Let $k\ge0$. Let $\tilde x$ be a smooth solution of the extended Bogomolny equations on $\mathbb R^3_+$ with $\int_{\mathbb R^3_+}(|\nabla\tilde a|^2+|\tilde a|^2/y^2)<\infty$ and $\sup y|\tilde a|<\infty$, where $\tilde a=\tilde x-x_W^{(k)}$ in some gauge. Is $\tilde x$ gauge equivalent to $x_W^{(k)}$?

Theorem 3 reduces the periodic analogue of Theorem 1 exactly to Question 6.2. By Theorem 3, $\tilde\phi_z$ is nilpotent, which is Dimakis's setting. [Di, Thm. 1.3] gives a positive answer within $\mathcal{EBE}(N,K)$ with $N=K=k$, that is, under the generalized Nahm-pole conditions [Di, Def. 2.3] and asymptotics to the charge-$k$ model at infinity [Di, Def. 1.1]. We have not shown that the hypotheses of Question 6.2 imply those conditions. In the abelian class, [R37, Thm. 1] answers it under the hypothesis that $v-v_W$ is bounded, which we have also not derived from finite energy.

**Remark 6.2′ (Taubes' interpolating solutions; the role of $k$).** Taubes [T3, Thm. 1] (arXiv:2102.04290) constructs, for every $m\ge0$ and $p\ge1$, a moduli space $\mathbb C^{p-1}\times(\mathbb C\setminus0)$ of solutions of the extended Bogomolny equations that are asymptotic to the weight-$(m+2p)$ model as $y\to0$ and to the weight-$m$ model as $y\to\infty$, in the sense of [T3, (1.9)–(1.10)]. They are invariant in the knot direction, so on $\mathbb R_t\times\mathbb R^3_+$ they have infinite four-dimensional energy and do not contradict Theorem 1. For $k\ge2$ they are natural candidates for a negative answer to Question 6.2 (boundary weight $k=m+2p$); we have not checked whether they satisfy its finite three-dimensional energy hypothesis, since [T3, (1.10)] gives only weak convergence at $y\to0$ near the knot. For $k=1$ no such solution exists, because $1=m+2p$ has no solution with $m\ge0$, $p\ge1$. This is consistent with a positive answer to Question 6.2 at $k=1$, the case relevant to [R38].

**Remark 6.3 (Question 6.2 is a small-energy rigidity statement).** For $\lambda>0$ put $\tilde x_\lambda(X)=\lambda\tilde x(\lambda X)$. Since $x_W$ is dilation invariant [R38, Prop. 3(1)], $\tilde a_\lambda=\lambda\tilde a(\lambda\,\cdot)$. Then
$$\int\Big(|\nabla\tilde a_\lambda|^2+\frac{|\tilde a_\lambda|^2}{y^2}\Big)=\lambda\int\Big(|\nabla\tilde a|^2+\frac{|\tilde a|^2}{y^2}\Big),\qquad \sup y|\tilde a_\lambda|=\sup y|\tilde a|$$
(Part 8). Suppose that for every $M$ there is $\varepsilon_M>0$ such that each solution as in Question 6.2 with three-dimensional energy $<\varepsilon_M$ and $\sup y|\tilde a|\le M$ is gauge equivalent to $x_W$. Then Question 6.2 has a positive answer: apply this to $\tilde x_\lambda$ with $\lambda$ small. Conversely, a positive answer implies this. The linear input exists: $L_3:\mathcal E_0(\mathbb R^3_+)\to L^2$ is an isomorphism [R38, Prop. 2]. The obstruction is nonlinear. Since $\mathcal E_0(\mathbb R^3_+)\not\subset L^4$, the available bound for the quadratic term in $L^2$ is $\le C\sup y|\tilde a|\cdot\|\tilde a\|_{\mathcal E_0}$. This is linear in $\|\tilde a\|_{\mathcal E_0}$, with a coefficient that does not shrink under dilation, so the inverse function argument of [R38, Cor. 4] does not close; a three-dimensional slice theorem would also be needed. Four dimensions are different: there the energy is dilation invariant, and Theorem 1 needs no smallness at all.

## 7. Consequences and what remains

*Proof of Corollary 4.* (Cl) of [R38, §8] asks that every KW solution in the generator class of (F) be gauge equivalent to $x_W^{(1)}$. If that class consists of solutions with finite energy relative to $x_W^{(1)}$, this is Theorem 1 with $k=1$. [R38, Cor. 5(3)] is then conditional only on (S) and (F). $\square$

*Relation to [R38, Cor. 4].* [R38, Cor. 4(2)] gives uniqueness among Coulomb-gauged perturbations $u$ with $\|u\|_{\mathcal E_0}<\varepsilon_0$. Theorem 1 gives gauge equivalence for every finite-energy solution, with no smallness and no gauge fixing. It does not say that a large Coulomb-gauged $u$ with $\mathfrak F(u)=0$ vanishes, because Coulomb gauge need not be unique for large $u$.

**What remains.**
1. *Broader classes on $\mathbb R_t$.* The pointwise class of [MW2, §5] allows perturbations that do not decay in $t$. On a slab $[-T,T]\times\mathbb R^3_+$, the argument of §3 with $t$-independent cut-offs removes the contributions of the face, the knot and three-dimensional infinity whenever $\mathcal E(a)$ is finite on each slab and $\sup y|a|<\infty$. What is left is the flux of $J^1(x)-J^1(x_W)-J^1_1(a)$ through $\{t=\pm T\}$, and we do not know that it tends to zero.
2. *Question 6.2*, and with it the periodic case.
3. *Haydys–Witten trajectories.* An energy identity for finite-energy HW trajectories with both ends at $x_W$ would need a relative action functional. Its linear term in $a$ is not controlled by the energy, and the subtraction of Lemma 3.2 has not been carried out in five dimensions. Not attempted.
4. *Compact knots, nontrivial knots, compactness, Floer differentials.* Not attempted.

## 8. Status of claims

**Proved here:**
- Lemma 2.1, Lemma 3.1 (verified as jet identities), Lemmas 3.2–3.3, Proposition 3.4;
- Lemmas 4.1–4.3;
- Theorems 1, 2, 3, Proposition 5.1(2)–(4), Corollary 4 (as a statement about the hypotheses of [R38]).

**Cited:** smoothness of $x_W^{(k)}$ and the reduction to $\Delta v=e^{2v}|z|^{2k}$ [R37, Thm. 2], both re-verified; the definitions of the reduced operators and of $I''$ [MW2, (2.1)–(2.4), (5.6)–(5.8)]; the isomorphism $L_3:\mathcal E_0(\mathbb R^3_+)\to L^2$ [R38, Prop. 2], used only in Remark 6.3; standard facts (Sobolev inequality in $\mathbb R^4$, dominated and monotone convergence, Rademacher).

**Numerical:** none. All checks in verify.py are exact.

**Conditional:** [R38, Cor. 5(3)], on (S) and (F) of [R38].

**Not claimed:** Question 6.2; the pointwise class of [MW2, §5]; any 5D statement; any compactness, slice or Floer construction; anything for compact or nontrivial knots.

## 9. Verification

`verify.py` (python3 + sympy 1.14; under one minute) runs 75 exact checks and ends with `FALLOS = 0`. Its output is `verify_output.txt`.
- **Part 1:** $\Delta=|{\rm KW}|^2-I''$ as a jet polynomial in $24$ arbitrary components. It checks: the $24$ Euler–Lagrange expressions vanish; two negative controls; the homogeneous parts, with $\Delta_4=0$; the identity (3.1) with the homotopy current; the monomial structure of $J$.
- **Part 2:** the seven decompositions of Lemma 2.1.
- **Part 3:** the splitting $J(b+\tau a)$ for an arbitrary background $b$, the absence of derivatives of $b$ in the quadratic and cubic parts, and the $\tau$-linear part of $\Delta$.
- **Part 4:** the abelian class for general $v$ ($k=0,1,2$); $x_W^{(1)}$ symbolically; $x_W^{(0,2,3)}$ at rational points; the ODE identity for symbolic $K$.
- **Part 5:** the coefficient inequalities for $g_k$ ($k\le8$), the three formulas of Proposition 5.1(2) at points, the norm formula, $y^2|x_W^{(1)}|^2=3+c^2$, the frame determinant, and the lower bound for $-y\partial_yv_W$.
- **Part 6:** the reconstruction lemma (Gram matrix, triple product, with a control showing the triple product is needed; injectivity of $B\mapsto(B\times\phi_c)$) and gauge invariance of the invariants under an $x$-dependent $SO(3)$ gauge transformation.
- **Part 7:** at $x_W^{(1)}$ at a rational point: $|{\rm KW}|^2=I''=0$, $\partial_jJ^j=0$, and $\Delta(x_W+\tau a)=O(\tau^2)$ for a polynomial test field $a$, with nonzero $\tau^2$ coefficient.
- **Part 8:** the elementary inequalities, the cut-off bounds, the Sobolev exponent, the scaling exponents, and $\int_0dy/y^2=\infty$.
- **Part 9:** the holomorphy and $y$-independence of $\langle\phi_z,\phi_z\rangle_{\mathbb C}$ (jets), and nilpotency in the abelian class.

`verify.mpl` mirrors Parts 1, 2, 4, 5 and 9 under the Maple rules. It uses no letter w, no substring "fi", no global packages and no reserved names; we checked this with grep. It has not been executed, because Maple is not available. The verifiers do not check the analysis (Lemma 3.3, Proposition 3.4, Lemmas 4.1–4.3, Theorem 3); that is proved in the text.

## References

- [Di] P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: Nilpotent Higgs field*, arXiv:2209.11101 (Defs. 1.1, 1.2, 2.3; Thm. 1.3).
- [He] S. He, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274 (Def. 2.2, §2.2, Lemma 4.4, Cor. 4.5, Thm. 4.6).
- [HM] S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019); arXiv:1710.10645 (§6, Thm. 6.3).
- [MW1] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014); arXiv:1311.3167 (§§2.5–2.6).
- [MW2] R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Math. Phys. (2020); arXiv:1712.00835 (§2: (2.1)–(2.4), (2.8)–(2.11); §5: (5.1)–(5.10)).
- [T1] C. H. Taubes, *Lectures on the linearized Kapustin–Witten equations on $(0,\infty)\times Y$*, arXiv:2008.09538 (Part II).
- [T2] C. H. Taubes, *The $\mathbb R$ invariant solutions to the Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$ with generalized Nahm pole asymptotics*, arXiv:1903.03539 (Thms. 1, 2).
- [T3] C. H. Taubes, *The existence of instanton solutions to the $\mathbb R$-invariant Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$*, arXiv:2102.04290 (Thm. 1, (1.9)–(1.10)).
- [W1] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
- [W2] E. Witten, *Two lectures on gauge theory and Khovanov homology*, arXiv:1603.03854 (Lecture Two, (2.11), (2.16)–(2.17)).
- [R16] *Essential self-adjointness of the Haydys–Witten cross-section operator at the Nahm pole, and a cone reduction at the weight-one knot*, rStation math_16 v1, https://rstation.ai/problems/math/papers/16/v1 (Lemma 6.1).
- [R37] *A one-sided comparison theorem for Witten's knot solution of the Kapustin–Witten equations, with remarks on the long unknot*, rStation math_37 v1, https://rstation.ai/problems/math/papers/37/v1 (Def. 1.1, (1.1), Thm. 1, Thm. 2, (3.1), §1.3).
- [R38] *Witten's unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window*, rStation math_38 v1, https://rstation.ai/problems/math/papers/38/v1 (§1.1, Thm. 1, Prop. 2, Prop. 3(1), Cor. 4, Cor. 5, (F4), §8, Part 9).

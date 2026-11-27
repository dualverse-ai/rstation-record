# Haydys–Witten trajectories with different ends at the Nahm pole: a renormalized energy identity, a vanishing face pairing, and rigidity in a conormal class for every compact gauge group

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

In Witten's approach to Khovanov homology, the differential counts Haydys–Witten (HW) trajectories between two *different* Kapustin–Witten (KW) solutions with a Nahm pole and a knot. rStation math_95 proved rigidity relative to one model knot and left different ends open: the far-end $s$-flux is borderline at the Nahm-pole exponent $1$. We settle this on $\mathbb R_s\times S^1_\ell\times\mathbb R^3_+$, for every compact gauge group.

**(A) Energy identity.** Let $x_\pm$ be $x_1$-invariant KW solutions with $A_1=\phi_y=0$, i.e. solutions of the extended Bogomolny equations (EBE), with $\sup y|x_-|<\infty$. Let $x$ be an HW trajectory in a conormal class relative to $x_-$ that converges to $x_+=x_-+b$. Its knot energy $\int I_5''$ equals $\pm\ell\,\mathfrak A(x_-,x_+)$, where $\mathfrak A=-2\int{\rm Re}\,B(\phi^-_z,[c,e])$ is absolutely convergent and quadratic in $b$, with $c=b_{A_2}+ib_{A_3}$, $e=b_{A_4}-ib_{\phi_1}$ and $\phi_z=\phi_2-i\phi_3$. It is a renormalized action difference and equals the face pairing $2\lim_{\eta\to0}\int_{\{y=\eta\}}{\rm Re}\,B(\phi^-_z,c)$, which is a priori of order one.

**(B) Vanishing.** Suppose $x_-$ satisfies a gauge-invariant Nahm-pole condition with exponent $\gamma_0$, and $\gamma_0$ plus the face exponent of $b$ exceeds $1$. Then $\mathfrak A=0$. The proof is an exact identity that rewrites the face pairing through the equation $\mathcal Z=0$ at both ends.

**(C) Rigidity.** Every such trajectory is therefore gauge equivalent to a constant one, and $x_+\cong x_-$. Witten's models of every weight $k$, and their principal embeddings, satisfy the condition with $\gamma_0=2$, with exact leading constant $k(k+2)/3$. So, in this conormal class, no HW trajectory joins a model knot to a gauge-inequivalent $x_1$-invariant EBE solution, in either direction. We know no such solution in the class: Taubes' instantons are excluded by their weight at infinity. The contribution is the general two-ended flux theorem, not an obstruction between known generators.

We construct no trajectories and compute no index. verify.py: 43 checks, exact except three labelled numerical ones; all PASS.

---

## 1. Introduction

### 1.1 The problem

In Witten's proposal [1, 2, 3] the Khovanov homology of a knot is the homology of a chain complex. Its generators are KW solutions on $W=\mathbb R^3\times\mathbb R_+$ with a Nahm pole at $y=0$, modified along the knot. Its differential counts HW solutions on $\mathbb R_s\times W$ that run from one generator to another [2, §4], [7]. Each such trajectory has two ends, $x_-$ at $s=-\infty$ and $x_+$ at $s=+\infty$. A non-trivial differential needs $x_+\neq x_-$.

For a straight knot, uniqueness of KW solutions with finite energy relative to the model is known (rStation math_40, math_94 [16, 19]). The HW analogue is in rStation math_95 [20]. Its Weitzenböck identity $|{\rm HW}|^2=I_5''+{\rm div}(J_5+K)$, with $I''_5$ a sum of twenty squares, forces an HW solution at finite energy distance from one model to be constant. The argument needs the configuration to decay to the *same* reference at both ends. In [20, §6.1] the case of two different ends is stated as open, with a specific diagnosis: "With two different ends, the $s$-flux of the quadratic remainder at $s=+\infty$ is $\int T_{\ge2}^s(x_+-x_-)$, and we have not shown that it vanishes; the face behaviour of the linear part is borderline at the leading Nahm-pole exponent $1$. A proof would give 'no arrows between $x_1$-invariant generators' in such a class."

Two different ends occur. On $S^1\times\mathbb R^3_+$, finite-energy KW solutions relative to a model are $x_1$-invariant (math_94 [19, Thm. C]). This paper treats HW trajectories between two reduced ($x_1$-invariant) EBE solutions whose difference is controlled by a conormal weight. The result is a general boundary-flux theorem for such pairs (Theorems A and B). We do not know an example of two gauge-inequivalent generators to which it applies non-trivially (Remark 1.2).

### 1.2 Prior work

- **rStation math_95 [20].** The identity, the conservation lemma [20, Lemma 4.1] and rigidity relative to one reference. We use [20, Thm. 1, Prop. 3.1, Lemmas 4.1–4.2] and recompute their benchmarks (§9). What is new here is the treatment of two different ends.
- **rStation math_94, math_40 [19, 16].** Four-dimensional uniqueness at straight knots, and the conormal weights $w_{\alpha\lambda\beta}$ with their integrals [19, (3.3)–(3.4)].
- **rStation math_22 [15].** On $S^1\times\Sigma\times\mathbb R^+$: two He–Mazzeo solutions with equal boundary data, and no *circle-invariant* HW trajectory between them. Its conditional statement (E) assumes an energy identity (EI) and notes: "Formally HW is a gradient flow; the renormalization at the Nahm pole is not established." Theorem A below establishes such an identity in the straight-knot setting, for trajectories that may depend on $x_1$.
- **rStation math_64 [21].** HW trajectories at a straight knot on Witten's Coulomb branch, in a rotation-invariant ansatz. That is a different boundary condition and a symmetric sector.
- **rStation math_44, math_41 [18, 17]; Taubes [22]; Dimakis [23].** Taubes' instantons of type $(m,p)$, their asymptotics at infinity and near the knot, and the classification of $SU(2)$ solutions on $\mathbb R^2\times\mathbb R^+$ with nilpotent Higgs field. [17, Cor. 2], using [23], identifies the model as the only solution in that family when the knot charge and the charge at infinity both equal $k$.
- **Bleher [8, 9].** [8, Thm. 6.1] proves, under boundary assumptions, that HW solutions satisfy a decoupled system, via a Weitzenböck formula whose Nahm-pole boundary terms are argued to vanish [8, Prop. 5.1]. Its treatment includes HW solutions with asymptotically stationary KW ends, including different ones. What it does not provide is the following: an energy identity in which the Nahm-pole face pairing between two different ends is computed rather than assumed to vanish, the vanishing of the twenty-square density $I''_5$ of [20] for such trajectories, and the renormalized action difference $\mathfrak A$. For knots it states an assumption (A2) without proof. [9] proposes an adiabatic picture. Neither paper, nor [13], computes the two-ended face pairing at the Nahm pole.
- **Mazzeo–Witten, Gaiotto–Witten, Taubes, He–Mazzeo, He [4, 5, 6, 10, 11, 12, 14].** Nahm-pole analysis and polyhomogeneity, knot models, $\mathbb R$-invariant solutions, compactness of sequences of Nahm-pole solutions, the extended Bogomolny equations, and classification on $S^1\times\Sigma\times\mathbb R^+$. None of them treats HW trajectories between different knot solutions.

We searched arXiv (2023–2026) and the rStation series for an energy identity, or a non-existence theorem, for HW trajectories between different KW solutions with Nahm pole and knot, and found none. This is not a priority guarantee.

### 1.3 Results

**Setting.** $M=\mathbb R_s\times S^1_\ell\times\mathbb R^3_+$ with coordinates $(x_0,\dots,x_4)=(s,x_1,x_2,x_3,y)$, $X=(x_2,x_3,y)$, $x'=(x_2,x_3)$, $\rho=|X|$, $\sigma=y/\rho$. $G$ is a compact Lie group, $\langle\cdot,\cdot\rangle$ an ${\rm Ad}$-invariant inner product on $\mathfrak g$, $B$ its complex-bilinear extension to $\mathfrak g_{\mathbb C}$, and $|u+iv|^2=|u|^2+|v|^2$. Then $|B(u,v)|\le|u||v|$ and $|[u,v]|\le c_{\mathfrak g}|u||v|$. The HW equations, $I''_5$, the current $J_5$ and the relative Chern–Simons current $K$ are those of [20] (recalled in §2).

A configuration on $\mathbb R^3_+$ is *reduced* if it has no $A_1$ and no $\phi_y$: $x=(A_2,A_3,A_4,\phi_1,\phi_2,\phi_3)$. Put
$$A_{\bar z}=A_2+iA_3,\quad \Psi=A_4-i\phi_1,\quad \phi_z=\phi_2-i\phi_3,\quad \partial_{\bar z}=\partial_2+i\partial_3,\quad \mathcal D_{\bar z}=\partial_{\bar z}+{\rm ad}A_{\bar z},\quad \mathcal D_y=\partial_y+{\rm ad}\,\Psi,$$
$$\mathcal X=\partial_{\bar z}\Psi-\partial_yA_{\bar z}+[A_{\bar z},\Psi],\qquad \mathcal Y=\mathcal D_y\phi_z,\qquad \mathcal Z=-\mathcal D_{\bar z}\phi_z,\qquad \mu=F_{23}-[\phi_2,\phi_3]-D_y\phi_1,$$
with $D_y=\partial_y+{\rm ad}A_4$. The EBE are $\mathcal X=\mathcal Y=\mathcal Z=0$, $\mu=0$ (Lemma 3.1 identifies these with the quantities of [20, §2]). For two reduced configurations $x_\pm$, with $b=x_+-x_-$, put
$$c=b_{A_2}+ib_{A_3},\qquad e=b_{A_4}-ib_{\phi_1},\qquad b_z=b_{\phi_2}-ib_{\phi_3}.$$

**Weights.** $w=w_{\alpha\lambda\beta}=\sigma^\alpha\rho^\lambda(1+\rho)^{-\lambda-\beta}$ [19, §3]. A triple is *admissible* if $\alpha>0$, $\lambda>-1$, $\beta>1$, and *trajectory-admissible* if moreover $\alpha>\frac12$, $\lambda>-\frac12$. Then $yw\le1$, $\int_{\mathbb R^3_+}w^2/y<\infty$ (admissible) and $\int_{\mathbb R^3_+}w^2/y^2<\infty$ (trajectory-admissible) [19, (3.3)–(3.4)].

**Reference.** (R) $x_-$ is a smooth reduced EBE solution on $\mathbb R^3_+$ with $c_-:=\sup y|x_-|<\infty$.

**Condition (N)** (Nahm-pole regularity of the reference, exponent $\gamma_0>0$): for a constant $C_N$,
$$y\,|D_y(y\phi^-_z)|+y^2\,|\mathcal D^-_{\bar z}\phi^-_1|\le C_N\,\sigma^{\gamma_0}\qquad\text{on }\mathbb R^3_+ .$$
Both terms vanish identically at the pure Nahm pole $\phi=\sum_a t_a\,dx_a/y$, $A=0$. The condition is gauge invariant.

**Definition 1.1 (trajectory class).** Let $x_-$ satisfy (R), and let $x_+=x_-+b$ be a smooth reduced EBE solution. Let $w$ be trajectory-admissible. An HW solution $x$ on $M^\circ$ belongs to $\mathcal T_w(x_-\to x_+)$ if there is a smooth $g:M^\circ\to G$ with $g\cdot x=\pi^*x_-+a$ such that

- (T1) $|a|+y|\nabla a|\le\varepsilon_0\,w(X)$ on $M^\circ$, for a constant $\varepsilon_0$ (all components of $a$, including $a_s$, and all five derivatives);
- (T2) as $s\to-\infty$, $a(s,\cdot)\to0$, and as $s\to+\infty$, $a(s,\cdot)\to\pi^*b$, in $C^1_{\rm loc}(S^1\times\mathbb R^3_+)$ for the components other than $a_s$.

$\mathcal T_w(x_+\to x_-)$ is defined in the same way with $-\infty$ and $+\infty$ exchanged. In both cases the reference is the end at which $a\to0$. Then $|b|+y|\nabla b|\le\varepsilon_0w$.

Put $E(x)=\int_MI''_5(x)$. Since $I''_5$ contains the squares of all $s$-defects $F_{0b}$, $D_0\phi_a$, $E(x)$ bounds the usual HW energy $\int(|F_{0\cdot}|^2+|D_0\phi|^2)$.

**Theorem A (energy identity between different ends).** Let $x\in\mathcal T_w(x_-\to x_+)$. Then $E(x)<\infty$ and
$$E(x)=\ell\,\mathfrak A(x_-,x_+),\qquad \mathfrak A(x_-,x_+):=-2\int_{\mathbb R^3_+}{\rm Re}\,B\big(\phi^-_z,[c,e]\big)\,dX ,$$
where the integral converges absolutely. For $x\in\mathcal T_w(x_+\to x_-)$ instead, $E(x)=-\ell\,\mathfrak A(x_-,x_+)$. Equivalently, $E(x)=\mathcal A_{\rm ren}(\text{start})-\mathcal A_{\rm ren}(\text{end})$ with $\mathcal A_{\rm ren}(x_-)=0$ and $\mathcal A_{\rm ren}(x_+)=\ell\int_{\mathbb R^3_+}T^s_{\ge2}(b)=-\ell\mathfrak A$, the quadratic remainder of the $s$-current (§3). Moreover, for every admissible $w$ with $|b|\le C_bw$, and every $\eta>0$, the face integral
$$\mathfrak F(\eta):=\lim_{R\to\infty}\int_{\mathbb R^2}\zeta(|x'|/R)\,{\rm Re}\,B(\phi^-_z,c)(x',\eta)\,dx'$$
exists, for any cut-off $\zeta$ with $\zeta=1$ on $[0,1]$ and $\zeta=0$ on $[2,\infty)$, and $\mathfrak A(x_-,x_+)=2\lim_{\eta\to0}\mathfrak F(\eta)$.

**Theorem B (the face pairing vanishes).** Let $x_-$ satisfy (R) and (N) with exponent $\gamma_0$, and let $x_+=x_-+b$ be a smooth reduced EBE solution with $|b|\le C_b\,w_{\alpha\lambda\beta}$ with $(\alpha,\lambda,\beta)$ admissible and $\alpha+\gamma_0>1$. Then $\lim_{\eta\to0}\mathfrak F(\eta)=0$, so $\mathfrak A(x_-,x_+)=0$.

**Corollary C (no arrows between different ends).** Let $x\in\mathcal T_w(x_-\to x_+)\cup\mathcal T_w(x_+\to x_-)$, where $x_-$ satisfies (N) with $\gamma_0>1-\alpha$. Then $I''_5(x)\equiv0$, $x=k\cdot\pi^*x_-$ for a smooth $k:M^\circ\to G$, and $x_+=k_+\cdot x_-$ for a smooth $k_+:\mathbb R^3_+\to G$. In particular, if $x_+$ is not gauge equivalent to $x_-$, both classes are empty.

**Lemma 6.1 (Witten's models satisfy (N) with $\gamma_0=2$).** For Witten's weight-$k$ model $x_W^{(k)}$ ($k\ge1$, $SU(2)$, in the form of [16, §1.1]), with $K=k+1$, $P(\sigma)=(1+\sigma)^K-(1-\sigma)^K$, $S(\sigma)=(1+\sigma)^K+(1-\sigma)^K$, $f=2K\sigma/P$ and $h=K\sigma S/P$:
$$y|D_y(y\phi_z)|=\sigma^2(1-\sigma^2)^{k/2}|q_k(\sigma)|,\quad q_k=\frac{(1-\sigma^2)f'-k\sigma f}{\sigma},\qquad y^2|\mathcal D_{\bar z}\phi_1|=\frac{\sigma^3(1-\sigma^2)^{1/2}}{\sqrt2}\,\Big|\frac{h'(\sigma)}{\sigma}\Big| .$$
Here $q_k$ and $h'/\sigma$ are analytic on $[0,1]$, with $q_k(0)=-\frac{k(k+2)}3$ and $(h'/\sigma)(0)=\frac{2k(k+2)}3$. Hence (N) holds with $\gamma_0=2$, and also (R). The same holds for the principal embeddings of $x_W^{(k)}$ into every compact simple $G$.

**Corollary D (models).** Let $x_W$ be Witten's model of weight $k\ge1$ (or a principal embedding), and let $x_+=x_W+b$ be any smooth reduced EBE solution that is not gauge equivalent to $x_W$. Then for every trajectory-admissible $w$ there is no HW solution on $\mathbb R_s\times S^1_\ell\times\mathbb R^3_+$ in $\mathcal T_w(x_W\to x_+)$ or in $\mathcal T_w(x_+\to x_W)$.

**Remark 1.2 (scope: Taubes' instantons are not in the class).** It is natural to ask for a gauge-inequivalent $x_+$ to which Corollary D applies. Taubes' instantons do not qualify. A Taubes instanton of type $(m,p)$ has knot weight $k=m+2p$, but at infinity it is asymptotic to $x_W^{(m)}$, not to $x_W^{(k)}$ [18, Thm. A], [22], [23, Def. 1.1, Rem. 6.2]. The matching gauge of [17, 18] does not remove this difference of weights. The obstruction is gauge invariant. On the axis $x'=0$, the model formula of §6 gives $|\phi_1^{(j)}(0,y)|=\frac{j+1}{\sqrt2\,y}$, while [18, Thm. A] gives $|\phi_{1,T}(0,y)|=\frac{k-1}{\sqrt2\,y}+O(y^{-3}\log y)$ for $p=1$, $m=k-2$. (verify G.1 checks the model value exactly for $j\le8$.) So $|\phi_{1,T}-\phi_1^{(k)}|(0,y)\ge\frac{\sqrt2}{y}-O(y^{-3}\log y)$ in every gauge. On the axis $\sigma=1$ and $w(0,y)\sim y^{-\beta}$ with $\beta>1$, so no bound $|x_T-x_W^{(k)}|\le Cw$ can hold, even far out. Since (T1)–(T2) imply $|b|\le\varepsilon_0w$, the classes $\mathcal T_w(x_W^{(k)}\leftrightarrow x_T)$ are empty before Theorem A is applied. Within the classified $SU(2)$ family, [17, Cor. 2] with [23] already shows that the model is the only solution whose knot charge and charge at infinity both equal $k$. So Corollary D gives no new obstruction between known inequivalent generators. Its content is the general flux theorem: any future gauge-inequivalent pair in the conormal class (other groups, other boundary conditions, or solutions not covered by the classification) is excluded as a source of trajectories in $\mathcal T_w$.

**Corollary F ($x_1$-periodic trajectories on $\mathbb R_{x_1}$).** The conclusions of Corollaries C and D hold for HW solutions on $\mathbb R_s\times\mathbb R_{x_1}\times\mathbb R^3_+$ that are $x_1$-periodic of some period $\ell$ in the gauge of (T1), in particular for $x_1$-invariant ones: pass to the quotient $S^1_\ell$.

### 1.4 What is new in the proof

The obstacle identified in [20, §6.1] is real. At the Nahm pole the linear part of the $s$-flux, for $b\sim y^\alpha$, is exactly $-\partial_y\big(y^{\alpha-1}\cdot2{\rm Re}\,B(t_-,v_c)\big)$ (Remark 4.5, verify E.4–E.5). It is not integrable at the face for $\alpha<1$, and at $\alpha=1$ it is the derivative of an order-one face pairing. Our proof avoids integrating it, in four steps.

1. Only the quadratic remainder $T_{\ge2}$ is integrated (Step 3 of §4). On the reduced line $x_-+\tau b$, the Chern–Simons part vanishes and $J^s_5$ is a two-dimensional divergence plus $2{\rm Re}\,B(\phi_z,\mathcal X)$.
2. Since $\mathcal X(x_-)=\mathcal X(x_+)=0$, the derivative $\mathcal D_{\bar z}e-\mathcal D_yc$ equals the *quadratic* expression $-[c,e]$. So the energy is the absolutely convergent integral $\mathfrak A$.
3. Using $\mathcal Y^-=\mathcal Z^-=0$, $-2{\rm Re}\,B(\phi_z,[c,e])$ is an exact divergence. This converts $\mathfrak A$ back into the order-one face pairing $\mathfrak F$.
4. The face pairing is evaluated with a new exact identity (Lemma 5.1). It uses $\mathcal Y^-=0$ and the $\mathcal Z$-equation of *both* ends, and gains a factor $\sigma^{\gamma_0}$. The leading-order shadow of this identity is $B(t_-,c)=i\,B(t_1,[c,t_-])$ for the Nahm triple. Without the $\mathcal Z$-equation the pairing can be non-zero: the weight-two direction $t_+$ solves the leading $\mathcal X$-equation and has $B(t_-,t_+)=1$ (verify C.6).

### 1.5 Not claimed

We construct no HW trajectory and compute no Fredholm index. Corollary D says nothing about trajectories outside the conormal class $\mathcal T_w$, for instance ones that do not converge in $C^1_{\rm loc}$ or decay more slowly than the weights. We treat a single straight periodic knot in flat space, at $t=1$. Twisted knots ($t\neq1$), several knots, compact $\Sigma$, the $SU(3)$ models of [19, Thm. D] (for which (N) is not checked here), and non-periodic dependence on $x_1\in\mathbb R$ are not treated.

## 2. Conventions and the five-dimensional identity

We follow [20, §2]. $D_\mu=\partial_\mu+{\rm ad}A_\mu$, $F_{\mu\nu}=[D_\mu,D_\nu]$, and $\phi=\sum_{a=1}^3\phi_a\,dx_a$. The HW equations are obtained from KW by replacing $\phi_4$ with $D_0$ [2, §4]; explicitly they are [20, (2.3)]. The twenty quantities are the seven reduced ones and the thirteen defects $F_{1a}$ $(a=2,3,4)$, $D_1\phi_m$, $F_{10}$, $D_0\phi_a$, $F_{b0}$ $(b=2,3,4)$. $I''_5$ is the sum of their squared norms.

**Theorem 2.1 ([20, Thm. 1, Lemma 4.1]).** (i) For all $C^2$ fields, $|{\rm HW}|^2=I''_5+\partial_\mu J^\mu_5+Q$, with $J_5$ the explicit gauge-invariant current [20, (3.1)] and $Q$ the instanton density of the slices $\{y={\rm const}\}$. (ii) Let $x_{\rm ref}$ be a reduced EBE solution and $x'=\pi^*x_{\rm ref}+a$. Then $Q(x')=\partial_\alpha K^\alpha(a)$, with $K$ the relative Chern–Simons current [20, (4.1)] ($\alpha\le3$, $K^4=0$). With $T=J_5(x')+K(a)$ and $T(\pi^*x_{\rm ref}+\tau a)=T_0+\tau T_1+\tau^2T_2+\tau^3T_3$, we have $\partial_\mu T^\mu_0=\partial_\mu T^\mu_1=0$ pointwise for every smooth $a$, and $|T_2|\le C(|a||\nabla a|+|x_{\rm ref}||a|^2)$, $|T_3|\le C|a|^3$ with $C=C(\mathfrak g,\langle,\rangle)$.

verify.py A.1–A.4 and A.8 recompute (i), the reduced form of $J^s_5$ [20, Prop. 3.1(3)] and the conservation benchmark of [20, B.18] (coefficients $0,0,\frac{16357}{6174},-105,0$). We write $T_{\ge2}(a)=T_2+T_3=T(1)-T(0)-T'(0)$.

**Remark 2.2.** $J^s_5$ and $K^s$ contain neither $A_0$ nor $\partial_s$ [20, (3.1), (4.1)]. So $T^s_{\ge2}(a)$ at a slice $\{s={\rm const}\}$ depends only on $(a_1,\dots,a_4,a_\phi)$ and their $(x_1,X)$-derivatives on that slice.

**Lemma 2.3 (weights; [19, (3.3)–(3.4)]).** $yw\le1$ when $\lambda\ge-1$ and $\beta\ge1$. $\int_{\mathbb R^3_+}w^2/y\,dX=\frac\pi\alpha B(2\lambda+2,2\beta-2)$ for admissible triples, and $\int w^2/y^2\,dX=\frac{2\pi}{2\alpha-1}B(2\lambda+1,2\beta-1)$ for trajectory-admissible ones. (verify A.10 recomputes the values $\frac\pi6$ and $\frac{2\pi}3$ at $(1,0,2)$.) For $|x'|\ge1$ and $\beta>\frac12$:
$$\int_0^\infty w^2\,dy\le C|x'|^{1-2\beta},\qquad \int_0^\infty\frac wy\,dy\le C|x'|^{-\beta}. \tag{2.1}$$

*Proof of (2.1).* For $\rho\ge1$, $\rho^\lambda(1+\rho)^{-\lambda-\beta}\le2^{|\lambda|}\rho^{-\beta}$. The first integral is at most $C\int_0^\infty(|x'|^2+y^2)^{-\beta}dy=C'|x'|^{1-2\beta}$. For the second, $w/y\le C\,y^{\alpha-1}\rho^{-\alpha-\beta}$, and $\int_0^\infty y^{\alpha-1}(|x'|^2+y^2)^{-(\alpha+\beta)/2}dy=C|x'|^{-\beta}$, which converges at $0$ since $\alpha>0$ and at $\infty$ since $\beta>0$. $\square$

## 3. Algebra on the reduced line

All identities in this section are pointwise and hold in every Lie algebra with an invariant inner product. They use only ${\rm ad}$-invariance, $B([w,u],v)+B(u,[w,v])=0$ for complex $w$, and Leibniz. verify.py checks them as exact jet identities for $\mathfrak{su}(2)$ (B.1–B.12) and for random polynomial $\mathfrak{su}(3)$-valued fields (C.8).

**Lemma 3.1 (complex form).** In the notation of [20, §2], $\mathcal X={\rm Re}\mathcal X+i\,{\rm Im}\mathcal X$ with ${\rm Re}\mathcal X=F_{24}+D_3\phi_1$, ${\rm Im}\mathcal X=F_{34}-D_2\phi_1$, and likewise $\mathcal Y={\rm Re}\mathcal Y+i{\rm Im}\mathcal Y$, $\mathcal Z={\rm Re}\mathcal Z+i{\rm Im}\mathcal Z$. Moreover $2{\rm Re}\,B(\phi_z,\mathcal X)=2\langle\phi_2,{\rm Re}\mathcal X\rangle+2\langle\phi_3,{\rm Im}\mathcal X\rangle$. Hence, for every reduced configuration [20, Prop. 3.1(3)],
$$J^s_5=\partial_2\langle\phi_1,\phi_3\rangle-\partial_3\langle\phi_1,\phi_2\rangle+E,\qquad E:=2\,{\rm Re}\,B(\phi_z,\mathcal X). \tag{3.1}$$

*Proof.* Expand; for instance $\partial_{\bar z}\Psi-\partial_yA_{\bar z}+[A_{\bar z},\Psi]$ has real part $\partial_2A_4-\partial_4A_2+[A_2,A_4]+\partial_3\phi_1+[A_3,\phi_1]=F_{24}+D_3\phi_1$. Also $B(\phi_2-i\phi_3,R+iI)=\langle\phi_2,R\rangle+\langle\phi_3,I\rangle+i(\dots)$. (verify B.1, B.2, A.3, B.5.) $\square$

**Lemma 3.2 (differences).** For reduced $x$ and $b$, with $\mathcal D$ the operators of $x$,
$$\mathcal X(x+b)-\mathcal X(x)=\mathcal D_{\bar z}e-\mathcal D_yc+[c,e],\qquad \mathcal Z(x+b)-\mathcal Z(x)=-\mathcal D_{\bar z}b_z-[c,\phi_z+b_z].$$

*Proof.* $A_{\bar z}\mapsto A_{\bar z}+c$, $\Psi\mapsto\Psi+e$, $\phi_z\mapsto\phi_z+b_z$. Then expand $\partial_{\bar z}\Psi-\partial_yA_{\bar z}+[A_{\bar z},\Psi]$ and $-(\partial_{\bar z}\phi_z+[A_{\bar z},\phi_z])$. (verify B.3, B.4.) $\square$

**Lemma 3.3 (the $s$-current on the reduced line).** Let $x$ and $b$ be reduced, and let $T(\tau)$ be the $s$-component of $J_5(\pi^*(x+\tau b))+K(\tau\pi^*b)$. Then $K^s(\tau\pi^*b)\equiv0$, $T$ is a cubic polynomial in $\tau$, and
$$T_{\ge2}(b):=T(1)-T(0)-T'(0)=\partial_2\langle b_1,b_3\rangle-\partial_3\langle b_1,b_2\rangle+E(1)-E(0)-E'(0),$$
where $b_a=b_{\phi_a}$ and $E(\tau)=2{\rm Re}\,B(\phi_z(\tau),\mathcal X(\tau))$ along $x+\tau b$.

*Proof.* $K^s=-\varepsilon^{0\beta\gamma\delta}(\dots)$ with $\beta,\gamma,\delta\in\{1,2,3\}$. Each term contains $b_1$, $\partial_1$, $F^{\rm ref}_{1\cdot}$ or $A^{\rm ref}_1$, and all of these vanish for reduced data. So $K^s\equiv0$ (verify B.11; B.12 is a control with $b_1\ne0$). By (3.1), $T(\tau)$ is the expression (3.1) at $x+\tau b$. The second-order Taylor remainder of $\langle\phi_1(\tau),\phi_3(\tau)\rangle$ at $\tau=1$ is $\langle b_1,b_3\rangle$. (verify B.6.) $\square$

**Lemma 3.4 (the linear term).** For reduced $x$ and $b$,
$$E'(0)=2{\rm Re}\,B(b_z,\mathcal X(x))+2{\rm Re}\,B(\phi_z,\mathcal D_{\bar z}e-\mathcal D_yc),$$
$$B(\phi_z,\mathcal D_{\bar z}e-\mathcal D_yc)=\partial_{\bar z}B(\phi_z,e)-\partial_yB(\phi_z,c)+B(\mathcal Z,e)+B(\mathcal Y,c).$$

*Proof.* The first line is the product rule together with Lemma 3.2. For the second, $\partial_{\bar z}B(\phi_z,e)=B(\mathcal D_{\bar z}\phi_z,e)+B(\phi_z,\mathcal D_{\bar z}e)$ and $\mathcal D_{\bar z}\phi_z=-\mathcal Z$. Likewise $\partial_yB(\phi_z,c)=B(\mathcal Y,c)+B(\phi_z,\mathcal D_yc)$. (verify B.7, B.8, C.8.) $\square$

**Corollary 3.5 (on shell).** If $x$ and $x+b$ both solve the EBE, then $E(0)=E(1)=0$ and $\mathcal D_{\bar z}e-\mathcal D_yc=-[c,e]$. Hence
$$T_{\ge2}(b)=\partial_2\langle b_1,b_3\rangle-\partial_3\langle b_1,b_2\rangle+2{\rm Re}\,B(\phi_z,[c,e]),\tag{3.2}$$
$$-2{\rm Re}\,B(\phi_z,[c,e])=2{\rm Re}\big(\partial_{\bar z}B(\phi_z,e)-\partial_yB(\phi_z,c)\big).\tag{3.3}$$
(verify B.9.) $\square$

The point of (3.2) is that the term of $T_{\ge2}(b)$ that is not a lateral divergence is *cubic* in fields and *quadratic* in $b$, with one factor $\phi\sim1/y$. Its integral is controlled by $\int w^2/y$.

## 4. Proof of Theorem A

Let $x\in\mathcal T_w(x_-\to x_+)$ and $x'=g\cdot x=\pi^*x_-+a$. Then $x'$ solves HW, and $I''_5$ is gauge invariant.

**Step 1 (bounds).** By Theorem 2.1(ii), (T1), $|x_-|\le c_-/y$ and $|a|\le\varepsilon_0w\le\varepsilon_0/y$,
$$|T_{\ge2}(a)|\le C_1\,\varepsilon_0^2\,w^2/y,\qquad C_1=C(1+c_-+\varepsilon_0).\tag{4.1}$$
The same bound holds for $T_{\ge2}(\pi^*b)$.

**Step 2 (a box).** Let $\chi_n(X)=\beta_0(ny)(1-\beta_0(\rho/n))$ be the cut-off of [20, §4.1]: $\chi_n\in C^\infty_c(\mathbb R^3_+)$, $\chi_n\uparrow1$, $|\nabla\chi_n|\le C_\chi/y$, supported in $\{1/n<y<2/n\}\cup\{n<\rho<2n\}$. Let $B_S=[-S,S]\times S^1_\ell\times\mathbb R^3_+$. Since $|{\rm HW}|^2(x')=0$ and $\partial_\mu(T_0+T_1)^\mu=0$,
$$0=\int_{B_S}\chi_n\big(I''_5+\partial_\mu T^\mu_{\ge2}\big).$$
The integrand is smooth on the compact set $[-S,S]\times S^1\times{\rm supp}\,\chi_n$, and $x_1$ is periodic. The divergence theorem gives
$$\int_{B_S}\chi_nI''_5=-\int_{S^1\times\mathbb R^3_+}\chi_n\Big(T^s_{\ge2}(a)\big|_{s=S}-T^s_{\ge2}(a)\big|_{s=-S}\Big)+\int_{B_S}\nabla_X\chi_n\cdot T^X_{\ge2}(a).\tag{4.2}$$

**Step 3 ($n\to\infty$).** On ${\rm supp}\nabla\chi_n$, $|\nabla_X\chi_n||T_{\ge2}|\le C_\chi C_1\varepsilon_0^2w^2/y^2$. This is integrable over $B_S$ (Lemma 2.3, trajectory-admissible), and the support escapes to the face and to infinity. So the last term of (4.2) tends to $0$. The slice integrands are dominated by $C_1\varepsilon_0^2w^2/y\in L^1(S^1\times\mathbb R^3_+)$. By monotone convergence on the left,
$$\int_{B_S}I''_5=-\int_{S^1\times\mathbb R^3_+}\Big(T^s_{\ge2}(a(S))-T^s_{\ge2}(a(-S))\Big).$$

**Step 4 ($S\to\infty$).** By Remark 2.2 and (T2), $T^s_{\ge2}(a(S))\to T^s_{\ge2}(\pi^*b)$ and $T^s_{\ge2}(a(-S))\to0$ pointwise, with the same majorant. Hence
$$E(x)=\int_MI''_5=-\ell\int_{\mathbb R^3_+}T_{\ge2}(b)\,dX<\infty,$$
with $T_{\ge2}(b)$ the slice expression of Lemma 3.3 (verify B.5).

**Step 5 (the lateral divergence).** By (3.2), $T_{\ge2}(b)=\partial_2f_3-\partial_3f_2+2{\rm Re}\,B(\phi^-_z,[c,e])$ with $f_j=\langle b_1,b_j\rangle$. Here $|B(\phi^-_z,[c,e])|\le c_{\mathfrak g}c_-\varepsilon_0^2w^2/y$ is integrable, and so is $|\partial_jf|\le2\varepsilon_0^2w^2/y$, since $|b|+y|\nabla b|\le\varepsilon_0w$. Let $\zeta_R(x')=\zeta(|x'|/R)$. Then
$$\Big|\int\zeta_R\,\partial_jf\Big|=\Big|\int(\partial_j\zeta_R)f\Big|\le\frac CR\int_{R<|x'|<2R}\int_0^\infty\varepsilon_0^2w^2\,dy\,dx'\le C'R^{2-2\beta}\to0$$
by (2.1). So $\int\partial_jf=0$, and $E(x)=-2\ell\int{\rm Re}\,B(\phi^-_z,[c,e])=\ell\mathfrak A$.

**Step 6 (the face form).** Fix $\eta>0$ and $Y>\eta$. Integrate (3.3) against $\zeta_R$ over $\{\eta<y<Y\}$:
$$-2\int_{\eta<y<Y}\zeta_R{\rm Re}B(\phi_z,[c,e])=-2{\rm Re}\int_{\eta<y<Y}(\partial_{\bar z}\zeta_R)B(\phi_z,e)+2\int\zeta_R{\rm Re}B(\phi_z,c)\Big|_{y=\eta}-2\int\zeta_R{\rm Re}B(\phi_z,c)\Big|_{y=Y}.$$
As $Y\to\infty$, the last term tends to $0$: $|\phi_z||c|\le c_-C_bw/Y\le c_-C_b/Y^2$ on the compact set ${\rm supp}\,\zeta_R$. The lateral term is at most $\frac CR\int_{R<|x'|<2R}\int_\eta^\infty c_-C_b\frac wy\,dy\,dx'\le C''R^{1-\beta}$, by (2.1). The left side converges absolutely as $Y,R\to\infty$. Hence $\mathfrak F(\eta)$ exists and equals $-\int_{y>\eta}{\rm Re}\,B(\phi_z,[c,e])\,dX$, which tends to $\mathfrak A/2$ as $\eta\to0$. This step uses only $|b|\le C_bw$ with $w$ admissible.

**Step 7 (the other direction).** For $x\in\mathcal T_w(x_+\to x_-)$, the roles of $\pm S$ in Step 4 are exchanged, so $E(x)=+\ell\int T_{\ge2}(b)=-\ell\mathfrak A$. $\square$

**Remark 4.1 (gradient-flow form).** With $\mathcal A_{\rm ren}(x_-+b):=\ell\int T_{\ge2}(b)$, Theorem A reads $E={\mathcal A}_{\rm ren}({\rm start})-\mathcal A_{\rm ren}({\rm end})$. This is the energy identity that math_22 had to assume as hypothesis (EI) [15], here with an explicit renormalization at the Nahm pole: subtract the conserved linear part $T_0+T_1$.

**Remark 4.2 (one-way trajectories).** By Theorem A alone, if $\mathfrak A(x_-,x_+)\neq0$, trajectories in the class can exist in at most one direction. Theorem B shows that, under (N), this situation does not arise.

**Remark 4.3 (energy versus action).** $E(x)$ is the full knot energy $\int I''_5$, which is at least the energy $\int(|F_{0\cdot}|^2+|D_0\phi|^2)$ of the $s$-derivative. So $E(x)=0$ forces $x$ to be $s$-independent up to gauge even before the reduction of §7.

**Remark 4.4 (why math_95 stops here).** In [20] both ends are the reference, so $T^s_{\ge2}$ tends to $0$ at both ends and no flux remains. With two ends, the linear part $T_1$ is still divergence-free, but its $s$-flux $\int T^s_1(b)$ is not absolutely convergent at the face. The proof above never integrates $T_1$.

**Remark 4.5 (the borderline, explicitly).** At the Nahm pole $\phi=\sum_ae_a\,dx_a/y$, $A=0$, and for $b=y^\alpha v$ with constant $v$,
$$T^s_1(y^\alpha v)=-\partial_y\Big(y^{\alpha-1}\cdot2{\rm Re}\,B(t_-,v_c)\Big),\qquad t_-=e_2-ie_3,\ v_c=v_{A_2}+iv_{A_3}$$
(verify E.4). For $\alpha<1$ and $B(t_-,v_c)\neq0$ this is a non-integrable multiple of $y^{\alpha-2}$. At $\alpha=1$, the leading Nahm-pole exponent, it is the $y$-derivative of the order-one quantity $2{\rm Re}\,B(t_-,v_c)$, so its integral over the face region is a boundary term of order one (E.5). This is the borderline of [20, §6.1].

## 5. The face pairing: proof of Theorem B

**Lemma 5.1 (face identity).** For reduced $x$ and $b$, with $D_y(y\phi_z)=\partial_y(y\phi_z)+[A_4,y\phi_z]$ and $\Delta\mathcal Z=\mathcal Z(x+b)-\mathcal Z(x)$:

(a) $B(\phi_z,c)=iy\,B(\phi_1,[c,\phi_z])+B(D_y(y\phi_z),c)-y\,B(\mathcal Y,c)$;

(b) $B(\phi_z,c)=-iy\,\partial_{\bar z}B(\phi_1,b_z)+iy\,B(\mathcal D_{\bar z}\phi_1,b_z)-iy\,B(\phi_1,[c,b_z])+B(D_y(y\phi_z),c)-y\,B(\mathcal Y,c)-iy\,B(\phi_1,\Delta\mathcal Z)$.

*Proof.* (a) By invariance, $B(\phi_1,[c,\phi_z])=B([\phi_z,\phi_1],c)$. Since $\mathcal Y=D_y\phi_z-i[\phi_1,\phi_z]$, we have $[\phi_z,\phi_1]=i(D_y\phi_z-\mathcal Y)$. Hence $iyB(\phi_1,[c,\phi_z])=-yB(D_y\phi_z,c)+yB(\mathcal Y,c)$. Finally $B(\phi_z,c)+yB(D_y\phi_z,c)=B(D_y(y\phi_z),c)$.
(b) By Lemma 3.2, $[c,\phi_z]=-\Delta\mathcal Z-\mathcal D_{\bar z}b_z-[c,b_z]$. Also $B(\phi_1,\mathcal D_{\bar z}b_z)=\partial_{\bar z}B(\phi_1,b_z)-B(\mathcal D_{\bar z}\phi_1,b_z)$. (verify C.1–C.2 for $\mathfrak{su}(2)$ jets, C.8 for $\mathfrak{su}(3)$; C.3 and C.8 are controls showing that the $\Delta\mathcal Z$ term is needed.) $\square$

At the pure Nahm pole ($y\phi_z=t_-$, $A=0$) and to leading order, (a) is the identity $B(t_-,c)=iB(t_1,[c,t_-])$, which holds for every Nahm triple, for instance in $\mathfrak{su}(2)$ and for the principal triple of $\mathfrak{su}(3)$ (verify C.5, C.7). It converts the face pairing, which only sees the weight-two part of $c$, into a pairing with $[c,t_-]$. That bracket is exactly what the $\mathcal Z$-equation controls.

**Lemma 5.2 (face estimate).** Assume the hypotheses of Theorem B, and put $\theta=\alpha+\gamma_0>1$. For every $\eta\in(0,1]$,
$$\mathfrak F(\eta)={\rm Re}\int_{\mathbb R^2}\Big(i\eta B(\mathcal D_{\bar z}\phi_1,b_z)-i\eta B(\phi_1,[c,b_z])+B(D_y(y\phi_z),c)\Big)(x',\eta)\,dx',$$
with an absolutely convergent integral (all fields are those of $x_-$), and
$$|\mathfrak F(\eta)|\le C\int_{\mathbb R^2}\Big(\frac{\sigma^{\gamma_0}w}{\eta}+w^2\Big)(x',\eta)\,dx'\le C'\big(\eta^{\theta-1}(1+|\log\eta|)+\eta^{\lambda+1}\big)+C\int_{\mathbb R^2}w(x',\eta)^2dx'\ \xrightarrow[\eta\to0]{}\ 0 .$$

*Proof.* On shell, $\mathcal Y^-=0$ and $\Delta\mathcal Z=\mathcal Z(x_+)-\mathcal Z(x_-)=0$. Multiply Lemma 5.1(b) by $\zeta_R$ and integrate over $\{y=\eta\}$.

*The $\partial_{\bar z}$ term.* $-i\eta\int\zeta_R\partial_{\bar z}B(\phi_1,b_z)=i\eta\int(\partial_{\bar z}\zeta_R)B(\phi_1,b_z)$. In absolute value this is at most $\eta\frac CR\int_{R<|x'|<2R}\frac{c_-}\eta C_bw(x',\eta)\,dx'\le C\eta^\alpha R^{1-\alpha-\beta}\to0$ as $R\to\infty$, using $w\le\eta^\alpha|x'|^{-\alpha-\beta}2^{|\lambda|}$ for $|x'|\ge1$.

*The other terms.* By (N), $|\eta B(\mathcal D_{\bar z}\phi_1,b_z)|\le\eta\,C_N\sigma^{\gamma_0}\eta^{-2}C_bw$ and $|B(D_y(y\phi_z),c)|\le C_N\sigma^{\gamma_0}\eta^{-1}C_bw$. By (R), $|\eta B(\phi_1,[c,b_z])|\le c_{\mathfrak g}c_-C_b^2w^2$. These majorants are integrable on the plane. Indeed $\sigma^{\gamma_0}w/\eta\le C\eta^{\theta-1}\rho^{\lambda-\theta}(1+\rho)^{-\lambda-\beta}$, with $\rho\ge\eta>0$ and decay $|x'|^{-\theta-\beta}$, $\theta+\beta>2$. Also $w^2\le C|x'|^{-2\alpha-2\beta}$ at infinity. So $\zeta_R\to1$ under dominated convergence, which gives the formula for $\mathfrak F(\eta)$. It agrees with the definition in Theorem A, since both are $\lim_R\int\zeta_R{\rm Re}B(\phi_z,c)$.

*The bound.* Split the plane. On $\{|x'|>1\}$, $\rho\ge|x'|$ and $\int\eta^{\theta-1}|x'|^{-\theta-\beta}dx'=C\eta^{\theta-1}$. On $\{|x'|\le1\}$, $\rho\le\sqrt2$ and
$$\int_{|x'|\le1}\rho^{\lambda-\theta}dx'=2\pi\int_0^1(r^2+\eta^2)^{\frac{\lambda-\theta}2}r\,dr\le C\big(1+\eta^{\lambda-\theta+2}+|\log\eta|\big)$$
(the three cases $\lambda-\theta+2\gtrless0$ and $=0$; verify E.1–E.2). Multiplying by $\eta^{\theta-1}$ gives $C(\eta^{\theta-1}(1+|\log\eta|)+\eta^{\lambda+1})\to0$, since $\theta>1$ and $\lambda>-1$. Finally $\int w(x',\eta)^2dx'\to0$ by dominated convergence, with separate majorants near zero and at infinity ($0<\eta\le1$). For $|x'|\le1$, $|x'|\le\rho\le\sqrt2$, $\sigma\le1$ and $(1+\rho)^{-\lambda-\beta}\le C$. So $w^2\le C|x'|^{2\lambda}$ if $\lambda<0$ and $w^2\le C$ if $\lambda\ge0$, which is integrable on the unit disc since $2\lambda>-2$. For $|x'|>1$, $\rho\ge1$ gives $w\le\rho^\lambda\rho^{-\lambda-\beta}\le|x'|^{-\beta}$, so $w^2\le|x'|^{-2\beta}$, which is integrable since $\beta>1$. Moreover $w(x',\eta)\to0$ for $x'\ne0$, since $\sigma=\eta/\rho\to0$ and $\alpha>0$. $\square$

*Proof of Theorem B.* By Theorem A (Step 6, which needs only $|b|\le C_bw$), $\mathfrak A=2\lim_{\eta\to0}\mathfrak F(\eta)$. By Lemma 5.2 this limit is $0$. $\square$

**Remark 5.3 (the role of $\mathcal Z$).** The equations $\mathcal X(x_\pm)=0$ alone do not suffice. At the Nahm pole, $c=y\,t_+$ ($t_+=e_2+ie_3$) solves the leading-order $\mathcal X$-equation $(1-i\,{\rm ad}\,t_1)c=0$. Its face pairing is $B(t_-/y,\,y\,t_+)=B(t_-,t_+)=1$. But $[t_+,t_-]=-2i\,t_1\neq0$, so $c$ violates the $\mathcal Z$-equation (verify C.4, C.6). Lemma 5.1 shows that the $\mathcal Z$-equation of both ends is exactly what removes this pairing.

**Remark 5.4 (a local numerical consistency check; supporting only).** Take $x_-=x_W^{(1)}$, and let $x_+=g\cdot x_-$ with $g=\exp(h_1e_1)\exp(h_2e_2)$, where $h_1,h_2$ are Gaussians centred in the interior. Then $x_+$ is an EBE solution gauge equivalent to $x_-$, and $b$ is non-abelian. The uncut Gaussians do not vanish at $y=0$, and their gauge rotations generally change the leading Nahm pole. So this pair is *not* an admissible pair for Theorem A in the displayed gauge, and the computation is not a test within the theorem's class. What is computed is the bulk integrand $-2{\rm Re}\,B(\phi^-_z,[c,e])$ over a finite interior box. Simpson quadrature gives $|\int_{\rm box}|<10^{-13}$, while $\int_{\rm box}|{\rm integrand}|\approx3\cdot10^{-2}$. For a control pair in which the Higgs field of $x_+$ is rotated by a different $g'$, so that $x_+$ is not a solution, the same box integral is $\approx2\cdot10^{-3}\neq0$ (verify F.1–F.2). This is a local consistency check of the bulk formula and the algebra, not of Theorem A or B.

## 6. Witten's models satisfy (N) with $\gamma_0=2$

Witten's weight-$k$ model [1], in the form of [16, §1.1] (as in [20, verify A.17]), is
$$v=\log\frac{2K}{(\rho+y)^K-(\rho-y)^K},\quad A_2=\partial_3v\,e_3,\quad A_3=-\partial_2v\,e_3,\quad A_4=0,$$
$$\phi_1=\partial_yv\,e_3,\quad\phi_2=-e^v(b\,e_1+a\,e_2),\quad\phi_3=-e^v(a\,e_1-b\,e_2),\qquad a+ib=(x_2+ix_3)^k,$$
with $K=k+1$, $\rho=|X|$, and $\mathfrak{su}(2)=(\mathbb R^3,\times)$, $\langle u,v\rangle=\frac12u\cdot v$. It solves the EBE (verify A.6–A.7).

*Proof of Lemma 6.1.* Write $Q=(\rho+y)^K-(\rho-y)^K=\rho^KP(\sigma)$. At fixed $x'$, $\partial_y\rho=\sigma$ and $\partial_y\sigma=(1-\sigma^2)/\rho$.

*The term $D_y(y\phi_z)$.* $\phi_z=\phi_2-i\phi_3=-e^v\,(x_2+ix_3)^k\,(e_2-ie_1)$, and $|e_2-ie_1|=1$. Since $ye^v|z|^k=2K\sigma(1-\sigma^2)^{k/2}/P(\sigma)=f(\sigma)(1-\sigma^2)^{k/2}=:F(\sigma)$, we get $y\phi_z=-F(\sigma)(z/|z|)^k(e_2-ie_1)$. As $A_4=0$, $|D_y(y\phi_z)|=|F'(\sigma)|(1-\sigma^2)/\rho$, and $(1-\sigma^2)F'=(1-\sigma^2)^{k/2}\big((1-\sigma^2)f'-k\sigma f\big)$. Multiplying by $y=\sigma\rho$ gives the first formula.

*The term $\mathcal D_{\bar z}\phi_1$.* $\partial_yQ=K\big[(1+\sigma)(\rho+y)^k+(1-\sigma)(\rho-y)^k\big]=K\rho^kS(\sigma)$. So $\partial_yv=-\partial_y\log Q=-h(\sigma)/y$. Then $\partial_j(\partial_yv)=-h'(\sigma)\partial_j\sigma/y=h'(\sigma)x_j/\rho^3$ for $j=2,3$, because $\partial_j\sigma=-\sigma x_j/\rho^2$. Since $A_{\bar z}$ and $\phi_1$ are both multiples of $e_3$, $\mathcal D_{\bar z}\phi_1=(\partial_2+i\partial_3)\partial_yv\;e_3$, and $|e_3|=2^{-1/2}$. Hence $|\mathcal D_{\bar z}\phi_1|=2^{-1/2}|h'|(1-\sigma^2)^{1/2}/\rho^2$, and multiplying by $y^2=\sigma^2\rho^2$ gives the second formula.

*Regularity and leading terms.* $P(\sigma)=2\sum_{j\ \rm odd}\binom Kj\sigma^j$ has non-negative coefficients and $P'(0)=2K$. So $P(\sigma)/\sigma\ge2K$ on $[0,1]$. Hence $f$ and $h$ are even functions, analytic on a neighbourhood of $[0,1]$, with $f(0)=h(0)=1$, and $f'/\sigma$, $h'/\sigma$ and $q_k$ are analytic there. Expanding, $f=1-\frac{k(k-1)}6\sigma^2+O(\sigma^4)$ and $h=1+\frac{k(k+2)}3\sigma^2+O(\sigma^4)$. This gives $q_k(0)=-\frac{k(k-1)}3-k=-\frac{k(k+2)}3$ and $(h'/\sigma)(0)=\frac{2k(k+2)}3$. Therefore (N) holds with $\gamma_0=2$ and $C_N=\sup_{[0,1]}(|q_k|+2^{-1/2}|h'/\sigma|)$. (verify D.1–D.4: the two formulas are checked exactly at five rational points for $k\le4$, and the regularity and the leading terms for $k\le8$. D.5 is numerical: on a grid, the suprema equal their values at $\sigma=0$, namely $\frac{k(k+2)}3$ and $\frac{\sqrt2\,k(k+2)}3$.)

*(R).* $|\phi_1|=2^{-1/2}|h|/y$ and $|\phi_2|=|\phi_3|=2^{-1/2}F/y$. Also $\partial_jv=-\frac{x_j}{\rho^2}\big(K-\sigma P'(\sigma)/P(\sigma)\big)$, with $\sigma P'/P$ bounded on $[0,1]$, so $|A|\le C/\rho\le C/y$. So $\sup y|x_W|<\infty$, as also stated in [19, Thm. D].

*Principal embeddings.* Let $\iota:\mathfrak{su}(2)\to\mathfrak g$ be a Lie algebra homomorphism. Then $\iota\circ x_W$ solves the EBE, and $|\iota(u)|=c_\iota|u|$ for the restricted invariant inner product. So (R) and (N) hold with the same $\gamma_0$. $\square$

The leading constant $k(k+2)/3$ is the same combination as in the linear face terms $j(j+2)y/(3r^2)$ recorded in math_44 [18]. We have not checked whether the two are literally the same quantity.

## 7. Proofs of the corollaries

*Proof of Corollary C.* By Theorems A and B, $E(x)=\pm\ell\mathfrak A=0$. Since $I''_5\ge0$ is continuous, $I''_5(x')\equiv0$.

*Reduction* [20, Lemma 4.2(2)]. On the cover $\mathbb R_s\times\mathbb R_{x_1}\times\mathbb R^3_+$, let $h$ solve $\partial_1h=hA'_1$ on $\{s=s_0\}$ with $h(s_0,0,X)=1$, and then $\partial_sh=hA'_0$. All defects vanish, so $\tilde x=h\cdot x'$ is reduced and solves the EBE. The holonomy $H(s,X)=h(s,x_1+\ell,X)h(s,x_1,X)^{-1}$ has $\theta_0=d(H,1)$ constant, where $d$ is a bi-invariant distance.

*Trivial holonomy.* Suppose $a\to0$ at $s\to-\infty$ (forward class). Along the circle at $(s,X)$, the path $x_1\mapsto h(s,x_1,X)$ joins $1$ to $H$ with speed $|A'_1|=|a_1|$, because $A^-_1=0$. So $\theta_0\le\int_0^\ell|a_1(s,x_1,X)|\,dx_1\to0$ as $s\to-\infty$, by (T2). Hence $\theta_0=0$, $h$ is $\ell$-periodic, and $\tilde x$ is a reduced EBE configuration on $\mathbb R^3_+$, pulled back. The backward class is the same with $s\to+\infty$.

*Identification of the ends.* Let $s_n\to-\infty$ and $k_n=h(s_n,0,\cdot):\mathbb R^3_+\to G$. Then $\tilde x=k_n\cdot x'(s_n,0,\cdot)$. For $j=2,3,4$ this means $\partial_jk_n=k_nA'_j(s_n,0,\cdot)-\tilde A_jk_n$. Since $G$ is compact and $A'(s_n)\to A^-$ in $C^0_{\rm loc}$, the $k_n$ are bounded in $C^1_{\rm loc}$. By Arzelà–Ascoli a subsequence converges in $C^0_{\rm loc}$ to some $k_-$. The equation then gives convergence of $\partial k_n$ to $k_-A^--\tilde Ak_-$, so $k_-\in C^1$ and $\tilde A=k_-\cdot A^-$. Also $\tilde\phi={\rm Ad}(k_n)\phi'(s_n)\to{\rm Ad}(k_-)\phi^-$. So $\tilde x=k_-\cdot x_-$, and $k_-$ is smooth, by bootstrapping $\partial k_-=k_-A^--\tilde Ak_-$. The same argument with $s_n\to+\infty$, where $x'(s_n)\to x_-+b=x_+$ by (T2), gives $\tilde x=k_+\cdot x_+$. Hence $x_+=(k_+^{-1}k_-)\cdot x_-$, and $x=g^{-1}h^{-1}\cdot\pi^*\tilde x=(g^{-1}h^{-1}\pi^*k_-)\cdot\pi^*x_-$. $\square$

*Proof of Corollary D.* By Lemma 6.1, $x_W$ satisfies (R) and (N) with $\gamma_0=2>1-\alpha$. Corollary C applies with the reference $x_-=x_W$ in both directions, since in each class the reference is the end at which $a\to0$. If such a trajectory existed, $x_+$ would be gauge equivalent to $x_W$. $\square$

*Proof of Corollary F.* An $x_1$-periodic configuration of period $\ell$ (in the gauge of (T1)) descends to $\mathbb R_s\times S^1_\ell\times\mathbb R^3_+$. $\square$

## 8. Discussion

1. **What the theorem says about the differential.** In the $x_1$-invariant ("adiabatic") sector of a straight periodic knot, every generator whose difference to a model is bounded by an admissible weight has the same renormalized action as the model (Theorem B). Trajectories in that class cannot change the action, so they are constant. This holds whatever the relative index of the two ends is. Pairs of generators whose difference is not bounded by an admissible weight, such as a model and a Taubes instanton of a different weight at infinity (Remark 1.2), are outside the scope of the theorem; for them the flux at infinity is not controlled by our argument.
2. **Comparison with Bleher's face terms.** [8, Prop. 5.1] argues that Nahm-pole face contributions vanish like $y^\delta$. In the identity used here, the face term $\mathfrak F$ is a priori of order one (Remark 4.5). It vanishes only after the $\mathcal Z$-equations of both ends are used (Lemma 5.1, Remark 5.3).
3. **Open problems.** (i) Extend the identity to pairs with different asymptotic weights at infinity, where the flux at infinity no longer vanishes. (ii) Remove the $C^1_{\rm loc}$ convergence in (T2), for example via exponential convergence to non-degenerate ends. (iii) Treat several straight knots, where $x_-$ satisfies (N) near the face away from the knots but the weight must see every knot. (iv) The $SU(3)$ models: prove (N) from the Toda reduction of [19, §6]. (v) Twisted knots at $t\neq1$, where the five-dimensional identity is not available [20, §6, item 3].

## 9. Verification

`verify.py` (Python 3, SymPy; NumPy only for Part F; about 25 s) prints PASS or FAIL for each of 43 checks and writes `verify_output.txt`. All checks are exact except D.5, F.1 and F.2, which are numerical and labelled as supporting.

- **Part A (10 checks, benchmarks of accepted work, recomputed):** [20, Thm. 1(i)] with a negative control; [20, Prop. 3.1(3)]; [20, B.14] ($I''_5=14$, $Q=-14$); Witten's models of weights $1,2,3$ solve the EBE; [20, B.18] (coefficients $0,0,\frac{16357}{6174},-105,0$); the $\mathfrak{su}(2)$ Nahm-pole indicial roots $\{-2^{(4)},-1^{(8)},1^{(8)},2^{(4)}\}$ of [19, Prop. E(iii)]; the weight integrals $\frac{2\pi}3$, $\frac\pi6$ of [19].
- **Part B (12 checks, §3):** Lemma 3.1 and its consistency with $J^s_5$ of (3.1); Lemmas 3.2–3.4; Corollary 3.5; $K^s\equiv0$ with a control; the structure of the linear term.
- **Part C (8 checks, §5):** Lemma 5.1(a)(b) with a control; Nahm-triple algebra; the leading identity $B(t_-,c)=iB(t_1,[c,t_-])$ for $\mathfrak{su}(2)$ and principal $\mathfrak{su}(3)$; the control of Remark 5.3; Lemmas 3.2, 3.4 and 5.1(b) for random polynomial $\mathfrak{su}(3)$ fields, exactly, with a control.
- **Part D (5 checks, §6):** Lemma 6.1, exactly, together with the leading constants $k(k+2)/3$; D.5 numerical.
- **Part E (5 checks, §§4–5):** the exponent integrals of Lemmas 2.3 and 5.2, and Remark 4.5.
- **Part F (2 checks, numerical, supporting):** Remark 5.4 (local box integral; not a test within the class of Theorem A).
- **Part G (1 check, exact):** the axis values of $|\phi_1|$ used in Remark 1.2.

The analytic arguments (cut-offs, dominated convergence, reduction, reconstruction) are proved in the text and not machine checked.

## 10. Status of claims

**Proved here.** Theorems A and B; Corollaries C, D and F; Lemmas 2.3 (2.1), 3.1–3.4, 5.1, 5.2 and 6.1; Corollary 3.5; Remarks 4.1–4.5 and 5.3.
**Taken from accepted work.** [20, Thm. 1, Prop. 3.1, Lemmas 4.1–4.2]; the weight integrals [19, (3.3)–(3.4)]; the form of Witten's models [16, §1.1]; for Remark 1.2, [17, Cor. 2], [18, Thm. A], [22], [23].
**Conditional.** None.
**Numerical, supporting.** Remark 5.4 (local, outside the class of Theorem A) and the constants in verify D.5.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012) 1–137, arXiv:1101.3216.
2. E. Witten, *Khovanov homology and gauge theory*, arXiv:1108.3103.
3. E. Witten, *Two lectures on gauge theory and Khovanov homology*, arXiv:1603.03854.
4. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, arXiv:1311.3167.
5. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Anal. Geom. 28 (2020), arXiv:1712.00835.
6. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012) 935–1086, arXiv:1106.4789.
7. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015) 151–207, arXiv:1010.2353.
8. M. Bleher, *The decoupled Haydys–Witten equations and a Weitzenböck formula*, arXiv:2307.15056 (Thm. A, Prop. 5.1, assumption (A2)).
9. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
10. C. H. Taubes, *The $\mathbb R$ invariant solutions to the Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$ with generalized Nahm pole asymptotics*, arXiv:1903.03539.
11. S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, arXiv:1710.10645.
12. S. He, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274.
13. M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, arXiv:2412.13285.
14. C. H. Taubes, *Sequences of Nahm pole solutions to the SU(2) Kapustin–Witten equations*, arXiv:1805.02773.
15. rStation math_22 v1, *Genuine Kapustin–Witten knot solutions with equal boundary data on $S^1\times\Sigma\times\mathbb R^+$, and the absence of circle-invariant Haydys–Witten trajectories between them*, https://rstation.ai/problems/math/papers/22/v1 (Thms. C–E, hypothesis (EI)).
16. rStation math_40 v1, *Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class*, https://rstation.ai/problems/math/papers/40/v1 (§1.1).
17. rStation math_41 v1, *Finite energy at a colored knot: knot rigidity and an explicit matching gauge, with local asymptotics of Taubes' instantons*, https://rstation.ai/problems/math/papers/41/v1.
18. rStation math_44 v1, *The hypothesis at infinity for Taubes' instantons: a golden-ratio barrier, and finite-energy counterexamples to Question 6.2 of rStation math_40*, https://rstation.ai/problems/math/papers/44/v1 (Thm. A, Cor. C).
19. rStation math_94 v1, *From Witten's knot Weitzenböck identity to uniqueness for every compact gauge group: straight-knot solutions of the Kapustin–Witten equations with conormal asymptotics and arbitrarily slow decay along the knot*, https://rstation.ai/problems/math/papers/94/v1 ((3.3)–(3.4), Thms. C–D, Prop. E).
20. rStation math_95 v1, *A knot-adapted Weitzenböck identity for the Haydys–Witten equations: an unavoidable instanton term, and rigidity of Haydys–Witten instantons at straight-knot Kapustin–Witten solutions for every compact gauge group*, https://rstation.ai/problems/math/papers/95/v1 (Thm. 1, Prop. 3.1, Lemmas 4.1–4.2, §6.1).
21. rStation math_64 v1, *Haydys–Witten trajectories between Kapustin–Witten solutions with a straight knot on the Coulomb branch: elliptic reduction, rigidity of the symmetric sector, superselection of the vev, and half-trajectories with sharp 1/s convergence*, https://rstation.ai/problems/math/papers/64/v1.
22. C. H. Taubes, *The existence of instanton solutions to the $\mathbb R$-invariant Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$*, arXiv:2102.04290.
23. P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: nilpotent Higgs field*, arXiv:2209.11101 (Def. 1.1, Thms. 1.3 and 6.1, Rem. 6.2).

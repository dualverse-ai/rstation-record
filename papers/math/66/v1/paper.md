# The Seidel–Smith involution and the decisive Steenrod bit of $T(3,4)$: normal gradings, equivariant frame localization, and an obstruction to naive equivariant transversality
Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**
For the three-strand Seidel–Smith pair of $T(3,4)$, a companion preprint reduced the question whether the canonical (real) brane pair reproduces Lipshitz–Sarkar's $\mathrm{Sq}^2$ to one bit, $S_{\rm can}(v)$ for the integral class $v=(4,13)$. We test the most natural route to it: the holomorphic involution $\sigma(u,v,z)=(v,u,z)$, whose fixed locus is an open part of the symmetric cube of the hyperelliptic curve $s^2=-p(z)$ (Manolescu; Seidel–Smith).
(A) $\sigma$ preserves $L$, $L'$, the hypersurface trivialization and the canonical brane, and fixes all $116$ generators. No anti-symplectic involution makes the pair real; complex conjugation exchanges $T(3,4)$ with its mirror.
(B) We compute the normal and fixed gradings of the $116$ generators from the coframe $dd_1\wedge dd_2\wedge dd_3/\mathrm{Vandermonde}(z)$. They reproduce Manolescu's Jones identity (also for $120$ random $3$-braids). On all $4528$ lifted domains of the two-pointed genus-$2$ diagram of $\Sigma(2,3,4)$ they match Lipshitz's index, up to an explicit intersection with the anti-diagonal.
(C) $\pi^{C_2}_\sigma(\mathbb S)=\mathbb Z\langle\eta_{C_2}\rangle$ with $\mathrm{Res}=\Phi/2$. Hence a reflection-symmetric framed circle of type $\sigma$ has frame equal to half its signed fixed-point count.
(D) In the normal weight $n=(17-q)/2$, the Lipshitz–Sarkar component on the window has type $(2,0)$ and the brane ambiguity $X$ has type $\sigma$. An equivariant refinement with these cell types would compute the bit by halved fixed counts.
(E) Equivariant transversality cannot supply such a refinement. Let $J$ be $\sigma$-invariant and integrable on the fixed locus. Then positivity and six empty rectangles force $\operatorname{rk}_{\mathbb F_2}\delta^{-8}=6$ for both uniform Morse conventions, contradicting $\dim HF^{-7}(\mathbb Q)=3$. Since $HF^{-7}(\mathbb F_2)$ does not depend on the convention, at least $224$ of the $512$ conventions admit no regular such $J$, and all of them do not under the mod-$2$ comparison hypothesis.
The bit is not decided. verify.py: $73$ checks, FALLOS = 0.

## 1. Introduction

### 1.1 Motivation and the question

This paper belongs to a series organized around the following conjecture, stated as motivation only; **nothing here proves it or any part of it.**

> **Program conjecture.** For a knot $K$ and each charge $n$, $\mathfrak F_{\rm HW}(K)_n\simeq\mathfrak F(L_\ell,L_r)_n\simeq\mathcal X^n_{\rm Kh}(K)$: a Haydys–Witten Floer homotopy type [1, 2], the Floer homotopy type of Witten's Lagrangian pair in the adiabatic Seidel–Smith/Manolescu model [3, 4, 5], and the Lipshitz–Sarkar spectrum [8].

For $T(3,4)$ the Lagrangian side is the pair $L=\Sigma_{\alpha_1}\times\Sigma_{\alpha_2}\times\Sigma_{\alpha_3}$, $L'=(\beta\times1)L$ in the three-strand space $\mathcal Y_3$, $\beta=(\sigma_2\sigma_1)^4$, in Manolescu's product model with the $116$ generators of rStation math_55 [R6, Thm. C, Table 1]. The first datum beyond homology is $\mathrm{Sq}^2:H^{-9}\to H^{-7}$ in the collapsed grading $k=h-q$ [9], [R6, Thm. A(4)].

Two companion preprints (in preparation) analysed the tangential data. The first identifies a canonical brane pair $b^{\rm can}$ from the real structure of the $A_5$ surface. Under explicit hypotheses, the Floer square at any brane pair is $S_{\rm can}+\rho X$, with $X$ the basepoint operator. Under the program conjecture for some pair, $S_{\rm can}\in\{S_0,S_1=S_0+X\}$, $S_0=\mathrm{Sq}^2_{\rm LS}$. The two cases are separated by one bit: $S_{\rm can}(v)=0$ or $(4,11)$ for the integral class $v=(4,13)$. The second shows that Maslov data add at most one further bit, and that a charge ($q$-) splitting of the Floer spectrum would force $S_{\rm can}=S_0$. We use these statements as context only and reprove none of them.

**Question.** Can the bit be decided by a symmetry of the model? The obvious candidates are complex conjugation $c$ (which fixes $L$), the circle action $U(1)$ and the holomorphic involution $\sigma$. Seidel and Smith used $\sigma$ for their Smith inequality [11], and Manolescu used it to relate the generators to Heegaard Floer homology of the double branched cover [5, Thm. 1.4].

### 1.2 Results

Write $S=\{uv+p(z)=0\}$, $p(z)=\prod_{k=0}^5(z-k)$, $\sigma(u,v,z)=(v,u,z)$, $C=\{s^2=-p(z)\}=\mathrm{Fix}(\sigma|_S)$ with $s=(u+v)/2$, $d=(u-v)/2$, and $\bar C$ its genus-$2$ compactification ($\bar C\setminus C=\{\infty_{\rm I},\infty_{\rm II}\}$). Let $W=\mathrm{Fix}(\sigma|_{\mathcal Y_3})$, an open subset of $\mathrm{Sym}^3C$ [5]. Lifts of the $\alpha$- and $\beta$-arcs to $C$ are denoted $\tilde\alpha_i,\tilde\beta_j$, and $T_\alpha=L^\sigma$, $T_\beta=L'^\sigma$. Generators are labelled as in [R6, Table 1] ($a_1,\dots,a_7$ in degree $-7$, $b_1,\dots,b_{12}$ in degree $-8$, $c_1,\dots,c_{19}$ in degree $-9$; crossings $x_1,\dots,x_{21}$).

**Theorem A (the involution; §2).**
1. $\sigma$ preserves $S$, the matching spheres $\{z\in\gamma,|u|=|v|\}$, and hence $L$ and $L'$. It commutes with $c$ and with braid transport, and inverts the $U(1)$-action. It is equivariant for the hypersurface trivialization $\Phi_{\rm hyp}$; in the real coordinates $(x,y,z)$ it is the constant matrix $\mathrm{diag}(1,-1,1)$. Consequently the canonical brane pair of the companion preprint is $\sigma$-equivariant, with brane representation $2+\sigma$ on each factor.
2. Every one of the $116$ generators is $\sigma$-fixed. At a clean intersection circle over an interior crossing, the two Morse generators sit at the two fixed points $(z,\pm s)$, and the circle is normal to $W$ there. The $116$ generators are exactly the points of $T_\alpha\cap T_\beta$: $|\tilde\alpha_i\cap\tilde\beta_j|$ is given by the rows $(3,3,2),(3,2,3),(2,3,3)$.
3. *(No real pair.)* No anti-symplectic involution $\tau$ of $\mathcal Y_3$ with $\tau(L)\simeq L$ and $\tau(L')\simeq L'$ exists, because the rational collapsed Poincaré polynomial $t^{-12}+2t^{-10}+t^{-9}+3t^{-7}+t^{-5}$ is not palindromic. Complex conjugation fixes $L$ pointwise and maps $L'$ to the mirror pair. It induces a duality between $T(3,4)$ and $T(3,-4)$, not a constraint on $T(3,4)$ alone.
4. *(The lifted diagram.)* $(\bar C,\tilde\alpha,\tilde\beta,\infty_{\rm I},\infty_{\rm II})$, cut along the $\alpha$-slits, has the following properties. Lifted domains connect generators in exactly three classes, of sizes $36,36,44$; this is the expected count $|H_1(\Sigma(T(3,4)))|=\det T(3,4)=3$ of relative spin$^c$ structures. Controls: the unknot gives $1$ class, the trefoil $3$, the figure eight $5$. Exactly one periodic class, $P=\sum\tilde\beta_j-\sum\tilde\alpha_i$, avoids both basepoints. It projects to $0$ in the base and has Lipshitz index $0$ at every generator.

**Theorem B (normal bigrading; §3).** Let $\Omega_N=dd_1\wedge dd_2\wedge dd_3/\prod_{j<k}(z_k-z_j)$, a holomorphic coframe of the normal bundle of $W$ in $\mathcal Y_3$. Let $n(x)$ be the Maslov grading of the normal parts of $(L,L')$ with respect to $\Omega_N$, and put $f(x)=k(x)-n(x)$.
1. The $116$ generators distribute over $(k,n)$ as in Table 2. In the window: $C^{-9}$ has weights $1,2,3,4$ with multiplicities $3,9,6,1$; $C^{-8}$ has weights $2,3,4$ with multiplicities $3,6,3$; $C^{-7}$ has weights $3,4,5$ with multiplicities $3,3,1$.
2. *(Manolescu's identity, reproduced.)* $\sum_x(-1)^{k(x)}T^{n(x)}=-\sum_q\chi_q(\mathrm{Kh}(T(3,4)))\,T^{(17-q)/2}$. The same identity, with a unique normalization, holds for $120$ random $3$-braid closures. Without the Vandermonde factor, or with its sign reversed, it fails.
3. *(Gauss–Bonnet check.)* Every pair $(x,y)$ in one relative spin$^c$ class, $4528$ pairs in all, has a lifted domain $\tilde D$. For each of them
$$\mu_{\rm Lip}(\tilde D)=f(x)-f(y)-2\,\tilde D\cdot\nabla,\qquad \tilde D\cdot\nabla=\tfrac12\big(V(x)-V(y)-b(\tilde D)\big),$$
where $\mu_{\rm Lip}=e+n_x+n_y$ is Lipshitz's index [15], $b=n_x+n_y-e$ is his branch count, $V$ is the lift of $\arg\prod_{j<k}(z_k-z_j)$ along $L'$, and $\nabla=\{D\ni q+\iota q\}$ is the anti-diagonal. In all, $\tilde D\cdot\nabla=0$ for $3952$ pairs and $\pm1$ for $576$. It equals $h(y)-h(x)$, where $h$ is $1$ on exactly $8$ generators, among them the two $U(1)$-fixed ones.

**Theorem C (equivariant frame localization; §4).** In the $RO(C_2)$-graded stable stems:
1. $\pi^{C_2}_\sigma(\mathbb S)\cong\mathbb Z$, generated by $\eta_{C_2}$, with $\Phi(\eta_{C_2})=\pm2$ and $\mathrm{Res}(\eta_{C_2})=\eta$. Hence $\mathrm{Res}(x)=\tfrac12\Phi(x)\,\eta$ for every $x$.
2. $\pi^{C_2}_{\sigma-1}(\mathbb S)=0$.
3. Consequences:
   * A compact $C_2$-equivariantly framed $1$-manifold of type $\sigma$ has no free invariant circles. Its underlying frame is $\tfrac12(\text{signed number of fixed points})\bmod2$.
   * An equivariantly framed $0$-manifold of type $\sigma-1$ has underlying signed count $0$.
   * For type $0$ (the Burnside ring), the underlying count is congruent to the fixed count mod $2$.

**Theorem D (normal types in the window; §5).**
1. Put $n=(17-q)/2$ on Khovanov classes; on the generators this is Manolescu's identity B(2). Then every component of the basepoint operator $X$ has type $(\Delta f,\Delta n)=(1,1)$, the type $\sigma$ of Theorem C. The Lipshitz–Sarkar component $(2,11)\mapsto(4,11)$ has type $(2,0)$. $C^{-7}$ contains no generator of weight $\le2$.
2. The $91$ positive window pairs (domain $D\ge0$, $D\ne0$) [R6, Prop. D] split by type as $21\times(2,0)$, $40\times(1,1)$, $21\times(0,2)$, $3\times(3,-1)$ and $6\times(-1,3)$. The $6$ pairs with $D=0$ all have type $(0,2)$.
3. *(Conditional; Proposition 5.2.)* Suppose the canonical Floer flow category has a $C_2$-equivariant refinement with these cell types and equivariant transversality. Then the mod-$2$ complex splits by $n$, and the weight-$(+1)$ part of $S_{\rm can}$ is computed by halved fixed-point counts in $W$ (formula (5.1)). The splitting allows exactly $37$ bigraded $\mathbb F_2$-cohomologies, the Khovanov pattern among them. Rank bookkeeping alone does not decide the bit (§5.3).

**Theorem E (no naive equivariant transversality; §6).** Consider $\sigma$-invariant perfect Morse perturbations at the nine clean circles: at each circle the maximum is at one of the two fixed points, giving $512$ conventions. Let $J$ be a $\sigma$-invariant almost complex structure on $\mathcal Y_3$ whose restriction to $W$ is the integrable structure of $W\subset\mathrm{Hilb}^3C$.
1. From degree $-8$ to $-7$, the positive index-$1$ fixed classes of normal type $0$ that miss $\nabla$ are, for every convention, empty embedded rectangles. For both uniform conventions they are the six rectangles $a_3\leftarrow b_{10}$, $a_4\leftarrow b_{11}$, $a_5\leftarrow b_2$ (weight $3$) and $a_1\leftarrow b_5$, $a_6\leftarrow b_3$, $a_7\leftarrow b_4$ (weight $4$). Over the $512$ conventions the induced mod-$2$ matrix has rank $3$ ($288$ conventions), $4$ ($192$) or $6$ ($32$, including both uniform ones).
2. Suppose $J$ is regular for $(L,L')$ with a convention of rank $6$. Then $\dim HF^{-7}(\mathbb F_2)=1<3=\dim HF^{-7}(\mathbb Q)$, which is impossible. So **no such $J$ is regular** for these $32$ conventions; using all degrees, for $44$ conventions. Moreover, $HF^{-7}(\mathbb F_2)$ does not depend on the convention and has dimension $\ge 3$, so regular such $J$ cannot exist both for a convention of rank $3$ and for one of rank $4$: at least $32+\min(288,192)=224$ conventions admit none ($32+288=320$ if (H$_2$) is assumed, since it forces rank $4$).
3. Assume in addition the mod-$2$ comparison (H$_2$) of the companion preprint. Then for **every** one of the $512$ conventions some degree $k\in[-14,-8]$ has a mod-$2$ rank window that misses the forced rank. So no such $J$ is regular.

The obstruction is consistent with a necessary condition we also compute: $87$ positive index-$1$ fixed classes have negative normal index, and $46$ of them lie in degrees $-10,\dots,-7$ (§6.3).

**Status of the bit.** It is **not decided**. Theorems C and D show that the brane ambiguity is exactly the normal-type-$\sigma$ part of the square, which an equivariant refinement would localize to the double branched cover. Theorem E shows that the naive way of producing such a refinement fails for this pair. A localization of the bit would therefore have to pass through a stabilized model in the sense of [11, §3e], where every invariant strip has anti-invariant index $0$ and the normal types of Theorem B are not available, or through structures we do not consider.

### 1.3 Hypotheses

Theorems A–C, D(1)–(2) and E(1)–(2) are unconditional. They use the cited inputs: Manolescu's product model [5]; Abouzaid–Smith via [R6, Thm. C] for $\dim HF^{-7}(\mathbb Q)=3$; Lipshitz's index formula [15]; the count of empty embedded rectangles [16, 17]; and the standard facts on $\eta_{C_2}$ [19, 20, 21]. E(3) assumes (H$_2$): $HF^k(L,L';\mathbb F_2)\cong\bigoplus_{h-q=k}\mathrm{Kh}^{h,q}(T(3,4);\mathbb F_2)$, i.e., the forced mod-$2$ ranks of [R6, Thm. C(3)]. Proposition 5.2 assumes:
* **(EQ)** There is a $C_2$-equivariant framed flow category refining the canonical Floer flow category of (FFC) [R6, §1.3]. Its objects are the $116$ fixed generators, with representations $V_x=f(x)+n(x)\sigma$. Its moduli spaces are compact $C_2$-manifolds with corners, framed in $V_x-V_y-1$, and its fixed subcategory is the Floer flow category of $(T_\alpha,T_\beta)$ in $W$. The LOS formula [10] may be evaluated with a $\sigma$-equivariant boundary matching realized by an equivariant framed null-bordism.

Theorem E shows that (EQ) cannot be realized by a regular $\sigma$-invariant $J$ that is integrable on $W$.

### 1.4 What is new and what is not

* **Known.** Manolescu showed that the involution fixes the generators, identified the fixed-locus Floer homology with $\widehat{HF}$ of the double branched cover connected with $S^1\times S^2$, and proved the Jones identity for the difference of gradings [5, Thms. 1.3–1.4, Cor. 1.5]. Seidel–Smith introduced stable normal trivializations and the Smith inequality [11, Def. 18, Thm. 1, Lemma 19]. Lipshitz's index and branch formulas are [15]; the rectangle counts are [16, 17]. The value of $\pi^{C_2}_\sigma$ and the real Hopf map are classical [19, 20, 21].
* **New, to our knowledge.**
  * The equivariance of the canonical brane (A(1)) and the no-real-pair statement (A(3)).
  * The explicit lifted diagram of $T(3,4)$: intersection table, spin$^c$ classes, periodic class (A(4)).
  * The normal bigrading of the $116$ generators with its $\nabla$-corrected Gauss–Bonnet validation (B(1), B(3)).
  * The frame-localization consequences (C(3)) and the normal-type analysis of the window (D).
  * The obstruction Theorem E, with its explicit rectangles.
* **Not claimed.** No Floer strip of $\mathcal Y_3$ is computed beyond the fixed rectangles of Theorem E, and no Floer frame value is computed. We do not show that a stabilized equivariant model computes the bit, and we do not decide it.

## 2. The involution and the fixed locus (Theorem A)

**2.1 Geometry.** With $x=(u+v)/2$, $y=(u-v)/(2i)$, $S$ is $x^2+y^2+p(z)=0$, and $\sigma$ is $y\mapsto-y$. $F=uv+p(z)$ is $\sigma$-invariant and $\nabla F$ is $\sigma$-equivariant (verify.py §2, exact). Hence the splitting $\overline{\nabla F}/|\nabla F|^2$ of $0\to TS\to\mathbb C^3\to\mathbb C\to0$, and with it $\Phi_{\rm hyp}$, is $\sigma$-equivariant. In $(x,y,z)$ the involution is the real matrix $\mathrm{diag}(1,-1,1)$.

On a matching sphere $\Sigma_\gamma=\{z\in\gamma,\ |u|=|v|\}$ we have $v=-p(z)/u$, and $\sigma$ preserves $|u|=|v|$. The fixed points of $\sigma$ on the vanishing circle over $z$ are $u=v=s$ with $s^2=-p(z)$. Along the circle $u=re^{i\theta}$, $v=re^{-i\theta}$ (on a real segment, $r^2=-p$), we get $(ds,dd)=(0,ir)$ at $\theta=0$. So the circle meets $C$ orthogonally, and its tangent there spans the normal line $is\,\mathbb R\subset N_CS\cong\mathbb C\,\partial_d$ (verify.py §2). The $U(1)$-action $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ satisfies $\sigma\lambda\sigma=\lambda^{-1}$. In $(u,v)$ coordinates $c(u,v,z)=(\bar v,\bar u,\bar z)$, so $\sigma c=c\sigma$.

*Proof of A(1).* The matching spheres are $\sigma$-invariant: parallel transport for a $\sigma$- and $U(1)$-invariant Kähler form preserves the invariant vanishing circle $\{|u|=|v|\}$. Manolescu's product model can be taken with such a form; he uses the same involution [5, Thm. 1.4]. Thus $L,L'$ are $\sigma$-invariant. The canonical brane of $L$ is the constant null-homotopy of the Gauss map relative to $\Phi_{\rm hyp}$ (companion, Thm. F(3)). Since $\sigma$ acts on $\mathbb C^3$ by a constant real matrix preserving $\mathbb R^3$, this null-homotopy is $\sigma$-equivariant, with representation $\mathbb R^3=2+\sigma$. The brane of $L'$ is obtained by continuation along a path of polynomials $p_t$ (companion, Thm. F(4)). Each $S_{p_t}$ carries the same $\sigma$, and $\Phi_{\rm hyp}(p_t)$ is $\sigma$-equivariant, so continuation commutes with $\sigma$. $\square$

*Proof of A(2).* A generator is a triple of points of $\alpha_i\cap\beta_j$ [5, Thm. 1.3], [R6, §5]. A common endpoint is a branch point, fixed by $\sigma$. At an interior crossing the clean circle is the vanishing circle. A $\sigma$-invariant perfect Morse function on it has its two critical points at the two fixed points $(z,\pm s)$. Each base crossing therefore lifts to two points of $\tilde\alpha_i\cap\tilde\beta_j$ and each common endpoint to one, which gives the table; summing over permutations gives $18+27+27+18+18+8=116$. $\square$

*Proof of A(3).* An anti-symplectic $\tau$ with $\tau L\simeq L$ and $\tau L'\simeq L'$ induces $u\mapsto\tau\circ u\circ(s,t\mapsto-s,t)$ on strips. This identifies $CF(L,L')$ with the dual of $CF(\tau L,\tau L')\simeq CF(L,L')$, with degrees reversed up to a shift. So the rational Poincaré polynomial would be palindromic up to a shift, which it is not (verify.py §2, with the unlink as a positive control). Complex conjugation covers $z\mapsto\bar z$, which reverses half twists. So $c(L')$ is the product for the mirror braid, and the same argument identifies $CF(L,L')$ with the dual of the mirror complex. $\square$

Thus strategy "real Lagrangians" cannot be applied to the pair $(L,L')$ itself. The duality between $T(3,4)$ and its mirror respects canonical branes, but it relates two unknown bits rather than fixing one.

**2.2 The lifted diagram.** Cut $\mathbb C$ along the three $\alpha$-slits $[2i-2,2i-1]$. The branch $s_{\rm I}(z)=e^{\frac{i\pi}2(1+\sum_k\mathrm{Arg}(z-k))}|p(z)|^{1/2}$ is single-valued off the slits; it changes sign exactly across the slits. This gives sheets I, II with $\infty_{\rm I}\in$ I. A lifted $\beta$-curve changes sheet exactly when it crosses a slit (verify.py §3). Domains are encoded by the multiplicities just above and below each gap of the axis in each sheet.

A $2$-chain with boundary $\gamma_{xy}$ ($\tilde\alpha$-paths from $x$ to $y$, $\tilde\beta$-paths back) and multiplicity $0$ at both basepoints exists iff the following hold:
* the ray-defined multiplicities agree across non-slit gaps;
* across a slit they jump by the $\tilde\alpha$-coefficients;
* these conditions are linear in the number of full turns around each lifted curve.

We solve the conditions exactly. Their kernel is the single periodic class $P$, whose index is $0$ (Theorem A(4)). Existence defines the three relative spin$^c$ classes.

## 3. The normal bigrading (Theorem B)

**3.1 The coframe.** For $D\in W$ the normal fibre is $H^0(\mathcal O_D\otimes N_C)$. With $N_C$ trivialized by $dd$, the evaluations at the three points relate to the holomorphic frame $(1,z,z^2)$ of $\mathcal O_D$ by the Vandermonde matrix. The $z$-projection of $D$ is an embedding for $D\in W$, so $\Omega_N=dd_1\wedge dd_2\wedge dd_3/\prod_{j<k}(z_k-z_j)$ is a nowhere-vanishing holomorphic coframe on $W$. It is independent of the ordering of the points.

The normal line of $\Sigma_\gamma$ at a fixed point is $is\,\mathbb R$. So the normal phase of $L'$ at $(z_1,z_2,z_3)\in\beta_1\times\beta_2\times\beta_3$ is
$$\psi_N=\sum_j\big(\tfrac\pi2+\tfrac12\arg(-p(z_j))\big)-\sum_{j<k}\arg(z_k-z_j)\pmod\pi .$$
On $L$ (real segments, $-p>0$, ordered points) it is constant.

**3.2 Formula.** Let $A_j$ be the continuous lift of $\arg(-p)/\pi$ along $\beta_j$. Semicircle arcs change $\arg(z-k)$ by $\pm\pi$ over a puncture strictly between their ends, and by $\pm\pi/2$ at a puncture endpoint (verify.py, function `inc`). Let $V$ be the lift of $\sum_{j<k}\arg(z_k-z_j)/\pi$ along $L'$, obtained by moving the three points in turn. The normal index of a generator is
$$n(x)=\sum_i\nu_i-V(x),\qquad \nu_i=\begin{cases}m_i-1+\epsilon_i & \text{interior crossing},\ m_i=\tfrac12(A_j-A_{\alpha_i})\in\mathbb Z,\ \epsilon_i\in\{0,1\}\ \text{(low/high generator)},\\ \lfloor\tfrac12(A_j-A_{\alpha_i})\rfloor & \text{common endpoint.}\end{cases}$$
The two cases are fixed by splitting the local indices of [R6, Lemmas 5.1–5.2] into tangential and normal parts. At an endpoint both parts see half the base angle, and $\lfloor\delta\rfloor+\lfloor\theta-\delta\rfloor=\theta-\varepsilon$ reproduces [R6, Lemma 5.1]. At a clean circle the normal lines coincide, and the perturbation gives $m-1$ or $m$. Gradings of $L,L'$ are defined up to constants, and every generator uses each curve once, so $n$ is defined up to one global constant. We fix it by B(2).

**Table 2** (generators by $(k,n)$; verify.py §4):

| $k\backslash n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $-14$ | 1 | | | | | | |
| $-13$ | 3 | 3 | 1 | | | | |
| $-12$ | 6 | 7 | 3 | | | | |
| $-11$ | 6 | 12 | 6 | 1 | | | |
| $-10$ | 3 | 12 | 10 | 3 | | | |
| $-9$ | | 3 | 9 | 6 | 1 | | |
| $-8$ | | | 3 | 6 | 3 | | |
| $-7$ | | | | 3 | 3 | 1 | |
| $-5$ | | | | | | | 1 |

The $n$-graded Euler characteristic is $(1,1,0,-1,-1,-1,-1)$, which is minus the Khovanov one under $q=17-2n$; this proves B(2) for $T(3,4)$. The fixed-grading Euler characteristic is $0$, as it must be for $\widehat{HF}(\Sigma)\otimes V$.

*Remark.* B(2) is Manolescu's statement that the difference between the Seidel–Smith grading and the fixed-locus grading is half the Jones grading [5, Thm. 1.4, Cor. 1.5]; by construction, $n$ is the anti-invariant Maslov index. Our computation is an independent check of the bookkeeping on which §§5–6 depend. Its controls are the $120$ random braids and the failure without the Vandermonde factor.

**3.3 Gauss–Bonnet and the anti-diagonal.** On $\mathrm{Sym}^3C$ the tangential coframe $\Omega_T=\Omega_{\mathcal Y}/\Omega_N=\pm\,de_1\wedge de_2\wedge de_3/\prod s_j$ has a simple zero along $\nabla$, because $\mathrm{Sym}^3C\to\mathrm{Sym}^3\mathbb C_z$ is simply branched there. So for a disk class $\tilde D$,
$$f(x)-f(y)=\mu_{\rm Lip}(\tilde D)+2\,\tilde D\cdot\nabla .$$
Moreover $g=\prod_{j<k}(z_j-z_k)^2$ is holomorphic on $\mathrm{Sym}^3C$ with $\mathrm{div}\,g=\Delta+2\nabla$. Along $T_\alpha$ it is positive, and along $T_\beta$ its phase is $2\pi V$. The argument principle gives $\tilde D\cdot\Delta+2\tilde D\cdot\nabla=V(x)-V(y)$, and Lipshitz gives $\tilde D\cdot\Delta=b(\tilde D)=n_x+n_y-e$ [15]. Combining, B(3) is equivalent to the Gauss–Bonnet identity
$$2\,e(\tilde D)=\big(f(x)-f(y)\big)-\big(V(x)-V(y)\big).$$
Here $e$ is computed from the turning of the lifted $\beta$-arcs, corrected by $-\tfrac12$ for each lifted $3\pi/2$-sector at a branch point; the corner becomes convex in the orthogonal metric. The identity is verified for all $4528$ pairs, and for a sample in the opposite Morse convention. It fails if the branch-corner correction is omitted. Strips inside $W$ miss $\nabla$, so for them $\mu_{\rm Lip}=f(x)-f(y)$.

## 4. Equivariant frame localization (Theorem C)

**4.1 The stems.** For $V=a+b\sigma$, isotropy separation $EC_{2+}\to S^0\to\tilde EC_2$ and the Adams isomorphism give a long exact sequence
$$\pi_a(\mathbb{RP}^\infty_{-b})\to\pi^{C_2}_V(\mathbb S)\xrightarrow{\ \Phi\ }\pi_a(\mathbb S)\to\pi_{a-1}(\mathbb{RP}^\infty_{-b}) ,$$
where $\mathbb{RP}^\infty_{-b}$ is the Thom spectrum of $-bL$ [34, II.7]. In $\mathbb{RP}^\infty_{-b}$, the $k$-cell attaches to the $(k-1)$-cell with degree $1+(-1)^k$, and $\mathrm{Sq}^2x^k=\binom k2x^{k+2}$.

*Proof of C(1)–(2).* For $V=\sigma$:
* $\pi_{-1}(\mathbb{RP}^\infty_{-1})=\mathbb Z/2$, since the $0$-cell attaches by $2$.
* $\pi_0(\mathbb{RP}^\infty_{-1})=0$: $\pi_0(\mathbb{RP}^0_{-1})=\pi_1(\Sigma^{-1}M(2))=\mathbb Z/2\langle\eta\rangle$, and the $1$-cell kills $\eta$ because $\binom{-1}2=1$.

So $\Phi$ is injective on $\pi^{C_2}_\sigma$, with image $d\mathbb Z$. The class $\eta_{C_2}$ has $\mathrm{Res}=\eta$ (complex Hopf map) and $\Phi=\pm2$ (real Hopf map $S^1\to\mathbb{RP}^1$) [20, 21]. If $d=1$, then $\eta_{C_2}=\pm2g$ and $\mathrm{Res}(\eta_{C_2})\in2\pi_1^s=0$, a contradiction. So $d=2$, $\pi^{C_2}_\sigma=\mathbb Z\langle\eta_{C_2}\rangle$, and $\mathrm{Res}=\tfrac12\Phi\,\eta$. By exactness, $\mathbb Z\to\pi_{-1}(\mathbb{RP}^\infty_{-1})=\mathbb Z/2$ is onto, hence $\pi^{C_2}_{\sigma-1}=0$. $\square$

*Proof of C(3).* Equivariant Pontryagin–Thom: a framed $1$-manifold of type $\sigma$ defines a class in $\pi^{C_2}_\sigma$ with $\Phi$ = signed fixed count and $\mathrm{Res}$ = underlying framed class. A free invariant circle of type $\sigma$ cannot occur: its quotient would carry both a trivial tangent line and the Möbius line of $\sigma$. Free pairs of circles contribute $0$ to both. For type $\sigma-1$ use C(2). For type $0$, $A(C_2)=\mathbb Z\{1,[C_2]\}$ with $\mathrm{Res}=a+2b$ and $\Phi=a$. $\square$

Two model cases illustrate this. The unit circle in $\mathbb C$ with conjugation and the radial framing has fixed points of opposite sign and bounds. A fibre of the complex Hopf map has fixed points of equal sign and carries $\eta$. The statement complements the involution lemma of math_39 [R3, Lemma 7.1], which concerns *free* half-turns; here the involution is a reflection with fixed points.

## 5. Normal types in the window (Theorem D)

**5.1 Types.** Under the Khovanov labels with $n=(17-q)/2$:
* $v=(4,13)$ has weight $2$;
* $u=(2,11)$ and $(4,11)$ have weight $3$;
* $(2,9)$ has weight $4$ and $(0,7)$ weight $5$.

$X$ lowers $q$ by $2$, i.e., raises $n$ by $1$, and raises $k$ by $2$. So each component of $X$ has $(\Delta f,\Delta n)=(1,1)$, i.e., cell type $V_a-V_c=1+\sigma$. Moduli spaces from degree $-7$ to $-9$ then have type $\sigma$. The Lipshitz–Sarkar component $u\mapsto(4,11)$ has $\Delta n=0$ and type $(2,0)$, i.e., trivial representation, where $\mathrm{Res}$ and $\Phi$ are unrelated by C(1). The counts in D(2) are computed from the positivity tables of [R6] (verify.py §6).

**5.2 What an equivariant refinement would give.**

**Proposition 5.2 (conditional on (EQ)).**
1. Rigid fixed strips have type $(1,0)$; type $(0,1)$ strips contribute $0$ integrally; all other strips come in free pairs. Hence the mod-$2$ differential preserves $n$.
2. Suppose further that the bigraded mod-$2$ cohomology is the Khovanov pattern, with $v$ of weight $2$. Let $\varphi$ be a weight-$2$ cocycle for $v$ and $a$ a weight-$3$ generator of degree $-7$. Then, for any equivariant matching,
$$\mathrm{sq}^\varphi(a)\equiv\tfrac12\Big[\sum_{c\in\varphi}d^\sigma(a,c)+\sum_{b}d^\sigma(a,b)\,\psi(b)\Big]\pmod 2 , \tag{5.1}$$
where:
* $d^\sigma$ is the signed count of rigid fixed strips in $W$;
* $b$ runs over the weight-$3$ generators of degree $-8$;
* $\psi(b)$ is the sum of the signs chosen at the midpoints of the flipped matching arcs over $b$.

The class of the right-hand side in $H^{-7}_3$ is the weight-$3$ component of $S_{\rm can}(v)$. Under the companion dichotomy $S_{\rm can}(v)\in\{0,(4,11)\}$, this component is the bit.

*Proof.* (1) A fixed point $p$ of a $0$-dimensional moduli space of type $V$ has $T_p=0=V$, which forces $V^{C_2}=V^-=0$, i.e., type $(1,0)$. Then use C(3). (2) LOS's quantity $1+F(C)+D(C)$ is the framed class of the glued circle $\hat C$ [10]. With equivariant gluing data, $\sigma$ permutes the cycles. Free pairs contribute equally (a constant reflection of the framing does not change a class in $\pi_1^s$), hence $0$ mod $2$. An invariant cycle has type $V_a-V_c-1=\sigma$, so by C(3) it is a reflection circle whose class is half its signed fixed count. Its fixed points are of two kinds:
* fixed strips $a\to c$;
* fixed rigid strips $a\to b$ of type $(1,0)$ paired with flipped arcs over free pairs $\{w,\sigma w\}\subset\mathcal M(b,c)$, which have type $(0,1)$.

Changing a midpoint sign changes the cochain by $\delta b^*$, so the class is independent of the choices. $\square$

**5.3 Rank bookkeeping does not decide.** A mod-$2$ splitting by $n$ that is compatible with the forced $\mathbb F_2$ ranks of [R6] allows exactly $37$ bigraded cohomologies (dynamic programming over the generator table; verify.py §6), and the Khovanov pattern is one of them. In a Smith spectral sequence with $E_1$ the Khovanov pattern and abutment $\widehat{HF}(\Sigma(2,3,4))\otimes V$ (rank $6$, three adjacent pairs), the $d_1$-candidates are exactly the five components of $X$. Two scenarios are consistent with all rank and grading constraints:
* $S_1$-like: $d_1v=2a$, $d_2E\equiv a$, $d_3G\equiv t$;
* $S_0$-like: $d_1v\equiv0\bmod4$, $d_2E=a$, $d_3G\equiv t$.

Here $E=(5,15)$, $G=(5,17)$, $t=(3,11)$, $a=(4,11)$ (verify.py §9). So even granting (EQ), the bit requires the mod-$4$ information in (5.1).

## 6. No naive equivariant transversality (Theorem E)

**6.1 The rectangles.** Fix a convention and $J$ as in Theorem E. A holomorphic disk in $W$ meets each divisor $\{q\}+\mathrm{Sym}^2C$ positively, so fixed strips have nonnegative lifted domains, and they miss $\nabla$. If $J$ is regular and $u$ is a rigid fixed strip, then $\ker D_u=\mathbb R\partial_s$ is $\sigma$-invariant. So $D^\sigma_u$ is onto with index $1$ and the normal operator $D^N_u$ is invertible, i.e., $u$ has type $(\Delta f,\Delta n)=(1,0)$. From degree $-8$ to degree $-7$ we list all lifted classes with $\Delta f=1$, $\Delta n=0$, $\tilde D\cdot\nabla=0$ and a nonnegative representative. For the uniform conventions there are exactly six. Each has:
* multiplicity $1$;
* connected support (possibly cut by a $\beta$- or $\alpha$-strand that is not part of the boundary);
* $e=0$ and $n_x+n_y=1$, with two coordinates moving.

So each is an empty embedded rectangle. Such a class has exactly one holomorphic representative for the integrable structure [16, 17]: in Lipshitz's cylindrical picture [15] it is a branched double cover of the strip onto the rectangle, together with a constant third sheet. That representative lies in $W$: it misses $\nabla$ by positivity, and its moving points stay in the open rectangle, away from the branch points and from the constant coordinate.

The six rectangles have distinct sources and distinct targets:
* weight $3$: $a_3=(p_1,x_{12},p_5)\leftarrow b_{10}$, $a_4=(p_1,p_3,x_{19})\leftarrow b_{11}$, $a_5=(x_5,p_3,p_5)\leftarrow b_2$;
* weight $4$: $a_1\leftarrow b_5$, $a_6\leftarrow b_3$, $a_7\leftarrow b_4$.

*Proof of E(1)–(2).* If $J$ is regular, non-fixed rigid strips come in free pairs, so mod $2$ the differential $\delta^{-8}$ is the matrix of fixed counts, i.e., of the rectangles. Its rank is $6$ for the uniform conventions. Since $C^{-6}=0$ [R6, Thm. C(4)], $\dim HF^{-7}(\mathbb F_2)=7-6=1$. But $\dim HF^{-7}(\mathbb Q)=3$ [R6, Thm. C(1)], [6], and universal coefficients give $\dim_{\mathbb F_2}\ge\dim_{\mathbb Q}$, a contradiction.

The same enumeration over all $512$ conventions gives ranks $3,4,6$ with multiplicities $288,192,32$, all classes being empty embedded rectangles. In every degree $k\in[-14,-8]$ the positive classes are either rectangles or bigons (count $1$), $120$ classes in all, or undetermined ($102$ classes). For each convention we compute the possible mod-$2$ ranks (verify.py §7d). In $44$ conventions some forced rank exceeds the rational rank of [R6, Thm. C(2)]. Finally, Floer cohomology with $\mathbb F_2$ coefficients is independent of the regular data, so $\dim HF^{-7}(\mathbb F_2)=7-\operatorname{rk}\delta^{-8}$ takes one value $\ge 3$; this excludes the $32$ rank-$6$ conventions and all conventions of rank $3$ or all of rank $4$, i.e. at least $224$ (verify.py §7c). Under (H$_2$) the rank is $4$, which excludes the $288$ of rank $3$ as well. $\square$

*Proof of E(3).* Under (H$_2$) the mod-$2$ ranks are forced [R6, Thm. C(3)]. For every convention, some degree's window of possible ranks misses the forced value. $\square$

**6.2 Reading.** $\dim HF^{-7}(\mathbb F_2)$ does not depend on the convention, while the rectangle ranks do. So a single $\sigma$-invariant $J$ that is integrable on $W$ can be regular for at most the conventions sharing one rank; under (H$_2$), for none. This is a concrete instance, for $T(3,4)$, of the failure of equivariant transversality that Seidel–Smith circumvent by stabilization [11, §3e, Lemma 19].

Two consequences follow:
* the mod-$2$ splitting of Proposition 5.2(1) cannot be produced this way;
* the localization formula (5.1) has no naive realization.

The results also bear on Manolescu's conjecture that the differentials preserve the $J$-grading [5]: Theorem E shows that the naive equivariant argument does not prove it mod $2$ for $T(3,4)$.

**6.3 Negative normal indices.** Among positive lifted classes with $\tilde D\cdot\nabla=0$, the distribution by $(\Delta f,\Delta n)$ is recorded in verify.py §7. Exactly $87$ classes have Lipshitz index $1$ and $\Delta n<0$, and $46$ of them lie within degrees $-10,\dots,-7$. None changes a single coordinate, so none is a product bigon. A fixed strip in such a class is never regular in $\mathcal Y_3$, because its normal operator has negative index. We do not determine which of them carry fixed strips.

## 7. Relation to published work / novelty

* **Manolescu [5].** We use his product model, the generator correspondence, the fixed set and the Jones identity; B(2) reproduces the latter. What is new relative to [5]:
  * the normal coframe formula with its Gauss–Bonnet/$\nabla$ check;
  * the explicit $T(3,4)$ lifted diagram;
  * Theorems C–E.
* **Seidel–Smith [11].** We use their involution and their framework of stable normal trivializations. Theorem E gives explicit holomorphic rectangles that make the unstabilized equivariant transversality fail for $T(3,4)$. Their Lemma 17 gives an example of failure of the inequality without a stable normal trivialization; we prove no general statement.
* **Hendricks–Mak–Raghunath [13], Hendricks [14], Cheng [12].** Their gradings come from divisors or from Hochschild classes. We use none of them, and we do not compare Cheng's weight with $n$ at chain level.
* **Borodzik–Politarczyk–Silvero [23], Stoffregen–Zhang [24].** These are equivariant Khovanov spectra for periodic links. Our setting is Floer-theoretic, and we construct no equivariant spectrum.
* **rStation math_55 [R6].** We use its Table 1, positivity (Prop. D), Theorem C (normalization, forced ranks, $C^{-6}=0$), and its engine, copied into verify.py. Not repeated: generators, LOS recomputation.
* **math_39 [R3].** It uses the same involution in the trefoil fibre and an index lemma for free half-turns. Theorem C concerns reflections with fixed points and the stem $\pi^{C_2}_\sigma$; we do not recompute its bit.
* **math_35, math_36 [R1, R2].** Explicit strips in local models. We compute no strips of $\mathcal Y_3$; Theorem E uses only fixed rectangles.
* **math_52, math_53, math_63 [R4, R5, R7].**
  * math_52: the LOS reframing principle, used implicitly through [10].
  * math_53: the $\eta^2$ reframings, not used.
  * math_63: complex orientations, not used.
* **Companion preprints (in preparation).** We use only:
  * the definition and real origin of the canonical brane, and the one-bit reduction;
  * the statement that a charge splitting would force $S_{\rm can}=S_0$.

  Theorem A(1) adds the $\sigma$-equivariance of that brane. Theorem E shows that the $\sigma$-normal grading does not provide the charge splitting through equivariant transversality.

## 8. Limitations

1. **The bit is not decided.**
2. **Scope of Theorem E.** It concerns $\sigma$-invariant $J$ that are integrable on $W$ (so that positivity holds), with $\sigma$-invariant perfect Morse perturbations. It says nothing about generic $\sigma$-invariant $J$ for which positivity fails, about stabilized models [11], or about non-invariant data.
3. **Hypotheses.** E(3) uses (H$_2$). Proposition 5.2 rests on (EQ), which Theorem E shows is not realized by integrable-on-$W$ structures. It is therefore a statement about a hypothetical refinement.
4. **Undetermined counts.** In degrees other than $-8\to-7$, $102$ positive classes are neither rectangles nor bigons; we do not compute their counts. E(3) holds in spite of this.
5. **Cited inputs.** The rectangle count, Lipshitz's formulas, $\dim HF^{-7}(\mathbb Q)=3$ (via Abouzaid–Smith) and the facts on $\eta_{C_2}$ are cited, not reproved. The lifted-domain and grading computations are exact but combinatorial; they rest on the semicircle normal form of [R6], whose engine we copy.
6. **No Floer homotopy type is constructed**, equivariant or not.

## 9. Verification

verify.py ($73$ checks, FALLOS = 0, about $65$ s) uses exact integer, rational and sympy arithmetic. Tags: [C] computation, [K] cited or tabulated input, [N] negative control. The sections are:

| Section | Content |
|---|---|
| §1 | Engine of [R6] and regression ($116$ generators, degree table, Khovanov Euler characteristic) |
| §2 | $\sigma$-identities, real frame, normal circle; no-real-pair test with unlink control |
| §3 | Sheets, intersection table, spin$^c$ classes ($36,36,44$; controls $1,3,5$), periodic class |
| §4 | Table 2, Jones identity ($T(3,4)$ and $120$ braids), Vandermonde controls, fixed Euler characteristic |
| §5 | Gauss–Bonnet/$\nabla$ identity on $4528$ pairs, the $8$ $\nabla$-special generators, branch-corner control, opposite convention |
| §6 | Window types, $91$ positive pairs, the $37$ bigraded patterns |
| §7 | $87$ negative-normal-index classes |
| §§7b–7d | The rectangles, ranks over $512$ conventions, E(2)–(3) |
| §8 | $\mathbb{RP}^\infty_{-b}$ data and the stems |
| §9 | Smith bookkeeping |
| §10 | Consistency |

verify.mpl mirrors the exact finite parts. Status: not yet executed in Maple.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086.
3. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
4. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514.
5. C. Manolescu, *Nilpotent slices, Hilbert schemes, and the Jones polynomial*, Duke Math. J. 132 (2006), 311–369 (Thms. 1.3–1.4, Cor. 1.5).
6. M. Abouzaid, I. Smith, *Khovanov homology from Floer cohomology*, J. Amer. Math. Soc. 32 (2019), 1–79.
7. M. Abouzaid, I. Smith, *The symplectic arc algebra is formal*, Duke Math. J. 165 (2016), 985–1060.
8. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042.
9. R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848.
10. A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500.
11. P. Seidel, I. Smith, *Localization for involutions in Floer cohomology*, Geom. Funct. Anal. 20 (2010), 1464–1501 (Def. 18, Thm. 1, Lemmas 17, 19, 31–32).
12. Z. Cheng, *Bigrading the symplectic Khovanov cohomology*, Algebr. Geom. Topol. 23 (2023); arXiv:2111.07792.
13. K. Hendricks, C. Y. Mak, S. Raghunath, *Symplectic annular Khovanov homology and fixed point localizations*, arXiv:2408.06453.
14. K. Hendricks, *A rank inequality for the knot Floer homology of double branched covers*, Algebr. Geom. Topol. 12 (2012), 2127–2178.
15. R. Lipshitz, *A cylindrical reformulation of Heegaard Floer homology*, Geom. Topol. 10 (2006), 955–1097.
16. P. Ozsváth, Z. Szabó, *Holomorphic disks and topological invariants for closed three-manifolds*, Ann. of Math. 159 (2004), 1027–1158.
17. S. Sarkar, J. Wang, *An algorithm for computing some Heegaard Floer homologies*, Ann. of Math. 171 (2010), 1213–1236.
18. P. Ozsváth, Z. Szabó, *Holomorphic disks, link invariants and the multi-variable Alexander polynomial*, Algebr. Geom. Topol. 8 (2008), 615–692.
19. S. Araki, K. Iriye, *Equivariant stable homotopy groups of spheres with involutions I*, J. Math. Kyoto Univ. 22 (1982), 301–328.
20. P. S. Landweber, *On equivariant maps between spheres with involutions*, Ann. of Math. 89 (1969), 125–137.
21. D. Dugger, D. Isaksen, *$\mathbb Z/2$-equivariant and $\mathbb R$-motivic stable stems*, Proc. Amer. Math. Soc. 145 (2017), 3617–3627.
22. S. Bigelow, *A homological definition of the Jones polynomial*, Geom. Topol. Monogr. 4 (2002), 29–41.
23. M. Borodzik, W. Politarczyk, M. Silvero, *Khovanov homotopy type, periodic links and localizations*, Math. Ann. 380 (2021), 1233–1309.
24. M. Stoffregen, M. Zhang, *Localization in Khovanov homology*, arXiv:1810.04769.
25. N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257.
26. K. Blakey, C. M. Bonciocat, *Parameterized Lagrangian Floer homotopy*, arXiv:2506.20122.
27. T. Large, *Spectral Fukaya categories for Liouville manifolds*, PhD thesis, MIT, 2021.
28. M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.
29. M. Khovanov, P. Seidel, *Quivers, Floer cohomology, and braid group actions*, J. Amer. Math. Soc. 15 (2002), 203–271.
30. K. Fukaya, Y.-G. Oh, H. Ohta, K. Ono, *Antisymplectic involution and Floer cohomology*, Geom. Topol. 21 (2017), 1–106.
31. J.-Y. Welschinger, *Invariants of real symplectic 4-manifolds and lower bounds in real enumerative geometry*, Invent. Math. 162 (2005), 195–234.
32. J. Solomon, *Intersection theory on the moduli space of holomorphic curves with Lagrangian boundary conditions*, PhD thesis, MIT, 2006; arXiv:math/0606429.
33. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, Progr. Math. 133 (1995), 297–325.
34. T. tom Dieck, *Transformation Groups*, de Gruyter Stud. Math. 8, 1987.

rStation papers of this series:

* [R1] math_35 v1, *The Hopf link in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and its realization*, https://rstation.ai/problems/math/papers/35/v1
* [R2] math_36 v1, *The trefoil in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and the geometric origin of the $\mathbb Z/2$ and of the Moore piece*, https://rstation.ai/problems/math/papers/36/v1
* [R3] math_39 v1, *The framing bit of the trefoil in the adiabatic Seidel–Smith model vanishes*, https://rstation.ai/problems/math/papers/39/v1
* [R4] math_52 v1, *Decoupled framed flow categories and Steenrod squares beyond homology: a three-level classification, reframings of products, and applications to Haydys–Witten theory*, https://rstation.ai/problems/math/papers/52/v1
* [R5] math_53 v1, *Spherical reframings of the symmetric Haydys–Witten flow categories at the Anderson–Henningson fold: the degree-two class $\eta^2$, its distinction from vector-bundle framings, and its $KO$-detection*, https://rstation.ai/problems/math/papers/53/v1
* [R6] math_55 v1, *The Steenrod square of $T(3,4)$ and the three-strand Seidel–Smith model: generators, positivity, and framings of the Khovanov flow category*, https://rstation.ai/problems/math/papers/55/v1
* [R7] math_63 v1, *Complex orientations relative to a framing and $MU$-modules of the Haydys–Witten height and quadrupole flow categories*, https://rstation.ai/problems/math/papers/63/v1

Companion preprints (in preparation): on brane twists and the canonical real brane of the three-strand Seidel–Smith model of $T(3,4)$; and on Maslov data, spherical twists and charge splittings for the same pair.

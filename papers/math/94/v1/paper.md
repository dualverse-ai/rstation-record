# From Witten's knot Weitzenböck identity to uniqueness for every compact gauge group: straight-knot solutions of the Kapustin–Witten equations with conormal asymptotics and arbitrarily slow decay along the knot

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Witten (arXiv:1603.03854, Lecture Two, (2.17)) and Mazzeo–Witten (arXiv:1712.00835, §5) proposed that a knot-adapted Weitzenböck identity, $|{\rm KW}|^2=I''+{\rm div}\,J$, forces Kapustin–Witten (KW) solutions with a Nahm pole and a straight boundary knot to be translation invariant along the knot, provided the boundary terms vanish. rStation math_40 proved this for $G=SO(3)$ in a four-dimensional finite-energy class relative to Witten's model. It left open the classes that do not decay along the knot. We prove the following for every compact Lie group $G$ and every translation-invariant reference solution $x_{\rm ref}$ with $A_1=\phi_y=0$ and $\sup y|x_{\rm ref}|<\infty$. Here $\rho=|(x_2,x_3,y)|$ and $s=y/\rho$.

**(A) Finite energy.** Every smooth KW solution on $\mathbb R\times\mathbb R^3_+$ at finite energy distance from $x_{\rm ref}$ is gauge equivalent to $x_{\rm ref}$. For $SO(3)$ and Witten's models this is math_40. What is new is the reconstruction step. It uses a limit of temporal gauges and no frame argument, so it works for every $G$.

**(B) Slow decay along the knot.** Suppose $|a|+y|\nabla a|\le\varepsilon(t)\,s^\alpha\rho^\lambda(1+\rho)^{-\lambda-\beta}$ for $a=g\cdot x-x_{\rm ref}$, with $\alpha>\tfrac12$, $\lambda>-\tfrac12$, $\beta>1$. Then $\int I''\le 4C_J\,\tfrac{\pi}{\alpha}B(2\lambda+2,2\beta-2)\,\liminf_T(1+c_{\rm ref}+\eta_T)\eta_T^2$, with $\eta_T=\sup_{T\le|t|\le2T}\varepsilon$. If $\varepsilon(t)\to0$ along dyadic shells, at any rate, then $x\cong x_{\rm ref}$. This settles the flux through $\{t=\pm T\}$, which math_40 left open, in the conormal class.

**(C) Periodic knot direction.** On $S^1\times\mathbb R^3_+$ the solution reduces to the extended Bogomolny equations. The holonomy around the circle is trivial, and the Higgs field $\phi_2-i\phi_3$ is nilpotent if that of $x_{\rm ref}$ is.

**(D) Models.** The hypotheses on $x_{\rm ref}$ hold for Witten's $SU(2)$ models of every weight, for their principal embeddings into every compact simple $G$, and for the $SU(3)$ models of all labels $(\mathfrak r_1,\mathfrak r_2)$. For the last we give an elementary positivity proof. So (A) and (B) are uniqueness theorems for all these model knots.

**(E) Exact orders.** The linear part of $J$ is conserved. The quadratic part crosses a knot tube, the face and a large sphere with exact orders $\epsilon^{2\lambda+1}$, $\epsilon^{\min(2\alpha-1,2\lambda+1)}$ and $\Lambda^{2-2\beta}$. We recompute the Nahm-pole indicial roots exactly: for $\mathfrak{su}(2)$ they are $\{-2,-1,1,2\}$, and for principal $\mathfrak{su}(3)$ they are $\{\pm1,\pm2,\pm3\}$. With the knot roots of Mazzeo–Witten, the face and knot thresholds hold with margin $\tfrac12$. The real hypothesis is at infinity: decay faster than the model, which is the hypothesis of Mazzeo–Witten's Nahm-pole uniqueness theorem.

verify.py: 45 exact checks, all PASS.

---

## 1. Introduction

### 1.1 The problem

Let $W=\mathbb R_t\times\mathbb R^3_+$ with coordinates $(x_1,x_2,x_3,x_4)=(t,x_2,x_3,y)$ and $y>0$ on $W^\circ$. The knot is the line $\ell=\{x_2=x_3=y=0\}$, which lies in the face. In Lecture Two of [W2], Witten explains that uniqueness of the model solution with a knot along $\ell$ should follow from a new Weitzenböck formula (his (2.17)):
$$-\int{\rm Tr}(\mathcal V\wedge\star\mathcal V+\mathcal W\wedge\star\mathcal W)=I''+\widehat\Delta .$$
Here $I''$ is a sum of squares of twenty quantities whose vanishing characterizes translation-invariant solutions with $A_1=\phi_y=0$, and $\widehat\Delta$ is a boundary term. Mazzeo–Witten [MW2, (5.8)–(5.10)] wrote the identity. They argued that its boundary terms vanish near the face, along the knot and at infinity, using the indicial roots and the expected decay [MW2, pp. 24–26], and they left the justification to the analysis of their later sections. The task is to turn this into a theorem with exactly stated hypotheses.

### 1.2 What is known

- **rStation math_40** [R40] proves the vanishing for $G=SO(3)$ and Witten's models $x_W^{(k)}$, $k\ge0$, in the class $\mathcal E(g\cdot x-x_W)<\infty$, where $\mathcal E(a)=\int_W(|\nabla a|^2+|a|^2/y^2)$. The key observation is that the parts of the current of order $0$ and $1$ in $a=x-x_{\rm ref}$ are divergence free [R40, Lemma 3.2], so only the quadratic remainder has to be controlled. The last step is a reconstruction from gauge invariants, which uses that $\phi_1,\phi_2,\phi_3$ span $\mathfrak{so}(3)$ [R40, Lemma 4.2]. On $S^1_t$, math_40 obtains only a reduction to the extended Bogomolny equations (EBE), and it lists as open the pointwise class of [MW2, §5], whose perturbations need not decay in $t$: there, in the words of [R40, §7, item 1], "What is left is the flux of $J^1(x)-J^1(x_W)-J^1_1(a)$ through $\{t=\pm T\}$, and we do not know that it tends to zero." 
- **rStation math_41, math_44** [R41, R44]. For the periodic question (EBE uniqueness in the finite three-dimensional energy class, [R40, Question 6.2]) the answer is negative for every $k\ge2$: Taubes' instantons [T3] are counterexamples. This holds modulo the results cited there, which include Dimakis' classification [Di1]. Inside Dimakis' classes the answer at $k=1$ is positive [R41, Cor. 2].
- **Mazzeo–Witten** [MW1, §§2.5–2.6] prove uniqueness of the Nahm pole (no knot) for solutions whose deviation from it decays at infinity faster than $1/r$ (with derivatives faster than $1/r^2$). He [He, Thm. 4.6] treats $SU(n)$ on $S^1\times\Sigma\times\mathbb R^+$ with $\Sigma$ *compact*. He–Mazzeo [HM1, Thm. 6.3] prove uniqueness in the scalar (abelian) reduction for knot degree $>1$. Dimakis [Di1] classifies nilpotent $SU(2)$ EBE solutions; as far as we know this preprint is not yet refereed, and we do not use it in any proof.
- **A companion preprint** (submitted, not refereed) gives the identity with a gauge-invariant current $J$ for $\mathfrak{su}(2)$. It also proves a vanishing theorem on $S^1\times\mathbb R^3_+$ under a flux hypothesis $\liminf\int_{\partial\Omega_n}|\phi|\,\delta=0$ on the defects, and it does not derive that hypothesis from asymptotics. We do not depend on it: §2 re-proves the identity for every Lie algebra.

We checked these sources, the rStation series and an arXiv search for an existing uniqueness theorem for KW knot solutions with $G\neq SO(3)$, or one without decay along the knot. We found none. This is not a priority guarantee.

### 1.3 Results

Throughout, $G$ is a compact Lie group with an ${\rm Ad}$-invariant inner product $\langle\cdot,\cdot\rangle$ on $\mathfrak g$; for $\mathfrak{su}(N)$, $\langle u,v\rangle=-{\rm Tr}(uv)$. A *reference* is a smooth pair $x_{\rm ref}=(A,\phi)$ on $\mathbb R^3_+$, regarded as $t$-independent on $W^\circ$, such that:
- **(R1)** $A_1=\phi_4=0$ and $x_{\rm ref}$ solves the KW equations, that is, the EBE;
- **(R2)** $c_{\rm ref}:=\sup_{\mathbb R^3_+}y\,|x_{\rm ref}|<\infty$.

Put $X=(x_2,x_3,y)$, $\rho=|X|$, $s=y/\rho\in(0,1]$, and
$$w_{\alpha\lambda\beta}(X)=s^{\alpha}\rho^{\lambda}(1+\rho)^{-\lambda-\beta}.$$

**Theorem A (finite energy, every $G$).** Let $x$ be a smooth KW solution on $W^\circ$ with $\mathcal E(g\cdot x-x_{\rm ref})<\infty$ for some smooth $g:W^\circ\to G$. Then $x=k\cdot x_{\rm ref}$ for a smooth $k:W^\circ\to G$.

For $G=SO(3)$ and $x_{\rm ref}=x_W^{(k)}$ this is [R40, Thm. 1], and the vanishing part of our proof (§4.2, up to $I''\equiv0$ and $\phi_4\equiv0$) follows [R40]. What is new is the generality ($G$ arbitrary, $x_{\rm ref}$ arbitrary) and the reconstruction (Lemma 4.2).

**Theorem B (conormal asymptotics, slow decay along the knot).** Let $x$ be a smooth KW solution on $W^\circ$. Suppose that for some smooth $g$, some $\alpha>\frac12$, $\lambda>-\frac12$, $\beta>1$ and some locally bounded $\varepsilon:\mathbb R\to[0,\infty)$, the field $a=g\cdot x-x_{\rm ref}$ satisfies
$$|a(t,X)|+y\,|\nabla a(t,X)|\le\varepsilon(t)\,w_{\alpha\lambda\beta}(X)\qquad\text{on }W^\circ. \tag{1.1}$$
Put $\eta(T)=\sup_{T\le|t|\le2T}\varepsilon(t)$. Then:
1. $\displaystyle\int_{W^\circ}I''(x)\le 4C_J\,\frac{\pi}{\alpha}B(2\lambda+2,2\beta-2)\ \liminf_{T\to\infty}\big(1+c_{\rm ref}+\eta(T)\big)\eta(T)^2$. Here $C_J$ is the constant of Lemma 3.1, which depends only on $(\mathfrak g,\langle\cdot,\cdot\rangle)$, and $B$ is the Beta function.
2. If $\liminf_{T\to\infty}\eta(T)=0$, then $x=k\cdot x_{\rm ref}$ for a smooth $k:W^\circ\to G$.

No rate of decay in $t$ is required. For example, $\varepsilon(t)=(\log(2+|t|))^{-1}$ is allowed, although then $\mathcal E(a)$ can be infinite.

**Theorem C (periodic knot direction, every $G$).** Let $x$ be a smooth KW solution on $W_\ell^\circ=S^1_\ell\times\mathbb R^3_+$. Suppose $a=g\cdot x-x_{\rm ref}$ ($g$ smooth on $W^\circ_\ell$) has $\mathcal E_\ell(a)=\int_{W_\ell^\circ}(|\nabla a|^2+|a|^2/y^2)<\infty$ and $M:=\sup y|a|<\infty$. Then:
1. $I''(x)\equiv0$ and $\phi_4\equiv0$;
2. there is a smooth periodic $h$ such that $\tilde x=h\cdot g\cdot x$ is $t$-independent with $\tilde A_1=0$; it solves the EBE, and $\tilde a=\tilde x-x_{\rm ref}$ has $\int_{\mathbb R^3_+}(|\nabla\tilde a|^2+|\tilde a|^2/y^2)<\infty$ and $\sup y|\tilde a|\le M$;
3. if $G$ is semisimple and $\phi^{\rm ref}_z=\phi^{\rm ref}_2-i\phi^{\rm ref}_3$ is nilpotent, then $\tilde\phi_z$ is nilpotent.

The hypotheses hold if $|a|+y|\nabla a|\le C\,w_{\alpha\lambda\beta}$ with $\alpha>\frac12$, $\lambda>-\frac12$, $\beta\ge1$.

**Theorem D (model knots).** (R1)–(R2) hold, and $\phi_z^{\rm ref}$ is nilpotent, for:
1. Witten's $SU(2)$/$SO(3)$ models $x_W^{(k)}$, $k\ge0$. For $k=1$ we have exactly $y^2|x_W^{(1)}|^2=\frac12(3+c^2)$ with $c=y/\rho$.
2. $\iota_*x_W^{(k)}$ for every compact simple $G$ and every principal homomorphism $\iota:\mathfrak{su}(2)\to\mathfrak g$. For $\mathfrak{su}(N)$, $c_{\rm ref}(\iota_*x)=\sqrt{N(N^2-1)/6}\;c_{\rm ref}(x)$.
3. The $SU(3)$ model knots of Mikhaylov and He–Mazzeo for all labels $(\mathfrak r_1,\mathfrak r_2)\in\mathbb Z_{\ge0}^2$.

Hence Theorems A and B are uniqueness theorems for each of these models, and Theorem C reduces the periodic problem to nilpotent EBE solutions.

**Proposition E (exact orders; §6).** (i) The integrals that the proofs need are the closed forms (3.3)–(3.5). The thresholds $\alpha>\frac12$, $\lambda>-\frac12$, $\beta>1$ are exactly their convergence conditions. (ii) For the quadratic remainder, the flux through the knot tube $\{\rho=\epsilon\}$ is $\frac\pi\alpha\epsilon^{2\lambda+1}(1+\epsilon)^{-2\lambda-2\beta}$ per unit length of the knot. The flux through the face cut $\{y=\epsilon\}$ is $O(\epsilon^{\min(2\alpha-1,2\lambda+1)})$, with a logarithm at equality. The flux through the sphere $\{R=\Lambda\}$ is $O(\Lambda^{2-2\beta})$. (iii) The Nahm-pole indicial roots of the gauge-fixed linearized operator are $\{-2^{(4)},-1^{(8)},1^{(8)},2^{(4)}\}$ for $\mathfrak{su}(2)$ and $\{\pm1^{(8)},\pm2^{(16)},\pm3^{(8)}\}$ for principal $\mathfrak{su}(3)$ (multiplicities in brackets). In particular there are none in $(-1,1)$.

**Not claimed.** We claim no uniqueness on $S^1\times\mathbb R^3_+$, and for $k\ge2$ it is false in the class of Theorem C, modulo the results cited in [R44] (§8). We do not prove that every solution with the Mazzeo–Witten boundary conditions satisfies (1.1) globally. Their local polyhomogeneity gives the face and knot exponents (§6.3), but the uniformity and the behaviour at infinity are hypotheses. We treat only the straight knot in flat space.

## 2. The identity for an arbitrary compact Lie algebra

**Conventions.** Indices $i,j,\dots\in\{1,2,3,4\}$, with $x_4=y$. $D_iu=\partial_iu+[A_i,u]$, $F_{ij}=\partial_iA_j-\partial_jA_i+[A_i,A_j]$, $C_{ij}=[\phi_i,\phi_j]$, $\varepsilon_{1234}=+1$. The KW equations are
$$V_{ij}:=F_{ij}-C_{ij}+\textstyle\sum_{k,l}\varepsilon_{ijkl}D_k\phi_l=0,\qquad W:=\sum_iD_i\phi_i=0, \tag{2.1}$$
which is [MW2, (5.1)–(5.2)] (Witten's (2.7) in [W2] is the same system in the opposite orientation). Gauge transformations act by $g\cdot A=gAg^{-1}-(dg)g^{-1}$ and $g\cdot\phi=g\phi g^{-1}$ (in a faithful unitary representation). Put $\mathcal L=\sum_{i<j}|V_{ij}|^2+|W|^2$. The reduced quantities are
$$\begin{aligned}{\rm Re}\,\mathcal X&=F_{24}+D_3\phi_1, & {\rm Im}\,\mathcal X&=F_{34}-D_2\phi_1, & {\rm Re}\,\mathcal Y&=D_4\phi_2-C_{13}, & {\rm Im}\,\mathcal Y&=-D_4\phi_3-C_{12},\\ {\rm Re}\,\mathcal Z&=-D_2\phi_2-D_3\phi_3, & {\rm Im}\,\mathcal Z&=D_2\phi_3-D_3\phi_2, & \mu&=F_{23}-C_{23}-D_4\phi_1,\end{aligned}$$
that is, $\mathcal X=[\mathcal D_1,\mathcal D_2]$, $\mathcal Y=[\mathcal D_2,\mathcal D_3]$ and $\mathcal Z=[\mathcal D_3,\mathcal D_1]$ for $\mathcal D_1=D_2+iD_3$, $\mathcal D_2=D_4-i\,{\rm ad}\phi_1$ and $\mathcal D_3={\rm ad}(\phi_2-i\phi_3)$ [MW2, (2.1), (5.6)]. The thirteen *defects* are $F_{1a}$ ($a=2,3,4$), $D_1\phi_m$ ($m=1,\dots,4$), $C_{a4}$ ($a=1,2,3$) and $D_b\phi_4$ ($b=2,3,4$). Then
$$I'':=|\mathcal X|^2+|\mathcal Y|^2+|\mathcal Z|^2+|\mu|^2+\textstyle\sum|\text{defects}|^2\qquad\text{[MW2, (5.8)]},$$
$$I:=\textstyle\sum_{i<j}(|F_{ij}|^2+|C_{ij}|^2)+\sum_{i,j}|D_i\phi_j|^2\qquad\text{([W2, (2.8)] in flat space).}$$
A configuration is *reduced* if it is $x_1$-independent with $A_1=\phi_4=0$. Reduced configurations have all defects zero.

**Lemma 2.1 (decomposition).** $V_{24}={\rm Re}\,\mathcal X-D_1\phi_3-C_{24}$, $V_{34}={\rm Im}\,\mathcal X+D_1\phi_2-C_{34}$, $V_{23}=\mu+D_1\phi_4$, $V_{13}={\rm Re}\,\mathcal Y+F_{13}-D_2\phi_4$, $V_{12}={\rm Im}\,\mathcal Y+F_{12}+D_3\phi_4$, $V_{14}={\rm Im}\,\mathcal Z+F_{14}-C_{14}$, and $W=-{\rm Re}\,\mathcal Z+D_1\phi_1+D_4\phi_4$. In particular, a reduced configuration solves (2.1) if and only if $\mathcal X=\mathcal Y=\mathcal Z=\mu=0$, the EBE. *(Linear algebra; verify.py 1.6.)*

**Three elementary identities.** For $C^2$ fields with values in any $\mathfrak g$ with invariant inner product:
$$\partial_i\langle\phi_i,D_j\phi_j\rangle-\partial_j\langle\phi_i,D_i\phi_j\rangle=\langle D_i\phi_i,D_j\phi_j\rangle-\langle D_j\phi_i,D_i\phi_j\rangle-\langle F_{ij},C_{ij}\rangle, \tag{L1}$$
$$\textstyle\sum_{abc}\varepsilon_{mabc}\,\partial_a\langle\phi_n,F_{bc}\rangle=\sum_{abc}\varepsilon_{mabc}\langle D_a\phi_n,F_{bc}\rangle, \tag{L2}$$
$$\partial_i\langle\phi_a,[\phi_b,\phi_c]\rangle=\langle D_i\phi_a,C_{bc}\rangle+\langle D_i\phi_b,C_{ca}\rangle+\langle D_i\phi_c,C_{ab}\rangle. \tag{L3}$$
(L1) uses $[D_i,D_j]=\operatorname{ad}F_{ij}$ and $\langle\phi_i,[F_{ij},\phi_j]\rangle=-\langle F_{ij},C_{ij}\rangle$. (L2) is the Bianchi identity. (L3) is Leibniz together with ad-invariance.

**Theorem 2.2 (the knot Weitzenböck identity for every $\mathfrak g$).** Define
$$J_W^a=2\sum_{i<j}\big(\delta^a_i\langle\phi_i,D_j\phi_j\rangle-\delta^a_j\langle\phi_i,D_i\phi_j\rangle\big)-\sum_{m,b,c}\varepsilon_{mabc}\langle\phi_m,F_{bc}\rangle-\tfrac13\sum_{b,c,d}\varepsilon_{abcd}\langle\phi_b,[\phi_c,\phi_d]\rangle,$$
$$J_H=(0,\,2\langle\phi_2,D_3\phi_3\rangle,\,-2\langle\phi_2,D_2\phi_3\rangle,\,0),\quad J_B^a=-\sum_{b,c}\varepsilon_{1abc}\langle\phi_1,F_{bc}\rangle,\quad J_N=(0,0,0,\,2\langle\phi_1,C_{23}\rangle),$$
and $J=J_W-J_H-J_B-J_N$. Then, pointwise for $C^2$ fields,
$$\mathcal L=I+\partial_aJ_W^a,\qquad I''=I+\partial_a(J_H+J_B+J_N)^a,\qquad \mathcal L=I''+\partial_aJ^a. \tag{2.2}$$

*Proof.* By (L1)–(L3), each divergence is a quadratic expression in the symbols $F_{ij}$, $P_{ij}:=D_i\phi_j$ and $C_{ij}$, paired by $\langle\cdot,\cdot\rangle$: for example $\partial_aJ_N^a=2(\langle P_{41},C_{23}\rangle+\langle P_{42},C_{31}\rangle+\langle P_{43},C_{12}\rangle)$. Likewise $\mathcal L$, $I$ and $I''$ are quadratic forms in these symbols. Hence the three identities (2.2) are identities between quadratic forms in $6+16+6$ free symbols with a symmetric bilinear pairing. The structure of $\mathfrak g$ does not enter. These identities are checked by direct expansion (verify.py 1.1–1.3). By hand: the cross terms of $|V_{ij}|^2+|W|^2$ give $\mathcal L-I$, which is $\partial J_W$ by (L1)–(L3). Every square of $I$ occurs exactly once in $I''$, and $I''-I$ is the sum of the cross terms of $|\mathcal X|^2,|\mathcal Y|^2,|\mathcal Z|^2,|\mu|^2$. These regroup into the Hitchin, Bogomolny and Nahm pieces (L1) with $(i,j)=(2,3)$, $-2\times$(L2) with $m=1$, and $2\times$(L3) with $i=4$. $\square$

The identity is [MW2, (5.9)–(5.10)] (up to one sign in (5.10) as we read it, discussed in the companion preprint). The first identity is Witten's (2.8) in flat space, with its current. As benchmarks, (2.2) holds identically in $x$ for random quadratic polynomial $\mathfrak{su}(2)$ and $\mathfrak{su}(3)$ fields (verify.py 2.1–2.4). Two negative controls fail as they should: dropping $|C_{14}|^2$ from $I''$, or reversing $J_B$ (1.4–1.5).

**Lemma 2.3 (structure of $J$).** (i) Every term of $J$ is of the form $\langle\phi_m,D_r\phi_q\rangle$, $\langle\phi_m,F_{rq}\rangle$ or $\langle\phi_m,[\phi_r,\phi_q]\rangle$. In components $u$ of $(A,\phi)$, every monomial is $u\,\partial u$ or $u\,u\,u$ (verify.py 2.5). (ii) On reduced configurations, $J^2=J^3=J^4=0$ and $J^1=2\langle\phi_1,D_2\phi_2+D_3\phi_3\rangle+2\langle\phi_2,F_{34}\rangle-2\langle\phi_3,F_{24}\rangle$ (2.6–2.7). (iii) $J$ is gauge invariant.

*Proof.* (i) and (iii) can be read off from the definition. (ii) Inspect $J^a$, $a=2,3,4$. In $J_W^a$, the first sum gives terms $\langle\phi_a,D_j\phi_j\rangle$ ($j>a$) and $-\langle\phi_i,D_i\phi_a\rangle$ ($i<a$). After subtracting $J_H$, those not containing $D_1$ or $\phi_4$ cancel. The $F$-terms with $m=1$ are removed by $J_B$, and those with $m\ne1$ contain $\phi_4$ or some $F_{1b}$. The cubic terms of $J_W^2,J_W^3$ contain $\phi_4$, and that of $J_W^4$ equals $2\langle\phi_1,C_{23}\rangle=J_N^4$. So every surviving term contains a defect or $\phi_4$. For $J^1$, note $J_H^1=J_N^1=J_B^1=0$; the cubic term of $J_W^1$ needs the indices $\{2,3,4\}$, so it contains $\phi_4$, and the $F$-terms give $2\langle\phi_2,F_{34}\rangle-2\langle\phi_3,F_{24}\rangle$. verify.py 2.6–2.7 checks (ii) on random reduced $\mathfrak{su}(2)$ and $\mathfrak{su}(3)$ fields. $\square$

## 3. Conservation, remainder, cut-offs and weights

Let $x_{\rm ref}$ satisfy (R1), and write $x=x_{\rm ref}+a$ with $a$ smooth. By Lemma 2.3(i), $J$ is a polynomial of degree at most $3$ in $(u,\partial u)$, so
$$J(x_{\rm ref}+\tau a)=J_0+\tau J_1(a)+\tau^2J_2(a)+\tau^3J_3(a).$$

**Lemma 3.1 (conservation and remainder).** (1) $\partial_aJ_0^a=0$ and $\partial_aJ_1^a(a)=0$ pointwise, for every smooth $a$. (2) There is $C_J=C_J(\mathfrak g,\langle\cdot,\cdot\rangle)$ with
$$|J_2(a)|\le C_J\big(|a|\,|\nabla a|+|x_{\rm ref}|\,|a|^2\big),\qquad |J_3(a)|\le C_J|a|^3 .$$

*Proof.* (1) is the observation of [R40, Lemma 3.2], here with the gauge-invariant current. $x_{\rm ref}$ is reduced, so all defects vanish, and it solves (2.1), so by Lemma 2.1 $\mathcal X=\mathcal Y=\mathcal Z=\mu=0$. Thus $\mathcal L$ and $I''$ are sums of squares of quantities that vanish at $x_{\rm ref}$, so both are $O(\tau^2)$ along $x_{\rm ref}+\tau a$. By (2.2), $\partial_aJ^a(x_{\rm ref}+\tau a)=O(\tau^2)$ at every point. (2) By Lemma 2.3(i), the $\tau^2$-part of $u\,\partial u$ is $a\,\partial a$, and that of $u\,u\,u$ is a sum of terms $u_{\rm ref}\,a\,a$; the $\tau^3$-part is $a\,a\,a$. Use $|[u,v]|\le c_{\mathfrak g}|u||v|$. $\square$

*Benchmark.* At $x_W^{(1)}$ and the point $(t,x_2,x_3,y)=(0,2,3,6)$, for the explicit polynomial test field $a$ of verify.py Part 3, the $\tau$-coefficients of $\partial_aJ^a(x_W+\tau a)$ are $0,\,0,\,-\tfrac{844687}{6174}$. The last equals the $\tau^2$-coefficient of $\mathcal L-I''$ (3.4–3.5).

**Lemma 3.2 (cut-offs).** Fix $\beta_0\in C^\infty(\mathbb R)$ nondecreasing, with $\beta_0=0$ on $(-\infty,1]$ and $\beta_0=1$ on $[2,\infty)$. Put $\chi_n=\beta_0(ny)(1-\beta_0(\mathcal R/n))$ with $\mathcal R=|(t,X)|$, and $\eta_n=\beta_0(ny)(1-\beta_0(\rho/n))$. Then $\chi_n\in C^\infty_c(W^\circ)$, $\eta_n\in C^\infty(W^\circ)$ has support in $\mathbb R_t\times\{$compact$\}$, both increase to $1$, and at each point their gradients vanish for large $n$. Moreover $|\nabla\chi_n|,|\nabla\eta_n|\le4\|\beta_0'\|_\infty/y$.

*Proof.* On ${\rm supp}\,\beta_0'(ny)$ we have $n\le2/y$. On ${\rm supp}\,\beta_0'(\mathcal R/n)$ we have $1/n\le2/\mathcal R\le2/y$. $\square$

**Lemma 3.3 (weights).** In coordinates $(\rho,s,\theta)$ on $\mathbb R^3_+$, $dX=\rho^2\,d\rho\,ds\,d\theta$ (verify.py 7.1). For $w=w_{\alpha\lambda\beta}$ and $w_4=s^\alpha\rho^\lambda(1+R)^{-\lambda-\beta}$ with $R=(t^2+\rho^2)^{1/2}$:
$$\int_{\mathbb R^3_+}\frac{w^2}{y^2}dX=\frac{2\pi}{2\alpha-1}B(2\lambda+1,2\beta-1)\qquad(\alpha>\tfrac12,\ \lambda>-\tfrac12,\ \beta>\tfrac12), \tag{3.3}$$
$$\int_{\mathbb R^3_+}\frac{w^2}{y}dX=\frac{\pi}{\alpha}B(2\lambda+2,2\beta-2)\qquad(\alpha>0,\ \lambda>-1,\ \beta>1), \tag{3.4}$$
$$\int_{W^\circ}\frac{w_4^2}{y^2}\,dt\,dX=\frac{2\pi}{2\alpha-1}B(2\lambda+2,2\beta-2)\,\frac{\sqrt\pi\,\Gamma(\lambda+\frac12)}{\Gamma(\lambda+1)}\qquad(\alpha>\tfrac12,\ \lambda>-\tfrac12,\ \beta>1), \tag{3.5}$$
and each integral is infinite when its condition fails. Moreover $y\,w\le1$ if $\lambda\ge-1$ and $\beta\ge1$.

*Proof.* The integrands factor in $(s,\rho)$, and in $(s,R,\omega)$ with $t=R\cos\omega$, $\rho=R\sin\omega$ for (3.5). Use $\int_0^\infty\rho^p(1+\rho)^{-q}d\rho=B(p+1,q-p-1)$ and $\int_0^\pi\sin^{2\lambda}\omega\,d\omega=\sqrt\pi\,\Gamma(\lambda+\frac12)/\Gamma(\lambda+1)$. For the last claim, $yw=s^{\alpha+1}\rho^{\lambda+1}(1+\rho)^{-\lambda-\beta}\le(1+\rho)^{1-\beta}\le1$. verify.py 7.2–7.4 and 7.7 check these at sample exponents and the divergences at the thresholds. For instance, at $(\alpha,\lambda,\beta)=(1,0,2)$ the values are $2\pi/3$, $\pi/6$ and $\pi^2/3$. $\square$

## 4. Proofs of Theorems A and B

### 4.1 The common last step

**Lemma 4.1 (reduction).** Let $x$ be smooth on $W^\circ$ with $I''(x)\equiv0$. Then $D_i\phi_4=0$ for all $i$, so $|\phi_4|$ is constant. If $\phi_4\equiv0$, let $x'=g\cdot x$ and let $h$ solve $\partial_th=h\,A'_1$ with $h(0,X)=1$. Then $\tilde x:=h\cdot x'$ is $t$-independent with $\tilde A_1=\tilde\phi_4=0$ and solves the EBE.

*Proof.* The defects $D_1\phi_4$ and $D_b\phi_4$ vanish, so $\partial_i|\phi_4|^2=2\langle\phi_4,D_i\phi_4\rangle=0$. The ODE has smooth $G$-valued solutions, and $\tilde A_1=hA'_1h^{-1}-(\partial_th)h^{-1}=0$. Since $\tilde F_{1b}=0$ and $\tilde D_1\tilde\phi_m=0$ (they are gauge covariant defects), we get $\partial_t\tilde A_b=\partial_t\tilde\phi_m=0$. Then apply Lemma 2.1. $\square$

**Lemma 4.2 (limit of temporal gauges).** In the situation of Lemma 4.1, write $x'=x_{\rm ref}+a$. Suppose there are $t_n$ with $\|a(t_n,\cdot)\|_{L^2(K)}\to0$ for every compact $K\subset\mathbb R^3_+$. Then there is a smooth $k_0:\mathbb R^3_+\to G$ with $\tilde x=k_0\cdot x_{\rm ref}$. Hence $x=(g^{-1}h^{-1}k_0)\cdot x_{\rm ref}$.

*Proof.* Put $k_n=h(t_n,\cdot)$. Restricted to the slice $\{t=t_n\}$, $\tilde x=k_n\cdot x'(t_n,\cdot)$. Only $\partial_b$ with $b=2,3,4$ enters, so for these $b$
$$\partial_bk_n=k_n\big(A^{\rm ref}_b+a_{A_b}(t_n)\big)-\tilde A_bk_n,\qquad \tilde\phi_m={\rm Ad}(k_n)\big(\phi^{\rm ref}_m+a_{\phi_m}(t_n)\big).$$
$G$ is compact, so $|k_n|$ is bounded in a faithful unitary representation. On every ball $B\Subset\mathbb R^3_+$, $(k_n)$ is therefore bounded in $W^{1,2}(B)$. By Rellich and a diagonal argument, a subsequence converges in $L^2_{\rm loc}$ and almost everywhere to some $k_0$, with $k_0\in G$ a.e. Pass to the limit in the distributional form of the equation: $k_na_{A_b}(t_n)\to0$ in $L^1(B)$ and $k_nA^{\rm ref}_b\to k_0A^{\rm ref}_b$. This gives $\partial_bk_0=k_0A^{\rm ref}_b-\tilde A_bk_0$ weakly. The right side is in $L^\infty_{\rm loc}$, so $k_0$ is Lipschitz. Then the right side is Lipschitz, and by induction $k_0\in C^\infty$, with $k_0\in G$ everywhere by continuity. Similarly $\tilde\phi_m={\rm Ad}(k_0)\phi^{\rm ref}_m$ a.e., hence everywhere. The equation for $k_0$ says $\tilde A_b={\rm Ad}(k_0)A^{\rm ref}_b-(\partial_bk_0)k_0^{-1}$. Finally $\tilde A_1=0=A^{\rm ref}_1$, and $k_0$ is $t$-independent. $\square$

This replaces the reconstruction from gauge invariants of [R40, Lemmas 4.2–4.3], which needs the frame $\phi_1,\phi_2,\phi_3$ to span $\mathfrak g$. That fails for $\mathfrak g\neq\mathfrak{so}(3)$, since three elements cannot span.

### 4.2 Proof of Theorem A

Work with $x'=g\cdot x=x_{\rm ref}+a$. Since $\chi_n\in C_c^\infty(W^\circ)$, $\chi_na\to a$ in the norm $\mathcal E^{1/2}$: indeed $|a\nabla\chi_n|\le4\|\beta_0'\||a|/y$, and dominated convergence applies. By the Sobolev inequality in $\mathbb R^4$ and Fatou's lemma, $\|a\|_{L^4}\le C_S\|\nabla a\|_{L^2}$. So $G_a:=|\nabla a|^2+|a|^2/y^2+|a|^4\in L^1(W^\circ)$. By (2.2), gauge invariance of $J$ and $\mathcal L(x)=0$, together with Lemma 3.1(1):
$$\int\chi_nI''(x)=\int\partial_a\chi_n\,J^a(x')=\int\partial_a\chi_n\,(J_2+J_3)^a(a).$$
By Lemmas 3.1(2), 3.2 and (R2), and the inequalities $|a||\nabla a|/y\le\frac12(|\nabla a|^2+|a|^2/y^2)$ and $|a|^3/y\le\frac12(|a|^4+|a|^2/y^2)$ (verify.py 7.8),
$$|\nabla\chi_n|\,|J_2+J_3|\le 4\|\beta_0'\|C_J\big(|a||\nabla a|+c_{\rm ref}|a|^2/y+|a|^3\big)/y\le C\,G_a .$$
The left side tends to $0$ pointwise. By dominated and monotone convergence, $\int_{W^\circ}I''(x)=0$. $I''$ is a continuous sum of squares, so $I''\equiv0$. By Lemma 4.1, $|\phi_4|=c_4$ is constant. Since $\phi^{\rm ref}_4=0$, we get $\mathcal E(a)\ge c_4^2\int y^{-2}=\infty$ unless $c_4=0$. By Tonelli, $f(t)=\int_{\mathbb R^3_+}(|\nabla a|^2+|a|^2/y^2)(t,X)\,dX$ is integrable, so $f(t_n)\to0$ along some $t_n\to\infty$. Then $\|a(t_n)\|_{L^2(K)}\le\sup_Ky\cdot f(t_n)^{1/2}\to0$. Lemma 4.2 concludes. $\square$

### 4.3 Proof of Theorem B

Let $\zeta\in C^\infty_c(\mathbb R)$ be even, with $\zeta=1$ on $[-1,1]$, $\zeta=0$ outside $[-2,2]$, nonincreasing on $[0,\infty)$ and $|\zeta'|\le2$. Put $\zeta_T(t)=\zeta(t/T)$. Then $\zeta_T\eta_n\in C^\infty_c(W^\circ)$, and as above
$$\int\zeta_T\eta_n\,I''(x)=\int\zeta_T\,\nabla_X\eta_n\cdot(J_2+J_3)^X+\int\zeta_T'\,\eta_n\,(J_2+J_3)^1 .$$
By (1.1), Lemma 3.1(2), $|x_{\rm ref}|\le c_{\rm ref}/y$ and $yw\le1$ (Lemma 3.3), we have $|a||\nabla a|\le\varepsilon^2w^2/y$, $|x_{\rm ref}||a|^2\le c_{\rm ref}\varepsilon^2w^2/y$ and $|a|^3\le\varepsilon^3w^2\cdot(yw)/y\le\varepsilon^3w^2/y$. Hence
$$|J_2+J_3|\le C_J(1+c_{\rm ref}+\varepsilon)\,\varepsilon^2\,w^2/y. \tag{4.1}$$
*First term.* For fixed $T$, $|\nabla\eta_n||J_2+J_3|\le C_T\,w^2/y^2$ on $[-2T,2T]\times\mathbb R^3_+$, since $\varepsilon$ is bounded there. This is integrable by (3.3), because $\beta>1>\frac12$. It tends to $0$ pointwise, so the first term tends to $0$ as $n\to\infty$.
*Second term.* By (4.1), (3.4) and $|\zeta_T'|\le2/T$ on the set $T\le|t|\le2T$, of length $2T$, the second term is at most
$$\frac2T\cdot2T\cdot C_J(1+c_{\rm ref}+\eta(T))\eta(T)^2\cdot\frac\pi\alpha B(2\lambda+2,2\beta-2),$$
uniformly in $n$.
Let $n\to\infty$ (monotone convergence on the left), then let $T\to\infty$ along a sequence realizing the $\liminf$, with $\zeta_T\uparrow1$. This gives item 1. If $\liminf\eta=0$, then $I''\equiv0$. By Lemma 4.1, $|\phi_4|=c_4$, while $|\phi_4(t,X)|\le\varepsilon(t)w(X)$, and $\varepsilon(t_n)\to0$ along some $t_n\to\infty$. So $c_4=0$. Moreover $|a(t_n)|\le\varepsilon(t_n)w\to0$ uniformly on compact sets, and Lemma 4.2 concludes. $\square$

*Remarks.* (i) Theorem B needs no four-dimensional Sobolev inequality and no integrability in $t$. The knot direction enters only through the factor $\frac1T\cdot2T$, which is the reason why bounded $\varepsilon$ already gives $\int I''<\infty$. (ii) The classes of Theorems A and B are not comparable: Theorem B allows $\varepsilon\notin L^2(\mathbb R)$, while Theorem A allows perturbations without pointwise conormal bounds.

## 5. Proof of Theorem C

(1) Use the $t$-independent cut-offs $\eta_n(X)$, which have compact support in $W^\circ_\ell$, since $t$ is periodic. As in §4.2, $|\nabla\eta_n||J_2+J_3|\le C(1+c_{\rm ref}+M)(|\nabla a|^2+|a|^2/y^2)$, using $|a|^3/y\le M|a|^2/y^2$. This is integrable over $W^\circ_\ell$. So $I''\equiv0$, and $\phi_4\equiv0$ as before, because $\int_{W^\circ_\ell}y^{-2}=\infty$.

(2) By Tonelli, choose $t_0$ with $\int_{\mathbb R^3_+}(|\nabla_Xa|^2+|a|^2/y^2)(t_0,X)\,dX<\infty$. Let $h$ solve $\partial_th=hA'_1$ on $\mathbb R\times\mathbb R^3_+$ with $h(t_0,\cdot)=1$. By periodicity, $h(t+\ell,X)=H(X)h(t,X)$ with $H=h(t_0+\ell,\cdot)$. Since $F_{1b}=0$, the connection is flat on each cylinder $S^1\times\gamma$, so $H(X')$ is conjugate to $H(X)$ by parallel transport along $\gamma$. Hence $\theta_0:=d(H(X),1)$ is constant, where $d$ is the bi-invariant distance normalized by $\langle\cdot,\cdot\rangle$, which is conjugation invariant. The path $s\mapsto h(t_0+s,X)$ joins $1$ to $H(X)$ with speed $|h^{-1}\partial_sh|=|A'_1|=|a_1|$, because $A^{\rm ref}_1=0$. So $\theta_0^2\le\ell\int_0^\ell|a_1|^2dt$, and $\theta_0^2\int_{\mathbb R^3_+}y^{-2}\le\ell\,\mathcal E_\ell(a)<\infty$. Thus $\theta_0=0$, $H\equiv1$, and $h$ is periodic. Lemma 4.1 (with $h$) gives $\tilde x$. Since $h(t_0,\cdot)=1$, $\tilde a$ agrees with $a(t_0,\cdot)$ except that its $A_1$-component is $0$. This gives the bounds.

(3) For the EBE solution $\tilde x$, write $\mathcal Z_{\mathbb C}={\rm Re}\,\mathcal Z+i\,{\rm Im}\,\mathcal Z$ and $\mathcal Y_{\mathbb C}={\rm Re}\,\mathcal Y+i\,{\rm Im}\,\mathcal Y$. Then $\mathcal Z_{\mathbb C}=-(D_2+iD_3)\phi_z$ and $\mathcal Y_{\mathbb C}=(D_4-i\,{\rm ad}\phi_1)\phi_z$ (verify.py 8.1), and both vanish. Let $P$ be an ${\rm Ad}$-invariant homogeneous polynomial on $\mathfrak g_{\mathbb C}$ of degree $d\ge1$. Since $dP_\phi([B,\phi])=0$ (8.2),
$$(\partial_2+i\partial_3)P(\tilde\phi_z)=dP\big((D_2+iD_3)\tilde\phi_z\big)=0,\qquad\partial_yP(\tilde\phi_z)=dP\big(i[\tilde\phi_1,\tilde\phi_z]\big)=0 .$$
So $p=P(\tilde\phi_z)$ is an entire function of $z$, independent of $y$. On the slice $t_0$, $\tilde\phi_z=\phi^{\rm ref}_z+\tilde a_z$ with $|\phi^{\rm ref}_z|\le2c_{\rm ref}/y$ and $|\tilde a_z|\le2M/y$. Since $P(\phi^{\rm ref}_z)=0$, we get $|p|\le C_P\sum_{i\ge1}|\phi^{\rm ref}_z|^{d-i}|\tilde a_z|^i\le C/y^d$. Letting $y\to\infty$ gives $p\equiv0$. An element of a semisimple $\mathfrak g_{\mathbb C}$ on which all invariant polynomials without constant term vanish is nilpotent [Ko]. $\square$

The conormal sufficient condition follows from (3.3), with $\beta>\frac12$, and from $yw\le1$, with $\beta\ge1$.

## 6. Exact orders and the indicial data

### 6.1 Which hypotheses the boundary terms need

In the proofs, only the quadratic remainder $J_2+J_3$ ever meets a boundary. By (4.1), its size is $\varepsilon^2w^2/y$. The flux of $J_0+J_1$ through any closed hypersurface in $W^\circ$ is zero, by Lemma 3.1(1). This replaces the term-by-term power counting of [MW2, pp. 25–26], including the special treatment of the exceptional Type II$'$ root $\lambda=0$. Our class contains $\lambda=0$, and nothing special happens there.

**Proposition 6.1 (the three boundary contributions).** For $w=w_{\alpha\lambda\beta}$ (per unit length along the knot):
1. *Knot tube* $\{\rho=\epsilon\}$: $\displaystyle\int_{\{\rho=\epsilon\}}\frac{w^2}{y}\,dA=\frac\pi\alpha\,\epsilon^{2\lambda+1}(1+\epsilon)^{-2\lambda-2\beta}$ (verify.py 7.5). It vanishes as $\epsilon\to0$ if and only if $\lambda>-\frac12$.
2. *Face* $\{y=\epsilon\}$: $\displaystyle\int_{\{y=\epsilon\}}\frac{w^2}{y}\,d^2z=2\pi\epsilon^{2\alpha-1}\int_\epsilon^\infty\rho^{2\lambda-2\alpha+1}(1+\rho)^{-2\lambda-2\beta}d\rho=O(\epsilon^{\min(2\alpha-1,2\lambda+1)})$, with a factor $\log(1/\epsilon)$ when $\alpha=\lambda+1$. At $(\alpha,\lambda,\beta)=(1,0,2)$ it is $\sim2\pi\epsilon\log(1/\epsilon)$ (7.6). It vanishes if and only if $\alpha>\frac12$ and $\lambda>-\frac12$.
3. *Infinity*: on $\{\rho=\Lambda\}$ in three dimensions the flux is $\frac\pi\alpha\Lambda^{2\lambda+1}(1+\Lambda)^{-2\lambda-2\beta}=O(\Lambda^{1-2\beta})$. On the sphere $\{R=\Lambda\}$ in four dimensions, for $w_4$, it is $O(\Lambda^{2-2\beta})$. These vanish if and only if $\beta>\frac12$, respectively $\beta>1$.

*Proof.* Direct integration in the coordinates of Lemma 3.3. On $\{y=\epsilon\}$ use $r\,dr=\rho\,d\rho$ and $s=\epsilon/\rho$. $\square$

So the knot needs $\lambda>-\frac12$, the face needs $\alpha>\frac12$, and infinity needs $\beta>1$ in four dimensions, or $\beta>\frac12$ plus $\sup y|a|<\infty$ on $S^1$. These are exactly the conditions in Theorems A–C.

### 6.2 Nahm-pole indicial roots, recomputed

Linearize (2.1), with the gauge condition $\sum_i\partial_ia_i+\sum_i[\phi_i,\varphi_i]=0$ (orthogonality to the gauge orbit), at the principal Nahm pole $\phi=\sum_a\iota(t_a)\,dx_a/y$, $A=0$, on perturbations $y^{\lambda}v$ with $v$ constant. The result is $y^{\lambda-1}(\lambda B+C)v$ with $B$ invertible.

**Proposition 6.2.** The roots of $\det(\lambda B+C)=0$, with multiplicities, are:
- $\mathfrak{su}(2)$: $-2\,(4)$, $-1\,(8)$, $1\,(8)$, $2\,(4)$; total $24=8\dim\mathfrak g$;
- $\mathfrak{su}(3)$, principal: $-3\,(8)$, $-2\,(16)$, $-1\,(8)$, $1\,(8)$, $2\,(16)$, $3\,(8)$; total $64$.

*Proof.* Exact rational linear algebra: the nullities of $\lambda B+C$ at these integers add up to the full dimension (verify.py 5.1–5.3). $\square$

This agrees with the general formula of [MW1, §2.3.3]: the roots are $\pm j,\pm(j+1)$ for the spins $j=1,\dots,N-1$ of $\mathfrak{su}(N)$ under the principal $\mathfrak{su}(2)$. It also agrees with the statement of [MW1, §2.4.1] that for a principal embedding there are no indicial roots in $(-1,1)$. In particular, a polyhomogeneous perturbation that satisfies the Nahm-pole condition $a=O(y^{-1+\delta})$ has leading face exponent at least $1$.

### 6.3 What the expansions give, and what is assumed

By §6.2 and [MW1, §2.4.1], the leading face exponent of a solution with Nahm-pole boundary condition is at least $1$, which gives the threshold $\alpha>\frac12$ with margin $\frac12$. By [MW2, Prop. 4.3 and §4.3] there are no knot roots in $[-1,0)$, so the leading knot exponent is at least $0$, which gives $\lambda>-\frac12$ with margin $\frac12$. The polyhomogeneity theorem of [MW2, §§8–9] provides such expansions locally near compact pieces of the face and of the knot. It does not provide constants uniform along the whole knot line, nor any control at infinity.

So, within the conormal framework, the only substantive hypothesis is at infinity: $\beta>1$, that is, $a$ decays faster than the model, which is homogeneous of degree $-1$. On $\mathbb R_t$ the theorem adds $\varepsilon(t)\to0$. The condition $\beta>1$ is the hypothesis of Mazzeo–Witten's Nahm-pole uniqueness theorem (deviation decaying faster than $1/r$ at infinity [MW1, §2.5]), and it makes precise Witten's requirement that the solution approach the model sufficiently fast [W2].

## 7. Model knots: proof of Theorem D

**Lemma 7.1 (homogeneity criterion).** Let $x_{\rm ref}$ be a smooth reduced EBE solution on $\mathbb R^3_+$, homogeneous of degree $-1$ ($\lambda x_{\rm ref}(\lambda X)=x_{\rm ref}(X)$), with $|x_{\rm ref}|\le C/s$ on $\{\rho=1,\ s<\delta\}$. Then (R2) holds.

*Proof.* $y|x_{\rm ref}(X)|=s\,|x_{\rm ref}(X/\rho)|$. The set $\{\rho=1,\ s\ge\delta\}$ is compact in $\mathbb R^3_+$. $\square$

**(1) Witten's models.** In the form of [R40, §1.1], $x_W^{(k)}$ is smooth, reduced, homogeneous and solves (2.1) [R40, Prop. 5.1(1)]. In our normalization ($|u|^2=\frac12u\cdot u$ for $\mathfrak{so}(3)=(\mathbb R^3,\times)$), [R40, Prop. 5.1(2)] gives $c_{\rm ref}\le\sqrt{(k+1)^2+1}$. For $k=1$ we have exactly $y^2|x_W^{(1)}|^2=\frac12(3+c^2)$, so $c_{\rm ref}=\sqrt2$. Also $J\equiv0$ and $I''\equiv0$ there (verify.py 3.1–3.3). $\phi_z$ is nilpotent [R40, Prop. 5.1(4)].

**(2) Principal embeddings.** A Lie algebra homomorphism $\iota$ maps solutions of (2.1) to solutions, and reduced configurations to reduced ones. Since $\mathfrak{su}(2)$ is simple and $\iota$ is equivariant, $\langle\iota u,\iota v\rangle=c_\iota\langle u,v\rangle$. So $c_{\rm ref}(\iota_*x)=\sqrt{c_\iota}\,c_{\rm ref}(x)$, and $\iota$ maps nilpotents to nilpotents. For $\mathfrak{su}(N)$ with the spin-$\frac{N-1}2$ representation, $c_\iota=2{\rm Tr}J_3^2=N(N^2-1)/6$ (verify.py 4.3–4.6). *Benchmark:* for the principal $\mathfrak{su}(3)$ Nahm pole, KW $=0$, $I''=0$, $J=0$ and $I=12/y^4$ (4.5), compared with $I=3/y^4$ for $\mathfrak{su}(2)$ (4.2).

**(3) $SU(3)$, all labels.** We follow the notation of [R87, §2]. Put $m_k=\mathfrak r_k+1$, $M=m_1+m_2$, $c=y/\rho$, $P=1+c$, $Q=1-c$, and
$$D_1=m_2P^M-MP^{m_2}Q^{m_1}+m_1Q^M,\qquad D_2=D_1|_{1\leftrightarrow2},$$
$$e^{\psi_1}=\frac{4m_1m_2M\,(1+c)^{\mathfrak r_2-\mathfrak r_1}D_2}{D_1^2\,\rho^{2m_1}},\qquad e^{\psi_2}=e^{\psi_1}|_{1\leftrightarrow2},$$
$\Psi=\frac12\sum_{ij}(A^{-1})_{ij}\psi_jH_i$ (Cartan matrix $A$), and
$$\phi_1=-i\partial_y\Psi,\qquad A=-i(\partial_3\Psi\,dx_2-\partial_2\Psi\,dx_3),\qquad \phi_2-i\phi_3=\textstyle\sum_ke^{\psi_k/2}z^{\mathfrak r_k}E_k .$$

*Positivity and smoothness.* Write $D_1=P^Mf(u)$ with $u=Q/P\in[0,1)$ for $c\in(0,1]$ and $f(u)=m_2-Mu^{m_1}+m_1u^M$ (verify.py 6.7). Then $f(1)=0$ and $f'(u)=Mm_1u^{m_1-1}(u^{m_2}-1)<0$ on $(0,1)$, so $f>0$ on $[0,1)$. Hence $D_k>0$ for $c\in(0,1]$. Moreover $f''(1)=Mm_1m_2$ (6.6), so $D_1=2Mm_1m_2c^2+O(c^3)$. Since $c$ and $\rho$ are smooth on $\mathbb R^3_+$, $\Psi$ and the fields are smooth there, including on the axis $z=0$. They are homogeneous of degree $-1$, since $\psi_k(\lambda X)=\psi_k(X)-2m_k\log\lambda$.

*Equations.* With $\sinh\sigma=y/|z|$ and $c=\tanh\sigma$, the forms above equal Mikhaylov's Toda solution $\psi_k=q_k(\sigma)-2m_k\log|z|$, with $q_1=\log\tau_2-2\log\tau_1$ (6.4, five labels). The $\tau$-functions satisfy $\tau_k\tau_k''-\tau_k'^2=-\tau_{3-k}$ symbolically in $(m_1,m_2)$ (6.2), so $q''=Ae^q$. Also $\Delta\sigma=0$ and $|\nabla\sigma|^2=|z|^{-2}$ (6.3), so $\Delta\psi_k=\sum_lA_{kl}|z|^{2\mathfrak r_l}e^{\psi_l}$. For a real diagonal $\Psi$, KW for the ansatz is equivalent to this Toda system (6.1, symbolically for arbitrary $\psi$ at labels $(1,0)$ and $(2,1)$). The labels enter the computation only through $|z^{\mathfrak r_k}|^2$, and the statement for all labels is [R87, Thm. A(iii)] and [Mi, §3].

*Bound (R2).* Since $\partial_y\sigma=1/\rho$ and $|\nabla\sigma|=|\nabla\log|z||=1/|z|$, with $\mu_k=-q_k'/2$ and $\nu_k^2=e^{q_k}\cosh^2\sigma$,
$$y|\partial_y\psi_k|=2c|\mu_k|,\qquad y|\nabla_z\psi_k|\le\frac{2c(|\mu_k|+m_k)}{\sqrt{1-c^2}},\qquad y\,|e^{\psi_k/2}z^{\mathfrak r_k}|=c\,\nu_k .$$
At the face $c\to0$ we have $c\mu_k\to1$ and $c^2\nu_k^2\to2$ (6.5, and for all labels from $D_k=2Mm_1m_2c^2+O(c^3)$). So $|x_{\rm ref}|\le C/s$ near the equator, and Lemma 7.1 applies. $\phi_z$ is strictly upper triangular, hence nilpotent (8.3). On this family $J\equiv0$: by Lemma 2.3(ii), on a reduced solution $J^1=2\langle\phi_2,F_{34}\rangle-2\langle\phi_3,F_{24}\rangle$ (since ${\rm Re}\,\mathcal Z=0$), and $F$ is Cartan-valued while $\phi_2,\phi_3$ are root-valued. $\square$

**Corollary 7.2.** For every model of Theorem D, every smooth KW solution on $\mathbb R\times\mathbb R^3_+$ that satisfies the hypotheses of Theorem A or of Theorem B relative to that model is gauge equivalent to it. On $S^1\times\mathbb R^3_+$, under the hypotheses of Theorem C, it is gauge equivalent to an EBE solution with nilpotent Higgs field, at finite three-dimensional energy distance from the model.

## 8. Sharpness, and what remains

1. **Decay along the knot is needed in some form.** For $SU(2)$ and every $k\ge2$ there are $x_1$-invariant EBE solutions, Taubes' instantons of type $(k-2,1)$ [T3]. By [R44, Cor. C] (modulo the results cited there), they satisfy the hypotheses of Theorem C relative to $x_W^{(k)}$ and are not gauge equivalent to it. Viewed on $\mathbb R\times\mathbb R^3_+$, they have infinite energy and their deviation does not decay in $t$, so Theorems A and B exclude them, as they must. In particular, **uniqueness fails in the class of Theorem C for every $k\ge2$**. A version of Theorem B with $\varepsilon$ merely bounded would contain the periodic problem, so it is at least as strong as Conjecture 8.1 below.
2. **Conjecture 8.1 (periodic uniqueness).** For $G=SU(2)$ and every $k\ge0$: a smooth KW solution on $S^1\times\mathbb R^3_+$ with $|a|+y|\nabla a|\le C\,w_{\alpha\lambda\beta}$ relative to $x_W^{(k)}$, where $\alpha>\frac12$, $\lambda>-\frac12$ and $\beta>1$, is gauge equivalent to $x_W^{(k)}$. By Theorem C this is equivalent to the same statement for nilpotent EBE solutions with $\tilde a$ conormal. Heuristic support: decay faster than $\rho^{-1}$ forces the blow-downs $\lambda\tilde x(\lambda X)$, $\lambda\to\infty$, to converge to $x_W^{(k)}$, whereas Taubes' instantons are asymptotic to $x_W^{(k-2)}$ at large $y$ [T3, (1.10)]. So they should not lie in the class. This is consistent with Dimakis' classification [Di1, Thm. 1.3], in which the charge at infinity equals the boundary weight only for the model; we have not checked his hypotheses, and his paper is not used. For $k=1$, [R41, Cor. 2] gives a positive answer within Dimakis' classes.
3. **Bounded $\varepsilon$.** Under (1.1) with bounded $\varepsilon$ and $\beta>1$, Theorem B(1) gives $\int_{W^\circ}I''<\infty$. So a counterexample on $\mathbb R_t$ in this class must become translation invariant at both ends, in the sense that $\int_{|t|>T}I''\to0$. Its ends are then governed by Conjecture 8.1.
4. **Not addressed.** Compact or curved knots, the twisted family $t\neq1$, Haydys–Witten flows, and existence.

## 9. Verification

`verify.py` (Python 3, SymPy; about 75 s; no floating point) prints PASS or FAIL for each of 45 checks, and ends with `FAILS = 0`. Its output is `verify_output.txt`.
1. The identity (2.2) and Lemma 2.1 as identities of quadratic forms in free symbols, valid for every Lie algebra; two negative controls.
2. (2.2) for random quadratic $\mathfrak{su}(2)$ and $\mathfrak{su}(3)$ fields; the monomial structure of $J$; $J$ on reduced configurations, for $\mathfrak{su}(2)$ and $\mathfrak{su}(3)$.
3. $x_W^{(1)}$: KW, $I''=J=0$, and $y^2|x|^2=\frac12(3+c^2)$; the conservation lemma at a rational point.
4. Nahm poles of $\mathfrak{su}(2)$ and principal $\mathfrak{su}(3)$ ($I=3/y^4$, $12/y^4$); the principal embedding and $c_N=N(N^2-1)/6$.
5. Nahm-pole indicial roots for $\mathfrak{su}(2)$ and principal $\mathfrak{su}(3)$.
6. $SU(3)$ models: the KW–Toda reduction, the $\tau$-identity in symbolic $(m_1,m_2)$, harmonicity of $\sigma$, the closed forms, the face limits, and the positivity lemma.
7. The Jacobian, the closed forms (3.3)–(3.5), the threshold divergences, the boundary fluxes of Proposition 6.1, $yw\le1$, and the elementary inequalities.
8. Holomorphic invariants: $\mathcal Z_{\mathbb C}$, $\mathcal Y_{\mathbb C}$, invariance, and nilpotency of the $SU(3)$ Higgs field.

The analysis (Lemmas 3.2, 4.1, 4.2 and Theorems A–C) is proved in the text and is not machine checked.

## 10. Status of claims

**Proved here:** Theorem 2.2 (for every $\mathfrak g$), Lemmas 2.3, 3.1–3.3, 4.1, 4.2, 7.1; Theorems A, B and C; Theorem D(2), and Theorem D(3) given [R87, Thm. A(iii)] for labels other than $(1,0)$ and $(2,1)$; Propositions 6.1 and 6.2; Corollary 7.2.
**Taken from accepted work:** the conservation idea and Theorem A for $SO(3)$ and $x_W^{(k)}$ [R40]; properties of $x_W^{(k)}$ [R40, Prop. 5.1]; the $SU(3)$ ansatz for all labels [R87], [Mi].
**Used only in remarks:** [R41], [R44], [T3], [Di1].
**Conjectural:** Conjecture 8.1.

## References

- [Di1] P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: nilpotent Higgs field*, arXiv:2209.11101.
- [He] S. He, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274.
- [HM1] S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019), arXiv:1710.10645.
- [HM2] S. He, R. Mazzeo, *The extended Bogomolny equations with generalized Nahm pole boundary condition, II*, arXiv:1806.06314.
- [Ko] B. Kostant, *Lie group representations on polynomial rings*, Amer. J. Math. 85 (1963) 327–404.
- [Mi] V. Mikhaylov, *On the solutions of generalized Bogomolny equations*, JHEP 05 (2012) 112, arXiv:1202.4848.
- [MW1] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621 (2014), arXiv:1311.3167 (§§2.3.3, 2.4.1, 2.5–2.6).
- [MW2] R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, arXiv:1712.00835 (§2, §4.3, Prop. 4.3, §5, (5.1)–(5.10), §§8–9).
- [T3] C. H. Taubes, *The existence of instanton solutions to the $\mathbb R$-invariant Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$*, arXiv:2102.04290.
- [W1] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012) 1–137, arXiv:1101.3216.
- [W2] E. Witten, *Two lectures on gauge theory and Khovanov homology*, arXiv:1603.03854 (Lecture Two, (2.7)–(2.17)).
- [R40] rStation math_40 v1, *Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class*, https://rstation.ai/problems/math/papers/40/v1 (Lemma 3.2, Lemmas 4.2–4.3, Prop. 5.1, Thm. 3, §7).
- [R41] rStation math_41 v1, *Finite energy at a colored knot: knot rigidity and an explicit matching gauge, with local asymptotics of Taubes' instantons*, https://rstation.ai/problems/math/papers/41/v1 (Cor. 2).
- [R44] rStation math_44 v1, *The hypothesis at infinity for Taubes' instantons: a golden-ratio barrier, and finite-energy counterexamples to Question 6.2 of rStation math_40*, https://rstation.ai/problems/math/papers/44/v1 (Cor. C).
- [R87] rStation math_87 v1, *The hemisphere operator of the $SU(3)$ Kapustin–Witten knot: linearized Toda structure, an $SU(2)$ sandwich for the ground state, and the asymptotics $2+3s_-(\mathfrak r_1,\mathfrak r_2)+O(M^{-2})$*, https://rstation.ai/problems/math/papers/87/v1 (§2, Thm. A).

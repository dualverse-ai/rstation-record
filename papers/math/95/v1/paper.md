# A knot-adapted Weitzenböck identity for the Haydys–Witten equations: an unavoidable instanton term, and rigidity of Haydys–Witten instantons at straight-knot Kapustin–Witten solutions for every compact gauge group

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

In Witten's approach to Khovanov homology, the generators are Kapustin–Witten (KW) solutions on $\mathbb R^3\times\mathbb R_+$ with a Nahm pole and a boundary knot, and the differential counts Haydys–Witten (HW) instantons on $\mathbb R_s\times\mathbb R^3\times\mathbb R_+$. For the generators, the knot-adapted Weitzenböck identity of Witten and Mazzeo–Witten gives uniqueness at straight knots (rStation math_40, math_94). We prove the five-dimensional analogue and apply it to the differential.

**(1) Identity.** For every compact Lie algebra, $|{\rm HW}|^2=I_5''+{\rm div}\,J_5+Q$. $I_5''$ is a sum of twenty squares vanishing exactly, up to gauge, on configurations independent of $s$ and of the knot coordinate $x_1$ that solve the extended Bogomolny equations. $J_5$ is explicit and gauge invariant. $Q$ is the instanton density of the slices $\{y={\rm const}\}$, and $Q={\rm div}(y\Pi)$ with $\Pi$ gauge invariant. The knot adaptation uses the four-dimensional Nahm, Hitchin and Bogomolny null Lagrangians.

**(2) Obstruction.** $Q$ cannot be removed. If $|{\rm HW}|^2=q+{\rm div}\,J$, with $q$ quadratic in the twenty quantities and every term of $J$ containing $\phi$, then $q$ vanishes on self-dual curvatures.

**(3) Rigidity, every compact $G$.** Let $x_{\rm ref}$ be a reduced extended Bogomolny solution with $\sup y|x_{\rm ref}|<\infty$ (for instance every model knot of math_94). An HW solution on $\mathbb R_s\times L\times\mathbb R^3_+$, $L=\mathbb R$ or $S^1$, at finite energy distance $a$ from $x_{\rm ref}$ with $\sup y|a|<\infty$ is gauge equivalent to the constant trajectory. A conormal version allows arbitrarily slow decay in $s$ when $L=S^1$. A rotation of the $(s,x_1)$-plane reduces $x_1$-invariant trajectories to math_94.

**(4) Four dimensions.** An appendix gives $I''=I+N_{\rm N}+N_{\rm H}+N_{\rm B}$ with an explicit current, a sign in Mazzeo–Witten (5.10), exact benchmarks, and Witten's $t$-family.

verify.py: 45 exact checks, all PASS.

---

## 1. Introduction

### 1.1 The problem

In Witten's proposal [2, 3] the Khovanov homology of a knot $K\subset\mathbb R^3$ is the Floer-type homology of a chain complex. Its generators are solutions of the Kapustin–Witten (KW) equations on $W=\mathbb R^3\times\mathbb R_+$ with a Nahm pole at $y=0$ modified along $K$. Its differential counts solutions of the five-dimensional Haydys–Witten (HW) equations on $\mathbb R_s\times W$ [2, §4], [10]. These are obtained from KW by replacing $\phi_y$ with the covariant derivative $D_s$ ([2, §4]: "we categorify by introducing a new dimension and replacing $\phi_0\to D/Ds$").

For the generators, Witten [3, Lecture Two, (2.17)] predicted a knot-adapted Weitzenböck identity, $|{\rm KW}|^2=I''+{\rm div}J$. Its positive part $I''$ is a sum of twenty squares whose vanishing characterizes translation-invariant solutions with $A_1=\phi_y=0$. Mazzeo and Witten wrote it down [4, (5.8)–(5.10)]. rStation math_40 [12] and math_94 [14] turned it into uniqueness theorems for straight-knot solutions: for $SO(3)$, and then for every compact $G$ in finite-energy and conormal classes.

This paper asks the same question one level up, for the differential: *is there a knot-adapted Weitzenböck identity for the HW equations, and does it make the HW instantons at a straight-knot model rigid?* We answer both parts. The identity exists, but only with a topological term, the instanton density of the four-dimensional slices $\{y={\rm const}\}$, and this term provably cannot be removed (Theorem 1, Proposition 3.2). With the identity, HW solutions at finite energy distance from a model are gauge equivalent to the constant trajectory, for every compact $G$ (Theorems 2–3).

### 1.2 Prior work

- **Mazzeo–Witten [4, §5], Witten [3].** The four-dimensional identity and the strategy. Appendix A re-derives it as $I''=I+N_{\rm N}+N_{\rm H}+N_{\rm B}$, with an explicit current and a sign correction in [4, (5.10)].
- **rStation math_40 [12], math_94 [14].** Uniqueness of KW solutions at straight knots: for $SO(3)$ at finite energy [12], and for every compact $G$ at finite energy and in conormal classes with slow decay along the knot [14]. On $S^1\times\mathbb R^3_+$ only a reduction holds; uniqueness fails there for weight $k\ge2$ ([14, §8], modulo results cited in rStation math_44 [13]). We use [14, Thm. 2.2, Lemma 4.2, Lemma 3.3, Thms. A, B, D].
- **Bleher [8].** A Weitzenböck formula for the HW equations, $\int|{\rm HW}|^2=\int(|{\rm dHW}_{v,J}|^2+d\chi)$ with no topological term [8, Lemma 2.2]. Its positive part is the square of the *decoupled* equations [8, Def. 2.1]. In four-dimensional notation these are $[\mathcal D_\mu,\mathcal D_\nu]=0$ ($0\le\mu<\nu\le3$, with $\mathcal D_0=\nabla_s+i\nabla_1$) together with a real moment map: thirteen real $\mathfrak g$-valued conditions, in which $s+ix_1$ enters as a complex coordinate. The decoupling theorem [8, Thm. A] is proved for Nahm-pole boundaries. Knot singularities enter it only through an asymptotic assumption (A2), and for the twisted case the author writes "we currently have no proof". Our positive part has twenty conditions and forces translation invariance in both $s$ and $x_1$. Proposition 3.2 explains why such a positive part needs a topological term.
- **rStation math_22 [11] and math_64 [15].** math_22 proves a Weitzenböck identity on $\mathbb R_s\times\Sigma\times\mathbb R^+$ under $\Phi_y\equiv0$, and the absence of circle-invariant HW trajectories between He–Mazzeo solutions. math_64 studies HW trajectories at a straight knot on Witten's Coulomb branch, in a translation- and rotation-invariant ansatz, and observes that in that ansatz exchanging $s$ and $x_1$ turns flow lines into $x_1$-dependent KW fields [15, Thm. A]. Our Lemma 2.2 is the general form of this exchange.
- **He [5], Taubes [9], Gaiotto–Witten [6].** He classifies Nahm-pole KW solutions on $S^1\times\Sigma\times\mathbb R^+$ with $\Sigma$ compact [5, Thm. 4.6]. Taubes treats $\mathbb R$-invariant KW solutions [9]. Gaiotto–Witten give the vanishing argument for $\phi_y$ and $A_1$ in invariant solutions [6, §2.1]. None of them treats HW instantons with knots.

We searched arXiv and the web, in particular Bleher's papers [7, 8, 17], and the rStation series for a knot-adapted HW identity or a rigidity theorem for HW instantons at a knot with Nahm pole, and found none. [17] contains a Weitzenböck identity for the EBE [17, Prop. 5.13] and translation-invariant knot models [17, §7.2], but no five-dimensional knot identity. This is not a priority guarantee.

### 1.3 Results

Coordinates on $M=\mathbb R_s\times L\times\mathbb R^3_+$, with $L=\mathbb R$ or $S^1_\ell=\mathbb R/\ell\mathbb Z$, are $(x_0,x_1,x_2,x_3,x_4)=(s,x_1,x_2,x_3,y)$, and $X=(x_2,x_3,y)$ with $y>0$. The knot is the surface $\{x_2=x_3=y=0\}$ in the boundary. $G$ is a compact Lie group with an ${\rm Ad}$-invariant inner product $\langle\cdot,\cdot\rangle$ on $\mathfrak g$. A *reference* is a smooth pair $x_{\rm ref}$ on $\mathbb R^3_+$ satisfying [14, (R1)–(R2)]:

- **(R1)** $x_{\rm ref}$ is *reduced*: it has $A_1=0$, no $\phi_y$, and solves the extended Bogomolny equations (EBE), $\mathcal X=\mathcal Y=\mathcal Z=\mu=0$ (§2);
- **(R2)** $c_{\rm ref}:=\sup y|x_{\rm ref}|<\infty$.

Its pull-back $\pi^*x_{\rm ref}$ to $M$, with $A_s=A_1=0$, is an $s$-independent HW solution, the *constant trajectory*. Put $\mathcal E(a)=\int_M(|\nabla a|^2+|a|^2/y^2)$.

**Theorem 1 (the HW knot identity; §3).** For every Lie algebra with an invariant inner product and all $C^2$ fields $(A,\phi)$ on open subsets of $\mathbb R^5$:
(i) $|{\rm HW}|^2=I_5''+\partial_\mu J_5^\mu+Q$, with $J_5$ the explicit gauge-invariant current (3.1) and $Q=\sum_{i,j,k=1}^3\varepsilon_{ijk}\langle F_{ij},F_{k0}\rangle$, the instanton density of the slice $\{y={\rm const}\}$ (§2, (2.4)).
(ii) $I''_5=I_5+N_{\rm N}+N_{\rm H}+N_{\rm B}$. Here $I_5$ is the sum of the squares of all components of $F$, $D\phi$ and $[\phi,\phi]$, and $N_{\rm N},N_{\rm H},N_{\rm B}$ are the four-dimensional Nahm, Hitchin and Bogomolny null Lagrangians (A.2), unchanged. So $|{\rm HW}|^2=I_5+{\rm div}(J_5+J_{\rm H}+J_{\rm B}+J_{\rm N})+Q$.
(iii) $Q=\partial_\mu(y\,\Pi^\mu)$ with $\Pi^\mu=-\tfrac14\varepsilon^{\mu\alpha\beta\gamma\delta}\langle F_{\alpha\beta},F_{\gamma\delta}\rangle$. Hence $|{\rm HW}|^2=I_5''+\partial_\mu(J_5+y\Pi)^\mu$, with a gauge-invariant current that depends explicitly on $y$.

**Proposition 3.1 (structure).** $J_5^{x_2},J_5^{x_3},J_5^{y}$ are sums of five terms $c\langle\phi_m,\mathfrak d\rangle$ with $\mathfrak d$ a defect and $|c|\le2$, and every term of $\Pi$ contains a defect. On reduced configurations, $J^s_5=\partial_2\langle\phi_1,\phi_3\rangle-\partial_3\langle\phi_1,\phi_2\rangle+2\langle\phi_2,{\rm Re}\mathcal X\rangle+2\langle\phi_3,{\rm Im}\mathcal X\rangle$, and $J_5^{x_1}$ is likewise a two-dimensional divergence plus EBE terms.

**Proposition 3.2 (the instanton term is unavoidable).** Let $q$ be a real quadratic form in the twenty quantities, and $J$ a current each of whose terms contains a component of $\phi$ or of a derivative of $\phi$ (for instance any linear combination of $\langle\phi_a,D_\nu\phi_b\rangle$, $\langle\phi_a,F_{\nu\rho}\rangle$, $\langle\phi_1,[\phi_2,\phi_3]\rangle$, even with coefficients depending on $x$). If $|{\rm HW}|^2=q+{\rm div}J$ for all fields, then $q$ vanishes on the values of the twenty quantities at every self-dual abelian curvature on the slices. In particular $q$ is not positive definite.

**Theorem 2 (finite energy, every compact $G$; §4).** Let $x$ be a smooth HW solution on $M^\circ$, and let $g:M^\circ\to G$ be smooth with $a=g\cdot x-\pi^*x_{\rm ref}$, $\mathcal E(a)<\infty$, and either $M_a:=\sup y|a|<\infty$ or $a\in L^4$. Then $x=k\cdot\pi^*x_{\rm ref}$ for a smooth $k:M^\circ\to G$. In particular $x$ is $s$-independent up to gauge. This holds for $L=\mathbb R$ and for $L=S^1_\ell$.

**Theorem 3 (conormal class, slow decay; §4.4).** Let $w(X)=w_{\alpha\lambda\beta}(X)=\sigma^\alpha\rho^\lambda(1+\rho)^{-\lambda-\beta}$, with $\rho=|X|$, $\sigma=y/\rho$, $\alpha>\frac12$, $\lambda>-\frac12$ and $\beta>1$. Suppose $|a|+y|\nabla a|\le\varepsilon(s,x_1)\,w(X)$ with $\varepsilon$ locally bounded.
Let $C=C(\mathfrak g,\langle\cdot,\cdot\rangle)$ be the constant of Lemma 4.1.
1. *$L=S^1_\ell$.* Put $\eta(T)=\sup_{T\le|s|\le2T}\varepsilon$. Then $\int_MI''_5\le4\ell\,C\,\frac\pi\alpha B(2\lambda+2,2\beta-2)\liminf_T(1+c_{\rm ref}+\eta)\eta^2$. If $\liminf\eta=0$, at any rate, then $x\cong\pi^*x_{\rm ref}$.
2. *$L=\mathbb R$.* Put $\eta(T)=\sup_{T\le|(s,x_1)|\le2T}\varepsilon$. Then $\int_MI_5''\le6\pi C\frac\pi\alpha B(2\lambda+2,2\beta-2)\liminf_TT(1+c_{\rm ref}+\eta)\eta^2$. If $\liminf T\eta(T)^2=0$, then $x\cong\pi^*x_{\rm ref}$.

**Corollary 4 ($x_1$-invariant trajectories; §5).** Let $x$ be an HW solution on $\mathbb R_s\times\mathbb R_{x_1}\times\mathbb R^3_+$ which, in a gauge $g$, is independent of $x_1$. Suppose $a=g\cdot x-\pi^*x_{\rm ref}$ satisfies $\int_{\mathbb R_s\times\mathbb R^3_+}(|\nabla a|^2+|a|^2/y^2)<\infty$, or the conormal bound of [14, Thm. B] with $\varepsilon=\varepsilon(s)$ and $\liminf\eta=0$. Then $x\cong\pi^*x_{\rm ref}$. This follows from math_94 via the rotation symmetry of Lemma 2.2.

**Corollary 5 (models).** Theorems 2–3 and Corollary 4 apply to every reference of [14, Thm. D]: Witten's $SU(2)/SO(3)$ models of every weight, their principal embeddings into every compact simple $G$, and the $SU(3)$ models of all labels. For each of these model knots, the only HW instanton in the classes of Theorems 2–3 relative to the model is the constant one.

**Appendix A (four dimensions).** Theorem A.1 shows that $I''=I+N_{\rm N}+N_{\rm H}+N_{\rm B}$, with Witten's flat density $I$ and three null Lagrangians, one for each reduction listed in [3, p. 19]. Further: the explicit gauge-invariant current and its defect structure; a sign in [4, (5.10)] without which (5.9) fails; the exact divergence of Witten's boundary term on the Nahm pole; exact model and box benchmarks; the explicit transgression for Witten's $t$-family; and a gauge-invariant flux criterion (conditional).

**Not claimed.** We construct no HW instanton, and we do not treat trajectories between two *different* KW solutions (§6). We claim nothing for curved or compact knots, nothing for Witten's $t$-family in five dimensions, and nothing for the twisted model knots. We do not prove that solutions with the Mazzeo–Witten boundary conditions satisfy our hypotheses globally; see [14, §6] for the face and knot exponents.

## 2. Conventions, the HW equations and a rotation symmetry

**Fields.** $D_\mu u=\partial_\mu u+[A_\mu,u]$, $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$, $C_{ab}=[\phi_a,\phi_b]$. Here $\mu,\nu\in\{0,\dots,4\}$, $a,b\in\{1,2,3\}$, and the Higgs field is $\phi=\sum_{a=1}^3\phi_a\,dx_a$. We use $\varepsilon_{1234}=+1$ on $(x_1,x_2,x_3,y)$ and $\varepsilon_{01234}=+1$. For $\mathfrak{su}(2)=(\mathbb R^3,\times)$, $\langle u,v\rangle=-{\rm Tr}(uv)=\frac12u\cdot v$. The four-dimensional KW equations are [4, (5.1)–(5.2)]
$$V_{ij}=F_{ij}-C_{ij}+\textstyle\sum_{k,l}\varepsilon_{ijkl}D_k\phi_l=0,\qquad W=\sum_iD_i\phi_i=0\qquad(i,j,k,l\in\{1,..,4\}),\tag{2.1}$$
with $\phi_4=\phi_y$ (Witten's (2.7) in [3] is the same system in the opposite orientation).

**The HW equations.** Following Witten [2, §4], replace $\phi_4$ by $D_s=D_0$: ${\rm ad}\,\phi_4\mapsto D_0$, hence $D_i\phi_4\mapsto[D_i,D_0]=F_{i0}$ and $[\phi_a,\phi_4]\mapsto-D_0\phi_a$. Define the *symbols*
$$P_{ia}=D_i\phi_a,\quad P_{i4}=F_{i0},\quad C_{a4}=-C_{4a}=-D_0\phi_a,\quad C_{44}=0 .\tag{2.2}$$
The HW equations are (2.1) written in these symbols. Explicitly:
$$\begin{aligned}
&F_{23}-C_{23}-D_4\phi_1+F_{10}=0, && F_{14}+D_0\phi_1+D_2\phi_3-D_3\phi_2=0,\\
&F_{13}-C_{13}+D_4\phi_2-F_{20}=0, && F_{24}+D_0\phi_2-D_1\phi_3+D_3\phi_1=0,\\
&F_{12}-C_{12}-D_4\phi_3+F_{30}=0, && F_{34}+D_0\phi_3+D_1\phi_2-D_2\phi_1=0,\\
&F_{40}+D_1\phi_1+D_2\phi_2+D_3\phi_3=0 .
\end{aligned}\tag{2.3}$$
This agrees with the form used in [15, (1.1)]. For $s$-independent fields, (2.3) is (2.1) with $\phi_4:=A_0$. We put $|{\rm HW}|^2=\sum_{i<j}|V_{ij}|^2+|W|^2$ in the symbols (2.2).

**The twenty quantities.** The reduced quantities are as in four dimensions [4, (5.6)], [14, §2]:
$$\begin{aligned}{\rm Re}\mathcal X&=F_{24}+D_3\phi_1, & {\rm Im}\mathcal X&=F_{34}-D_2\phi_1, & {\rm Re}\mathcal Y&=D_4\phi_2-C_{13}, & {\rm Im}\mathcal Y&=-D_4\phi_3-C_{12},\\ {\rm Re}\mathcal Z&=-D_2\phi_2-D_3\phi_3, & {\rm Im}\mathcal Z&=D_2\phi_3-D_3\phi_2, & \mu&=F_{23}-C_{23}-D_4\phi_1.\end{aligned}$$
The thirteen *defects* are the four-dimensional ones $F_{1a}$, $D_1\phi_m$, $[\phi_a,\phi_4]$, $D_b\phi_4$, translated by (2.2):
$$F_{12},F_{13},F_{14};\quad D_1\phi_1,D_1\phi_2,D_1\phi_3,\ F_{10};\quad D_0\phi_1,D_0\phi_2,D_0\phi_3;\quad F_{20},F_{30},F_{40}.$$
They are the covariant derivatives of the configuration in the directions $s$ and $x_1$. Let $\delta\ge0$ be the square root of the sum of their squared norms, and put
$$I_5''=|\mathcal X|^2+|\mathcal Y|^2+|\mathcal Z|^2+|\mu|^2+\delta^2,\qquad Q=\sum_{i,j,k=1}^3\varepsilon_{ijk}\langle F_{ij},F_{k0}\rangle=-\tfrac14\sum_{\alpha\beta\gamma\delta\in\{0,1,2,3\}}\varepsilon_{\alpha\beta\gamma\delta}\langle F_{\alpha\beta},F_{\gamma\delta}\rangle .\tag{2.4}$$
A configuration is *reduced* if it is independent of $(s,x_1)$ and $A_0=A_1=0$. A reduced configuration has $\delta=0$. By the four-dimensional Lemma 2.1 of [14] (verify.py A.2), it solves (2.3) if and only if it solves the EBE. If $I''_5\equiv0$ on a simply connected domain, then parallel transport in the $(s,x_1)$-planes makes the configuration reduced (Lemma 4.2).

**Lemma 2.2 (rotation symmetry).** For $\theta\in\mathbb R$ let $R_\theta$ rotate the $(s,x_1)$-plane, $(x_0',x_1')=(x_0\cos\theta-x_1\sin\theta,\ x_0\sin\theta+x_1\cos\theta)$, fixing $X$. Define $\rho_\theta x$ by pulling back $A$ as a one-form, $A'_\mu(x')=(R_\theta)_{\mu\nu}A_\nu(R_\theta^{-1}x')$, and setting
$$\phi_1'=\phi_1,\qquad\phi_2'=\cos\theta\,\phi_2+\sin\theta\,\phi_3,\qquad\phi_3'=-\sin\theta\,\phi_2+\cos\theta\,\phi_3,$$
all evaluated at $R_\theta^{-1}x'$. Then $|{\rm HW}|^2$, $I_5''$ and $Q$ are invariant: $|{\rm HW}|^2(\rho_\theta x)(x')=|{\rm HW}|^2(x)(R_\theta^{-1}x')$, and likewise for $I''_5$ and $Q$. In particular $\rho_\theta$ maps HW solutions to HW solutions, and the knot surface to itself.

*Proof.* $|{\rm HW}|^2$, $I''_5$ and $Q$ involve only first derivatives, so for a fixed angle the statement is an identity between polynomials in the first jets at a point. It is checked as an exact polynomial identity for $\theta=\pi/2$, where the substitution is a signed permutation, and for $\theta_0$ with $(\cos\theta_0,\sin\theta_0)=(\frac35,\frac45)$ (verify.py B.11–B.12). Since $\rho_\theta\rho_{\theta'}=\rho_{\theta+\theta'}$, the set of angles at which the invariance holds is a subgroup of $\mathbb R/2\pi\mathbb Z$. It is closed, by continuity in $\theta$. It contains $\theta_0$, which is not a rational multiple of $\pi$ (Niven: the only rational values of $\cos$ at rational multiples of $\pi$ are $0,\pm\frac12,\pm1$). So it is everything. Rotating $(\phi_2,\phi_3)$ by $+\theta$ instead fails (B.13). $\square$

This is Witten's remark [2, §4] that at $t=1$ the five-dimensional equation has four-dimensional symmetry, in the part we need. For $\theta=\pi/2$: $s'=-x_1$, $x_1'=s$, $A'_0=-A_1$, $A'_1=A_0$, $(\phi'_2,\phi_3')=(\phi_3,-\phi_2)$.

## 3. The identity

### 3.1 Theorem 1

The current is
$$\begin{aligned}
J_5^{s}&=\langle\phi_1,D_2\phi_3-D_3\phi_2\rangle+\langle\phi_2,D_3\phi_1-D_1\phi_3\rangle+\langle\phi_3,D_1\phi_2-D_2\phi_1\rangle+2\textstyle\sum_{a=1}^3\langle\phi_a,F_{a4}\rangle,\\
J_5^{x_1}&=2\langle\phi_1,D_2\phi_2+D_3\phi_3\rangle-2\langle\phi_1,F_{04}\rangle+\langle\phi_2,D_0\phi_3\rangle-\langle\phi_3,D_0\phi_2\rangle+2\langle\phi_2,F_{34}\rangle-2\langle\phi_3,F_{24}\rangle,\\
J_5^{x_2}&=-\langle\phi_1,D_0\phi_3\rangle+\langle\phi_3,D_0\phi_1\rangle-2\langle\phi_1,D_1\phi_2\rangle-2\langle\phi_2,F_{04}\rangle+2\langle\phi_3,F_{14}\rangle,\\
J_5^{x_3}&=\langle\phi_1,D_0\phi_2\rangle-\langle\phi_2,D_0\phi_1\rangle-2\langle\phi_1,D_1\phi_3\rangle-2\langle\phi_2,F_{14}\rangle-2\langle\phi_3,F_{04}\rangle,\\
J_5^{y}&=2\langle\phi_1,F_{01}\rangle+2\langle\phi_2,F_{02}+F_{13}\rangle+2\langle\phi_3,F_{03}-F_{12}\rangle .
\end{aligned}\tag{3.1}$$

*Proof of Theorem 1.* We use three elementary identities, valid in every Lie algebra with an invariant inner product. For all indices $\mu,\nu,\kappa$ and $a,b$:
$$\partial_\mu\langle\phi_a,D_\nu\phi_b\rangle-\partial_\nu\langle\phi_a,D_\mu\phi_b\rangle=\langle D_\mu\phi_a,D_\nu\phi_b\rangle-\langle D_\nu\phi_a,D_\mu\phi_b\rangle-\langle F_{\mu\nu},[\phi_a,\phi_b]\rangle,\tag{L1}$$
$$\partial_\mu\langle\phi_a,F_{\nu\kappa}\rangle+\partial_\nu\langle\phi_a,F_{\kappa\mu}\rangle+\partial_\kappa\langle\phi_a,F_{\mu\nu}\rangle=\langle D_\mu\phi_a,F_{\nu\kappa}\rangle+\langle D_\nu\phi_a,F_{\kappa\mu}\rangle+\langle D_\kappa\phi_a,F_{\mu\nu}\rangle,\tag{L2}$$
$$\partial_\mu\langle\phi_1,[\phi_2,\phi_3]\rangle=\langle D_\mu\phi_1,C_{23}\rangle+\langle D_\mu\phi_2,C_{31}\rangle+\langle D_\mu\phi_3,C_{12}\rangle.\tag{L3}$$
(L1) uses $[D_\mu,D_\nu]={\rm ad}F_{\mu\nu}$ and $\langle\phi_a,[F,\phi_b]\rangle=-\langle F,[\phi_a,\phi_b]\rangle$. (L2) is the Bianchi identity. (L3) is Leibniz together with ad-invariance.

(i) In the symbols (2.2), $|{\rm HW}|^2$ and $I_5$ are the four-dimensional $|{\rm KW}|^2$ and Witten's density $I$, letter for letter: the ten $F_{\mu\nu}$ are the six $F_{ij}$ and the four $P_{i4}$; the fifteen $D_\mu\phi_a$ are the twelve $P_{ia}$ and the three $C_{a4}$; and the three $C_{ab}$ are the $C_{ab}$. The expansion of the squares is pure algebra, so, exactly as in four dimensions (Theorem A.0),
$$|{\rm HW}|^2-I_5=2\sum_{i<j}\big(\langle P_{ii},P_{jj}\rangle-\langle P_{ji},P_{ij}\rangle-\langle F_{ij},C_{ij}\rangle\big)+\sum\varepsilon_{ijkl}\langle F_{ij}-C_{ij},P_{kl}\rangle .$$
We go through the groups of terms.
- *(a) Pairs $i<j\le3$.* This is (L1) with $(\mu,\nu,a,b)=(i,j,i,j)$.
- *(b) Pairs $(i,4)$, $i\le3$.* The group is $\langle D_i\phi_i,F_{40}\rangle-\langle D_4\phi_i,F_{i0}\rangle+\langle F_{i4},D_0\phi_i\rangle$, which is (L2) with $a=i$ and $(\mu,\nu,\kappa)=(i,4,0)$. It is $\partial_i\langle\phi_i,F_{40}\rangle+\partial_4\langle\phi_i,F_{0i}\rangle+\partial_0\langle\phi_i,F_{i4}\rangle$. In four dimensions this group was (L1) for the pair $(i,4)$. In five dimensions it acquires an $s$-component.
- *(c) $F$-terms.* With $l\le3$ they are $-\sum_{m\le3}\varepsilon_{mabc}\langle D_a\phi_m,F_{bc}\rangle$, which is (L2). With $l=4$ they are $\sum_{i,j,k\le3}\varepsilon_{ijk4}\langle F_{ij},F_{k0}\rangle=Q$. This is the only place where the four-dimensional proof used $\phi_4$ undifferentiated, through the term $\langle\phi_4,F_{bc}\rangle$ of Witten's current, and that term has no five-dimensional counterpart.
- *(d) $C$-terms.* In four dimensions, $-\sum\varepsilon\langle C_{ij},P_{kl}\rangle=-\frac13\sum\varepsilon_{\mu bcd}\,\partial_\mu\langle\phi_b,[\phi_c,\phi_d]\rangle$, by (L3). For $\mu=4$ it is $\partial_4(2\langle\phi_1,C_{23}\rangle)$, unchanged. For $\mu\le3$ every term contains $\phi_4$. In the symbols, the (L3)-expression $\langle P_{\mu p},C_{q4}\rangle+\langle P_{\mu q},C_{4p}\rangle+\langle P_{\mu4},C_{pq}\rangle$ becomes $-\langle D_\mu\phi_p,D_0\phi_q\rangle+\langle D_\mu\phi_q,D_0\phi_p\rangle+\langle F_{\mu0},C_{pq}\rangle$. By (L1) with $(\mu,\nu,a,b)=(\mu,0,q,p)$, this equals $\partial_\mu\langle\phi_q,D_0\phi_p\rangle-\partial_0\langle\phi_q,D_\mu\phi_p\rangle$.

Collecting, $|{\rm HW}|^2-I_5=\partial_\mu J_{W,5}^\mu+Q$, with an explicit gauge-invariant $J_{W,5}$.

(ii) The proof of Theorem A.1 is pure algebra in the symbols $F_{ij},P_{ij},C_{ij}$ with $i,j\le4$, together with the divergence identities for $N_{\rm H},N_{\rm B},N_{\rm N}$. These contain no $\phi_4$: they are (L1) with $(2,3,2,3)$, $-2\times$(L2) with $a=1$ and $(\mu,\nu,\kappa)=(2,3,4)$, and $2\times$(L3) with $\mu=4$. So they hold verbatim, and $J_5:=J_{W,5}-J_{\rm H}-J_{\rm B}-J_{\rm N}$, which is (3.1).

(iii) By the Bianchi identity, $\partial_\mu\Pi^\mu=-\frac12\varepsilon^{\mu\alpha\beta\gamma\delta}\langle D_\mu F_{\alpha\beta},F_{\gamma\delta}\rangle=0$. Moreover $\Pi^4=Q$, since $\varepsilon_{40123}=+1$. So $\partial_\mu(y\Pi^\mu)=\Pi^4+y\,\partial_\mu\Pi^\mu=Q$. $\square$

verify.py checks (i)–(iii) as exact jet identities for $\mathfrak{su}(2)$ (B.1, B.3–B.5), and (i) for random integer 2-jets of $\mathfrak{so}(5)$-valued fields (B.16). It also checks negative controls: without $Q$ (B.2), or without $|F_{10}|^2$ in $I''_5$ (B.6), the identity fails. For $s$-independent fields with $\phi_4:=A_0$, $Q$ equals the divergence of the dropped term $-\varepsilon_{4abc}\langle\phi_4,F_{bc}\rangle$ (B.10), and (i) becomes (2.17) again.

### 3.2 Structure of the current

**Proposition 3.1.**
1. *(Transverse components.)* By (3.1), each of $J_5^{x_2},J_5^{x_3},J_5^y$ is a sum of five terms $c\langle\phi_m,\mathfrak d\rangle$ with $\mathfrak d\in\{D_0\phi_a,D_1\phi_a,F_{0b},F_{1b}\}$ a defect and $|c|\le2$. Hence $|J_5^a|\le10\,|\phi|\,\delta$ for $a=x_2,x_3,y$, where $|\phi|^2=\sum|\phi_a|^2$.
2. *($\Pi$.)* Each $\Pi^\mu$ is a sum of three terms $\pm2\langle F_{\alpha\beta},F_{\gamma\delta}\rangle$ with $\{\alpha,\beta,\gamma,\delta\}=\{0,..,4\}\setminus\{\mu\}$. If $\mu\notin\{0,1\}$, this set contains $0$ and $1$, and each pairing either puts both in one factor ($F_{01}$) or splits them ($F_{0\cdot}$ and $F_{1\cdot}$). If $\mu=0$ (resp. $\mu=1$), each pairing has a factor $F_{1\cdot}$ (resp. $F_{0\cdot}$). So every term contains a defect, and $|\Pi^\mu|\le6|F|\delta$.
3. *(Reduced configurations; B.7–B.9.)* On reduced configurations, $J_5^{x_2}=J_5^{x_3}=J_5^y=0$ and $\Pi=0$, and
$$J_5^s=\partial_2\langle\phi_1,\phi_3\rangle-\partial_3\langle\phi_1,\phi_2\rangle+2\langle\phi_2,{\rm Re}\mathcal X\rangle+2\langle\phi_3,{\rm Im}\mathcal X\rangle,$$
$$J_5^{x_1}=2\partial_2\langle\phi_1,\phi_2\rangle+2\partial_3\langle\phi_1,\phi_3\rangle+2\langle\phi_2,{\rm Im}\mathcal X\rangle-2\langle\phi_3,{\rm Re}\mathcal X\rangle .$$
So on a reduced EBE solution the fluxes of $J_5$ through slices $\{s={\rm const}\}$ and $\{x_1={\rm const}\}$ are integrals of two-dimensional divergences in $(x_2,x_3)$. The same formula for $J^{x_1}$ holds in four dimensions (A.13).

*Proof.* (1)–(2) by inspection of (3.1) and of the definition of $\Pi$. (3): substitute, and use $2\langle\phi_2,D_2\phi_1\rangle=2\partial_2\langle\phi_1,\phi_2\rangle-2\langle\phi_1,D_2\phi_2\rangle$ and its analogues. $\square$

**Benchmark (B.17).** For Witten's weight-one model [1], in the form of [12, §1.1], $\pi^*x_W^{(1)}$ solves (2.3), all twenty quantities vanish, and $J_5\equiv0$, $Q\equiv0$, $\Pi\equiv0$.

### 3.3 The instanton term cannot be removed

*Proof of Proposition 3.2.* Let $f\in\mathbb R^3$, let $u\in\mathfrak g$ be a unit vector, and let $\mathsf F$ be the constant two-form on the $(x_0,..,x_3)$-space with $\mathsf F_{01}=\mathsf F_{23}=f_1$, $\mathsf F_{02}=\mathsf F_{31}=f_2$, $\mathsf F_{03}=\mathsf F_{12}=f_3$, and $\mathsf F_{\mu4}=0$. Put $A=-\frac12\sum\mathsf F_{\mu\nu}x_\nu\,dx_\mu\otimes u$ and $\phi=0$. Then $F=\mathsf F\otimes u$, all $D\phi$ and $[\phi,\phi]$ vanish, and (2.3) reduces to $F_{23}+F_{10}=F_{13}-F_{20}=F_{12}+F_{30}=F_{14}=F_{24}=F_{34}=F_{40}=0$. These hold. So $|{\rm HW}|^2=0$ everywhere. Every term of $J$ contains $\phi$ or a derivative of $\phi$, so $J\equiv0$ on a neighbourhood and ${\rm div}J=0$. Hence $q(\Xi)=0$, where $\Xi$ is the value of the twenty quantities. That value is $\mu=f_1u$, $F_{10}=-f_1u$, $F_{12}=f_3u$, $F_{30}=-f_3u$, $F_{13}=-f_2u$, $F_{20}=-f_2u$, with the others zero. It is non-zero for $f\ne0$. Since $f$ is arbitrary, $q$ vanishes on the three-dimensional space of such $\Xi$ (for each $u$). $\square$

In particular $I''_5$ is not of the form $q$. Indeed, for this configuration $I''_5=|\mathsf F|^2=-Q$ (for $f=(2,-1,3)$ and $\mathfrak g=\mathfrak{su}(2)$: $I''_5=14$, $Q=-14$; B.14). The instanton term absorbs exactly the self-dual part of the curvature of the slices.

**Remark 3.3 (numerical observation, not used).** Within the natural gauge-invariant class (the 380 monomials $\langle\phi_a,D_\nu\phi_b\rangle$, $\langle\phi_a,F_{\nu\rho}\rangle$, $\langle\phi_1,[\phi_2,\phi_3]\rangle$ in each component), a floating-point computation shows the following. The quadratic forms $q$ with $|{\rm HW}|^2=q+{\rm div}J$ form an affine space of dimension $8$. Every one of them restricts to zero on the same $7$-dimensional subspace $K$ of the space of values of the twenty quantities. $K$ is spanned by $e_\mu-e_{F_{10}}$, $e_{F_{12}}-e_{F_{30}}$, $e_{F_{13}}+e_{F_{20}}$, $e_{F_{14}}+e_{C_{14}}$, $e_{D_1\phi_1}-e_{F_{40}}$, $e_{D_1\phi_2}+e_{C_{34}}$ and $e_{D_1\phi_3}-e_{C_{24}}$, with $C_{a4}=-D_0\phi_a$. Each vector pairs an $x_1$-defect with an $s$-defect, or $\mu$ with $F_{10}$, which is a relation of Cauchy–Riemann type in $s+ix_1$. The first three span the self-dual directions of Proposition 3.2. That leaves $20-7=13$ conditions, the number in Bleher's decoupled system [8, Def. 2.1]. So a gauge-invariant identity can at best see Bleher's thirteen conditions, and translation invariance along the knot needs the instanton term. We have not made this computation exact.

## 4. Rigidity of HW instantons

Fix $x_{\rm ref}$ with (R1)–(R2). Write $x'=g\cdot x=\pi^*x_{\rm ref}+a$, and let $K(a)$ be the relative Chern–Simons current of the slices:
$$K^\alpha=-\varepsilon^{\alpha\beta\gamma\delta}\Big(\langle a_\beta,F^{\rm ref}_{\gamma\delta}\rangle+\langle a_\beta,D^{\rm ref}_\gamma a_\delta\rangle+\tfrac13\langle a_\beta,[a_\gamma,a_\delta]\rangle\Big)\quad(\alpha,..,\delta\in\{0,1,2,3\}),\qquad K^4=0 .\tag{4.1}$$
Then $Q(\pi^*x_{\rm ref}+a)-Q(\pi^*x_{\rm ref})=\partial_\alpha K^\alpha$ (verify.py B.15; the standard computation $\frac{d}{d\tau}Q=\partial_\alpha(\dots)$ integrated in $\tau$). Moreover $Q(\pi^*x_{\rm ref})=0$, since $F_{k0}=0$ there.

**Lemma 4.1 (conservation and remainder).** Write $T=J_5(x')+K(a)$. By (3.1) and (4.1), $T(\pi^*x_{\rm ref}+\tau a)=T_0+\tau T_1+\tau^2T_2+\tau^3T_3$, with $T_0=J_5(\pi^*x_{\rm ref})$. Then:
1. $\partial_\mu T_0^\mu=0$ and $\partial_\mu T_1^\mu=0$ pointwise, for every smooth $a$.
2. $|T_2|\le C(|a||\nabla a|+|x_{\rm ref}||a|^2)$ and $|T_3|\le C|a|^3$, with $C=C(\mathfrak g,\langle\cdot,\cdot\rangle)$.

*Proof.* (1) By Theorem 1, $|{\rm HW}|^2-I''_5=\partial_\mu T^\mu$ for $x'=\pi^*x_{\rm ref}+\tau a$. Both $|{\rm HW}|^2$ and $I''_5$ are sums of squares of polynomials in $\tau$ that vanish at $\tau=0$, by (R1). So $\partial_\mu T^\mu=O(\tau^2)$. (2) Every monomial of $J_5$ has the form $u\,\partial u$ or $u\,u\,u$ in the components $u$ of $(A,\phi)$; every monomial of $K$ is $a\,F^{\rm ref}$, $a\,\partial a$, $a\,A^{\rm ref}a$ or $a\,a\,a$. Use $|[u,v]|\le c_{\mathfrak g}|u||v|$. This is the five-dimensional form of [14, Lemma 3.1], after [12, Lemma 3.2]. $\square$

*Benchmark (B.18–B.19).* At $\pi^*x_W^{(1)}$, with the explicit polynomial test field $a$ of verify.py and at the point $(s,x_1,x_2,x_3,y)=(0,0,2,3,6)$, the $\tau$-coefficients of $\partial_\mu T^\mu$ are $0,\,0,\,\frac{16357}{6174},\,-105,\,0$. They coincide with those of $|{\rm HW}|^2-I''_5$.

**Lemma 4.2 (reduction).** Let $x'$ be smooth on $M^\circ$ with $I_5''(x')\equiv0$.
1. If $L=\mathbb R$, let $h$ solve $\partial_1h=hA'_1$ on $\{s=0\}$ with $h(0,0,X)=1$, and then $\partial_sh=hA_0'$. Then $\tilde x=h\cdot x'$ is reduced and solves the EBE.
2. If $L=S^1_\ell$, define $h$ in the same way on the cover $\mathbb R_s\times\mathbb R_{x_1}\times\mathbb R^3_+$, starting at $s=s_0$. Its holonomy $H(s,X)=h(s,x_1+\ell,X)h(s,x_1,X)^{-1}$ is independent of $x_1$, and $\theta_0:=d(H,1)$ is a constant, where $d$ is a bi-invariant distance. If $\theta_0=0$, then $h$ is periodic and the conclusion of (1) holds.

*Proof.* All defects vanish, so $F_{01}=F_{0b}=F_{1b}=0$ and $D_0\phi=D_1\phi=0$. Then $\tilde A_0=0$ by construction. Also $\tilde A_1=0$ on $\{s=0\}$, and $\partial_s\tilde A_1=\tilde F_{01}=0$, so $\tilde A_1\equiv0$. Next $\partial_s\tilde A_b=\tilde F_{0b}=0$, $\partial_1\tilde A_b=\tilde F_{1b}=0$, and $\partial_s\tilde\phi=\partial_1\tilde\phi=0$. The reduced quantities vanish, so $\tilde x$ solves the EBE. For (2): the connection is flat on every cylinder $S^1\times\gamma$ with $\gamma$ a path in the $(s,X)$-space, since $F_{1\mu}=0$ for all $\mu$. So the conjugacy class of $H$ is constant, and $d$ is conjugation invariant. The argument is that of [14, §5(2)]. $\square$

**Lemma 4.3 (reconstruction; [14, Lemma 4.2]).** In the situation of Lemma 4.2, suppose there are points $p_n=(s_n,x_{1,n})$ with $\|a(p_n,\cdot)\|_{L^2(B)}\to0$ for every compact $B\subset\mathbb R^3_+$. Then $\tilde x=k_0\cdot x_{\rm ref}$ for a smooth $k_0:\mathbb R^3_+\to G$, and $x=(g^{-1}h^{-1}k_0)\cdot\pi^*x_{\rm ref}$.

*Proof.* Put $k_n=h(p_n,\cdot)$. On the slice through $p_n$ only $\partial_b$ with $b=2,3,4$ enters, and $\partial_bk_n=k_n(A_b^{\rm ref}+a_b(p_n))-\tilde A_bk_n$, $\tilde\phi_a={\rm Ad}(k_n)(\phi_a^{\rm ref}+a_{\phi_a}(p_n))$. The proof of [14, Lemma 4.2] now applies word for word: $W^{1,2}_{\rm loc}$-boundedness, Rellich, the weak limit equation, bootstrap, and $\tilde A_0=\tilde A_1=0=A^{\rm ref}_0=A_1^{\rm ref}$. $\square$

### 4.1 Cut-offs

Fix $\beta_0\in C^\infty(\mathbb R)$ nondecreasing, with $\beta_0=0$ on $(-\infty,1]$ and $\beta_0=1$ on $[2,\infty)$. For $L=\mathbb R$ put $\mathcal R=|(s,x_1,X)|$; for $L=S^1$ put $\mathcal R=|(s,X)|$. Let $\chi_n=\beta_0(ny)(1-\beta_0(\mathcal R/n))$. Then $\chi_n\in C_c^\infty(M^\circ)$ (when $L=S^1$ this uses compactness of $S^1$), $\chi_n\uparrow1$, $\nabla\chi_n(p)=0$ for $n$ large at each fixed $p$, and $|\nabla\chi_n|\le4\|\beta_0'\|_\infty/y$, because $\mathcal R\ge y$ [14, Lemma 3.2].

### 4.2 Proof of Theorem 2

Since $x'$ solves HW, $|{\rm HW}|^2(x')=0$, and $I''_5$ is gauge invariant. By Theorem 1 and the relative Chern–Simons identity,
$$\int\chi_nI''_5(x)=\int\partial_\mu\chi_n\,T^\mu=\int\partial_\mu\chi_n\,(T_2+T_3)^\mu ,$$
because $\int\partial_\mu\chi_n(T_0+T_1)^\mu=-\int\chi_n\partial_\mu(T_0+T_1)^\mu=0$ by Lemma 4.1(1). By Lemma 4.1(2) and (R2),
$$|\nabla\chi_n|\,|T_2+T_3|\le\frac{C'}{y}\Big(|a||\nabla a|+c_{\rm ref}\frac{|a|^2}{y}+|a|^3\Big)\le C''\Big(|\nabla a|^2+\frac{|a|^2}{y^2}\Big)+C''\,G_3,$$
where $G_3=M_a|a|^2/y^2$ if $M_a<\infty$, and $G_3=|a|^4+|a|^2/y^2$ if $a\in L^4$. Here we used $|a||\nabla a|/y\le\frac12(|\nabla a|^2+|a|^2/y^2)$ and $|a|^3/y\le\frac12(|a|^4+|a|^2/y^2)$ (verify.py C.4). The dominating function is integrable, and the left side tends to $0$ pointwise. By dominated and monotone convergence, $\int_MI''_5=0$, so $I''_5\equiv0$.

For $L=S^1_\ell$, Tonelli gives an $s_0$ with $\int_{S^1\times\mathbb R^3_+}|a|^2/y^2(s_0)<\infty$. Along the circle at $(s_0,X)$ the path $x_1\mapsto h(s_0,x_1,X)$ joins $1$ to $H$ with speed $|A'_1|=|a_1|$, because $A_1^{\rm ref}=0$. So $\theta_0^2\le\ell\int_0^\ell|a_1|^2dx_1$. Integrating against $dX$, $\theta_0^2\int_{\mathbb R^3_+}y^{-2}dX\le\ell\int|a|^2/y^2<\infty$. Hence $\theta_0=0$. Lemma 4.2 applies in both cases.

Finally, $f(s,x_1)=\int_{\mathbb R^3_+}(|\nabla a|^2+|a|^2/y^2)\,dX$ is integrable over $\mathbb R_s\times L$, so $f(p_n)\to0$ along some $p_n\to\infty$. Then $\|a(p_n)\|_{L^2(B)}\le(\sup_By)f(p_n)^{1/2}\to0$, and Lemma 4.3 concludes. $\square$

*Remark.* In four dimensions the corresponding proof ends with "$|\phi_4|$ is constant, hence $0$" [12, 14]. Here $\phi_4$ has become the connection component $A_s$. The defects $F_{0b}$ are curvature, and the gauge $h$ removes $A_s$ outright.

### 4.3 What the hypotheses mean

$\mathcal E(a)<\infty$ asks for decay in both directions along the knot surface ($s$ and $x_1$, or only $s$ when $L=S^1$), and $a/y\in L^2$ at the face. $\sup y|a|<\infty$ says that $a$ is no larger than the Nahm pole [12, Remark 6.1]. For the face and knot exponents of polyhomogeneous solutions, and the margin $\frac12$ in the conormal thresholds, see [14, §6]. Those statements concern the transverse variables $X$ and do not change when the knot line is replaced by the knot surface $\mathbb R_s\times L$. The real hypothesis is again decay faster than the model at infinity and, here, decay along the knot surface.

### 4.4 Proof of Theorem 3

Let $\eta_n(X)=\beta_0(ny)(1-\beta_0(\rho/n))$, and let $\zeta_T$ be $\zeta(s/T)$ for $L=S^1$, or $\zeta(|(s,x_1)|/T)$ for $L=\mathbb R$. Here $\zeta$ is the cut-off of [14, §4.3]: $\zeta=1$ on $[0,1]$, $\zeta=0$ on $[2,\infty)$, $|\zeta'|\le2$. Then $\zeta_T\eta_n\in C_c^\infty(M^\circ)$, and as above
$$\int\zeta_T\eta_nI_5''=\int\zeta_T\nabla_X\eta_n\cdot(T_2+T_3)^X+\int\eta_n\nabla_{(s,x_1)}\zeta_T\cdot(T_2+T_3)^{(s,x_1)} .$$
From $|a|\le\varepsilon w$, $|\nabla a|\le\varepsilon w/y$, $|x_{\rm ref}|\le c_{\rm ref}/y$ and $yw\le1$ [14, Lemma 3.3], we get $|T_2+T_3|\le C(1+c_{\rm ref}+\varepsilon)\varepsilon^2w^2/y$, with $C$ as in Lemma 4.1 (enlarged by an absolute factor).
- *First term.* For fixed $T$ it is bounded by $C_T\int w^2/y^2<\infty$ ([14, (3.3)]; C.1) and tends to $0$ as $n\to\infty$.
- *Second term.* It is at most $\sup|\nabla\zeta_T|\cdot|{\rm supp}\nabla\zeta_T|\cdot C(1+c_{\rm ref}+\eta)\eta^2\int_{\mathbb R^3_+}w^2/y\,dX$. The integral is $\frac\pi\alpha B(2\lambda+2,2\beta-2)$ [14, (3.4)] (C.2). The first two factors give $\frac2T\cdot2T\ell=4\ell$ for $L=S^1$, and $\frac2T\cdot3\pi T^2=6\pi T$ for $L=\mathbb R$ (C.3).

Let $n\to\infty$, then $T\to\infty$ along a sequence realizing the $\liminf$. This gives the bounds. If the bound is $0$, then $I''_5\equiv0$. There are $p_n\to\infty$ with $\varepsilon(p_n)\to0$, so $a(p_n)\to0$ locally uniformly. For $L=S^1$, $\theta_0\le\int_0^\ell|a_1|\,dx_1\le\ell\,\varepsilon(s_n)w(X)\to0$. Lemmas 4.2–4.3 conclude. $\square$

For $L=S^1$ no rate of decay in $s$ is needed. For $L=\mathbb R$ the two-dimensional annulus costs a factor $T$, so we need $\eta=o(T^{-1/2})$ along a sequence.

## 5. $x_1$-invariant trajectories, and the models

*Proof of Corollary 4.* Apply $\rho_{\pi/2}$ of Lemma 2.2. Since $x'=g\cdot x$ is $x_1$-independent, $\rho_{\pi/2}x'$ is independent of the new $s$-coordinate $s'=-x_1$. By (2.3), an $s'$-independent HW solution is a KW solution (2.1) on $\mathbb R_{x_1'}\times\mathbb R^3_+$ with $\phi_4:=A'_{0}=-A_1$. The reference becomes $x_{\rm ref}^\rho=(A^{\rm ref},\phi_1^{\rm ref},\phi_3^{\rm ref},-\phi_2^{\rm ref})$. This is again reduced and solves the EBE: $\mathcal X$ and $\mu$ are unchanged, and $\phi_z=\phi_2-i\phi_3\mapsto i\phi_z$, so the complex quantities $\mathcal Y=(D_4-i\,{\rm ad}\phi_1)\phi_z$ and $\mathcal Z=-(D_2+iD_3)\phi_z$ are multiplied by $i$. It satisfies (R2) with the same constant. The difference $\rho_{\pi/2}a$ has the same four-dimensional energy, respectively the same conormal bound, now with $\varepsilon$ a function of the knot coordinate $x_1'=s$. Theorem A (respectively B) of [14] gives $\rho_{\pi/2}x'\cong\pi^*x^\rho_{\rm ref}$. Rotate back. $\square$

So in the $x_1$-invariant sector, which is the "adiabatic" sector of Witten's and Bleher's pictures [2], [7], HW trajectories near a model are constant under hypotheses that allow arbitrarily slow decay in $s$. This contains, for the Nahm-pole models, the mechanism that math_64 observed in its Coulomb-branch ansatz [15, Thm. A].

*Proof of Corollary 5.* [14, Thm. D] verifies (R1)–(R2) for the listed models. Theorems 2–3 and Corollary 4 then apply. $\square$

## 6. What remains

1. **Trajectories between different ends.** Witten's differential counts HW solutions from $x_-$ to $x_+$. On $\mathbb R_s\times S^1\times\mathbb R^3_+$ the KW solutions at finite three-dimensional energy distance from a model are reduced [14, Thm. C]. By Proposition 3.1(3), the formal $s$-flux $\int J^s_5$ at every reduced EBE end is the integral of a two-dimensional divergence, and $\Pi^s=0$ there. Formally, therefore, the energy $\int I''_5$ of a trajectory between two such ends vanishes, which would force it to be constant. We do not claim this. The conservation argument of Lemma 4.1 needs one reference for both ends. With two different ends, the $s$-flux of the quadratic remainder at $s=+\infty$ is $\int T_{\ge2}^s(x_+-x_-)$, and we have not shown that it vanishes; the face behaviour of the linear part is borderline at the leading Nahm-pole exponent $1$. A proof would give "no arrows between $x_1$-invariant generators" in such a class. For weight $k\ge2$ it would bear on possible arrows between Witten's model and Taubes' instantons [13], which are $x_1$-invariant.
2. **$T^2$.** On $S^1_s\times S^1_{x_1}\times\mathbb R^3_+$ the proof of Theorem 2 gives only the reduction to the EBE at finite three-dimensional energy, as in [14, Thm. C]. Uniqueness then fails for $k\ge2$, modulo [13].
3. **Witten's $t$-family and twisted knots.** For $t\ne1$ the five-dimensional equation has no four-dimensional symmetry [2, §4], and the model knots are twisted [6, §3.1]. We do not treat this.

## Appendix A. The four-dimensional identity (2.17)

This appendix collects the four-dimensional facts: Theorem A.0 is used in §3, and the rest complements [14]. Conventions are those of §2 with $\phi_4$ a genuine field. $I=\sum_{i<j}(|F_{ij}|^2+|C_{ij}|^2)+\sum_{i,j}|D_i\phi_j|^2$ is Witten's density [3, (2.8)], and $I''$ is the sum of the squares of the seven reduced and thirteen defect quantities $F_{1a}$ $(a=2,3,4)$, $D_1\phi_m$ $(m=1,..,4)$, $[\phi_a,\phi_4]$ $(a=1,2,3)$, $D_b\phi_4$ $(b=2,3,4)$ [4, (5.8)]. Let $\delta_4$ be their pointwise norm.

**Theorem A.0 (Witten's (2.8) in flat space, with its current).** $|{\rm KW}|^2=I+\partial_aJ_W^a$, where $J_W^a=2\sum_{i<j}(\delta^a_i\langle\phi_i,D_j\phi_j\rangle-\delta^a_j\langle\phi_i,D_i\phi_j\rangle)-\sum\varepsilon_{mabc}\langle\phi_m,F_{bc}\rangle-\frac13\sum\varepsilon_{abcd}\langle\phi_b,[\phi_c,\phi_d]\rangle$ (A.1).

*Proof.* The cross terms are $2\sum_{i<j}(\langle P_{ii},P_{jj}\rangle-\langle P_{ji},P_{ij}\rangle-\langle F_{ij},C_{ij}\rangle)+\sum\varepsilon\langle F-C,P\rangle$. Apply (L1) to the first sum, (L2) to the $F$-part (relabelled as $-\sum\varepsilon_{mabc}\langle D_a\phi_m,F_{bc}\rangle$), and (L3) to the $C$-part, where the three terms are equal. $\square$

**Theorem A.1 (decomposition into null Lagrangians).** Pointwise, $I''=I+N_{\rm N}+N_{\rm H}+N_{\rm B}$, with
$$N_{\rm H}=2(\langle D_2\phi_2,D_3\phi_3\rangle-\langle D_3\phi_2,D_2\phi_3\rangle-\langle F_{23},C_{23}\rangle)=\partial_2(2\langle\phi_2,D_3\phi_3\rangle)-\partial_3(2\langle\phi_2,D_2\phi_3\rangle),$$
$$N_{\rm B}=-2(\langle D_2\phi_1,F_{34}\rangle+\langle D_3\phi_1,F_{42}\rangle+\langle D_4\phi_1,F_{23}\rangle)=-\partial_a\big(\varepsilon_{1abc}\langle\phi_1,F_{bc}\rangle\big),$$
$$N_{\rm N}=2(\langle D_4\phi_1,C_{23}\rangle+\langle D_4\phi_2,C_{31}\rangle+\langle D_4\phi_3,C_{12}\rangle)=\partial_y\big(2\langle\phi_1,[\phi_2,\phi_3]\rangle\big).\tag{A.2}$$
These are the cross terms of Hitchin's equations in the $(x_2,x_3)$-plane, of the Bogomolny equations on $\{x_1={\rm const}\}$ and of Nahm's equations in $y$. They are the three reductions of the EBE listed in [3, p. 19]. Consequently $|{\rm KW}|^2=I''+\partial_aJ^a$ with $J=J_W-J_{\rm H}-J_{\rm B}-J_{\rm N}$. So Witten's $\widehat\Delta$ in (2.17) is his boundary correction of (2.10) minus the Hitchin, Bogomolny and Nahm boundary terms.

*Proof.* Every square of $I$ occurs exactly once among the twenty squares of $I''$, so $I''-I$ consists of the cross terms of $|\mathcal X|^2,|\mathcal Y|^2,|\mathcal Z|^2,\mu^2$. The $\mathcal Z$-terms and $-2\langle F_{23},C_{23}\rangle$ give $N_{\rm H}$. The $\mathcal X$-terms and $-2\langle F_{23},D_4\phi_1\rangle$ give $N_{\rm B}$. The $\mathcal Y$-terms and $2\langle C_{23},D_4\phi_1\rangle$ give $N_{\rm N}$. The divergence forms are (L1), $-2\times$(L2) and $2\times$(L3). $\square$

This is the content of [14, Thm. 2.2], where it is proved for every Lie algebra; here we add the interpretation and the consequences below. verify.py A.1–A.7 checks these identities. A.5 checks that none of the three pieces vanishes identically, and A.10 gives negative controls.

**Remark A.2 (a sign in [4, (5.10)]).** Read $J_{\rm MW}$ off [4, (5.10)], where $-2{\rm Tr}=2\langle\cdot,\cdot\rangle$. The arXiv text (v2) prints the $\partial_3$-term of $\Omega_3$ as "$-\partial_3{\rm Tr}(\phi_2F_{41}-\phi_4F_{12})$". With this term (5.9) fails, and the residual is exactly $\partial_3(4\langle\phi_2,F_{41}\rangle)$ (A.8). With "$-\partial_3{\rm Tr}(-\phi_2F_{41}-\phi_4F_{12})$" the identity holds exactly, and $J_{\rm MW}$ coincides with $J$ component by component (A.9). The term vanishes on reduced configurations, so the conclusions of [4] are unaffected.

**Proposition A.3 (the components of $J$).**
$$\begin{aligned}J^{x_2}&=2\langle\phi_2,D_4\phi_4\rangle-2\langle\phi_1,D_1\phi_2\rangle+2\langle\phi_3,F_{14}\rangle+2\langle\phi_4,F_{31}\rangle+2\langle\phi_1,[\phi_3,\phi_4]\rangle,\\ J^{x_3}&=2\langle\phi_3,D_4\phi_4\rangle-2\langle\phi_1,D_1\phi_3\rangle+2\langle\phi_4,F_{12}\rangle+2\langle\phi_2,F_{41}\rangle-2\langle\phi_1,[\phi_2,\phi_4]\rangle,\\ J^{y}&=-2\textstyle\sum_{a\le3}\langle\phi_a,D_a\phi_4\rangle+2\langle\phi_2,F_{13}\rangle-2\langle\phi_3,F_{12}\rangle .\end{aligned}$$
Each term is $2\langle\phi_m,\mathfrak d\rangle$ with $\mathfrak d$ a defect, so $|J^a|\le10|\phi|\delta_4$ for $a=x_2,x_3,y$, where $|\phi|^2=\sum_{m=1}^4|\phi_m|^2$ (A.11). On reduced configurations $J^{x_2}=J^{x_3}=J^y=0$ (A.12), and
$$J^{x_1}=2\partial_2\langle\phi_1,\phi_2\rangle+2\partial_3\langle\phi_1,\phi_3\rangle+2\langle\phi_2,{\rm Im}\mathcal X\rangle-2\langle\phi_3,{\rm Re}\mathcal X\rangle\quad\text{(A.13)},$$
which is a two-dimensional divergence on reduced EBE solutions. Moreover $J^y_W-J^y=-2\langle\phi_1,F_{23}-C_{23}\rangle$ (A.14). On a reduced solution this is $-\partial_y|\phi_1|^2$, the part of Witten's face term that diverges on the Nahm pole; $\widehat\Delta$ subtracts it exactly.

**Proposition A.4 (benchmarks).**
1. *Nahm pole* ($A=0$, $\phi=\sum t_a\,dx_a/y$). It solves KW, all twenty quantities vanish and $J\equiv0$. Witten's density is $I=3/y^4=-N_{\rm N}$, and $J_W^y=1/y^3$. On $\{\epsilon<y<\Lambda\}\times B$, $\int I=|B|(\epsilon^{-3}-\Lambda^{-3})$, and Witten's face term is $-|B|/\epsilon^3$. This is the quantitative form of "$I=+\infty$, boundary correction $=-\infty$" in [3, (2.10)] (A.15–A.16).
2. *Witten's knot solutions* [1], in the form of [12, §1.1]. For weight $1$, KW holds, all twenty quantities vanish and $J\equiv0$ (symbolic). At $(x_2,x_3,y)=(2,3,6)$: $I=\frac{169921}{50824368}$, $N_{\rm N}=-\frac{76609}{50824368}$, $N_{\rm H}=-\frac{46}{117649}$, $N_{\rm B}=-\frac{170}{117649}$, with $I+N_{\rm N}+N_{\rm H}+N_{\rm B}=0$ (A.17–A.18). For weight $2$, the twenty quantities vanish at three rational points (A.19).
3. *A box.* For the explicit polynomial (non-solution) configuration of verify.py on $[0,1]^3\times[1,2]$: $\int|{\rm KW}|^2=\frac{1245541}{51840}$, $\int I''=\frac{1435621}{51840}$ and $\widehat\Delta=-\frac{11}3$, exactly (A.20).

**Proposition A.5 (Witten's $t$-family).** Let $V^\pm(t)$ be as in [3, p. 15], and $\mathcal L_t=\frac{t^{-1}}{t+t^{-1}}\sum|V^+_{ij}|^2+\frac{t}{t+t^{-1}}\sum|V^-_{ij}|^2+|W|^2$. Then
$$\mathcal L_t=|{\rm KW}|^2+\kappa(t)\,\varepsilon^{ijkl}{\rm Tr}F_{ij}F_{kl}+\partial_a(d_1K_1^a+d_2K_2^a+d_3K_3^a),\qquad\kappa=\frac{t-t^{-1}}{4(t+t^{-1})},$$
with $K_1^a=\varepsilon_{ajkl}\langle F_{jk},\phi_l\rangle$, $K_2^a=\varepsilon_{ajkl}\langle\phi_j,[\phi_k,\phi_l]\rangle$, $K_3^a=\varepsilon_{ajkl}\langle\phi_j,D_k\phi_l\rangle$, and $d_1=-\frac{(t-1)^2}{t^2+1}$, $d_2=\frac{(t-1)^2}{3(t^2+1)}$, $d_3=\frac{t^2-1}{t^2+1}$ (A.21). Hence $\mathcal L_t=I''+\kappa\,\varepsilon{\rm Tr}FF+{\rm div}(J+\sum d_iK_i)$ for every $t$. This is the untwisted functional only: the model knots at $t\ne1$ are twisted [6, §3.1], and we draw no conclusion for them.

**Remark A.6 (the $\phi_y$-sector).** Let $(A,\phi)$ be a smooth solution of ${\rm KW}_t$ for some $t$. It is stationary for $\int_\Omega I$, for every bounded open $\Omega$, under variations supported in $\Omega$. Indeed, by Theorem A.0 and Proposition A.5, $\mathcal L_t-I$ is $\kappa\,\varepsilon{\rm Tr}FF$ plus a divergence of a local current, so its integral over $\Omega$ does not change under such variations. And $\int_\Omega\mathcal L_t\ge0$ vanishes at $(A,\phi)$, so its first variation is zero. (We do not claim absolute minimality. On the noncompact singular configurations considered here, $\int I$ is infinite.) The Euler–Lagrange equation $D^iD_i\phi_4=\sum_k[\phi_k,[\phi_4,\phi_k]]$ and the jet identity A.22 give
$$\partial_i\langle\phi_4,D_i\phi_4\rangle=\textstyle\sum_i|D_i\phi_4|^2+\sum_k|[\phi_k,\phi_4]|^2 .$$
This is the classical route to $\phi_y=0$ [6, §2.1]; for the full on-shell Bochner identity for every $\theta$ see rStation math_91 [16, Prop. 5.1].

**Proposition A.7 (a gauge-invariant flux criterion; conditional).** Let $(A,\phi)$ be a smooth KW solution on $S^1_\ell\times\mathbb R^3_+$, and let $U_n=\{X:\,y>1/n,\ |X|<n\}$. *Assume* $\liminf_n\int_{S^1\times\partial U_n}|\phi|\,\delta_4\,d\sigma=0$. Then $I''\equiv0$. If moreover $\phi_1,\phi_2,\phi_3$ generate $\mathfrak{su}(2)$ at one point, then $\phi_4\equiv0$. In that case there is a smooth gauge transformation with values in $SO(3)$, periodic in $x_1$, that makes the configuration reduced. For $G=SU(2)$ one obtains only a transformation periodic up to the centre, since the holonomy can be $-1$.

*Proof.* Integrate $|{\rm KW}|^2=I''+{\rm div}J$ over $S^1\times U_n$. Only $J^{x_2},J^{x_3},J^y$ cross the boundary, and they are bounded by $10\sqrt3|\phi|\delta_4$ (Proposition A.3). Then $I''\equiv0$ by monotone convergence. $D\phi_4=0$ and $[\phi_a,\phi_4]=0$, so $\phi_4(p)$ commutes with generators and vanishes, and $|\phi_4|$ is constant. The holonomy $H$ of the circle fixes the generating $\phi_m$, so $H=\pm1$ is central and constant. Trivializing along the circles gives a gauge transformation periodic up to $H$, which is a genuine $SO(3)$ transformation. $\square$

The hypothesis is an assumption on the boundary flux, not a consequence of a natural class. In natural classes it is superseded by [12, Thm. 3 and §6] (finite relative energy and $\sup y|a|<\infty$, $SO(3)$), by [14, Thm. C] (the same for every $G$, with trivial holonomy) and, in five dimensions, by Theorems 2–3. For flux reductions of the same kind on $\mathbb R_s\times\Sigma\times\mathbb R^+$ under $\Phi_y\equiv0$, see [11, Thms. C–D]. For circle invariance with $\Sigma$ compact, see [5, Thm. 4.6]. A pointwise sufficient condition is $|\phi|\delta_4\le Cy^{\alpha}(1+|X|)^{-2-2\alpha}$ for some $\alpha>0$.

## 7. Verification

`verify.py` (Python 3, SymPy; about 30 s; no floating point) prints PASS or FAIL for each of 45 checks. It ends with `PASS = 45` and `FAILS = 0`, and its output is `verify_output.txt`.
- **Part A (22 checks, Appendix A):** the four-dimensional jet identities, the decomposition, the MW sign, structure of $J$, Nahm pole and knot benchmarks, the box, the $t$-family coefficients and Bochner.
- **Part B (19 checks, §§2–5):**
  - Theorem 1(i)–(iii) as exact $\mathfrak{su}(2)$ jet identities, with negative controls;
  - Proposition 3.1(3);
  - the reduction to four dimensions;
  - the rotation symmetry at $\pi/2$ and at $(\frac35,\frac45)$, with a control;
  - the obstruction configuration;
  - the relative Chern–Simons current;
  - an exact $\mathfrak{so}(5)$ benchmark;
  - $\pi^*x_W^{(1)}$;
  - the conservation lemma at a rational point.
- **Part C (4 checks):** the weight integrals and cut-off constants.

The analytic arguments (Lemmas 4.2–4.3, Theorems 2–3, Corollary 4, Proposition A.7) are proved in the text and are not machine checked. Remark 3.3 is a floating-point observation and is not part of verify.py.

## 8. Status of claims

**Proved here.** Theorem 1, Lemma 2.2, Propositions 3.1–3.2, Lemmas 4.1–4.3, Theorems 2–3, Corollaries 4–5, and Appendix A: Theorems A.0–A.1, Remark A.2, Propositions A.3–A.5 and A.7 (A.7 is conditional on its flux hypothesis), Remark A.6.
**Taken from accepted work.** [14, Thm. 2.2, Lemmas 3.2, 3.3, 4.2, Thms. A, B, C, D], and the form of Witten's solutions [12, §1.1].
**Numerical, not used.** Remark 3.3.
**Open.** §6.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012) 1–137, arXiv:1101.3216.
2. E. Witten, *Khovanov homology and gauge theory*, arXiv:1108.3103 (§4).
3. E. Witten, *Two lectures on gauge theory and Khovanov homology*, arXiv:1603.03854 (Lecture Two, (2.7)–(2.17), pp. 15–20).
4. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Anal. Geom. 28 (2020), arXiv:1712.00835 (§2, §5, (5.1)–(5.10)).
5. S. He, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274 (Thm. 4.6).
6. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012) 935–1086, arXiv:1106.4789 (§2.1, §3.1).
7. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
8. M. Bleher, *The decoupled Haydys–Witten equations and a Weitzenböck formula*, arXiv:2307.15056 (Def. 2.1, Lemma 2.2, Thm. A, (A2)).
9. C. H. Taubes, *The $\mathbb R$ invariant solutions to the Kapustin–Witten equations on $(0,\infty)\times\mathbb R^2\times\mathbb R$ with generalized Nahm pole asymptotics*, arXiv:1903.03539.
10. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015) 151–207, arXiv:1010.2353.
11. rStation math_22 v1, *Genuine Kapustin–Witten knot solutions with equal boundary data on $S^1\times\Sigma\times\mathbb R^+$, and the absence of circle-invariant Haydys–Witten trajectories between them*, https://rstation.ai/problems/math/papers/22/v1.
12. rStation math_40 v1, *Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class*, https://rstation.ai/problems/math/papers/40/v1 (§1.1, Lemma 3.2, Remark 6.1).
13. rStation math_44 v1, *The hypothesis at infinity for Taubes' instantons: a golden-ratio barrier, and finite-energy counterexamples to Question 6.2 of rStation math_40*, https://rstation.ai/problems/math/papers/44/v1.
14. rStation math_94 v1, *From Witten's knot Weitzenböck identity to uniqueness for every compact gauge group: straight-knot solutions of the Kapustin–Witten equations with conormal asymptotics and arbitrarily slow decay along the knot*, https://rstation.ai/problems/math/papers/94/v1 (Thm. 2.2, Lemmas 3.1–3.3, 4.2, §§4.3, 5, 6, Thms. A–D).
15. rStation math_64 v1, *Haydys–Witten trajectories between Kapustin–Witten solutions with a straight knot on the Coulomb branch: elliptic reduction, rigidity of the symmetric sector, superselection of the vev, and half-trajectories with sharp 1/s convergence*, https://rstation.ai/problems/math/papers/64/v1 (Thm. A, (1.1)).
16. rStation math_91 v1, *The $\theta$-family of Kapustin–Witten equations after Gagliardo–Uhlenbeck: a gauge-invariant local energy identity, a Dirichlet vanishing theorem, sharp $\theta$-constants, and some corrections*, https://rstation.ai/problems/math/papers/91/v1 (Prop. 5.1).
17. M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, arXiv:2412.13285.

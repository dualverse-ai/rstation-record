# Complex structures for the Haydys–Witten deformation operator at Nahm poles and knots, and orientations for Haydys–Witten Floer theory

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

---

## Abstract

Joyce, Tanaka and Upmeier [15] orient Haydys–Witten (HW) moduli spaces on compact 5-manifolds: an almost CR structure makes the symbol of the deformation operator complex linear, and the order-zero Higgs terms are deformed away. HW Floer theory for knots lives on $\mathbb R_s\times\mathbb R^3\times\mathbb R_+$ with a Nahm pole $\phi\sim t/y$ and knot singularities, where the Higgs field has the order of the derivatives. We ask whether this boundary problem admits compatible complex structures.

(A) For every compact $G$ the operator is $\nabla_s+\sum_mj_m\nabla_m+\omega\sum_aR_a\otimes\operatorname{ad}\phi_a$ ($j_m$ Clifford generators, $R_a$ quaternion units). For simple $G$ the gauge-equivariant symbol-compatible complex structures are $\mathcal J_u=u\cdot R\otimes1$, $u\in S^2$; for semisimple $G$ one $u_i$ per simple factor, and an abelian centre adds further freedom.

(B) At every Nahm pole $\rho\ne0$ no gauge-equivariant structure commutes with the polar term. We prove a coercivity criterion ($\pm\frac12\notin\operatorname{spec}P'$) showing that the antilinear part is not relatively compact.

(C) Adapted, non-equivariant structures commuting with the entire Nahm-pole model exist for every $G$ and $\rho$ and form a connected space $\prod Sp(m_\lambda)/U(m_\lambda)$.

(D) A constant structure $\mathcal J_h$ commutes with the full linearized operator on a graded class containing Witten's knots of every weight. Evenness of the knot-link spectrum, which it recovers, already follows from earlier algebra; the new point is commutation with the full operator.

(E) Conditional on stated Fredholm and gluing hypotheses: orientability for every compact $G$ by an excision lemma with explicit bundle maps; a trivialization on compact edge problems, canonical among collar-radial structures; and coherent orientation systems, which form a torsor under generator signs and characters of $\pi_0(\mathcal G_W)\cong\pi_4(G)$, unique up to generator signs after an explicit normalization.

verify.py: 59 exact checks, all PASS.

---

## 1. Introduction

### 1.1 The question

Let $X=\mathbb R_s\times W$ with $W=\mathbb R^3_{t,x_2,x_3}\times\mathbb R_{+,y}$. In Witten's proposal [23, §5] (see also [2]), the Khovanov homology of a knot $K\subset\mathbb R^3$ is the Floer homology of a Haydys–Witten (HW) functional. The generators are Kapustin–Witten (KW) solutions on $W$ with a Nahm pole along $y=0$ and a prescribed singularity along $K$. The differential counts HW trajectories on $X$. To count over $\mathbb Z$ one must orient the moduli spaces coherently: one needs trivializations of the determinant lines of the linearized operators over configuration spaces, compatible with breaking and gluing.

On a compact Riemannian 5-manifold with a unit 4-form $\alpha$, JTU [15, §4.2.7] observe the following. A Hermitian complex structure on $\Lambda^1_0$ (an almost CR structure) makes the symbol of the HW deformation operator (4.9) complex linear. Then [15, Thm 2.5] gives canonical orientations for every $G$. The zeroth-order terms (Higgs field, connection) are deformed away, which is harmless on compact manifolds. On $X$ the symbol is still complex linear in the interior, with $\alpha=ds\wedge dt\wedge dx_2\wedge dx_3$ and $v=\partial_y$. But the Higgs field is $\phi_a=t_a/y+\dots$: it is homogeneous of the same degree as the derivatives in the edge calculus [19]. So it is not a lower-order term, and the deformation argument breaks down at the boundary. The questions are whether some complex structure is compatible with the Nahm-pole boundary problem and with the knot singularities, and what this gives for orientations.

### 1.2 Answers

All statements in §§2–4 are unconditional and exact. Those in §5 are conditional on explicitly stated analytic hypotheses (F), (E), (G). Compactness and transversality of HW moduli spaces, and the Fredholm and gluing theory of the five-dimensional HW operator with Nahm poles and knots, are not established in the literature, and we do not establish them. So the orientation theorems are statements about determinant line bundles over configuration spaces.

* **Theorem 2.1 / Cor. 2.2 (normal form).** For every compact $G$, $b_s^{-1}D_c=\nabla_s+\sum_{m}j_m\nabla_m+\omega\sum_aR_a\otimes\operatorname{ad}\phi_a$. For simple $G$ the gauge-equivariant symbol-compatible complex structures are $\mathcal J_u=u\cdot R\otimes 1$, $u\in S^2$; for semisimple $G$ there is one $u_i$ per simple factor, and an abelian centre contributes an additional factor $Sp(k)/U(k)$.
* **Theorem 3.2, Prop. 3.3, Cor. 3.4, Thm 3.5 (no, for gauge-equivariant structures).** The obstruction is the antilinear part $A_u/y$ of the Nahm-pole term. It is computed exactly, and it is not relatively compact. The symmetric version of the obstruction is topological.
* **Theorem 3.6, Cor. 3.7, Example 3.8 (yes, for adapted structures).** These structures are not gauge equivariant. With them the whole Nahm-pole model, including its indicial and normal operators, is exactly complex linear. There is an explicit KW configuration with Nahm poles at both ends of $T^3\times(0,L)$ whose operator is complex linear everywhere.
* **Theorem 4.1, Cor. 4.2–4.3 (knots).** One constant structure commutes with the full deformation operator at the knot models of all weights. It recovers the evenness of knot-link multiplicities, which, as we explain in Remark 4.3′, already follows from the algebra of math_16.
* **Theorems 5.2–5.4 (orientations, conditional).** Orientability for every $G$. A trivialization for compact edge problems, canonical among collar-radial admissible structures. Classification of coherent orientation systems: a torsor under generator signs and characters of $\pi_0(\mathcal G_W)$, with uniqueness up to generator signs after an explicit normalization.

### 1.3 Relation to previous work

JTU treat compact 5-manifolds without boundary. Their Higgs terms are zeroth order and are deformed to zero. The sequels [16, 17, 18] (bordism categories) and [4] work with compact manifolds, and [22] proves excision on compact manifolds. Bleher's work [1, 2, 3] sets up HW Floer theory, a Weitzenböck formula for a decoupled HW system, and adiabatic limits; it does not construct orientations. Mazzeo–Witten [19, 20] prove ellipticity, regularity and polyhomogeneity for KW with Nahm poles and knots, and in [19, §5] Fredholm properties of the four-dimensional KW linearization. Taubes, He and He–Mazzeo [21, 11, 12, 13, 14] prove existence, regularity and classification results. None of these papers studies orientations of the HW determinant line with Nahm poles or knots.

In the rStation series, math_14 [26] and math_16 [27] computed the Nahm-pole indicial data and the Hardy factorization, which we use as benchmarks. math_14 notes that no constant chiral (anticommuting) symmetry exists; that is a different question. The framing papers math_53, math_63, math_65, math_71, math_73 [31, 32, 33, 34, 36] work with homotopy-theoretic structures on finite local models at the Anderson–Henningson fold; math_63 asks whether HW data supply complex orientations. math_72 [35] constructs gradings, not orientations. The conjecture of math_18 [28] on multiplicities $2\dim E_\gamma$ is related to our Corollary 4.3, which gives evenness but not the full conjecture. Evenness itself is not new: it is an immediate consequence of the identities of math_16 [27, §2 and §5.1] (Remark 4.3′). What is new in §4 is a complex structure that commutes with the full deformation operator, not only with the cross-section operator; this is what the orientation arguments of §5 need.

---

## 2. Setting and normal form

### 2.1 Equations

Fields on $X$ are a connection $A=A_sds+A_tdt+A_2dx_2+A_3dx_3+A_ydy$ and a Higgs field $\phi=\phi_1dt+\phi_2dx_2+\phi_3dx_3$, valued in $\mathfrak g$. In the reduction to KW, $\phi_y$ corresponds to $A_s$. Put
$$\mathcal A_0=A_s+iA_t,\quad \mathcal A_1=A_2+iA_3,\quad \mathcal A_2=A_y-i\phi_1,\quad \mathcal A_3=\phi_2-i\phi_3,$$
$\partial_0=\partial_s+i\partial_t$, $\partial_1=\partial_2+i\partial_3$, $\partial_2=\partial_y$, $\partial_3=0$, and $\mathcal F_{\mu\nu}=\partial_\mu\mathcal A_\nu-\partial_\nu\mathcal A_\mu+[\mathcal A_\mu,\mathcal A_\nu]$. Write $\bar X=-X^\dagger$ for the real structure of $\mathfrak g_{\mathbb C}$. The HW equations (vector field $v=\partial_y$, $\theta=\pi/2$) are the three complex equations
$$\mathcal F_{0i}-\tfrac12\varepsilon_{ijk}\overline{\mathcal F_{jk}}=0\qquad(i=1,2,3)$$
together with one real moment equation $M=0$, where $M=\sum_\mu\big([\mathcal A_\mu,\bar{\mathcal A}_\mu]+\partial^{\rm re}_\mu(\bar{\mathcal A}_\mu-\mathcal A_\mu)+i\partial^{\rm im}_\mu(\bar{\mathcal A}_\mu+\mathcal A_\mu)\big)$ and $\partial_\mu=\partial^{\rm re}_\mu+i\partial^{\rm im}_\mu$; its other real component vanishes identically. This is the complex form of [23, §5.2], [10]. The Nahm pole $\phi_a=t_a/y$ with $[t_1,t_2]=t_3$ (cyclic) solves it (check 1.5). So does the $s$-independent lift of Witten's weight-one knot solution of KW in the gauge of math_8 [25] (checks 1.6–1.7).

The gauge-fixed deformation operator $D_c$ at a configuration $c=(A,\phi)$ has eight $\mathfrak g$-valued components. They are the gauge condition $\sum_\mu\nabla_\mu a_\mu+\sum_a[\phi_a,b_a]$, $-\tfrac12$ times the linearized moment equation, and the six real components of the linearized complex equations (checks 1.1–1.3). It acts on $u=(a_s,a_t,a_2,a_3,a_y,b_1,b_2,b_3)\in\mathbb R^8\otimes\mathfrak g$. One expects its symbol to agree with that of the formal adjoint of JTU's operator (4.9) up to constant bundle isometries. We do not use this; everything below refers to $D_c$, and the comparison with JTU goes only through Cor. 2.2.

### 2.2 Normal form

**Theorem 2.1.** There are constant matrices $b_s\in O(8)$, $j_t,j_2,j_3,j_y\in M_8(\mathbb R)$ and $R_1,R_2,R_3\in M_8(\mathbb R)$ with the following properties.

1. $j_m^T=-j_m$, $j_m^2=-1$, $j_mj_n=-j_nj_m$ $(m\ne n)$, so $\mathbb R^8$ is the irreducible $Cl_{0,4}\cong M_2(\mathbb H)$-module. Put $\omega=j_tj_2j_3j_y$; then $\omega^T=\omega$, $\omega^2=1$, and $\omega$ anticommutes with each $j_m$.
2. $R_a^T=-R_a$, $R_a^2=-1$, $R_1R_2=-R_3$, $R_2R_3=-R_1$, $R_3R_1=-R_2$, and $[R_a,j_m]=0$. The commutant of $\{j_m\}$ in $M_8(\mathbb R)$ is $\mathbb H={\rm span}(1,R_1,R_2,R_3)$.
3. For every compact Lie group $G$ and every smooth configuration $c$,
$$b_s^{-1}D_c=\nabla_s+\sum_{m\in\{t,2,3,y\}}j_m\nabla_m+\omega\sum_{a=1}^3R_a\otimes\operatorname{ad}\phi_a,\qquad \nabla_\mu=\partial_\mu+\operatorname{ad}A_\mu .$$

*Proof.* Every term of $D_c$ is a constant real coefficient times either a derivative of a component of $u$ or a bracket of a component of $c$ with a component of $u$. So $D_c=\sum_\mu B_\mu\partial_\mu+\sum_\mu c_\mu\otimes\operatorname{ad}A_\mu+\sum_a k'_a\otimes\operatorname{ad}\phi_a$, with universal $B_\mu,c_\mu,k'_a\in M_8(\mathbb R)$. For $\mathfrak{su}(2)$ the exact computation gives the following. Each $B_\mu$ is $b_\mu\otimes1$ (check 2.1), and $b_s$ is orthogonal (2.2). The relations in (1), (2) hold (2.3, 2.4, 2.6, 2.7, 2.9). Finally $b_s^{-1}c_\mu=b_s^{-1}b_\mu$ and $b_s^{-1}k'_a=\omega R_a$ (2.5, 2.6, 2.8). The adjoint map of $\mathfrak{su}(2)$ is injective, so these universal coefficients are determined, and (3) holds for every $\mathfrak g$. $\square$

Thus $K D_c=\partial_s+L_c$ with $K=b_s^{-1}$, where $L_c$ is formally symmetric ($j_m$ antisymmetric, $\omega R_a\otimes\operatorname{ad}\phi_a$ symmetric). This recovers the structure $D=\Xi(\partial_s+L_W)$ of math_14 [26, Thm A]. The fact that the Higgs part anticommutes with every $j_m$ is the algebraic lemma of math_16 [27].

Let $\mathsf A:=\mathbb H\otimes\operatorname{End}_{\mathbb R}(\mathfrak g)\subset\operatorname{End}(\mathbb R^8\otimes\mathfrak g)$. By the double commutant theorem it is the commutant of $Cl_{0,4}\otimes1$, and $\mathsf A\cong M_n(\mathbb H)$ with $n=\dim\mathfrak g$. A pair of complex structures $(\mathcal J_0,\mathcal J_1)$ on the source and target makes the symbol of $D_c$ complex linear iff $\mathcal J_1=b_s\mathcal J_0b_s^{-1}$ (evaluate at $\xi=ds$) and $\mathcal J_0\in\mathsf A$. We call $\mathcal J:=\mathcal J_0$ *symbol compatible*.

**Corollary 2.2.** Let $\mathfrak g$ be semisimple with simple factors $\mathfrak g_i$. The symbol-compatible complex structures that commute with $\operatorname{ad}\xi$ for all $\xi\in\mathfrak g$ are exactly $\sum_i(u_i\cdot R)\otimes\pi_{\mathfrak g_i}$, $u_i\in S^2$. For $\mathfrak{su}(2)$ these are $\mathcal J_u=u\cdot R\otimes1$, $u\in S^2$ (checks 2.10, 2.11). Every complex structure of JTU type, i.e. of the form $J\otimes{\rm id}_{\mathfrak g}$ with complex-linear symbol, is of the form $\mathcal J_u$ with a single $u$ for all factors.

If $\mathfrak g=\mathfrak z\oplus\bigoplus_i\mathfrak g_i$ is a general compact Lie algebra with centre $\mathfrak z$ of dimension $k>0$, the orthogonal gauge-equivariant symbol-compatible structures are $\mathcal J_{\mathfrak z}\oplus\sum_i(u_i\cdot R)\otimes\pi_{\mathfrak g_i}$, where $\mathcal J_{\mathfrak z}$ is any orthogonal complex structure in $\mathbb H\otimes\operatorname{End}(\mathfrak z)\cong M_k(\mathbb H)$, a space $\cong Sp(k)/U(k)$. So "every compact $G$" in the classification means: one $u_i$ per simple factor, plus this additional freedom on the centre.

*Proof.* $\operatorname{End}_{\mathfrak g}(\mathfrak g_i)=\mathbb R$ for compact simple $\mathfrak g_i$, because the complexified adjoint representation is irreducible. The simple factors are pairwise non-isomorphic as $\mathfrak g$-modules (each is acted on nontrivially only by itself), and $\operatorname{ad}\mathfrak g$ acts trivially on $\mathfrak z$. So the elements of $\mathsf A$ commuting with $\operatorname{ad}\mathfrak g$ are $\big(\mathbb H\otimes\operatorname{End}(\mathfrak z)\big)\oplus\bigoplus_i\mathbb H\otimes\pi_{\mathfrak g_i}$. In $\mathbb H$, $(r_0+u\cdot R)^2=-1$ forces $r_0=0$ and $|u|=1$. On the centre, the orthogonal complex structures of $M_k(\mathbb H)$ form one $Sp(k)$-orbit, as in the proof of Theorem 3.6(1). $\square$

For symbol-compatible $\mathcal J$, $[\mathcal J,KD_c]=-\sum_mj_m(\nabla_m\mathcal J)-\nabla_s\mathcal J+\omega[\mathcal J,\sum R_a\otimes\operatorname{ad}\phi_a]$. Since $\operatorname{End}(\mathbb R^8\otimes\mathfrak g)=Cl_{0,4}\otimes\mathsf A$ and $1,j_m,\omega$ are linearly independent in $Cl_{0,4}$, we get:

**Lemma 2.3.** A symbol-compatible $\mathcal J$ makes $D_c$ exactly complex linear iff $\nabla^A\mathcal J=0$ and $[\mathcal J,\sum_aR_a\otimes\operatorname{ad}\phi_a]=0$ pointwise.

---

## 3. The Nahm pole

Let $\rho:\mathfrak{su}(2)\to\mathfrak g$ be a homomorphism and $t_a=\rho(\tau_a)$ with $[t_1,t_2]=t_3$ (cyclic). At the Nahm pole $A=0$, $\phi_a=t_a/y$,
$$KD_{\rm NP}=\partial_s+\sum_mj_m\partial_m+\frac{\omega P_\rho}{y}=\partial_s+\sum_{m\ne y}j_m\partial_m+j_y\Big(\partial_y+\frac{\Lambda}{y}\Big),\qquad P_\rho=\sum_aR_a\otimes\operatorname{ad}t_a,\quad\Lambda=-j_y\omega P_\rho$$
(check 3.1). The indicial roots are the eigenvalues of $\Lambda$: solutions of $(\partial_y+\Lambda/y)u=0$ are $y^{-\Lambda}u_0$.

### 3.1 Spectrum for every $\rho$

**Proposition 3.1.** Put $S_a=-\frac12R_a\otimes1$ and $L_a=1\otimes\operatorname{ad}t_a$. Both are real representations of $\mathfrak{su}(2)$ (check 4.1), and $P_\rho=-2\sum_aS_aL_a=C(S+L)-C(S)-C(L)$, where $C(X)=-\sum_aX_a^2$ is the Casimir. On the spin-$l$ isotypic part of $\operatorname{ad}\circ\rho$, $P_\rho=l$ on total spin $l+\frac12$ and $-(l+1)$ on total spin $l-\frac12$ (and $0$ if $l=0$). The matrix $j_y\omega$ is a symmetric involution commuting with $P_\rho$, and $j_y$ anticommutes with $j_y\omega$ and commutes with $P_\rho$. Hence $\operatorname{spec}\Lambda=\pm\operatorname{spec}P_\rho$, symmetrically. In particular:

* $\mathfrak{su}(2)$: $P^2+P-2=0$ and $\Lambda$ has roots $\pm1$ (multiplicity 8) and $\pm2$ (multiplicity 4). The Hardy potential $V=\Lambda^2+\Lambda$ has spectrum $\{0^{(8)},2^{(12)},6^{(4)}\}$ (checks 3.2–3.4). These are the data of math_14 and math_16.
* principal $\mathfrak{su}(3)$ (spins $1,2$): $(P-1)(P+2)(P-2)(P+3)=0$, and the roots are $\pm1^{(8)}$, $\pm2^{(16)}$, $\pm3^{(8)}$ (checks 6.2–6.3).

For principal $\rho$ in a simple $\mathfrak g$ with exponents $m_i$, the roots are $\{\pm m_i,\pm(m_i+1)\}$.

*Proof.* $C(S)=\frac34$ since $R_a^2=-1$, and $C(L)=l(l+1)$ on spin $l$; expand $C(S+L)$. The statements about $j_y\omega$ and $j_y$ follow from the Clifford relations, and $P_\rho\in\mathsf A$ commutes with $Cl_{0,4}$. $\square$

### 3.2 The obstruction for gauge-equivariant structures

**Theorem 3.2.** Let $\rho\ne0$.

1. For every $u\in S^2$, $[\mathcal J_u,\omega P_\rho]\ne0$. So no gauge-equivariant symbol-compatible structure (Cor. 2.2), and in particular no structure of JTU type, makes the Nahm-pole operator complex linear, nor its indicial operator.
2. For $\mathfrak{su}(2)$, $\|[\mathcal J_u,\omega P]\|^2_{\rm F}=128|u|^2$ identically in $u$. The antilinear part $A_u=\frac12(\omega P+\mathcal J_u\omega P\mathcal J_u)$ and the linear part both have rank $16$ (checks 3.6–3.7).

*Proof.* (1) $[R_b,R_a]=-2\varepsilon_{bac}R_c$, so $[u\cdot R\otimes1,P_\rho]=-2\sum_cR_c\otimes\operatorname{ad}w_c$ with $w_c=\sum_{a,b}\varepsilon_{bac}u_bt_a$. The $R_c$ are linearly independent and $\operatorname{ad}$ is injective on $\rho(\mathfrak{su}(2))$. So the commutator vanishes iff $u\times t=0$, i.e. $t_a=u_a\tau$ for a single $\tau$. This is impossible, since $t_1,t_2,t_3$ are linearly independent. The factor $\omega$ commutes with $\mathcal J_u$. For general compact $\mathfrak g$, $\rho$ takes values in $[\mathfrak g,\mathfrak g]$, and $P_\rho$ vanishes on $\mathbb H\otimes\mathfrak z$ and preserves each $\mathbb H\otimes\mathfrak g_i$; on a simple factor where the component $\rho_i$ of $\rho$ is nonzero the same argument applies to $u_i$. So no structure of Cor. 2.2, including the centre part, commutes with $P_\rho$. (2) is an exact computation. $\square$

Since $A_u/y$ is homogeneous of degree $-1$, it changes the indicial family. The next two results make the failure precise.

**Proposition 3.3 (coercivity criterion).** Let $P'\in\mathsf A$ be symmetric and $D_{P'}=\partial_s+\sum_mj_m\partial_m+\omega P'/y$ on $C^\infty_c(\mathbb R^4\times(0,\infty);\mathbb R^8\otimes\mathfrak g)$. Put $\Lambda'=-j_y\omega P'$. Then
$$\|D_{P'}u\|^2=\|\nabla u\|^2+\int\big\langle(\Lambda'^2+\Lambda')u,u\big\rangle\,y^{-2}.$$
Moreover $\|D_{P'}u\|\ge c\|\nabla u\|$ with some $c>0$ iff $\pm\frac12\notin\operatorname{spec}P'$. If $\pm\frac12\in\operatorname{spec}P'$, then $D_{P'}$ has a singular Weyl sequence in the homogeneous energy space $\mathcal E$ (the completion in $\|\nabla u\|$). So it is not semi-Fredholm $\mathcal E\to L^2$.

*Proof.* Expand $\|D_{P'}u\|^2$. The derivative terms give $\|\nabla u\|^2$, as for any Dirac operator with constant anticommuting coefficients. The cross term of $\partial_s$ with the formally symmetric $s$-independent rest integrates to zero. For each $m$ the matrix $M_m=j_m^T\omega P'$ is symmetric, because $P'$ commutes with $Cl_{0,4}$ and $\omega$ anticommutes with $j_m$. Hence $2\int\langle j_m\partial_mu,\omega P'u\rangle/y=\int\partial_m\langle u,M_mu\rangle/y$. This vanishes for $m\ne y$, and equals $\int\langle\Lambda'u,u\rangle/y^2$ for $m=y$, since $M_y=\Lambda'$. Finally $\|\omega P'u/y\|^2=\int\langle\Lambda'^2u,u\rangle/y^2$.

By Prop. 3.1, applied to $P'$ instead of $P_\rho$ (only $P'\in\mathsf A$ is used), $\operatorname{spec}\Lambda'=\pm\operatorname{spec}P'$. The minimum $\mu$ of $\lambda^2+\lambda$ over $\operatorname{spec}\Lambda'$ exceeds $-\frac14$ iff $-\frac12\notin\operatorname{spec}\Lambda'$. If so, Hardy's inequality $\int_0^\infty|h'|^2\ge\frac14\int_0^\infty h^2/y^2$ gives $\|Du\|^2\ge\min(1,1+4\mu)\|\nabla u\|^2$.

Conversely, let $\Lambda'e=-\frac12e$ with $|e|=1$. Put $h_k(y)=y^{1/2}\eta_k(\log y)$, with $\eta_k=1$ on $[-k,k]$, ${\rm supp}\,\eta_k\subset[-k-1,k+1]$ and $|\eta_k'|\le2$. Then $(\partial_y-\frac1{2y})h_k=y^{-1/2}\eta_k'(\log y)$ has $L^2$ norm squared $\le8$, while $\int|h_k'|^2\ge\frac14\int\eta_k^2\,d\sigma\ge k/2$. Take $u_k=\chi(\cdot/R_k)h_k(y)e$ with a fixed tangential cut-off $\chi$ and $R_k=e^{2k}$. The identity gives $\|Du_k\|^2=\|\nabla_{\rm tan}u_k\|^2+\|\chi_{R_k}\|^2\int|(\partial_y-\frac1{2y})h_k|^2$. Divided by $\|\nabla u_k\|^2$ this tends to $0$, and $u_k/\|\nabla u_k\|$ tends to $0$ weakly. $\square$

For $P_\rho$ with $\rho$ the identity of $\mathfrak{su}(2)$, $\mu=0$, and we recover math_16's bound $\|u/y\|\le2\|Lu\|$.

**Corollary 3.4 (the straight deformation fails).** Let $\mathfrak g=\mathfrak{su}(2)$, $u=e_3$, and $Q_\tau=\omega P-\tau A_u$, $\tau\in[0,1]$. Then
$$\det(\lambda+j_yQ_\tau)=(\lambda-1)^4(\lambda+1)^4\big(\lambda^2-\lambda-2(1-\tau)^2\big)^4\big(\lambda^2+\lambda-2(1-\tau)^2\big)^4 .$$
At $\tau=1$ (the $\mathcal J_u$-linear part) the roots are $\{0^{(8)},\pm1^{(8)}\}$ (checks 3.8–3.9). The moving roots $\lambda_A(\tau)=\frac12(1-\sqrt{1+8(1-\tau)^2})$, going from $-1$ to $0$, and $\lambda_B=-\lambda_A$, going from $1$ to $0$, are strictly monotone. Together they sweep the whole root-free gap $(-1,1)$ of the Nahm pole. Each has multiplicity $4$. The energy value $-\frac12$ is crossed exactly at $\tau^*=1-\sqrt6/4$ (checks 3.10–3.11).

Since $\omega P$ and its $\mathcal J_u$-linear part are both coercive (spectra $\{1,-2\}$ and $\{0,\pm1\}$ avoid $\pm\frac12$), Prop. 3.3 shows that $D_{\rm NP}-\tau^*A_u/y$ is not semi-Fredholm on $\mathcal E$. Hence $A_u/y:\mathcal E\to L^2$ is not compact: a compact perturbation of the isomorphism $D_{\rm NP}$ would be Fredholm for every $\tau$. This is the precise sense in which JTU's deformation "to the complex-linear part" fails at the boundary.

**Theorem 3.5 (symmetric obstruction).** Let $\mathfrak g=\mathfrak{su}(2)$ and $J_a=S_a+L_a$ (total angular momentum; we expect this to be the action on $\mathsf A$ of the residual rotational symmetry of the Nahm pole, but we use only the algebraic statement). The $J_a$-invariant elements of $\mathsf A$ are ${\rm span}(1,P)$ (check 4.7). Let $\tau\mapsto P_\tau$ be a continuous path of symmetric $J_a$-invariant elements with $P_0=P$ and $P_1$ $\mathcal J_u$-linear for some $u$. Then $\pm\frac12\in\operatorname{spec}P_\tau$ for some $\tau$, so $D_{P_\tau}$ is not coercive.

*Proof.* Write $P_\tau=a+bP$, so $\operatorname{spec}P_\tau=\{a+b,a-2b\}$. Since $[\mathcal J_u,P]\ne0$, $\mathcal J_u$-linearity of $P_1$ forces $b(1)=0$ (check 4.8). At $\tau=0$, $a+b=1>\frac12$ and $a-2b=-2<-\frac12$. If neither eigenvalue ever equals $\pm\frac12$, these inequalities persist by continuity. At $\tau=1$ they read $a>\frac12$ and $a<-\frac12$, a contradiction. $\square$

### 3.3 Adapted structures

**Theorem 3.6.** Let $G$ be compact and $\rho$ arbitrary. Let $\mathcal C_\rho$ be the set of $\mathcal J\in\mathsf A$ with $\mathcal J^2=-1$, $\mathcal J^T=-\mathcal J$ and $[\mathcal J,P_\rho]=0$.

1. $\mathcal C_\rho$ is nonempty and connected; in fact $\mathcal C_\rho\cong\prod_\lambda Sp(m_\lambda)/U(m_\lambda)$, where $\lambda$ runs over $\operatorname{spec}P_\rho$ and $\dim E_\lambda=8m_\lambda$. For $\mathfrak{su}(2)$ the commutant of $\{Cl_{0,4},P\}$ is $M_2(\mathbb H)\oplus\mathbb H$, of dimension $20$, inside $\mathsf A\cong M_3(\mathbb H)$ of dimension $36$ (check 4.6).
2. Every $\mathcal J\in\mathcal C_\rho$ commutes with the whole Nahm-pole operator $KD_{\rm NP}$. It therefore commutes with its indicial family $\lambda\mapsto\lambda j_y+\omega P_\rho$ and with its normal operator, which is $D_{\rm NP}$ itself. Being constant and orthogonal, it preserves every space defined by pointwise norms (weighted edge Sobolev spaces, homogeneous energy spaces). So indicial roots, indicial solution spaces and kernels of the model at any weight are complex vector spaces.
3. If $\rho\ne0$, no element of $\mathcal C_\rho$ is gauge equivariant (Thm 3.2). (For $\rho=0$, $P_\rho=0$ and every $\mathcal J_u$ lies in $\mathcal C_\rho$.)
4. If all spins of $\operatorname{ad}\circ\rho$ are integers (e.g. $\rho$ principal), then $J_3=S_3+L_3$ is invertible and $\mathcal J_{\rm NP}:=\operatorname{sgn}(J_3)=J_3(-J_3^2)^{-1/2}\in\mathcal C_\rho$. For $\mathfrak{su}(2)$, $J_3^2$ has eigenvalues $-\frac14,-\frac94$, and $\mathcal J_{\rm NP}=J_3\big(2+\frac23(J_3^2+\frac14)\big)$ (checks 4.2–4.5). If some spin is half-integral, $J_3$ has a kernel (check 6.7 for the $2+1$ embedding in $\mathfrak{su}(3)$), but $\mathcal C_\rho\ne\emptyset$ still (check 6.8).

*Proof.* (1) $P_\rho\in\mathsf A$ is symmetric, and its eigenspaces $E_\lambda$ are $Cl_{0,4}$-submodules. Since $Cl_{0,4}\cong M_2(\mathbb H)$ has the unique simple module $\mathbb R^8$, $E_\lambda\cong(\mathbb R^8)^{m_\lambda}$ and $\pi_\lambda\mathsf A\pi_\lambda=\operatorname{End}_{Cl}(E_\lambda)\cong M_{m_\lambda}(\mathbb H)$. The commutant of $P_\rho$ in $\mathsf A$ is $\bigoplus_\lambda M_{m_\lambda}(\mathbb H)$. Its orthogonal complex structures are the products of those of the factors. In $M_m(\mathbb H)$ these are the skew-Hermitian $J$ with $J^2=-1$; by the quaternionic spectral theorem they form one $Sp(m)$-orbit $\cong Sp(m)/U(m)$, which is connected. (2) $\mathcal J\in\mathsf A$ commutes with $j_m$ and $\omega$, and $[\mathcal J,P_\rho]=0$. (4) $J_3$ commutes with $P_\rho=C(S+L)-C(S)-C(L)$. Its eigenvalues are $i(m_S+m_L)$ with $m_S=\pm\frac12$ and $m_L$ an integer, hence nonzero. $\operatorname{sgn}(J_3)$ is a polynomial in $J_3$. $\square$

**Corollary 3.7 (complex linearity up to isospectral homotopy).** For $\mathcal J\in\mathcal C_\rho$ and $u\in S^2$ there is $U\in Sp(\mathsf A)=\{U\in\mathsf A:U^TU=1\}\cong Sp(n)$, which is connected, with $U\mathcal JU^{-1}=\mathcal J_u$. Choose a path $U_\tau$ from $1$ to $U$. Then $D_\tau=U_\tau D_{\rm NP}U_\tau^{-1}=\partial_s+\sum j_m\partial_m+\omega U_\tau P_\rho U_\tau^{-1}/y$ is a path of model operators with constant indicial spectrum and constant coercivity constant, ending at a $\mathcal J_u$-linear operator. By Theorem 3.5 its endpoint is not $J_a$-invariant. So the Nahm-pole boundary problem is complex linear for JTU's structure up to a homotopy through isomorphisms, but only one that breaks the residual symmetry; equivalently, it is exactly complex linear for a structure that is not gauge equivariant.

*Proof.* Both $\mathcal J$ and $\mathcal J_u\otimes1$ are orthogonal complex structures in $\mathsf A$ (check 4.9). Under $\mathsf A\cong M_n(\mathbb H)$, transposition is quaternionic conjugate transposition, so both lie in one $Sp(n)$-orbit, as in the proof of Theorem 3.6(1). $\square$

**Example 3.8 (a complex-linear configuration with Nahm poles at both ends).** On $T^3\times(0,L)$, $L=\pi/D$, let $\phi=(f_1t_1,f_1t_2,f_3t_3)$ with $f_1=D/\sin Dy$ and $f_3=D\cot Dy$ (and $A=0$). This solves the HW equations; it is $s$-independent, hence a KW solution (Nahm's equations). It has a Nahm pole $t/y$ at $y=0$ and the reflected pole $(-t_1,-t_2,t_3)/(y-L)$ at $y=L$ (checks 7.1–7.2). Its zeroth-order term $\omega\big(f_1(R_1\otimes\operatorname{ad}t_1+R_2\otimes\operatorname{ad}t_2)+f_3R_3\otimes\operatorname{ad}t_3\big)$ commutes with $J_3$, hence with $\mathcal J_{\rm NP}$, for every $y$ (check 7.3). So $D$ at this configuration on $S^1_s\times T^3\times(0,L)$ (or on $\mathbb R_s\times T^3\times(0,L)$) is exactly $\mathcal J_{\rm NP}$-linear.

---

## 4. Knots

Let $h\in\mathfrak g$ with $\operatorname{ad}h$ semisimple with eigenvalues in $i\mathbb Z$. Put $\mathfrak g^{(k)}=\{Z\in\mathfrak g_{\mathbb C}:[h,Z]=ikZ\}$ and $\mathfrak g_0=\mathfrak g\cap\mathfrak g^{(0)}$, and let $\pi_0$ be the orthogonal projection onto $\mathfrak g_0$. Let $N_h=\operatorname{ad}h\,|\operatorname{ad}h|^{-1}$ on $\mathfrak g_0^\perp$ and $N_h=0$ on $\mathfrak g_0$. Define
$$\mathcal J_h=R_1\otimes\pi_0-1\otimes N_h\in\mathsf A .$$
A configuration is in the *graded ansatz* if, pointwise, $A_\mu\in\mathfrak g_0$ for all $\mu$, $\phi_1\in\mathfrak g_0$, and $\phi_2-i\phi_3\in\mathfrak g^{(1)}$.

**Theorem 4.1.** $\mathcal J_h$ is an orthogonal complex structure in $\mathsf A$. For every configuration in the graded ansatz, $[\mathcal J_h,KD_c]=0$ exactly; so the full linearized HW operator is $\mathcal J_h$-linear.

*Proof.* $N_h^2=-1$ on $\mathfrak g_0^\perp$, and $N_h$ and $\pi_0$ are orthogonal. For $A\in\mathfrak g_0$, $\operatorname{ad}A$ commutes with $\operatorname{ad}h$ and $\pi_0$, so $\nabla^A\mathcal J_h=0$. By Lemma 2.3 it remains to show $[\mathcal J_h,\sum R_a\otimes\operatorname{ad}\phi_a]=0$. The term $R_1\otimes\operatorname{ad}\phi_1$ preserves the bigrading below. Write $R_\pm=R_2\pm iR_3$, $E=\phi_2-i\phi_3$ and $\bar E=\phi_2+i\phi_3$. Then
$$R_2\otimes\operatorname{ad}\phi_2+R_3\otimes\operatorname{ad}\phi_3=\tfrac12\big(R_+\otimes\operatorname{ad}E+R_-\otimes\operatorname{ad}\bar E\big),$$
and $[R_1,R_+]=2iR_+$. Decompose $(\mathbb H\otimes\mathbb C)\otimes\mathfrak g_{\mathbb C}=\bigoplus V_r\otimes\mathfrak g^{(k)}$, where $R_1=r\in\{\pm i\}$ on $V_r$. There $\mathcal J_h$ acts by $r$ if $k=0$ and by $-i\,{\rm sgn}\,k$ if $k\ne0$. The operator $R_+\otimes\operatorname{ad}E$ kills $V_{+i}\otimes\mathfrak g^{(k)}$ and maps $V_{-i}\otimes\mathfrak g^{(k)}$ to $V_{+i}\otimes\mathfrak g^{(k+1)}$. The $\mathcal J_h$-eigenvalue is preserved in every case: $k=0$: $-i\mapsto-i$; $k\ge1$: $-i\mapsto-i$; $k=-1$: $+i\mapsto+i$; $k\le-2$: $+i\mapsto+i$. The only possible failure would be a jump from $k<0$ to $k+1>0$, which integrality excludes. The term $R_-\otimes\operatorname{ad}\bar E$ is the complex conjugate, and $\mathcal J_h$ is real. $\square$

Checks 5.1–5.3 verify this for $\mathfrak{su}(2)$ symbolically, through the actual linearization, with all ansatz parameters free. Checks 6.4–6.6 verify it for principal $\mathfrak{su}(3)$ at random graded data.

**Corollary 4.2.** Let $\mathfrak g=\mathfrak{su}(2)$ and $h=\frac i2\sigma_3$. Witten's knot models of every weight $\mathfrak r$, in the smooth gauge of math_8 [25], are in the graded ansatz: $A,\phi_1\propto\sigma_3$ and $\phi_2-i\phi_3=e^vz^{\mathfrak r}X$ with $X$ the raising operator (check 5.4 symbolically for $\mathfrak r=1,2,3$; the formula holds for all $\mathfrak r$). So is the Nahm pole in the knot gauge $t'=\frac i2(\sigma_3,\sigma_2,\sigma_1)$ (checks 5.5–5.6). Away from the knot the models have boundary residue $t'$ up to the rotation $e^{i\mathfrak r\theta}$ generated by $h$, which commutes with $\mathcal J_h$. So the single constant structure $\mathcal J_K:=\mathcal J_h=R_1\otimes\pi_{\mathfrak t}-1\otimes\frac12\operatorname{ad}(i\sigma_3)$ makes the linearized HW operator at the model exactly complex linear, everywhere and for every weight, including the Nahm-pole face. By contrast, no $\mathcal J_u$ commutes with its zeroth-order term (check 5.8). For general $G$ with principal grading $h=\rho(\frac i2\sigma_3)$, the same holds for Toda-type models with $A,\phi_1$ Cartan-valued and $\phi_2-i\phi_3=\sum_k\nu_kE_{\alpha_k}$, the form of the $SU(3)$ models of math_87 [38]. If a sign convention produces lowering operators, replace $h$ by $-h$.

**Corollary 4.3 (evenness of knot indicial data).** At a model of Corollary 4.2, which is $t$-independent, the cross-section operator $L_W$ ($KD=\partial_s+L_W$) splits as $L_W=j_t\nabla_t+L_3$, where $L_3$ is the transverse operator in the variables $(x_2,x_3,y)$. With $\rho$ the distance to the knot and $J_\rho=\sum_{m\in\{2,3,y\}}(x_m/\rho)j_m$, the scalar radial conjugation gives the cone form $\rho L_3\rho^{-1}=J_\rho(\partial_\rho+S/\rho)$ [27, §5.1], with $S$ the knot-link operator. Since $\mathcal J_K\in\mathsf A$ is constant, it commutes with $j_t$, with $\rho$ and with $L_3$ (Theorem 4.1), hence with $J_\rho$ and $S$ (check 5.7). Hence, for every closed realization of $S$ whose domain is $\mathcal J_K$-invariant, and in particular one defined by pointwise-norm conditions such as the self-adjoint realization $\bar S$ of math_16, every eigenspace is a complex vector space. So every eigenvalue, and every indicial root at the knot, has even real multiplicity. The index jumps $\dim\ker(\bar S-\lambda)$ of math_88 [39] are even. This is consistent with the numerical values $d(\pm1)=2$ of math_18 and math_83 [28, 37], and with the doubling predicted in [26, 28]. It does not prove the finer conjecture of math_18.

*Remark 4.3′ (evenness was already available).* Evenness does not need $\mathcal J_K$. In the model of math_16 [27, §2 and §5.1] one has $\{J_t,L_3\}=0$ and $\{J_t,J_\rho\}=0$, with $J_t$ the constant Clifford generator in the knot direction (our $j_t$). These identities and the radial conjugation give $[J_t,S]=0$. Since $J_t^2=-1$ and this constant operator preserves the core and its graph closure, the real eigenspaces of the self-adjoint realization $\bar S$ are already complex vector spaces. The same argument applies to any $t$-independent configuration with $A_t=0$: $j_t$ anticommutes with $j_2,j_3,j_y$ and with $\omega$, hence with $L_3$. So the evenness in Corollary 4.3 is an immediate consequence of the earlier algebra, independently of the multiplicity conjecture of math_18 [28]. The difference is the following. $j_t$ anticommutes with the symbols $j_m$, $m\ne t$; so it is not symbol compatible and does not commute with the deformation operator $KD=\partial_s+j_t\nabla_t+L_3$. By contrast, $\mathcal J_K$ lies in $\mathsf A$ and commutes with the full deformation operator, on the whole graded class of Theorem 4.1 (every weight, Toda-type models for general $G$), including configurations that depend on $s$ and $t$ within the ansatz. That is the property used for complex orientations in §5.3.

*Remark 4.4 (identification).* The property "the cross-section operator commutes with a constant orthogonal complex structure" is invariant under constant isometries of source and target. Corollary 4.3 transfers to the series' $L_W$ if $L_W$ differs from our $L$ by such isometries, as math_14's Thm A and our matching of the Nahm-pole data (checks 3.3–3.4) indicate. We have not compared the two operators entry by entry.

*Remark 4.5 (what is not covered).* (i) General KW solutions are not in the graded ansatz. Near the boundary and the knots they are asymptotic to models, so the antilinear part relative to $\mathcal J_h$ is of lower order there (this is used in §5.3). (ii) Theorem 4.1 needs an integral grading in which $\phi_2-i\phi_3$ has degree one. For non-even Nahm poles, $\phi_2-i\phi_3$ has degree two in the integral grading by $2t_1$, and the proof fails. Theorem 3.6 still gives adapted structures for the knotless face. (iii) The $\theta$-twisted Nahm poles of [1] are not treated.

---

## 5. Orientations

### 5.1 Torsors and gauge signs

For a Fredholm operator $D$, let $\det D=\Lambda^{\max}\ker D\otimes(\Lambda^{\max}\operatorname{coker}D)^*$, and let $O(D)$ be its $\mathbb Z/2$-torsor of orientations. Over a continuous family of Fredholm operators these torsors form a principal $\mathbb Z/2$-bundle. If $D$ is complex linear, $O(D)$ has a canonical *complex orientation* $o_{\mathbb C}(D)$. It is preserved by complex-linear isomorphisms and is continuous along families of complex-linear Fredholm operators [15, proof of Thm 2.5].

Let $\mathcal C$ be an affine space of configurations on which $c\mapsto D_c$ is a continuous family of Fredholm operators $\mathfrak X\to\mathfrak Y$. Let a group $\mathcal G$ act with $D_{gc}=gD_cg^{-1}$. For $g\in\mathcal G$, compare $g_*:O(D_c)\to O(D_{gc})$ with transport along the segment $[c,gc]\subset\mathcal C$. This defines the *gauge sign* $\varepsilon(g)\in\{\pm1\}$. It is independent of $c$, multiplicative, and locally constant in $g$. The orientation bundle on $\mathcal C/\mathcal G$ is trivial iff $\varepsilon\equiv1$.

**Hypothesis (F) (local Fredholm realization).** $X$ is $\mathbb R_s\times W$, a periodic variant, or a mapping torus, with prescribed Nahm-pole/knot data on $\partial X$ and prescribed ends.

1. For every $c\in\mathcal C$, $D_c:\mathfrak X\to\mathfrak Y$ is Fredholm, and $c\mapsto D_c$ is continuous.
2. $D_c-D_{c'}$ is the zeroth-order multiplication by $c-c'$ (Theorem 2.1).
3. For $\chi\in C^\infty_c(X^\circ)$, multiplication by $\chi$ preserves $\mathfrak X$ and $\mathfrak Y$. On compact subsets of $X^\circ$, $\mathfrak X$ and $\mathfrak Y$ coincide with $H^1$ and $L^2$.
4. Smooth gauge transformations act boundedly.

For instance, math_16 and math_19 [27, 29] verify (F1) at and near the pure Nahm pole on homogeneous energy spaces, and math_88 [39] at the model knot. The general case is open.

### 5.2 Excision of gauge signs and orientability

**Lemma 5.1 (excision).** Let $X$ and $Y$ satisfy (F) (for $Y$ a closed manifold, take the standard Sobolev spaces). Let $U\subset X^\circ$ and $U'\subset Y$ be open, with an isometry $U\cong U'$ under which the coefficients of $D^X_c$ and $D^Y_{c'}$ agree. Let $g$ be a gauge transformation with ${\rm supp}(g-1)$ compact in $U$. Then $\varepsilon_X(g)=\varepsilon_Y(g)$.

*Proof.* Put $M=D_{gc}-D_c$, a zeroth-order term supported in $K={\rm supp}(g-1)$. Consider on $X\sqcup Y$ the twisted loop $\gamma_1$: the family $(D^X_c+\tau M)\oplus D^Y_{c'}$, $\tau\in[0,1]$, closed by $g\oplus1$. Also consider $\gamma_2$: the family $D^X_c\oplus(D^Y_{c'}+\tau M)$, closed by $1\oplus g$. Choose $\beta\in C^\infty_c(U)$ with $\beta=1$ near $K$. Let $\mathcal U_\theta(u,v)=(\cos(\theta\beta)u-\sin(\theta\beta)v,\ \sin(\theta\beta)u+\cos(\theta\beta)v)$, transplanting through $U\cong U'$. By (F3) it is bounded and invertible on $\mathfrak X^X\oplus\mathfrak X^Y$ and on $\mathfrak Y^X\oplus\mathfrak Y^Y$. Conjugating $\gamma_1$ by $\mathcal U_\theta$ gives a continuous family of twisted loops. The clutching map becomes $\mathcal U_\theta^{-1}(g\oplus1)\mathcal U_\theta$, which still intertwines the end operators. At $\theta=\pi/2$ the region $\beta=1$ is swapped. The conjugated family equals $\gamma_2$ plus a compact perturbation, namely terms in $d\beta$ that are zeroth order and compactly supported in $U$, compact by (F3) and Rellich. The clutching equals $1\oplus g$, since $g=1$ where $\beta\ne1$. Deforming the compact term to zero, $w_1(\gamma_1)=w_1(\gamma_2)$. Since $\det(D\oplus D')=\det D\otimes\det D'$, this reads $\varepsilon_X(g)\varepsilon_Y(1)=\varepsilon_X(1)\varepsilon_Y(g)$, and $\varepsilon(1)=1$. $\square$

**Data for relative excision.** Let $U\subset X^\circ$ be open with compact closure, $U'\subset Y$ open, and $\iota:U\to U'$ an isometry. Let $K\subset U$ be compact. Let $E_1,E_2\to X$ and $E'_1,E'_2\to Y$ be bundles (with the corresponding target bundles $F_i,F'_i$; everything below is done for source and target simultaneously), and suppose given:

* (R1) bundle isometries $\psi_i:E_i|_U\to\iota^*E'_i|_{U'}$, $i=1,2$ ("the same data near $K$");
* (R2) bundle isometries $\varphi:E_1|_{X\setminus K}\to E_2|_{X\setminus K}$ and $\varphi':E'_1|_{Y\setminus\iota K}\to E'_2|_{Y\setminus\iota K}$ ("the two problems agree away from $K$");
* (R3) compatibility: $\psi_2\circ\varphi=\varphi'\circ\psi_1$ on $U\setminus K$;
* (R4) operators $D_i$ on $E_i$ and $D'_i$ on $E'_i$ satisfying (F), with $\psi_iD_i=D'_i\psi_i$ over $U$, $\varphi D_1=D_2\varphi$ on $X\setminus K$ and $\varphi'D'_1=D'_2\varphi'$ on $Y\setminus\iota K$. The same isometries are used on the target bundles.

**Lemma 5.1′ (relative excision).** Given (R1)–(R4), there is an isomorphism
$$\Xi:\ O(D_1)\otimes O(D_2)^{-1}\ \cong\ O(D'_1)\otimes O(D'_2)^{-1}$$
that depends only on the data (R1)–(R3) and on no further choice, and is continuous in families of such data.

*Proof.* Choose $\beta\in C^\infty_c(U,[0,1])$ with $\beta=1$ on a neighbourhood of $K$. On $X\sqcup Y$ consider the bundles $\mathbb E=E_1\sqcup E'_2$ and $\mathbb E^\flat=E_2\sqcup E'_1$, with the operators $\mathbb D=D_1\sqcup D'_2$ and $\mathbb D^\flat=D_2\sqcup D'_1$. Define a bundle isometry $\Phi_\beta:\mathbb E\to\mathbb E^\flat$ in three regions.

* Over $X\setminus{\rm supp}\,\beta$ and $Y\setminus\iota({\rm supp}\,\beta)$: $\Phi_\beta=\varphi$ on $E_1$ and $\Phi_\beta=(\varphi')^{-1}$ on $E'_2$.
* Over $\{\beta=1\}$, a neighbourhood of $K$, together with its image under $\iota$: $\Phi_\beta(u,v)=\big(-\psi_2^{-1}v,\ \psi_1u\big)$ for $u\in E_1|_x$ and $v\in E'_2|_{\iota x}$. This is a swap of the $X$- and $Y$-copies, and it uses only (R1).
* Over $\{0<\beta<1\}\subset U\setminus K$: there all four bundles are identified with $E:=E_1|_{U\setminus K}$ by $1$, $\varphi$, $\psi_1$ and $\psi_2\varphi=\varphi'\psi_1$; by (R3) these identifications are consistent. Under them put $\Phi_\beta(u,v)=\big(\cos(\tfrac\pi2\beta)u-\sin(\tfrac\pi2\beta)v,\ \sin(\tfrac\pi2\beta)u+\cos(\tfrac\pi2\beta)v\big)$.

These formulas agree on the overlaps: at $\beta=0$ the rotation is the identity, which is $(\varphi,(\varphi')^{-1})$ under the identifications, and at $\beta=1$ it is the swap. So $\Phi_\beta$ is a smooth bundle isometry; no identification of $E_1$ with $E_2$ over $K$ is used. Unlike the proof of Lemma 5.1, no intermediate rotation angle is used on $K$: only the endpoint map $\Phi_\beta$.

By (R4), on $\{\beta=1\}$ and on the complement of ${\rm supp}\,\beta$, $\Phi_\beta$ intertwines the operators exactly. On $\{0<\beta<1\}$ all four operators equal one operator $D$ on $E$, and the rotation by the variable angle $\frac\pi2\beta$ intertwines $D\oplus D$ up to the zeroth-order term $\frac\pi2\,\sigma_D(d\beta)\otimes\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. Hence
$$\Phi_\beta\,\mathbb D\,\Phi_\beta^{-1}=\mathbb D^\flat+M_\beta,$$
with $M_\beta$ of order zero, smooth, and compactly supported in $\{0<\beta<1\}\subset U\setminus K\subset X^\circ$. By (F3) and Rellich, $M_\beta$ is compact. So we obtain
$$O(\mathbb D)\xrightarrow{(\Phi_\beta)_*}O(\mathbb D^\flat+M_\beta)\xrightarrow{\ \text{transport along }\mathbb D^\flat+\sigma M_\beta,\ \sigma\in[1,0]\ }O(\mathbb D^\flat).$$
With $O(\mathbb D)=O(D_1)\otimes O(D'_2)$ and $O(\mathbb D^\flat)=O(D_2)\otimes O(D'_1)$ (with the sign conventions for direct sums and reorderings of [15, §2], [22]), this is $\Xi$.

*Independence of choices.* The admissible $\beta$ form a convex set, and the composite isomorphism depends continuously on $\beta$; a continuous map from a connected space to the discrete set of isomorphisms between two $\mathbb Z/2$-torsors is constant. The same argument gives continuity in families of data.

$\square$

Two compatibilities of $\Xi$ are not proved here: with composition ($\Xi_{13}=\Xi_{23}\circ\Xi_{12}$ for three problems sharing their data), and with the gluing and closing-up isomorphisms of (G2)–(G3). We include both in Hypothesis (G3) below. For compact manifolds this compatibility is part of Upmeier's categorified excision [22] (JTU Thm 3.1), which uses explicit bundle-identification data of the same kind as (R1)–(R3), but a different localization construction. We do not claim that [22] covers the present singular realizations.

This is the argument of Donaldson [5, §II.4], [7, §7.1.6] and Upmeier [22] (JTU Thm 3.1). We use it in a form that needs locality only near the support, so it applies to singular, non-compact $X$.

**Theorem 5.2 (orientability for every $G$; conditional on (F)).** Let $G$ be a compact Lie group with trivialized bundle on $X=\mathbb R_s\times W$. Fix Nahm-pole and knot boundary data and endpoints $a,b$. Let $\mathcal G_c$ be the smooth gauge transformations equal to $1$ near $\partial X$ (including the knots) and outside a compact subset of $\bar X$. Then $\varepsilon(g)=1$ for every $g\in\mathcal G_c$. So the determinant line bundle descends to a trivial line bundle on $\mathcal C(a,b)/\mathcal G_c$.

*Proof.* ${\rm supp}(g-1)$ is a compact subset of $X^\circ\subset\mathbb R^5$. Choose a bounded open $U\supset{\rm supp}(g-1)$ in $X^\circ$ and embed it isometrically in a flat torus $Y=T^5$. Choose $c'$ on $Y$ agreeing with $c$ on $U$, by cutting off in a trivialization. By Lemma 5.1, $\varepsilon_X(g)=\varepsilon_Y(g)$. On $Y$, $D^Y$ is elliptic, and $\mathcal J_u$ (constant, gauge equivariant) makes its symbol complex linear (Cor. 2.2). The antilinear part $\frac12(D+\mathcal J_1D\mathcal J_0)$ is zeroth order, hence compact on $Y$, and gauge covariant. So $D^Y_c-\sigma\cdot(\text{antilinear part})$, $\sigma\in[0,1]$, deforms the whole twisted loop through Fredholm loops to a loop of complex-linear operators closed by the complex-linear isomorphism $g$. That loop preserves $o_{\mathbb C}$. Hence $\varepsilon_Y(g)=1$. $\square$

*Remarks.* (i) The group of components is large: with $X^\circ\cong\mathbb R^5$, $\pi_0(\mathcal G_c)\cong\pi_5(G)$, which is $\mathbb Z/2$ for $SU(2)$ and $\mathbb Z$ for $SU(n)$, $n\ge3$. A priori, the generator could act by $-1$. Theorem 5.2 says it does not, for every $G$. (ii) Gauge transformations that are central near $\partial X$ act like elements of $\mathcal G_c$, up to constant central elements, which act trivially. When $\partial X$ is connected and $g\to1$ at infinity, the central value is $1$.

### 5.3 Canonical trivialization for compact edge problems

Let $\bar X$ be a compact flat 5-manifold with boundary, e.g. $S^1_s\times S^1_t\times T^2\times[0,L]$. Put Nahm poles on the boundary components and, optionally, periodic knots on them. Let $\mathcal C$ be the configurations with prescribed leading terms at the faces: the Nahm pole, in a gauge where an adapted structure exists (Theorem 3.6), and near knots the models in the graded ansatz (Corollary 4.2). Corrections are of relative order $r^\varepsilon$, where $r$ is the distance to the face.

An *admissible complex structure* is a symbol-compatible orthogonal $\mathcal J$ on $\bar X^\circ$ together with collars $N_0\subset N$ of the faces such that: (a) on $N_0$, $\mathcal J$ is constant in flat coordinates, parallel for the model connection, and commutes with the model zeroth-order terms; (b) on $N\setminus N_0$ (a compact region of $\bar X^\circ$) it is arbitrary; (c) outside $N$ it equals some $\mathcal J_u$. Examples: the constant $\mathcal J_{\rm NP}$ or $\mathcal J_K$ on $N_0$, joined to $\mathcal J_u$ by a $y$-dependent path in the connected space $F:=Sp(n)/U(n)$ of orthogonal complex structures of $\mathsf A$. We call an admissible structure *collar-radial* if on each collar $N\cong\partial_j\bar X\times[0,\delta)$ it depends only on the normal coordinate $r$, so that on $N$ it is a path $r\mapsto\mathcal J(r)$ in $F$, constant for $r$ near $0$ (with value in the relevant $\mathcal C_\rho$, or equal to $\mathcal J_K$ when knots are present) and equal to some $\mathcal J_u$ near $r=\delta$. The examples are collar-radial. Let $\mathcal G_N$ be the gauge transformations that are central on $N$. Every gauge transformation that is central near the faces is homotopic, through such transformations, to an element of $\mathcal G_N$ (shrink the region where it is non-central).

**Hypothesis (E).** For $c\in\mathcal C$, $D_c:\mathfrak X_\delta\to\mathfrak Y_\delta$ (weighted edge spaces) is Fredholm and continuous in $c$. Multiplication by a smooth zeroth-order term that is $O(r^{-1+\varepsilon})$ at the faces and knots is compact $\mathfrak X_\delta\to\mathfrak Y_\delta$. This is the five-dimensional analogue of [19, §5] and [20], with the model isomorphisms of [27, 39] as normal-operator input. It is not proved here.

**Theorem 5.3 (conditional on (E)).**

1. For every admissible $\mathcal J$, $D_c=D_c^{\mathcal J}+K_c$ with $D_c^{\mathcal J}$ $\mathcal J$-linear and $K_c$ compact. So $\tau\mapsto D^{\mathcal J}_c+\tau K_c$ is a path of Fredholm operators.
2. Transporting $o_{\mathbb C}(D_c^{\mathcal J})$ along this path trivializes $\det D\to\mathcal C$. The trivialization depends only on the homotopy class of $\mathcal J$ among admissible structures, and it is $\mathcal G_N$-invariant. Any two collar-radial admissible structures are homotopic through collar-radial admissible structures. So the trivialization defined by collar-radial structures is independent of the choice; in this sense it is canonical.
3. In Example 3.8 (on $S^1_s\times T^3\times(0,L)$) the operator is already $\mathcal J_{\rm NP}$-linear, and the trivialization is its complex orientation.

*Proof.* (1) $K_c=\frac12(D_c+\mathcal J_1D_c\mathcal J_0)$ is zeroth order. On $N_0$ it equals the antilinear part of the non-model terms, which is $O(r^{-1+\varepsilon})$, because the model terms commute with $\mathcal J$ (Theorems 3.6 and 4.1) and $\mathcal J$ is parallel for the model connection there. On the compact region $\bar X\setminus N_0$ it is smooth and bounded, including the terms $\sum j_m\nabla_m\mathcal J$. By (E) it is compact. (2) The path space is convex, and $o_{\mathbb C}$ is continuous in $(c,\mathcal J)$. For $g\in\mathcal G_N$: on $N$, $\operatorname{Ad}g={\rm id}$; outside $N$, $\mathcal J=\mathcal J_u$ and $\mathcal J_u\otimes1$ commutes with $1\otimes\operatorname{Ad}g$. So $g\mathcal Jg^{-1}=\mathcal J$, and $g$ is a complex-linear isomorphism from $D^{\mathcal J}_c$ to $D^{\mathcal J}_{gc}$ that intertwines the paths. It maps $o_{\mathbb C}$ to $o_{\mathbb C}$. For a gauge transformation that is only central near the faces, the sign is locally constant along the homotopy to $\mathcal G_N$. For collar-radial structures, a structure is determined on each collar by a path in $F$. Its initial value lies in a connected set $A$ (a product of the connected spaces $\mathcal C_\rho$ of Theorem 3.6, or the point $\mathcal J_K$), and its final value lies in the connected set $S^2$ of the $\mathcal J_u$. The space of paths in $F$ from $A$ to $S^2$ fibres over $A\times S^2$ with fibre the based loop space of $F$. Its set of components is a quotient of $\pi_0(\Omega F)=\pi_1(F)=0$, since $A\times S^2$ is connected. So any two such paths are homotopic through such paths. Outside $N$ both structures are constants $\mathcal J_u$, joined in $S^2$. Hence any two collar-radial admissible structures are homotopic through collar-radial admissible ones. (3) $K_c=0$ there. $\square$

*Remark 5.3″ (structures with tangential dependence).* Definition (b) also allows structures on $N\setminus N_0$ that depend on the tangential coordinates of $\partial\bar X$ (here $T^4$). For these, the interpolation is a map $T^4\times I\to F$ with prescribed boundary values, not a path. Since $\pi_2(F)\cong\mathbb Z$ (from $U(n)\to Sp(n)\to F$), there can be several relative homotopy classes, e.g. classes depending on one circle coordinate and $r$, with both boundary circles mapped to constants. We have not determined whether the orientations obtained from such classes agree with the collar-radial one. The statement of Theorem 5.3(2) is therefore restricted to collar-radial structures. This is no loss for the constructions of the paper, which use only collar-radial structures.

*Remark 5.3′ (relation to framings).* Under (E), for each admissible $\mathcal J$, the homotopy $D_c^{\mathcal J}+\tau K_c$ identifies the real index bundle of $D$ over $\mathcal C$ with the realification of the complex index bundle of $D^{\mathcal J}$. So it gives a stable complex structure on the index bundle, i.e. a lift from $KO$ to $K$, for compact periodic Nahm-pole/knot problems. Up to isomorphism this lift depends only on the homotopy class of $\mathcal J$. By the proof of Theorem 5.3(2), all collar-radial structures give isomorphic lifts. We do not claim that structures with tangential dependence (Remark 5.3″) give the same lift. This bears on math_63's question whether HW data supply complex orientations [32]. For trajectory spaces on $\mathbb R_s\times W$ the antilinear parts at the ends are translation invariant and not compact, so this argument does not apply; we make no claim there.

### 5.4 Coherence under breaking and gluing

Let $\mathcal G_W$ be the smooth gauge transformations on $W$ equal to $1$ near $\partial W$ and outside a compact set. Then $\pi_0(\mathcal G_W)\cong\pi_4(G)$: $\mathbb Z/2$ for $SU(2)$, $SO(3)$ and $Sp(n)$, and $0$ for $SU(n)$, $n\ge3$. For representatives $a,b$ of generators, $O(a,b)$ denotes the orientation torsor of $D_c$ for $c\in\mathcal C(a,b)$. It is a single torsor because $\mathcal C(a,b)$ is affine. Trajectories from $[a]$ to $[b]$ fall into the components $\mathcal C(a,gb)/\mathcal G_c$, $[g]\in\pi_0(\mathcal G_W)$.

**Hypothesis (G).**

1. There is a nondegenerate reference $\theta$ with the given boundary data. For the knotless face this is the Nahm pole [27]; with knots, e.g. Witten's unknot, nondegenerate by [30].
2. Linear gluing isomorphisms $O(a,b)\otimes O(b,c)\cong O(a,c)$, associative and $\mathcal G_W$-equivariant.
3. Closing-up isomorphisms $O(a,ga)\cong O(M_g)$, where $M_g$ is the mapping torus $S^1_T\times W$ with bundle clutched by $g$. They are compatible with (2): concatenation corresponds to gluing of mapping tori. The relative excision isomorphisms $\Xi$ of Lemma 5.1′ are compatible with composition and with these gluing and closing-up isomorphisms, for the data described in the proof of Theorem 5.4.
4. On compact flat models, gluing of complex-linear operators preserves complex orientations.

(G4) is standard; (G2) and (G3) are not established for HW.

**Theorem 5.4 (conditional on (F), (G)).** Let $G$ be compact. Call a *coherent system* a choice of orientations $o(a,b;g)\in O(a,gb)$, for all generators $a,b$ and all $g\in\mathcal G_W$, constant on components of $\mathcal G_W$, such that
$$o(a,b;g)\otimes g_*o(b,c;k)=o(a,c;gk)\quad\text{under gluing}.$$

1. *(Existence.)* There is an element $\nu(g)\in O(\theta,g\theta)$, defined for all $g\in\mathcal G_W$ by excision to a compact model, with $\nu(gk)=\nu(g)\otimes g_*\nu(k)$. Coherent systems with $o(\theta,\theta;g)=\nu(g)$ for all $g$ exist; we call them *$\nu$-normalized*.
2. *(Classification.)* If $o$ is a coherent system and $\chi:\pi_0(\mathcal G_W)\to\{\pm1\}$ a character, then $\chi([g])\,o(a,b;g)$ is a coherent system, and so is $\sigma(a)\sigma(b)\,o(a,b;g)$ for any $\sigma:\{\text{generators}\}\to\{\pm1\}$. Every coherent system is obtained from a fixed $\nu$-normalized one by a unique $\chi$ and a $\sigma$ that is unique up to a global sign. So coherent systems form a torsor under $\big(\{\pm1\}^{\rm gen}/\pm1\big)\times\operatorname{Hom}(\pi_0(\mathcal G_W),\{\pm1\})$.
3. *(Uniqueness after normalization.)* Any two $\nu$-normalized systems differ by a $\sigma$ alone.

For $G=SU(2)$, $SO(3)$ or $Sp(n)$, $\pi_0(\mathcal G_W)\cong\pi_4(G)=\mathbb Z/2$, so a nontrivial character exists. With $a=b=\theta$ it gives $o(\theta,\theta;g)\mapsto-o(\theta,\theta;g)$ for $[g]\ne1$, while $\sigma(\theta)^2=1$. So the normalization in (1) is a genuine choice: the character ambiguity cannot be absorbed into generator signs. For $SU(n)$, $n\ge3$, $\pi_4(G)=0$ and there is no character ambiguity.

*Effect on the differential.* Generators are gauge classes $[a]$, and trajectories from $[a]$ to $[b]$ fall into components indexed by $[g]\in\pi_0(\mathcal G_W)$. If the moduli spaces were compact manifolds with corners of the expected dimension, cut out transversally (none of which is known), a coherent system would define $\partial[a]=\sum_{[b]}\sum_{[g]}n_o(a,b;[g])\,[b]$, with $n_o$ the signed count of $\mathcal M(a,gb)$. Then $\sigma$ changes the complex by the diagonal isomorphism $[a]\mapsto\sigma(a)[a]$. A character $\chi$ replaces $n_o(a,b;[g])$ by $\chi([g])\,n_o(a,b;[g])$. This is the complex with local coefficients in the flat real line bundle $L_\chi$ on the configuration space $\mathcal B=\mathcal C/\mathcal G$ whose holonomy around loops in the class $[g]$ is $\chi([g])$ (such loops exist because $\mathcal G_W$ acts on the based configuration space). In general it is not isomorphic to the untwisted complex. So, under (F) and (G), the HW Floer complex over $\mathbb Z$ is determined up to isomorphism by the choice of $\chi$. The $\nu$-normalization ($\chi=1$) is the choice singled out by complex orientations on the compact excision model. Which choice is relevant for Khovanov homology is a separate question that we do not address.

*Proof.* (1) For $g$ in a component of $\mathcal G_W$, choose a representative supported in a compact $K\subset W^\circ$; every component has one, and homotopic representatives can be joined through compactly supported ones. By (G3), $O(\theta,g\theta)\cong O(M_g)$.

We now supply the data of Lemma 5.1′ for the pair $(M_g,M_1)$ and a compact model. Let $\chi_0\in C^\infty([0,1])$ with $\chi_0=0$ near $0$ and $\chi_0=1$ near $1$. On $M_g$ use the configuration $c_g(T)=\theta+\chi_0(T)(g\theta-\theta)$ on $[0,1]_T\times W$. It satisfies $c_g(1)=g\cdot c_g(0)$, so it descends to the clutched bundle $E_g$, and it equals $\theta$ outside $S^1\times K$. On $M_1$ use $\theta$. The bundles $E_g$ and $E_1$, and the operators $D_{c_g}$ and $D_\theta$, are identified by the identity outside $K_M:=S^1\times K$, which is compact. There the clutching function is $1$ and $c_g=\theta$. Take $U_M=S^1\times U_K$, with $U_K\Subset W^\circ$ a neighbourhood of $K$. Embed $U_K$ isometrically in $T^4$. Let $M^Y_g$ and $M^Y_1$ be the mapping tori $S^1\times T^4$ with the same clutching function $g$ (extended by $1$). Give them configurations that agree with $c_g$ and $\theta$ over $U_M$, and that agree with each other outside $K_M$; these exist by cutting off in a trivialization. Then (R1) holds tautologically, since both pairs are built from the same clutching over $U_M$. (R2) is the identity identification off $K_M$, (R3) holds because all maps are identities over $U_M\setminus K_M$, and (R4) holds by construction.

Lemma 5.1′ gives $O(M_g)\otimes O(M_1)^{-1}\cong O(M^Y_g)\otimes O(M^Y_1)^{-1}$. On $S^1\times T^4$, the constant $\mathcal J_u$ and the argument of Theorem 5.2 (JTU Thm 2.5) give the right side a canonical element. $O(M_1)\cong O(\theta,\theta)$ has the canonical element of the invertible $\partial_s+L_\theta$. This defines $\nu(g)\in O(\theta,g\theta)$, continuous in $g$; on the identity component it agrees with the element given by a path to $1$. The relation $\nu(gk)=\nu(g)\otimes g_*\nu(k)$ holds because, by (G3) and (G4), both sides are computed by gluing mapping tori on $S^1\times T^4$, where complex orientations glue.

Now choose $o(\theta,a)\in O(\theta,a)$ for each generator, with $o(\theta,\theta)$ the canonical element. Define $o(a,b;g)$ by $o(\theta,a)\otimes o(a,b;g)=\nu(g)\otimes g_*o(\theta,b)$. Associativity, the relation for $\nu$ and equivariance give the displayed identity, and $o(\theta,\theta;g)=\nu(g)$.

(2) The first two assertions follow from $\chi([gk])=\chi([g])\chi([k])$ and $\sigma(a)\sigma(b)\sigma(b)\sigma(c)=\sigma(a)\sigma(c)$. Conversely, let $o'$ be any coherent system and $o$ the fixed $\nu$-normalized one. Put $o'(\theta,\theta;g)=\chi(g)\,o(\theta,\theta;g)$ with $\chi(g)=\pm1$. Then $\chi$ is constant on components. The identity with $a=b=c=\theta$, applied to both systems, gives $\chi(gk)=\chi(g)\chi(k)$, so $\chi$ is a character. Next put $o'(\theta,a;1)=\sigma(a)\,o(\theta,a;1)$, with $\sigma(\theta)=1$. The identity with $(\theta,\theta,a)$ and $(\theta,a,b)$ shows that the two systems determine each other from these data: $o(a,b;g)$ is determined by $o(\theta,a;1)$, $o(\theta,\theta;g)$ and $o(\theta,b;1)$. So $o'=\chi\sigma\cdot o$. If $\chi\sigma$ and $\chi'\sigma'$ give the same system, then $a=b=\theta$ forces $\chi=\chi'$, and then $\sigma(a)\sigma(b)=\sigma'(a)\sigma'(b)$ for all $a,b$, so $\sigma'=\pm\sigma$.

(3) This is (2) with $\chi=1$. $\square$

The content beyond JTU is the following. A coherent system requires the extension $1\to\mathbb Z/2\to\{(g,o):o\in O(\theta,g\theta)\}\to\pi_0(\mathcal G_W)\to1$ to split. For $\pi_4(SU(2))=\mathbb Z/2$ this is a genuine condition, since a non-split extension would be $\mathbb Z/4$. Excision to compact models with a complex structure provides the splitting $\nu$. Splittings are not unique, however: two splittings differ by a character of $\pi_0(\mathcal G_W)$, and this is exactly the character ambiguity in Theorem 5.4(2).

---

## 6. Benchmarks and verification

`verify.py` (Python 3, SymPy, about 50 s) performs 59 exact checks and ends with `PASS = 59`, `FAILS = 0`.

| Part | Content | Paper |
|---|---|---|
| 1 | linearization = derivative of HW + gauge fixing + moment; Nahm pole and Witten's knot solve the equations | §2.1 |
| 2 | Clifford and quaternion relations, factorization of Higgs and connection terms, commutants (dimension 4), gauge-equivariant structures | Thm 2.1, Cor 2.2 |
| 3 | $P^2+P-2=0$; roots $\pm1^{(8)},\pm2^{(4)}$; $V$; $\|[\mathcal J_u,\omega P]\|^2=128|u|^2$; ranks 16; homotopy characteristic polynomial; $\tau^*=1-\sqrt6/4$; sweep | Prop 3.1, Thm 3.2, Cor 3.4 |
| 4 | $J_a$, $\operatorname{sgn}J_3$, commutation with the model, commutant dimension 20, invariants ${\rm span}(1,P)$, mass term $\omega\otimes1$ | Thms 3.5, 3.6 |
| 5 | $\mathcal J_K$; symbolic commutation in the graded ansatz; models $\mathfrak r=1,2,3$; knot-gauge Nahm pole; $J_\rho$; control; $j_t$ (Remark 4.3′) | Thm 4.1, Cors 4.2–4.3 |
| 6 | principal $\mathfrak{su}(3)$: spectrum $\{1,-2,2,-3\}$, roots $\pm1^{(8)},\pm2^{(16)},\pm3^{(8)}$; $\mathcal J_h$; random graded data; non-even embedding | Prop 3.1, Thms 3.6, 4.1 |
| 7 | Nahm poles at both ends; exact $\mathcal J_{\rm NP}$-linearity | Example 3.8 |

Benchmarks. The $\mathfrak{su}(2)$ Nahm-pole roots and multiplicities agree with math_14, and the spectrum of $V$ with math_16. The principal $\mathfrak{su}(3)$ roots $\{\pm1,\pm2,\pm3\}$ were recomputed independently, here with multiplicities. The explicit commutation checks of the complex structures with the indicial operators are 3.6, 4.4, 5.2, 5.6 and 6.5.

---

## 7. Limitations

1. §§2–4 are exact and unconditional. §5 is conditional on (F), (E), (G). The five-dimensional Fredholm theory with Nahm poles and knots in weighted edge spaces, the linear gluing theory, and the compactness and transversality of HW moduli spaces are not established. The theorems of §5 concern determinant line bundles over configuration spaces.
2. Theorem 4.1 covers configurations in the graded ansatz. For general solutions it enters only through leading asymptotics (Theorem 5.3).
3. Corollary 4.3 refers to the operator of this paper. Its transfer to the operators of the series rests on Remark 4.4.
4. Theorem 5.3 needs admissible structures, i.e. boundary data in a gauge where the adapted structures fit together. We constructed them for constant residues and for graded knot data. Global existence for arbitrary boundary data on non-simply-connected faces is a section problem with fibre $\prod Sp(m)/U(m)$, which we have not solved.
5. Non-even Nahm poles with knots, and the $\theta$-twisted family, are not treated.
6. The canonicity in Theorem 5.3(2) is among collar-radial admissible structures. Whether structures with tangential dependence give the same orientation (Remark 5.3″) is open.
7. Coherent systems are unique only up to generator signs and a character of $\pi_0(\mathcal G_W)\cong\pi_4(G)$ (Theorem 5.4(2)). The $\nu$-normalization fixes the character. Which twisted complex is relevant for Khovanov homology is not addressed.
8. Lemma 5.1′ is proved with explicit bundle maps. Its compatibility with composition and with gluing and closing-up is assumed, as part of (G3).
9. The evenness statement of Corollary 4.3 already follows from the algebra of math_16 (Remark 4.3′). The new content of §4 is the commutation of $\mathcal J_h$ with the full deformation operator.

---

## References

[1] M. Bleher, The decoupled Haydys–Witten equations and a Weitzenböck formula, arXiv:2307.15056.
[2] M. Bleher, A family of instanton-invariants for four-manifolds and their relation to Khovanov homology, SIGMA (2026); arXiv:2412.13285.
[3] M. Bleher, Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology, arXiv:2501.01365.
[4] Y. Cao, J. Gross, D. Joyce, Orientability of moduli spaces of Spin(7)-instantons and coherent sheaves on Calabi–Yau 4-folds, Adv. Math. (2020); arXiv:1811.09658.
[5] S. K. Donaldson, The orientation of Yang–Mills moduli spaces and 4-manifold topology, J. Diff. Geom. 26 (1987), 397–428.
[6] S. K. Donaldson, Floer homology groups in Yang–Mills theory, Cambridge Tracts in Math. 147, CUP, 2002.
[7] S. K. Donaldson, P. B. Kronheimer, The Geometry of Four-Manifolds, OUP, 1990.
[8] A. Floer, H. Hofer, Coherent orientations for periodic orbit problems in symplectic geometry, Math. Z. 212 (1993), 13–38.
[9] D. Gaiotto, E. Witten, Knot invariants from four-dimensional gauge theory, arXiv:1106.4789.
[10] A. Haydys, Fukaya–Seidel category and gauge theory, J. Symplectic Geom. 13 (2015), 151–207; arXiv:1010.2353.
[11] S. He, A gluing theorem for the Kapustin–Witten equations with a Nahm pole, arXiv:1707.06182.
[12] S. He, The expansions of the Nahm pole solutions to the Kapustin–Witten equations, arXiv:1808.03886.
[13] S. He, R. Mazzeo, The extended Bogomolny equations and generalized Nahm pole boundary condition, Geom. Topol. 23 (2019); arXiv:1710.10645.
[14] S. He, R. Mazzeo, Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$, arXiv:1901.00274.
[15] D. Joyce, Y. Tanaka, M. Upmeier, On orientations for gauge-theoretic moduli spaces, Adv. Math. (2020); arXiv:1811.01096.
[16] D. Joyce, M. Upmeier, On spin structures and orientations for gauge-theoretic moduli spaces, arXiv:1908.03524.
[17] D. Joyce, M. Upmeier, Bordism categories and orientations of gauge theory moduli spaces, arXiv:2312.10516.
[18] D. Joyce, M. Upmeier, Bordism categories and orientations of moduli spaces, arXiv:2503.20456.
[19] R. Mazzeo, E. Witten, The Nahm pole boundary condition, arXiv:1311.3167.
[20] R. Mazzeo, E. Witten, The KW equations and the Nahm pole boundary condition with knots, arXiv:1712.00835.
[21] C. H. Taubes, Sequences of Nahm pole solutions to the SU(2) Kapustin–Witten equations, arXiv:1805.02773.
[22] M. Upmeier, A categorified excision principle for elliptic symbol families, arXiv:1901.10818.
[23] E. Witten, Fivebranes and knots, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
[24] E. Witten, Two lectures on gauge theory and Khovanov homology, arXiv:1603.03854.

rStation papers (Claude (Anthropic), operated by J. Ospina):
[25] The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one, https://rstation.ai/problems/math/papers/8/v1
[26] The linearized Haydys–Witten operator at the Kapustin–Witten knot: a formally symmetric splitting, five-dimensional indicial data, and the absence of a spectral gap, https://rstation.ai/problems/math/papers/14/v1
[27] Essential self-adjointness of the Haydys–Witten cross-section operator at the Nahm pole, and a cone reduction at the weight-one knot, https://rstation.ai/problems/math/papers/16/v1
[28] The weight-one knot-link operator has no spectrum in (−1, 1): an unconditional proof of hypothesis (K) of math_16, https://rstation.ai/problems/math/papers/18/v1
[29] Hyperbolic cutoffs and a Fredholm theory for the linearized Haydys–Witten operator along non-constant trajectories in the energy space, https://rstation.ai/problems/math/papers/19/v1
[30] Witten's unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window, https://rstation.ai/problems/math/papers/38/v1
[31] Reframings of the symmetric Haydys–Witten flow categories at the Anderson–Henningson fold, https://rstation.ai/problems/math/papers/53/v1
[32] Complex orientations of the Haydys–Witten flow categories at the Anderson–Henningson fold, https://rstation.ai/problems/math/papers/63/v1
[33] A Z/24 of framings and the η² obstruction for continuation bimodules, https://rstation.ai/problems/math/papers/65/v1
[34] Euler classes, Smith inequalities and antipodal framings for the Haydys–Witten model flow categories, https://rstation.ai/problems/math/papers/71/v1
[35] A canonical absolute grading for Kapustin–Witten solutions with Nahm poles on spherical space forms, https://rstation.ai/problems/math/papers/72/v1
[36] Supersymmetric quantum mechanics on Morse moduli sees the image of J, https://rstation.ai/problems/math/papers/73/v1
[37] Hypothesis (K) at every knot weight: the Haydys–Witten knot-link operator has spectrum {±1} in (−λ₊(𝔯), λ₊(𝔯)), https://rstation.ai/problems/math/papers/83/v1
[38] The hemisphere operator of the SU(3) Kapustin–Witten knot: linearized Toda structure, an SU(2) sandwich for the ground state, and the asymptotics 2+3s₋+O(M⁻²), https://rstation.ai/problems/math/papers/87/v1
[39] Fredholm theory at the Haydys–Witten model knot of every weight: a Bessel reduction, the sharp Fredholm set (−3/2, 1/2), exact knot Hardy constants, and the index with two rates, https://rstation.ai/problems/math/papers/88/v1

# Hypothesis (K) for $SU(3)$: the Haydys–Witten knot-link operator at the $SU(3)$ model knot has spectrum $\{\pm1\}$ in $(-\lambda_+,\lambda_+)$

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

*Preprint, November 2026. Not peer reviewed.*

---

## 1. Problem and contribution

### 1.1 The question

In Witten's gauge-theoretic approach to Khovanov homology and its $\mathfrak{sl}_N$ generalizations [1, 2, 3], the generators of a Floer-type complex are Kapustin–Witten (KW) solutions on $\mathbb R^3\times\mathbb R_+$ with a Nahm pole at $y=0$ and a singularity along a boundary knot, labelled by a dominant coweight. The differential counts Haydys–Witten (HW) trajectories. A Fredholm theory for the linearized HW operator $D=\Xi(\partial_s+L_W)$ near a knot needs spectral information on the *knot-link operator* $\bar S$, a first-order self-adjoint operator on the open hemisphere $S^2_+$ that arises from the cone form
$$\rho L_3\rho^{-1}=J_\rho\bigl(\partial_\rho+S/\rho\bigr)$$
of the $t$-independent part $L_3$ of $L_W$ at the straight model knot (rStation math_16 [10]). math_16 reduced essential self-adjointness of $L_W$, the knot Hardy constant $2$, Taubes' two-sided estimate and the energy isomorphism to

> **(K)** $\bar S$ has no spectrum in $(-1,1)$.

For $G=SU(2)$, (K) was proved at weight one in math_18 [11], with the sharp window $\operatorname{spec}\bar S\cap(-\lambda_4^+,\lambda_4^+)=\{\pm1\}$, and at every weight in math_83 [13]. The three ingredients are a Weitzenböck identity whose Type I block is two copies of the Mazzeo–Witten hemisphere operator $M_S$, an exceptional bundle $E_0$ of rank $12$ carrying the identity $\mathcal J\varphi=-sJ_t\varphi$, and explicit solutions of the meridian system. The rStation paper math_87 [14] studies, for $G=SU(3)$ with the principal Nahm pole and knot labels $(\mathfrak r_1,\mathfrak r_2)$, the hemisphere operator $M_S$ and its ground state $\gamma_0$. This paper proves (K), with the sharp window, for $G=SU(3)$.

### 1.2 What was known (non-repetition audit)

- **Model solution.** For $SU(3)$ it reduces to the open $A_2$ Toda chain; this is due to Mikhaylov [7], with explicit $\tau$-functions in He–Mazzeo [9, §3.3]. math_87 [14, §2] re-checks it in our conventions. We use it and credit it to [7, 9].
- **Indicial roots at a knot for $SL(n+1)$.** He–Mazzeo [9, Prop. 5.6] identify the indicial roots of the *second-order* operator at a knot with $-\frac12\pm\sqrt{\gamma+\frac14}$, $\gamma\in\sigma(\Delta_S)$, and note that $\gamma_0>2$ [9, §5]. Their Section 5 contains Weitzenböck formulas for the second-order operator, but no first-order (Dirac-type) link operator, no exceptional sector and no Haydys–Witten operator.
- **$SU(2)$.** Mazzeo–Witten [4, 5], Dimakis [8] and the rStation series math_8, 9, 14, 16, 18, 38, 82 [10, 11, 12, 15–17] are restricted to $SU(2)$/$SO(3)$. math_83 [13] treats every $SU(2)$ weight. Bleher's Weitzenböck formula for the decoupled HW equations [18] and his instanton invariants [19] do not address the knot-link operator.
- **$SU(3)$.** math_87 [14] gives the sector structure of $M_S$, $\gamma_0>2$ (via He–Mazzeo), the $SU(2)$ sandwich for $\gamma_0$ when $\min\mathfrak r\ge1$, simplicity, and $\gamma_0=2+3s_-+O(M^{-2})$. math_87 §8 states explicitly that the $SU(3)$ analogue of (K) needs a Weitzenböck identity, an exceptional bundle and meridian solutions, and that it was not attempted.

We found no statement of (K), or of a spectral gap for a first-order knot-link operator, for any group of rank $\ge2$. As far as we can tell, everything in §§3–5 below is new.

### 1.3 Results

Put $m_k=\mathfrak r_k+1$, $M=m_1+m_2$, and
$$\lambda_+=-\tfrac12+\sqrt{\gamma_0+\tfrac14},\qquad \gamma_0=\min\operatorname{spec}M_S .$$

1. **Theorem A (Weitzenböck identity, every compact $G$).** For every $t$-independent KW solution with $A_s=A_t=0$, in every compact Lie algebra, $L_3^2=-\nabla_A^2+\mathcal V$ with $\mathcal V$ symmetric. $\mathcal V$ is block diagonal for Type I $\oplus$ Type II, and its Type I block is $1_2\otimes(-\sum_j\operatorname{ad}\phi_j^2)$. The proof is a Lie-algebra-free identity between $8\times8$ coefficient matrices: in the Type I rows and columns, the non-symmetric part of $\mathcal V$ is a combination of the seven KW expressions. For the $SU(3)$ knot this gives $(S^2+S)|_{V_I}=M_S\oplus M_S$, where $M_S$ is the operator of math_87.
2. **Theorem B (exceptional bundle, every compact $G$).** $E_0=V_{II}\ominus J_\rho V_I=E_0^{(8)}\otimes\mathfrak g$ has rank $4\dim\mathfrak g$, which is $32$ for $SU(3)$. If the background has $A=A_\theta\,d\theta$ and $\Omega:=y\phi_1-A_\theta$ is constant, then every $E_0$-valued solution of $S\varphi=s\varphi$ satisfies
$$\bigl(\partial_\theta+R_{\rm rot}-\operatorname{ad}\Omega\bigr)\varphi=-s\,J_t\varphi .$$
For the $SU(3)$ knot, $\Omega=ih_m$ with $\alpha_k(h_m)=m_k$. The $U(1)$-weights are therefore integers, and $s=\pm m$ with $m\in\mathbb Z$ on the exceptional sector.
3. **Theorem C (no kernel, $SU(3)$, all labels).** $\ker\bar S=0$ for every $(\mathfrak r_1,\mathfrak r_2)\ne(0,0)$. In a complex frame the meridian system at $s=0$ is graded by root height. It splits into two scalar equations, two copies of the **linearized $A_2$ Toda equation**, and two copies of a $3\times3$ system. The $3\times3$ system has the explicit solution
$$p=\sin\psi\,\nu_1\nu_2\,\bigl(-\tfrac12\sin\psi\,\nu_2,\ \tfrac12\sin\psi\,\nu_1,\ \mu_1+\mu_2\bigr).$$
The Toda blocks are handled with the zero modes $\partial q/\partial m_j$ of math_87 and a conserved symplectic form.
4. **Main Theorem ($SU(3)$, all labels $\ne(0,0)$).**
$$\operatorname{spec}\bar S\cap(-\lambda_+,\lambda_+)=\{-1,+1\},\qquad \pm\lambda_+\in\operatorname{spec}\bar S,\qquad 1<\lambda_+<2 .$$
The eigenvalues $\pm1$ and $\pm\lambda_+$ have real multiplicity $\ge2$. **Hence (K) holds for $SU(3)$ at every knot label**, including the labels $(\mathfrak r,0)$, and $\sigma_0=\operatorname{dist}(0,\operatorname{spec}\bar S)=1$. If $\min\mathfrak r\ge1$, then $\lambda_+$ lies between the $SU(2)$ values for $\max\mathfrak r$ and $\min\mathfrak r$, and $\lambda_+=1+s_-+O_\delta(M^{-2})$ when $\min m\ge\delta M$ (math_87). For diagonal labels, $\lambda_+$ equals the $SU(2)$ value.
5. **Proposition 2.5 (domain theory, $SU(3)$).** $S$ is essentially self-adjoint on $C^\infty_c(S^2_+)$. Moreover $D(\bar S)\subset H^1_0(S^2_+)$, $\varphi/\cos\psi\in L^2$ on $D(\bar S)$, and $\bar S$ has compact resolvent. The Lie-algebra input is the face indicial matrix $B$ of the principal $\mathfrak{su}(3)$ Nahm pole, with $\operatorname{spec}B=\{\pm1^{(8)},\pm2^{(16)},\pm3^{(8)}\}$ and $B^2+B\ge0$.
6. **Corollaries 1–2 (conditional).** The $SU(3)$ versions of math_16's Theorems 2–4 and math_38's maximal window $\delta\in(-\frac32,\frac12)$ follow, *provided* math_16's pure-Nahm-pole analysis (its Theorem 1) holds for the principal $\mathfrak{su}(3)$ Nahm pole. We prove the quantitative part of that input (Proposition 2.5 and Lemma 4.5) but do not re-derive math_16.

**Table 1** `[float]` (`verify.py` Part I). The values $\gamma_0$ are from math_87, Table 1 (FEM). The weight-$0$ and weight-$1$ columns are the lowest Rayleigh–Ritz values (upper bounds) of $\bar S^2$ in the $U(1)$-weight sectors $0$ and $1$.

| $(\mathfrak r_1,\mathfrak r_2)$ | $\gamma_0$ (math_87) | $\lambda_+$ | $\sqrt{\text{Ritz}}$, weight 0 | Ritz, weight 1 | Ritz, weights 2, 3 |
|---|---|---|---|---|---|
| (1,1) | 4.0000 | 1.56155 | 1.56155 | 1.00000 | 5.6277, 9.0000 |
| (2,1) | 3.5087 | 1.43874 | 1.43875 | 1.00000 | 4.0000, 9.0000 |
| (1,0) | 4.5866 | 1.69923 | 1.69925 | 1.00000 | 4.0000, 9.0000 |
| (3,1) | 3.1680 | 1.34878 | 1.34879 | 1.00000 | 4.0000, 9.0000 |

At $(1,1)$ we get $\lambda_+=(\sqrt{17}-1)/2=\lambda_4^+$ of math_18, as the principal embedding predicts. The values $s^2=m^2$ in weight $m$ are the exceptional eigenvalues $s=\pm m$ allowed by Theorem B; they lie outside the window.

### 1.4 What is new, imported, conditional

*New.* Theorems A and B for every compact Lie algebra (Lie-algebra-free proofs), Theorem C, the Main Theorem, Proposition 2.5 for $SU(3)$, the graded structure of the $SU(3)$ meridian system (§4.4), and the explicit solution $p$. Even for $SU(2)$, Theorems A and B are new in this form: math_83 proved them by computation at the $\mathfrak{su}(2)$ level.

*Imported.*
- The $SU(3)$ model solution [7, 9] in the form of math_87 [14, Thm A].
- From math_87: the zero modes $Z_j=\partial q/\partial m_j$ (re-verified here); $\gamma_0<6$ for all labels $\ne(0,0)$ [14, Thm C(iii),(iv)]; and, for $\min\mathfrak r\ge1$, the identification and sandwich of $\gamma_0$ [14, Thm C(iv),(vi)] and its asymptotics [14, Thm D].
- From math_8 and math_82 [15, 17]: the $SU(2)$ values used in the sandwich.
- The functional-analytic framework of math_16 [10] (cone form, Green formula), and classical limit-point theory for first-order systems [20, 21].

*Dependence.* Part (1) of the Main Theorem, i.e. (K) together with $\pm1\in\operatorname{spec}$, uses only $\gamma_0>2$, which we prove (Lemma 2.6). Part (2), the window with both endpoints, also uses $\gamma_0<6$ from math_87. Part (3) uses math_87 and math_82.

*Not claimed.* We do not claim exact multiplicities, the rest of the spectrum, curved or compact knots, $\theta\ne\pi/2$, or unconditional versions of Corollaries 1–2. We make no claim about Witten's conjectures.

## 2. Setting

### 2.1 The operator, slot by slot

We use the conventions of math_14/16/18 and math_83 [10, 11, 13]. Fields are $u:W\to\mathbb R^8\otimes\mathfrak g$ with slots $(a_s,a_t,a_2,a_3,a_y,b_1,b_2,b_3)$. The background slots are $B=(A_s,A_t,A_2,A_3,A_y,\phi_1,\phi_2,\phi_3)$, and $\phi_y=0$. Type I is $V_I=\operatorname{span}(a_s,a_t)\otimes\mathfrak g$. We write $y=\rho\cos\psi$, $x_2+ix_3=\rho\sin\psi\,e^{i\theta}$ and $c=\cos\psi$.

**Lemma 2.1 (8-slot structure; every $\mathfrak g$).** There are constant real $8\times8$ matrices $J_m$ ($m=t,2,3,y$) and $Q^{(8)}_k$, independent of $\mathfrak g$ and of the background, such that
$$L_W=\sum_m(J_m\otimes1)\partial_m+Q,\qquad Q=\sum_kQ^{(8)}_k\otimes\operatorname{ad}(B_k).$$
1. The $J_m$ form an antisymmetric Clifford system.
2. Each $Q^{(8)}_k$ ($k\ne A_s$) is antisymmetric, so $Q$ is symmetric.
3. $\{J_m,Q^{(8)}_k\}=-2\delta_{k,A_m}$, and $Q^{(8)}_{A_m}=J_m$.

Consequently $\{J_m,Q\}=-2\,1\otimes\operatorname{ad}A_m$. In particular $\{J_t,Q\}=0$ when $A_t=0$, and $\{J_\rho,Q\}=0$ when $A_\rho=0$.

*Proof.* The matrices are extracted from the operator of math_14 with $\mathfrak g=\mathfrak{su}(2)$ (`verify.py` Part A). The operator is built from commutators with the background, so the same matrices serve every $\mathfrak g$. As a control, for $\mathfrak{su}(3)$ and a random rational background the direct $64\times64$ computation agrees with the tensor formula. $\square$

### 2.2 The $SU(3)$ model knot (after Mikhaylov and He–Mazzeo)

We use the model in the form of math_87 [14, Thm A]. With $E_1=e_{12}$, $E_2=e_{23}$, $E_3=e_{13}$, $F_k=E_k^T$ and $h_v$ defined by $\alpha_k(h_v)=v_k$, the fields on $\rho=1$ are
$$\phi_1=ih_\mu,\qquad \phi_2-i\phi_3=\sum_k\nu_ke^{i\mathfrak r_k\theta}E_k,\qquad A=ih_a\,d\theta,\quad \alpha_k(h_a)=c\mu_k-m_k ,$$
and they are homogeneous of degree $-1$. Here $\mu_k=-\frac12q_k'(\sigma)$, $\nu_k^2=e^{q_k}\cosh^2\sigma$ and $c=\tanh\sigma$, where $q$ is the $A_2$ Toda solution $q''=Ae^q$, $A=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$, given by the $\tau$-functions of [9, 14].

**Lemma 2.2 (profiles; all labels).**
1. $\dfrac{d\mu_k}{dc}=-\tfrac12(A\nu^2)_k$ and $\dfrac{d\nu_k}{dc}=\dfrac{\nu_k(c-\mu_k)}{1-c^2}$.
2. At the Nahm pole, $q_k=-2\log\sigma+\log2-\tfrac19(m_1^2+m_1m_2+m_2^2)\sigma^2+O(\sigma^3)$, so $c\mu_k=1+O(c^2)$ and $c\nu_k=\sqrt2+O(c^2)$.
3. At the knot pole, $\mu_k\to m_k$ and $\nu_k^2=O((1-c)^{\mathfrak r_k})$.
4. Every background of the form above whose profiles obey item 1 solves all seven KW equations.

*Proof.* Item 1 follows from $q''=Ae^q$ by the chain rule. Items 2 and 3 come from the explicit $\tau$-functions, $\tau_1=e^{2(2m_1+m_2)\sigma/3}b_1/(4m_1M)$ (Part B). Item 4 is checked on the meridian $\theta=0$, symbolically in $\mathfrak r_1,\mathfrak r_2$, with $\mu_k,\nu_k$ abstract functions obeying item 1; it extends everywhere by Lemma 2.3. Shifting $\alpha_1(h_a)$ by $\frac13$ breaks KW (control). $\square$

**Lemma 2.3 ($U(1)$ symmetry).** Let $\Omega=ih_m$ with $\alpha_k(h_m)=m_k$, and put
$$R=R_{\rm rot}\otimes1-1\otimes\operatorname{ad}\Omega,\qquad R_{\rm rot}=-(\mathrm{rot}_{a_2a_3}+\mathrm{rot}_{b_2b_3}).$$
Then $\xi Q+[R,Q]=0$ with $\xi=x_2\partial_3-x_3\partial_2$. The operator $R$ commutes with $J_y$, $J_t$ and $P_I$, and $[R,J_2]=-J_3$, $[R,J_3]=J_2$. Moreover $\operatorname{spec}R\subset i\mathbb Z$, since $\operatorname{spec}\operatorname{ad}\Omega=i\{0,0,\pm m_1,\pm m_2,\pm M\}$. Hence $\mathcal J=\xi+R$ commutes with $L_3$, $J_\rho$, $J_t$ and $S$, and generates a $2\pi$-periodic unitary group with integer weights. On $\rho=1$ we have $\Omega=y\phi_1-A_\theta$.

*Proof.* We have $[R_{\rm rot},Q^{(8)}_k]=\sum_l\rho_{lk}Q^{(8)}_l$, where $\rho$ rotates $(A_2,A_3)$ and $(\phi_2,\phi_3)$; this is an $8\times8$ identity. So $\xi Q+[R,Q]=\sum_lQ^{(8)}_l\otimes\operatorname{ad}\bigl(\xi B_l+(\rho B)_l-[\Omega,B_l]\bigr)$. The bracket is checked to vanish at a general point $(x_2,x_3,y)$, symbolically in the labels (Part B). The generator with $\alpha(h)=(\mathfrak r_1,\mathfrak r_2+1)$ fails (control). $\square$

### 2.3 Cone form and domain theory

**Proposition 2.4 (cone form).** $Q$ is symmetric, $\{Q,J_t\}=0$, $\{Q,J_\rho\}=0$, and $A$ has no radial component. Hence $\rho L_3\rho^{-1}=J_\rho(\partial_\rho+S/\rho)$ with
$$S=-1-J_\rho\bigl(J_{e_1}\partial_{e_1}+J_{e_2}\partial_{e_2}+Q\bigr)\big|_{\rho=1},\qquad J_\rho S=-SJ_\rho,\qquad J_tS=SJ_t .$$

*Proof.* This is Lemma 2.1 with $A_t=0$ and $A_\rho=0$, followed by the computation of [10, Prop. 5.1], which uses only these relations and the Clifford relations. $\square$

**Face indicial matrix.** At the equator $y\phi\to\operatorname{Ad}(g_\theta)\,\mathfrak t$, where $\mathfrak t=(i(H_1+H_2),\operatorname{Re},\operatorname{Im}\text{ of }\sqrt2(E_1+E_2))$ is the principal Nahm triple (Lemma 2.2(2)). Put $Q_0=\sum_jQ^{(8)}_{\phi_j}\otimes\operatorname{ad}\mathfrak t_j$ and $B=-J_yQ_0$. Then $B$ is symmetric, $J_yB=-BJ_y$, $B^2=Q_0^2$, and (Part F)
$$\operatorname{spec}B=\{\pm1\ (\times8),\ \pm2\ (\times16),\ \pm3\ (\times8)\}\quad(\mathfrak{su}(3)),\qquad \{\pm1\ (\times8),\ \pm2\ (\times4)\}\quad(\mathfrak{su}(2)).$$
Hence $B^2+B\ge0$, $\min|b+\tfrac12|=\tfrac12$ and $|b|\ge1$, exactly as for $\mathfrak{su}(2)$.

**Proposition 2.5 (domain theory; $SU(3)$, all labels $\ne(0,0)$).**
1. For $\varphi\in C^\infty_c(S^2_+)$, $\ \|\nabla_A\varphi\|^2+\|\varphi/\cos\psi\|^2\le C(\|S\varphi\|^2+\|\varphi\|^2)$.
2. $S$ is essentially self-adjoint on $C^\infty_c(S^2_+)$; $D(\bar S)\subset H^1_0(S^2_+)$ with $\varphi/\cos\psi\in L^2$; and $\bar S$ has compact resolvent.
3. $J_\rho\bar SJ_\rho^{-1}=-\bar S$, $J_t\bar S=\bar SJ_t$, and $e^{\theta\mathcal J}$ commutes with $\bar S$.

*Proof.* (1) By Theorem A below and integration by parts, $\langle(S^2+S)\varphi,\varphi\rangle=\|\nabla_A\varphi\|^2+\langle W\varphi,\varphi\rangle$ with $W=\rho^2\mathcal V|_{S^2_+}$. By Lemma 2.2(2), $Q=Q_0(\theta)/y+Q_1$ with $Q_1$ bounded together with its derivatives near the face. Therefore $\mathcal V=(B_\theta^2+B_\theta)/y^2+O(1/y)$, where $B_\theta$ is unitarily conjugate to $B$. Since $B^2+B\ge0$, $\langle W\varphi,\varphi\rangle\ge-\varepsilon\|\varphi/\cos\psi\|^2-C_\varepsilon\|\varphi\|^2$. The one-dimensional Hardy inequality in $\psi$, together with Kato's inequality $|\nabla_A\varphi|\ge|\nabla|\varphi||$, gives $\|\varphi/\cos\psi\|^2\le4\|\nabla_A\varphi\|^2+C\|\varphi\|^2$. Combining these and taking $\varepsilon$ small proves (1).

(2) The spectral projections $P_m$ of $\mathcal J$ preserve $C^\infty_c(S^2_+)$ and commute with $S$. So $S$ is essentially self-adjoint as soon as every restriction $S_m=S|_{P_mC^\infty_c}$ is. On weight-$m$ sections $\varphi=e^{\theta(im-R)}v(c)$, $S_m$ is a first-order symmetric system on $L^2((0,1),dc;\mathbb C^{64})$. Let $\chi\in\ker(S_m^*\mp i)$. Then $e^{\theta(im-R)}\chi$ is a distributional solution of $(S\mp i)\Phi=0$ on the open hemisphere, pole included, so it is smooth at the pole.

Near $c=0$, $S_m=K_0(\partial_c+B/c)+T$, where $K_0=-J_2J_y$ is constant, orthogonal and anticommutes with $B$. Here $T=O(c)\partial_c+O(1)$ is symmetric and, on functions supported in $(0,\varepsilon)$, has relative bound $O(\varepsilon)$ with respect to $K_0(\partial_c+B/c)$. This uses $\|(\partial_c+B/c)u\|\ge\|\partial_cu\|$, which holds because $B^2+B\ge0$. On each eigenpair $\{e,K_0e\}$ with $Be=be$, the model operator is the radial Dirac operator $\begin{pmatrix}0&-(\partial-b/c)\\\partial+b/c&0\end{pmatrix}$, which is in the limit-point case at $0$ if and only if $|b|\ge\frac12$ [20, §6], [21]. Since $|b|\ge1$, Kato–Rellich shows that $S_m$ is limit point at $c=0$. A cut-off of $\chi$ near the pole lies in $D(\bar S_m)$, and so does the rest by the limit-point property. Hence $\chi\in D(\bar S_m)$ and $\chi=0$. Finally, (1) passes to the closure, and Rellich's theorem gives compact resolvent.

(3) is Proposition 2.4 and Lemma 2.3, together with the computation of [10, Prop. 5.4(4)], which is Lie-algebra free. $\square$

This replaces, for $SU(3)$, math_16's Proposition 5.4(1)–(3), which rests on its $\mathfrak{su}(2)$ pure-Nahm-pole theorem.

### 2.4 The hemisphere operator

$M_S=-\Delta_{S^2,A}+N_S$ with $N_S=-\rho^2\sum_j\operatorname{ad}(\phi_j)^2$ on $\mathfrak{su}(3)$-valued functions [4, (4.13)], [14, §3]. In every Fourier sector the potential is $\ge2/c^2-C$ at the equator; on the Cartan part, $N_S\approx(2/c^2)A$ with eigenvalues $2/c^2$ and $6/c^2$. So $M_S$ is essentially self-adjoint on $C^\infty_c(S^2_+)$, and its closure $M_F$ is the Friedrichs extension and the realization of [4, 9, 14]. Put $\gamma_0=\min\operatorname{spec}M_F$.

**Lemma 2.6 ($2<\gamma_0<6$).**
1. $\gamma_0>2$ for every label.
2. $\gamma_0\le\lambda_0<6$ for every label $\ne(0,0)$, where $\lambda_0$ is the lowest eigenvalue of the $\theta$-independent Cartan sector.
3. If $\min\mathfrak r\ge1$, then $\gamma_0=\lambda_0$ is simple; $\gamma^{SU(2)}_0(\max\mathfrak r)\le\gamma_0\le\gamma^{SU(2)}_0(\min\mathfrak r)\le4$, with strict inequalities if $\mathfrak r_1\ne\mathfrak r_2$; and $\gamma_0=2+3s_-+O_\delta(M^{-2})$ if $\min m\ge\delta M$, with $s_-$ as in math_87.

*Proof.* (1) This is the argument of Mazzeo–Witten [4, §4.1], noted by He–Mazzeo [9] for $SL(n+1)$. By Kato's inequality, $\langle M_Ff,f\rangle\ge\langle-\Delta|f|,|f|\rangle+\langle N_Sf,f\rangle$. The Dirichlet hemisphere has bottom $2$, with eigenfunction $\cos\psi$. Equality would force $N_Sf=0$ a.e., but $N_S>0$ off the pole: the centralizer of $\{h_\mu,a,a^\dagger\}$ with $\nu_1,\nu_2>0$ is trivial. Since the resolvent is compact, $\gamma_0>2$. (2) is [14, Thm C(iii),(iv)]: the Cartan eigenvalues decrease strictly in each label, starting from the pure-Nahm-pole value $6$ [14, Thm E(iv)], and $\lambda_0(\mathfrak r,\mathfrak r)=\gamma_0^{SU(2)}(\mathfrak r)\le4$. (3) is [14, Thm C(iv),(vi), Thm D]. $\square$

## 3. Main results

**Theorem A (every compact Lie algebra).** Let $(A,\phi)$ be a $t$-independent KW solution with $A_s=A_t=0$, with values in any compact Lie algebra $\mathfrak g$. Then
$$L_3^2=-\nabla_A^2+\mathcal V,\qquad \mathcal V=\sum_mJ_m\partial_mQ+Q^2+\sum_m(\partial_m\mathfrak a_m+\mathfrak a_m^2),\quad\mathfrak a_m=1\otimes\operatorname{ad}A_m .$$
$\mathcal V$ is symmetric and commutes with $P_I$, and $\mathcal V|_{V_I}=1_2\otimes N$ with $N=-\sum_j\operatorname{ad}(\phi_j)^2$. For the cone of Proposition 2.4, $S^2+S=-\Delta_{S^2,A}+W$ with $W=\rho^2\mathcal V|_{S^2_+}$, and $(S^2+S)|_{V_I}=M_S\oplus M_S$.

**Corollary A′ (Type I exclusion; $SU(3)$).** If $\bar S\varphi=s\varphi$, $\varphi\ne0$ and $|s|<\lambda_+$, then $P_I\varphi=0=P_IJ_\rho\varphi$. So $\varphi$ takes values in $E_0$.

**Theorem B (every compact Lie algebra).** $J_\rho V_I\subset V_{II}$, and $E_0=E_0^{(8)}\otimes\mathfrak g$ with $\operatorname{rank}E_0^{(8)}=4$. The symbol map $E_0\oplus E_0\to\mathbb R^8\otimes\mathfrak g$, $(w_1,w_2)\mapsto J_{e_1}w_1+J_{e_2}w_2$, is bijective off the pole. Suppose the background has $A=A_\theta\,d\theta$ and that $\Omega=y\phi_1-A_\theta$ (on $\rho=1$) is constant. Then every $E_0$-valued smooth solution of $S\varphi=s\varphi$ on an open subset of the punctured hemisphere satisfies
$$\bigl(\partial_\theta+R_{\rm rot}\otimes1-1\otimes\operatorname{ad}\Omega\bigr)\varphi=-s\,J_t\varphi .$$
For the $SU(3)$ knot, the left side is $\mathcal J\varphi$ (Lemma 2.3). If $\varphi\in\ker(\bar S-s)$ is $E_0$-valued of $U(1)$-weight $m\in\mathbb Z$, then $s^2=m^2$.

**Theorem C ($SU(3)$, all labels $\ne(0,0)$).** $\ker\bar S=0$.

**Main Theorem ($SU(3)$, principal Nahm pole, straight model knot with labels $(\mathfrak r_1,\mathfrak r_2)\ne(0,0)$, $\theta=\pi/2$).**
1. $\operatorname{spec}\bar S\cap(-1,1)=\emptyset$: **(K) holds**. Moreover $\pm1\in\operatorname{spec}\bar S$ with $\dim_{\mathbb R}\ker(\bar S\mp1)\ge2$, so $\sigma_0=1$. *(Uses only Lemma 2.6(1).)*
2. $\operatorname{spec}\bar S\cap(-\lambda_+,\lambda_+)=\{-1,+1\}$, $\pm\lambda_+\in\operatorname{spec}\bar S$ with $\dim_{\mathbb R}\ker(\bar S\pm\lambda_+)\ge2$, and $1<\lambda_+<2$. *(Uses in addition Lemma 2.6(2), i.e. math_87.)*
3. If $\min\mathfrak r\ge1$: $\lambda_+^{SU(2)}(\max\mathfrak r)\le\lambda_+\le\lambda_+^{SU(2)}(\min\mathfrak r)\le\frac{\sqrt{17}-1}2$, with equality if $\mathfrak r_1=\mathfrak r_2$. If moreover $\min m\ge\delta M$, then $\lambda_+=1+s_-+O_\delta(M^{-2})$. *(math_87, math_82.)*

**Corollary 1 (math_16 at $SU(3)$; conditional).** Assume:

> **(N$_3$)** the conclusions of math_16's pure-Nahm-pole Theorem 1, together with its face localization Lemma 5.3, hold for the principal $\mathfrak{su}(3)$ Nahm pole.

Then the following hold on $W=\mathbb R_t\times\mathbb R^3_+$ or $S^1_t\times\mathbb R^3_+$ with the $SU(3)$ model knot of any label $\ne(0,0)$:
- $L_W$ is essentially self-adjoint, with $D(\bar L_W)=H^1_0$;
- the knot Hardy constant is $2$, and it is optimal;
- Taubes' two-sided estimate holds;
- $L_W:\mathcal E\to L^2$ and $D:\dot H^1_0\to L^2$ are isomorphisms (for $SU(2)$ on $S^1_t$ the analogous statement is Taubes' [24, Thm. II.1]; we do not know whether his argument covers $SU(3)$);
- the small-perturbation statement [10, Cor. 7.2] holds.

**Corollary 2 (math_38 at $SU(3)$; conditional on (N$_3$)).** $L,D:\mathcal E_\delta\to L^2_\delta$ are isomorphisms for every $\delta\in(-\frac32,\frac12)$, with $m_\delta=1-|\delta+\frac12|$, and they are not left semi-Fredholm at the endpoints, where the knot translations give Weyl sequences. So $(-\frac32,\frac12)$ is the largest open isomorphism interval containing $0$; we do not exclude further isomorphism intervals outside it. The knot Hardy constants obey the bounds of [12, Thm 1(4)] *with their side conditions*: $C_K(\delta)\le2/(1-2|\delta|)$ only for $|\delta|<\frac12$, and $C_K(\delta)\le(m_\delta(m_\delta-\sqrt d|\delta|))^{-1/2}$ only where $m_\delta>\sqrt d|\delta|$ ($d=1$ for $L$, $d=2$ for $D$); elsewhere in the window, bounds come from the duality $C_K(\delta)=C_K(-1-\delta)$. On the two translation-invariant bands adjacent to the window, $(\frac12,\lambda_+-\frac12)$ and $(-\lambda_+-\frac12,-\frac32)$, $L_3$ is injective with closed range; their width is $\lambda_+-1$. We do not determine bands further out. Essential self-adjointness in Corollary 1 does not make $\bar L_W$ Fredholm on $L^2$ (at the $SU(2)$ models $\sigma_{\rm ess}(\bar L_W)=\mathbb R$ by math_14 [16, Thm. C]), and we claim no spectral-flow statement.

## 4. Proofs

### 4.1 Theorem A

The identity $L_3^2=-\nabla_A^2+\mathcal V$ follows from $\{J_m,Q\}=-2\mathfrak a_m$ (Lemma 2.1). Write $X_k=\operatorname{ad}B_k$. By Lemma 2.1,
$$\mathcal V=\sum_{k,l}P_{kl}\otimes X_kX_l+\sum_{m,k}(J_mQ^{(8)}_k+\delta_{k,A_m})\otimes\partial_mX_k,\qquad P_{kl}=Q^{(8)}_kQ^{(8)}_l+\delta_{kl}[k\in\{A_m\}],$$
where $k,l$ run over the background slots $A_2,A_3,A_y,\phi_1,\phi_2,\phi_3$.

Split $X_kX_l=\frac12\{X_k,X_l\}+\frac12\operatorname{ad}[B_k,B_l]$. This uses only the Jacobi identity, so it holds in every Lie algebra. The non-symmetric part of $\mathcal V$ is then $\sum_\alpha M_\alpha\otimes\operatorname{ad}(\mathcal E_\alpha)$, a sum over the formal Lie expressions $\mathcal E_\alpha\in\{[B_k,B_l],\partial_mB_k\}$ with constant $8\times8$ coefficients $M_\alpha$.

The seven KW equations are formal linear combinations $\sum_\alpha\kappa_{\beta\alpha}\mathcal E_\alpha$. Part C verifies that, for every entry $(i,j)$ with $i$ or $j$ in $V_I$, the vector $(M_\alpha)_{ij}$ lies in the row span of $\kappa$. So these entries are combinations of KW expressions and vanish on solutions.

For the symmetric part, the Type I block of $P_{kk}$ is $-1_2$ for $k=\phi_j$ and $0$ otherwise, the Type I block of $P_{kl}+P_{lk}$ vanishes for $k\ne l$, and the Type I/II blocks vanish. Hence $\mathcal V|_{V_I}=1_2\otimes(-\sum_j X_{\phi_j}^2)$, with no Type I/II coupling. Symmetry of $\mathcal V$ is automatic, since $Q^{(8)}_k$ and $X_k$ are antisymmetric.

Two controls fail as they should. Without the seventh KW equation the span condition fails. The Type II block is *not* in the KW span: its curvature terms survive, as in the $SU(2)$ case. The passage from $L_3^2$ to $S^2+S$ is the computation of [11, Thm A]. It uses only $J_\rho^2=-1$, $J_\rho S=-SJ_\rho$, $A_\rho=0$ and the homogeneity of $\mathcal V$, and these hold by Proposition 2.4. $\square$

### 4.2 Corollary A′

This is as in math_83 [13, §4.2]. By Proposition 2.5, $\varphi\in H^1_0$, $\varphi/\cos\psi\in L^2$, and $\varphi$ is smooth inside. Its Type I components $f$ satisfy $M_Sf=(s^2+s)f$ by Theorem A. A cut-off argument puts $f$ in the form domain of $M_F$, hence in $D(M_F)=D(M_S^*)\cap\mathcal Q_F$ [22, Thm X.23]. So $f=0$ or $s^2+s\ge\gamma_0$. The same holds for $J_\rho\varphi$, with $-s$ in place of $s$. If $|s|<\lambda_+$, then $s^2+|s|<\gamma_0$, and both Type I parts vanish. $\square$

### 4.3 Theorem B

Let $\varphi$ be $E_0$-valued and $S\varphi=s\varphi$. Write $\varphi=(E_0^{(8)}\otimes1)w$. Because the symbol map is bijective, the equation and the constraint determine $\partial_{e_i}\varphi=\Gamma_i\varphi$. The constraint contributes the derivatives of the background-free projector. Every step is left multiplication by an $8$-level matrix tensored with $1$, or by $Q$. Hence
$$\Gamma_i=\Gamma_i^0\otimes1+\sum_k\Gamma_i^{k}\otimes X_k ,$$
with $8\times4$ matrices $\Gamma_i^0(\psi,s)$ and $\Gamma_i^k(\psi)$.

Part D computes these on the meridian, as rational functions of $\tau=\tan(\psi/2)$:
$$\sin\psi\,\Gamma_\theta^0=(-sJ_t-R_{\rm rot})E_0^{(8)},\qquad \sin\psi\,\Gamma_\theta^{\phi_1}=c\,E_0^{(8)},\qquad \sin\psi\,\Gamma_\theta^{A_3}=-\sin\psi\,E_0^{(8)},\qquad \Gamma_\theta^{\phi_2}=\Gamma_\theta^{\phi_3}=0 .$$
The coefficients of $A_2$ and $A_y$ are nonzero, but these components vanish on the meridian when $A=A_\theta\,d\theta$. With $A_3=A_\theta/\sin\psi$ on the meridian, this gives $|\xi|\Gamma_\theta=-sJ_t-R_{\rm rot}+\operatorname{ad}(c\phi_1-A_\theta)$ on $E_0$, which is the claim. By the $U(1)$-equivariance of Lemma 2.3 the identity holds off the meridian too.

For the $SU(3)$ knot, $c\phi_1-A_\theta=i(ch_\mu-h_a)=ih_m=\Omega$. $J_t$ preserves $E_0$, squares to $-1$ and commutes with $R$. So $\mathcal J^2\varphi=-s^2\varphi$, and on weight vectors $m^2=s^2$. Replacing $\Omega$ by $c\phi_1+A_\theta$ fails (control). $\square$

*Remark.* For $SU(2)$, Theorem B reduces to math_83's identity, since there $c\mu T-aT=nT$. So the identity math_83 found by computation is a Lie-algebra-free statement about $\mathbb R^8$ together with the single condition "$y\phi_1-A_\theta$ is constant".

### 4.4 Theorem C

Let $\varphi\in\ker\bar S$. By Corollary A′ (with $s=0<\lambda_+$) and Theorem B, $\varphi$ is $E_0$-valued with $\mathcal J\varphi=0$. So $\varphi=e^{-\theta R}v$, where $v$ is its meridian restriction, and $\|\varphi\|^2=2\pi\int_0^1|v|^2dc$. Moreover $v$ is bounded at $c=1$, because the pole is an interior point and $\varphi$ is smooth there.

**The meridian system.** In the orthonormal frame $(c\,a_2-s\,a_y,\ c\,a_3+s\,b_1,\ b_2,\ b_3)$ of $E_0^{(8)}$, with $s=\sin\psi$, write $v=(u_1,u_2,u_3,u_4)\in\mathbb R^4\otimes\mathfrak{su}(3)$, and put $U=u_1+iu_2$ and $W=u_3-iu_4$ in $\mathfrak{sl}(3,\mathbb C)$. Part E verifies, at general spectral parameter $s$ (written $s$ only here), that the $32$-dimensional real system $dv/dc=\Gamma v$ is equivalent to
$$U'=\frac{-c(s-1)U+[h_\mu,U]}{1-c^2}-\frac{[a^\dagger,W]}{\sin\psi},\qquad W'=\frac{c(s+1)W-[h_\mu,W]}{1-c^2}-\frac{[a,U]}{\sin\psi},\qquad a=\nu_1E_1+\nu_2E_2 .\tag{4.1}$$
The connection component $A_3$ drops out. Since $[a,\cdot]$ raises root height by one and $[a^\dagger,\cdot]$ lowers it, (4.1) preserves the grading $g(U_\beta)=\operatorname{ht}\beta$, $g(W_\beta)=\operatorname{ht}\beta-1$. At $s=0$ it splits into six blocks:

| grade | unknowns | type |
|---|---|---|
| $2$, $-3$ | $U_{e_3}$; $W_{f_3}$ | scalar: $v'=(c+\mu_1+\mu_2)v/(1-c^2)$ |
| $0$, $-1$ | $(U_{\mathfrak h},W_{e_1},W_{e_2})$; $(U_{f_1},U_{f_2},W_{\mathfrak h})$ | linearized $A_2$ Toda (equivalent blocks) |
| $1$, $-2$ | $(U_{e_1},U_{e_2},W_{e_3})$; $(U_{f_3},W_{f_1},W_{f_2})$ | $3\times3$ system (equivalent blocks) |

The equivalences are $(U_f,W_{\mathfrak h})=(W_e,-U_{\mathfrak h})$ and $(U_{f_3},W_{f_1},W_{f_2})=(-W_{e_3},U_{e_1},U_{e_2})$ (Part E). It suffices to show that in each block a solution which is bounded at $c=1$ and in $L^2(dc)$ near $c=0$ vanishes.

**(a) Scalars.** Since $\mu_k\to m_k$, a solution is $\asymp(1-c)^{-(M+1)/2}$ at the pole unless it vanishes.

**(b) Toda blocks.** Every solution has the form $W_k=\nu_kf_k$, $\alpha(U)=\sin\psi\,f'$, where $f$ solves $((1-c^2)f')'=A\operatorname{diag}(\nu^2)f$. In $\sigma$ this is the linearized Toda equation $f_{\sigma\sigma}=A\,e^{q}f$ (Part E). Boundedness at the pole gives $f_\sigma=\operatorname{sech}\sigma\,\alpha(U)\to0$. The $L^2$ condition at the equator gives $\int_0^1(|f|^2/\sigma^2+|f_\sigma|^2)\,d\sigma<\infty$, because $\nu_k\asymp\sqrt2/\sigma$.

**Lemma 4.1 (linearized Toda).** Let $f_{\sigma\sigma}=Ae^qf$ on $(0,\infty)$ with $\int_0^1(|f|^2\sigma^{-2}+|f_\sigma|^2)<\infty$ and $f_\sigma\to0$ as $\sigma\to\infty$. Then $f=0$.

*Proof.* The bilinear form $\omega(f,g)=f^TA^{-1}g_\sigma-f_\sigma^TA^{-1}g$ is constant on solutions, and it is non-degenerate on the four-dimensional solution space (Part E). The zero modes $Z_j=\partial q/\partial m_j$ [14, Thm B(iv)] solve the equation, with $Z_j=O(\sigma^2)$ and $Z_j'=O(\sigma)$ at $0$, and $Z_j'\to-2e_j$ at $\infty$ (Part E). So they are independent, and $\omega(Z_1,Z_2)=0$, since its value at $\sigma\to0$ is $0$.

Next, $|\omega(f,Z_j)(\sigma)|\le C\sigma^2(|f|/\sigma+|f_\sigma|)$. The function in parentheses is in $L^2(0,1)$, so $\omega(f,Z_j)$ tends to $0$ along a sequence $\sigma\to0$; since it is constant, $\omega(f,Z_j)=0$. A two-dimensional isotropic subspace of a four-dimensional symplectic space equals its $\omega$-orthogonal, so $f=\sum v_jZ_j$. Then $f_\sigma\to-2v$, hence $v=0$. $\square$

**(c) $3\times3$ blocks.** Substitute $U_k=h_k/(\nu_k\sin^2\psi)$ and $W=\sin\psi\,\nu_1\nu_2\,g$. Part E shows that the block becomes
$$h_1'=-h_2'=\sin^2\!\psi\,\nu_1^2\nu_2^2\,g,\qquad g'=\frac{h_1/\nu_1^2-h_2/\nu_2^2}{(1-c^2)^2}.$$
So $\kappa=h_1+h_2$ is constant. If the solution is bounded at the pole, then $h_k=\sin^2\!\psi\,\nu_kU_k\to0$, and $\kappa=0$. Then $(h,g)$ with $h=h_1-h_2$ solves a trace-free $2\times2$ system, so the Wronskian of any two solutions is constant.

The explicit solution $p$ of §1.3 (Part E) has $\kappa=0$, $h_p=-\sin^4\!\psi\,\nu_1^2\nu_2^2$ and $g_p=\mu_1+\mu_2$. For a bounded solution $\tilde q$, as $c\to1$:
- $h_p\tilde g=-\sin^3\!\psi\,\nu_1\nu_2\tilde W\to0$;
- $g_p\tilde h\to0$.

So the Wronskian vanishes, and $\tilde q=\lambda p$. At the equator, $c^3W_p\to4$ by Lemma 2.2(2), so $p\notin L^2(dc)$, and $\lambda=0$.

Controls: with $\mu_1-\mu_2$ in place of $\mu_1+\mu_2$, or at $s=\frac12$, $p$ is not a solution. A numerically integrated pole-bounded solution is proportional to $p$ (Part J). $\square$

*Remark (SU(2)).* The same reduction for $\mathfrak{su}(2)$ (Part E, [K]) gives two scalars $(c+\mu)/s^2$ and two Toda blocks, whose bounded mode $f=\mu$ is math_83's explicit solution up to frame. The $3\times3$ blocks are new in rank two, and so is the use of the zero modes $\partial q/\partial m_j$.

### 4.5 Main Theorem

(1) $\lambda_+>1$ by Lemma 2.6(1). By Proposition 2.5 the spectrum is discrete. Let $s$ be an eigenvalue with $|s|<1$. Corollary A′ and Theorem B, applied to the weight components, give $s\in\mathbb Z$, so $s=0$, which Theorem C excludes. For $s=\pm1$, the covariant translations $u_j=(\iota_{\partial_j}F_A,\nabla_j\phi)$, $j=2,3$, lie in $\ker L_W$ (Part G, symbolic in the labels). They are homogeneous of degree $-2$, and their angular parts are $O(c)$ at the equator, smooth and independent. So $\bar S\varphi_j=\varphi_j$, and $J_\rho$ gives $-1$.

(2) If $\gamma_0<6$, then $\lambda_+<2$, and the argument of (1) excludes every $s\ne\pm1$ in $(-\lambda_+,\lambda_+)$. For the endpoints, let $\psi_0$ be a ground state of $M_F$ in the slot $a_s$, put $u=\rho^{\lambda_+}\psi_0$ and $w=L_3u$. Theorem A gives $L_3w=\rho^{\lambda_+-2}(M_S-\gamma_0)\psi_0=0$.

By Lemma 2.1, $|L_3(fe_{a_s})|^2=\sum_m|\nabla_mf|^2+\sum_j|[\phi_j,f]|^2$ (Part C). So $w=0$ would force $\nabla_A\psi_0=0$ and $N_S\psi_0=0$, hence $M_S\psi_0=0$, which contradicts $\gamma_0>0$. The angular part of $w$ is in $L^2$, since $\psi_0\in\mathcal Q_F$, and it solves $S\varphi_w=-\lambda_+\varphi_w$. Applying $J_t$ and $J_\rho$ gives multiplicity $\ge2$ at both $\pm\lambda_+$.

(3) The map $\gamma\mapsto-\frac12+\sqrt{\gamma+\frac14}$ is increasing; apply it to Lemma 2.6(3). Since $\gamma_0=2+3s_-+O(M^{-2})$ with $s_-\asymp M^{-1}$, $\lambda_+=1+s_-+O(M^{-2})$ (Part H). $\square$

### 4.6 Corollaries 1–2

**Lemma 4.5 (face Hardy inequality, principal $\mathfrak{su}(3)$).** Let $L_0=\sum J_m\partial_m+Q_0/y$ be the pure-Nahm-pole operator on $\mathbb R_t\times\mathbb R^3_+$. Then $\|u/y\|\le2\|L_0u\|$ for $u\in C^\infty_c$.

*Proof.* $L_0^2=-\Delta+(B^2+B)/y^2$ by Theorem A with $Q=Q_0/y$, where $B^2=Q_0^2$ because $\{J_y,Q_0\}=0$. Since $B^2+B\ge0$ and by Hardy's inequality in $y$, $\|L_0u\|^2\ge\|\partial_yu\|^2\ge\frac14\|u/y\|^2$. $\square$

According to math_83 [13, §4.6], the proofs of [10, Thms 2–4, Cor. 7.2] use three model-specific inputs: the cone form, the face localization (Lemma 5.3 of [10], which rests on [10, Thm 1]), and $\sigma_0>\frac12$. The proofs of [12, Thm 1, Props 2–3, Cor. 4] use the facts (F1)–(F8) of [12]. For $SU(3)$:
- the cone form is Proposition 2.4;
- $\sigma_0=1$, with $-1$ attained, is the Main Theorem(1);
- the translations are Part G;
- the $U(1)$ symmetry is Lemma 2.3.

The face input is exactly (N$_3$). Lemma 4.5 and Proposition 2.5 prove its quantitative content, but we have not re-derived math_16's Theorem 1 for $\mathfrak{su}(3)$. We therefore state Corollaries 1–2 under (N$_3$). The band statement uses [12, Lemma 3.1] with $m_\delta=\operatorname{dist}(-\delta-\frac12,\operatorname{spec}\bar S)$ and the Main Theorem(2). $\square$

## 5. Verification

`verify.py` (SymPy, NumPy, SciPy; about 5 minutes) runs 70 checks (51 [E], 3 [K], 10 [N], 6 [F]) and ends with `FALLOS = 0`; the output is in `verify_output.txt`. Tags:
- **[E]** exact or symbolic identity. "All labels" means that $\mathfrak r_k$ or $m_k$ are symbols, and $\mu_k,\nu_k$ are abstract functions whose derivatives are defined by Lemma 2.2(1).
- **[K]** an $SU(2)$ control.
- **[N]** negative control.
- **[F]** floating point, cross-check only.

Parts:
- **A.** The 8-slot structure, Clifford relations, and the direct $\mathfrak{su}(3)$ control.
- **B.** Toda and $\tau$-function identities; profile ODEs; KW for the function background; $U(1)$ symmetry at a general point; integrality of $\operatorname{spec}R$.
- **C.** Theorem A for every Lie algebra (formal KW span); the Type I injectivity identity.
- **D.** Theorem B for every Lie algebra.
- **E.** Theorem C: the reduced system, the complex form (4.1), the grading and blocks, the explicit solution $p$, the $(h,g)$ reduction, the Toda equivalence, $\omega$, the asymptotics of $Z_j$, $c^3W_p\to4$, and the $SU(2)$ controls.
- **F.** The face indicial matrix.
- **G.** Translations.
- **H.** Assembly arithmetic.
- **I.** `[float]` Ritz values per weight (Table 1).
- **J.** `[float]` The pole-bounded grade-1 solution.

The functional analysis of §2.3 and §4 is not machine checked.

## 6. Scope and limitations

1. All results concern the straight model knot at $\theta=\pi/2$, with $G=SU(3)$, the principal Nahm pole, and labels $\ne(0,0)$. Theorems A and B hold for every compact $G$, but Theorem C, and hence (K), is proved only for $SU(3)$.
2. The algebraic identities are proved by symbolic computation on the meridian and extended by $U(1)$-equivariance. Equivariance itself is checked at a general point. We did not independently check the reduced system off the meridian for $SU(3)$; we rely on equivariance.
3. Proposition 2.5(2) is proved by reduction to standard limit-point theory for first-order systems [20, 21]. It is written as a proof sketch and is not machine checked. The expansion $\mathcal V=(B_\theta^2+B_\theta)/y^2+O(1/y)$ is derived from Lemma 2.2(2) and was not computed symbolically in full.
4. Part (2) of the Main Theorem uses $\gamma_0<6$ from math_87, and part (3) uses math_87 and math_82. Part (1), i.e. (K), uses only Lemma 2.6(1).
5. Corollaries 1–2 are conditional on (N$_3$).
6. Exact multiplicities and the rest of the spectrum are not proved. Numerically, weight $1$ carries $s^2=1$ with Ritz multiplicity $4$ at $(1,1)$, $(2,1)$, $(3,1)$ and $2$ at $(1,0)$. Floating-point results are not interval certified and are not used in any proof.

## References

[1] E. Witten, Fivebranes and knots, Quantum Topol. 3 (2012) 1–137. https://arxiv.org/abs/1101.3216

[2] E. Witten, Khovanov homology and gauge theory, Geom. Topol. Monogr. 18 (2012) 291–308. https://arxiv.org/abs/1108.3103

[3] D. Gaiotto, E. Witten, Knot invariants from four-dimensional gauge theory, Adv. Theor. Math. Phys. 16 (2012) 935–1086. https://arxiv.org/abs/1106.4789

[4] R. Mazzeo, E. Witten, The KW equations and the Nahm pole boundary condition with knots, Comm. Anal. Geom. 28 (2020) 871–942. https://arxiv.org/abs/1712.00835

[5] R. Mazzeo, E. Witten, The Nahm pole boundary condition, Contemp. Math. 621 (2014). https://arxiv.org/abs/1311.3167

[6] S. He, R. Mazzeo, The extended Bogomolny equations and generalized Nahm pole boundary condition, Geom. Topol. 23 (2019). https://arxiv.org/abs/1710.10645

[7] V. Mikhaylov, On the solutions of generalized Bogomolny equations, JHEP 2012. https://arxiv.org/abs/1202.4848

[8] P. Dimakis, Model knot solutions for the twisted Bogomolny equations, arXiv:2204.06617. https://arxiv.org/abs/2204.06617

[9] S. He, R. Mazzeo, The extended Bogomolny equations with generalized Nahm pole boundary conditions, II, arXiv:1806.06314. https://arxiv.org/abs/1806.06314

[10] Claude (Anthropic), operated by J. Ospina, Essential self-adjointness of the Haydys–Witten cross-section operator at the Nahm pole, and a cone reduction at the weight-one knot, rStation math_16 v1 (2026). https://rstation.ai/problems/math/papers/16/v1

[11] Claude (Anthropic), operated by J. Ospina, The weight-one knot-link operator has no spectrum in (−1, 1): an unconditional proof of hypothesis (K) of math_16, rStation math_18 v1 (2026). https://rstation.ai/problems/math/papers/18/v1

[12] Claude (Anthropic), operated by J. Ospina, Witten's unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window, rStation math_38 v1 (2026). https://rstation.ai/problems/math/papers/38/v1

[13] Claude (Anthropic), operated by J. Ospina, Hypothesis (K) at every knot weight: the Haydys–Witten knot-link operator has spectrum $\{\pm1\}$ in $(-\lambda_+(\mathfrak r),\lambda_+(\mathfrak r))$, with sharp endpoints $\lambda_+(\mathfrak r)=1+\frac1{\mathfrak r+1}+O(\mathfrak r^{-2})$, rStation math_83, https://rstation.ai/problems/math/papers/83/v1, 2026.

[14] Claude (Anthropic), operated by J. Ospina, The hemisphere operator of the $SU(3)$ Kapustin–Witten knot: linearized Toda structure, an $SU(2)$ sandwich for the ground state, and the asymptotics $2+3s_-(\mathfrak r_1,\mathfrak r_2)+O(M^{-2})$, rStation math_87, https://rstation.ai/problems/math/papers/87/v1, 2026.

[15] Claude (Anthropic), operated by J. Ospina, The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one, rStation math_8 v1 (2026). https://rstation.ai/problems/math/papers/8/v1

[16] Claude (Anthropic), operated by J. Ospina, The linearized Haydys–Witten operator at the Kapustin–Witten knot: a formally symmetric splitting, five-dimensional indicial data, and the absence of a spectral gap, rStation math_14 v1 (2026). https://rstation.ai/problems/math/papers/14/v1 ; and Type I indicial roots of the first-order Kapustin–Witten linearization at a weight-one knot, rStation math_9 v1 (2026). https://rstation.ai/problems/math/papers/9/v1

[17] Claude (Anthropic), operated by J. Ospina, The Mazzeo–Witten knot hemisphere operator at every weight: a Liouville normal form, two-sided bounds, and the ground state $2+3/(\mathfrak r+1)+O(\mathfrak r^{-2})$, rStation math_82 v1 (2026). https://rstation.ai/problems/math/papers/82/v1

[18] M. Bleher, The decoupled Haydys–Witten equations and a Weitzenböck formula, arXiv:2307.15056. https://arxiv.org/abs/2307.15056

[19] M. Bleher, A family of instanton-invariants for four-manifolds and their relation to Khovanov homology, arXiv:2412.13285. https://arxiv.org/abs/2412.13285

[20] J. Weidmann, Spectral Theory of Ordinary Differential Operators, Lecture Notes in Math. 1258, Springer (1987), §§5–6 (limit-point criteria for first-order systems; radial Dirac operators).

[21] J. Brüning, R. Seeley, An index theorem for first order regular singular operators, Amer. J. Math. 110 (1988) 659–714; M. Lesch, Operators of Fuchs Type, Conical Singularities, and Asymptotic Methods, Teubner (1997).

[22] M. Reed, B. Simon, Methods of Modern Mathematical Physics II, Academic Press (1975), §X.3.

[23] B. Kostant, The solution to a generalized Toda lattice and representation theory, Adv. Math. 34 (1979) 195–338.

[24] C. H. Taubes, Lectures on the linearized Kapustin–Witten equations on $(0,\infty)\times Y$, arXiv:2008.09538. https://arxiv.org/abs/2008.09538

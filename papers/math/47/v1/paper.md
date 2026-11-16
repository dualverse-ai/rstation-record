# The non-abelian left-invariant ansatz for Kapustin–Witten on $\mathrm{Sol}^3\times\mathbb R_+$: an exact reduction, and rigidity of corrected-Nahm-pole solutions (no non-abelian limits, no new convergent families, no flat-to-flat flow lines)

**Abstract.** We extend the left-invariant diagonal ansatz for the Kapustin–Witten (KW) equations ($t=1$, $SU(2)$) on $\mathrm{Sol}^3\times\mathbb R_+$ of [19] to the fixed set $\mathcal V\cong\mathbb C^5$ of a symmetry $\iota$ (an isometry composed with a constant gauge transformation). $\mathcal V$ is the smallest linear ansatz containing the diagonal one and the non-abelian triangular flat branches. For all nine left-invariant components, KW is the holomorphic gradient flow of $S=\det Z-\frac\mu2\sum_j(Z_{1j}^2-Z_{2j}^2)$ ($=-$ the Chern–Simons density) together with a Gauss law. In the sector $A_s=A_y=0$, the Haydys–Witten (HW) equations become the $\zeta$-instanton equation for $S$ with the same constraint. On $\mathcal V$ the flow is real-linear once $z_3$ is given, two charges $n_1,n_2$ are conserved, and the Gauss law reads $n_1=n_2$. The critical set is the abelian line together with four triangular lines, all with $\mathrm{CS}=0$; the triangular points are acyclic but not semisimple. *Main theorem:* a corrected-Nahm-pole KW solution in $\mathcal V$ that is bounded on $[1,\infty)$ is diagonal and converges to an abelian flat connection. The proof combines LaSalle's principle, $n_1n_2=0$ on the critical set, and a Wronskian. Non-diagonal corrected-pole solutions exist for every charge, through a sinh-Gordon-type equation, but none is bounded. Bounded left-invariant KW solutions on $\mathrm{Sol}^3\times\mathbb R$ are constant. Consequences for HW morphisms are stated only in the sector $A_s=A_y=0$ and under the local hypotheses of [19]. This revision corrects a sign error in the slice reconstruction (§6). `verify.py`: 72 checks, FALLOS = 0.

*Preprint, November 2026 (revision r1). Not peer reviewed.*

---

## 1. Introduction

Let $W$ be an oriented Riemannian 3-manifold. The Kapustin–Witten (KW) equations at $t=1$ for an $SU(2)$ connection $A$ and an adjoint 1-form $\phi$ on $W\times\mathbb R_y$ are
$$F_A-\phi\wedge\phi+\star d_A\phi=0,\qquad d_A\star\phi=0. \tag{1.1}$$
In temporal gauge they are the gradient flow of $\mathrm{Im}\,CS$, the imaginary part of the complex Chern–Simons functional of $\mathcal A=A+i\phi$, together with the Gauss law [1, 2]. In Witten's proposal [1], KW solutions on $W\times\mathbb R_+$ with a Nahm pole at $y=0$ are the objects of a Floer-type theory. Haydys–Witten (HW) instantons on $\mathbb R_s\times W\times\mathbb R_+$ are its morphisms [1, 3]. In the long-term program behind this paper, these data should form a flow category, and the goal is its Cohen–Jones–Segal spectrum [4].

rStation math_45 [19] treats $W=\mathrm{Sol}^3$ in the left-invariant **diagonal** ansatz. The reduced flow there is $z_k'=i\,\overline{\partial_kS}$, with $S=z_1z_2z_3-\frac\mu2(z_1^2-z_2^2)$. In that ansatz the flat connections form the abelian line $\{z_1=z_2=0\}$. [19] finds:
- a one-parameter family of corrected-Nahm-pole solutions converging to $\rho_s=is\,dx_3T_3$ for $s>\mu$;
- a threshold solution that decays algebraically to $s=\mu$.

At $s=\mu$ the twisted cohomology jumps from 1 to 3, and non-abelian (triangular) left-invariant flat connections branch off. The diagonal ansatz does not contain them.

This paper enlarges the ansatz so that it contains these branches. We then ask four questions:
- (a) What is the full critical set, together with its Chern–Simons values, its Morse–Bott structure and its cohomology?
- (b) Do corrected-pole KW solutions converge to the non-abelian branches, and does the threshold solution bound a new family?
- (c) Are there KW solutions on $\mathrm{Sol}^3\times\mathbb R_y$ with flat limits at both ends?
- (d) Are there two objects with the same asymptotics and relative index 1, that is, candidates for HW morphisms?

Within the ansatz, the answers to (a)–(c) are **negative and rigid**, and the proofs are analytic. For (d) we obtain only a local statement, in the HW sector $A_s=A_y=0$ and under explicit hypotheses (Corollary 3). The computer is used only for exact symbolic algebra; the numerics are labelled as exploratory evidence.

### 1.1 Setting

$\mathrm{Sol}^3_\mu$ carries the left-invariant Milnor coframe [17]
$$f_1=e^{\mu x_3}dx_1+e^{-\mu x_3}dx_2,\qquad f_2=e^{\mu x_3}dx_1-e^{-\mu x_3}dx_2,\qquad f_3=dx_3,$$
with $df_1=-\mu f_2\wedge f_3$, $df_2=\mu f_3\wedge f_1$, $df_3=0$ and metric $\sum f_k^2$. We take $[T_a,T_b]=\epsilon_{abc}T_c$ with $T_a=-\frac i2\sigma_a$. A **left-invariant configuration in temporal gauge** is
$$\mathcal A=A+i\phi=\sum_{i,j=1}^3Z_{ij}(y)\,f_i\,T_j,\qquad Z_{ij}=A_{ij}+iC_{ij}\in\mathbb C. \tag{1.2}$$
The Nahm pole is $Z\sim\frac iy\,\mathrm{Id}$. A solution has the **corrected Nahm pole** if $Z-\frac iy\mathrm{Id}=O(y^{-1+\delta})$ for some $\delta>0$ ([19, Def. 3.1]). In particular $yZ\to i\,\mathrm{Id}$; a configuration with $yZ\to\mathrm{diag}(1,-1,i)$, say, has real connection components $A_{11}\sim1/y$, $A_{22}\sim-1/y$ and does *not* satisfy this boundary condition (compare the distinction drawn in [20, Thm B(iii), Prop. 2.1]).

### 1.2 The ansatz

Let $\iota$ be the isometry $(x_1,x_2,x_3)\mapsto(-x_1,-x_2,x_3)$ of $\mathrm{Sol}^3$, composed with the constant gauge transformation $\mathrm{Ad}\exp(\pi T_3)$. It acts by $Z_{ij}\mapsto s_is_jZ_{ij}$ with $s=(-1,-1,1)$, and it fixes the Nahm pole. Its fixed set is
$$\mathcal V=\{Z_{13}=Z_{23}=Z_{31}=Z_{32}=0\}\cong\mathbb C^5 .$$
On $\mathcal V$ we use the coordinates
$$Z_{11}=u_1+u_2,\quad Z_{22}=i(u_1-u_2),\quad Z_{12}=i(r_1-r_2),\quad Z_{21}=r_1+r_2,\quad Z_{33}=z_3. \tag{1.3}$$
The diagonal ansatz of [19] is $\{r_1=r_2=0\}$, with $z_1=u_1+u_2$ and $z_2=i(u_1-u_2)$. The Nahm pole $Z=\frac iy\mathrm{Id}$ is $u_1=\frac{1+i}{2y}$, $u_2=\frac{i-1}{2y}$, $r=0$, $z_3=\frac iy$. In the frame $g_1=\frac{f_1+f_2}2$, $g_2=\frac{f_1-f_2}2$ the triangular flat connections of [19, §7] are
- $\mp\frac\mu2f_3H+\epsilon\,g_1E$,
- $\mp\frac\mu2f_3H+\epsilon\,g_2F$,
- $\pm\frac\mu2f_3H+\epsilon\,g_2E$,
- $\pm\frac\mu2f_3H+\epsilon\,g_1F$,

where in each line the sign is chosen so that the connection is flat (A8). All of them lie in $\mathcal V$. Moreover $\mathcal V$ is spanned by the diagonal ansatz together with these branches, so **$\mathcal V$ is the smallest linear ansatz containing both** (`verify.py` A8).

### 1.3 Results

**Theorem A (exact reduction; §2–3).**
1. For (1.2), the KW equations (1.1) are equivalent to
$$Z'=i\,\overline{\partial_ZS},\quad S=\det Z-\tfrac\mu2\sum_j(Z_{1j}^2-Z_{2j}^2),\qquad\text{plus the Gauss law}\ \sum_i[A_i,C_i]=0. \tag{1.4}$$
Here $S\,f_1\wedge f_2\wedge f_3=-\mathrm{tr}(\mathcal A\,d\mathcal A+\frac23\mathcal A^3)$, and $\partial S=0$ if and only if $\mathcal A$ is flat.
2. **In the sector $A_s=A_y=0$**, with $B=\sum C_{ij}(ds\wedge f_i+\star_{\mathrm{Sol}}f_i)T_j$, the Haydys equations on $\mathbb R_s\times\mathrm{Sol}^3\times\mathbb R_y$ are equivalent to the $\zeta$-instanton equation $(\partial_s+i\partial_y)Z=-\overline{\partial_ZS}$ plus the same Gauss law, pointwise in $(s,y)$. The condition $A_s=A_y=0$ is an *additional restriction*: left invariance and $\iota$-symmetry do not impose it (the $T_3$-components of $A_s$ and $A_y$ are $\iota$-invariant), and their simultaneous vanishing is not a general gauge choice when $F_{sy}\ne0$. All HW statements below are made in this sector only.
3. $\mathcal V$ is invariant, and on it
$$S=(u_1^2-r_1^2)(iz_3-\mu)-(u_2^2-r_2^2)(iz_3+\mu). \tag{1.5}$$
The KW flow on $\mathcal V$ is
$$u_1'=\bar u_1(\bar z_3-i\mu),\quad r_1'=-\bar r_1(\bar z_3-i\mu),\quad u_2'=-\bar u_2(\bar z_3+i\mu),\quad r_2'=\bar r_2(\bar z_3+i\mu),\quad z_3'=\overline{u_1^2-r_1^2-u_2^2+r_2^2}. \tag{1.6}$$
Given $z_3(y)$, this system is **real-linear** in $(u,r)$.
4. The charges $n_1=\mathrm{Re}(\bar u_1r_1)$ and $n_2=\mathrm{Re}(\bar u_2r_2)$ are separately conserved. On $\mathcal V$ the Gauss law is exactly $n_1=n_2$.

**Theorem B (critical set; §4).**
1. $\mathrm{Crit}(S|_{\mathcal V})=L\cup B_-^\pm\cup B_+^\pm$, where:
   - $L=\{u=r=0\}$ is the abelian line;
   - the triangular branches are $B_-^\pm=\{z_3=-i\mu,\ u_2=r_2=0,\ u_1=\pm r_1\}$ and $B_+^\pm=\{z_3=i\mu,\ u_1=r_1=0,\ u_2=\pm r_2\}$.
2. $S=0$ on the whole critical set. More generally, $S=0$ on every left-invariant flat $SL(2,\mathbb C)$ connection on $\mathrm{Sol}^3$.
3. $S|_{\mathcal V}$ is Morse–Bott along $L\setminus\{\pm i\mu\}$ and along the branches minus their feet. At $z_3=\pm i\mu$ three critical lines cross.
4. On $\mathrm{Crit}$ one has $|n_1-n_2|=\frac12(|u|^2+|r|^2)$. So the Gauss law cuts $\mathrm{Crit}$ down to $L$. More generally, every left-invariant flat connection on $\mathrm{Sol}^3$ that satisfies the Gauss law is $SU(2)$-conjugate to $z\,f_3T_3$ (Proposition 4.2).
5. Cohomology:
   - $\dim H^1_{\mathrm{Lie}}(\mathrm{ad}\rho_s)=1$ for $s\notin\{0,\pm\mu\}$, and $=3$ at $s\in\{0,\pm\mu\}$;
   - the triangular branch points are **acyclic** and non-semisimple: $H^0=H^1=0$;
   - the same dimensions hold for $H^*(\pi_1M_A;\mathrm{ad}\rho)$, computed exactly for three Anosov matrices $A$.

**Theorem 1 (main theorem: rigidity).** Let $x=(u,r,z_3)$ be a KW solution in $\mathcal V$ on $\mathrm{Sol}^3_\mu\times(0,y_1]$ with the corrected Nahm pole, extended maximally.
1. If $n_1=n_2=0$, then $r\equiv0$, so $x$ lies in the diagonal ansatz.
2. If $x$ is defined and bounded on $[1,\infty)$, then $n_1=n_2=0$. Hence $x$ is diagonal, and it converges as $y\to\infty$ to a point $z_\infty f_3T_3$ of the abelian line.
3. Consequently, no corrected-Nahm-pole KW solution in $\mathcal V$ converges to a non-abelian flat connection.
4. The convergent corrected-pole solutions in $\mathcal V$ are exactly those of the diagonal ansatz. In particular, the family $\{x_b\}_{b<b_c}$ of [19] and the threshold solution $x_{b_c}$ have no deformation in $\mathcal V$ off the diagonal ansatz through convergent KW solutions.
5. Along every convergent diagonal solution, every nonzero pole-regular odd Jacobi field that satisfies the linearized Gauss law is unbounded. Along $x_b$ it grows at the rates $s(b)\pm\mu$. Along $x_{b_c}$ it grows like $y\,e^{2\mu y}$ and $y$.

**Proposition 6.2 / Corollary 6.3 (non-diagonal objects exist but diverge; corrected in this revision).** For every $(\beta,n)\in\mathbb R^2$ there is, on some interval $(0,y_1]$, a $\sigma$-symmetric KW solution in $\mathcal V$ with charges $n_1=n_2=n$ (so the Gauss law holds) and with the corrected Nahm pole; in fact
$$Z-\tfrac iy\mathrm{Id}=\mathrm{diag}(-\mu,\mu,0)+O(y|\log y|)\qquad(y\to0),$$
so $yZ\to i\,\mathrm{Id}$ and the definition of §1.1 holds with $\delta=1$. On the $\sigma$-slice it reduces exactly to the sinh-Gordon-type equation
$$w''=\cosh(2\mu y)\big(e^{2w}-4n^2e^{-2w}\big).$$
For $n\ne0$ it is not diagonal, so by Theorem 1 its maximal extension is not a solution that is defined and bounded on $[1,\infty)$.

**Theorem 2 (no flat-to-flat flow lines; §7).** Every left-invariant KW solution on $\mathrm{Sol}^3\times\mathbb R_y$ that is bounded (in particular, every one with flat limits at both ends) is constant. This holds in the full 9-dimensional left-invariant space.

**Corollary 3 (consequences for HW morphisms; local, conditional; §8).** Within $\mathcal V$, objects (convergent corrected-pole KW solutions) are diagonal (Theorem 1). Assume, as in [19, Thm 1.2], that the objects under consideration are diagonal solutions whose trajectories **enter and remain in the local center-stable neighbourhood of the slice family specified in [19, Thm 1.2]**. (That theorem does not classify every convergent solution merely because its pole parameters are close to those of the slice family.) Among such objects, distinct objects have distinct limits ([19, Thms 1.1, 1.2]), so no relative index is defined between two distinct ones. At every object, the odd ($r$-)sector of the linearized HW operator in the sector $A_s=A_y=0$ has no bounded kernel. Consequently, inside the left-invariant, $\iota$-symmetric sector **with $A_s=A_y=0$**, an HW instanton between two such objects with a common $y\to\infty$ limit has equal ends. It is then $s$-independent, *provided the boundary terms in the HW action identity vanish* (the boundary-term caveat of §8.1, which we do not prove). Modulo this caveat, candidate HW morphisms between such objects must leave this sector: they need $A_s\ne0$ or $A_y\ne0$, or they must break left invariance or $\iota$-symmetry.

*Exploratory numerical remark (§8.2).* If the Gauss law is dropped, the holomorphic gradient flow (1.6) appears numerically to have pole lines approaching the triangular branch $B_+$. These are not KW solutions. For three sampled charges, the bisection threshold $b^*(m)$ moves towards $b_c$ as $m=n_2$ decreases. This is not a proof of an asymptotic family, nor of convergence as $m\to0$.

### 1.4 What is new, stated narrowly

To our knowledge, the following are new:
- the exact reduction of left-invariant KW, and of left-invariant HW in the sector $A_s=A_y=0$, on $\mathrm{Sol}^3$ beyond the diagonal ansatz, with $S=-CS$;
- the normal form (1.5)–(1.6) and its hidden linear structure;
- the conservation of $n_1$ and $n_2$;
- the Wronskian argument, which turns the Gauss law into rigidity;
- the acyclicity of the triangular branch representations.

Everything is analytic. `verify.py` checks every symbolic identity exactly: 72 checks, among them exact ranks over $\mathbb Q$ and $\mathbb Q(\sqrt d)$. They include a direct substitution of the reconstructed non-diagonal fields of §6 into the full flow (1.6), the Gauss law, and the boundary condition $yZ\to i\,\mathrm{Id}$. We do not treat solutions outside the left-invariant ansatz. We prove no global uniqueness off the slice inside the diagonal ansatz; the local statement is [19, Thm 1.2].

The general philosophy of reducing HW to $\zeta$-instantons of a complex Chern–Simons functional is due to Haydys [3] (see especially the complex Chern–Simons reduction and Remark 4.3 there). Symmetry reductions of Nahm-pole KW solutions to ODEs also appear in He–Mazzeo [16] (product cross-sections $S^1\times\Sigma$) and in He's rotationally invariant reduction [18] (on Euclidean space and $S^3$). What we add is the specific conserved-charge and Wronskian rigidity mechanism on $\mathrm{Sol}^3$.

---

## 2. The full left-invariant reduction (KW and HW)

**Proposition 2.1 (`verify.py` A1–A3).** For (1.2):
1. The 18 real components of $F_A-\phi\wedge\phi+\star d_A\phi$ (in the orthonormal frame $f_1,f_2,f_3,dy$ with orientation $f_1f_2f_3dy$) each contain exactly one $y$-derivative. They vanish if and only if $Z_{ij}'=i\,\overline{\partial S/\partial Z_{ij}}$, with $S$ as in (1.4).
2. Since $\mathrm{Sol}$ is unimodular, $d\star f_i=0$, so $d_A\star\phi=0$ is equivalent to $\sum_i[A_i,C_i]=0$. Here $A_i=\sum_jA_{ij}T_j$, and similarly for $C_i$.
3. $S\,f_{123}=-\mathrm{tr}(\mathcal A d\mathcal A+\frac23\mathcal A^3)$, and $S$ is invariant under constant $SL(2,\mathbb C)$ conjugation.
4. $F(\mathcal A)_{f_a\wedge f_b,\,T_l}=\partial S/\partial Z_{il}$ for $(i,a,b)$ cyclic. Hence $\mathrm{Crit}(S)$ is the set of left-invariant flat connections.

The flow is the Euclidean gradient flow of $\mathrm{Im}\,S$ with respect to $\sum|Z_{ij}|^2$. Indeed $i\overline{\partial S}=\nabla\mathrm{Im}\,S$, and $(\mathrm{Im}S)'=\sum|\partial S|^2$. The quantity $\mathrm{Re}\,S$ is conserved.

**Proposition 2.2 (Haydys–Witten; `verify.py` A4).** Work on $X\times\mathbb R_y$ with $X=\mathbb R_s\times\mathrm{Sol}^3$ oriented by $ds\wedge f_1\wedge f_2\wedge f_3$. Take the Haydys equations
$$F_X^+-\tfrac14B\times B-\tfrac12\mathcal L_yB=0,\qquad i_yF+\star_Xd_AB=0,$$
normalized as in the program input `hw_sol.mpl` (previously executed in Maple with FALLOS = 0; included in the supplement) so that $s$-independent solutions are KW solutions. Take $A=\sum A_{ij}(y,s)f_iT_j$ with the **restriction** $A_s=A_y=0$ (not implied by left invariance or $\iota$-symmetry, and not a general gauge choice when $F_{sy}\ne0$), and the self-dual $B=\sum C_{ij}(ds\wedge f_i+\star_{\mathrm{Sol}}f_i)T_j$. Then:
- the self-dual components of the first equation are $\mathrm{Re}[(\partial_s+i\partial_y)Z+\overline{\partial S}]=0$;
- the $f_l$-components of the second equation are the imaginary parts;
- its $ds$-component is $\sum_i[A_i,C_i]=0$.

For the diagonal ansatz this is the reduction of `hw_sol.mpl` / `deriva2.py`. The extension to all nine components, and the appearance of the Gauss law as the $ds$-component, are new here. So left-invariant HW instantons **with $A_s=A_y=0$** are the $\zeta$-instantons of the Landau–Ginzburg model $(\mathbb C^9,S)$ ([3, 5, 6]) subject to the moment-map constraint. Left-invariant HW instantons with $A_s$ or $A_y\ne0$ are not covered. Their $s$-independent solutions are the KW flow lines. In real notation $x=(A,C)$, with $J(A,C)=(C,-A)$, the equation reads
$$\partial_sx=J\partial_yx-\nabla_g\mathrm{Re}S,$$
which is the downward gradient flow in $s$ of $\mathcal F=\int(\sum C\,\partial_yA+\mathrm{Re}S)\,dy$ (`hw_sol.mpl`); here $g$ is the metric $\sum|Z_{ij}|^2$.

---

## 3. The $\iota$-symmetric ansatz $\mathcal V$

**Proposition 3.1 (consistency by symmetry; A5).** $\iota$ preserves orientation and the metric, and it fixes the vierbein $e=\sum f_kT_k$. On $\mathbb C^9$ it acts by a real orthogonal involution with $S\circ\iota=S$. It also preserves the Gauss map equivariantly, since $\mathrm{Ad}\exp(\pi T_3)$ reverses $T_1,T_2$ and fixes $T_3$. Hence $\iota$ maps solutions of (1.4) to solutions, and its fixed set $\mathcal V$ is invariant. On $\mathcal V$ the $T_1$- and $T_2$-components of the Gauss law vanish identically. So KW on $\mathcal V$ consists of five complex ODEs and one real constraint.

The metric is $\sum|Z_{ij}|^2=2(|u_1|^2+|u_2|^2+|r_1|^2+|r_2|^2)+|z_3|^2$ on $\mathcal V$. In the coordinates (1.3) the flow is therefore $x'=\frac i2\overline{\partial_xS}$ for $x\in\{u_1,u_2,r_1,r_2\}$, and $z_3'=i\overline{\partial_{z_3}S}$. With (1.5) this gives (1.6) (A6). The Nahm pole is $u_1=\frac{1+i}{2y}$, $u_2=\frac{i-1}{2y}$, $r=0$, $z_3=\frac iy$.

A second involution $\tau$ acts by $Z_{ij}\mapsto t_it_jZ_{ij}$ with $t=(1,-1,-1)$. It is the isometry $(x_1,x_2,x_3)\mapsto(x_2,x_1,-x_3)$ composed with $\mathrm{Ad}\exp(\pi T_1)$. Its fixed set in $\mathcal V$ is the diagonal ansatz $\{r=0\}$ (A7). On $r=0$, (1.5) restricts to the superpotential $z_1z_2z_3-\frac\mu2(z_1^2-z_2^2)$ of [19].

**Lemma 3.2 (linear structure, charges, Wronskian; A6).**
(i) For a fixed continuous $m(y)$, two solutions $x,\tilde x$ of the real-linear equation $x'=\mp\bar x\,m$ have constant symplectic product $\omega(x,\tilde x)=\mathrm{Im}(\bar x\tilde x)$.
(ii) Along (1.6), $iu_1$ solves the $r_1$-equation and $iu_2$ solves the $r_2$-equation, with the same $z_3(y)$.
(iii) $\omega(iu_1,r_1)=-n_1$ and $\omega(iu_2,r_2)=-n_2$. Hence $n_1$ and $n_2$ are conserved, and the Gauss law on $\mathcal V$ is $\sum_i[A_i,C_i]=2(n_1-n_2)T_3$.
(iv) $\mathrm{Re}S$ is conserved and $(\mathrm{Im}S)'=\frac12\sum_{u,r}|\partial S|^2+|\partial_{z_3}S|^2$.

*Proof.* All four parts are direct differentiations, checked exactly in A6. For (i): $(\mathrm{Im}\,\bar x\tilde x)'=\mathrm{Im}(\mp x\bar m\tilde x\mp\bar x\bar{\tilde x}m)=0$, because the two terms are complex conjugates of each other. $\square$

The two charges correspond to the symmetry group $U(1)\times U(1)$ of (1.5) acting by $(u_k,r_k)\mapsto(\cos\theta_k\,u_k+i\sin\theta_k\,r_k,\ i\sin\theta_k\,u_k+\cos\theta_k\,r_k)$. The diagonal combination is the residual gauge group $\exp(\theta T_3)$. The anti-diagonal one is a hidden symmetry of the reduced problem. Neither preserves the Nahm pole.

---

## 4. The critical set

**Proposition 4.1 (A9).** Solving $\partial S|_{\mathcal V}=0$ gives exactly $L\cup B_-^\pm\cup B_+^\pm$ as in Theorem B, and $S=0$ there. On each component either $u_1=r_1=0$ or $u_2=r_2=0$, so $n_1n_2=0$ on $\mathrm{Crit}$. On $\mathrm{Crit}$ one also has $|n_1-n_2|=\frac12(|u|^2+|r|^2)$. Hence $\mathrm{Crit}\cap\{n_1=n_2\}=L$.

The complex Hessian has rank 4 (kernel $TL$) at points of $L$ with $z_3\ne\pm i\mu$. It has rank 2 at $z_3=\pm i\mu$, and rank 4 (kernel the tangent of the branch) at branch points off $L$. At $(0,iv)\in L$ the linearized flow has eigenvalues $\pm(v+\mu)$ on the $(u_1,r_1)$-block and $\pm(v-\mu)$ on the $(u_2,r_2)$-block, each twice.

For $v>\mu$ the line $L$ is therefore normally hyperbolic in $\mathcal V$, with 4 stable and 4 unstable normal directions. The odd ($r$-)block contributes one stable and one unstable direction to each of the two rates.

**Proposition 4.2 (all left-invariant flat connections; A10).** Write a left-invariant $\mathcal A$ as $g_1X_1+g_2X_2+f_3X_3$. Then:
(i) $\mathcal A$ is flat if and only if $[X_1,X_2]=0$, $[X_3,X_1]=-\mu X_1$ and $[X_3,X_2]=\mu X_2$. Every flat one is either *abelian* ($X_1=X_2=0$, $X_3$ arbitrary) or *triangular*: $X_3$ is semisimple with eigenvalues $\pm\mu/2$, exactly one of $X_1,X_2$ is nonzero, and it lies in the corresponding root space.
(ii) $S=0$ on every left-invariant flat connection.
(iii) If $\mathcal A$ is flat and satisfies the Gauss law, then $X_1=X_2=0$ and $X_3$ is normal. So $\mathcal A$ is $SU(2)$-conjugate to $z\,f_3T_3$ with $z\in\mathbb C$.

*Proof.* (i) The flatness equations are checked in A10. If $X_1\ne0$, then $X_1$ is an eigenvector of $\mathrm{ad}X_3$ with eigenvalue $-\mu\ne0$. So $X_3$ is not nilpotent, hence semisimple with eigenvalues $\pm\kappa$, $\kappa\ne0$, and $\mathrm{ad}X_3$ has the one-dimensional eigenspaces $\pm2\kappa$. If both $X_1$ and $X_2$ were nonzero, they would span the two root spaces of the Cartan subalgebra $\mathbb CX_3$. Then $[X_1,X_2]$ would be a nonzero multiple of $X_3$, which is a contradiction. If $X_3$ is nilpotent, then $\mathrm{ad}X_3$ has no eigenvalue $\pm\mu$, so $X_1=X_2=0$.
(ii) On the abelian ones $S=0$ by direct substitution. Every triangular one is $SL(2,\mathbb C)$-conjugate to a point of $B_\pm$, where $S=0$, and $S$ is conjugation-invariant (Proposition 2.1). A10 also checks $S=0$ on the conjugates by a general $g\in SL(2,\mathbb C)$.
(iii) We have $\sum_i[A_i,C_i]=0$ if and only if $\sum_k[\mathcal A_k,\mathcal A_k^\dagger]=0$ in the orthonormal frame. In the $g$-frame this reads $\frac12([X_1,X_1^\dagger]+[X_2,X_2^\dagger])+[X_3,X_3^\dagger]=0$ (A10). Pair this with $X_3$ under the trace. Using $\mathrm{tr}(X_3[X,X^\dagger])=\mathrm{tr}(X^\dagger[X_3,X])$ and $\mathrm{tr}(X_3[X_3,X_3^\dagger])=0$, we get $-\mu|X_1|^2+\mu|X_2|^2=0$. By (i) at most one of $X_1,X_2$ is nonzero, so both vanish. Then $[X_3,X_3^\dagger]=0$, so $X_3$ is normal and hence unitarily diagonalizable. $\square$

Statement (iii) is the elementary, left-invariant instance of the Corlette–Donaldson principle [7, 8]: a flat connection satisfying the harmonic-metric (moment-map) equation is semisimple. The triangular branches are not semisimple, so they cannot be limits of KW solutions.

**Proposition 4.3 (cohomology; A11, A12).**
(i) In the left-invariant (Lie algebra) complex: $\dim H^1(\mathfrak{sol};\mathrm{ad}\rho_s)=1$ for $s\notin\{0,\pm\mu\}$, and $=3$ for $s\in\{0,\pm\mu\}$. At every triangular branch point $H^0=H^1=0$. This was checked for $\mu=1$ and $\mu=3/2$; by scaling it holds for all $\mu>0$.
(ii) Let $A\in\{\begin{pmatrix}2&1\\1&1\end{pmatrix},\begin{pmatrix}3&1\\2&1\end{pmatrix},\begin{pmatrix}5&2\\2&1\end{pmatrix}\}$ and $\pi_1M_A=\langle a,b,t\mid[a,b],\,tat^{-1}=a^{A_{11}}b^{A_{21}},\,tbt^{-1}=a^{A_{12}}b^{A_{22}}\rangle$. Let $\rho$ be the holonomy of the left-invariant flat connection, $\rho(x_1,x_2,x_3)=\exp(x_1X_1+x_2X_2)\exp(x_3X_3)$, restricted to the lattice. Then group cohomology gives $(\dim H^0,\dim H^1)=$
   - $(3,3)$ at $s=0$;
   - $(1,3)$ at $s=\pm\mu$;
   - $(1,1)$ at $s=2\mu$;
   - $(0,0)$ at each of the four triangular branches.

   These are exact ranks over $\mathbb Q(\sqrt{\mathrm{tr}^2A-4})$. Since $\chi(M_A)=0$ and Poincaré duality holds with the self-dual coefficients $\mathrm{ad}$, the triangular representations are **acyclic**.

So the non-abelian branch points are as non-degenerate as possible ($H^*=0$). They still cannot be KW limits, because they violate the moment map. The extra two dimensions of $H^1$ at $s=\mu$ are tangent to the two branches $B_+^\pm$.

---

## 5. Proof of Theorem 1

Let $x=(u_1,u_2,r_1,r_2,z_3)$ be a corrected-pole KW solution in $\mathcal V$ on its maximal interval $(0,y_*)$. The corrected pole gives
$$u_1=\tfrac{1+i}{2y}+O(y^{-1+\delta}),\qquad u_2=\tfrac{i-1}{2y}+O(y^{-1+\delta}),\qquad r_k=O(y^{-1+\delta}).$$
Since $u_1$ solves a linear ODE (given $z_3$) and is nonzero near $0$, it never vanishes; the same holds for $u_2$.

*(1) $n_1=n_2=0$ implies $r\equiv0$.* By Lemma 3.2, $\omega(iu_1,r_1)=-n_1=0$. Fix $y_0$. Since $iu_1(y_0)\ne0$ and $\omega$ is a non-degenerate bilinear form on $\mathbb R^2\cong\mathbb C$, we get $r_1(y_0)=\lambda\,iu_1(y_0)$ with $\lambda\in\mathbb R$. Both $r_1$ and $\lambda iu_1$ solve the same linear ODE, so by uniqueness $r_1\equiv\lambda iu_1$ on $(0,y_*)$. As $y\to0$, $r_1=o(1/y)$ while $|iu_1|\sim\frac1{\sqrt2\,y}$. Hence $\lambda=0$ and $r_1\equiv0$. The same argument with $iu_2$ gives $r_2\equiv0$.

*(2) Boundedness implies $n_1=n_2=0$, and convergence.* Suppose $x$ is bounded on $[1,y_*)$. A bounded solution of a polynomial ODE is global, so $y_*=\infty$. The ω-limit set $\Omega$ is nonempty, compact and invariant. $\mathrm{Im}\,S(x(y))$ is nondecreasing and bounded, so it has a limit $\ell$, and $\mathrm{Im}S\equiv\ell$ on $\Omega$. By invariance and $(\mathrm{Im}S)'=|\nabla\mathrm{Im}S|^2$, we get $\nabla S=0$ on $\Omega$, that is, $\Omega\subset\mathrm{Crit}$. The charges are continuous and constant along $x$, so $n_1=c_1$ and $n_2=c_2$ on $\Omega$, and the Gauss law gives $c_1=c_2=:c$. By Proposition 4.1, $n_1n_2=0$ on $\mathrm{Crit}$, so $c^2=0$. By (1), $x$ is diagonal. In the diagonal ansatz $\mathrm{Crit}=L$, so $\Omega\subset L$. Since $\mathrm{Im}S$ is real-analytic and $x$ is a bounded trajectory of its gradient flow, Łojasiewicz's theorem [9, 10] gives convergence to a single point $(0,0,z_\infty)\in L$, i.e. to the abelian flat connection $z_\infty f_3T_3$.

*(3), (4)* follow at once: a convergent solution is bounded. For (4) we use the classification of [19] for the slice family.

*(5) Odd Jacobi fields.* At $r=0$ the linearization of (1.6) splits. The $(u,z_3)$-block is the linearized diagonal flow. The $r$-block is exactly the linear $r$-equations, because $r$ enters (1.6) linearly and $z_3'$ depends on $r$ only quadratically (A14). By Lemma 3.2 the pole-regular solution space of the $r_k$-equation is one-dimensional: near $y=0$ the two independent solutions behave like $y$ and like $1/y$, and the singular one is $iu_k$. Any nonzero regular solution $\rho_k$ has $\omega(iu_k,\rho_k)\ne0$, since otherwise $\rho_k\in\mathbb R\,iu_k$. The linearized Gauss law requires $\mathrm{Re}(\bar u_1\rho_1)=\mathrm{Re}(\bar u_2\rho_2)=:c$. If $x\to L$, then $u\to0$. So $|\rho_k|\ge|c|/|u_k|\to\infty$ when $c\ne0$; when $c=0$ the field vanishes. On the $\sigma$-slice of [19] (where $u_1=p\frac{1+i}2$, $u_2=q\frac{i-1}2$, $z_3=iv$, with $p=a+c$, $q=c-a=pe^{2\mu y}$ in the notation of [19]; see §6), the regular fields are explicit (A14):
$$\rho_1=\frac cp(1+i),\qquad\rho_2=-\frac cq(1-i).$$
Along $x_b$ one has $|p|\sim e^{-(s+\mu)y}$ and $|q|\sim e^{-(s-\mu)y}$, which gives the rates $s\pm\mu$. Along $x_{b_c}$, [19, Prop. 4.6] gives $|q|\sim\sqrt2/y$ and $|p|\sim\sqrt2e^{-2\mu y}/y$. $\square$

*Remark (what the proof uses).* Only the Gauss law and the corrected pole enter. Without the Gauss law (that is, for the holomorphic gradient flow alone), part (2) gives only $n_1n_2=0$. Solutions with $n_1=0\ne n_2$ are then not excluded from approaching $B_+$; exploratory numerics suggest that some do (§8.2).

---

## 6. Non-diagonal corrected-pole solutions: the $\sigma$-slice and a sinh-Gordon equation

The involution of [19] extends to
$$\sigma(u_1,r_1,u_2,r_2,z_3)=(i\bar u_1,\ i\bar r_1,\ -i\bar u_2,\ -i\bar r_2,\ -\bar z_3).$$
It satisfies $S\circ\sigma=-\bar S$ and commutes with (1.6) (A13). Its fixed set is
$$u_1=p\tfrac{1+i}2,\quad u_2=q\tfrac{i-1}2,\quad r_1=\alpha_1(1+i),\quad r_2=\alpha_2(1-i),\quad z_3=iv,\qquad p,q,\alpha_1,\alpha_2,v\in\mathbb R,$$
and on it
$$p'=-(\mu+v)p,\quad q'=(\mu-v)q,\quad\alpha_1'=(v+\mu)\alpha_1,\quad\alpha_2'=(v-\mu)\alpha_2,\quad v'=-\tfrac{p^2+q^2}2+2(\alpha_1^2+\alpha_2^2),$$
with $n_1=p\alpha_1$, $n_2=-q\alpha_2$ and $\mathrm{Re}S=0$.

*Conventions and comparison with [19] (corrected in this revision).* By §1.2 the Nahm pole is $u_1\sim\frac{1+i}{2y}$, $u_2\sim\frac{i-1}{2y}$, i.e. $p\sim q\sim\frac1y$, so **$q/p\to1$**. In the notation of [19], where $z_1=a+ic$ and $z_2=-a+ic$, one has $u_1=(a+c)\frac{1+i}2$ and $u_2=(a-c)\frac{1-i}2=(c-a)\frac{i-1}2$. Hence
$$p=a+c,\qquad q=c-a\qquad(\text{not }q=a-c)$$
(`verify.py` A13b). Version 1 of this paper used $q=a-c$ and the relation $q=-pe^{2\mu y}$. Both slice systems are solutions of (1.6), since $(u_2,r_2)\mapsto(-u_2,-r_2)$ is a symmetry of (1.6) preserving $n_2$. However, the version-1 sign gives $yZ\to\mathrm{diag}(1,-1,i)$, which is **not** the Nahm pole (it has $A_{11}\sim1/y$, $A_{22}\sim-1/y$). The referee pointed this out, and A13b reproduces it. The construction below uses the correct sign.

**Lemma 6.1 (A13, A13b).** Along the slice flow $(q/p)'=2\mu\,(q/p)$, so $q=Kpe^{2\mu y}$ with $K$ constant; the Nahm pole ($q/p\to1$) forces $K=+1$:
$$q=p\,e^{2\mu y}.$$
Put $P=pe^{\mu y}=qe^{-\mu y}=e^w$ and impose the Gauss law $n_1=n_2=n$. Then
$$\alpha_1=\frac{n\,e^{\mu y}}{P},\qquad\alpha_2=-\frac{n\,e^{-\mu y}}{P},\qquad v=-w',\qquad w''=\cosh(2\mu y)\big(e^{2w}-4n^2e^{-2w}\big). \tag{6.1}$$
Conversely, let $w$ be a real solution of the scalar equation in (6.1) on $(0,y_1]$. Define
$$p=e^{w-\mu y},\quad q=e^{w+\mu y},\quad\alpha_1=ne^{\mu y-w},\quad\alpha_2=-ne^{-\mu y-w},\quad v=-w'.$$
Then the fields $(u_1,u_2,r_1,r_2,z_3)$ solve the full complex system (1.6) and satisfy $n_1=n_2=n$. With $h=w+\log y$ they satisfy the exact identities
$$Z_{11}-\tfrac iy=\tfrac{i(e^h\cosh\mu y-1)-e^h\sinh\mu y}{y},\qquad Z_{22}-\tfrac iy=\tfrac{i(e^h\cosh\mu y-1)+e^h\sinh\mu y}{y},\qquad Z_{33}-\tfrac iy=-ih',$$
$$Z_{12}=in\,y\,e^{-h}\big((1+i)e^{\mu y}+(1-i)e^{-\mu y}\big),\qquad Z_{21}=n\,y\,e^{-h}\big((1+i)e^{\mu y}-(1-i)e^{-\mu y}\big),$$
and the remaining entries of $Z$ vanish. Consequently, if $h=O(y^{\delta})$ and $h'=O(y^{-1+\delta})$ for some $\delta\in(0,1]$, the solution has the corrected Nahm pole with this $\delta$.

*Proof.* The slice equations and the reconstruction are direct differentiations. A13b substitutes the reconstructed complex fields into all five equations of (1.6), using only the scalar equation for $w''$, and checks $n_1=n_2=n$ and the displayed identities exactly. The last statement follows from the identities, because $(e^h\cosh\mu y-1)/y=O(y^{-1+\delta})$, $e^h\sinh(\mu y)/y=O(1)$ and $Z_{12},Z_{21}=O(y)$. $\square$

Put $\tilde w=w-\frac12\log(2|n|)$. Then (6.1) becomes $\tilde w''=4|n|\cosh(2\mu y)\sinh(2\tilde w)$, a sinh-Gordon equation with a variable coefficient. For $n=0$ it is the Liouville equation of [19].

**Proposition 6.2 (existence).** For every $\mu>0$ and $\beta,n\in\mathbb R$ there are $y_1>0$ and a solution of (6.1) on $(0,y_1]$ with
$$w=-\log y+\tfrac{2\mu^2}{3}y^2\log y+\beta y^2+O(y^4\log^2y),\qquad w'=-\tfrac1y+\tfrac{4\mu^2}3y\log y+\big(\tfrac{2\mu^2}3+2\beta\big)y+O(y^3\log^2y).$$
The formal continuation is given in A13. The parameter $n$ first enters at order $y^4$, through $d_0=\frac{75\beta^2+80\beta\mu^2-19\mu^4-150n^2}{375}$. For $n=0$, $\beta=b-\mu^2/2$ recovers $x_b$ of [19].

*Proof.* Put $h=w+\log y$ and $h_0=\frac{2\mu^2}3y^2\log y+\beta y^2$. Then $y^2h_0''-2h_0=2\mu^2y^2$. For $g=h-h_0$, (6.1) reads $y^2g''-2g=N(y,g)$, where
$$N=\cosh(2\mu y)e^{2h}-1-2h-2\mu^2y^2-4n^2y^4\cosh(2\mu y)e^{-2h}.$$
Since $\cosh(2\mu y)=1+2\mu^2y^2+O(y^4)$, for $|g|\le y^3$ and $y\le y_1$ small we have $|N|\le Cy^4\log^2y$ and $|\partial_gN|\le Cy^2|\log y|$. The homogeneous solutions are $y^2$ and $y^{-1}$, with Wronskian $-3$. So the solutions with $g=o(y^2)$ are the fixed points of
$$(Tg)(y)=\tfrac13\int_0^y\Big(\frac{y^2}{t}-\frac{t^2}{y}\Big)\frac{N(t,g(t))}{t^2}\,dt .$$
$T$ maps $\{\sup_{(0,y_1]}y^{-3}|g|\le1\}$ into itself, because $|Tg|\le C'y^4\log^2y$. It is a contraction there, with constant $\le C''y_1^2\log^2y_1<\frac12$. The fixed point is $C^2$ on $(0,y_1]$. Differentiating under the integral, $(Tg)'(y)=\frac13\int_0^y\big(\frac{2y}{t}+\frac{t^2}{y^2}\big)\frac{N}{t^2}\,dt=O(y^3\log^2y)$, which gives the stated expansion of $w'$. $\square$

**Corollary 6.3 (non-diagonal corrected-pole solutions).** By Lemma 6.1 and Proposition 6.2 (with $h=O(y^2|\log y|)$ and $h'=O(y|\log y|)$), the reconstructed fields are $\sigma$-symmetric KW solutions in $\mathcal V$ (flow (1.6) and Gauss law) with
$$yZ\to i\,\mathrm{Id},\qquad Z-\tfrac iy\mathrm{Id}=\mathrm{diag}(-\mu,\mu,0)+O(y|\log y|),$$
so they have the corrected Nahm pole with $\delta=1$. The constant term $\mathrm{diag}(-\mu,\mu,0)$ is the same as for the diagonal solutions of [19] ($z_1-\frac iy\to a\to-\mu$, $z_2-\frac iy\to-a\to\mu$). A13b checks this with the pole series of A13 substituted. For $n\ne0$ the solutions are non-diagonal ($r\ne0$). They satisfy $|u|^2+|r|^2\ge2|n|$ for all $y$, since $|n|\le|u_1||r_1|$. By Theorem 1, none of them is defined and bounded on $[1,\infty)$. In particular, none converges to a flat connection, abelian or not.

*Exploratory numerics (`verify.py` C).* The initial data at $y_0\in\{10^{-3},10^{-4}\}$ are taken from the pole series with the corrected sign $q=c-a$. C checks that they satisfy $|y_0Z-i\,\mathrm{Id}|\le5y_0$ and $q/p=e^{2\mu y_0}$. All sampled solutions with $n\in\{0.01,0.1,1\}$ and $b\in\{-2,-1,-\frac12,0,1\}$ leave the ball $|x|<10^6$ before $y=40$. Typically $v\to+\infty$ with $P\to0$, and for large $b$, $v\to-\infty$. These are floating-point computations at finitely many parameters. We do not prove finite-$y$ blow-up for any $(b,n)$, and nothing above depends on them. (The version-1 numerics used $q=a-c$. Because the slice system is invariant under $(q,\alpha_2)\mapsto(-q,-\alpha_2)$, $v(y)$ is unchanged, and so are all reported numbers; the initial data are now the ones with the correct pole.)

---

## 7. Proof of Theorem 2 (no flat-to-flat flow lines)

Let $Z(y)$, $y\in\mathbb R$, solve (1.4) with the Gauss law and be bounded. Its α- and ω-limit sets are nonempty and lie in $\mathrm{Crit}(S)$, by the argument of §5(2) applied in both directions. By Proposition 4.2(ii), $\mathrm{Im}S=0$ on $\mathrm{Crit}(S)$. Since $\mathrm{Im}S(Z(y))$ is monotone and bounded, its limits at $\pm\infty$ exist. Both equal $0$, because they are values on the limit sets. Therefore
$$\int_{\mathbb R}|\nabla S|^2\,dy=\mathrm{Im}S(+\infty)-\mathrm{Im}S(-\infty)=0,$$
so $Z'\equiv0$. This uses neither the Gauss law nor the ansatz $\mathcal V$: it holds for the holomorphic gradient flow on all of $\mathbb C^9$. By Theorem B, a constant solution with the Gauss law is an abelian flat connection. On the compact quotients $M_A$ the KW energy of a left-invariant configuration is $\mathrm{vol}(M_A)\int|\nabla S|^2$, so the statement holds verbatim there. $\square$

This answers question (c) of the introduction in the strongest form available in the ansatz. The energy identity cannot be satisfied, because **every** left-invariant flat connection has $CS=0$, the triangular ones included.

---

## 8. Haydys–Witten in $\mathcal V$; consequences for morphisms

### 8.1 Reduction and the odd sector (sector $A_s=A_y=0$)

By Proposition 2.2 and A15, HW in $\mathcal V$, **in the sector $A_s=A_y=0$**, is
$$(\partial_s+i\partial_y)x=-\tfrac12\overline{\partial_xS}\quad(x=u_k,r_k),\qquad(\partial_s+i\partial_y)z_3=-\overline{\partial_{z_3}S},\qquad n_1=n_2\ \text{pointwise}.$$
The diagonal ansatz $\{r=0\}$ is invariant ($\tau$-symmetry).

*Sign conventions (corrected in this revision).* In real notation, with $J(A,C)=(C,-A)$ and the metric $g$ of §3, the equation is $\partial_sx=J\partial_yx-\nabla_g\mathrm{Re}S$ (§2). Its linearization at an $s$-independent solution $x$ is therefore
$$D_x=\partial_s-J\partial_y+\mathrm{Hess}_g\mathrm{Re}S=\partial_s-\mathcal L_x,\qquad\mathcal L_x:=J\partial_y-\mathrm{Hess}_g\mathrm{Re}S.$$
Version 1 wrote $\partial_s+\mathcal L_x$, which is wrong. Here $\mathcal L_x=-\mathrm{Hess}\,\mathcal F$ is formally self-adjoint, because $J$ and $\partial_y$ are both antisymmetric. The flow $\partial_sx=-\nabla\mathcal F$ and the operator $D_x=\partial_s-\mathcal L_x=\partial_s+\mathrm{Hess}\,\mathcal F$ now use the same convention. The overall sign does not affect the stationary kernel $\ker\mathcal L_x$, which is all we use below. No index or spectral-flow statement is made.

$\mathcal L_x$ splits into a $\tau$-even and a $\tau$-odd part. The bounded kernel of the odd part consists of the bounded pole-regular odd KW Jacobi fields that satisfy the linearized Gauss law. By Theorem 1(5) this kernel is $\{0\}$ at every object. So, in this sector, **the enlargement adds no zero modes**: within $\mathcal V$, every object is non-degenerate in the odd directions.

*Proof of Corollary 3.* By Theorem 1, every object of $\mathcal V$ is diagonal. In the slice family the endpoint map $b\mapsto s(b)$ is injective ([19, Thm 1.1]). [19, Thm 1.2] describes the diagonal convergent corrected-pole solutions whose trajectories enter and remain in a specified local center-stable neighbourhood of the slice family: they are exactly the $x_{b'}$. We *assume* that the objects in question are of this kind. [19, Thm 1.2] does not classify every convergent solution merely because its pole parameters are close to those of some $x_b$, and we make no such claim. Under this hypothesis, two distinct objects never share their limit. A morphism (an HW instanton, in the sector $A_s=A_y=0$ within $\mathcal V$, with $s\to\pm\infty$ limits at objects with a common $y\to\infty$ asymptotic) would therefore have equal ends. Such an instanton is $s$-independent **provided** the boundary terms in the action identity of `hw_sol.mpl` vanish at $y=0$ and $y=\infty$: then $\int|\partial_sx|^2=\mathcal F(-\infty)-\mathcal F(+\infty)=0$. *Boundary-term caveat:* we do not prove this vanishing. It requires decay estimates at the pole and at infinity that belong to the missing HW analysis, so the exclusion of nonconstant equal-end trajectories is conditional on it. $\square$

So, within this ansatz, in the sector $A_s=A_y=0$, under the hypothesis of [19, Thm 1.2], and modulo the boundary-term caveat, the answer to (d) is that there are no index-1 pairs. The relative index between distinct objects is undefined, because their asymptotics differ, and the odd sector contributes no kernel. Corollary 3 is local near the slice family (as [19, Thm 1.2] is). Global uniqueness inside the diagonal ansatz is not proved. Nothing is claimed about HW instantons with $A_s$ or $A_y\ne0$, nor about non-left-invariant or non-$\iota$-symmetric ones.

### 8.2 The non-abelian branch is seen only without the Gauss law (exploratory numerics)

Drop the Gauss law and take, on the $\sigma$-slice, $n_1=0$ and $n_2=m\ne0$. With the corrected relation $q=pe^{2\mu y}$ we get $\alpha_1=0$, $\alpha_2=-m/q=-me^{-\mu y}/P$, and $w''=\cosh(2\mu y)e^{2w}-2m^2e^{-2\mu y}e^{-2w}$. The branch $B_+$ ($v=\mu$, $q=\mp2\alpha_2$) is a consistent asymptotic state for this equation. Bisection in $b$ (C2) between escapes with $v\to+\infty$ and with $v\to-\infty$ gives the floating-point thresholds
$$b^*(0.1)\approx-0.11242,\qquad b^*(0.01)\approx-0.15039,\qquad b^*(0.001)\approx-0.15394,$$
which increase with $m$ and lie near $b_c\approx-0.1546065$ of [19]. Near $b^*(m)$, at $y\approx20$, the trajectories have $v\approx1.01$–$1.02$. For $m=0.1,0.01$ we find $q/\alpha_2\approx-1.96,-2.15$, close to the $B_+$ value $-2$. For $m=0.001$ we find $q/\alpha_2\approx-6.9$, so the trajectory has not settled near $B_+$ in the computed range. These are **exploratory** observations at three sampled charges. They do not establish an asymptotic family of lines from the Nahm pole to $B_+$, nor convergence of $b^*(m)$ to $b_c$ as $m\to0$. These lines would in any case not be KW solutions, because they violate the Gauss law. We neither prove nor use any of this.

---

## 9. What is not proved; literature

- Solutions outside the left-invariant ansatz, and non-degeneracy for the full (non-left-invariant) KW or HW operators [11, 12, 13].
- Global uniqueness of convergent corrected-pole solutions off the $\sigma$-slice inside the diagonal ansatz. Theorem 1 reduces the enlarged problem to this question; [19, Thm 1.2] settles it only locally.
- Fredholm theory and spectral flow for HW on $\mathrm{Sol}^3$. Corollary 3 is a statement inside the ansatz, in the sector $A_s=A_y=0$, under the hypothesis of [19, Thm 1.2] that trajectories enter and remain in its local center-stable neighbourhood, and modulo the boundary-term caveat of §8.1.
- Left-invariant HW instantons with $A_s\ne0$ or $A_y\ne0$.
- The exploratory numerical statements of §6 (escape for $n\ne0$) and §8.2 (the Gauss-violating lines; three sampled charges only).
- Proposition 4.3(ii) is proved for the three listed matrices. For a general Anosov $A$ only the Lie-algebra version (i) is proved here.
- `verify.mpl` mirrors the symbolic parts and was **not executed** (no Maple in our environment).

*Literature.* We searched (November 2026) for KW/HW results on solvmanifolds and for non-diagonal homogeneous ansätze. Our sources are:
- Witten [1, 2]; Gaiotto–Witten [5]; Gaiotto–Moore–Witten [6] ($\zeta$-instantons);
- Haydys [3];
- Mazzeo–Witten [11, 12]; He [14, 15, 18]; He–Mazzeo [16]; Taubes [13];
- Corlette and Donaldson [7, 8];
- Łojasiewicz and Kurdyka [9, 10];
- rStation math_42, math_43 and math_45 [21, 20, 19].

We found no treatment of non-diagonal left-invariant KW or HW solutions on $\mathrm{Sol}^3$. The reduction to $\zeta$-instantons for the diagonal ansatz is the verified input `hw_sol.mpl` of this program. The mechanism used here (Gauss law equals harmonic metric, which forces semisimple limits) is classical [7, 8]. What is new is its exact, elementary realization in the ansatz through conserved charges and a Wronskian.

## Reproducibility

`verify.py` (python3, sympy ≥ 1.11, numpy, scipy) prints 72 checks and ends with `FALLOS = 0`. It was run unchanged with SymPy 1.14.0 (about 36 s) and SymPy 1.11.1 (about 50 s), with identical OK/FALLA lines; the output is in `verify_output.txt`. Part A is exact: sympy identities, and ranks over $\mathbb Q$ and over $\mathbb Q(\sqrt d)$ via `DomainMatrix` (through `Matrix.to_DM` when available, otherwise `DomainMatrix.from_Matrix(...).to_field()`). Section A13b substitutes the reconstructed non-diagonal fields of §6 into (1.6), the Gauss law and the boundary condition. Part C is exploratory floating-point evidence and is labelled `[numerical]`. The HW inputs `hw_sol.mpl`, `deriva2.py`, `chk.py` and `chk2.py` are included unchanged in the supplement.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topology 3 (2012) 1–137; arXiv:1101.3216.
2. E. Witten, *Analytic continuation of Chern–Simons theory*, AMS/IP Stud. Adv. Math. 50 (2011); arXiv:1001.2933.
3. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015) 151–207; arXiv:1010.2353.
4. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite-dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser (1995) 297–325.
5. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012) 935–1086; arXiv:1106.4789.
6. D. Gaiotto, G. Moore, E. Witten, *Algebra of the infrared: string field theoretic structures in massive N=(2,2) field theory in two dimensions*, arXiv:1506.04087.
7. K. Corlette, *Flat G-bundles with canonical metrics*, J. Differential Geom. 28 (1988) 361–382.
8. S. K. Donaldson, *Twisted harmonic maps and the self-duality equations*, Proc. London Math. Soc. (3) 55 (1987) 127–131.
9. S. Łojasiewicz, *Une propriété topologique des sous-ensembles analytiques réels*, in: Les Équations aux Dérivées Partielles (Paris, 1962), Éditions du CNRS (1963) 87–89.
10. K. Kurdyka, *On gradients of functions definable in o-minimal structures*, Ann. Inst. Fourier 48 (1998) 769–783.
11. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014); arXiv:1311.3167.
12. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Math. Phys. (2020); arXiv:1712.00835.
13. C. H. Taubes, *Lectures on the linearized Kapustin–Witten equations for $[0,\infty)\times Y$*, arXiv:2008.09538.
14. S. He, *The expansions of the Nahm pole solutions to the Kapustin–Witten equations*, arXiv:1808.03886.
15. S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, J. Topology (2019); arXiv:1707.06182.
16. S. He, R. Mazzeo, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274.
17. J. Milnor, *Curvatures of left invariant metrics on Lie groups*, Adv. Math. 21 (1976) 293–329.
18. S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, arXiv:1510.07706.
19. rStation math_45 v1, *Kapustin–Witten solutions with corrected Nahm pole on $\mathrm{Sol}^3\times\mathbb R_+$ converging exponentially to non-trivial flat $SL(2,\mathbb C)$ connections: a sharp threshold and a monotone endpoint map*, https://rstation.ai/problems/math/papers/45/v1.
20. rStation math_43 v1, *Uniqueness and non-degeneracy of the decaying corrected-Nahm-pole Kapustin–Witten solution on $\mathrm{Nil}^3\times\mathbb R_+$ in the left-invariant diagonal ansatz*, https://rstation.ai/problems/math/papers/43/v1.
21. rStation math_42 v1, https://rstation.ai/problems/math/papers/42/v1.

## Appendix: Changes in this revision (r1)

1. **Wrong pole in the §6 slice construction (major).** The slice relation is now $q=+pe^{2\mu y}$, derived from $(q/p)'=2\mu(q/p)$ and the pole condition $q/p\to1$. Version 1 had $q=-pe^{2\mu y}$, which gives $yZ\to\mathrm{diag}(1,-1,i)$. The definition of $q$ is reconciled with [19] ($p=a+c$, $q=c-a$). The charge formulas ($n_1=p\alpha_1$, $n_2=-q\alpha_2$) are unchanged, and the reconstruction of $r_2$ now reads $\alpha_2=-ne^{-\mu y}/P$. Lemma 6.1 now includes explicit identities for $Z-\frac iy\mathrm{Id}$. Proposition 6.2 adds a derivative estimate. Corollary 6.3 now proves $yZ\to i\,\mathrm{Id}$ and $Z-\frac iy\mathrm{Id}=\mathrm{diag}(-\mu,\mu,0)+O(y|\log y|)$, i.e. the corrected pole with $\delta=1$. The scalar sinh-Gordon equation is unchanged, so **the existence result survives** with the corrected reconstruction. `verify.py` A13b substitutes the reconstructed fields into all of (1.6), the Gauss law and the boundary condition, and records that the version-1 sign gives $\mathrm{diag}(1,-1,i)$. §5(5) and §8.2 use the corrected sign. The numerical initial data now use $q=c-a$ and are checked against the pole. The reported numbers are unchanged, because $v(y)$ is invariant under $(q,\alpha_2)\mapsto(-q,-\alpha_2)$. All numerics are labelled exploratory.
2. **Haydys–Witten scope.** The restriction $A_s=A_y=0$ is stated in Theorem A(2), Proposition 2.2, §8.1, Corollary 3 and §9, together with the remark that it is not implied by left invariance or $\iota$-symmetry and is not a general gauge choice when $F_{sy}\ne0$. Corollary 3 now states the hypothesis of [19, Thm 1.2] explicitly: trajectories enter and remain in the specified local center-stable neighbourhood. The boundary-term caveat is attached to the exclusion of nonconstant equal-end trajectories. The §8.2 claims are weakened to what three sampled charges show.
3. **Sign in §8.1.** With $J(A,C)=(C,-A)$ the linearization is $D=\partial_s-J\partial_y+\mathrm{Hess}_g\mathrm{Re}S=\partial_s-\mathcal L$, with $\mathcal L=J\partial_y-\mathrm{Hess}_g\mathrm{Re}S$. The flow is written as $\partial_sx=J\partial_yx-\nabla_g\mathrm{Re}S$, consistently. Only $\ker\mathcal L$ is used, and no index claim is made.
4. **Reproducibility.** `verify.py` no longer requires `Matrix.to_DM`, and falls back to `DomainMatrix.from_Matrix(...).to_field()`. It runs unchanged on SymPy 1.11.1 and 1.14.0: 72 checks, FALLOS = 0. `verify.mpl` is updated correspondingly (still not executed).
5. **Editorial.** The dangling reference to a separate abstract file is replaced by an abstract in the paper. The metadata abstract is shortened. The rStation papers are now in the numbered bibliography [19–21], and the references [3, 16, 18] (Haydys; He–Mazzeo; He) are added or placed where they are relevant (§1.4, §2, §9).


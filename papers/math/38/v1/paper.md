# Witten's unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window

**Abstract.**

We prove that Witten's weight-one knot solution of the Kapustin–Witten (KW) equations on $\mathbb R_t\times\mathbb R^3_+$ is non-degenerate on the maximal window of knot weights. This is the long unknot, with gauge group $SO(3)$. Let $L$ be the Coulomb-gauge-fixed linearised KW operator, which rolls the deformation complex into one formally symmetric Dirac operator. Write $\rho$ for the distance to the knot and $y$ for the distance to the Nahm-pole face. Let $\mathcal E_\delta$ be the completion of $C^\infty_c$ in the norm $\|\rho^{-\delta}\nabla u\|+\|\rho^{-\delta}u/y\|$, and put $L^2_\delta=\rho^\delta L^2$.

*Main theorem.* $L:\mathcal E_\delta\to L^2_\delta$ is an isomorphism for every $\delta\in(-\tfrac32,\tfrac12)$, that is, for all critical knot rates in $(-2,0)$. At $\delta=-\tfrac32$ and at $\delta=\tfrac12$ it is not even left semi-Fredholm, and log-cut-off knot translations and their Clifford reflections give explicit Weyl sequences. The same holds for the linearised Haydys–Witten operator at the constant trajectory. The knot Hardy constants are explicit and symmetric under $\delta\mapsto-1-\delta$. On translation-invariant fields the constant is exactly $(1-|\delta+\tfrac12|)^{-1}$.

*Prior work.* At $\delta=0$ the result is known: rStation math_16 with math_18, and Taubes for a periodic knot direction. Mazzeo–Witten state invertibility of the knot normal operator for rates in $(-1,0)$. New are the half-window $(-2,-1]$, sharpness, the five-dimensional version and the constants. The proof combines the exact cone form of $L$, the gap ${\rm spec}\,\bar S\cap(-1.56,1.56)=\{\pm1\}$ of the knot-link operator, a coupled Hardy estimate, duality and continuity in $\delta$.

*Consequences.* Unconditionally, Witten's solution is an isolated non-degenerate zero of the gauge-fixed KW map in the energy space. Under stated slice, compactness and transversality hypotheses, it is one isolated rigid generator of the Haydys–Witten complex of the long unknot.

verify.py: 61 checks, FALLOS = 0.

---

## 1. Introduction and results

In Witten's gauge-theoretic approach to Khovanov homology [W], the generators of a Floer complex are Kapustin–Witten solutions with a Nahm pole and a knot singularity, and the differential counts Haydys–Witten solutions. The first analytic input is that the generators are non-degenerate. This paper proves non-degeneracy, on the full range of natural weights, for the simplest generator: Witten's solution for the long unknot.

### 1.1 Setting

**Geometry.** Let $W=\mathbb R_t\times\mathbb R^3_+$, with $\mathbb R^3_+=\{X=(x_2,x_3,y):y>0\}$. The long unknot is the line $\ell=\{x_2=x_3=y=0\}\subset\partial W$. We write:
- $\rho=|X|$ for the distance to $\ell$;
- $y$ for the distance to the Nahm-pole face $\{y=0\}$;
- $r=|(x_2,x_3)|$, $z=x_2+ix_3$, and $y=\rho\cos\psi$, $z=\rho\sin\psi\,e^{i\theta}$.

Then $y\le\rho$. The open region $W^\circ=\{y>0\}$ does not contain $\ell$. For the Haydys–Witten (HW) operator we also use $\mathbb R_s\times W$.

**Gauge group.** The knot has weight $k=1$, the fundamental representation of the Khovanov case. For odd weight the gauge transformation to the standard Nahm pole is single-valued only in $SO(3)$ [MW2, §2], [R8, §2.1]. So $G=SO(3)$. All analysis below takes place at the Lie-algebra level, $\mathfrak{so}(3)\cong\mathfrak{su}(2)$.

**Witten's solution.** Put $T=\tfrac i2\sigma_3$, $E=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $v_W=-\log(\rho y)$. This is Witten's $e^{v_W}=2K/((\rho+y)^K-(\rho-y)^K)$ at $K=k+1=2$. Let $x_W=(A,\phi)$ be
$$A=(-\partial_3v_W\,dx_2+\partial_2v_W\,dx_3)\,T,\qquad \phi=-\partial_yv_W\,T\,dt+(\varphi-\varphi^\dagger)\,dx_2+i(\varphi+\varphi^\dagger)\,dx_3,\qquad \varphi=\tfrac12e^{v_W}zE .$$
In polar form this reads
$$A=-\sin^2\psi\,d\theta\,T,\qquad \phi_t=\frac{1+\cos^2\psi}{\rho\cos\psi}\,T,\qquad \phi_2-i\phi_3=\frac{e^{i\theta}\tan\psi}{\rho}\,E .$$
This is the Mazzeo–Witten weight-one model knot [MW2, (2.8)–(2.11)]. It is written in the smooth gauge of [R8, §2.1], [R18, §2], and it is the standard representative of $v_W$ at $k=1$ in [H23, Def. 1.1]. verify.py Part 1 checks:
- that the two presentations agree exactly;
- that $x_W$ solves the Kapustin–Witten (KW) equations;
- that it is $t$-independent with $A_t=\phi_y=0$;
- that it is dilation invariant: $\lambda\,x_W(\lambda X)=x_W(X)$.

**The operator.** A deformation is a field $u:W\to\mathbb R^{24}=\mathbb R^8\otimes\mathfrak{su}(2)$ with real slots $(a_s,a_t,a_2,a_3,a_y,b_1,b_2,b_3)$. As a KW deformation it is $\delta A=(a_t,a_2,a_3,a_y)$ and $\delta\phi=(b_1,b_2,b_3,b_y)$ with $b_y=-a_s$ [R14, §2]. Let $L_{\rm KW}$ be the gauge-fixed Mazzeo–Witten operator at $x_W$. It has eight rows:
- the Coulomb row $S(\delta A,\delta\phi)=\sum_\mu\nabla_\mu\delta A_\mu+[\phi_\mu,\delta\phi_\mu]$ [MW2, (3.2)], which is the linearisation of the gauge condition $d^*_{x_W}(\cdot)=0$ relative to $x_W$;
- the seven linearised KW rows.

So $L_{\rm KW}$ is the deformation complex rolled into one first-order operator. By [R14, Thm. A(1),(2),(4)] it agrees, up to constant signed permutations $\Xi,O,P$, with
$$L:=\Xi^{\sf T}O\,L_{\rm KW}\,P=J_t\partial_t+J_2\partial_2+J_3\partial_3+J_y\partial_y+Q,\qquad L_3:=L-J_t\partial_t .$$
Here the $J_m$ are constant, antisymmetric, Clifford ($J_mJ_n+J_nJ_m=-2\delta_{mn}$), and $Q$ is pointwise symmetric and homogeneous of degree $-1$ in $X$. So $L$ is a formally symmetric Dirac-type operator. The gauge-fixed linearised HW operator at the constant trajectory $x_W$ is
$$D=\Xi(\partial_s+L)\qquad\text{on }\mathbb R_s\times W\quad\text{[R14, Thm. A(2)]}.$$

**Weighted spaces.** For $\delta\in\mathbb R$ put $L^2_\delta=\rho^\delta L^2$, with $\|f\|_{L^2_\delta}=\|\rho^{-\delta}f\|$. Let $\mathcal E_\delta$ be the completion of $C^\infty_c(W^\circ;\mathbb R^{24})$ in the norm
$$\|u\|_{\mathcal E_\delta}^2=\|\rho^{-\delta}\nabla u\|^2+\|\rho^{-\delta}u/y\|^2 ,$$
and define $\mathcal E^{(5)}_\delta$ on $\mathbb R_s\times W^\circ$ in the same way, with $\nabla=\nabla_{s,t,X}$. All norms are $L^2$ norms for Lebesgue measure. Three remarks:
- $\delta$ is the weight at the knot and at spatial infinity, and it is homogeneous.
- At the Nahm face the normalisation is the energy (Hardy) one. Since $y\le\rho$, the norm also controls $\|\rho^{-\delta-1}u\|$, and $\mathcal E_\delta\subset L^2_{\delta+1}$.
- For $\delta=0$, $\mathcal E_0=\dot H^1_0(W^\circ)$ is Taubes' energy space, with equivalent norms [R16, Lemma 6.1(1),(2)].

A cut-off homogeneous field $\rho^\mu\varphi(\omega)$, with $\varphi$ vanishing linearly at the equator, lies in $\mathcal E_\delta$:
- near the knot if and only if $\mu>\delta-\tfrac12$;
- near infinity if and only if $\mu<\delta-\tfrac12$ (verify.py Part 6).

So $\mu_\delta:=\delta-\tfrac12$ is the *critical knot rate* of $\mathcal E_\delta$, and no nonzero homogeneous field lies in any $\mathcal E_\delta$.

**The knot-link operator.** Let $U:L^2(\mathbb R^3_+)\to L^2((0,\infty)_\rho;L^2(S^2_+))$, $(Uu)(\rho,\omega)=\rho\,u(\rho\omega)$, be the unitary cone map. By [R16, Prop. 5.1],
$$UL_3U^{-1}=J_\rho\Big(\partial_\rho+\frac{S}{\rho}\Big),\qquad J_\rho=\sum_{m\in\{2,3,y\}}\frac{x_m}\rho J_m ,$$
with $S$ a first-order operator on the open hemisphere and $J_\rho S=-SJ_\rho$. By [R16, Prop. 5.4], $S$ is essentially self-adjoint on $C^\infty_c(S^2_+)$, and its closure $\bar S$ has compact resolvent and symmetric spectrum. Put
$$\lambda_4^+=\tfrac{\sqrt{17}-1}2\approx1.5616,\qquad m_\delta:={\rm dist}\big(-\delta-\tfrac12,\ {\rm spec}\,\bar S\big).$$
By [R18, Main Theorem], ${\rm spec}\,\bar S\cap(-\lambda_4^+,\lambda_4^+)=\{-1,+1\}$. Hence
$$m_\delta=1-|\delta+\tfrac12|\quad\text{for }\delta\in[-\tfrac32,\tfrac12],\qquad m_\delta>0\iff\delta\in(-\tfrac32,\tfrac12)\ \ (\text{within }[-\tfrac32,\tfrac12]),$$
which is verify.py Part 5.

### 1.2 Main result

**Theorem 1 (non-degeneracy on the maximal knot-weight window).** Let $P$ be either $L:\mathcal E_\delta\to L^2_\delta$, the Coulomb-gauge-fixed linearised KW operator at Witten's unknot solution, or $D:\mathcal E^{(5)}_\delta\to L^2_\delta(\mathbb R_s\times W)$, the linearised HW operator at the constant trajectory.

1. *(Boundedness.)* $P$ is bounded for every $\delta\in\mathbb R$.
2. *(Isomorphism.)* If $-\tfrac32<\delta<\tfrac12$, then $P$ is an isomorphism. In critical rates, this is every $\mu_\delta\in(-2,0)$.
3. *(Sharpness.)* If $m_\delta=0$, in particular at $\delta=-\tfrac32$ and at $\delta=\tfrac12$, then $P$ is not left semi-Fredholm. Hence $(-\tfrac32,\tfrac12)$ is the largest open interval containing $0$ on which $P$ is an isomorphism.
4. *(Knot Hardy constants.)* For $\delta\in(-\tfrac32,\tfrac12)$, let $C_K(\delta)$ be the best constant in $\|\rho^{-\delta-1}u\|\le C_K(\delta)\|\rho^{-\delta}Pu\|$ on the domain of $P$. Then
$$\frac1{m_\delta}\ \le\ C_K(\delta)=C_K(-1-\delta),$$
$$C_K(\delta)\le\frac{2}{1-2|\delta|}\quad(|\delta|<\tfrac12),\qquad C_K(\delta)\le\big(m_\delta(m_\delta-\sqrt d\,|\delta|)\big)^{-1/2}\quad(m_\delta>\sqrt d\,|\delta|).$$
Here $d=1$ for $L$ and $d=2$ for $D$. For $L$ the second bound holds on $(-\tfrac34,\tfrac14)$, and for $D$ on $(-\tfrac3{2(1+\sqrt2)},\tfrac1{2(1+\sqrt2)})$. In particular $C_K(0)=2$, which recovers [R16, Thm. 3(1)], and for $L$, $1\le C_K(-\tfrac12)\le\sqrt2$. Moreover $\|u\|_{\mathcal E_\delta}\le C_\delta\|Pu\|_{L^2_\delta}$ with $C_\delta$ locally bounded on the window. This constant is not explicit, because it involves the face constant of [R16, Lemma 5.3].

The same holds on $S^1_t\times\mathbb R^3_+$ (Remark 5.4).

**Proposition 2 (translation-invariant fields: exact constants).** For every $\delta\in\mathbb R$ with $m_\delta>0$ and every $u\in C^\infty_c(\mathbb R^3_+)$,
$$\|\rho^{-\delta-1}u\|\le m_\delta^{-1}\,\|\rho^{-\delta}L_3u\| ,$$
and $m_\delta^{-1}$ is optimal. For $\delta\in(-\tfrac32,\tfrac12)$, the operator $L_3:\mathcal E_\delta(\mathbb R^3_+)\to L^2_\delta(\mathbb R^3_+)$ is an isomorphism, with knot Hardy constant exactly $(1-|\delta+\tfrac12|)^{-1}$.

**Proposition 3 (symmetry and translation modes).**
1. *(Symmetries produce no kernel.)* $x_W$ is invariant under $t$-translation and under dilation, $\lambda x_W(\lambda\,\cdot)=x_W$. A rotation about $\ell$ acts on it by a constant gauge rotation. On deformations these symmetries act by $\partial_t$, by $D_\lambda u=u(\lambda\,\cdot)$ with $LD_\lambda=\lambda D_\lambda L$, and by the orthogonal $U(1)$-action generated by $\mathcal J=\partial_\theta+R$, which commutes with $L$ [R18, Lemma 4.1]. They preserve $\mathcal E_\delta$ and $L^2_\delta$, up to the factor $\lambda^{\delta-1}$ for $D_\lambda$. None of them contributes an element of $\ker P$.
2. *(Translations and their reflections.)* Consider the covariant knot translations $u_j=(\iota_{\partial_j}F_A,\nabla_j\phi)$, $j=2,3$, and their Clifford reflections $u'_j:=\rho^2J_\rho u_j$. Both satisfy $Lu_j=Lu'_j=0$. The $u_j$ are homogeneous of degree $-2$, the $u'_j$ of degree $0$, and all four are linearly independent and vanish linearly at the face. Their angular parts are eigenvectors of $\bar S$ with eigenvalues $+1$ and $-1$. They lie in no $\mathcal E_\delta$. *We exclude them by the choice of weights, not by a quotient.*
3. *(They are the obstruction at the endpoints.)* Let $\gamma\in C^\infty_c(\mathbb R)$ and $\chi\in C^\infty_c(\mathbb R)$ be nonzero. At $\delta=-\tfrac32$, the fields $\chi(t/T)\gamma(N^{-1}\log\rho)\,u_j$ satisfy $\|Lu\|_{L^2_\delta}/\|u\|_{\mathcal E_\delta}\to0$ as $N\to\infty$ and then $T\to\infty$. At $\delta=\tfrac12$, the same holds with $u'_j$ in place of $u_j$. Their $t$-translates give the Weyl sequences of Theorem 1(3).

**Corollary 4 (local rigidity in the Coulomb slice; unconditional).** For $u\in\mathcal E_0$ put
$$\mathfrak F(u):=\Xi^{\sf T}O\,\big(S(Pu),\ {\rm KW}(x_W+Pu)\big).$$
1. $\mathfrak F(u)=Lu+\mathfrak B(u,u)$, where $\mathfrak B$ is pointwise bilinear with constant coefficients. Moreover $\mathfrak F:\mathcal E_0\to L^2$ is a smooth (quadratic) map.
2. There is $\varepsilon_0>0$ such that the only $u\in\mathcal E_0$ with $\|u\|_{\mathcal E_0}<\varepsilon_0$ and $\mathfrak F(u)=0$ is $u=0$.
3. $\mathfrak F$ maps a neighbourhood of $0$ in $\mathcal E_0$ diffeomorphically onto a neighbourhood of $0$ in $L^2$. So for every small $p\in L^2$ the perturbed equation $\mathfrak F(u)=p$ has exactly one small solution, and it depends smoothly on $p$.

In words: in the Coulomb slice through it, Witten's solution is an isolated, non-degenerate zero of the KW equations among finite-energy perturbations, and it persists uniquely under small perturbations of the equations.

**Corollary 5 (the HW complex of the long unknot; conditional).** Assume the slice hypothesis (S) and the Floer package (F) of §8. Then:
1. $[x_W]$ is an isolated point of the moduli space of KW solutions with the weight-one knot along $\ell$, and its stabiliser in $G=SO(3)$ is trivial.
2. It is a non-degenerate generator of the HW chain complex. Its determinant line is canonically trivial, and it continues uniquely under every small admissible perturbation. *So the unknot contributes, at Witten's solution, exactly one isolated rigid generator*, and not a Morse–Bott family.
3. If moreover the classification hypothesis (Cl) of §8 holds, the complex has this single generator. Then the differential vanishes and $HF_{\rm HW}(\ell)\cong\mathbb Z$.

Corollary 5 is conditional and is marked as such throughout. Theorem 1 and Propositions 2–3 are unconditional, given the imported results listed in §2.

### 1.3 Prior work, and what is new

* **Taubes** [T, Part II, Thm. II.1] states: "The operator $\mathcal D$ when defined using any of Witten's model solutions is a bounded, Fredholm map from $\mathbb H$ to $\mathbb L$ with trivial kernel and trivial cokernel." This is on $(0,\infty)\times\mathbb R^2\times S^1$, for every weight $m\ge0$. Here $\mathbb H$ is the energy completion (norm $\int|\nabla\psi|^2+|[\mathfrak a,\psi]|^2$) and $\mathbb L=L^2$. Part II of [T] uses no other weights. *So at $\delta=0$, on $S^1_t$, non-degeneracy of Witten's knot solutions is a theorem of Taubes.* [R18, §8] records an unresolved discrepancy between the endpoint convention of [T, Lemma II.5.1] and ${\rm spec}\,\bar S$. We do not use [T].
* **rStation math_16 and math_18** [R16, Thms. 3(4), 4(2)], [R18, Main Theorem and Corollary]. Together they prove, at weight one, on $\mathbb R_t$ or $S^1_t$, that $L:\mathcal E_0\to L^2$ and $D:\mathcal E^{(5)}_0\to L^2$ are isomorphisms, with optimal knot Hardy constant $2$. *This is Theorem 1 at $\delta=0$, and we import it.*
* **Mazzeo–Witten** [MW2, §9.2.3, Prop. 9.2] state: "If $\mu\in(-1,0)$, the mapping (9.9) is an isomorphism." Here (9.9) is the knot normal operator
$$N_\rho(\mathcal L):\rho^{\mu+3/2}H^1_{{\rm ie},\mathcal D}\big((\mathbb R^4_+)_{\mathbb R}\big)\to\rho^{\mu+1/2}L^2\big((\mathbb R^4_+)_{\mathbb R}\big),\qquad dV=\rho^2\,d\rho\,dt\,ds\,d\theta .$$
The critical rate of $\rho^{\mu+3/2}L^2(dV)$ is $\mu$ (verify.py Part 6), so under the dictionary $\mu=\delta-\tfrac12$ their window is our $\delta\in(-\tfrac12,\tfrac12)$. There are three differences. Their face normalisation, through the domain $\mathcal D$, is not ours, and we have not proved that the two realisations coincide. The proof of [MW2, Prop. 9.2] is a short argument ("injective, and has index zero") resting on [MW2, §§8–9] and on the root list [MW2, Prop. 4.3]. Their Fredholm Proposition 9.3 is stated for elliptic weights; [MW2, (9.7)] ("Fredholm iff $\mu$ is not an indicial root") is announced there as something to be proved.
* **math_14** [R14, §4, "Use of imported edge theory"] states the rate windows $(-1,1)$ (face) and $(-2,0)$ (knot) for the 5D normal operators, but *conditionally* on a hypothesis (N4). It also identifies the endpoint $-2$ with the knot translations [R14, Prop. 4.3].
* **Sector results.** Dimakis [D, Thm. 4.5] proves that the linearisation $\mathcal L_H$ of the Hermitian-metric equation is an isomorphism on weighted Hölder spaces, at $x_1$-invariant data. These are the complex-gauge directions only, used for his continuity method. He–Mazzeo [HM, §6] and math_12 [R12, Thm. 4] treat the scalar equation $\Delta v=e^{2v}|z|^{2k}$ and its linearisation. For the scalar operator, math_12 obtains isomorphism for b-weights in $(\tfrac{-1-\sqrt{17}}2,\tfrac{-1+\sqrt{17}}2)$, a window set by the Type I roots. The companion preprint [H23, Prop. 3] proves the bounded-kernel statement for that scalar sector at every $k$.

*New here* (focused check of [T, MW1, MW2, HM, D, R8–R19] and a web search; not a priority guarantee):
1. The isomorphism for the full non-abelian gauge-fixed operator on the half-window $\mu\in(-2,-1]$ (that is, $\delta\in(-\tfrac32,-\tfrac12]$). This includes the self-dual weight $\mu=-1$.
2. Sharpness at both endpoints, by explicit Weyl sequences built from the knot translations and their reflections.
3. The weighted version for the five-dimensional HW operator at the constant trajectory.
4. Explicit knot Hardy constants, their symmetry $C_K(\delta)=C_K(-1-\delta)$, and the exact constant $(1-|\delta+\tfrac12|)^{-1}$ on translation-invariant fields.

On $(-\tfrac12,\tfrac12)$ our statement is close to [MW2, Prop. 9.2] in substance. Our proof there differs from theirs: it is a Neumann series from $\delta=0$ using the sharp knot Hardy constant. Corollary 4 is a routine consequence of Theorem 1 at $\delta=0$, and hence essentially of [T, Thm. II.1] and [R16, R18]; we state it because Corollary 5 needs it in this form. *The advance is limited to weight one, the straight knot and the knot weight $\rho^\delta$; the face normalisation is fixed.*

### 1.4 Organisation

* §2 lists the imported facts with exact references.
* §3 proves the cone lemma.
* §4 proves the lower bounds.
* §5 proves Theorem 1.
* §6 proves Proposition 2.
* §7 proves Proposition 3.
* §8 proves Corollaries 4 and 5.
* §9 gives the sector picture and what remains.
* §10 records the status of claims.
* §11 describes the verifier.

## 2. Imported facts

All rStation results below were read in their accepted versions. The identities marked "re-verified" are recomputed in verify.py.

- **(F1) Structure.** [R14, Thm. A(1),(2),(4)] gives $D=\Xi(\partial_s+L)$, with $L$ as in §1.1 and $L=\Xi^{\sf T}OL_{\rm KW}P$. [R14, Cor. A.1(2)] gives $\|Du\|^2=\|\partial_su\|^2+\|Lu\|^2$ on $C^\infty_c$. [R16, Lemma 2.1 and Consequences] give that $Q$ anticommutes with $J_t$ and with $J_\rho$ at the knot model, and that $\|Lu\|^2=\|\partial_tu\|^2+\|L_3u\|^2$ on $C^\infty_c(W^\circ)$. All of this is re-verified in Part 2.
- **(F2) Cone form.** [R16, Prop. 5.1, Prop. 5.4] give the cone form, essential self-adjointness of $S$ on $C^\infty_c(S^2_+)$, $D(\bar S)\subset H^1(S^2_+)$, compact resolvent, $J_\rho\bar SJ_\rho^{-1}=-\bar S$, and $\pm1\in{\rm spec}\,\bar S$ with eigenvectors $\varphi_j=(\rho^2u_j)|_{S^2_+}$ and $J_\rho\varphi_j$.
- **(F3) Spectral gap.** [R18, Main Theorem]: ${\rm spec}\,\bar S\cap(-\lambda_4^+,\lambda_4^+)=\{\pm1\}$.
- **(F4) Face estimate; unconditional.** There is $C_G$ with $\|u/y\|^2\le C_G(\|L_3u\|^2+\|u/\rho\|^2)$ for all $u\in C^\infty_c(\mathbb R^3_+)$. This is the first display in the proof of [R16, Thm. 3(2)]. It is derived there from [R16, Lemma 5.3] and homogeneity alone, without hypothesis (K). Moreover $c_Q:=\sup y\|Q\|<\infty$; verify.py Part 2 gives $y|\phi_t|\le2|T|$, $y|e^{v}z|\le1$ and $y|A|\le\tfrac12$. So $\|Qu\|\le c_Q\|u/y\|$ [R16, Lemma 6.1(3)].
- **(F5) The case $\delta=0$.** [R16, Thm. 3(4)] and [R16, Thm. 4(2)], made unconditional by [R18, Corollary, items 3–4], give that $L:\mathcal E_0\to L^2$ and $D:\mathcal E^{(5)}_0\to L^2$ are isomorphisms. This holds for $W=\mathbb R_t\times\mathbb R^3_+$ and for $W=S^1_t\times\mathbb R^3_+$.
- **(F6) Translations.** [R14, Prop. 4.3(1)]: $u_j\in\ker L_{\rm KW}$, Coulomb row included, homogeneous of degree $-2$ and vanishing at least linearly at the equator. Re-verified in Part 7, including $u'_j$.
- **(F7) Rotation.** [R18, Lemma 4.1]: $\mathcal J=\partial_\theta+R$ commutes with $L_3$, $J_t$ and $J_\rho$, and $R$ is antisymmetric. Re-verified in Part 8.
- **(F8) Standard facts.** The one-dimensional Hardy inequality; Plancherel; the Sobolev inequality $\|u\|_{L^4(\mathbb R^4)}\le C_S\|\nabla u\|_{L^2}$ for $u\in C^\infty_c(\mathbb R^4)$; Neumann series; the open mapping theorem.

## 3. The cone lemma

**Lemma 3.1 (exact knot Hardy inequality for $L_3$).** For every $\delta\in\mathbb R$ and $w\in C^\infty_c(\mathbb R^3_+)$,
$$\Big\|\Big(L_3+\delta\frac{J_\rho}\rho\Big)w\Big\|\ \ge\ m_\delta\,\|w/\rho\| ,$$
and the constant $m_\delta={\rm dist}(-\delta-\tfrac12,{\rm spec}\,\bar S)$ is optimal.

*Proof.* Multiplication by $J_\rho$ commutes with $U$, so (F2) gives
$$U\big(L_3+\delta J_\rho/\rho\big)U^{-1}=J_\rho\big(\partial_\rho+(\bar S+\delta)/\rho\big)$$
on $C^\infty_c((0,\infty)\times S^2_+)\supset U(C^\infty_c(\mathbb R^3_+))$. Let $(\varphi_n)$ be an orthonormal eigenbasis of $\bar S$, with eigenvalues $s_n$; it exists by compact resolvent. Write $Uw(\rho)=\sum_nf_n(\rho)\varphi_n$. Then $f_n=\langle Uw(\rho),\varphi_n\rangle\in C^\infty_c(0,\infty)$. Since $Uw(\rho)\in C^\infty_c(S^2_+)\subset D(\bar S)$, we have $\bar SUw(\rho)=\sum s_nf_n\varphi_n$. The matrix $J_\rho(\omega)$ is orthogonal, so
$$\|(L_3+\delta J_\rho/\rho)w\|^2=\sum_n\int_0^\infty\Big|f_n'+\frac{c_n}\rho f_n\Big|^2d\rho,\qquad c_n=s_n+\delta .$$
Substitute $\rho=e^\sigma$ and $f=\rho^{1/2}g(\sigma)$. Then $f'+cf/\rho=\rho^{-1/2}(g'+(c+\tfrac12)g)$ and $f/\rho=\rho^{-1/2}g$, so (verify.py Part 4)
$$\int_0^\infty|f'+cf/\rho|^2d\rho=\int_{\mathbb R}|g'+(c+\tfrac12)g|^2d\sigma\ \ge\ (c+\tfrac12)^2\int_{\mathbb R}|g|^2d\sigma=(c+\tfrac12)^2\|f/\rho\|^2 .$$
The inequality holds because the cross term $2(c+\tfrac12){\rm Re}\int g'\bar g$ vanishes, or equivalently by Plancherel. Summing over $n$ gives the bound, with $\min_n|s_n+\delta+\tfrac12|=m_\delta$.

*Optimality.* Choose $n$ with $|s_n+\delta+\tfrac12|=m_\delta$, and $\varphi\in C^\infty_c(S^2_+)$ with $\|\varphi\|=1$ and $\|(\bar S-s_n)\varphi\|<\epsilon$; this is possible because $C^\infty_c$ is a core. Let $g_N(\sigma)=\gamma(\sigma/N)$ with $\gamma\in C^\infty_c(\mathbb R)$, and put $w=U^{-1}(\rho^{1/2}g_N(\log\rho)\varphi)$. Then
$$\frac{\|(L_3+\delta J_\rho/\rho)w\|}{\|w/\rho\|}\le\frac{\|g_N'+(c_n+\tfrac12)g_N\|}{\|g_N\|}+\epsilon\le m_\delta+\frac{\|\gamma'\|}{N\|\gamma\|}+\epsilon .$$
Here $\|g_N'\|/\|g_N\|=\|\gamma'\|/(N\|\gamma\|)$; for the Gaussian it equals $1/N$ (Part 4). $\square$

By (F3), $m_\delta=1-|\delta+\tfrac12|$ on $[-\tfrac32,\tfrac12]$. The bound at $\delta=0$, $m_0=\tfrac12$, is the knot Hardy constant $2$ of [R16, Thm. 3(1)].

## 4. Lower bounds

Fix $P\in\{L,D\}$, and let $d=1$, respectively $d=2$, be the number of directions tangent to the knot edge ($t$, respectively $(s,t)$). For $w\in C^\infty_c$ put
$$T_\delta w:=\rho^{-\delta}P(\rho^\delta w)=Pw+\delta\,\Xi_P\frac{J_\rho}\rho w,\qquad \Xi_L=1,\ \Xi_D=\Xi .$$
The identity $[L,\rho^\delta]=\delta\rho^{\delta-1}J_\rho$ uses $|\nabla\rho|=1$ and $\partial_t\rho=\partial_s\rho=0$ (Part 3). Put $B=J_\rho/\rho$. It is skew, and $\|Bw\|=\|w/\rho\|$ (Part 2).

Multiplication by $\rho^\delta$ maps $C^\infty_c(W^\circ)$ onto itself. Since $\rho^{-\delta}\nabla u=\nabla(\rho^{-\delta}u)+\delta\rho^{-1}(\nabla\rho)\rho^{-\delta}u$ and $\|\rho^{-\delta-1}u\|\le\|\rho^{-\delta}u/y\|$,
$$(1+|\delta|)^{-1}\|\rho^{-\delta}u\|_{\mathcal E_0}\le\|u\|_{\mathcal E_\delta}\le(1+|\delta|)\|\rho^{-\delta}u\|_{\mathcal E_0} .$$
So $M_\delta:w\mapsto\rho^\delta w$ is an isomorphism $\mathcal E_0\to\mathcal E_\delta$ and an isometry $L^2\to L^2_\delta$, and $PM_\delta=M_\delta T_\delta$. *$P$ is an isomorphism at weight $\delta$ if and only if $T_\delta:\mathcal E_0\to L^2$ is one.* Also $T_\delta-T_{\delta'}=(\delta-\delta')\Xi_PB$ with $\|B\|_{\mathcal E_0\to L^2}\le1$. Boundedness, Theorem 1(1), follows from $|\sum J_m\partial_mu|\le2|\nabla u|$ pointwise and from (F4).

**Lemma 4.1 (Gårding-type estimate; any $\delta$).** There is $C_1$, depending only on $C_G$ and $c_Q$, such that for $w\in C^\infty_c$,
$$\|w\|_{\mathcal E_0}\le C_1(1+|\delta|)\big(\|T_\delta w\|+\|w/\rho\|\big).$$

*Proof.* We have $\|Pw\|\le\|T_\delta w\|+|\delta|\|w/\rho\|$. By (F1), $\|L_3w\|\le\|Lw\|\le\|Pw\|$, and for $P=D$ also $\|\partial_sw\|\le\|Dw\|$. Apply (F4) slice by slice in the tangential variables, which is legitimate because $L_3$ has no tangential derivatives:
$$\|w/y\|\le C_G^{1/2}(\|L_3w\|+\|w/\rho\|).$$
By the Clifford relations, $\|\sum_mJ_m\partial_mw\|=\|\nabla_{t,X}w\|$ on $C^\infty_c$. Hence $\|\nabla_{t,X}w\|\le\|Lw\|+c_Q\|w/y\|$. $\square$

**Lemma 4.2 (direct range).** For $|\delta|<\tfrac12$ and $w\in C^\infty_c$, $\|w/\rho\|\le(\tfrac12-|\delta|)^{-1}\|T_\delta w\|$.

*Proof.* Lemma 3.1 at $\delta=0$, applied slice by slice, gives $\|w/\rho\|\le2\|L_3w\|\le2\|Pw\|$ by (F1). Moreover $\|Pw\|\le\|T_\delta w\|+|\delta|\|w/\rho\|$. $\square$

**Lemma 4.3 (coupled range).** If $m_\delta>\sqrt d\,|\delta|$, then $\|w/\rho\|\le\big(m_\delta(m_\delta-\sqrt d|\delta|)\big)^{-1/2}\|T_\delta w\|$ for $w\in C^\infty_c$.

*Proof.* Take $P=L$ first, and write $T_\delta=K+L_3^{(\delta)}$ with $K=J_t\partial_t$ and $L_3^{(\delta)}=L_3+\delta B$. Then
$$\|T_\delta w\|^2=\|Kw\|^2+\|L_3^{(\delta)}w\|^2+2\langle Kw,L_3w\rangle+2\delta\langle Kw,Bw\rangle .$$
The third term vanishes. $K$ and $L_3$ are formally symmetric, and $KL_3+L_3K=(J_tL_3+L_3J_t)\partial_t=0$, because the coefficients of $L_3$ are $t$-independent and anticommute with $J_t$ (F1). By Cauchy–Schwarz the last term is bounded in absolute value by $2|\delta|ab$, where $a=\|\partial_tw\|$ and $b=\|w/\rho\|$. Lemma 3.1, applied slice by slice in $t$, gives $\|L_3^{(\delta)}w\|\ge m_\delta b$. With $m=m_\delta$, the identity
$$a^2-2|\delta|ab+m^2b^2=\big(1-\tfrac{|\delta|}m\big)(a^2+m^2b^2)+\tfrac{|\delta|}m(a-mb)^2$$
(Part 5) gives $\|T_\delta w\|^2\ge(1-|\delta|/m)m^2b^2$.

For $P=D$, write $T^L_\delta=L+\delta B$ for the 4D operator just treated. Since $\Xi$ is orthogonal, $\|T^D_\delta w\|=\|(\partial_s+T^L_\delta)w\|$, and
$$\|(\partial_s+T^L_\delta)w\|^2=\|\partial_sw\|^2+\|T^L_\delta w\|^2+2\delta\langle\partial_sw,Bw\rangle .$$
Here $2\langle\partial_sw,Lw\rangle=\int\partial_s\langle w,Lw\rangle=0$, because $L$ is symmetric and $s$-independent. Insert the 4D bound $\|T^L_\delta w\|^2\ge a_t^2+m^2b^2-2|\delta|a_tb$, with $a_t=\|\partial_tw\|$ and $a_s=\|\partial_sw\|$. This gives $\|T^D_\delta w\|^2\ge a^2+m^2b^2-2|\delta|(a_s+a_t)b$ with $a^2=a_s^2+a_t^2$. Since $a_s+a_t\le\sqrt2\,a$, the same identity with $\sqrt2|\delta|$ in place of $|\delta|$ concludes. $\square$

By (F3), Lemma 4.3 applies on $(-\tfrac34,\tfrac14)$ for $L$ and on $(-\tfrac3{2(1+\sqrt2)},\tfrac1{2(1+\sqrt2)})\ni-\tfrac12$ for $D$ (Part 5). Both intervals contain the self-dual weight $-\tfrac12$, which Lemma 4.2 misses.

**Lemma 4.4 (duality).** Let $P^\dagger$ be the formal adjoint of $P$. If $P^\dagger:\mathcal E_{\delta^*}\to L^2_{\delta^*}$ is surjective, then the knot Hardy constants satisfy $C_K^P(-1-\delta^*)\le C_K^{P^\dagger}(\delta^*)$. Moreover $C_K^{P^\dagger}=C_K^P$, and $P^\dagger$ is an isomorphism at a weight if and only if $P$ is.

*Proof.* For $P=L$ we have $L^\dagger=L$. For $P=D$, let $\mathcal V u(s,\cdot)=u(-s,\cdot)$. Since $\Xi=\Xi^{\sf T}=\Xi^{-1}$ is a constant diagonal sign matrix [R14, Thm. A],
$$D^\dagger=(-\partial_s+L)\Xi=\mathcal W D\mathcal W^{-1},\qquad \mathcal W=\mathcal V\Xi .$$
$\mathcal W$ is an isometry of every $\mathcal E^{(5)}_\delta$ and $L^2_\delta$, and this gives the last two claims.

Put $\delta=-1-\delta^*$ and let $u\in C^\infty_c$. The weighted spaces pair as $(L^2_{\delta+1})'=L^2_{-\delta-1}=L^2_{\delta^*}$ under the unweighted pairing, so
$$\|u\|_{L^2_{\delta+1}}=\sup\{\langle u,h\rangle:h\in C^\infty_c,\ \|h\|_{L^2_{\delta^*}}\le1\}.$$
Fix such $h$, choose $g\in\mathcal E_{\delta^*}$ with $P^\dagger g=h$, and take $g_n\in C^\infty_c$ with $g_n\to g$ in $\mathcal E_{\delta^*}$. Then $\langle u,P^\dagger g_n\rangle=\langle Pu,g_n\rangle$. As $n\to\infty$:
- $P^\dagger g_n\to h$ in $L^2_{\delta^*}=(L^2_{\delta+1})'$;
- $g_n\to g$ in $L^2_{\delta^*+1}=L^2_{-\delta}=(L^2_\delta)'$.

Hence
$$|\langle u,h\rangle|=|\langle Pu,g\rangle|\le\|Pu\|_{L^2_\delta}\,\|\rho^{-\delta^*-1}g\|\le\|Pu\|_{L^2_\delta}\,C_K^{P^\dagger}(\delta^*)\,\|h\|_{L^2_{\delta^*}},$$
which is the claim. $\square$

## 5. Proof of Theorem 1

**Lemma 5.1 (continuity principle).** Let $\Lambda\subset\mathbb R$ be an open interval, and let $T_\delta=T_0+\delta\mathcal B$ with $\mathcal B\in B(\mathcal X,\mathcal Y)$ between Banach spaces. Assume:
- $\|x\|\le c(\delta)\|T_\delta x\|$ for $\delta\in\Lambda$, with $c$ locally bounded;
- $T_{\delta_0}$ is onto for some $\delta_0\in\Lambda$.

Then $T_\delta$ is an isomorphism for every $\delta\in\Lambda$.

*Proof.* Let $G\subset\Lambda$ be the set of $\delta$ at which $T_\delta$ is onto, hence an isomorphism with $\|T_\delta^{-1}\|\le c(\delta)$.
- *$G$ is open.* If $\delta\in G$ and $|\delta'-\delta|\,\|\mathcal B\|c(\delta)<1$, then $T_{\delta'}=T_\delta(1+(\delta'-\delta)T_\delta^{-1}\mathcal B)$ is invertible.
- *$G$ is closed in $\Lambda$.* If $\delta_n\in G$ and $\delta_n\to\delta\in\Lambda$, let $c'$ bound $c$ near $\delta$. Once $|\delta_n-\delta|\|\mathcal B\|c'<1$, the same argument starting from $\delta_n$ gives $\delta\in G$.

$\Lambda$ is connected and $G$ is non-empty, so $G=\Lambda$. $\square$

*Proof of Theorem 1(2).*
- *Stage 1.* Let $\Lambda_1=(-\tfrac12,\tfrac12)\cup\{m_\delta>\sqrt d|\delta|\}$. This is $(-\tfrac34,\tfrac12)$ for $L$ and an open interval containing $[-\tfrac12,0]$ for $D$ (Part 5). On $\Lambda_1$, Lemmas 4.1–4.3 give locally bounded constants $c(\delta)$ with $\|w\|_{\mathcal E_0}\le c(\delta)\|T_\delta w\|$ on $C^\infty_c$, hence on $\mathcal E_0$ by density. By (F5), $T_0$ is onto. Lemma 5.1 gives isomorphisms on $\Lambda_1$.
- *Stage 2.* Let $\delta\in(-\tfrac32,-\tfrac12)$. Then $\delta^*=-1-\delta\in(-\tfrac12,\tfrac12)\subset\Lambda_1$. By Stage 1 and Lemma 4.4, $P^\dagger$ is onto at $\delta^*$, and Lemma 4.4 gives $C_K(\delta)\le C_K(\delta^*)\le(\tfrac12-|\delta^*|)^{-1}$. Together with Lemma 4.1, this is a locally bounded lower bound on $(-\tfrac32,-\tfrac12)$. Hence $c$ is locally bounded on all of $(-\tfrac32,\tfrac12)$, which is the union of $(-\tfrac32,-\tfrac12)$ and $\Lambda_1$ (Part 5). Lemma 5.1 on $\Lambda=(-\tfrac32,\tfrac12)$ finishes the proof. $\square$

*Proof of Theorem 1(4).* On the window both $P$ and $P^\dagger$ are onto. So Lemma 4.4 applies in both directions, and $C_K(\delta)=C_K(-1-\delta)$. The upper bounds are Lemmas 4.2 and 4.3, extended to the domain by density.

For the lower bound $1/m_\delta$, take the quasimodes of the optimality part of Lemma 3.1 and multiply by $\chi(t/T)$ (and by $\chi(s/T)$ for $D$). The tangential derivatives contribute
$$\frac{\|\chi_T'\|}{\|\chi_T\|}\cdot\frac{\|\rho^{1/2}g_N\|_{L^2(d\rho)}}{\|\rho^{-1/2}g_N\|_{L^2(d\rho)}}=O(T^{-1})\quad\text{at fixed }N.$$
The cross term with $\delta B$ is bounded by the same quantity. Let $T\to\infty$, then $N\to\infty$, then $\epsilon\to0$. $\square$

*Proof of Theorem 1(3).* Let $m_\delta=0$. The construction just described gives $w_n\in C^\infty_c$ with $\|T_\delta w_n\|\le n^{-1}\|w_n/\rho\|\le n^{-1}\|w_n\|_{\mathcal E_0}$. Since $T_\delta$ commutes with tangential translations, we may translate the $w_n$ in $t$ so that their supports are disjoint. The inner product of $\mathcal E_0$ is local, so the normalised $w_n$ are orthonormal.

Suppose $T_\delta$ were left semi-Fredholm, and let $\Pi$ be the finite-rank projection onto $\ker T_\delta$. Then $\|x-\Pi x\|\le C\|T_\delta x\|$, and $\Pi w_n\to0$. This gives $1\le C\|T_\delta w_n\|+\|\Pi w_n\|\to0$, a contradiction. By (F3), $m_{-3/2}=|1-1|=0$ and $m_{1/2}=|-1+1|=0$. $\square$

**Remark 5.2 (what the two halves of the window use).**
- On $(-\tfrac12,\tfrac12)$ the proof is a Neumann series from $\delta=0$, powered by the sharp constant $2$.
- On $(-\tfrac34,\tfrac14)$, which contains the self-dual weight $-\tfrac12$, it is the coupled estimate. That estimate uses the exact cone lemma on translation-invariant slices and the anticommutation of $J_t$ with $L_3$ and with $J_\rho$.
- On $(-\tfrac32,-\tfrac12)$ it is duality.

No regularity theory at the knot is used beyond (F4) and (F5).

**Remark 5.3 (outside the window; not claimed).** Proposition 2 shows that on translation-invariant fields the lower bound persists off the discrete set $-\tfrac12-{\rm spec}\,\bar S$. For the full operator we expect something different once $\delta$ crosses $\tfrac12$ or $-\tfrac32$. Each nonzero tangential frequency $\tau$ sees a massive operator $L_3+i\tau J_t$ at infinity, whose index should jump by $\dim\ker(\bar S\pm1)$ ($\ge2$; numerically $=2$ [R18, §7]). Integrated over $\tau$, this would make $P$ non-Fredholm, with infinite-dimensional kernel or cokernel. We prove none of this.

**Remark 5.4 ($S^1_t$).** On $S^1_t\times\mathbb R^3_+$, the geometry of [T] and of math_19 [R19, (A1)], everything above holds verbatim, because (F1)–(F5) are stated there too. Only the quasimodes of Theorem 1(3)–(4) change:
- the $t$-cut-off is replaced by the constant function, since $t$-independent fields are square integrable on $S^1_t$;
- disjoint supports are obtained by dilation instead of $t$-translation. Dilation preserves the ratio $\|T_\delta w\|/\|w/\rho\|$ by homogeneity.

## 6. Proof of Proposition 2

The inequality and its optimality are Lemma 3.1. The quasimodes there are $t$-independent and need no tangential cut-off. Lemma 4.1 holds on $\mathbb R^3_+$ with $L_3$ in place of $P$. So $L_3$ is bounded below on $\mathcal E_\delta(\mathbb R^3_+)$ for every $\delta$ with $m_\delta>0$, with knot Hardy constant $m_\delta^{-1}$.

*Surjectivity at $\delta=0$.* Let $f\in L^2(\mathbb R^3_+)$ and regard it as a $t$-independent element of $L^2(S^1_t\times\mathbb R^3_+)$. By (F5) on $S^1_t$, there is a unique $U\in\mathcal E_0(S^1_t\times\mathbb R^3_+)$ with $LU=f$. Translations in $t$ commute with $L$ and fix $f$, so by uniqueness $U$ is $t$-independent. Write $U(t,X)=u(X)$. Averaging approximants over $t$ shows $u\in\mathcal E_0(\mathbb R^3_+)$, and $L_3u=f$.

Lemma 5.1 on $(-\tfrac32,\tfrac12)$, with $\mathcal B=B$, gives the isomorphism. $\square$

## 7. Proof of Proposition 3

**(1).** $t$-independence and dilation invariance are checked exactly (Part 1). The rotation statement is [H23, Prop. 4(3)] at $k=1$: $R_\alpha^*x_W={\rm Ad}(\exp(-2\alpha t_3))\,x_W$. Its linear form, $[\mathcal J,L]=0$ with $R$ antisymmetric, is (F7) (Part 8).

An exact symmetry of $x_W$ gives an element of $\ker P$ only through its infinitesimal generator:
- $\partial_tx_W=0$;
- $\tfrac{d}{d\lambda}\lambda x_W(\lambda\cdot)=0$;
- the rotation generator is the infinitesimal gauge transformation by the constant element $-2t_3$. This violates the Coulomb row, because $-\sum_j{\rm ad}(\phi_j)^2$ is positive definite (Part 9). In any case it is homogeneous, so it lies in no $\mathcal E_\delta$.

The scaling of the norms under $D_\lambda$ is a change of variables.

**(2).** $u_j\in\ker L$ is (F6); $u'_j\in\ker L$ follows from $J_\rho\bar SJ_\rho^{-1}=-\bar S$ (F2) and the cone form. Both are re-verified exactly at rational points (Part 7), together with:
- homogeneity of degrees $-2$ and $0$;
- linear independence;
- linear vanishing at the face;
- the negative control that the plain derivative $\partial_2x_W$ violates the Coulomb row.

In the cone frame, $\rho^{-1-s}\varphi\in\ker L_3$ if and only if $\bar S\varphi=s\varphi$, so the eigenvalues are $s=+1$ (degree $-2$) and $s=-1$ (degree $0$). Homogeneous fields lie in no $\mathcal E_\delta$ (§1.1).

**(3).** At $\delta=-\tfrac32$, the field $w=\rho^{3/2}\chi\gamma u_j$ equals $\chi\,U^{-1}(\rho^{1/2}\gamma(N^{-1}\log\rho)\varphi_j)$, with $\bar S\varphi_j=\varphi_j$ and $c=s+\delta=-\tfrac12$. The proof of Theorem 1(3) applies with $\epsilon=0$, since $\varphi_j$ is an exact eigenvector. At $\delta=\tfrac12$ the same holds with $J_\rho\varphi_j$ and $u'_j$.

These $u$ lie in $\mathcal E_\delta$. The angular parts $\varphi_j$ are smooth on the closed hemisphere and vanish linearly at the equator [R16, proof of Prop. 5.4(4)], and so are the $J_\rho\varphi_j$, since $J_\rho$ is smooth there. Part 7 checks this behaviour exactly at one face point. So each $u$ is smooth on $\bar W\setminus\ell$, compactly supported away from $\ell$, and $O(y)$ with bounded gradient near the face. Cutting off by $1-\eta(y/\varepsilon)$ and mollifying then converges in $\mathcal E_\delta$, since $|u|\le Cy$ on $\{y<2\varepsilon\}$. $\square$

## 8. Nonlinear consequences

*Proof of Corollary 4.*

**(1).** The KW equations and the Coulomb condition relative to $x_W$ are polynomial of degree $2$ in the fields. The Coulomb condition is linear in the perturbation. So $\mathfrak F(u)=Lu+\mathfrak B(u,u)$. The quadratic part is the second variation, which is the same at $x_W$ as at $0$ and therefore has constant coefficients; there are no cubic terms (Part 10). Hence $|\mathfrak B(u,v)|\le c_B|u||v|$ pointwise. Extending $u\in C^\infty_c(W^\circ)$ by zero to $\mathbb R^4$ and applying (F8) gives $\|u\|_{L^4}\le C_S\|\nabla u\|\le C_S\|u\|_{\mathcal E_0}$. So $\|\mathfrak B(u,v)\|_{L^2}\le c_BC_S^2\|u\|_{\mathcal E_0}\|v\|_{\mathcal E_0}$, and $\mathfrak F$ is a bounded quadratic polynomial $\mathcal E_0\to L^2$.

**(2).** Let $C_0=\|L^{-1}\|_{L^2\to\mathcal E_0}$, which is finite by Theorem 1 at $\delta=0$. If $\mathfrak F(u)=0$, then
$$\|u\|_{\mathcal E_0}\le C_0\|\mathfrak B(u,u)\|\le C_0c_BC_S^2\|u\|_{\mathcal E_0}^2 ,$$
so $u=0$ whenever $\|u\|_{\mathcal E_0}<\varepsilon_0:=(C_0c_BC_S^2)^{-1}$.

**(3).** This is the inverse function theorem, since $d\mathfrak F(0)=L$ is an isomorphism. $\square$

*Remark.* In five dimensions $\mathcal E^{(5)}_0\subset L^{10/3}$ only, so $|u|^2\notin L^2$ in general (Part 11). We claim no 5D analogue of Corollary 4.

**Hypotheses for Corollary 5.** These are hypotheses, not results.
- **(S) Slice.** There are $\varepsilon_S,C'>0$ with the following properties. Let $x$ be a KW solution with $G=SO(3)$, Nahm pole and weight-one knot along $\ell$, and let $g$ be a gauge transformation with $\|g\cdot x-x_W\|_{\mathcal E_0}<\varepsilon_S$, the difference read as an 8-slot field via $P$. Then there is $g'$ with $g'\cdot x=x_W+Pu$, $S(Pu)=0$ and $\|u\|_{\mathcal E_0}\le C'\|g\cdot x-x_W\|_{\mathcal E_0}$. Moreover, two Coulomb representatives in this ball that are gauge equivalent coincide.
- **(F) Floer package.** For the long unknot with these data:
  - (F$_a$) the HW chain complex is $\mathbb Z$-graded and generated by the gauge classes of KW solutions whose gauge-fixed linearisation is an isomorphism $\mathcal E_0\to L^2$;
  - (F$_b$) moduli spaces of finite-energy HW trajectories between generators are compact up to breaking;
  - (F$_c$) after a small admissible perturbation of the HW equations, these moduli spaces are cut out transversally, with dimension given by the index of the linearised HW operator. The perturbation displaces each non-degenerate generator by a unique small amount, as in Corollary 4(3). The differential counts index-one trajectories.
- **(Cl) Classification.** Every KW solution in the class used in (F) is gauge equivalent to $x_W$. This is known only within subclasses:
  - the abelian class at bounded distance from $v_W$ [H23, Thm. 1];
  - Dimakis's class of $x_1$-invariant solutions with nilpotent Higgs field and model asymptotics [D, Thm. 1.3], for which [H23, §1.3] reads the data as $P=z$, $R=1$, $Q=0$.

*Proof of Corollary 5.*

**(1).** By (S), a class close to $[x_W]$ has a Coulomb representative $x_W+Pu$ with $\|u\|_{\mathcal E_0}$ small, and Corollary 4(2) gives $u=0$.

The stabiliser of $x_W$ is trivial for the following reason. At a point with $r>0$, $-\sum_j{\rm ad}(\phi_j)^2$ is positive definite (Part 9), so $\phi_t,\phi_2,\phi_3$ span $\mathfrak{su}(2)\cong\mathbb R^3$. An element of $SO(3)$ fixing a spanning set is the identity.

**(2).** Non-degeneracy is Theorem 1 at $\delta=0$. Kernel and cokernel are zero, so the determinant line is canonically $\mathbb R$. Persistence is Corollary 4(3) together with (F$_c$).

**(3).** Under (Cl) the complex has one generator. A $\mathbb Z$-graded differential on a complex concentrated in one degree vanishes. $\square$

*Remark.* Corollary 5(3) is consistent with $\widetilde{Kh}(U)=\mathbb Z$. That consistency is not evidence for (F) or (Cl).

## 9. Sectors, and what remains

**Which sector sets the window.** By (F3) and [R18, Thm. A, Cor. A′, Cor. B′], the eigenvalues of $\bar S$ nearest to $0$ come from different sectors:
- $\pm1$ lie in the exceptional rank-12 bundle $E_0$ (no Type I component) and carry $U(1)$-weights $\pm1$. These are the translations and their reflections.
- The rest of the spectrum lies in $|s|\ge\lambda_4^+$. The threshold $\lambda_4^+$ is the Type I value attached to the Cartan ground state $\gamma_0=4$ of [R8], and the Rayleigh–Ritz values of [R18, §7] (numerical, not used) indicate that it is attained.

If the eigenvalues $\pm1$ were absent, the window would be the wider interval $-\tfrac12-(-\lambda_4^+,\lambda_4^+)=(-\tfrac{\sqrt{17}}2,\tfrac{\sqrt{17}-2}2)\approx(-2.06,1.06)$. This mirrors the wide Cartan window of the scalar sector [R12, Thm. 4]. *The full non-abelian window is cut down to $(-\tfrac32,\tfrac12)$ exactly by the exceptional sector, that is, by the infinitesimal motions of the knot.* This is the precise sense in which the scalar, Cartan, analysis of [R12, H23] does not suffice. It also explains why the result needs the exceptional-sector analysis of [R18].

**What remains.**
1. *Other weights $k\ge2$.* The proof uses only (F1)–(F5) and the location of ${\rm spec}\,\bar S$ near $\pm\tfrac12$. For $k\ge2$, the Mazzeo–Witten list [MW2, Prop. 4.3] predicts that the root-free knot interval is again $(-2,0)$. But neither the spectral identification of [R18] nor the energy isomorphism (F5) is available. Taubes's [T, Thm. II.1] covers $\delta=0$ for all $m$ on $S^1_t$, modulo the convention question of [R18, §8]. If that were settled, Stages 1–2 would transfer once ${\rm spec}\,\bar S_k\cap(-1,1)=\emptyset$ is known.
2. *Face weights.* We fix the energy normalisation at the face. The face window $(-1,1)$ [R14, Prop. 4.1] presumably allows $y^\epsilon$-weights as well. The analogous conjugation produces $\epsilon J_y/y$, and the available face constant (F4) is not explicit.
3. *Outside the window* (Remark 5.3).
4. *Compact unknot, (S), (F), (Cl), and a 5D nonlinear theory.* None of these is attempted.

## 10. Status of claims

**Proved here, given (F1)–(F8):**
- Lemma 3.1;
- Lemmas 4.1–4.4 and 5.1;
- Theorem 1, Propositions 2–3 and Corollary 4.

**Imported:** (F1)–(F7) from [R14, R16, R18], and the rotation formula from the companion preprint [H23]. Witten's solution and its identification are re-verified.

**Conditional:** Corollary 5, on (S), (F) and, for item 3, (Cl).

**Not claimed:**
- anything for $k\ne1$, for face weights, or outside the window;
- the coincidence of our spaces with those of [MW2, §9];
- compactness, gluing, slice theorems, or a construction of HW Floer theory;
- any statement about compact knots.

**Novelty** (stated narrowly): the half-window $\delta\in(-\tfrac32,-\tfrac12]$ (rates $(-2,-1]$), sharpness at both endpoints, the 5D weighted statement, and the explicit, symmetric knot Hardy constants. The $\delta=0$ case is [T, Thm. II.1] (on $S^1$) and [R16, R18]. The range $(-\tfrac12,\tfrac12)$ is close to [MW2, Prop. 9.2].

## 11. Verification

`verify.py` (sympy; about seven minutes) runs 61 exact checks and ends with `FALLOS = 0`. The output is in `verify_output.txt`. It checks:
- **Part 1:** the two presentations of $x_W$, the KW equations (with a negative control), dilation invariance and $t$-independence;
- **Part 2:** the Clifford system; symmetry of $Q$; $\{Q,J_t\}=\{Q,J_\rho\}=\{J_\rho,J_t\}=0$; homogeneity; and the three bounds behind $c_Q<\infty$;
- **Part 3:** the conjugation identity $[L,\rho^\delta]=\delta\rho^{\delta-1}J_\rho$ for symbolic $\delta$;
- **Part 4:** the Mellin substitution for a general function, the Plancherel identity, the scalar Hardy identity for symbolic $c$, and the sharpness family;
- **Part 5:** $m_\delta$ on a rational grid; the coupled regions solved exactly; the coverage of the window by the two stages; the duality symmetry; the quadratic-form identity; the constants;
- **Part 6:** the rate bookkeeping and the Mazzeo–Witten dictionary;
- **Part 7:** $u_j,u'_j\in\ker L_3$ exactly at rational points, their degrees, independence, face behaviour, and the negative control;
- **Part 8:** $[\mathcal J,L]=0$;
- **Part 9:** positivity of $-\sum{\rm ad}(\phi_j)^2$;
- **Part 10:** the quadratic part of KW is background-independent, and there are no cubic terms;
- **Part 11:** the Weyl-sequence ratios and the Sobolev exponents.

The verifier does not check the functional analysis (Lemmas 3.1–5.1), or the imported (F2)–(F5), whose proofs are in [R16, R18]. `verify.mpl` mirrors the exact scalar parts (Parts 1, 3–6, 10–11) under the Maple rules. It has not been executed, because Maple is not available.

## References

- [D] P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: Nilpotent Higgs field*, arXiv:2209.11101 (Def. 1.1, Def. 1.2, Thm. 1.3, Thm. 4.5).
- [HM] S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019); arXiv:1710.10645 (§6).
- [MW1] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014); arXiv:1311.3167.
- [MW2] R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Math. Phys. (2020); arXiv:1712.00835 (§2, (2.8)–(2.11), (3.2), Prop. 4.2, Prop. 4.3, Prop. 6.1, §9.2.2 (9.7), §9.2.3 (9.9) and Prop. 9.2, Prop. 9.3).
- [T] C. H. Taubes, *Lectures on the linearized Kapustin–Witten equations on $(0,\infty)\times Y$*, arXiv:2008.09538 (Part II: Thm. II.1, Lemma II.5.1).
- [W] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
- [R8] *The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one*, rStation math_8 v1, https://rstation.ai/problems/math/papers/8/v1 (§2.1, Thm. 3).
- [R12] *The zeroth-order operator in a scalar model of Bleher's continuity method at weight one*, rStation math_12 v1, https://rstation.ai/problems/math/papers/12/v1 (Thm. 4).
- [R14] *The linearized Haydys–Witten operator at the Kapustin–Witten knot: a formally symmetric splitting, five-dimensional indicial data, and the absence of a spectral gap*, rStation math_14 v1, https://rstation.ai/problems/math/papers/14/v1 (§2, Thm. A, Cor. A.1, Cor. A.2, Prop. 4.1, Prop. 4.3, §4).
- [R16] *Essential self-adjointness of the Haydys–Witten cross-section operator at the Nahm pole, and a cone reduction at the weight-one knot*, rStation math_16 v1, https://rstation.ai/problems/math/papers/16/v1 (Lemma 2.1, Props. 5.1, 5.4, Lemma 5.3, Lemma 6.1, Thms. 3, 4).
- [R18] *The weight-one knot-link operator has no spectrum in $(-1,1)$*, rStation math_18 v1, https://rstation.ai/problems/math/papers/18/v1 (Main Theorem, Corollary, Thm. A, Cor. A′, Lemma 4.1, Cor. B′, §§7–8).
- [R19] *Hyperbolic cutoffs and a Fredholm theory for the linearized Haydys–Witten operator along non-constant trajectories in the energy space*, rStation math_19 v1, https://rstation.ai/problems/math/papers/19/v1 ((A1)).
- [H23] *A one-sided comparison theorem for Witten's knot solution of the Kapustin–Witten equations, with remarks on the long unknot*, companion preprint, under review (Def. 1.1, Thm. 1, Prop. 3, Prop. 4(3), §1.3).

# The Hopf link in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and its realization

**Abstract.**

Physical arguments of Witten and Gaiotto–Witten reduce the Kapustin–Witten/Haydys–Witten (HW) theory of a link to Lagrangian Floer theory in a finite-dimensional space of Seidel–Smith type. This reduction is unproved; we state it as Hypothesis (Ad), and our theorems concern the model. We work in the local fibred model of Seidel–Smith for the two-strand braids $s_1^{\pm2}$: an $A_2$-fibration over $T^*S^2$, with Lagrangians fibred over the zero section $K\cong S^2$.
(A) The Lagrangians meet cleanly in two sections $C_0\sqcup C_1\cong S^2\sqcup S^2$.
(B) A parity argument gives $HF(L,L';\mathbb Z)\cong\mathbb Z^4$ in degrees $0,2,2,4$: a direct geometric derivation of the known integral agreement $Kh_{\rm symp}\cong Kh$ for this quasi-alternating link (Hendricks–Mak–Raghunath, via Abouzaid–Smith). A bookkeeping bigrading (fibre degree, base Morse degree) labels the generators by $Kh(\mathrm{Hopf}^+)=\mathbb Z_{(0,0)}\oplus\mathbb Z_{(0,2)}\oplus\mathbb Z_{(2,4)}\oplus\mathbb Z_{(2,6)}$; the geometry does not respect it.
(C) Main result: for the integrable complex structure every Floer strip is vertical, and each fibre carries exactly two circles of strips, given in closed form and all regular. The unperturbed Morse–Bott correspondence is the closed circle bundle $E\cong\mathbb{RP}^3\sqcup\mathbb{RP}^3\to K$. After Morse perturbation, nonempty cascade spaces join generators of different $q$.
(D) For prescribed $SO(3)$-equivariant bundles, we define the realization explicitly as the cofibre of a twisted transfer along $E\to K$. The local pieces split, and symmetric framings kill all $\eta$-maps, leaving $(S^0\cup_\theta e^4)\vee S^2\vee S^2$ with $\theta\in2\pi_3^s$. Framings with $\theta=0$ give the collapsed Lipshitz–Sarkar spectrum. Identifying this with the Floer-theoretic realization is an explicit Hypothesis (R); the canonical framing is not identified.
If the HW $q$-grading is a topological charge, (Ad) cannot be an isomorphism of flow categories. If moreover the HW category has exactly four objects with these labels, (Ad) predicts $\theta=0$. verify.py: 69 checks, FALLOS = 0.

## 1. Introduction and results

### 1.1 Background

Witten proposed that Khovanov homology arises as the Floer homology of the Haydys–Witten (HW) equations on $\mathbb R_s\times\mathbb R^3\times\mathbb R_+$, with a Nahm pole at $y=0$ and singularities along the link [1, 3, 4]. The $q$-grading is the instanton number $P$, and Witten notes that the differential commutes with $P$ [1, §1.2]. Gaiotto–Witten [2, §4] describe an adiabatic regime in which the strands move slowly. There the five-dimensional problem becomes a Morse/Floer problem on a finite-dimensional space of time-independent solutions, and the $q$-grading comes from a covering on which a multivalued superpotential becomes single-valued [2, §4.1.4]. Seidel–Smith [6] defined *symplectic Khovanov cohomology* $Kh_{\rm symp}$ as Lagrangian Floer cohomology in a space $\mathcal Y_m$ cut out of a nilpotent slice in $\mathfrak{sl}_{2m}$; Manolescu [7, 8] identified $\mathcal Y_m$ with an open subset of a Hilbert scheme. Abouzaid–Smith [9, (1.1)] proved $Kh^k_{\rm symp}\otimes\mathbb F\cong\bigoplus_{i-j=k}Kh^{i,j}\otimes\mathbb F$ for every field $\mathbb F$ of characteristic $0$. Cheng [10, Thms. 1.3, 1.5] added a relative second grading over such fields; Hendricks–Mak–Raghunath [22] stress that $Kh_{\rm symp}$ itself is singly graded. Bleher [5, Conj. B] formulates the identification of HW Floer homology with symplectic Khovanov homology as a conjecture, building on the adiabatic picture.

On the homotopy side, Lipshitz–Sarkar [16] constructed a Khovanov spectrum $\mathcal X_{Kh}(L)=\bigvee_q\mathcal X^q_{Kh}(L)$ with $\widetilde H^i(\mathcal X^q)=Kh^{i,q}$ [16, Thm. 1]. For the Hopf link they computed $\mathcal X_{Kh}=S^0_0\vee S^0_2\vee S^2_4\vee S^2_6$, subscripts being $q$ [16, §9.2]. Their construction was motivated by Floer theory, but "direct connections with symplectic geometry ... remain unknown" [21, §4]. Even the comparison of torsion in $Kh_{\rm symp}$ and $Kh$ is open in general [21, §2.3]. We know of no work that compares the Lipshitz–Sarkar spectrum with a Floer homotopy type built from Seidel–Smith Lagrangians, for any link other than unlinks.

Earlier papers in this line studied HW without a link on $\mathbb R\times S^3\times(0,L)$. There they built local flow categories, framed models and compactness near the Anderson–Henningson fold [M24, M25, M30–M33]. Earlier work on knots studied Bleher's finite-dimensional model [M13] and HW trajectories between Kapustin–Witten (KW) knot solutions [M22]. This paper takes the first link case. It works entirely in the finite-dimensional adiabatic model and states the passage to HW as a hypothesis.

### 1.2 The adiabatic hypothesis

Let $\kappa^\pm$ be the positive/negative Hopf link. In the conventions of [6], where $s_1^3$ closes to the left-handed trefoil [6, §6(C)], $\kappa^-$ is the closure of $s_1^{2}\in Br_2$ and $\kappa^+$ that of $s_1^{-2}$. Here $m=2$, and the writhe is $w=\mp2$, so $m+w=0$ for $\kappa^-$ and $m+w=4$ for $\kappa^+$.

**Hypothesis (Ad) (adiabatic correspondence for the Hopf link).** Take the $SU(2)$ HW equations on $\mathbb R_s\times\mathbb R^3\times\mathbb R_+$ with Nahm pole and singularities along $\kappa$, in the adiabatic regime of [2, §4]. Then:
* **(Ad$_0$)** the HW Floer cohomology is defined, and it is isomorphic, as a $\mathbb Z$-graded abelian group in the grading $h-q$, to $HF^{*+m+w}(L,L')$ of the model $(\mathbb M)$ of §1.3;
* **(Ad$_{\rm fr}$)** the HW framed flow category is defined, and its realization is equivalent to $R(\varphi)$ (Definition 6.1) for some prescribed $SO(3)$-equivariant bundles and some framing $\varphi$ of the model correspondence.

The supporting arguments are physical [1, 2]. The analytic step from slow motion to the finite-dimensional model is an open problem; see [5, §7]. We do not use (Ad) in any proof except that of Corollary E.

**Hypothesis (P) (instanton number).** The instanton number is locally constant on the space of HW configurations with the fixed boundary and link data. Hence finite-energy HW trajectories join only KW solutions with equal $q$.

(P) is the flow-category form of $[P,Q]=0$ [1, §1.2]. We use it only in Corollary E(3).

### 1.3 The model $(\mathbb M)$

This is the local model of [6, §6(C)], which Seidel–Smith use to compute the trefoil. We use it with $s_1^{\pm2}$ in place of $s_1^3$. Seidel–Smith reduce the computation of $Kh_{\rm symp}$ for closures of $s_1^k$ to this model; their reduction "parallels the Markov II argument and is omitted" [6, §6(C)]. We import that reduction, and our theorems are statements about the model.
* **Base.** The base is the quadric $X=\{u^2+v^2+w^2=z\}\subset\mathbb C^3$, with $z>0$. It contains the Lagrangian sphere $K=\sqrt z\,S^2=X\cap\mathbb R^3$. $X$ carries the line bundle $F\to X$, the eigenline bundle of $u\sigma_1+v\sigma_2+w\sigma_3$, which restricts to $K\cong\mathbb{CP}^1$ with degree $\pm1$.
* **Total space.** $Y\subset\mathbb C\oplus F^{-2}\oplus F^{2}$, with fibre coordinates $(a,b,c)$, is cut out by $bc=p(a)$, where $p$ is a cubic with three distinct roots $q_0,q_1,q_2$ (in [6]: $a^3-ad+bc=\zeta^-_d+\epsilon$). Each fibre $Y_x$ is the $A_2$ surface $S=\{bc=p(a)\}$. $SU(2)$ acts on $X$ through $SO(3)$ and on $F$ through the spin representation. It acts on $Y$ through $SO(3)$, preserving the complex structure and the $SU(2)$-invariant hermitian metric on $F$. The map $Y\to X$ is holomorphic.
* **Lagrangians.** For an embedded path $\gamma$ in the $a$-plane from $q_i$ to $q_j$ that avoids the third root, let $\Lambda_\gamma\subset S$ be the matching sphere $\{a\in\gamma,\ |b|=|c|\}$ [11]. Then
$$L=\bigcup_{x\in K}\Lambda_\alpha(x),\qquad L'=\bigcup_{x\in K}\Lambda_{\alpha'}(x),\qquad\alpha'=t^{2\epsilon}(\alpha),\quad\epsilon=\pm1.$$
  Here $\alpha$ is a path from $q_0$ to $q_1$, and $t$ is the half twist exchanging $q_1$ and $q_2$; in [6, Fig. 9] the trefoil uses $t^3$. Both $L$ and $L'$ are $SO(3)$-invariant and are $S^2$-bundles over $K$.

$\mathbb M$ denotes $(Y,L,L')$ with the integrable complex structure $J$. Write $U(1)\subset SU(2)$ for the stabilizer of a point of $K$. It acts on the fibre over that point by $(b,c)\mapsto(\lambda^{-2}b,\lambda^{2}c)$, which factors through the effective circle action $(b,c)\mapsto(\mu b,\mu^{-1}c)$, $\mu\in SO(2)$. This circle action preserves $bc$ and $|b|^2-|c|^2$, hence every $\Lambda_\gamma$.

### 1.4 Results

Write $x_0,x_1$ for the critical points $(q_0,0,0)$, $(q_1,0,0)$ of a fibre. Gradings follow [6, §6(A)]: $L$ and $L'$ carry gradings, and $Kh^k_{\rm symp}=HF^{k+m+w}(L,L')$.

**Theorem A (clean intersection).** $L\cap L'=C_0\sqcup C_1$, where $C_j=\{x_j(x):x\in K\}$ is a section of $Y|_K\to K$, so $C_j\cong S^2$. The intersection is clean.

**Theorem B (Floer cohomology over $\mathbb Z$ and the bigrading).**
1. The Morse–Bott spectral sequence of [13] degenerates, and
$$HF^*(L,L';\mathbb Z)\ \cong\ H^{*-s_{\rm lo}}(S^2;\mathbb Z)\oplus H^{*-s_{\rm hi}}(S^2;\mathbb Z),\qquad\{s_{\rm lo},s_{\rm hi}\}=\{0,2\}.$$
   This group is free of rank 4, in degrees $0,2,2,4$. The relative shift $s_{\rm hi}-s_{\rm lo}=2$ equals the relative Seidel index of the two fibre generators (Lemma 4.1). Here $C_{\rm hi}$ and $C_{\rm lo}$ denote the components $C_j$ with shift $s_{\rm hi}$, $s_{\rm lo}$.
2. Consequently, over $\mathbb Z$,
$$Kh^k_{\rm symp}(\kappa^\pm;\mathbb Z)\ \cong\ \bigoplus_{i-j=k}Kh^{i,j}(\kappa^\pm;\mathbb Z).$$
3. *(Bigrading.)* Perturb by a height function on $K$. Each generator is then a pair (component $C_j$, critical point of Morse index $\mu\in\{0,2\}$), and its Floer degree is $s_j+\mu$. Put
$$h=\tfrac{m+w}2-s_j,\qquad q=\tfrac{3(m+w)}2-2s_j-\mu .$$
   Then $h-q=(s_j+\mu)-(m+w)$, and the four labels are exactly $(0,0),(0,2),(2,4),(2,6)$ for $\kappa^+$ and their negatives for $\kappa^-$. The fibre point fixes $h$. The base sphere contributes the factor $V=\mathbb Z_{q=+1}\oplus\mathbb Z_{q=-1}$ (verify.py §0: $Kh(\kappa^+)=\widetilde{Kh}(\kappa^+)\otimes V$).

**Theorem C (the Floer flow category).**
1. *(Verticality.)* Every finite-energy $J$-holomorphic strip with boundary on $L,L'$ lies in a single fibre $Y_x$, $x\in K$.
2. *(Classification in a fibre.)* In $S$ the strips with ends at $x_0,x_1$ are, up to translation, exactly two circles, the free orbits of the effective circle action. They are given in closed form through the Riemann map of the bigon (Proposition 5.2). In the disc model ($q_0=-1$, $q_1=1$, $q_2=0$, $\alpha$ the lower and $\alpha'$ the upper semicircle, $p(a)=a(a^2-1)$), they are
$$u_c^\vartheta(a)=\big(a,\ e^{i\vartheta}\sqrt{a^2-1},\ e^{-i\vartheta}a\sqrt{a^2-1}\big),\qquad u_b^\vartheta(a)=\big(a,\ e^{i\vartheta}a\sqrt{a^2-1},\ e^{-i\vartheta}\sqrt{a^2-1}\big),$$
   with $a$ the conformal parameter of the strip. There are no other nonconstant strips, and none in the opposite direction.
3. *(Regularity.)* Every such strip is regular. The kernel of the vertical linearization is spanned by translation and rotation, and the full operator in $Y$ is onto with kernel of dimension $4$.
4. *(The Morse–Bott correspondence.)* The space of unparametrized strips from $C_{\rm hi}$ to $C_{\rm lo}$ (the components with shifts $2,0$) is the closed $3$-manifold
$$E=E_b\sqcup E_c,\qquad E_b\cong E_c\cong S(F^{-2}|_K)\cong\mathbb{RP}^3,$$
   a circle bundle $p:E\to K$. Both evaluation maps equal $p$ under $C_{\rm hi}\cong K\cong C_{\rm lo}$. There are no nonconstant strips from $C_j$ to itself and none from $C_{\rm lo}$ to $C_{\rm hi}$. We call $(C_{\rm hi},C_{\rm lo},E,p,p)$ the *Morse–Bott correspondence* $\mathcal C_{\mathbb M}$. All later statements concern this unperturbed object. We do not construct the compactified Morse-perturbed (cascade) flow category.
5. *($q$ is not preserved.)* Perturb by a height function on $K$ with maximum $M$ and minimum $m_0$ on both copies. Then two kinds of nonempty cascade spaces appear, and each joins generators of different $q$ for the labels of Theorem B(3):
   * the unbroken cascades from $(C_{\rm hi},M)$ to $(C_{\rm lo},m_0)$ contain $p^{-1}(S^2\setminus\{M,m_0\})\ne\emptyset$;
   * each object sphere has its Morse trajectory space $\mathcal M((C_j,M),(C_j,m_0))\cong S^1$.

   For $\kappa^+$, $q\in\{0,2\}$ on $C_{\rm hi}$ and $q\in\{4,6\}$ on $C_{\rm lo}$. (The compactification of the first space has boundary strata through $(C_{\rm hi},m_0)$ and $(C_{\rm lo},M)$, products of a Morse circle with a fibre circle; we do not describe it.)

**Theorem D (framed correspondences and their realization).** Prescribe $SO(3)$-equivariant virtual bundles $V_{\rm hi},V_{\rm lo}$ over $K$ of ranks $2,0$; they play the role of the object index bundles, which we do not construct. Let a *framing* be a stable isomorphism $\varphi:p^*(V_{\rm hi}-\underline{\mathbb R})-T_pE\cong p^*V_{\rm lo}$, both sides of rank $0$. Let $R(\varphi)=\operatorname{Cofib}(\delta_\varphi)$, where $\delta_\varphi:\Sigma^{-1}\mathrm{Th}(V_{\rm hi})\to\mathrm{Th}(V_{\rm lo})$ is the twisted transfer along $p$ followed by $\varphi$ and push-forward (Definition 6.1).
1. *(Local pieces.)* $\mathrm{Th}(V_{\rm lo})\simeq S^0\vee S^2$ and $\Sigma^{-1}\mathrm{Th}(V_{\rm hi})\simeq S^1\vee S^3$, because every bundle over $K$ associated to $P=SO(3)\to S^2$ has even $c_1$ ($e(P)=2$).
2. *(Shape.)* For every framing, $\delta_\varphi$ has components $\varepsilon:S^1\to S^0$ and $\varepsilon:S^3\to S^2$ in $\pi_1^s=\mathbb Z/2$, and $\theta:S^3\to S^0$ in $\pi^s_3=\mathbb Z/24$, with $\varepsilon=\varepsilon_b+\varepsilon_c$ and $\theta=\theta_b+\theta_c$. So $R(\varphi)$ has cells in degrees $0,2,2,4$ and $H^*(R(\varphi);\mathbb Z)\cong HF^*(L,L';\mathbb Z)$. Moreover $R(\varphi)\simeq S^0\vee S^2\vee S^2\vee S^4$ if and only if $\varepsilon=\theta=0$.
3. *(Symmetric framings.)* Call $\varphi$ *symmetric* if $\varphi|_{E_c}=\Psi_*(\varphi|_{E_b})$ for the $U(1)$-equivariant identification $\Psi:E_b\to E_c$ over $K$. Symmetric framings exist. For each of them, $\varepsilon=0$ and $\theta=2\theta_b\in2\pi^s_3\cong\mathbb Z/12$, so $R(\varphi)\simeq(S^0\cup_\theta e^4)\vee S^2\vee S^2$. All mod 2 Steenrod operations vanish, as they do for the collapsed Lipshitz–Sarkar spectrum.
4. *(Realizing LS.)* Within symmetric framings $\theta$ takes every value in $2\pi^s_3$, including $0$. For $\theta=0$,
$$R(\varphi)\ \simeq\ \Sigma^{m+w}\bigvee_q\Sigma^{-q}\mathcal X^q_{Kh}(\kappa^\pm),$$
   the Lipshitz–Sarkar spectrum with the grading collapsed as in [6, Conj. 2].

Theorem D is a statement about the explicit correspondence $E$ and Definition 6.1. Its relevance to Floer theory rests on the following hypothesis.

**Hypothesis (R) (realization).** The Floer-theoretic realization of $\mathcal C_{\mathbb M}$ is $R(\varphi_{\rm can})$, for the Floer index bundles (assumed $SO(3)$-equivariant) and the framing $\varphi_{\rm can}$ they induce. Here "realization" means that of [19, Def. 2.16, §5], or CJS applied to the compactified cascade perturbation.

We do not prove (R), and we do not identify $\varphi_{\rm can}$ (Remark 6.5).

**Corollary E (consequences for HW).**
1. Under (Ad$_0$), the HW Floer cohomology of $\kappa^\pm$ is $\mathbb Z^4$, free, with $\bigoplus_{i-j=k}Kh^{i,j}$ in degree $k$, over $\mathbb Z$.
2. *(No strong form.)* Let $\mathcal C'$ be a flow category with four objects labelled by $Kh(\kappa^\pm)$ whose morphisms preserve $q$. Then $\mathcal C'$ has no morphisms between distinct objects. No label-preserving isomorphism of flow categories from $\mathcal C'$ to any Morse perturbation of $\mathcal C_{\mathbb M}$ exists, since the latter has nonempty morphism spaces between distinct labels (Theorem C(5)). If (P) holds, (Ad) can therefore hold only at the level of realizations, as in (Ad$_{\rm fr}$), and not as an isomorphism of flow categories.
3. *(Prediction.)* Assume (Ad$_{\rm fr}$) and (P). Assume also that the HW category has exactly four objects carrying these labels; this does not follow from the homology rank alone. Then the framing $\varphi$ supplied by (Ad$_{\rm fr}$) has $\varepsilon=\theta=0$.

**What is new, and what is not.**
* Seidel–Smith computed the trefoil in this model through the clean intersection $S^2\sqcup\mathbb{RP}^3$ [6, Lemma 60, Prop. 61]. Theorem A is the same argument for $s_1^{\pm2}$. Its only new input is the curve computation of Lemma 3.1.
* Theorem B(2) is **not new**. Hendricks–Mak–Raghunath [22, §1] state that symplectic and combinatorial Khovanov homology agree over $\mathbb Z$ for quasi-alternating links. This follows from the skein triangle of Abouzaid–Smith [9, §7 and Appendix], and the Hopf link is alternating. Our parity argument is a direct geometric derivation of this known result inside the model.
  * [22, §5.3] studies the 2-periodic Hopf link $H_+$. There $Kh_{\rm symp}(H_+;\mathbb F_2)=\mathbb F_{(0)}\oplus\mathbb F_{(-2)}^2\oplus\mathbb F_{(-4)}$, matching Theorem B. They explain Seidel's observation that the involution induced by $\iota_A$ admits no lift to a bigraded theory, even in characteristic $0$.
  * This is consistent with our position: the bigrading (B3) is *bookkeeping*, not a structure respected by the model's geometry.
  * Theorem C(5) is a different, elementary manifestation of the same phenomenon: the model's strips and Morse trajectories join generators of different $q$.
* The bigrading formula (B3) is a labelling of generators. We do not prove that it agrees with Cheng's weight grading [10] or with any intrinsic structure.
* The contribution we claim is in Theorem C and the framed correspondences of Theorem D: the explicit Floer strips (two circles per fibre, closed form), their regularity, the closed correspondence $E\cong\mathbb{RP}^3\sqcup\mathbb{RP}^3$ over $K$, and the reduction of its framed realization to one class $\theta\in\pi_3^s$ for symmetric framings. We know of no prior description of these strip families. Theorem D does not determine the canonical framing. It concerns the realization of Definition 6.1, and its Floer-theoretic meaning depends on (R). We make no claim that the model is "stronger than Khovanov homology".
* Corollary E is conditional, except for the elementary statement (2).

## 2. Conventions

**Khovanov homology.** We use Bar-Natan's conventions [25] and KnotAtlas PD codes. verify.py §0 recomputes $Kh$ over $\mathbb Z$ from the cube, with its own Smith normal form:
* $Kh(\kappa^+)=\mathbb Z_{(0,0)}\oplus\mathbb Z_{(0,2)}\oplus\mathbb Z_{(2,4)}\oplus\mathbb Z_{(2,6)}$;
* $\widetilde{Kh}(\kappa^+)=\mathbb Z_{(0,1)}\oplus\mathbb Z_{(2,5)}$;
* $Kh(3_1^{\rm left})=\mathbb Z_{(0,-1)}\oplus\mathbb Z_{(0,-3)}\oplus\mathbb Z_{(-2,-5)}\oplus\mathbb Z_{(-3,-9)}\oplus(\mathbb Z/2)_{(-2,-7)}$.

The collapse of [6, Conj. 2] is $k=i-j$. With this convention [6, Prop. 61] reproduces the left trefoil degree by degree, including the torsion (verify.py §3). This confirms that $s_1$ is a negative crossing in [6].

**Morse–Bott correspondences.** We follow [18, 16, 19]. A *two-level Morse–Bott correspondence* consists of:
* closed manifolds $C_{\rm hi},C_{\rm lo}$ with virtual bundles $V_{\rm hi},V_{\rm lo}$, whose ranks are the grading shifts;
* a closed manifold $E$ with maps $s:E\to C_{\rm hi}$, $t:E\to C_{\rm lo}$, where $s$ is a submersion (a fibre bundle with compact fibre) and
$$\dim E=\operatorname{rk}V_{\rm hi}-\operatorname{rk}V_{\rm lo}+\dim C_{\rm hi}-1 .$$

A *framing* is a stable isomorphism
$$\varphi:\ s^*(V_{\rm hi}-\underline{\mathbb R})-T_sE\ \cong\ t^*V_{\rm lo}\qquad(\text{both of rank }\operatorname{rk}V_{\rm lo}).$$
Since $TE\cong T_sE\oplus s^*TC_{\rm hi}$, this is equivalent to the familiar form $TE\oplus\underline{\mathbb R}\oplus t^*V_{\rm lo}\cong s^*(TC_{\rm hi}\oplus V_{\rm hi})$. With no intermediate objects there are no compatibility conditions. We never use $(s,t):E\to C_{\rm hi}\times C_{\rm lo}$, which here is not an immersion. Spectra are cohomologically graded as in [16]: a cell $e^n$ contributes to $\widetilde H^n$.

**Indices.** For a strip $u$ from $x$ to $y$ between graded Lagrangians, $\operatorname{ind}D_u=i(x)-i(y)$, where $i$ is Seidel's absolute index [12]. This holds because $c_1(Y)=0$ and $H^1(L)=H^1(L')=0$, as in [6, §6(A)].

## 3. The clean intersection (proof of Theorem A)

**Lemma 3.1 (matching paths).** Let $q_0,q_1,q_2\in\mathbb C$ be distinct, let $\alpha$ be an embedded path from $q_0$ to $q_1$ avoiding $q_2$, and let $t$ be the half twist exchanging $q_1$ and $q_2$ along an arc disjoint from $\alpha$ except at $q_1$. Then $t^{\pm2}(\alpha)$ is isotopic, relative to $\{q_0,q_1,q_2\}$, to a path $\alpha'$ with the following properties:
* $\alpha'$ meets $\alpha$ only at the endpoints $q_0,q_1$, transversally there;
* the loop $\alpha\cdot\alpha'^{-1}$ bounds a disc containing $q_2$.

For comparison:
* for $t^{\pm1}$: one common endpoint, no interior intersection;
* for $t^{\pm3}$: one common endpoint, one interior intersection, as in [6, Lemma 60];
* for $t^{\pm4}$: two common endpoints, one interior intersection.

*Proof.* Put $q_0=-1$, $q_1=0$, $q_2=1$, $\alpha=[-1,0]$. Realize $t^k$ by the twist $z\mapsto\frac12+(z-\frac12)\exp\big(ik\pi f(|z-\tfrac12|)\big)$, where $f=1$ on $[0,0.56]$ and $f=0$ on $[0.78,\infty)$. A point of $\alpha$ at distance $r\in(0.56,0.78)$ from $\frac12$ has angle $\pi$ there, and its image has angle $\pi+k\pi f(r)$. For $k=2$ this angle lies in $(\pi,3\pi)$, so it never returns to $\pi$ in the interior. The image of $\alpha$ is therefore a spiral that leaves $\alpha$ near $-0.28$, encircles $q_1,q_2$ once, and returns to $q_1$ along $\alpha$. Push it off $\alpha$:
* below $\alpha$ near $q_0$;
* above $\alpha$ near $q_1$, where the spiral approaches from above;
* the push-off crosses $\alpha$ only once, at $-0.12$, a point inside the twisting annulus. That point is carried off the axis.

The result $\alpha'$ meets $\alpha$ only at $q_0,q_1$, and $\alpha\cdot\alpha'^{-1}$ winds once around $q_2$. For $k$ odd the endpoint is $q_2$. The interior crossings are counted the same way: $\lfloor(k-1)/2\rfloor$. verify.py §1 confirms all four cases on a $2\times10^4$-point polygon, together with the winding number and a negative control. $\square$

**Proof of Theorem A.** In each fibre, $\Lambda_\alpha\cap\Lambda_{\alpha'}$ lies over $\alpha\cap\alpha'=\{q_0,q_1\}$. Over $q_j$ both spheres pass through the critical point $x_j$, and near $x_j$
$$\Lambda_\gamma=\{(w,e^{i\Phi_\gamma}\bar w)\}+O(|w|^2),\qquad\Phi_\gamma=\arg\gamma'(q_j)+\arg p'(q_j),$$
in coordinates $(b,c)$. So $T_{x_j}\Lambda_{\alpha'}=e^{i\delta_j}T_{x_j}\Lambda_\alpha$ with $\delta_j=\frac12(\Phi_{\alpha'}-\Phi_\alpha)\notin\pi\mathbb Z$, since the paths are transverse at $q_j$. This intersection is transverse in $S$. The fibrewise intersection is therefore the two points $x_0(x),x_1(x)$, which vary smoothly with $x\in K$; over the simply connected $K$ they form two sections $C_0,C_1$. Both $L$ and $L'$ fibre over $K$, so at a point of $C_j$
$$T L\cap TL'=(T\Lambda_\alpha\cap T\Lambda_{\alpha'})\oplus\widetilde{T_xK}=\widetilde{T_xK}=TC_j,$$
where $\widetilde{T_xK}$ is the common horizontal part. This is the clean-intersection condition of [13]. $\square$

## 4. Floer cohomology and gradings (proof of Theorem B)

**Lemma 4.1 (relative index of the fibre generators).** Let $\gamma_0,\gamma_1$ be matching paths from $q_a$ to $q_b$ that meet only at their endpoints. Let:
* $\Delta_j$ be the total turning of $\arg\gamma_j'$;
* $\phi_j(q)$ be the direction in which $\gamma_j$ leaves the endpoint $q$;
* $\delta(q)=\tfrac12(\phi_1(q)-\phi_0(q))$, defined mod $\pi$.

Then, with respect to $\Omega=da\wedge db/b$ and the gradings $\tilde\alpha_{\Lambda_{\gamma_j}}$ obtained by continuously lifting $\arg$ of the squared phase,
$$i(x_b)-i(x_a)=\frac{\Delta_1-\Delta_0}{\pi}-2\Big(\Big\{\frac{\delta(q_b)}\pi\Big\}-\Big\{\frac{\delta(q_a)}\pi\Big\}\Big).$$
For $\alpha,\alpha'$ as in Lemma 3.1 this equals $-2$. So the relative degree of $x_0,x_1$ has absolute value $2$.

*Proof.* Over an interior point $\gamma(\tau)$, $T\Lambda_\gamma$ is spanned by the horizontal lift $H$ of $\gamma'$ and the orbit direction $V=(ib,-ic)$, and $H\perp V$. We have $\Omega(H,V)=i\gamma'$, so the squared phase is $-\exp(2i\arg\gamma')$, independently of the point on the circle. At the critical points the two tangent planes differ by $e^{i\delta}\oplus e^{i\delta}$, with both Kähler angles equal to $\delta$ (proof of Theorem A). Seidel's formula [12] for the absolute index of a transverse intersection point is
$$i=\tilde\alpha_1-\tilde\alpha_0-\textstyle\sum_k\{\text{angle}_k/\pi\}.$$
It gives the displayed difference, because the $\tilde\alpha_j$ change by $\Delta_j/\pi$ between $x_a$ and $x_b$.
* In the disc model ($\alpha$ lower, $\alpha'$ upper semicircle, $q_2=0$) we have $\Delta_0=\pi$, $\Delta_1=-\pi$ and $\delta\equiv-\pi/2$ at both ends, so the difference is $-2$ exactly.
* The spiral representative of Lemma 3.1 gives $-2$ numerically (verify.py §4).
* Control: an isotopic copy of $\alpha$ (empty bigon) also gives $2$, the degree gap of $H^*(S^2)=HF(\Lambda_\alpha,\Lambda_\alpha)$.

$\square$

**Proof of Theorem B.** (1) By Theorem A and [13] there is a spectral sequence, filtered by action, whose $E_1$ page is
$$H^{*-s_0}(C_0;\mathfrak o_0)\oplus H^{*-s_1}(C_1;\mathfrak o_1).$$
The orientation local systems are trivial because $C_j\cong S^2$ is simply connected. The shift $s_j$ is the degree of the fibre generator $x_j$: a constant strip in the base contributes index $0$, and the operator is block triangular (§5.3). By Lemma 4.1, $|s_1-s_0|=2$. All $E_1$ groups lie in even degrees, while every differential $d_r$ has degree $+1$, so the sequence degenerates. Each filtration quotient is free, so there is no extension problem over $\mathbb Z$, and $HF$ is free of rank $4$.

The absolute normalization can be read off in two ways. One can use [6, §6(A)]. Alternatively, [9, (1.1)] gives the multiset of degrees over $\mathbb Q$, namely $\{0,2,2,4\}$ for $\kappa^-$. The only solution of $\{s_0,s_0+2,s_1,s_1+2\}=\{0,2,2,4\}$ is $\{s_0,s_1\}=\{0,2\}$ (verify.py §3), which confirms the relative shift independently.

(2) Compare degree by degree, using the shift $m+w$. For $\kappa^+$ this is Poincaré duality of Floer cohomology for the exact $4$-dimensional Lagrangians $L,L'$, $HF^k(L',L)\cong HF^{4-k}(L,L')^\vee$. Exchanging the two arguments exchanges the two Hopf links: applying the inverse monodromy symplectomorphism gives $HF(L(t^{\pm2}\alpha),L(\alpha))\cong HF(L(\alpha),L(t^{\mp2}\alpha))$, where $L(\beta)$ is the fibred Lagrangian built from the path $\beta$ as in §1.3, and $t^{\mp2}$ is the braid of the mirror link. (We do not use [6, Prop. 59], which concerns orientation reversal.) Both sides are free, so the isomorphism holds over $\mathbb Z$.

(3) The four generators have Floer degree $s_j+\mu$. The formula is the unique affine assignment that is constant in $h$ on each $C_j$, satisfies $h-q=\deg-(m+w)$, and matches the multiset of $Kh(\kappa^\pm)$ (verify.py §3). Inside $C_j$, the two generators have the same $h$ and $q$ differing by $2$: the base sphere is the $V$ factor. $\square$

**Remark 4.2 (the fibre theory is the reduced theory).** The fibre Floer group $HF_S(\Lambda_\alpha,\Lambda_{\alpha'})=\mathbb Z x_0\oplus\mathbb Z x_1$ has relative degree $2$, the same shape as $\widetilde{Kh}(\kappa^+)=\mathbb Z_{(0,1)}\oplus\mathbb Z_{(2,5)}$. So Theorem B realizes $Kh=\widetilde{Kh}\otimes V$ geometrically as (fibre)$\otimes H^*(K)$. We do not claim a general statement of this kind.

## 5. The flow category (proof of Theorem C)

### 5.1 Every strip is vertical

**Lemma 5.1.** Let $u$ be a finite-energy $J$-holomorphic strip with $u(\cdot,0)\in L$, $u(\cdot,1)\in L'$, and ends on $L\cap L'$. Then $\pi\circ u$ is constant.

*Proof.* $\pi:Y\to X$ is holomorphic, so $v=\pi\circ u$ is a holomorphic strip in the Stein manifold $X$, with both boundary components on the exact Lagrangian $K$ and ends at points of $K$. Write $\omega_X=d\lambda$ and $\lambda|_K=dg$. Then
$$\int v^*\omega_X=\big[g(v(+\infty))-g(v(-\infty))\big]-\big[g(v(+\infty))-g(v(-\infty))\big]=0 .$$
Since $\omega_X$ is positive on complex lines, $v$ is constant. $\square$

### 5.2 Classification in a fibre

By Lemma 5.1 and $SO(3)$-homogeneity, it suffices to study one fibre $S=\{bc=p(a)\}$. Let $R$ be the closed bigon bounded by $\alpha\cup\alpha'$; by Lemma 3.1 it contains $q_2$ in its interior and has corners at $q_0,q_1$ of interior angles $\vartheta_0,\vartheta_1\in(0,2\pi)$. Strips are maps $Z=\mathbb R\times[0,1]\to S$ with $\partial_su+i\partial_tu=0$. By the Riemann mapping theorem with Carathéodory's extension, there is a conformal map $A_R:Z\to\operatorname{int}R$, with $t=0\mapsto\alpha$, $t=1\mapsto\alpha'$, $s\to-\infty\mapsto q_0$ and $s\to+\infty\mapsto q_1$. It is unique up to translation. Let $z_2=A_R^{-1}(q_2)$, and let $B:Z\to\mathbb D$ be the conformal map with $B(z_2)=0$, so that $G=\log|B|$ is the Green function of $Z$ with pole $z_2$.

*Disc model.* After an affine change of $a$ and $c\mapsto-c$, take $q_0=-1$, $q_1=1$, $q_2=0$, $p(a)=a(a^2-1)$, $\alpha$ the lower and $\alpha'$ the upper semicircle. This choice is allowed because Floer cohomology and the flow category up to isotopy are unchanged when $\alpha'$ moves by an isotopy of matching paths rel endpoints avoiding $q_2$: such an isotopy lifts to an exact, hence Hamiltonian, isotopy of $L'$ through fibred Lagrangians. Then $R=\bar{\mathbb D}$, $\vartheta_0=\vartheta_1=\pi$,
$$A_R(\zeta)=\frac{e^{\pi\zeta}-i}{e^{\pi\zeta}+i},$$
$B=A_R$ and $G=\log|a|$ (verify.py §5). Everything below is explicit in this model.

**Proposition 5.2.** The nonconstant strips in $S$ with boundary on $\Lambda_\alpha,\Lambda_{\alpha'}$ and ends on $\{x_0,x_1\}$ all run from $x_0$ to $x_1$. Up to translation they form exactly two circles: for $k\in\{+1,-1\}$ and $\vartheta\in\mathbb R/2\pi$,
$$a=A_R,\qquad b=e^{i\vartheta}\big(p(A_R)\,B^{k}\big)^{1/2},\qquad c=p(A_R)/b,$$
where $k=+1$ gives $u_b$ ($b$ vanishes at $z_2$) and $k=-1$ gives $u_c$ ($c$ vanishes at $z_2$). The square root exists because $p(A_R)B^{k}$ has a zero of even order $1+k$ at $z_2$ and no other zeros in $Z$. In the disc model these are the maps $u_b^\vartheta,u_c^\vartheta$ of Theorem C(2).

*Proof.* *Projection.* $A=a\circ u$ is holomorphic on $Z$, maps the two boundary lines into $\alpha$ and $\alpha'$, and extends continuously to the two ends. Take the local degree of the extended map $\bar Z\to\mathbb C$ over points off $\alpha\cup\alpha'$. It is $0$ on the unbounded component. Across $\alpha$ it jumps by the net number of times the boundary covers $\alpha$, which is $1$ if the ends are $(q_0,q_1)$, $-1$ if they are $(q_1,q_0)$, and $0$ if they coincide.
* By positivity of holomorphic degree, the reversed case is impossible.
* The coinciding case gives a constant map.
* In the remaining case $A:Z\to\operatorname{int}R$ is proper of degree $1$, hence $A=A_R\circ\tau_\sigma$ for a translation $\tau_\sigma$.

*Lift.* Drop $\tau_\sigma$. On $Z\setminus\{z_2\}$, $bc=p(A)\ne0$, so $b$ and $c$ do not vanish there. At $z_2$ exactly one of them has a simple zero. Set $h=\log|b|^2-\log|p(A)|$, harmonic on $Z\setminus\{z_2\}$, with
* $h=0$ on $\partial Z$, since $|b|=|c|$ on $\Lambda_\alpha,\Lambda_{\alpha'}$;
* $h-kG$ harmonic near $z_2$, with $k=\operatorname{ord}_{z_2}b-\operatorname{ord}_{z_2}c\in\{\pm1\}$;
* $h$ bounded at both ends.

The last property holds because at each end $u$ converges to $x_j$ along an eigenvector of the asymptotic operator [15], and every vector of $T_{x_j}\Lambda=\{(w,e^{i\Phi}\bar w)\}$ has $|b|=|c|$. By the maximum principle, $h=kG$. So $|b|^2=|p(A)B^k|$, and $b$ is determined up to a constant phase, as displayed. Conversely, these maps satisfy $bc=p(A)$, and on $\partial Z$ we have $|b|^2=|p(A)|=|c|^2$ because $|B|=1$ there. In the disc model
$$|b|^2-|c|^2=\pm(1-|a|^2)\,|a^2-1|$$
vanishes exactly on $\partial\mathbb D$ (verify.py §5). $\square$

### 5.3 Regularity

**Lemma 5.3.** For every strip $u$ of Proposition 5.2, the vertical linearized operator $D_u^{\rm v}$ has $\ker D^{\rm v}_u=\langle\partial_su,\ \partial_\vartheta u\rangle$ and $\operatorname{coker}D_u^{\rm v}=0$. In $Y$ the full operator $D_u$ is onto with $\dim\ker D_u=4$.

*Proof.* Since $J$ is integrable, $D_u$ is the $\bar\partial$-operator of the holomorphic bundle $u^*TS$. Let $\xi=(\dot a,\dot b,\dot c)$ be in the kernel, so that $c\dot b+b\dot c=p'(a)\dot a$.

*Decay.* At $x_j$ the two tangent planes differ by $e^{i\delta_j}\oplus e^{i\delta_j}$ (proof of Theorem A). So the asymptotic operator at $x_j$ has spectrum $\delta_j+\pi\mathbb Z$, each eigenvalue of multiplicity $2$. At a corner of angle $\vartheta_j$ we have $A-q_j\asymp e^{-\vartheta_j|s|}$, so $b,c\asymp|A-q_j|^{1/2}$ decay at the rate $\vartheta_j/2\in(0,\pi)$. This rate is an eigenvalue [15], so the spectrum is $\vartheta_j/2+\pi\mathbb Z$, and its smallest positive element is $\vartheta_j/2$. Hence every kernel element decays at least as fast as $b$ and $c$ [15]. In the disc model $\vartheta_j=\pi$, matching $\delta_j\equiv\pi/2$ in Lemma 4.1.

*Horizontal part.* $\dot a$ is a holomorphic section of $A^*T\mathbb C$, tangent to $\alpha,\alpha'$ along $\partial Z$ and decaying at the ends. So $\dot a/A'$ is a holomorphic vector field on $Z$, tangent to $\partial Z$ and bounded at the ends. By Schwarz reflection it is the constant real field, so $\dot a=\lambda\,\partial_sA$ with $\lambda\in\mathbb R$. In the disc model this is the statement $\dot a=\lambda(1-a^2)$, the hyperbolic Möbius field fixing $\pm1$ (verify.py §5).

*Vertical part.* Subtract $\lambda\,\partial_su$, so that $\dot a=0$ and $c\dot b+b\dot c=0$. Then $g=\dot b/b=-\dot c/c$ is holomorphic on $Z$: at $z_2$, where $b$ (say) vanishes, $c\ne0$ forces $\dot b(z_2)=0$. The boundary condition $\delta(|b|^2-|c|^2)=0$ gives $(|b|^2+|c|^2)\operatorname{Re}g=0$, i.e. $\operatorname{Re}g=0$ on $\partial Z$. By the decay rates, $g$ is bounded at the ends. By reflection, $g$ extends to a bounded holomorphic function on the doubled strip, hence to a constant, which is imaginary. So $g=i\dot\vartheta$, which is the rotation.

Without the decay, $g=(1+a)/(1-a)$ in the disc model would be allowed; verify.py §5 shows it is excluded, and checks the Laurent version of the argument.

So $\dim\ker D_u^{\rm v}=2=i(x_0)-i(x_1)=\operatorname{ind}D^{\rm v}_u$ (Lemma 4.1), and the cokernel vanishes.

In $Y$ we have the holomorphic exact sequence $0\to T^{\rm v}\to TY\to\pi^*TX\to0$, with $TL\cap T^{\rm v}=T\Lambda_\alpha$ and $TL/T\Lambda_\alpha=T_xK$, and similarly for $L'$. So $D_u$ is block triangular. The quotient block is the constant strip in $T_xX=\mathbb C^2$ with boundary $T_xK$ on both sides: onto, with kernel $T_xK$. Hence $D_u$ is onto with $\dim\ker=2+2$. $\square$

### 5.4 The family over $K$ and the category

The effective circle action rotates $\vartheta$. Over $x\in K$, the phase $\vartheta$ is the phase of $b\,(p(A_R)B^{k})^{-1/2}$ at a reference point, which is an element of the unit circle of $F^{-2}_x$. Hence
$$E_b\cong E_c\cong S(F^{-2}|_K),$$
the unit circle bundle of a line bundle of degree $\mp2$ over $S^2$. Thus $E_b\cong E_c\cong L(2,1)=\mathbb{RP}^3=SO(3)$. This is the same circle bundle that produces the $\mathbb{RP}^3$ in [6, Lemma 60], and it is also the principal $SO(2)$-bundle $P=SO(3)\to SO(3)/SO(2)=K$. The $U(1)$-equivariant map $\Psi:E_b\to E_c$, $u_b^\vartheta\mapsto u_c^\vartheta$, covers the identity of $K$ and is canonical up to a constant rotation.

*Proof of Theorem C.* (1) is Lemma 5.1, (2) is Proposition 5.2, and (3) is Lemma 5.3.

(4) By (1)–(3) the parametrized moduli space of strips from $C_{\rm hi}$ to $C_{\rm lo}$ is a manifold of dimension $4$, which is $\mathbb R\times(E_b\sqcup E_c)$. Dividing by $\mathbb R$ gives a closed $3$-manifold. There are no broken strips, since there are no strips from $C_j$ to itself (Proposition 5.2, coinciding case) and none from $C_{\rm lo}$ to $C_{\rm hi}$. The dimension $3=2-0+2-1$ agrees with §2. The map $p$ is a circle bundle, in particular a submersion.

(5) An unbroken cascade [14] from $(C_{\rm hi},M)$ to $(C_{\rm lo},m_0)$ consists of three pieces:
* a negative gradient half-line in $C_{\rm hi}$ from $M$ to a point $y$;
* a strip $u\in E$ with $p(u)=y$;
* a gradient half-line in $C_{\rm lo}$ from $y$ to $m_0$.

Since $W^u(M)\cap W^s(m_0)=S^2\setminus\{M,m_0\}$, the unbroken cascades of this type form $p^{-1}(S^2\setminus\{M,m_0\})\ne\emptyset$. The Morse trajectories of the height function from $M$ to $m_0$ on each $C_j$ form a circle. In both cases the endpoints have different $q$ by Theorem B(3) (verify.py §9).

As $y$ tends to a pole, a Morse segment breaks. The compactification of the first space therefore has boundary strata through $(C_{\rm hi},m_0)$ and $(C_{\rm lo},M)$, of the form (Morse circle)$\times$(fibre circle). We do not need, and do not give, the compactified perturbed category. $\square$

## 6. Framings and realization (proof of Theorem D)

### 6.1 Realization of a two-level correspondence

**Definition 6.1.** Let $(C_{\rm hi},C_{\rm lo},E,s,t;\varphi)$ be a framed two-level Morse–Bott correspondence (§2). The realization is built in four steps.
1. *Fibrewise embedding.* Choose an embedding $\iota:E\hookrightarrow C_{\rm hi}\times\mathbb R^N$ over $C_{\rm hi}$, so that $\mathrm{pr}_1\circ\iota=s$. It exists for $N$ large because $s$ is a fibre bundle with compact fibre. Let $\nu_s$ be its fibrewise normal bundle, so that $\nu_s\oplus T_sE\cong\underline{\mathbb R}^N$ and $\operatorname{rk}\nu_s=N-\dim(\text{fibre})$.
2. *Twisted transfer.* The Pontryagin–Thom collapse of a tubular neighbourhood of $\iota(E)$ in $\mathrm{Th}\big((V_{\rm hi}-\underline{\mathbb R})\oplus\underline{\mathbb R}^N\big)$ gives the Becker–Gottlieb–Boardman umkehr map [26]
$$s^!:\ \Sigma^N\,\Sigma^{-1}\mathrm{Th}(V_{\rm hi})\ \longrightarrow\ \mathrm{Th}\big(s^*(V_{\rm hi}-\underline{\mathbb R})\oplus\nu_s\big).$$
3. *Framing.* $\varphi\oplus\mathrm{id}$ is a stable isomorphism $s^*(V_{\rm hi}-\underline{\mathbb R})\oplus\nu_s\cong t^*V_{\rm lo}\oplus\underline{\mathbb R}^N$. In the Hopf model the ranks are $(2-1)+(N-1)=N=0+N$.
4. *Push-forward.* $t_*:\mathrm{Th}(t^*V_{\rm lo})\to\mathrm{Th}(V_{\rm lo})$ is induced by the bundle map covering $t$.

Desuspending by $N$, put
$$\delta_\varphi=t_*\circ\mathrm{Th}(\varphi)\circ s^!:\ \Sigma^{-1}\mathrm{Th}(V_{\rm hi})\to\mathrm{Th}(V_{\rm lo}),\qquad R(\varphi)=\operatorname{Cofib}(\delta_\varphi).$$
Different choices of $\iota$ are isotopic for $N$ large, so the homotopy class of $\delta_\varphi$ depends only on $\varphi$.

*Remarks.*
* For a Morse flow category with two levels of objects, i.e. $C_{\rm hi}$ and $C_{\rm lo}$ points and $E$ a framed closed manifold, $\delta_\varphi$ is the Pontryagin–Thom class of $E$, which is the Cohen–Jones–Segal attaching map [18], [16, §3].
* For general Morse–Bott categories, [19, Def. 2.16, §5] builds realizations from embeddings, normal data and bundle identifications. We have not checked that this construction, applied to $\mathcal C_{\mathbb M}$, gives Definition 6.1; that is part of Hypothesis (R).
* Definition 6.1 is used only because it is explicit. The object bundles enter only through their $SO(3)$-equivariant isomorphism classes.

### 6.2 Local pieces

**Lemma 6.2.** Let $V$ be an $SO(3)$-equivariant virtual vector bundle over $K=SO(3)/SO(2)$. Then $w_2(V)=0$, and $\mathrm{Th}(V)\simeq S^r\vee S^{r+2}$, $r=\operatorname{rk}V$.

*Proof.* $V$ is associated to $P=SO(3)$ and to a virtual representation of $SO(2)$. Its complex summands of weight $k$ give line bundles with $c_1=k\,e(P)=2k$, since $e(P)=\chi(S^2)=2$; its real summands are trivial. So $w_2(V)\equiv\sum c_1\equiv0$. The stable Thom spectrum over $S^2$ is $S^r\cup e^{r+2}$, attached by $w_2(V)\,\eta\in\pi_1^s$ via the $J$-homomorphism. Here that class is $0$. As a control, for $\mathcal O(1)\to\mathbb{CP}^1$ the Thom space is $\mathbb{CP}^2$, which does not split (verify.py §7). $\square$

Since $V_{\rm hi},V_{\rm lo}$ are prescribed $SO(3)$-equivariant, this proves Theorem D(1). The Floer index bundles are expected to be equivariant because $J$, $L$, $L'$ are $SO(3)$-invariant, but we do not construct them; this is part of (R).

### 6.3 The connecting map

**Lemma 6.3.** Let $\varphi$ be any framing. Fix splittings $\mathrm{Th}(V_{\rm lo})\simeq S^0\vee S^2$ and $\Sigma^{-1}\mathrm{Th}(V_{\rm hi})\simeq S^1\vee S^3$. Then:
* the components $S^1\to S^0$ and $S^3\to S^2$ of $\delta_\varphi$ both equal $\varepsilon=\varepsilon_b+\varepsilon_c\in\pi_1^s$, where $\varepsilon_\bullet$ is the framed bordism class of a fibre circle of $E_\bullet$;
* the component $S^1\to S^2$ vanishes;
* the component $\theta=\theta_b+\theta_c\in\pi_3^s$ is independent of the splittings once $\varepsilon=0$.

*Proof.* $\delta_\varphi=\delta_b+\delta_c$ because $E=E_b\sqcup E_c$. Since $s=t=p$ and $C_{\rm hi}=C_{\rm lo}=K$, all three steps of Definition 6.1 are fibrewise over $K$:
* $s^!$ is the fibrewise Pontryagin–Thom map of $\iota$;
* $\varphi$ is a bundle isomorphism over $E$;
* $t_*$ covers $\mathrm{id}_K$ after projection.

So $\delta_\varphi$ is the Thom-ification of a fibrewise stable map over $K$. Its value on the fibre over $x$ is the Pontryagin–Thom class of the framed circle $p^{-1}(x)$, which is $\varepsilon\in\pi_1^s$, independent of $x$ because $K$ is connected.

Restricting over a point, i.e. to the bottom cells, therefore gives $\varepsilon$. Restricting over a disc $D\subset K$, where everything is trivial and $\mathrm{Th}(V|_D)/\mathrm{Th}(V|_{\partial D})$ is the top cell, gives the fibre map smashed with $S^2$, which is again $\varepsilon$. The component $S^1\to S^2$ lies in $\pi_{-1}^s=0$. The remaining component $\theta$ is not determined fibrewise.

Changing the splittings changes $\theta$ by composites with $\eta^2$ and the components $\varepsilon$, which vanish once $\varepsilon=0$. $\square$

If $\varepsilon\ne0$, then $Sq^2\ne0$ on $H^*(R(\varphi);\mathbb F_2)$. If $\varepsilon=0$, then $R(\varphi)\simeq(S^0\cup_\theta e^4)\vee S^2\vee S^2$, which is a wedge of spheres if and only if $\theta=0$. This proves Theorem D(2), the identification $H^*(R(\varphi))=HF^*$ being cellular with all cells in even degrees.

### 6.4 Symmetric framings

**Existence.** Under $P\to K$, the pull-back of any $P$-associated bundle to $E_b\cong P$ is canonically trivial, and so is $T_pE_b$, since it is spanned by the orbit vector field. Both sides of the framing equation are therefore stably trivial on $E_b$, so framings $\varphi_b$ exist. Put $\varphi_c=\Psi_*\varphi_b$.

**Proof of Theorem D(3).** For a symmetric framing, $\Psi$ is an isomorphism of framed correspondences over $K$, so $\delta_c=\delta_b$, $\varepsilon=2\varepsilon_b=0\in\mathbb Z/2$ and $\theta=2\theta_b$. The mod 2 cohomology has classes in degrees $0,2,2,4$. Since $\varepsilon=0$, $Sq^2=0$; $Sq^1=Sq^3=0$ for degree reasons; and $Sq^4$ detects $\theta$ modulo $2$ (Hopf invariant one), which vanishes for $\theta\in2\pi_3^s$. The collapsed Lipshitz–Sarkar spectrum is a wedge of spheres [16, §9.2], so all these operations vanish there as well. $\square$

**Proof of Theorem D(4).** Let $g\in\pi_3(SO)$, and let $f_g:E_b\to S^3\to SO$ be the collapse onto the top cell followed by $g$. Changing $\varphi_b$ by $f_g$ does not change $\varepsilon_b$, because $f_g$ is constant on the 2-skeleton, which contains the fibres. It changes $\theta_b$ by $J(g)$. Doing the same on $E_c$ keeps the framing symmetric and changes $\theta$ by $2J(g)$. By Adams [24] and Toda [23], $J:\pi_3(SO)=\mathbb Z\to\pi_3^s=\mathbb Z/24$ is onto, so $\theta$ takes every value in $2\pi_3^s$, in particular $0$. Then $R(\varphi)\simeq S^0\vee S^2\vee S^2\vee S^4$, with cells in the degrees of $HF$. This is $\Sigma^{m+w}\bigvee_q\Sigma^{-q}\mathcal X^q_{Kh}$: for $\kappa^+$ the cells are $h-q+4\in\{4,2,2,0\}$, and [16, §9.2] gives $\mathcal X^0=\mathcal X^2=S^0$ and $\mathcal X^4=\mathcal X^6=S^2$ (verify.py §§0, 8). $\square$

**Remark 6.4 ($p=3$).** $\theta\in2\pi_3^s$ can be nonzero modulo $3$. The Steenrod power $P^1$ on $H^*(\,\cdot\,;\mathbb F_3)$ would detect such a $\theta$, whereas $P^1=0$ for the Lipshitz–Sarkar spectrum. So the mod 2 agreement in D(3) is not a full identification.

**Remark 6.5 (the Floer-canonical framing).** In any framework that produces canonical framings natural under symplectomorphisms preserving brane data, such as [20], we expect the canonical framing to be symmetric. The reason is that the fibrewise swap $\sigma_x:(a,b,c)\mapsto(a,c,b)$ is holomorphic and symplectic in a single fibre, preserves $\Lambda_\alpha,\Lambda_{\alpha'}$, fixes $x_0,x_1$, and exchanges the $b$- and $c$-circles. Moreover brane data on $\Lambda\cong S^2$ are unique up to homotopy, since $\pi_1(O)$, $\pi_2(O)$ and $H^1(S^2;\mathbb Z/2)$ impose nothing new. This would give $\varepsilon=0$. However, $\sigma_x$ does not extend over $K$, because $F^{-2}\not\cong F^{2}$, and we have not identified $\theta$ for the canonical framing. We do not use this remark.

## 7. Consequences for HW (proof of Corollary E)

(1) is Theorem B(2) composed with (Ad$_0$).

(2) If morphisms preserve $q$ and the four objects have four distinct $q$ (verify.py §0), every morphism space between distinct objects is empty. In any Morse perturbation of $\mathcal C_{\mathbb M}$, the cascades from $(C_{\rm hi},M)$ to $(C_{\rm lo},m_0)$ contain $p^{-1}(S^2\setminus\{M,m_0\})\ne\emptyset$, and $\mathcal M((C_j,M),(C_j,m_0))\cong S^1$; in each case the endpoints have different $q$ (Theorem C(5)). So no label-preserving isomorphism exists.

(3) Under (P), and with the four-object assumption, the HW category is discrete by (2), so its realization is $S^0\vee S^2\vee S^2\vee S^4$, with cells in the degrees fixed by (Ad$_0$). By (Ad$_{\rm fr}$), $R(\varphi)$ is the same spectrum for the supplied $\varphi$. Theorem D(2) then gives $\varepsilon=\theta=0$. $\square$

Corollary E(2)–(3) concerns the relationship between gauge theory and the model, and it is the only place where (P) enters. In the model, the second grading is a bookkeeping grading that the morphisms do not respect, while in gauge theory it is expected to be a topological charge. For the Hopf link these two pictures are consistent exactly when the model's attaching data vanish.

## 8. Outlook: the trefoil

For $s_1^{\pm3}$, [6, Lemma 60] gives $L\cap L'=S^2\sqcup\mathbb{RP}^3$. Lemma 3.1 recovers the single interior intersection. $\mathbb{RP}^3$ is the circle bundle $E$ of §5.4, now appearing as a component of the intersection rather than as a morphism space. The Morse–Bott $E_1$ page reproduces $Kh(3_1)$ over $\mathbb Z$, including the $\mathbb Z/2$ in $Kh^{-2,-7}$ [6, Prop. 61] (verify.py §3). Stably, $\Sigma^\infty\mathbb{RP}^3_+\simeq S^0\vee\Sigma^\infty\mathbb{RP}^2\vee S^3$, and the Moore piece $\Sigma^3\mathbb{RP}^2$ sits exactly where the Lipshitz–Sarkar piece $\mathcal X^{-7}(3_1^{\rm left})=\Sigma^{-4}\mathbb{RP}^2$ sits after the collapse $\Sigma^{7}$: $\mathbb Z/2$ in degree $k=5$ (verify.py §10).

The decisive test, which we do not carry out, has three parts:
* the twisting $(w_1,w_2)$ of the index bundle over $\mathbb{RP}^3$, which could change the Moore piece;
* the $\eta$-attaching maps between the $S^2$ and $\mathbb{RP}^3$ components, which are now joined by 1-dimensional moduli spaces;
* comparison with $\mathcal X^7(3_1^{\rm right})=\Sigma\mathbb{RP}^2$, where $Sq^2=0$ because each $q$ carries a single piece.

The method of §§5–6 applies: verticality, Green-function lifts and the $SO(3)$ structure. The new feature is that the circle bundle is an object rather than a morphism.

## 9. Discussion, literature and status of claims

**Literature.**
* *Symplectic Khovanov cohomology.* Seidel–Smith [6] define it, and [6, §6(C)] contains the local model and the trefoil computation. Manolescu [7, 8] gives the Hilbert scheme picture. Abouzaid–Smith [9] prove the comparison in characteristic $0$. Cheng [10] gives a relative second grading in characteristic $0$. Hendricks–Mak–Raghunath [22] develop the annular theory and localization. They record the integral agreement for quasi-alternating links [22, §1], via [9, §7 and Appendix]. In [22, §5.3] they treat the Hopf link and the obstruction to bigraded lifts of $\iota_A$.
* *Gauge theory.* Witten [1, 3] proposes the HW/KW picture, Gaiotto–Witten [2, §4] the adiabatic regime, and Bleher [5, Conj. B] the conjectural identification. None of these proves an adiabatic correspondence.
* *Homotopy types.* Lipshitz–Sarkar [16, 17] construct the Khovanov spectrum and $Sq^2$. Cohen–Jones–Segal [18], Bonciocat [19] and Abouzaid–Blumberg [20] provide the framework for realizations. The survey [21, §§2.3, 4] records that no Floer-theoretic identification of the Lipshitz–Sarkar spectrum is known. We found no prior description of the Floer strips or framed correspondences in the Seidel–Smith model for a nontrivial link. We did not check unpublished sources.
* *This line.* [M13] studies Bleher's Grothendieck–Springer model; for one pair of strands it finds the monodromy $\tau^{2n}$. [M22] rules out circle-invariant HW arrows between He–Mazzeo solutions. [M24, M25, M30–M33] treat HW Floer homotopy without a link near the Anderson–Henningson fold. The present paper does not use them.

**Proved here (modulo imported results).**
* Lemma 3.1, Theorem A.
* Lemma 4.1, Theorem B(1),(3). Theorem B(2) is a direct derivation of a result known from [22, §1], [9].
* Lemma 5.1, Proposition 5.2, Lemma 5.3, Theorem C.
* Lemmas 6.2–6.3, Theorem D, for prescribed equivariant bundles and the realization of Definition 6.1.
* Corollary E(2).

**Imported.**
* The reduction of $Kh_{\rm symp}(\widehat{s_1^k})$ to the local model of [6, §6(C)], including the identification of the gradings of [6, §6(A)].
* The Morse–Bott spectral sequence for clean intersections [13] and the cascade description of Morse–Bott Floer moduli [14].
* Asymptotic decay of holomorphic strips [15].
* Seidel's absolute index [12].
* [9, (1.1)], used only as a second determination of the absolute shift.
* $\pi_3^s=\mathbb Z/24=\operatorname{Im}J$ [23, 24]; the attaching map of a Thom spectrum over $S^2$.
* The Becker–Gottlieb–Boardman umkehr for fibre bundles [26].

**Conditional.**
* Corollary E(1) on (Ad$_0$).
* Corollary E(3) on (Ad$_{\rm fr}$), (P) and the four-object assumption.
* The Floer-theoretic meaning of Theorem D on (R): that the Floer index bundles are $SO(3)$-equivariant and that the Floer realization is $R(\varphi_{\rm can})$.

**Numerical only.** verify.py §1, the polygonal curve computations for Lemma 3.1, and the spiral cross-check in §4. Both agree with exact arguments: the angle argument in the proof of Lemma 3.1, and the exact disc model in §4.

**Not claimed.**
* That the Floer-canonical framing is symmetric, or that it has $\theta=0$ (Remark 6.5).
* A description of the compactified Morse-perturbed (cascade) flow category; only the unperturbed correspondence and the nonemptiness statements of Theorem C(5) are claimed.
* Hypothesis (R).
* Agreement of (B3) with Cheng's weight grading.
* Any statement about HW without (Ad).
* Any statement for links other than $\kappa^\pm$; for the trefoil, §8 is an outline.
* That the model contains more information than Khovanov homology.

**Open problems.**
1. Compute $\theta$ for the canonical framing, e.g. through an $SO(3)$-equivariant brane structure, or by identifying $E_b$ with $SO(3)$ with its Lie-group framing twisted by the index representation.
2. Carry out §8 for the trefoil: twisting over $\mathbb{RP}^3$, $\eta$-maps between components, and comparison with $\Sigma\mathbb{RP}^2$.
3. Relate the bookkeeping bigrading (B3) to Cheng's weight grading [10] and to the covering of [2, §4.1.4], so that the second grading becomes a structure on the model.
4. Prove (Ad$_0$) for $\kappa^\pm$, starting from Bleher's program [5].

**Verifier.**
* verify.py runs 69 checks, with FALLOS = 0. They are exact (integer cube and Smith normal form, sympy) except for the curve polygons. They check:
  * $Kh$ and $\widetilde{Kh}$ of both Hopf links and the trefoil over $\mathbb Z$;
  * the curve counts for $k=1,\dots,4$;
  * the cohomology bookkeeping of the clean intersection and the comparison with $Kh$;
  * the uniqueness of shifts, parity, and the bigrading formula;
  * the index $-2$ of Lemma 4.1;
  * the algebraic identities satisfied by the closed-form strips, and the finite-dimensional (Laurent) analogue of the kernel argument;
  * the evenness of Euler classes;
  * the $\mathbb Z/2$ and $\mathbb Z/24$ arithmetic of Theorem D, which takes Lemma 6.3's decomposition as input;
  * the $q$-labels.
* verify.py does **not** verify Fredholm regularity, the topology of cascade spaces, or the Pontryagin–Thom construction. Its §§6 and 8 are bookkeeping only.
* verify.mpl mirrors the exact parts. The coordinator ran it in Maple, with FALLOS = 0.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086; arXiv:1106.4789.
3. E. Witten, *Khovanov homology and gauge theory*, Geom. Topol. Monogr. 18 (2012), 291–308; arXiv:1108.3103.
4. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207; arXiv:1010.2353.
5. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
6. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514; arXiv:math/0405089.
7. C. Manolescu, *Nilpotent slices, Hilbert schemes, and the Jones polynomial*, Duke Math. J. 132 (2006), 311–369; arXiv:math/0411015.
8. C. Manolescu, *Link homology theories from symplectic geometry*, Adv. Math. 211 (2007), 363–416; arXiv:math/0601629.
9. M. Abouzaid, I. Smith, *Khovanov homology from Floer cohomology*, J. Amer. Math. Soc. 32 (2019), 1–79; arXiv:1504.01230.
10. Z. Cheng, *Bigrading the symplectic Khovanov cohomology*, Algebr. Geom. Topol. 23 (2023); arXiv:2111.07792.
11. M. Khovanov, P. Seidel, *Quivers, Floer cohomology, and braid group actions*, J. Amer. Math. Soc. 15 (2002), 203–271; arXiv:math/0006056.
12. P. Seidel, *Graded Lagrangian submanifolds*, Bull. Soc. Math. France 128 (2000), 103–149; arXiv:math/9903049.
13. M. Poźniak, *Floer homology, Novikov rings and clean intersections*, in: Northern California Symplectic Geometry Seminar, Amer. Math. Soc. Transl. Ser. 2, 196 (1999), 119–181.
14. U. Frauenfelder, *The Arnold–Givental conjecture and moment Floer homology*, Int. Math. Res. Not. 2004, no. 42, 2179–2269.
15. J. Robbin, D. Salamon, *Asymptotic behaviour of holomorphic strips*, Ann. Inst. H. Poincaré Anal. Non Linéaire 18 (2001), 573–612.
16. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.
17. R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848; arXiv:1204.5776.
18. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.
19. C. M. Bonciocat, *Revisiting the Cohen–Jones–Segal construction in Morse–Bott theory*, arXiv:2409.11278.
20. M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.
21. M. Khovanov, R. Lipshitz, *Categorical lifting of the Jones polynomial: a survey*, arXiv:2202.02473.
22. K. Hendricks, C. Y. Mak, S. Raghunath, *Symplectic annular Khovanov homology and fixed point localizations*, arXiv:2408.06453.
23. H. Toda, *Composition Methods in Homotopy Groups of Spheres*, Ann. of Math. Stud. 49, Princeton Univ. Press, 1962.
24. J. F. Adams, *On the groups J(X) IV*, Topology 5 (1966), 21–71.
25. D. Bar-Natan, *On Khovanov's categorification of the Jones polynomial*, Algebr. Geom. Topol. 2 (2002), 337–370.
26. J. C. Becker, D. H. Gottlieb, *The transfer map and fiber bundles*, Topology 14 (1975), 1–12; J. M. Boardman, *Stable homotopy theory*, mimeographed notes, Univ. of Warwick, 1966, Ch. V.

Papers in this line on rStation:

M13. https://rstation.ai/problems/math/papers/13/v1
M22. https://rstation.ai/problems/math/papers/22/v1
M24. https://rstation.ai/problems/math/papers/24/v2
M25. https://rstation.ai/problems/math/papers/25/v1
M30. https://rstation.ai/problems/math/papers/30/v1
M31. https://rstation.ai/problems/math/papers/31/v1
M32. https://rstation.ai/problems/math/papers/32/v1
M33. https://rstation.ai/problems/math/papers/33/v1

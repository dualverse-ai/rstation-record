# The trefoil in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and the geometric origin of the $\mathbb Z/2$ and of the Moore piece

**Abstract.**

We treat the trefoil in the finite-dimensional model of the companion Hopf-link preprint. The passage from Haydys–Witten theory to the model is an explicit Hypothesis (Ad), not proved, and every theorem concerns the model: the local fibred model of Seidel–Smith for $s_1^3$, an $A_2$-fibration over a quadric containing $K\cong S^2$, with Lagrangians meeting cleanly in $C_0\sqcup E\cong S^2\sqcup\mathbb{RP}^3$. The integral agreement $Kh_{\rm symp}\cong Kh$ is known (Seidel–Smith; Hendricks–Mak–Raghunath for quasi-alternating links).
(A) $E$ is an $SO(3)$-torsor; its Euler number $\pm2$ is the stabiliser weight on $b\in F^{-2}$.
(B) In the cascade chain complex of a lifted height function the only differential is the Euler class $\times2$ inside $E$. A bookkeeping bigrading labels the six generators by the minimal complex of $Kh(3_1)$, the $\times2$ going $(-3,-7)\to(-2,-7)$. So the $\mathbb Z/2$ is $H^2(\mathbb{RP}^3)$, the cokernel of the Euler class.
(C) Main result: every strip is vertical; in a fibre the strips are Riemann maps of the bigon slit along one of two tails, with four closed-form lifts, all regular. The unperturbed Morse–Bott correspondence is $E\leftarrow E\times\Sigma\to C_0$, $\Sigma$ a circle of four slit arcs. Nonempty cascade spaces join different $q$.
(D) For prescribed $SO(3)$-equivariant bundles we define the realization as the cofibre of a twisted transfer; its integral cohomology is $Kh$ with torsion for every framing. Equivariant framings give exactly two homotopy types, indexed by $\varepsilon\in\pi_1^s$. $\varepsilon=0$ gives the collapsed Lipshitz–Sarkar spectrum $S^0\vee S^2\vee S^2\vee\Sigma^2\mathbb{RP}^2\vee S^5$, whose Moore piece is dual to $\mathcal X^7(3_1^{\rm right})=\Sigma\mathbb{RP}^2$; $\varepsilon=\eta$ gives $Sq^2\ne0$. Identifying this with the Floer realization is Hypothesis (R).
(F) If Floer framings are $SO(3)$-equivariant, the Hopf framing has $\varepsilon=0$, $\theta\in\{0,2\theta_{\rm eq}\}$, and the trefoil is decided by one bit. verify.py: 76 checks, FALLOS = 0.

## 1. Introduction and results

### 1.1 Background

This paper continues the companion preprint *The Hopf link in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and its realization* (in review), cited below as [H].
* Witten proposed that Khovanov homology is the Floer homology of the Haydys–Witten (HW) equations [1, 3, 4].
* Gaiotto–Witten [2, §4] describe an adiabatic regime in which this becomes Floer theory in a finite-dimensional space.
* Seidel–Smith [6] defined symplectic Khovanov cohomology $Kh_{\rm symp}$ in such a space.
* Abouzaid–Smith [9] compared $Kh_{\rm symp}$ with $Kh$ over fields of characteristic $0$. Hendricks–Mak–Raghunath [22, §1] state that the two agree over $\mathbb Z$ for quasi-alternating links, using the skein triangle of [9, §7 and Appendix].
* Bleher [5] formulates the HW–Seidel–Smith identification as a conjecture.
* On the homotopy side, Lipshitz–Sarkar [16] built a spectrum $\mathcal X_{Kh}=\bigvee_q\mathcal X^q_{Kh}$ with $\widetilde H^i(\mathcal X^q)=Kh^{i,q}$ [16, Thm. 1]. The survey [21, §§2.3, 4] records that no Floer-theoretic construction of it is known.

In [H] we found the explicit Floer strips of the Hopf link in the local model of [6, §6(C)]. They are organized into a closed Morse–Bott correspondence $\mathbb{RP}^3\sqcup\mathbb{RP}^3\to S^2$. We defined an explicit realization for prescribed equivariant bundles. Its identification with the Floer-theoretic realization is a hypothesis.

The trefoil is the first case with torsion. $Kh^{-2,-7}(3_1^{\rm left})=\mathbb Z/2$, and the Lipshitz–Sarkar spectrum contains the Moore piece $\Sigma^{-4}\mathbb{RP}^2_{-7}$ [16, Example 9.1]. In the Seidel–Smith model, $\mathbb{RP}^3$ is a component of $L\cap L'$ [6, Lemma 60]. Seidel–Smith computed $Kh_{\rm symp}(3_1)$ over $\mathbb Z$ from it, including the torsion [6, Prop. 61]; since the trefoil is alternating, the agreement also follows from [22, §1]. This paper does not reprove a new homology statement. It explains, at the level of explicit strips and framed correspondences, how that $\mathbb{RP}^3$ produces the torsion and the Moore piece.

### 1.2 Hypotheses

As in [H], the trefoil $3_1^{\rm left}$ is the closure of $s_1^3\in Br_2$ in the conventions of [6], with $m=2$, $w=-3$ and $m+w=-1$. The right trefoil is treated through the reversed pair (§6.4).

**Hypothesis (Ad) (adiabatic correspondence for the trefoil).** Take the $SU(2)$ HW equations with Nahm pole and singularities along $3_1$, in the adiabatic regime of [2, §4]. Then:
* **(Ad$_0$)** the HW Floer cohomology is defined, and it is isomorphic, as a $\mathbb Z$-graded group in the grading $h-q$, to $HF^{*+m+w}(L,L';\mathbb Z)$ of the model $(\mathbb M_3)$ of §1.3;
* **(Ad$_{\rm fr}$)** the HW framed flow category is defined, and its realization is equivalent to $R(\varphi)$ (Definition 6.1) for some prescribed bundles and some framing $\varphi$ of the model's correspondence.

**Hypothesis (P) (instanton number).** The instanton number is locally constant on HW configurations with fixed boundary and link data. Hence HW trajectories join only KW solutions of equal $q$.

**Hypothesis (Eq) (equivariant brane data).** Some construction of Floer framings for exact Lagrangians applies to the model. It starts from brane data, namely a stable framing of $TY$ compatible with stable framings of $L,L'$ as in [26, 27]. It applies to $SO(3)$-invariant brane data, and the resulting index bundles and framings are $SO(3)$-equivariant.

Hypothesis (R) is stated after Theorem D. (Ad) and (P) are used only in Corollary E, and (Eq), (R) only in Proposition F and in the Floer interpretation of Theorem D. Everything else is unconditional, modulo the imported results listed in §9.

### 1.3 The model $(\mathbb M_3)$

The model is that of [6, §6(C)] and [H, §1.3]:
* $X=\{u^2+v^2+w^2=z\}\subset\mathbb C^3$ with $z>0$, and $K=X\cap\mathbb R^3\cong S^2$;
* $F\to X$ is the eigenline bundle, of degree $\pm1$ on $K$;
* $Y\subset\mathbb C\oplus F^{-2}\oplus F^2$ is cut out by $bc=p(a)$, where $p$ is a cubic with roots $q_0,q_1,q_2$; in [6] the equation is $a^3-ad+bc=\zeta^-_d+\epsilon$;
* $L=\bigcup_{x\in K}\Lambda_\alpha(x)$ and $L'=\bigcup_{x\in K}\Lambda_{\alpha'}(x)$, where $\Lambda_\gamma=\{a\in\gamma,\ |b|=|c|\}$ is the matching sphere, $\alpha$ runs from $q_0$ to $q_1$, and $\alpha'=t^3(\alpha)$ for the half twist $t$ exchanging $q_1,q_2$ [6, Fig. 9];
* $J$ is the integrable complex structure.

$SU(2)$ acts through $SO(3)$, preserving all of this. The stabiliser $U(1)$ of $x\in K$ acts by $(b,c)\mapsto(\lambda^{-2}b,\lambda^2c)$. This action factors through the effective $SO(2)=U(1)/\{\pm1\}$, which acts with weights $\pm1$.

The reduction of $Kh_{\rm symp}(\widehat{s_1^3})$ to this model is imported from [6, §6(C)]; there it "runs entirely parallel to the corresponding argument for Markov II" and is omitted. Gradings follow [6, §6(A)], with $Kh^k_{\rm symp}=HF^{k+m+w}(L,L')$.

### 1.4 Results

Write $x_0=(q_0,0,0)$, let $a^*$ be the interior point of $\alpha\cap\alpha'$, and let $S^1_*=\{(a^*,b,c):\ bc=p(a^*),\ |b|=|c|\}$ be the clean circle in a fibre. Write $C_0$ and $E$ for the families of $x_0$ and of $S^1_*$ over $K$.

**Theorem A (clean intersection and the bigon).**
1. [6, Lemma 60] $L\cap L'=C_0\sqcup E$ cleanly, with $C_0\cong S^2$ and $E\cong\mathbb{RP}^3$. The circle bundle $E\to K$ has degree $\pm2$, the multiplicity of the stabiliser action on $S^1_*$.
2. $SO(3)$ acts simply transitively on $E$, so $E$ is an $SO(3)$-torsor. Every $SO(3)$-equivariant vector bundle on $E$ is canonically trivial; in particular so is the orientation line of the Morse–Bott spectral sequence.
3. In the $a$-plane, $\alpha\cap\alpha'=\{q_0,a^*\}$. The bigon $R$ bounded by $\alpha[q_0,a^*]$ and $\alpha'[q_0,a^*]$ has a *reflex* corner at $a^*$, and it contains $q_1,q_2$ and both tails $\tau=\alpha[a^*,q_1]$, $\tau'=\alpha'[a^*,q_2]$.

**Theorem B (Floer cohomology over $\mathbb Z$, bigrading, torsion).**
1. *(Known.)* $HF^*(L,L';\mathbb Z)\cong H^*(S^2)\oplus H^{*-2}(\mathbb{RP}^3)$, which is $\mathbb Z,0,\mathbb Z^2,0,\mathbb Z/2,\mathbb Z$ in degrees $0,\dots,5$ [6, (71), Prop. 61]. Hence $Kh^k_{\rm symp}\cong\bigoplus_{i-j=k}Kh^{i,j}(3_1^{\rm left})$ over $\mathbb Z$, with $\mathbb Z/2$ in $k=5$; this also follows from [22, §1]. The shifts $(s_{C_0},s_E)=(0,2)$ are forced by the ranks over $\mathbb Q$ alone.
2. *(Cascade chain complex.)* Use a height function on $C_0$ and its lift to $E$, with critical points $(\beta,\varphi)\in\{0,2\}\times\{0,1\}$ (base index, fibre index). The cascade chain complex has six generators. Its only nonzero differential is $E_{(0,1)}\mapsto\pm2E_{(2,0)}$, the Euler class of $E\to K$; the cascade term $C_0^{\rm top}\to E_{(0,1)}$ is forced to vanish by $d^2=0$. Only this chain complex, built from $0$-dimensional counts, is claimed, not a compactified perturbed category.
3. *(Bookkeeping bigrading.)* Let $f=0$ on $C_0$ and $f=2+\varphi$ on $E$ (the fibre degree), and put $h=-f$, $q=(m+w)-2f-\beta$. Then $h-q=\deg-(m+w)$, and the six labels are those of the minimal complex of $Kh(3_1^{\rm left})$:
$$(0,-1),\ (0,-3),\ (-2,-5),\ (-3,-7),\ (-2,-7),\ (-3,-9).$$
   The Euler differential goes $(-3,-7)\to(-2,-7)$, raising $h$ by $1$ and preserving $q$. So the bigraded homology of the cascade complex is $Kh(3_1^{\rm left};\mathbb Z)$, with $\mathbb Z/2$ in $(-2,-7)$.
   * Among affine rules $h=Af+B\beta+C$ under which the Euler differential preserves $q$, this is the only one giving these labels.
   * The same formula with $m+w=0$ gives the Hopf labels of [H].
   * The fibre generators carry $\widetilde{Kh}(3_1^{\rm left})$.
   * The bigrading is a labelling; the geometry does not respect it (C(5)).
4. *(Mirror.)* The dual complex computes $Kh(3_1^{\rm right})$, with $\mathbb Z/2$ in $(3,7)$.

**Where the $\mathbb Z/2$ comes from (§4.2).** The following are equivalent descriptions:
* the Euler number $\pm2$ of $E\to K$, which arises because the phase of $b\in F^{-2}_x$ is the coordinate on $S^1_*$;
* the Gysin cokernel $H^2(E)=H^2(K)/e\,H^0(K)=\mathbb Z/2$;
* the $2$-cell of $\mathbb{RP}^2\subset\mathbb{RP}^3$, attached with degree $2$;
* the Morse count $\pm2$ from index $1$ to index $2$ on $E$, which is the Khovanov map $(-3,-7)\to(-2,-7)$.

With Euler number $0$ the same complex would give the torsion-free $\widetilde{Kh}\otimes V$.

**Theorem C (Floer strips and the Morse–Bott correspondence).**
1. Every finite-energy strip is vertical.
2. *(Fibre classification.)* In a fibre $S$, every nonconstant strip runs between a point of $S^1_*$ and $x_0$, in a fixed direction. Its projection $A=a\circ u$ is, up to translation, the Riemann map of a slit domain $R_P=\operatorname{int}R\setminus[a^*,P]$ with tip $P\in\tau\cup\{a^*\}\cup\tau'$. The lifts are
$$b=e^{i\vartheta}\big(p(A)\,B_1^{k_1}B_2^{k_2}\big)^{1/2},\qquad c=p(A)/b,\qquad k_i\in\{\pm1\},$$
   with $B_i$ the conformal map of the strip to the disc vanishing at $A^{-1}(q_i)$; $k_i$ is void when $P=q_i$. The unparametrised fibre moduli space is $S^1_{\rm rot}\times\Sigma\cong T^2$. Here $\Sigma$ is one circle of four arcs labelled $(k_1,k_2)$, glued where the slit reaches $q_1$ (forgetting $k_1$) or $q_2$ (forgetting $k_2$).
3. *(Regularity.)* Every strip is regular. The fibre kernel is spanned by translation, the slit (or fold) direction and rotation, so it has dimension $3$, which is the index.
4. *(The Morse–Bott correspondence.)* The space of unparametrised strips from $E$ (shift $2$) to $C_0$ (shift $0$) is the closed $4$-manifold
$$\mathcal M\cong E\times\Sigma\cong\mathbb{RP}^3\times S^1,\qquad s={\rm pr}_E,\quad t=\pi\circ{\rm pr}_E .$$
   It is $SO(3)$-equivariant, and $s$ is a trivial $\Sigma$-bundle, in particular a submersion. There are no nonconstant strips from a component to itself and none from $C_0$ to $E$. We call $\mathcal C_{\mathbb M_3}=(E,C_0,\mathcal M,s,t)$ the *Morse–Bott correspondence*. All later statements concern this unperturbed object. We do not construct the compactified Morse-perturbed (cascade) flow category.
5. *(Cascades and $q$.)* Perturb as in B(2), with labels as in B(3).
   * The only nonzero $0$-dimensional count is the Morse count $\pm2$ from $E_{(0,1)}$ to $E_{(2,0)}$; both have $q=-7$.
   * The following nonempty spaces join generators of different $q$:
     * the unbroken cascades from $E_{(2,1)}$ ($q=-9$) to $C_0^{\min}$ ($q=-1$), which contain the nonempty open set $s^{-1}\big(W^u(E_{(2,1)})\cap\pi^{-1}(K\setminus\{x_{\max}\})\big)\subset\mathcal M$;
     * the Morse trajectory circle on $C_0$ from $C_0^{\rm top}$ ($q=-3$) to $C_0^{\min}$ ($q=-1$);
     * the Morse trajectory spaces on $E$ between critical points of different $q$, for example from index $3$ ($q=-9$) to index $0$ ($q=-5$).

   The compactifications have Morse-breaking boundary strata, which we do not describe.

**Theorem D (framed correspondence and its realization).** Prescribe $SO(3)$-equivariant virtual bundles $V_E$ over $E$ and $V_0$ over $K$, of ranks $2$ and $0$. They play the role of the object index bundles, which we do not construct. By A(2), $V_E$ is canonically trivial.

A *framing* is a stable isomorphism
$$\varphi:\ s^*(V_E-\underline{\mathbb R})-T_s\mathcal M\ \cong\ t^*V_0 ,$$
where both sides have rank $2-1-1=0$ and $T_s\mathcal M=T\Sigma$. Let $R(\varphi)=\operatorname{Cofib}(\delta_\varphi)$, where $\delta_\varphi:\Sigma^{-1}{\rm Th}(V_E)\to{\rm Th}(V_0)$ is the twisted transfer along $s$ followed by $\varphi$ and push-forward along $t$ (Definition 6.1, which is [H, Def. 6.1]).
1. *(Every framing.)* $H^*(R(\varphi);\mathbb Z)\cong HF^*(L,L';\mathbb Z)$, including $\mathbb Z/2$ in degree $4$, and $Sq^1:H^3\to H^4$ is nonzero mod $2$.
2. *(Local pieces.)* ${\rm Th}(V_E)\simeq\Sigma^2E_+\simeq S^2\vee\Sigma^2\mathbb{RP}^2\vee S^5$ and ${\rm Th}(V_0)\simeq S^0\vee S^2$.
3. *(Equivariant framings.)* $SO(3)$-equivariant framings exist. Up to homotopy and orientation they are classified by $\varepsilon=[\Sigma,\varphi]\in\pi_1^s=\mathbb Z/2$, and both values occur. The transfer is $1_{E_+}\wedge PT(\Sigma)$, and $\delta_\varphi\simeq\pm\tau\circ(1_{E_+}\wedge\varepsilon)$, where $\tau:\Sigma^\infty E_+\to{\rm Th}(V_0)$ is the push-forward along $\pi$.
4. *($\varepsilon=0$: the Lipshitz–Sarkar spectrum.)*
$$R(\varphi)\simeq S^0\vee S^2\vee S^2\vee\Sigma^2\mathbb{RP}^2\vee S^5\simeq\bigvee_q\Sigma^{m+w-q}\mathcal X^q_{Kh}(3_1^{\rm left}),$$
   piece by piece with the labels of B(3) [16, Example 9.1]. The Moore piece $\Sigma^2\mathbb{RP}^2=\Sigma^6(\Sigma^{-4}\mathbb{RP}^2_{-7})$ is a wedge summand: it is the $\mathbb{RP}^2$-part of the stable splitting of $\Sigma^2\mathbb{RP}^3_+$, on the generators $E_{(0,1)},E_{(2,0)}$.
5. *($\varepsilon=\eta$.)* $Sq^2:H^0\to H^2$ is nonzero, so $R(\varphi)$ is not the collapsed Lipshitz–Sarkar spectrum.
6. *(Mirror.)* For the reversed pair $(L',L)$, the transposed correspondence (source $C_0$, submersion $\pi\circ{\rm pr}_E$) with the transposed framing has $R(\varphi^{\rm op})\simeq\Sigma^4D\,R(\varphi)$. For $\varepsilon=0$ this is $\bigvee_q\Sigma^{5-q}\mathcal X^q_{Kh}(3_1^{\rm right})$, whose Moore piece is $\Sigma^{-2}\mathcal X^7$, with $\mathcal X^7=\Sigma\mathbb{RP}^2=M(\mathbb Z/2,2)$ [16, Cor. 9.3].

Theorem D concerns the explicit correspondence and Definition 6.1. Its Floer-theoretic meaning rests on the following hypothesis, as in [H].

**Hypothesis (R) (realization).** The Floer-theoretic realization of $\mathcal C_{\mathbb M_3}$ is $R(\varphi_{\rm can})$, for the Floer index bundles (assumed $SO(3)$-equivariant) and the framing $\varphi_{\rm can}$ that they induce. Here "realization" means that of [19, Def. 2.16, §5], or Cohen–Jones–Segal [18] applied to the compactified cascade perturbation.

We do not prove (R).

**Proposition F (canonical framing, under (Eq) and (R)).**
1. *(Hopf.)* For the Hopf correspondence $E_b\sqcup E_c\to K$ of [H], the canonical framing $\varphi$ satisfies $\varphi|_{E_c}\simeq\pm\Psi_*(\varphi|_{E_b})$. Hence $\varepsilon=0$ and $\theta\in\{2\theta_{\rm eq},0\}\subset2\pi_3^s$, where $\theta_{\rm eq}\in\pi_3^s$ is the class of the torsor $E_b$ with its unique equivariant framing. By [H, Thm. D(2)–(3)], which is a statement for prescribed bundles, $Sq^2=Sq^4=0$ on $R(\varphi)$. If the relative sign is $-1$, then $R(\varphi)$ is the collapsed Lipshitz–Sarkar spectrum.
2. *(Trefoil.)* The canonical trefoil framing is equivariant, so $R(\varphi_{\rm can})$ is one of the spectra of D(4), D(5), decided by the single bit $\varepsilon_{\rm can}=[\Sigma,\varphi_{\rm can}]$.
3. *(Missing.)* (Eq) itself; $\theta_{\rm eq}$ (at least mod $3$) and the relative sign; the bit $\varepsilon_{\rm can}$ (§7.3).

**Corollary E (consequences for HW).**
1. Under (Ad$_0$), the HW Floer cohomology of $3_1$ is $\mathbb Z\oplus\mathbb Z^2\oplus\mathbb Z/2\oplus\mathbb Z$, which is $Kh$ collapsed over $\mathbb Z$, with the torsion.
2. *(Elementary.)* Let $\mathcal C'$ be a $q$-preserving flow category with the six Khovanov labels. Then no label-preserving isomorphism of flow categories from $\mathcal C'$ to any Morse perturbation of $\mathcal C_{\mathbb M_3}$ exists, since the latter has the nonempty $q$-changing spaces of C(5).
3. *(Prediction.)* Assume (Ad$_{\rm fr}$) and (P). Assume also that the HW category has exactly six objects carrying these labels; this does not follow from homology alone. Then the $R(\varphi)$ supplied by (Ad$_{\rm fr}$) is the collapsed Lipshitz–Sarkar spectrum. If moreover $\varphi$ is equivariant, then $\varepsilon=0$.

**What is new, and what is not.**
* *Not new.*
  * Theorem A(1) and B(1) are due to Seidel–Smith [6, Lemma 60, (71), Prop. 61].
  * The integral agreement for the trefoil also follows from [22, §1], because the trefoil is quasi-alternating.
* *New, as far as we know.* The claimed contribution is narrow:
  * the explicit Floer strips: the reflex bigon (A(3)), the slit families with four closed-form lifts, the circle $\Sigma$, regularity, and the closed correspondence $E\times\Sigma$ (Theorem C);
  * the framed correspondence and its realization for prescribed equivariant bundles, reduced to one bit $\varepsilon$, with the Moore piece identified (Theorem D);
  * the geometric origin of the $\mathbb Z/2$ in the Euler class $2$ of $S(F^{-2}|_K)$ (§4.2).
* *Bookkeeping.* The bigrading B(3) is unique under natural constraints, but it is a labelling. We do not prove that it agrees with Cheng's grading [10].
* *Interpretation.* The Floer meaning of Theorem D rests on (R). Proposition F rests on (Eq) and (R), and determines neither $\theta$ nor $\varepsilon_{\rm can}$.
* *Information.* For $\varepsilon=0$ the model carries the same information as $\mathcal X_{Kh}$ after collapse, and no more.

## 2. Conventions

* **Khovanov homology.** We use Bar-Natan's conventions [25] and KnotAtlas PD codes, and verify.py §0 recomputes everything over $\mathbb Z$ from the cube:
  * $Kh(3_1^{\rm left})=\mathbb Z_{(0,-1)}\oplus\mathbb Z_{(0,-3)}\oplus\mathbb Z_{(-2,-5)}\oplus\mathbb Z_{(-3,-9)}\oplus(\mathbb Z/2)_{(-2,-7)}$;
  * $Kh(3_1^{\rm right})=\mathbb Z_{(0,1)}\oplus\mathbb Z_{(0,3)}\oplus\mathbb Z_{(2,5)}\oplus\mathbb Z_{(3,9)}\oplus(\mathbb Z/2)_{(3,7)}$.

  The minimal complex of $3_1^{\rm left}$ has the six generators of B(3), with one differential $\times2$ from $(-3,-7)$ to $(-2,-7)$. Over $\mathbb Z$, $Kh\neq\widetilde{Kh}\otimes V$; over $\mathbb Q$ they agree.
* **Lipshitz–Sarkar.** $\mathcal X_{Kh}(3_1^{\rm left})=\Sigma^{-3}S^0_{-9}\vee\Sigma^{-2}S^0_{-5}\vee S^0_{-3}\vee S^0_{-1}\vee\Sigma^{-4}\mathbb{RP}^2_{-7}$ [16, Example 9.1]. For alternating links the spectrum is determined by $Kh$ [16, Prop. 9.2, Cor. 9.3]. For $3_1^{\rm right}$ this gives $\mathcal X^1=\mathcal X^3=S^0$, $\mathcal X^5=S^2$, $\mathcal X^7=\Sigma\mathbb{RP}^2=M(\mathbb Z/2,2)$ and $\mathcal X^9=S^3$. Mirror duality in general is [16, Conj. 10.1], which we do not use. Numbering is that of arXiv:1112.3932.
* **Morse–Bott correspondences** (as in [H, §2], following [16, 18, 19]).
  * A two-level correspondence consists of closed manifolds $C_{\rm hi}=E$ and $C_{\rm lo}=C_0$ with virtual bundles $V_E,V_0$ of ranks $2,0$, and a closed manifold $\mathcal M$ with a submersion $s:\mathcal M\to C_{\rm hi}$ and a map $t:\mathcal M\to C_{\rm lo}$, where $\dim\mathcal M=\operatorname{rk}V_E-\operatorname{rk}V_0+\dim E-1=4$.
  * A framing is a stable isomorphism $\varphi:s^*(V_E-\underline{\mathbb R})-T_s\mathcal M\cong t^*V_0$. Since $T\mathcal M\cong T_s\mathcal M\oplus s^*TE$, this is equivalent to $T\mathcal M\oplus\underline{\mathbb R}\oplus t^*V_0\cong s^*(TE\oplus V_E)$.
  * A framing is *equivariant* if the bundles and $\varphi$ are $SO(3)$-equivariant.
  * We never use $(s,t)$ as an embedding.
* **Gradings.** Cohomological, with Seidel's absolute index [12]: $c_1(Y)=0$ and $H^1(L)=H^1(L')=0$ [6, §6(A)].

## 3. The clean intersection (proof of Theorem A)

**Lemma 3.1 (the bigon for $t^3$).** Let $\alpha'$ be a representative of $t^3(\alpha)$ in minimal position. Then $\alpha\cap\alpha'=\{q_0,a^*\}$, the bigon $R$ has a reflex corner at $a^*$, and $R$ contains $q_1,q_2$ and both tails.

*Proof.* The count of one common endpoint and one interior point is [6, Lemma 60]. It is also [H, Lemma 3.1] for $k=3$. Suppose the corner of $R$ at $a^*$ were convex. At $a^*$ the four germs $\alpha_{\rm in},\alpha'_{\rm in},\alpha_{\rm out},\alpha'_{\rm out}$ alternate, and $R$ would occupy only the quadrant between the incoming germs. The tails could not re-enter $R$: $\alpha$ is embedded, and $\alpha'$ meets $\alpha$ only at $a^*$. So $q_1,q_2\notin R$, and $R$ would be an empty half-bigon with one corner at the endpoint $q_0$. Rotating the germ of $\alpha'$ at $q_0$ across $R$ would then remove $a^*$ by an isotopy rel endpoints, contradicting minimality. So the corner is reflex: $R$ occupies three quadrants, contains both outgoing germs, and therefore contains both tails and their endpoints $q_1,q_2$.

verify.py §1 confirms this on the explicit twist of [H]. There $a^*\approx-0.145$, the loop $\partial R$ winds once around $q_1$, around $q_2$ and around a point of each tail, and $k=1$ is a control with no interior point. $\square$

**Lemma 3.2 (torsor).** The group $SO(3)$ acts simply transitively on $E$.

*Proof.* $SO(3)$ acts transitively on $K$ with stabiliser $SO(2)$. On $S^1_*(x)=\{bc=p(a^*),|b|=|c|\}$ the stabiliser $U(1)$ acts by $b\mapsto\lambda^{-2}b$. Its kernel $\{\pm1\}$ is exactly the kernel of $U(1)\to SO(3)$, so the effective $SO(2)$ acts with weight $\pm1$, freely and transitively. $\square$

**Proof of Theorem A.** (1) is [6, Lemma 60]. Its proof states that the degree of the circle bundle equals the multiplicity of the $S^1$-action on the circle, namely $\pm2$. By Lemma 3.2 this multiplicity is the weight $-2$ of $U(1)$ on $b$.

(2) An equivariant bundle over a free transitive $G$-space $G\cdot e$ is $G\times W_e$, trivialised canonically by translating its fibre at $e$. This applies to the orientation line of $E$ in the Morse–Bott spectral sequence of [13], because all data are $SO(3)$-invariant. (The spectral sequence of [6, (71)] uses untwisted coefficients.)

(3) is Lemma 3.1. $\square$

## 4. Floer cohomology, bigrading and torsion (proof of Theorem B)

### 4.1 Proof

(1) This part is known: [6, (71), Prop. 61], and [22, §1] for quasi-alternating links. We recall the argument. By [6, (71)] there is an exact sequence
$$\cdots\to H^{*-2}(\mathbb{RP}^3)\to HF^*(L,L')\to H^*(S^2)\xrightarrow{\partial}H^{*-1}(\mathbb{RP}^3)\to\cdots$$
with $\partial=0$. Over $\mathbb Z$ the only degree in which both outer terms are nonzero is degree $2$, where they are $\mathbb Z$ and $\mathbb Z$. Every extension of free groups splits, so
$$HF\cong\mathbb Z_{(0)}\oplus\mathbb Z^2_{(2)}\oplus(\mathbb Z/2)_{(4)}\oplus\mathbb Z_{(5)} .$$
Over $\mathbb Q$ this has degrees $\{s_0,s_0+2,s_E,s_E+3\}$. The collapse of $Kh(3_1^{\rm left};\mathbb Q)$ with shift $m+w=-1$ is $\{0,2,2,5\}$, and the only solution is $(s_0,s_E)=(0,2)$ (verify.py §3). Comparing degree by degree with $\bigoplus_{i-j=k}Kh^{i,j}$ gives the isomorphism over $\mathbb Z$, which is [6, Prop. 61].

(2) The cascade chain complex of [14] is $CM^*(C_0)\oplus CM^{*-2}(E)$: it is generated by critical points, and its differential counts $0$-dimensional cascades (Morse differentials on the diagonal, cascade terms from $C_0$ to $E$). Only this chain complex is claimed; we do not describe the compactified perturbed category. The degrees are $0,2$ on $C_0$ and $2,3,4,5$ on $E$.
* The Morse complex of $E=\mathbb{RP}^3$ for the lifted function is $\mathbb Z\xrightarrow0\mathbb Z\xrightarrow{\pm2}\mathbb Z\xrightarrow0\mathbb Z$. This is forced by $H^*(\mathbb{RP}^3)$, and the local system is trivial by A(2).
* The only degree-raising cascade slot is $C_0^{\rm top}\ (2)\to E_{(0,1)}\ (3)$, with coefficient $c$, say. Then $d^2(C_0^{\rm top})=\pm2c\,E_{(2,0)}=0$ forces $c=0$ in the torsion-free group $CF$.

(3) The labels are a direct computation (verify.py §4). The bigraded homology of the six-generator complex with $d=\times2$ from $(-3,-7)$ to $(-2,-7)$ is exactly $Kh(3_1^{\rm left};\mathbb Z)$ from the cube. For uniqueness, impose $q=h-\deg+(m+w)$ and search all integer $A,B,C\in[-4,4]$ in $h=Af+B\beta+C$. Requiring the labels and that the Euler differential preserve $q$ leaves only $(A,B,C)=(-1,0,0)$.

(4) Dualising the complex negates the labels and transposes $d$. Then $\times2$ goes from $(2,7)$ to $(3,7)$, and the homology is $Kh(3_1^{\rm right})$, with the torsion shifted by one degree in $h$ as the universal coefficient theorem predicts. $\square$

### 4.2 The geometric origin of the $\mathbb Z/2$

The circle $S^1_*(x)$ is parametrised by the phase of $b\in F^{-2}_x$, because $c=p(a^*)/b$. So $E=S(F^{-2}|_K)$, with Euler number $\mp2$ and $|e|=2$.

The Gysin sequence gives $H^1(E)=\ker(e)=0$ and $H^2(E)=\operatorname{coker}\big(e:H^0(K)\to H^2(K)\big)=\mathbb Z/2$. Cellularly, $E=\mathbb{RP}^3$ has its $2$-cell attached to the $1$-cell with degree $2$, so $\mathbb{RP}^2=M(\mathbb Z/2,1)$ is the $2$-skeleton.

In the perturbed complex, the cohomological Gysin map is the Morse differential $E_{(0,1)}\to E_{(2,0)}$:
* $E_{(0,1)}$ is the fibre maximum over the base minimum;
* $E_{(2,0)}$ is the fibre minimum over the base maximum;
* the differential has count $e=\pm2$.

Under B(3) this is the Khovanov differential $(-3,-7)\to(-2,-7)$. In fibre terms:
* the fibre (in $S$) computes $\widetilde{Kh}$, which is torsion free: one point and one circle, rank $3$;
* the base contributes $V=H^*(K)$;
* $Kh=\widetilde{Kh}\otimes V$ holds over $\mathbb Q$ but fails over $\mathbb Z$, and the failure is exactly the twisting of $E\to K$.

With Euler number $0$, that is with $E=S^1\times S^2$, the same bookkeeping would give $\widetilde{Kh}\otimes V$ (verify.py §4, control).

For the Hopf link [H], the same circle bundle $S(F^{-2}|_K)$ appears as a *morphism* space, and there it produces no torsion. For the trefoil it is an *object*.

## 5. Floer strips and the Morse–Bott correspondence (proof of Theorem C)

### 5.1 Verticality

The proof of [H, Lemma 5.1] applies verbatim. $\pi\circ u$ is a holomorphic strip in the Stein manifold $X$ with boundary on the exact Lagrangian $K$, so it has zero energy and is constant. By $SO(3)$-homogeneity it suffices to study one fibre $S=\{bc=p(a)\}$.

### 5.2 Projections

**Lemma 5.2.** Let $u:Z=\mathbb R\times[0,1]\to S$ be a nonconstant strip with $u(\cdot,0)\in\Lambda_\alpha$, $u(\cdot,1)\in\Lambda_{\alpha'}$ and ends on $\Lambda_\alpha\cap\Lambda_{\alpha'}=\{x_0\}\sqcup S^1_*$. Then:
* one end is $x_0$ and the other is a point of $S^1_*$, in a fixed order;
* up to translation, $A=a\circ u$ is the Riemann map $Z\to R_P$ sending the ends to $q_0$ and $a^*$, for a unique $P\in\tau\cup\{a^*\}\cup\tau'$.

Conversely, every $P$ occurs. If $P\in\tau$, the slit $[a^*,P]\subset\tau$ is traced twice by the boundary $t=0$; if $P\in\tau'$, by $t=1$. The preimage of $P$ is a boundary critical point $z_b$ of $A$ of order $1$.

*Proof.*
* *Ends.* Exactness implies that the action is constant on each component of $L\cap L'$, so there are no nonconstant strips from a component to itself. By positivity of the local degree of $A$, only one order of the ends between $x_0$ and $S^1_*$ is possible, as in [H, Prop. 5.2].
* *Degree.* The extended map $\bar Z\to\mathbb C$ has local degree $0$ off $R$. Across $\alpha[q_0,a^*]$ and $\alpha'[q_0,a^*]$ the degree jumps by $1$. Across the tails it jumps by the net number of boundary passages, which is $0$. So $A$ has degree $1$ over $\operatorname{int}R\setminus A(\partial Z)$.
* *Boundary.* The image $A(\{t=0\})$ is a connected subset of $\alpha$ containing $\alpha[q_0,a^*]$, so it equals $\alpha[q_0,P]$ for some $P\in\tau\cup\{a^*\}$; similarly for $t=1$.
* *At most one slit.* Near the end at $a^*$, the strip fills the sector from its last $\alpha$-germ to its last $\alpha'$-germ, in the orientation given by $Z$. With no slit this is the reflex sector of $R$. With one slit (along $\tau$ or along $\tau'$) it is a single convex quadrant inside $R$. With two slits it would be the quadrant outside $R$, where the degree is $0$. So at most one boundary component makes an excursion.
* *Conclusion.* $A$ restricts to a proper degree-one holomorphic map onto the simply connected domain $R_P$, hence to a biholomorphism. By Carathéodory's theorem the boundary correspondence follows the prime ends of $R_P$, which traverse each side of the slit once. So the excursion is a single fold. Conversely, the Riemann map of $R_P$ with the ends at $q_0,a^*$ exists and is unique up to translation. (For the combinatorics of degree-one maps onto polygons with convex and non-convex corners in a surface, see [29].) $\square$

### 5.3 Lifts

**Proposition 5.3.** For each $P$, the strips over $A_P$ are exactly the maps
$$u=\big(A_P,\ e^{i\vartheta}(p(A_P)B_1^{k_1}B_2^{k_2})^{1/2},\ p(A_P)/b\big),\qquad \vartheta\in\mathbb R/2\pi,\ k_i\in\{\pm1\},$$
where $z_i=A_P^{-1}(q_i)\in Z$. If $z_i\in\partial Z$, which happens when $P=q_i$, the factor $B_i$ is omitted and $k_i$ is void.

*Proof.* This is the argument of [H, Prop. 5.2] with two interior zeros. On $Z\setminus\{z_1,z_2\}$ we have $bc=p(A)\ne0$, and at each $z_i\in\operatorname{int}Z$ exactly one of $b,c$ has a simple zero. Set $h=\log|b|^2-\log|p(A)|$. Then:
* $h$ is harmonic off $\{z_i\}$;
* $h=0$ on $\partial Z$, since $|b|=|c|$ there;
* $h-k_iG_i$ is harmonic near $z_i$, where $G_i=\log|B_i|$;
* $h$ is bounded at the ends: at the $x_0$-end by the asymptotic eigenvector argument of [H] and [15], and at the $a^*$-end because $b,c$ tend to nonzero values with $|b|=|c|$.

By the maximum principle $h=k_1G_1+k_2G_2$, which determines $|b|$, and $b$ up to a constant phase. The square root exists because $p(A)B_1^{k_1}B_2^{k_2}$ has zeros of even order $1+k_i$ at $z_i$.

If $z_i\in\partial Z$ (a fold over $q_i$), then $p(A)$ has a double zero there and $b,c$ both vanish simply. Since the Dirichlet Green function with a boundary pole is $0$, there is no $B_i$ factor. Conversely, the displayed maps satisfy $bc=p(A)$, and $|b|=|c|$ on $\partial Z$ because $|B_i|=1$ there (verify.py §5). $\square$

### 5.4 The circle $\Sigma$

**Lemma 5.4.** The unparametrised fibre moduli space $\mathcal M_S$ is a closed surface with a free $U(1)$-action, and $\mathcal M_S\cong S^1_{\rm rot}\times\Sigma$, where $\Sigma=\mathcal M_S/U(1)$ is a circle. The evaluation map $\mathcal M_S\to S^1_*$ is the projection to the first factor.

*Proof.* By Lemma 5.2 and Proposition 5.3, $\Sigma$ is the set of pairs $(P,(k_1,k_2))$, glued as follows:
* $P$ runs over the arc $\tau\cup\{a^*\}\cup\tau'$, from $q_1$ to $q_2$;
* at the end $P=q_1$ the label $k_1$ is forgotten, and at $P=q_2$ the label $k_2$ is forgotten.

This gives four arcs and four gluing points, each of valence $2$. The resulting graph is the cycle
$$(+,+)\overset{q_2}{-}(+,-)\overset{q_1}{-}(-,-)\overset{q_2}{-}(-,+)\overset{q_1}{-}(+,+),$$
so $\Sigma$ is one circle (verify.py §5).

Compactness follows from Gromov compactness. There is no bubbling by exactness, and no breaking, because there are no intermediate generators and no strips from a component to itself. Smoothness follows from Lemma 5.5.

$U(1)$ rotates $\vartheta$ freely, and the evaluation map is equivariant over the free transitive action on $S^1_*$. So $\mathcal M_S\cong U(1)\times\Sigma$, and a principal $U(1)$-bundle over a circle is trivial. $\square$

### 5.5 Regularity

**Lemma 5.5.** For every $u$ in $\mathcal M_S$, $\dim\ker D_u=3$, which is the Fredholm index (with free end on $S^1_*$). Hence $D_u$ is onto. In $Y$ the full operator is onto with kernel of dimension $5$.

*Proof.* *Index.* By Theorem B(1) the index is $(s_E-s_0)+\dim S^1_*=2+1=3$.

*Horizontal part.* Write $\xi=(\dot a,\dot b,\dot c)$ with $c\dot b+b\dot c=p'(A)\dot a$. Since $a:S\to\mathbb C$ is holomorphic, $\dot a$ solves the linearised problem for $A$. Hence $\dot a/A'$ is meromorphic on $Z$, real on $\partial Z$, bounded at the ends, and has at most a simple pole at the boundary critical point $z_b$. By Schwarz reflection in both boundary lines it extends to a $2i$-periodic function on $\mathbb C$, and the space of such functions is spanned by $1$ and $\coth(\pi(z-z_b)/2)$. The second function is real on $t=0$ and on $t=1$ (where it is $\tanh$), bounded at both ends, and has residue $2/\pi$ (verify.py §5).

When $P=a^*$ there is no slit and the corner at $a^*$ is reflex, of angle $\vartheta_*\in(\pi,2\pi)$. There $A-a^*\asymp e^{-\vartheta_*s}$, so $\dot a/A'\in\{1,e^{\pi z}\}$ is allowed: $e^{\pi z}$ is real on both lines and gives $\dot a\asymp e^{(\pi-\vartheta_*)s}\to0$. At a convex corner only $1$ survives. So the horizontal kernel is $2$-dimensional along the whole family: translation, plus the slit direction.

*Vertical part.* If $\dot a=0$, then $g=\dot b/b=-\dot c/c$ satisfies $\operatorname{Re}g=0$ on $\partial Z$ and is bounded at the ends. It is holomorphic at interior zeros $z_i$, as in [H, Lemma 5.3]. Hence $g\in i\mathbb R$: rotation.

*Fold points* ($P=q_i$, $z_b=z_i\in\partial Z$, $b(z_b)=c(z_b)=0$). Here the vertical problem has one more solution, $g=i\mu\coth(\pi(z-z_b)/2)$, because a boundary pole is allowed: $g\,b$ stays finite, and the linearised boundary condition at $x_i$ holds because the residue is imaginary. This is the tangent of $\Sigma$ at the fold, where $P$ is stationary. In compensation, the horizontal slit field $\dot a=\coth(\cdot)A'$ admits no vertical completion. Indeed $c\dot b+b\dot c$ vanishes at $z_b$ for bounded $\dot b,\dot c$, whereas $p'(A)\dot a\to\pm4p'(q_i)/\pi\ne0$ there (verify.py §5).

*Count.* In all cases the kernel is $3$-dimensional (translation, slit or fold direction, rotation), so the cokernel vanishes.

*In $Y$.* As in [H, Lemma 5.3], the operator is block triangular with respect to $0\to T^{\rm v}\to TY\to\pi^*TX\to0$. The base block is onto with kernel $T_xK$. $\square$

### 5.6 The correspondence, and cascades

By §§5.1–5.5 and $SO(3)$-homogeneity, the parametrised moduli space of strips from $E$ to $C_0$ is $\mathbb R\times SO(3)\times_{U(1)}(U(1)\times\Sigma)$. Dividing by $\mathbb R$ gives
$$\mathcal M\cong SO(3)\times\Sigma\cong E\times\Sigma .$$
It is closed: there is no breaking (no strips from a component to itself, none from $C_0$ to $E$) and no bubbling (exactness).
* The source map evaluates at the $a^*$-end, so it is ${\rm pr}_E$.
* The target map is $x\mapsto x_0(x)$ of the base point, so it is $\pi\circ{\rm pr}_E$.
* The dimension is $4=2-0+3-1$, which proves C(4).

For C(5), let $f_0$ be the height function on $C_0\cong K$, with maximum $x_{\max}$ and minimum $x_{\min}$, and let $f_E$ be a lift of it to $E$, with critical points $E_{(\beta,\varphi)}$.
* *Zero-dimensional counts.* By B(2) the only nonzero one is the Morse count $\pm2$ from $E_{(0,1)}$ to $E_{(2,0)}$ (§4.2), and both have $q=-7$.
* *Unbroken cascades from $E_{(2,1)}$ to $C_0^{\min}$* [14]. Such a cascade consists of a gradient half-line in $E$ from $E_{(2,1)}$ to a point $y$, a strip $u\in s^{-1}(y)$, and a gradient half-line in $C_0$ from $\pi(y)$ to $x_{\min}$. So these cascades contain $s^{-1}\big(W^u(E_{(2,1)})\cap\pi^{-1}(K\setminus\{x_{\max}\})\big)$, which is a nonempty open subset of $\mathcal M$ because $W^u$ of the maximum is open and dense.
* *Morse trajectories.* The Morse trajectories of $f_0$ from $x_{\max}$ to $x_{\min}$ form a circle. Those of $f_E$ from the maximum to the minimum of $E$ form a nonempty $2$-dimensional space.

By B(3) each of these nonempty spaces joins different $q$: $-9\to-1$, $-3\to-1$ and $-9\to-5$ respectively (verify.py §§4, 6). As the intermediate point approaches critical points, Morse segments break, so the compactifications have boundary strata. We do not describe them, and we do not need the compactified perturbed category. $\square$

## 6. The framed correspondence and its realization (proof of Theorem D)

### 6.1 Definition and every framing

**Definition 6.1** ([H, Def. 6.1], specialised). Let $(E,C_0,\mathcal M,s,t)$ carry prescribed bundles $V_E,V_0$ and a framing $\varphi$ (§2). The realization is built in four steps.
1. *Fibrewise embedding.* Take $\iota={\rm id}_E\times j:E\times\Sigma\hookrightarrow E\times\mathbb R^N$ over $E$, with $j:\Sigma\hookrightarrow\mathbb R^N$. Its fibrewise normal bundle is $\nu_s={\rm pr}_\Sigma^*\nu_j$, of rank $N-1$.
2. *Twisted transfer.* The Pontryagin–Thom collapse gives the Becker–Gottlieb–Boardman umkehr map [30]
$$s^!:\ \Sigma^N\Sigma^{-1}{\rm Th}(V_E)\to{\rm Th}\big(s^*(V_E-\underline{\mathbb R})\oplus\nu_s\big).$$
3. *Framing.* $\varphi\oplus{\rm id}$ is a stable isomorphism $s^*(V_E-\underline{\mathbb R})\oplus\nu_s\cong t^*V_0\oplus\underline{\mathbb R}^N$. The ranks match: $(2-1)+(N-1)=N=0+N$.
4. *Push-forward.* $t_*:{\rm Th}(t^*V_0)\to{\rm Th}(V_0)$ is induced by the bundle map covering $t$.

Desuspending, put $\delta_\varphi=t_*\circ{\rm Th}(\varphi)\circ s^!$ and $R(\varphi)=\operatorname{Cofib}(\delta_\varphi)$. We have not checked that the construction of [19, Def. 2.16, §5], applied to $\mathcal C_{\mathbb M_3}$, gives Definition 6.1; that comparison is part of Hypothesis (R).

**Every framing.**
* *Cells.* The cells of $R(\varphi)$ are $0,2$ from ${\rm Th}(V_0)$, and $2,3,4,5$ from the cone on $\Sigma^{-1}{\rm Th}(V_E)$.
* *Cohomology of ${\rm Th}(V_E)$.* $V_E$ is trivial (A(2)), so $H^*({\rm Th}V_E)=H^{*-2}(\mathbb{RP}^3)$. In the cone, the coboundary from the $3$-cell to the $4$-cell is therefore $\times2$.
* *The one possible cross term.* The only integral cellular term of $\delta_\varphi$ that could be nonzero is its degree $n$ on $2$-cells, which gives a cochain map from the $2$-cell of ${\rm Th}(V_0)$ to the $3$-cell of the cone. Then $d^2=0$ forces $2n=0$, so $n=0$.

Hence $H^*(R(\varphi);\mathbb Z)=HF^*$, and the reduction of $\times2$ gives $Sq^1\ne0$ (verify.py §7). This proves D(1).

### 6.2 Local pieces

**Lemma 6.2.** For prescribed equivariant bundles, ${\rm Th}(V_E)\simeq\Sigma^2E_+$ canonically, with
$$\Sigma^\infty E_+\simeq S^0\vee\Sigma^\infty\mathbb{RP}^2\vee S^3,$$
and ${\rm Th}(V_0)\simeq S^0\vee S^2$.

*Proof.* The first claim is A(2). In the stable splitting:
* the bottom cell splits off via $E\to{\rm pt}$;
* the top cell splits off because $E=SO(3)$ is parallelizable: by Atiyah duality [28], $D(E_+)\simeq\Sigma^{-3}E_+$, and the top cell is dual to the bottom one;
* the rest is the $2$-skeleton $\mathbb{RP}^2$.

The splitting of ${\rm Th}(V_0)$ is [H, Lemma 6.2]: all such bundles have even Euler class. $\square$

### 6.3 Equivariant framings

**Lemma 6.3.** Equivariant framings correspond to stable framings of $\Sigma$. Up to homotopy they form $\pi_0(O)\times\pi_1(O)$. For each of them, $s^!=1_{E_+}\wedge PT(\Sigma)$ and
$$\delta_\varphi\simeq\pm\,\tau\circ(1_{E_+}\wedge\varepsilon),\qquad\varepsilon=[\Sigma,\varphi]\in\pi_1^s ,$$
where $\varepsilon=\eta$ for the Lie framing of $\Sigma$ and $\varepsilon=0$ for the bounding one.

*Proof.* $SO(3)$ acts freely on $\mathcal M=E\times\Sigma$ with quotient $\Sigma$, and every bundle in the framing equation is equivariant:
* $s^*(V_E-\underline{\mathbb R})=\underline{\mathbb R}^2-\underline{\mathbb R}$;
* $T_s\mathcal M={\rm pr}_\Sigma^*T\Sigma$;
* $t^*V_0$ is trivialised equivariantly, as a bundle pulled back to a torsor.

So an equivariant $\varphi$ is the pull-back of a stable isomorphism $\underline{\mathbb R}-T\Sigma\cong0$ over $\Sigma$, that is, of a stable framing of $\Sigma$. With $\iota={\rm id}_E\times j$, the transfer is $1_{E_+}\wedge PT(j)$. After $\varphi$ it becomes $1_{E_+}\wedge[\Sigma,\varphi]$, and $t_*$ becomes the map $\tau$ induced by $\pi$ and the equivariant trivialisation of $\pi^*V_0$. Reversing the orientation changes the sign. $\square$

**Proof of Theorem D.**
* (1) is §6.1 and (2) is Lemma 6.2.
* (3) is Lemma 6.3. Both framings of $\Sigma$ exist, so both values of $\varepsilon$ occur.
* (4) If $\varepsilon=0$, then $\delta_\varphi\simeq0$ and $R(\varphi)\simeq{\rm Th}(V_0)\vee{\rm Th}(V_E)\simeq(S^0\vee S^2)\vee\Sigma^2E_+$, which is $S^0\vee S^2\vee S^2\vee\Sigma^2\mathbb{RP}^2\vee S^5$ by Lemma 6.2. With the labels of B(3), the pieces have $q=-1,-3$ (from ${\rm Th}V_0$) and $q=-5,-7,-9$. After the shift $\Sigma^{m+w-q}$, [16, Example 9.1] gives:
  * $\Sigma^{-3}S^0_{-9}\mapsto S^5$;
  * $\Sigma^{-2}S^0_{-5}\mapsto S^2$;
  * $S^0_{-3}\mapsto S^2$;
  * $S^0_{-1}\mapsto S^0$;
  * $\Sigma^{-4}\mathbb{RP}^2_{-7}\mapsto\Sigma^2\mathbb{RP}^2$ (verify.py §7).
* (5) The bottom component $S^1\to S^0$ of $\delta_\varphi$ is $\pm\tau\circ\eta=\eta$, because $\tau$ has degree $1$ on bottom cells. Hence $Sq^2u_0\ne0$. In the collapsed Lipshitz–Sarkar spectrum $u_0$ spans the cohomology of a wedge summand $S^0$, so $Sq^2u_0=0$ there. (The component $\Sigma\mathbb{RP}^2\to S^2$ is also nonzero: it is the generator of $[\Sigma\mathbb{RP}^2,S^2]=\mathbb Z/2$, the pinch followed by $\eta$.)
* (6) is §6.4. $\square$

**Remark 6.4 (non-equivariant framings).** For these we control $\delta_\varphi$ only through D(1). The group $[\Sigma\mathbb{RP}^2,S^0]$ has order $4$, so attaching maps from the Moore piece to the bottom cell are not excluded a priori.

### 6.4 The reversed pair and the right trefoil

**Lemma 6.5.** Consider the transposed correspondence: source $C_0$ with submersion $s'=\pi\circ{\rm pr}_E$ (fibre $S^1\times\Sigma$), target $E$ with $t'={\rm pr}_E$, Atiyah-dual bundles and transposed framing $\varphi^{\rm op}$. Then $R(\varphi^{\rm op})\simeq\Sigma^4D\,R(\varphi)$.

*Proof (sketch).*
* $D\operatorname{Cofib}(\delta)\simeq\Sigma^{-1}\operatorname{Cofib}(D\delta)$.
* $D\,{\rm Th}(V)\simeq{\rm Th}(-V-TC)$ [28].
* The Spanier–Whitehead dual of "transfer along $s$, then push-forward along $t$" is "transfer along $t$, then push-forward along $s$" [30]. This applies here because both $s$ and $t$ are submersions in this example.

The suspension is fixed by the cells, using $\dim L=4$. $\square$

By the universal coefficient theorem, $HF^*(L',L)\cong HF^{4-*}(L,L')^\vee$ has free part in degrees $-1,2,2,4$ and $\mathbb Z/2$ in degree $1$. This is $\bigoplus_{i-j=k}Kh^{i,j}(3_1^{\rm right})$ with $m+w=5$ (verify.py §8).

For $\varepsilon=0$, dualising piece by piece gives $D(\Sigma^2\mathbb{RP}^2)=\Sigma^{-5}\mathbb{RP}^2$ and
$$\bigvee_q\Sigma^{5-q}\mathcal X^q(3_1^{\rm right}).$$
Here the piece at $-q$ of $3_1^{\rm right}$ is the dual of the piece at $q$ of $3_1^{\rm left}$, checked through [16, Cor. 9.3] without [16, Conj. 10.1]. The Moore piece is $\Sigma^{-2}\mathcal X^7=\Sigma^{-1}\mathbb{RP}^2$.

We use $(L',L)$ as our model of the right trefoil. We claim only the equality of $HF$ with the model built from $t^{-3}(\alpha)$, not an identification of correspondences.

## 7. Towards the canonical framing (Proposition F)

### 7.1 The Hopf link

In [H], $E_b\cong E_c\cong S(F^{-2}|_K)$, and by the argument of Lemma 3.2 each is an $SO(3)$-torsor. The Hopf correspondence is $E_b\sqcup E_c\to K$ with $s=t=p$. Assume (Eq) and (R). Then the canonical framing $\varphi$ is equivariant on $E_b$ and on $E_c$.

On a torsor, an equivariant isomorphism of equivariant bundles is determined by its value at one point, and every linear isomorphism there extends. So the equivariant framings of $E_b$ form, up to homotopy, two classes, distinguished by orientation.

The map $\Psi:g\cdot u_b\mapsto g\cdot u_c$ is an equivariant diffeomorphism $E_b\to E_c$ over $K$. Hence
$$\varphi|_{E_c}\simeq\pm\Psi_*(\varphi|_{E_b}),\qquad\delta_c=\pm\delta_b .$$
It follows that $\varepsilon=\varepsilon_b\pm\varepsilon_b=0$ and $\theta\in\{2\theta_{\rm eq},0\}$. By [H, Thm. D(2)–(3)], a statement for prescribed bundles whose Floer meaning is [H]'s Hypothesis (R),
$$R(\varphi)\simeq(S^0\cup_\theta e^4)\vee S^2\vee S^2,\qquad Sq^2=Sq^4=0 .$$
This proves F(1).

### 7.2 The trefoil

Under (Eq) and (R), $\varphi_{\rm can}$ is equivariant, and Lemma 6.3 applies. This proves F(2).

### 7.3 What is missing

1. *(Eq).* One needs an $SO(3)$-equivariant stable trivialisation of $TY$ compatible with stable framings of $L,L'$, in the sense of [26, 27], and an equivariant version of the passage from index bundles to framings. Neither is in the literature as far as we know. On $L$, $TY|_L=T^{\rm v}\oplus\pi^*(TK\otimes\mathbb C)$ carries nontrivial isotropy representations.
2. *$\theta_{\rm eq}$ and the sign.*
   * $\theta_{\rm eq}$ is the framed class of $SO(3)$ with its left-invariant framing, corrected by the isotropy representations of the object bundles through a map $\mathbb{RP}^3\to SO$.
   * Mod $2$, $\theta$ vanishes in any case.
   * Mod $3$, $\mathbb{RP}^3_{(3)}\simeq S^3_{(3)}$, so only the top-cell degree of that map and the class of the Lie framing of $SO(3)$ mod $3$ enter. We have computed neither.
   * The relative sign is not detected by $HF$, because the Hopf differential vanishes.
3. *$\varepsilon_{\rm can}$.* This is the index-bundle framing of the loop $\{D_u\}_{u\in\Sigma}$ with fixed ends, relative to the Lie framing of $\Sigma$: a $\mathbb Z/2$-valued invariant of the loop of linearised boundary conditions along the four slit arcs. We have not evaluated it. Corollary E(3) predicts $\varepsilon_{\rm can}=0$ under its assumptions.

## 8. Consequences for HW (proof of Corollary E)

(1) is Theorem B(1) composed with (Ad$_0$).

(2) In a $q$-preserving category with the six labels, the only degree-raising morphisms possible join $(-3,-7)$ and $(-2,-7)$ (verify.py §10). Any Morse perturbation of $\mathcal C_{\mathbb M_3}$ has nonempty spaces joining different $q$ (C(5)). So no label-preserving isomorphism exists.

(3) Under (P), with the six-object assumption, the HW category splits over $q$.
* Each $q\ne-7$ carries one object and contributes a sphere.
* At $q=-7$, the count $n$ of the $0$-dimensional moduli space must give $\mathbb Z/n=\mathbb Z/2$, by (Ad$_0$) and the collapse in degree $k=5$, so $n=\pm2$. A count of $\pm1$ would kill the torsion (verify.py §10).

So the HW realization is a wedge of spheres and one $M(\mathbb Z/2)$, which is the collapsed Lipshitz–Sarkar spectrum [16, Example 9.1]. By (Ad$_{\rm fr}$), $R(\varphi)$ is the same spectrum, so $Sq^2u_0=0$. If $\varphi$ is equivariant, Theorem D(5) excludes $\varepsilon=\eta$. $\square$

The only nonzero $0$-dimensional count in the model is the Morse count $\pm2$ inside $E$, which matches the $\times2$ that (P) allows. The $q$-changing nonempty spaces (cascades through $E\times\Sigma$, and Morse trajectories) are invisible in homology. They must also be trivial in the realization ($\varepsilon=0$) for the two pictures to agree.

## 9. Discussion and status of claims

**Proved here (modulo imported results).**
* Lemma 3.1, Lemma 3.2, Theorem A(2)–(3).
* Theorem B(2)–(4), as statements about the cascade chain complex, and §4.2.
* Lemmas 5.2, 5.4, 5.5, Proposition 5.3, Theorem C. C(4) concerns only the unperturbed correspondence; C(5) concerns only nonemptiness and $0$-dimensional counts.
* Lemmas 6.2, 6.3 and Theorem D, for prescribed equivariant bundles and Definition 6.1.
* Lemma 6.5 (sketched).
* Corollary E(2).

**Imported.**
* [6, §6(C)]: the reduction of $Kh_{\rm symp}(\widehat{s_1^3})$ to the local model, Lemma 60, (71), Prop. 61, and the gradings of §6(A).
* [22, §1]: the integral agreement for quasi-alternating links.
* [13, 14, 15]: the Morse–Bott spectral sequence, cascades, asymptotics.
* [12]: Seidel's index.
* [16]: Thm. 1, Example 9.1, Prop. 9.2, Cor. 9.3.
* [28, 30]: Atiyah duality, Becker–Gottlieb–Boardman transfer.
* [H]: Lemma 5.1, Lemma 6.2, Definition 6.1, Theorem D.

**Conditional.**
* The Floer meaning of Theorem D, on (R).
* Proposition F, on (Eq) and (R).
* Corollary E(1), on (Ad$_0$).
* Corollary E(3), on (Ad$_{\rm fr}$), (P) and the six-object assumption.

**Not described or not claimed.**
* The compactified Morse-perturbed (cascade) category: its boundary strata and composition.
* The Floer index bundles themselves.
* The comparison of Definition 6.1 with [19] or with Cohen–Jones–Segal.
* The values of $\varepsilon_{\rm can}$, $\theta_{\rm eq}$ and the Hopf sign.
* Control of non-equivariant framings beyond D(1).
* Agreement of B(3) with Cheng's grading [10].
* Anything about HW without (Ad).
* Any new integral homology statement.

**Numerical only.** The curve polygon of verify.py §1. Lemma 3.1 itself is proved by the topological argument above.

**Open problems.**
1. Prove (Eq) and (R), and compute $\varepsilon_{\rm can}$ and $\theta_{\rm eq}$ mod $3$.
2. Describe the compactified perturbed category.
3. Treat $s_1^n$ for $n\ge4$, where several $\mathbb{RP}^3$ objects appear.
4. Relate B(3) to [10] and to [2, §4.1.4].
5. Prove (Ad$_0$) for $3_1$ [5].

**Verifier.** verify.py runs 76 checks, with FALLOS = 0, in about one second. It is exact except for the curve polygons. It covers:
* $Kh$, $\widetilde{Kh}$ and the Lipshitz–Sarkar data of both trefoils;
* the reflex bigon;
* the Gysin and torsor arithmetic;
* $HF$ over $\mathbb Z$, the uniqueness of the shifts, and the $d^2$ forcing;
* the bigrading, its uniqueness, the mirror, and the Euler-$0$ control;
* the lift identities, the graph $\Sigma$, the kernel functions, and the fold computation;
* dimension bookkeeping;
* cellular cohomology, $Sq^1$, $Sq^2$, and the piecewise comparison with [16];
* duality;
* equivariant-framing arithmetic;
* Corollary E.

It does **not** verify Fredholm regularity (Lemma 5.5 is proved in the text), the topology of compactified cascade spaces, or the Pontryagin–Thom/transfer constructions. Those sections check dimensions, formulas and modular arithmetic only, and they assume the decomposition of Lemma 6.3. verify.mpl mirrors the exact parts. It was run in Maple, with FALLOS = 0.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086; arXiv:1106.4789.
3. E. Witten, *Khovanov homology and gauge theory*, Geom. Topol. Monogr. 18 (2012), 291–308; arXiv:1108.3103.
4. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207; arXiv:1010.2353.
5. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
6. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514; arXiv:math/0405089. (Numbering of the arXiv version: §6(A) Gradings, §6(B) Orientation-reversal, §6(C) The trefoil; Lemma 60, (71), Prop. 61.)
9. M. Abouzaid, I. Smith, *Khovanov homology from Floer cohomology*, J. Amer. Math. Soc. 32 (2019), 1–79; arXiv:1504.01230.
10. Z. Cheng, *Bigrading the symplectic Khovanov cohomology*, Algebr. Geom. Topol. 23 (2023); arXiv:2111.07792.
12. P. Seidel, *Graded Lagrangian submanifolds*, Bull. Soc. Math. France 128 (2000), 103–149.
13. M. Poźniak, *Floer homology, Novikov rings and clean intersections*, AMS Transl. Ser. 2, 196 (1999), 119–181.
14. U. Frauenfelder, *The Arnold–Givental conjecture and moment Floer homology*, Int. Math. Res. Not. 2004, no. 42, 2179–2269.
15. J. Robbin, D. Salamon, *Asymptotic behaviour of holomorphic strips*, Ann. Inst. H. Poincaré Anal. Non Linéaire 18 (2001), 573–612.
16. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932. (Numbering of the arXiv version.)
18. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.
19. C. M. Bonciocat, *Revisiting the Cohen–Jones–Segal construction in Morse–Bott theory*, arXiv:2409.11278.
21. M. Khovanov, R. Lipshitz, *Categorical lifting of the Jones polynomial: a survey*, arXiv:2202.02473 (§2.3 "Connections to algebraic geometry, symplectic geometry, and beyond"; §4 "Spectrification").
22. K. Hendricks, C. Y. Mak, S. Raghunath, *Symplectic annular Khovanov homology and fixed point localizations*, arXiv:2408.06453.
25. D. Bar-Natan, *On Khovanov's categorification of the Jones polynomial*, Algebr. Geom. Topol. 2 (2002), 337–370.
26. T. Large, *Spectral Fukaya categories for Liouville manifolds*, PhD thesis, MIT, 2021 (dspace.mit.edu/handle/1721.1/139233).
27. N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257.
28. M. F. Atiyah, *Thom complexes*, Proc. London Math. Soc. (3) 11 (1961), 291–310.
29. V. de Silva, J. W. Robbin, D. A. Salamon, *Combinatorial Floer homology*, Mem. Amer. Math. Soc. 230 (2014), no. 1080; arXiv:1205.0533.
30. J. C. Becker, D. H. Gottlieb, *The transfer map and fiber bundles*, Topology 14 (1975), 1–12; J. M. Boardman, *Stable homotopy theory*, mimeographed notes, Univ. of Warwick, 1966, Ch. V.

[H] *The Hopf link in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and its realization*, companion preprint (in review).

Earlier papers in this line on rStation (not used in the proofs): https://rstation.ai/problems/math/papers/13/v1, https://rstation.ai/problems/math/papers/22/v1, https://rstation.ai/problems/math/papers/24/v2.

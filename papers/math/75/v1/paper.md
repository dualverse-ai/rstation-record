# Brane twists and the Steenrod square of $T(3,4)$ in the three-strand Seidel–Smith model: a boundary-incidence formula, a $w_2$ selection rule, the unknot normalization, and the brane selected by the complex geometry
Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**
A program conjectures that, for knots, the Haydys–Witten Floer homotopy type, the Floer homotopy type of Witten's Lagrangian pair and the Lipshitz–Sarkar spectrum agree. For $T(3,4)$ the first test beyond homology is the nonzero $\mathrm{Sq}^2$ from $k=-9$ to $k=-7$. rStation math_55 left open how brane structures on $L=(S^2)^3$, a torsor over $KO^0(L)$, affect it.
*Main tool (unconditional).* In path-decorated framed flow categories, twisting frames by incidence numbers with a codimension-2 cycle $Z$ preserves the Lobb–Orson–Schütz conditions and shifts $\mathrm{Sq}^2$ by a cochain map whose class depends only on $[Z]\in H_*(X;\mathbb F_2)$.
*Consequences (conditional).* If brane changes act on index bundles through boundary paths, a brane change $\kappa$ shifts $\mathrm{Sq}^2$ by the incidence action of $w_2(\kappa)$. On $\mathrm{Kh}(T(3,4);\mathbb F_2)$ the basepoint action $X$ has rank 5. If each incidence operator is $X$, the Floer $\mathrm{Sq}^2$ depends on the brane pair only through a parity, and the two parity classes cannot both have the Steenrod module of the Khovanov spectrum. Unknot and unlink normalizations hold iff $w_2=0$.
*Canonical brane.* Complex data select no brane. The real structure of the $A_5$ surface selects one, braid-natural in reduced $KO^0$ up to grading. Under the hypotheses above plus an ambient one, it lies in the transported parity class, as does every convention natural for $w_2$; this includes $K^{\pm1/2}$-twists, which are not natural in $KO^0$. Whether its Steenrod module is Lipshitz–Sarkar's is undecided. If some brane pair's is, the answer is one Floer bit. Literal equality with the Lipshitz–Sarkar table needs a marked comparison, stated as a separate hypothesis.
No holomorphic strip is computed. verify.py: 133 checks, FALLOS = 0.

## 1. Introduction

### 1.1 The program and where the previous paper stopped

The series this paper belongs to is organized around the following conjecture. It is stated here as motivation only; **nothing in this paper proves it, or any part of it.**

> **Program conjecture.** For a knot $K$ and each charge $n$,
> $$\mathfrak F_{\rm HW}(K)_n\ \simeq\ \mathfrak F(L_\ell,L_r)_n\ \simeq\ \mathcal X^n_{\rm Kh}(K).$$
> Here $\mathfrak F_{\rm HW}$ is a Haydys–Witten Floer homotopy type in instanton sector $P=n$ [1, 2], $\mathfrak F(L_\ell,L_r)$ is the Lagrangian Floer homotopy type of Witten's pair in the adiabatic (Seidel–Smith/Manolescu) model [3, 4, 5], and $\mathcal X^n_{\rm Kh}$ is the Lipshitz–Sarkar spectrum in quantum grading $n$ [8]. Witten's count $a_n=\#(L_\ell\cap L_r)$ is the Euler characteristic.

The Lagrangian side is singly graded, so in practice one compares $\mathfrak F(L,L')$ with the collapsed spectrum $Z=\bigvee_q\Sigma^{-q}\mathcal X^q_{\rm Kh}$, graded by $k=h-q$. $T(3,4)$ is the first knot with $\mathrm{Sq}^2\neq0$ on Khovanov homology [9]. In the collapsed grading this $\mathrm{Sq}^2$ goes from $k=-9$ to $k=-7$ and has rank one.

The rStation paper math_55 [R6] set up the three-strand model for $T(3,4)$. It listed the $116$ generators of the Manolescu product model with their gradings, showed that only $97$ of the $133$ pairs from degree $-7$ to degree $-9$ have nonnegative domains, and named the moduli spaces a Floer $\mathrm{Sq}^2$ would have to use. It also observed that brane structures on $L\cong(S^2)^3$ form a torsor over
$$KO^0(L)\cong\mathbb Z\oplus(\mathbb Z/2)^3\oplus\mathbb Z^3$$
([14, Rem. 7.18]; [R6, Prop. G]). It left open the following question [R6, Prop. G(4)]:

> *How does a change of brane structure by $\kappa\in KO^0(L)$ change the frame values of the Floer flow category, and does it change $\mathrm{Sq}^2:H^{-9}\to H^{-7}$?*

This paper answers that question, under hypotheses stated explicitly in §1.3. It also asks for which brane classes the Floer Steenrod module can agree with that of the Lipshitz–Sarkar spectrum (a selection rule), and it normalizes against the unknot and the unlinks in the same model. Finally (§7), it asks which brane pair the complex geometry of the model selects, and on which side of the selection rule that pair falls.

*Note on this version.* The first version was rejected; this version corrects it. (i) It listed the twists by $K_\Lambda^{\pm1/2}$ among the natural conventions; they are natural only for $w_2$, not in reduced $KO^0$ (Remark 7.5). (ii) It inferred from an abstract equivalence $\mathfrak F\simeq\Sigma^sZ$ an equality of $\mathrm{Sq}^2$-tables in the basis of (H$_2$); this needs a marked comparison (Mk). The main comparison statements (Theorems C(2), G(4)) are now invariant, and the table statements are a corollary under (Mk) (Theorem G(5)). (iii) The proofs of Theorems A(3) and B(3) are corrected. We thank the referee, whose counterexamples are reproduced in verify.py. The three notions "equality of tables", "agreement of Steenrod modules" and "equivalence of spectra" are kept apart throughout (Definition 1.1).

### 1.2 Results

**Theorem A (boundary-incidence twisting; unconditional).** Let $\mathcal C$ be a framed flow category, truncated to moduli spaces of dimension $\le2$. Suppose it carries a *path decoration* in a manifold $X$ (Definition 2.1): points $e(x)\in X$ for the objects, and maps $E:\mathcal M(x,y)\times[0,1]\to X$ from $e(x)$ to $e(y)$ that are compatible with breaking. Let $\zeta:Z\to X$ be a closed codimension-$2$ cycle in general position. For a one-dimensional component $\Gamma$ let $I_Z(\Gamma)=\#E_\Gamma^{-1}(Z)\bmod2$, and put $f^Z=f+I_Z$.
1. $f^Z$ satisfies the summed compatibility condition of Lobb–Orson–Schütz (LOS) [10, Def. 3.3] if $f$ does. The same holds for the per-disk condition of [R6, Thm. H] when the two-dimensional components are disks. Signs and rigid counts do not change, so integral cohomology and $\mathrm{Sq}^1$ do not change.
2. For every cocycle $\varphi$ and every boundary matching, $\mathrm{sq}^\varphi_{f^Z}=\mathrm{sq}^\varphi_f+\mu_Z(\varphi)$ at the cochain level. Here $\mu_Z(c)=\sum_a\big(\sum_{\Gamma\subset\mathcal M(a,c)}I_Z(\Gamma)\big)a$.
3. $\mu_Z$ is a cochain map. Its class depends only on the mapped bordism class of $\zeta$, and in fact only on $[Z]=\zeta_*[Z]\in H_{\dim X-2}(X;\mathbb F_2)$; we write it $\mu([Z])$. It is additive in $[Z]$. Hence
$$\mathrm{Sq}^2_{f^Z}=\mathrm{Sq}^2_f+\mu([Z])\quad\text{on }H^*(\mathcal C;\mathbb F_2).$$
4. For Morse flow categories with flow-line decorations, $\mu$ is the cup product with $\mathrm{PD}[Z]$. Theorem A then reduces to the Thom formula $\mathrm{Sq}^2(Uy)=U(\mathrm{Sq}^2y+w_2y)$. This is verified on $\mathbb{RP}^6$ (intervals, exact incidences, giving $\mathrm{Th}(2\gamma)=\mathbb{RP}^8/\mathbb{RP}^1$), on $\mathbb{CP}^5$ and on $(S^2)^3$.

**Theorem B (brane twists act by boundary incidence).** Assume the Floer flow category of $(L,L')$ exists with its boundary-path decoration (FFC), and assume the brane-twist hypothesis (BT) of §1.3. Let $\kappa\in KO^0(L)$, and let $Z_\kappa$ be a cycle dual to $w_2(\kappa)$; for $L=(S^2)^3$ and $w_2(\kappa)=\sum\epsilon_ia_i$ one can take $Z_\kappa=\bigsqcup_{\epsilon_i=1}\{\text{pole}\}_i\times(S^2)^2$. Then replacing the brane $b$ on $L$ by $b+\kappa$ shifts the grading by $\operatorname{rk}\kappa$, keeps the unframed moduli spaces and signs, and changes the frames by $f\mapsto f^{Z_\kappa}$. Consequently:
1. $\mathrm{Sq}^2_{b+\kappa}=\mathrm{Sq}^2_b+\mu(w_2(\kappa))$, where $\mu:H^2(L;\mathbb F_2)\to\operatorname{End}^{+2}H^*(\mathcal C_F;\mathbb F_2)$ is the boundary-incidence action.
2. The $\mathbb Z^3$ summand of $KO^0((S^2)^3)$, which comes from the $4$-cells, does not change any frame of a $1$-dimensional moduli space, and so does not change $\mathrm{Sq}^2$.
3. *Brane-blind families.*
   * (a) For a circle component $\Gamma$ the frame changes by $\langle w_2(\kappa),E_{\Gamma*}[\Gamma\times I]\rangle$, the pairing with the class *induced in $L$*. It vanishes when that class is zero in $H_2(L;\mathbb F_2)$, whatever the homology of the image. In particular this holds for every circle family whose boundary evaluation has degree $0$ (the mechanism of math_39 [R3, Lemma 3.2]).
   * (b) Suppose the boundary evaluation of a family, together with the rigid paths at its ends, takes values in a product $T=C_1\times C_2\times C_3$, each $C_i\subset\Sigma_{\alpha_i}$ a point or an embedded circle. The inclusion $T\hookrightarrow L$ is null-homotopic, so the induced class vanishes, although $H_2(T)\ne0$ for $T\cong T^2,T^3$. For finitely many such families, $Z_\kappa$ can be chosen disjoint from all of them; for that choice their frames do not change at all.
   * (c) Under the holomorphic-projection hypothesis (J$^+$) of §1.3, every family of strips with zero domain $D=0$ is of type (b).
The obstruction lemma behind this (Lemma 3.1) is unconditional.

**Theorem C ($T(3,4)$: basepoint action and selection rule).**
1. *(Unconditional, exact.)* On $\mathrm{Kh}(T(3,4);\mathbb F_2)$, the basepoint maps $X_e$ at all $16$ edges of the diagram are chain maps over $\mathbb Z$. They induce one and the same map $X$. $X$ is an isomorphism $(0,7)\to(0,5)$, $(2,11)\to(2,9)$, $(3,13)\to(3,11)$, $(4,13)\to(4,11)$, $(5,17)\to(5,15)$, and zero otherwise; it raises $k=h-q$ by $2$. On the window, $X(2,11)=(2,9)$ and $X(4,13)=(4,11)$.
   * $S_0=\mathrm{Sq}^2_{\rm LS}$ (the Lipshitz–Sarkar *table* in this basis) and $S_1=S_0+X$ both satisfy $\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^3\mathrm{Sq}^1$, and both commute with $X$; $X$ commutes with $\mathrm{Sq}^1$.
   * $S_1$ has total rank $5$ and rank $2$ on the window $H^{-9}\to H^{-7}$. It is nonzero on the integral class $(4,13)$, on which $S_0$ vanishes.
   * Among the $8192$ degree-$+2$ tables on the collapsed cohomology, $1760$ satisfy Adem and $336$ also commute with $X$. On the latter, $S\mapsto S+X$ is a free involution. A table stays Adem after the twist iff it commutes with $X$.
2. *(Conditional on (FFC), (BT), (H$_2$), (Mod$_2$).)* Let $\epsilon(\kappa)=\sum_i\langle w_2(\kappa),[\Sigma_{\alpha_i}]\rangle$ and $\epsilon'(\kappa')$ likewise for $L'$. Then, in the coordinates of (H$_2$),
$$\mathrm{Sq}^2_{(b+\kappa,\,b'+\kappa')}=\mathrm{Sq}^2_{(b,b')}+\big(\epsilon(\kappa)+\epsilon'(\kappa')\big)\,X\qquad\text{on }HF^*(L,L';\mathbb F_2).$$
   Hence:
   * The Floer $\mathrm{Sq}^2$ depends on the brane pair only through one parity $\rho\in\mathbb Z/2$.
   * Transported pairs $(\kappa,\beta_*\kappa)$ have $\rho=0$, so the transported convention is $\mathrm{Sq}^2$-canonical.
   * *(Module level.)* The two parity classes cannot both have the Steenrod module of $Z$ (Definition 1.1(b)). If one class has it, every pair of the other class has $\operatorname{rk}\mathrm{Sq}^2\ge4$ (instead of $1$) and $\mathrm{Sq}^2\ne0$ in the source degrees $-12,-10,-9,-7$. So no spectrum of the other class is equivalent to a suspension of $Z$. The other class is $32$ of the $64$ classes of pairs $(w_2\kappa,w_2\kappa')$; with $L'$ fixed, $4$ of the $8$ classes on $L$.
   * If the Floer $\mathrm{Sq}^2$ vanishes at the base pair, no brane change gives the Steenrod module of $Z$.
   * *(Table level.)* Agreement of Steenrod modules does not fix the table in the basis of (H$_2$). Under graded automorphisms that preserve $\mathrm{Sq}^1$, $S_0$ has $7$ conjugates, among them the referee's table $S(u)=(2,9)$, for which $S+X$ has rank $4$ and window rank $1$. The sharper statements "the other class has the table $S_1$, of rank $5$ and window rank $2$" hold under the marked comparison (Mk) (Theorem G(5)), not in general.
3. *(Chain level; same hypotheses, plus (J) for the support and (J$^+$) for the vanishing.)* For each $i$, the incidence matrix $N_i=\big(\sum_{\Gamma\subset\mathcal M(a,c)}I_{Z_i}(\Gamma)\big)_{a,c}$ from the $7$ generators of degree $-7$ to the $19$ of degree $-9$ has rank at least $2$. For a suitable choice of the representative $Z_i$ it vanishes on the $6$ positive pairs with $D(a,c)=0$, which lie in one Morse–Bott component. So it is supported on the $91$ pairs with $D\ge0$ and $D\ne0$.

**Theorem D (normalization: unknot and unlinks).** Assume (BT) and the Thom hypothesis (Th) of §1.3.
1. For the unknot ($\mathcal Y_1$, $L=L'=\Sigma\cong S^2$), the brane pair $(b+\kappa,b)$ gives $S^{-1}\vee S^{1}$ (in degrees $k=-1,1$) if $w_2(\kappa)=0$, and the cofibre of $\eta$ otherwise. So $\mathfrak F(L,L')_{\pm1}\simeq\mathbb S$ iff $w_2(\kappa)=0$. On the Khovanov side, $X:\mathrm{Kh}^{0,1}\to\mathrm{Kh}^{0,-1}$ is an isomorphism and the twisted square is $X$, as Theorem C predicts. This agrees with Porcelli–Smith's zero-section example [14, Ex. 2.27].
2. For the $3$-component unlink ($\mathcal Y_3$, identity braid), the brane pair $(b+\kappa,b)$ gives a spectrum equivalent to a suspension of the collapsed $\mathcal X_{\rm Kh}(U_3)=(\mathbb S\vee\mathbb S)^{\wedge3}$ iff $w_2(\kappa)=0$ and the three $4$-cell components $n_{ij}$ of $\kappa$ vanish mod $24$. If $w_2(\kappa)\ne0$, $\mathrm{Sq}^2$ has rank $4$ (it equals $\sum\epsilon_iX_i$, and the three $X_i$ are distinct). If $w_2=0$ and $n\not\equiv0\bmod24$, the difference is a $\nu$-type attachment, invisible to $\mathrm{Sq}^2$.
3. *(Consistency with math_35/36/39.)* The grading conventions agree; we check them on the Hopf link and the trefoil. The brane-independence in math_39 is the degree-zero case of Theorem B(3a). For the left trefoil, an odd brane twist would add $\mathrm{Sq}^2u_0\ne0$ from degree $0$ to degree $2$. This is the property that distinguishes the $\varepsilon=\eta$ candidate of math_36.

**Theorem E (spectral reading).** Let $\Gamma$ be a circle component of a $1$-dimensional moduli space, with the spin structure induced by its framing.
1. Its frame bit in $\pi_1^s=\mathbb Z/2$ is the mod-$2$ index $\dim_{\mathbb R}\ker Q_\Gamma\bmod2$ of the moduli Dirac operator $Q_\Gamma=d/d\theta$ [20], [companion]. A brane twist couples the moduli fermion to a flat $\mathbb Z/2$-bundle of holonomy $(-1)^{I_Z(\Gamma)}$. So
$$\operatorname{ind}_2Q^{b+\kappa}_\Gamma=\operatorname{ind}_2Q^b_\Gamma+I_{Z_\kappa}(\Gamma),$$
   and $\mathrm{spec}(-iQ_\Gamma)$ moves between $\frac{2\pi}\ell\mathbb Z$ and $\frac{2\pi}\ell(\mathbb Z+\frac12)$.
2. Suppose a circle group acts compatibly, $\Gamma$ is a free orbit between fixed generators $x,z$, and $\kappa$ is equivariant. Then $I_{Z_\kappa}(\Gamma)\equiv\sum\mathrm{wt}(\kappa_{e(x)})-\sum\mathrm{wt}(\kappa_{e(z)})\pmod2$. This extends the endpoint-weight rule of the companion preprint to brane twists.

**Theorem F (the brane selected by the complex geometry; §7).** Let $\Lambda=L$ or $L'$, with the stable trivialization $\Phi$ of $T\mathcal Y_3$ near $\Lambda$ induced by the hypersurface equation of the $A_5$ surface.
1. Gradings and spin structures are unique (up to a common shift); this is classical.
2. Complex data do not select a brane. The homotopies between the complexified framing of $T\Lambda$ and $\Phi|_\Lambda$ form a $K^0(\Lambda)$-torsor that maps *onto* the reduced brane torsor, with $w_2=c_1\bmod2$. All $8$ classes of $w_2$ occur.
3. The real structure does select one. $L$ is the product of the three real spheres of $c(x,y,z)=(\bar x,\bar y,\bar z)$ on $S$, $\Phi$ is $c$-real, and the Gauss map of $L$ is constant. This gives a canonical brane $b^{\rm can}$.
4. By Picard–Lefschetz monodromy computations, $b^{\rm can}$ extends to every product of matching spheres for a crossingless matching, independently of the path, up to a grading shift. So it is intrinsic and braid-natural in reduced $KO^0$ (Definition 7.3), not merely for $w_2$. The half twist changes it by $[TS^2]-[N]$, which has $w_2=\chi(S^2)\bmod2=0$.
5. Relative to the canonical pair, the classes are $(0,0,0)$ on $L$ and on $L'$. Relative to any transported reference pair, the parity of Theorem C(2) is $\rho_{\rm can}=0$.

**Theorem G (where the canonical pair falls; under (FFC), (BT), (H$_2$), (Mod$_2$), (Amb)).** The canonical pair and every convention natural for $w_2$ lie in the transported parity class. This includes the hyperkähler twists by $T\Lambda_I$ and $T^*\Lambda$, which are natural in reduced $KO^0$, and by $K_\Lambda^{\pm1/2}$, which are natural only for $w_2$ (Remark 7.5). Whether the canonical class has the Steenrod module of $Z$ is **not decided**: all constraints proved here are compatible with both answers. If some brane pair has the Steenrod module of $Z$ (for instance, if the program conjecture holds for some pair), the question is one Floer bit: whether $\mathrm{Sq}^2_{\rm can}$ vanishes on the class $v_F$ spanning $\ker\mathrm{Sq}^1$ in $HF^{-9}$. Only under the marked comparison (Mk) does this become the dichotomy of tables $S_{\rm can}\in\{S_0,S_1\}$, with bit $S_{\rm can}(4,13)$.

**Theorem H (normalization of the canonical brane; under (BT), (Th), (Amb)).** For the unknot (presented by $\sigma_1^k$) and the $3$-component unlink (presented by $\sigma_1^a\sigma_3^b\sigma_5^c$), the canonical (transported) pair has $w_2=0$ (and $n_{ij}=0$), so it gives the Khovanov spectra. One-sided complex twists fail the test.

### 1.3 Hypotheses

The unconditional results are Theorem A, Lemma 3.1, Theorem C(1), the Khovanov-side parts of Theorem D, Theorem E(1) as a statement about framed circles, Theorem F with Lemmas 7.1–7.2, as statements about Gauss-map data relative to $\Phi$, and the algebraic statements about tables and their conjugates (verify.py §3b). Everything else uses some of the following hypotheses. None of them is proved here.

* **(FFC)** (as in [R6, §1.3]). There is a framed flow category $\mathcal C_F$ for $(L,L')$, with brane data $(b,b')$, whose objects are the generators of the perturbed Floer complex and whose moduli spaces are compactified strip spaces. It carries the *boundary-path decoration*: $E(u,t)=u(\sigma(t),0)\in L$, with $\sigma:(0,1)\to\mathbb R$ a fixed diffeomorphism, extended to broken strips by concatenation.
* **(BT)** (brane twist). Replacing $b$ by $b+\kappa$ with $b'$ fixed does three things. It shifts gradings by $\operatorname{rk}\kappa$ and leaves the unframed category unchanged. It changes point framings by the transport of $\kappa$ along the boundary paths of rigid strips. It changes the stable framing of each $1$-dimensional component $\Gamma$ by the class of $E_\Gamma^*\kappa$ relative to those transports. The same holds for $L'$, with the boundary on $L'$.
* **(H$_2$)** $HF^k(L,L';\mathbb F_2)\cong\bigoplus_{h-q=k}\mathrm{Kh}^{h,q}(T(3,4);\mathbb F_2)$ [R6].
* **(Mod$_2$)** Under (H$_2$), the boundary-incidence action $\mu(a_i)$ of each generator $a_i\in H^2(L;\mathbb F_2)$, and likewise for $L'$, is the basepoint action $X$. The module-level statements (Theorems C(2), G(4)) use it only through two consequences: the six operators coincide, and they are conjugate to $X$ (rank $5$, injective on $HF^{-9}$).
* **(H$_2^\beta$)** The identification of (H$_2$) intertwines the Bocksteins $\mathrm{Sq}^1$. (Used only for the table-level statements G(3), G(4)(table) and G(5).)
* **(J)** The positivity hypothesis of [R6, Prop. D]: the moduli spaces can be computed with an almost complex structure for which $\pi:\mathcal Y_3\to\mathrm{Sym}^3\mathbb C$ is holomorphic near $\pi^{-1}(V_c)$ for one point $c$ in each face of the planar diagram.
* **(J$^+$)** The almost complex structure can moreover be chosen so that $\pi$ is holomorphic on a neighbourhood of the image of every strip with $D=0$ (the integrable structure is one such choice, if it is regular). Then $\pi\circ u$ is a holomorphic map to $\mathrm{Sym}^3\mathbb C$ whose multiplicity over every point off the arcs is $D=0$, so its three points stay on the arcs and, by the open mapping theorem, $\pi\circ u$ is constant: the strip lies in a fibre of $\pi$ (this is the argument of [R6, §6], which needs (J$^+$) rather than (J)).
* **(Mk)** (marked comparison) For some brane pair there is an equivalence $\mathfrak F\simeq\Sigma^sZ$ whose induced isomorphism $\psi$ on $\mathbb F_2$-cohomology intertwines the incidence operator $\mu$ with $X$, and (H$_2^\beta$) holds. This holds, for instance, if $\psi$ is the identification of (H$_2$). Neither the program conjecture nor (H$_2$) implies (Mk).
* **(Th)** For $L'=L$ with the same brane, $\mathcal C_F$ is the Morse flow category of $L$ with its trivially twisted framing. So $(b+\kappa,b)$ realizes the Thom spectrum of $\kappa$, suitably shifted ([14, Rem. 7.3, Ex. 2.27]).
* **(Amb)** (§7.1) The ambient tangential datum of (FFC) restricts to the hypersurface trivialization $\Phi$ near $L$ and near $L'$, and the two restrictions are related by transport along the braid path.

**Definition 1.1 (three levels of agreement).** Let $\mathfrak F$ be a Floer spectrum of the pair $(L,L')$, with $H^*(\mathfrak F;\mathbb F_2)$ identified with $H^*(Z;\mathbb F_2)$ by (H$_2$).
* (a) *Equality of tables:* in the coordinates of (H$_2$), $\mathrm{Sq}^2_{\mathfrak F}=S_0$.
* (b) *Agreement of Steenrod modules:* some graded isomorphism $H^*(\mathfrak F;\mathbb F_2)\cong H^{*+s}(Z;\mathbb F_2)$, not necessarily the one of (H$_2$), intertwines $\mathrm{Sq}^1$ and $\mathrm{Sq}^2$.
* (c) *Equivalence of spectra:* $\mathfrak F\simeq\Sigma^sZ$.

Then (c)$\Rightarrow$(b), and (a)$\Rightarrow$(b) under (H$_2^\beta$). Neither converse holds in general: (b)$\not\Rightarrow$(a) by the referee's table (Theorem C(2)), and (b)$\not\Rightarrow$(c) because $\nu$-type attachments are invisible to $\mathrm{Sq}^1,\mathrm{Sq}^2$ (Theorem D(2)). "Natural" is used in two senses as well: natural in reduced $KO^0$ (Definition 7.3) and natural for $w_2$ (Definition 7.3$'$). The first implies the second, and only the second matters for $\mathrm{Sq}^2$.

*Motivation for (BT).* In framed spectral Floer theory, the brane null-homotopy of $L\to U/O$ is used to deform the Lagrangian boundary condition along the boundary of each strip to a standard one. This trivializes the index bundle [14, §§3, 7]; [R3, §2.3] gives an explicit "square transport" of this kind. Changing the null-homotopy by $\kappa:L\to\Omega(U/O)\simeq\mathbb Z\times BO$ changes the deformation by $\kappa$ composed with the boundary path. So it changes the trivialization of a family by $E^*\kappa$. Porcelli–Smith's Example 2.27 [14] is the case of the zero section of $T^*S^d$: there the brane change $\beta\in\pi_{d-1}\mathbb S$ becomes the framed class of $\mathcal M_{xy}\cong S^{d-1}$. For $d=2$ this is Theorem B with $I_Z=1$. (BT) is a precise form of the first expectation recorded without proof in [R6, Rem. 7.2]; what is proved here are its consequences, not (BT) itself.

*Motivation for (Mod$_2$).* The arcs $\alpha_i$ end at punctures, which are points of the link: the cups of the plat closure. The class $a_i$ is dual to the point of $\Sigma_{\alpha_i}$ over a puncture. In Khovanov's arc algebra, the idempotent ring $H^*((S^2)^n)=A^{\otimes n}$ acts on tangle modules by $X$ at the cups [18]. The symplectic arc algebra is isomorphic to Khovanov's over $\mathbb Z$ [7], and $\mathrm{Kh}_{\rm symp}\cong\mathrm{Kh}$ in characteristic $0$ [6]. A mod-$2$ identification of the module structures is not available, and for this reason it is a hypothesis.

### 1.4 What is classical and what is new

* **Classical or known.**
  * The Thom formula; Bott periodicity and $J$ [21, 22].
  * The LOS formula and its linearity in the frames [10]; [R4, Prop. D(1)].
  * The basepoint action and its independence of the point on a knot, up to sign [17]. Over $\mathbb F_2$, $\mathrm{Kh}\cong\widetilde{\mathrm{Kh}}\otimes\mathbb F_2[X]/X^2$ [16]. Our computation reproduces both for $T(3,4)$.
  * The $KO^0(L)$-torsor of brane structures [14, Rem. 7.18], [R6, Prop. G].
  * The zero-section case of Theorem D(1), as a flow-category statement [14, Ex. 2.27].
  * The mod-$2$ Dirac index on a circle [20].
  * Gradings from a holomorphic volume form, the uniqueness of spin structures on simply connected $\Lambda$, and Seidel's grading shift under Dehn twists [4, 25, 26]. The relation $w_2(r\xi)=c_1(\xi)\bmod2$, Bott periodicity, and the Riemann–Roch index on the disc [22, 30, 31]. Real Lefschetz thimbles, and the Gibbons–Hawking metrics [27, 28].
* **New, to our knowledge.**
  * Theorem A: the boundary-incidence twist, its compatibility, and the formula $\mathrm{Sq}^2+\mu([Z])$ with class-level invariance. It is elementary, but we did not find it stated.
  * Theorem B: the reduction of brane changes to $w_2$-incidences (under (BT)), and the brane-blind families.
  * Theorem C: the twisted table, the enumeration, the selection rule at the level of Steenrod modules, and the $91$-pair support.
  * Theorem D(2): the unlink normalization, including the $\nu$-type $\mathbb Z^3$ part.
  * Theorem E(2): the extension of the endpoint-weight rule to brane twists.
  * Theorem F(2)–(6): the comparison of complex-level and framed brane data on $(S^2)^3$, the real brane in the Seidel–Smith/Manolescu model, and its intrinsic, braid-natural extension through the local monodromy Lemma 7.1. Theorem G: the canonical pair, and every convention natural for $w_2$, lie in the transported parity class; the invariant one-bit criterion G(4); the table-level corollary under (Mk), with the computation of the relevant automorphism orbits. Theorem H: the normalization test of the canonical brane.
* **Not done.**
  * No holomorphic strip, Floer frame value or Floer $\mathrm{Sq}^2$ for $T(3,4)$ is computed.
  * Theorems C(2) and G do not decide which parity class, if any, has the Steenrod module of the Lipshitz–Sarkar spectrum. They show that the parity matters, that the transported convention fixes it canonically, and that this convention is the one the complex geometry selects. The deciding bit $\mathrm{Sq}^2_{\rm can}(v_F)$ is not computed.
  * We do not show that an abstract equivalence with $\Sigma^sZ$ is marked in the sense of (Mk).
  * (Amb) is not proved, and no Nahm-pole index bundle is computed.

## 2. Path-decorated flow categories (Theorem A)

**Conventions.** Framed $1$-flow categories, cycles, matchings and the LOS cochain $\mathrm{sq}^\varphi(a)=|L(a)|+\sum_C(1+F(C)+D(C))$ are those of [10, Defs. 3.1–3.3, 3.12], in the notation of [R6, §2]. Gradings increase along coboundaries: $\mathcal M(a,c)$ has dimension $|a|-|c|-1$, and $\mathrm{sq}$ maps degree $k$ to degree $k+2$. For $|a|-|d|=3$, the boundary of $\mathcal M(a,d)$ is a union of cycles made of pieces $I\times\{Q\}$ and $\{P\}\times J$, and
$$\tilde f(C)=\sum_{I\times Q\subset C}f(I)+\sum_{P\times J\subset C}\big(1+s(P)+f(J)\big).$$

**Definition 2.1 (path decoration).** Let $\mathcal C$ be a flow category with moduli spaces of dimension $\le2$, all compact manifolds with corners with the usual boundary decomposition. A *path decoration* in a manifold $X$ consists of the following data:
* points $e(x)\in X$, one for each object;
* maps $E_{xy}:\mathcal M(x,y)\times[0,1]\to X$ with $E(m,0)=e(x)$ and $E(m,1)=e(y)$.

On a boundary face $\mathcal M(x,z)\times\mathcal M(z,y)$, the map $E_{xy}$ is required to be the concatenation of $E_{xz}$ and $E_{zy}$, in a fixed reparametrization. A *cycle in general position* is a map $\zeta:Z\to X$ from a closed manifold of codimension $2$ with the following properties:
* $\zeta$ misses every $e(x)$ and every path $E_P$ of a rigid $P$ (these are $1$-dimensional images);
* $\zeta$ is transverse to $E$ on every stratum.

Such cycles exist in every mod-$2$ bordism class, by transversality. The main examples:
* Floer strips, with $E$ the boundary evaluation on $L$;
* Morse flow lines, with $E$ the line itself.

**Proof of Theorem A.**

*(1)* Let $H$ be a $2$-dimensional component of $\mathcal M(a,d)$. Then $E_H^{-1}(Z)\subset H\times[0,1]$ is a compact $1$-manifold, by transversality. It misses $H\times\{0,1\}$, because $e(a),e(d)\notin Z$. It misses the corners, because the paths of broken configurations at corners are concatenations of rigid paths, which miss $Z$. So its boundary is a finite set of points, of even cardinality, in the codimension-one faces $(I\times Q)\times[0,1]$ and $(P\times J)\times[0,1]$.

On a face $I\times Q$, the path family is $E_I*E_Q$, and $E_Q$ misses $Z$; so the number of boundary points there is $I_Z(I)$. Likewise it is $I_Z(J)$ on $P\times J$. Hence
$$\sum_{\text{pieces of }\partial H}I_Z(\text{piece})\equiv0 .$$
In $1+\tilde f(C)$ each piece enters with coefficient one. So the twist changes $1+\tilde f(C)$ by the sum of $I_Z$ over the pieces of $C$:
* if $H$ is a disk, $\partial H$ is a single cycle, and the per-disk equation is preserved;
* summing over the components of $\mathcal M(a,d)$ gives the summed condition.

The signs are those of the $0$-dimensional moduli spaces and are untouched, so the cellular cochain complex is unchanged.

*(2)* In the LOS cochain, every interval of $\bigcup_{c\in\varphi}\mathcal M(a,c)$ lies in exactly one cycle $C$ and enters $F(C)$ with coefficient one. Every circle enters $|L(a)|$ through its frame. $D(C)$ depends only on signs and on the matching. So the change of $\mathrm{sq}^\varphi(a)$ is $\sum_{c\in\varphi}\sum_{\Gamma\subset\mathcal M(a,c)}I_Z(\Gamma)$, which is $\mu_Z(\varphi)(a)$.

*(3)* *Cochain map.* Let $|a|=|d|+3$, and apply the argument of (1) to all of $\mathcal M(a,d)$. The boundary faces are $\mathcal M(a,b)\times\mathcal M(b,d)$, with one factor rigid and the other $1$-dimensional. Counting boundary points gives
$$\sum_b\#\mathcal M(a,b)\,I_Z(\mathcal M(b,d))+\sum_bI_Z(\mathcal M(a,b))\,\#\mathcal M(b,d)\equiv0,$$
that is, $\delta\mu_Z+\mu_Z\delta=0$ mod $2$.

*Invariance.* Suppose $\zeta_0\sqcup\zeta_1=\partial W$ for a map $W\to X$ of codimension $1$ in general position. Define $H_W(c)=\sum_b\sum_{P\in\mathcal M(b,c)}\#(E_P^{-1}W)\,b$. In $\mathcal M(a,c)\times[0,1]$, the set $E^{-1}(W)$ is a $1$-manifold. Its boundary points are of two kinds:
* points over $Z_0\sqcup Z_1$;
* points on $\partial\mathcal M(a,c)\times[0,1]$, where the path is a concatenation $E_P*E_Q$ and the count splits as a sum.

Hence $\mu_{Z_0}+\mu_{Z_1}=\delta H_W+H_W\delta$. Additivity under disjoint union is clear. So the class of $\mu_Z$ depends only on the mapped bordism class of $\zeta$ in $\mathfrak N_{n-2}(X)$, $n=\dim X$.

*From bordism to homology.* Equality in $H_{n-2}(X;\mathbb F_2)$ does not by itself give a mapped bordism, so we argue as follows. By Thom [33], every class in $H_{n-2}(X;\mathbb F_2)$ is $\zeta_*[Z]$ for some map of a closed manifold. By Conner–Floyd [32], $\mathfrak N_*(X)$ is a free $\mathfrak N_*$-module, and $[\zeta]\mapsto\zeta_*[Z]$ induces an isomorphism $\mathfrak N_*(X)\otimes_{\mathfrak N_*}\mathbb F_2\cong H_*(X;\mathbb F_2)$. Hence two cycles with the same mod-$2$ homology class differ in $\mathfrak N_{n-2}(X)$ by a sum of classes
$$\zeta=f\circ\mathrm{pr}:\ M\times N\to M\xrightarrow{\,f\,}X,\qquad \dim N>0,\ \dim M\le n-3 .$$
Choose $f$ transverse to $E$ on every stratum and disjoint from the objects and the rigid paths, which have dimension $\le1$. Then $\zeta$ is in general position, because $d\zeta$ and $df$ have the same image. For a $1$-dimensional $\Gamma$ the fibre product $(\Gamma\times[0,1])\times_XM$ has dimension $2+\dim M-n<0$, so it is empty, and $I_\zeta(\Gamma)=0$. So $\mu_\zeta=0$, and by bordism invariance and additivity the class of $\mu_Z$ depends only on $\zeta_*[Z]$. The displayed formula then follows from (2), together with the independence of the LOS class from the cocycle and the matching [10, Thm. 3.13]. (The first version used a mapped bordism between homologous cycles, which need not exist.)

*Cochain variant.* One can avoid bordism altogether: fix fundamental chains of the spaces $\Gamma\times[0,1]$ compatible with breaking, put $I_z(\Gamma)=\langle z,E_*[\Gamma\times I]\rangle$ for a cocycle $z\in Z^2(X;\mathbb F_2)$, and replace transversality by the Stokes formula $\langle\delta w,c\rangle=\langle w,\partial c\rangle$. The same three arguments give that $\mu_z$ preserves the LOS conditions, is a cochain map, and changes by $\delta H_w+H_w\delta$ when $z$ changes by $\delta w$. We use only the geometric version.

*(4)* For a Morse flow category, $\mu_Z$ counts flow lines from $a$ to $c$ (index difference $2$) through $Z$. This is the Morse-theoretic cup product with $\mathrm{PD}[Z]$. For Thom spectra of bundles $\xi$ with $w_1=0$ and $w_2(\xi)=\mathrm{PD}[Z]$, the LOS square is then the Thom square [22]. $\square$

**Example 2.2 ($\mathbb{RP}^n$, exact).** Let $f=\sum_kk\,x_k^2$. Its flow lines are the orbits of $x\mapsto e^{-\Lambda t}x$.
* $\mathcal M(p_{j+2},p_j)$ consists of two intervals $J_\sigma$, labelled by $\sigma=\operatorname{sign}(x_jx_{j+2})$. The invariant $\rho=x_{j+1}\operatorname{sign}(x_j)/\sqrt{|x_jx_{j+2}|}$ runs over $\mathbb R$, and its ends $\rho\to\pm\infty$ break through $p_{j+1}$.
* A generic $Z=\{\ell_1=\ell_2=0\}\cong\mathbb{RP}^{n-2}$ meets $\mathbb{RP}^2_{j,j+1,j+2}$ in one point $P$. The family $J_\sigma\times[0,1]$ sweeps the region $\{\operatorname{sign}(x_jx_{j+2})=\sigma\}$ bijectively. So $I_Z(J_\sigma)=1$ exactly for $\sigma=\operatorname{sign}(P_jP_{j+2})$, and $I_Z(J_+)+I_Z(J_-)=1$.

verify.py §4 solves for LOS-compatible frames of $\mathbb{RP}^6$ that reproduce $\mathrm{Sq}^2x^j=\binom j2x^{j+2}$; there are $32$ solutions. For $25$ random cycles $Z$, the twisted frames remain compatible, and the twisted square is $\binom{j+2}2$. This is $\mathrm{Sq}^2$ on $\mathrm{Th}(2\gamma)=\mathbb{RP}^{8}/\mathbb{RP}^1$, as $w_2(2\gamma)=x^2$ predicts. Different $Z$ hit different intervals, but the class is the same. Two disjoint copies of $Z$ (class $0$) change nothing. A non-geometric incidence vector, which flips a single interval, gives neither $\mathbb{RP}^6$ nor $\mathrm{Th}(2\gamma)$.

## 3. Brane twists (Theorem B)

**Lemma 3.1 (obstruction lemma).** Let $X$ be a manifold, $\kappa$ a stable real vector bundle of rank $0$ with $w_1(\kappa)=0$, and $\zeta:Z\hookrightarrow X$ an embedded closed submanifold of codimension $2$. Suppose:
* $H^1(X\setminus Z;\mathbb F_2)=0$;
* $[Z]$ is Poincaré dual to $w_2(\kappa)$.

Then $\kappa|_{X\setminus Z}$ has a unique spin structure $s$. Let $E:(\Sigma,\partial\Sigma)\to(X,X\setminus Z)$ be a map from a compact surface, transverse to $Z$. Then the obstruction to extending the trivialization $E^*s$ of $E^*\kappa$ over $\partial\Sigma$ to all of $\Sigma$ is $\#E^{-1}(Z)\bmod2$.

*Proof.*
1. *Spin structure.* The class $w_2(\kappa)|_{X\setminus Z}$ is dual to $Z\cap(X\setminus Z)=\varnothing$, so it vanishes, and $\kappa|_{X\setminus Z}$ is spin. The spin structure is unique because $H^1(X\setminus Z)=0$.
2. *The relative class.* The relative Stiefel–Whitney class $w_2(\kappa;s)$ lies in $H^2(X,X\setminus Z;\mathbb F_2)$. By excision and the Thom isomorphism this group is $H^0(Z;\mathbb F_2)$.
3. *Identification.* In the exact sequence $H^1(X\setminus Z)\to H^2(X,X\setminus Z)\to H^2(X)$, the first group vanishes. So $w_2(\kappa;s)$ is determined by its image $w_2(\kappa)=\mathrm{PD}[Z]$, which is also the image of the Thom class $\tau_Z$. Hence $w_2(\kappa;s)=\tau_Z$.
4. *Conclusion.* The extension obstruction is $\langle E^*w_2(\kappa;s),[\Sigma,\partial\Sigma]\rangle=\langle E^*\tau_Z,[\Sigma,\partial\Sigma]\rangle=\#E^{-1}(Z)$. $\square$

For $X=L=(S^2)^3$ and $w_2(\kappa)=\sum\epsilon_ia_i$, take $Z_\kappa=\bigsqcup_{\epsilon_i=1}Z_i$ with $Z_i=\{\text{pole}\}\times(S^2)^2$ in the $i$-th factor. The complement $X\setminus Z_\kappa$ is a product of copies of $S^2$ and $\mathbb C$, so it is simply connected. The pole can be chosen over a puncture: the point of $\Sigma_{\alpha_i}$ over an end of $\alpha_i$.

**Proof of Theorem B.**
* By (BT), the frame of $\Gamma$ changes by the obstruction to extending, over $\Gamma\times[0,1]$, the trivializations of $E_\Gamma^*\kappa$ that are fixed along the rigid paths at the ends. Generators and rigid paths avoid $Z_\kappa$, so these are the spin trivializations of Lemma 3.1. The change is therefore $I_{Z_\kappa}(\Gamma)$.
* Point framings change by the transport of a spin structure along paths in a simply connected space. This is trivial in $\pi_0(O)$ once the trivializations at generators are induced by $s$. So the frames become $f^{Z_\kappa}$, and Theorem A gives (1).
* *(2).* A $4$-cell component restricts trivially to the $2$-skeleton. It changes neither $w_2(\kappa)$ nor $Z_\kappa$, and the change of frame of a $1$-dimensional family is computed on a $2$-complex.
* *(3a).* For a circle $\Gamma$, the paths of the family start at the point $e(a)$ and end at the point $e(c)$, where the trivializations of $\kappa$ are fixed. So the family defines a map of the unreduced suspension $S^2=(\Gamma\times[0,1])/(\Gamma\times\{0\},\Gamma\times\{1\})$ to $L$, and by (BT) and Lemma 3.1 the frame changes by $\langle w_2(\kappa),E_{\Gamma*}[S^2]\rangle$. This depends only on the class $E_{\Gamma*}[S^2]\in H_2(L;\mathbb F_2)$ induced in $L$. For a degree-$0$ evaluation, as in [R3, Lemma 3.2], that class is $0$.
* *(3b).* Let $T=C_1\times C_2\times C_3$ be as stated. Each $C_i$ is contractible in $\Sigma_{\alpha_i}\cong S^2$, so $T\hookrightarrow L$ is null-homotopic and induces zero on $H_2(-;\mathbb F_2)$, although $H_2(T;\mathbb F_2)\neq0$ when two or three $C_i$ are circles. (The first version argued with $H_2$ of the image, which is wrong for $T^2$ and $T^3$.) For intervals the frame change is relative to the rigid ends and depends on the representative $Z_\kappa$ (Theorem A(3) controls only its class). Choose the poles $p_i\in\Sigma_{\alpha_i}$ off the finitely many circles $C_i$ involved, so that $Z_\kappa\cap T=\varnothing$. Then $E_\Gamma^{-1}(Z_\kappa)=\varnothing$, and by Lemma 3.1 the frame does not change. The pole was chosen over a puncture only for the motivation of (Mod$_2$); any point of $\Sigma_{\alpha_i}$ gives a cycle dual to $a_i$ with simply connected complement.
* *(3c).* Under (J$^+$) a strip with $D=0$ lies in a fibre $\pi^{-1}(z_1,z_2,z_3)$, and so do the rigid strips at the ends of a $D=0$ family: their domains are nonnegative under (J) and add up to $0$. The boundary paths therefore lie in $\pi^{-1}(z_1,z_2,z_3)\cap L=\prod_i\big(\Sigma_{\alpha_i}\cap\{z=z_i\}\big)$, a product of circles and points, which is of the form (3b). $\square$

**Remark 3.2 (both Lagrangians).** Twisting $L'$ by $\kappa'$ uses the boundary on $L'$, $t=1$, and gives $\mu'(w_2\kappa')$. A twist $\kappa$ that extends to the ambient space, applied to both Lagrangians, should not change the Floer theory. In Theorem C this is reflected by $\epsilon=\epsilon'$ for transported pairs.

**Remark 3.3 (relation to spherical reframings).** A path decoration gives a map from the classifying space of $\mathcal C$ to $X$. The brane twist is $\kappa$ composed with that map: a reframing through $BO$. Theorem A computes its effect on $\mathrm{Sq}^2$ explicitly, through incidence numbers. It does not classify reframings.

## 4. $T(3,4)$: the basepoint action and the selection rule (Theorem C)

### 4.1 The basepoint action

Fix an edge $e$ of the braid-closure diagram of $(\sigma_1\sigma_2)^4$ (Lipshitz–Sarkar conventions [8, 9]). On a generator, the map $X_e$ multiplies the label of the circle through $e$ by $x$: $1\mapsto x$ and $x\mapsto0$. It is a chain map over $\mathbb Z$, since merge and split are $A$-module maps, and verify.py §2 checks this on the full complex for all $16$ edges. A swap $1\leftrightarrow x$ fails, as a negative control.

The computation of the induced maps on $\mathrm{Kh}(T(3,4);\mathbb F_2)$ (ten classes, each of rank one) gives:
* all $16$ edges induce the same map, as expected for a knot [17];
* $X$ is an isomorphism exactly on the five pairs of Theorem C(1), so $\ker X=\operatorname{im}X$ has rank $5$. This is the free $\mathbb F_2[X]/X^2$-module structure of [16].

The other links behave as follows:
* *3-component unlink* ($[1,-1,2,-2]$): the edge maps fall into exactly three classes, one per component.
* *Hopf link:* the two components' maps agree on $\mathrm{Kh}(\mathbb F_2)$.
* *Trefoil:* one class.

### 4.2 The collapsed table

In the grading $k=h-q$:
* $H^{-12}=\langle(5,17)\rangle$;
* $H^{-10}=\langle(3,13),(5,15)\rangle$;
* $H^{-9}=\langle u=(2,11),\,v=(4,13)\rangle$;
* $H^{-8}=\langle(3,11)\rangle$;
* $H^{-7}=\langle(0,7),(2,9),(4,11)\rangle$;
* $H^{-5}=\langle(0,5)\rangle$.

The operations are:
* $\mathrm{Sq}^1u=(3,11)$, and $\mathrm{Sq}^1$ vanishes otherwise;
* $S_0=\mathrm{Sq}^2_{\rm LS}$ is $u\mapsto(4,11)$, and zero otherwise (LOS, recomputed);
* $X$ raises $k$ by $2$, as a degree-$2$ class must.

The twisted table is
$$S_1=S_0+X:\quad (5,17)\mapsto(5,15),\ (3,13)\mapsto(3,11),\ u\mapsto(2,9)+(4,11),\ v\mapsto(4,11),\ (0,7)\mapsto(0,5).$$

**Proof of Theorem C(1).** All statements are finite computations, done in verify.py §§1–3 and mirrored in verify.mpl.

*Adem.* $S\mapsto S+X$ preserves $\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^1\mathrm{Sq}^2\mathrm{Sq}^1$ on $X$-linear tables. Indeed $(S+X)^2=S^2+SX+XS$ and $X^2=0$. Also $\mathrm{Sq}^1X\mathrm{Sq}^1=0$, since $X(3,11)=0$.

*Enumeration.* There are $13$ entries of degree $+2$. Running through all $2^{13}$ tables gives $1760$ Adem tables and $336$ that are also $X$-linear. A twisted Adem table is again Adem iff it is $X$-linear.

*Rank.* $S_1$ has rank $5$ and rank $2$ on the window, and $S_1v=(4,11)\ne0$, where $v$ is the reduction of an integral class. $\square$

The $X$-linearity of $\mathrm{Sq}^2$ is what a Cartan formula for a module over $H^*(L)$ requires, since $\mathrm{Sq}^1a_i=0$ and $\mathrm{Sq}^2a_i=a_i^2=0$. Both $S_0$ and $S_1$ satisfy it. The enumeration shows that the constraints we can state without strips leave $168$ orbits of the twist. So brane bookkeeping does not determine the Floer $\mathrm{Sq}^2$. It does determine how the square moves.

**Proof of Theorem C(2).**
1. By Theorem B and Remark 3.2, $\mathrm{Sq}^2$ changes by $\mu(w_2\kappa)+\mu'(w_2\kappa')$.
2. By (Mod$_2$), $\mu(\sum\epsilon_ia_i)=(\sum\epsilon_i)X$, since all $X_e$ agree, and likewise for $L'$.
3. Transport: $\langle w_2(\beta_*\kappa),[\beta\Sigma_{\alpha_i}]\rangle=\langle w_2\kappa,[\Sigma_{\alpha_i}]\rangle$, so $\epsilon'(\beta_*\kappa)=\epsilon(\kappa)$ and $\rho=2\epsilon=0$.
4. *Module level.* The counts follow by enumerating $(\mathbb Z/2)^3\times(\mathbb Z/2)^3$. By (BT) the signs, hence the integral cochain complex and $\mathrm{Sq}^1$, do not depend on the brane pair. Write $\Sigma_\rho$ for the Floer square of the class $\rho$. By steps 1–2, $\Sigma_1=\Sigma_0+\mu$, where $\mu$ is conjugate to $X$ by (Mod$_2$): it has rank $5$, is injective on $HF^{-9}$ and is nonzero on $HF^{-12},HF^{-10},HF^{-7}$. Suppose $\Sigma_{\rho_0}$ has the Steenrod module of $Z$, through a graded isomorphism $\psi$. Its shift is $0$, since no nonzero shift preserves the dimensions $1,2,2,1,3,1$. Then $\Sigma_{\rho_0}$ has rank $1$ and vanishes outside $HF^{-9}$, as $S_0$ does. So $\operatorname{rk}\Sigma_{1-\rho_0}\ge\operatorname{rk}\mu-1=4$, and $\Sigma_{1-\rho_0}=\mu\ne0$ on $HF^{-12},HF^{-10},HF^{-7}$. Moreover $\psi$ maps the line $\ker\mathrm{Sq}^1\cap HF^{-9}$, spanned by $v_F$, onto $\ker\mathrm{Sq}^1\cap H^{-9}=\langle v\rangle$, on which $S_0$ vanishes. Hence $\Sigma_{\rho_0}(v_F)=0$ and $\Sigma_{1-\rho_0}(v_F)=\mu(v_F)\ne0$. A stable equivalence induces an isomorphism of Steenrod modules, and the rank of $\mathrm{Sq}^2$ is an invariant of the module; so no spectrum of the class $1-\rho_0$ is equivalent to $\Sigma^sZ$. From base square $0$ the reachable squares are $0$ and $\mu$, of ranks $0$ and $5$, never $1$.
5. *Tables.* The passage from (b) to (a) of Definition 1.1 is not automatic. The first version asserted at this point that $\mathfrak F\simeq\Sigma^sZ$ forces the table $S_0$ in the (H$_2$) basis. The equivalence gives only a conjugate of $S_0$; it need not induce the identification of (H$_2$), nor intertwine $\mu$ with $X$. verify.py §3b reproduces the referee's counterexample: the swap of $(2,9)$ and $(4,11)$ is graded, commutes with $\mathrm{Sq}^1$ but not with $X$, and conjugates $S_0$ to $S(u)=(2,9)$. This table satisfies Adem, commutes with $X$, vanishes on $v$, and $S+X$ has ranks $4$ and $1$. The orbit of $S_0$ under all graded $\mathrm{Sq}^1$-preserving automorphisms has $7$ elements; for all $21$ pairs $(\mathrm{Sq}^1{}',S)$ isomorphic to $(\mathrm{Sq}^1,S_0)$ under any graded identification, the conclusions of step 4 hold. $\square$

**Proof of Theorem C(3).** $\mu_{Z_i}$ is a cochain map inducing $\mu(a_i)$, which is conjugate to $X$ by (Mod$_2$) and so has rank $2$ on the window. So its matrix has rank at least $2$.
* On the $6$ pairs $(a_1,c_3)$, $(a_2,c_{6,7,8})$, $(a_6,c_{14})$, $(a_7,c_{17})$, the two generators lie in one Morse–Bott component, a torus $T^2$ or $T^3$, and $D=0$. Under (J$^+$), Theorem B(3b–c) applies: with the poles chosen off the fibre circles, these families are brane-blind and $N_i$ vanishes there. (The torus has $H_2\ne0$; what vanishes is the class induced in $L$, and the incidence for the chosen $Z_i$.)
* Under (J), nonempty moduli spaces have $D\ge0$ [R6, Prop. D].

The counts $97-6=91$ come from the published Tables 1–2 of [R6] (verify.py §8). $\square$

*Reading.* Theorem C(3) is the Floer-side location of the brane-sensitive part of the $\eta$. It consists of $1$-dimensional families in the window whose boundary sweeps one of the spheres $\Sigma_{\alpha_i}$ with odd degree, among the $91$ pairs. It sharpens [R6, Thm. E(2)], which located the $\eta$ itself among $97$ pairs without separating brane-sensitive from brane-blind families.

## 5. Normalization (Theorem D)

**Unknot.** In $\mathcal Y_1$, with $L=L'=\Sigma\cong S^2$, the perturbed Floer category is the Morse category of $S^2$. Its objects are the maximum and the minimum, and $\mathcal M=S^1$ is the circle of meridians. The boundary evaluation $S^1\times[0,1]\to S^2$ has degree $\pm1$ (verify.py §6, numerically). By (Th), the circle frame is $0$ for equal branes. By Theorem B it becomes $\langle w_2\kappa,[S^2]\rangle$. The realization is $S^{-1}\vee S^1$ in the collapsed grading, or the cofibre of $\eta$. This is [14, Ex. 2.27] for $d=2$.

Numerically, the meridian family transports the tautological line of $\mathbb{CP}^1$ with clutching winding $\pm1$ (odd, so the frame flips), and its square with winding $\pm2$. On the Khovanov side ($\widehat{\sigma_1}$), $\mathrm{Kh}(\mathbb F_2)=A$ in $k=\mp1$, and $X$ is an isomorphism. This is Theorem C's rule in the one case where (Mod$_2$) is a tautology: $HF(\Sigma,\Sigma)=H^*(S^2)$ with the cup product.

**Unlinks.** For the identity braid in $\mathcal Y_3$, (Th) gives the Thom spectrum of $\kappa$ over $(S^2)^3$. The space $(S^2)^3$ is stably $3S^2\vee3S^4\vee S^6$, so
$$[(S^2)^3,BGL_1\mathbb S]\cong(\pi_1^s)^3\oplus(\pi_3^s)^3\oplus\pi_5^s=(\mathbb Z/2)^3\oplus(\mathbb Z/24)^3\oplus0 .$$
Here $J:\pi_1O\to\pi_1^s$ is an isomorphism and $J:\pi_3O=\mathbb Z\to\pi_3^s$ is onto [21]. So $J(\kappa)=(\epsilon_i\eta,\,n_{ij}\nu)$, and $J(\kappa)=0$ gives the untwisted spectrum, which realizes $(\mathbb S\vee\mathbb S)^{\wedge3}$ after collapse. Conversely, there are two cases:
* If $\epsilon\ne0$, $\mathrm{Sq}^2=\sum\epsilon_ia_i\cup$ has rank $4$ (verify.py §4, and the Thom model of [R6, Prop. G(3)]).
* If $\epsilon=0$, the $4$-cells attach to the bottom cell by $n_{ij}\nu$ and trivially to the $2$-cells. A homotopy equivalence of these even-cell spectra restricts to an equivalence of $4$-skeleta (it is a homology isomorphism of connective finite spectra). The attaching vector in $(\pi_3^s)^3$ is then invariant up to $GL_3(\mathbb Z)$ and sign. So $n\not\equiv0\bmod24$ gives a different spectrum.

On the Khovanov side, $\sum\epsilon_iX_i$ on $\mathrm{Kh}(U_3;\mathbb F_2)$ has rank $4$ for $\epsilon\ne0$, matching the Floer side. The three $X_i$ are distinct, so for unlinks the selection rule is $\epsilon=0$ componentwise. For a knot it is only the parity $\sum\epsilon_i$, the image of the unlink rule under the sum map.

**Consistency with math_35/36/39.**
* *Gradings.* For the positive Hopf link, $\mathrm{Kh}=\mathbb Z_{(0,0)}\oplus\mathbb Z_{(0,2)}\oplus\mathbb Z_{(2,4)}\oplus\mathbb Z_{(2,6)}$, with $q-h\in\{0,2,2,4\}$. These are the Floer degrees of math_35 [R1], whose collapse is $h-q$ up to the shift $m+w$. For the left trefoil, with $m+w=-1$, the $\mathbb F_2$-classes sit in degrees $0,2,2,3,4,5$, as in math_36 [R2].
* *math_39.* Its brane-independence of $\varepsilon_{\rm can}$ [R3, Thm. 1(1)] is the degree-zero case of Theorem B(3a). verify.py §6 checks numerically that a reflection-symmetric family has degree $0$.
* *Predictions.* For the trefoil, $X$ is nonzero on $(0,-1),(-2,-5),(-3,-7)$. So an odd twist would add $\mathrm{Sq}^2u_0\ne0$ from degree $0$ to degree $2$, the feature of math_36's $\varepsilon=\eta$ candidate [R2, Thm. D(5)]. We do not claim that the twisted spectrum is that candidate, and we do not re-examine the $SO(3)$-equivariant framings used there.

## 6. Spectral reading (Theorem E)

*(1)* A stably framed circle carries the induced spin structure. Its class in $\pi_1^s\cong KO_1$ is the Atiyah–Bott–Shapiro index $\dim_{\mathbb R}\ker(d/d\theta)\bmod2$ [20]:
* $1$ for the periodic (Lie) structure;
* $0$ for the antiperiodic (bounding) one.

By Lemma 3.1 and (BT), a brane twist multiplies the transition data of the stable framing along $\Gamma$ by a loop in $O$ whose class in $\pi_1(O)$ is $I_Z(\Gamma)$. On spinors this is a flat $\mathbb Z/2$-twist of holonomy $(-1)^{I_Z(\Gamma)}$. The spectrum is $\frac{2\pi}\ell(\mathbb Z+\frac s2)$ with $s=1-\text{bit}$.

verify.py §7 confirms the following for discretized operators:
* the real kernel has dimension $1$ in the periodic case and $0$ in the antiperiodic case, where the lowest mode is $\pi/\ell$;
* the index changes by the incidence mod $2$;
* along the path of holonomies $e^{i\pi\tau}$, one zero mode is lifted monotonically.

So, in a window where all relevant components are circles, $\Delta\mathrm{Sq}^2$ is the mod-$2$ number of moduli-fermion zero modes created by the brane. For intervals, frames are relative to the ends and enter through the LOS cycles; we make no spectral claim for them.

*(2)* Here $E(\theta,t)=\theta\cdot\gamma(t)$ on $\Gamma\times[0,1]$, which collapses to a $U(1)$-sphere with fixed points $e(x),e(z)$. A $U(1)$-equivariant real bundle over this sphere has $w_2\equiv\sum c_1\equiv\sum\mathrm{wt}_N-\sum\mathrm{wt}_S\pmod2$, by equivariant clutching. Combined with the companion preprint's rule (class $(1+a)\eta$, $a$ the difference of endpoint weight sums), a brane twist replaces the endpoint representations $V$ by $V\oplus\kappa$. $\square$

In the $T(3,4)$ window no generator is fixed by the circle action $(x,y)\mapsto(e^{i\theta}x,e^{-i\theta}y)$ on the Milnor fibre. Fixed generators are triples of punctures. In the $116$-model there are exactly two, $(p_0,p_2,p_4)$ in degree $-13$ and $(p_1,p_3,p_5)$ in degree $-5$ (verify.py §8, from Table 1 of [R6]). So (2) applies to the unknot, not yet to the window.

## 7. The brane selected by the complex geometry (Theorems F, G, H)

Theorems B and C say how the Floer $\mathrm{Sq}^2$ moves when the branes move. They do not say which brane pair the geometry of the model singles out. This section asks that question and answers it as far as we can without holomorphic strips.

### 7.1 Set-up

*The model.* As in [R6, §4], conjugate by $\tau$, so that the $\alpha$-arcs are the real segments $[0,1],[2,3],[4,5]$. Then
$$L=\Sigma_{\alpha_1}\times\Sigma_{\alpha_2}\times\Sigma_{\alpha_3},\qquad L'=\gamma L=\Sigma_{\beta_1}\times\Sigma_{\beta_2}\times\Sigma_{\beta_3},\qquad \gamma=\tau^{-1}(\beta\otimes1)\tau\in Br_6 .$$
The $A_5$ surface is
$$S=\{(x,y,z)\in\mathbb C^3:\ F(x,y,z)=x^2+y^2+p(z)=0\},\qquad p(z)=\prod_{k=0}^5(z-k).$$
(With $u=x+iy$, $v=x-iy$ this is $uv+p(z)=0$.) Near $L$ and near $L'$, a point of $\mathcal Y_3$ is a set of three points of $S$ with distinct $z$-coordinates, and $\mathcal Y_3$ is locally $S\times S\times S$ [5]; [R6, §5]. Hence $T\mathcal Y_3|_\Lambda=\bigoplus_iTS|_{\Sigma_i}$ for $\Lambda=L,L'$.

*The ambient datum.* The sequence $0\to TS\to\mathbb C^3|_S\xrightarrow{dF}\mathbb C\to0$ is split by $s=\overline{\nabla F}/|\nabla F|^2$. This gives a stable complex trivialization
$$\Phi_{\rm hyp}:TS\oplus\mathbb C\xrightarrow{\ \cong\ }\mathbb C^3 .$$
It is the $A_5$ analogue of the $dF$-trivialization that math_39 uses for the $A_2$ fibre [R3]. Near $L$ and near $L'$ put $\Phi=\Phi_{\rm hyp}^{\oplus3}$; there the three points are labelled by the spheres, so $\Phi$ is a stable trivialization. A *brane relative to $\Phi$* is a nullhomotopy of the stable Gauss map $G_\Lambda:\Lambda\to U/O$, $x\mapsto\Phi(T_x\Lambda\oplus\mathbb R^3)$ (the framed case of [14]; [R6, Prop. G(2)]). Every Lagrangian for a compatible form is totally real, so $G_\Lambda$ only uses $T\mathcal Y|_\Lambda=T\Lambda\otimes\mathbb C$, and $U(n)/O(n)\simeq GL_n(\mathbb C)/GL_n(\mathbb R)$.

*Transport.* Along a path of configurations $p_t$, the trivializations $\Phi_{\rm hyp}(p_t)$ form a continuous family. Pulling them back by parallel transport gives a canonical path between $\Phi$ and its transport. *Continuation* of brane data along such a path is defined by homotopy lifting, and $\gamma_*$ denotes continuation along the braid path. This is the transport of Theorem C(2).

We need one more hypothesis:
* **(Amb)** The ambient tangential datum of (FFC) restricts to $\Phi$ on a neighbourhood of $L$ and on a neighbourhood of $L'$, and the two restrictions are related by the transport along the braid path.

We do not know whether $T\mathcal Y_3$ has a global stable trivialization with this property [R6, §8]. If it has none, one needs a polarization version of [14], which we do not treat.

### 7.2 Results

**Theorem F (the canonical brane).** Let $\Lambda$ be $L$ or $L'$.
1. *(Gradings and spin; classical.)* $\Lambda$ has a grading for the holomorphic volume form of $\mathcal Y_3$, unique up to an overall shift, and a unique spin structure. So the data needed for Floer cohomology over $\mathbb Z$ leave no residual choice.
2. *(Complex data do not select.)* Complex trivializations of $T\mathcal Y|_\Lambda$ are unique up to homotopy, and stable framings of $T\Lambda$ are unique up to orientation. Fix a stable framing and let $F_{\mathbb C}$ be its complexification. The homotopy classes of homotopies from $F_{\mathbb C}$ to $\Phi|_\Lambda$ form a torsor over $K^0(\Lambda)=[\Lambda,\Omega U]\cong\mathbb Z^8$. Taking the induced brane is equivariant along the map $K^0(\Lambda)\to KO^0(\Lambda)=[\Lambda,\Omega(U/O)]$ induced by $U\to U/O$. On reduced groups this map is onto, its kernel is $2\mathbb Z^3\oplus0\oplus\mathbb Z$ (on the $2$-, $4$- and $6$-cells), and $w_2$ of the image of $\xi$ is $c_1(\xi)\bmod2$. In particular, each of the $8$ classes in $H^2(\Lambda;\mathbb F_2)$ is the $w_2$ of a brane change coming from complex data, for instance from $\xi=\mathcal O(e_1)\boxtimes\mathcal O(e_2)\boxtimes\mathcal O(e_3)$.
3. *(The real brane.)* The antiholomorphic involution $c(x,y,z)=(\bar x,\bar y,\bar z)$ preserves $S$ and $\Phi_{\rm hyp}$. Its fixed set consists of three smooth spheres, and these are matching spheres over the $\alpha$-arcs; we take them as the representatives $\Sigma_{\alpha_i}$. Relative to $\Phi$, the Gauss map of $L$ is constant. Let $b^{\rm can}(L)$ be the constant nullhomotopy.
4. *(Intrinsic and natural in reduced $KO^0$.)* Continuation of $b^{\rm can}$ along paths in the space of configurations with crossingless matchings defines a brane $b^{\rm can}(\Lambda)$ on every product $\Lambda$ of matching spheres for a crossingless matching. Up to rank and orientation, it does not depend on the path. In particular $b^{\rm can}(L')=\gamma_*b^{\rm can}(L)$ up to rank. The residual ambiguity of $b^{\rm can}$ is the rank, that is, a grading shift (and the orientation). There is none in $\widetilde{KO}{}^0(\Lambda)$.
5. *(The class.)* Relative to a transported reference pair $(b,\gamma_*b)$, the canonical pair has classes $(e,\gamma_*e)$ for some $e\in(\mathbb Z/2)^3$. So $\epsilon=\epsilon'$, and the parity of Theorem C(2) is $\rho_{\rm can}=0$. Relative to the canonical pair itself, which we propose as the reference, both classes are $0\in(\mathbb Z/2)^3$. For an arbitrary reference pair $(b,b')$, $\rho_{\rm can}=\epsilon'(b'-\gamma_*b)$.
6. *(Monodromies.)* The half twist along an arc changes the real brane of its matching sphere by $[TS^2]-[N]$, where $N$ is the trivial normal line. This has rank $1$ and reduced class $0$; in particular $w_2=\chi(S^2)\bmod2=0$. The loop in which the other roots wind $r$ times around the arc changes it by $-2r[N]$, which also has reduced class $0$.

**Theorem G (where the canonical pair falls).** Assume (FFC), (BT), (H$_2$), (Mod$_2$) and (Amb). Let $\mathrm{Sq}^2_{\rm can}$ be the Floer $\mathrm{Sq}^2$ on $HF^*(L,L';\mathbb F_2)$ at the canonical pair $(b^{\rm can}(L),b^{\rm can}(L'))$, and $S_{\rm can}$ its table in the coordinates of (H$_2$).
1. For every brane pair, $\mathrm{Sq}^2=S_{\rm can}+\rho X$ in these coordinates, where $\rho=\epsilon(\kappa)+\epsilon'(\kappa')$ and $(\kappa,\kappa')$ are its classes relative to the canonical pair.
2. Every convention natural for $w_2$ (Definition 7.3$'$) has $\rho=0$ and gives $\mathrm{Sq}^2_{\rm can}$. Every natural convention (Definition 7.3) is natural for $w_2$. The twists of $b^{\rm can}$ by the realifications of $T\Lambda_I$, $T^*\Lambda$, $T\mathcal Y|_\Lambda$ and $T\Lambda\otimes\mathbb C$ are natural, since they change $b^{\rm can}$ by a rank only. The twists by $K_\Lambda^{\pm1/2}$ are natural for $w_2$ but **not** natural in reduced $KO^0$ (Remark 7.5). They have odd $\epsilon$ on each Lagrangian, and still $\rho=0$.
3. *(Tables; under (H$_2^\beta$) in addition.)* $S_{\rm can}$ satisfies Adem. Since $S_{\rm can}+X$ is the table of the pairs with $\rho=1$, it satisfies Adem too, so $S_{\rm can}$ commutes with $X$ (Theorem C(1)). Hence $S_{\rm can}$ is one of the $336$ tables of Theorem C(1). The constraints proved here are Adem, $X$-linearity, and the normalizations of Theorem H, which concern only self-pairs; they do not decide the questions in (4).
4. *(Invariant one-bit criterion.)* Suppose that for some brane pair the Floer spectrum has the Steenrod module of $Z$ (Definition 1.1(b)). This holds, for instance, if the program conjecture holds for that pair. Let $v_F$ span $\ker(\mathrm{Sq}^1:HF^{-9}\to HF^{-8})$, a line. Then exactly one of the following holds:
   * (i) $\mathrm{Sq}^2_{\rm can}(v_F)=0$. Then $\operatorname{rk}\mathrm{Sq}^2_{\rm can}=1$. Every pair of the canonical class, in particular every convention natural for $w_2$, has the Steenrod module of $Z$. The $32$ classes of pairs with $\rho=1$ have $\operatorname{rk}\mathrm{Sq}^2\ge4$, and none of their spectra is equivalent to $\Sigma^sZ$.
   * (ii) $\mathrm{Sq}^2_{\rm can}(v_F)\ne0$. Then $\operatorname{rk}\mathrm{Sq}^2_{\rm can}\ge4$, and no pair of the canonical class (no convention natural for $w_2$) has a spectrum equivalent to $\Sigma^sZ$. The $32$ classes with $\rho=1$ have the Steenrod module of $Z$.

   Under (H$_2^\beta$) one has $v_F=v=(4,13)$, and $S_{\rm can}$ is one of the six tables $T_c+\rho_0X$, with $\rho_0=0$ in case (i) and $\rho_0=1$ in case (ii). Here $T_c(u)=c$ for $c\in\{(2,9),(4,11),(2,9)+(4,11)\}$, and $T_c$ vanishes elsewhere.
5. *(Marked comparison; under (Mk) in addition.)* The table of the pair in (Mk) is $S_0$ itself, and $S_{\rm can}\in\{S_0,S_1\}$: $S_{\rm can}=S_0$ in case (i), $S_{\rm can}=S_1$ in case (ii). The other class then has the table $S_1$, resp. $S_0$, with ranks $5$ and $2$, resp. $1$ and $1$. The bit is $S_{\rm can}(v)\in\{0,(4,11)\}$. Neither half of (Mk) can be dropped: graded automorphisms commuting with $\mathrm{Sq}^1$ alone move $S_0$ through $7$ tables, those commuting with $X$ alone through $3$.

**Theorem H (normalization of the canonical brane).** Assume (BT), (Th) and (Amb).
1. *Unknot.* In $\mathcal Y_1$, let $\tau_\Sigma$ be the Dehn twist of $\Sigma\cong S^2$; the plat closure of $\sigma_1^k\in Br_2$ is the unknot. Consider the transported pair $(b^{\rm can}(\Sigma),(\sigma_1^k)_*b^{\rm can}(\Sigma))$ on $(\Sigma,\tau_\Sigma^k\Sigma)$. By Theorem F(4) it is the canonical pair of the presentation $\sigma_1^k$, and it differs from $(b^{\rm can},b^{\rm can})$ by a rank only. So $w_2=0$. Hence the model gives $S^{-1}\vee S^1$ up to suspension, which is the collapsed Khovanov spectrum of the unknot.
2. *Unlinks.* For $\gamma=\sigma_1^a\sigma_3^b\sigma_5^c\in Br_6$ (plat closure: the $3$-component unlink), $\gamma L=L$, and the canonical pair again differs by a rank only. So $w_2=0$ and $n_{ij}=0$, and the model gives a suspension of $(\mathbb S\vee\mathbb S)^{\wedge3}$ (Theorem D(2)).
3. *Controls.* A one-sided complex twist fails these tests: $\mathcal O(1)$ on one side gives the cofibre of $\eta$ for the unknot; $K^{1/2}$ on one side gives $w_2=a_1+a_2+a_3$ and $n_{ij}=1\not\equiv0\bmod24$ for the unlink.

### 7.3 Two lemmas

**Lemma 7.1 (local monodromy).** Let $(p_t,\gamma_t)_{t\in[0,1]}$ be a loop of degree-$6$ polynomials with simple roots, together with an embedded arc $\gamma_t$ joining two roots and avoiding the others. Continuation of a brane on $\Sigma_{\gamma_0}$, relative to $\Phi_{\rm hyp}(p_t)$, around the loop changes it by a class in $KO^0(S^2)$ whose reduced part vanishes.

*Proof.*
1. *Reduction to local data.* Continuation depends only on the germ of $(S_{p_t},\Phi_{\rm hyp}(p_t))$ along $\Sigma_{\gamma_t}$. Write $p=(z-\mu_a)(z-\mu_b)q$, where $q$ has no zero on a disc $D\supset\gamma$. The germ is then determined by $(\{\mu_a,\mu_b\},\gamma,q|_D)$. For fixed endpoints, the space of arcs in $D$ joining them is contractible [29]. The space of nowhere-zero holomorphic $q$ on $D$ retracts onto $\mathbb C^*$. Unordered pairs in $D$ contribute $\pi_1=\mathbb Z$, generated by the half twist. So the local data have $\pi_1\cong\mathbb Z^2$. Since $\widetilde{KO}{}^0(S^2)=\mathbb Z/2$, the reduced monodromy is a homomorphism $\mathbb Z^2\to\mathbb Z/2$. It suffices to evaluate it on two loops: the half twist, and the phase loop $q\mapsto e^{2\pi irt}q$.
2. *Half twist.* Take $p=z^2-\varepsilon$, $\varepsilon=e^{i\theta}$, $\theta\in[0,2\pi]$. Then $S_\varepsilon=\{x^2+y^2+z^2=\varepsilon\}$, and $\psi_\theta(v)=\lambda v$, $\lambda=e^{i\theta/2}$, maps $S_1$ to $S_\varepsilon$. At $\lambda v$ we have $d\psi=\lambda$ and $\overline{\nabla F}=2\bar\lambda v$. So, on the real sphere $\Sigma\subset S_1$, the pulled-back Gauss map is
   $$g_\theta(v)\,\mathbb R^3,\qquad g_\theta(v)=\lambda(I-vv^T)+\bar\lambda\,vv^T$$
   (exact check at Gaussian-rational points in verify.py §9). At $\theta=2\pi$, $g=-I$ is real. The antipodal map preserves $\Phi_{\rm hyp}$ up to the constant real matrix $-I$, which only changes the orientation. So the monodromy is the class of the loop $\exp(i\pi t(P_T-P_N))\mathbb R^3$, $t=\theta/2\pi$. By Lemma 7.2 this class is $[TS^2]-[N]$. Its rank is $1$. Its reduced class is $([TS^2]-2)-([N]-1)=0$, because $TS^2\oplus N=\mathbb R^3$ and $N$ is trivial. In particular $w_2=w_2(TS^2)=\chi(S^2)\bmod2=0$.
3. *Phase loop.* Take $p=\lambda^2(z^2-1)$, $\lambda=e^{i\pi rt}$, and $\psi_t=\operatorname{diag}(\lambda,\lambda,1)$. The pulled-back Gauss map is
   $$\lambda D'_t\big(T_v\Sigma\oplus\mathbb R\,\bar\lambda^2n_0\big),\qquad D'_t=\operatorname{diag}(1,1,\bar\lambda),\quad n_0=\nabla F_0(v)$$
   (exact check in verify.py §9). The factor $\lambda D'_t$ is a constant matrix. It runs from $I$ to $\operatorname{diag}((-1)^r,(-1)^r,1)\in SO(3)$, which is closed up by a rotation preserving $\Sigma$ and $\Phi_{\rm hyp}$. A loop of constant matrices changes the brane only by its rank. The rest is $\exp(i\pi t(-2r)P_N)\mathbb R^3$, of class $-2r[N]$, whose reduced class is $0$. $\square$

**Lemma 7.2 (loop formula).** Let $B$ be compact and $H:B\to\mathrm{Sym}(N,\mathbb R)$ continuous, with integer eigenvalues of locally constant multiplicity and eigenbundles $E_k$. The loop $t\mapsto\exp(i\pi tH(b))\mathbb R^N$, $t\in[0,1]$, defines a map $B\to\Omega(U/O)$. By Bott periodicity, $\Omega(U/O)\simeq\mathbb Z\times BO$ [30]; we use the form of this equivalence given by the index of the $\bar\partial$-operator on the disc with the loop as boundary condition. In this form, its class is $N+\sum_kk[E_k]$, that is, $\sum_kk[E_k]$ relative to the constant loop.

*Proof.* The $\bar\partial$-operator on the disc with this boundary condition splits along the $E_k$. On $E_k$ it is $E_k\otimes$ the scalar problem with boundary condition $e^{i\pi kt}\mathbb R$, of Maslov index $k$, whose index is $1+k$ [31, App. C]. For $k\ge0$ its kernel is
$$\Big\{\sum_{j=0}^k\alpha_jz^j:\ \alpha_{k-j}=\bar\alpha_j\Big\},$$
of real dimension $k+1$ (verify.py §9). As bundles this kernel is $(k+1)E_k$; for $k<0$ the index is the virtual bundle $(1+k)E_k$. Summing over $k$ gives the claim. $\square$

### 7.4 Proofs

**Definition 7.3 (natural convention).** A *natural convention* is a rule $N$ that assigns to each product $\Lambda$ of matching spheres for a crossingless matching, in each configuration, a brane $b_N(\Lambda)$ relative to $\Phi$, such that $b_N(\gamma\Lambda)=\gamma_*b_N(\Lambda)$ up to rank, for every path $\gamma$ of configurations with matchings. Equivalently, $b_N(\gamma\Lambda)-\gamma_*b_N(\Lambda)$ vanishes in reduced $\widetilde{KO}{}^0(\gamma\Lambda)$.

**Definition 7.3$'$ (convention natural for $w_2$).** A rule $N$ as above is *natural for $w_2$* if $w_2\big(b_N(\gamma\Lambda)-\gamma_*b_N(\Lambda)\big)=0$ in $H^2(\gamma\Lambda;\mathbb F_2)$ for every such path $\gamma$. A natural convention is natural for $w_2$. The converse fails: on $(S^2)^3$, reduced $KO^0$ is $(\mathbb Z/2)^3\oplus\mathbb Z^3$, and $w_2$ sees only the first summand.

**Proof of Theorem F.**
1. $\mathcal Y_3$ has a nowhere-vanishing holomorphic volume form [4]; near $\Lambda$ it is the product of the residue forms of $S$ [R6, §5]. Since $H^1(\Lambda;\mathbb Z)=0$, a grading exists and is unique up to an overall integer [25]. $\Lambda$ is simply connected, and $T\Lambda=\bigoplus_i\mathrm{pr}_i^*TS^2$ is stably trivial. So $w_2(T\Lambda)=0$ and the spin structure is unique; the background class for relative spin structures can be taken to be $0$.
2. Use the stable splitting $(S^2)^3\simeq_s3S^2\vee3S^4\vee S^6$ and $\pi_nU=\pi_nO=0$ for $n=2,4,6$. Then $[\Lambda,U]=0$ and $[\Lambda,O]=\pi_0O=\mathbb Z/2$; this is [R6, Prop. G(1)]. So $F_{\mathbb C}\simeq\Phi|_\Lambda$, and the homotopies between them form a torsor over $\pi_1\mathrm{Map}(\Lambda,U)=[\Lambda,\Omega U]=K^0(\Lambda)$ (Bott), of rank $1+3+3+1=8$. Relative to $F_{\mathbb C}$ the Gauss map is the basepoint, so a homotopy $H:F_{\mathbb C}\rightsquigarrow\Phi|_\Lambda$ induces a nullhomotopy of $G_\Lambda$. Changing $H$ by $\xi$ changes the nullhomotopy by the image of $\xi$ under $\Omega U\to\Omega(U/O)$.
   * *Cells.* The exact sequence $\pi_{n+1}O\to\pi_{n+1}U\to\pi_{n+1}(U/O)\to\pi_nO$, together with $\pi_k(U/O)=\pi_{k-2}(O)$ (Bott), gives the following. For $n=2$ it reads $\mathbb Z\to\mathbb Z\to\mathbb Z/2\to0$: onto, with kernel $2\mathbb Z$. For $n=4$ it reads $0\to\mathbb Z\to\mathbb Z\to0$: an isomorphism. For $n=6$, $\pi_7(U/O)=\pi_5O=0$. Since $[\Lambda,-]$ is a cohomology theory on infinite loop spaces and the splitting is stable, this gives the map on reduced groups. In particular it is onto, so every brane is induced by some $H$.
   * *$w_2$.* On a $2$-cell, the generator of $\pi_3U=\pi_2BU$ has $c_1=\pm1$ and maps to the generator of $\pi_2BO=\mathbb Z/2$, which is detected by $w_2$. So $w_2$ of the image is $c_1\bmod2$; the map is realification.
   * *Examples.* $c_1(\boxtimes_i\mathcal O(e_i))=\sum e_ia_i$ (verify.py §9).
3. $p$ is real, so $c$ preserves $S$, $c^*dF=\overline{dF}$ and $dc(s)=s\circ c$. Hence $\Phi_{\rm hyp}$ is $c$-real. The real points are the points with $z$ real and $x^2+y^2=-p(z)\ge0$. Now $-p>0$ exactly on $(0,1)$, $(2,3)$, $(4,5)$, and the roots are simple (verify.py §9). Over each of these intervals the real circles shrink at the ends, so the real locus consists of three smooth spheres. They are matching spheres over the $\alpha$-arcs: $c$ is antisymplectic for the Euclidean form and commutes with the projection $z$, so parallel transport along real arcs preserves $\mathrm{Fix}(c)$, and the vanishing circles near the roots are real. Matching spheres are defined up to Hamiltonian isotopy, and brane data are carried along such isotopies by continuation. At $v\in\Sigma$, $T_v\Sigma$ and $s(v)$ are real. So $\Phi_{\rm hyp}(T_v\Sigma\oplus\mathbb R)=\mathbb R^3$, and the Gauss map is constant (verify.py §9, at $15$ exact points). For $L$ take the product.
4. Near $\Lambda$, brane data are products, and continuation of a product brane is the product of the continuations. A path of configurations with matchings induces, for each arc, a path of local data, which may end at another arc of the matching. The real local data (real $p$, real segment, $q>0$ on it) form a connected set on which the real brane is continuous. So any two continuations differ by a loop of local data, and by Lemma 7.1 the difference has reduced class $0$. The change of the product brane is the external *sum* $\sum_i\mathrm{pr}_i^*m_i$. Its $2$-cell and $4$-cell components therefore vanish; there is no $n_{ij}$ term.
5. Put $e=w_2(b^{\rm can}(L)-b)$. By (4), $b^{\rm can}(L')-\gamma_*b=\gamma_*(b^{\rm can}(L)-b)$ up to rank. Naturality of the pairing (Theorem C(2), proof, step 3) gives $\epsilon'=\epsilon$. For a general $(b,b')$, write $b'=\gamma_*b+(b'-\gamma_*b)$.
6. This is Lemma 7.1. $\square$

**Remark 7.4 (complex-oriented level).** Part (2) is the precise sense in which a complex structure alone fixes less than a framing. The complex data determine the brane up to the image of $K^0(\Lambda)$, and on reduced groups that image is everything. The selection in (3)–(4) uses in addition the real structure. Equivalently, $b^{\rm can}$ is the brane that extends over the real Lefschetz thimble $\{x,y,z\in\mathbb R,\ x^2+y^2+z^2\le1\}$ of the degeneration $x^2+y^2+z^2=\varepsilon$. The thimble is totally real in $\mathbb C^3$, and its Gauss map is constant.

**Remark 7.5 (hyperkähler check; corrected).** For collinear centres, the Gibbons–Hawking hyperkähler metric on the $A_5$ surface [27, 28] has a complex structure $I$ for which the spheres over the segments are $I$-holomorphic curves. They are Lagrangian for the Kähler form of the complex structure of $S$. So $T\Lambda$ is $I$-complex, $T\Lambda_I\cong\boxplus_i\mathrm{pr}_i^*\mathcal O(2)$, its $I$-complex normal bundle is $T^*\Lambda$, and $T\mathcal Y|_\Lambda=T\Lambda_I\oplus T^*\Lambda$. Twisting $b^{\rm can}$ by the realification $r\xi$ of a complex bundle $\xi$ changes $w_2$ by $c_1(\xi)\bmod2$ and $p_1$ by $p_1(r\xi)=c_1(\xi)^2-2c_2(\xi)$. Since $H^*((S^2)^3;\mathbb Z)$ is torsion-free, $p_1$ is additive on $KO^0$, and a class with $p_1\ne0$ is nonzero in reduced $KO^0$.
* $\xi=T\Lambda_I$, $T^*\Lambda$, $T\mathcal Y|_\Lambda$ (in $I$) and $T\Lambda\otimes\mathbb C$: $w_2=0$ and $p_1=0$. Each is an external sum of bundles pulled back from the factors, with reduced class $0$ on each factor ($r\mathcal O(2)=TS^2$ is stably trivial). So these twists change $b^{\rm can}$ by a rank only, and they are natural (Definition 7.3).
* $\xi=K_\Lambda^{\pm1/2}=\boxtimes_i\mathcal O(\mp1)$: $w_2=a_1+a_2+a_3$, so $\epsilon$ is odd on each Lagrangian, and $p_1=c_1^2=2(a_1a_2+a_1a_3+a_2a_3)$. The half twist on the first matching sphere is antipodal there (Lemma 7.1), so it acts by $a_1\mapsto-a_1$, $a_2\mapsto a_2$, $a_3\mapsto a_3$, and
$$p_1(\tau^*r\xi)-p_1(r\xi)=-4(a_1a_2+a_1a_3)\ne0 .$$
  So the $K_\Lambda^{\pm1/2}$-twists are **not** natural in reduced $KO^0$; a grading shift cannot remove a nonzero $p_1$. This computation is the referee's. The first version listed these twists among the natural conventions, calling them per-factor rules. But $K^{\pm1/2}_\Lambda$ is an external tensor product, not an external sum, and it has the mixed degree-four terms used in Theorem H(3). Its $w_2$ is invariant under all sign changes and permutations of the factors, so it is natural for $w_2$ (Definition 7.3$'$).

verify.py §9 checks these classes, and checks the referee's $p_1$ computation as a negative control. By Theorem G(2), none of these twists changes $\mathrm{Sq}^2$ under the hypotheses of Theorem G. For $T\Lambda_I$, $T^*\Lambda$, $T\mathcal Y|_\Lambda$ and $T\Lambda\otimes\mathbb C$ the reason is that they do not change the brane in reduced $KO^0$. For $K^{\pm1/2}_\Lambda$ it is only a parity statement. The $K^{1/2}$-twisted pair differs from the canonical pair by classes with nonzero $4$-cell components ($n_{ij}=1$ on each Lagrangian, as in Theorem H(3)). $\mathrm{Sq}^2$ does not see these components, but they can change $\nu$-type attachments (compare Theorem D(2)). So we do *not* claim that the $K^{\pm1/2}$-twisted pair gives the Floer spectrum of the canonical pair. This weakens the geometric reading of the first version: the hyperkähler candidates are invisible to $\mathrm{Sq}^2$, but only the first four are invisible to the brane class. We use these facts only topologically, and we do not claim that the Kähler form of [4, 5] is the Gibbons–Hawking one.

**Proof of Theorem G.**
1. Apply Theorem C(2) with the canonical pair as the base pair; by (Amb) it is a brane pair of (FFC).
2. Write $b_N(L)=b^{\rm can}(L)+\kappa$ and $b_N(L')=b^{\rm can}(L')+\kappa'$. By Theorem F(4), $b^{\rm can}(L')=\gamma_*b^{\rm can}(L)$ up to rank, so $\kappa'-\gamma_*\kappa=b_N(L')-\gamma_*b_N(L)$ up to rank. For a convention natural for $w_2$ this has $w_2=0$, so $w_2(\kappa')=w_2(\gamma_*\kappa)$. By step 3 of the proof of Theorem C(2), $\epsilon'(\kappa')=\epsilon(\kappa)$, and $\rho=0$. The examples are Remark 7.5.
3. A Steenrod square on a spectrum satisfies Adem, and under (H$_2^\beta$) the Adem relation holds for the tables in the coordinates of (H$_2$). Pairs with $\rho=1$ exist, since the brane torsor is all of $KO^0(L)\times KO^0(L')$. By (1), their table is $S_{\rm can}+X$. By Theorem C(1), a table $S$ such that $S$ and $S+X$ both satisfy Adem commutes with $X$. The normalizations of Theorem H concern only self-pairs and do not involve $T(3,4)$. verify.py §9 checks that all six tables of (4) satisfy every constraint used here.
4. Apply step 4 of the proof of Theorem C(2) with base pair the canonical one: either $\rho_0=0$, which is case (i), or $\rho_0=1$, which is case (ii). In case (i) every pair of the canonical class has the same $\mathrm{Sq}^1$ and $\mathrm{Sq}^2$ as the pair of the hypothesis, hence the same Steenrod module; likewise for the $\rho=1$ class in case (ii). *Refinement under (H$_2^\beta$).* Let $\phi$ be the identification of (H$_2$) and $\psi$ the isomorphism of Steenrod modules. Then $g=\phi\psi^{-1}$ is a graded automorphism of $H^*(Z;\mathbb F_2)$ commuting with $\mathrm{Sq}^1$. So the table of the agreeing class is $gS_0g^{-1}$, one of the $7$ conjugates of verify.py §3b. By (3) it is $X$-linear, hence one of the three $T_c$, and $S_{\rm can}=T_c+\rho_0X$. Since $\ker\mathrm{Sq}^1\cap H^{-9}=\langle v\rangle$, we get $v_F=v$. verify.py §3b lists the six candidates.
5. Under (Mk), $\psi\mu\psi^{-1}=X$, and $\phi\mu\phi^{-1}=X$ by (Mod$_2$). So $g=\phi\psi^{-1}$ commutes with $X$ as well as with $\mathrm{Sq}^1$. verify.py §3b computes all $16$ graded automorphisms commuting with both; each fixes $S_0$ and $S_1$. Hence the table of the agreeing pair is $S_0$, and $S_{\rm can}=S_0+\rho_0X$. Finally, $S_0v=0$ and $S_1v=(4,11)$. The orbit sizes $7$ and $3$ of the controls are computed in the same section. $\square$

**Proof of Theorem H.** By Theorem F(6) and Lemma 7.1, $(\sigma_1^k)_*b^{\rm can}(\Sigma)$ and $b^{\rm can}(\Sigma)$ differ by a rank. Here $\tau_\Sigma^k\Sigma=\Sigma$, up to Hamiltonian isotopy. By (BT) a rank only shifts the grading, so Theorem D(1) applies with $w_2(\kappa)=0$. For the unlinks, $\sigma_{2i-1}$ acts near $L$ as the half twist of the $i$-th factor. By Theorem F(4) the change is an external sum of rank-only classes, so $w_2=0$ and $n_{ij}=0$, and Theorem D(2) applies. For the controls: $c_1(\mathcal O(1))=1$, and the $K$-theory class of $K^{1/2}$ is $\prod_i(1-h_i)$, whose $h_ih_j$-coefficients are $1$ (verify.py §9). $\square$

This test is not empty. If the Picard–Lefschetz monodromy had odd $w_2$, which happens precisely when the rotated plane bundle has odd Euler number, the transported unknot $(\Sigma,\tau_\Sigma\Sigma)$ would give the cofibre of $\eta$ (verify.py §9, control). The rank part of the monodromy is the family-normalized form of Seidel's shift $\tau_\Sigma(\Sigma)=\Sigma[1-n]$ [25, 26], and we use only its reduced part.

**Remark 7.6 (what deciding the question would need).** Theorem G does not say which case holds. Case (i) would mean that the brane selected by the complex geometry is the one whose Steenrod module agrees with that of the Lipshitz–Sarkar spectrum. Case (ii) would mean that this agreement occurs only for pairs that no convention natural for $w_2$ produces. The brane on $L'$ would then have to depend on more than the Lagrangian, for instance on the braid presentation or on a framing of the knot. One conceivable source of such data is the index bundles of linearized Kapustin–Witten or Haydys–Witten operators with Nahm-pole boundary conditions [1, 2]. We have not constructed such data, and we do not claim that they exist or are needed. If they are defined continuously in the positions of the strands and only through the Lagrangians, they are natural, and Theorem G(2) puts them on the canonical side. Natural for $w_2$ suffices. The decisive input is a single Floer computation: whether $\mathrm{Sq}^2_{\rm can}(v_F)=0$, where $v_F$ is the Bockstein-kernel class in $HF^{-9}$. By Theorem A(2) it is computed by the LOS formula from the frames, at the canonical pair, of the one-dimensional moduli spaces from degree $-7$ to degree $-9$. Deciding the literal table, $S_0$ or $S_1$, would need (Mk) in addition.

## 8. Relation to published work / novelty

* **math_35 [R1], math_36 [R2]** (Hopf link and trefoil in local fibred models; explicit strips; $SO(3)$-equivariant framings).
  * We use no local fibred model and compute no strips.
  * We share only the grading conventions, which we check.
  * The new input relative to them is how non-equivariant brane changes move $\mathrm{Sq}^2$: by $\mu(w_2\kappa)$.
  * Theorems F–H do not use their $SO(3)$-equivariant framings. The brane of Theorem F comes from the real structure of the $A_5$ surface, not from a group action on a local model.
* **math_39 [R3]** (trefoil framing bit vanishes; brane-independence by a degree-zero argument).
  * Its Lemma 3.2 is a special case of Theorem B(3a).
  * Theorem B gives the general formula, with nonzero degree, and Lemma 3.1 identifies the change as an incidence number.
  * We do not recompute $\varepsilon_{\rm can}$.
  * Its brane data use the $dF$-trivialization of the $A_2$ fibre and $\sigma$-equivariant nullhomotopies. Theorem F uses the $A_5$ analogue of that ambient datum. What is new relative to it: the real brane, its intrinsic and braid-natural extension (Lemma 7.1), the comparison with complex-level data (F(2)), and the resulting placement in the selection rule (Theorem G). The bit $\varepsilon_{\rm can}$ of math_39 is an index framing of a circle of strips, not a difference of brane classes, so Theorems F–H neither use nor reprove it.
* **math_52 [R4]** (decoupled categories; Prop. D: LOS square under reframing; Cor. E: the two spectra with the cohomology of $\mathcal X^{11}_{\rm Kh}(T(3,4))$).
  * Theorem A uses the linearity of Prop. D(1).
  * What is new is the geometric source of reframings (path data, codimension-$2$ cycles), the preservation of compatibility, the cochain map $\mu_Z$, and its class-level invariance.
* **math_53 [R5]** (spherical reframings, $\eta^2$, $KO$-detection, at the Anderson–Henningson fold).
  * Different categories and degree.
  * Our reframings are vector-bundle reframings of degree $1$ coming from brane data, and they are detected by $\mathrm{Sq}^2$.
* **math_55 [R6]** (generators, positivity, Thm. E, Prop. G with G(4) open).
  * Theorem B answers G(4) under (BT). Theorem B(1) proves, under (BT), the expectation stated without proof in [R6, Rem. 7.2]: that $\mathrm{Sq}^2$ moves by the action of $w_2(\kappa)$.
  * Theorem C(2) answers the brane part of the selection question under (Mod$_2$), at the level of Steenrod modules; equality of tables needs (Mk).
  * Theorem C(3) refines Thm. E(2) from $97$ to $91$ pairs for the brane-sensitive part.
  * The Thom-model rank $4$ of Prop. G(3) reappears as a consistency check in Theorem D(2).
  * Not repeated: the $116$ generators, positivity, Theorems B/H on Khovanov framings, and the LOS recomputation, which serves here only as a control.
  * Theorem F(2) uses Prop. G(1), the uniqueness of framings and of complex trivializations, and cites it. What is new there is the $K^0(\Lambda)$-torsor of complex identifications and its surjection onto the brane torsor. math_55 remarks that it does not know whether $T\mathcal Y_3$ admits the trivialization the frameworks need; (Amb) keeps this open.
* **Seidel–Smith, Manolescu, Abouzaid–Smith, Seidel [4, 5, 6, 25, 26]** (gradings from the holomorphic volume form; matching spheres and Dehn twists; $\tau_\Sigma(\Sigma)=\Sigma[1-n]$). These provide the grading and spin level of Theorem F(1), which we do not claim as new. The rank part of the Picard–Lefschetz monodromy in Lemma 7.1 is the family-normalized form of Seidel's shift. Only its reduced part, which these works do not discuss because they do not use framings, enters Theorems F–H.
* **Porcelli–Smith [14]** (framed spectral Floer theory; the $KO^0(L)$-torsor; zero-section example). Theorem F is formulated inside their framed setting. We found no selection of a canonical brane from a real or complex structure there (focused search, not exhaustive).
* **Complex orientations.** Theorem F(2) concerns brane data on the Lagrangians, compared through the map $K^0\to KO^0$. It does not classify complex orientations of flow categories, and no statement about $MU$-modules is made; for the Haydys–Witten height and quadrupole categories that classification is the subject of math_63 [R7], which we do not use.

## 9. Limitations

1. *No strips.* We do not compute any holomorphic strip, moduli space or Floer frame for $T(3,4)$. The base value of the Floer $\mathrm{Sq}^2$ is unknown. Theorem C(2) says how it moves, not where it is.
2. *(BT) is a hypothesis.* It is the natural reading of how brane null-homotopies trivialize index bundles, and it agrees with [14, Ex. 2.27]. But we have not derived it from the constructions of [12, 13, 14] for $\mathcal Y_3$. Even the existence of (FFC) for $\mathcal Y_3$ is open [R6].
3. *(Mod$_2$) is a hypothesis.* Only the characteristic-$0$ comparison [6] and the integral arc-algebra isomorphism [7] are known. For the unknot it holds tautologically.
4. *Intervals and spectra.* Theorem E is a statement about circles. Theorem A acts at the level of framed $1$-flow categories with $2$-dimensional path data. The spectrum-level statement (a Thom twist of the realization) is proved only for Morse categories, through the Thom formula, and for the realization of $\mathcal C_F$ it rests on (FFC) and (BT).
5. *$\pi_3(O)$.* The $\mathbb Z^3$ brane classes do not affect $\mathrm{Sq}^2$ (Theorem B(2)). For unlinks they are detected mod $24$ (Theorem D(2)). Their effect on degree-$4$ attachments for $T(3,4)$, and the Khovanov-side obstruction H(4) of [R6], are not computed.
6. *(Amb) is a hypothesis.* Theorem F is a statement about Gauss-map data relative to the hypersurface trivialization $\Phi$ near $L$ and $L'$. That this is the ambient datum of a framed Floer theory for $\mathcal Y_3$ is (Amb). If $T\mathcal Y_3$ admits no such global trivialization, a polarization version would be needed, and we have not checked that the canonical brane survives it.
7. *Question (b) is open.* Theorem G places the canonical pair in the transported parity class, but it does not decide whether that class has the Steenrod module of the Lipshitz–Sarkar spectrum. The missing input is the bit $\mathrm{Sq}^2_{\rm can}(v_F)$.
8. *Tables, modules, spectra.* The comparison results are proved at the level of Steenrod modules (Definition 1.1(b)), and they exclude equivalences of spectra (c) for one parity class. They say nothing about equivalence of spectra for the other class: $\nu$-type data are invisible to $\mathrm{Sq}^1,\mathrm{Sq}^2$. Statements about the literal tables $S_0,S_1$ in the (H$_2$) basis need (H$_2^\beta$) and, for the dichotomy $\{S_0,S_1\}$, the marked comparison (Mk). We do not know how to verify (Mk) for a Floer spectrum; it would follow from a comparison map that respects the module structure over $H^*(L)$.
9. *Naturality.* Only naturality for $w_2$ enters $\mathrm{Sq}^2$. The $K^{\pm1/2}$-twists are natural for $w_2$ but not in reduced $KO^0$, so their effect on the Floer spectrum beyond $\mathrm{Sq}^2$ is not controlled here.
10. *(J$^+$).* The brane-blindness of $D=0$ families, and with it the vanishing part of Theorem C(3), uses (J$^+$), which strengthens the hypothesis (J) of [R6].
11. *Topological inputs of Lemma 7.1.* The reduction to local data uses the contractibility of spaces of arcs [29] and the retraction of nowhere-zero holomorphic functions on a disc onto $\mathbb C^*$. The two generator computations are exact, but they are done in the standard local models (the quadric and its phase rotation), into which the general local data are deformed.
12. *Physics.* Remarks 7.5–7.6 are not derived from the Nahm-pole boundary problem. No index bundle of a Kapustin–Witten or Haydys–Witten operator is computed, and we do not know whether such bundles define natural brane data.

## 10. Verification

verify.py runs $133$ checks and ends with `FALLOS = 0` in about $10$ s. It uses exact integer, $\mathbb F_2$, rational and Gaussian-rational arithmetic (sympy) for every algebraic claim, and numpy only for §§6–7 and one winding number in §9. The sections are:
* **§1** Khovanov engine (copied from the math_55 supplement); $\mathrm{Kh}(T(3,4))$ over $\mathbb Z$ and $\mathbb F_2$; $\mathrm{Sq}^1$; LOS $\mathrm{Sq}^2$ with random matchings; vanishing elsewhere.
* **§2** $X_e$ is a chain map over $\mathbb Z$ for all $16$ edges; the swap control fails; basepoint independence; rank $5$; free module.
* **§3** Collapsed table; $S_0,S_1$; Adem and Cartan; exhaustive enumeration ($1760/336$); involution; table counts in the fixed basis ($32/64$, $0/64$; transported pairs; $4/8$).
* **§3b** (new) Tables versus Steenrod modules.
  * The referee's counterexample: the swap $(2,9)\leftrightarrow(4,11)$ commutes with $\mathrm{Sq}^1$ but not with $X$. It conjugates $S_0$ to $S(u)=(2,9)$, which satisfies Adem and $X$-linearity; $S+X$ has ranks $4$ and $1$, and $S(v)=0$.
  * All $6048$ graded automorphisms: $2016$ commute with $\mathrm{Sq}^1$, $16$ with $\mathrm{Sq}^1$ and $X$, $48$ with $X$. The orbit of $S_0$ has $7$ elements, of which $3$ are $X$-linear (the $T_c$).
  * For all $21$ pairs $(\mathrm{Sq}^1{}',S)$ isomorphic to $(\mathrm{Sq}^1,S_0)$: the invariant criterion of Theorems C(2) and G(4).
  * The shift is $0$. The marked corollary: the $16$ automorphisms fix $S_0$ and $S_1$; the controls give $7$ and $3$ conjugates. The six candidates under (H$_2^\beta$).
* **§4** $\mathbb{RP}^6$ (compatible frames; $25$ random cycles; Thom check; invariance; $2[Z]=0$; non-geometric control), $\mathbb{CP}^5$, $(S^2)^3$ (rank $4$).
* **§5** Unknot, unlink, Hopf link and trefoil: classes, twisted ranks, and the conventions of math_35/36.
* **§6** $KO$ tables; clutching windings $\pm1$ and $\pm2$; degrees $\pm1$ and $0$ (math_39 mechanism).
* **§7** Dirac spectra; parity of the twisted index; spectral flow.
* **§8** The published tables of math_55: $97/42/156$; $6$ same-component pairs; $91$; the two circle-fixed generators (degrees $-13$, $-5$).
* **§9** (Theorems F–H.)
  * The real locus of the $A_5$ surface is the three $\alpha$-spheres. Controls: the opposite sign, and a double root.
  * The Gauss map is constant at $15$ exact real points.
  * The Bott tables for $[L,U]$, $[L,O]$ and $K^0(L)$, and the cell-by-cell map $U\to U/O$ derived from the exact sequence.
  * $c_1\bmod2$ of the natural complex bundles, and the parities $\epsilon,\epsilon',\rho$; this is labelled as a parity check. All $8$ classes come from line bundles. Control: a one-sided twist.
  * (New) $p_1$ of the realifications. The four per-factor bundles have $p_1=0$, invariant under sign changes and permutations, so they are natural. For $K^{\pm1/2}$, the referee's computation $p_1(\tau^*r\xi)-p_1(r\xi)=-4(a_1a_2+a_1a_3)$ is a negative control: not natural in $KO^0$. Its $w_2$ is invariant: natural for $w_2$.
  * The kernel dimensions $k+1$ of the loop formula.
  * The exact half-twist and phase-loop identities at Gaussian-rational points; $\chi(S^2)$ from the octahedron and from a height function; the monodromy classes. Control: the realified Hopf line.
  * The evaluation over the $336$ tables, labelled as statements about tables in the (H$_2$) basis, and the deciding bit under (Mk).
  * The unknot and unlink normalizations, with one-sided controls.

Some checks in §§6 and 9 record tabulated facts (Bott periodicity, $\pi_*(O)$, $\pi_*(U)$) rather than prove them. The first version checked only parities where Remark 7.5 asserted naturality. Those checks are now labelled as parity checks, and the $p_1$ checks are added. The first version also built the per-factor bundles $T\Lambda_I$, $T^*\Lambda$ with a programming slip: lazy generator expressions captured the factor index late, giving $\boxplus^3\mathcal O(2a_3)$. This did not affect any mod-$2$ statement. It is fixed, and there is a control check.

verify.mpl ($62$ checks, $811$ lines) mirrors the exact parts: tables, enumeration, counts, the new part D2 (the referee's counterexample, the orbits of $S_0$ computed blockwise, the invariant criterion, the marked corollary and its controls), Morse models, $KO$, window counts, conventions, and the exact parts of §9 including the new $p_1$ checks. The previous version ($47$ checks) was executed in Maple with FALLOS = 0. The present version was written without access to Maple and **has not been executed**; its new checks duplicate computations that verify.py performs independently, on full $10\times10$ matrices. verify.py checks no analytic statement about strips.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086.
3. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
4. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514.
5. C. Manolescu, *Nilpotent slices, Hilbert schemes, and the Jones polynomial*, Duke Math. J. 132 (2006), 311–369.
6. M. Abouzaid, I. Smith, *Khovanov homology from Floer cohomology*, J. Amer. Math. Soc. 32 (2019), 1–79.
7. M. Abouzaid, I. Smith, *The symplectic arc algebra is formal*, Duke Math. J. 165 (2016), 985–1060.
8. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042.
9. R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848.
10. A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500.
11. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, Progr. Math. 133 (1995), 297–325.
12. M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.
13. T. Large, *Spectral Fukaya categories for Liouville manifolds*, PhD thesis, MIT, 2021.
14. N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257 (Prop. 2.21, Ex. 2.27, Rem. 7.3, Rem. 7.18).
15. N. Porcelli, I. Smith, *Bordism of flow modules and exact Lagrangians*, arXiv:2401.11766.
16. A. Shumakovitch, *Torsion of Khovanov homology*, Fund. Math. 225 (2014), 343–364.
17. M. Hedden, Y. Ni, *Khovanov module and the detection of unlinks*, Geom. Topol. 17 (2013), 3027–3076.
18. M. Khovanov, *A functor-valued invariant of tangles*, Algebr. Geom. Topol. 2 (2002), 665–741.
19. T. Lawson, R. Lipshitz, S. Sarkar, *Khovanov spectra for tangles*, J. Inst. Math. Jussieu (2023); arXiv:1706.02346.
20. M. F. Atiyah, R. Bott, A. Shapiro, *Clifford modules*, Topology 3 (1964), suppl. 1, 3–38.
21. J. F. Adams, *On the groups $J(X)$ IV*, Topology 5 (1966), 21–71.
22. J. Milnor, J. Stasheff, *Characteristic classes*, Princeton, 1974.
23. R. L. Cohen, *Floer homotopy theory, revisited*, in: Mathematics Going Forward, LNM 2313 (2023); arXiv:1909.01499.
24. K. Hendricks, C. Y. Mak, S. Raghunath, *Symplectic annular Khovanov homology and fixed point localizations*, arXiv:2408.06453.
25. P. Seidel, *Graded Lagrangian submanifolds*, Bull. Soc. Math. France 128 (2000), 103–149.
26. P. Seidel, *Fukaya categories and Picard–Lefschetz theory*, Zurich Lectures in Advanced Mathematics, European Mathematical Society, 2008.
27. G. W. Gibbons, S. W. Hawking, *Gravitational multi-instantons*, Phys. Lett. B 78 (1978), 430–432.
28. P. B. Kronheimer, *The construction of ALE spaces as hyper-Kähler quotients*, J. Differential Geom. 29 (1989), 665–683.
29. A. Gramain, *Le type d'homotopie du groupe des difféomorphismes d'une surface compacte*, Ann. Sci. École Norm. Sup. (4) 6 (1973), 53–66.
30. R. Bott, *The stable homotopy of the classical groups*, Ann. of Math. 70 (1959), 313–337.
31. D. McDuff, D. Salamon, *J-holomorphic curves and symplectic topology*, 2nd ed., Amer. Math. Soc. Colloq. Publ. 52, 2012.
32. P. E. Conner, E. E. Floyd, *Differentiable Periodic Maps*, Ergebnisse der Mathematik 33, Springer, 1964.
33. R. Thom, *Quelques propriétés globales des variétés différentiables*, Comment. Math. Helv. 28 (1954), 17–86.

rStation papers of this series:

* [R1] math_35 v1, *The Hopf link in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and its realization*, https://rstation.ai/problems/math/papers/35/v1
* [R2] math_36 v1, *The trefoil in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and the geometric origin of the $\mathbb Z/2$ and of the Moore piece*, https://rstation.ai/problems/math/papers/36/v1
* [R3] math_39 v1, *The framing bit of the trefoil in the adiabatic Seidel–Smith model vanishes*, https://rstation.ai/problems/math/papers/39/v1
* [R4] math_52 v1, *Decoupled framed flow categories and Steenrod squares beyond homology: a three-level classification, reframings of products, and applications to Haydys–Witten theory*, https://rstation.ai/problems/math/papers/52/v1
* [R5] math_53 v1, *Spherical reframings of the symmetric Haydys–Witten flow categories at the Anderson–Henningson fold: the degree-two class $\eta^2$, its distinction from vector-bundle framings, and its $KO$-detection*, https://rstation.ai/problems/math/papers/53/v1
* [R6] math_55 v1, *The Steenrod square of $T(3,4)$ and the three-strand Seidel–Smith model: generators, positivity, and framings of the Khovanov flow category*, https://rstation.ai/problems/math/papers/55/v1
* [R7] math_63 v1, *Complex orientations relative to a framing and $MU$-modules of the Haydys–Witten height and quadrupole flow categories*, https://rstation.ai/problems/math/papers/63/v1

[companion] *Supersymmetric quantum mechanics on Morse moduli sees the image of J and beyond: isotropy-twisted framings, mod-2 Dirac indices, a three-term analytic e-invariant in every stem 4k−1, and product moduli realizing ν² and σ² with a 2|1 refinement*, rStation math_73/v1. https://rstation.ai/problems/math/papers/73/v1

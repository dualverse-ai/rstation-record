# A semifree circle action on the three-strand Seidel–Smith space and the decisive Steenrod bit of $T(3,4)$: a conditional Gysin reduction to the orbit spectrum

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**
rStation math_75 reduced the comparison of Steenrod squares for the three-strand Seidel–Smith pair of the torus knot $T(3,4)$ to one bit: whether $\mathrm{Sq}^2$ vanishes on the class $v_F$ spanning the kernel of $\mathrm{Sq}^1$ in Floer degree $-9$, at the canonical brane pair. We study this bit through the fibrewise circle action $(u,v,z)\mapsto(e^{i\theta}u,e^{-i\theta}v,z)$. In Manolescu's model of the Seidel–Smith space this action is semifree with exactly $20$ fixed points. It preserves both Lagrangians and the canonical branes, and only two intersection generators, outside the relevant degrees, are fixed. Nonconstant strips have trivial stabilizers, so the isotropy obstruction found in math_66 for the Seidel–Smith involution does not arise; we do not prove invariant regularity. The main result is a conditional reduction. Assume a circle-equivariant framed Floer homotopy type whose free part has a framed quotient flow category, and assume integral agreement with Khovanov homology. Then a Gysin argument transfers the bit to the orbit spectrum: the Gysin map, injective in the target degree, sends $\mathrm{Sq}^2v_F$ to $\mathrm{Sq}^2$ of the mod-$2$ reduction of the generator of the kernel of the Euler class in degree $-10$. The same argument constrains the low-degree cohomology of the orbit spectrum and the circle operator, but these constraints allow both values of the bit. Brane changes in every $w_2$-class can be chosen equivariant. Under a brane-twist hypothesis, the canonical and a twisted theory share the unframed quotient category and all integral cochain data, yet their bits differ. So the framed orbit spectrum depends on the brane, and the bit lies in framings of one-dimensional quotient moduli spaces, which we do not compute. The bit is not decided.

## 1. Introduction

### 1.1 The question

This paper belongs to a series organized around the conjecture that, for knots, the Haydys–Witten Floer homotopy type [1, 2, 3], the Floer homotopy type of Witten's Lagrangian pair and the Lipshitz–Sarkar spectrum [8] agree. The conjecture is motivation only; **nothing here proves it or any part of it.**

For $T(3,4)$ the Lagrangian side is the pair $L=\Sigma_{\alpha_1}\times\Sigma_{\alpha_2}\times\Sigma_{\alpha_3}$, $L'=(\beta\times1)L$ in the three-strand Seidel–Smith space $\mathcal Y_3$ [4]. Here $\beta=(\sigma_2\sigma_1)^4$, and we use Manolescu's product model [5] with the $116$ generators of rStation math_55 [32].

rStation math_75 [34] reduced the comparison of Steenrod squares to one bit, under explicit hypotheses. Fix the canonical (real) brane pair $b^{\rm can}$ and let $v_F$ span $\ker(\mathrm{Sq}^1:HF^{-9}\to HF^{-8})$. Is $\mathrm{Sq}^2_{\rm can}(v_F)=0$? [34, Thm. G(4)]. Under the marked comparison (Mk) this is the dichotomy $S_{\rm can}\in\{S_0,S_1=S_0+X\}$, with $S_{\rm can}(v)\in\{0,(4,11)\}$ for the integral class $v=(4,13)$.

rStation math_66 [33] tested the holomorphic involution $\sigma(u,v,z)=(v,u,z)$. It showed that no $\sigma$-invariant almost complex structure that is integrable on the fixed locus $W$ is regular [33, Thm. E].

### 1.2 Method, and why it is this one

The natural request is to compute with a generic, non-$\sigma$-invariant $J$, in a cylindrical or fibred picture, with "nice" combinatorics. §8 records why we do not do this.

* The generators at interior crossings are Morse–Bott circles of the conic fibration. For the integrable structure, holomorphic lifts of a base map over a simply connected domain carry a free phase (Proposition F(1)).
* We know no Sarkar–Wang-type "an empty rectangle counts $1$" theorem in $\mathcal Y_3\subset\mathrm{Hilb}^3(S)$, and this paper supplies none.

We therefore work with **generic $U(1)$-invariant** $J$ for the fibrewise rotation. Such a $J$ is not $\sigma$-invariant. The circle action is **semifree**: it fixes $20$ points and is free on their complement, which contains every generator of degree $-12,\dots,-6$ (Theorem A). So nonconstant strips have trivial stabilizers (Theorem B(1)). This removes the isotropy obstruction that defeats $\sigma$, whose fixed locus has complex dimension $3$. It does not prove invariant regularity.

Under an equivariant Floer homotopy hypothesis this yields a reduction of the bit to the orbit spectrum (Theorem C). It also shows that the unframed equivariant data cannot decide the bit, and that the framed orbit spectrum must depend on the brane (Theorem D, Remark 5.1). Theorem E locates the bit in the framings of an explicit orbit-level window.

### 1.3 Results

Notation: $S=\{uv+p(z)=0\}$, $p(z)=\prod_{k=0}^5(z-k)$. In real coordinates $x=(u+v)/2$, $y=(u-v)/(2i)$ we have $S=\{x^2+y^2+p(z)=0\}$. $R_\theta$ is the rotation of the $(x,y)$-plane, i.e. $(u,v,z)\mapsto(e^{i\theta}u,e^{-i\theta}v,z)$. Generators are labelled as in [32, Table 1]:
* $a_1,\dots,a_7$ in degree $-7$;
* $b_1,\dots,b_{12}$ in degree $-8$;
* $c_1,\dots,c_{19}$ in degree $-9$.

$t=(3,11)$, $u=(2,11)$ and $v=(4,13)$ are the Khovanov classes in degrees $-8,-9,-9$.

**Theorem A (the circle action; unconditional).**
1. $R_\theta$ preserves $S$, the hypersurface trivialization $\Phi_{\rm hyp}$, the real locus, and every matching sphere $\Sigma_\gamma=\{z\in\gamma,|u|=|v|\}$. On $S$ it fixes exactly the six nodes $(0,0,k)$. Together with $\sigma$ it generates $O(2)$: $\sigma R_\theta\sigma=R_{-\theta}$. (The $O(2)$-symmetry of Seidel–Smith spaces is known [13, §1].)
2. In Manolescu's model of $\mathcal Y_3$ by tuples $(A,D,U,V)$ with $U^2+V^2+p=AD$ [5, Prop. 2.7], the action is $(U,V)\mapsto R_\theta(U,V)$. For every $\theta\notin2\pi\mathbb Z$, its fixed set is the $20$ points $(A,p/A,0,0)$ with $A\mid p$. Every other point has trivial stabilizer. So the action is semifree, and free on the complement of the $20$ points.
3. $L$ and $L'$ are invariant, and each contains $8$ fixed points. $L\cap L'$ contains exactly $2$ of them, the generators $(p_0,p_2,p_4)$ and $(p_1,p_3,p_5)$ in degrees $-13$ and $-5$. The canonical brane pair of [34, Thm. F] is $O(2)$-equivariant, with representation $\mathbb R^2_{(1)}\oplus\mathbb R$ on each factor.
4. $L\cap L'$ has $29$ Morse–Bott components, each a torus $T^c$ ($c\le3$).
   * $U(1)$ acts diagonally and freely on the $27$ with $c\ge1$, with trivial orbit bundle $T^c\cong U(1)\times T^{c-1}$.
   * Invariant Morse–Bott data give $57$ free critical orbits. Their levels $n$ (the degree of the lower cell) have multiplicities $(1,5,11,14,14,5,7)$ for $n=-14,\dots,-8$.
   * The tops of the components lie in degrees $-11$ ($7$), $-9$ ($13$) and $-7$ ($7$).
   * In the window, the $7$ orbits of level $-8$ are those of $a_1,\dots,a_7$. The $5$ orbits of level $-9$ lie in the tori of $a_1$, $a_2$ (two orbits), $a_6$ and $a_7$.

**Theorem B (no isotropy obstruction).**
1. *(Unconditional.)* Every nonconstant strip with boundary on $(L,L')$ has trivial stabilizer in $U(1)$. So $U(1)$ acts freely on all moduli spaces of nonconstant strips, and on all spaces of cascades between free orbits.
2. *(Under (U-FFC).)* The cochain complex has the block form (3.1). In particular $\delta$ vanishes on the $7$ bottoms of the level-$(-8)$ orbits, and $\operatorname{rk}\delta^{-8}\le5$.
3. *(Computed; a support statement.)* Consider the support allowed by positivity (J) and by the block form (3.1). In every degree $-14\le k\le-8$ its term rank is at least the rank forced over $\mathbb F_2$ and over $\mathbb Q$, even after all internal ($D=0$) entries are removed (Table 3). So the rank obstruction of [33, Thm. E] does not occur at the level of supports. In particular, the rank-$6$ rectangle matrix of [33] is not of $U(1)$-block form.

B(1) excludes one obstruction only: nontrivial isotropy of nonconstant strips. It does not give invariant regularity (§3). B(3) is a necessary condition: it does not construct a differential with the block coefficients of (3.1) and $\delta^2=0$.

**Theorem C (Gysin reduction; under (U-FFC), (H$_\mathbb Z$)).** Let $Y'$ be the free truncation of §4.1. Let $B'=Y'_{hU(1)}$ be its orbit spectrum, the realization of the framed quotient flow category $\mathcal B$, with one cell for each critical orbit of level $-13,\dots,-8$. Let $e$ be the action of $c_1\in H^2(BU(1))$, and $\pi^*,\pi_!$ the Gysin maps.
1. $\pi^*$ and $\pi_!$ commute with $\mathrm{Sq}^1$ and $\mathrm{Sq}^2$ on all classes ($\pi_!$ lowering degree by $1$).
2. $\pi_!:HF^{-7}(\mathbb Z)\to H^{-8}(B';\mathbb Z)$ is an isomorphism onto $\mathbb Z^3$, and $\pi_!:HF^{-7}(\mathbb F_2)\to H^{-8}(B';\mathbb F_2)$ is an isomorphism. We have $H^{-9}(B';\mathbb Z)\cong\mathbb Z/m$ with $m\in\{1,2\}$, and $\operatorname{coker}(e:H^{-10}(B';\mathbb Z)\to H^{-8}(B';\mathbb Z))\cong\mathbb Z/(2/m)$. Moreover $\ker\big(e|_{H^{-10}(B';\mathbb Z)}\big)\cong\mathbb Z$, generated by $w=\pi_!(v)$.
3. **(Bit formula.)** $\pi_!(\mathrm{Sq}^2v_F)=\mathrm{Sq}^2(\rho w)$ in $H^{-8}(B';\mathbb F_2)$. So the decisive bit vanishes iff $\mathrm{Sq}^2(\rho w)=0$ in the orbit spectrum, i.e. iff the $\eta$-attachment of the Euler-kernel class $w$ to the top cells of $B'$ vanishes.
4. The BV operator $\Delta:H^k\to H^{k-1}$ of the action commutes with $\mathrm{Sq}^1$ and $\mathrm{Sq}^2$, and $\Delta(t)=0$. Its rank on $HF^{-7}$ is $2-m$.
5. *(Computed.)* These constraints do not decide the bit. The Gysin dimension count and the $\Delta$-constraints are satisfiable for $S_0$, for $S_1$, and for each of the six tables $T_c+\rho X$ of [34, Thm. G(4)], with both values of $m$.

**Theorem D (brane-blindness of the unframed data; under (U-FFC)$_G$, (BT)$_G$, (H$_2$), (Mod$_2$), (H$_\mathbb Z$)).** Let $G\subset O(2)$ be closed, e.g. $U(1)$, $\langle\sigma\rangle$ or $O(2)$.
1. *(Unconditional.)* Every class $\epsilon\in H^2(L;\mathbb F_2)$ is $w_2$ of a $G$-equivariant brane change $\kappa_\epsilon$.
2. Let $\sum\epsilon_i$ be odd. Write $\mathcal F_{\rm can}$ and $\mathcal F_\epsilon$ for the $G$-equivariant theories of $(b^{\rm can},b'^{\rm can})$ and $(b^{\rm can}+\kappa_\epsilon,b'^{\rm can})$. They have the same equivariant unframed flow category and the same signs, hence the same integral cochain complex with its $G$-action. If $U(1)\subset G$, they also share:
   * the unframed quotient category $\mathcal B^\circ$ and its signs;
   * the cellular cochain complex of $B'$ and the Euler cochain map $\varepsilon$ of (3.1);
   * the groups $H^*(B';\mathbb Z)$ with $e$, the class $w$, and the maps $\pi^*$, $\pi_!$, $\Delta$ on cohomology.
3. Their squares on $v_F$ differ: $\mathrm{Sq}^2_\epsilon(v_F)-\mathrm{Sq}^2_{\rm can}(v_F)=\mu(v_F)\neq0$.

Hence no argument that uses only $G$-equivariance and the data listed in (2) can decide the bit.

D(2) does **not** list the framed quotient category $\mathcal B$ or the orbit spectrum $B'$. Remark 5.1 shows that, for $U(1)\subset G$, the two framed orbit spectra are not equivalent by any equivalence that is the identity on cellular cohomology. They differ in the framings of $1$-dimensional quotient moduli spaces.

**Theorem E (orbit-level window).** Let $\mathcal B$ be the framed quotient flow category of (U-FFC), with $7$, $5$ and $14$ objects in degrees $-8,-9,-10$.
1. *(Supports; under (U-FFC), (J); Tables 4–6.)*
   * $\delta^{-9}_{\mathcal B}$ has $18$ admissible entries with $D\neq0$ and $5$ internal ones. Under (Loc) the internal ones vanish.
   * The $1$-dimensional quotient moduli spaces $\mathcal M_{\mathcal B}(O_i,n)$ can be nonempty only for the $73$ pairs with $D\ge0$, $D\ne0$, and for one pair with $D=0$, inside the $a_2$-torus. The same $74$ pairs bound the support of the Euler entries $\varepsilon(O_i,n)$.
   * Their boundaries lie over the $5$ level-$(-9)$ orbits. There are $200$ admissible triples $(O_i,m,n)$, and for each of the $73$ pairs at least one intermediate orbit is admissible.
2. *(LOS form; under (U-FFC).)* Choose a cocycle $\varphi$ for $\rho w$ in the cellular cochain complex of $B'$, and let $f$ be the framing of $\mathcal B$. Then $\mathrm{Sq}^2(\rho w)=[\mathrm{sq}^\varphi_f]$, where $\mathrm{sq}^\varphi_f$ is the Lobb–Orson–Schütz cochain [10] of $\mathcal B$ in degrees $-10,-9,-8$. It depends only on the objects, the signed rigid moduli spaces and the framed $1$-dimensional moduli spaces in these degrees.
3. *(Where the bit sits; under (U-FFC)$_{U(1)}$, (BT)$_{U(1)}$, (H$_2$), (Mod$_2$), (H$_\mathbb Z$).)* Let $f_{\rm can}$ and $f_\epsilon$ ($\sum\epsilon_i$ odd) be the framings of the common unframed category $\mathcal B^\circ$ given by the two branes of Theorem D.
   * (a) The bit vanishes iff $[\mathrm{sq}^\varphi_{f_{\rm can}}]=0$.
   * (b) $[\mathrm{sq}^\varphi_{f_\epsilon}]-[\mathrm{sq}^\varphi_{f_{\rm can}}]=\pi_!(\mu(v_F))\neq0$. So $[\mathrm{sq}^\varphi_f]$ is not determined by $\mathcal B^\circ$ and its signs.
   * (c) If $f_{\rm can}$ and $f_\epsilon$ agree on the closed components, then they differ on at least one interval component of some $\mathcal M_{\mathcal B}(O_i,n)$ with $\varphi(n)=1$. The pair $(O_i,n)$ is one of the $74$ pairs of Table 6.
   * (d) Not determined here: the components of the $1$-dimensional moduli spaces and their end matchings; the rigid counts of $\delta^{-9}_{\mathcal B}$ (the $18$ entries with $D\neq0$) and of $\delta^{-10}_{\mathcal B}$; hence $\varphi$; and the frame values of $f_{\rm can}$.

**Proposition F (the fibred picture).**
1. *(Dirichlet lifts; elementary.)* Use the integrable structure on $S$ and the matching locus $\{|u|=|v|\}$. Let $\Omega\subset\mathbb C$ be a bounded simply connected domain with smooth boundary, and let $w$ be holomorphic near $\overline\Omega$ with $p\circ w\neq0$ on $\partial\Omega$. Lifts $(f,g,w)$ of $w$ to $S$, with $f,g$ holomorphic on $\Omega$ and continuous on $\overline\Omega$ and with $|f|=|g|$ on $\partial\Omega$, are in bijection with pairs $(Z_f,\lambda)$. Here $Z_f$ is an effective divisor with $Z_f\le\operatorname{div}(p\circ w)|_\Omega$ and $\lambda\in U(1)$. The factor $\lambda$ is the action of $R_\theta$, and it acts freely.
2. *(Census.)* The $73$ positive orbit pairs of Table 6 have $1$, $2$ or $3$ moving coordinates ($15$, $27$, $31$ pairs). $12$ of them have maximal multiplicity $2$.
3. *(Search.)* No presentation in the searched Hilden double coset or conjugacy family has fewer than $116$ generators (computational, with the stated search bounds).

**Status of the bit: not decided.** The sharpest statements proved are Theorem C(3) and Theorem E(3). Under the hypotheses, the bit is $\mathrm{Sq}^2(\rho w)$ for one canonical integral class $w$ of the orbit spectrum. It is computed by the LOS cochain of the framed quotient category in three degrees, with $74$ possible supports for the $1$-dimensional moduli spaces and $5$ intermediate objects. It is not a function of the unframed quotient data, by Theorem E(3)(b). Those unframed data are not determined here either (E(3)(d)). So what remains is the canonical framing of $\mathcal B$ in these degrees, *together with* the unframed data on which the LOS formula is evaluated.

### 1.4 Hypotheses

The unconditional results are:
* Theorem A;
* Theorem B(1) and (3), the latter as a statement about supports;
* the computations behind C(5) and E(1), as statements about the stated algebraic constraints;
* Theorem D(1);
* Proposition F.

The rest uses the following hypotheses:
* (FFC), (BT), (H$_2$), (Mod$_2$), (Amb) are those of [34, §1.3]. (H$_\mathbb Z$) is $HF^*(L,L';\mathbb Z)\cong\bigoplus_{h-q=*}\mathrm{Kh}^{h,q}(T(3,4);\mathbb Z)$ [32, §1.3], an integral form of the isomorphism proved over fields of characteristic zero by Abouzaid–Smith [6, 7]; see [12] for the bigrading. (J) is the positivity hypothesis [32, Prop. D].
* **(U-FFC)** The canonical Floer flow category has a $U(1)$-equivariant Morse–Bott refinement with the following properties:
  * its objects are the $57$ free critical orbits and the $2$ fixed points;
  * its moduli spaces are compact $U(1)$-manifolds with corners, framed $U(1)$-equivariantly by the equivariant canonical brane;
  * its realization is a finite $U(1)$-CW spectrum whose underlying spectrum is the canonical Floer spectrum, with orbit cells $U(1)_+\wedge e^n$ in the order of levels; the attaching map from the cell of $O''$ to the cell of $O$ is built from $\mathcal M(O,O'')$ and is null when that space is empty;
  * the quotient of its free part is a framed flow category $\mathcal B$, with framings induced by the equivariant ones, whose realization is the orbit spectrum.
* **(U-FFC)$_G$** for closed $G\subset O(2)$: a $G$-equivariant refinement of (FFC), framed $G$-equivariantly by the equivariant brane, for both brane pairs of Theorem D. For $U(1)\subset G$ it includes (U-FFC) for both pairs.
* **(BT)$_G$** is (BT) for $G$-equivariant brane changes. Explicitly: the twisted pair keeps the $G$-equivariant unframed category and its signs, and changes only the frames of $1$-dimensional moduli spaces, by the incidence rule of [34, Thm. B]. For $U(1)\subset G$ we include in (BT)$_G$ that the two quotient categories have the same unframed category $\mathcal B^\circ$ and the same signs.
* **(Loc)** The local Morse–Bott model of each component is the external product of the clean-circle models, with trivial orientation local systems.

(U-FFC) is the equivariant analogue of (FFC). Theorem B(1) removes one obstruction to its transversality part. Invariant regularity is not proved; it is part of (U-FFC). Foundations of framed and spectral Floer theory are developed in [14, 20, 21, 22]. What is not available in the literature, to our knowledge, is a construction of equivariant framed Floer homotopy types for semifree circle actions in this setting. We do not supply it.

### 1.5 What is known and what is new

* **Known.**
  * Manolescu's model and the torus action on the product region [5, Prop. 2.7, Cor. 2.9, §4].
  * The $O(2)$-symmetry [13].
  * Equivariant Floer homology without equivariant transversality [19, 29] (§9).
  * Gysin sequences, the BV operator of a circle action and Borel localization [25, 26].
  * The LOS formula [10] and its dependence on frame values [31, Prop. D].
  * The generator tables, engine and positivity [32]; the brane framework and the one-bit criterion [34]; the lifted engine [33].
* **New, to our knowledge.**
  * The semifreeness theorem A(2)–(4) with its orbit decomposition.
  * Theorem B(3), as a support computation.
  * The conditional Gysin reduction C(2)–(4): the Euler-kernel class $w$, the dichotomy $m$, and $\Delta(t)=0$.
  * Theorem D with Remark 5.1: which equivariant data are brane-independent, and the brane dependence of the framed orbit spectrum.
  * The orbit-level window E.
  * The census and search in F(2)–(3).
* **Not claimed.**
  * No holomorphic strip in $\mathcal Y_3$ is computed.
  * No frame is computed.
  * Invariant regularity and (U-FFC) are not proved.
  * No geometric formula for the Euler entries $\varepsilon$ is given.
  * No counting theorem for the fibred picture is given, and none is excluded.
  * The bit is not decided.

## 2. The circle action (Theorem A)

**2.1 On $S$.** $F=x^2+y^2+p(z)$ is invariant under $R_\theta$, and $\nabla F$ is equivariant (verify.py §2). $R_\theta$ is real orthogonal, so the splitting $\overline{\nabla F}/|\nabla F|^2$, and with it $\Phi_{\rm hyp}$, is equivariant. It also preserves $\mathbb R^3$. In $(u,v)$ the action is $(e^{i\theta}u,e^{-i\theta}v)$, so it preserves $|u|$, $|v|$ and $uv$.

On $\mathbb R^2$, $\det(R_\theta-1)=2-2\cos\theta$. So a nontrivial rotation fixes only points with $x=y=0$, which forces $p(z)=0$: these are the six nodes, the poles of the matching spheres [18]. Finally $\sigma=\mathrm{diag}(1,-1,1)$ satisfies $\sigma R_\theta\sigma=R_{-\theta}$.

For a $U(1)$-invariant Kähler form, parallel transport preserves the moment level $|u|^2-|v|^2=0$. Manolescu shows that the matching Lagrangians lie in the zero level of the torus moment map on the product region [5, §4]. So every matching sphere is invariant, and so are $L$ and $L'$. As in [33, Thm. A(1)], the product model can be taken with a form invariant under $\sigma$ and $U(1)$.

**2.2 On $\mathcal Y_3$.** By [5, Prop. 2.7] a point of $\mathcal Y_3$ is a tuple $(A,D,U,V)$ of polynomials with the following properties:
* $A$ is monic of degree $3$, and $\deg U,\deg V\le2$;
* $U^2+V^2+p=AD$;
* the corresponding ideal is $(A(z),\,x-U(z),\,y-V(z))$.

The rotation acts by $(U,V)\mapsto R_\theta(U,V)$, coefficientwise. A fixed point has $(R_\theta-1)(U,V)=0$, hence $U=V=0$ and $AD=p$. So $A$ is the product of three of the six linear factors of $p$, which gives the $20$ points (verify.py §3, exact division). These do not depend on $\theta$, so every other point has trivial stabilizer: the action is semifree.

A fixed point lies on $L$ iff it is a triple of poles, one over an end of each $\alpha_i$ ($8$ points). It lies on $L'$ iff it has one end of each $\beta_j$; the $\beta$-arcs join $(p_0,p_3)$, $(p_1,p_4)$, $(p_2,p_5)$ ($8$ points). The common ones are $(p_0,p_2,p_4)$ and $(p_1,p_3,p_5)$, the two generators of degrees $-13$ and $-5$ ([34, §6] lists them).

**2.3 The canonical brane.** By [34, Thm. F(3)], $b^{\rm can}(L)$ is the constant null-homotopy of the Gauss map relative to $\Phi_{\rm hyp}$. $R_\theta$ and $\sigma$ are constant real matrices that preserve $\mathbb R^3$, so this null-homotopy is $O(2)$-equivariant, with representation $\mathbb R^3=\mathbb R^2_{(1)}\oplus\mathbb R$. The brane of $L'$ is obtained by continuation along polynomials $p_t$ [34, Thm. F(4)]. Every $S_{p_t}$ carries the same $O(2)$, and $\Phi_{\rm hyp}(p_t)$ is equivariant, so continuation commutes with $O(2)$.

**2.4 Components and orbits.** A component is a triple of planar intersection points, together with a permutation. It is a product of clean circles (interior crossings) and points (common endpoints), so it is a torus $T^c$ carrying $2^c$ generators with binomial degree multiplicities. The change of coordinates $(t_1,\dots,t_c)\mapsto(t_1,t_2-t_1,\dots,t_c-t_1)$ is unimodular. It identifies the diagonal action with $U(1)\times T^{c-1}$, so the orbit bundle $T^c\to T^{c-1}$ is trivial. Under (Loc), the internal part of the equivariant cell structure is then $U(1)$ times a cell structure on $T^{c-1}$, which has no Euler entries.

An invariant Morse–Bott function is pulled back from a perfect Morse function on $T^{c-1}$. So a component of bottom degree $b_0$ has $\binom{c-1}j$ critical orbits of level $b_0+j$, each orbit carrying cells in degrees $n$ and $n+1$.

Summing over the components (Table 1) gives the level counts. The identity $C^k=o_k+o_{k-1}+\#\{\text{fixed cells of degree }k\}$ holds for every $k$ (verify.py §4).

**Table 1** (window components: tops $a_1,\dots,a_7$; $c$ = number of circles).

| top | component | $c$ | cells |
|---|---|---|---|
| $a_1$ | $(x_7,x_{13},p_5)$ | 2 | $c_3;\ b_1,b_2;\ a_1$ |
| $a_2$ | $(x_7,x_{14},x_{21})$ | 3 | $d;\ c_6,c_7,c_8;\ b_3,b_4,b_5;\ a_2$ |
| $a_3$ | $(p_1,x_{12},p_5)$ | 1 | $b_6;\ a_3$ |
| $a_4$ | $(p_1,p_3,x_{19})$ | 1 | $b_7;\ a_4$ |
| $a_5$ | $(x_5,p_3,p_5)$ | 1 | $b_8;\ a_5$ |
| $a_6$ | $(p_1,x_{14},x_{20})$ | 2 | $c_{14};\ b_9,b_{10};\ a_6$ |
| $a_7$ | $(x_6,p_3,x_{21})$ | 2 | $c_{17};\ b_{11},b_{12};\ a_7$ |

The other $13$ components with cells in degree $-9$ have their tops there. They are:
* $(p_0,x_{13},p_5)$, $(p_0,x_{14},x_{21})$, $(p_1,p_2,x_{20})$, $(p_1,x_{12},x_{19})$, $(x_5,p_3,x_{19})$, $(x_5,x_{12},p_5)$, $(x_5,x_{14},x_{20})$;
* $(x_6,p_3,p_4)$, $(x_6,x_{12},x_{21})$, $(x_6,x_{13},x_{20})$, $(x_7,p_2,x_{21})$, $(x_7,x_{13},x_{19})$, $(x_7,x_{14},p_4)$.

**Table 2** (free orbits by level).

| $n$ | $-14$ | $-13$ | $-12$ | $-11$ | $-10$ | $-9$ | $-8$ |
|---|---|---|---|---|---|---|---|
| $o_n$ | 1 | 5 | 11 | 14 | 14 | 5 | 7 |

So $C^{-7}=7=o_{-8}$, $C^{-8}=12=7+5$ and $C^{-9}=19=5+14$. In the window every degree-$(-8)$ generator is either the bottom of a level-$(-8)$ orbit or the top of a level-$(-9)$ orbit.

## 3. Isotropy and the block form (Theorem B)

*Proof of B(1).* If $\lambda\neq1$ fixes a strip $u$ pointwise, then $u$ takes values in $\mathrm{Fix}(\lambda)$, which is the $20$ isolated points of Theorem A(2). So $u$ is constant. A parametrized strip with $\lambda u=u\circ\tau_c$ for an $\mathbb R$-translation $\tau_c$ defines a homomorphism $U(1)\to\mathbb R$, which is trivial. A cascade between free orbits with a nonconstant strip has trivial stabilizer for the same reason; one without nonconstant strips lies in a free torus component. $\square$

So the obstruction of [33, Thm. E] has no analogue here. That obstruction came from strips inside a fixed locus of positive dimension, whose normal operator could not be made surjective by invariant perturbations. Trivial stabilizers remove that mechanism, but they do not by themselves give invariant regularity. For that one needs, for example, points at which a strip is injective modulo the group action, so that invariant perturbations supported near them reach all of the cokernel; this is the analogue of the regular points of Floer–Hofer–Salamon [27]. We do not prove it. It is part of (U-FFC).

**3.1 The block form.** In a free $U(1)$-CW spectrum, the orbit cell $U(1)_+\wedge e^n$ of an orbit $O$ has a bottom cell $O_{\rm b}$ (degree $n$) and a top cell $O_{\rm t}$ (degree $n+1$). The equivariant attaching maps are classified as follows:
* *between adjacent levels*, by $\pi_0^s(U(1)_+)=\mathbb Z$: one integer $\delta_{\mathcal B}(O,O')$, the same for bottoms and tops up to a fixed sign convention;
* *between levels differing by $2$*, by $\pi_1^s(U(1)_+)=\pi_1^s(S^0)\oplus\pi_1^s(S^1)=\mathbb Z/2\oplus\mathbb Z$: an $\eta$-component and an integer $\varepsilon(O,O'')$, which links $O''_{\rm t}$ to $O_{\rm b}$. We call $\varepsilon(O,O'')$ the Euler entry.

So the cellular cochains are $C^k=\mathrm{Bot}_k\oplus\mathrm{Top}_k$, with
$$\delta(O'_{\rm b})=\sum\delta_{\mathcal B}(O,O')\,O_{\rm b},\qquad \delta(O''_{\rm t})=\sum\delta_{\mathcal B}(O,O'')\,O_{\rm t}+\sum\varepsilon(O,O'')\,O_{\rm b}. \tag{3.1}$$
There is no term from a bottom to a top. The bottoms form a subcomplex isomorphic to the cellular cochains $C^*(B')$, and the tops form the quotient, isomorphic to $C^{*-1}(B')$. The long exact sequence of $0\to\mathrm{Bot}\to C^*(Y')\to\mathrm{Top}\to0$ is the Gysin sequence of §4.2. Its connecting map is induced by the cochain map $\varepsilon$, and it is $e$ up to a universal sign. (verify.py §6 checks this bookkeeping on the model $S^{2k+1}\to\mathbb{CP}^k$, $k\le3$.) We use $\varepsilon$ only through this abstract description. We give no formula for $\varepsilon(O,O'')$ in terms of the geometry of $\mathcal M(O,O'')$; see §6.

The $7$ bottoms of level $-8$ map to bottoms of level $-7$, of which there are none, so they are cocycles. Hence $\operatorname{rk}\delta^{-8}=\operatorname{rk}\delta^{-9}_{\mathcal B}\le o_{-9}=5$. This proves B(2).

*Proof of B(3).* An entry from a cell of $K'$ to a cell of $K$ requires $D(K,K')\ge0$ by positivity [32, Prop. D]. Domains depend only on the components, and $D(K,K)=0$ (verify.py §5). Bipartite matching gives the term ranks in Table 3, with and without the internal $D=0$ entries. Each is at least the forced rank over $\mathbb F_2$ and over $\mathbb Q$, the latter recomputed from $c_k=h_k+r_k+r_{k-1}$. Since the inequality survives the removal of all internal entries, it does not depend on (Loc). $\square$

**Table 3** (term ranks of the $U(1)$-support, with/without internal $D=0$ entries, against the forced $\mathbb F_2$-rank).

| $k$ | $-14$ | $-13$ | $-12$ | $-11$ | $-10$ | $-9$ | $-8$ |
|---|---|---|---|---|---|---|---|
| term rank | 1/1 | 7/7 | 16/16 | 25/23 | 19/17 | 12/12 | 5/5 |
| forced | 1 | 6 | 9 | 16 | 10 | 7 | 4 |

Term ranks are tested degree by degree. They do not show that a differential exists with the repeated block coefficients of (3.1) and $\delta^2=0$. They only exclude the tested support obstruction.

*Contrast.* For both uniform $\sigma$-conventions, the six rectangles of [33, Thm. E(1)] give a matrix $C^{-8}\to C^{-7}$ of rank $6>5$. No $U(1)$-invariant structure produces that matrix. The obstruction of [33] is a feature of $\sigma$, not of equivariance as such.

## 4. The Gysin reduction (Theorem C)

**4.1 Truncation.** The cells of degree $\le-6$ form a subcomplex $F_{\le-6}$; it omits only the fixed cell of degree $-5$. The cells of orbit level $\le-14$, together with the fixed cell of degree $-13$, form an invariant subcomplex $G'$: a free orbit cell of level $n$ attaches to the equivariant $(n-1)$-skeleton.

$Y'=F_{\le-6}/G'$ is a finite free $U(1)$-CW spectrum. Its orbit levels are $-13,\dots,-8$. Every cell of degree $-12,\dots,-7$ belongs to $Y'$, so $H^k(Y')=HF^k$ for $k=-11,\dots,-7$, over any coefficients (verify.py §6). Steenrod squares from degree $-9$ to degree $-7$ may be computed in $Y'$: the quotient map $F_{\le-6}\to Y'$ is an isomorphism on $H^k$ for $-11\le k\le-7$.

**4.2 Gysin.** For a free $U(1)$-spectrum $Y$, the cofibre sequence $U(1)_+\to S^0\to S^{\mathbb C}$ smashed with $Y$ gives, after taking orbits, $Y\to Y_{hU(1)}\to(Y_{hU(1)})^{\ell}$, where $\ell$ is the tautological line. With the Thom isomorphism this is the Gysin sequence
$$\cdots\to H^{k-2}(B')\xrightarrow{e}H^k(B')\xrightarrow{\pi^*}H^k(Y')\xrightarrow{\pi_!}H^{k-1}(B')\xrightarrow{e}H^{k+1}(B')\to\cdots$$
At cochain level it is the sequence of §3.1. $\pi^*$ is induced by a map of spectra, and the connecting map is induced by a map $(B')^\ell\to\Sigma Y'$. Thus $\pi_!$ commutes with the Steenrod operations up to the Thom isomorphism, where $\mathrm{Sq}^2(U_\ell x)=U_\ell(\mathrm{Sq}^2x+e\,x)$ and $\mathrm{Sq}^1(U_\ell x)=U_\ell\mathrm{Sq}^1x$. Hence
$$\pi_!\mathrm{Sq}^2y=\mathrm{Sq}^2\pi_!y+e\,\pi_!y=\mathrm{Sq}^2\pi_!y,$$
because $\operatorname{im}\pi_!=\ker e$. This proves C(1).

*Proof of C(2).* Use $H^*(Y')=HF^*$ in degrees $-11,\dots,-7$, (H$_\mathbb Z$), and the fact that $B'$ has no cells above degree $-8$.
* *Degree $-7$.* $H^{-7}(B')=0$ and $H^{-6}(B')=0$, so $\pi_!:H^{-7}(Y')\to H^{-8}(B')$ is an isomorphism over any coefficients. So $H^{-8}(B';\mathbb Z)\cong HF^{-7}(\mathbb Z)=\mathbb Z^3$.
* *Degree $-8$.* $0\to\operatorname{coker}(e|_{H^{-10}})\to HF^{-8}(\mathbb Z)=\mathbb Z/2\to H^{-9}(B';\mathbb Z)\to0$. Rationally this gives $H^{-9}(B';\mathbb Q)=0$.
* *Degree $-9$.* $0\to\operatorname{coker}(e:H^{-11}\to H^{-9})\to HF^{-9}(\mathbb Z)=\mathbb Z\to\ker(e|_{H^{-10}})\to0$. The left term is torsion inside $\mathbb Z$, hence $0$. So $\pi_!$ maps $HF^{-9}(\mathbb Z)$ isomorphically onto $\ker e$, and $w=\pi_!(v)$ generates it.
* The degree-$(-8)$ sequence then gives the two cases $m=1$ and $m=2$.

The exhaustive dimension count of verify.py §6 recovers all of this over $\mathbb Q$ and $\mathbb F_2$. Over $\mathbb Q$, every solution has $\dim H^{-8}(B')=3$, $H^{-9}(B')=0$, $e$ onto, and $\ker e$ a line. Over $\mathbb F_2$ exactly the two cases occur. As a control, if the torsion class $t$ is removed, the dichotomy disappears. $\square$

*Proof of C(3).* By (H$_\mathbb Z$), $v$ generates $HF^{-9}(\mathbb Z)$, and $v_F=\rho(v)$ spans $\ker\mathrm{Sq}^1$. By C(1), $\pi_!\mathrm{Sq}^2v_F=\mathrm{Sq}^2\pi_!\rho(v)=\mathrm{Sq}^2\rho(w)$. Finally, $\pi_!$ is an isomorphism in degree $-7$ over $\mathbb F_2$ (C(2)). $\square$

*Proof of C(4).* The action map $\Sigma^\infty U(1)_+\wedge F\to F$, restricted to $S^1\wedge F$, is a stable map $\Sigma F\to F$. It induces $\Delta$, which therefore commutes with all stable operations.

On a free orbit cell, the action carries $e^1\times O_{\rm b}$ onto $O_{\rm t}$. So on $Y'$ we have $\Delta=\pi^*\pi_!$; at cochain level it sends $O_{\rm t}^*\mapsto O_{\rm b}^*$.

Now $\mathrm{Sq}^1u=t$, and $\mathrm{Sq}^1$ vanishes on $HF^{-10}$. So $\Delta t=\Delta\mathrm{Sq}^1u=\mathrm{Sq}^1\Delta u=0$.

On $HF^{-7}$, $\pi_!$ is an isomorphism onto $H^{-8}(B')$, and $\pi^*:H^{-8}(B')\to H^{-8}(Y')$ has image $\operatorname{coker}(e|_{H^{-10}})$. The mod-$2$ dimension of that image is $1$ for $m=1$ and $0$ for $m=2$. $\square$

*Proof of C(5).* verify.py §7 enumerates all $2^9$ degree-$(-1)$ maps on the ten-dimensional collapsed cohomology. It keeps those with $\Delta^2=0$ that commute with $\mathrm{Sq}^1$ and with the given $\mathrm{Sq}^2$-table. For $S_0$ and every table with $\rho=0$ there are $64$; for $S_1$ and every table with $\rho=1$ there are $32$. All have $\Delta t=0$, and in every case both ranks $0$ and $1$ on $HF^{-7}$ occur. Borel localization ($d_2=c\,\Delta$) gives $\#\text{odd}-\#\text{even}=6-4=2$, the number of fixed cells; both fixed cells have odd degree, and this does not depend on the table. $\square$

## 5. Brane-blindness of the unframed data (Theorem D)

*Proof of D(1).* On $\Sigma_{\alpha_i}\cong\mathbb{CP}^1$, the rotation fixing the two poles is induced by $\mathrm{diag}(1,e^{i\theta})$ on $\mathbb C^2$. So $\mathcal O(\pm1)$ are $U(1)$-equivariant. The reflection $\sigma|_{\Sigma_{\alpha_i}}$ is conjugate to $w\mapsto\bar w$, which lifts antilinearly to $\mathbb C^2$ and conjugates $e^{i\theta}$ to $e^{-i\theta}$. So the realification of $\mathcal O(1)$ is $O(2)$-equivariant. Exterior products $\boxtimes_i\mathcal O(\epsilon_i)$ with the diagonal action, realified and minus a trivial $\mathbb R^2$ (virtual rank $0$, so no grading shift), realize all $8$ classes $w_2=\sum\epsilon_ia_i$. $\square$

*Proof of D(2).* By (BT)$_G$, twisting the equivariant canonical brane by $\kappa_\epsilon$ keeps the equivariant unframed category and its signs. The frames change by the incidences $I_{Z_\epsilon}$ [34, Thm. B], where $Z_\epsilon$ is a union of pole loci; these are $O(2)$-invariant.

As in [34, proof of Thm. C(2), step 4], the signs, and hence the integral cochain complex, do not depend on the brane; the integral complex of a framed flow category depends only on its objects and signed rigid counts [31, Prop. D(1)]. Both theories have the same objects and the same cell basis. For $U(1)\subset G$, the splitting of each orbit cell into bottom and top is part of the equivariant cell structure, which is fixed by the objects. The entries $\delta_{\mathcal B}(O,O')$ and $\varepsilon(O,O'')$ are matrix entries of the integral complex in this basis (3.1). So they coincide too. By (BT)$_G$ the two quotient categories have the same unframed category $\mathcal B^\circ$ and signs. Everything else in D(2) is computed from (3.1): $C^*(B')=\mathrm{Bot}$, $\pi^*$ and $\pi_!$ from the inclusion and the projection, $e$ from $\varepsilon$, $\Delta=\pi^*\pi_!$, and $w=\pi_!(v)$ with $v$ the generator of $HF^{-9}(\mathbb Z)$. $\square$

*Proof of D(3).* The twist changes the parity of [34, Thm. C(2)]. By that theorem and (Mod$_2$), the two squares differ by $\mu$, which is conjugate to $X$ and injective on $HF^{-9}$. So $\mu(v_F)\neq0$ (verify.py §8: $X$ is injective on $HF^{-9}$ and $X(v)=(4,11)$). $\square$

**Remark 5.1 (the framed orbit spectrum depends on the brane).** Let $U(1)\subset G$. Identify the cellular cohomology of the two orbit spectra $B'_{\rm can}$ and $B'_\epsilon$ through their common cochain complex (D(2)). Apply C(3) to both theories. Since $\pi_!$ is the same map and is an isomorphism in degree $-7$,
$$\mathrm{Sq}^2_{B'_\epsilon}(\rho w)-\mathrm{Sq}^2_{B'_{\rm can}}(\rho w)=\pi_!\big(\mathrm{Sq}^2_\epsilon v_F-\mathrm{Sq}^2_{\rm can}v_F\big)=\pi_!(\mu(v_F))\neq0.$$
So no equivalence $B'_{\rm can}\simeq B'_\epsilon$ induces the identity on cellular cohomology. The two framed quotient categories have the same unframed category and signs, so by [31, Prop. D(1)] they differ in the framings of $1$-dimensional moduli spaces. This is the mechanism of Theorem E(3). In particular $B'$ cannot be added to the shared data of D(2): together with C(3) and the injectivity of $\pi_!$ in degree $-7$, that would contradict D(3).

*Reading.* This explains why both symmetry routes stop:
* the $\sigma$-route of [33], where the brane ambiguity $X$ has normal type $\sigma$ [33, Thm. D];
* the present $U(1)$-route.

A symmetry can localize or compress the computation (Theorems C, E), but the data it controls are shared by $b^{\rm can}$ and $b^{\rm can}+\kappa_\epsilon$. Any successful argument must use something that distinguishes them:
* the real structure of $L$ (constant Gauss map) together with an actual index computation along boundary paths, as math_39 [30] did for the trefoil;
* or a charge splitting (HW70, companion).

## 6. The orbit-level window (Theorem E)

Order the level-$(-8)$ orbits as $O_1,\dots,O_7$ (tops $a_1,\dots,a_7$). The level-$(-9)$ orbits are $m_1$ ($a_1$-torus), $m_2,m_2'$ ($a_2$-torus), $m_6$ and $m_7$. The level-$(-10)$ orbits $n_1,\dots,n_{14}$ are, in this order:
* the top orbits of $(p_0,x_{13},p_5)$, $(p_0,x_{14},x_{21})$, $(p_1,p_2,x_{20})$, $(p_1,x_{12},x_{19})$, $(x_5,p_3,x_{19})$, $(x_5,x_{12},p_5)$, $(x_5,x_{14},x_{20})$;
* the top orbits of $(x_6,p_3,p_4)$, $(x_6,x_{12},x_{21})$, $(x_6,x_{13},x_{20})$, $(x_7,p_2,x_{21})$, $(x_7,x_{13},x_{19})$, $(x_7,x_{14},p_4)$;
* the bottom orbit of the $a_2$-torus.

In Tables 4–6, "+" means $D\ge0,D\ne0$, "0" means $D=0$ and "." means not positive.

**Table 4** ($\delta^{-9}_{\mathcal B}$; rows $O_1..O_7$, columns $m_1,m_2,m_2',m_6,m_7$): `0++..`, `.00..`, `++++.`, `.++++`, `+++.+`, `.++0.`, `.++.0`.

**Table 5** ($\delta^{-10}_{\mathcal B}$; rows $m_1,m_2,m_2',m_6,m_7$, columns $n_1..n_{14}$): `++...++.++++++`, `.+....+.+++++0`, `.+....+.+++++0`, `.+++..+.++++++`, `.+..+.++++++++`.

**Table 6** (possible supports of the $1$-dimensional quotient moduli spaces $\mathcal M_{\mathcal B}(O_i,n_l)$, and of the Euler entries $\varepsilon(O_i,n_l)$; rows $O_1..O_7$): `++...++.++++++`, `.+....+.+++++0`, `++++.++.++++++`, `.++++.++++++++`, `++..++++++++++`, `.+++..+.++++++`, `.+..+.++++++++`.

*Proof of E(1).* Supports follow from positivity, as in B(3). By (U-FFC), $\mathcal M_{\mathcal B}(O_i,n)$ is the quotient of the free $U(1)$-manifold $\mathcal M(O_i,n)$, and its boundary consists of products $\mathcal M_{\mathcal B}(O_i,m)\times\mathcal M_{\mathcal B}(m,n)$ with $m$ of level $-9$. Additivity of domains, checked on all triples, gives the $200$ admissible triples, distributed $30,55,55,30,30$ over $m_1,m_2,m_2',m_6,m_7$. By (U-FFC), the equivariant attaching map from the cell of $n$ to the cell of $O_i$ is null if $\mathcal M(O_i,n)=\emptyset$. So $\varepsilon(O_i,n)$ can be nonzero only on the $74$ pairs of Table 6. Under (Loc) the internal entries of $\delta^{-9}_{\mathcal B}$ are Morse pieces of a perfect function on $T^{c-1}$: two flow lines of opposite sign. $\square$

The table is only a support bound for $\varepsilon$. The integer $\varepsilon(O_i,n)$ is not a relative Euler number of the circle bundle $\mathcal M(O_i,n)\to\mathcal M_{\mathcal B}(O_i,n)$: the base is a compact $1$-manifold with boundary, so its absolute and relative $H^2$ vanish, while the Gysin count needs a nonzero Euler map ($e$ is onto a $3$-dimensional space over $\mathbb Q$). The integer $\varepsilon(O_i,n)$ is the $\pi_1^s(S^1)$-component of an equivariant attaching map (§3.1). Expressing it through phase, evaluation and gluing data of the families would need the construction behind (U-FFC); we do not attempt it, and nothing below uses it.

*Proof of E(2).* By (U-FFC), $B'$ is the realization of $\mathcal B$. As in §4.1, $H^{-10}(B'/\mathrm{sk}_{-11})\to H^{-10}(B')$ is onto and $H^{-8}$ is unchanged, so by naturality $\mathrm{Sq}^2$ on $H^{-10}(B')$ is computed by the full subcategory on levels $-10,-9,-8$. LOS [10, Defs. 3.1–3.3, 3.12; Thm. 3.13] applied to that framed $1$-flow category gives $\mathrm{Sq}^2(\rho w)=[\mathrm{sq}^\varphi_f]$. The cochain uses only the listed data. $\square$

*Proof of E(3).* (a) is C(3) with E(2) for the canonical theory. For (b), apply E(2) to both theories with the same cocycle $\varphi$, which exists because the cochain complexes coincide (D(2)). Then use Remark 5.1. For (c), the two framed categories have the same unframed category and signs. If they agree on closed components, they differ only by interval frame values $\varepsilon_0=f_\epsilon-f_{\rm can}$. By [31, Prop. D(1)] and its proof, $\mathrm{sq}^\varphi_{f_\epsilon}-\mathrm{sq}^\varphi_{f_{\rm can}}=E_{\varepsilon_0}\varphi$, where $(E_{\varepsilon_0}\varphi)(O)$ is the sum of $\varepsilon_0(I)$ over the interval components $I$ of $\mathcal M_{\mathcal B}(O,n)$ with $\varphi(n)=1$. By (b) this cochain is nonzero, so some such $I$ has $\varepsilon_0(I)=1$. Its pair $(O,n)$ has $\mathcal M_{\mathcal B}(O,n)\neq\emptyset$, so it is in Table 6 by E(1). (d) is a list. $\square$

E(3) does not say that the bit is an affine function on a known parameter space. The components of the moduli spaces, their end matchings and the rigid counts are unknown. So the set of framings, and $\varphi$, are not explicit. What E(3) proves is narrower: once these unframed data are fixed, the bit is decided by the canonical frame values, and the brane twist shows that the frame values matter.

Compared with the generator-level window, this is a compression of the possible supports:
* [32] has $97$ positive pairs and $12$ intermediate generators; [34, Thm. C(3)] has $91$ brane-sensitive pairs;
* here there are $73+1$ pairs and $5$ intermediate objects, all inside four tori.

## 7. What is computed and what is not

| item | status |
|---|---|
| fixed points, semifreeness, equivariance of $b^{\rm can}$ | proved (A) |
| no nontrivial stabilizers of nonconstant strips | proved (B(1)) |
| invariant regularity | **not proved**; part of (U-FFC) |
| support term ranks $\ge$ forced ranks | computed (B(3)); necessary condition only |
| block form, Gysin, $w$, $m$-dichotomy, $\Delta(t)=0$ | proved under (U-FFC), (H$_\mathbb Z$) (C) |
| BV/Gysin constraints decide the bit | **no** (C(5), computed) |
| equivariant lifts of all $w_2$-classes | proved (D(1)) |
| unframed data decide the bit | **no** (D(2)–(3), under (U-FFC)$_G$, (BT)$_G$, (H$_2$), (Mod$_2$), (H$_\mathbb Z$)) |
| framed orbit spectrum brane-independent | **no** (Remark 5.1, same hypotheses) |
| supports, $73$ classes, $200$ triples | computed under (J) (E(1)) |
| geometric meaning of the Euler entries | **not established** |
| components, end matchings, rigid counts, frames | **not computed** |
| the bit | **not decided** |

## 8. The fibred picture (Proposition F)

*Proof of F(1).* A lift of $w$ is $(f,g,w)$ with $fg=-p\circ w$ and $|f|=|g|$ on $\partial\Omega$. Equivalently, $|f|^2=|p\circ w|$ on $\partial\Omega$. Since $p\circ w\neq0$ on $\partial\Omega$, $f$ has no zeros on $\partial\Omega$. Its zero divisor $Z_f$ in $\Omega$ satisfies $Z_f\le\operatorname{div}(p\circ w)$, because $g$ is holomorphic.

Given $Z_f$, let $B_Z$ be the Blaschke product of $Z_f$ transported by a Riemann map; it is smooth up to $\partial\Omega$ and $|B_Z|=1$ there. Then $f/B_Z$ has no zeros, so $\log|f/B_Z|$ is harmonic with boundary values $\tfrac12\log|p\circ w|$. On a simply connected $\Omega$ this determines $f/B_Z$ up to a unimodular constant. Conversely, for each $Z_f\le\operatorname{div}(p\circ w)$ and $\lambda\in U(1)$, $f=\lambda B_Z\exp(h+i\tilde h)$, with $h$ the harmonic extension and $\tilde h$ a conjugate, and $g=-p\circ w/f$ give a lift. Changing $\lambda$ is the action $(f,g)\mapsto(\lambda f,\lambda^{-1}g)$ of $R_\theta$; it is free because $f\not\equiv0$. $\square$

verify.py §10 checks the model $w=\zeta$, $p=z-\tfrac12$ on the unit disc exactly. With $f=(\zeta-\tfrac12)(1-\zeta/2)^{-1/2}$ and $g=-(1-\zeta/2)^{1/2}$, we have $|f|=|g|$ on $|\zeta|=1$, and $|f|\neq|g|$ inside.

**Remark 8.1 (scope; not a theorem).** On the product region, $\mathcal Y_3$ is locally $S\times S\times S$ modulo the labelling. In the spirit of the cylindrical reformulation of Heegaard Floer theory [15, 16], strips correspond to curves on a $3$-fold branched cover of the strip. Suppose that every component of this source is simply connected, that its boundary avoids the roots, and that its sheet is not constant at a node. Then F(1) applies to each component, and the phases give a free $T^r$-action, with diagonal $R_\theta$. We do not verify these conditions. Components through common endpoints have punctures at roots, which F(1) does not treat. Constant sheets at poles carry no phase, so they contribute no circle factor. So we do not claim that the split structure gives free $T^r$-families in general.

*Consequences for the method.*
1. Where Remark 8.1 applies, strips of the split structure over a base class come in positive-dimensional families. Rigid counts then require a perturbation, and become cascade counts that depend on perturbation data, as [33, Thm. E] shows for $\sigma$-symmetric data.
2. This does not exclude a combinatorial theorem for suitably perturbed cascade counts. We only record that this manuscript supplies no such theorem. The Sarkar–Wang mechanism [17] is proved for $\mathrm{Sym}^g$ of a surface, and we know no analogue in $\mathcal Y_3$. Positivity (J) is the only input we use, and it is what Theorem E uses.
3. Census (F(2)) and search (F(3)):
   * verify.py §11 classifies the $73$ classes as $(1,1)\times15$, $(2,1)\times27$, $(3,1)\times19$, $(3,2)\times12$, where the pair is (moving coordinates, maximal multiplicity). A moving coordinate is one of the three planar coordinates in which the two components differ.
   * Left multiplication by the $194$ Hilden elements of length $\le3$ and conjugation by $3$-strand words of length $\le3$ never reduce the $116$ generators. A broader exploratory search (length $\le5$) also found none. This is a computational observation, not a minimality theorem.

## 9. Relation to published work

* **math_75 [34].** We use:
  * its canonical brane and its equivariance mechanism;
  * the boundary-incidence formula and (BT);
  * the one-bit criterion G(4), and its tables $S_0$, $S_1$, $T_c+\rho X$.

  Its Thm. E(2) uses a circle action only at fixed generators and notes that this does not reach the window. Theorem A shows why: the window is free. Theorems C–E are what the free part gives instead.
* **math_66 [33].** It is the $\sigma$-route, and its Theorem E is the no-go for $\sigma$-invariant $J$ integrable on $W$. Its notes discarded the $U(1)$ action because no window generator is $U(1)$-fixed. Here we use exactly that freeness. We use its engine (copied, credited) and the rank $6$ of its rectangle matrix as a control.
* **math_55 [32].** Generators, gradings, positivity, forced ranks and (H$_\mathbb Z$).
* **math_52 [31], math_39 [30].**
  * [31]: the dependence of the LOS square on frame values, used in Remark 5.1 and E(3).
  * [30]: the model of an actual frame computation, which Theorem D says is needed.
* **Equivariant Floer theory.** Hendricks–Lipshitz–Sarkar constructed $\mathbb Z/2$-equivariant Floer cohomology by a flexible method [19]. In [29] they constructed $G$-equivariant Floer homology for a Lie group $G$ acting symplectically and preserving the pair, without equivariant transversality, with a sample application to symplectic Khovanov homology. This is existing equivariant theory for our setting. It is a theory of (co)homology groups. It does not provide the framed equivariant Floer spectrum, the framed quotient flow category or the Steenrod squares that (U-FFC) assumes, and our results do not follow from it. We do not use [29]. Whether the cohomological statements of C(2) can be obtained from [29] alone, without (U-FFC), we leave open.
* **Other literature.**
  * Manolescu [5]: the model and the torus action on the product region.
  * Hendricks–Mak–Raghunath [13]: the $O(2)$-symmetry, $\mathbb Z/2$-localizations, and a $\mathbb Z/p$ conjecture. Our $U(1)$-semifreeness and Gysin reduction do not appear there.
  * Seidel–Smith [11]: localization for involutions, and stabilization for equivariant transversality.
  * Khovanov–Seidel [18]: matching spheres in $A_m$-fibres.
  * Lipshitz–Sarkar [8, 9, 24]: the Steenrod-square framework. The survey [24] records that no symplectic Khovanov homotopy type is constructed.
  * Tao [28]: a combinatorial $\mathrm{Sq}^2$ for grid homology with explicit framings, built on the Manolescu–Sarkar construction [23]. Its key input, explicit framings of rectangle-decomposition moduli spaces in $\mathrm{Sym}^n$ of a torus, has no counterpart here (§8).

## 10. Limitations

1. **The bit is not decided.**
2. **Hypotheses.** Theorems C–E rest on (U-FFC) (and (U-FFC)$_G$), (BT)$_G$ and (Loc), none of which is proved. They are the equivariant analogues of the hypotheses of [32, 34].
3. **Transversality.** Theorem B(1) excludes only nontrivial stabilizers of nonconstant strips. Invariant regularity is assumed in (U-FFC). Theorem B(3) tests supports degree by degree and constructs no differential.
4. **Brane dependence.** Only unframed data are brane-independent. The framed orbit spectrum depends on the brane (Remark 5.1).
5. **Euler entries.** We give no geometric formula for $\varepsilon(O,O'')$; only the abstract Gysin identity and a support bound are used.
6. **Positivity.** All supports use (J). The supports are necessary conditions only; we do not show that any entry is nonzero.
7. **Fibred picture.** F(1) is a lemma about simply connected domains with boundary avoiding the roots. Its use for branched cylindrical sources (Remark 8.1) is not justified here. F(3) is a bounded search, not a theorem.
8. **No strip of $\mathcal Y_3$ is computed.** The only holomorphic computation is the model of F(1).

## 11. Verification

verify.py ($63$ checks, FALLOS = 0, about $25$ s) uses exact integer, rational and sympy arithmetic. Tags: [C] computation, [K] cited input, [N] negative control. The checks certify finite statements only: orbit and support data, the enumerated algebraic constraints, and the bounded search. They do not construct moduli spaces, framed realizations, Euler entries or frames. Its sections are:

| § | content |
|---|---|
| 1 | engine of [32, 33] (copied) and regression |
| 2 | rotation identities |
| 3 | the $20$ fixed points (exact division), semifreeness |
| 4 | components, orbits, Tables 1–2 |
| 5 | domains, block form, Table 3, the [33] control |
| 6 | Gysin enumeration over $\mathbb Q$ and $\mathbb F_2$, torsion control; cellular Gysin model $S^{2k+1}\to\mathbb{CP}^k$ with control |
| 7 | $\Delta$-enumeration for the eight tables, localization parity |
| 8 | equivariant lifts; $X$ injective on $HF^{-9}$, $X(v)\ne0$ (input of D(3)) |
| 9 | Tables 4–6, rank-$4$ realizability, $200$ triples |
| 10 | Dirichlet model |
| 11 | census, search, control |

verify.mpl mirrors §§2–4, 6, 7, 8 (in part), 9 and 10 in Maple (about $320$ lines). Status: not executed in Maple.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086.
3. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
4. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514.
5. C. Manolescu, *Nilpotent slices, Hilbert schemes, and the Jones polynomial*, Duke Math. J. 132 (2006), 311–369; arXiv:math/0411015 (Prop. 2.7, Cor. 2.9, §4).
6. M. Abouzaid, I. Smith, *Khovanov homology from Floer cohomology*, J. Amer. Math. Soc. 32 (2019), 1–79.
7. M. Abouzaid, I. Smith, *The symplectic arc algebra is formal*, Duke Math. J. 165 (2016), 985–1060.
8. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042.
9. R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848.
10. A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500.
11. P. Seidel, I. Smith, *Localization for involutions in Floer cohomology*, Geom. Funct. Anal. 20 (2010), 1464–1501.
12. Z. Cheng, *Bigrading the symplectic Khovanov cohomology*, Algebr. Geom. Topol. 23 (2023); arXiv:2111.07792.
13. K. Hendricks, C. Y. Mak, S. Raghunath, *Symplectic annular Khovanov homology and fixed point localizations*, arXiv:2408.06453.
14. N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257.
15. R. Lipshitz, *A cylindrical reformulation of Heegaard Floer homology*, Geom. Topol. 10 (2006), 955–1097.
16. P. Ozsváth, Z. Szabó, *Holomorphic disks and topological invariants for closed three-manifolds*, Ann. of Math. 159 (2004), 1027–1158.
17. S. Sarkar, J. Wang, *An algorithm for computing some Heegaard Floer homologies*, Ann. of Math. 171 (2010), 1213–1236.
18. M. Khovanov, P. Seidel, *Quivers, Floer cohomology, and braid group actions*, J. Amer. Math. Soc. 15 (2002), 203–271.
19. K. Hendricks, R. Lipshitz, S. Sarkar, *A flexible construction of equivariant Floer homology and applications*, J. Topol. 9 (2016), 1153–1236.
20. T. Large, *Spectral Fukaya categories for Liouville manifolds*, PhD thesis, MIT, 2021.
21. M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.
22. K. Blakey, C. M. Bonciocat, *Parameterized Lagrangian Floer homotopy*, arXiv:2506.20122.
23. C. Manolescu, S. Sarkar, *A knot Floer stable homotopy type*, arXiv:2108.13566.
24. R. Lipshitz, S. Sarkar, *Spectra in Khovanov and knot Floer theories*, arXiv:2401.06218.
25. T. tom Dieck, *Transformation Groups*, de Gruyter Stud. Math. 8, 1987.
26. W.-Y. Hsiang, *Cohomology Theory of Topological Transformation Groups*, Ergeb. Math. 85, Springer, 1975.
27. A. Floer, H. Hofer, D. Salamon, *Transversality in elliptic Morse theory for the symplectic action*, Duke Math. J. 80 (1995), 251–292.
28. Y. Tao, *A Steenrod square for link Floer homology*, arXiv:2511.02000 (consulted at the level of the abstract).
29. K. Hendricks, R. Lipshitz, S. Sarkar, *A simplicial construction of G-equivariant Floer homology*, Proc. London Math. Soc. 121 (2020), 1798–1866.
30. rStation math_39 v1, *The framing bit of the trefoil in the adiabatic Seidel–Smith model vanishes*, https://rstation.ai/problems/math/papers/39/v1
31. rStation math_52 v1, *Decoupled framed flow categories and Steenrod squares beyond homology*, https://rstation.ai/problems/math/papers/52/v1
32. rStation math_55 v1, *The Steenrod square of $T(3,4)$ and the three-strand Seidel–Smith model: generators, positivity, and framings of the Khovanov flow category*, https://rstation.ai/problems/math/papers/55/v1
33. rStation math_66 v1, *The Seidel–Smith involution and the decisive Steenrod bit of $T(3,4)$: normal gradings, equivariant frame localization, and an obstruction to naive equivariant transversality*, https://rstation.ai/problems/math/papers/66/v1
34. rStation math_75 v1, *Brane twists and the Steenrod square of $T(3,4)$ in the three-strand Seidel–Smith model: a boundary-incidence formula, a $w_2$ selection rule, the unknot normalization, and the brane selected by the complex geometry*, https://rstation.ai/problems/math/papers/75/v1

Companion preprint (in preparation): on Maslov data, spherical twists and charge splittings for the same pair (HW70).

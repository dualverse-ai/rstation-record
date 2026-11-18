# The exact action spectrum of the isotropic Haydys–Witten sector at the Anderson–Henningson fold, with applications to action-filtered flow categories: spectral persistence, rigid windows, and a sign change of spectral invariants across the fold

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**

We compute the exact action spectrum of the isotropic Haydys–Witten (HW) sector on $\mathbb R\times S^3_r\times(0,L)$ with Nahm poles, for all $L$ beyond the Anderson–Henningson (AH) fold $L=\pi r$, and apply it to action-filtered homotopy types of the published HW flow categories near the fold. Following Hedenlund–Oldervoll, an action filtration turns a framed flow category into a diagram $t\mapsto|\mathcal C_{\ge t}|$ in $\mathrm{Fun}(\mathbb R^{\rm op},\mathrm{Sp})$.

(A) *Main result: isotropic sector, all $L>\pi r$.* Let $m\in(0,1)$ be the turning point of the static solution, $R=\sqrt{12-3m^2}$ and $k^2=2mR/(6-3m^2+mR)$. Then $L/r=2\sqrt6K(k)/\sqrt{6-3m^2+mR}$. The static action is finite and equals the Legendre transform $G=h\ell-S$ of the abbreviated action. Every nonconstant isotropic or Klein-symmetric trajectory has energy $E(L)=12\pi^2rG$. We prove $dE/dL=12\pi^2h\in(0,8\pi^2)$ and, with $\nu=L^2/r^2-\pi^2$, $E=r\big(\tfrac{8\sqrt{10}}5\nu^{3/2}-\tfrac{381\sqrt{10}}{250\pi^2}\nu^{5/2}+O(\nu^{7/2})\big)$; the leading term is from rStation math_46. For long intervals $E=8\pi^2L-12\sqrt3\pi^2r\log(2+\sqrt3)+864\pi^2re^{-2L/r}(1+o(1))$, with a global lower bound and interval-arithmetic enclosures.

(B) *Applications.* Recalling that the isotropic and $SU(2)\times SU(2)$ categories are contractible for every framing (rStation math_46 Cor. E, math_49 Thm. D(4), math_53 Thm. A(1)), their filtered types are sums of interval spectra with bars of length $E(L)$, pairwise at interleaving distance $E(L)/2$, which vanishes at the fold like $\nu^{3/2}$.

(C) *Quadrupole sector.* Adding the Lobb–Orson–Schütz conditions of rStation math_52 §7.3 in pairs gives even frame parity. The new point is that every proper action window is a wedge of spheres, although a standalone window admits framings realizing $S^1\cup_\eta e^3$. The filtered type is one of two explicit diagrams with identical homology persistence, distinguished by a $\pi_3$-bar of $\eta^2$.

(D) For calibrated filtrations, the spectral gap $c(\iota_1)-c(\iota_4)$ is positive below the fold and tends to $-E(L)$ above it.

verify.py: 129 checks, FALLOS = 0.

---

## 1. Introduction

### 1.1 Background

Haydys [9] and Witten [8] proposed Floer-type invariants with Kapustin–Witten (KW) solutions as critical points and Haydys–Witten (HW) instantons as flow lines. A homotopy-theoretic refinement needs a framed flow category in the sense of Cohen–Jones–Segal [3] and Lipshitz–Sarkar [4], or of Abouzaid–Blumberg [2]. A series of rStation papers has built such categories rigorously in the simplest geometry, $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends, near the Anderson–Henningson (AH) fold $L=\pi r$ [6, 7]:

* the AH instanton in the isotropic sector [27], and the complete isotropic flow category [34];
* the Klein-symmetric ($V_4$) sector [28], and the complete $SU(2)\times SU(2)$ category, on the round sphere [35] and on triaxial spheres [37];
* the full gauge-fixed theory near the fold: centre manifold, symmetry breaking by a quadrupole Higgs mass, smooth framed models, local compactness [30–33];
* framing questions, Steenrod squares and spherical reframings [38, 39];
* a solvable geometry, $\mathrm{Sol}^4$, in which every object has action $0$ [36].

All realizations found so far are contractible or $\Sigma^\infty(S^1\vee S^4)$.

The HW equations are a gradient flow, so these categories carry more than a spectrum: each object has an action and each morphism has an energy. Hedenlund–Oldervoll [1] showed that this datum, an *$A$-structure*, is homotopically meaningful. For a poset $A$ and the zero map $A\to U/O$ there is an equivalence $\mathcal Flow^A\simeq\mathrm{Fun}(A^{\rm op},\mathrm{Sp})$, $X\mapsto(a\mapsto X_a)$, where $X_a$ is the full subcategory on the objects of action $\ge a$ [1, Example 0.0.11]. In symplectic topology this is the setting of filtered Floer theory, barcodes and spectral invariants [13, 14, 23, 24, 25].

This paper computes the action-filtered homotopy types of the rigorously constructed HW categories, starting from the equations. The main new result is Theorem A, the exact action spectrum of the isotropic sector for all $L>\pi r$: the elliptic parametrization, the Legendre and Hamilton–Jacobi structure, the second fold coefficient, the long-interval law and rigorous enclosures. Theorems B–D are applications of Theorem A to the published categories.

*Relation to published work.* The categories themselves, their realizations and their reframings are recalled from the series [27–39], not claimed. In particular, the contractibility of the isotropic and $SU(2)\times SU(2)$ categories for every coherent framing is [34, Cor. E], [35, Thm. D(4)] and [39, Thm. A(1)]; given this, the bars of Theorem B follow from the two or four objects and the energy of Theorem A, and the interleaving distances are bottleneck distances of one or two bars. The frame parity C(1) is obtained by adding in pairs the Lobb–Orson–Schütz conditions written down in [38, §7.3]; the new quadrupole statement is the window rigidity and extension obstruction C(2) and the two filtered types C(3)–(4). The leading fold term of Theorem A(4) and the positivity of the action gap are [34, Thm. A(2)]. A detailed list is in §1.4.

### 1.2 Conventions

A framed flow category $\mathcal C$ is as in [4, §3]. It has graded objects; compact $\langle k\rangle$-manifolds $\overline{\mathcal M}(x,y)$ of dimension $|x|-|y|-1$ whose boundary strata are compositions; and coherent framings. Morphisms run from $x$ to $y$ with $|x|>|y|$. The CJS realization $|\mathcal C|$ is a finite CW spectrum with one cell of dimension $|x|$ for each object [3, 4]. Its cellular chain complex is $\partial x=\sum_{|y|=|x|-1}\#\mathcal M(x,y)\,y$. In the HW categories, trajectories run from lower to higher action (the flow is the *upward* gradient flow of the action in the conventions of [34]).

**Definition 1.1 (action filtration).** An *action filtration* of $\mathcal C$ is a function $f:\mathrm{Ob}(\mathcal C)\to\mathbb R$ such that $f(x)<f(y)$ whenever $x\ne y$ and $\mathcal M(x,y)\ne\emptyset$. It is *energy-calibrated* if every trajectory $u\in\mathcal M(x,y)$ has energy $E(u)=f(y)-f(x)$.

The relation generated by $\mathcal M(x,y)\neq\emptyset$ is a partial order on objects, and $f$ is an order-preserving map to $(\mathbb R,\le)$, i.e. an $\mathbb R$-structure in the sense of [1, Example 2.5.14]. For $t\in\mathbb R$ let $\mathcal C_{\ge t}$ be the full subcategory on $\{f\ge t\}$. It is closed under passing to targets of morphisms, so its realization is a subcomplex of $|\mathcal C|$ [4, §3]. The inclusions are strictly functorial in $t$, so
$$\Phi_f(\mathcal C):\ \mathbb R^{\rm op}\to\mathrm{Sp},\qquad t\mapsto|\mathcal C_{\ge t}|,$$
is an object of $\mathrm{Fun}(\mathbb R^{\rm op},\mathrm{Sp})$, the *filtered realization*. For $s\le t$, the *window* $W_{[s,t]}$ is the full subcategory on $\{s\le f\le t\}$. Its realization is the subquotient $|\mathcal C_{\ge s}|/|\mathcal C_{>t}|$ [4, §3].

*Relation with [1].* By [1, Example 0.0.11], the $\mathbb R$-structured category goes to $a\mapsto\mathrm{map}(1_a,\mathcal C)\simeq\mathrm{map}(1,\mathcal C_a)$, and $\mathcal C_a=\mathcal C_{\ge a}$. We work throughout with the cellular model $\Phi_f$. We do not use the identification of $\mathrm{map}(1,-)$ with the CJS realization, and none of our proofs depends on [1].

### 1.3 Results

Write $\nu=L^2/r^2-\pi^2$. For $m\in(0,1)$ and $\theta\in[0,\pi]$ put
$$\gamma(\theta)=1+\tfrac{1-\cos\theta}2+\tfrac{(1-\cos\theta)^2}4,\qquad \ell(m)=\int_0^\pi\frac{d\theta}{\sqrt{1-m^2\gamma(\theta)/3}},\qquad S(m)=m\int_0^\pi(1+\cos\theta)\sqrt{1-m^2\gamma(\theta)/3}\,d\theta,$$
$$h(m)=m-\tfrac{m^3}3,\qquad G(m)=h(m)\,\ell(m)-S(m).$$

**Theorem A (exact action spectrum of the isotropic sector; all $L>\pi r$).**
1. *(Parametrization.)* $\ell:(0,1)\to(\pi,\infty)$ is a strictly increasing real-analytic bijection. For $L>\pi r$ let $m=m(L)$ be defined by $\ell(m)=L/r$. Then the KW solution $k_+$ of [34] has turning point ${\rm Re}\,u=m/r$ at ${\rm Im}\,u=0$, and conserved quantity ${\rm Re}(u^3/3-r^{-2}u)=-h(m)/r^3$. Moreover
$$\ell(m)=\frac{2\sqrt6\,K(k)}{\sqrt{6-3m^2+mR}},\qquad R=\sqrt{12-3m^2},\qquad k^2=\frac{2mR}{6-3m^2+mR},$$
where $K$ is the complete elliptic integral of the first kind.
2. *(Action and energy.)* The static action
$$\mathfrak A[u]=6\pi^2r^3\int_0^L\Big[\tfrac12\big(p\,\partial_yq-q\,\partial_yp\big)+{\rm Re}\big(\tfrac{u^3}3-r^{-2}u\big)\Big]dy,\qquad u=p+iq,$$
is finite on $k_\pm$, and $\mathfrak A(k_\pm)=\mp6\pi^2r\,G(m)$. Here $S$ is the abbreviated action $\oint p\,dq$ and $G$ is its Legendre transform: $dS/dh=\ell$. Every nonconstant isotropic HW trajectory in the class of [34], and every nonconstant $V_4$ trajectory in the class of [35], runs from $k_+$ to $k_-$ and has energy
$$E(L)=\mathfrak A(k_-)-\mathfrak A(k_+)=12\pi^2r\,G(m(L)).$$
In the normalization of [34, Thm. A(2)], $\Delta\mathcal A(\nu)=2\ell^2G$.
3. *(Hamilton–Jacobi.)* $\dfrac{dE}{dL}=12\pi^2\,h(m(L))$. Since $h(m(L))$ increases from $0$ to $2/3$, $E$ is strictly increasing and strictly convex in $L$, with $0<dE/dL<8\pi^2$.
4. *(Fold expansion.)* $E=r\,\nu^{3/2}\Phi(\nu)$ with $\Phi$ real-analytic near $0$, and
$$E(L)=r\Big(\tfrac{8\sqrt{10}}5\,\nu^{3/2}-\tfrac{381\sqrt{10}}{250\pi^2}\,\nu^{5/2}+O(\nu^{7/2})\Big),\qquad \Delta\mathcal A=\tfrac{4\sqrt{10}}{15}\nu^{3/2}+\tfrac{19\sqrt{10}}{1500\pi^2}\nu^{5/2}+O(\nu^{7/2}).$$
5. *(Long intervals.)* For every $L>\pi r$,
$$E(L)>8\pi^2L-12\sqrt3\,\pi^2r\log(2+\sqrt3),$$
and as $L\to\infty$,
$$E(L)=8\pi^2L-12\sqrt3\,\pi^2r\log(2+\sqrt3)+864\,\pi^2r\,e^{-2L/r}\big(1+O(\tfrac Lr e^{-L/r})\big).$$
The slope $8\pi^2=12\pi^2\cdot\frac23$ is $6\pi^2$ times the difference $\frac43$ of the superpotential $u^3/3-u$ between its critical points $u=\pm1$. The constant is twice a Nahm-pole boundary energy $6\sqrt3\pi^2r\log(2+\sqrt3)$.
6. *(Rigorous values.)* Table 3.1 gives interval enclosures of $L/r$, $G$ and $E/r$, computed with outward rounding.

**Theorem B (persistence of the complete isotropic and $SU(2)\times SU(2)$ categories; an application of Theorem A).** Let $\pi r<L<\pi r+\delta$, with $\delta$ such that the complete categories $\mathcal C_{\rm iso}(L)$ of [34, Thm. D] and $\mathcal C_2(L)$ of [35, Thm. D] are defined. Equip them with their energy-calibrated action filtrations, normalized by $\mathfrak A$; for $\mathcal C_2$ this is $f(k_{ab})=\mathfrak A(k_a)+\mathfrak A(k_b)$. Write $E=E(L)$. Then, for every coherent framing (the framings for which the categories are contractible by [35, Thm. D(4)]):
1. $\Phi(\mathcal C_{\rm iso})\simeq I_{(-E/2,E/2]}S^0$ and $\Phi(\mathcal C_2)\simeq I_{(0,E]}S^0\oplus I_{(-E,0]}S^1$. The notation is that of §2: $I_{(a,b]}S^n$ is the interval spectrum, equal to $S^n$ for $a<t\le b$ and to $0$ otherwise. The attaching maps of the associated graded have degree $\pm1$.
2. $|\mathcal C_{\rm iso}|\simeq|\mathcal C_2|\simeq0$ (recalled: [34, Cor. E], [35, Thm. D(4)], [39, Thm. A(1)]), and the Conley indices are trivial. Nevertheless
$$d_I\big(\Phi(\mathcal C_{\rm iso}),0\big)=d_I\big(\Phi(\mathcal C_2),0\big)=d_I\big(\Phi(\mathcal C_{\rm iso}),\Phi(\mathcal C_2)\big)=E(L)/2>0 .$$
No increasing reparametrization of $\mathbb R$ identifies any two of $0$, $\Phi(\mathcal C_{\rm iso})$ and $\Phi(\mathcal C_2)$.
3. For $L,L'$ in the window,
$$d_I\big(\Phi(\mathcal C_{\rm iso}(L)),\Phi(\mathcal C_{\rm iso}(L'))\big)=\tfrac12|E(L)-E(L')|\le6\pi^2h(m(\max(L,L')))\,|L-L'|,$$
$$d_I\big(\Phi(\mathcal C_2(L)),\Phi(\mathcal C_2(L'))\big)=\min\big(|E(L)-E(L')|,\tfrac12\max(E(L),E(L'))\big).$$
4. *(Continuity across the fold.)* For $L<\pi r$ the categories are empty, so $\Phi=0$. Hence $L\mapsto\Phi(\mathcal C_{\rm iso}(L))$ is continuous at $L=\pi r$ for $d_I$, with $d_I=\frac{4\sqrt{10}}5r\,\nu^{3/2}(1+O(\nu))$. The modulus is exactly of order $(L-\pi r)^{3/2}$.

For the triaxial categories of [37, Thms. E–F] the same statements hold with $E$ replaced by the energy $E_c>0$ of the non-isotropic arrow, whose value we do not compute.

**Theorem C (the quadrupole sector: rigid windows and the two filtered types).** Let $\Sigma_Q=\Sigma_Q(\bar\nu,\varepsilon)$ be the eight-object local category of [31, Thm. C], with $\bar\nu<0$ and $0<\varepsilon<\varepsilon_0(\bar\nu)$. Its objects are $P_a^\pm$ in gradings $a+1$, $a=0,\dots,3$. Equip it with any coherent framing (in particular any of the reframings of [39]). Let $f$ be any action filtration with $f(P_a^+)=f(P_a^-)=:\varphi_a$; this holds for every action invariant under the antipodal symmetry $J$. Then $\varphi_0>\varphi_1>\varphi_2>\varphi_3$, and:
1. *(Frame parity; the conditions of [38, §7.3] added in pairs.)* The interval frame values $\lambda_{st}$ of $\mathcal M(P_2^s,P_0^t)$ and $\rho_{st}$ of $\mathcal M(P_3^s,P_1^t)$ satisfy $\sum_{s,t}\lambda_{st}\equiv\sum_{s,t}\rho_{st}\equiv0\bmod2$.
2. *(Rigid windows.)* $W_{[\varphi_2,\varphi_0]}\simeq S^1\vee S^3$ and $W_{[\varphi_3,\varphi_1]}\simeq S^2\vee S^4$. All windows of length two are wedges of two spheres. So every proper window is a wedge of spheres. The full window is $X_0=\Sigma^\infty(S^1\vee S^4)$ or $X_1=S^1\cup_{\eta^2}e^4$ [39]. By contrast, the standalone framed flow category $W_{[\varphi_2,\varphi_0]}$ admits framings, those of odd parity, with realization $S^1\cup_\eta e^3$. None of them extends to a coherent framing of $\Sigma_Q$.
3. *(The two filtered types.)* If $|\Sigma_Q|\simeq X_0$, then
$$\Phi_f(\Sigma_Q)\simeq Y_0:=F_{\varphi_0}S^1\oplus I_{(\varphi_1,\varphi_0]}S^1\oplus I_{(\varphi_2,\varphi_1]}S^2\oplus I_{(\varphi_3,\varphi_2]}S^3\oplus F_{\varphi_3}S^4 .$$
If $|\Sigma_Q|\simeq X_1$, then $\Phi_f(\Sigma_Q)\simeq Y_1:=J_{\varphi_3,\varphi_0}\oplus I_{(\varphi_1,\varphi_0]}S^1\oplus I_{(\varphi_2,\varphi_1]}S^2\oplus I_{(\varphi_3,\varphi_2]}S^3$, where $J_{\varphi_3,\varphi_0}={\rm cofib}\big(\eta^2:F_{\varphi_3}S^3\to F_{\varphi_0}S^1\big)$. Here $F_cS^n$ equals $S^n$ for $t\le c$ and $0$ for $t>c$.
4. *(Homology does not see the difference.)* $Y_0\not\simeq Y_1$, but $H_*(Y_0;A)\cong H_*(Y_1;A)$ as persistence modules, for every coefficient group $A$. In $Y_1$ the class $\eta^2\iota_1$ has the finite $\pi_3$-bar $(\varphi_3,\varphi_0]$; in $Y_0$ its bar is infinite.

**Remark 1.2 (finer than realization and Conley index; a bar count).** Let $\Sigma_H$ be the two-object height category below the fold [31, Thm. C′], [32, Thm. 3(4)], with its model framing and any action filtration $g$. Then $|\Sigma_Q|\simeq|\Sigma_H|\simeq\Sigma^\infty h(\bar B)$ for the model framings [32], but $\Phi_f(\Sigma_Q)\not\simeq\Phi_g(\Sigma_H)$ even after reparametrization. Indeed
$$d_I\big(\Phi_f(\Sigma_Q),\Phi_g(\Sigma_H)\big)=\max\Big(|\varphi_0-g(P_1)|,\ |\varphi_3-g(P_4)|,\ \max_a\tfrac{\varphi_a-\varphi_{a+1}}2\Big)>0 .$$

**Theorem D (spectral invariants across the fold; an application of Theorem A).** For $a\in H_*(|\mathcal C|;\mathbb Z)$ let $c_f(a)=\sup\{t: a\in{\rm im}(H_*(|\mathcal C_{\ge t}|)\to H_*(|\mathcal C|))\}$. Let $\iota_1,\iota_4$ generate $H_1,H_4$ of $|\mathcal C|\simeq X_0$ or $X_1$, and put $\gamma_f=c_f(\iota_1)-c_f(\iota_4)$.
1. *(Below the fold, unconditional.)* For $\Sigma_Q$ and $\Sigma_H$, every coherent framing and every action filtration: $\gamma_f=\max f-\min f>0$.
2. *(Leading energies.)* Every trajectory $u\in\mathcal M(P_a^s,P_b^{s'})$ of $\Sigma_Q$ has $X$-energy
$$E_X(u)=\tfrac{\pi}{18}\,\varepsilon|\bar\nu|\,(c_a-c_b)\big(1+O(|\bar\nu|^{1/2})\big)+O_{\bar\nu}(\varepsilon^2),$$
where $c_0<c_1<c_2<c_3$ is the spectrum of the quadrupole $C$. For every filtration calibrated to this order (Definition 6.3), $\gamma_f=\frac\pi{18}\varepsilon|\bar\nu|(c_3-c_0)(1+O(|\bar\nu|^{1/2}))+O_{\bar\nu}(\varepsilon^2)$.
3. *(Above the fold.)* Let $\Sigma_E(\varepsilon)$ be the two-object category of [32, Thm. 3(3)], with $\bar\nu>0$, whose objects $k_\pm(\varepsilon)$ have gradings $1$ and $4$. For every family of filtrations that is calibrated by continuity at $\varepsilon=0$ (Definition 6.4), $\gamma_{f_\varepsilon}\to-c_0E(L)<0$ as $\varepsilon\to0$. Here $c_0=c_0(L)>0$ is the normalization constant relating $E_X$ to the HW energy on isotropic configurations (§6.3), and $E(L)$ is given by Theorem A.
4. Hence the sign of $\gamma$ changes at the fold, although the realization is $X_0$, the suspended Conley index, on both sides [31, 32].

### 1.4 What is new, and what is imported

**New.**
* Theorem A in full: the elliptic parametrization of the length, the Legendre structure, the identification $\Delta\mathcal A=2\ell^2G$, the Hamilton–Jacobi identity, the second fold coefficient, the long-interval law with its constants, and the interval enclosures. [34] proved $\Delta\mathcal A>0$, $\Delta\mathcal A'=2P_1$ and the leading term $\frac23\sqrt{8/5}\,\nu^{3/2}$; Theorem A(4) recovers that term (verify.py S4).
* The filtered realizations of the HW categories treated here, and their interleaving distances (Theorems B, C(3)–(4), Remark 1.2). For the isotropic and $SU(2)\times SU(2)$ categories (Theorem B) these are applications of Theorem A: the contractibility for every coherent framing is recalled from [34, Cor. E], [35, Thm. D(4)], [39, Thm. A(1)], and the bars then follow from the object count and the energy. Remark 1.2 is a bar count.
* The rigidity of windows C(2) and the extension obstruction. The frame parity C(1) is not new as such: it follows by adding in pairs the four Lobb–Orson–Schütz conditions written down in [38, §7.3] (Proposition 5.1), and by Remark 5.3 it is the vanishing $\Gamma_1=0$ of [39]. [38, §7.3] also counted the 32 compatible frame assignments and showed that $\mathrm{Sq}^2$ vanishes on the *total* realization, where it vanishes for degree reasons. The new content is the window statement C(2).
* Spectral invariants for HW categories and the sign change across the fold (Theorem D), with the leading-order energies of the quadrupole trajectories. D(2)–(3) depend on the calibration Definitions 6.3–6.4 (see *Not claimed*).

**Imported, not claimed.**
* The HW categories, their objects, morphism spaces, transversality and compactness: [27–39]. Specifically: (F2), the energy identity and Theorem D of [34]; Theorems B and D of [35]; Theorems E–F of [37]; Theorems C, C′ and Lemma 4.2, Corollary 4.3 of [31]; Theorems 1 and 3 of [32]; the realizations $X_0,X_1$ and the classification of reframings in [39]; the count of compatible frame assignments and the Lobb–Orson–Schütz conditions for $\Sigma_Q$ in [38, §7.3]; contractibility of the isotropic and $SU(2)\times SU(2)$ categories for every coherent framing [34, Cor. E], [35, Thm. D(4)], [39, Thm. A(1)].
* The Hedenlund–Oldervoll framework [1], used only for motivation; the Lipshitz–Sarkar realization and its subcomplexes [4]; the Lobb–Orson–Schütz 1-flow calculus and its $\mathrm{Sq}^2$ formula [5]; the isometry theorem for persistence modules [10–12]; Yoneda's lemma in $\mathrm{Fun}(\mathbb R^{\rm op},\mathrm{Sp})$ [15]; the expansion of $K$ near $k=1$ [17]; minimal cell structures [16]; stable stems [21].

**Not claimed.** The existence of a renormalized HW action functional in the full gauge-fixed theory. This is why Theorem D(2)–(3) are stated for calibrated filtrations, which such a functional would produce. We also do not claim exact (non-leading) energies in the quadrupole sector, the value of $E_c$ for triaxial metrics, or any statement outside the fold windows where the categories are known.

## 2. Filtered realizations, interval spectra and interleavings

Throughout, $\mathrm{Fun}=\mathrm{Fun}(\mathbb R^{\rm op},\mathrm{Sp})$. For $t\le s$ there is a unique morphism $s\to t$ in $\mathbb R^{\rm op}$, and $X(s)\to X(t)$ denotes the structure map. A natural transformation is an equivalence iff it is a pointwise equivalence [15, §5.1.2]. A map of bounded-below spectra is an equivalence iff it induces an isomorphism on $H_*(-;\mathbb Z)$.

**Definition 2.1 (free and interval spectra).** For $c\in\mathbb R$ let $F_c=\Sigma^\infty_+\mathrm{Map}_{\mathbb R^{\rm op}}(c,-)$. Then $F_c(t)=\mathbb S$ for $t\le c$ and $F_c(t)=0$ for $t>c$, with identity structure maps. Put $F_cS^n=\Sigma^nF_c$. For $a<b$ the unique map $F_a\to F_b$ corresponding to $1\in\pi_0F_b(a)$ has cofibre
$$I_{(a,b]}S^n={\rm cofib}(\Sigma^nF_a\to\Sigma^nF_b),$$
which is $S^n$ for $a<t\le b$ and $0$ otherwise.

**Lemma 2.2 (Yoneda).** For $Y\in\mathrm{Fun}$:
1. $\mathrm{Map}(F_cS^n,Y)\simeq\Omega^{\infty+n}Y(c)$, by evaluation at $c$;
2. $\mathrm{Map}(I_{(a,b]}S^n,Y)\simeq{\rm fib}\big(\Omega^{\infty+n}Y(b)\to\Omega^{\infty+n}Y(a)\big)$, induced by the structure map. If $Y(a)\simeq0$, then evaluation at $b$ identifies $\pi_0\mathrm{Map}(I_{(a,b]}S^n,Y)$ with $\pi_nY(b)$, compatibly with composition.

*Proof.* (1) is the Yoneda lemma together with the adjunction $\Sigma^\infty_+\dashv\Omega^\infty$, pointwise [15, §5.1.3]. (2) follows by applying $\mathrm{Map}(-,Y)$ to the cofibre sequence of Definition 2.1. Compatibility with composition holds because evaluation at $b$ is a functor. ∎

**Definition 2.3 (interleaving).** For $\delta\ge0$ let $X[\delta](t)=X(t-\delta)$. The structure maps give $\sigma^X_\delta:X\to X[\delta]$. $X$ and $Y$ are *$\delta$-interleaved* if there are maps $\alpha:X\to Y[\delta]$ and $\beta:Y\to X[\delta]$ with $\beta[\delta]\circ\alpha\simeq\sigma^X_{2\delta}$ and $\alpha[\delta]\circ\beta\simeq\sigma^Y_{2\delta}$ in the homotopy category of $\mathrm{Fun}$. Put $d_I(X,Y)=\inf\{\delta\}$.

Interleavings compose and add, so $d_I$ is an extended pseudometric. It is bounded below by the interleaving distance of $H_n(-;\mathbb F)$ for every $n$ and every field $\mathbb F$.

**Lemma 2.4 (homology lower bound).** Let $X,Y\in\mathrm{Fun}$ be pointwise finite, with finitely many critical values. Then $d_I(X,Y)\ge d_B\big(\mathrm{bc}\,H_n(X;\mathbb F),\mathrm{bc}\,H_n(Y;\mathbb F)\big)$ for every $n$ and every field $\mathbb F$. Here ${\rm bc}$ is the barcode and $d_B$ the bottleneck distance.

*Proof.* $H_n(-;\mathbb F)$ maps $\delta$-interleavings to $\delta$-interleavings of persistence modules, after reindexing by $t\mapsto-t$. The modules are pointwise finite-dimensional, so the isometry theorem [11, 12], [10, Thm. 5.14] gives $d_I=d_B$ for them. ∎

The bottleneck cost of matching bars $(a,b]$ and $(a',b']$ is $\max(|a-a'|,|b-b'|)$, and that of leaving $(a,b]$ unmatched is $(b-a)/2$. Infinite bars must be matched with infinite bars of the same degree, at cost $|b-b'|$.

**Lemma 2.5 (interval calculus).** Fix $n$.
1. $I_{(a,b]}S^n$ is $\delta$-interleaved with $0$ iff $2\delta\ge b-a$.
2. $F_aS^n$ and $F_{a'}S^n$ are $|a-a'|$-interleaved.
3. If $\delta\ge\max(|a-a'|,|b-b'|)$, then $I_{(a,b]}S^n$ and $I_{(a',b']}S^n$ are $\delta$-interleaved.
4. Interleavings of summands give interleavings of direct sums.

Consequently, if $X$ and $Y$ are finite sums of free and interval spectra, then $d_I(X,Y)$ equals the bottleneck distance of their degreewise barcodes.

*Proof.* (1) $X$ is $\delta$-interleaved with $0$ iff $\sigma_{2\delta}\simeq0$. We have $I_{(a,b]}[2\delta]=I_{(a+2\delta,b+2\delta]}$, which vanishes at $a$. By Lemma 2.2(2), $\pi_0\mathrm{Map}(I_{(a,b]},I_{(a,b]}[2\delta])=\pi_n$ of the value at $b$. This is $\mathbb Z$ if $a+2\delta<b$ and $0$ otherwise, and $\sigma_{2\delta}$ corresponds to $1$ in the first case.

(2) Let $\delta=|a-a'|$. Then $F_{a'}[\delta]=F_{a'+\delta}$, and $\pi_0\mathrm{Map}(F_a,F_{a'+\delta})=\pi_0F_{a'+\delta}(a)=\mathbb Z$ since $a\le a'+\delta$. Take the class $1$ in both directions. The composite is the class $1\cdot1=1\in\pi_0F_{a+2\delta}(a)$, which is $\sigma_{2\delta}$.

(3) $I_{(a',b']}[\delta]=I_{(a'+\delta,b'+\delta]}$ vanishes at $a$ because $a\le a'+\delta$. If $a'+\delta<b$, the value at $b$ is $S^n$; take $\alpha$ of degree $1$, and otherwise $\alpha=0$. Define $\beta$ symmetrically. If $2\delta\ge b-a$, the composites are null-homotopic, as is $\sigma_{2\delta}$, by (1) and Lemma 2.2. If $2\delta<b-a$, then $b-a'\ge b-a-\delta>\delta$ and $b'-a>\delta$. So both $\alpha$ and $\beta$ have degree $1$. The composite has degree $1$ at $b$, and by Lemma 2.2(2) it equals $\sigma_{2\delta}$.

(4) is clear. For the consequence, an optimal bottleneck matching between barcodes of the same degree gives an interleaving by (1)–(4). Lemma 2.4 gives the reverse inequality, because $H_*(F_cS^n)$ and $H_*(I_{(a,b]}S^n)$ are the corresponding bars. ∎

**Lemma 2.6 (shift stability).** If $f,g$ are action filtrations of the same framed flow category with $\|f-g\|_\infty\le\delta$, then $\Phi_f$ and $\Phi_g$ are $\delta$-interleaved, and $|c_f(a)-c_g(a)|\le\delta$ for every class $a$.

*Proof.* $\{f\ge t\}\subset\{g\ge t-\delta\}\subset\{f\ge t-2\delta\}$. So inclusions of subcomplexes give $\Phi_f\to\Phi_g[\delta]\to\Phi_f[2\delta]$, and the composite is the inclusion $\sigma_{2\delta}$. The same holds with $f$ and $g$ exchanged. The statement about $c$ follows from the same inclusions. ∎

**Lemma 2.7 (splitting criterion).** Let $X\in\mathrm{Fun}$ be piecewise constant, i.e. its structure maps are identities on each interval between consecutive critical values. Suppose there are summands $Z_j\in\{F_cS^n,I_{(a,b]}S^n\}$ and maps $Z_j\to X$ such that, for every $t$, the induced map $\bigoplus_jZ_j(t)\to X(t)$ is an $H_*(-;\mathbb Z)$-isomorphism. Then $X\simeq\bigoplus_jZ_j$. A map $F_cS^n\to X$ is a class in $\pi_nX(c)$. A map $I_{(a,b]}S^n\to X$ is a class $\alpha\in\pi_nX(b)$ together with a null-homotopy of its image in $X(a)$; it exists iff that image vanishes in $\pi_nX(a)$.

*Proof.* Lemma 2.2 and the pointwise criterion for equivalences. ∎

## 3. The exact action spectrum of the isotropic sector (proof of Theorem A)

By scaling $(s,y,u)\mapsto(s/r,y/r,ru)$ [34, §1.2] we take $r=1$ until the end of §3.6. The isotropic HW equation is $\partial_su+i\partial_yu=\bar u^2-1$ [27, Thm. A], [34, (1.1)], and static solutions satisfy $u'=-i(\bar u^2-1)$.

### 3.1 Hamiltonian structure

**Lemma 3.1.** With $u=p+iq$ and $H(p,q)={\rm Re}(u^3/3-u)=p^3/3-pq^2-p$:
1. the static equation is $p'=-2pq=\partial_qH$, $q'=q^2+1-p^2=-\partial_pH$, and $H$ is conserved;
2. it is the Euler–Lagrange equation of $\int\big[\frac12(pq'-qp')+H\big]dy$, and ${\rm Re}(i\bar u'u)=pq'-qp'$;
3. on the level set $H=-h$ one has $pq'=h-\frac23p^3$ and $(pq)'=2p-\frac43p^3-h$.

*Proof.* Direct computation (verify.py S1). For (3), $H=-h$ gives $pq^2=p^3/3-p+h$. Substitute this into $pq'=pq^2+p-p^3$ and into $(pq)'=p'q+pq'=-pq^2+p-p^3$. ∎

**Lemma 3.2 (the object $k_+$).** Let $L>\pi$ and let $k_+$ be the isotropic KW solution of [34, (F2)]. There is a unique $y_0\in(0,L)$ with $q(y_0)=0$. The number $m:=p(y_0)$ lies in $(0,1)$, and along $k_+$ we have $H\equiv-h(m)$ with $h(m)=m-m^3/3\in(0,\frac23)$. Moreover $p$ increases on $(0,y_0)$, decreases on $(y_0,L)$, and tends to $0$ at both ends.

*Proof.* By [34, proof of Thm. A(2)], $p>0$ on $k_+$ and $|p|<\sqrt{q^2+1}$ on genuine solutions. So $q'=q^2+1-p^2>0$. The Nahm poles give $q\to-\infty$ at $y=0$ and $q\to+\infty$ at $y=L$, so $q$ has exactly one zero. At it, $m^2<1$, and $H=m^3/3-m=-h(m)$. Since $p'=-2pq$ has the sign of $-q$, $p$ is monotone on each side. Finally $p=O(y^{3/2})$ at $y=0$, and symmetrically at $y=L$, by [34, Thm. B(2)]. ∎

### 3.2 Length, abbreviated action and the elliptic form

For $0<m<1$ the cubic $p^3/3-p+h(m)$ factors as $\frac13(p-m)(p-p_2)(p-p_a)$, with $p_{2}=\frac{-m+R}2>m$ and $p_a=\frac{-m-R}2<0$, where $R=\sqrt{12-3m^2}$. Moreover $(p-p_a)(p_2-p)=3-m^2-mp-p^2$ (verify.py S2).

**Proposition 3.3.** On $k_+$:
$$L=\int_0^m\frac{dp}{\sqrt{Q(p)}}=\ell(m),\qquad Q(p)=\tfrac13\,p(m-p)(p-p_a)(p_2-p),$$
$$S:=\int_{k_+}p\,dq=2\int_0^m\sqrt{\tfrac{p^2}3-1+\tfrac hp}\,dp=S(m),$$
with $\ell,S$ as in §1.3. Moreover $\ell(m)=2\sqrt6K(k)/\sqrt{6-3m^2+mR}$ with $k^2=2mR/(6-3m^2+mR)$.

*Proof.* On $(0,y_0)$ we have $q=-\sqrt{p^2/3-1+h/p}$ by $H=-h$, and $dy=dp/p'=dp/(2p|q|)=dp/(2\sqrt{Q(p)})$, since $p^2(p^2/3-1+h/p)=Q(p)$. The interval $(y_0,L)$ contributes the same amount. This gives $L=\int_0^mQ^{-1/2}dp$.

Next, $\int p\,dq=[pq]-\int q\,dp$. The boundary term vanishes because $pq=O(y^{1/2})$ at the poles (Lemma 3.2 and $q\sim-1/y$). On each half, $-\int q\,dp=\int_0^m|q|\,dp$.

Substitute $p=m(1-\cos\theta)/2$. Then $dp/\sqrt{p(m-p)}=d\theta$ and $\sqrt{(m-p)/p}\,dp=\frac m2(1+\cos\theta)d\theta$. Also $3-m^2-mp-p^2=3(1-m^2\gamma(\theta)/3)$ (verify.py S2). This gives the $\theta$-formulas.

The elliptic form is the standard reduction of $\int_b^c dx/\sqrt{(x-a)(x-b)(c-x)(d-x)}=2K(k)/\sqrt{(d-b)(c-a)}$, $k^2=\frac{(c-b)(d-a)}{(d-b)(c-a)}$ for $a<b<c<d$ [18]. Apply it with $(a,b,c,d)=(p_a,0,m,p_2)$, and use $p_2(m-p_a)=\frac12(6-3m^2+mR)$ and $p_2-p_a=R$ (verify.py S2). A high-precision cross-check against direct integration along the orbit, in the $q$-parametrization, is verify.py S3. ∎

**Lemma 3.4.**
1. $\ell$ is strictly increasing, $\ell(0^+)=\pi$ and $\ell(1^-)=\infty$. Both $\ell$ and $S$ extend real-analytically to $|m|<1$, with $\ell$ even and $S$ odd.
2. $\dfrac{dS}{dm}=\ell(m)\,h'(m)$, i.e. $dS/dh=\ell$.
3. $\dfrac{dG}{dm}=h(m)\,\ell'(m)$, so $G(m)=\int_0^mh\,d\ell>0$ and $dG/d\ell=h$.

*Proof.* (1) $\gamma$ is increasing on $[0,\pi]$, with $\gamma(0)=1$ and $\gamma(\pi)=3$ (verify.py S2). For complex $|m|<1$ we have $|m^2\gamma/3|<1$, so the integrands are analytic in $m$, and they depend on $m^2$ (times $m$ for $S$). The integrand of $\ell$ is strictly increasing in $m>0$. At $m=1$ it is $\big((1-p)(2+p)/3\big)^{-1/2}$ with $p=(1-\cos\theta)/2$, which has a non-integrable singularity $\asymp(\pi-\theta)^{-1}$ at $\theta=\pi$. Monotone convergence gives $\ell(1^-)=\infty$.

(2) Write $S(h)=2\int_0^{m(h)}q(p,h)\,dp$ with $q(p,h)=\sqrt{p^2/3-1+h/p}$. Since $q(m(h),h)=0$, the Leibniz boundary term vanishes. Also $\partial_hq=1/(2pq)$ is integrable on $(0,m)$: it is $O((hp)^{-1/2})$ at $0$ and $O((m-p)^{-1/2})$ at $m$. Hence $dS/dh=\int_0^m dp/(p\,q)=\int_0^mQ^{-1/2}dp=\ell$. The interchange of derivative and integral is justified by dominated convergence after the substitution $p=m(h)\,\tau$, $\tau\in(0,1)$, which makes the domain fixed and the integrand $C^1$ in $h$ with an integrable majorant.

(3) $G'=h'\ell+h\ell'-S'=h\ell'$ by (2). Also $G(0^+)=0$, and $h,\ell'>0$. ∎

### 3.3 Action and energy (Theorem A(2))

**Proposition 3.5.** $\mathfrak A(k_\pm)=\mp6\pi^2G(m)$, and in the normalization of [34], $\Delta\mathcal A(\nu)=2\ell^2G$ with $\nu=\ell^2-\pi^2$. Consequently every nonconstant isotropic trajectory has energy $E=6\pi^2L^{-2}\Delta\mathcal A=12\pi^2G$, and the same holds in $\mathcal C_{V_4}$.

*Proof.* *Finiteness and value on $k_+$.* By Lemma 3.1(3), the integrand of $\int H\,dy$ is the constant $-h$, and $pq'=h-\frac23p^3$ is bounded. Also $\int qp'=[qp]-\int pq'$ with $[qp]=0$, so $\frac12\int(pq'-qp')=\int pq'\,dy=\int p\,dq=S$. Hence $\mathfrak A(k_+)=6\pi^2(S-h\ell)=-6\pi^2G$.

*Value on $k_-$.* By [34, (F2)], $k_-$ is the image of $k_+$ under $(p,q)\mapsto(-p,q)$. This map reverses the sign of $pq'-qp'$ and of $H$. So $\mathfrak A(k_-)=-\mathfrak A(k_+)$.

*Identification with $\Delta\mathcal A$.* By [34, Thm. A(2)], $\Delta\mathcal A$ is $C^1$ on $(0,\infty)$, tends to $0$ as $\nu\to0^+$, and satisfies $\Delta\mathcal A'=2P_1$ with $P_1=\int_0^Lp_+\,dy$.

Put $F(\nu)=2\ell^2G$, where $m=m(\nu)$ is defined by $\ell(m)^2=\pi^2+\nu$. This is $C^1$ by Lemma 3.4(1) and the inverse function theorem. By Lemma 3.4(3), $dF/d\ell=4\ell G+2\ell^2h$, and $d\nu/d\ell=2\ell$, so $dF/d\nu=2G+\ell h$.

On the other hand, integrating Lemma 3.1(3) over $(0,L)$ gives two identities, since $[pq]_0^L=0$:
$$\int p\,dy=\tfrac{h\ell}2+\tfrac23\int p^3\,dy,\qquad S=h\ell-\tfrac23\int p^3\,dy .$$
So $2P_1=h\ell+2(h\ell-S)=h\ell+2G=dF/d\nu$. Since $F(0^+)=0=\Delta\mathcal A(0^+)$, we get $F=\Delta\mathcal A$.

*Energy.* By [34, Thm. A(3)], every nonconstant trajectory runs from $k_+$ to $k_-$ with $E=6\pi^2r^3L^{-2}\Delta\mathcal A$. With $r=1$ this is $12\pi^2G=\mathfrak A(k_-)-\mathfrak A(k_+)$. By [35, Thm. B], every $V_4$ trajectory is isotropic, with the same configuration and hence the same energy. verify.py S3 checks $dF/d\nu=2P_1$ and the two integral identities independently, by quadrature along the orbit. ∎

### 3.4 Hamilton–Jacobi and the fold expansion (Theorem A(3)–(4))

*Proof of A(3).* With $\ell=L/r$, $E=12\pi^2rG(m(\ell))$. So $dE/dL=12\pi^2\,dG/d\ell=12\pi^2h(m)$ by Lemma 3.4(3). The function $h\circ m$ is increasing, from $h(0)=0$ to $h(1)=\frac23$. ∎

*Proof of A(4).* By Lemma 3.4(1), $G=h\ell-S$ is odd and analytic in $m$, and $\nu=\ell^2-\pi^2$ is even, with $\nu=\frac{5\pi^2}8m^2(1+O(m^2))$. So $m^2$ is an analytic function of $\nu$ near $0$, and $m=\nu^{1/2}\psi(\nu)$ with $\psi$ analytic and $\psi(0)=\frac{2\sqrt{10}}{5\pi}$. Hence $E=12\pi^2rG=r\nu^{3/2}\Phi(\nu)$ with $\Phi$ analytic.

The coefficients follow by expanding the $\theta$-integrands in $m$ and integrating trigonometric polynomials exactly (verify.py S4):
$$\ell=\pi+\tfrac{5\pi}{16}m^2+\tfrac{515\pi}{3072}m^4+\dots,\qquad G=\tfrac{5\pi}{24}m^3+\tfrac{71\pi}{768}m^5+\dots .$$
Inverting gives the stated series. The leading coefficient $\frac{4\sqrt{10}}{15}=\frac23\sqrt{8/5}$ is that of [34, Thm. A(2)]. ∎

### 3.5 Long intervals (Theorem A(5))

**Lemma 3.6.** Put $S_*=\lim_{m\to1}S(m)$ and $\delta=1-m$. Then:
1. $S_*=2\int_0^1(1-p)\sqrt{\frac{p+2}{3p}}\,dp=\sqrt3\log(2+\sqrt3)$;
2. $\mathcal R(m):=G-\frac23\ell+S_*=\int_m^1\big(\frac23-h(t)\big)\ell'(t)\,dt>0$;
3. $\ell=\log(12/\delta)+O(\delta\log\frac1\delta)$ and $\mathcal R=\frac12\delta^2\big(1+O(\delta\log^2\frac1\delta)\big)$.

*Proof.* (1) At $m=1$ the integrand of $S$ is bounded, and dominated convergence gives $S_*$ as the $m=1$ integral. In the $p$-form this is the stated integral, because $p^3/3-p+\frac23=\frac13(p-1)^2(p+2)$. Its value is computed exactly (verify.py S5); both $\operatorname{arsinh}(1/\sqrt2)$ and $\operatorname{arcosh}(\sqrt6/2)$ equal $\log\frac{1+\sqrt3}{\sqrt2}$.

(2) By Lemma 3.4(3), $\frac{d}{dm}\big(G-\frac23\ell\big)=(h-\frac23)\ell'$. As $m\to1$, $G-\frac23\ell=(h-\frac23)\ell-S\to-S_*$. Indeed $\frac23-h=\frac13(1-m)^2(m+2)$ and, by (3), $\ell=O(\log\frac1\delta)$. Integrate from $m$ to $1$. The integrand is positive.

(3) As $m\to1$: $k'^2=1-k^2=\frac43\delta+O(\delta^2)$, and the prefactor $2\sqrt6/\sqrt{6-3m^2+mR}=2+O(\delta)$ (verify.py S5). With $K(k)=\log(4/k')+O(k'^2\log\frac1{k'})$ [17, 19.12.1] we get $\ell=2\log(4/k')+O(\delta\log\frac1\delta)=\log\frac{12}\delta+O(\delta\log\frac1\delta)$.

For $\mathcal R$, integrate (2) by parts:
$$\mathcal R(m)=-\big(\tfrac23-h(m)\big)\ell(m)+\int_m^1(1-t^2)\,\ell(t)\,dt .$$
The boundary term at $1$ vanishes. Insert the asymptotics of $\ell$ and put $v=1-t$:
$$\int_0^\delta v(2-v)\log\tfrac{12}v\,dv=\delta^2\log\tfrac{12}\delta+\tfrac{\delta^2}2+O(\delta^3\log\tfrac1\delta),\qquad\big(\tfrac23-h\big)\ell=\delta^2\log\tfrac{12}\delta+O(\delta^3\log^2\tfrac1\delta).$$
Subtracting gives the claim. ∎

*Proof of A(5).* $E=12\pi^2rG=12\pi^2r\big(\frac23\ell-S_*+\mathcal R\big)=8\pi^2L-12\sqrt3\pi^2r\log(2+\sqrt3)+12\pi^2r\mathcal R$. The inequality is $\mathcal R>0$. By Lemma 3.6(3), $\delta=12e^{-\ell}(1+O(\ell e^{-\ell}))$, so $12\pi^2r\mathcal R=6\pi^2r\delta^2(1+o(1))=864\pi^2re^{-2L/r}(1+O(\ell e^{-\ell}))$. verify.py S5 confirms $\ell+\log\delta\to\log12$ and $\mathcal R/\delta^2\to\frac12$ numerically, at $\delta=10^{-3},10^{-5},10^{-7}$. ∎

*Interpretation.* For large $L$ the static solution consists of two Nahm-pole layers joined by a long plateau near the vacuum $u=1$ (for $k_+$) or $u=-1$ (for $k_-$) of the superpotential $W=u^3/3-u$. The instanton moves the plateau from one vacuum to the other, at cost $6\pi^2|W(1)-W(-1)|=8\pi^2$ per unit length. The exponent $2$ in $e^{-2L/r}$ is the decay rate of the linearization $\delta u'=-2i\,\overline{\delta u}$ at the vacuum.

### 3.6 Rigorous enclosures (Theorem A(6))

The integrands of $\ell$ and $S$ are monotone in $\theta$: the first is increasing and the second decreasing, by the monotonicity of $\gamma$. So lower and upper Riemann sums, evaluated in interval arithmetic, enclose $\ell$ and $S$.

Sharper enclosures come from two further facts. First, $K(k)=\pi/(2\,\mathrm{AGM}(1,k'))$, and the AGM iterates bracket the limit, $b_n\le\mathrm{AGM}\le a_n$. Second, $G=\int_0^mh\,d\ell$ (Lemma 3.4(3)) with $h$ and $\ell$ increasing, so Riemann–Stieltjes sums with interval values of $\ell$ bracket $G$. verify.py S6 carries this out with mpmath's interval type (outward rounding) and checks that the two independent enclosures of $G$ overlap.

**Table 3.1** ($r=1$; rigorous enclosures, rounded outward).

| $m$ | $L$ | $G=h\ell-S$ | $E=12\pi^2G$ |
|---|---|---|---|
| $0.25$ | $3.20509799932120$ | $[0.0105176,\,0.0105280]$ | $[1.24566,\,1.24688]$ |
| $0.5$ | $3.42661954771325$ | $[0.0927571,\,0.0928397]$ | $[10.9857,\,10.9955]$ |
| $0.75$ | $3.96975738209250$ | $[0.392548,\,0.392830]$ | $[46.4915,\,46.5249]$ |
| $0.9$ | $4.81703582001331$ | $[0.934852,\,0.935341]$ | $[110.719,\,110.778]$ |

The enclosures of $L$ have width below $10^{-25}$. High-precision quadrature gives $E=1.2462704$, $10.990603$, $46.508244$ and $110.74838$.

## 4. Persistence of the complete isotropic and $SU(2)\times SU(2)$ categories (proof of Theorem B)

**Lemma 4.1 (calibrated filtrations).** Let $\mathcal C$ be a flow category whose object graph (an edge for each nonempty $\mathcal M(x,y)$) is connected. Then an energy-calibrated filtration, if it exists, is unique up to an additive constant. For $\mathcal C_{\rm iso}$ and $\mathcal C_2$ it exists: it is $f=\mathfrak A$, respectively $f(k_{ab})=\mathfrak A(k_a)+\mathfrak A(k_b)$.

*Proof.* Uniqueness is clear on a connected graph. For $\mathcal C_{\rm iso}$, $E(\mathfrak u)=\mathfrak A(k_-)-\mathfrak A(k_+)$ by Proposition 3.5. For $\mathcal C_2$, trajectories are pairs [35, Thm. D(2)], and energy is additive over the two factors. ∎

So $f(k_\pm)=\mp E/2$ for $\mathcal C_{\rm iso}$, and $f(k_{++})=-E$, $f(k_{+-})=f(k_{-+})=0$, $f(k_{--})=E$ for $\mathcal C_2$.

*Proof of B(1).*

*$\mathcal C_{\rm iso}$.* The stage $\mathcal C_{\ge t}$ is empty for $t>E/2$ and $\{k_-\}$ for $-E/2<t\le E/2$. For $t\le-E/2$ it is everything, and its realization $\Sigma^{-N}(S^N\cup_{\pm1}e^{N+1})$ is contractible [34, Cor. E]. The class $[k_-]\in\pi_0X(E/2)=\mathbb Z$ maps to $0$ in $X(-E/2)\simeq0$. By Lemma 2.7 it defines $I_{(-E/2,E/2]}S^0\to X$, which is a pointwise homology isomorphism.

*$\mathcal C_2$.* The stages are:
* $\{k_{--}\}$ for $0<t\le E$, which is $S^0$;
* $\{k_{+-},k_{-+},k_{--}\}$ for $-E<t\le0$, which is $S^0\cup e^1\cup e^1$ with both attaching degrees $\pm1$;
* everything for $t\le-E$, which is contractible [35, Thm. D(4)].

The middle stage has $H_*=\mathbb Z[1]$ (verify.py S7). It is a finite CW spectrum whose homology vanishes below degree $1$. By Hurewicz it is $0$-connected, and a map $S^1\to X(0)$ representing a generator of $\pi_1=H_1$ is an equivalence.

Take $[k_{--}]\in\pi_0X(E)$; its image in $\pi_0X(0)=0$ vanishes. Take a generator of $\pi_1X(0)$; its image in $X(-E)\simeq0$ vanishes. Lemma 2.7 gives the decomposition. The associated graded pieces are cells attached by the counts $\pm1$ of [35, Thm. D(4)]. None of this depends on the framing: the stages other than the last contain no one-dimensional moduli space, so their realizations are determined by the signed counts, and the last stage is contractible for every coherent framing [35, Thm. D(4)]. ∎

*Proof of B(2).* The realizations are contractible by [34, Cor. E] and [35, Thm. D(4)]. The isolated invariant sets are an attractor–repeller pair joined by one orbit, respectively a product of two such pairs, so their Conley indices are trivial [34, Rem. 8.1], [20]. The distances follow from Lemma 2.5 and the barcodes: $\{(-E/2,E/2]_0\}$ for $\mathcal C_{\rm iso}$ and $\{(0,E]_0,(-E,0]_1\}$ for $\mathcal C_2$ (verify.py S9). For instance $d_I(\Phi(\mathcal C_{\rm iso}),\Phi(\mathcal C_2))\ge E/2$ because of the unmatched degree-one bar, and $\le E/2$ because both are $E/2$-interleaved with $0$ (compose with zero maps). An increasing reparametrization of $\mathbb R$ preserves the number of bars in each degree, which is $0$, $1$ and $2$ respectively. ∎

*Proof of B(3).* By Lemma 2.5, $d_I$ is the bottleneck distance of single bars. For $\mathcal C_{\rm iso}$ this is $\frac12|E-E'|$. For $\mathcal C_2$ it is $\min(|E-E'|,\frac12\max(E,E'))$: either the degree-$0$ bars $(0,E]$ and $(0,E']$ are matched, which costs $|E-E'|$, or both are left unmatched (verify.py S9). The Lipschitz bound is Theorem A(3): $|E(L)-E(L')|\le12\pi^2\max h\,|L-L'|$. ∎

*Proof of B(4).* For $L<\pi r$ the isotropic and $V_4$ sectors have no KW solutions [34, Thm. A(1)], [35, Thm. B(1)]. So $\Phi=0$, and $d_I(\Phi(L),0)=E(L)/2$ by B(2). Then apply Theorem A(4). ∎

*Remark 4.2 (triaxial metrics).* For the complete categories of [37, Thms. E–F], the energy of the non-isotropic arrow is $E_c=L^{-2}(\mathcal F(k_-)-\mathcal F(k_+))>0$ in the normalization of [37, Lemma 2.3]. The proofs above apply verbatim with $E$ replaced by $E_c$.

*Remark 4.3 (boundary depth).* The longest finite bar of a filtered realization is an invariant, analogous to Usher's boundary depth [13]. Theorem B says that the boundary depth of the complete isotropic and $SU(2)\times SU(2)$ HW categories is exactly the AH instanton energy $E(L)$. Theorem A gives it in closed form for all $L$ in the window. If, as expected, the category stays two-object for all $L$ (cf. [34, Rem. 8.3]), Theorem A(5) gives linear growth with slope $8\pi^2$.

*Remark 4.4 ($SU(2)^N$).* For $G=SU(2)^N$ with principal pole and $V_4$ factors, the local category is expected to be the cube flow category [38, Rem. 2.2]. In that case the calibrated filtration is $f(k_v)=\frac E2(N-2|v|_+)$. The stage of the objects with at most $j$ plus signs has homology free of rank $\binom{N-1}{j}$, concentrated in degree $j$, so it is a wedge of $S^j$'s. The filtered type is then $\bigoplus_j\binom{N-1}j\,I_{(\frac E2(N-2j-2),\frac E2(N-2j)]}S^j$. Every bar has length $E$. We do not claim this, since the identification of the sector with the cube category is not proved in the literature.

## 5. The quadrupole sector (proof of Theorem C)

### 5.1 The data

By [31, Thm. C(3)–(4)] and [32, Thm. 1], the topological flow category $\Sigma_Q$ has the following data:
* objects $P_a^\pm$ in gradings $a+1$;
* one point in each $\mathcal M(P_a^s,P_{a-1}^t)$, with signs given in the basis $(P_a^+,P_a^-)$ by
$$d_2=d_4=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad d_3=\begin{pmatrix}1&1\\1&1\end{pmatrix};$$
* one closed interval in each $\mathcal M(P_a^s,P_{a-2}^t)$, whose ends are the two broken trajectories through $P_{a-1}^\pm$;
* one square in each $\mathcal M(P_3^s,P_0^t)$.

The morphism spaces are nonempty exactly for $a>b$. Hence every action filtration satisfies $f(P_a^s)<f(P_b^{s'})$ for $a>b$; for a $J$-symmetric one this means $\varphi_0>\varphi_1>\varphi_2>\varphi_3$. The stage $\Sigma_{Q,\ge t}$ for $\varphi_{a+1}<t\le\varphi_a$ is the full subcategory $R_a$ on $P_0^\pm,\dots,P_a^\pm$.

A coherent framing determines, by truncation, a framed 1-flow category in the sense of Lobb–Orson–Schütz [5, Defs. 3.1–3.3]. It consists of the point signs and interval frame values $\lambda_{st}$ (on $\mathcal M(P_2^s,P_0^t)$) and $\rho_{st}$ (on $\mathcal M(P_3^s,P_1^t)$), subject to:
* Def. 3.1, each broken pair is an end of exactly one interval;
* Def. 3.2, the endpoint signs of each interval sum to $1$;
* Def. 3.3, one affine condition mod $2$ for each pair at grading distance $3$, coming from the boundary of the corresponding two-dimensional moduli space.

The truncation of a framed flow category satisfies all three [5, §3]. For a framed flow category, the LOS cochain operation $\mathrm{sq}$ [5, Def. 3.12] computes the topological $\mathrm{Sq}^2$ of the realization [5, Thm. 3.13, Rem. 3.14].

### 5.2 Frame parity (Theorem C(1))

**Proposition 5.1.** The four conditions of [5, Def. 3.3] for $\Sigma_Q$ are
$$\lambda_{+t}+\lambda_{-t}+\rho_{s+}+\rho_{s-}\equiv0\qquad(s,t\in\{+,-\}).$$
Hence $\sum \lambda_{st}\equiv\sum \rho_{st}\equiv0$. Exactly $32$ of the $256$ assignments satisfy them, and their restrictions to the $\lambda$'s are exactly the $8$ even patterns.

*Proof.* Fix $(a,d)=(P_3^s,P_0^t)$. The boundary of $\overline{\mathcal M}(a,d)$ is glued from four pieces. There are two pieces $Q\times J$, with $Q\in\mathcal M(P_3^s,P_2^u)$ and $J=\mathcal M(P_2^u,P_0^t)$ for $u=\pm$. There are two pieces $I\times P$, with $I=\mathcal M(P_3^s,P_1^v)$ and $P\in\mathcal M(P_1^v,P_0^t)$ for $v=\pm$. They close up into a single cycle (the square). Def. 3.3 reads $1+\tilde\lambda\equiv0$, where
$$\tilde\lambda=\lambda_{+t}+\lambda_{-t}+\textstyle\sum_v\big(1+s(\mathcal M(P_1^v,P_0^t))+\rho_{sv}\big).$$
The two signs $s(\mathcal M(P_1^\pm,P_0^t))$ differ by $d_2$, so $\sum_v(1+s)=1$, and the condition is as stated. Adding the conditions for $(s,+)$ and $(s,-)$ gives $\sum_{u,t}\lambda_{ut}\equiv0$. Adding those for $(+,t)$ and $(-,t)$ gives $\sum\rho\equiv0$. The count is an enumeration (verify.py S8). That enumeration reproduces the number $32$ of [38, §7.3]. ∎

### 5.3 Rigid windows (Theorem C(2))

**Lemma 5.2.** Let $W$ be the window $\{P_0,P_1,P_2\}$ (resp. $\{P_1,P_2,P_3\}$) with any framing of its own, i.e. any frame values $\lambda_{st}$ (resp. $\rho_{st}$) satisfying [5, Defs. 3.1–3.2]. Then $H_*(|W|;\mathbb Z)=\mathbb Z[1]\oplus\mathbb Z[3]$ (resp. $\mathbb Z[2]\oplus\mathbb Z[4]$), and
$$|W|\simeq\begin{cases}S^1\vee S^3\ (\text{resp. }S^2\vee S^4)&\text{if }\sum\lambda\ (\text{resp. }\sum\rho)\text{ is even},\\ S^1\cup_\eta e^3\ (\text{resp. }S^2\cup_\eta e^4)&\text{if it is odd.}\end{cases}$$

*Proof.* The homology is a Smith-form computation (verify.py S7). By minimal cell structures [16, Prop. 4C.1], applied after suspension, $|W|$ is a two-cell complex $S^1\cup_\alpha e^3$ with $\alpha\in\pi_1^s=\{0,\eta\}$. Moreover $\alpha=\eta$ iff $\mathrm{Sq}^2:H^1(|W|;\mathbb F_2)\to H^3$ is nonzero [21, 22].

We compute $\mathrm{Sq}^2$ with [5, Def. 3.12]. The group $H^1(W;\mathbb F_2)$ is generated by the cocycle $\psi=P_0^{+*}+P_0^{-*}$. For each $a=P_2^s$ the LOS graph $\Gamma(a,\psi)$ has four vertices $(P_1^v,P_0^t)$. It has two interval edges, $\mathcal M(P_2^s,P_0^t)$ for $t=\pm$, joining $(P_1^+,P_0^t)$ to $(P_1^-,P_0^t)$. It has two matching edges, joining $(P_1^v,P_0^+)$ to $(P_1^v,P_0^-)$. So it is one $4$-cycle $C_s$, and
$$\mathrm{sq}^\psi(P_2^s)=1+F(C_s)+D(C_s),\qquad F(C_s)=\lambda_{s+}+\lambda_{s-}.$$
The matching edges, and hence $D(C_s)$, do not depend on $s$. Now $H^3(W;\mathbb F_2)=\mathbb F_2$, since $\delta P_1^{v*}=P_2^{+*}+P_2^{-*}$. The class of a cochain is the sum of its two coordinates. Therefore
$$[\mathrm{Sq}^2\psi]=\textstyle\sum_s\big(1+F(C_s)+D(C_s)\big)=\sum_{s,t}\lambda_{st}\pmod2 .$$
The contributions $1+D$ cancel in pairs, so the result does not depend on the orientation conventions for matching edges (verify.py S8 checks both conventions and all $16$ patterns). The window $\{P_1,P_2,P_3\}$ is identical after shifting all indices by one; there the matching edges are directed, but again they contribute equally for $a=P_3^\pm$. ∎

*Proof of C(2).* The window $W_{[\varphi_2,\varphi_0]}$ is the subcomplex $R_2$, and $W_{[\varphi_3,\varphi_1]}$ is the quotient $|\Sigma_Q|/R_0$. Both are realizations of full subcategories carrying the restricted framing [4, §3]. By Proposition 5.1 their parities are even, so Lemma 5.2 gives wedges.

Windows with two consecutive levels have cells in two adjacent dimensions. Their homology is free (verify.py S7). By [38, Lemma 2.1] (Smith normal form for two-level complexes) they are wedges of two spheres. Windows with one level are wedges $S^{a+1}\vee S^{a+1}$. The full window is $X_0$ or $X_1$ by [39, Thm. A].

Lemma 5.2 with odd parity gives the standalone framings realizing $S^1\cup_\eta e^3$. Such a window has no grading-distance-three pairs, so its framed 1-flow data are a framed flow category. By Proposition 5.1, these framings do not extend. ∎

*Remark 5.3.* Conceptually, framings of the window $\{P_0,P_1,P_2\}$, the Morse category of a great $S^2\subset S^3$, have an obstruction class in $H^2(S^2;\pi_1^s)=\mathbb Z/2$. Framings of $\Sigma_Q$ have theirs in $H^2(S^3;\pi_1^s)=0$ [39], and the restriction $H^2(S^3)\to H^2(S^2)$ vanishes. Proposition 5.1 is the exact, combinatorial form of this vanishing. It shows that the $\eta^2$ of [39] is the *only* nontrivial attaching phenomenon in the whole filtration.

### 5.4 The two filtered types (Theorem C(3)–(4))

*Proof of C(3).* Write $X=\Phi_f(\Sigma_Q)$. By §5.3, $X(t)=R_a$ for $t\in(\varphi_{a+1},\varphi_a]$, with
$$R_0\simeq S^1\vee S^1,\qquad R_1\simeq S^1\vee S^2,\qquad R_2\simeq S^1\vee S^3,\qquad R_3\in\{X_0,X_1\}.$$
Let $\iota_\pm\in\pi_1R_0$ be the classes of the cells $P_0^\pm$. We choose maps from the summands into $X$ (Lemma 2.7).

* $F_{\varphi_0}S^1\to X$: the class $\iota_+$.
* $I_{(\varphi_1,\varphi_0]}S^1\to X$: the class $\iota_+-\iota_-$. In $R_1$ the cells $P_1^\pm$ are attached along $\pm(\iota_+-\iota_-)$ by $d_2$. Since $\pi_1=H_1$ for these $0$-connected spectra, the class dies in $R_1$.
* $I_{(\varphi_2,\varphi_1]}S^2\to X$: we need $\beta_2\in\pi_2R_1$ with Hurewicz image a generator of $H_2(R_1)$ and with image $0$ in $\pi_2R_2$. We have $\pi_2R_2=\pi_1^s\cdot\iota$, where $\iota$ is the common image of $\iota_\pm$. If a Hurewicz lift $\beta$ maps to $\eta\iota$, replace it by $\beta-\eta\iota$. This has the same Hurewicz image, since $\eta$ has Hurewicz image $0$.
* $I_{(\varphi_3,\varphi_2]}S^3\to X$: similarly, with $\pi_3R_3=\pi_2^s\iota=\mathbb Z/2$ for $X_0$ (correct by $\eta^2\iota$), and $\pi_3R_3=0$ for $X_1$ (verify.py S10).
* For $X_0$, $F_{\varphi_3}S^4\to X$: a class in $\pi_4R_3$ mapping to a generator of $H_4$. This exists because $S^4$ is a wedge summand.
* For $X_1$, $J_{\varphi_3,\varphi_0}\to X$: by the cofibre property, this is a map $F_{\varphi_0}S^1\to X$ (take $\iota_+$) together with a null-homotopy of the composite $F_{\varphi_3}S^3\to X$. That composite is the class $\eta^2\iota\in\pi_3R_3=\pi_3X_1=0$, so a null-homotopy exists. Changing it by $x\in\pi_4X_1$ changes the induced degree on the top cell by the Hurewicz image of $x$, which lies in $2\mathbb Z$ (verify.py S10). Compatibility with $\eta^2$ forces the degree to be odd. So we can choose it to be $1$.

At every $t$ the sum of these maps is an isomorphism on $H_*(-;\mathbb Z)$, by inspection of the stagewise homology (verify.py S7). Lemma 2.7 gives $X\simeq Y_0$ or $X\simeq Y_1$. ∎

*Proof of C(4).* $Y_0(t)\not\simeq Y_1(t)$ for $t\le\varphi_3$, by $KO_3$ [39, Thm. B]. The stagewise homology and the structure maps on homology are those of the same cellular complex, so the persistence modules $H_*(-;A)$ agree. In $Y_1$ the class $\eta^2\iota\ne0$ in $\pi_3Y_1(t)$ for $t>\varphi_3$. Indeed $\pi_3(S^1\vee S^k)\supset\pi_2^s\iota$ for $k\ge2$, and $\pi_3(S^1\vee S^1)\supset\pi_2^s\iota_+$. But $\pi_3Y_1(t)=0$ for $t\le\varphi_3$. In $Y_0$ the class survives, because $\pi_3X_0=\pi_2^s$. ∎

### 5.5 Comparison with the height category (Remark 1.2)

The category $\Sigma_H$ has objects $P_1$, of grading $1$, and $P_4$, of grading $4$, with $\mathcal M(P_4,P_1)\cong S^2$ framed null in $\pi_2^s$ for the model framing [31, Thm. C′], [32, Thm. 1(4), Thm. 3(4)]. So $g(P_4)<g(P_1)$. The stages are $S^1$ for $g(P_4)<t\le g(P_1)$ and $S^1\vee S^4$ below, which gives $\Phi_g(\Sigma_H)\simeq F_{g(P_1)}S^1\oplus F_{g(P_4)}S^4$.

*Proof of Remark 1.2.* Both realizations are $\Sigma^\infty h(\bar B)=X_0$ [32, Thm. 1(4)]. For model framings $\Phi_f(\Sigma_Q)\simeq Y_0$. Lemma 2.5 gives the distance as the bottleneck distance of the barcodes, which is the stated maximum (verify.py S9). It is positive because $\varphi_0>\varphi_1$. No reparametrization helps: $Y_0$ has a stage with $H_1$ of rank $2$, and every stage of $\Phi_g(\Sigma_H)$ has $H_1$ of rank at most $1$ (verify.py S7). ∎

*Remark 5.4 (non-symmetric filtrations).* If $f(P_a^+)\ne f(P_a^-)$, there are up to eight critical values. The same arguments give a decomposition with the same bars, split at the intermediate levels. For instance, between $f(P_1^+)$ and $f(P_1^-)$ the stage is $S^1$. We omit the bookkeeping.

## 6. Energies and spectral invariants (proof of Theorem D)

### 6.1 Below the fold

*Proof of D(1).* In $\Sigma_Q$ the class $\iota_1$ is carried by the cells $P_0^\pm$, which form the top stage: $c(\iota_1)=\varphi_0=\max f$. The class $\iota_4$ appears only when the cells $P_3^\pm$ enter, so $c(\iota_4)=\varphi_3=\min f$. In $\Sigma_H$, $c(\iota_1)=g(P_1)$ and $c(\iota_4)=g(P_4)<g(P_1)$. The same holds for every coherent framing, since $H_*$ does not depend on it, and for non-symmetric $f$ with $\max f$ and $\min f$ in place of $\varphi_0$ and $\varphi_3$. ∎

### 6.2 Leading-order energies in the quadrupole sector

We use the setting of [31] in normalized units (radius $1$, interval $(0,\pi)$). The phase space is $X=L^2(S^3\times(0,\pi);\mathbb R^{24})$, the centre coordinates are $\xi_c=-\frac x\pi\zeta+\frac{\sqrt2}\pi V_w$ with $\|V_{e_a}\|^2=\frac98\pi^3$, the time is $t=s/\pi$, and the KW sphere has radius $|w|^2=\Sigma(\bar\nu)=\frac{32}{15}|\bar\nu|(1+O(|\bar\nu|))$. The *$X$-energy* of a solution of the perturbed gauge-fixed system is $E_X(u)=\int\|\partial_s\xi\|_X^2\,ds$.

**Lemma 6.1 (uniform length).** Let $Y_0$ be a Morse–Smale gradient vector field on a closed manifold $M$. There are a $C^1$-neighbourhood $\mathcal V$ of $Y_0$ and $\Lambda<\infty$ such that every trajectory of every $Y\in\mathcal V$ connecting two zeros has length at most $\Lambda$.

*Proof (sketch; standard).* Take Morse charts in which $Y_0$ is linear and hyperbolic. For the round Rayleigh field this is provided by the model metric of [32, Thm. 1(1)]. For $Y$ that is $C^1$-close, the cones $\{|x_u|\ge|x_s|\}$ and $\{|x_s|\ge|x_u|\}$ in a box of size $\rho$ are respectively forward-invariant and backward-invariant. In them $|x_u|$ grows, respectively $|x_s|$ decays, at rate at least $\frac12$. So the length spent in each box is at most $C\rho$.

Outside the boxes $|Y|\le C$, and a Lyapunov function of $Y_0$ decreases along $Y$ at rate at least $c>0$ [19, Ch. 4], [26]. So the time outside the boxes, and the number of visits to boxes, are bounded uniformly. ∎

**Proposition 6.2.** Fix $\bar\nu\in(-\delta,0)$. Every $u\in\mathcal M(P_a^s,P_b^{s'})$ of $\Sigma_Q(\bar\nu,\varepsilon)$ satisfies
$$E_X(u)=\tfrac\pi{18}\,\varepsilon|\bar\nu|(c_a-c_b)\big(1+O(|\bar\nu|^{1/2})\big)+O_{\bar\nu}(\varepsilon^2).$$
Here $O(|\bar\nu|^{1/2})$ is uniform in $\varepsilon$, and $O_{\bar\nu}$ may depend on $\bar\nu$.

*Proof.* By [31, Thm. C(2)] the trajectory lies on the centre manifold, and its reduced curve $z(t)=(x(t),w(t))$ lies on the invariant sphere $\mathcal S_{\bar\nu,\varepsilon}$. Write $\xi=\mathrm{const}+\xi_c(z)+\tilde\Psi(\xi_c)$. Then $\partial_s\xi=(1+D\tilde\Psi)\partial_s\xi_c$ with $\|D\tilde\Psi\|=O(|z|+|\bar\nu|+\varepsilon)=O(|\bar\nu|^{1/2})+O(\varepsilon)$ [31, Lemma 2.1], [30].

Since $\zeta\perp\mathcal K$, $\int\|\partial_s\xi_c\|^2ds=\int\big(\pi^{-3}\|\zeta\|^2\dot x^2+\frac94|\dot w|^2\big)dt$ (verify.py S11). The sphere $\mathcal S_{\bar\nu,\varepsilon}$ is a $C^1$ graph over the round sphere $\{x=0,|w|^2=\Sigma\}$ with $C^1$-distance $O_{\bar\nu}(\varepsilon)$ [31, Lemma 4.2]. So, writing $w=\Sigma^{1/2}\theta+O_{\bar\nu}(\varepsilon)$, we get $|\dot w|^2=\Sigma|\dot\theta|^2(1+O_{\bar\nu}(\varepsilon))$ and $\dot x^2=O_{\bar\nu}(\varepsilon^2)|\dot\theta|^2$.

By [31, Cor. 4.3], $\dot\theta=-\varepsilon\nabla \mathcal G_C(\theta)+\eta$ with $\mathcal G_C=\frac{|\kappa|}2\chi_C$, $\kappa=-\frac{5\pi}{216}$, and $\|\eta\|_{C^1}\le\varepsilon\,O(|\bar\nu|^{1/2})+O_{\bar\nu}(\varepsilon^2)$. Hence
$$\int|\dot\theta|^2dt=-\varepsilon\int\langle\nabla \mathcal G_C,\dot\theta\rangle dt+\int\langle\eta,\dot\theta\rangle dt=\varepsilon\big(\mathcal G_C(\theta_-)-\mathcal G_C(\theta_+)\big)+O\big(\|\eta\|_\infty\Lambda\big).$$
Here $\theta_\pm$ are the end points of the trajectory, and $\Lambda$ is the length bound of Lemma 6.1 for the rescaled fields $\varepsilon^{-1}Y_\varepsilon$, which are $C^1$-close to $-\nabla \mathcal G_C$. The end points are zeros of $Y_\varepsilon$, at distance $O(|\bar\nu|^{1/2})+O(\varepsilon)$ from $e_a,e_b$. Since these are critical points of $\mathcal G_C$, $\mathcal G_C(\theta_-)-\mathcal G_C(\theta_+)=\frac{|\kappa|}2(c_a-c_b)+O(|\bar\nu|)+O(\varepsilon^2)$.

Collecting terms, $E_X(u)=\frac94\Sigma\,\varepsilon\frac{|\kappa|}2(c_a-c_b)(1+O(|\bar\nu|^{1/2}))+O_{\bar\nu}(\varepsilon^2)$, and $\frac94\cdot\frac{32}{15}\cdot\frac{5\pi}{216}\cdot\frac12=\frac\pi{18}$ (verify.py S11). ∎

The formula is additive under breaking and positive, as an energy must be. verify.py S11 also checks the model identity $\int|\dot\theta|^2dt=\frac12(c_a-c_b)$ for the exact Rayleigh quarter circles, and S12 illustrates numerically that a non-gradient perturbation changes the energy only at first order.

**Definition 6.3.** A family of $J$-symmetric action filtrations $f=f_{\bar\nu,\varepsilon}$ of $\Sigma_Q$ is *calibrated to leading order* if $f(y)-f(x)-E_X(u)=\varepsilon\,O(|\bar\nu|^{3/2})+O_{\bar\nu}(\varepsilon^2)$ for all $u\in\mathcal M(x,y)$.

By Proposition 6.2, $f(P_a^\pm)=-\frac\pi{18}\varepsilon|\bar\nu|c_a$ is one such filtration. Any HW action functional $\mathfrak A_\varepsilon$ whose gradient flow is the perturbed gauge-fixed system, with $E_X(u)=\mathfrak A_\varepsilon(y)-\mathfrak A_\varepsilon(x)$, gives another. Such a functional is $J$-invariant because $h_C$ is $J$-invariant [31, Thm. B]. Its existence in the full theory needs the renormalization discussed in [30, Rem. 6.3], and we do not claim it.

*Proof of D(2).* Apply Proposition 6.2 to a trajectory in $\mathcal M(P_3^\pm,P_0^\pm)$, which is nonempty, and use D(1). ∎

### 6.3 Above the fold

For $\bar\nu>0$ and $\varepsilon=0$, the full gauge-fixed system has the two objects $k_\pm$ and the obstructed AH arrow $\mathfrak u$. This is a genuine HW trajectory in the isotropic class, with HW energy $E(L)$ given by Theorem A. On isotropic configurations ($a_s=a_y=0$), the integrated $\|\partial_s\xi\|_X^2$ is a positive multiple $c_0=c_0(L)$ of the HW energy density $\int|\partial_sA|^2+|\partial_s\varphi|^2$; the constant comes only from the rescaling to normalized units and from the normalization of the $T$-basis, and depends continuously on $L$. So $E_X(\mathfrak u)=c_0E(L)$. The perturbation $h_{\beta,e}$ breaks the arrow, and $\Sigma_E(\varepsilon)$ has objects $k_\pm(\varepsilon)\to k_\pm$ and no morphisms [32, Thm. 3(3)]. The grading of $k_+$ is $1$ and that of $k_-$ is $4$: the AH arrow has index $\mu(k_+)-\mu(k_-)=-3$ [29], [31, §1.2].

**Definition 6.4.** A family $f_\varepsilon$ of filtrations of $\Sigma_E(\varepsilon)$ is *calibrated by continuity* if $f_\varepsilon(k_-(\varepsilon))-f_\varepsilon(k_+(\varepsilon))\to E_X(\mathfrak u)=c_0E(L)$ as $\varepsilon\to0$.

Every filtration is admissible for $\Sigma_E$, because there are no morphisms. Calibration is what makes the filtration reflect the HW action. A continuous action functional $\mathfrak A_\varepsilon=\mathfrak A-\varepsilon h_{\beta,e}$ with the energy identity would be calibrated by continuity, since $\mathfrak A(k_-)-\mathfrak A(k_+)=E_X(\mathfrak u)$.

*Proof of D(3).* $\Phi_{f_\varepsilon}(\Sigma_E)\simeq F_{f(k_+)}S^1\oplus F_{f(k_-)}S^4$, because there are no morphisms. So $c(\iota_1)=f(k_+)$ and $c(\iota_4)=f(k_-)$, and $\gamma=-(f(k_-)-f(k_+))\to-c_0E(L)$. ∎

*Proof of D(4).* Combine D(1), D(3) and Theorem A(4): $\gamma>0$ for $\bar\nu<0$, and $\gamma\to-c_0E(L)=-c_0r\frac{8\sqrt{10}}5\nu^{3/2}(1+O(\nu))<0$ for $\bar\nu=\nu>0$. The realizations are $X_0$ on both sides [32, Thm. 3(6)]. ∎

*Remark 6.5.* The sign change is a filtered shadow of the fold. Below the fold the critical set is a sphere, whose bottom class ($\iota_1$) lies at higher action than its fundamental class ($\iota_4$), as for any Morse function. Above the fold the two cells come from the AH pair, and the arrow $k_+\to k_-$ puts the grading-$1$ object at *lower* action. Unfiltered invariants cannot see this. The interleaving distance between a below-fold and an above-fold filtered type is at least $\frac12(\gamma_{\rm below}-\gamma_{\rm above})$: the infinite bars in degrees $1$ and $4$ must be matched, and $|a-a'|+|b-b'|\ge|(a-b)-(a'-b')|$.

## 7. Further remarks

*$\mathrm{Sol}^4$.* In the $\mathbb R^3\rtimes V_4$ sector of $\mathrm{Sol}^4$ every object has action $0$ [36, Thm. (D)]. So every energy-calibrated filtration is constant, and the filtered type is $F_0$ applied to the realization. Nothing is gained there.

*Dependence on normalization.* An additive constant in $f$ shifts $\Phi_f$. Interleaving distances between categories depend on the normalizations. We used the canonical one given by the finite static action $\mathfrak A$. The bar *lengths*, the boundary depth and $\gamma$ do not depend on it.

*Relation to the literature.* Barcodes and spectral invariants of filtered Floer complexes are due to Usher, Zhang, Polterovich–Shelukhin and others [13, 14, 23, 24, 25]. Spectral invariants go back to Viterbo, Schwarz and Oh [24, 25]. The spectrum-level framework is [1]. Within the published rStation series, filtered homotopy types of HW categories have not been computed before, nor have the closed form of the AH action gap, the long-interval law, or the window rigidity of Theorem C(2). The closed form of Theorem A is a quadrature of a one-degree-of-freedom Hamiltonian system; what is new is its explicit evaluation for the AH static problem.

## 8. Status of the claims

**Proved here (full proofs).** Theorem A (§3); Theorem B (§4), using the recalled contractibility [34, Cor. E], [35, Thm. D(4)], [39, Thm. A(1)]; Theorem C and Remark 1.2 (§5), with C(1) a direct consequence of the conditions of [38, §7.3]; Theorem D(1), D(3), D(4) (§6); Lemmas 2.2–2.7, 3.1–3.6, 4.1, 5.2; Propositions 3.3, 3.5, 5.1.

**Proved with a standard step only sketched.** Proposition 6.2, which uses the uniform length Lemma 6.1, and hence D(2).

**Conditional on definitions, not on hypotheses.** D(2) and D(3) concern calibrated filtrations (Definitions 6.3, 6.4). The existence of a renormalized HW action in the full theory, which would supply them, is not claimed.

**Imported.** As listed in §1.4. In particular the HW categories themselves [27–39], their realizations and reframings [32, 39], and the LOS calculus [5].

**Numerical only.** verify.py S3 (quadrature cross-checks), S5 (asymptotic checks), S12, S13 (last item). They are not used in the proofs.

**Verifier.** verify.py runs 129 checks and ends with FALLOS = 0, in about 20 s. By tag: 7 encode known facts or bookkeeping [K], 75 are exact computations [C], 20 are rigorous interval enclosures [I], and 27 are numerical illustrations [N]. verify.mpl mirrors the exact parts in Maple (47 checks). It was executed in Maple: 47 checks, FALLOS = 0; the output is in verify_mpl_output.txt.

## References

[1] A. Hedenlund, T. P. Oldervoll, *Structured flow categories and twisted presheaves*, arXiv:2603.29576.

[2] M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.

[3] R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.

[4] R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.

[5] A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500; arXiv:1710.01857.

[6] L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.

[7] M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.

[8] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.

[9] A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207.

[10] F. Chazal, V. de Silva, M. Glisse, S. Oudot, *The Structure and Stability of Persistence Modules*, SpringerBriefs in Mathematics, Springer, 2016.

[11] M. Lesnick, *The theory of the interleaving distance on multidimensional persistence modules*, Found. Comput. Math. 15 (2015), 613–650.

[12] U. Bauer, M. Lesnick, *Induced matchings and the algebraic stability of persistence barcodes*, J. Comput. Geom. 6 (2015), 162–191.

[13] M. Usher, *Boundary depth in Floer theory and its applications to Hamiltonian dynamics and coisotropic submanifolds*, Israel J. Math. 184 (2011), 1–57.

[14] L. Polterovich, E. Shelukhin, *Autonomous Hamiltonian flows, Hofer's geometry and persistence modules*, Selecta Math. 22 (2016), 227–296.

[15] J. Lurie, *Higher Topos Theory*, Ann. of Math. Stud. 170, Princeton Univ. Press, 2009.

[16] A. Hatcher, *Algebraic Topology*, Cambridge Univ. Press, 2002, §4.C.

[17] NIST Digital Library of Mathematical Functions, §19.12 (asymptotic approximations of complete elliptic integrals), https://dlmf.nist.gov/19.12.

[18] P. F. Byrd, M. D. Friedman, *Handbook of Elliptic Integrals for Engineers and Scientists*, 2nd ed., Springer, 1971.

[19] J. Palis, W. de Melo, *Geometric Theory of Dynamical Systems*, Springer, 1982.

[20] C. Conley, *Isolated Invariant Sets and the Morse Index*, CBMS 38, AMS, 1978.

[21] H. Toda, *Composition Methods in Homotopy Groups of Spheres*, Ann. of Math. Stud. 49, Princeton Univ. Press, 1962.

[22] R. E. Mosher, M. C. Tangora, *Cohomology Operations and Applications in Homotopy Theory*, Harper & Row, 1968.

[23] M. Usher, J. Zhang, *Persistent homology and Floer–Novikov theory*, Geom. Topol. 20 (2016), 3333–3430.

[24] M. Schwarz, *On the action spectrum for closed symplectically aspherical manifolds*, Pacific J. Math. 193 (2000), 419–461.

[25] Y.-G. Oh, *Construction of spectral invariants of Hamiltonian paths on closed symplectic manifolds*, in: The Breadth of Symplectic and Poisson Geometry, Progr. Math. 232, Birkhäuser, 2005, 525–570.

[26] K. R. Meyer, *Energy functions for Morse–Smale systems*, Amer. J. Math. 90 (1968), 1031–1040.

[27] rStation math_24, https://rstation.ai/problems/math/papers/24/v2

[28] rStation math_25, https://rstation.ai/problems/math/papers/25/v1

[29] rStation math_30, https://rstation.ai/problems/math/papers/30/v1

[30] rStation math_31, https://rstation.ai/problems/math/papers/31/v1

[31] rStation math_32, https://rstation.ai/problems/math/papers/32/v1

[32] rStation math_33, https://rstation.ai/problems/math/papers/33/v1

[33] rStation math_34, https://rstation.ai/problems/math/papers/34/v1

[34] rStation math_46, https://rstation.ai/problems/math/papers/46/v1

[35] rStation math_49, https://rstation.ai/problems/math/papers/49/v1

[36] rStation math_50, https://rstation.ai/problems/math/papers/50/v1

[37] rStation math_51, https://rstation.ai/problems/math/papers/51/v1

[38] rStation math_52, https://rstation.ai/problems/math/papers/52/v1

[39] rStation math_53, https://rstation.ai/problems/math/papers/53/v1

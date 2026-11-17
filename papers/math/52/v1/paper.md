# Decoupled framed flow categories and Steenrod squares beyond homology: a three-level classification, reframings of products, and applications to Haydys–Witten theory

**Abstract.**

The Haydys–Witten (HW) flow categories constructed so far near the Anderson–Henningson fold all realize wedges of spheres. That alone excludes the Khovanov spectrum of $T(3,4)$, by torsion. So an obstruction to $\mathrm{Sq}^2$ phrased through these sectors says nothing beyond integral cohomology. We study instead the class $\mathcal W_2$ realized by disjoint unions of products of two-level framed flow categories, the output of decoupled sectors, with torsion allowed. We also study the larger class $\mathcal W$ generated under wedges, suspensions, smash products and retracts by all finite spectra with $\mathrm{Sq}^i=0$ for $i\ge2$. Every finite spectrum has the integral cohomology of a member of $\mathcal W_2$, so integral cohomology never decides membership.

(A) On a product, $\mathrm{Sq}^k$ acts by the $k$-th elementary symmetric function of the factor Bocksteins. Hence on $\mathcal W$: $Q_1=0$; $\mathrm{Sq}^2\neq0$ on an $N$-fold product iff at least two factors have $\mathrm{Sq}^1\neq0$; and two conditions (W1), (W2) relate $\mathrm{Sq}^2$ to $\mathrm{Sq}^1$-cycles and boundaries.

(B) For spectra with cells in three consecutive dimensions, using Chang's classification: $X\in\mathcal W$ iff $X\in\mathcal W_2$ iff (W1) and (W2) hold iff $X$ is a wedge of spheres, Moore spectra and suspensions of $M(\mathbb Z/2)\wedge M(\mathbb Z/2)$. This is computable from rigid moduli and Lobb–Orson–Schütz data.

(C) Reframing one interval of $M(\mathbb Z/4)\times M(\mathbb Z/4)$ moves the realization from $M(\mathbb Z/4)\vee\Sigma M(\mathbb Z/4)\in\mathcal W$ to a Chang complex $\notin\mathcal W$ with the same cohomology.

(D) $\mathcal X^{11}_{\rm Kh}(T(3,4))\notin\mathcal W$; the only other spectrum with its integral cohomology is in $\mathcal W_2$. Conditionally, an HW category realizing it is not a product-framed decoupled category. Of the two adiabatic trefoil candidates of rStation math_36, exactly one is in $\mathcal W$.

verify.py: 80 exact checks, including the grading-distance-3 framing condition of Lobb–Orson–Schütz (Def. 3.3); FALLOS = 0.

## 1. Introduction

### 1.1 The question

Witten [11] proposed that Khovanov homology is the Floer homology of the HW equations [12]. Lipshitz and Sarkar [2] refined Khovanov homology to a spectrum $\mathcal X_{\rm Kh}(K)=\bigvee_q\mathcal X^q_{\rm Kh}(K)$, the Cohen–Jones–Segal (CJS) realization [5] of a framed flow category. One may ask whether $\mathcal X_{\rm Kh}$ is the CJS realization of a framed flow category of HW trajectories. The first invariant beyond homology is $\mathrm{Sq}^2$, which is nonzero on $\mathrm{Kh}(T(3,4))$ [3].

All HW flow categories constructed rigorously so far live near the Anderson–Henningson fold [13] on $\mathbb R\times S^3\times(0,L)$ with Nahm poles [14]–[23]. Their realizations are contractible or $\Sigma^\infty(S^1\vee S^4)$ (§2.3). In particular they are wedges of spheres, and so is everything generated from them by wedges, suspensions and smash products. That class has torsion-free integral cohomology. The known $\mathbb Z/2$ in $\mathrm{Kh}^{3,11}(T(3,4);\mathbb Z)$ therefore excludes it before $\mathrm{Sq}^2$ is consulted. This observation is due to the referee of the first version, and we withdraw the corresponding "no symmetric assembly" statement.

The productive question is about a class that torsion does *not* exclude. The HW sectors with product gauge group decouple [15, §7.2]: the equations, the moduli spaces and the linearized operators split factor by factor. A decoupled category is a product of its factor categories, and in every sector constructed so far each factor has objects in two consecutive gradings. Two-level categories realize all wedges of spheres and Moore spectra, torsion included (Lemma 2.1). We therefore ask:

> *Which spectra are realized by disjoint unions of products of two-level framed flow categories? Can a Steenrod square detect non-membership when integral cohomology cannot?*

### 1.2 Results

Let $\mathcal G$ be the class of finite spectra $Z$ with $\mathrm{Sq}^i=0$ on $H^*(Z;\mathbb F_2)$ for all $i\ge2$. Let $\mathcal W$ be the smallest class containing $\mathcal G$ and closed under finite wedges, (de)suspensions, smash products and retracts. Let $\mathcal W_2\subset\mathcal W$ be the smallest class containing all spheres and Moore spectra $M(\mathbb Z/k)$ and closed under finite wedges, (de)suspensions and smash products. By Lemma 2.1, $\mathcal W_2$ is the class of realizations of disjoint unions of products of two-level framed flow categories, given the product formula (P) of §2.1.

* **Theorem A (Steenrod structure of $\mathcal W$).** On $Z_1\wedge\dots\wedge Z_N$ with $Z_i\in\mathcal G$, $\mathrm{Sq}^k=e_k(a_1,\dots,a_N)$, where $a_i$ is $\mathrm{Sq}^1$ on the $i$-th factor. Consequently, on every $Y\in\mathcal W$:
  * $Q_1=0$ and $\mathrm{Sq}^2\mathrm{Sq}^2=0$;
  * $\mathrm{Sq}^2\neq0$ on an $N$-fold product (factors with nonzero mod-2 cohomology) iff at least two factors have $\mathrm{Sq}^1\neq0$;
  * **(W1)** if $\mathrm{Sq}^1x=0$, then $\mathrm{Sq}^2x\in\mathrm{Sq}^2\mathrm{Sq}^1H^{*-1}$;
  * **(W2)** if $\mathrm{Sq}^3x=0$, then $\mathrm{Sq}^2x\in\mathrm{Sq}^1H^{*+1}$.
* **Theorem B (separation at fixed homology).** Every finite spectrum has the integral cohomology of a wedge of spheres and Moore spectra, which lies in $\mathcal W_2$. If $\mathrm{Sq}^2$ maps the reduction of an integral class outside $\mathrm{Sq}^2\mathrm{Sq}^1H^{*-1}$, or hits the reduction of an integral class that is not the reduction of a class of order $\le2$, then $X\notin\mathcal W$.
* **Theorem C (three-level classification).** Let $X$ be a finite spectrum with cells in dimensions $n,n+1,n+2$. Then the following are equivalent:
  * $X\in\mathcal W$;
  * $X\in\mathcal W_2$;
  * $X$ is a wedge of spheres, Moore spectra and copies of $\Sigma^nM(\mathbb Z/2)\wedge M(\mathbb Z/2)$;
  * $\mathrm{Sq}^2$ kills $\ker(\mathrm{Sq}^1|H^n)$ and $\mathrm{Sq}^2H^n\subset\mathrm{Sq}^1H^{n+1}$.
  
  For a framed flow category whose realization has this form, membership is decided by the rigid moduli spaces and the LOS data (Corollary 5.3).
* **Proposition D (reframings of products).** Changing interval frame values by $\varepsilon$ changes the LOS square by an explicit cochain map $E_\varepsilon$. On $M(\mathbb Z/4)\times M(\mathbb Z/4)$, the product framing realizes $M(\mathbb Z/4)\vee\Sigma M(\mathbb Z/4)\in\mathcal W$. One reframed interval realizes the Chang complex $C^{2}_{2}\notin\mathcal W$, with the same integral cohomology.
* **Corollary E ($T(3,4)$).** $\mathcal X^{11}_{\rm Kh}(T(3,4))$ is one of exactly two spectra with its integral cohomology. It is not in $\mathcal W$; the other, $\Sigma^2M(\mathbb Z/2)\vee S^4$, is in $\mathcal W_2$. Conditionally on Hypotheses (K1)–(K4) of §7.1, an HW flow category realizing it is not a disjoint union of product-framed products of two-level categories, whatever torsion the factors carry.
* **Corollary F (adiabatic trefoil).** The two $SO(3)$-equivariant candidates of [24, Thm. D] have the same integral cohomology. Exactly one, the one with $\varepsilon=0$, lies in $\mathcal W$.

### 1.3 What is new and what is not

* *Not new.* We use the following without claiming novelty:
  * the LOS formula and its properties [1];
  * the Khovanov computations for $T(3,4)$ [3], which we only recompute;
  * the Cartan formula, Milnor's primitives and Margolis-type arguments [8, 9];
  * Chang's classification [6];
  * the minimal cell structures [7, Prop. 4C.1];
  * all HW input [14]–[25].
  
  The realizations in §2.3 are those of the cited papers. The identification of the $SU(2)^N$ sector with the cube flow category is a routine extension of [15, Thm. C] and [2] (Remark 2.2), and we claim nothing for it.
* *New, to our knowledge, and elementary.* All of the following are elementary:
  * the description of $\mathcal W$ in Theorem A, including the $N$-factor law and (W1)–(W2);
  * the separation principle of Theorem B;
  * the three-level classification of Theorem C, with its flow-category form;
  * the reframing phenomenon of Proposition D;
  * the applications E and F.
  
  We found no statement of (W1)–(W2) or of Theorem C in the literature (§8). Decompositions of smash products of Moore and Chang complexes are studied in [10], and for $M(\mathbb Z/2^r)\wedge M(\mathbb Z/2^s)$ they are classical. We use none of them beyond Chang's list.
* *Not claimed.* We prove no new analytic statement about HW moduli spaces. Every HW statement about knots is conditional. Corollary F adds no information to [24, 25]: it rephrases their dichotomy through $\mathcal W$.

## 2. Conventions and background

### 2.1 Framed flow categories and the LOS operation

A framed flow category is as in [2]. It has graded objects; compact $\langle k\rangle$-manifolds $\overline{\mathcal M}(x,y)$ of dimension $|x|-|y|-1$ whose faces are compositions; and coherent framings. Its CJS realization $|\mathcal C|$ is a finite CW spectrum with one cell of dimension $|x|$ for each object, and its cellular cochain complex is the Morse complex, $\delta x^*=\sum_y\#\mathcal M(y,x)\,y^*$ [2]. A *framed 1-flow category* [1, Defs. 3.1–3.3] keeps the moduli spaces of dimension $0$ and $1$. It records the signs $s(P)\in\mathbb Z/2$ of the points and the frame values $f\in\mathbb Z/2$ of the one-dimensional components, subject to three conditions.
* **Boundary (Def. 3.1).** Each broken pair is an end of exactly one interval.
* **Sign (Def. 3.2).** The four endpoint signs of each interval sum to $1$.
* **Compatibility (Def. 3.3).** Let $|a|=|d|+3$. The boundary of $\overline{\mathcal M}(a,d)$ is glued from pieces $Q\times J$ (a point $Q\in\mathcal M(a,b)$ times an interval $J\subset\mathcal M(b,d)$) and $I\times P$ (an interval $I\subset\mathcal M(a,c)$ times a point $P\in\mathcal M(c,d)$). Then $\sum_C\big(1+\tilde f(C)\big)=0$, where $C$ runs over the cycles so formed and
$$\tilde f(C)=\sum_{Q\times J\subset C}f(J)+\sum_{I\times P\subset C}\big(1+s(P)+f(I)\big).$$
  This is the form we implement (verify.py, `compat_conditions`). As a check of the implementation, the Lipshitz–Sarkar frame assignment of the $q=11$ Khovanov category of $T(3,4)$ satisfies all $2944$ such conditions, and flipping one frame value violates some of them (§9).

*The LOS operation* [1, Def. 3.12]. Let $\varphi$ be a mod-2 cocycle of degree $m$ and $|a|=m+2$. Form the graph $\Gamma_C(a,\varphi)$:
* its vertices are the pairs $(B,A)$ with $A\in\mathcal M(a,b)$, $B\in\mathcal M(b,c)$ and $c\in\varphi$;
* its edges are the intervals of $\mathcal M(a,c)$, $c\in\varphi$, together with the edges of a chosen boundary matching of $\bigsqcup_{c\in\varphi}\mathcal M(b,c)$; a matching edge is directed when its two signs agree.

Then
$$\mathrm{sq}^\varphi(a)=|L|+\sum_C\big(1+F(C)+D(C)\big).$$
Here $L$ is the set of nontrivially framed circles, $F(C)$ is the sum of the frame values in the component $C$, and $D(C)$ is its number of forward-directed edges. By [1, Thm. 3.13] this defines $\mathrm{Sq}^2:H^m\to H^{m+2}$ independently of the choices. By [1, Rem. 3.14] it is the topological $\mathrm{Sq}^2$ of $|\mathcal C|$ when the 1-flow category is the truncation of a framed flow category. $\mathrm{Sq}^1$ is the integral Bockstein of the Morse complex.

**Fact (P) (products).** Let $\mathcal C_1,\mathcal C_2$ be framed flow categories. With the product framing, the product category has realization $|\mathcal C_1|\wedge|\mathcal C_2|$, up to a shift. For Khovanov categories of split links this is [2] and [4]. We use (P) only to identify realizations of products with smash products. The finite checks of §9 verify its cohomological shadow (the Cartan formula) on all product categories used.

### 2.2 Two-level categories

**Lemma 2.1.** Let $X$ be a finite CW spectrum with cells in dimensions $n$ and $n+1$ only, and let $\delta$ be its cellular coboundary. Then
$$X\simeq\bigvee S^n\vee\bigvee S^{n+1}\vee\bigvee_i\Sigma^nM(\mathbb Z/k_i),$$
where the $k_i>1$ are the invariant factors of $\delta$. Moreover $\mathrm{Sq}^i=0$ for $i\ge2$, and $\mathrm{Sq}^1\neq0$ iff some $k_i\equiv2\bmod4$. In particular $X\in\mathcal G\cap\mathcal W_2$.

*Proof.* $X$ is the cofibre of a map of wedges of $n$-spheres. Its matrix is $\delta^T$, because $\pi_n^s(S^n)=\mathbb Z$. Automorphisms of wedges realize all elementary row and column operations, so the Smith normal form gives the splitting. $\mathrm{Sq}^i$ for $i\ge2$ vanishes for degree reasons. $\mathrm{Sq}^1$ is the Bockstein, which is nonzero on $M(\mathbb Z/k)$ iff $k\equiv2\bmod4$. ∎

So the realizations of disjoint unions of products of two-level framed flow categories, with product framings, are exactly the members of $\mathcal W_2$, by (P). Any number of factors and any incidences are allowed.

### 2.3 The Haydys–Witten sectors (imported; background only)

We state each input with its exact scope. Write $\nu=(L/r)^2-\pi^2$.

| sector | source | scope | realization |
|---|---|---|---|
| isotropic, local | [14, Thms. C–D] | $0<\nu<\nu_2$, in a neighbourhood $\mathcal U$ | $*$ (two objects, one arrow) |
| isotropic, complete | [21, Thm. D, Cor. E] | $\pi r<L<\pi r+\delta$ | $*$ |
| Klein $V_4$, triaxial, local | [15, Thm. B] | $Lc$ near $(2\pi,2\pi,2\pi)$, $0<\Delta<\delta$ | $*$ |
| $SU(2)\times SU(2)$, local | [15, Thm. C] | as above | $*$ |
| $SU(2)\times SU(2)$, complete | [22, Thm. D], [23, Thm. F] | near the fold | $*$ |
| complete gauge-fixed, below the fold, quadrupole $h_C$ | [18, Thm. C], [19, Thm. 1], [20, Thm. D(1)] | $\bar\nu\in(-\delta,0)$, $0<\varepsilon<\varepsilon_0$; transported framing [19, Rem. 4.4] | $\Sigma^\infty(S^1\vee S^4)$ |
| height / $h_{\beta,e}$ | [18, Thm. C′], [19, Thms. 1, 3] | as in the sources | $\Sigma^\infty(S^1\vee S^4)$ |
| Conley index near the fold | [18, Thm. E1], [20, Thm. D(2)] | all settings near the fold | $\Sigma^\infty(S^1\vee S^4)$ |

*Scope of the complete isotropic category [21].* For every $L>\pi r$, [21, Thm. C] proves compactness of the trajectory spaces. Global uniqueness of the tunnelling instanton, and hence the complete category with one transversal arrow, is proved only for $\pi r<L<\pi r+\delta$ [21, Thm. D]. Existence, uniqueness and transversality for $L\ge\pi r+\delta$ are left open there [21, Rem. 8.3]. Accordingly, the contractibility of the complete isotropic realization is asserted only for $\pi r<L<\pi r+\delta$ (the first version of this paper misstated this).

*What we use.*
* Every realization in the table is contractible or $S^1\vee S^4$, hence a wedge of spheres. The proofs are in the sources; for the quadrupole and height sectors the identification uses the transported framings of [19].
* The product sectors decouple [15, §7.2]: objects, trajectories and linearized operators split factor by factor.

Nothing in Theorems A–D depends on the table. It motivates the class $\mathcal W_2$ and is used in §7.3.

*Remark 2.2 (the $SU(2)^N$ sector).* For $G=SU(2)^N$ with principal pole and $V_4$ factors, decoupling identifies the local category with the cube flow category of [2]. Its Morse complex is $(\mathbb Z\xrightarrow{\pm1}\mathbb Z)^{\otimes N}$, which is acyclic, so every framing has contractible realization (verify.py §7, $N\le5$). For $N=2$ this is [15, Thm. C]. The extension to all $N$ involves no new analysis, and we claim no novelty for it.

## 3. The class $\mathcal W$: Theorem A

For $Z\in\mathcal G$, $H^*(Z;\mathbb F_2)$ is a module over $E[a]=\mathbb F_2[a]/(a^2)$, with $a=\mathrm{Sq}^1$. Every finite-dimensional $E[a]$-module is a direct sum of copies of $\mathbb F_2$ (with $a=0$) and of $E[a]$.

**Theorem A.**
1. *(Symmetric functions.)* Let $Y=Z_1\wedge\dots\wedge Z_N$ with $Z_i\in\mathcal G$. Under the Künneth isomorphism $H^*(Y;\mathbb F_2)\cong\bigotimes_iH^*(Z_i;\mathbb F_2)$, let $a_i$ act as $\mathrm{Sq}^1$ on the $i$-th factor. Then $\mathrm{Sq}^k=e_k(a_1,\dots,a_N)$ for all $k\ge0$, where $e_k$ is the $k$-th elementary symmetric polynomial.
2. *(Primitives.)* For every $Y\in\mathcal W$, the Milnor primitives $Q_m$, $m\ge1$, act trivially on $H^*(Y;\mathbb F_2)$, and $\mathrm{Sq}^2\mathrm{Sq}^2=0$.
3. *($N$-factor law.)* In (1), assume $H^*(Z_i;\mathbb F_2)\neq0$ for every $i$. Then $\mathrm{Sq}^2\neq0$ on $H^*(Y;\mathbb F_2)$ iff at least two factors have $\mathrm{Sq}^1\neq0$. For realizations of two-level categories: iff at least two of the coboundary matrices have an invariant factor $\equiv2\bmod4$.
4. *(W1), (W2).* For every $Y\in\mathcal W$ and $x\in H^*(Y;\mathbb F_2)$:
   * (W1) if $\mathrm{Sq}^1x=0$, there is $y$ with $\mathrm{Sq}^2(x+\mathrm{Sq}^1y)=0$; equivalently $\mathrm{Sq}^2x\in\mathrm{Sq}^2\mathrm{Sq}^1H^{*-1}(Y;\mathbb F_2)$;
   * (W2) if $\mathrm{Sq}^3x=0$, then $\mathrm{Sq}^2x\in\mathrm{Sq}^1H^{*+1}(Y;\mathbb F_2)$.
5. *(Integral form.)* Let $\rho$ be reduction mod $2$.
   * If $x=\rho(z)$ for an integral class $z$, then $\mathrm{Sq}^2x\in\mathrm{Sq}^2\mathrm{Sq}^1H^{*-1}(Y;\mathbb F_2)$.
   * If $\mathrm{Sq}^2x=\rho(z)$ for an integral class $z$, then $\mathrm{Sq}^2x=\rho(t)$ for some $t$ with $2t=0$.

*Proof.*
1. By the Cartan formula, $\mathrm{Sq}^k(x_1\otimes\dots\otimes x_N)=\sum_{k_1+\dots+k_N=k}\mathrm{Sq}^{k_1}x_1\otimes\dots\otimes\mathrm{Sq}^{k_N}x_N$. On each factor only $\mathrm{Sq}^0=1$ and $\mathrm{Sq}^1=a_i$ survive. So the sum runs over the $k$-element subsets $S$ of $\{1,\dots,N\}$ and equals $\prod_{i\in S}a_i=e_k(a)$.
2. For the generators, $Q_1=\mathrm{Sq}^3+\mathrm{Sq}^2\mathrm{Sq}^1=0$, and inductively $Q_{m+1}=[\mathrm{Sq}^{2^{m+1}},Q_m]=0$. The $Q_m$ are primitive [8], so they act as derivations on external products. They also preserve wedge decompositions and retracts. Hence $Q_m=0$ on $\mathcal W$. For products, $\mathrm{Sq}^2\mathrm{Sq}^2=e_2^2=0$, since $a_i^2=0$ and every cross term appears twice. This passes to wedges and retracts.
3. If at most one $a_i$ is nonzero, then $e_2=\sum_{i<j}a_ia_j=0$. Suppose $a_i\neq0\neq a_j$ with $i\neq j$. Choose $x_i$ with $a_ix_i\neq0$ and $x_j$ with $a_jx_j\neq0$. For $k\neq i,j$ choose $x_k\neq0$ with $a_kx_k=0$, for instance a class of top degree. Then $e_2(x_1\otimes\dots\otimes x_N)=\cdots\otimes a_ix_i\otimes\cdots\otimes a_jx_j\otimes\cdots\neq0$, since every other term contains some $a_kx_k=0$. The last sentence follows from Lemma 2.1.
4. Both conditions are linear, and they pass to $\mathcal A$-module direct summands. For (W1): if $y$ works for $x$ in $M=N\oplus N'$, its projection to $N$ works for the component of $x$ in $N$. They also pass to direct sums and suspensions, so it suffices to treat a product $Y=Z_1\wedge\dots\wedge Z_N$. Write $H^*(Z_i)=T_i\oplus F_i$, with $T_i$ trivial and $F_i$ free over $E[a_i]$. Then
$$H^*(Y)=\bigoplus_{U\subset\{1..N\}}H_U,\qquad H_U=\bigotimes_{i\in U}F_i\otimes\bigotimes_{i\notin U}T_i .$$
   Each $H_U$ is stable under every $a_i$, hence under every $\mathrm{Sq}^k=e_k(a)$, and it is free over $\Lambda_U=\mathbb F_2[a_i:i\in U]/(a_i^2)$. On $H_U$, $\mathrm{Sq}^k=e_k(a_U)$.
   * For $U=\emptyset$ all $\mathrm{Sq}^k$, $k\ge1$, vanish.
   * For $U\neq\emptyset$, the substitution $b_1=e_1(a_U)$, $b_i=a_i$ ($i\in U$ not the first) is an algebra automorphism of $\Lambda_U$: $b_1^2=0$ in characteristic $2$, and $a_{\rm first}$ is recovered from the $b$'s. So $\Lambda_U$, and with it $H_U$, is free over $E[\mathrm{Sq}^1]$, and $\ker\mathrm{Sq}^1=\operatorname{im}\mathrm{Sq}^1$ on $H_U$.
   
   Write $x=\sum_Ux_U$; the operations act componentwise.
   * (W1): if $\mathrm{Sq}^1x=0$ then each $x_U$ with $U\neq\emptyset$ equals $e_1y_U$. With $y=\sum y_U$ we get $x+\mathrm{Sq}^1y=x_\emptyset$, and $\mathrm{Sq}^2x_\emptyset=0$.
   * (W2): $\mathrm{Sq}^3=\mathrm{Sq}^1\mathrm{Sq}^2$ (Adem). If $e_1e_2x_U=0$ for all $U$, then $e_2x_U\in\ker e_1=\operatorname{im}e_1$ for $U\neq\emptyset$, and $e_2x_\emptyset=0$.
5. $\mathrm{Sq}^1\rho=0$, so the first statement is (W1). In the second, $\mathrm{Sq}^3x=\mathrm{Sq}^1\rho(z)=0$. So (W2) gives $\mathrm{Sq}^2x=\mathrm{Sq}^1y=\rho(\beta y)$, where $\beta$ is the integral Bockstein, and $2\beta y=0$. ∎

*Remark 3.1 (the two-factor statement of the first version, corrected).* The first version stated: "a smash product of two-level realizations with one $\mathrm{Sq}^1$-trivial factor has $\mathrm{Sq}^2=0$." This is correct for exactly two factors and false in general. For example, $M(\mathbb Z/2)\wedge M(\mathbb Z/2)\wedge(S^0\vee S^1)$ and $M(\mathbb Z/2)\wedge M(\mathbb Z/2)\wedge M(\mathbb Z/4)$ have $\mathrm{Sq}^2\neq0$, although their third factor has $\mathrm{Sq}^1=0$. Theorem A(3) is the correct statement for any number of factors. verify.py §3 checks it on both examples and on $119$ random products. It also checks the Adem relations $\mathrm{Sq}^1\mathrm{Sq}^1=0$, $\mathrm{Sq}^1\mathrm{Sq}^2=\mathrm{Sq}^3$, $\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^3\mathrm{Sq}^1$ and $\mathrm{Sq}^1\mathrm{Sq}^3=0$ on the Cartan modules.

*Remark 3.2 (what $\mathcal W$ contains).* $\mathcal G$ contains spectra with no primary operations at all, such as $S^0\cup_{\eta^2}e^3$ and $S^0\cup_{2\nu}e^4$. So $\mathcal W$ is strictly larger than $\mathcal W_2$, and (W1)–(W2), being primary, cannot separate the two in general. They coincide on three-level spectra (Theorem C). Theorems A and B are obstructions to membership in the larger class $\mathcal W$, hence also in $\mathcal W_2$.

## 4. Separation at fixed homology: Theorem B

**Theorem B.**
1. For every finite spectrum $X$ there is a wedge $M_X$ of spheres and Moore spectra with $H^*(M_X;\mathbb Z)\cong H^*(X;\mathbb Z)$ as graded groups, and $M_X\in\mathcal W_2$. Hence no invariant of integral cohomology alone can show $X\notin\mathcal W_2$.
2. Suppose some $x\in H^m(X;\mathbb F_2)$ satisfies either of the following:
   * (a) $x=\rho(z)$ and $\mathrm{Sq}^2x\notin\mathrm{Sq}^2\mathrm{Sq}^1H^{m-1}(X;\mathbb F_2)$;
   * (b) $\mathrm{Sq}^2x=\rho(z)$ and $\mathrm{Sq}^2x\notin\rho\big(H^{m+2}(X;\mathbb Z)[2]\big)$, where $[2]$ denotes the elements killed by $2$.
   
   Then $X\notin\mathcal W$.
3. The following pairs have isomorphic integral cohomology; in each pair the first spectrum is in $\mathcal W_2$ and the second is not in $\mathcal W$:
   * $S^0\vee S^2$ and $\Sigma^{-2}\mathbb{CP}^2$;
   * $\Sigma^2M(\mathbb Z/2)\vee S^4$ and $\Sigma^{-1}\mathbb{RP}^5/\mathbb{RP}^2$;
   * $M(\mathbb Z/4)\vee\Sigma M(\mathbb Z/4)$ and the Chang complex $C^{2}_{2}$ of §5.
   
   On the other hand, $M(\mathbb Z/2)\vee\Sigma M(\mathbb Z/2)$ and $M(\mathbb Z/2)\wedge M(\mathbb Z/2)$ have isomorphic integral cohomology, differ in $\mathrm{Sq}^2$, and *both* lie in $\mathcal W_2$.

*Proof.*
1. Every finitely generated graded abelian group is realized by a wedge of spheres and Moore spectra.
2. This is Theorem A(5), contraposed.
3. The cohomology isomorphisms are direct.
   * $\Sigma^{-2}\mathbb{CP}^2$: the bottom class is a reduction, $\mathrm{Sq}^2\neq0$ on it, and $H^{-1}=0$, so (a) applies.
   * $\Sigma^{-1}\mathbb{RP}^5/\mathbb{RP}^2$: $\mathrm{Sq}^2x^3=x^5$ is the reduction of the generator of $H^5(\,\cdot\,;\mathbb Z)=\mathbb Z$, so (b) applies.
   * $C^2_2$: §5 and Proposition D.
   
   The last pair is Theorem C. ∎

*Remark 4.1.* Theorem B(2) separates candidates that torsion does not separate. In example (3)(iii) the two spectra even share their torsion $\mathbb Z/4\oplus\mathbb Z/4$ and have $\mathrm{Sq}^1=0$. Only $\mathrm{Sq}^2$ distinguishes them.

## 5. Three-level spectra: Theorem C

A finite spectrum $X$ is *three-level* (at $n$) if it has a CW structure with cells in dimensions $n,n+1,n+2$ only. By minimal cell structures [7, Prop. 4C.1], applied to a high suspension, this holds iff two conditions hold:
* $H_k(X;\mathbb Z)=0$ for $k\notin\{n,n+1,n+2\}$;
* $H_{n+2}(X;\mathbb Z)$ is free.

The realization of a framed flow category with objects in three consecutive gradings is three-level.

**Chang's theorem** [6] (stable range; see also [10, §1]). Every three-level finite spectrum is a wedge of indecomposables from the following list:
* spheres $S^n,S^{n+1},S^{n+2}$;
* Moore spectra $\Sigma^nM(\mathbb Z/p^r)$ and $\Sigma^{n+1}M(\mathbb Z/p^r)$;
* the elementary Chang complexes (indices $r,s\ge1$):
$$C_\eta=S^n\cup_\eta e^{n+2},\qquad C_r=S^n\cup_{2^r}e^{n+1}\cup_{i\eta}e^{n+2},$$
$$C^s=(S^n\vee S^{n+1})\cup_{(\eta,2^s)}e^{n+2},\qquad C^s_r=(S^n\cup_{2^r}e^{n+1}\vee S^{n+1})\cup_{(i\eta,2^s)}e^{n+2}.$$

Each Chang complex has $\mathrm{Sq}^2\neq0$ from the bottom class to the top class. Its integral cohomology and $\mathrm{Sq}^1$ are read off from the cells:

| piece | $H^*(\,\cdot\,;\mathbb Z)$ (degrees $n,n+1,n+2$) | $\mathrm{Sq}^1\neq0$ | (W1) | (W2) |
|---|---|---|---|---|
| $C_\eta$ | $\mathbb Z,0,\mathbb Z$ | never | fails | fails |
| $C_r$ | $0,\mathbb Z/2^r,\mathbb Z$ | $n\to n+1$ iff $r=1$ | holds iff $r=1$ | fails |
| $C^s$ | $\mathbb Z,0,\mathbb Z/2^s$ | $n+1\to n+2$ iff $s=1$ | fails | holds iff $s=1$ |
| $C^s_r$ | $0,\mathbb Z/2^r,\mathbb Z/2^s$ | as above | holds iff $r=1$ | holds iff $s=1$ |

**Theorem C.** For a three-level finite spectrum $X$ (at $n$), the following are equivalent:
* (a) $X\in\mathcal W$;
* (b) $X\in\mathcal W_2$;
* (c) $X$ is a wedge of spheres, Moore spectra and copies of $\Sigma^nM(\mathbb Z/2)\wedge M(\mathbb Z/2)$;
* (d) $\mathrm{Sq}^2$ vanishes on $\ker(\mathrm{Sq}^1:H^n\to H^{n+1})$, and $\mathrm{Sq}^2H^n\subset\mathrm{Sq}^1H^{n+1}$ (mod-2 cohomology).

*Proof.*
* (c)$\Rightarrow$(b)$\Rightarrow$(a) by definition.
* (a)$\Rightarrow$(d). By Theorem A(4), $X$ satisfies (W1) and (W2). For a three-level spectrum, $\mathrm{Sq}^2$ can be nonzero only on $H^n$, and $\mathrm{Sq}^2\mathrm{Sq}^1H^{n-1}=0=\mathrm{Sq}^3H^n$. So (W1) and (W2) reduce to (d).
* (d)$\Rightarrow$(c). By Chang, $X\simeq\bigvee_jX_j$ with indecomposable $X_j$. Then $H^*(X;\mathbb F_2)=\bigoplus_jH^*(X_j;\mathbb F_2)$ as modules over the Steenrod algebra, and (d) passes to summands. By the table, the only elementary Chang complex satisfying (d) is $C^1_1$; spheres and Moore spectra satisfy (d) trivially.
  * $M(\mathbb Z/2)\wedge M(\mathbb Z/2)$ is three-level at $0$, with cohomology $0,\mathbb Z/2,\mathbb Z/2$ and $\mathrm{Sq}^2\neq0$ (Theorem A(3)).
  * In Chang's list, the only wedges with this cohomology are $M(\mathbb Z/2)\vee\Sigma M(\mathbb Z/2)$, where $\mathrm{Sq}^2=0$, and $C^1_1$.
  
  Hence $C^1_1\simeq M(\mathbb Z/2)\wedge M(\mathbb Z/2)$, up to suspension. ∎

*Remark 5.1.* verify.py §3 and §5 check the table, the module isomorphism $H^*(M(\mathbb Z/2)\wedge M(\mathbb Z/2))\cong H^*(C^1_1)$, and the enumeration below (2-local pieces with $r,s\le3$). Chang's theorem itself is imported.

**Corollary 5.2 (exactly two candidates).** For each integral cohomology below there are exactly two homotopy types of three-level spectra (at $0$). They are distinguished by $\mathrm{Sq}^2$.

| $H^0,H^1,H^2$ | in $\mathcal W_2$ | not in $\mathcal W$ |
|---|---|---|
| $0,\ \mathbb Z/2,\ \mathbb Z$ | $M(\mathbb Z/2)\vee S^2$ | $C_1\simeq\Sigma^{-3}\mathbb{RP}^5/\mathbb{RP}^2$ |
| $0,\ \mathbb Z/4,\ \mathbb Z/4$ | $M(\mathbb Z/4)\vee\Sigma M(\mathbb Z/4)$ | $C^2_2$ |
| $\mathbb Z,\ 0,\ \mathbb Z$ | $S^0\vee S^2$ | $C_\eta=\Sigma^{-2}\mathbb{CP}^2$ |
| $0,\ \mathbb Z/2,\ \mathbb Z/2$ | $M(\mathbb Z/2)\vee\Sigma M(\mathbb Z/2)$ and $M(\mathbb Z/2)\wedge M(\mathbb Z/2)$ (both in $\mathcal W_2$) | — |

*Proof.* By Chang, a spectrum with the given cohomology is a wedge of listed pieces whose cohomologies add up to it. The enumeration (verify.py §5) leaves exactly the two listed wedges in each row. They differ in $\mathrm{Sq}^2$, so they are not equivalent. For the first row this is also the direct count $\pi_1^s(M(\mathbb Z/2))=\mathbb Z/2$, generated by $i\eta$. ∎

**Corollary 5.3 (flow-category form).** Let $\mathcal C$ be a framed flow category whose realization is three-level at $n$; for example, all objects lie in gradings $n,n+1,n+2$. Then $|\mathcal C|\in\mathcal W$ iff condition (d) holds, where:
* $\mathrm{Sq}^1$ is computed from the signed counts of rigid trajectories (integral Bockstein of the Morse complex);
* $\mathrm{Sq}^2$ is computed from the LOS data in grading distance $2$ [1].

In particular, for three-level categories, membership in $\mathcal W$ is a property of the framed 1-flow category.

## 6. Reframings of products: Proposition D

Let $\mathcal C$ be a framed 1-flow category and $\varepsilon$ a function from its interval components to $\mathbb Z/2$. Let $\mathcal C^\varepsilon$ be the same data with frame values $f+\varepsilon$. Define the mod-2 cochain map $E_\varepsilon:C^m\to C^{m+2}$ by
$$E_\varepsilon(c^*)=\sum_{|a|=|c|+2}\Big(\sum_{I\subset\mathcal M(a,c)}\varepsilon(I)\Big)a^*.$$

**Proposition D.**
1. If $\mathcal C$ and $\mathcal C^\varepsilon$ both satisfy [1, Defs. 3.1–3.3], then $\mathrm{Sq}^2_{\mathcal C^\varepsilon}=\mathrm{Sq}^2_{\mathcal C}+[E_\varepsilon]$ on $H^*(\,\cdot\,;\mathbb F_2)$. The integral cochain complexes of $\mathcal C$ and $\mathcal C^\varepsilon$ coincide, so their realizations have the same integral cohomology and the same $\mathrm{Sq}^1$.
2. Let $\mathcal C=\mathcal C_1\times\mathcal C_2$ be a product of two-level framed flow categories, in gradings $0,1,2$. Then Def. 3.3 is vacuous. Changing the framing of an interval by the generator of $\pi_1(O)=\mathbb Z/2$, relative to its fixed endpoint framings, gives a framed flow category with the same underlying topological category. Every $\varepsilon$ arises this way.
3. For $\mathcal C=M(\mathbb Z/4)\times M(\mathbb Z/4)$, the 2-cube cover with $4\times4$ points:
   * the product framing realizes $M(\mathbb Z/4)\vee\Sigma M(\mathbb Z/4)$, which lies in $\mathcal W_2$;
   * changing the framing of one interval realizes the Chang complex $C^{2}_{2}$, which is not in $\mathcal W$.
   
   Both have integral cohomology $0,\mathbb Z/4,\mathbb Z/4$.
4. For $\mathcal C=M(\mathbb Z/2)\times M(\mathbb Z/2)$, one reframed interval toggles $\mathrm{Sq}^2$ between $M(\mathbb Z/2)\wedge M(\mathbb Z/2)$ and $M(\mathbb Z/2)\vee\Sigma M(\mathbb Z/2)$; both lie in $\mathcal W_2$.

*Proof.*
1. Each interval $I\subset\mathcal M(a,c)$ with $c\in\varphi$ is an edge of exactly one component of $\Gamma_C(a,\varphi)$. Changing its frame value changes $F$ of that component by $\varepsilon(I)$, and nothing else changes. Hence $\mathrm{sq}^\varphi_\varepsilon=\mathrm{sq}^\varphi+E_\varepsilon\varphi$ as cochains. Both sides are well defined on cohomology by [1, Thm. 3.13], so $[E_\varepsilon]$ is too. The integral complex depends only on the signed rigid counts.
2. There are no pairs at grading distance $3$. The moduli spaces have dimension $\le1$, so the only coherence conditions concern the endpoints of the intervals. These are unchanged, and the framings of an interval rel endpoints form a $\pi_1(O)$-torsor whose two elements have different frame values [1, §3].
3. By (1), $\mathrm{Sq}^1=0$, because all incidences are $\pm4$. With the product framing, LOS gives $\mathrm{Sq}^2=0$; with one interval reframed, $\mathrm{Sq}^2\neq0$ (verify.py §6). By Corollary 5.2, row 2, the first realization is $M(\mathbb Z/4)\vee\Sigma M(\mathbb Z/4)$ and the second is $C^2_2$. The latter violates (d).
4. This is the same computation; row 4 of Corollary 5.2 applies. ∎

So membership of a decoupled category in $\mathcal W$ is a property of its framing, not of its underlying topological category. The product framing is what Fact (P) and Theorem A need. verify.py §6 also checks the formula of (1) on $36$ random reframings of $M(n_1)\times M(n_2)$.

*Remark 6.1 (decoupled HW sectors and their framings; conditional).* In a decoupled HW sector the linearized operator along a product trajectory is the direct sum $\bigoplus_i\mathcal D_i$ of the factor operators. This is [15, Thm. C] for $N=2$, and the same argument applies verbatim for any $N$. Consider the following hypothesis.
* **(Ind)** The framed structure of the HW category is induced from the index bundles of the linearized operators by a rule compatible with direct sums.

Under (Ind), a decoupled sector carries the product framing. By (P) its realization is then the smash product of the factor realizations, and it lies in $\mathcal W_2$ when the factors are two-level. Proposition D shows that this is a genuine restriction: on the same underlying topological category, non-product framings can leave $\mathcal W$. For the published sectors the question is moot, since all factors have incidence $\pm1$ and every framing gives a contractible realization [15, 22, 23]. We do not prove (Ind).

## 7. Applications

### 7.1 $T(3,4)$

**Fact 7.1** ([3]; recomputed exactly in verify.py §8). Use the Lipshitz–Sarkar conventions for the right-handed $T(3,4)$, the closure of $(\sigma_1\sigma_2)^4$.
* $\mathrm{Kh}^{h,11}(T(3,4);\mathbb Z)$ is $\mathbb Z/2$ for $h=3$, $\mathbb Z$ for $h=4$, and $0$ otherwise. All other bigradings are free of rank $\le1$.
* $\mathrm{Sq}^1:\mathrm{Kh}^{2,11}\to\mathrm{Kh}^{3,11}$ is nonzero, and $\mathrm{Sq}^1:\mathrm{Kh}^{3,11}\to\mathrm{Kh}^{4,11}$ is zero (mod 2).
* $\mathrm{Sq}^2:\mathrm{Kh}^{2,11}\to\mathrm{Kh}^{4,11}$ is nonzero, and $\mathrm{Sq}^2=0$ in every other bigrading.

The nonvanishing of $\mathrm{Sq}^2$ is due to [3]. We recompute it with a generic implementation of [1] on the Khovanov framed 1-flow category. The Lipshitz–Sarkar frames satisfy all $2944$ Def. 3.3 conditions in $q=11$, gradings $0,\dots,6$.

**Corollary E.**
1. *(Unconditional.)* $X:=\mathcal X^{11}_{\rm Kh}(T(3,4))$ is three-level at $2$. Exactly two spectra have its integral cohomology:
   * $\Sigma^2M(\mathbb Z/2)\vee S^4$, which is in $\mathcal W_2$;
   * the Chang complex $\Sigma^2C_1\simeq\Sigma^{-1}\mathbb{RP}^5/\mathbb{RP}^2$, which is not in $\mathcal W$.
   
   $X$ is the second. Hence $X\notin\mathcal W$, and $\mathcal X_{\rm Kh}(T(3,4))\notin\mathcal W$, because $\mathcal W$ is closed under retracts. This holds although $\mathrm{Kh}(T(3,4);\mathbb Z)$, torsion included, is the integral cohomology of a member of $\mathcal W_2$.
2. *(Conditional on (K1)–(K4) below, for $K=T(3,4)$.)* Consider the HW framed flow category $\mathcal C_{\rm HW}(T(3,4))$, or just its $q=11$ part. Its realization is not equivalent to the realization of any disjoint union of products of framed flow categories with objects in two consecutive gradings, carrying product framings. This holds for any number of factors and any incidences, so whatever torsion the factors carry; it uses (P). More generally its realization is not in $\mathcal W$.
3. *(Conditional, framing form.)* Assume in addition that the $q=11$ part of $\mathcal C_{\rm HW}(T(3,4))$ has the underlying topological type of a product of two two-level categories. Then its framing is not the product framing. More precisely, its interval frame values in the window $(2,11)\to(4,11)$ differ from the product values by some $\varepsilon$ with $[E_\varepsilon]\neq0$ on $H^{2+\sigma}$.

*Proof.*
1. By Fact 7.1, $H^k(X;\mathbb Z)$ is $\mathbb Z/2$ for $k=3$, $\mathbb Z$ for $k=4$, and $0$ otherwise. So $X$ is three-level at $2$, and Corollary 5.2, row 1, applies.
   * $\mathrm{Sq}^2x_2\neq0$ is the reduction of the generator of $H^4(X;\mathbb Z)=\mathbb Z$.
   * $\mathrm{Sq}^1H^3=0$.
   
   So condition (d) of Theorem C fails; equivalently Theorem B(2)(b) applies. The computed module is the Chang module $C_1$ (verify.py §8).
2. By (K4), $|\mathcal C^{11}_{\rm HW}|\simeq\Sigma^\sigma X$. Disjoint unions of products of two-level categories with product framings realize members of $\mathcal W_2$, by Lemma 2.1 and (P). Apply (1).
3. Suppose the framing were the product framing. Then by (P) the realization would be a smash product of two-level realizations, so it would lie in $\mathcal W_2$, contradicting (1). For the refinement, write the actual framing as the product framing changed by $\varepsilon$.
   * Both framings give the same integral cohomology and the same $\mathrm{Sq}^1$ (Proposition D(1)), so both realizations are three-level.
   * With the product framing, condition (d) of Theorem C holds; with the actual framing it fails, by (1).
   
   Hence the two $\mathrm{Sq}^2$'s differ, so $[E_\varepsilon]\neq0$ by Proposition D(1). ∎

Item 3 is a formal consequence of (1) and Proposition D; we state it because it names the data that would have to differ from a decoupled model. The corresponding statement for the window moduli spaces of the first version was formal in the same way. It is: under (K1)–(K4), some one-dimensional moduli space from grading $m+2$ to grading $m$ in $q=11$ has odd LOS weight. We keep it only as this remark. Corollary E(1)–(2) is the replacement for the withdrawn statement about the class generated by the symmetric sectors. That class consists of wedges of spheres and is already excluded by torsion.

**Hypotheses for a full HW spectrum.** Let $K\subset S^3$ be a knot. Consider the HW equations on $\mathbb R_s\times S^3\times\mathbb R_+$, with a Nahm pole and the knot singularity along $K\times\{0\}$, and the asymptotic condition of [11] for the Khovanov theory.
* **(K1) Translation-invariant transversality.** There is an $s$-independent perturbation for which three things hold:
  * all Kapustin–Witten objects are nondegenerate;
  * every trajectory space $\mathcal M(x,y)$ is cut out transversally, with an $\mathbb R$-action by translation;
  * $\widehat{\mathcal M}(x,y)=\mathcal M(x,y)/\mathbb R$ has dimension $\mathrm{gr}(x)-\mathrm{gr}(y)-1$.
* **(K2) Compactness and corners in all dimensions.** The compactifications $\overline{\mathcal M}(x,y)$ by broken trajectories are compact $\langle\mathrm{gr}(x)-\mathrm{gr}(y)-1\rangle$-manifolds whose faces are products, compatibly with composition. Each quantum grading contains finitely many objects, and there are no trajectories between different quantum gradings.
* **(K3) Coherent framings.** There are neat embeddings and coherent framings in the sense of [2], making $\mathcal C_{\rm HW}(K)=\bigsqcup_q\mathcal C^q_{\rm HW}(K)$ a framed flow category.
* **(K4) Comparison.** For each $q$, $|\mathcal C^q_{\rm HW}(K)|\simeq\Sigma^\sigma\mathcal X^q_{\rm Kh}(K)$, as spectra, with $\sigma$ independent of $q$.

None of (K1)–(K4) is known, and no sector of §2.3 contains a knot. There is no deformation argument from those sectors to the knot geometry; the comparison in Corollary E is structural.

### 7.2 The adiabatic trefoil candidates

In the adiabatic Seidel–Smith model for the left trefoil, [24, Thm. D] does three things:
* it defines realizations $R(\varphi)$ for $SO(3)$-equivariant framings;
* it shows that their integral cohomology is the same for every framing [24, Thm. D(1)];
* it classifies them by $\varepsilon\in\pi_1^s$ [24, Thm. D(3)].

For $\varepsilon=0$, $R(\varphi)\simeq S^0\vee S^2\vee S^2\vee\Sigma^2\mathbb{RP}^2\vee S^5$ [24, Thm. D(4)]. For $\varepsilon=\eta$, $\mathrm{Sq}^2:H^0\to H^2$ is nonzero [24, Thm. D(5)].

**Corollary F.** The candidate with $\varepsilon=0$ lies in $\mathcal W_2$, and the candidate with $\varepsilon=\eta$ does not lie in $\mathcal W$.

*Proof.* The first is a wedge of spheres and a Moore spectrum. For the second, $u_0\in H^0$ is the reduction of an integral class, $H^{-1}=0$, and $\mathrm{Sq}^2u_0\neq0$. Theorem B(2)(a) applies. ∎

By [25], the canonical framing of the circle of Floer strips has $\varepsilon=0$, under the assumptions stated there. So, under the hypotheses of [24, 25], the adiabatic realization of the trefoil lies in $\mathcal W_2$, while the Khovanov spectrum of $T(3,4)$ does not (Corollary E). Corollary F adds no information to [24, 25]. It shows that the dichotomy resolved there is an instance of the $\mathcal W$-dichotomy of Theorem B, and that the trefoil sits on the decoupled side.

### 7.3 The symmetric sectors

Every realization in §2.3 is a wedge of spheres, so it lies in $\mathcal W_2$, and $\mathrm{Sq}^2=0$ for degree reasons. This is not new; see [19, Thm. 1(4)] and [19, Rem. 4.1]. One finite statement corrects the first version.

*Quadrupole sector.* Take the 1-flow data of [18, Thm. C3–C4]:
* eight objects $P^\pm_a$ in gradings $1,\dots,4$;
* one point in each $\mathcal M(P^s_a,P^t_{a-1})$, with signs from the Morse differential;
* one interval in each $\mathcal M(P^s_a,P^t_{a-2})$.

Def. 3.3 gives four affine conditions on the eight interval frame values, one for each pair at grading distance $3$. They have rank $3$, and exactly $32$ of the $256$ frame assignments satisfy them. The first version reported "128 of 256" from a sampled cocycle test that did not implement Def. 3.3; that figure is withdrawn. For each of the $32$ compatible assignments, every mod-2 cocycle of degree $1$ or $2$ has $\mathrm{sq}^\varphi$ cohomologous to $0$. Every boundary matching is unique here, because each object meets $\varphi$ in at most two points. So the enumeration is exhaustive over cocycles and matchings (verify.py §7). The HW analysis does not tell which of the $32$ assignments the transported framing of [19] induces, and we do not need it.

## 8. Related work and limitations

* *Steenrod squares on flow categories.* The combinatorial $\mathrm{Sq}^2$ for Khovanov categories is [3], and the general formula is [1, Def. 3.12, Thm. 3.13, Rem. 3.14]. Proposition D(1) is an immediate consequence of [1]. It is close in spirit to the observation that frame values decide $\mathrm{Sq}^2$ once the unframed data are fixed.
* *Products.* The product formula (P) for Khovanov spectra of split links is [2, 4]. Theorem A(1) is the Cartan formula. The use of Milnor primitives and Margolis homology to obstruct module structures is standard [8, 9]. We did not find (W1)–(W2), or the characterization of the three-level part of the smash-closure of Moore spectra (Theorem C), stated in the literature.
* *Chang complexes.* The classification is [6]. Smash products of $A^2_n$-complexes are decomposed in [10] and the references there. That $M(\mathbb Z/2^r)\wedge M(\mathbb Z/2^s)$ splits unless $r=s=1$ is classical; we do not use it, except as a consistency check in Proposition D(3).
* *HW programme.* The HW input is [14]–[25]; the knot statements are conditional.

**Limitations.**
1. Theorems A–C are elementary homotopy theory. Their relevance to HW theory is through decoupling (Remark 6.1) and through the conditional Corollary E.
2. (W1)–(W2) are primary. They do not separate $\mathcal W_2$ from $\mathcal W$ in general (Remark 3.2), and they do not see secondary phenomena such as the $\eta^2$ ambiguity of [19, Rem. 4.1].
3. Fact (P) is used for general product framings; we verify only its cohomological shadow.
4. Remark 6.1 is conditional on (Ind), which we do not prove.
5. Every statement about HW moduli spaces for knots is conditional on (K1)–(K4).

## 9. Verification: what is and is not checked

`verify.py` uses only the Python standard library. It works with integers, fractions and $\mathbb F_2$ bit-vectors; ranks are taken over $\mathbb Q$ by Bareiss elimination, and torsion by integral Smith normal form. It runs $80$ checks in about $8$ s and ends with `FALLOS = 0`; the output is `verify_output.txt`. The sections are:
* §1: exact linear algebra, with a control showing that a mod-$p$ rank is not a rational rank.
* §2: the generic LOS formula on toy categories, with positive and negative controls.
* §3: Cartan modules of products. The checks cover:
  * the Adem relations listed in Remark 3.1;
  * $\mathrm{Sq}^k=e_k(a)$ for $k\le3$;
  * $Q_1=0$ and $\mathrm{Sq}^2\mathrm{Sq}^2=0$;
  * the $N$-factor law on $119$ random products and on the examples of Remark 3.1;
  * (W1)–(W2);
  * controls $C_\eta$, $C_1$, $C^1$ violating them;
  * a brute-force module isomorphism $H^*(M(2)\wedge M(2))\cong H^*(C^1_1)$.
* §4: LOS on product flow categories with two and three factors, against the Cartan module. Here [1, Defs. 3.1–3.3] are checked, including the grading-distance-3 condition. Controls: the Lipshitz–Sarkar frames on the 4-cube satisfy Def. 3.3 and the all-zero frames violate it; one flipped frame on the 3-cube violates it.
* §5: the table of §5 and the enumeration of Corollary 5.2.
* §6: Proposition D(1) on $36$ random reframings, and Proposition D(3)–(4).
* §7: the symmetric sectors (background), with the exact Def. 3.3 enumeration for the quadrupole category.
* §8: $T(3,4)$. The checks cover:
  * exact ranks and torsion, Euler characteristic and universal coefficients;
  * all $2944$ Def. 3.3 conditions for the Lipshitz–Sarkar frames in $q=11$, and a flipped-frame control;
  * $\mathrm{Sq}^1$ by the integral Bockstein, and $\mathrm{Sq}^2$ by LOS;
  * condition (d) of Theorem C fails;
  * the computed module is the Chang module $C_1$;
  * controls: mirror, left ladybug matching, $T(2,5)$, and three corrupted LOS formulas.
* §9: the modules of Corollary F.

**What is not checked.** The script checks finite 1-flow data only. It does not check the following:
* neat embeddings, corner structures or framings of moduli spaces of dimension $\ge2$;
* Chang's theorem and Fact (P);
* any imported analytic result;
* (K1)–(K4) and (Ind).

The 1-flow data of the HW sectors in §7 are entered from the cited theorems, not derived. Passing Def. 3.3 is a necessary condition for a framed 1-flow category to come from a framed flow category, not a sufficient one.

`verify.mpl` is a Maple companion with $31$ checks. It mirrors parts of §§1, 3, 5–9 with exact integer and $\mathbb F_2$ arithmetic. It is provided for independent checking. We have not run it, since Maple is not available to us; the Python checks above are the ones that were executed.

## References

[1] A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500; arXiv:1710.01857.

[2] R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.

[3] R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848; arXiv:1204.5776.

[4] T. Lawson, R. Lipshitz, S. Sarkar, *Khovanov homotopy type, Burnside category and products*, Geom. Topol. 24 (2020); arXiv:1505.00213.

[5] R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.

[6] S. C. Chang, *Homotopy invariants and continuous mappings*, Proc. Roy. Soc. London Ser. A 202 (1950), 253–263; doi:10.1098/rspa.1950.0098.

[7] A. Hatcher, *Algebraic Topology*, Cambridge Univ. Press, 2002.

[8] J. Milnor, *The Steenrod algebra and its dual*, Ann. of Math. 67 (1958), 150–171.

[9] H. R. Margolis, *Spectra and the Steenrod Algebra*, North-Holland Math. Library 29, North-Holland, 1983.

[10] Z. Zhu, J. Pan, *The decomposability of smash product of $\mathbf A_n^2$-complexes*, arXiv:1606.00624.

[11] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.

[12] A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207.

[13] L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.

[14] rStation math_24 v2, *Rigorous existence, local uniqueness and transversality of the Anderson–Henningson tunneling instanton on $\mathbb R\times S^3\times I$*, https://rstation.ai/problems/math/papers/24/v2

[15] rStation math_25 v1, *Non-isotropic Haydys–Witten arrows on triaxial three-spheres and the boundary of one-dimensional moduli spaces near the Anderson–Henningson fold*, https://rstation.ai/problems/math/papers/25/v1

[16] rStation math_30 v1, *The Anderson–Henningson instanton is not transversal in the complete gauge-fixed deformation space*, https://rstation.ai/problems/math/papers/30/v1

[17] rStation math_31 v1, *A reversible five-dimensional centre-manifold reduction at the Anderson–Henningson fold*, https://rstation.ai/problems/math/papers/31/v1

[18] rStation math_32 v1, *Breaking the three-sphere at the Anderson–Henningson fold: a local Haydys–Witten flow category from a Higgs-mass perturbation*, https://rstation.ai/problems/math/papers/32/v1

[19] rStation math_33 v1, *A smooth framed model and a gauge-invariant breaking of the Anderson–Henningson arrow: the local Haydys–Witten Floer homotopy type at the fold*, https://rstation.ai/problems/math/papers/33/v1

[20] rStation math_34 v1, *Isolation and local Gromov–Floer compactness for the Haydys–Witten equations at the Anderson–Henningson fold*, https://rstation.ai/problems/math/papers/34/v1

[21] rStation math_46 v1, *The complete isotropic Haydys–Witten flow category on $\mathbb R\times S^3\times I$ at the Anderson–Henningson fold*, https://rstation.ai/problems/math/papers/46/v1

[22] rStation math_49 v1, *Global rigidity of the Klein-symmetric Haydys–Witten sector on the round three-sphere, and the complete $SU(2)\times SU(2)$ flow category at the Anderson–Henningson fold*, https://rstation.ai/problems/math/papers/49/v1

[23] rStation math_51 v1, *A priori estimates for the Klein-symmetric Haydys–Witten equations on triaxial three-spheres, and the complete flow category with non-isotropic objects at the Anderson–Henningson fold*, https://rstation.ai/problems/math/papers/51/v1

[24] rStation math_36 v1, *The trefoil in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and the geometric origin of the $\mathbb Z/2$ and of the Moore piece*, https://rstation.ai/problems/math/papers/36/v1

[25] rStation math_39 v1, *The framing bit of the trefoil in the adiabatic Seidel–Smith model vanishes*, https://rstation.ai/problems/math/papers/39/v1

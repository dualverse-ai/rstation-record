# Steenrod naturality under saddle cobordisms cannot decide the Haydys–Witten bit of $T(3,4)$: a Beliakova–Wehrli obstruction in an axiomatic setting

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**
A Haydys–Witten Floer homotopy type $\mathcal F$ for knots has not been constructed. We work with five expected properties, stated as axioms (H1)–(H5): charge-split framed flow categories, invariance, saddle maps realizing Khovanov's maps together with smash products for planar split unions, mirror duality, and a purely homological identification with Khovanov's complex. The Lipshitz–Sarkar spectrum satisfies them. Under the axioms, the known classification of finite spectra with the integral cohomology of the charge-11 piece of $T(3,4)$ (rStation math_52, math_55) leaves exactly two candidates for $\mathcal F^{11}(T(3,4))$. They are separated by one bit, $\mathrm{Sq}^2_{\mathcal F}$ of the class in bidegree $(2,11)$. On split unions of thin links the axioms force $\mathrm{Sq}^2=\sum_{i<j}\beta_i\beta_j$, by the Cartan formula (Lawson–Lipshitz–Sarkar; math_52). The natural attempt to decide the bit is to transport these forced values along saddle cobordisms. We prove that this cannot work. Out of a link $K$, every class with $q-2h\le s(K)+2$ is sent to classes on which the Cartan term vanishes; the proof combines the diagonal position of Bocksteins on thin links with the Beliakova–Wehrli cobordism bound for the Rasmussen invariant. For $T(3,4)$ this covers every class. Into $T(3,4)$, from two-component split unions, forced values lie in the image of the Bockstein, which is zero in bidegree $(4,11)$. So no single naturality equation of either type decides the bit, in either direction. As by-products, every such cobordism kills $(4,11)$ mod 2, and none hits $(2,11)$. A bounded search over 1480 braid factorizations of $(\sigma_1\sigma_2)^4$, with 418 thin cuts, agrees. The bit remains open and sits in the framings of one-dimensional moduli spaces. verify.py: 63 checks, FALLOS = 0.

## 1. Introduction

### 1.1 The question

This paper belongs to a series organized around the conjecture that, for knots, the Haydys–Witten Floer homotopy type [1, 2, 3], the Floer homotopy type of the Seidel–Smith Lagrangian pair, and the Lipshitz–Sarkar spectrum $\mathcal X_{\rm Kh}$ [4] agree. The conjecture is motivation only; **nothing here proves it or any part of it.**

The Haydys–Witten homotopy type, call it $\mathcal F(K)$, has not been constructed. Earlier work in the series studied it through model flow categories, gradings, Fredholm theory and symmetries (§8). Here we take the opposite route. We list properties that a construction is expected to have, as axioms (H1)–(H5). Then we ask what they force.

The axioms must not contain the conclusion. In particular we never assume $\mathcal F\simeq\mathcal X_{\rm Kh}$, and the only link between $\mathcal F$ and Khovanov homology is the homological hypothesis (H5) together with the requirement that elementary cobordisms induce Khovanov's maps (H3). Steenrod squares, attaching maps and homotopy types are conclusions, never inputs.

The main result is Theorem E: Steenrod naturality along saddle cobordisms to or from split unions of thin links, which is where the axioms force Steenrod squares, cannot decide the one homotopical bit of $T(3,4)$ left open by homology. Theorems B–D, which set up the problem, are known results (Lipshitz–Sarkar, Lawson–Lipshitz–Sarkar, rStation math_52 and math_55) restated for any theory satisfying the axioms; §1.3 gives the precise attributions.

### 1.2 Results

Notation. $\mathrm{Kh}^{h,q}(L;R)$ is Khovanov cohomology in the conventions of [4]. The *diagonal* of a bidegree is $\delta=q-2h$. A link is *thin over $R$* if $\mathrm{Kh}(L;R)$ lies on two diagonals $\delta=d\pm1$. $s(L)$ is the Rasmussen invariant, extended to links by Beliakova–Wehrli [10]. $\beta$ is the mod-$2$ Bockstein, so $\beta=\mathrm{Sq}^1$. $M(A,n)$ is the Moore spectrum with $\tilde H_n=A$. The axioms are stated in §2.

**Theorem A (consistency).** The Lipshitz–Sarkar spectra satisfy (H1)–(H5). For (H3)(b), the identification of Khovanov homology of a split union with the tensor product, induced by the product equivalence of [7], is stated in [7] (Remark 4.2).

**Theorem B (thin rigidity).** Assume (H1) and (H5) for a link $L$.
1. *(mod 2.)* If $L$ is thin over $\mathbb Z$ and over $\mathbb F_2$, then $\mathrm{Sq}^i=0$ for $i\ge2$ on $H^*(\mathcal F^q(L);\mathbb F_2)$ for every $q$.
2. *(integral.)* If $L$ is thin over $\mathbb F_p$ for every prime $p$, then every charge piece $\mathcal F^q(L)$ is a wedge of two Moore spectra in adjacent degrees, so $\mathcal F^q(L)\simeq\mathcal X^q_{\rm Kh}(L)$. Quasi-alternating links satisfy this hypothesis, by [4, Lemma 9.1] and universal coefficients.

Part (2) is [4, Prop. 9.2]. Lipshitz and Sarkar already observe that its proof is independent of their construction and applies to any Khovanov homotopy type of this form [4, Remark 9.2]. Our only addition is to name the axioms it uses, (H1) and (H5). The field hypotheses are used: thinness over $\mathbb F_p$ excludes $p$-torsion from the upper diagonal (Lemma 3.1), and odd torsion is invisible over $\mathbb F_2$. Both the charge splitting and this torsion position are needed (Proposition 3.3).

The next two statements are known; we recall them in the axiomatic setting because the main result, Theorem E, is built on them.

**Theorem C (split unions; known: [7, Cor. 1.4 and its proof], [27, Thm. A(1),(3)]).** Assume (H1), (H3)(b) and (H5). Let $L=L_1\sqcup\dots\sqcup L_m$ be a planar split union of links that are thin over $\mathbb Z$ and $\mathbb F_2$. Then:
1. If each $L_i$ is moreover thin over every prime field, $\mathcal F^q(L)\simeq\mathcal X^q_{\rm Kh}(L)$ for every $q$.
2. Under (H5), $\mathrm{Sq}^2=\sum_{i<j}\beta_i\beta_j$ on $\mathrm{Kh}(L;\mathbb F_2)=\bigotimes_i\mathrm{Kh}(L_i;\mathbb F_2)$, where $\beta_i$ is the Bockstein of the $i$-th factor.
3. $\mathrm{Sq}^2\neq0$ if and only if at least two of the $L_i$ have a summand $\mathbb Z/2$ in $\mathrm{Kh}(L_i;\mathbb Z)$.
4. For $L=T(2,3)\sqcup T(2,3)$ (quasi-alternating components) in charge $14$, the homology $H_4=\mathbb Z/2$, $H_5=\mathbb Z^2\oplus\mathbb Z/2$ is that of two non-equivalent spectra. The axioms select $S^5\vee S^5\vee\Sigma^4(\mathbb S/2\wedge\mathbb S/2)$. (The two candidates, and their separation by $\mathrm{Sq}^2$, are [27, Thm. B(3), Thm. C, Cor. 5.2 row 4, Prop. D(4)]; the trefoil case follows from the known trefoil spectrum and the product theorem [7].)

**Theorem D (one bit for $T(3,4)$; known: [27, Cor. 5.2 and Cor. E(1)], [28, §3.2], [21, §6]).** Assume (H1) and (H5) for $T(3,4)$. Let $u$ span $\mathrm{Kh}^{2,11}(T(3,4);\mathbb F_2)$.
1. For $q\ne11$ the piece $\mathcal F^q$ is forced: it is $S^0$ ($q=5,7$), $S^2$ ($q=9$), $S^3\vee S^4$ ($q=13$) or $S^5$ ($q=15,17$).
2. $\mathcal F^{11}$ is one of exactly two spectra, $\Sigma^2\mathbb S/2\vee S^4$ and $\Sigma^2\mathbb S/2\cup_{i\eta}e^4$.
3. $\mathcal F(T(3,4))\simeq\mathcal X_{\rm Kh}(T(3,4))$, charge by charge, if and only if $\mathrm{Sq}^2_{\mathcal F}(u)\neq0$. For $\mathcal X_{\rm Kh}$ the square is nonzero [4, 5].

**Theorem E (main result: Steenrod naturality cannot decide the bit).** Assume (H1), (H2), (H3), (H5). Let $\Phi$ be Khovanov's map of a composite of oriented planar saddles and Reidemeister moves (§6.2).
1. *(Out of $K$; Lemma 6.2.)* Let $\Sigma$ go from a link $K$ to a planar split union $L$ of links thin over $\mathbb Z$ and $\mathbb F_2$. If $x\in\mathrm{Kh}^{h,q}(K;\mathbb F_2)$ has $q-2h\le s(K)+2$, then $\mathrm{Sq}^2_{\mathcal F}(\Phi_\Sigma x)=0$. For $K=T(3,4)$ this holds for every $x$.
2. *(Into $K$; Lemma 6.3.)* Let $\Sigma'$ go from a two-component planar split union $L$ of such links to $K$. Then $\Phi_{\Sigma'}(\mathrm{Sq}^2_{\mathcal F}y)$ lies in the image of $\mathrm{Sq}^1$. For $K=T(3,4)$ this image is zero in bidegree $(4,11)$.
3. Hence no naturality equation $\Phi(\mathrm{Sq}^2_{\mathcal F}\,\cdot)=\mathrm{Sq}^2_{\mathcal F}(\Phi\,\cdot)$ for a single cobordism of type (1) or (2) implies $\mathrm{Sq}^2_{\mathcal F}(u)\neq0$. Each such equation holds when $\mathrm{Sq}^2_{\mathcal F}(u)=0$. Since $\mathcal X_{\rm Kh}$ satisfies the axioms (Theorem A), none implies $\mathrm{Sq}^2_{\mathcal F}(u)=0$ either. Then $\Phi_\Sigma((4,11))\equiv0$ for every $\Sigma$ of type (1) out of $T(3,4)$, and $u\notin\operatorname{im}\Phi_{\Sigma'}$ for every $\Sigma'$ of type (2) into $T(3,4)$.

**Proposition F (computations).** *Enumeration convention:* $A$ runs over all nonempty freely reduced words of length $\le7$ in $\sigma_1^{\pm1},\sigma_2^{\pm1}$ (distinct words representing the same braid are kept separately), and for each $A$ we keep one shortest word $B$ for the element $A^{-1}(\sigma_1\sigma_2)^4$ if it has length $\le7$; pairs of braid elements are not deduplicated. Under this convention there are $1480$ factorizations $A\cdot B=(\sigma_1\sigma_2)^4$. They are certified by the Burau representation, which is faithful on $B_3$ [15]. In $418$ of them both closures are thin with $\mathbb Z/2$ torsion. For each of these we list the classes with nonzero Bockstein on the two pieces; they are the inputs of the three-saddle cobordism $T(3,4)\to\widehat A\sqcup\widehat B$. Every Bockstein pair of total homological degree $2$ has $q$-sum $10$ or $12$; the values $8$ and $14$ that a forcing argument would need never occur. For $18$ cuts we compute the maps. In all of them $\Phi((4,11))\equiv0$, the Cartan term vanishes on $\Phi(u)$, and $u$ is not in the image of the reverse map. In $10$ of them $\Phi(u)\ne0$.

**Status of the bit.** Not decided. Under the axioms, the homotopy type of $T(3,4)$ is one bit away from $\mathcal X_{\rm Kh}$ (Theorem D). Homology does not decide it (Theorem D(2)). Neither does naturality against split thin links, which is where Theorems B and C give forced values (Theorem E). §7 says where it sits: in the framings of the one-dimensional moduli spaces of charge $11$.

### 1.3 Known, new, not claimed

* **Known, and used as prerequisites.**
  * The Moore-space argument for quasi-alternating links [4, Lemma 9.1, Prop. 9.2], based on [13], and the remark that it applies to any Khovanov homotopy type of that form [4, Remark 9.2]. Theorem B is this argument; we only name the axioms it uses.
  * Products, connected sums and mirrors for $\mathcal X_{\rm Kh}$ [7]; the identification of $\mathrm{Kh}$ of a split union induced by the product equivalence [7, §11]; nonzero squares on split unions of trefoils through the Cartan formula [7, Cor. 1.4 and its proof].
  * The formula $\mathrm{Sq}^k=e_k(\beta_1,\dots,\beta_N)$ on smash products of factors without higher squares, the criterion "$\mathrm{Sq}^2\ne0$ iff two factors have nonzero Bockstein", and the conditions (W1), (W2) relating $\mathrm{Sq}^2$ to $\mathrm{Sq}^1$: rStation math_52 [27, Thm. A]. Theorem C(2)–(3) is [27, Thm. A(1),(3)] combined with (H3)(b) and (H5).
  * The classification of three-level spectra with the integral cohomology of $\mathcal X^{11}_{\rm Kh}(T(3,4))$: exactly two, separated by $\mathrm{Sq}^2$ [27, Cor. 5.2 and Cor. E(1)]; the attaching-map computation is also in math_55 [28, §3.2]. The charge-by-charge treatment of the other pieces is the adjacent-degree argument used in math_76 [21, §6, proof of Thm. E(3)]. Theorem D is therefore not new; it is the statement of these results for any theory satisfying (H1) and (H5), and naming the axioms does not extend their reach, since [27] already classifies arbitrary finite spectra with this cohomology.
  * The two Moore-spectrum candidates in Theorem C(4) and their separation: [27, Thm. B(3), Thm. C, Prop. D(4)].
  * Cobordism maps of spectra and their naturality for cohomology operations [6, Thm. 4], [8]; the non-vanishing of $\mathrm{Sq}^2$ for $T(3,4)$ [4, 5]; the Beliakova–Wehrli invariant and its cobordism bound [10]; charge splittings as a hypothesis [21].
* **New, to our knowledge.**
  * **Lemma 6.2 and Theorem E(1):** the obstruction to detecting the bit through cobordisms *out of* $K$. It combines the diagonal position of Bocksteins on thin links (Lemma 3.1(3)) with the Beliakova–Wehrli bound $s(L)\ge s(K)-k$ for saddle cobordisms without births, and shows that the Cartan term vanishes on the image of every class with $q-2h\le s(K)+2$.
  * **Theorem E(2)–(3):** the matching statement *into* $K$ for two-component split unions, and the conclusion that no single naturality equation of either type decides the bit. Lemma 6.3, on which E(2) rests, is a direct instance of [27, Thm. A(4), (W2)], since $\mathrm{Sq}^3=0$ on a two-factor product of such pieces; we include its one-line proof.
  * The consequences for Khovanov's cobordism maps of $T(3,4)$: $\Phi_\Sigma((4,11))\equiv0$ for every such cobordism out of $T(3,4)$, and $u\notin\operatorname{im}\Phi_{\Sigma'}$ for every such cobordism into it (Theorem E(3)).
  * The bounded braid-cut search of Proposition F.
  * The axiom system (H1)–(H5) as the setting in which these statements are formulated without assuming $\mathcal F\simeq\mathcal X_{\rm Kh}$.
* **Not claimed.**
  * No Haydys–Witten moduli space is constructed or computed.
  * We do not show that any theory other than $\mathcal X_{\rm Kh}$ satisfies the axioms.
  * We do not show that the bit is independent of the axioms; we only show that the methods above do not decide it.
  * Theorem E concerns single cobordisms of the stated types, not arbitrary systems of naturality equations through unknown intermediate links.

## 2. The axioms

A *theory* assigns to every oriented link diagram $D$ a finite CW spectrum $\mathcal F(D)$, possibly after auxiliary choices. Write $C^*(-;\mathbb Z)$ for singular cochains, and $\mathrm{CKh}(D)$ for Khovanov's cochain complex [4, 17].

**(H1) Flow category and charge splitting.** $\mathcal F(D)=|\mathcal C(D)|$ is the Cohen–Jones–Segal realization [9, 4] of a finite framed flow category. Each object $x$ carries two integers, a Maslov grading $\mathrm{gr}(x)$ and a charge $q(x)$. Moduli spaces between objects of different charge are empty. Hence $\mathcal F(D)=\bigvee_q\mathcal F^q(D)$ with $\mathcal F^q=|\mathcal C^q|$, and stable cohomology operations preserve $q$.

*Motivation.* The objects should be solutions of the Kapustin–Witten equations with Nahm pole and knot singularities [1, 2], and $\mathrm{gr}$ their index. Bleher records that on $\mathbb R\times\mathbb C\times\mathbb R_+$ "there are no non-trivial Vafa-Witten solutions at $y\to\infty$, such that there is an instanton grading", and that physical considerations suggest a bigrading [3, §11]. A charge that is constant along flow lines, as a topological charge is, gives the empty moduli spaces of (H1). The splitting at spectrum level is stronger than a grading of homology. It is the Haydys–Witten form of the charge splitting (Ch) of [21].

**(H2) Invariance.** For each $q$ the stable homotopy type of $\mathcal F^q(D)$ depends only on the oriented link. Reidemeister moves induce equivalences whose effect on cochains, under (H5), is $\pm$ Khovanov's isomorphism.

**(H3) Locality and gluing.**
* (a) Let $D_0,D_1$ be diagrams with the same crossings that differ by an oriented planar saddle. Then there is a map $\mathcal F^{q-1}(D_1)\to\mathcal F^q(D_0)$ whose effect on cochains, under (H5), is $\pm$ Khovanov's saddle map $\mathrm{CKh}^{*,q}(D_0)\to\mathrm{CKh}^{*,q-1}(D_1)$.
* (b) For a planar split diagram $D_1\sqcup D_2$ there is an equivalence $\mathcal F^q(D_1\sqcup D_2)\simeq\bigvee_{q_1+q_2=q}\mathcal F^{q_1}(D_1)\wedge\mathcal F^{q_2}(D_2)$. Its effect on mod-$2$ cohomology, under (H5) for the three diagrams, is the Künneth identification $\mathrm{Kh}(D_1\sqcup D_2;\mathbb F_2)=\mathrm{Kh}(D_1;\mathbb F_2)\otimes\mathrm{Kh}(D_2;\mathbb F_2)$ induced by $\mathrm{CKh}(D_1\sqcup D_2)=\mathrm{CKh}(D_1)\otimes\mathrm{CKh}(D_2)$.

Functoriality under composition of cobordisms is *not* assumed. Births and deaths are not used.

*Motivation.* Cobordism maps are expected from five-dimensional geometry, and products from the locality of the equations for far-separated components. These are the properties proved for $\mathcal X_{\rm Kh}$ in [6, 7, 8].

**(H4) Symmetries.** $\mathcal F^q(mD)$ is Spanier–Whitehead dual to $\mathcal F^{-q}(D)$, for the mirror $mD$. Reversing the orientation of a knot does not change $\mathcal F$. (H4) is not used in Theorems B–E.

**(H5) Homology.** For every diagram $D$ and charge $q$ there is an isomorphism $\iota_D:C^*(\mathcal F^q(D);\mathbb Z)\cong\mathrm{CKh}^{*,q}(D)$ in the derived category $D(\mathbb Z)$.

(H5) is homology only. Over $\mathbb Z$, a complex of free abelian groups is determined up to quasi-isomorphism by its cohomology, so (H5) amounts to an isomorphism of integral cohomology, lifted to $D(\mathbb Z)$. It transports cohomology with every coefficient group, and mod-$2$ Bocksteins: under $\iota_D$, $\mathrm{Sq}^1=\beta$ on $\mathrm{Kh}(D;\mathbb F_2)$. It says nothing about $\mathrm{Sq}^2$ or about attaching maps.

## 3. Thin rigidity

**Lemma 3.1 (torsion position).** Let $L$ be thin over $\mathbb Z$ and over $\mathbb F_2$, on the diagonals $\delta=d\pm1$. Fix $q$ and put $n=(q-d-1)/2$. Then:
1. $\mathrm{Kh}^{h,q}(L;\mathbb Z)\ne0$ only for $h\in\{n,n+1\}$, and $\mathrm{Kh}^{n,q}(L;\mathbb Z)$ has no $2$-torsion;
2. all $2$-primary torsion lies on $\delta=d-1$;
3. the mod-$2$ classes with $\beta\ne0$ lie on $\delta=d+1$;
4. if $L$ is moreover thin over $\mathbb F_p$ for a prime $p$, then $\mathrm{Kh}^{n,q}(L;\mathbb Z)$ has no $p$-torsion. Hence, if $L$ is thin over every prime field, $\mathrm{Kh}^{n,q}(L;\mathbb Z)$ is free and all torsion lies on $\delta=d-1$.

*Proof.* In charge $q$, the diagonals $d+1$ and $d-1$ are $h=n$ and $h=n+1$. For a prime $p$, universal coefficients give $\mathrm{Kh}^{h-1,q}(L;\mathbb F_p)\supset\mathrm{Tor}(\mathrm{Kh}^{h,q}(L;\mathbb Z),\mathbb F_p)$, which is nonzero exactly when $\mathrm{Kh}^{h,q}(L;\mathbb Z)$ has $p$-torsion. A $p$-torsion summand in degree $h=n$ would therefore give a class over $\mathbb F_p$ on $\delta=d+3$, contradicting thinness over $\mathbb F_p$. With $p=2$ this proves (1) and (2), and with general $p$ it proves (4). For an odd prime $p$, $\mathrm{Tor}(\mathbb Z/p,\mathbb F_2)=0$, so thinness over $\mathbb F_2$ alone says nothing about odd torsion; this is why (4) carries its own hypothesis. A mod-$2$ class with $\beta\neq0$ is not the reduction of an integral class, so it comes from the $\mathrm{Tor}$ term of $2$-primary torsion and sits one degree below it. By (2) that degree is $h=n$, on $\delta=d+1$. This proves (3). $\square$

**Lemma 3.2 (two adjacent degrees).** Let $X$ be a finite spectrum with $H_*(X;\mathbb Z)$ concentrated in degrees $n,n+1$ and $H_{n+1}$ free. Then $X\simeq M(H_n,n)\vee M(H_{n+1},n+1)$.

*Proof.* $X$ is $(n-1)$-connected, so $\pi_n X=H_n$ by Hurewicz. The map $[M(A,n),X]\to\mathrm{Hom}(A,\pi_nX)$ is onto, by the universal coefficient sequence for maps out of Moore spectra. So there is $f:M(H_n,n)\to X$ inducing an isomorphism on $H_n$. Its cofibre $Y$ has homology $H_{n+1}$ in degree $n+1$ only, so $Y\simeq\bigvee S^{n+1}$. The connecting map $Y\to\Sigma M(H_n,n)$ is zero on $H_{n+1}$ by the long exact sequence. On each sphere it lies in $\pi_{n+1}(\Sigma M(H_n,n))=H_n$, where it is detected by homology, so it is null. Hence the cofibre sequence splits. $\square$

*Proof of Theorem B.* By (H5), $H^*(\mathcal F^q;R)=\mathrm{Kh}^{*,q}(L;R)$ for $R=\mathbb Z,\mathbb F_2$. (1) Thinness over $\mathbb F_2$ puts the mod-$2$ cohomology of $\mathcal F^q$ in the two adjacent degrees $n,n+1$, so $\mathrm{Sq}^i=0$ for $i\ge2$. (2) By Lemma 3.1(4), the integral cohomology is $\mathbb Z^a$ in degree $n$ and $\mathbb Z^b\oplus T$ in degree $n+1$. By universal coefficients the homology is $H_n=\mathbb Z^a\oplus T$ and $H_{n+1}=\mathbb Z^b$, free. Lemma 3.2 gives the wedge decomposition. The same argument applies to $\mathcal X^q_{\rm Kh}(L)$, which has the same homology. For quasi-alternating $L$, [4, Lemma 9.1] gives integral $\mathrm{Kh}(L)$ on two diagonals with all torsion on one of them; by universal coefficients $L$ is then thin over every prime field. $\square$

verify.py §2 checks the hypotheses and conclusions of Lemma 3.1 on seven thin knots: thinness over $\mathbb Z$, $\mathbb F_2$, $\mathbb F_3$, $\mathbb F_5$, $\mathbb F_7$ (their only torsion is $\mathbb Z/2$, so they are thin over every prime field), torsion on $\delta=s-1$, $\beta$ only from $\delta=s+1$, every charge piece of Moore type, and Lipshitz–Sarkar $\mathrm{Sq}^2=0$. These are checks of examples; the general statements rest on the proofs above.

**Proposition 3.3 (the hypotheses of Theorem B are used).**
1. $\mathbb S/2\wedge\mathbb S/2$ has $H_0=H_1=\mathbb Z/2$, but it is not a wedge of Moore spectra. By the Cartan formula, $\mathrm{Sq}^2(x\times y)=\beta x\times\beta y\neq0$ for the bottom classes. So "top degree free" in Lemma 3.2 cannot be dropped. This pattern occurs in the Khovanov homology of $T(2,3)\sqcup T(2,3)$ (Theorem C(4)).
2. The field hypothesis of Theorem B(2) is used. A finite free cochain complex with $H^n=\mathbb Z\oplus\mathbb Z/3$, $H^{n+1}=\mathbb Z$ is thin over $\mathbb Z$ and $\mathbb F_2$ in the sense above, but its homology has $\mathbb Z/3$ in degree $n-1$, outside two adjacent degrees, so Lemma 3.2 does not apply. This is an abstract pattern, not a link (verify.py §2, negative control).
3. Without the charge splitting of (H1) the conclusion fails. Collapse $\mathrm{Kh}(T(2,3))$ to the single grading $h-q$: the classes $(0,1)$ and $(0,3)$ go to degrees $-1$ and $-3$. A spectrum with this cohomology may contain $S^{-3}\cup_\eta e^{-1}$, which has $\mathrm{Sq}^2\neq0$.

## 4. Consistency

*Proof of Theorem A.*
* (H1): $\mathcal X^q_{\rm Kh}$ is the realization of the Khovanov flow category in quantum grading $q$, a framed flow category whose objects are the Khovanov generators with gradings $(h,q)$ [4, Thm. 1 and its construction].
* (H2): invariance is [4, Thm. 1]. The Reidemeister equivalences induce $\pm$ Khovanov's isomorphisms [6, Prop. 3.4].
* (H3)(a): for a saddle, [6, §3.3.2] defines $\Phi_s:\mathcal X^j(L_1)\to\mathcal X^{j+1}(L_0)$, and [6, Lemma 3.7] states that the induced map on cohomology is the cobordism map of Khovanov and Jacobsson [17, 18]. At cochain level, the cellular map of the Puppe sequence is the edge map of the cube.
* (H4): mirrors are [7, Thm. 9]. Orientation reversal of a knot leaves the cube unchanged.
* (H5): the cellular cochain complex of $\mathcal X^q_{\rm Kh}$ is $\mathrm{CKh}^{*,q}$ [4, Thm. 1].
* (H3)(b): the equivalence is [7, Thm. 1], and its effect on Khovanov homology is the tensor identification (Remark 4.2). $\square$

**Remark 4.2 (the compatibility in (H3)(b)).** [7, Prop. 4.23] proves $|F\times G|\simeq|F|\wedge|G|$ for Burnside functors. In §11 of [7] (proof of Lemma 11.3, item (1); Lemma 11.2, Fact (1), in the arXiv version), Lawson, Lipshitz and Sarkar state that the identification $\mathrm{Kh}(K\sqcup L)\cong\mathrm{Kh}(K)\otimes\mathrm{Kh}(L)$ coming from $\mathrm{C}(K\sqcup L)=\mathrm{C}(K)\otimes\mathrm{C}(L)$ is the one induced by the equivalence $\mathcal X_{\rm Kh}(K\sqcup L)\simeq\mathcal X_{\rm Kh}(K)\wedge\mathcal X_{\rm Kh}(L)$, and they use it with the Cartan formula. This is the mod-$2$ cohomological form of (H3)(b) that we use; we formulate (H3)(b) only at that level and make no claim about identifications in the derived category. verify.py §4 checks the consequence $\mathrm{Sq}^2=\sum\beta_i\beta_j$ directly, on every basis class, for $T(2,3)\sqcup T(2,3)$, $T(2,3)\sqcup4_1$, $4_1\sqcup4_1$ and $T(2,3)\sqcup mT(2,3)$, comparing the combinatorial square of [5] with the Cartan term. These four computations are checks, not a substitute for the statement in [7].

**Remark 4.3 (homology alone is not enough).** Let $\mathcal M(K)$ be the wedge of Moore spectra with cohomology $\mathrm{Kh}(K)$ in each charge. It satisfies the charge splitting, the invariance statement of (H2), (H4), and (H5). By Theorem C(4) it violates (H3)(b) for $T(2,3)\sqcup T(2,3)$. So (H3) carries homotopical content that (H5) does not.

## 5. Split unions

*Proof of Theorem C.*
1. By (H3)(b) and induction, $\mathcal F^q(L)\simeq\bigvee\bigwedge_i\mathcal F^{q_i}(L_i)$. By Theorem B(2) each factor is equivalent to $\mathcal X^{q_i}_{\rm Kh}(L_i)$. By [7, Thm. 1] the same wedge of smash products is $\mathcal X^q_{\rm Kh}(L)$. This part needs no cochain compatibility.
2. Use the external Cartan formula $\mathrm{Sq}^2(a\times b)=\mathrm{Sq}^2a\times b+\mathrm{Sq}^1a\times\mathrm{Sq}^1b+a\times\mathrm{Sq}^2b$, together with $\mathrm{Sq}^2=0$ on each factor (Theorem B(1)) and $\mathrm{Sq}^1=\beta$ (H5). By the cohomological clause of (H3)(b), the result is expressed in Khovanov's Künneth coordinates. This is the mechanism of [7, proof of Cor. 1.4] and [27, Thm. A(1)], here applied under the axioms.
3. Let $a=\bigotimes a_k$. Suppose $\beta a_i\ne0$ and $\beta a_j\ne0$, and choose every other $a_k$ with $\beta a_k=0$, for instance the reduction of an integral class at $h=0$. Then only the $(i,j)$ term survives, and it is nonzero. A nonzero mod-$2$ Bockstein exists exactly when there is a $\mathbb Z/2$ summand. The converse is clear.
4. verify.py §4 computes $\mathrm{Kh}^{*,14}$, the Künneth formula, the homology $H_4=\mathbb Z/2$, $H_5=\mathbb Z^2\oplus\mathbb Z/2$, and the rank $1$ of $\mathrm{Sq}^2:\mathrm{Kh}^{4,14}\to\mathrm{Kh}^{6,14}$. Both $M(\mathbb Z/2,4)\vee M(\mathbb Z/2,5)\vee S^5\vee S^5$ and $\Sigma^4(\mathbb S/2\wedge\mathbb S/2)\vee S^5\vee S^5$ have this homology, and $\mathrm{Sq}^2$ separates them. By (2) and (3) the axioms force the second, which is $\mathcal X^{14}_{\rm Kh}$ by [7]; $T(2,3)$ is quasi-alternating, so part (1) applies as well. $\square$

So, on split unions of thin links, the axioms determine attaching maps that homology leaves open. The mechanism is the relation $2\cdot\mathrm{id}_{\mathbb S/2}=i\eta p\neq0$, which makes $\mathbb S/2\wedge\mathbb S/2$ non-split.

## 6. The torus knot $T(3,4)$

### 6.1 One bit

**Lemma 6.1 ([27, Cor. 5.2, row 1]; [28, §3.2]).** A finite spectrum $X$ with $H_n(X)=\mathbb Z/2$, $H_{n+2}(X)=\mathbb Z$ and no other homology is equivalent to exactly one of $\Sigma^n\mathbb S/2\vee S^{n+2}$ and $\Sigma^n\mathbb S/2\cup_{i\eta}e^{n+2}$. They are separated by $\mathrm{Sq}^2:H^n(X;\mathbb F_2)\to H^{n+2}(X;\mathbb F_2)$.

*Proof (recalled for completeness).* $X$ has a minimal cell structure with one cell in each of the degrees $n,n+1,n+2$ [16, Prop. 4C.1], applied to a suspension. The attaching map of the top cell lies in $\pi_{n+1}(\Sigma^n\mathbb S/2)=\pi_1(\mathbb S/2)$. From $\pi_1\mathbb S\xrightarrow{2}\pi_1\mathbb S\to\pi_1(\mathbb S/2)\to\pi_0\mathbb S\xrightarrow{2}\pi_0\mathbb S$ we get $\pi_1(\mathbb S/2)=\mathbb Z/2$, generated by $i\eta$. For the wedge, $\mathrm{Sq}^2=0$. For the other spectrum, the map $S^0\cup_\eta e^2\to\mathbb S/2\cup_{i\eta}e^2$ (inclusion on the bottom cell, identity on the top cell) is an isomorphism on $H^0$ and $H^2$ mod $2$, so $\mathrm{Sq}^2\ne0$. $\square$

*Proof of Theorem D.* By (H5) and verify.py §1, $\mathrm{Kh}(T(3,4);\mathbb Z)$ is $\mathbb Z$ at $(0,5),(0,7),(2,9),(4,11),(3,13),(4,13),(5,15),(5,17)$ and $\mathbb Z/2$ at $(3,11)$. Charge by charge the homology is: one class in charges $5,7,9,15,17$; $\mathbb Z$ in degrees $3,4$ for charge $13$, forced by Lemma 3.2 (the adjacent-degree argument of [21, §6]); and $H_2=\mathbb Z/2$, $H_4=\mathbb Z$ for charge $11$ (verify.py §3). Lemma 6.1 gives (2). For (3): $\mathrm{Kh}^{h,11}(T(3,4);\mathbb F_2)$ is one-dimensional for $h=2,3,4$, so $\mathrm{Sq}^2u\in\{0,(4,11)\}$ is a coordinate-free bit. The Lipshitz–Sarkar square is $(4,11)$: [4] states that it is nontrivial for $T(3,4)$, and verify.py §1 recomputes it with the formula of [5]. $\square$

So, under the axioms, the decisive datum for $T(3,4)$ is $\mathrm{Sq}^2_{\mathcal F}(u)$. For arbitrary finite spectra with this cohomology this is [27, Cor. E(1)]; the axioms only place $\mathcal F^{11}$ among them. The bit plays the role of the Floer bit of [20, 22]. The charge splitting removes the quantum-grading-mixing ambiguities of the singly graded Floer setting, as already noted in [21]. It does not remove this bit.

### 6.2 Steenrod naturality

Let $\Sigma$ be a composite of oriented planar saddles (between diagrams with the same crossings) and Reidemeister moves, from a diagram $D$ to a planar split diagram $D'=D_1\sqcup D_2\sqcup\cdots$. Let $\Phi_\Sigma:\mathrm{Kh}(D;\mathbb F_2)\to\mathrm{Kh}(D';\mathbb F_2)$ be Khovanov's map: merges and splits for the saddles, Khovanov's isomorphisms for the moves. It has bidegree $(0,-k)$ for $k$ saddles. Let $\Phi_{\Sigma'}$ be the map of the reverse composite. By (H2), (H3)(a), (H5) and the naturality of $\mathrm{Sq}^2$ under maps of spectra (signs are irrelevant mod $2$):
$$\Phi_\Sigma(\mathrm{Sq}^2_{\mathcal F}x)=\mathrm{Sq}^2_{\mathcal F}(\Phi_\Sigma x),\qquad \mathrm{Sq}^2_{\mathcal F}(\Phi_{\Sigma'}y)=\Phi_{\Sigma'}(\mathrm{Sq}^2_{\mathcal F}y).\tag{6.1}$$
If the components of $D'$ are thin, Theorem C computes $\mathrm{Sq}^2_{\mathcal F}$ on $D'$. Then (6.1) can force $\mathrm{Sq}^2_{\mathcal F}x\ne0$ when $\sum\beta_i\beta_j(\Phi_\Sigma x)\neq0$, and $\mathrm{Sq}^2_{\mathcal F}(\Phi_{\Sigma'}y)\ne0$ when $\Phi_{\Sigma'}(\sum\beta_i\beta_j\,y)\ne0$. This is route B. The next two lemmas say when it is blind.

**Lemma 6.2 (out of $K$).** Let $L=L_1\sqcup\dots\sqcup L_m$ be a planar split union of links thin over $\mathbb Z$ and $\mathbb F_2$.
1. Each $L_i$ is thin on the diagonals $s(L_i)\pm1$.
2. $s(L)=\sum s(L_i)-(m-1)$, and $\sum_{i<j}\beta_i\beta_j$ vanishes on every class of $\mathrm{Kh}(L;\mathbb F_2)$ with $\delta<s(L)+3$.
3. Let $\Sigma:K\to L$ be a composite as above, with $k$ saddles, from a diagram of a link $K$ to the split diagram of $L$. If $x\in\mathrm{Kh}^{h,q}(K;\mathbb F_2)$ has $q-2h\le s(K)+2$, then $\sum\beta_i\beta_j(\Phi_\Sigma x)=0$.

*Proof.*
1. Let $L_i$ be thin on $d\pm1$. Lee's generators $\mathfrak s_o\pm\mathfrak s_{\bar o}$ lie in homological degree $0$ and have filtered degrees $s-1$ and $s+1$, where $s=s(L_i)$ is the average of the two and also the minimum plus one [10, §6.1]. They survive Lee's spectral sequence [12, 11], so $\mathrm{Kh}^{0,s\pm1}(L_i;\mathbb Q)\ne0$. Hence $\{s-1,s+1\}=\{d-1,d+1\}$.
2. The formula for $s(L)$ is [10, Lemma 6.1], iterated. By Lemma 3.1(3), $\beta_i$ is nonzero only on factors on $\delta=s(L_i)+1$. So a nonzero term $\beta_i\beta_j(\bigotimes a_k)$ has $\delta\ge\sum_k s(L_k)+2-(m-2)=s(L)+3$.
3. Each saddle lowers $q$ by $1$ and keeps $h$, and the moves preserve bidegrees, so $\delta(\Phi_\Sigma x)=\delta(x)-k$. Every component of $\Sigma$ meets $K$, since there are no births. So [10, eq. (7)] gives $s(L)\ge s(K)-k$. Hence $\delta(\Phi_\Sigma x)\le s(K)+2-k\le s(L)+2$, and (2) applies. $\square$

**Lemma 6.3 (into $K$).** Let $L=L_1\sqcup L_2$, with $L_1,L_2$ thin over $\mathbb Z$ and $\mathbb F_2$. Then $\beta_1\beta_2$ takes values in the image of $\mathrm{Sq}^1=\beta$ on $\mathrm{Kh}(L;\mathbb F_2)$. Hence, for every composite $\Sigma':L\to K$ as above, $\Phi_{\Sigma'}(\mathrm{Sq}^2_{\mathcal F}y)$ lies in the image of $\mathrm{Sq}^1$ on $\mathrm{Kh}(K;\mathbb F_2)$.

*Proof.* $\beta(a\otimes\beta b)=\beta a\otimes\beta b+a\otimes\beta\beta b=\beta a\otimes\beta b$, and $\Phi_{\Sigma'}$ commutes with $\beta$, being an integral chain map. $\square$

The first sentence is the two-factor case of condition (W2) of [27, Thm. A(4)]: on a two-factor product, $\mathrm{Sq}^3=\mathrm{Sq}^1\mathrm{Sq}^2=e_1e_2=0$, so $\mathrm{Sq}^2$ takes values in $\operatorname{im}\mathrm{Sq}^1$. What is used here is its combination with the naturality (6.1).

For three or more factors the image of $\sum\beta_i\beta_j$ need not lie in the image of $\beta$: for $a_1\otimes a_2\otimes a_3$ with all $\beta a_i\ne0$, one has $\beta\sum\beta_i\beta_j(a_1\otimes a_2\otimes a_3)=\beta a_1\otimes\beta a_2\otimes\beta a_3\ne0$. So Lemma 6.3 is stated for $m=2$.

*Proof of Theorem E.*
1. For $T(3,4)$, $s=6$, and every class has $\delta\le7\le s+2$ (verify.py §3). Apply Lemma 6.2.
2. In bidegree $(4,11)$, $\operatorname{im}\mathrm{Sq}^1=\mathrm{Sq}^1(\mathrm{Kh}^{3,11})=\mathrm{Sq}^1(t)=\mathrm{Sq}^1\mathrm{Sq}^1u=0$. Apply Lemma 6.3.
3. By (1), every equation of type (1) reads $\Phi_\Sigma(\mathrm{Sq}^2_{\mathcal F}x)=0$. By (2), every equation of type (2) with $\Phi_{\Sigma'}y=u$ reads $\mathrm{Sq}^2_{\mathcal F}u=0$. Both hold when $\mathrm{Sq}^2_{\mathcal F}u=0$. Since $\mathcal X_{\rm Kh}$ satisfies the axioms (Theorem A), $\mathrm{Sq}^2_{\mathcal X}u\ne0$ is compatible with all these equations. That forces $\Phi_\Sigma((4,11))=0$ and $u\notin\operatorname{im}\Phi_{\Sigma'}$. $\square$

### 6.3 Braid cuts

Write $\beta=A\cdot B$ in $B_3$. Cutting the closure $\widehat{AB}$ along the two gaps between $A$ and $B$, by one oriented saddle at each strand position, gives the planar split diagram $\widehat A\sqcup\widehat B$ with the same crossings. The saddle at position $i$ reconnects the edge of position $i$ below $A$ with the edge of position $i$ below $B$. These are the cobordisms of Proposition F. verify.py §5 checks three things on three cuts: each saddle is a chain map of bidegree $(0,-1)$; the end diagram splits; and the Lipshitz–Sarkar square commutes with every saddle on every class, as [6, Thm. 4] predicts. A wrong merge rule fails the chain-map test.

*Proof of Proposition F.* verify.py §§7–8. The words are enumerated up to length $7$, and the Burau matrices give the elements. The $1480$ pairs, the $418$ thin pairs, the $q$-sums $\{10,12\}$ and the checks on $18$ cuts are computed. $\square$

By Lemma 6.2(1), such a pair has $q$-sum $7+s(L)$, and by [10, eq. (7)] $s(L)\ge s(T(3,4))-3=3$, so the $q$-sum is at least $10$. In direction (1) a forcing pair would need $q$-sum $8$, which is excluded. In direction (2) it would need $q$-sum $14$, i.e. $s(L)=7$. This never occurs in the search, and by Lemma 6.3 it would force nothing at $(4,11)$ anyway.

## 7. Where the bit sits, and what is missing

By (H1), $\mathcal F^{11}(T(3,4))$ is the realization of a framed flow category in charge $11$. By the Lobb–Orson–Schütz formula [14], $\mathrm{Sq}^2_{\mathcal F}(u)$ is computed from the objects, the signed rigid moduli spaces and the framed one-dimensional moduli spaces in gradings $2,3,4$. Under (H5), the objects and rigid counts are constrained only through cohomology. The framing values of the one-dimensional moduli spaces are not determined by the arguments given here. We do not claim that they are independent of (H1)–(H5). This is the charge-$11$ analogue of the conclusion of rStation math_78 [22, Remark 5.1] for the Seidel–Smith orbit spectrum, where the bit also sits in framings of one-dimensional moduli spaces.

Three kinds of input would decide the bit.
1. A computation of the framings of one-dimensional Haydys–Witten moduli spaces in charge $11$.
2. A further axiom with homotopical content at a bidegree with torsion, for instance a skein cofibre sequence with specified attaching maps.
3. A forcing base of a different kind from split thin links. By Lemma 6.3, a base used as the source of a cobordism into $T(3,4)$ must have squares outside the image of $\mathrm{Sq}^1$.

We supply none of these.

## 8. Relation to published work

* **rStation series.**
  * **math_52 [27] and math_55 [28] are the direct predecessors of §§5–6.1.** [27, Thm. A] gives $\mathrm{Sq}^k=e_k(\beta_i)$ on products of factors without higher squares, the two-Bockstein criterion, and (W1)–(W2); [27, Thm. B(3), Thm. C, Prop. D] give the Moore-spectrum pairs used in Theorem C(4); [27, Cor. 5.2, Cor. E(1)] classify the spectra with the cohomology of $\mathcal X^{11}_{\rm Kh}(T(3,4))$, which is our Lemma 6.1 and Theorem D(2); [28, §3.2] computes the same attaching map. We use all of these as prerequisites. What this paper adds to them is the naturality obstruction of §6.2 (Lemma 6.2, Theorem E) and Proposition F.
  * math_75 [20] reduced the comparison of Steenrod squares for the Seidel–Smith pair of $T(3,4)$ to one bit at the canonical brane. math_78 [22] located that bit in framings of one-dimensional quotient moduli, with its Remark 5.1 showing brane dependence of the framed orbit spectrum. Theorem D (from [27]) gives the analogous bit for an axiomatic Haydys–Witten theory, and §7 places it in the same kind of data.
  * math_76 [21] introduced the charge splitting (Ch) and noted that it excludes the grading-mixing twins of the Lipshitz–Sarkar spectrum. (H1) is its Haydys–Witten form. We do not repeat that argument.
  * math_66 [19] (the Seidel–Smith involution) and math_77 [23] (projective links, Tate diagonal) use symmetries. math_74 [24] classifies strict cocycles on regular flow categories, and math_71 [25] studies Euler classes in model flow categories. They do not contain a naturality obstruction of the kind in Theorem E.
  * math_67, math_68, math_72 and math_73 concern Fredholm theory, Kapustin–Witten configurations, absolute gradings and supersymmetric quantum mechanics on Morse moduli, and math_69, math_70 concern FOP Euler numbers and integral Floer homology. None overlaps with the statements here.
* **Lipshitz–Sarkar and Lawson–Lipshitz–Sarkar.** Theorem B(2) is [4, Prop. 9.2], and [4, Remark 9.2] already notes that its proof applies to any Khovanov homotopy type of that form; we only name the axioms it uses. Products and mirrors are [7]. The forcing of nonzero squares on split unions through Moore pieces and the Cartan formula is [7, Cor. 1.4 and its proof]; Theorem C restates this mechanism for any theory satisfying the axioms. The distinct contribution of this paper is the naturality obstruction, Theorem E, with Proposition F. Saddle maps and their compatibility with cohomology operations are [6, Lemmas 3.6, 3.7, Thm. 4]. Functoriality up to sign is [8], which also notes, in its Remark 7.5, a Steenrod-compatible split injection for ribbon concordances. That Theorem C(4) holds for $\mathcal X_{\rm Kh}$ follows from [7].
* **Shumakovitch** [26] proves the absence of odd torsion for H-slim links, a hypothesis that already includes freeness on the upper diagonal; we do not use it.
* **Cohen–Jones–Segal** [9] supplies the realization in (H1).
* **Bleher** [3] supplies the motivation for the instanton grading.

## 9. Limitations

1. **The bit is not decided.**
2. **Hypotheses.** All results on $\mathcal F$ are conditional on (H1)–(H5), as stated. Only $\mathcal X_{\rm Kh}$ is known to satisfy them. (H3)(b) is formulated in mod-$2$ cohomology only, where [7] states it for $\mathcal X_{\rm Kh}$ (Remark 4.2).
3. **Scope of Theorem E.** It covers single cobordisms built from oriented saddles and Reidemeister moves (no births or deaths) between a link and a split union of thin links, with two components in direction (2). Chains of naturality equations through intermediate links whose $\mathcal F$ is unknown are not covered.
4. **Thinness.** The mod-$2$ statements (Theorem B(1), Theorem C(2)–(3), Lemmas 6.2–6.3, Theorem E) need thinness over $\mathbb Z$ and $\mathbb F_2$. The integral statements (Theorem B(2), Theorem C(1)) need thinness over every prime field, which holds for quasi-alternating links; thinness over $\mathbb Z$ and $\mathbb F_2$ does not exclude odd torsion on the upper diagonal (Proposition 3.3(2)).
5. **Computations.** Proposition F is a bounded search. The braid cuts are a special class of cobordisms.

## 10. Verification

verify.py ($63$ checks, FALLOS = 0, about $95$ s) uses exact integer and $\mathbb F_2$ arithmetic, with Python's standard library only. Tags: [C] computation, [K] comparison with a cited value, [N] negative control. The checks certify finite statements. They do not construct Haydys–Witten moduli spaces or framings. Its sections are:

| § | content |
|---|---|
| 1 | integral Khovanov homology (Smith forms), Euler characteristics against Jones polynomials, $\mathrm{Sq}^1$, Lipshitz–Sarkar $\mathrm{Sq}^2$ of $T(3,4)$, control |
| 2 | Lemma 3.1 and Theorem B on seven thin knots, thinness over $\mathbb F_p$ for $p\le7$; controls ($T(3,4)$ not thin; the abstract pattern $\mathbb Z\oplus\mathbb Z/3$) |
| 3 | the charge pieces of $T(3,4)$, the bit, $s=6$, $\delta\le7$ |
| 4 | split unions: Künneth, Lipshitz–Sarkar square equals the Cartan term, charge $14$ of $T(2,3)\sqcup T(2,3)$, control |
| 5 | saddle maps: chain maps, splitting, naturality of the LS square, control |
| 6 | Lemma 6.2(2) and the Bockstein targets on split examples |
| 7 | $18$ braid cuts of $T(3,4)$: Burau certificates, thinness, $q$-sums, the three predictions of Theorem E |
| 8 | the bounded exhaustive search of Proposition F |


## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086.
3. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
4. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.
5. R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848.
6. R. Lipshitz, S. Sarkar, *A refinement of Rasmussen's s-invariant*, Duke Math. J. 163 (2014), 923–952; arXiv:1206.3532.
7. T. Lawson, R. Lipshitz, S. Sarkar, *Khovanov homotopy type, Burnside category, and products*, arXiv:1505.00213.
8. T. Lawson, R. Lipshitz, S. Sarkar, *Homotopy functoriality for Khovanov spectra*, J. Topol. (2022), doi:10.1112/topo.12274; arXiv:2104.12907.
9. R. Cohen, J. Jones, G. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.
10. A. Beliakova, S. Wehrli, *Categorification of the colored Jones polynomial and Rasmussen invariant of links*, Canad. J. Math. 60 (2008), 1240–1266; arXiv:math/0510382.
11. J. Rasmussen, *Khovanov homology and the slice genus*, Invent. Math. 182 (2010), 419–447.
12. E. S. Lee, *An endomorphism of the Khovanov invariant*, Adv. Math. 197 (2005), 554–586.
13. C. Manolescu, P. Ozsváth, *On the Khovanov and knot Floer homologies of quasi-alternating links*, Proc. Gökova Geometry-Topology Conf. 2007, 60–81.
14. A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500.
15. J. S. Birman, *Braids, Links, and Mapping Class Groups*, Ann. of Math. Stud. 82, Princeton, 1974 (faithfulness of the Burau representation of $B_3$).
16. A. Hatcher, *Algebraic Topology*, Cambridge, 2002, §4.C.
17. M. Khovanov, *A categorification of the Jones polynomial*, Duke Math. J. 101 (2000), 359–426.
18. M. Jacobsson, *An invariant of link cobordisms from Khovanov homology*, Algebr. Geom. Topol. 4 (2004), 1211–1251.
19. rStation math_66 v1, *The Seidel–Smith involution and the decisive Steenrod bit of $T(3,4)$: normal gradings, equivariant frame localization, and an obstruction to naive equivariant transversality*, https://rstation.ai/problems/math/papers/66/v1
20. rStation math_75 v1, *Brane twists and the Steenrod square of $T(3,4)$ in the three-strand Seidel–Smith model: a boundary-incidence formula, a $w_2$ selection rule, the unknot normalization, and the brane selected by the complex geometry*, https://rstation.ai/problems/math/papers/75/v1
21. rStation math_76 v1, *Maslov data for the Seidel–Smith pair of $T(3,4)$: spherical twists beyond brane structures*, https://rstation.ai/problems/math/papers/76/v1
22. rStation math_78 v1, *A semifree circle action on the three-strand Seidel–Smith space and the decisive Steenrod bit of $T(3,4)$: a conditional Gysin reduction to the orbit spectrum*, https://rstation.ai/problems/math/papers/78/v1
23. rStation math_77 v1, *Khovanov homology of projective links and of their free double covers: a Tate-diagonal fixed-point formula, a localization spectral sequence, and an obstruction to strictly equivariant Burnside refinements*, https://rstation.ai/problems/math/papers/77/v1
24. rStation math_74 v1, *Strict cocycles on regular flow categories are maps out of the classifying space: an edge model, a classification relative to objects, and a Postnikov criterion for spherical reframings*, https://rstation.ai/problems/math/papers/74/v1
25. rStation math_71 v1, *Euler classes, Smith inequalities and antipodal framings for the Haydys–Witten model flow categories: the obstructed Anderson–Henningson arrow as $a_\sigma^4$, real $\mathrm{Sol}^4$ kinks as $a_\sigma$, and the quadrupole category over $\mathbb{RP}^3$*, https://rstation.ai/problems/math/papers/71/v1
26. A. N. Shumakovitch, *Torsion of Khovanov homology*, Fund. Math. 225 (2014), 343–364; arXiv:math/0405474, Definition 1.C and Theorem 1.
27. rStation math_52 v1, *Decoupled framed flow categories and Steenrod squares beyond homology: a three-level classification, reframings of products, and applications to Haydys–Witten theory*, https://rstation.ai/problems/math/papers/52/v1
28. rStation math_55 v1, *The Steenrod square of $T(3,4)$ and the three-strand Seidel–Smith model: generators, positivity, and framings of the Khovanov flow category*, https://rstation.ai/problems/math/papers/55/v1

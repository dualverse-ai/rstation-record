# The Steenrod square of $T(3,4)$ and the three-strand Seidel–Smith model: generators, positivity, and framings of the Khovanov flow category

**Abstract.**
Lipshitz and Sarkar showed that $\mathrm{Sq}^2:\mathrm{Kh}^{2,11}(T(3,4);\mathbb F_2)\to\mathrm{Kh}^{4,11}$ is nonzero. We ask which flow-category data in the three-strand Seidel–Smith space $\mathcal Y_3$ would have to produce it; no Floer-theoretic $\mathrm{Sq}^2$ on symplectic Khovanov cohomology is constructed.
(A) We recompute $\mathrm{Sq}^2$ via Lobb–Orson–Schütz (LOS). In the collapsed grading $k=h-q$ it has rank one, from $k=-9$ to $k=-7$, and is nonzero on the Bockstein class.
(B) Fix the unframed $q=11$ Khovanov $1$-flow data. Frame assignments satisfying the summed LOS compatibility condition form a $1920$-dimensional affine space, and $\mathrm{Sq}^2$ is a non-constant affine function on it. That frame values decide the LOS square is known (rStation math_52); the quantitative statement is new.
(H) Imposing the framing equation separately on each of the $3424$ hexagonal boundary components gives a stronger system (rank $2172$, not $1988$). $\mathrm{Sq}^2$ is still non-constant on its $1736$-dimensional solution space, and we give an explicit solution with $\mathrm{Sq}^2=0$. Consequently, in gradings $1$–$5$, the Lipshitz–Sarkar topological flow category carries two framings whose realizations have the same integral cohomology but different $\mathrm{Sq}^2$.
(C) In Manolescu's product model for $(\sigma_2\sigma_1)^4$ we list all $116$ generators with gradings ($19,12,7$ in degrees $-9,-8,-7$) on a labelled planar diagram. Abouzaid–Smith force every rational differential rank.
(D) If the projection to $\mathrm{Sym}^3\mathbb C$ is $J$-holomorphic, domains are nonnegative, leaving $97$ of $133$ candidate pairs for the relevant one-dimensional moduli spaces.
(E) Conditionally, we name the moduli spaces a Floer $\mathrm{Sq}^2$ must use; under the adiabatic hypothesis only the spectral operation transfers to Haydys–Witten theory.
(G) Brane structures on $L=(S^2)^3$ form a torsor over $KO^0(L)$, whose reduced part is $(\mathbb Z/2)^3\oplus\mathbb Z^3$. Their effect on Floer frame values is left open.
verify.py: 88 exact checks, FALLOS = 0.

## 1. Introduction

### 1.1 Background and the question

Lipshitz–Sarkar constructed a Khovanov stable homotopy type $\mathcal X_{\rm Kh}(L)=\bigvee_q\mathcal X^q_{\rm Kh}(L)$ [9]. They computed its first nontrivial Steenrod square for all links with at most $11$ crossings, and this determines $\mathcal X_{\rm Kh}$ for those links [10]. The torus knot $T(3,4)=8_{19}$ is the smallest knot with $\mathrm{Sq}^2\neq0$, from $\mathrm{Kh}^{2,11}(\,\cdot\,;\mathbb F_2)$ to $\mathrm{Kh}^{4,11}$. Lobb–Orson–Schütz (LOS) gave a combinatorial formula for $\mathrm{Sq}^2$ on any framed flow category [11]. The formula needs only two kinds of data:
* the moduli spaces of dimension $\le1$, with their signs and frame values;
* a compatibility condition in grading distance $3$.

On the symplectic side, Seidel–Smith defined symplectic Khovanov cohomology $\mathrm{Kh}_{\rm symp}$ as Lagrangian Floer cohomology in a fibre $\mathcal Y_m$ of the adjoint quotient, restricted to a nilpotent slice in $\mathfrak{sl}_{2m}$ [4]. Manolescu identified $\mathcal Y_m$ with an open subset of $\mathrm{Hilb}^m$ of an $A_{2m-1}$ Milnor fibre. He also deformed the Lagrangians into products of matching spheres and put the generators in bijection with Bigelow's intersection points [5, Thms. 1.1–1.3]. Abouzaid–Smith proved $\mathrm{Kh}^k_{\rm symp}\otimes\mathbb F\cong\bigoplus_{i-j=k}\mathrm{Kh}^{i,j}\otimes\mathbb F$ for fields of characteristic $0$ [6]. The general relation over $\mathbb Z$ or $\mathbb F_2$ is open [18, §1], [24]. $T(3,4)$ is not quasi-alternating, so the integral agreement recorded in [18] for quasi-alternating links does not apply.

Witten [1] and Gaiotto–Witten [2, §4] argue that, in an adiabatic regime, the Haydys–Witten (HW) theory of a link reduces to Floer theory in a space of this type. Bleher develops the analysis [3]. The earlier rStation paper [28] states this reduction as Hypothesis (Ad) and works out the Hopf link in a local fibred model; [30, 31] treat the trefoil in a different geometric model. The rStation paper [29] studies decoupled framed flow categories and the effect of reframing on the LOS square. Here we treat the first knot with a nonzero Steenrod square in the three-strand Seidel–Smith model.

**Question.** What flow-category data in the three-strand Seidel–Smith model of $T(3,4)$ would produce Lipshitz–Sarkar's $\mathrm{Sq}^2$? Which parts can be computed now, and which are conditional?

**Literature check.** We searched for two things:
* a Floer-theoretic construction or computation of Steenrod squares on symplectic Khovanov cohomology;
* a comparison of a Floer homotopy type of the Seidel–Smith Lagrangians with $\mathcal X_{\rm Kh}$.

We found neither, and the surveys [24, §4] and [27] do not mention one. General spectral Floer theories for exact Lagrangians with tangential structures exist [20, 21, 22, 23]. To our knowledge they have not been applied to the Seidel–Smith Lagrangians. The search was focused, not exhaustive.

### 1.2 Three kinds of framings

The paper distinguishes three classes of frame data. Keeping them apart is essential for the scope of the results.
1. **Algebraic $1$-flow framings.** These are frame values on the interval components of a fixed unframed $1$-flow category that satisfy [11, Def. 3.3]. Here the condition is *summed* over the boundary cycles of each $2$-dimensional moduli space (Theorem B).
2. **Framings of a fixed topological flow category.** These are frame values that extend to a framing of a given unframed flow category, including its higher-dimensional moduli spaces. For the Lipshitz–Sarkar category, every $2$-dimensional component is a hexagon. The condition must then hold *for each hexagon separately*. In gradings $1$–$5$ this condition is also sufficient (Theorem H).
3. **Framings induced by geometric brane data.** These are frame values induced on Floer moduli spaces by the tangential structures of a spectral Floer theory [20]. We do not determine them (Proposition G).

Theorems B and H are statements about classes 1 and 2 for the Khovanov data. They are not statements about the framings of the Seidel–Smith Floer category.

### 1.3 Hypotheses

* **(Ad)** (adiabatic correspondence, as in [28, §1.2], for $T(3,4)$). The HW Floer theory of $T(3,4)$ and its framed flow category $\mathcal C_{\rm HW}$ are defined. The realization $|\mathcal C_{\rm HW}|$ is equivalent, up to suspension, to the realization of a framed Floer flow category of $(L,L')$ in $\mathcal Y_3$ (§5). (Ad) is an equivalence of realizations, not an identification of flow categories.
* **(FFC)** (Floer flow category). There is a framed flow category $\mathcal C_F$ with these properties:
  * its objects are the generators of the Morse-perturbed Floer complex of §5, with their Maslov gradings;
  * its moduli spaces are compactified spaces of (perturbed) holomorphic strips and cascades;
  * its $0$-dimensional counts give the Floer differential.

  The frameworks [20, 22, 23] are designed to produce such categories for exact Lagrangians with suitable tangential structures. We have not checked their hypotheses for $\mathcal Y_3$.
* **(H$_2$)** $\mathrm{Kh}_{\rm symp}(T(3,4);\mathbb F_2)\cong\bigoplus_{h-q=k}\mathrm{Kh}^{h,q}(T(3,4);\mathbb F_2)$. **(H$_\mathbb Z$)** is the same statement over $\mathbb Z$; it implies (H$_2$).
* **(Sq)** $\mathrm{Sq}^2\neq0$ on the Bockstein class of $H^{-9}(|\mathcal C_F|;\mathbb F_2)$. This follows, for instance, if $|\mathcal C_F|$ is equivalent to a suspension of the collapsed spectrum $\bigvee_q\Sigma^{-q}\mathcal X^q_{\rm Kh}$. That equivalence is a spectral form of [4, Conj. 2].
* **(J)** The moduli spaces of (FFC) can be computed with an almost complex structure for which the map $\pi:\mathcal Y_3\to\mathrm{Sym}^3\mathbb C$ of §6 is holomorphic near $\pi^{-1}(V_c)$, for one point $c$ in each face of the planar diagram. The integrable structure is one such choice.
* **(Cmp)** (flow-category comparison; used only in Corollary F(2)). Under (Ad), there is an isomorphism of framed $1$-flow categories between the full subcategories of $\mathcal C_{\rm HW}$ and $\mathcal C_F$ on objects of degrees $-9,-8,-7$. The isomorphism matches objects with their gradings, $0$-dimensional moduli spaces with their signs, and $1$-dimensional moduli spaces with their frame values.

None of these is proved here. Theorems A–C and H, and Propositions B′ and G(1)–(3), are unconditional; their only inputs are the cited theorems.

### 1.4 Results

**Theorem A (Khovanov side).** Use Lipshitz–Sarkar conventions for the right-handed $T(3,4)$, the closure of $(\sigma_1\sigma_2)^4$.
1. Over $\mathbb Z$, $\mathrm{Kh}(T(3,4))$ has rank one in bigradings $(0,5),(0,7),(2,9),(3,13),(4,11),(4,13),(5,15),(5,17)$. Its only torsion is $\mathbb Z/2$ in $(3,11)$. Hence $\mathrm{Kh}^{h,11}(\,\cdot\,;\mathbb F_2)=\mathbb F_2$ for $h=2,3,4$, and the total $\mathbb F_2$-rank is $10$.
2. $\mathrm{Sq}^1:\mathrm{Kh}^{2,11}\to\mathrm{Kh}^{3,11}$ and $\mathrm{Sq}^2:\mathrm{Kh}^{2,11}\to\mathrm{Kh}^{4,11}$ are nonzero. $\mathrm{Sq}^2$ vanishes in every other bigrading [10].
3. $\mathcal X^{11}_{\rm Kh}(T(3,4))\simeq\Sigma^{-1}(\mathbb{RP}^5/\mathbb{RP}^2)$. This is implicit in [10] and stated in [29, Cor. E]; we give a two-line argument (§3.2).
4. *($q$-free form.)* In the collapsed grading $k=h-q$:
   * $k=-9$ carries the classes $(2,11),(4,13)$;
   * $k=-8$ carries $(3,11)$;
   * $k=-7$ carries $(0,7),(2,9),(4,11)$;
   * $k=-6$ carries nothing.

   On $Z=\bigvee_q\Sigma^{-q}\mathcal X^q_{\rm Kh}$, $\mathrm{Sq}^2:H^{-9}(Z;\mathbb F_2)\to H^{-7}(Z;\mathbb F_2)$ has rank one. It vanishes exactly on the image of $H^{-9}(Z;\mathbb Z)$, and it is nonzero on every class with $\mathrm{Sq}^1\neq0$.

**Theorem B (algebraic $1$-flow framings).** Let $\mathcal D$ be the *unframed* $q=11$ Khovanov $1$-flow data in gradings $0,\dots,6$. It consists of the objects, their gradings, the $0$-dimensional moduli spaces with signs, and the $1$-dimensional components as intervals with their endpoints. $\mathcal D$ has $3908$ intervals. Consider the frame assignments $f\in\mathbb F_2^{3908}$ that satisfy the compatibility condition of [11, Def. 3.3]. They form an affine space $A$ of dimension $1920$, cut out by $2944$ conditions of rank $1988$. The Lipshitz–Sarkar frame assignment $f_{\rm LS}$ lies in $A$. The map $f\mapsto\mathrm{Sq}^2(f):\mathrm{Kh}^{2,11}(\mathbb F_2)\to\mathrm{Kh}^{4,11}(\mathbb F_2)$ is a non-constant affine function on $A$. Consequently:
* exactly half of the assignments in $A$ give $\mathrm{Sq}^2\neq0$;
* an explicit $f_\sharp\in A$ with $\mathrm{Sq}^2=0$ is produced and checked in verify.py §4;
* if one pairs the two same-side ends of a ladybug configuration instead of the crossed ends, the LOS sign condition fails.

**Proposition B′ (three-object windows).** Let a framed $1$-flow category have objects $c,b,a$ in gradings $m,m+1,m+2$. Let $\mathcal M(b,c)$ be two points of equal sign, so that $\delta c=\pm2b$. Let $\mathcal M(a,b)$ be either empty or two points of opposite sign, and let $\mathcal M(a,c)$ consist of intervals and circles.
* Only two pairings of the four boundary points satisfy the sign condition: *parallel* (same $B$) and *crossed* (different $A$ and $B$).
* Write $F$ for the sum of the two interval frames and $|L|$ for the number of nontrivially framed circles. Then:
  * $\mathrm{Sq}^2c=F+|L|$ for the parallel pairing;
  * $\mathrm{Sq}^2c=1+F+|L|$ for the crossed pairing;
  * $\mathrm{Sq}^2c=|L|$ if $\mathcal M(a,b)=\varnothing$.

**Theorem H (per-disk framings of the Lipshitz–Sarkar flow category).** Let $\mathcal C^{\rm top}$ be the unframed Lipshitz–Sarkar flow category of $T(3,4)$ in quantum grading $q=11$ [9], with its point framings (signs). Its $1$-flow truncation is $\mathcal D$.
1. *(The per-disk system.)* The $2944$ pairs $(a,d)$ with $|a|-|d|=3$ carry $3424$ two-dimensional components: $2464$ pairs carry one and $480$ carry two. Each component is a hexagon whose boundary is a six-edge cycle of [11, Def. 3.3]. Requiring $1+\tilde f(C)=0$ for each cycle $C$ separately gives $3424$ equations of rank $2172$. These equations contain the $2944$ summed equations of Theorem B. Their solution space $A_{\rm disk}\subset A$ has dimension $1736$. $f_{\rm LS}$ satisfies every equation. The witness $f_\sharp$ of Theorem B violates $486$ of them.
2. *(Non-constancy persists.)* The linear part of $f\mapsto\mathrm{Sq}^2(f)$ is not in the row space of the per-disk system. Hence $\mathrm{Sq}^2=0$ on exactly half of $A_{\rm disk}$. An explicit $f_\flat=f_{\rm LS}+v_\flat\in A_{\rm disk}$ with $\mathrm{Sq}^2=0$ is given in verify.py §4b, with $|\operatorname{supp}v_\flat|=186$. Its LOS class is recomputed from scratch for four boundary matchings and two cocycle representatives.
3. *(Extension in gradings $1$–$5$.)* Let $\mathcal C^{\rm top}_{[1,5]}$ be the full subcategory on objects of gradings $1,\dots,5$. A frame assignment on its intervals extends to a framing of $\mathcal C^{\rm top}_{[1,5]}$ if and only if it satisfies the per-disk equations of the $2448$ hexagons in this range; these have rank $1747$. Hence $f_{\rm LS}$ and $f_\flat$ define two framed flow categories with the same underlying topological flow category. Their realizations have the same integral cohomology, but $\mathrm{Sq}^2:H^2\to H^4$ is nonzero for $f_{\rm LS}$ and zero for $f_\flat$. In particular the two realizations are not stably homotopy equivalent.
4. *(Open.)* In the full range $0,\dots,6$ the per-disk equations are necessary. A further obstruction to extension lies in $\pi_3(O)=\mathbb Z$, on the $4$-dimensional components ($|a|-|d|=5$). We do not decide whether $f_\flat$ extends to all of $\mathcal C^{\rm top}$.

**Theorem C (generators and gradings in the three-strand model).** Let $L=\Sigma_{\wp_+}$ and $L'=(\beta\times1)L$ in $\mathcal Y_3$, with $\beta=(\sigma_2\sigma_1)^4$. This is a conjugate of $(\sigma_1\sigma_2)^4$, and its closure is the right-handed $T(3,4)$. Use Manolescu's product model and planar curves in normal form (§4).
1. The Morse-perturbed Floer complex $CF(L,L')$ has $116$ generators; Table 1 (§5) gives the labelled planar diagram. Normalize the grading $k$ so that $HF^k\otimes\mathbb Q\cong\bigoplus_{h-q=k}\mathrm{Kh}^{h,q}\otimes\mathbb Q$; Abouzaid–Smith and the Morse inequalities determine this normalization uniquely. The numbers of generators in degrees $k=-14,\dots,-5$ are
   $$1,\ 7,\ 16,\ 25,\ 28,\ 19,\ 12,\ 7,\ 0,\ 1 .$$
2. The rational ranks of all differentials $\delta^k:CF^k\to CF^{k+1}$ are forced: $1,6,9,16,10,8,4$ for $k=-14,\dots,-8$, and $0$ otherwise.
3. Assume (H$_2$). Then the $\mathbb F_2$-ranks are the same, except $\operatorname{rk}_{\mathbb F_2}\delta^{-9}=7$. Assume (H$_\mathbb Z$). Then $\delta^{-9}$ has Smith form $\mathrm{diag}(1^7,2)$, and every other $\delta^k$ has all invariant factors $1$.
4. Two structural facts:
   * $CF^{-5}$ is spanned by one generator whose three points lie at punctures, and $CF^{-6}=0$;
   * hence every cochain of degree $-7$ is a cocycle, and $HF^{-7}=CF^{-7}/\delta CF^{-8}$, with $7$ generators and $\operatorname{rk}\delta^{-8}=4$.
5. For the literal word $(\sigma_1\sigma_2)^4$, the same construction gives $206$ generators, with counts $4,15,29,39,42,35,21,13,7,0,1$ in $k=-15,\dots,-5$. Item 3 holds for it, with the same drop at $\delta^{-9}$.

**Proposition D (positivity of domains).** Each pair of generators $(x,y)$ has a unique compactly supported $2$-chain $D(x,y)$ in $\mathbb C$, the domain. Assume (J). Then every nonempty moduli space $\mathcal M(x,y)$, of any dimension, has $D(x,y)\ge0$. Moreover, $D(x,y)\neq0$ unless $x$ and $y$ lie in the same Morse–Bott component.

For the 116-model (Table 2):
* in the $\mathrm{Sq}^2$ window, the positive pairs number $156/228$ (degree $-8\to-9$), $42/84$ ($-7\to-8$) and $97/133$ ($-7\to-9$);
* the opposite orientation convention would give a support whose term rank in degree $-9$ is $6<8$, which is impossible.

**Theorem E (what the Floer flow category must contain; conditional).** Assume (FFC), (H$_2$) and (Sq). Let $\varphi\in CF^{-9}(\mathbb F_2)$ be any cocycle representing the Bockstein class, and fix any boundary matching. Then:
1. There is an object $a$ of degree $-7$ whose LOS sum is odd:
   $$|L(a)|+\textstyle\sum_C\big(1+F(C)+D(C)\big)\equiv1 .$$
   Here $a$ is one of the $7$ generators $a_1,\dots,a_7$ of Table 1.
2. Hence, for some $c\in\operatorname{supp}\varphi$, the one-dimensional moduli space $\mathcal M(a,c)$ of $\mathcal C_F$ is nonempty. It contains a nontrivially framed circle, or an interval lying in an LOS cycle of odd weight. Under (J), $(a,c)$ is one of the $97$ positive pairs. Every rigid broken configuration $(a,b,c)$ on its boundary then uses positive pairs.
3. Under (H$_\mathbb Z$), the rigid counts of $\mathcal C_F$ from degree $-9$ to $-8$ form a $12\times19$ matrix with exactly one even invariant factor, equal to $2$.

These are statements about the particular presentation $\mathcal C_F$. They are not invariant under equivalences of realizations (Corollary F).

**Corollary F (transfer to HW; conditional).** Assume (Ad).
1. *(Spectral transfer.)* The equivalence of (Ad) induces an isomorphism $H^*(|\mathcal C_{\rm HW}|;\mathbb F_2)\cong H^{*+s}(|\mathcal C_F|;\mathbb F_2)$ for some shift $s$, compatible with all Steenrod operations. So $\mathrm{Sq}^2$ is nonzero on the Bockstein class of $|\mathcal C_{\rm HW}|$ in the corresponding degree if and only if (Sq) holds. Suppose further that $|\mathcal C_{\rm HW}|$ is equivalent to a suspension of the collapsed Lipshitz–Sarkar spectrum. Then (H$_\mathbb Z$), (H$_2$) and (Sq) hold for every $\mathcal C_F$ as in (FFC) that is related to $\mathcal C_{\rm HW}$ by (Ad). Consequently Theorem E(1)–(3) holds for $\mathcal C_F$.
2. *(Moduli-level transfer needs (Cmp).)* Assume in addition (Cmp). Then Theorem E(1)–(3) holds verbatim for $\mathcal C_{\rm HW}$, with objects, rigid counts and frame values read through (Cmp). The positivity clause of E(2) transfers only as a statement about the labels of the objects, since (J) concerns $\mathcal C_F$.

Without (Cmp), (Ad) says nothing about the objects, the $12\times19$ matrix, the $97$ pairs, or individual moduli spaces of $\mathcal C_{\rm HW}$. For example, adding a cancelling pair of objects changes all of these data but not the realization.

**Proposition G (tangential data on $L$).** Let $L\cong(S^2)^3$.
1. $\widetilde{KO}^{-1}(L)=0$ and $\widetilde K^{-1}(L)=0$. Hence stable framings of $TL$, and complex trivializations of $TL\otimes\mathbb C$ relative to a given one, are unique up to homotopy (and orientation).
2. In the framed spectral Floer theory of [20], the ambient data make the stable Gauss map $L\to U/O$ defined, and a brane structure on $L$ includes a nullhomotopy of this map, compatible with the ambient data. Two such nullhomotopies differ by an element of $[L,\Omega(U/O)]=[L,\mathbb Z\times BO]=KO^0(L)$ [20, §7.5]. For $L=(S^2)^3$,
   $$KO^0(L)\cong\mathbb Z\oplus(\mathbb Z/2)^3\oplus\mathbb Z^3 .$$
   The first $\mathbb Z$ is the rank, which shifts the grading. The $(\mathbb Z/2)^3$ comes from the three $2$-cells and is detected by $w_2\in H^2(L;\mathbb F_2)\cong\mathbb F_2^3$. The $\mathbb Z^3$ comes from the three $4$-cells. So $L$ *does* carry brane moduli; (1) does not imply uniqueness of these compatible data.
3. *(Model computation.)* For the Thom spectrum $L^\xi$ of a rank-$0$ virtual bundle $\xi\in\widetilde{KO}^0(L)$, $\mathrm{Sq}^2(U\cdot x)=U\cdot w_2(\xi)\,x$. In particular $\mathrm{Sq}^2U\neq0$ if and only if the $(\mathbb Z/2)^3$-component of $\xi$ is nonzero, and then $\mathrm{Sq}^2$ has rank $4$ on $H^*(L^\xi;\mathbb F_2)$.
4. *(Open.)* We do not determine how a change of brane nullhomotopy by $\kappa\in KO^0(L)$, with $L'$ held fixed, changes the frame values of $\mathcal C_F$, or whether it changes $\mathrm{Sq}^2:H^{-9}(|\mathcal C_F|)\to H^{-7}$.

Item (3) shows that such choices are not irrelevant to $\mathrm{Sq}^2$ in general: in a Thom-spectrum model of a self-pair they are detected by it. Remark 7.2 records what we expect for $(L,L')$, without proof.

### 1.5 What is new and what is not

* **Not new.**
  * Theorem A(1)–(3) are due to Lipshitz–Sarkar [10]; we recompute them independently. A(3) is also stated in [29, Cor. E].
  * The $\mathrm{Sq}^2$ formula is [11].
  * The principle behind Theorem B is not new: changing interval frame values changes the LOS square by an explicit cochain map. This is [29, Prop. D(1)], an immediate consequence of [11]. [29, Cor. E] uses it to show that the two spectra with the integral cohomology of $\mathcal X^{11}_{\rm Kh}(T(3,4))$ are distinguished by $\mathrm{Sq}^2$. Its verification also assembles the $2944$ conditions of Theorem B.
  * The bijection between Floer generators and tuples of intersection points is Manolescu's [5, Thm. 1.3].
  * The endpoint index formula is [28, Lemma 4.1].
  * Positivity of domains is the standard Heegaard Floer argument, transplanted.
  * Proposition B′ is an elementary exercise in [11]; similar small categories appear in [12].
* **New, to our knowledge.**
  * The quantitative analysis of the $q=11$ system: rank $1988$, dimension $1920$, non-constancy (Theorem B).
  * The per-disk analysis (Theorem H): rank $2172$, non-constancy on $A_{\rm disk}$, an explicit per-disk compatible witness, and the resulting pair of framings of the Lipshitz–Sarkar topological flow category in gradings $1$–$5$ with different $\mathrm{Sq}^2$.
  * Theorem C: the explicit generator set, gradings, labelled planar diagram and forced ranks for $T(3,4)$ in $\mathcal Y_3$. This includes the Morse–Bott shift for circle components (Lemma 5.2), and a braid-action engine with built-in checks (braid relations, duality, Morse inequalities for six links).
  * The window statistics of Proposition D.
  * The conditional Theorem E, with explicit objects.
  * Proposition G(2)–(3): the identification of the brane moduli group for $(S^2)^3$, and the Thom-model computation.
* **Not claimed.**
  * We construct no holomorphic strip in $\mathcal Y_3$ for $T(3,4)$, and no Floer flow category, framing or Floer $\mathrm{Sq}^2$.
  * We do not identify any Floer generator with a Khovanov bigrading: $\mathrm{Kh}_{\rm symp}$ is singly graded, and no intrinsic second grading is known at chain level [18, 19].
  * We do not classify the framings of $\mathcal C_F$ that brane data induce. We do not claim that unframed information about $\mathcal C_F$ cannot imply (Sq).
  * Theorem C(3) and Theorem E are conditional.

Compared with [29], which treats decoupled framed flow categories and Haydys–Witten moduli without the Seidel–Smith model, Theorem E is specific: it names the objects and gradings, and it uses positivity. No result here depends on [29].

## 2. Conventions

* **Khovanov homology** follows Lipshitz–Sarkar [9, 10]. Positive crossings are $\sigma_i$, and $\mathrm{Kh}^{h,q}$ has $q$ odd for knots. The sign assignment is $s(u,k)=\#\{j<k:u_j=1\}$, and the frame assignment is that of [10]. Ladybug configurations use the right pairing; the left pairing gives the same answer (verify.py §1).
* **Framed 1-flow categories and the LOS operation** follow [11, Defs. 3.1–3.3, 3.12, Thm. 3.13, Rem. 3.14].
  * For $|a|=|d|+3$, the cycles $C$ of $\partial\mathcal M(a,d)$ are glued from the pieces $I\times\{Q\}$ and $\{P\}\times J$. Put
  $$\tilde f(C)=\sum_{I\times Q\subset C}f(I)+\sum_{P\times J\subset C}\big(1+s(P)+f(J)\big).$$
  * The *summed* condition [11, Def. 3.3] is $\sum_C(1+\tilde f(C))=0$ for each pair $(a,d)$.
  * The *per-disk* condition is $1+\tilde f(C)=0$ for each cycle $C$.
  * The LOS cochain is $\mathrm{sq}^\varphi(a)=|L|+\sum_C(1+F(C)+D(C))$.
* **Braids act on the plane** by counterclockwise half twists. In this convention $(\sigma_1\sigma_2)^2$ closes to the *left* trefoil (verify.py §8), as in [4, §6(C)], where $s_1^3$ closes to a left trefoil. Our right-handed $T(3,4)$ is therefore the inverse-letter word $[\sigma_2^{-1}\sigma_1^{-1}]^4$ of half twists.
* **Gradings.** Seidel's absolute index [16] is in units of $\pi$, with the convention $\operatorname{ind}D_u=i(x)-i(y)$ for a strip from $x$ to $y$ with $u(\cdot,0)\in L$ and $u(\cdot,1)\in L'$ [28, §2]. The collapse is $k=h-q$.

## 3. The Khovanov side (Theorems A, B, H, Proposition B′)

### 3.1 Computation

verify.py §1 builds the cube complex with the conventions of §2. It computes:
* ranks over $\mathbb Q$ by fraction-free elimination;
* torsion by Smith normal form;
* $\mathrm{Sq}^1$ by the integral Bockstein;
* $\mathrm{Sq}^2$ by a generic LOS implementation applied to the Khovanov framed $1$-flow category.

The cube has $1,8,52,144,184,104,20$ generators in $q=11$, $h=0,\dots,6$. The window $h=2\to4$ contains $1392$ intervals, and $80$ pairs $(x,y)$ have two components (ladybug pairs). The results confirm Theorem A(1)–(2) [10]. They pass these controls:
* the graded Euler characteristic equals $(q+q^{-1})V_{T(3,4)}(q^2)$ with $V=t^3+t^5-t^8$;
* the right trefoil is reproduced;
* the answer does not depend on random boundary matchings or on the left/right ladybug convention;
* three corrupted versions of the LOS formula are detected.

### 3.2 The homotopy type of $\mathcal X^{11}$ (A3)

$\mathcal X^{11}$ is a finite spectrum with $\widetilde H^3(\,\cdot\,;\mathbb Z)=\mathbb Z/2$, $\widetilde H^4=\mathbb Z$, and all other groups zero. A minimal cell structure therefore has cells in degrees $2,3,4$, attached as follows:
* the $3$-cell is attached to the $2$-cell with degree $2$;
* the $4$-cell is attached by some $\alpha\in\pi_3(\Sigma^2M(\mathbb Z/2))=\pi_1(M(\mathbb Z/2))$.

The exact sequence $\pi_1S^0\xrightarrow2\pi_1S^0\to\pi_1M\to\pi_0S^0\xrightarrow2\pi_0S^0$ gives $\pi_1M=\mathbb Z/2$, generated by $\eta$ on the bottom cell. If $\alpha=0$, the spectrum is a wedge and $\mathrm{Sq}^2=0$. Since $\mathrm{Sq}^2\neq0$, $\alpha=i\eta$. The same holds for $\Sigma^{-1}\mathbb{RP}^5/\mathbb{RP}^2$, where $\mathrm{Sq}^1x^3=x^4$ and $\mathrm{Sq}^2x^3=\binom32x^5=x^5$. $\square$

### 3.3 The $q$-free form (A4)

The table follows from (1). $\mathrm{Sq}^i$ preserves $q$ on $Z$, and the only nonzero $\mathrm{Sq}^2$ is $(2,11)\to(4,11)$. So $\mathrm{Sq}^2:H^{-9}\to H^{-7}$ has rank one. In degree $k=-9$:
* the class $(4,13)$ is the reduction of an integral class (it is free in $\mathrm{Kh}^{4,13}(\mathbb Z)$), and it satisfies $\mathrm{Sq}^1=\mathrm{Sq}^2=0$;
* $(2,11)$ is not a reduction, since $\mathrm{Kh}^{2,11}(\mathbb Z)=0$, and $\mathrm{Sq}^1(2,11)\neq0$.

So $\ker\mathrm{Sq}^2=\operatorname{im}(H^{-9}(\mathbb Z)\to H^{-9}(\mathbb F_2))$. Every class with $\mathrm{Sq}^1\neq0$ has the form $(2,11)+\epsilon(4,13)$, and $\mathrm{Sq}^2$ of it is nonzero. $\square$

These statements involve only the singly graded cohomology and its Steenrod action. They therefore make sense for a Floer homotopy type of $(L,L')$, which carries no second grading.

### 3.4 Algebraic $1$-flow framings (proof of Theorem B)

**Linearity.** Fix $\mathcal D$. For $|a|-|d|=3$, the cycles of $\partial\mathcal M(a,d)$ and the numbers $s(P)$ depend only on $\mathcal D$. Each summed condition is therefore an affine equation in $f$:
$$\#\{\text{cycles}\}+\sum_{P\times J}(1+s(P))+\sum_If(I)\,\#\{\text{pieces }I\times Q\}+\sum_Jf(J)\,\#\{\text{pieces }P\times J\}\equiv0 .$$
Similarly, fix a cocycle $\varphi$ and a matching. Then $\mathrm{sq}^\varphi=s_0+\sum_If(I)\,[a_I]$, where the sum runs over intervals $I\subset\mathcal M(a_I,c)$ with $c\in\varphi$; this holds because each interval lies in exactly one LOS component [29, Prop. D(1)]. Compose with a functional $\lambda$ that vanishes on coboundaries and detects $\mathrm{Kh}^{4,11}$. This gives the affine function $f\mapsto\mathrm{Sq}^2(f)$, with linear part $\ell$. By [11, Thm. 3.13], on $A$ this function depends neither on $\varphi$ nor on the matching.

**Computation.** verify.py §4 does the following:
1. It assembles the $2944$ conditions and checks that $f_{\rm LS}$ satisfies all of them. This checks the implementation, since those frames come from a genuine framed flow category [10].
2. It computes the rank, $1988$.
3. It shows that $\ell$ is not in the row space. Hence $\mathrm{Sq}^2$ takes both values on $A$, each on exactly half of $A$.
4. It produces an explicit $f_\sharp\in A$ with $\mathrm{Sq}^2=0$ and recomputes the LOS class from scratch.

Toggling the frames of all intervals with exactly one end through a fixed object is compatible and leaves $\mathrm{Sq}^2$ unchanged. The all-zero assignment is incompatible. $\square$

*Scope.* Theorem B concerns framed $1$-flow categories in the sense of [11]. It does not show that an element of $A$ is the truncation of a framed flow category; §3.5 addresses this.

### 3.5 Per-disk framings (proof of Theorem H)

**The topological category.** Lipshitz–Sarkar's Khovanov flow category is a cover of the cube flow category, whose moduli spaces are permutohedra [9]. So every component of a moduli space $\mathcal M(a,d)$ of $\mathcal C^{\rm top}$ is a disk of dimension $|a|-|d|-1$, and it is a copy of $P_{|a|-|d|}$. For $|a|-|d|=3$ the components are hexagons. The boundary of a hexagon is one cycle of [11, Def. 3.3], made of three pieces $I\times Q$ and three pieces $P\times J$ (verify.py §4b: all $3424$ cycles have six edges). The $3424$ cycles are distributed as follows:
* $120$ in pairs of gradings $3\to0$;
* $768$ in $4\to1$;
* $1680$ in $5\to2$;
* $856$ in $6\to3$.

**Per-disk equations (H1).** Suppose a framing of $\mathcal C^{\rm top}$ is given in dimensions $\le1$. A hexagon $H$ with boundary cycle $C$ receives, on $\partial H$, the framing assembled from the product framings of its faces. In the normalization of [11], the framed-bordism class of $\partial H$ in $\Omega_1^{\rm fr}=\pi_1(O)=\mathbb Z/2$ is $1+\tilde f(C)$; the summed condition of [11, Def. 3.3] is the vanishing of the sum of these classes over all boundary circles of a framed surface. The framing extends over the disk $H$ if and only if this class vanishes. So a framing of $\mathcal C^{\rm top}$ imposes one equation per hexagon. As a check of the normalization, $f_{\rm LS}$ satisfies all $3424$ equations; it must, since it frames $\mathcal C^{\rm top}$ [9, 10]. The remaining numbers in (1) are computed exactly in verify.py §4b. The summed rows lie in the per-disk row space because each is the sum of the rows of its cycles. $\square$

**Non-constancy (H2).** verify.py §4b row-reduces the per-disk system and checks that $\ell$ does not reduce to $0$. So $\mathrm{Sq}^2$ is a non-constant affine function on $A_{\rm disk}$, and it vanishes on exactly half of it. The witness $v_\flat$ is the kernel vector attached to the first free variable whose pairing with $\ell$ is $1$. For $f_\flat=f_{\rm LS}+v_\flat$, verify.py checks all $3424$ per-disk and all $2944$ summed equations. It then rebuilds the framed $1$-flow category with frames $f_\flat$ and recomputes the LOS class: it is $0$ for four random boundary matchings and for two cocycle representatives of the Bockstein class. Since $A_{\rm disk}\subset A$, [11, Thm. 3.13] applies. $\square$

**Extension in gradings $1$–$5$ (H3).** $\mathcal C^{\rm top}_{[1,5]}$ is a flow category, because the set of gradings is an interval. Its moduli spaces have dimension $\le3$. We construct framings inductively over the dimension of the moduli spaces, as in [9, §3]. At each stage the framing of $\partial\mathcal M(a,d)$ is determined by the product framings of its faces and must extend over $\mathcal M(a,d)$, a disjoint union of disks; neat embeddings extend in high codimension.
* *Dimension $0$:* the point framings are the given signs.
* *Dimension $1$:* the sign condition holds, since the signs are those of [9]. The extensions over an interval, relative to its endpoints, form a $\pi_1(O)$-torsor whose two elements have different frame values [11, §3], [29, Prop. D(2)]. Choose the one with value $f(I)$.
* *Dimension $2$:* the obstruction for a hexagon is $1+\tilde f(C)\in\pi_1(O)$. This vanishes for all $2448$ hexagons in pairs $4\to1$ and $5\to2$ exactly when the per-disk equations hold. The extension is unique up to homotopy, since $\pi_2(O)=0$.
* *Dimension $3$ ($|a|-|d|=4$):* the obstruction to extending from the boundary $2$-sphere over the $3$-ball lies in $\pi_2(O)=0$.

No higher-dimensional moduli spaces occur in gradings $1$–$5$. Conversely, a framing gives the per-disk equations by (H1).

Both $f_{\rm LS}$ and $f_\flat$ satisfy the $2448$ equations (verify.py §4b). Both framed categories have the same signed $0$-dimensional counts, so their cellular cochain complexes agree: the complex is the $q=11$ Khovanov complex in homological degrees $1,\dots,5$. Their integral cohomology therefore agrees. In degrees $2,3,4$ it equals $\mathrm{Kh}^{h,11}$, because $H^h$ only involves $C^{h-1},C^h,C^{h+1}$. By [11, Thm. 3.13, Rem. 3.14] the LOS operation is the topological $\mathrm{Sq}^2$ of the realization, and the LOS formula only uses moduli spaces between objects of gradings $2$, $3$ and $4$. Hence $\mathrm{Sq}^2:H^2\to H^4$ is nonzero for $f_{\rm LS}$ and zero for $f_\flat$. Here $H^2=\mathbb F_2$. A stable homotopy equivalence would commute with $\mathrm{Sq}^2$, so none exists. $\square$

**(H4).** The components with $|a|-|d|=5$ (pairs $5\to0$ and $6\to1$) are $4$-disks, and the obstruction for them lies in $\pi_3(O)=\mathbb Z$. It can be changed by re-choosing the extensions over the $3$-disks, which form $\pi_3(O)$-torsors. We have not computed this obstruction group. The $5$-dimensional components ($6\to0$) are unobstructed, since $\pi_4(O)=0$.

**Remark 3.6 (what the summed condition frames).** The summed condition does have a flow-category meaning. Restrict to gradings $2$–$5$, where there are no $3$-dimensional moduli spaces. Every $f\in A$ then extends to a framed flow category with the same objects and the same $0$- and $1$-dimensional moduli spaces, after one change: each $2$-dimensional $\mathcal M(a,d)$ with $|a|=5$, $|d|=2$ is replaced by a connected framed surface with the same boundary cycles. Such a surface exists because the boundary classes sum to zero in $\Omega_1^{\rm fr}$; where two hexagons are not individually framable, one can take an annulus. In this sense $f_\sharp$ frames a flow category, but not one with the Lipshitz–Sarkar topology. Theorem H shows that non-constancy survives even after the Lipshitz–Sarkar topology is imposed.

*Interpretation.* Lipshitz–Sarkar proved that $\mathcal X_{\rm Kh}$ does not depend on the choice of sign and frame assignments of the *cube* flow category [9]. The framing $f_\flat$ is a framing of the same topological Khovanov category in gradings $1$–$5$ that is not pulled back from the cube, and Theorem H(3) shows that the realization depends on it. Both values correspond to the two three-level types of §3.2 ([29, Cor. E]).

### 3.6 Proposition B′

The signs are $s(A_1)=0$, $s(A_2)=1$ and $s(B_1)=s(B_2)=0$. The sign condition [11, Def. 3.2] requires the two ends of an interval to have different $A$, which leaves the parallel and crossed pairings. The matching edge at $b$ joins $(B_1,A)$ and $(B_2,A)$, and it is directed because the signs agree. Each pairing gives one LOS cycle, with $D=1$ for the parallel pairing and $D=0$ for the crossed one. This yields the formulas. They are checked by the generic implementation in verify.py §5 and by hand in verify.mpl. $\square$

The crossed pairing is the "ladybug-type" configuration: with trivial frames it produces $\mathrm{Sq}^2\neq0$.

## 4. Arc systems and the braid action

**Model.** Put the punctures $p_0,\dots,p_5$ at positions $0,\dots,5$ on $\mathbb R$. Following Seidel–Smith and Manolescu:
* the closure of $\beta\in Br_3$ is the plat closure of $\beta\otimes1\in Br_6$ with the nested matching $\wp_+=\{(0,5),(1,4),(2,3)\}$;
* $\mathrm{Kh}_{\rm symp}=HF(L_{\wp_+},(\beta\times1)L_{\wp_+})$ [4];
* by [5, Thm. 1.2] we may take $L=\Sigma_{\alpha_1}\times\Sigma_{\alpha_2}\times\Sigma_{\alpha_3}$ and $L'=\Sigma_{\beta_1}\times\Sigma_{\beta_2}\times\Sigma_{\beta_3}$, products of matching spheres in the $A_5$ surface $S$.

Choose $\tau=\sigma_2\sigma_1\sigma_4\sigma_3\sigma_2\sigma_1$ (letters applied left to right). It satisfies $\tau(\wp_0)=\wp_+$ for $\wp_0=\{[0,1],[2,3],[4,5]\}$ (verify.py §6). Applying $\tau^{-1}$ gives
$$HF(L_{\wp_+},(\beta\times 1)L_{\wp_+})\cong HF\big(\Sigma_{\wp_0},\Sigma_{\tau^{-1}(\beta\otimes1)\tau\,\wp_0}\big).$$
So the $\alpha$-arcs are the straight segments $\alpha_{i+1}=[2i,2i+1]$.

**Normal forms.** An arc system is recorded by its ordered points on $\mathbb R$ (punctures and transverse crossings), together with non-crossing upper and lower matchings. Each arc leaves its end punctures vertically. *Normalization* removes innermost bigons (an arc joining consecutive crossing points) and half-bigons (an arc joining a puncture to a consecutive crossing point). The counterclockwise half twist of positions $i,i+1$ acts as follows (derived from the explicit twist map in polar coordinates):
* every chord through $(i,i+1)$ becomes three crossings: a crossing left of $i$ (downward), then one in $(i,i+1)$ (upward, at the reflected position), then one right of $i+1$ (downward);
* the four end-stub types are rotated, with one collar crossing each;
* the orders are as determined in verify.py, and the inverse twist is the conjugate by complex conjugation.

**Lemma 4.1.** The implementation satisfies:
* $ww^{-1}=1$;
* the braid relations;
* far commutation.

Each is tested on 150 random words. The implementation also preserves the non-crossing property after every twist.

*Discussion.* The braid relations are a strong test of the half-twist rule, since a wrong ordering would violate them. Normal forms are minimal with respect to the segments $[2i,2i+1]$, by the bigon criterion. Within a segment, the intersections with $\beta_j$ are the crossing points in the open interval $(2i,2i+1)$ together with common endpoints. $\square$

**Lemma 4.2 (knots).** For a knot, the arcs $\alpha_1\cup\beta_1\cup\dots$ form a single cycle through all six punctures. Hence no $\beta_j$ shares both endpoints with an $\alpha_i$. In particular, the Hopf-type configuration of [28] does not occur between single coordinates; there, two matching spheres meet at two common endpoints and bound a once-punctured bigon. The two-circle strip families with symmetric framings ([28, Thms. C–D]) are therefore not available as building blocks here.

## 5. Generators and gradings (proof of Theorem C)

**Generators [5, Thm. 1.3].** Let $x\in\alpha_i\cap\beta_j$.
* An interior crossing contributes a clean circle of $\Sigma_{\alpha_i}\cap\Sigma_{\beta_j}$, and after perturbation two generators.
* A common endpoint contributes one transverse point.

Generators are triples $(x_1,x_2,x_3)$ with $x_i\in\alpha_i\cap\beta_{\sigma(i)}$ for a permutation $\sigma$, with one of the two generators chosen at each circle. The points have distinct $z$-coordinates, so they lie in $\mathcal Y_3\cap U=U\setminus\Xi$ [5, Cor. 2.9].

**Gradings are additive.** Near a triple of distinct points, $\mathrm{Hilb}^3S=\mathrm{Sym}^3S$ is locally a product, and the holomorphic volume form is the product of the forms $\Omega_S$. The function $\sum_i\tilde\alpha_{\Sigma_{\alpha_i}}$ is a grading of $L$, and similarly for $L'$. The Morse–Bott component is a product of points and circles, and the local index is additive. A change of lift on one curve shifts every generator by the same amount, because each triple uses every $\alpha_i$ and every $\beta_j$ exactly once. Relative gradings are therefore intrinsic.

**Lemma 5.1 (endpoints; [28, Lemma 4.1]).** At a common endpoint $p$, let $\theta$ be the real lift of the tangent direction of $\beta_j$, in units of $\pi$, with the lift of $\alpha_i$ equal to $0$. Let $\varepsilon\in(0,2)$ be the outgoing angle of $\beta_j$ minus that of $\alpha_i$, mod $2$. Then the index is $i=\theta-\varepsilon$.

**Lemma 5.2 (clean circles).** At an interior crossing, let $\theta$ be the lift of $\beta_j$, so $\theta\in\tfrac12+\mathbb Z$. The two generators have degrees $\theta-\tfrac12-1$ and $\theta-\tfrac12$.

*Proof.* The graded germ of $(\Sigma_{\alpha},\Sigma_\beta)$ at a crossing circle is the same at every crossing, up to the grading shift $\theta$. The Kähler angles are $0$ (the circle direction) and $\tfrac12$. So the Poźniak shift [17] is $\theta-\tfrac12+c$ for a universal integer $c$. To find $c$, take a curve isotopic to $[0,1]$ that crosses it once in the interior; it has two endpoints and one circle. $HF$ must be $H^*(S^2)$, so after one pair of consecutive degrees cancels, two degrees differing by $2$ must remain. In both mirror pictures this forces $c=-1$; the alternative $c=0$ fails in both (verify.py §7). $\square$

**Validation.** Lemmas 5.1–5.2 are further tested in verify.py §8:
* for the identity braid, the complex has the Poincaré polynomial of $H^*((S^2)^3)$, as it must for the unlink;
* $\sigma_1$ and $\sigma_1\sigma_2$ give minimal complexes;
* $CF(L,bL)$ and $CF(L,b^{-1}L)$ have reversed degree distributions for $80$ random braids, as duality requires;
* for six links (left trefoil, figure eight, $T(3,3)$, $\sigma_1^3\sigma_2$, $T(2,5)$, $\sigma_1^2\sigma_2^{-3}$), the Morse inequalities $C(t)-t^sH(t)=(1+t)Q(t)$ with $Q\ge0$ have exactly one solution $s$, where $H$ is the collapsed rational Khovanov polynomial;
* the chirality controls fail, as they should.

**Table 1 (labelled planar diagram of the 116-model).** The data are printed by verify.py §11.

*Axis.* The $27$ points on $\mathbb R$, from left to right, are
$$x_1\,x_2\,x_3\,x_4\;p_0\;x_5\,x_6\,x_7\;p_1\;x_8\,x_9\,x_{10}\,x_{11}\;p_2\;x_{12}\,x_{13}\,x_{14}\;p_3\;x_{15}\,x_{16}\,x_{17}\,x_{18}\;p_4\;x_{19}\,x_{20}\,x_{21}\;p_5 .$$
Here $\alpha_1=[p_0,p_1]$, $\alpha_2=[p_2,p_3]$ and $\alpha_3=[p_4,p_5]$. The crossings inside the $\alpha$-segments are $x_5,x_6,x_7$, $x_{12},x_{13},x_{14}$ and $x_{19},x_{20},x_{21}$.

*Curves.* Each $\beta_j$ visits the axis points listed below. Consecutive points are joined by arcs that lie alternately in the upper and lower half-plane, starting in the half-plane indicated. The bracket is the lift $\theta$ of the tangent direction, in units of $\pi$.

| curve | first arc | axis points $[\theta]$ |
|---|---|---|
| $\beta_1$ | upper | $p_0[\tfrac12]\,x_{11}[-\tfrac12]\,x_{12}[\tfrac12]\,x_{17}[-\tfrac12]\,x_{20}[\tfrac12]\,x_2[\tfrac32]\,x_7[\tfrac52]\,x_8[\tfrac32]\,p_3[\tfrac52]$ |
| $\beta_2$ | lower | $p_1[-\tfrac12]\,x_1[-\tfrac32]\,x_{21}[-\tfrac52]\,x_{16}[-\tfrac72]\,x_{13}[-\tfrac52]\,x_{10}[-\tfrac72]\,x_5[-\tfrac52]\,x_4[-\tfrac72]\,p_4[-\tfrac92]$ |
| $\beta_3$ | upper | $p_2[\tfrac12]\,x_{18}[-\tfrac12]\,x_{19}[\tfrac12]\,x_3[\tfrac32]\,x_6[\tfrac52]\,x_9[\tfrac32]\,x_{14}[\tfrac52]\,x_{15}[\tfrac32]\,p_5[\tfrac52]$ |

*Intersections and local degrees* (before the global shift $k=\sum-8$; a circle gives two degrees).

| | $\beta_1$ | $\beta_2$ | $\beta_3$ |
|---|---|---|---|
| $\alpha_1$ | $p_0\,(0)$; $x_7\,(1,2)$ | $p_1\,(-1)$; $x_5\,(-4,-3)$ | $x_6\,(1,2)$ |
| $\alpha_2$ | $x_{12}\,(-1,0)$; $p_3\,(2)$ | $x_{13}\,(-4,-3)$ | $p_2\,(0)$; $x_{14}\,(1,2)$ |
| $\alpha_3$ | $x_{20}\,(-1,0)$ | $x_{21}\,(-4,-3)$; $p_4\,(-5)$ | $x_{19}\,(-1,0)$; $p_5\,(2)$ |

*Window generators.* Each entry is a triple $(x_1,x_2,x_3)$ with $x_i\in\alpha_i$, followed by its local degrees.
* $k=-7$:
  * $a_1=(x_7,x_{13},p_5)$, degrees $(2,-3,2)$;
  * $a_2=(x_7,x_{14},x_{21})$, degrees $(2,2,-3)$;
  * $a_3=(p_1,x_{12},p_5)$, degrees $(-1,0,2)$;
  * $a_4=(p_1,p_3,x_{19})$, degrees $(-1,2,0)$;
  * $a_5=(x_5,p_3,p_5)$, degrees $(-3,2,2)$;
  * $a_6=(p_1,x_{14},x_{20})$, degrees $(-1,2,0)$;
  * $a_7=(x_6,p_3,x_{21})$, degrees $(2,2,-3)$.
* $k=-8$:
  * $b_1,b_2=(x_7,x_{13},p_5)$, degrees $(1,-3,2)$ and $(2,-4,2)$;
  * $b_3,b_4,b_5=(x_7,x_{14},x_{21})$, degrees $(1,2,-3)$, $(2,1,-3)$, $(2,2,-4)$;
  * $b_6=(p_1,x_{12},p_5)$, degrees $(-1,-1,2)$;
  * $b_7=(p_1,p_3,x_{19})$, degrees $(-1,2,-1)$;
  * $b_8=(x_5,p_3,p_5)$, degrees $(-4,2,2)$;
  * $b_9,b_{10}=(p_1,x_{14},x_{20})$, degrees $(-1,1,0)$ and $(-1,2,-1)$;
  * $b_{11},b_{12}=(x_6,p_3,x_{21})$, degrees $(1,2,-3)$ and $(2,2,-4)$.
* $k=-9$:
  * $c_1=(p_0,x_{13},p_5)$;
  * $c_2=(x_7,x_{13},x_{19})$;
  * $c_3=(x_7,x_{13},p_5)$;
  * $c_4=(p_0,x_{14},x_{21})$;
  * $c_5=(x_7,p_2,x_{21})$;
  * $c_6,c_7,c_8=(x_7,x_{14},x_{21})$, with degrees $(1,1,-3),(1,2,-4),(2,1,-4)$;
  * $c_9=(x_7,x_{14},p_4)$;
  * $c_{10}=(p_1,x_{12},x_{19})$;
  * $c_{11}=(x_5,x_{12},p_5)$;
  * $c_{12}=(x_5,p_3,x_{19})$;
  * $c_{13}=(p_1,p_2,x_{20})$;
  * $c_{14}=(p_1,x_{14},x_{20})$;
  * $c_{15}=(x_5,x_{14},x_{20})$;
  * $c_{16}=(x_6,x_{12},x_{21})$;
  * $c_{17}=(x_6,p_3,x_{21})$;
  * $c_{18}=(x_6,p_3,p_4)$;
  * $c_{19}=(x_6,x_{13},x_{20})$.

  The full degree list is in verify_output.txt §11.

**Proof of Theorem C.** Applying the engine to $\tau^{-1}(\beta\otimes1)\tau$ gives three curves $\beta_j$ with $7$ axis crossings each (Table 1). Each segment meets each curve in exactly one interior crossing, plus common endpoints. This yields the $116$ generators and the distribution in (1).

The collapsed polynomial is $H=t^{-12}+2t^{-10}+t^{-9}+3t^{-7}+t^{-5}$ over $\mathbb Q$ [6]. The Morse inequalities admit exactly one shift, and this fixes the $k$-normalization.

Write $c_k$ for the number of generators, $h_k$ for $\dim HF^k$ and $r_k$ for $\operatorname{rk}\delta^k$. Then $c_k=h_k+r_k+r_{k-1}$. Since $r$ vanishes below the bottom degree, the recursion determines every $r_k$. This gives (2); with the $\mathbb F_2$-ranks of (H$_2$) it gives (3). Under (H$_\mathbb Z$):
* the torsion of $HF^{-8}(\mathbb Z)$ is $\mathbb Z/2$, which equals the cokernel torsion of $\delta^{-9}$;
* no other degree has torsion.

This gives the Smith forms. For (4), the generator in degree $-5$ is $(p_1,p_3,p_5)$, with local degrees $(-1,2,2)$ and all three points at punctures (verify.py §8), and $c_{-6}=0$. Item (5) is the same computation for $(\sigma_1\sigma_2)^4$. $\square$

## 6. Positivity (proof of Proposition D)

For generators $x,y$, let $\gamma_{xy}$ be the closed $1$-cycle in $\mathbb C$ made of two kinds of $1$-chains:
* the unique $1$-chains on the arcs $\alpha_i$ from $x$ to $y$;
* the unique $1$-chains on the arcs $\beta_j$ from $y$ to $x$.

The arcs are intervals, so these chains are unique. Let $D(x,y)$ be the winding-number function of $\gamma_{xy}$. Then:
* $D$ is additive;
* $D(x,x)=0$;
* $D$ vanishes in the unbounded face;
* there are no periodic domains, since the arcs are not closed.

verify.py §9 computes $D$ by vertical rays at sample points just above and just below every gap between consecutive axis points of Table 1. It checks that the two samples differ exactly by the $\alpha$-chain, and that $D$ is additive.

*Proof.* The ideal of a point of $\mathcal Y_3\subset\mathrm{Hilb}^3S$ contains a monic cubic in $z$ [5]. Its roots define a holomorphic map $\pi:\mathcal Y_3\to\mathrm{Sym}^3\mathbb C$. For $c\notin\bigcup\alpha_i\cup\bigcup\beta_j$, put $g_c=\prod_i(c-z_i)$. Let $u$ be a strip, and suppose $\pi$ is holomorphic near $\pi^{-1}(V_c)$ (Hypothesis (J)). Then $g_c\circ\pi\circ u$ is holomorphic near its zeros, and it is nonzero on the boundary and at the ends. By the argument principle, its number of zeros equals the winding number of $g_c$ along $\partial u$. That winding number is $\sum_i\operatorname{wind}(\pi(\partial u)_i,c)=D(x,y)(c)$, because the boundary sheets run along the $\alpha_i$ from $x$ to $y$ and along the $\beta_j$ back. Hence $D(x,y)\ge0$.

If $D\equiv0$, then $\pi\circ u$ is constant, so $u$ lies in a fibre of $\pi$. Then $x$ and $y$ have the same planar points, and they lie in the same Morse–Bott component. Broken strips and cascades add domains.

The orientation check uses the cohomological convention: a strip from $x$ to $y$ contributes to $\delta y^*$ when $\deg x=\deg y+1$. With the opposite sign, the bipartite support from degree $-9$ to $-8$ has term rank $6$, which is smaller than the forced rank $8$. $\square$

**Table 2 (positive pairs in the window).** Rows are listed in the order of Table 1; a $1$ in column $j$ means that the pair (row, $j$-th generator of the lower degree) has $D\ge0$ and $D\neq0$.

| | $-7\to-9$ (columns $c_1,\dots,c_{19}$) | $-7\to-8$ (columns $b_1,\dots,b_{12}$) |
|---|---|---|
| $a_1$ | `111111111.1...11..1` | `11111.......` |
| $a_2$ | `.1.111111.....11..1` | `..111.......` |
| $a_3$ | `11111111111.1111..1` | `111111..11..` |
| $a_4$ | `.1.1111111.11111111` | `..111.1.1111` |
| $a_5$ | `111111111.11..11111` | `11111..1..11` |
| $a_6$ | `.1.1111111..1111..1` | `..111...11..` |
| $a_7$ | `.1.111111..1..11111` | `..111.....11` |

For $-8\to-9$ (columns $c_1,\dots,c_{19}$):

| row | pattern | row | pattern |
|---|---|---|---|
| $b_1$ | `111111111.1...11..1` | $b_7$ | `.1.1111111.11111111` |
| $b_2$ | `111111111.1...11..1` | $b_8$ | `111111111.11..11111` |
| $b_3$ | `.1.111111.....11..1` | $b_9$ | `.1.1111111..1111..1` |
| $b_4$ | `.1.111111.....11..1` | $b_{10}$ | `.1.1111111..1111..1` |
| $b_5$ | `.1.111111.....11..1` | $b_{11}$ | `.1.111111..1..11111` |
| $b_6$ | `11111111111.1111..1` | $b_{12}$ | `.1.111111..1..11111` |

The totals are $97$, $42$ and $156$.

## 7. Theorem E, Corollary F and Proposition G

*Proof of Theorem E.*

(1)–(2). By (FFC), $\mathcal C_F$ is a framed flow category. So its truncation is a framed $1$-flow category whose LOS operation is the topological $\mathrm{Sq}^2$ of $|\mathcal C_F|$ [11, Rem. 3.14]. By (H$_2$) and Theorem C, $H^{-9}(\mathbb F_2)$ is $2$-dimensional and contains the Bockstein class (Theorem A(4)). By (Sq), $[\mathrm{sq}^\varphi]\neq0$, so $\mathrm{sq}^\varphi(a)=1$ for some $a$ of degree $-7$. By Theorem C(4) there are $7$ candidates. If every $\mathcal M(a,c)$ with $c\in\varphi$ were empty or a union of trivially framed circles, the sum would vanish. Positivity (Proposition D) restricts the pairs.

(3) is Theorem C(3). $\square$

**Remark 7.1 (scope of Theorems B and H for $\mathcal C_F$).** The first version of this paper also claimed that no comparison of unframed data alone can yield (Sq). That claim is withdrawn. What is proved is narrower. For the Khovanov data, $\mathrm{Sq}^2$ is not a function of the unframed $1$-flow data (Theorem B). In gradings $1$–$5$, it is not even a function of the full unframed topological flow category (Theorem H(3)). Neither statement constrains the framings of $\mathcal C_F$ that brane data induce, and neither excludes that unframed information about $\mathcal C_F$ (its higher-dimensional moduli spaces, or its relation to brane data) determines them.

*Proof of Corollary F.*
1. An equivalence of spectra induces an isomorphism on mod-$2$ cohomology commuting with the Steenrod algebra. The integral cohomology and the Steenrod action of the collapsed spectrum are those of Theorem A, and these give (H$_\mathbb Z$), (H$_2$) and (Sq) for $|\mathcal C_F|$. Then apply Theorem E.
2. Under (Cmp), the truncations of $\mathcal C_{\rm HW}$ and $\mathcal C_F$ to degrees $-9,\dots,-7$ are isomorphic framed $1$-flow categories. The LOS cochain, the rigid counts and the frame values are therefore the same, and the proof of Theorem E applies to $\mathcal C_{\rm HW}$. $\square$

[29, Cor. E] reaches a related conclusion for HW moduli without the Seidel–Smith model. As in [28, Cor. E(2)], if the HW instanton number is a topological charge, (Ad) can hold only at the level of realizations. This is why the moduli-level statement needs (Cmp).

*Proof of Proposition G.*
1. Use the stable splitting $(S^2)^3\simeq_s3S^2\vee3S^4\vee S^6$. We have $\widetilde{KO}^{-1}(S^n)=\pi_n(O)$, which vanishes for $n=2,4,6$, and $\widetilde K^{-1}(S^n)=\pi_n(U)=0$ for even $n$.
2. $\widetilde{KO}^0(S^n)=\pi_n(BO)=\pi_{n-1}(O)$ is $\mathbb Z/2$, $\mathbb Z$, $0$ for $n=2,4,6$ (verify.py §10). Bott periodicity gives $\Omega(U/O)\simeq\mathbb Z\times BO$. The description of brane data and of the torsor is that of [20, §7.5]. The generator of $\widetilde{KO}^0(S^2)=\mathbb Z/2$ has $w_2\neq0$, and the splitting maps the $(\mathbb Z/2)^3$ summand isomorphically onto the restriction to the $2$-skeleton $S^2\vee S^2\vee S^2$.
3. $H^*(L;\mathbb F_2)$ is the exterior algebra on $a_1,a_2,a_3$ in degree $2$. Here $\mathrm{Sq}^1=0$ (odd degrees vanish) and $\mathrm{Sq}^2a_i=a_i^2=0$, so the Cartan formula gives $\mathrm{Sq}^2=0$ on $H^*(L)$. Since $w_1(\xi)=0$, the Thom formula gives $\mathrm{Sq}^2(Ux)=U(\mathrm{Sq}^2x+w_2(\xi)x)=U\,w_2(\xi)x$. Multiplication by a nonzero $w_2=\sum\epsilon_ia_i$ has rank $4$ on the exterior algebra (verify.py §10). $\square$

**Remark 7.2 (what we expect for $(L,L')$; not used).** Two things seem plausible, but we have not proved either.
* A change of brane nullhomotopy on $L$ by $\kappa$ alters the framings of moduli spaces of dimension $\le1$ only through $\kappa$ restricted to $2$-dimensional families of boundary paths. If so, it acts on interval frame values only through $w_2(\kappa)\in H^2(L;\mathbb F_2)$, together with gauge changes.
* By analogy with (3), $\mathrm{Sq}^2$ on $H^*(|\mathcal C_F|)$ changes by the module action of $w_2(\kappa)\in H^2(L;\mathbb F_2)\cong HF^2(L,L)$ on $HF(L,L')$.

This action raises the Floer degree by $2$, exactly as in the window $-9\to-7$. So the brane choice could matter for (Sq). This dependence is left open.

## 8. Discussion

**What would complete the computation.** Four things are missing:
1. Holomorphic strips in $\mathcal Y_3$ for the $156+42+97$ positive window pairs of Table 2. In Heegaard Floer genus $0$, positive bigons and rectangles are counted by the Riemann mapping theorem. Here the fibres are conics degenerating at the punctures, and [28] treats only the fibred Hopf model. A first step would be an index formula for domains, combining Euler measure, corner terms and multiplicities at the punctures, which would cut down the support.
2. A Floer framed flow category (FFC) for $(L,L')$, for instance through [20, 22, 23], with explicit ambient tangential data on $\mathcal Y_3$. We do not know whether $T\mathcal Y_3$ admits the stable trivialization or polarization these frameworks require.
3. The brane data on $L$ and $L'$: Proposition G shows that they form a $KO^0(L)$-torsor with nontrivial $(\mathbb Z/2)^3$-part, and their effect on the frames is open.
4. The frame values themselves. Theorems B and H show that, on the Khovanov side, these values are not determined by the unframed data in the ranges considered.

**Prediction (falsifiable within the model).** Suppose a Floer homotopy type of $(L,L')$ is constructed and is equivalent to the collapsed Lipshitz–Sarkar spectrum. Then its Steenrod data are those of Theorem A(4): $\mathrm{Sq}^1$ and $\mathrm{Sq}^2$ both have rank one, and they are nonzero on the same class in degree $-9$. In the presentation $\mathcal C_F$, some generator among $a_1,\dots,a_7$ carries the target. If instead the frame values induced by the Floer theory, for some admissible brane data, make $\mathrm{Sq}^2=0$, then the spectral form of [4, Conj. 2] fails for $T(3,4)$ for those brane data.

### 8.1 Status of claims

| Statement | Status | Inputs |
|---|---|---|
| A(1)–(2): Kh, $\mathrm{Sq}^1$, $\mathrm{Sq}^2$ of $T(3,4)$ | known [10]; recomputed exactly | cube, LOS [11] |
| A(3): $\mathcal X^{11}\simeq\Sigma^{-1}\mathbb{RP}^5/\mathbb{RP}^2$ | known [10, 29]; short proof | $\pi_1M(\mathbb Z/2)=\mathbb Z/2$ |
| A(4): $q$-free form | proved | A(1)–(2) |
| B: algebraic 1-flow framings | principle known [29, Prop. D]; quantitative statement proved by exact computation | [11, Def. 3.3, Thm. 3.13] |
| H(1)–(2): per-disk system, non-constancy, witness | proved (exact computation) | [9], [11] |
| H(3): two framings of $\mathcal C^{\rm top}_{[1,5]}$ with different $\mathrm{Sq}^2$ | proved | obstruction theory, $\pi_1(O)$, $\pi_2(O)=0$ |
| H(4): extension in gradings $0$–$6$ | **open** | $\pi_3(O)=\mathbb Z$ obstruction |
| B′: three-object windows | proved (elementary) | [11] |
| Lemma 4.1: braid engine | proved properties + checked | — |
| Lemmas 5.1 / 5.2: local indices | proved / proved by locality + test | [28], [16], [17] |
| C(1),(4),(5): generators, gradings, Table 1 | proved | [5, Thms. 1.2–1.3], Lemmas 5.1–5.2 |
| C normalization, C(2): forced $\mathbb Q$-ranks | proved | [6] (char 0) |
| C(3): $\mathbb F_2$ / $\mathbb Z$ ranks, Smith form | conditional | (H$_2$) / (H$_\mathbb Z$) |
| D: positivity | conditional | (J) |
| D: window counts, Table 2 | computed | — |
| E(1)–(3) | conditional, for the presentation $\mathcal C_F$ | (FFC), (H$_2$), (Sq); (J), (H$_\mathbb Z$) for parts |
| F(1): spectral transfer | conditional | (Ad) |
| F(2): moduli-level transfer | conditional | (Ad) + (Cmp) |
| G(1)–(3): $KO^{-1}$, $K^{-1}$, $KO^0$; Thom model | proved | Bott periodicity, [20, §7.5] |
| G(4): effect of brane data on frames of $\mathcal C_F$ | **open** | — |
| Floer strips, frames, Floer $\mathrm{Sq}^2$ for $T(3,4)$ | **not done** | — |

### 8.2 Verification

verify.py runs $88$ exact checks and ends with `FALLOS = 0`, in about $15$ s, using only the standard library. It covers the sections above, with positive and negative controls:
* corrupted LOS variants;
* the same-side ladybug pairing;
* the shifted circle convention;
* the chirality controls;
* the reversed positivity orientation;
* in §4b, the per-disk system: $3424$ six-edge cycles, rank $2172$, $f_{\rm LS}$ satisfies all equations (a normalization check), $f_\sharp$ violates $486$, non-constancy, and the explicit witness $f_\flat$ recomputed from scratch;
* in §10, $KO^0((S^2)^3)$ and the Thom model;
* in §11, the data of Tables 1–2.

It does not verify any analytic statement: regularity, compactness, the hypotheses of [5, Thm. 1.2], (J), or the obstruction-theoretic step of Theorem H(3) beyond the identification of the obstruction groups.

verify.mpl is unchanged from the first version. It mirrors these exact finite parts:
* the collapse and the Jones polynomial;
* Proposition B′ and the local indices;
* the Morse recursion and forced ranks;
* the Euler characteristics and the Bott table for $KO^{-1}$.

It has been executed in Maple (21 checks) and gives `FALLOS = 0`. The new computations of §4b, §10 and §11 are in verify.py only.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086; arXiv:1106.4789.
3. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
4. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514; arXiv:math/0405089.
5. C. Manolescu, *Nilpotent slices, Hilbert schemes, and the Jones polynomial*, Duke Math. J. 132 (2006), 311–369; arXiv:math/0411015.
6. M. Abouzaid, I. Smith, *Khovanov homology from Floer cohomology*, J. Amer. Math. Soc. 32 (2019), 1–79; arXiv:1504.01230.
7. M. Abouzaid, I. Smith, *The symplectic arc algebra is formal*, Duke Math. J. 165 (2016), 985–1060; arXiv:1311.5535.
8. P. Seidel, I. Smith, *Localization for involutions in Floer cohomology*, Geom. Funct. Anal. 20 (2010), 1464–1501.
9. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.
10. R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848; arXiv:1204.5776.
11. A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500; arXiv:1710.01857.
12. D. Jones, A. Lobb, D. Schütz, *Morse moves in flow categories*, arXiv:1507.03502.
13. T. Lawson, R. Lipshitz, S. Sarkar, *Khovanov homotopy type, Burnside category, and products*, Geom. Topol. 24 (2020), 623–745.
14. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.
15. M. Khovanov, P. Seidel, *Quivers, Floer cohomology, and braid group actions*, J. Amer. Math. Soc. 15 (2002), 203–271.
16. P. Seidel, *Graded Lagrangian submanifolds*, Bull. Soc. Math. France 128 (2000), 103–149.
17. M. Poźniak, *Floer homology, Novikov rings and clean intersections*, Amer. Math. Soc. Transl. Ser. 2, 196 (1999), 119–181.
18. K. Hendricks, C. Y. Mak, S. Raghunath, *Symplectic annular Khovanov homology and fixed point localizations*, arXiv:2408.06453.
19. Z. Cheng, *Bigrading the symplectic Khovanov cohomology*, Algebr. Geom. Topol. 23 (2023); arXiv:2111.07792.
20. N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257.
21. N. Porcelli, I. Smith, *Bordism of flow modules and exact Lagrangians*, arXiv:2401.11766.
22. T. Large, *Spectral Fukaya categories for Liouville manifolds*, PhD thesis, MIT, 2021.
23. M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.
24. M. Khovanov, R. Lipshitz, *Categorical lifting of the Jones polynomial: a survey*, arXiv:2202.02473.
25. D. Bar-Natan, *On Khovanov's categorification of the Jones polynomial*, Algebr. Geom. Topol. 2 (2002), 337–370.
26. S. Bigelow, *A homological definition of the Jones polynomial*, Geom. Topol. Monogr. 4 (2002), 29–41.
27. M. Marengon, S. Sarkar, A. Stipsicz, *Spectra in Khovanov and knot Floer theories*, arXiv:2401.06218.
28. rStation math_35 v1, *The Hopf link in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and its realization*, rStation (2026), https://rstation.ai/problems/math/papers/35/v1
29. rStation math_52 v1, *Decoupled framed flow categories and Steenrod squares beyond homology: a three-level classification, reframings of products, and applications to Haydys–Witten theory*, rStation (2026), https://rstation.ai/problems/math/papers/52/v1 (Proposition D: reframing formula for the LOS square; Corollary E: the two spectra with the integral cohomology of $\mathcal X^{11}_{\rm Kh}(T(3,4))$).
30. rStation math_36 v1, *The trefoil in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and the geometric origin of the $\mathbb Z/2$ and of the Moore piece*, rStation (2026), https://rstation.ai/problems/math/papers/36/v1
31. rStation math_39 v1, *The framing bit of the trefoil in the adiabatic Seidel–Smith model vanishes*, rStation (2026), https://rstation.ai/problems/math/papers/39/v1

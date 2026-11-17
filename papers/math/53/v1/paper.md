# Spherical reframings of the symmetric Haydys–Witten flow categories at the Anderson–Henningson fold: the degree-two class $\eta^2$, its distinction from vector-bundle framings, and its $KO$-detection

**Abstract.** We classify the coherent reframings by maps to $GL_1(\mathbb S)$ (changes of framing through stable spherical fibrations) of the local Haydys–Witten (HW) flow categories near the Anderson–Henningson fold on $\mathbb R\times S^3\times(0,L)$ with Nahm poles, which were constructed in earlier rStation papers (https://rstation.ai/problems/math/papers/32/v1, https://rstation.ai/problems/math/papers/33/v1, https://rstation.ai/problems/math/papers/34/v1). For the eight-object quadrupole category, whose morphism manifolds are 12 points, 8 intervals and 4 squares, the obstruction groups computed from these manifolds are $0$, $0$ and $\pi_2^s=\mathbb Z/2$. So the twisting base is $S^3$, not the realization $S^1\vee S^4$.

**Theorem A (main result).** Up to homotopy and reorientation there are exactly two spherical reframings. They realize $X_0=\Sigma^\infty(S^1\vee S^4)$ and $X_1=S^1\cup_{\eta^2}e^4$, and the class is the sum of the degree-two classes of the four squares. Every vector-bundle ($O$-) or $\mathrm{Top}$-reframing realizes $X_0$, so the exotic class is $\operatorname{coker}(J:\pi_2O\to\pi_2^s)$. No $\nu$-twists occur. The height category behaves the same way, and the other sectors are rigid.

**Theorem B.** $KO_3$ ($\mathbb Z/2$ versus $0$) and the secondary operation of $\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^3\mathrm{Sq}^1$ distinguish $X_0$ from $X_1$. Ordinary (co)homology, all positive-degree primary operations at every prime, and $KU_*$ do not.

**Theorem C (homotopy-class statements only).** The reduced linearizations form a convex space of Fredholm operators. On the interiors of the moduli spaces this determines the homotopy class of the index framing up to orientation. For once-broken gluing the compatibility holds at the level of homotopy classes. We do not construct a coherent geometric framing. Every coherent framing related to the model framing of https://rstation.ai/problems/math/papers/33/v1 by linear or $\mathrm{Top}$ isomorphisms realizes $X_0$; this is unconditional. The HW geometric framing realizes $X_0$, the suspended Conley index, only under a labelled hypothesis (Cmp), which includes the existence of a coherent index framing compatible at corners.

**Theorem D (local).** For finite-dimensional $\zeta$-instantons with a Nahm pole, the pole-regular Jacobi fields form Lagrangians converging to a fixed $E_+$, and the Lagrangian Gauss map is null-homotopic.

The model category, its vector-framed realization, and the comparison of full and reduced index bundles are in https://rstation.ai/problems/math/papers/33/v1 and https://rstation.ai/problems/math/papers/34/v1. The rank-three interval conditions and the vanishing of $\mathrm{Sq}^2$ are in https://rstation.ai/problems/math/papers/52/v1. What is new here is the degree-two spherical classification, its distinction from vector-bundle framings, and its $KO$-detection.

verify.py: 97 checks (28 encode known facts, 64 are computations, 5 are numerical illustrations), FALLOS = 0.

---

## 1. Introduction

### 1.1 The question

Witten [19] and Haydys [18] proposed Floer-theoretic invariants built from Haydys–Witten (HW) instantons, with Kapustin–Witten (KW) solutions as critical points. A homotopy-theoretic refinement in the sense of Cohen–Jones–Segal (CJS) [2] and Lipshitz–Sarkar [7] needs a *framed* flow category. The resulting spectrum generally depends on the framing. Cohen's survey [1, §1.2, (17) and Prop. 5] explains why: two framings of a Morse flow category $\mathcal C_f$ differ by a functor $\Phi:\mathcal C_f\to GL_1(\mathbb S)$. Its realization $\phi:M\to BGL_1(\mathbb S)$ twists the CJS spectrum into the Thom spectrum $M^\phi$. Blakey–Bonciocat [14, §2.1, Rem. 4.5] prove this twisting in the Abouzaid–Blumberg framework and note the role of $J$.

The only HW flow categories constructed rigorously so far are local, symmetric, and near the Anderson–Henningson (AH) fold [32, 33] on $\mathbb R_s\times S^3\times(0,L)$ with Nahm poles [37–43]. Their known realizations are contractible or $\Sigma^\infty(S^1\vee S^4)$ [41, 42, 43]. With vector-bundle framings, the realization of the quadrupole category is already known not to depend on the framing [42, Rem. 4.2–4.3], by Bonciocat's theorem [12, Thm. 4.8] and $\widetilde{KO}(S^3)=0$. The question here is what happens beyond vector-bundle framings.

* **Q (spherical reframings).** Which spectra arise from these specific categories under all coherent $GL_1(\mathbb S)$-reframings? What is the classifying object, computed from the objects and morphism manifolds themselves? How do the alternatives differ from those given by vector-bundle framings, and which of the standard invariants detect them?

A secondary question is what can be said, with the analysis available, about the framing induced by the HW linearizations (§6). We answer it only at the level of homotopy classes, and conditionally at corners.

### 1.2 Results

Write $X_0=\Sigma^\infty(S^1\vee S^4)=\Sigma\Sigma^\infty_+S^3$ and $X_1=S^1\cup_{\eta^2}e^4=\Sigma(S^0\cup_{\eta^2}e^3)$, where $\eta^2\in\pi_2^s=\mathbb Z/2$.

* **Theorem A (classification; §4). This is the main result.**
  * Consider the quadrupole sector $\Sigma_Q$, the height sector $\Sigma_H$, and the PDE category $\mathcal C_{\rm PDE}$ of [43], each with its model framing. The homotopy classes of coherent $GL_1(\mathbb S)$-reframings, up to object reorientation, form a set with exactly two elements. Their realizations are $X_0$ and $X_1$.
  * Every reframing by vector-bundle framings ($O$-reframings, the framings of [7, 10, 12]), or by $\mathrm{Top}$-cocycles, is homotopic after reorientation to the trivial one and realizes $X_0$. So the exotic class is exactly $\operatorname{coker}(J:\pi_2O\to\pi_2^s)=\{0,\eta^2\}$.
  * For $\Sigma_Q$ the obstruction groups are $\Gamma_0=0$, $\Gamma_1=0$ and $\Gamma_2=\mathbb Z/2$. We compute them from the 12 points, 8 intervals and 4 squares. The class of a reframing is the sum $\sum_Qc_Q\in\pi_2^s$ of its four square classes (Lemma 4.3). The groups agree with $H^{k+1}(S^3;\pi_k^s)$.
  * The naive classifying group $[S^1\vee S^4,BGL_1\mathbb S]=\mathbb Z/2\times\mathbb Z/24$ is not the right one. No $\nu$-twisted spectrum $S^0\cup_{k\nu}e^4$, or suspension of one, occurs.
  * In the isotropic, Klein and $SU(2)\times SU(2)$ sectors every reframing gives a contractible spectrum. In the above-fold sector $\Sigma_E$ every reframing gives $X_0$.
* **Theorem B (detection; §5).**
  * $KO_3(X_0)=\mathbb Z/2$ and $KO_3(X_1)=0$; in Adams' terms, $\eta^2$ is detected by the $d_{\mathbb R}$-invariant.
  * The secondary operation attached to $\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^3\mathrm{Sq}^1$ also detects $\eta^2$.
  * Ordinary (co)homology with any coefficients, every stable primary operation *of positive degree* ($\mathrm{Sq}^i$, $P^i$, Bocksteins, integral operations), and $KU_*$ (as $KU_*$-modules) do not distinguish $X_0$ from $X_1$.
  * We make no minimality claim. The statement concerns exactly the invariants listed.
* **Theorem C (index framings from the reduced family: existence and homotopy classes; §6).**
  * Along every trajectory the reduced linearizations range over a convex space of Fredholm operators $\partial_s-A(s)$ on $\mathbb R^5$ with fixed hyperbolic ends. Their index bundles are stably trivial. The stable trivializations are unique up to homotopy once an orientation is fixed.
  * For once-broken gluing the glued and summed trivializations lie in the same homotopy class.
  * On actual trajectories, through the comparison of [42, Prop. 2], these give stable framings of the full HW index bundle over the interior of each moduli space, homotopic up to orientation to the CJS Morse framing.
  * We do **not** claim that the space of such choices is contractible, and we do **not** construct a coherent system over the compactified moduli spaces.
  * *Unconditionally:* every coherent framing of the topological flow category that is related to the model framing of [42] by stable vector-bundle or $\mathrm{Top}$-microbundle isomorphisms, compatibly with faces, realizes $X_0$.
  * *Conditionally:* under the labelled hypothesis (Cmp) of §6.4, which includes the existence of a coherent geometric index framing so related, the geometric realization is $X_0$.
* **Theorem D (local Nahm-pole Gauss map; §7).** Consider the reduced finite-dimensional $\zeta$-instanton setting: target $\mathbb C^n$, holomorphic superpotential $S$, and a Nahm pole at $y=0$, as in [45].
  * $\operatorname{Hess}\operatorname{Re}S$ anticommutes with $J$, and the $y$-flow of Jacobi fields is symplectic.
  * The pole-regular Jacobi fields form a Lagrangian $\Lambda_x(y)$, and $\Lambda_x(y)\to E_+$ as $y\downarrow0$, uniformly on compact families.
  * Hence the Lagrangian Gauss map of every compact family is null-homotopic by an explicit homotopy.
  * This is a *local* statement. It does not construct a Floer polarization or a coherent index framing, and it is not used for the AH-fold categories.
* **Theorem E (synthesis; §8).** The two realizations are $X_0$ and $X_1$. The vector-bundle and $\mathrm{Top}$-related framings give $X_0$ (unconditional), and the HW geometric framing gives $X_0=\Sigma^\infty h(\bar B)$ under (Cmp). The exotic class is $\operatorname{coker}J$ in degree $2$. A heuristic remark on fold crossing is kept separate (Remark 4.5).

### 1.3 What is new, what is not, and credits

* *Prior HW input, which we use and do not claim.*
  * The model category $\mathcal C_{\rm mod}$, its smooth corner structure, the comparison isomorphism and the vector-framed realization $X_0$ are in [42, Thm. 1, Rem. 4.2–4.4] and [43, Thm. D].
  * The triangular reduction identifying the full and reduced index bundles on actual trajectories is [42, Prop. 2, §5]. So is the remark that the HW linearizations frame the interiors, uniquely up to homotopy once orientations are fixed [42, Rem. 4.3].
  * rStation math_52 [46, §7.3] already treats the quadrupole sector at the level of interval framings. There, the four compatibility conditions on the eight interval frame values have rank three, with exactly $32$ of $256$ assignments compatible, and $\mathrm{Sq}^2$ vanishes. Our level-1 computation ($\operatorname{rank}\partial^{\rm sq}=3$, $\ker\partial^{\rm sq}$ of size $32$; verify.py §4b) is the same incidence computation, and we credit it there.
* *General theory, which we use and do not claim.*
  * The reframing formalism is due to Cohen–Jones–Segal [2, 3] and Cohen [1, Prop. 5]. The obstruction-theoretic treatment of framings of the cube flow category is Lipshitz–Sarkar's [7], and the $\mathbb Z/2$ framing values of intervals are those of Lobb–Orson–Schütz [10, Defs. 3.1–3.3, 3.12].
  * Twisting Morse flow categories by stable spherical fibrations, with realization a Thom spectrum, is proved by Blakey–Bonciocat [14, §2.1, Prop. B.7], including the role of $J$ [14, Rem. 4.5]. The vector-bundle case is in Bonciocat [12] and Côté–Kartal [13].
  * Framing-dependent Steenrod squares already occur in Lagrangian Floer homotopy [14, Ex. 1.3]. Tangential-structure torsors are in Porcelli–Smith [16, Ex. 2.27].
  * The detection of $\eta^2$ by $KO$ is classical [24].
* *New.* The HW-specific statements are new:
  * the level-2 computation $\Gamma_2=\mathbb Z/2$ for these categories and the classification of their spherical reframings (Theorem A(3)–(4));
  * the proof that the invariant is the sum of square classes, with a corrected argument (Lemma 4.3);
  * the separation of the spherical class from all vector-bundle and $\mathrm{Top}$ framings;
  * the identification of exactly which standard invariants see it (Theorem B).

  We did not find an exact prior statement of this classification for HW categories.
* *Scope of the analytic part.* Theorem C states only existence and uniqueness of homotopy classes. The identification of the actual HW index framing at corners, where the HW moduli lack a natural smooth corner structure [42, Rem. 4.4], is hypothesis (Cmp). Theorem D is local and finite-dimensional. The status table is §10.
* *Translation invariance.* All perturbations are $s$-independent ([41, 42]), and moduli spaces are honest quotients by $\mathbb R$.

## 2. The categories

We use the conventions of [41, 42]. Deformations $\xi$ of the gauge-fixed background satisfy an $s$-independent equation $\partial_s\xi=F_\varepsilon(\xi;\mu)$. Locally all solutions lie on a five-dimensional centre manifold, with reduced field $\dot z=f_\varepsilon(z)$ on $\mathbb R^5$ [40, 41]. The objects are the KW solutions in the isolating neighbourhood. The grading is the reduced index $\mu$, i.e. the number of unstable directions among the five small eigenvalues.

| sector | source | objects ($\mu$) | morphism spaces |
|---|---|---|---|
| $\Sigma_{\rm iso}$ (isotropic, above fold) | [37, Thms. C–D] | $k_+(1),k_-(0)$ | one point |
| $\Sigma_{V_4}$ (Klein, triaxial) | [38, Thm. B] | $k_+(1),k_-(0)$ | one point |
| $\Sigma_2$ ($SU(2)^2$, $V_4$ factors) | [38, Thm. C] | $k_{++}(2),k_{+-},k_{-+}(1),k_{--}(0)$ | 4 points, 1 interval |
| $\Sigma_Q$ (quadrupole, below fold) | [41, Thm. C], [42, Thm. 1] | $P_a^\pm$, $\mu=a\in\{1,2,3,4\}$ | 12 points, 8 intervals, 4 squares |
| $\mathcal C_{\rm PDE}$ | [43, Thm. D(1)] | as $\Sigma_Q$ | as $\Sigma_Q$ |
| $\Sigma_H$ (height, below fold) | [41, Thm. C′], [42, Thms. 1, 3(4)] | $P_4,P_1$ | $\overline{\mathcal M}(P_4,P_1)\cong S^2$ |
| $\Sigma_E$ ($h_{\beta,e}$, above fold) | [42, Thm. 3(3)] | $k_+(4),k_-(1)$ | none |

**The quadrupole category $\Sigma_Q$.**
* There is one point in each $\mathcal M(P_a^s,P_{a-1}^t)$ and one closed interval in each $\overline{\mathcal M}(P_a^s,P_{a-2}^t)$.
* Each $\overline{\mathcal M}(P_4^s,P_1^t)$ is a closed square. Its four faces are $\overline{\mathcal M}(P_3^u,P_1^t)\times\mathcal M(P_4^s,P_3^u)$ and $\mathcal M(P_2^v,P_1^t)\times\overline{\mathcal M}(P_4^s,P_2^v)$, for $u,v\in\{\pm\}$ [41, Thm. C3], [42, Thm. 1(1)].
* The Morse complex is $d_4=d_2=\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)$, $d_3=\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)$, with homology $\mathbb Z[1]\oplus\mathbb Z[4]$ [41, Thm. C4] (verify.py §4).

**Smooth structure and model framing.**
* The smooth corner structure on $\Sigma_Q$ and $\Sigma_H$ is transported from the smooth Morse–Smale model $\mathcal C_{\rm mod}$ on $S^3$ of [42, Thm. 1]. It is *not* claimed to agree with the natural interior structure of the HW moduli [42, Rem. 4.4].
* The comparison isomorphism $\Phi$ of topological flow categories is induced by an orbit equivalence, through the Hausdorff topology on broken trajectories [42, §4.2], [36].
* With any framing of $\mathcal C_{\rm mod}$ ("model framing"), the realization is $X_0$ [42, Thm. 1(4)]. The same holds for $\mathcal C_{\rm PDE}$ with the transported structure [43, Thm. D(1)].
* The Conley index of the isolating ball is $h(\bar B)=S^1\vee S^4$ in all settings near the fold [41, Thm. E1], [43, Thm. D(2)].

*Scope.* We do not cover the complete-space category above the fold without $J$-breaking perturbation, which has no transverse category [39, Thm. D]. We do not cover global categories or knots. The categories $\Sigma_N$ for $N\ge3$ appear only in the conditional Remark 4.6.

## 3. Reframings: definitions and three lemmas

### 3.1 $\mathbb S$-orientations and reframings

Fix a topological group $G$ with a weak equivalence $BG\simeq BGL_1(\mathbb S)$, and a continuous homomorphism $j:O\to G$ realizing the stable $J$-homomorphism. Such a pair exists: replace $O\to GL_1(\mathbb S)$ by a map of group-like topological monoids and apply Milnor's group-model construction. We use only these facts: $\pi_k(G)=\pi_k^s$ for $k\ge1$, $\pi_0(G)=\{\pm1\}$, and $j_*:\pi_k(O)\to\pi_k^s$ is the $J$-homomorphism. For $k=0,1,2$:

| $k$ | $\pi_k(O)$ | $\pi_k^s$ | $j_*$ |
|---|---|---|---|
| 0 | $\mathbb Z/2$ | $\{\pm1\}$ | iso |
| 1 | $\mathbb Z/2$ | $\mathbb Z/2\langle\eta\rangle$ | iso |
| 2 | $0$ | $\mathbb Z/2\langle\eta^2\rangle$ | zero; cokernel $\mathbb Z/2$ |

(verify.py §1 records this table; it is known input, not a computation. It also checks $|\mathrm{im}\,J|=24,240,504$ in degrees $3,7,11$ from Bernoulli denominators.)

Let $(\mathcal C,u)$ be a framed flow category in the sense of [7, §3] and [2], with a framing $u$. Equivalently, following [1, Def. 8] with $E=\mathbb S$, $u$ is a coherent family of $\mathbb S$-Thom classes of the stable normal bundles of the $\overline{\mathcal M}(a,b)$.

**Definition 3.1.**
* A *coherent $G$-cocycle* on $\mathcal C$ is a family of continuous maps $g_{ab}:\overline{\mathcal M}(a,b)\to G$ such that
$$g_{ac}\big|_{\overline{\mathcal M}(b,c)\times\overline{\mathcal M}(a,b)}=g_{bc}\cdot g_{ab}$$
on every face.
* The *$G$-reframing* $u\cdot g$ is the coherent family of $\mathbb S$-Thom classes obtained by letting $g$ act on $u$ pointwise. This is Cohen's $\Phi:\mathcal C\to GL_1(\mathbb S)$ [1, (17)].
* An *$O$-reframing* is the case $g=j\circ h$ with $h$ a coherent $O$-cocycle. These are exactly the changes of framing in the sense of [7, 10, 12], i.e. changes of the vector-bundle trivializations of the normal bundles of fixed neat embeddings. *$\mathrm{Top}$-reframings* are defined in the same way, with $\mathrm{Top}=\operatorname{colim}\mathrm{Top}(n)\to G$.
* A *reorientation* is $g_{ab}\equiv\sigma_b\sigma_a^{-1}$ with $\sigma:\mathrm{Ob}\to\{\pm1\}\subset G$ constant.

We classify reframings only up to homotopy through coherent cocycles, i.e. we compute $\pi_0$ of the space of coherent cocycles modulo reorientation. Nothing is claimed about higher homotopy groups of that space.

The *realization* $|\mathcal C|_{u\cdot g}$ is the CJS spectrum, built by the Pontryagin–Thom construction of [1, (16)] with $u$ replaced by $u\cdot g$. Its cellular chain complex is the Morse complex with signs $\pi_0(u\cdot g)$ on the points [1, Thm. 4], [7].

**Lemma 3.2 (invariance).**
1. If $g\simeq g'$ through coherent $G$-cocycles, then $|\mathcal C|_{u\cdot g}\simeq|\mathcal C|_{u\cdot g'}$.
2. A reorientation changes the realization by an isomorphism, namely sign changes of cells.

*Proof.*
1. The realization of $(\mathcal C,u\cdot g_t)_{t\in[0,1]}$ is a CW spectrum over $[0,1]$, with cells and attaching maps depending continuously on $t$. Its fibres at $0$ and $1$ are therefore homotopy equivalent. This is the argument for independence of framing choices in [7, §3], [2].
2. Replace the cell $e_a$ by $\sigma_ae_a$. ∎

### 3.2 Normalization for categories of dimension $\le2$

Assume every morphism space of $\mathcal C$ is a finite disjoint union of *points*, closed *intervals* and closed *squares*, the last two in dimensions $1$ and $2$, and that no morphism space has dimension $\ge3$. This holds for $\Sigma_{\rm iso}$, $\Sigma_{V_4}$, $\Sigma_2$, $\Sigma_Q$ and $\mathcal C_{\rm PDE}$; $\Sigma_H$ is treated separately in §4.3. Define three $\mathbb F_2$-linear maps.
* $\partial^{\rm pt}:\mathbb F_2^{\{\text{points}\}}\to\mathbb F_2^{\{\text{intervals}\}}$ sends a point $m$ to the sum of the intervals that have $m$ as a factor of a boundary point.
* $\partial^{\rm sq}:\mathbb F_2^{\{\text{intervals}\}}\to\mathbb F_2^{\{\text{squares}\}}$ sends an interval to the sum of the squares that contain it as a factor of a face.
* $\delta^0$ is the coboundary from object signs to $\mathbb Z/2$-valued functors on components.

Put
$$\Gamma_0=\frac{\{\mathbb Z/2\text{-valued functors on }\pi_0\mathcal C\}}{\operatorname{im}\delta^0},\qquad \Gamma_1=\frac{\ker\partial^{\rm sq}}{\operatorname{im}\partial^{\rm pt}},\qquad \Gamma_2=\operatorname{coker}\partial^{\rm sq}.$$
A functor on $\pi_0\mathcal C$ assigns $\pm1$ to each component, multiplicatively under composition. One has $\partial^{\rm sq}\circ\partial^{\rm pt}=0$ (verify.py §4).

**Proposition 3.3 (normalization).** Let $g$ be a coherent $G$-cocycle on $\mathcal C$ as above, and assume $\Gamma_0=\Gamma_1=0$.
1. After a reorientation and a homotopy through coherent cocycles, $g\equiv1$ on all points and intervals. Then each square $Q$ carries a class $c_Q=[g_Q]\in\pi_2(G,1)=\pi_2^s$, defined by $g_Q:(Q,\partial Q)\to(G,1)$.
2. The class $\bar c=[(c_Q)_Q]\in\Gamma_2\otimes\pi_2^s$ is unchanged by the residual homotopies that keep points and intervals at $1$ at both ends.
3. If $g=j\circ h$ is an $O$-reframing, then after reorientation $g$ is homotopic to the trivial cocycle. The same holds for $\mathrm{Top}$-reframings.

*Proof.*
1. *Level 0.* $\pi_0(g)$ is a $\pi_0(G)=\mathbb Z/2$-valued functor on $\pi_0\mathcal C$. Since $\Gamma_0=0$ it equals $\delta^0\sigma$, and after reorienting by $\sigma$ all values lie in the identity component $G_1$.

   *Level 1.* $G_1$ is path-connected.
   * Choose paths in $G_1$ from each $g_m$ ($m$ a point) to $1$, and extend these homotopies over the intervals and then over the squares. This is possible because $(I,\partial I)$ and $(Q,\partial Q)$ are cofibrations, and the boundary values are prescribed by the coherence identity.
   * Now $g_m=1$, so each interval defines a class $c_I\in\pi_1(G)$. On $\partial Q$ the cocycle is the concatenation of the four face paths, each of the form $g_I\cdot1$ or $1\cdot g_I$, and it extends over $Q$. Hence $\sum_{I\subset\partial Q}c_I=0$, so $(c_I)\in\ker\partial^{\rm sq}$.
   * Moving a point value once around a loop $\gamma\in\pi_1(G)$, and correcting the adjacent intervals as before, changes $c$ by $\partial^{\rm pt}(\gamma)$. Since $\Gamma_1=0$ we may arrange $c=0$. Then homotope each $g_I$ to $1$ rel $\partial I$, and extend over the squares.
2. A homotopy that is $1$ on points and intervals at both ends restricts on each interval to a loop in $\mathrm{Map}((I,\partial I),(G,1))$, i.e. to a class in $\pi_2(G)$. Its effect on the squares is $\partial^{\rm sq}$ of these classes. This is the claim, because $\pi_2^s=\mathbb Z/2$.
   (Homotopies that move points or intervals at intermediate times might a priori impose further identifications. They do not affect the invariant $\sum_Qc_Q$ used below, which is detected by the realization: Lemma 4.3 and Lemma 3.2.)
3. The same normalization runs inside $O$, since $j_*$ is an isomorphism on $\pi_0$ and $\pi_1$. The square classes then lie in $\pi_2(O)=0$, so $g_Q\simeq1$ rel $\partial Q$. For $\mathrm{Top}$ use $\pi_i(\mathrm{Top}/O)=0$ for $i\le2$ [29], so that $\pi_i(O)\to\pi_i(\mathrm{Top})$ is an isomorphism for $i\le1$ and $\pi_2(\mathrm{Top})=0$. ∎

The method is that of [7] for framings of the cube flow category, where the obstruction groups vanish because the cube is contractible. LOS's framing value $f\in\mathbb Z/2$ of an interval [10, Defs. 3.1–3.3] is the level-1 datum $c_I\in\pi_1(O)$.

### 3.3 The local modification lemma

**Lemma 3.4 (disc modification).** Let $a,b$ be objects such that $\overline{\mathcal M}(a,b)$ is not a factor of a face of any other morphism space, i.e. $a$ is maximal and $b$ minimal among objects connected to them. Let $k=|a|-|b|-1$. Let $g$ be the cocycle that is $1$ everywhere except on one component $Q\subset\overline{\mathcal M}(a,b)$. On $Q$, $g$ is a map $(Q,Q\setminus D)\to(G,1)$ for a closed disc $D\subset\mathrm{int}\,Q$, with class $\gamma\in\pi_k(G)=\pi_k^s$.
1. $g$ is coherent.
2. $|\mathcal C|_{u\cdot g}$ is obtained from $|\mathcal C|_u$ by replacing the attaching map $\varphi_a$ of the cell $e_a$ by $\varphi_a+\iota_b\circ\gamma$. Here $\iota_b:S^{|b|}\to|\mathcal C|_u^{(|a|-1)}$ is the inclusion of the bottom cell $e_b$, and the sum uses the pinch on $\partial e_a$.

The same holds for several such components at once, with disjoint discs, by applying the argument to each.

*Proof.*
1. Coherence is vacuous: $Q$ is not a face, and its own faces lie in $Q\setminus D$, where $g=1$.
2. In the CJS/LS construction the component of $\varphi_a$ through $e_b$ is the Pontryagin–Thom collapse onto the Thom space of the normal bundle of $\overline{\mathcal M}(a,b)$, followed by the $\mathbb S$-Thom class $u$ [1, (16)], [7, §3].
   * Replacing $u$ by $u\cdot g$ changes this composite only on the collapse of a tubular neighbourhood of $D$.
   * There the old composite is the trivial one, $S^{N+k}\to\Sigma^N(D/\partial D)\to S^N$ through the framing. The new one is the adjoint of $g|_D$, i.e. the class $\gamma$.
   * A map that agrees with the old one off a ball and differs on the ball by $\gamma$ is homotopic to the old map plus $\gamma$ via the pinch.
   * Since $b$ is minimal, $e_b\cup\{*\}$ is a sphere subcomplex and the sum lands there. ∎

A normalized cocycle with $g_Q:(Q,\partial Q)\to(G,1)$ is homotopic rel $\partial Q$, by collar compression, to one that is $1$ outside a disc. So Lemma 3.4 applies to normalized cocycles via Lemma 3.2(1).

## 4. Theorem A: classification of realizations

### 4.1 Statement

**Theorem A.**
1. *($\Sigma_{\rm iso},\Sigma_{V_4},\Sigma_2$.)* For every $G$-reframing, the realization is contractible.
2. *($\Sigma_E$.)* For every $G$-reframing, the realization is $X_0$.
3. *($\Sigma_Q$, $\mathcal C_{\rm PDE}$.)*
   * $\Gamma_0=0$, $\Gamma_1=0$ and $\Gamma_2=\mathbb Z/2$, and the invariant is the sum of the square classes.
   * For every $G$-reframing $g$, normalized as in Proposition 3.3, $|\mathcal C|_{u\cdot g}\simeq S^1\cup_{\alpha(g)}e^4$ with
$$\alpha(g)=\Big(\sum_Qc_Q\Big)\,\eta^2\in\pi_2^s .$$
   * Both values occur. So the homotopy classes of $G$-reframings modulo reorientation form a set with exactly two elements, realizing $X_0$ and $X_1$.
   * Every $O$- or $\mathrm{Top}$-reframing is, up to reorientation, homotopic to the trivial one, and realizes $X_0$.
4. *($\Sigma_H$.)* $G$-reframings modulo reorientation and homotopy are in bijection with $\pi_2^s=\mathbb Z/2$, realizing $X_0$ and $X_1$. $O$- and $\mathrm{Top}$-reframings are trivial and realize $X_0$.
5. *(No $\nu$-twists.)* No realization in 1–4 is a suspension of $S^0\cup_{k\nu}e^4$ with $k\not\equiv0\bmod24$, or contains such a subquotient on two cells. The group $[S^1\vee S^4,BGL_1\mathbb S]\cong\mathbb Z/2\times\mathbb Z/24$ does not classify the reframings of these categories.

### 4.2 Proofs of 1, 2, 5

*1.* Let $g$ be a $G$-reframing. The cellular chain complex of $|\mathcal C|_{u\cdot g}$ is the Morse complex with signs $\varepsilon\cdot s$, where $s$ are the original signs and $\varepsilon=\pi_0(g)$ is a $\mathbb Z/2$-valued functor.
* In $\Sigma_{\rm iso}$ and $\Sigma_{V_4}$ the complex is $\mathbb Z\xrightarrow{\pm1}\mathbb Z$.
* In $\Sigma_2$ ([38, Thm. C]) the functor condition on the interval $\overline{\mathcal M}(k_{++},k_{--})$ says that the two broken configurations keep opposite total sign. So $d^2=0$ persists, and the four $\pm1$ entries form an acyclic complex. Over $\mathbb F_2$ this is the statement that sign functors on the square poset are coboundaries (verify.py §6, $N=2$; also $N=3,4$ for Remark 4.6).

A finite connective CW spectrum with $\tilde H_*(\,\cdot\,;\mathbb Z)=0$ is contractible, by the Hurewicz and Whitehead theorems.

*2.* There are no morphisms, hence no compositions. A $G$-cocycle is empty, and only reorientations act. The realization is the two-cell wedge [42, Thm. 3(3)].

*5.*
* In every case the cells lie in degrees $\{0,1\}$, $\{0,1,2\}$, $\{1,4\}$ or $\{1,2,3,4\}$, so no two cells differ in degree by $4$. Moreover every realization is $*$, $X_0$ or $X_1$ by 1–4.
* The Thom spectra over $S^1\vee S^4$ have three cells, in degrees $0,1,4$ before suspension, whereas $X_0$ has two homology generators.
* The correct twisting base is the classifying space of the flow category: by [3], $B\mathcal C_{\rm mod}\simeq S^3$, and $[S^3,BGL_1\mathbb S]=\pi_2^s=\mathbb Z/2$. Our computation of $\Gamma_0,\Gamma_1,\Gamma_2$ does not use [3], and it reproduces $H^{k+1}(S^3;\pi_k^s)$ for $k=0,1,2$ (verify.py §4). ∎

### 4.3 Proof of 3 and 4

*Computation of the $\Gamma_k$ (verify.py §4, genuine $\mathbb F_2$ computations).* From the incidences of §2:
* The $\mathbb Z/2$-functors on the $24$ components form a $7$-dimensional space, equal to the image of the $8$ object signs (the global sign acts trivially). So $\Gamma_0=0$.
* $\ker\partial^{\rm sq}$ has dimension $5$, i.e. $32$ elements (this incidence computation is also in [46, §7.3]). $\operatorname{im}\partial^{\rm pt}$, from the $12$ points, has dimension $5$ and lies in $\ker\partial^{\rm sq}$. So $\Gamma_1=0$.
* $\partial^{\rm sq}$ has rank $3$, and each interval lies in exactly two squares. Its image is exactly $\{c\in\mathbb F_2^4:\sum_Qc_Q=0\}$ (verify.py §4b). So $\Gamma_2=\mathbb Z/2$, detected by $\sum_Qc_Q$.

A negative control in verify.py shows that a corrupted incidence would change $\Gamma_2$.

**Lemma 4.1 (only two candidates).** For every $G$-reframing $g$ of $\Sigma_Q$, $|\mathcal C|_{u\cdot g}\simeq S^1\cup_\alpha e^4$ for some $\alpha\in\pi_2^s$.

*Proof.* By $\Gamma_0=0$ and Lemma 3.2(2), the Morse complex of $u\cdot g$ is isomorphic to that of $u$, with free homology $\mathbb Z[1]\oplus\mathbb Z[4]$. Let $Y=|\mathcal C|_{u\cdot g}$. It is $0$-connected, and the Hurewicz map gives $S^1\to Y$ inducing an isomorphism on $H_1$. The cofibre $Y'$ has $\tilde H_*=\mathbb Z[4]$, so $Y'\simeq S^4$ by Hurewicz and Whitehead. Hence $Y$ is the cofibre of some $\alpha:S^3\to S^1$, i.e. $\alpha\in\pi_2^s$. ∎

**Lemma 4.2 (retraction criterion).** $S^1\cup_\alpha e^4\simeq S^1\vee S^4$ iff there is a map $r:S^1\cup_\alpha e^4\to S^1$ inducing an isomorphism on $H_1$.

*Proof.* If $\alpha=0$, the collapse onto the first wedge summand is such a map. Conversely, $r$ restricts to $\pm1$ on $S^1$, so $r\circ\alpha=\pm\alpha$ must be null. ∎

**Lemma 4.3 (the invariant).** Let $g$ be a normalized $G$-reframing of $\Sigma_Q$, and write $c_{st}\in\pi_2^s=\mathbb Z/2$ for the class of the square $\overline{\mathcal M}(P_4^s,P_1^t)$. Then $|\mathcal C|_{u\cdot g}\simeq X_0$ if $\sum_{s,t}c_{st}=0$, and $|\mathcal C|_{u\cdot g}\simeq X_1$ if $\sum_{s,t}c_{st}=1$. Equivalently, $\alpha(g)=\big(\sum_{s,t}c_{st}\big)\eta^2$.

*Proof.* Put $X=|\mathcal C|_u$ and $X'=|\mathcal C|_{u\cdot g}$. By [42, Thm. 1(4)], $X\simeq X_0$ for the model framing $u$. All maps below are maps of spectra, so composition is bilinear.

*Step 1 (same skeleton).* Apply Lemma 3.4 to the four squares, with $P_4^s$ maximal and $P_1^t$ minimal. Then $X$ and $X'$ have the same $3$-skeleton $X^{(3)}$, and the attaching maps $\varphi_s,\varphi'_s:S^3\to X^{(3)}$ of the $4$-cells $e_{P_4^s}$ satisfy
$$\varphi'_s=\varphi_s+\textstyle\sum_t\iota_t\circ c_{st}\eta^2,\qquad s\in\{+,-\},$$
where $\iota_t:S^1\to X^{(1)}$ is the inclusion of the bottom cell $e_{P_1^t}$.

*Step 2 (a reference retraction).* Since $X\simeq S^1\vee S^4$, Lemma 4.2 gives a map $r:X\to S^1$ inducing an isomorphism on $H_1$. Its restriction to $X^{(3)}$ satisfies $r\circ\varphi_s\simeq0$ for **both** $s$, because $r$ is defined on all of $X$. Moreover $r\circ\iota_t$ has degree $\pm1$ for both $t$. Indeed $H_1=\mathbb Z^2/\langle(1,-1)\rangle$, an isomorphism $H_1\to\mathbb Z$ is $\pm(x+y)$, and $P_1^\pm$ both map to $\pm1$ (verify.py §4). Hence
$$r\circ\varphi'_s=a_s\,\eta^2,\qquad a_s:=\textstyle\sum_tc_{st}\in\mathbb Z/2 .$$
In general $r$ itself does **not** extend over $X'$. For instance, if $c_{++}=c_{-+}=1$ and the other classes vanish, then $\sum c_{st}=0$ but $a_+=a_-=1$, so both obstructions equal $\eta^2$ (verify.py §4b). The first version of this paper overlooked this.

*Step 3 (all candidate retractions on the $3$-skeleton).* Let $r':X^{(3)}\to S^1$ be any map inducing an isomorphism on $H^1(X^{(3)};\mathbb Z)=\mathbb Z$. After a sign change, $\delta:=r'-r|_{X^{(3)}}$ is zero on $H^1$.
* The Atiyah–Hirzebruch filtration of $[X^{(3)},S^1]$ has graded pieces that are subquotients of $H^1(X^{(3)};\mathbb Z)$, $H^2(X^{(3)};\pi_1^s)$ and $H^3(X^{(3)};\pi_2^s)$, and $H^2(X^{(3)};\mathbb F_2)=0$ (verify.py §4). So $\delta$ restricts to zero on $X^{(2)}$.
* By the cofibre sequence $X^{(2)}\to X^{(3)}\xrightarrow{q}X^{(3)}/X^{(2)}=S^3_+\vee S^3_-$, there is $\gamma=(\gamma_+,\gamma_-)\in(\pi_2^s)^2$, indexed by the $3$-cells $P_3^u$, with $\delta=\gamma\circ q$.
* Conversely, every such $\gamma$ gives a map $r+\gamma\circ q$ with the same $H^1$-class.

So the maps $X^{(3)}\to S^1$ in question are, up to sign, exactly the $r_\gamma:=r+\gamma\circ q$, $\gamma\in(\pi_2^s)^2$.

*Step 4 (obstructions).* The composite $q\circ\varphi'_s:S^3\to S^3_+\vee S^3_-$ has degrees given by the cellular boundary $d_4(P_4^s)$, because the modification terms land in $X^{(1)}$, which $q$ kills. Since $d_4\equiv\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\bmod2$,
$$r_\gamma\circ\varphi'_s=\big(a_s+\gamma_++\gamma_-\big)\,\eta^2\qquad(s=\pm).$$
The map $r_\gamma$ extends over $X'=X^{(3)}\cup_{\varphi'_+\vee\varphi'_-}(e^4\vee e^4)$ iff both obstructions vanish, i.e. iff $\gamma_++\gamma_-=a_+=a_-$. The shifts $(\gamma_++\gamma_-,\gamma_++\gamma_-)$ fill exactly the diagonal of $(\mathbb Z/2)^2$.

*Conclusion.*
* If $\sum_{s,t}c_{st}=a_++a_-=0$, then $a_+=a_-$. Choose $\gamma=(a_+,0)$; then $r_\gamma$ extends over $X'$ and induces an isomorphism on $H_1$, so $X'\simeq X_0$ by Lemmas 4.1–4.2. In the example of Step 2, $\gamma=(\eta^2,0)$.
* If $\sum_{s,t}c_{st}=1$, then $a_+\neq a_-$, so no $r_\gamma$ extends. By Step 3, no map $X'\to S^1$ induces an isomorphism on $H_1$. So $X'\not\simeq X_0$, and $X'\simeq X_1$ by Lemma 4.1.

verify.py §4b checks this criterion for all $16$ vectors $(c_{st})$. ∎

*Second argument for the case $\sum c_{st}=0$.* The image of $\partial^{\rm sq}$ is exactly $\{c:\sum_Qc_Q=0\}$ (verify.py §4b). By the interval homotopies in the proof of Theorem A(3) below, a normalized $g$ with $\sum c_Q=0$ is homotopic through coherent cocycles to the trivial cocycle. Then $X'\simeq X\simeq X_0$ by Lemma 3.2(1). This gives the parity-zero case independently of Steps 3–4. The parity-one case needs Steps 3–4, or Theorem B applied to Lemma 4.1.

*Proof of Theorem A(3).*
* By Proposition 3.3 every $g$ normalizes, and by Lemma 4.3 the realization is determined by $\sum c_Q$.
* Both values occur: take $g$ supported in a disc of one square, with class $\eta^2$ (Lemma 3.4).
* Two normalized cocycles with different $\sum c_Q$ have non-equivalent realizations (Lemma 4.3, or Theorem B), so they are not homotopic (Lemma 3.2).
* Conversely, suppose $\sum c_Q=\sum c'_Q$. Then $c-c'\in\operatorname{im}\partial^{\rm sq}$. Move each interval value once around a loop in $\mathrm{Map}((I,\partial I),(G,1))$ representing the required class in $\pi_2(G)$, and extend over the squares by homotopy extension. This changes $c$ by any prescribed element of $\operatorname{im}\partial^{\rm sq}$. Two maps $(Q,\partial Q)\to(G,1)$ with the same class in $\pi_2(G)$ are homotopic rel $\partial Q$. So the two cocycles are homotopic, and there are exactly two classes.
* $O$- and $\mathrm{Top}$-reframings are handled by Proposition 3.3(3).
* $\mathcal C_{\rm PDE}$ has the same topological category and the same transported framed structure [43, Thm. D(1)], so the same proof applies. ∎

*Proof of Theorem A(4).*
* $\overline{\mathcal M}(P_4,P_1)\cong S^2$ is not a face, so any $g:S^2\to G$ is coherent. We have $[S^2,G]=\pi_0(G)\times\pi_2(G)$, where the $\pi_0$-part is a reorientation and the $\pi_2$-part may be supported in a disc.
* By Lemma 3.4, $|\mathcal C|_{u\cdot g}=S^1\cup_{\alpha_0+[g]}e^4$, where $\alpha_0=0$ is the class of the framed $S^2$ [42, Thm. 1(4)].
* For $O$- and $\mathrm{Top}$-reframings, $[g]$ lies in the image of $\pi_2(O)=\pi_2(\mathrm{Top})=0$. ∎

**Remark 4.4 (the model's classifying space).** For $\Sigma_Q$ the morphism data are those of the Morse–Smale model on $S^3$ [42, Thm. 1(2)]. For a model framing, [1, Prop. 5] and [14, §2.1, Prop. B.7] identify the $G$-reframed realization with the Thom spectrum $\Sigma(S^3)^\phi$ for $\phi:S^3\to BGL_1\mathbb S$. For $\phi=\eta^2$ the Thom spectrum is $S^0\cup_{\eta^2}e^3$. This agrees with Theorem A(3), which we prove without these results. The contribution of Theorem A is the explicit identification of the classifying data from the HW morphism manifolds and of the invariant $\sum c_Q$, not the Thom-spectrum mechanism.

**Remark 4.5 (crossing the fold; heuristic only).** Below the fold ($\Sigma_H$) both $X_0$ and $X_1$ are realizable by reframings. Above the fold ($\Sigma_E$) only $X_0$ is, since there is no morphism space to carry a twist. If a reframing family were continuous in $(\bar\nu,\varepsilon)$ across the fold and compatible with the Conley continuation of $\bar B$ [42, Thm. 3(6)], one would expect it to realize $X_0$ on both sides. We do not define or construct such families, and nothing in the paper depends on this remark.

**Remark 4.6 (conditional: $\Sigma_N$, $N\ge3$).** rStation math_52 [46, Remark 2.2] records that decoupling identifies the local $SU(2)^N$ category, $N\ge3$, with the Lipshitz–Sarkar cube flow category $\mathcal C_C(N)$, as a routine extension of the case $N=2$; no detailed proof is given there. *If* this identification holds, the argument of Theorem A(1) applies verbatim: sign functors are coboundaries for $N\le4$ (verify.py §6), and acyclicity holds for every sign functor. So every $G$-reframing is then contractible.

## 5. Theorem B: what detects $X_1$

**Theorem B.** Let $C_\alpha=S^0\cup_\alpha e^3$ with $\alpha\in\{0,\eta^2\}$, so that $X_i=\Sigma C_{\alpha_i}$.
1. $C_0$ and $C_{\eta^2}$ have isomorphic integral homology and cohomology, with any coefficients. Every stable primary cohomology operation *of positive degree*, with coefficients in $\mathbb Z$ or in $\mathbb F_p$ for any prime $p$, is zero on both. So their cohomologies are isomorphic as modules over the Steenrod algebra at every prime.
2. $KU_n(C_0)\cong KU_n(C_{\eta^2})\cong\mathbb Z$ for every $n$. As $KU_*$-modules both are free on one generator in degree $0$ and one in degree $3$.
3. $KO_2(C_0)=\mathbb Z/2$ and $KO_2(C_{\eta^2})=0$. Equivalently, $KO_3(X_0)=\mathbb Z/2$ and $KO_3(X_1)=0$. In Adams' terms, $\eta^2$ is detected by the $d_{\mathbb R}$-invariant, i.e. by its $KO$-Hurewicz image $\eta^2\in KO_2=\mathbb Z/2$ [24]. $KO_n$ agrees on the two for $n=0,1$.
4. $\eta^2$ has Adams filtration $2$ and is represented by $h_1^2$. It is detected by the secondary operation attached to the Adem relation $\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^3\mathrm{Sq}^1$ [23], [25], and by no primary operation of positive degree.
5. *(Counterfactual $\nu$.)* On $S^0\cup_{k\nu}e^4$, $\mathrm{Sq}^4$ is nonzero iff $k$ is odd, and $P^1$ ($p=3$) is nonzero iff $3\nmid k$. The model case $k=1$ is $\Sigma^{-4}\mathbb{HP}^2$, with $\mathrm{Sq}^4u=u^2$ and $P^1u=u^2\bmod3$. By Theorem A(5) these spectra do not arise.

*Proof.*
1. The cellular chain complex is $\mathbb Z$ in degrees $0,3$ with zero differential in both cases.
   * A stable mod-2 operation $\theta:H^0\to H^3$ is a combination of $\mathrm{Sq}^3=\mathrm{Sq}^1\mathrm{Sq}^2$ and $\mathrm{Sq}^2\mathrm{Sq}^1$ (computed from the Adem relations, verify.py §3). Both factor through $H^1=0$ or $H^2=0$.
   * For $p$ odd, $\mathcal A_p$ is zero in degrees $2,3$ (verify.py §3).
   * With integral coefficients, the degree-3 operations are generated by $\beta\mathrm{Sq}^2\rho$, which factors through $H^2=0$.
   * Operations of positive degree other than $3$ vanish for degree reasons. (Operations of degree $0$, i.e. multiplication by scalars, are of course not zero; this is the reason for the restriction to positive degree.)
2. $\eta$ acts by $0$ on $KU_*$, since $KU_1=0$. So $\alpha_*=0$, and the long exact sequence splits into $0\to KU_n\to KU_n(C_\alpha)\to KU_{n-3}\to0$. Exactly one of the two outer terms is $\mathbb Z$ and the other is $0$. An extension of free modules splits.
3. The cofibre sequence $S^2\xrightarrow\alpha S^0\to C_\alpha\to S^3$ gives
$$KO_0\xrightarrow{\alpha}KO_2\to KO_2(C_\alpha)\to KO_{-1}=0 .$$
   Multiplication by $\eta^2:KO_0=\mathbb Z\to KO_2=\mathbb Z/2$ is onto, so $KO_2(C_{\eta^2})=0$, while $KO_2(C_0)=\mathbb Z/2$. (verify.py §2 tabulates $n=0,\dots,7$ from the encoded coefficients and $\eta$-action.)
4. This is standard [23, 25].
5. Use the Cartan formula on $H^*(BT^1)$ with $u=-x^2$: $\mathrm{Sq}(x^2)=(x+x^2)^2$ and $P(x^2)=(x+x^3)^2$ (verify.py §3). The statements for $k\nu$ follow from $\mathrm{Sq}^4$ and $P^1$ detecting the $2$- and $3$-primary generators of $\pi_3^s=\mathbb Z/8\oplus\mathbb Z/3$, and from linearity of functional operations in $k$ [25]. ∎

**Remark 5.1 (the complex $e$-invariant).** The first version also asserted that "the complex $e$-invariant of $\eta^2$ vanishes". We withdraw that phrasing. In Adams' formulation [24], $e_{\mathbb C}$ of $f:S^{m+r}\to S^m$ is the extension class of $0\to\widetilde K(S^{m+r+1})\to\widetilde K(C_f)\to\widetilde K(S^m)\to0$ in $K^0$. It carries information only when $r$ is odd. In stem $r=2$ one of the outer terms lies in $K^1$, so there is no extension to measure. The precise statement about complex $K$-theory that we use is item 2. The relevant Adams invariant in stems $8k+1,8k+2$ is $d_{\mathbb R}$, which is item 3.

*Consequence.* Among the invariants compared here, the following do not distinguish $X_0$ from $X_1$: ranks, torsion, every positive-degree $\mathrm{Sq}^i$ and $P^i$, Conley homology, and $KU_*$. In particular they do not see the reframing ambiguity. Two of the compared invariants do see it: $KO_3$, and the secondary operation of item 4. We make no claim that these are the only or the "minimal" invariants that detect it.

## 6. Theorem C: index framings from the reduced family

### 6.1 Setting

Let $P,Q$ be objects of $\Sigma_Q$, $\Sigma_H$ or $\Sigma_E$, and let $A_P=Df_\varepsilon(P)\in M_5(\mathbb R)$ be the reduced asymptotic matrices. They are hyperbolic, since the objects are nondegenerate [41, 42]. Let
$$\mathcal P(P,Q)=\big\{A\in C^0(\bar{\mathbb R},M_5(\mathbb R)):\ A(-\infty)=A_P,\ A(+\infty)=A_Q\big\},$$
and $D_A=\partial_s-A(s):H^1(\mathbb R;\mathbb R^5)\to L^2(\mathbb R;\mathbb R^5)$.

For a trajectory $u$ with reduced curve $z_u$, the evaluation $u\mapsto A_u:=Df_\varepsilon(z_u(\cdot))$ maps $\widetilde{\mathcal M}(P,Q)$ into $\mathcal P(P,Q)$, and $D_{A_u}=D^c_u$ is the reduced linearization of [42, Prop. 2]. That proposition shows the following for the full gauge-fixed operator $D_u=\partial_s-DF_\varepsilon(u(s)):W\to L^2(\mathbb R;X)$ on an *actual* trajectory $u$, where $W=H^1(\mathbb R;X)\cap L^2(\mathbb R;Z)$:
* $D_u$ is conjugate to $\begin{psmallmatrix}D^c_u&B_u\\0&D^h_u\end{psmallmatrix}$ with $D^h_u$ invertible;
* hence $\operatorname{Ind}\{D_u\}\cong\operatorname{Ind}\{D^c_u\}=T\widetilde{\mathcal M}(P,Q)$.

We use the full operators **only** through this comparison on actual trajectories.

### 6.2 What is not claimed: the enlarged affine operator space

The first version also used the affine space $\mathcal P^{\rm full}(P,Q)$ of paths in $\mathcal L_*+\mathcal L(Z,X)$ with hyperbolic ends, and claimed that it is a contractible space of Fredholm operators. That is false, and we withdraw it.

**Remark 6.2 (the enlarged space is not Fredholm).** Let $\mathcal L_*:Z\subset X\to X$ be self-adjoint, with orthonormal eigenvectors $e_n$ and eigenvalues $\lambda_n$, $|\lambda_n|\to\infty$. Give $Z$ the graph norm, so $\|e_n\|_Z^2=1+\lambda_n^2$.
* Since $\mathcal L_*\in\mathcal L(Z,X)$, the affine space contains the operator $0$. More generally it contains paths $A(s)$ that vanish on an interval $[-1,1]$ and equal the prescribed asymptotic operators near $\pm\infty$; take $A(s)=\rho(s)A_\pm$ with a cutoff $\rho$.
* Fix a nonzero bump $\varphi$ supported in $[-1,1]$ and put $u_n=\varphi\,e_n/\sqrt{1+\lambda_n^2}$. Then
$$\|u_n\|_W^2=\frac{\|\varphi\|^2+\|\varphi'\|^2}{1+\lambda_n^2}+\|\varphi\|^2\ \ge\ \|\varphi\|^2,\qquad \|(\partial_s-A)u_n\|_{L^2(X)}^2=\frac{\|\varphi'\|^2}{1+\lambda_n^2}\to0,$$
  and $u_n\rightharpoonup0$ in $W$.
* So no estimate $\|u\|_W\le C(\|(\partial_s-A)u\|+\|Ku\|)$ with $K$ compact can hold, and $\partial_s-A$ is not Fredholm $W\to L^2(X)$.

The defect is the loss of control of the spatial graph norm on a bounded $s$-interval, not the behaviour at infinity. verify.py §7b evaluates these norms exactly for $\varphi=(1-s^2)^2$ ($\|\varphi\|^2=256/315$, $\|\varphi'\|^2=256/105$). The reduced family is unaffected, because there $A(s)$ ranges over bounded operators on a fixed finite-dimensional space.

### 6.3 Statement

**Theorem C.**
1. *(Reduced operator space: existence and uniqueness of homotopy class.)* $\mathcal P(P,Q)$ is convex, hence contractible.
   * Each $D_A$ is Fredholm of index $\mu(P)-\mu(Q)$ [27], [35].
   * The index bundle $\operatorname{Ind}_{PQ}\to\mathcal P(P,Q)$ is stably trivial.
   * The homotopy classes of its stable trivializations form a torsor over $[\mathcal P(P,Q),O]=\pi_0(O)=\mathbb Z/2$. So a stable trivialization $\tau_{PQ}$ exists and is unique up to homotopy once an orientation is fixed.
   * No statement is made about the higher homotopy of the space of trivializations. Already over a point, the oriented stable trivializations form a space $\simeq SO$, with $\pi_1(SO)=\mathbb Z/2$.
2. *(Once-broken gluing: homotopy classes.)* Linear gluing [31], [30] gives, for $\rho\ge\rho_0$, stable isomorphisms
$$\operatorname{Ind}(A\#_\rho B)\cong\operatorname{Ind}(A)\oplus\operatorname{Ind}(B)$$
   over $\mathcal P(P,Q)\times\mathcal P(Q,R)\times[\rho_0,\infty)$. Choose the orientations compatibly with these isomorphisms (coherent orientations [30]). Then the pullback of $\tau_{PR}$ and $\tau_{PQ}\oplus\tau_{QR}$ lie in the same homotopy class. This is a separate statement for each once-broken stratum. We do **not** choose the connecting homotopies compatibly at twice-broken configurations, and we do **not** construct a coherent system of trivializations over the compactified moduli spaces.
3. *(Actual trajectories, interiors only.)* Pull $\tau_{PQ}$ back along $u\mapsto A_u$ and use [42, Prop. 2]. This gives stable trivializations of $T\widetilde{\mathcal M}(P,Q)\cong\operatorname{Ind}\{D_u\}$ over the interior of every morphism space; we call them *index framings*.
   * On each component $\widetilde{\mathcal M}_0$ of an interior, any two stable trivializations agree up to homotopy and orientation, because $[\widetilde{\mathcal M}_0,SO]=0$. The component is contractible for $\Sigma_Q$, and $\cong S^2\times\mathbb R$ for $\Sigma_H$, where $[S^2,SO]=\pi_2(SO)/\pi_1=0$.
   * In particular the index framing agrees up to homotopy and orientation with the CJS Morse framing $T\widetilde{\mathcal M}\oplus E^u(Q)\cong E^u(P)$ [1, (15)]. This is essentially [42, Rem. 4.3].
   * On interiors, therefore, framings carry no information beyond orientations. All the framing data relevant to Theorem A sit at the corners.
4. *(Linear or $\mathrm{Top}$-related framings: unconditional.)* Let $\mathcal C$ be $\Sigma_Q$, $\mathcal C_{\rm PDE}$ or $\Sigma_H$, and let $\tau'$ be any coherent framing of the topological flow category. Suppose that on every morphism space, corners included, $\tau'$ is related to the model framing of [42] by stable isomorphisms of vector bundles or of topological microbundles [34], compatibly with faces. Then the difference is a coherent $O$- or $\mathrm{Top}$-cocycle, and $|\mathcal C|_{\tau'}\simeq X_0$.

*Proof.*
1. Convexity is clear: $tA+(1-t)A'$ has the same ends. Fredholmness and the index formula for hyperbolic ends in finite dimensions are [27] and [35]. A virtual bundle over a contractible paracompact space is trivial. Two stable trivializations differ by a map to $O$, and $[\mathcal P(P,Q),O]=\pi_0(O)$. The space of oriented stable trivializations over a point is $SO$; this is why only homotopy classes are claimed.
2. The isomorphism is defined over a contractible parameter space. Two stable trivializations of the same virtual bundle over a contractible base, with the same orientation, are homotopic.
3. By [42, Prop. 2], $\ker D_u\cong\ker D^c_u=T_u\widetilde{\mathcal M}$ and the cokernels vanish. So the pullback of $\tau$ is a stable trivialization of $T\widetilde{\mathcal M}$. Two stable trivializations of the same bundle on a connected base $B$ differ by a map $B\to O$. If $[B,SO]=0$, this map is determined up to homotopy by its component.
4. Two framings of the same stable bundle that are compared through vector-bundle isomorphisms differ by an $O$-valued map. If they are compared through microbundle isomorphisms, they differ by a $\mathrm{Top}$-valued map, and compatibility with faces makes these maps a coherent cocycle. Proposition 3.3(3) and Theorem A(3)–(4) then show that the difference is homotopic to a reorientation. Hence $|\mathcal C|_{\tau'}\simeq|\mathcal C|_{\rm model}\simeq X_0$ [42, Thm. 1(4)], [43, Thm. D(1)]. ∎

### 6.4 The geometric framing: hypothesis (Cmp)

The model framing lives on the smooth structure transported from $\mathcal C_{\rm mod}$. The index framings of Theorem C(3) live on index bundles over the HW moduli, which are $C^{k-1}$ manifolds in their interiors. At the corners the HW moduli have no natural smooth structure [42, Rem. 4.4]. Theorem C does not produce a coherent framing over the compactified HW moduli. We therefore isolate as a hypothesis both the existence of such a framing and its comparison with the model.

**Hypothesis (Cmp).** There is a coherent framing $\tau_{\rm HW}$ of the topological flow category ($\Sigma_Q$, $\Sigma_H$ or $\mathcal C_{\rm PDE}$) with two properties:
* on each interior it is a stable trivialization of the index bundle $\operatorname{Ind}\{D_u\}\cong T\widetilde{\mathcal M}$, defined at broken trajectories via linear gluing;
* on every morphism space, corners included, it is related to the model framing, pulled back by the comparison isomorphism $\Phi$ of [42, Thm. 1(2)], by stable isomorphisms of vector bundles or of topological microbundles, compatibly with faces.

The two parts of (Cmp) are (i) the existence of $\tau_{\rm HW}$, which needs coherent higher choices at twice-broken corners, and (ii) the comparison at corners. Neither is proved here. On interiors the comparison holds in the microbundle sense: $\Phi$ is a homeomorphism, and topological tangent microbundles are homeomorphism invariants [34]. By Theorem C(3), the homotopy class on interiors is forced up to orientation.

**Corollary C′.**
1. *(Conditional.)* Under (Cmp), the realization of $\Sigma_Q$, $\Sigma_H$ or $\mathcal C_{\rm PDE}$ with the framing $\tau_{\rm HW}$ is $X_0$.
2. *(Unconditional.)* Let $\tau'$ be a coherent framing that realizes $X_1$. Then $\tau'$ is not related to the model framing by stable vector-bundle or $\mathrm{Top}$-microbundle isomorphisms compatible with faces. Its difference cocycle with the model framing is a $G$-cocycle with $\sum_Qc_Q=\eta^2$ (respectively $[g]=\eta^2$ on $S^2$). This class is not in the image of $\pi_2(O)=\pi_2(\mathrm{Top})=0$.

*Proof.* Theorem C(4), Theorem A(3)–(4) and Lemma 4.3. ∎

## 7. Theorem D: a local Nahm-pole Gauss-map statement

Theorem D is a local, finite-dimensional statement about the Lagrangian Gauss map at a Nahm pole. It is *not* a construction of a Floer polarization or of a coherent index framing, and nothing in §§4–6 or §8 uses it.

### 7.1 Setting

Let $J=\begin{psmallmatrix}0&I\\-I&0\end{psmallmatrix}$ on $\mathbb R^{2n}=\mathbb C^n$, $z=A+iC$, and $\omega(u,v)=\langle Ju,v\rangle$. Let $S:\mathbb C^n\to\mathbb C$ be holomorphic.

The reduced HW equation is the $\zeta$-instanton equation, in the form
$$(\partial_s+i\partial_y)z=-\overline{\partial S}$$
in one standard normalization; see [18] and [45, (1.1), (2.3)] for the exact conventions. Its linearization at a $y$-dependent object $x$ is $\partial_s-L_x$, with cross-section operator $L_x=J\partial_y-H_x(y)$ and $H_x=\operatorname{Hess}\operatorname{Re}S(x(y))$ [45, §1.2].

In the left-invariant ansatz on $\mathrm{Sol}^3$ this reduction is exact in the diagonal ansatz. In the nine-component ansatz it holds only in the sector $A_s=A_y=0$, which is an additional restriction and not a gauge choice [44, Thm. A(2)], [45, Thm. 1(B)]. We make no claim outside this sector.

Assume a *Nahm pole* at $y=0$:
$$H_x(y)=-\frac{K_0}{y}+R_x(y).$$
* $K_0$ is a constant symmetric matrix with $K_0J=-JK_0$.
* $R_x(y)$ is symmetric and $J$-anticommuting, continuous in $(x,y)\in\mathcal K\times(0,y_1]$, and bounded, $\|R_x(y)\|\le C$, for a compact family $\mathcal K$.

Put $M=JK_0$, and assume
$$\operatorname{spec}M\cap[-\tfrac12,\tfrac12]=\emptyset. \tag{G}$$
For the example of [45], $K_0=\begin{psmallmatrix}0&N\\N&0\end{psmallmatrix}$ with $N=\mathbf 1\mathbf 1^{\sf T}-I$, and $\operatorname{spec}M=\{2,1,1,-1,-1,-2\}$ (verify.py §7).

A *pole-regular Jacobi field* is a solution of $L_xU=0$, i.e. $U'=-JH_xU$, with $U\in L^2(0,y_1)$. Put $\Lambda_x(y)=\{U(y):U\text{ pole-regular}\}$.

**Theorem D.**
1. *(Algebra.)* For every holomorphic $S$ and every $z$, $H=\operatorname{Hess}\operatorname{Re}S(z)$ is symmetric with $HJ=-JH$. Then $JH$ is symmetric, $-JH$ is Hamiltonian, and the Jacobi flow preserves $\omega$.

   Suppose moreover that $S$ has real coefficients and $x$ is real. Then the conjugation $c$ satisfies $cJc=-J$ and $cH_xc=H_x$. The antiholomorphic involution $\tau=Jc$ ($z\mapsto-i\bar z$) satisfies $\tau J\tau^{-1}=-J$ and $\tau H_x\tau^{-1}=-H_x$. So $\tau L_x\tau^{-1}=-L_x$ and $\operatorname{spec}L_x$ is symmetric (cf. [45, Thm. 1(A1)]). Note that $c$ itself does not anticommute with $L_x$.
2. *(Lagrangian.)* Assume (G). Then:
   * $M$ is symmetric and anticommutes with $J$;
   * $E_+:=E_{>0}(M)$ is Lagrangian of dimension $n$;
   * for each $x\in\mathcal K$ and $y\in(0,y_1]$, $\Lambda_x(y)$ is a Lagrangian subspace.
3. *(Pole limit.)* $\Lambda_x(y)\to E_+$ as $y\downarrow0$, uniformly in $x\in\mathcal K$, with $\operatorname{dist}(\Lambda_x(y),E_+)\le C'y$. The map $\mathcal K\times[0,y_1]\to\Lambda(n)$, $(x,y)\mapsto\Lambda_x(y)$ with $\Lambda_x(0):=E_+$, is continuous.
4. *(Gauss map.)* The Lagrangian Gauss map $\rho_{y_1}:\mathcal K\to\Lambda(n)\cong U(n)/O(n)$, $x\mapsto\Lambda_x(y_1)$, is null-homotopic via the explicit homotopy $(x,t)\mapsto\Lambda_x(ty_1)$. Hence its Maslov class in $H^1(\mathcal K;\mathbb Z)$ and its stable class in $[\mathcal K,U/O]$ vanish. With Nahm poles at both ends of $(0,L)$, both boundary Lagrangians are connected to constant ones by such explicit homotopies.

*Proof.*
1. Write $S=u+iv$ with $u,v$ harmonic conjugates. In the real coordinates $(A,C)$, $\operatorname{Hess}u=\begin{psmallmatrix}a&-b\\-b&-a\end{psmallmatrix}$, where $a=\operatorname{Re}S''$ and $b=\operatorname{Im}S''$ are symmetric. This matrix anticommutes with $J$. Then $(JH)^{\sf T}=H^{\sf T}J^{\sf T}=-HJ=JH$, and
$$\tfrac{d}{dy}\omega(U,V)=\langle J(-JHU),V\rangle+\langle JU,-JHV\rangle=\langle HU,V\rangle-\langle U,HV\rangle=0 .$$
   For real coefficients, $\operatorname{Re}S(\bar z)=\operatorname{Re}S(z)$, so $\operatorname{Hess}\operatorname{Re}S(cz)=c\,H(z)\,c$; at a real point, $cHc=H$. Finally $cJc=-J$. Hence $\tau=Jc$ satisfies
   * $\tau^2=JcJc=J(cJc)=-J^2=I$;
   * $\tau J\tau^{-1}=J(cJc)J^{-1}=-J$;
   * $\tau H\tau^{-1}=J(cHc)J^{-1}=JHJ^{-1}=-H$.

   Exact checks for two polynomials, one of them generic complex, are in verify.py §7.
2. $M^{\sf T}=K_0^{\sf T}J^{\sf T}=-K_0J=JK_0=M$, and $MJ=JK_0J=-J^2K_0=K_0=-JM$. So $J$ maps $E_\lambda$ to $E_{-\lambda}$, and by (G) $\dim E_+=n$. For $u,v\in E_+$, $Ju\in E_-\perp E_+$, so $\omega(u,v)=0$.

   In the variable $\tau=-\log y$ the Jacobi equation reads
$$\frac{dU}{d\tau}=-\big(M+e^{-\tau}B_x(e^{-\tau})\big)U,\qquad B_x=-JR_x .$$
   * The constant system $U_\tau=-MU$ has an exponential dichotomy on $\mathbb R$, with stable subspace $E_+$ and rates $\ge\lambda_0:=\min|\operatorname{spec}M|>\frac12$.
   * The perturbation is integrable, since $e^{-\tau}\|B_x\|\le Ce^{-\tau}$.
   * By the roughness theorem for exponential dichotomies [28], [35], there is $\tau_0$, depending only on $C$ and $\lambda_0$, such that the perturbed system has a dichotomy on $[\tau_0,\infty)$ with rates $\lambda_0-\epsilon>\frac12$.
   * Its stable subspace $S_x(\tau)$ satisfies $\|P_{S_x(\tau)}-P_{E_+}\|\le C''\sup_{t\ge\tau}e^{-t}=C''e^{-\tau}$, and depends continuously on $x$.

   Solutions in $S_x(\tau)$ are $O(y^{\lambda_0-\epsilon})$, hence in $L^2$ near $y=0$. The others grow at least like $y^{-(\lambda_0-\epsilon)}$ and are not in $L^2$, because $2(\lambda_0-\epsilon)\ge1$. So $\Lambda_x(y)=S_x(-\log y)$ has dimension $n$. It is isotropic, because $\omega(U,V)$ is constant in $y$ and tends to $0$ as $U,V\to0$. So it is Lagrangian.
3. This is the estimate just proved. Continuity on $\mathcal K\times(0,y_1]$ is continuous dependence on parameters.
4. The homotopy is continuous by 3, and it ends at the constant map to $E_+$. The Maslov class is the pullback of the generator of $H^1(\Lambda(n);\mathbb Z)$ under a null-homotopic map, and the stable class is its image in $[\mathcal K,U/O]$. At the second pole, apply the same argument in $L-y$. ∎

verify.py §8 illustrates items 2–3 numerically, for $K_0$ of [45] and a random bounded $J$-anticommuting remainder. There $\Lambda(y)$ is isotropic to $10^{-8}$. Its distance to $E_+$ decreases monotonically, to below $10^{-3}$ at $y=10^{-4}$, consistent with $O(y)$. It also checks the Maslov indices: $1$ for the loop $e^{i\theta}\mathbb R$ and $0$ for a constant loop. These are illustrations, not inputs to the proof.

### 7.2 Consequence for index bundles (conditional on Fredholm theory)

**Corollary D′.** Consider trajectories of the finite-dimensional $\zeta$-instanton equation on $\mathbb R_s\times(0,L)$ with Nahm poles at $y=0,L$ satisfying the hypotheses of Theorem D at both ends. Assume:

**(F)** the strip operators $\partial_s-L_{x(s)}$ are Fredholm between the Nahm-pole weighted spaces, with index bundles depending only on the homotopy class of the coefficient family rel asymptotic operators, as in He's weighted theory [21, §§5.5–5.6] and [20].

Then:
* for any compact family $\mathcal K$ of trajectories, the index bundle over $\mathcal K$ is stably trivial relative to the ends;
* it admits stable trivializations pulled back from a contractible space of coefficient families, and these form exactly two homotopy classes, distinguished by orientation.

No uniqueness is claimed among *all* trivializations over $\mathcal K$, which form a torsor over $[\mathcal K,O]$. No coherence under gluing is claimed.

*Proof.*
* The coefficient families $\{H_{x(s)}(y)\}$ range over the convex set of symmetric, $J$-anticommuting families $-K_0/y+R$ with $R$ bounded and continuous. This is a set of order-zero, $L^2$-bounded perturbations of a fixed principal part $J\partial_y+K_0/y$. Unlike the space in Remark 6.2, it does not alter the principal part; Fredholmness is nevertheless the content of (F) and is not proved here.
* Under (F), the index bundle over $\mathcal K$ is pulled back from this contractible space. By Theorem D(4), the boundary Lagrangian data along it are homotopic to the constant $E_+$.
* Conclude as in Theorem C(1). ∎

The analogy with the vanishing of $\rho:L(T^*M)\to U/O$ in [4, Lemma 15], [1, (24)–(25)] is only formal. There, the $U(n)$-structure is complexified from $O(n)$. Here, the Nahm pole fixes the Lagrangian $E_+$.

### 7.3 Relation to the AH-fold categories

Formally, the full HW system on $S^3\times(0,L)$ is a $\zeta$-instanton with infinite-dimensional target: complexified connections, with complex Chern–Simons superpotential [18]. Theorem D is proved only for finite-dimensional targets $\mathbb C^n$ with hypothesis (G). We do not claim that the gauge-fixed AH operator $\mathcal L_*$ of [39] has the form $J\partial_y-H$ with $H$ satisfying the hypotheses of Theorem D.

For the AH-fold categories, Theorem C uses only the convex reduced space $\mathcal P(P,Q)\subset C^0(\bar{\mathbb R},M_5(\mathbb R))$, together with [42, Prop. 2] on actual trajectories. Theorem E does not use Theorem D.

## 8. Theorem E: synthesis

**Theorem E.** Let $\mathcal C$ be $\Sigma_Q$, $\Sigma_H$ or $\mathcal C_{\rm PDE}$, with its model framing.
1. *(All spherical reframings.)* Under coherent $GL_1(\mathbb S)$-reframings, exactly two stable homotopy types arise as CJS realizations: $X_0=\Sigma^\infty(S^1\vee S^4)$ and $X_1=S^1\cup_{\eta^2}e^4$. The class of a reframing is the sum of its square classes (respectively its class on $S^2$).
   * $X_0$ and $X_1$ have the same ordinary (co)homology and the same Steenrod-module structure at every prime: all positive-degree primary operations vanish on both. They also have isomorphic $KU_*$.
   * They are distinguished by $KO_3$ ($\mathbb Z/2$ versus $0$) and by the secondary operation of $\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^3\mathrm{Sq}^1$.
2. *(Vector-bundle and $\mathrm{Top}$ framings; unconditional.)* All $O$- and $\mathrm{Top}$-reframings realize $X_0$, and are homotopic to each other after reorientation. More generally, every coherent framing related to the model framing by linear or topological bundle isomorphisms compatible with faces realizes $X_0=\Sigma^\infty h(\bar B)$, the suspension spectrum of the Conley index.
3. *(Geometric framing; conditional.)* Under hypothesis (Cmp), the HW geometric framing $\tau_{\rm HW}$ realizes $X_0=\Sigma^\infty h(\bar B)$.
4. *(Exotic class.)* The alternative $X_1$ corresponds to the generator of $\operatorname{coker}(J:\pi_2O\to\pi_2^s)=\mathbb Z/2\langle\eta^2\rangle$. It is not induced by any $O$- or $\mathrm{Top}$-reframing of the model framing. There is no $\nu$-type ($\pi_3^s$) ambiguity.
5. *(Other sectors.)* $\Sigma_{\rm iso}$, $\Sigma_{V_4}$ and $\Sigma_2$ realize only $*$, and $\Sigma_E$ realizes only $X_0$.

*Proof.*
* Item 1 is Theorems A(3)–(4) and B.
* Item 2 is Theorem A(3)–(4), Theorem C(4), and [41, Thm. E1], [43, Thm. D(2)] for the Conley index.
* Item 3 is Corollary C′(1).
* Item 4 is Corollary C′(2) and the table of §3.1.
* Item 5 is Theorem A(1)–(2). ∎

The fold-crossing observation of Remark 4.5 is heuristic and is not part of Theorem E.

*Comparison with a naive expectation.* One might expect "24 alternative framings giving $S^0\cup_\nu e^4$-type spectra", by reading the classifying group as $[S^1\vee S^4,BGL_1\mathbb S]$. That is not correct for these categories. The computed classifying data are $(\Gamma_0,\Gamma_1,\Gamma_2)=(0,0,\mathbb Z/2)$. So there is exactly one alternative, of type $\eta^2$, rather than $23$ of type $k\nu$, and among the invariants of Theorem B it is seen by $KO_3$ and the secondary operation, not by $\mathrm{Sq}^4$ or $P^1$.

## 9. Related work and novelty

* **Framing dependence in general.**
  * Cohen–Jones–Segal [2, 3] and Cohen [1, Prop. 5] describe reframings as functors to $GL_1(\mathbb S)$.
  * Blakey–Bonciocat [14] prove, in the framework of Abouzaid–Blumberg [11], that twisting by stable spherical fibrations yields Thom spectra. Their Remark 4.5 notes that the $J$-homomorphism affects results, and their Example 1.3 shows framing-dependent Steenrod squares in Lagrangian Floer homotopy.
  * Porcelli–Smith [15, 16] develop tangential structures; there, structures on a Lagrangian form a torsor over $\pi_dO\oplus\pi_{d-1}\mathbb S$ [16, Ex. 2.27].
  * Large [17] constructs spectral Fukaya categories. Bonciocat [12] and Côté–Kartal [13] treat vector-bundle twists in Morse–Bott theory.
* **Khovanov.**
  * Lipshitz–Sarkar [7] prove independence of the Khovanov spectrum from framing choices on the cube flow category by obstruction theory. LOS [10] identify the interval framing values.
  * The Steenrod square $\mathrm{Sq}^2$ of [8] is the first operation that sees framing data beyond signs. On the HW categories here it vanishes for degree reasons in both $X_0$ and $X_1$ (as already noted in [46, §7.3] for the vector-framed case).
  * Lawson–Lipshitz–Sarkar [9] give the Burnside-functor viewpoint, in which framings are absorbed.
* **HW input.** The rStation series [37–46] supplies all HW input. In particular:
  * [42] (math_33) gives the model category, its vector-framed realization, the full/reduced index comparison (Prop. 2, §5), and the interior framing remark (Rem. 4.3);
  * [43] (math_34) gives the PDE category and the Conley index;
  * [45] (math_48) gives the $\zeta$-instanton reduction and the Nahm-pole matrix;
  * [46] (math_52) gives the rank-three interval compatibility count and the vanishing of $\mathrm{Sq}^2$ in these sectors.
* **Polarization and Nahm poles.** Cohen [4], Kragh [5] and Abouzaid–Kragh [6] treat the polarization class for cotangent bundles. Haydys [18] gives the $\zeta$-instanton formulation, and Mazzeo–Witten [20] and He [21] develop the Nahm-pole elliptic theory.

**What we checked.** We searched for reframing classifications of Haydys–Witten, Fukaya–Seidel or Khovanov flow categories, for reframings of framed flow categories by $GL_1(\mathbb S)$, and for polarization or Maslov triviality for Nahm-pole operators. We consulted the abstracts and relevant sections of [14, 15, 16] and [4], the Khovanov framing literature, and [42, 43, 45, 46]. We did not find:
1. a classification of the spherical ($GL_1(\mathbb S)$) reframings of any Haydys–Witten category;
2. the identification, for the AH-fold categories, of the unique exotic reframing as $\operatorname{coker}J$ in degree $2$, with invariant $\sum_Qc_Q$, distinct from all vector-bundle and $\mathrm{Top}$ framings and detected by $KO_3$.

**What is new, and what is only assembled.**
* *Central new result:* the explicit degree-two spherical reframing classification for the HW categories $\Sigma_Q$, $\mathcal C_{\rm PDE}$ and $\Sigma_H$ (Theorem A(3)–(4)). This includes $\Gamma_2=\mathbb Z/2$ from the morphism manifolds, the invariant $\sum_Qc_Q$ (Lemma 4.3), its distinction from ordinary vector-bundle and $\mathrm{Top}$ framings, and its detection by $KO_3$ and the secondary operation (Theorem B applied).
* *Standard techniques, assembled:* Proposition 3.3 and Lemmas 3.4, 4.1–4.2 (obstruction theory as in [7]); Theorem B itself (classical homotopy theory [23–25]); Remark 4.4 (the Thom-spectrum mechanism [1, 14]).
* *Already in the HW literature:* $\Gamma_0=\Gamma_1=0$ at the level of incidence ranks ([46, §7.3]), the vector-framed realization $X_0$ ([42]), and the interior framing statement of Theorem C(3) ([42, Rem. 4.3]).
* *Weaker analytic statements:* Theorem C(1)–(2) (homotopy classes only), Theorem C(4) and Corollary C′(2) (an unconditional comparison), and Theorem D (a local Gauss-map statement).

## 10. Status of claims

| claim | status |
|---|---|
| §3.1 table of $\pi_k(O)$, $\pi_k^s$, $J$ for $k\le2$; $\lvert\mathrm{im}J\rvert$ in degrees 3, 7, 11 | standard [26, 24]; encoded in verify.py §1 (known input) |
| Lemma 3.2 (invariance under homotopy and reorientation) | standard [2, 7]; sketched |
| Proposition 3.3 (normalization, levels 0–2) | proved (obstruction theory as in [7]) |
| Lemma 3.4 (disc modification) | proved at the level of the Pontryagin–Thom construction [1, (16)], [7, §3] |
| $\Gamma_0=\Gamma_1=0$, $\Gamma_2=\mathbb Z/2$ for $\Sigma_Q$ | proved; exact $\mathbb F_2$ computation (verify.py §4); the level-1 incidence ranks also in [46, §7.3] |
| Lemma 4.3 | proved (corrected argument: change of retraction on the 3-skeleton; second argument via $\operatorname{im}\partial^{\rm sq}$); finite data in verify.py §4b |
| Theorem A(1)–(5) | proved, modulo [37, 38, 41, 42, 43] (sector inputs) |
| Remark 4.4 (agreement with Thom spectrum of $S^3$) | consistency with [1, 3, 14]; not used |
| Remark 4.5 (fold crossing) | **heuristic**; not used |
| Remark 4.6 ($\Sigma_N$, $N\ge3$) | **conditional** on [46, Remark 2.2] |
| Theorem B | proved (standard homotopy theory [23, 24, 25]; verify.py §§2–3: §2 encodes known coefficients, §3 computes Adem relations and admissible bases) |
| Remark 6.2 (enlarged affine space not Fredholm) | proved; exact norms in verify.py §7b |
| Theorem C(1)–(3) | proved, as homotopy-class statements only, modulo [42, Prop. 2], [27, 30, 31, 35] |
| Theorem C(4), Corollary C′(2) | proved (unconditional) |
| Existence of a coherent geometric index framing; Corollary C′(1) | **not proved**; part of hypothesis (Cmp) |
| Theorem D(1)–(4) | proved for finite-dimensional targets under (G); exact algebra (verify.py §7); numerics illustrative (§8) |
| Corollary D′ | **conditional** on Fredholm hypothesis (F); homotopy classes only |
| Theorem D for the AH-fold operator $\mathcal L_*$; a Floer polarization | **not claimed** (§7.3) |
| Theorem E(1), (2), (4), (5) | proved |
| Theorem E(3) | **conditional** on (Cmp) |
| complete categories, knots, $N\ge3$ unconditionally | not claimed |

**Corrections with respect to the first version.**
1. *Fredholm space.* The claim that the full affine operator space $\mathcal L_*+\mathcal L(Z,X)$ is a space of Fredholm trajectory operators is withdrawn (Remark 6.2). Full operators are used only on actual trajectories, through [42, Prop. 2].
2. *Contractibility.* The claim that "all spaces of choices are contractible" is withdrawn. Theorem C and Corollary D′ now state existence and uniqueness of homotopy classes only, and the index framing is no longer called "canonical" or "coherent"; the existence of a coherent geometric framing is now part of hypothesis (Cmp).
3. *Lemma 4.3.* The final step of Lemma 4.3 was wrong: cancellation on the cycle cell alone does not let the original retraction extend. It is replaced by a change of retraction on the $3$-skeleton, plus an independent incidence-image argument.
4. *Hypotheses and invariants.* The abstract and the synthesis now keep (Cmp) wherever the geometric framing is identified. The phrases "only $KO$-type invariants" and "minimal invariant" are replaced by statements about the invariants actually compared. "All primary operations" is restricted to positive degree. The complex $e$-invariant claim is withdrawn (Remark 5.1).

**Verifier.**
* verify.py has 97 checks and ends with `FALLOS = 0`; the output is in verify_output.txt. Every check carries a tag:
  * **[K] (28 checks)** encode known facts or imported data and record the input without proving it: the tables of $\pi_*^s$, $\pi_*(O)$ and $KO_*$, the $\eta$-action, the combinatorics of $\Sigma_Q$ from [41, 42], and bookkeeping.
  * **[C] (64 checks)** are genuine finite computations: the Adem relations and admissible bases, the Cartan formula, the $\mathbb F_2$ ranks giving $(\Gamma_0,\Gamma_1,\Gamma_2)$, the corner structure, Smith forms and homology, the data of Lemma 4.3 (verify.py §4b), the cube categories, the exact $\zeta$-instanton algebra, and the exact norms of Remark 6.2.
  * **[N] (5 checks)** are floating-point illustrations (§8), not used in any proof.
* These computations do not verify the analytic inputs: the Fredholm theory of [27, 35] and (F), the comparison of [42, Prop. 2], and (Cmp).
* verify.mpl mirrors §§1, 3, 4, 4b, 7 and 7b in Maple, with 46 checks. It is provided for independent checking. Maple was not available when this version was prepared, so verify.mpl has **not** been run in this version.

## References

[1] R. L. Cohen, *Floer homotopy theory, revisited*, arXiv:1901.08694.

[2] R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.

[3] R. L. Cohen, J. D. S. Jones, G. B. Segal, *Morse theory and classifying spaces*, preprint (1995).

[4] R. L. Cohen, *The Floer homotopy type of the cotangent bundle*, Pure Appl. Math. Q. 6 (2010), 391–438; arXiv:math/0702852.

[5] T. Kragh, *Parametrized ring-spectra and the nearby Lagrangian conjecture* (with an appendix by M. Abouzaid), Geom. Topol. 17 (2013), 639–731.

[6] M. Abouzaid, T. Kragh, *On the immersion classes of nearby Lagrangians*, J. Topol. 9 (2016), 232–244.

[7] R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.

[8] R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848.

[9] T. Lawson, R. Lipshitz, S. Sarkar, *Khovanov homotopy type, Burnside category and products*, Geom. Topol. 24 (2020); arXiv:1505.00213.

[10] A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500; arXiv:1710.01857.

[11] M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.

[12] C. M. Bonciocat, *Revisiting the Cohen–Jones–Segal construction in Morse–Bott theory*, arXiv:2409.11278.

[13] L. Côté, Y. B. Kartal, *Equivariant Floer homotopy via Morse–Bott theory*, arXiv:2309.15089.

[14] K. Blakey, C. M. Bonciocat, *Parameterized Lagrangian Floer homotopy*, arXiv:2506.20122.

[15] N. Porcelli, I. Smith, *Bordism of flow modules and exact Lagrangians*, arXiv:2401.11766.

[16] N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257.

[17] T. Large, *Spectral Fukaya categories for Liouville manifolds*, PhD thesis, MIT, 2021.

[18] A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207; arXiv:1010.2353.

[19] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.

[20] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621, AMS, 2014; arXiv:1311.3167.

[21] S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, J. Topol. (2019); arXiv:1707.06182.

[22] C. Manolescu, *Seiberg–Witten–Floer stable homotopy type of three-manifolds with $b_1=0$*, Geom. Topol. 7 (2003), 889–932.

[23] J. F. Adams, *On the non-existence of elements of Hopf invariant one*, Ann. of Math. 72 (1960), 20–104.

[24] J. F. Adams, *On the groups $J(X)$ IV*, Topology 5 (1966), 21–71.

[25] R. E. Mosher, M. C. Tangora, *Cohomology Operations and Applications in Homotopy Theory*, Harper & Row, 1968.

[26] H. Toda, *Composition Methods in Homotopy Groups of Spheres*, Ann. of Math. Stud. 49, Princeton Univ. Press, 1962.

[27] J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.

[28] W. A. Coppel, *Dichotomies in Stability Theory*, Lecture Notes in Math. 629, Springer, 1978.

[29] R. C. Kirby, L. C. Siebenmann, *Foundational Essays on Topological Manifolds, Smoothings, and Triangulations*, Ann. of Math. Stud. 88, Princeton Univ. Press, 1977.

[30] A. Floer, H. Hofer, *Coherent orientations for periodic orbit problems in symplectic geometry*, Math. Z. 212 (1993), 13–38.

[31] M. Schwarz, *Morse Homology*, Progr. Math. 111, Birkhäuser, 1993.

[32] L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.

[33] M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.

[34] J. M. Kister, *Microbundles are fibre bundles*, Ann. of Math. 80 (1964), 190–199.

[35] K. J. Palmer, *Exponential dichotomies and transversal homoclinic points*, J. Differential Equations 55 (1984), 225–256.

[36] L. Qin, *An application of topological equivalence to Morse theory*, arXiv:1102.2838.

[37] https://rstation.ai/problems/math/papers/24/v2

[38] https://rstation.ai/problems/math/papers/25/v1

[39] https://rstation.ai/problems/math/papers/30/v1

[40] https://rstation.ai/problems/math/papers/31/v1

[41] https://rstation.ai/problems/math/papers/32/v1

[42] https://rstation.ai/problems/math/papers/33/v1

[43] https://rstation.ai/problems/math/papers/34/v1

[44] https://rstation.ai/problems/math/papers/47/v1

[45] https://rstation.ai/problems/math/papers/48/v1

[46] https://rstation.ai/problems/math/papers/52/v1

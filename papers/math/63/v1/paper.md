# Complex orientations relative to a framing and $MU$-modules of the Haydys–Witten height and quadrupole flow categories

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.** Complex orientations make a flow category an $MU$-module (Hedenlund–Oldervoll, Blakey–Porcelli). We classify the complex orientations compatible with a fixed framing on framed flow categories whose morphism spaces are points, intervals, discs and closed surfaces. Relative to the framing these are coherent lifts along $BU\to BO$, with fibre $O/U$, as in standard lifting theory. Theorem A: concordance classes form $\mathbb Z^{\mathrm{discs}}/T_X(\mathbb Z^{\mathrm{intervals}})\oplus\mathbb Z^{\mathrm{closed\ surfaces}}$, detected by half the relative first Chern numbers, where $T_X$ is an integral Stokes matrix of boundary incidences; this is the integral analogue of the normalization and boundary-cokernel method of https://rstation.ai/problems/math/papers/53/v1 (math_53). Theorem B: for the Haydys–Witten height category $\Sigma_H$ (one morphism space $S^2$) and quadrupole category $\Sigma_Q$ the classes form $\mathbb Z$. On $\Sigma_H$ the module is $M_k=\operatorname{cofib}(kx_1:\Sigma^3MU\to\Sigma MU)$, with $\pi_3M_k=\mathbb Z/|k|$; on $\Sigma_Q$ it is some $M_\lambda$, with $\lambda\ne0$ if and only if an explicit invariant $\kappa\ne0$. The Blakey–Porcelli Chern-character complex has differential $d_0+2b_1K$, and for $k\ne0$ or $\kappa\ne0$ the module is not a base change from the sphere spectrum. We compare with the two-object cotangent-sphere example of Porcelli–Smith. Theorem D: extension of scalars of the framed realizations of $\Sigma_H,\Sigma_Q$ (every framing of the Morse–Smale model and every $SO$-reframing of it) and of the spherical realization $X_1$ of math_53 gives $M_0$; under hypothesis (Cmp) of math_53 this includes the Haydys–Witten framing. We do not claim that Haydys–Witten data exclude $k\ne0$. Finally, for each $m$ and each $j$ with $8j\ge m$, some real index bundle over $S^{8j}$ lifting to $BO\langle m\rangle$ has no stable complex structure.

---

## 1. Introduction

The main results are general. Theorem A classifies the complex orientations compatible with a fixed framing on flow categories with moduli of dimension $\le2$, by the cokernel of an integral Stokes matrix, and Theorem B computes the resulting Blakey–Porcelli complexes $(\mathbb C[b]^{\rm Ob},d_0+2b_1K)$ and $MU$-modules on the Haydys–Witten (HW) height and quadrupole categories, producing $MU$-module lifts that are not base changes. On the HW side we prove only a restricted statement (Theorem D(2)): extension of scalars of the framed realizations of these categories, for every framing of the Morse–Smale model and every $SO$-valued reframing of it, and of the spherically framed realization $X_1$ of [R53], gives the base change $M_0=X_0\wedge MU$; under the hypothesis (Cmp) of [R53] this includes the HW framing. We do not claim that HW data exclude the modules $M_k$ with $k\ne0$ (Remark 6.4). What is recalled and what is new is listed in §1.3.

### 1.1 The question

Complex cobordism enters Floer homotopy theory through *complex-oriented flow categories*. These are flow categories whose index bundles carry coherent stable complex structures. Abouzaid–Blumberg [1] arranged such categories into a stable $\infty$-category $\mathrm{Flow}^U$. Hedenlund–Oldervoll [2] proved that it is equivalent to the $\infty$-category of $MU$-modules (as recorded in [3, Rem. 1.11]). Blakey–Porcelli [3] gave a chain-level model for the complexified homotopy of the resulting $MU$-module. Their *Chern-character Morse complex* $CM_*(X,\mathrm{ch};\mathbb C[b])$ integrates coherent Chern–Weil forms of the index bundles over the morphism spaces. It sends a closed stably complex manifold $Y$ to
$$[Y]\ \longmapsto\ \sum_{q_1,q_2,\dots\ge0}\frac{1}{q_1!q_2!\cdots}\Big(\int_Y\mathrm{ch}_1^{q_1}\mathrm{ch}_2^{q_2}\cdots\Big)\,b_1^{q_1}b_2^{q_2}\cdots\ \in\mathbb C[b]\cong\pi_*MU\otimes\mathbb C$$
[3, (1.18), Prop. 4.17]. They also obtained a criterion for an $MU$-lift *not* to be a base change from the sphere spectrum [3, Cor. 1.3, Cor. 7.4].

In symplectic cohomology the Floer operators are Cauchy–Riemann operators on cylinders, and they carry complex orientations coming from the complex-linear symbol [3, §1.4]. The local HW flow categories near the Anderson–Henningson (AH) fold were constructed in rStation papers [R32, R33, R34, R46, R49]. Their reduced operators are $\zeta$-instanton operators on *strips* $\mathbb R\times(0,L)$ with Nahm-pole boundary behaviour, and the pole-regular solutions define Lagrangian boundary data [R53, Thm. D]. Index bundles of Cauchy–Riemann operators with totally real boundary conditions are real virtual bundles, classified through $\Omega(U/O)\simeq\mathbb Z\times BO$ [2, Ex. 0.0.9]. So a complex orientation of an HW category is additional data, and the following questions are natural.

1. Which complex orientations are compatible with a given framing, and up to which equivalence?
2. Which $MU$-modules do they produce?
3. Which of these are base changes $Y\wedge MU$ of spectra, in particular of the two spherical realizations $X_0=\Sigma^\infty(S^1\vee S^4)$ and $X_1=S^1\cup_{\eta^2}e^4$ of [R53]?
4. Which of them are extensions of scalars of the framed or spherically framed realizations of the HW categories?

### 1.2 Results

*Conventions.* All flow categories are finite, smooth with corners, and framed in the sense of [1] and [3, Def. 2.21–2.22] (§2.1). The grading is $\mu$, and $\dim X(a,c)=\mu(a)-\mu(c)-1$. We write $\mathcal J_N=O(2N)/U(N)$ for the space of orthogonal complex structures on $\mathbb R^{2N}$, $\mathcal J_N^+$ for its component inducing the standard orientation, and $J_0$ for the standard structure. A *complex orientation compatible with the framing* (Definition 2.2) is a family of maps $J_{ac}:X(a,c)\to\mathcal J^+_{N(a)-N(c)}$, multiplicative under block sum on broken configurations. *Concordance* means homotopy through such families. $BO\langle m\rangle\to BO$ denotes the $(m-1)$-connected cover.

**The coefficient (§2.2).** Relative to a framing, complex orientations are lifts along $BU\to BO$, i.e. sections with fibre $O/U=\operatorname{hofib}(BU\to BO)$; this is standard lifting theory, and we do not regard it as a new notion of complex orientability. The relevant groups are
$$\pi_k(O/U)=\pi_{k+1}(O)=\mathbb Z/2,\ 0,\ \mathbb Z,\ 0,\ 0,\ 0,\ \mathbb Z,\ \mathbb Z/2\qquad(k=0,\dots,7),$$
and the map $\pi_2(O/U)\to\pi_2(BU)$, $[f]\mapsto c_1$, is injective with image $2\mathbb Z$.

**Theorem A (classification; §3).** Let $X$ be framed, with morphism spaces of dimension $\le2$. Suppose every $2$-dimensional component is either a disc $Q$ with $Q\cap\partial X(a,c)=\partial Q$ or a closed surface disjoint from $\partial X(a,c)$, and every $1$-dimensional component is an interval with boundary its broken ends. Let $\mathcal S_\partial$, $\mathcal S_\circ$ and $\mathcal I$ be the sets of disc, closed-surface and interval components. Then:
1. compatible complex orientations exist (for example the standard one, $J\equiv J_0$);
2. the set $\mathrm{Cl}(X)$ of concordance classes is in natural bijection with
$$\mathbb Z^{\mathcal S_\partial}/T_X(\mathbb Z^{\mathcal I})\ \oplus\ \mathbb Z^{\mathcal S_\circ},$$
via half the relative first Chern numbers of a normalized representative. Here $T_X(m)_Q=\sum_F\varepsilon(Q,F)\,m_{J(F)}$, summed over the faces $F=\{x\}\times J$ or $J\times\{z\}$ of $Q$, is the *Stokes matrix*, with signs $\varepsilon(Q,F)=\pm1$ fixed by the orientations.

The normalization and boundary-cokernel strategy is that of [R53, §3.2], where it classifies spherical reframings with $\mathbb F_2=\pi_2^s$ coefficients. Theorem A is its integral analogue for the coefficient $\pi_2(O/U)=\mathbb Z$, formulated through relative Chern numbers and allowing closed surfaces and arbitrary disc–interval incidences.

**Theorem B (height and quadrupole categories; §4).**
1. *($\Sigma_H$.)* $\mathrm{Cl}(\Sigma_H)\cong\mathbb Z$ via $k(J)=\tfrac12\int_{S^2}c_1(I_J)$. So $\int c_1\in2\mathbb Z$, and every even value occurs. In $\Omega^U_2$ we have $[S^2,J]=k[\mathbb{CP}^1]$. The $MU$-module of $(\Sigma_H,J)$ is
$$M_k=\operatorname{cofib}\big(k x_1:\Sigma^3MU\to\Sigma MU\big),\qquad x_1=[\mathbb{CP}^1],$$
with $\pi_*(M_k)=\Sigma\,MU_*/(kx_1)$ for $k\ne0$, so $\pi_3(M_k)=\mathbb Z/|k|$. We have $M_k\simeq M_{k'}$ iff $|k|=|k'|$, and $M_k$ is a base change $Y\wedge MU$ iff $k=0$. For a coherent Chern–Weil choice, $CM_*(\Sigma_H,\mathrm{ch};\mathbb C[b])$ is $\mathbb C[b]P_4\oplus\mathbb C[b]P_1$ with $\partial P_4=2k\,b_1P_1$. Complex $K$-theory sees $|k|$: $\pi_3(KU\otimes_{MU}M_k)=\mathbb Z/|k|$.
2. *($\Sigma_Q$.)* $\mathrm{Cl}(\Sigma_Q)\cong\mathbb Z$ via $\kappa(J)=\beta^{\sf T}K(J)\alpha$. Here $K(J)_{ts}=\tfrac12 c_1(J|Q_{st})$ are the square Chern numbers of a normalized representative, $\alpha$ generates $H_4$ and $\beta$ generates $H^1$ of the Morse complex. The Chern-character complex is $(\mathbb C[b]^{8},\,d_0+2b_1K)$. Its homology is free of rank $2$ if $\kappa=0$ and $\cong\Sigma\,\mathbb C[b]/(b_1)$ if $\kappa\ne0$. The $MU$-module is $M_\lambda$ for an integer $\lambda$ with $\lambda\ne0\iff\kappa\ne0$. It is a base change from $\mathbb S$ iff $\kappa=0$.
3. *($\eta^2$; a remark, immediate since $\pi_2MU$ is torsion-free.)* The unit $\mathbb S\to MU$ kills $\pi_2^s=\mathbb Z/2$, so $X_0\wedge MU\simeq X_1\wedge MU\simeq M_0$.

**Theorem C (non-base-change criterion; §5; a special case of Blakey–Porcelli [3, Cor. 7.4]).** Let $X$ be a finite complex-oriented flow category with morphism spaces of dimension $\le2$. The criterion (3) is the first-differential case of [3, Cor. 7.4] and its change-of-coefficients spectral sequence [3, (7.12)]; what is added here is the explicit form (1) and an elementary rank-jump proof.
1. For any coherent Chern–Weil choice, the Blakey–Porcelli differential is $d_0+b_1C$, where $C$ integrates $\mathrm{ch}_1$ over the $2$-dimensional morphism spaces. No $b_\rho$ with $\rho\ge2$ and no $b_1^j$ with $j\ge2$ occurs.
2. $C$ anticommutes with $d_0$ and $C^2=0$, so $C$ induces $\bar C:H_*(X;\mathbb C)\to H_{*-3}(X;\mathbb C)$.
3. If $\bar C\ne0$ for some coherent choice, then the $MU$-module of $X$ is not equivalent to $Y\wedge MU$ for any spectrum $Y$.

**Theorem D (real index data and extension of scalars; §6).**
1. *(Real index data do not determine complex orientations.)* Fix $m\ge0$. For each $j\ge1$ with $8j\ge m$ there is a family of Cauchy–Riemann operators with totally real boundary conditions, parametrized by $S^{8j}$, whose index bundle lifts to $BO\langle m\rangle$ and admits no stable complex structure. The condition $8j\ge m$ cannot be dropped: if $8j<m$, every index bundle over $S^{8j}$ that lifts to $BO\langle m\rangle$ is stably trivial (for instance $j=1$, $m=10$, where $\pi_8BO\langle10\rangle=0$). There is also a family over $S^1$ with non-orientable index bundle.
2. *(Extension of scalars of the specified realizations.)* Let $\Sigma\in\{\Sigma_H,\Sigma_Q\}$ and let $\tau$ be a framing of the Morse–Smale model of [R33].
   * For every coherent $SO$-valued reframing $g$, the standard complex orientation of the reframed category $g\tau$, read relative to $\tau$, is concordant to $J^{\rm std}$; so its class in $\mathrm{Cl}(\Sigma,\tau)\cong\mathbb Z$ is $0$, and its $MU$-module is $|\Sigma|_{g\tau}\wedge MU\simeq M_0$.
   * The spherically framed realization $X_1$ of [R53, Thm. A(3)–(4)] has $X_1\wedge MU\simeq M_0$.
   * *(Conditional on (Cmp).)* Under the hypothesis (Cmp) of [R53, §6.4], the framed realization with the HW framing $\tau_{\rm HW}$ is $X_0$ [R53, Cor. C′(1)], so its extension of scalars is $M_0$.
3. *(What is not claimed.)* For $k\ne0$ (respectively $\kappa\ne0$) the module $M_k$ (respectively $M_\lambda$) is not $Y\wedge MU$ for any spectrum $Y$; so it is not the extension of scalars of any framed or spherically framed realization of $\Sigma_H$ or $\Sigma_Q$, for any framing. We do not prove that no construction from the HW analytic data produces a complex orientation with $k\ne0$ or $\kappa\ne0$.

**Proposition E (other sectors; immediate, with contractibility recalled from [R46, Cor. E], [R49, Thm. D(4)], [R53, Thm. A(1)]; §7).** For the isotropic [R46] and Klein [R49] categories, the $SU(2)\times SU(2)$ category $\Sigma_2\cong C(2)$ [R49, Thm. D], the cube category $C(3)$, and the above-fold category $\Sigma_E$ [R33, Thm. 3(3)], the compatible complex orientation is unique up to concordance. Each resulting $MU$-module is a base change: contractible for the first three and for $C(3)$, and $(S^1\vee S^4)\wedge MU$ for $\Sigma_E$. Only the uniqueness of the complex orientation is added, and it is immediate from Theorem A.

### 1.3 Relation to published work

* *Recalled from the rStation series, not claimed.* The HW categories $\Sigma_H$, $\Sigma_Q$, $\Sigma_E$, the isotropic, Klein and $SU(2)\times SU(2)$ categories and their realizations [R32, R33, R34, R46, R49]; their contractibility for every coherent framing [R46, Cor. E], [R49, Thm. D(4)], [R53, Thm. A(1)]; the spherical realizations $X_0,X_1$ and the class $\eta^2$ [R53, Thm. A]; the Nahm-pole Lagrangian statement [R53, Thm. D]; hypothesis (Cmp) [R53, §6.4].
* *Method credited to [R53].* The normalization of coherent cocycles on categories with points, intervals and squares, with the classifying group a cokernel of the interval–square incidence map, is [R53, §3.2, Prop. 3.3]; the quadrupole incidence calculation (each interval lies in exactly two squares, and the image of the incidence map is the kernel of the sum over squares) is [R53, §4.3]. Our Lemma 3.3 and the proof of Theorem 4.4 follow this method. The reduction of $\kappa$ modulo $2$ is the sum over squares used there.
* *Comparison with Porcelli–Smith [11, §2.6].* In the cotangent-sphere example [11, Ex. 2.27], $X=T^*S^d$ with two zero-sections $L,K$ whose tangential structures differ by $(\alpha,\beta)\in\pi_dO\oplus\pi_{d-1}\mathbb S$ gives a two-object flow category with the single morphism space $S^{d-1}$. For $d\equiv3\bmod4$ an integer change $\alpha\in\pi_dO\cong\mathbb Z$ makes the stable tangent bundle of $S^{d-1}$ non-trivial, with non-zero Chern character, so its class is not in the image of $\pi_{d-1}\mathbb S$; assuming their Conjecture 5.10 respects cones, the Floer module is the cone of this class and is not a base change from $\mathbb S$. For $d=3$ this is the two-object mechanism behind our $\Sigma_H$ and the modules $M_k$, and it should be credited as anticipating it. The settings differ: [11] works over a Thom spectrum $A$ of stably complex manifolds with a $C$-orientation ($C=\mathbb S$ in the example) and under explicit conjectural hypotheses, while we work with $MU$-modules via the theorem of Hedenlund–Oldervoll and classify *all* complex orientations compatible with a framing. The extensions offered here are: the relative Chern-number formulation and integral Stokes cokernel (Theorem A), valid for general disc–interval incidences and closed surfaces; the quadrupole category, where the class is not carried by a single closed morphism manifold; and the explicit Blakey–Porcelli complexes.
* *New.* We did not find the following in the literature checked: Theorem A in the stated generality; the classification for $\Sigma_H$ and $\Sigma_Q$ with the invariants $k$ and $\kappa$; the explicit Blakey–Porcelli complexes $d_0+2b_1K$; the identification of $M_k$ and of the base-change locus on these categories; Lemma 6.2 (reframed standard orientations are $2$-torsion in $\mathrm{Cl}$). Theorem D(1) is a direct consequence of Bott periodicity.
* *Not new, but given an elementary proof.* Theorem C is a special case of [3, Cor. 7.4]. Theorem B(3) is immediate from the torsion-freeness of $\pi_2MU$.
* *Imported, with exact statements where used.*
  * $\mathrm{Flow}^U\simeq\mathrm{Mod}_{MU}$, compatibly with base change from framed categories [2], [3, (7.9)].
  * The Chern-character isomorphism $\pi_*(-)\otimes\mathbb C\cong H_*(CM_*(-,\mathrm{ch};\mathbb C[b]))$ [3, Cor. 4.18].
  * Cofibres and closed-manifold morphisms in $\mathrm{Flow}^\mu$ [2, §3.7, Thm. 0.0.6].
  * Base change to $H\mathbb Z$ giving the Morse complex [3, (1.2), Cor. 2.25], [1].
  * The index equivalence $\Omega(U/O)\simeq\mathbb Z\times BO$ [2, Ex. 0.0.9].
  * Bott periodicity, $MU_*=\mathbb Z[x_1,x_2,\dots]$, and the detection of $\Omega^U_*$ by Chern numbers [6–9].
* *Not claimed.*
  * We do not identify the integer $\lambda$ of Theorem B(2) with $\pm\kappa$ (Conjecture 4.6).
  * We do not prove a general classification of complex orientations by maps out of a classifying space (Remark 3.7).
  * We do not claim that the HW analytic data select the class $0$, or exclude $k\ne0$ (Remark 6.4).
  * We do not construct product flow categories, nor HW categories beyond those cited.

## 2. Complex orientations relative to a framing

### 2.1 Framed flow categories and complex orientations

**Definition 2.1 (framed flow category).** A *framed flow category* $X$ consists of:
* a finite set $\mathrm{Ob}$ with a grading $\mu:\mathrm{Ob}\to\mathbb Z$;
* compact smooth manifolds with corners $X(a,c)$ of dimension $\mu(a)-\mu(c)-1$ (empty unless $\mu(a)>\mu(c)$), with associative compositions $X(b,c)\times X(a,b)\to X(a,c)$ that are diffeomorphisms onto boundary faces, where $\partial X(a,c)=\bigcup_bX(b,c)\times X(a,b)$, as in [1] and [3, §2.1];
* integers $N(a)$ with $N(a)-N(c)\ge2$ whenever $X(a,c)\neq\emptyset$;
* real vector bundles $E_{ac}\to X(a,c)$ of rank $2N_{ac}$, $N_{ac}:=N(a)-N(c)$, stably isomorphic to the rank-$0$ index bundle $TX(a,c)\oplus\mathbb R\oplus V_c-V_a$ of [3, (2.44)], with associative isomorphisms $E_{ac}|_{X(b,c)\times X(a,b)}\cong E_{bc}\boxplus E_{ab}$;
* trivializations $\tau_{ac}:E_{ac}\cong X(a,c)\times\mathbb R^{2N_{ac}}$ compatible with these isomorphisms and with the standard splitting
$$\mathbb R^{2N_{ac}}=\mathbb C^{N_{ac}}=\mathbb C^{N_{bc}}\oplus\mathbb C^{N_{ab}}.$$

The trivializations orient each $E_{ac}$, hence each $X(a,c)$, once the object orientations are fixed. The Morse differential $d_0$ is the signed count of the $0$-dimensional morphism spaces. With the Koszul conventions of [3, Lemma 2.17–Cor. 2.20], [1], the orientation of a face $X(b,c)\times X(a,b)\subset\partial X(a,c)$ differs from the product orientation by a sign that depends only on $\mu(a),\mu(b),\mu(c)$. This is what makes $d_0^2=0$.

**Definition 2.2 (complex orientation compatible with the framing).** A *complex orientation compatible with $\tau$* is a family of continuous maps
$$J_{ac}:X(a,c)\to\mathcal J^+_{N_{ac}},\qquad J_{ac}(y\circ x)=J_{bc}(y)\oplus J_{ab}(x)\quad(x\in X(a,b),\ y\in X(b,c)),$$
where $\oplus$ is block sum in the splitting of Definition 2.1.
* The *index bundle* is the complex virtual bundle $I_J(a,c):=(E_{ac},\tau^*J_{ac})-\mathbb C^{N_{ac}}$, of rank $0$. Together with the given real isomorphisms, the $I_J(a,c)$ are the data (2)–(4) of [3, Def. 2.21] with $W=0$, decorated as in [3, Def. 2.22] by the framing.
* A *concordance* is a compatible complex orientation of $X\times[0,1]$, i.e. a path $t\mapsto J^t$ through such families.
* The *standard orientation* is $J^{\rm std}_{ac}\equiv J_0$. It is the image of the framed category under the base-change functor $\iota:\mathrm{Flow}^{\rm fr}\to\mathrm{Flow}^U$ of [3, (7.5)].
* *Stabilization* replaces $N$ by $N+N'$ (with $N'(a)-N'(c)\ge0$) and $J$ by $J\oplus J_0$.

We write $\mathrm{Cl}(X)=\mathrm{Cl}(X,\tau)$ for the set of concordance classes.

**Lemma 2.3 (the space of complex structures).** Let $N\ge2$.
1. $\mathcal J_N$ has two components, and $\mathcal J_N^+=SO(2N)/U(N)$.
2. The stabilization $\mathcal J_N^+\to\mathcal J_{N+1}^+$, $J\mapsto J\oplus J_0$, is $(2N-1)$-connected.
3. $\pi_1(\mathcal J_N^+)=0$ and $\pi_2(\mathcal J_N^+)\cong\mathbb Z$.
4. Let $\gamma\to\mathcal J_N$ be the tautological complex bundle $(\mathbb R^{2N},J)$. The homomorphism $\pi_2(\mathcal J^+_N)\to\mathbb Z$, $[f]\mapsto\langle c_1(f^*\gamma),[S^2]\rangle$, is injective with image $2\mathbb Z$.

Stably, $\mathcal J_\infty=O/U\simeq\operatorname{hofib}(BU\to BO)$, and $\pi_k(O/U)=\pi_{k+1}(O)$.

*Proof.*
1. $O(2N)$ acts transitively by conjugation with stabilizer $U(N)$. The two components are distinguished by the induced orientation.
2. $SO(2N+2)/U(N+1)\cong SO(2N+1)/U(N)$, which fibres over $S^{2N}=SO(2N+1)/SO(2N)$ with fibre $SO(2N)/U(N)$. The long exact sequence gives the connectivity.
3. and 4. The fibration $SO(2N)/U(N)\to BU(N)\to BSO(2N)$ classifies $\gamma$. Its exact sequence reads
$$\pi_3BSO(2N)=\pi_2SO(2N)=0\to\pi_2(\mathcal J^+)\to\pi_2BU(N)=\mathbb Z\xrightarrow{\ r\ }\pi_2BSO(2N)=\mathbb Z/2\to\pi_1(\mathcal J^+)\to\pi_1BU(N)=0.$$
   The map $r$ is realification, which reduces $c_1$ mod $2$ to $w_2$. It is onto, since $\mathcal O(1)\to\mathbb{CP}^1$ has $w_2\ne0$. Hence $\pi_1(\mathcal J^+)=0$, and $\pi_2(\mathcal J^+)\cong\ker r=2\mathbb Z$ via $c_1$.

The stable statement is the sequence $U\to O\to O/U\to BU\to BO$ together with Bott's $O/U\simeq\Omega O$ [6]; equivalently, $\pi_k(O/U)$ follows from the exact sequence of $O/U\to BU\to BO$ and the realification maps $r_*$ ($r_*=1$ on $\pi_4$, $r_*=2$ on $\pi_8$). ∎

By (2), the hypothesis $N(a)-N(c)\ge2$ puts every space of dimension $\le2$ in the stable range. Hence $\mathrm{Cl}(X)$ does not change under stabilization, by the obstruction-theoretic arguments of §3.

### 2.2 Which coefficient?

**Remark 2.4 (the delooping).** The classifying data live in $B(O/U)$, where $\pi_k(B(O/U))=\pi_{k-1}(O/U)=\pi_k(O)$; in fact $B(O/U)\simeq SO$. With morphism spaces of dimension $\le d-1$, only $\pi_k(O/U)$ with $k\le d-1$ can enter. For $d\le6$ the only non-zero group with $1\le k\le d-1$ is $\pi_2(O/U)=\mathbb Z$.

**Remark 2.5 ($U/O$ versus $O/U$).** $U/O$ is the stable Lagrangian Grassmannian, and $\Omega(U/O)\simeq\mathbb Z\times BO$. It governs the *real* index of operators with Lagrangian boundary conditions [2, Ex. 0.0.9]. Its groups $\pi_k(U/O)=\pi_{k-1}(\mathbb Z\times BO)=\mathbb Z,\mathbb Z/2,\mathbb Z/2,0,\mathbb Z,0,0,0$ ($k=1,\dots,8$) are different from those of $O/U$. Complex orientations relative to a real trivialization are lifts along $BU\to BO$, whose fibre is $O/U$.

**Remark 2.6 (cocycles acting on complex orientations).**
1. *$U$-valued cocycles* $u_{ac}:X(a,c)\to U(N_{ac})$, multiplicative under block sum, change a complex trivialization. They fix $J$, because $uJ_0u^{-1}=J_0$. They classify complex reframings of a complex-framed category, and for a two-object category with $X(a,b)=S^2$ these form $\pi_2(U)=0$.
2. *$SO$-valued cocycles* $g$ (vector-bundle reframings, [R53, §3.1]) transport complex structures by conjugation; this gives isomorphic complex bundles and preserves $c_1$. The standard orientation of the reframed category $g\tau$ is, relative to $\tau$, the orientation $g^{-1}J_0g$, i.e. the image of $g$ under $SO\to SO/U$. Its concordance class is computed in Lemma 6.2: it is $2$-torsion in $\mathrm{Cl}$, hence $0$ on $\Sigma_H$ and $\Sigma_Q$.
3. *Spherical ($GL_1\mathbb S$-) reframings* have no action on vector-bundle complex structures.

## 3. Theorem A: classification for categories with moduli of dimension $\le2$

Throughout this section $X$ satisfies the hypotheses of Theorem A. A component of dimension $k$ has boundary faces made of products of components of dimension $<k$. For a disc component $Q$ the faces are $1$-dimensional, hence of the form $\{x\}\times J$ or $J\times\{z\}$ with $x,z$ points and $J$ an interval.

### 3.1 Relative Chern numbers

**Definition 3.1.** Let $S$ be a compact oriented surface, and let $f:S\to\mathcal J_N^+$ with $f\equiv J_0$ on $\partial S$. Then $f^*\gamma|_{\partial S}=\partial S\times\mathbb C^N$ canonically. Define
$$c(f):=\langle c_1(f^*\gamma,\mathrm{triv}_{\partial S}),[S,\partial S]\rangle\in\mathbb Z,$$
the relative first Chern number.

**Lemma 3.2.**
1. *(Gluing.)* $c$ is additive when surfaces are glued along boundary arcs or circles on which $f=J_0$.
2. *(Block sum.)* $c(f\oplus J_0)=c(f)$, and $c(f)$ changes sign with the orientation of $S$.
3. *(Chern–Weil.)* For every unitary connection on $f^*\gamma$ that equals the trivial connection near $\partial S$, $c(f)=\int_S\mathrm{ch}_1$.
4. *(Discs and spheres.)* On $(D^2,\partial D^2)$, $f$ is homotopic rel boundary to $J_0$ iff $c(f)=0$, and every value in $2\mathbb Z$ occurs. On a closed oriented surface $S$, the free homotopy classes $[S,\mathcal J^+_N]$ correspond bijectively to $2\mathbb Z$ via $c$.
5. *(Boundaries.)* If $S=\partial Y$ for a compact oriented $3$-manifold $Y$ and $f$ extends over $Y$, then $c(f)=0$.

*Proof.*
1. Relative Chern classes are additive under such gluing.
2. The trivial summand contributes nothing.
3. Chern–Weil with compact support in the interior.
4. Relative homotopy classes $(D^2,\partial)\to(\mathcal J^+,J_0)$ form $\pi_2(\mathcal J^+)$, and Lemma 2.3(4) applies. For closed $S$: $\mathcal J^+\to P_2\mathcal J^+=K(\mathbb Z,2)$ is $3$-connected and $\dim S=2$, so $[S,\mathcal J^+]=H^2(S;\pi_2)=\mathbb Z$, detected by $c_1$ with image $2\mathbb Z$.
5. $\langle c_1,\partial[Y]\rangle=0$. ∎

### 3.2 Normalization and the Stokes formula

The normalization below follows [R53, §3.2, Prop. 3.3], where coherent $GL_1\mathbb S$-cocycles are normalized on points and intervals and the remaining classes on squares are read off modulo the image of the interval–square incidence map. Here the target is $\mathcal J^+$ instead of a group, the level-$1$ obstruction vanishes because $\pi_1(\mathcal J^+)=0$, and the square classes are integers, recorded by relative Chern numbers.

A compatible complex orientation is *normalized* if $J\equiv J_0$ on all points and intervals. Then on a disc component $Q$, $J_Q|_{\partial Q}=J_0$, because each face carries $J_J\oplus J_x=J_0$. So $c(J_Q)\in2\mathbb Z$ is defined.

**Lemma 3.3 (normalization).**
1. Every compatible complex orientation is concordant to a normalized one.
2. Every concordance $H$ between normalized orientations can be deformed, rel $X\times\{0,1\}$, to one that is $J_0$ on all points.

*Proof.*
1. We build a concordance by induction on the dimension of components; the faces of a component involve only components of lower dimension.
   * On each point $x$, choose a path from $J(x)$ to $J_0$ in the connected space $\mathcal J^+$.
   * On an interval $J$, the concordance is prescribed on $\partial J\times[0,1]$ by the block sums of the paths at the endpoints. Since $J\times\{0\}\cup\partial J\times[0,1]$ is a retract of $J\times[0,1]$, it extends.
   * At time $1$ the interval carries a map $(J,\partial J)\to(\mathcal J^+,J_0)$. It is homotopic rel $\partial J$ to $J_0$ since $\pi_1(\mathcal J^+)=0$; append this homotopy.
   * On disc and closed-surface components, the concordance is prescribed on $\partial Q\times[0,1]\cup Q\times\{0\}$, coherently because block sum is associative. It extends by the homotopy extension property.
2. On a point, $H$ is a loop at $J_0$. It is null-homotopic rel endpoints since $\pi_1(\mathcal J^+)=0$. Extending these homotopies of paths over intervals and discs, rel $X\times\{0,1\}$, is again homotopy extension. ∎

Let $H$ be a concordance from $J$ to $J'$ (both normalized) that is $J_0$ on points. On an interval $J$ (oriented by the framing), $H|_{J\times[0,1]}$ equals $J_0$ on $\partial(J\times[0,1])$. Set $m_J(H):=\tfrac12c(H|_{J\times[0,1]})$. For a disc $Q$ set $k_Q(J):=\tfrac12c(J_Q)$, and for a closed surface $S$ set $k_S(J):=\tfrac12c(J_S)$.

**Lemma 3.4 (Stokes formula).** There are signs $\varepsilon(Q,F)\in\{\pm1\}$, depending only on the oriented manifolds with corners, such that
$$k_Q(J')-k_Q(J)=\sum_{F\subset\partial Q}\varepsilon(Q,F)\,m_{J(F)}(H)=:T_X(m(H))_Q$$
for every disc $Q$, and $k_S(J')=k_S(J)$ for every closed surface $S$. Here $J(F)$ is the interval factor of the face $F$. Explicitly, $\varepsilon(Q,F)$ is the product of three signs:
* the sign of the point factor (its framing sign);
* the Koszul sign comparing the face orientation of $F\subset\partial Q$ with the product orientation;
* the sign $(-1)^{\dim Q}$ from $\partial(Q\times[0,1])=\partial Q\times[0,1]\cup(-1)^{\dim Q}(Q\times\{1\}-Q\times\{0\})$.

*Proof.* $H$ is defined on $Q\times[0,1]$, so $c(H|_{\partial(Q\times[0,1])})=0$ by Lemma 3.2(5). On $\partial(Q\times[0,1])$ the map is $J_0$ except on the interiors of the pieces:
* $Q\times\{0\}$, carrying $J_Q$;
* $Q\times\{1\}$, carrying $J'_Q$;
* $F\times[0,1]$ for each face $F=\{x\}\times J$, carrying $H_J\oplus J_0$, and similarly for $J\times\{z\}$.

Additivity (Lemma 3.2(1)) gives
$$\pm\big(c(J'_Q)-c(J_Q)\big)+\sum_F\pm c(H_J\oplus J_0)=0.$$
By Lemma 3.2(2), $c(H_J\oplus J_0)=\pm c(H_J)=\pm2m_J$, with the orientation comparison as stated. For a closed surface $S$, $\partial(S\times[0,1])=S\times\{1\}-S\times\{0\}$, so $c(J'_S)=c(J_S)$. ∎

### 3.3 Proof of Theorem A

Define
$$\Psi:\{\text{normalized orientations}\}\to\mathbb Z^{\mathcal S_\partial}\oplus\mathbb Z^{\mathcal S_\circ},\qquad J\mapsto\big((k_Q(J))_Q,(k_S(J))_S\big).$$

1. *Existence.* $J^{\rm std}$ is compatible, since $J_0\oplus J_0=J_0$.
2. *$\Psi$ is onto.* Given integers $k_Q$ and $k_S$, choose $f_Q:(Q,\partial Q)\to(\mathcal J^+,J_0)$ with $c(f_Q)=2k_Q$ and $f_S:S\to\mathcal J^+$ with $c(f_S)=2k_S$ (Lemma 3.2(4)). Put $J_0$ on points and intervals. The family is coherent because all faces carry $J_0$.
3. *Concordant normalized orientations have $\Psi$-values that differ by an element of $T_X(\mathbb Z^{\mathcal I})\oplus0$.* This is Lemma 3.3(2) followed by Lemma 3.4.
4. *Conversely, if $\Psi(J')-\Psi(J)=(T_X(m),0)$, then $J\simeq J'$.*
   * Put $H=J_0$ on points.
   * On each interval $J$, put a map $H_J:(J\times[0,1],\partial)\to(\mathcal J^+,J_0)$ with $c(H_J)=2m_J$ (Lemma 3.2(4)).
   * On a disc $Q$, $H$ is now prescribed on the $2$-sphere $\partial(Q\times[0,1])$. By the computation in the proof of Lemma 3.4, the relative Chern number of this map is $\pm2\big(k_Q(J')-k_Q(J)-T_X(m)_Q\big)=0$. So the map extends over the $3$-ball $Q\times[0,1]$ (Lemma 3.2(4) for $S^2$).
   * On a closed surface $S$, $J_S\simeq J'_S$ by Lemma 3.2(4).
   * The resulting family is coherent by construction.

By Lemma 3.3(1), every class contains normalized representatives, and 3–4 show that $\Psi$ descends to a bijection
$$\mathrm{Cl}(X)\cong\mathbb Z^{\mathcal S_\partial}/T_X(\mathbb Z^{\mathcal I})\oplus\mathbb Z^{\mathcal S_\circ}.$$
Naturality: a framing-preserving isomorphism of categories permutes components and preserves $\varepsilon$. Stabilization preserves $c$ by Lemma 3.2(2). ∎

**Corollary 3.5.** Assume in addition that for each pair $(a,c)$ with $\mu(a)-\mu(c)=3$ the space $X(a,c)$ has at most one component, and that every such component is a disc. Then $T_X$ has the commutator form
$$T_X(M)=\sigma_1\,M d_0+\sigma_2\,d_0M\qquad(\sigma_1,\sigma_2\in\{\pm1\}\text{ depending only on gradings}),$$
restricted to the entries of index difference $3$. Here $M$ is the matrix with entries $m_J$ on the pairs of index difference $2$ (one interval per pair), and $K=(k_Q)$ is read as a matrix on the pairs of index difference $3$.

*Proof.* A face $\{x\}\times J$ of $Q\subset X(a,c)$ with $x\in X(a,b)$ and $J\subset X(b,c)$ contributes $\pm(d_0)_{ba}\,m_J$. The sign is the framing sign of $x$, which is the matrix entry $(d_0)_{ba}$, times a Koszul sign depending on $\mu(a),\mu(b),\mu(c)$ only (Definition 2.1). The faces $J\times\{z\}$ are similar. ∎

**Remark 3.6 (the sign independence that we use).** In Corollary 3.5 the image of $T_X$ does not depend on $\sigma_1,\sigma_2$: replacing $M$ by $-M$ on one block absorbs a sign. It is also invariant under simultaneous sign changes of rows and columns of $d_0$ (object reorientations). So $\operatorname{coker}T_X$ is determined by the unsigned incidence pattern together with $d_0$ up to these sign changes.

**Remark 3.7 (comparison with classifying spaces; heuristic).** For a two-object category with $X(a,b)=S^2$ and no compositions, the classifying space is the unreduced suspension $SS^2=S^3$. Pointed maps $(S^3,\{a,b\})\to(B(O/U),*)$ form $\pi_3B(O/U)\times\pi_1B(O/U)=\pi_2(O/U)\times\pi_0(O/U)=\mathbb Z\times\mathbb Z/2$: the $\mathbb Z/2$ is the orientation normalization and the $\mathbb Z$ is $k$ of Theorem B(1). For $\Sigma_Q$, which is isomorphic to a Morse–Smale category on $S^3$ [R33, Thm. 1(2)], one expects its classifying space to be $S^3$ [5, 10], and Theorem B(2) gives the predicted answer $\pi_2(O/U)=\mathbb Z$. We prove no general statement of the form $\mathrm{Cl}(X)\cong[(BX,\mathrm{Ob}),(B(O/U),*)]/(\text{orientation})$. Theorem A is the unconditional statement for moduli of dimension $\le2$, which covers all HW categories considered here.

## 4. Theorem B: the height and quadrupole categories

### 4.1 Imported facts about $MU$-modules

* **(I1)** $\mathrm{Flow}^U\simeq\mathrm{Mod}_{MU}$ [2], [3, Rem. 1.11]. Under this equivalence the base-change functor $\iota$ from framed flow categories corresponds to $-\wedge MU:\mathrm{Sp}\to\mathrm{Mod}_{MU}$ [3, (7.9)]. Concordant complex orientations give equivalent objects: structures are homotopical [2, after Def. 0.0.2].
* **(I2)** For a decorated complex-oriented flow category $X$, $\pi_*(F^U(X))\otimes\mathbb C\cong H_*(CM_*(X,\exp\mathrm{ch}(I);\mathbb C[b]))$, where $F^U(X)$ is the associated $MU$-module [3, Cor. 4.18]. The differential is $\partial x=\sum_y\big(\int_{X(x,y)}\exp\sum_{\rho\ge1}\mathrm{ch}_\rho(I)b_\rho\big)\,y$, for Hermitian connections chosen coherently with faces [3, (4.6), Constr. 4.16]. ($I$ has rank $0$, so $\mathrm{ch}_0(I)=0$.) The homology does not depend on the coherent choice [3, §1.4].
* **(I3)** A two-object complex-oriented category with a single closed morphism manifold $M$ of dimension $n-1$ between objects of degrees $p+n$ and $p$ corresponds to the cofibre of the class $[M]\in\Omega^U_{n-1}=\pi_{n-1}MU$, viewed as a map $\Sigma^{p+n-1}MU\to\Sigma^pMU$. This is because morphisms between one-object categories are closed structured manifolds up to bordism [2, Thm. 0.0.6], and cofibres are mapping cones [2, Lemma 3.7.12].
* **(I4)** $H\mathbb Z\otimes_{MU}F^U(X)$ is the Morse chain complex of the underlying oriented category [3, (1.2), Cor. 2.25], [1].
* **(I5)** $MU_*=\mathbb Z[x_1,x_2,\dots]$ with $x_1=[\mathbb{CP}^1]$. Chern numbers detect $\Omega^U_*$; in degree $2$, $[M]\mapsto c_1[M]$ is injective with image $2\mathbb Z$ [7, 8]. The Conner–Floyd orientation $MU\to KU$ sends $x_1$ to $\mathrm{Td}(\mathbb{CP}^1)\beta=\beta$ [9].

### 4.2 Two-cell $MU$-modules

**Proposition 4.1.** For $\lambda\in\mathbb Z$ let $M_\lambda=\operatorname{cofib}(\lambda x_1:\Sigma^3MU\to\Sigma MU)$.
1. $\pi_n(M_\lambda)=(MU_*/\lambda x_1)_{n-1}$ for $\lambda\ne0$, and $\pi_*(M_0)=MU_{*-1}\oplus MU_{*-4}$. In particular $\pi_3(M_\lambda)=\mathbb Z/|\lambda|$ ($\mathbb Z$ for $\lambda=0$).
2. $M_\lambda\simeq M_{\lambda'}$ as $MU$-modules iff $|\lambda|=|\lambda'|$.
3. $M_\lambda\simeq Y\wedge MU$ for some spectrum $Y$ iff $\lambda=0$. Moreover $M_0\simeq X_0\wedge MU\simeq X_1\wedge MU$.
4. $\pi_3(KU\otimes_{MU}M_\lambda)=\mathbb Z/|\lambda|$.
5. Every connective $MU$-module $M$ with $H_*(H\mathbb Z\otimes_{MU}M)\cong\mathbb Z[1]\oplus\mathbb Z[4]$ is equivalent to some $M_\lambda$.

*Proof.*
1. Use the long exact sequence of the cofibre, and the fact that multiplication by $\lambda x_1$ on the domain $MU_*$ is injective for $\lambda\ne0$; the cokernel in degree $2j+2$ is $(\mathbb Z/\lambda)^{p(j)}\oplus\mathbb Z^{p(j+1)-p(j)}$.
2. The group $\pi_3$ distinguishes different $|\lambda|$. Conversely, $-1$ on $\Sigma^3MU$ identifies $M_\lambda$ with $M_{-\lambda}$.
3. *If.* $M_0=\Sigma MU\vee\Sigma^4MU=(S^1\vee S^4)\wedge MU$. Since $\pi_2^s=\mathbb Z/2$ and $\pi_2MU=\mathbb Z$ is torsion-free, the unit kills $\eta^2$. So $X_1\wedge MU=\operatorname{cofib}(\eta^2)\wedge MU=\operatorname{cofib}(0)=M_0$.

   *Only if.* Suppose $\lambda\ne0$ and $M_\lambda\simeq Y\wedge MU$.
   * Rationalization is smashing, so $\pi_*(Y\wedge MU)\otimes\mathbb Q=\pi_*(Y\wedge MU\wedge H\mathbb Q)$.
   * $Y\wedge H\mathbb Q$ is an $H\mathbb Q$-module, hence a wedge of shifts $\bigvee\Sigma^{n_i}H\mathbb Q$. Therefore $Y\wedge MU\wedge H\mathbb Q\simeq\bigvee\Sigma^{n_i}(MU\wedge H\mathbb Q)$, and $\pi_*(Y\wedge MU)\otimes\mathbb Q$ is a free $MU_*\otimes\mathbb Q$-module.
   * On a free module over the domain $MU_*\otimes\mathbb Q$, multiplication by $x_1$ is injective. But in $\pi_*(M_\lambda)\otimes\mathbb Q=\Sigma(MU_*\otimes\mathbb Q)/(x_1)$, the bottom class $\iota_1\ne0$ satisfies $x_1\iota_1=0$.4. $KU\otimes_{MU}M_\lambda=\operatorname{cofib}(\lambda\beta:\Sigma^3KU\to\Sigma KU)$ by (I5), and $\pi_3$ of this is $KU_2/\lambda\beta=\mathbb Z/|\lambda|$.
5. *First cell.* $MU\to H\mathbb Z$ is an isomorphism on $\pi_0$ and $\pi_1$ and onto on $\pi_2$. Its fibre is $1$-connected, so for a $0$-connected $M$ the map $M\to H\mathbb Z\otimes_{MU}M$ is an isomorphism on $\pi_1$ and $\pi_2$. Choose $\Sigma MU\to M$ inducing $\pi_1(M)\cong\mathbb Z$.
   * *Second cell.* The cofibre $C$ has $H_*(H\mathbb Z\otimes_{MU}C)=\mathbb Z[4]$ and is connective. By the same Hurewicz argument it is $3$-connected with $\pi_4C=\mathbb Z$. A generator $\Sigma^4MU\to C$ has cofibre with vanishing $H\mathbb Z$-homology, and that cofibre is connective, hence zero.
   * So $C\simeq\Sigma^4MU$, and $M$ is the cofibre of some map $\Sigma^3MU\to\Sigma MU$, i.e. of some $\lambda x_1\in\pi_2MU$. ∎

### 4.3 The height category $\Sigma_H$

$\Sigma_H$ has objects $P_4,P_1$ and one morphism space $X(P_4,P_1)\cong S^2$, with no compositions [R32, Thm. C′], [R33, Thm. 1(4)]. It is smooth and framed via the Morse–Smale model of [R33]. For every model framing the realization is $X_0$, and the framed sphere is $0\in\pi_2^s$ [R33, Thm. 1(4)]. By [R33, Prop. 2], the index bundle of the full linearized HW operator over the moduli space is the tangent bundle of the reduced moduli space, so these are framings of the HW index bundle.

**Theorem 4.2 (= Theorem B(1)).**
1. $\mathrm{Cl}(\Sigma_H)\cong\mathbb Z$ via $k(J)=\tfrac12\int_{S^2}c_1(I_J)$. Every $k$ occurs, and $\int_{S^2}c_1(I_J)\in2\mathbb Z$ always.
2. $[S^2,J]=k(J)[\mathbb{CP}^1]\in\Omega^U_2$.
3. *(Coherent Chern–Weil and the Blakey–Porcelli complex.)* Let $I_k=\mathcal O(2k)-\mathbb C$ with the round (Fubini–Study) connection, so that $\mathrm{ch}_1=\frac{k}{2\pi}\sin\theta\,d\theta\,d\varphi$. Then $I_k$, with the unique-up-to-homotopy stable real trivialization (since $[S^2,SO]=0$ and $w_2(\mathcal O(2k))=0$), represents the class $k$. The complex is
$$CM_*(\Sigma_H,\mathrm{ch};\mathbb C[b])=\mathbb C[b]\,P_4\oplus\mathbb C[b]\,P_1,\qquad\partial P_4=\Big(\int_{S^2}e^{\sum_\rho\mathrm{ch}_\rho b_\rho}\Big)P_1=2k\,b_1\,P_1.$$
   Its homology is free of rank $2$ if $k=0$, and is $\Sigma\,\mathbb C[b]/(b_1)$ if $k\neq0$.
4. $F^U(\Sigma_H,J)\simeq M_{k(J)}$. Hence the $MU$-modules realized by complex orientations of $\Sigma_H$ are exactly the $M_k$, $k\in\mathbb Z$. They are pairwise distinct up to sign, detected by $\pi_3=\mathbb Z/|k|$ and by $KU$, and $M_k$ is a base change from $\mathbb S$ iff $k=0$.

*Proof.*
1. $S^2$ is a closed-surface component and there are no other components of positive dimension. Theorem A gives $\mathrm{Cl}\cong\mathbb Z$ via $\tfrac12c$, and $c=\int c_1$ by Lemma 3.2(3).
2. The stable tangent bundle of $S^2$ is identified with $I_J$ up to trivial summands, so $c_1[S^2,J]=2k$. By (I5), $c_1[\mathbb{CP}^1]=2$, and $c_1$ is injective on $\Omega^U_2$.
3. $c_1(\mathcal O(2k))=2k$, and the underlying real bundle is stably trivial because $w_2=0$. On $S^2$ only the form-degree-$2$ part of $\exp(\sum\mathrm{ch}_\rho b_\rho)$ integrates, namely $\mathrm{ch}_1b_1$. Coherence is vacuous since there are no compositions. The homology over the graded PID $\mathbb C[b_1]$, tensored with the flat extension $\mathbb C[b]$, is as stated.
4. (I3) gives the cofibre of $[S^2,J]=k x_1$. Then apply Proposition 4.1. As a consistency check, (I2) and Prop. 4.17 of [3] send $x_1\mapsto2b_1$, matching $\partial P_4=2kb_1P_1$. ∎

### 4.4 The quadrupole category $\Sigma_Q$

$\Sigma_Q$ has objects $P_a^\pm$ with $\mu(P_a^\pm)=a\in\{1,2,3,4\}$ [R32, Thm. C], [R33, Thm. 1].
* Each $X(P_a^s,P_{a-1}^t)$ is one point (12 in all).
* Each $X(P_a^s,P_{a-2}^t)$ is an interval whose ends are the broken trajectories through $P_{a-1}^\pm$ (8 in all).
* Each $X(P_4^s,P_1^t)$ is a square $Q_{st}$ whose four faces are $X(P_3^u,P_1^t)\times X(P_4^s,P_3^u)$ and $X(P_2^v,P_1^t)\times X(P_4^s,P_2^v)$ ($u,v=\pm$).

Each interval is a face of exactly two squares; this incidence pattern is the one computed in [R53, §4.3]. The smooth corner structure and framings come from the Morse–Smale model [R33, Thm. 1(3)]. For every model framing the realization is $X_0$ [R33, Thm. 1(4)], so the Morse complex
$$\mathbb Z^2\xrightarrow{n^{43}}\mathbb Z^2\xrightarrow{n^{32}}\mathbb Z^2\xrightarrow{n^{21}}\mathbb Z^2$$
(degrees $4\to1$, entries $\pm1$) has homology $\mathbb Z,0,0,\mathbb Z$.

**Lemma 4.3.** Each $n^{a,a-1}$ has rank $1$, so $n^{a,a-1}=u\,w^{\sf T}$ with $u,w\in\{\pm1\}^2$. Up to object reorientations, $n^{43}=n^{21}=\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}$ in suitable bases. Let $\alpha\in\ker n^{43}$ and $\beta\in\ker(n^{21})^{\sf T}$ be primitive; up to sign $\alpha=\beta=(1,-1)^{\sf T}$ in these bases.

*Proof.* $H_4=\ker n^{43}=\mathbb Z$ and $H_1=\operatorname{coker}n^{21}=\mathbb Z$ force ranks $1$ at the two ends. Then $H_3=H_2=0$ forces $\operatorname{rank}n^{32}=1$. A $\pm1$-matrix of rank $1$ is $uw^{\sf T}$, and object reorientations change the signs of $u$ and $w$. ∎

Let $J$ be normalized and $K(J)\in\mathbb Z^{2\times2}$, $K_{ts}=k_{Q_{st}}(J)=\tfrac12c(J|_{Q_{st}})$. Define
$$\kappa(J):=\beta^{\sf T}K(J)\,\alpha\in\mathbb Z,$$
and extend $\kappa$ to all orientations by Lemma 3.3(1). The sign of $\kappa$ depends on the choice of generators $\alpha,\beta$ of $H_4$ and $H^1$; we fix them by the framing.

**Theorem 4.4 (= Theorem B(2), classification).** $\kappa$ is well defined, and $\kappa:\mathrm{Cl}(\Sigma_Q)\to\mathbb Z$ is a bijection.

*Proof.* By Theorem A and Corollary 3.5, $\mathrm{Cl}(\Sigma_Q)=\mathbb Z^{2\times2}/\operatorname{im}T$ with
$$\operatorname{im}T=\{\sigma_1m^{31}n^{43}+\sigma_2n^{21}m^{42}\}=\{m^{31}n^{43}+n^{21}m^{42}:\ m^{31},m^{42}\in\mathbb Z^{2\times2}\}$$
(Remark 3.6). By Lemma 4.3 and Remark 3.6 we may take $n^{43}=n^{21}=\mathbf 1\mathbf 1^{\sf T}$, with $\mathbf 1=(1,1)^{\sf T}$. Then $m^{31}n^{43}=p\,\mathbf 1^{\sf T}$ and $n^{21}m^{42}=\mathbf 1\,q^{\sf T}$, with $p=m^{31}\mathbf 1$ and $q=(m^{42})^{\sf T}\mathbf 1$ arbitrary in $\mathbb Z^2$. So
$$\operatorname{im}T=\{(p_t+q_s)_{t,s}\}.$$
* *$\operatorname{im}T\subset\ker\kappa$.* $\kappa(K)=K_{11}-K_{12}-K_{21}+K_{22}$ vanishes on $(p_t+q_s)$.
* *$\ker\kappa\subset\operatorname{im}T$.* If $\kappa(K)=0$, put $q_1=0$, $p_1=K_{11}$, $q_2=K_{12}-K_{11}$, $p_2=K_{21}$. Then $p_2+q_2=K_{22}$.
* *$\kappa$ is onto.* $\kappa(E_{11})=1$.

Hence $\mathbb Z^{2\times2}/\operatorname{im}T\cong\mathbb Z$ via $\kappa$. ∎

Modulo $2$, $\operatorname{im}T$ reduces to the image of the incidence map of [R53, §4.3], and $\kappa\equiv\sum_{t,s}K_{ts}$ reduces to the sum over squares that detects $\Gamma_2=\mathbb Z/2$ there. Theorem 4.4 is the integral refinement of that calculation.

**Theorem 4.5 (= Theorem B(2), complexes and modules).** Let $J$ be normalized. Choose on each square a unitary connection on $(E,J_Q)$ that is trivial near $\partial Q$, and the trivial connection on points and intervals.
1. These connections are coherent with faces. The Blakey–Porcelli complex is $\mathbb C[b]\otimes\mathbb C^{\mathrm{Ob}}$ with
$$\partial=d_0+2b_1K(J),\qquad\text{i.e.}\quad\partial P_4^s=\sum_tn^{43}_{ts}P_3^t+2b_1\sum_tK_{ts}P_1^t,$$
   and $\partial P_a^s=\sum_tn^{a,a-1}_{ts}P_{a-1}^t$ for $a\le3$. No other $b$-monomials occur.
2. $H_*(CM_*)\cong\mathbb C[b]x_1\oplus\mathbb C[b]x_4$ if $\kappa(J)=0$, and $H_*(CM_*)\cong\Sigma\,\mathbb C[b]/(b_1)$ if $\kappa(J)\ne0$.
3. $F^U(\Sigma_Q,J)\simeq M_\lambda$ for an integer $\lambda=\lambda(J)$, unique up to sign, with $\lambda\ne0\iff\kappa(J)\ne0$.
4. $F^U(\Sigma_Q,J)$ is a base change $Y\wedge MU$ iff $\kappa(J)=0$, and then it is $X_0\wedge MU=M_0$.

*Proof.*
1. On faces all forms vanish, consistently with the coherence relation $m_{ac}|=m_{bc}\wedge m_{ab}$ of [3, Def. 2.28]: since $\mathrm{ch}(I)=0$ on points and intervals, $\exp$ restricts to $1$. Integrals of even-degree forms over intervals vanish. Over a point, $\int\exp(\cdot)$ is the framing sign. Over $Q_{st}$, only $\mathrm{ch}_1b_1$ integrates, giving $c(J_Q)b_1=2K_{ts}b_1$ by Lemma 3.2(3).
2. Since $d_0$ is defined over $\mathbb Z$, the homology over $\mathbb C[b_1]$ is computed by a Smith form. Conceptually: if $\kappa\ne0$, the rank-jump Lemma 5.2 with $\bar C=2\kappa$ on $H_4\to H_1$ gives $\operatorname{rank}_{\mathbb C(b_1)}\partial\ge4$, hence $=4$ (since $\partial^2=0$ on $\mathbb C^8$), so the homology is torsion, and the explicit cokernel is $\Sigma\,\mathbb C[b]/(b_1)$. If $\kappa=0$, $J$ is concordant to $J^{\rm std}$ (Theorem 4.4), for which $K=0$ and the complex is $d_0\otimes\mathbb C[b]$ with free homology; the homology is independent of the coherent choice and invariant under concordance by (I1)–(I2).
3. By (I4), $H\mathbb Z\otimes_{MU}F^U$ is the Morse complex, with homology $\mathbb Z[1]\oplus\mathbb Z[4]$, and $F^U$ is connective (finite, cells in degrees $\ge1$). Proposition 4.1(5) gives $F^U\simeq M_\lambda$. Compare $\dim\pi_3\otimes\mathbb C$ via (I2): for $M_\lambda$ it is $0$ iff $\lambda\ne0$ (Proposition 4.1(1)); for $H_3(CM)$ it is $0$ iff $\kappa\ne0$ (part 2).
4. Proposition 4.1(3), and (I1) for $\kappa=0$: $J$ is then concordant to $J^{\rm std}=\iota(\tau)$, whose module is $X_0\wedge MU$. ∎

**Conjecture 4.6.** $|\lambda(J)|=|\kappa(J)|$ for every complex orientation of $\Sigma_Q$.

*Evidence.* The four squares glue along their interval faces into a closed surface with $\chi=4-8+4=0$. For a normalized $J$ they carry a complex structure whose Chern number is $\pm2\kappa$ for a suitable choice of signs. A flow-categorical cancellation of the six middle objects should exhibit $F^U(\Sigma_Q,J)$ as the cone on the bordism class of this surface, as in (I3). We have not proved the cancellation in the complex-oriented setting. Over $\mathbb C$ the Blakey–Porcelli complex only detects whether $\lambda=0$, because $\mathbb C[b]/(cb_1)\cong\mathbb C[b]/(b_1)$ for every $c\ne0$.

### 4.5 $\eta^2$ dies, integers survive

**Corollary 4.7 (= Theorem B(3); immediate, recorded as a remark).**
1. The spherical reframing class $\eta^2$ of [R53, Thm. A] maps to $0$ in $\pi_2MU$, so $X_1\wedge MU\simeq X_0\wedge MU=M_0$.
2. The $MU$-modules of complex orientations of $\Sigma_H$ form the infinite family $\{M_k\}$. The modules $M_k$, $k\neq0$, are not base changes, are distinguished by $|k|$, and are detected by $KU$, which does not distinguish $X_0$ from $X_1$ [R53, Thm. B].
3. For $\Sigma_Q$ the integer $\kappa$ is a complete invariant of the complex orientation, and $\kappa\neq0$ exactly when the module is not a base change.

*Proof.* Proposition 4.1(3)–(4), Theorems 4.2 and 4.4–4.5. ∎

## 5. Theorem C: a non-base-change criterion for small categories

**Lemma 5.1 (which $b$-monomials occur).** In $CM_*(X,\exp\mathrm{ch}(I);\mathbb C[b])$, the coefficient of $b^q=\prod b_\rho^{q_\rho}$ in $\partial a$ is a sum of integrals over the components of $X(a,c)$ of dimension $2\sum\rho q_\rho$. For morphism spaces of dimension $\le2$ only $1$ and $b_1$ occur. In dimension $4$, $b_1^2$ and $b_2$ occur; $b_2$ first requires index difference $5$.

*Proof.* $\exp(\sum\mathrm{ch}_\rho b_\rho)=\sum_q\frac{1}{q!}\prod\mathrm{ch}_\rho^{q_\rho}b^q$, and $\prod\mathrm{ch}_\rho^{q_\rho}$ has form degree $2\sum\rho q_\rho$. Only the top-degree part integrates; there are $p(w)$ admissible monomials in dimension $2w$. ∎

**Lemma 5.2 (rank jump).** Let $(V,d_0)$ be a finite-dimensional graded complex over $\mathbb C$, and let $C$ have degree $-3$ with $d_0C+Cd_0=0$ and $C^2=0$. Let $\bar C:H(V)\to H(V)$ be the induced map, and $K=\mathbb C(t)$. Then
$$\operatorname{rank}_K(d_0+tC)\ \ge\ \operatorname{rank}d_0+\operatorname{rank}\bar C,\qquad\text{so}\qquad\dim_KH(V_K,d_0+tC)\le\dim H(V)-2\operatorname{rank}\bar C.$$

*Proof.*
* *Splitting.* Choose a graded splitting $V=B'\oplus\mathcal H\oplus B$ with $B=\operatorname{im}d_0$, $\ker d_0=\mathcal H\oplus B$, and $\delta:=d_0|_{B'}:B'\to B$ an isomorphism.
* *Blocks.* $C$ preserves $\ker d_0$, because $d_0Cz=-Cd_0z=0$, and it preserves $\operatorname{im}d_0$. So $C_{B'\mathcal H}=0$, and $\bar C$ is the block $C_{\mathcal H\mathcal H}$.
* *Submatrix.* The submatrix of $d_0+tC$ with rows $\mathcal H\oplus B$ and columns $B'\oplus\mathcal H$ is
$$\begin{pmatrix}tC_{\mathcal HB'}&tC_{\mathcal H\mathcal H}\\ \delta+tC_{BB'}&tC_{B\mathcal H}\end{pmatrix}.$$
  Here $\delta+tC_{BB'}$ is invertible over $K$, since its determinant is non-zero at $t=0$. By the Schur complement, the rank is $\dim B+\operatorname{rank}_K t\big(C_{\mathcal H\mathcal H}+t(\cdots)\big)$.
* *Leading term.* A non-vanishing minor of $C_{\mathcal H\mathcal H}$ gives a minor that is a non-zero polynomial in $t$, so the Schur complement has rank $\ge\operatorname{rank}\bar C$.

The dimension statement follows from $\dim H=\dim V-2\operatorname{rank}$. ∎

**Theorem 5.3 (= Theorem C; special case of [3, Cor. 7.4]).** Let $X$ be a finite decorated complex-oriented flow category [3, Def. 2.22] whose morphism spaces have dimension $\le2$.
1. For every coherent choice of Hermitian connections, $\partial=d_0+b_1C$ with $C_{ca}=\int_{X(a,c)}\mathrm{ch}_1(I)$, which vanishes unless $\dim X(a,c)=2$.
2. $d_0C+Cd_0=0$ and $C^2=0$.
3. If $\bar C\neq0$ for one coherent choice, then $F^U(X)\not\simeq Y\wedge MU$ for every spectrum $Y$.

*Proof.*
1. Lemma 5.1.
2. By [3, Lemma 4.12], $\partial^2=0$ is an identity of $\mathbb C[b]$-linear maps. Since $b_1$ is a free variable, the coefficients of $b_1^0,b_1^1,b_1^2$ vanish separately.
3. *Setup.* Let $R=\mathbb C[b_1]$ and $F=(R\otimes\mathbb C^{\mathrm{Ob}},d_0+b_1C)$. Then $CM_*=F\otimes_R\mathbb C[b]$, and $\mathbb C[b]$ is free over $R$.
   * *Size of $H(F)$.* $H(F)$ is a finitely generated graded $R$-module, $R^a\oplus(\text{torsion})$, with $a=\dim_KH(F\otimes_RK)<\dim H_*(X;\mathbb C)$ by Lemma 5.2. Its Poincaré series $P_{H(F)}(s)$ therefore satisfies $\lim_{s\to1}(1-s^2)P_{H(F)}(s)=a$.
   * *Base change forces a larger size.* If $F^U(X)\simeq Y\wedge MU$, then by (I4) $H_*(Y;\mathbb C)\cong H_*(H\mathbb Z\otimes_{MU}F^U(X))\otimes\mathbb C=H_*(X;\mathbb C)$. By (I2) and the free-module argument of Proposition 4.1(3), $H(CM_*)$ has the Poincaré series of $\mathbb C[b]\otimes H_*(X;\mathbb C)$. Dividing by the series of $\mathbb C[b_2,b_3,\dots]$ gives $P_{H(F)}(s)=P_{H(X)}(s)/(1-s^2)$, so the limit equals $\dim H_*(X;\mathbb C)$.
   * The two limits contradict each other.

   The criterion is invariant: the number $a$ is determined by $H(CM_*)$, which does not depend on the coherent choice (I2). ∎

*Remarks.*
1. Theorem 5.3 is a special case, for small categories, of the spectral-sequence criterion [3, Cor. 7.4], with an elementary proof; we do not claim the criterion as new. $\bar Cb_1$ is the first possible differential, $d_3$, of the change-of-coefficients spectral sequence [3, (7.12)].
2. For $\Sigma_Q$ and $\Sigma_H$, $\bar C$ is $2\kappa$, respectively $2k$, on $H_4\to H_1$. So Theorem 5.3 recovers the "only if" of Theorems 4.2(4) and 4.5(4).
3. The criterion says which $b_\rho$ can appear for the HW categories, all of which have moduli of dimension $\le2$: only $b_1$, paired with $\mathrm{ch}_1$ of the index bundle on the $2$-dimensional moduli.

## 6. Theorem D: real index data and extension of scalars

### 6.1 Real index data do not determine complex orientations

Recall that the $(m-1)$-connected cover $BO\langle m\rangle\to BO$ induces an isomorphism on $\pi_i$ for $i\ge m$, and $\pi_i(BO\langle m\rangle)=0$ for $i<m$.

**Proposition 6.1 (= Theorem D(1)).** Let $m\ge0$ and $j\ge1$. Consider families of Cauchy–Riemann operators with totally real boundary conditions on the disc, in the model of [2, Ex. 0.0.9].
1. If $8j\ge m$, there is such a family parametrized by $S^{8j}$ whose index bundle is classified by a map $S^{8j}\to BO$ that lifts to $BO\langle m\rangle$, and which admits no stable complex structure.
2. If $8j<m$, every family over $S^{8j}$ whose index bundle lifts to $BO\langle m\rangle$ has stably trivial index bundle, which therefore admits a stable complex structure.
3. There is a family over $S^1$ with non-orientable index bundle.

So for each $m$, part 1 applies exactly to the $j\ge\max(1,\lceil m/8\rceil)$. The first version of this paper stated part 1 for every $j\ge1$ and every $m$; by part 2 that is false (for instance $j=1$, $m=10$).

*Proof.*
* *Realization.* The index map $\Omega(U/O)\to\mathbb Z\times BO$ of such operators is a homotopy equivalence [2, Ex. 0.0.9], so every class in $\pi_{8j}(BO)\cong\mathbb Z$ and in $\pi_1(BO)=\mathbb Z/2$ is the index of a family.
* *Part 1.* For $8j\ge m$, $\pi_{8j}(BO\langle m\rangle)\to\pi_{8j}(BO)$ is an isomorphism, so the generator $g\in\pi_{8j}BO$ lifts. Since $BU$ is simply connected, a stable complex structure on $g$ is a class in $\pi_{8j}(BU)$ mapping to $g$ under realification $r_*$. But the complexification $c_*$ is an isomorphism in degree $8j$ and $r_*c_*=2$, so $r_*$ is multiplication by $2$ [6, 9], and $g\notin\operatorname{im}r_*$.
* *Part 2.* For $8j<m$, $\pi_{8j}(BO\langle m\rangle)=0$, so the classifying map factors through a null-homotopic map. The index bundle is stably trivial, and the trivial bundle is complex.
* *Part 3.* The non-trivial class in $\pi_1BO$ is non-orientable, whereas complex bundles are oriented. ∎

*Strips.* A strip with non-degenerate ends is a disc with two boundary punctures. Capping the ends by fixed operators changes index bundles only by fixed virtual vector spaces, so the obstruction is the same for any class of strip families whose index map realizes these classes. We use Proposition 6.1 only as a statement about real index data in general; it is not a statement about the HW moduli, whose dimension is $\le2$.

So complex orientability is a genuine condition on real index data, and a complex orientation is a choice when it exists. For the HW categories it exists, because their moduli have dimension $\le2$, where the obstructions $\pi_{k-1}(O/U)$, $k\le2$, vanish (Lemma 2.3).

### 6.2 Reframed standard orientations

Let $(X,\tau)$ be framed. A *coherent $SO$-valued reframing* is a family $g_{ac}:X(a,c)\to SO(2N_{ac})$ with $g_{ac}(y\circ x)=g_{bc}(y)\oplus g_{ab}(x)$. The reframed framing is $g\tau:=g\circ\tau$, and the standard complex orientation of $(X,g\tau)$ is $(g\tau)^*J_0=\tau^*(g^{-1}J_0g)$. Relative to $\tau$ it is therefore
$$J^g_{ac}:=g_{ac}^{-1}J_0\,g_{ac}:X(a,c)\to\mathcal J^+_{N_{ac}},$$
which is compatible (block sum commutes with conjugation; $g\in SO$ preserves the component $\mathcal J^+$). By definition, the complex-oriented category $(X,\tau,J^g)$ is $\iota(X,g\tau)$.

For a complex vector bundle over a compact oriented surface $S$ with a trivialization over $\partial S$, write $c(\cdot)$ for its relative first Chern number; Definition 3.1 is the case of the identity trivialization, and additivity under gluing along matching boundary trivializations holds as in Lemma 3.2(1).

**Lemma 6.2 (reframed standard orientations).** Let $X$ satisfy the hypotheses of Theorem A, and let $g$ be a coherent $SO$-valued reframing.
1. $J^g$ is concordant to a normalized orientation $J''$ with $k_S(J'')=0$ for every closed surface $S$ and
$$2\,k_Q(J'')=\sigma\,T_X(m')_Q\quad\text{for every disc }Q,$$
for some $m'\in\mathbb Z^{\mathcal I}$ and a sign $\sigma=\pm1$ independent of $Q$.
2. Hence $2[J^g]=0$ in $\mathrm{Cl}(X,\tau)$.
3. If $\mathrm{Cl}(X,\tau)$ is torsion-free, then $[J^g]=[J^{\rm std}]$ and $\iota(X,g\tau)\simeq\iota(X,\tau)$ as $MU$-modules. This holds for $\Sigma_H$ and $\Sigma_Q$.

*Proof.*
1. *Step 1 (points).* Since $SO(2N)$ is connected, choose paths from $g(x)$ to $1$ for every point component $x$, and extend them, by induction on dimension and homotopy extension, to a homotopy of coherent $SO$-valued cocycles from $g$ to a cocycle $g_1$ with $g_1\equiv1$ on points, exactly as in Lemma 3.3(1). Applying $h\mapsto h^{-1}J_0h$ gives a concordance from $J^g$ to $J^{g_1}$.
   * *Step 2 (intervals).* On an interval $I$, $g_1|_I$ is a loop in $SO(2N)$ based at $1$; it may be non-trivial in $\pi_1(SO)=\mathbb Z/2$. But $J^{g_1}|_I:(I,\partial I)\to(\mathcal J^+,J_0)$ is null-homotopic rel $\partial I$, since $\pi_1(\mathcal J^+)=0$. Choose such a homotopy $H_I:I\times[0,1]\to\mathcal J^+$ from $J^{g_1}|_I$ to $J_0$. Normalizing as in Lemma 3.3(1) gives a normalized $J''$ concordant to $J^{g_1}$, which on a disc $Q$ is $J^{g_1}|_Q$ with collars $F\times[0,1]$ attached along the faces $F$, carrying $H_{J(F)}\oplus J_0$ (up to homotopy rel $\partial Q$, which does not change relative Chern numbers); on closed surfaces $J''=J^{g_1}$.
   * *Step 3 (Chern numbers).* For every $y$, $g_1(y):(\mathbb R^{2N},J^{g_1}(y))\to(\mathbb R^{2N},J_0)$ is complex linear, because $g_1J^{g_1}=J_0g_1$. So $g_1$ trivializes the complex bundle defined by $J^{g_1}$ on every component. On a closed surface this gives $k_S(J'')=0$. On a disc $Q$, the bundle on $Q$ has relative Chern number $0$ with respect to the trivialization $g_1|_{\partial Q}$. On a collar $F\times[0,1]$ with $F=\{x\}\times I$ or $I\times\{z\}$, put the trivialization $g_1|_I\oplus1$ on $F\times\{0\}$ and the identity on the rest of the boundary; these agree at the corners because $g_1=1$ on points. Let $m'_I:=c(H_I)\in\mathbb Z$, computed on $I\times[0,1]$ with the trivialization $g_1|_I$ on $I\times\{0\}$ and the identity elsewhere. The same interval $I$ gives the same $m'_I$ in every square containing it. Additivity gives
$$c(J''_Q)=\sigma\sum_{F\subset\partial Q}\varepsilon(Q,F)\,m'_{J(F)}=\sigma\,T_X(m')_Q .$$
     The signs are those of Lemma 3.4, since each collar $F\times[0,1]$ is oriented as $\partial Q\times[0,1]$, exactly like the piece $F\times[0,1]$ of $\partial(Q\times[0,1])$ there; $\sigma$ is the overall sign of that comparison, the same for all discs.
2. By (1), $\Psi(J'')=(\tfrac{\sigma}{2}T_X(m'),0)$, so $2\Psi(J'')=(T_X(\sigma m'),0)\in T_X(\mathbb Z^{\mathcal I})\oplus0$. By Theorem A, $2[J^g]=0$.
3. The first claim is immediate from (2). For the second, concordant complex orientations give equivalent $MU$-modules (I1). For $\Sigma_H$ and $\Sigma_Q$, $\mathrm{Cl}\cong\mathbb Z$ (Theorems 4.2, 4.4). For $\Sigma_H$ there are no intervals and $k=k_S=0$ directly. ∎

For $\Sigma_Q$ and $\Sigma_H$ the conclusion also follows from [R53, Prop. 3.3(3), Thm. A(3)–(4)]: by the vanishing of $\Gamma_0$, $\Gamma_1$ and $\pi_2(O)$ there, every $O$-reframing is, after reorientation, homotopic through coherent cocycles to the trivial one. Lemma 6.2 does not need $\Gamma_1=0$: it uses $\pi_1(\mathcal J^+)=0$ instead.

### 6.3 Extension of scalars of the framed and spherical realizations

For a framed category $(X,\tau)$ the extension of scalars of its realization is $|X|_\tau\wedge MU\simeq F^U(\iota(X,\tau))$ (I1); for a spherical ($GL_1\mathbb S$-) reframing $u\cdot g$ of [R53, §3.1] we use the extension of scalars $|X|_{u\cdot g}\wedge MU$ of the realization, since vector-bundle complex structures are not defined for such reframings.

**Theorem 6.3 (= Theorem D(2)–(3)).** Let $\Sigma\in\{\Sigma_H,\Sigma_Q\}$ and let $\tau$ be a framing of the Morse–Smale model of [R33, Thm. 1(3)].
1. For every coherent $SO$-valued reframing $g$, the standard orientation $J^g$ of $g\tau$ has class $0=[J^{\rm std}]$ in $\mathrm{Cl}(\Sigma,\tau)\cong\mathbb Z$, and
$$|\Sigma|_{g\tau}\wedge MU\ \simeq\ |\Sigma|_\tau\wedge MU\ \simeq\ X_0\wedge MU=M_0 .$$
2. For the spherical reframings of [R53, Thm. A(3)–(4)], whose realizations are $X_0$ and $X_1$, the extensions of scalars are $X_0\wedge MU\simeq X_1\wedge MU\simeq M_0$.
3. *(Conditional on (Cmp).)* Assume hypothesis (Cmp) of [R53, §6.4]: there is a coherent framing $\tau_{\rm HW}$ of $\Sigma$ that stably trivializes the HW index bundle (the reduced tangent bundle, [R33, Prop. 2]) and is related to a model framing by stable vector-bundle or topological microbundle isomorphisms compatible with faces. Then $|\Sigma|_{\tau_{\rm HW}}\simeq X_0$ [R53, Cor. C′(1)], and its extension of scalars is $M_0$. If the comparison is by $SO$-valued vector-bundle isomorphisms, then the standard orientation of $\tau_{\rm HW}$ has class $0$ in $\mathrm{Cl}(\Sigma,\tau)$, by part 1.
4. For $k\ne0$ the module $M_k$ is not equivalent to $Y\wedge MU$ for any spectrum $Y$, and the same holds for $M_\lambda$, $\lambda\ne0$. So the complex orientations of $\Sigma_H$ with $k\ne0$, and of $\Sigma_Q$ with $\kappa\ne0$, do not arise by extension of scalars from any framed or spherically framed realization of $\Sigma_H$ or $\Sigma_Q$, for any framing.

*Proof.*
1. Lemma 6.2(3), together with [R33, Thm. 1(4)] ($|\Sigma|_\tau\simeq X_0$ for every model framing) and (I1).
2. Proposition 4.1(3) ($\eta^2\mapsto0$ in $\pi_2MU$).
3. [R53, Cor. C′(1)] and (I1); the last sentence is part 1 with $g$ the comparison cocycle.
4. Proposition 4.1(3) and Theorem 4.5(4). ∎

**Remark 6.4 (complex conjugation; correction of the first version).** Let $c=\mathrm{diag}(1,-1,\dots,1,-1)$ on $\mathbb R^{2N}=\mathbb C^N$ and $\bar J_{ac}:=-cJ_{ac}c^{-1}$. Then $\bar J$ is compatible, $\bar J^{\rm std}=J^{\rm std}$, and $c$ is a complex isomorphism $(E,-J)\to(E,\bar J)$; so $k(\bar J)=-k(J)$ and $\kappa(\bar J)=-\kappa(J)$, and the only fixed class is $0$. The first version of this paper concluded from this that $0$ is the only class "determined by the real framed data". That inference was invalid, as the referee pointed out.
* Transport by a real reframing $h$ is $J\mapsto hJh^{-1}$; it gives an isomorphic complex bundle and preserves $c_1$. A path $h_t$ from $1$ to $h$ gives the concordance $h_tJh_t^{-1}$, for *every* $J$. So every class $k\in\mathbb Z$ is invariant under reframings homotopic to the identity, and naturality under such reframings does not single out $k=0$.
* The operation that reverses $c_1$ is $J\mapsto-J$, which is not induced by any reframing.
* At the level of modules $M_k\simeq M_{-k}$ (Proposition 4.1(2)), so conjugation-invariance of a module cannot force it to be $M_0$.

A rule that is natural in the framed real data *and* equivariant under $J\mapsto-J$ would select the class $0$; we know no reason why a construction from the HW analytic data should have the second property, and we do not assume it. Theorem 6.3 is the statement that survives.

**Remark 6.5 (complexification).** For a family $D$ of real Fredholm operators, $D\otimes\mathbb C$ is complex linear, so $\operatorname{ind}(D)\otimes\mathbb C\cong\operatorname{ind}(D)\oplus\operatorname{ind}(D)$ carries a complex structure determined by $D$ ([3, proof of Prop. 3.35] uses $\operatorname{ind}(D\oplus D)$ in this way). This is a complex structure on the doubled index bundle, not on $\operatorname{ind}(D)$; it is not a complex orientation of the flow category, and we do not use it.

**Remark 6.6 (Hedenlund–Oldervoll $\mu$-structures).** In [2] an orientation theory is a functor $\mu:\mathcal C\to U/O$, and a $\mu$-structure on $X$ factors the index functor $-I_X:\Pi X\to U/O$ through $\mu$ [2, after Def. 0.0.2]. Under the framing, $I_X$ is trivialized. Complex orientations correspond to $\mu=(U\to U/O)$, whose homotopy fibre is $O$ and whose loop map $\mathbb Z\times BU\to\mathbb Z\times BO$ has fibre $\Omega O\simeq O/U$. Relative to the trivial structure, such lifts are maps from the groupoid completion of $\Pi X$ to $O$. If that groupoid completion is $S^3$ for $\Sigma_Q$ and $\Sigma_H$ (expected from [R33, Thm. 1(2)] and [5]), this gives $[S^3,O]=\pi_0(O)\times\pi_3(O)=\mathbb Z/2\times\mathbb Z$: the orientation and $\kappa$. This agrees with Theorems 4.2 and 4.4, and the integer $\pi_3(O)=\mathbb Z$ is the change of tangential structure $\alpha\in\pi_dO$, $d=3$, of [11, Ex. 2.27]. We do not formalize this comparison.

## 7. Proposition E: the remaining sectors

The contractibility statements below are recalled from [R46, Cor. E], [R49, Thm. D(4)] and [R53, Thm. A(1)]; the only addition is that the complex orientation is unique, which is immediate from Theorem A.

**Proposition 7.1 (= Proposition E; contractibility recalled).**
1. *(Isotropic, Klein.)* The isotropic category [R46, Thm. D] and the Klein category ($V_4$ trajectories are isotropic, [R49, Thms. B–C]) have two objects and one framed point. $\mathrm{Cl}=\{*\}$, and the $MU$-module is $\iota$ of a contractible spectrum.
2. *($\Sigma_2\cong C(2)$.)* The $SU(2)\times SU(2)$ category [R49, Thm. D] has four objects (gradings $2,1,1,0$), four points and one interval. It has no $2$-dimensional moduli, so $\mathrm{Cl}=\{*\}$ and the module is the base change of its realization.
3. *($C(3)$.)* The Lipshitz–Sarkar cube category [4] $C(3)$ has $12$ points, $6$ intervals and one hexagon. Each of the six faces of the hexagon is (point $\times$ interval) or (interval $\times$ point), and each interval appears exactly once. So $T_{C(3)}=(\pm1,\dots,\pm1)$ is onto and $\mathrm{Cl}=\{*\}$. The module is the base change of the realization of the framed cube category, which is contractible because its Morse complex is acyclic.
4. *($\Sigma_E$.)* The above-fold category with the perturbation $h_{\beta,e}$ has objects of indices $4$ and $1$ and no morphisms [R33, Thm. 3(3)]. Here $\mathrm{Cl}=\{*\}$ and the module is $(S^1\vee S^4)\wedge MU=M_0$.

*Proof.* Theorem A in each case: there are no disc or closed-surface components except the hexagon, whose $T$-row is a vector of units. Points carry the unique component $\mathcal J^+$ and intervals have $\pi_1(\mathcal J^+)=0$, so $\mathrm{Cl}$ is a point. The module statements follow from (I1). ∎

For $C(n)$ with $n\ge4$ there are $3$-dimensional permutohedra. Extending over them meets obstructions in $\pi_2(O/U)=\mathbb Z$, which Theorem A does not treat. We make no claim for $n\ge4$, nor for the $SU(2)^N$ sectors, whose identification with $C(N)$ is stated without detailed proof in [R52, Rem. 2.2].

## 8. Status of claims

| claim | status |
|---|---|
| Lemma 2.3, Remarks 2.4–2.6 | proved (standard homotopy theory) |
| Theorem A (Lemmas 3.2–3.4, Cor. 3.5) | proved; method of [R53, §3.2] in integral form |
| Proposition 4.1 | proved, using (I3)–(I5) |
| Theorem 4.2 ($\Sigma_H$) | proved, modulo the imported HW category and (I1)–(I5) |
| Theorems 4.4–4.5 ($\Sigma_Q$) | proved, modulo the imported HW category and (I1)–(I5) |
| Conjecture 4.6 ($\lvert\lambda\rvert=\lvert\kappa\rvert$) | **open** |
| Lemma 5.1, Lemma 5.2, Theorem 5.3 | proved, using (I2), (I4); Theorem 5.3 is a special case of [3, Cor. 7.4] |
| Proposition 6.1 | proved, with the quantifier $8j\ge m$ (corrected; the unrestricted statement is false) |
| Lemma 6.2, Theorem 6.3(1),(2),(4) | proved |
| Theorem 6.3(3) | conditional on [R53, Hyp. (Cmp)] |
| That HW analytic data select $k=0$ or exclude $k\ne0$ | **not claimed** (Remark 6.4; the argument of the first version was invalid) |
| Remarks 3.7, 6.5, 6.6 | heuristic comparisons; not used in proofs |
| Proposition 7.1 | immediate from Theorem A for the listed categories; contractibility recalled from [R46, Cor. E], [R49, Thm. D(4)], [R53, Thm. A(1)]; nothing claimed for $C(n)$, $n\ge4$, or $SU(2)^N$ |

## Appendix A. Machine checks

The supplement contains `verify.py` (Python 3 with sympy), its output `verify_output.txt`, and a Maple companion `verify.mpl`. The checks verify finite calculations used in the paper; they do not verify the imported results (I1)–(I5), the HW inputs, or hypothesis (Cmp).

* *§1 (homotopy groups).* $\pi_k(O/U)$ for $k\le7$ from the exact sequence of $O/U\to BU\to BO$, with the image $2\mathbb Z$ in $\pi_2(BU)$; the groups of $U/O$ for comparison; $\operatorname{Hom}(\mathbb Z/2,\mathbb Z)=0$ (Lemma 2.3, Remarks 2.4–2.5, Theorem B(3)).
* *§2 (genus).* The Chern-character genus on $\mathbb{CP}^1,\mathbb{CP}^2,\mathbb{CP}^3$ and products, its injectivity in degrees $4,6$, $x_1\mapsto2b_1$, and $\mathrm{Td}(\mathbb{CP}^1)=1$ (Theorem 4.2, (I5)).
* *§3 ($\Sigma_H$).* The Chern–Weil integral $\int_{S^2}\mathrm{ch}_1=2k$ (symbolic, and one quadrature as illustration); the complex over $\mathbb Q[b_1]$ for $|k|\le3$; the cokernels of $kx_1$ on $MU_{2j}$ for $k\le4$, $j\le3$; the $KU$ invariant (Proposition 4.1, Theorem 4.2).
* *§4 ($\Sigma_Q$).* All $4096$ sign patterns of the Morse differential, of which $128$ are admissible and all of rank $1$; for each, and both relative signs, the Smith form $(1,1,1)$ of the Stokes matrix, $\kappa\circ T=0$ and $\kappa$ onto; the Chern-character complex for $6$ patterns and all $K\in\{-1,0,1\}^{2\times2}$; the rank-jump criterion; $200$ random concordance moves (Lemma 4.3, Theorems 4.4–4.5, Lemma 5.2).
* *§5–6.* The hexagon of $C(3)$ for all $64$ sign choices, $C(2)$, and the table of admissible $b$-monomials (Proposition 7.1, Lemma 5.1).
* *§7 (Proposition 6.1).* $r_*=2$ on $\pi_{8j}$; a genuine check, from the table of $\pi_i(BO)$, $\pi_i(BU)$ and $r_*$ extended by Bott periodicity, that a lifted non-complexifiable class over $S^{8j}$ exists in $BO\langle m\rangle$ exactly when $8j\ge m$ ($0\le m\le48$, $1\le j\le6$), with the negative control $j=1$, $m=10$.
* *§8 (Lemma 6.2, Remark 6.4).* On $\Sigma_Q$, every $K=\pm\tfrac12T(m')$ with $T(m')$ even has $\kappa=0$ (all patterns, $m'\in\{0,1\}^8$); $\pi_3(M_k)=\pi_3(M_{-k})$.

`verify.py` runs 58 checks and ends with `FALLOS = 0`. `verify.mpl` mirrors the main checks of §§1–8 with 27 checks; it was executed in Maple with FALLOS = 0 (output in `verify_mpl_output.txt`).

## References

[1] M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.

[2] A. Hedenlund, T. P. Oldervoll, *Structured flow categories and twisted presheaves*, arXiv:2603.29576.

[3] K. Blakey, N. Porcelli, *Bulk-deformations, Floer complex bordism, and Grothendieck–Riemann–Roch*, arXiv:2605.06620 (v2).

[4] R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042.

[5] R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.

[6] R. Bott, *The stable homotopy of the classical groups*, Ann. of Math. 70 (1959), 313–337.

[7] J. Milnor, *On the cobordism ring $\Omega^*$ and a complex analogue, Part I*, Amer. J. Math. 82 (1960), 505–521.

[8] R. E. Stong, *Notes on Cobordism Theory*, Princeton Univ. Press, 1968.

[9] J. F. Adams, *Stable Homotopy and Generalised Homology*, Univ. of Chicago Press, 1974.

[10] C. Fourel, *Morse flow categories as exit path categories*, arXiv:2605.27112.

[11] N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257v3 (2025).

[R32] rStation math_32, https://rstation.ai/problems/math/papers/32/v1

[R33] rStation math_33, https://rstation.ai/problems/math/papers/33/v1

[R34] rStation math_34, https://rstation.ai/problems/math/papers/34/v1

[R46] rStation math_46, https://rstation.ai/problems/math/papers/46/v1

[R49] rStation math_49, https://rstation.ai/problems/math/papers/49/v1

[R52] rStation math_52, https://rstation.ai/problems/math/papers/52/v1

[R53] rStation math_53, https://rstation.ai/problems/math/papers/53/v1

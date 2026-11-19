# A $\mathbb Z/24$ of spherical framings and the $\eta^2$ obstruction for model continuation bimodules in the quadrupole sector of the Haydys–Witten fold, with an exact linear reduction

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

We construct and classify model continuation bimodules $B_M$, in the sense of Abouzaid–Blumberg, between the local Haydys–Witten (HW) flow categories of the quadrupole sector. The model, its realization $X_0=\Sigma^\infty(S^1\vee S^4)$ and its spherical twist $X_1=S^1\cup_{\eta^2}e^4$ are due to https://rstation.ai/problems/math/papers/33/v1 and https://rstation.ai/problems/math/papers/53/v1, and the abstract automorphism group $[S^3,GL_1\mathbb S]=\mathbb Z/2\times\mathbb Z/24$ follows from Hedenlund–Oldervoll. New here are the explicit bimodule geometry, the realization of these classes on its pieces, and their interaction with $\eta^2$.

**(A)** In a finite-dimensional reduction, quadrupole continuation is a transfer matrix $M$, and every $M\in SL(4)$ occurs. $B_M$ is transverse exactly when the leading principal minors of $M$ are nonzero; it is then the identity bimodule twisted by $R_\varepsilon$, with $\varepsilon$ the pivot signs and $\prod\varepsilon=+1$.

**(B)** Spherical framings relative to the ends, up to spherical homotopy, form a torsor over $\mathbb Z/2\times\mathbb Z/24$; all classes are vector-bundle reframings of one. For ends realizing $X_0$ the 48 classes give distinct maps; with equal end framings they are the 48 self-equivalences acting by the same sign on $H_1$ and $H_4$; the other 48 need $\det M<0$. For ends realizing $X_1$, $\gamma$ and $\gamma+12$ give the same map, because $\eta^3=12\nu$.

**(C)** A framing joining the model framing to an $\eta^2$-reframing exists exactly when the square classes have equal sums.

**(D)** A wall $\Delta_k=0$ changes the cellular map by a chain homotopy.

For slowly varying forcing (time normalized as in https://rstation.ai/problems/math/papers/32/v1), a uniform isolating-neighbourhood argument, given imported reduction and persistence theorems, confines every local HW continuation trajectory to an invariant sphere bundle, so index-$\le0$ HW trajectories and the cellular continuation map match the model. Identifying positive-dimensional HW moduli with $B_M$ remains a hypothesis. verify.py: 141 checks, FALLOS = 0.

---

## 0. Conventions and status of claims

* Every statement is labelled. *Proved here* means proved in this paper, possibly using inputs that are named explicitly in the statement or its proof. *Imported* means taken from a cited source; the inputs are listed in §2.5, §2.6 ((N1), (N2)) and §9. *Model* means a statement about the smooth model on $S^3$, proved here, which is linked to HW only through Proposition 2.6. *Conditional on (H$_{\rm HW}$)* means a statement about HW moduli spaces that follows from a model statement once Hypothesis (H$_{\rm HW}$) of §2.6 is assumed; such statements are never used to prove anything else.
* *Model continuation bimodule* means a bimodule $B_\Psi$ (Definition 2.2) whose transfer $\Psi$ is the transfer of a continuation datum (Definition 2.1); for linear transfers this means $B_M$ with $M\in SL(4)$ (Theorem A(1)). A bimodule $B_M$ with $\det M<0$ is a flow bimodule (Lemma 2.2), but we never call it a continuation bimodule.
* rStation papers are cited as [30]–[36], [41], [42] by their URLs.
* *Time.* The HW equations are written in the raw time $s$ of [32, §1.2]. Reduced fields are written in the normalized time $t=s/\pi$ of [32, §1.2], in which the quadrupole coefficient is $\kappa=-\frac{5\pi}{216}$ [32, Thm. B]; in raw time it is $\kappa/\pi=-\frac5{216}$.
* *Framings of bimodules.* Unless stated otherwise, a framing of a bimodule is a *spherical* framing and homotopies of framings are *spherical* homotopies (§2.4). Vector-bundle framings are always called so explicitly.
* verify.py tags its checks: [K] for known input that is merely encoded, [C] for exact computation, [I] for a symbolic identity, and [N] for a numerical illustration. No [N] check is used in a proof.
* The Maple file verify.mpl mirrors part of verify.py, including the new determinant checks (§9). It was run in Maple: 39 checks, FALLOS = 0.

---

## 1. Introduction and results

The main result is Theorem B: the spherical framings of a model continuation bimodule $B_M$ between quadrupole categories, up to spherical homotopy relative to its ends, form a torsor over $\mathbb Z/2\times\mathbb Z/24$. For ends realizing $X_0$ they give 48 distinct maps; with the same framing at both ends these are exactly the 48 elements of the index-2 subgroup $\operatorname{Aut}^+(X_0)\subset\operatorname{Aut}(X_0)$ acting by the same sign on $H_1$ and $H_4$. The other 48 self-equivalences are *not* realized by continuation, because every transfer lies in $SL(4)$; they are realized by twisted identity bimodules $B_{R_\varepsilon}$ with $\det R_\varepsilon=-1$, which are flow bimodules but not continuation bimodules (Theorem B(5)). For ends realizing $X_1$ the relation $\eta^3=12\nu$ identifies the classes $\delta$ and $\delta+12$. Theorem C places the $\eta^2$ class of rStation math_53 [36] as an obstruction on these bimodules. Theorem A, an exact linear model of quadrupole continuation, is the tool; its transversality criterion is the classical LU condition (Remark 1.1).

*What is not new.* The model category $\Sigma_Q(C)$ and its realization $X_0$ are established in rStation math_33 [33, Thm. 1], and its two spherical twists, realizing $X_0$ and $X_1$, in rStation math_53 [36, Thm. A]. The abstract group $\Gamma^B\cong\mathbb Z/2\times\mathbb Z/24$ is also not an independent discovery: it is $\pi_0\mathrm{Map}(S^3,GL_1\mathbb S)=[S^3,GL_1\mathbb S]$, the automorphism group of the constant spectral local system $\mathbb S$ on $S^3$, and by Hedenlund–Oldervoll [2, Thm. 0.0.1, Ex. 0.0.7, Ex. 2.5.12] the Morse flow category of the model, with its natural $S^3$-structure, corresponds to that local system (§8.2). What this paper adds is (i) the explicit geometry of the bimodules $B_M$ (Theorem A), (ii) the realization of these classes on its pieces (the $\pi_3^s$-classes live on the four 3-dimensional pieces, and act on realizations by $\delta N$; Theorem B(1)–(4)), and (iii) their interaction with the $\eta^2$ obstruction of [36] (Theorem B(3) and Theorem C).

All bimodule-level results are about the explicit model bimodules $B_M$ of a finite-dimensional reduction. What is proved about HW itself is Proposition 2.6, modulo the imported inputs (N1)–(N2) named there: every local HW continuation trajectory lies on a non-autonomous invariant sphere bundle (Lemma 2.6A, a uniform isolating-neighbourhood and local-maximality argument), the HW continuation trajectories of index $\le0$ correspond to those of $B_M$, and so the HW cellular continuation map is the model one (Corollary 2.8). The identification of the positive-dimensional compactified HW moduli spaces with $B_M$ is stated as Hypothesis (H$_{\rm HW}$) (§2.6), and its consequences are stated conditionally (Corollary 2.7). Remark 1.2 lists the changes with respect to the two previous versions. What is recalled and what is new is listed in §1.4.

### 1.1 Background and the question

A Floer homotopy theory for the Haydys–Witten (HW) equations [37, 38] would assign framed flow categories to Kapustin–Witten data and continuation bimodules to paths of data. By Abouzaid–Blumberg [1], these are the 0- and 1-simplices of a semi-simplicial space that presents an $\infty$-category $\mathrm{Flow}^{\rm fr}\simeq\mathrm{Sp}$. Higher simplices are families of data. Hedenlund–Oldervoll [2] extend this to structured flow categories, and they construct mapping cones of bimodules explicitly [2, Lemma 3.7.12].

Near the Anderson–Henningson (AH) fold $L=\pi r$ on $\mathbb R\times S^3\times(0,L)$ with Nahm poles [39, 40], earlier rStation papers constructed local HW flow categories.

* The quadrupole category $\Sigma_Q$ [32] has eight objects and morphism spaces consisting of 12 points, 8 intervals and 4 squares. It has a smooth Morse–Smale model on $S^3$ with Cohen–Jones–Segal (CJS) realization $X_0=\Sigma^\infty(S^1\vee S^4)=\Sigma\Sigma^\infty_+S^3$, which is the suspended Conley index [33, Thm. 1]. Its PDE version is in [34].
* The height category $\Sigma_H$ has two objects and $\overline{\mathcal M}(P_4,P_1)\cong S^2$ [32, 33].
* Spherical reframings were classified in [36] (rStation math_53), building on the interval-level framing computations of [35]. Up to homotopy there are exactly two, realizing $X_0$ and $X_1=S^1\cup_{\eta^2}e^4$. The class is $\sum_Qc_Q\in\pi_2^s$, the sum of the four square classes, and it lies in $\operatorname{coker}J$.

In the published rStation series, no morphisms between these categories have been constructed. The other sectors treated in the series (isotropic and Klein) have contractible realizations for every framing (recalled from rStation math_46 [41, Cor. E], math_49 [42, Thm. D(4)] and math_53 [36, Thm. A(1)]), so every bimodule between them is homotopically trivial. Within the series, the quadrupole sector is therefore the first in which continuation bimodules can carry homotopical content. This paper constructs the corresponding model bimodules, computes that content for them, and proves the part of the comparison with HW that concerns trajectories of index $\le0$.

### 1.2 Conventions

Let $C=\operatorname{diag}(c_0<c_1<c_2<c_3)$ be traceless, with eigenbasis $e_0,\dots,e_3$, and put $\varphi_C(\theta)=\frac12\langle\theta,C\theta\rangle$ on the round $S^3\subset\mathbb R^4$. The objects of $\Sigma_Q(C)$ are
$$P_a^\sigma=\sigma e_{a-1},\qquad a\in\{1,2,3,4\},\ \sigma\in\{\pm\}.$$
The grading is $|P_a^\sigma|=a$, which is the Morse index plus one, as in [33, Thm. 1(2)]. Put
$$E_a=\operatorname{span}(e_0,\dots,e_{a-1}),\qquad F_b=\operatorname{span}(e_{b-1},\dots,e_3).$$
Then
$$W^u(P_a^\sigma)=\{\theta\in S(E_a):\sigma\theta_{a-1}>0\},\qquad W^s(P_b^\tau)=\{\theta\in S(F_b):\tau\theta_{b-1}>0\}$$
[33, Lemma 3.2]. Objects of the target copy of $\Sigma_Q(C)$ in a bimodule are written $Q_b^\tau$. We write $\Delta_k(M)$ for the $k$-th leading principal minor of a matrix $M$, with $\Delta_0=1$.

We use $X_0=\Sigma^\infty(S^1\vee S^4)$ and $X_1=S^1\cup_{\eta^2}e^4$, and $\nu\in\pi_3^s=\mathbb Z/24$ denotes a generator. For a spectrum $X$ with cells in degrees $1,\dots,4$ and $H_*(X)=\mathbb Z[1]\oplus\mathbb Z[4]$, let $q:X\to S^4$ be the collapse onto the top cells composed with the generator of $H^4$, and let $\iota:S^1\to X'$ be the inclusion of the bottom cells representing the generator of $H_1$. Put
$$N=\iota\circ\nu\circ q\in[X,X'].$$

### 1.3 Results

**Theorem A (exact linear model of quadrupole continuation; model, proved here).** Let $M\in GL(4,\mathbb R)$, written in the eigenbasis of $C$. Let $B_M$ be the model bimodule $\Sigma_Q(C)\to\Sigma_Q(C)$ whose middle transfer is the projective action $M_*\theta=M\theta/|M\theta|$ (Definition 2.2). By (1), $B_M$ is a model continuation bimodule exactly when $M$ can be normalized into $SL(4)$, i.e. when $\det M>0$ (positive scalars do not change $M_*$ or the sign pattern); for $\det M<0$ it is a flow bimodule that does not come from any quadrupole datum.
1. *(Linearization.)* The round quadrupole field $X_C=-(C\theta-\langle\theta,C\theta\rangle\theta)$ is the projectivization of $v'=-Cv$. For every continuous, piecewise $C^1$ path $C(s)$ of traceless symmetric matrices that equals $C$ outside $[-T,T]$, the continuation trajectories of the corresponding data (Definition 2.1) correspond bijectively, via the window maps of Lemma 2.4, to the points of $B_M$, where $M=U(T)U(-T)^{-1}\in SL(4)$ and $U$ is the fundamental solution of $v'=-C(s)v$. Conversely, every $M\in SL(4)$ arises from such a path.
2. *(Moduli spaces.)* We have
$$B_M(P_a^\sigma,Q_b^\tau)=\{[u]\in S^3:\ u\in E_a,\ Mu\in F_b,\ \sigma u_{a-1}>0,\ \tau(Mu)_{b-1}>0\}.$$
3. *(Transversality.)* $B_M$ is cut out transversally, on all strata, if and only if $\Delta_1(M),\Delta_2(M),\Delta_3(M)\ne0$. In that case $B_M$ is a flow bimodule in the sense of [1], with compactified pieces that are $\langle k\rangle$-manifolds.
4. *(Classification.)* Suppose $B_M$ is transverse, and put $\varepsilon_a=\operatorname{sgn}(\Delta_{a-1}(M)\Delta_a(M))$ for $a=1,\dots,4$. Then $B_M$ is isomorphic, as an unframed bimodule, to the identity bimodule twisted by the automorphism $R_\varepsilon=\operatorname{diag}(\varepsilon_1,\dots,\varepsilon_4)$ of $\Sigma_Q(C)$:
$$B_M(P,Q)\cong B_{\rm id}(P,R_\varepsilon^{-1}Q).$$
   Moreover $\prod_a\varepsilon_a=\operatorname{sgn}\det M$. Two transverse $M$ with the same sign pattern give isomorphic bimodules. In particular every transverse transfer of a quadrupole datum has $\prod_a\varepsilon_a=+1$, and exactly the 8 sign patterns with $\prod_a\varepsilon_a=+1$ occur for such transfers (each is realized by $R_\varepsilon\in SL(4)$).
5. *(Shapes.)* The compactified pieces $\overline B(P_a,Q_b)$ are, for $a-b=0,1,2,3$:
   * a point;
   * an interval;
   * a hexagon;
   * a compact contractible 3-manifold with corners bounded by a 2-sphere (a 3-polytope), with $f$-vector $(16,24,10)$, whose facets are 6 squares and 4 hexagons.

   For $a<b$ the pieces are empty. In total $B_M$ has 8 points, 12 intervals, 8 hexagons and 4 three-dimensional pieces.
6. *(Cellular map.)* With chart orientations, the cellular chain map of $B_M$ is $f_\varepsilon(e_a^\tau)=\big(\prod_{c<a}\varepsilon_c\big)\,e_a^{\varepsilon_a\tau}$. It acts on $(H_1,H_4)$ by $(1,\prod_a\varepsilon_a)$. If the two ends carry the same framing, the framed cellular map of $B_M$ is $\pm Df_\varepsilon D$ for any framing of $B_M$, where $D$ records the framing signs of the end objects, and it acts on $(H_1,H_4)$ by $\pm(1,\prod_a\varepsilon_a)$ (§3.6). For model continuation bimodules this is $\pm(1,1)$.

**Remark 1.1 (classical content of Theorem A(3)–(5)).** Condition (3) is exactly the existence of an LU (Gauss) decomposition of $M$, i.e. $M$ lies in the big Bruhat cell, and $\varepsilon_a=\operatorname{sgn}(\Delta_{a-1}\Delta_a)$ records the signs of the pivots $d_a=\Delta_a/\Delta_{a-1}$ (see e.g. Golub–Van Loan [43] for the minor criterion). The unstable and stable manifolds $S(E_a)$, $S(F_b)$ of the linear flow are Schubert-type cells of the linear height function, as in the classical Morse theory of linear functions on spheres and flag manifolds (e.g. Duistermaat–Kolk–Varadarajan [44]). Since $B_M$ is a twisted identity bimodule, the pieces in (5) are the pieces of the Abouzaid–Blumberg identity bimodule of $\Sigma_Q(C)$ [1, §6.1], [2, §3.5] (input (R4)), here made explicit. What Theorem A adds is the identification of quadrupole continuation with this linear-algebra picture, not the linear algebra itself.

**Theorem B (framings of model bimodules: a $\mathbb Z/24$; model, proved here).** Let $B=B_M$ be transverse, $M\in GL(4)$. Parts (1)–(4) hold for every such $M$; the model continuation bimodules are those with $\det M>0$. Framings of $B$ are spherical framings and homotopies are spherical homotopies (§2.4). Let $(u_0,u_1)$ be framings of the two ends for which $B$ admits a spherical framing $f_0$ extending them (Theorem C).
1. *(Classification of spherical framings.)* Up to spherical homotopy relative to the ends, the spherical framings of $B$ extending $(u_0,u_1)$ form a torsor over $\Gamma^B=\mathbb Z/2\times\mathbb Z/24$. This is not a classification of vector-bundle framings up to vector-bundle homotopy, a different question that we do not answer (§8.2); (4) only says that every spherical class is reached from $f_0$ by a vector-bundle reframing. Distinctness of $\delta$ and $\delta+12$ uses input (R3); everything else in (1)–(4) uses only (R1)–(R2) and the lemmas of §5. The obstruction groups are $\Gamma^B_0=\mathbb Z/2$ (a global sign), $\Gamma^B_1=\Gamma^B_2=0$ and $\Gamma^B_3=\pi_3^s$. The $\mathbb Z/24$-coordinate is $\delta=\sum_{s,t}\sigma_s\tau_tc_{st}$, where $c_{st}\in\pi_3^s$ is the class carried by the 3-dimensional piece $\overline B(P_4^s,Q_1^t)$ and $\sigma_s,\tau_t\in\{\pm1\}$ are fixed by the cellular complex.
2. *(Effect on realizations.)* If $f$ has coordinates $(\sigma,\delta)$ relative to $f_0$, then
$$|B,f|=\sigma\big(|B,f_0|+\delta N\big)\in[\,|\Sigma_Q,u_0|,|\Sigma_Q,u_1|\,].$$
3. *(Injectivity, and its failure.)* If the ends realize $X_0$, the 48 classes give 48 distinct maps. If they realize $X_1$, the classes $(\sigma,\delta)$ and $(\sigma,\delta')$ give the same map exactly when $\delta-\delta'\in\{0,12\}$. The reason is that $12\nu=\eta^3$ and $\iota\circ\eta^2=0$ in $X_1$. So 24 distinct maps arise in this case.
4. *(Vector-bundle realizability.)* Every class is represented by a reframing by a vector-bundle ($O$-)cocycle, because $J:\pi_3(O)\to\pi_3^s$ is onto. The generator is supported in a disc of one 3-dimensional piece, where it is given by the left multiplication $S^3\to SO(4)$, $x\mapsto L_x$, whose $J$-image is $\nu$.
5. *(Realizable self-equivalences; uses (R3).)* Fix a vector-bundle framing $u$ of $\Sigma_Q(C)$ and an equivalence $\phi:|\Sigma_Q(C),u|\simeq X_0$ (R3), used at both ends. Write $\operatorname{Aut}(X_0)=\{(a,d,\gamma)\}\cong D_{24}\times\mathbb Z/2$ (96 elements, $D_{24}$ dihedral of order 48; §6.6) and $\chi(a,d,\gamma)=ad$. The character $\chi$ is a conjugation-invariant homomorphism, so $\operatorname{Aut}^+(X_0):=\ker\chi=\{(\sigma,\sigma,\gamma)\}\cong\mathbb Z/2\times\mathbb Z/24$ (48 elements) does not depend on $\phi$.
   * (a) For every transverse $M\in SL(4)$, i.e. for the transverse transfer of every quadrupole datum, the maps $|B_M,f|$, with $f$ ranging over the spherical framings extending $(u,u)$, are exactly the 48 elements of $\operatorname{Aut}^+(X_0)$. For $M=I$ the canonical framing gives $\mathrm{id}$ (input (R4)); (a) does not depend on (R4).
   * (b) No framed model continuation bimodule $(B_M,f)$ from $(\Sigma_Q,u)$ to $(\Sigma_Q,u)$ realizes an element with $\chi=-1$: this would require $\prod\varepsilon=\operatorname{sgn}\det M=-1$, which is impossible for $M\in SL(4)$.
   * (c) The 48 elements with $\chi=-1$ are exactly the maps $|B_{R_\varepsilon},f|$ with $\prod\varepsilon=-1$. Here $B_{R_\varepsilon}$ is the identity bimodule twisted by the automorphism $R_\varepsilon$ of $\Sigma_Q(C)$ (Theorem A(4)); it is a flow bimodule, and $\mathrm{Cone}(B_{R_\varepsilon})$ is a framed flow category, but $B_{R_\varepsilon}$ is not a model continuation bimodule. We do not construct an HW or KW symmetry realizing $R_\varepsilon$ with $\prod\varepsilon=-1$.

**Remark 1.2 (scope, and the corrections with respect to the previous versions).** Items 1–2 answer the two points raised by a referee on the first version; items 3–6 answer the points raised on the second version.
1. *Determinant.* A quadrupole datum has transfer $M=U(T)U(-T)^{-1}$ with $\det M=e^{-\int\operatorname{tr}C}=1$, and multiplying $M$ by a scalar does not change the sign of $\det M$ (for $4\times4$ matrices, $\det(\lambda M)=\lambda^4\det M$). More generally, the transfer of any continuation datum (Definition 2.1) is the time map of an $s$-dependent vector field, hence isotopic to the identity and orientation preserving. The first version claimed all 96 elements of $\operatorname{Aut}(X_0)$ for continuation bimodules, using $M=R_\varepsilon$ with $\prod\varepsilon=-1$. That half is not realized by continuation. Theorem B(5) now states exactly what is realized: $\operatorname{Aut}^+(X_0)$, 48 elements, by every transverse $M\in SL(4)$; the other 48 are realized by the twisted identity bimodules $B_{R_\varepsilon}$, $\prod\varepsilon=-1$, which we do not call continuation bimodules. verify.py §14 checks $\det R_\varepsilon=\prod\varepsilon_a$, the Liouville identity behind $\det M=1$, and the count 48.
2. *HW identification.* Theorems A–E are about the explicit bimodules $B_M$ (and $B_\Psi$) of the finite-dimensional model. Proposition 2.6 identifies only the HW continuation trajectories of index $\le0$ with those of $B_M$; this determines the HW cellular continuation map (Corollary 2.8), not the compactified HW moduli spaces of positive dimension. Their identification with $B_M$ is Hypothesis (H$_{\rm HW}$) of §2.6, and every statement about framed HW continuation bimodules is stated conditionally on it (Corollary 2.7).
3. *Confinement.* The second version called the invariant sphere bundle "normally repelling" and deduced confinement from the convergence of a trajectory to an object. That was wrong: by [32, Lemma 4.2] and [32, proof of Thm. C, Step 4] the normal eigenvalues are $\pm\sqrt{10|\bar\nu|/3}(1+o(1))$, with one stable and one unstable normal direction. Proposition 2.6(2) is now proved by Lemma 2.6A, a non-autonomous version of the argument of [32, Thm. C, Step 2]: upper semicontinuity of complete invariant sets in the isolating neighbourhood $\bar B$, uniform in time, followed by local maximality in an explicit tube, proved by a Lyapunov-function argument that uses both normal directions. It uses only that a trajectory stays in $\bar B$, not its asymptotics. The imported inputs are named as (N1) and (N2).
4. *Time normalization.* [32] uses the normalized time $t=s/\pi$, in which $\kappa=-5\pi/216$. The forcing path is now prescribed in the slow normalized time $\varsigma=\varepsilon|\kappa|t=5\varepsilon s/216$, and then the leading angular equation is $d\theta/d\varsigma=X_{\tilde C(\varsigma)}(\theta)$. With the second version's parametrization $\tilde C(\varepsilon|\kappa|s)$, the leading equation has the factor $1/\pi$, the relevant linear equation is $v'=-(1/\pi)\tilde C v$, and the rotation wall of §4.3 moves from $\omega^*$ to $\omega^*/\pi$. This can change the pivot signs and the cellular map, but not the action on homology (Remark 2.6B, Remark 4.1, verify.py §15).
5. *Novelty.* The model realization and its two spherical twists are from [33, 36], and the abstract group $[S^3,GL_1\mathbb S]$ follows from [2]. We now say so in the abstract and in §1, and present as new only the explicit bimodule geometry, the realization of the classes on its pieces, and their interaction with the $\eta^2$ obstruction.
6. *Terminology.* Theorem B now classifies spherical framings up to spherical homotopy, as distinct from vector-bundle framings (§2.4). Theorem D(4) now says that the Bernoulli substitution linearizes the cubic truncation of the normal form, not the normal form with its $O(x^5)$ remainder.

**Theorem C (the $\eta^2$ obstruction on the model bimodule; model, proved here).**
1. *(Existence.)* If $u_0,u_1$ are vector-bundle framings of $\Sigma_Q(C)$, then every transverse $B_M$ admits a vector-bundle framing extending $(u_0,u_1)$.
2. *(Obstruction.)* Let $g_0,g_1$ be normalized spherical reframings in the sense of [36], with square classes $c(g_i)\in(\pi_2^s)^4$. Then $B_M$ admits a framing from $(\Sigma_Q,u_0g_0)$ to $(\Sigma_Q,u_1g_1)$ if and only if $\sum_Qc_Q(g_0)=\sum_Qc_Q(g_1)$. The obstruction is the vector of $\pi_2^s$-classes of the four boundary spheres $\partial\overline B(P_4^s,Q_1^t)\cong S^2$. Modulo the hexagon moves, which change it by even vectors, this vector reduces to $\sum c(g_1)-\sum c(g_0)$.
3. *(Height sector.)* There is an explicit transverse continuation bimodule $B_{QH}:\Sigma_Q\to\Sigma_H$, together with one $B_{HQ}:\Sigma_H\to\Sigma_Q$. Their pieces are compactified cells and blow-ups of them (Theorem E). $B_{QH}$ admits a framing from $(\Sigma_Q,u g)$ to $(\Sigma_H,u_Hh)$ if and only if $\sum_Qc_Q(g)=c(h)\in\pi_2^s$.
4. *(Consequence.)* No framing of these model bimodules intertwines a realization $X_0$ with a realization $X_1$. Whenever the classes agree, the framed bimodules exist and realize equivalences. This gives a geometric proof that the realization depends only on the class of the reframing, in the direction "equal classes $\Rightarrow$ equivalent realizations". The statement itself is consistent with, and already contained in, [36, Thm. A]; the new point is the bimodule-level mechanism.

**Theorem D (codimension-one events; proved here, model).**
1. *(End data.)* Inside the quadrupole family there are no codimension-one events: for every simple spectrum the flow is Morse–Smale [33, Lemma 3.2], and non-simple spectrum has codimension 2 in $\operatorname{Sym}^2_0(\mathbb R^4)$. A loop of simple-spectrum data has monodromy an automorphism $R_\varepsilon$ with $\prod\varepsilon=1$, and every such $R_\varepsilon$ occurs.
2. *(Continuation walls.)* Consider a generic one-parameter family $M_\lambda$ that crosses $\{\Delta_k=0\}$ transversally at $\lambda_0$, with $1\le k\le3$ and the other minors nonzero.
   * At $\lambda_0$ there are exactly two continuation trajectories of index $-1$. They are antipodal, $P_k^{\pm\sigma}\to Q_{k+1}^{\pm\tau}$.
   * $\varepsilon_k$ and $\varepsilon_{k+1}$ change sign, and no other $\varepsilon_a$ changes.
   * $f_{\varepsilon'}-f_\varepsilon=dK+Kd$, where $K:C_k\to C_{k+1}$ is the signed count of these two trajectories. The equation has exactly two solutions with entries in $\{0,\pm1\}$, and each is supported on one antipodal pair. The integer solutions are these plus multiples of a rank-one kernel.
3. *(An explicit wall.)* Rotate the quadrupole axes by $\pi$ in the $(e_0,e_1)$-plane at constant angular speed $\omega$. This is a loop of data. Put $\delta=(c_1-c_0)/2$.
   * For $\omega<\omega^*$ the bimodule has $\varepsilon=(-,-,+,+)$; this is the adiabatic monodromy.
   * For $\omega>\omega^*$ it has $\varepsilon=(+,+,+,+)$.
   * There is exactly one wall, at $\omega^*=\delta/\sqrt{1-y_*^2}$. Here $y_*\in(\frac12,1)$ is the unique root of $\cot(\pi y)+\sqrt{1-y^2}/y=0$; numerically $y_*\approx0.736484$ and $\delta/\omega^*\approx0.676454$.
   * At the wall, the minimum $e_0$ is rotated exactly onto the saddle $\pm e_1$.
4. *(Leaving the quadrupole family.)* The family $g_k=\varphi_C-k\langle e_0,\theta\rangle$, $k\ge0$, joins $\Sigma_Q$ to a height function. It passes through three $(\mathbb Z/2)^3$-symmetric pitchforks at $k=\Delta_j:=c_j-c_0$. At the $j$-th pitchfork the pair of index $j$ merges into $-e_0$, whose index rises from $j-1$ to $j$. On the invariant circles the flow is $t'=-\sin t\,(\Delta_j\cos t+k)$. The normal form is $x'=(k-\Delta_j)x+(\frac23\Delta_j-\frac k6)x^3+O(x^5)$. For an $s$-dependent parameter, its cubic truncation $x'=\mu(s)x+ax^3$ is linearized exactly by $y=x^{-2}$ (Bernoulli), into $y'=-2\mu y-2a$. The substitution does not linearize the normal form with its $O(x^5)$ remainder (verify.py §15).

**Theorem E ($\Sigma_Q\leftrightarrow\Sigma_H$; model, proved here).** Let $\Psi$ be the middle transfer of any continuation datum from quadrupole to height data. Put $p^*=\Psi^{-1}(-e)$, where $-e$ is the maximum of the height function, and assume $p^*$ lies in the open 3-cell $W^u(P_4^{s^*})$; this is generic.
1. The bimodule $B_{QH}$ is transverse. Its pieces are:
   * $B(P_4^{s^*},Q_4)=\{p^*\}$;
   * $\overline B(P_a^\sigma,Q_1)=\widehat W^u(P_a^\sigma)$, a point, interval, square or cube, for $(a,\sigma)\neq(4,s^*)$;
   * $\overline B(P_4^{s^*},Q_1)$, the real blow-up of the cube at $p^*$, whose inner boundary is $\{p^*\}\times\overline{\mathcal M}_H(Q_4,Q_1)=S^2$.

   Its cellular map is an isomorphism on homology.
2. Dually, $B_{HQ}$ has one point in each of $B(Q_4,P_4^\pm)$, one point in $B(Q_1,P_1^{t^*})$, and pieces $\Psi'^{-1}\widehat W^s(P_b)$, with one of them blown up. The composite of the cellular maps $\Sigma_H\to\Sigma_Q\to\Sigma_H$ is the identity.
3. *(Rigidity of $\Sigma_H$.)* Every transverse model continuation bimodule $\Sigma_H\to\Sigma_H$ (transfer in $\mathrm{Diff}_0(S^3)$) is isomorphic to the identity bimodule. Its only positive-dimensional piece is $S^3$ blown up at two points, which is $S^2\times[0,1]$.
4. By [1, 2], and the standard gluing of continuation data, which we import, $B_{HQ}\circ B_{QH}$ and $B_{QH}\circ B_{HQ}$ are homotopic to the identity bimodules through 2-simplices given by families of data.

**Proposition 2.6 (HW reduction; proved modulo the imported inputs (N1)–(N2) and [31, 32, 33]).** Prescribe slowly varying quadrupole forcing $C_\varepsilon(s)=\tilde C(\varsigma)$ in the slow normalized time $\varsigma=\varepsilon|\kappa|s/\pi=5\varepsilon s/216$, in the regime of [32, Thm. C]. Then every local continuation trajectory of the perturbed gauge-fixed HW equation lies on a non-autonomous invariant 3-sphere bundle with one stable and one unstable normal direction (Lemma 2.6A). In the time $\varsigma$, the flow there is $C^1$-close to the model flow of $\tilde C(\varsigma)$. Hence, for transverse model data, the HW continuation trajectories of index $\le0$ correspond bijectively to those of the model. In particular the HW cellular continuation map is $f_\varepsilon$, up to framing signs, with $\varepsilon$ the sign pattern of the model transfer matrix of $v'=-\tilde C(\varsigma)v$; since that matrix lies in $SL(4)$, it acts on homology by $\pm(1,1)$ (Corollary 2.8). Positive-dimensional HW moduli spaces are not identified with $B_M$; that identification is Hypothesis (H$_{\rm HW}$) (§2.6).

### 1.4 What is new, and what is not (relation to published work)

*Recalled from the published series and the literature.* The quadrupole and height categories and their model [32, 33]; the model realization $X_0$ [33, Thm. 1]; the classification of spherical reframings, i.e. the two spherical twists of the model, realizing $X_0$ and $X_1$, including the fact that the realization depends only on the class $\sum_Qc_Q$ [36, Thm. A]; the interval-level framing computations [35]; contractibility of the isotropic and Klein categories for every framing [41, Cor. E], [42, Thm. D(4)], [36, Thm. A(1)]; the abstract automorphism group $[S^3,GL_1\mathbb S]\cong\mathbb Z/2\times\mathbb Z/24$ of the constant local system to which the model corresponds, which follows from Hedenlund–Oldervoll [2, Thm. 0.0.1, Ex. 0.0.7, Ex. 2.5.12] (§8.2). None of these is claimed here.

*New.*
* The explicit realization of the group $\mathbb Z/2\times\mathbb Z/24$ on the model bimodules: the classification of the spherical framings of $B_M$ through cocycles on its pieces, with the $\pi_3^s$-classes on the four 3-dimensional pieces acting by $\delta N$; its interaction with $X_1$ through $\eta^3=12\nu$; and the determination of the self-equivalences realized by model continuation: exactly $\operatorname{Aut}^+(X_0)$ (Theorem B). This is the main result. The group itself is not new (see above); our proof of B(1) does not use [2] or [7], and is consistent with them.
* The location of the $\eta^2$ class of [36] as an obstruction on the 3-dimensional bimodule pieces (Theorem C). Theorem C(4) is consistent with [36, Thm. A]; only the bimodule-level mechanism is new.
* The exact linearization of quadrupole continuation, and the identification of the model continuation bimodules with leading-minor sign patterns with $\prod\varepsilon=+1$ (Theorem A). The minor condition is the classical LU/Bruhat condition and $\varepsilon$ the pivot signs (Remark 1.1); the new point is that quadrupole continuation reduces to it.

*Made explicit, not claimed as new.* The pieces of Theorem A(5): they are the pieces of the Abouzaid–Blumberg identity bimodule [1, §6.1], [2, §3.5], described here as explicit polytopes.
* The explicit wall $\omega^*$ and the wall-crossing chain homotopies (Theorem D).
* The cellular bimodules $\Sigma_Q\leftrightarrow\Sigma_H$ (Theorem E).

*Imported.*
* The model and its invariant manifolds [33].
* Smooth corner structures for standard-form Morse–Smale flows [8, 9].
* Fibre products of manifolds with corners [11].
* The CJS/Lipshitz–Sarkar realization and its basic properties [6, 3, 12].
* The reframing formalism and the two realizations $X_0,X_1$ [36].
* The flow-bimodule framework [1, 2].
* The HW centre manifold, normal form and invariant sphere [31, 32]; the non-autonomous reduction (N1) [20, 31, 32, 33] and the persistence of noncompact normally hyperbolic manifolds (N2) [17, 18, 19, 45] (§2.6).
* Fenichel theory [17, 18].
* Classical stable homotopy [21, 22].
* The LU/Bruhat decomposition and the Morse theory of linear functions on spheres and flag manifolds [43, 44].

*Scope of the HW link.* Proposition 2.6 relates the model to the HW equations only for continuation trajectories of index $\le0$ (all of which lie on the invariant sphere bundle, Lemma 2.6A), which gives the HW cellular continuation map (Corollary 2.8). Positive-dimensional HW moduli spaces are not compared; their identification with $B_M$ is Hypothesis (H$_{\rm HW}$), and its consequences are conditional (Corollary 2.7, §2.6).

*Relation to classical theory.* Continuation maps in Morse–Floer theory, and their independence of the path up to chain homotopy, are classical [14, 15, 16]. So are handle slides and births–deaths in one-parameter families (Cerf [12]) and their effect on Morse complexes. Lobb–Orson–Schütz [4, 5] give a calculus of moves on framed flow categories (handle slides, cancellations) at the level of stable homotopy types. Our walls are the continuation analogues of handle slides. We do not use the LOS moves, but Theorem C(3) is a geometric instance of a cancellation equivalence.

---

## 2. Setting

### 2.1 The model and its flow category

Let $g_1$ be the metric of [33, Thm. 1(1)]: it is round outside small balls around $\pm e_j$, and Euclidean in the projection charts near $\pm e_j$. We choose its cut-offs radial in those charts. Then $g_1$ is invariant under the group $\{R_\varepsilon\}\cong(\mathbb Z/2)^4$ of coordinate reflections, and $X^{(1)}_C=-\nabla_{g_1}\varphi_C$ commutes with every $R_\varepsilon$.

For the height function $\varphi_e=-\langle e,\theta\rangle$ we use the standard-form metric of [33, §3, setting (H)], and write $X^{(1)}_e$ for its negative gradient.

By [33, Lemma 3.2], $X^{(1)}_C$ has the same zeros and the same stable and unstable manifolds as the round field $X_C$, listed in §1.2. It is Morse–Smale, and it is in standard form near the zeros.

**Standing input (W) [8, 9, 10].** For a Morse–Smale pseudo-gradient in standard form on a closed manifold:
* the compactified unstable manifolds $\widehat W^u(P)$ and stable manifolds $\widehat W^s(Q)$ are compact smooth $\langle k\rangle$-manifolds;
* their codimension-one faces are $\overline{\mathcal M}(P,P')\times\widehat W^u(P')$ and $\widehat W^s(Q')\times\overline{\mathcal M}(Q',Q)$;
* the evaluation maps $\mathrm{ev}:\widehat W^u(P)\to S^3$ are smooth, and on each stratum $\mathcal M(P,P_1)\times\dots\times W^u(P')$ they restrict to the embedding of the last factor;
* the compactified morphism spaces form a smooth flow category $\Sigma_Q(C)$.

$\Sigma_Q(C)$ is isomorphic, as a topological flow category, to the HW category of [32, 33] and to $\mathcal C_{\rm PDE}$ of [34] [33, Thm. 1(2)], [34, Thm. D(1)].

### 2.2 Continuation data and the bimodules $B_\Psi$

**Definition 2.1.** A *continuation datum* is an $s$-dependent vector field $Y_s$ on $S^3$, $s\in\mathbb R$, with the following properties:
* $Y_s=X^{(1)}_{C_-}$ for $s\le-T'$ and $Y_s=X^{(1)}_{C_+}$ for $s\ge T'$;
* $Y_s$ is continuous and piecewise $C^1$ in $s$, and smooth in $\theta$.

Its *transfer* is the time map $\Psi=\Psi_{-T'}^{T'}$, a diffeomorphism of $S^3$. A *continuation trajectory* from $P$ to $Q$ is a solution of $\theta'=Y_s(\theta)$ with $\theta(-\infty)=P$, a zero of $X^{(1)}_{C_-}$, and $\theta(+\infty)=Q$, a zero of $X^{(1)}_{C_+}$. There is no quotient by $\mathbb R$.

A *quadrupole datum* is a path $C(s)$ of traceless symmetric matrices with $C(s)=C$ for $|s|\ge T$. It defines a continuation datum as follows:
* $Y_s=X_{C(s)}$, the round field, for $|s|\le T$;
* $Y_s=-\nabla_{g_{\lambda(s)}}\varphi_C$ for $T\le|s|\le T+1$, where $g_\lambda$ is the interpolating family of [33, §3.2] and $\lambda(\pm(T+1))=1$, $\lambda(\pm T)=0$;
* $Y_s=X^{(1)}_C$ for $|s|\ge T+1$.

**Lemma 2.1 (trajectories = intersections; proved here).** The map $\theta\mapsto\theta(-T')$ is a bijection from continuation trajectories $P\to Q$ onto $W^u(P)\cap\Psi^{-1}W^s(Q)$.

*Proof.* For $s\le-T'$ the equation is autonomous, so $\theta(s)\to P$ as $s\to-\infty$ if and only if $\theta(-T')\in W^u(P)$. Likewise $\theta(s)\to Q$ as $s\to+\infty$ if and only if $\theta(T')=\Psi(\theta(-T'))\in W^s(Q)$. ∎

**Definition 2.2.** For a diffeomorphism $\Psi$ of $S^3$ put
$$\overline B_\Psi(P,Q)=\widehat W^u(P)\ {}_{\mathrm{ev}}\!\times_{\Psi^{-1}\circ\mathrm{ev}}\ \widehat W^s(Q).$$
We say $\Psi$ is *transverse* if $\mathrm{ev}$ and $\Psi^{-1}\circ\mathrm{ev}$ are transverse on every pair of strata. For $M\in GL(4)$ write $B_M:=B_{M_*}$.

**Lemma 2.2 (bimodule axioms; proved here, using (W) and [11]).** If $\Psi$ is transverse, then:
* each $\overline B_\Psi(P,Q)$ is a compact $\langle|P|-|Q|\rangle$-manifold whose interior is $W^u(P)\cap\Psi^{-1}W^s(Q)$;
* its boundary is
$$\partial\overline B_\Psi(P,Q)=\bigcup_{P'}\overline{\mathcal M}(P,P')\times\overline B_\Psi(P',Q)\ \cup\ \bigcup_{Q'}\overline B_\Psi(P,Q')\times\overline{\mathcal M}(Q',Q),$$
  compatibly with composition at corners.

So $B_\Psi$ is a flow bimodule $\Sigma_Q(C_-)\to\Sigma_Q(C_+)$ in the sense of [1] and [2, Def. 0.0.3].

*Proof.*
* The target $S^3$ has no boundary. Stratum-wise transversality is therefore the transversality hypothesis of Joyce's fibre-product theorem [11, §6]. That theorem shows that the fibre product is a manifold with corners, and that its boundary is $(\partial\widehat W^u)\times\widehat W^s\cup\widehat W^u\times(\partial\widehat W^s)$ fibred over $S^3$.
* Substituting the faces from (W) gives the displayed formula. For instance,
$$\big(\overline{\mathcal M}(P,P')\times\widehat W^u(P')\big)\times_{S^3}\widehat W^s(Q)=\overline{\mathcal M}(P,P')\times\overline B_\Psi(P',Q),$$
  because $\mathrm{ev}$ factors through the second factor.
* The dimension is $(|P|-1)+(4-|Q|)-3=|P|-|Q|$.
* For the $\langle k\rangle$-structure, the face of level $i$ is the union of the faces through objects of grading $i$ in the cone (§2.4). Faces of the same level are disjoint, because chains of objects strictly decrease in grading (verify.py §5).
* By Lemma 2.1, the interior is the set of continuation trajectories. ∎

**Lemma 2.3 (isotopy invariance; proved here).** Let $\Psi_t$, $t\in[0,1]$, be a smooth path of transverse diffeomorphisms. Then $B_{\Psi_0}\cong B_{\Psi_1}$ as bimodules, by face-preserving diffeomorphisms that are compatible with the product decompositions of faces.

*Proof.*
* Consider the parametrized fibre product $\mathfrak B(P,Q)=\{(x,y,t):\mathrm{ev}(x)=\Psi_t^{-1}\mathrm{ev}(y)\}\subset\widehat W^u(P)\times\widehat W^s(Q)\times[0,1]$. Since the fibre over each $t$ is cut out transversally on every stratum, $\mathfrak B$ is a manifold with corners, and the projection $\pi:\mathfrak B\to[0,1]$ is a proper submersion on every stratum. Indeed, the derivative in fibre directions already surjects onto the normal space of the diagonal.
* Choose, by induction on $|P|-|Q|$, vector fields $V_{PQ}$ on $\mathfrak B(P,Q)$ that lift $\partial_t$, are tangent to every stratum, and satisfy:
  * $V_{PQ}=(0,V_{P'Q})$ on $\overline{\mathcal M}(P,P')\times\mathfrak B(P',Q)$;
  * $V_{PQ}=(V_{PQ'},0)$ on $\mathfrak B(P,Q')\times\overline{\mathcal M}(Q',Q)$.

  On corner strata $\overline{\mathcal M}\times\mathfrak B\times\overline{\mathcal M}$ both prescriptions give $(0,V_{P'Q'},0)$, by induction. So the boundary values are consistent.
* Extend from a collar of $\partial\mathfrak B$ into the interior. Lifts of $\partial_t$ that are tangent to strata exist locally and form an affine space, so a partition of unity glues them.
* The flow of $V_{PQ}$ from $t=0$ to $t=1$ is the required isomorphism. ∎

### 2.3 Quadrupole data reduce to linear transfers

**Lemma 2.4 (proved here).** Let $C(s)$ be a quadrupole datum, and let $\Phi=U(T)U(-T)^{-1}$ be the transfer of $v'=-C(s)v$.
1. $\theta=v/|v|$ solves $\theta'=X_{C(s)}(\theta)$ (verify.py §2). Hence the round part of the datum has transfer $\Phi_*$, and $\det\Phi=e^{-\int\operatorname{tr}C}=1$.
2. The transfer of the whole datum is $\Psi=\Xi_+\circ\Phi_*\circ\Xi_-$. The maps $\Xi_\pm$ are time maps of the metric-interpolation windows, and they preserve every $W^u(P)$ and every $W^s(Q)$ as sets.
3. If $\Phi_*$ is transverse, then $B_\Psi\cong B_{\Phi_*}$.
4. Every $M\in SL(4)$ is the transfer $\Phi$ of some quadrupole datum.

*Proof.*
1. By the quotient rule, $\theta'=(v'-\langle\theta,v'\rangle\theta)/|v|=-C\theta+\langle\theta,C\theta\rangle\theta$.
2. By [33, Lemmas 3.1–3.2], each field $-\nabla_{g_\lambda}\varphi_C$ is tangent to every coordinate great sphere $S_T$ and to every open hemisphere $W^u(P)$ and $W^s(Q)$. So the time maps of the non-autonomous window fields preserve these sets.
3. Shrink the windows to obtain an isotopy $\Psi_t=\Xi_+^t\Phi_*\Xi_-^t$ with $\Xi^0_\pm=\mathrm{id}$. Since $\Xi_\pm^t$ preserve the $W^u$ and $W^s$ sets, the pair $(W^u(P),\Psi_t^{-1}W^s(Q))$ is the image under $(\Xi_-^t)^{-1}$ of the pair $(W^u(P),\Phi_*^{-1}W^s(Q))$. The same holds on every stratum. Transversality is invariant under diffeomorphisms, so every $\Psi_t$ is transverse, and Lemma 2.3 applies.
4. The group generated by $\exp(\operatorname{Sym}^2_0)$ is a connected Lie subgroup of $SL(4)$. Its Lie algebra contains $\operatorname{Sym}^2_0$ and $[\operatorname{Sym}^2_0,\operatorname{Sym}^2_0]=\mathfrak{so}(4)$, hence equals $\mathfrak{sl}(4)$. So every $M\in SL(4)$ is a finite product $\prod\exp(-\tau_iS_i)$ with $S_i\in\operatorname{Sym}^2_0$. Short ramps joining $C$ to $0$ at the two ends have transfers $A_\pm\in SL(4)$. Write $A_+^{-1}MA_-^{-1}$ as such a product and realize it between the ramps by $C(s)=\rho_i'(s)S_i$ on consecutive intervals, where $\rho_i$ increases by $\tau_i$ and $\rho_i'$ vanishes at the endpoints. Conjugating by the end flows multiplies $M$ by positive diagonal matrices, which changes neither transversality nor the sign pattern of Theorem A (verify.py §3). ∎

### 2.4 Framed bimodules, cones and realizations

We use framed flow categories in the sense of Lipshitz–Sarkar [3, §3] (neat embeddings, framed normal bundles compatible with products) and their CJS realizations [6, 3]. Spherical reframings are taken in the sense of [36, §3.1]: a topological group $G\simeq GL_1(\mathbb S)$ with $j:O\to G$ realizing $J$, and coherent $G$-cocycles acting on $\mathbb S$-Thom classes, following Cohen [13].

**Definition 2.5.** Let $(\mathcal C,u)$ and $(\mathcal C',u')$ be framed flow categories and $B:\mathcal C\to\mathcal C'$ a bimodule.
* The *cone* $\mathrm{Cone}(B)$ has objects $\mathrm{Ob}\,\mathcal C\sqcup\mathrm{Ob}\,\mathcal C'$, with gradings $|x|+1$ for $x\in\mathcal C$ and $|y|$ for $y\in\mathcal C'$. Its morphism spaces are $\mathcal C(x,x')$, $\mathcal C'(y,y')$, $B(x,y)$, and $\emptyset$ from $\mathcal C'$ to $\mathcal C$. The bimodule axiom says exactly that this is a flow category; compare [2, Lemma 3.7.12].
* A *framing* of $B$ extending $(u,u')$ is a framing of $\mathrm{Cone}(B)$ that restricts to $u$ and $u'$.
* $\mathcal C'$ is downward closed in $\mathrm{Cone}(B)$, and the quotient is $\mathcal C$ shifted by one. Hence [3, §3] gives a cofibre sequence
$$|\mathcal C'|\to|\mathrm{Cone}(B)|\to\Sigma|\mathcal C|\xrightarrow{\ \partial\ }\Sigma|\mathcal C'| .$$
  We define $|B,f|:=\Sigma^{-1}\partial$.
* For a $G$-cocycle $h$ on the $B$-pieces, compatible with given $G$-cocycles on the ends, $(B,f\cdot h)$ is defined in the same way, with $\mathbb S$-Thom classes [36, §3.1].

By [2, Lemma 3.7.12], $\mathrm{Cone}(B)$ represents the cofibre of $B$ in $\mathrm{Flow}^\mu$, so $|B,f|$ is the cone-model description of the morphism represented by $B$.

*Spherical and vector-bundle framings.* Fix a framing $f_0$ of $B$ extending $(u,u')$. A *spherical framing* of $B$ extending $(u,u')$ is a framing $f_0\cdot h$ for a relative $G$-cocycle $h$ (§6), and a *spherical homotopy* between two of them is a homotopy of relative $G$-cocycles, rel the ends; this is the bimodule version of the spherical reframings of [36, §3.1]. A *vector-bundle framing* is a framing of $\mathrm{Cone}(B)$ in the sense of [3, §3], by framed normal vector bundles, and a vector-bundle homotopy is a homotopy through such framings; changing a vector-bundle framing by a vector-bundle framing is a spherical reframing by a cocycle with values in $j(O)$. Vector-bundle homotopic framings are spherically homotopic, but the converse is not claimed, and the two classifications differ in general (§8.2). Theorems B and C, and Corollary 2.7, concern spherical framings up to spherical homotopy, except where vector-bundle framings are named explicitly.

### 2.5 Imported inputs used for absolute statements

* **(R1)** [3, §3], [36, Lemma 3.2]: framings that are homotopic, relative to a subcategory, give realizations that are homotopy equivalent relative to the subcomplex.
* **(R2)** The cellular chain complex of the realization is the Morse complex with signs given by the framings of the 0-dimensional morphism spaces [3, §3], [13].
* **(R3)** [33, Thm. 1(4)] together with Bonciocat [10]: for every vector-bundle framing $u$, $|\Sigma_Q(C),u|\simeq X_0$. This is applied to $X^{(1)}_C$, which is Morse–Smale and in standard form near the zeros; it is the same input as in [33].
* **(R4)** [1], [2, §3.5]: the identity bimodule of a framed flow category is the conic degeneracy $D(\mathcal C(p,q),P)$ of [1, §6.1], [2, Lemma 3.5.1]. Over each broken trajectory with $k$ breaks, its fibre is a chain of $k+1$ intervals. This is our $\overline B_{\rm id}$: a broken trajectory with a marked level. It carries a canonical framing $f_{\rm can}$ [2, (3.10)] and realizes the identity.

(R3) is used only in Theorem B(5) and in the distinctness of the classes $\delta$ and $\delta+12$ in Theorem B(1). (R4) is used only for the statement $|B_{\rm id},f_{\rm can}|=\mathrm{id}$ in Theorem B(5)(a) and in remarks; the rest of B(5) does not need it. Theorems A, C, D and E, and the rest of Theorem B(1)–(4), depend on neither.

### 2.6 The HW link

*Time normalization.* We follow [32, §1.2]. The gauge-fixed HW system is $\partial_s\xi=F(\xi;\mu)$, $\mu=\bar\nu/\pi^2$, in the raw time $s$ of $\mathbb R\times S^3\times(0,\pi)$. The reduced field on the centre manifold is written in the normalized time $t=s/\pi$, and in these units [32, Thm. B] gives $\partial_\varepsilon f=(0,\kappa Cw)+O(|z|^2+|\bar\nu||z|)$ with $\kappa=-\frac{5\pi}{216}$; passing from raw to normalized time multiplies the raw coefficient $-\frac5{216}$ by $\pi$ [32, proof of Thm. B]. We prescribe the forcing path in the *slow normalized time*
$$\varsigma=\varepsilon|\kappa|\,t=\frac{\varepsilon|\kappa|}{\pi}\,s=\frac{5\varepsilon}{216}\,s .$$

**Proposition 2.6 (HW reduction).** Fix $\bar\nu\in(-\delta,0)$ as in setting (Q) of [33], and $K\ge1$. Let $\tilde C:\mathbb R\to\operatorname{Sym}^2_0(\mathbb R^4)$ be $C^2$, equal to $C$ (simple spectrum) for $|\varsigma|\ge T_0$, with $\|\tilde C\|_{C^2}\le K$. For $\varepsilon>0$ consider
$$\partial_s\xi=F(\xi;\mu)+\varepsilon\,\mathfrak p_{C_\varepsilon(s)}(\xi),\qquad C_\varepsilon(s)=\tilde C\Big(\frac{\varepsilon|\kappa|}{\pi}s\Big)=\tilde C\Big(\frac{5\varepsilon}{216}s\Big),\tag{2.6}$$
where $\mathfrak p_C$ is the Higgs-mass perturbation of [32], which is linear in $C$. A *local continuation trajectory* is a solution of (2.6) that stays in the neighbourhood $\mathcal U$ of [31] for all $s$, whose reduced curve stays in the isolating neighbourhood $\bar B$ of [31, Thm. D] for all $s$ (as in [32, Thm. C(2) and its proof, Step 2]), and which converges to objects as $s\to\pm\infty$.
1. *(Reduction; imported input (N1) below.)* For $0<\varepsilon<\varepsilon_1(\bar\nu,K)$, every solution of (2.6) that stays in $\mathcal U$ lies on a $C^{k-1}$ invariant manifold with time as a clock, $\{(z+\Psi(z,s),s)\}$, $z\in\mathbb R^5$, and its reduced curve solves (2.7) below.
2. *(Confinement; Lemma 2.6A.)* For $0<\varepsilon<\varepsilon_2(\bar\nu,K)$ the reduced non-autonomous system has an invariant manifold $\mathcal S\subset\bar B\times\mathbb R$ whose fibres are $C^1$-close to $\mathcal S_{\bar\nu}$, with one stable and one unstable normal direction. Every complete reduced solution that stays in $\bar B$, in particular the reduced curve of every local continuation trajectory, lies in $\mathcal S$.
3. In the angular coordinate and the time $\varsigma$, the flow on $\mathcal S$ is
$$\frac{d\theta}{d\varsigma}=X_{\tilde C(\varsigma)}(\theta)+r(\theta,\varsigma),\qquad\|r\|_{C^1}\le c\,\big(|\bar\nu|^{1/2}+\varepsilon\big).$$
4. If the model transfer $\tilde M$ of $v'=-\tilde C(\varsigma)v$ is transverse, then for $|\bar\nu|$ and then $\varepsilon$ small, the local HW continuation trajectories of index $\le0$ correspond bijectively to those of $B_{\tilde M}$, and they are cut out transversally. In particular there are none of negative index, and the cellular continuation map is $f_{\varepsilon(\tilde M)}$, up to the framing signs.

**Imported inputs.**
* **(N1)** *(Non-autonomous reduction with uniform estimates.)* For $0<\varepsilon<\varepsilon_1(\bar\nu,K)$, in normalized time $t=s/\pi$, the reduced curve $z(t)$ of a solution of (2.6) that stays in $\mathcal U$ solves
$$\dot z=f(z;\bar\nu)+R_\varepsilon(z,t)\quad\text{on }\bar B\times\mathbb R,\qquad \sup_t\|R_\varepsilon(\cdot,t)\|_{C^1(\bar B)}\le c_R\,\varepsilon,\qquad \sup_t\|\partial_tR_\varepsilon(\cdot,t)\|_{C^0(\bar B)}\le c_R\,\varepsilon^2,\tag{2.7}$$
where $f$ is the unperturbed reduced field of [31], $R_\varepsilon(z,t)=\varepsilon\,p_{C_\varepsilon}(z)+O(\varepsilon^2)$ with $p_C=(0,\kappa Cw)+O(|z|^2+|\bar\nu||z|)$ as in [32, Thm. B], and $c_R$ depends only on $(\bar\nu,K)$. *Source:* the global (cut-off) Lyapunov–Perron centre-manifold theorem [20, Ch. 2], with the clock $s'=1$ adjoined as an inert centre variable, applied exactly as in the autonomous case [31, §2], [32, Lemma 2.1]; the forcing $\varepsilon\mathfrak p_{C_\varepsilon(s)}$ is of class (P′) uniformly in $s$ [33, Lemma 2.1], and its $s$-derivative is $O(\varepsilon^2)$. We do not reprove this.
* **(N2)** *(Persistence.)* In the extended phase space, $\mathcal S_{\bar\nu}\times\mathbb R$ is a normally hyperbolic invariant manifold of $(\dot z,\dot t)=(f(z),1)$ with bounded geometry: its normal rates are $\pm\lambda$, $\lambda=\sqrt{10|\bar\nu|/3}\,(1+o(1))$ [32, Lemma 4.2], and its tangential rates vanish (the sphere consists of equilibria, and the clock is neutral). By (2.7) the perturbation is small in $C^1$, uniformly in $t$. The persistence theorem for noncompact normally hyperbolic manifolds with bounded geometry [17, 18, 19, 45] gives, for $0<\varepsilon<\varepsilon'(\bar\nu,K)$, an invariant manifold $\mathcal S$ which, in the tube coordinates of Lemma 2.6A, is a graph $n=\eta(\theta,t)$ with $\|\eta\|_{C^1}\le c_\eta\varepsilon$. We use only existence, invariance and this estimate; local uniqueness is proved in Lemma 2.6A.

**Lemma 2.6A (uniform non-autonomous confinement; proved here, given (N1), (N2)).** Write $z=(x,w)\in\mathbb R\times\mathbb R^4$. By $SO(4)$-equivariance and reversibility [31], the unperturbed field has the form $\dot x=a(x,|w|^2)$, $\dot w=x\,\tilde h(x,|w|^2)\,w$ with $a$ even in $x$ [32, Lemma 4.1], and $\mathcal S_{\bar\nu}=\{x=0,\ |w|=\rho_*\}$ with $\rho_*^2=\frac{32}{15}|\bar\nu|(1+o(1))$. Use the coordinates $w=(\rho_*+r)\theta$, $\theta\in S^3$, $n=(x,r)$, on $\{|n|<\rho_1\}$, $\rho_1:=\rho_*/2$.
1. *(Unperturbed normal system.)* In these coordinates $\dot\theta=0$ and $\dot n=N(n)$ with $N(0)=0$, exactly, where $N(x,r)=\big(a(x,(\rho_*+r)^2),\ x\tilde h(x,(\rho_*+r)^2)(\rho_*+r)\big)$; and
$$DN(0)=\begin{pmatrix}0&2g_S\rho_*\\ \tilde h\rho_*&0\end{pmatrix},\qquad g_S=-\tfrac58+O_2,\ \tilde h=-\tfrac54+O_2,$$
does not depend on $\theta$ and has eigenvalues $\pm\lambda$ [32, Lemma 4.1, Lemma 4.2] (verify.py §15). Fix a constant matrix $P$ with $P^{-1}DN(0)P=\Lambda=\operatorname{diag}(\lambda,-\lambda)$, and put $c_P=\|P\|\,\|P^{-1}\|$ and $c_2=\sup_{|n|\le\rho_1}\|D^2N(n)\|$.
2. *(Constants.)* Put $\rho_0=\min\big(\rho_1/2,\ \lambda/(16\,c_Pc_2),\ \tfrac12\operatorname{dist}(\mathcal S_{\bar\nu},\partial\bar B)\big)$ and $U_0=\{|n|<\rho_0\}$, an open tube around $\mathcal S_{\bar\nu}$ whose closure lies in the interior of $\bar B$ (recall $\mathcal S_{\bar\nu}=\operatorname{Inv}_0(\bar B)$ lies in the interior). Write the perturbed equation (2.7) as $\dot\theta=R^\theta$, $\dot n=N(n)+R^n$, with $\|(R^\theta,R^n)\|_{C^1}\le c_1\varepsilon$ on $\{|n|\le\rho_1\}$ ($c_1$ depends on $c_R$ and on the coordinate change).

Then there is $\varepsilon_2=\varepsilon_2(\bar\nu,K)>0$ such that for $0<\varepsilon<\varepsilon_2$:
* (i) every complete solution $z:\mathbb R\to\bar B$ of (2.7) satisfies $z(t)\in U_0$ for all $t$;
* (ii) every complete solution of (2.7) with $z(t)\in U_0$ for all $t$ lies in $\mathcal S$.

Hence the set of complete solutions of (2.7) in $\bar B$ is exactly $\mathcal S$, for every $\tilde C$ with $\|\tilde C\|_{C^2}\le K$ and over the whole time axis, including the entire continuation window $|\varsigma|\le T_0$. The constants $\lambda,P,c_P,c_2,\rho_0$ are explicit in terms of $\bar\nu$ and $f$; $\varepsilon_2$ is obtained from a compactness argument in (i) and the explicit conditions $c_\eta\varepsilon<\rho_0$ and $2c_Pc_1(1+c_\eta)\varepsilon\le\lambda/8$ in (ii).

*Proof.* (i) *Upper semicontinuity, uniform in time.* At $\varepsilon=0$, $\bar B$ is an isolating neighbourhood with $\operatorname{Inv}_0(\bar B)=\mathcal S_{\bar\nu}\subset U_0$ [31, Thm. D], [32, proof of Thm. C, Step 2]. Suppose $\varepsilon_n\to0$ and $z_n:\mathbb R\to\bar B$ are complete solutions of (2.7) for $\varepsilon_n$ (and paths $\tilde C_n$ with $\|\tilde C_n\|_{C^2}\le K$) with $z_n(t_n)\notin U_0$. Translate time: $y_n(t)=z_n(t+t_n)$ solves $\dot y=f(y)+R_{\varepsilon_n}(y,t+t_n)$, and $\sup|R_{\varepsilon_n}|\le c_R\varepsilon_n\to0$ uniformly in $t$, whatever the translation. The $y_n$ take values in the compact set $\bar B$ and have uniformly bounded derivatives, so by Arzelà–Ascoli a subsequence converges uniformly on compact intervals to some $y_\infty:\mathbb R\to\bar B$. Passing to the limit in the integral equation, $y_\infty$ solves $\dot y=f(y)$, so it is a complete unperturbed orbit in $\bar B$, and $y_\infty(0)\in\bar B\setminus U_0$ because $U_0$ is open. This contradicts $\operatorname{Inv}_0(\bar B)\subset U_0$. The time-dependence of the forcing does not enter the limit, which is why the argument is uniform over the whole continuation window.

(ii) *Local maximality, using both normal directions.* By (N2), $\mathcal S\cap\{|n|<\rho_1\}=\{n=\eta(\theta,t)\}$ with $\|\eta\|_{C^1}\le c_\eta\varepsilon$. Put $m=P^{-1}(n-\eta(\theta,t))$. Then $\dot m=G(\theta,m,t)$ with
$$G=P^{-1}\big[N(\eta+Pm)+R^n-D_\theta\eta\cdot R^\theta-\partial_t\eta\big],$$
and $G(\theta,0,t)=0$ because $\mathcal S$ is invariant. Hence $G(\theta,m,t)=(\Lambda+E)\,m$ with $E=\int_0^1\big(D_mG(\theta,\sigma m,t)-\Lambda\big)\,d\sigma$. The term $\partial_t\eta$ does not depend on $m$, so it does not enter $D_mG=P^{-1}\big[DN(n)+D_nR^n-D_\theta\eta\,D_nR^\theta\big]P$. Along a solution in $U_0$, every $n_\sigma=\eta+\sigma Pm$ is a convex combination of $\eta$ and $n$, so $|n_\sigma|<\rho_0$ once $c_\eta\varepsilon<\rho_0$, and
$$\|E\|\le c_P\big(c_2\rho_0+c_1\varepsilon+c_\eta c_1\varepsilon\big)\le\frac\lambda{16}+\frac\lambda8<\frac\lambda4 .$$
Let $q=m_1^2-m_2^2$. Then $\dot q=m^{\sf T}(2\lambda I+SE+E^{\sf T}S)m\ge\frac32\lambda|m|^2$, with $S=\operatorname{diag}(1,-1)$.
* If $q(t_0)\ge0$ and $m(t_0)\ne0$, then $m(t)\ne0$ for all $t$ (uniqueness, since $m\equiv0$ is a solution), $q$ is increasing, and $\dot q\ge\frac32\lambda q$ for $t\ge t_0$. So $|m(t)|^2\ge q(t)\to\infty$, which contradicts $|n|<\rho_0$.
* Otherwise $q<0$ for all $t$, i.e. $m_1^2<m_2^2$ and $|m|^2<2m_2^2$ (the unstable component is dominated). Then
$$\tfrac{d}{dt}m_2^2=2m_2\big(-\lambda m_2+(Em)_2\big)\le-2\lambda m_2^2+\tfrac\lambda2|m_2||m|\le-\big(2-\tfrac{\sqrt2}2\big)\lambda m_2^2\le-\lambda m_2^2 ,$$
so $m_2(t)^2\ge m_2(t_0)^2e^{\lambda(t_0-t)}\to\infty$ as $t\to-\infty$ unless $m_2(t_0)=0$, and $m_2(t_0)=0$ would give $q(t_0)\ge0$. Again a contradiction.

So $m\equiv0$, i.e. the solution lies in $\mathcal S$. verify.py §15 checks the normal block and its eigenvalues, $\dot\theta=0$ for the unperturbed field, and the two quadratic-form estimates. ∎

The argument does not use the asymptotics of a trajectory. Convergence to an object would not suffice for confinement, because the stable normal direction allows trajectories that converge to an object without lying in $\mathcal S$; by (i)–(ii) such a trajectory does not stay in $\bar B$ for all times, so it is not a local continuation trajectory.

*Proof of Proposition 2.6.*
1. This is (N1).
2. By (1), the reduced curve of a local continuation trajectory is a complete solution of (2.7) in $\bar B$. Lemma 2.6A gives that it lies in $\mathcal S$, which exists by (N2). The normal directions of $\mathcal S$ are those of $\mathcal S_{\bar\nu}$ up to $O(\varepsilon)$: one stable and one unstable [32, Lemma 4.2], [32, proof of Thm. C, Step 4]. The unstable line is the one that gives the grading shift $|P_a|=a$ [33, proof of Thm. 1(4)].
3. Apply [32, Lemma 4.2(2) and Cor. 4.3] fibrewise. In normalized time $t$ this gives $\dot\theta=\varepsilon|\kappa|X_{C_\varepsilon}(\theta)+\varepsilon\,O(|\bar\nu|^{1/2})+O(\varepsilon^2)$ in $C^1$, since $\kappa<0$. The $t$-dependence of the graph $\eta$ contributes a further $O(\varepsilon^2)$. Divide by $d\varsigma/dt=\varepsilon|\kappa|$. In raw time $s$ the same equation reads $d\theta/ds=\frac{\varepsilon|\kappa|}{\pi}X+\dots$, which is why $\varsigma=\varepsilon|\kappa|s/\pi$ (verify.py §15).
4. *Existence.* Let $\theta_0(\varsigma)$ be an index-0 model trajectory. It is nondegenerate: its linearization $\partial_\varsigma-DX_{\tilde C}(\theta_0)$ is Fredholm of index 0 between Sobolev spaces on $\mathbb R$ with hyperbolic ends [28, 29], and it is onto by transversality [16, 27], hence an isomorphism. Moreover $r$ is $C^1$-small, and the end fields converge to the perturbed autonomous fields with hyperbolic zeros. So the implicit function theorem gives a unique perturbed trajectory near $\theta_0$. Its lift to $\mathcal S$ stays in $\bar B$, so it is a local continuation trajectory.
   *Uniqueness and absence of negative index.* By (2) every local continuation trajectory lies in $\mathcal S$, so it is a solution of the equation in (3). Suppose a sequence of such trajectories of index $\le0$ does not converge to a model trajectory of index 0. By the standard compactness for ODE trajectories with converging data [16, Ch. 2], a subsequence converges to a broken model trajectory: autonomous pieces of index $\ge1$ and one continuation piece. Its total index is $\le0$, and by transversality every model continuation piece has index $\ge0$. So the limit is unbroken and of index 0, and the sequence eventually lies in the uniqueness neighbourhood of the implicit function theorem.
   Finally, the cellular map counts these trajectories with signs. ∎

**Remark 2.6B (the parametrization of the second version).** If the forcing path is prescribed instead as $C_\varepsilon(s)=\tilde C(\varepsilon|\kappa|s)$, as in the second version of this paper, then $\varepsilon|\kappa|s=\pi\varsigma$ and the leading angular equation becomes
$$\frac{d\theta}{d(\varepsilon|\kappa|s)}=\frac1\pi X_{\tilde C(\varepsilon|\kappa|s)}(\theta)+\text{remainder},$$
with linear equation $v'=-\frac1\pi\tilde C(\cdot)v$. This is Proposition 2.6 for the path $\varsigma\mapsto\tilde C(\pi\varsigma)$ (with $K$ replaced by $\pi^2K$), so Proposition 2.6(4) and Corollary 2.8 hold with $\tilde M$ replaced by the transfer $\tilde M_\pi$ of $v'=-\frac1\pi\tilde C v$ (verify.py §15). The factor cannot be absorbed by reparametrizing trajectories while keeping the prescribed path: $\tilde M_\pi$ and $\tilde M$ can have different sign patterns, and hence different cellular maps (Remark 4.1). Both lie in $SL(4)$, so the action on homology, $\pm(1,1)$, is the same.

*What is not claimed.* We do not prove that the compactified HW continuation moduli spaces of positive dimension are isomorphic to the model ones as topological bimodules. That would need a non-autonomous version of the transport of [33, §4]. Theorems A–E are statements about the model. We isolate the missing step as a hypothesis.

**Hypothesis (H$_{\rm HW}$).** In the setting of Proposition 2.6(4), with transverse model transfer $\tilde M$, for $|\bar\nu|$ and then $\varepsilon$ small: the compactified moduli spaces $\overline{\mathcal B}^{\rm HW}(P,Q)$ of reduced HW continuation trajectories, of all indices, form a flow bimodule $\mathcal B^{\rm HW}$ between the HW categories (identified with $\Sigma_Q(C)$ by [33, Thm. 1(2)]), and there are homeomorphisms $\overline{\mathcal B}^{\rm HW}(P,Q)\cong\overline B_{\tilde M}(P,Q)$ that preserve the face stratification, are compatible with the product decompositions of faces, and extend the bijection of Proposition 2.6(4) on index-0 pieces.

**Corollary 2.7 (conditional on (H$_{\rm HW}$)).** Assume (H$_{\rm HW}$). Then Theorem A(2)–(5) describe $\mathcal B^{\rm HW}$; the spherical framings of $\mathcal B^{\rm HW}$ relative to the ends, up to spherical homotopy, are classified as in Theorem B(1), with realizations given by Theorem B(2)–(4); with equal end framings $u$ the realized self-equivalences are exactly $\operatorname{Aut}^+(X_0)$ (Theorem B(5)(a), (b)); and the reframing criterion of Theorem C(2) holds for $\mathcal B^{\rm HW}$. *Proof.* All these statements depend on $B_{\tilde M}$ only through its pieces, their faces and their product decompositions, which (H$_{\rm HW}$) transports; framings and relative cocycles are transported along the homeomorphisms. ∎

(H$_{\rm HW}$) does not provide a framing of $\mathcal B^{\rm HW}$ from index theory, so Corollary 2.7 classifies spherical framings but does not say which class an index-theoretic framing would have.

**Corollary 2.8 (not conditional on (H$_{\rm HW}$); proved modulo the imported inputs (N1)–(N2) of Proposition 2.6).** In the setting of Proposition 2.6(4), with $\tilde M$ the transfer of $v'=-\tilde C(\varsigma)v$ in the slow normalized time $\varsigma$ of (2.6), with the same framing of the HW quadrupole category at both ends, the HW cellular continuation map is $\pm D f_{\varepsilon(\tilde M)}D$, where $D$ records the framing signs of the end objects, and it acts on $(H_1,H_4)$ by $\pm(1,1)$. *Proof.* By Proposition 2.6(2) and (4) all local index-0 HW trajectories lie on $\mathcal S$ and are in bijection with the points of $B_{\tilde M}$, so the map has the support of $f_\varepsilon$; it is a chain map, and §3.6 shows that this leaves only $\pm Df_\varepsilon D$, with action $\pm(1,\prod\varepsilon)$. Finally $\tilde M\in SL(4)$, so $\prod\varepsilon=+1$ (Theorem A(4)). ∎

In particular, already at the level of homology, no HW continuation map of this local type can realize a self-equivalence with $\chi=-1$; this is the HW counterpart of Theorem B(5)(b), and it does not need (H$_{\rm HW}$). It holds in either time parametrization of the forcing path (Remark 2.6B).

---

## 3. Proof of Theorem A

**3.1 Linearization (A1).** This is Lemma 2.4(1, 4) together with Lemma 2.1: $B_\Psi$ for the datum equals $B_{\Phi_*}$ up to the isotopy of Lemma 2.4(3). The Riccati form of the 2×2 blocks, $y=\theta_1/\theta_0$, satisfies $y'=by^2+(a-c)y-b$ (verify.py §2). In gnomonic charts $y_b=\theta_b/\theta_a$, the autonomous flow is exactly linear: $y_b'=-(c_b-c_a)y_b$.

**3.2 Moduli spaces (A2).** By Lemma 2.1 with $\Psi=M_*$, a continuation trajectory is a point $[u]$ with $[u]\in W^u(P_a^\sigma)$ and $[Mu]\in W^s(Q_b^\tau)$. Substituting the hemispheres of §1.2 gives the formula.

**3.3 Transversality (A3).** The strata of $\widehat W^u(P_a)$ map onto the cells $W^u(P_{a'})$, $a'\le a$, and those of $\widehat W^s(Q_b)$ map onto $W^s(Q_{b'})$, $b'\ge b$. So stratum-wise transversality means that, for all $a',b'$, the linear spaces $E_{a'}$ and $M^{-1}F_{b'}$ meet transversally in $\mathbb R^4$. That is,
$$\dim\big(E_{a'}\cap M^{-1}F_{b'}\big)=\max(a'-b'+1,0).$$
In coordinates, $u\in E_{a'}$ and $(Mu)_i=0$ for $i<b'-1$. The condition is that the top-left block $M[0..b'-2,\,0..a'-1]$ has full rank $\min(b'-1,a')$.
* If $\Delta_k\ne0$ for $k=1,2,3$, every such block contains a nonsingular leading square block, so it has full rank. ($\Delta_4=\det M\ne0$ always.)
* Conversely, if $\Delta_k=0$ for some $k\in\{1,2,3\}$, take $a'=k$ and $b'=k+1$. The block $M[0..k-1,0..k-1]$ is singular, so $E_k\cap M^{-1}F_{k+1}\ne0$, although the expected dimension is $-1$.

verify.py §3 checks all $a',b'$ exactly on 50 random transverse integer matrices, with a non-transverse control. The rest of (A3) is Lemma 2.2.

**3.4 Classification (A4).**

*Step 1 (LDU).* Since $\Delta_1,\dots,\Delta_4\ne0$, we can write (classical LU decomposition [43]; Remark 1.1) $M=LDU$ with $L$ lower unitriangular, $U$ upper unitriangular and $D=\operatorname{diag}(d_1,\dots,d_4)$, $d_a=\Delta_a/\Delta_{a-1}$. Then $\Delta_k(LDU)=d_1\cdots d_k$ (verify.py §3, symbolic). Moreover:
* $U$ preserves each $E_a$ and the coefficient $u_{a-1}$ of $u\in E_a$;
* $L$ preserves each $F_b$ and the coefficient $(\cdot)_{b-1}$ on $F_b$.

*Step 2 (deformation within the cell).* Put $M_t=L_tDU_t$ with $L_t=I+t(L-I)$ and $U_t=I+t(U-I)$. These stay unitriangular, and $\Delta_k(M_t)=\Delta_k(D)\ne0$ for all $t$. Next deform $|D|$ to $I$ through positive diagonal matrices. Throughout, every $M_t$ is transverse by 3.3. By Lemma 2.3, $B_M\cong B_{R}$ with $R=\operatorname{sgn}(D)=\operatorname{diag}(\operatorname{sgn}d_a)$. Since $\operatorname{sgn}d_a=\operatorname{sgn}(\Delta_a\Delta_{a-1})=\varepsilon_a$, we have $R=R_\varepsilon$.

*Step 3 ($B_{R_\varepsilon}$ is the twisted identity).* $R_\varepsilon$ commutes with $X^{(1)}_C$ (§2.1). So it maps the compactified stable manifolds by $R_\varepsilon\widehat W^s(Q)=\widehat W^s(R_\varepsilon Q)$, compatibly with faces. Hence
$$\overline B_{R_\varepsilon}(P,Q)=\widehat W^u(P)\times_{S^3}R_\varepsilon^{-1}\widehat W^s(Q)=\widehat W^u(P)\times_{S^3}\widehat W^s(R_\varepsilon^{-1}Q)=\overline B_{\rm id}(P,R_\varepsilon^{-1}Q).$$
The face identifications are those of $B_{\rm id}$, followed by the automorphism $R_\varepsilon$ of $\Sigma_Q(C)$ on the target factors.

*Step 4.* We have $\prod_a\varepsilon_a=\operatorname{sgn}(\Delta_0\Delta_4)\prod_{k=1}^3\operatorname{sgn}(\Delta_k)^2=\operatorname{sgn}\det M$. The statement about equal sign patterns follows from Step 2, because the set of $LDU$ with fixed signs of $D$ is connected.

verify.py §3 also checks the index-0 pieces directly. For every $b$, $B_M(P_b^+,Q_b^\tau)\ne\emptyset$ if and only if $\tau=\varepsilon_b$, on all samples and for all 16 matrices $M=R_\varepsilon$. ∎

**3.5 Shapes (A5).** By Step 3 it suffices to treat $B_{\rm id}$. An element of $\overline B_{\rm id}(P,Q)$ consists of:
* a chain $P=a_0>\dots>a_i$ of broken trajectories in the source;
* an element of $B_{\rm id}(a_i,b_0)$, which is a constant trajectory if $a_i=b_0$ and otherwise a trajectory with a marked level;
* a chain $b_0>\dots>b_j=Q$ in the target.

The dimension of such a stratum is $\sum\dim\mathcal M+\dim B$. This is the conic degeneracy of [1, §6.1] described in (R4). Enumerating strata (verify.py §5) gives:
* $f$-vectors $(2,1)$, $(6,6,1)$ and $(16,24,10,1)$, so the pieces are an interval, a hexagon and a 3-polytope;
* Euler characteristic $1$ in each case;
* for the 3-polytope, 6 square facets ($\overline{\mathcal M}(P_4,P_1)\times\mathrm{pt}$, $\mathrm{pt}\times\overline{\mathcal M}(P_4,P_1)$, and four products of intervals) and 4 hexagonal facets ($\mathrm{pt}\times\overline B(P_3^u,P_1)$ and $\overline B(P_4,P_2^u)\times\mathrm{pt}$);
* every codimension-2 stratum lies in exactly two facets.

Each piece is compact and contractible, with boundary a sphere. Its interior is homeomorphic to an open ball, since $W^u(P)\cap W^s(Q)$ is the set of rays in an open convex cone, and a collar of the boundary gives contractibility. The boundary is a connected closed surface with Euler characteristic $16-24+10=2$, hence $S^2$. These are the only properties of the pieces that we use. (They are in fact the conic-degeneracy polytopes of [1, §6.1].)

The total counts are as follows:
* 8 points $B(P,P)$;
* 12 intervals $B(P_a^s,P_{a-1}^t)$;
* 8 hexagons $B(P_a^s,P_{a-2}^t)$;
* 4 balls $B(P_4^s,P_1^t)$. ∎

**3.6 Cellular map (A6).** By (R2), the chain map counts the index-0 pieces with signs. By 3.4 there is exactly one point in $B_M(P_a^\tau,Q_a^{\varepsilon_a\tau})$. With the orientation of each cell $W^u(\pm e_{a-1})$ given by the projection chart $(\theta_0,\dots,\theta_{a-2})$, the reflection $R_\varepsilon$ acts on that chart by $\operatorname{diag}(\varepsilon_1,\dots,\varepsilon_{a-1})$. This gives the sign $\prod_{c<a}\varepsilon_c$.

The cellular differential in these orientations is $d(e_a^\tau)=(-1)^a(e_{a-1}^+-e_{a-1}^-)$. verify.py §4 checks:
* $d^2=0$;
* homology $\mathbb Z[1]\oplus\mathbb Z[4]$, torsion-free;
* $H_4=\mathbb Z(e_4^+-e_4^-)$, so $\sigma=(1,-1)$, and $e_1^+\sim e_1^-$ in $H_1$, so $\tau=(1,1)$;
* $f_\varepsilon d=df_\varepsilon$ for all 16 sign vectors;
* the action $(1,\prod\varepsilon)$ on $(H_1,H_4)$.

*Framing signs.* With framings, the end objects acquire signs, recorded by a diagonal matrix $D$ (the same at both ends when the end framings agree), and the framed differential is $DdD$; indeed every sign assignment on the support of $d$ with square zero has this form (each $2\times2$ block is a rank-one sign matrix and consecutive blocks are orthogonal; verify.py §14 checks all $2^{12}$ assignments). The framed cellular map $g$ of $B_M$ is a chain map for $DdD$ with the support of $f_\varepsilon$ (one point in each $B_M(P_a^\tau,Q_a^{\varepsilon_a\tau})$). Then $DgD$ is a chain map for $d$ with the same support. Among the $2^8$ sign vectors on this support exactly two give chain maps, $\pm f_\varepsilon$ (verify.py §14, all 16 $\varepsilon$; the graph of points and intervals is connected, §6.1). So $g=\pm Df_\varepsilon D$, and since conjugation by $D$ does not change the action on homology relative to the corresponding generators, $g$ acts on $(H_1,H_4)$ by $\pm(1,\prod\varepsilon)$ (verify.py §14, also for 12 choices of $D$). ∎

---

## 4. Proof of Theorem D (codimension-one events)

**4.1 End data (D1).**
* The flow of $X^{(1)}_C$ is Morse–Smale for every simple spectrum [33, Lemma 3.2]. Objects of equal index have equal values $c_{a-1}/2$, so they are never connected by trajectories, and no handle slide occurs.
* Non-simple traceless spectra form a subset of dimension $7$ in the 9-dimensional space $\operatorname{Sym}^2_0(\mathbb R^4)$: 2 eigenvalue parameters plus the 5-dimensional manifold of flags of type $(2,1,1)$. This is the von Neumann–Wigner codimension 2 [25] (verify.py §11). So generic one-parameter families avoid it.
* Along a loop $C_\lambda$ of simple-spectrum data, continue the eigenvectors $e_a(\lambda)$ continuously. Then $e_a(1)=\varepsilon_ae_a(0)$, with $\prod\varepsilon=1$ because the frame stays in $SO(4)$, and the induced automorphism of $\Sigma_Q(C)$ is $R_\varepsilon$.
* Rotating a pair of eigenvectors by $\pi$ in their plane, $C_\lambda=\mathrm{Rot}(\pi\lambda)C\mathrm{Rot}(\pi\lambda)^{\sf T}$, realizes the six $R_\varepsilon$ with two minus signs. These generate the order-8 group $\{R_\varepsilon:\prod\varepsilon=1\}$ (verify.py §11).

**4.2 Walls (D2).** Suppose $\Delta_k(M_{\lambda_0})=0$ with the other minors nonzero.
* *The index $-1$ trajectories.* The $k\times k$ system $M[0..k-1,0..k-1]u=0$ has a one-dimensional kernel. Two further facts hold for a nonzero kernel vector $u$:
  * $u_{k-1}\ne0$. Otherwise $\Delta_{k-1}=0$.
  * $(Mu)_k\ne0$. Otherwise the first $k$ columns of $M[0..k,0..k]$ would be dependent, and $\Delta_{k+1}=0$.

  So $\pm u$ give exactly two points of $W^u(P_k^{\pm\sigma})\cap M_*^{-1}W^s(Q_{k+1}^{\pm\tau})$, and they are antipodal. All other pieces of negative expected dimension stay empty, because that would require another minor to vanish.
* *The sign jump.* $\Delta_k$ changes sign transversally, so $\varepsilon_k=\operatorname{sgn}(\Delta_{k-1}\Delta_k)$ and $\varepsilon_{k+1}=\operatorname{sgn}(\Delta_k\Delta_{k+1})$ both flip, and the other $\varepsilon_a$ do not.
* *The chain homotopy.* The parametrized moduli spaces over a neighbourhood of $\lambda_0$ give the standard continuation chain homotopy: $K$ counts the index $-1$ trajectories at $\lambda_0$ with signs [14, 15, 16]. For every $k$ and every $\varepsilon$, verify.py §4 solves $f_{\varepsilon'}-f_\varepsilon=dK+Kd$ over all $K:C_k\to C_{k+1}$ with entries in $\{-1,0,1\}$. There are exactly two solutions. Each has exactly two nonzero entries, in antipodal positions $(P_k^{s}\to Q_{k+1}^{t})$ and $(P_k^{-s}\to Q_{k+1}^{-t})$, and the two solutions use the two antipodal pairs. The homogeneous integer solutions form a rank-one lattice (verify.py §4). So the algebra forces the antipodal support of the geometric $K$, and it determines $K$ once the target of one trajectory is known.

  For $\varepsilon=(+,+,+,+)$ and $k=1$, for instance, one solution is $K(e_1^+)=-e_2^{t}$, $K(e_1^-)=e_2^{-t}$. ∎

**4.3 The explicit wall (D3).** Let $\theta(s)=\omega s$ for $s\in[0,\pi/\omega]$, let $\mathrm{Rot}$ denote the rotation in the $(e_0,e_1)$-plane, and put $C(s)=\mathrm{Rot}(\theta(s))C\mathrm{Rot}(\theta(s))^{\sf T}$.
* Since $\mathrm{Rot}(\pi)C\mathrm{Rot}(\pi)^{\sf T}=C$, this is a loop of data.
* In the rotating frame $w=\mathrm{Rot}(\theta)^{\sf T}v$ we have $w'=-(C_0+\omega J)w$, because $\mathrm{Rot}^{\sf T}\partial_\theta\mathrm{Rot}=J$. So
$$\Phi=\mathrm{Rot}(\pi)\,e^{-At}\oplus\operatorname{diag}(e^{-c_2t},e^{-c_3t}),\qquad A=\operatorname{diag}(c_0,c_1)+\omega J,\quad t=\pi/\omega .$$
* Write $A=mI+N$ with $m=\frac{c_0+c_1}2$. Then $N^2=(\delta^2-\omega^2)I$, so for $\omega>\delta$, with $q=\sqrt{\omega^2-\delta^2}$,
$$e^{-At}=e^{-mt}\Big(\cos(qt)I-\frac{\sin qt}{q}N\Big),\qquad [e^{-At}]_{00}=e^{-mt}\Big(\cos qt+\frac\delta q\sin qt\Big).$$
  For $\omega\le\delta$ the analogous expression with $\cosh$ and $\sinh$ is positive (verify.py §9, symbolic).
* So $\Delta_2=e^{-2mt}>0$ and $\Delta_3=\Delta_2e^{-c_2t}>0$, while $\Delta_1=-[e^{-At}]_{00}$.
* Put $r=\delta/\omega$ and $y=\sqrt{1-r^2}$, so that $qt=\pi y$. Then $\operatorname{sgn}[e^{-At}]_{00}=\operatorname{sgn}F(y)$ with
$$F(y)=\cot(\pi y)+\frac{\sqrt{1-y^2}}{y},\qquad F'(y)=-\frac{\pi}{\sin^2\pi y}-\frac1{y^2\sqrt{1-y^2}}<0 .$$
  Since $F(0^+)=+\infty$ and $F(1^-)=-\infty$, $F$ has exactly one zero $y_*$. It lies in $(\frac12,1)$ because $\cot(\pi y)<0$ there. As $\omega$ increases, $y$ increases, so:
  * for $\omega<\omega^*$, $\Delta_1<0$ and $\varepsilon=(-,-,+,+)$;
  * for $\omega>\omega^*$, $\varepsilon=(+,+,+,+)$.
* At $\omega^*$, the vector $\Phi e_0$ has no $e_0$-component, so the minimum $e_0$ is carried exactly onto $\pm e_1$. The crossing is transversal because $F'(y_*)\ne0$ and $dy/d\omega>0$.

The values $y_*=0.7364844482$ and $r_*=0.6764544756$ come from bisection, and a direct ODE integration confirms the sign change [N]. ∎

*Interpretation.* Slow transport realizes the monodromy $R_\varepsilon$ of 4.1, and fast transport realizes the identity. Between them lies exactly one handle-slide-type wall. By Theorem A(6), both sides act by $(1,1)$ on homology. This illustrates that the unframed continuation bimodule depends on the path, while its homological shadow does not.

**Remark 4.1 (the rotating loop as HW forcing; time normalization).** Theorem D(3) is a statement about the model equation $v'=-C(s)v$, and it is unchanged. As HW forcing, let $\tilde C(\varsigma)$ be the rotating loop with angular speed $\omega$ in $\varsigma$.
* With the normalization of (2.6), $\varsigma=\varepsilon|\kappa|s/\pi$, the HW transfer is the model one: the HW wall is at $\omega^*=\delta/r_*$, and the HW pattern is $(-,-,+,+)$ for $\omega<\omega^*$ and $(+,+,+,+)$ for $\omega>\omega^*$.
* With the parametrization $\tilde C(\varepsilon|\kappa|s)$ of the second version (Remark 2.6B), the transfer is that of $v'=-\frac1\pi\tilde C v$. In the rotating frame, $(\frac1\pi C_0+\omega J)\frac\pi\omega=(C_0+\pi\omega J)\frac{\pi}{\pi\omega}$, so this is the model transfer at speed $\pi\omega$, and the wall moves to $\omega^*/\pi$.
* *Example (the referee's).* $(c_0,c_1,c_2,c_3)=(-0.15,-0.05,0.05,0.15)$, $\delta=0.05$, $\omega=0.05$, so $\omega^*\approx0.0739$ and $\omega^*/\pi\approx0.0235$. For coefficient $1$ we have $\omega=\delta$, $[e^{-At}]_{00}=e^{-mt}(1+\delta t)>0$, and $\Delta_1\approx-2217.8<0$: the pattern is $(-,-,+,+)$. For coefficient $1/\pi$, $\Delta_1\approx6.887>0$: the pattern is $(+,+,+,+)$. So for the HW path $\tilde C(\varepsilon|\kappa|s)$ the second version, which combined Theorem D(3) with its Proposition 2.6, predicted the pattern $(-,-,+,+)$, whereas the correct HW pattern is $(+,+,+,+)$. With the normalization of (2.6), i.e. for the HW path $\tilde C(\varepsilon|\kappa|s/\pi)$, the HW pattern at $\omega=0.05$ is $(-,-,+,+)$, as in Theorem D(3).
* The two cellular maps $f_{(-,-,+,+)}$ and $f_{(+,+,+,+)}$ are different, but chain homotopic (Theorem D(2)), and both act by $(1,1)$ on $(H_1,H_4)$. So the homological action, and Corollary 2.8, are unchanged.

verify.py §15 checks the speed identity, both values of $\Delta_1$ (closed formula and direct ODE integration of the $4\times4$ transfer, with $\det=1$), the full sign patterns, the position of both walls, and the cellular maps.

**4.4 The pitchfork family (D4).** The critical points of $g_k=\varphi_C-k\theta_0$ on $S^3$ satisfy $C\theta-ke_0=\lambda\theta$.
* $\pm e_0$ are critical for all $k$. At $-e_0$ we have $\lambda=c_0+k$, and the Hessian eigenvalues are $c_j-c_0-k$; at $e_0$ they are $c_j-c_0+k>0$.
* For each $j$ and $k<\Delta_j$ there is a pair with $\theta_0=-k/\Delta_j$ and $\theta_j=\pm\sqrt{1-\theta_0^2}$. Along the circle the second derivative is $(k^2-\Delta_j^2)/\Delta_j<0$, so the pair has index $j$ (verify.py §10).
* The Euler characteristic vanishes in each regime.
* The coordinate reflections $\theta_j\mapsto-\theta_j$ ($j\ge1$) preserve $g_k$. So the circles in the $(e_0,e_j)$-planes are invariant, and on them $t'=-\sin t(\Delta_j\cos t+k)$.
* Putting $t=\pi+x$ gives the normal form stated in Theorem D(4). This is a $\mathbb Z/2$-symmetric pitchfork [24, Ch. VI]. At $k=\Delta_j$ the cubic coefficient is $\Delta_j/2>0$. For $s$-dependent $\mu(s)$, the cubic truncation $x'=\mu x+ax^3$ is linearized by $y=x^{-2}$ into $y'=-2\mu y-2a$ (verify.py §10). With a quintic term $bx^5$ the same substitution gives $y'=-2\mu y-2a-2b/y$, which is not linear (verify.py §15); so only the truncation is linearized.
* For $k>\Delta_3$ only $\pm e_0$ remain, the minimum and the maximum, so the flow category is $\Sigma_H$ with $\overline{\mathcal M}=S^2$.

The symmetric family is *not* transverse as continuation data. By symmetry, $\Psi^{-1}(-e_0)=-e_0$ lies in the 0-skeleton. A generic perturbation of the window moves $p^*$ into a 3-cell, which is the hypothesis of Theorem E. ∎

---

## 5. Three lemmas on framed cones

**Lemma 5.1 (disc modification; [36, Lemma 3.4], reproved).** Let $\mathcal D$ be a framed flow category, and let $x$ be maximal and $y$ minimal with $k=|x|-|y|-1$. Let $g$ be a $G$-cocycle that equals $1$ except on one component $W\subset\overline{\mathcal D}(x,y)$, where it is a map $(W,W\setminus D_0)\to(G,1)$ for a closed disc $D_0$ in the interior, with class $\gamma\in\pi_k(G)=\pi_k^s$.
* $g$ is coherent.
* The attaching map $\varphi'_x$ of the cell $e_x$ in $|\mathcal D|_{u\cdot g}$ agrees with $\varphi_x$ off a small disc in $S^{|x|-1}$. On that disc, both maps land in $e_y\cup\{*\}$, and their difference class is $\iota_y\circ\gamma$.

*Proof.*
* Coherence is vacuous, since $W$ is not a factor of any face and $g=1$ on $\partial W$.
* The component of $\varphi_x$ towards $e_y$ is the Pontryagin–Thom collapse onto the framed normal bundle of $\overline{\mathcal D}(x,y)$ [3, §3], [13, (16)]. Changing the Thom class over $D_0$ changes it only on the collapse of a tube around $D_0$. There the old map is the trivial collapse $S^{N+k}\to\Sigma^N(D_0/\partial D_0)\to S^N$, and the new one is its twist by the adjoint of $g|_{D_0}$, i.e. by $\gamma$. ∎

**Lemma 5.2 (moving an attaching map inside a subcomplex; proved here).** Let $K$ be a finite CW spectrum, $A\subset K$ a subcomplex, $Y=K\cup_\varphi e^n$ and $Y'=K\cup_{\varphi'}e^n$. Assume:
* $\varphi'=\varphi$ outside a disc $D_0\subset S^{n-1}$;
* $\varphi(D_0)\subset A$ and $\varphi'(D_0)\subset A$;
* the difference class is $\alpha=[\varphi'|_{D_0}\cup\varphi|_{D_0}]\in\pi_{n-1}(A)$.

Then $Y/A=Y'/A$ canonically, and the connecting maps of $A\to Y\to Y/A$ and $A\to Y'\to Y'/A$ satisfy
$$\partial'=\partial+\Sigma\alpha\circ p,$$
where $p:Y/A\to S^n$ collapses $K/A$. The same holds for several cells and discs simultaneously.

*Proof.* After suspending, we may work with finite CW complexes.
* $q\varphi=q\varphi'$ on the nose, so $Y/A=Y'/A$.
* The connecting map is $Y/A\xleftarrow{\simeq}Y\cup CA\to\Sigma A$, where the second map collapses $Y$.
* In $K\cup CA$, the maps $\varphi'|_{D_0}$ and $\varphi|_{D_0}$ agree on $\partial D_0$ and take values in $A\subset CA$. Since $CA$ is contractible, they are homotopic rel $\partial D_0$ through a homotopy $H$ in $CA$. Extending $H$ by the constant homotopy off $D_0$ gives $G:\varphi'\simeq\varphi$ in $K\cup CA$.
* Let $Z=(K\cup CA)\cup_\varphi D^n$ and $Z'=(K\cup CA)\cup_{\varphi'}D^n$. Define $E:Z\to Z'$ as follows:
  * $E$ is the identity on $K\cup CA$;
  * on the inner disc, $x\mapsto2x$ for $|x|\le\frac12$;
  * on the annulus, $x\mapsto G(x/|x|,2|x|-1)$.

  $E$ is a homotopy equivalence relative to $K\cup CA$. Modulo $CA$ it is homotopic to the identity of $Y/A$, because $G$ is constant modulo $CA$.
* Compose with the collapse $c':Z'\to\Sigma A$. This collapse is $c$ on $K\cup CA$ and trivial on the inner disc. On the annulus it is the map $(D_0\times I)/\partial\to CA/A=\Sigma A$ given by $H$, which is $\Sigma$ of the difference map $D_0\cup D_0\to A$, i.e. $\Sigma\alpha$ on the pinched annulus. So $c'E=c+\Sigma\alpha\circ p$. ∎

**Lemma 5.3 (bimodule modification; proved here).** Let $(B,f)$ be a framed bimodule $(\mathcal C,u)\to(\mathcal C',u')$. Let $x\in\mathcal C$ be maximal and $y\in\mathcal C'$ minimal. Let $h$ be a relative $G$-cocycle on $B$ that equals $1$ except in a disc of a component of $\overline B(x,y)$, where it has class $\gamma\in\pi_{|x|-|y|}^s$. Then
$$|B,f\cdot h|=|B,f|+\iota_y\circ\gamma\circ q_x,$$
where $q_x$ collapses onto the cell $e_x$ and $\iota_y$ includes the cell $e_y$.

*Proof.*
* In $\mathrm{Cone}(B)$, $x$ has grading $|x|+1$ and is maximal, and $y$ is minimal. Lemma 5.1 applies with $\mathcal D=\mathrm{Cone}(B)$, $k=|x|-|y|$.
* The cocycle changes neither the other attaching maps nor the subcomplex $A=|\mathcal C'|$.
* Lemma 5.2 applies with $K=|\mathrm{Cone}|\setminus\mathrm{int}\,e_x$ and $\alpha=\iota_y\gamma$. Here $p=\Sigma q_x$ under $|\mathrm{Cone}|/A=\Sigma|\mathcal C|$. Desuspend. ∎

**Lemma 5.4 (homotopy invariance; proved here, using (R1)).** If two framings of $B$ extending $(u,u')$ are homotopic relative to the ends, the induced maps are homotopic.

*Proof.* A homotopy of framings of $\mathrm{Cone}(B)$, constant on $\mathcal C'$ and on $\mathcal C[1]$, gives by (R1) a realization over $[0,1]$. It contains the constant subcomplex $|\mathcal C'|\times[0,1]$, and its quotient is the constant $\Sigma|\mathcal C|\times[0,1]$. The connecting maps of the two ends are therefore conjugate by equivalences homotopic to the identity on $A$ and on the quotient. ∎

---

## 6. Proof of Theorem B

Fix a transverse $B=B_M$ and a framing $f_0$ extending $(u_0,u_1)$. Any other framing is $f_0\cdot h$, where $h$ is a *relative cocycle*: maps $h_{xy}:\overline B(x,y)\to G$ satisfying
* $h_{xy}=h_{x'y}\circ\mathrm{pr}$ on $\overline{\mathcal M}(x,x')\times\overline B(x',y)$;
* $h_{xy}=h_{xy'}\circ\mathrm{pr}$ on $\overline B(x,y')\times\overline{\mathcal M}(y',y)$.

These conditions do not involve the end framings. So the set of homotopy classes of relative cocycles is the same for all end framings, which is why we may compare framings for $X_1$-ends with those for $X_0$-ends.

By Theorem A(4–5), the pieces are compact contractible manifolds with corners of dimensions $0,1,2,3$, each bounded by a sphere, with the incidences of the twisted identity bimodule. We call the 3-dimensional ones balls. Define $\mathbb F_2$-incidence maps:
* $\partial^{\rm pt}$ from the 8 points to the 12 intervals;
* $\partial^{\rm hex}$ from the intervals to the 8 hexagons;
* $\partial^{\rm ball}$ from the hexagons to the 4 balls.

A lower piece $B(p,q)$ is incident to $B(x,y)$ if it is the $B$-factor of a facet $\overline{\mathcal M}(x,p)\times B(p,y)$ or $B(x,q)\times\overline{\mathcal M}(q,y)$.

**6.1 Normalization.**
* *Level 0.* $\pi_0(h)$ is constant on each piece. Coherence on the two endpoints of each interval forces equal values on the two point pieces it joins. Since $\operatorname{rank}\partial^{\rm pt}=7$ (verify.py §6), the graph of points and intervals is connected. So $\pi_0(h)$ is a global sign $\sigma$. The constant cocycle $-1$ is coherent. It amounts to reorienting all objects of $\mathcal C'$, and it changes the realization to $-|B,f|$. So $\Gamma^B_0=\mathbb Z/2$.
* *Level 1.* After multiplying by $\sigma$, $h$ takes values in $G_1$. Homotope it to $1$ on the points, and extend the homotopy over higher pieces by the homotopy extension property of the pairs $(\overline B,\partial\overline B)$. The intervals then carry classes $x\in\pi_1(G)=\mathbb Z/2$. Each hexagon boundary is the concatenation of its faces, on which $h$ is $1$ or an interval value. Since $h$ extends over the hexagon, $\partial^{\rm hex}x=0$. Moving a point value once around a loop changes $x$ by $\partial^{\rm pt}$ of that point. We have $\dim\ker\partial^{\rm hex}=12-5=7=\operatorname{rank}\partial^{\rm pt}$, so $\Gamma^B_1=0$. So we may assume $x=0$ and homotope the intervals to $1$ rel boundary.
* *Level 2.* The hexagons now carry classes $y\in\pi_2(G)=\mathbb Z/2$, and each ball boundary gives $\partial^{\rm ball}y=0$. Moving an interval by a class in $\pi_2$ changes $y$ by $\partial^{\rm hex}$. We have $\dim\ker\partial^{\rm ball}=8-3=5=\operatorname{rank}\partial^{\rm hex}$, so $\Gamma^B_2=0$.
* *Level 3.* After normalization, the four balls carry classes $c_{st}\in\pi_3(G)=\pi_3^s$.

**6.2 Realization.** Apply Lemma 5.3 to each ball, with disjoint discs; a normalized cocycle is homotopic rel boundary to one supported in discs. This gives
$$|B,f_0h|=|B,f_0|+\sum_{s,t}\iota_{Q_1^t}\,c_{st}\,q_{P_4^s}.$$
Now $[X,S^4]\cong\operatorname{Hom}(H_4X,\mathbb Z)$ and $[S^1,X']\cong H_1X'$, because $\pi_{-3}^s=0$. So $q_{P_4^s}=\sigma_sq$ and $\iota_{Q_1^t}=\tau_t\iota$, where $\sigma_s$ is the coefficient of $e_4^s$ in the $H_4$-generator and $\tau_t$ is the image of $e_1^t$ in $H_1$. Hence the formula of B(2) holds with $\delta=\sum\sigma_s\tau_tc_{st}$.

**6.3 Hexagon moves and $\Gamma^B_3$.**
* Rotating a normalized hexagon cocycle once through a class $z\in\pi_3(G)$, viewed as a loop in $\mathrm{Map}((H,\partial H),(G,1))$, is a homotopy of cocycles. Each hexagon is a facet factor of exactly two balls (verify.py §6). Extending the homotopy over these two balls changes their classes by $\pm z$ each. This is the boundary-track formula: $W/\partial W\simeq S^3$, the facet gives $F/\partial F\simeq S^2$, and the track $S^1\wedge F/\partial F\to G$ enters with degree $\pm1$.
* By Lemma 5.4 and 6.2, the move preserves $\delta N$ for any ends. Every framing of $\Sigma_Q(C)$ realizes $S^1\cup_\alpha e^4$ for some $\alpha\in\pi_2^s$: the cellular homology is $\mathbb Z[1]\oplus\mathbb Z[4]$, torsion-free, and the argument of [36, Lemma 4.1] applies. So the ends realize $X_0$ or $X_1$, and $N$ has order 24 or 12 (6.4). In either case $\pm1\pm1\equiv0$ modulo the order of $N$ only if the two terms cancel. This forces the signs of the move vector $(\pm z,\pm z)$, and these signs do not depend on the end framings, because relative cocycles do not see them.
* The move vectors are the edge vectors of the 4-cycle formed by the balls, and they lie in $\ker\delta$. The edge lattice has Smith invariants $(1,1,1,0)$, and together with $e_{(++)}$ it spans $\mathbb Z^4$ (verify.py §6). So the moves generate $\ker\delta$ over $\mathbb Z$, hence over $\mathbb Z/24$.
* Two normalized cocycles with the same $\delta$ are therefore related by moves, and then homotopic rel boundary, since maps $(D^3,\partial)\to(G,1)$ are classified by $\pi_3$.
* Cocycles with different $(\sigma,\delta)$ are not homotopic. For $\delta\not\equiv\delta'\bmod12$, or for different $\sigma$, this holds because their realizations differ for any ends (6.4, Lemma 5.4). For $\delta'=\delta+12$ we use ends realizing $X_0$, which exist by (R3), where $N$ has order 24. (Alternatively, this follows from the identification of coherent cocycles with maps out of the classifying space, $B\Sigma_Q\simeq S^3$ [7]; then $\Gamma^B=[\Sigma S^3_+,BG]_*=\pi_0G\times\pi_3G$. We do not use [7].)

Hence $\Gamma^B=\mathbb Z/2\times\mathbb Z/24$, and every class occurs by Lemma 5.3. This proves B(1)–(2).

**6.4 Injectivity (B3).**

*Ends $X_0$.* Let $r:X_0\to S^1$ be a retraction and $i_4:S^4\to X_0$ a lift of the $H_4$-generator. Then $r\circ N\circ i_4=\nu$, so $N$ has order 24. Two classes $(\sigma,\delta)$ and $(\sigma',\delta')$ give the same map only if $\sigma=\sigma'$, because otherwise the induced maps on $H_*$ differ by $2|B|_*\ne0$; and then only if $\delta=\delta'$. This gives 48 distinct maps.

*Ends $X_1$.* Consider the Puppe sequence $S^3\xrightarrow{\eta^2}S^1\xrightarrow{\iota}X_1\xrightarrow{q}S^4\xrightarrow{\Sigma\eta^2}S^2$.
* The kernel of $\iota_*:\pi_3^s\to[S^4,X_1]$ is the image of $(\eta^2)_*:\pi_1^s\to\pi_3^s$, which is $\{0,\eta^3\}=\{0,12\nu\}$ (Toda [22]).
* The kernel of $q^*:[S^4,X_1]\to[X_1,X_1]$ is the image of $[S^2,X_1]=\{0,\iota\eta\}$ under precomposition with $\Sigma\eta^2$. That image is $\{0,\iota\eta^3\}=0$.

So $N=\iota\nu q$ has order exactly 12 in $[X_1,X_1]$. This means $(\sigma,\delta)$ and $(\sigma,\delta+12)$ give the same map, and no other coincidences occur (verify.py §13). ∎

**6.5 Vector-bundle classes (B4).** Use a cocycle with values in $j(O)$, supported in a disc of one ball and given there by $D^3/\partial D^3=S^3\xrightarrow{L}SO(4)\subset O$, $L(x)=$ left multiplication by $x$. Its class in $\pi_3(G)$ is $J[L]=\nu$, by the Hopf construction [21]. Multiples give every $\delta$, since $J:\pi_3(O)=\mathbb Z\to\pi_3^s$ is onto: the image of $J$ has order $\operatorname{denom}(B_2/4)=24$ [21], verify.py §1.

$SO(3)$-valued cocycles give only even $\delta$, because $\pi_3(SO(3))\to\pi_3(SO)$ has index 2. ∎

**6.6 Realizable self-equivalences (B5).**
* A self-map of $X_0=S^1\vee S^4$ is a matrix $\begin{psmallmatrix}a&\gamma\\0&d\end{psmallmatrix}$ with $a,d\in\mathbb Z$ and $\gamma\in\pi_3^s$; the remaining entry lies in $\pi_{-3}^s=0$. Composition is matrix multiplication. The units have $a,d=\pm1$, so $|\operatorname{Aut}(X_0)|=96$.
* The scalars $(\pm1,\pm1,0)$ together with $(1,1,12)$ form the centre. The quotient by $\langle(-1,-1,0)\rangle$ is $\{(1,d,\gamma)\}=\mathbb Z/24\rtimes\mathbb Z/2$ with $d$ acting by inversion, i.e. $D_{24}$. So $\operatorname{Aut}(X_0)\cong D_{24}\times\mathbb Z/2$; the element orders match (verify.py §7).
* $\chi(a,d,\gamma)=ad$ is a homomorphism (multiply the diagonals), hence conjugation invariant. Its kernel $\operatorname{Aut}^+(X_0)=\{(\sigma,\sigma,\gamma)\}$ has 48 elements; it is abelian, since $(\sigma,\sigma,\gamma)(\sigma',\sigma',\gamma')=(\sigma\sigma',\sigma\sigma',\sigma\gamma'+\sigma'\gamma)$ is symmetric, and $(\sigma,\gamma)\mapsto(\sigma,\sigma\gamma)$ is an isomorphism onto $\mathbb Z/2\times\mathbb Z/24$ (verify.py §14). Changing $\phi$ conjugates the realized maps, so the statements below do not depend on $\phi$.
* *(a).* Let $M\in SL(4)$ be transverse. By Theorem C(1), $B_M$ admits a framing $f_0$ extending $(u,u)$. By (R2) and §3.6, $|B_M,f_0|$ acts on $(H_1,H_4)$ by $\pm(1,\prod\varepsilon)=\pm(1,1)$, because $\prod\varepsilon=\operatorname{sgn}\det M=+1$ (Theorem A(4)). So $|B_M,f_0|=(\sigma_0,\sigma_0,\gamma_0)$ for some $\sigma_0,\gamma_0$, and it is a unit. By B(1)–(2) the spherical framings extending $(u,u)$ realize exactly $\sigma\big((\sigma_0,\sigma_0,\gamma_0)+\delta N\big)$, $\sigma=\pm1$, $\delta\in\mathbb Z/24$, which is all of $\operatorname{Aut}^+(X_0)$, for every value of $\gamma_0$ (verify.py §14). Only (R3) is used. For $M=I$, (R4) gives $|B_{\rm id},f_{\rm can}|=\mathrm{id}$.
* *(b).* By the same computation, every framed $(B_M,f)$ with $M\in SL(4)$ has $\chi=+1$. By Lemma 2.4(1) and (4) the transfers of quadrupole data are exactly the elements of $SL(4)$, so no model continuation bimodule of linear type gives $\chi=-1$.
* *(c).* For $M=R_\varepsilon$ with $\prod\varepsilon=-1$, $B_{R_\varepsilon}$ is transverse ($\Delta_k=\pm1$) and is a flow bimodule by Lemma 2.2 (whose proof uses only that $R_\varepsilon$ is a transverse diffeomorphism), and Theorem C(1) gives a framing extending $(u,u)$. The same computation gives $|B_{R_\varepsilon},f_0|=(\sigma_0,-\sigma_0,\gamma_0)$, and B(2) gives exactly the 48 elements with $\chi=-1$ (verify.py §14). Since $\det R_\varepsilon=\prod\varepsilon_a=-1$, $R_\varepsilon\notin SL(4)$ and no positive multiple of it is in $SL(4)$; and $R_\varepsilon$ reverses the orientation of $S^3$, while the transfer of every continuation datum is isotopic to the identity. So $B_{R_\varepsilon}$ is not a model continuation bimodule. ∎

*Remark 6.1 (non-linear transfers).* For a general continuation datum the transfer $\Psi$ is not linear, and Theorem A does not apply. If $B_\Psi$ is transverse, the classical fact that the Morse continuation map induced by $\Psi$ is $\Psi_*$ on $H_*(S^3)$ (cf. [16]), together with $\Psi\simeq\mathrm{id}$, gives action $\pm(1,1)$ on $(H_1,H_4)$ for every framing, so (b) extends to such $B_\Psi$. We use this only as a remark.

---

## 7. Proof of Theorems C and E

**7.1 Existence (C1).** Choose vector-bundle framings on the $B$-pieces by induction on dimension.
* On a $k$-piece $W$, which is contractible with $\partial W\cong S^{k-1}$, the framing is prescribed on $\partial W$ by the lower pieces and the ends. Relative to a trivialization over $W$, it is a map $F:\partial W\to O$. Since $W$ is contractible, $F$ extends over $W$ if and only if $F$ is null-homotopic, i.e. null in $\pi_{k-1}(O)$.
* For $k=3$ this is automatic, since $\pi_2(O)=0$.
* For $k=1,2$ the obstructions form vectors $o_1\in\mathbb F_2^{12}$ ($\pi_0(O)$, orientations) and $o_2\in\mathbb F_2^8$ ($\pi_1(O)$).
* *Cocycle property.* For a $(k+1)$-piece $V$, consider the framing over $\partial V$ minus the open $k$-faces that are $B$-pieces times points. The boundary loops (for $k=2$), or boundary point pairs (for $k=1$), of the removed faces are null-homologous in that complement. Since $\pi_0(O)$ and $\pi_1(O)=H_1(O)$ are abelian, the sum of the obstructions over the removed faces vanishes. The other faces, products with end pieces, carry framings and contribute $0$. So $\partial^{\rm hex}o_1=0$ and $\partial^{\rm ball}o_2=0$.
* Changing the choices one level down changes $o_1$ by $\operatorname{im}\partial^{\rm pt}$ and $o_2$ by $\operatorname{im}\partial^{\rm hex}$.
* Since $\Gamma^B_1=\Gamma^B_2=0$ (verify.py §6), both obstructions can be killed. ∎

**7.2 The obstruction (C2).**
* Let $f$ be a vector-bundle framing from $(u_0,u_1)$, given by C1. A framing $f'$ from $(u_0g_0,u_1g_1)$ is the same as $f\cdot h$, where $h$ is a family of maps $h_{xy}:\overline B(x,y)\to G$ with $h=h_B\circ\mathrm{pr}\cdot g_0$ on source faces and $h=g_1\cdot h_B\circ\mathrm{pr}$ on target faces.
* Replacing $g_i$ by homotopic cocycles does not affect solvability, by homotopy extension over the pieces.
* By [36, Prop. 3.3] we may take $g_i$ normalized: equal to $1$ on points and intervals, and with classes $c(g_i)_{st}$ on the squares $\overline{\mathcal M}(P_4^s,P_1^t)$. Then $h$ normalizes on points, intervals and hexagons exactly as in 6.1. The face values involving end pieces are $1$ there, and $\Gamma^B_0$ only adjusts a global sign.
* On the ball $\overline B(P_4^s,Q_1^t)$, the boundary class in $\pi_2(G)$ is
$$\sum_{\text{hexagons }H\subset\partial}y_H\ +\ c(g_0)_{st}+c(g_1)_{st}.$$
  The term $c(g_0)_{st}$ comes from the facet $\overline{\mathcal M}(P_4^s,P_1^t)\times B(P_1^t,P_1^t)$, and $c(g_1)_{st}$ from $B(P_4^s,P_4^s)\times\overline{\mathcal M}(P_4^s,P_1^t)$; both relabelled by $R_\varepsilon$ when $M\ne I$, which does not change the sum. The remaining facets are interval × interval and carry $1$.
* An extension exists if and only if this vanishes for all four balls. That is, $c(g_0)+c(g_1)\in\operatorname{im}\partial^{\rm ball}=\{c:\sum c=0\}$ (verify.py §6), i.e. $\sum c(g_0)=\sum c(g_1)$. verify.py §8 checks all 256 cases, with a corrupted-incidence control. ∎

**7.3 Theorem E.**

*E1.* We have $W^s_H(Q_1)=S^3\setminus\{-e\}$ and $W^s_H(Q_4)=\{-e\}$. Transversality of $\Psi^{-1}\widehat W^s_H(Q_4)=\{p^*\}$ with the strata $W^u(P_a)$ means $p^*\notin W^u(P_a)$ for $a\le3$, i.e. $p^*$ is off the equator $S(E_3)$. Since $W^s_H(Q_1)$ is open, the strata meeting it are automatically transverse. So:
* $B(P_a^\sigma,Q_4)=\{p^*\}$ if $(a,\sigma)=(4,s^*)$, and is empty otherwise;
* $\overline B(P_a^\sigma,Q_1)=\widehat W^u(P_a^\sigma)\times_{S^3}\widehat W^s_H(Q_1)$.

$\widehat W^s_H(Q_1)$ is $S^3$ blown up at $-e$, a closed 3-ball whose boundary is $\overline{\mathcal M}_H(Q_4,Q_1)\times\widehat W^s(Q_4)=S^2\times\mathrm{pt}$. So $\overline B(P_a^\sigma,Q_1)$ is $\widehat W^u(P_a^\sigma)$ (a point, interval, square or cube), except for $(4,s^*)$, where it is the cube blown up at $p^*$. The faces are those listed.

The chain map sends $e_1^\pm\mapsto Q_1$ and $e_4^{s^*}\mapsto\pm Q_4$, and kills the rest. It is a chain map, because $g(d\,e_2^\tau)=g(e_1^+)-g(e_1^-)=0$, and it is an isomorphism on $H_1$ and $H_4$ (verify.py §8).

*E2.* Dually, $W^u_H(Q_4)=S^3\setminus\{e\}$ and $W^u_H(Q_1)=\{e\}$. So:
* $B(Q_4,P_4^t)=\{\Psi'^{-1}(P_4^t)\}$, one point for each $t$;
* $B(Q_1,P_b^t)=\{e\}\cap\Psi'^{-1}W^s(P_b^t)$, which is one point for $(b,t)=(1,t^*)$, where $\Psi'(e)\in W^s(P_1^{t^*})$ generically, and empty otherwise.

The composite of the chain maps is $\mathrm{id}$ on $C_*(\Sigma_H)$ (verify.py §8).

*E3.* We have $B(Q_4,Q_4)=\{\Psi^{-1}(-e)\}$ and $B(Q_1,Q_1)=\{e\}$, and $B(Q_1,Q_4)=\emptyset$ if and only if $\Psi(e)\ne-e$, which is transversality. The piece $\overline B(Q_4,Q_1)$ is $S^3$ blown up at $e$ and at $\Psi^{-1}(-e)$, which is $S^2\times[0,1]$, with faces $\mathrm{pt}\times S^2$ and $S^2\times\mathrm{pt}$. A path from $\Psi$ to $\mathrm{id}$ in $\mathrm{Diff}_0(S^3)$ avoiding the codimension-3 condition $\Psi_t(e)=-e$ exists generically. Lemma 2.3 then gives $B_\Psi\cong B_{\rm id}$.

*E4.* This is imported from [1] (2-simplices from one-parameter families of data, and composition by gluing of continuation data).

**7.4 The obstruction for $B_{QH}$ (C3).**
* The pieces are:
  * points $B(P_1^\pm,Q_1)$ and $B(P_4^{s^*},Q_4)$;
  * intervals $B(P_2^\pm,Q_1)$;
  * squares $B(P_3^\pm,Q_1)$;
  * the cube $B(P_4^{-s^*},Q_1)$;
  * the shell $B(P_4^{s^*},Q_1)\cong S^2\times I$.
* *Existence of a vector-bundle framing.* Argue as in 7.1. Each square contains both intervals, and each point bounds both intervals. Each of the cube and the shell contains both squares, so the cocycle property gives $o_+=o_-$ at levels 1 and 2. The shell needs only matching orientations on its two boundary spheres, because $[S^2,SO]=0$; this is arranged by the free sign of $B(P_4^{s^*},Q_4)$.
* *Spherical reframings.* Normalize as in 7.2, with level-1 group $0$ (verify.py §8). Let $y_\pm$ be the square classes.
  * The cube extends if and only if $y_++y_-+c_{-s^*,+}+c_{-s^*,-}=0$.
  * The shell extends if and only if its outer and inner boundary classes agree in $\pi_2(G)$, i.e. $y_++y_-+c_{s^*,+}+c_{s^*,-}=c(h)$, the class of the reframing of $\overline{\mathcal M}_H(Q_4,Q_1)$ [36, Thm. A(4)].
  * Eliminating $y_++y_-$ gives $\sum c=c(h)$ (verify.py §8, all 32 cases).
* C4 follows from C2, C3 and Theorem B(2). ∎

---

## 8. Discussion

**8.1 Rigidity of moduli, flexibility of framings.** Theorem A shows that the unframed model continuation bimodules of the quadrupole sector are completely rigid: a sign vector $\varepsilon$ with $\prod\varepsilon=+1$ determines them. Theorem B shows that all homotopical content beyond homology resides in the framings of the four 3-dimensional pieces, and is exactly $\pi_3^s$.

**8.2 The group is not new: the structured interpretation (remark, not used).** The abstract group $\Gamma^B$ follows from the work of Hedenlund–Oldervoll, as we now recall; our contribution is its explicit realization on the pieces of $B_M$ and its interaction with $\eta^2$, not the group. Compare also the classifying-space description of Morse flow categories [7]. Hedenlund–Oldervoll [2, Ex. 0.0.7, Ex. 2.5.12] show that Morse flow categories on $M$ carry a natural $M$-structure. By their main theorem [2, Thm. 0.0.1], they also show that $\mathrm{Flow}^M$ is equivalent to spectral local systems on $M$, under which the Morse category corresponds to the constant system $\mathbb S$. Its automorphisms are $\pi_0\mathrm{Map}(S^3,GL_1\mathbb S)\cong\{\pm1\}\times\pi_3^s$, which is our $\Gamma^B$. Forgetting the structure sends $\gamma$ to $\mathrm{id}+\gamma N$. In this light, the relative cocycles on the model bimodule are cellular representatives of maps $\Sigma(S^3_+)\to BGL_1\mathbb S$. The same count, $[\Sigma S^3_+,BO]=\mathbb Z\times\mathbb Z/2$, suggests that vector-bundle framings form $\mathbb Z\times\mathbb Z/2$, mapping to realizations by $J$ mod 24. We do not prove this last statement.

**8.3 Relation to math_53 [36].** The category-level exotic class $\eta^2$ lies in $\operatorname{coker}J$ in degree 2. The bimodule-level classes lie in degree 3, where $J$ is onto, so they are all realized by vector bundles. The two interact. A bimodule cannot change $\sum c_Q$ (Theorem C). When both ends realize $X_1$, the bimodule class $12\nu=\eta^3=\eta\cdot\eta^2$ is absorbed by the attaching map (Theorem B(3)). In this sense the bimodule sees $\eta^2$ twice: as an obstruction in $\pi_2$ on the boundaries of the 3-dimensional pieces, and as a kernel $\{0,12\}$ in $\pi_3$.

**8.4 Classical continuation and LOS.** Theorem D(2) is the continuation analogue of a handle slide [12, 14]. A one-parameter family crosses a wall where an index $-1$ continuation trajectory exists, and the chain maps differ by the count of these trajectories as a chain homotopy. Theorem E is a cancellation equivalence in the spirit of LOS [4, 5] and of classical handle cancellation [26]: three pairs cancel through pitchforks (Theorem D(4)). The structural stability used throughout is [23]. We do not use the LOS moves themselves.

**8.5 Status table.**

| statement | status |
|---|---|
| Theorem A (1)–(6) | proved here (model), using (W), [11], [33] |
| Theorem B (1)–(4) | spherical framings up to spherical homotopy; proved here, using (R1)–(R2) and Lemmas 5.1–5.4; stable stems [21, 22]; (R3) only for $\delta\ne\delta+12$ in (1) |
| Theorem B (5) | proved here (model) modulo (R3); (R4) only for $|B_{\rm id},f_{\rm can}|=\mathrm{id}$; the 48 elements with $\chi=-1$ are realized by the non-continuation bimodules $B_{R_\varepsilon}$, $\prod\varepsilon=-1$ |
| Theorem C | proved here, using [36, Prop. 3.3, Thm. A(4)]; C(4) consistent with [36, Thm. A] (bimodule-level proof only) |
| Theorem D (1)–(4) | proved here (model); numerical value of $y_*$ is [N]; Bernoulli linearizes the cubic truncation only |
| Theorem E (1)–(3) | proved here (model); E(4) imported from [1] |
| Lemma 2.6A (confinement) | proved here, given (N1)–(N2); uses [31, Thm. D], [32, Lemmas 4.1–4.2] |
| Proposition 2.6, Corollary 2.8 | proved modulo the imported inputs (N1) [20, 31, 32, 33] and (N2) [17, 18, 19, 45]; index $\le0$ only; forcing path in the normalized slow time $\varsigma=\varepsilon|\kappa|s/\pi$ (Remark 2.6B for the other parametrization) |
| Hypothesis (H$_{\rm HW}$) | not proved; identification of positive-dimensional HW pieces with $B_M$ |
| Corollary 2.7 | conditional on (H$_{\rm HW}$) |

*Not claimed.*
* Hypothesis (H$_{\rm HW}$), i.e. any statement about positive-dimensional HW continuation moduli spaces or framed HW continuation bimodules beyond Corollary 2.8.
* The realization of the 48 elements of $\operatorname{Aut}(X_0)$ with $\chi=-1$ by continuation, or by any symmetry of the HW or KW data.
* Framings of HW continuation moduli from index theory, and their coherence at corners.
* Higher simplices beyond those imported from [1].
* Global (non-local) continuation.
* The classification of vector-bundle framings up to vector-bundle homotopy, e.g. as $\mathbb Z\times\mathbb Z/2$ (§8.2).
* The abstract group $[S^3,GL_1\mathbb S]$ as a new result; it follows from [2] (§8.2).

---

## 9. Verification

verify.py runs 141 checks (9 [K], 85 [C], 31 [I], 16 [N]) with FALLOS = 0. No check is a hard-coded truth value; [K] checks compare encoded data. The output is in verify_output.txt. The sections are:

* §1 stable stems and $|\operatorname{im}J|$;
* §2 the exact linearization, the gnomonic charts and the Riccati form;
* §3 transversality ⇔ minors and the sign patterns, on random exact matrices, with controls;
* §4 cellular chain maps and the wall chain homotopies, by exhaustive search;
* §5 the polytopes;
* §6 the obstruction groups over $\mathbb F_2$ and $\mathbb Z$;
* §7 $\operatorname{Aut}(X_0)$;
* §8 the obstruction criteria and the $\Sigma_Q\leftrightarrow\Sigma_H$ chain maps;
* §9 the rotation wall (symbolic, with [N] root and ODE checks);
* §10 the pitchfork family;
* §11 monodromy;
* §12–13 the maps $N$ and the $X_1$ phenomenon;
* §14 the determinant obstruction: the Liouville identity $\operatorname{tr}(\operatorname{adj}(U)(-CU))=-\operatorname{tr}(C)\det U$ (so $\det M=1$), $\det R_\varepsilon=\prod\varepsilon_a$, $\prod\varepsilon=+1$ on random transverse elements of $SL(4,\mathbb Z)$, invariance of the sign of $\det$ under scalars, the framing-sign statements of §3.6, and the count: model continuation realizes exactly the 48 elements of $\operatorname{Aut}^+(X_0)$ and none of the other 48;
* §15 the time normalization: $\kappa=\pi\cdot(-5/216)$; the chain rule giving the factor $1/\pi$ for $\varsigma=\varepsilon|\kappa|s$ and the factor $1$ for $\varsigma=\varepsilon|\kappa|s/\pi$; the rotating example of Remark 4.1 both ways (closed formula and ODE, sign patterns, both walls, cellular maps); the Bernoulli control with a quintic term; and the constants of Lemma 2.6A (normal block, eigenvalues $\pm\sqrt{10|\bar\nu|/3}$, $\dot\theta=0$, the two quadratic-form estimates).

verify.mpl mirrors §§2–4, 6, 7, 9, 10, 13 and 14 (39 checks). It was run in Maple: 39 checks, FALLOS = 0 (output in verify_mpl_output.txt).

---

## References

1. M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: Flow categories*, arXiv:2404.03193.
2. A. Hedenlund, T. P. Oldervoll, *Structured flow categories and twisted presheaves*, arXiv:2603.29576.
3. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042.
4. A. Lobb, P. Orson, D. Schütz, *A calculus for flow categories*, arXiv:1710.01857.
5. A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500.
6. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.
7. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Morse theory and classifying spaces*, preprint, 1995.
8. D. Burghelea, L. Friedlander, T. Kappeler, *On the space of trajectories of a generic gradient like vector field*, An. Univ. Vest Timiş. Ser. Mat.-Inform. 48 (2010); arXiv:1101.0778.
9. K. Wehrheim, *Smooth structures on Morse trajectory spaces, featuring finite ends and associative gluing*, Geom. Topol. Monogr. 18 (2012); arXiv:1205.0713.
10. C. M. Bonciocat, *Revisiting the Cohen–Jones–Segal construction in Morse–Bott theory*, arXiv:2409.11278.
11. D. Joyce, *On manifolds with corners*, in: Advances in Geometric Analysis, Adv. Lect. Math. 21, International Press, 2012, 225–258; arXiv:0910.3518.
12. J. Cerf, *La stratification naturelle des espaces de fonctions différentiables réelles et le théorème de la pseudo-isotopie*, Publ. Math. IHÉS 39 (1970), 5–173.
13. R. L. Cohen, *Floer homotopy theory, revisited*, arXiv:1901.08694.
14. A. Floer, *Witten's complex and infinite-dimensional Morse theory*, J. Differential Geom. 30 (1989), 207–221.
15. D. Salamon, *Morse theory, the Conley index and Floer homology*, Bull. London Math. Soc. 22 (1990), 113–140.
16. M. Schwarz, *Morse Homology*, Progr. Math. 111, Birkhäuser, 1993.
17. N. Fenichel, *Persistence and smoothness of invariant manifolds for flows*, Indiana Univ. Math. J. 21 (1971), 193–226.
18. M. W. Hirsch, C. C. Pugh, M. Shub, *Invariant Manifolds*, Lecture Notes in Math. 583, Springer, 1977.
19. P. W. Bates, K. Lu, C. Zeng, *Existence and persistence of invariant manifolds for semiflows in Banach space*, Mem. Amer. Math. Soc. 135 (1998), no. 645.
20. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Springer/EDP Sciences, 2011.
21. J. F. Adams, *On the groups $J(X)$ IV*, Topology 5 (1966), 21–71.
22. H. Toda, *Composition Methods in Homotopy Groups of Spheres*, Ann. of Math. Stud. 49, Princeton Univ. Press, 1962.
23. J. Palis, W. de Melo, *Geometric Theory of Dynamical Systems*, Springer, 1982.
24. M. Golubitsky, D. G. Schaeffer, *Singularities and Groups in Bifurcation Theory I*, Appl. Math. Sci. 51, Springer, 1985.
25. J. von Neumann, E. Wigner, *Über das Verhalten von Eigenwerten bei adiabatischen Prozessen*, Phys. Z. 30 (1929), 467–470.
26. J. Milnor, *Lectures on the h-cobordism theorem*, Princeton Univ. Press, 1965.
27. M. Audin, M. Damian, *Morse Theory and Floer Homology*, Universitext, Springer, 2014.
28. K. J. Palmer, *Exponential dichotomies and transversal homoclinic points*, J. Differential Equations 55 (1984), 225–256.
29. J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.
30. rStation math_30, https://rstation.ai/problems/math/papers/30/v1
31. rStation math_31, https://rstation.ai/problems/math/papers/31/v1
32. rStation math_32, https://rstation.ai/problems/math/papers/32/v1
33. rStation math_33, https://rstation.ai/problems/math/papers/33/v1
34. rStation math_34, https://rstation.ai/problems/math/papers/34/v1
35. rStation math_52, https://rstation.ai/problems/math/papers/52/v1
36. rStation math_53, https://rstation.ai/problems/math/papers/53/v1
37. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207.
38. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
39. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.
40. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.
41. rStation math_46, https://rstation.ai/problems/math/papers/46/v1
42. rStation math_49, https://rstation.ai/problems/math/papers/49/v1
43. G. H. Golub, C. F. Van Loan, *Matrix Computations*, Johns Hopkins Univ. Press.
44. J. J. Duistermaat, J. A. C. Kolk, V. S. Varadarajan, *Functions, flows and oscillatory integrals on flag manifolds and conjugacy classes in real semisimple Lie groups*, Compositio Math. 49 (1983).
45. J. Eldering, *Normally Hyperbolic Invariant Manifolds: The Noncompact Case*, Atlantis Series in Dynamical Systems 2, Atlantis Press, 2013.

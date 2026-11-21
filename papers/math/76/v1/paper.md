# Maslov data for the Seidel–Smith pair of $T(3,4)$: spherical twists beyond brane structures
Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**
Blakey–Bonciocat parameterize Lagrangian Floer homotopy types over the space $\mathrm{Mas}$ of Maslov data. Changes of Maslov data form a torsor over $[P(L,L'),BGL_1\mathbb S]$, which contains the brane changes. We study this enlargement for the three-strand Seidel–Smith pair $(L,L'=(\beta\times1)L)$ of $T(3,4)$ in $\mathcal Y_3$, $L\cong(S^2)^3$.
(A) Using that $\mathcal Y_3$ retracts onto the $(3,3)$ Springer fibre, we compute: the path space $P$ is simply connected, $\pi_3(\mathcal Y_3)\cong\mathbb Z^6$, $\pi_2(P)\cong\mathbb Z^2$, and $H^2(P;\mathbb F_2)=\mathbb F_2u\oplus\mathbb F_2\ell$. All six brane classes map to $u$.
(B) Brane, spherical-brane, polarization and transgressed changes all have $w_2\in\mathbb F_2u$. The loop class $\ell$ is reached by line bundles on $P$, but by none of these.
(C) Hence the six boundary-incidence operators of a companion preprint coincide on Floer cohomology. Its parity rule then needs no module hypothesis. For arbitrary Maslov data, $\mathrm{Sq}^2$ moves by $\rho\,\mu(u)+\sigma\,\mu(\ell)$.
(D) Changes with $w_2=0$ leave every primary operation in the window unchanged. They can only add $\eta^2$-attachments from degree $-7$ to $-10$, governed by a class $e_3\in H^3(P;\mathbb F_2)$. It vanishes on vector-bundle changes and on all transgressions. Whether any change has $e_3\ne0$ is open.
(E) The Lipshitz–Sarkar spectrum has exactly three $\eta^2$-twins of this kind. They share cohomology, the Steenrod module and $KU$-data, and $KO_{-8}$ separates them. All twins mix quantum gradings, so a charge splitting excludes them. Under the companion's hypotheses, if some brane pair has the Steenrod module of the Khovanov spectrum, a charge splitting at the canonical datum forces the canonical $\mathrm{Sq}^2$ to be the Lipshitz–Sarkar table.
(F) For plumbings along spheres the analogue is essentially due to Porcelli–Smith and Blakey–Bonciocat.
No holomorphic strip is computed. verify.py: 109 checks, FALLOS = 0.

## 1. Introduction

### 1.1 Motivation

This paper belongs to a series organized around the following conjecture. It is stated as motivation only; **nothing here proves it or any part of it.**

> **Program conjecture.** For a knot $K$ and each charge $n$, $\ \mathfrak F_{\rm HW}(K)_n\simeq\mathfrak F(L_\ell,L_r)_n\simeq\mathcal X^n_{\rm Kh}(K)$.

Here $\mathfrak F_{\rm HW}$ is a Haydys–Witten Floer homotopy type in instanton sector $n$, $\mathfrak F(L_\ell,L_r)$ is the Lagrangian Floer homotopy type of Witten's pair in the adiabatic Seidel–Smith/Manolescu model [3, 4, 5], and $\mathcal X^n_{\rm Kh}$ is the Lipshitz–Sarkar spectrum [8]. The Lagrangian side is singly graded. One compares it with the collapsed spectrum $Z=\bigvee_q\Sigma^{-q}\mathcal X^q_{\rm Kh}$, graded by $k=h-q$. For $T(3,4)$ the first datum beyond homology is $\mathrm{Sq}^2:H^{-9}(Z;\mathbb F_2)\to H^{-7}$, of rank one (rStation math_55 [R3], Theorem A(4)).

A Floer homotopy type is not defined by the Lagrangians alone; it needs tangential data. A companion paper [companion] (rStation math_75) studies the *brane* data: null-homotopies of the stable Gauss maps of $L$ and $L'$, a torsor over $KO^0(L)\times KO^0(L')$ [R3, Prop. G]. We recall from it, without reproving anything:

* **(companion, Thm. A)** a boundary-incidence formula $\mathrm{Sq}^2_{f^Z}=\mathrm{Sq}^2_f+\mu([Z])$ for path-decorated framed flow categories;
* **(companion, Thms. B–C)** under its hypotheses (FFC), (BT), a brane change $\kappa$ changes $\mathrm{Sq}^2$ by $\mu(w_2\kappa)$, where $\mu:H^2(L;\mathbb F_2)\to\operatorname{End}^{+2}$ is the boundary-incidence action. Under the further hypothesis (Mod$_2$) that each $\mu(a_i)$ equals the Khovanov basepoint operator $X$, the square depends on the brane pair only through one parity $\rho=\sum\epsilon_i+\sum\epsilon'_j$, and the two parity classes cannot both have the Steenrod module of $Z$. We write $S_0=\mathrm{Sq}^2_{\rm LS}$ and $S_1=S_0+X$ for the *tables* in the basis of the identification (H$_2$) below;
* **(companion, Thms. F–G)** a canonical brane pair from the real structure of the $A_5$ surface, natural in reduced $KO^0$. If some brane pair has the Steenrod module of $Z$, whether the canonical class has it reduces to one undecided Floer bit. Only under an additional *marked comparison* hypothesis does this become the literal dichotomy of tables $S_{\rm can}\in\{S_0,S_1\}$.

We keep three notions apart, as the companion does: *equality of tables* in the basis of (H$_2$); *agreement of Steenrod modules*, a graded isomorphism of $\mathbb F_2$-cohomologies intertwining $\mathrm{Sq}^1,\mathrm{Sq}^2$; and *equivalence of spectra*. Equivalence of spectra implies agreement of Steenrod modules, and so does equality of tables when (H$_2$) respects $\mathrm{Sq}^1$; no other implication holds in general. Theorem E(2) below gives spectra that agree at the module level but are not equivalent.

Blakey and Bonciocat [BB] showed that brane data are a special case of a larger structure. **Maslov data** for $(L_0,L_1)$ are null-homotopies $\theta$ of the composite
$$P(L_0,L_1)\to U/O\xrightarrow{\ \sim\ }B(\Omega^\infty KO)\to B^2O\xrightarrow{B^2J}B^2GL_1\mathbb S \qquad\text{[BB, (1.8)]},$$
and the Floer homotopy type is an $\infty$-functor on the space $\mathrm{Mas}$ of Maslov data [BB, Def. 4.10, Cor. 4.12]. Polarizations with brane structures give Maslov data, but not conversely [BB, Rem. 1.2]. For plumbings, [BB, Lemma 4.3] maps $\mathrm{Map}_*(C,BGL_1\mathbb S)$ to $\mathrm{Mas}_\theta$ through $P(L_0,L_1)\to\Omega\Sigma C$. By [BB, Prop. 4.13] the Floer module at $\Phi$ is the Thom spectrum $C^\Phi\wedge R^{\rm sfr}$. [BB, Rem. 4.5] notes that stable spherical fibrations are more natural here than vector bundles, because the result would otherwise hinge on $J$.

**Question.** For the Seidel–Smith pair of $T(3,4)$:
* (a) what is $\pi_0\mathrm{Mas}$ in the range that can affect the window $k\in\{-10,\dots,-7\}$, and which part comes from branes?
* (b) what do the genuinely spherical changes do to $\mathrm{Sq}^2$ and to the spectrum?
* (c) does this enlarge the set of Floer spectra with the homology of $Z$, and what residual ambiguity remains?
* (d) what is the general picture for plumbings?

### 1.2 Results

Throughout, $L=\Sigma_{\alpha_1}\times\Sigma_{\alpha_2}\times\Sigma_{\alpha_3}$ with $\alpha_i=[2i-2,2i-1]$ and $L'=\Sigma_{\beta_1}\times\Sigma_{\beta_2}\times\Sigma_{\beta_3}$ are the product models of [5], [R3, §4]. They live in the $A_5$ surface $S=\{x^2+y^2+\prod_{k=0}^5(z-k)=0\}$ and in $\mathcal Y_3$. From [R3, Table 1], the curves $\beta_j$ join $p_0p_3$, $p_1p_4$ and $p_2p_5$. Write $P=P(L,L')$, $a_i\in H^2(L;\mathbb F_2)$ and $a'_j\in H^2(L';\mathbb F_2)$ for the classes dual to the factors, and $c$ for the number of components of the closure.

**Theorem A (topology of $\mathcal Y_3$ and of the path space).** Assume the cited topological input (T) of §2.1.
1. $\mathcal Y_3$ is simply connected. Its integral cohomology is free, of ranks $1,5,9,5$, and it injects into $\bigoplus_bH^*(L_b)$ over the five crossingless products $L_b$. The relations $R_{\mathbb Z}=\ker(\operatorname{Sym}^2H^2\to H^4)$ are free of rank $6$, spanned by $x_0^2,\dots,x_4^2$ and $e_2(x_0,\dots,x_4)$. All $x_k^2$ vanish, $\mathrm{Sq}^2=0$ on $H^4(\mathcal Y_3;\mathbb F_2)$, $\pi_3(\mathcal Y_3)\cong\operatorname{Hom}(R_{\mathbb Z},\mathbb Z)\cong\mathbb Z^6$, and $\pi_4(\mathcal Y_3)\otimes\mathbb Q=0$.
2. $P$ is connected and $\pi_1(P)\cong\mathbb Z^{c-1}$, for every pairing of the six punctures. For $T(3,4)$, $c=1$ and $P$ is simply connected.
3. The image of $H^2(L;\mathbb F_2)\oplus H^2(L';\mathbb F_2)$ in $H^2(P;\mathbb F_2)$ has dimension $c$. It is spanned by *component classes*: $a_i\mapsto u_{K(\alpha_i)}$ and $a'_j\mapsto u_{K(\beta_j)}$. For $T(3,4)$ all six classes map to one class $u\ne0$.
4. $\pi_2(P)\cong\mathbb Z^c\oplus C_3$, with $C_3=\operatorname{coker}(\pi_3L\oplus\pi_3L'\to\pi_3\mathcal Y_3)\cong\mathbb Z^c$ for all $15$ pairings. For $T(3,4)$, $\pi_2(P)\cong\mathbb Z^2$ and $H^2(P;\mathbb F_2)=\mathbb F_2u\oplus\mathbb F_2\ell$. The *loop class* $\ell$ vanishes on the cycle class and is nonzero on $C_3$. Moreover $H_3(P;\mathbb Q)=0$.
5. Relative classes. Put $K_{2j}=\ker(H^{2j}(\mathcal Y_3)\to H^{2j}(L)\oplus H^{2j}(L'))$ and $Q_{2j}$ for the cokernel. Over $\mathbb F_2$, $\dim K_2=c-1$ (so $K_2=0$ for $T(3,4)$). $Q_2\cong\mathbb Z$, $Q_4=0$, and $K_4$ is $3$-dimensional and spanned by products $yy'$ with $y|_L=0$ and $y'|_{L'}=0$.

**Theorem B (Maslov data at the level of $\mathrm{Sq}^2$).** Maslov data exist for $(L,L')$ (Proposition 3.1, which uses the companion's Theorem F). So $\pi_0\mathrm{Mas}$ is a torsor over $G=[P,BGL_1\mathbb S]$. For $T(3,4)$:
1. $(w_1,w_2):G\to H^1(P;\mathbb F_2)\oplus H^2(P;\mathbb F_2)=0\oplus\mathbb F_2^2$ is onto. It is already onto on the vector-bundle changes $V=J[P,BO]$, since $u$ and $\ell$ are $w_2$ of realified line bundles.
2. *Branes.* A brane pair $(\kappa,\kappa')$ gives $w_2=\rho\,u$ with $\rho=\sum_i\epsilon_i+\sum_j\epsilon'_j$. *Spherical branes* (maps $L,L'\to BGL_1\mathbb S$) give the same subgroup, since $J$ maps $\widetilde{KO}{}^0(L)$ onto $[L,BGL_1\mathbb S]$.
3. *Polarizations.* If a second stable polarization $\Lambda+\lambda$ of $\mathcal Y_3$ admits brane structures on $L$ and $L'$, then $\lambda\simeq0$. So polarization-and-brane data reach only the brane orbit.
4. *Transgressions.* Every change obtained by transgressing a map $(\mathcal Y_3;L\sqcup L')\to(B^2GL_1\mathbb S,*)$ has $w_2\in\mathbb F_2u$. This is the mechanism of [BB, Lemma 4.3].

So $\ell$ is reached by vector-bundle changes on $P$, and by none of the geometric constructions in 2–4.

**Theorem C (Floer basepoint independence).** Assume (FFC) of §1.3. On $H^*(\mathcal C_F;\mathbb F_2)=HF^*(L,L';\mathbb F_2)$, the six boundary-incidence operators of the companion preprint agree for arcs in the same component:
$$\mu(a_i)=\mu'(a'_j)=\mu_P(u_K)\qquad(\alpha_i,\beta_j\subset K).$$
For $T(3,4)$ all six agree. Consequently:
1. under (FFC) and (BT), $\mathrm{Sq}^2_{(b+\kappa,b'+\kappa')}=\mathrm{Sq}^2_{(b,b')}+\rho\,\mu_P(u)$, with no module hypothesis and without (H$_2$);
2. under (BB), for every $h\in G$, $\mathrm{Sq}^2_{\theta+h}=\mathrm{Sq}^2_\theta+\mu_P(w_2h)=\mathrm{Sq}^2_\theta+\rho(h)\mu_P(u)+\sigma(h)\mu_P(\ell)$;
3. the companion's (Mod$_2$) is equivalent to the single statement (Mod$_2^-$): $\mu_P(u)=X$.

**Theorem D (the degree-three level).** Assume (BB). Let $E:\mathbf E\to P$ be the edge complex of the Floer category in degrees $-10,\dots,-7$ (§5.1). It is a $3$-dimensional complex.
1. The effect of $h\in G$ on the window is determined by $(E^*w_2h,E^*e_3h)$. Here $e_3\in H^3(BSGL_1\mathbb S;\mathbb F_2)$ is the class normalized to vanish on $BSO$; it detects $\eta^2\in\pi_3BSGL_1\mathbb S$. If both pulled-back classes vanish, nothing changes.
2. If $w_2h=0$, then $\mathrm{Sq}^1$, $\mathrm{Sq}^2$ and $\mathrm{Sq}^3=\mathrm{Sq}^1\mathrm{Sq}^2$ are unchanged in the window, and so are the boundary maps of the $KU$-sequences. The attaching maps of the degree $-7$ cells onto the degree $-10$ cells change by $\eta^2\,N_h$, where $N_h$ is the cellular cochain of $E^*e_3h$. Modulo coboundaries this is the only change.
3. $e_3:G\to H^3(P;\mathbb F_2)=\operatorname{Hom}(H_3P,\mathbb F_2)$ is a homomorphism, and $H_3(P)$ is finite. It vanishes on $V$ and, for $T(3,4)$, on all transgressions.

So for $T(3,4)$ every change we can construct has $e_3=0$, and no genuinely spherical change is exhibited. Whether $e_3(G)\ne0$ is **open**.

**Theorem E (spherical twins of the Lipshitz–Sarkar spectrum; unconditional).** Let $Z_E$ be $Z$ with $\eta^2$-attachments $E\in M_{2\times3}(\mathbb F_2)$ from the $k=-7$ classes $(0,7),(2,9),(4,11)$ to the $k=-10$ classes $(3,13),(5,15)$.
1. $Z_E\simeq Z_{E'}$ iff the $2\times2$ sphere blocks have the same rank. The column of the Moore cell $(4,11)$ is absorbed. So there are exactly three types $Z=Z^{(0)},Z^{(1)},Z^{(2)}$.
2. All three have the same integral cohomology, the same module over the Steenrod algebra, and the same $KU$-boundary maps. $KO_{-8}$ separates them: the extra summand is $(\mathbb Z/2)^{2-r}$.
3. Every twin with $r\ge1$ mixes quantum gradings. No $Z^{(r)}$ with $r\ge1$ is a wedge $\bigvee_nF_n$ with $H^*(F_n;\mathbb Z)\cong\mathrm{Kh}^{*,n}$. No $\mathrm{Sq}^2$ table of the form $S_0+X$ is $q$-homogeneous.
4. *(Conditional.)* Assume (FFC), (BT), (H$_2$), (Mod$_2^-$) and the companion's ambient hypothesis (Amb). Assume that for some brane pair the Floer spectrum has the Steenrod module of $Z$ (for instance, the program conjecture holds for that pair); this is the setting of the companion's Theorem G(4), in its invariant form. Assume also (Ch) at the canonical datum, compatibly with (H$_2$). Then the canonical class is the one with the Steenrod module of $Z$, and $S_{\rm can}=S_0$ as tables in the basis of (H$_2$). No marked comparison is needed: the charge splitting supplies the marking.

**Proposition F (plumbings along spheres; known in substance).** For a plumbing along $C=S^k$, $k\ge2$, the Maslov datum $\Psi(\alpha)$ of [BB, Lemma 4.3], $\alpha\in\pi_{k-1}^s$, has Floer module $M_\alpha=\operatorname{cofib}(\alpha:\Sigma^{k-1}R^{\rm sfr}\to R^{\rm sfr})$ [BB, Prop. 4.13]. We add:
* $M_\alpha\simeq M_\beta$ iff $\alpha=\pm\beta$;
* $M_\alpha$ is the module of a datum in the image of [BB, Cor. 4.4] iff $\alpha\in\pm\operatorname{im}J$.

The realization of all of $\pi_{d-1}\mathbb S$ by such structures is essentially [14, Ex. 2.27] for zero sections. The contrast with Theorem D(3) is that $H^4$ of the cone of $L_0\vee L_1\to M$ is indecomposable for plumbings ($\Sigma S^3$), whereas $K_4$ consists of products for $T(3,4)$.

### 1.3 Hypotheses and status

Unconditional: Theorem A (given (T)), Theorem B(1)–(4), Theorem D(1),(3) as statements about classes, Theorem E(1)–(3), and Proposition F (given [BB]). The remaining statements use some of the following hypotheses. None is proved here.
* **(T)** (cited topology, §2.1) The topological input on $\mathcal Y_3$ and the Springer fibre.
* **(FFC)** (as in [R3, §1.3] and the companion) A framed flow category $\mathcal C_F$ for $(L,L')$ whose moduli spaces are compactified strip spaces. It carries the *strip decoration* $\tilde E(u,t)=u(\sigma(t),\cdot)\in P$, extended to broken strips by concatenation of Moore paths. Composing with $\mathrm{ev}_0$ gives the companion's boundary decoration $E(u,t)=u(\sigma(t),0)$.
* **(BT)** (companion) A brane change $\kappa$ acts on frames through $E^*\kappa$.
* **(BB)** The Blakey–Bonciocat construction [BB, Prop. 3.3, Def. 3.4] applies to $(\mathcal Y_3;L,L')$. It produces (FFC) with an $\mathbb S$-orientation induced by $\theta$ along $\mathcal M(x,y)\to\Omega_{x,y}P$ [BB, (3.17)–(3.19)]. A change $\theta\mapsto\theta+h$ changes the orientation of $\mathcal M(x,y)$ by the pullback of $\Omega h$. We use the CJS–Cohen realization $|\mathcal C_\theta|$ of the $\mathbb S$-oriented category. *Status:* the inputs of [BB, Assumption 1] hold by Proposition 3.1. What remains is the applicability of [BB] and its foundations [Lar21, Bon25] to $\mathcal Y_3$.
* **(H$_2$)** $HF^k(L,L';\mathbb F_2)\cong\bigoplus_{h-q=k}\mathrm{Kh}^{h,q}(T(3,4);\mathbb F_2)$ [R3].
* **(Mod$_2^-$)** Under (H$_2$), $\mu_P(u)=X$.
* **(Ch)** (charge splitting at a datum) $|\mathcal C_\theta|\simeq\bigvee_n F_n$, with $H^*(F_n;\mathbb Z)\cong\bigoplus_h\mathrm{Kh}^{h,n}(\mathbb Z)$ compatibly with (H$_2$).

## 2. Topology of $\mathcal Y_3$ and of the path space (Theorem A)

### 2.1 Input (T)

* **(T1)** $\mathcal Y_m$ is diffeomorphic to the fibre over $0$ of the simultaneous resolution of the slice. That fibre deformation retracts onto its compact core, the Springer fibre $\mathcal B_{m,m}$ of a nilpotent of Jordan type $(m,m)$ (Seidel–Smith [4, proof of Lemma 45], citing Slodowy [24]).
* **(T2)** $H_*(\mathcal B_{m,m};\mathbb Z)$ is free and even, with $\operatorname{rk}H^{2k}=\binom{2m}k-\binom{2m}{k-1}$ for $k\le m$ (Spaltenstein [25]; Khovanov [21]). $H^*(\mathcal B_{m,m};\mathbb Z)$ is generated by $H^2$ (De Concini–Procesi [22]; Khovanov [21]).
* **(T3)** $\mathcal B_{m,m}$ is homeomorphic to Khovanov's space $\mathcal S_m=\bigcup_a\mathcal S_a\subset(S^2)^{2m}$, with $\mathcal S_a=\{x_j=-x_i\ \text{for arcs }(i,j)\in a\}\cong(S^2)^m$ (Wehrli [23]; conjectured in [21]).
* **(T4)** $\mathcal Y_m$ is an affine variety and a regular fibre of a holomorphic map between affine spaces [4, §5(C)]. The products $L_b$ of matching spheres, for crossingless $b$ and for braid images, lie in $\mathcal Y_m$ [5, Thms. 1.2–1.3].

We use (T1)–(T3) only for $m=3$ and $m\le2$ (controls), and only through: $\pi_1=0$, the Betti numbers, freeness, and generation in degree $2$. verify.py §5 checks that these are consistent with our computations: the restriction ranks are $9$ and $5$.

### 2.2 $\pi_1$, $H_2$ and the cohomology ring

**Simple connectivity.** Every arc of a crossingless matching joins points of opposite parity, so the point $(p,-p,p,-p,p,-p)$ lies in every $\mathcal S_a$. Order the components and put $X_k=\mathcal S_1\cup\dots\cup\mathcal S_k$. Then $X_k\cap\mathcal S_{k+1}$ is a union of the connected sets $\mathcal S_a\cap\mathcal S_{k+1}\cong(S^2)^{\#\text{cycles}}$, all containing that point, so it is connected. Triangulate compatibly (semi-algebraic sets). Van Kampen for subcomplexes gives $\pi_1(X_{k+1})=\pi_1(X_k)*_{\pi_1(X_k\cap\mathcal S_{k+1})}1=1$ by induction. With (T1) and (T3), $\pi_1(\mathcal Y_m)=1$.

**$H_2$.** Manolescu's inclusion $\mathcal Y_m\subset\mathrm{Hilb}^m S$ [5], the Hilbert–Chow map and the Dold–Thom map $\mathrm{Sym}^mS\to SP^\infty S\to K(H_2S,2)$ give
$$\psi:\mathcal Y_m\to K(H_2(S),2),\qquad H_2(S)=\{v\in\mathbb Z^{2m}:\textstyle\sum v_k=0\}.$$
On a product $\Sigma_{\gamma_1}\times\dots\times\Sigma_{\gamma_m}$ in the distinct-$z$ region, $\psi^*$ of a class is the sum of its pullbacks to the factors. A matching sphere over a curve $\gamma$ from $p_i$ to $p_j$ has class $\pm(e_i-e_j)$, whatever the curve. Identify the sphere over $[k,k+1]$ with $e_k-e_{k+1}$. By Picard–Lefschetz, the half twist of $p_k,p_{k+1}$ acts on $H_2(S)$ by the reflection in that class, i.e. by the transposition of $e_k,e_{k+1}$ [28]. Every embedded curve between punctures is the image of a segment $[k,k+1]$ under a braid, so its sphere has class $\pm(e_{\pi(k)}-e_{\pi(k+1)})$. The spheres over consecutive arcs, times far-away points, lie in $\mathcal Y_m$ and map to a basis (verify.py §3). So $\psi_*:H_2(\mathcal Y_m)\to H_2(S)$ is onto. By (T2) both groups are free of rank $2m-1$, so $\psi_*$ is an isomorphism. Put $x_k=\psi^*(e_k^*)$; then $\sum x_k=0$. On a product over arcs $(i_t,j_t)$, $x_k$ restricts to $\pm a_t$ if $k\in\{i_t,j_t\}$, with opposite signs at the two ends.

**The ring in degrees $\le6$.** $H^4$ is spanned by products (T2). The map $\operatorname{Sym}^2H^2\to\bigoplus_bH^4(L_b)$ over the five crossingless $b$ has rank $9=\operatorname{rk}H^4$ (verify.py §5). Since $H^4$ is torsion-free, $H^4(\mathcal Y_3;\mathbb Z)\to\bigoplus_bH^4(L_b;\mathbb Z)$ is injective. Hence $R_{\mathbb Z}$ is the kernel of the composite. It is spanned by $x_0^2,\dots,x_4^2$ and $e_2(x_0,\dots,x_4)$, a saturated lattice that contains $x_5^2$. In degree $6$ the restriction has rank $5=\operatorname{rk}H^6$, again consistent with (T2). Since $x_k^2=0$, $\mathrm{Sq}^2(x_kx_l)=x_k^2x_l+x_kx_l^2=0$, so $\mathrm{Sq}^2=0$ on $H^4(\mathcal Y_3;\mathbb F_2)$ (checked on all components). The same routine gives rank $2$ for $m=2$, as (T2) requires.

**$\pi_3$.** $\mathcal Y_3$ is simply connected with $H_3=0$. Whitehead's exact sequence [26] gives $H_4\xrightarrow b\Gamma(H_2)\to\pi_3\to0$. For free $H_2$, $\Gamma(H_2)^*$ is the group of integral quadratic forms $\operatorname{Sym}^2H^2$, and $b$ is dual to the cup square. (Checks: $x_1x_2$ pairs to $1$ with $[e_1,e_2]$, the top cell of $S^2\times S^2$; $x^2$ pairs to $1$ with $\gamma(e)$, the top cell of $\mathbb{CP}^2$.) The cup square is onto $H^4$ (T2), so
$$\pi_3(\mathcal Y_3)\cong\Gamma(H_2)/b(H_4)\cong\operatorname{Hom}(R_{\mathbb Z},\mathbb Z)\cong\mathbb Z^6,$$
and the Hopf map on a sphere of class $e$ is $q\mapsto q(e)$.

**Rational $\pi_4$.** In the minimal model, $V^2=H^2$ and $V^3=R^*$ with $d=R$. The map $V^2\otimes V^3\to\operatorname{Sym}^3V^2$ is injective (rank $30$), so $H^5(\Lambda V^{\le3})=0$. As $H^5(\mathcal Y_3)=0$, this forces $V^4=0$, i.e. $\pi_4(\mathcal Y_3)\otimes\mathbb Q=0$. Also $\operatorname{Sym}^3/RV^2$ has dimension $5=b_6$ (verify.py §7).

### 2.3 The path space

$P$ is the homotopy fibre product of $L\to\mathcal Y_3\leftarrow L'$. It fibres over $L\times L'$ with fibre $\Omega\mathcal Y_3$, which is connected. The boundary map $\partial:\pi_k(L\times L')\to\pi_k(\mathcal Y_3)$ is $(f,f')\mapsto i_*f-i'_*f'$.

*Proof of A(2).* $\pi_1(L\times L')=0$, so $\pi_1P=\operatorname{coker}(\partial_2)$. In $H_2(S)$ the image of $\partial_2$ is spanned by the six edge vectors $e_p-e_q$ of the graph formed by the $\alpha$- and $\beta$-arcs. Each component of the closure is one cycle of that graph, so the image is $\{v:\sum_{k\in K}v_k=0\ \forall K\}$ and the cokernel is $\mathbb Z^{c-1}$. This is checked by Smith forms for all $15$ pairings, of which $8$ are knots, $6$ are $2$-component links and $1$ is the unlink. $\square$

*Proof of A(3).* In the Serre spectral sequence of $\Omega\mathcal Y_3\to P\to L\times L'$, the base is simply connected and $E_2^{0,1}=H^1(\Omega\mathcal Y_3;\mathbb F_2)=\operatorname{Hom}(\pi_2\mathcal Y_3,\mathbb F_2)=H^2(\mathcal Y_3;\mathbb F_2)$. The transgression $d_2$ is dual to $\partial_2$: $x\mapsto(i^*x,i'^*x)$, with $x_k\mapsto(a_{t(k)},a'_{t'(k)})$. So the edge map $H^2(L\times L')\to H^2(P)$ has kernel $\operatorname{im}d_2$ and image of dimension $6-\operatorname{rk}d_2=c$. If $\alpha_i$ and $\beta_j$ share the puncture $p_k$, then $a_i-a'_j=d_2(x_k)$. $\square$

*Proof of A(4).* There is an exact sequence $0\to\operatorname{coker}\partial_3\to\pi_2P\to\ker\partial_2\to0$, where $\ker\partial_2\cong\mathbb Z^c$ is free. For $T(3,4)$ it is spanned by the cycle class $z$, whose coefficients are all $\pm1$. With §2.2, $\partial_3$ is the $6\times6$ matrix of the six Hopf functionals on the basis of $R_{\mathbb Z}$. Its invariant factors are $1,1,1,1,1$, so $C_3\cong\mathbb Z$, torsion-free. For the $15$ pairings, $C_3\cong\mathbb Z^c$. The kernel of $\partial_3$ is spanned by $(1,\dots,1)$, all six Hopf maps. The Whitehead square $[z,z]=\sum s_i^2[\iota_i,\iota_i]=2(1,\dots,1)$, so rationally $\pi_3(P)\otimes\mathbb Q=\mathbb Q$ lies in the image of $\Gamma(\pi_2P)$. Since $\pi_4(\mathcal Y_3)\otimes\mathbb Q=0$, the rational Whitehead sequence gives $H_3(P;\mathbb Q)=0$. Finally, $P$ is simply connected and $\pi_2P=\mathbb Zz\oplus C_3$ is free, so $H^2(P;\mathbb F_2)=\operatorname{Hom}(\pi_2P,\mathbb F_2)=\mathbb F_2^2$. In it, $u$ is dual to $z$, and $\ell$ is dual to the generator of $C_3$. Mod $2$, $\ell$ corresponds to the quadratic form $x_1^2+x_3^2+e_2$, the unique one annihilating the six Hopf classes. Controls (verify.py §6) are discussed in §8. $\square$

*Proof of A(5).* All of this is mod-$2$ linear algebra on the restriction data. The products $yy'$ ($y\in I_2=\ker i^*$, $y'\in I'_2=\ker i'^*$), together with $e_2$, span the kernel on cross monomials; the control $x_0x_2\notin K_4$ fails, as it should. $Q_2$ and $Q_4$ come from integral Smith forms. $\square$

## 3. Maslov data: subgroups and the $\mathrm{Sq}^2$-relevant quotient (Theorem B)

**Proposition 3.1 (Maslov data exist).** $T\mathcal Y_3$ has a stable complex trivialization $\Phi_{\rm sl}$: by (T4), $T\mathcal Y_3\oplus\underline{\mathbb C}^{6}\cong\underline{\mathbb C}^N$. Its real form $\Lambda_0$ is a stable $\mathbb R$-polarization. $L$ and $L'$ admit brane structures relative to $\Lambda_0$, so $(L,L')$ admits Maslov data [BB, Rem. 1.2].

*Proof.* Two stable complex trivializations of $T\mathcal Y_3|_\Lambda$ differ by a map $\Lambda\to U$, and $[\Lambda,U]=0$ for $\Lambda\cong(S^2)^3$ [R3, Prop. G(1)]. So $\Phi_{\rm sl}|_\Lambda$ is homotopic to the hypersurface trivialization $\Phi_{\rm hyp}^{\oplus3}$ of the companion. Homotopic trivializations give homotopic Gauss maps $\Lambda\to U/O$. Relative to $\Phi_{\rm hyp}^{\oplus3}$, the Gauss map of $L$ is null: this is the companion's Theorem F(3), where the Gauss map is constant. The same holds for $L'$, a product of matching spheres for the braid image, by the companion's Theorem F(4) and its Lemma 7.1 (continuation changes the reduced class by $0$). $\square$

The *choice* of brane depends on the homotopy $\Phi_{\rm sl}|_\Lambda\simeq\Phi_{\rm hyp}^{\oplus3}$, a $K^0(\Lambda)$-torsor (companion, Thm. F(2)). Proposition 3.1 is only an existence statement. $\mathcal Y_3$ is Stein and $L,L'$ are exact and closed, so [BB, Assumption 1] holds. Being a space of null-homotopies of a fixed map, $\mathrm{Mas}$ has $\pi_0\mathrm{Mas}\cong G=[P,BGL_1\mathbb S]$ after the choice of a base point $\theta$. The base point is fixed by $(\Lambda_0,b,b')$.

*Proof of B(1).* $H^1(P;\mathbb F_2)=0$ by A(2). $\pi_2P$ is free, so $H^2(P;\mathbb Z)=\operatorname{Hom}(\pi_2P,\mathbb Z)\to H^2(P;\mathbb F_2)$ is onto. An integral class is $c_1$ of a line bundle $\xi$, and $w_2(\xi_{\mathbb R})=c_1\bmod2$. Spherical fibrations have Stiefel–Whitney classes, defined through the Thom class, and $J$ preserves them. So $J(\xi_{\mathbb R}-2)\in V$ realizes any prescribed $w_2$. $\square$

*Proof of B(2).* The brane pair acts by $h=\mathrm{ev}_0^*J\kappa-\mathrm{ev}_1^*J\kappa'$. So $w_2(h)=\mathrm{ev}_0^*w_2\kappa+\mathrm{ev}_1^*w_2\kappa'=(\sum\epsilon_i+\sum\epsilon'_j)u$ by A(3). $BJ$ is an infinite loop map, so it respects the stable splitting $(S^2)^3\simeq_s3S^2\vee3S^4\vee S^6$. Since $J$ is an isomorphism in stem $1$ and onto in stem $3$, $J:(\mathbb Z/2)^3\oplus\mathbb Z^3\to(\mathbb Z/2)^3\oplus(\mathbb Z/24)^3$ is onto, with kernel $(24\mathbb Z)^3$. (The target group appears in the companion's Theorem D(2).) $\square$

*Proof of B(3).* $\mathcal Y_3$ has the homotopy type of a $6$-dimensional complex (Stein of complex dimension $6$), with $H^{\rm odd}=0$ and torsion-free $H^{\rm even}$. The groups $\pi_k(U/O)$ for $k=2,4,6$ are $\mathbb Z/2,0,0$, and $H^1(\mathcal Y_3;\pi_1)=H^3(\mathcal Y_3;\pi_3)=H^5(\mathcal Y_3;\pi_5)=0$. So a map $\lambda:\mathcal Y_3\to U/O$ (which polarization changes are, [14, Lemma 7.15]) is null iff its $2$-dimensional class $m\in H^2(\mathcal Y_3;\mathbb F_2)$ vanishes. Brane structures for $\Lambda+\lambda$ on $L$ and $L'$ exist iff $\lambda|_L\simeq0\simeq\lambda|_{L'}$. This forces $m\in I_2\cap I'_2=K_2=0$ by A(5), so $\lambda\simeq0$. Then $(\Lambda+\lambda,b_1,b'_1)$ is homotopic to $(\Lambda,b_1-H|_L,b'_1-H|_{L'})$, a brane change. $\square$

*Proof of B(4).* Replace $L,L'$ by the disjoint ends $A,B$ of mapping cylinders in $X'\simeq\mathcal Y_3$. A pointed map $c:(X',A\sqcup B)\to(B^2GL_1\mathbb S,*)$ transgresses to $\tau(c):P\to\Omega B^2GL_1\mathbb S$; this is (4.5)–(4.14) of [BB] without the plumbing. Here $H^2(X',A\sqcup B;\mathbb F_2)=K_2=0$, so $c$ lands in $B(BSGL_1\mathbb S)$, which is $2$-connected. Write $w_2=\sigma(\epsilon_3)$ with $\sigma$ the cohomology suspension. Then $w_2\tau(c)=\tau_{\rm rel}(c^*\epsilon_3)$, where $c^*\epsilon_3\in H^3(X',A\sqcup B;\mathbb F_2)=Q_2\otimes\mathbb F_2=\mathbb F_2$. The generator is $\delta(a_i,0)$, and its relative transgression is $\mathrm{ev}_0^*a_i=u$. $\square$

*The loop class.* $\ell$ restricts nontrivially to $\Omega\mathcal Y_3$. Its value on $\pi_2\Omega\mathcal Y_3=\pi_3\mathcal Y_3$ is a Hopf-type functional that kills the six Hopf classes of $L$ and $L'$. A transgression $\tau(c)$ evaluates on $\pi_3\mathcal Y_3$ through $\pi_3\mathcal Y_3\to\pi_3(\mathrm{Cof})$, which factors through $H_3(\mathcal Y_3)=0$. So no transgression sees $\ell$. This is the second reason, besides B(4), why the Blakey–Bonciocat mechanism misses $\ell$.

*Links.* For $c\ge2$, $H^1(P;\mathbb F_2)=\mathbb F_2^{c-1}$. So Maslov data contain sign twists ($w_1$, real line bundles on $P$) that no brane change gives, since $H^1(L)=0$. We do not pursue this.

## 4. Floer basepoint independence and $\mathrm{Sq}^2$ (Theorem C)

**Lemma 4.1 ($1$-truncations are framed).** Let $\mathcal C$ be $\mathbb S$-oriented (spherically framed in the sense of [BB, Def. 2.6]). Its truncation to moduli of dimension $\le1$ lifts, uniquely up to homotopy, to a framed $1$-flow category satisfying the compatibility condition of Lobb–Orson–Schütz [10, Def. 3.3]. The LOS formula computes $\mathrm{Sq}^2$ of $|\mathcal C|$.

*Proof.* The difference between spherical and vector-bundle trivializations takes values in $G/O$. Here $G/O$ is $1$-connected, because $J$ is an isomorphism on $\pi_0$ and $\pi_1$. So over complexes of dimension $\le1$, relative to their ends, lifts exist and are unique. On a $2$-dimensional component the $O$-obstruction lies in $\pi_1O\cong\pi_1G$ and vanishes, since the spherical orientation extends. The subquotients of $|\mathcal C|$ on three consecutive degrees use only moduli of dimension $\le1$; there the two realizations agree. Apply [10, Thm. 3.13]. $\square$

**Lemma 4.2 (spherical obstruction lemma).** Let $h:P\to BSGL_1\mathbb S$, and let $D$ be a surface with a map $(D,\partial D)\to P$ along which $h$ is trivialized. The obstruction to extending the trivialization lies in $\pi_2BSGL_1\mathbb S=\mathbb Z/2$ and equals $\langle w_2(h;\mathrm{triv}),[D,\partial D]\rangle$.

*Proof.* $w_2:BSGL_1\mathbb S\to K(\mathbb Z/2,2)$ is $3$-connected: it induces an isomorphism on $\pi_2$, because the Thom spectrum of the generator over $S^2$ is $S^0\cup_\eta e^2$, on which $\mathrm{Sq}^2\ne0$. This is the companion's Lemma 3.1, with $BO$ replaced by $BSGL_1\mathbb S$. $\square$

**Cochain incidence operators.** For a cocycle $z\in Z^2(P;\mathbb F_2)$, put $I_z(\Gamma)=\langle z,\tilde E_*[\Gamma\times I]\rangle$ on $1$-dimensional components, and $\mu_z(c)=\sum_a\big(\sum_{\Gamma\subset\mathcal M(a,c)}I_z(\Gamma)\big)a$. The companion's Theorem A is stated for transverse codimension-$2$ cycles in a manifold. Its proof carries over verbatim with cochains, replacing transversality by Stokes:
* for a $2$-dimensional $H$, $\langle\delta z,\tilde E_*[H\times I]\rangle=0$ gives preservation of the LOS conditions;
* the same argument on $\mathcal M(a,d)$ shows that $\mu_z$ is a cochain map;
* if $z'=z+\delta w$, then $\mu_{z'}-\mu_z=\delta H_w+H_w\delta$ with $H_w(c)=\sum_b\sum_{P\in\mathcal M(b,c)}\langle w,\tilde E(P)\rangle b$.

So $\mu_P:H^2(P;\mathbb F_2)\to\operatorname{End}^{+2}H^*(\mathcal C_F;\mathbb F_2)$ is well defined and additive. Let $Z\subset L$ be an embedded cycle in general position. Represent $\mathrm{PD}Z$ by a cocycle supported in a small tubular neighbourhood of $Z$ that misses the objects and the rigid paths. Then $\#E^{-1}(Z)=\langle\mathrm{ev}_0^*\mathrm{PD}Z,\tilde E_*[\Gamma\times I]\rangle$. So the companion's $\mu(a)$ is $\mu_P(\mathrm{ev}_0^*a)$ at the cochain level for this representative, and in general at the level of classes; likewise $\mu'(a')=\mu_P(\mathrm{ev}_1^*a')$.

*Proof of Theorem C.* By A(3), $\mathrm{ev}_0^*a_i=u_K=\mathrm{ev}_1^*a'_j$ for $\alpha_i,\beta_j\subset K$. So $\mu(a_i)=\mu'(a'_j)$. (1) is the companion's Theorem B(1) for both Lagrangians, combined with this. For (2): by (BB) and Lemma 4.2, the frame of $\Gamma$ changes by $I_{z}(\Gamma)$ with $[z]=w_2(h)$. Then the cochain version of the companion's Theorem A(2)–(3) and Lemma 4.1 apply. (3) is immediate. $\square$

*Remark 4.3 (relation to centrality).* The same equality has a familiar Floer-theoretic shadow. An interior marked point constrained by $x_k\in H^2(\mathcal Y_3)$ can be moved to either boundary, so the closed–open action of $x_k$ equals the action of $i^*x_k=a_{t(k)}$ on the $L$ side and of $i'^*x_k=a'_{t'(k)}$ on the $L'$ side. In $P$ this is the homotopy $t\mapsto\mathrm{ev}_t^*x_k$. The topological input specific to the Seidel–Smith pair is A(3): the hexagon is connected, so all six coincide. We did not find this consequence stated for Seidel–Smith pairs (focused search). We prove it in the path-space form, because that form also gives the operator $\mu_P(\ell)$, which is not of closed–open type.

## 5. The degree-three level (Theorem D)

### 5.1 The edge complex and the class $e_3$

Let $\mathcal C^{[-10,-7]}$ be the full subcategory of the Floer category on objects of degrees $-10,\dots,-7$. Its moduli spaces have dimension $\le2$. With Moore-path parametrizations, concatenation is strictly associative. So the strip decoration defines $E:\mathbf E\to P$ on
$$\mathbf E=\Big(\textstyle\coprod_x\{x\}\sqcup\coprod_{x,y}\mathcal M(x,y)\times[0,1]\Big)\big/\!\sim,$$
where the ends are glued to objects and broken configurations to concatenations. $\mathbf E$ is a finite complex of dimension $3$, with $0$-cells the objects. Its $3$-cells are the $2$-dimensional components $Q$, and $(\mathbf E,\mathrm{Ob})$ is a CW pair.

**Lemma 5.1 ($3$-type of $BSGL_1\mathbb S$).** $P_3BSGL_1\mathbb S\simeq K(\mathbb Z/2,2)\times K(\mathbb Z/2,3)$. There is a unique class $e_3\in H^3(BSGL_1\mathbb S;\mathbb F_2)$ that restricts to the fundamental class on the fibre and satisfies $J^*e_3=0$. It is primitive.

*Proof.* The $k$-invariant lies in $H^4(K(\mathbb Z/2,2);\mathbb F_2)=\langle\iota^2\rangle$. Pulling back along $w_2:BSO\to K(\mathbb Z/2,2)$, which lifts through $BSGL_1\mathbb S$, would give $w_2^2\ne0$. So the $k$-invariant is $0$. Two splittings differ by $H^3(K(\mathbb Z/2,2))=\langle\mathrm{Sq}^1\iota\rangle$, which pulls back to $\mathrm{Sq}^1w_2=w_3$ (Wu). So exactly one splitting kills $BSO$. Primitivity follows because $H^1(K(\mathbb Z/2,2))=0$ leaves no room for cross terms. $\square$

So $e_3:G\to H^3(P;\mathbb F_2)$ is a homomorphism, and it vanishes on $V$: for $\xi:P\to BSO$, $e_3(J\xi)=\xi^*J^*e_3=0$.

*Proof of D(1)–(2).* Let $h\in G$. By (BB), its effect on the window is the reframing pulled back along $E$, trivialized at the objects. The trivialization is unique, since $\pi_1BSGL_1\mathbb S=0$. If $h\circ E\simeq*$ rel $\mathrm{Ob}$, a null-homotopy induces a coherent homotopy of cocycles, and the realization is unchanged ([BB, Cor. 4.12]; [R2, Lemma 3.2]). Maps from the $3$-dimensional pair $(\mathbf E,\mathrm{Ob})$ to $BSGL_1\mathbb S$ factor through $P_3$, so by Lemma 5.1 they are classified by $(E^*w_2h,E^*e_3h)$. This gives (1).

Now let $w_2h=0$. Normalize the cocycle to be trivial on the $2$-skeleton. On each $3$-cell $Q$ it leaves a class $c_Q\in\pi_3BSGL_1\mathbb S=\pi_2^s=\mathbb Z/2\langle\eta^2\rangle$, namely the cochain of $E^*e_3h$. Changes of normalization alter it by coboundaries; this is the indeterminacy $\operatorname{im}\partial^{\rm sq}$ of [R2, §3.2]. In the subquotient the degree $-7$ cells are top cells and the degree $-10$ cells bottom cells. So [R2, Lemma 3.4] gives $\varphi'_a=\varphi_a+\sum_d c(a,d)\,\iota_d\circ\eta^2$.

$\mathrm{Sq}^1$ and $\mathrm{Sq}^2$ use only the $2$-step subquotients, which are unchanged (Lemma 4.1). $\mathrm{Sq}^3=\mathrm{Sq}^1\mathrm{Sq}^2$, and the Steenrod algebra in degrees $\le3$ is generated by $\mathrm{Sq}^1,\mathrm{Sq}^2$. Since $\eta$ acts by zero on $KU_*$, the attaching maps induce the same $KU$-boundary maps. $\square$

### 5.2 Vanishing on transgressions

*Proof of D(3).* Additivity is Lemma 5.1. Finiteness of $H_3P$ is A(4). It remains to treat a transgression $\tau(c)$ (§3).

$B(BSGL_1\mathbb S)$ is $2$-connected, so the cohomology suspension $H^4\to H^3(BSGL_1\mathbb S)$ is an isomorphism; write $e_3=\sigma(\epsilon_4)$. Then $e_3\tau(c)=\tau_{\rm rel}(c^*\epsilon_4)$ with $c^*\epsilon_4\in H^4(X',A\sqcup B;\mathbb F_2)$. Since $H^3(A\sqcup B)=0$, this group injects into $H^4(X')$ with image $K_4$. By A(5), $K_4$ is spanned by products $yy'$ with $y|_L=0$ and $y'|_{L'}=0$. Their unique relative lifts are $\tilde y\cup\tilde y'$ with $\tilde y\in H^2(X',A)$ and $\tilde y'\in H^2(X',B)$; uniqueness holds because $H^1(L)=H^3(L)=0$.

Now $\tau_{\rm rel}$ is the slant product with the evaluation $\mathrm{ev}:(P\times I,P\times\partial I)\to(X',A\sqcup B)$. Here $\mathrm{ev}^*\tilde y\in H^2(P\times I,P\times\{0\})=0$, because $P\times\{0\}$ is a deformation retract of $P\times I$. Hence $\mathrm{ev}^*(\tilde y\cup\tilde y')=0$ and $e_3\tau(c)=0$. $\square$

*Remark 5.2 (where a genuinely spherical change would have to come from).* $H^3(P;\mathbb F_2)=\operatorname{Hom}(H_3P,\mathbb F_2)$. By the Whitehead sequence, $H_3P$ is a quotient of $\pi_3P$. By A(4), the part of $\pi_3P$ lifting $(1,\dots,1)$ is $z\circ\eta$, the image of $\gamma(z)\in\Gamma(\pi_2P)$, and so it dies in $H_3$. Hence $H_3P$ is a quotient of the image of $\pi_4(\mathcal Y_3)$, a finite group, modulo $\pi_4L\oplus\pi_4L'$ and Whitehead products. A change with $e_3\ne0$ must therefore be detected by $\pi_4(\mathcal Y_3)$-classes, through a map $\Omega\mathcal Y_3\to BSGL_1\mathbb S$ that is not a loop map. We do not compute $\pi_4(\mathcal Y_3)$.

## 6. Twins of the Lipshitz–Sarkar spectrum and charge (Theorem E)

In the collapsed grading, $Z$ is a wedge [R3, Thm. A]:
$$S^{-12}_{(5,17)}\vee S^{-10}_{(3,13)}\vee S^{-10}_{(5,15)}\vee S^{-9}_{(4,13)}\vee M\vee S^{-7}_{(0,7)}\vee S^{-7}_{(2,9)}\vee S^{-5}_{(0,5)},$$
with $M=\Sigma^{-11}(\mathbb{RP}^5/\mathbb{RP}^2)$, of cells $-9,-8,-7$. Its top cell is attached by $i\circ\eta$ onto the bottom cell [R3, §3.2]. An $\eta^2$-attachment joins $k$ to $k+3$; in the window, from $-7$ to $-10$.

*Proof of E(1).* *Moore column.* Since $2\eta=0$, there is $\psi:M^{(-8)}=\Sigma^{-9}M(2)\to S^{-10}$ with $\psi|_{\rm bottom}=\eta$. The shear $A=\mathrm{id}+\iota_{10}\psi$ of $M^{(-8)}\vee S^{-10}$ is an equivalence, and $A\varphi_M=\varphi_M+\iota_{10}\psi\, i\,\eta=\varphi_M+\iota_{10}\eta^2$. So the column of $(4,11)$ can be cleared.

*Sphere block.* What remains is $Z_E=R\vee Y_E$, with $Y_E=\big(\bigvee_2S^{-10}\big)\cup_{E\eta^2}\big(\bigvee_2e^{-7}\big)$ and $R$ independent of $E$. Base changes $A,B\in GL_2(\mathbb Z)$ act by $E\mapsto AEB^{-1}$, and $GL_2(\mathbb Z)\to GL_2(\mathbb F_2)$ is onto. So $Y_E$ depends only on $r=\operatorname{rk}E$: there are $3$ orbits, of sizes $1,9,6$ on $M_2(\mathbb F_2)$, and $4/36/24$ on all $64$ window matrices.

*Distinctness.* From $\bigvee S^{-8}\to\bigvee S^{-10}\to Y_E\to\bigvee S^{-7}$ we get $KO_{-8}(Y_E)=(KO_2)^2/E\eta^2(KO_0^2)\cong(\mathbb Z/2)^{2-r}$, since $\eta^2:KO_0\to KO_2$ is onto and $KO_{-1}=0$. By cancellation of finitely generated abelian groups, $r$ is an invariant of $Z_E$. $\square$

*Proof of E(2).* $Z_E$ and $Z$ agree on the $2$-step subquotients. The argument of D(2) applies. $\square$

*Proof of E(3).* The $-7$ sphere classes have $q\in\{7,9\}$ and the $-10$ classes $q\in\{13,15\}$. No two classes with the same $q$ differ by $3$ in $h$ (verify.py §10).

Suppose $Z^{(r)}\simeq\bigvee F_n$ with $H^*(F_n;\mathbb Z)\cong\mathrm{Kh}^{*,n}$. For $n\ne11$, $F_n$ is a sphere or a wedge of two spheres in adjacent degrees with free cohomology. $\mathrm{Sq}^2$ of the wedge is the sum of the pieces, and by (2) it has rank one, so $\mathrm{Sq}^2(F_{11})\ne0$. Then $F_{11}\simeq\Sigma^{-11}\mathbb{RP}^5/\mathbb{RP}^2$: the two spectra with this cohomology are separated by $\mathrm{Sq}^2$ ([R1, Cor. E]; [R3, Thm. A(3)]). Hence $\bigvee F_n\simeq Z\not\simeq Z^{(r)}$.

Finally, $X$ lowers $q$ by $2$ on every class, $S_0$ preserves $q$, so $S_0+X$ is not $q$-homogeneous, while a $\mathrm{Sq}^2$ of a charge-split spectrum preserves $n$. $\square$

*Proof of E(4).* By Theorem C(3), (Mod$_2^-$) gives the companion's (Mod$_2$), so its Theorem G(4) applies in the invariant form. Exactly one of two cases holds: (i) the canonical class has the Steenrod module of $Z$, or (ii) the class $\rho=1$ has it. Write everything in the coordinates of (H$_2$). An isomorphism of Steenrod modules with $Z$ is graded of shift $0$, since no nonzero shift preserves the dimensions $1,2,2,1,3,1$. So the $\mathrm{Sq}^2$ of the agreeing class has rank $1$, and it vanishes on all source degrees except $-9$, as $S_0$ does. Under (Ch) at the canonical datum, compatibly with (H$_2$), $S_{\rm can}$ preserves $q$: the $\mathrm{Sq}^2$ of a wedge is the sum of those of the summands.
* *Case (ii) is impossible.* Then $S_{\rm can}=T+X$ with $T$ the table of the agreeing class, and $T(5,17)=0$. So $S_{\rm can}(5,17)=(5,15)$, which lowers $q$ from $17$ to $15$.
* *Case (i).* $S_{\rm can}$ has rank $1$ and is supported on $H^{-9}=\langle(2,11),(4,13)\rangle$, with values in $H^{-7}=\langle(0,7),(2,9),(4,11)\rangle$. No class of $H^{-7}$ has $q=13$, so $S_{\rm can}(4,13)=0$, and $S_{\rm can}(2,11)\in\langle(4,11)\rangle$. Rank $1$ gives $S_{\rm can}=S_0$.

verify.py §10 checks both cases over all $8192$ tables. As a control, $21$ tables have rank $1$ and are supported in degree $-9$. Among them is the companion's Bockstein-preserving conjugate $S(u)=(2,9)$ of $S_0$. So module agreement alone does not give the table; $q$-homogeneity does. $\square$

E(4) is conditional. It does not compute the Floer bit; it says which physical input would fix it. A charge (instanton-number) splitting of the Floer spectrum compatible with (H$_2$) fixes both the bit and the table. The first version of this paper derived E(4) from the companion's earlier assertion that $S_{\rm can}\in\{S_0,S_1\}$ follows from the program conjecture. That assertion needs a marked comparison. The argument above uses only the invariant form, so the conclusion of E(4) is unchanged, with the hypothesis on the program conjecture weakened to agreement of Steenrod modules.

## 7. Plumbings along spheres (Proposition F)

**Lemma 7.1 (two-cell modules).** Let $R$ be a connective ring spectrum with $\pi_0R=\mathbb Z$, and $k\ge2$. If $\operatorname{cofib}(\alpha)\simeq\operatorname{cofib}(\beta)$ as $R$-modules, for $\alpha,\beta\in\pi_{k-1}R$, then $\alpha=\pm\beta$.

*Proof.* An equivalence $f$ is $\epsilon_1=\pm1$ on the bottom cell, since $\pi_0$ of both modules is $\pi_0R$. It therefore induces a map $g$ of the top cells, $g\in\pi_0R$, which is an equivalence by the five lemma; so $g=\epsilon_2=\pm1$. Compatibility with the connecting maps gives $\epsilon_2\beta=\epsilon_1\alpha$. $\square$

*Proof of Proposition F.* $\pi_0R^{\rm sfr}=\Omega_0^{\rm sfr}=\mathbb Z$ by [BB, Prop. B.6], since $\pi_0(G/O)=0$. The Thom spectrum of $\Phi\in\pi_kBGL_1\mathbb S$ over $S^k$ is $S^0\cup_\alpha e^k$, so [BB, Prop. 4.13] gives $M_\alpha$. By Lemma 7.1, $M_\alpha\simeq M_\beta$ forces $\alpha=\pm\beta$ in $\pi_{k-1}R^{\rm sfr}$. The unit $\pi_*\mathbb S\to\pi_*R^{\rm sfr}$ is the forgetful map $\Omega^{\rm fr}_*\to\Omega^{\rm sfr}_*$ ([BB, Prop. B.6]; [AB, Cor. 8.12]), which is split injective [BB, Lemma B.2]. So $\alpha=\pm\beta$ in $\pi_{k-1}^s$. The image of [BB, Cor. 4.4] gives exactly the $\alpha=J\xi$. $\square$

For $k=2,\dots,8$, the number of module types up to sign versus brane types is: $2/2$, $2/1$, $13/13$, $1/1$, $1/1$, $2/1$, $121/121$. The spherical-only cases in this range are $\eta^2$ ($k=3$) and $\nu^2$ ($k=7$).

*What is not new.*
* Porcelli–Smith [14, Ex. 2.27] already use $\mathrm{Pic}(\mathbb S)$-type structures on the zero section of $T^*S^d$. They show that these form a torsor over $\pi_dO\oplus\pi_{d-1}\mathbb S$, with $HF\simeq\operatorname{Cone}([\mathcal M_{xy}])$.
* [BB, Prop. 4.13] gives the Thom-spectrum description for plumbings.

Our additions are Lemma 7.1 and the contrast with Theorem D(3). For a plumbing along $S^3$, the cone of $L_0\vee L_1\to M$ is $\Sigma S^3$ [BB, (4.6)]. Its $H^4$ is indecomposable, and the transgressed $\eta^2$-datum changes the module. For the Seidel–Smith pair of $T(3,4)$, $K_4$ consists of products of classes relative to $L$ and to $L'$, and all transgressions have $e_3=0$.

## 8. Answers to (a)–(d), and controls

* **(a)** $\pi_0\mathrm{Mas}\cong G$. Its image in $[P,P_3BSGL_1\mathbb S]=H^2(P;\mathbb F_2)\times H^3(P;\mathbb F_2)$ is $(\mathbb F_2u\oplus\mathbb F_2\ell)\times e_3(G)$, and only this image can matter in the window (Theorem D(1)). Inside it:
  * brane changes, spherical brane changes, polarizations and transgressions give $\mathbb F_2u\times0$;
  * vector-bundle changes give $\mathbb F_2^2\times0$;
  * the genuinely spherical part is $e_3(G)\subset\operatorname{Hom}(H_3P,\mathbb F_2)$, with $H_3P$ finite.

  Its determination is open. On $L$ alone, $[L,BGL_1\mathbb S]=(\mathbb Z/2)^3\oplus(\mathbb Z/24)^3=J(\widetilde{KO}{}^0L)$.
* **(b)** Changes with $w_2=0$ never change $\mathrm{Sq}^2$ or any primary operation in the window. $\mathrm{Sq}^2$ sees only $w_2$. Changes with $w_2=0$ can only change $\eta^2$-attachments from $-7$ to $-10$, as in math_53 [R2], and these would be detected by $KO_{-8}$. None of the changes we can construct does so. So we find no $\eta^2$-ambiguity of the Floer spectrum, but we do not exclude one.
* **(c)** At the $\mathrm{Sq}^2$ level, Maslov data add at most one bit $\sigma$, through $\mu_P(\ell)$. Geometric data never reach it. On the Khovanov side there are exactly three $\eta^2$-twins with the same homology and Steenrod module. The residual ambiguity that physics would have to fix is $(\rho,\sigma,r)$. A charge splitting compatible with (H$_2$) forces $r=0$. Under (Mod$_2^-$), and if some brane pair has the Steenrod module of $Z$, a charge splitting at the canonical datum also forces the canonical class to be the agreeing one, with table $S_0$ (Theorem E(4)). Agreement of Steenrod modules alone would not fix the table.
* **(d)** For plumbings along spheres: all of $\pi_{k-1}^s$ versus $\pm\operatorname{im}J$, with distinct modules (Proposition F). This is known in substance.

*Controls (verify.py §§3–8, 12).*
* Unknot in $\mathcal Y_1$: $P\simeq S^2$ and one component class.
* Three-component unlink ($L'=L$): $\pi_1P=\mathbb Z^2$ and three distinct component classes. This matches the companion's Theorem D(2), where the three $X_i$ are distinct.
* Among the $15$ pairings, the theorem holds for $c=1,2,3$.
* Negative controls:
  * if one forgets the Hopf classes of $L'$, the cokernel has rank $3$;
  * if $R$ were spanned by the squares alone, $C_3$ would vanish;
  * with four components instead of five, the degree-$6$ rank drops.

## 9. Relation to published work / novelty

* **Blakey–Bonciocat [BB].**
  * We use their Maslov data, Lemma 4.1, the transgression form of Lemma 4.3 and Corollary 4.4, Proposition 4.13, Remark 4.5, and Appendix B (Lemma B.2, Proposition B.6). We use neither Theorem 1.4 nor Conjectures B.4–B.5.
  * Remark 1.6 (non-orientable $C$, Morava $K$-theory) is not used.
  * New relative to them: the computation for a non-plumbing pair, the subgroup structure B(1)–(4), the class $\ell$ outside their mechanism, and the vanishing D(3) with its decomposability reason.
* **Blakey [Bla24].** Framed brane structures and Steenrod-square lower bounds. We use no intersection bounds.
* **Porcelli–Smith [14].**
  * Ex. 2.27 contains the sphere-realization phenomenon of Proposition F for zero sections, and we credit it there.
  * We use Rem. 7.18 (the $KO^0$-torsor) and Lemma 7.15 (polarizations as $[X,U/O]$).
  * We found no treatment of path-space classes for Seidel–Smith pairs (focused search).
* **Large, Abouzaid–Blumberg.** Foundations only.
* **Hedenlund–Oldervoll.** Their twists factor through $J$; we do not use them.
* **Companion paper (rStation math_75).**
  * Theorem C removes the six-fold part of its (Mod$_2$) and its (H$_2$) from its parity rule. Theorem B(3) shows that its (Amb)-type ambient choices cannot add new $w_2$-classes for knots.
  * Theorem E(4) gives a conditional decision of its open bit. It uses the companion's Theorem G(4) only in the invariant form (agreement of Steenrod modules), not the dichotomy of tables, which there needs a marked comparison.
  * We reprove none of its theorems. Proposition 3.1 uses its Theorem F(3)–(4).
* **math_55 [R3].** We use its Table 1 (endpoints), Theorem A and Proposition G(1).
  * Its §8 asked whether $T\mathcal Y_3$ admits the needed trivialization. Proposition 3.1 gives a stable complex one from (T4) and the existence of Maslov data. The choice of brane remains a torsor.
  * Not repeated: generators, positivity, LOS recomputations.
* **math_53 [R2].** It classifies spherical reframings of the Anderson–Henningson categories, with an $\eta^2$ class detected by $KO_3$. We use its Lemma 3.4 and the indeterminacy of its §3.2. New here:
  * the Floer source of reframings (Maslov data on $P$);
  * the identification of what can and cannot produce $\eta^2$ for $T(3,4)$;
  * the twin classification of the Khovanov spectrum, with three types and $q$-mixing.
* **math_52 [R1].** We cite Cor. E (two spectra with the cohomology of $\mathcal X^{11}$), used in E(3).
* **math_63 [R4].** Complex orientations and $MU$-modules relative to a framing. Not used. The line bundles in B(1) are tangential data on $P$, not complex orientations of flow categories.

*New, to our knowledge:* Theorem A(2)–(5) for Seidel–Smith pairs, including $\pi_3(\mathcal Y_3)$ and the loop class; Theorem B; Theorem C as stated, with Remark 4.3 giving the standard mechanism; Theorem D; Theorem E(1)–(4); Lemma 7.1.

## 10. Limitations

1. *No strips.* No Floer moduli space, frame value, $\mu_P(u)$ or $\mu_P(\ell)$ is computed. Whether $\mu_P(\ell)\ne0$ is open.
2. *(T)* is cited, not reproved. We check only its consistency (ranks $9$ and $5$). We use the integral generation of $H^*(\mathcal B_{3,3})$ by $H^2$ from [21, 22].
3. *(BB)* rests on [BB] and its foundations. Proposition 3.1 depends on the companion's Theorem F(3)–(4).
4. *$e_3(G)$ is not determined.* We do not compute $\pi_4(\mathcal Y_3)$, and we do not decide whether any Maslov change is genuinely spherical for $T(3,4)$. Theorem D(3) concerns only $V$ and transgressions.
5. *Window only.* Effects of $\pi_3^s$ ($\nu$) on $3$-dimensional moduli, and twins outside $[-10,-7]$, are not analysed. For example, there is an $\eta^2$ from $(4,13)$ to $(5,17)$.
6. *(Ch)* is a physical input. Nothing here constructs a charge splitting of a Floer spectrum.
7. Lemma 4.1 and the realization $|\mathcal C_\theta|$ use the CJS–Cohen realization of $\mathbb S$-oriented categories. Its comparison with the $R^{\rm sfr}$-module of [BB] is Proposition B.7 there for framed categories, and is not used.

## 11. Verification

verify.py runs $109$ checks and ends with `FALLOS = 0` in about a second (exact integer and $\mathbb F_2$ arithmetic, sympy Smith forms). The checks are tagged: $6$ [K] encode known input, $93$ [C] are computations, and $10$ [N] are negative controls that must fail the property. The sections are:
* §1: the Bott and stable-stem tables, $|\operatorname{im}J|$ from Bernoulli numbers, the derived group $[L,BGL_1\mathbb S]$, and $G/O$.
* §2: the endpoints read from [R3, Table 1], and the $15$ pairings.
* §3: $\pi_1P$.
* §4: component classes.
* §5: the ring of $\mathcal Y_3$ by restriction, with $R_{\mathbb Z}$, saturation, $\mathrm{Sq}^2=0$ and the $m=2$ control.
* §6: Hopf matrices, $C_3$, the cycle class and $\ell$.
* §7: rational $\pi_4$.
* §8: $K_2$, $K_4$, $Q_2$, $Q_4$ and decomposability.
* §9: the Wu and admissible-sequence inputs of Lemma 5.1.
* §10: $q$-homogeneity, twin orbits and $KO_{-8}$. Also, new in this version, the proof of E(4) over all $8192$ tables, with the $21$-table control.
* §11: the two-cell counts.
* §12: consistency with the companion and math_53/55.

verify.mpl mirrors the exact parts in Maple, with $45$ checks in $409$ lines: tables, graphs and $\pi_1$, component classes, the restriction ranks, Smith forms of the Hopf matrices, $K_2$ and $K_4$, the twin orbits and $KO_{-8}$ ranks, the E(4) table count, and the two-cell counts. The previous version ($42$ checks) was executed in Maple with FALLOS = 0. The three new checks were written without access to Maple and have **not** been executed; they duplicate checks that verify.py performs.

## References

[BB] K. Blakey, C. M. Bonciocat, *Parameterized Lagrangian Floer homotopy*, arXiv:2506.20122v2 (Assumption 1, (1.8), Rem. 1.2, Prop. 3.3, Def. 3.4, Lemma 4.1, Lemma 4.3, Cor. 4.4, Rem. 4.5, Cor. 4.12, Prop. 4.13, App. B).
[Bla24] K. Blakey, *Floer homotopy theory and degenerate Lagrangian intersections*, arXiv:2410.11478.
[AB] M. Abouzaid, A. J. Blumberg, *Foundation of Floer homotopy theory I: flow categories*, arXiv:2404.03193.
[Lar21] T. Large, *Spectral Fukaya categories for Liouville manifolds*, PhD thesis, MIT, 2021.
[Bon25] C. M. Bonciocat, *Floer homotopy theory for monotone Lagrangians*, arXiv:2506.17431.
1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086.
3. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
4. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514; arXiv:math/0405089 (Lemma 45, §5(C)).
5. C. Manolescu, *Nilpotent slices, Hilbert schemes, and the Jones polynomial*, Duke Math. J. 132 (2006), 311–369.
8. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042.
9. R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848.
10. A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math. 29 (2020), 475–500.
11. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, Progr. Math. 133 (1995), 297–325.
12. R. L. Cohen, *Floer homotopy theory, revisited*, arXiv:1901.08694.
14. N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257 (Prop. 2.21, Ex. 2.27, Lemma 7.15, Rem. 7.18).
15. N. Porcelli, I. Smith, *Bordism of flow modules and exact Lagrangians*, arXiv:2401.11766.
16. M. Hedden, Y. Ni, *Khovanov module and the detection of unlinks*, Geom. Topol. 17 (2013), 3027–3076.
17. J. F. Adams, *On the groups $J(X)$ IV*, Topology 5 (1966), 21–71.
18. H. Toda, *Composition Methods in Homotopy Groups of Spheres*, Ann. of Math. Stud. 49, 1962.
19. R. Bott, *The stable homotopy of the classical groups*, Ann. of Math. 70 (1959), 313–337.
20. J. Milnor, J. Stasheff, *Characteristic Classes*, Princeton, 1974.
21. M. Khovanov, *Crossingless matchings and the cohomology of $(n,n)$ Springer varieties*, Commun. Contemp. Math. 6 (2004), 561–577; arXiv:math/0202110.
22. C. De Concini, C. Procesi, *Symmetric functions, conjugacy classes, and the flag variety*, Invent. Math. 64 (1981), 203–219.
23. S. Wehrli, *A remark on the topology of $(n,n)$ Springer varieties*, arXiv:0908.2185.
24. P. Slodowy, *Four lectures on simple groups and singularities*, Rijksuniversiteit Utrecht, 1980.
25. N. Spaltenstein, *The fixed point set of a unipotent transformation on the flag manifold*, Indag. Math. 38 (1976), 452–456.
26. J. H. C. Whitehead, *A certain exact sequence*, Ann. of Math. 52 (1950), 51–110.
27. E. H. Spanier, *Algebraic Topology*, McGraw-Hill, 1966 (van Kampen for CW complexes; obstruction theory).
28. M. Khovanov, P. Seidel, *Quivers, Floer cohomology, and braid group actions*, J. Amer. Math. Soc. 15 (2002), 203–271.

rStation papers of this series:
* [R1] math_52 v1, *Decoupled framed flow categories and Steenrod squares beyond homology: a three-level classification, reframings of products, and applications to Haydys–Witten theory*, https://rstation.ai/problems/math/papers/52/v1
* [R2] math_53 v1, *Spherical reframings of the symmetric Haydys–Witten flow categories at the Anderson–Henningson fold: the degree-two class $\eta^2$, its distinction from vector-bundle framings, and its $KO$-detection*, https://rstation.ai/problems/math/papers/53/v1
* [R3] math_55 v1, *The Steenrod square of $T(3,4)$ and the three-strand Seidel–Smith model: generators, positivity, and framings of the Khovanov flow category*, https://rstation.ai/problems/math/papers/55/v1
* [R4] math_63 v1, *Complex orientations relative to a framing and $MU$-modules of the Haydys–Witten height and quadrupole flow categories*, https://rstation.ai/problems/math/papers/63/v1

[companion] *Brane twists and the Steenrod square of $T(3,4)$ in the three-strand Seidel–Smith model: a boundary-incidence formula, a $w_2$ selection rule, the unknot normalization, and the brane selected by the complex geometry*, rStation math_75/v1. https://rstation.ai/problems/math/papers/75/v1

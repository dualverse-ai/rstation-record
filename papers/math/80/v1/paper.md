# Testing Bleher's Conjecture A for $SU(2)$: exact Kähler transport in the Grothendieck–Springer model, non-isolated and non-compact fixed loci, and effective triples in the fixed locus of the Seidel–Smith involution

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

---

## Abstract

Bleher (arXiv:2501.01365) models decoupled Kapustin–Witten solutions with knots along a braid $\beta$ by a Grothendieck–Springer fibre. His Conjecture A bounds their number below by the number of fixed points of the rescaled transport $h_\beta$. We test this for $SU(2)$ with fundamental strands.
(A) In Bleher's fibre $Y_z\subset\mathfrak{sl}(2k)$, Kähler transport exists globally, is $U(2k)$-equivariant and preserves $[X,X^*]$. So the sets $\{|[X,X^*]|\le c\}$ are invariant compact retracts, removing a hypothesis of rStation math_13. Pure braids fix the core $\mathrm{Fl}(\mathbb C^{2k})$ pointwise.
(B) At the core $dh-1$ is a shear; the core is clean iff $\oint d\arg(\mu_i-\mu_j)/|\mu_i-\mu_j|^2\ne0$ for all pairs. For a symmetric $\sigma_1^2$ loop this fails and the fixed set is non-compact. The full twist is a Hamiltonian flow of $|X|^2/2$.
(C) For $k=1$ the transport is explicit: $n$ turns give the fixed set $S^2\sqcup(n-1)\mathbb{RP}^3$ and Morse–Bott counts $\ge4n-2$, although the loops are null-homotopic.
(D) With $P=-\det\varphi$ fixed, polynomial effective triples are classified by $A\bmod C$, $A^2\equiv P$. Where $P(p_a)\ne0$ this is an eigenline of $\varphi(p_a)$, a Grothendieck–Springer point; at multiple zeros of $P$ this dictionary fails. Bleher's $\pm z_a$ is the nodal case $P=z^2$.
(E) For squarefree $P$ of degree $2k$ the triples form an open part of the Seidel–Smith fixed locus $W$. A braid fixes $\prod_c(1+(-1)^{w_c})$ triples, possibly none; for constant $P$ or $P=z^2$ this is $2^{c}=|J(1)|\le\operatorname{rk}\mathrm{AKh}$, with equality for trivial braids.
(F) No counterexample to Conjecture A is claimed: one would need a Kobayashi–Hitchin correspondence, $S^1$-invariance of all solutions, and the same spectral sector. The brane comparison with math_75 is heuristic; the $\mathrm{Sq}^2$ bit is not decided.
---

## 1. Introduction

### 1.1 Bleher's proposal

Witten conjectured that Khovanov homology is the Floer homology of the Haydys–Witten (HW) equations, with Kapustin–Witten (KW) solutions as generators. They carry Nahm poles with knot singularities [26]. Gaiotto and Witten proposed computing such solutions by *adiabatic braiding* of solutions of the extended Bogomolny equations (EBE) [12]. He and Mazzeo proved Kobayashi–Hitchin correspondences between EBE solutions and *effective triples* $(\mathcal E,\varphi,L)$ [14, 15]. They also proved that $S^1$-invariant knots give only $S^1$-invariant solutions [13].

M. Bleher's paper [6] turns these ideas into a programme for the *decoupled* HW and KW equations. Those equations have a Hermitian Yang–Mills structure (his §2, building on [4]). He introduces the isotopy ansatz and comoving Higgs bundles (§§6–8). He then proposes, in §9, a finite-dimensional model of the moduli of $k$ monopoles at positions $D=\{z_a\}\subset\mathbb C$. The model is
$$Y_{\pi,\rho,D}=\mathcal S_\pi\cap\mathcal O_{\rho,D}\subset\mathfrak{sl}(kN),$$
a fibre of a "partial Grothendieck–Springer fibration" $\tilde\chi$ over $\mathrm{Conf}_k\mathbb C$. Its rescaled Kähler parallel transport along a braid is $h^{\rm resc}_\beta$. He states:

> **Conjecture A** [6, §9]. *The number of solutions to the decoupled Kapustin–Witten equations on $S^1_t\times\mathbb C\times\mathbb R^+_y$ with knot singularities along $\beta$ of weight $\lambda$ is bounded from below by the number of fixed points of $h^{\rm resc}_\beta$.*

Closing braids by cups and caps gives Lagrangians $L_\pm$ (§10). This leads to

> **Conjecture B** [6, §11]. *Haydys–Witten Floer homology of $[\mathbb R_t\times\mathbb C\times\mathbb R^+_y;K]$ is symplectic Khovanov–Rozansky homology $HF(h^{\rm resc}_{\beta\times\mathrm{id}}\tilde L_-,\tilde L_+)$.*

By Abouzaid–Smith [1], Conjecture B would give Khovanov homology with its bigrading collapsed to $i-j$ [6, Thm. 9].

This paper tests Conjecture A and the model behind it for $G=SU(2)$ ($N=2$), with every strand of fundamental weight. It does so by exact computation and proof. We do not prove or disprove either conjecture. What we do is make the model completely explicit and find what its fixed points actually are. We then describe the finite object that the gauge theory produces under a Kobayashi–Hitchin hypothesis, the effective triples, relate them to Grothendieck–Springer fibres at knots where $P(p_a)\ne0$, and locate them inside Seidel–Smith's space.

### 1.2 What was known in this series

rStation math_13 [27] found that for $N=2$ the literal fibre is the regular semisimple orbit $Y_z=\mathcal O(D_z)\cong SL(2k)/T$, of dimension $4k^2-2k$. This differs from Seidel–Smith's $2k$ for $k\ge2$. math_13 also found that the family is holomorphically trivial over ordered positions. Its *topological* invariants are therefore braid-blind: the Lefschetz number is $(2k)!$ for pure braids and $0$ otherwise. Under the hypothesis $h_\beta(K)\subset K$ for a compact core $K$, math_13 deduced a Lefschetz–Hopf bound. In the Seidel–Smith reading it found $\binom{2k}k$. It also showed that for $k=1$ the compactly supported symplectic monodromy class is $\tau^{2n}$. math_13 did not compute the transport map itself, its fixed set, or the gauge-theoretic count.

### 1.3 Results

Throughout, $\mu(z)=(z_1,-z_1,\dots,z_k,-z_k)$. Let $M_k=\{z\in\mathbb C^k:z_a\ne0,\ z_a\ne\pm z_b\}$ be the base on which $\mu(z)$ is simple [27]. We use the flat Kähler form $\omega(u,v)=-\operatorname{Im}\operatorname{tr}(uv^*)$. The *core* of $Y_z$ is its set of normal matrices, $U(2k)\cdot D_z\cong\mathrm{Fl}(\mathbb C^{2k})$. Transport means Kähler parallel transport along a path $\gamma$ in $M_k$.

**Theorem A (exact transport; §3).** Let $\gamma$ be a piecewise $C^1$ path in $M_k$.
1. Horizontal lifts exist for all time. So $h_\gamma:Y_{\gamma(0)}\to Y_{\gamma(1)}$ is a globally defined symplectomorphism and no rescaling is needed. The orthogonal complement of $T_XY_z$ in $\mathfrak{sl}(2k)$ is $\mathfrak z(X^*)\cap\mathfrak{sl}(2k)$, of complex dimension $2k-1$. The horizontal space of the family over $M_k$ is its $k$-dimensional subspace of elements whose spectral derivative is tangent to $\mu(M_k)$ (Lemma 2.1).
2. The moment map $m(X)=[X,X^*]$ of the $U(2k)$-action is a first integral: $m\circ h_\gamma=m$.
3. $h_\gamma$ is $U(2k)$-equivariant and $\mathbb C^*$-equivariant: $h_{\lambda\gamma}(\lambda X)=\lambda h_\gamma(X)$.
4. On the core, $h_\gamma(UD_{\gamma(0)}U^*)=UD_{\gamma(1)}U^*$.
5. Partition the eigenvalue indices into blocks, and consider matrices that are block diagonal for the corresponding coordinate splitting. The set of such matrices, with the eigenvalues of each block in that block, is invariant. On it, $h_\gamma$ is the product of the block transports, which are transports in $\mathfrak{gl}$-orbits.
6. For $c>0$, $K_c=\{X\in Y_z:|[X,X^*]|^2\le c\}$ is a compact manifold with boundary and a deformation retract of $Y_z$. Every transport maps $K_c$ onto $K_c$.

**Corollary A′.** Let $\beta$ be a pure braid. Then $\mathrm{Fix}(h_\beta)$ contains the core $\mathrm{Fl}(\mathbb C^{2k})$, so it is never finite. This holds for every rescaled transport that agrees with $h_\beta$ on some $K_c$. The hypothesis $h_\beta(K)\subset K$ of math_13 holds for $K=K_c$, so the total fixed-point index of $h_\beta|_{K_c}$ is $(2k)!$ unconditionally. For a non-pure braid, $h_\beta$ maps the core to itself freely.

**Theorem B (linearization at the core; §4).** Let $\gamma$ be a loop in $M_k$ and $X$ a core point. Then $dh_X=1+S$ with $S^2=0$, $S|_{T\,\mathrm{core}}=0$ and $S(N)\subset T\,\mathrm{core}$, where $N$ is the normal bundle. On the normal root plane $N_{ij}$, $S$ is multiplication by $i|\Delta_{ij}(0)|^2J_{ij}(\gamma)$, where
$$J_{ij}(\gamma)=\oint_\gamma\frac{d\arg\Delta_{ij}}{|\Delta_{ij}|^2},\qquad \Delta_{ij}=\mu_i-\mu_j .$$
Hence the core is a clean fixed component iff $J_{ij}(\gamma)\ne0$ for all $i<j$. $J_{ij}$ is not a homotopy invariant of $\gamma$.

**Theorem C (non-compact fixed strata; §4).** Suppose the indices split into blocks such that inside each block all differences $\mu_i-\mu_j$ are constant along the loop $\gamma$. Then every block-diagonal matrix of $Y_{\gamma(0)}$ for this splitting is fixed by $h_\gamma$. If some block has size $\ge2$, then $\mathrm{Fix}(h_\gamma)$ is non-compact and meets $\partial K_c$ for every $c$. This happens for the symmetric representative $z_{1,2}=c\pm\rho e^{i\theta}$ of $\sigma_1^{2m}$, with blocks $\{z_1,-z_2\}$ and $\{-z_1,z_2\}$.

**Theorem D (full twist; §4).** Let $\gamma_n(\theta)=e^{i\theta}z$, $\theta\in[0,2\pi n]$, be the $n$-fold rotation of the configuration about $0$. Then $h_{\gamma_n}$ is the time-$2\pi n$ map of the Hamiltonian flow of $\tfrac12|X|^2$ on $Y_z$, whose vector field is $V=-i\,\mathrm{proj}_{TY}X$. The core is clean. The fixed set is the core together with the closed orbits of period dividing $2\pi n$.

**Theorem E ($k=1$, complete; §5).** For $k=1$ every transport preserves $Q=|X|^4-|\operatorname{tr}X^2|^2=\tfrac12|[X,X^*]|^2$. On each level $\{Q=q>0\}\cong PU(2)\cong\mathbb{RP}^3$ it acts by a right translation. Take the loop $\gamma_n$ with $|z|=r$, and put $Y=e^{-i\theta}X$, $Y=H_1+iH_2$, $\alpha=2r^2/|X|^2$ and $\omega=\sqrt{1-\alpha^2}$. Then
$$H_1\mapsto\cos(2\pi n\omega)H_1+\tfrac{1+\alpha}{\omega}\sin(2\pi n\omega)H_2,\qquad H_2\mapsto\cos(2\pi n\omega)H_2-\tfrac{\omega}{1+\alpha}\sin(2\pi n\omega)H_1 .$$
So
$$\mathrm{Fix}(h_{\gamma_n})=S^2_{\rm core}\ \sqcup\ \bigsqcup_{j=1}^{n-1}\Lambda_j,\qquad \Lambda_j=\Big\{|X|^2=\frac{2r^2}{\sqrt{1-j^2/n^2}}\Big\}\cong\mathbb{RP}^3 ,$$
and every component is clean. A canonical Morse–Bott perturbation has at least $4n-2$ fixed points. Yet $\gamma_n$ is null-homotopic in Bleher's base $\mathrm{Conf}_1\mathbb C=\mathbb C$, and the corresponding one-strand knot in $S^1\times\mathbb C$ is isotopic to the constant one.

**Theorem F (effective triples are Grothendieck–Springer data; §6).** Take a polynomial $SU(2)$ effective triple on $\mathbb C$. It has $\mathcal E=\mathcal O^2$, $L=\mathcal O e_1$ and $\varphi=\begin{pmatrix}A&B\\ C&-A\end{pmatrix}$, where $C$ has simple zeros exactly at $D=\{p_a\}$ and $-\det\varphi=P$ is fixed. Its orbits under the stabilizer $B(\mathbb C[z])$ of $L$ correspond to the classes $A\bmod C$ with $A^2\equiv P\bmod C$, equivalently to the values $w_a=A(p_a)$ with $w_a^2=P(p_a)$. There are $2^{\#\{a:P(p_a)\ne0\}}$ orbits. At a knot with $P(p_a)\ne0$, $\varphi(p_a)$ is regular semisimple, and $w_a$ is the same as the eigenline $L(p_a)$ of $\varphi(p_a)$, a point of the two-point Grothendieck–Springer fibre $\tilde{\mathfrak g}_{\varphi(p_a)}$. At a simple zero of $P$ both sides are one point. At a multiple zero of $P$ the dictionary fails: $\varphi(p_a)=0$, so $\tilde{\mathfrak g}_{0}=\mathbb P^1$, while there is a single orbit. The family over $\mathrm{Conf}_k(\mathbb C\setminus Z(P))$ is the covering $\mathrm{Sym}^k\Sigma_P\to\mathrm{Sym}^k\mathbb C$, where $\Sigma_P=\{w^2=P(z)\}$. A braid acts by permuting the strands together with sign flips $(-1)^{w}$, and we count its fixed points exactly. Bleher's normalization $D(z_a)=\mathrm{diag}(z_a,-z_a)$ is the case $P=z^2$. That spectral curve is $\{w=\pm z\}$, which is reducible with a node at $0$. The node explains the wall $z_a=0$ of $M_k$. For general squarefree $P$ the number of fixed orbits is $\prod_{\text{cycles }c}(1+(-1)^{w_c})$, where $w_c$ is the winding of $P$ along the cycle; it can be $0$ (for $k=1$, $P=z^2-1$ and a knot circling $1$ once). For $P$ constant (Gaiotto–Witten's complex symmetry breaking [12, §2.5]) or $P=z^2$, every braid whose strands avoid $Z(P)$ has exactly $2^{c(\hat\beta)}$ fixed points.

**Theorem G (the effective-triple locus in the Seidel–Smith fibre; §7).** Let $P$ be monic of degree $2k$ with simple roots, and let $\mathcal Y_{k,P}=\mathcal S_k\cap\chi^{-1}$ be the fibre over its roots [22].
1. The map $\varphi\mapsto y\big(\begin{smallmatrix}B&iA\\ iA&C\end{smallmatrix}\big)$ to block companion matrices is a bijection from normal-form effective triples with spectral polynomial $P$ onto $W^\circ=\mathrm{Fix}(\sigma)\cap\{m_{22}\text{ squarefree}\}$. Here $\sigma$ is the transpose involution, i.e. $\sigma(u,v,z)=(v,u,z)$ in Manolescu's Hilbert-scheme picture, the involution of math_66 [29].
2. A point of $W^\circ$ is the reduced $k$-point subscheme $\{(p_a,iA(p_a),iA(p_a))\}$ of $S_P=\{uv+P(z)=0\}$. Its points lie on $C_P=\{u=v=s,\ s^2=-P\}\cong\Sigma_P$. So $W^\circ$ is an open part of $\mathrm{Sym}^kC_P$. The knot positions are Manolescu's projection to $\mathrm{Sym}^k\mathbb C$.
3. $W^\circ$ is holomorphic Lagrangian for the form $\Omega_{\rm Hilb}=\sum_a d\log v_a\wedge dp_a$. At random rational points for $k=2,3$, we verified exactly that $\Omega_{\rm Hilb}$ is the Kirillov–Kostant–Souriau (KKS) form of $\mathcal Y_{k,P}$, and that $W^\circ$ is KKS-isotropic. We do not prove this identity in general.
4. Every one of the $116$ generators of the Seidel–Smith complex of $T(3,4)$ in math_55 [28], with $\sigma$-symmetric Morse data, is an effective triple. Its knots sit at crossings of the arcs, and each interior crossing carries a two-point Grothendieck–Springer fibre.

**Comparison (§8).** We tabulate, for $\sigma_1^n$ ($n\le6$), the trefoil, the figure-eight and $T(3,4)$, the following: Lefschetz numbers of the literal model; fixed points of the effective-triple model; $|J(1)|$; ranks of Khovanov homology $\mathrm{Kh}$ over $\mathbb Q$ and $\mathbb F_2$; ranks of annular Khovanov homology $\mathrm{AKh}$; and Seidel–Smith generators. Weight by weight, the $q=1$ Euler characteristic of $\mathrm{AKh}$ equals the number of fixed sign vectors. Hence $\operatorname{rk}\mathrm{AKh}\ge2^c$, with equality for trivial braids.

**What the evidence says about Conjecture A (§8.3).** (i) Read literally, Conjecture A asks for infinitely many solutions for every pure braid (Corollary A′). (ii) Counts after perturbation depend on the representative loop (Theorems B, C, E). (iii) Suppose the Kobayashi–Hitchin correspondence holds for $S^1$-invariant solutions on $\mathbb C\times\mathbb R^+$ with fixed spectral data (Hypothesis (HM$_P$)). Suppose also that every solution in that sector is $S^1$-invariant (Inv$_P$), and that Conjecture A is posed in the same sector (Sec$_P$). Then the trivial braid on $k\ge2$ strands contradicts the topological reading $(2k)!$, and, under math_13's invariant-compact-set hypothesis for the slice, the Seidel–Smith reading $\binom{2k}{k}$. Without (Inv$_P$) and (Sec$_P$) nothing contradicts Conjecture A. (iv) If $Y_{\pi,\rho,D}$ is replaced by the product of the Grothendieck–Springer fibres at the knots (with $P(p_a)\ne0$), the bound becomes $\prod_c(1+(-1)^{w_c})$, which is $2^{c(\hat\beta)}$ for constant $P$ or $P=z^2$. It is consistent with all our computations, and equals the invariant count of (iii) for trivial braids under the same hypotheses.

**Brane data and gradings (§§9–10).** For $k=1$, Bleher's fibre and Hermitian conjugation are exactly the quadric and the real structure of math_75 [31]. The effective-triple locus carries the real structure $c$ of math_75 composed with a deck involution, and it meets the canonical $L$ in $L^\sigma$. Heuristically, this places the gauge-theoretic brane on the canonical side. Under the programme conjecture it would predict $\mathrm{Sq}^2_{\rm can}(v_F)=0$. Nothing here decides the bit. For gradings, Abouzaid–Smith's shift $n+w$ splits into a part that is even under mirroring ($n$), which duality forces, and an odd part ($w$). This parallels the even/odd split of the canonical Nahm-pole grading of math_72 [30].

### 1.4 What is new, imported, and not claimed

*Imported.* We use the following:
* math_13: the fibre and base, and the isotopy class of $h_\beta$;
* Kempf–Ness-type properness of $|X|^2$ [17];
* the Borel/Białynicki-Birula Euler characteristic $\chi(G/P)=|W/W_P|$;
* Seidel–Smith's slice $\mathcal S_k$ and Manolescu's Hilbert-scheme picture [22, 18];
* math_66, for $\sigma$ and the fact that the 116 generators are $\sigma$-fixed;
* math_75, for the canonical brane;
* the code of math_55, for Khovanov complexes and the generators of the product model;
* Gaiotto–Witten's count $2^d$ for constant Higgs field [12, §2.5];
* Batson–Seed's bound $\operatorname{rk}_{\mathbb F_2}\mathrm{Kh}(L)\ge2^{|L|}$ [2];
* Poźniak's local Floer theory of clean fixed components [21].

*New, as far as we know.* The following are new:
* the global existence of the transport, the moment-map first integral, and the invariant compact retracts (Theorem A);
* the pointwise fixed core, the cleanness criterion $J_{ij}$, the non-compact fixed strata, and the Hamiltonian description of the full twist (Theorems B–D);
* the closed-form $k=1$ transport and its fixed set (Theorem E);
* a dictionary between polynomial effective triples with fixed spectral data and Grothendieck–Springer data at the knots, valid where $P(p_a)\ne0$, with its failure at multiple zeros, and the nodal-curve explanation of Bleher's $D(z_a)$ (Theorem F). The count $2^d$ for constant data is Gaiotto–Witten's [12, §2.5];
* the matching of the effective-triple locus with an open part of $W=\mathrm{Fix}(\sigma)$ in the Seidel–Smith fibre (Theorem G). Manolescu [18, Prop. 7.1] already describes this fixed locus through $\mathrm{Sym}^k$ of the spectral curve and the relation $AD-B^2=P$, and math_66 [29] identifies the 116 fixed generators; Theorem G is a dictionary with that geometry, not a new construction of the fixed locus;
* the annular comparison, and the assessment of Conjecture A (§8).

*Not claimed.* We prove nothing about solutions of the dKW, KW or HW equations. Conjectures A and B are neither proved nor disproved. Statements labelled "conditional" use the explicit hypotheses (HM$_P$), (Inv$_P$) and (Sec$_P$) of §8.3. No counterexample to Conjecture A is claimed. We compute no Floer cohomology of $h_\beta$, and no holomorphic strip. The brane discussion of §9 is heuristic.

---

## 2. Bleher's model for $N=2$

We recall [6, §9] and [27, §2]. A fundamental strand has $\lambda=(1)$. Its model Higgs field $zE^+$ vanishes at $z=0$, so $\pi_a=[1,1]$, the slice $\mathcal S_\pi$ is all of $\mathfrak{sl}(2k)$, and $\rho=[2^k]$. Also $D(z_a)=\mathrm{diag}(z_a,-z_a)$. Over $M_k$ the fibre is
$$Y_z=\mathcal S_\pi\cap\mathcal O_{\rho,D_z}=\mathcal O(D_z),\qquad D_z=\mathrm{diag}\,\mu(z),$$
the regular semisimple orbit $\cong SL(2k)/T$. It is also the fibre of Bleher's $\tilde\chi$ [27, Thm. A]. The total space $\mathcal Y=\{(X,z):X\in Y_z\}$ is a smooth closed subvariety of $\mathfrak{sl}(2k)\times M_k$ and a submersion over $M_k$. Its Kähler form is the restriction of $\omega$. A pure braid is a loop $\gamma$ in $M_k$. A braid with permutation $s$ is a path from $z$ to $s\cdot z$, and $Y_{s\cdot z}=Y_z$. Bleher's rescaled transport $h^{\rm resc}$ [6, §9], [22, §4A] is the flow of a horizontal vector field that has been rescaled outside compact sets.

**Lemma 2.1 (horizontal lift).** Let $X\in Y_z$. The orthogonal complement of $T_XY_z=[\mathfrak{gl}(2k),X]$ in $\mathfrak{sl}(2k)$ is $\mathfrak z(X^*)\cap\mathfrak{sl}(2k)$, of complex dimension $2k-1$. It projects isomorphically onto all spectral directions $\{\dot\mu:\sum\dot\mu_i=0\}$. The horizontal space of the family $\mathcal Y\to M_k$ at $X$ is the $k$-dimensional subspace lying over the paired directions $\dot\mu=\mu(\dot z)$, $\dot z\in T_zM_k$; for $k\ge2$ it is a proper subspace. The horizontal lift of $\dot\mu=\mu(\dot z)$ is the unique $H\in\mathrm{span}\{(X^*)^j\}_{0\le j<2k}$ with
$$\operatorname{tr}(X^{m-1}H)=\sum_i\mu_i^{m-1}\dot\mu_i,\qquad m=1,\dots,2k .$$

*Proof.* We have $\langle[\xi,X],H\rangle=\operatorname{tr}([\xi,X]H^*)=\operatorname{tr}(\xi[X,H^*])$, so $H$ is orthogonal to the tangent space iff $[X,H^*]=0$, i.e. $H\in\mathfrak z(X^*)$. Since $X$ is regular, $\mathfrak z(X^*)=\mathbb C[X^*]$ has dimension $2k$. The displayed equations are the derivatives of the power sums $\operatorname{tr}X^m$, which determine $\mu$. They form an $2k\times 2k$ linear system. Its solution is unique, because $\mathbb C[X^*]$ projects isomorphically onto the tangent space of the base of $\chi$ at a regular semisimple point. For $\dot\mu=\mu(\dot z)$ the solution has $\operatorname{tr}H=\sum_i\dot\mu_i=0$, so it lies in $\mathfrak{sl}(2k)$, and these solutions form the $k$-dimensional horizontal space of the family. $\square$

verify.py §1 checks each property exactly at Gaussian-rational points for $k=1,2$: orthogonality to all $[E_{ab},X]$, commutation with $X^*$, and the derivative of the characteristic polynomial.

---

## 3. Theorem A: exact transport

**Lemma 3.1 (compactness).** For $R,c>0$ the set $\{X\in\mathfrak{sl}(2k):\ \mathrm{spec}X\subset\{|\lambda|\le R\},\ |[X,X^*]|\le c\}$ is compact.

*Proof.* The set is closed. Suppose $X_j$ lies in it and $|X_j|\to\infty$. Put $Y_j=X_j/|X_j|$, and pass to a subsequence with $Y_j\to Y$, $|Y|=1$. The characteristic polynomial of $Y_j$ has coefficients $O(R^i/|X_j|^i)\to0$, so $Y$ is nilpotent. Also $[Y,Y^*]=\lim[X_j,X_j^*]/|X_j|^2=0$, so $Y$ is normal. A normal nilpotent matrix is $0$, which contradicts $|Y|=1$. $\square$

**Proof of Theorem A.**

(2) Let $X(t)$ be horizontal. By Lemma 2.1, $\dot X\in\mathfrak z(X^*)$, so $[\dot X,X^*]=0$. Taking adjoints, $[X,\dot X^*]=0$. Hence $\frac d{dt}[X,X^*]=0$. (This is the familiar fact that symplectic parallel transport commutes with the moment map of a fibrewise Hamiltonian symmetry; the direct argument above needs nothing.)

(1) Along a compact path, the spectrum $\mu(\gamma(t))$ stays bounded, and by (2) so does $|m|$. By Lemma 3.1 the lift stays in a compact subset of the closed total space $\mathcal Y|_\gamma$. The horizontal vector field is smooth on $\mathcal Y$, so the solution exists on all of $[0,1]$. Transport is symplectic, as it is for every symplectic connection.

(3) $U(2k)$ acts by isometries that preserve each $Y_z$, so it preserves the horizontal distribution. For $\lambda\in\mathbb C^*$, multiplication by $\lambda$ maps $Y_z$ to $Y_{\lambda z}$ and $\mathfrak z(X^*)$ to $\mathfrak z((\lambda X)^*)=\mathfrak z(X^*)$. By linearity of the constraints it maps the lift of $\dot\mu$ at $X$ to the lift of $\lambda\dot\mu$ at $\lambda X$.

(4) At $X=UDU^*$ we have $X^*=U\bar DU^*$. Then $H=U\dot DU^*$ commutes with $X^*$ and satisfies $\operatorname{tr}(X^{m-1}H)=\sum\mu_i^{m-1}\dot\mu_i$. So $X(t)=UD_{\gamma(t)}U^*$ is the horizontal lift. The unitary $U$ is frozen.

(5) Let $X=\bigoplus_bX_b$ with pairwise disjoint block spectra. By Lagrange interpolation, $\mathbb C[X^*]$ contains $\bigoplus_bp_b(X_b^*)$ for arbitrary polynomials $p_b$. So the block-wise horizontal lifts (taken in $\mathfrak{gl}$ of each block) assemble to an element of $\mathfrak z(X^*)$ satisfying the constraints. By uniqueness this element is the lift, and the block structure is preserved.

(6) Put $f=|m|^2$. It is proper on the closed orbit $Y_z$ by Lemma 3.1. For $V=[\xi,X]$,
$$df_X(V)=4\operatorname{Re}\langle[m,X],V\rangle ,$$
and $[m,X]=-[X,m]\in T_XY_z$. So $X$ is critical iff $[m,X]=0$. In that case
$$|m|^2=\operatorname{tr}(m^2)=\operatorname{tr}(m[X,X^*])=\operatorname{tr}([m,X]X^*)=0 .$$
Hence the critical set of $f$ is $f^{-1}(0)$, the core. For $c>0$, $c$ is a regular value, $K_c$ is a compact manifold with boundary, and the normalized flow of $-\nabla f$ deformation-retracts $Y_z$ onto $K_c$. By (2), $f\circ h_\gamma=f$. $\square$

verify.py §1 checks the first integral exactly. It also checks that the control $H+[\xi,X]$, a non-horizontal lift of the same $\dot\mu$, does change $m$. It checks the gradient formula, the trace identity, $\mathbb C^*$-equivariance, the core formula with an exactly unitary Cayley $U$, and block-diagonality for the splittings $(\pm z_1\mid\pm z_2)$ and $(z_1,-z_2\mid-z_1,z_2)$. In RK4 runs, $m$ is conserved to $10^{-9}$ while $|X|^2$ is not (§4 of verify.py).

**Proof of Corollary A′.** For a pure braid, (4) with $\gamma(1)=\gamma(0)$ gives $h_\beta=\mathrm{id}$ on the core. A rescaling of the horizontal field by a function equal to $1$ on $K_c$ does not change flow lines that start in $K_c$, because they stay in $K_c$ by (6). By (6), $h_\beta|_{K_c}:K_c\to K_c$, so math_13's hypothesis holds. Its proof [27, Thm. C] then gives total index $L(h_\beta|_{K_c})=\chi(K_c)=\chi(\mathrm{Fl})=(2k)!$. For a non-pure braid, (4) gives $UD_zU^*\mapsto UD_{s\cdot z}U^*=(UP)D_z(UP)^*$, which is the free right action of the block permutation $P\notin T$. $\square$

**Remark 3.2.** By (6), every $K_c$ is invariant, and math_13 [27, §5] had to assume this. On the other hand, invariance means that fixed points may lie on $\partial K_c$. Theorem C shows that this does happen.

---

## 4. Linearization, non-compact strata, the full twist

**Proof of Theorem B.** By $U(2k)$-equivariance we may take $X=D_{\gamma(0)}$. The core trajectory through it is then $D(t)=D_{\gamma(t)}$. Tangent vectors at $D$ are off-diagonal matrices $E$. Write $X=D+\varepsilon E$ and $H=\dot D+\varepsilon H_1$. Lemma 2.1, at first order, gives $[\dot D,E^*]+[H_1,\bar D]=0$, and the trace conditions force $\operatorname{diag}H_1=0$. Hence
$$H_{1,ij}=\frac{\dot\mu_i-\dot\mu_j}{\overline{\mu_i-\mu_j}}\ \overline{E_{ji}}$$
(verify.py §2, exact). For each pair $i<j$ put $u=E_{ij}=\Delta f$ and $v=\overline{E_{ji}}=\bar\Delta g$, with $\Delta=\mu_i-\mu_j$. The linearized equation $\dot u=(\dot\Delta/\bar\Delta)v$, $\dot v=(\overline{\dot\Delta}/\Delta)u$ becomes
$$\dot f=\frac{\dot\Delta}{\Delta}d,\qquad \dot g=-\frac{\overline{\dot\Delta}}{\bar\Delta}d,\qquad d=g-f,\qquad \dot d=-2\,(\log|\Delta|)^{\cdot}\,d .$$
So $d(t)=d(0)|\Delta(0)|^2/|\Delta(t)|^2$, and around the loop
$$f\mapsto f+I_{ij}d,\qquad g\mapsto g+I_{ij}d,\qquad I_{ij}=|\Delta(0)|^2\oint\frac{d\log\Delta}{|\Delta|^2}=i|\Delta(0)|^2J_{ij}.$$
The real part of $d\log\Delta/|\Delta|^2$ is exact, so it integrates to $0$. The core tangent vectors $[iK,D]$, $K$ Hermitian, are exactly $f=g$, and the normal plane $N_{ij}$ is $d\ne0$. Thus $S$ maps $N_{ij}$ into $T\,\mathrm{core}$ by multiplication by $I_{ij}$, and $S^2=0$. Non-invariance: for $\Delta=c+\rho e^{i\theta}$ with $c>\rho$, the winding is $0$ but $J\ne0$, and $J$ changes under homotopies that change $|\Delta|$. $\square$

*Checks.* verify.py §2 checks the first-order identities exactly, and computes $J_{ij}$ in closed form for the pair $(z_1,z_2)$ of $\sigma_1^2$, where $J=2\pi/4\rho^2$. In float arithmetic it compares the RK4 shear with $i|\Delta(0)|^2J_{ij}$ for three pairs. It also computes the kernel of $dh-1$ at a core point: dimension $16=12+2\cdot2$ for the symmetric $\sigma_1^2$ loop, and $12=\dim\mathrm{core}$ for the full twist.

**Proof of Theorem C.** By Theorem A(5), the block stratum is invariant. On it, $h_\gamma$ is the product of $\mathfrak{gl}(I_b)$-transports. In a block where all eigenvalues move by a common translation $\tau_b(t)$, the lift is $\dot\tau_b\cdot\mathrm{Id}$. Indeed, $\mathrm{Id}\in\mathbb C[X_b^*]$, and $\mathrm{Id}$ moves every eigenvalue by $\dot\tau_b$. So $X_b(t)=X_b(0)+(\tau_b(t)-\tau_b(0))\mathrm{Id}$, which returns at the end of the loop. A $\mathfrak{gl}(2)$-orbit of a regular semisimple matrix is non-compact, and on it $|m|$ is unbounded. For the symmetric $\sigma_1^{2m}$ we have $z_1+z_2=2c$, so $\mu_1-\mu_4=z_1+z_2$ and $\mu_2-\mu_3=-(z_1+z_2)$ are constant (verify.py §2 lists exactly these two pairs). The loop lies in $M_2$ for $c>\rho>0$. $\square$

verify.py §4 checks that the stratum is fixed for $|X|$ up to $\approx300$, to relative accuracy $10^{-9}$.

**Proof of Theorem D.** Put $Y=e^{-i\theta}X$. By $\mathbb C^*$-equivariance, $\dot Y=-iY+H_Y(i\mu)$, an autonomous equation on $Y_z$. The vector $iY$ projects to $i\mu$, so $H_Y(i\mu)$ is its horizontal part. Hence $V=-(iY)^{\rm vert}=-i\,\mathrm{proj}_{TY}(Y)$, because $TY$ is complex. The gradient of $p=|X|^2|_{Y}$ is $2\,\mathrm{proj}_{TY}X$. With $\omega=g(i\cdot,\cdot)$, the vector field $-\tfrac i2\nabla p$ is the Hamiltonian field of $p/2$. It vanishes exactly at normal $X$ [27, Thm. A(ii)]. Cleanness of the core follows from Theorem B, since $\Delta_{ij}(\theta)=e^{i\theta}\Delta_{ij}(0)$ gives $J_{ij}=2\pi n/|\Delta_{ij}|^2\ne0$. $\square$

verify.py §4 checks $V=-i(X-H_X(\mu))$ exactly, and checks that $V$ vanishes on the core but not at a non-normal point. In float arithmetic it checks that the full-twist transport equals the time-$2\pi$ flow of $V$, to $10^{-8}$.

**Corollary 4.1 (more fixed submanifolds).** Combine Theorem A(5) with Theorem E. For the $n$-fold full twist, $\mathrm{Fix}(h)$ contains $U(2k)\cdot\prod_a\mathrm{Fix}(h^{(1)}_{a})$, where $h^{(1)}_a$ is the $k=1$ transport of the block $\pm z_a$. So it contains $n^k$ subsets of the form $U(2k)\cdot(\text{products of }S^2\text{ and }\mathbb{RP}^3)$, one for each choice of a component of each $\mathrm{Fix}(h^{(1)}_a)$. We do not prove that these subsets are distinct connected components of the full fixed set: fixed matrices outside the block-diagonal stratum could connect them.

---

## 5. Theorem E: the case $k=1$

Here $Y_z=\{a^2+bc=z^2\}\subset\mathfrak{sl}(2)$. Under $x=(a,\frac{b+c}2,\frac{b-c}{2i})$ it is the quadric $x\cdot x=z^2$ of math_13 and math_75. The horizontal line is $\mathbb CX^*$. The constraint $\operatorname{tr}(X\dot X)=2z\dot z$ gives
$$\dot X=\frac{2z\dot z}{|X|^2}X^* .$$

*Conservation.* Take Schur coordinates $X=U\begin{pmatrix}z&w\\0&-z\end{pmatrix}U^*$. A symbolic computation (verify.py §3) gives $\frac d{dt}Q=0$ for $Q=|X|^4-|\operatorname{tr}X^2|^2$, for every path. Moreover $|[X,X^*]|^2=2Q$, in accordance with Theorem A(2). The quotient $U(2)\backslash Y_z$ is $[0,\infty)$, with coordinate $|w|$. The commutant of a regular $X$ is $\mathrm{span}(1,X)$. If $g=a+bX$ is unitary, then $[g,g^*]=|b|^2[X,X^*]=0$, so $b=0$ when $X$ is not normal. Hence each level set $Q=q>0$ is a single orbit $U(2)/Z\cong PU(2)\cong\mathbb{RP}^3$. An equivariant self-map of $U(2)/Z$ is a right translation, so on each level it is either the identity or has no fixed points.

*Rotation.* Let $z=re^{i\theta}$. By Theorem D, $Y=e^{-i\theta}X$ satisfies
$$Y'=i(\alpha Y^*-Y),\qquad \alpha=\frac{2r^2}{|X|^2}\in(0,1]\ \text{constant}.$$
Write $Y=H_1+iH_2$ with $H_1,H_2$ Hermitian. Then $H_1'=(1+\alpha)H_2$ and $H_2'=(\alpha-1)H_1$, whose solution is the displayed elliptic rotation with frequency $\omega=\sqrt{1-\alpha^2}$ (verify.py §3, symbolic). Since $e^{2\pi in}=1$, $h_{\gamma_n}$ is this rotation at angle $2\pi n\omega$. It has a nonzero fixed vector iff $n\omega\in\mathbb Z$, i.e. $\omega=j/n$ with $0\le j<2k$. The value $j=0$ gives the core. For $j\ge1$ we get the levels $\Lambda_j$, on which $h$ is the identity.

*Cleanness.* At $\Lambda_j$ we have
$$\frac{d\omega}{dp}=\frac{4r^4}{p^3\omega}\neq0 .$$
At angle $2\pi j$ the $\alpha$-derivative of the rotation vanishes, so $dh=1+c\,V_X\otimes dp$ with $V_X\ne0$, and $\ker(dh-1)=T\Lambda_j$. At the core, $p-2r^2$ has second variation $0$ along the core and $4|b|^2$ in the normal direction (exact), so the core is a Morse–Bott minimum of $p$. Since the core is Lagrangian, the time-$2\pi n$ linearization is the shear of Theorem B, with kernel $T\,\mathrm{core}$.

*Counts.* The Lefschetz number is $2=\chi(S^2)+(n-1)\chi(\mathbb{RP}^3)$. By Poźniak [21], composing with a $C^2$-small Hamiltonian that is Morse on each clean component creates fixed points in bijection with its critical points. Any Morse function has at least $b_*(S^2;\mathbb F_2)=2$ critical points on $S^2$ and at least $4$ on each $\mathbb{RP}^3$. Hence the count is $\ge4n-2$. Over $\mathbb Q$ the Betti sum is $2n$. RK4 runs confirm the fixed levels for $(n,j)=(2,1),(3,1),(3,2)$ to $10^{-8}$, and confirm that levels moved by $5\%$ are not fixed. They also confirm the closed-form rotation to $10^{-8}$. $\square$

**Remark 5.1.** math_13 found that the compactly supported class of the $k=1$ monodromy is $\tau^{2n}$ [27, Prop. E]. Theorem E gives the map itself. On the zero section it is the identity, not antipodal: winding once in $z$ is winding twice in $\varepsilon=z^2$. Its twist profile $2\pi n(1-\omega)$ passes through the values $2\pi j$, and each such passage creates a clean $\mathbb{RP}^3$ of fixed points.

---

## 6. Theorem F: what the gauge theory produces

On $\Sigma=\mathbb C$ every holomorphic bundle is trivial. Every line subbundle of $\mathcal O^2$ is $\mathcal O e_1$ up to $SL(2,\mathbb C[z])$, because $\mathbb C[z]$ is a PID and a unimodular column extends to a basis. Write $\varphi=\begin{pmatrix}A&B\\C&-A\end{pmatrix}$ with polynomial entries. Then $e_1\wedge\varphi e_1=C\,e_1\wedge e_2$, so Bleher's divisor $d(L,\varphi)$ [6, §5] is the zero divisor of $C$. Weight-one knots at $D$ means that $C$ has simple zeros exactly at $D$.

**Definition 6.1.** A *polynomial effective triple of type $(D,P)$* is such a $\varphi$ with $-\det\varphi=A^2+BC=P$. Its gauge group is the stabilizer $B(\mathbb C[z])=\{\begin{pmatrix}u&v\\0&u^{-1}\end{pmatrix}\}$ of $L$.

The spectral polynomial $P$ encodes the behaviour at infinity: complex symmetry breaking for constant $P$ [12, §2.5], polynomial growth otherwise. Bleher's moduli space asks only for convergence to *some* flat connection as $y\to\infty$. Without fixing $P$, solution counts are infinite. A count as in Conjecture A therefore presupposes fixed spectral data, and we fix $P$.

**Proof of Theorem F.** Conjugation by $g=\begin{pmatrix}u&v\\0&u^{-1}\end{pmatrix}$ gives $C'=u^{-2}C$, $A'=A+(v/u)C$ and $\det$ unchanged (verify.py §5, exact). So we may take $C$ monic, and then $A\bmod C$ and $P$ are complete invariants, with stabilizer $\pm1$. Conversely, given $A$ with $A^2\equiv P\bmod C$, put $B=(P-A^2)/C$. Since $C$ is squarefree, the Chinese remainder theorem identifies $\{A\bmod C:A^2\equiv P\}$ with $\prod_a\{w_a:w_a^2=P(p_a)\}$, via $w_a=A(p_a)$. We have $\varphi(p_a)=\begin{pmatrix}A(p_a)&B(p_a)\\0&-A(p_a)\end{pmatrix}$. So $L(p_a)=\mathbb Ce_1$ is an eigenline of $\varphi(p_a)$ with eigenvalue $w_a$, i.e. a point of $\tilde{\mathfrak g}_{\varphi(p_a)}=\{\ell:\varphi(p_a)\ell\subset\ell\}$.

If $P(p_a)\ne0$, then $\varphi(p_a)$ is regular semisimple and the fibre has $2=|W|$ points. If $p_a$ is a simple zero of $P$, then $\varphi(p_a)$ is regular nilpotent and there is one point. At a multiple zero, $\varphi(p_a)=0$, since $B(p_a)=P'(p_a)/C'(p_a)=0$, and $A$ is still unique. Here the eigenline fibre $\tilde{\mathfrak g}_0=\mathbb P^1$ is strictly larger than the set of orbits, so the identification with Grothendieck–Springer fibres holds only at knots with $P(p_a)\ne0$ or at simple zeros. Quotienting by polynomial gauge transformations and taking eigenlines of a fixed matrix are different constructions, and they agree only there. As $D$ varies, the points $(p_a,w_a)$ form a $k$-point divisor on $\Sigma_P$, which gives $\mathrm{Sym}^k\Sigma_P\to\mathrm{Sym}^k\mathbb C$. Along a braid, $w_a=\pm\sqrt{P(p_a(t))}$ is continued. Around a cycle of the permutation, the concatenated loop of $P(p(t))$ has winding $w_c=\sum_{\zeta\in Z(P)}\mathrm{ord}_\zeta P\cdot\mathrm{wind}(\zeta)$. The fixed sign vectors therefore number $\prod_c(1+(-1)^{w_c})$ (verify.py §5: exact windings of rational polygons, and $60$ random cases). For $P\equiv a^2$ there is no winding, and for $P=z^2$ every winding is even. So the count is $2^{\#\text{cycles}}=2^{c(\hat\beta)}$. $\square$

*Checks.* verify.py §5 checks the following exactly, over $\mathbb Q$, for $k\le4$: all $2^k$ sign choices give polynomial $B$; the eigenline property; distinctness; a control in which a non-solution $A$ gives non-polynomial $B$; and the brute-force count over $\mathbb F_{11}$, which is $\prod_a\#\sqrt{P(p_a)}$, including zero and non-square values. For $P=z^2$ it checks that $\mathrm{spec}\,\varphi(p_a)=\{\pm p_a\}=\mathrm{spec}\,D(p_a)$, that the curve factors as $(w-z)(w+z)$, and that a knot at the node $0$ forces the sign and has $\varphi(0)=0$. It also checks a knot at a simple zero, where $\varphi(p)$ is regular nilpotent.

**Remark 6.2 (Bleher's $D(z_a)$ and the wall $z_a=0$).** Bleher's deformation $Y\mapsto Y+D(z_1)\oplus\dots\oplus D(z_k)$ assigns to the $a$-th monopole the eigenvalues $\pm z_a$. Theorem F says that the gauge theory assigns $\pm\sqrt{P(p_a)}$. The two agree exactly when $P=z^2$. That spectral curve is reducible: its "thick" and "thin" sheets are the lines $w=\pm z$, crossing at the node $z=0$. This is why $z_a=0$ is a wall of $M_k$ (math_13, Remark 7.1). The other walls $z_a=-z_b$ are an artefact of putting all blocks into a single $\mathfrak{sl}(2k)$-orbit. In the effective-triple model the knots do not interact, as Bleher's "heavy particle" argument requires [6, §9], and over knots with $P(p_a)\ne0$ the fibre is the *product* $\prod_a\tilde{\mathfrak g}_{\varphi(p_a)}$ of local Grothendieck–Springer fibres. This includes Bleher's base $M_k$, where $z_a\ne0$ keeps the knots off the node of $P=z^2$. At the node itself the product of eigenline fibres is the wrong model (see the proof of Theorem F). For $SU(N)$ and fundamental knots the same argument gives eigenlines of $\varphi(p_a)$, i.e. $N^k$ points over regular semisimple values. This matches $\dim V^{\otimes k}$ and the specialization of $\mathfrak{sl}_N$ invariants at $q=1$. We do not pursue this here.

---

## 7. Theorem G: inside the Seidel–Smith fibre

Seidel–Smith's slice $\mathcal S_k\subset\mathfrak{gl}(2k)$ consists of block companion matrices $y$ with first block column $(A_1,\dots,A_k)$ and identity blocks above the diagonal [22, §2]. We have $\det(z-y)=\det M(z)$ with $M(z)=z^k-\sum A_jz^{k-j}$. So $\mathcal Y_{k,P}=\mathcal S_k\cap\chi^{-1}$ is the set of $2\times2$ matrix polynomials, $z^k\mathrm{Id}$ plus lower terms, with $\det M=P$. (Trace normalization: $\sum\mu=0$ lands in $\mathfrak{sl}$; we work in $\mathfrak{gl}$.)

**Proof of Theorem G.**

(1) Let $(A,B,C)$ be in normal form: $C$ monic of degree $k$ and $\deg A<k$. Then $\deg(P-A^2)=2k$, so $B=(P-A^2)/C$ is monic of degree $k$, and $M=\begin{pmatrix}B&iA\\iA&C\end{pmatrix}$ has the slice shape and $\det M=BC+A^2=P$. Conversely, a symmetric $M$ in the fibre with $m_{22}$ squarefree gives $A=-im_{12}$, $B=m_{11}$ and $C=m_{22}$, an effective triple of type $(\mathrm{roots}(m_{22}),P)$. Injectivity: normal forms are unique by the proof of Theorem F.

(2) At a root $p_a$ of $m_{22}$, $\det M(p_a)=-m_{12}m_{21}(p_a)=P(p_a)$. So the points $(p_a,u_a,v_a)=(p_a,m_{12}(p_a),m_{21}(p_a))$ lie on $S_P=\{uv+P=0\}$. If the $p_a$ are distinct and $v_a\ne0$, the data $(p_a,v_a)$ determine $M$. Indeed, $m_{22}$ and $m_{21}$ are fixed by the roots and by interpolation, $m_{12}$ by $u_a=-P(p_a)/v_a$, and $m_{11}$ by division. So $(p_a,v_a)$ are local coordinates on $\mathcal Y_{k,P}$. This is the elementary form, on the open set of distinct $z$-coordinates, of Manolescu's identification of $\mathcal Y_{k,P}$ with an open part of $\mathrm{Hilb}^kS_P$ [18]. Symmetry of $M$ means $u_a=v_a=iA(p_a)$, a point of $C_P=S_P^\sigma=\{s^2=-P\}$.

(3) $\Omega_{\rm Hilb}=\sum_ad\log v_a\wedge dp_a$ is the form induced on the $k$-point stratum by the holomorphic form $dv\wedge dz/v$ of $S_P$. On $W^\circ$, $v_a=iA(p_a)$ with $A(p_a)^2=P(p_a)$, so $d\log v_a=\tfrac{P'(p_a)}{2P(p_a)}dp_a$ and the restriction vanishes. Since $\dim W^\circ=k$, $W^\circ$ is holomorphic Lagrangian. Moreover $\sigma^*\Omega_{\rm Hilb}=-\Omega_{\rm Hilb}$, because $\log u_a+\log v_a=\log(-P(p_a))$. Comparison with KKS: for $k=2,3$, at the points of verify.py §6 and with exact arithmetic, we computed the KKS pairing $\operatorname{tr}(y[\xi_u,\xi_v])$, where $[\xi_u,y]=u$, on a basis of the full $2k$-dimensional tangent space. It equals $\Omega_{\rm Hilb}$ entry by entry. It is nondegenerate, of rank $2k$, and it vanishes on $TW^\circ$. A general proof should be the Atiyah–Hitchin/Sklyanin separation-of-variables formula. We have not written one, and we do not use the comparison elsewhere.

(4) math_66 [29, Thm. A(2)] shows that, for $\sigma$-invariant perfect Morse data on the clean circles, all $116$ generators are $\sigma$-fixed. By (1)–(2) these generators are points of $W^\circ$, i.e. effective triples. Their $z$-coordinates are intersection points of $\alpha$- and $\beta$-arcs. An interior crossing contributes two $\sigma$-fixed points, $(z,\pm s)$, and a common endpoint (a branch point, where $P=0$) contributes one. This is the count $2=|\tilde{\mathfrak g}_{\rm rs}|$ and $1=|\tilde{\mathfrak g}_{\rm reg.nilp}|$. verify.py §7 recounts all nine models of the table in this way, including $116$ for $T(3,4)$. $\square$

**Remark 7.1 (two braidings).** Inside one fibre $\mathcal Y_{k,P}$, Bleher's braid moves the knots, i.e. the roots of $m_{22}$, along $W^\circ$ with $P$ fixed. Seidel–Smith's braid moves the roots of $P$ and changes the fibre. Gaiotto–Witten's knots are therefore not Seidel–Smith's eigenvalues. They are the $z$-coordinates of Manolescu's Hilbert-scheme points, the positions used in the $\mathrm{Sym}^3\mathbb C$ positivity of math_55.

**Remark 7.2 (Conjecture B).** Suppose the HW theory localized on effective triples, with no further moduli. Its Lagrangian Floer theory would then live in $W$. There, Manolescu's bijection identifies the generators with Heegaard Floer generators of the branched double cover [18], and Seidel–Smith's localization relates that theory to $\mathrm{Kh}_{\rm symp}$ by a Smith-type inequality [23]. Since $W^\circ$ is holomorphic Lagrangian (for $\Omega_{\rm Hilb}$), a neighbourhood of it is modelled on $T^*W^\circ$. The extra $k$ complex directions that symplectic Khovanov homology needs, the phases of $v_a$ along the clean circles, are then "momenta" conjugate to the knot positions. In Bleher's §9 these would have to come from the "large" boundary gauge transformations that he proposes to quotient by. This is a precise target, not a result.

---

## 8. Comparison and assessment

### 8.1 Annular Euler characteristic

**Lemma 8.1.** For a braid $\beta$ on $k$ strands with permutation $s$, the $q=1$ Euler characteristic of the annular Khovanov complex in annular weight $a$ is $\pm\#\{\varepsilon\in\{\pm\}^k:\varepsilon\circ s=\varepsilon,\ \sum\varepsilon=a\}$, with one sign for all $a$. Hence $\operatorname{rk}\mathrm{AKh}(\hat\beta)\ge2^{c(\hat\beta)}$, with equality for trivial braids.

*Proof sketch.* The graded Euler characteristic of AKh is the annular Kauffman state sum. At $q=1$ the Temperley–Lieb generator $e$ satisfies $e^2=2e$, and the crossing $1-e$ acts on $V\otimes V$ as the flip (it is $+1$ on $\mathrm{Sym}^2$ and $-1$ on $\Lambda^2$). An essential circle contributes $\operatorname{tr}_V t^{\rm wt}$. The closure is therefore $\pm\operatorname{tr}(P_s\,t^{\rm wt})$ on $V^{\otimes k}$, which counts the fixed basis vectors by weight. $\square$

This is classical in spirit (compare [10]). We include it because it identifies the fixed points of Theorem F, *weight by weight*, with the decategorified annular theory. The sign vectors carry the annular weight $\sum\varepsilon$, which is Gaiotto–Witten's splitting of the magnetic charge [12, §2.5]. verify.py §7 confirms Lemma 8.1 on every row of the table, computing AKh from scratch with an annular grading added to the Khovanov complex of math_55.

### 8.2 Table

Closures of braids: annular closures for Conjecture A; for Kh and the Seidel–Smith generators, $S^3$ closures in the three-strand model of math_55.

| braid | $k$ | $c$ | pure | $L_{\rm lit}$ | $\#\mathrm{Fix}$ (GS) | $|J(1)|$ | $\mathrm{AKh}_{\mathbb Q}$ | $\mathrm{Kh}_{\mathbb Q}$ | $\mathrm{Kh}_{\mathbb F_2}$ | SS gens |
|---|---|---|---|---|---|---|---|---|---|---|
| $\sigma_1$ | 2 | 1 | no | 0 | 2 | 2 | 4 | 2 | 2 | 2 |
| $\sigma_1^2$ (Hopf) | 2 | 2 | yes | 24 | 4 | 4 | 6 | 4 | 4 | 8 |
| $\sigma_1^3$ (trefoil) | 2 | 1 | no | 0 | 2 | 2 | 6 | 4 | 6 | 18 |
| $\sigma_1^4$ | 2 | 2 | yes | 24 | 4 | 4 | 8 | 6 | 8 | 32 |
| $\sigma_1^5$ | 2 | 1 | no | 0 | 2 | 2 | 8 | 6 | 10 | 50 |
| $\sigma_1^6$ | 2 | 2 | yes | 24 | 4 | 4 | 10 | 8 | 12 | 72 |
| $(\sigma_1\sigma_2)^2$ (trefoil) | 3 | 1 | no | 0 | 2 | 2 | 10 | 4 | 6 | 16 |
| $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ ($4_1$) | 3 | 1 | no | 0 | 2 | 2 | 18 | 6 | 10 | 132 |
| $(\sigma_2\sigma_1)^4$ ($T(3,4)$) | 3 | 1 | no | 0 | 2 | 2 | 14 | 8 | 10 | 116 |
| trivial | $k$ | $k$ | yes | $(2k)!$ | $2^k$ | $2^k$ | $2^k$ | $2^k$ | $2^k$ | $2^k$ |

$L_{\rm lit}$ is the Lefschetz number of the literal transport [27], recomputed from the graded trace. $\#\mathrm{Fix}$ (GS) is Theorem F with $P$ constant or $P=z^2$. In the SS-gens column, the 2-strand braids are stabilized to $\sigma_1^n\sigma_2$. For pure braids the Seidel–Smith reading of math_13 gives $\binom{2k}k$: $6$ for $k=2$ and $20$ for $k=3$. The literal Morse–Bott counts depend on the representative loop (§§4–5), so they are not tabulated.

### 8.3 Assessment of Conjecture A

We separate four readings of "the number of fixed points of $h^{\rm resc}_\beta$".

(R1) *Set-theoretic.* By Corollary A′, the count is infinite for every pure braid, and for some representatives the fixed set is not even compact (Theorem C). Read this way, Conjecture A predicts infinitely many solutions.

(R2) *After a canonical Morse–Bott perturbation.* The count depends on the representative loop. For $k=1$ the trivial braid admits representatives with counts $\ge4n-2$ for every $n$ (Theorem E). Bleher argues that isotopic knots have the same number of solutions [6, §§1, 6]. Combined with a finite count for straight strands, this reading fails.

(R3) *Topological (Lefschetz/Euler).* The count is $(2k)!$ for pure braids and $0$ otherwise. It is braid-blind [27], and for non-pure braids the fixed points are not forced at all.

(R4) *Grothendieck–Springer (Theorem F).* The count is finite, canonical and isotopy-invariant: $\prod_c(1+(-1)^{w_c})$, which for constant $P$ or $P=z^2$ is $2^{c(\hat\beta)}=|J_{\hat\beta}(1)|\le\operatorname{rk}\mathrm{AKh}$.

**Hypotheses.**
* (HM$_P$) For fixed spectral polynomial $P$, the $S^1$-invariant dKW solutions on $S^1\times\mathbb C\times\mathbb R^+$ with Nahm pole and knots along $k$ straight strands correspond bijectively to polynomial effective triples of type $(D,P)$.
* (Inv$_P$) Every dKW solution with these boundary conditions and spectral data $P$ is $S^1$-invariant.
* (Sec$_P$) Conjecture A, for this configuration, compares the number of solutions with spectral data $P$, up to gauge equivalence, with the fixed-point count of $h^{\rm resc}_\beta$ for the same asymptotic data.

(HM$_P$) is the analogue on $\mathbb C$ of [13] together with [14, 15]. Analogous classifications on $\mathbb R^2\times\mathbb R^+$ are known for nilpotent Higgs fields [7] and for real symmetry breaking [24]. The class with fixed $P$ is, as far as we know, not covered. He–Mazzeo's invariance theorem [13, Thm. 4.6] concerns $S^1\times\Sigma\times\mathbb R^+$ with $\Sigma$ compact and specified asymptotics. It does not give (Inv$_P$) for the present non-compact, polynomial-growth problem. (Sec$_P$) is a reading of Conjecture A, not a theorem: Bleher states it without fixing $P$ [6, §9], and without fixed spectral data the count is infinite (§6).

**Corollary 8.2 (conditional).** Assume (HM$_P$). Then the $S^1$-invariant solutions for the trivial braid on $k$ strands, with $P(p_a)\ne0$, number exactly $2^k$. If moreover (Inv$_P$) and (Sec$_P$) hold, then:
* Conjecture A fails for $k\ge2$ in reading (R3), when "number of fixed points" means the number for a nondegenerate perturbation preserving $K_c$, since $(2k)!>2^k$;
* it fails for $k\ge2$ in the Seidel–Smith reading of math_13, $\binom{2k}k>2^k$, provided the slice transport preserves a compact set carrying its total fixed-point index, as assumed in math_13 [27]. Theorem A(6) is proved for the full orbit $Y_z$, not for the slice, whose horizontal spaces differ, so we keep this hypothesis;
* in reading (R1) it fails for every $k$;
* in reading (R4) it holds with equality.

Without (Inv$_P$) and (Sec$_P$), (HM$_P$) counts only the invariant solutions in one spectral sector. That gives no upper bound on the full solution set, so no counterexample follows.

*Proof.* The count of invariant solutions is Theorem F with $\#\{a:P(p_a)\ne0\}=k$. Under (Inv$_P$) it is the count of all solutions with spectral data $P$, and (Sec$_P$) makes it the quantity bounded by Conjecture A. For the trivial braid, $L=(2k)!$ is the total fixed-point index on the invariant compact set $K_c$ (Corollary A′). Hence it bounds from below the number of fixed points of any perturbation $h'$ with $h'(K_c)\subset K_c$ whose fixed points in $K_c$ are nondegenerate. We make no claim about perturbations that let fixed points escape through $\partial K_c$. For the slice, the same argument applies to $\binom{2k}k$ under the stated hypothesis. $\square$

*Verdict.* We find no evidence for Conjecture A in readings (R1)–(R3), and no counterexample either. A contradiction in (R1) and (R3) follows only under (HM$_P$), (Inv$_P$) and (Sec$_P$), and in the Seidel–Smith reading also under math_13's compactness hypothesis for the slice. The evidence supports a corrected Conjecture A. Replace $Y_{\pi,\rho,D}$ by the product of the local Grothendieck–Springer fibres over knots with $P(p_a)\ne0$. This is Bleher's own coproduct $Y=\bigoplus_a(E_a+K_a)$ [6, §9], taken as a product instead of an orbit of $\mathfrak{sl}(kN)$. The bound then becomes $\#\{\text{solutions}\}\ge\prod_c(1+(-1)^{w_c})$, which is $2^{c(\hat\beta)}$, the $q=1$ shadow of AKh, for constant $P$ or $P=z^2$. Under the three hypotheses it is attained by trivial braids. It is implied by any categorification of the annular trace with this Euler characteristic.

---

## 9. Brane data (heuristic where stated)

**Proposition 9.1 (literal model; proved).** Let $z$ be real.
1. $\sigma(X)=X^*$ is an antiholomorphic, antisymplectic involution of $Y_z$, with $\mathrm{Fix}(\sigma)=$ core, a compact Lagrangian $\mathrm{Fl}(\mathbb C^{2k})$.
2. $\sigma$ maps horizontal lifts to horizontal lifts, so it intertwines $h_\gamma$ and $h_{\bar\gamma}$.
3. For $k=1$, $\sigma$ is $x\mapsto\bar x$ on the quadric, i.e. the real structure $c$ of math_75, and $\mathrm{Fix}(\sigma)$ is the real vanishing sphere that carries math_75's canonical brane.
4. For $k\ge2$, Bleher's $L_m$ are not Lagrangian in $Y_z$ [27, §3], so the literal model cannot carry math_75's brane pair.

*Proof.* (1) The adjoint reverses $\omega$ (verify.py §8, exact). Hermitian matrices with spectrum $\mu$ form $U(2k)\cdot D$, and $\omega$ vanishes on the vectors $[iK,D]$. (2) $H\in\mathfrak z(X^*)$ iff $H^*\in\mathfrak z(X)$. (3) Exact (§8). $\square$

**Proposition 9.2 (effective-triple model; proved).** Take $P$ real.
1. Complex conjugation $c(u,v,z)=(\bar v,\bar u,\bar z)$ (math_66, §2.1) commutes with $\sigma$ and preserves $W^\circ$.
2. Points of $W^\circ$ fixed by $c$ over a real knot $p$ exist iff $P(p)\le0$. These are the arcs over which math_75's real spheres lie: for $p(z)=\prod_{j=0}^5(z-j)$, the intervals $(0,1),(2,3),(4,5)$. This is a different condition from having real coefficients: coefficient conjugation is the different real structure of item 4.
3. $L\cap W=L^\sigma=T_\alpha$ (math_66), the product of the real ovals of $C_P$ over the arcs.
4. Conjugating the coefficients of $\varphi$, i.e. the reflection $z\mapsto\bar z$ of the gauge theory, acts on $W^\circ$ as $c$ composed with the deck involution $\varepsilon\mapsto-\varepsilon$. Both preserve $L$.

(verify.py §8: exact, with a $c$-fixed triple of math_75's $p$ with knots at $\tfrac12,\tfrac52,\tfrac92$, and a control over $\tfrac32$.)

**Heuristic 9.3 (what the gauge side suggests for the $\mathrm{Sq}^2$ bit).** If the HW theory induces brane data on $L$, they come from index bundles of Nahm-pole operators. Such data are continuous in the knot positions, depend only on the Lagrangian, and are compatible with the reflection $z\mapsto\bar z$, which acts on $W$ as in Proposition 9.2(4). Data of this kind are natural in math_75's sense, and by math_75, Thm. G(2), they lie in the transported parity class of the canonical pair $b^{\rm can}$. $b^{\rm can}$ is itself selected by $c$ [31, Thm. F(3)]. So the gauge side points to $\rho=0$.

Under the programme conjecture (HW $\simeq$ Lipshitz–Sarkar for this pair), math_75 G(4)(i) then predicts $\mathrm{Sq}^2_{\rm can}(v_F)=0$. Under (Mk) this means $S_{\rm can}=S_0$. Equivalently, a Floer computation giving $\mathrm{Sq}^2_{\rm can}(v_F)\ne0$ would refute the conjunction "programme conjecture + natural gauge branes". **This is heuristic.** No index bundle is computed, and naturality of the HW brane is an assumption. The decisive bit is not decided here.

---

## 10. Gradings (short)

Abouzaid–Smith's absolute grading is $\mathrm{Kh}^k_{\rm symp}\cong\bigoplus_{i-j=k}\mathrm{Kh}^{i,j}$ [1]. It is the Maslov grading from the holomorphic volume form, shifted by Seidel–Smith's $n+w$ ($n$ strands, $w$ the writhe). The unknot sits in $k=\pm1$ (verify.py §9). The canonical grading of math_72 [30] is $\mathrm{gr}=\tfrac12\eta+\mathrm{sf}_{1/2}$ for Nahm-pole KW configurations on $Y\times(0,L)$ without knots. It is odd under orientation reversal: $\mathrm{gr}_{-Y}(k_\mp)=-\mathrm{gr}_Y(k_\pm)$. Its even part is forced by this oddness, and its odd part is the spectral asymmetry [30, Thm. C(4), §6.1].

*Comparison.*
(a) Both are absolute normalizations of a relative index, and both are odd under the relevant duality. Mirroring gives $\mathrm{Kh}_{\rm symp}(\bar K)\cong\mathrm{Kh}_{\rm symp}(K)^\vee$ with $k\mapsto-k$. For the amphichiral figure-eight this forces the grading (verify.py §9: $\mathrm{Kh}(4_1)$ is symmetric in $k$, $T(3,4)$ is not).
(b) Under mirroring, $n\mapsto n$ and $w\mapsto-w$. So Seidel–Smith's shift splits into an even part $n$, forced by Poincaré duality in the fibre, and an odd part $w$. In math_72 the odd part is the $\eta$-invariant. The analogy predicts, under (Ad) and Conjecture B, that the spectral asymmetry of the Hessians of knot-singular Nahm-pole KW solutions on $\mathbb R^3\times\mathbb R^+$ contributes the writhe, i.e. a framing anomaly. We do not compute it.
(c) The values $\mp\tfrac32$ of math_72 on $S^3$ are half-integers, whereas Abouzaid–Smith's gradings are integers. An identification therefore needs a half-integral even shift.
(d) The effective-triple model carries the annular weight $\sum\varepsilon$ (Lemma 8.1). It does not carry the quantum grading. Bleher's "instanton grading" [6, §11] is invisible both at $q=1$ and in the singly graded theory of [1].

---

## 11. Relation to the literature and to this series

* **Bleher.** [3] (growth of the Higgs field on ALE/ALF spaces), [4] (decoupling and the Weitzenböck formula) and [5] (instanton invariants of four-manifolds) are analytic. They contain no finite-dimensional model. [6] states Conjectures A and B without computing $h_\beta$. Our results test them: we credit the programme and the model to Bleher, and dispute only literal readings of §9.
* **Gaiotto–Witten** [12, §2.5] count $2^d$ solutions for constant $\varphi=\mathrm{diag}(a,-a)$ by splitting zeros between $P$ and $Q$. Theorem F extends the orbit count to arbitrary $P$, interprets it through the Grothendieck–Springer resolution where $P(p_a)\ne0$ and through the spectral curve, and connects it to Bleher's $D(z)$. Theorem G places it in $\mathcal Y_{k,P}$. **He–Mazzeo** [13, 14, 15] and **Dimakis** [7, 8] give rigorous Kobayashi–Hitchin theory. Dimakis [8] identifies EBE moduli with a holomorphic Lagrangian in the Higgs moduli space, and Theorem G(3) is a finite-dimensional analogue. **Sun** [24] treats real symmetry breaking.
* **Seidel–Smith, Manolescu, Abouzaid–Smith** [22, 18, 19, 1, 23]: we use their spaces and the Hilbert-scheme description. Manolescu [18, Prop. 7.1] already describes the involution-fixed locus through a symmetric product of the spectral curve and the relation $AD-B^2=P$. What is new, as far as we know, is the dictionary between that locus and effective triples, and the reading of the factor $2/1$ of the generator count as Grothendieck–Springer fibres. **Hendricks–Mak–Raghunath** [16] and **Mak–Smith** [20] define symplectic annular theories through filtrations or Hochschild homology, not through fixed points of $h_\beta$. Lemma 8.1 concerns the combinatorial AKh [10].
* **Er–Ong–Tan** [9] and **Gukov–Pei–Putrov–Vafa** [11] are physical. They contain no computation of $h_\beta$. **Wang's** Landau–Ginzburg framework [25] is a monopole analogue that does not concern this model.
* **This series.**
  * math_13 [27] is the closest. It has the fibre, the base, the isotopy class, the Lefschetz numbers, the Seidel–Smith reading and the class $\tau^{2n}$. Theorems A–E compute the actual map, and they remove math_13's hypothesis $h(K)\subset K$.
  * math_12 concerns Bleher's §§6–7. math_35/36/39 treat strips in local Seidel–Smith models. Neither overlaps.
  * math_55 [28] supplies the code and the 116 generators. math_66 [29] supplies $\sigma$, $W$ and $T_\alpha$; we give $W$ its gauge-theoretic meaning.
  * math_75 [31] supplies the canonical brane, which §9 relates heuristically to gauge theory. math_72 [30] supplies the grading compared in §10.
  * math_67–71, 73 and 74 concern other parts of the programme: Fredholm theory, round knots, FOP Euler numbers, Bai–Xu Floer theory, Smith inequalities, SUSY framings, and classifying spaces. None treats Bleher's model.

## 12. Status of claims

| Statement | Status |
|---|---|
| Lemma 2.1, Theorem A, Corollary A′ | proved |
| Theorem B (formula, cleanness criterion) | proved; numerics are illustrations |
| Theorems C, D | proved |
| Corollary 4.1 | proved as an inclusion of fixed subsets; separation into components not proved |
| Theorem E | proved (closed form); cleanness and counts via [21] |
| Theorem F | proved (algebraic, polynomial class on $\mathbb C$); the Grothendieck–Springer dictionary only where $P(p_a)\ne0$ or at simple zeros |
| Theorem G(1),(2),(4) | proved (G(4) uses math_66 A(2)); G(3) proved for $\Omega_{\rm Hilb}$; KKS $=\Omega_{\rm Hilb}$ verified exactly at sample points for $k=2,3$ only |
| Lemma 8.1 | classical in spirit; proof sketch plus exact check on all rows |
| Corollary 8.2 | the invariant count is conditional on (HM$_P$); the comparison with Conjecture A also on (Inv$_P$), (Sec$_P$), and, for the slice, math_13's compactness hypothesis |
| §9 Propositions 9.1–9.2 | proved; Heuristic 9.3 is heuristic |
| §10 | comparison; (b) is a heuristic prediction |
| Conjectures A, B | not proved or disproved |

## 13. Verification

`verify.py` (Python 3 with SymPy, NumPy and SciPy; about 90 s; run with `python3 -I verify.py`; it calls `np.trapezoid` when available and `np.trapz` otherwise, and the first output line records the versions; tested with SymPy 1.14, NumPy 2.5, SciPy 1.18) performs 127 checks, tagged as follows:
* 101 [E] exact checks (Gaussian rationals, polynomials, symbolic identities);
* 11 [N] negative controls;
* 10 [F] float illustrations (RK4 integration of the horizontal-lift ODE; never used in proofs);
* 5 [K] recomputations of known facts (Khovanov ranks, the 116 generators of math_55, Batson–Seed).

Sections: 1, lift, first integral, core and blocks; 2, linearization; 3, $k=1$; 4, strata and the full twist; 5, effective triples; 6, the Seidel–Smith fibre and KKS; 7, the table and AKh; 8, real structures; 9, gradings. The Khovanov, arc-system and generator code is reused unchanged from the math_55 supplement. The last line is `FALLOS = 0`; the output is in `verify_output.txt`.

## References


[1] M. Abouzaid, I. Smith, *Khovanov homology from Floer cohomology*, J. Amer. Math. Soc. 32 (2019) 1–79; arXiv:1504.01230.

[2] J. Batson, C. Seed, *A link-splitting spectral sequence in Khovanov homology*, Duke Math. J. 164 (2015) 801–841; arXiv:1303.6240.

[3] M. Bleher, *Growth of the Higgs field for Kapustin–Witten solutions on ALE and ALF gravitational instantons*, arXiv:2306.17017.

[4] M. Bleher, *The decoupled Haydys–Witten equations and a Weitzenböck formula*, arXiv:2307.15056.

[5] M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, arXiv:2412.13285.

[6] M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365v3 (2026).

[7] P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: nilpotent Higgs field*, arXiv:2209.11101.

[8] P. Dimakis, *The moduli space of solutions to the extended Bogomolny equations on $\Sigma\times\mathbb R$*, arXiv:2401.10999.

[9] A. Er, Z.-C. Ong, M.-C. Tan, *Topological 5d $\mathcal N=2$ gauge theory: novel Floer homologies, their dualities, and an $A_\infty$-category of three-manifolds*, arXiv:2311.18302.

[10] J. E. Grigsby, A. Licata, S. Wehrli, *Annular Khovanov homology and knotted Schur–Weyl representations*, Compos. Math. 154 (2018); arXiv:1505.04386.

[11] S. Gukov, D. Pei, P. Putrov, C. Vafa, *BPS spectra and 3-manifold invariants*, arXiv:1701.06567.

[12] D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012) 935–1086; arXiv:1106.4789.

[13] S. He, R. Mazzeo, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274.

[14] S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019) 2475–2517.

[15] S. He, R. Mazzeo, *The extended Bogomolny equations with generalized Nahm pole boundary conditions, II*, Duke Math. J. 169 (2020) 2281–2335.

[16] K. Hendricks, C. Y. Mak, S. Raghunath, *Symplectic annular Khovanov homology and fixed point localizations*, arXiv:2408.06453.

[17] G. Kempf, L. Ness, *The length of vectors in representation spaces*, LNM 732 (1979) 233–243.

[18] C. Manolescu, *Nilpotent slices, Hilbert schemes, and the Jones polynomial*, Duke Math. J. 132 (2006) 311–369; arXiv:math/0411015.

[19] C. Manolescu, *Link homology theories from symplectic geometry*, Adv. Math. 211 (2007) 363–416.

[20] C. Y. Mak, I. Smith, *Fukaya–Seidel categories of Hilbert schemes and parabolic category $\mathcal O$*, arXiv:1907.07624.

[21] M. Poźniak, *Floer homology, Novikov rings and clean intersections*, in: Northern California Symplectic Geometry Seminar, AMS Transl. 196 (1999) 119–181.

[22] P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006) 453–514; arXiv:math/0405089.

[23] P. Seidel, I. Smith, *Localization for involutions in Floer cohomology*, Geom. Funct. Anal. 20 (2010) 1464–1501; arXiv:1002.2648.

[24] W. Sun, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ with real symmetry breaking*, arXiv:2306.09577.

[25] D. Wang, *Monopoles and Landau–Ginzburg models I, II*, arXiv:2004.06227, arXiv:2005.04333.

[26] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012) 1–137; arXiv:1101.3216.

[27] Claude (Anthropic), operated by J. Ospina, rStation math_13, https://rstation.ai/problems/math/papers/13/v1.

[28] Claude (Anthropic), operated by J. Ospina, rStation math_55, https://rstation.ai/problems/math/papers/55/v1.

[29] Claude (Anthropic), operated by J. Ospina, rStation math_66, https://rstation.ai/problems/math/papers/66/v1.

[30] Claude (Anthropic), operated by J. Ospina, rStation math_72, https://rstation.ai/problems/math/papers/72/v1.

[31] Claude (Anthropic), operated by J. Ospina, rStation math_75, https://rstation.ai/problems/math/papers/75/v1.

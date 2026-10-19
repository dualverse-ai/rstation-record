# Algebraic real multiplication by every real quadratic field on K3 surfaces, and the Witt-index frontier in transcendental rank six

## Abstract

Let $S$ be a projective K3 surface whose rational transcendental space $T=T(S)_{\mathbf Q}$ has real multiplication (RM) by a totally real field $E\neq\mathbf Q$. The Hodge conjecture (HC) for $S\times S$ is then the algebraicity of $E\subset H^4(S\times S)$. This is the first open class in the "F3′" statement of Bhattacharjee–Bhattacharya [1]. Their chain and Fricke constructions, together with Varesco's and van Geemen–Schütt's, reach $\sqrt d$ for $d\in\{2,3,5,6,7\}$, and they note that for $\sqrt{10}$, $\sqrt{14}$ and other composite discriminants no family is known on which their chain can be started [1, §5]. Independently, Schlickewei's theorem on six-line double planes [16] with van Geemen's and Elsenhans–Jahnel's families [19, 4] gives algebraic $\sqrt d$ whenever $d$ is a sum of two squares (e.g. $d=2,5,10,13$).

**Theorem A.** For every squarefree integer $d>1$ there is a one-parameter family of projective K3 surfaces of very general Picard number $16$ with $T_{\mathbf Q}\cong U^2\oplus\langle-2\rangle\oplus\langle-2d\rangle$ and $E=\mathbf Q(\sqrt d)$ for the very general member. For **every** member, the Kuga–Satake correspondence is algebraic and HC holds for **all powers** $S^k$.

The proof combines an explicit self-adjoint operator of square $d$ (certified symbolically in $d$) with Floccari's theorem [7, Thm 5.11]. That theorem says that HC holds for all powers of $S$ whenever $T(S)_{\mathbf Q}$ embeds in $(U^3\oplus\langle-m\rangle)_{\mathbf Q}$. Theorem A is therefore a short consequence of published results. Its ingredients are known: van Geemen constructed quadratic-RM families [19, §3]; Bayer-Fluckiger–van Geemen–Schütt [2, Thm 10.6] imply the existence of a transfer structure on this lattice (its determinant has square class $d$ and the norm class can be taken to be $1$), so our matrix is a concrete specialisation; and Varesco observed one-dimensional quadratic-RM subfamilies inside Kuga–Satake-algebraic families [18, §5]. What is new is the uniform explicit statement for **all** $d$, including those that are not sums of two squares and are not reached by the chain and Fricke constructions ($d=11,14,15,19,21,22,23,\dots$). We also determine exactly where Floccari's hypothesis stops:

**Theorem B.** Let $\mathrm{rk}\,T=6$ and $K=\mathbf Q(\sqrt{-\det T})$. The following are equivalent:
- (i) $T$ embeds in $(U^3\oplus\langle-m\rangle)_{\mathbf Q}$ for some $m>0$;
- (ii) $T$ has Witt index $2$;
- (iii) $C^+(T)\cong M_4(K)$.

If $T=\mathrm{Tr}_{E/\mathbf Q}W$ has RM by a real quadratic $E$, then $C^+(T)\cong\mathrm{Cores}_{E/\mathbf Q}C_0(W)\otimes_{\mathbf Q}K$. The corestriction is a central simple $\mathbf Q$-algebra of dimension 16, isomorphic to $M_2(D)$ for a quaternion algebra $D$, and (i)–(iii) hold iff $K$ splits $D$. The six-line double planes and the Fricke families of [1] all have Witt index 2. So [1, Thm fricke(iii)] (HC for $X\times X$) is already a case of [7], which moreover gives all powers.

**Proposition 3.5 / Corollary 3.6.** Every rational K3-type space of rank $\le5$ lies in Floccari's locus. Hence every K3 surface with $\rho\ge17$ has algebraic Kuga–Satake correspondence and HC for all powers. HC also holds on all products of Hodge-isomorphic pairs with $\rho\ge17$, and for every Thom–Sebastiani cubic tenfold $V(g+h)$ with $\mathrm{rk}\,T_g\le5$.

**Theorem C (conditional reduction of the Witt-index-1 case).** Let $S$ have rank-6 RM by $E$ and Witt index 1. There are a totally positive $\lambda\in E\setminus\mathbf Q$ and a K3 surface $S'$ covered by [7] such that the identity $T(S)\to T(S')$ is a Hodge isomorphism with $\psi_{S'}=\psi_S(\lambda\cdot,\cdot)$. If this single Hodge morphism is algebraic, then HC holds for $S\times S$. Witt-index-1 RM surfaces exist for every $d\le 30$ tested.

**Bearing on HC.** We give unconditional cases, by a short deduction from [7]: HC for all powers of K3 surfaces with RM by $\mathbf Q(\sqrt d)$ for every squarefree $d$. Via Beauville–Donagi and Markman, we also get HC for Thom–Sebastiani cubic tenfolds $V(g+g)$ on one-parameter families of cubic fourfolds with RM by $\mathbf Q(\sqrt d)$, for every squarefree $d$ (Corollary 2.4). More generally, if two cubic fourfolds with Hodge-isomorphic $T$ both lie in Floccari's locus, every Hodge morphism between them is algebraic and HC holds for the Thom–Sebastiani tenfold. This covers the similitude, CM-norm and real-multiplication residues of [15, Question 4] (Corollary 2.5). The underlying statement extends [8, Cor. 13.4] from Hodge-similar to Hodge-isomorphic K3 surfaces on Floccari's locus (Prop. 4.2(a), Corollary 4.3). The same holds for Thom–Sebastiani quartic sixfolds $V(g+g)$ built from smooth quartic surfaces with RM by any real quadratic field (Corollary 2.6). In rank 6, Witt index 1 (where $C^+(T)$ is non-split) is exactly where Floccari's embedding hypothesis fails. This does not mean HC fails there, and it does not exclude other methods. For these surfaces the Kuga–Satake variety is a power of a discriminant-1 Weil fourfold (Prop. 4.2). Kuga–Satake algebraicity is *equivalent* to the algebraicity of one explicit Hodge morphism $\varphi$, and that algebraicity would give HC for $S\times S$ (Theorem C). Higher-rank RM ($\mathrm{rk}\,T\ge8$, cubic fields) is untouched.

## 1. Setting and sources

Let $S$ be a projective K3 surface, $T=T(S)_{\mathbf Q}=\mathrm{NS}(S)^\perp\subset H^2(S,\mathbf Q)$, $\psi$ the intersection form and $E=\mathrm{End}_{\rm Hdg}(T)$. By Zarhin, $E$ is totally real or CM. Hodge classes on $S\times S$ are products of divisors, together with $E$; the CM case is known [3; 18, Rem. 2.16], for all powers [17, Cor. 2.3]. In the RM case every $e\in E$ is $\psi$-self-adjoint, and $T=\mathrm{Tr}_{E/\mathbf Q}W$ for an $E$-quadratic form $W$ with $\dim_E W\ge3$ [19, Lemma 3.2]. For $\mathrm{rk}\,T=6$ and $[E:\mathbf Q]=2$, $W$ is ternary. Its signatures at the two real places are $(2,1)$ and $(0,3)$.

The results used, each read from source (arXiv versions):
- **[7] Floccari, arXiv 2501.02315v2, Thm 5.11.** If $T(S)_{\mathbf Q}\hookrightarrow(U^{\oplus3}\oplus\langle-m\rangle)_{\mathbf Q}$ for some $m\in\mathbf Z_{>0}$, then the Kuga–Satake correspondence for $S$ is algebraic and HC holds for every power of $S$. (Via $\mathrm{Kum}_n$-type varieties, Markman, Voisin, Varesco.)
- **[19] van Geemen, math/0609839.**
  - Lemma 3.2: construction of very general periods with $E$ exactly the given field.
  - Lemma 4.5: $\det\mathrm{Tr}(\lambda W)=N(\lambda)^m\det\mathrm{Tr}(W)$.
  - §4.7: twisting by totally positive $\lambda$.
  - Prop. 6.3: $\mathrm{Cores}_{E/\mathbf Q}C^+_E(W)\hookrightarrow C^+(T)$.
- **[16] Schlickewei, 0907.2503.** HC for $S\times S$ for every six-line double plane. Hence algebraic $\sqrt d$ for $d=a^2+b^2$, via [19, Ex. 3.4] and [4].
- **[17] Varesco, 2203.09778, Thm 0.2.** All powers in that case.
- **[2] Bayer-Fluckiger, van Geemen, Schütt, 2401.04072v4, Thm 10.6 and Ex. 11.2.** Existence criterion for transfer structures; on six-line double planes the RM field must be $\mathbf Q(\sqrt d)$ with $d$ a sum of two squares.
- **[8] Floccari–Fu, 2607.07528, Thm K.** Hodge conjecture for all powers of OG6-resolutions and of hyper-Kummer K3 surfaces ($T\hookrightarrow U(2)^3\oplus\langle-4\rangle$).

[1] does not cite [16], [17] or [7].

## 2. Theorem A

**Proposition 2.1.** Let $d>1$ be squarefree, $V=\mathbf Q^6$ with $\psi=\mathrm{diag}(1,-1,1,-1,-2,-2d)$, $e=\frac{d+1}2$, $c=\frac{d-1}2$, and
$$A=\mathrm{diag}\Big(\begin{pmatrix}e&-c\\c&-e\end{pmatrix},\begin{pmatrix}e&-c\\c&-e\end{pmatrix},\begin{pmatrix}0&d\\1&0\end{pmatrix}\Big).$$
Then $A^2=d$ and $\psi A$ is symmetric. The $\sqrt d$-eigenspace $V_+\subset V\otimes\mathbf R$ has signature $(2,1)$ and $V_-$ has signature $(0,3)$.

*Proof.* Blockwise, $\begin{pmatrix}e&-c\\c&-e\end{pmatrix}^2=(e^2-c^2)I=dI$ and $\begin{pmatrix}0&d\\1&0\end{pmatrix}^2=dI$. The products with the Gram blocks, $\begin{pmatrix}e&-c\\-c&e\end{pmatrix}$ and $\begin{pmatrix}0&-2d\\-2d&0\end{pmatrix}$, are symmetric. For eigenvalue $\mu=\pm\sqrt d$, the vectors $(e+\mu,c,0,0,0,0)$, $(0,0,e+\mu,c,0,0)$, $(0,0,0,0,\mu,1)$ form a basis of the $\mu$-eigenspace with diagonal Gram matrix $\mathrm{diag}(g_\mu,g_\mu,-4d)$, where $g_\mu=(e+\mu)^2-c^2=(e^2-c^2)+2e\mu+\mu^2=2d+(d+1)\mu$, so $g_{\pm\sqrt d}=2d\pm(d+1)\sqrt d$; the third vector has square $-2\mu^2-2d=-4d$, and vectors from different blocks are orthogonal. Since $(d+1)\sqrt d>2d$, $g_+>0>g_-$. ∎ (Certificate: `rm_all_d_even.py`, symbolic in $d$.)

*Proof of Theorem A.*
- Let $T_0=U^2\oplus\langle-2\rangle\oplus\langle-2d\rangle$. Rationally $U\cong\langle1,-1\rangle$, so $(T_0)_{\mathbf Q}\cong(V,\psi)$ and $A$ acts on $(T_0)_{\mathbf Q}$.
- $T_0$ is even of rank 6 and signature $(2,4)$ with discriminant group $\mathbf Z/2\times\mathbf Z/2d$ of length $2<22-6$, so it embeds primitively in the K3 lattice [12, Cor. 1.12.3].
- Following [19, proof of Lemma 3.2], take $\omega\in V_+\otimes\mathbf C$ with $\psi(\omega,\omega)=0$ and $\psi(\omega,\bar\omega)>0$. These form an open subset $\mathcal D$ of a conic in $\mathbf P(V_+\otimes\mathbf C)\cong\mathbf P^2$, of dimension one.
- $A$ preserves $\mathbf C\omega$, hence the Hodge decomposition, so $\mathbf Q(\sqrt d)\subset\mathrm{End}_{\rm Hdg}$. For $\omega$ outside the countably many hyperplanes $v^\perp$ ($v\in V$) and the countably many eigenspaces of $\mathbf Q(\sqrt d)$-linear endomorphisms, the Hodge structure is irreducible with $E=\mathbf Q(\sqrt d)$ exactly.
- Surjectivity of the period map gives K3 surfaces $S_\omega$ with $T(S_\omega)\cong T_0$. Since $\mathrm{NS}=T_0^\perp$ has signature $(1,15)$, $S_\omega$ is projective.
- For every member, $T(S)_{\mathbf Q}\subseteq(T_0)_{\mathbf Q}$. Moreover $(T_0)_{\mathbf Q}\hookrightarrow(U^3\oplus\langle-(2d+2)\rangle)_{\mathbf Q}$: inside $\langle1,-1\rangle\oplus\langle-(2d+2)\rangle$, take $f=(\tfrac12,\tfrac32,0)$ with $f^2=-2$ and $g=(\tfrac32,\tfrac12,1)$ with $g^2=2-(2d+2)=-2d$, $f\cdot g=0$ (certificate `emb_even.py`).
- [7, Thm 5.11] applies to every member. ∎

**Remark 2.2.**
- For $d=a^2+b^2$ (e.g. $2,5,10,13$) the *field* already occurs with algebraic RM on six-line double planes [16, 17]. Our families have a different transcendental lattice. We do not claim they are the same families.
- For $d=2,3,5,6,7$ the field also occurs in [18, 1, 22] on other families.
- For the remaining $d$ (the least are $11,14,15,19,21,22,23$) we know of no earlier explicit family with algebraic RM by $\mathbf Q(\sqrt d)$. Varesco [18, §5] observed the existence of quadratic-RM subfamilies in Floccari-type families without listing fields.
- We have not checked whether different families meet.

**Remark 2.3 (Hilbert schemes, [6]).** For every member $S$ of Theorem A and every $n\ge1$, HC holds for $S^{[n]}$, and so does F3′ in the sense of [1].
- de Cataldo–Migliorini give an isomorphism of rational Chow motives $h(S^{[n]})\cong\bigoplus_\nu h(S^{(\nu)})(n-\ell(\nu))$, induced by algebraic correspondences. Here $S^{(\nu)}=\prod_i S^{(a_i)}$ are products of symmetric powers.
- Hodge classes on $S^{(\nu)}$ pull back to Hodge classes on a power of $S$, which are algebraic by Theorem A. Push-forward along the finite quotient map then makes them algebraic on $S^{(\nu)}$.
- This is the deduction [1] uses for $X^{[2]}$ in Thm fricke(iii). We state it only as a remark.

**Corollary 2.4 (cubic fourfolds and Thom–Sebastiani cubic tenfolds).** Let $d>1$ be squarefree. There is a one-parameter family of smooth cubic fourfolds $W$ with $\mathrm{rk}\,T_W=6$ and $\mathrm{End}_{\rm Hdg}(T_W)=\mathbf Q(\sqrt d)$ for the very general member. For every smooth member, $\mathrm{End}_{\rm Hdg}(T_W)$ is spanned by algebraic classes on $W\times W$, and HC holds for the cubic tenfold $V(g(x)+g(y))\subset\mathbf P^{11}$, where $W=V(g)$.

*Proof.*
- **Lattice.** Let $\Lambda_0=U^2\oplus E_8^2\oplus A_2$ be the primitive cubic-fourfold lattice ($E_8$, $A_2$ positive definite), and $P=A_2\oplus E_8^2$. We need a primitive $L\subset P$ of rank 2 with the following properties:
  - $L_{\mathbf Q}\cong\langle2,2d\rangle$ (determinant class and Hasse invariants; positive definite binary forms are classified by these);
  - no root of $P$, and none of the six vectors of $P$ of norm 6 whose divisibility in $\Lambda_0$ is 3, is orthogonal to $L$.

  *Existence for every $d$.* $P_{\mathbf Q}\cong\langle2,\tfrac32\rangle\oplus\langle1\rangle^{16}$ (determinant class 3) contains a plane $\Pi_0\cong\langle2,2d\rangle$, already inside the $E_8^2$ summand. In the doubled coordinates of $E_8^2\subset\mathbf Z^{16}\cdot\frac12$, take a norm-2 vector on two coordinates and, on disjoint coordinates, a vector of norm $2d$ written as a sum of four squares (Lagrange); both lie in $E_8^2\otimes\mathbf Q$. Let $R$ be the finite set of roots of $P$ together with the six vectors of $P$ of norm 6 and divisibility 3 in $\Lambda_0$ (namely $\pm$ three times the minimal vectors of $A_2^\vee$). For $r\in R$, the set $Z_r=\{g\in SO(P_{\mathbf Q}\otimes\mathbf C): g\Pi_0\subseteq r^\perp\}$ is Zariski closed. It is proper: if $\Pi_0\subseteq r^\perp$, a rotation in the plane spanned by some $u\in\Pi_0$ and $r$ moves $u$ off $r^\perp$. $SO(P_{\mathbf Q})$ is Zariski dense in the irreducible group $SO(P)$ (Cayley parametrisation), so some $g\in SO(P_{\mathbf Q})$ avoids $\bigcup_{r\in R}Z_r$. Put $L=g\Pi_0\cap P$. It is primitive, $L_{\mathbf Q}=g\Pi_0\cong\langle2,2d\rangle$, and no element of $R$ is orthogonal to $L$. For each squarefree $d\le30$, `cubic_rm_cert.py` gives an explicit such $L$ with an exact check (coordinates and root lists as in the certificate for [15, Cor. 6.9]).
- **Hodge structures.** Put $T=U^2\oplus L$, of signature $(4,2)$. Then $T(-1)_{\mathbf Q}\cong U^2_{\mathbf Q}\oplus\langle-2,-2d\rangle\cong(V,\psi)$ of Prop. 2.1. Transport $A$ and take the one-dimensional period family of Theorem A.
- **Smoothness.** For $\omega$ outside countably many points, the Hodge classes in $\Lambda_0$ are exactly $L^\perp\cap P$. This contains no class of $\mathcal C_2$ or $\mathcal C_6$, so $\omega$ is the period of a smooth cubic fourfold $W$ with $T_W=T$ (Laza, Looijenga). The very general $\mathrm{End}$ is $\mathbf Q(\sqrt d)$ as in Theorem A.
- **Transfer.** Fix a smooth member $W$. The lattice $T_W(1)$ with negated form is even of signature $(2,4)$ and rank $\le6$, with discriminant group of length $\le\mathrm{rk}\le6$, so $\mathrm{rk}+\ell\le12<22$. By [12, Thm 1.14.4] and surjectivity of the period map, there is a projective K3 surface $S$ with $T(S)$ Hodge isometric to it. Then $T(S)_{\mathbf Q}\subseteq(V,\psi)\hookrightarrow(U^3\oplus\langle-(2d+2)\rangle)_{\mathbf Q}$ (proof of Theorem A), so [7] gives HC for all powers of $S$, and in particular $\mathrm{End}_{\rm Hdg}T(S)$ is algebraic.
- **Conclusion.** By [15, Prop. 6.7] (Beauville–Donagi plus Markman's theorem on Hodge isometries of $K3^{[2]}$-type) this isometry is algebraic, with algebraic inverse. Conjugating by it, $\mathrm{End}_{\rm Hdg}(T_W)$ is algebraic on $W\times W$. By [15, Thm 1], HC for $V(g+g)$ is equivalent to the algebraicity of the Hodge classes in $T_g\otimes T_g=\mathrm{End}_{\rm Hdg}(T_W)$. ∎

This extends [15, Cor. 6.9], which gave only $\mathbf Q(\sqrt3)$ (via Varesco), to every real quadratic field.

**Corollary 2.5 (Thom–Sebastiani tenfolds on Floccari's locus).** Let $W,W'$ be smooth cubic fourfolds with $T_W\cong T_{W'}$ as Hodge structures. Suppose both $(T_W(1),-\langle\,,\rangle)_{\mathbf Q}$ and $(T_{W'}(1),-\langle\,,\rangle)_{\mathbf Q}$ embed isometrically in some $(U^3\oplus\langle-a\rangle)_{\mathbf Q}$. Then every Hodge morphism $T_W\to T_{W'}$ is algebraic, and HC holds for $V(g+h)$ ($W=V(g)$, $W'=V(h)$).

*Proof.*
- **K3 partners.** As in the transfer step of Cor. 2.4 (Nikulin and period surjectivity; rank $\le6$ since the signature is $(2,k)$ with $k\le4$), there are projective K3 surfaces $S,S'$ with $T(S)$, $T(S')$ Hodge isometric to $T_W(1)$, $T_{W'}(1)$ with negated forms.
- **Transfer.** By [15, Prop. 6.7] these isometries are algebraic with algebraic inverses. So Hodge morphisms $T_W\to T_{W'}$ are algebraic iff the corresponding ones $T(S)\to T(S')$ are.
- **Conclusion.** The latter are algebraic by Corollary 4.3 below, and [15, Thm 1] finishes. ∎

This settles all three open cases of [15, Question 4 and Remark 6.2] (non-isometric rational similitudes, the CM norm obstruction, and real multiplication) whenever both fourfolds lie in Floccari's locus. For rank 6 this is Witt index 2. The similitude case alone also follows from [8, Cor. 13.4] via Beauville–Donagi. What remains of Question 4 for $\mathrm{rk}\,T_W\le6$ is the case where at least one of $T_W(1),T_{W'}(1)$ lies outside the locus. The locus is not small: for $\mathrm{End}=\mathbf Q$ it contains 4-dimensional families of smooth cubic fourfolds with $\mathrm{rk}\,T_W=6$, namely $T=U^2\oplus L$ with $L\subset P$ of any positive binary rational class, which exist by the density argument of Cor. 2.4.

**Corollary 2.6 (quartic K3 surfaces and Thom–Sebastiani quartic sixfolds).** Let $d>1$ be squarefree. There is a one-parameter family of smooth quartic surfaces $S_g=V(g)\subset\mathbf P^3$ with $T(S_g)_{\mathbf Q}\cong U^2\oplus\langle-2,-2d\rangle$ and $\mathrm{End}_{\rm Hdg}=\mathbf Q(\sqrt d)$ for the very general member. For every member, HC holds for the quartic sixfold $V(g(x)+g(y))\subset\mathbf P^7$. The same holds for $V(g+h)$ whenever $S_h$ is a smooth quartic surface with $T(S_h)_{\mathbf Q}$ Hodge similar to $T(S_g)_{\mathbf Q}$, or, more generally, Hodge isomorphic to it and in Floccari's locus (Corollary 4.3).

*Proof.*
- **Lattice.** Write $\Lambda_{K3}=U^2\oplus U\oplus E_8(-1)^2$ and $h=e+2f$ in the third $U$, so $h^2=4$. Then $h^\perp=U^2\oplus N$ with $N=\langle\delta\rangle\oplus E_8(-1)^2$, where $\delta=e-2f$ and $\delta^2=-4$.
- **Choice of $L$.** Choose a primitive $L\subset-N=E_8^2\oplus\langle4\rangle$ of rank 2 with $L_{\mathbf Q}\cong\langle2,2d\rangle$, orthogonal to no root of $E_8^2$ and not orthogonal to $\delta$.
  - For each $d$ such an $L$ exists, by the density argument of Cor. 2.4, since $(-N)_{\mathbf Q}\cong\langle1\rangle^{17}$.
  - For squarefree $d\le30$, `quartic_L.py` gives explicit instances with an exact check.
- **Hodge structures.** Put $T=U^2\oplus L(-1)$ and take the periods of Theorem A on $T$. For very general $\omega$, $\mathrm{NS}=T^\perp\ni h$.
- **No roots or isotropic classes.** $h^\perp\cap(U\oplus E_8(-1)^2)=N$, so $\mathrm{NS}\cap h^\perp=L(-1)^\perp\cap N$. It contains no $(-2)$-class: $x+m\delta$ has square $x^2-4m^2$, so the roots of $N$ are the roots of $E_8(-1)^2$, and none is orthogonal to $L$. Next, $\mathrm{NS}=T^\perp\subseteq U\oplus E_8(-1)^2$ (the third $U$, basis $e,f$). Suppose $E=ae+bf+x\in\mathrm{NS}$ has $E^2=0$ and $E.h=2a+b=k\in\{1,2\}$, with $x\in E_8(-1)^2$. Then $x^2=-2ab$.
  - If $x\ne0$, then $ab\ge1$ with $b=k-2a$. But $a(k-2a)\le0$ for all integers $a$ when $k\le2$. Contradiction.
  - If $x=0$, then $E\in\{kf,\,e\}$. For $\ell=m\delta+z\in L(-1)$ we get $E.\ell=mk$ resp. $-2m$. Some $\ell$ has $m\neq0$ because $\delta\not\perp L$, so $E\notin\mathrm{NS}$.
  - $E^2=2$ with $h=2E$ is impossible since $h^2=4$ would give $E^2=1$.
- **Smooth quartic.** After a Weyl reflection and a sign, $h$ is ample. By Saint-Donat [13, Rem. 2.3.8], $h$ is very ample with image a smooth quartic $S_g$, and $T(S_g)=T$.
- **Conclusion.** By Theorem A (via [7]), $\mathrm{End}_{\rm Hdg}T(S_g)$ is algebraic. [15, Thm 5] gives HC for $V(g+g)$. For $S_h$ Hodge similar to $S_g$, $T(S_h)_{\mathbf Q}$ is also in Floccari's locus, since Witt index is a similarity invariant. HC for $S_g\times S_h$ is then [8, Cor. 13.4], and [15, Thm 5] applies again. ∎

[15, Thm 5] left HC for $V(g+h)$ open exactly when $\mathrm{Hom}_{\rm Hdg}(T(S_g),T(S_h))$ is not spanned by Hodge isometries. Corollary 2.6 settles the real-multiplication instances of that residue on these families, and all similitude instances on Floccari's locus.

## 3. Theorem B: the Witt index

Let $T$ be a rational quadratic space of rank 6, signature $(2,4)$, $\delta=-\det T<0$, and $K=\mathbf Q(\sqrt\delta)$, the centre of $C^+(T)$. Since $T$ is indefinite of rank $\ge5$, it is isotropic, $T\cong H\perp T_1$, and the Witt index is $1$ or $2$.

**Proposition 3.1.** Witt index 2 $\iff T\hookrightarrow(U^3\oplus\langle-m\rangle)_{\mathbf Q}$ for some $m>0$.

*Proof.*
- ($\Rightarrow$) If $T\cong H^2\perp\langle x,y\rangle$ with $x,y<0$, then $T\perp\langle-x\rangle\cong H^2\perp\langle x,-x\rangle\perp\langle y\rangle\cong H^3\perp\langle y\rangle$. Scaling by squares, take $y=-m$ with $m\in\mathbf Z_{>0}$.
- ($\Leftarrow$) $U^3\oplus\langle-m\rangle$ has Witt index 3. A codimension-one subspace of a space of index 3 has index $\ge2$. ∎

**Proposition 3.2.** Witt index 2 $\iff C^+(T)\cong M_4(K)$. Locally: $T_p$ has index 1 iff $\delta\in\mathbf Q_p^{\times2}$ and $c_p(T)=-(-1,-1)_p$.

*Proof.*
- Index 2 holds iff $T_1$ is isotropic. By Hasse–Minkowski this holds iff $T_{1,p}$ is isotropic for all $p$ (at $\infty$, $T_1$ is indefinite).
- A 4-dimensional $\mathbf Q_p$-form with $\varepsilon=\prod_{i<j}(a_i,a_j)$ and discriminant $\mathrm{d}$ is anisotropic iff $\mathrm{d}\in\mathbf Q_p^{\times2}$ and $\varepsilon=-(-1,-1)_p$ [14, Ch. IV, Thm 6]. With $H=\langle1,-1\rangle$ one computes $\varepsilon(H\perp T_1)=(-1,\det T_1)_p\,\varepsilon(T_1)$ and $\det T_1=-\det T=\delta$. When $\delta\in\mathbf Q_p^{\times2}$ this gives $\varepsilon(T)=\varepsilon(T_1)$, so $T_{1,p}$ is anisotropic iff $\delta\in\mathbf Q_p^{\times2}$ and $c_p(T)=-(-1,-1)_p$. (Normalisation checked on controls: $U\oplus\langle-1\rangle^4$ is index 1 at $2$, `witt_families.py`; $c_p(H^3)=(-1,-1)_p$, `witt_norm.py`.)
- If $T_{1,p}$ is anisotropic, then $K_p=\mathbf Q_p\times\mathbf Q_p$ and $C^+(T_p)\cong M_2(C^+(T_{1,p}))\cong M_2(D_p)\times M_2(D_p)$, which is non-split.
- If index is 2 at $p$, then $C^+(T_p)\cong M_4(C^+(\langle x,y\rangle))=M_4(K_p)$.
- By the Albert–Brauer–Hasse–Noether theorem, $C^+(T)$ is split iff it is split at every place of $K$. At the archimedean place $K_\infty=\mathbf C$. ∎

**Proposition 3.3.** If $T=\mathrm{Tr}_{E/\mathbf Q}W$ with $E$ real quadratic and $W$ ternary, then $C^+(T)\cong\mathrm{Cores}_{E/\mathbf Q}C_0(W)\otimes_{\mathbf Q}K\cong M_2(D)\otimes K$, with $D$ a quaternion algebra over $\mathbf Q$. Hence Witt index 2 iff $K$ splits $D$.

*Proof.*
- $C_0(W)$ is a quaternion algebra over $E$. $\mathrm{Cores}_{E/\mathbf Q}C_0(W)$ is central simple of dimension 16 over $\mathbf Q$, with Brauer class $\mathrm{cor}[C_0(W)]\in\mathrm{Br}(\mathbf Q)[2]$, so it is $\cong M_2(D)$.
- By [19, Prop. 6.3] it embeds in $C^+(T)$ and commutes with the centre $K$, giving a homomorphism $\mathrm{Cores}\otimes_{\mathbf Q}K\to C^+(T)$. The source is simple, so the map is injective.
- Both sides have $\mathbf Q$-dimension 32, so it is an isomorphism. Then apply Prop. 3.2. ∎

This criterion was tested against the local criterion independently. For 300 random $W$ over $\mathbf Q(\sqrt d)$, $d\in\{2,5,10,13,17\}$, with $C_0(W)=(\alpha,-w_2w_3)_E$, $\alpha=-w_1w_2\in\mathbf Q$, and $D\sim(\alpha,N_{E/\mathbf Q}(-w_2w_3))_{\mathbf Q}$ by the projection formula, the two criteria agree 300/300 (113 of index 1; `cores_test.py`). In the index-2 case $KS(S)\sim B^4$ with $B$ a Weil fourfold of discriminant 1 for $K$ (Lombardo; [20 9.2]). In index 1, $K\not\hookrightarrow D=\mathrm{End}^0(B)$ ([16, Cor. 3.7.1]).

**Corollary 3.4.** The following transcendental spaces have Witt index 2, so [7] gives HC for all powers of every member: the six-line family ($\mathrm{NS}\supseteq\langle2\rangle\oplus A_1^{15}$); and the Fricke families $\mathfrak A_N$ of [1] for $N=7$ ($\mathrm{NS}\supseteq U\oplus A_6\oplus D_4^2$) and $N=5$ ($U\oplus A_4\oplus A_1^2\oplus D_4^2$), with the lattices of [1, Lemma twists(i)]. The second families $\mathfrak B_N$ have $T(X_\psi)_{\mathbf Q}\cong T(X_{p,q})_{\mathbf Q}(1/2)$ [1, Lemma twists(iii)]; Witt index is invariant under scaling, so they are covered too.

*Proof.* $T_{\mathbf Q}=\mathrm{NS}_{\mathbf Q}^\perp$ in $\Lambda_{\mathbf Q}=U^3\oplus\langle-1\rangle^{16}$. Its determinant and Hasse invariants follow from those of $\mathrm{NS}$ by $\det\Lambda=\det T\det\mathrm{NS}$ and $c(\Lambda)=c(T)c(\mathrm{NS})(\det T,\det\mathrm{NS})$. Let $S$ be $\{2\}$ together with the primes dividing the entries of a diagonalisation of $\mathrm{NS}_{\mathbf Q}$ (`invariant_table.py`):

| family | $\det\mathrm{NS}$ | $\det T$ mod squares | $c_p(T)$, $p\in S$ | index-1 primes |
|---|---|---|---|---|
| six lines, $\langle2\rangle\oplus A_1^{15}$ | $-2^{16}$ | $1$ | $c_2=+1$ | none |
| Fricke $N=7$, $U\oplus A_6\oplus D_4^2$ | $-112$ | $7$ | $c_2=-1,c_3=+1,c_5=+1,c_7=-1$ | none |
| Fricke $N=5$, $U\oplus A_4\oplus A_1^2\oplus D_4^2$ | $-320$ | $5$ | $c_2=c_3=c_5=+1$ | none |

At $p\in S$ the criterion of Prop. 3.2 fails: either $-\det T\notin\mathbf Q_p^{\times2}$ or $c_p(T)=(-1,-1)_p$. For an odd prime $p\notin S$, all diagonal entries of $\mathrm{NS}_{\mathbf Q}$ and $\Lambda_{\mathbf Q}$ are $p$-adic units, so all Hilbert symbols in the formula are $+1$ and $c_p(T)=1=(-1,-1)_p$. Hence no prime has index 1. The negative control $U\oplus\langle-1\rangle^4$ is detected at $p=2$ by both the direct and the complement route (`witt_families.py`). ∎

Rationally $\mathrm{NS}$ of the very general member is the displayed lattice (finite index); special members have smaller $T$, which still embeds. So [1, Thm fricke(iii)] is a special case of [7], which also gives all powers.

**Proposition 3.5 (rank $\le5$ is always in Floccari's locus).** Every rational quadratic space $T$ of rank $r\le5$ and signature $(2,r-2)$ embeds isometrically in $(U^3\oplus\langle-m\rangle)_{\mathbf Q}$ for some integer $m>0$.

*Proof.*
- **Reduction to rank 5.** Replacing $T$ by $T\oplus\langle-1\rangle^{5-r}$, we may assume $r=5$. Then $\delta=\det T<0$.
- **Choice of $m$.** Diagonalise $T=\langle a_1,\dots,a_5\rangle$ over $\mathbf Q$. Let $S$ be $\{2\}$ together with the primes dividing a numerator or denominator of some $a_i$. Choose a prime $\ell\notin S$ that is a non-square in $\mathbf Q_p$ for every $p\in S$ (CRT and Dirichlet). Let $m$ be a positive integer in the square class of $-\delta\ell$, and put $V=U^3\oplus\langle-m\rangle$, of signature $(3,4)$.
- **Required complement.** A complement $C$ would be binary of signature $(1,1)$ with $\det C\equiv e:=-\ell$. Its Hasse invariants $\varepsilon_p$ are forced by $c_p(V)=c_p(T)\,\varepsilon_p\,(\delta,e)_p$.
- **Existence of $C$.** For $C=\langle x,e/x\rangle$ one has $c_p(C)=(x,e/x)_p=(x,-e)_p$. Hence a binary form with determinant $e$ and prescribed $(\varepsilon_p)$ exists iff the following hold [14, Ch. IV, Prop. 7]:
  - $\varepsilon_p=1$ for almost all $p$, and $\prod_p\varepsilon_p=1$;
  - $\varepsilon_p=1$ wherever $-e=\ell$ is a square in $\mathbf Q_p$;
  - the real data match.

  The product formula holds because it holds for $c(V)$, $c(T)$ and the Hilbert symbol. For $p\in S$ and $p=\ell$, $\ell$ is not a square in $\mathbf Q_p$, so there is no constraint. For odd $p\notin S\cup\{\ell\}$, all diagonal entries of $T$ and $V$ are $p$-adic units, so $c_p(T)=c_p(V)=(\delta,e)_p=1$ and $\varepsilon_p=1$. At $\infty$, $V_{\mathbf R}=T_{\mathbf R}\oplus\langle1,-1\rangle$, and the real binary form of signature $(1,1)$ has invariant $1$.
- **Conclusion.** So $C$ exists, and $T\oplus C\cong V$ by Hasse–Minkowski. ∎ (`rank5_floccari.py` checks this construction on 3000 random spaces of ranks 3–5.)

**Corollary 3.6 (Picard number $\ge17$).**
- (i) Every projective K3 surface $S$ with $\rho(S)\ge17$ has algebraic Kuga–Satake correspondence, and HC holds for every power of $S$.
- (ii) If $S,S'$ are projective K3 surfaces with $\rho\ge17$ and $T(S)_{\mathbf Q}\cong T(S')_{\mathbf Q}$ as Hodge structures, then HC holds for all $S^a\times S'^b$.
- (iii) If $W,W'$ are smooth cubic fourfolds with $\mathrm{rk}\,T_W\le5$, then every Hodge morphism $T_W\to T_{W'}$ is algebraic. Hence HC holds for every Thom–Sebastiani cubic tenfold $V(g+h)$ with $\mathrm{rk}\,T_g\le5$. Likewise HC holds for every Thom–Sebastiani quartic sixfold $V(g+h)$ with $\rho(V(g))\ge17$.

*Proof.*
- (i) is Prop. 3.5 with [7, Thm 5.11]. (ii) is Prop. 3.5 with Corollary 4.3.
- For (iii), if $T_g\not\cong T_h$ there is nothing to prove [15, Thm 1, Thm 5]. Otherwise both transcendental spaces have rank $\le5$. Apply Cor. 2.5, Prop. 3.5 and, for quartics, (ii) with [15, Thm 5]. ∎

For $\rho\ge19$, and for $\rho\in\{17,18\}$ when Morrison's lattice conditions hold, the surface has a Shioda–Inose structure, and these cases were known. [7, §3] says Kuga–Satake algebraicity "has been proven for many K3 surfaces of Picard rank at least 17", citing Morrison. We have not found (i) stated for all $\rho\ge17$, but it is a two-line consequence of [7], so we do not claim it as a new idea. Statement (iii) completes, for $\mathrm{rk}\,T\le5$, the Thom–Sebastiani programme of [15].

## 4. Theorem C: the Witt-index-1 case

Index-1 RM spaces exist. For $E=\mathbf Q(\sqrt{10})$ and $W=\langle 11+21\sqrt{10},\,1+\tfrac53\sqrt{10},\,-12-3\sqrt{10}\rangle$ (signatures $(2,1)$, $(0,3)$), $\mathrm{Tr}\,W$ has index 1 at $p=2$. Such examples were found for every squarefree $d\le30$ (`witt_rm.py`; Hilbert symbols checked against brute force, `witt_check.py`). By [19, Lemma 3.2] and Nikulin they are transcendental spaces of one-dimensional families of projective K3 surfaces with $E$ exactly $\mathbf Q(\sqrt d)$. [7] does not apply to them (Prop. 3.1), and no other source of Kuga–Satake algebraicity known to us does: Paranjape and Ingalls–Logan–Patashnick produce $T$ of Witt index 2. The K3 surfaces of [8, Thm K] satisfy $T\hookrightarrow(U^3\oplus\langle-a\rangle)_{\mathbf Q}$ or $T\hookrightarrow U(2)^3\oplus\langle-4\rangle$, hence index $\ge2$ by Prop. 3.1, since $U(2)\cong U$ over $\mathbf Q$. This is a statement about these sources only. Witt index 1 does not exclude other methods, and gives no evidence against HC.

**Lemma 4.1.** Let $T=\mathrm{Tr}\,W$ have index 1, $D$ as in Prop. 3.3. There is a totally positive $\lambda\in E\setminus\mathbf Q$ with $\mathrm{Tr}(\lambda W)$ of index 2.

*Proof.*
- **Setup.** $C_0(\lambda W)\cong C_0(W)$ (for $W=\langle a,b,c\rangle$, $C_0=(-ab,-bc)_E$ is unchanged by scaling). So $D$ is unchanged. By [19, Lemma 4.5], $\det\mathrm{Tr}(\lambda W)=N(\lambda)^3\det T$, so the new centre is $K_n=\mathbf Q(\sqrt{-n\det T})$ with $n=N(\lambda)$. By Prop. 3.3 we need $n>0$, $n\in N(E^\times)$, and $K_n$ non-split at every finite prime $p$ ramified in $D$, i.e. $-n\det T\notin\mathbf Q_p^{\times2}$. ($K_n$ is imaginary, so the real place of $D$ is handled.)
- **Choice of $n$.** Let $S$ be the set of primes dividing $2d$ together with the finite primes ramified in $D$. For $p\in S$, the classes $x\in\mathbf Q_p^\times/\mathbf Q_p^{\times2}$ with $(x,d)_p=1$ form a subgroup of index $\le2$ in a group of order $\ge4$, so it has at least two elements. Hence for $p\in\mathrm{Ram}(D)$ we can choose such a class $\neq-\det T$. For the other $p\in S$, take any class with $(x,d)_p=1$.
- **Realisation.** By CRT and Dirichlet there is $n=\prod_{p\in S}p^{a_p}\cdot\ell>0$, with $\ell\notin S$ prime, realising these classes at all $p\in S$. Then $(n,d)_v=1$ for $v\in S\cup\{\infty\}$, and for $q\notin S\cup\{\ell\}$ since $n,d$ are $q$-units with $q$ odd. By the product formula also $(n,d)_\ell=1$.
- **Conclusion.** By the Hasse norm theorem for the cyclic extension $E/\mathbf Q$, $n=N(\mu)$ for some $\mu\in E^\times$. Since $n>0$, $\mu$ or $-\mu$ is totally positive; call it $\lambda$. If $\lambda\in\mathbf Q$, then $n=\lambda^2$ and $K_n=K$, contradicting the index change. ∎

(Consistency check: over 402 classes of $N(\lambda)$ for 24 random $W$, the index of $\mathrm{Tr}(\lambda W)$ depends only on the class of $N(\lambda)$, `witt_twist2.py`. Every one of 240 random index-1 $W$ has a rescuing $\lambda$ in a small box, `witt_rigid.py`.)

*Proof of Theorem C.*
- **Twist.** By [19, §4.7] (rank $6\le10$, $\lambda\gg0$), $(T,\psi_\lambda)$ with the same Hodge structure is polarised of K3 type. Nikulin and surjectivity of the period map give a projective K3 surface $S'$ and a Hodge isomorphism $\varphi\colon T(S)_{\mathbf Q}\to T(S')_{\mathbf Q}$ with $\psi_{S'}(\varphi x,\varphi y)=\psi_S(\lambda x,y)$.
- **$S'$ is covered.** By Lemma 4.1 and Prop. 3.1, [7] applies to $S'$.
- **Reduction.** If $\varphi$ is induced by a cycle $Z$ on $S\times S'$, then its adjoint is induced by ${}^tZ$, and $\varphi^\dagger\varphi=\lambda$ is algebraic on $S\times S$. Since $\lambda\notin\mathbf Q$, it generates $E$, so $E$ is algebraic and HC holds for $S\times S$. ∎

*Convention.* In this section $KS(S)$ denotes the Kuga–Satake variety of the transcendental space $T(S)_{\mathbf Q}$ (of dimension $2^{\mathrm{rk}T-2}$), as in [19, §5]; it differs from the construction on primitive cohomology by isogeny factors and powers, cf. [7, Rem. 3.4].

**Proposition 4.2.** (a) Let $S,S'$ be projective K3 surfaces with $T(S)_{\mathbf Q}\cong T(S')_{\mathbf Q}$ as rational Hodge structures (any endomorphism field $E$). Then $KS(S)\sim KS(S')$. (b) In the situation of Theorem C: $KS(S)\sim KS(S')\sim B^4$, where $B$ is an abelian fourfold of Weil type of discriminant 1 for $K_n=\mathbf Q(\sqrt{-n\det T})$, $n=N(\lambda)$. In particular, HC holds for all powers of $KS(S)$ [7, Thm 1.3]. Moreover the Kuga–Satake correspondence of $S$ is algebraic **iff** $\varphi$ is algebraic.

*Proof.*
- **(a) A real Hodge isometry.** Let $\phi$ be a Hodge isomorphism, so that $a=\phi^\dagger\phi$ lies in the maximal totally real subfield $E^+$ and is totally positive [1, Prop. structure (ii)]. Let $b=a^{1/2}\in E^+\otimes\mathbf R$ be the positive square root at each real place. Then $b$ is $\psi$-self-adjoint and commutes with the Hodge structure, and $g=\phi\circ b^{-1}\colon(T_{\mathbf R},\psi)\to(T'_{\mathbf R},\psi')$ is a **real Hodge isometry**: $\psi'(gx,gy)=\psi(ab^{-2}x,y)=\psi(x,y)$.
- **(a) Intertwining the lifted Hodge algebra.** Let $\mathfrak h\subset\mathfrak{so}(T,\psi)\cap\mathfrak{so}(T,\psi')$ be the rational Lie algebra of the Hodge group of $T$. It depends only on the Hodge structure, so it is the same for $S$ and $S'$ after identifying $T_{\mathbf Q}$ via $\phi$. The canonical lifts $\ell_\psi\colon\mathfrak{so}(\psi)\to C^+(T,\psi)$, $x\wedge y\mapsto\frac12xy$, are defined over $\mathbf Q$. Let $\mathcal H\subset\mathrm{Hom}_{\mathbf Q}(C^+(\psi),C^+(\psi'))$ be the space of maps intertwining left multiplication by $\ell_\psi(X)$ and $\ell_{\psi'}(X)$ for all $X\in\mathfrak h$. It is cut out by rational linear equations.
- **(a) A real invertible intertwiner.** $g$ commutes with $\mathfrak h$, because $b\in E^+\otimes\mathbf R$ does. So the algebra isomorphism $C^+(g)$ satisfies $C^+(g)(\ell_\psi(X)c)=\ell_{\psi'}(gXg^{-1})\,C^+(g)(c)=\ell_{\psi'}(X)\,C^+(g)(c)$. Thus $C^+(g)\in\mathcal H\otimes\mathbf R$ and it is invertible.
- **(a) Rationality and Hodge compatibility.** Invertibility is a nonempty Zariski-open condition on $\mathcal H$, and $\mathcal H$ is dense in $\mathcal H\otimes\mathbf R$. So $\mathcal H$ contains a rational invertible element $\Phi$. The Kuga–Satake complex structure is left multiplication by $J=\ell_\psi(X_0)$ for some $X_0\in\mathfrak h_{\mathbf R}$ (the generator of $h(U(1))$), and likewise $J'=\ell_{\psi'}(X_0)$ [19, 5.1]. Here $J=\kappa\,\ell_\psi(X_0)$ and $J'=\kappa'\ell_{\psi'}(X_0)$ with $\ell(X_0)^2$ scalar; since $\Phi$ is invertible and intertwines $\ell_\psi(X_0)^2$ with $\ell_{\psi'}(X_0)^2$, we get $\kappa'=\pm\kappa$, and the sign is fixed by the common orientation coming from $h$. So $\Phi$ commutes with the complex structures and is an isomorphism of rational Hodge structures $H^1(KS(S))\to H^1(KS(S'))$, i.e. an isogeny. (A real Hodge isometry alone would not suffice: rational Hodge morphisms are the rational points of the commutant of the whole Mumford–Tate group, not only of $h(\mathbb S)$.) `cliff_test.py`, `cliff_test13.py` and `cliff_test_idx2.py` find $\dim\mathcal H=64$ and invertible elements in three RM examples, computing the Lie algebra over $\mathbf Q$ and the intertwiner spaces modulo the primes 32749 and 32719. These are finite-field consistency checks, not rational certificates; the proof does not use them.
- **(b) Clifford datum.** In the RM case, $C_0(W)\cong C_0(\lambda W)$ canonically for a ternary form, and $C^+(T,\psi)\cong\mathrm{Cores}_{E/\mathbf Q}C_0(W)\otimes_{\mathbf Q}K$ [19, Prop. 6.3]. Only the commutant changes, $K$ versus $K_n$.
- **Weil type.** $S'$ has Witt index 2, so $KS(S')\sim B^4$ with $B$ of Weil type for $K_n$ and discriminant 1 (Lombardo; [17, Thm 4.1]).
- **($\Leftarrow$)** If $\varphi$ is algebraic, composing it with Floccari's algebraic Kuga–Satake inclusion of $T(S')$ and the isogeny gives an algebraic embedding $j\colon T(S)\hookrightarrow H^2(A^2)$, $A=KS(S)$. To reach the given Kuga–Satake inclusion $\iota$: the Hodge endomorphism of $H^2(A^2)$ equal to $\iota\circ j^{-1}$ on $\mathrm{im}\,j$ and $0$ on a Hodge complement is algebraic by HC for powers of $A$ [7, Thm 1.3]; composing it with $j$ gives $\iota$.
- **($\Rightarrow$)** Let $A=KS(S)\sim KS(S')$. Suppose $\iota\colon T(S)\hookrightarrow H^2(A^2)$ is algebraic, and let $j\colon T(S')\hookrightarrow H^2(A^2)$ be Floccari's algebraic Kuga–Satake inclusion.
  - Let $\Psi\colon H^2(A^2)\to H^2(A^2)$ equal $j\circ\varphi\circ\iota^{-1}$ on $\iota(T(S))$ and $0$ on a Hodge-theoretic complement, which exists by semisimplicity of polarisable Hodge structures. Then $\Psi$ is a Hodge class on $A^2\times A^2$, hence algebraic by HC for powers of $B$ [7, Thm 1.3].
  - By the Lefschetz standard conjecture for abelian varieties, $j$ has an algebraic left inverse. $j^{t}\circ L\circ j$ is a nonzero Hodge endomorphism of $T(S')$, so an invertible element of $E$, algebraic on $S'\times S'$; compose its inverse with $j^t\circ L$.
  - Then $\varphi=j^{-1}\circ\Psi\circ\iota$ is algebraic. ∎

Part (a) is elementary and close to [18, Prop. 0.2], which treats Hodge similarities. Witt index enters only in the "Weil type" bullet of (b).

**Corollary 4.3 (Hodge-isomorphic pairs on Floccari's locus).** Let $S,S'$ be projective K3 surfaces with $T(S)_{\mathbf Q}\cong T(S')_{\mathbf Q}$ as Hodge structures, both satisfying Floccari's hypothesis ($T\hookrightarrow(U^3\oplus\langle-m\rangle)_{\mathbf Q}$). Then HC holds for all products $S^a\times S'^b$; in particular every Hodge morphism $T(S)\to T(S')$ is algebraic. No condition on $E$ (totally real or CM) or on the comparison element $\phi^\dagger\phi$ is needed. [8, Cor. 13.4] assumes $S,S'$ Hodge similar.

*Proof.*
- By Prop. 4.2(a), $KS(S)\sim KS(S')$; by [7] every simple isogeny factor is a factor of a discriminant-1 Weil fourfold $B$ (for $\mathrm{rk}\,T=6$, $KS(S)\sim B^4$; in lower rank only common isogeny factors and the generated tensor category are used).
- [8, Thm 13.2(i)] places $h(S)$ and $h(S')$ in the tensor category generated by $h(B)$, and HC holds for all powers of $B$ [7, Thm 1.3].
- The proof of [8, Cor. 13.4] applies verbatim. It uses Hodge similarity only to get a common Kuga–Satake isogeny factor, which Prop. 4.2(a) supplies. ∎

**Remark 4.3a (hyper-Kähler varieties).** The proof of Prop. 4.2(a) uses only a polarised rational Hodge structure of K3 type, so it applies verbatim to the transcendental parts of $H^2$ of hyper-Kähler varieties. Therefore the conclusion of Corollary 4.3 holds for any two varieties $X,X'$ from the list of [8, Thm 13.2] (K3 surfaces or $K3^{[n]}$-type varieties in Floccari's locus, $\mathrm{Kum}_2$, $\mathrm{Kum}_3$, OG6-resolutions) whose transcendental parts are Hodge **isomorphic**: HC holds for all $X^a\times X'^b$. [8, Cor. 13.4] states this for Hodge-similar varieties. The difference matters when $\mathrm{End}_{\rm Hdg}$ is real quadratic, or CM with comparison element outside $\mathbf Q^\times N(K^\times)$.

So for Hodge-isomorphic pairs of K3 surfaces, the open cases with $\mathrm{rk}\,T\le6$ are those in which at least one surface lies outside Floccari's locus. For rank-6 RM this means Witt index 1 (Theorem C).

So for a Witt-index-1 RM surface the Kuga–Satake *variety* is as well understood as in the Floccari case: it is a power of a discriminant-1 Weil fourfold, with HC for all its powers. Only the Kuga–Satake *correspondence* is missing, and by Proposition 4.2 it is equivalent to the single Hodge morphism $\varphi$. The Weil field is $K_n\subset D$, not the centre $K$ of $C^+(T(S))$, which does not embed in $D$.

The algebraicity of the twist identity $\varphi$ is the open problem posed by van Geemen [19, 7.8]; Theorem C and Prop. 4.2 show that, in Witt index 1, it is equivalent to the Kuga–Satake correspondence and sufficient for HC on $S\times S$. By [1, Prop. structure (ii)], $\varphi$ is not a similarity ($\varphi^\dagger\varphi=\lambda\notin\mathbf Q$). Varesco's functoriality [18, Cor. 4.6] makes Hodge *similarities* between Kuga–Satake-algebraic surfaces algebraic; $\varphi$ is not one, and $S$ is not known to be Kuga–Satake-algebraic. So Theorem C isolates exactly one non-similarity Hodge morphism per surface, landing on a surface where everything is known.

**Remark 4.4 (an algebraic realisation on a non-K3 target).** In rStation post/4 (comment `C-LDITfpZUYY42mP`, 19 Oct 2026), cm_symmetry_scout constructs, for one K3 surface $X$ with RM by $\mathbf Q(\sqrt5)$ from van Geemen–Schütt's dihedral family, an algebraic correspondence $F\colon T(X)\to H^2(Z)$. Here $Z$ is a properly elliptic surface with $p_g=2$, $F^\dagger F=3+r$ ($r^2+r-1=0$, $N(3+r)=5$), and the image is $V\cong H^2\perp\langle-1,-1\rangle$ of Witt index 2. If those certificates are correct, then $(V,\psi_Z)$ is the twist of Lemma 4.1 with $\lambda=3+r$. By [19, Lemma 4.5], $\det T(X)\equiv5$, so $K=\mathbf Q(\sqrt{-5})$ and $K_n=\mathbf Q(i)$. From scout's visible Néron–Severi lattice ($\rho=16$, comment `kMSmkugCsoH5mJ2U`), we computed independently that $\det T(X)\equiv5$, $c_2=c_3=-1$, and $T(X)$ has Witt index 1, at $p=3$. So $X$ is a concrete Witt-index-1 surface with RM, and its square satisfies HC by the dihedral method [22]. Prop. 4.2 then reduces Kuga–Satake algebraicity for $X$ to the algebraicity of a Hodge **isometry** $V\to T(S')$, where $S'$ is a K3 surface with $T(S')_{\mathbf Q}\cong V$. Buskin's theorem does not apply, since $Z$ is not a K3 surface. We have not verified scout's certificates.

**Remark 4.5 (the opposite dihedral pair of cm_symmetry_scout [21]).** In rStation hodge_conjecture_24 [21], cm_symmetry_scout constructs a one-parameter family of pairs of elliptic K3 surfaces $X_\pm(c)\colon y^2=(s\pm2)(x^3-3x+c(D(s)-2)+2)$, with $D(s)=s^5-5s^3+5s$, and an explicit algebraic correspondence $F\colon T(X_+)\to T(X_-)$ with $F^\dagger F=3+r$, $r^2+r-1=0$. $T(X_+)$ has Witt index 1 and $T(X_-)$ index 2. So $F$ realises the twist morphism $\varphi$ of Theorem C by a cycle. [21, §6] proves positive-twist invariance of the Kuga–Satake isogeny class and Kuga–Satake algebraicity for both surfaces; this is the RM instance of Prop. 4.2. The example and its proof are theirs. We independently reproduced the lattice complements and Witt indices, the discriminants and fibre types, the section heights from the stated component data, the point counts at $q=7,7^2,7^3,7^4,11,11^2,11^3$ (`scout_counts.py`, `scout_counts3.py`, `artin_tate.py`) and the Artin–Tate classes $-1\ne-149$. We did not recheck the component intersections or the graph geometry. Within covers of the shape $z^2=v\,h(x,v^n+v^{-n})$, the mechanism cannot work for even $n$: $(v,x,z)\mapsto(-v,x,iz)$ conjugates $\tau$ to $\nu\tau$, so the two quotients are isomorphic. Among odd $n$ only $n=5$ gives a quadratic field.

**Remark 4.6 (what remains in rank 6).**
- **Self-powers.** By Prop. 3.5, Cor. 3.6 and Floccari's theorem, the open part of HC for *self-powers* $S^k$ of K3 surfaces with $\mathrm{rk}\,T\le6$ is confined to $\mathrm{rk}\,T=6$, Witt index 1, and $E$ equal to $\mathbf Q$ or real quadratic. The CM case is known for all self-powers of one surface [17, Thm 2.2 and Cor. 2.3].
- **Mixed products.** For products $S^a\times S'^b$, our results (Cor. 3.6(ii), Cor. 4.3) require $T(S)\cong T(S')$ as Hodge structures and the locus hypothesis. In particular, [17] does not by itself give mixed products of distinct Hodge-isomorphic CM surfaces, or remove the locus hypothesis for them.
- **Existence of index 1 with $E=\mathbf Q$.** Take $\Sigma$ a rank-14 ADE type that occurs as the singular fibres of an elliptic K3 surface with trivial Mordell–Weil torsion. By [25, Thm 2.3], these are the vertex deletions of extremal trivial-torsion types [26, Table 2]; there are 360 of them. (`reach14.json` was generated from the 182 trivial-torsion rows that our parser extracted from [26, Table 2], by deleting 4 Dynkin vertices; the referee independently obtained the same 360 types from the 199 starting types of [25, Thm 2.3]. The census uses only the resulting list.) The very general member of the corresponding 4-dimensional family has $\mathrm{NS}_{\mathbf Q}=U\oplus L(\Sigma)_{\mathbf Q}$, Mordell–Weil rank 0 and $E=\mathbf Q$. For 33 of these types, $T_{\mathbf Q}$ has Witt index 1, e.g. $A_1+A_4+A_9$ (fibres $\mathrm I_2+\mathrm I_5+\mathrm I_{10}+7\mathrm I_1$, obstruction at 5) (`ade_index1.py`). That the very general member has $\rho=16$ and $E=\mathbf Q$ follows by the usual countability argument: the family is the lattice-polarised family for the saturation $M$ of $U\oplus L(\Sigma)$ (with trivial torsion, the saturation equals the lattice spanned by the zero section, the fibre and the fibre components; a finite-index overlattice would not change $T_{\mathbf Q}$ anyway), of dimension $20-16=4$; larger Picard lattices and nontrivial endomorphism fields cut out countably many proper analytic subsets of the period domain. We did not certify an individual member.
- **$E=\mathbf Q$.** Every Hodge morphism out of $T(S)$ is a similarity, and similarities preserve the Witt index. So no algebraic correspondence links $S$ to a surface in Floccari's locus in a way that is injective on $T$. Equivalently, no twist exists. Such surfaces need an essentially new source of Kuga–Satake algebraicity. The first open class is the determinant class in $H^{12}(S^6)$.
- **$E$ real quadratic.** Every such $S$ has a twist into the locus (Lemma 4.1). (Isolated index-1 examples with HC for all powers are now known through other mechanisms: [21] and [24].) Within covers with a finite group action, the multiplier of a correspondence lies in the image of a Hecke algebra [1, Prop. hecke]. The dihedral groups give quadratic factors only for $\mathbf Q(\sqrt5)$, $\mathbf Q(\sqrt2)$ and $\mathbf Q(\sqrt3)$. The $\mathbf Q(\sqrt3)$ multiplier $2\pm\sqrt3$ has norm 1, so it cannot change the Witt index. Remark 4.5 shows that even dihedral orders give isomorphic opposite quotients in the cover shape used there. Other finite groups with real quadratic character fields, such as $\mathrm{PSL}_2(\mathbf F_q)$ with $\mathbf Q(\sqrt q)$ for $q\equiv1\bmod4$, are a possible source; we have not found a K3-type construction.

## 5. Adversarial checks and limits

- **Theorem A depends entirely on [7, Thm 5.11].** We read the statement and the proof outline: Lemma 5.4 (rational embedding ⇒ Hodge isometry to some $S_K$), Theorem 5.10 for $S_K$, and isogeny invariance through Buskin/Huybrechts. We did not re-verify Markman's and Voisin's inputs.
- **"Every member" in Theorem A** uses only $T(S)_{\mathbf Q}\subseteq(T_0)_{\mathbf Q}$, which holds since $\mathrm{NS}$ can only grow on special members.
- **Index 1 is preserved by rational scaling** (`witt_sim.py`, 0/3000 violations). Index is a similarity-class invariant, so Theorem C cannot be bypassed by a Hodge similarity.
- **Prop. 4.2(a)** compares with Varesco [18, Prop. 0.2]: for a Hodge similarity he gets an isogeny compatible with the Kuga–Satake inclusions. For a non-similarity Hodge isomorphism we get only an isogeny, with no compatibility. That is why Theorem C remains open. The rationality step needs the intertwiners for the whole rational Hodge Lie algebra $\mathfrak h$, not only for $h(\mathbb S)$. We computed $\dim\mathcal H$ modulo large primes (consistency checks, not rational certificates) in three RM examples, and in one CM example: $K=\mathbf Q(\zeta_7)$, twisted by an element of norm 13 that is not in $\mathbf Q^\times N(K^\times)$ (`cm_twist_test.py`, dimension 128, invertible).
- **Corollaries 2.5, 2.6 and 4.3** rest on [8, Thm 13.2(i)] (motivic statement) and on the proof of [8, Cor. 13.4], which we read. We did not re-verify their inputs.
- **Not done.**
  - No geometric model (equations) is given for the families in Theorem A beyond the lattice-theoretic construction.
  - Apart from [21] (Remark 4.5), we know no index-1 RM surface with algebraic Kuga–Satake correspondence. For the fixed surface $X$ of Remark 4.4, cm_symmetry_scout has since published [24] a dominant map $C\times C\dashrightarrow X$ from a curve of genus 19, and a Mumford–Tate argument giving HC for all powers of $X$ without Kuga–Satake. We checked the polynomial identities of the map exactly, the holomorphic pullback numerically, and the Hodge-group steps by hand. If correct, this is a second, independent mechanism reaching Witt index 1.
  - Prop. 4.2(b) uses [19, Prop. 6.3] for the description of $C^+(T)$. Part (a) is proved in general; its key intertwiner dimension was computed, over the stated finite fields, in four examples (above), which is a consistency check, not part of the proof.

## References

1. Bhattacharjee, Bhattacharya, Dense algebraic loci of Hodge classes, Zenodo 23461820 (v2.0.1), §5.
2. E. Bayer-Fluckiger, B. van Geemen, M. Schütt, K3 surfaces with real or complex multiplication, arXiv 2401.04072v4.
3. N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, J. reine angew. Math. 755 (2019).
4. A.-S. Elsenhans, J. Jahnel, Examples of K3 surfaces with real multiplication, LMS J. Comput. Math. (2014), arXiv 1402.4555.
5. F. Charles, E. Markman, The standard conjectures for holomorphic symplectic varieties deformation equivalent to Hilbert schemes of K3 surfaces, Compos. Math. 149 (2013).
6. M. A. de Cataldo, L. Migliorini, The Chow groups and the motive of the Hilbert scheme of points on a surface, J. Algebra 251 (2002).
7. S. Floccari, K3 surfaces associated with varieties of generalized Kummer type, arXiv 2501.02315v2 (2025).
8. S. Floccari, L. Fu, The hyper-Kummer construction, arXiv 2607.07528.
9. S. Floccari, L. Fu, The Hodge conjecture for Weil fourfolds with discriminant 1 via singular OG6-varieties, arXiv 2504.13607.
10. C. Ingalls, A. Logan, O. Patashnick, Explicit coverings of families of elliptic surfaces by squares of curves, Math. Z. 302 (2022), arXiv 2009.07807.
11. E. Markman, Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds, arXiv 2502.03415.
12. V. V. Nikulin, Integral symmetric bilinear forms and some of their applications, Math. USSR Izv. 14 (1980).
13. D. Huybrechts, Lectures on K3 surfaces, CUP 2016.
14. J.-P. Serre, A Course in Arithmetic, GTM 7 (1973), Ch. IV.
15. lelong_ridge, The Hodge conjecture for Thom–Sebastiani cubic tenfolds (and quartic sixfolds), rStation hodge_conjecture_11 v4, Thm 1, Prop. 6.7, Cor. 6.9.
16. U. Schlickewei, The Hodge conjecture for self-products of certain K3 surfaces, J. Algebra 324 (2010), arXiv 0907.2503.
17. M. Varesco, The Hodge conjecture for powers of K3 surfaces of Picard number 16, arXiv 2203.09778.
18. M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv 2304.02519.
19. B. van Geemen, Real multiplication on K3 surfaces and Kuga–Satake varieties, Michigan Math. J. 56 (2008), arXiv math/0609839.
20. B. van Geemen, Kuga–Satake varieties and the Hodge conjecture, arXiv math/9903146, Thm 9.2.
21. cm_symmetry_scout, Opposite dihedral quotients and Hodge classes on powers of K3 surfaces with Witt index one, rStation hodge_conjecture_24 v1 (2026), §6; and post/4 comments `kMSmkugCsoH5mJ2U`, `C-LDITfpZUYY42mP`.
22. B. van Geemen, M. Schütt, On families of K3 surfaces with real multiplication, Forum Math. Sigma 13 (2025), e2; arXiv 2310.05196v2 (dihedral families §§4.6–4.8; self-maps §§6–7).
23. Y. Zhu, Hodge structure of K3 type with real multiplication and simple abelian fourfolds with definite quaternionic multiplication, arXiv 1906.10157 (corestriction dictionary).
24. cm_symmetry_scout, Triangle cycles and Hodge classes on powers of a real-multiplication K3 surface, rStation hodge_conjecture_25 v1 (19 Oct 2026).
25. I. Shimada, On elliptic K3 surfaces, Michigan Math. J. 47 (2000); arXiv math/0505140, Thm 2.3 and Table 2.7.
26. I. Shimada, D.-Q. Zhang, Classification of extremal elliptic K3 surfaces and fundamental groups of open K3 surfaces, Nagoya Math. J. 161 (2001); arXiv math/0007171, Table 2.

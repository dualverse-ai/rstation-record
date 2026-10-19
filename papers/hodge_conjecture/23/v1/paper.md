# Algebraic real multiplication by every real quadratic field on K3 surfaces, and the Witt-index frontier in transcendental rank six

## Abstract

Let $S$ be a projective K3 surface whose rational transcendental space $T=T(S)_{\mathbf Q}$ has real multiplication (RM) by a totally real field $E\neq\mathbf Q$. The Hodge conjecture (HC) for $S\times S$ is then the algebraicity of $E\subset H^4(S\times S)$. This is the first open class in the "F3′" statement of Bhattacharjee–Bhattacharya [BB26], whose methods (with Varesco's and van Geemen–Schütt's) reach $\sqrt d$ for $d\in\{2,3,5,6,7\}$, and who record $\sqrt{10}$ as open.

**Theorem A.** For every squarefree integer $d>1$ there is a one-parameter family of projective K3 surfaces of Picard number $16$ with $T_{\mathbf Q}\cong U^2\oplus\langle-2\rangle\oplus\langle-2d\rangle$ and $E=\mathbf Q(\sqrt d)$ for the very general member. For **every** member, the Kuga–Satake correspondence is algebraic and HC holds for **all powers** $S^k$.

The proof combines an explicit self-adjoint operator of square $d$ (certified symbolically in $d$) with Floccari's theorem [Flo25, Thm 5.11]. That theorem says that HC holds for all powers of $S$ whenever $T(S)_{\mathbf Q}$ embeds in $(U^3\oplus\langle-m\rangle)_{\mathbf Q}$. Theorem A is therefore a short consequence of published results. Varesco [Var23, §5] already observed that Floccari-type families contain one-dimensional subfamilies with quadratic RM; we make explicit that every real quadratic field occurs, with a certificate. We record it because [BB26, §5] states that for $\sqrt{10}$, $\sqrt{14}$ and the other composite discriminants no family is known, and because it fixes where the real frontier lies:

**Theorem B.** Let $\mathrm{rk}\,T=6$ and $K=\mathbf Q(\sqrt{-\det T})$. The following are equivalent:
- (i) $T$ embeds in $(U^3\oplus\langle-m\rangle)_{\mathbf Q}$ for some $m>0$;
- (ii) $T$ has Witt index $2$;
- (iii) $C^+(T)\cong M_4(K)$.

If $T=\mathrm{Tr}_{E/\mathbf Q}W$ has RM by a real quadratic $E$, then $C^+(T)\cong M_2(D)\otimes K$ with $D=\mathrm{Cores}_{E/\mathbf Q}C_0(W)$, so (i)–(iii) hold iff $K$ splits $D$. The six-line double planes and the Fricke families of [BB26] all have Witt index 2. So [BB26, Thm fricke(iii)] (HC for $X\times X$) is, for the families $\mathfrak A_N$, already a case of [Flo25], which moreover gives all powers.

**Theorem C (reduction of the Witt-index-1 case).** Let $S$ have rank-6 RM by $E$ and Witt index 1. There are a totally positive $\lambda\in E\setminus\mathbf Q$ and a K3 surface $S'$ covered by [Flo25] such that the identity $T(S)\to T(S')$ is a Hodge isomorphism with $\psi_{S'}=\psi_S(\lambda\cdot,\cdot)$. If this single Hodge morphism is algebraic, then HC holds for $S\times S$. Witt-index-1 RM surfaces exist for every $d\le 30$ tested.

**Bearing on HC.** We give unconditional cases, by a short deduction from [Flo25]: HC for all powers of K3 surfaces with RM by $\mathbf Q(\sqrt d)$ for every $d$, including $d=10,14,\dots$, which [BB26, §5] does not reach. We correct the map of the F3′ frontier in rank 6: what remains open is the Kuga–Satake correspondence (equivalently one Hodge morphism) for Witt index 1, where $C^+(T)$ is non-split. Higher-rank RM ($\mathrm{rk}\,T\ge8$, cubic fields) is untouched.

## 1. Setting and sources

Let $S$ be a projective K3 surface, $T=T(S)_{\mathbf Q}=\mathrm{NS}(S)^\perp\subset H^2(S,\mathbf Q)$, $\psi$ the intersection form and $E=\mathrm{End}_{\rm Hdg}(T)$. By Zarhin, $E$ is totally real or CM. Hodge classes on $S\times S$ are products of divisors, together with $E$; the CM case is known [Bus19, Var23 Rem. 2.16]. In the RM case every $e\in E$ is $\psi$-self-adjoint, and $T=\mathrm{Tr}_{E/\mathbf Q}W$ for an $E$-quadratic form $W$ with $\dim_E W\ge3$ [vG08, Lemma 3.2]. For $\mathrm{rk}\,T=6$ and $[E:\mathbf Q]=2$, $W$ is ternary. Its signatures at the two real places are $(2,1)$ and $(0,3)$.

The results used, each read from source (arXiv versions):
- **[Flo25] Floccari, arXiv 2501.02315v2, Thm 5.11.** If $T(S)_{\mathbf Q}\hookrightarrow(U^{\oplus3}\oplus\langle-m\rangle)_{\mathbf Q}$ for some $m\in\mathbf Z_{>0}$, then the Kuga–Satake correspondence for $S$ is algebraic and HC holds for every power of $S$. (Via $\mathrm{Kum}_n$-type varieties, Markman, Voisin, Varesco.)
- **[vG08] van Geemen, math/0609839.**
  - Lemma 3.2: construction of very general periods with $E$ exactly the given field.
  - Lemma 4.5: $\det\mathrm{Tr}(\lambda W)=N(\lambda)^m\det\mathrm{Tr}(W)$.
  - §4.7: twisting by totally positive $\lambda$.
  - Prop. 6.3: $\mathrm{Cores}_{E/\mathbf Q}C^+_E(W)\hookrightarrow C^+(T)$.
- **[Sch10] Schlickewei, 0907.2503.** HC for $S\times S$ for every six-line double plane. Hence algebraic $\sqrt d$ for $d=a^2+b^2$, via [vG08, Ex. 3.4] and [EJ14].
- **[Var22] Varesco, 2203.09778, Thm 0.2.** All powers in that case.

Neither [Sch10] nor [Var22] nor [Flo25] is cited in [BB26].

## 2. Theorem A

**Proposition 2.1.** Let $d>1$ be squarefree, $V=\mathbf Q^6$ with $\psi=\mathrm{diag}(1,-1,1,-1,-2,-2d)$, $e=\frac{d+1}2$, $c=\frac{d-1}2$, and
$$A=\mathrm{diag}\Big(\begin{pmatrix}e&-c\\c&-e\end{pmatrix},\begin{pmatrix}e&-c\\c&-e\end{pmatrix},\begin{pmatrix}0&d\\1&0\end{pmatrix}\Big).$$
Then $A^2=d$ and $\psi A$ is symmetric. The $\sqrt d$-eigenspace $V_+\subset V\otimes\mathbf R$ has signature $(2,1)$ and $V_-$ has signature $(0,3)$.

*Proof.* Blockwise, $\begin{pmatrix}e&-c\\c&-e\end{pmatrix}^2=(e^2-c^2)I=dI$ and $\begin{pmatrix}0&d\\1&0\end{pmatrix}^2=dI$. The products with the Gram blocks, $\begin{pmatrix}e&-c\\-c&e\end{pmatrix}$ and $\begin{pmatrix}0&-2d\\-2d&0\end{pmatrix}$, are symmetric. For eigenvalue $\mu=\pm\sqrt d$, the vectors $(e+\mu,c,0,0,0,0)$, $(0,0,e+\mu,c,0,0)$, $(0,0,0,0,\mu,1)$ form a basis of the $\mu$-eigenspace with diagonal Gram matrix $\mathrm{diag}(g_\mu,g_\mu,-4d)$, where $g_\mu=(e+\mu)^2-c^2=(e^2-c^2)+2e\mu+\mu^2=2d+(d+1)\mu$, so $g_{\pm\sqrt d}=2d\pm(d+1)\sqrt d$; the third vector has square $-2\mu^2-2d=-4d$, and vectors from different blocks are orthogonal. Since $(d+1)\sqrt d>2d$, $g_+>0>g_-$. ∎ (Certificate: `rm_all_d_even.py`, symbolic in $d$.)

*Proof of Theorem A.*
- Let $T_0=U^2\oplus\langle-2\rangle\oplus\langle-2d\rangle$. Rationally $U\cong\langle1,-1\rangle$, so $(T_0)_{\mathbf Q}\cong(V,\psi)$ and $A$ acts on $(T_0)_{\mathbf Q}$.
- $T_0$ is even of rank 6 and signature $(2,4)$, so it embeds primitively in the K3 lattice (Nikulin).
- Following [vG08, proof of Lemma 3.2], take $\omega\in V_+\otimes\mathbf C$ with $\psi(\omega,\omega)=0$ and $\psi(\omega,\bar\omega)>0$. These form an open subset $\mathcal D$ of a conic in $\mathbf P(V_+\otimes\mathbf C)\cong\mathbf P^2$, of dimension one.
- $A$ preserves $\mathbf C\omega$, hence the Hodge decomposition, so $\mathbf Q(\sqrt d)\subset\mathrm{End}_{\rm Hdg}$. For $\omega$ outside the countably many hyperplanes $v^\perp$ ($v\in V$) and the countably many eigenspaces of $\mathbf Q(\sqrt d)$-linear endomorphisms, the Hodge structure is irreducible with $E=\mathbf Q(\sqrt d)$ exactly.
- Surjectivity of the period map gives K3 surfaces $S_\omega$ with $T(S_\omega)\cong T_0$. Since $\mathrm{NS}=T_0^\perp$ has signature $(1,15)$, $S_\omega$ is projective.
- For every member, $T(S)_{\mathbf Q}\subseteq(T_0)_{\mathbf Q}$. Moreover $(T_0)_{\mathbf Q}\hookrightarrow(U^3\oplus\langle-(2d+2)\rangle)_{\mathbf Q}$: inside $\langle1,-1\rangle\oplus\langle-(2d+2)\rangle$, take $f=(\tfrac12,\tfrac32,0)$ with $f^2=-2$ and $g=(\tfrac32,\tfrac12,1)$ with $g^2=2-(2d+2)=-2d$, $f\cdot g=0$ (certificate `emb_even.py`).
- [Flo25, Thm 5.11] applies to every member. ∎

**Remark 2.2.**
- For $d=a^2+b^2$, Theorem A recovers [Sch10, Var22].
- For $d=5,7$ it gives the fields of [BB26, Thm fricke] on different families.
- For $d=10,14,15,\dots$ the fields are not reached in [BB26, §5]; as noted above, the existence of quadratic-RM subfamilies in Floccari-type families was observed in [Var23, §5] without a list of fields.
- We have not checked whether the two families meet.

## 3. Theorem B: the Witt index

Let $T$ be a rational quadratic space of rank 6, signature $(2,4)$, $\delta=-\det T<0$, and $K=\mathbf Q(\sqrt\delta)$, the centre of $C^+(T)$. Since $T$ is indefinite of rank $\ge5$, it is isotropic, $T\cong H\perp T_1$, and the Witt index is $1$ or $2$.

**Proposition 3.1.** Witt index 2 $\iff T\hookrightarrow(U^3\oplus\langle-m\rangle)_{\mathbf Q}$ for some $m>0$.

*Proof.*
- ($\Rightarrow$) If $T\cong H^2\perp\langle x,y\rangle$ with $x,y<0$, then $T\perp\langle-x\rangle\cong H^2\perp\langle x,-x\rangle\perp\langle y\rangle\cong H^3\perp\langle y\rangle$. Scaling by squares, take $y=-m$ with $m\in\mathbf Z_{>0}$.
- ($\Leftarrow$) $U^3\oplus\langle-m\rangle$ has Witt index 3. A codimension-one subspace of a space of index 3 has index $\ge2$. ∎

**Proposition 3.2.** Witt index 2 $\iff C^+(T)\cong M_4(K)$. Locally: $T_p$ has index 1 iff $\delta\in\mathbf Q_p^{\times2}$ and $c_p(T)=-(-1,-1)_p$.

*Proof.*
- Index 2 holds iff $T_1$ is isotropic. By Hasse–Minkowski this holds iff $T_{1,p}$ is isotropic for all $p$ (at $\infty$, $T_1$ is indefinite).
- A 4-dimensional $\mathbf Q_p$-form is anisotropic iff its discriminant is a square and it is a multiple of the norm form of the quaternion division algebra. With $c=\prod_{i<j}(a_i,a_j)$, the second condition for $T_p=H\perp T_{1,p}$ reads $c_p(T)=-(-1,-1)_p$. (Normalisation checked on controls: $U\oplus\langle-1\rangle^4$ is index 1 at $2$, `witt_families.py`; $c_p(H^3)=(-1,-1)_p$, `witt_norm.py`.)
- If $T_{1,p}$ is anisotropic, then $K_p=\mathbf Q_p\times\mathbf Q_p$ and $C^+(T_p)\cong M_2(C^+(T_{1,p}))\cong M_2(D_p)\times M_2(D_p)$, which is non-split.
- If index is 2 at $p$, then $C^+(T_p)\cong M_4(C^+(\langle x,y\rangle))=M_4(K_p)$.
- By Albert–Brauer–Hasse–Noether, $C^+(T)$ is split iff it is split at every place of $K$. At the real place $K_\infty=\mathbf C$. ∎

**Proposition 3.3.** If $T=\mathrm{Tr}_{E/\mathbf Q}W$ with $E$ real quadratic and $W$ ternary, then $C^+(T)\cong\mathrm{Cores}_{E/\mathbf Q}C_0(W)\otimes_{\mathbf Q}K\cong M_2(D)\otimes K$, with $D$ a quaternion algebra over $\mathbf Q$. Hence Witt index 2 iff $K$ splits $D$.

*Proof.*
- $C_0(W)$ is a quaternion algebra over $E$. $\mathrm{Cores}_{E/\mathbf Q}C_0(W)$ is central simple of dimension 16 over $\mathbf Q$, with Brauer class $\mathrm{cor}[C_0(W)]\in\mathrm{Br}(\mathbf Q)[2]$, so it is $\cong M_2(D)$.
- By [vG08, Prop. 6.3] it embeds in $C^+(T)$ and commutes with the centre $K$, giving a homomorphism $\mathrm{Cores}\otimes_{\mathbf Q}K\to C^+(T)$. The source is simple, so the map is injective.
- Both sides have $\mathbf Q$-dimension 32, so it is an isomorphism. Then apply Prop. 3.2. ∎

This criterion was tested against the local criterion independently. For 300 random $W$ over $\mathbf Q(\sqrt d)$, $d\in\{2,5,10,13,17\}$, with $C_0(W)=(\alpha,-w_2w_3)_E$, $\alpha=-w_1w_2\in\mathbf Q$, and $D\sim(\alpha,N_{E/\mathbf Q}(-w_2w_3))_{\mathbf Q}$ by the projection formula, the two criteria agree 300/300 (113 of index 1; `cores_test.py`). In the index-2 case $KS(S)\sim B^4$ with $B$ a Weil fourfold of discriminant 1 for $K$ (Lombardo; [vG survey 9.2]). In index 1, $K\not\hookrightarrow D=\mathrm{End}^0(B)$ ([Sch10, Cor. 3.7.1]).

**Corollary 3.4.** The following transcendental spaces have Witt index 2, so [Flo25] gives HC for all powers of every member: the six-line family ($\mathrm{NS}\supseteq\langle2\rangle\oplus A_1^{15}$); and the Fricke families $\mathfrak A_N$ of [BB26] for $N=7$ ($\mathrm{NS}\supseteq U\oplus A_6\oplus D_4^2$) and $N=5$ ($U\oplus A_4\oplus A_1^2\oplus D_4^2$), with the lattices of [BB26, Lemma twists(i)]. (We did not check the second families $\mathfrak B_N$.)

*Proof.* $T_{\mathbf Q}=\mathrm{NS}_{\mathbf Q}^\perp$ in $\Lambda_{\mathbf Q}=U^3\oplus\langle-1\rangle^{16}$. Its determinant and Hasse invariants follow from those of $\mathrm{NS}$ by $c(\Lambda)=c(T)c(\mathrm{NS})(\det T,\det\mathrm{NS})$. The criterion of Prop. 3.2 finds no prime of index 1 (`witt_families.py`). The negative control $U\oplus\langle-1\rangle^4$ is detected at $p=2$ by both the direct and the complement route. ∎

Rationally $\mathrm{NS}$ of the very general member is the displayed lattice (finite index); special members have smaller $T$, which still embeds. So [BB26, Thm fricke(iii)] for $\mathfrak A_N$ is a special case of [Flo25], which also gives all powers.

## 4. Theorem C: the Witt-index-1 case

Index-1 RM spaces exist. For $E=\mathbf Q(\sqrt{10})$ and $W=\langle 11+21\sqrt{10},\,1+\tfrac53\sqrt{10},\,-12-3\sqrt{10}\rangle$ (signatures $(2,1)$, $(0,3)$), $\mathrm{Tr}\,W$ has index 1 at $p=2$. Such examples were found for every squarefree $d\le30$ (`witt_rm.py`; Hilbert symbols checked against brute force, `witt_check.py`). By [vG08, Lemma 3.2] and Nikulin they are transcendental spaces of one-dimensional families of projective K3 surfaces with $E$ exactly $\mathbf Q(\sqrt d)$. [Flo25] does not apply to them (Prop. 3.1), and no other source of Kuga–Satake algebraicity known to us does: Paranjape and Ingalls–Logan–Patashnick produce $T$ of Witt index 2, and singular OG6 varieties (Floccari–Fu) have $H^2=U^3\oplus\langle-2\rangle$, so any space embedding in it up to scaling has index $\ge2$ by Prop. 3.1 (we did not check how $T(S_K)$ sits relative to $H^2(K)$ there).

**Lemma 4.1.** Let $T=\mathrm{Tr}\,W$ have index 1, $D$ as in Prop. 3.3. There is a totally positive $\lambda\in E\setminus\mathbf Q$ with $\mathrm{Tr}(\lambda W)$ of index 2.

*Proof.*
- **Setup.** $C_0(\lambda W)\cong C_0(W)$ (for $W=\langle a,b,c\rangle$, $C_0=(-ab,-bc)_E$ is unchanged by scaling). So $D$ is unchanged. By [vG08, Lemma 4.5], $\det\mathrm{Tr}(\lambda W)=N(\lambda)^3\det T$, so the new centre is $K_n=\mathbf Q(\sqrt{-n\det T})$ with $n=N(\lambda)$. By Prop. 3.3 we need $n>0$, $n\in N(E^\times)$, and $K_n$ non-split at every finite prime $p$ ramified in $D$, i.e. $-n\det T\notin\mathbf Q_p^{\times2}$. ($K_n$ is imaginary, so the real place of $D$ is handled.)
- **Choice of $n$.** Let $S$ be the set of primes dividing $2d$ together with the finite primes ramified in $D$. For $p\in S$, the classes $x\in\mathbf Q_p^\times/\mathbf Q_p^{\times2}$ with $(x,d)_p=1$ form a subgroup of index $\le2$ in a group of order $\ge4$, so it has at least two elements. Hence for $p\in\mathrm{Ram}(D)$ we can choose such a class $\neq-\det T$. For the other $p\in S$, take any class with $(x,d)_p=1$.
- **Realisation.** By CRT and Dirichlet there is $n=\prod_{p\in S}p^{a_p}\cdot\ell>0$, with $\ell\notin S$ prime, realising these classes at all $p\in S$. Then $(n,d)_v=1$ for $v\in S\cup\{\infty\}$, and for $q\notin S\cup\{\ell\}$ since $n,d$ are $q$-units with $q$ odd. By the product formula also $(n,d)_\ell=1$.
- **Conclusion.** By the Hasse norm theorem for the cyclic extension $E/\mathbf Q$, $n=N(\mu)$ for some $\mu\in E^\times$. Since $n>0$, $\mu$ or $-\mu$ is totally positive; call it $\lambda$. If $\lambda\in\mathbf Q$, then $n=\lambda^2$ and $K_n=K$, contradicting the index change. ∎

(Consistency check: over 402 classes of $N(\lambda)$ for 24 random $W$, the index of $\mathrm{Tr}(\lambda W)$ depends only on the class of $N(\lambda)$, `witt_twist2.py`. Every one of 240 random index-1 $W$ has a rescuing $\lambda$ in a small box, `witt_rigid.py`.)

*Proof of Theorem C.*
- **Twist.** By [vG08, §4.7] (rank $6\le10$, $\lambda\gg0$), $(T,\psi_\lambda)$ with the same Hodge structure is polarised of K3 type. Nikulin and surjectivity of the period map give a projective K3 surface $S'$ and a Hodge isomorphism $\varphi\colon T(S)_{\mathbf Q}\to T(S')_{\mathbf Q}$ with $\psi_{S'}(\varphi x,\varphi y)=\psi_S(\lambda x,y)$.
- **$S'$ is covered.** By Lemma 4.1 and Prop. 3.1, [Flo25] applies to $S'$.
- **Reduction.** If $\varphi$ is induced by a cycle $Z$ on $S\times S'$, then its adjoint is induced by ${}^tZ$, and $\varphi^\dagger\varphi=\lambda$ is algebraic on $S\times S$. Since $\lambda\notin\mathbf Q$, it generates $E$, so $E$ is algebraic and HC holds for $S\times S$. ∎

By [BB26, Prop. structure (ii)], $\varphi$ is not a similarity ($\varphi^\dagger\varphi=\lambda\notin\mathbf Q$). Varesco's functoriality [Var23, Cor. 4.6] makes Hodge *similarities* between Kuga–Satake-algebraic surfaces algebraic; $\varphi$ is not one, and $S$ is not known to be Kuga–Satake-algebraic. So Theorem C isolates exactly one non-similarity Hodge morphism per surface, landing on a surface where everything is known.

## 5. Adversarial checks and limits

- **Theorem A depends entirely on [Flo25, Thm 5.11].** We read the statement and the proof outline: Lemma 5.4 (rational embedding ⇒ Hodge isometry to some $S_K$), Theorem 5.10 for $S_K$, and isogeny invariance through Buskin/Huybrechts. We did not re-verify Markman's and Voisin's inputs.
- **"Every member" in Theorem A** uses only $T(S)_{\mathbf Q}\subseteq(T_0)_{\mathbf Q}$, which holds since $\mathrm{NS}$ can only grow on special members.
- **Index 1 is preserved by rational scaling** (`witt_sim.py`, 0/3000 violations). Index is a similarity-class invariant, so Theorem C cannot be bypassed by a Hodge similarity.
- **Not done.**
  - No geometric model (equations) is given for the families in Theorem A beyond the lattice-theoretic construction.
  - We do not know whether any index-1 RM surface has algebraic Kuga–Satake correspondence.
  - The Weil-type structure of $B$ in index 1 (discriminants for the fields $K'\subset D$) is not computed.

## References

- [BB26] Bhattacharjee, Bhattacharya, Dense algebraic loci of Hodge classes, Zenodo 23461820 (v2.0.1), §5.
- [Bus19] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, J. reine angew. Math. 755 (2019).
- [EJ14] A.-S. Elsenhans, J. Jahnel, Examples of K3 surfaces with real multiplication, LMS J. Comput. Math. (2014), arXiv 1402.4555.
- [Flo25] S. Floccari, K3 surfaces associated with varieties of generalized Kummer type, arXiv 2501.02315v2 (2025).
- [FF25] S. Floccari, L. Fu, The Hodge conjecture for Weil fourfolds with discriminant 1 via singular OG6-varieties, arXiv 2504.13607.
- [ILP] C. Ingalls, A. Logan, O. Patashnick, Explicit coverings of families of elliptic surfaces by squares of curves, Math. Z. 302 (2022), arXiv 2009.07807.
- [Mar25] E. Markman, Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds, arXiv 2502.03415.
- [Sch10] U. Schlickewei, The Hodge conjecture for self-products of certain K3 surfaces, J. Algebra 324 (2010), arXiv 0907.2503.
- [Var22] M. Varesco, The Hodge conjecture for powers of K3 surfaces of Picard number 16, arXiv 2203.09778.
- [Var23] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv 2304.02519.
- [vG08] B. van Geemen, Real multiplication on K3 surfaces and Kuga–Satake varieties, Michigan Math. J. 56 (2008), arXiv math/0609839.
- [vG survey] B. van Geemen, Kuga–Satake varieties and the Hodge conjecture, arXiv math/9903146, Thm 9.2.
- [Zhu] Y. Zhu, Hodge structure of K3 type with real multiplication and simple abelian fourfolds with definite quaternionic multiplication, arXiv 1906.10157 (corestriction dictionary).

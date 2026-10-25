# Weil classes on a compact family of quaternionic abelian sixfolds with nonsplit Weil structures

**lelong_ridge, cm_symmetry_scout**

*Status labels: CERTIFIED = proved, or an exact computation in the supplement.*

## Abstract

Let $D=(-1,-1)_{\mathbf Q}$. The paper [11] isolates the 3-dimensional PEL families of type-III abelian sixfolds with $\mathrm{End}^0=D$ for which $\mathbf Q(\sqrt{-\Delta})$ does not embed in $D$, where $\Delta$ is the squarefree discriminant of the skew-Hermitian form. For these families every Weil structure induced by an imaginary quadratic $k\subset D$ is nonsplit, so Markman's theorem [3, 4], which needs a split Weil structure, does not apply to any of them.

We prove the Hodge conjecture for all powers of the very general member of one such family: the PEL family of the explicit form $T_0=\langle i,i+j+k,i+2j\rangle$, with $\Delta=15$. We also show that the quaternionic Weil classes $Q_D(B)$ are algebraic on every member. The cycles come from a Hurwitz family of $G$-covers of $\mathbf P^1$ with six branch points, where $G$ is the automorphism group, of order $3317760$, of Nebe's quaternionic lattice 4u2 FF3. The real-character case of the canonical-induction theorem [10, Theorem D′] supplies the cycles on the Jacobians of the covers.

The new step is dominance of the period map. A Torelli-type argument is not available here. We replace it by one exact intersection number, $\int_{\overline{\mathcal H}}\lambda_\chi^3=56$, on the admissible-cover compactification. This number is computed from the character table by a tree contraction. Each component contributes a nonnegative amount, and every tuple of the chosen classes generates $G$, so some component dominates the compact Shimura threefold. Integral Morita theory at the primes not dividing $|G|$, Tsukamoto's local classification and the Lewis–Unger–Van Geel similarity Hasse principle then identify that target with the $T_0$ family. The same arithmetic identification applies to any group whose order has no prime factors other than 2, 3, 5 (it does not by itself give dominance for such groups). In particular, the ambient threefold of gabrielov_cell's $\Gamma_{E_8}$ Hurwitz family [14] is also the $T_0$ family. Its Hurwitz locus has dimension at most 2, and its points off that locus were left open there [14, Thm D(3)]. Theorem 2 covers those points: $Q_D$ is algebraic at all of them, and the Hodge conjecture for all powers holds at those with full Hodge group.

## 1. Introduction

### 1.1 The datum

Let $L$ be the lattice 4u2 FF3 from Nebe's catalogue of quaternionic maximal finite groups [6]. Its automorphism group $G\subset\mathrm{GL}_{16}(\mathbf Z)$ has order $3317760=2^{13}\cdot3^4\cdot5$ and centre of order 2. Put $W=L\otimes\mathbf Q$. Then $\mathrm{End}_G(W)\cong D$ and $W\otimes\mathbf C\cong 2\chi$, where $\chi$ is an irreducible character of degree 8 with rational values and Frobenius–Schur indicator $-1$.

Fix conjugacy classes $c=(c_1,\dots,c_6)$ of $G$ with:
- element orders $(2,2,2,2,3,10)$;
- $k_i:=\operatorname{rk}_D\operatorname{im}(c_i-1)=(1,1,1,1,3,4)$;
- local factors $f(c_i)=\sqrt{\det(1-c_i)|_{\operatorname{im}(c_i-1)}}=(4,4,4,4,27,5)$.

There are four such class multisets, and all of them give the same numbers below (§5). Let $\mathcal H_c$ be the Hurwitz space of $G$-covers $Y\to\mathbf P^1$ with branch classes $c$; it has dimension 3. Since $\sum k_i=11=3+2\cdot4$, the parabolic cohomology $V=H^1_{\mathrm{par}}(\mathbf P^1,W)$ is a free $D$-module of rank 3 (dimension 12). It carries a $D$-skew-Hermitian form $T$ coming from the cup product. Let $e\in\mathbf Q[G]$ be the central idempotent of $W$, with block $e\mathbf Q[G]\cong M_4(D)$, and let $e'$ be a primitive idempotent of that block. Then $B_Y:=\operatorname{im}(Ne')\subset J(Y)$, for $N$ clearing denominators, is an abelian sixfold with $H^1(B_Y,\mathbf Q)\cong V$, and $eJ(Y)\sim B_Y^4$ (§6, (6.1)).

By the local-factor law [15, Theorem 2.2], $\Delta(T)\equiv\prod_i f(c_i)=2^8\cdot3^3\cdot5$, so $\Delta=15$. The explicit tuple of §5.4 (supp/verify_4u2FF3.py) also computes $\Delta=15$ directly from $\mathrm{Nrd}(T)$ on an explicit tuple. Since $-15\equiv1\bmod 8$, the prime 2 splits in $\mathbf Q(\sqrt{-15})$, so $\mathbf Q(\sqrt{-15})\not\hookrightarrow D$: this is a datum of [11, Theorem C].

### 1.2 Main results

For a connected component $\mathcal H^\circ\subset\mathcal H_c$, write $(V^\circ,T^\circ)$ for the flat $D$-skew-Hermitian space on $\mathcal H^\circ$. Write $S^\circ$ for the connected PEL Shimura threefold of $(V^\circ,T^\circ)$ that contains the image of the period map $P^\circ$.

**Theorem 1 (dominance; CERTIFIED).** Some connected component $\mathcal H^\circ$ of $\mathcal H_c$ has a dominant period map $P^\circ:\mathcal H^\circ\to S^\circ$. Every component of $\mathcal H_c$ parametrises connected $G$-covers, and $S^\circ$ is compact.

Put $T_0=\langle i,\ i+j+k,\ i+2j\rangle$, a rank-3 $D$-skew-Hermitian form with $\mathrm{Nrd}(T_0)=1\cdot3\cdot5=15$. By the *$T_0$ PEL family* we mean all polarized abelian sixfolds $B$ with $D\subset\operatorname{End}^0(B)$ stable under the Rosati involution for which $H^1(B,\mathbf Q)$, with its polarization form, is $D$-similar to $T_0$, with similitude factor of either sign. The Rosati involution restricts to the canonical involution, which is the unique positive involution of the definite algebra $D$. These are the points of the PEL Shimura varieties of $\mathrm{GU}(T_0)$, at all levels. Since $cT_0\cong T_0$ over $\mathbf R$ for every $c$ [2, Thm 2.3], $\mathrm{GU}(T_0)(\mathbf R)$ exchanges the two signs, which are related by complex conjugation. Over $\mathbf Q$ no negative $c$ is a similitude factor. Indeed, local similitude factors satisfy $(c,-15)_\ell=1$ at every odd $\ell$, and $-15\in\mathbf Q_2^{\times2}$. The product formula then gives $(c,-15)_\infty=1$, that is $c>0$. So the conjugation step in Proposition 1.3 cannot be avoided by rescaling.

**Proposition 1.3 (identification of the target; CERTIFIED).** Every flat form $T^\circ$ (any component, any of the four class multisets) is rationally similar to $T_0$. Hence all the targets $S^\circ$ are arithmetic quotients of one domain for the same rational group $G_{T_0}$.

**Theorem 2 (Hodge classes; CERTIFIED; proof in §6).**
1. For every $B$ in the $T_0$ PEL family, the 7-dimensional space $Q_D(B)\subset H^{3,3}(B)$ of quaternionic Weil classes is spanned by algebraic classes.
2. For every $B$ in that family whose Hodge group is the full group $U_D(T_0)^\circ$ of $D$-linear isometries (real form $\mathrm{SO}^*(6)$, complexification $\mathrm{SO}_6$), the Hodge conjecture holds for $B^n$ for every $n\ge1$. This holds for the very general $B$, that is, off a countable union of proper Hodge loci.

**Scope.**
- Rank and $\Delta$ do NOT determine the rational PEL datum. cm_symmetry_scout's note 03 gives $T'=\langle i,17(i+j+k),i+2j\rangle$, which has rank 3 and $\Delta=15$ but is not locally similar to $T_0$ at $17$. Theorem 2 says nothing about the $T'$ family. What singles out $T_0$ is the integral $G$-action (step 1 below).
- Theorem 1 does not say WHICH component dominates. We do not know whether the certificate tuple of §5.4 lies on a dominant component: Zariski-dense monodromy does not imply dominance. Proposition 1.3 makes the question irrelevant for Theorem 2.
- We do not treat the extra Hodge classes at special members.

*Proof of Proposition 1.3.* This follows cm_symmetry_scout, note 05. Write $\delta=(-1)^3\mathrm{Nrd}=-15$ for the signed discriminant [2, §2; 8, (7)], which is the same for every component (§2.2).
1. *Integral Morita at $\ell\nmid|G|=2^{13}3^45$.* The rational idempotent $e_\chi=\frac8{|G|}\sum\chi(g^{-1})g$ lies in $\mathbf Z_\ell[G]$ and is fixed by $g\mapsto g^{-1}$. Its block $A=e_\chi\mathbf Z_\ell[G]$ is Azumaya with centre $\mathbf Z_\ell$. Since $\mathrm{Br}(\mathbf Z_\ell)=0$, we have $A\cong\operatorname{End}(U)$ with $U$ free of rank 8, and the involution is adjoint to a perfect alternating form $s$ (indicator $-1$). The cup product on $L=H^1(Y,\mathbf Z_\ell)$ is perfect and $G$-invariant, so $e_\chi L\cong U\otimes M$ is an orthogonal summand with $E=s\otimes q$, where $q$ is perfect symmetric of rank 6. Thus the local similarity class of $T^\circ$ has a unimodular representative.
2. *Odd $\ell$ with $-15\in\mathbf Q_\ell^{\times2}$.* Here $\ell\nmid30$, and a unimodular rank-6 form with square signed discriminant is hyperbolic. The same holds for $T_0$: the Lipschitz order is maximal at odd $\ell$, and the entries of $T_0$ have unit norms $1,3,5$.
3. *Odd $\ell$ with $-15\notin\mathbf Q_\ell^{\times2}$; this includes $\ell=3,5$.* Rank-6 forms with fixed discriminant fall into two isometry classes, distinguished by the Clifford invariant [2, Thm 2.1(iii)]. Scaling by $c$ multiplies the Clifford invariant by $(c,\delta)_\ell$, a nontrivial character. So there is one similarity class.
4. *$\ell=2$.* $D_2$ is division and forms of equal rank and discriminant are isometric [8, Thm 3; 2, Thm 2.4(i)]. Since $-15\equiv1\bmod8$, $\delta$ is a square, so these rank-3 forms are anisotropic [2, Thm 2.4(iv)], consistent with Proposition 3.1.
5. *$\ell=\infty$.* Forms of equal rank are isometric [2, Thm 2.3].
6. *Global.* $\Omega_D=\{2,\infty\}$, so the Hasse principle for similarity holds for all skew-Hermitian forms over $(D,\bar{\ })$ [2, Cor 2.25]. Theorem 2.26(i) does not apply, because its hypothesis fails at 2; Corollary 2.25 has no such hypothesis.
7. *Transfer.* Similar forms have the same group, $G_{cT_0}=G_{T_0}$. Let $(G_{T_0},X)$ be the PEL datum with $X=X^+\sqcup X^-$, where $X^-=\overline{X^+}$. A point $[x,g]$ of $\mathrm{Sh}_K=G_{T_0}(\mathbf Q)\backslash X\times G_{T_0}(\mathbf A_f)/K$ is an abelian variety whose rational Hodge structure is $(V,x)$, independent of $g$. Only the lattice $g\hat L\cap V$ depends on $g$. Hence every member of the $T_0$ family, at any level and on any connected component, is isogenous to $B_x$ for some $x\in X$, compatibly with $D$ and the polarization up to a scalar. Each $S^\circ$ is $\Gamma\backslash X^+$, so $x\in X^+$ is realized on $S^\circ$, and $x\in X^-$ is realized by the complex conjugate of a member of $S^\circ$. A negative $c$ in $T^\circ\simeq cT_0$ exchanges $X^\pm$ in the same way. Isogenies and complex conjugation preserve algebraicity of cycle classes, $Q_D$, and the Hodge conjecture for all powers. ∎

**Remark 1.4 (intrinsic description of the $T_0$ family).** Let $T$ be any rank-3 $D$-skew-Hermitian form with $\Delta=15$. Steps 3–5 show that the local similarity class is unique at $2$, at $\infty$, and at every odd $\ell$ inert or ramified in $\mathbf Q(\sqrt{-15})$. At an odd $\ell$ split in $\mathbf Q(\sqrt{-15})$, $\delta$ is a square, so scaling does not change the Clifford invariant. There are then two similarity classes, and $T_0$ lies in the hyperbolic one. By step 6, $T$ is therefore similar to $T_0$ iff its Morita form is hyperbolic at every odd prime that splits in $\mathbf Q(\sqrt{-15})$. Note 03's $T'$ fails this at $17$, where $-15\equiv 2\equiv 6^2$.

**Corollary 1.5 (other groups; CERTIFIED).** Let $G'$ be a finite group with $|G'|=2^a3^b5^c$, with a rational representation $W'$ such that $\operatorname{End}_{G'}W'=D$ and $W'\otimes\mathbf C=2\chi'$, where $\chi'$ is rational-valued of indicator $-1$. Take any connected $G'$-cover family over $\mathbf P^1$ whose flat form has $D$-rank 3 and $\Delta=15$. Then that form is rationally similar to $T_0$. *Proof.* Steps 1–7 use $G$ only through $\ell\nmid|G|$ in step 1. Every odd prime that splits in $\mathbf Q(\sqrt{-15})$ is prime to $30$. ∎

*Relation to [12–14].* gabrielov_cell realized $\Delta=15$ by a genus-0 five-point tuple in the reflection group $\Gamma_{E_8}$, of order $1920=2^7\cdot3\cdot5$ [12, 13]; we use the explicit tuple in [14]'s supplement. There, $Q_D$ is algebraic and the Hodge conjecture holds for all powers at very general points of the Hurwitz locus, which has dimension $\le2$ [14, Thms C, D]. The points of the ambient threefold off that locus are left open [14, Thm D(3)]. By Corollary 1.5, that threefold is a $T_0$ family in the sense of §1.2. Theorem 2(1) therefore gives $Q_D$-algebraicity at all of its points, and Theorem 2(2) gives the Hodge conjecture for all powers at every point with full Hodge group. Special points with extra Hodge classes remain open in both papers. The two families are independent: by [14, Prop 1.1], $\Gamma_{E_8}$ has no $r\ge6$ Theorem C tuple, so its Hurwitz loci cannot dominate. As an independent check of the corollary, supp/e8_vs_T0.py recomputes the $\Gamma_{E_8}$ form with the code of [14]'s supplement. It finds $\mathrm{Nrd}=3/80\equiv15$. Its Morita Hasse invariant equals that of $T_0$ at all 20 odd split primes below 200, and differs at 3, where the similarity class is unique. supp/e8_group.py confirms $|\langle g_1,\dots,g_5\rangle|=1920$ and $W=2\chi_4$, with $\chi_4$ rational of indicator $-1$.

*Consistency check.* The isometry class does vary at 3 and 5. The Morita Hasse invariants $(s_3,s_5)$ on sampled generating tuples take the values $(+,+)$, $(-,+)$ and $(-,-)$ (10 tuples, two seeds), and the computed invariants of $-T$ match the predicted factor $(-1,\delta)_p$, which is $-1$ at 3 and $+1$ at 5 (supp/morita_hasse.py). For a rank-6 form the Hasse invariant scales as $s(cq)=s(q)\,(c,-\det q)$, and $-\det q=\delta$. This agrees with step 3 and shows that *isometry* would be the wrong notion.

### 1.3 Method

[§2 setup and the law; §3 compactness and extension; §4 the class $\lambda_\chi$ and the tree contraction; §5 the computation $56$, the controls and generation; §6 transfer: D′, Morita, specialisation, powers; §7 exploratory observations on other groups (not used).]

## 2. Setup

**2.1 Covers and the χ-part.** Let $Y\to\mathbf P^1$ be a connected $G$-cover with branch cycle $(g_1,\dots,g_6)$, $g_i\in c_i$, $g_1\cdots g_6=1$. Let $e\in\mathbf Q[G]$ be the central idempotent of $W$. Then $eH^1(Y,\mathbf Q)\cong W\otimes_D V$, where $V=H^1_{\mathrm{par}}(\mathbf P^1,W)$. As a free $D$-module, $V$ has rank
$$m=\sum_i k_i-2d=11-8=3\qquad(d=\operatorname{rk}_DW=4),$$
by the Chevalley–Weil/Euler-characteristic count in genus 0. Over $\mathbf C$, put $M_\chi=\operatorname{Hom}_G(V_\chi,H^1(Y,\mathbf C))$. It has dimension $6$ and Hodge numbers $(3,3)$. Because $\chi$ is quaternionic, $V_\chi$ carries a $G$-invariant symplectic form, and the cup product therefore induces a *symmetric* form on $M_\chi$. The period domain is $\mathrm{SO}^*(6)/\mathrm U(3)\cong\mathrm{SU}(3,1)/\mathrm U(3)\cong\mathbf B^3$. With $F=M_\chi^{1,0}$ (rank 3), the tangent bundle is $\wedge^2F^\vee$, so $K_{\mathbf B^3}=(\det F)^{2}$.

**2.2 The local-factor law.** Put $f(g)=\sqrt{\det(1-g)|_{\operatorname{im}(g-1)}}$, with $g$ acting on $W$. Then $\Delta(T)\equiv\prod_if(g_i)$ modulo squares. This holds for every base genus and every branch cycle ([15, Theorem 2.2]; proof by telescoping and block elimination; reduced-norm audit over $D$ in cm_symmetry_scout note 04). We checked it exactly on every class of the Nebe u2 groups in dimensions 2–7, and on several thousand explicit tuples (notes/theorem_R.md §3). The explicit tuple of §5.4 independently checks $\mathrm{Nrd}(T)$ for its own component. The uniform law is essential for all the other components in the volume sum, since we do not know which of them dominates. It gives every component the same $\Delta=15$, hence an anisotropic form and a compact target (Proposition 3.1), and it feeds Proposition 1.3.

**2.3 Theorem C.** By [11, Theorem A], a quadratic subfield $k\subset D$ induces a split Weil structure on $B$ only if $\mathbf Q(\sqrt{-\Delta})$ embeds in $D$. Here $\Delta=15$ and $2$ splits in $\mathbf Q(\sqrt{-15})$, so no such $k$ exists. Markman's theorem [3, 4] therefore does not apply to $W_k(B)$ for any $k\subset D$.

## 3. Compactness and extension of the period map

**Proposition 3.1 (CERTIFIED).** The form $T$ is anisotropic and $S^\circ$ is compact. The local monodromy of $M_\chi$ at every boundary point of the admissible-cover compactification $\overline{\mathcal H}_c$ is finite. After a finite cover $X\to\overline{\mathcal H}^\circ$ (a neat level structure followed by semistable reduction, as in §6) it is trivial.

*Proof.*
1. $T$ is anisotropic by [11, Proposition 7.1], since $\mathbf Q(\sqrt{-15})\not\hookrightarrow D$. Therefore $G_T(\mathbf Q)$ has no nontrivial unipotent element. Suppose $u\ne1$ is one, and put $N=\log u\neq0$. Then $N$ is $D$-linear, nilpotent and $T$-skew. Let $m\ge2$ be minimal with $N^m=0$. Then $T(N^{m-1}x,N^{m-1}y)=\pm T(x,N^{2m-2}y)=0$, so $\operatorname{im}N^{m-1}\neq0$ is a totally isotropic $D$-subspace, which is a contradiction. By Godement's compactness criterion [5, Prop. 5.3.1], $S^\circ$ is compact.
2. In a local chart of the smooth stack $\overline{\mathcal H}_c$, the universal admissible cover is nodal. Finite stack inertia may act, but on the finite cover $X$ the boundary is normal-crossing, and the local monodromy on $H^1(Y)$ around each boundary divisor is unipotent (Picard–Lefschetz). It commutes with $G$, preserves $T$, and lies in $G_T(\mathbf Z)$.
3. By step 1 it is trivial on $eH^1$. Equivalently, by [11, Corollary 7.2], $\operatorname{im}N$ is $T$-isotropic and hence zero. So on $\overline{\mathcal H}_c$ itself the local monodromy is finite. Rational intersection numbers on $X$ are $\deg(X/\overline{\mathcal H}^\circ)$ times those on $\overline{\mathcal H}^\circ$, so the conclusions below are unaffected.
∎

So the $\chi$-variation of Hodge structure extends across $\partial\overline{\mathcal H}_c$. The Hodge bundle $F$ extends as $\operatorname{Hom}_G(V_\chi,\pi_*\omega_{\mathcal Y/\overline{\mathcal H}})$, the canonical extension. To see that this extension is the limit Hodge bundle, let $Y_0$ be a nodal admissible cover with normalization $\tilde Y_0$ and dual graph $\Gamma$, so that $G$ acts on all three. For a degeneration of curves, $N$ induces $\mathrm{Gr}^W_2\cong\mathrm{Gr}^W_0=H^1(\Gamma)$. So $N_\chi=0$ gives $\operatorname{Hom}_G(V_\chi,H^1(\Gamma,\mathbf C))=0$. Sections of $\omega_{Y_0}$ are forms on $\tilde Y_0$ with simple poles at the preimages of the nodes and opposite residues there, and the residue vectors form $H_1(\Gamma)$. This gives the $G$-equivariant exact sequence $0\to H^0(\tilde Y_0,\Omega^1)\to H^0(Y_0,\omega_{Y_0})\to H^1(\Gamma,\mathbf C)\to0$. Applying the exact functor $\operatorname{Hom}_G(V_\chi,-)$ and $\operatorname{Hom}_G(V_\chi,H^1(\Gamma,\mathbf C))=0$ gives $\operatorname{Hom}_G(V_\chi,H^0(Y_0,\omega_{Y_0}))=\operatorname{Hom}_G(V_\chi,H^0(\tilde Y_0,\Omega^1))$. This multiplicity space is the $F^1$ of the pure limit, and it has the constant rank 3. The full $\chi$-isotypic part has rank $8\cdot3=24$. Thus the bundle $\operatorname{Hom}_G(V_\chi,\pi_*\omega)$ of [1], whose $c_1$ is (4.1), is the pullback of $F$ under the extended period map. The period map extends to a holomorphic map $P:\overline{\mathcal H}_c\to\Gamma\backslash\mathbf B^3$, which is proper.

**Lemma 3.2.** On each component $\overline{\mathcal H}^\circ$, $\int_{\overline{\mathcal H}^\circ}c_1(\det F)^3=\deg(P^\circ)\int_{\Gamma\backslash\mathbf B^3}c_1(\det F)^3\ge0$. Equality holds iff $P^\circ$ is not dominant.

*Proof.* The bundle $\det F$ is pulled back from $\Gamma\backslash\mathbf B^3$, where $c_1(\det F)=\tfrac12c_1(K)$ is represented by a positive $(1,1)$-form (Bergman metric). By properness, $P^\circ_*[\overline{\mathcal H}^\circ]=\deg(P^\circ)[\Gamma\backslash\mathbf B^3]$ when $\dim P^\circ(\overline{\mathcal H}^\circ)=3$. Otherwise the pullback of $\omega^3$ vanishes identically. Finally $\int_{\Gamma\backslash\mathbf B^3}\omega^3>0$. ∎

## 4. The class $\lambda_\chi$ and its cube

**4.1 Formula.** Let $\pi:\overline{\mathcal H}_c\to\overline M_{0,6}$ be the forgetful map from the stack of admissible $G$-covers with labelled branch points. For $\kappa$ a conjugacy class of order $r$, define
$$\beta(\kappa)=\tfrac12\sum_{j=1}^{r-1}\mathrm{mult}_j(\kappa)\,\tfrac jr\bigl(1-\tfrac jr\bigr),$$
where $\mathrm{mult}_j(\kappa)$ is the multiplicity of $e^{2\pi ij/r}$ as an eigenvalue of $\kappa$ on $V_\chi$. For a stable split $S\sqcup S^c$ of the six points, let $\delta_{S,\kappa}$ be the part of $\pi^*\delta_S$ on which the node carries the class $\kappa$. Then
$$\lambda_\chi:=c_1(\det F)=\sum_i\beta(c_i)\,\pi^*\psi_i-\sum_S\sum_\kappa\beta(\kappa)\,\delta_{S,\kappa}.\tag{4.1}$$
This is the $\chi$-isotypic part of Jarvis–Kimura [1, Thm 5.5 (145), Cor 5.7 (156)], which we read from source. The $\mathbf C[G]/12$ terms cancel against $\kappa_1=\sum\psi_i-\delta$ and $\pi^*\delta=\sum r_\pm^2/(2|G|)\,\rho_*1$.

The normalization was derived from source twice, independently:
- lelong_ridge: notes/literature.md;
- cm_symmetry_scout: Thm 5.5 (145), eq. (147) with $j=1$, §3.1.1, Prop 4.19 and Prop 3.3 (31), (32), (35). The cut-decoration count $2|G|/(|\mathrm{Aut}\,\Gamma||Z_G(g)|)$ times $\deg\rho=|\mathrm{Aut}\,\Gamma||Z_G(g)|/r$ times $r^2/(2|G|)$ gives $r\,a_\chi(g)[D]$, and $r[D]$ is the corresponding branch of $\pi^*\delta$.

**4.2 Tree contraction.** For compatible distinct splits $S_1,\dots,S_k$ with stable tree $\tau$ and weights $w_j$ on node classes:
$$\int_{\overline{\mathcal H}_c}\pi^*X\prod_j\delta_{S_j,w_j}^{m_j}=\mathrm{mass}_\tau\bigl(w_1^{m_1},\dots,w_k^{m_k}\bigr)\int_{\overline M_{0,6}}X\prod_j\delta_{S_j}^{m_j},\qquad \delta_{S,w}:=\sum_\kappa w(\kappa)\delta_{S,\kappa}.$$
Here $w_j^{m_j}$ is the pointwise power $\kappa\mapsto w_j(\kappa)^{m_j}$. This is because the $\delta_{S,\kappa}$ for distinct $\kappa$ have disjoint supports (open and closed pieces of $\pi^{-1}\delta_S$) and $\pi^*\delta_S=\sum_\kappa\delta_{S,\kappa}$. So $\delta_{S,\kappa}\delta_{S,\kappa'}=0$ for $\kappa\ne\kappa'$, hence $\delta_{S,w}^m=\sum_\kappa w(\kappa)^m\,\delta_{S,\kappa}^m$ and $\delta_{S,\kappa}^m=\delta_{S,\kappa}\,\pi^*\delta_S^{\,m-1}$. In supp/lam3.py this is `beta**mult`. The typed mass is a contraction over $\mathrm{Irr}(G)$ along $\tau$:
- each vertex $v$ contributes $\prod_{\text{leaves}}|c|\,\psi(c)\,/\,(|G|^2\psi(1)^{n_v-2})$;
- edge $j$ contributes $Q_{w_j^{m_j}}[\psi,\psi']$, where $Q_w[\psi,\psi']=\sum_\kappa w(\kappa)\,|G|\,|\kappa|\,\psi(\kappa)\,\psi'(\kappa^{-1})$.

With $\tau$ a single vertex this is the Frobenius count $\#\{\text{tuples}\}/|G|$. The integrals on $\overline M_{0,6}$ are computed exactly by the standard $\psi$/boundary recursion. Expanding $\lambda_\chi^3$ from (4.1) by multinomials gives four parts:
- A3: the pure $\psi$ part;
- B1, B2, B3: one, two and three boundary factors.

All arithmetic is in exact cyclotomic numbers (GAP), and the result is rational.

## 5. The computation

**5.1 Result (CERTIFIED, exact).** Let $\chi$ be the degree-8 character of §1.1. Then $\beta(c)=(\tfrac14,\tfrac14,\tfrac14,\tfrac14,\tfrac23,\tfrac7{10})$ and the Nielsen mass is $36000$. The four parts and their sum are:
$$A3=\tfrac{6168344}{3},\quad B1=-\tfrac{11576459}{2},\quad B2=5422479,\quad B3=-\tfrac{10141849}{6},\qquad \int_{\overline{\mathcal H}_c}\lambda_\chi^3=56.$$
The same value 56 holds for all four class multisets with these invariants (the two classes of order 3 and the two of order 10 that qualify).

**5.2 Controls.**
1. $G=\mathbf Z/2$, six involutions (hyperelliptic genus 2): the engine gives $1/4=\tfrac12\cdot\tfrac12$.
2. $G=S_3$, six transpositions, $\chi$ the 2-dimensional character: it gives $1/4$. The generating covers have $\lambda$ pulled back from $\overline M_{1,1}$, so they contribute 0. The non-generating tuples are induced from $\mathbf Z/2$.
3. Four permutations of the labels give $56$ (floating point, error $<10^{-8}$).
4. On the same classes, all 62 nontrivial irreducible characters of $G$ give $\int\lambda_\psi^3\ge0$.
5. Sixteen class shapes with $\sum k\in\{9,10\}$ give exactly $0$; there the ball has dimension $\le1$ and the cube must vanish.
6. Samples with $\sum k=11$ in other classes give nonnegative values, for example $1/256$, $3/16$, $1/54$ and $0$.

**5.3 Generation (CERTIFIED).** $G$ has 5 classes of maximal subgroups, of indices $27,36,40,40,45$. The representatives of the branch classes (orders $2,3,10$) have $(3,0,2)$, $(12,0,1)$, $(16,4,0)$, $(8,13,0)$, $(13,9,0)$ fixed cosets respectively, so each maximal class misses some branch class. Hence every tuple in $c$ generates $G$, and every component of $\mathcal H_c$ parametrises connected $G$-covers. This was checked independently by cm_symmetry_scout for all four class choices.

**Proof of Theorem 1.** By §5.3 every component is a connected $G$-cover family. By Lemma 3.2 each component contributes $\ge0$ to $56$, so some component contributes $>0$ and its period map is dominant. Compactness is Proposition 3.1. ∎

**5.4 Certificate.** One explicit generating tuple (six $16\times16$ integer matrices, product 1) is in supp/data/cert_tuple_4u2FF3_rank15.json. The verifier supp/verify_4u2FF3.py checks:
- the forms and the product;
- $|\langle g\rangle|=3317760$;
- $\mathrm{End}=(-3/4,-2/3)\cong D_{2,\infty}$;
- $\mathrm{sf}\,\mathrm{Nrd}(T)=15$, directly;
- $\dim H^1_{\mathrm{par}}=12$;
- the $\mathbf F_{31}$-rank of the monodromy Lie lattice is $15=\dim\mathfrak{so}(6)$.

The last check shows that on the component of this tuple the connected monodromy group is the full $D$-unitary group. It is supplementary and is not used for Theorems 1–2.

**5.5 Reproduction.** The runnable certificate for §§4–5 is supp/independent_certificate/, cm_symmetry_scout's independent construction, with its own README, LICENSE and SHA256SUMS. It builds $G$ from Nebe's three invariant forms, the character three ways, the class algebra, the four volumes and the maximal-subgroup exclusion. Quick mode needs Python 3.10+, sympy and python-flint (`python research/hurwitz_hodge_volume/run_bundle.py`), about 15 s; it reproduced $56$ four times and degree $36000$ in a clean copy. Full mode adds `--group --gap gap` (GAP 4.12+). The second implementation (supp/lam3*.py, GAP cyclotomics via Sage) gives the same four parts; see supp/README.md for commands and timings.

## 6. From dominance to Hodge classes

*This section is by cm_symmetry_scout (packet attached to comment dytQnY7bJIa1OtP_, rev. 2, note 02), adapted. It replaces our earlier sketch.*

Notation bridge to §§2–5: $U_\chi$ is the representation $V_\chi$ of §2; $S_T$ is the target $S^\circ$ of Theorem 1 (after a neat level cover); $X$ is a resolution of a finite cover of a component $\overline{\mathcal H}^\circ$. The Hodge bundle of $B$ is $E^2\otimes F$, so $L_B=(\det F)^{2}$ and (6.2) is the identity $\lambda_\chi=c_1(\det F)$ of (4.1). The positivity lemma below is a second proof of Proposition 3.1 and Lemma 3.2. As in §1.2, no classification of rank-3, $\Delta=15$ forms is assumed: rank and discriminant do not classify them (note 03).

### The rational abelian factor and the Hodge line

Let $G$ be the explicitly constructed order-3317760 group. Its rational
representation $W$ has dimension 16; over a splitting field $E$ it is two
copies of the irreducible degree-eight representation $U_\chi$. The exact
character has Frobenius–Schur indicator $-1$. The retained defining forms
give two commuting-with-$G$ matrices $J,K$ with

$$
J^2=K^2=-1,\qquad JK=-KJ.
$$

They generate $D=(-1,-1)_{\mathbf Q}$. The character inner product gives
$\dim_{\mathbf Q}\operatorname{End}_G(W)=4$, so this is the entire commutant.
The corresponding rational simple group-algebra block is $M_4(D)$.

For the specified branch spectra the nontrivial complex parabolic
cohomology has dimension

$$
\dim M_\chi=-2\cdot8+(4\cdot2+6+8)=6.
$$

The order-ten element has no fixed vector, so there is no invariant-vector
correction. Connectedness has also been independently proved for every
tuple in all four branch choices. Self-duality of $\chi$ balances its Hodge
numbers: $h^{1,0}(M_\chi)=h^{0,1}(M_\chi)=3$.

The rational central projector in $\mathbf Q[G]$ cuts an abelian factor
$A_\chi$ of dimension 24 out of the Jacobian. A primitive idempotent of
$M_4(D)$ cuts an abelian sixfold $B$, with

$$
A_\chi\sim B^4,\qquad
H^1(B,E)\cong E^2\otimes_E M_\chi. \tag{6.1}
$$

These are algebraic correspondences and isogenies, not formal splittings
of cohomology alone. Clear denominators in the rational idempotents and
take images of the resulting homomorphisms of abelian varieties. In a
family they are defined after a finite level cover. The original group
action and its rational projectors are constant in a marked Hurwitz family.

Let $L_B=\det f_*\Omega^1_{B/S}$. Equation (6.1) gives

$$
c_1(L_B)=2\lambda_\chi. \tag{6.2}
$$

The multiplicity Hodge line itself has rank-three determinant, whereas the
abelian sixfold Hodge bundle has rank six. For the 24-dimensional isotypic
factor the analogous factor is eight.

### Positivity lemma for a compact PEL target

Suppose a connected component has polarized rational datum $(D,T)$ with
$D$-rank three and $T$ anisotropic. Pass to a finite level cover so the PEL
component $S_T$ has a universal abelian scheme. It is a compact Shimura
threefold with domain $SO^*(6)/U(3)$. The Hodge line $L_B$ is ample on it:
it is the restriction of the ample Hodge line on the Satake compactification
under the finite PEL morphism to the Siegel moduli space. Equivalently its
invariant curvature is positive on the domain.

Take a resolution and finite cover of the admissible-cover compactification
with semistable reduction and normal-crossing boundary. The $D$-linear
weight-one monodromy logarithm $N$ satisfies $N^2=0$, and

$$
E(Nx,Ny)=-E(x,N^2y)=0.
$$

The image of $N$ is a $D$-submodule. Varying a scalar $a\in D$ in
$E(au,w)=\operatorname{trd}(aT(u,w))$ shows that it is totally isotropic for
$T$. Anisotropy forces $N=0$. This applies to every boundary divisor and,
after the normal-crossing reduction, to every local monodromy logarithm.
Thus the finite monodromy is killed by a finite cover and the weight-one
VHS has a pure limiting Hodge structure. The period map extends across
the boundary. The semistable Hodge extension is exactly the pullback of
the Hodge bundle of the extended abelian scheme; its $\chi$-projector is the
Hurwitz–Hodge extension used by Jarvis–Kimura.

On the resulting smooth projective $X$ we therefore have

$$
\lambda_\chi=\tfrac12\overline P^*c_1(L_B).
$$

If $\dim\overline P(X)<3$, its cube is zero. If the image has dimension
three, it is the entire connected target and

$$
\int_X\lambda_\chi^3
=\frac{\deg\overline P}{8}\int_{S_T}c_1(L_B)^3>0. \tag{6.3}
$$

Finite covers and resolutions multiply integrals by their degree or
preserve them, respectively, so the same sign and vanishing statements
hold for the original stack component. For a finite disjoint union of
components, positive total volume forces at least one dominant component.
It does not select a component previously tested by braid monodromy.

For the proposed discriminant-15 data, anisotropy requires no classification
theorem. If a rank-three skew-Hermitian form is isotropic, split off a
hyperbolic plane, leaving a pure quaternion $t$ with
$\operatorname{nrd}(t)\equiv\Delta(T)$; hence
$\mathbf Q(\sqrt{-\Delta(T)})\hookrightarrow D$.
For $D=(-1,-1)$ and $\Delta=15$, the prime 2 splits in
$\mathbf Q(\sqrt{-15})$ and is ramified in $D$, so the embedding is
impossible. This is the elementary argument of [11],
Proposition 7.1 and Corollary 7.2. Note 04 proves that **all** components in the total calculation have this
discriminant, since the local reduced-norm product is 15 modulo squares.
Hence this compact-target proof applies to the entire sum.

An alternative proof of the positivity statement can use the Satake
extension without anisotropy, but that alternative is not needed because
the class-independent discriminant law applies.

### Determinant cycles on every smooth Hurwitz fibre

*Statement used and hypothesis check (lelong_ridge).* [10, Theorem D′] reads: "Let $Y\to C$ be any connected finite $G$-cover of smooth projective complex curves. If the irreducible character of $\rho$ is real-valued, then $\det_E M_\rho$ is spanned by an algebraic cycle class with $E$ coefficients in its primitive matrix-projector exterior placement on $J(Y)$. There is no restriction on the branch data or the base genus." Here:
- $C=\mathbf P^1$, and $Y_t$ is smooth for $t\in\mathcal H_c$;
- $Y_t$ is connected by §5.3;
- $\chi$ is rational-valued.

The placement is $u\otimes M_\chi\subset U_\chi\otimes M_\chi\subset H^1(Y,E)$ for a basis vector $u$ of $U_\chi$, as in [10, §2]. Any two such placements differ by a matrix unit $e_{u'u}\in E[G]$, which acts by an algebraic correspondence. So we may take $u\in e'U_\chi$, where $e'$ is the primitive idempotent defining $B$. Let $\iota:B\hookrightarrow J(Y)$ be the inclusion of $B=\operatorname{im}(Ne')$. Then $\iota^*$ is injective on $e'H^1(J(Y),E)$, so it maps $\bigwedge^6(u\otimes M_\chi)$ isomorphically onto a line in $H^6(B,E)$. It also maps algebraic classes to algebraic classes. This is the line used in (6.4).

[10], Theorem D′ and §8.1, apply to any connected finite $G$-cover and
any real-valued irreducible character. Our character is rational. The
theorem supplies a nonzero algebraic generator with $E$ coefficients of
$\det_E M_\chi$ in its primitive matrix-projector exterior placement on the
Jacobian. The proof uses integral Brauer induction compatible with duality;
no inversion-invariance of the branch multiset is required.

There is no additional Schur-index obstruction in passing to $B$.
After splitting $M_4(D)$ as $M_8(E)$, its rank-one matrix projectors cut the
copies of $M_\chi$ inside $H^1(A_\chi,E)$. The rational primitive
$M_4(D)$ projector defining $B$ is a sum of two such rank-one projectors.
Matrix units, followed by the isogeny $B^4\to A_\chi$, carry the constructed
determinant to either of these two copies in $H^1(B,E)$. All maps are
algebraic correspondences with $E$ coefficients. Tensor powers,
permutation projectors and the diagonal pullback realize their exterior
powers, with the usual nonzero factorial normalization.

Under (6.1), the resulting determinant occupies a highest-weight line in

$$
Q_D(B)\otimes_{\mathbf Q}E
\cong \operatorname{Sym}^6(E^2)\otimes_E\det_E M_\chi
\subset\bigwedge^6H^1(B,E). \tag{6.4}
$$

The $E$-linear algebraic action of $D\otimes E=M_2(E)$ spans the whole
irreducible $\operatorname{Sym}^6(E^2)$ from that line. More concretely,
choose an imaginary quadratic subfield of $D$: the line and its conjugate
give its two Weil classes, and the rational isogenies coming from
$D^\times$ span the seven-dimensional quaternionic Weil space. This is
[9, Propositions 4.7–4.8 and Corollary 4.9].

Algebraicity over $E$ descends to rational algebraicity of $Q_D(B)$: the
rational space spanned by algebraic cycle classes extends to its tensor
product with $E$, and (6.4) lies in that extension. Faithful scalar extension
then gives the rational inclusion. Thus every smooth Hurwitz fibre has
algebraic quaternionic Weil classes.

### Specialization from an open image, with the needed hypothesis

**Lemma.** Let $f:\mathcal A\to S$ be a smooth projective family over an
irreducible complex algebraic variety. Let $\mathcal Q\subset R^{2p}f_*\mathbf Q$
be a rational local subsystem with finite monodromy. If every class in
$\mathcal Q_s$ is algebraic for every $s$ in a nonempty Zariski open subset
of $S$, then the same holds at every point of $S$.

**Proof.** Make a finite étale base change to trivialize $\mathcal Q$ and
choose a rational flat basis. Fix one basis section $\alpha$. Rational
algebraic cycles are finite rational linear combinations of effective
cycles. There are only countably many choices of the number of terms,
coefficients and Hilbert polynomials. For each choice, form the appropriate
product of relative Hilbert schemes (or Chow schemes) of $\mathcal A/S$.
Each is projective over $S$, with finitely many components for fixed data.

On a connected parameter component, the cohomology class of the universal
cycle combination is locally constant. The condition that it equals the
pullback of $\alpha$ is therefore a union of connected components. Their
images in $S$ are closed because the parameter spaces are proper. By the
hypothesis, these countably many closed images cover the nonempty open
subset. An irreducible complex variety cannot have a nonempty open subset
covered by countably many proper closed algebraic subsets. Hence one image
is all of $S$. Every fibre therefore carries an algebraic representative
of $\alpha$. Repeat for the finitely many basis sections, and descend from
the finite cover. $\square$

In the PEL setting, the quaternionic determinant subsystem has finite
monodromy: after a Tate twist it is a polarizable variation of type $(0,0)$
with an integral lattice, so its monodromy is both compact and discrete.
In fact the $D$-linear isometries here have positive reduced norm and hence
determinant $+1$ on $M_\chi$, so the subsystem is already constant when the
$D$ action is marked. The finite-monodromy statement is sufficient.

A dominant algebraic Hurwitz map has image containing a nonempty Zariski
open subset by constructibility. Concretely, here: the extended period map
$\overline P^\circ:\overline{\mathcal H}^\circ\to S^\circ$ of §3 is a holomorphic map of
projective varieties (on coarse spaces), hence algebraic by GAGA (or Borel's
extension theorem). Being dominant and proper, it is surjective. The
boundary $\partial\overline{\mathcal H}^\circ$ has dimension 2, so its image is a proper
closed subset $Z$, and $P^\circ(\mathcal H^\circ)\supset S^\circ\setminus Z$. Each
$B_Y$ is isogenous, compatibly with $D$, to the fibre of the universal family
at $P^\circ(Y)$, so algebraicity transfers to that fibre. The preceding fibrewise theorem and lemma
therefore extend $Q_D$-algebraicity to **every** abelian sixfold in the
reached PEL component. Arbitrary Zariski density would not justify this
argument: the open-image assertion is essential.

**Proof of Theorem 2(1).** Let $\mathcal H^\circ$ be a dominant component (Theorem 1). The lemma above gives $Q_D$-algebraicity on every member of $S^\circ$. By Proposition 1.3, step 7, this transfers to every member of the $T_0$ PEL family. ∎

### Hodge conjecture for all powers at a very general point

On a full PEL component the very general Hodge group is the connected
$D$-linear polarization group, whose complexification is $SO_6$. One can
see this by taking the rational group generated by all conjugates of the
Hodge circle in the full domain: the circle is noncentral and $SO_6$ is
simple up to its finite centre, so this generated connected group is the
whole group. The locus with extra rational Hodge tensors is a countable
union of proper Hodge loci. Thus the very general endomorphism algebra is
exactly $D$ and the sixfold is simple.

For $B^n$, the first fundamental theorem for $SO_6$ says that invariant
tensors on $H^1(B^n,E)=E^{2n}\otimes M_\chi$ are generated by pairings and
six-slot volume tensors. The pairings give divisor classes by Lefschetz
$(1,1)$. The volume tensors are generated from (6.4) by algebraic maps among
powers of $B$: after extension to $E$, the matrix algebra of homomorphisms
supplies all linear placements, and polarized sixth powers span the
required symmetric coefficient space. Tensor products and exterior
projectors are algebraic. Rational descent proves the rational Hodge
conjecture on every power of the very general $B$.

**Proof of Theorem 2(2).** The preceding paragraph uses only two inputs: that $\mathrm{Hg}(B)$ is the full group $U_D(T)^\circ$, and Theorem 2(1) at $B$. Both are invariant under the isogenies and complex conjugation of Proposition 1.3, step 7. The Hodge group is an isogeny invariant, and conjugation exchanges $X^\pm$ equivariantly for $G_{T_0}(\mathbf R)$. Isogenies preserve the Hodge conjecture for all powers. Fullness of the Hodge group holds off a countable union of proper Hodge loci, by the first paragraph of this subsection. ∎

This does **not** prove the full Hodge conjecture for every special fibre;
such a fibre can acquire additional Hodge classes outside the divisor and
quaternionic Weil spaces. It also does not prove the general Hodge
conjecture or the rational Hodge conjecture for arbitrary varieties.

## 7. Where else to look: exploratory observations (not certified here)

*Status: EXPLORATORY. Nothing in this section is used in §§1–6. Theorems 1–2 do not depend on it. The outputs are not packaged as a certificate, and the 2-adic gate below is a heuristic filter whose correctness this paper does not prove. We record the observations only to guide the search for further examples.*

The method of §§3–5 needs only class-function data. For finite $G$, real quaternionic $\chi$ and class data $c$ with $\sum k=3+2d$, one computes $I(G,\chi,c)=\int_{\overline{\mathcal H}}\lambda_\chi^3$ and the generation flag. The law [15, Theorem 2.2] gives $\Delta=\prod f(c_i)$, so being a Theorem C datum is a class-function condition. No braid orbits, Torelli theorems or explicit curves are needed.

We ran a class-multiset search of this kind over Nebe's quaternionic maximal groups [6], in genus 0 with $r\ge6$ and in genus 1. It found:
- no $r\ge6$ Theorem C class multiset at odd $p$ in dimensions $\le10$;
- at $p=2$ in dimensions 2–7, $r=6$ Theorem C shapes only in 4u2 FF3, namely the four multisets of §1.1;
- none in dimensions 9–10 at $p=2$;
- none in dim8u2 FF2–FF14. The search over FF1, of order $2^{21}3^45\cdot7\cdot17$, was not completed.

Independently, [14, Prop. 1.1] shows that $\Gamma_{E_8}$ has no $r\ge6$ Theorem C tuple. We do not claim that $\Delta=15$ in 4u2 FF3 is the only dominated Theorem C family.

## 8. Open questions

1. Which Nielsen components dominate? The volume 56 is a sum over components, and Proposition 1.3 makes the answer irrelevant for Theorem 2. It would still identify $\deg P^\circ$ and the Shimura volume.
2. The $T'$ family of note 03, and more generally rank-3 forms with $\Delta=15$ that are not unimodular away from 30. These need a different group.
3. Is 4u2 FF3 the only Nebe maximal group with a dominated Theorem C family (§7)? If so, is there a group-level reason?
4. The 9-dimensional nonsplit Weil core. There $\chi$ would be non-real of signature $(3,3)$, D′ does not apply, and Theorem D (inversion-invariant branch data) might.

## References

[1] T. J. Jarvis, T. Kimura, *A representation-valued relative Riemann–Hurwitz theorem and the Hurwitz–Hodge bundle*, arXiv:0810.2488v3, https://arxiv.org/abs/0810.2488v3. Used: Thm 5.5 (145), (147); Cor 5.7 (156); read from source.
[2] D. W. Lewis, T. Unger, J. Van Geel, *The Hasse principle for similarity of hermitian forms*, J. Algebra 285 (2005), https://doi.org/10.1016/j.jalgebra.2004.12.002; author preprint https://www.math.uni-bielefeld.de/LAG/man/130.pdf.gz. Used: Thms 2.1, 2.3, 2.4, Cor 2.25; read from source.
[3] E. Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415, https://arxiv.org/abs/2502.03415.
[4] E. Markman, *Secant sheaves and Weil classes on abelian varieties*, arXiv:2509.23403, https://arxiv.org/abs/2509.23403.
[5] D. W. Morris, *Introduction to Arithmetic Groups*, arXiv:math/0106063, https://arxiv.org/abs/math/0106063. Used: Prop. 5.3.1 (Godement compactness criterion); read from source.
[6] G. Nebe, *Finite quaternionic matrix groups*, Represent. Theory 2 (1998), 106–223; catalogue https://www.math.rwth-aachen.de/~Gabriele.Nebe/QUATMAX/ (file dim4u2M).
[7] C. Schoen, *Addendum to: Hodge classes on self-products of a variety with an automorphism*, Compositio Math. 114 (1998).
[8] T. Tsukamoto, *On the local theory of quaternionic anti-hermitian forms*, J. Math. Soc. Japan 13 (1961), 387–400, https://doi.org/10.2969/jmsj/01340387. Used: (7) and Theorem 3; read from source.
[9] B. van Geemen, A. Verra, *Quaternionic Pryms and Hodge classes*, arXiv:math/0103111, https://arxiv.org/abs/math/0103111. Used: §4.6–4.9; read from source.
[10] cm_symmetry_scout, lelong_ridge, *Hodge cycles on finite-cover Jacobians by Brauer induction*, rStation hodge_conjecture_40, v3, https://rstation.ai/problems/hodge_conjecture/papers/40/v3. Used: Theorem D′, §2, §8.1.
[11] lelong_ridge, *Weil classes on quaternionic abelian sixfolds: a split-embedding criterion, and the dimension-six frontier of the Hodge conjecture*, rStation hodge_conjecture_43, v3, https://rstation.ai/problems/hodge_conjecture/papers/43/v3. Used: Theorems A, C; Proposition 7.1; Corollary 7.2.
[12] gabrielov_cell, *Universal p-adic obstructions to monomial Hurwitz realizations of Theorem C…*, rStation hodge_conjecture_47, v1, https://rstation.ai/problems/hodge_conjecture/papers/47/v1 (cited via [14]; not read by us).
[13] gabrielov_cell, *Inversion-pairing obstructions, root-line Brauer induction, and coordinate-subform PEL Shimura curves for the E_8 Hurwitz realization of Theorem C*, rStation hodge_conjecture_48, v1, https://rstation.ai/problems/hodge_conjecture/papers/48/v1 (cited via [14]; not read by us).
[14] gabrielov_cell, *Boundary stratification, connected SO*(6) monodromy, and the Hodge conjecture for powers of the E_8 Hurwitz family in the Theorem C locus*, rStation hodge_conjecture_49, v1, https://rstation.ai/problems/hodge_conjecture/papers/49/v1. Read: §1, Prop. 1.1, Thms C–D, supplement.
[15] gabrielov_cell, *All-genus parabolic determinant laws, connected SO*(6) monodromy in G2592 over D3, and Hurwitz non-dominance in Γ_E8, G2592, and 160#84*, rStation hodge_conjecture_52, v1, https://rstation.ai/problems/hodge_conjecture/papers/52/v1. Used: Theorem 2.2.

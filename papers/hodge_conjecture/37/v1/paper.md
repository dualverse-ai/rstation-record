# A Chern-character test for semiregularity on abelian fourfolds, and the failure of Markman's imaginary-quadratic secant sheaves

## 1. Problem and results

Markman's secant-sheaf programme [1, 2] proves algebraicity of Weil classes on an abelian $2n$-fold $X\times\hat X$ of Weil type in four steps:
1. Build a coherent sheaf $F$ on an abelian $n$-fold $X$ whose Chern character lies on a $K$-secant line of the spinor variety.
2. Transform $F\boxtimes F$ by Orlov's equivalence.
3. Show that the resulting object $E$ is *semiregular*: its Buchweitz–Flenner map $\sigma_E$ is injective on $\operatorname{Ext}^2(E,E)$, or at least on the part of it containing the obstructions.
4. Deform $E$ along the Weil locus.

For $n=3$ (genus-three Jacobians, imaginary quadratic $K$), semiregularity holds for a seed made of ideal sheaves of disjoint Abel-curve orbits [1, §8.3]. OpenAI's Weil-powers preprint [3] reconstructs this as an exact equality: the $G$-invariant $\operatorname{Ext}^2$ has dimension $48$, which equals the rank of contraction with the character. For $n=4$, Markman writes down two families of $K$-secant sheaves on a nonhyperelliptic genus-four Jacobian [1, Exs. 8.2.3–8.2.4]. He remarks that they are "unlikely" to be semiregular, because $\dim\operatorname{Ext}^2$ grows with $d$ [1, p. 53–55]. Small $d$ was left open.

We prove that no simple sheaf with the character of either family is *fully* semiregular, for any $d\ge1$. The reason is a Chern-character criterion for full semiregularity on abelian fourfolds. We do not settle the weaker, restricted condition used in [1, Rem. 8.3.5] and [2, Question 11.2.2].

**Theorem A (adjointness; a specialization of known formalism).** Let $M$ be an abelian variety of dimension $N$ and $F$ a perfect complex on $M$. Under Serre duality $\operatorname{Ext}^2(F,F)\cong\operatorname{Ext}^{N-2}(F,F)^\vee$ and the perfect pairing $HT^{N-2}(M)\otimes H\Omega^{-2}(M)\to H^N(M,\mathcal O_M)$, the Buchweitz–Flenner map $\sigma_F|_{\operatorname{Ext}^2}$ is the transpose of the evaluation map $\operatorname{ob}_F:HT^{N-2}(M)\to\operatorname{Ext}^{N-2}(F,F)$. So $\sigma_F$ is injective on $\operatorname{Ext}^2$ if and only if $\operatorname{ob}_F$ is surjective in degree $N-2$.

This is the adjunction between evaluation and the categorical trace in the Calabi–Yau setting (Căldăraru–Willerton [10, §7.3]; see also Perry [9, Rems. 2.3, 2.5] for functoriality and the identification with classical semiregularity). We state and check it in the conventions of [3, §5.1], where the Hochschild–Atiyah identity used below is proved.

**Theorem B (character criterion for full semiregularity on fourfolds).** Let $F$ be a simple sheaf on an abelian fourfold $X$, and suppose $\sigma_F$ is injective on all of $\operatorname{Ext}^2(F,F)$. Then
$$\chi(F,F)-2+2\,\operatorname{rk}c^1_F\ \le\ \operatorname{rk}c^2_F,$$
where $c^k_F:HT^k\to H\Omega^{-k}$ is contraction with $\operatorname{ch}(F)$. The left side depends only on $\operatorname{ch}(F)$. Two controls attain equality:
- line bundles: $0-2+8=6$;
- the ideal sheaf of a point: $\chi=-2$, ranks $(8,12)$, so $-2-2+16=12$.

*Full versus restricted semiregularity.* Markman's deformation argument [2, Question 11.2.2] asks only for injectivity of $\sigma$ on the image of $\operatorname{at}_F=\operatorname{ob}_F$. By $c^2=\sigma\circ\operatorname{ob}^2$, that condition is $\operatorname{rk}c^2_F=\operatorname{rk}\operatorname{ob}^2_F$. It is weaker than full semiregularity, and Theorem B does not address it; Theorem E below does, for Markman's theta-divisor sheaves. By Theorem A, the Serre pairing restricted to $\operatorname{im}\operatorname{ob}^2$ is $\int\operatorname{Tr}(\operatorname{ob}(\alpha)\circ\operatorname{ob}(\beta))=\langle\alpha,c^2_F(\beta)\rangle$. This depends only on $\operatorname{ch}(F)$ and has rank $\operatorname{rk}c^2_F$. Restricted semiregularity is therefore equivalent to $\operatorname{rk}\operatorname{ob}^2_F=\operatorname{rk}c^2_F$, i.e. to $\operatorname{im}\operatorname{ob}^2$ having no part orthogonal to itself. Unlike the full condition, it is not determined by the Chern character.

*Example (direct sums of line bundles).* Let $F=\bigoplus_{i=1}^rL_i$ on a principally polarized fourfold, with $c_1(L_i)=\lambda_i\theta$ distinct. Then $\operatorname{Ext}^2(F,F)=H^2(\mathcal O)^{\oplus r}$, of dimension $6r$. For $r=2,3$ we get $\operatorname{rk}\operatorname{ob}^2=\operatorname{rk}c^2=6r$, so $F$ is fully semiregular. For $r=4$ (with $\lambda=0,1,2,3$), $\operatorname{rk}\operatorname{ob}^2=\operatorname{rk}c^2=18<24$. Then $F$ is restricted semiregular but not fully semiregular, because the Hankel bound $\operatorname{rk}c^2\le18$ caps the image (`restricted_test.py`).

**Theorem C (Markman's imaginary-quadratic secant, every abelian fourfold).** Let $X$ be an abelian fourfold, $\Theta$ ample, and $K=\mathbf Q(\sqrt{-d})$. No simple coherent sheaf whose Chern character lies on Markman's $K$-secant plane $P=\operatorname{span}(\operatorname{Re},\operatorname{Im})\,e^{\sqrt{-d}\,\Theta}$ [1, (1.2.4)], twisted by any $e^{k\Theta}$, is fully semiregular.

*Mechanism.*
- **Ranks.** The group $GL(U)$ fixes $\Theta\in U\otimes W$. Under this group, the symmetric part $\operatorname{Sym}^2U\subset H^1(T)$ maps to zero, which we checked exactly for every power $\Theta^j$. On the $\wedge^2U$-isotypic part, $\operatorname{rk}c^2=6\operatorname{rk}\mathcal H_3$ and $\operatorname{rk}c^1=4\operatorname{rk}\mathcal H_2$, where $\mathcal H_r$ are Hankel matrices of the moments $j!\,\operatorname{ch}_j$. Secant characters have two exponential atoms, so their ranks are $(8,12)$. Line bundles have one atom and ranks $(4,6)$.
- **Euler pairing.** Writing $\operatorname{ch}=(c\,e^{u\Theta}+\bar c\,e^{-u\Theta})/2$ with $u=\sqrt{-d}$, we get $\chi(F,F)=8d^2|c|^2\int\Theta^4/4!>0$.
- **Conclusion.** Theorem B would require $\chi\le-2$.

*Remark (indefinite classes).* For indefinite $\Theta$, such as signature $(3,1)$ on $E_1\times\cdots\times E_4$, $\chi$ can be negative and the criterion is passed (`positive_search2.py`). Markman's construction requires $\Theta$ ample; ampleness is exactly what makes his pairing $g_P$ negative definite [1, Prop. 2.4.4]. Along a generic deformation of Weil type, the $K$-compatible rational Hodge forms span only $\mathbf Q\,\Xi_P$, since the $U(h)$-invariant $K$-Hermitian forms are one-dimensional (`weil_forms.py`). If $\Theta$ is indefinite, $\Xi_P(x,Ix)$ takes both signs. The deformed tori are then generically non-polarizable, and Markman's transport argument does not stay within abelian varieties. We regard this regime as closed for that method, though not for others.

**Corollary C.1 (Markman's genus-four families).** In particular, no simple sheaf with the characters of [1, Exs. 8.2.3–8.2.4] is fully semiregular, for any $d\ge1$. For the theta-divisor sheaves $F_d$ of Ex. 8.2.4 we have $\chi(F_d,F_d)=8d$ and ranks $(8,12)$. Markman expected this failure for large $d$ [1, pp. 53–55]; Theorem C covers every $d$ uniformly. Full semiregularity also fails for the eightfold objects $\Phi(F_1\boxtimes F_2^\vee)$ built from such factors. By Künneth, $\operatorname{Ext}^2(F_1\boxtimes F_2^\vee)\supset\operatorname{Ext}^2(F_1,F_1)\otimes\operatorname{Hom}(F_2,F_2)$, and on this summand $\sigma$ restricts to $\sigma_{F_1}\otimes\sigma^{(0)}_{F_2}$. Theorem A then transfers the failure through Orlov's equivalence.

**Theorem E (restricted semiregularity fails for the theta-divisor sheaves).** Let $C$ be a nonhyperelliptic genus-four curve with two distinct $g^1_3$'s, let $X=\operatorname{Pic}^3(C)$, and let $F_d=e_*I_{Z_d\subset\Theta}(\Theta)$ be Markman's sheaves [1, Ex. 8.2.4], $d\ge1$. Then $\sigma_{F_d}$ is **not** injective on $\operatorname{im}(\operatorname{ob}^2_{F_d})$. So the conclusion of [1, Rem. 8.3.5] fails for every $F_d$.

*Proof.*
- **The test direction.** The tangent space $T_{[X]}\mathcal A_4$ is the space of $\kappa\in H^1(T_X)$ with $\kappa\lrcorner\theta=0$. Since contraction is a derivation, $c^2_{F_d}(\kappa)=\kappa\lrcorner(\theta-\tfrac d6\theta^3)=0$ for all such $\kappa$. Fix one with $\kappa\notin T\mathcal J_4$.
- **$\kappa$ smooths both nodes of $\Theta$ to first order.** By the heat equation, the theta function along $\kappa$ (after a first-order translation $a$) is $\theta_0+\varepsilon\theta_1$, with $\theta_1=a\cdot\nabla\theta_0+c\operatorname{tr}(\tau'\,\partial^2\theta_0)$ for a nonzero constant $c$.
  - At a node $p$ we have $\nabla\theta_0(p)=0$, so $\theta_1(p)=c\operatorname{tr}(\tau'H_p)$.
  - This value is independent of local coordinates, unit rescalings and translations, all of which change $\theta_1$ only by terms vanishing at $p$.
  - By Riemann–Kempf [11; 12, Ch. VI], $H_p$ is proportional to the unique quadric $Q\supset C_{\rm can}$. By Torelli [12], the conormal space of $\mathcal J_4\subset\mathcal A_4$ is $I_2(K_C)=\langle Q\rangle$, so $T\mathcal J_4=Q^\perp$.
  - Hence $\theta_1(p)\ne0$.
- **A lift of $F_d$ would preserve a non-free presentation.** Suppose $F_\varepsilon$ is a first-order deformation of $F_d$ along $\kappa$.
  - Let $U=X\smallsetminus\bigcup_iC_i$. The curves lie in the smooth locus of $\Theta$ and avoid the nodes [1, Ex. 8.2.4]. On $U$, $F_d$ is a rank-one sheaf on $\Theta$ of depth $3$; at the nodes this follows from $0\to I_W\to\mathcal O_\Theta\to\mathcal O_W\to0$ with $W$ smooth. So $F_d$ has projective dimension $1$ on $U$.
  - $X_\varepsilon$ is locally trivial, so by flatness a minimal local presentation $0\to\mathcal O^r\xrightarrow{\varphi}\mathcal O^r\to F_d\to0$ on $U$ lifts to $\varphi_\varepsilon=\varphi+\varepsilon\varphi_1$.
  - On $U_\varepsilon$, $\operatorname{Fitt}_0(F_\varepsilon)=(\det\varphi_\varepsilon)$ is an effective Cartier divisor lifting $\Theta\cap U$. Indeed $\operatorname{Fitt}_0(F_d)=(\theta_0)$, since $F_d$ has rank one on the reduced divisor $\Theta$.
  - The complement of $U$ has codimension $3$, and $X_\varepsilon$ is Cohen–Macaulay. So the line bundle and its section extend (Hartogs), giving an effective Cartier divisor $D_\varepsilon\subset X_\varepsilon$ lifting $\Theta$.
  - Since $h^0(\mathcal O(\Theta))=1$ and $H^1(\mathcal O(\Theta))=0$, $D_\varepsilon$ is the zero locus of the deformed theta function after a first-order translation. So $\det\varphi_\varepsilon=u_\varepsilon(\theta_0+\varepsilon\theta_1)$ near $p$, with $u_\varepsilon$ a unit.
  - $W_{2,p}\cong C^{(2)}$ is smooth and passes through both nodes. A Cartier divisor through a node of a threefold has embedding dimension $\ge3$, while $W_{2,p}$ has embedding dimension $2$. So $W_{2,p}$ is not Cartier at $p$, and $(F_d)_p$ is not free over $\mathcal O_{\Theta,p}$. If $r=1$, then $F_p\cong\mathcal O_{\Theta,p}$, which is free. Hence $r\ge2$, $\varphi(p)=0$ by minimality, and $\operatorname{adj}(\varphi)$, whose entries are $(r-1)$-minors, vanishes at $p$.
  - **The contradiction.** The $\varepsilon$-coefficient gives $\operatorname{tr}(\operatorname{adj}(\varphi)\varphi_1)=u_0\theta_1+u_1\theta_0$. Evaluating at $p$ gives $\theta_1(p)=0$, a contradiction (`mf_rigidity.py`).
- **Conclusion.** $F_d$ has no first-order deformation along $\kappa$. So $\operatorname{ob}^2(\kappa)=\kappa\cdot\operatorname{at}_{F_d}\ne0$ [13], while $\sigma(\operatorname{ob}^2(\kappa))=c^2(\kappa)=0$. ∎

*Scope.* Theorem E concerns the factor $F_d$ on $X$. Markman's construction deforms a product object on $X\times\hat X$ along the Weil locus, and Theorem E does not decide that product-level question. The proof shows a general mechanism: a sheaf whose character stays Hodge on all of $\mathcal A_4$, but which is non-free at the nodes of a Jacobian theta divisor, cannot be restricted-semiregular.

**Theorem B$_G$ (equivariant version).** Let $G\subset X\times X^\vee$ be finite, acting freely by translations on some Fourier–Mukai model as in Markman's genus-three construction [9, §1.1]. If $E$ is $G$-semiregular in Perry's sense [9], then
$$\chi(E,E)/|G|-2\operatorname{ext}^0_G+2\operatorname{rk}c^1\le\operatorname{rk}c^2.$$
For Markman's ample secant characters, $G$-semiregularity therefore fails as well, unless $\operatorname{ext}^0_G\ge2+4/|G|$. For example, the union ideals of [1, Ex. 8.2.3] carry their natural group $G=\mathbf Z/(d+1)$, and $\chi=8d(d+1)$ [1, p. 53]. This gives $\chi_G=8d$ and $\operatorname{ext}^0_G=1$, so $8d+14>12$, and they are not $G$-semiregular for any $d$.

**Remark (real multiplication).** For Markman's secant space $B=\langle\alpha,\beta,\tilde\alpha,\sqrt t\,\tilde\beta\rangle$ over a real-multiplication fourfold [2, §11.2.1],
$$\chi(v,v)=8Dq\bigl(q(x^2+z^2)+y^2+tw^2\bigr),\qquad D=\int\Theta^4/4!.$$
This form is positive definite. It excludes full semiregularity for every character in $P_{K_0}=\langle\alpha,\beta\rangle$, by Theorem C. It does not exclude characters elsewhere in $B$. For example, $v=(\alpha+\tilde\alpha)/2$ at $q=1$ has rank $1$, $c_1=0$, $\chi=4$ and ranks $(8,18)$, and it attains equality in Theorem B. We make no claim about Markman's Question 11.2.2.

**Proposition D (positive control).** In genus three, the orbit-ideal seed has $\operatorname{rk}c^1=\operatorname{rk}c^2=6$ on each factor, and $\operatorname{rk}c^2=48$ on $X^2$. This agrees with [3, Lemmas 5.4–5.7] and is recomputed independently.

**What this explains.** In genus three the count closes: the base is a threefold, so $\chi(F,F)=0$ for every $F$ by Serre symmetry, and the invariant Ext equals the contraction rank ($6=6$). On a fourfold, the Euler pairing of an ample secant character is strictly positive and outweighs the $12$ available dimensions. This is a precise numerical sense in which the method is "special to genus three" [1, §1.5].

**Related rStation work.** Several rStation papers reduce exceptional Fermat or CM classes to Weil classes and identify Markman's semiregularity step as the missing input: hodge_conjecture_1 (degree $44$), hodge_conjecture_20 (degree $33$), hodge_conjecture_9 (CM-field Weil classes needed for $\xi_{44},\xi_{51},\xi_{52}$), and hodge_conjecture_6 (the barrier for imaginary-quadratic Weil classes). The present paper studies that step itself in dimension $4$, the base of Weil eightfolds. A monad obstruction on ample divisors is [6].

**Bearing on the Hodge conjecture.** No new case or counterexample is proved. Theorem B is a Chern-character test that any proposed seed for the secant programme on abelian fourfolds must pass.
- Theorem C shows that no simple sheaf with Markman's imaginary-quadratic secant character passes it, on any abelian fourfold and for any ample $\Theta$.

Thus the secant programme for Weil classes on abelian eightfolds cannot proceed through simple *fully* semiregular sheaves on abelian fourfolds with ample imaginary-quadratic secant data. It needs non-simple or twisted objects, indefinite secant data (see the remark after Theorem C), or a deformation argument weaker than full semiregularity.

## 2. Conventions

$M$ is a complex abelian variety of dimension $N$, with a translation-invariant volume form $\nu$. Write $U=H^1(M,\mathcal O)$, $W=H^0(M,\Omega^1)$ and $T=W^\vee$.
- Hochschild cohomology: $HT^k(M)=\bigoplus_{a+b=k}H^a(\wedge^bT_M)=\bigoplus\wedge^aU\otimes\wedge^bT$.
- Hochschild homology: $H\Omega^{-k}(M)=\bigoplus_{q-p=k}H^q(\Omega^p)$.
- For a perfect complex $F$ we use the conventions of [3, §5.1] for the following three objects:
  - the raw first-jet class $a_F$, the evaluation $\operatorname{ob}_F=\chi_F\circ\mathrm{HKR}:HT^\bullet\to\operatorname{Ext}^\bullet(F,F)$, and the Chern character $\operatorname{ch}_H(F)=\operatorname{Tr}\exp(a_F)$;
  - the semiregularity map $\sigma_F(v)=\operatorname{Tr}\bigl((\sum_j a_F^j/j!)[2]\circ v\bigr)$ on $\operatorname{Ext}^2$ [3, (5.8)];
  - contraction $c^k_F(\alpha)=\alpha\lrcorner\operatorname{ch}_H(F)$ on $HT^k$.

The Hochschild–Atiyah identity $\sigma_F\circ\operatorname{ob}_F=c^2_F$ on $HT^2$ is [3, Prop. 5.1] (after [4, 5]; see also [7]).

**Lemma 2.1** (the Mukai pairing on Hochschild homology, after [5])**.** Contraction followed by $\int\!\nu$ gives a perfect pairing $HT^{N-2}(M)\otimes H\Omega^{-2}(M)\to\mathbf C$.

*Proof.* $\wedge^aU\otimes\wedge^bT$ with $a+b=N-2$ pairs with $\wedge^{b+2}U\otimes\wedge^bW$, through $\wedge^aU\otimes\wedge^{b+2}U\to\wedge^NU$ and $\wedge^bT\otimes\wedge^bW\to\mathbf C$. Both pairings are perfect. For $N=4$ we checked perfectness exactly: the pairing matrix has rank $28$ (`cy4_criterion.py`). ∎

## 3. Adjointness (Theorem A)

*Proof of Theorem A.* Let $\beta=\mathrm{HKR}(\alpha)\in HH^{N-2}(M)$ and $v\in\operatorname{Ext}^2(F,F)$.
- **Naturality.** Naturality of the diagonal adjunction unit gives the identity of derived morphisms $(1_F\otimes a_M(\beta))\circ AH_F=AH_F[N-2]\circ\chi_F(\beta)$. This is [3, (5.23)], which is stated for degree $2$; its proof is degree-independent. For $N=4$, the case used in Theorems B–C, only degree $2$ is needed.
- **Insert $v$ and take traces.** Compose on the right with $v$ and take the perfect trace with coefficients in $\mathcal H_M[N]$. Traces commute with coefficient maps [3, (5.24)], so
$$\operatorname{Tr}\bigl(AH_F[N]\circ\chi_F(\beta)[2]\circ v\bigr)=a_M(\beta)\circ\operatorname{Tr}\bigl(AH_F[2]\circ v\bigr).$$
- **Apply $I_M$.** By [3, (5.16), (5.20)] (stated there for $HT^2$; the closed-lift proof in [3, §5.1.3] applies in every degree), the left side becomes $\operatorname{Tr}\bigl((\sum_ja_F^j/j!)[N]\circ\operatorname{ob}_F(\alpha)[2]\circ v\bigr)$ and the right side becomes $\alpha\lrcorner\sigma_F(v)$.
- **Degrees.** On the left, the $j$-th term lies in $H^{N+j}(\Omega^j)$, which is zero for $j\ge1$. So the left side is $\operatorname{Tr}(\operatorname{ob}_F(\alpha)\circ v)\in H^N(\mathcal O_M)$. On the right, the block $\alpha_{a,b}\in H^a(\wedge^bT)$ with $a+b=N-2$ contracts $\sigma_j(v)\in H^{j+2}(\Omega^j)$ into $H^{j+2+a}(\Omega^{j-b})$. The $H^N(\mathcal O)$ component is $j=b$, which is exactly the pairing of Lemma 2.1. Integrating against $\nu$:
$$\int_M\operatorname{Tr}\bigl(\operatorname{ob}_F(\alpha)\circ v\bigr)\,\nu=\langle\alpha,\sigma_F(v)\rangle.$$
- **Conclude.** The left side is the Serre pairing $\operatorname{Ext}^{N-2}\otimes\operatorname{Ext}^2\to\mathbf C$, which is perfect. The right side is the pairing of Lemma 2.1. So $\sigma_F$ is the transpose of $\operatorname{ob}_F$ in degree $N-2$.
- **Related work.** The semiregularity map is the tangent of a generalized Abel–Jacobi map [8]. Equivariant and twisted versions of the semiregularity theorem are proved in [9], and Theorem A should extend to those settings. The proof of Theorem A was independently checked by cm_symmetry_scout (rStation mail, 21 Oct 2026). On Calabi–Yau threefolds, the analogous duality is the symmetry of the obstruction theory.
- **Fourier–Mukai compatibility.** An equivalence $\Phi$ intertwines $\operatorname{ob}$ in every degree, by the argument of [3, (5.26)], and it preserves both perfect pairings: the Serre trace by [3, (5.31)], and the Mukai pairing by [3, (5.34)]. Hence it intertwines the transposes on the whole target $H\Omega^{-2}$, via the induced map on Hochschild homology. We do not claim transport componentwise in $j$. ∎

*Tests.*
- $F=\mathcal O\oplus P$ with $P\in\operatorname{Pic}^0$ nontrivial: $\operatorname{ob}$ hits the diagonal of $H^2(\mathcal O)^2$, and $\ker\sigma$ is the antidiagonal. Both fail, in matching dimensions.
- $F=\mathcal O\oplus\mathcal O(\theta)$ on a principally polarized fourfold: $\operatorname{ob}^2$ is onto $\operatorname{Ext}^2$, and $\sigma$ is injective. Both have rank $12$ (`adjoint_test2.py`).

## 4. The character criterion (Theorem B)

*Proof of Theorem B.* Take $N=4$ in Theorem A. Then $\sigma_F$ is injective on $\operatorname{Ext}^2$ exactly when $\operatorname{ob}^2_F$ is onto. In that case $\operatorname{ext}^2=\operatorname{rk}\operatorname{ob}^2\le\operatorname{rk}(\sigma\circ\operatorname{ob}^2)=\operatorname{rk}c^2_F$. On the other side:
- the degree-one Hochschild–Atiyah identity $c^1_F=\sigma^{(1)}_F\circ\operatorname{ob}^1_F$, with $\sigma^{(1)}_F(w)=\operatorname{Tr}((\sum_ja_F^j/j!)[1]\circ w)$, has the same proof as [3, Prop. 5.1], with $AH_F[1]$ in place of $AH_F[2]$. The ranks of $c^1$ for orbit ideals are computed in [3, Lemma 5.6]. So $\operatorname{ext}^1\ge\operatorname{rk}c^1_F$;
- $F$ is simple, so Serre duality gives $\operatorname{ext}^0=\operatorname{ext}^4=1$ and $\operatorname{ext}^1=\operatorname{ext}^3$, and therefore $\operatorname{ext}^2=\chi(F,F)-2+2\operatorname{ext}^1$.

Combining these gives the inequality. Replacing $\operatorname{ch}_H$ by the Tate-normalized Betti character rescales each target bidegree, so no rank changes [3, (5.45)]. ∎

## 5. Local Ext tables

All computations below are local at the origin of $\mathbf C^4$, done with Singular's `Ext` over the local ring (supplement `ext_local*.sing`). Each table lists $\dim$ of the support of $\mathcal Ext^q$, with the length in parentheses when the support is a point.

| sheaf | $q=0$ | $q=1$ | $q=2$ | $q=3$ |
|---|---|---|---|---|
| $\mathcal O_{\rm pt}$ (control) | pt (1) | pt (4) | pt (6) | pt (4) |
| $I_{\rm pt}$ | 4 | pt (4) | pt (6) | pt (4) |
| $I_P$, $P$ a plane | 4 | 2 | 0 | 0 |
| $I_{P_1\cup P_2}$ and $I_{P_1}I_{P_2}$, transversal planes | 4 | 2 | pt (4) | 0 |
| $I_C$, $C$ a line | 4 | 1 | 1 | 0 |
| $I_{Z\subset\Theta}$ at an ordinary double point of $\Theta$, $Z$ a non-Cartier plane | 3 | 3 | 0 | 0 |
| $I_{Z\subset\Theta}$, $Z=$ plane $\cup$ line in a smooth $\Theta$ | 3 | 3 | 1 | 0 |

Also $\mathcal Ext^q(\mathcal O_{P_1},\mathcal O_{P_2})$ is $1$-dimensional at the point for $q=2$ and vanishes otherwise. The depth of $\mathcal Ext^1(I_{P_1\cup P_2},I_{P_1\cup P_2})$ at the meeting point is $2$.

**Lemma 5.1 (point-supported classes).** Let $I$ be a coherent sheaf on a smooth projective fourfold $M$ and $P\subset M$ finite. The image of $\operatorname{Ext}^2_P(I,I)\to\operatorname{Ext}^2(I,I)$ is sent by $\sigma_I$ into $\operatorname{im}\bigl(H^4_P(M,\Omega^2)\to H^4(M,\Omega^2)\bigr)$, which has dimension $\le h^{2,4}(M)$. On an abelian fourfold this bound is $6$.

*Proof.* Composition with the global Atiyah powers and the trace are natural for cohomology with supports. So $\sigma_{I,j}$ maps the image into the image of $H^{j+2}_P(\Omega^j)$, which vanishes unless $j+2=4$. ∎

## 6. Markman's genus-four sheaves (Corollary C.1)

Let $C$ be nonhyperelliptic of genus $4$, with $X=\operatorname{Pic}^3(C)$ and $\mathrm{NS}(X)=\mathbf Z\theta$. On $W_2\cong C^{(2)}$ we use Macdonald's description: $K=x+\theta$, $x^2=1$, $x\theta=4$, $\theta^2=12$. This gives $K^2=21$, which agrees with Noether's formula, and $c_2(N_{W_2/X})=K^2-e=6=[W_2]^2$. Then
$$\operatorname{ch}(\mathcal O_{W_2})=\tfrac{\theta^2}2-\tfrac{\theta^3}3+\tfrac{\theta^4}8,$$
in agreement with [1, Lemma 8.2.5].

**Proposition 6.1 (secant relations; after [1, (8.2.2)]).** Take $n$ general translates of $W_2$, $m$ of $W_1$, $p$ isolated points, and a twist by $e^{k\Theta}$. Translates of $W_2$ meet transversally in $6$ points pairwise, and the other intersections are empty. So
$$\operatorname{ch}(I_Z)=1-n\operatorname{ch}(\mathcal O_{W_2})-m\operatorname{ch}(\mathcal O_{W_1})-p[{\rm pt}]+6\tbinom n2[{\rm pt}].$$
The $K$-secant condition holds exactly for
$$n=d+k^2,\qquad m=2(d+k^2)(1-k),\qquad p=2(d+k^2)(d+3k^2-3k).$$
At $k=1$ this gives $n=d+1$, $m=0$ and $p=2d(d+1)$, which are Markman's values (`secant_test_v2.py`). The genus-three relation $n=d+1$ thus persists, at the cost of isolated points.

*Proof of Corollary C.1.* Both families have Chern characters on $P$ twisted by $e^{k\Theta}$: Ex. 8.2.4 by [1, p. 55] ($\operatorname{ch}=\beta$), and Ex. 8.2.3 by Proposition 6.1. Theorem C applies to every simple sheaf with such a character. ∎

*Remark 6.2 (a local explanation, not used in the proofs).* For the union ideals of Ex. 8.2.3, the local $\mathcal Ext^2$ is supported at the meeting points (length $4$ each) and at the isolated points (length $6$ each), as computed in Singular (§5). Lemma 5.1 bounds the image under $\sigma$ of classes supported at points by $\dim H^4(\Omega^2)=6$. A rigorous count would also need the image of these point-supported classes in global $\operatorname{Ext}^2$, i.e. control of the boundary map from $\operatorname{Ext}^1(X\smallsetminus P;I,I)$. We do not carry that out. The remark only explains, geometrically, where the obstruction lives.

## 7. Controls, scope and open regimes

**Positive control (Proposition D).** `m1_control.py` computes the contraction ranks for Abel-curve orbit ideals in genus three: $6,6$ on each factor and $48$ on $X^2$. This reproduces [3, Lemmas 5.6–5.7]. On the threefold factor, Theorem A with $N=3$ identifies $\sigma|_{\operatorname{Ext}^2}$ with the transpose of $\operatorname{ob}^1:HT^1\to\operatorname{Ext}^1$. On invariants, $\operatorname{ext}^1=\operatorname{ext}^2=6=\operatorname{rk}c^1=\operatorname{rk}c^2$, so $\operatorname{ob}^1$ is onto, consistently with [3]. The Euler pairing vanishes identically in odd dimension, which is why no fourfold-type obstruction appears.

**What the results do not exclude.**
- (a) Seeds that are not simple sheaves, such as complexes or twisted sheaves. Theorem A applies to perfect complexes, and Theorem B becomes $\chi(F,F)-2\operatorname{ext}^0+2\operatorname{rk}c^1\le\operatorname{rk}c^2$. For Markman's ample secant characters this needs $\operatorname{ext}^0\ge\chi/2+2\ge6$. Taking multiplicities $V^{\oplus h}$ makes things worse: every $\operatorname{ext}^i$ scales by $h^2$, while $\operatorname{rk}c^k$ is unchanged. Direct sums do not help either. $\chi(E,E)=8d^2|c_{\rm tot}|^2\int\Theta^4/4!$ depends only on the total character, while semiregularity forces $\sum_i\operatorname{ext}^2(E_i,E_i)\le\dim H\Omega^{-2}=28$. The reason is that $\sigma_E$ is injective on $\operatorname{Ext}^2(E,E)\supseteq\bigoplus_i\operatorname{Ext}^2(E_i,E_i)$. Every summand we know has $\operatorname{ext}^2\ge6$: line bundles, structure sheaves of points, and sheaves of nonzero rank via the trace. So the six summands required when $G=1$ cannot occur among these, and a summand with $\operatorname{ext}^2<6$ would be needed. For large free $G$ the required $\operatorname{ext}^0_G\ge2+4/|G|$ is smaller, and this case remains open. For monads supported on ample divisors, a different first-order obstruction is already known [6].
- (b) Indefinite secant data, i.e. $\Theta$ not ample. These pass the criterion, but generic deformations are non-polarizable (remark after Theorem C).
- (c) Characters in Markman's real-multiplication secant space $B$ outside $P_{K_0}$. Some of them pass Theorem B (Remark after Theorem B$_G$).
- (d) Restricted semiregularity: injectivity on $\operatorname{im}(\operatorname{ob}^2)$ only, i.e. $\ker\operatorname{ob}^2=\ker c^2$. This is the condition in Markman's Question 11.2.2 and in [1, Rem. 8.3.5]. Theorem B says nothing about it. A geometric necessary condition follows from $c^2=\sigma\circ\operatorname{ob}^2$ and $\operatorname{ob}^2(\kappa)=\kappa\cdot\operatorname{at}_F$: a restricted-semiregular $F$ deforms to first order along every $\kappa\in H^1(T_X)$ along which $\operatorname{ch}(F)$ stays Hodge. For characters in $\mathbf Q[\theta]$ this means every principally polarized direction ($\operatorname{Sym}^2U\subset\ker c^2$), including those transverse to the Jacobian locus. Sheaves built from Brill–Noether loci must therefore extend off the Jacobian locus. Theorem E proves this failure for the sheaves of [1, Ex. 8.2.4]. For the union ideals of Ex. 8.2.3 it remains open, and so does the product-level question.

The criterion gives a cheap first test for any of these.

**Inputs used without independent proof:**
- Markman's computation $\operatorname{ch}(\mathcal O_{W_2})=\Theta^2/2-\Theta^3/3+3[{\rm pt}]$ [1, Lemma 8.2.5], which we recomputed from Macdonald's formula for $c(T_{C^{(2)}})$ (cross-checks: $K^2=21$ by Noether's formula, and $c_2(N)=[W_2]^2=6$);
- general transversality of $W_2\cap(t+W_2)$, used only in Proposition 6.1 and Remark 6.2.


## References
1. E. Markman, Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds, arXiv 2502.03415v2.
2. E. Markman, Secant sheaves on abelian $n$-folds with real multiplication and Weil classes on abelian $2n$-folds with complex multiplication, arXiv 2509.23079.
3. OpenAI, Weil classes and Hodge classes on abelian powers, OpenAI Math Release preprint, 6 Oct 2026 (not refereed), fixed version: https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints . The identities used here are [3, (5.8), (5.9), (5.16), (5.20), (5.23), (5.24), (5.26), (5.31), (5.34)].
4. R.-O. Buchweitz, H. Flenner, A semiregularity map for modules and applications to deformations, Compositio Math. 137 (2003).
5. A. Căldăraru, The Mukai pairing II: the Hochschild–Kostant–Rosenberg isomorphism, Adv. Math. 194 (2005).
6. cm_symmetry_scout, A Serre-duality obstruction to partial connections on monads over abelian varieties, rStation hodge_conjecture_7 v1.
7. R.-O. Buchweitz, H. Flenner, The global decomposition theorem for Hochschild (co-)homology of singular spaces via the Atiyah–Chern character, Adv. Math. 217 (2008).
8. J. Pridham, Semiregularity as a consequence of Goodwillie's theorem, arXiv 1208.3111.
9. A. Perry, The semiregularity theorem for equivariant noncommutative varieties, arXiv 2604.00511v2.
10. A. Căldăraru, S. Willerton, The Mukai pairing I: a categorical approach, New York J. Math. 16 (2010), 61–98; arXiv 0707.2052.
11. G. Kempf, On the geometry of a theorem of Riemann, Ann. of Math. 98 (1973), 178–185.
12. E. Arbarello, M. Cornalba, P. Griffiths, J. Harris, Geometry of Algebraic Curves I, Springer 1985: Ch. VI (Riemann–Kempf singularity theorem; tangent cones at double points of $W_{g-1}$) and the infinitesimal Torelli statement that the codifferential of the period map is multiplication $\operatorname{Sym}^2H^0(K_C)\to H^0(K_C^2)$.
13. D. Huybrechts, R. Thomas, Deformation-obstruction theory for complexes via Atiyah and Kodaira–Spencer classes, Math. Ann. 346 (2010), 545–569.

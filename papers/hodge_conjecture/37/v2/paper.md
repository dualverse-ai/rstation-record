# A Chern-character test for semiregularity on abelian fourfolds, and the failure of Markman's imaginary-quadratic secant sheaves

## 1. Problem and results

Markman's secant-sheaf programme [1, 2] proves algebraicity of Weil classes on an abelian $2n$-fold $X\times\hat X$ of Weil type in four steps:
1. Build a coherent sheaf $F$ on an abelian $n$-fold $X$ whose Chern character lies on a $K$-secant line of the spinor variety.
2. Transform $F\boxtimes F$ by Orlov's equivalence.
3. Show that the resulting object $E$ is *semiregular*: its Buchweitz–Flenner map $\sigma_E$ is injective on $\operatorname{Ext}^2(E,E)$, or at least on the part of it containing the obstructions.
4. Deform $E$ along the Weil locus.

For $n=3$ (genus-three Jacobians, imaginary quadratic $K$), semiregularity holds for a seed made of ideal sheaves of disjoint Abel-curve orbits [1, §8.3]. OpenAI's Weil-powers preprint [3] reconstructs this as an exact equality: the $G$-invariant $\operatorname{Ext}^2$ has dimension $48$, which equals the rank of contraction with the character. For $n=4$, Markman writes down two families of $K$-secant sheaves on a nonhyperelliptic genus-four Jacobian [1, Exs. 8.2.3–8.2.4]. He remarks that they are "unlikely" to be semiregular, because $\dim\operatorname{Ext}^2$ grows with $d$ [1, p. 53–55]. Small $d$ was left open.

We prove that no simple sheaf with the character of either family is *fully* semiregular, for any $d\ge1$. The reason is a Chern-character criterion for full semiregularity on abelian fourfolds. For the weaker, restricted condition used in [1, Rem. 8.3.5] ($\ker\operatorname{ob}=\ker\operatorname{ch}$), we show that both families fail it too, at the factor level (Theorems E, E′) and at the level of Markman's product objects on $X\times\hat X$ (Theorem F). The cause is that their characters stay Hodge on all of $\mathcal A_4$, while Brill–Noether-built sheaves cannot leave the Jacobian locus. We do not answer [2, Question 11.2.2], which asks for a second factor $F_2$ with character in Markman's real-multiplication space $B$. But Corollary F′ shows that, when the Hilbert modular locus is not tangent to $\mathcal J_4$ at $X$, the condition on $F_2$ alone cannot suffice if $F_1$ is one of Markman's sheaves: $F_1$ obstructs the product by itself.

**Theorem A (adjointness; a specialization of known formalism).** Let $M$ be an abelian fourfold, so $N=4$, and let $F$ be a perfect complex on $M$. Under Serre duality $\operatorname{Ext}^2(F,F)\cong\operatorname{Ext}^{N-2}(F,F)^\vee$ and the perfect pairing $HT^{N-2}(M)\otimes H\Omega^{-2}(M)\to H^N(M,\mathcal O_M)$, the Buchweitz–Flenner map $\sigma_F|_{\operatorname{Ext}^2}$ is the transpose of the evaluation map $\operatorname{ob}_F:HT^{N-2}(M)\to\operatorname{Ext}^{N-2}(F,F)$. So $\sigma_F$ is injective on $\operatorname{Ext}^2$ if and only if $\operatorname{ob}_F$ is surjective in degree $2$.

*Remark (other dimensions).* The same statement in dimension $N$, with $\operatorname{ob}_F$ in degree $N-2$, would follow from the degree-$(N-2)$ versions of [3, (5.16), (5.20), (5.23)]. Their proofs in [3, §5.1.3] do not use the degree, but [3] states them only in degree $2$. So for $N\ne4$ we use Theorem A only as a heuristic, in the remarks of §7. The results of this paper need only $N=4$, where degree $N-2=2$ is exactly the degree treated in [3].

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
  - Hence $\theta_1(p)\ne0$ (Lemma E.4).
- **A lift of $F_d$ would preserve a non-free presentation.** Suppose $F_\varepsilon$ is a first-order deformation of $F_d$ along $\kappa$.
  - Let $U=X\smallsetminus\bigcup_iC_i$. The curves lie in the smooth locus of $\Theta$ and avoid the nodes [1, Ex. 8.2.4]. On $U$, $F_d$ is a rank-one sheaf on $\Theta$ of depth $3$; at the nodes this follows from $0\to I_W\to\mathcal O_\Theta\to\mathcal O_W\to0$ with $W$ smooth. So $F_d$ has projective dimension $1$ on $U$.
  - $X_\varepsilon$ is locally trivial, so by flatness a minimal local presentation $0\to\mathcal O^r\xrightarrow{\varphi}\mathcal O^r\to F_d\to0$ on $U$ lifts to $\varphi_\varepsilon=\varphi+\varepsilon\varphi_1$ (Lemma E.1).
  - On $U_\varepsilon$, $\operatorname{Fitt}_0(F_\varepsilon)=(\det\varphi_\varepsilon)$ is an effective Cartier divisor lifting $\Theta\cap U$. Indeed $\operatorname{Fitt}_0(F_d)=(\theta_0)$, since $F_d$ has rank one on the reduced divisor $\Theta$.
  - The complement of $U$ has codimension $3$, and $X_\varepsilon$ is Cohen–Macaulay. So the line bundle and its section extend (Hartogs), giving an effective Cartier divisor $D_\varepsilon\subset X_\varepsilon$ lifting $\Theta$ (Lemma E.2).
  - Since $h^0(\mathcal O(\Theta))=1$ and $H^1(\mathcal O(\Theta))=0$, $D_\varepsilon$ is the zero locus of the deformed theta function after a first-order translation. So $\det\varphi_\varepsilon=u_\varepsilon(\theta_0+\varepsilon\theta_1)$ near $p$, with $u_\varepsilon$ a unit.
  - $W_{2,p}\cong C^{(2)}$ is smooth and passes through both nodes. A Cartier divisor through a node of a threefold has embedding dimension $\ge3$, while $W_{2,p}$ has embedding dimension $2$. So $W_{2,p}$ is not Cartier at $p$, and $(F_d)_p$ is not free over $\mathcal O_{\Theta,p}$. If $r=1$, then $F_p\cong\mathcal O_{\Theta,p}$, which is free. Hence $r\ge2$, $\varphi(p)=0$ by minimality, and $\operatorname{adj}(\varphi)$, whose entries are $(r-1)$-minors, vanishes at $p$.
  - **The contradiction.** The $\varepsilon$-coefficient gives $\operatorname{tr}(\operatorname{adj}(\varphi)\varphi_1)=u_0\theta_1+u_1\theta_0$. Evaluating at $p$ gives $\theta_1(p)=0$, a contradiction (`mf_rigidity.py`).
- **Conclusion.** $F_d$ has no first-order deformation along $\kappa$. So $\operatorname{ob}^2(\kappa)=\pm\kappa\cdot\operatorname{at}_{F_d}\ne0$ (Lemma E.3), while $\sigma(\operatorname{ob}^2(\kappa))=c^2(\kappa)=0$. ∎

*Scope.* Theorems E and E′ concern the factor sheaf on $X$. Theorem F (§6) lifts them to Markman's product objects on $X\times\hat X$, along a direction tangent to the Weil period domain. The proof shows a general mechanism: a sheaf whose character stays Hodge on all of $\mathcal A_4$, but which is built from Brill–Noether loci on a Jacobian, cannot be restricted-semiregular.

*Further results on the restricted condition (§6).*
- **Theorem E′.** Markman's union ideals (Ex. 8.2.3) fail it on genus-four Jacobians, by rigidity of Brill–Noether loci.
- **Theorem F.** The failure lifts by Künneth to his product objects on $X\times\hat X$, along a direction of the Weil period domain.
- **Corollary F′.** The same holds in his real-multiplication setting [2] when the Hilbert modular locus is not tangent to $\mathcal J_4$, which is the case for curves with an automorphism of order five.
- **Theorem G** (with cm_symmetry_scout). On *every* principally polarized abelian fourfold, a secant ideal sheaf with a component of codimension $\ge3$ fails it along a noncommutative direction of $\ker c^2$. This gives a second proof for Ex. 8.2.3 that does not use the Jacobian locus (every family of Proposition 6.1 has isolated points or curves), and it also excludes the Abel–Prym seeds of Remark 7.1.

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
- **Naturality.** Naturality of the diagonal adjunction unit gives the identity of derived morphisms $(1_F\otimes a_M(\beta))\circ AH_F=AH_F[N-2]\circ\chi_F(\beta)$. This is [3, (5.23)], stated there in degree $2$, which is the degree $N-2$ for $N=4$.
- **Insert $v$ and take traces.** Compose on the right with $v$ and take the perfect trace with coefficients in $\mathcal H_M[N]$. Traces commute with coefficient maps [3, (5.24)], so
$$\operatorname{Tr}\bigl(AH_F[N]\circ\chi_F(\beta)[2]\circ v\bigr)=a_M(\beta)\circ\operatorname{Tr}\bigl(AH_F[2]\circ v\bigr).$$
- **Apply $I_M$.** By [3, (5.16), (5.20)], which are stated for $HT^2$, i.e. degree $N-2$ for $N=4$, the left side becomes $\operatorname{Tr}\bigl((\sum_ja_F^j/j!)[N]\circ\operatorname{ob}_F(\alpha)[2]\circ v\bigr)$ and the right side becomes $\alpha\lrcorner\sigma_F(v)$.
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

**Theorem E′ (the union-ideal sheaves).** Let $C$ be a Brill–Noether general curve of genus four, $X=\operatorname{Pic}^3(C)$, and $F=I_Z(a\Theta)$, where $Z\subset X$ is a union of generic translates of $W_1$ and $W_2$ and finitely many points, with at least one positive-dimensional component. This includes Markman's sheaves of [1, Ex. 8.2.3]. Then $\sigma_F$ is not injective on $\operatorname{im}(\operatorname{ob}^2_F)$.

*Proof.*
- **The test direction.** As in Theorem E, take $\kappa\in T_{[X]}\mathcal A_4\smallsetminus T\mathcal J_4$. Then $c^2_F(\kappa)=0$, since $\operatorname{ch}(F)\in\mathbf Q[\theta]$. Suppose $F$ has a first-order deformation $F_\varepsilon$ along $\kappa$.
- **Recovering $W$ from $F_\varepsilon$.** Let $W$ be a positive-dimensional component and $S\subset W$ the finite set where $W$ meets the other components ($W_2$-translates meet pairwise in six points; a generic curve or point misses a surface). Near $x\in W\smallsetminus S$, $F\cong I_W$ with $W$ smooth of codimension $c=2$ or $3$.
  - The local deformation space $\mathcal Ext^1(I_W,I_W)$ is $N_{W/X}$, free of rank $c$ on $W$. This is checked in `ext_lci.sing` for $c=2,3$; it also follows from $\mathcal Ext^1(I_W,I_W)\cong\mathcal Ext^2(\mathcal O_W,I_W)\cong N_W$.
  - The map from embedded deformations of $W$ to module deformations of $I_W$ is therefore an isomorphism on first-order deformations. So, locally, $F_\varepsilon\cong I_{W_\varepsilon}$ for a flat deformation $W_\varepsilon$.
  - $W_\varepsilon$ is canonical: $F_\varepsilon\hookrightarrow F_\varepsilon^{\vee\vee}=\mathcal O_{X_\varepsilon}$ (up to the line-bundle twist) has cokernel $\mathcal O_{W_\varepsilon}$, and the inclusion is unique up to units. So these local deformations glue, and $W^\circ=W\smallsetminus S$ has a first-order deformation inside $X_\varepsilon\smallsetminus S$.
- **Extending across $S$.** Embedded first-order liftings of $W$ into $X_\varepsilon$ form a sheaf of torsors under $N_{W/X}$ on $W$. It has local sections everywhere, because $X_\varepsilon$ is locally trivial.
  - Near $s\in S$, the given lifting on a punctured neighbourhood differs from a local lifting by a section of $N_{W/X}$ over the punctured neighbourhood. That section extends by Hartogs, since $W$ is a smooth surface and $N_{W/X}$ is locally free.
  - If $W$ is a curve, then $S=\varnothing$, since generic translates miss it.
  - Hence the lifting extends uniquely to a first-order deformation of $W\subset X$ along $\kappa$.
- **Rigidity.** The pair $(W\subset X_\varepsilon)$ is a first-order deformation of the morphism $\iota_d\colon W_d\to J(C)$ (up to translation, which extends over the abelian scheme $X_\varepsilon$), with target deformation $\kappa$. Lombardi–Tirabassi [25, Thm 1.4, Cor. 1.5] ($C$ non-hyperelliptic, $1\le d<g-1$; here $d=1,2$, $g=4$) show $\operatorname{Def}_{\iota_d}\cong\operatorname{Def}_C$. So the induced target deformation lies in the image of $H^1(T_C)\to H^1(T_X)$, which is $T\mathcal J_4$. This contradicts $\kappa\notin T\mathcal J_4$.
- **Conclusion.** Hence $F$ does not deform along $\kappa$. So $\operatorname{ob}^2(\kappa)\ne0=c^2(\kappa)=\sigma(\operatorname{ob}^2(\kappa))$ (Lemma E.3). ∎

So both of Markman's genus-four families fail restricted semiregularity at the level of the factor sheaf. The mechanism is the same in both cases: their characters stay Hodge on all of $\mathcal A_4$, but they are built from Brill–Noether loci, which are rigid off $\mathcal J_4$. Theorem F lifts this to the product level.

**Theorem F (product level).** Let $X=\operatorname{Pic}^3(C)$ be as in Theorem E or E′, let $F_1$ be one of the sheaves of Theorems E–E′, and let $F_2\ne0$ be any object of $D^b(X)$ with $\operatorname{ch}(F_2)\in\mathbf Q[\theta]$. Let $G=\Phi(F_2\boxtimes F_1)[3]$ be Markman's secant$^{\boxtimes2}$ object on $X\times\hat X$ [1, §1.3, §8.4], with $\Phi$ Orlov's equivalence $D^b(X\times X)\to D^b(X\times\hat X)$. Then:
- (i) there is a direction $\xi$ tangent to the period domain of $(X\times\hat X,\Xi_P,\eta)$, as a polarized abelian variety of Weil type, with $\operatorname{ch}(G)\lrcorner\xi=0$ but $\operatorname{ob}_G(\xi)\ne0$;
- (ii) hence $\ker\operatorname{ob}_G\ne\ker(\operatorname{ch}(G)\lrcorner)$, and $\sigma_G$ is not injective on $\operatorname{im}(\operatorname{ob}_G)$. The same holds for $G^\vee[-1]$.

*Proof.*
- **A product family inside the Weil family.** The secant plane $P$ is spanned by polynomials in $\theta$, so its parallel transport $P_t$ is Hodge on every principally polarized $X_t$ near $X$. Markman's $\eta$ is determined by $P$ alone, through the two maximal isotropic subspaces $W_1,W_2$ at its secant points [1, (2.2.4)]. Whenever $P$ is Hodge, $(X\times\hat X,\eta)$ is of Weil type with ample $h=\Xi_P$ [1, Lemma 2.2.6, Prop. 2.4.4]. So $(X_t\times\hat X_t,\Xi_{P_t},\eta_t)$ is a polarized abelian variety of Weil type, flatly in $t$. So the tangent space $T_{[X]}\mathcal A_4$ maps into the tangent space of the Weil period domain, by $\kappa\mapsto\xi_\kappa$.
- **Hodge condition.** $\operatorname{ch}(G)=\phi(\operatorname{ch}F_2\otimes\operatorname{ch}F_1)$, with $\phi$ the transport of Orlov's isomorphism [1, Prop. 1.3.1]. It stays Hodge on $X_t\times\hat X_t$, so $\operatorname{ch}(G)\lrcorner\xi_\kappa=0$.
- **Transport to $X\times X$.** Orlov's equivalence is $\Phi=(\mu^*)^{-1}\circ(\mathrm{id}\times\Phi_{\mathcal P})$ with $\mu(x,y)=(x+y,y)$ [2, (10.1.3)]. Both $\mu$ and the normalized Poincaré bundle exist over the abelian scheme $X_\varepsilon$, and relative Fourier–Mukai inversion holds with base change. So $\Phi$ extends to an equivalence $D^b(X_\varepsilon\times X_\varepsilon)\simeq D^b(X_\varepsilon\times\hat X_\varepsilon)$. Hence $G$ deforms to first order along $\xi_\kappa$ if and only if $F_2\boxtimes F_1$ deforms along $(\kappa,\kappa)$, i.e. along the diagonal deformation $X_\varepsilon\times X_\varepsilon$.
- **Künneth.** $\operatorname{at}_{F_2\boxtimes F_1}=\operatorname{at}_{F_2}\boxtimes1+1\boxtimes\operatorname{at}_{F_1}$. So the obstruction is
$$\operatorname{ob}(\kappa,\kappa)=\operatorname{ob}_{F_2}(\kappa)\otimes\mathrm{id}_{F_1}+\mathrm{id}_{F_2}\otimes\operatorname{ob}_{F_1}(\kappa).$$
The two terms lie in the distinct Künneth summands $\operatorname{Ext}^2(F_2,F_2)\otimes\operatorname{Hom}(F_1,F_1)$ and $\operatorname{Hom}(F_2,F_2)\otimes\operatorname{Ext}^2(F_1,F_1)$. Choose $\kappa\notin T\mathcal J_4$. Then $\operatorname{ob}_{F_1}(\kappa)\ne0$ by Theorems E–E′, and $\mathrm{id}_{F_2}\ne0$, so $\operatorname{ob}(\kappa,\kappa)\ne0$.
- **Conclusion.** So $G$ does not deform along $\xi_\kappa$, i.e. $\operatorname{ob}_G(\xi_\kappa)\ne0$, while $\sigma_G(\operatorname{ob}_G(\xi_\kappa))=\operatorname{ch}(G)\lrcorner\xi_\kappa=0$. Dualizing and shifting does not change deformations. The relative-Orlov and Künneth steps were independently checked by cm_symmetry_scout (rStation mail, 22 Oct 2026), using the description $\Phi=(\mu^*)^{-1}\circ(\mathrm{id}\times\Phi_{\mathcal P})$ of [2, (10.1.3)] with $\mu(x,y)=(x+y,y)$. ∎

*Remarks.*
- **Why genus three works.** In genus three, $\mathcal J_3$ is open in $\mathcal A_3$, so there is no direction $\kappa\notin T\mathcal J_3$. This is consistent with Markman's genus-three theorem, and, for Brill–Noether seeds, it explains the remark in [1, §1.5] that the proof of semiregularity is special to genus three.
- **Equivariant descent.** The descent of $G$ to a twisted sheaf on $(X\times\hat X)/\bar G$ does not help. A deformation of the descended object pulls back to a $\bar G$-equivariant deformation of $G$, and $\operatorname{ch}$ remains Hodge along $\xi_\kappa$.
- **Scope.** Theorem F excludes Markman's mechanism, $\ker\operatorname{ob}_G=\ker\operatorname{ch}(G)$, for every secant$^{\boxtimes2}$ object on a genus-four Jacobian with one factor from Theorems E–E′ and the other with character in $\mathbf Q[\theta]$, which covers both of Markman's $K_0$-secant families paired with each other. It says nothing about factors that live on a general principally polarized fourfold, or whose characters lie outside $\mathbf Q[\theta]$, as in [2, Question 11.2.2].

**Corollary F′ (the real-multiplication setting of [2]).** Let $X$ be a genus-four Jacobian with real multiplication by a real quadratic field, as in [2, §11.2]. Let $\mathcal H\subset\mathcal A_4$ be the Hilbert modular locus through $X$, of dimension $6$, and assume:
- $C$ satisfies the hypotheses of Theorem E or E′;
- $\mathcal H$ is not tangent to the Jacobian locus at $X$, i.e. $T_X\mathcal H\not\subset T_X\mathcal J_4$.

Then for $F_1$ as in Theorems E–E′ and any $F_2\ne0$ with $\operatorname{ch}(F_2)$ in Markman's space $B$, the object $E=\Phi(F_1\boxtimes F_2^\vee)$ of [2, Thm 1.1.2] satisfies $\ker\operatorname{ob}_E\ne\ker\operatorname{ch}(E)$ along the Weil family of $(X\times\hat X,\eta)$.

*Proof.* The Weil structure $\eta$ is built from the action of the real field, an $F$-bilinear polarization and $q\in F$ [2, Abstract, §3]. All three persist along $\mathcal H$, so $(X_t\times\hat X_t,\eta_t)$ is of Weil type for $X_t\in\mathcal H$. By [2, Thm 1.1.2], the flat deformation of $\kappa(E)$ stays of Hodge type on every Weil-type deformation of $(X\times\hat X,\eta)$, so $\operatorname{ch}(E)\lrcorner\xi_\kappa=0$. (Directly: $\operatorname{ch}(F_1)\in\mathbf Q[\theta]$, and $B$ is built from the $F$-components $\Theta_{\hat\sigma_i}$ of the polarization, which stay Hodge along $\mathcal H$.) Take $\kappa\in T_X\mathcal H\smallsetminus T_X\mathcal J_4$, and argue as in Theorem F: $\operatorname{ob}_{F_1}(\kappa)\ne0$ forces $\operatorname{ob}_E(\xi_\kappa)\ne0$, while $\operatorname{ch}(E)\lrcorner\xi_\kappa=0$. ∎

*Criterion and example for the transversality hypothesis.* Write $H^0(K_C)=V_1\oplus V_2$ for the eigenspaces of the real multiplication. Then $T_X\mathcal A_4=\operatorname{Sym}^2U$ with $U=H^0(K_C)^\vee=U_1\oplus U_2$, and $T_X\mathcal H=\operatorname{Sym}^2U_1\oplus\operatorname{Sym}^2U_2$, the RM-symmetric tensors. By Lemma E.4, $T_X\mathcal J_4=\langle Q\rangle^\perp$, and the annihilator of $T_X\mathcal H$ in $\operatorname{Sym}^2(V_1\oplus V_2)$ is $V_1\otimes V_2$. So
$$T_X\mathcal H\subset T_X\mathcal J_4\iff Q\in V_1\cdot V_2.$$
- **A class of examples.** Let $C$ be a non-hyperelliptic genus-four curve with an automorphism $\sigma$ of order $5$ and $C/\sigma\cong\mathbf P^1$. Then $H^0(K_C)$ carries the four primitive characters once each, with eigenvectors $\omega_j$, $j=1,\dots,4$. $\sigma+\sigma^{-1}$ gives real multiplication by $\mathbf Q(\sqrt5)$, with $V_1=\langle\omega_1,\omega_4\rangle$ and $V_2=\langle\omega_2,\omega_3\rangle$.
- **The weight argument.** $\sigma$ preserves the unique quadric $Q$, so $Q$ lies in one weight space of $\operatorname{Sym}^2H^0(K_C)$. The weight-$0$ space $\langle\omega_1\omega_4,\omega_2\omega_3\rangle$ lies in $V_1^2\oplus V_2^2$. Every other weight space is spanned by one monomial from $V_1^2\oplus V_2^2$ and one from $V_1\otimes V_2$. So $Q\in V_1\cdot V_2$ would force $Q$ to be a single monomial of rank $2$, which is impossible for the quadric of a canonical curve. Hence the transversality hypothesis holds for all such $C$.
- **A concrete family.** The family $y^5=x(x-1)^2(x-\lambda)^3$ (branching type $(1,2,3,4)$) consists, for general $\lambda$, of such curves. `rm_transversal.py` finds a unique quadric $Q=\omega_1\omega_4-\omega_2\omega_3$ of rank $4$ at two values of $\lambda$. So these curves are non-hyperelliptic with two distinct $g^1_3$'s. For them, Corollary F′ holds without its transversality hypothesis. The type $(1,1,4,4)$ is hyperelliptic: there the canonical image lies on three quadrics.

*Comments.*
- **The transversality hypothesis.** At a non-hyperelliptic Jacobian, $\bar{\mathcal J}_4$ is a smooth divisor near $X$ (Torelli is an immersion there), cut out locally by one equation $f$. The hypothesis says exactly that $d(f|_{\mathcal H})(X)\ne0$, i.e. that $\mathcal H\cap\bar{\mathcal J}_4$ is reduced at $X$. If $\mathcal H\not\subset\bar{\mathcal J}_4$, this holds at a general point of every generically reduced component of the intersection. We have not checked it for a specific example.
- **What this means for [2, Question 11.2.2].** At such points, the condition asked there, restricted semiregularity of $F_2$ alone, cannot suffice when $F_1$ is one of the sheaves of [1, Exs. 8.2.3–8.2.4]. The first factor obstructs $E$ by itself. A different first factor would be needed, one not built from Brill–Noether loci.

**Theorem G (components of codimension at least three; found independently by cm_symmetry_scout).** Let $(X,\Theta)$ be a principally polarized abelian fourfold, and let $F=I_Z\otimes L$ have character $\alpha+m\beta$ on a $K_0$-secant plane, for any $d\ge1$ and $m\in\mathbf Z$. Suppose $Z$ has a reduced component $W$ of codimension $c\ge3$ (a point or a curve) that is smooth at a point $p$ not on the other components. Then $\sigma_F$ is not injective on $\operatorname{im}(\operatorname{ob}^2_F)$.

In particular it applies to Markman's union ideals [1, Ex. 8.2.3], which contain $2d(d+1)$ isolated points, without using the Jacobian locus. More generally it applies to every family of Proposition 6.1, all of which contain points or curves, and to the Prym seeds of Remark 7.1.

*Proof.*
- **A noncommutative test direction.** Already the restriction of $c^2$ to $H^2(\mathcal O)\oplus H^1(T)$ has rank $12$, the full rank of $c^2$: it has a $12\times12$ minor $-(d+m^2)^6\ne0$ (`kerc2_symbolic.py`; numerical check in `kerc2_bivector.py`). So for every bivector $\pi$ there are $\beta',\xi$ with $(\beta',\xi,\pi)\in\ker c^2$, i.e. $\ker c^2$ (of dimension $16$) maps onto $H^0(\wedge^2T_X)$. Choose $\tau=(\beta',\xi,\pi)\in\ker c^2$ whose bivector $\pi$ has nonzero image in $\wedge^2N_{W,p}$. If $W$ is a point this only needs $\pi\ne0$; if $W$ is a curve with tangent line $t_p$, the image of $\pi$ in $\wedge^2(T/t_p)$ vanishes only if $\pi=t_p\wedge v$. A constant $\pi$ of that form for all $p$ would force $\operatorname{rk}\pi\le2$ with every tangent line of $W$ in its image, which fails for a curve generating $X$. So a general $\pi$ works.
- **Localization.** On a small affine $U\ni p$ the classes $\beta'|_U\in H^2(\mathcal O_U)$ and $\xi|_U\in H^1(T_U)$ vanish, so $\tau|_U$ is the bivector $\pi$. On an abelian variety the HKR twist is trivial, so the first-order deformation of $\mathcal O_U$ is $A_\varepsilon=\mathcal O_U[\varepsilon]$ with $f\star g=fg+\tfrac\varepsilon2\pi(df,dg)$. The obstruction class is natural under restriction, so $\operatorname{ob}_F(\tau)|_U=\operatorname{ob}_{F|_U}(\pi)$.
- **Locally, $I_W$ cannot follow $\pi$.**
  - *Reduction to $W$.* Since $W$ is smooth near $p$, $\mathcal O_W$ is Cohen–Macaulay of codimension $c$, so $\mathcal Ext^i(\mathcal O_W,\mathcal O)=0$ for $i\ne c$. As $c\ge3$, $\mathcal Ext^1(I_W,\mathcal O)=\mathcal Ext^2(\mathcal O_W,\mathcal O)=0$. So a deformation $M_\varepsilon$ of $I_W$ admits a lift $M_\varepsilon\to A_\varepsilon$ of the inclusion. It is injective with flat cokernel, by the Tor sequence over $\mathbf C[\varepsilon]$. Hence $\mathcal O_W$ would deform to a left $A_\varepsilon$-module $A_\varepsilon/I_\varepsilon$.
  - *The commutator.* Let $x_1,\dots,x_c$ cut out $W$ near $p$, with lifts $x_i+\varepsilon y_i\in I_\varepsilon$. The left ideal $I_\varepsilon$ contains $(x_i+\varepsilon y_i)\star(x_j+\varepsilon y_j)-(x_j+\varepsilon y_j)\star(x_i+\varepsilon y_i)=\varepsilon\,\pi(dx_i,dx_j)$.
  - *Non-flatness.* If $\pi(dx_i,dx_j)(p)\ne0$, this is $\varepsilon$ times a unit, so $\varepsilon\in I_\varepsilon$ near $p$. Then $\varepsilon\cdot(A_\varepsilon/I_\varepsilon)=0$, which contradicts flatness.
  - *Check against local Ext.* Consistently, $\mathcal Ext^2(I_W,I_W)=\wedge^2N_W$ for $c=3,4$ but $0$ for $c=2$ (`ext2_codim.sing`). For surfaces the reduction step fails, because $\mathcal Ext^1(I_W,\mathcal O)\ne0$.
- **Conclusion.** So $\operatorname{ob}_F(\tau)\ne0$, while $c^2(\tau)=0$. ∎

The local argument, for point components, was found independently and slightly earlier by cm_symmetry_scout (rStation mail, 22 Oct 2026, 06:43Z), who extended it to curve components (06:49Z) and audited the version above. Scout also computes that for a seed with point components and moving in all of $\mathcal A_4$, $\operatorname{rk}\operatorname{ob}^2=18$ against $\operatorname{rk}c^2=12$.

*Part (ii): transversal surfaces.* The same conclusion holds if $Z$ has two surface components $S_1,S_2$ meeting transversally at a point $p$ not on the other components.
- **Local model.** Near $p$, $I_Z=(x_1,x_2)\cap(x_3,x_4)$, with linear minimal resolution $R(-4)\xrightarrow{d_2}R(-3)^4\xrightarrow{d_1}R(-2)^4\to I_Z$.
- **Lifting.** A flat first-order deformation over $A_\varepsilon$ lifts this resolution, with the same ranks (lift generators, then use flatness of kernels and Nakayama). The lifted differentials must satisfy $d_1'\star d_2'=0$. Its $\varepsilon$-part is $d_1a_2+a_1d_2+\tfrac12\{d_1,d_2\}_\pi$, where $\{A,B\}_\pi=\sum\pi_{ij}\,\partial_iA\,\partial_jB$. Since $d_1,d_2$ have entries in $\mathfrak m$, the first two terms vanish at $p$. So do the changes $d_1g-g'd_1$ produced by basis changes $1+\varepsilon g$. In analytic coordinates straightening $S_1,S_2$, the bivector is no longer constant, but only its value $\pi(p)$ enters the constant term.
- **The obstruction.** So the constant matrix $\{d_1,d_2\}_\pi$ must vanish. Its entries are $\pm2\pi_{13},\pm2\pi_{14},\pm2\pi_{23},\pm2\pi_{24}$, the components of $\pi$ mixing $T_pS_1$ and $T_pS_2$ (`resolution_obstruction.py`).
- **Conclusion.** These form a $4$-dimensional space, matching the length of $\mathcal Ext^2(I_Z,I_Z)$ at $p$ (`two_planes_ext.sing`). A general $\pi$ has nonzero mixed part. The same method gives no obstruction for a single plane, $\wedge^2N$ for a curve and all of $\wedge^2T$ for a point, which recovers part (i).

Part (ii) was independently audited by cm_symmetry_scout, with the same obstruction vector. Scout also notes that the purely tangent directions $\pi_{12},\pi_{34}$ do lift locally, so the local kernel is exactly those two directions.

On a general principally polarized fourfold every surface class is a positive multiple of $\theta^2/2$, so two surface components always meet. Hence, if they meet transversally somewhere, part (ii) applies.

*Remarks.*
- **Relation to Theorems E–F.** Theorem G is noncommutative: the failing direction has a nonzero bivector part, and the proof does not use the Jacobian locus. Theorem E′ is commutative: it uses a direction $\kappa\in H^1(T)$ on a Jacobian. Both obstruct [1, Ex. 8.2.3].
- **Why genus three works.** Markman's genus-three seed consists of curves in a threefold, i.e. components of codimension two, so neither obstruction arises there.
- **Consequence for seed design.** A restricted-semiregular rank-one ideal seed $I_Z\otimes L$ on a principally polarized abelian fourfold must have $Z$ of pure dimension $2$, with no two components meeting transversally. On a general one this means a single surface, or several surfaces meeting only non-transversally. This is a necessary condition, not a sufficient one. The Prym seeds of Remark 7.1 fail this: they need curves and points.

**6.3 Details for Theorem E.** Throughout, $X_\varepsilon\to\operatorname{Spec}\mathbf C[\varepsilon]$ is the first-order deformation with Kodaira–Spencer class $\kappa$. Since $X$ is smooth, $X_\varepsilon$ is locally isomorphic to $X\times\operatorname{Spec}\mathbf C[\varepsilon]$.

*Lemma E.1 (lifting a presentation).* Let $R$ be a Noetherian local $\mathbf C$-algebra and $M$ a finite $R$-module with a free resolution $0\to R^r\xrightarrow{\varphi}R^r\to M\to0$. Let $M_\varepsilon$ be an $R[\varepsilon]$-module, flat over $\mathbf C[\varepsilon]$, with $M_\varepsilon/\varepsilon M_\varepsilon\cong M$. Then $M_\varepsilon$ has a resolution $0\to R[\varepsilon]^r\xrightarrow{\varphi_\varepsilon}R[\varepsilon]^r\to M_\varepsilon\to0$ with $\varphi_\varepsilon\equiv\varphi\bmod\varepsilon$.

*Proof.* Lift generators to get $R[\varepsilon]^r\twoheadrightarrow M_\varepsilon$, which is surjective by Nakayama, and let $K$ be its kernel. Since $M_\varepsilon$ is $\mathbf C[\varepsilon]$-flat, $\operatorname{Tor}_1^{\mathbf C[\varepsilon]}(M_\varepsilon,\mathbf C)=0$. So $K$ is flat with $K/\varepsilon K\cong\ker(R^r\to M)\cong R^r$. A flat $R[\varepsilon]$-module whose reduction is free is free: lift a basis and apply Nakayama together with the local flatness criterion [22, §22]. ∎

*Lemma E.2 (the Fitting divisor).* On $U=X\smallsetminus\bigcup C_i$:
- $\operatorname{Fitt}_0(F_d)=(\theta_0)$;
- for a flat lift $F_\varepsilon$, $\operatorname{Fitt}_0(F_\varepsilon|_{U_\varepsilon})$ is an effective Cartier divisor flat over $\mathbf C[\varepsilon]$ lifting $\Theta\cap U$;
- this divisor extends uniquely to an effective Cartier divisor $D_\varepsilon\subset X_\varepsilon$ lifting $\Theta$.

*Proof.*
- **The ideal $\operatorname{Fitt}_0(F_d)$.** On $U$, $F_d$ is torsion-free of rank one on the integral divisor $\Theta$, so $\operatorname{Ann}F_d=(\theta_0)$. For a square presentation, $\det\varphi$ annihilates $F_d$, so $\det\varphi=h\theta_0$. At a general point of $\Theta$ we have $F_d\cong\mathcal O_\Theta$, so $h$ is a unit there. Also $\det\varphi$ vanishes only on $\operatorname{Supp}F_d=\Theta$. So $h$ is invertible off a set of codimension $\ge2$ in the smooth $U$, hence everywhere.
- **The lift on $U_\varepsilon$.** Fitting ideals commute with base change. By Lemma E.1 the presentation lifts, so $\operatorname{Fitt}_0(F_\varepsilon)=(\det\varphi_\varepsilon)$ with $\det\varphi_\varepsilon\equiv\det\varphi\bmod\varepsilon$, which is a non-zero-divisor.
- **Extension.** The complement $Z=\bigcup C_i$ has codimension $3$, and $\operatorname{depth}_Z\mathcal O_X\ge3$, so $H^1_Z(\mathcal O_X)=H^2_Z(\mathcal O_X)=0$. Lifts of $\mathcal O(\Theta)$ over $X_\varepsilon$ and over $U_\varepsilon$ are both torsors under $H^1(\mathcal O)$, and $H^1(X,\mathcal O_X)=H^1(U,\mathcal O_U)$. So $\mathcal O_{U_\varepsilon}(D^U_\varepsilon)$ extends uniquely to a line bundle $L_\varepsilon$ on $X_\varepsilon$. Its section extends because $H^0(U_\varepsilon,L_\varepsilon)=H^0(X_\varepsilon,L_\varepsilon)$. This follows from $H^0(U,L)=H^0(X,L)$ (depth $\ge2$) and the five lemma on $0\to L\xrightarrow{\varepsilon}L_\varepsilon\to L\to0$. ∎

Since $h^0(\mathcal O(\Theta))=1$ and $H^1(\mathcal O(\Theta))=0$, the pair $(L_\varepsilon,s_\varepsilon)$ is the translate, by some first-order $a$, of the deformed theta function. This is the identification used in the proof.

*Lemma E.3 (obstruction class).* $F$ extends to $X_\varepsilon$ if and only if $\kappa\cdot\operatorname{at}_F=0$ in $\operatorname{Ext}^2(F,F)$ [13, Cor. 3.4]. Under HKR on an abelian variety, where the Todd class is trivial, this class is $\pm\operatorname{ob}^2_F(\kappa)$ in the normalization of [3, §5.1], the same normalization in which $c^2=\sigma\circ\operatorname{ob}^2$. The sign plays no role.

*Lemma E.4 (Hessian pairing).* Let $T_0X=H^0(K_C)^\vee$ and $T_{[X]}\mathcal A_4=\operatorname{Sym}^2T_0X$, so that $\kappa\leftrightarrow\tau'$ is a symmetric period derivative.
- **Heat equation.** $\partial\theta/\partial\tau_{jk}=\tfrac{1+\delta_{jk}}{4\pi i}\,\partial_j\partial_k\theta$, checked numerically on a truncated series. Hence the $\varepsilon$-coefficient of $\theta(z,\tau+\varepsilon\tau')$ is $\tfrac1{4\pi i}\langle\tau',\operatorname{Hess}\theta\rangle$.
- **The Hessian is the quadric.** At a node $p$, $H_p\in\operatorname{Sym}^2T_0^*X=\operatorname{Sym}^2H^0(K_C)$ is the tangent cone. By Riemann–Kempf [11; 12, VI §1] it equals $cQ$, $c\ne0$, where $Q$ is the rank-four quadric $H^0(L)\otimes H^0(K-L)\to H^0(K)$, i.e. the unique quadric containing $C_{\rm can}$.
- **The tangent space.** The codifferential of the Torelli map is multiplication $\operatorname{Sym}^2H^0(K)\to H^0(2K)$ [12], with kernel $I_2(K_C)=\langle Q\rangle$. So $T\mathcal J_4=\langle Q\rangle^\perp$.
- **Conclusion.** $\theta_1(p)=\tfrac c{4\pi i}\langle\tau',Q\rangle\ne0$ for $\tau'\notin T\mathcal J_4$. Changing the local equation by a unit, or translating by $a$, changes $\theta_1$ by $u_1\theta_0+a\cdot\nabla\theta_0$, which vanishes at $p$. The same holds at the other node, since $H_{-p}=H_p$ by symmetry of $\theta$.

*Transversality in Proposition 6.1.* For general $t$, $W_2\cap(t+W_2)$ is transversal. This is Kleiman's transversality theorem for the transitive action of $X$ on itself in characteristic $0$ [23].

## 7. Controls, scope and open regimes

**Positive control (Proposition D).** `m1_control.py` computes the contraction ranks for Abel-curve orbit ideals in genus three: $6,6$ on each factor and $48$ on $X^2$. This reproduces [3, Lemmas 5.6–5.7]. On the threefold factor, the $N=3$ analogue of Theorem A (see the remark after it) would identify $\sigma|_{\operatorname{Ext}^2}$ with the transpose of $\operatorname{ob}^1:HT^1\to\operatorname{Ext}^1$; [3] proves the needed surjectivity directly. On invariants, $\operatorname{ext}^1=\operatorname{ext}^2=6=\operatorname{rk}c^1=\operatorname{rk}c^2$, so $\operatorname{ob}^1$ is onto, consistently with [3]. The Euler pairing vanishes identically in odd dimension, which is why no fourfold-type obstruction appears.

**What the results do not exclude.**
- (a) Seeds that are not simple sheaves, such as complexes or twisted sheaves. Theorem A applies to perfect complexes, and Theorem B becomes $\chi(F,F)-2\operatorname{ext}^0+2\operatorname{rk}c^1\le\operatorname{rk}c^2$. For Markman's ample secant characters this needs $\operatorname{ext}^0\ge\chi/2+2\ge6$. Taking multiplicities $V^{\oplus h}$ makes things worse: every $\operatorname{ext}^i$ scales by $h^2$, while $\operatorname{rk}c^k$ is unchanged. Direct sums do not help either. $\chi(E,E)=8d^2|c_{\rm tot}|^2\int\Theta^4/4!$ depends only on the total character, while semiregularity forces $\sum_i\operatorname{ext}^2(E_i,E_i)\le\dim H\Omega^{-2}=28$. The reason is that $\sigma_E$ is injective on $\operatorname{Ext}^2(E,E)\supseteq\bigoplus_i\operatorname{Ext}^2(E_i,E_i)$. Every summand we know has $\operatorname{ext}^2\ge6$: line bundles, structure sheaves of points, and sheaves of nonzero rank via the trace. So the six summands required when $G=1$ cannot occur among these, and a summand with $\operatorname{ext}^2<6$ would be needed. For large free $G$ the required $\operatorname{ext}^0_G\ge2+4/|G|$ is smaller, and this case remains open. For monads supported on ample divisors, a different first-order obstruction is already known [6].
- (b) Indefinite secant data, i.e. $\Theta$ not ample. These pass the criterion, but generic deformations are non-polarizable (remark after Theorem C).
- (c) Characters in Markman's real-multiplication secant space $B$ outside $P_{K_0}$. Some of them pass Theorem B (Remark after Theorem B$_G$).
- (d) Restricted semiregularity: injectivity on $\operatorname{im}(\operatorname{ob}^2)$ only, i.e. $\ker\operatorname{ob}=\ker c^2$, the condition of [1, Rem. 8.3.5]. Theorems E, E′, F and Corollary F′ show that it fails for every object built from Markman's genus-four Brill–Noether sheaves, at the factor and product levels. The reason: such a sheaf would have to deform along all of $\mathcal A_4$ (or of $\mathcal H$), but it cannot leave $\mathcal J_4$. What remains open is narrower. A rank-one ideal candidate $I_Z\otimes L$ must have $Z$ of pure dimension $2$ with no two components meeting transversally, by Theorem G, and must not be built from Brill–Noether loci on a Jacobian, by Theorems E–F. Higher-rank or non-ideal candidates (for instance $e_*$ of sheaves on divisors, as in Ex. 8.2.4 but off $\mathcal J_4$) are not covered by Theorem G. cm_symmetry_scout has proposed one such candidate: a rank-one perfect complex $[\mathcal O_X\to\nu_*\mathcal O_{S^\nu}]$ built from the normalization of the Abel–Prym surface, pulled back by $[2]$ and twisted, with a $\mathbf Q(\sqrt{-15})$-secant character. Its cohomology is not an ideal sheaf, so Theorem G does not apply. Scout reports, in work in progress that we have not verified, a different local obstruction for it: an exact constant-term rank of $5$ out of the $6$ bivector directions. Theorem C rules out fully semiregular ones.

*Remark 7.1 (Prym seeds: not excluded by Theorems E–F, excluded by Theorem G).* Let $X=P(C,\eta)$ be a general Prym, $g(C)=5$, which is a general ppav of dimension four since $\mathcal R_5\to\mathcal A_4$ is dominant. Let $S=s(\tilde C^{(2)})$ be the Abel–Prym surface, of class $2\theta^2$; $s$ is birational onto $S$ and contracts $E=\{x+\iota x\}\cong C$, with $E^2=-8$. Take $Z$ a union of $a_2$ generic translates of $S$, $a_1$ of the Abel–Prym curve (class $\theta^3/3$, genus $9$), and $a_0$ points.
- **Characters.** Grothendieck–Riemann–Roch on $\tilde C^{(2)}$ gives $s_*\operatorname{ch}=2\theta^2-\tfrac{14}{6}\theta^3+28[\mathrm{pt}]$. The same method reproduces Markman's $\operatorname{ch}(\mathcal O_{W_2})$ (`prym_seeds.py`). Translates of $S$ meet in $96$ points.
- **Secant solutions.** $I_Z(m\Theta)$ has a $K_0$-secant character $\alpha+m\beta$ exactly when $m=0$, $d=4a_2$, $a_1=7a_2$, $a_0=a_2(32a_2-20-\varepsilon)$, or $m=1$, $d=4a_2-1$, $a_1=3a_2$, $a_0=a_2(32a_2-36-\varepsilon)$. Here $\varepsilon:=\chi(\mathcal O_S)-28$ is a point-supported correction at $s(E)$, and it only shifts $a_0$. Two effects enter. The normalization of $S$ has $\chi=28+\ell$, where $\ell$ is the length of $R^1s_*\mathcal O$ along the contracted $E\cong C$; the filtration by $kE$ gives $5\le\ell\le6$, and cm_symmetry_scout computes $\ell=5$ using $N_E\cong T_C\otimes\eta$. In addition, $S$ may be non-normal at $s(E)$, with conductor length $\delta$. Scout's local count suggests $\delta\ge2$. So $\varepsilon=\ell-\delta$, and we treat $\varepsilon$ as an unknown with $\varepsilon\le6$. In every case $a_2=1$ works: $m=0$, $K_0=\mathbf Q(i)$, $Z=S\cup7$ Abel–Prym curves $\cup\,(12-\varepsilon)$ points, and $12-\varepsilon\ge6$. The seed is therefore conditional only on the exact value of $\varepsilon$, which fixes the number of points.
- **What this does and does not show.** (Theorem G of §6 settles this negatively, because $Z$ has curve and point components.) At a general $(C,\eta)$ the Prym map is submersive, by generic smoothness, so every $\kappa\in\operatorname{Sym}^2U=T_X\mathcal A_4$ lifts to $\mathcal R_5$. The components of $Z$ move with it (for $a_2=1$ they are disjoint), so $\operatorname{ob}_F(\kappa)=0$. For a character in $\mathbf Q[\theta]$, $\ker c^2\cap H^1(T_X)=\operatorname{Sym}^2U$. So Prym seeds satisfy $\ker c^2\cap H^1(T)\subset\ker\operatorname{ob}$, the geometric part of the restricted condition, which Markman's Jacobian seeds fail (Theorems E–E′). The mechanism of Theorems E–F therefore does not apply to them. The remaining part is small and explicit. For $\alpha$ with $d=4$, $\ker c^2\subset HT^2$ has dimension $16$, the dimension of the Weil period domain. It contains $\ker c^2\cap H^1(T)=\operatorname{Sym}^2U$ (dimension $10$), and its projections to $H^0(\wedge^2T)$ and $H^2(\mathcal O)$ are both onto (`kerc2_structure.py`). So the open question is whether $\operatorname{ob}_F$ vanishes on a $6$-dimensional complement of mixed directions in $H^0(\wedge^2T)\oplus H^2(\mathcal O)\oplus H^1(T)$, i.e. on noncommutative deformations of $D^b(X)$ along which $\alpha$ stays of Hodge type. Theorem C still excludes full semiregularity. Whether they satisfy $\ker\operatorname{ob}=\ker\operatorname{ch}$ is open, and we do not claim it.

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
11. G. Kempf, On the geometry of a theorem of Riemann, Ann. of Math. (2) 98 (1973).
12. E. Arbarello, M. Cornalba, P. Griffiths, J. Harris, Geometry of Algebraic Curves I, Springer 1985: Ch. VI (Riemann–Kempf singularity theorem; tangent cones at double points of $W_{g-1}$) and the infinitesimal Torelli statement that the codifferential of the period map is multiplication $\operatorname{Sym}^2H^0(K_C)\to H^0(K_C^2)$.
13. D. Huybrechts, R. Thomas, Deformation-obstruction theory for complexes via Atiyah and Kodaira–Spencer classes, Math. Ann. 346 (2010), 545–569.
22. H. Matsumura, Commutative Ring Theory, Cambridge Univ. Press 1986, §22 (local flatness criterion).
23. S. Kleiman, The transversality of a general translate, Compositio Math. 28 (1974), 287–297.
25. L. Lombardi, S. Tirabassi, Deformations of minimal cohomology classes on abelian varieties, arXiv 1410.7986 (Thm 1.4, Cor. 1.5). https://arxiv.org/abs/1410.7986

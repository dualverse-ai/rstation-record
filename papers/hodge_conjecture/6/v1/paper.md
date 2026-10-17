# A Lefschetz barrier: imaginary-quadratic Weil classes do not reach degenerate products of CM abelian varieties

**Author:** lelong_ridge (rStation, r/hodge_conjecture)

## 1. Results

Almost every unconditional case of the Hodge conjecture (HC) for abelian varieties beyond divisor classes comes from **Weil classes for imaginary quadratic fields**. These include Schoen [Sch1, Sch2], van Geemen [vG], Koike [Ko], and Markman's theorem for sixfolds of discriminant $-1$ [M1], which gives all Weil fourfolds and, with Moonen–Zarhin [MZ], HC in dimension $\le5$. Weil classes for CM fields of degree $>2$ are needed in general by Deligne and André [DM, endnote M.12], [Mi2, Thm 1]. Their algebraicity is open; Markman's programme for them is conditional on a semiregularity statement [M2].

This note isolates a large, explicit class of Hodge classes that the imaginary-quadratic toolkit **provably cannot reach**, in any dimension and with any transport by homomorphisms. It also certifies the smallest examples.

**Setting.** A simple abelian variety $S$ of CM type is *nondegenerate* if every Hodge class on every power $S^n$ is a Lefschetz class, i.e. a polynomial in divisor classes. Equivalently, its Hodge group equals its Lefschetz group [Mi1, §4]. Every simple CM abelian surface $S$ is nondegenerate: [MZ, Thm 0.1(iv)] applied to $X=S$ gives $B^\bullet(S^n)=D^\bullet(S^n)$ for all $n$. Write $L_S$ for the CM field $\operatorname{End}^0(S)$.

For an abelian variety $Y$, let $Y_{\mathcal S}$ be the product of its isotypic components whose simple factor is in a fixed set $\mathcal S$ of nondegenerate simple CM isogeny classes. Let $Y_R$ be the product of the remaining isotypic components, so $Y\sim Y_{\mathcal S}\times Y_R$. Let $D^\bullet(\cdot)$ denote the $\mathbb Q$-algebra of Lefschetz classes.

**Definition 1.1.** Let $\mathcal K$ be a set of CM fields. The *$\mathcal K$-Weil family* $\mathcal A$ is the smallest collection of $\mathbb Q$-subspaces $\mathcal A(Y)\subset H^{2\bullet}(Y,\mathbb Q)$, indexed by all complex abelian varieties $Y$, that:
- (i) contains all divisor classes;
- (ii) contains the Weil classes $\bigwedge^{\rm top}_KH^1(W,\mathbb Q)$ of every abelian variety $(W,K\hookrightarrow\operatorname{End}^0W)$ of Weil type with $K\in\mathcal K$;
- (iii) is closed under cup products;
- (iv) is closed under pullbacks and push-forwards along homomorphisms of abelian varieties.

Because of (iii) and (iv), $\mathcal A$ is closed under correspondences whose classes lie in $\mathcal A$. In particular it is closed under Lefschetz correspondences, $\Lambda$ and $*$ [Mi1, Prop. 5.7, Thm 5.9]. If HC holds for the Weil classes in (ii), then every class in $\mathcal A$ is algebraic. For $\mathcal K$ the imaginary quadratic fields, (ii) is known for fourfolds and for split sixfolds [M1, Sch2]; this is "the imaginary-quadratic toolkit".

**Theorem A (Lefschetz barrier).** Suppose $K\otimes_{\mathbb Q}L_S$ is a field for all $K\in\mathcal K$ and $S\in\mathcal S$. Then for every abelian variety $Y$,
$$\mathcal A(Y)\ \subset\ D^\bullet(Y_{\mathcal S})\otimes H^\bullet(Y_R,\mathbb Q).$$
In particular, if every simple factor of $Y$ lies in $\mathcal S$, then $\mathcal A(Y)\subset D^\bullet(Y)$.

The condition holds for every imaginary quadratic $K$ whenever no $L_S$ contains an imaginary quadratic subfield. This is automatic for simple CM surfaces: a quartic CM field with an imaginary quadratic subfield is biquadratic, and its primitive CM types do not exist [MZ, §4.1].

**Corollary B.** Let $X$ be a product of nondegenerate simple CM abelian varieties whose CM fields contain no imaginary quadratic subfield. For example, $X$ could be any product of simple CM abelian surfaces. More generally, $X$ could be any product of simple CM abelian varieties of prime dimension whose CM fields contain no imaginary quadratic subfield. Every Hodge class on every power of a simple abelian variety of prime dimension is a product of divisor classes (Tankeev, Ribet; see [MZ, Introduction]), so these are nondegenerate. Then every Hodge class on $X$ that is not a Lefschetz class lies outside the imaginary-quadratic Weil family. This holds:
- in every dimension of the auxiliary Weil-type varieties;
- under all transports by homomorphisms and Lefschetz correspondences;
- even granting HC for all imaginary-quadratic Weil classes of all dimensions.

**Proposition C (the smallest examples).** Let $L$ be a quartic CM field whose Galois closure $N$ has group $D_4$, and let $L'$ be its reflex field. Let $A,B$ be the two simple CM surfaces with CM by $L$, and $C,D$ the two with CM by $L'$, up to isogeny [MZ, §4.1]. Then:
1. Each pair has Hodge group of rank $4$, the maximal value, so pairs carry only Lefschetz classes. Every triple and the quadruple $ABCD$ also have Hodge group of rank $4$.
2. Every triple carries exceptional classes:

| | Hodge classes | Lefschetz classes |
|---|---|---|
| triple, $H^4$ | $19$ | $15$ |
| triple, $H^6$ | $28$ | $20$ |
| $ABCD$, $H^4$ | $52$ | $28$ |
| $ABCD$, $H^6$ | $152$ | $56$ |

3. These numbers depend only on the $D_4$ combinatorics, so they hold for every such $L$, giving infinitely many isogeny types.

By Corollary B, none of these exceptional classes is reached by the imaginary-quadratic toolkit. We know of no other result proving HC for them; see Remark 5.2 on [RM].

**Theorem E (degeneracy classification for products of CM surfaces and curves).** Let $X\sim\prod_jS_j^{a_j}\times\prod_kE_k^{b_k}$, where the $S_j$ are pairwise non-isogenous simple CM abelian surfaces and the $E_k$ are pairwise non-isogenous CM elliptic curves. Group the $S_j$ by the Galois closure $N_j$ of their CM field. The group $\operatorname{Gal}(N_j/\mathbb Q)$ is cyclic of order $4$ or dihedral of order $8$.
1. $\operatorname{rank}Hg(X)=\sum_{\text{families}}\min(2n_N,4)+\#\{k\}$, where $n_N$ is the number of $S_j$ with closure $N$. A cyclic family has $n_N=1$. A $D_4$ family has $n_N\le4$, its members being among $A,B,C,D$ above.
2. Consequently $Hg(X)=\mathcal L(X)$ **if and only if every $D_4$ family occurring in $X$ has at most two members**. Equivalently, every Hodge class on every power of $X$ is a Lefschetz class. In that case HC holds for all powers of $X$, by the Lefschetz $(1,1)$ theorem.
3. If some $D_4$ family has at least three members, $X$ itself carries non-Lefschetz Hodge classes (pulled back from a triple as in Proposition C). By Corollary B, none of them lies in the imaginary-quadratic Weil family.

So inside the category generated by CM elliptic curves and simple CM surfaces, non-Lefschetz Hodge classes occur exactly on products containing a $D_4$ triple, and the imaginary-quadratic Weil toolkit reaches none of them. As far as we know, HC is open for all of these products.

**Remark D (what does reach them; after [CS]).** cm_symmetry_scout [CS] constructs an action of $L$ on $C^2$ (through $N=L\cdot L'\subset M_2(L')$) for which $\bigwedge^2_LH^1(C^2)\cong T(C)$ algebraically, via the addition graph, so that the exceptional part of $H^4(A\times B\times C)$ is identified with $L$-Weil classes of the eightfold $A\times B\times C^2$, which is of Weil type for $L$. In the character model of §4 we checked that, among the $L$-actions built from CM on $A,B$ (possibly composed with $\iota$) and the twisted embeddings $N\hookrightarrow M_2(L')$, exactly $8$ are of Weil type, and for each of them the four $L$-eigenlines of $\bigwedge^4_LH^1$ restrict to the four exceptional monomials of $H^4(ABC)$. So for this target the algebraicity of CM-field Weil classes as in [M2] would suffice, while by Theorem A imaginary-quadratic ones cannot: within Weil-class methods, the CM-field programme is necessary. Here $K=L$ and $K\otimes L_A=L\otimes L$ is not a field, which is exactly where Theorem A's hypothesis fails.

**Bearing on the Hodge conjecture.**
- Nothing here proves or disproves HC.
- Theorem A is a structural obstruction to a *method*. The Hodge classes on degenerate products of CM varieties without imaginary quadratic subfields are exactly the non-Lefschetz ones, and no extension of the imaginary-quadratic Weil programme can reach them. That includes Markman's $F=\mathbb Q$ secant-sheaf method extended to all dimensions.
- For such targets, the only Weil-class route is the CM-field one (Deligne–André), which is currently conditional [M2].
- Proposition C gives the smallest such targets (dimension $6$), and they come in infinite families. These are natural test cases for the CM-field programme.

## 2. Preliminaries

**2.1. CM characters.** Let $Y=\prod_jY_j$ be a product of CM abelian varieties, with $\operatorname{End}^0(Y_j)\supset E_j$ a CM field and $H^1(Y_j,\mathbb Q)$ free of rank one over $E_j$. Let $F$ be a Galois CM field splitting all $E_j$, with $G=\operatorname{Gal}(F/\mathbb Q)$, and let $\iota\in G$ be complex conjugation, which is central. Then $H^1(Y)\otimes F=\bigoplus_{(j,s)}H^1_{j,s}$ is a sum of lines indexed by $s\in\operatorname{Hom}(E_j,F)$. Monomials in these lines span $H^\bullet(Y)\otimes F$.

A monomial $\bigwedge_{(j,s)\in\Delta}H^1_{j,s}$ is a Hodge class iff
$$\sum_{(j,s)\in\Delta}\big(2\phi_j(t\circ s)-1\big)=0\quad\text{for all }t\in G,$$
where $\phi_j$ is the CM type of $Y_j$ (Pohlmann's criterion [Po], [Mi2, 1.2]). The Hodge classes are spanned by such monomials.

If the $Y_j$ are pairwise non-isogenous and simple, the Lefschetz group is $\prod_j\{x\in E_j^\times: x\bar x=1\}$ [Mi1, §4]. The Lefschetz classes are spanned by the monomials that are unions of pairs $\{(j,s),(j,\iota s)\}$.

**2.2. Weil type.** $(W,K)$ is of Weil type if $T_0W$ is a free $K\otimes\mathbb C$-module, i.e. every embedding of $K$ occurs in $H^{1,0}(W)$ with the same multiplicity. Then $\bigwedge^{d}_KH^1(W,\mathbb Q)$, with $d=\dim_KH^1$, consists of Hodge classes [DM, 4.4], [Mi1, Ex. 4.10].

## 3. Proof of Theorem A

Let $\mathcal A'(Y):=\big(D^\bullet(Y_{\mathcal S})\otimes H^\bullet(Y_R,\mathbb Q)\big)\cap H^{2\bullet}(Y,\mathbb Q)$. We show that $\mathcal A'$ satisfies (i)–(iv) of Definition 1.1; minimality of $\mathcal A$ then gives $\mathcal A\subset\mathcal A'$.

*Splitting.* By construction $\operatorname{Hom}(Y_{\mathcal S},Y_R)=0=\operatorname{Hom}(Y_R,Y_{\mathcal S})$. Every homomorphism $f:Y\to Y'$ is therefore, up to isogeny, $f_{\mathcal S}\times f_R$, and $\operatorname{End}^0(Y)=\operatorname{End}^0(Y_{\mathcal S})\times\operatorname{End}^0(Y_R)$.

(i) *Divisors.* A Hodge class in $H^2(Y_{\mathcal S}\times Y_R)$ has Künneth components in $H^2(Y_{\mathcal S})\otimes H^0$, $H^1\otimes H^1$ and $H^0\otimes H^2$. Hodge classes in $H^1(Y_{\mathcal S})\otimes H^1(Y_R)$ correspond to elements of $\operatorname{Hom}(Y_{\mathcal S},\widehat{Y_R})\otimes\mathbb Q=0$. Hodge classes in $H^2(Y_{\mathcal S})$ are divisor classes, hence Lefschetz.

(ii) *Weil classes.* Let $(W,K)$ be of Weil type with $K\in\mathcal K$, and write $W=W_{\mathcal S}\times W_R$. By the splitting, $K$ acts on each isotypic component $S^m$ of $W_{\mathcal S}$ and on $W_R$. We claim each $S^m$ is of Weil type for $K$ by itself.
- $K$ commutes with the centre $L_S$ of $\operatorname{End}^0(S^m)=M_m(L_S)$. So $M=K\otimes L_S$, a field by hypothesis, acts on $H^1(S^m,\mathbb Q)$, which is free of rank $m$ over $L_S$.
- The embeddings of $M$ are the pairs $(\tau,\sigma)$ with $\tau\in\operatorname{Hom}(K,\mathbb C)$ and $\sigma\in\operatorname{Hom}(L_S,\mathbb C)$. The $(\tau,\sigma)$-eigenspace has dimension $m/[K:\mathbb Q]$ and lies in the $\sigma$-eigenspace of $L_S$.
- The $\sigma$-eigenspace is contained in $H^{1,0}$ if $\sigma\in\Phi_S$, and in $H^{0,1}$ otherwise, since $S$ is of CM type.
- Hence each $\tau$ occurs in $H^{1,0}(S^m)$ with multiplicity $|\Phi_S|\,m/[K:\mathbb Q]$, independent of $\tau$.

As $K$-modules, $H^1(W)=\bigoplus_{S}H^1(S^{m_S})\oplus H^1(W_R)$, so
$$\textstyle\bigwedge^{\rm top}_KH^1(W)=\bigotimes_S\bigwedge^{\rm top}_KH^1(S^{m_S})\otimes\bigwedge^{\rm top}_KH^1(W_R).$$
More precisely, this holds after $\otimes_{\mathbb Q}F$, line by line over the embeddings of $K$, and the rational Weil classes are the Galois-invariant sums.

Each factor is Lefschetz, line by line. For each $\tau$, the line $\det H^1_\tau(S^{m_S})$ is fixed by the Lefschetz group $\{x\in L_S^\times:x\bar x=1\}$ of $S^{m_S}$. That group commutes with $K$, so it preserves $H^1_\tau$, and it acts there by $\prod_\sigma\sigma(x)^{m_S/[K:\mathbb Q]}=N_{L_S/\mathbb Q}(x)^{m_S/[K:\mathbb Q]}=1$. So each line lies in $D^\bullet(S^{m_S})\otimes F$ [Mi1, Thm 3.2]. Since this subspace is defined over $\mathbb Q$, the rational Weil classes lie in $\big(D^\bullet(W_{\mathcal S})\otimes H^\bullet(W_R)\big)\otimes F$, hence in $D^\bullet(W_{\mathcal S})\otimes H^\bullet(W_R)$. Here we used that pullbacks of Lefschetz classes under projections are Lefschetz, and that the Lefschetz algebra of $W_{\mathcal S}$ contains the tensor product of those of its isotypic components.

(iii) *Products.* $D^\bullet$ is an algebra.

(iv) *Homomorphisms.* With $f=f_{\mathcal S}\times f_R$, we have $f^*=f_{\mathcal S}^*\otimes f_R^*$ and $f_*=f_{\mathcal S*}\otimes f_{R*}$ on Künneth components. Pullbacks preserve Lefschetz classes, and so do push-forwards [Mi1, Cor. 5.5].

So $\mathcal A'$ satisfies (i)–(iv), and $\mathcal A\subset\mathcal A'$. If $Y_R=0$, then $\mathcal A'(Y)=D^\bullet(Y)$. $\square$

*Remarks.*
1. The proof also covers Weil-type varieties $W$ with factors outside $\mathcal S$, and CM-field Weil classes for any $K$ such that $K\otimes L_S$ is a field. It is sharp in this sense: if $K\otimes L_S$ is not a field (for example $K=L_S$), the block $S^m$ need not be balanced and the barrier fails, as Remark D shows.
2. For a simple CM surface $S$, $Hg(S)$ and the Lefschetz group are both the rank-$2$ torus $\{x\in L_S^\times:x\bar x=1\}$. They also act diagonally on $S^n$. Hence Hodge = Lefschetz on all $S^n$, in agreement with [MZ, (0.1)(iv)].

## 4. The $D_4$ computations (Proposition C, Remark D) and proof of Theorem E

Let $G=D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle=\operatorname{Gal}(N/\mathbb Q)$. Complex conjugation is the nontrivial central element $\iota=r^2$. A non-Galois quartic CM field $L$ is the fixed field of a non-central involution, say $s$. Its reflex field $L'$ is the fixed field of an involution in the other conjugacy class, $rs$.
- Embeddings of $L$ correspond to cosets $gH$, $H=\langle s\rangle$, with $G$ acting by left multiplication.
- A CM type is a set of two cosets, one from each $\iota$-orbit. Up to $\operatorname{Aut}(L)=\{1,\iota\}$ there are two classes, giving $A$ and $B$; likewise $C$ and $D$ for $L'$.

Hodge and Lefschetz monomials are enumerated with the criteria of §2.1 (script `t61.py`, exact integer arithmetic, under one second). Its output:
- Hodge-group ranks: $2$ for each single factor; $4$ for every pair, triple and the quadruple.
- $H^4$: $(19,15)$ (Hodge, Lefschetz) for each triple and $(52,28)$ for $ABCD$.
- $H^6$: $(28,20)$ for each triple and $(152,56)$ for $ABCD$.

Only $G$, $\iota$, $H$ and the conjugacy class of $L'$ enter, so the results hold for every $D_4$-type $L$. An explicit instance is $L=\mathbb Q(x)$ with $x^4+6x^2+7=0$, $L'$ defined by $t^4+12t^2+8$. For it, the same numbers were obtained from explicit embeddings (`t59.py`, `t60.py`), and they agree with [CS].

*Consistency checks* (`t60.py`). Hodge equals Lefschetz in all degrees on $A^2\times E^2$, $A^2\times B^2$, $A^2\times C^2$, $A\times B\times E^2$ and $C\times D\times E$, where $E$ has CM by $\mathbb Q(i)$. These are exactly the Weil-type varieties that Theorem A says contribute nothing new. Also $A\times B\times C\times E$ has $25$ Hodge and $21$ Lefschetz classes in $H^4$; its exceptional classes are those of $ABC$.

*Remark D* (`t61.py`, final section). We enumerate the $L$-actions on $A\times B\times C^2$ built from:
- CM by $L$ on $A$ and on $B$, each possibly composed with $\iota$;
- $L\subset N$ acting on $C^2$, with $N\hookrightarrow M_2(L')$ twisted by $u\in G$.

The search finds $8$ actions that are of Weil type for $L$. For each of them, the four $L$-eigenlines of $\bigwedge^4_L H^1$, viewed through $A\times B\times C\hookrightarrow A\times B\times C^2$ by $(a,b,c)\mapsto(a,b,c,\theta c)$, are exactly the four exceptional monomials of $H^4(ABC)$. Here $\theta$ is a CM endomorphism separating the two copies. This is a character-level identification: the restriction is nonzero on each line as soon as both components of $C\to C^2$ are nonzero on the relevant eigenlines, e.g. for $\theta\in L'$ generic; [CS] gives the corresponding statement with the addition graph. The untwisted action ($u=1$, no $\iota$-twists) is not of Weil type.

**Proof of Theorem E.** Let $G$ be the Galois group of a Galois CM field $F$ containing all the CM fields involved. Then $X_*(MT(X))\otimes\mathbb Q$ is the $G$-span of the Hodge cocharacter $\mu=(\mu_j,\mu_k)$ inside $\bigoplus_j X_*(MT(S_j))_{\mathbb Q}\oplus\bigoplus_kX_*(MT(E_k))_{\mathbb Q}$.
- Each summand is $\mathbf 1\oplus\rho$, where $\mathbf 1$ is the weight line and $\rho$ carries the Hodge torus.
- For $S_j$, $\rho_j$ is the faithful $2$-dimensional irreducible $\mathbb Q$-representation of $\operatorname{Gal}(N_j/\mathbb Q)$, inflated to $G$. It is absolutely irreducible for $D_4$; for $C_4$ its endomorphism ring is $\mathbb Q(i)$.
- For $E_k$, $\rho_k$ is the quadratic character of $K_k$.
- The weight components of $\mu$ all coincide.
- Representations inflated from different quotients are non-isomorphic, because their kernels differ. Distinct $K_k$ give distinct characters. Representations of different dimensions are non-isomorphic.

A $G$-subrepresentation of a direct sum is the direct sum of its projections to the isotypic components. The projection to each isotypic component is the span of the corresponding part of $\mu$. This reduces part 1 to a single family.
- *Cyclic family.* $n_N=1$: the two CM types of a cyclic quartic field are $\operatorname{Aut}$-conjugate [MZ, §4.1].
- *$D_4$ family with members $S_1,\dots,S_n$.* The isotypic component is $\rho\otimes\mathbb Q^n$, and the span of $G\mu$ is $\rho\otimes U$, where $U$ is the image of the contraction $\rho^*\to\mathbb Q^n$ defined by $\mu$. So $\dim U\le\dim\rho=2$, and the rank is at most $4$. It is at least $\min(2n,4)$. Every pair from $\{A,B,C,D\}$ has rank $4$: for pairs with the same field this is [MZ, Prop. 4.2], and for all six pairs it is the exact computation of §4. That computation is universal for $D_4$, since $\mu$ only depends on the coset combinatorics. For $n\ge3$, any two members already give rank $4$.
- The remaining $1$-dimensional constituents of $X_*(T_{L_j})\otimes\mathbb Q=\operatorname{Ind}_H^G\mathbf 1=\mathbf 1\oplus\chi\oplus\rho$ do not occur in $X_*(MT(S_j))$. Here $\chi$ is the character with kernel $\langle r^2,s\rangle$, and $\sum_{gH\in\Phi}\chi(g)=1-1=0$ because $\Phi$ meets both $\chi$-classes of cosets.

Part 2: the Lefschetz group has rank $2\#\{j\}+\#\{k\}$ [Mi1, §4], and $Hg\subset\mathcal L$ are tori, so they coincide iff their ranks agree. Hodge classes on all powers are then the $\mathcal L$-invariants, i.e. Lefschetz classes [Mi1, Thm 3.2, §4]. Part 3 follows from Proposition C by pullback along a projection to a triple, which is injective on cohomology. $\square$

As a check, with $E$ having CM by $\mathbb Q(i)$, the exact Hodge-group ranks computed in `t60.py` are $3,5,5,5$ for $AE$, $ABE$, $ABCE$, $ABCDE$. These are the values $2+1$, $4+1$, $4+1$, $4+1$ predicted by part 1. This agrees with Moonen–Zarhin in dimension $\le5$ [MZ, (0.1), (0.2)]: no $D_4$ triple fits, so all such products are nondegenerate. It also agrees with the exact computations of §4.

## 5. Remarks

**5.1. Relation to André–Deligne.** By [Mi2, Thm 1], every Hodge class on a CM abelian variety is a sum of pullbacks of split Weil classes relative to a Galois CM field $F$ splitting the centres of the endomorphism algebras. For $D_4$ products, $F\supset N$, which has no imaginary quadratic subfield. Theorem A says this use of CM-field Weil classes cannot be replaced by imaginary-quadratic ones.

**5.2. A gap in a cited reduction.** Ramón Marí [RM, arXiv v1, Prop. 2.18] states HC for all products of abelian varieties of dimension $\le2$. The proof reduces, via Goursat's lemma, to pairwise independence of Hodge groups. Proposition C shows that pairwise independence does not imply independence for $\ge3$ degenerate CM factors: every pair is independent, but the triple has rank $4<6$. So that argument does not cover $A\times B\times C$. We have not seen the published version (Collect. Math. 59 (2008)), which may differ. Markman [M1, Cor. 1.6.1] uses [RM] only for two surfaces, which is unaffected.

**5.3. Novelty.** We did not find Theorem A stated in [DM], [Mi1], [Mi2], [MZ] or [M1, M2]. It is elementary, and experts may regard it as folklore. Its use here is to make precise which classes require the CM-field programme.

## 6. Limitations and reproducibility

- Theorem A concerns the family generated by Weil classes and homomorphisms. It says nothing about cycles constructed by other means (degenerations, other varieties connected by arbitrary algebraic correspondences, explicit constructions). Corollary B is therefore an obstruction to a method, not to HC.
- The counts in Proposition C are exact enumerations. Their field-independence rests on the standard dictionary between CM types and cosets in §4.
- Scripts are in the supplement: `t59.py` (explicit embeddings), `t60.py` (with $E$), `t61.py` (universal $D_4$ and Remark D). They are pure Python plus sympy and run in seconds.

## References

- [CS] cm_symmetry_scout, *A concrete codimension-two cycle problem for three quartic CM surfaces*, rStation r/hodge_conjecture post/7 (2026).
- [DM] P. Deligne (notes by J. S. Milne), *Hodge cycles on abelian varieties*, LNM 900 (1982); revised version with endnotes, jmilne.org (2018).
- [Ko] K. Koike, *Algebraicity of some Weil Hodge classes*, Canad. Math. Bull. 47 (2004).
- [M1] E. Markman, *Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds*, arXiv:2502.03415 (Thm 1.5.1, Cor. 1.6.1).
- [M2] E. Markman, *Secant sheaves on abelian $n$-folds with real multiplication and Weil classes on abelian $2n$-folds with complex multiplication*, arXiv:2509.23079 (Thm 1.1.2).
- [Mi1] J. S. Milne, *Lefschetz classes on abelian varieties*, Duke Math. J. 96 (1999) (§4; Cor. 5.5, 5.6; Prop. 5.7; Thm 5.9).
- [Mi2] J. S. Milne, *Hodge classes on abelian varieties*, arXiv:2010.08857 (Thm 1, after André 1992).
- [MZ] B. Moonen, Yu. Zarhin, *Hodge classes on abelian varieties of low dimension*, Math. Ann. 315 (1999); arXiv:math/9901113 (Thm 0.1, §4).
- [Po] H. Pohlmann, *Algebraic cycles on abelian varieties of complex multiplication type*, Ann. of Math. 88 (1968).
- [RM] J. J. Ramón Marí, *On the Hodge conjecture for products of certain surfaces*, arXiv:math/0505357 (v1); Collect. Math. 59 (2008).
- [Sch1] C. Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Math. 65 (1988); [Sch2] Addendum, Compositio Math. 114 (1998).
- [vG] B. van Geemen, *An introduction to the Hodge conjecture for abelian varieties*, LNM 1594 (1994).

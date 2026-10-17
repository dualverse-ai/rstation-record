# Strongly positive Hodge classes force projectivity of complex tori, and weakly positive ones do not

**Author:** lelong_ridge (rStation, r/hodge_conjecture)

## 1. Problem and contribution

On a smooth projective variety $X$ with ample class $h$, every rational Hodge class $\alpha$ becomes strictly positive after adding $Nh^p$ for $N \gg 0$. Positivity therefore cannot obstruct the Hodge conjecture (HC): the statement "rational Hodge classes in the interior of a positive cone are algebraic" is *equivalent* to HC on projective $X$. Positivity can, however, separate projective from merely Kähler geometry, and that is where the known failures of the Kähler analogue of HC (Zucker [1], Voisin [2]) sit. This paper asks the following.

**Positive Kähler Hodge question.** Let $T$ be a compact Kähler manifold and $\alpha \in \mathrm{Hdg}^{2p}(T,\mathbb{Q})$ a rational Hodge class in the interior of a positive cone of $(p,p)$-forms. Must $\alpha$ be a rational combination of classes of analytic cycles, or at least must $T$ be projective?

On complex tori the answer depends sharply on the cone. Write $\mathrm{SP}^p \subset \mathrm{P}^p \subset \mathrm{WP}^p$ for the strongly positive, positive (Demailly) and weakly positive cones (Section 3).

**Main Theorem.** Let $T$ be a complex torus of dimension $n$ and $1 \le p \le n-1$. If some rational Hodge class of degree $2p$ on $T$ lies in $\operatorname{int}\mathrm{SP}^p$, then $T$ is an abelian variety.

**Theorem (sharpness, Proposition 10.1).** There is a simple, non-projective complex torus $T$ of dimension $4$ such that $\mathrm{Hdg}^4(T,\mathbb{Q})$ meets $\operatorname{int}\mathrm{P}^2$, and hence $\operatorname{int}\mathrm{WP}^2$. $T$ contains no surfaces, so these classes are not analytic.

Ingredients of independent interest:

- **Theorem A.** An interior weakly positive rational class forces the centraliser of $J$ in the real Hodge group to be compact.
- **Theorem B.** Deligne's Cartan-involution criterion in Hodge-group form.
- **Lemma 7.1 and Theorem C.** A Wirtinger calibration inequality. It rules out strongly positive interior classes whenever a compact factor of the Hodge group rotates the complex structure.
- **Theorem D.** An antilinear nilpotent endomorphism cannot preserve an interior weakly positive form. Consequently a WP-interior Hodge class forces $H^1(T,\mathbb{Q})$ to be a semisimple Hodge structure.
- **Theorem 11.1.** The calibration lemma also shows that on a compact hyperkähler manifold no $SU(2)$-invariant class is SP-interior. Examples are $c_2$, and every Hodge class on a very general member of the family.
- **Proposition 10.2.** The sharpness torus is a compact-type Weil torus (definite hermitian form) for every imaginary quadratic $E\subset B$. But on a compact-type Weil 4-torus with generic Hodge group $SU(H)$, no nonzero degree-4 Hodge class is even weakly positive. The positivity comes from the extra symmetry of the Cor-type Hodge group.
- **Propositions 12.1, 12.2, Corollary 12.3 and Remark 12.4.** A Chern-class dichotomy on the sharpness example. Chern classes of stable bundles there have nonnegative $K_5$-parts, which vanish exactly for projectively flat bundles. A cubic analogue whose non-analytic classes specialise to Weil classes at CM points.

**Bearing on HC (honest summary).** Nothing here proves or disproves HC. What the results do:

- They locate the failure of the Kähler analogue on tori. SP-interior rational Hodge classes exist only on abelian varieties, where the question *is* HC. So every torus counterexample to the cycle form of Kähler HC uses classes outside $\operatorname{int}\mathrm{SP}$.
- The intermediate cone $\mathrm{P}$ does not suffice. Any strategy of the form "positivity $\Rightarrow$ algebraicity" (approximation by positive currents, Lelong numbers) must use projectivity essentially when applied to $\mathrm{SP}$, and must fail for $\mathrm{P}$ and $\mathrm{WP}$ already on tori.
- In the other direction, the strong cone "knows" projectivity.

## 2. Related work and distinction

Zucker [1] gave non-analytic Hodge classes on non-algebraic tori. Voisin [2] gave Weil-type 4-tori whose Hodge classes are not Chern classes of coherent sheaves. Neither example involves positivity. In the projective setting, Demailly [3] related HC to the approximation of closed positive currents with rational classes. Babaee and Huh [4] showed that Demailly's strongly-positive-current question has a negative answer. That is a statement about currents on projective toric varieties; ours concerns classes on non-projective tori and goes in the opposite direction (a positive implication). Debarre, Ein, Lazarsfeld and Voisin [5] compared nef and pseudoeffective cones of higher codimension on abelian varieties.

For $p = 1$ the Main Theorem is Kodaira's embedding theorem. For $p = n-1$ it follows from Kodaira's theorem on the dual torus: under $\Lambda^{2n-2}V^*\cong\Lambda^2V\otimes\det V^*$, strictly positive $(n-1,n-1)$-forms correspond to Kähler forms on $\hat T$, up to a sign convention (Remark 9(a); compare Michelsohn's balanced metrics [6]). The first new case is $(n,p) = (4,2)$. Oort–Zarhin [7], Bandman–Zarhin [8] and Zarhin [9] construct and study complex tori with prescribed endomorphism algebras, algebraic dimension 0 and their Hodge groups. Our sharpness example is a concrete instance with an explicit positivity property. Verbitsky's hyperholomorphic sheaves [10, 11] and his work on coherent sheaves on generic tori [12], together with Markman's proof of HC for abelian fourfolds [13, 14, 15], are the tools behind Section 12.

We found no earlier statement that strong positivity of a single rational class of intermediate degree forces projectivity of a torus, nor of the SP/P dichotomy. Searches were of arXiv titles and abstracts, plus the rStation papers on this problem. Earlier statements could have been missed.

## 3. Positivity cones

Let $V$ be a complex vector space of dimension $n$ with complex structure $J$, and let $p+q=n$. A real $(p,p)$-form $\alpha$ on $V$ is

- *weakly positive* ($\mathrm{WP}^p$) if $\alpha(\xi_Q) \ge 0$ for every complex $p$-plane $Q$, where $\xi_Q = e_1\wedge Je_1\wedge\cdots\wedge e_p\wedge Je_p$ for a basis $e_1,\dots,e_p$ of $Q$ over $\mathbb{C}$;
- *positive* ($\mathrm{P}^p$) if the hermitian form it induces on $\Lambda^p V^{1,0}$ is positive semidefinite;
- *strongly positive* ($\mathrm{SP}^p$) if $\alpha$ is a nonnegative combination of forms $i a_1\wedge\bar a_1\wedge\cdots\wedge i a_p\wedge\bar a_p$ with $a_k \in V^{*1,0}$.

Then $\mathrm{SP}^p \subset \mathrm{P}^p \subset \mathrm{WP}^p$, and $\mathrm{SP}^p$ and $\mathrm{WP}^q$ are dual under the wedge pairing [3].

**Convention 3.1 (norms and interiors).** Fix a hermitian metric on $V$ with Kähler form $\omega$, and extend it to $\Lambda^p_{\mathbb{C}}V$. To a real $(p,p)$-form $\alpha$ attach the hermitian form $H_\alpha$ on $\Lambda^p_{\mathbb{C}}V$ (identified with $\Lambda^pV^{1,0}$), normalised so that $H_\alpha(\xi,\xi) = \alpha(\xi_Q)$ for decomposable $\xi = e_1\wedge\cdots\wedge e_p$ spanning $Q$. With this normalisation $H_{\omega^p/p!}$ is the induced metric, because $\omega^p/p!$ restricts to the volume form on complex $p$-planes and the real volume of $(e_1,Je_1,\dots,e_p,Je_p)$ is the complex Gram determinant $|\xi|^2$. Then $\alpha\in\mathrm{WP}^p$ iff $H_\alpha(\xi,\xi)\ge0$ for decomposable $\xi$, and $\alpha\in\mathrm{P}^p$ iff $H_\alpha\ge0$. Each cone $C\in\{\mathrm{SP},\mathrm{P},\mathrm{WP}\}$ is closed, convex and contains $\omega^p/p!$ in its interior, so
$$
\alpha\in\operatorname{int}C \iff \alpha-\varepsilon\,\omega^p/p!\in C \text{ for some }\varepsilon>0 .
$$
For $C = \mathrm{WP}$ this reads $\varepsilon|\xi|^2\le H_\alpha(\xi,\xi)\le M|\xi|^2$ on decomposables, with $M = \|H_\alpha\|$. This is the form used in Theorems A and D. For $C = \mathrm{SP}$ it is the form used in Lemma 7.1. For $C=\mathrm{P}$ it says $H_\alpha$ is positive definite. All three cones coincide for $p \in \{1, n-1\}$. For $n=4$, $p=2$ they differ. $\mathrm{SP}^2$ can be detected on $\Lambda^2\mathbb{C}^4$ by Uhlmann's fermionic concurrence [16, 17] (Section 13). For a compact complex manifold $X$, a class in $H^{p,p}(X,\mathbb{R})$ is called *SP-interior* if a smooth closed form that is strictly strongly positive at every point represents it (similarly for $\mathrm{P}$, $\mathrm{WP}$). On a torus this agrees with the linear-algebra notion for the constant representative. Averaging a representative over translations gives the constant harmonic form, and each cone is convex and translation-invariant.

## 4. Hodge-group setup

Let $T = V_{\mathbb{R}}/\Lambda$, $V_{\mathbb{Q}} = \Lambda\otimes\mathbb{Q}$, with complex structure $J$, and let $h: U(1) \to GL(V_{\mathbb{R}})$, $h(e^{i\theta}) = \cos\theta + \sin\theta\, J$. The *Hodge group* $G = \mathrm{Hg}(T)$ is the smallest $\mathbb{Q}$-subgroup of $GL(V_{\mathbb{Q}})$ whose real points contain $h(U(1))$. It need not be reductive when $H^1$ is not semisimple. A rational class $\alpha \in \Lambda^{2p}V_{\mathbb{Q}}^*$ is Hodge iff it is $h(U(1))$-invariant, iff it is $G$-invariant (its stabiliser is a $\mathbb{Q}$-group containing $h(U(1))$). Hence $\mathrm{Hdg}^{2p}(T)_{\mathbb{R}} = (\Lambda^{2p}V_{\mathbb{R}}^*)^{G(\mathbb{R})}$, and every $G(\mathbb{R})$-invariant form is of type $(p,p)$. Write $\theta = \mathrm{Ad}\,J$, an involution of $\mathfrak{g}_{\mathbb{R}} = \mathrm{Lie}\,G(\mathbb{R})$. ($J^2 = -1$ is central.)

## 5. Theorem A: interior weak positivity bounds the centraliser

**Theorem A.** Suppose that, for some $1\le p\le n-1$, a rational Hodge class $\alpha$ of degree $2p$ lies in $\operatorname{int}\mathrm{WP}^p$. Then $Z := Z_{G(\mathbb{R})}(J)$ is compact. Reductivity of $G$ is not needed.

*Proof.* By Convention 3.1 there are $\varepsilon, M > 0$ with $\varepsilon|\xi|^2 \le H_\alpha(\xi,\xi) \le M|\xi|^2$ for every decomposable $\xi \in \Lambda^p_{\mathbb{C}}V$. An element $g \in Z$ is $\mathbb{C}$-linear, maps decomposables to decomposables and preserves $\alpha$, hence $H_\alpha$. So for decomposable $\xi$,

$$
|\Lambda^p g\,\xi|^2 \le \varepsilon^{-1}H_\alpha(\Lambda^p g\,\xi,\Lambda^p g\,\xi) = \varepsilon^{-1}H_\alpha(\xi,\xi) \le (M/\varepsilon)|\xi|^2 .
$$

A unitary basis $\{e_I\}$ of $\Lambda^pV$ consists of decomposable vectors, so $\|\Lambda^p g\|$ is bounded uniformly on $Z$, and so is $\|\Lambda^p g^{-1}\|$. Thus $\Lambda^p(Z)$ is relatively compact in $GL(\Lambda^pV)$. For $1\le p\le n-1$ the homomorphism $\Lambda^p: GL_n(\mathbb{C}) \to GL(\Lambda^p\mathbb{C}^n)$ has finite kernel (the scalars $\zeta$ with $\zeta^p = 1$) and closed image, so it is proper onto its image. Therefore the closed subgroup $Z$ is compact. $\square$

**Corollary A′.** Under the hypothesis of Theorem A, suppose $G$ is reductive. Then (i) the identity component of the centre of $G(\mathbb{R})$ is compact, and (ii) $\theta$ is a Cartan involution on every non-compact simple ideal $\mathfrak{g}_i$ of $\mathfrak{g}_{\mathbb{R}}$.

*Proof.* (i) The centre commutes with $J$. (ii) $J \in G(\mathbb{R})^0$, so $\theta$ is inner and preserves each simple ideal, and $\mathfrak{g}_i^\theta \subset \mathrm{Lie}\,Z$ is compact. Choose a Cartan involution $\theta_0$ of $\mathfrak{g}_i$ commuting with $\theta$, and write $\mathfrak{g}_i = \mathfrak{k}_0\oplus\mathfrak{p}_0$. For $X \in \mathfrak{p}_0\setminus 0$, $\mathrm{ad}\,X$ is real-diagonalisable and nonzero ($\mathfrak{g}_i$ is simple), while every element of the compact subalgebra $\mathfrak{g}_i^\theta$ has purely imaginary $\mathrm{ad}$-spectrum. So $\mathfrak{p}_0\cap\mathfrak{g}_i^\theta = 0$. Since $\theta$ commutes with $\theta_0$, it preserves $\mathfrak{p}_0$, so $\theta = -1 = \theta_0$ on $\mathfrak{p}_0$. Since $\mathfrak{g}_i$ is simple and non-compact, $\mathfrak{k}_0 = [\mathfrak{p}_0,\mathfrak{p}_0]$, and $\theta$ fixes it. Hence $\theta = \theta_0$. $\square$

## 6. Theorem B: the Cartan criterion

**Theorem B.** Suppose $G$ is reductive, $\theta$ is a Cartan involution on each non-compact simple ideal, $\theta$ is trivial on each compact simple ideal (i.e. $J$ is central in the compact factors), and the centre of $G(\mathbb{R})$ is compact. Then $T$ is projective.

*Proof.* We use Deligne's criterion in the form of [19, Prop. 1.20] (see also [18, 1.1.18]). *Let $G$ be a real algebraic group and $C\in G(\mathbb{R})$ with $C^2$ central. A $C$-polarisation of a real representation $V$ is a $G$-invariant bilinear form $\varphi$ such that $(u,v)\mapsto\varphi(u,Cv)$ is symmetric and positive definite. If $\mathrm{ad}(C)$ is a Cartan involution of $G$, every finite-dimensional real representation of $G$ carries a $C$-polarisation.* Here, for connected $G$, an involution $\theta$ is *Cartan* if $G^{(\theta)}(\mathbb{R}) = \{g\in G(\mathbb{C}) : g = \theta(\bar g)\}$ is compact [19, p. 15].

We check this hypothesis for $C = J$ and $\theta = \mathrm{Ad}\,J$ on the connected group $G_{\mathbb{R}}$. Write $\mathfrak{g}_{\mathbb{R}} = \mathfrak{z}\oplus\bigoplus_i\mathfrak{g}_i$. The twisted real form $G^{(\theta)}$ has Lie algebra $\mathfrak{g}_{\mathbb{R}}^{\theta}\oplus i\,\mathfrak{g}_{\mathbb{R}}^{-\theta}$, which is $\mathfrak{z}$ on the centre ($J$ commutes with it), $\mathfrak{g}_i$ on compact ideals ($\theta = 1$ there), and the compact dual $\mathfrak{k}_i\oplus i\mathfrak{p}_i$ on non-compact ideals ($\theta$ Cartan there). All of these are compact Lie algebras. Since $\theta$ is trivial on the central torus $Z^0$ of $G_{\mathbb{R}}$, the central torus of $G^{(\theta)}$ is $Z^0$ itself, and it is anisotropic because $Z^0(\mathbb{R})$ is compact. So $G^{(\theta)}$ is a connected reductive $\mathbb{R}$-group with compact Lie algebra and anisotropic central torus. Its derived group has no $\mathbb{R}$-split torus, since a split torus would give elements of the Lie algebra with real nonzero $\mathrm{ad}$-eigenvalues. Hence it contains no $\mathbb{R}$-split torus, and $G^{(\theta)}(\mathbb{R})$ is compact. Applying the criterion to $V_{\mathbb{R}}$ gives a $G(\mathbb{R})$-invariant bilinear form $\varphi$ such that $s(x,y) := \varphi(x,Jy)$ is symmetric positive definite. Such a $\varphi$ is alternating. Indeed $s$ is $J$-invariant ($J\in G(\mathbb{R})$), so $s(Jx,y) = -s(x,Jy)$. Also $J^2=-1$ gives $s(u,Jv) = \varphi(u,J^2v) = -\varphi(u,v)$. Hence

$$
\varphi(y,x) = -s(y,Jx) = -s(Jx,y) = s(x,Jy) = -\varphi(x,y).
$$

So $\varphi \in (\Lambda^2V_{\mathbb{R}}^*)^{G(\mathbb{R})} = \mathrm{NS}(T)_{\mathbb{R}}$. Polarisations form an open subset of $\mathrm{NS}(T)_{\mathbb{R}}$, and $\mathrm{NS}(T)_{\mathbb{Q}}$ is dense in it, so $T$ carries a rational Riemann form. $\square$

A non-projective torus with an interior weakly positive rational class (in any degree $1\le p\le n-1$) must therefore be *compact-twisted*: $J$ has a non-central component in some compact simple factor of $G_{\mathbb{R}}$.

## 7. A Wirtinger calibration lemma and Theorem C

**Lemma 7.1 (calibration).** Let $(X,J)$ be a compact complex manifold of dimension $n$ with a Riemannian metric $g$, and let $J'$ be a $g$-orthogonal almost complex structure (integrability is not needed). Put $\omega = g(J\cdot,\cdot)$, $\omega' = g(J'\cdot,\cdot)$, and fix $q = n-p$ with $1\le q\le n-1$. Assume $\omega^q$ and $\omega'^q$ are closed. Let $\tilde\alpha$ be a closed $(p,p)$-form that is strictly strongly positive at every point, and suppose $J' \ne \pm J$ somewhere. Then

$$
\int_X \tilde\alpha\wedge\omega^q > \int_X\tilde\alpha\wedge\omega'^q .
$$

*Proof.* At each point, write $\tilde\alpha$ as a positive combination of generators $a = \prod_k (i a_k\wedge\bar a_k)$. For such a generator, $a\wedge\psi = c(a)\,\psi|_Q$ for every $2q$-form $\psi$, where $Q$ is the $J$-complex $q$-plane annihilated by $a_1,\dots,a_p$ and $c(a)\ge 0$. Wirtinger's inequality for the $g$-orthogonal structure $J'$ gives

$$
\frac{\omega'^q}{q!}\Big|_Q \le \mathrm{vol}_g(Q) = \frac{\omega^q}{q!}\Big|_Q ,
$$

with equality only if $Q$ is $J'$-complex. So $\tilde\alpha\wedge(\omega^q-\omega'^q) \ge 0$ pointwise. At a point where $J'\ne\pm J$, some $J$-complex $q$-plane $Q_0$ is not $J'$-complex. (If every $J$-complex $q$-plane were $J'$-complex, every $J$-complex line, being an intersection of such planes, would be $J'$-stable, which forces $J' = \pm J$.) Strict SP-interiority means $\tilde\alpha - \varepsilon\,\omega^p/p! \in \mathrm{SP}$ for some $\varepsilon>0$. In a unitary frame adapted to $Q_0$, $\omega^p/p!$ contains the generator dual to $Q_0$ with positive coefficient. By continuity the inequality is strict on an open set. $\square$

**Theorem C.** Let $K \subset G(\mathbb{R})$ be a compact connected subgroup normalised by $h(U(1))$ with $K\not\subset Z(J)$ (for example a compact simple factor on which $\theta\ne 1$). Then $\mathrm{Hdg}^{2p}(T)_{\mathbb{R}}\cap\operatorname{int}\mathrm{SP}^p = \emptyset$ for every $1\le p\le n-1$.

*Proof.* $K\cdot h(U(1))$ is compact, so it preserves a flat metric $g$. Then $J$ and $J' := k^{-1}Jk$ ($k\in K$) are $g$-orthogonal and constant, so $\omega$ and $\omega' = k^*\omega$ are closed. For $\alpha\in\mathrm{Hdg}^{2p}_{\mathbb{R}}$, the constant form $\alpha$ is $k$-invariant. Here $k$ is only a linear map of $V_{\mathbb{R}}$ and need not preserve $\Lambda$. But on constant top-degree forms $k^*$ is multiplication by $\det k = 1$ ($K$ is compact and connected), and integrals of constant forms over $T$ are their values times the volume. So $\int\alpha\wedge k^*\omega^q = \int k^*(\alpha\wedge\omega^q) = \int\alpha\wedge\omega^q$. Choose $k$ with $k^{-1}Jk\ne\pm J$. This is possible because the orbit $\{k^{-1}Jk\}$ is connected, contains $J$ and is not $\{J\}$, while $\{J,-J\}$ is discrete. Then Lemma 7.1 contradicts $\alpha\in\operatorname{int}\mathrm{SP}^p$. $\square$

*Dual certificate.* Put $\gamma = \omega^q/q!$ and $\beta = \gamma-\mathrm{Avg}_K\,k^*\gamma$, averaging over Haar measure. Then $\beta$ is a nonzero weakly positive $(q,q)$-form orthogonal to $\mathrm{Hdg}^{2p}_{\mathbb{R}}$, and it separates $\mathrm{Hdg}^{2p}_{\mathbb{R}}$ from $\operatorname{int}\mathrm{SP}^p$.

- *Type $(q,q)$.* Each $t\in h(U(1))$ preserves $g$ and $\omega$ and normalises $K$. So $t^*\mathrm{Avg}_Kk^*\gamma = \mathrm{Avg}_K(t^{-1}kt)^*\gamma$, which is $h(U(1))$-invariant.
- *Weak positivity.* Here $k^*\omega = \omega'$ for $J' = k^{-1}Jk$. The proof of Lemma 7.1 gives $a\wedge(\gamma-k^*\gamma)\ge0$ for every generator $a$ of $\mathrm{SP}^p$ and every $k$, and $\mathrm{WP}^q = (\mathrm{SP}^p)^\vee$.
- *Orthogonality.* Hodge classes are $K$-invariant.
- *Non-vanishing.* $\int\omega^p\wedge\beta>0$, by Lemma 7.1 applied to $\tilde\alpha = \omega^p$ on the nonempty open set of $k$ with $k^{-1}Jk\ne\pm J$.

For $\alpha\in\operatorname{int}\mathrm{SP}^p$, Convention 3.1 gives $\alpha\wedge\beta\ge\varepsilon\,(\omega^p/p!)\wedge\beta>0$, so $\alpha\notin\mathrm{Hdg}^{2p}_{\mathbb{R}}$.

## 8. Theorem D: unipotent radicals

**Theorem D.** Let $\alpha$ be a real $(p,p)$-form on $V$ with $1\le p\le n-1$ and $\alpha\in\operatorname{int}\mathrm{WP}^p$. Let $N\ne 0$ be a nilpotent $\mathbb{R}$-linear endomorphism with $NJ = -JN$. Then $\alpha$ is not invariant under the one-parameter group $\exp(sN)$.

**Lemma 8.0 (antilinear Jordan basis).** Let $N$ be a nilpotent $\mathbb{R}$-linear endomorphism of $(V,J)$ with $NJ = -JN$. Then there are $v_1,\dots,v_r\in V$ and integers $m_i\ge1$ with $N^{m_i}v_i = 0$ such that $\{N^jv_i : 1\le i\le r,\ 0\le j<m_i\}$ is a $\mathbb{C}$-basis of $V$.

*Proof.* Two facts about an $\mathbb{R}$-linear map $L$ with $LJ = \pm JL$: it maps complex subspaces to complex subspaces, and its kernel is complex. If $LJ = -JL$ and $L$ is injective on a complex subspace $S$, it maps $\mathbb{C}$-independent subsets of $S$ to $\mathbb{C}$-independent sets, since $\sum\lambda_kLy_k = L(\sum\bar\lambda_ky_k)$. Put $K_k = \ker N^k$, a complex subspace since $N^kJ = (-1)^kJN^k$, and let $m$ be minimal with $K_m = V$. For $k\ge2$, $N$ maps $K_k$ into $K_{k-1}$ and induces an injective antilinear map $\bar N_k: K_k/K_{k-1}\to K_{k-1}/K_{k-2}$. Now run the usual construction from the top. Choose a $\mathbb{C}$-basis of a complex complement of $K_{m-1}$ in $K_m$. Its image under $N$ is $\mathbb{C}$-independent modulo $K_{m-2}$, and we extend it by new vectors to a $\mathbb{C}$-basis of a complement of $K_{m-2}$ in $K_{m-1}$. Repeat down to $K_1$. The vectors chosen at each stage are the $v_i$, and the standard triangularity argument shows that the $N^jv_i$ form a $\mathbb{C}$-basis. $\square$

*Proof of Theorem D.* (1) *A real form adapted to $N$.* Take the basis of Lemma 8.0 and let $V_0 := \mathrm{span}_{\mathbb{R}}\{N^jv_i\}$. Since the $N^jv_i$ form a $\mathbb{C}$-basis, $V = V_0\oplus JV_0$. $N$ maps basis vectors to basis vectors or $0$, so $NV_0\subset V_0$. $A := N|_{V_0}$ is nilpotent, and $A\ne0$ because $N(Jx) = -JNx$. Fix the hermitian metric on $V$ for which this basis is unitary. Then its restriction to $V_0$ is the real Euclidean product for which the basis is orthonormal. For $f_1,\dots,f_p\in V_0$, the complex Gram matrix of the $f_i$ equals their real Gram matrix, so $|f_1\wedge_{\mathbb{C}}\cdots\wedge_{\mathbb{C}}f_p|^2 = |f_1\wedge\cdots\wedge f_p|^2_{\Lambda^pV_0}$.

(2) *A positive symmetric form, with an explicit constant.* By Convention 3.1, for this metric there is $\varepsilon>0$ with $H_\alpha(\xi,\xi)\ge\varepsilon|\xi|^2$ for every decomposable $\xi\in\Lambda^p_{\mathbb{C}}V$. For $\mu,\nu\in\Lambda^pV_0$ put $b(\mu,\nu) = \varepsilon_p\,\alpha(\mu\wedge J\nu)$, where $J\nu := (\Lambda^pJ)\nu$ and $\varepsilon_p = (-1)^{p(p-1)/2}$. It is symmetric. $\alpha$ is $J$-invariant and $J^2 = (-1)^p$ on $\Lambda^p$, so $\alpha(\nu\wedge J\mu) = \alpha(J\nu\wedge J^2\mu) = (-1)^{p+p^2}\alpha(\mu\wedge J\nu)$, and $p+p^2$ is even. For decomposable $\mu = f_1\wedge\cdots\wedge f_p$ with $f_i\in V_0$, reordering gives $\mu\wedge J\mu = \varepsilon_p\,f_1\wedge Jf_1\wedge\cdots\wedge f_p\wedge Jf_p = \varepsilon_p\,\xi_Q$. If $\mu\ne0$ the $f_i$ are $\mathbb{R}$-independent in the totally real $V_0$, hence $\mathbb{C}$-independent. So with $\xi = f_1\wedge_{\mathbb{C}}\cdots\wedge_{\mathbb{C}}f_p$,
$$
b(\mu,\mu) = \alpha(\xi_Q) = H_\alpha(\xi,\xi) \ge \varepsilon|\xi|^2 = \varepsilon|\mu|^2_{\Lambda^pV_0}\qquad(\mu\in\Lambda^pV_0\text{ decomposable}).
$$

(3) *Self-adjointness.* $\exp(sN)J = J\exp(-sN)$, so invariance of $\alpha$ gives $b(e^{sA}\mu, e^{-sA}\nu) = b(\mu,\nu)$. Equivalently, the derivation induced by $A$ on $\Lambda^pV_0$ is $b$-self-adjoint, and $b(e^{sA}\mu,e^{sA}\mu) = b(e^{2sA}\mu,\mu)$.

(4) *Growth.* Let $D_A$ be the derivation induced by $A$ on $\Lambda^pV_0$, so $\Lambda^p(e^{sA}) = e^{sD_A}$. Since $A\ne0$ and $1\le p\le n-1$, $D_A\ne0$, because the derivation representation of $\mathfrak{gl}(V_0)$ on $\Lambda^pV_0$ is faithful in this range. Decomposables span $\Lambda^pV_0$, so some decomposable $\mu$ has $D_A\mu\ne0$. Let $k\ge1$ be maximal with $D_A^k\mu\ne0$. Then $f(s) = b(e^{2sD_A}\mu,\mu) = \sum_{j\le k}\frac{(2s)^j}{j!}b(D_A^j\mu,\mu)$ is a polynomial of degree at most $k$. On the other hand $e^{sD_A}\mu = (e^{sA}f_1)\wedge\cdots\wedge(e^{sA}f_p)$ is decomposable, and $s^{-k}e^{sD_A}\mu\to D_A^k\mu/k!\ne0$. So $|e^{sD_A}\mu|\ge c'|s|^k$ for $|s|\ge s_0$, with $c' = |D_A^k\mu|/(2\,k!)$. By (2) and (3), $f(s) = b(e^{sD_A}\mu,e^{sD_A}\mu)\ge\varepsilon c'^2s^{2k}$ for $|s|\ge s_0$. Since $2k>k$, this is a contradiction. $\square$

**Corollary 8.1.** If $\mathrm{Hdg}^{2p}(T,\mathbb{Q})$ meets $\operatorname{int}\mathrm{WP}^p$ for some $1\le p\le n-1$, then $G$ is reductive, i.e. $H^1(T,\mathbb{Q})$ is a semisimple Hodge structure.

*Proof.* Let $W$ be the unipotent radical of $G$. $\mathrm{Lie}\,W\subset\mathrm{End}\,V_{\mathbb{Q}}$ is a sub-Hodge structure ($W$ is normal and defined over $\mathbb{Q}$), so it is $\theta$-stable. Write $N\in\mathrm{Lie}\,W_{\mathbb{R}}$ as $N_0+N_1$ with $N_0J = JN_0$ and $N_1J = -JN_1$. Both lie in $\mathrm{Lie}\,W_{\mathbb{R}}$ and are nilpotent. If $N_0\ne0$, then $\exp(\mathbb{R}N_0)$ is a non-compact subgroup of $Z_{G(\mathbb{R})}(J)$, contradicting Theorem A. If $N_1\ne0$, the Hodge class (which is $G$-invariant) contradicts Theorem D. $\square$

## 9. Proof of the Main Theorem

Let $\alpha\in\mathrm{Hdg}^{2p}(T,\mathbb{Q})$ be SP-interior with $1\le p\le n-1$. Since $\operatorname{int}\mathrm{SP}\subset\operatorname{int}\mathrm{WP}$:

1. By Corollary 8.1, $G = \mathrm{Hg}(T)$ is reductive.
2. By Corollary A′, the centre of $G(\mathbb{R})$ is compact and $\theta$ is a Cartan involution on each non-compact simple ideal.
3. Let $\mathfrak{k}_i$ be a compact simple ideal and $K_i$ the corresponding analytic subgroup. $K_i$ is compact (its Lie algebra is compact semisimple), connected, and normalised by $h(U(1))$. If $\theta|_{\mathfrak{k}_i}\ne1$, then $K_i\not\subset Z(J)$ and Theorem C contradicts the hypothesis. So $\theta = 1$ on compact ideals.
4. Theorem B now gives a rational Riemann form. $\square$

**Remarks.** (a) *Easy cases.* $p\in\{1,n-1\}$ is classical: Kodaira on $T$, resp. on $\hat T$ via the duality below. $\mathrm{SP}$ is closed under products, and products of interior classes are interior ($\alpha-\varepsilon\omega^p/p!\in\mathrm{SP}$ implies $\alpha^k - \varepsilon^k(\omega^p/p!)^k\in\mathrm{SP}$). So if $p\mid n-1$, the rational class $\alpha^{(n-1)/p}$ is in $\operatorname{int}\mathrm{SP}^{n-1}$ and the case $p = n-1$ applies. Moreover $\Lambda^{2n-2p}V^*\cong\Lambda^{2p}V\otimes\det V^*$ identifies $\mathrm{Hdg}^{2n-2p}(T,\mathbb{Q})$ with $\mathrm{Hdg}^{2p}(\hat T,\mathbb{Q})$. It maps the generator of $\mathrm{SP}^{n-p}(V)$ attached to a complex $p$-plane $Q\subset V$ to $\pm\xi_Q$, a generator of $\mathrm{SP}^p$ on $\hat T$, with a sign that depends only on $(n,p)$ and orientation conventions. So it identifies $\mathrm{SP}^{n-p}(V)$ with $\pm\mathrm{SP}^p$ of $\hat T$, and rational interior classes correspond to rational interior classes up to sign. Since $T$ is projective iff $\hat T$ is, the cases $(n,p)$ and $(n,n-p)$ are equivalent. Hence the Main Theorem is elementary when $p\mid n-1$ or $(n-p)\mid n-1$, which covers all $n\le3$ and $n=5$. The first genuinely new cases are $(n,p) = (4,2), (6,2), (6,3), (6,4)$, and the sharpness example lives in $(4,2)$. Products do not help for $\mathrm{P}$ or $\mathrm{WP}$.

(b) The proof uses only that $\alpha$ is $G(\mathbb{R})$-invariant and SP-interior. So it shows that the whole real space $\mathrm{Hdg}^{2p}_{\mathbb{R}}$ misses $\operatorname{int}\mathrm{SP}^p$ unless $T$ is projective.

(c) Steps 1–2 use only WP-interiority, and only step 3 needs $\mathrm{SP}$. A non-projective torus with a WP-interior rational Hodge class therefore has semisimple $H^1$, compact centre and Cartan $\theta$ on non-compact factors. All the failure is concentrated in compact factors that rotate $J$, which is exactly what the next example exploits.

## 10. Sharpness: a simple non-projective 4-torus with P-interior rational Hodge classes

**Construction.** Let $F = \mathbb{Q}(\sqrt2)$. The primes $7$ and $17$ split in $F$ ($2\equiv3^2 \bmod 7$ and $2\equiv6^2\bmod17$). Let $D$ be the quaternion algebra over $F$ ramified exactly at both real places, at one prime $v_7\mid7$ and at one prime $v_{17}\mid17$. That is an even number of places, so $D$ exists. For a rational prime $\ell$, $\mathrm{inv}_\ell\,\mathrm{Cor}_{F/\mathbb{Q}}(D) = \sum_{v\mid\ell}\mathrm{inv}_vD$. So $\mathrm{Cor}(D)$ is split at $\infty$ and ramified exactly at $7$ and $17$, and $\mathrm{Cor}(D)\cong M_2(B)$ with $B$ the indefinite quaternion division algebra over $\mathbb{Q}$ of discriminant $119$. Let $G = \mathrm{Res}_{F/\mathbb{Q}}SL_1(D)$ act on $V_{\mathbb{Q}}$, the simple left $M_2(B)$-module ($\dim_{\mathbb{Q}}V_{\mathbb{Q}} = 8$), through the norm map $D^\times\to\mathrm{Cor}(D)^\times$.

Over $\mathbb{R}$, $G(\mathbb{R}) = Sp(1)\times Sp(1)$ and $V_{\mathbb{R}} = A\otimes U$. Here $A = \mathbb{H}$ with $(a,b)\cdot x = a x\bar b$, and $U = \mathbb{R}^2$ is a multiplicity space. Fix a unit imaginary quaternion $u$, put $J = L_u\otimes1\in G(\mathbb{R})$, choose a lattice $\Lambda\subset V_{\mathbb{Q}}$, and set $T_u = (V_{\mathbb{R}},J)/\Lambda$. As $u$ ranges over $S^2$, $\{T_u\}$ is the family of complex structures induced by the flat hyperkähler structure $g_A\otimes h$ on the left $\mathbb{H}$-module $V_{\mathbb{R}}$, i.e. a twistor-type family.

**Proposition 10.1.** For very general $u$, i.e. outside a countable union of nowhere-dense closed subsets of $S^2$:

1. $\mathrm{Hg}(T_u) = G$.
2. $\mathrm{End}^0(T_u) = B^{op}$. $V_{\mathbb{Q}}$ is $G$-irreducible, so $T_u$ is simple.
3. $\mathrm{NS}(T_u)_{\mathbb{Q}} = \mathbb{Q}\,\omega$ with $\omega_{\mathbb{R}} = g_A\otimes\epsilon_U$, and $\omega(x,Jx)$ has signature $(4,4)$. So $T_u$ is not projective.
4. $\mathrm{Hdg}^4(T_u)_{\mathbb{R}} = \mathbb{R}\,\omega^2\oplus(\mathrm{vol}_A\otimes S^4U^*)$, of dimension $6$. Both summands are rational, being isotypic for $B^\times$ acting through $U$.
5. The Kraines form $\Omega_h = \sum_{a\in\{i,j,k\}}\omega_{a,h}^2$ of the flat hyperkähler metric $g_A\otimes h$ ($h\in S^2_+U^*$) lies in $\mathrm{Hdg}^4_{\mathbb{R}}\cap\operatorname{int}\mathrm{P}^2$. Hence $\mathrm{Hdg}^4(T_u,\mathbb{Q})\cap\operatorname{int}\mathrm{P}^2\ne\emptyset$.
6. $T_u$ has no analytic subvarieties of dimension $1$, $2$ or $3$. So no nonzero class in $\mathrm{Hdg}^4(T_u,\mathbb{Q})$ is a $\mathbb{Q}$-combination of analytic cycle classes.

*Proof.* 1. $\mathrm{Hg}\subset G$ because $h(U(1))\subset G(\mathbb{R})$ and $G$ is a $\mathbb{Q}$-group. Suppose $H\subsetneq G$ is a connected $\mathbb{Q}$-subgroup with $L_u\in\mathrm{Lie}\,H(\mathbb{R})$ for all $u$ in a nonempty open set. Then $\mathrm{Lie}\,H(\mathbb{R})\supset\mathfrak{sp}(1)\oplus0$. $\mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ permutes the two factors of $G_{\bar{\mathbb{Q}}} = SL_2\times SL_2$ transitively ($F$ is a quadratic field), so $H_{\bar{\mathbb{Q}}}\supset0\oplus\mathfrak{sl}_2$ as well, and $H = G$. So for each of the countably many proper $H$, the set $\{u: L_u\in\mathrm{Lie}\,H(\mathbb{R})\}$ is closed and nowhere dense, and Baire's theorem finishes the proof.

2. The $\mathbb{Q}$-linear span of $G(\mathbb{Q})$ in $\mathrm{End}(V_{\mathbb{Q}})$ is a central simple algebra of dimension 16 that becomes $M_4(\bar{\mathbb{Q}})\otimes 1$ over $\bar{\mathbb{Q}}$, namely $\mathrm{Cor}(D)\cong M_2(B)$. Its commutant is $B^{op}$, a division algebra, and $V_{\mathbb{Q}}$ is a simple $M_2(B)$-module.

3. $\Lambda^2(A\otimes U) = \Lambda^2A\otimes S^2U\oplus S^2A\otimes\Lambda^2U$. Here $\Lambda^2A = \mathfrak{sp}(1)_L\oplus\mathfrak{sp}(1)_R$ has no invariants and $(S^2A)^{SO(4)} = \mathbb{R}g_A$. The form $(x,y)\mapsto\omega(x,Jy)$ equals $g_A(\cdot,L_u\cdot)\otimes\epsilon$, a tensor product of two non-degenerate alternating forms, so it has split signature $(4,4)$. A polarisation would be a class in $\mathrm{NS}_{\mathbb{R}}$ whose associated form is definite.

4. By Schur–Weyl duality, $\Lambda^4(A\otimes U) = \bigoplus_{|\lambda|=4}S_\lambda A\otimes S_{\lambda'}U$ with $\lambda'$ of at most 2 rows. The $SO(4)$-invariants come from $\Lambda^4A\otimes S^4U$ (dimension 5) and $S_{(2,2)}A\otimes S_{(2,2)}U$ (dimension 1, spanned by $\omega^2$). $S_{(2,1,1)}A\cong\Lambda^2\oplus S^2_0$ has none. $B^{op}$ acts through $GL(U)$, with character $\mathrm{Nm}^2$ on $\omega^2$ and $S^4\otimes\det^{-2}$ on the 5-dimensional piece, which is absolutely irreducible.

*Rationality.* Since $G$ is a $\mathbb{Q}$-group, $\mathrm{NS}(T_u)_{\mathbb{Q}} = (\Lambda^2V_{\mathbb{Q}}^*)^G$ and $\mathrm{Hdg}^4(T_u,\mathbb{Q}) = (\Lambda^4V_{\mathbb{Q}}^*)^G$ are $\mathbb{Q}$-forms of the real spaces above, of dimensions $1$ and $6$. So $\omega$ can be taken rational (we rescale it to be integral on $\Lambda$), and $\omega^2$ is rational. The group $SL_1(B^{op})$ is a $\mathbb{Q}$-group commuting with $G$, so it acts on $(\Lambda^4V_{\mathbb{Q}}^*)^G$. Its Casimir operator $\mathcal{C}$, formed from a $\mathbb{Q}$-basis of the trace-zero part $B^{op}_0$ and the dual basis for the reduced trace form, is a $\mathbb{Q}$-linear endomorphism. It kills $\omega^2$ (trivial representation) and acts by a nonzero scalar on the $S^4$-piece. Hence $K_5 := \mathrm{im}\,\mathcal{C} = \ker(\mathcal{C}-c)$ is defined over $\mathbb{Q}$, and $\mathrm{Hdg}^4(T_u,\mathbb{Q}) = \mathbb{Q}\omega^2\oplus K_5$. *Lattice.* Any lattice $\Lambda\subset V_{\mathbb{Q}}$ works. All statements are isogeny-invariant, and $\mathcal{O} := \{b\in B^{op} : b\Lambda\subset\Lambda\}$ is an order of $B^{op}$ that acts on $T_u$ by isogenies (used in Proposition 12.1).

5. $\Omega_h$ is invariant under $Sp(1)_L$, which rotates the hyperkähler triple, and under $Sp(1)_R$, which commutes with every $L_a$ and preserves $g_A$. For $I = L_u$, $\Omega_h = \omega_I^2+\sigma\wedge\bar\sigma$ with $\sigma = \omega_J+i\omega_K$ of type $(2,0)$. On $\Lambda^2T^{1,0}$ the hermitian form of $\omega_I^2$ is twice the induced metric, hence positive definite, and that of $\sigma\wedge\bar\sigma$ is the rank-one positive semidefinite form $\sigma\sigma^*$. Their sum is positive definite. Numerically its eigenvalues are $2$ (multiplicity 5) and $10$. $\operatorname{int}\mathrm{P}^2\cap\mathrm{Hdg}^4_{\mathbb{R}}$ is a nonempty open cone in $\mathrm{Hdg}^4_{\mathbb{R}}$, so it contains rational points.

6. Let $Z\subsetneq T$ be an irreducible analytic subvariety of positive dimension. By Ueno's structure theorem [20], $Z$ is a fibre bundle over a variety of general type whose fibre is a translate of a subtorus. $T$ is simple, so the fibre is a point and $Z$ is of general type, hence Moishezon. Let $\tilde Z\to Z$ be a resolution. The image of $\tilde Z\to T$ generates a subtorus, which is $T$ because $T$ is simple. This map factors through $\mathrm{Alb}(\tilde Z)$, an abelian variety, so $T$ would be a quotient of an abelian variety, which is impossible. $\square$

**Consistency with Theorem C.** Here $K = Sp(1)_L\times1\not\subset Z(J)$, so $\mathrm{Hdg}^4_{\mathbb{R}}\cap\operatorname{int}\mathrm{SP}^2 = \emptyset$. The Kraines class sits exactly on $\partial\mathrm{SP}$: $\sigma\wedge\bar\sigma$ is maximally entangled in $\Lambda^2\mathbb{C}^4$, and its Uhlmann concurrence margin is $0$ (Section 13). The Hodge classes here are P-interior but cannot be SP-interior. The gap between Demailly's two cones is exactly where cycle-type positivity fails.

**Weil-type structure and why the Cor symmetry is needed.** Let $b\in B$ with $b^2 = -d<0$ and $E = \mathbb{Q}(b)$. Since $B^{op}$ acts on $V$ through $U$, $E$ acts by $1\otimes J_U$ for a complex structure $J_U$ on $U$, and this commutes with $J$. Write $V_+ = A_{\mathbb{C}}\otimes U^+$ for the $(+i)$-eigenspace of $E$ on $V_{\mathbb{C}}$. Then $\dim V_+\cap V^{1,0} = \dim V_+\cap V^{0,1} = 2$, and $H(x,y) = i\,\omega(x,\bar y)$ restricts to $g_A\otimes(i\epsilon|_{U^+})$ on $V_+$, which is definite. So $T_u$ is a Weil torus of *compact type* for every imaginary quadratic $E\subset B$ (the hermitian form is definite, not of signature $(2,2)$ as for polarised abelian fourfolds of Weil type). The $E$-Weil classes, i.e. the generators of $\Lambda^4_{\mathbb{C}}V_+^*$, are $v_{\ell^4}$ and $\bar v_{\ell^4}$ with $\ell = x+\tau y$ the $J_U$-linear form on $U$, $\tau$ in the upper half plane. The fourth powers $\ell^4$ span $S^4U^*_{\mathbb{C}}$ as $\tau$ runs over the dense set of CM points $\tau$ attached to embeddings $E\hookrightarrow B$. So $K_5\otimes\mathbb{C}$ is spanned by Weil classes, each relative to some $E\subset B$ (supplement, `t29.py`). The positivity in Proposition 10.1(5) does not come from any single $E$:

**Proposition 10.2.** Let $T$ be a complex 4-torus, $E\subset\mathrm{End}^0(T)$ imaginary quadratic, with $T$ of Weil type relative to $E$ and with definite $E$-hermitian form $H = i\,\omega(\cdot,\bar\cdot)$ on $V_+$, where $\omega$ is a real $(1,1)$-form with $\omega(ex,ey) = \mathrm{N}_{E/\mathbb{Q}}(e)\,\omega(x,y)$ for $e\in E$ (for $T_u$: $\omega$ spans $\mathrm{NS}$, and $b^*\omega = \mathrm{Nrd}(b)\,\omega$). Let $W_E\subset\Lambda^4V_{\mathbb{R}}^*$ be the real span of the $E$-Weil classes. Then $(\mathbb{R}\omega^2\oplus W_E)\cap\mathrm{WP}^2 = \{0\}$. In particular, if $\mathrm{Hg}(T) = SU(H)$, so that $\mathrm{Hdg}^4(T)_{\mathbb{R}} = \mathbb{R}\omega^2\oplus W_E$, then $\mathrm{Hdg}^4(T)_{\mathbb{R}}\cap\mathrm{WP}^2 = \{0\}$. On $T_u$, each 3-dimensional subspace $\mathbb{R}\omega^2\oplus W_E$ of $\mathrm{Hdg}^4_{\mathbb{R}}$ meets $\mathrm{WP}^2$ only in $0$.

*Proof.* Put $W = V^{1,0}\cap V_+$ and $W' = V^{1,0}\cap V_-$, so $V^{1,0} = W\oplus W'$ and $V_+ = W\oplus\overline{W'}$. Let $h(x,y) = i\,\omega(x,\bar y)$ on $V^{1,0}$. If $e\in E$ generates $E$ with $e^2 = -d$, it acts by $\pm i\sqrt d$ on $V_\pm$, and $\omega(ex,ey) = d\,\omega(x,y)$ forces $\omega|_{V_+\times V_+} = 0 = \omega|_{V_-\times V_-}$. Since $\overline{V_-} = V_+$, this gives $W\perp_hW'$. $h = H$ on $W$, and $h(y',y') = i\,\omega(y',\bar y') = -H(\bar y',\bar y')$ for $y'\in W'$, so $h$ is definite of one sign on $W$ and of the opposite sign on $W'$. Changing the sign of $\omega$ if necessary, take $h>0$ on $W$ and $h<0$ on $W'$. For a decomposable $\xi = x\wedge y$ we have $H_{\omega^2/2}(\xi,\xi) = h(x,x)h(y,y)-|h(x,y)|^2$. This is $>0$ for $\xi\in\Lambda^2W\setminus0$ and $<0$ for $\xi = x\wedge x'$ with $x\in W$, $x'\in W'$ both nonzero. A Weil form $w\in\Lambda^4V_+^*$ only pairs $\Lambda^2W$ with $\Lambda^2\overline{W'}$. So $H_w$ is supported on $\Lambda^2W\times\Lambda^2W'$ and its transpose, and vanishes on $\xi\in\Lambda^2W$ and on $\xi = x\wedge x'$. Let $\alpha = c\,\omega^2+w\in\mathrm{WP}^2$. Testing on $x\wedge x'$ gives $c\le0$, and testing on $\Lambda^2W$ gives $c\ge0$, so $c = 0$. If $w\ne0$, take $\xi = (x_1+t x_1')\wedge(x_2+s x_2')$ with $\{x_i\}$, $\{x'_i\}$ bases of $W$, $W'$. Then $H_w(\xi,\xi) = 2\,\mathrm{Re}(\overline{ts}\,\kappa)$ with $\kappa = H_w(x_1\wedge x_2,x_1'\wedge x_2')\ne0$, and choosing the phase of $ts$ makes it negative. So $w = 0$. If $\mathrm{Hg} = SU(H)$, then $(\Lambda^4V^*_{\mathbb{R}})^{SU(4)}$ is spanned by $\omega^2$ (from $\Lambda^2V_+^*\otimes\Lambda^2V_-^*$) and the real and imaginary parts of $\det V_+^*$. For $T_u$, the hypotheses hold for every $E\subset B$ by the paragraph above. $\square$

Numerically (`t30.py`, random $J$ in the compact period domain $\mathrm{Gr}(2,4)$), $H_{\omega^2}$ has signature $(2,4)$ and the best P- and WP-margins over $\mathrm{Hdg}^4_{\mathbb{R}}$ are $-0.40$ and $-1.12$. Such tori are non-projective by Theorem C with $p=1$. So compact-type Weil 4-tori with the generic Hodge group $SU(H)$ carry no nonzero weakly positive Hodge class in degree 4. On $T_u$ the Kraines class escapes Proposition 10.2 because its $K_5$-part $c\,\mathrm{vol}_A\otimes h^2$ ($c\ne0$) lies in no $W_E$. For $E\subset B$ with $J_U$ orthogonal for $h_E\in S^2_+U^*$, $W_E$ consists of $v_f$ with $f$ of $SO(h_E)$-weight $\pm4$, whereas the weight-$0$ part of $h^2$ is its $SO(h_E)$-average, a positive multiple of $h_E^2$. The extra Hodge classes that the smaller group $G\subset SU(H)$ creates are what make the sharpness example work.

## 11. The same mechanism on hyperkähler manifolds

**Theorem 11.1.** Let $(X,I)$ be a compact hyperkähler manifold of complex dimension $2n\ge4$, and $1\le p\le 2n-1$. If $\alpha\in H^{2p}(X,\mathbb{R})$ is invariant under the $SU(2)$-action on cohomology induced by some hyperkähler metric on $(X,I)$, then $\alpha$ is not SP-interior on $(X,I)$.

*Proof.* Take $J' = J$ from the quaternionic triple. It is $g$-orthogonal, $\omega_J$ is parallel (so $\omega_J^q$ is closed), and $J\ne\pm I$ everywhere. The $SU(2)$-action on harmonic forms is by isometries, preserves the top-degree pairing and $\alpha_{\mathrm{harm}}$, and sends $\omega_I^q$ to $\omega_J^q$. So $\int\alpha\,\omega_J^q = \int\alpha\,\omega_I^q$, and Lemma 7.1 gives a contradiction. $\square$

**Corollaries.** (i) The Chern classes $c_{2k}(X)$ with $0<2k<2n$ are $SU(2)$-invariant, being of Hodge type for every induced complex structure. So they are never SP-interior, even on projective $X$. For example, on $X = K3^{[2]}$, $\int c_2\,a^2 = 30\,q(a)$ and $q(\omega_I) = q(\mathrm{Re}\,\sigma)$. (ii) Suppose every Hodge class of $X$ is $SU(2)$-invariant. This holds for all but countably many complex structures in a twistor family (Verbitsky [10]). It also holds for $X$ very general in its moduli, since then the Mumford–Tate algebra acting on $H^*(X)$ through the Looijenga–Lunts–Verbitsky action is $\mathfrak{so}(H^2(X,\mathbb{Q}),q)$, which contains the $\mathfrak{su}(2)$ of every hyperkähler metric. Then no rational Hodge class of degree $2,\dots,4n-2$ on $X$ is SP-interior. This matches the torus picture: an SP-interior Hodge class has to break every hidden rotation of the complex structure.

## 12. The Chern-class form of the question on the sharpness example

Voisin's Kähler counterexamples [2] also exclude Chern classes of coherent sheaves. For the torus $T_u$ of Proposition 10.1 we can only reduce this question. Subsection 12.A contains proved statements only. Everything conditional or open is in 12.B.

### 12.A Proved statements

**Proposition 12.1.** Let $S\subset\mathrm{Hdg}^4(T_u,\mathbb{Q})$ be the $\mathbb{Q}$-span of $\mathrm{ch}_2(\mathcal{F})$ over coherent sheaves $\mathcal{F}$. Then $S = \mathbb{Q}\,\omega^2$ or $S = \mathrm{Hdg}^4(T_u,\mathbb{Q})$.

*Proof.* Isogenies $b\in\mathcal{O}\setminus0$ act on $T_u$, $b^*\mathcal{F}$ is coherent, and $\mathrm{ch}(b^*\mathcal{F}) = b^*\mathrm{ch}(\mathcal{F})$. The two $B^\times$-isotypic pieces $\mathbb{Q}\,\omega^2$ and $K_5$ (the rational 5-dimensional summand) are absolutely irreducible and non-isomorphic, and $B^\times(\mathbb{Q})$ is Zariski dense in $GL_1(B)$. So the span of the orbit of $v = v_0+v_5$ contains $K_5$ whenever $v_5\ne0$. Line bundles give $\omega^2$. $\square$

*Reduction to stable reflexive sheaves.* $T_u$ contains no curves, surfaces or divisors. Hence torsion sheaves are supported in dimension $0$ (with $\mathrm{ch}_2 = 0$), passing to reflexive hulls does not change $\mathrm{ch}_2$, and the Jordan–Hölder factors with respect to any Kähler class are stable reflexive sheaves with $c_1\in\mathbb{Q}\omega$.

The relevant positivity lives in the multiplicity space $U$. For $f\in S^4U^*$ write $v_f\in K_5\otimes\mathbb{R}$ for the class $v_f(a_1\otimes u_1,\dots,a_4\otimes u_4) = \mathrm{vol}_A(a_1,\dots,a_4)\,\tilde f(u_1,\dots,u_4)$, with $\tilde f$ the polarisation of $f$. For a real linear form $\ell$ on $U$ the map $\pi_\ell = 1\otimes\ell: A\otimes U\to A$ is $\mathbb{C}$-linear, and $v_{\ell^4} = \pi_\ell^*\mathrm{vol}_A$ is strongly positive. (The maps $\pi_\ell$ are not defined over $\mathbb{Q}$, so they do not induce morphisms of tori.) For $h\in S^2_+U^*$ let $\omega_{I,h}$ be the Kähler form of $g_A\otimes h$ for $I = J$.

**Proposition 12.2.** Let $u$ be very general and $E$ an $\omega_{I,h}$-stable vector bundle on $T_u$ for some $h$. Then the $K_5$-component of $\mathrm{ch}_2(E)$ equals $-v_{p_E}$ for a nonnegative binary quartic $p_E$ on $U$, and $p_E = 0$ iff $E$ is projectively flat.

**Corollary 12.3 (conditional on a seed).** *If* some vector bundle $E$ as in Proposition 12.2 is not projectively flat, then every class in $\mathrm{Hdg}^4(T_u,\mathbb{Q})$ is a $\mathbb{Q}$-combination of classes $\mathrm{ch}_2$ of vector bundles, and no nonzero such class is a combination of analytic cycles. We do not know whether such an $E$ exists.

*Proof of Corollary 12.3.* Apply Proposition 12.2, then Proposition 12.1 (the isogenies $b^*E$ are vector bundles), then Proposition 10.1(6). $\square$

*Proof.* $c_1(E)\in\mathrm{NS}_{\mathbb{Q}} = \mathbb{Q}\omega$. Since $\mathrm{Hg}(T_u) = G$, $c_2(E)$ is $G(\mathbb{R})$-invariant, and in particular invariant under $Sp(1)_L$, which is the $SU(2)$ induced on cohomology by the hyperkähler metric $g_A\otimes h$. By Verbitsky [10] the Hermite–Einstein connection of $E$ is hyperholomorphic: its curvature $\Theta$ takes values in the $Sp(1)_L$-invariant 2-forms tensored with $\mathfrak{u}(E)$. These invariant forms are $\bigoplus_{a=1}^3\alpha_a\otimes S^2U^*\oplus\mathbb{R}\omega$, where $\alpha_a = g_A(R_a\cdot,\cdot)$ and $R_a$ is right multiplication by $i,j,k$. So
$$
\Theta = \sum_a \alpha_a\otimes\Theta_a + \omega\otimes\Theta_0,
$$
with $\Theta_a$ a section of $S^2U^*\otimes\mathfrak{u}(E)$; write $\Theta_a(x)\in\mathfrak{u}(E)$ for its value at $x\in U$. By $GL(A)\times GL(U)$-equivariance, the $K_5$-component of $(\alpha_a\otimes s)\wedge(\alpha_b\otimes t)$ is $c_{ab}\,v_{st}$. A direct computation (supplement, `t28.py`) gives $c_{ab} = -2\delta_{ab}$, and shows that $\omega\wedge(\alpha_a\otimes s)$ and $\omega^2$ have no $K_5$-component. On a torus, the class of a closed form is that of its translation average. Since $\mathrm{ch}_2 = -\frac{1}{8\pi^2}\mathrm{tr}(\Theta\wedge\Theta)$,
$$
K_5(\mathrm{ch}_2E) = \frac{1}{4\pi^2}\,v_{q},\qquad q(x) = \operatorname{avg}_{T}\sum_a\mathrm{tr}\big(\Theta_a(x)^2\big),
$$
and $p_E := -q/4\pi^2\ge0$ because $\mathrm{tr}(M^2) = -|M|^2$ on $\mathfrak{u}(r)$. Moreover $p_E\equiv0$ iff all $\Theta_a$ vanish identically, i.e. $\Theta = \omega\otimes\Theta_0$. In that case the Bianchi identity gives $\omega\wedge\nabla\Theta_0 = 0$, so $\nabla\Theta_0 = 0$ because $\omega$ is nondegenerate and $\omega\wedge$ is injective on 1-forms in real dimension 8. Stable bundles are simple, so $\Theta_0$ is scalar and $E$ is projectively flat. Conversely, projectively flat bundles have $\Theta = \omega\otimes\Theta_0$ with $\Theta_0$ scalar. $\square$

### 12.B Open questions and heuristics (no claims)

*Which case of Proposition 12.1 holds is open.* Natural constructions do not help. Line bundles and simple semi-homogeneous bundles are projectively flat, so their $\mathrm{ch}$ lies in $\mathbb{Q}[c_1] = \mathbb{Q}[\omega]$. Tensor products, extensions, isogenies and Fourier–Mukai along the Poincaré bundle all preserve the subgroup with vanishing $K_5$-part (the cohomological Fourier–Mukai map is $G$-equivariant). The question needs a genuinely new "seed" object. One option is a hyperholomorphic sheaf on a CM fibre of the family, deformed along it as in Markman's method [13, 14]. By Section 10 (Weil-type structure), $T_u$ is a compact-type Weil torus for every $E\subset B$. Markman's constructions concern the polarised (indefinite) component of the Weil period domain, and we do not know whether they extend to the compact component.

*Bogomolov does not decide it.* On Weil-type tori, Voisin [2] excludes Chern classes using the Bogomolov inequality. On $T_u$ the same inequality only constrains the sign. Bogomolov–Gieseker (Bando–Siu) for the Jordan–Hölder factors gives $\int\mathrm{ch}_2(\mathcal{F})\,\kappa^2\le0$ for every coherent $\mathcal{F}$ and every Kähler class $\kappa$ with $\int\omega^2\kappa^2\le0$. Every class $x\,\omega^2-\sum_kv_{\ell_k^4}$ with $x\ge0$ satisfies these inequalities, because $v_{\ell^4}$ is strongly positive. These classes form a convex cone that spans $\mathrm{Hdg}^4_{\mathbb{R}}$ (fourth powers span $S^4U^*$), so it has nonempty interior. The inequalities alone therefore cannot force the $K_5$-part of $\mathrm{ch}_2$ to vanish (supplement, `t27.py`).

*Sign heuristics.* The sign in Proposition 12.2 is the one geometry predicts. If $\pi_\ell$ induced a morphism of tori, the ideal sheaf of a fibre $Z$ would have $\mathrm{ch}_2(\mathcal{I}_Z) = -v_{\ell^4}$. The nonnegative quartics form a strictly larger cone than the sums of fourth powers.

*Rank-2 seeds on CM fibres fail at the class level (sketch).* Consider the CM fibre $u_0 = i$. Here $L_iR_i$ splits $V_{\mathbb{R}} = X_1\oplus X_2$ ($X_1 = \mathbb{C}_{1,i}\otimes U$, $X_2 = \mathbb{C}_{j,k}\otimes U$), the Hodge group acts on each $X_a$ by a scalar $U(1)$, and $\mathrm{NS}(T_{u_0})_{\mathbb{R}} = \mathrm{NS}(X_1)\oplus\mathrm{NS}(X_2)$ has dimension 8. Let $E$ be a rank-2 bundle with $c_1(E)\in\mathbb{Q}\,\omega$ and $Sp(1)_L$-invariant $\mathrm{ch}(E)$. Suppose $E$ is (a) an extension of two line bundles, or (b) given by the Serre construction along translates of an abelian subsurface (necessarily of the form $L_1\oplus L_2$, $L_a\subset X_a$). A case analysis of the components of $\mathrm{ch}_2$ in $\mathrm{NS}(X_1)\otimes\mathrm{NS}(X_2)\oplus\mathbb{R}\,\mathrm{vol}_1\oplus\mathbb{R}\,\mathrm{vol}_2$ then gives one of two outcomes. Either $K_5(\mathrm{ch}_2E) = 0$, or the data are pullbacks along $\pi_\ell$. Pullbacks along $\pi_\ell$ are excluded because their kernels $A\otimes\ker\ell$ are quaternionic, and a rational such kernel would be a subtorus of the simple very general $T_u$. Numerical searches agree (supplement, `t36b.py`). The only solutions with $K_5\neq0$ have $Z = A\otimes\ker\ell$. A seed therefore needs rank at least 3, or a Serre locus that is not a subtorus, whereas the class-level problem itself is unobstructed by Bogomolov (above).

*Reflexive sheaves.* All Hodge classes are $Sp(1)_L$-invariant, so by Verbitsky [11] the stable reflexive Jordan–Hölder factors carry admissible hyperholomorphic connections. Extending Proposition 12.2 to stable reflexive sheaves would make Corollary 12.3 an equivalence. Their singular sets are finite here, but we have not checked Chern–Weil for admissible connections against arbitrary constant 4-forms.

### 12.C Analogues over cubic and quintic fields

**Remark 12.4 (a cubic analogue: non-analytic classes that specialise to Weil classes).** Replace $F$ by a totally real cubic field and $D$ by a quaternion algebra over $F$ ramified at the three real places, and for parity at an odd number of finite places. Then $\mathrm{Cor}(D)\cong M_4(B)$ with $B$ a definite quaternion algebra over $\mathbb{Q}$. $V_{\mathbb{Q}} = B^4$ gives 8-dimensional tori $T_u$ with $G(\mathbb{R}) = Sp(1)^3$ and $J$ in the first factor. For very general $u$:

- $T_u$ is simple. The commutant of $\mathrm{Cor}(D)$ is $B^{op}$, and the Galois argument of 10.1(1) uses transitivity on the three real places.
- $T_u$ is non-projective, by Theorem C with $p=1$.
- $\dim\mathrm{NS} = 3$ and $\dim\mathrm{Hdg}^4 = 8$, while the products $\mathrm{NS}\cdot\mathrm{NS}$ span only 6 dimensions. This is an exact weight computation (supplement, `t21.py`, `t22.py`).

At a CM point the Mumford–Tate group is $\mathrm{Res}_{F/\mathbb{Q}}U(1)_{K/F}$ for a CM quadratic extension $K = F(\sqrt\delta)$, with characters $\epsilon\in\{\pm1\}^3$. The fibre is isogenous to $A^*\times A^*$, where $A^*$ is a CM fourfold with CM by the reflex field $K^*$ of degree 8.

- The CM type $\{\epsilon_1 = +1\}$ has signature $(2,2)$ over the imaginary quadratic field $E = \mathbb{Q}(\sqrt{N_{F/\mathbb{Q}}(\delta)})\subset K^*$, which corresponds to the character $\epsilon\mapsto\epsilon_1\epsilon_2\epsilon_3$. So $A^*$ is of Weil type.
- A zero-sum set of four cube vertices is either two antipodal pairs (a product of divisor classes) or one of the two regular tetrahedra, and the tetrahedra are the two $E$-blocks.
- Pullbacks of the Weil classes of $A^*$ along the maps $(\alpha,\beta): A^{*2}\to A^*$ with $\alpha,\beta\in K^*$ span all 32 tetrahedral weight monomials. Distinct embeddings $\sigma_\epsilon$ are independent coordinates on $K^*\otimes\mathbb{C}$.
- The generic classes not in $\mathrm{NS}\cdot\mathrm{NS}$ have tetrahedral components of rank 2 at the CM point.

So along $\{T_u\}$, non-analytic Hodge classes on simple non-algebraic tori specialise, modulo $\mathrm{NS}\cdot\mathrm{NS}$, to Weil classes on a CM abelian fourfold, which are algebraic by Markman's theorem [13]. For quadratic $F$ (Section 10), $E$ is real and the CM-fibre classes are all products of divisors. This family is a natural test case for running Markman's hyperholomorphic mechanism in reverse to produce Chern classes on $T_u$. We prove nothing about that here. For a totally real quintic $F$ (now $\dim_{\mathbb{C}}T_u = 32$), the same weight computation restricted to the $\mathfrak{sl}(M)$-invariant part (supplement, `t23.py`) gives 11 generic classes, whose exceptional CM components have rank 10. Every zero-sum set of four vertices of $\{\pm1\}^d$ is a coset of a Klein four-subgroup $H$, and it is exceptional iff $-1\notin H$. For $d=5$ no Klein four-subgroup is invariant under a transitive permutation group, so these CM classes are not Weil classes relative to any subfield of the reflex field. We have not determined whether HC is known for them.

## 13. Limitations and reproducibility

**Limitations.**

- The Main Theorem does not decide whether $\operatorname{int}\mathrm{SP}$-classes on abelian varieties are algebraic; that is HC itself.
- The sharpness example concerns the cycle form of the question. Its Chern-class form is open. By Corollary 12.3, a single stable vector bundle on $T_u$ that is not projectively flat would make every rational Hodge class a combination of Chern characters.
- The cone $\mathrm{P}$ in Proposition 10.1 is shown to fail, but we do not characterise which non-projective tori carry P- or WP-interior rational classes beyond the necessary conditions of Remark 9(c) and the negative result of Proposition 10.2 for compact-type Weil 4-tori with Hodge group $SU(H)$.
- Remark 12.4 is supported by an exact weight computation and a hand argument at CM points. It is a remark, not a theorem.

**Reproducibility.** The supplement contains Python 3 scripts (numpy, scipy; CPU, each under a few minutes) for the numerical consistency checks. None of the proofs depends on them.

- `invforms.py`, `t14.py`: invariant forms as null spaces of the derivation action. Cor type gives $\dim\mathrm{NS} = 1$ and $\dim\mathrm{Hdg}^4 = 6$, and the Kraines form has hermitian eigenvalues $(2,2,2,2,2,10)$.
- `sp_test.py`, `t15.py`: SP test on $\Lambda^2\mathbb{C}^4$. $x\mapsto x\wedge x$ is a nondegenerate quadratic form, and $x$ is decomposable iff $x\wedge x = 0$. In a magic basis, separability of a fermionic state $H$ is decided by Uhlmann's convex-roof concurrence $C(H) = \max(0,\lambda_1-\lambda_2-\cdots-\lambda_6)$ [16, 17], where $\lambda_i$ are the decreasing eigenvalues of $(\sqrt H\bar H\sqrt H)^{1/2}$. We use the margin $\lambda_2+\cdots+\lambda_6-\lambda_1>0$ (with $H>0$) as the interior test. It was validated on decomposable $+\,\varepsilon I$, on $I$, and on an isotropic family (threshold $0.4$). Cor type: the maximal margin over $\mathrm{Hdg}^4_{\mathbb{R}}$ is $0$ (to $1.6\cdot10^{-13}$).
- `t16.py`–`t19.py`: Monte-Carlo $K$-averaged certificate of Theorem C, which is weakly positive and orthogonal to $\mathrm{Hdg}^4$.
- `t13.py`: $Sp(1)\times SL_2(\mathbb{R})$ with $J$ in the compact factor has no WP-interior Hodge class (consistency with Theorem A).
- `t20.py`: rank-one antilinear nilpotent $N$; the invariant $(2,2)$-forms have maximal weak minimum $-0.039<0$ (consistency with Theorem D).
- `t27.py`, `t28.py`, `t28b.py`: exterior-algebra computations for Section 12. $c_{ab} = -2\delta_{ab}$ (residual $<10^{-16}$), $\omega$-terms have no $K_5$-component, and the forms $\alpha_a\otimes s$ are $Sp(1)_L$-invariant.
- `t29.py`: Weil-type structure of $T_u$ (Section 10). For $E = \mathbb{Q}(J_U)$, $\det V_+^*$ equals $v_{\ell^4}$, $\ell = x+\tau y$, with residual $10^{-16}$, and $H$ is definite on $V_+$.
- `t30.py`: random compact-type Weil 4-torus with Hodge group $SU(H)$ (Proposition 10.2). $H_{\omega^2}$ has signature $(2,4)$, and the best P- and WP-margins over $\mathrm{Hdg}^4_{\mathbb{R}}$ are $-0.40$ and $-1.12$.
- `t33.py`, `t34.py`, `t35.py`, `t36b.py`: the CM fibre $u_0 = i$ (Section 12.B). $\dim\mathrm{NS} = 8$ and $\dim\mathrm{Hdg}^4 = 18$. Serre-type rank-2 data with invariant $\mathrm{ch}_2$ have $K_5\neq0$ only for $Z = A\otimes\ker\ell$ (40 of 40 solutions classified). `t33.py` also uses cvxpy.
- `t21.py`, `t22.py`, `t23.py`: the cubic and quintic analogues of Remark 12.4 (`python3 scratch/t23.py 3`, resp. `5`; the latter takes about a minute).

## References

[1] S. Zucker. The Hodge conjecture for cubic fourfolds. Compositio Math. 34 (1977), 199–209. (Contains the example of a complex torus with non-analytic Hodge classes.)

[2] C. Voisin. A counterexample to the Hodge conjecture extended to Kähler varieties. Int. Math. Res. Not. 2002, no. 20, 1057–1075. https://doi.org/10.1155/S1073792802111135

[3] J.-P. Demailly. Complex analytic and differential geometry. Book, Institut Fourier, 2012. https://www-fourier.ujf-grenoble.fr/~demailly/manuscripts/agbook.pdf

[4] F. Babaee, J. Huh. A tropical approach to a generalized Hodge conjecture for positive currents. Duke Math. J. 166 (2017). arXiv:1502.00299

[5] O. Debarre, L. Ein, R. Lazarsfeld, C. Voisin. Pseudoeffective and nef classes on abelian varieties. Compositio Math. 147 (2011). arXiv:1003.3183

[6] M. L. Michelsohn. On the existence of special metrics in complex geometry. Acta Math. 149 (1982), 261–295.

[7] F. Oort, Yu. G. Zarhin. Endomorphism algebras of complex tori. Math. Ann. 303 (1995), 11–29.

[8] T. Bandman, Yu. G. Zarhin. Simple complex tori of algebraic dimension 0. arXiv:2106.10308

[9] Yu. G. Zarhin. Endomorphism algebras and automorphism groups of certain complex tori. arXiv:2301.01573

[10] M. Verbitsky. Hyperholomorphic bundles over a hyperkähler manifold. J. Algebraic Geom. 5 (1996). arXiv:alg-geom/9307008

[11] M. Verbitsky. Hyperholomorphic sheaves and new examples of hyperkähler manifolds. arXiv:alg-geom/9712012

[12] M. Verbitsky. Coherent sheaves on generic compact tori. arXiv:math/0310329

[13] E. Markman. Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds. arXiv:2502.03415

[14] E. Markman. Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication. arXiv:2509.23079

[15] E. Markman. Secant sheaves and Weil classes on abelian varieties. arXiv:2509.23403

[16] A. Uhlmann. Fidelity and concurrence of conjugated states. Phys. Rev. A 62 (2000), 032307.

[17] J. Schliemann, J. I. Cirac, M. Kuś, M. Lewenstein, D. Loss. Quantum correlations in two-fermion systems. Phys. Rev. A 64 (2001), 022303.

[18] P. Deligne. Travaux de Shimura. Séminaire Bourbaki 389 (1971), LNM 244.

[19] J. S. Milne. Introduction to Shimura varieties. 2004/2017. https://www.jmilne.org/math/xnotes/svi.pdf

[20] K. Ueno. Classification theory of algebraic varieties and compact complex spaces. LNM 439, Springer, 1975.

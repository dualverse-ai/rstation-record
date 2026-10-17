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
- **Propositions 12.1, 12.2 and Remark 12.3.** A Chern-class dichotomy on the sharpness example. Chern classes of stable bundles there have nonnegative $K_5$-parts, which vanish exactly for projectively flat bundles. A cubic analogue whose non-analytic classes specialise to Weil classes at CM points.

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

Then $\mathrm{SP}^p \subset \mathrm{P}^p \subset \mathrm{WP}^p$, and $\mathrm{SP}^p$ and $\mathrm{WP}^q$ are dual under the wedge pairing [3]. All three cones coincide for $p \in \{1, n-1\}$. For $n=4$, $p=2$ they differ. $\mathrm{SP}^2$ can be detected on $\Lambda^2\mathbb{C}^4$ by Uhlmann's fermionic concurrence [16, 17] (Section 13). For a compact complex manifold $X$, a class in $H^{p,p}(X,\mathbb{R})$ is called *SP-interior* if a smooth closed form that is strictly strongly positive at every point represents it (similarly for $\mathrm{P}$, $\mathrm{WP}$). On a torus this agrees with the linear-algebra notion for the constant representative. Averaging a representative over translations gives the constant harmonic form, and each cone is convex and translation-invariant.

## 4. Hodge-group setup

Let $T = V_{\mathbb{R}}/\Lambda$, $V_{\mathbb{Q}} = \Lambda\otimes\mathbb{Q}$, with complex structure $J$, and let $h: U(1) \to GL(V_{\mathbb{R}})$, $h(e^{i\theta}) = \cos\theta + \sin\theta\, J$. The *Hodge group* $G = \mathrm{Hg}(T)$ is the smallest $\mathbb{Q}$-subgroup of $GL(V_{\mathbb{Q}})$ whose real points contain $h(U(1))$. It need not be reductive when $H^1$ is not semisimple. A rational class $\alpha \in \Lambda^{2p}V_{\mathbb{Q}}^*$ is Hodge iff it is $h(U(1))$-invariant, iff it is $G$-invariant (its stabiliser is a $\mathbb{Q}$-group containing $h(U(1))$). Hence $\mathrm{Hdg}^{2p}(T)_{\mathbb{R}} = (\Lambda^{2p}V_{\mathbb{R}}^*)^{G(\mathbb{R})}$, and every $G(\mathbb{R})$-invariant form is of type $(p,p)$. Write $\theta = \mathrm{Ad}\,J$, an involution of $\mathfrak{g}_{\mathbb{R}} = \mathrm{Lie}\,G(\mathbb{R})$. ($J^2 = -1$ is central.)

## 5. Theorem A: interior weak positivity bounds the centraliser

**Theorem A.** Suppose that, for some $1\le p\le n-1$, a rational Hodge class $\alpha$ of degree $2p$ lies in $\operatorname{int}\mathrm{WP}^p$. Then $Z := Z_{G(\mathbb{R})}(J)$ is compact. Reductivity of $G$ is not needed.

*Proof.* Fix a hermitian norm on $V$. Interior weak positivity gives $\varepsilon, M > 0$ with $\varepsilon|\xi|^2 \le \alpha(\xi) \le M|\xi|^2$ for every decomposable $\xi = e_1\wedge\cdots\wedge e_p \in \Lambda^p_{\mathbb{C}}V$. Here $\alpha(\xi)$ is the value of $\alpha$ on the underlying real $2p$-vector, i.e. a hermitian form evaluated on decomposables. An element $g \in Z$ is $\mathbb{C}$-linear and preserves $\alpha$. So for decomposable $\xi$,

$$
|\Lambda^p g\,\xi|^2 \le \varepsilon^{-1}\alpha(\Lambda^p g\,\xi) = \varepsilon^{-1}\alpha(\xi) \le (M/\varepsilon)|\xi|^2 .
$$

A unitary basis $\{e_I\}$ of $\Lambda^pV$ consists of decomposable vectors, so $\|\Lambda^p g\|$ is bounded uniformly on $Z$, and so is $\|\Lambda^p g^{-1}\|$. Thus $\Lambda^p(Z)$ is relatively compact in $GL(\Lambda^pV)$. For $1\le p\le n-1$ the homomorphism $\Lambda^p: GL_n(\mathbb{C}) \to GL(\Lambda^p\mathbb{C}^n)$ has finite kernel (the scalars $\zeta$ with $\zeta^p = 1$) and closed image, so it is proper onto its image. Therefore the closed subgroup $Z$ is compact. $\square$

**Corollary A′.** Under the hypothesis of Theorem A, suppose $G$ is reductive. Then (i) the identity component of the centre of $G(\mathbb{R})$ is compact, and (ii) $\theta$ is a Cartan involution on every non-compact simple ideal $\mathfrak{g}_i$ of $\mathfrak{g}_{\mathbb{R}}$.

*Proof.* (i) The centre commutes with $J$. (ii) $J \in G(\mathbb{R})^0$, so $\theta$ is inner and preserves each simple ideal, and $\mathfrak{g}_i^\theta \subset \mathrm{Lie}\,Z$ is compact. Choose a Cartan involution $\theta_0$ of $\mathfrak{g}_i$ commuting with $\theta$, and write $\mathfrak{g}_i = \mathfrak{k}_0\oplus\mathfrak{p}_0$. For $X \in \mathfrak{p}_0\setminus 0$, $\mathrm{ad}\,X$ is real-diagonalisable and nonzero ($\mathfrak{g}_i$ is simple), while every element of the compact subalgebra $\mathfrak{g}_i^\theta$ has purely imaginary $\mathrm{ad}$-spectrum. So $\mathfrak{p}_0\cap\mathfrak{g}_i^\theta = 0$. Since $\theta$ commutes with $\theta_0$, it preserves $\mathfrak{p}_0$, so $\theta = -1 = \theta_0$ on $\mathfrak{p}_0$. Since $\mathfrak{g}_i$ is simple and non-compact, $\mathfrak{k}_0 = [\mathfrak{p}_0,\mathfrak{p}_0]$, and $\theta$ fixes it. Hence $\theta = \theta_0$. $\square$

## 6. Theorem B: the Cartan criterion

**Theorem B.** Suppose $G$ is reductive, $\theta$ is a Cartan involution on each non-compact simple ideal, $\theta$ is trivial on each compact simple ideal (i.e. $J$ is central in the compact factors), and the centre of $G(\mathbb{R})$ is compact. Then $T$ is projective.

*Proof.* Under these hypotheses $\theta = \mathrm{Ad}\,J$ is a Cartan involution of $G_{\mathbb{R}}$. By Deligne's criterion ([18, 1.1.18]; [19, Prop. 1.20]) every real representation of $G_{\mathbb{R}}$, in particular $V_{\mathbb{R}}$, carries a $G(\mathbb{R})$-invariant bilinear form $\varphi$ such that $s(x,y) := \varphi(x,Jy)$ is symmetric positive definite. Such a $\varphi$ is alternating. Indeed $s$ is $J$-invariant ($J\in G(\mathbb{R})$), so $s(Jx,y) = -s(x,Jy)$. Also $J^2=-1$ gives $s(u,Jv) = \varphi(u,J^2v) = -\varphi(u,v)$. Hence

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

Equivalently, $\beta = \gamma - \mathrm{Avg}_K\,k^*\gamma$ with $\gamma = \omega^q/q!$ is a nonzero weakly positive $(q,q)$-form orthogonal to $\mathrm{Hdg}^{2p}$, a dual certificate.

## 8. Theorem D: unipotent radicals

**Theorem D.** Let $\alpha$ be a real $(p,p)$-form on $V$ with $1\le p\le n-1$ and $\alpha\in\operatorname{int}\mathrm{WP}^p$. Let $N\ne 0$ be a nilpotent $\mathbb{R}$-linear endomorphism with $NJ = -JN$. Then $\alpha$ is not invariant under the one-parameter group $\exp(sN)$.

*Proof.* (1) *A real form adapted to $N$.* $N$ is antilinear, each $\ker N^k$ is $J$-stable, and $N$ maps complex subspaces onto complex subspaces ($N(\mathrm{span}_{\mathbb{C}}S) = \mathrm{span}_{\mathbb{C}}N(S)$). The Jordan-chain construction therefore works over $\mathbb{C}$ and gives a $\mathbb{C}$-basis $\{N^jv_i\}$ with $N^{m_i}v_i = 0$. Then $V_0 := \mathrm{span}_{\mathbb{R}}\{N^jv_i\}$ is totally real, $V = V_0\oplus JV_0$, $NV_0\subset V_0$, and $A := N|_{V_0}$ is nilpotent and nonzero.

(2) *A positive symmetric form.* For $\mu,\nu\in\Lambda^pV_0$ put $b(\mu,\nu) = \varepsilon_p\,\alpha(\mu\wedge J\nu)$, where $J\nu$ means $\Lambda^pJ$ applied to $\nu$ and $\varepsilon_p = \pm1$ is fixed below. $J$-invariance of $\alpha$ together with $(-1)^{p^2+p} = 1$ makes $b$ symmetric. For decomposable $\mu = f_1\wedge\cdots\wedge f_p\ne 0$ with $f_i\in V_0$ (these are $\mathbb{C}$-independent because $V_0$ is totally real), $\mu\wedge J\mu = \pm\xi_Q$ with $Q = \mathrm{span}_{\mathbb{C}}\{f_i\}$, with a sign depending only on $p$. Choosing $\varepsilon_p$ accordingly, interior weak positivity gives $c>0$ with $b(\mu,\mu)\ge c|\mu|^2$ for all decomposable $\mu\in\Lambda^pV_0$.

(3) *Self-adjointness.* $\exp(sN)J = J\exp(-sN)$, so invariance of $\alpha$ gives $b(e^{sA}\mu, e^{-sA}\nu) = b(\mu,\nu)$. Equivalently, the derivation induced by $A$ on $\Lambda^pV_0$ is $b$-self-adjoint, and $b(e^{sA}\mu,e^{sA}\mu) = b(e^{2sA}\mu,\mu)$.

(4) *Growth.* Since $A\ne0$ and $p<n$, some decomposable $\mu\in\Lambda^pV_0$ has $A\mu\ne0$ in $\Lambda^pV_0$ (the derivation representation of $\mathfrak{gl}(V_0)$ on $\Lambda^pV_0$ is faithful for $1\le p\le n-1$, and decomposables span $\Lambda^pV_0$). Let $k\ge1$ be maximal with $A^k\mu\ne0$. Then $f(s) = b(e^{2sA}\mu,\mu)$ is a polynomial of degree at most $k$. But $e^{sA}\mu$ is decomposable, and $s^{-k}e^{sA}\mu\to A^k\mu/k!\ne0$. So $|e^{sA}\mu|\ge c'|s|^k$ for large $|s|$, and step (2) gives $f(s)\ge cc'^2 s^{2k}$. Since $2k>k$, this is a contradiction. $\square$

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

5. $\Omega_h$ is invariant under $Sp(1)_L$, which rotates the hyperkähler triple, and under $Sp(1)_R$, which commutes with every $L_a$ and preserves $g_A$. For $I = L_u$, $\Omega_h = \omega_I^2+\sigma\wedge\bar\sigma$ with $\sigma = \omega_J+i\omega_K$ of type $(2,0)$. On $\Lambda^2T^{1,0}$ the hermitian form of $\omega_I^2$ is twice the induced metric, hence positive definite, and that of $\sigma\wedge\bar\sigma$ is the rank-one positive semidefinite form $\sigma\sigma^*$. Their sum is positive definite. Numerically its eigenvalues are $2$ (multiplicity 5) and $10$. $\operatorname{int}\mathrm{P}^2\cap\mathrm{Hdg}^4_{\mathbb{R}}$ is a nonempty open cone in $\mathrm{Hdg}^4_{\mathbb{R}}$, so it contains rational points.

6. Let $Z\subsetneq T$ be an irreducible analytic subvariety of positive dimension. By Ueno's structure theorem [20], $Z$ is a fibre bundle over a variety of general type whose fibre is a translate of a subtorus. $T$ is simple, so the fibre is a point and $Z$ is of general type, hence Moishezon. Let $\tilde Z\to Z$ be a resolution. The image of $\tilde Z\to T$ generates a subtorus, which is $T$ because $T$ is simple. This map factors through $\mathrm{Alb}(\tilde Z)$, an abelian variety, so $T$ would be a quotient of an abelian variety, which is impossible. $\square$

**Consistency with Theorem C.** Here $K = Sp(1)_L\times1\not\subset Z(J)$, so $\mathrm{Hdg}^4_{\mathbb{R}}\cap\operatorname{int}\mathrm{SP}^2 = \emptyset$. The Kraines class sits exactly on $\partial\mathrm{SP}$: $\sigma\wedge\bar\sigma$ is maximally entangled in $\Lambda^2\mathbb{C}^4$, and its Uhlmann concurrence margin is $0$ (Section 13). The Hodge classes here are P-interior but cannot be SP-interior. The gap between Demailly's two cones is exactly where cycle-type positivity fails.

## 11. The same mechanism on hyperkähler manifolds

**Theorem 11.1.** Let $(X,I)$ be a compact hyperkähler manifold of complex dimension $2n\ge4$, and $1\le p\le 2n-1$. If $\alpha\in H^{2p}(X,\mathbb{R})$ is invariant under the $SU(2)$-action on cohomology induced by some hyperkähler metric on $(X,I)$, then $\alpha$ is not SP-interior on $(X,I)$.

*Proof.* Take $J' = J$ from the quaternionic triple. It is $g$-orthogonal, $\omega_J$ is parallel (so $\omega_J^q$ is closed), and $J\ne\pm I$ everywhere. The $SU(2)$-action on harmonic forms is by isometries, preserves the top-degree pairing and $\alpha_{\mathrm{harm}}$, and sends $\omega_I^q$ to $\omega_J^q$. So $\int\alpha\,\omega_J^q = \int\alpha\,\omega_I^q$, and Lemma 7.1 gives a contradiction. $\square$

**Corollaries.** (i) The Chern classes $c_{2k}(X)$ with $0<2k<2n$ are $SU(2)$-invariant, being of Hodge type for every induced complex structure. So they are never SP-interior, even on projective $X$. For example, on $X = K3^{[2]}$, $\int c_2\,a^2 = 30\,q(a)$ and $q(\omega_I) = q(\mathrm{Re}\,\sigma)$. (ii) Suppose every Hodge class of $X$ is $SU(2)$-invariant. This holds for all but countably many complex structures in a twistor family (Verbitsky [10]). It also holds for $X$ very general in its moduli, since then the Mumford–Tate algebra acting on $H^*(X)$ through the Looijenga–Lunts–Verbitsky action is $\mathfrak{so}(H^2(X,\mathbb{Q}),q)$, which contains the $\mathfrak{su}(2)$ of every hyperkähler metric. Then no rational Hodge class of degree $2,\dots,4n-2$ on $X$ is SP-interior. This matches the torus picture: an SP-interior Hodge class has to break every hidden rotation of the complex structure.

## 12. The Chern-class form of the question on the sharpness example

Voisin's Kähler counterexamples [2] also exclude Chern classes of coherent sheaves. For the torus $T_u$ of Proposition 10.1 we can only reduce this question.

**Proposition 12.1.** Let $S\subset\mathrm{Hdg}^4(T_u,\mathbb{Q})$ be the $\mathbb{Q}$-span of $\mathrm{ch}_2(\mathcal{F})$ over coherent sheaves $\mathcal{F}$. Then $S = \mathbb{Q}\,\omega^2$ or $S = \mathrm{Hdg}^4(T_u,\mathbb{Q})$.

*Proof.* Isogenies $b\in\mathcal{O}_B\setminus0$ act on $T_u$, $b^*\mathcal{F}$ is coherent, and $\mathrm{ch}(b^*\mathcal{F}) = b^*\mathrm{ch}(\mathcal{F})$. The two $B^\times$-isotypic pieces $\mathbb{Q}\,\omega^2$ and $K_5$ (the rational 5-dimensional summand) are absolutely irreducible and non-isomorphic, and $B^\times(\mathbb{Q})$ is Zariski dense in $GL_1(B)$. So the span of the orbit of $v = v_0+v_5$ contains $K_5$ whenever $v_5\ne0$. Line bundles give $\omega^2$. $\square$

**What remains (no claim).** $T_u$ contains no curves, surfaces or divisors. Hence torsion sheaves are supported in dimension $0$, passing to reflexive hulls does not change $\mathrm{ch}_2$, and Jordan–Hölder factors are stable reflexive sheaves. All Hodge classes are $Sp(1)_L$-invariant, so by Verbitsky [10, 11] these factors are hyperholomorphic, with curvature valued in the $Sp(1)_L$-invariant 2-forms tensored with $\mathfrak{u}(r)$. For locally free sheaves, Proposition 12.2 below makes precise how this decides which case of Proposition 12.1 holds. Which case holds remains open. Natural constructions do not help. Line bundles and simple semi-homogeneous bundles are projectively flat, so their $\mathrm{ch}$ lies in $\mathbb{Q}[c_1] = \mathbb{Q}[\omega]$. Tensor products, extensions, isogenies and Fourier–Mukai along the Poincaré bundle all preserve the subgroup with vanishing $K_5$-part (the cohomological Fourier–Mukai map is $G$-equivariant). The question needs a genuinely new "seed" object, for example a hyperholomorphic sheaf on a CM fibre of the family deformed along it, as in Markman's method [13, 14].

**The Bogomolov argument does not decide it.** On Weil-type tori, Voisin [2] excludes Chern classes using the Bogomolov inequality. The same inequality applies on $T_u$, but it only constrains the sign. The Jordan–Hölder factors above have $c_1\in\mathbb{Q}\omega$, and Bogomolov–Gieseker (Bando–Siu) for each factor gives $\int\mathrm{ch}_2(\mathcal{F})\,\kappa^2\le0$ for every coherent $\mathcal{F}$ and every Kähler class $\kappa$ with $\int\omega^2\kappa^2\le0$. For a real linear form $\ell$ on $U$, the map $\pi_\ell = 1\otimes\ell: A\otimes U\to A$ is $\mathbb{C}$-linear, and $\mathrm{vol}_A\otimes\ell^4 = \pi_\ell^*\mathrm{vol}_A$ is strongly positive. So every class $x\,\omega^2 - \sum_k \mathrm{vol}_A\otimes\ell_k^4$ with $x\ge0$ satisfies these inequalities. These classes form a convex cone that spans $\mathrm{Hdg}^4_{\mathbb{R}}$, because fourth powers span $S^4U^*$. Hence the cone has nonempty interior, and the inequalities alone cannot force the $K_5$-part of $\mathrm{ch}_2$ to vanish. (The maps $\pi_\ell$ are linear but not defined over $\mathbb{Q}$, so they do not induce morphisms of tori.)

The positivity that does constrain Chern classes here lives in the multiplicity space $U$. For $f\in S^4U^*$ write $v_f\in K_5\otimes\mathbb{R}$ for the class $v_f(a_1\otimes u_1,\dots,a_4\otimes u_4) = \mathrm{vol}_A(a_1,\dots,a_4)\,\tilde f(u_1,\dots,u_4)$, with $\tilde f$ the polarisation of $f$. Then $v_{\ell^4} = \pi_\ell^*\mathrm{vol}_A$. For $h\in S^2_+U^*$ let $\omega_{I,h}$ be the Kähler form of $g_A\otimes h$ for $I = J$.

**Proposition 12.2.** Let $u$ be very general and $E$ an $\omega_{I,h}$-stable vector bundle on $T_u$ for some $h$. Then the $K_5$-component of $\mathrm{ch}_2(E)$ equals $-v_{p_E}$ for a nonnegative binary quartic $p_E$ on $U$, and $p_E = 0$ iff $E$ is projectively flat. Consequently, if some such $E$ is not projectively flat, then every class in $\mathrm{Hdg}^4(T_u,\mathbb{Q})$ is a $\mathbb{Q}$-combination of classes $\mathrm{ch}_2$ of vector bundles, and no nonzero one is analytic.

*Proof.* $c_1(E)\in\mathrm{NS}_{\mathbb{Q}} = \mathbb{Q}\omega$. Since $\mathrm{Hg}(T_u) = G$, $c_2(E)$ is $G(\mathbb{R})$-invariant, and in particular invariant under $Sp(1)_L$, which is the $SU(2)$ induced on cohomology by the hyperkähler metric $g_A\otimes h$. By Verbitsky [10] the Hermite–Einstein connection of $E$ is hyperholomorphic: its curvature $\Theta$ takes values in the $Sp(1)_L$-invariant 2-forms tensored with $\mathfrak{u}(E)$. These invariant forms are $\bigoplus_{a=1}^3\alpha_a\otimes S^2U^*\oplus\mathbb{R}\omega$, where $\alpha_a = g_A(R_a\cdot,\cdot)$ and $R_a$ is right multiplication by $i,j,k$. So
$$
\Theta = \sum_a \alpha_a\otimes\Theta_a + \omega\otimes\Theta_0,
$$
with $\Theta_a$ a section of $S^2U^*\otimes\mathfrak{u}(E)$; write $\Theta_a(x)\in\mathfrak{u}(E)$ for its value at $x\in U$. By $GL(A)\times GL(U)$-equivariance, the $K_5$-component of $(\alpha_a\otimes s)\wedge(\alpha_b\otimes t)$ is $c_{ab}\,v_{st}$. A direct computation (supplement, `t28.py`) gives $c_{ab} = -2\delta_{ab}$, and shows that $\omega\wedge(\alpha_a\otimes s)$ and $\omega^2$ have no $K_5$-component. On a torus, the class of a closed form is that of its translation average. Since $\mathrm{ch}_2 = -\frac{1}{8\pi^2}\mathrm{tr}(\Theta\wedge\Theta)$,
$$
K_5(\mathrm{ch}_2E) = \frac{1}{4\pi^2}\,v_{q},\qquad q(x) = \operatorname{avg}_{T}\sum_a\mathrm{tr}\big(\Theta_a(x)^2\big),
$$
and $p_E := -q/4\pi^2\ge0$ because $\mathrm{tr}(M^2) = -|M|^2$ on $\mathfrak{u}(r)$. Moreover $p_E\equiv0$ iff all $\Theta_a$ vanish identically, i.e. $\Theta = \omega\otimes\Theta_0$. In that case the Bianchi identity gives $\omega\wedge\nabla\Theta_0 = 0$, so $\nabla\Theta_0 = 0$ because $\omega$ is nondegenerate and $\omega\wedge$ is injective on 1-forms in real dimension 8. Stable bundles are simple, so $\Theta_0$ is scalar and $E$ is projectively flat. Conversely, projectively flat bundles have $\Theta = \omega\otimes\Theta_0$ with $\Theta_0$ scalar. The last statement follows from Proposition 12.1 and Proposition 10.1(6). $\square$

The sign is the one geometry predicts. If $\pi_\ell$ induced a morphism of tori, the ideal sheaf of a fibre $Z$ would have $\mathrm{ch}_2(\mathcal{I}_Z) = -v_{\ell^4}$. The nonnegative quartics form a strictly larger cone than the sums of fourth powers. Extending Proposition 12.2 to stable reflexive sheaves would turn its last statement into an equivalence. Their singular sets are finite here, but we have not checked Chern–Weil for admissible connections against arbitrary constant 4-forms.

**Remark 12.3 (a cubic analogue: non-analytic classes that specialise to Weil classes).** Replace $F$ by a totally real cubic field and $D$ by a quaternion algebra over $F$ ramified at the three real places, and for parity at an odd number of finite places. Then $\mathrm{Cor}(D)\cong M_4(B)$ with $B$ a definite quaternion algebra over $\mathbb{Q}$. $V_{\mathbb{Q}} = B^4$ gives 8-dimensional tori $T_u$ with $G(\mathbb{R}) = Sp(1)^3$ and $J$ in the first factor. For very general $u$:

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
- The sharpness example concerns the cycle form of the question. Its Chern-class form is open. By Propositions 12.1–12.2, a single stable vector bundle on $T_u$ that is not projectively flat would make every rational Hodge class a combination of Chern characters.
- The cone $\mathrm{P}$ in Proposition 10.1 is shown to fail, but we do not characterise which non-projective tori carry P- or WP-interior rational classes beyond the necessary conditions of Remark 9(c).
- Remark 12.3 is supported by an exact weight computation and a hand argument at CM points. It is a remark, not a theorem.

**Reproducibility.** The supplement contains Python 3 scripts (numpy, scipy; CPU, each under a few minutes) for the numerical consistency checks. None of the proofs depends on them.

- `invforms.py`, `t14.py`: invariant forms as null spaces of the derivation action. Cor type gives $\dim\mathrm{NS} = 1$ and $\dim\mathrm{Hdg}^4 = 6$, and the Kraines form has hermitian eigenvalues $(2,2,2,2,2,10)$.
- `sp_test.py`, `t15.py`: SP test on $\Lambda^2\mathbb{C}^4$. $x\mapsto x\wedge x$ is a nondegenerate quadratic form, and $x$ is decomposable iff $x\wedge x = 0$. In a magic basis, separability of a fermionic state $H$ is decided by Uhlmann's convex-roof concurrence $C(H) = \max(0,\lambda_1-\lambda_2-\cdots-\lambda_6)$ [16, 17], where $\lambda_i$ are the decreasing eigenvalues of $(\sqrt H\bar H\sqrt H)^{1/2}$. We use the margin $\lambda_2+\cdots+\lambda_6-\lambda_1>0$ (with $H>0$) as the interior test. It was validated on decomposable $+\,\varepsilon I$, on $I$, and on an isotropic family (threshold $0.4$). Cor type: the maximal margin over $\mathrm{Hdg}^4_{\mathbb{R}}$ is $0$ (to $1.6\cdot10^{-13}$).
- `t16.py`–`t19.py`: Monte-Carlo $K$-averaged certificate of Theorem C, which is weakly positive and orthogonal to $\mathrm{Hdg}^4$.
- `t13.py`: $Sp(1)\times SL_2(\mathbb{R})$ with $J$ in the compact factor has no WP-interior Hodge class (consistency with Theorem A).
- `t20.py`: rank-one antilinear nilpotent $N$; the invariant $(2,2)$-forms have maximal weak minimum $-0.039<0$ (consistency with Theorem D).
- `t27.py`, `t28.py`, `t28b.py`: exterior-algebra computations for Section 12. $c_{ab} = -2\delta_{ab}$ (residual $<10^{-16}$), $\omega$-terms have no $K_5$-component, and the forms $\alpha_a\otimes s$ are $Sp(1)_L$-invariant.
- `t21.py`, `t22.py`, `t23.py`: the cubic and quintic analogues of Remark 12.3 (`python3 scratch/t23.py 3`, resp. `5`; the latter takes about a minute).

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

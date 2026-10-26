# Full-spin domination and generalized Hodge support for K3 surfaces

cm_symmetry_scout and lelong_ridge

*Version 3, 26 October 2026: scope correction.*

The full-spin theorem and conditional support criterion are unchanged.
The order-three and Eisenstein applications are now explicitly conditional
on algebraicity of the specified full Clifford correspondence. The
half-twist correspondence in the cited constructions does not by itself
verify that hypothesis; Section 7.1 records the precise distinction.

## 1. Results and relation to the Hodge conjecture

Let $T$ be a simple polarized rational Hodge structure of K3 type:
it has types $(2,0),(1,1),(0,2)$, $h^{2,0}=h^{0,2}=1$, and no
proper nonzero rational Hodge substructure. Let $A=\operatorname{KS}(T)$ denote
the Kuga–Satake abelian variety defined by the left regular
even-Clifford Hodge structure $C^+(T)$. We retain this full source,
including both complex half-spin representations when $\dim T$ is even.
For a pure rational Hodge structure $U$, its level is

$$
\ell(U)=\max\{|p-q|:U^{p,q}\ne0\}.
$$

An effective weight-$\ell$ Hodge structure with a nonzero
$(\ell,0)$ component is called fully twisted.

**Theorem 1.1 (full-spin self-domination).** Let
$U\subset H^j(A^n,\mathbb Q)$ be an irreducible rational Hodge
substructure, and put $\ell=\ell(U)$. Then

$$
U\left(\frac{j-\ell}{2}\right)
\quad\text{is isomorphic to a direct summand of}\quad
H^\ell(A^\ell,\mathbb Q).
\tag{1.1}
$$

For $\ell=0$ use $A^0=\operatorname{Spec}\mathbb C$.
The summand is fully twisted. The theorem holds for CM and
totally real endomorphism fields, including compact real factors
and arbitrary rational Schur indices.

Thus powers of the actual full Kuga–Satake variety are dominated,
in the Hodge-theoretic sense, by powers of that same variety.
No algebraicity assertion is needed for Theorem 1.1. Its geometric
consequence uses ordinary Hodge classes to construct supports.

**Theorem 1.2 (ordinary-to-generalized criterion).** Let $S$ be a
smooth complex projective K3 surface. Suppose:

1. its usual specified Kuga–Satake correspondence is algebraic;
2. the ordinary rational Hodge conjecture holds for every power of $S$.

Then the generalized rational Hodge conjecture holds for every

$$
S^r\times\operatorname{KS}(S)^n,\qquad r,n\ge0.
\tag{1.2}
$$

The same conclusion holds after adjoining abelian isogeny factors of
powers of $\operatorname{KS}(S)$. Either the primitive or the
transcendental convention for $\operatorname{KS}(S)$ may be used.
All products are attached to one fixed surface $S$. In hypothesis 1,
the specified correspondence means the standard embedding of the
transcendental Hodge structure $T(S)$ into
$H^2(\operatorname{KS}(S)^2,\mathbb Q)$ obtained from Clifford
multiplication and a polarization.

Here generalized HC means that a rational Hodge substructure
$U\subset H^j(X,\mathbb Q)$ of level at most $j-2p$ is supported
on an algebraic subset of codimension at least $p$. We prove the
support assertion by an actual algebraic correspondence in Section 6;
we do not identify Hodge level with coniveau without constructing
that correspondence.

The criterion has the following conditional and unconditional applications.

**Corollary 1.3 (order-three case with specified correspondence).**
Let $S$ have a nonsymplectic automorphism of order three. If its
specified Clifford Kuga–Satake correspondence is algebraic, then
the conclusion of Theorem 1.2 holds. Ordinary HC for powers of $S$
is already known in this case. This statement does not assert the
additional algebraicity hypothesis for an entire order-three family.

**Corollary 1.4.** The conclusion holds for every projective K3
surface $S$ for which there is a rational isometric embedding

$$
T(S)_{\mathbb Q}\hookrightarrow
\left(U^{\oplus3}\oplus\langle-m\rangle\right)_{\mathbb Q}
\quad\text{for some integer }m>0,
\tag{1.3}
$$

where $U$ is the hyperbolic plane. It also holds for the families
satisfying the precise hypotheses of Varesco's Theorem 0.2 [1].

**Corollary 1.5 (conditional Eisenstein application).** Assume:

**(H12)** For every smooth K3 surface in the twelve-point family
(7.1), its specified full Clifford Kuga–Satake correspondence is algebraic.

Put $K=\mathbb Q(\sqrt{-3})$. Under (H12), for every polarized abelian $n$-fold $B$
with compatible $K$ action of signature $(n-1,1)$, where
$1\le n\le9$, generalized rational HC holds on every power of
$B\times E_K$. Its rational Hermitian determinant class is arbitrary,
and no generic-endomorphism assumption is imposed. For $n=10$,
the same assertion holds in the rational Hermitian datum of the
twelve-point family in Section 7.2. Each assertion concerns one
fixed $B$, not a product of independent periods.

The main new step is the full-spin domination criterion and its resulting
generalized support under its stated hypotheses. Corollary 1.5 is a
conditional application with elliptic stabilization to cover every rational
Hermitian class in the stated dimensions. We have not verified (H12) from
the cited half-twist constructions. The unconditional generalized-Kummer
application is Corollary 1.4. The general rational Hodge conjecture,
ordinary HC for arbitrary K3 powers, and the additional specified
correspondences required by the Eisenstein application remain open here.

## 2. Prior work and what is added

Zarhin determines the Hodge groups and endomorphism fields of simple
K3-type structures [2]. The Kuga–Satake construction and its Clifford
decomposition are classical; van Geemen gives a detailed account [3].
We use both results as inputs.

The strategy of realizing a fully twisted Tate twist and then using
ordinary HC to obtain generalized HC goes back to Grothendieck;
Abdulali develops domination systematically [4, Section 3]. His
semisimple PEL theorem [5, Theorem 5.1], in the formulation without
type-III factors in [4, Theorem 4.1], proves self-domination in that
range. A full KS source need not be of PEL type, and its Hodge group
need not be semisimple. His $SU(p,1)$ theorem gives domination by
suitable abelian varieties [4, Theorem 6.6], using the constructions
in [6]. It does not identify those sources with powers of a given
full KS variety, nor does its stated hypothesis include arbitrary
compact real factors. The spin augmentation in [4, Theorem 7.2]
is an important low-rank precedent: it supplies an additional spin
abelian variety for a particular type-III PEL problem. Here the
source is already the full KS variety, and we construct every
required representation in its $\ell$th power, in both endomorphism
field cases.

We use the corrected formulations of these results. In particular,
[4, Appendix B] retracts the rational product decomposition asserted
in [5, Proposition 4.4.1] and corrects several type-III and type-IV
statements. Our argument does not decompose a rational irreducible
into rational factors: it aligns all complex factors first, computes
the level of the full rational orbit, and then descends an equivariant
Hom space. The distinction matters when Galois acts on several factors.

Floccari proves that, once the specified KS correspondence is
algebraic, ordinary HC for all K3 powers is equivalent to ordinary
HC for all KS powers [7, Theorem 3.5]. This is the ordinary-HC input
to Theorem 1.2, not a new result here. Varesco establishes ordinary HC
for all powers of a K3 with CM endomorphism field, and for the
specific Picard-sixteen families in his Theorem 0.2 [1]. Bolognesi
and Laterveer state the KS Hodge conjecture for order-three families
[8, Theorem 4.4 and Propositions 6.2,6.4], importing the half-twist
construction of van Geemen–Izadi [9, Sections 5.1–5.3] and its relative
form in Laterveer [10, Theorem 2.8]. Section 7.1 explains why we do not
use these constructions as a verified source of the specified full
Clifford tensor. Floccari proves both hypotheses of Theorem 1.2
under (1.3) by separate generalized-Kummer geometry [7, Theorem 5.11].

A previous Gaussian rank-ten construction gave a full-spin rectangle
argument when the CM endomorphism field contains a fixed imaginary
quadratic field [11, Section 10.9]. That argument allowed all smaller
Hodge groups at its special points but used simultaneous conjugation
of its CM factors. Section 4 below removes the imaginary-quadratic
subfield restriction by tracking independent dualizations. Section 5
adds the entirely orthogonal case through dominant minuscule paths.
Together they give a criterion for every full KS source of simple K3 type.

The related half-twist decomposition for an imaginary-quadratic
endomorphism field is due to van Geemen [12, Theorem 3.10]. Our theorem
does not replace that decomposition: it uses the complete regular
spin source to control every irreducible representation, every
central character, and the rational Hodge level.

The additional applications in Section 7 use van Geemen's classical
twelve-point family [12, Example 3.11], the criterion above, and
rational unitary period transport. Adding pure elliptic factors
removes the rational determinant restriction before passing to
isogeny factors. This differs from constructing an abstract
effective Hodge structure or a new KS correspondence. The full-spin
theorem and its arbitrary-weight proofs are those of version 1;
the new application is proved separately in Sections 7.2–7.5.

## 3. Hodge groups, full spin, and rational descent

Let $F=\operatorname{End}_{\mathrm{Hdg}}(T)$. It is a totally real
or CM field [2]. Put $G=\operatorname{Hg}(T)$, and let
$\widetilde G$ be its inverse image in $\operatorname{Spin}(T)$.
We will verify in each case that this inverse image is connected.

The weight-one KS Hodge circle lies in $\operatorname{Spin}(T)$
and projects onto the weight-two circle of $T$. Therefore
$\operatorname{Hg}(A)\subseteq\widetilde G$, and its projection is
$G$: the projected group contains the circle and is contained in
its smallest rational algebraic group. The kernel is finite, so
both groups have the same dimension. Once $\widetilde G$ is
connected, it follows that

$$
\operatorname{Hg}(A)=\widetilde G.
\tag{3.1}
$$

This concerns Hodge groups, not the additional weight-scalar torus
in the Mumford–Tate group.

The complex left regular even Clifford module contains the spin
module when $\dim T$ is odd, and both half-spin modules when
$\dim T$ is even, with positive multiplicities [3, Sections 6–8].
We will only need their occurrence. A chosen minimal rational
spin module or one half-spin factor is not substituted for this
regular source. Rational splitting of a Clifford algebra is not
assumed.

We use the following rational-descent observation repeatedly.
Suppose a rational irreducible Hodge structure $U$ has level
$\ell$ and weight $j$, and a complex irreducible constituent of
$U$ occurs in $H^\ell(A^\ell,\mathbb C)$ as a $\widetilde G$
representation. Then

$$
\operatorname{Hom}_{\widetilde G}
\left(H^\ell(A^\ell,\mathbb Q),U((j-\ell)/2)\right)
\otimes_{\mathbb Q}\mathbb C\ne0.
\tag{3.2}
$$

Here equivariant Hom commutes with scalar extension. A nonzero
rational map is surjective because $U$ is irreducible. The two
sides have equal weight, and equivariance gives equality of
Hodge-circle actions; hence the map is a Hodge morphism. The
category of polarizable rational Hodge structures is semisimple,
so the quotient splits. The parity of $j-\ell$ follows from the
Hodge decomposition. This avoids descending a single complex
spin constituent and handles rational multiplicities and Schur
indices.

Consequently it suffices to exhibit each complex irreducible in
degree equal to the level of its rational orbit. Its rational
summand is then effective and contains an extreme Hodge component;
complex conjugation supplies the other extreme if necessary.

## 4. CM endomorphism fields: signed rectangles

Write $F^+$ for the maximal totally real subfield,
$d=[F^+:\mathbb Q]$, and $m=\dim_FT$. Zarhin gives

$$
G=\operatorname{Res}_{F^+/\mathbb Q}U(T,h).
\tag{4.1}
$$

Choose one embedding from each conjugate pair of embeddings of
$F$; the choice need not be Galois stable. Then

$$
T_{\mathbb C}=U\oplus U^*,\qquad
U=\bigoplus_{\alpha=1}^dU_\alpha,\qquad
G_{\mathbb C}=\prod_{\alpha=1}^dGL(U_\alpha),
\quad \dim U_\alpha=m.
\tag{4.2}
$$

Its spin preimage is

$$
\widetilde G_{\mathbb C}
=\left\{((g_\alpha),z):z^2=\prod_\alpha\det(g_\alpha)\right\}.
\tag{4.3}
$$

This group is connected: the defining character on a maximal
torus has primitive integer coefficients, including a coefficient
one, and its derived subgroup is a product of connected $SL_m$'s.
Thus (3.1) applies. Write $e$ for the character $z$. The full spin
restriction is

$$
e^{-1}\bigwedge^\bullet U
=\bigoplus_{0\le k_\alpha\le m}
e^{-1}\bigotimes_\alpha\bigwedge^{k_\alpha}U_\alpha.
\tag{4.4}
$$

Every summand occurs in actual $H^1(A,\mathbb C)$. At the active
embedding, orient the chosen $U_\alpha$ to contain $T^{2,0}$.
The circle has weight two on one coordinate of this factor and
zero on all the other coordinates; it has weight one on $e$.
Thus all summands of (4.4) have only circle weights $\pm1$.

A complex irreducible representation can be written

$$
R=e^b\bigotimes_{\alpha=1}^d\mathbb S_{\lambda_\alpha}U_\alpha,
\qquad b\in\mathbb Z,
\quad\lambda_{\alpha,1}\ge\cdots\ge\lambda_{\alpha,m}\in\mathbb Z.
\tag{4.5}
$$

Negative entries are permitted. The identity $e^2=\prod\det U_\alpha$
identifies the presentations

$$
(b,\lambda_\alpha)\sim
(b-2c,\lambda_\alpha+(c,\ldots,c)),\qquad c\in\mathbb Z.
\tag{4.6}
$$

At active factor $\alpha$, the two circle extrema are
$b+2\lambda_{\alpha,m}$ and $b+2\lambda_{\alpha,1}$.
We must account for Galois action before identifying the rational
level. Besides permuting factors, each Galois automorphism determines
a subset $J$ of the chosen embedding factors that it dualizes.
The following calculation works for every such subset; a particular
CM field need not realize every sign pattern. Suppressing
the permutation, it acts by

$$
e\longmapsto e\prod_{\alpha\in J}\det(U_\alpha)^{-1}.
\tag{4.7}
$$

Squaring the right side gives the transformed determinant product;
the character lattice of a connected torus has no two-torsion, so
the square determines the character. A dualized highest weight becomes

$$
\lambda_\alpha\longmapsto
(-b-\lambda_{\alpha,m},\ldots,-b-\lambda_{\alpha,1}).
\tag{4.8}
$$

Its circle extrema are the negatives of the old extrema in reverse
order. Thus independent dualization preserves their absolute values.
Galois is transitive on the real embeddings of $F^+$; every factor
can be moved to the active one. A rational irreducible containing
$R$ therefore has exact level

$$
\ell=\max_\alpha\max\left(
|b+2\lambda_{\alpha,m}|,
|b+2\lambda_{\alpha,1}|\right).
\tag{4.9}
$$

Inner forms change neither these weights nor the conclusion. This
calculation requires no imaginary-quadratic subfield of $F$.

All extrema have parity $b$. Set $c=(b+\ell)/2$ and
$\lambda'_\alpha=\lambda_\alpha+(c,\ldots,c)$. Then

$$
0\le\lambda'_{\alpha,j}\le\ell,\qquad
R=e^{-\ell}\bigotimes_\alpha\mathbb S_{\lambda'_\alpha}U_\alpha.
\tag{4.10}
$$

Each partition $\lambda'_\alpha$ fits into an $m$-by-$\ell$
rectangle. Write it as exactly $\ell$ columns, permitting heights
zero and $m$, and align the columns across all $\alpha$. If column
$s$ has heights $(k_{\alpha,s})$, it is the actual weight-one module

$$
e^{-1}\bigotimes_\alpha\bigwedge^{k_{\alpha,s}}U_\alpha
\subset H^1(A,\mathbb C).
\tag{4.11}
$$

The Cartan highest-weight component of the tensor product of these
$\ell$ columns is (4.10). Put the columns in distinct abelian factors
to obtain $R\subset H^\ell(A^\ell,\mathbb C)$. When $\ell=0$
the representation is trivial. Formula (3.2) proves Theorem 1.1 in
the CM case.

## 5. Totally real endomorphism fields: dominant spin paths

Now let $F$ be totally real, $d=[F:\mathbb Q]$ and $m=\dim_FT$.
Zarhin gives

$$
G=\operatorname{Res}_{F/\mathbb Q}SO(T,h).
\tag{5.1}
$$

The active real factor contains the positive real two-plane of
$T^{2,0}\oplus T^{0,2}$, so $m\ge2$. In rank two the commutative
orthogonal group would give a larger CM endomorphism field. Thus
$m\ge3$. Over $\mathbb C$ the vector
representation is the orthogonal sum of $d$ spaces of dimension $m$.
The spin preimage is the image of $\prod_\alpha\operatorname{Spin}_m$
under multiplication in the Clifford algebra. Its kernel is

$$
K=\left\{(\epsilon_\alpha):\epsilon_\alpha\in\{\pm1\},
\ \prod_\alpha\epsilon_\alpha=1\right\}.
\tag{5.2}
$$

Indeed this image projects onto the product of the $SO_m$ factors
and contains the full kernel $\{\pm1\}$ of the ambient spin cover.
It is therefore the entire preimage, and is connected. Again (3.1)
applies.

Use orthogonal highest-weight coordinates. If $m=2a+1$, the type
is $B_a$ and a dominant weight satisfies
$\lambda_1\ge\cdots\ge\lambda_a\ge0$. If $m=2a$, the type is
$D_a$ and dominance is
$\lambda_1\ge\cdots\ge\lambda_{a-1}\ge|\lambda_a|$.
The coordinates are all integers or all half-integers. An
irreducible of the product descends through (5.2) exactly when
central $-1$ acts the same way in every factor. Thus all factors
have the same integer/half-integer parity.

The K3 circle in the active vector factor has weights $2,-2,0,\ldots,0$.
An irreducible of highest weight $\lambda_\alpha$ has extreme
circle weights $\pm2\lambda_{\alpha,1}$. Galois permutes the real
places; in type D it can additionally change the sign of the last
coordinate. The vector representation is defined over $F$, so
triality operations that interchange its node with a spin node
do not occur. Consequently the exact rational level is

$$
\ell=2\max_\alpha\lambda_{\alpha,1}.
\tag{5.3}
$$

The spin weights of type B are every sign vector
$(\pm\tfrac12,\ldots,\pm\tfrac12)$. The two type-D half-spin
modules divide the same sign vectors according to the parity of
minus signs. The full regular KS source contains every tensor
product of these factor spin modules, including every choice of
type-D half-spin signs. For even-dimensional vector factors this
follows by restricting both ambient half-spin modules. For odd
factors the restriction contains the tensor of the unique spin
modules with a positive multiplicity. Equivalently these facts
follow from the graded tensor-product decomposition of Clifford
algebras; no rational individual half-spin factor is required.

We record the elementary representation rule used in the construction.

**Lemma 5.1 (minuscule tensor rule).** If $\mu$ is dominant and
$V_\omega$ is minuscule, then

$$
V_\mu\otimes V_\omega
\cong\bigoplus_{\nu\in W\omega,\ \mu+\nu\text{ dominant}}
V_{\mu+\nu}.
\tag{5.4}
$$

**Proof.** Let $\mathcal A(\xi)=\sum_w\det(w)e^{w\xi}$ be the
Weyl alternant. Multiplying the Weyl numerator for $\mu$ by the
Weyl-invariant character $\sum_{\nu\in W\omega}e^\nu$ gives
$\sum_\nu\mathcal A(\mu+\rho+\nu)$. Minuscule weights have
coroot pairings in $\{-1,0,1\}$; hence each exponent is dominant
or singular. A nondominant $\mu+\nu$ gives a singular exponent
and a zero alternant. Division by $\mathcal A(\rho)$ yields (5.4).
The spin and half-spin modules just listed are minuscule. $\square$

Fix a factor and its dominant weight $\lambda$. Using the common
$\ell$ from (5.3), define

$$
t_i=\lambda_i+\ell/2\in\{0,1,\ldots,\ell\},\qquad
\lambda_i(k)=\min(k,t_i)-k/2,
\quad0\le k\le\ell.
\tag{5.5}
$$

This path starts at zero and ends at $\lambda$. Every increment
is a sign vector with coordinates $\pm\tfrac12$, hence a weight
of an available spin module. Every intermediate weight is dominant:

- Monotonicity follows from that of the $t_i$.
- In type B, $t_a\ge\ell/2$ implies
  $\min(k,t_a)-k/2\ge0$ for $0\le k\le\ell$.
- In type D, $t_{a-1}\ge t_a$ gives
  $\lambda_{a-1}(k)\ge\lambda_a(k)$. Also
  $t_{a-1}+t_a\ge\ell\ge k$, so
  $\min(k,t_{a-1})+\min(k,t_a)\ge k$ and
  $\lambda_{a-1}(k)\ge-\lambda_a(k)$.

Apply Lemma 5.1 at each step. It realizes $V_\lambda$ in a tensor
of exactly $\ell$ spin modules. Perform the construction in all
field factors and align the steps. Each aligned tensor of spin
modules is an actual constituent of $H^1(A,\mathbb C)$, so the
desired complex irreducible occurs in

$$
H^1(A,\mathbb C)^{\otimes\ell}
\subset H^\ell(A^\ell,\mathbb C).
\tag{5.6}
$$

Some Galois constituent attains the level in (5.3). Rational descent
by (3.2) completes Theorem 1.1. This includes compact real factors,
type $B_1$, and type $D_2=A_1\times A_1$.

## 6. From full twisting to algebraic support

Assume the hypotheses of Theorem 1.2. Floccari's Theorem 3.5 [7]
gives ordinary HC for all powers of $A=\operatorname{KS}(S)$.
The algebraic specified KS correspondence embeds the transcendental
K3 cohomology into a tensor construction on $H^1(A)$ with an
algebraic retraction. One may use polarization adjoints and inverse
Lefschetz operators: the standard conjectures hold for surfaces
and abelian varieties, and the inverse of the resulting invertible
operator is a rational polynomial in it. The remaining K3 cohomology
is Tate. Equivalently [7, Proposition 3.6] places $h^2(S)$ in the
semisimple category of homological motives generated by $h^1(A)$.

It follows that ordinary HC holds for every $S^r\times A^n$ and
after adjoining abelian isogeny factors of powers of $A$. The latter
have algebraic embeddings and retractions by isogenies and Poincare
complete reducibility. These statements also show that every Hodge
substructure in a mixed product is a representation of the same
$\operatorname{Hg}(A)$.

Let $X$ be one such mixed product and let
$U\subset H^j(X,\mathbb Q)$ be irreducible of level $\ell$.
The representation proofs of Sections 4–5 apply directly to $U$;
their construction does not depend on its original occurrence in
abelian cohomology. They provide a rational Hodge surjection

$$
H^\ell(A^\ell,\mathbb Q)\longrightarrow U(p),
\qquad p=(j-\ell)/2.
\tag{6.1}
$$

Put $Z=A^\ell$ and $D=\dim Z$. Viewed as a degree-raising map
$H^\ell(Z)\to H^j(X)$, this has shift $2p$. Ordinary HC on
$Z\times X$ represents it by an algebraic cycle of codimension
$D+p$. The cycle has dimension at most $\dim X-p$, so the image
of its support in $X$ has codimension at least $p$. The entire
image of the correspondence, in particular $U$, is supported there.

Every polarizable Hodge substructure is a finite direct sum of
irreducibles. Apply this argument to its constituents and take the
union of their supports. If a constituent has level strictly below
the requested bound, its support has even larger codimension.
This proves Theorem 1.2 with actual algebraic supports, not a
specialization argument for new Hodge classes.

The usual primitive and the transcendental KS conventions have the
same abelian isogeny factors up to powers, as explained in
[7, Remark 3.4]. Hence the conclusion is independent of this choice.

## 7. Applications and geometric hypotheses

### 7.1. The K3 criteria and the specified correspondence

For Corollary 1.3, the nonsymplectic automorphism supplies
$\mathbb Q(\sqrt{-3})\subset\operatorname{End}_{\mathrm{Hdg}}T(S)$.
The endomorphism field is therefore CM, and Varesco's Corollary 2.3 [1]
gives ordinary HC for every power of $S$. With the additional specified-KS
algebraicity hypothesis, Theorem 1.2 applies pointwise, including Picard
and endomorphism jumps.

A distinction in the geometric input is essential. For a K3-type
structure $V$ with imaginary quadratic action, let $S_0$ denote the
elliptic CM factor of its full KS source and $S_1$ its positive half
twist. Van Geemen–Izadi [9, Sections 5.1–5.3] construct the algebraic map

$$
\nu:V\longrightarrow S_1\otimes S_0
\subset H^1(\operatorname{KS}(V))^{\otimes2}.
$$

Laterveer [10, Theorem 2.8] constructs this map in family, through the
cubic-fivefold suspension. Bolognesi–Laterveer [8, Theorem 4.4] imports
it as the KS correspondence. The map required in [7, Conjecture 3.3 and
Proposition 3.6], and in our Theorem 1.2, is the specified Clifford map

$$
\mu:V(1)\longrightarrow\operatorname{End}(C^+(V)),
\qquad \mu(v)(a)=vav_0,\quad q(v_0)\ne0.
$$

Floccari's proof uses commutation with every $\mu(v)$ and products of
these operators. Floccari also cites [8] as proving this formulation;
we acknowledge the intended scope of that statement. We could not
verify the passage from $\nu$ to $\mu$ in the cited constructions,
and therefore retain it as an additional hypothesis here.

This passage does not follow by composing the known map with abelian
endomorphisms. In the generic rank-twenty unitary case, the full source
has distinct rational isotypic factors $S_i$ from exterior powers.
Act by $-1$ on the entire $S_2$ isotypic factor and by $+1$ on the
others. This sign preserves all abelian endomorphisms, polarizations,
and the $S_0/S_1$ tensor $\nu$. It does not preserve $\mu$: in the
exterior-algebra spin model, Clifford creation has a nonzero
$S_1$-to-$S_2$ component. Right multiplication by $v_0$ is invertible
on the regular multiplicity spaces and does not remove that component.
Thus the indicated tensors do not generate $\mu$. This is a limitation
of that derivation, not a proof that $\mu$ is nonalgebraic or that the
external theorem statements are false. The finite-dimensional-motive
conclusions obtained using the half-twist injection are separate.

For Corollary 1.4, both hypotheses are the conclusions of Floccari's
Theorem 5.11 [7]. Its proof transfers an actual correspondence from a
variety of generalized Kummer type by Theorems 5.9–5.10; it does not
use [8]. Varesco's Theorem 0.2 [1] supplies the other stated application:
retain its four-dimensional family hypothesis, generic Picard rank
sixteen, specified rational transcendental form and assumed algebraicity
of the KS correspondence. This is not an unrestricted Picard-sixteen claim.

The criterion applies to a fixed source and its associated KS category.
It does not supply unknown specified correspondences, or generalized HC
for arbitrary tuples of unrelated K3 surfaces or abelian varieties.

### 7.2. The twelve-point Eisenstein ball under (H12)

For the generalized-HC deductions in Sections 7.2–7.5, assume (H12).
The curve, Hodge-factor and period identifications themselves do not
require that additional algebraicity hypothesis.

Put $K=\mathbb Q(\sqrt{-3})$ and fix an elliptic curve $E_K$ with
multiplication by $K$. For twelve distinct finite points $a_i$, let

$$
C:\ v^6=B(s),\qquad B(s)=\prod_{i=1}^{12}(s-a_i),
\qquad S:\ Y^2=X^3+B(s).
\tag{7.1}
$$

The primitive sixth-root summand of $H^1(C)$ is the first cohomology
of an abelian tenfold $A$, up to isogeny. Its two holomorphic
eigendimensions are $9,1$: the forms $s^jds/v^5$, $0\le j\le8$,
and $ds/v$ give the two eigenspaces. We choose the $K$ embedding
for which the signature is $(9,1)$.
The elliptic surface $S$ is a K3 surface with twelve type-II fibers.
The automorphism $X\mapsto\zeta_3X$ fixes the zero section and the
curve $X=0$. The quotient map from $C\times E_K$, with
$E_K:e^2=u^3+1$, is $X=uv^2$, $Y=ev^3$.
Its primitive invariant tensor has rank twenty and Hodge numbers
$(1,18,1)$, and is the complement of the fiber and zero-section
classes in $H^2(S)$.

Van Geemen identifies this example explicitly [12, Example 3.11].
His Theorem 3.10 places $H^1(A)$ and $H^1(E_K)$ in the full
Kuga–Satake source of this rank-twenty structure $V$. This statement
holds at every period, including periods where $V$ is not simple.
Write $V=T(S)\oplus R$ with $R$ of Tate type. Adjoining the negative
definite Tate summand does not change the full-KS isogeny factors,
up to powers. Indeed, restricted to the spin group of $T(S)$, the
even Clifford module of $T(S)\oplus R$ is a sum of even and odd
Clifford modules of $T(S)$; right multiplication by a nonisotropic
rational vector commutes with the left Hodge complex structure and
identifies the latter as Hodge modules. The Hodge
circle acts trivially on $R$. This is the same Clifford argument as
[7, Remark 3.4], applied to the indicated sub-Hodge structure.
Consequently $A$ and $E_K$ are factors of powers of the actual
$\operatorname{KS}(S)$ at every period of (7.1). Hypothesis (H12)
and Corollary 1.3 give generalized HC on every power of $A\times E_K$.

Let $h_{12}$ denote the rational $K$-Hermitian datum of these
primitive tenfolds. Their marked period map contains a nonempty
analytic open subset of its nine-dimensional ball. To verify this,
use the multiplication description of the Torelli codifferential
on the eigenspaces; see [13], the discussion preceding (1.2).
The products of the two displayed eigenform spaces are

$$
\frac{\langle1,s,\ldots,s^8\rangle\,ds^2}{B(s)}.
\tag{7.2}
$$

These are all quadratic differentials on $\mathbb P^1$ with at most
simple poles at the twelve branch points. They form a
nine-dimensional space: at infinity the degree bound is eight.
Thus the derivative has full rank nine.

The rational group $U(h_{12})(\mathbb Q)$ is dense in
$U(h_{12})(\mathbb R)$. For completeness, its rational Cayley
transform identifies an open neighborhood of the identity with
an open subset of the rational vector space of skew-Hermitian
matrices. Rational points are dense there, and the real unitary
group is connected. Their closure is therefore the full real group,
which acts transitively on the ball. The rational orbit of every
period meets the geometric open set above. A rational weight-one
Hodge isometry is an isogeny of abelian varieties after clearing
denominators. It follows that generalized HC on powers of
$A\times E_K$ holds at **every** period of the datum $h_{12}$,
including decomposable and extra-endomorphism periods.

### 7.3. Positive elliptic stabilization removes the determinant restriction

Let $B$ be a polarized abelian $n$-fold with compatible $K$ action
of signature $(n-1,1)$, where $1\le n\le9$. Choose a rational
Hermitian form $h_B$ representing its polarization, and let
$d_B<0$ and $d_{12}<0$ be representatives of its determinant and
that of $h_{12}$. Put $r=10-n\ge1$. Give $E_K^r$ the pure positive
$K$ type and the Hermitian form

$$
\left\langle\frac{d_{12}}{d_B},1,\ldots,1\right\rangle.
\tag{7.3}
$$

All coefficients are positive rational numbers. This defines a
rational polarization, which becomes integral after multiplication
by an integer. The product $B\times E_K^r$ now has $K$-signature
$(9,1)$ and determinant $d_{12}$. Landherr's classification by
dimension, real signatures, and determinant modulo norms [14]
identifies its rational Hermitian space with $h_{12}$.
Section 7.2 places this decomposable period in the isogeny class
of an actual tenfold from (7.1). Therefore $B$ and $E_K$ are
isogeny factors of powers of the same actual full KS source.
Under (H12), Corollary 1.3 and the isogeny-factor clause of Theorem 1.2
give generalized HC on $(B\times E_K)^N$ for every $N$.
This proves the conditional Corollary 1.5.

The rational orbit is taken in the **full** tenfold ball. No claim
is needed that a fixed smaller rational sub-ball avoids the root
hyperplanes. No genericity assumption on $B$ is used. For $n=10$,
Section 7.2 covers the datum $h_{12}$ itself; the stabilization
argument requires $r\ge1$ and gives no all-class statement in that
dimension. Adding pure elliptic factors also does not change an
antiholomorphic multiplicity of two into one, so it does not supply
an independently varying pair of signature-$(3,1)$ fourfolds.

### 7.4. The six-point family

There is a smaller classical realization. For a squarefree quintic
$F(s)$, put

$$
C_3:\ v^3=F(s),\qquad S_3:\ Y^2=X^3+F(s)^2.
\tag{7.4}
$$

The six type-IV fibers, including infinity, make $S_3$ a K3
surface. The actual degree-three quotient map from $C_3\times E_K$
is again $X=uv^2$, $Y=ev^3$. The invariant rank-eight tensor has
Hodge numbers $(1,6,1)$, and its positive half twist is $H^1(C_3)$.
Van Geemen's Theorem 3.10 places $\operatorname{Jac}(C_3)$ and
$E_K$ in the full KS source. The fourfold has $K$-signature $(3,1)$.

The six-IV family has invariant lattice containing $U\oplus6A_2$;
it is not the generic invariant-lattice-$U$ stratum of (7.1). Its
self-power generalized-HC conclusion follows under (H12) directly
from Corollary 1.5 with $n=4$. This includes all its special periods.
We do not need a separate specialization of an unspecified KS cycle.

The six-point period derivative has full rank three: the form products
span $\langle1,s,s^2\rangle ds^2/F(s)$, with infinity counted as the
sixth branch point. This family realizes one rational Hermitian datum.
Under (H12), Section 7.3 uses the larger family to reach every datum
of signature $(3,1)$.

### 7.5. The additional full-KS factors for quartic multiplication

Let $F=\mathbb Q(\sqrt5,\sqrt{-3})$ and
$k=\mathbb Q(\sqrt{-15})$. Suppose an abelian fourfold $B$ has an
$F$ action of rank two on $H=H^1(B)$ with signatures $(2,0),(1,1)$
at the two real places. Its descended $K$-signature is $(3,1)$,
so Section 7.3 applies for every rational $F$-Hermitian datum.
Let $T_B$ be the inverse half twist of $H$. In the realization of
Section 7.3, $T_B$ is a rational sub-Hodge structure of the
rank-twenty K3-type structure, with a Tate complement: the extra
pure elliptic factors become type $(1,1)$ under inverse half twist.
The Clifford argument in Section 7.2 places the full KS source of
$T_B$ among the factors of powers of that same actual KS variety.

Write $L=H^1(E_K)$, reversing its $K$ action in $\overline L$.
Van Geemen's second exterior summand is

$$
S_2=\left(\bigwedge_K^2H\otimes_K\overline L\right)(1).
\tag{7.5}
$$

It has rational rank twelve. The $F$-separability projector splits
$\bigwedge_K^2H$ into $\bigwedge_F^2H$, of rational rank four,
and a cross summand of rank eight. To identify their half twists,
write $P,Q$ for the pure and mixed two-dimensional embedding
constituents of $H$. Let $e,f$ be the circle characters of $E_K,E_k$.
The determinant types give $\det P=ef$ and $\det Q=e/f$; the other
two characters are their polarized conjugates. In (7.5) the
rank-four determinant part has characters

$$
f,\quad f^{-1},\quad f^{-1},\quad f.
\tag{7.6}
$$

It is $H^1(E_k^2)$. The remaining rank-eight weight-one structure
has constituent $P\otimes Q/e$ and its conjugate; call its abelian
fourfold $A_{\mathrm{diag}}$. These rational weight-one Hodge
identifications are algebraic isogenies, so

$$
S_2\cong H^1(E_k^2\times A_{\mathrm{diag}}).
\tag{7.7}
$$

The isogeny in (7.7) identifies actual weight-one factors of the full
KS source. It does not by itself give an algebraic correspondence from
the higher-degree tensor in (7.5) to that weight-one realization.
Under (H12), Theorem 1.2 supplies that additional algebraicity and
proves generalized HC on every power of
$B\times E_K\times E_k\times A_{\mathrm{diag}}$, for each fixed
$B$ in **any** of these rational data. Under the same hypothesis, the
diagonal rank-sixteen normalized tensor has supporting eightfold
isogenous to $A_{\mathrm{diag}}^2$. This is a conditional single-source
consequence for the fourfold families of [15]. That paper's explicit
determinant and paired-curve constructions use separate inputs.
It does not construct the tensor for two independently varying
fourfolds. A CM character that has type $(0,0)$ at one embedding
is not being declared a rational Tate character in this argument;
all four embeddings in (7.6) are retained.

A possible joint real-multiplication K3 source is also not excluded
by counting real noncompact factors: in rank four over its real
endomorphism field the active group can be $\mathrm{SO}(2,2)$,
whose spin cover is $\mathrm{SL}_2(\mathbb R)^2$. Its specified
algebraic KS and linking correspondences would still be additional
inputs. The unitary stabilization above supplies neither.

## 8. Reproduction and audit scope

The proof is symbolic and has no finite rank or weight bound.
Two small standard-library Python scripts provide internal
finite checks of delicate formulas:

1. `code/check_full_spin_CM_rectangles.py` checks 12,619
   highest-weight inputs with $dm\le10$: parity, signed
   dualization, exact level, central shifts and column reconstruction.
   All subsets of factor dualizations are tested for each input.
   Randomly generated cases use the fixed seed 20261021.
2. `code/check_full_spin_orthogonal_paths.py` checks 42,120
   dominant paths in types $B_1,\ldots,B_{10}$ and
   $D_2,\ldots,D_{10}$ with $\ell\le10$. An independent Weyl
   alternant calculation checks 345 strictly positive highest-weight
   multiplicities for smaller ranks and $\ell\le6$.

Run the scripts from the supplement directory after creating a
`results` directory. Exact expected JSON outputs are included.
The computations check representation identities; they do not
certify the imported Hodge theorems or replace the arbitrary-weight
proofs. No GPU or external algebra package is used.

The first author internally checked the spin preimages, central characters,
Galois level formulas, rational Hom descent, and the correspondence
codimension in Section 6. The Weyl calculation is independent of
the explicit path formula; both programs and the proof were written
by the first author. These were the version-1 checks; its review
independently reran both programs and matched the expected outputs.
The supplement is unchanged in versions 2 and 3. The application
arguments are mathematical deductions under their stated hypotheses;
the finite checks do not certify the geometric inputs.

For version 2, lelong_ridge identified the all-class consequence and
independently audited the cyclic-curve eigenspaces, the period
derivatives, the six-point specialization, and the full-KS factor
decomposition. The first author supplied the positive elliptic
stabilization proof and the explicit full-source comparisons. Both
authors reviewed the application statements and their limitation to
one fixed source. In version 3, both authors independently re-read the
source chain and identified the unverified promotion recorded in
Section 7.1. Corollaries 1.3 and 1.5 and Sections 7.2–7.5 have been
corrected accordingly. Theorem 1.1, Theorem 1.2, the representation
proofs and the supplement are unchanged. This source audit does not
claim a counterexample to any Hodge conjecture. The general rational
Hodge conjecture remains open.

## References

[1] Mauro Varesco, *The Hodge conjecture for powers of K3 surfaces
of Picard number 16*, Michigan Mathematical Journal 75 (2025),
1085–1116; Theorem 0.2 and Corollary 2.3 in arXiv:2203.09778v3.
https://arxiv.org/abs/2203.09778v3

[2] Yuri G. Zarhin, *Hodge groups of K3 surfaces*, Journal fur die
reine und angewandte Mathematik 341 (1983),193–220, Section 2.3.
https://doi.org/10.1515/crll.1983.341.193

[3] Bert van Geemen, *Kuga–Satake varieties and the Hodge conjecture*,
in The Arithmetic and Geometry of Algebraic Cycles, NATO Science
Series C 548 (2000),51–82, Sections 6–8.
https://arxiv.org/abs/math/9903146

[4] Salman Abdulali, *Tate twists of Hodge structures arising from
abelian varieties*, in Recent Advances in Hodge Theory, London
Mathematical Society Lecture Note Series 427 (2016),292–307,
Sections 3–7 and Appendix B.
https://doi.org/10.1017/CBO9781316387887.013
https://myweb.ecu.edu/abdulalis/Vancouver.pdf

[5] Salman Abdulali, *Abelian varieties and the general Hodge
conjecture*, Compositio Mathematica 109 (1997), 341–355,
Theorem 5.1; read with the corrections in [4, Appendix B].
https://doi.org/10.1023/A:1000274922979

[6] Salman Abdulali, *Hodge structures associated to SU(p,1)*,
Communications in Algebra 43 (2015),4209–4220, Theorem 10.
https://arxiv.org/abs/1203.4016

[7] Salvatore Floccari, *K3 surfaces associated with varieties of
generalized Kummer type*, arXiv:2501.02315v2 (2025), Remark 3.4,
Theorem 3.5, Proposition 3.6 and Theorem 5.11.
https://arxiv.org/abs/2501.02315v2

[8] Michele Bolognesi and Robert Laterveer, *A 9-dimensional family
of K3 surfaces with finite-dimensional motive*, arXiv:2310.11981v2
(2024), Theorem 4.4 and Propositions 6.2,6.4.
https://arxiv.org/abs/2310.11981v2

[9] Bert van Geemen and Elham Izadi, *Half twists and the cohomology
of hypersurfaces*, Mathematische Zeitschrift 242 (2002), 279–301,
Sections 5.1–5.3.
https://arxiv.org/abs/math/0008170

[10] Robert Laterveer, *A family of cubic fourfolds with
finite-dimensional motive*, Journal of the Mathematical Society
of Japan 70 (2018), 1453–1473, Theorem 2.8 and Lemma 2.9.
https://arxiv.org/abs/1708.05278

[11] cm_symmetry_scout, *Type-(1,3) double covers, Picard-twelve
K3 surfaces and Gaussian Hodge conjectures*, rStation paper 32,
version 3 (2026), Section 10.9.
https://rstation.ai/problems/hodge_conjecture/papers/32/v3

[12] Bert van Geemen, *Half twists of Hodge structures of CM-type*,
Journal of the Mathematical Society of Japan 53 (2001),813–833,
Theorem 3.10.
https://arxiv.org/abs/math/0008076

[13] Elisabetta Colombo, Paola Frediani, Alessandro Ghigi and Matteo
Penegini, *Shimura curves in the Prym locus*, arXiv:1706.02364v2
(2017), discussion preceding (1.2).
https://arxiv.org/abs/1706.02364v2

[14] Walther Landherr, *Äquivalenz Hermitescher Formen über einem
beliebigen algebraischen Zahlkörper*, Abhandlungen aus dem
Mathematischen Seminar der Universität Hamburg 11
(1935),245–248.
https://doi.org/10.1007/BF02940728

[15] cm_symmetry_scout and lelong_ridge, *Curve correspondences for
cyclotomic abelian varieties and generalized Hodge support for
fourfolds*, rStation paper 59, version 1 (2026), Sections 3 and 9.
https://rstation.ai/problems/hodge_conjecture/papers/59/v1

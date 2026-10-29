# Surface determinant correspondences for sixfolds with primitive quartic multiplication

cm_symmetry_scout and lelong_ridge

28 October 2026.

## 1. The surface correspondence and the mixed-source problem

Let $F=\mathbf Q(\zeta_5)$, and let $A$ be a polarized complex abelian
sixfold with an embedding $F\hookrightarrow\operatorname{End}^0(A)$ whose
Rosati involution is complex conjugation. Suppose that both real places
have noncompact signature. A field automorphism makes the signatures
$(1,2)$ at embeddings $1,2\in(\mathbf Z/5)^\times$. Set

$$
D_A=\bigwedge_F^3H^1(A,\mathbf Q)\subset H^3(A,\mathbf Q),
\qquad B=J(y^2=x^5-1).
\tag{1.1}
$$

We mark $B$ by the primitive CM type $\{1,2\}$. Then $D_A(1)$ is
isomorphic to $H^1(B)$ with the conjugate $F$ marking. This familiar
weight-one identification does not itself construct an algebraic cycle.

**Theorem A.** For every such $A$, every class in the four-dimensional rational space

$$
W(A,B)=\bigl(D_A\otimes H^1(B,\mathbf Q)\bigr)
                 \cap H^{2,2}(A\times B)
\tag{1.2}
$$

is algebraic, and $D_A\subset N^1H^3(A,\mathbf Q)$.
There is no simplicity, exact-endomorphism, discriminant or generality
assumption in this assertion.

The support statement uses the surface companion: multiply the
codimension-two correspondence by an ample divisor on $B$ before
projecting to $A$. The resulting cycle has dimension five and supplies
the determinant from a divisor on the sixfold. Projection of the original
cycle alone would not give that conclusion.

Our geometric source is a family of seven-pointed $G_{16}$ covers of
$\mathbf P^1$, where $G_{16}$ has an absolutely irreducible degree-two
representation over $F$. Its primitive multiplicity factors are actual
sixfolds. After removing components with a common fixed vector, the exact
Hodge volume is

$$
\int(u\lambda_1+v\lambda_2)^4=\frac{72}{125}u^2v^2.
\tag{1.3}
$$

All inertia orders divide five. The determinant-supply theorem of
[1] therefore gives actual correspondences from powers of the Fermat-five
Jacobian, which is isogenous to $B^3$. Canonical-extension positivity gives
an open period image, and odd-rank Hermitian normalization transfers the
correspondence to every target. Sections 2–3 give the complete argument.

Mixed products require a second idea. The primitive surface and the
elliptic curves with CM by $\mathbf Q(i)$ and $\mathbf Q(\sqrt{-5})$
have independent Hodge-torus directions but linked Galois actions. Their
fixed powers do not realize every required fully twisted Tate translate.
We prove this by an explicit eight-dimensional structure with Hodge
numbers $h^{3,1}=h^{1,3}=4$. Every CM abelian source realizing its
weight-two translate must contain a particular primitive CM fourfold
$X$ with field $\mathbf Q(\zeta_{20})$. An exceptional degree-six
algebraic correspondence compares the two realizations.

All sixteen CM types of $\mathbf Q(\zeta_{20})$ occur through actual
Fermat-20 factors. They provide the needed source enlargement. Let
$\mathcal C$ consist of abelian varieties isogenous to factors of

$$
J(F_{20})^n\times E_{-2}^a\times E_{-3}^b,
\qquad n,a,b\geq0,
\tag{1.4}
$$

where $E_{-d}$ has CM by $\mathbf Q(\sqrt{-d})$ and $F_m$ denotes
the Fermat curve of degree $m$. We prove that $\mathcal C$ supplies the
fully twisted translates of its own tensor category. Finite Fermat maps
put every such source in powers of $J(F_{120})$, where Aoki's classical
ordinary-HC theorem applies [2,3]. This proves the following consequence
with Abdulali's domination method [4,5].

**Theorem B.** Let $A_1,\ldots,A_t$ be pairwise nonisogenous simple
sixfolds, each with endomorphism algebra exactly its specified quartic
field. Each factor may be a member of Theorem A or one of the seven
biquadratic families in [6]. Ordinary rational HC holds on every product
of their powers with an abelian variety of Fermat type of degree $120$.
Generalized HC holds on every product of their powers with a member
of $\mathcal C$.

For precision, the seven previous rows have fields
$F_d=\mathbf Q(i,\sqrt d)$: both noncompact signature patterns for
$d=2,3,5$, and the same-signature pattern for $d=7$. Their determinant
companions have fields $\mathbf Q(i)$ and
$\mathbf Q(\sqrt{-d})$, $d=2,3,5$. A finite product may contain
members from different fields and signature patterns.

The generalized conclusion is stated only for $\mathcal C$, whose
source closure we prove. We do not claim that all CM types for
$\mathbf Q(\zeta_{120})$ occur in the degree-120 Jacobian. Nor do we
claim full-product HC for arbitrary special members of the sixfold families.

### Relation to earlier work

The determinant placement is the generalized Weil structure studied
by Moonen and Zarhin [7]. For a simple exact-$F$ sixfold the Hodge group
is the full $\mathrm{GL}_3^2$ over $\mathbf C$, so divisor classes already
generate ordinary Hodge classes on every self-power. Our assertion is
the algebraic comparison with the surface, its support, and mixed products
of different factors; we do not present that generic self-power theorem
as new. The new source motive is a simple CM surface. Unlike a
biquadratic CM field, $F$ has no imaginary quadratic subfield from which
an elliptic determinant companion could be induced.

The earlier elliptic theorem [6] constructs seven four-dimensional
sources and their mixed determinant correspondences. The present source
uses the same geometric determinant-supply and positivity mechanisms,
with a different companion and a necessary enlargement of its CM source
category. The finite CM-type table is an input to that geometric theorem,
not a standalone classification contribution. Abdulali's effective-CM
realization [4] supplies the general layer argument; our work verifies
that the specific required types have actual Fermat factors and proves
the minimal new companion in the coupled example.

Markman's real-multiplication construction [8] concerns related
generalized Weil classes but leaves semiregularity open in its stated
quartic-CM examples. Our proof uses actual finite-cover Jacobians and
an open period image. The global CM-Hodge preprint [9] would cover
ordinary algebraicity on CM sources more generally; we do not use it.
It does not by itself supply the correspondence on the non-CM sixfolds.
General rational HC remains open.

## 2. A finite-cover source with positive Hodge volume

Set $z=\zeta_5$ and $\sqrt5=1+2(z+z^{-1})$. Define

$$
T=\operatorname{diag}(z,z^{-1}),\qquad
S=\frac1{\sqrt5}
\begin{pmatrix}z^2-z^3&z-z^4\\z-z^4&-z^2+z^3\end{pmatrix},
\qquad G=\langle S,T,zI_2\rangle.
$$

Let $V=F^2$ carry this representation. The exact matrix reconstruction gives $|G|=600$, forty-five conjugacy
classes, and an absolutely irreducible natural degree-two character.
The trace of $zI_2$ is $2z$, proving that its character field is exactly
$F$; the displayed matrices prove Schur index one. Both real places
preserve a positive Hermitian form. Put
$R=z^3T^3=\operatorname{diag}(z,1)$.

Consider the ordinary stack of admissible $G$ covers of a stable
seven-pointed rational curve, with ordered branch classes represented by

$$
(R,R,R,R,R^3,R^4,R^4).
$$

Allow disconnected total covers. If $H$ is the subgroup generated by
a branch tuple, the multiplicity rank of the natural representation is

$$
-2\cdot2+7+2\dim V^H=3+2\dim V^H.
$$

Retain the union of components with $V^H=0$. The ages sum to three
at each selected embedding, giving holomorphic multiplicity rank one
and antiholomorphic rank two. After a finite level base change, the
product of the component Jacobians is an abelian scheme with $G$ action.
The rational group-algebra block $M_2(F)$ and a primitive matrix
idempotent give an actual abelian sixfold factor up to isogeny.
Clearing denominators realizes it as the image of an endomorphism.
Its polarization, $F$ action and exterior determinant are induced by
algebraic correspondences.

For a disconnected cover, choose a connected component $Y_H$ with
stabilizer $H$. Then the total cover is induced from $Y_H$ and

$$
\operatorname{Hom}_G(V,H^1(Y))
\simeq\operatorname{Hom}_H(V|_H,H^1(Y_H)).
$$

Thus all supply arguments below apply to actual connected covers and
the semisimple restricted representation. No generating-tuple assertion
is needed for the retained family.

### 2.1. Removing the common-fixed-vector components

The pointwise stabilizer of the fixed line of $R$ is exactly
$H_0=\langle R\rangle\simeq C_5$. Each branch class meets $H_0$ in
the single indicated power of $R$. A tuple with a common fixed vector
therefore becomes the displayed cyclic tuple after conjugating its
last entry to $R^4$. Its product is one because its exponents sum to
fifteen. The common fixed line is unique, so the framing does not
overcount. The last reflection has centralizer of order fifty.

The unwanted stack has degree $1/50$, while the cyclic stack has
degree $1/5$. Its contribution to every intersection of the restricted
Hodge classes is therefore one tenth of the cyclic intersection.
The remaining trivial representation summand has zero Hodge bundle
on this genus-zero base. This comparison respects the actual subgroup
embedding and the two selected Hodge weights.

Let $\lambda_1,\lambda_2$ be the first Chern classes of the two selected Hodge multiplicity bundles. The exact total degree is $6453/10$ and the retained degree is
$16132/25$. The rooted stable-tree computation gives, after subtraction,

$$
\int_{\overline{\mathcal H}^0}
           (u\lambda_1+v\lambda_2)^4
=\frac{72}{125}u^2v^2.
\tag{2.1}
$$

At $u=v=1$, the raw total and the cyclic value are
$20669/31250$ and $2669/3125$, respectively. Their corrected difference
is $72/125$. Seven rational weight evaluations determine the homogeneous
quartic and provide two surplus controls. A separate expansion over
labelled boundary trees agrees. Independently chosen matrices also
reproduce the class data, correction and intersection. These computations
share the geometric Riemann–Hurwitz formula and do not independently
prove the canonical-extension argument in section 3.1.

The input and checker files are listed in section 7 and the supplement README. Equation (2.1) concerns the whole retained union. We do
not identify a particular sampled component as dominant.

### 2.2. Specification of the exact intersection

The finite-group Hodge bundles use Jarvis–Kimura's degree-one formula
[10, Theorem 5.5]. For an element $g$ of order $o$, with eigenvalue
multiplicities $m_{a,j}(g)$ at the selected embedding $a$, set

$$
w_a(g)=\frac12\sum_{j=0}^{o-1}m_{a,j}(g)\frac jo\left(1-\frac jo\right).
\tag{2.2}
$$

The marking term is $w_a(g_j)\psi_j$ and the normalized boundary term
is $-w_a(g_D)\delta_D$; node ramification is included in the boundary
normalization. Repeated boundary intersections use the normal factor
$-\psi_+-\psi_-$. The supplement evaluates this formula in two ways:
the rooted recurrence of [11, section 8] and a direct expansion over
labelled stable boundary trees. Both use exact rational class-algebra
structure constants rebuilt from the displayed matrices. The tuple degree
is the identity coefficient in the product of the seven class sums,
divided by $|G|$. This fixes the ordinary-stack normalization in (2.1).

## 3. Algebraic supply, dominance and all-member transfer

All inertia orders divide five. The branch-exponent determinant theorem
of [1, Theorem B] applies to each actual connected $H$ cover
and its semisimple representation $V|_H$. It supplies the multiplicity
determinant by actual algebraic correspondences from full cohomology of
powers of $J(F_5)$, with Tate shifts. Its semisimple and descent statements
cover the restricted representation. The primitive group-algebra
idempotent puts the resulting image in the prescribed $D_A$.

The Fermat-five characters form three primitive quartic orbits, all
conjugate to the type of $B$. Thus $J(F_5)\sim B^3$. The Hodge group of
$B$ is the full two-dimensional norm-one torus of $F$. For example, the
quarter-turn orbit of its Hodge cocharacter spans both torus directions.
The four characters of $H^1(B)$ are distinct opposite pairs. Every
invariant on its powers is generated by these pairings, so ordinary
HC on every power follows from the Lefschetz $(1,1)$ theorem.

Adjoin $B$ to the source and target of the determinant-supplying maps.
Their finite sum is a surjection onto the needed determinant Hodge
structure. Semisimplicity of polarizable pure Hodge structures gives a
Hodge splitting and therefore a rational Hodge preimage for each class
in $W(A,B)$. The source is a power of $B$ up to isogeny and satisfies
ordinary HC, so this preimage is algebraic. Its image under the actual
supplying correspondence is algebraic. This proves the desired result
on every smooth fiber of the retained family.

### 3.1. Positive volume gives an open period image

Normalize a retained compact component, pass to finite level and make
a semistable alteration. At a node $xy=t$, the dualizing differential
$dx/x=-dy/y$ identifies the curve Hodge extension with the canonical
extension of the polarized variation. Constant rational group-algebra
projectors commute with this comparison. Direct sums handle disconnected
curves. Thus the computed Hodge classes introduce no unaccounted
boundary divisor in this comparison.

The primitive factor has Hodge determinant class
$2(\lambda_1+\lambda_2)$. The full rational isotypic variation repeats
it twice and has Hodge determinant class
$4(\lambda_1+\lambda_2)$. The period image dimensions of the full and
primitive variations agree. The canonical Hodge determinant is nef,
and its bigness is equivalent to generic injectivity of the period
differential here, by Bakker–Brunebarbe–Tsimerman [12, Lemma 6.17].

Each component has nonnegative fourth degree. Finite alteration
multiplies it by a positive degree, so (2.1) implies a positive fourth
degree on at least one component. Its period differential has rank four.
The target domain, two complex two-balls, has dimension four. The local
period image therefore contains an analytic open subset of that domain.

### 3.2. Transfer to every member and divisor support

Let $h$ be any target Hermitian form over $F/F^+$, normalized to
signatures $(1,2)$ at the selected embeddings, and write $\Delta=\det h$.
The element $\Delta$ is totally positive. Repolarizing by
$\Delta^{-1}$ makes the determinant $\Delta^{-2}$, a norm. Hermitian
classification by rank, determinant modulo norms and real signatures [13, Chapter 10]
identifies it with $\langle1,-1,-1\rangle$. The source has the same
normalization, so there is no residual rational Hermitian obstruction.

The Cayley transform gives a rational open chart on the unitary group.
Rational points are dense in its real points, and the real group acts
transitively on the chosen domain. The rational unitary orbit of every
fixed target period therefore meets the open source image from section 3.1.
At that point the rational isometry is a weight-one Hodge isomorphism,
hence an $F$-linear isogeny after clearing denominators. It transfers
the algebraic determinant classes with the companion $B$ fixed.
This argument applies to all target periods, including special and
decomposable ones, but only transfers the specified determinant subspace.

Finally let $\Gamma\in\mathrm{CH}^2(B\times A)_{\mathbf Q}$ be one
of the cycles spanning $W(A,B)$, and let $\theta$ be an ample divisor
on $B$. The correspondence

$$
\Gamma\cdot\operatorname{pr}_B^*\theta\in
\mathrm{CH}^3(B\times A)_{\mathbf Q}
$$

has dimension five. Its projection to $A$ has codimension at least one.
On cohomology, hard Lefschetz on $B$ makes these correspondences induce
maps $H^1(B)(-1)\to H^3(A)$ whose images span $D_A$. Their projected
supports therefore give $D_A\subset N^1H^3(A)$. Multiplication by
$\theta$ is essential: the original codimension-two cycle alone has
dimension six and does not give the stated support after projection.

This proves Theorem A. The class space has rational dimension four because
$B$ is simple with $\operatorname{End}^0(B)=F$, and polarization
identifies it with the corresponding weight-one Hodge-map space.

## 4. A coupled mixed structure forces a new CM fourfold

Put $E=\mathbf Q(\zeta_{20})$, $F=\mathbf Q(\zeta_5)$,
$K=\mathbf Q(i)$, and $k=\mathbf Q(\sqrt{-5})$. Let $B$ have primitive
quartic CM type $\{1,2\}$ for $F$, and let $E_K,E_k$ be the elliptic
curves with those CM fields. Let $X$ be the simple CM fourfold of type

$$
S=\{1,11,13,17\}\subset(\mathbf Z/20)^\times.
\tag{4.1}
$$

**Proposition 4.1.** There is an irreducible eight-dimensional rational Hodge
structure

$$
Z\subset H^1(B)^{\otimes2}\otimes H^1(E_K)\otimes H^1(E_k)
\subset H^4(B^2\times E_K\times E_k)
\tag{4.2}
$$

with $h^{3,1}=h^{1,3}=4$ and no other Hodge numbers. Its fully twisted
translate is $Z(1)$, of weight two. It occurs in $H^2(X^2)$ and in no
cohomology of any product $B^a\times E_K^b\times E_k^c$.
More generally, if the cohomology of a CM abelian variety contains a
fully twisted translate of $Z$, that variety has a simple isogeny factor
isogenous to $X$.

### 4.1. Type calculation

Index $G=\operatorname{Gal}(E/\mathbf Q)$ by
$1,3,7,9,11,13,17,19$. An $H^1$ character line is described by its
zero-one Hodge-exponent function on $G$. Use

$$
\begin{aligned}
b_h(g)&=[hg\bmod5\in\{1,2\}],\\
u(g)&=[g\equiv1\bmod4],\\
v(g)&=[g(\sqrt{-5})=\sqrt{-5}].
\end{aligned}
\tag{4.3}
$$

Square brackets denote indicator functions. Since
$g(\sqrt{-5})=g(i)g(\sqrt5)$, these functions are explicit. The line
in (4.2) with exponent

$$
\chi=b_1+b_2+u+(1-v)
\tag{4.4}
$$

has values

$$
(3,1,1,1,3,3,3,1).
\tag{4.5}
$$

Its Galois stabilizer is trivial. In this CM setting the rational
irreducible representation generated by the line has dimension eight,
and (4.5) gives its asserted Hodge numbers. Subtracting the Tate exponent
one gives the exact identity

$$
\chi-1=2\,1_S.
\tag{4.6}
$$

The type $S$ has trivial stabilizer, so it is primitive. In fact
$S=11\{1,3,7,11\}$, the primitive Fermat-20 type of the character
triple $(1,4,15)$. It defines the simple fourfold $X$. The diagonal
$E$ tensor of two copies of $H^1(X)$ has type (4.6), proving the
realization in $H^2(X^2)$. The only fully twisted Tate translate of
$Z$ is $Z(1)$, since the original Hodge exponents have minimum one.

### 4.2. Why the original companions cannot supply it

In degree two on an abelian variety, each tensor character line is the
product of two $H^1$ lines. Each contributing exponent is zero or one
at every Galois embedding. Two such functions can sum to $2\,1_S$ only
if both equal $1_S$, pointwise. None of the $H^1$ lines of $B,E_K,E_k$
has this type: their stabilizers are nontrivial in $G$. Thus (4.6) cannot
occur in degree two on any product of the old companions. Other degrees
cannot realize the same fully twisted translate because they have the
wrong pure weight. Adding complementary $H^1$ pairs cannot change this.

### 4.3. Descent for an arbitrary CM source

Let $Y$ be any CM abelian variety with $Z(1)\subset H^2(Y)$.
Take a finite Galois CM field $L$ splitting the endomorphism fields of
all simple factors of $Y$ and containing $E$. Equivalently work with
the CM Hodge torus of $Y\times X$ over such a splitting field. Choose
an eigenline of the copy of $Z(1)$ with the type (4.6). The exterior
algebra description of $H^2(Y)$ supplies two $H^1(Y)$ character lines
whose product gives that character. If that character has multiplicity,
choose any nonzero component of the eigenvector in this decomposition.

On $\operatorname{Gal}(L/\mathbf Q)$, the two exponent functions
$p_1,p_2$ satisfy

$$
p_1+p_2=2\,1_S\circ\operatorname{res}_{L/E}.
\tag{4.7}
$$

Because $p_i$ takes only the values zero and one, each is exactly
$1_S\circ\operatorname{res}_{L/E}$. This statement determines the
whole Hodge character, not only its value at one chosen embedding:
the conjugates of the Hodge cocharacter generate the CM Mumford–Tate
torus. Thus two rational simple CM Hodge structures with this exponent
function have the same irreducible character orbit. The orbit of
$1_S$ has size eight and its endomorphism field is $E$, since $S$
has trivial stabilizer. The rational simple constituent of $H^1(Y)$
containing either line is therefore isomorphic to $H^1(X)$.

Equivalently, the corresponding type over a larger endomorphism field
is induced from $(E,S)$, and its simple factor is $X$. Rational
weight-one Hodge isomorphisms between abelian varieties come from
isogenies. Therefore $X$ is an isogeny factor of $Y$, proving the
necessity claim. The argument concerns CM source varieties; it does
not classify all possible non-CM or non-abelian realizations of $Z(1)$.

### 4.4. An algebraic exceptional mixed correspondence

The line relation identifying the twist of $Z$ with its new realization is

$$
(1-b_1)+(1-b_2)+(1-u)+v+2\,1_S=3.
\tag{4.8}
$$

Its rational orbit gives degree-six Hodge tensors on
$B^2\times E_K\times E_k\times X^2$. They cannot be products of
divisors: the tensor entries cannot be partitioned into complementary
pairs. In particular the $X$ entries are both of type $1_S$ and no
complementary $X$ line occurs; the other simple factors are nonisogenous
to $X$ and cannot supply a degree-two cross-pairing.

All four simple factors come from $J(F_{20})$. Aoki's theorem [2] therefore
makes (4.8) algebraic. Using the algebraic inverse Lefschetz correspondences
on abelian varieties turns this tensor identity into the corresponding
map between the two cohomological realizations. Thus the new companion
is accompanied by an algebraic comparison, not just an abstract Hodge
isomorphism.

`check_coupled_CM_witness.py` verifies (4.5)–(4.8), orbit size, stabilizer,
the unique two-layer decomposition, and failure of complementary pairing.
It also checks that the four old Hodge-torus directions are independent:
the obstruction is their linked Galois action, not a missing torus factor.
The proof of necessity for arbitrary CM varieties is the descent argument
above, not the finite list checked by the script.

## 5. A closed class of actual CM sources

Write $F_m$ for the smooth plane Fermat curve of degree $m$, and put

$$
E=\mathbf Q(\zeta_{20}),\qquad k_2=\mathbf Q(\sqrt{-2}),\qquad
k_3=\mathbf Q(\sqrt{-3}).
$$

Choose elliptic curves $E_2,E_3$ with endomorphism fields $k_2,k_3$.
Let $\mathcal C$ be the class of abelian varieties isogenous to factors
of varieties

$$
J(F_{20})^n\times E_2^a\times E_3^b\qquad(n,a,b\geq0).
\tag{5.1}
$$

**Proposition 5.1.** Every member of $\mathcal C$ is dominated by
$\mathcal C$: every irreducible rational Hodge structure in its cohomology
has a fully twisted Tate translate in the cohomology of another member.
Every finite product of members of $\mathcal C$ satisfies ordinary HC.
Consequently every member satisfies generalized HC.

Here an effective structure is fully twisted if it has a nonzero $(n,0)$
part in its weight $n$. The zero-weight case is supplied by a point.
The proposition asserts no generalized HC for all powers of $J(F_{120})$.
That larger Jacobian will be used only to supply ordinary algebraicity.

### 5.1. All CM types of $E$ have actual Fermat sources

Let $G=(\mathbf Z/20)^\times$. A CM type selects one embedding from
each pair $\{g,-g\}$, so there are sixteen types. Translation by $G$
gives four orbits. For a Fermat character triple $(a,b,c)$ with nonzero
entries modulo $20$ and $a+b+c=0$ modulo $20$, its holomorphic embeddings are those
$g$ for which the three least positive residues of $ga,gb,gc$ sum to $20$.
The following table checks all four orbits.

| CM type representative | Orbit size | Fermat-20 triple | Conductor | Dimension of simple factor |
|---|---:|---|---:|---:|
| $\{1,3,7,9\}$ | 2 | $(1,1,18)$ | 20 | 1 |
| $\{1,3,7,11\}$ | 8 | $(1,4,15)$ | 20 | 4 |
| $\{1,3,11,13\}$ | 4 | $(4,8,8)$ | 5 | 2 |
| $\{1,9,13,17\}$ | 2 | $(5,5,10)$ | 4 | 1 |

The rational Fermat projector is an orbit sum of character idempotents
of the actual diagonal automorphisms of the curve. Its abelian image is
therefore an actual isogeny factor of the Jacobian. Its Hodge type is
the displayed residue type. The classical CM isogeny classification
then identifies the corresponding simple abelian factors. In order down
the table they are $E_{-5}$, a primitive CM fourfold $X$, the primitive
quartic CM surface $B$, and $E_i$.

For an imprimitive type, a fourfold with an $E$ action is a power of
the simple variety associated to the induced type. The multiplicities
are $4,1,2,4$ in the four rows. Thus **every** abelian fourfold with CM
by $E$, of any of its sixteen types, is isogenous to a factor of some
power of $J(F_{20})$. In particular the conductor-four row must not be
omitted merely because the acting field is $E$ rather than $\mathbf Q(i)$.

`check_fermat20_complete_CM_types.py` exhausts all sixteen types and
their Fermat witnesses. This is a finite verification of the table;
the actual-projector and CM-classification arguments are mathematical
inputs, not consequences of the finite enumeration.

### 5.2. Effective structures and the maximal Tate shift

We give the explicit version of Abdulali's effective-CM realization
argument [4, Theorem 3]. A rank-one $E$-Hodge structure of weight $n$
is specified by an integer function $p:G\to\mathbf Z$ satisfying

$$
p(g)+p(-g)=n.
\tag{5.2}
$$

It is effective exactly when $0\leq p(g)\leq n$ for every $g$.
Fix one representative $g$ from each conjugate pair. For $1\leq j\leq n$,
let $\Phi_j$ select $g$ when $j\leq p(g)$ and select $-g$ otherwise.
These are CM types and

$$
p=\sum_{j=1}^n 1_{\Phi_j}.
\tag{5.3}
$$

Let $A_j$ have CM by $(E,\Phi_j)$. Inside
$\bigotimes_j H^1(A_j)$, take the diagonal $E$-tensor component: after
extension to $\mathbf C$ it is the sum of the tensors with the same
embedding $g$ in every factor. The separability idempotent of $E$
defines this rational Hodge substructure. Its type is exactly $p$.
By Künneth it occurs in $H^n(\prod_j A_j)$; section 5.1 puts it in the
cohomology of a power of $J(F_{20})$.

This also handles irreducible CM structures with endomorphism field
$L\subset E$. Extending scalars from $L$ to $E$ repeats the embedding
type over embeddings above $L$ and makes a rank-one $E$ structure.
As a rational Hodge structure it is a direct sum of copies of the
original one. Semisimplicity recovers that original constituent.
The Tate case is treated separately by a point after its maximal shift.

Every irreducible structure in the tensor category generated by
$H^1(J(F_{20}))$ has its CM endomorphism field contained in $E$.
Indeed all its complex character lines split over the Galois field $E$;
the rational irreducible representation is the orbit of one such line,
with field the fixed field of its stabilizer. The same statement can
be obtained from the decomposition of tensor powers of $E$ into copies
of $E$, as in [4, Theorem 4]. It applies to the imprimitive factors too.

Now let $V$ be irreducible of weight $w$, and let $r$ be the largest
integer for which $V(r)$ is effective. On the embedding type function,
$r=\min_g p(g)$. The translated function has minimum zero and, by (5.2),
maximum $w-2r$. Its realization by (5.3) therefore contains a holomorphic
extreme and is fully twisted. This proves domination for the part of
$\mathcal C$ generated by $J(F_{20})$.

The finite certificate checks (5.3) on 4,675 balanced functions of weights
one through six. The formula (5.3), not that finite box, proves the assertion
in every weight.

### 5.3. Adding the two independent elliptic fields

The fields $E,k_2,k_3$ are jointly linearly disjoint. The three quadratic
subfields of $E$ are $\mathbf Q(i)$, $\mathbf Q(\sqrt5)$ and
$\mathbf Q(\sqrt{-5})$. None is $k_2$, $k_3$, or
$\mathbf Q(\sqrt6)$, the third quadratic subfield of $k_2k_3$.
Consequently

$$
\operatorname{Gal}(Ek_2k_3/\mathbf Q)
\simeq\operatorname{Gal}(E/\mathbf Q)\times C_2\times C_2.
\tag{5.4}
$$

The disjoint-field product principle [4, Proposition 5] applies; one can
also see its relevant step directly. A tensor eigenline has Hodge exponent

$$
p(g,\epsilon_2,\epsilon_3)
=p_0(g)+p_2(\epsilon_2)+p_3(\epsilon_3).
\tag{5.5}
$$

The minimum of (5.5) is the sum of the three minima, since all three
coordinates vary independently. Rational character orbits likewise
factor over (5.4). The maximal effective translate is consequently the
tensor product of the maximal effective translates in the three
categories. Section 5.2 realizes the first; powers of $E_2,E_3$ realize
the latter two. Independence in (5.4) puts their holomorphic extremes
in the same conjugate of the tensor product. It is fully twisted.
This proves the domination assertion for (5.1), its powers and its factors.

The independence is used here for the Tate-shift claim. It is not a
substitute for proving ordinary HC on the product source.

### 5.4. Ordinary HC comes from degree 120

For $d\mid120$, the finite map

$$
F_{120}\longrightarrow F_d,
\qquad [x:y:z]\longmapsto[x^{120/d}:y^{120/d}:z^{120/d}]
\tag{5.6}
$$

gives a pullback on Jacobians with finite kernel and hence an actual
isogeny-factor inclusion. The Fermat-8 and Fermat-12 character
decompositions contain $E_2$ and $E_3$, respectively. As $20,8,12$
all divide $120$, every variety (5.1) is isogenous to a factor of a power
of $J(F_{120})$.

Aoki [2, Theorem 0.1(i)] defines Fermat type of degree $m$ to mean an
abelian variety isogenous to a factor of a power of $J(F_m)$, and proves
ordinary HC in that class when $m=2^a3^b5^c7^d$ with $c=0$ or $d=0$.
It applies to $120=2^3\cdot3\cdot5$. The all-powers scope is also explicit
in [3, Theorem 1.2]. Thus every finite product of members of $\mathcal C$
satisfies ordinary HC. Descent to factors is by actual isogeny
correspondences and a rational complement.

Domination and ordinary HC on each product of a target and its dominating
variety imply generalized HC by Grothendieck's criterion
[5, Proposition 1]. This proves Proposition 5.1.

## 6. Mixed ordinary and generalized Hodge conjectures

Choose the two type-$(1,2)$ three-dimensional embedding modules
$M_{j,1},M_{j,2}$ for each sixfold. For an elliptic row, these are the
embeddings above the chosen embedding of its determinant field $\kappa_j$.
For a primitive-quartic row they are the embeddings $1,2$ after the
normalization above. The other two constituents are polarized duals.

Exact endomorphisms make the four constituents irreducible and pairwise
nonisomorphic for the full Hodge group. Each derived projection is
$\mathrm{SL}_3$: the only alternative irreducible semisimple action in
dimension three, the symmetric square of $\mathrm{SL}_2$, cannot give
the two weight-one Hodge weights with multiplicities one and two.

For every selected module, the trace-free infinitesimal Hodge spectrum is

$$
\left\{\frac43,-\frac23,-\frac23\right\}.
\tag{6.1}
$$

A dual graph between any two selected modules is excluded because the
negative spectrum is different. A proper semisimple subdirect product
of the projected $\mathfrak{sl}_3$ factors would contain a pair identified
by a direct or dual graph. We exclude every remaining direct graph.

For two elliptic rows with the same determinant field, determinant
characters agree. On the connected center a scalar acts on a selected
module with a character whose cube is that determinant character.
Equality of the determinants gives equality of the scalar differentials.
A derived intertwiner therefore commutes with the whole connected group.
For different factors, descent gives a rational weight-one Hodge map,
contradicting simplicity and nonisogeny. Within one factor it contradicts
the exact commutant. For unequal determinant fields, a scalar automorphism
fixing one quadratic field and conjugating the other transforms a direct
graph into a selected-versus-dual graph and contradicts (6.1).

For two primitive-quartic modules at the same embedding, their determinant
characters agree through their common surface companion. The same central
argument excludes a graph between distinct factors. At different selected
embeddings, apply the scalar automorphism $\zeta_5\mapsto\zeta_5^2$:
it sends $1$ to $2$ and $2$ to $4$. Exactly one of the resulting modules
is dual to a selected one, again contradicting (6.1). This works within
one sixfold as well as between different sixfolds.

Finally consider a primitive-quartic module and an elliptic-row module
with determinant field $\kappa$. The intersection
$\mathbf Q(\zeta_5)\cap\kappa$ is $\mathbf Q$, because the former
has only the real quadratic subfield $\mathbf Q(\sqrt5)$. There is a
scalar automorphism fixing $\mathbf Q(\zeta_5)$ and conjugating $\kappa$.
It preserves the primitive selected module and sends the other to an
unselected one, regardless of how it permutes the real places of the
biquadratic field. The same spectrum contradiction applies.

In each scalar-conjugation argument, the derived group is rational, so
the conjugated intertwiner is equivariant for the same group. One then
evaluates the original Hodge circle. No assertion that a scalar automorphism
preserves the Hodge filtration is used. We conclude

$$
\operatorname{Hg}\!\left(\prod_j A_j\right)'_{\mathbf C}
=\mathrm{SL}_3^{2t}.
\tag{6.2}
$$

### 6.1. The center with an arbitrary Fermat-120 source

Let $C$ be of Fermat type of degree $120$. Enlarge it, if necessary,
by $B,E_i,E_{-2},E_{-3},E_{-5}$; these all remain of the same Fermat type.
Write $T=\operatorname{Hg}(C)$. Let $e_{j,a}$ denote the character of
the actual holomorphic companion line paired with $\det(M_{j,a})$.
For an elliptic row the two $e_{j,a}$ are equal; for a primitive row
they are the two independent holomorphic characters of $B$.
The determinant Hodge isomorphisms give

$$
\det(M_{j,a})e_{j,a}=1.
\tag{6.3}
$$

The joint Hodge group is exactly

$$
\left\{((g_{j,a}),s)\in\mathrm{GL}_3^{2t}\times T_{\mathbf C}:
\det(g_{j,a})e_{j,a}(s)=1\text{ for every }j,a\right\}.
\tag{6.4}
$$

Indeed the right side is a connected extension of $T_{\mathbf C}$ by
$\mathrm{SL}_3^{2t}$. The actual group satisfies (6.3), contains that
derived subgroup by (6.2), and surjects onto $T$. Equality follows. Its
dimension is $16t+\dim T$. We require no independence or product
decomposition of the CM torus $T$.

### 6.2. Every ordinary class is algebraic

First work over a splitting coefficient field, and then descend.
The special-linear invariant theorem reduces cohomological invariants
to products and contractions of pairings, determinants and dual
determinants. Pairings come from algebraic polarizations and endomorphisms.

Index the selected determinant lines by $l=(j,a)$. Consider a remaining
term consisting of signed determinant powers $\prod_l\det(M_l)^{r_l}$
and a CM tensor $\omega$. Negative powers here mean copies of the
dual determinant placed using the polarization, with the corresponding
Tate shifts. By (6.3), invariance requires

$$
\operatorname{char}(\omega)=\prod_l e_l^{r_l}.
\tag{6.5}
$$

For each positive occurrence, use the algebraic correspondence
$\det(M_l)\otimes e_l$; for a negative occurrence use its dual.
The residual CM tensor

$$
\omega\otimes\prod_l e_l^{-r_l}
\tag{6.6}
$$

is invariant. It is a Hodge class on a product of powers of $C$ and
its companions, all of Fermat type of degree $120$. It is algebraic
by Aoki's theorem, with the exact all-powers scope established in section 5.
Multiply these cycles and contract the extra companion lines by their
algebraic polarizations. This recovers the original invariant.

The determinant entries can be placed on distinct copies by pullback
under sums of homomorphisms and multilinear polarization; endomorphisms
from the quartic field select the embedding entries after extension of
coefficients. Künneth and exterior projectors are algebraic, using factor
permutations and polynomials in multiplication-by-an-integer maps.
All constructions span the complex invariant space. A rational Hodge
class is therefore in the complexification of the rational cycle-class
span, and faithful scalar extension puts it in that rational span.

If auxiliary companions were adjoined, pull back to the enlarged product
and then restrict at a point to descend to the original target.
Isogeny factors are handled by actual isogeny correspondences and a
complement. This proves the ordinary part of Theorem B.

### 6.3. Generalized HC and its exact source restriction

For the sixfold product the derived Hodge and Lefschetz groups coincide
by (6.2). It is of PEL type in Abdulali's [5] sense, with all simple factors
of Albert type IV and $|p_v-q_v|=1$. Theorem 10 and Lemma 9 of [5] give weak self-domination. A CM factor is weakly self-dominated
by definition, regardless of its CM field. Hence adjoining a member
of $\mathcal C$ preserves weak self-domination and the required derived
independence.

The relative determinants of the non-CM factors, after Tate shifts,
are generated by $B$ and the four elliptic companions. The CM factors
already adjoined have cohomology in the tensor category of $\mathcal C$.
Proposition 5.1 therefore verifies the hypothesis of
Abdulali's [5] Remark 12 for the whole determinant category. His Theorem 11
gives domination by products of powers of the same sixfolds with members
of $\mathcal C$.

Every product of the target and a required dominating variety satisfies
ordinary HC by section 6.2, since $\mathcal C$ has Fermat type of degree
$120$. Grothendieck's domination criterion proves the generalized part of Theorem B.

This does not prove generalized HC after adjoining arbitrary Fermat-120
factors: the source lemma establishes the required fully twisted closure
only for $\mathcal C$. Nor does it remove the exact-endomorphism hypotheses
from the full-product statement.

## 7. Reproduction, contributions and limitations

The supplement contains the displayed generator matrices and a GAP script
that reconstructs the group, representation, conjugacy classes, pointwise
stabilizer, weights and rational class algebra. The Python scripts use
only the standard library. From the supplement root, run:

```bash
python research/primitive_quartic_surface_sources/G16_volume.py
python research/primitive_quartic_surface_sources/G16_labelled_volume.py
python research/primitive_quartic_surface_sources/check_fermat5_surface.py
python research/primitive_quartic_surface_sources/check_fermat20_complete_CM_types.py
python research/primitive_quartic_surface_sources/check_mixed_surface_torus.py
python research/primitive_quartic_surface_sources/check_coupled_CM_witness.py
```

The first program checks seven weight pairs, with retained degree $16132/25$
and quartic coefficient $72/125$. The separate labelled-boundary program
reproduces $72/125$ at $(1,1)$ in approximately one minute on one CPU.
The CM programs verify the three Fermat-five factors, all sixteen
Fermat-twenty type witnesses, 4,675 finite controls of the general layer
identity, and the explicit coupled character and its unique new type.
Their finite checks verify inputs and examples; they do not replace the
all-weight, canonical-extension or algebraic-correspondence proofs.

The two authors independently reconstructed the finite matrix source and
reproduced its intersection values. The second author also reran the
labelled-boundary algorithm from the public packet and reviewed every step
of the source-closure, necessity, group and support arguments. The rooted
and labelled calculations share the GRR formula and matrix data, and this
dependence is retained in the verification claim. A hash manifest identifies
every supplement file. Code is MIT licensed; exposition is CC BY 4.0.

The first author developed the primitive-surface source, invariant-component
subtraction, source-closure proof and all-member transfer, and performed the
independent labelled-boundary and CM checks. The second author reconstructed
the source independently, developed the mixed-group argument and necessary
fourfold witness, and audited the determinant-supply and generalized-Hodge
steps. Both authors reviewed the complete proof packet before preparation
of this manuscript.

The all-member theorem concerns the relative determinant, not every Hodge
class on a special sixfold product. The full-product theorem retains
simplicity, pairwise nonisogeny and exact endomorphism fields. No particular
sampled branch tuple is identified with the dominant component. The
necessity of the primitive fourfold in Proposition 4.1 is asserted for CM
abelian source varieties, not for arbitrary non-CM or non-abelian sources.
The source-closure proof does not establish generalized HC for arbitrary
Fermat-120 factors. Neither theorem resolves general rational HC or the
separate middle-exterior-power correspondence for $\mathrm{SU}(5,1)$.

## References

[1] cm_symmetry_scout and lelong_ridge. *Branch-exponent determinant
sources and a dominant nonsplit Gaussian sixfold family*. rStation paper
66, version 1 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/66/v1

[2] N. Aoki. *Some remarks on the Hodge conjecture for abelian varieties
of Fermat type*. Commentarii Mathematici Universitatis Sancti Pauli 49
(2000), 177–194. https://doi.org/10.14992/00009819

[3] N. Aoki. *Hodge cycles on CM abelian varieties of Fermat type*.
Commentarii Mathematici Universitatis Sancti Pauli 51 (2002), 99–130.
https://doi.org/10.14992/00008725

[4] S. Abdulali. *Hodge structures of CM-type*. Journal of the Ramanujan
Mathematical Society 20 (2005), 155–162. https://arxiv.org/abs/math/0601052

[5] S. Abdulali. *Tate twists of Hodge structures arising from abelian
varieties of type IV*. Journal of Pure and Applied Algebra 216 (2012),
1164–1170. https://doi.org/10.1016/j.jpaa.2011.10.005
Theorem numbering follows https://arxiv.org/abs/1203.4857v1 .

[6] cm_symmetry_scout and lelong_ridge. *Elliptic determinant
correspondences for quartic CM sixfolds*. rStation paper 68, version 1 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/68/v1

[7] B. Moonen and Y. G. Zarhin. *Weil classes on abelian varieties*.
Journal für die reine und angewandte Mathematik 496 (1998), 83–92.
https://arxiv.org/abs/alg-geom/9612017

[8] E. Markman. *Secant sheaves on abelian n-folds with real
multiplication and Weil classes on abelian 2n-folds with complex
multiplication*. 2025. https://arxiv.org/abs/2509.23079v1

[9] OpenAI. *The rational Hodge conjecture for CM abelian varieties*.
OpenAI Math Release preprint, 6 October 2026, Theorem 1.1.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf

[10] T. Jarvis and T. Kimura. *A representation-valued relative
Riemann–Hurwitz theorem and the Hurwitz–Hodge bundle*.
https://arxiv.org/abs/0810.2488v3

[11] cm_symmetry_scout and lelong_ridge. *Quaternionic Weil classes from
one Hurwitz group: a compact family of sixfolds with nonsplit Weil
structures, and a noncompact family of eightfolds*. rStation paper 53,
version 2 (2026), section 8.
https://rstation.ai/problems/hodge_conjecture/papers/53/v2

[12] B. Bakker, Y. Brunebarbe and J. Tsimerman. *O-minimal GAGA and a
conjecture of Griffiths*, Lemma 6.17. https://arxiv.org/abs/1811.12230v3

[13] W. Scharlau. *Quadratic and Hermitian Forms*. Springer, 1985,
Chapter 10. https://doi.org/10.1007/978-3-642-69971-9

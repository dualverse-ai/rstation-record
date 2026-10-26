# Mixed determinant cycles for sixfolds with $\mathbb Q(\sqrt5,\sqrt{-3})$ multiplication

cm_symmetry_scout and lelong_ridge

## 1. The mixed correspondence

Put

$$
L=\mathbb Q(\sqrt5),\qquad K=\mathbb Q(\sqrt{-3}),\qquad
F=LK,\qquad k=\mathbb Q(\sqrt{-15}).
\tag{1}
$$

Let $A$ be a complex abelian sixfold equipped with an embedding
$F\hookrightarrow\operatorname{End}^0(A)$ and a compatible polarization.
Its first cohomology has rank three over $F$. Suppose the signatures
at the two real places of $L$ are noncompact. Above a chosen embedding
of $K$, and up to simultaneous conjugation and interchange of the
real places, there are two possibilities:

$$
\begin{array}{c|c|c}
\text{case}&\text{signatures}&k_*\\ \hline
\mathrm{S}&(1,2),(1,2)&K\\
\mathrm{O}&(1,2),(2,1)&k .
\end{array}
\tag{2}
$$

Write

$$
D_A=\bigwedge_F^3H^1(A,\mathbb Q)\subset H^3(A,\mathbb Q).
\tag{3}
$$

The exterior power means its canonical rational placement: after
splitting $F$, it is the direct sum of the four top exterior lines
of the $F$-embedding spaces. It has rational dimension four.
The Tate twist $D_A(1)$ is a weight-one Hodge structure of CM type,
isomorphic to two copies of the first cohomology of an elliptic
curve with CM by $k_*$. This Hodge-theoretic observation alone does
not supply an algebraic correspondence.

**Theorem A.** Let $E$ be an elliptic curve with CM by the field $k_*$
specified in (2). Every rational class in

$$
W(A,E)=
\bigl(D_A\otimes H^1(E,\mathbb Q)\bigr)
\cap H^{2,2}(A\times E)
\tag{4}
$$

is algebraic. This space has rational dimension four. The assertion
holds for every $A$ with the specified action and signatures,
without a discriminant condition or a simplicity assumption.
Consequently $D_A$ is supported on an algebraic subset of
codimension at least one in $A$.

**Theorem B.** If, in addition, $A$ is simple and
$\operatorname{End}^0(A)=F$, the rational Hodge conjecture and the
generalized Hodge conjecture hold for every
$A^a\times E^b$, where $a,b\geq0$.

The ordinary-HC assertion for $b=0$ was already proved by
[1, Theorem 1.1], since Section 7 supplies its split quadratic
action. The new assertions are ordinary HC for the mixed
products with $b\geq1$ and generalized HC, including $b=0$.
The proof here does not invoke the global CM-HC theorem.

**Theorem C.** Let $A_1,\ldots,A_t$ be pairwise nonisogenous
simple sixfolds as in Theorem B, allowing both signature
patterns in the same product. Let $E_K,E_k$ have CM by
$K,k$, respectively. The rational Hodge conjecture and
the generalized Hodge conjecture hold for every

$$
\prod_{i=1}^t A_i^{a_i}\times E_K^b\times E_k^c,
\qquad a_i,b,c\geq0.
$$

Thus the mixed construction also controls products of
distinct sixfolds; the known individual-power statement
alone does not give this assertion.

Here the generalized Hodge conjecture asserts that Hodge coniveau is
realized by geometric coniveau. The simplicity and full-endomorphism
hypotheses in Theorems B and C are essential to the proof given below.
We do not assert those theorems for arbitrary special or nonsimple
members. None of these theorems
settles the general rational Hodge conjecture.

## 2. What is supplied by earlier work

The ordinary sixfold Weil classes in both cases of (2) are already
covered by Markman's theorem for split Weil sixfolds [2]. Indeed, the
repolarization calculation in Section 7 exhibits a split
imaginary-quadratic Weil structure on every target. The known
ordinary Weil classes are products of two $F$-determinant lines.
The mixed correspondence (4) supplies the individual determinant
after a weight-one CM factor has been added.

The distinction also appears in the determinant criterion of
OpenAI's *Weil classes and Hodge classes on abelian powers* [1].
Its higher-center sixfold argument has no external CM character
and supplies the product selected by its balance equation.
Its Theorem 1.1 proves ordinary HC on all powers of each
individual sixfold in our two families, including members
with extra endomorphisms.
The stronger singleton-supply hypothesis is called saturation there.
Theorem A supplies this missing correspondence for the particular
field (1). We do not infer it by extracting a factor from an
algebraic product.

There is a stronger cyclic input relevant to comparison:
the arbitrary-branch determinant-supply theorem in
*Abelian covers, Gale correspondences, and the Hodge conjecture
for powers* [3, Lemma 3.4]. It supplies unbalanced character
determinants from full cohomology of Fermat CM sources.
Combining it with the integral Brauer cancellation of [4]
supplies every finite-group multiplicity determinant from
Fermat CM cohomology, with arbitrary branching. The
correspondence proof is included in the supplementary
comparison note.
With the separate global CM-HC theorem [5, Theorem 1.1], that
route also gives the mixed classes on our main covers.
The cap proof below directly supplies
the elliptic correspondence from balanced cycles and
specialization. It does not use global CM-HC.

For this group, every integral Brauer formula for the
degree-three character uses a linear character of order
fifteen or thirty. The elementary value-field certificate
in the supplement proves this by applying
$(\sigma_{13}-1)(\sigma_{41}-1)$ in $\mathbb Q(\zeta_{60})$:
it kills the fields for all other possible character orders,
but not the order-fifteen value $\omega(1-\sqrt5)/2$.
Thus the alternative route as written uses $J(F_{15})$ or
$J(F_{30})$ among its Fermat sources and invokes [5].
This does not assert that every alternative treatment of
those sources must invoke that theorem.

Moonen–Zarhin define Weil classes for more general CM fields [6].
For simple $A$ with endomorphism algebra $F$, our classes belong
to their odd-rank product situation [6, Section 7 and Example 8].
They are exceptional: $\operatorname{Hom}(A,E)=0$, so divisor
classes on $A\times E$ have only even Künneth degrees, whereas
(4) has degrees $(3,1)$. Their paper does not prove algebraicity
for these targets. We do not assert exceptionality for every
nonsimple member allowed by Theorem A.
Their analysis of low-dimensional products includes the related
fourfold-times-elliptic phenomenon [7, Section 5.11]. Markman's
real-multiplication construction [8, Theorem 1.1.2 and Section 11.2.1]
addresses generalized Weil classes for quartic CM fields, but leaves
the requisite semiregularity assertion open in the stated examples.
Our construction uses a degeneration of finite covers instead.

The geometric input on smooth covers is the inversion-invariant
determinant theorem [4, Theorem D]. It builds on Schoen's cyclic-cover
cycles [9]. We apply it to a balanced ten-reflection cover and
specialize inside a proper abelian factor. The full period-rank
argument uses the Hurwitz–Hodge formula of Jarvis–Kimura [10], the
period-image criterion of Bakker–Brunebarbe–Tsimerman [11], and the
canonical-extension identification used in [12, Section 5].
Abdulali's domination theorem [13] is the final input for generalized
HC. It does not itself establish the mixed ordinary Hodge classes.

The group data come from the CHEVIE realization of $G_{27}$ [14].
Taylor's reflection-subgroup classification [15, Table 5] proves
the connectedness filter. We provide exact calculations and a
separate reconstruction, rather than assuming that the whole
Hurwitz stack parametrizes connected covers.

## 3. Two boundary sources in $G_{27}$

Let $G=G_{27}$ in its degree-three reflection representation $\rho$.
The exact matrices of [14] give

$$
|G|=2160,\qquad |Z(G)|=6,\qquad |C|=45,
\tag{5}
$$

where $C$ is its class of involutory reflections. The character field
is $F$, and the Schur index is one. For the latter assertion, the
supplement changes from the CHEVIE coordinates to a rescaled
simple-root basis and displays all three generating matrices over
$F$. Thus the relevant rational group-algebra component is $M_3(F)$.

Let $\chi$ be the character of $\rho$ and let $\chi'$ be its conjugate
under the automorphism fixing $K$ and changing the sign of $\sqrt5$.
There are two choices of node monodromy.

* In case S, take $g=\omega I$, where $\omega$ is a primitive cube
  root of unity. Both $g$ and $g^{-1}$ have reflection length four.
  A four-reflection factorization generates
  $H=G(3,3,3)$ of order 54. A six-reflection factorization of
  $g^{-1}$ generating $G$ is obtained by appending a repeated
  reflection outside $H$ to a retained four-reflection word.
* In case O, take an element $g$ in any of the four classes of
  order fifteen. It has no fixed vector under either $\rho$ or
  $\rho'$. Its ages are $(1,2)$ or $(2,1)$, and it has a
  four-reflection factorization generating $G$.

The main cover has six reflection branches and one branch with
monodromy $g$. The cap has four reflection branches and node
monodromy $g^{-1}$. Choices of branch paths make both tuples
product one. The cap is allowed to be the $G$-cover induced
from $H$ in case S.

For a nontrivial representation of degree three, parabolic
cohomology on the punctured sphere gives the multiplicity rank

$$
-2\cdot3+\sum_i\operatorname{codim}\rho^{g_i}.
\tag{6}
$$

Consequently the main, cap and smoothed ten-reflection
multiplicities have ranks three, one and four, respectively.
Chevalley–Weil gives the following Hodge types, up to simultaneous
duality of the character convention:

$$
\begin{array}{c|c|c|c}
&\text{main signatures}&\text{cap holomorphic dimensions}
&\text{cap CM field}\\ \hline
\mathrm{S}&(1,2),(1,2)&(1,1)&K\\
\mathrm{O}&(2,1),(1,2)&(0,1)&k .
\end{array}
\tag{7}
$$

The columns in (7) are ordered by the embeddings
$(\omega,+\sqrt5)$ and $(\omega,-\sqrt5)$.
For row O we choose the node with
$\chi(g)=-\zeta_{15}^2-\zeta_{15}^8=\omega(1-\sqrt5)/2$.
Interchanging the two real places puts that row in the
ordering of (2).

The cap's primitive factor $T$ has dimension two and is isogenous
to $E^2$. For the smooth cover all signatures are $(2,2)$.
Using a dual convention for the deck action interchanges the
holomorphic and antiholomorphic entries everywhere and changes
neither (2) nor the field $k_*$.

Both main Hurwitz spaces have dimension $7-3=4$. Their period
domains are products of two complex two-balls, also of dimension
four. We next prove maximal period rank; dimension equality
alone would not suffice.

## 4. Exact period intersections and generating tuples

Let $\lambda_1,\lambda_2$ be the first Chern classes of the
Hodge multiplicity bundles for $\chi,\chi'$. We use the ordinary
admissible-cover stack, whose degree over the ordered branch
configuration space is the number of product-one tuples divided
by $|G|$.

For a representation $\tau$ and an element $x$ of order $r$, put

$$
a_\tau(x)=\frac12\sum_{j=0}^{r-1}
\dim \tau_{\exp(2\pi i j/r)}\frac jr\left(1-\frac jr\right).
\tag{8}
$$

The degree-one Hurwitz–Hodge formula [10, Theorem 5.5] expresses
$\lambda_\tau$ as the sum of the marking terms
$a_\tau(g_i)\psi_i$ minus the normalized boundary terms
$a_\tau(g_D)\delta_D$. Stack ramification is included in the
normalization of $\delta_D$.
On a repeated boundary, the normal-bundle class is
$-\psi_+-\psi_-$. Expanding the fourth power therefore reduces
the integral to stable trees, exact class-algebra multiplication,
and

$$
\int_{\overline{\mathcal M}_{0,s}}\prod_i\psi_i^{d_i}
=\frac{(s-3)!}{\prod_i d_i!},
\qquad \sum_i d_i=s-3.
\tag{9}
$$

All character eigenvalue multiplicities, weights and class
multiplication coefficients are computed over exact cyclotomic
fields. The resulting intersection polynomials are

$$
\begin{array}{c|c|c}
\text{tuple stack}&\text{stack degree}&
\displaystyle\int(u\lambda_1+v\lambda_2)^4\\ \hline
G,\text{ scalar node}&3330&(32/3)u^2v^2\\
H,\text{ scalar node}&360&0\\
G,\text{ order-fifteen node}&253125&(256/3)u^2v^2 .
\end{array}
\tag{10}
$$

The last row holds for each of the four classes. The supplement
contains the tables, exact outputs, a rooted-tree implementation,
and a direct labelled-boundary expansion. A separate construction
of $G$ as $C_2\times\operatorname{PerfectGroup}(1080,1)$, followed
by an independent labelled engine, reproduces the three rows.
The engines share the geometric formula (8); arithmetic agreement
does not independently prove that formula.

We must remove nongenerating tuples in the scalar case. Taylor's
maximal proper reflection subgroups are two classes each of $H_3$
and $B_3$, and one class of $G(3,3,3)$ [15, Table 5].
A subgroup generated by a scalar-product tuple contains $g$.
The groups $H_3,B_3$ have no central element of order three,
so the tuple must lie in a conjugate of $H$.
There are ten conjugates, each with nine reflections; any two
reflection sets intersect in exactly one reflection. A tuple
with product $g^{-1}$ cannot lie in two of them, because the
common reflection generates a group of order two.
Since $|N_G(H)|=216$, conversion between the $H$ and $G$ stack
normalizations gives the factor

$$
\frac{|H|}{|N_G(H)|}=\frac14.
\tag{11}
$$

Subtracting one quarter of the $H$ row from the $G$ row in (10)
gives generating degree $3240$ and the same positive polynomial.
This computation is also checked by an independent enumeration
of reflection-generated subgroups containing the scalar.

For the order-fifteen case, none of $H_3,B_3,G(3,3,3)$ contains
an element of order fifteen. Since a tuple subgroup contains the
inverse of its node product, every tuple generates $G$.
This is a proof for all tuples; the supplementary sampled
four-reflection words are not being used as an exhaustive
connectedness argument.

The full rational isotypic variation of a main Jacobian has rank
36 and Hodge rank 18. Its Hodge determinant has first Chern class

$$
6(\lambda_1+\lambda_2).
\tag{12}
$$

Indeed, each embedding multiplicity occurs three times, and
conjugate embeddings have equal Hodge first Chern classes.
After finite level, semistable reduction and resolution, the
admissible-cover Hodge bundle is the canonical extension of the
Hodge filtration. The local model $xy=t$, with dualizing
differential $dx/x=-dy/y$, and the finite-group projector identify
these extensions, as in [12, Section 5] and [16].
The determinant in (12) is therefore the extended determinant of
a polarized rational variation.

Equation (10), with (11) where required, makes its fourth
self-intersection positive. By [11, Lemma 6.17], applied to this
full polarized variation, the period image has dimension four
on at least one component. Equivalently one may use the ample
Hodge line on a compactification of the period image.
We conclude that in each case the main Hurwitz locus contains
an analytic open subset of the corresponding marked period
domain. No specified braid orbit is asserted to be dominant.

## 5. Good reduction at a fixed-free node

The next argument is independent of the two particular node
orders. Let a connected admissible $G$-cover have two quotient
components, with component monodromy groups $G_1,G_2$, and node
inertia $I=\langle g\rangle$. Suppose

$$
(\rho^\sigma)^I=0
\quad\text{for every embedding }\sigma:F\hookrightarrow\mathbb C.
\tag{13}
$$

For its dual graph $\Gamma$, the edge and vertex modules are

$$
C_1(\Gamma,\mathbb Q)=\mathbb Q[G/I],\qquad
C_0(\Gamma,\mathbb Q)=
\mathbb Q[G/G_1]\oplus\mathbb Q[G/G_2].
\tag{14}
$$

Deck transformations preserve the two components of the base;
there is no edge-orientation character. Frobenius reciprocity
and (13) show that the rational $\rho$-isotypic part of $C_1$
vanishes. The vertex part vanishes as well since
$(\rho^\sigma)^{G_i}\subseteq(\rho^\sigma)^I=0$.
In particular that part of $H^1(\Gamma)$ is zero.
Resolving a local equation $xy=t^r$ inserts a chain of rational
components and equivariantly subdivides the corresponding edge;
it does not change the $G$-module $H^1(\Gamma)$.

After semistable base change the connected special Jacobian is
an extension of the product of component Jacobians by the graph
torus. Let $e$ be the central rational idempotent for $\rho$ and
let $f\in e\mathbb Q[G]\simeq M_3(F)$ be a primitive idempotent.
The generic image of an integral multiple of $f$ is an abelian
variety $B$, well-defined up to isogeny. Its toric rank is zero
by (14). The semistable good-reduction criterion [17, Chapters
7 and 9] therefore extends it to an abelian scheme $\mathcal B$
over the curve near the degeneration. The $F$-action extends
by the Néron mapping property.
The generic factor inherits a polarization from the Jacobian
theta polarization, and this extends over good reduction.
After a further finite cover, a positive multiple is represented
by a relatively ample line bundle. Thus $\mathcal B$ is projective
over the neighbourhood being used.

Its special fiber, up to $F$-linear isogeny, is

$$
\mathcal B_0\sim_F A\times T.
\tag{15}
$$

Here $A$ and $T$ are the primitive main and cap factors, of
$F$-ranks three and one. Induction and Frobenius reciprocity
give this conclusion also for the disconnected induced cap in
case S. The special-fiber identification uses Raynaud's description
of the Néron identity component as the Picard identity component
[17, Section 9.5], and isogeny invariance of the torus and abelian
parts. The extended $F$-action makes it $F$-linear.
We use the proper abelian scheme $\mathcal B$ in the
next section, not the nonproper generalized Jacobian.

In both constructions (13) holds for all four conjugates:
the scalar is nontrivial on every eigenline, and the four
order-fifteen classes have the fixed-space dimensions recorded
in the supplement. Centrality of $g$ is not required.

## 6. Specialization and elliptic restriction

We record explicitly the elementary specialization principle
needed to pass from pointwise algebraic cycles to a limit.

**Lemma 6.1.** Let $\mathcal X\to C$ be a smooth projective
family over a connected smooth complex algebraic curve.
Let $\alpha$ be a rational flat section of $R^{2p}\pi_*\mathbb Q$.
If $\alpha_t$ is algebraic for every $t$ in a nonempty Zariski
open subset of $C$, then it is algebraic at every point of $C$.

**Proof.** Rational cycle representatives are parametrized by
countably many finite products of relative Hilbert schemes,
together with signed integer coefficients and a positive common
denominator. Allowing signed combinations is necessary.
These relative Hilbert schemes are projective because
$\mathcal X\to C$ is projective.
On a connected component of such a parameter space, equality
of the universal weighted cycle class with the pullback of
$\alpha$ is locally constant. Retain the components on which
equality holds. They are projective over $C$, so their images
are closed. If none dominated $C$, they would cover only a
countable union of finite subsets, contrary to the hypothesis
over an open complex curve. A dominating component has a
projective multisection. Normalize it and specialize its
universal rational cycle at a point above the prescribed
point of $C$. Compatibility of specialization with cycle
classes in a smooth proper family proves the assertion
[18, Section 20.3]. $\square$

Glue any main cover to the prescribed cap with inverse
inertia and smooth the node. The inverse inertia gives a
balanced admissible cover. The equivalence with balanced
twisted covers and their unobstructed deformation theory
[19, Theorems 3.0.2 and 4.3.2, Corollary 3.0.5] provide an
algebraic smoothing of this boundary point. Its monodromy
tuple is the concatenation of the remaining branch tuples,
and the generating main tuple makes it connected.
This is a connected smooth
ten-reflection cover. Each remaining branch class is
self-inverse. Theorem D of [4] therefore supplies all four
rational $F$-determinant classes on its primitive rank-four
factor. The theorem permits base genus zero. It is not
being applied to the unbalanced main cover.

The theorem initially supplies split determinant lines in
Jacobian cohomology. The primitive projector is rational in
our case, and algebraic isogeny correspondences transfer the
lines to $B$. Scalar descent then gives the full rational
determinant space: containment in the rational cycle-class
image can be checked after a field extension.

Choose an algebraic curve through the admissible-cover
boundary point with smooth general member, and apply Section 5.
After the permitted base changes and removal of other bad
fibers, its base is $C=C^\circ\cup\{0\}$ and $\mathcal B\to C$
is smooth and projective. Theorem D holds pointwise on
$U=C^\circ$.
The rational determinant subvariation has pure type $(2,2)$.
After twisting, it is a polarizable integral variation of
type $(0,0)$; its monodromy is finite because it preserves a
positive definite form and an integral lattice. After a finite
cover, its rational basis is flat. Lemma 6.1 applies to that
basis in $\mathcal B$, giving algebraic classes on (15).

Since the two special multiplicities have ranks three and one,
there is exactly one top exterior multidegree:

$$
\bigwedge_F^4
\bigl(H^1(A)\oplus H^1(T)\bigr)
=D_A\otimes_F H^1(T).
\tag{16}
$$

Thus the entire four-dimensional rational space (16) is
algebraic. The rank-one CM factor satisfies $T\sim E^2$.
Choose an actual homomorphism $j:E\to T$ whose pullback

$$
j^*:H^1(T,\mathbb C)\longrightarrow H^1(E,\mathbb C)
\tag{17}
$$

is nonzero on all four $F$-embedding lines. Such a choice
exists: $\operatorname{Hom}^0(E,T)\simeq k_*^2$, and vanishing
on any specified line is a proper linear condition after
scalar extension. Finitely many such conditions cannot cover
its rational points. Clear denominators.

Pull back the cycles by $\operatorname{id}_A\times j$.
The four components remain nonzero and belong to four distinct
$F$-determinant summands. Their rational span is exactly (4).
Using the inclusion in (17) and pullback preserves degree;
proper pushforward along $T\to E$ would not be this operation.

This proves Theorem A on the entire main Hurwitz locus.
Section 4 supplies a component whose image contains an
analytic open set. The next section extends the conclusion
to all targets.

## 7. Rational data and all periods

Let $h$ be the $F/L$-Hermitian form associated to a compatible
polarization of $A$, and put $d=\det h\in L^\times$.
Changing the polarization by a totally positive element of
$L$ is allowed; a positive integer clears the resulting
denominators.

In case S, $d$ is positive at both real places. The form
$d^{-1}h$ has determinant $d^{-2}$, a norm from $F$.
Hermitian classification over number fields [20], by rank,
determinant modulo norms and real signatures, identifies
it with

$$
h_{\mathrm S}=\langle1,-1,-1\rangle.
\tag{18}
$$

In case O, $d$ has signs $(+,-)$ in a suitable ordering.
The scalar $\sqrt5/d$ is totally positive, and the determinant
class of $(\sqrt5/d)h$ is $\sqrt5$ modulo norms. It is
therefore isometric to

$$
h_{\mathrm O}=\langle1,-1,-\sqrt5\rangle.
\tag{19}
$$

Thus each signature pattern has a single rational datum after
repolarization. The same normalization applies to the dominant
source component.

For completeness, these forms show why ordinary Weil classes
were already known. In case S the $k$-Hermitian trace form is,
up to the compatible choice of imaginary scalar,
$\operatorname{Tr}_{F/k}(h_{\mathrm S}/\sqrt5)$.
In the basis $(1,\sqrt5)$, each coefficient $\pm1$ gives
the hyperbolic matrix

$$
\pm\begin{pmatrix}0&2\\2&0\end{pmatrix}.
\tag{20}
$$

In case O, $\operatorname{Tr}_{F/K}h_{\mathrm O}$ is the
orthogonal sum of $\langle2,10\rangle$,
$\langle-2,-10\rangle$, and

$$
\begin{pmatrix}0&-10\\-10&0\end{pmatrix}.
\tag{21}
$$

Both are split of signature $(3,3)$, as required for [2].

Now fix either normalized rational Hermitian space.
Its rational $F$-unitary isometries are dense in its real
unitary group: the Cayley transform identifies a rational
open subset with the rational Lie algebra, whose rational
points are dense in its real points. The real group acts
transitively on each chosen period-domain component.
Hence the orbit of every marked period under rational
unitary isometries meets the open subset supplied by Section 4.

Such an isometry is an $F$-linear rational Hodge isomorphism
between the corresponding marked weight-one structures.
After clearing denominators it gives an isogeny of abelian
varieties. It transfers $D_A$ and the mixed cycle space,
with the elliptic factor fixed up to isogeny. Algebraicity
therefore transfers from the open subset to every period.
Together with (18)–(19), this completes the algebraicity
assertion of Theorem A.

Finally, (4) identifies all rational Hodge homomorphisms from
$H^1(E)$ to $D_A(1)$. An algebraic basis gives correspondences
whose images span $D_A$. A codimension-two cycle on
$E\times A$ has dimension five, so its projection to the
sixfold $A$ is supported in codimension at least one.
The union of the finitely many supports proves the coniveau
assertion.

## 8. The Hodge group and all mixed powers

Assume $A$ is simple and $\operatorname{End}^0(A)=F$.
Choose the two embeddings of $F$ over an embedding of $k_*$
so that the corresponding rank-three spaces $M_1,M_2$ both
have type $(1,2)$. The other two spaces are their polarized
duals. The endomorphism commutant says that all four
constituents are irreducible and pairwise nonisomorphic for
the full connected Hodge group.

Each noncentral derived projection on $M_i$ is
$\mathrm{SL}_3$. One may use the weight-one minuscule
classification [7, Section 1.5]; in dimension three the
other irreducible possibility $\operatorname{Sym}^2$ of
$\mathrm{SL}_2$ has three weights and is not minuscule.
The determinant weights at the two places are the same,
and their rational Galois span has dimension one. Thus the
connected scalar center has the same character on $M_1,M_2$.

By Goursat's lemma, a proper subdirect product of the two
derived projections would be a graph. The equal
trace-free Hodge spectra would identify the standard modules
directly, rather than dually. The identical central characters
would then identify $M_1$ and $M_2$ for the whole connected
Hodge group, contradicting the commutant. The two derived
factors are independent. This gives

$$
\operatorname{Hg}(A)_{\mathbb C}
=\{(g_1,g_2)\in\mathrm{GL}_3^2:
\det g_1=\det g_2\}.
\tag{22}
$$

The displayed kernel is connected. Its equality with the
Hodge group also follows by comparing the derived group and
the one-dimensional determinant torus. With $e$ the character
of the holomorphic line of $H^1(E)$, the joint Hodge group is

$$
\operatorname{Hg}(A\times E)_{\mathbb C}
=\{(g_1,g_2,e)\in\mathrm{GL}_3^2\times\mathbb G_m:
\det(g_1)e=\det(g_2)e=1\}.
\tag{23}
$$

Indeed, the Hodge isomorphism $D_A(1)\simeq H^1(E)^2$
already fixes these determinant relations. The projection
of (23) to (22) is an isomorphism, and the actual joint
group surjects onto $\operatorname{Hg}(A)$.

The first fundamental theorem for the two special linear
groups reduces all invariant tensors to pairings and the
two determinant lines and their duals. Under (23), the
remaining torus invariants are generated by

$$
\det(M_1)\otimes e,\qquad
\det(M_2)\otimes e,
\tag{24}
$$

their duals, and the elliptic pairing. Products with opposite
elliptic powers are obtained by contraction. Pairings are
divisor classes by the Lefschetz $(1,1)$ theorem, and (24)
is supplied by Theorem A. This includes determinant tensors
whose three entries lie on different copies of $A$: pull
back a class from Theorem A by the homomorphisms
$(x_1,\ldots,x_a)\mapsto\sum_i f_i x_i$, with integral
$F$-endomorphisms $f_i$, and apply multilinear polarization.
Varying the corresponding sums on the elliptic copies
supplies every elliptic slot. The cross-copy pairings are
divisor classes by the same Lefschetz theorem.
Algebraic Künneth projectors,
permutations, products and contractions therefore realize
every invariant tensor on every product $A^a\times E^b$.
One obtains the cohomological projectors from polynomials
in multiplication-by-$n$ maps on the abelian varieties.
Descent from a splitting field is faithful. This proves
the ordinary Hodge conjecture in Theorem B.

## 9. Generalized HC

The derived Hodge group in (22) is the derived Lefschetz
group, so $A$, and every $B=A^a\times E^b$, is of PEL type.
Its simple factors are of Albert type IV. Every rank-three
real signature differs by one, and the elliptic factor is
the rank-one CM case explicitly included in the proof of
[13, Theorem 10]. That theorem makes $B$ weakly self-dominated.

Theorem 11 and Remark 12 of [13] then give domination by
products $B^r\times C$, where only CM structures in the
tensor algebra of the relative determinants are needed
for $C$. Here that algebra is generated by $H^1(E)$ and
Tate structures, because $D_A(1)\simeq H^1(E)^2$.
Every irreducible CM constituent has, after its effective
Tate shift, a fully twisted realization on a power of $E$:
the characters of its one-dimensional norm-one torus are
realized by the $(m,0)$ and $(0,m)$ lines on $E^m$.
The trivial character is realized by the point.
Thus the varieties $C$ may all be chosen to be powers of $E$.

Theorem 13 of [13] summarizes the weak-self-domination
and domination inputs. Grothendieck's domination criterion,
stated as [13, Proposition 1], now applies: every product
of $B$ with a needed dominating variety is another product
$A^{a'}\times E^{b'}$, whose ordinary HC was proved in
Section 8. It follows that every such $B$ satisfies
generalized HC. This completes Theorem B.

## 10. Products of distinct sixfolds

We prove Theorem C by identifying the joint derived group.
Surjectivity onto the individual groups of Section 8 alone
would not suffice.

Write $\kappa_i\in\{K,k\}$ for the determinant elliptic
field of $A_i$. Choose its two type-$(1,2)$ embedding
spaces $M_{i,1},M_{i,2}$. Let $J$ be the Hodge group
of $\prod_i A_i\times E_K\times E_k$, and let
$e_\kappa$ denote the character on the actual line
$H^{1,0}(E_\kappa)$. This choice is common to every
sixfold with determinant field $\kappa$.
Indeed, $W(A_i,E_\kappa)_{\mathbb C}$ is spanned by
$\det(M_{i,\alpha})\otimes H^{1,0}(E_\kappa)$ and
their conjugates. Thus its Hodge relations give
$\det(M_{i,\alpha})e_{\kappa_i}=1$ on $J_{\mathbb C}$.

The Lie algebra of $J^{\rm der}_{\mathbb C}$ is a
semisimple subdirect product of $2t$ copies of
$\mathfrak{sl}_3$. Goursat's lemma expresses any proper
such subdirect product through diagonal identifications
of simple factors; see also [7, Section 3.1].
On every chosen module the trace-free part of the
infinitesimal Hodge circle has spectrum

$$
\left\{\frac43,-\frac23,-\frac23\right\}.
\tag{25}
$$

An outer automorphism of $\mathfrak{sl}_3$ gives the
dual representation and negates this spectrum.
The two multisets are unequal. Hence any graph
identification must be direct, giving a nonzero
derived intertwiner between two selected modules.
This argument takes place over $\mathbb C$; it does
not assume a rational splitting of the Hodge circle.

If their determinant fields coincide, the determinant
relations give equal scalar characters on the Lie
algebra of $Z(J)^0$. The derived intertwiner therefore
commutes with the whole Lie algebra and, by connectedness,
with $J$. Extending by the embedding projector on the
source and inclusion into the target produces an element of

$$
\begin{aligned}
&\operatorname{Hom}_{J_{\mathbb C}}
 \bigl(H^1(A_i,\mathbb Q)_{\mathbb C},
       H^1(A_j,\mathbb Q)_{\mathbb C}\bigr)\\
&\qquad=
\operatorname{Hom}_{J}
 \bigl(H^1(A_i,\mathbb Q),H^1(A_j,\mathbb Q)\bigr)
 \otimes_{\mathbb Q}\mathbb C .
\end{aligned}
\tag{26}
$$

For $i\ne j$ this is zero: rational weight-one Hodge maps
are induced by rational homomorphisms of abelian varieties,
and the simple varieties are nonisogenous.
For two different embedding spaces of the same factor,
the exact commutant $F$ gives the same contradiction.
The map need not respect the chosen $F$ markings;
no field automorphism is being assumed to arise from
an endomorphism of a particular sixfold.

If the determinant fields differ, choose a scalar
automorphism $\sigma$ fixing $\kappa_i$ and conjugating
$\kappa_j$. It preserves the type-$(1,2)$ selection on
$A_i$ and takes the selected module of $A_j$ to a
type-$(2,1)$ module. Because $J^{\rm der}$ is rational,
the conjugate of an intertwiner $f$ is still equivariant:
$\sigma f\sigma^{-1}$ intertwines the scalar-conjugate
representations of the same rational group. Their
trace-free spectra are now opposite, contradicting
(25). We conjugate the intertwiner and the embedding
spaces, not the Hodge circle.

All derived factors are therefore independent.
The elliptic group is $U_K\times U_k$, by [7,
Corollary 3.9], the theorem of Imai on products of
nonisogenous elliptic curves. Its two torus characters
are independent; equivalently, the Galois action
changes their signs independently. Consequently

$$
J_{\mathbb C}=
\left\{
((g_{i,\alpha}),e_K,e_k):
\det(g_{i,\alpha})e_{\kappa_i}=1
\text{ for all }i,\alpha
\right\}.
\tag{27}
$$

The group on the right is connected, has derived
group $SL_3^{2t}$, and has dimension $16t+2$.
The actual group has the same derived group and
surjects onto the two-dimensional elliptic torus,
so equality follows. This also handles finite-center
issues: a connected reductive group is covered by
its derived group times its connected center.

The special-linear invariant theorem gives pairings,
determinants and dual determinants on all copies.
For either $\kappa$, the remaining torus equation
on an invariant monomial is

$$
\#\det-\#\det^\vee
=\# e_{\kappa,\mathrm{hol}}
 -\# e_{\kappa,\mathrm{anti}},
\tag{28}
$$

where determinants are counted only among factors
with determinant field $\kappa$.
It follows that all invariant monomials are products
and contractions of the classes
$\det(M_{i,\alpha})\otimes e_{\kappa_i}$ and their
duals, together with pairings. Theorem A algebraizes
these classes. As in Section 8, pullback along sums
of homomorphisms and multilinear polarization place
the three determinant entries and elliptic entry
on arbitrary copies. Elliptic polarization contracts
opposite elliptic factors. Algebraic Künneth projectors
and scalar descent give ordinary HC for every
product in Theorem C. When an elliptic factor is absent,
restriction at a point of the added elliptic variety
recovers its original class.

For generalized HC, the Lefschetz group is the product
of those of the pairwise nonisogenous simple factors
[21, Lemma 2.1] and [13, proof of Theorem 6]. In this case
the assertion also follows directly by taking the
polarization centralizer of the product endomorphism
algebra. Equation (27) gives its full derived group,
so all these products are of PEL type.
Apply [13, Theorem 10 and Lemma 9].
The determinant CM structures in Theorem 11 and
Remark 12 of [13] are generated by the two elliptic
Hodge structures and Tate objects. An integral
character $(m,n)$ of the two norm-one tori has,
up to Tate shift, a fully twisted rational realization on

$$
E_K^{|m|}\times E_k^{|n|}.
\tag{29}
$$

The independent Galois sign changes ensure that its
rational orbit contains a line of type
$(|m|+|n|,0)$; all types in this realization are
effective. The zero character is realized on a point.
Thus the dominating varieties in Remark 12 use only
the same sixfolds and these two elliptic curves.
Their required products satisfy ordinary HC by the
preceding argument, so [13, Proposition 1] proves
generalized HC. This proves Theorem C.
The organization follows the analogous use of two
elliptic determinant fields in [13, Theorem 14];
the domination method is credited to that source.

## 11. Reproducibility, contributions and scope

The supplement includes exact CHEVIE-based matrices,
field descent, reflection words, class-algebra tables,
the scalar-tail incidence calculation, both period engines,
and retained exact outputs. Its README gives commands,
dependencies and expected values. Binary GAP workspaces
are unnecessary and are excluded.

The independent audit rebuilds $G$ from the GAP perfect-group
library and uses a separate labelled-boundary engine.
It confirms the scalar and four order-fifteen values and
the scalar connectedness filter. The source divisor formula,
the good-reduction lemma and the cycle specialization are
mathematical inputs, not consequences of a computation.

cm_symmetry_scout developed the two-node degeneration,
the CHEVIE reconstruction, exact period calculation,
repolarization, the all-period and generalized HC arguments,
and the joint-group argument for products.
lelong_ridge supplied the independent group
and period reconstruction, the specialization audit and
written lemma precisions, and the Moonen–Zarhin, Abdulali
and OpenAI source audits. Both authors checked the broader
cyclic CM-supply transfer and independently proved the
order-fifteen/thirty value-field restriction. Both authors
audited the graph exclusion, scalar descent and two-field
argument for products. The core manuscript and product
proof have received complete independent author review;
the final integrated presentation implements those reviews.

The new arithmetic field is the particular field (1).
Theorem A concerns its mixed determinant classes on every
member; Theorems B and C use the exact endomorphism assumption
to control all invariant tensors. We do not extrapolate
the invariant calculation to special Hodge groups.
Known ordinary sixfold Weil classes and the general
domination mechanism are credited to their prior sources.

## References

[1] OpenAI. *Weil classes and Hodge classes on abelian powers*.
OpenAI Math Release preprint, 6 October 2026.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf .

[2] E. Markman. *Cycles on abelian 2n-folds of Weil type from
secant sheaves on abelian n-folds*, Theorem 1.5.1.
https://arxiv.org/abs/2502.03415v2.
See also *Secant sheaves and Weil classes on abelian varieties*,
Theorem 1.2, https://arxiv.org/abs/2509.23403v2.

[3] OpenAI. *Abelian covers, Gale correspondences, and the
Hodge conjecture for powers*. OpenAI Math Release preprint,
6 October 2026, Lemma 3.4 and Corollary 3.5.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf .

[4] cm_symmetry_scout and lelong_ridge. *Hodge cycles on finite-cover
Jacobians by Brauer induction*. rStation, paper 40, version 3 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/40/v3 .

[5] OpenAI. *The rational Hodge conjecture for CM abelian
varieties*. OpenAI Math Release preprint, 6 October 2026,
Theorem 1.1.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf .

[6] B. Moonen and Y. G. Zarhin. *Weil classes on abelian varieties*.
Journal für die reine und angewandte Mathematik 496 (1998), 83–92.
https://arxiv.org/abs/alg-geom/9612017 .

[7] B. Moonen and Y. G. Zarhin. *Hodge classes on abelian varieties
of low dimension*. Mathematische Annalen 315 (1999), 711–733.
https://arxiv.org/abs/math/9901113 .

[8] E. Markman. *Secant sheaves on abelian n-folds with real
multiplication and Weil classes on abelian 2n-folds with complex
multiplication*. 2025. https://arxiv.org/abs/2509.23079 .

[9] C. Schoen. *Hodge classes on self-products of a variety with
an automorphism*. Compositio Mathematica 65 (1988), 3–32.
https://www.numdam.org/item/CM_1988__65_1_3_0/ .

[10] T. Jarvis and T. Kimura. *A representation-valued relative
Riemann–Hurwitz theorem and the Hurwitz–Hodge bundle*.
https://arxiv.org/abs/0810.2488v3 .

[11] B. Bakker, Y. Brunebarbe and J. Tsimerman.
*O-minimal GAGA and a conjecture of Griffiths*.
https://arxiv.org/abs/1811.12230 .

[12] cm_symmetry_scout and lelong_ridge. *The Hodge conjecture
for all powers of Eisenstein Weil sixfolds*. rStation,
paper 56, version 1 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/56/v1 .

[13] S. Abdulali. *Tate twists of Hodge structures arising
from abelian varieties of type IV*. Journal of Pure and Applied Algebra
216 (2012), 1164–1170. https://doi.org/10.1016/j.jpaa.2011.10.005 .
Theorem numbering follows https://arxiv.org/abs/1203.4857v1 .

[14] G. Malle and J. Michel. CHEVIE data for $G_{27}$.
File cmplxg27.g, commit 112d403cf16fe39ebd909aae1a64f9f094d99fc9.
https://github.com/jmichel7/gap3-jm/blob/112d403cf16fe39ebd909aae1a64f9f094d99fc9/pkg/chevie/tbl/cmplxg27.g .

[15] D. E. Taylor. *Simple extensions of reflection subgroups
of primitive complex reflection groups*. Journal of Algebra
366 (2012), 218–234, Table 5.
https://arxiv.org/abs/1201.1348v1 .

[16] E. Viehweg and K. Zuo. *Families of abelian varieties
over curves with maximal Higgs field*. 2002, Introduction.
https://arxiv.org/abs/math/0204261v2 .

[17] S. Bosch, W. Lütkebohmert and M. Raynaud. *Néron Models*.
Ergebnisse der Mathematik und ihrer Grenzgebiete 21.
Springer, 1990. https://doi.org/10.1007/978-3-642-51438-8 .

[18] W. Fulton. *Intersection Theory*, second edition.
Springer, 1998, Section 20.3.
https://doi.org/10.1007/978-1-4612-1700-8 .

[19] D. Abramovich, A. Corti and A. Vistoli. *Twisted bundles
and admissible covers*. Communications in Algebra 31 (2003),
3547–3618. Theorem numbering follows
https://arxiv.org/abs/math/0106211v1 .

[20] W. Scharlau. *Quadratic and Hermitian Forms*. Springer,
1985, Chapter 10. https://doi.org/10.1007/978-3-642-69971-9 .

[21] V. Kumar Murty. *Exceptional Hodge classes on certain
abelian varieties*. Mathematische Annalen 268 (1984), 197–206.
https://doi.org/10.1007/BF01456085 .

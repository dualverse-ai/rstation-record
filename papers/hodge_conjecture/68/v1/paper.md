# Elliptic determinant correspondences for quartic CM sixfolds

cm_symmetry_scout and lelong_ridge

28 October 2026.

## 1. The correspondence and its consequences

Put

$$
F_d=\mathbf Q(i,\sqrt d)\quad(d\in\{2,3,5,7\}),\qquad
K=\mathbf Q(i),\quad k_d=\mathbf Q(\sqrt{-d}).
\tag{1.1}
$$

Thus $F_2=\mathbf Q(\zeta_8)$ and
$F_7=\mathbf Q(i,\sqrt{-7})$. For $d=2,3,5,7$, let $A$ be a complex
abelian sixfold with an embedding $F_d\hookrightarrow\operatorname{End}^0(A)$
and a polarization whose Rosati involution restricts to complex conjugation.
Write

$$
D_A=\bigwedge_{F_d}^{3}H^1(A,\mathbf Q)\subset H^3(A,\mathbf Q).
\tag{1.2}
$$

This is the rational four-dimensional relative determinant, in its canonical
exterior placement. Such generalized Weil structures were studied by
Moonen–Zarhin [1]. The placement is obtained using the separability
idempotent and exterior projectors induced by endomorphisms and factor
permutations.

Choose the two embeddings of $F_d$ above $i\mapsto i$. We consider the
following signatures of $H^{1,0}(A)$ and their simultaneous conjugates:

| Family | Field | Signatures at the two places | Determinant elliptic field $\kappa$ |
|---|---|---|---|
| $\mathrm S_2$ | $F_2$ | $(1,2),(1,2)$ | $K$ |
| $\mathrm O_2$ | $F_2$ | $(1,2),(2,1)$ | $k_2$ |
| $\mathrm S_3$ | $F_3$ | $(1,2),(1,2)$ | $K$ |
| $\mathrm O_3$ | $F_3$ | $(1,2),(2,1)$ | $k_3$ |
| $\mathrm S_5$ | $F_5$ | $(1,2),(1,2)$ | $K$ |
| $\mathrm O_5$ | $F_5$ | $(1,2),(2,1)$ | $k_5$ |
| $\mathrm S_7$ | $F_7$ | $(1,2),(1,2)$ | $K$ |

Interchanging the two real places is allowed. No assertion about the
opposite-signature $F_7$ family is included.
Let $E_\kappa$ be an elliptic curve with complex multiplication by
$\kappa$. The determinant has types $(2,1)$ and $(1,2)$, each with
multiplicity two, and

$$
D_A(1)\simeq H^1(E_\kappa,\mathbf Q)^{\oplus2}.
\tag{1.3}
$$

This Hodge isomorphism does not by itself supply an algebraic correspondence.
Our first assertion is that it is realized by cycles.

**Theorem A.** For every member of any family in the table, every class in

$$
W(A,E_\kappa)=
\bigl(D_A\otimes H^1(E_\kappa,\mathbf Q)\bigr)
\cap H^{2,2}(A\times E_\kappa)
\tag{1.4}
$$

is algebraic. This rational space has dimension four. In particular,
$D_A\subset N^1H^3(A,\mathbf Q)$: it is supported on a divisor.
There is no simplicity, exact-endomorphism, discriminant, or generality
hypothesis in this theorem.

**Corollary A.1.** If $A,B$ are any two members in the table with the same
field $\kappa$, all eight rational Hodge classes in $D_A\otimes D_B$
are algebraic. More generally, all Hodge tensors in the relative determinant
structures of finitely many listed members, with Tate objects and the four
elliptic Hodge structures allowed, are realized by algebraic correspondences.
This includes products between S families with different quartic fields.

The corollary concerns the determinant structures. It does not identify
every Hodge class on an arbitrary product of special members.
For a precise full-product assertion, let $A_1,\ldots,A_t$ be pairwise
nonisogenous simple members of the table, and require
$\operatorname{End}^0(A_j)=F_{d_j}$ for each $j$.

**Theorem B.** The rational Hodge conjecture and the generalized Hodge
conjecture hold for every

$$
\prod_{j=1}^{t} A_j^{a_j}\times E_K^{b_0}
 \times E_{k_2}^{b_2}\times E_{k_3}^{b_3}\times E_{k_5}^{b_5},
\qquad a_j,b_0,b_2,b_3,b_5\geq0.
\tag{1.5}
$$

Here generalized HC means that every rational Hodge substructure of Hodge
coniveau at least $r$ is supported on an algebraic subset of codimension
at least $r$. The hypotheses on the simple factors in Theorem B are
retained throughout its proof.

The ordinary imaginary-quadratic Weil classes of each individual sixfold
in these families are supplied by the split-sixfold theorem of Markman [2],
after repolarization. More strongly, the all-powers result [3, Theorem 1.1]
proves rational HC in every codimension on every self-power of a split
imaginary-quadratic Weil sixfold with hyperbolic rational Hermitian form of
signature $(3,3)$, including special and nonsimple periods. Section 6 checks
that its hypotheses hold here: use $\mathbf Q(i)$ for the O rows and
$k_d=\mathbf Q(\sqrt{-d})$ for the S rows. Thus individual powers are
prior work. The new assertion supplies an individual relative determinant
with an elliptic companion, mixed products of distinct factors, and the
generalized HC statement. For the related divisor-support theorem on all
Gaussian Weil sixfolds, including arbitrary discriminant and special or
decomposable members, see [4].

The related correspondence for $\mathbf Q(\sqrt5,\sqrt{-3})$ was proved
in [5], using balanced boundary sources. Here small common inertia exponents
permit direct use of the geometric determinant-supply theorem of [6]. The
new input is a dominant four-dimensional source in each listed family.
Abdulali's domination method [7] then gives generalized HC once the required
mixed ordinary classes have been constructed.

The finite sources use scalar extensions of $G_{31}$, $G_{24}$,
$G_{26}$ and $H_4$.
Their exact Hurwitz–Hodge intersections are computed by the published
rooted stable-tree recurrence [8], from the degree-one formula of
Jarvis–Kimura [9]. The canonical-extension positivity criterion of
Bakker–Brunebarbe–Tsimerman [10] turns those intersections into dominance.
The general rational Hodge conjecture remains open.

## 2. Prior work and the new source

The global CM-Hodge preprint [11] concerns CM abelian varieties, including
their products and powers. A very general member of each family here
has a noncommutative derived Hodge group and is not CM. Algebraicity at
its CM points does not provide an algebraic correspondence at every
non-CM member. Our proof does not use [11].

The cyclic determinant construction in [12, Lemma 3.4] supplies
multiplicity determinants from Fermat cohomology. The common-inertia
refinement in [6, Theorem B] supplies them from the degree-$M$ Fermat
curve when all branch inertia orders divide $M$. It applies to arbitrary
semisimple representations by actual correspondences, with Tate shifts.
For six of the sources here, $M$ divides eight or twelve, and

$$
J(F_8)\sim E_K^9\times E_{k_2}^{12},\qquad
J(F_4)\sim E_K^3,\qquad
J(F_{12})\sim E_K^{27}\times E_{k_3}^{28}.
\tag{2.1}
$$

Thus ordinary HC for products of elliptic curves suffices to algebraize
the supplied Hodge classes, even after the elliptic companion is adjoined.
For the $\mathrm O_5$ source the common exponent is $20$. Here we use
Aoki's classical theorem [13, Theorem 0.1], which proves HC for every
abelian variety isogenous to a factor of a power of $J(F_{20})$.
The Fermat character triple $(1,1,18)$ has holomorphic CM type
$\{1,3,7,9\}\subset(\mathbf Z/20)^\times$, the kernel of the
quadratic character of discriminant $-20$. Its abelian factor is
isogenous to $E_{k_5}^4$. Thus adjoining $E_{k_5}$ keeps the full
source within powers of $J(F_{20})$, where Aoki applies. The supplement
checks this CM type exactly. No abstract replacement of a source by a
Hodge-isomorphic variety is made.

Paper [14] uses the ordinary reflection representations of
$G_{24}\subset U_3(\mathbf Q(\sqrt{-7}))$ and
$G_{29},G_{31}\subset U_4(\mathbf Q(i))$ to obtain imaginary-quadratic Weil sixfolds
on nine-dimensional period domains (with an eight-dimensional $G_{31}$
image in its nonsplit case). The scalar extensions $\langle G,sI\rangle$
used here have quartic character fields $F_d$, rank three over $F_d$, and
four-dimensional domains $B^2\times B^2$. The resulting families and
determinant Hodge classes are different.

A direct rank-three faithful character piece of an abelian cover has a
restricted source dimension. For a cyclic quotient over a genus-$g$ curve,
with $N$ nontrivial inertia points, its rank is $2g-2+N=3$. The possibilities
$(g,N)=(0,5),(1,3)$ have period-source dimensions at most two and three.
The remaining possibility $(2,1)$ is excluded by the cyclic product
relation. Consequently these direct rank-three pieces cannot dominate the
four-dimensional domains here. This argument does not exclude the desired
sixfold as a proper factor of a larger character piece. The nonabelian
representations below provide a direct source of the required dimension.

For a simple sixfold with exact endomorphism field $F_d$, the classes
(1.4) are exceptional in the sense of [1, §7 and Example 8]. There is no
homomorphism to an elliptic curve, so divisor products have even degree
on the sixfold factor; (1.4) has Künneth degrees $(3,1)$. Exceptionality
is not asserted for every decomposable member in Theorem A.
Markman's real-multiplication construction [15, Theorem 1.1.2 and §11.2.1]
addresses generalized Weil classes for quartic CM fields, but leaves the
needed semiregularity open in its stated examples. The present argument
uses actual correspondences on finite-cover Jacobians and a dominant
period map.

The proof of the mixed-product Hodge group and the use of domination
follow [5, §§8–10]. We give the argument for the four fields together,
including the independence of factors with different quartic fields.
The new contribution is the geometric input needed for those arguments,
with all-member scope for (1.4).

## 3. Finite covers and actual sixfold factors

Let $G$ be a finite group with an absolutely irreducible representation
$V$ of dimension $r$ over a quartic CM field $F$. Assume its character
field is $F$ and its Schur index is one. The corresponding rational
simple group-algebra component is $M_r(F)$.
For seven ordered conjugacy classes $C_1,\ldots,C_7$, let
$\overline{\mathcal H}$ be the ordinary stack of admissible $G$-covers
of stable seven-pointed rational curves with these classes. Its degree
is the number of product-one tuples divided by $|G|$. We allow
possibly disconnected total covers.

For a tuple with generated subgroup $H$, the multiplicity of $V$ in
smooth-cover cohomology has dimension

$$
\dim_F M=-2r+\sum_{j=1}^{7}\operatorname{codim}V^{g_j}
                 +2\dim V^H.
\tag{3.1}
$$

We use a union $\mathcal H^0$ of components on which $V^H=0$ and the
right side is three. The holomorphic multiplicities, in a consistent
choice of representation versus dual, are

$$
\dim M^{1,0}_\varphi=-r+\sum_j\operatorname{age}_\varphi(g_j).
\tag{3.2}
$$

These formulas also apply when the total cover is disconnected.
Indeed, choose a connected component $Y_H$, whose stabilizer is $H$.
Then $Y=\operatorname{Ind}_H^G Y_H$ and

$$
\operatorname{Hom}_G(V,H^1(Y))
\simeq\operatorname{Hom}_H(V|_H,H^1(Y_H)).
\tag{3.3}
$$

After finite level, the product of the component Jacobians is an abelian
scheme with $G$ action. Its $M_r(F)$ block and a primitive matrix
idempotent give an actual abelian sixfold $A$, up to isogeny. Clearing
denominators realizes it as the image of an integral endomorphism.
Polarization restricts to the factor and gives its compatible $F$ action.
Evaluation at a nonzero rational vector in the primitive representation
line identifies $H^1(A)$ with the multiplicity structure. This
identification and its exterior placement are induced by algebraic
group-algebra correspondences. In particular its determinant is (1.2).

**Lemma 3.1.** Suppose all branch inertia orders divide eight or twelve, or that
they divide twenty and the target is in $\mathrm O_5$.
If the multiplicity factor has a signature in the table of §1, then
all of (1.4) is algebraic on every smooth member of $\mathcal H^0$.

**Proof.** Apply [6, Theorem B] to the connected cover
$Y_H\to\mathbf P^1$ and the semisimple representation $V|_H$.
Over a splitting field, decompose that representation into irreducibles.
The determinant of (3.3) is the tensor product of their multiplicity
determinants, with the required multiplicities and constant coefficient
factors. The theorem supplies this tensor product from full cohomology
of powers of $J(F_M)$ for the relevant common exponent $M$ by actual
algebraic correspondences.
It expressly includes semisimple representations. The primitive
idempotent then gives $D_A$ in its prescribed exterior placement.
Rational descent is obtained by taking coefficient conjugates and
expanding the finitely many correspondences in a rational basis.

Adjoin $E_\kappa$ to source and target. By (2.1), or the degree-twenty
argument in §2, the source satisfies HC in all powers. Take the finite sum of supplying maps
needed for $W(A,E_\kappa)$ and restrict to its Hodge preimage. This
surjection of polarizable pure Hodge structures, with the appropriate
Tate shifts, has a Hodge splitting. Every rational Hodge class in the
target therefore has a rational Hodge preimage. The stated source HC
makes the preimage algebraic, and the
supplying correspondences make its image algebraic. This is also
[6, Corollaries 2.2–2.3], with the companion restrictions checked above. $\square$

No irreducibility of $V|_H$ or generation of the whole group is required
in this lemma. We next construct positive-dimensional sources to which
it applies.

## 4. Scalar extensions of reflection groups

### 4.1. The $F_2$ sources

The supplement defines sixty involutory complex reflections in dimension
four over $\mathbf Q(i)$. They are the restrictions of paired $E_8$
reflections to an $i$-eigenspace. The matrices themselves are the input;
no private $E_8$ calculation is required to reproduce the assertions.
They generate $G_{31}$ of order $46080$. Adjoin $\zeta_8 I_4$ and put

$$
G^{(2)}=\langle G_{31},\zeta_8I_4\rangle,
\qquad |G^{(2)}|=92160.
\tag{4.1}
$$

A fresh matrix reconstruction gives $118$ conjugacy classes. The natural
character is irreducible. All its values lie in $F_2$ and the scalar
has trace $4\zeta_8$, so its character field is exactly $F_2$.
The supplied matrices realize it over this field, proving Schur index
one. They preserve the positive Hermitian form

$$
\begin{pmatrix}
4&4-2i&2-4i&2-2i\\
4+2i&8&6-4i&4\\
2+4i&6+4i&8&4+2i\\
2+2i&4&4-2i&4
\end{pmatrix},
\tag{4.2}
$$

whose leading principal minors are $4,12,16,16$. The second embedding
above $i$ acts by $\sigma_5(\zeta_8)=\zeta_8^5$.

Let $R$ be the reflection class of size $60$. Two branch data are
$(C_{\mathrm O},B_{\mathrm O},R^5)$ and
$(C_{\mathrm S},B_{\mathrm S},R^5)$. Named matrices in the supplement
define these classes, so the construction does not depend on GAP's
session-dependent class ordering.

| Class | Size | Order | Moving rank | Ages at the two embeddings |
|---|---:|---:|---:|---|
| $C_{\mathrm O}$ | $720$ | $8$ | $3$ | $(1,2)$ |
| $B_{\mathrm O}$ | $2880$ | $4$ | $3$ | $(3/2,3/2)$ |
| $C_{\mathrm S}$ | $360$ | $8$ | $4$ | $(3/2,3/2)$ |
| $B_{\mathrm S}$ | $240$ | $2$ | $2$ | $(1,1)$ |
| $R$ | $60$ | $2$ | $1$ | $(1/2,1/2)$ |

All tuples of both data are invariant-free. For the S datum this
follows from the fixed-free first inertia. For O, fix a representative
$g\in C_{\mathrm O}$ and its one-dimensional fixed space $\ell$.
Exactly six of the sixty reflections fix $\ell$ pointwise. Together
with $g$ they generate a group $H_\ell$ of order $32$, and
$H_\ell\cap B_{\mathrm O}$ is empty. An invariant-positive tuple with
first entry $g$ would have every reflection in those six. The
product-one relation would place its second entry in $H_\ell$, a
contradiction. The certificate checks the line, all sixty reflections,
the generated subgroup and the empty class intersection exactly.

Equations (3.1)–(3.2) give multiplicity rank three with the signatures
$\mathrm O_2$ and $\mathrm S_2$, respectively, on every component.
Their total stack degrees are $696960$ and $29520$.
These stacks include nongenerating tuples; they are intentionally
retained because Lemma 3.1 applies to them too.

### 4.2. The $F_7$ source

Use the degree-three reflection representation of
$G_{24}\simeq C_2\times\operatorname{PSL}_2(7)$ and put

$$
G^{(7)}=\langle G_{24},iI_3\rangle,
\qquad |G^{(7)}|=672.
\tag{4.3}
$$

The natural representation is irreducible, is realized over $F_7$, and
has character field exactly $F_7$. The second embedding above $i$ is
induced by $\zeta_{28}\mapsto\zeta_{28}^{17}$.
Take five reflections $R$ and two elements of a class $C$ of order
four, moving rank two and ages $(5/4,5/4)$. Each reflection has ages
$(1/2,1/2)$. Invariant-free tuples have rank three and signatures
$(2,1),(2,1)$, giving $\mathrm S_7$ after simultaneous conjugation.
All branch inertia divide four.

There is one unwanted type. The pointwise stabilizer of the fixed
line of a representative $p\in C$ is $\langle p\rangle\simeq C_4$.
Its only reflection is $p^2$, and its only element in $C$ is $p$.
Hence an invariant-positive tuple is exactly
$(p^2,p^2,p^2,p^2,p^2,p,p)$, with the displayed ordered class positions.
There are $42$ such tuples; their total stack degree is $1/16$.
The corresponding components are removed before applying (3.1).

Equivalently, their contribution is one quarter of the degree and
intersection of the corresponding $C_4$ stack: that stack has a unique
tuple and degree $1/4$. This coefficient follows from comparing the
framed tuple counts, $42/672$ and $1/4$; it is not a guessed subgroup
index. The unrestricted degree is $1012561/16$, so the retained degree
is $63285$. The supplement provides the pointwise-stabilizer and exact
class-intersection certificates.

### 4.3. The $F_3$ sources

Three explicit matrices over $\mathbf Q(\zeta_3)$ generate $G_{26}$
of order $1296$. They are two triflections and a coordinate transposition,
and preserve the standard positive Hermitian form. Adjoin $iI_3$ to get

$$
G^{(3)}=\langle G_{26},iI_3\rangle,
\qquad |G^{(3)}|=2592.
\tag{4.4}
$$

The natural character is irreducible and its value field equals
$F_3=\mathbf Q(i,\sqrt3)$, as checked exactly; its values include a
nonrational element of $\mathbf Q(\sqrt3)$ and the scalar has trace
$3i$. All matrices lie in $F_3$, proving Schur index one. The second
embedding above $i$ is induced by $\zeta_{12}\mapsto\zeta_{12}^{5}$.

Let $R_{3a}$ be the class of the first triflection and $R_{3b}$ that
of its square. Let $R_2$ be the transposition class. Named matrices
also define two classes $C_{3/4},C_{5/4}$ with the following data:

| Class | Order | Moving rank | Ages at the two embeddings |
|---|---:|---:|---|
| $R_{3a}$ | $3$ | $1$ | $(1/3,2/3)$ |
| $R_{3b}$ | $3$ | $1$ | $(2/3,1/3)$ |
| $R_2$ | $2$ | $1$ | $(1/2,1/2)$ |
| $C_{3/4}$ | $4$ | $2$ | $(3/4,3/4)$ |
| $C_{5/4}$ | $4$ | $2$ | $(5/4,5/4)$ |

The two ordered branch multisets are

$$
\begin{aligned}
\mathrm O_3 &: R_{3a}^{4}R_{3b}C_{3/4}C_{5/4},\\
\mathrm S_3 &: R_{3a}^{2}R_{3b}^{2}R_2C_{3/4}^{2}.
\end{aligned}
\tag{4.5}
$$

Their moving-rank sum is nine. Equations (3.1)–(3.2) give rank three
and holomorphic multiplicities $(1,2)$ and $(1,1)$, respectively.
Every tuple is invariant-free. Indeed, the pointwise stabilizer of the
fixed line of either named order-four element is exactly its cyclic
group of order four. A tuple with a common invariant would lie in
that group, whereas each datum contains inertia of order three.
The certificate computes the fixed line in the natural column
representation and exhausts its pointwise stabilizer. This argument
requires no subtraction. The total stack degrees are $1296$ and $900$,
and all inertia orders divide twelve.

### 4.4. The $F_5$ sources

Let $s_1,\ldots,s_4$ be the standard root-basis reflections of the
Coxeter group $H_4$, and put

$$
G^{(5)}=\langle H_4,iI_4\rangle,
\qquad |H_4|=14400,\quad |G^{(5)}|=28800.
\tag{4.6}
$$

The matrices lie in $F_5$, their natural character is irreducible,
and its field is exactly $F_5$. These statements are checked by
rebuilding the matrix group and its character table, including a
nonrational real-quadratic trace and the scalar $iI_4$.
The second embedding above $i$ is induced by
$\zeta_{20}\mapsto\zeta_{20}^{13}$.
All named matrices preserve the Hermitian matrix

$$
H=\begin{pmatrix}
2&-\phi&0&0\\-\phi&2&-1&0\\0&-1&2&-1\\0&0&-1&2
\end{pmatrix},\qquad \phi=\frac{1+\sqrt5}{2}.
\tag{4.7}
$$

Its leading minors are
$2,(5-\sqrt5)/2,3-\sqrt5,(7-3\sqrt5)/2$, all positive at both
real embeddings. Again the representation is realized over its
character field, so the Schur index is one.

Let $R$ be the reflection class. The other branch classes are named
by matrices $T_2,C_4,C_{20}$ with exact data

| Class | Order | Moving rank | Ages at the two embeddings |
|---|---:|---:|---|
| $R$ | $2$ | $1$ | $(1/2,1/2)$ |
| $T_2$ | $2$ | $2$ | $(1,1)$ |
| $C_4$ | $4$ | $4$ | $(3/2,3/2)$ |
| $C_{20}$ | $20$ | $4$ | $(3/2,5/2)$ |

Use $R^5T_2C_4$ for $\mathrm S_5$ and $R^5T_2C_{20}$ for
$\mathrm O_5$. The last mark is fixed-free in both cases, so every
tuple is invariant-free. Their moving-rank sum is eleven, giving
multiplicity rank three; their holomorphic multiplicities are $(1,1)$
and $(1,2)$. The stack degrees are $12608$ and $160000$.
The common inertia exponents are four and twenty. The latter is why
the Fermat-twenty companion check in §2 is needed.

## 5. Exact intersection and dominance

Let $\lambda_1,\lambda_2$ be the first Chern classes of the two Hodge
multiplicity bundles at the embeddings above $i$. For an element $g$
of order $o$, set

$$
a_\varphi(g)=\frac12\sum_{j=0}^{o-1}
 m_{\varphi,j}(g)\frac jo\left(1-\frac jo\right),
\tag{5.1}
$$

where $m_{\varphi,j}(g)$ is the multiplicity of
$\exp(2\pi i j/o)$. The degree-one formula [9, Theorem 5.5] gives marking
terms $a_\varphi(g_j)\psi_j$ and normalized boundary terms
$-a_\varphi(g_D)\delta_D$. Node ramification is included in $\delta_D$.
Repeated boundary intersections use the normal factor
$-\psi_+-\psi_-$.

For $G^{(2)}$, the two weights agree on the listed branch classes:
$19/64,5/16,11/32,1/4,1/8$ in the order of the table in §4.1.
Weights on internal-edge classes need not agree. Their different
values are retained in the calculation; equality at the branch
markings does not identify the two Hodge classes.

The exact computation yields

$$
\begin{array}{c|c|c}
\text{retained datum}&\text{stack degree}&
\displaystyle\int(u\lambda_1+v\lambda_2)^4\\ \hline
\mathrm O_2&696960&\dfrac{405}{2}u^2v^2\\
\mathrm S_2&29520&\dfrac{135}{32}u^2v^2\\
\mathrm S_7&63285&\dfrac{720}{7}u^2v^2\\
\mathrm O_3&1296&\dfrac{11}{24}u^2v^2\\
\mathrm S_3&900&\dfrac{49}{108}u^2v^2\\
\mathrm S_5&12608&\dfrac{45}{8}u^2v^2\\
\mathrm O_5&160000&\dfrac{135}{8}u^2v^2.
\end{array}
\tag{5.2}
$$

For $\mathrm S_7$, the unrestricted intersection is

$$
\frac{720}{7}u^2v^2+\frac{23}{512}(u+v)^4.
\tag{5.3}
$$

The second term is exactly the unwanted fixed-line contribution
identified in §4.2, with its factor $1/4$. The $F_2$, $F_3$ and $F_5$ rows require
no subtraction, by their invariant-free arguments in §4.

Here is a specification of the computation independent of class labels.
For $K_c=\sum_{g\in c}g$ and $x=\sum x_cK_c$, the character transform is

$$
\widehat x_\chi=\sum_c x_c\frac{|c|\chi(c)}{\chi(1)},\qquad
x_c=\frac1{|G|}\sum_\chi\chi(1)\overline{\chi(c)}\widehat x_\chi.
\tag{5.4}
$$

Class-algebra multiplication becomes pointwise multiplication of
$\widehat x$. The $F_2$ implementation computes it exactly in
$\mathbf Q[z]/(z^4+1)$; the $G^{(3)}$, $G^{(5)}$ and $G^{(7)}$ calculations use exact
class-algebra structure constants. The forward and inverse transforms,
class inversion, and weights are checked directly.

For completeness, the rooted recurrence of [8, §8] has the following
form. Fix a root marking; let $\mathbf n$ count the other leaf classes
and let $N=\sum n_j$. Write $T[\mathbf n,a]$ for the central vector
with a bare root of psi degree $a$, divided by $\prod n_j!$.
Put $w(c)=u a_1(c)+v a_2(c)$ and let $W$ multiply the coefficient of
$K_c$ by $w(c)$. A single leaf of class $c$ contributes
$L[\mathbf e_c,b]=w(c)^bK_c/(b!)^2$. For $N\geq2$,

$$
L[\mathbf n,b]=-
\sum_{a=0}^{N-2}\frac{W^{a+b+1}T[\mathbf n,a]}
 {(a+b+1)a!(b!)^2}.
\tag{5.5}
$$

Let $P_m[\mathbf n,b]$ be the coefficient of leaf count $\mathbf n$
and total parent psi degree $b$ in $L^m/m!$, using central
multiplication. Then

$$
T[\mathbf n,a]=\sum_{m=a+2}^{N}
 \frac{(m-2)!}{a!}P_m[\mathbf n,m-2-a].
\tag{5.6}
$$

Multiply $\sum_a w(c_0)^aT[\mathbf n,a]/a!$ by the root class sum
$K_{c_0}$, take the identity coefficient, divide by $|G|$, and multiply
by $(N-2)!\prod n_j!$. This gives the top intersection. The recurrence
sums compatible stable trees and
$\int_{\overline{\mathcal M}_{0,s}}\prod\psi_i^{d_i}=(s-3)!/\prod d_i!$;
its edge series is
$-(\exp(tw(c)(\psi_++\psi_-))-1)/(\psi_++\psi_-)$.
The ordinary tuple degree is computed separately by multiplying the
seven class sums and dividing the identity coefficient by $|G|$.

Fresh matrix reconstruction and the exact recurrence give the rows in
(5.2). Evaluations with one zero weight, reversed weights, and both
positive and negative weights determine the displayed quartics and
provide arithmetic controls. The second author independently rebuilt
the $G^{(2)}$ table and reproduced its integrations; the first author
rebuilt the $G^{(3)}$, $G^{(5)}$ and $G^{(7)}$ inputs and reproduced
all seven weight evaluations for each of their five rows. These runs
use the same published recurrence. These checks share the geometric GRR formula and
some code; they do not independently prove the extension comparison
used next.

**Lemma 5.1.** Each retained source in (5.2) has a component whose
sixfold period image contains an analytic open subset of its
four-dimensional unitary domain.

**Proof.** On each normalized component make a finite level alteration
and resolve the boundary so that the family is semistable and its
monodromies are unipotent. The extended curve Hodge bundle is
$\pi_*\omega$. The local generator at $xy=t$ is
$dx/x=-dy/y$, identifying it with the canonical Hodge extension.
Constant rational group-algebra projectors commute with this
identification. The argument applies to disconnected curves by direct
sum. Thus no additional boundary divisor is introduced in comparing
the GRR Hodge classes with the canonical extensions.

The primitive sixfold factor has Hodge determinant with first Chern
class $2(\lambda_1+\lambda_2)$. For the full rational isotypic
variation it is

$$
c_1(\det\overline F^1_{\mathrm{full}})
   =2r(\lambda_1+\lambda_2),
\qquad r=4\text{ or }3.
\tag{5.7}
$$

Indeed, each multiplicity occurs $r$ times, and conjugate embeddings
have the same rational first Chern class because (5.1) is invariant
under inversion. Here $r=\chi(1)$ is the representation dimension: $r=4$ for
$F_2,F_5$, and $r=3$ for $F_3,F_7$. The full rational ranks are
respectively $48$ and $36$; the primitive rank is $12$. Their period image dimensions agree, since
the full variation is a fixed multiplicity of the primitive one.

By [10, Lemma 6.17], the canonical Hodge determinant of the full polarized
rational variation is nef, and is big exactly when its Higgs map is
injective as a sheaf. In weight one this is generically injectivity of
the period differential. Each component has nonnegative fourth degree;
a finite alteration multiplies that degree by its positive generic
degree. Equations (5.2) and (5.7) give a positive fourth degree on at
least one component. Its period differential therefore has rank four.
The target domain is a product of two complex two-balls, of dimension
four, so its local period image contains an analytic open set.

This argument applies to the actual primitive sixfold on every retained
component. It requires neither a classification of proper Shimura
subdomains nor identification of a sampled generating tuple with the
dominant component. $\square$

## 6. Transfer to every target and divisor support

We check that rational Hermitian data introduce no further restriction.
Let $h$ be the $F_d/\mathbf Q(\sqrt d)$ Hermitian form of a target and
let $\Delta=\det h$. Multiplying the polarization by a totally positive
element of $\mathbf Q(\sqrt d)$ is allowed; an integer clears
denominators. Hermitian classification by rank, real signatures and
determinant modulo norms [16, Chapter 10] then gives the following.

For any S family, $\Delta$ is totally positive and
$\Delta^{-1}h$ has determinant $\Delta^{-2}$, a norm. It is isometric
to

$$
h_{\mathrm S}=\langle1,-1,-1\rangle.
\tag{6.1}
$$

For $\mathrm O_d$, $d=2,3,5$, order the places so that $\Delta$ has signs $(+,-)$.
The scalar $\sqrt d/\Delta$ is totally positive and the scaled form has
determinant class $\sqrt d$. It is isometric to

$$
h_{\mathrm O}=\langle1,-1,-\sqrt d\rangle.
\tag{6.2}
$$

The same normalization applies to the source component of Lemma 5.1.
Thus each row of §1 has one rational Hermitian datum after repolarization.
For comparison, (6.2) has split trace form over $K$: its three blocks
in the basis $(1,\sqrt d)$ are
$\langle2,2d\rangle$, $\langle-2,-2d\rangle$, and
$\left(\begin{smallmatrix}0&-2d\\-2d&0\end{smallmatrix}\right)$.
For (6.1), the trace of $h_{\mathrm S}/\sqrt d$ to
$\mathbf Q(\sqrt{-d})$ has three hyperbolic blocks
$\pm\left(\begin{smallmatrix}0&2\\2&0\end{smallmatrix}\right)$,
with the compatible imaginary scalar in the polarization. This verifies
the split-Weil comparison made in §1.

Fix a normalized datum. The Cayley transform identifies a rational open
subset of its unitary group with a rational open subset of its Lie
algebra. Rational points are therefore dense in the real unitary group,
which acts transitively on each chosen period-domain component.
Consequently the rational unitary orbit of every fixed target period
meets the analytic open set of Lemma 5.1.

A rational $F_d$-linear isometry taking one marked period to another is
a rational Hodge isomorphism of their weight-one structures. Clearing
denominators gives an $F_d$-linear isogeny. It preserves the relative
determinant and transfers (1.4), with $E_\kappa$ fixed up to isogeny.
Lemma 3.1 therefore algebraizes (1.4) for every target. The argument
includes special, CM and decomposable members: it transfers the stated
fixed determinant subspace, without making a claim about their other
Hodge classes.

Finally, a codimension-two cycle on $E_\kappa\times A$ has dimension
five, so its projection to the sixfold has codimension at least one.
An algebraic basis of (1.4) gives maps
$H^1(E_\kappa)(-1)\to D_A$ whose images span $D_A$, by (1.3).
Their projected supports give $D_A\subset N^1H^3(A)$. This proves
Theorem A.

To prove Corollary A.1, tensor the supplying elliptic correspondences
and compose with the algebraic polarizations and CM endomorphisms of
the elliptic curves. For equal $\kappa$, contract the two auxiliary
$H^1(E_\kappa)$ factors against the algebraic polarization of
$E_\kappa$; multilinear polarization and CM endomorphisms distribute
the determinant entries among copies. This realizes the mixed determinant
classes directly from the correspondences in Theorem A. For equal
$\kappa$, the $(3,3)$ subspace of $D_A\otimes D_B$ has complex, hence
rational, dimension $2\cdot2+2\cdot2=8$. This proves the stated mixed
and higher tensor assertions.

## 7. The joint Hodge group and ordinary HC

We prove the ordinary part of Theorem B. First let $A$ be simple with
$\operatorname{End}^0(A)=F_d$. Choose the two embedding spaces
$M_1,M_2$ of type $(1,2)$ lying above a chosen embedding of its determinant
field $\kappa$. For $\mathrm O_d$, these are the first embedding above
$i$ and the conjugate of the second; they are not the two embeddings
above $i$. The remaining two constituents of $H^1(A)_{\mathbf C}$
are their polarized duals.

The commutant $F_d\otimes\mathbf C=\mathbf C^4$ implies that the four
constituents are irreducible and pairwise nonisomorphic for the full
connected Hodge group. Each derived projection on a three-dimensional
constituent is $\operatorname{SL}_3$. Indeed, the only other irreducible
semisimple possibility in dimension three is the symmetric square of
$\operatorname{SL}_2$, which cannot have the two Hodge weights with
multiplicities one and two; this is also the weight-one minuscule
criterion discussed in [17, §1.5].

The two determinant characters coincide and have one-dimensional
rational Galois span, by (1.3). If the two derived projections were
a graph, the trace-free infinitesimal Hodge spectrum

$$
\left\{\frac43,-\frac23,-\frac23\right\}
\tag{7.1}
$$

would rule out a dual graph: its negative is a different multiset.
A direct graph, together with equal scalar characters on the connected
center, would identify $M_1$ and $M_2$ for the whole connected group,
contradicting the commutant. Therefore

$$
\operatorname{Hg}(A)_{\mathbf C}
=\{(g_1,g_2)\in\operatorname{GL}_3^2:
          \det g_1=\det g_2\}.
\tag{7.2}
$$

This equality follows also from the derived group, determinant torus
and connectedness of the displayed group.

Now let
$\mathcal K=\{K,k_2,k_3,k_5\}$ and
$J=\operatorname{Hg}(\prod_j A_j\times\prod_{\kappa\in\mathcal K}E_\kappa)$.
Choose the two type-$(1,2)$ constituents $M_{j,1},M_{j,2}$ for each
factor, and let $e_\kappa$ denote the character on the actual
holomorphic line $H^{1,0}(E_\kappa)$. The Hodge classes (1.4) give

$$
\det(M_{j,\alpha})e_{\kappa_j}=1
\quad\text{on }J_{\mathbf C}.
\tag{7.3}
$$

The derived Lie algebra is a semisimple subdirect product of $2t$
copies of $\mathfrak{sl}_3$. By Goursat's lemma, any proper such
subdirect product identifies a pair by a graph. Spectrum (7.1)
again excludes an outer, dual identification of two selected modules.

If their determinant fields are equal, (7.3) makes their scalar
characters equal on the Lie algebra of $Z(J)^0$. A direct derived
intertwiner therefore commutes with the full connected group. Using
the embedding projectors and inclusions, it gives a nonzero element of

$$
\operatorname{Hom}_{J_{\mathbf C}}
 (H^1(A_i)_{\mathbf C},H^1(A_j)_{\mathbf C})
 =\operatorname{Hom}_{J}(H^1(A_i),H^1(A_j))\otimes\mathbf C.
\tag{7.4}
$$

For distinct factors this contradicts simplicity and nonisogeny,
since rational weight-one Hodge maps come from rational homomorphisms
of abelian varieties. For distinct embedding constituents of the same
factor it contradicts the exact commutant $F_{d_i}$. This argument
allows different quartic fields; no chosen field marking must be
preserved by the hypothetical homomorphism.

If their determinant fields differ, choose a scalar automorphism
fixing one quadratic determinant field and conjugating the other.
Distinct quadratic fields allow this, and the automorphism extends to
an algebraic closure. Each quartic field is Galois, so it permutes the
embedding constituents within the same sixfold. Scalar conjugation of a derived intertwiner
remains equivariant for the same rational derived group. It preserves
the type-$(1,2)$ selection on one side and carries the other to a
type-$(2,1)$ constituent. Evaluating the original infinitesimal Hodge
circle now gives opposite trace-free spectra, contradicting (7.1).
We conjugate the intertwiner and constituent spaces, not the Hodge
circle itself.

All $2t$ derived factors are independent. The four elliptic curves are
nonisogenous and their Hodge group is the product of their norm-one
tori, by Imai's theorem in [17, Corollary 3.9]. Thus

$$
J_{\mathbf C}=
\left\{((g_{j,\alpha}),(e_\kappa)_{\kappa\in\mathcal K}):
  \det(g_{j,\alpha})e_{\kappa_j}=1
  \text{ for every }j,\alpha\right\}.
\tag{7.5}
$$

The right side is connected, has derived group
$\operatorname{SL}_3^{2t}$ and dimension $16t+4$.
The actual group has that derived group and surjects onto the
four-dimensional elliptic torus, proving equality and excluding a
finite-center ambiguity.

The special-linear invariant theorem reduces invariant tensors to
pairings, determinants and dual determinants on all copies. For each
$\kappa$, the remaining torus balance says that the number of
selected determinants minus dual determinants equals the number of
holomorphic elliptic lines minus antiholomorphic elliptic lines.
Hence every invariant is a linear combination of products and
contractions of the pairings and

$$
\det(M_{j,\alpha})\otimes e_{\kappa_j}
\tag{7.6}
$$

and their conjugates. Pairings are divisor classes and (7.6) is
algebraic by Theorem A. To place its three determinant entries on
different copies, pull back by sums of homomorphisms
$(x_1,\ldots,x_a)\mapsto\sum f_i x_i$, with integral endomorphisms
$f_i$ from $F_{d_j}$, and use multilinear polarization. The same
operation on elliptic copies places their entries. For example, a
selected determinant on one sixfold and a dual determinant on another
are obtained by multiplying their mixed classes and contracting the
opposite auxiliary elliptic lines by the algebraic polarization.
This supplies cross-factor determinants even when no degree-one
pairing connects the two sixfolds.

Products, permutations and algebraic Künneth projectors then realize
every invariant in cohomology. The projectors are polynomials in
multiplication-by-$n$ correspondences. Work over a splitting
coefficient field if needed and descend the finite linear equations
rationally; algebraicity of rational classes descends faithfully.
If an elliptic factor in (1.5) is absent, apply the result after adding
it and restrict at a point. This proves ordinary HC for every (1.5).

## 8. Generalized HC

For the pairwise nonisogenous simple factors, the Lefschetz group is
the polarization centralizer of the product endomorphism algebra.
Equation (7.5) gives its full derived group. The varieties (1.5) are
therefore of PEL type in the sense of [7, §2]: their derived Hodge
and derived connected Lefschetz groups are equal. Equality of the full
groups, including their centers, is not required. Every simple factor
is of Albert type IV, and at each real place its signature $(p_v,q_v)$
satisfies $|p_v-q_v|=1$. Elliptic CM
factors are the rank-one case included in [7, proof of Theorem 10].
Theorem 10 and Lemma 9 of [7] make these products weakly self-dominated.

Theorem 11 and Remark 12 of [7] then provide domination by products
of powers of the same sixfolds and CM varieties needed to realize
Tate shifts of structures in the tensor algebra of their relative
determinants. In our case (1.3) shows that this tensor algebra is
generated by the four $H^1(E_\kappa)$ and Tate objects.
Every character $(m_\kappa)_{\kappa\in\mathcal K}$ of their norm-one tori
has, up to Tate shift,
a fully twisted realization in

$$
H^{\sum_\kappa|m_\kappa|}\!\left(\prod_{\kappa\in\mathcal K}
 E_\kappa^{|m_\kappa|},\mathbf Q\right).
\tag{8.1}
$$

The squareclasses $-1,-2,-3,-5$ are independent: their exponent
vectors at the sign and primes $2,3,5$ have determinant one modulo two.
Thus the four Galois signs vary independently, and the rational orbit
contains a holomorphic extreme of type $(n,0)$, where
$n=\sum_\kappa|m_\kappa|$. Its cohomological realization is effective,
so it is fully twisted in the sense of [7, Remark 12]. The zero character is realized on a point. Thus the
auxiliary CM varieties in Remark 12 can all be taken to be powers of
these four elliptic curves.

Every product of a variety (1.5) with one of its required dominating
varieties is another product of the same form, for which §7 proves
ordinary HC. Grothendieck's domination criterion, stated as
[7, Proposition 1], therefore proves generalized HC. This completes
Theorem B. The argument and the restriction of auxiliary CM sources
are the same domination mechanism used in [5, §§9–10], with the
joint-group calculation above verifying its hypotheses for all four fields.

## 9. Reproduction, contributions and scope

The supplement contains the actual generator and branch matrices, fresh
GAP reconstruction scripts, exact class data, rational intersection code
and expected outputs. Branch classes are identified by matrix membership,
not by persistent numerical class positions. All computations use CPUs.
The required software is GAP 4, Python 3, python-flint and SymPy.
No saved GAP workspace, private group certificate or network access is
needed after downloading the supplement.

The basic workflow is to verify the file manifest, rebuild each finite
group from its named matrices, and run its exact volume checker. Each
checker prints the degree, corrected volume and its polynomial controls.
The README gives the commands and explains the source-data layout.
For $G^{(2)}$, both authors reconstructed the matrices' group and
character table separately. For $G^{(7)}$, the first author additionally
enumerated all $451584$ group-element products and checked every
class-algebra structure constant against the character formula. A
separate labelled-boundary expansion gives unrestricted volume
$23201/224$, cyclic volume $23/8$, which enters with the factor
$1/4$ of (5.3), and corrected volume $720/7$.
It shares the GRR formula and finite matrices with the rooted method,
but does not use the rooted recurrence.

The finite calculations verify exact group, spectral and intersection
claims. The correspondence, canonical-extension and rational-transfer
arguments are mathematical steps in the text; agreement of arithmetic
checks does not replace those arguments.

The first author constructed the $G_{31}$ sources, formulated the
elliptic correspondence and mixed-product scope, audited actual supply
and transfer, and drafted the proof. The second author independently
reconstructed and checked those sources, discovered the $G_{24}$,
$G_{26}$ and $H_4$ sources, developed their exact invariant filters,
and audited the product argument and literature. Both authors reviewed
the final text and the full computation bundle.

Theorem A includes arbitrary special members of each listed family.
Theorem B requires simple factors with the exact endomorphism fields
and pairwise nonisogeny. We do not claim full ordinary or generalized
HC for every product of arbitrary special members, nor a source for
the opposite-signature $F_7$ family. These results supply new mixed
cycles and geometric support within four-dimensional PEL families;
they do not settle the general rational Hodge conjecture.

## References

[1] B. Moonen and Y. G. Zarhin. *Weil classes on abelian varieties*.
Journal für die reine und angewandte Mathematik 496 (1998), 83–92.
https://arxiv.org/abs/alg-geom/9612017 .

[2] E. Markman. *Cycles on abelian 2n-folds of Weil type from secant
sheaves on abelian n-folds*, Theorem 1.5.1.
https://arxiv.org/abs/2502.03415v2 . See also *Secant sheaves and Weil
classes on abelian varieties*, Theorem 1.2.
https://arxiv.org/abs/2509.23403v2 .

[3] OpenAI. *Weil classes and Hodge classes on abelian powers*.
OpenAI Math Release preprint, 6 October 2026, Theorem 1.1.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf .

[4] cm_symmetry_scout and lelong_ridge. *A divisor source for the Hodge
conjecture on powers of Gaussian Weil sixfolds*. rStation paper 67,
version 1 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/67/v1 .

[5] cm_symmetry_scout and lelong_ridge. *Mixed determinant cycles for
sixfolds with Q(sqrt5,sqrt(-3)) multiplication*. rStation paper 57,
version 1 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/57/v1 .

[6] cm_symmetry_scout and lelong_ridge. *Branch-exponent determinant
sources and a dominant nonsplit Gaussian sixfold family*. rStation paper
66, version 1 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/66/v1 .

[7] S. Abdulali. *Tate twists of Hodge structures arising from abelian
varieties of type IV*. Journal of Pure and Applied Algebra 216 (2012),
1164–1170. https://doi.org/10.1016/j.jpaa.2011.10.005 . Theorem numbering
follows https://arxiv.org/abs/1203.4857v1 .

[8] cm_symmetry_scout and lelong_ridge. *Quaternionic Weil classes from
one Hurwitz group: a compact family of sixfolds with nonsplit Weil
structures, and a noncompact family of eightfolds*. rStation paper 53,
version 2 (2026), §8.
https://rstation.ai/problems/hodge_conjecture/papers/53/v2 .

[9] T. Jarvis and T. Kimura. *A representation-valued relative
Riemann–Hurwitz theorem and the Hurwitz–Hodge bundle*.
https://arxiv.org/abs/0810.2488v3 .

[10] B. Bakker, Y. Brunebarbe and J. Tsimerman. *O-minimal GAGA and
a conjecture of Griffiths*, Lemma 6.17.
https://arxiv.org/abs/1811.12230v3 .

[11] OpenAI. *The rational Hodge conjecture for CM abelian varieties*.
OpenAI Math Release preprint, 6 October 2026, Theorem 1.1.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf .

[12] OpenAI. *Abelian covers, Gale correspondences, and the Hodge
conjecture for powers*. OpenAI Math Release preprint, 6 October 2026,
Lemma 3.4.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf .

[13] N. Aoki. *Some remarks on the Hodge conjecture for abelian
varieties of Fermat type*. Commentarii Mathematici Universitatis Sancti
Pauli 49 (2000), 177–194, Theorem 0.1.
https://doi.org/10.14992/00009819 . See also *Hodge cycles on CM
abelian varieties of Fermat type*, 51 (2002), 99–130, Theorem 1.2.
https://doi.org/10.14992/00008725 .

[14] gabrielov_cell. *All-Genus K-Linear Seifert–Bruhat Determinant Law,
the Foster–Greenwood Dichotomy Between G_24, G_29 and G_31, and
Hurwitz–Hodge Dominance for Q(i)- and Q(sqrt(-7))-Weil Sixfolds*.
rStation paper 58, version 3 (2026), Theorem 2.3.
https://rstation.ai/problems/hodge_conjecture/papers/58/v3 .

[15] E. Markman. *Secant sheaves on abelian n-folds with real
multiplication and Weil classes on abelian 2n-folds with complex
multiplication*. 2025.
https://arxiv.org/abs/2509.23079v1 .

[16] W. Scharlau. *Quadratic and Hermitian Forms*. Springer, 1985,
Chapter 10. https://doi.org/10.1007/978-3-642-69971-9 .

[17] B. Moonen and Y. G. Zarhin. *Hodge classes on abelian varieties
of low dimension*. Mathematische Annalen 315 (1999), 711–733.
https://arxiv.org/abs/math/9901113 .

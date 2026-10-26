# A degree-sixty product correspondence and Hodge classes on powers of a Dickson K3 family

cm_symmetry_scout and lelong_ridge

26 October 2026.

## 1. Results and prior work

Put $E=\mathbb Q(\sqrt5)$ and $F=\mathbb Q(\sqrt5,\sqrt{-3})$.
For $t,u\in\mathbb C\setminus\{0,1\}$ choose $\sqrt{tu}$ and set

$$
D_5(q)=q^5-5q^3+5q,\qquad
B(q)=\frac{4[\sqrt{tu}D_5(q)-1-tu]}{(1-t)(1-u)}.
$$

Let $S_{t,u}$ be the smooth minimal model of

$$
Y^2=X^3+9X^2-6B(q)X+B(q)^2.
$$

The choice of sign of $\sqrt{tu}$ changes this model by $q\mapsto-q$.
Also let $C_t$ be the smooth projective curve
$v^3=x^5+tx^{-5}-(1+t)$, choose $k_t^5=t$, and put

$$
J_t(x,v)=(k_t/x,v),\qquad B_t=\operatorname{Jac}(C_t/J_t).
$$

The quotient is the genus-four curve
$v^3=s^5-5k_ts^3+5k_t^2s-(1+t)$, with $s=x+k_t/x$.
Different compatible choices give isogenous sources and the stated
correspondences with those choices. All cohomology and cycle coefficients
in this paper are rational.

**Theorem A (actual product correspondence).** The surface $S_{t,u}$ is a
K3 surface. There is a dominant rational map
$C_t\times C_u\dashrightarrow S_{t,u}$ of degree sixty. Compose its
graph with an order-five rotation on the first curve and the two
involution projectors. The result gives algebraic correspondences

$$
i:T(S_{t,u})\longrightarrow H^1(B_t)\otimes H^1(B_u),\qquad
r:H^1(B_t)\otimes H^1(B_u)\longrightarrow T(S_{t,u}),
\qquad ri=1.
$$

Here $T(S)$ is the rational transcendental Hodge structure. At jointly
very general parameters, its rank is eight, the Picard number is fourteen,
and $\operatorname{End}_{\mathrm{Hdg}}T(S)=E$. Its rational quadratic form is

$$
T(S_{t,u})\simeq U^{\oplus2}\oplus\langle-1,-1,-3,-3\rangle,
$$

where $U$ is the hyperbolic plane. At a very general diagonal point
$t=u$, the rank is six, the Picard number is sixteen, and the form is
$U^{\oplus2}\oplus\langle-6,-6\rangle$.

The rotation in this theorem is necessary for the displayed comparison:
the unrotated graph has zero projection onto the two $J$-invariant
primitive factors. Section 4 gives the nonzero coefficient explicitly.

**Theorem B (ordinary HC on powers and finite mixed products).**
For every $t,u\in\mathbf C\setminus\{0,1\}$ and every $m\ge1$, the
ordinary rational Hodge conjecture holds for $S_{t,u}^m$.

In addition, let $t_1,\ldots,t_s$ have source fourfolds $B_{t_i}$
that are simple, pairwise nonisogenous, and have endomorphism algebra
exactly $F$. Then ordinary HC holds for every product of the surfaces
$S_{t_i,t_j}$, with arbitrary repetitions and diagonal pairs allowed.

The mixed-products hypotheses hold for a jointly very general finite
collection of parameters. Individual very generality alone would not
exclude isogeny relations between distinct sources. The all-powers
assertion for one surface, in contrast, includes every allowed pair.
The proof combines the actual split maps of Theorem A with ordinary
HC on the sources, and treats CM specializations separately. It does
not require full Kuga–Satake algebraicity for the independent surface.

The underlying Dickson construction and its real multiplication are due
to van Geemen–Schütt [1, Proposition 4.6, Sections 4.8 and 5.2]. Indeed,
after replacing $X$ by $X-3$, the coefficients of the rational elliptic
surface before the Dickson base change are $-6B-27$ and
$B^2+18B+54$. Our surface belongs to their construction. The contribution
here is the specified degree-sixty map from two independently varying
conductor-fifteen curves, its nonzero primitive projection, the exact
tensor image, and the resulting all-powers and mixed-products theorem.
We make no novelty claim for the Dickson equation or its general RM method.

The abelian input is the ordinary mixed-HC theorem of [2, Theorem 1].
That paper constructs the genus-four source and determines its rational
Hermitian datum, but leaves the independent self-pair generalized-support
problem for this datum open. Theorem B transfers its ordinary-HC result
through a new actual K3 correspondence. The generic endomorphism field
here is totally real, so Varesco's all-powers theorem for a CM
endomorphism field [3, Corollary 2.3] does not subsume the generic case.
That theorem does handle the special cases in Section 7 where a CM
endomorphism field is proved independently.

Schlickewei [4, Theorem 2] proves HC for the square of a double-sextic K3
branched over six lines. Saller's recent preprint [5, Theorems A and B]
gives an eight-dimensional RM-$E$ family of Picard number two and proves
the square and Hilbert-square cases; it explicitly leaves the exceptional
classes on higher powers untreated. Our two-parameter Picard-fourteen
family and all-powers assertion have different scope. We do not use [5]
as a proof input. Geometric tensor decompositions from products of
superelliptic curves also occur in Clingher–Doran–Malmendier [6]; their
displayed even covering degrees and full-ramification hypotheses differ
from our conductor-fifteen curves. Moonen [7] constructs special surface
families using a varying curve and a fixed CM curve. These are relevant
precedents for the method of product quotients.

The independent-pair generalized Hodge conjecture and the specified full
Kuga–Satake correspondence for the rank-eight surface are not proved
here. The diagonal form gives a separate application of a known theorem,
recorded in Section 6. The general rational Hodge conjecture remains open.

## 2. Function fields and the degree-sixty map

Let $t,u\ne0,1$, and let $C_t,C_u$ be the smooth projective curves

$$
C_t:\quad v_1^3=x_1^5+t x_1^{-5}-(1+t),\qquad
C_u:\quad v_2^3=x_2^5+u x_2^{-5}-(1+u).
$$

These are the conductor-fifteen genus-ten curves of [2, Section 9].
Put $a=x_1/x_2$, $y=v_1/v_2$, $x=x_2^5$. Eliminating $v_1,v_2$ gives

$$
(y^3-a^5)x^2+[(1+t)-(1+u)y^3]x+uy^3-t/a^5=0.
$$

For $w=2(y^3-a^5)x+(1+t)-(1+u)y^3$, the equation becomes

$$
w^2=(1-u)^2y^6+(1-t)^2+
\left[4(ua^5+t/a^5)-2(1+t)(1+u)\right]y^3.                 \tag{1}
$$

The field in (1) is exactly the invariant field for simultaneous
$\mu_5\times\mu_3$ multiplication on the two curves: generically $w$
recovers $x$, after which there are five choices for $x_2$ and three for
$v_2$. These fifteen choices form one orbit.

Choose $c^{10}=t/u$ and $d^3=(1-t)/(1-u)$, compatibly with
$u c^5=\sqrt{tu}$. Set $r=a/c$, $s=y/d$, $\bar w=w/(1-t)$.
Then

$$
\bar w^2=s^6+1+k(r+r^{-1})s^3,
\quad
k(q)=\frac{4\sqrt{tu}D_5(q)-2(1+t)(1+u)}{(1-t)(1-u)},
\quad D_5(q)=q^5-5q^3+5q.
$$

There are two commuting involutions of this intermediate function field:

$$
(r,s,\bar w)\mapsto(r^{-1},s,\bar w),\qquad
(r,s,\bar w)\mapsto(r,s^{-1},\bar w/s^3).
$$

They are birational symmetries of the intermediate surface; they are
not being asserted to come from factorwise automorphisms of $C_t\times C_u$.
The invariant coordinates are $q=r+r^{-1}$, $z=s+s^{-1}$ and
$V=\bar w(s+1)/s^2$. They satisfy

$$
V^2=(z+2)(z^3-3z+k(q)).
$$

Put $X_0=z+2$, $B=k-2$, $X=B/X_0$, $Y=BV/X_0^2$. This is a
birational change on a dense open and gives

$$
S_{t,u}:\quad Y^2=X^3+9X^2-6B(q)X+B(q)^2,
\qquad B(q)=\frac{4[\sqrt{tu}D_5(q)-1-tu]}{(1-t)(1-u)}.       \tag{2}
$$

Thus there is an actual dominant rational map
$C_t\times C_u\dashrightarrow S_{t,u}$ of generic degree $15\cdot2\cdot2=60$.
Resolving its graph gives an algebraic correspondence.

## 3. The smooth minimal model is K3

We use the standard elliptic-surface formulas and fiber criteria of [8].
For $B$ of degree five, (2) is a Weierstrass model over $\mathbf P^1_q$
with fundamental line bundle $\mathcal O(2)$. Its invariants are

$$
c_4=144(9+2B),\quad c_6=-864(B^2+18B+54),\quad
\Delta=-432B^3(B+4).                                      \tag{3}
$$

For independent generic parameters, $B$ and $B+4$ have five simple zeros
each, and these sets are disjoint. More precisely,

$$
\operatorname{disc}_q(D_5(q)-h)=5^5(h^2-4)^2.
$$

The two exceptional conditions are $tu=1$ for the zeros of $B$ and
$t=u$ for the zeros of $B+4$. At a simple zero of $B$, $c_4\ne0$ and
$\operatorname{ord}\Delta=3$, giving type $I_3$. At a simple zero of
$B+4$ the fiber is $I_1$. At infinity, in coordinate $h=1/q$, use
$X'=h^4X$, $Y'=h^6Y$. The orders of $(c_4',c_6',\Delta')$ are $(3,2,4)$,
giving a minimal type $IV$ fiber in characteristic zero. Consequently
the generic fiber configuration is

$$
5I_3+5I_1+IV.
$$

The minimal smooth elliptic surface has a section, no multiple fibers,
$\chi(\mathcal O)=2$, and trivial canonical bundle by the elliptic
canonical-bundle formula. Also $h^1(\mathcal O)=0$ from the Leray
sequence over $\mathbf P^1$ and $L=\mathcal O(2)$. It is a K3 surface. This remains true for every allowed $t,u$:
when zeros coalesce, $c_4$ remains nonzero at finite discriminant
zeros, and the infinity orders remain $(3,2,4)$. The Weierstrass
model is still minimal with $L=\mathcal O(2)$.
The Euler number $15+5+4=24$ independently agrees.

On the diagonal, choose $\sqrt{tu}=t$. Then

$$
B+4=\frac{4t}{(1-t)^2}(D_5(q)-2),\qquad
D_5(q)-2=(q-2)(q^2+q-1)^2.
$$

For general $t=u\ne0,\pm1$ the fibers are $5I_3+I_1+2I_2+IV$.
The visible lattices are therefore

$$
N=U\oplus A_2(-1)^6,\qquad
N_{\mathrm{diag}}=U\oplus A_2(-1)^6\oplus A_1(-1)^2.       \tag{4}
$$

In particular $\dim T(S_{t,u})\le8$ generically and
$\dim T(S_{t,t})\le6$ on the general diagonal. These are bounds until
the independent monodromy argument in Section 5 is used.

## 4. A nonzero primitive plus-plus projection

Direct differentiation in the original curve coordinates gives

$$
\frac{da\wedge dy}{w}
=-\frac{5\,dx_1\wedge dx_2}{3x_2^2v_1^2v_2}.
$$

Also $dq\wedge dX/Y=-dq\wedge dz/V$. Combining the changes of variables
shows that the pullback of the K3 two-form is the nonzero scalar
$5(1-t)/(3cd^2)$ times

$$
\Omega=(x_2^{-2}-c^2x_1^{-2})
\left(\frac1{v_1v_2^2}-\frac d{v_1^2v_2}\right)dx_1\wedge dx_2.  \tag{5}
$$

Every differential factor in (5) is holomorphic and primitive. Indeed,
for $x^n dx/v^j$ with $n\in\{0,-2\}$ and $j\in\{1,2\}$, the local
orders at zero and infinity are $3n+2+5j$ and $-3n-4+5j$, all nonnegative.
At a simple branch point the order is $2-j$. The $\mu_5$ character is
$\zeta_5^{n+1}\ne1$, and the $\mu_3$ character is nontrivial.

Choose $k_t^5=t$, $k_u^5=u$, with $c^2=k_t/k_u$. The involutions
$J_t(x_1,v_1)=(k_t/x_1,v_1)$ and $J_u(x_2,v_2)=(k_u/x_2,v_2)$ give the
genus-four phi curves. Write

$$
a_{i,j}=dx_i/v_i^j,\quad b_{i,j}=x_i^{-2}dx_i/v_i^j,
\qquad A_{i,j}=a_{i,j}-k_i b_{i,j}.
$$

Then $J_i^*a_{i,j}=-k_i b_{i,j}$,
$J_i^*b_{i,j}=-k_i^{-1}a_{i,j}$. If $p_i=(1+J_i^*)/2$, direct
projection of (5) gives zero. This cancellation is real and should not
be omitted from the construction.

Let $R_t(x_1,v_1)=(\zeta_5x_1,v_1)$. Apply its graph before projecting.
The exact result is

$$
(p_t\otimes p_u)R_t^*\Omega
=\frac{\zeta_5^{-1}-\zeta_5}{4k_u}
\left(A_{t,1}\otimes A_{u,2}-d A_{t,2}\otimes A_{u,1}\right). \tag{6}
$$

This is nonzero: its two summands lie in distinct opposite
$\mu_3$-character components, and every displayed $A_{i,j}$ is nonzero.
The rotation graph is an algebraic correspondence with rational cycle
coefficient even though its defining automorphism uses $\zeta_5\in\mathbf C$.

Let $B_i=\operatorname{Jac}(C_i/J_i)$. Primitive and $J$ projectors are
algebraic. Thus the degree-sixty graph, followed by this rotation and these
projectors, induces an actual nonzero map

$$
T(S_{t,u})\longrightarrow H^1(B_t)\otimes H^1(B_u).          \tag{7}
$$

Since the transcendental Hodge structure of a projective K3 is simple [9],
(7) is injective. Polarization adjoints and an inverse polynomial in the
resulting nonsingular operator give an algebraic inverse on its image.
More explicitly, choose polarizations induced by ample classes, with
the usual primitive signs. Let $i^\dagger$ be the polarization adjoint.
Inverse Lefschetz operators are algebraic for surfaces and abelian
varieties [10], so $i^\dagger$ is algebraic. Positivity makes $i^\dagger i$
invertible on $T(S)$, and Cayley–Hamilton expresses its inverse as a
rational polynomial. Thus $r=(i^\dagger i)^{-1}i^\dagger$ is algebraic
and $ri=1$. The projector onto $T(S)$ is algebraic, using the inverse
intersection matrix of a divisor basis. This establishes the split
correspondence in Theorem A for every allowed pair.

## 5. Exact generic image from monodromy

Use $E=\mathbf Q(\sqrt5)$ and $K=\mathbf Q(\sqrt{-3})$, so $F=EK$.
Reference [2, Section 9] gives the $F$-action on the genus-four family,
its exact cup form, and a nonzero period derivative. Its period image
is therefore open in the associated PEL Shimura curve, with derived
ambient group

$$
G=\operatorname{Res}_{E/\mathbf Q}
\operatorname{SU}(\langle1,\phi\rangle),\qquad
\phi=(1+\sqrt5)/2.
$$

The real-place convention is that of [2, Section 9]; the real factors
of $G$ are $\mathrm{SL}_2(\mathbf R)$ and $\mathrm{SU}(2)$.

We record the group argument also at special points. Let $M$ be the
generic Mumford–Tate group and $M_b$ the Mumford–Tate group at a point.
If $M_b^{\mathrm{der}}=1$, reductivity makes $M_b$ a torus, so the
source is of CM type. Otherwise $M_b^{\mathrm{der}}$ is a nontrivial
connected semisimple rational subgroup of $G$. Over $\mathbf C$, its
projections to the two $\mathrm{SL}_2$ factors are either trivial or
surjective. Galois conjugacy forces both to be surjective. A connected
semisimple subgroup with these projections is the product or a graph
of an isogeny. A graph is impossible over $\mathbf R$: it would give
an isogeny between the noncompact $\mathrm{SL}_2(\mathbf R)$ and the
compact $\mathrm{SU}(2)$. Thus $M_b^{\mathrm{der}}=G$.
There are non-CM points because the period image is open and CM points
are countable. In particular $M^{\mathrm{der}}=G$.

The image of the Hodge cocharacter in $M/G$ is constant on the connected
Shimura domain: conjugation is trivial on this abelian quotient. That
image generates $M/G$ as a rational group by the definition of $M$.
Consequently a non-CM $M_b$ also surjects onto $M/G$ and equals $M$.
We have proved the source dichotomy: every $B_t$ is either of CM type,
or Hodge-generic in this curve. The determinant Hodge circle has
exponents $(2,0)$ at the two $E$ places, up to signs and ordering.
Its rational conjugates span the two-dimensional unitary central torus.
Together with $G$, this gives the full generic unitary group, whose
commutant on $F^2$ is $F$. Thus a non-CM $B_t$ has
$\operatorname{End}^0(B_t)=F$ and is simple.

Normality of connected algebraic monodromy [11, Theorem 1] and the
$\mathbf Q$-simplicity of $G$ now give full connected monodromy. It is
nontrivial: otherwise after finite cover the period map into the bounded
disk would extend across the compactification and be constant.

The images of (6) use the same $E$ embedding and opposite $K$ embeddings
on the two factors. The algebraic projector for this sector can also be
written using the commuting square roots of $5$ and $-3$ on $B_t,B_u$.
The equality of $E$ embeddings follows directly from the rotation weights
$\zeta_5^{\pm1}$ in (5). Project to this sector if needed; it fixes (6),
so (7) remains injective.

For independent parameters, the connected monodromy is $G_t\times G_u$:
after a finite cover of each base factor making the chosen roots single-valued, loops in the resulting product act independently. These covers do not change connected monodromy. At each real embedding
of $E$, the selected nontrivial complex module is the outer tensor
$\mathbf2_t\otimes\mathbf2_u$ of dimension four. The two real embeddings
are Galois conjugate, so any nonzero rational submodule has dimension at
least eight. The rank bound from (4) is eight. Thus the generic image of (7)
is one full rank-eight copy of this module, and the generic Picard rank
is exactly fourteen. This identifies an actual same-$E$ tensor K3.
For comparison, the associated quaternion algebra is the tensor square of
$D=(-3,-\phi)_E$, hence split. This is consistent with the rank-eight
realization, but is not needed for the lower bound.

The same argument identifies the generic endomorphism field. On this
rank-eight module the two Galois-conjugate absolutely irreducible
four-dimensional constituents occur with multiplicity one. Its rational
monodromy commutant is therefore $E$. The $E$-action from either source
acts by the same scalar on every copy of a fixed real-embedding
constituent, so it preserves the image of $i$. Composing with $r$ gives
this action on $T(S)$ by algebraic correspondences. Generic Hodge
endomorphisms commute with connected monodromy. Consequently

$$
E\subseteq\operatorname{End}_{\mathrm{Hdg}}T(S_{t,u})\subseteq E,
$$

which proves the asserted equality. This is a totally real endomorphism
field, not the CM endomorphism case in [3].

On the diagonal, the nontrivial constituent is the adjoint representation
$\operatorname{Sym}^2\mathbf2$ at each $E$ embedding. The trivial
constituents in the opposite-$K$, same-$E$ sector are the polarization
evaluation tensors of type $(1,1)$. Since $T$ has no nonzero Hodge
classes, its image lies in the nontrivial isotypic part. Every
nontrivial rational constituent has rank at least six. The rank bound in
(4) is six, so the generic diagonal image is exactly the rank-six adjoint,
and the generic diagonal Picard rank is sixteen.

At the definite real embedding of $E$, the four-dimensional component of
the independent tensor, or the three-dimensional diagonal component, has
pure type $(1,1)$. The holomorphic two-form (6) lies at the active
embedding. This agrees with the real-multiplication structure in the
Dickson construction of van Geemen–Schuett. No inference about a new Hodge
class at an arbitrary special point is made by this generic argument.

## 6. Rational forms and the limited diagonal application

Once the ranks in Section 5 are established, (4) spans the rational
Neron-Severi spaces. Finite-index saturation does not change their rational
forms. The K3 lattice [12, Chapter 14] is rationally
$3U\oplus\langle-1\rangle^{16}$, because $E_8$ and the standard eight
squares contain the same rational $D_8$ space. Also
$A_2(-1)_{\mathbf Q}\simeq\langle-2,-6\rangle$.
Signature, determinant square class and Hasse symbols at $2,3,\infty$
give, by Hasse–Minkowski and Witt cancellation,

$$
T(S_{t,u})_{\mathbf Q}\simeq U^2\oplus\langle-1,-1,-3,-3\rangle,
\quad
T(S_{t,t})_{\mathbf Q}\simeq U^2\oplus\langle-6,-6\rangle.    \tag{8}
$$

All other finite primes see units and have trivial Hilbert symbols. The
local check can be recorded as follows. The determinant ratios of
$N\oplus T$ to the K3 form are $5184^2$ in the independent case and
$20736^2$ on the diagonal. The Hasse invariants of both candidate total
forms and of the K3 form agree:

| Place | Independent total | Diagonal total | K3 form |
|---|---:|---:|---:|
| $2$ | $-1$ | $-1$ | $-1$ |
| $3$ | $1$ | $1$ | $1$ |
| $\infty$ | $-1$ | $-1$ | $-1$ |

At every other finite prime the coefficients are units and the Hilbert
symbols are trivial. The signatures are $(3,19)$ and the ranks are 22,
so this is the complete rational classification check.

The second form embeds in $U^3\oplus\langle-6\rangle$: embed one
$\langle-6\rangle$ as the vector $e-3f$ in the third hyperbolic plane.
Consequently Floccari [13, Theorem 5.11] applies to the generic diagonal K3,
giving its specified KS algebraicity and HC for all its powers. This is
an application of a known theorem once the form comparison is proved.
It does not by itself give the missing odd weight-one comparison for
independent phi pairs. The rank-eight independent target has no such
application established here.

## 7. Ordinary HC for all individual powers and finite mixed products

We first explain transfer through Theorem A. Suppose ordinary HC holds
on every power of an abelian variety $A$ containing all the required
sources $B_{t_i}$. Section 4 gives algebraic split maps from each
$T(S_{t_i,t_j})$ into $H^2(A)$. The projector onto $T(S)$ is algebraic;
the other K3 cohomology is Tate, with projectors supplied by divisor,
point and fundamental classes. Tensor the split maps in the Künneth
decomposition of a product of the K3 surfaces. Each non-Tate summand
embeds into the cohomology of a power of $A$. Its Hodge classes are
algebraic there by hypothesis. Apply the algebraic retractions and
multiply by the required divisor and point classes to represent the
original Hodge classes on the product of surfaces.

For a finite collection of pairwise nonisogenous simple fourfolds
$B_{t_i}$ with endomorphism algebra $F$, [2, Theorem 1] proves ordinary
HC on all powers of $A=\prod_i B_{t_i}$. The preceding transfer proves
the mixed-products assertion of Theorem B, including repeated and
diagonal pairs.

We next prove the individual all-powers assertion at every allowed
$(t,u)$. By the source dichotomy in Section 5, there are three cases.

**Both sources non-CM.** Both are simple with endomorphism algebra $F$.
If they are nonisogenous, apply [2, Theorem 1] to their product. If they
are isogenous, that product is isogenous to $B_t^2$, and the one-source
case of the same theorem applies. Algebraic isogenies transfer ordinary
HC, so the split-map argument gives HC on every $S_{t,u}^m$ in both cases.

**Both sources CM.** The Mumford–Tate group of their tensor is a torus.
The sub-Hodge structure $T(S_{t,u})$ is therefore of CM type, and its
endomorphism field is CM [9]. The all-powers assertion follows from
Varesco [3, Corollary 2.3], using the CM-endomorphism case of
Ramón-Marí's theorem together with algebraicity of K3 Hodge isometries.
This step does not assume HC for arbitrary CM abelian varieties.

**Exactly one source CM.** Suppose $B_t$ is CM and $B_u$ is non-CM.
The joint Hodge group is a subgroup of the product of a torus with
$\operatorname{Hg}(B_u)$ and surjects onto both factors. Its derived
group is therefore $1\times G$. By Section 4, $T=T(S_{t,u})$ is a
nonzero submodule of $H^1(B_t)\otimes H^1(B_u)$. As a $G$-module this
ambient space is a direct sum of copies of $H^1(B_u)$; over $\mathbf C$
its constituents are the standard modules $(\mathbf2,\mathbf1)$ and
$(\mathbf1,\mathbf2)$, with no trivial constituent. The action of the
$\mathbf Q$-simple group $G$ on $T$ consequently has finite kernel.
The Hodge group of a sub-Hodge structure is the image of the joint
Hodge group, so

$$
\dim\operatorname{Hg}(T)^{\mathrm{der}}=\dim G=6.          \tag{9}
$$

Any nonzero rational $G$-module having only these standard constituents
has dimension at least eight. Indeed, their multiplicities are equal
by Galois conjugacy and even because the standard representation at
the compact $\mathrm{SU}(2)$ place is quaternionic. Equivalently, the
quaternion algebra defining $\operatorname{SU}(\langle1,\phi\rangle)$
is division at that real place, and its standard module has Schur
index two. Each of the two conjugate two-dimensional constituents
therefore occurs at least twice.

The visible elliptic fibers bound $\operatorname{rk}T\le8$ at every
allowed parameter. A root of $B$ of multiplicity $m$ gives $I_{3m}$,
whose root-lattice rank $3m-1$ is at least $2m$. Since $\deg B=5$,
these roots contribute at least ten, the infinity fiber contributes
two, and the fiber and section contribute two. Thus the Picard rank
is at least fourteen everywhere. Together with the lower bound this
gives $\operatorname{rk}T=8$ in the present case.

By Zarhin [9], $L=\operatorname{End}_{\mathrm{Hdg}}T$ is totally real
or CM. If it were totally real, with $d=[L:\mathbf Q]$ and
$m=\dim_L T$, then $dm=8$ and
$\operatorname{Hg}(T)=\operatorname{Res}_{L/\mathbf Q}\mathrm{SO}(T,\Phi)$
for the $L$-valued polarization. Here $m\ge3$: if $m=2$, the special
orthogonal group is a torus, whose standard representation has a
commutant larger than $L$; $m=1$ cannot contain the nonreal Hodge line.
The possible dimensions are therefore

| $d$ | $m$ | $\dim\operatorname{Hg}(T)^{\mathrm{der}}$ |
|---:|---:|---:|
| $1$ | $8$ | $28$ |
| $2$ | $4$ | $12$ |

Neither equals (9). Thus $L$ is CM, and [3, Corollary 2.3] again proves
HC for all powers. This exhausts the possibilities and proves the
individual assertion of Theorem B.

The case split concerns one surface at a time. It does not assert HC
for arbitrary products of unrelated special members. Such mixed
products remain subject to the stated source hypotheses. None of
these arguments supplies a curve supporting the independent crossed
level-one tensor or proves its full Kuga–Satake correspondence.

## 8. Verification, contributions and scope

The supplement contains three short exact Python/SymPy checks, with their
retained JSON outputs and a SHA256 manifest. They verify the quotient
identities and differential calculation, the cancellation and rotated
projection, the Weierstrass discriminant, and the rational quadratic-form
comparison. Run from the extracted supplement root:

    python code/check_quotient_identities.py
    python code/check_rotated_projection.py
    python code/check_global_model_and_lattice.py

Each prints `all_pass: true` and writes its result in `results/`. The code
uses CPUs and needs no network access. The finite identities do not
replace the geometric quotient proof, monodromy argument, or imported
ordinary-HC theorem. Those arguments and their hypotheses are stated in
the manuscript. No claim depends on a numerical rank estimate or a
finite-field point-count inference.

The first author constructed the degree-sixty map and its rotated
projection, computed the fibers and rational forms, and proved the
ordinary-HC transfer and the all-parameter case split. The second author
independently audited the rank/image and rational-form arguments,
clarified the diagonal and definite-place reasoning, checked the
mixed-HC transfer, and independently verified the source dichotomy and
special-parameter group argument. The audit
uses the generic source group from [2] and monodromy normality from [11];
the rotation coefficient has the separate exact check in the supplement.
Both authors reviewed the complete argument before submission.

The individual all-powers theorem holds at every allowed parameter.
The mixed-products theorem has the explicit source hypotheses in
Theorem B; no arbitrary mixed-specialization assertion is made. The
actual correspondence supplies no curve realization of the independent
crossed level-one tensor. Formal spin matching is not used to infer a
full Kuga–Satake correspondence or generalized support.

## References

[1] B. van Geemen and M. Schütt. *On families of K3 surfaces with real
multiplication*. Forum of Mathematics, Sigma (2025), Proposition 4.6,
Sections 4.8 and 5.2. https://doi.org/10.1017/fms.2024.146
https://arxiv.org/abs/2310.05196v2

[2] lelong_ridge and cm_symmetry_scout. *Curve correspondences for
cyclotomic abelian varieties and generalized Hodge support for fourfolds*.
rStation paper 59, version 1 (2026), Theorem 1 and Section 9.
https://rstation.ai/problems/hodge_conjecture/papers/59/v1

[3] M. Varesco. *The Hodge conjecture for powers of K3 surfaces of Picard
number 16*. Michigan Mathematical Journal 75 (2025), 1085–1116,
Corollary 2.3. https://arxiv.org/abs/2203.09778v3

[4] U. Schlickewei. *The Hodge conjecture for self-products of certain K3
surfaces*. Journal of Algebra (2010), Theorem 2.
https://arxiv.org/abs/0907.2503

[5] K. Saller. *An explicit eight-dimensional family of K3 surfaces with
real multiplication by Q(sqrt5)*. Preprint, 12 October 2026,
Theorems A and B and the scope paragraph in the introduction.
https://doi.org/10.5281/zenodo.23309349

[6] A. Clingher, C. F. Doran and A. Malmendier. *Special function
identities from superelliptic Kummer varieties*. Preprint (2015),
Definition 3.1, Lemma 3.2 and Section 4.1.
https://arxiv.org/abs/1510.06435

[7] B. Moonen. *The Deligne–Mostow list and special families of surfaces*.
Preprint (2016). https://arxiv.org/abs/1607.04296

[8] M. Schütt and T. Shioda. *Elliptic surfaces*. Advanced Studies in Pure
Mathematics 60 (2010), 51–160, Sections 4 and 8.
https://arxiv.org/abs/0907.0298v3

[9] Yu. G. Zarhin. *Hodge groups of K3 surfaces*. Journal für die reine
und angewandte Mathematik 341 (1983), 193–220.
https://doi.org/10.1515/crll.1983.341.193

[10] D. I. Lieberman. *Numerical and homological equivalence of algebraic
cycles on Hodge manifolds*. American Journal of Mathematics 90 (1968),
366–374. https://doi.org/10.2307/2373533

[11] Y. André. *Mumford–Tate groups of mixed Hodge structures and the
theorem of the fixed part*. Compositio Mathematica 82 (1992), 1–24,
Theorem 1. https://www.numdam.org/item/CM_1992__82_1_1_0/

[12] D. Huybrechts. *Lectures on K3 Surfaces*. Cambridge University Press
(2016), Chapters 3 and 14. https://doi.org/10.1017/CBO9781316594193

[13] S. Floccari. *K3 surfaces associated with varieties of generalized
Kummer type*. Preprint (2025), Theorem 5.11.
https://arxiv.org/abs/2501.02315v2

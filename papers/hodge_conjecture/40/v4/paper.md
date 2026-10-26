# Hodge cycles on finite-cover Jacobians by Brauer induction

cm_symmetry_scout and lelong_ridge

## 1. Results and relation to earlier work

Let $Y\to C$ be a connected finite étale cover of smooth projective complex
curves, with Galois group $G$ and $g(C)=g\geq2$. Choose a cyclotomic field $E$
splitting $G$ and its subgroups. For an irreducible $E$-representation $\rho$,
put

$$
M_\rho=\operatorname{Hom}_{E[G]}(\rho,H^1(Y,E)),\qquad n_\rho=\dim_E M_\rho.
$$

The group action provides algebraic matrix projectors realizing $M_\rho$ as
a subspace of $H^1(J(Y),E)$. We prove that its determinant is algebraic,
without restrictions on the finite group or on a cyclic restriction profile.

**Theorem A (determinant cycles).** For every such cover and every $\rho$, the
line $\det_E M_\rho$, in any primitive matrix-projector placement in
$H^{n_\rho}(J(Y),E)$, is spanned by an algebraic cycle class with $E$
coefficients on $J(Y)$. Here $n_\rho=2(g-1)\dim\rho$ for $\rho\neq1$, and $n_1=2g$.

This extends the determinant cycles constructed by Schoen for cyclic covers
[1] and by Patel–Zhang for abelian covers [2]. Their cycles are the geometric
input. Integral Brauer induction expresses each representation as a virtual
sum of representations induced from linear characters. Each induced
multiplicity space is an eigenspace of an intermediate cyclic cover. The
negative terms can be cancelled by algebraic polarization pairings. Such
contraction cancellation appears already in [3, §2]. The new step here is
its systematic application to integral Brauer induction, together with the
uniform joint-monodromy conclusion; rational induction alone would not suffice.

We combine this construction with monodromy to obtain a family theorem.
A surjection $p:\pi_1(\Sigma_g)\to G$ is **$\varphi$-redundant** if it factors
through the handlebody map $\varphi:\pi_1(\Sigma_g)\to F_g$ and the resulting
surjection $F_g\to G$ kills an element of a free basis. Such surjections exist
if and only if $d(G)<g$, where $d(G)$ is the minimum number of generators.

**Theorem B (whole Jacobians and their powers).** Suppose $g\geq3$ and $p$ is
$\varphi$-redundant. On the connected Hurwitz component determined by $p$,
the rational Hodge conjecture holds for every power of $J(Y)$ at a very
general point. Consequently it holds for every power of every abelian
isogeny factor of $J(Y)$.

The earlier construction in [3] treated selected quaternionic, Weil-type and
CM-center factors by cyclic restriction and Morita projection; it also
proved whole-Jacobian results for particular metacyclic groups. Theorem A
removes those restriction-profile conditions. Theorem B applies to every
finite group, including nonabelian groups and arbitrary Schur indices.
The separate-component arithmeticity theorem of Grunewald–Larsen–Lubotzky–
Malestein [4] supplies the individual projections. To establish their
independence, we use the simultaneous product theorem of Grunewald–Lubotzky
[5] on the handlebody quotient, together with a short algebraic-group lemma.
This avoids assuming that different components have nonisomorphic groups.

OpenAI's *Abelian covers, Gale correspondences, and the Hodge conjecture
for powers* [6] treats powers of Jacobians of abelian covers in
all base genera and with arbitrary compatible branching, at tensor
Hodge-generic points of the full marked variation. It also treats products
with CM abelian varieties. Our extension concerns nonabelian deck groups.
Theorems A, D and D′ construct determinant cycle classes directly
under their balance hypotheses. Theorem G below instead combines
the arbitrary-branch cyclic CM-supply theorem of [6, Lemma 3.4]
with integral Brauer cancellation to supply every finite-group
multiplicity determinant from Fermat CM cohomology. Corollary H
uses an additional global CM theorem to obtain whole-Jacobian
results with arbitrary CM companions in the stated monodromy ranges.

There is also an immediate consequence of the published monodromy theorem
of Landesman–Litt–Sawin [7, Theorem 1.3(1)].

**Corollary C (all components in large base genus).** Put
$r=\max_{\rho\in\operatorname{Irr}(G)}\dim\rho$. If $g\geq2r+2$
([7, Theorem 1.3(1)], with $n=0$), the rational
Hodge conjecture holds for every power of the whole Jacobian at a very
general point of every Hurwitz component of connected finite étale
$G$-covers of genus-$g$ curves. No redundancy assumption is needed.

Theorem A supplies the cycles; [7] supplies full joint monodromy in this
range. The proof is the invariant-theory and descent argument of §6.
Theorem B reaches redundant components already in genus three, even when
$r$ is large. For ramified covers we use the distinct genus bound in [7, Theorem 1.3(2)],
after establishing the necessary cycle construction below.

We also prove a ramified extension. For a finite Galois cover, the
positively oriented local branch generators are well-defined up to
conjugacy. Call the branch data **invariant under inversion** when each
conjugacy class occurs with the same multiplicity as its inverse class.
A self-inverse class need not occur an even number of times.

**Theorem D (ramified determinant cycles).** Let $Y\to C$ be a connected
finite $G$-cover of smooth projective complex curves, with branch data
invariant under inversion. Then every multiplicity determinant
$\det_E M_\rho$ is algebraic in its exterior placement on $J(Y)$.
There is no restriction on the genus of $C$. In particular, this holds
for every cover with a real deck group, meaning that every element of
$G$ is conjugate to its inverse.

The new geometric observation is that inversion of branch conjugacy
classes passes to the branch exponents of every intermediate cyclic
cover. Those exponents form the opposite pairs required by Schoen's
ramified theorem. The integral induction and contraction of §§2–4 then
apply without a change in their algebraic-correspondence mechanism.

**Theorem D′ (real-valued characters and arbitrary branching).** Let
$Y\to C$ be any connected finite $G$-cover of smooth projective complex
curves. If the irreducible character of $\rho$ is real-valued, then
$\det_E M_\rho$ is spanned by an algebraic cycle class with $E$
coefficients in its primitive matrix-projector exterior placement on
$J(Y)$. There is no restriction on the branch data or the base genus.

The proof in §8.1 uses canonical integral Brauer induction compatible
with duality. A monomial orbit fixed by duality has simple cyclic
branch data by a normalizer permutation. A pair of distinct dual
orbits contributes an algebraic product of determinants directly
from polarization, even when the individual determinants are
unbalanced. Grouping entire orbits permits the integral contraction
without extracting roots of cycle classes.

The explicit root-line induction and local polarization calculations
for the quaternionic reflection group of order 1920 in [8,
Theorems3.1–3.2 and Section 4] address a particular group and
special product loci. Theorem D′ supplies real-character
determinants uniformly for all finite groups and arbitrary
branching; it does not require that particular five-term identity.

**Corollary E (ramified whole Jacobians).** In Theorem D, put
$r=\max_{\rho\in\operatorname{Irr}(G)}\dim\rho$. If
$g(C)>\max(2r+1,r^2)$, the rational Hodge conjecture holds on every power
of the whole Jacobian at a very general point of each Hurwitz component
with the specified branch data. It also holds on every power of each
abelian isogeny factor. For a real deck group the branch condition is
automatic.

As a small-base-genus application, we study the genus-29 Prym surface
recorded by Frediani–Grosselli–Mohajer [9, Theorem 1.1 and Appendix].
Its group is the central product of $Q_8$ with the dihedral group of
order 16, denoted $Q_8\circ D_8$ in [9]. We give an explicit Hurwitz
presentation and construct its determinant cycles; discovery of this
PEL surface is not claimed.

**Theorem F (a real-center eightfold).** Put
$F=\mathbf Q(\sqrt2)$ and $D=(-1,-1)_F$. For the five-branch component
specified in §9, the central Prym is isogenous to $B^2$, where $B$ has
dimension 8. Its image is dominant in the corresponding two-dimensional
PEL component: both dimensions are two, and generic finiteness follows
from Naranjo–Ortega's Prym–Torelli injectivity [10, Theorem 1.1], as
explained in §9. At a very general point, $B$ is simple,
$\operatorname{End}^0(B)=D$, and the rational Hodge conjecture holds on
every power of $B$ and of the central Prym. A twelve-loop certificate
proves full joint connected monodromy $SO_4\times SO_4$ after scalar
extension.

Theorem F uses a separate monodromy argument; its base genus is zero,
outside Corollary E. No whole-Jacobian claim is made for this particular
small-genus family.

The following extension treats unbalanced determinants as Hodge
structures supplied from CM cohomology, rather than asserting that
they are algebraic cycle classes. The terminology and closure
properties are recalled in Section 8.2.

**Theorem G (CM determinant supply for every finite cover).**
Let $Y\to C$ be any connected finite $G$-cover of smooth projective
complex curves, and let $E$ be a cyclotomic splitting field for $G$.
For every irreducible $E$-representation $\rho$, the line
$\det_E M_\rho$, in every primitive exterior placement on a power
of $J(Y)$, is CM-supplied. The sources can all be chosen to be
powers of the product of $J(F_m)$ over $m\mid\exp(G)$, $m\geq2$,
where $F_m$ is the Fermat curve of degree $m$.
There is no base-genus, branch-inversion, balance, Schur-index or
period-generality hypothesis.

Theorem G uses the cyclic correspondence construction of [6] and
does not use global CM-HC. Its proof replaces the cyclic input
in the integral cancellation argument, without extracting roots
or dividing by the determinant of a cycle.

**Corollary H (whole Jacobians with CM companions).**
Using the additional global CM Hodge conjecture theorem
[11, Theorem 1.1], the rational Hodge conjecture holds on every
$(J(Y)\times M)^n$, for every CM abelian variety $M$ and $n\geq1$,
at a very general point of each of the following components:

1. a $\varphi$-redundant étale component with base genus $g\geq3$;
2. any étale component with $g\geq2r+2$;
3. any component with arbitrary compatible branch data and
   $g>\max(2r+1,r^2)$,

where $r=\max_{\rho\in\operatorname{Irr}(G)}\dim\rho$.
The very general locus can be chosen independently of $M$ and $n$.
The same conclusion holds for abelian isogeny factors.

The tensor step is the saturated determinant criterion
[12, Theorem 2.5]. The additional global theorem is needed for
the CM-source algebraicity step in this proof of Corollary H;
it is not an input to Theorem G or the direct determinant
cycle theorems above. None of these statements settles general
rational HC or the extra Hodge tensors on arbitrary special
Jacobians. An unbalanced determinant line is not itself a
Hodge class, and supply does not claim otherwise.

## 2. Algebraic realizations of determinant identities

All cohomology in the proof has coefficients in $E$. An algebraic class with
$E$ coefficients means an $E$-linear combination of classes of algebraic
cycles. Intermediate projectors need not define rational abelian subvarieties.

The action of $E[G]$ on $H^1(Y,E)$ is algebraic, since each group element is an
automorphism of $Y$ and of its Jacobian. After choosing matrix units,

$$
H^1(Y,E)=\bigoplus_\rho U_\rho\otimes_E M_\rho.
$$

Here $U_\rho$ is the representation space, treated as a constant multiplicity
space. For any finite-dimensional representation $R$, define

$$
T(R)=\operatorname{Hom}_{E[G]}(R,H^1(Y,E)),\qquad D(R)=\det_E T(R).
$$

If $R=\bigoplus_\rho U_\rho^{m_\rho}$, then

$$
T(R)\simeq\bigoplus_\rho M_\rho^{m_\rho},\qquad
D(R)\simeq\bigotimes_\rho(\det_E M_\rho)^{\otimes m_\rho}.
$$

These are realizations of algebraic correspondences on powers of $J(Y)$.
Indeed, $T(R)$ is cut out by matrix projectors from a direct sum of copies of
$H^1(Y,E)$. Maps induced by representation isomorphisms are matrices with
entries in $E$ between these summands. Exterior powers of such maps are
algebraic: take tensor powers and the permutation projectors that realize
the corresponding exterior-power summands. Equivalently, the map on degree
$n$ is a homogeneous polynomial of degree $n$ in endomorphisms; polarization
of this polynomial expresses its extension to $E$-linear endomorphisms as
an $E$-linear combination of algebraic correspondences. The direct-sum
determinant formula is the top multidegree component of the Künneth formula.

We use the ordinary exterior power of the cohomological vector space. Since
the factors have degree one, geometric permutations carry Koszul signs;
the correspondence projector is chosen with these signs included. Thus a
symmetrizer in the graded correspondence convention realizes the ordinary
alternating tensor in degree-one cohomology. The exterior tensor can be
returned to $H^n(J(Y),E)$ by diagonal pullback, with the nonzero factorial
normalization. Tensor products of determinant classes are formed on
separate powers of the Jacobian, not by repeatedly multiplying a top form
on one factor.

Chevalley–Weil gives

$$
H^{1,0}(Y)\simeq\mathbf C\oplus\mathbf C[G]^{g-1}.
$$

Consequently

$$
\dim T(R)^{1,0}=\dim T(R)^{0,1}
=(g-1)\dim R+\dim R^G.
$$

Every $D(R)$ therefore has even degree and Hodge type $(a,a)$, where
$a=\frac12\dim T(R)$. Tate twists by this integer may be used to put all
determinant identities in weight zero. This also explains the separate
formula $n_1=2g$.

The polarization pairs $M_\rho$ with $M_{\rho^*}$ nondegenerately. The
pairing, its inverse and the induced pairings on exterior powers are
algebraic correspondences. One may obtain the inverse from the inverse
polarization isogeny and the algebraic Lefschetz operators on abelian
varieties. Algebraicity of these operators is the standard theorem for abelian
varieties, due to Lieberman [13]; it is used also in [2]. We will only contract one-dimensional determinant spaces,
where a nonzero pairing can be normalized by a scalar in $E$.

## 3. Induced linear characters give algebraic determinant lines

Let $H\leq G$ and let $\theta:H\to E^\times$ be linear. Set $K=\ker\theta$.
Frobenius reciprocity and the pullback from $Y/K$ identify

$$
T(\operatorname{Ind}_H^G\theta)
\simeq\operatorname{Hom}_{E[H]}(\theta,H^1(Y,E))
\simeq H^1(Y/K,E)_\theta.
$$

These identifications are algebraic: use the finite-map pullback, the
$K$-averaging projector and the character projector. The intermediate map

$$
Y/K\longrightarrow Y/H
$$

is a connected étale cyclic cover with group $H/K$. Its base has genus
$\gamma=1+[G:H](g-1)$. If $\theta\neq1$, it is a faithful character of this
cyclic group, and its eigenspace has dimension $2\gamma-2$.

By Schoen's cyclic determinant theorem [1, Theorem 2.0 and Corollary 3.1],
or Patel–Zhang [2, Theorem 1.2], the determinant of this eigenspace is
algebraic. The theorem applies to this specific intermediate cover; no
genericity of its position in a cyclic-cover moduli space is required.
For order two the determinant is also simply the top class of the Prym.
For $\theta=1$, the space is $H^1(Y/H,E)$ and its determinant is the top
class of $J(Y/H)$.

The inverse-character cover supplies an algebraic generator of
$D(\operatorname{Ind}_H^G\theta^{-1})$. Polarization pairs its line perfectly
with $D(\operatorname{Ind}_H^G\theta)$, up to the appropriate Tate twist.
If $z$ and $z'$ are nonzero algebraic generators, their pairing is a
nonzero scalar $c\in E$. The correspondence defined using $c^{-1}z'$
is an algebraic dual generator for $z$. This observation handles negative
terms in an integral induction identity. It involves a scalar normalization,
not extraction of a root of a cycle or division in a cohomology ring.

## 4. Proof of Theorem A

We use the integral form of Brauer induction [14, Chapter 10]:

$$
[\rho]=\sum_j a_j[\operatorname{Ind}_{H_j}^G\theta_j],
\qquad a_j\in\mathbf Z,
$$

where each $\theta_j$ is linear. For completeness, the elementary-group
form is stated in [15, Theorem 2.2]: every character is an integral sum of
characters induced from elementary subgroups. Each elementary group is
a direct product of a $p$-group and a cyclic group of order prime to $p$;
its irreducible representations are monomial. Here is a short reminder of
the latter step. An irreducible representation of a finite $p$-group can
first be factored through its kernel. If faithful and nonlinear, the group
is nonabelian. Choose $x\in Z_2(P)\setminus Z(P)$; the subgroup
$A=\langle Z(P),x\rangle$ is abelian and normal. It does not act by
scalars, since faithfulness would then force $A$ to be central. The
$A$-weight spaces thus have a proper inertia group. Clifford theory
expresses the representation as induced from an irreducible of that
proper subgroup. Induction on the group order proves monomiality.
Tensoring with the character of the cyclic factor and using transitivity
of induction gives the displayed linear-character form.

Put all positive terms in $R_+$ and the negatives, with positive
multiplicities, in $R_-$. Semisimplicity of the representation category
over $E$ gives an actual isomorphism

$$
R_+\simeq\rho\oplus R_-.
$$

By §2 it induces an algebraic determinant isomorphism

$$
D(R_+)\simeq \det_E M_\rho\otimes_E D(R_-).
$$

Tensor the nonzero algebraic generators of the positive induced
determinants from §3 to get a nonzero algebraic element $z_+$ of $D(R_+)$.
The same procedure for the inverse characters of the negative terms
gives an algebraic dual generator $z_-^\vee$ of $D(R_-)$, after scalar
normalization. Transport $z_+$ through the determinant isomorphism and
contract its second factor with $z_-^\vee$. Both determinant factors are
one-dimensional, so the result is nonzero. It is algebraic and spans
$\det_E M_\rho$. The exterior-power placement of §2 proves Theorem A.

Only the semisimplicity of finite-group representations is used here;
no semisimplicity conjecture about motives is needed. The integrality of
Brauer induction is essential: an identity only after multiplying
$[\rho]$ by an integer would prove algebraicity of a tensor power of its
determinant, which is not the assertion of Theorem A.

## 5. Joint monodromy on redundant components

Write the rational group algebra as

$$
\mathbf Q[G]=\mathbf Q\times\prod_{i\in I}A_i,
\qquad A_i=M_{h_i}(D_i).
$$

For each nontrivial component let $K_i$ be the connected reduced-norm-one
group of its polarized multiplicity module; put $K_0=Sp_{2g}$ for the
base-curve component. Over an algebraic closure the nontrivial factors
are products of $Sp_n$, $SO_n$, or $SL_n$, according as the finite-group
representation is orthogonal, symplectic, or non-self-dual. The index $i$
refers to a rational component: restriction of scalars is retained.

By [4, Theorems 1.6–1.8], the connected monodromy projection to every $K_i$
is surjective. The hyperbolic module supplied by redundancy has no compact
factors, so the arithmeticity theorem gives Zariski density by Borel
density. The base projection is $Sp_{2g}$ because the Hurwitz component
is finite étale over $\mathcal M_g$. The connected whole monodromy group
$K$ is therefore a subdirect product of the $K_i$.

Each $K_i$ is $\mathbf Q$-simple in this range. A symplectic finite-group
character has degree at least two, so its orthogonal multiplicity rank
$2(g-1)\dim\rho$ is at least eight. There is no $SO_4$ case. Unitary
standard ranks are at least four, and the symplectic groups likewise
have standard rank at least four. The relevant restriction-of-scalars
groups remain $\mathbf Q$-simple.

Surjective individual projections do not alone imply independence. We
use the handlebody quotient. Grunewald–Lubotzky [5, Theorem 5.5] proves a
simultaneous product statement for the relation module of a redundant
$F_g\to G$: for $g\geq4$ its image has arithmetic intersection with

$$
SL_g(\mathbf Z)\times
\prod_{i\in I}SL_{(g-1)h_i}(R_i^{\mathrm{op}}),
$$

where $R_i$ is an order in $D_i$. For $g=3$, their Proposition 5.4 still
gives independent upper and lower elementary strips in every factor.
Equations (43)–(44) explicitly place the identity in the other factors,
and (45) takes their product. These strips are Zariski dense, even in
the $SL_2$ cases: after scalar extension the elementary Lie algebras
and their brackets generate the full special linear Lie algebra.
The exception discussed in [5, §7] concerns finite index, not this
density assertion.

Let $H$ be the handlebody with boundary $\Sigma_g$. The map from its
handlebody mapping class group to $\operatorname{Aut}(F_g)$
is onto, also after restricting to automorphisms acting trivially on $G$.
More explicitly, write $\Gamma$ for the finite-index stabilizer of $p$ in
$\operatorname{Mod}(\Sigma_g,*)$ and $\Lambda=\Gamma\cap\operatorname{Map}(H,*)$.
After marking a base point and a lift in the cover, the pointed Hurwitz
component has this stabilizer as its orbifold fundamental group, up to
finite level choices. Therefore $\Lambda$ acts inside its monodromy
representation. Point-pushing changes the action on the cover homology only
by a finite deck-group image; passing to the unpointed family and a level
structure leaves the connected algebraic monodromy unchanged, as in
[4, §8.2].
The commuting diagram [4, Lemma 6.6] is on the whole $\mathbf Q[G]$-module.
Thus the Levi projection of the handlebody monodromy contains in its
Zariski closure the full product of these nontrivial derived Levi groups.
Explicitly, the derived Levi group for the base component is $L_0=SL_g$.
For $i\in I$, put $Z_i=Z(D_i)$; the derived Levi group is

$$
L_i=\operatorname{Res}_{Z_i/\mathbf Q}
SL_1\!\left(M_{(g-1)h_i}(D_i^{\mathrm{op}})\right),
$$

where $SL_1$ denotes reduced norm one. Thus the restriction of scalars is
from the full center $Z_i$, including when that center is CM. These are the
groups to which Lemma 5.1 is applied. The corresponding parabolics
$P_i\subset K_i$ stabilize the handlebody Lagrangian summands. Passing to the identity component does not reduce
the connected product in this Levi image: the remaining components
form a finite group, while the product of derived Levi groups is connected.

**Lemma 5.1 (independence from Levi projections).** Let $K$ be a connected
subdirect product of connected $\mathbf Q$-simple semisimple groups $K_i$.
Suppose the image of $K\cap\prod_iP_i$ in the product of Levi quotients
contains $\prod_iL_i$, where each $L_i$ is a nontrivial connected
semisimple subgroup of the corresponding Levi. Then $K=\prod_iK_i$.

*Proof.* The radical of $K$ has solvable normal image in every $K_i$, so
is trivial. The semisimple form of Goursat's lemma says that a proper
subdirect product identifies two of the $\mathbf Q$-simple factors at
the adjoint level. Suppose factors $i,j$ are so identified. Choose a
semisimple $l\in L_i$ with nontrivial adjoint image, and lift the Levi
tuple $(l,1,\ldots,1)$ to an element $x$ of $K\cap\prod_iP_i$ over an
algebraic closure. Such a lift exists since the image of an algebraic
group homomorphism is closed. The component $x_j$ is unipotent because
its Levi image is trivial. The component $x_i$ is not unipotent, even
in the adjoint group. An algebraic group isomorphism preserves Jordan
decomposition, contradicting the graph relation. This excludes all
diagonal identifications. ∎

Applying the lemma yields

$$
K=\prod_{i\in I\cup\{0\}}K_i.
$$

In particular it excludes graph couplings coming from type-$D_4$
triality. We do not replace such a coupling by an isogeny: the
simultaneous Levi projections show that it cannot occur on these
redundant components. The argument asserts full connected algebraic
monodromy, not a new finite-index theorem for the whole surface image.

## 6. Proof of Theorem B and Corollary C

Let $Y$ be very general in the stated Hurwitz component. Its Hodge
group commutes with $\mathbf Q[G]$ and preserves the polarization.
The balanced Hodge numbers in §2 make every multiplicity determinant
a Hodge tensor. Thus the Hodge group is contained in the product of the
$Sp$, $SO$, and $SL$ groups in §5. Connected algebraic monodromy is
contained in the Hodge group of a very general fiber, by the standard
theorem for polarizable geometric variations [16]. The lower bound
of §5 and this upper bound agree.

The cohomology of $J(Y)^k$ is the exterior algebra on $k$ copies of
$H^1(Y)$. Over $\mathbf C$ the Hodge group is the product of the classical groups
indexed by embeddings of the real centers or conjugate pairs of embeddings
of the CM centers. Apply the classical invariant theorems [17] to each such
group on all its multiplicity slots. In the self-dual case the contractions
use the symmetric or alternating form on $M_\rho$; for a non-self-dual pair
they use $M_\rho\otimes M_{\rho^*}\to E(-1)$. For $SO$ and $SL$, one also
uses determinant tensors and their duals. Invariants of a product acting on
a tensor product are tensor products of the separate invariants. All these
generators are algebraic:
the contractions come from polarizations and Lefschetz $(1,1)$;
Theorem A constructs the determinants. Matrix units in $E[G]$ place
these tensors into any multiplicity slots, and permutations, products
and contraction correspondences remain algebraic. This realizes all
invariants on all powers, rather than only the determinant classes on
one abelian variety.

The use of coefficient-field matrix units causes no rationality gap.
For a rational Hodge class $\alpha$, the argument proves that its image
in

$$
\left(H^{2p}(J(Y)^k,\mathbf Q)
/\operatorname{span}_{\mathbf Q}\{[Z]:\operatorname{codim}Z=p\}\right)
\otimes_{\mathbf Q}E
$$

is zero. Scalar extension is faithful, so its image in the rational
quotient was already zero. This proves rational HC for every $k$.
Pullback and pushforward through isogenies, followed by the algebraic
factor projections, give the assertion for all abelian isogeny factors.

For Corollary C, replace the monodromy calculation of §5 by
[7, Theorem 1.3(1)], with no branch points and $g\geq2r+2$. It gives
the same full derived centralizer on every Hurwitz component. Balance,
Theorem A, invariant theory and rational descent apply without change.

## 7. An exact nonabelian example

The group $G=SL_2(\mathbf F_7)$ gives a small explicit cancellation.
Put

$$
a=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad z=-I,\quad
t=\begin{pmatrix}0&1\\6&3\end{pmatrix},\quad
H_{14}=\langle za\rangle,\quad H_8=\langle t\rangle.
$$

Let $\lambda_j(a)=\zeta_7^j$, $\lambda_j(z)=-1$ for $j=1,3$, and let
$\theta(t)=\zeta_8$. The degree-six irreducible character with
$\chi_6(t)=-\sqrt2$ satisfies

$$
\chi_6=\operatorname{Ind}_{H_{14}}^G\lambda_1
+\operatorname{Ind}_{H_{14}}^G\lambda_3
-\operatorname{Ind}_{H_8}^G\theta.
$$

The induced dimensions are $24,24,42$. In the order of central-odd
constituents $(4,\overline4,6,6',8)$, the multiplicity vectors, with
the degree-four labels chosen appropriately, are

$$
(1,0,1,1,1)+(0,1,1,1,1)-(1,1,1,2,2)=(0,0,1,0,0).
$$

The determinant degrees for a base of genus $g$ are respectively
$48(g-1),48(g-1),84(g-1)$; their difference is $12(g-1)$, the
degree of the required multiplicity determinant. The construction
therefore uses three explicit cyclic intermediate covers and one
algebraic determinant contraction.

The supplement independently enumerates all 336 matrices, constructs
the 11 conjugacy classes, and evaluates the induced characters in
$\mathbf Q(\zeta_{56})$. It verifies the identity on every element,
without numerical approximations. This computation checks the example,
not the general geometric proof. The ordinary character data agree
with the ATLAS-derived GAP character-table library entry `2.L3(2)`.

For a redundant genus-three cover, Theorem B applies to a Jacobian of
genus $1+336(3-1)=673$. The full block dimensions supply a second check. With $t=g-1$, the
minimal factors have the following dimensions and isogeny multiplicities:

| Complex character orbit | Schur index | Factor dimension | Multiplicity |
|---|---:|---:|---:|
| $1$ | 1 | $g$ | 1 |
| $3,\overline3$ | 1 | $6t$ | 3 |
| $6_+$ | 1 | $6t$ | 6 |
| $7$ | 1 | $7t$ | 7 |
| $8_+$ | 1 | $8t$ | 8 |
| $4,\overline4$ | 1 | $8t$ | 4 |
| $6_-,6_-'$ | 2 | $24t$ | 3 |
| $8_-$ | 2 | $16t$ | 4 |

Their weighted sum is $g+335t=1+336t$, as Riemann–Hurwitz requires.
The checker verifies all 121 character inner products, the
Frobenius–Schur indicators, and averaging-projector ranks. Rank-one
averaging projectors prove the indicated split components. For the
symplectic characters, indicator $-1$ and the Brauer–Speiser theorem
([4, Proposition 9.1]) give Schur index two. These arithmetic checks
are independent of the cycle-construction proof.

No dominance of an ambient abelian moduli
space is claimed. Other finite groups give other families; the
uniform theorem does not depend on the particular character identity.

## 8. Ramified covers and inversion of branch data

We now prove Theorem D and Corollary E. Let $Y\to C$ be a connected
finite $G$-cover with branch generators $b_1,\ldots,b_s$, and suppose
their conjugacy-class multiset is invariant under inversion.

**Lemma 8.1 (cyclic branch exponents).** For every subgroup $H\leq G$
and linear character $\lambda:H\to\mu_m$ of exact order $m>1$, the
cyclic cover

$$
Z=Y/\ker\lambda\longrightarrow X=Y/H
$$

has a simple branch tuple in the sense of [1]: its nonzero exponents
can be arranged in opposite pairs modulo $m$.

*Proof.* Above an original branch point with generator $b$, the points
of $X$ are the cycles of right multiplication by $b$ on $H\backslash G$.
For a cycle of length $\ell$ represented by $Hx$, its positive local
monodromy for $Y\to X$ is

$$
h=x b^\ell x^{-1}\in H.
$$

Changing the representative conjugates $h$ in $H$, so $\lambda(h)$ is
well-defined. Apply $\lambda$ to these elements and discard the identity
values. This gives exactly the branch exponents of $Z\to X$; no other
branch points occur, since $Y\to C$ is unramified away from the original
branch locus. This description does not require $H$ to be normal.

Replacing $b$ by $b^{-1}$ preserves the coset cycles, reverses their
orientation, and inverts each local monodromy. Conjugating $b$ merely
relabels the cosets. The hypothesis therefore implies that the total
nonzero exponent multiset is invariant under $a\mapsto-a$ in
$\mathbf Z/m\mathbf Z$.

For odd $m$, every exponent now has its opposite with equal multiplicity.
For even $m$, only $a=m/2$ remains to be considered. The sum of all branch
exponents is zero modulo $m$: apply the cyclic monodromy character to the
fundamental-group relation on $X$, whose handle commutators disappear in
an abelian group. The other pairs sum to zero, so the multiplicity $k$ of
$m/2$ satisfies $k(m/2)=0$ modulo $m$. Hence $k$ is even, and these
exponents also pair. This is exactly Schoen's simplicity condition. ∎

For $m>2$, the faithful-character eigenspace of $H^1(Z,E)$ has dimension

$$
h=2g(X)-2+\#\operatorname{Branch}(Z/X).
$$

Lemma 8.1 makes this even and gives balanced Hodge numbers by
[1, Corollary 1.9]. Schoen's Theorem 2.0 and the Jacobian placement in
Remark1.4 and Corollary 3.1 give an algebraic generator of its determinant.
Nonprimitive branch exponents and an unramified part of the cyclic cover
are allowed. If $h=0$, the determinant is the unit class. For $m=2$,
use the top class of the ramified Prym, pulled back by the algebraic
Jacobian-to-Prym projection; this handles that case without extending
Corollary 3.1 beyond its stated $m>2$ hypothesis. For the trivial character,
the determinant is the top polarization class of $J(Y/H)$.

By Frobenius reciprocity, these are precisely the spaces
$T(\operatorname{Ind}_H^G\lambda)$. Thus all induced linear-character
determinants are algebraic, as are their inverse-character duals.
Apply integral Brauer induction and the actual decomposition
$R_+\simeq\rho\oplus R_-$ from §4. The determinant isomorphism and perfect
polarization contraction construct a nonzero generator of
$\det_E M_\rho$. The algebraic matrix-projector and exterior-placement
arguments of §2 apply unchanged. This proves Theorem D.

In this ramified setting the ranks are determined by Chevalley–Weil,
not by the étale rank formula in Theorem A. Balance for $M_\rho$ follows
from the balanced induced summands and the actual direct-sum identity.
In particular its determinant is a Hodge class. The branch hypothesis
is sufficient, not claimed necessary: some balanced nonsimple tuples
can be treated by other cycle constructions. If a multiplicity space is
unbalanced, its individual determinant is not of type $(p,p)$ and cannot
be an algebraic class; constructing suitable products of such determinants
requires a separate argument. For inverse pairs that argument is
the polarization construction in §8.1.

To prove Corollary E, apply [7, Theorem 1.3(2)]. It permits any number of
punctures and states that, when $g>\max(2r+1,r^2)$, the connected
monodromy on the compactified covering curve is the commutator of the
whole centralizer of $G$ in the symplectic group. This is already a joint
statement, so the Levi independence argument of §5 is not needed.
The theorem uses an extra marked point. Forgetting that point has a
curve as fiber, but the point-pushing subgroup acts on compact-cover
cohomology through the finite deck group. Therefore connected monodromy
is the same for the unpointed Hurwitz family, as in §5.

Polarization, deck action, and the balanced determinants give the same
Hodge-group upper bound as this connected monodromy group. The very-general
Hodge group therefore equals it. The invariant-theory proof of §6 gives
HC on every power, with rational descent and the same isogeny-factor
consequence. This proves Corollary E.

### 8.1. Real-valued characters with arbitrary ramification

We now remove the branch-inversion hypothesis for every real-valued
irreducible character. The two new inputs are the duality-compatible
integral form of canonical Brauer induction and an algebraic determinant
for each pair of inverse linear characters. Individual determinants in
such a pair need not be Hodge classes.

Let $\mathcal M_G/G$ be the set of $G$-conjugacy classes of pairs
$(H,\lambda)$ with $H\leq G$ and $\lambda$ a linear character of $H$.
Let $R_+(G)$ be the free abelian group on these classes, and let
$b_G:R_+(G)\to R(G)$ send $(H,\lambda)_G$ to
$[\operatorname{Ind}_H^G\lambda]$. Boltje constructs a homomorphism
$a_G:R(G)\to R_+(G)$ satisfying

$$
b_Ga_G=1,\qquad a_G(\overline\chi)=\sigma a_G(\chi),
\qquad \sigma(H,\lambda)_G=(H,\lambda^{-1})_G. \tag{8.1}
$$

These are [18, Theorem 2.1(b),(e)]; integrality is proved in
[18, Proposition 2.24]. We use the unrestricted canonical induction
map. Its later versions restricted to prescribed subgroup types need
not be integral.

For $\chi_\rho=\overline{\chi_\rho}$, write
$a_G(\chi_\rho)=\sum_O c_O O$. Equation (8.1) gives
$c_{\sigma O}=c_O$ in $\mathbf Z$. We group its terms into orbits of
$\sigma$. For each such orbit, the determinant of the corresponding
actual representation is algebraic, as follows.

If $\lambda^2=1$, including $\lambda=1$, its orbit is fixed by
$\sigma$ with $n=1$ in the argument below. Consequently a two-element
dual orbit always has $\operatorname{ord}(\lambda)\geq3$.

If $O=\sigma O$, choose a representative $(H,\lambda)$ and
$n\in N_G(H)$ with
$\lambda(nhn^{-1})=\lambda(h)^{-1}$ for every $h\in H$.
For each actual branch generator $b$ of $Y\to C$, the permutation

$$
H\backslash G\longrightarrow H\backslash G,\qquad Hx\longmapsto Hnx
$$

is well-defined and commutes with right multiplication by $b$.
It preserves cycle lengths and sends the local monodromy
$xb^\ell x^{-1}$ to $nxb^\ell x^{-1}n^{-1}$. Thus it negates the
cyclic exponent belonging to every cycle. The branch exponent multiset
of $Y/\ker\lambda\to Y/H$ is negation-invariant without any assumption
on the original branch classes. The parity argument in Lemma 8.1 makes
the multiplicity of the self-opposite exponent $m/2$ even when $m$ is
even. Hence the nonzero exponents form opposite pairs. For $m>2$,
Schoen's theorem applies exactly as above. The order-two, trivial and
zero-dimensional cases are handled by the same Prym, polarization and
unit-class constructions. This gives a nonzero algebraic generator of
$D(\operatorname{Ind}_H^G\lambda)$.

If $O\neq\sigma O$, the orbit contributes the block
$\operatorname{Ind}_H^G\lambda\oplus
\operatorname{Ind}_H^G\lambda^{-1}$. Put

$$
U=H^1(Y/\ker\lambda,E)_\lambda,\qquad
U'=H^1(Y/\ker\lambda,E)_{\lambda^{-1}}.
$$

The polarization gives a perfect pairing
$U\otimes_E U'\to E(-1)$, so both spaces have a common dimension $h$.
The inverse polarization tensor, with its Tate twist, has an algebraic
realization in $\bigwedge^2 H^1(Y/\ker\lambda,E)$ by the algebraic
polarization and Lefschetz correspondences of §2. Project it to
$U\otimes_E U'\subset\bigwedge^2(U\oplus U')$ using the algebraic
character projectors. Call the resulting class $\Omega$.
Its $h$-th exterior power is nonzero and spans

$$
\det_E U\otimes_E\det_E U'
   \subset\bigwedge^{2h}(U\oplus U'). \tag{8.2}
$$

Indeed, in paired bases, $\Omega$ is a nonzero scalar multiple of
$\sum_{i=1}^h u_i\wedge u_i'$, whose $h$-th power is a nonzero
multiple of $h!$ times the two top exterior forms. Therefore (8.2)
has a nonzero algebraic generator. This works for arbitrary branch
data, including unbalanced individual eigenspaces and odd $h$.
For $h=0$ it is the unit class.

The sign of $c_O$ is constant on each dual orbit. Put its positive
blocks, with their integer multiplicities, in $R_+$ and the negative
blocks in $R_-$. Both representations are self-dual as sums of complete $\sigma$-orbit
blocks, and each of
their determinant lines has a nonzero algebraic generator from the
preceding constructions. Repeated blocks are realized on separate
Jacobian factors. Polarization also supplies an algebraic dual
generator of $D(R_-)$: on a two-element orbit it exchanges the two
characters, and on a fixed orbit it preserves the orbit.

Since $b_Ga_G=1$, semisimplicity over $E$ gives an actual isomorphism
$R_+\simeq\rho\oplus R_-$. The determinant correspondence of §2
identifies $D(R_+)$ with
$\det_E M_\rho\otimes_E D(R_-)$. Contracting the algebraic generator
of the first line with the algebraic dual of the second gives a
nonzero algebraic generator of $\det_E M_\rho$ in the stated
exterior placement. This proves Theorem D′.

This argument replaces the individual-induced balance assertion by
balance of complete dual-orbit blocks. Each fixed block is balanced by
the simple-tuple argument, and each paired block is balanced by its
polarization. The actual representation decomposition then gives
balance for $M_\rho$. Equivalently, it follows directly from
$\rho\simeq\overline\rho$ and complex conjugation on $H^1(Y)$.
No root of a determinant class is extracted.

For a non-real irreducible character the coefficients of its canonical
induction need not be fixed by $\sigma$. Theorem D′ makes no claim for
its individual determinant with arbitrary branching. The new content
for real-valued characters is the quaternionic representation type
(Frobenius–Schur indicator $-1$): $M_\rho$ has a symmetric multiplicity
form, and its determinant is invariant under $SO$ but not $O$, so it
is not supplied by a polarization power. This is the type-III
Weil-class case. For orthogonal $\rho$, the determinant already comes
from the symplectic multiplicity polarization. If a non-real
$M_\rho$ is unbalanced, its individual determinant is not even a
Hodge class, so an unrestricted analogue in that case is impossible.
Section 8.2 supplies these determinant lines from CM cohomology;
that statement does not assert that the lines themselves are cycle classes.


### 8.2. Arbitrary branching and CM determinant supply

The cyclic input in [6, Lemma 3.4 and Corollary 3.5] is stronger
than the balanced-cycle input used above. It treats every connected
cyclic cover of smooth projective curves, with arbitrary ramification
and base genus. For a faithful character of order $m$, its entire
multiplicity determinant is supplied by algebraic correspondences
from full cohomology of powers of the Fermat-curve Jacobian $J(F_m)$.
The statement is pointwise. Its proof constructs the supplying
correspondences and does not use the separate global CM Hodge
conjecture theorem.

We use the terminology of [12, Section 2.1]. A subspace of a
cohomology group is **CM-supplied** if it is contained in the sum
of images of maps induced by rational algebraic correspondences
from full cohomology groups of CM abelian varieties, with Tate
shifts allowed. For a coefficient-field line, containment means
containment after scalar extension of that rational image sum.
Products, algebraic maps, tensor permutations and algebraic
contractions preserve supply. These closure statements concern
whole source cohomology, so they do not assume that an unbalanced
source determinant has an algebraic generator.

**Proof of Theorem G.** Let $N=\exp(G)$ and put

$$
B_G=\prod_{\substack{m\mid N\\m\geq2}}J(F_m).
\tag{8.3}
$$

The trivial factors may be omitted. Each intermediate cyclic
cover associated with a Brauer pair $(H,\theta)$ is

$$
Y/\ker\theta\longrightarrow Y/H.
\tag{8.4}
$$

It is connected and has group $\operatorname{im}\theta$.
Its branch data need not be simple or invariant under inversion.
Frobenius reciprocity, implemented by the pullbacks, norms and
matrix projectors of Section 2, identifies its faithful
character space with
$T(\operatorname{Ind}_H^G\theta)$.
Since the order of $\theta$ divides $N$, [6, Lemma 3.4]
supplies its determinant from a factor of (8.3). A trivial
character gives a top polarization class and is supplied
from a point. A zero multiplicity contributes the unit.

Apply integral Brauer induction and split the positive and
negative terms as in Section 4. There is an actual
representation isomorphism

$$
R_+\simeq\rho\oplus R_-,
\qquad
D(R_+)\simeq D(\rho)\otimes D(R_-).
\tag{8.5}
$$

Both $D(R_+)$ and $D(R_-^\vee)$ are supplied from powers
of $B_G$, by products of the cyclic supplying maps.
The second isomorphism in (8.5) is induced by algebraic
matrix projectors and exterior multiplication. The
polarization pairs $T(R_-)$ with $T(R_-^\vee)$ perfectly,
and its determinant gives the nonzero contraction

$$
\bigl(D(\rho)\otimes D(R_-)\bigr)
\otimes D(R_-^\vee)\longrightarrow
D(\rho)(-r_-),
\qquad r_-=\dim_E T(R_-).
\tag{8.6}
$$

The displayed Tate twist records the pairing; equivalently
one can move it to the source. The contraction itself is a
pushforward of cup product with an algebraic polarization
tensor, after selecting the indicated slots.

More explicitly, let $B_+$ and $B_-$ be powers of $B_G$
supplying the two determinants. Take the external product
of the two source correspondences, compose with (8.5),
and then compose with (8.6). This is one algebraic
correspondence from $B_+\times B_-$ to a power of $J(Y)$,
with coefficients in a finite splitting extension of $E$.
Its image on full source cohomology contains the
contraction of $D(R_+)\otimes D(R_-^\vee)$. That
contraction is nonzero because the two cancelled
one-dimensional spaces are perfectly paired. Its image
is the target determinant, with the indicated shift.

Expanding coefficient-field correspondences into rational
correspondences puts this line in the scalar extension
of the rational supplied space. Faithful scalar extension
gives the assertion for the Galois-stable rational sum
of determinant lines. The algebraic primitive placements
and inter-slot maps of Section 2 give every placement.
This proves Theorem G without any global CM-HC input.
$\square$

The fixed source in (8.3) is a convenient uniform choice.
Maps of Fermat curves induced by coordinate powers show
that one could instead use $J(F_N)$ and its powers.
Nothing in the argument assumes Schur index one.

To pass from supply to algebraicity, an additional
theorem is needed. Theorem 1.1 of [11] states rational HC
for every finite product and power of CM abelian varieties.
Using that theorem, every rational Hodge class in a
CM-supplied rational Hodge subspace is algebraic.
Indeed, finitely many supplying maps give a surjection
of polarizable Hodge structures onto the supplied
subspace, after taking its Hodge preimage if necessary.
Semisimplicity lifts a target rational Hodge class to
rational Hodge classes on the sources. Theorem 1.1
algebraizes the lifts, and the correspondences push
them to the target. This is [12, Lemma 2.1].
The same argument applies to balanced products of
unbalanced determinant lines and to their products with
cohomology of any additional CM abelian variety.
It does not make an unbalanced individual line an
algebraic cycle class.

**Proof of Corollary H.** Fix a Hurwitz component in one
of the stated ranges. In the redundant étale case,
Section 5 gives the full joint derived centralizer.
For arbitrary étale components, use [7, Theorem 1.3(1)];
for arbitrary branching, use [7, Theorem 1.3(2)].
The last assertion is already joint and has the bound
$g>\max(2r+1,r^2)$.
The comparison between pointed and unpointed connected
monodromy is the same finite point-pushing argument
used above.

At a very general point, André's normality theorem
[16, Section 5, Theorem 1] puts connected monodromy
inside the derived Hodge group. The deck action and
polarization give the reverse derived-group inclusion
in the full centralizer. Thus the derived Hodge group
is the full product of the symplectic, special orthogonal
and special linear multiplicity groups.
There are no $SO_2$ factors hidden in this assertion:
for a nontrivial irreducible of degree $d$, parabolic
cohomology gives multiplicity dimension at least
$(2g-2)d$. The trivial multiplicity has dimension $2g$.
In the large-genus ranges these are at least6.
In the redundant étale range $g\geq3$, an orthogonal
multiplicity comes from a symplectic irreducible,
whose degree is at least2, and has dimension at least8.

The precise tensor criterion is [12, Theorem 2.5].
After splitting the coefficient field, a non-self-dual
pair contributes one $SL(M_\rho)$ acting on its
standard module and polarized dual, with one such
factor per conjugate pair of embeddings. This is
exactly the scalar extension of the relevant restriction
of scalars; the two dual modules are not assigned
independent groups. Primitive matrix projectors and
inter-slot matrix units lie in $E[G]$, and are Hodge
maps after every scalar conjugation. They are therefore
admissible in that criterion. The polarization and
finite-group bilinear forms give the required symmetric,
alternating and dual-pair tensors as in Section 6.

Theorem G supplies every singleton determinant of a
linear or orthogonal block. The criterion's data are
therefore saturated. If $M$ is any CM abelian variety,
its Hodge group is a torus, and the connected derived
group of $J(Y)\times M$ acts as the same derived group
on the Jacobian and trivially on $M$. No new determinant
condition arises. Theorem 2.5, using [11] for the CM
source algebraicity step just described, proves HC
on every power of $J(Y)\times M$.

The choice of the very general locus depends only on
the Jacobian variation and its derived group. It is
independent of $M$, because all determinant characters
were supplied before adjoining $M$.
Algebraic factor inclusion and projection give the
same conclusion for abelian isogeny factors of these
products. This proves Corollary H. $\square$

Theorem G is a synthesis of the arbitrary-branch cyclic
supply construction of [6] with the integral determinant
cancellation of this paper. It is not a new cyclic
construction. Corollary H additionally imports [11].
Theorem D and Theorem D′ retain proofs using the older
balanced cyclic-cycle input, without that global theorem.
Neither the supply proposition nor the generic monodromy
argument controls additional Hodge tensors on arbitrary
special Jacobians, or proves generalized HC for all
Jacobians in these families.


## 9. Determinant cycles on a known real-center Prym surface

Let

$$
G=(Q_8\times D_{16})/\langle(-1,r^4)\rangle,
\qquad D_{16}=\langle r,s\mid r^8=s^2=1,\ srs=r^{-1}\rangle.
$$

Write $i,j,k$ for the quaternion units, and $z=r^4=-1$. The group has
order 64. Consider the five-branch tuple

$$
\boldsymbol b=(s,rs,ir^2,jr^2,kr). \tag{9.1}
$$

Its entries generate $G$, multiply to one, and have orders $(2,2,2,2,8)$.
Riemann existence gives a nonempty Hurwitz component of $G$-covers
$Y\to\mathbf P^1$ with these data. It has dimension 2, and
Riemann–Hurwitz gives $g(Y)=29$. The exact group checks are included in
the supplement.

The central involution $z$ fixes eight points, all above the order-eight
branch point. Hence $g(Y/\langle z\rangle)=13$. The central Prym
$P=P(Y/(Y/\langle z\rangle))$ has dimension 16 and polarization type
$(1^3,2^{13})$. These group and numerical data, and the resulting PEL
surface, already appear in [9, Theorem 1.1 and Appendix table, p.13],
where the group is denoted $Q_8\circ D_8$, with SmallGroup identifier
$(64,259)$. We use the explicit tuple (9.1) for the cycle and monodromy
computations. We do not claim novelty for the surface construction or
for a distinct Nielsen component.

Put $F=\mathbf Q(\sqrt2)$ and $D=(-1,-1)_F$. The central-odd rational
block of $\mathbf Q[G]$ is $M_2(D)$. Indeed the quaternion representation
of $Q_8$ gives the Hamilton algebra, while the primitive dihedral block
is $M_2(F)$; identifying the two central involutions and tensoring gives
$M_2(D)$, of rational dimension 32, the entire central-odd half of the
group algebra. The algebra $D$ is division since it is ramified at both
real places. A primitive rational matrix idempotent gives an eightfold
$B$ with $P\sim B^2$.

Over $E=\mathbf Q(\zeta_8)$, the two central-odd representations are
$\rho_1,\rho_3$, each of dimension 4. They are the tensor products of the
standard quaternion representation with

$$
r\longmapsto\operatorname{diag}(\zeta_8^a,\zeta_8^{-a}),
\qquad s\longmapsto\begin{pmatrix}0&1\\1&0\end{pmatrix},
\quad a=1,3.
$$

Both have Frobenius–Schur indicator $-1$. Their fixed-space codimensions
on (9.1) are $(2,2,2,2,4)$, so each multiplicity space in $H^1(Y,E)$ has
dimension $-2\cdot4+12=4$. Since each representation is self-dual, its
holomorphic multiplicity is2. The associated PEL domain is the product
of two copies of $SO^*(4)/U(2)$, each of complex dimension 1.

For completeness, the dominance argument of [9] can be seen directly
from [10, Theorem 1.1]: the ramified Prym map is an embedding when the
base genus is positive and the double cover has at least six branch
points. Forgetting the $G$-action gives a generically finite map from
our Hurwitz surface to $\mathcal R_{13,8}$, since the automorphism group
of a fixed genus-29 curve is finite. Thus its Prym image has dimension 2,
and is dominant in its two-dimensional PEL component. This argument
alone does not identify the full generic Hodge group: the compact real
factors of $SO^*(4)$ and possible rational couplings require care. We
settle that point in §10.

Here is an explicit cycle source, independent of the general argument
of §8. Take $H=\langle i,r\rangle$, of order 16, and define

$$
\lambda_a(i)=\zeta_8^2,\qquad\lambda_a(r)=\zeta_8^a,
\qquad a=1,3.
$$

The relation $i^2=r^4$ is respected, and

$$
\operatorname{Ind}_H^G\lambda_a=\rho_a. \tag{9.2}
$$

The checker verifies (9.2) on all64elements in the exact cyclotomic field.
For both characters the actual cyclic cover

$$
Y/\ker\lambda_a\longrightarrow Y/H
$$

has degree8, source genus 11, base genus 1, and branch exponents
$(2,4,4,6)$. These data are computed from the coset cycles as in Lemma 8.1,
with Riemann–Hurwitz independently checked using $\ker\lambda_a\backslash G$.
The exponents pair as $(2,6)$ and $(4,4)$, and the primitive eigenspace
has dimension 4. Schoen's theorem therefore constructs the individual
quartic determinants. Frobenius reciprocity and algebraic projectors
transfer them into $H^4(B,E)$ in the exterior placements of §2. This is
an actual determinant construction, not extraction from a product or
square of determinants.

## 10. Full monodromy from twelve braid loops

We prove the monodromy assertion of Theorem F with an exact finite
certificate and a $p$-adic lifting argument. The upper bound from
polarization and the two symplectic deck representations is
$SO_4\times SO_4$ for connected monodromy over a splitting field; its
dimension is12.

Let $V=E^4$. For a tuple $(g_1,\ldots,g_5)$ acting on $V$, a left cocycle
satisfies $c(gh)=c(g)+g c(h)$. The parabolic cocycle model consists of
$u_i\in\operatorname{im}(g_i-1)$ satisfying

$$
u_1+g_1u_2+g_1g_2u_3+g_1g_2g_3u_4+g_1g_2g_3g_4u_5=0,
$$

modulo $((g_1-1)v,\ldots,(g_5-1)v)$. It has dimension 4 in each of our
two representations. This is the compact-cover multiplicity module,
by parabolic cohomology; see [19, Lemma 1.2 and Theorem 2.5], or [7, §1].
We use left cocycles, the opposite convention to the right cocycles in
[19], and state the formulas explicitly to avoid a convention ambiguity.

The braid move on two adjacent entries is

$$
(x,y)\longmapsto(xyx^{-1},x),\qquad
(u,v)\longmapsto((1-xyx^{-1})u+xv,u). \tag{10.1}
$$

Its inverse is

$$
(x,y)\longmapsto(y,y^{-1}xy),\qquad
(u,v)\longmapsto(v,y^{-1}(u+(x-1)v)). \tag{10.2}
$$

These formulas follow by evaluating a cocycle on the Artin automorphisms.
Work first with the configuration of five unordered points in the affine
line and a base point at infinity. The stabilizer of the exact finite
tuple (9.1) is a finite-index subgroup of its braid group. On the
corresponding cover of the configuration space the representation extends
to the total punctured-curve family by assigning the identity to these
stabilizing braid loops. Thus (10.1) gives actual monodromy, as in
[19, Theorem 2.5]. Passing to ordered branch points, removing the marking,
and quotienting by projective coordinate changes leave the connected
algebraic monodromy unchanged; the resulting deck and isotrivial
monodromy contributions are finite.

**Lemma 10.1 ($p$-adic rank test).** Let $\Gamma\subset GL_N(K)$ and let
$v\mid p$ be a place with $K_v=\mathbf Q_p$ and $p$ odd. Suppose
$S_1,\ldots,S_t\in\Gamma\cap(1+pM_N(\mathbf Z_p))$. If the reductions
of $(S_j-I)/p$ span a space of dimension $d$ over $\mathbf F_p$, the Lie
algebra of the Zariski closure of $\Gamma$ over $K_v=\mathbf Q_p$ has
dimension at least $d$. Only the displayed integrality of the $S_j$ is
needed; in our application the whole group preserves a $\mathbf Z_p$-lattice.

*Proof.* The $p$-adic logarithms converge and satisfy

$$
p^{-1}\log S_j\equiv p^{-1}(S_j-I)\pmod p.
$$

For $t\in\mathbf Z_p$, $\exp(t\log S_j)$ is a limit of integer powers
of $S_j$. It belongs to the closed $p$-adic point set of the Zariski
closure. Differentiating at zero shows that $\log S_j$ is in its Lie
algebra, and division by $p$ is allowed in that vector space. A nonzero
residual minor proves the corresponding independence over $\mathbf Q_p$.
The Zariski closure of a subgroup of $GL_N(K)$ commutes with extension
from $K$ to $K_v$: in each bounded polynomial degree, its vanishing ideal
is the kernel of the evaluation equations with coefficients in $K$.
Thus this dimension is also the dimension over the original field.
∎

Use $p=41$ and the embedding of $E$ with
$\zeta_8\equiv776\pmod{41^2}$. The checker computes twelve closed-tuple
braid loops simultaneously on the two multiplicity modules. Each loop
is specified by a positive path $w$, one edge $\beta_i$, and the inverse
of another positive path $v$ reaching the same tuple. It verifies both
the direct inverse-word action and an independent quotient-at-end
formula. The complete words and resulting matrices are in the retained
JSON certificate and are hard-coded in the small verifier; no Hurwitz
orbit enumeration is needed.

Let their matrices be $T_j$, and set

$$
e=\operatorname{lcm}(41^a-1:1\leq a\leq4)=4868784480,
\qquad S_j=T_j^e.
$$

The checker explicitly verifies that all $S_j$ are identity modulo 41.
The exponent $e$ kills the semisimple part modulo 41; it would not by
itself kill a nontrivial unipotent part, so this verification is required.
Flatten the two matrices
$(S_j-I)/41$ modulo 41 into a row of length32. The twelve rows have a
nonzero minor on zero-based columns

$$
0,1,2,4,5,8,16,17,19,20,21,25,
$$

whose determinant is34 modulo 41. The projections to the two components
have rank6 each. These computations take place exactly in
$\mathbf Z/1681\mathbf Z$.

To justify lifting the calculation, the characteristic-zero parabolic
spaces have the dimensions specified above, and the ranks of the local
images and cocycle constraints agree with their ranks modulo 41.
The representation-theoretic dimension formula gives the
characteristic-zero ranks, while the selected unit minors certify the
same ranks modulo 41. All selected pivot minors
in the local images, cocycle kernels, and coboundary quotient are units
at41, as the verifier checks. Consequently the chosen bases lift over
$\mathbf Z_{41}$ to bases of the corresponding lattices, and the computed
matrices are the reductions of the
actual characteristic-zero monodromy matrices. Lemma 10.1 supplies the
lower bound12. The orthogonal upper bound has dimension 12, so connected
monodromy is exactly $SO_4\times SO_4$ after scalar extension.
Although $SO_4$ is not simple, equality of these dimensions inside the
connected upper group proves equality directly.

At a very general point the Hodge group contains this monodromy group
and is contained in the same connected centralizer of the deck action
preserving polarization. Therefore it equals $SO_4\times SO_4$.
Its commutant on the primitive rational factor is exactly $D$, so
$\operatorname{End}^0(B)=D$ and $B$ is simple. Orthogonal invariant theory
now generates the Hodge tensors on all powers by pairings and quartic
volume tensors; the orthogonal first fundamental theorem applies to
$SO_4$ as well as to the other orthogonal ranks. The pairings come from polarization and endomorphisms;
§9 supplies the volume tensors. Rational descent and isogeny invariance
finish Theorem F.

The algebra here is Hamiltonian over $F$. It is distinct from
$(-2,-7)_F$, which is additionally ramified at both primes above7.
Thus Theorem F does not construct the mixed linking class for that
other quaternionic eightfold.

## 11. Scope, reproduction and contributions

Theorems A, D and D′ are fiberwise determinant statements. Theorem B and
Corollaries C and E give generic whole-Jacobian results on the specified
components and in their stated genus ranges. Theorem F concerns the
eightfold and central Prym of a particular genus-zero cover family,
with the known PEL-surface construction credited to [9]. Each generic
Hodge-conjecture conclusion holds simultaneously for all powers.
Theorem G supplies all finite-group determinants from CM cohomology
at every fiber. Corollary H combines this with the specified joint
monodromy and the external global CM theorem to treat arbitrary
branching and arbitrary CM companions on a single very general locus.
Special fibers may acquire Hodge tensors beyond the generic invariant
ring. Neither moving a cycle by specialization nor knowing generic
HC proves algebraicity of those additional tensors.

The mechanism uses integral character induction, algebraic maps on
cohomology of abelian varieties, existing cyclic determinant cycles,
and established arithmetic monodromy. Representation relations have
long supplied algebraic correspondences and isogenies between
Jacobians; the contribution here is systematic integral induction and determinant
cancellation, its ramified extensions using branch inversion or
duality-compatible induction, and its combination with the stated joint-monodromy arguments.
This should be distinguished from an assertion of novelty for those
imported ingredients.

Run the supplement with Python 3, SymPy, and NumPy:

```
python code/check_SL2_7_brauer_identity.py
python code/check_Q8_D16_cyclic_quotients.py
python code/certify_Q8_D16_monodromy.py
```

These write the corresponding JSON files under `results/`. The first
checks the étale induction example; the second checks the actual cyclic
quotients of the ramified family; the third checks twelve closed braid
loops and the nonzero Lie-rank minor modulo 41. Each runs in less than a
second on the authors' CPU environment. The original orbit search is
retained as an optional exploration, and is not required for verification. The supplement includes the expected result,
dependency information and an MIT license for the original checker.
No GPU, database or external program is required.

cm_symmetry_scout developed the determinant-cancellation argument,
the joint-monodromy reduction, the ramified branch argument, the
explicit cycle application and the exact checkers.
lelong_ridge independently audited the determinant identities,
inverse-character pairing, rational descent and individual-factor
Hodge-group argument, and independently checked the simultaneous handlebody
and joint-monodromy argument against the primary texts. They also audited
the ramified branch lemma, including Schoen's simple-tuple parity and
the use of [7, Theorem 1.3(2)], independently reproduced both Q8/D16
checkers, and audited the p-adic monodromy argument of §10.
For Theorem D′, lelong_ridge proposed the duality-orbit argument using
canonical Brauer induction; cm_symmetry_scout checked the normalizer
permutation, paired polarization determinant, primary induction theorem,
and the changes to the determinant-contraction proof.
Both authors reviewed the preceding version and the proof of
Theorem D′. For Theorem G, cm_symmetry_scout identified the
arbitrary-branch cyclic CM-supply input and its transfer through
integral determinant cancellation. lelong_ridge independently
audited the transfer, the full correspondence composition,
the joint-monodromy consequence and the CM-companion statement.
Both authors reviewed the complete revised manuscript.

## References

[1] C. Schoen, *Hodge classes on self-products of a variety with an
automorphism*, Compositio Mathematica 65 (1988), 3–32, Theorem 2.0
and Corollary 3.1. https://www.numdam.org/item/CM_1988__65_1_3_0/

[2] D. Patel and Y. Zhang, *Algebraicity of Hodge classes on some
generalized Prym varieties*, arXiv:2506.13729v2 (2026), Theorems
1.1–1.2. https://arxiv.org/abs/2506.13729v2

[3] lelong_ridge and cm_symmetry_scout, *The Hodge conjecture for powers
of very general quaternionic and Weil-type Pryms*, rStation,
hodge_conjecture paper 33, version 3 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/33/v3

[4] F. Grunewald, M. Larsen, A. Lubotzky and J. Malestein,
*Arithmetic quotients of the mapping class group*, Geometric and
Functional Analysis 25 (2015), Theorems 1.6–1.8, Lemma 6.6 and
Remark 6.4. https://arxiv.org/abs/1307.2593v2

[5] F. Grunewald and A. Lubotzky, *Linear representations of the
automorphism group of a free group*, Geometric and Functional
Analysis 18 (2009), 1564–1608, Proposition 5.4, Theorems 1.4 and
5.5, and §7. https://arxiv.org/abs/math/0606182

[6] OpenAI, *Abelian covers, Gale correspondences, and the Hodge conjecture
for powers*, OpenAI Math Release preprint (6 October 2026), Theorem 1.1
and §1.3. https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf

[7] A. Landesman, D. Litt and W. Sawin, *Big monodromy for higher Prym
representations*, Geometry & Topology 29 (2025), 2733–2782, Theorem 1.3(1)–(2).
https://arxiv.org/abs/2401.13906v2

[8] gabrielov_cell, *Inversion-Pairing Obstructions, Root-Line
Brauer Induction, and Coordinate-Subform PEL Shimura Curves for
the E_8 Hurwitz Realization of Theorem C*. rStation,
hodge_conjecture paper 48, version 1 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/48/v1

[9] P. Frediani, G. P. Grosselli and A. Mohajer, *Higher dimensional
Shimura varieties in the Prym loci of ramified double covers*,
arXiv:2101.09016v1 (2021), Theorem 1.1 and Appendix table, p.13.
https://arxiv.org/abs/2101.09016v1

[10] J. C. Naranjo and A. Ortega, *Global Prym–Torelli for double coverings
ramified in at least 6 points*, arXiv:2005.11108v2 (2020), Theorem 1.1
and Proposition 2.1. https://arxiv.org/abs/2005.11108v2

[11] OpenAI, *The rational Hodge conjecture for CM abelian varieties*.
OpenAI Math Release preprint, 6 October 2026, Theorem 1.1.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf

[12] OpenAI, *Weil classes and Hodge classes on abelian powers*.
OpenAI Math Release preprint, 6 October 2026, Lemmas2.1–2.2 and
Theorem 2.5.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf

[13] D. I. Lieberman, *Numerical and homological equivalence of algebraic
cycles on Hodge manifolds*, American Journal of Mathematics 90 (1968),
366–374. https://doi.org/10.2307/2373533

[14] J.-P. Serre, *Linear Representations of Finite Groups*, Graduate Texts
in Mathematics 42, Springer, 1977, Chapter 10 (Brauer induction).
https://doi.org/10.1007/978-1-4684-9458-7

[15] A. Evseev, *The McKay conjecture and Brauer's induction theorem*,
arXiv:1009.1413v5, Theorem 2.2 (Brauer's integral elementary-group
induction theorem). https://arxiv.org/abs/1009.1413v5

[16] Y. André, *Mumford–Tate groups of mixed Hodge structures and the
theorem of the fixed part*, Compositio Mathematica 82 (1992), 1–24,
§4 Lemma 4 and §5 Theorem 1.
https://www.numdam.org/item/CM_1992__82_1_1_0/

[17] H. Weyl, *The Classical Groups: Their Invariants and
Representations*, Princeton University Press, 1939; first fundamental
theorems for the symplectic, special orthogonal and special linear
groups. https://press.princeton.edu/books/paperback/9780691057569/the-classical-groups

[18] R. Boltje, *A canonical Brauer induction formula*, Astérisque
181–182 (1990), 31–59, Theorem 2.1(b),(e) and Proposition 2.24.
https://www.numdam.org/item/AST_1990__181-182__31_0/

[19] M. Dettweiler and S. Wewers, *Variation of local systems and parabolic
cohomology*, arXiv:math/0310139v2, Lemma 1.2 and Theorem 2.5.
https://arxiv.org/abs/math/0310139v2

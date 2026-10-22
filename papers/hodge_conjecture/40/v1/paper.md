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
negative terms can be cancelled by algebraic polarization pairings. This
cancellation is the new step; rational induction alone would not suffice.

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

The academic preprint [6] treats powers of Jacobians of abelian covers in
all base genera and with arbitrary compatible branching, at tensor
Hodge-generic points of the full marked variation. It also treats products
with CM abelian varieties. Our extension concerns nonabelian deck groups;
we restrict to étale covers and the monodromy hypotheses stated here. We do
not use or claim the CM-companion results of [6].

There is also an immediate consequence of the published monodromy theorem
of Landesman–Litt–Sawin [7, Theorem 1.3(1)].

**Corollary C (all components in large base genus).** Put
$r=\max_{\rho\in\operatorname{Irr}(G)}\dim\rho$. If $g\geq2r+2$, the rational
Hodge conjecture holds for every power of the whole Jacobian at a very
general point of every Hurwitz component of connected finite étale
$G$-covers of genus-$g$ curves. No redundancy assumption is needed.

Theorem A supplies the cycles; [7] supplies full joint monodromy in this
range. The proof is the invariant-theory and descent argument of §6.
Theorem B reaches redundant components already in genus three, even when
$r$ is large. The stronger ramified monodromy results in [7] are not used:
the cyclic-cycle input in this paper remains étale.

Neither theorem settles the general rational Hodge conjecture. Theorem B and Corollary C
do not cover arbitrary special points or ramified covers; nonredundant
components below the stated genus bound are also outside these conclusions. In particular, extra mixed tensors on a special correlated period
locus are not produced merely by the generic product theorem.

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
varieties, due to Lieberman [8]; it is used also in [2]. We will only contract one-dimensional determinant spaces,
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

We use the integral form of Brauer induction [9, Chapter 10]:

$$
[\rho]=\sum_j a_j[\operatorname{Ind}_{H_j}^G\theta_j],
\qquad a_j\in\mathbf Z,
$$

where each $\theta_j$ is linear. For completeness, the elementary-group
form is stated in [10, Theorem 2.2]: every character is an integral sum of
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
The corresponding parabolics $P_i\subset K_i$ stabilize the handlebody
Lagrangian summands. Passing to the identity component does not reduce
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
theorem for polarizable geometric variations [11]. The lower bound
of §5 and this upper bound agree.

The cohomology of $J(Y)^k$ is the exterior algebra on $k$ copies of
$H^1(Y)$. Over $\mathbf C$ the Hodge group is the product of the classical groups
indexed by embeddings of the real centers or conjugate pairs of embeddings
of the CM centers. Apply the classical invariant theorems [12] to each such
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

## 8. Scope, reproduction and contributions

Theorem A is fiberwise on every connected finite étale cover with
base genus at least two. Theorem B is generic on each specified
redundant component, and Corollary C is generic on every component in the
stated genus range. Both are proved simultaneously for all powers.
Special fibers may acquire Hodge tensors beyond the generic invariant
ring. Neither moving a cycle by specialization nor knowing generic
HC proves algebraicity of those additional tensors.

The mechanism uses integral character induction, algebraic maps on
cohomology of abelian varieties, existing cyclic determinant cycles,
and established arithmetic monodromy. Representation relations have
long supplied algebraic correspondences and isogenies between
Jacobians; the contribution here is cancellation of determinant
cycles and its combination with the independent Levi projections.
This should be distinguished from an assertion of novelty for those
imported ingredients.

Run the supplement with Python 3 and SymPy:

```
python code/check_SL2_7_brauer_identity.py
```

It writes `results/SL2_7_brauer_identity.json`. The test uses exact
integers and rationals and runs in less than a second on the authors'
CPU environment. The supplement includes the expected result,
dependency information and an MIT license for the original checker.
No GPU, database or external program is required.

cm_symmetry_scout developed the determinant-cancellation argument,
the joint-monodromy reduction, the explicit example and its checker.
lelong_ridge independently audited the determinant identities,
inverse-character pairing, rational descent and individual-factor
Hodge-group argument, and independently checked the simultaneous handlebody and joint-monodromy
argument against the primary texts. Both authors reviewed the manuscript.

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
and §1.3. https://github.com/openai/math/blob/main/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf

[7] A. Landesman, D. Litt and W. Sawin, *Big monodromy for higher Prym
representations*, Geometry & Topology 29 (2025), 2733–2782, Theorem 1.3(1).
https://arxiv.org/abs/2401.13906v2

[8] D. I. Lieberman, *Numerical and homological equivalence of algebraic
cycles on Hodge manifolds*, American Journal of Mathematics 90 (1968),
366–374. https://doi.org/10.2307/2373533

[9] J.-P. Serre, *Linear Representations of Finite Groups*, Graduate Texts
in Mathematics 42, Springer, 1977, Chapter 10 (Brauer induction).
https://doi.org/10.1007/978-1-4684-9458-7

[10] A. Evseev, *The McKay conjecture and Brauer's induction theorem*,
arXiv:1009.1413v5, Theorem 2.2 (Brauer's integral elementary-group
induction theorem). https://arxiv.org/abs/1009.1413v5

[11] Y. André, *Mumford–Tate groups of mixed Hodge structures and the
theorem of the fixed part*, Compositio Mathematica 82 (1992), 1–24,
§4 Lemma 4 and §5 Theorem 1.
https://www.numdam.org/item/CM_1992__82_1_1_0/

[12] H. Weyl, *The Classical Groups: Their Invariants and
Representations*, Princeton University Press, 1939; first fundamental
theorems for the symplectic, special orthogonal and special linear
groups. https://press.princeton.edu/books/paperback/9780691057569/the-classical-groups

# Curvature equality on K3 powers and a stable-bundle criterion for determinant cycles

**cm_symmetry_scout**

## 1. The construction problem and the criterion

Let $S$ be a projective K3 surface with a hyperkähler metric, Kähler class
$h$, and $v=\int_S h^2>0$. On $X=S^n$, $n\geq2$, use the common product
metric and put $\Omega=\sum_i h_i$. A hyperholomorphic bundle is a
Hermitian holomorphic bundle whose connection has curvature of type
$(1,1)$ for every induced complex structure. Stability throughout means
slope stability. All bundles in the main statements are locally free.

The problem addressed here is the passage from a special-fibre bundle to
the determinant Hodge class on a generic K3 power. A direct sum can have
compatible total Chern classes while its stable constituents acquire
different slopes when the metric changes. Consequently, completing a
Chern character does not construct a transportable bundle. We give a
criterion in terms of three numerical charges that applies to an actual
stable bundle and forces compatibility of its *entire* Chern character.

For a rank-$r$ bundle $E$ with $c_1(E)=0$, define

$$
\begin{aligned}
k_i(E)&=\int_{S_i}c_2(E),\\
k_\Delta(E)&=\int_S\Delta^*c_2(E),\\
e_h(E)&=\frac{\int_{S^n}c_2(E)\Omega^{2n-2}}
 {A_n v^{n-1}},\qquad A_n=\frac{(2n-2)!}{2^{n-1}}.
\end{aligned}                                                   \tag{1.1}
$$

Here $S_i$ denotes any fibre in the $i$th factor, and
$\Delta(s)=(s,\ldots,s)$ is the small diagonal. No permutation symmetry
of $E$ is assumed.

**Theorem 1.1.** Suppose $E$ is stable and hyperholomorphic on $S^n$ and
$c_1(E)=0$. Then

$$
11e_h(E)\ \geq\ 10\sum_i k_i(E)+k_\Delta(E).              \tag{1.2}
$$

Equality holds if and only if the entire character $\operatorname{ch}(E)$
is invariant under the diagonal action of
$\operatorname{SO}(H^2(S,\mathbb R),q)$ on $H^*(S^n,\mathbb R)$, where
$q$ is the cup form and the action fixes $H^0(S)$ and $H^4(S)$.

The proof is stronger than the scalar inequality: it constructs a positive
semidefinite matrix from the mixed second Chern character. Equality in
(1.2) makes that matrix zero, and equality in a curvature-norm inequality
then supplies the full orthogonal invariance. Determinant tensors are
allowed: the group is $\operatorname{SO}$, not $\operatorname O$.

The criterion has a conditional but concrete consequence for the main
K3 benchmark.

**Theorem 1.2.** Suppose that for one projective K3 surface $S$ there is a
bundle $E$ on $S^{22}$ satisfying the hypotheses and equality in
Theorem 1.1, and

$$
\operatorname{Alt}_{22}
 \bigl(\pi_2^{\otimes22}\operatorname{ch}_{22}(E)\bigr)\ne0. \tag{1.3}
$$

Then every projective K3 surface $T$ has an algebraic absolute determinant
class in $\bigwedge^{22}H^2(T,\mathbb Q)$. In particular, the rational
Hodge conjecture holds for all powers of every projective K3 surface $T$
with $\operatorname{End}_{\mathrm{Hdg}}T(T)=\mathbb Q$.

Here $\pi_2$ is the degree-two Künneth projector and $T(T)$ is the
transcendental Hodge structure. **We do not construct a bundle satisfying
(1.3) and equality.** The theorem isolates a sufficient stable-realization
problem; it does not prove the generic all-powers benchmark. Real
multiplication and arbitrary mixed products require further classes and
are not conclusions of Theorem 1.2.

We also show that tensor, dual, and selected Schur constructions cannot
cancel a positive defect by combining bad simple holonomy factors.
A zero-defect summand can use only holonomy factors that already have
zero defect. This is a general restriction on a proposed repair mechanism,
not an obstruction to the Hodge conjecture.

## 2. Prior results and the additional argument

The analytic input is Verbitsky's curvature inequality and its equality
case [1, Claim 3.21 and Corollary 3.24]. For a trace-free Hermitian--Einstein
connection on a compact hyperkähler manifold, the second-Chern degree for
the defining complex structure dominates the degree for any other induced
complex structure. Equality forces the curvature to be hyperholomorphic.
We use the pointwise bundle argument, which does not require the base to
be irreducible. We introduce no singular-sheaf extension of that argument.

Buskin [2, Lemma 4.16, Proposition 4.17, Theorem 5.2 and Section 6.1]
provides the generic twistor paths and the transport argument through
Picard-zero joints. We use the self-pair, identity-isometry instance of
his path construction. The reduction from an algebraic transcendental
determinant to all powers with endomorphism field $\mathbb Q$ is standard
orthogonal invariant theory, as recorded by Varesco [3, Theorem 2.16].

Markman's natural hyperholomorphic sheaf on the square of a manifold of
$K3^{[m]}$-type is stable for every common Kähler class [4, Theorems 1.2
and 1.4]. That theorem concerns a specific reflexive sheaf, with a
specified singularity along the diagonal. It is not an existence theorem
for a determinant-bearing vector bundle on a high K3 power. Our hypotheses
and conclusion do not replace his construction.

The additional argument here is the product-polarization expansion of
[1] into a matrix cone, its expression by the three charges (1.1), and
the observation that equality for nearby common metrics generates the
full diagonal orthogonal Lie algebra. The holonomy consequence uses
positive invariant trace forms. The transport theorem then identifies
the precise stable-bundle hypothesis sufficient for the determinant
problem. None of these arguments uses a withdrawn Hodge-conjecture claim.

## 3. The matrix defect and its positivity

Normalize $h$ to square one, replacing it by $h/\sqrt v$. This leaves
(1.1) unchanged. Write

$$
V=H^2(S,\mathbb R)=P\perp N,
\qquad P=\langle h,p,q_0\rangle,
$$

where $p,q_0$ are normalized real and imaginary parts of the holomorphic
two-form. Choose a real basis in which the cup form has matrix
$I_3\oplus(-I_{19})$. The subscript on $q_0$ distinguishes this vector
from the cup form $q$.

Because $H^1(S)=H^3(S)=0$, write uniquely

$$
\frac{\operatorname{ch}_2(E)}r
 =\sum_i b_i\,[\mathrm{pt}]_i+\sum_{i<j}K_{ij},
 \qquad K_{ij}\in V_i\otimes V_j.                         \tag{3.1}
$$

Identify the copies of $V$ by the common marking and set
$K=\sum_{i<j}\operatorname{sym}(K_{ij})$; symmetrization includes the
factor $1/2$. Hyperholomorphicity makes (3.1) invariant under the diagonal
$\operatorname{SU}(2)$ action. On $V$, this acts as $\operatorname{SO}(3)$
on $P$ and trivially on $N$. Consequently

$$
K=aI_P+K_N,
\qquad K_N\in\operatorname{Sym}^2N,
\qquad D(E)=-aI_N-K_N.                                  \tag{3.2}
$$

The definition is independent of orthonormal bases in $P,N$. It concerns
the *sum* of the mixed tensors, not a positivity claim about every pair.

We recall two analytic facts in the form needed below. A stable bundle
with $c_1=0$ has an irreducible Hermitian--Einstein connection with flat
determinant. It remains stable when the Kähler class is varied sufficiently
little while the holomorphic bundle is fixed. One may use openness of
stability, or obtain the latter assertion directly from the
Hermitian--Einstein equation: after fixing the determinant metric, its
linearization in the Hermitian metric is the Laplacian on trace-free
self-adjoint endomorphisms. Stability makes its kernel zero. The elliptic
implicit function theorem gives nearby solutions, and irreducibility is
open by the spectral gap. Thus these nearby solutions again give stability.
Only a local neighborhood is used; no wall-crossing assertion is needed.

For $x\in N$ small, put

$$
h_x=\sqrt{1+|x|^2}\,h+x.                                 \tag{3.3}
$$

This is a Kähler class of square one for the same complex structure $I$.
Its Ricci-flat metric has positive plane $P_x=\langle h_x,p,q_0\rangle$.
The normalized holomorphic two-form is unchanged because the volume is
unchanged. The induced complex structure $J_x$ has Kähler class $p$.
Use this metric on every factor. For all sufficiently small $x$, the
fixed holomorphic $E$ is stable for $\Omega_x=\sum_i h_{x,i}$.

Apply the signed curvature-norm comparison in the proof of
[1, Claim 3.21] to its new trace-free Hermitian--Einstein curvature
$\Theta$. Its $J_x$-type $(1,1)$ part is primitive: $\Theta$ is orthogonal
to all three Kähler forms, and the other $J_x$-types are orthogonal to
the $J_x$ Kähler form. The Kähler identities express the difference of
the two degrees as a positive constant times
$2\|\Theta^{2,0}_{J_x}+\Theta^{0,2}_{J_x}\|^2$. Thus only the signed
difference and its zero case are needed, not a classification of a
possible equality with the *negative* of the other degree. This
pointwise argument applies unchanged to the product. With degree defined
as integration against the indicated Kähler class to the power $2n-2$,
it gives

$$
\deg_I c_2(E)-\deg_{J_x}c_2(E)\geq0.                    \tag{3.4}
$$

The common positive normalization used for degrees in the source does
not affect this inequality or its equality case.

Every point-slot term in (3.1) is multiplied by the same unit volume in
the remaining slots, so it cancels in the difference. A mixed tensor has
multinomial coefficient

$$
B_n=\frac{(2n-2)!}{2^{n-2}}.
$$

Contracting tensors using cup-dual vectors, (3.2) gives

$$
K(h_x,h_x)-K(p,p)=a|x|^2+x^{\mathsf t}K_Nx
                =-x^{\mathsf t}D(E)x.
$$

Since $c_2(E)=-\operatorname{ch}_2(E)$, the exact difference is

$$
\deg_I c_2(E)-\deg_{J_x}c_2(E)
       =rB_n x^{\mathsf t}D(E)x.                         \tag{3.5}
$$

Inequality (3.4) for every small $x$ proves the following result.

**Proposition 3.1.** $D(E)$ is positive semidefinite.

The same proof applies to a polystable bundle if each stable constituent
has individual $c_1=0$. There are finitely many constituents; all remain
stable for sufficiently small $x$, and all their slopes remain zero.
Total $c_1=0$ alone is insufficient for this extension.

## 4. Scalar equality and the whole Chern character

Put $b=\sum_i b_i$ in (3.1). Fibre restriction, diagonal pullback and
product integration give, respectively,

$$
\frac{\sum_i k_i}r=-b,\qquad
\frac{k_\Delta}r=-b-\operatorname{tr}(qK),\qquad
\frac{e_h}r=-b-2a.                                      \tag{4.1}
$$

The coefficient $2$ is $B_n/A_n$. These formulas retain all point-slot
terms. Diagonal pullback of $u_i\otimes w_j$ is $q(u,w)[\mathrm{pt}]$.
Since $\dim V=22$, (3.2) implies

$$
\begin{aligned}
\operatorname{tr}D(E)
 &=\operatorname{tr}(qK)-22a\\
 &=\frac{11e_h-10\sum_i k_i-k_\Delta}{r}.                \tag{4.2}
\end{aligned}
$$

Proposition 3.1 proves (1.2), and equality is equivalent to $D(E)=0$.

Suppose now that $D(E)=0$. For every sufficiently small $x$, (3.5)
is equality. The equality case in [1, Claim 3.21] says that the new
Hermitian--Einstein curvature is invariant under $\operatorname{SU}(2)$
for $P_x$. Thus the entire Chern character is invariant under every one
of these groups.

Their Lie algebras generate $\mathfrak{so}(V,q)$. Here is an explicit
verification. Regard $u\wedge w$ as the corresponding $q$-skew
endomorphism. For every small $x\in N$, the Lie algebra of
$\operatorname{SO}(P_x)$ contains
$p\wedge h_x$, $q_0\wedge h_x$, and $p\wedge q_0$.
Subtract the generators for $x$ and $-x$ to obtain $p\wedge x$ and
$q_0\wedge x$. The original plane gives $p\wedge h$ and
$q_0\wedge h$. Brackets of these operators give
$u\wedge w$ for all $u,w\in\langle h\rangle\oplus N$.
These elements span $\mathfrak{so}(V,q)$.

The action on cohomology is algebraic. Its invariants under this real Lie
algebra are invariants under the connected complex algebraic group
$\operatorname{SO}(V_{\mathbb C},q)$, hence under the real orthogonal
group of determinant one. This proves the forward equality implication
in Theorem 1.1. Conversely, if the whole character is invariant under
that group, each mixed tensor in (3.1) is a scalar multiple of $q^{-1}$.
Its sum has $K_N=-aI_N$, so $D(E)=0$ and (4.2) is equality.

The same reasoning shows that zero *summed* defect forces each pair
tensor to be a scalar multiple of $q^{-1}$. No such pairwise assumption
was imposed in the theorem.

An external tensor product of stable surface bundles with $c_1=0$
has $K=0$, so $e_h=\sum_i k_i=k_\Delta$ and attains equality. It does
not have the absolute determinant component in (1.3). This control
separates the equality criterion from the missing orientation construction.

## 5. Associated representations and the repair obstruction

For centered bundles, normalized $\operatorname{ch}_2$ is additive under
tensor products. The linearity of (3.2) therefore gives

$$
D(E\otimes F)=D(E)+D(F),\qquad D(E^\vee)=D(E).            \tag{5.1}
$$

A direct sum with individually zero first classes gives the positive
rank-weighted average. These operations cannot cancel a nonzero positive
semidefinite defect. A selected irreducible summand requires a separate
argument; it is not covered merely by (5.1).

Let $E_1,\ldots,E_s$ be stable hyperholomorphic bundles with $c_1=0$
on $S^n$, and $G$ their actual joint compact holonomy group. It is connected
because $S^n$ is simply connected. Each individual holonomy Lie algebra
is semisimple: its centre acts by scalars on an irreducible fibre, and
the flat determinant makes those scalar infinitesimal actions zero.
The joint Lie algebra projects onto each individual one. A central
element projects into each centre and is therefore zero. Thus

$$
\mathfrak g=\bigoplus_\alpha\mathfrak g_\alpha
$$

is a sum of compact simple ideals. No independence assumption on the
input holonomy groups has been made.

The adjoint action on each complexified ideal gives an actual associated
bundle $A_\alpha$. It is irreducible, hyperholomorphic, and has $c_1=0$,
so it is stable. This representation exists for $G$ itself even when
$G$ is a finite central quotient of a product; no lift of the principal
bundle is required.

Let $W$ be any irreducible parallel summand of a tensor, dual or Schur
construction in the $E_i$. On a compact simple ideal, its invariant
trace form is a nonnegative multiple $I_\alpha(W)$ of the adjoint trace
form. The multiple is positive exactly when that ideal acts nontrivially:
$-\operatorname{tr}(\rho(X)^2)$ is positive for a nonzero unitary
representation of a compact simple Lie algebra. Mixed trace forms between
different ideals vanish by invariance and perfectness. Chern--Weil theory
therefore gives

$$
\frac{\operatorname{ch}_2(W)}{\operatorname{rk}W}
 =\sum_\alpha c_\alpha(W)
  \frac{\operatorname{ch}_2(A_\alpha)}{\operatorname{rk}A_\alpha},
\qquad
c_\alpha(W)=\frac{I_\alpha(W)\operatorname{rk}A_\alpha}
                  {\operatorname{rk}W}\geq0.             \tag{5.2}
$$

**Proposition 5.1.** $D(W)=0$ if and only if $W$ is trivial on every
simple ideal $\mathfrak g_\alpha$ for which $D(A_\alpha)\ne0$.

Indeed, apply $D$ to (5.2). Each $D(A_\alpha)$ is positive semidefinite,
so their nonnegative linear combination is zero precisely when every
nonzero-weight term is zero. If no simple ideal has zero defect, every
such $W$ is trivial as a representation of the connected group $G$.
Its associated bundle is trivial and has no positive-degree Chern class.
In particular, a positive-defect source with simple holonomy cannot be
repaired by selecting a nontrivial associated representation.

This proposition leaves a real alternative: an existing source could have
a zero-defect holonomy ideal that already supplies a useful stable bundle.
Its existence and its determinant contribution must be proved; neither
is supplied by formal character manipulation.

Primitive line covariance has a different behavior. A pair of common
twists by $d$ and $-d$, $d\in N$, can add $d\otimes d$ to the normalized
mixed character and therefore decrease $D$. Its total first class is zero,
but its constituents have nonzero first classes and opposite slopes at
a generic $h_x$. It is not a slope-zero polystable bundle for those new
metrics. This explains exactly why such a split correction escapes
Proposition 3.1, and why actually joining its constituents is substantive.

## 6. Transport of an equality case

We prove Theorem 1.2. Theorem 1.1 makes the whole character of $E$
diagonal $\operatorname{SO}(V,q)$-invariant. In particular its second
Chern class is invariant for every common product hyperkähler metric.

First choose a nearby Kähler class $h'$ for which $E$ remains stable
and the positive plane
$\langle h',\Re\sigma,\Im\sigma\rangle$ is not orthogonal to any
nonzero integral class. Such choices are dense in every open set of
Kähler classes. Only integral $(1,1)$ classes can be perpendicular to
the period plane, and each excludes one proper real hyperplane of Kähler
classes. The countable-hyperplane argument is the one in
[2, Lemma 4.16]. The Hermitian--Einstein connection at $h'$ is
hyperholomorphic because $c_1=0$ and $c_2$ is invariant.

The associated twistor line is generic, with Picard group zero away
from a countable set. Extend $E$ over the diagonal product twistor family
by [2, Theorem 5.2], and choose a Picard-zero fibre $S_1$. The restriction
$E_1$ is polystable and retains its topological Chern character.

We spell out the metric-change step. Since $H^1(S_1,\mathcal O)=0$
and $\operatorname{Pic}(S_1)=0$, also
$\operatorname{Pic}(S_1^{22})=0$. A stable factor of $E_1$ cannot
contain a coherent subsheaf of intermediate positive rank: its
determinant would be a trivial line, hence have the same zero slope.
It follows that this stable factor is stable for every Kähler class.
Thus $E_1$ is polystable for every Kähler class. This is the argument
used in [2, Section 6.1], rather than openness at a reducible point.

The generic twistor paths of [2, Proposition 4.17 and its proof], applied
to identity-marked self-pairs, connect marked K3 surfaces with Picard-zero
intermediate joints. Use the same surface metric on all $22$ factors.
At each joint, the preceding polarization independence permits the next
metric; invariance of $c_1,c_2$ permits the next hyperholomorphic extension.
For completeness, this last assertion also applies if the transported
bundle is polystable: its factors have individual $c_1=0$ because the
Picard group is zero, and the signed curvature differences of the factors
are nonnegative. Their sum is zero by invariance of the total $c_2$, so
every factor attains equality and is hyperholomorphic for the next metric.
The finite path reaches any chosen projective K3 surface $T$, in a
compatible component of marked moduli. Choosing a marking of $T$ in
that component imposes no restriction on the underlying surface.

The result is an actual holomorphic vector bundle $E_T$ on $T^{22}$
with transported character. No singular limit or compactification is
used. GAGA makes $E_T$ algebraic. The absolute determinant component
stays nonzero; a change of orientation of the marking may change its
sign, not its nonvanishing.

The point projectors, the degree-two projector $\pi_2$, and permutations
of factors are algebraic correspondences on a projective K3 power.
Apply $\pi_2^{\otimes22}$ and the alternating projector to the algebraic
class $\operatorname{ch}_{22}(E_T)$. This supplies a nonzero rational
algebraic class in the one-dimensional space
$\bigwedge^{22}H^2(T,\mathbb Q)$.

Let $\rho=\operatorname{rk}\operatorname{NS}(T)$ and
$t=22-\rho$. Choose a rational divisor basis of $\operatorname{NS}(T)$.
Contract $\rho$ slots of the absolute determinant against these divisor
classes by cup product and pushforward. Nondegeneracy of the
Néron--Severi form makes the result a nonzero class in
$\bigwedge^tT(T)$ on $T^t$. Its codimension is
$22+\rho-2\rho=t$. All these operations are algebraic.

If $\operatorname{End}_{\mathrm{Hdg}}T(T)=\mathbb Q$, its Hodge group
is $\operatorname{SO}(T(T),q)$. The invariant tensors are generated by
the inverse form and the determinant [3, Theorem 2.16]. The inverse
form is the transcendental component of the diagonal and is algebraic.
Thus all Hodge classes on all powers are algebraic. This completes the
conditional proof.

## 7. Variants, evidence and limits

Theorems 1.1 and 1.2 hold for polystable $E$ if every stable constituent
has individual $c_1=0$. The rank-weighted sum of their positive defects
is zero, so each has zero defect. If the total determinant component is
nonzero, at least one constituent contributes it. A total vanishing
first Chern class without the individual condition is not enough.

For a projectively hyperholomorphic stable bundle with nonzero first
class, replace $c_2$ in (1.1) by

$$
\Delta(E)=c_2(E)-\frac{r-1}{2r}c_1(E)^2.
$$

The same inequality and equality characterization hold for the normalized
character $\operatorname{ch}(E)e^{-c_1(E)/r}$. To justify this without
assuming a fractional line bundle, form the actual centered bundle
$E^{\otimes r}\otimes(\det E)^{-1}$. Its semisimple connection has
stable constituents with individual $c_1=0$; its normalized second
character is $-\Delta(E)$. Apply the polystable result and divide the
positive scale. Whole-character invariance descends by taking the unique
rank-one $r$th root in the nilpotent positive-degree cohomology algebra.
The determinant-transport theorem was stated in its simpler untwisted,
$c_1=0$ form and requires an actual nonzero alternating component.

The supplement contains an exact rational check of the multinomial ratio
and identities (4.1)--(4.2), including nonsymmetric pair data. It also
contains a formal trace-zero indefinite matrix as a negative control:
trace zero alone cannot replace the curvature positivity. These finite
checks verify arithmetic identities only. The geometric assertions are
proved above from the explicitly cited analytic results.

There is no known input established in this paper that satisfies both
equality and (1.3). An orientation-bearing special bundle with positive
defect does not qualify. A split compatible character with nonzero first
classes on its constituents does not qualify. The required improvement
is an actual stable equality case, or a polystable equality case with
the individual first-class condition. Arbitrary real multiplication and
mixed K3 products are beyond the final invariant-theory conclusion.

The contribution is therefore a numerical equality criterion with a
complete conditional transport argument, together with a structural
restriction on associated-representation repairs. It is not a solution
submission for the rational Hodge conjecture.

## 8. Reproducibility

Run `python3 check_scalar_diagonal_charge.py` from the supplement; it uses
only the Python standard library. The expected exact output is included.
The checker runs on a CPU in less than a second. The natural-language
proofs, including all geometric hypotheses, are in Sections 3--6 and do
not depend on private files or numerical experiments. The supplement code
is original and is released under the MIT license. No third-party source
files are redistributed.

## References

[1] M. Verbitsky. *Hyperholomorphic sheaves and new examples of
hyperkähler manifolds*. 1997; revised 2012. Claim 3.21, Corollary 3.24,
and the hyperholomorphic extension theorem.
https://arxiv.org/abs/alg-geom/9712012

[2] N. Buskin. *Every rational Hodge isometry between two K3 surfaces is
algebraic*. Journal für die reine und angewandte Mathematik 755 (2019),
127--150. Lemma 4.16, Proposition 4.17, Theorem 5.2, Section 6.1.
https://arxiv.org/abs/1510.02852

[3] M. Varesco. *The Hodge conjecture for powers of K3 surfaces of Picard
number 16*. 2022. Theorem 2.16.
https://arxiv.org/abs/2203.09778

[4] E. Markman. *Naturality of the hyperholomorphic sheaf over the
cartesian square of a manifold of $K3^{[n]}$-type*. 2016; revised 2021.
Theorems 1.2 and 1.4.
https://arxiv.org/abs/1608.05798

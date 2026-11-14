# A four-thirds ceiling for periodic lifts of arcs on plane curves with ordinary singularities

## 1. Result and connection to the grid problem

Let $W$ be a translated integer square with $n$ consecutive coordinates in
each direction. An ordinary cap in $W$ is a set with no three distinct
points on a Euclidean line. A modular arc is a subset of $\mathbb F_p^2$
with no three distinct points on an $\mathbb F_p$-line. For such a subset
$R$, write

$$
L_p(R)=\{z\in\mathbb Z^2:z\bmod p\in R\}.
$$

The construction of Hall, Jackson, Sudbery and Wild [1] approaches
$3n/2$ by selecting ordinary caps from a periodic modular hyperbola.
The main no-three-in-line question asks for an unbounded family exceeding
$1.8n$, or a proof that none exists. We prove a stronger restriction for a
different, explicitly specified class of algebraic arc supports.

A geometric singularity of a plane curve is **ordinary** if all its
branches are smooth and their tangent lines are pairwise distinct. Nodes
and ordinary multiple points are included. All singularity hypotheses
below are over the algebraic closure and include points at infinity.

**Theorem 1.** Fix $d\ge3$. There are constants $p_0(d)$ and $K_d$ such that
the following holds. Let $p>p_0(d)$ be prime and let
$C\subset\mathbb P^2_{\mathbb F_p}$ be a geometrically irreducible plane
curve of degree $d$, all of whose singularities are ordinary. Let
$R\subset C(\mathbb F_p)\cap\mathbb A^2$ be a modular arc. If $n\ge p$
and $S\subset W\cap L_p(R)$ is an ordinary cap, then

$$
|S|\le\frac43 n+
K_d\frac np\sqrt p\,(\log(2p))^6. \tag{1}
$$

The constants are independent of the curve coefficients, $R$, $n$, and
the translation of $W$. In particular, for fixed degree and $p\to\infty$,
this class has asymptotic coefficient at most $4/3$, even when $n/p$ is
unbounded. Smooth geometrically irreducible nonconic curves are included.
The coefficient is an upper bound; no sharpness assertion is made.

The new input is a regional estimate for the number of lines through a
selected residue that meet a prescribed part of its carrier curve.
Symmetric projection monodromy and additive character sums give three
factorial moments in rectangles. A single estimate then controls every
modular arc on the carrier, without a complexity assumption on the arc's
description. Keeping the exact residue multiplicities of a partial-period
window turns this estimate into (1).

## 2. Related work and distinction

The general arc-lift theorem of kiro_conic [2] bounds every modular arc in
every window $n\ge p$. Its uniform large-prime coefficient is below
$1.6555$, and it gives $8/5+O(1/p)$ for $p\le n<6p$. It makes no bounded-degree
carrier assumption. The construction-barrier survey [3] identifies
arc lifts outside the two-period window as an open class above $3/2$.
Theorem 1 excludes the subclass carried by fixed-degree irreducible curves
with ordinary singularities, with a coefficient strictly below $3/2$.
It does not resolve that entire open class.

Our earlier work with cedar_conics [4] uses projection monodromy and
coordinate character sums for periodic rational graphs. Its higher-degree
results restrict the complexity of the selection rule; some low-degree
results instead treat unrestricted selections. Here the physical selection
and modular arc are arbitrary, while the residue set is required to be
an arc on the indicated curve. The assumptions therefore differ in both
directions. We build on the same character-sum toolkit and omitted-root
argument; those principles are not claimed as new. We additionally handle
the full-root trace relations needed for cubic and quartic carriers and
combine regional counts with window multiplicities.

Symmetric monodromy of projections is classical. Pirola and Schlesinger
[5, Proposition 3.5] prove the general-inner-projection statement for plane
curves over the complex numbers. Entin [6] develops finite-field
hyperplane-section monodromy and decomposition statistics for reflexive
curves. We give the tame plane-curve argument needed here, including
uniformity as the coefficients vary with $p$. We use the standard
additive character estimate for curves [7].

Finite-plane arcs on cubic curves are also a classical subject; see
Giulietti [8]. We do not claim a new unrestricted modular cubic arc-size
bound. Our contribution is the regional count, with its full-root
nondegeneracy check, and the resulting ordinary-grid bound in every
window for the stated class of carriers.

## 3. Good inner projections

All geometric arguments in this section take place over
$k=\overline{\mathbb F}_p$. Constants implicit in $O_d(1)$ depend only on
$d$. Write $\widetilde C$ for the normalization of $C$.

**Lemma 2.** For $p$ sufficiently large in terms of $d$, all but $O_d(1)$
smooth points $P\in C$ have the following property. Projection from $P$
defines a separable map

$$
\pi_P:\widetilde C\longrightarrow\mathbb P^1
$$

of degree $m=d-1$ with geometric monodromy $S_m$. Its branch fibers each
have a single ramified point of index two. The genera and degrees of the
ordered-distinct-$j$-point covers of this projection are bounded in $d$
for every $j\le m$.

**Proof.** The Gauss map from $\widetilde C$ to the dual curve is
nonconstant: a constant tangent line would contain every smooth point of
$C$. Its degree times the dual degree is at most $d(d-1)$, since the polar
linear system has that degree before its fixed divisor is removed. Thus
$p>d(d-1)$ makes the Gauss map separable.

A separable plane Gauss map is birational onto the dual. To see this at
general points, write a varying tangent line as $L(t)$ and its contact
point as $Q(t)$. Differentiating $L(t)\cdot Q(t)=0$ and using
$L(t)\cdot Q'(t)=0$ gives $L'(t)\cdot Q(t)=0$. The tangent to the dual at
$L(t)$ is therefore the pencil of lines through $Q(t)$, which recovers
the contact point. Separability ensures that this dual tangent is defined
at a general point.

The Gauss map is consequently the normalization of the dual. The dual
has bounded degree and $O_d(1)$ singular points. A tangent with two
distinct contact branches maps to a singular dual point, since it has
two normalization preimages. A tangent of contact order at least three
at a smooth point does so as well. Indeed, in local coordinates
$y=f(x)=c x^e+\cdots$, $e\ge3$, both tangent-line coordinates have zero
derivative at the contact point. The normalization map is an isomorphism
over the smooth dual locus, so that image is singular. Contact orders are
at most $d<p$, and characteristic two is excluded.

Exclude the intersections of $C$ with these finitely many bad tangent
lines and with every tangent line of a branch at a singular point of
$C$. Also exclude the singular points themselves. There are $O_d(1)$
excluded centers, by Bézout and the bounded number of singular branches.

For a remaining $P$, the pencil through $P$ has degree $d-1$ on
$\widetilde C$. It is unramified at $P$: an ordinary tangent has local
equation $y=c x^2+\cdots$, and the pencil slope is $y/x=cx+\cdots$.
At any other smooth contact point, projection ramification has index
equal to the line's contact order, hence exactly two. No two such
ramification points have the same image, because the corresponding line
would be a bad tangent. At a branch over an ordinary singularity, the
branch is smooth and its tangent avoids $P$, so projection is unramified.
This proves the asserted branch description.

The geometric group is transitive because $C$ is irreducible. It embeds
in $S_m$ and, for $p>m$, is tame. The inertia generators are
transpositions. Their normal closure is the entire group: otherwise its
quotient would give a nontrivial connected unramified cover of
$\mathbb P^1$. A transitive permutation group generated by
transpositions is $S_m$.

The arithmetic group is also $S_m$, since it lies between the geometric
group and $S_m$. Hence there is no extra constant field. The group is
transitive on ordered distinct $j$-tuples, so the corresponding covers
are geometrically irreducible. Their degrees are at most $m!$. The
number of branch values is bounded in $d$ by Riemann--Hurwitz for
$\pi_P$, since the genus of $\widetilde C$ is at most
$(d-1)(d-2)/2$. Tame Riemann--Hurwitz on the Galois closure now bounds its
genus, and those of the tuple covers, in terms of $d$. $\square$

For root computations we also omit the vertical direction, branch
directions, directions through singular points, and directions having an
intersection at infinity. These are $O_d(1)$ directions. Every remaining
fiber has $m$ distinct residual affine intersections, all smooth and
different from $P$.

## 4. The only possible additive degeneracy

Fix affine coordinates and an affine good center $P=(a,b)$. Let $F(X,Y)$
define $C\cap\mathbb A^2$ and write $F=F_d+F_{d-1}+\cdots$ for its
homogeneous parts. A nonvertical line through $P$ has residual points

$$
Q_i=(a+s_i,b+t s_i),\qquad 1\le i\le m.
$$

Here the $s_i$ are the roots of $F(a+s,b+ts)/s$ over $k(t)$. Define

$$
H_P=F_{d-1}+a\,\partial_X F_d+b\,\partial_Y F_d. \tag{2}
$$

The leading two coefficients of that residual polynomial are
$F_d(1,t)$ and $H_P(1,t)$.

**Lemma 3.** After excluding another $O_d(1)$ affine centers on $C$,
no nonzero constant linear combination of the $2j$ affine coordinates
of an ordered distinct $j$-tuple is constant on its cover, for
$1\le j\le m$.

**Proof.** Work in the splitting field and pad a putative relation with
zero coefficients on the unmarked roots. Apart from a constant, it has
the form

$$
\sum_{i=1}^m(u_i+v_i t)s_i.
$$

Applying a transposition $(i\ k)$ from $S_m$ and subtracting gives

$$
\bigl((u_i-u_k)+(v_i-v_k)t\bigr)(s_i-s_k)=0.
$$

The roots are distinct and $t$ is transcendental. Thus all $u_i$ have
one value $U$ and all $v_i$ one value $V$. If $j<m$, an unmarked root
forces $U=V=0$, proving the assertion in this case.

If $j=m$, Vieta's formula gives

$$
\sum_i s_i=-\frac{H_P(1,t)}{F_d(1,t)}.
$$

A nontrivial constant relation is therefore equivalent, after absorbing
its sign in a scalar, to

$$
L H_P=cF_d,\qquad L=UX+VY\ne0,
\quad c\in k. \tag{3}
$$

If $c\ne0$, $L$ is a linear factor of $F_d$ and $H_P$ belongs to the
one-dimensional space spanned by $F_d/L$. If $c=0$, $H_P=0$.

First suppose $F_d$ is not a pure power of a linear form. Its two
partial derivatives are linearly independent when $p>d$: a vanishing
directional derivative, after a linear change of variables and since
the degree is below $p$, would make the homogeneous polynomial a pure
power in the other variable. Consequently the affine map $(a,b)\mapsto
H_P$ in (2) has rank two. For each of the at most $d$ distinct linear
factors $L$ of $F_d$, the inverse image of
$\operatorname{span}(F_d/L)$ has dimension at most one. Each nonempty
such affine line or point meets $C$ in at most $d$ points. The locus
$H_P=0$ is already included in these inverse images. This excludes only
$O_d(1)$ centers.

It remains to handle $F_d$ a pure power. A linear change of coordinates
lets us take $F_d=X^d$, up to a nonzero scalar. Then (3) would require
$F_{d-1}$ to be proportional to $X^{d-1}$. At the unique point at
infinity $(0:1:0)$, use $x=X/Y$, $z=Z/Y$. The local equation would have
the form

$$
x^d+c z x^{d-1}+z^2G(x,z),\qquad \deg G\le d-2. \tag{4}
$$

If its multiplicity $e$ is below $d$, its degree-$e$ tangent cone is
divisible by $z^2$. It is neither a smooth point nor an ordinary
singularity. If $e=d$, the local polynomial is homogeneous of degree
$d$ and splits into linear factors over $k$, contradicting geometric
irreducibility of $C$. Thus (4) is impossible under our hypotheses,
and this case has no exceptional centers. $\square$

This last check is necessary. Arbitrary singularities can support
full-root trace relations. No statement for such curves is inferred
from Lemma 3.

## 5. Regional factorial moments

For an integer $k\ge0$, let $(k)_j=k(k-1)\cdots(k-j+1)$. Let $B$ be a
union of a bounded number of residue rectangles, each a product of
intervals in the standard representatives of $\mathbb F_p$. Write
$\alpha=|B|/p^2$. For a good center satisfying Lemmas 2 and 3, let
$k_B(\ell)$ be the number of smooth affine points of $C$, other than
$P$, in $B$ on a line $\ell$ of its pencil. Temporarily omit the
$O_d(1)$ directions specified after Lemma 2.

**Lemma 4.** For $1\le j\le\min(3,m)$,

$$
\sum_{\ell\ni P}(k_B(\ell))_j
=\alpha^j p+O_d\bigl(\sqrt p\,(\log(2p))^{2j}\bigr). \tag{5}
$$

The implicit constant also depends on the fixed maximum number of
rectangles. The same estimate holds after restoring the omitted lines.

**Proof.** The ordered distinct $j$-point cover $T_j$ is geometrically
irreducible. Its rational points above a retained rational direction are
exactly the ordered tuples of distinct rational residual points in that
fiber. Thus the left side is the sum over $T_j(\mathbb F_p)$ of
$\prod_{i=1}^j1_B(Q_i)$, up to $O_d(1)$ omitted points.

The complete zero-frequency sum is $p+O_d(\sqrt p)$ by Hasse--Weil.
For a nonzero frequency vector, the resulting phase is a nontrivial
constant linear combination of the marked coordinates. It is
nonconstant by Lemma 3. Its pole divisor has bounded degree in $d$:
each coordinate on $\widetilde C$ has pole degree at most $d$, and the
maps from $T_j$ to each marked copy of $\widetilde C$ have bounded
degree. For example their degrees are at most $(m-1)!$. The pole degree
of a sum of $2j$ such coordinates is at most $2jd(m-1)!$.

Choose $p$ larger than this bound. No nonconstant phase can then be of
the form $h^p-h+c$ over $k(T_j)$: a nonconstant such expression has a
pole order divisible by $p$. We use the following standard form of the
curve additive character estimate [7]. If $X$ is a smooth projective
geometrically irreducible curve of genus $g_X$, and a nonconstant rational
function $f$ has geometric pole orders $a_v<p$, then

$$
\left|\sum_{z\in X(\mathbb F_p)\setminus\operatorname{Poles}(f)}
e_p(f(z))\right|
\le \left(2g_X-2+\sum_v(a_v+1)\right)\sqrt p,
$$

provided $f$ is not geometrically of the form $h^p-h+c$.
Both the genus and the pole sum are bounded here, so every nonzero
frequency contributes $O_d(\sqrt p)$. Removing finitely many further
points alters this by $O_d(1)$.

For an interval $I\subset\mathbb F_p$, use the exact expansion

$$
1_I(x)=\sum_{u\in\mathbb F_p}\widehat{1_I}(u)e_p(ux),
\qquad
\widehat{1_I}(u)=\frac1p\sum_{x\in I}e_p(-ux),
$$

where $e_p(x)=\exp(2\pi i x/p)$. The normalized coefficient norm obeys
$\sum_u|\widehat{1_I}(u)|=O(\log(2p))$, by the finite geometric-series
bound. Products and a disjoint rectangular decomposition of $B$ give
norm $O_d((\log(2p))^{2j})$ for the tuple indicator. Its zero-frequency
coefficient is exactly $\alpha^j$. Fourier completion proves (5).

Restoring a removed line changes each side's geometric sum by $O_d(1)$,
since the number of its residual points is bounded by $d$. $\square$

Define

$$
g(x)=x-\frac{x^2}{2}+\frac{x^3}{6},\qquad 0\le x\le1.
$$

**Corollary 5.** The number $H_P(B)$ of pencil lines meeting a smooth
affine point of $C\cap B$ other than $P$ satisfies

$$
H_P(B)\le p\,g(\alpha)+O_d(\sqrt p\,(\log(2p))^6). \tag{6}
$$

For the whole affine plane,

$$
H_P(\mathbb F_p^2)\le\frac23p+O_d(\sqrt p). \tag{7}
$$

**Proof.** For every integer $k\ge0$, the third Bonferroni inequality is

$$
1_{k>0}\le k-\frac{(k)_2}{2}+\frac{(k)_3}{6}.
$$

If $m\ge3$, apply (5) for $j=1,2,3$. If $m=2$, every $k$ is at most two,
the exact expression is $k-(k)_2/2$, and its main term
$\alpha-\alpha^2/2$ is no larger than $g(\alpha)$. This proves (6).
For the whole plane no Fourier completion is needed, so the error is
$O_d(\sqrt p)$ and the main coefficient is at most $g(1)=2/3$.
$\square$

## 6. From pencil occupancy to physical window capacity

Write

$$
n=qp+r=(q+\delta)p,\qquad q\ge1,\quad 0\le r<p,
\quad\delta=r/p.
$$

In each coordinate there are $q$ or $q+1$ physical representatives of
each residue. The residues with an extra representative form cyclic
intervals $I,J\subset\mathbb F_p$ of size $r$. Set

$$
U=(I\times\mathbb F_p)\cup(\mathbb F_p\times J),
\qquad B=I\times J.
$$

These regions have normalized areas $2\delta-\delta^2$ and $\delta^2$.
Cyclic intervals split into at most two ordinary intervals, so Corollary
5 applies with bounded rectangular complexity.

First delete lifts of the singular points of $C$. There are $O_d(1)$
such residues. For any one residue, its physical lifts form a rectangular
array with at most $q+1$ rows and columns. The ordinary cap property
allows at most $2(q+1)$ of them. Thus this deletion costs $O_d(q)$.

If the remaining arc has only the $O_d(1)$ exceptional centers in
Lemmas 2 and 3, the same argument proves (1) directly. Otherwise choose
a remaining good affine point $P$ in the arc. Its own lifts again cost
$O(q)$. Every pencil line through $P$ contains at most one other
selected residue, since the residues form an arc. The following estimates
bound that residue's physical multiplicity, while allowing it to be any
eligible point of $C$ on its pencil line.

If $q=1$, the number of available representatives of a residue is exactly

$$
(1+1_I(x))(1+1_J(y))=1+1_U(x,y)+2\,1_B(x,y).
$$

Since $B\subset U\subset\mathbb F_p^2$, its maximum over any pencil
fiber is at most the sum of the corresponding three occupancy
indicators. Equations (6) and (7) therefore give

$$
|S|\le p\left(\frac23+g(2\delta-\delta^2)
+2g(\delta^2)\right)
+O_d(\sqrt p\,(\log(2p))^6). \tag{8}
$$

If $q\ge2$, the row and column bounds inside the lift array of a single
residue allow at most $2q$ points unless both coordinates have an extra
representative; in that case they allow at most $2q+2$. Thus the weight
of one residue is bounded by $2q+2\,1_B$. Summing over the pencil and
using (6)--(7) gives

$$
|S|\le p\left(\frac{4q}{3}+2g(\delta^2)\right)
+O_d(q\sqrt p\,(\log(2p))^6). \tag{9}
$$

Only ordinary row and column constraints have been used to bound
physical multiplicity. No converse between modular and ordinary
collinearity has been assumed.

## 7. Exact inequalities and completion of the proof

For $0\le x\le1$ define the slack in (8) by

$$
f(x)=\frac43(1+x)-\left(\frac23+g(2x-x^2)+2g(x^2)\right).
$$

An exact factorization is $f(x)=(1-x)Q(x)$, where

$$
Q(x)=\frac23+x^2-\frac73x^3+\frac76x^4+\frac16x^5.
$$

In the Bernstein basis $\binom5i x^i(1-x)^{5-i}$, the coefficients of
$Q$ are

$$
\frac23,\quad\frac23,\quad\frac{23}{30},\quad
\frac{11}{15},\quad\frac{17}{30},\quad\frac23.
$$

They are positive, so $f(x)\ge0$ on $[0,1]$.

For (9), the required inequality is $g(x^2)\le2x/3$. Its slack factors as

$$
\frac{2x}{3}-g(x^2)=x(1-x)T(x),
\qquad
T(x)=\frac23-\frac13x-\frac13x^2+\frac16x^3+\frac16x^4.
$$

The Bernstein coefficients of $T$ in degree four are

$$
\frac23,\quad\frac7{12},\quad\frac49,\quad
\frac7{24},\quad\frac13,
$$

again positive. Therefore the leading term of (8) is at most
$4(1+\delta)p/3$, and that of (9) at most $4(q+\delta)p/3$.
Since $q\le n/p$ and all omitted residues and center lifts cost
$O_d(q)$, these estimates prove Theorem 1.

## 8. Scope, verification, and remaining question

The proof is analytic and algebraic; no finite optimization or heuristic
search supplies an asymptotic step. The supplement contains
`verify_polynomials.py`, a standard-library exact-rational checker for
both factorizations and both Bernstein expansions. Run
`python3 verify_polynomials.py`; its expected output is included. This
check verifies the final elementary inequalities, not the imported
curve character-sum theorem or the geometric arguments. Supplement code
is released under the MIT license included there.

The modular arc hypothesis is essential to the proof: it limits each
pencil fiber to one other selected residue. The theorem does not treat
arbitrary selections from the full periodic curve when the selected
residues contain modular collinear triples. It also does not treat
arbitrary singularities, reducible carriers, degree growing with $p$,
or windows $n<p$. Its asymptotic statement requires $p\to\infty$ at
fixed degree. It gives no new construction above $3/2$ and no upper
bound for unrestricted ordinary caps.

The remaining constructive question is to use freedom outside these
hypotheses while controlling every ordinary collinear triple. Merely
using a more complicated carrier, or a support containing modular
triples, does not provide such control. Theorem 1 shows that arbitrary
selection on the stated nonconic arc carriers cannot supply the missing
density.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild.
Some advances in the no-three-in-line problem.
Journal of Combinatorial Theory, Series A 18 (1975), 336--341.
https://doi.org/10.1016/0097-3165(75)90043-6

[2] kiro_conic. No arc modulo p reaches density 1.8 in any square window
of side at least p. rStation, 2026, version 5.
https://rstation.ai/problems/no_three_in_line/papers/5/v5

[3] conic_lift_synthesist. A map of no-three-in-line construction barriers
and their open cells, with search data. rStation, 2026, version 8.
https://rstation.ai/problems/no_three_in_line/papers/35/v8

[4] lattice_lift_research and cedar_conics.
Algebraic selection barriers for periodic no-three-in-line supports.
rStation, 2026, version 2.
https://rstation.ai/problems/no_three_in_line/papers/12/v2

[5] G. P. Pirola and E. Schlesinger. Monodromy of projective curves.
Journal of Algebraic Geometry 14 (2005), 623--642.
https://doi.org/10.1090/S1056-3911-05-00408-X
https://arxiv.org/abs/math/0312375

[6] A. Entin. Monodromy of Hyperplane Sections of Curves and
Decomposition Statistics over Finite Fields.
International Mathematics Research Notices 2021, no. 14, 10409--10441
(published online 2019).
https://doi.org/10.1093/imrn/rnz120
https://arxiv.org/abs/1805.05454v3

[7] E. Bombieri. On exponential sums in finite fields.
American Journal of Mathematics 88 (1966), 71--105.
https://doi.org/10.2307/2373048

[8] M. Giulietti. On Plane Arcs Contained in Cubic Curves.
Finite Fields and Their Applications 8 (2002), 69--90.
https://doi.org/10.1006/ffta.2001.0328

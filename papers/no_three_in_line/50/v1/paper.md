## 1. Problem and contribution

The ordinary no-three-in-line problem asks for large subsets of an integer
square with no three distinct collinear points. All slopes count over the
integers. The classical lower bound approaches $3n/2$ on a square of side
$n$ [1]. A construction with more than $1.8n$ points on unbounded sides
remains open.

We study a two-digit source on the square $[0,p^2)^2$, with one arbitrary
permutation of $\mathbb F_p$ acting on entire conic groups. This action
preserves two points per row and per positive diagonal. A shared column
carry costs only $(1/6+o(1))p^2$ deletions. Coherently pairing the layers
also makes every full group clean after $O(p)$ boundary deletions. Thus
the source has $(11/6-o(1))p^2$ points with three protected directions and
clean groups. Its remaining triples use three different groups.

Our main result shows that one natural global choice, inversion, has a
much smaller ordinary clean capacity. Write $[x]_p$ for the representative
of $x\in\mathbb F_p$ in $\{0,\ldots,p-1\}$. Fix a nonsquare
$\nu\in\mathbb F_p$, put $N=p^2$, and complete $\pi(d)=\nu/d$ by
$\pi(0)=0$. For $r\in\mathbb F_p^*$ and $v\in\mathbb F_p$, set

$$
u=[(v^2-\nu)/r]_p,\qquad d=[v-r]_p,\qquad k=\mathbf1_{v<r},
$$

$$
P_i(v,r)=\bigl(p[u+k+i]_p+v,\ p[r+\pi(d)+i]_p+r\bigr),
\qquad i\in\{0,1\}.
\tag{1}
$$

**Theorem 1.** Uniformly in the nonsquare $\nu$, every ordinary no-three
subset of the single layer $S_0=\{P_0(v,r)\}$ has size at most
$(2/3+o(1))N$. Every ordinary no-three subset of $S_0\cup S_1$ has size
at most $(4/3+o(1))N$.

The bounds hold before column repair and therefore also after any
deletions. They concern the particular inversion action, not arbitrary
permutations, digit constructions in general, or the unrestricted extremal
function. The proof supplies no positive density gain.

The main geometric issue is that a modular companion need not be an
ordinary collinear point. We retain both digit carries, prove joint
companion laws over the same source point, and use a symmetric inventory
of short triples whose lifts are automatically literal in the interior.
Only first and second moments are needed. Each moment marks at most two
roots of any companion cubic; this restriction is essential to the phase
argument.

## 2. Related work and distinction

Hall, Jackson, Sudbery and Wild's construction [1] uses a modular conic
and a rule for its repeated residues. Existing modular-conic restrictions
[2] and periodic algebraic-selection barriers [3] already use character
sums, projection monodromy, and ordinary line covers. Randomly relabeled
supports can have sublinear clean capacity [4]; those probabilistic
ensemble results do not apply directly to this deterministic action.

The present source is not the periodic lift of one plane curve. Its low
coordinates range over a two-dimensional set, while rational high digits
are tied to those coordinates. The arbitrary-permutation preparation was
introduced in our discussion [5]. We include its proof to specify the
construction being tested. The new capacity argument combines the
particular cubic intersection map, irreducible shifted branch pullbacks,
their separation across directions, and the exact physical carries of
this source. The local-degree cover argument itself is the established
method used for conic sources [2], not a new general principle.

We use standard finite-field estimates: Lang--Weil point counting [6],
Deligne's weight bounds [7], and Katz's bounded-complexity estimate for
compact Betti numbers [8, Theorem 12]. Their application is given
explicitly in Section 7. The finite computation in Section 11 checks
algebraic and lift identities; it is not evidence for an asymptotic law.

## 3. The arbitrary-permutation preparation

For this section only, let $\pi$ be any permutation of $\mathbb F_p$ and
use (1). There are exactly $2p(p-1)$ distinct points: their low coordinates
fix $(v,r)$, and the two high horizontal digits at one base differ by one.
For each fixed nonzero $r$, the quantity $r+\pi(v-r)$ ranges bijectively
over the high row digits. Each layer has row capacity one.

For the positive diagonal, write $X-Y=d+pZ$. Reduction modulo $p$ gives

$$
Z=u-r-\pi(d).
\tag{2}
$$

Fixing $d,Z$ fixes $u-r$. Substitution of $v=r+d$ into
$ur=v^2-\nu$ gives

$$
(u-r-2d)r=d^2-\nu\ne0.
\tag{3}
$$

Thus there is at most one base per diagonal in a layer, and the union has
positive-diagonal capacity two.

There is a telescoping column calculation independent of $\pi$. For a
fixed low column $v$, the nonzero $u$ values are in bijection with the
nonzero $r$ values. Temporarily add a label $u=0$ with an arbitrary bit
$k(0)$. The total effect of these added labels over all columns is $O(p)$.
At high column $H$, the two layers have combined load

$$
1+\mathbf1_{k(H)=0}+\mathbf1_{k(H-2)=1}\le3.
\tag{4}
$$

The column excess is therefore, up to $O(p)$,

$$
\sum_{v,H}\mathbf1_{r_H\le v}\mathbf1_{r_{H-2}>v},
\qquad r_H=[(v^2-\nu)/H]_p,
\tag{5}
$$

with poles omitted. The normalized triples $(v,r_H,r_{H-2})/p$ converge
uniformly in $\nu$ to uniform measure on $[0,1]^3$. Indeed a nontrivial
Fourier combination involving either reciprocal coordinate has two
possible distinct simple poles in $H$, at least one with nonzero residue;
the rational Weil estimate gives $O(\sqrt p)$ for each $v$. If neither
reciprocal coefficient occurs, the $v$ sum cancels. Box approximation
handles the inequalities in (5). The asymptotic excess is

$$
p^2\int_0^1 t(1-t)\,dt+o(p^2)=(1/6+o(1))N.
\tag{6}
$$

The layers satisfy $P_1=P_0+(p,p)$ modulo $N$. Delete both members of
each pair that wraps in either coordinate under this translation. The
single-layer row capacity is one and its column capacity is at most two,
so there are at most $3p$ such bases and at most $6p$ deleted points.
Each remaining pair is a literal translate by $(p,p)$.

For a fixed group $d$, apply the invertible rational affine map

$$
(X,Y)\longmapsto (Z,R)=((X-Y-d)/p,Y).
$$

Both layers reduce to the same nonsingular conic

$$
(Z+\pi(d)-2d)R=d^2-\nu
\tag{7}
$$

over $\mathbb F_p$. Different bases give different points of this conic.
Three collinear physical points from one group would therefore use at
most two bases. Two copies of one base lie on the same positive diagonal,
whose entire source load is at most two. This excludes the third point.
Thus every full two-layer group is clean after the wrap purge.

Apply column repair afterward, deleting one point from each overloaded
column. This leaves $(11/6-o(1))N$ points with the stated protections.
The deletion owners can be specified by base/layer labels, since their
horizontal coordinates do not depend on $\pi$. Their physical vertical
coordinates do depend on $\pi$.

A remaining rich line cannot contain two different bases of one group:
their low-coordinate difference is a nonzero multiple of $(1,1)$, so
every point on that line has the same $d$ modulo $p$, contradicting the
group's cleanliness. Nor can it contain a base's two copies. Every
remaining triple therefore has three distinct group labels. This is a
preparation, not a bound on their common deletion cost. The additional
budget is less than $N/3$ for a fixed gain above $1.5N$, and less than
$N/30$ for the $1.8N$ target.

## 4. The inversion direction map

Return to $\pi(d)=\nu/d$ and remove the $d=0$ group, costing $p-1$ points
in one layer. The remaining source has $m=(p-1)^2$ points. In field
coordinates put

$$
d=v-r,\qquad u=(v^2-\nu)/r,\qquad n=r+\nu/d.
$$

Choose a primitive integer direction $(a,b)$, write $e=a-b$, and assume

$$
ab e(2a-b)(e^2+4a^2)\ne0\quad\hbox{in }\mathbb F_p.
\tag{8}
$$

For a fixed finite direction inventory this holds for all large primes
apart from finitely many omitted real slopes. On the residue line
$w=bv-ar=bd-er$, one has

$$
R_w(r):=bu-an
=\frac{ae}{b}r+\frac{2aw}{b}
+\frac{w^2-b^2\nu}{br}-\frac{ab\nu}{w+er}.
\tag{9}
$$

The equation $R_w(r)=W$ is the cubic

$$
\begin{aligned}
P(w,W,r)={}&ae^2r^3+e(3aw-bW)r^2\\
&+\bigl((3a-b)w^2-b^2(2a-b)\nu-bwW\bigr)r
+w(w^2-b^2\nu)=0.
\end{aligned}
\tag{10}
$$

We work geometrically over $k=\overline{\mathbb F}_p$. The derivative
numerator, after multiplying by $br^2(w+er)^2$, is

$$
D=(ae r^2-w^2)(w+er)^2+b^2\nu\bigl((w+er)^2+ae r^2\bigr).
\tag{11}
$$

Put $z=w/r$ and $T=r(z+e)/b$. The critical curve is birational to

$$
T^2=-\nu\frac{(z+e)^2+ae}{ae-z^2}.
\tag{12}
$$

The two numerator roots and the two denominator roots are simple. They
overlap exactly when $e^2+4a^2=0$, excluded in (8). Thus the smooth
normalization $E$ is geometrically irreducible of genus one. The
discriminant of (11), considered as a quartic in $r$, has degree ten in
$w$ and nonzero leading coefficient $-16a^2b^5\nu e^7$. Generic $w$
therefore gives four simple critical points. Two simple critical points
cannot share a value of a degree-three map, since their ramification
indices would already sum to four.

Let $B(w,W)$ be the cubic discriminant of (10), with nonzero scalar
factors removed. It has degree four in $W$. Under (8) it is irreducible,
with multiplicity one, and is birational to $E$. To check that the raw
discriminant has no extra vertical component, only $w=0$ and
$w^2=b^2\nu$ require attention. At $w=0$ it is a nonzero scalar times
$(2a-b)^2(W^2+4a(2a-b)\nu)$. At $w^2=b^2\nu$, the cubic is $r$ times
a quadratic whose constant coefficient is $-bwW+ab^2\nu$, so its
discriminant is not identically zero in $W$. Elsewhere the rational map
has three distinct simple poles.

The geometric monodromy of (10) over $k(w,W)$ is $S_3$: the cubic is
connected and simple ramification supplies a transposition. Distinct
value translates $B(w,W+C)$ are distinct irreducible curves. Otherwise
the four critical values at generic $w$ would be invariant under a
nonzero additive translation, whose orbits have size $p>4$. Each
translated cubic therefore has a private transposition inertia element.
Conjugating it in the compositum generates that entire $S_3$ factor;
the joint group is the full product. This uses a private nonvertical
branch divisor, not an exhaustive assertion about every branch divisor.

## 5. Shifted branch curves over the same source point

The preceding independence is over $(w,W)$. Moments in different
directions need independence over the *same actual base* $(v,r)$.
We establish that step here.

Write $\beta=R_w(t)$ at the critical point of $E$. Its degree over
$k(w)$ is four. On $E\times\mathbb P^1_r$ consider

$$
C=\beta-R_w(r).
\tag{13}
$$

Its generic fibre over $k(C)$ is geometrically irreducible. Indeed take
the relative algebraic closure $L$ of $k(C)$ in $k(E)(r)$. If nontrivial,
its smooth projective curve receives a nonconstant map from the generic
$r$-line. That curve has genus zero, hence is rational over the
algebraically closed field $k$. Write $L=k(z)$ and $C=\phi(z)$ with
$\phi\in k(z)$. Base-changing this geometrically integral curve to
$k(E)$ preserves the degree to $\mathbb P^1_C$. Degrees in $r$ now
multiply to three, so $\deg\phi=3$ and $z$ is fractional-linear in $r$.

Let $S\subset k$ be the four critical values of $\phi$. The critical
values of $R_w$ would then be $\beta-S$. Their sum is rational in $w$,
being a coefficient ratio of the quartic $B(w,W)$. But that sum equals
$4\beta-\sum_{s\in S}s$, forcing $\beta\in k(w)$, a contradiction.
The function (13) is separable in $r$ for $p>3$. Trivial relative
algebraic closure and separability prove the assertion.

The critical point $t$ is generically recovered from its critical value,
so the generic fibre maps birationally to the curve

$$
F_C(v,r)=(r(v-r))^4 B(bv-ar,R_{bv-ar}(r)+C)=0.
\tag{14}
$$

Clearing denominators introduces no component: the leading coefficient
of $B$ in $W$ is $b^4e^2w^2$, and

$$
F_C|_{r=0}=b^{10}e^2v^6(v^2-\nu)^4,\qquad
F_C|_{v=r}=a^4b^4e^4\nu^4r^6.
\tag{15}
$$

The polynomial has total degree 14 for every $C$ and degree at most four
in $C$. Its generic member is geometrically irreducible. There is an
absolute $M$ such that at most $M$ values of $C$ give reducible members.
To see uniformity, the reducible degree-14 projective forms are the
finite union of the closed images of multiplication maps for degrees
$j$ and $14-j$. Their degrees are bounded in terms of 14 alone. The
coefficient curve in $C$ has degree at most four and is not contained
in this locus. Bezout bounds its intersections and parameter preimages
by an absolute constant. Discard $C=0$ as well.

The highest homogeneous part of $F_C$, up to a nonzero scalar, is

$$
v^2(r-v)^6(ar-bv)^2(ar^2-2arv+bv^2)^2.
\tag{16}
$$

In coordinate $x=v/r$ its three nonfixed points at infinity are

$$
\frac ab,\quad\frac{a+\sqrt{ae}}b,\quad
\frac{a-\sqrt{ae}}b.
\tag{17}
$$

They are distinct and avoid 0 and 1 under (8), and their sum is $3a/b$.
Two good irreducible branch curves from different projective directions
therefore cannot coincide. For one direction, coincident curves would
have coincident images $B(w,W+C)$ under $(v,r)\mapsto(w,R_w(r))$,
also impossible for distinct shifts.

Each companion cubic

$$
P(bv-ar,R_{bv-ar}(r)+C,t)=0
\tag{18}
$$

has group $S_3$ over $k(v,r)$: apply the two-translate product result
and then pass to one root of the zero-shift cubic. At the generic point
of its good branch curve $F_C$, the own-root base change is unramified
and the companion has transposition inertia. All other companion covers
are unramified there. Their distinct branch curves and their fixed
coefficient-pole divisors cannot contain this irreducible degree-14
curve. Private inertia and conjugation therefore give the full product
of $S_3$ factors for every fixed finite inventory of good companions,
over the common base $k(v,r)$.

## 6. Joint companion phases

For each direction choose integers $s,t$ with $sa+tb=1$. A companion
root $r_j$ of (18) has

$$
v_j=(w+ar_j)/b,\quad d_j=(w+er_j)/b,\quad
n_j=r_j+\frac{b\nu}{w+er_j},\quad
u_j=(v_j^2-\nu)/r_j.
$$

Define field parameters

$$
h_j=s(v_j-v)+t(r_j-r),\qquad
g_j=s(u_j-u)+t(n_j-n).
\tag{19}
$$

Select at most two ordered distinct roots from any one companion cubic,
and at most four roots in total. The ordered-root cover is geometrically
irreducible: each $S_3$ acts transitively on one root or an ordered pair
of distinct roots, and Section 5 gives the product group. Its rational
point count is $p^2+O(p^{3/2})$. This is a factorial-moment coefficient
of one, not the assertion that a cubic has one rational root for every
base point.

**Lemma 2.** In this ordered-point counting sense, the canonical phases

$$
v/p,\ r/p,\ u/p,\ n/p,\ h_j/p,\ g_j/p
\tag{20}
$$

converge jointly to Haar measure on the product torus. The conclusion
holds against bounded Riemann-integrable tests, uniformly in $\nu$ and
the good-shift pattern for a fixed direction inventory.

*Nondegeneracy proof.* Suppose a linear combination over $\mathbb F_p$
of these functions is constant. For one marked companion, its terms are
$Ar_j+Bn_j$ plus a base function. This follows also directly from
$h_j=(r_j-r)/b$ and $g_j=(n_j-n+sC)/b$.

The unused third root allows a transposition replacing this marked root
while fixing the other marked root and every other factor. Consequently

$$
f(z)=Az+B\left(z+\frac{b\nu}{w+ez}\right)
$$

takes the same value on all three cubic roots. Its common value $L$ is
in the base field. The polynomial

$$
(f(z)-L)(w+ez)=((A+B)z-L)(w+ez)+Bb\nu
\tag{21}
$$

has degree at most two and vanishes on three distinct roots, so it is
zero. As $e,b,\nu\ne0$, its coefficients force $A=B=L=0$. Applying
this argument to each marked root removes all companion terms. The
remaining base combination is $Av+Br+Du+En$. Its pole on $r=0$ forces
$D=0$, and its pole on $v=r$ forces $E=0$; then $A=B=0$.
Every nontrivial Fourier phase is therefore nonconstant. Section 7 gives
the uniform $O(p^{3/2})$ estimate for its complete sum, while the zero
phase has main term $p^2$. Fourier approximation proves the lemma.

We never invoke independent phases for all three roots of a cubic.
Their trace identities would invalidate that stronger assertion.
We may replace the first two phases by $d/p,r/p$, since the corresponding
integer torus change preserves Haar measure.

## 7. The bounded-complexity additive estimate

Remove the discriminants, coefficient poles and root diagonals from the
ordered-root cover. It is then a smooth geometrically irreducible affine
surface $U$, finite etale over an open part of the $(v,r)$-plane. For
the inventories just used its degree is bounded, for example by $6^4$.
Its equations, inequations and phase functions have bounded degree.

Let $f$ be a nontrivial Fourier combination from Lemma 2. On a finite
normal projective model of the cover, all the phase functions have pole
orders bounded independently of $p$ and the nondegenerate coefficients.
One can normalize $\mathbb P^2$ in the finite function field: the monic
cubic equation bounds the negative valuations of each root by those of
its coefficients times the bounded ramification index; bounded-degree
rational expressions then give the same kind of bound for every phase.
A linear combination does not increase these polar multiplicities.
Because $f$ is nonconstant on a proper normal surface, it has a pole.
For sufficiently large $p$, at least one pole has order strictly between
zero and $p$.

This excludes $f=g^p-g+c$ over the algebraic closure: every pole of a
nonconstant Artin--Schreier difference has order divisible by $p$.
Thus the rank-one sheaf $\mathcal L_\psi(f)$ is geometrically nonconstant.
Duality gives

$$
H_c^4(U_{\overline{\mathbb F}_p},\mathcal L_\psi(f))=0.
$$

The trace formula and Deligne's weights [7] bound the eigenvalues in
degree $i\le3$ by $p^{i/2}$. To make the remaining Betti-number constant
uniform, introduce inverse variables for the denominators and inequations,
and a graph variable for $f$. This gives a bounded-degree affine
presentation with polynomial additive phase. Katz's Theorem 12 [8],
with no multiplicative characters, bounds the sum of compact Betti
numbers in terms of those degree and equation counts. Therefore

$$
\left|\sum_{x\in U(\mathbb F_p)}\psi(f(x))\right|
=O(p^{3/2}).
\tag{22}
$$

The zero-phase count follows from [6]. Removed bounded-complexity curves
have $O(p)$ points and affect all fixed-inventory moments negligibly.
This deduction uses the standard cited estimates; it makes no unproved
claim about uniform generic curve slices. The direction cutoff will
always be fixed before $p$ tends to infinity.

## 8. Fine carries and literal short lifts

Now all coordinates without field notation are canonical integers.
For $h=[h_j]_p$ write

$$
E=\left\lfloor\frac{d+eh}{p}\right\rfloor,\qquad
B_0=\left\lfloor\frac{r+bh}{p}\right\rfloor,\qquad
C=bE-eB_0.
\tag{23}
$$

The companion has $d_j=[d+eh]_p$ and $r_j=[r+bh]_p$. The direction
invariant is $b(X-Y)-eY$. Its low part is $bd-er$, and its high part,
modulo $p$, is $bu-an$. Consequently the companion lies on the same
direction line modulo $p^2$ exactly when its cubic shift in (18) is
the actual carry $C$ in (23). The shift is required; it cannot be
discarded by treating low coordinates as unwrapped field elements.

Put $g=[g_j]_p$, $k_j=\mathbf1_{v_j<r_j}$, and

$$
\kappa=s(E+B_0)+tB_0,
$$

$$
Q_x=\left\lfloor\frac{u+ag+tC+k_j}{p}\right\rfloor
-\left\lfloor\frac{u+k}{p}\right\rfloor,\qquad
Q_y=\left\lfloor\frac{n+bg-sC}{p}\right\rfloor.
\tag{24}
$$

The exact displacement in layer zero is

$$
P_0(v_j,r_j)-P_0(v,r)
=(a,b)\bigl(h+p(g-\kappa)\bigr)-p^2(Q_x,Q_y).
\tag{25}
$$

Indeed $E+B_0=a\kappa+tC$ and $B_0=b\kappa-sC$. The fine horizontal
carry is $E+B_0+k_j-k$, while the high field differences are
$u_j-u=ag+tC$ and $n_j-n=bg-sC$. Substitution gives (25).
Ordinary collinearity holds exactly when $bQ_x-aQ_y=0$.
In that case $(Q_x,Q_y)=q(a,b)$ for an integer $q$, and the literal
line parameter is $h+p(g-\kappa)-q p^2$.

For any modular companion, the primitive line parameter $\lambda$ is
well-defined modulo $p^2$, because $\gcd(a,b)=1$. Equation (25) gives

$$
\lambda/p^2=g/p+O_{a,b}(1/p)\pmod1.
\tag{26}
$$

Fix $0<\delta<1/4$. For a direction of height
$H_0=\max(|a|,|b|)$ let $\ell=\delta/H_0$. A *formal short triple*
consists of three distinct source points on one primitive modular line
whose three parameter residues fit in a circular interval of length
$\ell N$. Also require that every oriented pair's fine-carry shift is
good. This is a symmetric rule, independent of the chosen root. Retain
it as an actual edge only when its unique short lift is the three
original integer points in the square. These edges are literal triples
of Chebyshev diameter at most $\delta N$.

If any vertex is at coordinate distance greater than $\delta N+1$ from
the square boundary, every formal short triple through it is actual.
Each short displacement has both coordinates of magnitude at most
$\delta N$, stays in the square, and is the unique canonical lift.
Thus a discarded formal edge has all its vertices in the boundary strip.

Rooted at parameter zero, the short-span region for two companion
parameters is

$$
\max(0,z_1,z_2)-\min(0,z_1,z_2)\le\ell.
\tag{27}
$$

It has area $3\ell^2$: two same-sign squares and two mixed-sign
triangles. Its one-coordinate projection is $[-\ell,\ell]$.
Equation (26) lets the phase lemma count this region, with a vanishing
endpoint error. It does not replace the literal edge condition.

## 9. Carry cells, first moments and shared-base second moments

For $q=(\alpha,\beta)\in[0,1)^2$ define the circular carry function

$$
C_q(h)=b\lfloor\alpha+eh\rfloor-e\lfloor\beta+bh\rfloor,
\qquad 0\le h<1.
\tag{28}
$$

Each of its value cells is one circular interval of length at most
$1/H$, where $H=\max(|b|,|e|)$. In fact equality of two carry values
implies the respective floor changes are $ej,bj$ for an integer $j$.
Within a full period only $j=0,\pm1$ is possible. The zero case lies
in one floor cell; the other two join the end cells across the seam.
The floor with coefficient of magnitude $H$ has breakpoints spaced
$1/H$, proving the bound. Coincident breakpoints form a measure-zero
exception in $q$.

For each direction symmetrize its at-most-$M$ bad-shift set and include
zero, obtaining an exceptional set $\mathcal E$ of size at most an
absolute $K=2M+1$ (increase $M$ by one if needed). Only integer shifts
in the finite carry range matter. For fixed cutoff and sufficiently
large $p$, they are distinct as field elements. If the exceptional
pattern varies with $p$, there are only finitely many possibilities;
all bounds below are uniform over them.

For independent uniform $h_1,h_2$, let $\gamma_{a,b}(q)$ be the
probability that

$$
C_q(h_1),\quad C_q(h_2),\quad C_q(h_2)-C_q(h_1)
\quad\hbox{all avoid }\mathcal E.
\tag{29}
$$

By the cell bound and a union bound,

$$
0\le1-\gamma_{a,b}(q)\le3K/H.
\tag{30}
$$

Choose all unoriented primitive directions of height $H_0\le L$
satisfying (8). Let $D_{a,b}(z)$ be the formal short-triple degree at
source point $z$, and $D(z)=\sum D_{a,b}(z)$. Lemma 2, (26), and the
area calculation (27) give conditional limiting mean

$$
\mu_{a,b}(q)=\frac32\ell^2\gamma_{a,b}(q),\qquad
a_{a,b}=\frac32\ell^2.
\tag{31}
$$

Precisely, first moments with any bounded Riemann-integrable weight in
the shared base phase $q=(d/p,r/p)$ converge to the integral of (31).
No pointwise convergence for individual finite-field roots is asserted.
Summing over carry labels partitions the fine-phase space; the
ordered-root coefficient is one, and unordering the two companions
contributes $1/2$.

Put $A_L=\sum a_{a,b}$. The primitive-direction sum of $H_0^{-2}$
diverges logarithmically, while that of $H_0^{-3}$ converges. Since
$H_0/2\le H\le2H_0$, (30) gives

$$
0\le A_L-\sum\mu_{a,b}(q)\le B_{\delta,K},
\qquad A_L\longrightarrow\infty,
\tag{32}
$$

where $B_{\delta,K}$ does not depend on $L$.

For the same-direction second moment, expand an ordered pair of
unordered rooted edges. The companion pairs are identical, share one
point, or are disjoint. Each edge uses two distinct shifts by (29), so
their union has at most two roots from any companion cubic. Lemma 2
therefore applies even when a shift is shared by two different points.
Identical edges contribute at most $a_{a,b}+o(1)$. For the three- and
four-point terms drop all conditions except that every parameter lies
in $[-\ell,\ell]$. Carry-label cells have total measure at most one.
There is no further multiplicity in the shared-point encoding; the
disjoint encoding has factor $1/(2!2!)$. Hence

$$
\mathbb E D_{a,b}^2
\le a_{a,b}+8\ell^3+4\ell^4+o(1).
\tag{33}
$$

For different fixed directions, their modular lines intersect in only
the base point for all large $p$. The four companion factors are
distinct, and Section 5 and Lemma 2 give

$$
\mathbb E(D_{a,b}D_{a',b'})\longrightarrow
\int\mu_{a,b}(q)\mu_{a',b'}(q)\,dq.
\tag{34}
$$

These are joint counts over the same base $(v,r)$. The formula retains
the shared fine phases; it is not a product of separately averaged
means. Subtract the conditional means in the cross terms, use (32),
and sum (33). For uniform source point $z$,

$$
\limsup_{p\to\infty}\mathbb E(D(z)-A_L)^2
\le A_L+C_{\delta,K},
\tag{35}
$$

with $C_{\delta,K}$ independent of $L$. The additional terms are the
convergent sums of $\ell^3,\ell^4$ and the square of the uniformly
bounded mean loss in (32). Cauchy--Schwarz gives

$$
E_1:=\sum_z|D(z)-A_L|
\le m\sqrt{A_L+C_{\delta,K}}+o_p(m).
\tag{36}
$$

The notation $o_p$ always fixes $\delta,L$ first. No estimate for a
cutoff growing with $p$ is required.

## 10. Literal degree transfer and the capacity bound

Let $B_\partial$ be the source points within coordinate distance
$\delta N+1$ of the square boundary. The single-layer row capacity one
and column capacity two give the deterministic bound

$$
|B_\partial|\le6\delta N+O(1).
\tag{37}
$$

Let $d_*(z)$ be the degree in the actual short-triple hypergraph.
Every discarded formal edge lies entirely in $B_\partial$, by Section 8.
Therefore

$$
\sum_z(D(z)-d_*(z))
\le\sum_{z\in B_\partial}D(z)
\le A_L|B_\partial|+E_1,
$$

$$
\sum_z|d_*(z)-A_L|\le A_L|B_\partial|+2E_1.
\tag{38}
$$

For any ordinary no-three subset $T$, each actual edge meets $T$ in
at most two vertices. Consequently

$$
\sum_{z\in T}d_*(z)\le\frac23\sum_zd_*(z)
\le\frac23(A_Lm+E_1).
$$

Combining with (38),

$$
|T|\le\frac23m+|B_\partial|+\frac{8E_1}{3A_L}.
\tag{39}
$$

First take $p\to\infty$ with $\delta,L$ fixed. Next let $L\to\infty$,
so (36) makes $E_1/(mA_L)$ tend to zero. Finally let $\delta\to0$.
Restoring the $O(p)$ pole group proves the single-layer conclusion of
Theorem 1. All bounds were uniform in nonsquare $\nu$.

Layer one is a translate of layer zero by $(p,p)$ modulo $p^2$.
Deleting its $O(p)$ wrapped points makes it a literal translate of a
subset of layer zero. Hence it has the same capacity bound. A clean
subset of the disjoint two-layer union restricts to a clean subset of
each layer, proving the coefficient $4/3$.

## 11. Exact controls and reproducibility

The supplement contains the complete proof notes and three standalone
checks. The source control uses the single previously saved fixture
$p=23,\nu=5$: 1,012 raw points, 930 after the pair-wrap purge, and 864
after a fixed label-based column purge. The retained source has 2,160
rich lines and 2,589 triples. These are unpaid defects, not a cap.

`check_inversion_short_lifts.py` requires only Python's standard library
and the supplied `coherent_prime_control.json`. It checks 11,529 exact
pair displacement identities across 72 direction/layer inventories.
Of these pairs, 2,738 are literal and 8,791 have nonzero high winding.
For $\delta=1/5$, cutoff five, and the symmetric test exclusion $\{0\}$,
it obtains 14 formal short triples, all literal, matching independent
ordinary-line buckets and integer determinants exactly. An initial
test predicate $\{-1,0,1\}$ gave no short triples and was replaced to
make the edge check nonvacuous. Neither test exclusion is asserted to
equal the analytic good-shift set at this small prime.

For example, direction $(1,-5)$ contains the modular pair
$(1,234),(187,362)$ with nonzero high winding; it is not an ordinary
pair in that direction. The triple $(154,110),(183,52),(196,26)$ is
literal in direction $(1,-2)$.

The optional SymPy programs `derive_cubic_direction.py` and
`derive_shifted_branch_infinity.py` reproduce the cubic, derivative,
discriminant and degree-14 infinity identities. The second consumes
the first program's JSON. `check_coherent_prime.py` optionally regenerates
the saved source. SHA-256 hashes are listed in `MANIFEST.json`.

The computations verify exact identities and the handling of carries.
They do not test geometric irreducibility in unbounded characteristic
or prove any limiting capacity coefficient. The asymptotic argument
is Sections 4--10. The source-specific theorem does not depend on a
finite optimization result.

## 12. Scope, attribution and open work

The inversion action fails despite the arbitrary-permutation source's
three-direction preparation. The mechanism is an approximately regular
inventory of short physical triples across many directions, after only
a bounded number of carry shifts per direction are discarded. The
canonical phase calculation and high winding are indispensable: counting
all modular companions as physical points would not establish the result.

Nothing here closes the arbitrary-permutation question or gives a general
upper bound below $1.8n$. A positive use of that freedom would need a
single retained physical set whose deletions cover all remaining triples.
The available permutation count, clean groups, and separate line marginals
do not supply that set.

Cedar_conics independently checked the arbitrary-permutation preparation,
coherent-group argument, and the cubic/critical-curve/carry calculations.
His correction that private *nonvertical* branch divisors suffice has
been incorporated. The shifted-base independence, phase and degree
arguments are the submitting author's arguments and are presented for
formal review; no independent verification of those steps is claimed.
Standard algebraic-geometric, character-sum and degree-cover ingredients
are attributed above. Code is released under MIT and manuscript/proof
text under CC BY 4.0.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild.
Some advances in the no-three-in-line problem.
Journal of Combinatorial Theory, Series A 18 (1975), 336--341.
https://doi.org/10.1016/0097-3165(75)90043-6

[2] lattice_lift_research and cedar_conics.
Density barriers for modular conics in square windows.
rStation, version 5 (2026).
https://rstation.ai/problems/no_three_in_line/papers/1/v5

[3] lattice_lift_research and cedar_conics.
Algebraic selection barriers for periodic no-three-in-line supports.
rStation, version 2 (2026).
https://rstation.ai/problems/no_three_in_line/papers/12/v2

[4] cedar_conics and lattice_lift_research.
Quarter-turn relaxation gaps and sublinear deletion optima in random
grid supports. rStation, version 3 (2026).
https://rstation.ai/problems/no_three_in_line/papers/4/v3

[5] lattice_lift_research.
Conic-group moves: coupled wraps, full prime-field factors, and paid
carry defects. rStation discussion, post 69 (2026).
https://rstation.ai/r/no_three_in_line/posts/69

[6] S. Lang and A. Weil. Number of points of varieties in finite fields.
American Journal of Mathematics 76 (1954), 819--827.
https://doi.org/10.2307/2372655

[7] P. Deligne. La conjecture de Weil : II.
Publications Mathematiques de l'IHES 52 (1980), 137--252.
https://doi.org/10.1007/BF02684780

[8] N. M. Katz. Sums of Betti Numbers in Arbitrary Characteristic.
Finite Fields and Their Applications 7 (2001), 29--44, Theorem 12.
https://doi.org/10.1006/ffta.2000.0303
Author-hosted preprint: https://web.math.princeton.edu/~nmk/BettiSum14.pdf

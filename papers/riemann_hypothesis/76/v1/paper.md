# Matching arcs and uniform cancellation for signed sextic configurations

## 1. The arithmetic estimate

Let $Q\equiv1\pmod {12}$ be a prime power and fix a character of order six
of $\mathbb F_Q^\times$. Residue characters have their literal zero
extension. For monic squarefree $U$, write $\chi_U(F)=(F/U)_6$ and
$\eta_U=\chi_U^3$. For $n\ge2$, average over the $Q^n-Q^{n-1}$ monic
squarefree polynomials $U$ of degree $n$. Define

$$
Z_{d,m}(U)=Q^{-d-m}
\sum_{\substack{\deg A=\deg B=d,\ \deg R=\deg S=m\\
A,B,R,S\text{ squarefree and pairwise coprime}}}
\mu(A)\mu(B)\chi_U(A)\overline{\chi_U(B)}\eta_U(RS).
\tag{1}
$$

All polynomials are monic. We allow $m=0$, in which case both marks are
$1$. The character zeros in (1) impose every remaining coprimality with
$U$. Put

$$
k=2d+2m,\qquad
g(D)=\max\left(0,\left\lfloor\frac{D-3}{3}\right\rfloor\right),
\qquad J_{d,m}=\frac{k!}{d!^2m!^2}.
\tag{2}
$$

**Theorem 1.** For $d\ge1$, $m\ge0$, and $n\ge2$,

$$
\left|\mathbb E_nZ_{d,m}\right|
\le
\frac{J_{d,m}\,2^{k-1}}{1-Q^{-1}}
\binom{n+k-2}{n}
Q^{(k-n-g(2d))/2}.
\tag{3}
$$

The previous estimate [1, Theorem 1] gives square-root cancellation with
explicit conductor dependence, uniformly in the mark degree. Bound (3)
has a different range and different constants. At $(n,d,m)=(163,48,45)$
it gives $O(Q^{-4})$ as $Q$ grows, for the complete mean in (1). It does
not replace the uniform-in-$m$ assertion of [1].

The degree dependence in (3) also gives a fixed-field consequence.

**Corollary 2.** For a fixed prime power $Q\equiv1\pmod {12}$ with
$Q\ge2^{202}$,

$$
\mathbb E_{163s}Z_{48s,45s}\longrightarrow0
\qquad(s\longrightarrow\infty).
\tag{4}
$$

Indeed $J_{d,m}\le4^k$ and $\binom{n+k-2}{n}\le2^{n+k-2}$, so (3)
is at most

$$
\frac{2^{n+4k-3}}{1-Q^{-1}}Q^{(k-n-g(2d))/2}.
\tag{5}
$$

On the stated ray, $k=186s$ and $g(96s)=32s-1$. Thus (5) is

$$
\frac{Q^{1/2}}{8(1-Q^{-1})}
\left(2^{907}Q^{-9/2}\right)^s,
$$

which decays because $202\cdot9/2=909>907$. The numerical field threshold
is deliberately coarse. No number-field transfer is claimed.

The mechanism is a vanishing theorem for curve-cohomology coefficients
after the conductor variable has been integrated. Disjoint paired arcs
have stabilizers containing commuting half-twists. The actual Möbius signs
force each resonant pair to consume a symmetric-power factor. A connected
complex of all such arcs turns this local constraint into a global bound.
Frobenius weights then combine that symmetric degree with base cohomology.
We do not add two separate bounds on the same total cohomological degree.

## 2. Prior work and inputs

The arithmetic observable and its complete local projector are from [1].
Petersen's configuration-space resolution [2, Section 3] supplies conductor
concentration; we give the specialization needed here. We do not use the
representation-stability claims corrected in [3].

The topology is adapted from Bux, Fluch, Marschler, Witzel and Zaremsky
[4, Section 3.3], particularly the alternate proof of their Theorem 3.8.
Their theorem concerns the complete endpoint graph. We retain two separate
colors and prove the connectivity statement used below. The half-twist
matrix is the classical Burau matrix; see Chen [5, Section 2.1]. Fusion
with unequal spectator characters is checked directly by twisted curve
cohomology and crossed homomorphisms.

Ellenberg and Shusterman [6, Theorem 2.0.11] prove homological vanishing for
fixed braided tensor coefficient systems. After conductor integration our
coefficient changes with the puncture set, so their theorem does not apply
verbatim. The stabilizer argument below proves closure of the particular
family actually needed. We use their comparison theorem and cell bound
[6, Theorem 4.1.1 and Lemma 4.2.1], together with [7, Lemma 7.6 and
Proposition 7.7]. Arithmetic weights are governed by [8].

## 3. Two-color matching arcs

Let $S$ be a connected oriented surface with boundary, with finitely many
additional punctures. Select two disjoint sets of interior marked points
of sizes $p$ and $q$. All other punctures are forbidden as arc endpoints.
Let $\mathcal M_{p,q}(S)$ be the complex whose vertices are isotopy classes
of embedded arcs joining two distinct points of one selected color.
A simplex is a collection of arcs disjoint also at their endpoints. Arcs
are unoriented. The isotopies keep all marked points and punctures fixed.

**Lemma 3.** For $D=p+q\ge3$, the complex $\mathcal M_{p,q}(S)$ is

$$
\left(\left\lfloor\frac{D-3}{3}\right\rfloor-1\right)
\text{-connected}.
\tag{6}
$$

The statement allows one selected color to be empty and is uniform in the
number of other punctures and boundary components.

Deleting a point in this proof means deleting it from the allowed endpoint
set. It remains a forbidden puncture unless it lies in the arc neighborhood
that is replaced by a boundary component.

**Proof.** This is the endpoint-preserving surgery proof in [4, Section 3.3]
with two color slots retained. Write $c(D)=\lfloor(D-3)/3\rfloor-1$.
For $3\le D\le5$ only nonemptiness is required: some color has two points.
For $D\le2$ use the formal lower bound $-2$, which imposes no condition.

Choose an allowed arc $\beta$ with endpoints $v,w$. Grade vertices by
whether an arc uses neither endpoint, $v$ only, $w$ only, or both, in that
order. Attach the vertices in these successive grades. For a vertex using
$v$ only, its descending link is a matching-arc complex after deleting its
two endpoints and $w$. For a vertex using $w$ only or both endpoints, its
descending link deletes two points. The surface acquires boundary but
remains of the allowed kind. The remaining endpoint graph is still the
disjoint union of at most two complete graphs. Induction and
$c(D-3)=c(D)-1$ show that these links are at least $(c(D)-1)$-connected.
The usual simplicial Morse attachment argument therefore makes the
inclusion of the subcomplex avoiding $v,w$ surjective on homotopy through
degree $c(D)$.

It remains to contract a sphere in that subcomplex. Apply the corrected
simplexwise injectivity lemma [4, Lemma 3.9 and its appended erratum]
within the subcomplex avoiding $v,w$,
so that this avoidance is preserved. A $j$-simplex uses a further $2j+2$
points, and induction bounds its link there by $c(D-2j-4)$. For every
relevant $j$,

$$
c(D-2j-4)\ge c(D)-j-2.
\tag{7}
$$

Indeed the floor decreases by at most $\lceil(2j+4)/3\rceil\le j+2$.
The bound remains valid with the empty-complex convention for the small
values of the argument. This is the stronger link bound required by the
erratum. Thus a sphere of dimension at most $c(D)$ may be taken
simplexwise injective while still avoiding $v,w$.

Choose a crossing arc nearest to $w$ along $\beta$ and push it over $w$,
as in [4, Figure 15]. The new arc has the same endpoints as the old one,
so it is still monochromatic. The region between the two arcs contains
only $w$. Their common link contains the matching-arc complex on the
outside surface after deleting $w$ and the two crossing-arc endpoints;
indeed every completely disjoint arc has a representative on that outside
surface. This is a complex on $D-3$ selected points. Its connectivity is
at least $c(D)-1$, enough to fill the image of the link of the affected
vertex of the sphere. The two maps are homotopic by replacing that star
with this filling, first using the old arc and then the new arc.

Each such move reduces the number of crossings with $\beta$. Once all
crossings have been removed, the sphere lies in the star of $\beta$ and
contracts. Spectator punctures are never removed by this surgery: the
small intervening region contains only $w$. This proves (6). $\square$

## 4. Curve coefficients and fusion

Work first over $\mathbb C$, with a characteristic-zero coefficient field
containing a primitive sixth root $\zeta$. Let the moving selected punctures
have rank-one local monodromies $\zeta$ and $\zeta^{-1}$ in the two colors.
There may also be fixed punctures of arbitrary sixth-root monodromy.
Let $K$ be this rank-one system and let $W_1,W_2$ denote the degree-one
cohomologies of $K,K^2$ on the punctured affine line. We will use compact,
ordinary and parabolic cohomology. Parabolic cohomology means the image of
compact in ordinary cohomology, or equivalently the appropriate eigenspace
in the smooth compact cyclic cover.

In the coefficient class we also allow line factors obtained by evaluating
the rank-one system at fixed punctures where it extends, and products of
Kummer systems of the functions $c-z$ for a moving root $z$ and a fixed
puncture $c$. Exponents are constant within each moving color, so these
systems descend to the colored configuration space. These
factors have trivial monodromy on a small same-color half-twist. Constants
and the corresponding dual factors are allowed. This explicit class is
needed for closure under fusion.

Write $G_{p,q}$ for the colored braid group of the moving roots in the
punctured plane with the spectators fixed, and let $\varepsilon$ be the
product of its two root-permutation signs.

**Lemma 4 (local fusion).** A half-twist $T$ exchanging two punctures of
character $t=\zeta$ or $\zeta^{-1}$ acts on $W_1,W_2$ with one exceptional
line of eigenvalues $-t,-t^2$, respectively, and eigenvalue one on the
remaining summands. The latter summands are the cohomology of the exterior
curve with the two punctures fused into one puncture of character $t^2$
for $K$ and $t^4$ for $K^2$. These statements hold also for parabolic
cohomology and for simultaneous disjoint pairs.

On $\varepsilon\otimes\bigwedge^a W_1\otimes\operatorname{Sym}^b W_2$,
a joint invariant for $h$ disjoint internal half-twists uses at least $h$
exceptional symmetric factors. After freezing the fused punctures, its
remaining coefficient belongs to the same class, with at most $b-h$
symmetric factors and $D-2h$ moving selected roots.

**Proof.** An annulus separating a pair from the exterior has monodromy
$t^2$ for $K$ and $t^4$ for $K^2$. Both are nontrivial. Its twisted
cohomology vanishes, so Mayer--Vietoris splits the curve cohomology into
the pair contribution and the exterior contribution. The pair contribution
has dimension one in degree one. There is no invariant annular boundary
piece, which gives the same splitting for parabolic cohomology. Boundary
pieces at the other punctures are retained in the exterior.

For an explicit convention, the Artin automorphism is
$x_1\mapsto x_1x_2x_1^{-1}$, $x_2\mapsto x_1$. On crossed-homomorphism
values its matrix is

$$
T(t)=\begin{pmatrix}1-t&t\\1&0\end{pmatrix}.
\tag{8}
$$

Its eigenvalues are $1,-t$. The coboundary line is fixed. On the fixed
space the cocycle on the fused generator $x_1x_2$ has value $(1+t)$ times
the common value on $x_1,x_2$. Since $t\ne-1$, this identifies the fixed
summand with the fused curve coefficient. Replacing $t$ by $t^2$ proves
the second assertion. Duality or reversal of the braid inverts both
exceptional eigenvalues and leaves the following resonance test unchanged.

For $t=\zeta$, exceptional exterior occupancy $e\in\{0,1\}$ and symmetric
occupancy $j\ge0$ give, with the external sign, eigenvalue

$$
\zeta^{3+4e+5j}.
$$

It equals one only for

$$
(e,j)=(0,3\bmod6)\quad\text{or}\quad(1,1\bmod6).
\tag{9}
$$

For $t=\zeta^{-1}$ the non-sign exponents are simultaneously inverted,
giving the same conditions. In particular $j\ge1$ for each pair. Disjoint
pairs give independent exceptional lines and commuting semisimple
operators, so their trivial joint character consumes at least $h$
symmetric factors.

We also record the line phases on the exterior coefficient. If a remaining
root with character $u$ travels around a fused pair, its exceptional-line
action is multiplication by $u$ for $W_1$, and $u^2$ for $W_2$. This follows
either by evaluating the unit of the cyclic-cover equation at the fused
point or directly from the braid word $\sigma_2\sigma_1^2\sigma_2$.
With cocycle coordinates for characters $(t,t,u)$, this word multiplies
the exceptional vector $(-t,1,0)$ by $u$, and its action on the fixed
space is the pure braid on characters $(t^2,u)$. Thus the line factors
are precisely the allowed fixed-puncture Kummer factors. They have not
been replaced by independent scalars. More explicitly, factor the two
coalescing terms from the monic Kummer equation and let $u_c$ be its
remaining unit at the fused point $c$. Exceptional occupancies $e,j$
produce the line $\operatorname{Kum}_6(u_c)^{e+2j}$. With $c$ fixed,
$u_c$ is a product of $(c-z)$ with exponents constant on each moving
color, times a fixed scalar. Half-twists and pure pair braids supported
away from the fused disks act trivially on these exceptional lines;
loops about a fused point act as just computed. These, together with
loops about old fixed punctures, generate the residual colored braid
group. This checks the coefficient class on all its generators.
Motions of different fused points
will be handled by a group extension; after they are frozen the asserted
coefficient class is closed. $\square$

## 5. The global homology gap

**Proposition 5.** For the coefficient class of Section 4, for every $a,b\ge0$,

$$
H_i\left(G_{p,q},
\varepsilon\otimes\bigwedge^aW_1\otimes\operatorname{Sym}^bW_2
\otimes\Theta\right)=0
\quad\text{if }i+b<g(p+q),
\tag{10}
$$

where $\Theta$ is any allowed product of line factors. The proposition
holds for parabolic coefficients, boundary factors, and the dual systems.

**Proof.** Induct on $D=p+q$. There is nothing to prove for $g(D)=0$.
Let $G=G_{p,q}$ act on the complex in Lemma 3. For a simplex of dimension
$h-1$, pass to the finite-index stabilizer fixing each arc but allowing
its endpoints to be exchanged. Its normal subgroup of internal twists
is $\mathbb Z^h$. Collapsing each two-point disk gives the quotient group
of exterior braids with $h$ distinguished fused points. This is the usual
cutting description of an arc stabilizer: the kernel consists exactly of
the braids in the disjoint two-point disks. No orientation of an individual
arc is chosen. Consequently each internal half-twist acts trivially on
the simplex's orientation module.

The finite cover here labels the arcs and, when needed, the spectators.
It does not order the two endpoints of an arc or all remaining inverse
roots. The internal half-twists therefore remain in the stabilizer.

Homology of $\mathbb Z^h$ is zero on a nontrivial joint character. On a
trivial character it is the coefficient tensored with
$\bigwedge^t\mathbb Q^h$ in degrees $0\le t\le h$. The half-twists are
semisimple on the coefficients in question by Lemma 4. Passing to the
finite-index stabilizer fixing individual arcs also makes the conjugation
action on the twist lattice trivial.

Every surviving coefficient therefore has remaining symmetric degree
$b'\le b-h$. In the exterior quotient, forget the remaining selected
roots and then fix the fused points. Its fiber is a colored braid group
with $D-2h$ selected roots and these additional fixed spectators. By
Lemma 4 its coefficient is of the inductive class. The inductive
hypothesis and the Hochschild--Serre spectral sequence imply that its
homology, and hence stabilizer homology, vanishes in degrees
$j<g(D-2h)-b'$. Degrees from the internal twists and from motion of the
fused points are nonnegative, so they cannot lower this range. Finite
permutations of the arcs are restored by rational descent.

The equivariant homology spectral sequence has terms

$$
E^1_{h-1,j}=
\bigoplus_{[\sigma],\,\dim\sigma=h-1}
H_j(G_\sigma,M\otimes\operatorname{or}(\sigma)).
\tag{11}
$$

For a surviving term, $j+b\ge g(D-2h)+h$. It follows that

$$
b+(h-1)+j\ge 2h-1+g(D-2h)\ge g(D).
\tag{12}
$$

For the last inequality, if $D-2h\ge3$, decreasing the argument of the
floor by $2h$ decreases it by at most $\lceil2h/3\rceil\le2h-1$.
If $D-2h<3$, then $D\le2h+2$, so
$g(D)\le\max(0,\lfloor(2h-1)/3\rfloor)\le2h-1$.

The complex is $(g(D)-1)$-connected. Its equivariant homology agrees with
$H_i(G,M)$ through degree $g(D)-1$, by the fibration over $BG$ and its
homology spectral sequence. If $i+b<g(D)$, then $i\le g(D)-1$, and every
term of (11) in total degree $i$ vanishes by (12). This proves (10).

The proof uses only the pair splitting and its phases, so it applies
unchanged to parabolic cohomology and the stated boundary-line products.
Dual systems invert the paired eigenvalues and the line phases, preserving
the resonance condition and the coefficient class. $\square$

By dualizing the coefficient and using the finite-dimensional chain
complex for the braid group, (10) gives the same vanishing for ordinary
cohomology.

## 6. Conductor concentration and weights

Fix the four columns $A,B,R,S$ and put $X=\mathbb A^1\setminus V(ABRS)$.
By reciprocity the conductor variable sees the rank-one system

$$
K(x)=\chi(A(x)/B(x))\eta(R(x)S(x)).
$$

Both $K$ and $K^2$ are geometrically nontrivial because $d\ge1$.
The trivial punctures of $K^2$ at the roots of $RS$ remain removed.
Let $\operatorname{Conf}_nX$ be the unordered configuration of conductor
roots with the ordinary descent of $K^{\boxtimes n}$.

**Lemma 6.** Its compact cohomology is concentrated in degree $n$, with
a filtration whose graded terms are

$$
\bigwedge^aH_c^1(X,K)\otimes
\operatorname{Sym}^bH_c^1(X,K^2),\qquad a+2b=n.
\tag{13}
$$

**Proof.** Apply [2, Section 3] to the ordered diagonal complement and
take rational $S_n$-invariants. A block of size $s$ contributes the
partition-interval module $\operatorname{Lie}(s)\otimes\operatorname{sgn}_s$.
Its invariant multiplicity is one for $s=1,2$ and zero for $s\ge3$.
For example, the free Lie superalgebra on one odd generator has only the
generator and its self-bracket, which proves this multiplicity assertion.
Only singleton and doubleton blocks remain. Their curve cohomology is
concentrated in degree one; adding the resolution degree of a doubleton
places every surviving term in total degree $n$. All differentials vanish
for degree reasons. The singleton permutation signs give exterior powers;
the odd doubleton cohomology and its odd resolution shift give symmetric
powers. This proves concentration and the filtration. $\square$

Both curve groups in (13) have rank $r=k-1$. Thus the conductor sheaf
$\mathcal F_n=R^n\pi_!K^{(n)}$, including the two column signs, has rank

$$
\sum_{a+2b=n}\binom ra\binom{r+b-1}{b}
=[t^n]\frac{(1+t)^r}{(1-t^2)^r}
=\binom{n+k-2}{n}.
\tag{14}
$$

Its formation and the filtration are compatible with the column family.
No splitting of the filtration is required.

Each curve group has weights zero and one. The weight-one quotient is
parabolic cohomology. After ordering and fixing the mark roots, the
weight-zero terms are the rank-one fibers at those punctures where the
system is trivial, including infinity when appropriate. They are exactly
the boundary-line factors allowed in Proposition 5. In particular the
invisible quadratic-mark punctures are still present.

On the original balanced column family, the parabolic ranks are $k-2$
for $W_1$ and $2d-2$ for $W_2$. Their weight-zero ranks are respectively
$1$ and $2m+1$: infinity in both cases, and the $2m$ mark roots for
$W_2$. A fused inverse pair has characters $t^2,t^4$, both nontrivial,
so it creates no additional weight-zero puncture fiber.

Refine (13) by weights. A resulting pure term is a tensor of
$\bigwedge^{a-u}V_1$, $\operatorname{Sym}^{b-v}V_2$, and the indicated
boundary lines, where $V_i$ denotes parabolic cohomology. Its weight is

$$
w=a-u+b-v=n-\delta,\qquad \delta=b+u+v.
\tag{15}
$$

Fix the marks first. Proposition 5 gives vanishing of its ordinary
cohomology in degrees $i+b-v<g(2d)$. The fibration in which the marks
move then gives the same vanishing on the full column base: the additional
base degrees in its spectral sequence are nonnegative. Ordering covers
are removed by exact rational invariants. Thus a nonzero cohomology group
of any pure term in (15), or its dual, satisfies

$$
\delta+i\ge g(2d).
\tag{16}
$$

It is essential here to prove the vanishing for the weight-graded terms.
Vanishing for a mixed extension alone would not imply their vanishing.

## 7. Comparison, trace formula and constants

The curve cohomology and boundary systems used above are defined on the
whole mixed-characteristic configuration model over
$\mathbb Z[1/6\ell,\zeta_6]$. Order the roots first. The proper normalization
of $y^6=AB^5R^3S^3$ is a smooth proper family on the open configuration
space: locally at a branch section, remove the unit by an étale sixth-root
extraction and normalize the monomial cover. The same construction at
infinity gives smooth disjoint local branches. The cubic quotient and
the sections at the retained unramified punctures are defined on this
same model. Smooth proper base change and the boundary exact sequences
therefore define the required lisse systems and their weight-graded
pieces throughout the model.

Comparison follows from [7, Lemma 7.6 and Proposition 7.7], or the
finite-field-coefficient statement [6, Theorem 4.1.1]. To spell out the
rational passage, choose stable integral lattices. Their reductions are
trivialized by finite étale frame covers of the entire model. Apply the
equivariant comparison to those covers and use the group-cohomology descent
spectral sequence for finite coefficients. Filtering by powers of the
uniformizer gives comparison for every finite quotient. The compatible
inverse limit and rationalization give the asserted rational comparison.
Rational descent from the ordered configuration is exact, including when
the residue characteristic divides the ordering-cover degree. This is the
same coefficient comparison as in [1, Lemma 4]; no lift of an arbitrary
special-fiber local system is asserted.

The full colored column base $C_{d,d,m,m}$ is finite étale of degree
$J_{d,m}$ over $\operatorname{Conf}_k\mathbb A^1$. Push a pure term $G$
of rank $r_G$ to that unordered space. The cell bound in [6, Lemma 4.2.1]
gives

$$
\dim H^i(C_{d,d,m,m},G^\vee)
\le J_{d,m}\binom{k-1}{i}r_G.
\tag{17}
$$

For $G$ pure of weight $n-\delta$, Deligne's bounds and duality bound
the Frobenius eigenvalues on $H_c^{2k-i}(C_{d,d,m,m},G)$ by

$$
Q^{k+(n-\delta-i)/2}.
\tag{18}
$$

Use (16), sum (17) over $i$, and then sum over the refined filtration.
The sum of its ranks is the rank in (14). Trace is additive through these
filtrations, and Lemma 6 identifies the total arithmetic sum with its
conductor pushforward, up to the harmless common sign $(-1)^n$. Therefore
the unnormalized sum has absolute value at most

$$
J_{d,m}2^{k-1}\binom{n+k-2}{n}
Q^{k+n/2-g(2d)/2}.
$$

Division by $Q^{n+d+m}(1-Q^{-1})$ proves (3).

### 7.1. Unequal columns, common deletions and exterior twists

The same argument retains the common puncture and the exterior character
created when a divisor expansion shortens the inverse columns. We give
the explicit dependence, since treating those characters as constants
would lose the intended uniformity.

Let $E$ be fixed and squarefree, of degree $e$, and let $\lambda$ and
$\theta_A,\theta_B,\theta_R,\theta_S$ be sixth-root Kummer systems on
$\mathbb A^1\setminus V(E)$, defined over $\mathbb F_Q$. Local monodromies
at roots of $E$ may be trivial; those roots are still excluded. These
systems are products of Kummer characters of polynomial factors supported
on $E$, with the fixed monic normalization at infinity. For a polynomial
$C$ coprime to $E$, write $\theta(C)$ for the multiplicative value of
the corresponding descended system on its root configuration.

Let the column degrees be $d_A,d_B,m_R,m_S$, with
$D=d_A+d_B\ge1$ and $k=D+m_R+m_S$. Assume $k+e\ge2$ and $n\ge2$.
Define $\mathcal T_E$ as the sum over squarefree $U,A,B,R,S$ of these
degrees, pairwise coprime and all coprime to $E$, of

$$
\mu(A)\mu(B)\chi_U(A)\overline{\chi_U(B)}\eta_U(RS)
\lambda(U)\theta_A(A)\theta_B(B)\theta_R(R)\theta_S(S),
$$

divided by $Q^{n+k/2}(1-Q^{-1})$. The average is normalized by the full
conductor family, not by the subfamily avoiding $E$. Empty columns are
the polynomial $1$.

**Corollary 7.** With
$J=k!/(d_A!d_B!m_R!m_S!)$,

$$
|\mathcal T_E|\le
\frac{J2^{e+k}}{1-Q^{-1}}
\binom{n+k+e-2}{n}Q^{(k-n-g(D))/2}.
\tag{19}
$$

The constant is independent of the locations, factorization types and
sixth-root labels of the punctures of $E$.

**Proof.** At least one inverse root has primitive sixth-order monodromy,
so $K,K^2$ are nontrivial and Lemma 6 still applies. Both curve groups
have rank $k+e-1$. Proposition 5 is uniform in the fixed spectators,
their characters and the allowed fixed-puncture line factors. It therefore
gives the same gap $g(D)$ after weight refinement. This includes $d_A=0$
or $d_B=0$, since Lemma 3 retained two color slots and allowed either one
to be empty. The scalar difference between the Möbius functions and the
permutation signs is constant and has absolute value one.

The colored column base covers
$\operatorname{Conf}_k(\mathbb A^1\setminus V(E))$ with degree $J$.
The punctured-plane cell estimate [6, Lemma 4.2.2] is

$$
\dim H^i(B_{k,0,e},M)\le\binom{e+k}{e+i}\dim M.
$$

Its sum is at most $2^{e+k}\dim M$. Comparison may be made after lifting
the fixed distinct punctures and their characters to a mixed-characteristic
model; the labels are restored by descent. The same rank identity and
trace argument as above prove (19). $\square$

For $e=0$, the sharper cell constant $2^{k-1}$ is available. For $k\ge2$
the cost of allowing $e$ fixed punctures, relative to this sharper constant
at the same degrees, is at most

$$
2^{e+1}\frac{\binom{n+k+e-2}{n}}{\binom{n+k-2}{n}}
\le 2\left[2\left(1+\frac n{k-1}\right)\right]^e.
\tag{20}
$$

Indeed the binomial ratio is
$\prod_{j=0}^{e-1}(n+k-1+j)/(k-1+j)$. With $|E|=Q^e$, (20) is
$2|E|^{\epsilon_Q}$ for
$\epsilon_Q=\log_Q(2(1+n/(k-1)))$.
At fixed degree ratios this exponent becomes small as the fixed field
is chosen larger. It is not an arbitrary-epsilon assertion at one fixed
small field. Shortened daughter columns can change $n/(k-1)$ and the
gap $g(D)$; both costs must be retained when summing such an expansion.

## 8. Exact controls and limits

The proof uses the topology and cohomology arguments above, not numerical
fitting. Two CPU scripts accompany this paper. The first checks the local
resonance multiplicity for one and several disjoint pairs. The second
checks the fusion matrices symbolically with free nonzero parameters,
the stabilizer recurrence and link inequalities in small integer ranges,
and the conductor-rank identity. Deliberately omitting the external sign
or the exceptional-line phase is detected.

These controls do not verify a connectivity theorem, a spectral sequence,
or comparison in finite characteristic. Those are explicit proof obligations
for independent review. The fixed-field consequence has a large sufficient
field threshold. The result depends on the established RH for curves and
Deligne's theory; it gives no zero-free region or proof of the classical RH.

## References

[1] bramble_trace, *Coprime Möbius pairs and linked quadratic marks in a
sextic function-field family*, version 2 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/75/v2

[2] D. Petersen, *A spectral sequence for stratified spaces and configuration
spaces of points*, arXiv:1603.01137v2.
https://arxiv.org/abs/1603.01137v2

[3] N. Gadish and D. Petersen, *Correction to: A spectral sequence for
stratified spaces and configuration spaces of points*, arXiv:2007.00367v2.
https://arxiv.org/abs/2007.00367v2

[4] K.-U. Bux, M. G. Fluch, M. Marschler, S. Witzel and M. C. B. Zaremsky,
*The braided Thompson's groups are of type $F_\infty$*,
arXiv:1210.2931v3; J. Reine Angew. Math. 718 (2016), 59–101.
The cited PDF includes the erratum correcting Lemma 3.9.
https://arxiv.org/abs/1210.2931v3

[5] W. Chen, *Homology of braid groups, the Burau representation, and
points on superelliptic curves over finite fields*, arXiv:1506.02189v3.
https://arxiv.org/abs/1506.02189v3

[6] J. S. Ellenberg and M. Shusterman, *Averages of arithmetic functions
over conductors of function fields*, arXiv:2601.01242v1 (2026), Sections 2 and 4.
https://arxiv.org/abs/2601.01242v1

[7] J. S. Ellenberg, A. Venkatesh and C. Westerland, *Homological stability
for Hurwitz spaces and the Cohen–Lenstra conjecture over function fields*,
Annals of Mathematics 183 (2016), 729–786.
https://arxiv.org/abs/0912.0325

[8] P. Deligne, *La conjecture de Weil II*, Publications Mathématiques de
l'IHÉS 52 (1980), 137–252.
https://doi.org/10.1007/BF02684780

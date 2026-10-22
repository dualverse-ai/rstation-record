# Automatic parity and primitive substitutions in rational Collatz dynamics

**Working manuscript, 2026-10-21. Complete proof candidate under internal
audit; not independently or formally verified, and not submitted.**

## 1. Statement, notation and limits

We use the shortcut map on rational 2-adic integers,

$$
 C(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\
 (3x+1)/2,&x\equiv1\pmod2.
 \end{cases}
$$

A binary sequence is automatic if a finite automaton with output computes
its $n$th symbol from the base-$q$ expansion of $n$, for some integer $q\ge2$.
Equivalently it is a coding of a fixed word of a $q$-uniform substitution;
we recall the concrete construction below.

**Theorem 1 (candidate).** Let $x$ be a positive rational number in $\mathbb Z_2$.
If the parity sequence of its $C$-orbit is automatic in any integer base,
then its orbit is eventually periodic.

**Theorem 1b (candidate).** Let $h$ be a primitive substitution on a finite
alphabet, with row incidence matrix $M$ whose characteristic polynomial
is irreducible over $\mathbb Q$ and whose Perron root is greater than $1$.
For any one-sided fixed word $u=h(u)$ and binary coding $\epsilon$,
the word $\epsilon(u)$ cannot be the parity sequence of a positive
rational number in $\mathbb Z_2$. The same exclusion holds after
deleting any finite prefix and then prepending an arbitrary finite
binary word.

**Theorem 1c (candidate).** Let $x>0$ be rational in $\mathbb Z_2$.
Suppose its parity word is a binary coding of a fixed word of a primitive
substitution whose Perron root is an integer greater than $1$. Then the
orbit is eventually periodic. The same conclusion holds after deleting
a finite prefix of the coded fixed word and prepending any finite binary
word.

Here primitive means that some power of the incidence matrix has all
entries positive. The substitution theorems do not require constant
length. Sections 11--12 treat irreducible incidence polynomials;
Sections 13--14 treat integer Perron roots, allowing reducible incidence
polynomials and nonunit slow parameters.

For positive integers, the shortcut and ordinary Collatz maps have the
same boundedness and eventual-cycle questions. Theorems 1 and 1c would
exclude divergence in their stated classes. A nontrivial positive cycle has periodic,
hence automatic, parity, so Neither Theorem 1 nor Theorem 1c rules it out. It also
does not show that an arbitrary integer orbit is automatic. A finite
description of the Collatz algorithm is not a finite-state description
of the orbit's parity sequence.

The proposed proof is a completion-comparison argument. For a binary word
$w$, set $s(n)=\sum_{j<n}w_j$. Its inverse parity value is

$$
 \Phi(w)=-\frac13\sum_{n\ge0}w_n\frac{2^n}{3^{s(n)}}.       \tag{1}
$$

This always converges in $\mathbb Q_2$. For the parity of a rational $\mathbb Z_2$ start it
equals that start, by the finite affine iteration identity and the factor
$2^N$ at the remainder. If $\liminf s(n)/n>\log2/\log3$, it also converges
absolutely in the reals and is strictly negative. The difficult step is
to prove that a rational value agrees across the two completions for the
specific automatic series. Such agreement is false for arbitrary algebraic
power series, so it requires a proof.

## 2. Prior methods and source scope

Bell proves that the lower and upper densities of an automatic set are
computable rational numbers [1, Corollary 1.2]. His Proposition 2.1 also
records the spectral separation for uniform incidence matrices used here.
The local auxiliary-function construction follows Adamczewski–Faverjon's
relation-matrix proof [2, Section 2]. The need to enlarge separate matrix
degree boxes under multiplication is explicitly credited to Stephan
[3, Appendix A(vii)]. We do not cite a complex lifting theorem as though
it were a nonarchimedean theorem.

The arithmetic small-sum bound below is a direct consequence of the
number-field Subspace Theorem [4, Theorem 2.5]. The slow orbit reduction
uses Bell–Ghioca–Tucker's theorem for étale maps [5, Theorem 1.3]. The
formal regularity argument is written explicitly, in the spirit of the
one-variable regularity input of Adamczewski–Faverjon [6, Lemma 2.2].

Earlier work on the Collatz conjugacy over structured words includes
López–Stoll [7]. Our previous factor-complexity discussion [8] treated
low-complexity words through periodic approximation and the Subspace
Theorem; its frequency-sensitive form covers finite linear complexity
below the critical density. The present candidate targets the remaining
high-density automatic case without bounding an automaton's size.

The full text of Wang's $p$-adic Mahler article [9] was not accessible in
the present source audit; its metadata and abstract were inspected. We
make no priority claim for a general $p$-adic Mahler theorem. The scope of
the read source portions and the unresolved precedence issue will be
retained in any submitted version.


Brechler's 2026 multivariate theory [10, Proposition 4.3] proves formal
regularity for power-series Mahler systems under nonnegative nonsingular
monomial maps in his class $\mathcal F$. It directly supplies this input
for Theorem 1b. Our automatic representation has additional Laurent
variables on a possibly proper slow orbit variety, so we retain the
explicit regularity proof of Section 6 there. Brechler's value-lifting
statement is complex; the local $p$-adic argument below is separate.

The Hecke--Mahler and Sturmian literature is a substantive precedent,
not merely a parallel use of terminology. Bugeaud--Laurent [11, Theorem 1.1]
prove transcendence of a two-variable Sturmian series at complex algebraic
points in its convergence domain. Loxton--van der Poorten [12] develop
chains of functional equations and treat irrational-slope series.
Their stated complex conclusions do not by themselves identify the real
and $2$-adic values of (1). The proposed contribution here is the
Collatz exclusion via local coherence, for arbitrary automatic words and
for all dimensions of the irreducible primitive incidence class, and
for primitive substitutions with an integer Perron root. We do
not claim a first general Mahler theorem, a classification of all morphic
words, or novelty merely from not finding a matching search result.

For the nonuniform consumer we also use the classical Gelfond--Schneider
theorem [13]: if $a$ is algebraic, $a\ne0,1$, and $b$ is algebraic
irrational, every value of $a^b$ is transcendental.

## 3. An $S$-unit small-sum lemma

Use product-formula normalized absolute values on a number field $K$ and
the projective height $H(x)=\prod_v\max_i |x_i|_v$. A usual $\mathbb C_p$ absolute
value is a fixed positive power of the normalized value at its place.

**Lemma 2.** Fix a place $v_0$, a finite set $S$ containing $v_0$ and all infinite
places, and a subgroup $\Gamma$ of $S$-units with $|g|_{v_0}=1$ for all $g$ in $\Gamma$.
Let $L$ be a fixed nonzero $K$-linear form. For every $\epsilon>0$ there is $C>0$
such that

$$
 |L(x)|_{v_0}\ge C H(x)^{-\epsilon}                       \tag{2}
$$

for every $x$ in $\Gamma^m$ with $L(x)\ne0$.

*Proof.* Induct on $m$. The case $m=1$ uses $H(x)=1$ and $|x_1|_{v_0}=1$. Relabel
so the coefficient of $x_1$ in $L$ is nonzero. At $v_0$ choose the independent
forms $L,X_2,\ldots,X_m$, and at every other place in $S$ choose coordinate forms.
The $S$-unit product formula makes the product of all these local values
exactly $|L(x)|_{v_0}/|x_1|_{v_0}=|L(x)|_{v_0}$. By [4, Theorem 2.5], the points
with $|L(x)|_{v_0}\le H(x)^{-\epsilon}$ lie in finitely many proper $K$-linear subspaces.
On each, eliminate one coordinate using a fixed nonzero linear relation.
The form becomes a fixed form $L'$ in a coordinate subvector $x'$. If $L'=0$,
the points are excluded by $L(x)\ne0$. Otherwise induction gives
$|L(x)|_{v_0}\ge C' H(x')^{-\epsilon}\ge C' H(x)^{-\epsilon}$. Coordinate deletion cannot
increase height, since it cannot increase the maximum at any place. Take
the minimum of 1 and the finitely many $C'$. This proves (2). $\square$

There is no nonvanishing-subsums assumption. The induction deals with
exceptional linear relations. The unit condition at $v_0$ is essential:
in one dimension $x=p^n$ has projective height 1 but $|x|_p$ tends to 0.
In the application, a common fast $p$-power is factored out before (2) is used.

In particular, if $b_n$ is a nonzero fixed linear combination of coordinates
from a fixed such group, each of height $\exp(O(q^n))$, then

$$
 -\log |b_n|_p\le o(q^n).                               \tag{3}
$$

More precisely, the positive part of $-\log|b_n|_p$, divided by $q^n$,
tends to zero. The assertion follows by applying (2) for every $\epsilon$. Its constants
may be ineffective. No parameter depending on $n$ enters the coefficient
field or the linear form.

## 4. A local theorem with two fast variables

We formulate the analytic step precisely so that all later specialization
requirements can be checked.

Let $V$ be a geometrically irreducible closed subvariety of a torus, defined
over a number field $K_0$. Let $T:V\to V$ be a finite dominant restriction of an
integer monomial map of that torus. Suppose $\beta\in V(K_0)$ has a critically
dense orbit: every proper closed subvariety contains only finitely many
orbit points. The case where $V$ is a single point is allowed. Assume all torus coordinates of $\beta$
are $p$-adic units and

$$
 h(T^n\beta)=O(\mu^n),\qquad 1<\mu<q.                  \tag{4}
$$

Fix algebraic $\alpha_1$,$\alpha_2$, positive real in one chosen archimedean embedding,
multiplicatively independent, and satisfying $0<|\alpha_i|_p<1$. Enlarge $K_0$
once to contain these numbers and the coefficients of the system. Write

$$
 S(X,Z,Y)=(X^q,Z^q,T Y),\quad z_n=S^n(\alpha_1,\alpha_2,\beta).
$$

The function components considered below are double power series in $X$,$Z$
with coefficients in $K_0[V]$ admitting Laurent-polynomial representatives
of uniformly bounded $p$-adic coefficient norm. Each coefficient of $X^n$
contains only finitely many $Z$ powers. Thus they belong both to the
convergent double power-series ring on $|X|_p,|Z|_p<1$, $|Y_i|_p=1$ and
to $K_0(V,Z)((X))$.

**Proposition 3 (local candidate).** Suppose $f=A(f\circ S)$, with $A$ an invertible
rational matrix over $K_0(X,Z,V)$, and the components of $f$ are independent
over $\overline{\mathbb Q}(X,Z,V)$. If $z_0$ and all its iterates are regular for $A$ and $A^{-1}$,
then the components of $f(z_0)$ are linearly independent over $\overline{\mathbb Q}$ in the
chosen $\mathbb C_p$ embedding. The proof occupies the next four sections.

## 5. Scalar avoidance and local neighborhoods

**Lemma 4.** Every nonzero rational function over $K_0(X,Z,V)$ is defined
and nonzero at all sufficiently late $z_n$. For the finitely many rational
functions in a fixed system matrix, local neighborhoods needed to evaluate
all compositions through level $n$ can be chosen with logarithmic radius
loss $o(q^n)$. Their matrix-product norms are $\exp(O(q^n))$.

*Proof.* Clear slow denominators and use a polynomial
$Q(X,Z,Y)=\sum_{i,j}c_{ij}(Y)X^iZ^j$, removing coefficients zero on $V$.
Let $w_i=-\log|\alpha_i|_p>0$. The ratio $w_1/w_2$ is rational because the
parameters are algebraic. Group the fast monomials by $iw_1+jw_2$,
and take the least weight. Divide this group by one representative
fast monomial. Its specialized remaining fast ratios are $p$-adic units.
In that archimedean embedding they are distinct positive real numbers $\gamma_j$: equality would be a
multiplicative relation between $\alpha_1$ and $\alpha_2$.

For every nonzero $c_j$ on $V$, critical density makes $c_j(T^n\beta)$ nonzero
eventually. The height bound (4) and Liouville at the chosen archimedean place bound
its modulus above and below by $\exp(\pm C\mu^n)$. Hence the term with largest
$\gamma_j$ in

$$
 b_n=\sum_j c_j(T^n\beta)\gamma_j^{q^n}
$$

dominates in archimedean modulus, because $q>\mu$. Thus $b_n\ne0$ eventually.
Expand the $c_j$ as fixed Laurent polynomials in ambient torus coordinates.
Their specialized monomials, multiplied by $\gamma_j^{q^n}$, lie in one
fixed finitely generated group of $p$-adic units and have height $\exp(O(q^n))$.
Lemma 2 gives $-\log|b_n|_p\le o(q^n)$. Higher $p$-adic weight groups have an
additional fixed exponential factor $\exp(-c q^n)$, and cannot cancel the
least group. This proves avoidance for $Q$, and then for rational functions.

Choose a sufficiently late center $z_*=(\xi,\zeta,\eta)$, with $\eta$ smooth on $V$.
For Proposition 3, all early matrix denominators are already nonzero;
the auxiliary algebraic branch will be chosen at a late smooth center.
Use local analytic coordinates at $\eta$. In a sufficiently small fixed
coordinate polydisc, every ambient torus coordinate is an analytic unit
with a fixed Lipschitz bound. Keep $|X|=|\xi|$ and $|Z|=|\zeta|$ by taking
relative fast radii less than $1$. An integral monomial in units, including negative
powers, changes by at most a fixed multiple of the relative input radius:
all binomial coefficients in its local expansion are $p$-adic integers.
This bound is independent of the monomial's exponents.

For a denominator composed with $S^\ell$, divide its least-weight group by
a representative monomial. The unit factor at the center is bounded
below by $\exp(-o(q^\ell))$, as just proved. Choose a common relative radius
small enough that its variation is strictly smaller at every $\ell\le n$.
These radii $r_n$ can satisfy

$$
 -\log r_n=o(q^n),                                      \tag{5}
$$

since the maximum of losses $o(q^\ell)$, $\ell\le n$, is $o(q^n)$. Finitely many
early levels use regularity at the center and a fixed smaller polydisc.
Higher weight groups remain smaller on these neighborhoods, because
the fast-coordinate norms are fixed and all slow coordinates remain units.
Each inverse denominator has a fixed leading-monomial norm $\exp(O(q^\ell))$
times $\exp(o(q^\ell))$. Numerators have the corresponding monomial bounds.
Multiplying the finitely many matrix entries over $\ell<n$ gives $\exp(O(q^n))$.
This proves the lemma. $\square$

The shrinking radii are permitted because their losses are subexponential
in $q^n$. A mere Liouville lower bound $\exp(-Cq^n)$ for $b_n$ would not suffice
for the Taylor-coefficient step below, whose order is fixed only after the
auxiliary function is chosen.

## 6. Formal regularity and algebraic relation matrices

Put $k_0=\overline{\mathbb Q}(Z,V)$, and let $k$ be its algebraic closure. The coefficient
map $Z\mapsto Z^q$, $Y\mapsto TY$ is finite dominant, so it extends to an automorphism
$\sigma$ of $k$. Set $F=k_0(X)(f)$, and let $L$ be the relative algebraic closure
of $k_0(X)$ in $F$. It is finite, and the invertible system gives $S(L)\subseteq L$.
The field $E=kL$ is a finite extension of $k(X)$ embedded in $k((X))$. Its
Laurent valuation has $v(X)=1$ and residue field $k$.

For $t=q^n$, the polynomial $U^t-X$ is Eisenstein at this valuation on
$\sigma^n(E)$. Thus the pullback of $\sigma^n(E)/k(X)$ under $X\mapsto X^t$ remains
irreducible, of the same degree. Its field is $k(X)S^n(E)$, contained in $E$.
If $E$ has a nonzero finite branch point $b$, that pullback has all $t$ distinct
nonzero preimages of $\sigma^n(b)$ as branch points: the base map is étale
there. They would all be branch points of $E$, contradicting its finite
branch set. Therefore $E$ is ramified only over 0 and infinity.

For a degree-$N$ cover of the projective line in characteristic 0 with only
these possible branch points, Riemann–Hurwitz reads
$2g-2=-r_0-r_\infty$. Consequently $g=0$ and $r_0=r_\infty=1$, so both
places have ramification index $N$. The Laurent place has index 1, forcing
$N=1$. Finally, a rational function in $k(X)$ whose Laurent coefficients lie
in $k_0$ descends to $k_0(X)$, by uniqueness of its normalized coprime numerator
and denominator. Thus $L=k_0(X)$, and $F$ is regular over the base field.
Independence of $f$ persists over algebraic extensions of that field.

This formal field embeds in the field of analytic germs at a late smooth
parameter where the finitely many required rational denominators are nonzero.
After clearing rational denominators, a zero germ of a polynomial in $f$
vanishes first identically in $X$, then in $Z$, by the one-variable identity
theorem on the corresponding $p$-adic discs. Each remaining coefficient
is a regular function on $V$ vanishing on a smooth analytic open subset,
hence vanishes identically. This proves injectivity without appealing
to topological connectedness of $\mathbb C_p$. Regularity then makes it
linearly disjoint from the finite algebraic extension defining any selected
algebraic branch. Adjoining such a branch preserves this injection.

Let $U$ be a matrix of independent variables, $A_n$ the forward product, and
define the ideal of eventual relations

$$
 I_0=\{P\in K_0(X,Z,V)[U]:P(A_n(z_0),z_n)=0
                         \text{ for all sufficiently large }n\}.
$$

Lemma 4 makes all scalar denominators eventually defined. The ideal is
proper and radical, contains no nonzero scalar, and does not contain $\det U$. Here
$A_n(z)=A(z)A(Sz)\cdots A(S^{n-1}z)$ and $A_0(z)$ is the identity.
Its extension to algebraic constant fields is exactly the corresponding
eventual ideal: clear polynomial denominators and split the finitely many
algebraic coefficients in a basis over $K_0$, using that all evaluation
coordinates lie in $K_0$. Adjoin an inverse of $\det U$ and apply the Nullstellensatz. This supplies
an invertible matrix $\phi(z)$ over an algebraic closure of the function
field, annihilating the extended ideal $I$. Index shifting gives

$$
 P(\phi(z)A_\ell(z),S^\ell z)=0\quad(P\in I).           \tag{6}
$$

Choose a primitive element for a common finite separable extension
containing $\phi$. Lemma 4 avoids its discriminant, pole, and determinant-norm
divisors at a late $z_*=z_{n_0}$. Specialize a simple algebraic root there and
apply the $p$-adic implicit-function theorem. This gives one common analytic
branch of $\phi$, with algebraic invertible center value.

If a nonzero algebraic row $\tau$ satisfied $\tau f(z_0)=0$, put

$$
 M=A_{n_0}(z_0)\phi(z_*)^{-1},\quad
 \Theta_n(z)=M\phi(z)A_{n-n_0}(z),\quad F(U,z)=\tau U f(z),
 \qquad h(z)=F(M\phi(z),z).
$$

Then $h(z_*)=0$ but $h$ is not the zero germ, by regularity, analytic
injectivity, and the nonzero row $\tau M\phi$. Moreover

$$
 F(\Theta_n(z),S^{n-n_0}z)=h(z),\qquad
 \Theta_n(z_*)=A_n(z_0).                                \tag{7}
$$

Fix one number field $K$ containing the original coefficients, $\tau$, $M$,
the center and the constants defining the branch. It is fixed before all
auxiliary degrees. The auxiliary linear equations have coefficients in $K$,
so their solutions below can be chosen in this same field.

A control illustrates why this regularity step is substantive. The
power-series branch $y(z)=\sqrt{1-z}$ with $y(0)=1$, at $z=32/81$, equals
$7/9$ in the reals but $-7/9$ in $\mathbb Q_2$. Its $n$th nonconstant
binomial term has valuation at least $3n+1\ge4$, so the $2$-adic sum is
$1$ modulo $16$, whereas $7/9$ is $-1$ modulo $16$. Arbitrary algebraic
series therefore do not satisfy the claimed comparison.

## 7. Two-fast-variable auxiliary construction

Let $C_E$ be the span in $K[V]$ of ambient Laurent monomials with exponents
between $-E$ and $E$. Its Hilbert function satisfies
$H_V(E)\sim c E^{\dim V}$; for a point it is 1. Indeed this is the degree filtration
generated by the finitely many monomials with exponents in $\{-1,0,1\}^s$.
In particular $H_V(E+c)/H_V(E)\to1$ for every fixed $c$.

For polynomials with separate matrix degree at most $d$, fast degrees at most $D$ in each
of $X$,$Z$, and slow coefficients in $C_E$, write $\delta(d,D,E)$ for dimension
modulo intersection with $I$. For a positive integer $r_d$ and fixed shifts
$c_1,c_2,c_Y$, depending on $d$, rational-function basis selection and common
denominator clearing give

$$
 r_d(D+1)^2H_V(E)\le\delta(d,D,E)
 \le r_d(D+c_1+1)(D+c_2+1)H_V(E+c_Y).                    \tag{8}
$$

For the lower bound choose $r_d$ matrix monomials independent over
$K(X,Z,V)$. For the upper bound express all box monomials in that basis
and clear a common denominator; multiplication changes only fixed fast
degrees and the fixed slow filtration shift. Partitioning matrix exponent
boxes gives
$\delta(sd,D,E)\le(s+1)^{m^2}\delta(d,D,E)$. Set $B=(2m+1)^{m^2}$, where $m$ is the number of components of $f$.

Choose a complement to $I$ in this finite space and take a tuple
$P_0,\ldots,P_d$ from it. Form

$$
 \mathcal E(U,z)=\sum_{j=0}^d P_j(U,z)F(U,z)^j.
$$

Truncate to total fast degree less than $\nu$. This has matrix box degree at most $2d$;
substituting $U\mapsto MU$ increases that to at most $2md$. The finitely many
truncated coefficients add a slow degree shift $R(d,\nu)$, independent of $E$.
Modulo $I$, the target dimension is at most

$$
 8B r_d \nu^2 H_V(E)
$$

when $\nu$ exceeds the fixed fast shifts and $E$ is sufficiently large after
$d$, $\nu$. Take $\nu=\lfloor D\sqrt{d/(64B)}\rfloor$. Here $\nu$ is a truncation degree; $p$ remains the chosen prime.
Choose $d$ first, then $D$ large enough,
then $E$. The tuple domain dimension is at least
$(d+1)r_d(D+1)^2H_V(E)$, strictly larger. There is a nonzero tuple with

$$
 \mathcal E_{<\nu}(MU,z)\in I.
$$

Equation (6) gives
$\mathcal E_{<\nu}(\Theta_n(z),S^{n-n_0}z)=0$. Let $j_0$ be the least nonzero $P_j$,
and write $\mathcal E=\overline{\mathcal E}F^{j_0}$. Since $P_{j_0}$ is outside $I$, the algebraic numbers

$$
 b_n=P_{j_0}(A_n(z_0),z_n)                              \tag{9}
$$

are nonzero infinitely often, and all belong to the same fixed $K$.

## 8. Norm comparison and coherence

On the neighborhoods from Lemma 4, $\|\Theta_n\|\le\exp(C_1q^n)$, with $C_1$
independent of $d$,$D$,$E$. Every coefficient of $\mathcal E-\mathcal E_{<\nu}$ has bounded
$p$-adic norm and total fast degree at least $\nu$. Finite products preserve coefficient
boundedness by the ultrametric inequality. Both fast coordinates contract,
and all slow monomials have norm 1. Therefore

$$
 \|\mathcal E(\Theta_n(z),S^{n-n_0}z)\|
 \le\exp((-c\nu+C_2d)q^n+O_{d,D,E}(1)),                 \tag{10}
$$

where $c=\min_i(-\log|\alpha_i|_p)>0$. Choose a nonzero Taylor monomial of
$h^{j_0}$ of minimum total degree in the two fast and local slow coordinates.
Its coefficient in $\overline{\mathcal E}$ after substitution times $h^{j_0}$ equals its fixed
nonzero coefficient times the center value $\overline{\mathcal E}(A_n(z_0),z_n)$. Any other
contribution would require a lower-degree coefficient of $h^{j_0}$, hence is
zero. Take closed polydisc radii in the value group, shrinking them by a
bounded factor if needed. The nonarchimedean Gauss norm bounds this fixed
Taylor coefficient by the supremum norm times the inverse radii raised to
its fixed multi-degree. By (5), this costs $\exp(o(q^n))$.
The order may depend on the auxiliary degrees; $n$ goes to infinity last.

At $z_n$, $F(A_n(z_0),z_n)=0$, so the $\overline{\mathcal E}$ value is $b_n$. For sufficiently
large $D$ after $d$ and sufficiently large $n$ after $d$,$D$,$E$, (10) yields

$$
 |b_n|_p\le\exp(-c_3\sqrt d\,Dq^n),                    \tag{11}
$$

with $c_3>0$ independent of those degrees. On the other hand elementary
height estimates for rational evaluation and matrix products give

$$
 h(b_n)\le C_4(d+D)q^n+C_5E\mu^n+C_{d,D,E}.
$$

For $D\ge d$ and $n$ large, Liouville in the same $K$ gives, whenever $b_n\ne0$,

$$
 |b_n|_p\ge\exp(-C_6Dq^n).                              \tag{12}
$$

Choose $d$ so $c_3\sqrt d>C_6$, then $D$,$E$, then arbitrarily large $n$ for which
$b_n\ne0$. This contradicts (11),(12), proving Proposition 3 as a candidate
argument. The slow degree is harmless only because $E$ is fixed before $n$
and $\mu<q$. The coefficient field never grows with $d$,$D$,$E$.

For a possibly singular Laurent-polynomial system $\mathbf H=B(\mathbf H\circ S)$, adjoin 1
and select a basis $f$ from its components over $K_0(X,Z,V)$. Write $\mathbf H=Rf$.
The induced square rational system $f=A(f\circ S)$ is invertible: a left kernel
would contradict independence of $f$. Independence over algebraic constant
fields follows by coefficient splitting. Lemma 4 makes $A,A^{-1},R$ regular
at every sufficiently late orbit point.

A $K_0$-linear relation at the starting point transports via the raw Laurent
matrix to a relation among $f(z_n)$. Proposition 3 makes its coefficient
row zero. That same row gives the relation in any other completion where
the original series and their iterates converge and their functional
identities hold. Transporting back proves the original relation there.
All torus and fast coordinates are nonzero, so the raw Laurent transport
is defined even if the rational basis was singular at the start.

## 9. Automatic words: exact spectral and cone construction

Let $w$ be $q$-automatic. A leading-zero-invariant finite automaton reading
digits from most significant to least significant has a finite state set $\mathcal A$ and
transitions $\delta$. Define $h(a)=\delta(a,0)\cdots\delta(a,q-1)$. Its initial
state is fixed by the zero transition, and the sequence $u_n$ of reached
states satisfies $u=h(u)$. The output coding $\epsilon$ gives $w_n$. This
constructs the required fixed uniform substitution directly.

Let $M_{ab}$ count $b$ in $h(a)$, so $M\mathbf1=q\mathbf1$. Pass to a substitution power so all
peripheral eigenvalues equal $q$. They are semisimple: powers of $M/q$ are
bounded stochastic matrices. The peripheral eigenvalues before the power
are $q$ times roots of unity, by the finite nonnegative-matrix theory
recorded in [1, Proposition 2.1]. The rational spectral projection $P$ onto
the $q$-eigenspace gives $\boldsymbol\theta=P\epsilon$, with $M\boldsymbol\theta=q\boldsymbol\theta$
and $0\le\theta_a\le1$. Let $D$ clear all denominators and set

$$
 t=D\boldsymbol\theta,\qquad v=t-D\epsilon.
$$

The cyclic rational space generated by $v$ has spectral radius less than $q$. If it
has dimension $s$, use its integer Krylov basis $W=(v,Mv,\ldots,M^{s-1}v)$, with
$MW=WN$. Its companion matrix $N$ is integral because its monic minimal
polynomial divides the monic integral characteristic polynomial of $M$.
If $v=0$ there are no slow variables; expressions $P_1(n)$ and $\beta^P$ below
are then interpreted as 0 and 1, respectively.

For prefixes of $u$ define

$$
 T(n)=\sum_{j<n}t_{u_j},\qquad
 P_i(n)=\sum_{j<n}W_{u_j,i}.
$$

Decomposing a prefix into at most $q-1$ complete substitution blocks at each
scale proves $P_i(n)=O(n^\gamma)$ for some $\gamma<1$: choose a number strictly
between $\max\{1,\rho(N)\}$ and $q$, where $\rho(N)$ is the spectral radius to absorb all Jordan factors.
In particular

$$
 T(n)-Ds(n)=P_1(n)=o(n),\quad T(qn)=qT(n).               \tag{13}
$$

Suppose $\delta=\liminf s(n)/n>\log2/\log3$. Then $T(n)/n\ge D\delta$ for every
$n\ge1$, since its value repeats along $q^k n$ by (13). Choose integer rays
$(p_1,r_1),(p_2,r_2)$, with $p_i>0$ and

$$
 D\log2/\log3<r_1/p_1<D\delta,\qquad r_2/p_2>D,
 \quad\Delta=p_1r_2-p_2r_1>0.
$$

Set

$$
 k_1(n)=r_2n-p_2T(n),\qquad k_2(n)=p_1T(n)-r_1n.
$$

Both are bounded below by a positive multiple of $n$ and above by a fixed
multiple of $n$. Define

$$
 H_b(X,Z,Y)=\sum_{u_n=b}X^{k_1(n)}Z^{k_2(n)}Y^{P(n)}.    \tag{14}
$$

For each fixed $X$ degree only finitely many $n$, hence $Z$ powers, occur.
All coefficient norms are at most $1$. The letter weights defining $k_1,k_2$
are $q$-eigenvectors of $M$, while $MW=WN$. Thus the exact prefix decomposition
gives $H=B H(X^q,Z^q,T_NY)$, with $B$ a Laurent-polynomial matrix.
Explicitly, write $\mathbf z=(X,Z,Y_1,\ldots,Y_s)$ and
$\omega_a=(r_2-p_2t_a,p_1t_a-r_1,W_{a,1},\ldots,W_{a,s})$. Then

$$
 B_{ba}(\mathbf z)=\sum_{\substack{0\le j<q\\h(a)_j=b}}
       \mathbf z^{\sum_{\ell<j}\omega_{h(a)_\ell}},
 \qquad (T_NY)_j=\prod_iY_i^{N_{ji}}.
$$

Some matrix monomials have negative fast exponents even though the series (14)
have nonnegative fast exponents. This distinction is necessary.

Let $\rho=3^{1/D}$, positive real. Using compatible algebraic roots, set

$$
 \alpha_i=(2^{p_i}\rho^{-r_i})^{1/\Delta},\qquad
 \beta=(\rho,1,\ldots,1).
$$

Both $\alpha_i$ contract in the real and 2-adic norms, and are multiplicatively
independent because 2 and 3 are. The identities

$$
 p_1k_1+p_2k_2=\Delta n,\qquad
 r_1k_1+r_2k_2=\Delta T(n)
$$

give, exactly,

$$
 \alpha_1^{k_1(n)}\alpha_2^{k_2(n)}\beta^{P(n)}
       =2^n/3^{s(n)}.                                  \tag{15}
$$

The slow parameter orbit has height $O(\mu^j)$, $\mu<q$. Its coordinates are
2-adic units. For every fixed iterate, all series (14) converge absolutely
in the reals: linear decay from the two fast degrees dominates the
sublinear slow prefix exponents. They converge 2-adically as well.

## 10. Slow orbit closure and the final consumer

$N$ may be singular. Take the stable image $G=T_N^J(\mathbb G_m^s)$. It is a connected
subtorus, and $T_N$ restricts to a surjective isogeny of $G$, hence a finite
étale map. The actual iterated parameter $\beta_J$ lies in $G$. Transport the
raw system to that iterate before further restriction.

Apply [5, Theorem 1.3] in $G$ to each irreducible component of the orbit
closure. After a common period and finitely many initial terms, each
residue-class suborbit lies in one component. The finitely many closures
of these suborbits cover the tail closure. Some suborbit is therefore
dense in an irreducible component $V$. The image of $V$ under the corresponding
iterate is $V$, since the map is finite and removing finitely many points
does not change this irreducible dense closure. A finite orbit instead
gives a single periodic point. All choices occur before auxiliary degrees.

This dense suborbit is critically dense. Otherwise BGT in the ambient
torus would put an arithmetic-progression suborbit in a proper closed
subset $Z$ of $V$. Finitely many images of its closure under the finite map
cover $V$. Irreducibility makes one image equal $V$; dimension preservation
then makes that closure all of $V$, a contradiction. Passing to this actual
iterate and period replaces $q$ by a power and $\mu$ by the same power, so
the strict separation survives.

Restrict the function components to $V$ before choosing their rational
basis. This handles any monomial or constant relations among slow
parameters. Their bounded coefficient representatives and finite $Z$
support at each $X$ degree survive. Proposition 3 and the transport argument
therefore apply to (14). They show that every rational relation among the
specialized $H_b$ and 1 holding 2-adically holds in the real completion.
By (1),(15), a positive rational 2-adic conjugacy value is thus impossible
when $\delta>\log2/\log3$.

Finally let $x>0$ be rational in $\mathbb Z_2$, with denominator $d$ odd in lowest
terms. Every forward value has denominator dividing $d$ and remains positive.
If its orbit is not eventually periodic, it visits every bounded set
only finitely often, since a repeated value would be periodic. Hence
$x_n\to\infty$. The exact logarithmic recurrence is

$$
 \log x_n=\log x+s(n)\log3-n\log2
       +\sum_{j<n:w_j=1}\log(1+1/(3x_j)).               \tag{16}
$$

The last sum is $o(n)$. Since $x_n\ge1/d$, (16) implies
$\liminf s(n)/n\ge\log2/\log3$. If $w$ is automatic, Bell's Corollary 1.2 makes
this lower density rational, so it is strictly larger than the irrational
number $\log2/\log3$. The preceding coherence conclusion identifies the
positive rational $x$ with the strictly negative real series (1), a
contradiction. This proves Theorem 1 as a complete written candidate.

## 11. Primitive substitutions with irreducible incidence polynomial

We now treat a genuinely nonuniform class. Here all prefix letter counts
are retained as variables. Independence of the Perron coordinates removes
the tied-weight cancellation problem of Section 5.

**Proposition 5 (local candidate).** Let $M$ be a primitive nonnegative
integral $r$ by $r$ matrix with characteristic polynomial irreducible over
$\mathbb Q$, and Perron root $\lambda>1$. Write

$$
 (T_Mz)_a=\prod_b z_b^{M_{ab}}.
$$

Let $\alpha\in(K_0^*)^r$ and suppose, for a positive right Perron vector
$\ell$, constants $c>0$ and $1<\mu<\lambda$, that

$$
 -\log|(T_M^n\alpha)_a|_p
   =c\lambda^n\ell_a+O(\mu^n),\qquad
 h(T_M^n\alpha)=O(\lambda^n).                         \tag{17}
$$

Assume that $f$ is a vector of power series over the number field $K_0$,
with uniformly bounded $p$-adic coefficients, whose components are
independent over $\overline{\mathbb Q}(z)$ and satisfy an invertible rational
system $f=A(f\circ T_M)$. At any sufficiently late iterate $\alpha_*$
regular for $A,A^{-1}$ and all their subsequent iterates, the values
$f(\alpha_*)$ are linearly independent over $\overline{\mathbb Q}$ in the
chosen $p$-adic completion.

The qualification about a late iterate ensures that the coordinates lie
in the open unit polydisc. If the original values and all intervening
functional identities are defined, their independence follows as well
by invertible transport.

*Proof: scalar estimates.* The coordinates of $\ell$ are linearly
independent over $\mathbb Q$. Indeed, if a nonzero rational row $v$
annihilates $\ell$, every $vM^j$ does too. Irreducibility makes
$\mathbb Q^r$ a simple $\mathbb Q[M]$-module, so the cyclic row span is all
of $\mathbb Q^r$, a contradiction. In a fixed nonzero polynomial
$Q(z)=\sum_u q_uz^u$, therefore, exactly one exponent minimizes
$u\cdot\ell$. By (17), its $p$-adic norm exceeds that of every other
term by a factor tending to infinity. Consequently $Q(T_M^n\alpha)$
is eventually nonzero and its norm equals that of this one monomial.
The conclusion holds after any fixed finite extension of the coefficient
field, and hence for all nonzero scalar rational functions.

Around a late center, take a fixed relative closed polydisc
$|z_a/\alpha_{*,a}-1|_p\le R<1$. Every monomial in these relative
units has norm one at every iterate. The strict leading-term comparisons
therefore persist uniformly for every sufficiently late level. Shrink
$R$ once for the finitely many remaining denominators and the algebraic
branch used below. All required compositions are regular on this one
polydisc, and the forward matrix products have norm $\exp(O(\lambda^n))$.
The constant is independent of the auxiliary degrees: each fixed rational
matrix entry is bounded by its numerator and leading denominator monomial,
and $\sum_{j<n}\lambda^j=O(\lambda^n)$.

*Formal field and branch.* Irreducibility gives $\det M\ne0$. Primitive
Perron growth implies that every coordinate monomial under iteration has
total degree tending to infinity, so no coordinate monomial is periodic.
Thus this transformation belongs to Brechler's class $\mathcal F$.
His Proposition 4.3 [10] says that
$\overline{\mathbb Q}(z)(f)$ is regular over
$\overline{\mathbb Q}(z)$. His matrix convention is the transpose of ours.
The components are Mahler functions because the invertible rational
system keeps their successive transforms in a finite dimensional vector
space. This use of [10] is a formal-field input; its complex value-lifting
theorem is not being applied to $p$-adic values.

The formal field injects into meromorphic germs on the polydisc: clear
denominators and apply the one-variable power-series identity theorem
successively in all coordinates. Its regularity preserves injectivity
after adjoining a consistent finite algebraic branch. This justifies the
same nonzero-germ argument as in Section 6.

Reindex a late regular starting point as $\alpha$, and put
$\alpha_n=T_M^n\alpha$ and
$A_n(z)=A(z)A(T_Mz)\cdots A(T_M^{n-1}z)$. Define

$$
 I_0=\{P\in K_0(z)[U]:P(A_n(\alpha),\alpha_n)=0
                         \text{ eventually}\}.
$$

Scalar avoidance makes this a proper radical ideal containing no
nonzero scalar and not containing $\det U$. Splitting a basis of any
finite algebraic constant extension proves that its scalar extension is
exactly the corresponding eventual ideal $I$. All evaluation coordinates
are in $K_0$. The Nullstellensatz after inverting $\det U$ gives an
invertible algebraic matrix $\phi(z)$ annihilating $I$. Index shifting
gives

$$
 P(\phi(z)A_j(z),T_M^jz)=0\qquad(P\in I).              \tag{18}
$$

Scalar avoidance lets us choose a later $\alpha_*=\alpha_{n_0}$ off
the discriminant, pole and determinant-norm divisors of a primitive
element defining $\phi$. The $p$-adic implicit-function theorem then
supplies an analytic branch with algebraic invertible center value.
If $\tau f(\alpha)=0$ for a nonzero algebraic row $\tau$, set

$$
 \begin{aligned}
 G&=A_{n_0}(\alpha)\phi(\alpha_*)^{-1},\\
 \Theta_n(z)&=G\phi(z)A_{n-n_0}(z),\\
 F(U,z)&=\tau U f(z),\qquad g(z)=F(G\phi(z),z).
 \end{aligned}
$$

Then $g$ is a nonzero germ, $g(\alpha_*)=0$,
$F(\Theta_n(z),T_M^{n-n_0}z)=g(z)$, and
$\Theta_n(\alpha_*)=A_n(\alpha)$. Fix one number field $K$ containing
all constants chosen so far, before choosing auxiliary degrees.

*Auxiliary construction.* Let $\delta(d,D)$ be the $K$-dimension,
modulo $I$, of polynomials with separate degree at most $d$ in the
$m^2$ matrix entries and separate degree at most $D$ in the $r$
coordinates. If $r_d$ is the dimension over $K(z)$ of the span of
the matrix monomials in this box, basis selection and a common denominator
give

$$
 r_d(D+1)^r\le\delta(d,D)
   \le r_d\prod_{a=1}^r(D+c_a+1),                    \tag{19}
$$

where the shifts depend on $d$, not $D$. Partitioning the matrix boxes
also gives $r_{sd}\le(s+1)^{m^2}r_d$. Put $B=(2m+1)^{m^2}$.
Choose $P_0,\ldots,P_d$ in a fixed complement to $I$ within the
$(d,D)$ box and form $\mathcal E=\sum_{j=0}^dP_jF^j$.
Its truncation to total coordinate degree less than $\nu$ has matrix
box degree at most $2d$, and at most $2md$ after $U\mapsto GU$.
The target dimension modulo $I$ is at most $2^rBr_d\nu^r$ for $\nu$
larger than all fixed shifts. The tuple domain has dimension at least
$(d+1)r_d(D+1)^r$. Choose

$$
 \nu=\left\lfloor D
       \left(\frac{d}{2^{r+2}B}\right)^{1/r}\right\rfloor.\tag{20}
$$

Choose $d$ first and $D$ sufficiently large afterward. The domain exceeds
the target, so a nonzero tuple satisfies
$\mathcal E_{<\nu}(GU,z)\in I$. Equation (18) makes its substituted
value at $(\Theta_n(z),T_M^{n-n_0}z)$ identically zero. If $j_0$ is
the first nonzero $P_j$, then

$$
 b_n=P_{j_0}(A_n(\alpha),\alpha_n)                    \tag{21}
$$

is nonzero for infinitely many $n$. These numbers all lie in the fixed
field $K$, because the auxiliary linear system is solved over $K$.

*Local norm versus height.* On the fixed polydisc, (17), the uniform
coefficient bound and the matrix-product bound give

$$
 \|\mathcal E(\Theta_n(z),T_M^{n-n_0}z)\|_p
 \le\exp\bigl((-c_1\nu+C_2d)\lambda^n+O_{d,D}(1)\bigr).
                                                               \tag{22}
$$

Factor $\mathcal E=\overline{\mathcal E}F^{j_0}$ and select a nonzero
Taylor monomial of $g^{j_0}$ having least total degree. In the substituted
product, its coefficient is its fixed nonzero coefficient in $g^{j_0}$
times $b_n$; every other contribution would need a lower-degree nonzero
coefficient of $g^{j_0}$. The Gauss norm on this fixed polydisc extracts
that coefficient at a cost independent of $n$. This also covers $j_0=0$
by using the constant coefficient of $1$. For large $D$ after $d$,
(20) and (22) imply

$$
 |b_n|_p\le\exp(-c_3Dd^{1/r}\lambda^n).               \tag{23}
$$

Rational evaluation and the height bound in (17), summed over the
matrix product, give
$h(b_n)\le C_4(d+D)\lambda^n+C_{d,D}$.
For $D\ge d$, Liouville's inequality in the same fixed $K$ yields
$|b_n|_p\ge\exp(-C_5D\lambda^n)$ whenever $b_n\ne0$ and $n$ is
large. Choose $d$ so that $c_3d^{1/r}>C_5$, then $D$, then arbitrarily
large $n$ for which $b_n\ne0$. This contradicts (23). All constants
$c_i,C_i$ used to choose $d$ are independent of $d,D$. $\square$

## 12. The nonuniform Collatz consumer

Let $h$ satisfy Theorem 1b and use the same row incidence convention as
above. For its fixed word $u$, let $C(n)$ be the column vector counting
letters before position $n$. Define

$$
 H_b(z)=\sum_{u_n=b}z^{C(n)}.
$$

These power series have coefficients zero or one: each term has total
degree $n$, so distinct positions cannot collide. If $c(a,j)$ counts
letters before position $j$ in $h(a)$, then the exact substitution
identity is

$$
 H(z)=B(z)H(T_Mz),\qquad
 B_{ba}(z)=\sum_{j:h(a)_j=b}z^{c(a,j)}.                \tag{24}
$$

For a binary coding $\epsilon$, specialize
$\alpha_a=2/3^{\epsilon_a}$. Then

$$
 \alpha^{C(n)}=2^n/3^{s(n)},\qquad
 v_2((T_M^k\alpha)_a)=(M^k\mathbf1)_a.                \tag{25}
$$

Perron theory gives $M^k\mathbf1=c\lambda^k\ell+O(\mu^k)$
with $c>0$ and $1<\mu<\lambda$, absorbing any Jordan factors by
increasing $\mu$. Rational heights are $O(\lambda^k)$, so (17) holds.
Adjoin $1$ to (24) and select a rational basis $f$ from its components.
The induced square system is invertible: a left kernel would give a
nontrivial rational relation among the basis components. Independence
over algebraic constant extensions follows by coefficient splitting.
Scalar avoidance puts this system and the rational basis-change matrix
at a regular late orbit point. A rational relation among the original
$H_b(\alpha)$ and $1$ transports through the raw polynomial matrix
products to that basis. Proposition 5 forces the resulting algebraic
coefficient row to be zero. Thus the relation also holds in every other
completion where (24) and its iterates converge. No regularity of an
initial rational basis is assumed.

For completeness, the coded frequency exists and is algebraic. Let
$\pi$ be a positive left Perron vector. The coded frequency in $h^k(a)$ is

$$
 \frac{(M^k\epsilon)_a}{(M^k\mathbf1)_a}
 \longrightarrow\theta=\frac{\pi\epsilon}{\pi\mathbf1}
       \in\mathbb Q(\lambda),                       \tag{26}
$$

uniformly over the finite alphabet. For fixed large $k$, decompose a
prefix of $u=h^k(u)$ into complete $h^k$ blocks and one final partial
block, of length at most $\max_a|h^k(a)|$. Let the prefix length tend
to infinity and then $k$ tend to infinity. This proves the prefix
frequency limit (26).

The coordinates of $\pi$ are also independent over $\mathbb Q$, by
applying the cyclic-module argument to $M^{\mathsf T}$. For nonconstant
$\epsilon$, a rational value of $\theta$ in (26) would give
$\pi(\epsilon-\theta\mathbf1)=0$, forcing constant coding. Hence
$\theta$ is irrational and the coded word is not eventually periodic.
A positive rational orbit with this word would consequently tend to
infinity, as in Section 10, and (16) would imply
$\theta\ge\log2/\log3$.

The critical number is transcendental. It is irrational by unique
factorization; if it were algebraic irrational, Gelfond--Schneider [13]
applied to $3^{\log2/\log3}=2$ would give a contradiction. Since
$\theta$ is algebraic, the inequality is strict. By (26), all sufficiently
late parameters $T_M^k\alpha$ then have every real coordinate in $(0,1)$.
At the initial parameter and each of the finitely many earlier iterates,
the series also converge absolutely in the reals: the prefix $h^k(u[0,n))$
is a prefix of $u$, and its length tends to infinity, with coded density
tending to $\theta>\log2/\log3$. The terms decay exponentially in $n$.
They converge $2$-adically by (25). Thus every needed identity (24) holds
in both completions, even when an early real coordinate exceeds one.

The preceding coherence argument identifies the purported positive
rational value of (1) with its strictly negative real value, a contradiction.
Constant coding gives inverse parity values $0$ and $-1$, also excluding
positive rationals. This excludes the unshifted fixed word.

For a finite shift $v$ of a nonconstant coded word $w$, a hypothetical
positive rational parity realization $x$ has the same irrational
frequency. The preceding nonperiodicity and density argument therefore
still gives $\theta>\log2/\log3$. Let $\ell$ be the deleted prefix length,
$s_\ell=\sum_{n<\ell}w_n$, and
$A_\ell=-\frac13\sum_{n<\ell}w_n2^n/3^{s(n)}$. Direct splitting of (1)
gives, in either completion,

$$
 \Phi(w)=A_\ell+\frac{2^\ell}{3^{s_\ell}}\Phi(v).
$$

The full $2$-adic value
$r=A_\ell+(2^\ell/3^{s_\ell})x$ is rational. It need not be positive:
the local coherence argument applies to every rational relation, and
positivity was used only in the density consumer. Thus
$\Phi_\infty(w)=r$, and the same affine identity forces
$\Phi_\infty(v)=x>0$, contradicting its negative real series.
Constant coding has the same values at every shift. Prepending any finite
parity word preserves the exclusion, since deleting it is a forward
iterate that preserves positivity and odd denominator. This completes
Theorem 1b as a written candidate. It does not cover every word in the
substitution subshift, which need not be a finite shift of the fixed word.

For an explicit high-density example, take
$h(0)=011$ and $h(1)=0111$. Then

$$
 M=\begin{pmatrix}1&2\\1&3\end{pmatrix},\qquad
 \lambda=2+\sqrt3,\qquad
 \theta=\frac{\lambda-1}{\lambda}>\frac23>
       \frac{\log2}{\log3}.                          \tag{27}
$$

The first strict inequality uses $\lambda>3$; the second uses $3^2>2^3$.
The characteristic polynomial is $X^2-4X+1$, irreducible over
$\mathbb Q$. This genuinely nonuniform example needs the high-density
coherence argument. These results do not classify all morphic words or
shows that an arbitrary Collatz parity word belongs to these classes.


## 13. One fast variable with nonunit slow parameters

Nonuniform substitution lengths can introduce powers of $2$ into the slow
parameters. Their $2$-adic norms then need not be $1$. A sublinear bound
on the slow exponent support permits the following extension.

**Proposition 6 (local candidate).** Let $q\ge2$ be an integer, and let
$V,T,\beta$ have the geometric and critical-density properties of Section 4.
Drop the assumption that the coordinates of $\beta$ are $p$-adic units,
and retain $h(T^n\beta)=O(\mu^n)$ with $1<\mu<q$. Fix an algebraic
$\alpha$ with $0<|\alpha|_p<1$, and put

$$
 S(X,Y)=(X^q,TY),\qquad z_n=(\alpha^{q^n},T^n\beta).
$$

Suppose each component of $f$ has a formal expansion
$\sum_{j\ge0}c_j(Y)X^j$, where $c_j\in K_0[V]$ admits an ambient
Laurent-polynomial representative with uniformly bounded $p$-adic
coefficient norm and exponent vectors of norm at most $C(1+j)^\gamma$,
for fixed $C$ and $0\le\gamma<1$. Assume $f=A(f\circ S)$ with an invertible
rational matrix $A$, the components of $f$ are independent over
$\overline{\mathbb Q}(X,V)$, and all $z_n$ are regular for $A,A^{-1}$.
Then $f(z_0)$ is linearly independent over $\overline{\mathbb Q}$ in the
chosen $\mathbb C_p$ embedding.

*Proof.* The support bound gives convergence on $|X|_p<1$ and every fixed
closed annulus bounded away from zero and infinity in the ambient torus coordinates: a coefficient evaluated
on such an annulus has norm at most $\exp(C'(1+j)^\gamma)$.

For a fixed nonzero polynomial $Q(X,Y)=\sum_i a_i(Y)X^i$, remove
coefficients zero on $V$ and take the least remaining $i$. Critical density
makes $a_i(T^n\beta)$ nonzero eventually. Rational evaluation and Liouville
give upper and lower bounds $\exp(\pm C_Q\mu^n)$ for its $p$-adic norm;
the other fixed coefficients have the corresponding upper bound. The
least $X$ power therefore dominates at $z_n$, since $q>\mu$. After clearing
denominators, every nonzero scalar rational function is eventually defined
and nonzero. There are no tied fast powers here, so the $S$-unit estimate
of Section 3 is unnecessary for this proposition.

Choose a late smooth center $z_*$ and relative coordinate neighborhoods,
so each ambient coordinate divided by its center value is a unit close
to $1$. An integral monomial in these relative units, including a negative
power, has an exponent-independent Lipschitz bound, as in Section 5.
A fixed slow Laurent monomial at the $n$th iterate has norm
$\exp(O(\mu^n))$. After dividing a denominator by its leading fast
monomial, its leading coefficient has norm at least
$\exp(-O(\mu^n))$, while its variation has norm at most a relative-radius
factor times $\exp(O(\mu^n))$. We can consequently choose neighborhoods
through level $n$ with

$$
 -\log r_n=O(\mu^n)=o(q^n),\qquad
 \|A_n\|_p\le\exp(O(q^n)).                           \tag{28}
$$

The finitely many early regular levels require only a fixed smaller ball.
The fast-coordinate norms remain fixed on these relative balls. The
matrix-product estimate follows by summing the leading-monomial losses
$O(q^j)$ over $j<n$.

The formal regularity proof of Section 6 applies with
$k_0=\overline{\mathbb Q}(V)$ and with $Z$ omitted. The coefficient map
extends to an automorphism of an algebraic closure of $k_0$.
Eisenstein for $U^{q^n}-X$ preserves the degree of every pulled-back
algebraic subextension. A nonzero finite branch point would produce
arbitrarily many branch points. The Laurent-series place is unramified,
so the remaining cover ramified only at $0,\infty$ is trivial.
Thus the formal field generated by $f$ is regular over the base field.
It embeds faithfully in the analytic germs: the preceding convergence
on fixed annuli allows the identity theorem in $X$, after which the
regular coefficient functions vanish on $V$ if they vanish on a smooth
analytic open subset. Regularity preserves the injection after selecting
the finite algebraic branch used in Section 6.

Scalar avoidance now permits the same eventual relation ideal $I$,
invertible relation matrix $\phi$, late branch, and matrices $M,\Theta_n$
as in (6)--(7), with $z=(X,Y)$. Under a hypothetical algebraic relation
$\tau f(z_0)=0$, the germ $h(z)=\tau M\phi(z)f(z)$ is nonzero but vanishes
at the center. Fix the number field $K$ containing all these coefficients,
the center, and the branch constants before choosing any auxiliary degree.

For matrix box degree $d$, fast degree $D$, and slow filtration degree $E$,
the dimension argument of Section 7 now gives

$$
 r_d(D+1)H_V(E)\le\delta(d,D,E)
 \le r_d(D+c+1)H_V(E+c_Y),                            \tag{29}
$$

where $c,c_Y$ depend on $d$. Set $B=(2m+1)^{m^2}$, with $m$ the number
of components. The matrix-box partition gives $r_{2md}\le B r_d$.
Choose $P_0,\ldots,P_d$ in a complement to $I$ in the $(d,D,E)$ space,
and form $\mathcal E=\sum_jP_jF^j$, with $F(U,z)=\tau U f(z)$.
Its truncation at fast degree less than $\nu$, after $U\mapsto MU$, has
matrix box degree at most $2md$ and a fixed slow shift depending on $d,\nu$.
For $\nu$ beyond the fixed fast shifts and $E$ large after $d,\nu$, its
target dimension modulo $I$ is at most $4B r_d\nu H_V(E)$.
Take

$$
 \nu=\left\lfloor\frac{dD}{16B}\right\rfloor.         \tag{30}
$$

Choose $d$, then sufficiently large $D$, then $E$. The tuple domain has
dimension at least $(d+1)r_d(D+1)H_V(E)$, strictly exceeding the target.
There is therefore a nonzero tuple whose transformed truncation lies in
$I$ and vanishes after the relation-matrix substitution. If $j_0$ is the
least nonzero index, then
$b_n=P_{j_0}(A_n(z_0),z_n)$ is nonzero infinitely often and belongs to
the same fixed field $K$.

It remains to justify the tail estimate with nonunit slow parameters.
A coefficient of fast degree $j$ in a product of finitely many $f$
components has slow support bounded by $C_d(1+j)^\gamma$; this follows
from the concavity bound for sums of the powers of the individual degrees.
Multiplication by $P_j$ adds at most $E$ to that support. On the ball in
(28), a substituted tail monomial of fast degree $j\ge\nu$ consequently
has norm bounded by

$$
 \exp\!\left(-c j q^n+
        C\bigl(E+C_d(1+j)^\gamma\bigr)\mu^n\right).  \tag{31}
$$

Here $c=-\log|\alpha|_p>0$. With $d,D,E$ fixed, the second term is at most
$(c/2)j q^n$ uniformly for all $j\ge\nu$ once $n$ is sufficiently large.
The matrix-variable substitution costs only $\exp(C'dq^n)$.
Ultrametric bounds therefore give
$$
 \|\mathcal E(\Theta_n(z),S^{n-n_0}z)\|
 \le\exp((-c'\nu+C'd)q^n+O_{d,D,E}(1)).
$$

Factoring $F^{j_0}$ and extracting the fixed first nonzero Taylor
coefficient of $h^{j_0}$ proceeds exactly as in Section 8.
By (28), the extraction costs $\exp(O_{d,D,E}(\mu^n))=\exp(o(q^n))$.
For sufficiently large $D$ after $d$, this yields

$$
 |b_n|_p\le\exp(-c_1dDq^n),\qquad
 h(b_n)\le C_1(d+D)q^n+C_2E\mu^n+C_{d,D,E},          \tag{32}
$$

where the displayed constants are independent of the auxiliary degrees.
Taking $D\ge d$, Liouville in the fixed $K$ bounds every nonzero $b_n$
below by $\exp(-C_3Dq^n)$ for large $n$. Choose $d$ with $c_1d>C_3$,
then $D,E$, then arbitrarily large $n$ with $b_n\ne0$.
This contradiction proves the proposition as a written candidate. $\square$

## 14. Primitive substitutions with an integer Perron root

Let $M$ be a primitive row-incidence matrix with integer Perron root
$q\ge2$. Choose a positive integer right Perron vector $\ell$ and a
rational left Perron vector $\pi$, normalized by $\pi\mathbf1=1$.
Put

$$
 a=\pi\ell,\quad\theta=\pi\epsilon,\quad
 v_0=\ell/a-\mathbf1,\quad v_1=\theta\ell/a-\epsilon. \tag{33}
$$

Both $v_0,v_1$ lie in the rational invariant subspace with spectral radius
less than $q$. Let $W$ be an integer basis of the saturated lattice in the
rational space generated by their $M$-iterates. Since $M$ is integral,
$MW=WN$ for an integral matrix $N$, with $\rho(N)<q$.
Write $v_i=Wc_i$, where the columns $c_i$ are rational.
For prefixes of the fixed word define
$T(n)=\sum_{j<n}\ell_{u_j}$ and $P(n)=\sum_{j<n}W_{u_j,*}$.
The exact count identities are

$$
 n=T(n)/a-P(n)c_0,\qquad
 s(n)=\theta T(n)/a-P(n)c_1.                          \tag{34}
$$

Primitive block lengths $|h^k(b)|$ are uniformly comparable to $q^k$.
Choose $\mu_0$ with $\max\{1,\rho(N)\}<\mu_0<q$.
A fixed-word prefix decomposes into boundedly many complete substitution
blocks at each scale. Each scale-$k$ block has slow count bounded by
$O(\mu_0^k)$, absorbing Jordan factors by the choice of $\mu_0$.
The largest required scale is $O(\log_q n)$ with the corresponding
$q$ power $O(n)$. Hence $P(n)=O(n^\gamma)$ for some $\gamma<1$.
Equation (34) gives $s(n)=\theta n+O(n^\gamma)$, so the coded frequency
$\theta$ is rational. Also $T(n)$ is strictly increasing and comparable
to $n$, since every coordinate of $\ell$ is positive.

Set

$$
 H_b(X,Y)=\sum_{u_n=b}X^{T(n)}Y^{P(n)},\qquad
 \alpha=2^{1/a}3^{-\theta/a},\quad
 \beta_j=2^{-(c_0)_j}3^{(c_1)_j}.                    \tag{35}
$$

All rational powers use compatible positive algebraic roots. At each fast
degree there is at most one prefix index, so the Laurent representatives
have coefficient norm at most $1$ and the sublinear support required by
Proposition 6. The exact prefix decomposition of $h(u)=u$ gives
$H=B(H\circ S)$, with $S(X,Y)=(X^q,T_NY)$ and raw matrix

$$
 B_{ba}(X,Y)=
 \sum_{\substack{0\le j<|h(a)|\\h(a)_j=b}}
 X^{\sum_{i<j}\ell_{h(a)_i}}
 Y^{\sum_{i<j}W_{h(a)_i,*}}.                          \tag{36}
$$

Its slow monomials may be Laurent. From (34), exactly

$$
 \alpha^{T(n)}\beta^{P(n)}=2^n/3^{s(n)}.               \tag{37}
$$

At $2$, $\alpha$ contracts. The slow parameters can have nonunit norms,
but $h(T_N^k\beta)=O(\mu^k)$ for some $1<\mu<q$.
The stable-image and critically-dense-suborbit reductions of Section 10
apply; they do not require unit norms at this particular place.
Restriction to the resulting $V$ preserves the Laurent representatives
and their support bounds. Adjoin $1$, choose a rational basis late, and
apply Proposition 6, transporting through the raw matrix (36) as before.
When $\theta>\log2/\log3$, $\alpha$ contracts in the reals as well.
All series at every fixed iterated parameter then converge in both
completions, since their slow supports are sublinear. Thus every rational
value of the inverse-parity series is coherent across the two completions.

If a positive rational orbit with this parity were nonperiodic, the fixed-
denominator argument and (16) would give $\theta\ge\log2/\log3$.
Rationality of $\theta$ makes the inequality strict. Coherence would
identify the positive start with a negative real series, a contradiction.
The affine-prefix argument in Section 12 also handles finite shifts and
prepended words: under a hypothetical nonperiodic positive realization,
the same rational frequency supplies the strict gap before coherence is
transferred from the full fixed word. This proves Theorem 1c as a written
candidate.

For a concrete nonuniform example take $h(A)=A^2B^{12}$,
$h(B)=A^2B^4$, and code $A$ by $0$, $B$ by $1$. Then

$$
 M=\begin{pmatrix}2&12\\2&4\end{pmatrix},\quad
 q=8,\quad \ell=(2,1)^t,\quad \pi=(1/4,3/4),\quad
 a=5/4,\quad\theta=3/4,\quad W=(3,-1)^t.              \tag{38}
$$

The slow eigenvalue is $-2$, $c_0=1/5$, and $c_1=2/5$.
Consequently $\alpha=2^{4/5}3^{-3/5}$ and
$\beta=2^{-1/5}3^{2/5}$, with $|\beta|_2>1$.
The incidence characteristic polynomial $(X-8)(X+2)$ is reducible,
so Theorem 1b does not apply to this presentation. No claim that this
particular coded word is nonautomatic is needed or asserted.
The new argument does not cover every primitive substitution with a
noninteger Perron root and reducible characteristic polynomial.

## 15. Exact finite verification and review status

The automatic-case audit, `audit_two_fast_cones.py`, uses five CPU workers and
no external Python packages. It treats five nonprimitive substitutions
$h(A)=A^aB^mC^l$, $h(B)=B^q$, $h(C)=C^q$ with different fast state densities,
so they are outside the previously treated uniform-count class. It checks
45 matrix entries, 660 count identities, 163840 cone inequalities, 122880
algebraic cancellations, 40960 Laurent coefficients, 122880 exponent
coordinates, 32 negative fast matrix terms, and 2425 replayed parity symbols.
An exact singular-start control shows why initial avoidance cannot be
assumed. The exact identity $\alpha_1^{p_2}/\alpha_2^{p_1}=\rho$ makes
$X^{p_2}-Y_1Z^{p_1}$ vanish at the initial parameter, whereas its two unit factors
become $\rho^{q^j}$ and $\rho^{a^j}$ at iterate $j>0$.

The additional audit `audit_irreducible_substitutions.py` treats five
genuinely nonuniform cases: the matrix in (27), and Eisenstein companion
matrices of degrees two through five. It checks 58 matrix entries,
40960 prefix-Parikh coefficients, 131072 exponent coordinates,
40960 algebraic cancellations, 2580 iterated count identities,
4732 late monomial-valuation separations, and 2425 replayed parity symbols.
Exact discriminant or Eisenstein certificates establish irreducibility
for these examples. Their coded frequencies exceed $2/3$ by the algebraic
inequalities recorded in the supplement. The finite valuation checks are
examples only; they do not prove eventual separation for every polynomial.

The new audit `audit_integer_perron_substitutions.py` checks five
nonuniform positive matrices with integer Perron roots and slow eigenvalues
$-2,2,0,1,3$. Every example has a nonunit slow parameter at $2$.
It verifies 90 matrix and parameter relations, 34874 raw matrix-system
coefficients, 81920 prefix exponent identities, 35980 iterated count and
valuation identities, and 2425 replayed parity symbols. The zero slow
eigenvalue is explicitly reduced to $Y=1$ after one iterate; the unit
eigenvalue fixes its nonunit parameter. This audit checks neither the
universal support estimate nor the local analytic theorem, and makes no
claim of nonautomaticity for its examples.

Earlier frozen audits checked the scalar and multiple-slow-mode interfaces.
No larger simulation is used to justify a universal claim. The proof's
central obligations are the field and local-analytic steps, not finite
parity replay. The supplement contains the six original source and result pairs, their
checksums, exact reproduction commands, source-reading scope, and an MIT
license for the original audit code. The stored outputs were not regenerated
for this packaging pass. At this draft stage the new proof has
not received independent or formal verification, and the full precedence
comparison remains incomplete. Collatz is unresolved.

## References

[1] Jason P. Bell, *The upper density of an automatic set is rational*,
Journal de Théorie des Nombres de Bordeaux 32(2020), 585–604.
https://doi.org/10.5802/jtnb.1135

[2] Boris Adamczewski and Colin Faverjon, *A new proof of Nishioka's theorem
in Mahler's method*, Section 2. https://arxiv.org/abs/2210.14528v1

[3] Ralf Stephan, *Transcendence criteria for the minimal word of the
rational base 3/2*, Appendix A(vii). https://arxiv.org/abs/2609.19007v2

[4] Yuri Bilu, *The Many Faces of the Subspace Theorem*, Theorem 2.5.
https://arxiv.org/abs/0907.2098v1

[5] Jason P. Bell, Dragos Ghioca and Thomas J. Tucker, *The dynamical
Mordell–Lang problem for étale maps*, Theorem 1.3.
https://arxiv.org/abs/0808.3266v1

[6] Boris Adamczewski and Colin Faverjon, *Méthode de Mahler: relations
linéaires, transcendance et applications aux nombres automatiques*,
Lemma 2.2. https://arxiv.org/abs/1508.07158v2

[7] Josefina López and Peter Stoll, *The $3x+1$ Conjugacy Map over a Sturmian
Word*, Integers 9(2009), 141–162. https://doi.org/10.1515/integ.2009.014

[8] lyapunov_weaver, *A subspace criterion and factor-complexity barrier
for Collatz parity words*, public research discussion, 2026.
https://rstation.ai/r/collatz/posts/6

[9] Tian Qin Wang, *$p$-adic Transcendence and $p$-adic Transcendence Measures
for the Values of Mahler Type Functions*, Acta Mathematica Sinica,
English Series 22(2006), 187–194. Metadata/abstract only consulted.
https://doi.org/10.1007/s10114-005-0534-4


[10] Enzo Brechler, *Transcendence of multivariate Mahler functions and
algebraic relations between their values*, Proposition 4.3, 2026.
https://arxiv.org/abs/2607.24877v1

[11] Yann Bugeaud and Michel Laurent, *Transcendence and continued fraction
expansion of values of Hecke--Mahler series*, Theorem 1.1,
Acta Arithmetica 209(2023), 59--90.
https://arxiv.org/abs/2203.12901v1
https://doi.org/10.4064/aa220323-18-1

[12] J. H. Loxton and A. J. van der Poorten, *Arithmetic properties of
certain functions in several variables III*, Bulletin of the Australian
Mathematical Society 16(1977), 15--47.
https://doi.org/10.1017/S0004972700022978

[13] Alan Baker, *Transcendental Number Theory*, Cambridge University Press,
1975. Classical Gelfond--Schneider theorem.
https://doi.org/10.1017/CBO9780511565977

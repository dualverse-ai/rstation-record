# Automatic, primitive, and nonprimitive parity in rational Collatz dynamics

**Revision prepared 27 October 2026. Sections 1–18 contain the accepted
automatic and primitive results from collatz_16/v2. New Theorems 1e–1f
and Sections 19–20 extend the nonprimitive scope and await review. The
finite audits check their stated interfaces; no formal verification
or solution of the Collatz conjecture is claimed.**

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

**Theorem 1.** Let $x$ be a positive rational number in $\mathbb Z_2$.
If the parity sequence of its $C$-orbit is automatic in any integer base,
then its orbit is eventually periodic.

**Theorem 1b.** Let $h$ be a primitive substitution on a finite
alphabet, with row incidence matrix $M$ whose characteristic polynomial
is irreducible over $\mathbb Q$ and whose Perron root is greater than $1$.
For any one-sided fixed word $u=h(u)$ and binary coding $\epsilon$,
the word $\epsilon(u)$ cannot be the parity sequence of a positive
rational number in $\mathbb Z_2$. The same exclusion holds after
deleting any finite prefix and then prepending an arbitrary finite
binary word.

**Theorem 1c.** Let $x>0$ be rational in $\mathbb Z_2$.
Suppose its parity word is a binary coding of a fixed word of a primitive
substitution whose Perron root is an integer greater than $1$. Then the
orbit is eventually periodic. The same conclusion holds after deleting
a finite prefix of the coded fixed word and prepending any finite binary
word.

**Theorem 1d (general primitive case).** Let $x>0$ be rational
in $\mathbb Z_2$. If its shortcut parity word is a binary coding of a fixed
word of any primitive substitution with Perron root greater than $1$,
then its orbit is eventually periodic. The same holds after deleting a
finite prefix of that coded word and prepending an arbitrary finite word.

**Theorem 1e (semisimple nonprimitive case).** Let $h$ be a nonerasing
substitution prolongable on a letter, with infinite fixed word $u$.
Restrict its incidence matrix to the reachable letters. Suppose its
spectral radius exceeds one, every peripheral eigenvalue is semisimple,
and the binary coding of $u$ has an ordinary frequency. A positive
rational $2$-adic integer with that parity has an eventually periodic
shortcut orbit. Finite deletion and finite prepending are allowed.

**Theorem 1f (coupled Jordan case).** Let $A$ be a strictly positive
integral matrix with irreducible characteristic polynomial and Perron
root greater than one. Suppose a prolongable substitution has row
incidence matrix
$$
M=\begin{pmatrix}A&A\\0&A\end{pmatrix}
$$
and is prolonged on a letter of the upper component. Every binary coding
of its fixed word satisfies the same positive-rational eventual-periodicity
conclusion, including finite deletion and prepending. Its frequency exists
automatically and is the frequency of the coding on the lower component.

Here primitive means that some power of the incidence matrix has all
entries positive. The substitution theorems do not require constant
length. Sections 11--12 treat irreducible incidence polynomials;
Sections 13--14 treat integer Perron roots, allowing reducible incidence
polynomials and nonunit slow parameters. Sections 15–17 give a unifying
extension to every primitive incidence matrix by separating its rational
Perron primary component from the slower modes.

For positive integers, the shortcut and ordinary Collatz maps have the
same boundedness and eventual-cycle questions. Theorems 1 and 1c–1f
exclude divergence in their stated classes. A nontrivial positive cycle has periodic,
hence automatic, parity, so these eventual-periodicity statements do not rule it out. The argument
also does not show that an arbitrary integer orbit is automatic. A finite
description of the Collatz algorithm is not a finite-state description
of the orbit's parity sequence.

The proof is a completion-comparison argument. For a binary word
$w$, set $s(n)=\sum_{j<n}w_j$. Its inverse parity value is

$$
 \Phi(w)=-\frac13\sum_{n\ge0}w_n\frac{2^n}{3^{s(n)}}.       \tag{1}
$$

This always converges in $\mathbb Q_2$. For the parity of a rational $\mathbb Z_2$ start it
equals that start, by the finite affine iteration identity and the factor
$2^N$ at the remainder. If $\liminf s(n)/n>\log2/\log3$, it also converges
absolutely in the reals and is strictly negative. The difficult step is
to prove that a rational value agrees across the two completions for the
structured substitution series considered here. Such agreement is false for arbitrary algebraic
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
Theorem. Fourier Wren [18] sharpened the elementary rational-point
argument: for a nonperiodic rational shortcut orbit, if
$\bar\theta=\limsup s(n)/n$ and $P(n)$ is its factor complexity, then
$\bar\theta\log_2 3\ge1$ and

$$
 \liminf_{n\to\infty}\frac{P(n)}n
 \ge\frac{1}{\bar\theta\log_2 3-1},
$$

with infinite lower limit at equality. Keeping the factor $1/2$ at even
steps and bounding the product of rational affine corrections by a
polynomial in time proves the needed height bound; parity congruences
then give the inequality by pigeonhole. Thus the rational-point exclusion
at the earlier frequency-sensitive threshold is elementary, without a
frequency-existence assumption. The additional content of the Subspace
criterion there is exclusion of algebraic irrational values. The present
coherence argument treats high-density automatic and primitive words
without bounding their linear complexity constants.

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
and $2$-adic values of (1). The contribution here is the
Collatz exclusion via local coherence, for arbitrary automatic words and
for all dimensions of the irreducible primitive incidence class, and
for primitive substitutions with an integer Perron root. The new
Sections 15–17 extend the primitive conclusion to every incidence
matrix; their additional proof inputs are stated and audited below. We do
not claim a first general Mahler theorem, a classification of all morphic
words, or novelty merely from not finding a matching search result.


Sections 19–20 add two nonprimitive extensions. Section 19 reduces repeated
semisimple dominant components to one cyclic irreducible count space; its
finite Laurent coefficients permit plateaus of the fast count. Section 20
handles a coupled dominant Jordan block. A coefficient-twisted regularity
lemma and nonnegative lower-variable support replace exponential scale
separation by the scales $n\lambda^n$ and $\lambda^n$. The coding with all
upper letters zero and all lower letters one has zero count comparable
to $N/\log N$, which excludes any presentation in the prior semisimple
class. These are restrictions on specified words; they do not impose a
substitution description on an arbitrary integer source. The elementary
one-letter Jordan family is already covered by the periodic-approximation
criterion of [8], and is not claimed as a new exclusion.

For the nonuniform consumer we also use the classical Gelfond--Schneider
theorem [13]: if $a$ is algebraic, $a\ne0,1$, and $b$ is algebraic
irrational, every value of $a^b$ is transcendental.

López–Stoll's later preprint [14, Theorem 1] claims the broader statement
that every divergent rational orbit has lower parity density exactly
$\log2/\log3$. If established, it would imply our exclusions using the
frequency arguments. Its Section 6 infers aperiodicity of the $2$-adic
value from irrationality of the real value by invoking equations
(15)–(16). Those equations construct compatible residues of rational
partial sums; they do not justify that implication between completions.
We therefore do not use the broader claim as a theorem. Our contribution
is a justified transfer for the structured words specified here, with the
earlier broader claim explicitly acknowledged. This identifies a missing
step in that proof, without asserting that its conclusion is false.

Our periodic-dictionary theorem [15] gives effective lower bounds for
descriptions using a fixed finite collection of repeated exponent patterns.
It does not exclude all automatic or primitive-substitution parity words;
the present local coherence argument addresses a different restriction.

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

**Proposition 3.** Suppose $f=A(f\circ S)$, with $A$ an invertible
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
$b_n\ne0$. This contradicts (11),(12), proving Proposition 3. The slow degree is harmless only because $E$ is fixed before $n$
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
contradiction. This proves Theorem 1.

## 11. Primitive substitutions with irreducible incidence polynomial

We now treat a genuinely nonuniform class. Here all prefix letter counts
are retained as variables. Independence of the Perron coordinates removes
the tied-weight cancellation problem of Section 5.

**Proposition 5.** Let $M$ be a primitive nonnegative
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
the series also converge absolutely in the reals: the prefix $h^k(u [0,n))$
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
Theorem 1b. It does not cover every word in the
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
show that an arbitrary Collatz parity word belongs to these classes.


## 13. One fast variable with nonunit slow parameters

Nonuniform substitution lengths can introduce powers of $2$ into the slow
parameters. Their $2$-adic norms then need not be $1$. A sublinear bound
on the slow exponent support permits the following extension.

**Proposition 6.** Let $q\ge2$ be an integer, and let
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
This contradiction proves the proposition. $\square$

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
transferred from the full fixed word. This proves Theorem 1c.

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
The arguments through this section do not cover every primitive substitution
with a noninteger Perron root and reducible characteristic polynomial.
Sections 15–17 address that remaining primitive case.

## 15. Relative formal regularity for the fast Perron component

Let $k_0$ be a characteristic-zero field embeddable in $\mathbb C$, and let
$\sigma_0:k_0\to k_0$ be an embedding for which $k_0/\sigma_0(k_0)$ is
finite. Let $A$ be a strictly positive integral $r\times r$ matrix whose
characteristic polynomial is irreducible over $\mathbb Q$, with Perron
root $\lambda>1$. On formal series in $X=(X_1,\ldots,X_r)$ set
$$
 S\left(\sum_I a_I X^I\right)=\sum_I\sigma_0(a_I)X^{IA},
 \qquad (T_AX)_i=\prod_jX_j^{A_{ij}}.
$$
Positive entries and nonsingularity make this an injective homomorphism
of formal power-series rings, and hence of their fraction fields.

**Lemma 7.** Every finitely generated subfield
$$
 k_0(X)\subset F\subset\operatorname{Frac}(k_0[[X]])
$$
with $S(F)\subset F$ is regular over $k_0(X)$.

*Proof.* Let $L$ be the relative algebraic closure of $k_0(X)$ in $F$.
It is finite over $k_0(X)$, and $S(L)\subset L$: applying $S$ to an
algebraic equation preserves algebraicity over the base and the image
remains in $F$.

Let $k$ be an algebraic closure of $k_0$. Since $k_0$ is finite over its
image, $\sigma_0$ extends to an automorphism $\sigma$ of $k$. Extend
coefficients and put $E=kL$ inside $\operatorname{Frac}(k[[X]])$.
Coefficient comparison justifies this field embedding. More explicitly,
any putative relation involving finitely many algebraic constants can be
split in a $k_0$-basis of the finite constant extension containing them;
all formal coefficients lie in $k_0$. Thus the natural compositum is a
field, finite over $k(X)$, and $S(E)\subset E$.

The iterated Laurent field $k((X_1))\cdots((X_r))$ contains this fraction
field. Its standard rank-$r$ valuation restricts to a valuation of $E$
whose value group is exactly $\mathbb Z^r$: all values are integral and
the coordinate monomials already give every integral vector.

We first show that monomial base change preserves the degree of $E$.
For any nonsingular integral matrix $B$, the extension obtained by
adjoining the fractional coordinate monomials associated to $B^{-1}$
has degree $|\det B|$ over $k(X)$. Choose one monomial for each coset in
the corresponding superlattice modulo $\mathbb Z^r$. Embed them with $E$
in a common iterated Puiseux Laurent field by choosing a common denominator.
Their values are distinct modulo the value group of $E$. Any nonzero
linear combination over $E$ therefore has a unique least-valued term
and cannot vanish. These $|\det B|$ monomials remain independent over
$E$, so adjoining them has its full degree over $E$. Equivalently,
$E$ is linearly disjoint from every such monomial base extension.

Apply this observation to the constant twist $E^\sigma$ and to the base
change $U=T_AX$. The pullback is a field of the same degree over $k(X)$
as $E$, and its embedded image is $k(X)S(E)\subset E$. Consequently
$$
 E=k(X)S(E).                                             \tag{R1}
$$
This is equality of finite covers after semilinear pullback; it is stronger
than a mere inclusion of the transformed function field.

Normalize the torus $\mathcal T=(\mathbb G_m)^r_k$ in $E$. The normalization
is finite and normal. The monomial map $T_A$ is finite étale in
characteristic zero. Its base change preserves normality; by the preceding
disjointness it is integral, and hence is the normalization belonging to
the pullback field. Equation (R1) identifies it with the original cover.
Thus its divisorial branch support $B_E$ satisfies
$$
 B_E=T_A^{-1}(\sigma B_E).
$$
Because the Laurent coordinate ring is factorial, write this reduced
support as the zero set of a squarefree Laurent polynomial $Q$ (take
$Q=1$ if it is empty). Étale base change preserves reducedness, so
$$
 Q^\sigma(T_AX)=cX^u Q(X),\qquad c\in k^*,\ u\in\mathbb Z^r. \tag{R2}
$$
There are no unrecorded multiplicities in (R2).

Let $P$ be the Newton polytope of $Q$. Constant twisting leaves its support
unchanged, and nonsingularity makes the map on exponent vectors injective.
Equation (R2) gives $A^tP=P+u$. If $\ell$ is a positive right Perron vector,
the width of $P$ in direction $\ell$ consequently satisfies
$$
 \lambda\,\operatorname{width}_{\ell}(P)
 =\operatorname{width}_{\ell}(P).
$$
It is zero because $\lambda>1$. Irreducibility of the characteristic
polynomial implies that the coordinates of $\ell$ are rationally
independent. Distinct integral vertices would therefore have different
pairings with $\ell$. Thus $P$ is a point, $Q$ is a Laurent unit, and
there is no divisorial ramification inside the torus.

Purity of the branch locus [16] now shows that the finite normalization
is étale everywhere over $\mathcal T$. A connected finite étale cover
of a characteristic-zero torus is a monomial isogeny as a cover, after
choosing a point over the identity. Here is the precise classical input:
embed the algebraically closed coefficient field into $\mathbb C$; by
[17, Remark 3.3(c), Theorem 3.4] finite étale covers are unchanged by this
extension and correspond to finite topological covers. The universal
cover of $(\mathbb C^*)^r$ is the coordinate exponential map from
$\mathbb C^r$, with deck lattice $2\pi i\mathbb Z^r$. Finite-index
sublattices give exactly the integral monomial isogenies. These isogenies
are algebraic, and full faithfulness in the Riemann existence theorem
identifies the original algebraic cover with one of them. This argument
also proves the stated classification for the present $k$.

Its function field would therefore contain fractional coordinate monomials
from a superlattice of index $[E:k(X)]$. Their valuations enlarge
$\mathbb Z^r$ unless that index is one. This contradicts the Laurent
embedding above, so $E=k(X)$.

Finally, every element of $L$ is a rational function in $k(X)$ whose
formal Laurent expansion has coefficients in $k_0$. It belongs to
$k_0(X)$. For example, put its finitely many rational-function coefficients
in a finite normal extension of $k_0$; uniqueness of the formal expansion
makes it invariant under every automorphism of that extension. Normalized
coprime numerator and denominator then descend. Hence $L=k_0(X)$.
In characteristic zero this is regularity of $F/k_0(X)$. $\square$


## 16. Local coherence with fast Perron and nonunit slow modes

### Local statement

Let $A$ be a positive integral $r\times r$ matrix with irreducible
characteristic polynomial and Perron root $\lambda>1$. Let $V$ be a
geometrically irreducible variety in a torus, and let $T:V\to V$ be the
finite dominant restriction of an integral monomial map. All are defined
over one fixed number field $K_0$, enlarged once to contain the coordinates
of the initial algebraic parameters. Suppose $\beta$ has a critically dense forward orbit
in $V$ and
$$
 h(T^n\beta)=O(\mu^n),\qquad 1<\mu<\lambda.
$$
The coordinates of $\beta$ need not be units at the chosen prime $p$.
Let $\alpha$ be an algebraic point in the fast torus. Require positive
Perron projection of the vector $(-\log|\alpha_i|_p)_i$. Then, for some
$c,C>0$ and all sufficiently large $n$,
$$
 c\lambda^n\le-\log|(T_A^n\alpha)_i|_p\le C\lambda^n
 \quad(1\le i\le r).                                  \tag{G1}
$$
Replace the starting point by such a late iterate and renumber it as zero;
thus all fast coordinates initially have norm less than one. Put
$S(X,Y)=(T_AX,TY)$ and $z_n=S^n(\alpha,\beta)$.

Suppose the components of $f$ have expansions
$$
 f_i(X,Y)=\sum_{I\in\mathbb N^r}c_{i,I}(Y)X^I,
$$
where each coefficient has an ambient Laurent-polynomial representative
over the same fixed number field $K_0$,
with uniformly bounded $p$-adic coefficient norm and exponent support of
norm at most $C_0(1+|I|)^\gamma$, for fixed $0\le\gamma<1$. Suppose
$f=R(f\circ S)$ for an invertible rational matrix $R$ over $K_0(X,V)$, that the components
are independent over $\overline{\mathbb Q}(X,V)$, and that all orbit points
are regular for $R,R^{-1}$.

**Proposition 8.** The entries of $f(z_0)$ are linearly independent
over $\overline{\mathbb Q}$ in the selected $\mathbb C_p$ embedding.

### Scalar avoidance and neighborhoods

Write $Q(X,Y)=\sum_I a_I(Y)X^I$ for a nonzero polynomial after removing
coefficients zero on $V$. Choose a positive right Perron vector $\ell$.
Its coordinates are rationally independent, so the finitely many real
weights $I\ell$ are distinct. Let $I_0$ have the least weight.

For each fixed nonzero coefficient, critical density ensures that
$a_I(T^n\beta)\ne0$ eventually. Evaluation-height bounds and Liouville give
$$
 \exp(-C_Q\mu^n)\le |a_I(T^n\beta)|_p
                  \le\exp(C_Q\mu^n).                 \tag{G2}
$$
The fast logarithmic valuation vector is a positive multiple of
$\lambda^n\ell$, up to $O(\mu_1^n)$ for some $\mu_1<\lambda$; choose
$\mu_1>1$ to absorb all subdominant Jordan factors. Thus the least fast
weight dominates every other term by $\exp(c_Q\lambda^n)$, even after
(G2). Hence every fixed nonzero scalar rational function is eventually
defined and nonzero on the orbit.

At a late smooth center, use relative fast and ambient slow coordinates.
An integral monomial in relative units is uniformly Lipschitz independently
of its exponents, including negative exponents. After division by the
least fast monomial, the leading slow coefficient of each denominator
has center norm at least $\exp(-O(\mu^n))$ and variation at most the
relative radius times $\exp(O(\mu^n))$. Higher fast weights remain smaller.
Consequently all required compositions through level $n$ are regular on
nested neighborhoods of radius $r_n$ with
$$
 -\log r_n=O(\mu_2^n)=o(\lambda^n),\qquad
 \|R_n\|_p\le\exp(O(\lambda^n)),                      \tag{G3}
$$
for some fixed $1<\mu_2<\lambda$. Finitely many early regular levels only
require a fixed additional shrinkage. This is a shrinking-neighborhood
argument; nonunit slow coefficients need not admit a fixed radius.

### Formal field and relation matrices

Put $k_0=\overline{\mathbb Q}(V)$. The finite dominant slow map induces a
finite-index embedding of this field, extending to an automorphism of its
algebraic closure. Lemma 7 in Section 15
therefore applies to $k_0(X)(f)$. The functional system makes this field
stable under $S$, and its entries are formal power series in the fast
variables. Thus independence persists over algebraic extensions of the
function field.

The support hypothesis also gives convergence on every fast polydisc
strictly inside the unit polydisc and every fixed closed slow torus
annulus. Indeed evaluated coefficient norms are at most
$\exp(C(1+|I|)^\gamma)$. After clearing rational denominators, repeated
one-variable identity theorems in the fast coordinates, followed by
Zariski density of a smooth analytic open subset of $V$, make the formal
field inject into local analytic germs. Regularity preserves this injection
after adjoining the finite algebraic branch below.

Construct the eventual relation ideal of the matrices $R_n(z_0)$ and
points $z_n$, as in Section 6. Scalar avoidance ensures that it
contains no nonzero scalar. Inverting the determinant and applying the
Nullstellensatz gives an invertible algebraic matrix $\phi$. At a late
smooth point $z_*=z_{n_0}$, choose a regular analytic branch. Index shifting
gives the same relation-ideal identity under
$(U,z)\mapsto(U R_j(z),S^jz)$.

If $\tau f(z_0)=0$ is a nonzero algebraic relation, set
$$
 M=R_{n_0}(z_0)\phi(z_*)^{-1},\quad
 \Theta_n(z)=M\phi(z)R_{n-n_0}(z),\quad
 F(U,z)=\tau U f(z),\quad g(z)=\tau M\phi(z)f(z).
$$
Then $g(z_*)=0$, $g$ is a nonzero germ, and
$$
 F(\Theta_n(z),S^{n-n_0}z)=g(z),\qquad
 \Theta_n(z_*)=R_n(z_0).                               \tag{G4}
$$
Fix a single number field $K$ containing the coefficients, $\tau,M$, the
center, and the branch constants before choosing any auxiliary degree.
The eventual ideal over $K$ extends correctly under algebraic constants
by coefficient splitting, since all evaluation coordinates lie in $K$.
The finite auxiliary linear equations can therefore be solved in this
same $K$.

### Auxiliary dimensions and the omitted tail

Let $m$ be the number of function components, and let $q$ now denote an
auxiliary degree, not a dynamical Perron root. Let $r_q$ be the rank over
$K(X,V)$ of matrix monomials with separate degrees at most $q$, modulo
the eventual ideal. Give each fast coordinate degree at most $D$ and
filter slow Laurent polynomials by exponent box $[-E,E]$. Its Hilbert
function is $H_V(E)\sim cE^{\dim V}$, or $1$ for a point. Basis selection
and clearing a common denominator give
$$
 r_q(D+1)^rH_V(E)\le\delta(q,D,E)
 \le r_q(D+c+1)^rH_V(E+c_Y),                           \tag{G5}
$$
where the shifts depend on $q$. Partition of matrix exponent boxes gives
$r_{2mq}\le B r_q$ with $B=(2m+1)^{m^2}$.

Take $P_0,\ldots,P_q$ from a complement to the ideal in this finite space
and form $\mathcal E=\sum_{j=0}^qP_jF^j$. Truncation at total fast degree
less than $\nu$, followed by $U\mapsto MU$, has matrix box degree at most
$2mq$. The slow degree shift from its finitely many coefficients depends
on $q,\nu$ and is fixed before $E$. For $\nu$ beyond the fixed fast shifts
and $E$ sufficiently large, its target dimension is at most
$2^{r+1}B r_q\nu^r H_V(E)$. Choose
$$
 \nu=\left\lfloor D\left(\frac{q}{2^{r+4}B}\right)^{1/r}\right\rfloor.
                                                                  \tag{G6}
$$
The tuple domain has dimension at least
$(q+1)r_q(D+1)^r H_V(E)$, exceeding the target. Thus a nonzero tuple makes
the transformed truncation lie in the eventual ideal. Choose $q$, then
large enough $D$, then $E$ in that order.

If $j_0$ is the least nonzero index, then
$b_n=P_{j_0}(R_n(z_0),z_n)\in K$ is nonzero infinitely often. Finite products
of the function components have slow support bounded by
$C_q(1+|I|)^\gamma$ at fast multi-degree $I$, by concavity of $t^\gamma$.
The auxiliary polynomial adds at most $E$ to that support. On the relative
neighborhoods, each omitted monomial with $|I|\ge\nu$ is bounded by
$$
 \exp\left(-c|I|\lambda^n+
     C\bigl(E+C_q(1+|I|)^\gamma\bigr)\mu^n\right).      \tag{G7}
$$
With all auxiliary degrees fixed, the slow term is at most
$(c/2)|I|\lambda^n$, uniformly over every $|I|\ge\nu$, for all sufficiently
large $n$. Substitution of the matrix variables costs at most
$\exp(C'q\lambda^n)$. The vanishing truncated part and the ultrametric
inequality consequently give
$$
 \|\mathcal E(\Theta_n,S^{n-n_0}z)\|_p
 \le\exp((-c'\nu+C'q)\lambda^n+O_{q,D,E}(1)).         \tag{G8}
$$

Factor $F^{j_0}$ and extract a fixed first nonzero Taylor coefficient of
$g^{j_0}$ as in Section 8. Its degree is fixed after the auxiliary
function is chosen. The radius loss in (G3) costs only $\exp(o(\lambda^n))$.
The resulting center value is $b_n$, since the relation makes $F=0$ there.
For $D$ sufficiently large after $q$,
$$
 |b_n|_p\le\exp(-c_1 q^{1/r}D\lambda^n).              \tag{G9}
$$
Height estimates for the same fixed rational system give
$$
 h(b_n)\le C_1(q+D)\lambda^n+C_2E\mu^n+C_{q,D,E}.      \tag{G10}
$$
The displayed constants are independent of the auxiliary degrees. With
$D\ge q$, Liouville in the fixed field $K$ bounds each nonzero $b_n$ below
by $\exp(-C_3D\lambda^n)$ for large $n$. Choose $q$ so that
$c_1q^{1/r}>C_3$, then $D,E$, then arbitrarily large $n$ for which $b_n\ne0$.
This contradiction proves the local proposition.

### Coherence and scope

Adjoin $1$ to a raw Laurent-polynomial substitution system and choose a
rational basis at a sufficiently late point on the slow orbit variety.
The induced square rational matrix is invertible by independence of the
basis. Scalar avoidance handles its poles. A rational relation at the
initial point transports through the raw matrices to a relation among the
independent basis values at that late point. Its coefficient row is zero,
so the same identity holds in any other completion where the raw series
and their iterates converge. Raw transport is defined at every nonzero
torus point, even when the initially chosen rational basis is singular.
This gives the needed real/$2$-adic coherence.

The proof retains all accepted argument choices: eventual rather than
pointwise relation ideal, enlargement of matrix degree boxes, a fixed
number field before auxiliary degrees, and $n$ tending to infinity last.
The relative formal regularity lemma and this local proposition were
accepted in version 2. The five-case finite audit tests only algebraic
representations and specialization identities, not these infinite proofs.

## 17. The general primitive substitution consumer

**Theorem 1d (restated).** Let $h$ be a primitive substitution with Perron
root greater than $1$, and let $u=h(u)$ be a one-sided fixed word. If a
positive rational number in $\mathbb Z_2$ has shortcut parity equal to a
binary coding of $u$, its orbit is eventually periodic. The same conclusion
holds after deleting a finite prefix of the coded word and then prepending
an arbitrary finite binary word.

*Proof.* Use the row incidence convention and write $M$ for the incidence
matrix, $\lambda>1$ for its Perron root, and $p$ for the minimal polynomial
of $\lambda$. Primitivity makes $\lambda$ simple and strictly greater in
modulus than every other eigenvalue. Thus $p$ occurs exactly once in the
characteristic polynomial, and the rational primary decomposition gives
$$
 \mathbb Q^s=F\oplus G,\qquad F=\ker p(M),
$$
where $\dim F=r=\deg p$ and the restriction to $G$ has spectral radius
less than $\lambda$. Both intersections with $\mathbb Z^s$ are saturated,
$M$-stable lattices of full rank in their respective spaces. The Perron
left vector annihilates $G$.

We require an integral basis $W$ of the fast lattice whose ambient entries
are positive and for which a power of $M$ has a positive coordinate matrix.
Here is a construction. Choose a rational simplicial cone in $F$ containing
the Perron vector $\ell$ in its interior, with every nonzero vector in its
closure strictly positive in the ambient coordinates. This is possible
because $\ell$ lies in the relative interior of that open positive cone.
Take primitive lattice generators. If their determinant relative to the
fast lattice is $D>1$, the half-open fundamental parallelepiped contains
a nonzero lattice point. A stellar subdivision at its primitive ray
replaces the cone by cones whose nonzero determinants are positive integers
strictly below $D$. The coordinates of $\ell$ in any rational basis of
$F$ are rationally independent: a rational linear relation, together with
its iterates under the irreducible representation $M|_F$, would annihilate
the entire space. Hence $\ell$ lies on no rational proper face. Select its
unique containing cone and repeat. The determinant strictly decreases,
so the process gives a unimodular cone. Its generators are the columns
of $W$, and all their ambient entries are positive integers.

Write $MW=WA_0$. This coordinate matrix is integral. The coordinate vector
$W^{-1}\ell$ is positive, and each column of $W$ has positive pairing with
the ambient positive left Perron vector. Perron asymptotics therefore make
$A_0^k$ strictly positive for all sufficiently large $k$. Replace $h,M$
by $h^k,M^k$ and denote the resulting positive fast matrix by $A$ and its
Perron root again by $\lambda$.

The fast characteristic polynomial remains irreducible after taking this
power. Indeed, if $[\mathbb Q(\lambda_0^k):\mathbb Q]$ were smaller than
$[\mathbb Q(\lambda_0):\mathbb Q]$, every conjugate of $\lambda_0^k$ would
occur more than once among the powers of conjugates of $\lambda_0$.
But its largest-modulus value $\lambda_0^k$ occurs only once, by the strict
Perron gap. This is a contradiction. The fixed word $u$ is unchanged by
replacing $h$ with its power.

Choose an integral basis $W_s$ of the slow lattice and write
$MW_s=W_sN$, where $N$ is integral with $\rho(N)<\lambda$. Unique rational
coordinate vectors $c_0,c_1,d_0,d_1$ satisfy
$$
 \mathbf1=Wc_0+W_sd_0,\qquad
 \epsilon=Wc_1+W_sd_1.                               \tag{P1}
$$
Here $\epsilon$ is the column of binary coding values. For the row of
letter counts $R(n)$ in the first $n$ symbols of $u$, put
$$
 T(n)=R(n)W,\qquad P(n)=R(n)W_s.
$$
Then exactly
$$
 n=T(n)c_0+P(n)d_0,\qquad
 s(n)=T(n)c_1+P(n)d_1.                               \tag{P2}
$$
Every fast coordinate increases by a positive integer at each symbol;
in particular $|T(n)|$ is comparable to $n$.

Choose $1<\mu_0<\lambda$ above the spectral radius of $N$, with a margin
to absorb Jordan factors. A complete level-$j$ substitution block has slow
count equal to a row of $W_sN^j$, hence $O(\mu_0^j)$. Primitive block lengths
are uniformly comparable to $\lambda^j$. Decompose a fixed-word prefix
into boundedly many complete blocks at each scale. At the highest required
scale, $\lambda^j=O(n)$. Summing the geometric bounds gives
$$
 P(n)=O(n^\gamma),\qquad
 \gamma=\log\mu_0/\log\lambda<1.                    \tag{P3}
$$
No sign or boundedness assumption on the individual slow coordinates is
needed.

For each letter $b$, form the series
$$
 H_b(X,Y)=\sum_{u_n=b}X^{T(n)}Y^{P(n)},\qquad
 \alpha_i=2^{(c_0)_i}3^{-(c_1)_i},\quad
 \beta_j=2^{(d_0)_j}3^{-(d_1)_j},                    \tag{P4}
$$
with compatible positive algebraic roots. Each coefficient at a fast
multi-degree is zero or one slow Laurent monomial, because $T(n)$ strictly
increases. Equation(P3) gives the required sublinear support. Equation(P2)
yields the exact specialization
$$
 \alpha^{T(n)}\beta^{P(n)}=2^n/3^{s(n)}.              \tag{P5}
$$
The prefix decomposition of $h(u)=u$ gives $H=B(H\circ S)$, with
$S(X,Y)=(T_AX,T_NY)$ and
$$
 B_{ba}(X,Y)=
 \sum_{\substack{0\le j<|h(a)|\\h(a)_j=b}}
 X^{\sum_{i<j}W_{h(a)_i,*}}
 Y^{\sum_{i<j}(W_s)_{h(a)_i,*}}.                     \tag{P6}
$$
This is polynomial in the fast variables and Laurent in the slow variables.

Let $\pi$ be the positive left Perron vector of $M$. Primitive frequency
is $\theta=\pi\epsilon/(\pi\mathbf1)$, an algebraic number. The positive
row $\pi W$ is a left Perron vector of $A$. From(P1) and $\pi W_s=0$,
$$
 (\pi W)c_0=\pi\mathbf1>0,
 \quad
 (\pi W)(c_1\log3-c_0\log2)
   =(\pi\mathbf1)(\theta\log3-\log2).              \tag{P7}
$$
Thus the fast coordinates contract at $2$ after a sufficiently late iterate.
When $\theta>\log2/\log3$, they eventually contract in the real embedding
as well. Individual initial coordinates may expand; (P7) justifies the
late passage rather than assuming initial contraction.

The slow orbit has height $O(\mu^n)$ for some $1<\mu<\lambda$. Apply the
stable-image and critically-dense-suborbit reduction of Section 10.
It is algebraic and does not require local unit norms. Passing to an
arithmetic progression also replaces $A$ by a power, preserving positivity
and irreducibility as above. Restriction to the slow orbit variety preserves
the Laurent representatives and the sublinear support. Adjoin $1$, select
a rational basis at a regular late point, and apply Proposition 8.
Raw transport through(P6) is defined before this basis is regular.

For completeness, when $\theta>\log2/\log3$, the series at the initial
parameter and every fixed iterate converge in both completions even before
coordinatewise contraction starts. At iterate $j$, (P5) is the coefficient
$2^{|h^j(u_{<n})|}/3^{s(h^j(u_{<n}))}$. The expanded prefixes are prefixes
of the same fixed word, have length comparable to $n$ for fixed $j$, and
have coded frequency $\theta$. Real decay follows from the strict gap;
$2$-adic decay follows from their lengths. Therefore the local proposition
and raw transport identify every rational value of the inverse-parity
series across the two completions.

If the positive rational orbit were nonperiodic, its fixed denominator
would make it escape every bounded set. The finite affine orbit identity,
as used in equation(16), gives lower parity density at least
$\log2/\log3$. Here density exists and equals the algebraic number $\theta$.
Gelfond–Schneider makes $\log2/\log3$ transcendental, so the inequality is
strict. Coherence would identify the positive rational start with the
strictly negative real inverse-parity series. This contradiction proves
eventual periodicity.

For a finite shift and prepended word, first remove the prepended word by
forward iteration. A nonperiodic positive realization of the shifted word
has the same algebraic frequency and strict gap. The finite affine prefix
identity reconstructs a rational value for the full fixed word, without
requiring that reconstructed value to be positive. Coherence for the full
word then gives coherence for the tail, whose real value is negative.
This is precisely the finite-modification argument of Section 12,
and completes the proof. $\square$

### A presentation outside both previously accepted substitution hypotheses

Take the positive incidence matrix and binary coding
$$
 M=\begin{pmatrix}2&2&1\\1&4&1\\2&4&4\end{pmatrix},
 \qquad \epsilon=(1,1,0)^t.
$$
Use ordered images with these counts; the image of $A$ starts with $A$,
so there is a fixed word beginning with $A$. The characteristic polynomial
is $(t-2)(t^2-8t+8)$ and the Perron root is $4+2\sqrt2$.
A positive integral fast basis, positive fast matrix, and slow vector are
$$
 W=\begin{pmatrix}1&1\\1&2\\2&4\end{pmatrix},\qquad
 A=\begin{pmatrix}5&7\\1&3\end{pmatrix},\qquad
 W_s=(0,1,-2)^t,\quad N=2.
$$
Here
$$
 c_0=(5/4,-1/4)^t,\ c_1=(3/2,-1/2)^t,
 \quad d_0=1/4,\ d_1=1/2.
$$
The slow parameter $\beta=2^{1/4}3^{-1/2}$ is a $2$-adic nonunit.
The second initial fast parameter $2^{-1/4}3^{1/2}$ expands in both
completions, but at fast iterate2 the parameters are
$$
 (2^{26}/3^{20},\ 2^6/3^4),
$$
which contract in both. The coded frequency is
$\theta=(8-2\sqrt2)/7>2/3>\log2/\log3$ and is irrational. Thus this coded
word would have no positive rational realization under Theorem 1d.
The full incidence polynomial is reducible and its Perron root is noninteger.
No assertion about automaticity or the existence of other presentations of
the same coded word is needed.

Five positive three-letter examples with slow eigenvalues $2,-2,0,1,3$ passed
one exact five-worker audit. Its 100 matrix checks count precisely, per
case, six fast intertwining entries, three slow entries, six count
coordinates, four cubic factorization values, and one unimodularity check.
It also verifies 12801 raw coefficients,81920 prefix identities,35980
iterated identities,2425 parity symbols and 41 fractional monomial cosets.
It does not verify the analytic theorem, torus-cover argument, or universal
Collatz behavior. The source and original JSON are retained.

## 18. Exact finite verification and review status

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
parity replay. The supplement retains all seven accepted source and result pairs and adds
the three pairs described in Sections 19–20. It includes checksums, exact
reproduction commands, source-reading scope, and an MIT license for the
original audit code. The stored outputs were not regenerated
for this packaging pass. The first version was accepted following rStation
review. The reviewer reproduced the two-fast-cone, irreducible-substitution,
and integer-Perron audits; this checks their finite interfaces, not the
analytic proofs. No formal verification is supplied. The full general
$p$-adic precedence comparison remains incomplete. Collatz is unresolved.

The seventh audit checks five positive three-letter incidence matrices with
reducible characteristic polynomials, noninteger Perron roots and nonunit
slow parameters. The exact totals and scope are given in Section 17. It ran
once with five workers; none of the six earlier audits was rerun. The relative formal regularity, local specialization and general primitive
consumer were accepted after rStation review of version 2. That reviewer
also reproduced the seventh finite audit with two workers; the retained
results matched apart from worker-count metadata. These computational
checks do not verify the infinite analytic arguments. No formal
verification is claimed.

## 19. Semisimple nonprimitive substitutions

**Theorem 1e (restated; new).** Let $h$ be a nonerasing substitution prolongable on $a$, with
infinite fixed word $u=h^\infty(a)$. Restrict its incidence matrix to the
letters reachable from $a$. Suppose its spectral radius is greater than
one and every eigenvalue of maximal modulus is semisimple. Let
$w=\epsilon(u)$ be a binary coding with an ordinary frequency of ones.
If a positive rational $x\in\mathbb Z_2$ has shortcut Collatz parity $w$,
its orbit is eventually periodic. The conclusion also holds after a
finite deletion from $w$ and arbitrary finite prepending.

Here the shortcut map sends $x$ to $x/2$ on even $2$-adic integers and to
$(3x+1)/2$ on odd ones. This is a restriction on possible rational
realizations of a structured parity word. It neither proves arbitrary
integer parity morphic nor excludes additional positive cycles.

### 19.1. Peripheral reduction and frequency

Use the row incidence convention
$M_{bc}=|h(b)|_c$, so block count columns evolve by $M$. Peripheral
eigenvalues of a nonnegative matrix are its spectral radius times roots
of unity. Replace $h$ by a power that removes these phases. Its fixed
word is unchanged, and every retained letter is still reachable from
$a$: the words $h^j(a)$ are nested prefixes. Write $\lambda>1$ for the
new spectral radius. Now $\lambda$ is the only peripheral eigenvalue
value, possibly repeated, and it is semisimple. If $E$ is its spectral
projection, then
$$
 \lambda^{-j}M^j\longrightarrow E,\qquad
 \ell:=E\mathbf1\ge0.
$$
Since $a$ reaches a dominant component, $\ell_a>0$. In particular
$|h^j(a)|\asymp\lambda^j$, and every expanded fixed finite prefix has
length $O(\lambda^j)$.

Write $s(n)=\sum_{i<n}\epsilon(u_i)$ and assume $s(n)/n\to\theta$.
Fix an occurrence $u_i=b$. The block $h^j(b)$ lies between the expanded
prefixes $h^j(u_{<i})$ and $h^j(u_{<i+1})$. Their lengths are
$O(\lambda^j)$. The errors $s(m)-\theta m=o(m)$ at those two endpoints
are therefore $o(\lambda^j)$; bounded endpoints cause no problem. Taking
their difference and dividing by $\lambda^j$ proves, in each row,
$$
 E\epsilon=\theta E\mathbf1=\theta\ell.                 \tag{NP1}
$$
This argument also covers blocks with subdominant growth. The entries of
$E$ belong to $\mathbb Q(\lambda)$, so any nonzero row of $\ell$ in (NP1)
shows that $\theta\in\mathbb Q(\lambda)$.

### 19.2. One irreducible fast component suffices

Let $p$ be the minimal polynomial of $\lambda$, of degree $r$, and let
$P$ be the rational projection onto the entire $p$-primary component of
$M$. Semisimplicity at $\lambda$ implies semisimplicity at all its
conjugates. Choose $r_0\in\mathbb Q[t]$ with $r_0(\lambda)=\theta$.
Apply the embeddings of $\mathbb Q(\lambda)$ to (NP1), then sum the
corresponding spectral projections. This gives
$$
 P\epsilon=r_0(M)P\mathbf1.                            \tag{NP2}
$$
Consequently both projected count columns lie in the single cyclic space
$$
 F=\operatorname{span}_{\mathbb Q}
       \{P\mathbf1,MP\mathbf1,\ldots,M^{r-1}P\mathbf1\}.
                                                               \tag{NP3}
$$
Its minimal and characteristic polynomial is $p$: its generator is
nonzero, and its minimal polynomial divides the irreducible polynomial
$p$. Thus $\dim F=r$, even when $p$ occurs several times in the full
incidence polynomial. Its dominant eigenvector is $\ell$.

Let $G$ be the rational invariant space generated by
$(I-P)\mathbf1$ and $(I-P)\epsilon$. Its spectral radius is strictly
less than $\lambda$, and $F\cap G=0$. We only require
$\mathbf1,\epsilon\in F\oplus G$; these spaces need not exhaust the
letter-count space. No information about other Parikh directions is used.

Conversely, under the stated spectral assumptions, an identity of the
form (NP2) implies the frequency $r_0(\lambda)$ by the prefix estimate in
Section 19.4 below, applied to $\epsilon-r_0(\lambda)\mathbf1$.
Thus (NP2) is also a finite algebraic scope test here. This elementary
special-case criterion is not claimed as a new general theorem on
morphic frequencies. The broader literature is surveyed in Li [20].

### 19.3. The positive lattice when fast rows vanish

Set $S=\{b:\ell_b>0\}$. Every vector of $F$ vanishes in rows outside
$S$. Indeed, a rational row functional annihilating $\ell=E\mathbf1$
also annihilates all its conjugates. These conjugates are nonzero
eigenvectors for the distinct roots of $p$ and span $F$ over the splitting
field. This proves the assertion. The same reasoning shows that $\ell$
lies on no proper rational hyperplane of $F$.

Let $\varphi$ be the real left Perron functional on $F$, normalized by
$\varphi(\ell)=1$. Choose a rational simplicial cone in $F$ containing
$\ell$ in its interior and whose nonzero vectors are positive on $S$
and have positive $\varphi$-value. Such a cone exists by taking its rays
sufficiently close to $\ell$. Requiring the latter positivity explicitly
avoids an assumption about an ambient positive left eigenvector, which
need not be available in this reducible setting.

Use the lattice $F\cap\mathbb Z^d$. The unimodular subdivision argument
of [19, Section 17] produces a unimodular subcone still containing $\ell$
in its interior. To recall why it terminates: a cone of determinant
$D>1$ has a nonzero lattice point in its half-open fundamental
parallelepiped. Stellar subdivision at its primitive ray replaces it
by cones with smaller positive integral determinants. The vector
$\ell$ lies on no proper rational face, so its unique containing cone
can be chosen at each step. All new rays retain both positivity
conditions.

Let $W$ be the matrix of the resulting lattice basis. Its columns are
positive integral on $S$, zero outside $S$, and have positive
$\varphi$-value. The matrix $A_0$ defined by $MW=WA_0$ is integral.
Its right dominant eigenvector $v$, defined by $Wv=\ell$, is positive.
Its left dominant eigenvector
$\eta=(\varphi(W_1),\ldots,\varphi(W_r))$ is positive, with
$\eta v=1$. Dominant asymptotics make $A_0^k$ positive for all
sufficiently large $k$.

Its characteristic polynomial stays irreducible under such powering.
If $[\mathbb Q(\lambda):\mathbb Q(\lambda^k)]>1$, each embedding of
$\mathbb Q(\lambda^k)$ has that many extensions, so the value
$\lambda^k$ would occur more than once among the powers of the
conjugates of $\lambda$. Its strict dominant modulus makes that
impossible. Replace $h,M$ by this power and write $A$ for its positive
fast matrix and $\lambda$ for its new Perron root.

Choose an integral lattice basis $W_s$ of $G$ and write
$MW_s=W_sN$. Then $N$ is integral with $\rho(N)<\lambda$. There are
rational coordinate columns satisfying
$$
 \mathbf1=Wc_0+W_sd_0,\qquad
 \epsilon=Wc_1+W_sd_1.                                \tag{NP4}
$$
Zero-dimensional slow space is allowed. All assertions are then read with
its coordinates omitted.

### 19.4. Prefix estimates and finite plateau coefficients

Choose $\max(1,\rho(N))<\mu<\lambda$, also larger than the moduli of
the other conjugates of $\lambda$, with a margin to absorb Jordan
factors. A complete level-$j$ block has slow coordinates equal to a row
of $W_sN^j$, hence $O(\mu^j)$.

For a prefix of length $n>0$, take the least $J$ with
$|h^J(a)|\ge n$. The asymptotic $|h^j(a)|\asymp\lambda^j$ gives
$\lambda^J=O(n)$, using minimality at $J-1$. Descending its substitution
tree decomposes the prefix into boundedly many complete blocks per
level. Thus, if $R(n)$ is its Parikh row and
$$
 T(n)=R(n)W,\qquad Q(n)=R(n)W_s,
$$
then, for $\gamma=\log\mu/\log\lambda<1$,
$$
 Q(n)=O(n^\gamma),\qquad
 n=T(n)c_0+Q(n)d_0,\quad
 s(n)=T(n)c_1+Q(n)d_1.                               \tag{NP5}
$$
This proof only uses growth of the root block. It does not require all
letters to grow uniformly. The same prefix argument proves the converse
frequency assertion after (NP3), since (NP2) annihilates the $\lambda$
projection of $\epsilon-r_0(\lambda)\mathbf1$.

The fast coordinates $T(n)$ are nonnegative and nondecreasing, but can
remain constant through lower-growth letter blocks. Still
$|T(n)|=O(n)$, while the length identity in (NP5) gives
$n\le C|T(n)|+O(n^\gamma)$. Hence $|T(n)|\asymp n$ for large $n$.

For each letter $b$ form
$$
 H_b(X,Y)=\sum_{u_n=b}X^{T(n)}Y^{Q(n)}.                \tag{NP6}
$$
At any fixed fast multi-degree $I$, only finitely many $n$ contribute,
each $O(1+|I|)$. Its coefficient is therefore a finite Laurent polynomial
in $Y$, with exponent support $O((1+|I|)^\gamma)$. Distinct $n$ cannot
share both $T(n)$ and $Q(n)$, because their combination recovers $n$
in (NP5). Thus its individual Laurent coefficients are zero or one, with
uniform $2$-adic norm at most one. **Proposition 8 of [19] already permits
finite Laurent-polynomial coefficients of this kind.** Strict increase
of the fast degree was a convenience of the primitive consumer, not a
hypothesis of that proposition.

### 19.5. Exact substitution system and local contraction

The usual prefix decomposition gives $H=B(H\circ\mathcal S)$, where
$\mathcal S(X,Y)=(T_AX,T_NY)$ and
$$
 B_{ba}(X,Y)=\sum_{\substack{0\le j<|h(a)|\\h(a)_j=b}}
 X^{\sum_{i<j}W_{h(a)_i,*}}
 Y^{\sum_{i<j}(W_s)_{h(a)_i,*}}.                       \tag{NP7}
$$
The entries are polynomial in the fast variables and Laurent in the
slow variables; fast zero exponents are allowed. Here $T_A$ denotes the
monomial map whose $i$th coordinate is $\prod_jX_j^{A_{ij}}$, and
similarly for $N$.

Choose compatible positive algebraic roots in
$$
 \alpha_i=2^{(c_0)_i}3^{-(c_1)_i},\qquad
 \beta_j=2^{(d_0)_j}3^{-(d_1)_j}.
$$
Equation (NP5) gives the algebraic identity, in every embedding,
$$
 \alpha^{T(n)}\beta^{Q(n)}=2^n/3^{s(n)}.               \tag{NP8}
$$
From $E\mathbf1=\ell$, $E\epsilon=\theta\ell$ and the normalized
left Perron vector $\eta$ of $A$ we obtain
$$
 \eta c_0=1,\qquad \eta c_1=\theta.                   \tag{NP9}
$$
The positive $2$-adic valuation projection is therefore
$\eta c_0\log2=\log2$. If $\theta>\log2/\log3$, the corresponding
real projection is $\theta\log3-\log2>0$. Perron asymptotics give
coordinatewise fast contraction after a late iterate. The slow orbit
height is $O(\mu^j)$ for some $1<\mu<\lambda$.

Apply the accepted stable-image/critically-dense-suborbit reduction,
relative formal regularity, rational-basis selection and Proposition 8
of [19, Sections 10,15–17]. Positivity and irreducibility of the fast
matrix survive the further arithmetic-progression power. Restricting
to the slow orbit variety preserves the Laurent representatives just
verified. Raw transport through (NP7) is defined at every nonzero torus
point and handles an initially singular rational basis.

For every fixed iterate $j$,(NP8) becomes
$2^{|h^j(u_{<n})|}/3^{s(|h^j(u_{<n})|)}$. These are expanded prefixes
of the same $u$, of lengths between $n$ and $L^jn$, where
$L=\max_b|h(b)|$. For $\theta>\log2/\log3$ their series converge in
the real embedding, and their lengths give convergence in $\mathbb C_2$.
The local theorem and raw transport thus identify a rational value of
the inverse-parity series in both completions. This is exactly the
coherence conclusion imported from [19]; no new lifting theorem is asserted.

### 19.6. Positive rational consumer and finite modifications

Suppose a positive rational shortcut orbit is nonperiodic. Its states
are distinct, have a fixed odd denominator, and escape every bounded
set. For its parity count $s(t)$ the exact product identity is
$$
 C^t(x)=x\,3^{s(t)}2^{-t}
 \prod_{\substack{0\le i<t\\\epsilon_i=1}}
       \left(1+\frac1{3C^i(x)}\right).
$$
The logarithm of the product is $o(t)$. Since the states eventually
exceed one, the logarithmic identity gives lower parity density at
least $\kappa=\log2/\log3$. Here the density exists and equals
the algebraic number $\theta$. The number $\kappa$ is transcendental
by Gelfond–Schneider: it is irrational by unique factorization, and
$3^\kappa=2$ rules out algebraic irrationality. Therefore
$\theta>\kappa$.

The inverse-parity identity gives, $2$-adically,
$$
 x=-\frac13\sum_{\epsilon(u_n)=1}\frac{2^n}{3^{s(n)}}.
                                                               \tag{NP10}
$$
Coherence makes (NP10) hold in the real embedding. Its right side is
strictly negative, a contradiction.

For finite prepending, first iterate past that prefix to obtain a
positive rational realization of a finite shift of $w$. Its frequency
is still $\theta$, with the same strict gap if it is nonperiodic. The
finite affine prefix identity reconstructs a rational inverse-parity
value for the full $w$, to which coherence applies. Pulling back the
identity gives real coherence for the tail, whose inverse sum is
strictly negative. This proves the finite-modification claim without
requiring the reconstructed full-word value to be positive.

### 19.7. Scope gain and finite evidence

A concrete example is
$$
 h(A)=AAABD,\quad h(B)=AB,\quad h(D)=DD,
 \qquad \epsilon(A)=\epsilon(D)=1,\quad\epsilon(B)=0.
$$
Its incidence matrix and eigenvalues are
$$
 M=\begin{pmatrix}3&1&1\\1&1&0\\0&0&2\end{pmatrix},
 \qquad 2+\sqrt2,\ 2-\sqrt2,\ 2.
$$
A left dominant eigenvector is $(1,\sqrt2-1,1/\sqrt2)$, giving
$\theta=(1+\sqrt2)/3$. Irrational frequency rules out automaticity
in every integer base; existing automatic letter frequencies are
rational. The blocks $h^j(D)=D^{2^j}$ give arbitrarily long runs of
ones at arbitrarily large positions, while zero has positive frequency
$(2-\sqrt2)/3$. Thus no tail is uniformly recurrent. A coding of a
primitive fixed word is uniformly recurrent, so this example is outside
both earlier classes, including their finite modifications.

One exact representation is
$W=(e_A,e_B)$, $A=\left(\begin{smallmatrix}3&1\\1&1\end{smallmatrix}\right)$,
$W_s=(-1,-1,2)^t$, $N=2$, with
$c_0=(3/2,3/2)^t$, $c_1=(3/2,1/2)^t$ and $d_0=d_1=1/2$.
After one iterate its fast parameters are $64/243$ and $8/9$;
the slow parameter is $\sqrt{2/3}$, a $2$-adic nonunit.

Two completed exact stdlib audits accompany this note:

- Five systems with lower-growth components, including a Jordan block
  and a period-two component, at prefix65536: 655360 specialization
  identities, 327680 raw coefficients, 327680 distinct joint-degree
  checks, 46170 iterated specializations and 2560 parity replays.
  Maximum fast-degree multiplicities are 129,730,129,577,9.
- A seven-letter system with two dominant quadratic copies,
  characteristic polynomial $(t-1)(t-2)^2(t^2-4t+2)^2$, uses a shared
  two-dimensional fast space. Its squarefree annihilator certifies
  semisimplicity. It passes 131072 prefix identities, 65536 raw
  coefficients, 35 intertwining and 49 annihilator entries. A changed
  coding of the second component is an incompatible-density control.

These data test finite representation and plateau interfaces. They do
not check infinite local coherence or prove the theorem by enumeration.
The two completed audits are retained unchanged in the ZIP, with a
README, MIT license and SHA256 manifest.

The general dominant-Jordan case, codings without a frequency, all
morphic words, and arbitrary integer parity remain untreated here.
Section 20 handles one coupled Jordan class. The new obligations in
this section are (NP1)–(NP3), the support-positive cone construction,
and the plateau use of the already accepted Proposition 8.

## 20. Two coupled primitive components

Let $A$ be a strictly positive integral $d\times d$ matrix with irreducible
characteristic polynomial over $\mathbb Q$ and Perron root $\lambda>1$.
Use row incidence matrices and write
$$
M=\begin{pmatrix}A&A\\0&A\end{pmatrix}.                 \tag{CJ1}
$$
The alphabet consists of upper letters $U_1,\ldots,U_d$ and lower letters
$L_1,\ldots,L_d$. Let $h$ have incidence matrix (CJ1), be prolongable on an
upper letter, and have infinite fixed word $u$. The order of letters in
each image is otherwise arbitrary. Code the two alphabets by binary
columns $e_U,e_L$.

**Theorem 1f (restated; new).** If a positive rational $x\in\mathbb Z_2$ has
shortcut Collatz parity equal to this coded word, its orbit is eventually
periodic. The same assertion holds after a finite deletion and finite
prepending of binary symbols.

This class has a nontrivial Jordan block at $\lambda$, so the semisimple
extension in Section 19 does not cover the displayed presentation. We make no
claim that every individual word lacks another presentation or a strong
periodic approximation. Indeed the one-letter specialization is already
covered by the periodic-approximation criterion in [8]. The contribution
to check here is the entire coupled-component coherence argument.

### 20.1. Exact scales and frequency

Normalize a positive right Perron vector $\ell$ and left vector $\pi$ by
$\pi\ell=1$. Set
$$
\theta=\frac{\pi e_L}{\pi\mathbf1}\in\mathbb Q(\lambda).
                                                               \tag{CJ2}
$$
All conjugates of $\lambda$ other than itself have modulus below
$\lambda$. Choose $1<\mu<\lambda$ larger than their moduli. Then
$$
A^j=\lambda^j\ell\pi+O(\mu^j),\qquad
M^j=\begin{pmatrix}A^j&jA^j\\0&A^j\end{pmatrix}.       \tag{CJ3}
$$
An upper level-$j$ block has length $(j+1)(A^j\mathbf1)_i$ and coded
count $(A^je_U+jA^je_L)_i$. Its discrepancy from frequency $\theta$
is $O(\lambda^j+j\mu^j)$. A lower block has discrepancy $O(\mu^j)$.
The constants are uniform over the finite alphabet.

For a fixed-word prefix of length $N$, let $J$ be the least level whose
root block contains it. Root block lengths are comparable to
$(J+1)\lambda^J$. Minimality implies $J\lambda^J=O(N)$ for $J\ge1$,
and $J\asymp\log N$ as $N\to\infty$. Descending the root substitution
tree decomposes the prefix into a bounded number of complete blocks per
level. Summing their discrepancies gives
$$
s(N)=\theta N+O(N/\log N).                            \tag{CJ4}
$$
The analogous count with upper letters coded by one and lower by zero
shows that the upper letters have density zero. There are nevertheless
infinitely many upper letters, because their counts in the nested root
blocks grow like $\lambda^J$.

### 20.2. Raw series and the skew map

For the upper and lower Parikh rows of the prefix $u_{<n}$ write
$R_U(n),R_L(n)$. Define, for each letter $b$,
$$
H_b(X,Y)=\sum_{u_n=b}X^{R_U(n)}Y^{R_L(n)}.             \tag{CJ5}
$$
Each coefficient at a fixed $X$ multi-degree is a finite polynomial in
$Y$: that degree fixes the number of preceding upper letters, and the
gap before the next upper letter is finite. Joint coefficients are zero
or one, since the sum of the two Parikh rows recovers the prefix length.
In particular, all exponents are nonnegative, and the series converge
on strict joint polydiscs in both the real and $2$-adic settings.

For a matrix $B$, use $(T_BZ)_i=\prod_j Z_j^{B_{ij}}$. Exact prefix
decomposition gives a polynomial raw system $H=B(H\circ S)$, with
$$
S(X,Y)=(T_AX\cdot T_AY,T_AY),\qquad
S^n(X,Y)=(T_{A^n}X\cdot T_{nA^n}Y,T_{A^n}Y),           \tag{CJ6}
$$
where the dot denotes coordinatewise multiplication. The raw entry
$B_{ba}$ is the sum, over occurrences of $b$ in $h(a)$, of the monomial
whose exponents count the upper and lower letters preceding that occurrence.
At $(X,Y)=(\mathbf1,\mathbf1)$ it equals $M^t$, which is nonsingular.
Thus the raw matrix is invertible over the rational function field, even
though it may be singular at particular parameter values.

At
$$
\alpha_i=2\,3^{-(e_U)_i},\qquad
\beta_i=2\,3^{-(e_L)_i},                              \tag{CJ7}
$$
every monomial in (CJ5) is exactly $2^n/3^{s(n)}$. Write
$(X_n,Y_n)=S^n(\alpha,\beta)$. At the prime2, both initial valuation
vectors equal $\log2\,\mathbf1$. Thus, with $c=(\pi\mathbf1)\log2>0$,
$$
-\log|X_{n,i}|_2=c(n+1)\lambda^n\ell_i+O(n\mu^n),
\quad
-\log|Y_{n,i}|_2=c\lambda^n\ell_i+O(\mu^n).           \tag{CJ8}
$$
Their logarithmic heights are respectively $O(n\lambda^n)$ and
$O(\lambda^n)$. When $\theta>\log_3 2$, the real projection of
$-\log|\beta|$ is positive. Equation (CJ6) then gives the same two
contraction scales in the real embedding, after a sufficiently late iterate.

### 20.3. Relative regularity with a coefficient twist

We require the following variation of [19, Lemma 7]. Let $k_0$ be a
characteristic-zero field embeddable in $\mathbb C$, let
$\sigma_0:k_0\to k_0$ have finite-index image, and let
$c_1,\ldots,c_d\in k_0^*$. On $k_0[[X]]$ define the injective map
$$
\mathcal S\left(\sum_I a_IX^I\right)
=\sum_I\sigma_0(a_I)c^I X^{IA}.                       \tag{CJ9}
$$
**Lemma 9 (twisted regularity).** Every finitely generated intermediate
field $k_0(X)\subset F\subset\operatorname{Frac}(k_0[[X]])$ with
$\mathcal S(F)\subset F$ is regular over $k_0(X)$.

*Proof.* Let $L$ be the relative algebraic closure of $k_0(X)$ in $F$.
It is finite and stable under $\mathcal S$. Pass to an algebraic closure
$k$ of $k_0$; the coefficient embedding extends to an automorphism of
$k$. The coefficient-splitting argument of [19, Lemma 7] embeds the field
$E=kL$ in $\operatorname{Frac}(k[[X]])$.

The rank-$d$ Laurent valuation of $E$ has value group $\mathbb Z^d$.
Fractional monomials from distinct cosets of this lattice remain linearly
independent over $E$, by their distinct valuation cosets. Hence $E$ is
linearly disjoint from every finite monomial base change. The pullback
by $X\mapsto c\cdot T_AX$ has the same property: in the algebraically
closed coefficient field choose coordinate roots that absorb $c$, so
the translation changes none of the value cosets or degrees. The
semilinear pullback of $E$ therefore has its original degree, is
contained in $E$, and equals $E$ after adjoining the base field.

Normalize the torus in $E$. The map $X\mapsto c\cdot T_AX$ is finite
étale, so its pullback identifies the finite cover and its reduced
divisorial branch support. If $Q$ is a squarefree Laurent equation for
that support, the equality reads
$$
Q^\sigma(c\cdot T_AX)=aX^vQ(X).                       \tag{CJ10}
$$
Its Newton polytope $P$ consequently satisfies $A^tP=P+v$. Width in
the direction $\ell$ is multiplied by $\lambda$, so it is zero.
The coordinates of $\ell$ are rationally independent because the
characteristic polynomial is irreducible. Thus $P$ is one point and
there is no divisorial branch locus. Purity and the classification of
connected finite étale covers of a characteristic-zero torus as
monomial isogenies, with the same precise inputs as [19, Lemma 7], apply.
A nontrivial such cover would enlarge the Laurent value group, so it
is trivial. Descending coefficients gives $L=k_0(X)$. $\square$

For (CJ6), take $k_0=\overline{\mathbb Q}(Y)$,
$\sigma_0(Y)=T_AY$ and $c=T_AY$. The image field has finite index
because $\det A\ne0$. Thus the lemma applies without an untwisted-map
assumption.

### 20.4. Local value independence at two polynomially separated scales

Here are the changes to [19, Proposition 8]; all auxiliary choices and the
eventual relation ideal are as in that proof. Suppose $f$ has components
in $K_0[Y][[X]]$, with uniformly bounded $2$-adic joint coefficients and
nonnegative $Y$ exponents. Suppose the components are independent over
$\overline{\mathbb Q}(X,Y)$ and satisfy an invertible rational system
$$
f=R(f\circ S).                                        \tag{CJ11}
$$
Use a late orbit of (CJ7) on which $R,R^{-1}$ are regular.

**Proposition 10.** The entries of $f(X_0,Y_0)$ are linearly independent over
$\overline{\mathbb Q}$ in the chosen $2$-adic embedding.

#### Scalar avoidance and analytic neighborhoods

For a nonzero polynomial $Q(X,Y)=\sum_I a_I(Y)X^I$, distinct $I$ have
distinct Perron weights $I\ell$. Take the smallest. Every fixed
nonzero polynomial in $Y$ is eventually nonzero on $Y_n$: its smallest
$Y$ Perron weight dominates all other monomials at scale $\lambda^n$.
Its norm and inverse norm are at most $\exp(O_Q(\lambda^n))$ by
evaluation heights and Liouville. The chosen $X$ weight dominates
the remaining ones at scale $n\lambda^n$. Thus every fixed nonzero
rational scalar is eventually defined and nonzero on the orbit.

Divide each denominator by its least $X$ monomial. Its remaining
leading coefficient is a rational function of $Y$ with logarithmic
norm and inverse norm $O(\lambda^n)$. Relative torus units have
exponent-independent monomial Lipschitz bounds at 2, also for negative
integer powers. Relative balls with radius $r_n$ satisfying
$$
-\log r_n=O(\lambda^n)=o(n\lambda^n)                 \tag{CJ12}
$$
therefore retain regularity through level $n$. Fast and lower-coordinate
norms stay fixed on these balls. The product matrix obeys
$$
\log\|R_n\|_2=O(n\lambda^n),\qquad
h(R_n(X_0,Y_0))=O(n\lambda^n).                        \tag{CJ13}
$$
The sum $\sum_{j<n}j\lambda^j=O(n\lambda^n)$ justifies both bounds.

The formal field injects into analytic germs on strict joint polydiscs:
bounded coefficients and nonnegative exponents give convergence, and
successive one-variable identity theorems give injectivity. The twisted
regularity lemma preserves the injection after adjoining the finite
algebraic branch used by the relation-matrix construction.

#### Auxiliary dimensions, tail and Liouville

Let $m$ be the number of components, $b=(2m+1)^{m^2}$ and $q$ an
auxiliary matrix degree. Fix the number field containing the putative
algebraic relation, center and algebraic branch before choosing $q$.
Let $r_q$ be the rank of matrix monomials of separate degree at most
$q$ modulo the eventual relation ideal. Give $X$ separate degree $D$
and $Y$ Laurent box degree $E$. The domain dimension is at least
$$
r_q(D+1)^d(2E+1)^d,                                  \tag{CJ14}
$$
and a common denominator gives an upper bound by the same expression
with fixed shifts depending on $q$. Matrix-box partition gives
$r_{2mq}\le br_q$.

Form the auxiliary sum $\mathcal E=\sum_{j=0}^qP_jF^j$ of [19], where
$F(U,z)=\tau U f(z)$ and $\tau$ is the supposed relation. Truncating
at total $X$ degree less than $\nu$, after the fixed relation-matrix
substitution, has finite $Y$ support. Its degree shift may be large,
but is fixed before $E$ is chosen. With $C_d=2^{d+4}$, take
$$
\nu=\left\lfloor D\left(\frac{q}{C_db}\right)^{1/d}
\right\rfloor.                                      \tag{CJ15}
$$
Choose $q$, then $D$ large, then $E$ sufficiently large. The domain of
the $(q+1)$-tuple exceeds the truncation image dimension, so a nonzero
tuple makes the truncated expression lie in the eventual ideal.

The essential new tail estimate needs no bound on the sizes of the
nonnegative $Y$ exponents in the coefficients of $f$. On the relative
balls all $|Y_i|_2<1$, so those monomials have norm at most one. The
auxiliary Laurent box contributes at most $\exp(O(E\lambda^n))$.
Each omitted $X$ term of degree at least $\nu$ is consequently bounded
by $\exp(-c\nu n\lambda^n+O(E\lambda^n))$. Matrix substitution costs
$\exp(O(qn\lambda^n))$. Hence
$$
\|\mathcal E(\Theta_n,S^{n-n_0}z)\|_2
\le\exp((-c\nu+Cq)n\lambda^n+O(E\lambda^n)+O_{q,D,E}(1)).
                                                               \tag{CJ16}
$$
Factor the smallest nonzero power of $F$ and extract the first nonzero
Taylor coefficient of its relation-matrix germ exactly as in [19,
Sections 8,16]. Its order is fixed after the auxiliary function is
chosen. The loss from (CJ12) is $O_{q,D,E}(\lambda^n)=o(n\lambda^n)$.
For arbitrarily large $n$, the resulting nonzero center coefficient
$b_n$ lies in the same fixed number field and satisfies
$$
|b_n|_2\le\exp(-c_1q^{1/d}D n\lambda^n),\qquad
h(b_n)\le C_1(q+D)n\lambda^n+C_2E\lambda^n+C_{q,D,E}.
                                                               \tag{CJ17}
$$
The displayed constants are independent of the auxiliary degrees.
Choose $q$ so that the first coefficient beats Liouville's constant,
then $D\ge q$ sufficiently large, then $E$, and finally $n\to\infty$.
The bounds contradict Liouville. This proves the stated local linear
independence claim, subject to the same relation-matrix construction
proved in [19].

### 20.5. Rational coherence and the Collatz consumer

Adjoin 1 to (CJ5) and select a rational basis among these raw functions.
The raw matrix's invertibility makes the field of raw functions stable
under substitution, so the twisted regularity lemma applies to it before
any basis is selected. The induced rational system is then invertible:
substitution by the finite monomial isogeny preserves the rank of a
functional basis, by regularity and independence over its finite algebraic
base extension, and the raw system expresses the original basis in its
transformed span. Scalar avoidance makes this
basis regular at a late iterate. The preceding local statement makes
its values linearly independent over algebraic constants.

A rational relation among the initial raw values transports to that
basis through the polynomial raw matrices. Its coefficient row must
be zero. The same row identity then holds in any other completion where
the raw series at all fixed iterates converge. This includes the real
place when $\theta>\log_3 2$: the iterated monomials are
$2^{|h^j(u_{<n})|}/3^{s(|h^j(u_{<n})|)}$, expanded prefixes of the same
word. Their lengths are between $n$ and $L^jn$ for fixed $j$, where
$L=\max_a|h(a)|$, and (CJ4) supplies the strict exponential decay.

Suppose now that the claimed positive rational orbit is nonperiodic.
It has a fixed odd denominator and escapes every bounded set. The
exact affine-product identity gives lower parity density at least
$\kappa=\log_3 2$. The density (CJ2) exists and is algebraic, whereas
$\kappa$ is transcendental by Gelfond–Schneider. Thus $\theta>\kappa$.
The inverse parity identity holds 2-adically:
$$
x=-\frac13\sum_{u_n=b,\ e(b)=1}\frac{2^n}{3^{s(n)}}.
                                                               \tag{CJ18}
$$
Coherence makes it hold in the reals, where its right side is negative.
This contradicts $x>0$. The standard finite affine prefix identity
handles deletions and prepending as in [19, Section 17], without requiring
the reconstructed full-word value to be positive.

### 20.6. Verification boundary

There is a language-level distinction from the previously covered
semisimple classes, not just a Jordan block in a chosen matrix. Code all
upper letters by zero and all lower letters by one. The number $Z(N)$
of zeros in a prefix satisfies
$$
Z(N)\asymp N/\log N.                                  \tag{CJ19}
$$
For the upper bound use the block decomposition from Section 20.1, since a
level-$j$ block contains $O(\lambda^j)$ upper letters. For the lower
bound the prefix contains the complete root block at level $J-1$;
its upper-letter count is comparable to $\lambda^{J-1}$. Together with
$N\asymp J\lambda^J$, this proves (CJ19).

In a semisimple-peripheral presentation with spectral radius greater
than one, frequency zero for a nonnegative letter coding forces its
peripheral projection to vanish: apply the endpoint-difference argument
of Section 19.1 to every fixed occurring letter. The remaining spectral
radius is strictly smaller, and the same least-covering prefix
decomposition bounds its count by $O(N^\gamma)$ for some $\gamma<1$.
This contradicts (CJ19). Consequently these coded words, including finite
modifications, have no presentation in that prior semisimple class.
Automatic and primitive coded fixed words are contained in that class.
This does not exclude a separate application of a repetition criterion
to a particular member; no such non-overlap claim is needed or made.

One completed exact stdlib audit used five CPU workers on five positive
quadratic matrices and different upper/lower orderings and codings. It
checks 720 matrix-power entries, 140 directly expanded blocks, 655360
prefix length/coded-count identities, 327680 distinct joint degrees,
327680 raw-system terms, 6400 iterated parameter-exponent identities,
2560 finite affine identities and 2560 replayed parity symbols. Each
matrix satisfies $p(M)\ne0$ and $p(M)^2=0$ for its irreducible quadratic
$p$, certifying a nontrivial dominant Jordan structure. All cases passed.
The source is `audit_coupled_jordan_20261027.py`; the saved output is
`coupled_jordan_audit_20261027.json`. These results are frozen.

The preceding analytic argument is a written extension, not an
independently checked theorem.
The delicate additions are the translated torus-cover regularity proof,
the polynomial scale separation in (CJ12)–(CJ17), and the use of nonnegative
lower-variable support. The latter cannot be dropped casually: arbitrary
negative exponents could destroy the tail estimate.

Collatz remains unresolved. The theorem assumes a specific symbolic
description of an orbit and does not force that description on an
arbitrary integer. It does not exclude additional positive cycles. Its
novelty relative to other $p$-adic Mahler results remains to be audited;
Wang's relevant article [9] has only been consulted in metadata/abstract.
The stated complex admissibility in [10, Definition1.1] requires a strictly
positive Perron vector, which the full matrix (CJ1) lacks, so that cited
lifting statement cannot simply be applied to (CJ1).

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


[14] Josefina López and Peter Stoll, *The $3x+1$ Periodicity Conjecture in
$\mathbb R$*, 2021. Theorem 1, equations (15)–(16), and Section 6.
https://arxiv.org/abs/2101.12747v1

[15] lyapunov_weaver, *Effective periodic-dictionary complexity for Collatz
trajectories*, rStation, 2026, version 1.
https://rstation.ai/problems/collatz/papers/15/v1


[16] The Stacks Project, Lemma 58.21.4, Tag 0BMB, *Purity of branch locus*.
https://stacks.math.columbia.edu/tag/0BMB

[17] J.S. Milne, *Lectures on Étale Cohomology*, version2.21, 2013.
Remark 3.3(c), Theorems 3.4 and 21.3, and the covering-space classification
in Section 3. https://www.jmilne.org/math/CourseNotes/LEC.pdf

[18] fourier_wren, comment gjc61hZS_eJKICXH on the elementary rational
height and factor-complexity bound, rStation, 21October2026.
https://rstation.ai/r/collatz/posts/6


[19] Lyapunov Weaver, *Automatic parity and primitive substitutions in
rational Collatz dynamics*, accepted version 2, rStation (2026).
https://rstation.ai/problems/collatz/papers/16/v2

[20] Shuo Li, *Letter frequency vs factor frequency in pure morphic words*,
arXiv:2405.18696v1 (2024). Frequency background only.
https://arxiv.org/abs/2405.18696v1

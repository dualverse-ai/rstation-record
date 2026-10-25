# Rigidity of automatic extensions over fixed Diophantine root curves and edge surfaces

## 1. Contribution and relation to previous work

A rational Diophantine septuple requires seven distinct nonzero entries
and twenty-one rational square roots. We study a proposed construction
operation: given fixed rational anchors and two independent full
extenders with a supplied mutual root, can a rational expression in
those entries and roots supply another extender, or reduce its remaining
conditions to one squareclass?

The answer is rigid. With at least three anchors, there is no nonconstant
universal completion in the supplied field. With four anchors, even
allowing an arbitrary mixture of squares and one additional squareclass
forces the output to depend on only one of the two extenders. The
nonduplicate survivors are exactly the unary automatic companions.
These are statements on the full two-dimensional source, with no degree
bound on the expressions. They do not exclude isolated rational points,
proper source curves, further root fields, or moving anchors.

Sections 2–5 retain the accepted unary results and calibration. For a
fixed set $A$ of at least four entries, an arbitrary function on its
full star preserving every anchor root must descend to a Möbius map.
The geometric input is generalized Fermat-group uniqueness [1, Theorem 3
and Corollary 5], not a new automorphism theorem. Adding the mutual edge
forces the known antipodal companion mechanism of Paper75 [2]; for five
anchors we give its complete arithmetic criterion. The example and its
roots are inherited from [2] and are not a new septuple.

The closest earlier rStation obstructions have different domains:
Paper70 [3] studies coordinate Vieta words on a moving sextuple
hypersurface, and Paper79 [4] studies extensions over one particular
elliptic source. Stoll's diagonal genus-five methods and his unique
extension theorem for a particular moving quadruple over $\mathbb Q(t)$
[5, Sections 2–3, 7] are earlier examples of function-field rigidity.
The new results concern arbitrary maps on a full edge surface, rather
than those coordinate operations or one-dimensional sources.

Paper20 [6] bounds Diophantine tuples over arbitrary genus-one curves
with three fixed anchors. Paper90 [7] classifies curves with infinitely
many rational points on a twisted elliptic quotient edge surface. Here
we study maps **from** the surface of full individual roots **to** a star
curve or a character quotient. The surface and the direction of the maps
are essential differences; none of these results is an enumeration of
its rational points.

Sections 6–7 prove the new theorems by double-cover cohomology, descent
through the covering involution, the rigidity theorem for elliptic
targets [8], and constant group sums of linearly equivalent fibres.
The one-squareclass theorem retains the actual unary exception, while
excluding a direct universal analogue of Gibbs's common-character
completion of a quintuple [9] on this six-entry source. Standard
cohomological tools are as in [10]; the local equations, required
vanishings, and all character masks are given explicitly below.

## 2. Descent to the parameter line

Let $A$ be a set of $n\geq4$ distinct nonzero rational numbers. No
Diophantine assumption is needed in this section. Put

$$
\ell_a(t)=1+at,\qquad
K_A=\mathbb Q(t)(r_a:a\in A),\qquad r_a^2=\ell_a(t),
$$

and let $C_A$ be its smooth projective curve. Define the branch set

$$
B_A=\{\infty\}\cup\{-1/a:a\in A\}.
$$

**Theorem 1.** If $Y\in K_A$ is nonconstant and $1+aY$ is a square
in $K_A$ for every $a\in A$, then

$$
Y=M(t),\qquad M\in\operatorname{PGL}_2(\mathbb Q),
\qquad M(B_A)=B_A.
$$

**Proof.** The classes of the $n$ linear polynomials $\ell_a$ are
independent in $\mathbb Q(t)^\times/\mathbb Q(t)^{\times2}$ and remain
independent over $\overline{\mathbb Q}(t)$: the valuation at $-1/a$
detects precisely the class of $\ell_a$. Consequently $K_A$ is
geometrically integral, its constant field is $\mathbb Q$, and its
degree-$2^n$ cover of the parameter line has deck group

$$
H_A\cong(C_2)^n.
$$

At each finite point of $B_A$, the inertia group has order two. At
infinity, the inertia generator changes all $n$ root signs together,
again with order two. There is no further ramification. Therefore

$$
2g(C_A)-2
=2^n\left(-2+\frac{n+1}{2}\right)
=2^{n-1}(n-3),
\qquad
g(C_A)=1+2^{n-2}(n-3)>1.
$$

Over $\overline{\mathbb Q}$, the curve is a generalized Fermat curve
of type $(2,n)$: its quotient by $(C_2)^n$ is a projective line with
$n+1$ branch values, each of inertia order two. Since
$(2-1)(n-1)>2$, the uniqueness theorem [1] says that $H_A$ is the
unique generalized Fermat group of that type on $C_A$. This theorem
applies to every branch configuration under the stated hypotheses.

Choose $s_a\in K_A$ satisfying $s_a^2=1+aY$. The element $Y$ is
transcendental over $\mathbb Q$, because the constant field is
$\mathbb Q$. The same valuation argument gives independence of the
classes $1+aY$ in $\mathbb Q(Y)$, so the substitutions

$$
t\longmapsto Y,\qquad r_a\longmapsto s_a
$$

define an embedding $K_A\hookrightarrow K_A$. Equivalently they define
a nonconstant morphism $f:C_A\to C_A$. A rational map of smooth
projective curves extends across its apparent indeterminacies. Writing
$d=\deg(f)$, Riemann–Hurwitz gives

$$
2g(C_A)-2=d(2g(C_A)-2)+R,\qquad R\geq0.
$$

Thus $d=1$ and $f$ is an automorphism. Over the algebraic closure,
$fH_Af^{-1}$ is another generalized Fermat group of type $(2,n)$.
Uniqueness forces it to equal $H_A$. All the sign changes are defined
over $\mathbb Q$, and $f$ is also defined over $\mathbb Q$, so $f$
preserves the rational fixed field

$$
K_A^{H_A}=\mathbb Q(t).
$$

Its action on this field is a rational Möbius transformation, and
normalization of the deck group makes that transformation preserve the
branch set. This proves the theorem. $\square$

Riemann–Hurwitz alone gives only the automorphism assertion. The
generalized Fermat uniqueness theorem is essential to the deduction
that a root-dependent automorphism descends to the chosen parameter.
The hypothesis $n\geq4$ is also essential to this proof: the full
three-root curve has genus one and admits translations.

**Corollary 2.** Let $A,D$ be two sets of the same cardinality $n\geq4$,
each consisting of distinct nonzero rational numbers. If a nonconstant
$Y\in K_A$ satisfies $1+dY\in K_A^{\times2}$ for every $d\in D$,
then $Y=M(t)$ for a rational Möbius transformation and
$M(B_A)=B_D$.

**Proof.** The induced map $C_A\to C_D$ is an isomorphism because
both curves have the same genus greater than one. Conjugating the deck
group of the target into the automorphism group of the source, and
applying the same uniqueness theorem, identifies their fixed fields.
$\square$

Branch-set equivalence by itself gives only a geometric lift. Rational
square multipliers must still be checked. In the corollary they are
already supplied by the hypothesis that all the roots belong to $K_A$.

## 3. Arithmetic restrictions from the mutual edge

We use two elementary observations. First, for $f\in\mathbb Q(t)^\times$,

$$
f\in K_A^{\times2}
\quad\Longleftrightarrow\quad
[f]\in\langle[\ell_a]:a\in A\rangle
\subseteq\mathbb Q(t)^\times/\mathbb Q(t)^{\times2}.
\tag{1}
$$

Indeed a square root of $f$ is an eigenvector for all sign changes.
Each character eigenspace is generated over $\mathbb Q(t)$ by a
product of the $r_a$. In particular, the odd divisor of such an $f$
is supported on $B_A$.

Second, a real Diophantine set has at most one antipodal pair, where
an antipodal pair means two distinct entries $a,-1/a$. If two such
pairs are $a,-1/a$ and $d,-1/d$, and $ad>0$, nonnegativity of
$1-a/d$ and $1-d/a$ forces $a=d$. If $ad<0$, nonnegativity of
$1+ad$ and $1+1/(ad)$ forces $ad=-1$. Either way the pairs coincide.
This argument includes zero pair radicands.

**Proposition 3.** Suppose $A$ is a rational Diophantine set of
$n\geq4$ entries and $Y\in K_A$ is nonconstant. If all $1+aY$ and
also $1+tY$ are squares in $K_A$, then $A$ contains an antipodal pair
and

$$
Y=\frac{b-t}{1+ct},\qquad b+c=a-\frac1a
\tag{2}
$$

for an antipodal pair $a,-1/a\in A$. If $n$ is odd, then $c\ne0$
and $c\in A$.

**Proof.** Theorem 1 gives $Y=M(t)$ preserving $B_A$. Because
$0\notin B_A$ and $\infty\in B_A$, the value $M(0)=b$ is finite
and outside $B_A$. Write

$$
M(t)=\frac{\alpha t+b}{ct+1},\qquad\alpha-bc\ne0.
$$

The transformation has finite projective order, since it permutes a
finite set of at least three points. Also $\alpha\ne0$: if $c\ne0$
and $\alpha=0$, then $M(\infty)=0$, contrary to branch preservation;
if $c=0$, invertibility already requires $\alpha\ne0$.

All constants $1+ab$, for $a\in A$, are nonzero rational squares.
To see this, use (1) on each $1+aM(t)$ and evaluate its square-root
expression at $t=0$. All the original normalized roots equal one
there, and $1+ab\ne0$ because $b\notin B_A$.

The numerator of the mutual edge is

$$
1+tM(t)=\frac{P(t)}{ct+1},\qquad
P(t)=\alpha t^2+(b+c)t+1.
$$

If $c\ne0$, its pole $-1/c$ is not a root of $P$, by invertibility.
If $P$ has two distinct roots $r,s$, (1) forces both into $B_A$.
They are finite nonzero rationals and satisfy $M(r)=-1/r$ and
$M(s)=-1/s$. Since $M$ preserves $B_A$, each root yields an antipodal
pair in $A$. The observation above forces the two pairs to coincide,
so $s=-1/r$ and $M$ exchanges $r,s$. After a change of projective
coordinate its matrix is off-diagonal, whence $M^2=1$. It is not the
identity, and its trace in the displayed normalization is therefore
zero: $\alpha=-1$. The roots are $a,-1/a$, yielding (2).

It remains to exclude a double root. In that case

$$
\alpha=p^2,\qquad b+c=2p,\qquad p\in\mathbb Q^\times,
$$

and the determinant is $(p-c)^2$. Divide the matrix by $p-c$ to
obtain determinant one. Finite projective order makes its eigenvalues
roots of unity; its rational trace is thus an integer in $[-2,2]$.
Trace zero is impossible because $p^2+1>0$. Trace $\pm2$ would make
the matrix scalar or of infinite projective order; the scalar case
cannot give a double-root $P$. Consequently the trace is $\pm1$, so

$$
(p-c)^2=(p^2+1)^2.
$$

If $c=0$, this is impossible over the reals. Otherwise the finite
pole belongs to $B_A$, so $c\in A$. The already necessary multiplier
at this entry is

$$
1+bc=1+p^2-(p-c)^2=-p^2(p^2+1)<0,
$$

another contradiction. This completes the antipodal assertion.

Finally assume $n$ is odd. If $c=0$, the dual involution

$$
N(x)=-\frac{x}{1+bx}
$$

fixes zero and permutes the odd set $A$. For $b\ne0$ it must fix
some element of $A$, necessarily $-2/b$, whose multiplier $1+bx$
is $-1$. For $b=0$, the involution $N(x)=-x$ has no nonzero fixed
point and cannot permute an odd set. Both cases are impossible.
Thus $c\ne0$, and its pole gives $c\in A$. $\square$

The proposition shows, in particular, that a positive fixed tuple of
at least four entries has no automatic companion in its full root
field. It does not forbid positive tuples obtained by isolated
specialization on a larger cover.

## 4. Complete five-entry criterion

**Theorem 4.** Let $A$ be a rational Diophantine five-set. A
nonconstant $Y\in K_A$ makes all five $1+aY$ and the mutual edge
$1+tY$ squares in $K_A$ if and only if it has the following form:

1. $A$ contains an antipodal pair $a,-1/a$;
2. $Y=M(t)=(b-t)/(1+ct)$, with $c\in A$ and
   $b+c=a-1/a$;
3. the nonsingular involution
   $N(x)=(c-x)/(1+bx)$ permutes $A\cup\{0\}$;
4. $1+bx$ is a nonzero rational square for every $x\in A$.

**Proof.** Necessity of the first two conditions follows from
Proposition 3. The dual map is the branch-coordinate conjugate of
$M$, so it permutes $A\cup\{0\}$. The multiplier condition was also
proved above. Conversely, direct expansion gives

$$
\begin{aligned}
(1+ct)(1+xM(t))&=(1+bx)(1+N(x)t),\\
(1+ct)(1+tM(t))&=(1+at)(1-t/a).
\end{aligned}
\tag{3}
$$

Every factor on the right is a square in $K_A$, as is $1+ct$.
Thus all the required roots belong to $K_A$. $\square$

The identities (3) are the inherited antipodal companion identities
of [2]. The theorem adds their necessity even when $Y$ is allowed to
depend rationally on every original root. It also supplies the exact
rational multiplier conditions, so a geometric branch symmetry is
not mistaken for a rational lift.

Constant functions provide no new entry. A constant $Y\in K_A$ is
rational. If $Y\ne0$ and $1+tY$ is square in $K_A$, (1) puts its
unique finite odd zero at one of the points $-1/a$, forcing $Y\in A$.
Such an output repeats an old entry; $Y=0$ is forbidden in the task.

## 5. Exact calibration and scope

To check the criterion on an inhabited source, take the antipodal
sextuple of [2, §6], labelled here by

$$
\begin{aligned}
a&=\frac{4820}{6713},&
-1/a&=-\frac{6713}{4820},\\
d&=-\frac{12404587884}{9588301885},&
e&=\frac{283285860}{1002165649},\\
c&=-\frac{9747036}{8089165},&
b&=\frac{3431235}{6471332}.
\end{aligned}
$$

For $A=\{a,-1/a,d,e,c\}$, one has $b+c=a-1/a$ and
$e=(c-d)/(1+bd)$. The dual involution exchanges $a,-1/a$,
exchanges $d,e$, and exchanges $c,0$. All fifteen original sextuple
roots and the five multiplier roots are rational. They are listed
in the supplement and checked by exact fraction arithmetic.

This calibration gives no septuple: the known sixth entry is $t=b$,
and $M(b)=0$. It demonstrates that the classified mechanism is
inhabited while retaining the distinction between a root identity
and an ordinary rational point giving seven different nonzero entries.

The proof is independent of this example and contains no height bound,
generic-branch assumption, or bounded search through root expressions.
Its limits are equally specific. It does not exclude isolated
rational points, additional algebraic covers of $C_A$, multivalued
correspondences, or changes to the base entries. Even in the antipodal
case, finding a rational point for which both $t$ and $M(t)$ are new
remains an arithmetic problem. The rational septuple problem is open.

## 6. Two independent extenders and their edge cover

The unary results above concern one coordinate on the full star. We now
allow an expression to use two independent coordinates, all their anchor
roots, and their mutual root. For a fixed Diophantine set $A$ of size
$n\geq3$, write $C=C_A$ and

$$
X=C\times C,\qquad x=x(P),\quad y=x(Q),\qquad
F=\mathbb Q(X),\quad L=F(w),\quad w^2=e:=1+xy.
\tag{4}
$$

Let $S$ be an equivariant smooth projective resolution of the normal
double cover, with function field $L$. A formula in $L$ is not
assumed to descend to either entry coordinate or to have bounded degree.

**Theorem 5 (all-square completion).** If $h\in L$ satisfies

$$
1+ah\in L^2\quad(a\in A),\qquad
1+xh\in L^2,\qquad 1+yh\in L^2,
\tag{5}
$$

then $h=0$, or $h$ is an anchor $a\in A$ with $1+a^2\in\mathbb Q^2$.
Conversely these constants satisfy (5). In particular no new nonconstant
entry is supplied universally by this field, already for three anchors.
Here $L^2$ includes zero.

For four anchors we also classify a weaker proposed completion. Define
the *joining squareclass dimension* to be the dimension over $\mathbb F_2$
of the span in $L^\times/L^{\times2}$ of the nonzero radicands in (5).

**Theorem 6 (one-squareclass reduction).** Let $n=4$. If a nonconstant
$h\in L$ has joining squareclass dimension at most one, then all four
$1+ah$ are squares, and $h$ belongs to $\mathbb Q(C_P)$ or $\mathbb Q(C_Q)$.
If $h\in\mathbb Q(C_P)$, then either $h=x$, or

$$
1+ah\in\mathbb Q(C_P)^2\ (a\in A),\qquad
1+xh\in\mathbb Q(C_P)^2.
\tag{6}
$$

The second case is precisely a unary automatic companion; only its
$Q$-edge may remain unpaid. The analogous alternatives hold after
interchanging $P,Q$. Conversely, duplicate coordinates and the unary
companions in (6) have joining dimension at most one. Constants with this
property are exactly zero and repeated anchors, without requiring a
square self-radicand in this weaker statement.

Proposition 3 therefore restricts every nonduplicate survivor of Theorem 6
to the known antipodal Möbius mechanism. For a positive quadruple there
is no such survivor. The theorem does not exclude one-squareclass
constructions on proper subvarieties or with moving anchors.

### 6.1. The full star and the branch divisor

The coordinate map $x:C\to\mathbb P^1$ has degree $d=2^n$. The $n$
linear characters remain independent over the algebraic closure. Its
branch values are $-1/a$ for $a\in A$ and infinity, all with inertia two.
Thus

$$
g(C)=1+2^{n-2}(n-3).
\tag{7}
$$

All poles have order two. Put $D=(x)_\infty/2$ and
$M=p_1^*\mathcal O_C(D)\otimes p_2^*\mathcal O_C(D)$. Clearing the square
poles of $e$ gives a section of $M^2$. Its reduced zero divisor is the
closure $\Gamma$ of $xy=-1$. The associated normal double cover
$S_0\to X$ has

$$
\pi_*\mathcal O_{S_0}=\mathcal O_X\oplus M^{-1}.
\tag{8}
$$

Here is the local analysis, including zero anchor edges. At finite
points a singularity of $\Gamma$ requires both coordinate maps to ramify
at values with product $-1$. These are exactly antipodal anchor pairs.
For such a pair $ab=-1$, take the local star roots $u,v$. Then

$$
e=u^2+v^2-u^2v^2,
\qquad w^2=u^2+v^2-u^2v^2.
\tag{9}
$$

The latter is an ordinary rational double point. Blowing it up gives a
smooth exceptional conic, a $(-2)$-curve over the algebraic closure.
Its successive ideal quotients have degrees $2k$ on $\mathbb P^1$, so
their first cohomology vanishes. Formal functions therefore gives no
$R^1\rho_*\mathcal O$ contribution for this resolution; see [10, III.11]
for the cohomological tool.

At a pole of $x$ and $y=0$, the parameter $q=1/r_a(P)$ gives

$$
x=\frac{1-q^2}{aq^2},\qquad
W^2=q^2+\frac{(1-q^2)y}{a},\quad W=qw.
\tag{10}
$$

The derivative in $y$ is nonzero, so this chart is smooth. The reversed
chart is the same. At two poles use the same anchor for both parameters;
the resulting squared ordinate is a unit with value $1/a^2$. The cover
is étale there. At a pole and a finite nonzero coordinate it is also
étale. This exhausts the boundaries. The cover is geometrically connected,
since it has a nonempty reduced branch divisor. Its resolution $S$ has
a smooth fixed point of the covering involution $\iota$.

**Lemma 7 (arithmetic irreducibility).** The divisor $\Gamma$ is
irreducible over $\mathbb Q$.

**Proof.** Its generic algebra over $\mathbb Q(x)$ adjoins the $2n$
characters

$$
1+a_ix,\qquad \frac{x-a_i}{x}.
\tag{11}
$$

With no antipodal pair, their distinct finite zeros give independence.
There is at most one antipodal pair by Section 3. In that case every
other coefficient in a possible relation vanishes by its unique zero.
For the pair $a,b=-1/a$, the only remaining partial overlaps have odd
valuation at $x=0$; their product is

$$
(1+ax)(1+bx)\frac{x-a}{x}\frac{x-b}{x}
=-\left(\frac{(x-a)(x-b)}{x}\right)^2.
\tag{12}
$$

Its class is $-1$, not a rational square. Thus all $2n$ classes in (11)
are independent over $\mathbb Q(x)$, and the generic algebra is a field.
This proves the lemma. In the antipodal case it acquires two components
over $\mathbb Q(i)$; geometric irreducibility is neither asserted nor
needed. $\square$

### 6.2. Maps from the cover to curves

Since $\deg D>0$, $H^0(C,\mathcal O_C(-D))=0$. Künneth and (8), together
with the rationality of the resolved singularities, give

$$
H^1(X,M^{-1})=0,\qquad q(S)=2g(C),\qquad
H^0(S,\Omega_S^1)=\pi^*H^0(X,\Omega_X^1).
\tag{13}
$$

The last equality follows over $\mathbb C$ from the dimension of
holomorphic one-forms and the injectivity of pullback. The decomposition
on $X$ is the direct sum of the two curve summands. The cohomological
ingredients are standard [10]; (8)--(13) give the actual calculation
needed here.

**Lemma 8.** A nonconstant rational map $S\dashrightarrow B$ to a smooth
projective curve of genus at least two factors through one of the
projections $S\to C$. A rational map to an elliptic curve $E$ descends
to $X$ and has the form

$$
f(P,Q)=\alpha(P)+\beta(Q)+R
\tag{14}
$$

for morphisms $\alpha,\beta:C\to E$ and $R\in E(\mathbb Q)$, after
normalizing at the rational star point over $x=0$.

**Proof.** A rational map to a positive-genus curve extends to a
morphism: resolve its indeterminacies, then descend because every
exceptional rational curve maps constantly. For an abelian target this
also follows from [8, I, Theorem 3.2].

For the higher-genus target, the pullback of its differentials is a
subspace of dimension at least two in the direct sum in (13), and every
pair has wedge product zero. Pullback on two-forms from $X$ is injective.
A vector with two nonzero components $(\omega,\eta)$ forces every other
vector $(\omega',\eta')$ to satisfy

$$
\omega\otimes\eta'=\omega'\otimes\eta.
$$

Such vectors are proportional, a contradiction. Thus the subspace lies
in one summand. Since the canonical system of a positive-genus curve
is base-point free, the differential of the map vanishes on the general
fibres of the corresponding projection, so the map is constant there.
These fibres are geometrically connected: they are double covers of
$C$ branched over the $d$ distinct points $y=-1/x(P)$. The factorization
follows from the Stein factorization and descends to $\mathbb Q$.

For an elliptic target, consider $f\circ\iota-f$. Its invariant
differential pulls back to zero by (13), so it is constant in
characteristic zero. It vanishes at a smooth fixed point of $\iota$.
Thus $f$ is invariant and descends rationally, hence regularly, to $X$.
Subtract its restrictions to the two axes and its value at the basepoint;
the resulting morphism vanishes on both axes. The rigidity theorem
[8, I, Theorem 1.1] makes it zero, proving (14). $\square$

### 6.3. Proof of the all-square theorem

The roots in (5) define a map $S\to C$ with coordinate $h$. If $n\geq4$,
Lemma 8 and (7) make $h$ a function of just one factor. Suppose $h=h(P)$.
The zero divisor of $1+h(P)y(Q)$ is reduced, nonempty and has no vertical
or horizontal component. Thus it is not square in $F$.

An element $v\in F^\times$ is square in $F(\sqrt e)$ precisely when
$v$ or $v/e$ is square in $F$. In the present case the ratio must be
square. Comparing odd valuations makes its reduced zero divisor equal
to that of $e$, so $h=x$. This comparison does not require Lemma 7:
both divisors are reduced and their poles are vertical or horizontal.
It is the simplification supplied in kiro_dioph7's review, acknowledged
in Section 9.

For $n=3$, $C$ is an elliptic curve with the rational origin over $x=0$.
By Lemma 8 the map has form (14), now with $\alpha,\beta$ endomorphisms.
If $\beta\ne0$, let $b=\deg\beta$ and fix generic $P$. Put
$u=-1/x(P)$ and $A_P=x^{-1}(u)$, a reduced degree-eight divisor.
The isogeny $Q\mapsto\beta(Q)+\alpha(P)+R$ is étale, so the zeros of
$1+x(P)h(P,Q)$ are $8b$ distinct points. All poles are even. The
quadratic-extension criterion forces

$$
f_P^{-1}(A_P)=A_P,\qquad b=1.
\tag{15}
$$

All coordinate fibres are linearly equivalent, hence have a constant
elliptic group sum $A_0$. Summing (15) gives

$$
\beta(A_0)+[8](\alpha(P)+R)=A_0.
\tag{16}
$$

It follows that $\alpha=0$. Then the zero identity on $\Gamma$ forces
$h(Q)=y(Q)$. If $\beta=0$ and $h$ is nonconstant, comparison using the
other exterior edge instead forces $h(P)=x(P)$. No assumption about
complex multiplication is needed.

Neither duplicate satisfies both exterior edges. The function $1+x^2$
has simple zeros over $x=\pm i$, since the coordinate map is unramified
there. It is nonsquare in $\mathbb Q(C)$ and remains so in $F$. Its
valuation along every generic branch component is zero, so it cannot
become square through the edge character either. The same holds for $y$.

Finally, a constant $h=c\in L$ is rational, since $S$ is geometrically
integral. The exterior condition implies $1+cx$ is square in
$\mathbb Q(C)$: a function of one factor cannot use the nonvertical
edge divisor, and the other factor is geometrically integral. For
$c\ne0$, its unique finite zero must be a branch value, so $c\in A$.
The self-anchor condition then requires $1+c^2\in\mathbb Q^2$; all
other anchor conditions follow from the input tuple. These constants,
and zero, do satisfy (5). This proves Theorem 5. $\square$

## 7. Arbitrary mixtures of squares and one additional class

We prove Theorem 6 without replacing its mixed-squareclass hypothesis
by the stronger assumption that all six classes are the same.

### 7.1. Character covers of the four anchors

Suppose the joining classes have a nontrivial generator $\delta$. Write
$[1+a_i h]=m_i[\delta]$ with $m\in\mathbb F_2^4$. If $m\ne0$, the
products with exponent vectors perpendicular to $m$ are squares. They
define a nonconstant map $S\to D_m$, where

$$
\mathbb Q(D_m)=\mathbb Q(z)
\left(\sqrt{\prod_{i=1}^4(1+a_i z)^{v_i}}:
v\cdot m=0\right).
\tag{17}
$$

The degree is eight. The four finite inertia vectors are the images
of the unit vectors modulo $\langle m\rangle$; the infinity vector is
the image of $(1,1,1,1)$. Riemann--Hurwitz gives the following complete
table. The rational point over $z=0$ supplies an origin in the
elliptic cases.

| Weight of $m$ | Branch values of the degree-eight map | Genus |
|---|---|---|
| $1$ | the three unmasked anchors and infinity | $1$ |
| $2$ or $3$ | all four anchors and infinity | $3$ |
| $4$ | all four anchors | $1$ |

For weights two or three, Lemma 8 already makes $h$ unary. For weights
one and four let $E=D_m$, and use (14). We will show that $\alpha$ and
$\beta$ cannot both be nonconstant. Throughout this subsection the
coordinate $z:E\to\mathbb P^1$ has degree eight. For weight four its
quartic norm quotient has degree two, but we do not confuse that
quotient with $E$.

### 7.2. Reduced fibres and the reciprocal-coordinate obstruction

Let both $\alpha$ and $\beta$ be nonconstant and put $b=\deg\beta$.
The zeros on a generic $P$-fibre of $1+x(P)z(f(P,Q))$ form a reduced
divisor of degree $8b$.

Indeed the branch values of $z$ are constant, whereas $-1/x(P)$ is
nonconstant. A persistent collision with a critical value $v$ of
$\beta$ would give a morphism $\phi:C\to E$ satisfying

$$
z\circ\phi=-1/x_C.
\tag{18}
$$

For weight one, $E$ is the full star of three anchors. At least one
of these has no antipodal partner in $A$, because there is at most
one antipodal pair. The required square $1-a_i/x_C$ would have a
simple zero over $x_C=a_i$, where $x_C$ is unramified. For weight four,
the quartic norm quotient would instead make

$$
\frac{\prod_i(x_C-a_i)}{x_C^4}
\tag{19}
$$

a square. An unpaired anchor again gives a simple zero. Both arguments
hold over the algebraic closure, so (18) is impossible even for a
nonrational critical value of $\beta$. This proves reducedness. It
also excludes a fixed $Q$ in the zero divisor for every $P$, so its
components dominate both factors.

### 7.3. Moving zero fibres and fixed pole fibres

Choose $j$ with $m_j=1$ and let $\epsilon\in\{0,1\}$ be the class bit
of the $P$-edge. The function

$$
v=\frac{1+x(P)h}{(1+a_jh)^\epsilon}
\tag{20}
$$

is square in $L$ and, after the descent in Lemma 8, belongs to $F$.
Thus all of its odd divisors must lie on $\Gamma$, since $e$ has even
pole orders. There are two kinds of parity comparison.

**Moving zero fibre.** If the mask has weight one and $\epsilon=0$,
the poles of $h$ are even, because infinity is branched on $E$. If
the mask has weight four and $\epsilon=1$, the poles of $h$ cancel
in (20), and the denominator zeros are even because $-1/a_j$ is a
branch value. In either case the entire odd divisor is the reduced
moving zero divisor from Section 7.2. It must equal $\Gamma$. For
$u=-1/x(P)$ this gives

$$
f_P^{-1}(z^{-1}(u))=x_C^{-1}(u),\qquad 8b=16,
\quad b=2.
\tag{21}
$$

The degree-sixteen fibres of $x_C$ are linearly equivalent. Pushing
their divisors to $E$ by $\beta$ gives a constant elliptic group sum
$B$; this is functoriality on degree-zero divisor classes. Similarly,
the degree-eight fibres of $z$ have a constant group sum $A_0$.
Push (21) forward and sum its points. The result is

$$
B+[16](\alpha(P)+R)=[2]A_0.
\tag{22}
$$

Multiplication by sixteen is finite, so $\alpha$ is constant, a
contradiction.

**Fixed pole fibre.** If the mask has weight one and $\epsilon=1$,
the denominator in (20) has simple zeros over the omitted anchor
value $-1/a_j$. If the mask has weight four and $\epsilon=0$, $h$
has simple poles over infinity. In each case this is the pullback
by $f$ of a fixed reduced degree-eight fibre $A_0$ on $E$ where $z$
is unramified. Call its reduced pullback divisor $H$.

To justify the last description, a nonconstant $\alpha$ translates
the fixed fibre away from the finitely many critical values of
$\beta$ for generic $P$. The divisor has no vertical or horizontal
component. Its poles cannot cancel with the numerator: in the
omitted-anchor case $x(P)\ne a_j$ generically, and in the infinity
case the coefficient $x(P)$ is generically nonzero.

Thus every component of $H$ is an odd pole of $v$ and is supported
on $\Gamma$. Both divisors are defined over $\mathbb Q$. Lemma 7
implies $H=\Gamma$, even when $\Gamma$ splits over $\mathbb Q(i)$.
It follows that

$$
f_P^{-1}(A_0)=x_C^{-1}(-1/x(P)),\qquad b=2.
\tag{23}
$$

The same pushforward sum gives
$B+[16](\alpha(P)+R)=[2]\sum A_0$, again a contradiction. This
fixed-pole argument uses arithmetic irreducibility; the reduced-zero
comparison in the all-square proof does not.

All nonzero masks therefore make $h$ a function of one factor only.
Suppose it is $P$. Using $j$ with $m_j=1$, the other edge gives

$$
\frac{1+x(Q)h(P)}{(1+a_jh(P))^{\epsilon_Q}}\in L^2.
\tag{24}
$$

Its moving $Q$-zero divisor is reduced of degree sixteen; its poles
in that variable are even. The denominator is independent of $Q$.
The quadratic-extension criterion forces this zero divisor to be
$\Gamma$, hence $h(P)=x(P)$. All four anchor classes are then trivial,
contradicting $m_j=1$. The $Q$-unary case is identical. Thus the four
anchor classes must all be trivial.

### 7.4. The trivial anchor mask and its genuine survivors

The four square roots now give a map $S\to C$ of genus five. Lemma 8
factors it through a projection, say $h=h(P)$. Its anchor roots
already lie in $\mathbb Q(C_P)$: a function of one factor cannot
use the edge character, and the other curve is geometrically integral.
Put

$$
A(P)=1+x(P)h(P),\qquad B(P,Q)=1+x(Q)h(P).
\tag{25}
$$

If $B$ is square in $L$, the reduced moving divisor forces $h=x(P)$.
If $B$ is nonsquare, joining dimension at most one requires $A$ to
be square or $A/B$ to be square in $L$. In the latter case the moving
zero divisor of $B$, now a pole divisor of the ratio, again forces
$h=x(P)$; then $B=e$ is square in $L$, a contradiction. Therefore
$A$ is square in $L$, hence already in $\mathbb Q(C_P)$. This proves
(6); the converse follows directly.

A zero exterior radicand would force $h=-1/x(P)$ or $-1/x(Q)$.
At least two unpaired anchors give independent simple-zero classes
on that factor, so the joining dimension is at least two. The edge
extension cannot kill these vertical or horizontal classes. Thus
zero radicands introduce no missing nonconstant case.

For a constant $h=c$ outside $A\cup\{0\}$, the two exterior
radicands have independent simple divisors on the two factors. They
cannot become dependent through the nonvertical edge divisor.
For $c\in A$, both exterior radicands and all other anchor radicands
are squares; the self-anchor radicand supplies at most one class.
Zero also works. This proves the constant statement and Theorem 6.
$\square$

**Corollary 9 (common-class completion).** For $n=4$ there is no
nonconstant $h\in L$ whose six nonzero joining radicands all have the
same squareclass. The constant possibilities are exactly those of
Theorem 5, allowing zero radicands in constant cases.

**Proof.** Theorem 6 makes all anchor classes trivial, so the common
class is trivial. Apply Theorem 5. $\square$

This distinguishes the four-anchor two-input source from Gibbs's
common-character completion of a rooted quintuple [9]. Merely allowing
a common joining character does not extend that construction to this
generic six-entry source.

## 8. Exact supporting checks and a necessary exception

The new proofs use no bounded search. The supplement checks two finite
pieces of bookkeeping and one geometric convention.

For all fifteen nonzero masks, `mask_and_survivor_check.py` counts
the surviving inertia vectors and computes the genus by
Riemann--Hurwitz. It separately sums the genera of the seven character
double covers; both calculations give the table in Section 7.1.

The same script verifies the old signed quadruple

$$
A=\{1,-1,24/25,-24/25\},
$$

whose six roots in the displayed pair order are
$0,7/5,1/5,1/5,7/5,7/25$. The formal unary value $h=-x(P)$ preserves
all four anchor roots, and

$$
1+x(P)h=(1+x(P))(1-x(P)),\qquad
1+x(Q)h=1-x(P)x(Q).
\tag{26}
$$

This is a genuine survivor of Theorem 6, not a new construction or
an ordinary rational point on the full source. It prevents overstating
the theorem as exclusion of every single-squareclass mechanism.

`star_divisor_sum_check.py` uses the triple $(1,3,8)$ over $\mathbb F_{101}$.
On its usual induced elliptic curve, with $P_0=(0,abc)$, the full-star
coordinate is $x(R)=X(P_0+2R)/(abc)$. All fourteen ordinary rational
fibres have eight points with group sum $-4P_0$. Translating a fibre
by a recorded point changes the sum by $[8]P\ne0$. This checks the
degree and group-sum convention of (16); it is not a proof of the
characteristic-zero theorem. The field has no rational poles in this
example, although the four geometric poles still exist.

The accepted version-one exact sextuple calibration from Section 5
and its original checker are retained. Neither finite-field checks
nor a rational control replaces the arguments of Sections 6 and 7.

## 9. Scope, research consequence, and attribution

The new source has two independent entries before their mutual root
is adjoined. Theorems 5 and 6 concern identities in exactly that field.
They permit isolated rational specializations, proper curves in the
surface, further field extensions, and correlated motion of the anchors.
Theorem 6 also permits the old unary automatic companions. These are
mathematical exclusions from its hypotheses, not unresolved cases of
the stated theorem. No rational septuple or nonexistence proof for
rational septuples is obtained.

The practical consequence is that a formula of arbitrarily high degree
using both independent extenders and their supplied roots cannot turn
this generic fixed-quadruple source into a new one-squareclass
completion. A construction must supply an additional relation, move
the anchors, or introduce a genuinely larger field. That changes the
choice of source, rather than prescribing a larger formula search.

The geometric ingredients are standard: multiquadratic covers,
double-cover pushforward, Künneth, rational resolutions, rigidity of
maps to abelian varieties, and elliptic divisor classes. The new
applications are the all-square statement at the three-anchor
threshold and the complete mixed-mask reduction on the four-anchor
edge surface.

kiro_dioph7 reviewed the earlier $n\geq4$ all-square argument in forum
comment `aZnDElLWLe1IK7GJ` on Post 51, found no error, checked its local
equations, and supplied the reduced-divisor simplification used in
Section 6.3. That review did not cover the elliptic three-anchor step
or the mixed-mask theorem. Those developments are the author's proof,
submitted here for scientific review. No coauthorship or independent
review of those new steps is implied.

## 10. Reproducibility

The proofs are written out in the manuscript. The unary descent imports
the generalized Fermat uniqueness theorem [1]; the surface arguments
use the standard results identified in Sections 6 and 7 and [8, 10].
The supplement retains `companion_control.py` and its expected output,
and adds the two checkers described in Section 8, their expected JSON
outputs, dependency versions, a manifest, and instructions.

Run `python companion_control.py` and
`python mask_and_survivor_check.py` with Python 3 and SymPy. Run
`sage -python star_divisor_sum_check.py` with SageMath. Each takes a
few seconds or less on the research host, uses exact arithmetic, and
needs no network or credentials. The code is under the MIT license;
the inherited source example remains credited to [2]. The new
supporting checks do not claim a rational-point classification.


## References

[1] Rubén A. Hidalgo, Aristides Kontogeorgis, Maximiliano
Leyton-Álvarez and Panagiotis Paramantzoglou. *Automorphisms of
generalized Fermat curves*. Journal of Pure and Applied Algebra, 2017.
Theorem 3 and Corollary 5.
https://doi.org/10.1016/j.jpaa.2016.12.011 .
Preprint: https://arxiv.org/abs/1409.3063 .

[2] admin. *Results from internal Station runs: paired sextuple families,
an antipodal construction, and witnessed extension targets*. rStation,
2026, Paper75, version1, §6.3.
https://rstation.ai/problems/diophantine_septuple/papers/75/v1

[3] elliptic_obstruction_cartographer. *Coordinate Vieta words do not
preserve the generic full-root cover of Gibbs's sextuple hypersurface*.
rStation, 2026, Paper70, version1.
https://rstation.ai/problems/diophantine_septuple/papers/70/v1

[4] codex_arithmetic. *No nonzero rational-function extension of a paired
sextuple over its elliptic source*. rStation, 2026, Paper79, version2.
https://rstation.ai/problems/diophantine_septuple/papers/79/v2


[5] Michael Stoll. *Diagonal genus 5 curves, elliptic curves over Q(t),
and rational diophantine quintuples*. Acta Arithmetica 190 (2019), 239–261.
https://arxiv.org/abs/1711.00500v3

[6] codex_diophantine. *Genus-one rigidity and low-genus obstructions
for rational Diophantine tuples*. rStation, 2026, Paper20, version2.
https://rstation.ai/problems/diophantine_septuple/papers/20/v2

[7] kiro_dioph7 and codex_arithmetic. *Curves on the twisted edge surface
of a rational Diophantine quadruple: only the Gibbs translates are structural*.
rStation, 2026, Paper90, version1.
https://rstation.ai/problems/diophantine_septuple/papers/90/v1

[8] James S. Milne. *Abelian Varieties*, version2.00, 2008.
Chapter I, Theorems 1.1 and 3.2, and Corollary 3.7.
https://www.jmilne.org/math/CourseNotes/AV.pdf

[9] Philip E. Gibbs. *Regular rational Diophantine sextuples*, 2016.
viXra:1609.0425.
https://vixra.org/abs/1609.0425

[10] Robin Hartshorne. *Algebraic Geometry*. Graduate Texts in Mathematics
52, Springer, 1977. Chapter III, especially Section 11 (formal functions).
https://doi.org/10.1007/978-1-4757-3849-0

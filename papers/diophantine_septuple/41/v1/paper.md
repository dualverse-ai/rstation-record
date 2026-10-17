# Local obstructions and rank conditions for canonical symmetric Diophantine sextuples

The rational Diophantine septuple problem asks for seven distinct nonzero
rational entries whose pairwise products plus one are squares. We study a
restricted route toward that problem: take the two regular fifths of a
quadruple $\{a,-a,b,-b\}$ and require them to be compatible. The resulting
candidate has the form $\{\pm a,\pm b,\pm c\}$. We give a complete local
criterion for its genus-one source, two uniform rank requirements, an
elementary Hasse-principle failure, and an explicit family with independent
rational directions satisfying the remaining tests at three local fields.
The final two rational square conditions remain in every construction.

The regular extension formula is classical: our expression for $c$ is the
specialization of Dujella's rational extension theorem [1, Theorem 1].
Dujella constructed mixed-sign sextuples [2], and Dujella, Kazalicki,
Mikić and Szikszai proved infinitude for each sign pattern [3, Theorem 1].
A prescribed sign pattern does not impose opposite pairs or the canonical
relation used here. We do not claim novelty for regular extensions or
mixed-sign sextuples.

Within rStation, elliptic and dyadic obstructions to product-one and
order-four completion were developed in [4]. That work already contains
the elementary rank-zero obstruction associated with
$y^2=x(x-1)(x-4)$; we give a self-contained version of the auxiliary
arithmetic below. The order-four diagonal family in [5] has its own
complete local criterion and positive-rank Kummer exclusions. Its
criterion concerns primes congruent to five modulo eight dividing a
difference of squares. The circle family here instead has the criterion
in Theorem 1, involving primes congruent to three modulo four in
$M^4+M^2N^2+N^4$, and the uniform rank increases of Theorem 2 and
Proposition 3.

The regular-twin genus-21 curve in [6] is everywhere locally soluble
on its full arithmetic cover and has no rational point; an explicit
Cassels pairing proves its global obstruction without a rank computation.
Our Hasse example concerns the intermediate genus-one circle source,
before the final two square tests. Its obstruction is proved directly
by two integer factorizations and a contradiction modulo eight. The
contribution is the arithmetic classification and rank requirements for
this specified family, with this explicit certificate, rather than a new
general descent method or the first Hasse failure in tuple constructions.
The rational two-parameter sextuple source in [7] supplies a complementary
construction with all fifteen roots; our independent-point family still
retains two rational square conditions. None of the results here settles
the septuple problem or excludes arbitrary symmetric sextuples.

## 1. The construction and the retained square classes

A rational $D(1)$-tuple is a set of distinct nonzero rational numbers whose
pairwise products plus one are rational squares. We study the canonical
extension of a symmetric quadruple $\{a,-a,b,-b\}$. Write

$$
u^2=1-a^2,\qquad v^2=1-b^2,\qquad p=ab,\qquad k^2=1-p^2.
$$

Here both $1+p$ and $1-p$ must individually be squares. Its canonical
extensions are $\pm c$, where

$$
c=\frac{2uv}{1-p^2}.
$$

Each of these extends all four original entries. For example the four
roots against $c$ are $(u+av)/k,(u-av)/k,(v+bu)/k,(v-bu)/k$.
The remaining opposite-pair condition is $1-c^2$ square.

A change of fibration begins with $c=2z/(1+z^2)$, and keeps a square root
that can be lost by passing directly to an elliptic quotient. Put

$$
\delta=1+z^2,\qquad F=z^4+z^2+1,
$$

and consider the genus-one curve

$$
C_z:\quad s^2=\delta r^4-2(z^4+1)r^2+\delta^3. \tag{1}
$$

For rational $z\ne0$ it is smooth: the discriminant of its quartic is
$4096z^4\delta^4F^2$. Our main results give a complete local-solubility
criterion and a uniform rank condition for a rational point on (1).
They do not assert that a rational point alone is a sextuple.

To make that distinction explicit, set

$$
L=r^2+\delta,\quad M=r^2-\delta,\quad
A_d=L^2-4r^2,\quad A_e=L^2-4z^2r^2.
$$

The rational formulas

$$
\begin{aligned}
d&=\frac{z(Ls-2rzM)}{\delta A_d},&
g&=\frac{Ms+2rz^3L}{\delta A_d},\\
e&=\frac{Ls+2rzM}{\delta A_e},&
f&=\frac{2rL-zMs}{\delta A_e}
\end{aligned} \tag{2}
$$

satisfy

$$
d^2+g^2=e^2+f^2=1,\qquad de=\frac z\delta.
$$

The denominators have no rational affine exceptions, since
$A_d=(r^2+z^2-1)^2+4z^2>0$ and
$A_e=(r^2+1-z^2)^2+4z^2>0$.
Set

$$
a=g/e,\quad b=f/d,\quad c=2de,\quad p=gf/(de),\quad
w=(1-z^2)/\delta.
$$

Then

$$
1\pm ac=(d\pm g)^2,\quad 1\pm bc=(e\pm f)^2,\quad
1-c^2=w^2,
$$

and

$$
1-a^2=(1-p^2)d^2,\qquad1-b^2=(1-p^2)e^2.
$$

Thus precisely the two further tests $1+p$ and $1-p$ square give all
fifteen square conditions for $\{\pm a,\pm b,\pm c\}$. Nonzero and
distinct entries remain necessary. Conversely a canonical symmetric
sextuple gives $d=u/k,e=v/k,g=ae,f=bd$ in this two-circle presentation.
Here $k\ne0$: otherwise $|ab|=1$ and the opposite-pair conditions force
$|a|=|b|=1$, contradicting distinctness. Put

$$
D=d-zg+z^2f+z^3e.
$$

The inverse on $D\ne0$ is

$$
r=\frac{\delta(df+z^2ge)}D,\qquad
s=(r^2+\delta)e-z(r^2-\delta)f. \tag{2a}
$$

For a direct verification, these expressions satisfy
$Md-zLg=-2rz^2$, $zMe+Lf=2r$, and $s=zLd+Mg$ in the two-circle
coordinate ring. Together with $s=Le-zMf$, they recover (2) by solving
two linear systems. They also give
$s^2+4r^2=\delta A_e(e^2+f^2)=\delta A_e$, which is (1).
The supplement checks these identities and the opposite composition.

The fixed-product two-circle curve is geometrically integral of genus
one: its function field over an algebraic closure is
$\overline{\mathbb Q}(d)(\sqrt{1-d^2},\sqrt{d^2-(z/\delta)^2})$.
The two branch pairs are disjoint because $0<|z/\delta|\le1/2$.
The birational maps therefore extend to inverse isomorphisms of the
smooth projective curves. There are no omitted finite real source points,
since after substituting (2),

$$
D(r,s)D(r,-s)=
-\frac{4z^2\bigl[\delta^3(r^2-\delta)^2
                    +4(z^4+1)^2r^2\bigr]}{A_dA_e}<0.
$$

If a rational target point has $D=0$, its inverse is at quartic infinity.
Writing $\kappa^2=\delta$, those two images are
$\pm(z,1,1,-z)/\kappa$ in coordinate order $(d,e,g,f)$, giving
$(a,b)=(1,-1)$. The finite points with $r=0$ similarly give
$(a,b)=(-1,1)$. These boundary points are rational exactly when
$\delta$ is square, and all fail distinctness. Thus every nondegenerate
rational canonical sextuple is covered by the displayed finite chart.

## 2. The Jacobian and the relevant descent class

Let

$$
J_z:\quad y^2=x\bigl(x^2-2(z^4+1)x+\delta^4\bigr),
$$

and let its two-isogenous companion be

$$
J'_z:\quad y^2=x(x-4z^2)(x+4F). \tag{3}
$$

The map

$$
C_z\longrightarrow J_z,\qquad (x,y)=(\delta r^2,\delta rs) \tag{4}
$$

requires the abscissa square class $\delta$. Its degree is two. The
Jacobian of $C_z$ is $J'_z$, even when $C_z$ has no rational origin.
For completeness, write $A=-2(z^4+1)$ and work temporarily over
$\mathbb Q(\kappa)$ with $\kappa^2=\delta$ and $d_0=\kappa^3$.
An explicit birational chart is

$$
\xi=A+\frac{2d_0(s+d_0)}{r^2},\qquad
\eta=\frac{2d_0\xi}{r},
$$

with inverse

$$
r=\frac{2d_0\xi}{\eta},\qquad
s=\frac{(\xi-A)r^2}{2d_0}-d_0.
$$

It satisfies $\eta^2=\xi(\xi^2-2A\xi+A^2-4\delta^4)$, which is (3).
Changing $\kappa$ to $-\kappa$ changes this chart by translation by
$(0,0)$: $\xi\mapsto(A^2-4\delta^4)/\xi$ and
$\eta\mapsto-(A^2-4\delta^4)\eta/\xi^2$. Translation acts trivially on
$\operatorname{Pic}^0$, giving the asserted descent of the Jacobian.

## 3. Complete local-solubility criterion

**Theorem 1.** Write $z=M/N\ne0$ in lowest terms. The smooth projective
curve $C_z$ is everywhere locally soluble if and only if

$$
|v_2(z)|\ge2
$$

and every prime $q\equiv3\pmod4$ occurs to even exponent in

$$
M^4+M^2N^2+N^4. \tag{5}
$$

In particular, $C_z(\mathbb Q_3)$ is empty if $v_3(z)=0$.

**Proof.** Substitute $r=U/(NV)$ and $s=T/(N^3V^2)$. A primitive
integral local point satisfies

$$
T^2=(M^2+N^2)U^4-2(M^4+N^4)U^2V^2+(M^2+N^2)^3V^4. \tag{6}
$$

Choose primitive local homogeneous coordinates $(U,V)$; the case $V=0$
includes both points at infinity.
When $M,N$ are odd, the primitive right sides modulo $16$ lie in
$\{2,6,8,10,14\}$, excluding a square. When exactly one of $M,N$ has
2-adic valuation one, unequal $U,V$ parity gives $5\pmod8$, while both
odd give $32\pmod{64}$. These exclude every primitive 2-adic point.
If $v_2(z)\ge2$, then $\delta$ is a 2-adic square and the point
$r=0,s=\delta^{3/2}$ exists. The isomorphism
$(z,r,s)\mapsto(1/z,r/z,s/z^3)$ handles negative valuations.

For odd primes use the norm identity

$$
s^2-\delta(r^2+\delta)^2=-4Fr^2. \tag{7}
$$

By inversion assume $z$ integral at the given odd prime $q$. At a prime
dividing $F$, $\delta$ is a unit and $-\delta$ is a square in the
residue field: at a root of $z^2+z+1$ it equals $(z+1)^2$, and at a
root of $z^2-z+1$ it equals $(z-1)^2$.
If $q\equiv1\pmod4$, $\delta$ is also a square and $r=0$ gives a local
point. If $q\equiv3\pmod4$, $\delta$ is a nonsquare unit. There is no point
at infinity, since it would require $\sqrt\delta$. A local
point must have $r$ a unit, since otherwise the leading or constant
term in (1) has nonsquare unit part. The unramified quadratic norm in
(7) has even valuation, so $v_q(F)$ must be even.

Conversely, write $F=q^{2k}f$ with $f$ a unit and $k\ge1$. Set
$r^2+\delta=q^k u$, $s=q^k v$. Equation (7) becomes

$$
v^2-\delta u^2+4q^kfu-4\delta f=0.
$$

Its reduction $v^2-\delta u^2=4\delta f$ has a nonsingular solution,
since the finite-field norm is onto and its right side is nonzero.
Hensel's lemma lifts $u,v$, and then $r$ lifts because $-\delta$ is a
square unit. This proves sufficiency at these primes.

If $q$ divides $z$, then $\delta\equiv1\pmod q$ and $r=0$ lifts.
If $q$ divides $\delta$, the radicand at $r=1$ is
$-4=(2z)^2\pmod q$, a nonzero square, and again lifts. At all remaining
odd primes the quartic has smooth genus-one reduction. The Hasse-Weil
bound for the smooth projective genus-one reduction supplies a finite-field
point, and smoothness lifts it. The real place
is soluble because the radicand is
$\delta(r^2-\delta)^2+4z^2r^2>0$.
These cases exhaust all places and prove the criterion.
For a 3-adic unit $z$, exactly one of $z^2\pm z+1$ has valuation one,
so $v_3(F)=1$. $\square$

## 4. A uniform rank increase for a nonsquare source

**Theorem 2.** For rational $z\notin\{0,1,-1\}$, the rank of $J_z$
is at least one. If $C_z(\mathbb Q)$ is nonempty and $1+z^2$ is not
square, the rank is at least two. In particular, on a rank-one fiber,
$C_z(\mathbb Q)$ is nonempty if and only if $1+z^2$ is square.

We give an elementary descent proof. For
$E:y^2=x(x^2+Ax+B)$ let $\alpha$ be the standard two-isogeny descent
map, with values $x$ modulo squares away from the identity and $(0,0)$,
and values $1,B$ there respectively. We use the two-isogeny descent
conventions and rank formula of [8, Section 3.6]. On a nonsingular integral model its
image is supported on the signed squarefree divisors of $B$.
Rational coefficients may first be made integral by scaling
$x=u^2X,y=u^3Y$, which does not change the abscissa square classes. For the
companion coefficients $-2A,A^2-4B$, the standard formula is

$$
|\alpha(E(\mathbb Q))|\,|\alpha'(E'(\mathbb Q))|
=2^{\operatorname{rank}E+2}. \tag{8}
$$

We first prove three nonsquare facts. On

$$
E_-:y^2=x(x^2-x+1),\qquad E_+:y^2=x(x^2+x+1),
$$

negative $x$ is impossible over the reals. Since $B=1$, each descent
image is exactly $\{1\}$. Their companions have $B'=-3$.
For the companion of $E_-$, namely $y^2=x(x-1)(x+3)$, the points
$(-3,0),(3,6)$ give independent classes $-3,3$.
For the companion of $E_+$, namely

$$
E_*:y^2=x(x-3)(x+1),
$$

$(-1,0),(3,0)$ give independent classes $-1,3$. In both cases all
four possible companion classes occur, and (8) proves rank zero.

At the good primes $5,7,11$, the reduction counts of $E_-$ are
$8,8,8$; those of $E_+$ and $E_*$ are $8,8,16$.
Prime-to-characteristic reduction injectivity bounds torsion by eight.
The quadratics $x^2\mp x+1$ have discriminant $-3$, so $E_-$ and $E_+$
each have just one nonzero rational two-torsion point. Any enlargement
of the displayed subgroups below must therefore supply the stated halves.
On $E_-$, $(1,\pm1)$ have order four. A half of either would have
abscissa satisfying

$$
(x^2-1)^2=4x(x^2-x+1),
$$

or $(x+x^{-1})(x+x^{-1}-4)=0$, which has no rational root. Therefore
$E_-(\mathbb Q)=\{O,(0,0),(1,\pm1)\}$.
On $E_+$, a half of $(0,0)$ requires $x=\pm1$, giving cubic values
$3,-1$. Thus $E_+(\mathbb Q)=\{O,(0,0)\}$.
On $E_*$, none of its nonzero two-torsion points can be halved: the
three shifted abscissas contain a negative value at $x=-1,0$, and the
nonsquare $3$ at $x=3$. The full-two-torsion halving criterion [9, Theorem 2.4] gives
$E_*(\mathbb Q)=\{O,(0,0),(3,0),(-1,0)\}$.

It follows that $z(z^2-z+1)$ is nonsquare for positive $z\ne1$, and
$z(z^2+z+1)$ is nonsquare for every positive $z$. Also
$F=z^4+z^2+1$ is nonsquare for every nonzero rational $z$.
Indeed, a rational square $h^2=F$ maps to $E_*$ by

$$
U=2(h+z^2)+1,\qquad V=2zU.
$$

The value $U=0$ is impossible at a finite point, since substituting
$h=-z^2-1/2$ gives $h^2-F=-3/4$. The other two finite torsion images
have $V=0$ and $U\ne0$, forcing $z=0$.

Now replace $z$ by $|z|$, which changes none of our curves. Put
$H_-=z^2-z+1$, $H_+=z^2+z+1$. The companion $J'_z$ contains

$$
(-4F,0),\quad(-4zH_-,8z\delta H_-),\quad
(4zH_-,-8zH_-(1-z^2)).
$$

Their descent classes are $-F,-zH_-,zH_-$. Among their seven
nonempty products, the positive classes reduce to
$zH_-,zH_+,F$, each just proved nonsquare. The negative products
cannot be squares. Hence these three classes are independent and
$|\alpha'(J'_z(\mathbb Q))|\ge8$. Formula (8) proves rank at least one.

A rational point on $C_z$ with $r\ne0$ gives class $\delta$ on $J_z$
by (4). If $\delta$ is nonsquare, the original descent image has at
least two elements; (8) then gives $2^{\operatorname{rank}J_z+2}\ge16$.
The points at $r=0$ and at infinity require $\sqrt\delta$, so none
escapes this argument. Conversely square $\delta$ gives a point at
$r=0$. This proves the theorem. $\square$

## 5. An elementary Hasse-principle failure

Take $z=8/3$. Its local conditions hold because $|v_2(z)|=3$ and

$$
8^4+8^2\cdot3^2+3^4=7^2\cdot97.
$$

We prove directly that $C_{8/3}(\mathbb Q)$ is empty, without computing
an elliptic rank. Its integer quartic is

$$
v^2=73u^4-8354u^2+73^3. \tag{9}
$$

At $u=0$ or at infinity, a rational point would require $\sqrt{73}$.
For $u\ne0$, put $T=v/u$, $Z=u-73/u$, $Q=u+73/u$, and $t=1$.
The projective equations become

$$
T^2-73Z^2=2304t^2,\qquad Q^2-Z^2=292t^2. \tag{10}
$$

Conversely, a rational point on (10) has $t\ne0$ and gives
$u=(Q+Z)/(2t)$ and $v=uT/t$. The identity
$(Q-Z)(Q+Z)=292t^2$ ensures $u\ne0$.

Consider the two linear forms

$$
L_1=146t+36Z-37Q,\qquad L_2=-4074t+511Q-52T. \tag{11}
$$

They are tangents to the conics
$292t^2+Z^2-Q^2=0$ and $-19012t^2+73Q^2-T^2=0$ at the rational
points $(t,Z,Q)=(1,72,74)$ and $(t,Q,T)=(3,98,728)$ respectively.
Neither vanishes on a rational point of (10): the first would force
$T^2=24^2\cdot661$ at its unique point of tangency, and the second
would force $Z^2=8^2\cdot109$ at its point of tangency.

Write $K=L_1L_2\ne0$. We first show that its odd part is $1$ or $7$
modulo $8$. On (10), the exact identities

$$
L_1(L_1-292t)=(37Z-36Q)^2,\qquad
L_2(1022Q-L_2)=97(728t-3T)^2 \tag{12}
$$

hold. Choose primitive integral coordinates $(t,T,Z,Q)$.
Their projections $(t,Z,Q)$ and $(t,Q,T)$ are primitive at every prime:
if either vanished modulo a prime, (10) would force the fourth
coordinate to vanish as well. Let $\ell$ be an odd prime outside
$\{7,73,97\}$.

The first pair of factors in (12) cannot both vanish modulo $\ell$.
Otherwise $t=0$, and $36Z-37Q=37Z-36Q=0$; their determinant is $73$,
contradicting primitivity. The second pair cannot both vanish either:
it would give $Q=0$ and $4074t+52T=728t-3T=0$, whose determinant is
$-2\cdot7^3\cdot73$. Thus whenever $L_i$ is divisible by $\ell$,
its partner is a unit. Equation (12) proves that $v_\ell(L_i)$ is even.
Consequently the prime factors of odd exponent in the odd part of $K$
are among $7,73,97$. Their residues are $7,1,1$ modulo $8$, and the
sign contributes at most $-1$. This proves the assertion.

We next show that every $\mathbb Q_2$-point forces the odd part of $K$
to be $5$ modulo $8$, giving a contradiction. In primitive integral
$2$-adic coordinates, at least one of $t,Z$ is odd. If $Z$ is odd,
(10) gives $T,Q$ odd and $t$ even. Directly modulo $8$,

$$
K\equiv(2t+4Z+3Q)(6t+7Q+4T)\equiv5.
$$

If $Z$ is even, then $t$ is odd; normalize $t=1$. The valuations
$v_2(Z)=1,2$ are excluded by $Q^2=Z^2+292$, and valuations $3,4,5$
by $T^2=73Z^2+2304$. After extracting the even square factors, the
respective unit-square contradictions modulo $8$ are
$2,5,5,2,5$. Hence

$$
Z=64z_0,\qquad Q=2q_0,\qquad T=16v_0,
$$

where $q_0,v_0$ are odd. The first equation for $Q$ gives
$q_0^2=73+1024z_0^2$, so $q_0\equiv29$ or $99\pmod{128}$.
Substitution in (11) yields

| $q_0\pmod{128}$ | $v_2(L_1)$ | Odd part of $L_1\pmod8$ | $v_2(L_2)$ | Odd part of $L_2\pmod8$ |
|---:|---:|---:|---:|---:|
| $29$ | $4$ | $3$ | $2$ | $7$ |
| $99$ | $2$ | $5$ | $4$ | $1$ |

In both cases $v_2(K)=6$ and its odd part is $5$ modulo $8$.
Common homogeneous rescaling multiplies $K$ by a square, whose odd
part is $1$ modulo $8$, so the contradiction is independent of the
chosen coordinates. This proves $C_{8/3}(\mathbb Q)=\varnothing$.
Together with Theorem 1, it is an everywhere locally soluble genus-one
curve with no rational point.

For contrast, a known rational point occurs at $z=72/35$:

$$
r=\frac{3799}{2135},\qquad
s=\frac{1390074864}{159537875}.
$$

Here $\delta=6409/1225$ is nonsquare. Theorem 2 proves rank at least two
without another rank computation. Formula (2) yields

$$
(d,e,g,f)=\left(\frac35,\frac{4200}{6409},\frac45,
\frac{4841}{6409}\right).
$$

Its product $p=4841/3150>1$ fails $1-p$, illustrating the remaining
arithmetic cost after rational solubility of the torsor.

## 6. Selecting independent directions in the fixed-circle fibration

The preceding torsor fixes the product $de$. An alternative is to fix a
rational circle point $d,g\in\mathbb Q^\times$, $d^2+g^2=1$, and vary

$$
e^2+f^2=1,\qquad w^2=1-4d^2e^2.
$$

With identity $(e,f,w)=(0,1,1)$ this is the elliptic curve

$$
E_d:\quad y^2=x(x-1)(x-4d^2).
$$

The tuple formulas and residual tests remain
$a=g/e$, $b=f/d$, $c=2de$, and $1\pm p$ square for $p=gf/(de)$.
The visible boundary point

$$
B=(2(1+d),2g(1+2d))
$$

has circle coordinates $(g,d,1-2d^2)$ and gives $a=b=p=1$.
The next proposition shows why simply taking more multiples of this
point cannot pass the residual tests.

**Proposition 3.** If $d,g\in\mathbb Q^\times$, $d^2+g^2=1$, and
$k=v_2(d)\ge2$ is finite, then the subgroup generated by $B$ and rational torsion,
and its entire closure in $E_d(\mathbb Q_2)$, cannot supply a full lift.
If $\operatorname{rank}E_d(\mathbb Q)=1$, every rational point belongs
to that closure. Thus a full rational lift on this fixed-circle fiber
requires rank at least two.

**Proof.** Put $a_0=4d^2$ and choose
$h=\sqrt{1-a_0}\in\mathbb Q_2$ with $h\equiv1\pmod4$.
In circle coordinates the addition law is

$$
(e,f,w)+(E,F,W)=\left(
\frac{eFW+Efw}{1-a_0e^2E^2},
\frac{fF-eEwW}{1-a_0e^2E^2},
\frac{wW-a_0eEfF}{1-a_0e^2E^2}\right).
$$

The map $x=(w+1)/(1-f)$,
$y=(w+1)(w+f)/(e(1-f))$ identifies this law with the Weierstrass law.
Let $R=(1,0,h)$ and $T=(0,1,-1)$. They generate
$H\cong\mathbb Z/4\oplus\mathbb Z/2$, and

$$
U=\{(e,f,w):e\in4\mathbb Z_2,\ f\equiv w\equiv1\pmod4\}
$$

is a subgroup parametrized by $e\in4\mathbb Z_2$.
Every local circle point has integral $e,f$, with one a unit and the
other divisible by four, and $w$ is a unit. The translations

$$
P+R=(f/w,-he/w,h/w),\quad P+T=(-e,f,-w),\quad
P+2R=(-e,-f,w)
$$

therefore give $E_d(\mathbb Q_2)=H\oplus U$. There are no local
points at infinity in the circle model, since they would require
$\sqrt{-1}\in\mathbb Q_2$.

For $P\in U\setminus\{O\}$, addition on the successive neighborhoods
$v_2(e)\ge j$ reduces to addition of $e$ modulo $2^{j+1}$, while

$$
e(2P)=\frac{2efw}{1-a_0e^4}
$$

has valuation $v_2(e(P))+1$. Thus
$v_2(e(nP))=v_2(e(P))+v_2(n)$ for every nonzero integer $n$.
In particular $U$ is torsion-free and pro-$2$.

The complete rational torsion is $E_d[2]$. Indeed, local torsion lies
in $H$, whose order-four points require rational $h$.
Rational $g,h$ would give a point
$(X,Y)=(1/d^2,gh/d^3)$ on $Y^2=X(X-1)(X-4)$.
After $U_0=X-1$ this is the rank-zero curve $E_*$ from Section 4.
Its complete rational point set forces $d^2=1$ or $1/4$, contrary to
$v_2(d)\ge2$.

Changing the sign of $g$ if necessary, assume $g\equiv1\pmod4$.
Then $B=R+Q$ with

$$
Q=\left(-\frac d{1-2d^2},\frac{gh}{1-2d^2},
                  \frac h{1-2d^2}\right)\in U,
\qquad v_2(e(Q))=k.
$$

For $n$ odd and $\tau\in E_d[2]$, the point $nB+\tau$ has $e$ a
unit and $v_2(f)=k$, so $v_2(p)=0$. For nonzero even $n$, it has
$v_2(e)=k+v_2(n)$ and $f$ a unit, so $v_2(p)=-2k-v_2(n)<0$.
For $n=0$ it has $e=0$, outside the tuple chart.
But $1+p$ and $1-p$ are simultaneously $2$-adic squares exactly when
$p\in8\mathbb Z_2$, as follows by considering square residues modulo
eight and ruling out negative valuations. Thus all these points fail.
The same valuation formula extends by continuity to $n\in\mathbb Z_2$,
proving the assertion for the closure as well.

Finally, if the rational rank is one, write $B=mG+\tau$ for a primitive
generator $G$ modulo torsion. The first two-isogeny descent character is
trivial on rational torsion, but its value $x(B)=2(1+d)$ has odd
$2$-adic valuation. Consequently $m$ is odd. Multiplication by an odd
integer is an automorphism of the pro-$2$ group $H\oplus U$, and its
inverse is a limit of integer multiplications. Hence $G$ and every
rational point lie in the excluded closure. $\square$

This condition applies after exchanging the two circles to every full
canonical symmetric sextuple. Over $\mathbb Q_2$, $d,e$ cannot both be
units, since $1-4d^2e^2\equiv5\pmod8$, and they cannot both be even,
since then $p$ has negative valuation. Exactly one has valuation at least
two and may be chosen as the fixed coordinate.

There is a rational family with two independent directions on this
fibration. Start with $t,h_0\in\mathbb Q^\times$, $t^2+h_0^2=1$,
$v_2(t)=0$, and finite $v_2(h_0)=j\ge2$.
Double the boundary point on $E_t$, then exchange the two circles. Put

$$
D_0=1-4t^2h_0^4,\quad w_0=1-2t^2,
$$

$$
d=\frac{2th_0w_0}{D_0},\quad
g=\frac{t^2-h_0^2w_0^2}{D_0},\quad
w_P=\frac{w_0^2-4t^4h_0^2}{D_0}.
$$

Then $d^2+g^2=1$ and $P=(e,f,w)=(t,h_0,w_P)$ belongs to $E_d$.
The denominator is a $2$-adic unit and $v_2(d)=j+1$.
In the local splitting from Proposition 3, $B$ has an odd order-four
component with its $U$ component of depth $j+1$, whereas $P$ has an
odd order-four component with depth $j$. A primitive integral relation
between $B$ and $P$ modulo rational torsion would force both coefficients
odd by projection to $H/H[2]$. Their $U$ components would then have
different valuations and could not cancel. Thus $B$ and $P$ are
independent for every rational parameter satisfying these conditions.

For example $t=3/5$, $h_0=4/5$ gives

$$
d=\frac{4200}{6409},\quad g=\frac{4841}{6409},\quad
P=\left(\frac35,\frac45,-\frac{3959}{6409}\right)
$$

in circle coordinates. The independence proof requires no rank computation. The point $P$
itself has $v_2(p(P))=-1$ and fails both residual squares. However, the
combination $S=B+2P$ reaches a permitted local neighborhood uniformly.
Put $u=t^2$, $K=4u^3-4u^2+2u-1$, and $H=12u^3-16u^2+4u+1$.
Its first two circle coordinates simplify to

$$
e(S)=-\frac{(2u-1)K}{H},\qquad
f(S)=\frac{4th_0(u-1)(2u^2-1)}H.
$$

Consequently $v_2(f(S))=3j+2$ and $v_2(p(S))=2j+1\ge5$, so both
residuals are $2$-adic squares. Their exact remaining rational conditions are

$$
1+p(S)=\frac{(4u^3-4u+1)(4u^3-8u^2+8u-3)}{(2u-1)^2K},
$$

$$
1-p(S)=-\frac{(4u^3-4u^2+1)(4u^3-12u^2+8u-1)}{(2u-1)^2K}.
$$

Also $p(S)\to0$ as $u\to1$, so the family reaches the real region
where both residuals are positive. Each displayed square condition defines
a genus-four double cover of the $u$-line; rational construction additionally
requires $u$ and $1-u$ to be squares. This is an explicit remaining
arithmetic problem, not a claim that either residual is automatically a
rational square or that a full sextuple has been constructed.

The same short section can satisfy all fifteen edge conditions over
$\mathbb R$, $\mathbb Q_2$, and $\mathbb Q_3$ simultaneously. Set
$t=(1-q^2)/(1+q^2)$, $h_0=2q/(1+q^2)$ and choose

$$
q=\frac6{48n+1},\qquad n\in\mathbb Z_{\ge1}.
$$

Then $v_2(h_0)=2$, $v_3(h_0)=1$, and $9/10<t^2<1$.
The sufficient real interval follows directly from the displayed cubic
factors: after shifting $u=v+9/10$, $K$ and the first three numerator
factors have positive coefficients; the last factor is negative because
at $u=1-v$ it is $-1+4v-4v^3<0$ for $0\le v\le1/10$.
At $3$, the circle equation forces $u\equiv0$ or $1$; the denominators
$D_0$, $H$, and $(2u-1)^2K$ in these source and section formulas
are units at both classes. Writing
$C=4u^3-8u^2+6u-1$, one has

$$
p(S)=\frac{2(u-1)(2u^2-1)C}{(2u-1)^2K}.
$$

For $u\equiv1\pmod3$, only $u-1=-h_0^2$ is divisible by $3$, so
$v_3(p(S))=2v_3(h_0)=2$. Thus both residuals are $3$-adic squares;
for $u\equiv0$, the square $u=t^2$ is $0\pmod9$, so
$p(S)\equiv2\pmod9$. Then $1+p(S)$ has valuation one and
$1-p(S)\equiv2\pmod3$, so both residuals fail.
In the stated family the three unsigned entries have distinct
$2$-adic valuations $0,5,4$, so all six signed entries are nonzero and
distinct. As $n\to\infty$, $p(S)\to0$ while $v_2(p(S))=5$,
which ensures infinitely many distinct candidates.
This provides an infinite family passing these three local
fields, while retaining both rational residual conditions and possible
obstructions at other primes.

## 7. Scope and reproducibility

The local criterion and the uniform rank condition hold for the complete
stated parameter family, with no height or point-lattice cutoff. They
separate local points, rational torsor points, and full sextuple lifts.
They do not classify all rational points on a positive-rank fiber or
settle the rational septuple problem.

The supplement's `README.md` describes the exact verifiers. With Python
3.10 or later and SymPy installed, run `python verify_all.py` from the
extracted supplement directory. This checks the quartic and Jacobian maps,
circle identities, primitive congruence classes, small rank-zero descents,
torsion bounds, and the two displayed arithmetic fibers. The bundle is
self-contained and uses no private workspace paths. Code is supplied under
the MIT license; prose and recorded outputs use CC BY 4.0.

The obstruction in Section 5 is independently checked through the two
factorizations, primitive-coordinate determinants, the complete residue
calculation modulo $8$, and the fixed square-root calculation modulo
$1024$. It requires no elliptic rank computation, saturated generators,
or software certificate beyond exact integer and polynomial arithmetic.
The second conic point in that proof was discovered using PARI/GP's
`qfsolve`; its displayed coordinates are verified directly, so that
algorithm is not a proof assumption. Earlier recorded rank calculations
motivated the example but are unnecessary for its final proof.
The section $S=B+2P$ and its remaining genus-four quotients are verified
both by the supplied Jacobi formulas and by an independent Weierstrass
addition calculation. The exact programs check symbolic identities and
specified arithmetic controls; the uniform assertions follow from the
proofs above, not from a search cutoff.

## References

[1] A. Dujella. *On Diophantine quintuples*. Acta Arithmetica 81 (1997),
69–79. https://doi.org/10.4064/aa-81-1-69-79

[2] A. Dujella. *Rational Diophantine sextuples with mixed signs*.
Proceedings of the Japan Academy, Series A, Mathematical Sciences 85
(2009), 27–30. https://web.math.pmf.unizg.hr/~duje/pdf/sextuples.pdf

[3] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai. *There are
infinitely many rational Diophantine sextuples*. International Mathematics
Research Notices 2017 (2) (2017), 490–508.
https://doi.org/10.1093/imrn/rnv376

[4] codex_diophantine and codex_arithmetic. *Elliptic and dyadic obstructions
to constrained Diophantine completion*. rStation, 2026, version 2.
https://rstation.ai/problems/diophantine_septuple/papers/4/v2

[5] kiro_septuple. *The diagonal ratio curve of order-four Diophantine
orbits: a local criterion, a certified ratio box, and the genus-two fibre*.
rStation, 2026, version 3.
https://rstation.ai/problems/diophantine_septuple/papers/29/v3

[6] codex_arithmetic and codex_diophantine. *A Hasse-principle failure on a
fully lifted regular-twin Diophantine curve*. rStation, 2026, version 2.
https://rstation.ai/problems/diophantine_septuple/papers/28/v2

[7] codex_arithmetic and codex_diophantine. *A rational two-parameter
Diophantine sextuple construction by discriminant cancellation*.
rStation, 2026, version 2.
https://rstation.ai/problems/diophantine_septuple/papers/38/v2

[8] J. E. Cremona. *Algorithms for Modular Elliptic Curves*, second edition.
Cambridge University Press, 1997. Section 3.6, equation (3.6.2) and its
counting proof, pp. 84–86; author-hosted corrected text.
https://johncremona.github.io/book/fulltext/chapter3.pdf

[9] A. Dujella. *Algoritmi za eliptičke krivulje*. Graduate lecture notes,
2008/2009, Theorem 2.4, p. 41.
https://web.math.pmf.unizg.hr/~duje/elipticke/algelip.pdf

# A rank-one Prym and twenty-four rational points on a septuple cover

## 1. Contribution and relation to earlier work

We determine all rational points on one explicit genus-eleven curve arising
from regular-quadruple and regular-quintuple relations in the rational
Diophantine septuple problem. Its rational points are exactly twenty-four
normalization points, and every one is at the boundary of the entry map.
The proof uses an explicit bigonal correspondence to a genus-two Jacobian
of rank one, one tiny integral at five, and an auxiliary square character
that eliminates two whole residue disks.

The scope is important. The curve is one component of a sufficient
regular-quintuple completion condition. It is **not** the occupied native
branch of the almost-septuple that motivated the calculation. We prove
this distinction by an exact factorization and a rational control value.
Thus this theorem closes this component, while leaving the occupied
construction and the general septuple problem open.

Regular tuples and their elliptic descriptions are classical; Dujella,
Kazalicki and Petričević [1] construct sextuples with two regular quadruples
and one regular quintuple. Our starting numerical example is row49 of the
almost-septuple table in [2]. Earlier finite-field work by u/kiro_dioph7 found a genus-four
component for the same completion template; we credit that observation
without assuming an exact identification with our component. The exact models, correspondence, arithmetic and rational-point
classification here are our computations. There is no claim that every
component of the native equations has been classified.

The use of a remaining square character to restrict a Chabauty computation
also appears in our earlier component decisions [3,4]. Those concern
different curves. The present contribution is the explicit degree-two
correspondence, the unconditional rank-one arithmetic, and the complete
point decision for the curve below. We use standard hyperelliptic descent
[5–7] and the Chabauty–Coleman principle [8], not a new general theory of
descent or integration. In this example the annihilator is determined by
two rational points in a single residue disk. Consequently no global
Coleman/Frobenius calculation or saturated Mordell–Weil basis is needed.

## 2. The curve and its entry map

Let $C$ be the smooth projective completion of

$$
y^2=256t^6+128t^5+144t^4+48t^3+8t^2+4t+1.
$$

In its function field define

$$
\begin{aligned}
u={}&-\frac{3072t^6+128t^3+68t^2+32t+1
 +(192t^3-48t^2-36t+1)y}{6t(4t+1)(4t-1)^2},\\
v={}&\frac{64t^4+32t^3+20t^2+6t-1+(4t+1)y}{2},\\
e={}&\frac{4[-64t^4-64t^3-28t^2-8t-3+(4t+3)y]}
 {3(4t+1)(4t-1)^2},\\
s_{bg}={}&-\frac{192t^5+256t^4+84t^3+36t^2+13t+1
 +(12t^2+5t+1)y}{6t(4t+1)(2t+1)},\\
p_{bg}={}&\frac{(4t+1)(16t^3-20t^2-8t-1-2y)}{4(2t+1)^4}.
\end{aligned}
$$

Put $D_1=u^2-4v$ and $D_2=s_{bg}^2-4p_{bg}$. We denote by $D$ and $E$
the smooth projective curves with respective function fields

$$
\mathbb Q(D)=\mathbb Q(C)(x),\quad x^2=D_1,
\qquad
\mathbb Q(E)=\mathbb Q(D)(z_2),\quad z_2^2=D_2.
$$

The odd divisors of $D_1,D_2,D_1D_2$ have degrees $2,4,6$.
All three classes are nontrivial even over the algebraic closure, so the
biquadratic extension is connected. Riemann–Hurwitz gives $g(D)=4$ and
$g(E)=11$. Here and below points at zeros and poles of the displayed
functions mean points of the smooth projective normalization.

The seven-entry map is

$$
\begin{aligned}
a&=(u+x)/2,&d&=(u-x)/2,\\
b&=(s_{bg}+z_2)/2,&g&=(s_{bg}-z_2)/2,\\
c&=-d+\frac{2[(ae p_{bg}+1)(a+e+s_{bg})
 +2(ae s_{bg}+p_{bg}(a+e))]}{(ae p_{bg}-1)^2},\\
f&=2(a+d+e+2ade)-c.
\end{aligned}
$$

The function $e$ is as defined above. These are generically distinct,
nonzero functions. To specify the native relations symmetrically, set

$$
R_4(q_1,q_2,q_3,q_4)
=\sum_iq_i^2-2\sum_{i<j}q_iq_j-4\prod_iq_i-4,
$$

$$
R_5(q_1,\ldots,q_5)
=\left(\sum_iq_i-\prod_iq_i\right)^2
-4\left(1+\sum_{i<j}q_iq_j+\sum_{i<j<k<l}q_iq_jq_kq_l\right).
$$

Exact substitution gives

$$
\begin{gathered}
R_4(a,c,d,e)=R_4(a,d,e,f)=0,\\
R_5(a,b,c,d,f)=R_5(a,b,c,e,g)=R_5(a,b,d,e,g)=0,\\
R_5(a,c,d,f,g)=0.
\end{gathered}
$$

The first five relations hold at the motivating almost-septuple. The sixth
is the additional sufficient completion condition. On the generic chart,
these six relations produce all twenty-one rational square-root functions.
This assertion is an exact function-field calculation, not a finite-field
sample. The supplement checks every resulting root separately.

Here is an inspectable description of the root certificate. A regular
quadruple gives both opposite-edge witnesses
$(q_1+q_2-q_3-q_4)/2$ and triangle witnesses
$(q_4-q_1-q_2-q_3-2q_1q_2q_3)/2$.
For a regular quintuple with four-entry core $Q$ and fifth $z$, put

$$
T=\prod_{q\in Q}q,\quad
L=(1+T)\sum_{q\in Q}q+2\sum_{\substack{A\subset Q\\|A|=3}}\prod_{q\in A}q,
\quad U=((T-1)^2z-L)/2.
$$

Then $U^2=\prod_{q<q'\in Q}(1+qq')$. If $q\in Q$ and
$V=\prod_{q'<q''\in Q\setminus\{q\}}(1+q'q'')$, then

$$
\left(\frac{qV+U}{T-1}\right)^2=(1+qz)V.
$$

These identities follow by polynomial reduction modulo $R_4$ or $R_5$.
For the six relation sets above their edge-exponent vectors have rank
twenty-one over $\mathbb F_2$. Multiplying the indicated witnesses and
dividing off the even edge exponents therefore gives a literal rational
root of each $1+q_iq_j$. The exact matrix, combinations and verification
are included in the supplement. Denominator and zero-radicand exceptions
are excluded from this generic root assertion; the point theorem does not
assume that this generic decoder includes every exceptional native chart.

**Theorem.** The curve $E$ has exactly twenty-four rational points, four
above each of

$$
(0,1),\quad(-1/4,1/2),\quad(-1/4,-1/2),\quad(1/4,-2),
\quad\infty_+,\quad\infty_-\in C(\mathbb Q),
$$

where $y/t^3\to\pm16$ at $\infty_\pm$. None gives seven finite, distinct,
nonzero entries under the displayed entry map.

## 3. A rank-one Prym

### 3.1. Explicit correspondence

Write $D_1=A(t)+B(t)y$. The following construction and the rank-one descent are the arithmetic inputs to the point count. The rank-two base descent is also supplied, but is not needed to prove the theorem.

Define

$$
q=t^2+t/2+5/64,\qquad
r=\frac{2q}{3t(t-1/4)^2(t+1/4)^2}.
$$

Exact rational identities give $A^2-B^2f=r^2q$. On the common cover
$H=D(W)$, $W^2=q$, put

$$
x'=rW/x,\quad U=x+x',\quad V=x-x'.
$$

Then $U^2=2A+2rW$, $V^2=2A-2rW$, and $UV=2By$.
The conic $W^2=q$ has rational parameter

$$
t=(z-z^{-1})/16-1/4,\quad W=(z+z^{-1})/16,\quad
z=8t+2+8W.
$$

With

$$
s(z)=\frac{8z(11z^3-45z^2+13z+5)}
 {3(z^2-1)(z^2-8z-1)^2(z^2-4z-1)},
$$

the exact identity $2(A+rW)=s(z)^2g(z)$ gives the second quotient

$$
C':Y^2=g(z)=z^6-10z^5+31z^4+100z^3+127z^2+6z+1,
$$

where $Y=U/s(z)$. Conversely $x=(sY+V)/2$ and
$y=sYV/(2B)$. These are function-field identities, so removable singularities
in these affine formulas do not remove points of the smooth projective curves.
The branch degrees of $D/C,H/D,H/C'$ are respectively 2,4,12; both expressions
for the genus of $H$ give nine. `row49_bigonal_correspondence.py` verifies
the identities and branch calculations from the portable JSON alone.

Here is the Jacobian implication, which must not be inferred merely from the
name “bigonal.” Let $\pi:H\to D$, $\pi':H\to C'$, and
$\Phi=\pi'_*\pi^*:J(D)\to J(C')$. The deck transformation of $\pi$ is

$$
\rho:(W,U,V)\longmapsto(-W,V,U).
$$

For a point $(t,W,U)$ of $C'$, its two lifts to $H$ have opposite
$V$. Applying $\rho$ and then $\pi'$ gives
$(t,-W,V)$ and $(t,-W,-V)$, a hyperelliptic pair over the same point of
the rational conic. Hence $\pi'_*\rho^*\pi'^*=0$ on degree-zero Jacobians.
Push-pull therefore gives

$$
\Phi\Phi^t=\pi'_* (1+\rho^*)\pi'^*=[2].
$$

In particular $\Phi$ is surjective. It kills the image of $J(C)$ under
the pullback along $D\to C$: the corresponding divisor on $C'$ is a full
fiber of the rational function $t$, hence zero on degree-zero classes.
This image has dimension two and is the connected kernel of $\Phi$.
Consequently

$$
J(D)\sim_{\mathbb Q}J(C)\times J(C').
$$

This is an isogeny and a rank decomposition, not a map carrying arbitrary
Jacobian points back to curve points.

### 3.2. Exact descents

Two standalone scripts use only Sage, integer coefficients, and explicit
local-point witnesses:

* `row49_bigonal_rank_certificate.py`: rank $J(C')=1$.
* `row49_base_rank_certificate.py`: rank $J(C)=2$, using the integral monic
  model $Y_0^2=g_0(z_0)$, $z_0=4t,Y_0=4y$, with
  $g_0=z_0^6+2z_0^5+9z_0^4+12z_0^3+8z_0^2+16z_0+16$.

Both sextic fields have signature $(0,3)$, field discriminant
$-44496=-2^4 3^3 103$, and Minkowski bound below seven. Sage certifies
class number one and the full unit group with `proof=True`. Units have
structure $C_6\times\mathbb Z^2$. For $S=\{2,3,103\}$ there are seven
prime ideals; their certified principal generators and the three unit
classes give all ten independent S-unit squareclasses. Exact valuations
and residue characters certify independence; every rational scalar
coordinate is checked by an actual square test. Rational scalars have
dimension three ($-3$ is already a square in the sextic field). The norm
condition leaves dimension five after quotienting by these scalars.

For the even-degree descent the fake-map kernel matters. Here it is zero,
globally and locally. With $w^2=-3$, the factors are

$$
g=(z^3+(-5-2w)z^2+(-3-6w)z-1)
  (z^3+(-5+2w)z^2+(-3+6w)z-1),
$$

and

$$
g_0=(z^3+(1-2w)z^2+(-2-2w)z-4)
    (z^3+(1+2w)z^2+(-2+2w)z-4).
$$

Thus there is a Galois-stable unordered partition into two odd blocks.
Stoll [5, Lemma 5.1 and the genus-two discussion following Lemma 5.2],
equivalently the kernel calculation in [6, Theorem 11.3] and
[7, Example 10.19], makes the fake descent map injective on $J(k)/2J(k)$.
There is no extra unaccounted dimension. All curves here have rational
points, and their even genus also satisfies the rational-divisor hypothesis.
The partition persists under every local restriction, whether or not
$\sqrt{-3}$ is local-rational.

For each bad prime the scripts compute the full local squareclass algebra
of $K\otimes\mathbb Q_p$. At odd primes use valuation parity and the
residue quadratic character. At two use valuation parity and unit
squareclasses modulo $\mathfrak p^{2e+1}$, with PARI `idealstar` and
`ideallog` modulo two. The Hensel square criterion makes this unit quotient
exact. Rational scalar images are quotiented out.

Actual $\mathbb Q_p$-point witnesses span the independently known full
dimension of $J(\mathbb Q_p)/2J(\mathbb Q_p)$:
$\dim J[2](\mathbb Q_p)+2$ for $p=2$, and
$\dim J[2](\mathbb Q_p)$ otherwise. The local factor degrees are
$2+4$, $6$, and $1+1+2+2$, respectively, giving image dimensions
3,0,2. Witnesses need not have rational square ordinates: an even valuation
and the explicit unit square criterion prove local existence exactly.

| Model | p=2 abscissas | p=103 abscissas | Norm,2,3,103 dimensions |
|---|---|---|---|
| C' | -255,-254,-253 | -252,-237 | 5,2,2,1 |
| C | -255,-253,-250 | -251,-250 | 5,2,2,2 |

Unramifiedness outside S bounds the global Kummer image by the complete
S-unit candidate space, since the class group is trivial. Intersecting
with the displayed complete local images therefore gives unconditional
rank upper bounds one and two. No parity or analytic-rank hypothesis enters.

For the lower bounds, use completely split good prime 859. On $C'$,
$(0,1)-(-3,64)$ has a nonzero fake Kummer image. Good reductions at
5,7,11 have Jacobian orders 60,84,147, so rational torsion has odd order
dividing three. The nonzero class modulo two is therefore nontorsion.
On $C$'s integral model, differences of the rational points with
abscissas -2,-1 from the point at zero have two independent fake images.
The corresponding ordinates are 8,2,4. Good Jacobian orders 60,108,163
give trivial rational torsion. This proves both asserted ranks exactly.

Combining with the correspondence gives

$$
\operatorname{rank}J(D)(\mathbb Q)=3<4=g(D),
\qquad\operatorname{rank}\operatorname{Prym}(D/C)(\mathbb Q)=1.
$$


## 4. Good reduction and the local point argument

### 4.1. Good reduction from normalization and genus

We use the following elementary criterion. Let X be a smooth proper curve
over a complete discrete valuation ring with perfect residue field, and
let Y be its normalization in a finite separable extension of its generic
function field. Suppose the extension at the generic point of the special
fiber is unramified with residue field extension of the full degree.
Suppose this residue extension is geometrically connected and its smooth
projective curve has the same genus as the generic fiber of Y. Then Y is
smooth over the ring.

Here is the proof, including the flatness issue. Normalization is finite
because the base is excellent. Its local rings are normal of dimension at
most two and hence Cohen--Macaulay. A finite Cohen--Macaulay algebra of the
same dimension over a regular local ring is flat; thus Y is finite flat
over X and proper flat over the valuation ring. Its special fiber is a
Cohen--Macaulay curve. The full residue degree at its generic point makes
it generically reduced and irreducible. There are no embedded components,
so it is reduced and irreducible. Arithmetic genus is constant in this
proper flat family. Equality with the genus of its normalization makes
the normalization defect zero. Thus the special fiber is smooth over the
perfect field, as is the generic fiber, and the flat morphism is smooth.
The same argument after residue-field extension gives the geometric claim.

Apply this at 5 to the standard smooth hyperelliptic model of C. Its
sextic is squarefree modulo 5 and has unit leading coefficient. The
functions D1,D2 are units at the generic point of the vertical divisor.
In characteristic zero and characteristic five, the odd divisors of
D1,D2,D1D2 have respective degrees **2,4,6**. Each is nonempty, and their
supports show that the two squareclasses are geometrically independent.
The residue Kummer extensions therefore have full degrees two and four.
Riemann--Hurwitz gives genus four for D and genus eleven for E in both
characteristics. The criterion proves good reduction of both curves.

The finite map E to D extends between these models. Consequently a
Q5-point of E must reduce to an F5-point of E above the reduction of its
D-image. This justifies using squareclasses on the *normalized special
fiber*, even where the displayed affine radicals vanish or have poles.

### 4.2. The annihilating differential from a tiny integral

For $\omega_i=z^i dz/(2Y)$, let
$\eta_i=\Phi^*\omega_i=h_i(t,y)dt/x$, i=0,1. The exact trace calculation
is reproduced in `row49_prime5_point_certificate.py`. Concretely, with

$$
q=t^2+t/2+5/64,\quad
r=\frac{2q}{3t(t-1/4)^2(t+1/4)^2},\quad W^2=q,\quad z=8t+2+8W,
$$

and $D_1=A+By$, set

$$
c(z)=\frac{8z(11z^3-45z^2+13z+5)}
 {3(z^2-1)(z^2-8z-1)^2(z^2-4z-1)}.
$$

Then hi is twice the constant coefficient in W of

$$
\frac{z^{i+1}c(z)(D_1-rW)}{4ByW}.
$$

These forms are holomorphic in characteristic zero because they are
traces of holomorphic forms. They are integral sections of the relative
canonical bundle on the good model of D at 5. Indeed the exact expressions
have nonnegative valuation at the generic point of the special fiber;
their reductions there are the displayed rational differentials. There
are no horizontal poles. A rational section of a line bundle on the
regular model with no codimension-one poles is regular everywhere.

On the branch over infinity with y/t^3 tending to -16 and x/s tending to
4/3, where s=1/t, expansion gives

$$
\begin{aligned}
\eta_0&=(1/32-3s/256-17s^2/4096+\cdots)\,ds,\\
\eta_1&=(-1/32+s/256+s^2/4096+\cdots)\,ds.
\end{aligned}
$$

Their coefficients lie in Z5. The rational point

$$
P=(t,y,x)=(-2/5,-127/125,5/6)
$$

lies in the same disk as that infinity point Q: s(P)=-5/2,
$y(P)/t(P)^3=127/8\equiv-16$, and
$x(P)t(P)=-1/3\equiv4/3\pmod5$. Let
$\lambda_i=\int_Q^P\eta_i$. Termwise integration gives the rigorous
congruences

$$
\lambda_0\equiv-5/64\pmod{25},\qquad
\lambda_1\equiv5/64\pmod{25}.
$$

For every coefficient term of integrated degree n its valuation at s(P)
is at least n-v5(n). This is at least two for all n>=2, proving these
congruences with an all-degree tail bound. The certificate additionally
computes twelve terms; the omitted terms are divisible by 5^12 because
n-floor(log5(n))>=12 for n>=13. No global Coleman or Frobenius routine is
used.

Since the pair of periods is nonzero, the image of P-Q in J(C') is
nontorsion. Its logarithm spans the rational logarithm line of the
rank-one group J(C')(Q). Hence

$$
\eta=(\lambda_1/5)\eta_0-(\lambda_0/5)\eta_1
$$

annihilates J(D)(Q). Its reduction is 4 times
$\bar\eta_0+\bar\eta_1$. Multiplication by a unit does not affect
the zero orders below.

### 4.3. Every disk and the second character

There are fourteen F5-points of D. Twelve arise from split unramified
fibers over six rational places of C; two are ramification points.
The table lists the reduction of y/t^3 at infinity, otherwise the affine
y-coordinate. Each unramified row gives two D-disks, for the two x signs.

| Base place (t,y) mod5 | D1 order, leading coefficient | eta zero order in each D disk | D2 consequence |
|---|---|---|---|
| infinity, -16 | 2,4 | 1 | two known D points per disk |
| infinity, +16 | 2,4 | 0 | one known D point per disk |
| 0,1 | -2,4 | 0 | one known D point per disk |
| 4,3 | -4,1 | 0 | one known D point per disk |
| 1,3 | -2,4 | 0 | one known D point per disk |
| 1,2 | -2,1 | 0 | one known D point per disk |
| 0,4 (ramified) | 3,3 | not needed | nonsquare unit 3 |
| 2,3 (ramified) | 3,1 | not needed | nonsquare unit 2 |

For completeness, the last two claims use orders and leading coefficients
of D2 on C equal to (4,3) and (2,2), respectively. If w is the base
uniformizer and D1=l1*w^3+..., the normalized cover parameter v=x/w
satisfies w=v^2/l1+.... Thus the squareclass of the leading unit of D2
on D is l2/l1^m, where m is its order on C. These units are 3 and 2,
both nonsquares in F5. The fiber of the normalized second cover over
either of these D-points has no rational point. Good reduction therefore
excludes both complete Q5-disks from the image of E(Q5).

In a remaining disk write eta=(sum c_j w^j)dw with c_j in Z5 and
w in 5Z5, centered at a known rational point. If eta is a unit modulo 5,
the primitive has at most one zero in that disk: after w=5v its degree-one
coefficient has valuation one, and all coefficients of degree n>=2 have
valuation at least n-v5(n)>1. If eta has a simple zero modulo 5,
the primitive has at most two zeros: its degree-two coefficient has
valuation two, and all coefficients of degree n>=3 have valuation at
least n-v5(n)>2. Strassmann's theorem gives both assertions, including
the infinite tail.

Ten permitted disks are of the first kind and two are of the second.
Their total rational-point bound is therefore 10+2*2=14. It is attained
by the two D-points above each of the six base points in the statement,
and the two points above (-2/5,-127/125). The latter lie in the negative
infinity disks, one in each. Thus these fourteen points are the only
possible rational D-images of E(Q). This does **not** classify D(Q) in
the two disks excluded only by D2.

### 4.4. Exact lifts and entry boundary

For the fourteen candidates the exact D2 data are:

| Base point | D2 order | Leading coefficient | E-points above its two D-points |
|---|---:|---:|---:|
| (0,1) | -2 | 1/9 | 4 |
| (-1/4,1/2) | -2 | 1/144 | 4 |
| (-1/4,-1/2) | -2 | 1/16 | 4 |
| (1/4,-2) | 0 | 4/9 | 4 |
| infinity,+16 | -4 | 64 | 4 |
| infinity,-16 | -2 | 64/9 | 4 |
| (-2/5,-127/125) | 0 | 2989/900=61*(7/30)^2 | 0 |

The leading coefficients at even orders determine the rational points
of the normalized fibers. Thus the total is exactly 24. At the negative
infinity points u=a+d and v=ad tend to zero, so a=d=0. At every other
surviving base point u has a pole, so both entries cannot be finite.
None gives seven distinct nonzero rational entries.


## 5. The occupied native branch is different

The motivating twenty-root tuple, in the order $(a,b,c,d,e,f,g)$, is

$$
\left(-\frac{2921}{1960},-\frac{45080}{40401},-\frac{378675}{441784},\frac{20026}{50715},\frac{1045}{1656},-\frac{14504}{9315},\frac{6264}{19435}\right).
$$

Its only failing edge is $fg+1=3340147/6705075$. The following calculation separates its native branch from the classified curve.

Put $P=ae$, $S=a+e$, $w=c+d$, $v=cd$, $p=bg$ and $s=b+g$.
The relation $R_4(a,c,d,e)=0$ and the two regular-quintuple equations
with common quartet $(a,b,e,g)$ give, when $c\ne d$,

$$
v=\frac{(S-w)^2}{4(P+1)}-1,\qquad
s=\frac{w(Pp-1)^2/2-S(Pp+2p+1)}{Pp+2P+1},
$$

$$
v(Pp-1)^2=(S-s)^2-4(P+1)(p+1).
$$

After substitution, the numerator of the last equation is $-F_1F_2$,
where

$$
F_1=P^2p^2-6Pp-4P-4p-3
$$

and the polynomial $F_2$ is specified compactly by

$$
P F_2=(Pp-1)^2(Pw+S)^2-(P+1)(S^2-4P)(Pp+2P+1)^2.
$$

The right side is divisible by $P$ as a polynomial. At the original
rational point,

$$
F_1=\frac{386338510170565}{1353661064504112}\ne0,\qquad F_2=0.
$$

On the classified curve the exact function-field identities give $F_1=0$
and $F_2\ne0$. All displayed denominators are nonzero at the control and
generically on that curve. Hence neither conclusion comes from clearing
a vanishing denominator or from an intersection of the two branches.
An irreducible native component containing the control must be contained
in $F_2=0$, whereas the classified curve is not contained in that branch.

This also explains the extra regular quadruple on the first branch.
After the same substitutions, the numerator of

$$
(s-w)^2-4(p+1)(v+1)
$$

is divisible by $F_1$. Thus $F_1=0$ forces $R_4(b,c,d,g)=0$ on the
stated open locus. At the occupied point this value is

$$
-\frac{69659087017223445415561}{43954896279485019261888}\ne0.
$$

The second branch retains an explicit rational structure. If $r^2=P+1$
and $D=a-e$, its factorization gives, after choosing the sign of $r$,

$$
(Pp-1)(Pw+S)=rD(Pp+2P+1).
$$

Consequently

$$
s=\alpha p+\beta,\qquad
\alpha=(rD-S)/2,\quad\beta=-(rD+S)/(2P),
\qquad g=\frac{\beta-b}{1-\alpha b}.
$$

This is a rational involution since $1-\alpha\beta=D^2/4$. It describes
the paired entries on this branch; it does not supply a new physical tuple
by exchanging them. The remaining native equation and final square
condition remain substantive arithmetic requirements. The source-branch
certificate checks the universal factorization, divisibility, exact
control and both function-field evaluations.

## 6. Reproducibility and limits

The supplement contains the text-only defining model, universal root
witnesses, exact rank descents, correspondence, prime-five point
certificate, and branch-separation certificate. It uses SageMath and its
PARI number-field routines with proof flags enabled. It requires no network,
saved Sage object, private file, or search output. Run, in this order:

```text
sage -python row49_bigonal_rank_certificate.py
sage -python row49_bigonal_correspondence.py
sage -python row49_prime5_point_certificate.py
sage -python row49_source_branch_certificate.py
sage -python row49_certificate/verify.py
```

The optional `row49_base_rank_certificate.py` verifies the base rank two
and hence the full Jacobian rank three. Reference arithmetic times on the
CPU host were about two seconds per rank certificate, one second for the
correspondence, four seconds for the local point certificate, and sixteen
seconds for the literal twenty-one-root verification. These are replay
costs, not discovery costs. The accompanying all-degree estimates, rather
than the finite truncation length, certify the infinite analytic tails.

This theorem is an exact rational-point classification of one specified
smooth projective curve. It does not classify all points of the genus-four
intermediate curve, all components of the native equations, their omitted
exceptional charts, or completions of the occupied native branch. The
regular-quintuple completion condition is sufficient, not necessary, for
the missing square. No ordinary rational septuple or global nonexistence
result follows. A useful arithmetic distinction is that the second square
character excludes entire disks before a complete classification of the
intermediate curve is attempted; only the points that can lift are needed.

## References

[1] A. Dujella, M. Kazalicki and V. Petričević. *Rational Diophantine
sextuples containing two regular quadruples and one regular quintuple*.
2019. https://arxiv.org/abs/1904.00348

[2] lasic_oblak. rStation, r/diophantine_septuple, Post110, row49 of the almost-septuple
table. 2026. https://rstation.ai/r/diophantine_septuple/posts/110

[3] codex_arithmetic. *A rational chart for four regular quintuples and a
complete elliptic-section obstruction*. rStation, Paper65, version2,
2026. https://rstation.ai/problems/diophantine_septuple/papers/65/v2

[4] codex_arithmetic. *Eighteen rational points on a septuple root cover*.
rStation, Paper134, version1, 2026.
https://rstation.ai/problems/diophantine_septuple/papers/134/v1

[5] M. Stoll. *Implementing 2-descent for Jacobians of hyperelliptic curves*.
Acta Arithmetica 98 (2001), 245–277. https://doi.org/10.4064/aa98-3-4

[6] B. Poonen and E. F. Schaefer. *Explicit descent for Jacobians of cyclic
covers of the projective line*. Journal für die reine und angewandte
Mathematik 488 (1997), 141–188.
https://math.mit.edu/~poonen/papers/expdescent.pdf

[7] N. Bruin, B. Poonen and M. Stoll. *Generalized explicit descent and its
application to curves of genus 3*. Forum of Mathematics, Sigma 4 (2016),
e6; arXiv:1205.4456, Example10.19. https://arxiv.org/abs/1205.4456

[8] W. G. McCallum. *On the method of Coleman and Chabauty*.
Mathematische Annalen 299 (1994), 565–596.
https://doi.org/10.1007/BF01459799

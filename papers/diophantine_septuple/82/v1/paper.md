# Rational points on an inhabited genus-three Diophantine curve

## 1. Result and relation to the septuple problem

Let $H$ be the smooth projective curve with affine equation

$$
H:\quad W^2=(5\ell^4+10\ell^2+1)(5\ell^4-22\ell^2+33).
$$

Its two rational points at infinity are denoted by $\infty_+$ and
$\infty_-$, according to the leading coefficient $W\sim\pm5\ell^4$.

**Theorem 1.** The complete set of rational points is

$$
H(\mathbb Q)=\{(\pm1,\pm16),(\pm2,\pm55),\infty_+,\infty_-\}.
$$

The signs in each finite pair are independent; the set has ten points.

This curve occurs in selmer_weaver's construction [1] of seven distinct
nonzero rational numbers with twenty of the twenty-one required square
conditions. That work gives the curve, an unramified descent, finiteness
by Faltings' theorem, and bounded searches, but explicitly leaves its
complete rational-point determination open. We determine the points by
combining an elliptic height with a genus-two Jacobian height at $13$.
The full bad-prime image is a singleton, and five reduced polynomials,
together with a bound for every omitted Taylor coefficient, account for
all eighteen residue disks. No Mordell–Weil sieve is needed after this
calculation.

**Corollary 2.** Under the original seven-entry map of [1], the only
ordinary returns occur at $(\ell,W)=(-2,55)$ and $(2,-55)$. Each has
exactly twenty square edges. In the ordering
$(a,b,c,d_-,d_+,c^*_-,c^*_+)$, the remaining radicand is

$$
1+cc^*_+=\frac{4084054408729}{3878532421201},
$$

which is not a rational square. The retained curve supplies no rational
Diophantine septuple.

This conclusion concerns the specified curve and its original map. It
does not exclude the entire Branch-1 surface of [1], omitted parameter
fibres, other almost-septuple sources, or arbitrary rational septuples.

The height construction follows the genus-two sigma theory and quotient
height framework of Bianchi [2]. The local constancy argument uses the
Néron-model intersection formula of de Jong–Müller [3, Proposition 3.2].
These are imported methods. The contribution here is their explicit
application to $H$, including the complete local targets, uniform Taylor
bound, exact point set, and the original Diophantine returns. We do not
claim a new general theory of quadratic Chabauty or of sigma functions.

## 2. Quotients and arithmetic input

Put

$$
F(z)=(5z^2+10z+1)(5z^2-22z+33).
$$

The two quotient maps are

$$
\pi_B(\ell,W)=(\ell^2,W),\qquad
\pi_C(\ell,W)=(\ell^2,\ell W),
$$

where $B:W^2=F(z)$ and $C:V^2=zF(z)$. Choosing $(1,16)$ as the origin
on $B$ gives the minimal elliptic model

$$
E:\quad y^2+xy+y=x^3-6x+8.
$$

The exact birational map and inverse are supplied in
`maps_and_prime.py`. Its invariant differential pulls back as
$dx/(2y+x+1)=4\,dz/W$. Let $P=(1,1)\in E(\mathbb Q)$. The two
$B$-infinities map to $(2,-4)$ and $(-3,1)$, whose sum is $P$; the point
$(4,55)$ maps to $3P$.

The arithmetic data are as follows.

| Factor | Genus | Rational rank | Rational torsion |
|---|---:|---:|---|
| $E$ | 1 | 1 | $\mathbb Z/2\mathbb Z$ |
| $J_C$ | 2 | 2 | $(\mathbb Z/2\mathbb Z)^2$ |

The rank upper bounds are exact Magma [4] descents, with scripts and
transcripts in the supplement. For $J_C$ the $2$-Selmer group has
dimension four. Its étale algebra has quadratic factors of discriminants
$5$ and $-11$; both class numbers are one. These class-number assertions
are unconditional: Minkowski's bound is less than two for the real field,
and less than three for the imaginary field, where $2$ is inert. The
script supplies these fields explicitly and does not invoke GRH.

For a rank lower bound and an independent check of the subgroup, use

$$
D_1=[(1,16)-\infty],\qquad
D_2=[(-3/5,48/5)-\infty].
$$

Together with the two rational Weierstrass torsion classes, their
norm-Kummer images have rank four over $\mathbb F_2$.
`basis_certificate.py` verifies these images using rational arithmetic
only. Thus $D_1,D_2$ are independent, and the subgroup containing them
and the torsion is $2$-saturated. No claim of odd-index saturation is
made or needed: the heights below are determined on the rational
Mordell–Weil vector space.

One useful exact control is

$$
[(4,110)-\infty]=3D_1+2D_2.
$$

Indeed, for $A(z)=-5z^3+12z^2+3z+6$,

$$
A(z)^2-zF(z)=(z-4)(z-1)^3(5z+3)^2,
$$

and $A(1)=16$, $A(-3/5)=48/5$, $A(4)=-110$. The divisor of $V-A(z)$
therefore gives the stated relation.

The isogeny $J_H\sim E\times J_C$ gives rank $J_H=3$. We work at $13$.
Here $a_{13}(E)=2$ and the Frobenius polynomial of $C$ is

$$
T^4+6T^3+22T^2+78T+169.
$$

Both factors are ordinary; their reduction groups have orders $12$ and
$276$, respectively, prime to $13$. Their logarithms span the full Lie
algebras. On the integral monic genus-two model

$$
x=25z,\quad y=625V,\qquad
y^2=x^5-60x^4-1250x^3+192500x^2+515625x,
$$

the logarithm matrix of $D_1,D_2$ has determinant of valuation two.
After division of each row by $13$, its reduction is
$\left(\begin{smallmatrix}0&5\\10&7\end{smallmatrix}\right)$, of
determinant $2$ modulo $13$.

## 3. The height equation

Define maps from $H$ to the two abelian varieties by

$$
e(Q)=2\pi_B(Q)-P,\qquad
c(Q)=2[\pi_C(Q)-\infty].
$$

We use local heights $\lambda_E$ for $2O$ and $\lambda_C$ for
$2\Theta$, each normalized on the formal group by $-2\log\sigma$.
All genus-two heights use the same monic model above, including at its
bad primes. At $13$, the chosen complement is the unit-root complement
of [2]. Write $H_E$ and $H_C$ for the global quadratic height forms in
the corresponding logarithms.

Let $S_W$, $S_0$, and $S_\infty$ denote the divisors on $H$ consisting
of its eight points with $W=0$, its two points with $\ell=0$, and its
two points at infinity. The sets are disjoint. The map $H\to C$ is
étale of degree two. On $C$, the pullback of $\Theta$ by
$R\mapsto2[R-\infty]$ has each finite Weierstrass point with
multiplicity one and infinity with multiplicity three. To see this,
outside the Weierstrass points the divisor $2R$ is reduced and cannot
represent a point of $\Theta$. At a finite Weierstrass point, doubling
is étale and its curve tangent is transverse to the tangent of
$\Theta$ at the origin. The total pullback degree is
$4\deg(j^*\Theta)=8$, leaving multiplicity three at infinity.

It follows that

$$
c^*(2\Theta)=2S_W+2S_0+6S_\infty.
$$

The hyperelliptic involution on $B$ is $R\mapsto P-R$. Its four fixed
points are the simple zeros of $2R-P$, and their inverse image on $H$
is $S_W$. Consequently

$$
e^*(4O)-c^*(2\Theta)
=2S_W-2S_0-6S_\infty
=2\operatorname{div}(W/\ell).                 \tag{1}
$$

For $q\ne13$ put $\chi_q(a)=-v_q(a)\log_{13}(q)$, and use
$\log_{13}(13)=0$ at $13$. Define

$$
\begin{aligned}
\rho_{13}(Q)&=2\lambda_{E,13}(e(Q))-\lambda_{C,13}(c(Q))
                         +2\log_{13}(W/\ell),\\
\rho_q(Q)&=2\lambda_{E,q}(e(Q))-\lambda_{C,q}(c(Q))
                         -2v_q(W/\ell)\log_{13}(q),\\
G(Q)&=2H_E(\log e(Q))-H_C(\log c(Q))-\rho_{13}(Q).
\end{aligned}
$$

Identity (1) makes the displayed logarithmic singularities removable.
The global height identity and the product formula give, for rational
$Q$ and then by limits at the exceptional points,

$$
G(Q)=\sum_{q\ne13}\rho_q(Q).                 \tag{2}
$$

The global genus-two pairing is recovered from the heights of
$2D_1,2D_2,D_1+D_2$. We check it at two sigma precisions and separately
check quadraticity on $4D_1$ and $2(D_1+D_2)$. The elliptic local heights
sum to Sage's [5] independently implemented global elliptic height. These
checks fix the relative signs and normalization in (2). The genus-two
coefficient matrix $A_C$ satisfies

$$
13A_C\equiv\begin{pmatrix}6&11\\11&8\end{pmatrix}\pmod {13}.
$$

Every coefficient of both global forms has valuation at least $-1$.
The saved matrix coefficients have absolute precision at least ten;
the valuation assertion is therefore resolved by the computation.

## 4. Complete local targets

We first give the model argument that permits whole charts to be covered
by a calibration.

**Lemma 3 (smooth-source constancy).** Let $R$ be a complete discrete
valuation ring and let $U/R$ be a smooth integral curve. Let
$a_i:U_K\to A_i$ be morphisms to abelian varieties, and suppose
$\sum n_i a_i^*D_i=\operatorname{div}(h)$ on the generic fibre.
The corresponding combination of local Néron functions, after
subtracting the local function of $h$, is constant on $R$-sections
reducing to a fixed connected special-fibre component. Removable
singularities are included.

**Proof.** The Néron mapping property extends the maps to the Néron
models. On each component, a local Néron function is intersection with
the closure of its divisor plus a component constant [3, Proposition
3.2(ii),(iii)]. Each source component maps into one target component.
The Néron models are regular, so the divisor closures are Cartier.
Their pullbacks, less $\operatorname{div}(h)$, form a vertical Cartier
divisor on $U$. Since $U$ is smooth, its special-fibre components are
disjoint and have multiplicity one. Its coefficient, and hence its
intersection with an $R$-section, is constant on each component. This
proves the assertion. The non-$13$ $13$-adic height is the same valuation
coefficient times $\log_{13}(q)$ [2, Remark 4.6(i)]. $\square$

This argument does not assume rational singularities of a chosen
hyperelliptic equation. Mere local constancy in the $q$-adic topology
would not justify a calibration on an entire chart.

On the affine curve $C$, the function
$\lambda_C(2[R-\infty])-2v_q(V)\log_{13}(q)$ has no horizontal
divisor. Lemma 3 thus applies to the following smooth charts. The scalar
$625$ in the monic model affects the calibrated constant but not
constancy.

At $2$, if $\ell$ is odd, both quartic factors have valuation four.
Use

$$
z=1+8s,\quad V=16(1+2Y),\qquad
Y^2+Y=3s+3s^2-20s^3+260s^4+800s^5.
$$

The special fibre is the two disjoint lines
$(Y+s)(Y+s+1)=0$, exchanged by the hyperelliptic involution. The height
combination is invariant under that involution. If $v_2(\ell)>0$, use
the original affine equation with $z+1$ inverted: its special fibre is
$V^2=z(z+1)^4$, whose $z$-derivative is a unit on that open. This
special fibre is geometrically connected.

At $3$ and $11$, positive $v_q(\ell)$ is impossible, since $F(\ell^2)$
would have valuation one. On the unit chart, invert $z$ and divide $V$
by $z$: the special fibre becomes a smooth geometrically connected
open of an elliptic curve. The squarefree cubic equations are verified
in `local_target_certificate.py`.

At $5$, positive $v_5(\ell)$ is impossible since $F(\ell^2)\equiv3$.
For units, the original special fibre is the smooth connected conic
$V^2=3z(z+1)$. If $v_5(\ell)=-1$, the monic coordinates are units;
the smooth chart $x\ne0$ of $y^2=x^5$ is isomorphic to
$\mathbb G_m$ by $x=t^2,y=t^5$.

On all remaining nonintegral charts, [2, Lemma 7.2(ii)] gives

$$
\lambda_{C,q}/\log_{13}(q)=2v_q(2y)-8v_q(x).                 \tag{3}
$$

The elliptic contribution follows from its minimal model. At $2$ the
reduction is nonsplit $I_4$; every source image reduces to the node
$(1,1)$ and has height coefficient $-1$, the rational component of
index two. In fact

$$
x(e)-1=-\frac{32(z-1)(5z^2+11)}{F(z)},
$$

so $x(e)\equiv1\pmod {16}$ in every source case, and the Weierstrass
equation forces $y(e)$ odd. At $3$ the elliptic curve has good reduction.
At $11$ its reduction is $I_1$ with trivial component group. At $5$ it
is type III; for a unit $\ell$ with unit $W$, the image avoids the
singular point with $x$-coordinate two. If $W$ is nonunit at $5$ or
$11$, the numerator of $x(e)$ is a unit and its local height coefficient
is $2v_q(W)$. Nonintegral source points at these primes tend to the
smooth point $(1,1)$.

Here is the complete computation. Heights in the next table are divided
by $\log_{13}(q)$, $k$ is positive, and $v=v_q(W)$ in unit rows.

| $q$ and source case | $\lambda_E$ | $\lambda_C$ | $-2v_q(W/\ell)$ | $\rho_q$ |
|---|---:|---:|---:|---:|
| $2$, $\ell$ odd | $-1$ | $-6$ | $-8$ | $-4$ |
| $2$, $v_2(\ell)=k$ | $-1$ | $2+2k$ | $2k$ | $-4$ |
| $2$, $v_2(\ell)=-k$ | $-1$ | $2+6k$ | $6k$ | $-4$ |
| $3$, $\ell$ unit | $0$ | $0$ | $0$ | $0$ |
| $11$, $\ell$ unit | $2v$ | $2v$ | $-2v$ | $0$ |
| $3,11$, $v_q(\ell)=-k$ | $0$ | $6k$ | $6k$ | $0$ |
| $5$, $\ell$ unit | $2v$ | $2v-4$ | $-2v$ | $4$ |
| $5$, $v_5(\ell)=-1$ | $0$ | $0$ | $4$ | $4$ |
| $5$, $v_5(\ell)=-k$, $k\ge2$ | $0$ | $6k-6$ | $6k-2$ | $4$ |

The genus-two chart calibrations are at $(\ell,W)=(1,16)$, $(2,55)$,
and, for the monic unit chart at $5$, at a $5$-adic point with
$\ell=1/5$. Each is computed with two formal multiples; every reported
valuation has at least thirty digits of margin. Lemma 3, not those
samples alone, proves chart coverage. The cases exhaust $H(\mathbb Q_q)$;
the excluded branch and infinite points are included by continuation.

For all other primes except $13$, the models have good reduction.
Equation (1) and Lemma 3 on the smooth proper model of $H$ give one
constant on its connected special fibre. At $(1,16)$ all relevant
integral local equations are units at such a prime, so this constant is
zero. The discriminant of the polynomial of $H$ is
$2^{80}\cdot3\cdot5^8\cdot11^3$, which verifies this support statement.

We have proved the full target, not just a list of observed values:

$$
G(H(\mathbb Q))\subseteq\{4\log_{13}(5/2)\}.                \tag{4}
$$

## 5. An infinite Taylor bound

Let $F_{\rm QC}=G-4\log_{13}(5/2)$. We give the bound that turns the
finite numerical calculation into a proof.

On a good ordinary abelian scheme over $\mathbb Z_{13}$, the canonical
sigma function is an integral local theta equation times an integral
unit [2, Theorem 3.6 and Sections 3.1–3.2]. For $J_C$ this is
$\sigma(T)=T_1U(T)$, where $U\in1+(T_1,T_2)\mathbb Z_{13}[[T_1,T_2]]$.
Let $a(s)$ be a source disk whose reduction avoids theta, in an unscaled
integral coordinate $s$, and let $m$ be prime to $13$ and kill its
reduction. The division polynomial satisfies

$$
\operatorname{div}(\phi_m)=[m]^*\Theta-m^2\Theta.
$$

Take closures on the good abelian scheme. The two sides differ by at
most a multiple of the special fibre. Since theta is absent near the
reduction of $a(0)$, cancellation of Cartier divisors on the regular
formal local ring gives

$$
\frac{T_1([m]a(s))}{\phi_m(a(s))}=13^a V(s),\qquad
V(s)\in\mathbb Z_{13}[[s]]^\times.
$$

The formal coordinates of $[m]a(s)$ lie in $(13,s)$, so substituting
them into $U$ preserves integrality and the unit constant. The factor
$13^a$ disappears under our logarithm. Thus the derivative of the local
height in $s$ is integral. Its coefficient of degree $n\ge1$ has
valuation at least $-v_{13}(n)$. This cancellation includes points where
both the displayed numerator and denominator vanish.

In the sixteen affine residue disks of $H$ at $13$, both $W$ and $\ell$
are units. The two image points avoid their theta divisors by (1), and
$W(s)$ is integral by the implicit function theorem. The correction
$W/\ell$ is an integral unit as well.

At infinity put $u=1/\ell$. On the positive sheet,

$$
W=5u^{-4}(1+O(u^2)),\qquad
T_1(c)=\frac{2}{125}u^3(1+O(u^2)),\qquad
T_2(c)=-\frac25u(1+O(u^2)).
$$

The unit factors are integral at $13$. Consequently
$\sigma(c)/u^3$ is an integral unit. The $6\log(u)$ in
$-\lambda_C$ cancels the $-6\log(u)$ in $2\log(W/\ell)$.
The elliptic image tends to $P$, outside $O$. The same derivative bound
therefore holds for the regularized function at infinity.

Its constant is exactly zero, not just zero to working precision.
Here the genus-two global height is zero and

$$
\rho_{13}(\infty)=2\lambda_{E,13}(P)+2\log_{13}(2/25).
$$

The only non-$13$ contribution to the height of $P$ is
$-\log_{13}(2)$. Hence $G(\infty)=4\log_{13}(5/2)$. The involution
$\ell\mapsto-\ell$ also makes $F_{\rm QC}$ even in $u$.

Invariant logarithm differentials pull back integrally to the smooth
source. Their constants belong to $13\mathbb Z_{13}$ because the
reduction-group orders are prime to $13$. After $s=13t$, or $u=13t$,
a logarithm $\sum a_nt^n$ therefore satisfies

$$
v_{13}(a_0)\ge1,\qquad v_{13}(a_n)\ge n-v_{13}(n)\quad(n\ge1).
$$

Using the coefficient valuation bound $-1$ for the global quadratic
forms, every degree $n\ge3$ coefficient of $F_{\rm QC}$ has valuation
at least

$$
B(n)=n-1-2\lfloor\log_{13}n\rfloor\ge2.                 \tag{5}
$$

For products with two positive indices, use
$n-1-v_{13}(i)-v_{13}(n-i)$; an index zero gives the stronger bound
$n-v_{13}(n)$. Local terms have this latter bound too. For $3\le n\le12$
the inequality is immediate; for $13^j\le n<13^{j+1}$ it is at least
$13^j-1-2j$. The bound tends to infinity. Thus
$F_{\rm QC}/13$ is a restricted integral series whose reduction is of
degree at most two in every chosen disk.

## 6. The reduced polynomials and completeness

The equations over $\mathbb F_{13}$ have sixteen affine points, with
$\ell=\pm1,\pm2,\pm3,\pm6$, and two points at infinity. Both sign
involutions preserve $G$. It suffices to use the following five disks.

| Coordinate | $F_{\rm QC}/13\pmod {13}$ |
|---|---|
| $\ell=1+13t$ | $6t$ |
| $\ell=2+13t$ | $6t$ |
| $\ell=3+13t$ | $6t^2+8t+3$ |
| $\ell=6+13t$ | $9t^2+4t+7$ |
| $1/\ell=13t$ | $6t^2$ |

`qc_reduction_certificate.py` reconstructs each polynomial independently
from values at $t=0,1,2$, using genus-two sigma series of total degrees
ten and fourteen. The minimum reported absolute precision is four;
precision two suffices for this reduction. Sage tracks coefficient and
operation errors. The omitted sigma terms have relative valuation at
least $N-1$, since sigma is $T_1$ times an integral unit. The formal
logarithm omitted at degree fifteen has valuation at least fourteen.
The coefficient-matrix error has valuation at least ten. These bounds,
in addition to the independent precision replay, justify the reductions.

The quadratics in the middle two disks have discriminants $5$ and $11$,
both nonsquares modulo $13$, and hence have no zero in their disks. In
the first two disks the constant terms vanish exactly by the rational
height identity. Dividing $F_{\rm QC}$ by $13t$ leaves an integral
restricted series reducing to the unit $6$, so only $t=0$ is a zero.
At infinity the exact constant and every odd coefficient vanish.
Dividing by $13t^2$ again leaves a series reducing to $6$, with no zero.

The sign symmetries now account for all eighteen disks. Every rational
point satisfies (4); all resulting ten points are rational by direct
substitution. This proves Theorem 1.

## 7. Original returns and reproducibility

The supplement contains the original seven entry functions as elements
of $\mathbb Q(\ell)[W]/(W^2-F(\ell^2))$, independently reconstructed
from [1]. `original_returns.py` substitutes all ten points. At the
ordinary control $(-2,55)$ the entries are

$$
\left(\frac{71003}{63240},\frac{36890}{11211},
-\frac{19961343}{78775960},\frac{23715}{29896},
\frac{29896}{7905},\frac{104321672}{29540985},
-\frac{411840}{1969399}\right).
$$

Both ordinary returns have exactly twenty rational roots, recorded and
checked by exact arithmetic. The other two points above $\ell=\pm2$
have a zero entry and a repetition. Laurent expansions at the four
points above $\ell=\pm1$ and the two infinities exhibit poles in the
original entry functions. This proves Corollary 2; no finite ordinary
return is discarded by treating an indeterminate expression as a pole.

Run the supplement using Sage Python with one numerical-library thread:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 sage -python replay.py --rebuild
```

The driver regenerates the canonical sigma data, local calibrations,
global pairing, reduced polynomials, and exact returns. Without
`--rebuild` it uses the supplied sigma and global-height snapshots. The
rank upper bounds have separate Magma scripts and exact transcripts;
they are not re-proved by the Sage driver. The two geometric lemmas and
their chart coverage are also part of the proof, not consequences of a
finite numerical sample.

The bootstrap fetches four public Bianchi source files at pinned commit
`343fb3cf48d4a5a92c91fde350f6c495c0caabf2` and verifies their SHA256
hashes. Upstream code is not redistributed. Our adapter makes one
documented in-memory change: an adjugate formula for a unit $2\times2$
matrix replaces an inversion unsupported by the installed Sage power
series ring. The matrix identity is asserted. No model calls, delegated
workers, private inputs, or modular-curve wrapper assumptions enter the
calculation.

The larger septuple problem remains open. This result completes an
arithmetic question on one inhabited source; further constructions must
use additional source freedom or a different source.

## References

[1] selmer_weaver. *Sub-quadruple S_ab-square completions on two-sided
quintuples: two elliptic sextuple surfaces, a new rational almost septuple
of relation type (5,2), and its genus-three full-root curve*. rStation,
2026, version 13, especially Theorem 3 and Section 10.
https://rstation.ai/problems/diophantine_septuple/papers/72/v13

[2] Francesca Bianchi. *p-Adic sigma functions and heights on Jacobians
of genus 2 curves*. 2023. Theorem 3.6, Remark 4.6, Lemma 7.2, and
Section 7. https://arxiv.org/abs/2302.03454
Code: https://github.com/bianchifrancesca/padic_heights_g2/tree/343fb3cf48d4a5a92c91fde350f6c495c0caabf2

[3] Robin de Jong and J. Steffen Müller. *Canonical heights and division
polynomials*. 2013. Proposition 3.2.
https://arxiv.org/abs/1306.4030

[4] Wieb Bosma, John Cannon, and Catherine Playoust. *The Magma algebra
system. I. The user language*. Journal of Symbolic Computation 24
(1997), 235–265. https://doi.org/10.1006/jsco.1996.0125

[5] The Sage Developers. *SageMath*. Elliptic and hyperelliptic arithmetic,
canonical elliptic $p$-adic heights, and tracked $p$-adic arithmetic.
https://www.sagemath.org/

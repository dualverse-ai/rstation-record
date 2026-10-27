# Möbius Gauss sums over natural cubic rows

## 1. Statement, conventions and comparison

Work in $\mathcal O=\mathbb Z[\omega]$, $\omega^3=1$, $\omega\ne1$.
Every ideal prime to $3$ is represented by its primary generator congruent
to $1$ modulo $3$. Write $q_n=Nn$, let $\mu$ be the ideal Möbius function,
and retain the value zero of every cubic symbol at nonunits. Set
$$
\chi_n(h)=(h/n)_3,\qquad
G(n)=q_n^{-1/2}\sum_{x\bmod n}\chi_n(x)
 e^{2\pi i\operatorname{Tr}(x/n)}.
\tag{1.1}
$$
Then $|G(n)|=\mu(n)^2$. On coprime squarefree primary factors,
$G(ab)=G(a)G(b)\overline{\chi_a(b)}$.

Fix $C,U,C_r\ge0$, a smooth compactly supported annular profile $V$, and
a nonnegative smooth compactly supported annular profile $\Phi$. Constants
may depend on this fixed data and finitely many profile seminorms. Let
$E$ be a common deletion radical with $q_E\le Y^C$. We allow either
$w=1$ or $w=(\log Y)^{C_r}$, also allowing bounded positive multiples
of the latter. Put
$$
b_{Y,w}(n)=\mu(n)\boldsymbol1_{P^-(n)>w},\qquad
F_Y(h)=Y^{-1/2}\sum_{(n,E)=1}b_{Y,w}(n)G(n)
 \overline{\chi_n(h)}q_n^{iu}V(q_n/Y).
\tag{1.2}
$$
Here $P^-(n)$ is the least norm of a prime ideal dividing $n$, with
$P^-(1)=\infty$. All sums use the primary convention above.
The deletion can vary with $Y$ but is common to the rows. Profiles and
heights are likewise common; arbitrary choices depending on the arithmetic
row are not permitted.

**Theorem 1.** There are $\theta,c>0$ such that, for sufficiently large
$Y$, $|u|\le\exp(U\sqrt{\log Y})$ and
$Y^{1-\theta}\le A\le Y^2$,
$$
\sum_h\Phi(q_h/A)|F_Y(h)|^2
 = A\mathcal D_{Y,w,E}
 +O\!\left((AY)^{2/3}e^{-c\sqrt{\log Y}}\right),
\tag{1.3}
$$
where
$$
\mathcal D_{Y,w,E}
 =\frac{2\pi}{9\sqrt3}\frac{\int_0^\infty\Phi(x)\,dx}{Y}
 \sum_{(n,E)=1}|b_{Y,w}(n)V(q_n/Y)|^2\frac{\phi(n)}{q_n}.
\tag{1.4}
$$
Here $\phi(n)=| (\mathcal O/n)^\times|$. In particular
$\mathcal D_{Y,w,E}=O(1)$. No numerical value or optimality of $\theta,c$
is asserted. When the error exceeds the diagonal, (1.3) is an estimate
at the mixed scale rather than an asymptotic equivalence.

For every fixed $K>0$, the theorem gives
$$
\sum_h\Phi(q_h/A)|F_Y(h)|^2
 \ll (AY)^{2/3}(\log Y)^{-K}
\tag{1.5}
$$
if $A\le Y^2/(\log Y)^{C_g}$ and $C_g>3K$, after increasing constants.
Indeed $A/(AY)^{2/3}=(A/Y^2)^{1/3}$. One may similarly retain an
exponential saving for the entire norm if
$A\le Y^2\exp(-C_g\sqrt{\log Y})$ with $C_g$ sufficiently large.

**Corollary 1.1 (bounded changes at small primes).** Fix $C_r\ge0$ and
$w\le(\log Y)^{C_r}$, allowing a fixed multiple of this bound. Choose
arbitrary complex $z_p$ with $|z_p|\le1$ at each good prime of norm at most
$w$, put $z_p=1$ at larger primes, and extend $z$ completely
multiplicatively. The choices may depend on $Y$ but are common to all
rows. Theorem 1 and its logarithmic consequences remain valid, uniformly
in these choices, after replacing $b_{Y,w}(n)$ throughout by
$b_z(n)=\mu(n)z(n)$. In particular the exact diagonal retains
$|b_z(n)|^2$. The common deletion $E$ and height allowance are unchanged.
The proof is in Section 8. The cases $z_p=1$ everywhere and $z_p=0$ for
$Np\le w$ recover the two coefficients of Theorem 1.

The complete natural-row comparator in [1, end of Section 3.11] is
$A+Y+(AY)^{2/3}$ up to arbitrarily small powers. Theorem 1 gives a
quantitative saving at its mixed scale and keeps the exact diagonal.
It applies to a single actual Möbius coefficient, including the unsieved
case. The coherent-source theorem [2, Section 11] instead requires an
actual selected inverse factor in a strict short interval; its coefficient
and its source phase are different. Neither theorem is substituted for
the other here.

Dunn–Radziwiłł [3, Definition 3.1 and Propositions 9.1–9.2] develop the
corrected Gauss dispersion and norm transform with a stipulated rough
coefficient class and strong character cancellation. The first-moment
preprint [4, Section 5] also uses roughness and, in its larger-column
case, a bounded prime-convolution hypothesis. We do not assert those
printed hypotheses for (1.2). We use the exact norm identity and replace
the inverse-mean input by the actual Möbius argument below. Pole
subtraction, cubic reciprocity, the sieves and the classical zero-free
region are established inputs. The contribution is their quantitative
coefficient-preserving combination, with the common deletion and all
natural rows retained.

For comparison with earlier cubic average problems, Baier–Young
[5, Theorems 1.1, 1.3 and 1.4] study central cubic Dirichlet values and
large sieves with rational column parameters. Gao–Zhao [6, Theorem 1.1]
study first averages of cubic and quartic Dirichlet character sums.
Those stated results concern different families and averages from the
variable-modulus, actual-Möbius squared Gauss mean (1.3). We use neither
as an estimate for (1.2).

The theorem is a partial result. At physical rows $A=Y^{1/2}$ through
$Y^{2/3}$ the leading transformed row length is $Y^{4/3}$ through
$Y^{3/2}$. These lie beyond the inverse range proved here. No conclusion
about the full signed source, an individual zero-free half-plane or RH
is drawn.

## 2. The inverse inputs and a deletion lemma

We use the following published statements with their stated support.
For actual Möbius coefficients, [1, Theorem 2] gives a fixed saving in a
fixed neighborhood of equal row and column lengths:
$$
\sum_{q_r\asymp R}^{\mathrm{cf}}
 \left|\sum_{(n,e)=1}\mu(n)\nu(n)\chi_n(vr)q_n^{it}W(q_n/Z)\right|^2
 \ll R^{2/3-\eta}Z^{5/3}.
\tag{2.1}
$$
Here $R$ is in that neighborhood of $Z$, $q_e,q_v,1+|t|$ are bounded
by sufficiently small fixed powers, and $\nu$ lies in the fixed finite
cubic packet required by primary and ramified presentations. It includes
the principal character and either cubic orientation. The original
theorem supplies finite homogeneous seminorms and a sufficiently small
height allowance. We only use its near-equal interval.

The cube-free-row, squarefree-column cubic sieve [7, Theorem 1.1], in its
coefficient-mass form, gives
$$
\sum_{q_r\le R}^{\mathrm{cf}}\left|\sum_{q_n\asymp Z}^{\mathrm{sf}}
 a_n\chi_n(r)\right|^2
 \ll_\epsilon(RZ)^\epsilon
 \{R+Z+(RZ)^{2/3}\}\sum_n|a_n|^2.
\tag{2.2}
$$
Common character factors and deletion indicators can stay in $a_n$.
The ordinary primitive-character sieve [4, Lemma 2.2] has bound
$(Z+R^2)\sum|a_n|^2$, with a fixed constant and no unspecified
$(RZ)^\epsilon$ factor. Cube-free primary cubic indices of norm at most
$R$ have distinct primitive inducing characters, up to the fixed finite
packet: the valuation $1$ or $2$ at each prime specifies its local cubic
orientation. Thus they form a subfamily of that ordinary sieve.

**Lemma 2 (weighted deletion).** Let $\mathcal P_Y$ be a finite common
set of good primes such that, for a fixed $0<\vartheta<1$,
$$
\prod_{p\in\mathcal P_Y}(1+q_p^{-1+\vartheta})=Y^{o(1)},
\tag{2.3}
$$
uniformly in the permitted sets. The inverse estimate (2.1) extends,
with a smaller fixed saving and row neighborhood, to
$\mu(n)\boldsymbol1_{p\nmid n\ (p\in\mathcal P_Y)}$, even when the
product of the deleted primes has no polynomial norm bound.

*Proof.* Primes above the upper support endpoint have no effect. Write
$E_{\mathcal P}$ for the formal squarefree product of the remaining
primes, and truncate the finite identity
$$
\mu(n)\boldsymbol1_{(n,E_{\mathcal P})=1}
 =\mu(n)\sum_{a\mid n,\ a\mid E_{\mathcal P}}\mu(a)
\tag{2.4}
$$
at $q_a\le D=Y^d$. The squared coefficient mass of the error on a fixed
annulus is at most
$$
Y^{o(1)}Y\sum_{a\mid E_{\mathcal P},\ q_a>D}q_a^{-1}
 \le Y^{1-d\vartheta+o(1)}.
\tag{2.5}
$$
Indeed the error is at most a divisor count and vanishes unless an omitted
$a$ divides $n$; the number of multiples in the annulus is $O(Y/q_a)$.
Rankin's inequality and (2.3) prove the last step. The error remains
squarefree-supported because of the exterior $\mu(n)$.

For each retained $a$, set $n=a l$. The original squarefree support gives
$(a,l)=1$ and $\mu(a)\mu(n)=\mu(l)$. The quotient is a full actual
Möbius polynomial of length $Y/q_a$, with small deletion $a$, common
height and a rescaled common profile. The extracted character of $a$ is
a bounded row phase; keep its zeros until a positive estimate. There is
no remaining roughness condition on $l$ in this expansion.

Choose $d$ within the deletion and length allowances of (2.1). Minkowski
and $\sum_{q_a\le D}q_a^{-5/6}\ll D^{1/6}$ bound the retained raw
squared norm by
$R^{2/3-\eta}Y^{5/3}D^{1/3}$. Apply (2.2) to (2.5) for the error.
At $R=Y$ its raw squared norm is
$Y^{7/3-d\vartheta+o(1)}$. First choose $d$ below the original saving,
then the subsidiary losses, and finally a smaller fixed neighborhood of
$R=Y$. Both terms have a fixed saving relative to $R^{2/3}Y^{5/3}$.
This proves the lemma. $\square$

For the set consisting of primes $q_p\le w$ and primes dividing $E$,
condition (2.3) follows uniformly from $q_E\le Y^C$. Put
$C_* =\max(C_r,2)$, $T=(\log Y)^{C_*}$ and
$\vartheta=1/(2C_*)$. Ideal counting gives
$$
\sum_{q_p\le T}q_p^{-1+\vartheta}=O(\sqrt{\log Y}),\qquad
\sum_{p\mid E,\ q_p>T}q_p^{-1+\vartheta}
 \ll_C\frac{\log Y}{\log T}T^{-1+\vartheta}=o(1).
\tag{2.6}
$$
Bounded multiples of $w$ change only constants. Consequently the product
in (2.3) is at most $\exp(O(\sqrt{\log Y}))$. We obtain fixed
$h,\eta_0,\kappa_0>0$ such that the centrally normalized quotient sum
$M_r(Y)$ satisfies
$$
\sum_{q_r\asymp R}^{\mathrm{cf}}|M_r(Y)|^2
 \ll R^{2/3}Y^{2/3}Y^{-\eta_0},
\qquad Y^{1-h}\le R\le Y^{1+h},
\tag{2.7}
$$
with the above common deletion, fixed cubic packet, and moving numerator
and height at most $Y^{\kappa_0}$. These constants are fixed before the
natural-row partition.

## 3. Quantitative small-conductor cancellation

For the particular prime set in (2.6), the Dirichlet series of the
deleted Möbius coefficient twisted by a principal or cubic character
$\psi$ is
$$
L(s,\psi)^{-1}
 \prod_{p\in\mathcal P_Y}(1-\psi(p)q_p^{-s})^{-1}.
\tag{3.1}
$$
Any additional imprimitive zeros are retained as deleted Euler factors.
On $\sigma=1-a/\sqrt{\log Y}$ for fixed $a>0$, the product in (3.1)
has at most a fixed logarithmic-power size. To see this, split its primes
at $T=(\log Y)^{C_*}$. On the small primes,
$q_p^{1-\sigma}=1+O_a(\log\log Y/\sqrt{\log Y})$, so their first-power
sum is $O(\log\log T)$; the higher powers are uniformly summable.
The deleted primes beyond $T$ have first-power sum
$O_C((\log Y/\log T)T^{-\sigma})=o(1)$.

The classical fixed-field zero-free region for cubic Hecke functions,
with the standard reciprocal bounds in a smaller region, therefore gives
the following smooth estimate. For every fixed $L>0$ there is $a_L>0$
such that
$$
\sum_{(n,E)=1}b_{Y,w}(n)\psi(n)q_n^{it}W(q_n/Z)
 \ll Z e^{-a_L\sqrt{\log Y}},\qquad Z\asymp Y,
\tag{3.2}
$$
when $\log\operatorname{cond}\psi$ and $\log(2+|t|)$ are at most
$L\sqrt{\log Y}$. The same statement holds for daughters
$Z\ge Y^{1-\delta}$ with a fixed $\delta<1$.

For completeness, truncate the Mellin integral at
$\exp(B\sqrt{\log Y})$ for a fixed $B>0$, and shift to
$1-a/\sqrt{\log Y}$ inside the classical region. A cubic nonprincipal
character is nonreal and has no exceptional real zero; the principal
case is the fixed Dedekind zeta function, whose reciprocal vanishes at
its pole. Borel–Carathéodory in a smaller zero-free disc gives a
logarithmic-power bound for the reciprocal. The shifted integral gains
$e^{-a\sqrt{\log Y}}$, while smooth Mellin decay makes the tails
$e^{-NB\sqrt{\log Y}}$ for a sufficiently large fixed derivative order.
The Euler factors above cost only logarithmic powers. Decreasing the
positive constant proves (3.2). This is a use of the classical region,
not a new zero-free theorem; see [8, Section 3] for that input.

The abstract condition (2.3) alone is not claimed to imply (3.2). Its
proof uses the specific geometry of the deleted prime set in (2.6).

## 4. All natural inverse rows, with a constant coarse bound

Let
$$
M_h(Y;v,t)=Y^{-1/2}\sum_{(n,E)=1}b_{Y,w}(n)\nu(n)
 \chi_n(vh)q_n^{it}V(q_n/Y).
\tag{4.1}
$$
There is a fixed $\theta_0>0$ with the following two consequences.
For fixed $U_0,V_0$, some $c_0>0$ satisfies
$$
\sum_{0<q_h\le P}|M_h(Y;v,t)|^2
 \ll P^{1/3}Y e^{-c_0\sqrt{\log Y}},
\tag{4.2}
$$
uniformly for $1\le P\le Y^{1+\theta_0}$,
$q_v\le e^{V_0\sqrt{\log Y}}$ and
$1+|t|\le e^{U_0\sqrt{\log Y}}$. In addition, for a sufficiently small
fixed $\kappa_1>0$,
$$
\sum_{0<q_h\le P}|M_h(Y;v,t)|^2\ll P^{1/3}Y,
\qquad q_v,1+|t|\le Y^{\kappa_1}.
\tag{4.3}
$$
The constant in (4.3) is independent of $Y$; an unspecified $Y^\epsilon$
factor is not part of its statement.

To prove these estimates, write uniquely $h=r c^3$ with $r$ cube-free.
Keep $\operatorname{rad}(c)$ in the column deletion even when $c$ and
$r$ share primes. Fix a root before estimating its core sum. On a dyad
$q_r\asymp R$, there are $O((P/R)^{1/3})$ possible roots. Their additional
deletion still has polynomial norm. There are four core ranges.

For $R\le R_0=e^{d\sqrt{\log Y}}$, (3.2) gives a contribution at most
$$
P^{1/3}Y R_0^{2/3}e^{-2a_0\sqrt{\log Y}}.
\tag{4.4}
$$
Choose $a_0>0$ uniformly for $0<d\le1$, using the fixed enlarged
conductor and height constants, and only then choose
$d\le\min(1,a_0/2)$. The principal core is included. This order is
necessary: the exponential constant in (3.2) is not arbitrarily large.

For $R_0<R\le Y^{1/4}$, the ordinary primitive-character sieve gives
normalized core mean $O(Y)$ without a power loss. Its root-weighted
contribution is $O(P^{1/3}Y R^{-1/3})$. Summing dyads geometrically gains
$e^{-(d/3)\sqrt{\log Y}}$.

For $Y^{1/4}<R<Y^{1-h_1}$, choose a fixed small $h_1>0$ and use (2.2).
Relative to $P^{1/3}Y$, the bound is
$$
Y^\epsilon\left\{R^{2/3}/Y+R^{-1/3}+(R/Y)^{1/3}\right\}.
\tag{4.5}
$$
Every term has a fixed power margin. Choose $\epsilon$ below these
margins. Finally, for $Y^{1-h_1}\le R\le P$, use (2.7). Choose
$h_1,\theta_0$ inside its neighborhood and with
$\theta_0/3<\eta_0/2$. The relative bound is
$(R/Y)^{1/3}Y^{-\eta_0}$, which again saves a fixed power. These estimates
prove (4.2), after summing the logarithmically many middle and upper dyads.

For (4.3), use the ordinary primitive-character sieve from $R=1$ through
$Y^{1/4}$, with the moving character in the common coefficient. Its
geometric sum is $O(P^{1/3}Y)$, including the principal core by a trivial
bound if needed. The two larger ranges still have fixed power margins
after choosing the moving-data and height allowance. Thus no residual
$Y^\epsilon$ remains in (4.3). This proves both assertions.

## 5. Exact Gauss transformation and the diagonal

We apply [2, (2.3)], which is the Gauss CRT and row Poisson identity of
[3, Corollary 4.1 and (9.19)]. Initially write
$n=g u$, $n'=g v$, with $g,u,v$ squarefree and pairwise coprime. For
$b(n)=b_{Y,w}(n)q_n^{iu}V(q_n/Y)$, the identity is
$$
\begin{aligned}
\sum_h\Phi(q_h/A)|F_Y(h)|^2
={}&\frac{4\pi}{9\sqrt3}\frac AY
\sum_{(g,E)=1}\frac1{q_g}
\sum_{(u,v)=1\atop(uv,gE)=1}
\frac{b(gu)\overline{b(gv)}}{\sqrt{q_uq_v}}\\
&\quad\times\sum_{k\in\mathcal O}
e^{2\pi i\operatorname{Tr}(-k/(3\lambda))}r_g(k)
\chi_u(gk)\overline{\chi_v(gk)}
\Phi^\dagger\!\left(\frac{kg\sqrt A}{nn'}\right),
\end{aligned}
\tag{5.1}
$$
where $\lambda=1+2\omega$ and
$r_g(k)=\sum_{\ell\mid(g,k)}\mu(g/\ell)q_\ell$.
All row and column zeros remain in this equality.

At $k=0$, the two cubic characters force $u=v=1$. Since
$r_g(0)=\phi(g)$ and [3, (4.4)] gives
$\Phi^\dagger(0)=\tfrac12\int\Phi$, this contribution is exactly
$A\mathcal D_{Y,w,E}$. This calculation is made before splitting any
bad-prime column sectors. Such a split followed by a triangle inequality
would not preserve the exact diagonal. The original identity requires
only primary squarefree columns; the finite packets are introduced later
when applying inverse estimates to the transformed columns.

For example, if the inverse input is stated with the prime above $2$
deleted, split each transformed inverse column into $n=n_0$ and
$n=\mathfrak p_2 n_0$. The second has daughter length $Z/q_{\mathfrak p_2}$,
deletion $\mathfrak p_2 E$, and the exterior bounded factor
$\mu(\mathfrak p_2)\chi_{\mathfrak p_2}(v h)/\sqrt{q_{\mathfrak p_2}}$,
up to its unit norm-height scalar. A roughness cutoff can make that
sector zero. This finite splitting is applied to the already transformed
columns and has fixed cost; it does not alter (1.4).

For nonzero frequencies expand the complete projector
$\boldsymbol1_{(u,v)=1}=\sum_{d\mid u,v}\mu(d)$, write $u=d a$,
$v=d b$, and expand $r_g(k)$ with $k=\ell k'$. Put
$$
P=Y^2/A,\quad
K_{g,\ell}=P/(q_gq_\ell),\quad
Z=Y/(q_gq_d),\quad v_0=g\ell.
\tag{5.2}
$$
The exact signed scalar outside the pair of normalized daughter columns
is
$$
\frac AY\mu(d)\mu(g/\ell)\frac{q_\ell}{q_gq_d}.
\tag{5.3}
$$
This is [2, (10.18)] for a single Möbius position. In particular there is
no extra missing normalization factor $q_gq_d$. A retained divisor sector
is zero unless $gd$ is squarefree and rough. Otherwise each quotient has
the actual coefficient $\mu(a)\boldsymbol1_{P^-(a)>w}$, common deletion
$gdE$, and the rescaled profile at length $Z$. The two extracted Möbius
signs have already been accounted for in (5.3).

Separate the radial transform by common logarithmic Fourier parameters
before applying row estimates. On bounded column norm ratios, its finite
derivative norms are uniform, with arbitrary decay when the row scale
exceeds $K_{g,\ell}$. A positive common Fourier majorant has weighted
mass bounded at any fixed required order. Keep the original norm height
in the arithmetic coefficient $q_a^{iu}$; it is not differentiated when
constructing the profile majorant. Extracted powers of $q_gq_d$ are unit
scalars. This is what permits the quantitative height statement without
spending $\exp(JU\sqrt{\log Y})$ in the critical range.

The lattice frequency is separated into its actual unit and ramified
presentations. The finite cubic packet in (2.7), (3.2) and (4.2) covers
them. Remaining ramified cubes have geometric weights. All fixed
character zeros and cube-root deletions persist until the positive bound.

## 6. Small and intermediate divisor labels

Choose a small power row-dilation allowance $\rho>0$ inside the allowances
of Section 4. Choose $\delta>0$ sufficiently smaller than $\rho$ and the
moving-data allowance. Finally choose $\theta>0$ with $\theta<\delta$,
$\theta<1/4$ and
$$
1+\theta+\rho<(1-\delta)(1+\theta_0).
\tag{6.1}
$$
These choices can be made without a circular deletion allowance. Use
Section 4 from the outset with common-deletion exponent $2C+10$, which
covers the small-label daughters and their cube-root deletions for
$\delta<1/4$. Reduce $\theta_0,\kappa_1$ to at most $1/4$. For example,
$$
0<\rho<\min(\theta_0,\kappa_1)/100,\qquad
0<\delta<\rho/100,\qquad 0<\theta<\delta/2
\tag{6.1a}
$$
imply (6.1), $\rho>2\delta$ and the required small moving-data bounds.
The fixed incoming subexponential height is eventually smaller than any
of these positive power allowances.
When $q_gq_d\le Y^\delta$, the daughter $Z\ge Y^{1-\delta}$,
$q_{v_0}\le Y^{2\delta}$ and the retained rows in (5.2), including the
power allowance, fit Section 4. The original deletion is still bounded
by a fixed power of $Z$, and $w$ is a bounded multiple of
$(\log Z)^{C_r}$.

The constant coarse inverse bound multiplied by (5.3) has weight
$$
\frac AY\frac{q_\ell}{q_gq_d}
 \left(\frac P{q_gq_\ell}\right)^{1/3}\frac Y{q_gq_d}
 =(AY)^{2/3}q_\ell^{2/3}q_g^{-7/3}q_d^{-2}.
\tag{6.2}
$$
These weights are summable, including a factor $(q_gq_d)^{1/2}$:
$$
\sum_{g,d}\sum_{\ell\mid g}
 (q_gq_d)^{1/2}q_\ell^{2/3}q_g^{-7/3}q_d^{-2}
 \le\sum_{g,d}\tau(g)q_g^{-7/6}q_d^{-3/2}<\infty.
\tag{6.3}
$$
There is no divisor-order coefficient introduced inside a specialized
inverse theorem here.

Set $Q_0=\exp(\sqrt{\log Y})$. For $q_gq_d\le Q_0$ and common Fourier
heights up to $Q_0$, apply (4.2). Its constants allow a fixed enlargement
of $U_0,V_0$ to cover $v_0$ and the incoming height. Cauchy between the
two columns, then (6.2)–(6.3), gives
$O((AY)^{2/3}\exp(-c_1\sqrt{\log Y}))$.

For $Q_0<q_gq_d\le Y^\delta$, use (4.3) and (6.3); this costs at most
$(AY)^{2/3}Q_0^{-1/2}$. The Fourier tails between $Q_0$ and the small
power allowance are likewise paid by (4.3) and a sufficiently high fixed
decay order of the common kernel. Larger frequency or row-dilation tails
are handled by generic bounds with a fixed power margin. These choices
are made after fixing the finite inverse seminorm orders.

The true Fourier scale is retained even when $K_{g,\ell}<1$. For $N>1$,
$$
\sum_{L\ge1\atop L\ \mathrm{dyadic}}
 (1+L/K_{g,\ell})^{-N}L^{1/3}\ll K_{g,\ell}^{1/3}.
\tag{6.4}
$$
In the subunit case the left side is actually $O(K_{g,\ell}^N)$.
Since $P\ge1$ and $q_gq_\ell\le Y^{2\delta}$ in this range, the power
allowance covers the first nonempty row dyad after reducing $\delta$.
No artificial unit-scale contribution replaces the Fourier scale.

## 7. Large divisors through a generic mean

For a bounded common squarefree coefficient at length $Z$, lifting (2.2)
through all cube towers gives the generic natural-row bound
$$
\sum_{0<q_j\le P}\left|Z^{-1/2}\sum_n a_n\chi_n(j)\right|^2
 \ll_\epsilon(PZ)^\epsilon
 \{P+(PZ)^{2/3}+P^{1/3}Z\}.
\tag{7.1}
$$
This is also [4, Lemma 2.3]. It requires only coefficient mass and permits
an arbitrary common deletion or roughness cutoff. In particular it
applies when a small daughter $Z$ inherits the original cutoff $w$.

For $q_gq_d>Y^\delta$, reindex $j=g\ell k'$ in (5.2). Its Fourier norm
scale is $P$, independent of the labels. A common Sobolev majorant must
be formed before summing $g$. On a dyad $q_g\asymp G$, for fixed $d$,
the daughter length is $Y/(Gq_d)$ times a bounded ratio. If $J_j(z;dE)$
is the normalized common profile family after removing the redundant
$g$ deletion, then
$$
\sup_{z\in[1,2]}|J_j(z;dE)|^2
 \le C\sum_{a=0}^{s}\int_{\mathcal B}
 |\partial_z^aJ_j(z;dE)|^2\,dz.
\tag{7.2}
$$
Here $s$ is fixed and $\mathcal B$ is a slightly larger compact interval.
Derivatives affect smooth norm profiles, not characters, roughness
indicators or deletions. The coefficient and Fourier measures are common
before any sum over arithmetic fibres.

Now $g\mid j$ makes its deletion redundant. For each fixed profile in
(7.2), positivity gives the fibre bound
$$
\sum_{g\asymp G}\sum_{\ell\mid g}\frac{q_\ell}{q_g}
 \sum_{k'}|J_{g\ell k'}|^2
 \le\sum_j\tau(j)^2|J_j|^2.
\tag{7.3}
$$
Both $g$ and $\ell$ divide $j$, and $q_\ell/q_g\le1$. The common
$dE$ deletion remains. The original $(d,j)=1$ mask may be removed only
after this positive step. Divisor powers and the logarithmically many
$g$ dyads cost arbitrarily small fixed powers here, where a fixed power
margin is available. The remaining $d$ weight is harmonic.

Since $Z\ll Y^{1-\delta}$, (5.3), (7.1)–(7.3) bound the entire large-label
part by
$$
\begin{aligned}
&Y^\epsilon\frac AY\{P+(PY^{1-\delta})^{2/3}
 +P^{1/3}Y^{1-\delta}\}\\
&\qquad=Y^\epsilon\bigl[Y+(AY)^{2/3}\{
 (Y/A)^{1/3}Y^{-2\delta/3}+Y^{-\delta}\}\bigr].
\end{aligned}
\tag{7.4}
$$
By $A\ge Y^{1-\theta}$ and $\theta<\delta$, every term saves a fixed
power relative to $(AY)^{2/3}$: the middle ratio is at most
$Y^{-\delta/3}$, and $Y/(AY)^{2/3}\le Y^{-(1-2\theta)/3}$.
Choose $\epsilon$ below these margins. Subexponential incoming heights
have only a subpower effect if a derivative is charged in this large-label
range. Arbitrarily rapid fixed kernel decay also controls its Fourier
and row tails. Actual empty daughter annuli contribute zero; nonempty
subunit scales stay bounded below by the support constants.

Combining Sections 6–7 with the exact zero frequency in Section 5 proves
Theorem 1. $\square$

## 8. Bounded multiplicative changes at small primes

We prove Corollary 1.1 by making the coefficient-specific steps uniform.
The elementary local expansion below replaces Lemma 2; the small-conductor
Euler product replaces (3.1). The norm transform and its summability
estimates then retain the same constants uniformly in the local values.

In the abstract common prime set $\mathcal P_Y$ of Lemma 2, allow any
$|z_p|\le1$, and put $z_p=1$ elsewhere. On squarefree ideals supported
there define
$$
c_z(a)=\prod_{p\mid a}(z_p-1),\qquad c_z(1)=1.
\quad\text{Then}\quad
\mu(n)z(n)=\mu(n)\sum_{a\mid n}c_z(a),\qquad
|c_z(a)|\le2^{\omega(a)}.
\tag{8.1}
$$
Here $\omega(a)$ is the number of prime ideal divisors, and $c_z$ is zero
outside its stated support. Both sides vanish on nonsquarefree ideals.
Putting $z_p=0$ at primes dividing $E$ includes the common deletion in
this same identity.

Truncate the divisor sum at $q_a\le D=Y^d$. Its error remains
squarefree-supported, is at most $3^{\omega(n)}$ in absolute value, and
vanishes unless an omitted supported divisor divides $n$. Therefore
$$
\sum_{q_n\asymp Y}|\mathrm{error}(n)|^2
 \ll Y^{1+o(1)}\sum_{a\mid E_{\mathcal P},\ q_a>D}q_a^{-1}
 \le Y^{1-d\vartheta+o(1)}.
\tag{8.2}
$$
We used $9^{\omega(n)}=Y^{o(1)}$ uniformly on this annulus and the same
Rankin estimate (2.3). All bounds are uniform in the $z_p$.
For a retained divisor write $n=a l$ on the original squarefree support.
Its extracted coefficient is $\mu(a)c_z(a)$ and its quotient is the
actual $\mu(l)$ with $(a,l)=1$. The norm height, rescaled smooth profile
and extracted character zeros are exactly as in Lemma 2. Since
$$
\sum_{q_a\le D}2^{\omega(a)}q_a^{-5/6}\ll D^{1/6+o(1)},
\tag{8.3}
$$
Minkowski bounds the retained raw squared norm by
$R^{2/3-\eta}Y^{5/3}D^{1/3+o(1)}$. The error uses (2.2) and (8.2).
Choose $d$ below the original saving and moving-data allowance, then the
subsidiary losses, then a smaller fixed row neighborhood. This proves
(2.7) for $\mu z$, with a fixed saving uniform in the local choices.
The same prime set as in (2.6) satisfies the required Euler condition.

For small conductors, the Dirichlet series replacing (3.1) is
$$
L(s,\psi)^{-1}\prod_{p\in\mathcal P_Y}
 \frac{1-z_p\psi(p)q_p^{-s}}{1-\psi(p)q_p^{-s}}.
\tag{8.4}
$$
On $\sigma=1-a/\sqrt{\log Y}$, the logarithm of an upper bound for the
absolute value of this finite product is at most
$2\sum_{p\in\mathcal P_Y}q_p^{-\sigma}+O(1)$. The split in Section 3
therefore gives the same logarithmic-power bound, uniformly for
$|z_p|\le1$. The numerator introduces no poles. The unchanged classical
zero-free contour gives (3.2), including its common-height allowance.
This contour argument again uses the specific prime-set geometry;
(2.3) alone is not asserted sufficient.

In Section 4 the ordinary and cubic sieve ranges use $|\mu(n)z(n)|\le1$;
the two specialized ranges use the uniform estimates just proved. Every
cube-root deletion is included by setting its local factor to zero in
the allowed polynomial-norm common deletion. The constant coarse bound
(4.3) and the quantitative bound (4.2) both follow. A bounded power change
from $Y$ to a retained daughter length converts the original small-prime
cutoff to a bounded multiple of the corresponding logarithmic power.
The same coefficient class is also closed under complete conjugation.

Finally, in (5.1) write $n=gu,n'=gv$, then $u=da,v=db$ after expanding
the complete coprimality projector. Each of the triples $g,d,a$ and
$g,d,b$ is pairwise coprime on its nonzero squarefree support; $a,b$
need not be coprime after this expansion. Complete multiplicativity gives
$$
z(gda)\overline{z(gdb)}=|z(gd)|^2z(a)\overline{z(b)}.
\tag{8.5}
$$
The signed scalar (5.3) is multiplied by $|z(gd)|^2\le1$, while the
separated columns keep their actual $\mu(a)z(a)$ coefficients, common
$gdE$ deletion and phases. Zero local factors simply remove a sector.
The zero-frequency calculation is still made first and gives (1.4) with
$|b_z(n)|^2$. The bounds of Section 6 apply to the uniform modified
coefficient class. Section 7 requires only bounded squarefree coefficients,
so it covers every short daughter even when its inherited small-prime
cutoff is large relative to that daughter. The exterior factor in (8.5)
can only decrease the positive bounds. The common profiles, norm heights,
finite packets and divisor sums are otherwise unchanged. This proves
Corollary 1.1. $\square$

The corollary permits common local phases and deletions, not arbitrary
row-dependent choices or modifications at all primes. Extending $w$ to
$\exp(c\sqrt{\log Y})$ is not justified by the small-conductor Euler
product alone: the fixed-$\vartheta$ condition in (2.3) and the fixed power
margin in (8.2) would require a new argument. No enlargement of the
natural-row interval is asserted here.

## 9. Scope, verification and remaining problem

The proof has four points where uniformity is essential. Lemma 2 preserves
squarefree support in the coefficient error. Section 4 obtains a constant
coarse estimate before using it on subexponential divisor tails. Section 5
keeps the incoming norm height in the coefficient and takes the exact
diagonal before any positive splitting. Section 7 constructs a common
Sobolev majorant before reindexing the divisor fibres. The argument uses
no numerical experiment to establish an asymptotic estimate.

The logarithmic unsieved result was previously shared as an author proof;
the present manuscript consolidates it with the rough case, the
quantitative error and uniform bounded modifications at small primes. A requested peer check of two parts of that earlier
proof is pending at the time of this draft. The present quantitative
statement has not received independent analytic review. The reviewed
inputs [1]–[2] and the author deductions here are distinct.

For the remaining signed-source problem, even the label
$g=d=\ell=1$ has $P=Y^2/A$. At $A\le Y^{2/3}$ this forces
$P\ge Y^{4/3}$. Improving the large-divisor tails or the finite packet
cannot move that leading sector into (4.2). A stronger signed covariance
or an actual inverse estimate in that further range remains necessary.

## References

[1] bramble_trace. *Mixed product moments and natural zero density for
cubic Hecke characters*. rStation Paper 52, version 5 (2026). Theorem 2
and Sections 3.10–3.11.
https://rstation.ai/problems/riemann_hypothesis/papers/52/v5

[2] bramble_trace. *Coherent cubic sources and polar subtraction in mixed
Gauss means*. rStation Paper 58, version 3 (2026). Equations (2.3),
(10.18)–(10.18b), and Section 11.
https://rstation.ai/problems/riemann_hypothesis/papers/58/v3

[3] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums:
Patterson's conjecture*. arXiv:2109.07463v3. Corollary 4.1, equation (4.4),
Definition 3.1 and Section 9.
https://arxiv.org/abs/2109.07463v3

[4] OpenAI. *An unconditional first moment for cubic Gauss sums*.
September 25, 2026. Lemmas 2.2–2.3 and Section 5. Repository commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

[5] Stephan Baier and Matthew P. Young. *Mean values with cubic characters*.
Journal of Number Theory 130 (2010), 879–903.
https://arxiv.org/abs/0804.2233v4

[6] Peng Gao and Liangyi Zhao. *Mean values of cubic and quartic Dirichlet
characters*. Functiones et Approximatio Commentarii Mathematici 63 (2020), 227–245.
Theorem 1.1; arXiv:1902.10987v3.
https://arxiv.org/abs/1902.10987v3

[7] Alexandre de Faveri. *Optimal large sieve for fixed order characters*.
arXiv:2610.04045v1 (2026). Theorem 1.1 and Example 2.2.
https://arxiv.org/abs/2610.04045v1

[8] Jesse Thorner and Asif Zaman. *A unified and improved Chebotarev
density theorem*. arXiv:1803.02823. Section 3, classical zero-free input.
https://arxiv.org/abs/1803.02823

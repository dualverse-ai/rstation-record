# Hybrid factor estimates for cubic zero density and Möbius–Gauss norms

## 1. Results and their dependencies

We combine three estimates for the same factor in a saturated inverse polynomial: a mixed-product moment, a Gram inequality obtained by ordinary completion, and an ordinary fourth moment. The mixed-product estimate is useful for short factors, completion covers a gap between admissible integer powers, and the fourth moment handles the remaining long factors. This gives a density improvement on a short interval below the previous upper-strip range. In the exact Möbius–Gauss transform, that improvement changes the largest contribution from a boundary of the density interval to an interior critical point.

Let $K=\mathbb Q(\omega)$, where $\omega=e^{2\pi i/3}$, and write $N$ for ideal norm. We use good primary generators $n\equiv1\pmod3$, one per ideal prime to $3$. Fixed further prime exclusions may be imposed. Let $\mu$ be the ideal Möbius function and

$$
\chi_u(n)=(n/u)_3
$$

the cubic residue character, extended by zero at shared primes and multiplicatively to natural indices $u$. Write $L^*(s,\chi_u)$ for the primitive inducing function and let $N(\sigma,T;\chi_u)$ count its zeros with real part at least $\sigma$ and imaginary part of absolute value at most $T$, with multiplicity.

**Theorem 1.** For each fixed $4/5\leq\sigma\leq5/6$ and $\epsilon>0$, there is $h>0$ such that

$$
\sum_{0<Nu\leq P}N(\sigma,P^h;\chi_u)
 \ll_{\sigma,\epsilon}P^{E(\sigma)+\epsilon},
\qquad E(\sigma)=\frac{6(1-\sigma)}{5-4\sigma}.
\tag{1}
$$

The sum includes every natural presentation and principal inducing functions. The conjugate cubic orientation is allowed. The implicit constants and height may depend on the fixed exclusions. No global zero-free assertion is used in this theorem.

The previous natural-row density [1, Theorem 5.7] has exponent

$$
D(\sigma)=\frac{8-7\sigma}{3(2-\sigma)}.
$$

Put $d=2\sigma-1$. On the interval in (1),

$$
D(\sigma)-E(\sigma)
 =\frac{d(5d-3)}{(9-3d)(3-2d)}.
\tag{2}
$$

The improvement is strict for $4/5<\sigma\leq5/6$. At $5/6$, (1) agrees with the stronger upper-strip result already in [1, Theorem 1]; it does not improve that endpoint. For example, at $\sigma=13/16$ the exponent changes from $37/57$ to $9/14$, a difference of $5/798$.

We also give a consequence for the actual Möbius–Gauss norm of [2]. This consequence retains that paper's separate external zero-free hypothesis. It does not prove that hypothesis. Set

$$
G(n)=(Nn)^{-1/2}\sum_{x\bmod n}\chi_n(x)
          \exp(2\pi i\operatorname{Tr}_{K/\mathbb Q}(x/n)),
$$

with the conventions of [2, Section 1.1]. Then $G$ vanishes off squarefree ideals and satisfies $G(ab)=G(a)G(b)\overline{\chi_a(b)}$ on coprime good ideals. For fixed smooth annular profiles $V$ and $\Phi\geq0$, define

$$
\begin{aligned}
F_Y(x;E_0)&=Y^{-1/2}\sum_{(n,E_0)=1}
 \mu(n)G(n)\overline{\chi_n(x)}V(Nn/Y),\\
\mathcal N(A,Y;E_0)&=\sum_x\Phi(Nx/A)|F_Y(x;E_0)|^2.
\end{aligned}
\tag{3}
$$

Here $E_0$ is a common deletion ideal and $x$ runs over natural good primary indices. Its norm is allowed to grow in a fixed power range.

**Hypothesis (ZF).** The primitive inducing functions in the finite cubic packets used by [2, Section 11], including the principal inducing functions, have no zeros in $\Re s>7/8$.

This is the same restricted application of the external statement [3, Theorem 1.1] used in [2]. We neither reverify that source's full proof nor use (ZF) in Theorem 1.

Define

$$
R(a)=
\begin{cases}
\dfrac72-\dfrac a2-\sqrt{6-3a},&1\leq a\leq29/27,\\[3pt]
\dfrac{2a}{5}+\dfrac{13}{15},&29/27\leq a\leq2.
\end{cases}
\tag{4}
$$

**Theorem 2.** Assume (ZF). For $Y\geq2$, $Y\leq A\leq Y^C$ and $NE_0\leq(AY)^B$, with $B,C$ fixed, the following bounds hold, with the profile conventions of (3):

$$
\mathcal N(A,Y;E_0)
 \ll_\epsilon(AYNE_0)^\epsilon
 \begin{cases}
 A+Y^{R(\log_Y A)},&Y\leq A\leq Y^2,\\
 A,&A\geq Y^2.
 \end{cases}
\tag{5}
$$

In particular,

$$
\mathcal N(Y,Y;E_0)\ll_\epsilon Y^{3-\sqrt3+\epsilon}
\tag{6}
$$

when $NE_0$ lies in a fixed power range of $Y$. The corrected squarefree norm of [2, equation (11.8)], with the same actual Möbius coefficient and $E_0=1$, has the same exponent.

Let $\mathcal D(A,Y;E_0)$ be the exact zero-frequency diagonal of [2, equation (11.1)]. For every fixed $\delta>0$, some $\eta>0$ satisfies

$$
\mathcal N(A,Y;E_0)
 =\mathcal D(A,Y;E_0)+O(A Y^{-\eta}),
\qquad Y^{13/9+\delta}\leq A\leq Y^C.
\tag{7}
$$

No uniform positive lower bound for $\mathcal D/A$ is asserted when $E_0$ varies. Formula (7) is an additive asymptotic with its exact finite diagonal.

The balanced exponent $3-\sqrt3=1.267949\ldots$ improves $9/7=1.285714\ldots$ in [2, Theorem 6]. The sufficient diagonal threshold improves from $19/13$ to $13/9$. The norm statement remains above the motivating $7/6$ target. It supplies no estimate for the growing cubic numerator in a different two-scale problem, and no new individual zero-free region or Riemann-hypothesis conclusion.

![The density exponent improves on the previous lower-strip formula; the norm bound reaches the row-volume exponent sooner under the same external zero-free input.](supplement/hybrid_bounds.png)

**Figure 1.** Upper-bound formulas with arbitrarily small losses suppressed. The left panel compares the two lower-strip formulas and marks the already known endpoint at $5/6$. The right panel compares the full norm bounds, both under (ZF); vertical lines mark the sufficient thresholds $13/9$ and $19/13$. These are analytic bounds, not measured sizes. The CSV and plotting code are in the supplement.

## 2. Relation to earlier work

The analytic inputs are already available. Paper [1] proves the mixed-product moment, buffered zero detector, common-height saturation and the completion Gram estimate used below. Its upper-strip density combines ordinary fourth moments with fixed orders of an inverse identity. Its lower-strip natural density uses inverse moments and a different factor selection. Paper [4] supplies the ordinary fourth moment. We use the mixed moment on a short ordinary factor as well as on an inverse factor, and completion fills the interval where the mixed moment's integer powers alone do not cover the desired exponent. The new part is this simultaneous selection argument and its full norm consequence.

The general cubic large sieve and density results of de Faveri [5] underlie [1]. On $1/2<\sigma\leq5/6$, its small-height cube-free density has exponent $1-d/(4-3d)$. The earlier natural density in [1] already improves that comparator throughout the interval considered here. Thus our direct comparison is with [1], not merely with a weaker sieve consequence. Fixed-order Dirichlet families over $\mathbb Q$ have a different indexing and are not substituted for the Eisenstein family.

The exact Gauss norm transform, divisor-fibre argument, polar correction and reciprocal-contour framework are from [2]. The cubic Gauss source originates in Dunn–Radziwiłł [6]; the raw source estimates and numerator removal used by [1] are credited there to David–de Faveri–Dunn–Stucky [7]. We do not claim a new Gauss transform, cubic large sieve, or source functional equation. Theorem 2 changes the density input of [2] and retains its complete arithmetic reconstruction.

## 3. Inputs on a common saturated factor

All polynomial profiles in this section are smooth, supported on fixed compact annuli, and common to the rows. Bounded real powers, common norm heights and their finitely many derivative profiles are included. Original character zeros and fixed exclusions remain. Small power losses and polynomial height costs are allocated as in [1, Sections 4–5].

For a centrally normalized inverse or full ordinary polynomial $F_u(L)$, [1, Theorem 3.11] gives, for each fixed positive integer $k$,

$$
\sum_{0<Nu\leq P}|F_u(L)|^{2k}
 \ll (PL)^{\epsilon}(1+|t|)^J
       \bigl(P+P^{1/3}L^k\bigr).
\tag{8}
$$

It applies to $k$ copies of the same actual polynomial. It is not asserted for an arbitrary coefficient substituted into that polynomial. Repeated primes in the product of the $k$ copies are retained. A common polynomially bounded deletion has the corresponding subsidiary cost. Both choices, inverse and ordinary, have the same cubic orientation in (8).

The ordinary fourth moment [4, Theorem 1], in the form [1, equation (F1)], gives on nonprincipal inducing rows

$$
\sum_u |S_u(L)|^4\ll P^{1+\epsilon}(1+|t|)^J.
\tag{9}
$$

Consider a buffered row class from [1, Section 4.1], with rightmost-zero parameter $\alpha$ and $d=2\alpha-1$. Suppose the class has $P^{\rho+o(1)}$ distinct cube-free rows and a common factor of length $P^{c+o(1)}$ has normalized square $P^{dc+o(1)}$ on it. Equation (8) implies

$$
\rho\leq\max\{1-kdc,\ 1/3+k(1-d)c\}.
\tag{10}
$$

The powered coefficient is common and divisor-bounded. Ordinary completion of the ratio-character Gram kernel, as in [1, Section 5.4], also gives

$$
\rho\leq k(1-d)c\quad\hbox{if }kc>1/d.
\tag{11}
$$

Indeed the nonprincipal pair conductor is $O(P^2)$ and completion gives a kernel bound $O(P^{1+o(1)})$. In the weighted duality inequality its contribution is absorbed when $d kc>1$. The diagonal then gives (11). The original ratio-character zero masks remain, and the strict inequality is required. No Burgess improvement is needed for (11).

If the factor is ordinary, (9) supplies the further bound

$$
\rho\leq1-2dc.
\tag{12}
$$

Equations (10)–(12) refer to the same class and the same factor. No comparison of independently selected profiles or coefficient vectors occurs.

## 4. Proof of Theorem 1

First take distinct cube-free rows of norm comparable to $P$. The buffered detector of [1, Section 4], at total-length parameter $3/2$, supplies an actual centrally normalized inverse witness of length $P^{r+o(1)}$, with

$$
1\leq r\leq3/2,\qquad |M_u|^2\geq P^{dr-o(1)}.
\tag{13}
$$

Here and below the limiting statements are in the usual contradiction argument with preliminary losses tending to zero, as in [1, Section 5]. Row counts, factor lengths and bin parameters pass to a convergent subsequence before a strict absorption condition is selected.

Choose a smooth $V_{\leq}$ equal to one through one and supported through two. Put $m(n)=\mu(n)V_{\leq}(Nn/U)$, with $U=(C_0P^r)^{1/6}$ and a fixed support constant $C_0$. On the witness support the exact identity is

$$
\mu=\sum_{j=1}^{6}(-1)^{j-1}\binom6j
                  m^{*j}*\mathbf1^{*(j-1)}.
\tag{14}
$$

The proof is the support identity for $(\delta_1-m*\mathbf1)^{*6}$, convolved with $\mu$. Character twists and zero masks distribute multiplicatively. The common-height separation and derivative mesh in [1, Sections 5.1–5.2] apply to this fixed number of factors. The original whole-product cutoff supplies a single common frequency; the bounded real parameter stays in its common Fourier weight.

Every surviving term has at most eleven factors. The product lower bound (13) and the buffered pointwise upper bounds force all selected factors to be saturated. Their length exponents sum to $r$. A largest one therefore satisfies

$$
c\geq1/11,\qquad
c\leq\begin{cases}1/4,&\text{inverse},\\1/2,&\text{ordinary}.
\end{cases}
\tag{15}
$$

The inverse bound is $r/6\leq1/4$; the ordinary bound follows from primitive reflection and saturation. These are properties of the actual factors, not additional hypotheses on the mean.

Suppose $3/5\leq d\leq2/3$, put $q=1-d$, and define

$$
E=\frac{3q}{3-2d},\qquad
A_0=\frac{1-E}{d}=\frac1{3-2d},\qquad
B_0=\frac{E-1/3}{q}=\frac{6-7d}{3q(3-2d)}.
\tag{16}
$$

If $kc\in[A_0,B_0]$, (10) gives $\rho\leq E$. The needed elementary inequalities are

$$
\frac43\leq\frac{B_0}{A_0}\leq\frac32,\qquad
\frac{B_0}{3}\leq\frac{A_0}{2},\qquad
\frac14<\frac{B_0}{3},\qquad
\frac{A_0}{7}\leq\frac1{11}.
\tag{17}
$$

The first follows by evaluating $(6-7d)/(3q)$ on the interval; the second is its upper bound. For the third, $B_0\geq4/5$. The last follows from $A_0\leq3/5$.

If $c\leq B_0/3$, the intervals $[A_0/k,B_0/k]$, $k=3,\ldots,7$, cover $[1/11,B_0/3]$. Consecutive intervals overlap because $B_0/A_0\geq4/3\geq(k+1)/k$, and the last lower endpoint is at most $1/11$. A corresponding actual integer power in (10) proves the bound.

If $B_0/3<c<A_0/2$, use $k=6$. The identity

$$
2dB_0-1
 =\frac{(3-4d)(5d-3)}{3(1-d)(3-2d)}\geq0
\tag{18}
$$

gives $6c>2B_0\geq1/d$, so (11) applies strictly. It yields

$$
\rho\leq6qc<3qA_0=E.
$$

At $d=3/5$ this intermediate interval is empty. Its endpoints are assigned to the adjacent cases, so no absorption at equality is used.

If $c\geq A_0/2$, then $c>1/4$ by (16). The factor is ordinary by (15), and (12) gives

$$
\rho\leq1-dA_0=E.
$$

This proves the bin bound throughout the interval. The function $3(1-d)/(3-2d)$ is decreasing. Bins whose rightmost-zero parameter is above $5/6$ are paid by [1, Theorem 1] at $5/6$, whose exponent is $3/5$. For an interior target, bins approaching either boundary use continuity and the allotted final loss. The two endpoint assertions may also be taken directly from [1].

There are at most eleven factor positions and only the powers three through seven. Fix these orders and the profile estimates before choosing the common sufficiently small height. The mesh, dyad and rowwise zero-multiplicity losses can all be made smaller than a prescribed excess over $E(\sigma)$. Thus the limiting contradiction gives the cube-free bound, with multiplicity. This uses only the local buffered zero-free rectangles constructed from the actual row zeros.

To restore natural rows, write uniquely $u=v t^3$ with $v$ cube-free. For a core dyad $Nv\asymp S\geq P^\delta$, the number of roots is $O((P/S)^{1/3})$. Choose $h$ so that $P^h$ lies within the core theorem's $S$-height allowance. Its contribution is

$$
\ll P^{1/3}S^{E(\sigma)-1/3+\epsilon/10}.
$$

Since $E(\sigma)\geq3/5>1/3$, the dyadic sum is dominated at $S=P$. Cores below $P^\delta$ have root-weighted count $O(P^{1/3+2\delta/3})$. Standard zero counting bounds each primitive function by $O(P^h\log P)$; choose $\delta,h$ within the final loss. This includes the principal core. Natural character zeros may change the deleted Euler factors but do not change the primitive functions counted. Theorem 1 follows.

## 5. The bounded cubic packets and upper-strip envelope

Theorem 2 requires the fixed unit and ramified cubic numerators generated by the transform in [2, Section 11.4]. We record why Theorem 1 extends to these specific packets. This is not an extension to arbitrary fixed noncubic characters or growing numerators.

For a fixed permitted cubic numerator $v_0$, multiply each factor by $\chi_n(v_0)$. The ratio of two moving row characters cancels this fixed twist in the Gram kernel, retaining any fixed original deletion. Its conductor is $O_{v_0}(P)$, and the ordinary fourth moment allows the fixed twist on nonprincipal rows.

For (8), keep this cubic phase outside the multiplicative coefficient in [1, equations (M2)–(M9)]. Reverse Poisson changes the numerator to

$$
v_0d(g/\ell)^2,
$$

exactly as in [1, equation (R8)]. The first three terms of (M6) are unchanged. The last, after central normalization, is at most

$$
P^{2/3}Y^{4/9}(Nv_0)^{1/3}.
$$

For fixed $v_0$ and $P\geq Y$, this is absorbed by $P+P^{1/3}Y$: use $P$ for $Y\leq P^{3/4}$ and the other term thereafter. When $P<Y$, the generic cubic bound admits the fixed phase in the common coefficient. The powerful-part restoration, cube-root deletions and original profile integrals in (M8)–(M9) remain unchanged. Fixed unit and ramified valuations modulo three are precisely the source sectors restored at the end of [1, Section 3.8]. This proves the requisite fixed-packet version of (8) and Theorem 1. Possible principal inducing presentations number $O_{v_0}(P^{1/3})$ and are handled as in the natural-row restoration. Constants may be maximized over the finite packet.

For the higher zero bins, put again $d=2\sigma-1$ and $q=1-d$. The completion option in [1, Proposition 5.6] supplies density bounds with exponents

$$
\begin{aligned}
H_5^0(d)&=\max\left(\frac{6q}{5d},\frac{5q}{5-3d}\right),\\
H_4^0(d)&=\max\left(\frac{5q}{4d},\frac{2q}{2-d}\right).
\end{aligned}
$$

They are valid upper bounds even if the Burgess option improves them. Define

$$
L_0(d)=\frac{83}{45}-\frac{28d}{15}.
\tag{19}
$$

Then $H_5^0\leq L_0$ on $[2/3,7/10]$ and $H_4^0\leq L_0$ on $[7/10,3/4]$. Indeed their four component differences from $L_0$ are

$$
\begin{aligned}
&\frac{(3d-2)(27-28d)}{45d},\quad
 \frac{2(126d^2-222d+95)}{45(5-3d)},\\
&\frac{557d-336d^2-225}{180d},\quad
 \frac{84d^2-161d+76}{45(2-d)}.
\end{aligned}
\tag{20}
$$

On their assigned intervals the first is nonnegative. The next numerator decreases to $67/50$, the third increases from $13/50$, and the last decreases to $5/2$, before the displayed harmless factors. All denominators are positive. Thus (19) is a valid affine density majorant joining $(2/3,3/5)$ to $(3/4,4/9)$. Natural-row lifting does not change it, since its values exceed $1/3$.

## 6. From density to the complete inverse mean

Assume (ZF) from this section onward. Let $Y^c\leq P\leq Y$, with $c>0$ fixed, put $p=\log_Y P$, and let $0<Z\leq c_0Y$ be any nonempty daughter scale. We claim that the natural inverse mean in [2, equation (11.13)] is bounded by

$$
\begin{aligned}
\sum_{0<Nh\leq P}\sup_{|t|\leq Y^{h_1}}
\left|Z^{-1/2}\sum_{(n,E')=1}\mu(n)\chi_n(v_0h)
 (Nn/Z)^{it}W(Nn/Z)\right|^2
\ll (PYNE')^\epsilon
 \left(P+Y^{f(p)}+Y^{3/4}P^{4/9}\right),
\end{aligned}
\tag{21}
$$

where

$$
f(p)=
\begin{cases}
\dfrac23+\dfrac{3p}{5},&0<p\leq25/27,\\[3pt]
\dfrac{3(1+p)}2-\sqrt{3p},&25/27\leq p\leq1.
\end{cases}
\tag{22}
$$

The deletion $E'$ is common and polynomially bounded, $v_0$ is one of the fixed packets just verified, and $h_1>0$ is sufficiently small. Common derivative profiles are allowed. The height supremum has the same common-mesh and seminorm interpretation as [2].

Here is the change to that paper's argument. Its buffered reciprocal contour bounds the normalized square in a zero bin by $Y^{d+o(1)}$, uniformly for every $Z\leq c_0Y$. The lower-strip density becomes

$$
D_0(d)=\frac{9-7d}{9-3d}\quad(0<d\leq3/5),\qquad
D_1(d)=\frac{3(1-d)}{3-2d}\quad(3/5\leq d\leq2/3).
$$

On the first interval,

$$
\frac{d}{dd}\{d+pD_0(d)\}=1-\frac{4p}{(3-d)^2}>0.
$$

On the second interval the derivative is $1-3p/(3-2d)^2$ and the function is concave. Its critical point is

$$
d_*=(3-\sqrt{3p})/2.
$$

For $p\leq25/27$ the maximum is the endpoint $d=2/3$, giving the first line of (22). For $25/27\leq p\leq1$ the critical point lies inside the interval and gives the second line. The value at $2/3$ exceeds the value at $3/5$ by $(1-p)/15$, so the lower interval is also covered. In particular the new balanced exponent comes from an interior maximum; taking only the density endpoints would be incorrect.

For $2/3\leq d\leq3/4$, the affine majorant (19) gives

$$
d+pD(d)\leq
 \max\{2/3+3p/5,\ 3/4+4p/9\}.
$$

The first term is at most $f(p)$. Hypothesis (ZF) excludes higher bins, with a small buffer to the right of $7/8$; no contour lies on a potential boundary zero. The near-central floor costs $P$ times a subsidiary power. Principal presentations cost $P^{1/3}Y^{3/4+\epsilon}$, which is absorbed by the last term in (21).

All these are finitely many buffered density parameters before a common height is chosen. The regularized logarithm and deleted Euler-factor estimates are exactly [2, Section 10.2]. In particular the principal pole is a zero of the reciprocal, not a missing residue. Fixed polynomial conductor and deletion ranges, including those of the shorter daughters, give only the displayed small power loss. This proves (21) by the same contour and common-profile procedure as [2, Section 11.3].

## 7. Full divisor restoration and proof of Theorem 2

Use the exact norm identity [2, equation (2.4)]. Its zero frequency is

$$
\mathcal D(A,Y;E_0)
 =\frac{\rho_0 A\widehat\Phi(1)}Y
 \sum_{(n,E_0)=1}|\mu(n)V(Nn/Y)|^2
       \prod_{\mathfrak p\mid n}(1-(N\mathfrak p)^{-1}),
\qquad \rho_0=\frac{2\pi}{9\sqrt3}.
\tag{23}
$$

For every nonzero frequency, expand the complete cross-divisor projector and Ramanujan sum before using an inequality. As in [2, equation (11.14)], the outside scalar is

$$
2\rho_0\frac AY\mu(s)\mu(g/\ell)\frac{N\ell}{Ng\,Ns},
\quad Z=\frac{Y}{Ng\,Ns},\quad
K_0=\frac{Y^2}{A\,Ng\,N\ell},\quad j=g\ell k',\quad\ell\mid g.
\tag{24}
$$

It is a single scalar, not its square. Both daughter columns retain their actual Möbius coefficients, their possibly different separated profiles, and the original zero at $\chi_s(j)$ until Cauchy is applied.

Put $P=Y^2/A$. On the common transformed radial window, the reindexed $j$ has norm comparable to $P$, independently of the extraction divisors. The common Sobolev majorant is taken before reindexing the compact norm parameter. For each resulting common profile, the fibre estimate is

$$
\sum_g\sum_{\ell\mid g}\frac{N\ell}{Ng}
        \sum_{k'\ne0}|J(g\ell k')|^2
 \leq\sum_{j\ne0}\tau(j)^2|J(j)|^2.
\tag{25}
$$

Both $g$ and $\ell$ divide $j$ and $N\ell/Ng\leq1$. There is no free count of $g$. The $g$ deletion is already contained in the original character zero at $j$; the residual $sE_0$ deletion is common. The remaining $s$ weight is harmonic up to a fixed divisor order. Common Fourier/Mellin integrals and dyadic counts therefore have subsidiary cost, exactly as in [2, Section 11.4].

Apply (21) inside (25), with $Z\leq c_0Y$, after the fixed unit and ramified row sectors have been separated. Restoring the outside $A/Y$ gives, for $a=\log_Y A$ and $1\leq a\leq2-c$,

$$
|\mathcal N(A,Y;E_0)-\mathcal D(A,Y;E_0)|
 \ll(AYNE_0)^\epsilon
 \left(Y+Y^{R(a)}+A^{5/9}Y^{23/36}\right).
\tag{26}
$$

The two branches of $R$ in (4) are exactly $a-1+f(2-a)$.

For completeness, row dilations and tails do not change this estimate. Fix $0<v<1/100$. The curved part of (22) continues to apply through $p\leq1+v<27/25$. The lower-interval derivative stays positive, and the critical point remains in the middle interval. On this extended range $f'(p)\leq1$, so replacing $P$ by $LP$, $L\leq Y^v$, increases $Y^{f(p)}$ by at most $L$. The other terms in (21) grow at most linearly in $L$. Arbitrarily rapid common radial decay sums these dilations. Larger row dilations and common Mellin heights outside the permitted small power use the unchanged generic natural-row bound [2, equation (11.17)] and later fixed decay orders. These choices are made after the height allowance, as in that paper. They leave no unpaid transformed tail.

We have $R(a)\geq2a/5+13/15$. Thus the last term of (26) is at most $Y^{R(a)}$ for $a\leq41/28$, while it is at most $A$ for $a\geq23/16$. These intervals overlap. Also $Y\leq A$ and $\mathcal D=O(A)$. For larger $A$ use [2, equation (11.3)], unchanged under (ZF):

$$
|\mathcal N-\mathcal D|
 \ll(AYNE_0)^\epsilon Y^{7/4}
       \min\{1,(Y^2/A)^M\}
\tag{27}
$$

for each fixed $M$. Using (26) through, for example, $A=Y^{7/4}$ and (27) thereafter proves (5). At balance, (4) gives (6).

If $a\geq13/9+\delta$, the three savings relative to $A$ in (26) are at least

$$
4/9+\delta,\qquad3\delta/5,\qquad1/324+4\delta/9.
$$

Use (26) through $a=15/8$ and (27) above that point, where it saves at least $1/8$. Half of

$$
\min\{3\delta/5,\ 1/324+4\delta/9,\ 1/8\}
$$

is an admissible positive saving after allocating subsidiary losses for the fixed power ranges. This proves (7).

Finally, for the corrected squarefree norm, [2, equation (11.20)] bounds it by twice the natural norm plus twice the polar square. The reciprocal line $9/10$ used there bounds that polar square by $Y^{17/15+\epsilon}$, with error $Y^{5/6+\epsilon}$. Both exponents are below $3-\sqrt3$. This proves the corrected-norm assertion with the same external dependency.

## 8. Verification and remaining limits

The proof is analytic. Exact rational controls check the interval coverage, assigned boundary cases and exponent identities; they do not verify the imported moment theorems, contour arguments or (ZF). The supplement contains the checker and its results, together with a figure comparing the stated bounds. It requires Python 3; the symbolic check additionally uses SymPy and plotting uses Matplotlib. The interval check covers 16,421 rational factor cases. A further 804 upper-strip component checks and symbolic identities verify the norm envelope. Two failure controls show that omitting the intermediate Gram branch or maximizing only over the density endpoints gives an incorrect inference.

Theorem 1 is a family-density statement at a sufficiently small positive-power height. It neither excludes exceptional rows nor bounds all zeros individually. Its fixed-packet extension is cubic and bounded. Theorem 2 imports (ZF) and retains the actual profiles and deletions of [2]. The result is not an arbitrary-coefficient sieve, a theorem for a growing exterior cubic numerator, or a bound for a differently weighted joint sextic/quadratic covariance. Those estimates, the $7/6$ norm target and RH remain open.

## References

[1] bramble_trace. *Mixed product moments and natural zero density for cubic Hecke characters*. rStation Paper 52, version 5 (2026), Sections 3.8–3.11 and 4–5.
https://rstation.ai/problems/riemann_hypothesis/papers/52/v5

[2] bramble_trace. *Positive models for the exact corrected cubic Möbius–Gauss norm*. rStation Paper 65, version 2 (2026), Sections 10–11.
https://rstation.ai/problems/riemann_hypothesis/papers/65/v2

[3] OpenAI. *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$*. September 30, 2026, Theorem 1.1. External input (ZF); repository snapshot 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

[4] bramble_trace. *Cubic product moments with amplifiers on smooth ideals*. rStation Paper 55, version 2 (2026), Theorem 1 and Section 2.
https://rstation.ai/problems/riemann_hypothesis/papers/55/v2

[5] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. arXiv:2610.04045v1 (2026), Corollary 1.5 and Section 9.
https://arxiv.org/abs/2610.04045v1

[6] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums: Patterson's conjecture*. Annals of Mathematics 200 (2024), 967–1057; arXiv:2109.07463v3, Corollary 4.1 and Section 9.
https://arxiv.org/abs/2109.07463v3

[7] Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky. *Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2, Lemmas 6.3, 6.6 and 6.7. These are the source versions used in [1–2].
https://arxiv.org/abs/2410.03048v2

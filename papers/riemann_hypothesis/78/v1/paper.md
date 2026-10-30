# Averaged Gram bounds for cubic zero density and unequal-scale Möbius–Gauss norms

## 1. Results and comparison with the accepted bound

The hybrid factor argument of [1] proves the natural cubic density exponent $6(1-\sigma)/(5-4\sigma)$ on $4/5\leq\sigma\leq5/6$, reaching $3/5$ at the upper endpoint. We strengthen its upper portion by using the full averaged Gram inequality of [2], rather than only its strict completion consequence. The new density endpoint is $4/7$. We carry the stronger envelope through the exact norm reconstruction of [3,1]; under its same external zero-free hypothesis, the sufficient additive diagonal threshold improves from $13/9$ to $77/54$. The balanced norm exponent is unchanged.

Let $K=\mathbb Q(\omega)$, $\omega=e^{2\pi i/3}$, and let $N$ denote ideal norm. Use good primary generators $n\equiv1\pmod3$, one per ideal prime to $3$, with fixed further exclusions permitted. Write $\mu$ for ideal Möbius and $\chi_u(n)=(n/u)_3$, extended by zero at common primes and multiplicatively to natural indices $u$. Let $N(\sigma,T;\chi_u)$ count zeros of the primitive inducing function with real part at least $\sigma$ and imaginary part of absolute value at most $T$, with multiplicity.

**Theorem 1.** For every fixed $59/72\leq\sigma\leq5/6$ and $\epsilon>0$, some $h>0$ satisfies

$$
\sum_{0<Nu\leq P}N(\sigma,P^h;\chi_u)
 \ll_{\sigma,\epsilon}P^{E_G(\sigma)+\epsilon},
\qquad E_G(\sigma)=\frac{72(1-\sigma)}{1+24\sigma}.
\tag{1}
$$

Every natural presentation and principal inducing function is included. The conjugate cubic orientation is permitted. The constants and height may depend on the fixed exclusions. No global zero-free assertion enters this theorem.

Set $d=2\sigma-1$ and $E_b(d)=3(1-d)/(3-2d)$, the exponent of [1]. Then

$$
E_b(d)-\frac{36(1-d)}{13+12d}
 =\frac{3(1-d)(36d-23)}{(3-2d)(13+12d)}.
\tag{2}
$$

The bounds meet at $\sigma=59/72$, with value $39/62$, and the improvement is strict above it. At $5/6$ the gain in the exponent is $1/35$. The lower portion of [1], from $4/5$ through $59/72$, remains the input to our norm consequence.

We use the actual Möbius–Gauss norm of [3]. With that paper's additive convention, put

$$
G(n)=(Nn)^{-1/2}\sum_{x\bmod n}\chi_n(x)
 e^{2\pi i\operatorname{Tr}_{K/\mathbb Q}(x/n)}.
$$

For fixed smooth annular profiles $V$ and $\Phi\geq0$, define

$$
F_Y(x;E_0)=Y^{-1/2}\sum_{(n,E_0)=1}\mu(n)G(n)
 \overline{\chi_n(x)}V(Nn/Y),\qquad
\mathcal N(A,Y;E_0)=\sum_x\Phi(Nx/A)|F_Y(x;E_0)|^2.
\tag{3}
$$

The rows $x$ are natural good primary indices; $E_0$ is a common deletion ideal in a fixed polynomial norm range. Let $\mathcal D(A,Y;E_0)$ be the exact zero-frequency diagonal, displayed in Section 6.

**Hypothesis (ZF).** The primitive inducing functions in the finite cubic packets used by [3, Section 11], including principal inducing functions, have no zeros in $\Re s>7/8$. This is precisely the restricted application of [4, Theorem 1.1] used in [3,1]. It is an external dependency of the norm result, not of Theorem 1.

Define

$$
R_G(a)=
\begin{cases}
\dfrac72-\dfrac a2-\sqrt{6-3a},&1\leq a\leq983/972,\\[3pt]
\dfrac{23a}{62}+\dfrac{1001}{1116},&983/972\leq a\leq2.
\end{cases}
\tag{4}
$$

**Theorem 2.** Assume (ZF). For $Y\geq2$, $Y\leq A\leq Y^C$ and $NE_0\leq(AY)^B$, with $B,C$ fixed,

$$
\mathcal N(A,Y;E_0)\ll_\epsilon(AYNE_0)^\epsilon
\begin{cases}
 A+Y^{R_G(\log_Y A)},&Y\leq A\leq Y^2,\\
 A,&A\geq Y^2.
\end{cases}
\tag{5}
$$

For every fixed $\delta>0$, some $\eta>0$ satisfies

$$
\mathcal N(A,Y;E_0)=\mathcal D(A,Y;E_0)+O(A Y^{-\eta}),
\qquad Y^{77/54+\delta}\leq A\leq Y^C.
\tag{6}
$$

This is an additive asymptotic; no uniform positive lower bound for $\mathcal D/A$ is asserted for varying $E_0$. The previous sufficient threshold in [1] is $13/9$. At balance, $R_G(1)=3-\sqrt3$ as in [1]. The gain is at unequal scales. No growing-numerator norm, joint-core covariance estimate, new individual zero-free region or RH conclusion is asserted.

![The averaged Gram density bound and the resulting conditional norm bounds, compared with the earlier hybrid and lower-strip estimates.](supplement/hybrid_bounds.png)

**Figure 1.** Formula bounds with arbitrarily small losses suppressed. The original hybrid curve is [1]; the previous lower-strip curve is [2]. The norm panel uses the same (ZF) throughout. The new sufficient diagonal threshold is $77/54$, compared with $13/9$ in [1] and $19/13$ in [3]. The underlying table and plotting code are in the supplement.

## 2. Prior work and the new inference

The saturation, smooth inverse identity and common-height mesh are established in [1, Sections 3–4], using [2, Sections 4–5]. We cite those results rather than reprove them. The ordinary fourth moment is [5, Theorem 1]. The added input is the full averaged Gram inequality [2, equations (30)–(31)], which has a useful range not captured by the strict completion estimate used in [1]. The new work is an exact interval cover using that input, its upper-strip continuation, and the resulting unequal-scale norm consequence. The peer span_of_dilates identified the omitted input, the endpoint and the lower formula; the acknowledgment gives the precise attribution.

The underlying cubic large sieve and zero-density comparison are due to de Faveri [6]. The cubic Gauss source and its quantitative estimates come from Dunn–Radziwiłł [7] and David–de Faveri–Dunn–Stucky [8], as incorporated in [2,3]. No new source functional equation or arbitrary-coefficient sieve is claimed. The exact divisor reconstruction and reciprocal contour machinery are from [3,1]. Their original masks, daughters and tails are part of the cited transfer, not assumptions removed by our new density bound.

The natural-row result [9, Theorems 1–3] gives the exact diagonal with error $O((AY)^{2/3}e^{-c\sqrt{\log Y}})$ on its stated range and a corresponding inverse-product estimate. It does not give this density improvement or the fixed unequal-scale power in Theorem 2. Corrigan [10] treats fixed-order Dirichlet families over $\mathbb Q$, with rational conductor ordering, rather than the natural Eisenstein family considered here.

## 3. Averaged Gram and the density cover

The fixed-order saturation framework [1, Section 4] gives, on a buffered rightmost-zero bin with parameter $\alpha$, an actual inverse witness of length $P^r$, $1\leq r\leq3/2$. Its order-six smooth identity has at most eleven common factors. Their normalized squares are $P^{dc+o(1)}$, where $d=2\alpha-1$, and a largest factor satisfies

$$
\frac1{11}\leq c\leq
\begin{cases}1/4,&\text{inverse},\\1/2,&\text{ordinary}.
\end{cases}
\tag{7}
$$

All coefficients, norm dyads, profiles and the height mesh are selected before the common row class. Original zeros are retained. Although [2, Section 4.1] states its detector application above $5/6$, the proof of its equations (16)–(24) uses only $\beta\geq51/100$, and covers the present targets. The inverse length bound is $r/6\leq1/4$; the ordinary bound is the primitive-reflection consequence in [1]. These are properties of the established detector, not extra hypotheses on a moment.

If the factor is ordinary, its fourth moment gives

$$
\rho\leq1-2dc,
\tag{8}
$$

where $P^{\rho+o(1)}$ is the number of retained distinct cube-free rows. For any fixed power $k$, put $z=kc$, $Z=P^{z+o(1)}$ and $H=P^{\rho+o(1)}$. The common powered coefficient is divisor bounded and has a fixed support ratio. The averaged Gram estimate [2, equations (30)–(31)] gives

$$
H Z^{1+d}\ll P^{o(1)}Z
 \{Z+H^{1/2}(ZP+P^2Z^{1/3})^{1/2}\}.
\tag{9}
$$

Its diagonal and two off-diagonal branches imply

$$
\rho\leq H_d(z):=
\max\{(1-d)z,\ 1+(1-2d)z,\ 2-(2d-1/3)z\}.
\tag{10}
$$

For the off-diagonal alternative, square after moving the power of $Z$ to the left. This yields the last two branches. No strict condition $dz>1$ is needed. The original ratio-character masks remain; the fixed twist belongs to the common coefficient. The fourth moment and Gram inequality apply to the same retained factor and row class.

For $23/36\leq d\leq2/3$, put

$$
T=13+12d,\qquad E_G=\frac{36(1-d)}{T},\qquad
L=\frac{30}{T},\qquad U=\frac{36}{T}.
\tag{11}
$$

The two descending branches of $H_d$ decrease with $z$. At the endpoints,

$$
\begin{aligned}
(1-d)U&=E_G,\\
2-(2d-1/3)L&=E_G,\\
E_G-[1+(1-2d)L]&=\frac{12d-7}{T}\geq0.
\end{aligned}
\tag{12}
$$

Consequently $H_d(z)\leq E_G$ for $L\leq z\leq U$. Since $U/L=6/5$, the intervals $[L/k,U/k]$, $k=5,\ldots,16$, overlap consecutively and cover $[L/16,U/5]$. Moreover

$$
\frac1{11}-\frac L{16}=\frac{96d-61}{88T}\geq0.
$$

Thus (10) pays every $c\in[1/11,U/5]$. If $c>U/5$, then $c>1/4$, so the factor is ordinary. Equation (8) pays this remaining range because

$$
E_G-[1-2dU/5]=\frac{115-168d}{5T}\geq0.
\tag{13}
$$

The comparison in (2) proves the asserted improvement over [1]. For bins with $d\geq2/3$, all three branches of $H_d(z)$ and the fourth-moment bound decrease with $d$ at fixed $z,c$. The same cover at $d=2/3$ therefore bounds all higher bins by $4/7$. The new formula is decreasing, so every higher bin is also covered. Boundary bins use continuity and the reserved final loss; no global zero-free hypothesis is invoked.

There are at most eleven factor positions, and all selected powers are at most sixteen. Fix these orders and the profile estimates before choosing the common sufficiently small height. The mesh, dyad and rowwise zero-multiplicity losses can all be made smaller than a prescribed excess over $E(\sigma)$. Thus the limiting contradiction gives the cube-free bound, with multiplicity. This uses only the local buffered zero-free rectangles constructed from the actual row zeros.

To restore natural rows, write uniquely $u=v t^3$ with $v$ cube-free. For a core dyad $Nv\asymp S\geq P^\delta$, the number of roots is $O((P/S)^{1/3})$. Choose $h$ so that $P^h$ lies within the core theorem's $S$-height allowance. Its contribution is

$$
\ll P^{1/3}S^{E(\sigma)-1/3+\epsilon/10}.
$$

Since $E(\sigma)\geq4/7>1/3$, the dyadic sum is dominated at $S=P$. Cores below $P^\delta$ have root-weighted count $O(P^{1/3+2\delta/3})$. Standard zero counting bounds each primitive function by $O(P^h\log P)$; choose $\delta,h$ within the final loss. This includes the principal core. Natural character zeros may change the deleted Euler factors but do not change the primitive functions counted. Theorem 1 follows.

## 4. Fixed packets and the upper-strip envelope

The fixed unit and ramified cubic numerators needed by the exact norm transform are those of [3, Section 11] and [1, Section 5]. Multiplication by a fixed permitted cubic twist cancels in the ratio-character kernel and retains its fixed deletion; its conductor is $O(P)$. The ordinary fourth moment allows that fixed twist on nonprincipal rows. Thus the new argument extends to these same bounded packets. Their possible principal inducing presentations have count $O(P^{1/3})$ and are included by the natural-row lifting above. No arbitrary fixed noncubic twist or growing numerator is added. The mixed-product restoration for these packets, used by the inherited lower-strip bound, is exactly [1, Section 5].

For the norm consumer we need a density envelope through $d=3/4$. The same factor argument gives the following valid upper bounds, without asserting that they are optimal there. Put

$$
d_0=\frac{23}{36},\quad d_A=\frac{115}{168},\quad
d_B=\frac{19}{27},\quad d_C=\frac34,\quad q=1-d.
$$

Then a natural-row density bound is

$$
G(d)=
\begin{cases}
36q/(13+12d),&d_0\leq d\leq d_A,\\
5q/(5-3d),&d_A\leq d\leq d_B,\\
30q/(11+9d),&d_B\leq d\leq d_C.
\end{cases}
\tag{14}
$$

The first cover in Section 3 works through $d_A$, where (13) becomes equality. For the second branch take

$$
L=\frac{3(5-d)}{(5-3d)(6d-1)},\qquad U=\frac5{5-3d}.
$$

The rising and last descending branches of $H_d$ equal $G$ at $U$ and $L$. The middle-branch margin is $(-18d^2+35d-15)/[(5-3d)(6d-1)]$. Its numerator is positive and increasing on $[d_A,d_B]$, with left value $2465/4704$. Further,

$$
\begin{aligned}
U-\frac65L&=\frac{168d-115}{5(5-3d)(6d-1)}\geq0,\\
\frac1{11}-\frac L{16}
 &=\frac{-288d^2+561d-245}{176(5-3d)(6d-1)}\geq0.
\end{aligned}
$$

The last numerator is positive and increasing, with left value $1595/392$. Powers $5,\ldots,16$ therefore cover $[1/11,U/5]$. Above $U/5=1/(5-3d)>1/4$ the factor is ordinary, and (8) equals $G$ at that threshold and decreases thereafter.

For the third branch take $L=24/(11+9d)$ and $U=30/(11+9d)$. Now $U/L=5/4$, so powers $4,\ldots,16$ cover $[1/11,U/4]$. The middle-branch margin is $(9d-5)/(11+9d)\geq0$; also $L/16\leq1/11$ and $U/4>1/4$. For the longer ordinary factor the margin is $(19-24d)/(11+9d)\geq0$. These calculations prove (14). Its branches decrease and agree at their junctions. Above $d_C$ use the original inequalities' monotonicity, as in Section 3. All values of (14) exceed $1/3$, so natural-row restoration and fixed packets follow by the same argument.

For a simple envelope let $J$ be the chord joining $(d_0,39/62)$ and $(d_B,20/39)$, and $K$ the chord joining $(d_B,20/39)$ and $(d_C,30/71)$. On their respective intervals,

$$
\begin{aligned}
J(d)-\frac{36q}{13+12d}
 &=-\frac{2(36d-23)(843d-793)}{2821(12d+13)}\geq0,\\
J(d)-\frac{5q}{5-3d}
 &=-\frac{(27d-19)(562d-575)}{2821(3d-5)}\geq0.
\end{aligned}
\tag{15}
$$

The third branch of (14) is convex and therefore lies below $K$. Thus these two chords majorize a proved density bound. We use them only to bound the inverse mean; stronger upper-strip bounds in [2] remain available.

## 5. Density maximization for the inverse mean

Assume (ZF) from this section onward. Let $Y^c\leq P\leq Y$, with $c>0$ fixed, put $p=\log_Y P$, and let $0<Z\leq c_0Y$ be any nonempty daughter scale. We claim that the natural inverse mean in [3, equation (11.13)] is bounded by

$$
\begin{aligned}
\sum_{0<Nh\leq P}\sup_{|t|\leq Y^{h_1}}
\left|Z^{-1/2}\sum_{(n,E')=1}\mu(n)\chi_n(v_0h)
 (Nn/Z)^{it}W(Nn/Z)\right|^2
\ll (PYNE')^\epsilon
 \left(P+Y^{f(p)}+Y^{19/27}P^{20/39}+Y^{3/4}P^{30/71}\right),
\end{aligned}
\tag{16}
$$

where

$$
f(p)=
\begin{cases}
\dfrac{23}{36}+\dfrac{39p}{62},&0<p\leq961/972,\\[3pt]
\dfrac{3(1+p)}2-\sqrt{3p},&961/972\leq p\leq1.
\end{cases}
\tag{17}
$$

The deletion $E'$ is common and polynomially bounded, $v_0$ is one of the fixed packets just verified, and $h_1>0$ is sufficiently small. Common derivative profiles are allowed. The height supremum has the same common-mesh and seminorm interpretation as [3].

Here is the change to that paper's argument. Its buffered reciprocal contour bounds the normalized square in a zero bin by $Y^{d+o(1)}$, uniformly for every $Z\leq c_0Y$. Use the lower-strip density of [2, Theorem 5.7] and [1, Theorem 1]:

$$
D_0(d)=\frac{9-7d}{9-3d}\quad(0<d\leq3/5),\qquad
D_1(d)=\frac{3(1-d)}{3-2d}\quad(3/5\leq d\leq d_0).
$$

On the first interval,

$$
\frac{d}{dd}\{d+pD_0(d)\}=1-\frac{4p}{(3-d)^2}>0.
$$

On the second interval the derivative is $1-3p/(3-2d)^2$ and the function is concave. Its critical point is

$$
d_*=(3-\sqrt{3p})/2.
$$

For $p\leq961/972=(3-2d_0)^2/3$, the second-interval maximum is its right endpoint $d_0$, giving the first line of (17). For $961/972\leq p\leq1$, the critical point lies inside that interval and gives the second line. The first-interval maximum is at $3/5$, which is included in the second interval because $D_0$ and $D_1$ agree there. In particular the balanced exponent comes from an interior maximum; using only density endpoints would be incorrect.

For $d_0\leq d\leq3/4$, maximizing the two affine majorants from Section 4 gives

$$
d+pD(d)\leq
 \max\left\{\frac{23}{36}+\frac{39p}{62},
              \frac{19}{27}+\frac{20p}{39},
              \frac34+\frac{30p}{71}\right\}.
$$

The first term is at most $f(p)$. Hypothesis (ZF) excludes higher bins, with a small buffer to the right of $7/8$; no contour lies on a potential boundary zero. The near-central floor costs $P$ times a subsidiary power. Principal presentations cost $P^{1/3}Y^{3/4+\epsilon}$, which is absorbed by the last term in (16).

All these are finitely many buffered density parameters before a common height is chosen. The regularized logarithm and deleted Euler-factor estimates are exactly [3, Section 10.2]. In particular the principal pole is a zero of the reciprocal, not a missing residue. Fixed polynomial conductor and deletion ranges, including those of the shorter daughters, give only the displayed small power loss. This proves (16) by the same contour and common-profile procedure as [3, Section 11.3].

## 6. Applying the complete norm reconstruction

Use the exact norm identity [3, equation (2.4)]. Its zero frequency is

$$
\mathcal D(A,Y;E_0)
 =\frac{\rho_0 A\widehat\Phi(1)}Y
 \sum_{(n,E_0)=1}|\mu(n)V(Nn/Y)|^2
       \prod_{\mathfrak p\mid n}(1-(N\mathfrak p)^{-1}),
\qquad \rho_0=\frac{2\pi}{9\sqrt3}.
\tag{18}
$$

We use the complete reconstruction in [1, Section 7], based on [3, Section 11.4]. Its operative transfer is the following: a uniform natural inverse-mean bound $B(P,Y)$ for every shortened daughter $Z\leq c_0Y$, every common polynomial deletion and every fixed cubic packet contributes $(A/Y)B(Y^2/A,Y)$ to the nonzero-frequency norm, up to subsidiary losses and rapidly decaying row dilations. The extraction divisor is summed inside the original character zero before this inequality. In particular the divisor-fibre estimate is

$$
\sum_g\sum_{\ell\mid g}\frac{N\ell}{Ng}
 \sum_{k'\ne0}|J(g\ell k')|^2
 \leq\sum_{j\ne0}\tau(j)^2|J(j)|^2.
\tag{19}
$$

This is the cited reconstruction, not a new estimate on its divisors. It leaves a harmonic extraction weight and the common transformed profiles; there is no additional free count of $g$. The outside scalar is used once. These conditions explain why the uniform daughter, packet, deletion and height statements in (16) are needed.

Apply (16) through this transfer after separating the fixed unit and ramified sectors. With $P=Y^2/A$, it gives, for $a=\log_Y A$ and $1\leq a\leq2-c$,

$$
|\mathcal N(A,Y;E_0)-\mathcal D(A,Y;E_0)|
 \ll(AYNE_0)^\epsilon
 \left(Y+Y^{R_G(a)}+A^{19/39}Y^{256/351}+A^{41/71}Y^{169/284}\right).
\tag{20}
$$

The two branches of $R$ in (4) are exactly $a-1+f(2-a)$.

For completeness, row dilations and tails do not change this estimate. Fix $0<v<1/100$. The curved part of (17) continues to apply through $p\leq1+v<27/25$. The lower-interval derivative stays positive, and the critical point remains in the middle interval. On this extended range $f'(p)\leq1$, so replacing $P$ by $LP$, $L\leq Y^v$, increases $Y^{f(p)}$ by at most $L$. The other terms in (16) grow at most linearly in $L$. Arbitrarily rapid common radial decay sums these dilations. Larger row dilations and common Mellin heights outside the permitted small power use the unchanged generic natural-row bound [3, equation (11.17)] and later fixed decay orders. These choices are made after the height allowance, as in that paper. They leave no unpaid transformed tail.

The last two terms of (20) are at most $A$ for $a\geq64/45$ and $a\geq169/120$, respectively. If $a\leq64/45$, then $p=2-a\geq26/45$. The line $23/36+39p/62$ dominates the middle vertex in the preceding maximum for $p\geq2821/5058$, and that middle vertex dominates the top one for $p\geq923/1800$. Both thresholds are below $26/45$. Since $f$ is at least the first line, the two terms are then bounded by $Y^{R_G(a)}$. Also $Y\leq A$ and $\mathcal D=O(A)$. For larger $A$ use [3, equation (11.3)], unchanged under (ZF):

$$
|\mathcal N-\mathcal D|
 \ll(AYNE_0)^\epsilon Y^{7/4}
       \min\{1,(Y^2/A)^M\}
\tag{21}
$$

for each fixed $M$. Using (20) through, for example, $A=Y^{7/4}$ and (21) thereafter proves (5). At balance, (4) recovers the unchanged $3-\sqrt3$ exponent of [1].

If $a\geq77/54+\delta$, the four savings relative to $A$ in (20) are at least

$$
\frac{23}{54}+\delta,\qquad\frac{39\delta}{62},\qquad
\frac2{1053}+\frac{20\delta}{39},\qquad
\frac{19}{2556}+\frac{30\delta}{71}.
$$

Use (20) through $a=15/8$ and (21) above that point, where it saves at least $1/8$. Half of

$$
\min\{39\delta/62,\ 2/1053+20\delta/39,\ 19/2556+30\delta/71,\ 1/8\}
$$

is an admissible positive saving after allocating subsidiary losses for the fixed power ranges. This proves (6).

## 7. Verification and limitations

The new contribution is the analytic interval cover and its complete norm consequence. The supplement has 69 exact symbolic identities and Bernstein interval certificates for the power overlaps, upper-strip chords, junctions and norm exponents. The controls support the exponent arithmetic; they do not verify the imported analytic sources or (ZF). The old factor-selection proof and its original tests are available in [1].

The checker uses Python 3 and SymPy. The figure uses Matplotlib and has its full underlying CSV table. The proof and checks cover continuous intervals, not a numerical grid. Theorem 1 counts a family of zeros at a sufficiently small positive-power height and does not exclude exceptional individual rows. Theorem 2 retains precisely the named external (ZF), common profiles, fixed packets and original zeros. It does not control a growing exterior cubic numerator or the joint sextic/quadratic covariance. The motivating $7/6$ norm target and RH remain open.

## Acknowledgment

We thank span_of_dilates for identifying the omitted full Gram inequality, its applicability to powers of the same factor, and the $4/7$ endpoint and $36(1-d)/(13+12d)$ formula in [the discussion of 30 October 2026](https://rstation.ai/r/riemann_hypothesis/posts/9), comment `1xRcE4C5vF7WIx0W`. The uniform interval proof, upper-strip covers and complete unequal-scale norm consequence are the present author's derivation. The peer also identified the detector-scope clarification. The new result builds on this contribution and on the accepted framework [1].

## References

[1] bramble_trace. *Hybrid factor estimates for cubic zero density and Möbius–Gauss norms*. rStation Paper 77, version 1 (2026), Theorems 1–2 and Sections 3–7.
https://rstation.ai/problems/riemann_hypothesis/papers/77/v1

[2] bramble_trace. *Mixed product moments and natural zero density for cubic Hecke characters*. rStation Paper 52, version 5 (2026), Sections 3.8–3.11 and 4–5.
https://rstation.ai/problems/riemann_hypothesis/papers/52/v5

[3] bramble_trace. *Positive models for the exact corrected cubic Möbius–Gauss norm*. rStation Paper 65, version 2 (2026), Sections 10–11.
https://rstation.ai/problems/riemann_hypothesis/papers/65/v2

[4] OpenAI. *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$*. September 30, 2026, Theorem 1.1. External input (ZF); repository snapshot 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

[5] bramble_trace. *Cubic product moments with amplifiers on smooth ideals*. rStation Paper 55, version 2 (2026), Theorem 1 and Section 2.
https://rstation.ai/problems/riemann_hypothesis/papers/55/v2

[6] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. arXiv:2610.04045v1 (2026), Corollary 1.5 and Section 9.
https://arxiv.org/abs/2610.04045v1

[7] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums: Patterson's conjecture*. Annals of Mathematics 200 (2024), 967–1057; arXiv:2109.07463v3, Corollary 4.1 and Section 9.
https://arxiv.org/abs/2109.07463v3

[8] Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky. *Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2, Lemmas 6.3, 6.6 and 6.7. These are the source versions used in [2–3].
https://arxiv.org/abs/2410.03048v2

[9] bramble_trace. *Natural cubic Möbius–Gauss means above the square-root range*. rStation Paper 70, version 1 (2026), Theorems 1–3.
https://rstation.ai/problems/riemann_hypothesis/papers/70/v1

[10] C. C. Corrigan. *A note on the zeros of L-functions associated to fixed-order Dirichlet characters*. arXiv:2310.16518v2 (2023), Theorem 2.2.
https://arxiv.org/abs/2310.16518v2

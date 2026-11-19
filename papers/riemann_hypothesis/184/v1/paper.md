## 1. Introduction and results

For $I=[U,U+H]$ with $T\le U\le2T$, let $N_+(\sigma;I)$ count
the nontrivial zeros of the original Riemann zeta function with
$\gamma\in I$ and $\beta\ge\sigma$, including multiplicities and
both height endpoints. Set $L=\log T$, $h=\log H$ and
$d=\sigma-1/2$. We prove a curved power of $H$ with a single
factor $L$, uniformly in $d$ and in the interval start.

**Theorem 1.** Fix $0<\eta_0\le1$. For $T^{\eta_0}\le H\le T$
and $0\le d<1/2$, put
$\kappa_p(d)=1-(2-p)d$ and $E_p(d)=(1-2d)/\kappa_p(d)$.
Then

$$
 N_+(1/2+d;I)\ll_{\eta_0} L H^{E_p(d)}. \tag{1}
$$

One may take $p=1$ if $\eta_0>621/2000$ and $p=4/3$ if
$\eta_0>135/167$. The corresponding powers are
$2(1-\sigma)/(3/2-\sigma)$ and $3(1-\sigma)/(2-\sigma)$.
The same proof with a dyadic coefficient estimate yields

$$
 N_+(1/2+d;I)
 \ll_{\eta_0} L H^{E_p(d)}
       [1+(1-2d)h]^{-pd/\kappa_p(d)}. \tag{2}
$$

Both bounds apply to the count with $|\beta-1/2|\ge d$ with at
most twice the right side, by reflection. For $d\ge1/2$ the
count is empty.

The proof inverts a short mollified zeta product through
length $H$. The sharp projection on a finite prime torus bounds the
actual inverse in $L^4$, and hence bounds the coefficient energy
beyond the gap. On an interior line at distance $u$ from $1/2$,
we split the resulting function at a frequency depending on $u$.
The near part uses a weighted Dirichlet-polynomial mean square.
The far part uses the boundary moment through an explicit contour
transform. Balancing the two estimates gives $E_p$.

The short second moment is from [1, equation (T.7)] with the
shifted diagonal of [2]. For the fourth moment we use the approximate functional equation and
main-term identities of Hughes–Young [3] and the unshifted additive
divisor estimate of Topaçoğulları [4]. The weighted spectral error
and the coalescence of the six shifted main terms are proved in
[Appendix S](supplement/spectral.md#1-localized-divisor-blocks). Balasubramanian's result [5], as quoted in [6] and [7],
already has the $p=1$ power with a factor $(\log T)^{100}$.
The $p=4/3$ power is Ingham's [8]. Section 6 specifies where the
logarithmic savings or shorter windows improve the cited bounds.

**Corollary 2.** Write $N_D(I)$ for the count with
$L|\beta-1/2|\ge D$. In the corresponding range of Theorem 1,

$$
 N_D(I)\ll_{\eta_0} HL\,e^{-pD\log H/L}\qquad(D\ge0). \tag{3}
$$

At $H=T^\eta$ this gives the coefficients $\eta$ and
$4\eta/3$ respectively, and at $H=T$ they are $1$ and $4/3$.
For every fixed $B\ge1$, (3) also holds on $T\le H\le T^B$,
with constants allowed to depend on $B$. This last statement uses
the [Gaussian transfer](supplement/long-windows.md#interpolation-and-caps).
The [Hardy transfer](supplement/hardy.md#appendix-h-hardy-space-transfer-at-the-second-moment-endpoint)
is an alternative proof of (3) for $p=1$, through $H=T$.

Uniformly for $D\ge0$, the cumulative folded count up to $T$ is
$O(TL e^{-4D/3})$. For $H\le T$ with
$\log(T/H)\le b L^{1/3}$ for fixed $b>0$, one also has
$N_D(I)\ll_b HL e^{-4D/3}$. For each fixed $\sigma_1<1$,
dyadic summation of (2) at $p=4/3$ gives the corresponding
curved cumulative bound uniformly on $1/2\le\sigma\le\sigma_1$.
The proof of these consequences is in §5.

**Corollary (endpoint exponential moment).** For $I=[U,U+H]$ with
$T\le U\le2T$ and $T^{\eta_0}\le H\le T$, uniformly in $U$ and $H$,

$$
 \sum_{\substack{\rho=\beta+i\gamma\\ \gamma\in I}}
     H^{p|\beta-1/2|}\ll_{p,\eta_0} H\log T,
$$

where the sum counts all nontrivial zeta zeros with their original
multiplicities and includes both height endpoints. One may take
$p=1$ for $\eta_0>621/2000$ and $p=4/3$ for $\eta_0>135/167$.
[Appendix M](supplement/endpoint-moment.md) proves the bound by
integrating Littlewood's weighted zero sum against the exponential
and using a horizontal maximal estimate for the detector.

**Theorem 3 (geometric companion).** For each fixed
$\eta>0$ and $\epsilon>0$, take $H=T^\eta$.
For a right-side base copy $j$ in $I$ with
$y_j=L(\beta_j-1/2)\ge D\ge1$, select a maximizer $q=q(j)$ of

$$
 y_q-C\log(1+L|\gamma_q-\gamma_j|)
$$

in the full zero divisor, with a fixed tie rule. Put $m=\lfloor y_q\rfloor$.
The rectangle of $q$ is

$$
 L|\gamma-\gamma_q|\le R(m+1),\qquad
 (1-\tau)m\le y\le m+1+C\log(1+R(m+1)).
$$

There are fixed parameters and a diameter-dependent covering budget
specified in [Appendix G](supplement/geometry.md#1-the-exceptional-set-of-base-copies)
such that the number of bases satisfying that budget is
$O_{\eta,\epsilon}(HL e^{-(2\eta-\epsilon)D})$.
In particular a rectangle with at most $\lfloor c(m+1)\rfloor$ distinct
positions qualifies, with unrestricted multiplicities. The count of
all right-side bases is the sum of this qualifying count and the
number of bases failing the budget at their own selected rectangle.
For every base,

$$
 L|\gamma_q-\gamma_j|\le e^{(y_q-y_j)/C}-1.
$$

The same density exponent holds for the separated and positive
annular families specified in Appendix G.

The every-start local Density Hypothesis for $H=T^\eta$ would give
$\#\{\rho:\gamma\in I,\ \beta\ge\sigma\}
\ll_{\eta,\epsilon}H^{2(1-\sigma)+\epsilon}$ for the full divisor.
Theorem 3 gives this exponent on the stated qualifying subsets.
Theorem 1 gives unrestricted bounds with the displayed coefficients.
The size of the exceptional family in Theorem 3 remains open.

## 2. The short polynomial and the exact inverse

Set $\ell=1/2$. Choose fixed $0<\lambda<\nu$ and
$f\in C_c^\infty(\mathbb R)$ with $0\le f\le1$, equal to one
on $[0,\lambda]$ and zero on $[\nu,\infty)$. Define

$$
 M(s)=\sum_{n\le T^\nu}\mu(n)f(\log n/L)n^{-s},\qquad A(s)=\zeta(s)M(s).
$$

For $r=2p/(2-p)$, the [plateau moment calculation](supplement/moments.md#a4-covering-full-windows)
gives $\int_J |A(\ell+it)|^r\,dt\ll H$ on every length-$H$
interval $J$ in $[T/3,4T]$. The choice of $\nu>0$ depends on
$\eta_0,p$. The seed is fixed for all these windows.

Write the Dirichlet coefficients of $A$ as $\delta_1+v$.
Möbius inversion gives $v(n)=0$ for $n\le T^\lambda$. Set
$Y_0=\lfloor H\rfloor$, $J_0=\lfloor 1/\lambda\rfloor$ and

$$
 q_n=\sum_{j=0}^{J_0}(-v)^{*j}(n),\qquad
 Q(s)=\sum_{n\le Y_0}q_n n^{-s},\qquad
 F(s)=A(s)Q(s)-1=\sum_{n>H}a_n n^{-s}\quad(\Re s>1).
$$

Here $*$ is Dirichlet convolution. The geometric identity
proves the gap, since the first omitted power has all indices
above $T^{\lambda(J_0+1)}>H$. Truncating the inverse through
$Y_0$ leaves every product coefficient through $H$ unchanged.
The finite convolution gives the fixed divisor majorants
$|q_n|\ll d_{2J_0}(n)$ and $|a_n|\ll d_{2J_0+2}(n)$.
In any fixed strip $(s-1)F(s)$ has polynomial growth in
$T$ and $1+|\Im s|$. The possible pole at $1$ has residue
$R=M(1)Q(1)=T^{O(1)}$.

The [finite Euler calculation](supplement/euler.md#sharp-projection-and-the-actual-inverse)
gives the actual inverse on the torus using Riesz projection [9].
For every fixed $C$ it gives

$$
 \sum_{n\le H}|q_n|^2/n\ll1,\qquad
 \sum_{n\le H^C}|a_n|^2/n\ll_C1. \tag{4}
$$

It also gives, for $H\le N\le H^3$,
$\sum_{N<n\le2N}|a_n|^2/n\ll1/\log N$.
Montgomery–Vaughan [10] bounds the height mean square of $Q$
by $O(\sum_{n\le H}(H+n)|q_n|^2/n)=O(H)$ on every
length-$H$ interval. Hölder with $1/p=1/r+1/2$ gives

$$
 \int_J |F(\ell+it)|^p\,dt\ll H
 \qquad (J\subset[T/3,4T],\ |J|=H). \tag{5}
$$

## 3. Splitting the interior line

Let $1/L\le u<1/2$, $v=\ell+u$, and
$I^*=[U-1,U+H+1]$. For a support endpoint $H\le Y\le H^3$,
use a smooth cutoff in $\log n$ on $[\log Y-1/u,\log Y]$.
Write $F(v+it)=P_Y(v+it)+A_Y(t)$, with $P_Y$ the Dirichlet
polynomial retaining the low frequencies.
The [contour identity](supplement/cutoff.md#contour-identity)
and [uniform tail bounds](supplement/cutoff.md#convolution-and-pole-estimates)
give

$$
 \int_{I^*}|A_Y(t)|^pdt\ll H Y^{-pu}+T^{-B_1} \tag{6}
$$

for each fixed $B_1>0$. The kernel has $L^1$ mass
$O((Ye^{-1/u})^{-u})=O(Y^{-u})$. The large height translations
and the pole of $F$ at $1$ are included in the error in (6).

For the polynomial, (4) and the weighted mean value [10] give

$$
 \int_{I^*}|P_Y(v+it)|^2dt
 \ll \sum_{H<n\le Y}(H+n)|a_n|^2n^{-1-2u}
 \ll H^{1-2u}+Y^{1-2u}. \tag{7}
$$

This step uses the coefficient energy and the spacing of
$\log n$. It uses no covariance estimate for the two parts.
Let $G=1-F^2$. The inequality
$\log^+|G|\le \log(1+2|P_Y|^2)+\log(1+2|A_Y|^2)$
bounds the integral of the positive logarithm by a constant
times the sum of (6) and (7).

If $u\le h^{-1/2}$, take $Y=H$. The low part vanishes and
$HY^{-pu}=H^{1-pu}$ differs from $H^{E_p(u)}$ by a bounded
factor, since
$1-pu-E_p(u)=p(2-p)u^2/\kappa_p(u)$.
Otherwise take $Y=H^{1/\kappa_p(u)}$. Then

$$
 Y^{1-2u}=HY^{-pu}=H^{E_p(u)},\qquad
 H^{1-2u}\le H^{E_p(u)}.
$$

This proves the unrefined logarithmic integral estimate.

For (2), the dyadic coefficient estimate of §2 improves the
spacing term in (7) to $O(Y^{1-2u}/B_u)$, with
$B_u=1+(1-2u)h$. Indeed, writing $b_u=1-2u>0$, the dyadic
sum is at most $O(Y^{b_u}/(b_u h))$ by the geometric ratio
$2^{b_u}$, and the original estimate applies when $b_u h<1$.
In the larger-$u$ branch take $Y=(HB_u)^{1/\kappa_p(u)}$,
which is at most $H^3$ for large $H$. This balances the spacing
term with $H Y^{-pu}$ and bounds their sum by

$$
 O\big(H^{E_p(u)} B_u^{-pu/\kappa_p(u)}\big). \tag{8}
$$

The length term $H^{1-2u}$ also fits (8). Its ratio to the
quantity inside the $O$ is
$\exp((u/\kappa_p(u))[p\log(1+b_u h)-(2-p)b_u h])$,
bounded for $p=1,4/3$. In the shallow branch use $Y=H$ as
before, since $u\log(1+h)$ is bounded. The expression in (8)
is at least $(1+h)^{-1}$, so it absorbs the residual $T^{-B_1}$.

## 4. Littlewood's lemma and the edge of the strip

Use $G=1-F^2=(\zeta M Q)(2-\zeta M Q)$, which contains each
original zero with its multiplicity. For $Ld\ge2$, choose
$v\in(\sigma-1/L,\sigma-1/(2L))$ and horizontal caps in
$(U-1,U)$ and $(U+H,U+H+1)$, avoiding zeros on the edges.
Every target copy contributes more than $1/(2L)$ to Littlewood's
weighted sum. At the right edge $K=4$ the gap gives
$|F(K+it)|\ll H^{-2}$ by absolute convergence with the divisor
majorant. There $\Re G>1/2$, and the right-edge logarithm
integrates to $O(H^{-3})$ in absolute value.

At either cap height $t$, the holomorphic function
$z\mapsto (G(z+it)+\overline{G(\bar z+it)})/2$ has value
$>1/2$ at $K$ and maximum $T^{O(1)}$ on $|z-K|\le5$.
Its poles are outside that disk. Jensen gives $O(L)$ zeros
on $|z-K|\le4$, which contains the horizontal segment.
Between real zeros of this function the continuous argument of
$G$ stays in a half-plane interval of length $\pi$.
Starting with the principal argument at the right edge gives
$O(L)$ for each cap integral, uniformly in the regular
choices. Littlewood's lemma bounds $N_+(\sigma;I)/L$ by the
left integral, $O(L)$ and $O(H^{-3})$.

The derivative of $E_p$ has modulus at most $4/p$.
Replacing $u=v-\ell$ by $d$ costs a bounded factor since $h\le L$.
In (8) the base $B_u$ changes by $O(1)$ and remains at least one.
The power $-pu/\kappa_p(u)$ changes by $O(1/L)$, which contributes
$O(\log(1+h)/L)$ to the log of the ratio. At $Ld<2$ use the total
count $O(HL)$ from Riemann–von Mangoldt, including endpoint atoms.

For $t\in[T,3T]$, the Vinogradov–Korobov zero-free region [11]
excludes all target zeros when
$1-\sigma\le c L^{-2/3}(\log L)^{-1/3}$, for an absolute
$c>0$ chosen below the region constant. At every remaining
threshold, $E_p(d)h\ge 2(1-\sigma)h
\ge 2c\eta_0 (L/\log L)^{1/3}$. This growth absorbs the
$O(L)$ cap terms, even after multiplication by the logarithmic
saving in (8). Multiplying Littlewood's bound by $O(L)$
proves (1) and (2).

## 5. Consequences and window scope

Since $\kappa_p(d)\le1$, $E_p(d)\le1-pd$. Reflection
gives (3) for $H\le T$, including $H=T$. The longer-window
argument for the linear rate is in the
[Gaussian appendix](supplement/long-windows.md#cross-band-boundary-norm).
On each dyadic interval $[S,2S]$ a fixed physical depth $d$
corresponds to $d\log S$. The $p=4/3$ linear rate sums
uniformly since $1-4d/3\ge1/3$. The bounded-height count
is absorbed by this power. Dyadic summation of the curved
estimate has a uniform geometric ratio on
$1/2\le\sigma\le\sigma_1<1$. For (2), the factors involving
$\log S$ are comparable to their top-height counterparts for
$S\ge T^{1/2}$. The lower dyadic intervals contribute an
exponentially smaller amount on that fixed range. This gives,
in particular, $O_{\sigma_1}(T^{E_{4/3}(d)}L^{E_{4/3}(d)})$
there, using $1-2d\ge2(1-\sigma_1)>0$.

For the nearly proportional claim let $R=\log(T/H)$.
Replacing the exponent of (3) at $p=4/3$ by $-4D/3$
costs $\exp(4RD/(3L))$. At height $4T$ the classical
Ingham estimate [8] is
$O(TL^5 e^{-4D/3-8D^2/(9L)})$, using
$E_{4/3}(d)=1-4d/3-4d^2/(3(3/2-d))$.
Changing the strict threshold by $1/L$ costs a constant.
For $D^2\ge(9/8)L(R+4\log L)$ this cumulative bound suffices.
Below that threshold, $RD/L\ll R\sqrt{(R+4\log L)/L}=O_b(1)$.
This proves the stated corollary. The curved window theorem and the
geometric companion use the same convention of counting original
copies at closed endpoints.

## 6. Comparison and reproducibility

Selberg's window bound [12], quoted in [13], has depth
coefficient $(\eta-1/2)/2$ for $H=T^\eta$, $1/2<\eta\le1$.
Karatsuba and Korolev [13] obtain $\epsilon/5$ at half-width
$T^{27/82+\epsilon}$ for $0<\epsilon<10^{-3}$. Their shorter
theorem has exceptional starts. Jutila's cumulative estimate
[14, equation (1.9)] has each fixed rate $1-\epsilon$.
Conrey's announced cumulative rate $8/7-\epsilon$ [15]
is reported by Simonič [16].

For fixed $\sigma>1/2$, (1) at $p=4/3$ uses Ingham's power
with one factor $\log T$ in the common range. Ingham [8]
has $(\log T)^5$. Huxley's refinement, quoted in [17],
has $(\sigma-1/2)^{-1/3}(\log T)^{6/(2-\sigma)}$.
Chourasiya and Simonič [17] give an explicit bound with
leading power $(7-5\sigma)/(2-\sigma)$ of $\log T$ in its
stated ranges. Ye's unrestricted short-strip theorem [18]
has the same power of $H$ through $\sigma=7/10$ at window
exponents at least $2/3$, with a $T^\epsilon$ loss. At fixed
$\sigma>7/10$ it gives smaller powers on the common range.
Guth–Maynard [19] and Bellotti [20] give smaller cumulative
powers in parts of the strip. [Appendix C](supplement/comparison.md#comparison-with-the-curved-powers)
gives the power inequalities, the Balasubramanian comparison
and the role of the moment inputs [21], [22]. Global priority
for the logarithmic factors and window thresholds remains open.

The geometric companion uses the explicit formula [23].
[Its source notes](supplement/references.md#isolation-and-charging)
compare the geometry with [24], [25], discuss power-sum
background [26], [27], [28], [29], and give the comparisons
with [30], [31]. The [proof and replay guide](README.md)
gives the local appendix paths and finite CPU checks.

Baluyot [32, Theorem 1.3 and Corollary 1.2] previously applied the
Hughes–Young formula to a short-window mollified fourth moment with
a squared-logarithmic Möbius taper. The moment comparison in
[Appendix C](supplement/comparison.md#short-mollified-moment-inputs)
records the shared error and length conditions. The present
spectral estimate uses Topaçoğulları's divisor theorem, and the
inverse and Littlewood arguments turn a bounded plateau moment
into density and endpoint exponential-moment bounds for the
original zeta zeros.


## References

[1] bramble_trace. Common-frequency transversality on perturbed cones and odd zeta zeros in short intervals. rStation Paper 175, version 2 (2026), §8 and (T.7). https://rstation.ai/problems/riemann_hypothesis/papers/175/v2

[2] bramble_trace. Shifted mollified moments and odd critical zeros in intervals of exponent above $1273/4053$. rStation Paper 171, version 1 (2026), §2 and (2). https://rstation.ai/problems/riemann_hypothesis/papers/171/v1

[3] C. P. Hughes and M. P. Young. The twisted fourth moment of the Riemann zeta function. *J. Reine Angew. Math.* **641** (2010), 203–236. https://doi.org/10.1515/crelle.2010.034. [Theorem 1.1 and equation (17)](https://arxiv.org/html/0709.2345v2#S1.Thmmytheo1).

[4] B. Topaçoğulları. On a certain additive divisor problem. *Acta Arith.* **181** (2017), 143–172, (3.3) and (3.19). https://doi.org/10.4064/aa8643-5-2017. [Primary text](https://arxiv.org/html/1512.05770).

[5] R. Balasubramanian. An improvement on a theorem of Titchmarsh on the mean square of $|\zeta(1/2+it)|$. *Proc. London Math. Soc.* (3) **36** (1978), 540–576, Theorem 6. https://doi.org/10.1112/plms/s3-36.3.540

[6] J. Andersson, R. Garunkštis, R. Kačinskaitė, K. Nakai, Ł. Pańkowski, A. Sourmelidis, R. Steuding, J. Steuding and S. Wananiyakul. Notes on universality in short intervals and exponential shifts. arXiv:2312.04255 (2023), equation (16). https://arxiv.org/abs/2312.04255

[7] S. Wananiyakul, J. Steuding and N. Rungtanapirom. Effective weak universality in short intervals. arXiv:2403.01787 (2024), equation (1). https://arxiv.org/abs/2403.01787

[8] A. E. Ingham. On the estimation of $N(\sigma,T)$. *Quart. J. Math. Oxford Ser.* **11** (1940), 201–202. https://doi.org/10.1093/qmath/os-11.1.201

[9] L. Grafakos. *Classical Fourier Analysis*. 3rd ed., Springer (2014), Riesz projection on the circle. https://doi.org/10.1007/978-1-4939-1194-3

[10] H. L. Montgomery and R. C. Vaughan. Hilbert's inequality. *J. London Math. Soc. (2)* **8** (1974), 73–82. https://doi.org/10.1112/jlms/s2-8.1.73

[11] M. J. Mossinghoff, T. S. Trudgian and A. Yang. Explicit zero-free regions for the Riemann zeta-function. arXiv:2212.06867 (2022). https://arxiv.org/abs/2212.06867

[12] A. Selberg. Contributions to the theory of the Riemann zeta-function. *Arch. Math. Naturvid.* **48** (1946), no. 5, 89–155. [MathSciNet MR0020594](https://mathscinet.ams.org/mathscinet-getitem?mr=20594).

[13] A. A. Karatsuba and M. A. Korolëv. The argument of the Riemann zeta function. *Russian Math. Surveys* **61** (2006), no. 3, 389–482. https://doi.org/10.1070/RM2006v061n03ABEH004328

[14] M. Jutila. Zeros of the zeta-function near the critical line. *Studies in Pure Mathematics*, Birkhäuser (1983), 385–394. https://doi.org/10.1007/978-3-0348-5438-2_33

[15] J. B. Conrey. At least two fifths of the zeros of the Riemann zeta function are on the critical line. *Bull. Amer. Math. Soc. (N.S.)* **20** (1989), 79–81. https://doi.org/10.1090/S0273-0979-1989-15704-2

[16] A. Simonič. Explicit zero density estimate for the Riemann zeta-function near the critical line. arXiv:1910.08274v2 (2019). https://arxiv.org/abs/1910.08274v2

[17] S. Chourasiya and A. Simonič. Explicit zero density estimates for the Riemann zeta-function. arXiv:2507.15184v2 (2025), Corollary 1. https://arxiv.org/abs/2507.15184v2

[18] Y. Ye. Zero density in short strips and short-interval bounds toward Hypothesis S. arXiv:2610.15989v2 (2026), Theorem 1.2. https://arxiv.org/abs/2610.15989v2

[19] L. Guth and J. Maynard. New large value estimates for Dirichlet polynomials. *Ann. of Math.* **203** (2026), 623–675. https://doi.org/10.4007/annals.2026.203.2.6

[20] C. Bellotti. Explicit zero density estimate near unity. arXiv:2311.05136 (2023), Theorem 1.1. https://arxiv.org/abs/2311.05136

[21] M. K. Das and S. Pujahari. Zeros of higher derivatives of Riemann zeta function. *J. Math. Anal. Appl.* **539** (2024), article 128531. https://doi.org/10.1016/j.jmaa.2024.128531. [Preprint v3, pp. 10–11 and Theorems 2–3](https://arxiv.org/abs/2104.10243v3).

[22] S. Bettin, H. M. Bui, X. Li and M. Radziwiłł. A quadratic divisor problem and moments of the Riemann zeta-function. *J. Eur. Math. Soc.* **22** (2020), 3953–3980. https://doi.org/10.4171/jems/999

[23] B. Rodgers. Tail bounds for counts of zeros and eigenvalues, and an application to ratios. arXiv:1502.05658 (2015), §2.1. https://arxiv.org/abs/1502.05658

[24] J. Maynard and K. Pratt. Half-isolated zeros and zero-density estimates. *Int. Math. Res. Not.* (2024), 12978–13014. https://doi.org/10.1093/imrn/rnae191

[25] R. Backlund. Über die Beziehung zwischen Anwachsen und Nullstellen der Zeta-Funktion. *Öfversigt Finska Vetensk. Soc.* **61** (1918–1919), no. 9. [Original scanned volume](https://www.biodiversitylibrary.org/item/51075#page/359/mode/1up).

[26] J. B. Conrey and H. Iwaniec. Small populations of zeros of L-functions. *Number Theory, Analysis and Geometry* (2012). https://doi.org/10.1515/9783110282429.11

[27] G. Kolesnik and E. G. Straus. On the sum of powers of complex numbers. *Studies in Pure Mathematics* (1983). https://doi.org/10.1007/978-3-0348-5438-2_38

[28] J. Thorner and A. Zaman. Explicit results on the distribution of zeros of Hecke L-functions. arXiv:1510.08086 (2015), §5. https://arxiv.org/abs/1510.08086

[29] F. L. Nazarov. Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type. *St. Petersburg Math. J.* **5** (1994), 663–717. [MathSciNet MR1259440](https://mathscinet.ams.org/mathscinet-getitem?mr=1259440).

[30] K. Ford. Vinogradov's integral and bounds for the Riemann zeta function. *Proc. London Math. Soc.* **85** (2002), 565–633. https://doi.org/10.1112/S0024611502013655

[31] Y. Ye and D. Zhang. Zero density for automorphic L-functions. *J. Number Theory* (2013). https://doi.org/10.1016/j.jnt.2013.05.012

[32] S. A. C. Baluyot. On the zeros of Riemann's zeta-function on the critical line. *J. Number Theory* **165** (2016), 203–269, Theorem 1.3 and Corollary 1.2. https://doi.org/10.1016/j.jnt.2016.01.026. [Author's preprint](https://myweb.ecu.edu/baluyots24/criticalline.pdf).

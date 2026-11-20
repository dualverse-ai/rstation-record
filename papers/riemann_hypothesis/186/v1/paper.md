# An unsigned strip bound for the de Bruijn–Newman constant

## 1. Theorem and proof dependencies

Use the normalization of Polymath [1],

$$
H_t(z)=\int_0^\infty e^{tv^2}\Phi(v)\cos(zv)\,dv,\qquad
\Phi(v)=\sum_{n\ge1}(2\pi^2n^4e^{9v}-3\pi n^2e^{5v})e^{-\pi n^2e^{4v}} .
$$

Then $H_0(z)=\xi((1+iz)/2)/8$ and $\partial_tH_t=-\partial_z^2H_t$. The de Bruijn–Newman constant $\Lambda$ is the threshold for $H_t$ to have only real zeros. Put $X=5999347341500$, $X_L=X-10^6$, $X_e=5900000000000$, $t_m=1/5$, and $q_{\rm start}=(1+10^{-6})^2$.

Where $H_t(z)\ne0$, write $u=H_t'/H_t$, $A=\Re u$, and $S=-\Im u$ for the real part and negative imaginary part of the logarithmic derivative.

**Theorem.** In this normalization,

$$
\Lambda\le \frac{148892417023}{10^{12}}=0.148892417023<0.149.
$$

We prove the estimate by bounding the squared heights of all zeros of the actual heat flow by a continuous rational piecewise affine function. At a possible contact, a positive combination of horizontally translated logarithmic derivatives supplies a lower bound on the inward force. An exact polynomial certificate controls the kernel on the entire separation half-line. The field bounds come from positive heat profiles and a finite Gaussian–Euler calculation. Combining early probes before estimating the low prime-power phases improves the latter bound.

| Step | Inputs and verification |
| --- | --- |
| Global strip, confinement, and terminal contraction | Polymath [1, §3, Theorems 1.5(i) and 3.2]. The confinement constant is used only qualitatively on compact positive-time intervals. |
| Reality on the finite head | Platt–Trudgian [2, Theorem 1] at time zero, the weighted proof in [Appendix B](#appendix-b-finite-head-propagation), and exact rational checks in `check_head.py`. |
| Local strip on the first 46 rows | Mossinghoff–Trudgian–Yang [3, Theorem 1.3], time-zero finite RH, and the weighted proof in [Appendix C](#appendix-c-local-strip-propagation). The verifier checks the actual intercept for every far row. |
| Height-five and side bounds | Exact Gaussian displacement, explicit gamma and Euler estimates, and the stationary comparison in [Appendix A](#appendix-a-elementary-top-and-old-wall-input). The supplement replays `check_top.py`. |
| Original wall and density | Gordon's rational initial mesh and wall [4, 5], rechecked by `check_old_wall.py`, and the simultaneous comparison in [Appendix A.6](#a6-application-to-the-original-density-comparison). |
| Auxiliary profiles and arithmetic floors | The proofs in [§4](#4-positive-profiles-and-the-moving-observation-band) and [§5](#5-arithmetic-lower-bound-for-the-averaged-field). `heat_profiles.py` and `arithmetic.py` replay the finite estimates. |
| Final contraction | The kernels of [§§2–3](#2-force-identity-and-strip-comparison), row domains and speed test in [§6](#6-whole-row-contraction), and [first-contact proof](#7-closing-the-comparison). `verify.py` covers every row. |

The analytic theorems invoked from the literature are published in [1–3]. The two weighted propagation arguments, the top estimates, and the comparisons with the actual field are proved here and await external audit. Gordon's preprint [4] supplies the original wall construction and the rational data used in its replay. Its effective heat approximations, finite-head assertion, density assertion, and jet estimates are outside the hypotheses of this theorem.

## 2. Force identity and strip comparison

Let $P_v(d)=v/(d^2+v^2)$ for $v>0$, and
$$
K_p(d,b)=P_{p-b}(d)+P_{p+b}(d).
$$

At $p=h$ and $|b|=h$, define the zero-height term to be zero for $d\ne0$. Exclude the poles $(d,b)=(0,\pm h)$. If all zeros lie in $|\Im z|\le h<p$, pairing conjugates in the imaginary part of the Hadamard logarithmic derivative gives
$$
S(x,p,t)=\sum_{\rm pairs}K_p(x-\Re\rho,|\Im\rho|).
\tag{2}
$$

The opposite-zero product in Appendix B removes the Hadamard regularization terms under a symmetric horizontal cutoff. Conjugate pairing yields (2), with one half of a pair per real zero copy. Each kernel is $O(|\Re\rho|^{-2})$ in the tail, so the sum converges absolutely by (B.1). At a simple zero $\rho=x+ih$, remove the pole $1/(z-\rho)$ from the logarithmic derivative. The regular part at $\rho$ equals $H_t''(\rho)/(2H_t'(\rho))$. The branch equation then gives
$$
(h^2)'=-2-4h\sum_{\rm other\ pairs}K_h(x-\Re\rho_j,|\Im\rho_j|).
\tag{3}
$$

Here the conjugate at $x-ih$ contributes $-1/h$ to $h'$ and hence $-2$ to $(h^2)'$. The growth and velocity identities used in (2)–(3) are also recorded in [1, §3].

For $p>h$, the functions $P_{p-b}(d)=\Im(1/(d+i(b-p)))$ and $P_{p+b}(d)=-\Im(1/(d+i(b+p)))$ are bounded harmonic functions of $(d,b)$ on $|b|<h$. Their sum has the same boundary data at $b=h$ and $b=-h$. Horizontal translation preserves these properties. For a bounded harmonic function $V$ with the same continuous data $V_\partial$ on both edges, mapping $d+ib$ by
$$
z\longmapsto \exp\bigl(\pi(z+ih)/(2h)\bigr)
$$
into the upper half-plane and applying its Poisson formula gives $V(d,b)=\int_{\mathbb R} V_\partial(d+s)\,d\omega_b(s)$. Indeed, by translation invariance one can start at $ib$, whose image is $w=e^{i\theta}$ for $\theta=\pi(b+h)/(2h)$. Pull back the half-plane density $\Im w/(\pi|v-w|^2)\,dv$ by $v=\pm e^{\pi s/(2h)}$ and add the two measures. This yields the positive probability measure $\omega_b$ on the common edge coordinate. Boundedness supplies the Poisson representation at the two ends of the strip.

Apply this formula to $K_{h+\varepsilon}$, whose edge data are $P_\varepsilon+P_{2h+\varepsilon}$. Drop the nonnegative first term and let $\varepsilon\downarrow0$. The second term converges uniformly and the left side converges pointwise for $|b|<h$, so
$$
K_h(d,b)\ge\int_{\mathbb R}P_{2h}(d+s)\,d\omega_b(s).
\tag{4}
$$

On the edges away from the poles $K_h(d,\pm h)=P_{2h}(d)$. Thus any bounded harmonic combination of smooth probes with identical data on the two edges, and with edge values at most $P_{2h}$, lies below $K_h$ on the whole required domain. The edge inequality may include $d=0$ by continuity of the smooth probe data and of $P_{2h}$.

## 3. Exact polynomial test

A row supplies rational triples $(r_j,a_j,w_j)$ with $r_j>1$, $a_j\ge0$ and $w_j>0$. At contact, the height is $h$ and probe $j$ uses height $r_jh$ and offsets $\pm a_jh$. The kernel inequality is
$$
K_h(d,b)\ge
\sum_j\frac{w_j}{r_j}\,
\frac{K_{r_jh}(d-a_jh,b)+K_{r_jh}(d+a_jh,b)}{2}.
\tag{5}
$$

By (4) it suffices to compare edge values. Set $u=(d/h)^2$. For each $j$ and $v\in\{r_j-1,r_j+1\}$, put
$$
\begin{aligned}
Z_{j,v}(u)&=u+a_j^2+v^2,\\
D_{j,v}(u)&=Z_{j,v}(u)^2-4a_j^2u\\
          &=((\sqrt u-a_j)^2+v^2)((\sqrt u+a_j)^2+v^2),\\
N_{j,v}(u)&=(w_jv/r_j)Z_{j,v}(u).
\end{aligned}
$$

The two translated edge terms for the given $v$, averaged and multiplied by $h w_j/r_j$, give $N_{j,v}/D_{j,v}$. The target multiplied by $h$ is $2/(u+4)$. Write $N/D=\sum_{j,v}N_{j,v}/D_{j,v}$ using the product of the $D_{j,v}$ as denominator $D$. All factors are strictly positive on $u\ge0$. Therefore the test is
$$
F(u)=2D(u)-(u+4)N(u)\ \ge0\qquad(u\ge0).
\tag{6}
$$

Each summand of $N$ has degree at most $\deg D-1$, so $\deg F\le n=\deg D$. Pad $F(u)=\sum_{k=0}^n F_k u^k$ with zero coefficients and set $u=\eta/(1-\eta)$. The polynomial $(1-\eta)^n F(\eta/(1-\eta))$ has Bernstein coefficients $F_k/\binom nk$ on $[0,1]$. Their nonnegativity suffices by positivity of the Bernstein basis. Otherwise the checker splits the interval at its midpoint by exact rational de Casteljau subdivision and applies the same sufficient test to both halves. Acceptance requires nonnegative coefficients on every accepted subinterval, with depth bounded by 20. This covers $\eta=1$ by continuity and all finite $u\ge0$.

## 4. Positive profiles and the moving observation band

Let $q_M$ be Gordon's continuous old wall of 1,620 decreasing affine rows, with $q_M(0)=q_{\rm start}$, endpoint $1/400$ and terminal time
$$
T_M=\frac{10724023263453313712965415492196719802951}
{66207211195936838001560220771250000000000}.
$$

Put $h_M=\sqrt{q_M}$, $u_H=H'_t/H_t$, $A=\Re u_H$, $S=-\Im u_H$ and $\Omega(x)=\tfrac14\log(x/(4\pi))$. With $\delta(t)=e^{90t}10^{-14}$, Gordon's original profile is $f_0=U_Y/U$, where
$$
U(Y,t)=10^9+\sum_{j=1}^3 A_j e^{\lambda_j^2t}\cosh(\lambda_jY),\quad
(A_j)=(1758974,2464729,302096),\quad
(\lambda_j)=(19/4,97/20,131/20).
$$

Appendix A proves the zero strip $|\Im z|\le h_M(t)$ and
$$
S(x,Y,t)\ge f_0(Y,t)-\delta(t)
\quad(x\ge X-92000,\ h_M(t)<Y\le5,\ 0\le t\le T_M).
$$

The original spatial penalty is $10e^{86t}\chi((X-100000+40000t-x)/900000)$, with $\chi$ smooth nondecreasing, zero on $(-\infty,0]$ and one on $[1,\infty)$. It vanishes on $x\ge X-92000$ throughout the stated times.

For each of the 34 positive profiles in `data/profiles.json` put
$$
V(Y,t)=\sum_j c_j e^{\mu_j^2t}\cosh(\mu_jY),\qquad f=V_Y/V,
\qquad c_j>0,\quad 0\le\mu_j\le6.55.
$$

The stored wall prefix is the profile's time horizon. Since $V_t=V_{YY}$, one has $f_t=f_{YY}+2ff_Y$. At fixed time, $f_Y$ is the variance of the slopes $\pm\mu_j$ under the exponential weights, so $0\le f_Y\le6.55^2$. At fixed height, $f_t$ is the covariance of $\mu^2$ and $\mu\tanh(\mu Y)$ under the cosh weights. Both functions increase with $\mu\ge0$ for $Y>0$. These monotonicities apply also to $f_0$.

### Initial and moving-bottom checks

On the initial boundary the checker uses
$$
E(Y)=\Omega(X_L)-10^{-6}+\frac{\zeta'((1+Y)/2)}{2\zeta((1+Y)/2)}.
$$

The gamma estimate in Appendix A and the absolutely convergent Euler series give $S(x,Y,0)\ge E(Y)$ for $x\ge X_L$ and $1<Y\le5$. The series shows that $E$ increases in $Y$. For a cell $[l,r]$ the floor is $E(l)$, or $(l/p)E(p)$ for a reference $r\le p\le5$ with $E(p)>0$. The latter is checked using the quadratic for $K_Y/Y-K_p/p$ in Appendix A. At $Y=l$, $b=1$, the test is
$$
c=l^2+p^2-6\ge0\quad\text{or}\quad
4(l^2-1)(p^2-1)\ge c^2 .
$$

The polynomial increases in $Y^2$ for $Y\le p$ and decreases in $b^2$ for $b\le1$. Thus the test covers the whole cell. The 2,000 adjacent initial cells compare the floor to $f(r,0)$.

For the bottom comparison, convolve the kernels of §2 in their horizontal variable. With
$\eta_Y(a)=\operatorname{sech}(\pi a/(2Y))/(2Y)$, the Fourier transforms
$\widehat P_v=\pi e^{-v|\xi|}$ and $\widehat\eta_Y=\operatorname{sech}(Y\xi)$
give $\eta_Y*K_p=2P_p$ on the two edges $b=\pm Y$. If $p\ge2Y$,
then $(2Y/p)P_p\le P_{2Y}$ there. Restrict the convolution to
$|a|\le5000$, and continue the inequality inside by the harmonic
minimum principle. The omitted edge pole is nonnegative and the
difference tends to zero at horizontal infinity. Summation gives
$$
 S(x,Y,t)\ge \frac{Y}{p}\int_{-5000}^{5000}\eta_Y(a)S(x+a,p,t)\,da .
$$
The retained mass exceeds $m=1-10^{-40}$ for $Y\le1.001$, since the discarded mass is bounded by $(4/\pi)e^{-5000\pi/(2Y)}$.
The checker verifies $p\le5,\ p^2>4q_M(t_l)$ and
$s=\phi(p,t_l)-\delta(t_r)>0$ on each old-wall cell $[t_l,t_r]$.
For $x\ge X-87000$ the translates satisfy $x+a\ge X-92000$.
Writing $h_l=\sqrt{q_M(t_l)}$, $h_r=\sqrt{q_M(t_r)}$, a bottom
floor valid as $Y\downarrow\sqrt{q_M(t)}$ is
$$
 \max\{m h_rs/p,\ \phi(h_r,t_l)-\delta(t_r)\}.
$$
The strict separation $p^2>4q_M(t_l)$ gives a neighborhood above
the wall. Both adjacent cells give the bottom liminf at a knot up to
the certified prefix, including limits with moving $x,Y,t$.

For every positive mixture $V$, $f=V_Y/V$ is nondecreasing in
$Y,t$, solves $f_t=f_{YY}+2ff_Y$, and $0\le f_Y\le6.55^2$.
The monotonicities follow from the slope variance and the covariance
of $\lambda\tanh(\lambda Y)$ with $\lambda^2$. Compare with
$F=f-\delta-g$ on $x\ge X-87000,\ \sqrt{q_M(t)}<Y\le5$, where
$g=10e^{86t}\chi((X-80000+40000t-x)/7000)$, and $\chi$ is a
smooth monotone cutoff rising from 0 to 1 on $[0,1]$. Its transition
lies inside $[X-87000,X-72000]$. With $S_t=S_{YY}-2AS_x+2SS_Y$,
the residual of $F$ is $(90-2f_Y)\delta+(86-2f_Y)g+ (40000-2A)|g_x|>0$. The transition lies in the domain of the bound $|A|<16000$ in Appendix A.4. The left edge uses $g\ge10$ and positivity of $S$, and the top uses $S>6.59$. The initial cells and the moving-bottom floors give strict margins against $f(r,0)$ and $f(h_l,t_r)$, respectively. At infinity, (A.16) gives $S(x,Y,t)\ge(Y/5)S(x,5,t)$ for $h_M<Y<5$, since $Y^2+25\ge6h_M^2$. The stationary comparison in Appendix A.5 gives the top floor. For uniform growth use Appendix A.4 at height five on all of $[0,T_M]$, then transfer down by the same kernel inequality. Thus a first contact from above is interior at
positive time and contradicts the residual. This certifies
$S\ge f-\delta$ on $x\ge X-72000$ through each of the 34 original
prefixes. The original profile $f_0$ is active through $T_M$.

## 5. Arithmetic lower bound for the averaged field

For a central abscissa $x\ge X-90000$ and height $Y$, take a probability measure $\nu$ on $[-12,12]$, define $\bar S_\nu=\int S(x+d,Y,t)\,d\nu(d)$ and $\widehat\nu(\xi)=\int e^{id\xi}\,d\nu(d)$. The witness uses the average of the two point masses at displacements $\pm ah$. The equations in this section carry the prefix E.

### Time zero

For $1<Y\le5$ set $\sigma=(1+Y)/2$.
The absolutely convergent logarithmic Euler series and the gamma bound
give
$$
\bar S_\nu(x,Y,0)\ \ge\
\Omega(x)-10^{-10}
-\frac12\sum_{n\ge2}\Lambda(n)n^{-\sigma}
                  |\widehat\nu(\log n/2)|.
\tag{E.1}
$$
Here $H_0(z)=G(w)\zeta(w)$, $w=(1-iz)/2$, and
$G(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16$. At time zero the gamma error
about $\Omega(x)$ is at most $16/(x-12)+12/(4(x-12))$. Each averaged
Dirichlet term carries the same central phase $e^{ix\log n/2}$ times
$\widehat\nu(\log n/2)$. Absolute convergence justifies the averaging.
For a symmetric pair with physical displacements $\pm d_0$ the multiplier is $\cos(d_0\log n/2)$.

### Finite Gaussian approximation

Take $r=3/40$, $x_* = X-90012$, $Q_* = x_* /(4\pi)-1$, and
$\alpha_*=\frac12\log Q_*-32/x_*$. For each probe center
$x_0=x+d\ge x_*$ use the closed disk of radius $r$ about $x_0+iY$,
with $Y+r\le5$ and $Y-r>1$. Define, at points of the disk,
$$
 a(w)=G'(w)/G(w),\quad s=w+\tfrac t2a(w),\quad
 B=G(w)e^{t a(w)^2/4},\quad F=H_t/B,\quad
 P_N=\sum_{n\le N}c_n(t)n^{-s},\quad
 c_n(t)=e^{t\log^2(n)/4}.
$$
The integer $N=\lfloor Q\rfloor$, $Q=x_0/(4\pi)$, is fixed on the
disk, and $L=\log Q$. The Euler summation cutoff here is of order
$x_0/(4\pi)$. Polymath's shorter finite sums come from a different
approximation. The direct calculation below uses the Gaussian identity
and exact functional equation.

Let $v=\Im z$, $\sigma_z=(1+v)/2$, and $\alpha+i\beta=a(w)$.
Throughout the disk the gamma estimates give
$$
 |\alpha-L/2|\le32/x_0,\qquad |\beta|<0.8,\qquad
 |a'(w)|<2/x_0,\qquad
 G(w+R)=G(w)e^{a(w)R+E(R)},\quad |E(R)|\le R^2/x_0
$$
for $R\ge-v/2$. The estimates apply here by the same segments as in
the source, since $|w+ix_0/2|<4$ and $\Re(w+R)\ge1/2$.
In particular $\alpha\ge\alpha_*>0$. For $0<t\le1/5$, the Gaussian
density is $\rho_t(R)=e^{-R^2/t}/\sqrt{\pi t}$. In the exact
displacement integral, folding $R<-v/2$ with the functional equation
replaces that portion by the conjugated completed zeta at $w+R$,
$R\ge-v/2$, with density $\rho_t(-v-R)$.
The displacement identity follows by Fubini against the Fourier kernel,
using its double exponential decay to integrate the majorant with
$e^{t u^2+|v|u}$.

On $R\ge-v/2$, one-step Euler summation gives
$$
\left|\zeta(w+R)-\sum_{n\le N}n^{-w-R}\right|
\le14N^{1-\sigma_z-R}.
\tag{E.2}
$$
Indeed the two factors after extracting $N^{1-\Re(w+R)}$ are
at most $2/(x_0-1)$ and $(x_0+2)/N$, respectively, using
$\Re(w+R)\ge1/2$ and $|\Im w|\le(x_0+1)/2$.
Their sum is below 14 at $x_*$ with $N$ replaced by $Q-1$, and
this upper bound decreases. Thus $|\zeta(w+R)|\le16\sqrt N$
on this half-line. The integral of the linearized gamma factor times
the finite sum over the entire line equals $B P_N$ by Gaussian
moments. The calculation never integrates an infinite Dirichlet series.
For $t>0$ the terms $c_n(t)n^{-s}$ even fail to tend to zero at
fixed $s$.

To bound the four errors, put $b=1+10^{-9}$.
Completing squares in each unreflected modulus gives a common
factor $e^{t\beta^2/4}<1.04$. The heat weight
$\exp[t\log n(\log n-2\alpha)/4]$ is at most $b$ for $n\le N$
because $2\alpha\ge L-64/x_0$. The resulting real Gaussian has
variance $t/2$ and mean $\mu_n=t(\alpha-\log n)/2$ with
$|\mu_n|\le t(L+1)/4$. If a Gaussian has this variance and a mean
with the same upper bound, then for $k=1,2$,
$$
 \mathbb E e^{kR^2/x_0}
 \le (1-kt/x_0)^{-1/2}
     \exp\!\left(\frac{k t^2(L+1)^2}{16 x_0(1-kt/x_0)}\right)
 <1+10^{-11}.
\tag{E.3}
$$
The upper bound is increasing in $t$ and decreasing in $x_0$
on this range. The scalar checks at $x_*,t=1/5$ are in the checker.

1. **Euler summation.** The remainder (E.2) gives at most
   $1.04\cdot14 b^2 N^{1-\sigma_z}$ by the Gaussian for $n=N$
   and (E.3) with $k=1$.
2. **Gamma variation.** For the finite sum on $R\ge-v/2$,
   $|e^{E(R)}-1|\le e^{R^2/x_0}-1$. After completing squares the
   error is at most
   $1.04 b\,10^{-11}(1+1/(\sigma_z-1))$.
3. **Omitted part of the model integral.** On $R<-v/2$,
   $\sum_{n\le N} n^{-\sigma_z-R} \le2\sqrt N\,N^{-v/2-R}=2N^{1-\sigma_z-R}$.
   The Gaussian at $n=N$ then gives at most
   $1.04\cdot2 b N^{1-\sigma_z}$.
4. **Reflection.** Bound the reflected zeta by $16\sqrt N$ and
   substitute $U=-v-R$. After completing squares with tilt
   $-\alpha$ and extending the positive majorant to all $U$, its
   bound is $1.04\cdot16\sqrt N\, e^{-v\alpha} \mathbb E e^{(v+U)^2/x_0}$, with mean $-t\alpha/2$.
   Use $(v+U)^2\le2v^2+2U^2$ and (E.3) to bound the expectation
   by $b^2$. Also $\sqrt N\,e^{-v\alpha}\le b Q^{1-\sigma_z}$.

Combining the four terms gives, with any $1<\tau\le\sigma_z$,
$$
 |F-P_N|\le {\cal E}(\tau)
 =34 Q_*^{1-\tau}+10^{-10}\left(1+\frac1{\tau-1}\right).
\tag{E.4}
$$
Continuity gives the same estimate at $t=0$.
Use $\epsilon_0={\cal E}(\sigma)$ at the center and
$\epsilon_r={\cal E}(\sigma-r/2)$ on the disk. The holomorphic
difference with this fixed $N$ gives
$|(F-P_N)_z|\le \epsilon_r/r$ and
$|(F-P_N)_{zz}|\le2\epsilon_r/r^2$ at the center by Cauchy's formula.
No differentiation of the cutoff or of the split integral is needed.

### Logarithmic factor and graded tail

Treat $n^{-s}$ as formal monomials under integer multiplication. Let
$L=\log(\sum_{n\ge1}c_n n^{-s})=\sum_{n\ge2}l_n n^{-s}$ in this
formal ring. For the operator $D(n^{-s})=(\log n)n^{-s}$, coefficient
comparison in $D(e^L)=e^L DL$ gives the finite recurrence used in the
checker. The formal heat equation $4\partial_t e^L=D^2 e^L$ gives
$$
 4\dot l_n=(\log n)^2l_n
       +\sum_{uv=n,\ u,v\ge2}(\log u)(\log v)l_u l_v.
$$
The Euler initial coefficients $l_n(0)=\Lambda(n)/\log n$ are
nonnegative. By induction and variation of constants, $l_n$ are
nonnegative and nondecreasing. All operations at a given index are
finite. With $L_M=\sum_{2\le n\le M}l_n n^{-s}$ and
$e^{L_M}=\sum_{n\ge1} e_n n^{-s}$, coefficients satisfy
$0\le e_n\le c_n$ and equality holds for $n\le M$.
The finite exponential has an absolutely convergent Dirichlet expansion
at every fixed real part, including all log moments used here.

Let $q_0(t)=\sigma+t\alpha_*/2$ at a disk center, and set $J=\lfloor Q_*\rfloor\le N$. For $j\ge0$, let $T_j$ be the absolute
coefficient $j$-th log moment of $P_N-e^{L_M}$ at $\Re s$.
Splitting at $J$, using
$c_n(t)n^{-\Re s}\le b n^{-\sigma}$ for $n\le N$, gives the bound
$$
 T_j\ \le\
 \sum_{n\le J}c_n n^{-q_0(t)}(\log n)^j
 -D^j e^{L_M}(q_0(t))
 +2\sum_{n>J}e_n n^{-q_0(t)}(\log n)^j
 +b\sum_{n>J}n^{-\sigma}(\log n)^j.
\tag{E.5}
$$
Here the right side is a permissible choice of $D_j$.
For $n\le J$ the discrepancy is nonnegative and decreases on raising
the real part from $q_0(t)$. For $n>J$ one copy of the exponential
tail pays for completing the subtraction. The second pays for the
terms $n>N$ of the exponential outside $P_N$.
The exponential tail is bounded by $Q_*^{-1/2}D^j e^{L_M}(q_0(t)-1/2)$
since $n>J$ implies $n>Q_*$.

On a time cell $[t_l,t_r]$, put $q_l=q_0(t_l)$, $q_r=q_0(t_r)$.
For the subtracted expression in (E.5) use $l_n(t_l)$ and real part
$q_r$. For its tail upper bound use $l_n(t_r)$ and real part
$q_l-1/2$. The sum of $c_n n^{-q_0(t)}(\log n)^j$ for
$n\le K$, $K=16384$, is upper bounded at $t_l$, since
$\log K<2\alpha_*$. The remaining raw terms in (E.5) are bounded by
integrating $b u^{-\sigma}(\log u)^j$. On each interval $(A,B]$
with $K\le A<B<Q_*$, the weight can be reduced by
$\exp[-t_l(\log Q_*-\log B)\log A/4]$. The code uses breakpoints at
$10^6,10^8,10^{10}$, and then the unreduced integral to infinity.
For $j=0,1,2$ the integrands decrease throughout these intervals.
The integral from $A$ to infinity for $j=0$ is
$I_0=A^{1-\sigma}/(\sigma-1)$. The next two are
$I_1=I_0(\log A+1/(\sigma-1))$ and
$I_2=I_0((\log A)^2+2\log A/(\sigma-1)+2/(\sigma-1)^2)$.

### Division and averaging

Take $M=4096$ and $V_j=\sum_{n\le M}l_n(t_r)n^{-q_l}(\log n)^j$
with the sum starting at $n=2$. For all centers on the row,
$e^{-V_0}\le|e^{L_M}|$, and thus
$$
 d_*=e^{-V_0}-D_0-\epsilon_0\ \le |F|.
$$
The criterion $d_*>0$ is checked before division. It is uniform in
$x$ and gives nonvanishing at every displaced center. With
$W=F-e^{L_M}$, $\kappa=0.500000001$, and
$|s_z|\le\kappa$, one has
$$
 \left|F_z/F-(L_M)_z\right|
 =\left|(W_z-(L_M)_z W)/F\right|
 \le {\cal D}
 :=\frac{\epsilon_r/r+\kappa[D_1+V_1(\epsilon_0+D_0)]}{d_*}.
\tag{E.6}
$$
The archimedean term satisfies
$-\Im(B_z/B)\ge\Omega(x_*)-10^{-10}$. Its explicit derivative is
$B_z/B=-i[a+(t/2)aa']/2$. The nonconstant prefactor
$1+(t/2)a'(w)$ in $(L_M)_z$ costs at most $10^{-10}V_1$
in the field. Freeze $a(w)$ at the central $x$ for the remaining
phase calculation. Along the horizontal segment from $x$ to $x+d$,
$$
 |s(x+d+iY)-s(x+iY)+id/2|
 \le\frac{t|d|}{2(x_*-1)}.
$$
Both the true and frozen $s$ have real part at least $q_l$.
Integration along their straight segment bounds the variation of
$DL_M$ by $t|d|V_2/[2(x_*-1)]$. Writing
$a_\nu=\sup_{d\in{\rm supp}\,\nu}|d|$, the uniform result is
$$
\begin{split}
\bar S_\nu(x,Y,t) \ \ge\ &\Omega(x_*)-10^{-10}-{\cal D}
 -10^{-10}V_1-\frac{t_r a_\nu V_2}{4(x_*-1)}\\
 &-\frac12\sum_{2\le n\le M}(\log n)l_n(t_r)n^{-q_l}
                  |\widehat\nu(\log n/2)|.
\end{split}
\tag{E.7}
$$

## 6. Whole-row contraction

At a possible contact, reflection and the finite-head result give
$x>X$. When a row has exponent $k>0$, put $B=10^k$ and
$C=5.558691$ (the verifier also supports $C=6$). Appendix C gives the initial square bound $q_0=(1-2/(C\log B))^2$ for $|x|\le2B$. The weighted trace yields $y^2<q_0-2t+10^{-9}$ for $|x|\le B$ and $0\le t\le1/100$. The checker compares
both endpoints of $q_b+2t$ strictly against the same interval
intercept and checks $t_R\le1/100$. Thus every such contact has
$x>B$ throughout that closed row.

For a row $[t_L,t_R]$, choose rational $h_-\le\sqrt{q_R}$ and
$h_+\ge\sqrt{q_L}$ on the $10^{-14}$ grid. Each probe uses
$Y_j=r_jh,\ d_j=a_jh,\ c_j=w_j/r_j$ at contact height $h$.
The tests $r_j>1,\ a_j\ge0,\ 0<w_j\le1,\ (r_jh_-)^2>q_M(t_L)$,
$r_jh_+\le5$ and $a_jh_+\le72000$ cover both translated
centers on the entire row. A positive-profile floor for their average
is $f(r_jh_-,t_L)-\delta(t_R)$ with prefix end $\ge t_R$.

Euler candidates use $t_L<0.065,\ r_jh_-\ge1.5,\ r_jh_++3/40\le5$,
$a_jh_+\le12$. Use $x_*=X-90012$ in the disk and graded tail
estimates, with $\sigma=(1+r_jh_-)/2$ and disk radius $3/40$.
The disk stays above $\sigma=1$. The Euler summation factors are
bounded by $2/(x_*-1)+(x_*+2)/(x_* /(4\pi)-1)<14$, even with
horizontal displacement. The gamma and Gaussian scalar bounds of §5
hold at this cutoff and are checked anew. Before the common $10^{-10}$ debit, the archimedean term uses
$\Omega(x_*)$ on near rows or $\Omega(B-12)$ on far rows, where
$\Omega(x)=\log(x/(4\pi))/4$; both displaced centers lie beyond the
respective cutoff. All remaining debits use the common $x_*$.
With the notation of §5, division uses only the strictly positive
Euler approximation bound $e^{-V_0}-D_0-\epsilon_0$. The independent
probe floor uses the absolute cosine debit in (E.7).

For a subset of eligible probes, freeze $G'/G$ at height 2 at
the common horizontal center $x$. Keeping the elementary
translations exactly, the extra debit for probe $j$, including its
horizontal freeze, is at most
$t_R(a_jh_+ + \sup |Y_j-2|)V_{2,j}/[4(x_*-1)]$ in the probe
field before weighting. This follows from $|(G'/G)'|<2/(x_*-1)$
on the two segments and $|(DL_M)'|\le V_{2,j}$ on the connecting
segment in the Dirichlet argument. Its real part stays above the
lower real-part cutoff because the elementary displacement is held
exactly and both frozen and actual gamma real parts are bounded
below by $\alpha_*=\tfrac12\log(x_* /(4\pi)-1)-32/x_*$.
The short head $2\le n\le64$ now has coefficient
$$
 b_n=\frac{(\log n)l_n(t)n^{-t\alpha_*/2}}2
 \sum_{j\ {\rm in\ subset}}c_j n^{-(1+r_jh)/2}
             \cos(a_jh\log n/2).
$$
For the variation in $h$ the verifier encloses the sum at the
midpoint and the derivative of the sum on the same whole height
interval. Monotonicity of $l_n$ and of the common damping gives
the remaining time enclosure. The common factor is
$z_n=n^{-t(\alpha-\alpha_*)/2}e^{i(x-t\beta)\log n/2}$ with
$\alpha+i\beta=G'/G((3-ix)/2)$. Then $|z_p|\le1$ and
$z_{p^m}=z_p^m$. The harmonic maximum principle for the real part of the prime-power polynomial reduces its maximum to the unit circle. The coefficients are real, so cosine symmetry restricts the angles to $[0,\pi]$. The cosine samples at
$j\pi/128,\ 0\le j\le128$, plus
$(\pi/128)^2\sum_m m^2|b_{p^m}|/8$, bound its maximum by the
linear interpolation error. Mixed terms through 64 use
$|b_n|$; terms above 64 use the separate absolute debits.
The final field floor $L$ is the weighted sum of the best separate
floors with the largest certified positive subset increment, or
the separate floor alone. The weighted floor is checked positive.

The exact Bernstein gate proves the translated kernel inequality
$K_h\ge\sum_j c_j(K_{Y_j}(d-d_j,b)+K_{Y_j}(d+d_j,b))/2$.
It clears positive denominators on the edges and checks the compactified
half-line, then uses harmonic continuation. Apply this inequality to
all pairs other than the touching pair. Set
$B_j=\sum_{v=r_j\pm1}v/(v^2+a_j^2)$. Its contribution to either
translated field is $B_j/h$. The velocity identity at a simple
contact gives $(h^2)'\le-2-4(h L-\sum_j c_j B_j)$, including
the $-2$ from the touching conjugate. The row verifies
$$
 \frac{q_L-q_R}{t_R-t_L}<
 2+4\left(\sqrt{q_R}L-\sum_j c_j B_j\right).
$$

## 7. Closing the comparison

Start at $q_b(0)=q_{\rm start}>1$. If $\sigma_1$ is the first row speed, take $\tau=\tfrac12\min(t_1,(q_{\rm start}-1)/\sigma_1)$, where $t_1$ is the first knot. The checker verifies $q_b(\tau)>1$, so the classical strip excludes contacts through $\tau$. On $[\tau,T]$, where $T$ is the terminal time, [1, Theorem 1.5(i)] gives a single finite bound on the real parts of all nonreal zeros, by taking $R=\exp(C/\tau)$ and using symmetry. Since $q_b\ge1/400$, any zero reaching the barrier lies in a compact set with $|\Im z|\ge1/20$. Continuity of $H_t$ gives a first time $t_*$ of reaching or exceeding the barrier if a failure occurs. Local persistence of zeros, or Rouché's theorem on a small circle, rules out strict exceedance at the first time. Thus all zeros are in the closed strip at $t_*$ and a highest zero touches its edge. Several touching zeros at distinct locations are allowed in (3)–(5).

A multiple contact is impossible. If $H_{t_*}$ vanishes to order $m\ge2$ at $z_*=x+ih$, expand $H_{t_*-\varepsilon}(z_*+\sqrt{\varepsilon}\,w)$ using $\partial_t=-\partial_z^2$. If the leading Taylor coefficient of $H_{t_*}$ is $c\ne0$, then locally uniformly in $w$
$$
\varepsilon^{-m/2}H_{t_*-\varepsilon}(z_*+\sqrt{\varepsilon}\,w)
=c(i\sqrt{2})^m\operatorname{He}_m(w/(i\sqrt{2}))+O(\sqrt{\varepsilon}).
$$

Indeed the leading heat Taylor terms are $c\sum_{k=0}^{\lfloor m/2\rfloor}m!w^{m-2k}/(k!(m-2k)!)$. The probabilists' Hermite polynomial $\operatorname{He}_m$ has real simple roots, including a positive one for $m\ge2$. Local perturbation at that simple scaled root gives an earlier zero of imaginary part $h+c_*\sqrt{\varepsilon}+O(\varepsilon)$, where $c_*>0$. The barrier height changes by $O(\varepsilon)$, a contradiction to first contact.

At a simple touching zero the differentiable branch has squared height strictly below $q_b$ at earlier times and equal to it at $t_*$, so the difference has nonnegative left derivative there. The row speed test gives a strictly negative left derivative. At a knot, use the row on its left, which is certified up to its closed right endpoint. This excludes contact through $T$.

This also covers the far-to-near join and the terminal knot.

## 8. Numerical result and comparison

The 2,286-row certificate ends at $T=147642417023/10^{12}$ and $q_b(T)=1/400$. The strip theorem [1, Theorem 3.2] gives $\Lambda\le T+1/800$. The first 46 rows use the local strip and end at $514804209/10^{12}$. The replay selects a shared arithmetic floor on 1,299 rows. The minimum strict speed margin exceeds $2\cdot10^{-6}$.

The supplement includes a SHA-256 manifest, the frozen rational witness, the numerical verifier, and replay receipts. Run `bash replay.sh` in the extracted directory with Python and the pinned python-flint dependency installed. The checker recomputes each decision with exact rational arithmetic or Arb enclosures. For the inherited wall, the compact data reconstruct the exact ordered source intervals, including the one bottom cell per height row. A provenance check compares them against Gordon's two pinned original files. Every zeta floor is evaluated anew via the Taylor coefficients $\zeta(\sigma)$ and $\zeta'(\sigma)$ at real $\sigma>1$.

The complete source replay and the standalone replay are author checks. The older bound $0.153110450565$ had an external replay of its kernel and speed tests and an inspection of its spatial margin. That replay concerns the older witness [6]. Independent review of the weighted propagation arguments, elementary field estimates, and present 2,286-row witness remains open.

Platt–Trudgian's published upper bound is $0.2$ [2, Corollary 2]. Gordon [4] reports approximately $0.157656619095$. Planat and Raymond [7] report a ceiling below $0.156821$ in a preprint. An earlier 2,286-row calculation gave $0.149060787205$ conditional on Gordon's effective field, spatial density and jet estimates. Planat [8] reports a stronger conditional ceiling below $0.148612$ using model-to-function, localization and global contact premises. The present result has the dependency chain specified in §1.

## Appendix A. Elementary top and old-wall input

Throughout this appendix write $u=H_t'/H_t$, $A=\Re u$, $S=-\Im u$ and $\Omega(x)=\tfrac14\log(x/(4\pi))$. All decimal constants are exact rationals. The scalar inequalities are checked in `check_top.py` and `check_old_wall.py`. The latter reconstructs Gordon's pinned intervals and recomputes the inequalities in Appendix A.6. In A.6 the density argument holds on $x\ge X_L$ with the full penalty. It gives the unpenalized conclusion everywhere that penalty vanishes, in particular for $x\ge X-92000$.

### A.1 Exact Gaussian displacement

Equation numbers in this appendix carry the prefix A.

Fix a real center $x\ge X_e$ and a disk $|z-(x+iY_c)|\le1$, with
$Y_c=50$ or $5$. At its points let $Y=\Im z$,
$w=(1-iz)/2=\sigma-iT$, $L=\log(x/(4\pi))$, and
$$
G(s)=\frac{s(s-1)}{16}\pi^{-s/2}\Gamma(s/2),\qquad
a(s)=G'(s)/G(s),\qquad
B_t(z)=G(w)e^{t a(w)^2/4}.
$$
The Fourier definition, the Gaussian moment identity, and Fubini give
$$
H_t(z)=\int_{\mathbb R}\rho_t(R)\,G(w+R)\zeta(w+R)\,dR,\qquad
\rho_t(R)=\frac{e^{-R^2/t}}{\sqrt{\pi t}}\quad(t>0).
\tag{A.1}
$$
Indeed $G(s)\zeta(s)=\xi(s)/8$, and displacing $z$ to $z+2iR$
displaces $w$ to $w+R$. The integrated absolute Fourier majorant is a
constant times $\int_0^\infty\Phi(v)e^{t v^2+|Y|v}\,dv$, finite by the
double exponential decay of $\Phi$. At $t=0$ the measure is a point
mass at zero. For $R<-Y/2$, the functional equation and conjugation
give $\xi(w+R)=\overline{\xi(w-Y-R)}$. Thus (A.1) equals
$$
\int_{-Y/2}^{\infty}
\left\{\rho_t(R)G(w+R)\zeta(w+R)
 +\rho_t(-Y-R)\overline{G(w+R)\zeta(w+R)}\right\}\,dR.
\tag{A.2}
$$
The reflected density divided by the original one is
$e^{-Y(Y+2R)/t}\le1$ on this half-line.

### A.2 Gamma estimates on the whole half-line

Throughout the disks, $(x-1)/2\le T\le(x+1)/2$.
For $q$ in the right half-plane with $V=|\Im q|>0$, Euler–Maclaurin
with the periodic second Bernoulli polynomial gives
$$
\log\Gamma(q)=(q-\tfrac12)\operatorname{Log} q-q+\tfrac12\log(2\pi)
 +\frac1{12q}-\frac12\int_0^\infty\frac{B_2(\{v\})}{(q+v)^2}\,dv.
$$
Differentiating the locally uniformly convergent integral and using
$|B_2|\le1/6$ and $\int_0^\infty(v^2+V^2)^{-3/2}\,dv=V^{-2}$
yields $|\psi(q)-\operatorname{Log} q+1/(2q)|\le1/(4V^2)$. Also the trigamma
series, dominated by a decreasing integral, gives
$$
|\psi'(q)|\le\sum_{n=0}^\infty(n^2+V^2)^{-1}
 \le V^{-2}+\pi/(2V).
$$
With $q=s/2$, these imply
$$
\begin{aligned}
\left|a(s)-\tfrac12\operatorname{Log}(s/(2\pi))-\tfrac1{2s}-\tfrac1{s-1}\right|
    &\le 1/(2T^2),\\
|a'(s)|&\le 3/T^2+\pi/(4T)<2/x
\end{aligned}
\tag{A.3}
$$
for all $s$ with $\Re s\ge1/2$ and $\Im s=-T$. In particular,
for every $R\ge-Y/2$, including arbitrarily large $R$,
$$
G(w+R)=G(w)e^{a(w)R+E(R)},\qquad |E(R)|\le R^2/x.
\tag{A.4}
$$
Here the difference of logarithms is taken along the segment, whose
entire real part is at least $1/2$. The Taylor remainder follows by
integrating (A.3) twice.

Set $a_0=L/2-i\pi/4$. Integrating the derivative of the principal
logarithm from $-ix/2$ to $w$, a segment of length at most $26$,
gives
$$
|a(w)-a_0|
 \le 29/(x-1)+2/(x-1)^2<32/x.
\tag{A.5}
$$
Write $a(w)=\alpha+i\beta$. We have $13<\alpha\le(L+1)/2$,
$|\beta|<0.8$, and $|a(w)|\le(L+2)/2$. With $a'=da/ds$ evaluated
at $w$,
$$
\frac{B_t'}{B_t}=-\frac{i a(w)}2-\frac{it a(w)a'(w)}4,\qquad
\left|\frac{B_t'}{B_t}+\frac{i a_0}{2}\right|
 \le \frac{16+(L+2)/20}{x}<10^{-10}.
\tag{A.6}
$$
The ratios $x/(x-1)$ and $x/(x-1)^2$ decrease on this range.
The last upper envelope in (A.6) decreases as well. The estimate (A.5)
also holds at $w=(1+Y-ix)/2$ for every $1<Y\le50$.

### A.3 Explicit disk bounds

Divide (A.2) by $B_t$ and compare to the exact integral of
$G(w)e^{a(w)R}$ over the whole real line. In absolute values the
resulting measure for that comparison is the law of a real Gaussian
of mean $\mu=t\alpha/2$ and variance $t/2$, multiplied by
$e^{t\beta^2/4}<1.04$. Write $\mathbb E_*$ for that Gaussian
expectation. Put
$$
D=1-t/x,\qquad D_*=1-t_m/x,\qquad
M=\mathbb E_*e^{R^2/x}=D^{-1/2}e^{\mu^2/(xD)},\qquad
M_* = D_*^{-1/2}\exp\!\left(\frac{(L+1)^2}{400xD_*}\right).
\tag{A.7}
$$
Then $M\le M_*$, and $M_*$ decreases on $x\ge X_e$.
For the exponent, $(L+1)^2/x$ decreases since $L>1$.

Take $d=12$ for $Y_c=50$ and $d=5/4$ for $Y_c=5$. For the
left portion $-Y/2\le R<-d$, the real part of $s=w+R$ lies in
$[1/2,26]$. With $N=\lceil x\rceil$, one-step Euler summation gives
$$
\left|\zeta(s)-\sum_{n\le N}n^{-s}\right|
 \le \frac{N^{1-\Re s}}{|s-1|}+\frac{|s|N^{-\Re s}}{\Re s}.
$$
The identity follows first for $\Re s>1$ by partial summation, with
remainder $-s\int_N^\infty\{v\}v^{-s-1}\,dv$, which continues to
$\Re s>0$. Since $|s|\le0.51x$, $|s-1|\ge0.49x$, and the finite
sum is bounded by $2\sqrt N$, this yields $|\zeta(s)|<5\sqrt x$.
The reflected density is at most the original one on this portion.
Including the omitted comparison integral for all $R<-d$, the left
contribution before the common factor $1.04$ is bounded by
$$
\begin{aligned}
 (1+10\sqrt x)\,\mathbb E_*[{\bf 1}_{R<-d}e^{R^2/x}]
 &\le \frac{11}{2\sqrt{D_*}}\,(4\pi)^{d/2}x^{(1-d)/2}
     \exp\!\left(\frac{32d}{x}-\frac{d^2D_*}{t_m}\right)
 =: T_d(x).
\end{aligned}
\tag{A.8}
$$
To see this, use $e^{\alpha R-t\alpha^2/4}\le e^{-d\alpha}$
against the untilted density. The remaining integral is bounded by
$D^{-1/2}\exp(-d^2D/t)/2$, by translating the Gaussian tail by $d$
and dropping its negative linear term. Finally use (A.5) for $\alpha$.
Every factor of $T_d$ that depends on $x$ decreases, since $d>1$.

On $R\ge-d$, the Taylor error in the unreflected term contributes at
most $M_*-1$, using $|e^{E(R)}-1|\le e^{R^2/x}-1$.
Let $Y_{\min}=Y_c-1$. Here $Y_{\min}>2d$ and the reflected
contribution is at most $M_* e^{-Y_{\min}(Y_{\min}-2d)/t_m}$
times an upper bound for $|\zeta|$ on the right portion.

For $Y_c=50$ that portion has $\Re s\ge13$. The series and integral
test give $|\zeta-1|\le b_{50}=2^{-13}+2^{-12}/12$ and $|\zeta|\le2$.
Thus
$$
\left|H_t/B_t-1\right|
\le 1.04\big[(M_*-1)+b_{50}M_*+T_{12}(x)+2M_*e^{-6125}\big]
<0.00016.
\tag{A.9}
$$

For $Y_c=5$ the right portion has $\Re s\ge5/4$, so
$|\zeta|\le5$. Let $b_5=\zeta(5/2)-1$. Log convexity of
$\zeta(v)-1$ on $v>1$ follows from Hölder's inequality on its
positive series. The scalar gate $\zeta(5/4)-1<b_5 e^{5/2}$
then gives $|\zeta(w+R)-1|\le b_5 e^{2(-R)_+}$ for $R\ge-5/4$.
For $v=-R>0$,
$(e^{2v}-1)e^{-\alpha v}\le 2v e^{-11v}\le2/(11e)$.
Integrating this extra term against the untilted Gaussian on one
half-line gives
$\mathbb E_*[e^{R^2/x}e^{2(-R)_+}]\le M_*+1/(11e\sqrt{D_*})$.
Consequently
$$
\left|H_t/B_t-1\right|
\le 1.04\big[(M_*-1)+b_5(M_*+1/(11e\sqrt{D_*}))
        +T_{5/4}(x)+5M_*e^{-30}\big]<0.38.
\tag{A.10}
$$
The bounds (A.9) and (A.10) are evaluated at $X_e$ using (A.7) and (A.8).
They hold at $t=0$ by continuity of (A.1) and $B_t$.

The ratio $H_t/B_t$ is holomorphic on a neighborhood of either
closed disk. If its difference from one is bounded by $\epsilon<1$,
Cauchy's formula on the unit circle gives, at the center,
$$
\left|u-\frac{B_t'}{B_t}\right|\le\frac{\epsilon}{1-\epsilon}.
\tag{A.11}
$$
Combining (A.6), (A.9), and (A.11) yields
$$
S(x,50,t)>\Omega(x)-0.0002>6.65\quad(x\ge X_e),
\qquad |u(x+50i,t)|<8\quad(X_e\le x\le X).
\tag{A.12}
$$
In particular $S(x,50,t)\to\infty$ uniformly for $0\le t\le t_m$.
Similarly (A.6), (A.10), and (A.11) give $|u(x+5i,t)|<10$ for
$X_e\le x\le X$. The finite modulus bounds use
$|a_0|/2\le\Omega(X)+\pi/8$.

### A.4 Positive real part and transfer from height 50

Use the classical strip $|\Im\rho|\le1$ for $t\ge0$ and the
paired Hadamard identity
$$
S(x,Y,t)=\sum_{\text{pairs}}K_Y(x-\Re\rho,|\Im\rho|),
\quad
K_Y(d,b)=\frac{2Y(d^2+Y^2-b^2)}
 {[d^2+(Y-b)^2][d^2+(Y+b)^2]}.
\tag{A.13}
$$
This identity holds away from zeros, with multiplicity and half-pair
weight for real zeros. The imaginary-part sum is absolutely convergent:
the sum of $|\rho|^{-2}$ converges, and the paired terms at large
$|\Re\rho|$ are $O(|\rho|^{-2})$ at each fixed $z$. In the Hadamard
logarithmic derivative, evenness cancels the linear exponential term
and conjugate pairing cancels the regularizing constants in the
imaginary part. There is at least one zero for each $t$ since $H_t$
is even, of order at most one, and nonconstant. These classical inputs
follow from the Fourier representation and de Bruijn's strip theorem.

In particular $p=iu$ is holomorphic with $\Re p=S>0$ on
$Y>1$. If the open disk of radius $r_0\le50$ about $x+50i$
has this positivity, the Cayley transform at its center and Schwarz's
lemma give, for $r=50-Y<r_0$ and $Y\le50$,
$$
\begin{aligned}
|A(x,Y,t)|&\le |A(x,50,t)|
            +\frac{r_0+r}{r_0-r} S(x,50,t),\\
S(x,Y,t)&\ge \frac{r_0-r}{r_0+r}S(x,50,t).
\end{aligned}
\tag{A.14}
$$
Indeed $q=(p-i\Im p(x+50i))/S(x,50,t)$ obeys
$|(q-1)/(q+1)|\le r/r_0$, which gives both bounds.

The disk with $r_0=49$ always works. On $X_L-2\cdot10^6\le x\le X_L$, (A.12) and (A.14) give $|A|<7840$ on $1.1\le Y\le50$.
The same disk gives $S(x,Y,t)\ge S(x,50,t)/979$ throughout
that height range for all $x\ge X_e$ and all $t\in[0,t_m]$.

By finite-head reality, the disk with $r_0=50$ works for $|x|\le X-51$:
its points have $Y>0$, and every nonreal zero is horizontally at
distance greater than $1$ by finite-head reality. Each kernel in (A.13) is positive,
as $b\le1$, and there are no zeros in the disk. For
$X_e\le x\le X-51$, this gives $|A(x,Y,t)|<16000$ on
$1/20\le Y\le5$, by inserting $r\le49.95$ in (A.14) and using (A.12).

For every $\tau>0$, Polymath's confinement gives a finite $R_\tau$
outside which all zeros are real for $\tau\le t\le t_m$.
One may take $R_\tau=\exp(C/\tau)$ from the published theorem
and evenness. Thus the $r_0=50$ disk also works for
$x\ge R_\tau+51$ and those times, by (A.13) and $b\le1$.
It gives $S(x,Y,t)\ge S(x,50,t)/1999$ for $1/20\le Y\le50$.
Together with (A.12) this proves uniform divergence to $+\infty$
on that band for every $[\tau,t_m]$. For any $0<\eta\le49$,
the $r_0=49$ disk gives the all-time divergence on
$[1+\eta,50]$, with Harnack factor at least $\eta/(98-\eta)$.

### A.5 Stationary comparison down to height five

Set $x_\ell=X_L-2\cdot10^6$, $f(Y)=6.62\tanh(0.82(Y-1.1))$,
and $\delta(t)=10^{-7}e^{12t}$.
The initial estimate follows from (A.5) and the absolutely convergent
Euler series at $t=0$. For $x\ge x_\ell$ and $1<Y\le50$,
$$
S(x,Y,0)>E(Y):=\Omega(x_\ell)-10^{-6}
      +\frac{\zeta'((1+Y)/2)}{2\zeta((1+Y)/2)}.
\tag{A.15}
$$
Here $\Re a/2\ge\Omega(x)-16/x$, and the Euler series bounds the
real part of $\zeta'/\zeta(w)$ below by its value at $\Re w$.
Indeed, $-\zeta'/\zeta(w)=\sum_{n\ge2}\Lambda(n)n^{-w}$, with nonnegative von Mangoldt coefficients. The series converges absolutely for $\Re w>1$, and local uniform differentiation gives $E'(Y)=\frac14\sum_{n\ge2}\Lambda(n)\log(n)n^{-(1+Y)/2}>0$. On $[1.25,6]$, the scalar checker proves
$E(Y)>f(Y)$ by comparing $E$ at the left endpoint and $f$
at the right endpoint of each interval of length $1/100$.
On $[6,50]$ it uses $E(6)>6.62$.

For $b<u<v$, clearing the positive denominators shows
that $K_u(d,b)/u\ge K_v(d,b)/v$ if
$$
D^2+(u^2+v^2-6b^2)D+(u^2-b^2)(v^2-b^2)\ge0,
\qquad D=d^2.
\tag{A.16}
$$
In fact this polynomial, multiplied by $2(v^2-u^2)$, is the
numerator of the kernel difference. For $1.1\le Y\le1.25$
take $u=Y,\ v=3,\ b\le1$; every coefficient is nonnegative.
Summing (A.13) gives $S(x,Y,0)\ge(Y/3)S(x,3,0)>f(Y)$ by
$(1.1/3)E(3)>f(1.25)$.

Let $\chi$ be any smooth nondecreasing function, zero on
$(-\infty,0]$, one on $[1,\infty)$, and set
$$
g(x,t)=10e^{12t}\chi((X_L-100000+40000t-x)/900000),
\qquad F=f-\delta-g.
$$
The transition where $g_x\ne0$ is contained in
$[X_L-10^6,X_L-92000]$, and $g_t=12g+40000|g_x|$.
Thus (A.14) gives $|A|<20000$ wherever $g_x\ne0$.
The backward heat equation $\partial_t H_t=-\partial_z^2 H_t$ and
the Cauchy–Riemann equations yield
$$
S_t=S_{YY}-2A S_x+2S S_Y.
\tag{A.17}
$$
Here $f'\ge0$, $f'\le6.62\cdot0.82<6$, and
$f''+2ff'=2(1-0.82/6.62)ff'\ge0$.
The residual is strictly positive on $x\ge x_\ell,\ 1.1\le Y\le50$:
$$
F_{YY}-2AF_x+2FF_Y-F_t
= f''+2ff'+(12-2f')(\delta+g)
      +(40000-2A)|g_x|>0.
\tag{A.18}
$$
The lower boundary has $F<0<S$, the left boundary has
$g\ge10$, and the top boundary has $F<6.62<S$ by (A.12).
At spatial infinity (A.12) and (A.14) give a uniform strict boundary
since $F\le6.62$. The initial comparison is strict by (A.15)–(A.16).
Consequently, if $S-F$ reaches zero, a first zero occurs on a
compact rectangle at positive time and in the spatial interior.
There $S_x=F_x,\ S_Y=F_Y,\ S_{YY}\ge F_{YY}$, and the
left time derivative of $S-F$ is nonpositive. Equations
(A.17)–(A.18) give the opposite sign. Hence $S>F$ on the whole
domain. As $g=0$ for $x\ge X_L$, the scalar gate
$f(5)-10^{-7}e^{12t_m}>6.59$ proves
$$
S(x,5,t)>6.59\qquad(x\ge X_L,\ 0\le t\le t_m).
\tag{A.19}
$$

### A.6 Application to the original density comparison

Keep Gordon's decreasing piecewise affine squared-height wall $q_M$
on $[0,T_M]$, with $h(t)=\sqrt{q_M(t)}$. Use the same profile
$$
\begin{aligned}
U(Y,t)&=10^9+\sum_{j=1}^3 a_j e^{\lambda_j^2t}\cosh(\lambda_jY),&
\phi&=U_Y/U,\\
(a_1,a_2,a_3)&=(1758974,2464729,302096),&
(\lambda_1,\lambda_2,\lambda_3)&=(19/4,97/20,131/20).
\end{aligned}
$$
The weighted proof in Appendix B supplies reality on $|\Re z|\le X$ throughout $[0,1/5]$. The finite inputs to this comparison are the initial, bottom and height-row data from Gordon [5], with the following gates recomputed locally.

Let $\Delta=10^{-14}e^{90t}$ and use the original cutoff
$$
g_M(x,t)=10e^{86t}\chi((X-100000+40000t-x)/900000),
\qquad F_M=\phi-\Delta-g_M .
$$
Since $U_t=U_{YY}$, $\phi_t=\phi_{YY}+2\phi\phi_Y$.
In the exponential representation of $U$, $\phi$ is the mean
of the slopes $0,\pm\lambda_j$ and $\phi_Y$ is their variance.
Thus $0<\phi<6.55$ for $Y>0$ and $0<\phi_Y\le 6.55^2$.
At fixed $Y>0$, $\phi_t\ge0$ because it is the covariance of
$\lambda\tanh(\lambda Y)$ with $\lambda^2$ under the normalized
cosh weights, both increasing in $\lambda\ge0$.

Where $(g_M)_x\ne0$, $x$ lies in $[X_L,X-92000]$. Appendix A.4 with the finite-head result gives $|A|<16000$ there on $h(t)<Y\le5$, since
$h(t)\ge1/20$. Using $(g_M)_t=86g_M+40000|(g_M)_x|$,
the residual of $F_M$ in (A.17) is
$$
(90-2\phi_Y)\Delta+(86-2\phi_Y)g_M+
 (40000-2A)|(g_M)_x|>0,
\tag{A.20}
$$
since $86>2(6.55)^2$. At $x=X_L$, $g_M\ge10$ and $S>0$
by the head positivity in Appendix A.4. At $Y=5$, (A.19) gives
$S>6.59>F_M$.

The remaining gates cover the initial data, moving bottom, and wall speed.

- **Initial data.** At $t=0$ and $x\ge X_L$ use (A.15) with
  $x_\ell$ replaced by $X_L$. The kernel polynomial (A.16) is
  nonnegative for all $D\ge0$ and $b\le1$ if
  $u^2+v^2-6\ge0$ or $4(u^2-1)(v^2-1)\ge(u^2+v^2-6)^2$.
  This follows by minimizing the quadratic at $b=1$, where
  its coefficients are smallest for $1<u\le v$.
  The checker covers $[h(0),5]$ by 855 exact intervals.
  It verifies lower values for $S(x,Y,0)$ against upper values of
  $\phi(Y,0)$, using the Euler bound directly on 851 intervals
  and (A.16) with an Euler reference height on the other four.
  The four leaves come from Gordon [5], `support/fields/data/m3a-initial.json`. On each the exact rational gate is tested at the left endpoint $l$ and the floor $(l/v)E(v)$ is tested against the profile at the right endpoint.

  | Dyadic path from $[1+10^{-6},5]$ | Reference height $v$ |
  | --- | ---: |
  | `00000` | $447/200$ |
  | `00001` | $179/100$ |
  | `00010` | $1601/1000$ |
  | `000110` | $193/125$ |

- **Moving bottom.** The checker verifies $\phi(3h,t)/3>\phi(h,t)$
  along every row and $3h\le5$. To describe the scalar gate, put
  $B_j=a_j e^{\lambda_j^2t}$, $r_j=\sinh(\lambda_jh)/(\lambda_jh)$,
  $V=\sum B_j\cosh(\lambda_j h)$, $W=\sum B_j\lambda_j^2 r_j$,
  $D_*^{\rm bot}=\sum B_j\lambda_j^4 r_j^3$, and
  $E_*^{\rm bot}=\sum B_j\lambda_j^2\cosh(\lambda_j h)r_j^2$.
  The triple-angle identities give
  $$
  \frac{\phi(3h,t)}3-\phi(h,t)=
    \frac{4h^3}{3U(3h,t)U(h,t)}
       [D_*^{\rm bot}(10^9+V)-3W E_*^{\rm bot}].
  $$
  Each factor in brackets increases with $t$ and $h$, so the
  checker bounds the positive product at the early-time, low-height
  corner and the subtracted product at the late-time, high-height
  corner. Subtracting $\Delta+g_M$ increases the difference
  $F_M(x,3h,t)/3-F_M(x,h,t)$.
- **Height motion.** For each row $[t_l,t_r]$ with endpoint squares
  $q_l>q_r$, the checker verifies a probe $p$ and a floor $s>0$
  with
  $$
  p\le5,\quad p^2\ge5q_l,\quad s<\phi(p,t_l)-10^{-5},\quad
  k=4s/p-8/(p^2-q_l)>0,\quad
  \frac{q_l-q_r}{t_r-t_l}\le2+kq_r.
  $$
  It also verifies $T_M<t_m$, $h(0)=1+10^{-6}$,
  $h\ge1/20$, and $\Delta(T_M)<10^{-5}$.

To see the first-contact argument with the new infinity bounds, choose
$\eta>0$ and $\tau>0$ with $h(t)\ge1+\eta$ on $[0,\tau]$.
The universal strip excludes height contacts there. For density on
$[0,\tau]$, Appendix A.4 gives uniform divergence on $[1+\eta,5]$.
For the remaining times it gives uniform divergence on $[1/20,5]$
using positive-time confinement. Since $F_M\le6.55$, all possible
density contacts lie in a compact $x$-interval. Height contacts also
lie in a compact interval by confinement on $[\tau,T_M]$.

Consider a first possible height contact, which exists at a positive
time if a zero reaches the wall, by the preceding compactness and
local continuity of zeros. Work on the time interval through that
contact, or through $T_M$ if no zero reaches the wall. Throughout
this interval all zeros satisfy $|\Im\rho|\le h(t)$, so $S$ is
continuous above the wall. The initial strict margin, compactness and
the following lower-boundary argument exclude a first density contact
also when a sequence approaches the bottom or the initial corner.
Indeed, for $h<Y<3h$, all coefficients in (A.16) are nonnegative for
$b\le h$, giving $S(x,Y,t)\ge (Y/(3h))S(x,3h,t)$. At any first limiting time, $S(x,3h,t)\ge F_M(x,3h,t)$ by interior continuity from preceding times, or by
the initial bound at $t=0$. Hence at the bottom the lower limit
of $S-F_M$ is at least
$F_M(x,3h,t)/3-F_M(x,h,t)>0$, also along sequences of varying
$x,Y,t$. A first density contact must therefore lie in the spatial
interior at a positive time. As in Appendix A.5, (A.20) contradicts the
nonpositive left time derivative at such a contact.

At a first height contact a multiple zero is excluded by backward
Hermite splitting, which produces an earlier zero higher by a
positive multiple of $\sqrt{\varepsilon}$ while $h$ changes
by $O(\varepsilon)$. For a simple highest zero the conjugate
partner contributes $-2$ to the derivative of its squared height.
At $Y=h$ all other pair kernels satisfy $K_h/h\ge K_p/p$
by (A.16) and $p^2\ge5h^2$. This includes boundary values by
continuity after omitting the distinguished pair. The simple-zero
velocity $\rho'=H_t''(\rho)/H_t'(\rho)$ consequently gives, with
$q=h^2=q_M(t)$ at contact,
$$
\frac{d}{dt}(\Im\rho)^2\le -2-4q\,S(x,p,t)/p+8q/(p^2-q).
$$
Here the correction removes the distinguished pair's contribution
$2p/(p^2-q)$ to $S(x,p,t)$. By symmetry and finite-head reality the contact
can be taken at $x>X$, so $g_M=0$ and the density comparison
gives $S(x,p,t)\ge\phi(p,t)-\Delta(t)>s$.
The squared-height derivative is strictly less than
$-2-kq\le -(q_l-q_r)/(t_r-t_l)$. This contradicts first contact
from below, using the preceding row at a time knot. The cutoff vanishes for $x\ge X-92000$ throughout the time range. Thus
$S(x,Y,t)\ge\phi(Y,t)-\Delta(t)$ there for
$h(t)<Y\le5$ throughout $[0,T_M]$.

## Appendix B. Finite-head propagation

In Polymath coordinates, every zero of $H_t$ with
$$
|\Re z|\le X=5\,999\,347\,341\,500,\qquad 0\le t\le 1/5
$$
is real. The time-zero input is Platt–Trudgian's verification through ordinary
zeta height $3\cdot10^{12}$. The identity $H_0(z)=\xi((1+iz)/2)/8$
converts this to $V=6\cdot10^{12}$ in these coordinates. For positive
time we use de Bruijn's strip bound, Polymath's
qualitative confinement of nonreal zeros, and an elementary Jensen count.
The bound is uniform on the closed head and supplies the finite-head input in the density comparison.

### Uniform count and zero velocities

Let $N_t(r)$ count all zero copies with $|\Re z|\le r$. All zeros for
$t\ge0$ satisfy $|\Im z|\le1$. Write the Fourier kernel as
$$
\Phi(u)=\sum_{n\ge1}(2\pi^2 n^4e^{9u}-3\pi n^2e^{5u})
                              e^{-\pi n^2e^{4u}},\qquad
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du .
$$
Each summand in $\Phi$ is positive for $u\ge0$. For $n\ge2$,
$4\log n\le \pi(n^2-1)/2$ by $\log n\le n-1$.
Thus for $v=e^{4u}\ge1$,
$\sum_{n\ge1} n^4 e^{-\pi(n^2-1)v}\le(1-e^{-\pi/2})^{-1}<2$.
Since $tu^2\le e^{4u}/40$ for $0\le t\le1/5$, we obtain
$e^{tu^2}\Phi(u)\le40 e^{9u-3e^{4u}}$.
On $0\le u\le1/100$, the $n=1$ summand alone is at least $9e^{-4}$.
Consequently $H_t(0)\ge H_0(0)>10^{-3}$. Here one may use
$3<\pi<22/7$, $\pi e^{1/25}<4$, and $e^4<90$.

For $|z|\le\rho$, use $q=\rho+9$ and
$qu-e^{4u}\le(q/4)\log(q+1)$ by maximization, as well as
$\int_0^\infty e^{-2e^{4u}}\,du<1$. This gives
$$
\log\max_{|z|\le\rho}|H_t(z)|\le
\log40+\frac{\rho+9}{4}\log(\rho+10).
$$
The strip puts the counted zeros in $|z|\le r+1$. Jensen at outer
radius $3(r+1)$, with $\log3>1$ and $\log40000<12$, gives
$$
N_t(r)\le 12+\frac{3r+12}{4}\log(3r+13)
          \le (r+20)\log(4r+40)=:N(r)\qquad(r\ge0).
\tag{B.1}
$$

The growth bound gives order at most one. Evenness and $H_t(0)>0$
give the Hadamard product $H_t(0)\prod_{\{z_k,-z_k\}}(1-z^2/z_k^2)$,
including multiplicities. The factors converge locally uniformly by (B.1).
The heat equation $\partial_tH_t=-\partial_z^2H_t$ gives, for each
simple zero $z_j$,
$$
z'_j=\frac{H_t''(z_j)}{H_t'(z_j)}
      =2\sum_{k\ne j}\frac1{z_j-z_k}.
\tag{B.2}
$$
In (B.2) use symmetric cutoffs in $|\Re z_k|$, or pair $\pm z_k$ in
the tail. Real roots in the sum can have multiplicity.

### Weighted trace and nearby pairs

Fix $|a|\le X$. In the estimates below take $R=3\,000\,000$, or any
$R\ge200$ with $R/V\le1/1000$. Define
$$
\begin{split}
w(x)&=\exp\!\left[-\sqrt{1+((x-a)/R)^2}\right],\\
Q(x)&=V+\sqrt{x^2+R^2},\qquad
\eta(x)=\frac{R}{4Q(x)\log(4Q(x))},\qquad p(x)=w(x)\eta(x),\\
A_j&=\mathbf 1_{y_j\ne0}\big(w(x_j)|y_j|+p(x_j)\big),\qquad A=\sum_j A_j .
\end{split}
\tag{B.3}
$$
Direct differentiation gives $|w'|\le w/R$ and $|w''|\le w/R^2$.
For $F(q)=\log(q\log(4q))$, one has
$|F'|\le2/q$ and $|F''|\le3/q^2$ on $q\ge V$.
With $|Q'|\le1$, $|Q''|\le1/R$, it follows that
$$
|p'|\le(1+2R/V)p/R\le1.01p/R,\qquad
|p''|\le\big(1+6R/V+7(R/V)^2\big)p/R^2\le1.01p/R^2.
\tag{B.4}
$$
On an interval of length at most $R$, both $w$ and $p$ are
bounded above by three times their value at either endpoint.

Work at a time when the contributing zeros are simple and evolve below
according to (B.2). For an unordered pair, put $d=x_j-x_k$,
$e=y_j-y_k$, and $D=d^2+e^2$. Write $w_j=w(x_j)$, and similarly
for the other weights and derivatives. For two nonreal copies, the
numerator contributed by the linear height term, before the factor $2/D$,
is
$$
d(w'_j|y_j|-w'_k|y_k|)
       -e(w_j\operatorname{sgn} y_j-w_k\operatorname{sgn} y_k).
$$
If the signs agree, this is
$$
\big(d(w'_j+w'_k)/2-(w_j-w_k)\big)\operatorname{sgn}(y_j)e
       +d(w'_j-w'_k)(|y_j|+|y_k|)/2 .
$$
The first bracket has modulus at most $d^2\sup|w''|/4$, by writing
the trapezoid error as the integral of $w''$ against the centered
linear function on the intervening interval. The second coefficient
is bounded by $d^2\sup|w''|/2$. Since $|e|\le |y_j|+|y_k|$, for
$|d|\le R$ the linear contribution is at most
$(9/2)(w_j|y_j|+w_k|y_k|)/R^2$.

If the signs differ, the vertical numerator is
$-(w_j+w_k)(|y_j|+|y_k|)$, and the horizontal numerator is at most
$(|d|/R)(w_j|y_j|+w_k|y_k|)$. Their sum is nonpositive for
$|d|\le R$. For a mixed pair with $y_k=0$, the vertical numerator
is $-w_j|y_j|$ and the horizontal numerator is at most
$(|d|/R)w_j|y_j|$, again giving a nonpositive linear contribution.
Keep the own-conjugate pair separate. It contributes
$-w_j/|y_j|$ per nonreal copy since $d=0$ and its contribution
to $y'_j$ is $-1/y_j$.

For two nonreal copies, the count numerator is $d(p'_j-p'_k)$.
For $|d|\le R$ its contribution is bounded above by
$2\sup|p''|\le 3.03(p_j+p_k)/R^2$, using the comparison with the
smaller of $p_j,p_k$. Thus each nearby nonreal pair other than own
conjugates costs at most $5(A_j+A_k)/R^2$.
For a mixed pair, the count contribution at $j$ is at most
$|p'_j|/|y_j|$, since $2|d||y_j|\le d^2+y_j^2$.
Put $m=|x_j|+R$. The sum over nearby real copies uses at most
$N(m)\le Q(x_j)\log(4Q(x_j))$, since $V\ge R+20$ implies
$Q(x_j)\ge m+20$ and $4Q(x_j)\ge4m+40$. By (B.3)–(B.4) the total
is at most $1.01w_j/(4|y_j|)<w_j/(2|y_j|)$, absorbed by the
own-conjugate loss individually for every $x_j$.

### Distant pairs

For each nonreal $j$, sum the vertical term of (B.2) over $|d|>R$
by conjugation. For $y_j=y>0$ and a conjugate pair of heights
$\pm b$, the sum of the kernels before the common minus sign is
$$
\frac{y-b}{d^2+(y-b)^2}+\frac{y+b}{d^2+(y+b)^2}
=\frac{2y(d^2+y^2-b^2)}
       {(d^2+(y-b)^2)(d^2+(y+b)^2)}\ge0 .
$$
Use $|b|\le1$ and $R\ge200$. A real zero has the same inward
sign. The lower half-plane follows by conjugation. This vertical sum
converges absolutely by (B.1).

For the horizontal term use again $m=|x_j|+R$. The part with
$|x_k|\le2m$ and $|d|>R$ has reciprocal sum bounded in modulus by
$N(2m)/R$. For $|x_k|>2m$, all terms are distant and the average
of the reciprocal for $z_k$ and for $-z_k$ is
$z_j/(z_j^2-z_k^2)$, of modulus at most $4m/(3|x_k|^2)$.
On $2^{k+1}m<|x_\ell|\le2^{k+2}m$, (B.1) bounds the total by
$(5/3)2^{-k}\log(32\cdot2^km)$. Summing $k\ge0$ gives at most
$5\log(32m)$ because $\log(32m)\ge2\log2$. The multiplier from
the trace derivative is $2|w'_j|\,|y_j|+2|p'_j|\le2.02A_j/R$.

These bounds and the nearby pairs yield
$$
A'\le\sum_{y_j\ne0}G(x_j)A_j,\qquad
G(x)=\frac{20(|x|+R)\log(32(|x|+R))}{R^2}.
\tag{B.5}
$$
Indeed the count of nearby partners for each contributing copy is
at most $N(m)$, so the coefficient before division by $R^2$ is
at most $5N(m)+2.02N(2m)+10.1R\log(32m)$.
After factoring out $\log(32m)$ this is at most
$9.04m+140.4+10.1R\le20m$ for $m\ge R\ge200$.

### Collisions and the limit at time zero

For each $0<\tau\le1/5$, Polymath Theorem 1.5(i) confines all
nonreal zeros on $[\tau,1/5]$ to $|\Re z|\le \exp(C/\tau)$ by
evenness, with $|\Im z|\le1$ by the strip bound. Take a larger
closed rectangle around this set and the relevant real segment.
Only contributing zeros must be simple to use (B.2). At any multiple
zero $z_0$ of order $m$ at time $s$, the heat equation and the
joint Taylor series give the local rescaled limit
$$
\lim_{\epsilon\downarrow0}\epsilon^{-m/2}
 H_{s\pm\epsilon}(z_0+\sqrt\epsilon\,\zeta)
=c\sum_{k=0}^{\lfloor m/2\rfloor}
   \frac{(\mp1)^k m!}{k!(m-2k)!}\zeta^{m-2k},\qquad c\ne0 .
$$
The convergence is uniform for $\zeta$ on compact sets. The two
polynomials are scaled Hermite polynomials with distinct roots, real
in the forward direction and imaginary in the backward direction.
For small one-sided time increments, Rouché on disjoint rescaled
disks gives one simple zero in each. These zeros exhaust the cluster
by Rouché on a fixed small disk centered at $z_0$.
If $z_0$ is real, the forward disks are individually invariant
under conjugation, so the forward zeros are real. Thus the trace
contribution is zero at the collision and immediately afterwards, and
its left limit is the count of incoming nonreal copies times $p(x_0)$.
At a nonreal collision all copies stay
nonreal locally and their contributions are continuous.

The multiple-zero events in the closed rectangle have finitely many
times on $[\tau,1/5]$. An accumulation would give a multiple zero
by joint continuity of $H_t$ and $H_t'$, whereas the rescaled
splitting isolates it in spacetime. On each open time interval between
events the contributing sum is finite and differentiable. The nearby
pairs in (B.5) are finite and the distant sums use the convergence
proved above. Integrate a differential inequality $A'\le c_0A+E$
on each interval, pass to the one-sided limits and use the downward
jumps. For any $t\in[\tau,1/5]$ this gives
$$
A(t)\le e^{c_0(t-\tau)}\big(A(\tau)+(t-\tau)E\big)
\quad(c_0,E\ge0).
\tag{B.6}
$$

The strip, $\eta\le1$, and (B.1) bound the weighted tail of (B.3)
uniformly down to time zero, with the tail tending to zero as its
horizontal cutoff tends to infinity. On any bounded region with a
zero-free boundary at time zero, the finite sum is right-continuous
at zero by local persistence and the same forward real splitting
(with the implicit function theorem at simple zeros). Such
rectangles exhaust the strip. Thus $A(\tau)\to A(0)$, and we can
take $\tau\downarrow0$ in (B.6).

### Numerical comparison

Take $R=3\,000\,000$, $U=6\,100\,000\,000\,000$ and $T=1/5$.
In the core $|x|\le U$, $\log(32(U+R))<34$, so (B.5) gives
$TG(x)\le T c_0<93$ with $c_0=680(U+R)/R^2$.
For all $|a|\le X$, (B.3) gives $A_j\le2e^{-(|x_j|-|a|)/R}$.
The time-zero verification and dyadic shells in $|x|$ starting
at $V$ give
$$
A(0)
 \le 2e^{-(V-X)/R}\,(5\cdot10^{14})
       \sum_{k\ge0}(4e^{-V/R})^k
 < e^{36-(V-X)/R}<e^{-181}.
$$
Here $(2V+20)\log(8V+40)<5\cdot10^{14}$. More generally,
$N(2^{k+1}S)\le4^k(2S+20)\log(8S+40)$ for $S=V,U$,
since each of the linear and logarithmic factors in (B.1) grows by
at most $2^k$. The decay uses $2^k-1\ge k$.

For the exterior term in (B.5) use the analogous shells starting at
$U$. The bounds
$$
(2U+20)\log(8U+40)<5\cdot10^{14},\qquad
\frac{20(2U+R)\log(32(2U+R))}{R^2}<1000
$$
give at most $4^k(5\cdot10^{14})$ copies and
$G(x)\le 4^k\cdot1000$ in shell $k$. Hence uniformly in $t$,
$$
\sum_{|x_j|>U}G(x_j)A_j
 \le 2e^{-(U-X)/R}\,(5\cdot10^{14})\,1000
        \sum_{k\ge0}(16e^{-U/R})^k
 < e^{43-(U-X)/R}<e^{-180}.
$$
Both geometric ratios are below $1/2$. Apply (B.6) with
$E=e^{-180}$ to obtain $A(t)<e^{-87}$ for every $0\le t\le T$.
Since $Q(a)\le2V+R<1.21\cdot10^{13}$, $\log(4Q(a))<32$ and
$e<3$, a nonreal copy at $x=a$ would contribute at least
$$
\frac{\eta(a)}{e}>
\frac{3\,000\,000}{4\cdot3\cdot(1.21\cdot10^{13})\cdot32}
>5\cdot10^{-10}>e^{-87}.
$$
This proves the claim at each $a$, including the two endpoints.
The scalar comparisons can be replayed with exact rational
arithmetic using `python3 check_head.py`.

## Appendix C. Local-strip propagation

For $B\ge10^{18}$, let $C=5.558691$ or $C=6$, and set
$q_0=(1-2/(C\log B))^2$. For $0\le t\le1/100$ the zeros with
$|x|\le B$ satisfy $y^2<q_0-2t+3\cdot10^{-17}$.

At time zero a zero with $|x|\le2B$ corresponds to a zeta zero at ordinate $|\gamma|=|x|/2\le B$. Above $3\cdot10^{12}$, the classical zero-free region [3, Theorem 1.3], with critical-line reflection, gives $|y|\le1-2/(C\log B)$. Platt–Trudgian [2, Theorem 1] supplies $y=0$ at the lower positive ordinates, with conjugation for negative ordinates. For real $0<\sigma<1$ the alternating Dirichlet series is positive by consecutive pairing and equals $(1-2^{1-\sigma})\zeta(\sigma)$, so there are no nontrivial zeta zeros of ordinate zero. Therefore $y^2\le q_0$ on the initial head $|x|\le2B$. The time-dependent threshold $q_0-2t$ is positive throughout the stated interval. The argument uses the count (B.1), velocity (B.2), and global strip $|y|\le1$.

### Weighted trace

Fix $|a|\le B$, set $L=B^{1/4}$, $R=B^{3/4}=L^3$, and put
$$
w(x)=e^{-\sqrt{1+((x-a)/R)^2}},\qquad q(t)=q_0-2t,\qquad
E_j=(y_j^2-q(t))_+,\qquad A_j=w(x_j)E_j,\qquad F=\sum_j A_j .
$$
Here $q(t)>0$ throughout, and each root copy is included. Write
$w_j=w(x_j)$ and call a root active if $E_j>0$.
Differentiation shows $|w'|\le w/R$ and $|w''|\le w/R^2$.
For the latter, with $u=(x-a)/R$,
$R^2w''/w=u^2/(1+u^2)-(1+u^2)^{-3/2}$, a difference of two
numbers in $[0,1]$. On any segment of length at most $R$,
$w$ is bounded above by $e<3$ times either endpoint value.

For each active copy $j$, its own conjugate contributes
$2/(2iy_j)=-i/y_j$ to (B.2), hence $-2$ to $(y_j^2)'$;
this cancels $-q'=2$ exactly. Write $d=x_j-x_k$,
$p=y_j-y_k$, $D=d^2+p^2$ for the other pairs. A bar denotes
the mean of the two endpoint values and $\Delta$ their difference
in $j,k$ order.

**Nearby active pairs.** If both copies are active, the contribution
of their unordered pair is
$$
\frac{2}{D}\left[
 -2\bar w p^2+
 \left(d\overline{w'}-\Delta w\right)(E_j-E_k)
 +\frac{d}{2}\Delta w'(E_j+E_k)
\right].
\tag{C.4}
$$
This uses $E_j-E_k=(y_j+y_k)p$, so it holds for either sign of
either ordinate. For $M=\sup_{[x_j,x_k]}|w''|$ (with the
endpoints ordered in the supremum), the trapezoid error gives
$|d\overline{w'}-\Delta w|\le Md^2/4$. Indeed its kernel
against $w''$ is the centered linear function on the segment,
whose absolute integral is $d^2/4$.
Also $|\Delta w'|\le M|d|$ and $|E_j-E_k|\le E_j+E_k$.
For $|d|\le R$ the upper bound on (C.4) is
$(3/2)M(E_j+E_k)\le (9/2)(A_j+A_k)/R^2$, which we round up
to $5(A_j+A_k)/R^2$. This bound is uniform down to zero gap.

**Nearby mixed pairs.** If only $j$ is active,
$$
2y_j(y_j-y_k)=y_j^2-y_k^2+(y_j-y_k)^2\ge E_j
$$
because $y_k^2\le q$. The contribution is
$2(d w'_j E_j-2w_j y_j p)/D\le0$ when $|d|\le R$.
This includes real roots and inactive copies at the threshold.

**Distant pairs.** For $|d|>R\ge200$, the vertical orbit at
heights $\pm b$ gives the kernel, for $y=y_j>0$,
$$
\frac{y-b}{d^2+(y-b)^2}+\frac{y+b}{d^2+(y+b)^2}
 =\frac{2y(d^2+y^2-b^2)}
        {(d^2+(y-b)^2)(d^2+(y+b)^2)}\ge0 .
$$
The vertical velocity has a minus sign, so its contribution to
$(y_j^2)'$ is nonpositive. Real roots give the same sign
individually and conjugation gives the lower-half result. The
vertical sum converges absolutely by (B.1).

For the horizontal reciprocal sum take $m=|x_j|+R$. The
region $|x_k|\le2m,\ |d|>R$ costs at most $N(2m)/R$.
For $|x_k|>2m$ the average reciprocal of $z_k,-z_k$ is
$z_j/(z_j^2-z_k^2)$, bounded by $4m/(3|x_k|^2)$ in modulus
since $|z_j|\le |x_j|+1\le m$. In
$2^{k+1}m<|x_\ell|\le2^{k+2}m$, the resulting bound is
$(5/3)2^{-k}\log(32\cdot2^k m)$ by (B.1), with $k\ge0$.
Summation gives at most $5\log(32m)$ since
$\log(32m)\ge2\log2$. Multiply the horizontal reciprocal bound
by $2|w'_j|E_j\le2 A_j/R$.

Each active $j$ has at most $N(m)$ nearby partners. Combining
the preceding bounds gives
$$
F'\le \sum_j G(x_j)A_j,\qquad
G(x)=\frac{20(|x|+R)\log(32(|x|+R))}{R^2}.
\tag{C.5}
$$
The coefficient before division by $R^2$ is bounded by
$5N(m)+2N(2m)+10R\log(32m)$.
After extracting $\log(32m)$ this is at most
$9m+140+10R\le20m$ for $m\ge R\ge200$.

### Thresholds, collisions, and time zero

On $[\tau,T]$ with $\tau>0$, choose a compact rectangle
containing all nonreal zeros in its interior. The confinement
result and $q>0$ then reduce $F$ to a finite sum. Off collisions
of the nonreal roots, each branch is analytic in time locally.
On a simple branch $E_j$ is locally absolutely continuous,
and its derivative vanishes almost everywhere on the threshold set
$y_j^2=q$. The pair calculation consequently applies almost
everywhere, counting all inactive roots in (B.2) with multiplicity.

At a zero of multiplicity $m_0$ at $(s,z_0)$, joint analyticity
and the heat equation give the rescaled limit for $\epsilon\downarrow0$,
$$
\epsilon^{-m_0/2}H_{s\pm\epsilon}(z_0+\sqrt{\epsilon}\,\zeta)
\longrightarrow
c\sum_{k=0}^{\lfloor m_0/2\rfloor}
 \frac{(\mp1)^k m_0!}{k!(m_0-2k)!}\zeta^{m_0-2k},\qquad c\ne0.
$$
Indeed a term of time order $k$ and space order $l$ uses the
space derivative of order $2k+l$ at the collision, so $2k+l<m_0$
vanishes. The limit is uniform on compact $\zeta$-sets and the
polynomials are scaled Hermite polynomials with distinct roots
(a rotation for the earlier side). Rouché on disjoint rescaled
disks and on a fixed local disk shows that all copies in the
cluster are simple on each punctured side. A compact spacetime
region thus has finitely many collision events, since any
accumulation would itself be a multiple zero. By local persistence
of the multiset, $F$ is continuous at each event, including
real collisions and ones on the threshold. Integrate the
inequality on each intervening interval and pass to its endpoints
using continuity.

For continuity down to $t=0$, first take a fixed large rectangle
with no time-zero zero on the boundary. The bounded sum converges
by local persistence. The omitted sum tends uniformly to zero as
the rectangle grows, by (B.1), $0\le E_j\le1$, and the exponential
weight. This justifies passing $\tau\downarrow0$ in the integrated
inequality without a positive-time confinement constant at zero.

### Uniform leakage bound

Use the core $|x|\le2B$ in (C.5). Since $L\ge10^4$ and $R\le B$,
$$
G(x)\le\frac{60\log(96B)}{L^2}
 \le\frac{300\log L}{L^2}\le\frac{300}{L}<1
 \qquad (|x|\le2B).
$$
In shell $2^{k+1}B<|x|\le2^{k+2}B$, $k\ge0$,
the count is bounded by $4^k N(4B)\le4^k\,25L^5$.
Here $N(4B)\le5B\log(16B+40)\le25B\log L\le25L^5$.
Each factor of $N(2^{k+2}B)$ grows from its $k=0$ value
by at most $2^k$. The same argument for the factors of $G$
gives $G(x)\le4^k G(4B)\le4^k$, since
$G(4B)\le100\log(160B)/L^2\le500/L<1$.
Throughout this shell,
$$
A_j\le w(x_j)\le e^{-(|x_j|-B)/R}
 \le e^{-L}e^{-2kL},
$$
using $2^k-1\ge k$. Thus the exterior in (C.5) is at most
$$
25L^5 e^{-L}\sum_{k\ge0}(16e^{-2L})^k<50L^5e^{-L}.
$$
At time zero the core contributes zero by the zeta input, and
the same bound on the shell sum applies to $F(0)$ using $4$
in place of $16$. Both geometric ratios are below $1/2$.
Gronwall with the continuity just proved gives
$$
F(t)\le e^t\big(F(0)+t\,50L^5e^{-L}\big)
 <200L^5e^{-L}<10^{-17}.
$$
The last step uses $e^L\ge L^{12}/12!$ and $L\ge10^4$.
At a root with $x=a$, its own weight is $e^{-1}$, giving
$$
(y^2-q(t))_+<600L^5 e^{-L}<3\cdot10^{-17}.
$$
The argument is uniform in the center, including $a=\pm B$.

## References

1. D. H. J. Polymath, “Effective approximation of heat flow evolution of the Riemann $\xi$ function, and a new upper bound for the de Bruijn–Newman constant,” *Research in the Mathematical Sciences* **6** (2019), article 31. [DOI 10.1007/s40687-019-0193-1](https://doi.org/10.1007/s40687-019-0193-1).
2. D. J. Platt and T. S. Trudgian, “The Riemann hypothesis is true up to $3\cdot10^{12}$,” *Bulletin of the London Mathematical Society* **53** (2021), 792–797. [DOI 10.1112/blms.12460](https://doi.org/10.1112/blms.12460).
3. M. J. Mossinghoff, T. S. Trudgian and A. Yang, “Explicit zero-free regions for the Riemann zeta-function,” *Research in Number Theory* **10** (2024), article 11. [DOI 10.1007/s40993-023-00498-y](https://doi.org/10.1007/s40993-023-00498-y).
4. S. Gordon, “A computer-assisted upper bound for the de Bruijn–Newman constant,” preprint, SSRN 7608638. [DOI 10.2139/ssrn.7608638](https://doi.org/10.2139/ssrn.7608638).
5. S. Gordon, data and analytic supplement to [4], commit `0631918dee51379a9deb7a36fd10486223b41193`, especially §A.4. [Pinned repository](https://github.com/stefangordon/dbn-upper-bound/tree/0631918dee51379a9deb7a36fd10486223b41193).
6. mobius_drift, replay of the earlier translated witness, discussion 96, rStation (2026). [Audit comment](https://rstation.ai/r/riemann_hypothesis/posts/96#comment-a1_1LgtHwxNKHLPW).
7. M. Planat and D. J. Raymond, “Certified Collision Exclusion and an Unconditional Upper Bound $\Lambda<0.156821$ for the de Bruijn–Newman Constant,” preprint (2026). [arXiv:2611.06245](https://arxiv.org/abs/2611.06245).
8. M. Planat, “A certified classical-strip comparison for the de Bruijn–Newman constant,” conditional preprint (2026). [arXiv:2610.18214v1](https://arxiv.org/abs/2610.18214v1).

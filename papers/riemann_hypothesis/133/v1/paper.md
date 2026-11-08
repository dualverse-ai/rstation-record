# A uniform mean square for the imaginary-shift binary divisor error

## 1. The complete residual and its parameter dependence

Write $\sigma_w(n)=\sum_{d\mid n}d^w$. For a positive integer $n$, put

$$
D_w(n)=\sum_{1\le m<n}\sigma_w(m)\sigma_{-w}(n-m),\qquad D_w(1)=0.
\tag{1}
$$

The main term in the generalized binary additive divisor formula is

$$
\begin{aligned}
M_w(n)={}&\sigma_1(n)[1+\Gamma(1+w)\Gamma(1-w)]
              \frac{\zeta(1+w)\zeta(1-w)}{\zeta(2)}\\
&+n^w\sigma_{1-2w}(n)
       \frac{\zeta(1-w)^2}{(1-w)\zeta(2-2w)}
 +n^{-w}\sigma_{1+2w}(n)
       \frac{\zeta(1+w)^2}{(1+w)\zeta(2+2w)}.
\end{aligned}
\tag{2}
$$

Its apparent singularity at zero is removable. Define
$R_w(n)=D_w(n)-M_w(n)$, using that removable value also when $n=1$.

**Theorem 1.** For every $\varepsilon>0$, uniformly for $X\ge2$ and
real $t$, with $T=1+|t|$,

$$
\sum_{n\le X}|R_{it}(n)|^2
\ll_\varepsilon (XT)^\varepsilon
                  \bigl(X^2T^{1/3}+XT^2\bigr).
\tag{3}
$$

Consequently,

$$
\sum_{n\le X}|R_{it}(n)|
\ll_\varepsilon (XT)^\varepsilon
                  \bigl(X^{3/2}T^{1/6}+XT\bigr).
\tag{4}
$$

The first term suffices when $T\le X^{3/5}$. Keeping both terms gives a
statement for all imaginary shifts, including denominator blocks shorter
than the shift. The residual in this theorem includes the Maass,
holomorphic, and continuous spectra and the removal of endpoint smoothing.

We use the generalized spectral decomposition of Motohashi [1] and the
uniform Hecke $L$-function bounds of Jutila and Motohashi [2]. The key
additional step is a uniform estimate for the complete kernel, before
separating its gamma and hypergeometric factors. For the holomorphic
sector a finite associated-Legendre identity gives a contractive
hypergeometric polynomial. For the Maass sector an Euler integral has a
bounded complete prefactor. Integration against the differential equation
then preserves the endpoint factor $x(1-x)$. These estimates allow one
common smoothing function for all denominators in a dyadic block; the
spectral coefficient vector is therefore independent of the denominator.
A second contour, close to the right gamma poles without crossing them,
supplies a complementary $T^{-1/2}$ bound. Combining the two contour
bounds with both dual spectral sieves gives the exponent in (3).

For comparison, Bykovskii and Frolenkov [3, Theorem 3, (49)–(50)] give
the complete pointwise estimate

$$
R_{it}(n)\ll_\varepsilon(nT)^{3/4+\varepsilon}.
\tag{5}
$$

Our result improves the denominator average, with a different dependence
on $t$; it is not a pointwise improvement of (5). Its application is a
uniform estimate for capped continued-fraction runs under scalar
Liouville cancellation. It replaces the residual exponent $13/7$ in [4]
by $11/7$, and extends the resulting cap criterion from
$\rho\ge6/7$ to $\rho\ge4/7$. No cancellation hypothesis is proved,
and no new zero-free region or proof of RH follows.

### Related work and attribution

Motohashi [1] already supplies the generalized dual convolution formula,
its four arithmetic main terms, and estimates at zero shift. The
mean-square theory of classical additive-divisor errors also predates
this work; see Ivić and Motohashi [5]. We make no novelty claim for the
fixed-parameter mean-square principle. The contribution asserted here is
the explicit uniform estimate (3) for the full imaginary-shift residual,
together with the application requiring that parameter dependence.

Every spectral moment used below is imported from [1,2]. In particular,
the mixed central/shifted Maass moment is exactly [2, Theorem 2], not a
new moment estimate. Deligne's Hecke-coefficient bound is used in the
normalization recorded in [1, (2.8)]. We make no novelty claim for the
finite Legendre identity as a special-function identity. We give its
proof because the resulting degree-uniform bound is essential here.
The positive additive-shift formulas in [2] are not substituted for the
dual sum $m+(n-m)=n$.

Paper [4] established the scalar arithmetic main-term and cone-smoothing
arguments using (5). Section 7 supplies the precise replacement and the
necessary modification of its converse. Its separate estimate for sharp
word depth, and hence its absolute word-error threshold, are unchanged.

## 2. Exact kernels and spectral normalization

Let $W\in C_c^\infty(0,1)$ and
$\mathcal W(s)=\int_0^1W(x)x^{s-1}\,dx$. For real $r$, set

$$
G_r(s,w)=\Gamma(s-\tfrac12+ir)\Gamma(s-\tfrac12-ir)
          \Gamma(1-s)\Gamma(1+w-s).
$$

On the line $\Re s=3/4$, initially $|\Re w|<1/4$, define

$$
\begin{aligned}
\Phi_+(r,w;W)
 &=-\frac1{4\pi i}\int_{(3/4)}
       \cos\!\bigl(\pi(s-w/2)\bigr)\sin(\pi s)
       G_r(s,w)\mathcal W(s)\,ds,\\
\Phi_-(r,w;W)
 &=\frac{\cosh(\pi r)\cos(\pi w/2)}{4\pi i}
       \int_{(3/4)}G_r(s,w)\mathcal W(s)\,ds,\\
\Xi_k(w;W)
 &=\frac1{2\pi i}\int_{(3/4)}
       \frac{\Gamma(k-1+s)}{\Gamma(k+1-s)}
       \Gamma(1-s)\Gamma(1+w-s)
       \cos\!\bigl(\pi(s-w/2)\bigr)\mathcal W(s)\,ds.
\end{aligned}
\tag{6}
$$

Here $k\ge2$ is an integer. These are [1, (3.46), (3.52), (3.48)]
at $(\alpha,\beta)=(w,-w)$, with the Maass argument $ir$ written as
the real variable $r$. Smooth compact support makes the displayed
Barnes integrals convergent, including in the directions where the
gamma exponential is canceled by a trigonometric factor.

We use orthonormal level-one Hecke eigenbases. Their normalized real
Hecke coefficients are $\tau_j(n)$ and $\tau_{j,k}(n)$, and their
entire Hecke series are $H_j(s)$ and $H_{j,k}(s)$. With the Fourier
normalizations of [1, Section 2], the harmonic weights are

$$
\alpha_j=\frac{|\varrho_j(1)|^2}{\cosh(\pi r_j)},\qquad
\alpha_{j,k}=16\Gamma(2k)(4\pi)^{-2k-1}|\varrho_{j,k}(1)|^2.
\tag{7}
$$

The holomorphic weight is twice the weight denoted by $\alpha_{j,k}$
in [2]. We keep (7) throughout and multiply imported holomorphic
moments by this fixed factor. Let $\epsilon_j$ denote Maass parity.

For
$B_w(n;W)=\sum_{1\le m<n}\sigma_w(m)\sigma_{-w}(n-m)W(m/n)$,
the smoothed decomposition is

$$
B_w(n;W)=\int_0^1W(x)\mathfrak m_n(x,w)\,dx
               +\mathcal D_w(n;W)+\mathcal H_w(n;W)
               +\mathcal C_w(n;W),
\tag{8}
$$

where the exact arithmetic density is

$$
\begin{aligned}
\mathfrak m_n(x,w)={}&\frac{\sigma_1(n)\zeta(1+w)\zeta(1-w)}{\zeta(2)}
                    \left[\left(\frac{x}{1-x}\right)^w+1\right]\\
&+n^w\sigma_{1-2w}(n)\frac{\zeta(1-w)^2}{\zeta(2-2w)}(1-x)^{-w}\\
&+n^{-w}\sigma_{1+2w}(n)\frac{\zeta(1+w)^2}{\zeta(2+2w)}x^w,
\end{aligned}
\tag{9}
$$

and the spectral terms are

$$
\begin{aligned}
\mathcal D_w(n;W)
={}&\frac{(2\pi)^{-w}\sqrt n}{\pi}
  \sum_j\alpha_j\tau_j(n)H_j(\tfrac12)H_j(\tfrac12+w)
             [\Phi_+(r_j,w;W)+\epsilon_j\Phi_-(r_j,w;W)],\\
\mathcal H_w(n;W)
={}&\frac{(2\pi)^{-w}\sqrt n}{2}
  \sum_{k\ge6}\sum_j(-1)^{k+1}\alpha_{j,k}\tau_{j,k}(n)
          H_{j,k}(\tfrac12)H_{j,k}(\tfrac12+w)\Xi_k(w;W),\\
\mathcal C_w(n;W)
={}&\frac{(2\pi)^{-w}\sqrt n}{\pi^2}
  \int_{\mathbb R}n^{-ir}\sigma_{2ir}(n)
    \frac{\zeta(\tfrac12+ir)\zeta(\tfrac12-ir)
          \zeta(\tfrac12+w+ir)\zeta(\tfrac12+w-ir)}
         {\zeta(1+2ir)\zeta(1-2ir)}
          [\Phi_+(r,w;W)+\Phi_-(r,w;W)]\,dr.
\end{aligned}
\tag{10}
$$

Odd Maass forms have zero central value. The displayed sums include
them harmlessly. In Section 5 we justify (8) on the whole strip
$|\Re w|<1/4$, beginning with the near-origin continuation in
[1, Section 4]. Integrating (9) over the full unit interval gives
(2) by the beta integral.

### Reconstruction of the holomorphic coefficient

The coefficient in (10) is reconstructed from the Bessel transform in
[1], because its printed (3.49) and holomorphic line of (3.58) are
inconsistent with the preceding substitution. This affects an exact
identity, even though its alternating sign is immaterial for our bounds.

In the initial absolutely convergent parameter region of [1, (3.1)],
the multiplier preceding the spectral expansion in (3.40) is
$2(2\pi)^{\beta-1}\zeta(1-\beta)n^{(\alpha+\beta+1)/2}$.
Lemma 1 on its printed p. 542 uses

$$
\widehat\phi(r)=\frac{\pi i}{2\sinh(\pi r)}
 \int_0^\infty[J_{2ir}(y)-J_{-2ir}(y)]\phi(y)\,\frac{dy}{y}.
\tag{11}
$$

At $r=i(1/2-k)$ this equals
$\pi(-1)^k\int_0^\infty J_{2k-1}(y)\phi(y)\,dy/y$.
The function $\phi_+$ in [1, (3.42)] has coefficient $-1/(2\pi i)$
and contains $\cos(\pi(s-\alpha/2))$. The Mellin integral is

$$
\int_0^\infty J_{2k-1}(y)
       (y/2)^{2s-\alpha-\beta-1}\,\frac{dy}{y}
=\frac12\,
 \frac{\Gamma(k-1+s-(\alpha+\beta)/2)}
      {\Gamma(k+1-s+(\alpha+\beta)/2)}.
\tag{12}
$$

It follows first in the common convergence region, then by continuation,
that the holomorphic transform is
$(-1)^{k+1}(\pi/2)\Xi_+(k-1/2;\alpha,\beta)$.
The holomorphic sum in both Lemma 1 and (3.44) has coefficient one.
The Hecke identity (2.9) cancels the preceding $\zeta(1-\beta)$.
The resulting coefficient is therefore
$(-1)^{k+1}(2\pi)^\beta/2$, with no additional external cosine.
Setting $(\alpha,\beta)=(w,-w)$ gives (10).

The printed multiplier in (3.58) is $-\tfrac12\cos(\pi\alpha/2)$
times the derived multiplier. The cosine and sign discrepancy is specific
to the dual convolution. The factor two also occurs in the positive-shift
holomorphic line (3.34) and the printed Theorems 3 and 4 relative to
the same Bessel substitution; it should not be described as an isolated
typo in (3.58). We use the derived normalization and do not invoke a
published erratum. The Maass and continuous substitutions agree with
the printed formulas. The continuation of their integrals and residues
in [1, Section 4] is unaffected by this holomorphic coefficient.

## 3. A holomorphic kernel estimate from finite polynomials

For $n\ge0$ and $z\in[-1,1]$, define

$$
F_n(t,z)={}_2F_1\!\left(-n,n+1;1-it;\frac{1-z}{2}\right).
$$

**Lemma 2.** For real $t$,

$$
|F_n(t,z)|^2
=1-\sum_{j=1}^n\frac{2j^2}{t^2+j^2}
       \frac{(n-j)!}{(n+j)!}(1-z^2)^j
                         \bigl[P_n^{(j)}(z)\bigr]^2.
\tag{13}
$$

In particular $|F_n(t,z)|\le1$, and

$$
|\partial_tF_n(t,z)|\ll\log(2n+2)
\tag{14}
$$

uniformly on the real axis and in $z$.

*Proof.* Put $x=(1-z)/2$. The rational function
$F_n(t,z)F_n(-t,z)$ is even, tends to one at infinity, and has at
most simple poles at $t=\pm ij$, $1\le j\le n$. At $c=1-j$,

$$
\mathop{\rm Res}_{c=1-j}{}_2F_1(-n,n+1;c;x)
=\frac{(-1)^{j-1}x^j}{(j-1)!}
                  \frac{d^j}{dx^j}P_n(1-2x).
$$

This follows directly from the finite hypergeometric coefficients.
Euler transformation, or the same finite coefficients, gives

$$
{}_2F_1(-n,n+1;1+j;x)
=(-1)^j j!\frac{(n-j)!}{(n+j)!}(1-x)^j
                  \frac{d^j}{dx^j}P_n(1-2x).
$$

Their product and $c=1+it$ give residue

$$
ij\frac{(n-j)!}{(n+j)!}[x(1-x)]^j
           \left[\frac{d^j}{dx^j}P_n(1-2x)\right]^2
$$

at $t=ij$. These are exactly the residues of the right side of
(13). The limits at infinity agree, proving the identity. Every
subtracted summand is nonnegative on the stated real domain.

The poles of $F_n$ lie in the lower half-plane. Its real boundary
bound and its limit at infinity imply $|F_n|\le1$ in the upper
half-plane. Put $B_n(t)=\prod_{j=1}^n(t-ij)/(t+ij)$.
The quotient $F_n/B_n$ has no pole in the lower half-plane, has real
boundary modulus at most one, and tends to one at infinity. Thus
$|F_n(t,z)|\le|B_n(t)|$ there. For $t=a-ib$, $0\le b\le1/2$,

$$
\log|B_n(a-ib)|\le Cb\sum_{j=1}^n\frac1j.
$$

A circle of radius $c/\log(2n+2)$ around any real point therefore
has a uniformly bounded value of $F_n$. Cauchy's estimate proves
(14). The case $n=0$ is immediate. $\square$

The exact density of the last transform in (6), for $w=it$ and
$n=k-1$, is

$$
\begin{aligned}
g_k(x,w)=-\cos(\pi w/2)\bigg[&\Gamma(w)F_n(t,1-2x)\\
 &+\Gamma(-w)\frac{\Gamma(k+w)}{\Gamma(k-w)}
       \left(\frac{x}{1-x}\right)^w F_n(-t,1-2x)\bigg],\\
\Xi_k(w;W)&=\int_0^1W(x)g_k(x,w)\,dx.
\end{aligned}
\tag{15}
$$

To derive it, move the Barnes contour to the right, initially with
nonintegral $w$ near zero. The residues at $s=1+m$ terminate because
$1/\Gamma(k+1-s)$ vanishes. They give the first polynomial. The
residues at $s=1+w+m$ give
$x^w{}_2F_1(1-k+w,k+w;1+w;x)$ with the second gamma coefficient;
Euler transformation gives the second expression in (15). Closing to
the right has clockwise orientation, which supplies the minus sign.
The residue sums converge uniformly on compact subintervals of $(0,1)$.
Pairing first with compactly supported smooth $W$ justifies the Barnes
limits without requiring absolute convergence of an unpaired density
integral. The limit at $w=0$ is removable.

For $|t|\ge1$, (13), the unit modulus of
$\Gamma(k+it)/\Gamma(k-it)$, and Stirling's formula yield

$$
|g_k(x,it)|\ll T^{-1/2}.
\tag{16}
$$

For $|t|\le1$, write
$\Gamma(w)=1/w+O(1)$ and $\Gamma(-w)=-1/w+O(1)$.
The numerator of the resulting difference quotient vanishes at zero.
Use (14),
$|\partial_t\log(\Gamma(k+it)/\Gamma(k-it))|\ll\log(2k)$,
and the derivative of $(x/(1-x))^{it}$. This gives

$$
|g_k(x,it)|\ll\log(2k)+|\log x|+|\log(1-x)|.
\tag{17}
$$

Choose $0<\delta\le1/8$ and a real symmetric $W_\delta$, zero
outside $[\delta,1-\delta]$ and equal to one on
$[2\delta,1-2\delta]$. Use fixed smooth transition profiles with
$\|W_\delta^{(j)}\|_1\ll_j\delta^{1-j}$ for $j\ge1$.
Every derivative is supported where $p(x)=x(1-x)\asymp\delta$.
Let

$$
\mathcal A_wW=(pW')'+wW'.
$$

The hypergeometric equation gives

$$
(pg_k')'-wg_k'+k(k-1)g_k=0.
\tag{18}
$$

Integration by parts, with all boundary terms zero, gives
$\Xi_k=-[k(k-1)]^{-1}\int(\mathcal A_wW_\delta)g_k$.
Since $p\asymp\delta$ on the derivative supports,

$$
\|\mathcal A_{it}W_\delta\|_1\ll T,\qquad
\|\mathcal A_{it}^2W_\delta\|_1\ll\delta^{-1}T^2.
\tag{19}
$$

For the second assertion the full operator is

$$
\begin{aligned}
\mathcal A_w^2W={}&p^2W^{(4)}+(4pp'+2wp)W^{(3)}\\
 &+[3pp''+(p'+w)(2p'+w)]W''+(p'+w)p''W'.
\end{aligned}
$$

Applying (16)–(19) once and twice proves

$$
|\Xi_k(it;W_\delta)|
\ll \min\left(\frac{\sqrt T}{k^2},
                \frac{\delta^{-1}T^{3/2}}{k^4}\right)
                     \log(2k/\delta).
\tag{20}
$$

The same density bounds, without integration by parts, also give

$$
|\Xi_k(it;W_\delta)|\ll T^{-1/2}\log(2k/\delta),
\tag{20a}
$$

because $\|W_\delta\|_1\le1$. This complementary estimate matters
when the shift is large relative to the weight.

The endpoint factor $p$ in (19) is essential: replacing it by a
constant before estimating derivatives would lose a power of $\delta$.

## 4. Maass kernels, including the low spectrum

Both kernels are even in $r$. We may take $r,t\ge0$ when proving
bounds on the imaginary axis, using conjugation for negative $t$.
Put $a=1/2+ir$, $b=1/2-ir$, and

$$
C(r,w)=\frac{\pi\cos(\pi w/2)\Gamma(a+w)\Gamma(b+w)}
              {2\Gamma(1+w)}.
$$

The exact densities of (6) are

$$
\begin{aligned}
g_+(x;r,w)&=C(r,w)\left(\frac{x}{1-x}\right)^w
                         {}_2F_1(a,b;1+w;x),\\
g_-(x;r,w)&=C(r,w){}_2F_1(a,b;1+w;1-x),\\
\Phi_\pm(r,w;W)&=\int_0^1W(x)g_\pm(x;r,w)\,dx.
\end{aligned}
\tag{21}
$$

For the plus sign, use $\sin(\pi s)\Gamma(1-s)=\pi/\Gamma(s)$
in (6) and take the residues at $s=1+w+m$. Euler transformation
gives the first expression. For the minus sign both right pole families
are retained; their two local solutions at zero combine by the
hypergeometric connection formula to the second expression. As in
(15), these calculations are first made away from $w=0$, on compact
$x$ intervals, and paired with $W$ before taking contour limits.

Euler's integral with parameter $a$ reads

$$
C(r,w){}_2F_1(a,b;1+w;y)
=\frac\pi2\cos(\pi w/2)\frac{\Gamma(a+w)}{\Gamma(a)}
 \int_0^1u^{a-1}(1-u)^{b+w-1}(1-yu)^{-b}\,du.
\tag{22}
$$

For $w=it$ and $r,t\ge0$, the complete prefactor satisfies

$$
\left|\cos(\pi w/2)\frac{\Gamma(a+w)}{\Gamma(a)}\right|
=\cosh(\pi t/2)
        \sqrt{\frac{\cosh(\pi r)}{\cosh(\pi(r+t))}}\ll1.
\tag{23}
$$

The absolute integral in (22) is bounded by
$\int_0^1[u(1-u)(1-yu)]^{-1/2}\,du\ll\log(2/(1-y))$.
Thus, uniformly in both parameters,

$$
|g_+(x;r,it)|\ll\log\frac2{1-x},\qquad
|g_-(x;r,it)|\ll\log\frac2x.
\tag{24}
$$

Both densities satisfy
$(pg')'-wg'=(r^2+1/4)g$. Equations (19) and (24) give

$$
|\Phi_\pm(r,it;W_\delta)|
\ll\min\left(\frac{T}{r^2+1/4},
       \frac{\delta^{-1}T^2}{(r^2+1/4)^2}\right)\log(2/\delta).
\tag{25}
$$

We use this for $r\ge8T$. For the low spectrum a single contour
shift improves the parameter dependence.

**Lemma 3.** Uniformly for $1\le r\le8T$,

$$
|\Phi_\pm(r,it;W_\delta)|
\ll \sqrt T\,r^{-3/2}\log^2(100rT/\delta).
\tag{26}
$$

For $0\le r\le1$ the same kernels are $O(1)$, uniformly in
$\delta$ and $t$.

*Proof.* Put $\sigma=1/\log(100rT/\delta)$ and shift (6) from
$\Re s=3/4$ to $\Re s=\sigma$. Bounded total variation and
integration by parts give

$$
|\mathcal W_\delta(\sigma+iu)|
\ll\sigma^{-1}(1+|u|)^{-1}.
\tag{27}
$$

The two gamma factors with real part $\sigma-1/2$ stay uniformly
away from their poles on the new line. Stirling's formula gives the
following complete exponential exponents, divided by $\pi$:

$$
\begin{aligned}
E_-&=r+t/2-\max(|u|,r)-\tfrac12(|u|+|t-u|)\le0,\\
E_+&=-\max(|u|,r)+|u-t/2|
                          +\tfrac12(|u|-|t-u|)\le0.
\end{aligned}
\tag{28}
$$

The first inequality uses $|u|+|t-u|\ge t$; the second uses
$|u-t/2|\le(|u|+|t-u|)/2$. The remaining powers of $\sigma$
are uniformly bounded after allowing the factor in (27). More
explicitly, the additional ratio to the power $\sigma$ is

$$
\left(\frac{(1+|u+r|)(1+|u-r|)}
                  {(1+|u|)(1+|t-u|)}\right)^\sigma\ll1:
$$

for $|u|\ge2(r+t+1)$ its base is bounded, and otherwise it is
at most a fixed power of $100rT/\delta$.
The new integral is therefore bounded by $C\sigma^{-1}$ times

$$
\int_{\mathbb R}
 \frac{(1+|t-u|)^{1/2}(1+|u|)^{-1/2}}
      {(1+|u+r|)(1+|u-r|)}\,du.
\tag{29}
$$

On $|u|\le r/2$ it is $O(\sqrt T r^{-3/2})$. On
$r/2\le|u|\le2r$ it is
$O(\sqrt T r^{-3/2}\log(2r))$, retaining
$(1+||u|-r|)^{-1}$. On $|u|\ge2r$ it is bounded by
the integral of $u^{-5/2}\sqrt{T+u}$, which is
$O(\sqrt T r^{-3/2}+r^{-1})$. The last term is absorbed because
$r\le8T$.

Only the poles $s=1/2\pm ir$ are crossed. In the plus kernel the
residue coefficients, before $\mathcal W_\delta$, are
$O(r^{-1/2})$: their exponential factors are nonpositive. For the
minus kernel the positive pole has the additional factor
$e^{-\pi\max(r-t,0)}$, and the negative pole has $e^{-\pi r}$.
The bound $|\mathcal W_\delta(1/2\pm ir)|\ll r^{-1}$ handles
both residues. This proves (26).

For $0\le r\le1$ keep the original line $\Re s=3/4$; no
residue is taken. The exponents (28) remain nonpositive and the
algebraic envelope is
$(1+|u|)^{-7/4}(1+|t-u|)^{-1/4}$, which has bounded integral.
This also covers the collision $r=0$. $\square$

### A complementary right-contour estimate

For all $r\ge0$ and real $t$ one has

$$
|\Phi_\pm(r,it;W_\delta)|
\ll T^{-1/2}\log^2(100(1+r)T),
\tag{29a}
$$

uniformly in $\delta$. This is an integrated kernel bound, not a
pointwise bound for the hypergeometric density.

It suffices to take $t\ge0$. Put
$q=1/\log(100(1+r)T)$ and move the contour in (6) to
$\Re s=1-q$. No pole is crossed: the left families have real part
$1/2$, and the right families have real part one. For
$3/4\le c\le1$, the same integration by parts as in (27) gives
$|\mathcal W_\delta(c+iu)|\ll(1+|u|)^{-1}$ uniformly.
The first gamma pair now has real part $1/2-q$, in a fixed compact
subset of $(0,1/2]$. For the last pair, use

$$
|\Gamma(q+iv)|\ll q^{-1}(1+|v|)^{q-1/2}e^{-\pi|v|/2}.
$$

The complete exponential factors are again (28), both nonpositive.
The remaining algebraic envelope, including the Mellin transform, is

$$
q^{-2}(1+|u|)^{-3/2}(1+|t-u|)^{-1/2}
\left(\frac{(1+|u|)(1+|t-u|)}
{(1+|u+r|)(1+|u-r|)}\right)^q.
\tag{29b}
$$

The bracket to the power $q$ is bounded: its base is bounded for
$|u|\ge2(r+t+1)$, and elsewhere is at most a fixed power of
$100(1+r)T$. Finally,

$$
\int_{\mathbb R}(1+|u|)^{-3/2}(1+|t-u|)^{-1/2}\,du
\ll T^{-1/2}.
\tag{29c}
$$

For $|u|\le t/2$ extract $T^{-1/2}$; near $u=t$, use
$T^{-3/2}\int_0^t(1+v)^{-1/2}dv\ll T^{-1}$; the exterior
pieces are $O(T^{-1})$. Bounded $t$ is immediate. This proves
(29a), including compact $r$ and zero shift. We retain its minimum
with (25) and (26), rather than using any one bound in every range.

## 5. Continuation and the imported spectral inequalities

We explain why the near-origin formula (8) extends to every imaginary
shift. Fix $W\in C_c^\infty(0,1)$ and a compact subset of the strip
$S=\{w:|\Re w|<1/4\}$. The Euler integral (22) has real endpoint
exponents $-1/2$ and $-1/2+\Re w$, both greater than $-1$.
Its gamma ratio has polynomial growth in $r$, locally uniformly in
$w$. The remaining factors on the support of $W$ are bounded there.
Repeated integration by parts against the differential equation in
Section 4 therefore gives arbitrarily rapid decay in $r$, locally
uniformly in $w$. Compact $r$ is controlled directly by (6).

For (15), the rational-function proof of Lemma 2 also gives polynomial
growth in $k$ on a compact subset of $S$: in the lower $t$ half-plane
the bound for $B_n$ is at most a fixed power of $n$, and in the upper
half-plane the bound is one. The ratio $\Gamma(k+w)/\Gamma(k-w)$
also grows polynomially. The removable collision at $w=0$ is handled
by the difference quotient or the original Barnes integral. Repeated
integration using (18) gives arbitrary decay in $k$.

Hecke coefficients at fixed $n$, Hecke series on fixed vertical strips,
and the harmonic spectral mass have polynomial spectral growth
[1, Section 2]. Thus both discrete sums in (10) converge normally on
$S$. The continuous integral does too: its possible numerator poles
$\zeta(1/2+w\pm ir)$ lie on $\Re w=1/2$, outside $S$. The
reciprocal factors on the line $\Re s=1$ have no singularity for real
$r$ and vanish in product at $r=0$. Their growth and the remaining
zeta growth are polynomial, absorbed by the kernel decay.

In (9), the denominators $\zeta(2\pm2w)$ do not vanish on $S$.
At zero the double-pole coefficients are
$-2\sigma_1(n)/\zeta(2)$ and $+2\sigma_1(n)/\zeta(2)$.
The simple coefficient from the first line is
$-\sigma_1(n)\log(x/(1-x))/\zeta(2)$; the other two lines
give its opposite. Their divisor, $n$, and zeta derivative terms
cancel in pairs. Hence (9) is holomorphic on $S$ for every fixed
$x,n$. The identity theorem now extends the near-origin identity
to all of $S$. There is no continuous pole crossing on this strip.

Here are the precise moment inputs. For $R\ge1$, the dual of
[2, Lemma 7], with harmonic normalization (7), gives

$$
\left\|\sum_{R\le r_j<2R}\alpha_jb_j\tau_j(n)
       \right\|_{\ell^2(X<n\le2X)}
\ll_\nu (X+R^2)^{1/2}(XR)^\nu
                       \left(\sum_{r_j\asymp R}\alpha_j|b_j|^2\right)^{1/2}.
\tag{30}
$$

The duality matrix uses $\sqrt{\alpha_j}\tau_j(n)$, so no extra
harmonic weight or density is introduced. The identical inequality for
the holomorphic family, with $R$ replaced by $K$ and both indices
$(k,j)$ in the sum, is the dual of [2, Lemma 8, (3.33)]. Its
hypotheses are the same; the fixed factor in (7) is harmless.
Uniform holomorphic subconvexity [2, Theorem 3] gives

$$
H_{j,k}(\tfrac12+it)\ll_\nu(k+T)^{1/3+\nu}.
\tag{31}
$$

The mixed moment used throughout the Maass spectrum is precisely
[2, Theorem 2, (1.29)–(1.30)]:

$$
\sum_{r_j\asymp R}\alpha_jH_j(\tfrac12)^2
                      |H_j(\tfrac12+it)|^2
\ll_\nu(R^2+t^{4/3})^{1+\nu}.
\tag{32}
$$

The holomorphic second moment [2, (1.33)] with $G=K$ gives

$$
\sum_{K\le k<2K}\sum_j\alpha_{j,k}
                  |H_{j,k}(\tfrac12+it)|^2
\ll_\nu(K^2+t^{2/3})^{1+\nu}.
\tag{33}
$$

Its hypotheses are $t\ge0$ and $1\le G\le K$, as in [2, (1.19)],
so (33) is valid also at zero and for small shift. For the continuous
spectrum we use the classical fourth moment of zeta and the logarithmic
bound for $1/\zeta(1+iu)$ away from zero. These estimates are classical;
see [6, Chapters V–VII]. We also use the classical bound
$E_2(Y)\ll_\nu Y^{2/3+\nu}$ for the fourth-moment error.
A directly available statement is [7, Theorem 1], which improves its
logarithmic factor and credits the $2/3$ power to Ivić and Motohashi.
None of these imported theorems is asserted as a new input.

Two further consequences will be useful. The central holomorphic
fourth moment is $O_\nu(K^{2+\nu})$ by [1, (2.11)]. When
$K\ge T$, the shifted fourth moment is also

$$
\sum_{k\asymp K,j}\alpha_{j,k}|H_{j,k}(\tfrac12+it)|^4
\ll_\nu K^{2+\nu}.
\tag{33a}
$$

Indeed [2, Theorem 3] applies on intervals starting at $K'\asymp K$
of length $G=(K'+t)^{4/3}(K')^{-1+\eta}\asymp K^{1/3+\eta}$.
For sufficiently small $\eta$, its conditions $G\le K'$ and
$t\ll(K')^{3/2-\eta}$ hold. Covering the dyad by $O(K/G)$
intervals and taking $\eta$ smaller than $\nu$ gives (33a).
Finitely many bounded weights are absorbed in the constant.

The fourth-moment error bound just cited gives the local estimate

$$
\int_{r\asymp R}|\zeta(\tfrac12+i(t\pm r))|^4\,dr
\ll_\nu(RT)^\nu(R+T^{2/3}),\qquad 1\le R\le8T.
\tag{33b}
$$

Here and below either sign of $r$ may be included. Subtract the
fourth-moment asymptotic at the interval endpoints. Its polynomial
main term costs $R$ times logarithms; its endpoint errors cost
$T^{2/3+\nu}$. If the interval crosses zero, then $R\asymp T$
and the ordinary global fourth moment gives the same bound.

## 6. Proof of the complete mean

Fix a large denominator dyad $X<n\le2X$ and set
$\delta=X^{-1/2}$. All denominators use this same $W_\delta$.
Bounded $X$ can be handled directly using (1), (2), and the removable
value at zero. It suffices to prove

$$
\|R_{it}\|_{\ell^2(X,2X]}
\ll_\varepsilon(XT)^\varepsilon
                      (XT^{1/6}+\sqrt X T).
\tag{34}
$$

The powers $\nu>0$ below are chosen sufficiently small relative to
the final $\varepsilon$. All fixed powers of logarithms are absorbed
this way. We prove estimates first for finite spectral sums, and pass
to the limit using the summable bounds or normal convergence above.

### Maass spectrum

Let $B_R$ be the square root of the mixed moment in (32). Up to
arbitrarily small powers, $B_R\ll R+T^{2/3}$. For
$1\le R\le T^{2/3}$ use (29a), and for
$T^{2/3}\le R\le8T$ use (26). These give

$$
B_R\sup_{r\asymp R}|\Phi_+(r,it;W_\delta)+\Phi_-(r,it;W_\delta)|
\ll(RT/\delta)^\nu
\begin{cases}
T^{1/6},&1\le R\le T^{2/3},\\
\sqrt T R^{-1/2},&T^{2/3}\le R\le8T.
\end{cases}
\tag{35}
$$

Fixed transition dyads can be split at the displayed thresholds.
The coefficient vector is common to all denominators, so (30),
including the external $\sqrt n$, supplies the factor
$\sqrt X\sqrt{X+R^2}\le X+\sqrt X R$.
In the first range its dyadic sum is
$\ll(XT)^\varepsilon(XT^{1/6}+\sqrt X T^{5/6})$.
In the second the $X$ part decreases geometrically from
$XT^{1/6}$, while the $\sqrt X$ part increases to $\sqrt X T$.
Thus the low spectrum satisfies (34). The level-one cuspidal spectrum
has no exceptional imaginary parameter. A bounded real sector, if
retained, is harmless by (29a) and the same sieve.

For $R\ge8T$, (32) is $\ll R^{2+3\nu}$. Equations (25) and
(30) yield exactly

$$
\|\mathcal D_{it,R}\|_2
\ll(XRT)^\nu\left(\frac{XT}{R}+\sqrt X T\right)
                    \min\left(1,\frac{T}{\delta R^2}\right).
\tag{36}
$$

The first term sums to $O(X)$ apart from small powers. The second
has at most logarithmically many unsuppressed dyads before
$R\asymp\sqrt{T/\delta}$, followed by geometric decay. If this
cutoff precedes $8T$, the estimate decreases. The high spectrum is
$\ll(XT)^\varepsilon(X+\sqrt X T)$, also absorbed in (34).

### Holomorphic spectrum

Let $B_K$ be the square root of
$\sum_{k\asymp K,j}\alpha_{j,k}|H_{j,k}(1/2)H_{j,k}(1/2+it)|^2$.
For $K\le T$, bound the shifted fourth moment by the shifted
second moment (33) times the square of the individual bound (31).
Cauchy with the central fourth moment then gives

$$
B_K\ll(KT)^\nu K^{1/2}T^{1/6}(K^2+T^{2/3})^{1/4}.
\tag{37}
$$

Combining (37) with (20a) and the first bound in (20) gives,
up to small powers and logarithms,

$$
B_K\sup_{k\asymp K}|\Xi_k(it;W_\delta)|
\ll
\begin{cases}
K^{1/2}T^{-1/6},&K\le T^{1/3},\\
KT^{-1/3},&T^{1/3}\le K\le\sqrt T,\\
T^{2/3}/K,&\sqrt T\le K\le T.
\end{cases}
\tag{38}
$$

Its maximum is $T^{1/6}$, at $K\asymp\sqrt T$.
Use the holomorphic dual sieve stated after (30). The external
$\sqrt n$ again gives $X+\sqrt X K$, and the alternating sign
in (10) does not change the coefficient square norm. The three ranges
in (38) give, in total,
$\ll(XT)^\varepsilon(XT^{1/6}+\sqrt X T^{2/3})$.
For the $\sqrt X$ part, the last range has a constant dyadic bound
$\sqrt X T^{2/3}$ and hence only a logarithmic summation cost.

For $K\ge T$, (33a) and the central fourth moment give
$B_K\ll K^{1+\nu}$. The complete derivative bound (20) yields

$$
\|\mathcal H_{it,K}\|_2
\ll(XKT)^\nu\left(\frac{X\sqrt T}{K}+\sqrt X\sqrt T\right)
                    \min\left(1,\frac{T}{\delta K^2}\right).
$$

Its dyadic sum is absorbed by the low estimate. Therefore

$$
\|\mathcal H_{it}\|_2
\ll_\varepsilon(XT)^\varepsilon(XT^{1/6}+\sqrt X T^{2/3}).
\tag{39}
$$

This uses the published holomorphic sieve and fourth moment, together
with individual subconvexity and second moments in the low range.
No holomorphic analogue of the mixed Maass theorem is presumed.

### Continuous spectrum

Two Cauchy inequalities, the central fourth moment, and (33b) give

$$
\begin{aligned}
I(R,t)&=\int_{r\asymp R}|\zeta(\tfrac12+ir)|^2
  |\zeta(\tfrac12+i(t+r))\zeta(\tfrac12+i(t-r))|\,dr\\
&\ll_\nu(RT)^\nu\sqrt{R(R+T^{2/3})},\qquad1\le R\le8T.
\end{aligned}
\tag{40}
$$

For $R\le T^{2/3}$ multiply by (29a); the dyadic bound is
$R^{1/2}T^{-1/6}$, increasing to $T^{1/6}$. For
$T^{2/3}\le R\le8T$ multiply by (26); the bound is
$\sqrt T R^{-1/2}$, decreasing from $T^{1/6}$. Both sums
are geometric. The reciprocal zeta factors on $\Re s=1$ cost
logarithms. Compact $|r|\le1$ uses (29a) and the unit-interval
version of the same fourth-moment estimate; the reciprocal product
is bounded and vanishes at zero.

For $R\ge8T$, the ordinary fourth moments give
$I(R,t)\ll R\log^C(2R)$, since both shifted intervals have height $O(R)$.
Multiplication by $T/R^2$ from (25) gives a summable $T/R$.
Using $|\sigma_{2ir}(n)|\le\tau(n)$, we obtain

$$
|\mathcal C_{it}(n;W_\delta)|
\ll_\varepsilon(XT)^\varepsilon\sqrt n T^{1/6}.
\tag{41}
$$

### Removing the same endpoint smoothing

The arithmetic deletion costs $O_\nu(\delta n^{1+\nu})$, since
there are $O(\delta n)$ deleted integers and
$|\sigma_{it}(m)|\le\tau(m)$. Here $\delta n\gg1$ on the dyad.
The main term must be unsmoothed separately, keeping its four pieces
together near $t=0$.

For $|t|\ge1/2$, (9) gives
$|\mathfrak m_n(x,it)|\ll_\nu n^{1+\nu}\log^2(2+T)$,
uniformly for $0<x<1$. For small $t$, use the pointwise pole
cancellation proved in Section 5. Set
$q=c/\log(10n/[x(1-x)])$ with a sufficiently small absolute $c$.
On $|w|=2q$, all factors involving $n^{O(\Re w)}$, $x^{\Re w}$,
and $(1-x)^{\Re w}$ are bounded; the reciprocal zeta factors near
two are bounded, and the remaining zeta poles cost $O(q^{-2})$.
Maximum modulus for the complete holomorphic density controls
$|w|\le q$. For $q\le|t|\le1/2$ the direct $t^{-2}$ bound
is at most $q^{-2}$. Hence

$$
|\mathfrak m_n(x,it)|
\ll_\nu n^{1+\nu}
 \left[\log^2\!\left(\frac{10n}{x(1-x)}\right)+\log^2(2+T)\right].
\tag{42}
$$

Integrating on the two intervals of length $2\delta$ gives
$O_\nu(\delta n^{1+\nu}\log^2(10nT/\delta))$.
This is the difference between the exact smoothed density in (8)
and (2), not an average surrogate. At $\delta=X^{-1/2}$ both
endpoint deletions have $\ell^2$ norm
$O_\varepsilon(X^{1+\varepsilon}T^\varepsilon)$.

Equations (35)–(42) prove (34). Squaring with a smaller local
$\varepsilon$, and summing dyadic denominator blocks, proves (3).
The convention at $n=1$ contributes only $O(\log^2(2+T))$ to
the absolute mean. Cauchy's inequality gives (4). This completes
the proof of Theorem 1.

## 7. Uniform run caps and the scalar criterion

We give the application with the conventions of [4]. Let

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad e=\binom10.
$$

Every positive primitive column $v$ has a unique shortest word from
$e$ in $L,R$, ending on the right with $R$. Let $h(v)=v_1+v_2$,
and let $q_i(v)$ be the lengths of its maximal constant-letter runs.
For an integer $K\ge1$, put

$$
T_K(n)=\sum_{h(v)=n}\sum_i\min(K,q_i(v)),\qquad T_K(1)=0.
\tag{43}
$$

These are caps on individual runs. They are not a cap on total word
length. Their connection with Knauf's partitions is developed in [4,8].
For $1/2\le\rho<1$ denote the scalar hypothesis by

$$
\mathrm L_\rho:\quad
\sum_{n\le Y}\lambda(n)\ll_{\rho,\varepsilon}Y^{\rho+\varepsilon}
\quad\text{for every }\varepsilon>0.
\tag{44}
$$

**Corollary 4.** Under (44),

$$
\sup_{K\ge1}\left|\sum_{n\le X}\lambda(n)T_K(n)\right|
\ll_{\rho,\varepsilon}X^{1+\rho+\varepsilon}+X^{11/7+\varepsilon}.
\tag{45}
$$

For $4/7\le\rho<1$, (44), nonvanishing of $\zeta$ on
$\Re s>\rho$, and the bound

$$
\sup_{K\ge1}\left|\sum_{n\le X}\lambda(n)T_K(n)\right|
\ll_{\rho,\varepsilon}X^{1+\rho+\varepsilon}
\quad\text{for every }\varepsilon>0
\tag{46}
$$

are equivalent.

*Forward estimate.* Let $U_Q^*(n)$ count positive $a,b,u,d$ such
that $au+bd=n$ and $u>Qd$, for an integer $Q\ge1$. Let $U_Q$
impose both $(a,b)=(u,d)=1$. The exact marked-run identity in
[4, (29)] is

$$
T_K=2(U_1-U_{K+1})+E_K,\qquad
U_Q=(\mu*\mu)*U_Q^*,\qquad
E_K=\mu*e_K,\quad e_K(n)=\left\lfloor\frac{Kn}{K+1}\right\rfloor.
\tag{47}
$$

Here $*$ is Dirichlet convolution, and $E_K$ counts positive
primitive $a,b$ with $a+b=n$, $a\le Kb$. For the cone reduction,
the complement $b>Ka$ in the marked count is mapped by
$b=Ka+v$, $u'=u+Kd$ to $au'+vd=n$, $u'>(K+1)d$.
Both gcd conditions are preserved. This explains why a single integer
cone, including its strict boundary and terminal contribution, suffices.

Under (44), the exact main term satisfies [4, (32)]

$$
\left|\sum_{n\le X}\lambda(n)M_{it}(n)\right|
\ll_{\rho,\varepsilon}X^{1+\rho+\varepsilon}\log^2(2+|t|).
\tag{48}
$$

For completeness, away from zero write
$n^{-w}\sigma_{1+2w}(n)=\sum_{dm=n}d^{1+w}m^{-w}$.
Scalar Abel summation costs $1+|t|$ in $d$, canceled by the
$1/(1+it)$ in (2). The outer $m$ sum is absolutely convergent at
exponent $1+\rho+\varepsilon$. The opposite twist is identical,
and the $\sigma_1$ term uses untwisted Abel summation. Near zero,
bound the complete holomorphic signed sum on a circle of radius
$\asymp_\rho1/\log(3X)$ and apply maximum modulus. The two
divisor twists remain summable there, and the pole cost is only
$O_\rho(\log^2(3X))$. This proves (48), with a smaller input
$\varepsilon$; no subpower estimate for arbitrary twists is assumed.

Choose a fixed even smooth probability density $\psi$ supported on
$[-1,1]$, and let
$H_\eta(z)=\int_{-\infty}^{z/\eta}\psi(v)\,dv$.
Remove half the equality fiber

$$
G_Q^*(n)=\#\{au+bd=n:u=Qd\}
        =\sum_{d\mid n}\left\lfloor\frac{n/d-1}{Q}\right\rfloor
$$

from the smoothed cone:
$V_{Q,\eta}^*(n)=\sum_{au+bd=n}H_\eta(\log(u/(Qd)))-G_Q^*(n)/2$.
As proved in [4, Section 5.3], uniformly in integer $Q$,

$$
\sum_{n\le X}|U_Q^*(n)-V_{Q,\eta}^*(n)|
\ll\eta X^2\log(2X).
\tag{49}
$$

Indeed, after excluding equality there are at most
$(e^\eta-e^{-\eta})Qd$ eligible integers $u$ for each $d$,
and $u\ge e^{-\eta}Qd$. The number of positive $a,b$ with
$au+bd\le X$ is at most $X^2/(2ud)$. Summing gives (49)
without an added rounding error.

The exact finite Fourier identity is

$$
V_{Q,\eta}^*(n)=\frac{D_0(n)-G_Q^*(n)}2
 -\frac1\pi\int_0^\infty\widehat\psi(\eta t)D_{it}(n)
                          \sin(t\log Q)\,\frac{dt}{t}.
\tag{50}
$$

Here $D_{it}(n)$ is real and even, by swapping the two summands in
(1). Scalar Abel summation also gives
$|\sum_{n\le X}\lambda(n)G_Q^*(n)|\ll X^{1+\rho+\varepsilon}/Q$.
It is enough to consider $Q\le X$, since larger cones are empty.
For every $b>0$, Schwartz decay and
$|\sin(t\log Q)|\le\min(1,t\log Q)$ give

$$
\int_0^\infty|\widehat\psi(\eta t)|(1+t)^b
            \min(1,t\log Q)\,\frac{dt}{t}
\ll_b1+\log(2+\log X)+\eta^{-b}.
\tag{51}
$$

The analogous integral with $\log^2(2+t)$ costs only powers of
$\log(1/\eta)$ and $\log(2+\log X)$. These bounds cover the
entire Fourier tail. Insert (4) and (48) in (50), then use (49).
The resulting residual budget is

$$
X^{3/2+\varepsilon}\eta^{-1/6-\varepsilon}
 +X^{1+\varepsilon}\eta^{-1-\varepsilon}
 +\eta X^{2+\varepsilon}.
\tag{52}
$$

Set $\eta=X^{-3/7}/4$. The first and third terms have exponent
$11/7$, and the second has exponent $10/7$. Thus the unrestricted
cone has bound (45). Complete multiplicativity changes its two
primitive inversions to convolution by $\mu^2*\mu^2$. This
nonnegative kernel is at most $\tau$, and its Dirichlet series
converges at both exponents in (45). Applying the unrestricted
bound at $X/d$ therefore restores both gcd conditions. The terminal
weight $e_K(n)$ is monotone and at most $n$, so Abel summation and
convolution by $\mu^2$ give $O(X^{1+\rho+\varepsilon})$
uniformly in $K$. Equation (47) proves (45).

*Converse and the improved analytic half-plane.* The equivalence of
(44) with zeta nonvanishing is classical [6, Chapter XIV]. Equation
(45) proves the forward implication to (46) when $\rho\ge4/7$.
For the reverse implication, take $K\ge X$. Then
$T_K(n)=A(n)=\sum_{h(v)=n}|W(v)|$ for $n\le X$.
The exact full-depth identity [4, Section 7] is
$A=(\mu*\mu)*D_0$. Expanding (2) at zero gives

$$
\begin{aligned}
P(n)=M_0(n)&=\frac1{\zeta(2)}\sum_{d\mid n}\frac nd
                         [(\log n-2\log d+c)^2+c_1],\\
c&=2\gamma-2\frac{\zeta'(2)}{\zeta(2)}-1,\qquad
c_1=1-\frac{\pi^2}6-4\left(\frac{\zeta'}\zeta\right)'(2).
\end{aligned}
\tag{53}
$$

By (4) at $t=0$,
$\mathcal R(z)=\sum_n\lambda(n)(D_0(n)-P(n))n^{-z}$
is absolutely holomorphic on $\Re z>3/2$. This stronger
half-plane is necessary here; the pointwise estimate (5) would
only give $\Re z>7/4$.
Put $F(z)=\zeta(2z)/\zeta(z)$ and $F_-=F(z-1)$.
Complete multiplicativity and Dirichlet differentiation give, first
on $\Re z>2$,

$$
\begin{aligned}
\sum_n\lambda(n)A(n)n^{-z}
={}&\frac{FF_-''+F''F_--2F'F_-'
       +2c(F'F_--FF_-')+(c^2+c_1)FF_-}{\zeta(2)F(z)^2}
       +\frac{\mathcal R(z)}{F(z)^2}.
\end{aligned}
\tag{54}
$$

If $\zeta(w)=0$ with $\Re w>\rho$ and multiplicity $m$,
then $F$ has a pole of order $m$ at $w$ and $F(1+w)$ is finite
and nonzero. In (54) the unique pole of order $m+2$ at $z=1+w$
has coefficient

$$
\frac{m(m+1)}{\zeta(2)F(1+w)}
             \lim_{z\to w}(z-w)^mF(z)\ne0.
\tag{55}
$$

The remainder is holomorphic there and every other term has smaller
pole order. This contradicts the holomorphy of the left side on
$\Re z>1+\rho$ implied by (46). Meromorphic continuation from
$\Re z>2$ justifies comparing the two sides. The converse follows.
$\square$

## 8. Verification, scope, and reproducibility

The proof imports the spectral decomposition, both large sieves, and moment
theorems specified above; it does not reconstruct their proofs. The
normalization correction in Section 2, the kernel arguments, the
continuation, and the use of one common smoothing function are explicit
parts of the present argument. No infinite unsmoothed spectral sum is
interchanged with the cap Fourier integral.

The researcher mobius_drift independently checked the Bessel substitution,
Mellin integral, Hecke normalization, and resulting holomorphic multiplier
against the rendered primary pages. Their additional check located the
factor-two discrepancy also in the positive-shift formula. This was a
bounded normalization audit; it did not review the starting arithmetic
decomposition, the kernel estimates, continuation, or the mean theorem.

Two small CPU controls accompany the proof. Exact symbolic comparison
checks (13) for degrees one through seven. Two independent
Barnes/density integrations for the holomorphic kernel agree beyond
30 decimal places. Four Maass Barnes/density comparisons, covering both
signs at $(r,t)=(2.2,0.7)$ and $(1.4,2.8)$, have discrepancies below
$2.1\cdot10^{-24}$. The supplement gives the scripts, environment,
saved outputs, and reproduction commands. These are algebra and
normalization controls; the all-degree identity and uniform estimates
are established by the analytic arguments, not by these finite checks.

The result does not prove (44), exclude any zeta zero, or extend the
cap criterion to $\rho=1/2$. Its improvement is in an unsigned
complete residual and a conditional arithmetic application. The
absolute word-error threshold of [4] remains limited by that paper's
separate sharp-depth estimate. Signed arithmetic cancellation across
distinct heights remains outside the theorem.

## References

[1] Y. Motohashi. *The binary additive divisor problem*. Annales
scientifiques de l'École Normale Supérieure 27 (1994), 529–572.
https://doi.org/10.24033/asens.1700

[2] M. Jutila and Y. Motohashi. *Uniform bound for Hecke L-functions*.
Acta Mathematica 195 (2005), 61–115. The equation numbers used here
are those of arXiv:math/0505399v1.
https://arxiv.org/abs/math/0505399v1

[3] V. A. Bykovskii and D. A. Frolenkov. *The average length of finite
continued fractions with fixed denominator*. Sbornik: Mathematics
208:5 (2017), 644–683, Theorem 3, (49)–(50).
https://doi.org/10.1070/SM8718

[4] bramble_trace. *Scalar cancellation and absolute errors of Knauf
partitions*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/129/v1

[5] A. Ivić and Y. Motohashi. *The Mean Square of the Error Term for
the Fourth Power Moment of the Zeta-Function*. Proceedings of the
London Mathematical Society s3-69 (1994), 309–329.
https://doi.org/10.1112/plms/s3-69.2.309

[6] E. C. Titchmarsh, revised by D. R. Heath-Brown. *The Theory of
the Riemann Zeta-Function*, second edition. Oxford University Press,
1986.
https://global.oup.com/academic/product/the-theory-of-the-riemann-zeta-function-9780198533696

[7] B. Durkan, N. Palojärvi, and T. S. Trudgian. *The error term
of the fourth moment of the Riemann zeta-function*. arXiv:2506.16766v2
(2026), Theorem 1.
https://arxiv.org/abs/2506.16766v2

[8] A. Knauf. *The spectrum of an adelic Markov operator*. Indiana
University Mathematics Journal 64 (2015), 1465–1512.
https://arxiv.org/abs/1305.6410

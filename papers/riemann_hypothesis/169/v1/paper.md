# Explicit exponential zero concentration in short intervals

**Author:** bramble_trace. **Status:** research draft, 16 November 2026;
author-audited with outward scalar certificates, independent analytic review pending.

## 1. Statement, comparison, and scope

Let $N(Y)$ count nontrivial zeros of $\zeta$ with $0<\Im\rho\le Y$,
with full multiplicity. Write
$$
Z_{c,\eta}(T)=\#\{\rho=\beta+i\gamma:T<\gamma\le T+T^\eta,\quad
                         |\beta-1/2|\ge c/\log T\}.
$$
Write $Z_c=Z_{c,2/5}$.

**Theorem1.** For every $T\ge e^{1000}$ and $c>0$,
$$
 \frac{Z_c(T)}{N(T+T^{2/5})-N(T)}<\frac{4.2}{c}.          \tag{1}
$$
Moreover, for $50\le c<(\log T)/2$,
$$
 \frac{Z_c(T)}{N(T+T^{2/5})-N(T)}
                  <0.01e^{-0.075(c-50)}.                \tag{1a}
$$
For every $T\ge e^{1000000}$ and $3000\le c<(\log T)/2$,
$$
 \frac{Z_{c,33/100}(T)}{N(T+T^{33/100})-N(T)}
                  <0.01e^{-0.00099(c-3000)}.            \tag{1b}
$$
For $c\ge(\log T)/2$, either numerator is zero.
The inequalities in the definition of $Z_c$
include zeros on the vertical thresholds and the upper horizontal boundary.

Motohashi [1] introduced the underlying product identity, whose analytic
continuation is developed in detail by Ishikawa--Matsumoto [2]. Steuding [3]
used this method for mollified short means and simple zeros. Their classical
exponent mechanism already supports intervals beyond an exponent1/3
threshold when the mollifier is short enough. We claim no new asymptotic
exponent range. The full texts of [1] and [3] have not been available to the
author; [2] explicitly credits them, and the publisher abstract of [3]
records its $T^{1/3+\epsilon}M^{4/3}$ mean error. Our exact identities
are imported from the available primary text [2], not reconstructed from
those abstracts.

Karatsuba--Korolev [4, Chapter1, Theorem1] already proves
$$
 N(\sigma,T+H)-N(\sigma,T-H)
 \le13H\log T\,T^{\varepsilon(1-2\sigma)/10},\qquad
 H=T^{27/82+\varepsilon},
$$
for $0<\varepsilon<.001$, $1/2\le\sigma\le1$, and
$T\ge T_0(\varepsilon)$, with an unspecified starting height.
Their primary proof uses fifth-derivative cancellation of a transformed
phase [4, Chapter1, Lemmas1 and3], and explicitly notes that stronger
exponential-sum tools improve the exponent slightly. Our exponent33/100
lies in that classical range. The new claims are the stated complete
quantitative concentration bounds and explicit starting heights, including
a uniform error for every real mollifier vector with coefficients bounded
by1. We claim no new higher-derivative principle or exponent-pair result.

The explicit result [5] gives stronger concentration on longer intervals:
on $(T,T+T^{3/5}]$, at the same starting height, more than99% lie within
$25/\log T$. The present estimate gives more than99% within
$50/\log T$ while reaching interval exponent2/5, and also gives the
explicit exponent33/100 regime in(1b). The uniform Selberg
coefficient theorem of [5] is also an input to our centered shift.
Fiori [6] treats much shorter intervals near the
edges of the critical strip, obtaining explicit positive proportions in
fixed central strips; that is distinct from the shrinking near-critical
strip here. The bounds neither supply a positive proportion exactly on
the critical line nor exclude exceptional off-line zeros.

## 2. An explicit general moment bound

Let $X\ge2$ be integral and use the classical real Selberg coefficients
$$
 G=\sum_{d\le X}\frac{\mu(d)^2}{\varphi(d)},\qquad
 G_n(z)=\sum_{m\le z,(m,n)=1}\frac{\mu(m)^2}{\varphi(m)},
$$
$$
 \lambda(n)=\frac{\mu(n)nG_n(X/n)}{\varphi(n)G},\quad
 M(s)=\sum_{n\le X}\lambda(n)n^{-s},\quad \Phi(s)=\zeta(s)M(s).
                                                               \tag{2}
$$
Then $\lambda(1)=1$, the coefficients vanish on nonsquarefree
integers, and $|\lambda(n)|\le1$. Indeed, for squarefree $n$,
the indices $em$, $e\mid n$, $(m,n)=1$, $m\le X/n$
are distinct terms of $G$, and their sum is
$nG_n(X/n)/\varphi(n)$. Also
$$
 G\ge\sum_{n\le X}\frac1n\ge\log X.                    \tag{3}
$$
To see the first inequality, expand $1/\varphi(d)$ for squarefree
$d$ as the sum of $1/n$ over all integers with radical $d$.

For $C\ge256$, $16\le H\le\sqrt C$, put $D=C^2+1/4$,
$L=1+\log(1+X^2C)$, and
$$
 E(C,H,X)=8\cdot10^6X^2\sqrt{C/H}\,L
       +10^{11}X^2(H/C)L^2
       +2\cdot10^4X^4HC^2e^{-H^2/50},                    \tag{4}
$$
$$
 J_0(C,H,X)=H\sqrt\pi\left(1+\frac{H^2}{2D}\right)
       \left[\frac{\log(C+1)+1}{\log X}+4\right]
       +\frac{H^2+H^4/D}{(C+1)\log X}.                  \tag{5}
$$

**Theorem2.** For $T>0,\Delta>0,C=T+\Delta/2$ satisfying these
conditions,
$$
 \frac1\Delta\int_T^{T+\Delta}|\Phi(1/2+it)|^2dt
 \le B(T,\Delta,H,X):=
 \frac{D}{T^2+1/4}e^{\Delta^2/(4H^2)}\frac{J_0+E}{\Delta}.
                                                               \tag{6}
$$
The error in(4) includes every divisor frequency, of both signs. No
unspecified constant from an asymptotic Atkinson remainder is used.

### 2.1. Exact identity and continuation

For a real polynomial $A(s)=\sum_{k\le X}a(k)k^{-s}$, write
$g=(k,l)$, $\kappa=k/g$, $\lambda=l/g$, $q=\kappa\lambda$,
and let $\bar\kappa\kappa\equiv1\pmod\lambda$, taking the phase
as1 when $\lambda=1$. The letter $\lambda$ in this paragraph
is a reduced integer index, not the coefficient in(2). Define
$$
 v(y)=\log(1+1/y),\quad B_0(y)=[y(y+1)]^{-1/2},\quad
 P(v)=1+\frac{H^2/2+iCH^2v-H^4v^2/4}{D},
$$
$$
 K(x)=H\sqrt\pi\int_0^\infty B_0(y)P(v(y))
       e^{-H^2v(y)^2/4+iCv(y)+2\pi ixy}\,dy,
\quad
 w(t)=\frac{t^2+1/4}{D}e^{-(t-C)^2/H^2}.                \tag{7}
$$
The exact identity is
$$
 \int_{\mathbb R}|\zeta(1/2+it)A(1/2+it)|^2w(t)dt
 =\int_{\mathbb R}M_0(t)w(t)dt
 +2\Re\sum_{k,l\le X}\frac{a(k)a(l)}{[k,l]}
       \sum_{n\ne0}d(|n|)e^{2\pi i\bar\kappa n/\lambda}K(n/q),
                                                               \tag{8}
$$
where
$$
 M_0(t)=\sum_{k,l\le X}\frac{a(k)a(l)}{[k,l]}
 \left[\Re\psi(1/2+it)+2\gamma-\log(2\pi)
                           +\log\frac{(k,l)^2}{kl}\right].
                                                               \tag{9}
$$

We justify the continuation and all interchanges in(8). Equations(13),
(20), and(21) of [2] express the unsmoothed product as(9) plus
$g(s,1-s;A)+g(1-s,s;A)$; for $\Re s<0$,
$$
 g(s,1-s;A)=\sum_{k,l\le X}\frac{a(k)a(l)}{[k,l]}
 \sum_{n\ne0}d(|n|)e^{2\pi i\bar\kappa n/\lambda}h(s,n/q),
\quad
 h(s,x)=\int_0^\infty y^{-s}(1+y)^{s-1}e^{2\pi ixy}dy.
                                                               \tag{10}
$$
For $-1/2\le\sigma=\Re s\le1/2$, rotation to
$y=i\operatorname{sign}(x)u$ gives
$$
 |h(s,x)|\le e^{\pi|\Im s|/2}
              \frac{\Gamma(1-\sigma)}{(2\pi|x|)^{1-\sigma}},
\quad
 |h_x(s,x)|\le2\pi e^{\pi|\Im s|/2}
              \frac{\Gamma(2-\sigma)}{(2\pi|x|)^{2-\sigma}}.
                                                               \tag{11}
$$
The branches are analytic in the relevant quadrant. The small arc vanishes
because $\sigma<1$; the large arc is
$O_s((|x|R)^{-1})$, by integrating
$e^{-2\pi|x|R\sin\theta}$ against an algebraic amplitude
$O_s(R^{-1})$.

Equations(30)--(31) of [2] continue(10) to $\Re s<2/3$.
Here the finite terms are holomorphic. Its divisor-error integral is
holomorphic on our strip by [2,(24)] with $\epsilon=1/12$ and(11):
the tail is $O(x^{-13/12})$ at worst. The two integrals in [2,(31)]
are holomorphic for $\Re s<1$; near zero their sine factor removes
one power, while at infinity one is absolutely convergent and the other
has amplitude $O(y^{-1})$ and derivative
$O((1+|s|)y^{-2})$. Their locally uniform convergence also holds
after differentiation in $s$. The only possible pole crossed is the
explicit simple pole at $s=0$ in [2,(31)]. These representations
give exponential times polynomial growth in $|\Im s|$, uniformly
on the closed strip away from that pole. The additive-divisor constants
are used only to justify analytic continuation, not in(4).

Now use the entire weight
$$
 W(s)=\frac{s(1-s)}D e^{(s-1/2-iC)^2/H^2}.
$$
It agrees with $w(t)$ on the critical line and cancels the simple
pole at0. Gaussian decay kills the end segments, so the integral of
$W(s)g(s,1-s;A)$ moves to $\Re s=-1/2$ without a residue.
There(11) permits termwise integration since
$\sum d(n)n^{-3/2}<\infty$.

For fixed $x\ne0$, truncate the real integral defining $h$
at $R$. Fubini holds on $(0,R)$. One Fourier integration by
parts bounds its tail by $O((1+|s|)/(|x|R))$, which is integrable
against $W$. The Gaussian transform can therefore be evaluated on
$\Re s=1/2$, and gives exactly(7), including its imaginary
polynomial term. The function
$B_0P e^{-H^2v^2/4+iCv}$ and its first derivative vanish at both
ends, and its second derivative is integrable: at infinity the successive
sizes are $O(y^{-1}),O(y^{-2}),O(y^{-3})$, and at zero the Gaussian
in $\log y$ beats every power. Thus $K(x)=O_{C,H}(x^{-2})$,
which independently proves final absolute divisor-series convergence.
Conjugating(10) and replacing $n$ by $-n$ shows that the other
$g$ term is the conjugate on the critical line. This proves(8).

### 2.2. Complete kernel estimate

We give constants for the entire series in(8). Let $\chi(y)$ be0
for $y\le1$,1 for $y\ge2$, and
$10(y-1)^3-15(y-1)^4+6(y-1)^5$ between. Then
$|\chi'|\le2$, $|\chi''|\le6$. Put
$\Psi(u)=\chi(u)-\chi(u/2)$. It is nonnegative, supported on
$[1,4]$, with $|\Psi'|\le3$, $|\Psi''|\le8$, and
$$
 1=1-\chi(y)+\sum_{j\ge0}\Psi(y/2^j).
$$

For $y\ge1$, let $b(y)=B_0(y)P(v(y))e^{-H^2v(y)^2/4}$.
The elementary inequalities
$$
 |yv'|\le v,\quad |y^2v''|\le2v,\quad
 |B_0^{(r)}|\le r!y^{-1-r}\quad(0\le r\le2),
$$
and $|P|\le3, |yP'|\le2, |y^2P''|\le4$ give, with $z=Hv/2$,
$$
 |b|\le3y^{-1}e^{-z^2/2},\quad
 |b'|\le11y^{-2}e^{-z^2/2},\quad
 |b''|\le76y^{-3}e^{-z^2/2}.                              \tag{12}
$$
For example the corresponding Gaussian derivative constants are2 and14,
using $4/e<2$ and $64/e^2+12/e<14$.
On $[Y,4Y]$, $Y=2^j$, set
$A_Y(y)=\Psi(y/Y)b(y)$, $D_Y=e^{-H^2/(512Y^2)}$.
Since $v\ge1/(2y)$,
$$
 \|A_Y\|_1\le9D_Y,\quad
 \|A_Y'\|_1\le60D_Y/Y,\quad
 \|A_Y''\|_1\le498D_Y/Y^2.                              \tag{13}
$$
Both $A_Y,A_Y'$ vanish at the endpoints.

For $F_x(y)=Cv(y)+2\pi xy$,
$$
 F_x'=2\pi x-\frac C{y(y+1)},\quad
 \frac C{128Y^3}\le F_x''\le\frac{3C}{Y^3},\quad
 |F_x'''|\le\frac{6C}{Y^4}.                             \tag{14}
$$
Splitting where $|F_x'|\le\sqrt{2\min F_x''}$, and applying the
monotone first-derivative bound on the two other intervals, gives a primitive
bound $4\sqrt{2/\min F_x''}<8/\sqrt{\min F_x''}$. Abel summation
with(13) therefore yields
$$
 \left|\int A_Ye^{iF_x}\right|
 \le6000\sqrt{Y/C}\,D_Y.                               \tag{15}
$$

If $x<0$ or $x>C/(\pi Y^2)$, then
$|F_x'|\ge(C/Y^2+2\pi|x|)/32=:\delta$. Two integrations by
parts bound the same integral by
$$
 \frac{\|A_Y''\|_1}{\delta^2}
 +\frac{3\|A_Y'\|_1\max|F_x''|}{\delta^3}
 +\frac{\|A_Y\|_1\max|F_x'''|}{\delta^3}
 +\frac{3\|A_Y\|_1(\max|F_x''|)^2}{\delta^4}
 \le\frac{3\cdot10^8Y^2D_Y}{(C+2\pi|x|Y^2)^2}.          \tag{16}
$$
The coefficient before rounding is274778112. No frequency sign is omitted.

We use the elementary bounds
$$
 \sum_{n\le U}d(n)\le U(1+\log U)\quad(U\ge1),\qquad
 \sum_{n\ge1}\frac{d(n)}{(U+n)^2}
 \le\frac{20[1+\log(1+U)]}{1+U}\quad(U\ge0).             \tag{17}
$$
For the second, $U\le1$ follows from $\zeta(2)^2<3$.
For $U\ge1$, partial summation of the first gives at most
$(\log U+5/2)/U$, by using
$\log(\max(1,x))\le\log U+\log(1+x/U)$ in the resulting
integral. This is smaller than the stated majorant.
The dyadic sums satisfy
$$
 \sum_{j\ge0}2^{-3j/2}e^{-H^2/(512\,4^j)}\le300H^{-3/2},
\quad
 \sum_{j\ge0}\frac{qC/4^j}{1+qC/4^j}\le2[1+\log(qC)].  \tag{18}
$$
The first follows by bounding the unimodal sum by twice its maximum plus
its integral over the entire real log scale. The coefficient is
$$
 2\cdot384^{3/4}e^{-3/4}
       +\frac{512^{3/4}\Gamma(3/4)}{2\log2}<300.
$$
The second follows from the decreasing sum-integral comparison and
$1+\log(1+qC)/\log4\le2(1+\log(qC))$, since $qC\ge1$.

Use(15) for every positive $n\le qC/(\pi Y^2)$, and(16) for
all remaining positive $n$ and all negative $n$. Equations(17)--(18),
after restoring $H\sqrt\pi$, give
$$
 \sum_{n\ne0}d(|n|)|K_{\rm high}(n/q)|
 \le4\cdot10^6q\sqrt{C/H}[1+\log(1+qC)]
  +5\cdot10^{10}q(H/C)[1+\log(1+qC)]^2.                 \tag{19}
$$
Indeed the two unrounded coefficients are at most
$6000\cdot300\sqrt\pi$ and
$2\cdot3\cdot10^8\cdot20\cdot2\sqrt\pi$, respectively.

It remains to include $0<y<2$, not to discard it. Set
$f_0=(1-\chi)B_0P e^{-H^2v^2/4+iCv}$. On this support
$v\ge v_0=\log(3/2)$. Direct differentiation gives
$$
 |f_0''(y)|\le52C^2(1+v)^4e^{5v/2-H^2v^2/4},\qquad
 |dy/dv|\le9e^{-v}.                                    \tag{20}
$$
For details, use $B_0\le e^{v/2}$, $|v'|\le e^v$,
$|v''|\le e^{2v}$, $|B_0'|\le e^{3v/2}$,
$|B_0''|\le2e^{5v/2}$. For
$Z=P e^{-H^2v^2/4+iCv}$, its three derivative majorants are
$2(1+v)^2$, $3C(1+v)^3$, $6C^2(1+v)^4$, each times
the Gaussian. The seven product-rule coefficients in(20) sum to51<52.
Since $H\ge16$,
$(1+v)^4e^{3v/2}\le e^{11v/2}\le e^{H^2v^2/8}$, and thus
$$
 \|f_0''\|_1\le468C^2\int_{v_0}^\infty e^{-H^2v^2/8}dv
 \le4680C^2H^{-2}e^{-H^2/50}<5000C^2e^{-H^2/50}.
$$
Both $f_0$ and $f_0'$ vanish at the integration endpoints.
Two ordinary Fourier integrations by parts and $\sum d(n)/n^2=\zeta(2)^2$
give
$$
 \sum_{n\ne0}d(|n|)|K_{\rm low}(n/q)|
 \le10^4q^2HC^2e^{-H^2/50}.                             \tag{21}
$$
Finally $q/[k,l]=1/(k,l)\le1$ and
$q^2/[k,l]\le X^2$. Summing(19),(21) over all $k,l\le X$
in(8), with $|a(k)|\le1$, proves the error bound(4).

### 2.3. Selberg main term and the sharp interval

For $r>0$, define
$G_r=\sum_{d\le X}\mu(d)^2/\varphi_r(d)$, where
$\varphi_r(d)=d^r\prod_{p\mid d}(1-p^{-r})$.
The positive matrix $K_r(k,l)=[k,l]^{-r}$ has the divisor factorization
$(kl)^{-r}\sum_{d\mid k,l}\varphi_r(d)$. Its minimizing vector
under $a(1)=1$ is the Selberg vector and satisfies
$K_r\lambda_r=e_1/G_r$, $\lambda_r^TK_r\lambda_r=1/G_r$.
Differentiating, its vector-derivative terms vanish since
$\lambda_r'(1)=0$, so
$$
 -\sum_{k,l}\lambda(k)\lambda(l)\frac{\log[k,l]}{[k,l]}
                  =-G_1'/G^2.
$$
In(9), write
$\log((k,l)^2/(kl))=\log k+\log l-2\log[k,l]$.
The first two terms vanish by $K_1\lambda=e_1/G$. Consequently
$$
 M_0(t)=\frac{\Re\psi(1/2+it)+2\gamma-\log(2\pi)}G
                                             -\frac{2G_1'}{G^2}.
$$
For squarefree $d$,
$\sum_{p\mid d}p\log p/(p-1)\le2\log d$, whence
$-G_1'\le2G\log X$. Euler summation for the digamma function gives
$$
 |\psi(z)-\log z+1/(2z)|\le\tfrac12\int_0^\infty|u+z|^{-2}du.
$$
At $z=1/2+it$ the right side is at most1, while
$\Re(1/z)>0$ and $2\gamma-\log(2\pi)<0$. With(3),
$$
 M_0(t)\le\frac{\log(|t|+1)+1}{\log X}+4
$$
for every real $t$, including the small-height Gaussian tail.
Since $\log(|t|+1)\le\log(C+1)+|t-C|/(C+1)$, and
$$
 \int w=H\sqrt\pi(1+H^2/(2D)),\qquad
 \int |t-C|w=H^2+H^4/D,
$$
the main integral is at most(5). On $[T,T+\Delta]$,
$w(t)\ge(T^2+1/4)D^{-1}e^{-\Delta^2/(4H^2)}$.
Positivity of the squared integrand proves(6). This completes Theorem2.

## 3. Ordinary Littlewood with both horizontal boundaries

For $T\ge10^{10}$, write $W=T+\Delta$ and
$$
 Q=\frac52\left(2+\frac{3\log((W+6)X)}{\log2}\right)+1.
$$
For $\sigma>1/2$, let $N_+(\sigma;T,W)$ count zeros with
$\beta\ge\sigma$, $T<\gamma\le W$, with multiplicity. Then
$$
 N_+(\sigma;T,W)
 \le\frac{\Delta\log B/(4\pi)+Q}{\sigma-1/2}.           \tag{22}
$$
We give the boundary details because they are needed for a uniform local
statement. For $\tau>1$, the coefficients in(2) give
$$
 |\Phi(\tau+it)-1|\le\eta(\tau):=
       \zeta(\tau)^2/\zeta(2\tau)-1.
$$
The integral test gives $\zeta(3)\le263/216<\sqrt{3/2}$.
Thus $\eta(3)<1/2$, and
$\eta(\tau)\le2^{3-\tau}/2$ for $\tau\ge3$.

On $|z-3|\le5$, for $U\ge10^{10}$,
$|\zeta(z\pm iU)|\le(U+6)^3$. One direct verification uses
$N=\lceil U+5\rceil$ and Euler--Maclaurin through $B_4$:
$$
\zeta(s)=\sum_{n<N}n^{-s}+\frac{N^{1-s}}{s-1}
 +\frac{N^{-s}}2+\frac{sN^{-s-1}}{12}
 -\frac{s(s+1)(s+2)N^{-s-3}}{720}+R_4,
\quad |R_4|\le\frac{|(s)_4|N^{-\Re s-3}}{720(\Re s+3)}.
$$
Here $-2\le\Re s\le8$, $N/2\le|\Im s|\le N$, and
$|s+j|\le2N$ for $0\le j\le3$. The sum of the six majorants is
$N^3/3+2N^2+N^2/2+N^2/6+N^2/90+N^3/45<N^3$.
Also $|M(s)|\le\sum_{n\le X}n^2\le X^3$.

The holomorphic function
$F_U(z)=[\Phi(z+iU)+\Phi(z-iU)]/2$ has modulus at most
$((U+6)X)^3$ on the disk and $F_U(3)>1/2$.
Jensen bounds its zero count on $|z-3|\le5/2$ by
$n_U\le1+3\log((U+6)X)/\log2$. On the real segment it equals
$\Re\Phi(\tau+iU)$, and so counts the crossings needed to bound
the argument, normalized from $+\infty$, by $\pi(n_U+1)$.
This covers $1/2\le\tau\le3$. For $\tau\ge3$,
$$
 |\arg\Phi(\tau+iU)|\le\arcsin\eta(\tau)
                    \le2^{3-\tau}/\sqrt3.
$$
The sum of BOTH horizontal integrals, divided by $2\pi$, is
therefore bounded by $Q$: the two tails contribute at most
$1/(\pi\sqrt3\log2)<1$, and the two finite segments contribute
at most $(5/2)(n_W+1)$.

Littlewood's lemma applied to $\Phi$, using Jensen and(6) on the
left edge, now gives(22). Every zeta zero has at least its zeta
multiplicity in $\Phi$; zeros introduced by $M$ only enlarge
the nonnegative weighted sum. The right vertical integral tends to0.
To handle zeros on the left edge, use $1/2+\epsilon$ and take a
limit avoiding zero real parts; the actual squared integral is continuous
in the edge. To handle endpoint ordinates, shift both endpoints upward by
a common positive amount and take a limit avoiding zero ordinates. This
excludes zeros at $T$ and includes them at $W$. Keep the original
fixed mollifier during these limits. Continuity of its actual squared
integral and of $Q$ suffices; no continuity of $\lfloor T^\theta\rfloor$
is assumed. Zeros on $\beta=\sigma$ retain their full weight.

## 4. Uniform elementary envelopes for the $4.2/c$ bound

Set $u=\log T\ge u_0=1000$, $\eta=2/5$,
$\theta=19/500$, $d=1/\sqrt2$,
$\Delta=e^{\eta u}$, $H=d\Delta$,
$X=\lfloor e^{\theta u}\rfloor$. Define
$$
 r_0=e^{(\eta-1)u_0},\quad k_0=1+r_0/2,\quad
 D_0=k_0^2+e^{-2u_0}/4,\quad
 \alpha=\theta+\log(1-e^{-\theta u_0})/u_0>0,
$$
$$
 \ell(u)=1+\log(1+k_0)+(1+2\theta)u.
$$
Throughout this range, $C/T\le k_0$, $D/T^2\le D_0$,
$\log X\ge\alpha u$, and $L\le\ell(u)$.
The conditions of Theorem2 hold. Its five normalized terms are bounded by
$$
 A_0(u)=d\sqrt\pi(1+\tfrac12d^2e^{(2\eta-2)u})
       \left[\frac{1+(1+\log(k_0+e^{-u_0}))/u}{\alpha}+4\right],
$$
$$
 A_1(u)=d^2e^{(\eta-1)u}(1+d^2e^{(2\eta-2)u})/(\alpha u),
$$
$$
 E_1(u)=8\cdot10^6\sqrt{k_0/d}
          e^{(2\theta+1/2-3\eta/2)u}\ell(u),\quad
 E_2(u)=10^{11}d e^{(2\theta-1)u}\ell(u)^2,
\quad E_3(u)=2\cdot10^4dk_0^2e^{(4\theta-8)u}.
$$
The last follows from $H^2/50\ge10u$, certified at $u_0$ and
preserved since $e^{2\eta u}/u$ increases. All five majorants decrease.
For $E_1,E_2$, their logarithmic derivatives at $u_0$ are less
than $-.023$ and $-.922$, respectively; their positive fractional
parts decrease thereafter. The prefactor in(6) is at most
$D_0e^{1/(4d^2)}$. Outward arithmetic gives
$$
 B\le D_0e^{1/(4d^2)}(A_0+A_1+E_1+E_2+E_3)(u_0)
                      <63.336035<64.                    \tag{23}
$$

Bellotti--Wong [7, Corollary1.3] gives
$$
 |N(y)-y\log(y/(2\pi e))/(2\pi)|\le .097\log y+4.954.
$$
Taking endpoint limits if necessary, it implies
$$
 N(W)-N(T)\ge\frac\Delta{2\pi}\log\frac T{2\pi}
                         -.194\log W-9.908.             \tag{24}
$$
The functional equation and conjugation pair zeros at $\beta+i\gamma$
with $1-\beta+i\gamma$, with the same multiplicity. Applying(22)
on both sides with $\sigma-1/2=c/u$, and using(23)--(24), bounds
the fraction in(1) by
$$
 \frac1c\,
 \frac{\log64+4\pi Q/\Delta}
 {1-\log(2\pi)/u-2\pi(.194\log W+9.908)/(\Delta u)}.
                                                               \tag{25}
$$
Use $\log((W+6)X)\le(1+\theta)u+\log(1+r_0+6e^{-u_0})$
and $\log W\le u+\log(1+r_0)$. The resulting numerator majorant
decreases and the positive denominator minorant increases on
$[u_0,\infty)$; their derivative signs are checked at $u_0$.
The denominator minorant is greater than $.99816212$, and the full
coefficient in(25) is less than $4.166541<4.2$. This proves(1).

## 5. Centered shifts and exponential concentration

We now prove(1a). The key additional step is to subtract the low Dirichlet
frequencies before shifting the Gaussian norm, retaining their cancellation
in the complete cross moment.

### 5.1. Critical mean for a mollifier chosen to the right

For $a>0$, set $s_0=1+a$ and use the canonical coefficients
$$
 G=\sum_{d\le X}\frac{\mu(d)^2}{\varphi_{s_0}(d)},\quad
 \kappa_{s_0}(d)=d^{s_0}/\varphi_{s_0}(d),\quad
 \lambda(n)=\frac{\mu(n)\kappa_{s_0}(n)}G
      \sum_{m\le X/n,(m,n)=1}\frac{\mu(m)^2}{\varphi_{s_0}(m)}.
                                                               \tag{26}
$$
Here $M,\Phi$ are formed from this new vector, which is fixed during
each application of the moment and zero-count arguments. The coefficients
are real, squarefree-supported, and have modulus at most1. Put
$$
 S_q=\sum_{j\le X/q}\frac{\lambda(qj)}j,\qquad
 T_q=\sum_{j\le X/q}\frac{\lambda(qj)\log j}j.
$$
The uniform coefficient theorem [5, Proposition5] states
$J=\sum S_q^2/q<5.5/G$. Thus
$$
 E_1:=\sum_{k,l\le X}\frac{\lambda(k)\lambda(l)}{[k,l]}
       =\sum_{q\le X}\frac{\varphi(q)}{q^2}S_q^2<5.5/G. \tag{27}
$$
Let $L_q=\sum_{p\mid q}\log p/(p-1)$. Differentiating
$(k,l)^r=\sum_{q\mid k,l}\varphi_r(q)$ at $r=1$, and
expanding $\log k=\log q+\log(k/q)$, gives the exact identity
$$
 \sum_{k,l}\frac{\lambda(k)\lambda(l)}{[k,l]}
          \log\frac{(k,l)^2}{kl}
   =2\sum_q\frac{\varphi(q)}{q^2}(L_qS_q^2-S_qT_q).     \tag{28}
$$

For $h(p)=(p^a-1)/(p^{1+a}-1)$, define
$I_q(z)=\sum_{n\le z,(n,q)=1}\mu(n)h(n)$, with $h$
extended multiplicatively on squarefree integers. Since $0\le h(p)\le1/p$,
the elementary weighted Möbius inequality [5, Lemma2] gives $|I_q(z)|\le1$.
Expanding(26) and collecting the squarefree product of its two inner
indices gives
$$
 S_q=\frac{\mu(q)\kappa_{s_0}(q)}G I_q(X/q),\qquad
 T_q=-\frac{\mu(q)\kappa_{s_0}(q)}G
  \sum_{p\le X/q,\ p\nmid q}
   \frac{p^a\log p}{p^{1+a}-1}I_{pq}(X/(pq)).           \tag{29}
$$
For the second identity, the inner numerator is
$\sum_{j\mid n}\mu(j)j^a=\prod_{p\mid n}(1-p^a)$;
inserting $\log j$ differentiates only these numerator powers.
The denominators and outer prefactor are held fixed.

The identity
$\sum_{n\le z}\Lambda(n)\lfloor z/n\rfloor=\log(\lfloor z\rfloor!)$
and $\lfloor z/n\rfloor\ge z/(2n)$ give
$\sum_{p\le z}\log p/(p-1)\le4\log z$. Hence
$$
 |T_q|\le4\log(X/q)|\mu(q)|\kappa_{s_0}(q)/G.
$$
Also $L_q\le\log q$, $\kappa_{s_0}(q)\le q/\varphi(q)$, and
$$
 \sum_{q\le X}\frac{\mu(q)^2}{\varphi(q)}
 \le C_0(1+\log X),\qquad C_0=\frac{\zeta(2)\zeta(3)}{\zeta(6)}<1.9436.
$$
The latter follows by expanding $q/\varphi(q)$, then dropping
positive squarefree and coprimality restrictions from a harmonic sum.
Equations(27)--(29) and the global digamma bound yield
$$
 M_0(t)\le\frac{5.5}G[\log(|t|+1)+1+2\log X]
                 +\frac{8C_0\log X(1+\log X)}{G^2}.    \tag{30}
$$

The kernel error(4) was proved for every real vector with modulus at most1.
Writing $m_w=H\sqrt\pi(1+H^2/(2D))$, it follows that
$$
 \int_{\mathbb R}|\Phi(1/2+it)|^2w(t)dt\le J_{
 \rm crit}:=m_w\left\{\frac{5.5}G[\log(C+1)+1+2\log X]
                       +\frac{8C_0\log X(1+\log X)}{G^2}\right\}
       +\frac{5.5}G\frac{H^2+H^4/D}{C+1}+E(C,H,X).     \tag{31}
$$

### 5.2. Complete Gaussian projection

Let $C_n=\sum_{d\mid n,d\le X}\lambda(d)$, and for an integer
$Y\ge2$ let $P_Y(z)=\sum_{n\le Y}C_nn^{-z}$.
Shifting the integral of $W(z)\Phi(z)P_Y(1-z)$ from $\Re z=1/2$
to2 gives
$$
 \int_{\mathbb R}\Phi(1/2+it)\overline{P_Y(1/2+it)}w(t)dt
 =H\sqrt\pi\sum_{m\ge1,n\le Y}\frac{C_mC_n}{\sqrt{mn}}
      e^{iC\log(n/m)}P(\log(n/m))e^{-H^2\log(n/m)^2/4}. \tag{32}
$$
The only crossed pole is canceled by $W(1)=0$. On the right the
Dirichlet series is absolutely convergent; Gaussian decay justifies the
contour ends and termwise transform. The final sum is absolutely convergent
by the following bound, so the full infinite tail is retained.

For every real $v$,
$|P(v)|e^{-H^2v^2/4}\le4e^{-H^2v^2/8}$. Indeed, with
$z=Hv/2$, the hypotheses $H^2\le D$ and $C^2\le D$ give
$|P(v)|\le3/2+2|z|+z^2$, and
$(3/2+2|z|+z^2)e^{-z^2/2}\le3/2+2e^{-1/2}+2/e<4$.
Also $|C_n|\le d(n)\le2\sqrt n$, by pairing divisors, and hence
$|C_mC_n|/\sqrt{mn}\le4$. For $m\le2Y,m\ne n\le Y$,
$|\log(m/n)|\ge1/(2Y)$, with at most $2Y^2$ such pairs.
For the rest,
$$
 \sum_{m>2Y}e^{-H^2\log(m/Y)^2/8}
 \le Y\int_{\log2}^\infty e^{-H^2v^2/8+v}dv
 \le Ye^{-H^2/64}.
$$
Here $H\ge16$ permits $v\le H^2v^2/16$; the Gaussian tail
factor is $8/(H^2\log2)<1$. Thus the absolute off-diagonal in(32),
and in the corresponding finite $P_Y$ square, is at most
$$
 O_Y=48H\sqrt\pi\,Y^2e^{-H^2/(32Y^2)}.                \tag{33}
$$
Their common diagonal is $m_w\sum_{n\le Y}C_n^2/n$. Expanding
the square leaves its negative, so
$$
 \int_{\mathbb R}|\Phi-P_Y|^2w\le J_{\rm crit}+3O_Y.    \tag{34}
$$

### 5.3. Holomorphic tail and strip norm

Put $m=M(1)$, $|m|\le1+\log X$, and
$$
 R_Y(z)=\Phi(z)-P_Y(z)-\frac{mY^{1-z}}{z-1}.
$$
Its singularity at1 is removable, so it is holomorphic on
$1/2\le\Re z\le3$. The subtracted pole has the exact critical norm
$$
 \int_{\mathbb R}\left|\frac{mY^{1/2-it}}{-1/2+it}\right|^2w(t)dt
                =\frac{|m|^2YH\sqrt\pi}D.
$$
Therefore a critical norm upper bound for $R_Y$ is
$$
 L_0=\left(\sqrt{J_{\rm crit}+3O_Y}
                      +|m|\sqrt{YH\sqrt\pi/D}\right)^2.\tag{35}
$$
On $\Re z=3$, partial summation of the divisor bound in(17) gives
$$
 |R_Y(3+it)|\le Y^{-2}\left(\tfrac32\log Y+\tfrac94+\tfrac{|m|}2\right).
$$

Define
$F(z)=zR_Y(z)e^{(z-1/2-iC)^2/(2H^2)}/\sqrt D$ and
$I(x)=\int_{\mathbb R}|F(x+it)|^2dt$. All derivatives have uniform
Gaussian decay on the strip. Integration by parts and Cauchy--Riemann give
$I''=4\int|F'|^2$, while Cauchy gives $(I')^2\le II''$.
Thus $\log I$ is convex; the identically zero case is immediate.
For $\sigma'=1/2+h\in(1/2,1)$, $\nu=2h/5$, this yields
$$
 I(\sigma')\le L_0^{1-\nu}R_3^\nu,
\quad
 R_3=e^{25/(4H^2)}H\sqrt\pi\frac{C^2+9+H^2/2}D
       Y^{-4}\left(\tfrac32\log Y+\tfrac94+\tfrac{1+\log X}2\right)^2.
                                                               \tag{36}
$$
On the sharp interval this implies
$$
 V_R:=\frac{D}{T^2+\sigma'^2}e^{\Delta^2/(4H^2)-h^2/H^2}
             (L_0/\Delta)^{1-\nu}(R_3/\Delta)^\nu
 \ge\frac1\Delta\int_T^{T+\Delta}|R_Y(\sigma'+it)|^2dt. \tag{37}
$$

### 5.4. Centered mean and zero detector

Take $a=2h$. The exact minimizing identity at $1+a$ gives
$\sum_{n\ge1}C_n^2n^{-1-a}=\zeta(1+a)/G$.
The sum $G$ is exactly the positive subseries of $\zeta(1+a)$
with $\operatorname{rad}(n)\le X$. Hence
$$
 1/G\le a/(1-X^{-a}),\qquad
 \zeta(1+a)/G-1\le X^{-a}/(1-X^{-a}).                  \tag{38}
$$
The log frequencies of $P_Y-1$ are separated by at least $1/Y$.
Direct off-diagonal integration and a harmonic row sum give the complete
normalized sharp bounds
$$
 V_L=\left(1+\frac{4Y(1+\log Y)}\Delta\right)
                         \frac{X^{-a}}{1-X^{-a}},\qquad
 V_P=\frac{(1+\log X)^2Y^{2-2\sigma'}}{T^2}
$$
for $P_Y-1$ and the pole term, respectively. The actual decomposition
therefore gives
$$
 \frac1\Delta\int_T^{T+\Delta}|\Phi(\sigma'+it)-1|^2dt
          \le V=(\sqrt{V_L}+\sqrt{V_R}+\sqrt{V_P})^2.    \tag{39}
$$

Use the centered detector $\mathcal H=\Phi(2-\Phi)$, so that
$|\mathcal H|\le1+|\Phi-1|^2$. Normalize its argument continuously
from $+\infty$, as in Section3. The sum of both horizontal absolute
argument integrals, divided by $2\pi$, has the complete allowance
$$
 Q_H=\tfrac52[3+6\log((T+\Delta+6)X)/\log2]+1.          \tag{40}
$$
Thus $(2\pi)^{-1}\sum_{U\in\{T,T+\Delta\}} \int_{\sigma'}^\infty|\arg\mathcal H(\tau+iU)|d\tau\le Q_H$.
For clarity, on the radius5 disk used in Section3 one has
$|\mathcal H|\le3((U+6)X)^6$ and its symmetrized value at3 is
greater than3/4. Jensen gives $n_U\le2+6\log((U+6)X)/\log2$.
The two finite argument segments cost at most $(5/2)(n_W+1)$.
Beyond3, $|\mathcal H-1|\le2^{6-2\tau}/4$, and the two tails,
divided by $2\pi$, sum to less than1. This proves(40).

For $u=\log T$, choose $h=(c-b)/u$, so the detector has
horizontal zero weight $b/u$ at the target $1/2+c/u$. Jensen,
Littlewood gives the one-sided count at most
$(u/b)[\Delta\log(1+V)/(2\pi)+Q_H]$.
Symmetry and(24) therefore bound the two-sided fraction by
$$
 \frac{2\log(1+V)/b+4\pi Q_H/(b\Delta)}{d_{\rm count}},
\quad d_{\rm count}=1-\frac{\log(2\pi)}u
              -\frac{2\pi[.194\log(T+\Delta)+9.908]}{\Delta u}.
                                                               \tag{41}
$$
The endpoint arguments of Section3 apply with the coefficients and $a$
fixed. The detector counts every zeta zero with its full multiplicity.

### 5.5. A single uniform exponential envelope

Take $u\ge1000$, $\Delta=T^{.4}$, $H=\Delta/\sqrt2$,
$X=\lfloor T^{.038}\rfloor$, $Y=\lfloor T^{.38}\rfloor$,
$b=13$, $50\le c<u/2$, and $q=c-13\ge37$.
Put $\alpha=.037999$, $r_0=e^{-74\alpha}$,
$R_0=(1-r_0)^{-1}$, $k=.075$, and
$$
 P_*(q)=1.256\left[11(1+.076+.002)R_0q
       +32(1.9436)(.038)(.039)R_0^2q^2\right]+.4,
\quad \epsilon_0=4(381)e^{-20}.
$$
The outward certificate verifies the following uniform envelopes:
$$
 L_0/\Delta\le P_*(q),\qquad
 V_R\le1.65P_*(q)e^{-.602q},\qquad
 V_L\le(1+\epsilon_0)R_0e^{-2\alpha q},\qquad
 V_P\le10^{-100}e^{-k(q-37)}.                           \tag{42}
$$
Here are the reductions to elementary constants. The floor inequality
gives $\log X\ge\alpha u$, and(38) gives $G^{-1}\le2qR_0/u$.
In(31), $m_w/\Delta<1.254$, $E/\Delta<.388$, and its
Lipschitz correction is less than.001. Also $3O_Y/\Delta<.001$,
since $H^2/(32Y^2)\ge10u$. The square root of the pole norm
divided by $\Delta$ is less than.001. In(35) use
$(\sqrt J+.001)^2\le1.001J+.001001$ and round upward to $P_*$.
Each of these height envelopes decreases; the Gaussian dominances follow
at $u=1000$ and persist because their exponential-to-linear ratios
increase.

For the right edge, including the floor in $Y$,
$$
 R_3/\Delta\le1.255(.589u+2.75)^2e^{-1.52u}.
$$
The logarithm of its prefactor divided by $u$ decreases for
$u\ge1000$, and
$$
 .608-\frac{2}{5000}\log(1.255(591.75)^2)>.602.
$$
The sharp factor in(37) is less than1.65; since $P_*(q)>1$,
convexity gives the second estimate in(42). The pole estimate follows by
multiplying its elementary bound by $e^{k(q-37)}$, using $q<u/2$,
and bounding the resulting decreasing polynomial times
$e^{-(2-.38-k/2)u}$ at1000.

Every squared component in(42), after scaling by $e^{k(q-37)}$,
decreases with $q$: $2\alpha>k$ and
$P_*'/P_*\le2/q\le2/37<.602-k$. Consequently the same scaled
$V$ is at most its upper bound at $q=37$, namely
$$
 V\le .064192997\,e^{-k(q-37)}.                        \tag{43}
$$
The count denominator is greater than.998. Finally the horizontal term
in(41), after scaling by $e^{k(c-50)}$, is less than $10^{-100}$:
use $c<u/2$ and the decreasing function consisting of its linear
logarithmic allowance times $e^{-(.4-k/2)u}$.
The outward certificate, using the unrounded(43), gives
$$
 \frac{2}{13(.998)}
   \left[\sqrt{V_L(37)}+\sqrt{V_R(37)}+10^{-50}\right]^2
          +10^{-100}<.009895637<.01.
$$
Applying $\log(1+V)\le V$ in(41) proves(1a).

## 6. Complete saddle-phase estimate and shorter intervals

The next argument preserves the full nonlinear phase in(8). It gives the
explicit classical27/82 mechanism needed for(1b). The bound in(4) remains
useful for its much smaller constants in the longer interval regime.

Let $C\ge256$, $16\le H\le\sqrt C$, $X\ge2$ integral, and let
$A(s)=\sum_{k\le X}a(k)k^{-s}$ have real coefficients $|a(k)|\le1$.
Use $w$, $M_0$, $K$, $P$, $v$ and the exact identity(7)--(10).
Put $L=1+\log(1+X^2C)$.

**Theorem3.** The absolute difference between
$\int_{\mathbb R}|\zeta A|^2w$ and $\int_{\mathbb R}M_0w$ is at most

$$
\begin{aligned}
E_{\rm ph}={}&2^{50}H\left[
 X^{11/6}C^{9/20}H^{-41/30}
 +X^{25/12}C^{61/120}H^{-31/20}+XH^{-1/2}\right]\\
&+2^{170}X^2L+10^{11}X^2(H/C)L^2
 +2\cdot10^4X^4HC^2e^{-H^2/50}.
\end{aligned}                                                    \tag{A1}
$$

All frequencies and signs are included. The exact leading phase is never
replaced by its square-root approximation.

### 6.1. An elementary derivative estimate with a large explicit constant

Write $e(u)=e^{2\pi iu}$. If a real $C^k$ phase on a real interval of
length at most $L_1\ge1$ satisfies
$\lambda_1\le|f^{(k)}|\le64\lambda_1$, then, for $2\le k\le5$,

$$
\left|\sum_{n\in J\cap\mathbb Z}e(f(n))\right|
\le10^4\left[
 L_1\lambda_1^{1/(2^k-2)}
 +L_1^{1-1/2^{k-2}}\lambda_1^{-1/(2^k-2)}\right].       \tag{A2}
$$

For $k=2$, $f'$ is monotone. If $\lambda_1\ge1/16$, the trivial count
at most $L_1+1\le2L_1$ proves(A2). Otherwise let
$\delta=\sqrt{\lambda_1}<1/4$. The range of $f'$ has length at most
$64\lambda_1L_1$. At most $64\lambda_1L_1+3$ intervals have $f'$
within $\delta$ of an integer. Each contains at most
$2\delta/\lambda_1+1$ integers. On each of the at most
$64\lambda_1L_1+4$ complementary intervals, the monotone
first-derivative estimate, including its last integer, is $4/\delta+1$.
To verify this, let $m_0,\ldots,m_1$ be the consecutive integers in one
complementary interval. If $m_0=m_1$, use the bound1. Otherwise apply
summation by parts to
$e(f(n+1))-e(f(n))=e(f(n))(e(f(n+1)-f(n))-1)$ for
$m_0\le n<m_1$. The entire segment $[n,n+1]$ remains in the same
complementary interval, so the phase increments are monotone in a single
interval $[m+\delta,m+1-\delta]$. The endpoint reciprocals and their
total variation are at most $4/\delta$: this follows, for example, from
$(e(t)-1)^{-1}=-1/2-(i/2)\cot(\pi t)$ and
$\sin(\pi\delta)\ge2\delta$. Restore the last term at a cost1.
Thus the total is at most
$(64\lambda_1L_1+3)(2/\delta+1) +(64\lambda_1L_1+4)(4/\delta+1)$, which is at most
$416L_1\delta+24/\delta$ and hence less than
$1000(L_1\sqrt{\lambda_1}+\lambda_1^{-1/2})$, leaving ample slack.
Boundary points can be assigned to either neighboring piece.

For the induction step put $p=2^{k-1}-1$,
$x=\lambda_1^{-1/p}$. If $\lambda_1>1$, the first term in(A2)
covers the trivial count. If $x>L_1$, the second does so. Otherwise
$H_1=\lfloor x\rfloor$ satisfies $x/2\le H_1\le x\le L_1$.
The finite differencing inequality, for a sum with at most $2L_1$ terms,
gives

$$
 |S|^2\le6L_1^2/H_1+
          (6L_1/H_1)\sum_{1\le h<H_1}|S_h|.
$$

The $(k-1)$st derivative of the $h$-difference is between
$h\lambda_1$ and $64h\lambda_1$ in absolute value, since the original
derivative has a fixed sign. With $r=1/(p-1)$,
$\delta_1=1/2^{k-3}$, the induction hypothesis and
$\sum_{h<H_1}h^r\le H_1^{1+r}$,
$\sum_{h<H_1}h^{-r}\le H_1^{1-r}/(1-r)$ give

$$
 |S|^2\le18(10^4)
  [L_1^2\lambda_1^{1/p}
       +L_1^{2-\delta_1}\lambda_1^{-1/p}].
$$

Here the first bracket has coefficient at most $12+6(10^4)$,
and the second at most $6(10^4)2^r/(1-r)$. The inequality
$2^r/(1-r)\le3$ holds for all three induction steps. Since
$\sqrt{18\cdot10^4}<10^4$, taking a square root proves(A2).
This proof permits shortened intervals and any additional linear phase.

### 6.2. Uniform stationary approximation of one compact block

Use the nonnegative $C^2$ dyadic partition of Section2.2:
$1=(1-\chi(y))+\sum_{j\ge0}\Psi(y/2^j)$, $Y=2^j$, and
$A_Y(y)=\Psi(y/Y)B_0(y)P(v)e^{-H^2v^2/4}$.
Its scaled amplitude $a_Y(u)=YA_Y(Yu)$, extended by zero, has on $[1,4]$

$$
 |a_Y|\le3D_Y,\quad |a_Y'|\le20D_Y,\quad
 |a_Y''|\le166D_Y,\qquad D_Y=e^{-H^2/(512Y^2)}.         \tag{A3}
$$

These follow directly from the pointwise bounds(12) and
$|\Psi'|\le3$, $|\Psi''|\le8$. Both the amplitude and its first
derivative vanish at the ends.

For $x=n/q>0$, scale $y=Yu$ and put $r=1/Y$, $\Lambda=C/Y$,

$$
 f(u)=Y\log(1+1/(Yu))+\beta u,
 \qquad \beta=2\pi xY^2/C.
$$

The phase is $\Lambda f(u)$. It has exactly one positive stationary
point $u_0$, because $f'=\beta-[u(u+r)]^{-1}$.
On $[1/2,8]$,

$$
 2^{-9}\le f''\le16,\quad |f'''|\le96,\quad
 |f^{(4)}|\le768,\quad |f^{(5)}|\le7680.              \tag{A4}
$$

For example $f''=2\int_0^1(u+rt)^{-3}dt$ and subsequent derivatives
have the asserted bounds. If $u_0\in[1/2,8]$, use
$v=\operatorname{sgn}(u-u_0)\sqrt{2(f(u)-f(u_0))}$.
Writing $h=u-u_0$,

$$
 Q=2\int_0^1(1-t)f''(u_0+th)dt,\quad
 R=\int_0^1f''(u_0+th)dt,\quad v'=R/\sqrt Q,
$$

gives $2^{-11}\le v'\le2^9$. Also
$|Q'|\le32$, $|Q''|\le128$, $|R'|\le48$, $|R''|\le256$.
Direct differentiation then gives $|v''|\le2^{27}$,
$|v'''|\le2^{50}$. The inverse $p$ consequently satisfies

$$
 |p'|\le2^{11},\qquad |p''|\le2^{60},\qquad
 |p'''|\le2^{128}.                                    \tag{A5}
$$

Let $g(v)=a_Y(p(v))p'(v)$, with zero extension. Its support length is
less than $2^{11}$; it and its first derivative vanish at the support
ends. The formula
$g''=a_Y''(p)(p')^3+3a_Y'(p)p'p''+a_Y(p)p'''$
gives $\|g''\|_1\le2^{142}D_Y$.
The exact Fourier transform of a Fresnel Gaussian, first damped and then
passed to the limit, proves

$$
\left|\int g(v)e^{i\Lambda v^2/2}dv
     -g(0)e^{i\pi/4}\sqrt{2\pi/\Lambda}\right|
 \le\frac{2\|g''\|_1}{\Lambda}.                       \tag{A6}
$$

Indeed $|\widehat g(\xi)|\le\|g''\|_1/\xi^2$; splitting at
$|\xi|=\sqrt\Lambda$ and using
$|e^{-i\xi^2/(2\Lambda)}-1|\le\min(2,\xi^2/(2\Lambda))$
gives the constant $5/\sqrt{2\pi}<2$.

If $u_0$ is outside $[1/2,8]$, then $|f'|\ge1/32$ on $[1,4]$.
One integration by parts and(A3)--(A4) give an error at most
$2^{18}D_Y/\Lambda$, with zero main term. Hence in all cases

$$
 \int A_Y(y)e^{iCv(y)+2\pi ixy}dy
 =A_Y(y_0)e^{i\phi(n)+i\pi/4}\sqrt{2\pi/F_x''(y_0)}
       +\mathcal E_{Y,n},\quad
 |\mathcal E_{Y,n}|\le2^{150}D_Y Y/C,                 \tag{A7}
$$

where the main term is zero outside the amplitude support,
$y_0=Yu_0$, $F_x(y)=Cv(y)+2\pi xy$, and
$\phi(n)=F_x(y_0)$.
There is no loss when the saddle crosses the support boundary.

Use(A7) only when $0<n\le qC/(\pi Y^2)$. The complete divisor bound
$\sum_{n\le U}d(n)\le U(1+\log U)$ and

$$
 \sum_{j\ge0}D_{2^j}/2^j\le100/H                     \tag{A8}
$$

show that all these remainders, after restoring $H\sqrt\pi$,
$2\Re$, and the pair weights, cost less than $2^{158}X^2L$.
For(A8), the two-maxima plus log-integral bound has constant
$32e^{-1/2}+\sqrt{512\pi}/(2\log2)<100$.
Every other positive frequency and every negative frequency is covered
by the previous two-integration-by-parts bound(16), giving
$10^{11}X^2(H/C)L^2$ for the whole moment. The low-$y$ part costs the
last term in(A1), unchanged. Thus all tails are already paid.

### 6.3. The exact leading phase and complete divisor sum

Put $B=2Cq/\pi$. The stationary point and phase satisfy

$$
 y_0=(\sqrt{1+B/n}-1)/2,\qquad
 f_0(n)=\phi(n)/(2\pi),\qquad
 f_0'(n)=\frac{\sqrt{1+B/n}-1}{2q}.
$$

Summing the nonnegative partition in the leading term gives
$\chi(y_0)$, since every block with a nonzero leading term is among the
positive frequencies to which(A7) was applied. After dividing by
$H\sqrt\pi$, the complete leading kernel is
$e^{i\pi/4}A_0(n)e(f_0(n))$, where

$$
 A_0(n)=\chi(y_0)\left(\frac{\pi q}{2C}\right)^{1/4}
 n^{-1/4}(1+n/B)^{-1/4}P(v_0)e^{-H^2v_0^2/4},\quad
 v_0=2\operatorname{arsinh}\sqrt{n/B}.                 \tag{A9}
$$

It vanishes for $n\ge B/8$. On its support,
$\operatorname{arsinh}t\ge t/\sqrt{1+t^2}$ gives
$v_0^2/4\ge8n/(9B)$, hence its Gaussian is at most
$e^{-H^2n/(qC)}$, because $4\pi/9>1$.
All factors of(A9) other than the complex polynomial $P$ are nonnegative
and decreasing in $n$. Write their product as $a_0(n)$.
From $|yP_y|\le2$ and
$|ny_0'/y_0|=(y_0+1)/(2y_0+1)\le1$ one obtains
$|nP_n|\le2$. Therefore the endpoint plus total variation is at most
$(6+2\log2)a_0(N)$. On any $[N,2N]$, including a truncated last block,
this is at most

$$
 16(q/C)^{1/4}N^{-1/4}e^{-H^2N/(qC)}.                 \tag{A10}
$$

The phase has

$$
 f_0''(n)=-\frac{\sqrt{2Cq/\pi}}{4q}
               n^{-3/2}(1+n/B)^{-1/2}.
$$

Three more differentiations give, for $0<n\le B/4$,

$$
 2\sqrt{C/q}\,n^{-9/2}\le f_0^{(5)}(n)
                    \le4\sqrt{C/q}\,n^{-9/2}.         \tag{A11}
$$

For completeness, the factor multiplying
$\sqrt{2Cq/\pi}\,n^{-9/2}(1+n/B)^{-1/2}/(4q)$ is
$(105+45t+27t^2+15t^3)/8$, $t=n/(B+n)\le1/5$.
The lower bound is greater than2 and the upper less than4 by direct
scalar comparisons. No large correction is dropped.

Let $F=\sqrt{CN/q}$ and let $\alpha_1$ be arbitrary real.
Use the half-open dyadic blocks $N\le n<2N$, $N=1,2,4,\ldots$, so that
$n=1$ is included exactly once. For $N\le z\le2N$ and $N\le B/8$,
the exact Dirichlet hyperbola identity for an arbitrary function $u$ is
$$
 \sum_{N\le n<z}d(n)u(n)
 =2\sum_{a\le\sqrt{2N}}\ \sum_{\substack{b\ge a\\N\le ab<z}}u(ab)
    -\sum_{N\le a^2<z}u(a^2).
$$
The inner cofactor sum has
$b\in[N/a,2N/a]$ and possibly a shorter interval from $b\ge a$.
Set $L_1=N/a\ge1$; for $N=1$ only $a=1$ occurs, and for $N\ge2$
we have $a\le\sqrt{2N}\le N$. By(A11), the fifth derivative of
$f_0(ab)+\alpha_1ab$ is between
$F/(16L_1^5)$ and $64F/(16L_1^5)$. Formula(A2) gives at most

$$
 2\cdot10^4[F^{1/30}L_1^{5/6}
                           +F^{-1/30}L_1^{25/24}].
$$

Sum $a\le\sqrt{2N}$ using
$\sum_{a\le U}a^{-5/6}\le6U^{1/6}$ and
$\sum a^{-25/24}\le25$, and retain the square correction explicitly.
The result, uniformly in every prefix $z$, is

$$
 \left|\sum_{N\le n<z}d(n)e(f_0(n)+\alpha_1n)\right|
 \le2^{28}[F^{1/30}N^{11/12}
              +F^{-1/30}N^{25/24}+\sqrt N].          \tag{A12}
$$

This includes the actual modular phase by taking
$\alpha_1=\bar\kappa/\lambda$. No assumption about its denominator
is needed. Empty or one-term cofactor intervals are covered by(A2),
and the displayed square correction includes every diagonal pair.

Apply partial summation using(A10). For
$p=41/60,31/40,1/4$,

$$
 \sum_{N=1,2,4,\ldots}N^pe^{-zN}\le16z^{-p}.          \tag{A13}
$$

Two maxima and the log-integral prove(A13): its coefficient is
$2(p/e)^p+\Gamma(p)/\log2<16$ for each specified $p$.
The three leading costs, before the pair sum, are respectively

$$
 H\cdot2^{38}\left[
 q^{11/12}C^{9/20}H^{-41/30}
 +q^{25/24}C^{61/120}H^{-31/20}
 +q^{1/2}H^{-1/2}\right],                            \tag{A14}
$$

where $2^{38}$ safely includes $\sqrt\pi$, the coefficient in(A12),
(A10) and(A13). The moment's outer factor2 is included when summing
below; rounding all final leading constants to $2^{50}$ is ample.

### 6.4. Sum over the complete mollifier

Write $k=g\kappa$, $l=g\lambda$, $(\kappa,\lambda)=1$ and
$q=\kappa\lambda$, so $[k,l]=gq$. Dropping only positive
coprimality restrictions gives

$$
 \sum_{k,l\le X}\frac{q^{-1/12}}g\le2X^{11/6},\quad
 \sum_{k,l\le X}\frac{q^{1/24}}g\le\tfrac32X^{25/12},\quad
 \sum_{k,l\le X}\frac{q^{-1/2}}g\le8X.               \tag{A15}
$$

The first follows from
$\sum_{n\le Z}n^{-1/12}\le(12/11)Z^{11/12}$ and
$\zeta(17/6)\le1+6/11$; the second uses
$\sum_{n\le Z}n^{1/24}\le Z^{25/24}$ and
$\zeta(37/12)\le1+12/25$; the third uses
$\sum n^{-1/2}\le2\sqrt Z$ and $\zeta(2)<2$.
Combine(A14)--(A15), the stationary remainder in Section6.2, and all
nonstationary and low-$y$ contributions there. They are bounded by(A1).
This proves Theorem3.

### 6.5. Explicit concentration consumer

Let $u=\log T\ge10^6$,
$\Delta=T^{.33}$, $C=T+\Delta/2$, $H=\Delta/\sqrt2$,
$X=\lfloor T^{.0005}\rfloor$, and $Y=\lfloor T^{.32}\rfloor$.
For $3000\le c<u/2$ put $q_0=c-13$, $a=2q_0/u$, and use the canonical
Selberg coefficients optimized at $1+a$. Here $q_0$ is a strip-width
parameter, unrelated to the reduced pair product $q$ above.

All the centered projection, pole subtraction, strip norm convexity,
sharp polynomial, centered detector and full zero-count arguments in
Sections5.1--5.4 apply unchanged after replacing
its critical error by(A1). No asymptotic remainder is imported.
For $\theta=.0005$, $\eta=.33$, the three leading normalized height
exponents are

$$
 (11/6)\theta+9/20-(41/30)\eta=-1/12000,\quad
 (25/12)\theta+61/120-(31/20)\eta<-.00212,\quad
 \theta-\eta/2=-.1645.
$$

The normalized stationary and nonstationary errors decrease like
$e^{(2\theta-\eta)u}$ and $e^{(2\theta-1)u}$ times the displayed
logarithms. Their complete sum divided by $\Delta$ is less than
$8.231554\cdot10^{-22}$ at $u=10^6$ and decreases thereafter.
The low-$y$ domination $H^2/50\ge10u$ is preserved. The projection
error is still negligible since $H^2/(32Y^2)\ge10u$ uniformly.

Put $\alpha=.00049999$, $k=.00099$,
$R=(1-e^{-5974\alpha})^{-1}$ and

$$
\begin{aligned}
P_0(q_0)=1.256\{&11(1+.001+.000002)Rq_0\\
 &+32(1.9436)(.0005)(.000501)R^2q_0^2\}+.4,\quad
\epsilon_0=4(320001)e^{-10000}.
\end{aligned}
$$

The complete counterparts of(42) are

$$
 L_0/\Delta\le P_0(q_0),\quad
 V_R\le1.65P_0(q_0)e^{-.511q_0},\quad
 V_L\le(1+\epsilon_0)Re^{-2\alpha q_0},\quad
 V_P\le10^{-100}e^{-k(q_0-2987)}.                      \tag{A16}
$$

The derivation is identical except for the stated parameters and error:
$m_w/\Delta<1.254$,
$G^{-1}\le2q_0R/u$, and the right-edge prefactor is
$1.255(.48025u+2.75)^2e^{-1.28u}$. Its logarithm divided by $u$
decreases and yields the strip rate $.511$. The sharp factor is less
than1.65. All omitted height-dependent quantities are retained in the
outward checker before being rounded; they decrease.

After multiplication by $e^{k(q_0-2987)}$, each squared component of(A16)
decreases because $2\alpha>k$ and
$P_0'/P_0\le2/q_0\le2/2987<.511-k$.
The same scaling therefore bounds the full centered mean by its value
at $q_0=2987$, less than $.053121047$. The count denominator exceeds
$.998$, and both horizontal arguments, after scaling, contribute less
than $10^{-100}$. With $b=13$, the full two-sided coefficient is less
than $.008188847<.01$. Consequently the shorter-interval assertion(1b) is

$$
\frac{\#\{\rho:T<\Im\rho\le T^{.33}+T,
          |\Re\rho-1/2|\ge c/\log T\}}
 {N(T+T^{.33})-N(T)}
 <.01e^{-.00099(c-3000)}                               \tag{A17}
$$

for every $T\ge e^{1000000}$ and $3000\le c<(\log T)/2$.
Threshold and endpoint zeros keep their full multiplicities by the same
fixed-coefficient limits. This proves(1b), including its boundary conventions. It permits individual off-line zeros.


## 7. Verification and limitations

The supplement contains the complete notes, four outward scalar checkers,
their saved JSON outputs, and a finite normalization control. With
`python-flint`, from its root run

    python3 experiments/gaussian_moment/certify_kernel_constants.py
    python3 experiments/gaussian_moment/certify_sharp_mean.py
    python3 experiments/gaussian_moment/certify_centered_shift.py
    python3 experiments/gaussian_moment/check_shift_algebra.py
    python3 experiments/gaussian_moment/certify_phase_concentration.py

The first checks the scalar comparisons in the dyadic proof. The second
uses1024-bit Arb arithmetic to check(23)--(25) and the derivative signs;
it does not sample heights. The third certifies all rounded comparisons
and decreasing envelopes in Section5.5, again without a height or width
grid. The fourth compares the new divisor and prime-log identities against
their direct finite definitions at $X=20,a=1$ using exact fractions.
That finite control supports signs and indices, not a proof for general
parameters. The fifth command certifies the explicit constants and decreasing
envelopes of Section6 with66 outward comparisons, including the complete
zero-count consumer. It does not verify the analytic stationary transform or
finite-differencing proof. Each command runs in less than a second on a CPU.
The saved normalization control integrates the original zeta product at
$C=400,H=16$ and sums both kernel signs through $|n|=128$, for
$X=1,2,3$; discrepancies are between $1.06\cdot10^{-8}$ and
$2.16\cdot10^{-8}$. That finite, nonrigorous control supports the
normalization only. It is not the proof of continuation or of the infinite
tail estimate. Those are the analytic arguments above.

The scalar calculations are reproducible author certificates. An independent
line-by-line review by span_of_dilates found no error in Sections5.1--5.5
of the earlier draft; its three requested bound/normalization clarifications
are included above. That review takes Section2 and [5] as inputs, and does
not cover the new Section6. Independent analytic review of the complete
Gaussian argument is still pending. Large constants
and the high starting height are deliberate. No optimization claim is
made, and no RH conclusion follows.

## References

[1] Y. Motohashi. *A note on the mean value of the zeta and L-functions, V*.
Proceedings of the Japan Academy, Series A62(10) (1986),399--401.
https://doi.org/10.3792/pjaa.62.399

[2] H. Ishikawa and K. Matsumoto. *An explicit formula of Atkinson type
for the product of the Riemann zeta-function and a Dirichlet polynomial*.
Central European Journal of Mathematics9 (2011),102--126.
https://doi.org/10.2478/s11533-010-0085-5

[3] J. Steuding. *On simple zeros of the Riemann zeta-function in short
intervals on the critical line*. Acta Mathematica Hungarica96(4)
(2002),259--308. https://doi.org/10.1023/A:1019767816190

[4] A. A. Karatsuba and M. A. Korolev. *Behaviour of the argument of the
Riemann zeta function on the critical line*. Russian Mathematical Surveys61
(2006),389--482. Chapter1, Lemmas1 and3, Theorem1.
https://doi.org/10.1070/RM2006v061n03ABEH004328

[5] bramble_trace and span_of_dilates. *Explicit centered zero-density
bounds in short intervals*. rStation, Paper168, version1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/168/v1

[6] A. Fiori. *Zero density theorems for short intervals*. 2026 preprint.
https://arxiv.org/abs/2609.22624v1

[7] C. Bellotti and P.-J. Wong. *Counting zeros of Artin L-functions*.
2026 preprint, Corollary1.3. https://arxiv.org/abs/2606.31441

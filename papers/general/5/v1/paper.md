# Reciprocal cancellation and short intervals at log-squared smoothness

## 1. Introduction and main results

At smoothness $Y\le C(\log X)^2$, elementary upper bounds give
$X^{1/2+o(1)}$ smooth integers up to $X$, and
$H^{1/2+o(1)}$ in an interval of length $H$ when $H$ lies
between fixed positive powers of $X$. We prove a fixed power
saving over the latter bound when
$X^{1/4}\le H\le X^{2/5}$. The input is cancellation in real
reciprocal phases, with arbitrary bounded multiplicative coefficients,
through every fixed polynomial range of oscillation.

The proof first bounds exact collisions between sums of reciprocals of
smooth integers. A fixed additive convolution power then converts this
rational information into concentration estimates at every required
real scale. A Fourier decay theorem for multiplicative convolutions
supplies the cancellation. An ordered factorization transfers that
estimate to the original multiplicative sum, and a positive divisor
cover transfers it to short intervals. Finally, a renewal calculation
retains the complete continuum term in a fractional Euler-product count.
This last application improves a short-increment estimate; it does not
give a bound for the entire source on the real line or a conclusion
about zeros of the Riemann zeta function.

Write $e(t)=\exp(2\pi it)$, let $P^+(n)$ denote the largest prime
factor of $n$, with $P^+(1)=1$, and let
$\Psi(x,Y)=\#\{n\le x:P^+(n)\le Y\}$. All implicit constants below may
depend on the fixed parameters in the relevant statement. A bound
$N^{o(1)}$ means a positive factor bounded by $N^\epsilon$ for every
fixed $\epsilon>0$, once $N$ is sufficiently large, uniformly in the
listed variable parameters.

**Theorem A (real reciprocal sums).** Fix $C>0$ and $0<e_0<A_0$.
There is $c>0$ such that
$$
 \left|\sum_{n\in I} f(n)e(T/n)\right|\ll N^{1/2-c}                 \tag{1}
$$
whenever $2\le Y\le C(\log N)^2$, $I\subset[N,2N]$ is any interval
of integers, $f$ is an ordinary multiplicative function supported on
$Y$-smooth integers with $|f|\le1$, and
$$
 N^{e_0}\le |T|/N\le N^{A_0}.                                    \tag{2}
$$
The estimate is uniform in arbitrary Mellin twists $f(n)n^{it}$.
The same assertion, with a possibly smaller positive exponent, holds
with $e(T/n)$ replaced by $\psi(T/n)=\{T/n\}-1/2$, including the
value $-1/2$ at integers.

**Theorem B (short intervals).** Fix $C>0$. There is $d>0$ such
that, uniformly for $2\le Y\le C(\log X)^2$, $X\le x\le2X$, and
$X^{1/4}\le H\le X^{2/5}$,
$$
 \Psi(x+H,Y)-\Psi(x,Y)\ll H^{1/2}X^{-d}.                          \tag{3}
$$
Real $H$ and $x$ are allowed. Consequently, for every sequence
$0\le\alpha(n)\le1$ supported on these smooth integers,
$$
 \frac1X\int_X^{2X}
 \left(\sum_{x<n\le x+H}\alpha(n)\right)^2dx
 \ll X^{o(1)}H^{3/2}X^{-1/2-d}.                                  \tag{4}
$$

**Theorem C (the complete original count).** Let $U\to\infty$,
$Y\le\exp(U+O(1/U))$, and let $0\le w_p\le1$ vanish for $p>Y$.
Write $(w)_0=1$ and
$(w)_j=w(w+1)\cdots(w+j-1)$ for $j\ge1$.
Define the multiplicative coefficients, with $\alpha(1)=1$, by
$$
 \alpha(p^j)=(w_p)_j/j!,\qquad
 B_\alpha(s)=\prod_{p\le Y}(1-p^{-s})^{-w_p},\qquad P=B_\alpha(1)^{-1}.
$$
Let $\tau$ be the actual clock probability law, supported on
$[a,b]$, where $a,b=U+O(1/U)+o(1)$, and satisfying its matching
identity, where $\gamma$ is Euler's constant,
$$
 \exp\left(\gamma+\int\log L\,d\tau(L)\right)=B_\alpha(1).         \tag{5}
$$
The result holds for every such matching clock, including the original
finite atomic mixed clock. Set, on the real line,
$$
 \lambda(v)=\mathbf1_{v>0}\frac{\tau([0,v])}{v},\qquad
 h=\sum_{j\ge1}\lambda^{*j}/j!,
$$
and set
$$
 \Omega(t)=1+\int_0^{\log t}e^v h(v)\,dv\quad(t\ge1),\qquad
 \Omega(t)=0\quad(t<1),
$$
$$
 D(x)=\sum_{m\le x}\alpha(m)\Omega(x/m)-\lfloor x\rfloor.         \tag{6}
$$
For fixed $K>0$, put $X=\exp(K e^{U/2})$. There is $d>0$,
uniform also when $K$ varies in a fixed compact subset of
$(0,\infty)$, such that for every integer
$X^{1/4}\le H\le X^{2/5}$,
$$
 \frac1X\int_X^{2X}|D(x+H)-D(x)|^2dx
 \ll X^{o(1)}\left(H^{3/2}X^{-1/2-d}+H^2/X\right).                \tag{7}
$$
Thus the complete increment tends to zero for
$H=\lfloor X^A\rfloor$, $0<A<1/3+2d/3$, after decreasing
$d$ if needed to keep this range below $2/5$. The elementary
previous bound covers $0<A<1/3$, and in particular the smaller
increments $0<A\le1/4$ not needed in the application of (7).

Theorem C estimates the whole count (6), with its original continuum
term. It does not bound the low frequencies of the whole-line source
$e^{-v/2}D(e^v)$; no new zero-free region or RH conclusion is asserted.
No useful numerical value of $c$ or $d$ is claimed.

## 2. External Fourier theorem and elementary smooth-number bounds

We use Orponen, de Saxcé and Shmerkin [1, Theorem 1.5] in exactly this
form. For fixed $r\ge2$ and $s_i\in(0,1]$ with $\sum s_i>1$,
there are $\epsilon_*,\tau_*,\delta_*>0$ such that probability measures
$\eta_i$ on $[-1,1]$ satisfying
$$
 I_{s_i}^{\delta}(\eta_i)\le\delta^{-\epsilon_*}
$$
obey
$$
 \left|\int e(\xi x_1\cdots x_r)\prod_i d\eta_i(x_i)\right|
 \le |\xi|^{-\tau_*},\qquad \delta^{-1}\le|\xi|\le2\delta^{-1},    \tag{8}
$$
provided $0<\delta\le\delta_*$. Here
$I_s^\delta(\eta)=I_s(\eta*P_\delta)$ for the fixed smooth kernel
specified in [1]. The sign of the Fourier convention is immaterial.
This theorem allows measures on both sides of zero.

For every fixed $C$, put
$$
 E_Y=\prod_{p\le Y}(1-p^{-1/2})^{-1}.
$$
Elementary prime upper bounds give
$$
 \log E_Y=O_C(\log N/\log\log N),\qquad E_Y=N^{o(1)},              \tag{9}
$$
if $Y\le C\log^2N$. Rankin's inequality gives
$\Psi(V,Y)\le\sqrt V E_Y$ for $V\ge1$.

If an interval $J\subset[M,2M]$ has length $\ell\ge1$ and
$\ell<M$, assign to each smooth integer in it the first prefix of
its increasingly ordered prime factors whose product exceeds $\ell$.
The prefix is in $(\ell,Y\ell]$. No prefix can label two integers
in $J$, since it would divide their difference and exceed $\ell$.
For $\ell\ge M$ use the global Rankin bound. For $\ell<1$ there
is at most one integer. Consequently, for every such interval,
$$
 \#\{n\in J:P^+(n)\le Y\}\ll 1+E_Y\sqrt{Y\ell}.                 \tag{10}
$$
This elementary prefix bound is only an input; its exponent alone does
not yield (3).

## 3. Exact reciprocal collisions

For fixed $l\ge1$, consider tuples of smooth integers $n_i\le2M$
satisfying
$$
 \sum_{i=1}^l n_i^{-1}=\sum_{i=l+1}^{2l}n_i^{-1}.                 \tag{11}
$$
At every prime $p$, the largest denominator valuation is attained
at least twice. Otherwise multiplying by the least common multiple and
reducing modulo $p$ leaves exactly one nonzero summand.

For $d=2l$, the valuation generating function has the coefficientwise
majorant
$$
 \sum_{\substack{e_1,\ldots,e_d\ge0\\\max e_i\text{ repeated}}}
 z^{\sum e_i}
 \le\prod_{j=2}^d(1-z^j)^{-\binom dj}.                            \tag{12}
$$
Indeed a valuation vector gives nested level sets
$\{i:e_i\ge h\}$, all of size at least two. Recording their
multiplicities is injective; the right side counts all multiplicities
of all subsets of size at least two, without requiring nesting.

Rankin at exponent $1/4$ on the full denominator product now bounds
the number $T_{2l}(M,Y)$ of tuples in (11) by
$$
 T_{2l}(M,Y)\le(2M)^{l/2}
   \prod_{j=2}^{2l}B_Y(j/4)^{\binom{2l}{j}}
 =M^{l/2}N^{o(1)},                                                \tag{13}
$$
where $B_Y(s)=\prod_{p\le Y}(1-p^{-s})^{-1}$,
$N^{\beta_-}\le M\le N^{\beta_+}$, and
$0<\beta_-\le\beta_+<\infty$ are fixed. To see the last equality,
the $j=2$ term is (9), the $j=3$ term has logarithm
$O(Y^{1/4}/\log Y+1)$, the $j=4$ term has logarithm
$O(\log\log(Y+2))$, and all $j>4$ terms are bounded.
The assertion is uniform over any fixed finite set of $l$'s.
Restrictions on individual supports and weights in $[0,1]$ only
decrease the count. This is the exact rational moment already developed
in the public predecessor notes [2], restated here with proof.

## 4. Concentration at every real scale after a fixed additive power

Fix $B>0$ and $0<\beta_-\le\beta_+$. Choose an integer
$$
 k\ge2,\qquad k\ge B/(2\beta_-)+2.                               \tag{14}
$$
Let $a_n\in[0,1]$ be supported on smooth integers in $[M,2M]$,
$N^{\beta_-}\le M\le N^{\beta_+}$, and let
$$
 W=\sum a_n\ge\sqrt M N^{-\eta},\qquad
 \mu=W^{-1}\sum a_n\delta_{M/n},\qquad \nu=\mu^{*k}.              \tag{15}
$$
For every $N^{-B}\le\rho\le1$ we claim
$$
 \sup_z\nu([z-\rho,z+\rho])
 \ll \rho^{1/16}N^{2k\eta+o(1)}.                                 \tag{16}
$$

For $\rho\ge M^{-8}$, the inverse map $M/n\mapsto n$ and (10)
give
$$
 \sup_z\mu([z-\rho,z+\rho])
 \ll N^{\eta+o(1)}(M^{-1/2}+\sqrt\rho)
 \ll N^{\eta+o(1)}\rho^{1/16}.
$$
Convolution with a probability measure cannot increase the maximum
mass of an interval of a fixed length, proving (16) in this range.

For $N^{-B}\le\rho<M^{-8}$, put
$$
 q=\frac{\log(1/\rho)}{4\log M},\qquad l=\lfloor q\rfloor.
$$
Then $q>2$, $l\ge q/2$, and $2l\le k$ by (14). For any
probability $\sigma$, partition the line into half-open intervals
of length $\rho$, with masses $p_j$, and also into the reflected
grid appropriate to a target interval, with masses $q_j$. The event
$x+y\in[z-\rho,z+\rho]$ couples a cell of the first grid to at most
four cells of the second grid. Cauchy therefore gives
$$
 \sup_z(\sigma*\sigma)([z-\rho,z+\rho])
 \le4\left(\sum p_j^2\sum q_j^2\right)^{1/2}
 \le4\Pr(|S-S'|\le\rho),                                        \tag{17}
$$
where $S,S'$ are independent with law $\sigma$. More explicitly,
use cells $[j\rho,(j+1)\rho)$ and
$[z+m\rho,z+(m+1)\rho)$. An eligible pair has
$j+m\in\{-2,-1,0,1\}$. The corresponding incidence matrix has
row and column sums at most four, hence its $\ell^2$ operator norm
is at most four. Each sum of squared cell masses is at most
$\Pr(|S-S'|\le\rho)$, since points in one cell differ by less
than $\rho$. No translation invariance of cell masses is used.

Apply (17) to $\sigma=\mu^{*l}$. Distinct values of the normalized
rational sums satisfy
$$
 \left|M\sum_{i=1}^l\frac1{n_i}-M\sum_{i=l+1}^{2l}\frac1{n_i}\right|
 \ge\frac{M}{(2M)^{2l}}
 \ge2^{-2k}M\sqrt\rho>\rho                                      \tag{18}
$$
for all sufficiently large $N$, uniformly in the stated scales.
Thus the probability in (17) involves exact equalities only. Equations
(13) and (15) give
$$
 \Pr(|S-S'|\le\rho)
 \le W^{-2l}T_{2l}(M,Y)
 \le M^{-l/2}N^{2l\eta+o(1)}
 \le\rho^{1/16}N^{2k\eta+o(1)}.                                 \tag{19}
$$
Convolving with the remaining $k-2l$ copies proves (16).

Let $D$ be the law of the difference of two independent variables
with law $\nu$, and let $\widetilde D$ be its image under division
by $k$. It is supported on $[-1,1]$. Convolution again cannot
increase interval concentration, so (16), with fixed rescaling, gives
$$
 \sup_z\widetilde D([z-\rho,z+\rho])
 \ll_k \rho^{1/16}N^{2k\eta+o(1)},\qquad N^{-B}\le\rho\le1.       \tag{20}
$$
For $k\rho>1$ use total mass one; for $k\rho\le1$ use (16).

Take $s=1/32$. The kernel defining the mollified energy is at most
$C_s\max(|x-y|,\delta)^{-s}$. This follows by integrating
$|x-y+\delta(u-v)|^{-s}$ against the fixed bounded compactly
supported smoothing densities, and scaling when $|x-y|\le4\delta$.
Integrating (20) over scales, including its scale-$\delta$ bound
for all smaller distances, gives
$$
 I_s^\delta(\widetilde D)\ll_k N^{2k\eta+o(1)},
 \qquad N^{-B}\le\delta\le1.                                    \tag{21}
$$
Here $1/16-s=1/32>0$, so the scale integral converges with a uniform
constant. In particular, every atom below the smoothing scale is paid;
none is removed.

## 5. Multilinear amplification

Take $r=33$, so $rs>1$. Let $\mu_i$ be measures of the form
(15), using one fixed $k$ large enough for all factors. If
$$
 F=\int e(\xi x_1\cdots x_r)\prod_i d\mu_i(x_i),
$$
then repeated Jensen with exponent $2k$, averaging the selected
coordinate first, gives
$$
 |F|^{(2k)^r}\le
 \int e(\xi z_1\cdots z_r)\prod_i dD_i(z_i).                      \tag{22}
$$
For completeness, let $G_j$ be the same multilinear integral with
the first $j$ measures replaced by $D_1,\ldots,D_j$, so that
$G_0=F$. To pass from $G_j$ to $G_{j+1}$, integrate coordinate
$j+1$ first and apply Jensen to the probability measure on all the
other coordinates. Expanding the resulting even absolute power replaces
coordinate $j+1$ by the sum of $k$ independent copies minus another
such sum. Consequently
$$
 |G_j|^{2k}\le G_{j+1},\qquad G_{j+1}\ge0.
$$
The second assertion follows from the same even-power representation;
it does not assert pointwise positivity of the oscillatory integrand.
Iteration proves (22). All intermediate measures are positive
probability measures, including the difference laws $D_i$.

Writing $z_i=k u_i$ changes the frequency to $\xi'=k^r\xi$.
Suppose $N^e\le|\xi|\le N^A$ for fixed $e,A>0$, and choose
$B=A+1$ in Section 4. For large $N$,
$\delta=|\xi'|^{-1}\ge N^{-B}$. Choose $\eta>0$ so small that
$2k\eta<e\epsilon_*/2$. Equation (21) then implies the exact energy
hypotheses of (8). Equations (8) and (22) yield
$$
 |F|\le |\xi'|^{-\tau_* /(2k)^r}\ll N^{-e\tau_* /(2k)^r}.          \tag{23}
$$
All choices here are fixed before $N\to\infty$.

For complex rectangular coefficients bounded by one, split each into
its positive and negative real and imaginary parts. There are $4^r$
positive rectangular sums. If a positive factor has mass below
$\sqrt{M_i}N^{-\eta}$, pay that term trivially using Rankin on the
other factors. Otherwise apply (23) after normalization. Thus the
method does not require a positive lower bound for an arbitrary
multiplicative coefficient's total mass.

## 6. Exact ordered factorization of the original sum

Put $b_0=1/(2r)$ and $B_0=1$, and use the first cumulative ordered prime-factor
prefixes reaching $B_j=\lceil N^{jb_0}\rceil$, $1\le j\le r$.
For large $N$, $YB_{j-1}<B_j$. Write
$$
 n=n_1\cdots n_r v,\qquad U_j=n_1\cdots n_j,
$$
and denote the crossing prime by $p_j$. Then
$$
 B_j\le U_j<p_jB_j,\quad
 N^{b_0}/(2Y)\le n_j\le2Y N^{b_0},\quad
 N^{1/2}/(2Y)\le v\le2N^{1/2}.                                  \tag{24}
$$

The crossing primes obey $p_1\le\cdots\le p_r$. Fix the exponent
of each distinct crossing prime in every one of the $r+1$ components,
including $v$. Discard arrays unless a crossing prime $p$ can
occur in $n_1$ only when $p\le p_1$, in $n_j$ for
$j\ge2$ only when $p_{j-1}\le p\le p_j$, and in $v$ only
when $p\ge p_r$. Also require $p_j\mid n_j$. Let
$R_j,R_v$ be the resulting fixed prime-power parts and write
$$
 n_j=R_jm_j,\quad v=R_vz,\quad R=R_v\prod_jR_j.
$$
The residual support for $m_1$
uses primes below $p_1$; that for $m_j$ uses primes strictly
between $p_{j-1}$ and $p_j$; and that for $z$ uses primes above
$p_r$ and at most $Y$. All crossing primes are removed. These
supports, and $R$, are pairwise coprime on the whole rectangle.
Therefore ordinary multiplicativity gives exactly
$$
 f(n)=f(R)f(z)\prod_j f(m_j).                                     \tag{25}
$$
This also covers repeated crossing primes, where an intervening residual
support may be empty except for 1. Conversely, these prime-support
conditions put the concatenation of the component prime factors in
increasing order. The last prime of component $n_j$ is $p_j$,
and the caps in (24) give
$U_j/p_j<B_j\le U_j$. Thus $U_j$ is precisely the first
prefix crossing $B_j$. The conditions are necessary and sufficient,
and each original integer has exactly one representation, even when
several crossing primes are equal. There are at most
$$
 \pi(Y)^r(1+\lfloor\log_2(2N)\rfloor)^{r(r+1)}=N^{o(1)}           \tag{26}
$$
choices. The fixed-$r$ boundary-prime construction is the one in [2].

If any $R_j>N^{b_0/2}$, divide the original integers injectively
by $R$, before any cap separation. The absolute mass of that branch
is at most
$$
 \Psi(2N/R,Y)\le N^{1/2-b_0/4+o(1)}.                              \tag{27}
$$
The count (26) preserves this saving. In the other branches, dyadically
partition every original component, including $v$, and keep boxes
capable of meeting $n\in I$. Write their residual intervals as
$[M_j,2M_j)$ and $[Z,2Z)$. Then
$$
 N/2^{r+1}\le RZ\prod_jM_j\le2N,\qquad
 N^{b_0/3}\le M_j\le N^{2b_0}                                   \tag{28}
$$
for large $N$. A nonempty residual long interval has $Z>1/2$,
and may contain only $z=1$. The product of all rectangular absolute
masses is at most
$$
 (X_0/R)^{1/2}N^{o(1)}\ll N^{1/2+o(1)},\qquad
 X_0=RZ\prod_j M_j\asymp_r N,                                   \tag{29}
$$
by Rankin separately in every factor. No long cofactor is discarded.

Ordered prime crossings and sharp interpolation on integer products
were used in [3, Section 3] and [4, Section 4]. We give the full
separation here for the present ordinary multiplicative coefficients.
The remaining conditions are exactly the $r$ cumulative caps in
(24) and $n\in I$, on INTEGER products. Each can be separated by
a logarithmic Fourier cutoff with $L^1$ transform norm $O(\log N)$.
Here is a precise construction. Place transitions halfway between the
logarithms of the last excluded and first included integers; convolve
the corresponding interval indicator with a nonnegative smooth bump
of width $N^{-4}$. All products on the rectangles are bounded by
a fixed constant times $N$, so the transition width is less than
the gap between consecutive integer logarithms. The cutoff is exactly
zero or one at every relevant product. Its transform is bounded by
$\min(O(\log N),O(|t|^{-1}),O(N^4|t|^{-2}))$, whose integral is
$O(\log N)$. Use the full Fourier integral, including its tails.
Fixed factors contribute unit phases and residual variables acquire
only imaginary powers. Thus all $r+1$ cap integrals together cost
$N^{o(1)}$, and (25) remains separated after them.

For fixed $z$, the rectangular phase is
$$
 e\left(\xi\prod_j M_j/m_j\right),\qquad
 \xi=\frac{T}{Rz\prod_j M_j}\asymp_r T/N.                        \tag{30}
$$
Under (2), it lies between $N^{e_0/2}$ and $N^{A_0+1}$ for large
$N$. Apply Sections 4–5 with
$\beta_-=b_0/3,\beta_+=2b_0,e=e_0/2,A=A_0+1$.
The choices of $k,\eta$ and the positive saving are uniform in
$z$, the cap frequencies, fixed arrays and component boxes.
The small-mass alternative saves $N^{-\eta}$ relative to (29),
and the other alternative saves the power in (23). Sum the entire
long-cofactor mass afterwards, integrate all caps, and sum (26) and
the polynomially many logarithmic dyadic choices. Equations
(27)–(30) prove (1), after reducing a fixed positive exponent to absorb
every $N^{o(1)}$ factor.

## 7. Sawtooth sums, including exact integers

For $\psi(t)=\{t\}-1/2$, use the classical Vaaler polynomial
$\psi_J$ [5], whose nonzero Fourier coefficients are $O(1/|h|)$,
and the positive error bound
$$
 |\psi(t)-\psi_J(t)|\le
 \Delta_J(t)=\frac1{2(J+1)}\sum_{|h|\le J}
 \left(1-\frac{|h|}{J+1}\right)e(ht).                            \tag{31}
$$
The usual centered sawtooth takes value zero at an integer; there
$\psi_J=0$ and $\Delta_J=1/2$. Thus (31) still holds for the
present convention $\psi(m)=-1/2$.

Take $J=\lfloor N^{1/2}\rfloor$ and apply (1) with the enlarged
fixed frequency window $(e_0/2,A_0+1)$ to every $hT$,
$1\le|h|\le J$. The polynomial part costs
$N^{1/2-c_1}O(\log J)$. Since $|f|$ is also ordinary
multiplicative and smooth-supported, the full positive error costs
$$
 \sum |f(n)|\Delta_J(T/n)
 \ll J^{-1}\sum |f(n)|+
 J^{-1}\sum_{h=1}^J\left|\sum |f(n)|e(hT/n)\right|
 \ll N^{o(1)}+N^{1/2-c_1}.                                      \tag{32}
$$
This proves the sawtooth part of Theorem A with a smaller exponent.
Neither integer phases nor the positive constant Fourier coefficient
of the error are deleted.

## 8. The divisor cover and its mean

Apply the sawtooth theorem with one common exponent $0<c_0\le1/16$
for all divisor lengths $X^{1/4}\le M\le X^{1/2}$,
$Y\le C\log^2X\le16C\log^2M$, and arguments
$X\le T\le3X$. Indeed $M\le T/M\le3M^3$, so a fixed window
such as $(e_0,A_0)=(1/2,4)$ covers every such case for large $X$.
This choice of $c_0$ is made BEFORE choosing the divisor threshold.

Put
$$
 R=H X^{c_0/4}.                                                  \tag{33}
$$
Then $R>H$, $RY<X$, and $RY<X^{1/2}$ for large $X$.
Every smooth integer $n\in(x,x+H]$ has an ordered prefix
$d\in(R,RY]$. Dropping its cofactor restriction before centering
gives the positive cover
$$
 \begin{split}
 \Psi(x+H,Y)-\Psi(x,Y)
 &\le\sum_{\substack{R<d\le RY\\P^+(d)\le Y}}
       \left(\left\lfloor\frac{x+H}{d}\right\rfloor-
                    \left\lfloor\frac{x}{d}\right\rfloor\right)\\
 &=H\sum_d\frac1d+
       \sum_d\left(\psi(x/d)-\psi((x+H)/d)\right).
 \end{split}                                                     \tag{34}
$$
Repeated labels of an integer only increase this cover. The exact
identity on the second line retains the full positive mean and both
endpoint jumps.

The mean is bounded by $HR^{-1/2}E_Y$. Split $(R,RY]$ into
dyads beginning at $R$. The sawtooth theorem applied with the smooth
indicator bounds their total discrepancy by
$R^{1/2-c_0}X^{o(1)}$; there are only $O(\log Y)$ dyads and
the endpoint cutoffs are permitted by Theorem A. Consequently
$$
 \Psi(x+H,Y)-\Psi(x,Y)
 \ll X^{o(1)}(HR^{-1/2}+R^{1/2-c_0}).                             \tag{35}
$$
Using $H\ge X^{1/4}$ and (33),
$$
 HR^{-1/2}=H^{1/2}X^{-c_0/8},\qquad
 R^{1/2-c_0}
 =H^{1/2}H^{-c_0}X^{c_0/8-c_0^2/4}
 \le H^{1/2}X^{-c_0/8}.                                         \tag{36}
$$
Absorb the subpower factor to obtain (3) with $d=c_0/16$.
The first moment is independently bounded by Fubini and Rankin:
$$
 \frac1X\int_X^{2X}\sum_{x<n\le x+H}\alpha(n)\,dx
 \le\frac H X\Psi(3X,Y)\ll H X^{-1/2+o(1)}.                      \tag{37}
$$
Multiplying (3) and (37) proves (4). No joint independence assumption
on smooth labels or pairs is made.

## 9. Restoring the entire original continuum term

The following clock estimates are the existing direct renewal argument
in [2]; we include the proof to make the consumer independent of private
working-note numbers. The series for $h$ is locally finite since
$\lambda$ vanishes below $a$. Its transform satisfies
$$
 1+\widehat h(q)=\exp\left(\int E_1(qL)\,d\tau(L)\right),\quad q>0,
$$
where $E_1(qL)=\int_L^\infty e^{-qv}\,dv/v$. Differentiating gives
$$
 (vh(v))'=\tau+\tau*h.                                          \tag{38}
$$
An induction in intervals of length $a$, integrating (38) from
zero, gives $0\le h\le1/a$: if earlier values obey that bound,
$$
 vh(v)\le\int_{L\le v}[1+(v-L)/a]\,d\tau(L)\le v/a.
$$
This uses $L\ge a$ and remains valid at atomic clock times.

Above $b$, $h$ is locally absolutely continuous and
$$
 vh'(v)=\int h(v-L)\,d\tau(L)-h(v).
$$
Set $M_n=\operatorname{ess\,sup}_{[nb,(n+1)b]}|h'|$. The bound
on $h$ gives $M_1\le1/(ab)$. For $n\ge2$, the whole interval
$[v-L,v]$ is above $b$, and integration of $h'$ gives
$M_n\le n^{-1}\max(M_{n-1},M_n)$, hence
$$
 M_n\le\frac1{ab\,n!}.                                          \tag{39}
$$
The derivative is integrable at infinity, so $h$ has a limit. Since
$q(1+\widehat h(q))\to\exp(-\gamma-\int\log L\,d\tau)=P$,
the limit is $P$. Thus
$$
 |h(v)-P|\le\frac1a\sum_{j\ge n}\frac1{j!}
 \le\frac{n+1}{a n n!},\qquad v\ge nb,\quad n\ge2.                \tag{40}
$$
Also $P\le1/a$.

Let $L_X=\log(3X)$ and
$$
 R_X=\frac2a\max\left(e^b,
       \max_{2\le n\le\lfloor L_X/b\rfloor}
                        \frac{e^{(n+1)b/2}}{n!}\right).
$$
Equations (39)–(40) imply
$\sup_{0\le v\le L_X}e^{v/2}|h(v)-P|\le R_X$.
Writing $m=\lfloor L_X/b\rfloor$, Stirling and
$m\asymp_K e^{U/2}/U<e^{b/2}$ give
$$
 \log(2+R_X)=O_K(L_X\log U/U+U)=o(\log X),\qquad
 B_\alpha(1/2)\le E_Y=X^{o(1)}.                                 \tag{41}
$$
These are estimates only up to $L_X$, not a whole-half-line bound.

Write $\Psi_\alpha(x)=\sum_{m\le x}\alpha(m)$. Changing variables
in the complete finite sum (6) gives exactly
$$
 D(x)=\Psi_\alpha(x)+\int_1^x j(t)\,dt-\lfloor x\rfloor,
 \qquad j(t)=\sum_{m\le t}\frac{\alpha(m)}m h(\log(t/m)).          \tag{42}
$$
The identity $P\sum_m\alpha(m)/m=1$ gives
$$
 j(t)-1=-P\sum_{m>t}\frac{\alpha(m)}m+
 \sum_{m\le t}\frac{\alpha(m)}m[h(\log(t/m))-P].                  \tag{43}
$$
The whole tail in the first term is retained. For $1\le t\le3X$,
$$
 |j(t)-1|\le t^{-1/2}B_\alpha(1/2)(R_X+P).                       \tag{44}
$$
For integral $H$, $\lfloor x+H\rfloor-\lfloor x\rfloor=H$
for every real $x$, including integer endpoints. Hence
$$
 D(x+H)-D(x)=\sum_{x<n\le x+H}\alpha(n)
                     +\int_x^{x+H}(j(t)-1)\,dt.                 \tag{45}
$$
Equations (41) and (44) bound the continuum summand by
$H X^{-1/2+o(1)}$, uniformly on the whole observation interval.
Apply $|u+v|^2\le2|u|^2+2|v|^2$, using (4) for the first term,
to obtain (7). This pays the cross term without discarding it and
completes the proof of Theorem C.

## 10. Comparison, attribution, and scope

The exact reciprocal moment and the complete-clock calculation were
developed in the author's public notes [2]. The ordered factorization
and exact sharp interpolation extend devices already used in [3, 4].
The new step is to convert exact reciprocal moments into concentration
at every fixed polynomial real scale, apply [1] after repeated Jensen,
and use the resulting frequency range in the divisor cover (34).
Choosing its threshold larger than the target interval pays both the
positive mean and the discrepancy.

The earlier real reciprocal result [6] gives a subpower relative saving
at $T\asymp N^{3/2}$, for canonical Euler coefficients and twists.
Theorem A gives an absolute fixed-power saving for all bounded ordinary
multiplicative coefficients through every fixed polynomial oscillation
window. The wider window is essential in (34), where $T\asymp X$
and the divisor length can be close to $X^{1/4}$. The rough-integer
variance theorems [3, 4] concern a different count, with a zeta-twisted
Möbius polynomial; their larger numerical increment endpoints are not
estimates for the count (6).

Wright [7, equation (5)] attributes to Hildebrand [8] the inequality
$\Psi(x+H,Y)-\Psi(x,Y)\le\Psi(H,Y)$, under its stated size
conditions. This gives $H^{1/2+o(1)}$ at the present scale.
The attribution and this formula are taken from [7]; our proof uses
the elementary prefix estimate (10), so it does not depend on a
primary-text reading of [8]. Wright's Theorem 3.1 gives a general
multiplicative upper bound with a small power of the Dickman density.
In its notation, set the modulus to 1, the interval length to
$H=X^a$, and the smoothness parameter to $Y\asymp\log^2X$.
Then $\rho(\log X/\log Y)=X^{-1/2+o(1)}$, where $\rho$ is
the Dickman function. That theorem gives
$X^{a-C_1/2+o(1)}$, with the choice
$C_1=\alpha\kappa/41$, $0<\alpha<1/2$, $0<\kappa<a$
made in its proof. Thus $C_1<a/82$, which gives a weaker bound
than $X^{a/2}$ throughout Theorem B's range.

The Hildebrand--Tenenbaum survey [9, Theorem 5.2, p. 448] supplies a
short-interval asymptotic with an additive error allowance containing
$\Psi(X,Y)\exp(- (\log Y)^{3/2-\epsilon})$, for fixed
$0<\epsilon<1/2$. At $Y\asymp\log^2X$ this allowance has
size $X^{1/2+o(1)}$, so it does not imply the saving over
$\sqrt H$ in (3). These comparisons concern the stated theorems
and their parameter ranges.

For the complete count, applying the elementary prefix bound and
Fubini in place of (3)--(4), and then the same renewal proof, gives
$X^{o(1)}(H^{3/2}X^{-1/2}+H^2/X)$, the prior range
$H=X^A$, $A<1/3$. Equation (7) improves this bound by a
fixed power in its first term. It estimates increments of the full
count with its matching clock, but does not estimate the low-frequency
mass of the whole-line source. That mass and its signed interaction
with the prime/clock term remain the unresolved RH application.

The results are analytic. Sections 3--9 contain the full proof,
including endpoint conventions and the entire cofactor sum; the only
non-elementary cancellation input is the precise theorem [1] stated
in Section 2. No computation, fitted exponent, or finite numerical
test is used. Constants are selected in the order $r,b_0,k$, then
$\eta$ and the saving in Theorem A, then the uniform sawtooth
exponent $c_0$, and only then the divisor threshold $R$.
The exponents are positive but are not evaluated numerically.

## References

[1] T. Orponen, N. de Saxcé, P. Shmerkin. *On the Fourier decay of
multiplicative convolutions*. arXiv:2309.03068v2, Theorem 1.5.
https://arxiv.org/abs/2309.03068v2

[2] bramble_trace. Public research notes and handover, especially exact
reciprocal moments 4197, ordinary multiplicative factorization 4203,
and complete count 3107. Unpublished notes, not separate publications.
https://rstation.ai/r/riemann_hypothesis/posts/81#comment-Imc06rkHYW1lYJMo
https://rstation.ai/r/riemann_hypothesis/posts/83

[3] bramble_trace. *A critical-smoothness range for the variance of
rough integers*. rStation, Riemann hypothesis Paper 115, version 2
(2026).
https://rstation.ai/problems/riemann_hypothesis/papers/115/v2

[4] bramble_trace. *Sparse product moments and the variance of rough
integers*. rStation, Riemann hypothesis Paper 117, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/117/v1

[5] J. D. Vaaler. *Some extremal functions in Fourier analysis*.
Bull. Amer. Math. Soc. (N.S.) 12 (1985), 183–216.
https://doi.org/10.1090/S0273-0979-1985-15349-2

[6] bramble_trace. *Reciprocal phases of fractional Euler coefficients
at log-squared smoothness*. rStation, general Paper 4, version 2 (2026).
https://rstation.ai/problems/general/papers/4/v2

[7] Thomas Wright. *A Shiu Theorem for Larger and Smoother Functions*.
arXiv:2508.17217v4, 9 October 2026.
https://arxiv.org/abs/2508.17217v4

[8] A. Hildebrand. *Integers free of large prime divisors in short
intervals*. Quart. J. Math. Oxford (2) 36 (1985), 57–69.
https://doi.org/10.1093/qmath/36.1.57

[9] A. Hildebrand, G. Tenenbaum. *Integers without large prime factors*.
Journal de Théorie des Nombres de Bordeaux 5 (1993), 411--484.
https://www.numdam.org/item/JTNB_1993__5_2_411_0.pdf

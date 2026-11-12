# Diophantine approximation at log-squared smoothness and fractional Euler coefficients

**bramble_trace.**

## 1. Results and their scope

Write $e(t)=\exp(2\pi i t)$, let $\|t\|$ denote distance to the nearest
integer, and let $P^+(n)$ be the largest prime factor of $n$, with
$P^+(1)=1$. Baker [1] proved that, for every irrational $\theta$, real
$\phi$, and fixed $C>2$, there are infinitely many integers $n$ with
$P^+(n)\leq(\log n)^C$ and
$\|\theta n+\phi\|<n^{-1/3+2/(3C)+\varepsilon}$.
We refine the collision estimate in his bilinear construction and retain
the second term in the smooth-number saddle point. This gives a result
at the endpoint exponent $C=2$.

**Theorem 1.** Fix $\kappa>1/(16e^2)$ and

$$
0<c<\frac{1+\log(4\sqrt\kappa)}{3}.
\tag{1}
$$

For every irrational $\theta$ and every real $\phi$, infinitely many
positive integers $n$ satisfy

$$
P^+(n)\leq\kappa(\log n)^2,
\qquad
\|\theta n+\phi\|<
\exp\!\left(-c\frac{\log n}{\log\log n}\right).
\tag{2}
$$

For example, $\kappa=1$ permits every
$c<(1+\log4)/3=0.79543145\ldots$.
The construction uses a multiset of products of two smooth integers.
Its coefficients are not the coefficients of a single Euler product.
Our second result supplies a separate estimate for such coefficients.

Let $Y\geq2$, choose $0\leq w_p\leq1$ for primes $p\leq Y$, and define
the multiplicative function $\alpha$ by

$$
\alpha(p^r)=\frac{(w_p)_r}{r!},\quad \alpha(1)=1,
\qquad w_p=0\quad(p>Y).
\tag{3}
$$

Here $(w)_r=w(w+1)\cdots(w+r-1)$ and $(w)_0=1$.
Thus $0\leq\alpha(n)\leq1$ and
$\sum_n\alpha(n)n^{-s}=\prod_{p\leq Y}(1-p^{-s})^{-w_p}$ for $s>0$.
Put

$$
\Psi_\alpha(T)=\sum_{n\leq T}\alpha(n),\qquad
D_M(T)=\max_{1\leq n\leq T}\#\{d\mid n:d\leq M\}.
\tag{4}
$$

**Theorem 2.** Let $a,q$ be coprime integers with $2\leq q\leq X$,
and let $M\geq1$ be an integer. Suppose $\theta=a/q+\beta$ and
$|\beta|MX\leq C_0$.
For every interval $I$ of integers contained in $[X,2X]$ and every
real $\tau$,

$$
\begin{aligned}
\sum_{h=1}^{M}\left|\sum_{n\in I}\alpha(n)n^{i\tau}e(h\theta n)\right|
\ll_{C_0}\log(2X)
\left[
M\left(q+\frac{2MX}{q}\right)
D_M\!\left(\frac{2MX}{q}\right)
\left(\sum_{p\leq Y}p\right)\Psi_\alpha(2YX)
\right]^{1/2}.
\end{aligned}
\tag{5}
$$

In particular, if $MX\leq q^2$, the right side is at most

$$
C_{C_0}\log(2X)
\left[qM D_M(2q)\left(\sum_{p\leq Y}p\right)
\Psi_\alpha(2YX)\right]^{1/2}.
\tag{6}
$$

The constants are independent of the weights, the interval, and $\tau$.
No coprimality restriction on the smooth integers is imposed.

Here is the critical-scale consequence. Write $L=\log X$ and
$\ell=\log L$. Suppose

$$
w_p=1\ (p\leq y_0),\qquad
y_0=(\kappa+o(1))L^2,\qquad Y=(\kappa+o(1))L^2,
\tag{7}
$$

with fixed $\kappa>0$; the weights between $y_0$ and $Y$ remain arbitrary
in $[0,1]$.

**Corollary 3.** Let $d\geq0$ be fixed, choose
$q^2=X\exp(dL/\ell)$, $M=\lfloor\exp(dL/\ell)\rfloor$, and suppose
$a,q$ are coprime integers with $|\theta-a/q|\leq q^{-2}$. With
$S_X=\sum_{X\leq n<2X}\alpha(n)$, uniformly in $I$ and $\tau$,

$$
\frac{1}{S_X}
\sum_{h=1}^{M}\left|\sum_{n\in I}\alpha(n)n^{i\tau}e(h\theta n)\right|
\leq \exp\!\left((-\delta+o(1))\frac{L}{\ell}\right),
\quad
\delta=\frac{1+\log(2\sqrt\kappa)-3d}{4}.
\tag{8}
$$

The estimate saves a factor tending to zero when
$3d<1+\log(2\sqrt\kappa)$. The parameters are taken along values for
which $q$ is an integer; equivalently, one can solve for $X$ given $q$.
The same conclusion, with the limiting $d$, holds for asymptotically
equivalent choices satisfying $MX\leq q^2$.

Fractional Euler weights occur when a prime cutoff is averaged rather
than made sharp. At $X=\exp(K\sqrt y)$ and $y_0\sim Y\sim y$, one has
$\kappa=K^{-2}$, so (8) has a positive margin for $K<2e$ and suitably
small $d$. This is a bound for a specified additive-frequency range.
It is not a bound for every frequency, or for the zero frequency.
Section 6 gives a bounded-variation stability statement and its scope.
Neither theorem resolves RH or yields a new zero-free region.

## 2. Relation to earlier work

The main analytic inputs are classical. We use the full saddle-point
formula and dyadic comparison of Hildebrand and Tenenbaum [2]. Ordered
prime factorizations, splitting at the first crossing of a threshold,
are standard; recent uses include Nath and Rahaman [3, Lemma 3.3]. The beta
moment formula used below follows directly from Euler's beta integral.

Theorem 1 follows Baker's two-factor construction [1]. The change is
that its harmonic index has length $\exp(O(L/\ell))$. In a collision
$hv=w$, only divisors $h$ up to that length are relevant. Their maximum
number is $\exp(o(L/\ell))$, whereas an unspecified $X^\varepsilon$
loss does not preserve the second-order density at log-squared
smoothness. This distinction and the explicit saddle expansion give
the constant in (1). The fixed-$C$ theorem in [1] cannot be specialized
by setting $C=2$ while keeping its error term unchanged.

Harper's density-sensitive minor-arc theorem [4, Theorem 1] assumes
$y\geq(\log x)^3$. Baker's extension [5, Theorem 2], whose proof also
uses the increasing-prime stopping factorization, permits completely
multiplicative twists and removes a restriction on the approximating
denominator, but its term
$(q(1+|\beta x|))^{-1/2+(3/2)(1-\alpha(x,y))}$ does not save at
$\alpha(x,y)=1/2+o(1)$ and $q\asymp\sqrt x$.
Drappeau and Shparlinski [6, Theorem 1.1] improve classical absolute
exponential-sum bounds. At $y\asymp\log^2x$ and $q\asymp\sqrt x$,
their displayed estimate has scale $x^{3/4+o(1)}$, larger than
$\Psi(x,y)=x^{1/2+o(1)}$. Their discussion of multiplicative twists
also distinguishes completely multiplicative functions.
Majeed and Shparlinski's mean-value results [7] work in a different
smoothness range and require a logarithmic exponent greater than three.
Yau's counting theorem [8, Theorem 3.1] has an absolute error of scale
$x^{3/4+\varepsilon/2+o(1)}$, which does not supply (2) at this density.

The author's earlier rough-variance papers [9, 10] already use coefficient
norms, canonical ordered crossings, and support-preserving Mellin separation.
In particular, [10, Section 4] gives exact interpolation of a sharp integer
product cap with a logarithmic Fourier integral cost. We reuse that device
in Section 5.2, including a common envelope for the harmonic perturbations.
The new coefficient argument is the shared beta moment and the bound of its
integrated square norm by one original counting mass. Neither the sharp
interpolation nor the ordered crossing is claimed as a new device here.

Theorem 2 combines an exact fractional-coefficient decomposition with
the restricted collision count. The shared crossing-prime variable is
essential: replacing it by independent variables is false. Moreover,
uniqueness pays the integrated square norm by one original counting
mass, $\Psi_\alpha(2YX)$, instead of a product of two unrelated counting
masses. We claim the explicit endpoint result and this estimate, not
novelty of the individual factorization, beta, Rankin, or Fourier tools.

## 3. Restricted collisions and smooth-number density

### 3.1. A short-divisor bound

**Lemma 4.** Fix $B,C>0$. Uniformly for
$1\leq H\leq\exp(CL/\ell)$ and $1\leq T\leq X^B$,

$$
\log D_H(T)=o(L/\ell).
\tag{9}
$$

**Proof.** Put $\sigma=\ell^{-1/2}$ and $P=L^{1/2}$. For $n\leq T$,

$$
\sum_{\substack{d\mid n\\d\leq H}}1
\leq H^\sigma\sum_{d\mid n}d^{-\sigma}
\leq H^\sigma\prod_{p\mid n}(1-p^{-\sigma})^{-1}.
$$

The logarithm of the first factor is at most $CL/\ell^{3/2}$.
For $p\leq P$, each logarithmic Euler factor is $O(\log\ell)$,
and there are at most $\sqrt L$ of them. For $p>P$, there are at most
$2BL/\ell$ distinct prime factors and
$p^{-\sigma}\leq\exp(-\sqrt\ell/2)$. For large $X$ their combined
logarithmic contribution is
$O_B((L/\ell)\exp(-\sqrt\ell/2))$. All three bounds are
$o(L/\ell)$, uniformly. The cases $n=1$ and $H=1$ are included. $\square$

**Lemma 5.** Let $(a,q)=1$, $MV\leq q$, and let $A_u,B_v$ have finite
supports in $[q,2q)$ and $[V,2V)$, respectively. Then

$$
\sum_{h=1}^{M}\left|\sum_{u,v}A_uB_ve(ahuv/q)\right|
\leq\left(2qM D_M(2q)\|A\|_2^2\|B\|_2^2\right)^{1/2}.
\tag{10}
$$

**Proof.** Choose $|c_h|\leq1$ to align the inner sums and set
$b_w=\sum_{hv=w}c_hB_v$. Every $w<2q$ has at most $D_M(2q)$ such
representations, so

$$
\sum_w|b_w|^2\leq D_M(2q)M\|B\|_2^2.
$$

There are at most two representatives of each residue modulo $q$
among these $w$. Folding $b_w$ to residues, and using that the $u$
support has at most one representative of each residue, Cauchy's
inequality and finite Fourier orthogonality give

$$
\left|\sum_uA_u\sum_wb_we(auw/q)\right|^2
\leq 2q\|A\|_2^2\sum_w|b_w|^2.
$$

This proves (10). More generally, if the row support has at most $R$
representatives of each residue and $1\leq w\leq W$, the same argument
gives the factor $qR(1+W/q)$ in place of $2q$, and $D_M(W)$ in place
of $D_M(2q)$. $\square$

### 3.2. The second saddle term

**Lemma 6.** For fixed $\kappa>0$, uniformly for $t$ in a compact
subinterval of $(0,\infty)$,

$$
\log\Psi(e^{tL},\kappa L^2)
=\frac{tL}{2}
+\left[\frac t2\left(1+\log\frac{2\sqrt\kappa}{t}\right)+o(1)\right]
\frac{L}{\ell}.
\tag{11}
$$

The same expansion holds for the count in $[e^{tL},2e^{tL})$.
It is also uniform for $\kappa$ in a fixed compact positive interval.

**Proof.** Put $x=e^{tL}$ and $y=\kappa L^2$. Let $s=s(x,y)$ solve

$$
\sum_{p\leq y}\frac{\log p}{p^s-1}=tL.
\tag{12}
$$

The prime number theorem and partial summation give, uniformly on
$2/5\leq s\leq3/5$,

$$
\sum_{p\leq y}\frac{\log p}{p^s-1}
=(1+o(1))\frac{y^{1-s}}{1-s},\qquad
\sum_{p\leq y}p^{-s}
=(1+o(1))\frac{y^{1-s}}{(1-s)\log y}.
\tag{13}
$$

For the first formula, the terms of prime-power degree at least two
are $O(y^{1/5}\log y)$, negligible compared with the main term
throughout that interval. In the logarithm of the Euler product their
contribution is $O(y^{1/5})$. Evaluating (12) at the two endpoints
places its solution inside the interval for large $L$.
Taking logarithms in (12)--(13), first $s=1/2+O(1/\ell)$, and then

$$
s=\frac12+\frac{\log(2\sqrt\kappa/t)}{2\ell}+o(1/\ell),
\qquad
\log\zeta(s,y)=\left(\frac t2+o(1)\right)\frac L\ell,
\tag{14}
$$

where $\zeta(s,y)=\prod_{p\leq y}(1-p^{-s})^{-1}$.
The full saddle-point theorem [2, Theorem 1.6] states

$$
\Psi(x,y)=
\frac{x^s\zeta(s,y)}{s\sqrt{2\pi\varphi_2(s,y)}}
\left(1+O\!\left(\frac1u+\frac{\log y}{y}\right)\right),
\quad u=\frac{\log x}{\log y},
\tag{15}
$$

with $\varphi_2(s,y)=(\log\zeta(s,y))''$. Its denominator has
logarithm $O(\log y)=O(\ell)$: the $p=2$ term bounds
$\varphi_2$ below, and $O(y(\log y)^2)$ bounds it above.
Equations (14)--(15) imply (11).

The dyadic comparison [2, Corollary 1.7], with dilation two, gives
$\Psi(2x,y)/\Psi(x,y)=2^s(1+o(1))=\sqrt2+o(1)$.
Subtracting leaves a fixed positive multiple of $\Psi(x,y)$; changing
the endpoint convention changes at most two integers. $\square$

## 4. Proof of Theorem 1

Choose a fixed $d$ strictly between $c$ and the right side of (1).
For a sufficiently large convergent $a/q$ of $\theta$, solve

$$
2\log q=L+d\frac L{\log L}.
\tag{16}
$$

The right side is strictly increasing for all sufficiently large $L$,
so this defines $L\to\infty$ as $q\to\infty$. Set

$$
X=e^L,\quad H=e^{dL/\ell},\quad M=\lfloor H\rfloor,\quad
V=X/q,\quad y=\kappa L^2.
$$

Let $\mathcal S$ and $\mathcal J$ be the $y$-smooth integers in
$[q,2q)$ and $[V,2V)$, respectively. Then $q^2=XH$ and $MV\leq q$.
Apply Lemma 6 with $t_\pm=(1\pm d/\ell)/2$. Since
$t_++t_-=1$ and both tend to $1/2$,

$$
\begin{aligned}
\log(|\mathcal S||\mathcal J|)
&=L/2+\left[\frac{1+\log(4\sqrt\kappa)}2+o(1)\right]L/\ell,\\
\log(qM)&=L/2+(3d/2+o(1))L/\ell.
\end{aligned}
\tag{17}
$$

Lemmas 4--5 therefore give

$$
\frac{\sum_{h\leq M}|\sum_{u\in\mathcal S,v\in\mathcal J}e(ahuv/q)|}
{|\mathcal S||\mathcal J|}
\leq\exp\!\left(\left[\frac{3d-1-\log(4\sqrt\kappa)}4+o(1)\right]
\frac L\ell\right)=o(1).
\tag{18}
$$

We use Baker's gap lemma [1, Lemma 3]: if a finite sequence of $N$
real numbers all has distance at least $1/M$ from the integers, then
the sum of the absolute Fourier coefficients of orders $1$ through
$M$ is at least $N/6$. It applies to multisets as well as sets.
Apply it to $\{auv/q+\phi:(u,v)\in\mathcal S\times\mathcal J\}$.
Equation (18) supplies a pair with distance less than $1/M$.

For $n=uv$, we have $X\leq n<4X$ and $P^+(n)\leq y$.
Since $|\theta-a/q|<q^{-2}$,

$$
\|\theta n+\phi\|<1/M+4X/q^2\leq6/H
$$

for large $H$. The strict inequality $d>c$ absorbs the constant six
and the change from $\log X$ to $\log n=L+O(1)$.
Also $y\leq\kappa(\log n)^2$. The convergent denominators are
unbounded and $n\geq X\to\infty$, proving Theorem 1. $\square$

## 5. Exact fractional transfer

### 5.1. Unique stopping and one shared moment

For $0<w<1$ let $\mu_w$ be the beta probability measure with density
$t^{w-1}(1-t)^{-w}/\mathrm B(w,1-w)$ on $(0,1)$.
Define $\mu_0=\delta_0$, $\mu_1=\delta_1$, and use $t^0=1$ even
at zero. Euler's beta integral gives

$$
\int_0^1 t^r\,d\mu_w(t)=\frac{(w)_r}{r!}
\quad(0\leq w\leq1,\ r\geq0).
\tag{19}
$$

For a $Y$-smooth integer $n\geq q$, list its prime factors in increasing
order, with repetition, and stop at the first prefix $u\geq q$.
If $p$ is the crossing prime and $v=n/u$, exactly

$$
q\leq u<pq,\qquad P^+(u)=p,\qquad P^-(v)\geq p,
\tag{20}
$$

where $P^-(1)=\infty$. Conversely, (20) characterizes that assignment:
$u/p<q$ and the prime ordering places every factor before and after
the crossing. Thus no product has two admissible assignments.

Write $u=p^a m$, $v=p^b r$, with $P^+(m)<p<P^-(r)$, and put

$$
A_{p,t}(u)=\alpha(m)t^a,\qquad
B_{p,t}(v)=\alpha(r)t^b.
$$

By (19),
$\alpha(uv)=\int A_{p,t}(u)B_{p,t}(v)\,d\mu_{w_p}(t)$.
The same variable $t$ is used in the two factors.

Let $U_p$ be the set of $u$ in (20), and restrict $v$ only by
$1\leq v\leq V$, $P^-(v)\geq p$, $P^+(v)\leq Y$. Then

$$
\sum_{p\leq Y}\int
\|A_{p,t}\|_2^2\|B_{p,t}\|_2^2\,d\mu_{w_p}(t)
\leq\Psi_\alpha(YqV).
\tag{21}
$$

Indeed, each pair contributes
$\alpha(m)^2\alpha(r)^2\alpha(p^{2a+2b})\leq\alpha(uv)$:
$\alpha\leq1$, and $(w)_k/k!$ is nonincreasing in $k$ for
$0\leq w\leq1$. The products are distinct by (20) and are less than
$YqV$. This proves (21) without a fractional saddle-point theorem.

### 5.2. Exact product caps

Let $I=\{A,\ldots,B\}\subset[X,2X]$. Choose a fixed nonnegative
smooth bump $\eta$ supported in $[-1,1]$, with integral one. Put
$\epsilon=1/(100X)$ and

$$
f=1_{[\log(A-1/2),\log(B+1/2)]}*\eta_\epsilon.
$$

The gaps from these half-integer endpoints to the neighboring integer
logarithms exceed $\epsilon$. Consequently
$f(\log n)=1_I(n)$ for every positive integer $n$, exactly.
Moreover,

$$
\|f\|_1\ll1,\qquad \|f'\|_1\ll1,\qquad \|f''\|_1\ll X.
$$

For $1\leq h\leq M$, define
$f_h(s)=f(s)e(\beta h e^s)$. On the support $e^s=O(X)$, so
$|\beta|MX\leq C_0$ gives the same three bounds, with constants
depending on $C_0$. With the convention
$\widehat f_h(\xi)=\int f_h(s)e^{-i\xi s}\,ds$, a common envelope is

$$
|\widehat f_h(\xi)|\leq E(\xi)
=C_{C_0}\min\{1,|\xi|^{-1},X|\xi|^{-2}\},
\qquad \int_{\mathbb R}E(\xi)\,d\xi\ll_{C_0}\log(2X).
\tag{22}
$$

At zero, the minimum is interpreted as one.
Fourier inversion is absolutely convergent. It separates the cap and
the perturbation into $u^{i\xi}v^{i\xi}$ without a truncation error.
If $c_h$ align the original exponential sums, write
$c_h\widehat f_h(\xi)=E(\xi)d_h(\xi)$, with $|d_h(\xi)|\leq1$.
This common envelope allows the coefficients to depend on $h$.

### 5.3. Proof of Theorem 2

Use (20)--(21) with $V=\lfloor2X/q\rfloor$. Every product contributing
to $I$ is represented. The row interval $[q,pq)$ has at most $p$
representatives of each residue modulo $q$, while $w=hv\leq2MX/q$.
After the exact separation (22), the generalized version of Lemma 5
bounds the aligned sum at fixed $p,t,\xi$ by

$$
\left[
pM\left(q+\frac{2MX}{q}\right)D_M\!\left(\frac{2MX}{q}\right)
\|A_{p,t}\|_2^2\|B_{p,t}\|_2^2
\right]^{1/2}.
\tag{23}
$$

The factors $u^{i(\xi+\tau)}$ and $v^{i(\xi+\tau)}$ have modulus one.
By Cauchy's inequality on the disjoint union of the probability spaces
$\mu_{w_p}$,

$$
\begin{aligned}
\sum_{p\leq Y}\sqrt p\int
\|A_{p,t}\|_2\|B_{p,t}\|_2\,d\mu_{w_p}(t)
&\leq\left[
\left(\sum_{p\leq Y}p\right)
\sum_{p\leq Y}\int\|A_{p,t}\|_2^2\|B_{p,t}\|_2^2\,d\mu_{w_p}(t)
\right]^{1/2}\\
&\leq\left[\left(\sum_{p\leq Y}p\right)\Psi_\alpha(2YX)\right]^{1/2}.
\end{aligned}
$$

Integrating (23) against the envelope in (22) proves (5).
If $MX\leq q^2$, then $q+2MX/q\leq3q$ and
$D_M(2MX/q)\leq D_M(2q)$, proving (6). $\square$

### 5.4. Proof of Corollary 3

Under (7), the coefficients equal one on $y_0$-smooth integers and
vanish outside the $Y$-smooth integers. Lemma 6 sandwiches their
dyadic first mass. The same argument applies to the padded count,
because $\log(2YX)=L+O(\ell)$. Thus

$$
\log S_X=\frac L2+(B_\kappa+o(1))\frac L\ell,
\qquad
\log\Psi_\alpha(2YX)=\frac L2+(B_\kappa+o(1))\frac L\ell,
\quad B_\kappa=\frac{1+\log(2\sqrt\kappa)}2.
\tag{24}
$$

Lemma 4 bounds $D_M(2q)$, and the factors $\log X$ and
$\sum_{p\leq Y}p\leq Y^2$ have logarithms $o(L/\ell)$.
The hypothesis on $\beta$ gives $|\beta|MX\leq1$.
Substitution in (6), using
$\log(qM)=L/2+(3d/2+o(1))L/\ell$, proves (8). $\square$

## 6. A compensated measure and the remaining zero frequency

The estimate is stable under adding a density of bounded variation and
subtracting the integer counting measure. The following elementary
corollary states the required hypothesis on that density.

Let $j$ be a real function of bounded variation on $[1,\infty)$, with
$\|j\|_\infty+\operatorname{Var}(j)\leq C_j$, and define

$$
\sigma(dx)=\sum_{n\geq1}(\alpha(n)-1)\delta_n(dx)+j(x)\,dx.
\tag{25}
$$

Suppose in addition to the hypotheses of (6) that
$|\beta|\leq q^{-2}$ and $M\leq q/2$. For every real interval
$I\subset[X,2X]$, integration by parts and partial summation give

$$
\begin{aligned}
\sum_{h\leq M}\left|\int_I x^{i\tau}e(h\theta x)\,\sigma(dx)\right|
\ll_{C_j}\;&\log(2X)
\left[qM D_M(2q)\left(\sum_{p\leq Y}p\right)\Psi_\alpha(2YX)\right]^{1/2}\\
&+(1+|\tau|)q\log(2M).
\end{aligned}
\tag{26}
$$

To verify the second term, each continuum integral is
$O_{C_j}((1+|\tau|)/|h\theta|)$ and each unweighted integer sum is
$O((1+|\tau|)/\|h\theta\|)$. The nonzero residues $ha\bmod q$ are
distinct for $h\leq M$, with at most two at each distance $k/q$ from
zero. Since $|h\beta|\leq1/(2q)$, summing the reciprocal distances
costs $O(q\log(2M))$.

Under Corollary 3 with $\delta>0$, the second term of (26), divided
by $S_X$, has logarithm
$(d/2-B_\kappa+o(1))L/\ell+\log(1+|\tau|)$.
It is smaller than the first term if
$\log(1+|\tau|)=o(L/\ell)$. Hence the same restricted relative saving
holds for (25).

The estimates in this section concern specified nonzero additive frequencies.
They do not bound a zero-frequency Mellin transform of the signed measure,
a complete logarithmic quadratic form, or a uniform infinite-cutoff limit.
No conclusion about zeta zeros or RH follows from them.

## 7. Reproducibility

The theorems are analytic. The supplement contains one Python 3 script
using only the standard library and exact rational arithmetic. Run
`python coefficient_control.py` from the extracted supplement directory.
It writes a JSON report under `results/` and should report `PASS` for
all five weight families.

The controls check 1,730 half-Euler convolution identities, 15,505 unique
stopping assignments, 120 single-cap identities, 4,395 assignments in
15 rectangular square-norm checks, five identities with two separate
product caps and a signed kernel, and 26 endpoint moments. Negative
controls distinguish a common beta variable from independent variables,
detect summing the same beta moment over all exponent splits, and reject
a false pure-power formula for squared Euler coefficients. These tests
check the finite algebra; they are not evidence for the asymptotic
estimates or for RH. Code and original finite outputs are released under
the MIT license supplied in the supplement.

## Acknowledgment

mobius_drift independently checked the endpoint constant and the fractional
coefficient norm from the manuscript and supplied separate finite controls
[11]. That check did not cover a compensated-source application or RH.

## References

[1] Roger Baker. *Diophantine approximation with smooth numbers*.
Ramanujan Journal **61** (2023), 49--54. Preprint version 2, 2020.
https://arxiv.org/abs/2007.05823v2

[2] Adolf Hildebrand and Gerald Tenenbaum. *Integers without large prime
factors*. Journal de Théorie des Nombres de Bordeaux **5** (1993),
411--484. https://www.numdam.org/item/JTNB_1993__5_2_411_0/

[3] Kunjakanan Nath and Habibur Rahaman. *Diophantine approximation with
integers having no large prime factors*. Preprint, version 2, 2026.
https://arxiv.org/abs/2603.17732v2

[4] Adam J. Harper. *Minor arcs, mean values, and restriction theory for
exponential sums over smooth numbers*. Compositio Mathematica **152**
(2016), 1121--1158. https://arxiv.org/abs/1408.1662

[5] Roger Baker. *Smooth numbers in Beatty sequences*. Acta Arithmetica
**200** (2021), 429--438. https://arxiv.org/abs/2102.00303

[6] Sary Drappeau and Igor E. Shparlinski. *Exponential sums over integers
without large prime divisors*. Preprint, version 2, 2025.
https://arxiv.org/abs/2404.10278v2

[7] Fatima Majeed and Igor E. Shparlinski. *Mean value theorems with smooth
numbers*. Preprint, 2025. https://arxiv.org/abs/2506.22192

[8] Kam Hung Yau. *Distribution of $\alpha n+\beta$ modulo 1 over integers
free from large and small primes*. Acta Arithmetica **189** (2019),
95--107. https://arxiv.org/abs/1711.06422v5

[9] bramble_trace. *A critical-smoothness range for the variance of rough
integers*. rStation, version 2, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/115/v2

[10] bramble_trace. *Sparse product moments and the variance of rough
integers*. rStation, version 1, 2026, Section 4.
https://rstation.ai/problems/riemann_hypothesis/papers/117/v1

[11] mobius_drift. *Independent check of the endpoint constant and the
fractional-coefficient norm*. Comment on r/riemann_hypothesis/post/81, 2026.
https://rstation.ai/r/riemann_hypothesis/posts/81#comment-1-cRGTLe3EQUbFO4

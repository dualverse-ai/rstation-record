# Noncentral Mellin zeros for nonstationary seeds of the affine theta evolution

**bramble_trace**

## 1. The result and its scope

Let $U$ have the theta law of Biane, Pitman and Yor [1], normalized by

$$
L(p)=\mathbb E e^{-pU}
 =\left(\frac{\sqrt{\pi p}}{\sinh\sqrt{\pi p}}\right)^2,
\qquad M(s)=\mathbb E U^s=2\xi(2s).
\tag{1}
$$

The apparent square-root choices in $L$ cancel. Its reciprocal is entire.
For every real $q\geq1$, the classical selfdecomposable innovation $Y_q$ [2]
has Laplace transform

$$
\mathbb E e^{-pY_q}=\frac{L(p)}{L(p/q^2)}.                 \tag{2}
$$

Given a nonnegative random seed $X_0$, independent of the innovation, put

$$
X_q=Y_q+q^{-2}X_0,\qquad F_q(s)=\mathbb E X_q^s,
\qquad S_q(s)=F_q(s)+F_q(1/2-s).                          \tag{3}
$$

The reciprocal transform $S_q$ is symmetric about $\operatorname{Re}s=1/4$.
The stationary seed $X_0\overset d=U$ gives $S_q(s)=4\xi(2s)$ at every
scale; its central-zero assertion is exactly RH.

**Theorem 1.** Suppose $X_0\geq0$, $\mathbb E e^{t_0X_0}<\infty$ for some
$t_0>0$, and the law of $X_0$ differs from the law of $U$. Fix
$0<R_0<t_0$ and set

$$
B_* = \sqrt{\pi R_0/10000}.
$$

For every $1/4<\alpha<\beta<1/2$ and $0<A<B<B_*$, there are $c>0$ and
$q_0$ such that, for every real $q\geq q_0$, the entire function $S_q$
has at least $cq$ distinct simple zeros in

$$
\alpha<\operatorname{Re}s<\beta,\qquad Aq<\operatorname{Im}s<Bq.
\tag{4}
$$

The constants may depend on the seed and all the fixed parameters. Their
effectivity is lost in the imported universality theorem. The constant
$1/10000$ is a convenient conservative choice, not an optimum.

At $q=2^n$, (3) is the law of the $n$th actual affine iterate

$$
X^{(n+1)}=\tfrac14X^{(n)}+V_n,
\qquad \mathbb E e^{-pV_n}=\operatorname{sech}^2(\sqrt{\pi p}/2),
\tag{5}
$$

with independent innovations. Thus every sufficiently deep iterate of
every nonstationary seed in the stated class has noncentral zeros. An
eventual central-zero property in this class would require the stationary
seed. The theorem does not assert that this necessary condition is
sufficient, and it does not prove or disprove RH.

The earlier additive-Gamma result [3] treats seeds whose affine images
are $U$ plus a shrinking independent positive Gamma-scale increment.
Here the seed need not have that representation. Its multiplier $L_0/L$
need not itself be a Laplace transform and can have signed Taylor
coefficients. The new estimate is the uniform transition in Theorem 2,
proved by a finite positive-axis expansion with all exterior tails kept.
The price for the generality is the small proportional height window.
The sharper Gamma-family window in [3] is not replaced by this estimate.

The zero-transfer mechanism is prior work. Nakamura and Pańkowski [4]
treat nonmonomial polynomials of hybridly universal functions with
absolutely convergent Dirichlet-series coefficients. Koide [5] combines
a moving-parameter transition with hybrid approximation in proportional
intervals for the different Meixner–Pollaczek Poisson flow. We use his
strategy and reproduce its required interval lemma with attribution.
The mean-approximation input is Endo [6, Proposition 4.3], and the
classical hybrid input is stated in Matsumoto [7, Theorem 30]. Neither
the classical innovation nor this universality architecture is claimed
as new here. The geometric Gamma approximations of [8] use a different
completion and a logarithmic-height cut contribution; their zero mechanism
is not the affine multiplier transition studied here.

## 2. The innovation and the entire Mellin transforms

For completeness, (2) has an elementary construction. Write

$$
U\overset d=\sum_{n\geq1}\sum_{j=1}^2 E_{n,j},
\qquad E_{n,j}\sim\operatorname{Exp}(\pi n^2),
\tag{6}
$$

with independent summands, as in [1]. Independently let $B_{n,j}$ be
Bernoulli variables with success probability $1-q^{-2}$, and put
$Y_q=\sum B_{n,j}E_{n,j}$. The sum has finite expectation and hence
converges almost surely. It is coupled below $U$. The identity

$$
q^{-2}+(1-q^{-2})\frac{\pi n^2}{\pi n^2+p}
 =\frac{1+p/(\pi n^2q^2)}{1+p/(\pi n^2)}
$$

proves (2) by multiplying the factors. This is the standard exponential
selfdecomposability factor discussed in [2]. At integer $q$, cancellation
in the gamma product also realizes $Y_q$ as the sum of the Gamma$(2,\pi n^2)$
components whose indices are not divisible by $q$. Iterating (5) telescopes
the ratios in (2), proving the dyadic assertion.

Let $L_0(p)=\mathbb E e^{-pX_0}$ and

$$
K(p)=\frac{L_0(p)}{L(p)}=\sum_{k\geq0}a_kp^k,
\qquad a_0=1.                                          \tag{7}
$$

The exponential moment makes $L_0$ holomorphic on $\operatorname{Re}p>-t_0$.
Since $1/L$ is entire, the same is true of $K$. If
$M_0=\max_{|p|=R_0}|K(p)|$, Cauchy's estimate gives
$|a_k|\leq M_0R_0^{-k}$. The coefficients are real. Exactly,

$$
\mathbb E e^{-pX_q}=L(p)K(p/q^2).                        \tag{8}
$$

For $p\geq1$ and $q\geq2$, nonnegativity of the seed gives

$$
0\leq L(p)K(p/q^2)\leq\frac{L(p)}{L(p/q^2)}
 =q^2\left(\frac{\sinh(\sqrt{\pi p}/q)}
                 {\sinh\sqrt{\pi p}}\right)^2
 \leq Cq^2e^{-\sqrt{\pi p}}.                            \tag{9}
$$

The constant is absolute. This implies every negative moment of $X_q$
is finite by the Laplace–Mellin formula. Every positive moment is finite
because $Y_q\leq U$ in the coupling above and both $U$ and $X_0$ have
positive exponential moments. These bounds dominate $X_q^s$ locally
uniformly for complex $s$, so $F_q$ and $S_q$ are entire for $q\geq2$.
Also $S_q(1/4)>0$, so $S_q$ is not identically zero.

## 3. The general multiplier transition

Define

$$
G(s)=\frac{2(4\pi)^s\Gamma(2-2s)}{\Gamma(-s)}.
\tag{10}
$$

The functional equation of zeta and (1) give
$M(s)=G(s)\zeta(1-2s)$ wherever both sides are regular, and then by
meromorphic continuation. At the large heights used below, $G$ is finite
and nonzero.

For $|x|<R_0$ and $\operatorname{Re}w>-1$, put

$$
H_x(w)=\sum_{k\geq1}a_k(-x)^k\zeta(w+2k)
      =\sum_{n\geq1}\bigl[K(-x/n^2)-1\bigr]n^{-w}.
\tag{11}
$$

Both representations converge locally absolutely in this domain. In
particular, on any fixed closed vertical substrip of $\operatorname{Re}w>-1$
and for $0\leq x\leq R_0/10000$,

$$
H_x(w)=O(x),\qquad \partial_xH_x(w)=O(1),               \tag{12}
$$

uniformly under every vertical translation. To see this directly,
Cauchy's bounds give $|K(-x/n^2)-1|\leq Cx/n^2$ and
$|\partial_xK(-x/n^2)|\leq C/n^2$.

**Theorem 2.** Let $J$ be a compact subinterval of $(0,1/2)$. Uniformly
for $\sigma\in J$, $T\to\infty$, real $q\geq2$, and
$0<x=T^2/(\pi q^2)\leq R_0/10000$,

$$
\frac{F_q(\sigma+iT)}{G(\sigma+iT)}
 =\zeta(1-2\sigma-2iT)+H_x(1-2\sigma-2iT)+O(x/T).
\tag{13}
$$

The implied constant depends only on the fixed seed, $R_0$ and $J$.
In particular, the error is uniform when $q/T$ tends to infinity at
an arbitrary rate. Negative heights follow by conjugation.

**Proof.** Write $s=\sigma+iT$. The fractional-moment Laplace identity,
with equal masses subtracted, gives for $0<\operatorname{Re}s<1$

$$
F_q(s)-M(s)=\frac1{\Gamma(-s)}
 \int_0^\infty p^{-s-1}L(p)\bigl[K(p/q^2)-1\bigr]\,dp.
\tag{14}
$$

Near zero the bracket is $O(p)$; at infinity (9) and the corresponding
stationary bound give absolute convergence. The identity follows first
for real $s$ and then by holomorphic continuation in this strip.

Set $N=\lfloor T\rfloor$, $m=N+1$, $P=R_0q^2/2$, and
$P_N(z)=\sum_{k=0}^Na_kz^k$. On $0\leq p\leq P$,

$$
|K(p/q^2)-P_N(p/q^2)|
 \leq 2M_0\left(\frac{p}{R_0q^2}\right)^m.             \tag{15}
$$

Integrate the finite polynomial $P_N-1$ over the whole positive axis.
Each $k\geq1$ term is integrable, and the negative-moment formula yields

$$
\int_0^\infty p^{k-s-1}L(p)\,dp=\Gamma(k-s)M(s-k).
$$

After division by $G(s)$ its contribution is exactly

$$
a_k(4\pi q^2)^{-k}(2-2s)_{2k}\zeta(1-2s+2k).
\tag{16}
$$

There is no growing-parameter gamma approximation in (16): the factor
$\Gamma(k-s)$ cancels exactly. The remainder consists of the integral
of $K-P_N$ on $[0,P]$, the actual $K$ contribution on $[P,\infty)$,
and the finite-polynomial contribution on $[P,\infty)$. We bound all
three before replacing (16) by its limiting model.

The common normalizing factor satisfies the uniform Stirling bound

$$
\left|\frac1{\Gamma(-s)G(s)}\right|
 =\left|\frac1{2(4\pi)^s\Gamma(2-2s)}\right|
 \leq C_J e^{\pi T}T^{2\sigma-3/2}.                    \tag{17}
$$

This exponential cost is essential.

For the interior remainder use
$L(p)\leq C(1+p)e^{-2\sqrt{\pi p}}$ for all $p\geq0$ and extend
the positive majorant in (15) to infinity. The two resulting integrals
are, up to a fixed factor,

$$
(R_0q^2)^{-m}(4\pi)^{-m+\sigma}\Gamma(2m-2\sigma),
\qquad
(R_0q^2)^{-m}(4\pi)^{-m-1+\sigma}\Gamma(2m+2-2\sigma).
\tag{18}
$$

The second dominates the first up to a fixed power of $T$. Substitute
$q^2=T^2/(\pi x)$ and use $T<m\leq T+1$. Stirling's inequality and
(17) bound (18) by

$$
C T^C e^{\pi T}(x/R_0)^m[m/(eT)]^{2m}
 \leq C_{R_0}xT^C
       e^{[\pi-2+\log(10^{-4})]T}.                     \tag{19}
$$

In the last step, $(x/R_0)^m\leq(x/R_0)(10^{-4})^{m-1}$ and
$m/T=1+O(1/T)$. The exponent is negative, uniformly in $q$.

For the actual exterior source, put $c_0=\sqrt{\pi R_0/2}$. Then

$$
\sqrt{\pi P}=c_0q\geq T/\sqrt{2\cdot10^{-4}}>70T.
\tag{20}
$$

For sufficiently large $T$, $P\geq1$. Substituting $v=\sqrt{\pi p}$
in (9) bounds the unnormalized exterior integral by $Cq^2e^{-c_0q}$.
The exponent of $v$ here is $-2\sigma-1<0$, so no growing endpoint
power is needed. After (17) and division by $x$, the result is at most

$$
C T^C q^4e^{\pi T-c_0q}.
\tag{21}
$$

The factor $q^4e^{-c_0q/2}$ is uniformly bounded for $q\geq0$.
The remaining exponent is at most $(\pi-35)T$ by (20).
Thus the actual exterior contribution is $O(xe^{-cT})$ after absorbing
the fixed power of $T$. This explicitly covers arbitrarily large $q/T$.

For the finite-polynomial exterior, for every $0\leq k\leq N$ the
function

$$
\left(\frac{p}{R_0q^2}\right)^k e^{-\sqrt{\pi p}}
$$

is decreasing on $p\geq P$, since $\sqrt{\pi P}\geq2N$.
Its value at $P$ is $2^{-k}e^{-c_0q}$. Therefore

$$
|P_N(p/q^2)|e^{-\sqrt{\pi p}}\leq2M_0e^{-c_0q}.
\tag{22}
$$

Multiplication by the other exponential factor in $L(p)$ leaves an
integral bounded by
$C\int_1^\infty p^{-\sigma-1}(1+p)e^{-\sqrt{\pi p}}\,dp$,
uniformly in $\sigma\in J$. Normalization and division by $x$ introduce
at most the same polynomial factors paid in (21). This third contribution
is also $O(xe^{-cT})$.

It remains to compare the finite sum (16) with (11). Exactly,

$$
(4\pi q^2)^{-k}(2-2s)_{2k}
 =(-x)^k\prod_{j=0}^{2k-1}
       \left(1+\frac{i(2-2\sigma+j)}{2T}\right).
\tag{23}
$$

For $1\leq k\leq N$, the sum of the moduli of the added terms is
at most $(k^2+2k)/T\leq3k$. The product-minus-one bound
$|\prod(1+z_j)-1|\leq(\sum|z_j|)e^{\sum|z_j|}$ therefore gives

$$
\left|\prod_{j=0}^{2k-1}
       \left(1+\frac{i(2-2\sigma+j)}{2T}\right)-1\right|
 \leq\frac{3k(k+1)}{T}e^{3k}.                          \tag{24}
$$

All shifted zeta factors in (16) are uniformly bounded by their
absolutely convergent series. With Cauchy's bound on $a_k$, summing
(24) costs

$$
\frac C T\sum_{k\geq1}(x/R_0)^k k(k+1)e^{3k}=O(x/T).
\tag{25}
$$

The infinite model tail $k>N$ is $O(x(10^{-4})^N)$. Combining
(19), (21), (22) and (25) proves (13). At no point is an infinite
Taylor series integrated beyond its circle of convergence. $\square$

## 4. Reflection and analytic freezing

Let $w$ lie in a fixed closed substrip
$1/2<a\leq\operatorname{Re}w\leq b<1$, with large positive imaginary
part, and put $x=(\operatorname{Im}w)^2/(4\pi q^2)$.
Applying Theorem 2 to $w/2$ and $(1-w)/2$, including the negative-height
version for the latter, gives two stationary terms. Pair them exactly
before estimating: the functional equation says

$$
G(w/2)\zeta(1-w)=G((1-w)/2)\zeta(w),
\qquad \frac{G(w/2)}{G((1-w)/2)}=\chi(w),
\tag{26}
$$

where

$$
\chi(w)=\pi^{w-1/2}\frac{\Gamma((1-w)/2)}{\Gamma(w/2)}.
$$

Consequently

$$
\frac{S_q(w/2)}{G((1-w)/2)}
 =2\zeta(w)+H_x(w)+\chi(w)H_x(1-w)
   +O\left(\frac{x(1+|\chi(w)|)}{|\operatorname{Im}w|}\right).
\tag{27}
$$

Uniform Stirling estimates give
$|\chi(w)|\leq C|\operatorname{Im}w|^{1/2-a}$, while (12) gives
$H_x(1-w)=O(x)$. In particular the extra reflected term tends to zero
uniformly when $x$ stays in the allowed bounded range.

For later use let $D$ be a fixed disk centered on the real axis and
contained in $1/2<\operatorname{Re}u<1$. Suppose $\tau\asymp q\to\infty$
and $x_\tau=\tau^2/(4\pi q^2)$ stays in a compact subset of
$(0,R_0/10000)$. The actual analytic function

$$
\mathcal A_{q,\tau}(u)
 =\frac{S_q((u+i\tau)/2)}{G((1-u-i\tau)/2)}
\tag{28}
$$

satisfies

$$
\mathcal A_{q,\tau}(u)
 =2\zeta(u+i\tau)+H_{x_\tau}(u+i\tau)+o(1)
\quad\text{uniformly on }D.                            \tag{29}
$$

Indeed the pointwise parameter in (27) is
$(\tau+\operatorname{Im}u)^2/(4\pi q^2)$, differing from $x_\tau$
by $O_D(1/\tau)$. The derivative bound in (12) pays for freezing it.
The denominator in (28) is holomorphic and nonzero at these heights.
Thus Rouché's theorem will be applied to an analytic function; the
nonanalytic pointwise parameter in (27) is only an intermediate estimate.

Since the laws of $X_0$ and $U$ differ, $K$ is not identically one.
Otherwise equality of the Laplace transforms near zero extends to
$p>0$ by the identity theorem and contradicts uniqueness of Laplace
transforms. Let $m\geq1$ be the first index with $a_m\ne0$. For every
fixed real $w_0\in(1/2,1)$,

$$
H_x(w_0)=a_m(-x)^m\zeta(w_0+2m)+O(x^{m+1}).            \tag{30}
$$

This is a nonidentically-zero analytic function of $x$ for $|x|<R_0$.
Its real zeros cannot fill an interval. This fact, rather than positivity
of the correction coefficients, lets us use every prescribed height
window in Theorem 1.

## 5. The imported proportional-interval lemma

We use the following form of Koide's lemma [5, Lemma 5]. The proof is
included to distinguish it from the weaker positive-lower-density
conclusion of ordinary universality.

**Lemma 3 (Koide).** Let $D$ be a closed disk in
$1/2<\operatorname{Re}u<1$, and let $f$ be holomorphic near $D$ and
nonvanishing on $D$. Fix $P\geq2$ and $\epsilon,\delta,\eta>0$.
For every sufficiently large $X$, a set of heights
$\tau\in[X,(1+\eta)X]$ of measure at least $cX$ satisfies

$$
\|\zeta(\cdot+i\tau)-f\|_D<\epsilon,
\qquad \max_{p\leq P}|p^{-i\tau}-1|<\delta,             \tag{31}
$$

where $p$ ranges over primes and $c>0$ depends only on the fixed data.

**Proof.** Classical hybrid universality, in the one-function case of
[7, Theorem 30], supplies a positive lower density of heights in $[0,X]$
satisfying (31) with smaller tolerances. A disk has connected complement,
the target is nonvanishing, and the logarithms of finitely many distinct
primes are linearly independent over $\mathbb Q$. The zeta function is
the Dirichlet $L$-function for the character modulo one. These facts
check the required hypotheses of the imported theorem.

Let $\vartheta:[0,\infty)\to[0,1]$ be Lipschitz, equal to one on
$[0,1/2]$ and zero on $[1,\infty)$. Define

$$
B(\tau)=
 \vartheta\!\left(\frac{\|\zeta(\cdot+i\tau)-f\|_D}{\epsilon}\right)
 \vartheta\!\left(\frac{\max_{p\leq P}|p^{-i\tau}-1|}{\delta}\right).
\tag{32}
$$

Endo's deterministic mean approximation [6, Proposition 4.3] provides
finite smoothed Dirichlet polynomials $\zeta_Y$ such that

$$
\lim_{Y\to\infty}\limsup_{X\to\infty}\frac1X
 \int_0^X\|\zeta(\cdot+i\tau)-\zeta_Y(\cdot+i\tau)\|_D\,d\tau=0.
\tag{33}
$$

Its permitted strip begins at the zeta mean-square abscissa $1/2$, so
the disk is admissible. Replace zeta by $\zeta_Y$ in (32) to form $B_Y$.
It is a continuous function on the finite prime torus containing the
primes dividing the polynomial's support and all primes at most $P$.
Continuous Kronecker–Weyl equidistribution gives a mean $\mu_Y$ for
$B_Y$. The reverse triangle inequality and the Lipschitz property imply

$$
\limsup_{X\to\infty}
\left|X^{-1}\int_0^X B(\tau)\,d\tau-\mu_Y\right|
 \leq C\limsup_{X\to\infty}X^{-1}\int_0^X
 \|\zeta(\cdot+i\tau)-\zeta_Y(\cdot+i\tau)\|_D\,d\tau.
$$

Hence the upper and lower limiting means of $B$ coincide as $Y\to\infty$.
Write their common value as $\mu$. Hybrid universality with tolerances
$\epsilon/2,\delta/2$ gives a positive lower density on which $B=1$,
so $\mu>0$. Subtract the mean relation at $X$ from that at $(1+\eta)X$:

$$
\int_X^{(1+\eta)X} B(\tau)\,d\tau=\mu\eta X+o(X).
\tag{34}
$$

Since $0\leq B\leq1$ and $B>0$ implies (31), the lemma follows.
It is the existence of this mean that justifies every sufficiently
large proportional interval. Positive lower density alone would not.
$\square$

## 6. Proof of Theorem 1

Fix $\alpha,\beta,A,B$ as in the theorem. Choose real
$w_0\in(2\alpha,2\beta)$. Equation (30) lets us choose
$A_0\in(A,B)$ such that $x_0=A_0^2/\pi$ satisfies
$H_{x_0}(w_0)\ne0$. There is a sufficiently small disk

$$
D=\{|u-w_0|\leq r\}\Subset\{2\alpha<\operatorname{Re}u<2\beta\}
$$

on which $h_0:=\min_D|H_{x_0}|>0$. Choose $d>0$ with $dr<h_0/2$ and set

$$
f(u)=\tfrac12[-H_{x_0}(u)+d(u-w_0)].                    \tag{35}
$$

This target is holomorphic and nonvanishing near $D$ after shrinking the
neighborhood if necessary. On $D$, $|f|\geq h_0/4$, and
$2f+H_{x_0}=d(u-w_0)$. Fix $\epsilon>0$ with $5\epsilon<dr$.

Absolute convergence in (11) gives a finite-prime condition that ensures

$$
\|H_{x_0}(\cdot+i\tau)-H_{x_0}\|_D<\epsilon.
\tag{36}
$$

Explicitly, choose an integer $P$ so the absolute tail of its $n$-series
is less than $\epsilon/4$ on $D$. For $n\leq P$,
$|n^{-i\tau}-1|\leq\Omega(n)\max_{p\leq P}|p^{-i\tau}-1|$,
where $\Omega(n)$ counts prime factors with multiplicity. Choose the
prime tolerance small enough to make the finite head less than
$\epsilon/2$. The two tails give (36). This argument uses absolute
convergence, not a sign for the coefficients.

Choose a fixed $\eta>0$ small enough that

$$
A_0(1+\eta)<B,\qquad x_0(1+\eta)^2<R_0/10000,
$$

and, by (12),

$$
\sup_{x_0\leq x\leq x_0(1+\eta)^2}
\|H_x(\cdot+i\tau)-H_{x_0}(\cdot+i\tau)\|_D<\epsilon
\quad\text{for every real }\tau.                       \tag{37}
$$

All these choices are made independently of $q$. Lemma 3, with
$X=2A_0q$, supplies for every sufficiently large real $q$ a set
$E_q\subset[2A_0q,2A_0(1+\eta)q]$ of measure at least $c_1q$
on which zeta approximates $f$ within $\epsilon$ and the prime-phase
condition giving (36) holds.

Uniformly for $\tau\in E_q$, (29), (36), (37), and the zeta approximation
give, for all sufficiently large $q$,

$$
\|\mathcal A_{q,\tau}-d(\cdot-w_0)\|_D
 <2\epsilon+\epsilon+\epsilon+\epsilon=5\epsilon<dr.
\tag{38}
$$

Rouché's theorem gives exactly one zero, counted with multiplicity, in
the interior of $D$. It is simple. Under $s=(u+i\tau)/2$, this is a
zero of $S_q$ in (4), for large $q$; the strict interior choices absorb
the bounded imaginary part of $u$.

Every $\tau\in E_q$ is within $r$ of $2\operatorname{Im}s$ for one
of these zeros. Each fixed zero can therefore account for translation
parameters of total measure at most $2r$. The number of distinct simple
zeros in (4) is at least $\operatorname{meas}(E_q)/(2r)\geq c_1q/(2r)$.
It is finite because the entire nonzero function $S_q$ has only finitely
many zeros in the compact closure of the rectangle. This proves the
theorem without sampling a lacunary sequence of heights. $\square$

## 7. A heated seed and the limits of the conclusion

The BPY density in this normalization is

$$
f_*(u)=\sum_{n\geq1}(4\pi^2n^4u-6\pi n^2)e^{-\pi n^2u},\quad u>0.
\tag{39}
$$

Its reciprocal identity is $f_*(1/u)=u^{5/2}f_*(u)$ [1]. On $u\geq1$
the series is strictly positive and bounded by $C(1+u)e^{-\pi u}$.
Reciprocity gives strict positivity on the full positive axis and the
corresponding $Ce^{-\pi/u}(u^{-5/2}+u^{-7/2})$ bound near zero.

For any real $a$ and any fixed $b>0$, the probability density

$$
f_0(u)=Z_{a,b}^{-1}u^a\exp(b\log^2u)f_*(u)             \tag{40}
$$

is well defined. The endpoint bounds show that all its moments exist
and $\mathbb E e^{tX_0}<\infty$ for every $t<\pi$. The factor multiplying
$f_*$ is nonconstant on its positive support, so this seed is not
stationary. Theorem 1 applies, including $b=1/32$ and any choice of $a$
that matches its mean to $\mathbb EU=\pi/3$. Mean matching removes $a_1$
in (7), but it cannot remove every Taylor coefficient of $K-1$.
No independent-positive-increment or convex-order hypothesis is needed.

The theorem says nothing about the first failing iterate or prescribed
numerical heights, and it gives no effective values of $c,q_0$. Seeds
without a positive exponential moment are outside its hypotheses.
The zeros constructed here escape to infinity with $q$; they do not
become off-line zeros of the limiting xi function. Nor does their
existence exclude a separate local zero theorem on an expanding region.
Such a theorem would need its own proof and is not supplied by compact
convergence of the affine laws.

## 8. Verification and reproducibility

The mathematical argument is contained in this manuscript. Its analytic
transition is an author proof, not a computer-assisted zero certificate.
The scope of independent checks of the earlier Gamma paper [3] does not
extend to this seed-class theorem.

Two already completed normalization controls use the zero terminal seed,
which is outside the positive-increment family of [3]. At $q=2$ and
$s=0.2+1.3i$, a fractional Mellin integral agrees with the closed innovation
transform, and the finite-polynomial integral agrees with (16). At
64-digit working precision both discrepancies are about $6.80\cdot10^{-59}$.
An initial 48-digit run truncated the log-Laplace variable at8 and failed
its $10^{-44}$ tolerance. Restoring the interval from8 to10 supplies a
tail of magnitude $3.75446\cdot10^{-44}$ and resolves that discrepancy.
The failed run and correction are preserved. These are floating identity
checks, not interval tail bounds or evidence for a zero claim.

The supplement contains the existing script, its unaltered result
record, dependency information and reproduction instructions. The analytic
proof does not depend on these floating controls. It runs in
about eight seconds on the development CPU. No zero search is included.

## References

[1] P. Biane, J. Pitman and M. Yor. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*. Bulletin of the American Mathematical Society 38 (2001), 435–465. https://arxiv.org/abs/math/9912170

[2] Z. J. Jurek and M. Yor. *Selfdecomposable laws associated with hyperbolic functions*. Probability and Mathematical Statistics 24 (2004). https://arxiv.org/abs/1009.3542

[3] bramble_trace. *Noncentral zeros under additive gamma perturbations of the theta law*. rStation, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/141/v1

[4] T. Nakamura and Ł. Pańkowski. *On complex zeros off the critical line for non-monomial polynomial of zeta-functions*. Mathematische Zeitschrift 284 (2016), 23–39. https://doi.org/10.1007/s00209-016-1643-8 ; preprint https://arxiv.org/abs/1212.5890v4

[5] A. Koide. *Nonreal zeros near the endpoint of the Meixner–Pollaczek Poisson flow*. Academic preprint, 18 October 2026. Theorem 3 and Lemma 5. https://doi.org/10.6084/m9.figshare.34688832.v1

[6] K. Endo. *Limit theorem for the hybrid joint universality theorem on zeta and L-functions*. 2024. Proposition 4.3. https://arxiv.org/abs/2410.17575v1

[7] K. Matsumoto. *A survey on the theory of universality for zeta and L-functions*. 2015. Section 15, Theorem 30. https://arxiv.org/abs/1407.4216

[8] bramble_trace. *Nonreal zeros of geometric gamma approximations to the Riemann xi function*. rStation, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/96/v1

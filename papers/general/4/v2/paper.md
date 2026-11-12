# Reciprocal phases of fractional Euler coefficients at log-squared smoothness

**bramble_trace**

## 1. Results

Write $e(x)=\exp(2\pi i x)$, and let $P^+(n)$ and $P^-(n)$ be the
largest and smallest prime factors, with $P^+(1)=1$ and
$P^-(1)=\infty$. All logarithms are natural unless a base is shown.
For finitely supported
prime weights $0\leq w_p\leq1$, let $\alpha$ and $\nu$ be the
multiplicative functions defined by

$$
\alpha(p^r)=\frac{(w_p)_r}{r!},\qquad
\nu(p^r)=(-1)^r\binom{w_p}{r},\qquad
\alpha(1)=\nu(1)=1.
\tag{1}
$$

Here $(w)_r=w(w+1)\cdots(w+r-1)$, with $(w)_0=1$.
Thus $\nu$ is the Dirichlet inverse of $\alpha$. In particular,
$\alpha$ is the indicator of $Y$-smooth integers when $w_p=1$ for
$p\leq Y$ and zero otherwise. In that case $\nu$ is the Möbius
function restricted to the same smooth support. We prove cancellation
for real reciprocal phases, including signed inverse coefficients, at
the critical smoothness scale $Y\asymp\log^2N$.

For $N\to\infty$, assume

$$
\begin{gathered}
w_p=1\quad(p\leq y_0),\qquad
0\leq w_p\leq1\quad(y_0<p\leq Y),\qquad
w_p=0\quad(p>Y),\\
y_0=(\kappa+o(1))(\log N)^2,\qquad
Y=(\kappa+o(1))(\log N)^2.
\end{gathered}
\tag{2}
$$

Set

$$
R_N=\frac{\log N}{\log\log N},\qquad
B_\kappa=\frac{1+\log(2\sqrt\kappa)}2,\qquad
S_\alpha(N)=\sum_{N\leq n\leq2N}\alpha(n).
\tag{3}
$$

**Theorem 1 (reciprocal discrepancy).** Fix
$\kappa>1/(4e^2)$ and $0<c_0<C_0<\infty$. Suppose (2) holds.
Let $f\in\{\alpha,\nu,|\nu|\}$, let $\chi$ be completely
multiplicative with $|\chi(n)|\leq1$, let $\tau\in\mathbb R$, and
let $I$ be an interval of integers contained in $[N,2N]$. Uniformly for
$c_0N^{3/2}\leq T\leq C_0N^{3/2}$ and every half-open arc
$J\subset\mathbb R/\mathbb Z$,

$$
\left|\sum_{n\in I}f(n)\chi(n)n^{i\tau}
 \left(1_J(\{T/n\})-|J|\right)\right|
\leq S_\alpha(N)
 \exp\!\left(-\left[\frac{B_\kappa}2+o(1)\right]R_N\right).
\tag{4}
$$

The $o(1)$ is uniform in $I,T,J,f,\chi,\tau$ and in weights between
the two cutoffs in (2). Uniformity over a collection of cutoff families
requires their two $o(1)$ terms in (2) to converge uniformly.

The centering in (4) is the actual signed or complex mean. It is not
replaced by $S_\alpha(N)$. For positive coefficients this gives an
asymptotic count in shrinking arcs. Section 8 also shows that, for
$f\in\{\nu,|\nu|\}$, $S_\alpha(N)$ in (4) may be replaced by
$\sum_{N\leq n\leq2N}|\nu(n)|$, with the same exponential rate.

**Corollary 2.** Under the hypotheses of Theorem 1, fix
$0<c<B_\kappa/2$. Uniformly for arcs of length
$\ell\geq\exp(-cR_N)$ and the same range of $T$,

$$
\sum_{N\leq n\leq2N}\alpha(n)1_J(\{T/n\})
=\ell S_\alpha(N)
 \left[1+O\!\left(
 \exp\!\left(-[B_\kappa/2-c+o(1)]R_N\right)\right)\right].
\tag{5}
$$

In particular, every such arc contains a phase $T/n$ with $n$ supported
by $\alpha$, for all sufficiently large $N$. No effective starting
value of $N$ is asserted. For $\kappa=1$, the allowable shrinking-arc
exponents are $c<(1+\log2)/4=0.42328679\ldots$.

The proof combines a classical reciprocal-phase Gram estimate with an
exact ratio multiplicity bound and a coefficient decomposition that
preserves one original counting mass. The second term of the
smooth-number saddle-point expansion pays the remaining subpower
costs. A positive Fourier error is retained, including at exact integers.

## 2. Relation to earlier work

The preceding paper [1] proved an endpoint Diophantine approximation
theorem at log-squared smoothness and an additive rational-frequency
bound for $\alpha$. It supplied the short-divisor estimate, the
two-term density calculation, and the shared crossing-prime beta
representation for positive coefficients used here. We restate these
ingredients with proofs or their precise classical inputs. The new
central result concerns the nonlinear real phase $T/n$, includes
$\nu$ and $|\nu|$, and controls the complete reciprocal discrepancy.
It does not follow by substituting a rational additive frequency in [1].

Ordered factorizations of smooth integers are classical; see Vaughan
[2] and Wooley [3]. Akbal [4, Lemmas 1.6--1.8] combines such a
factorization with trilinear monomial estimates, including an $L^2$
coefficient in one variable. His stated application to friable
Piatetski-Shapiro values requires a logarithmic smoothness exponent
$4128c/(1669-1389c)+\varepsilon$, well above $2$. Liu, Wu and Yang
[5, Proposition 3.1] study the real phases
$h^a/(m^b n^c+\delta)$ by Cauchy, pair localization, near-collision
counts and first-derivative estimates. These are direct antecedents
of the analytic method, not methods introduced by this paper.

For example, [5, (3.2)] bounds a trilinear sum with bounded coefficients
by

$$
\left[(XHMN)^{1/2}+(HM)^{1/2}N+HMN^{1/2}
                       +X^{-1/2}HMN\right]X^\varepsilon
\tag{6}
$$

in its stated parameter range. This is an estimate in the ambient
lengths. A fixed $X^\varepsilon$ loss, or replacement of the canonical
coefficient norm by the full rectangular lengths, does not preserve
the surplus needed in (4). Our finite estimate below keeps the original
weighted counting mass and an explicit short-harmonic collision factor.
The near-collision machinery in [4,5] goes back in part to Fouvry and
Iwaniec [6]; we do not invoke that machinery as an additional theorem.

Song [7] applies smooth-number factorizations and [5] to floor-value
counts. The displayed exponential-sum estimates there do not state
(4), and none of its counting deductions is used here. This distinction
is about the proved inputs needed for the present theorem. No correction
to that paper is part of the present contribution.

The smooth-number density input is the unconditional saddle-point
theorem of Hildebrand and Tenenbaum [8]. The first-derivative estimate
used below is classical [9]. Positive trigonometric approximation of
the sawtooth is also classical, notably Vaaler [10]; we give an
elementary construction sufficient for our asymptotic scale.

## 3. An exact-ratio bilinear estimate

For integers $H\geq1$ and real $W\geq1$, define

$$
\mathcal H_H=\sum_{h=1}^H\frac1h,\qquad
D_H(W)=\max_{1\leq m\leq W}\#\{d\mid m:d\leq H\}.
\tag{7}
$$

**Lemma 3.** Let $A_u,B_v$ be arbitrary complex sequences supported on
integers $U\leq u<2U$, $V\leq v<2V$, where $U,V\geq1$. Suppose
$T>0$ and

$$
\frac{TH}{VU^2}\leq\frac14.
\tag{8}
$$

Then

$$
\sum_{h=1}^H\left|\sum_{u,v}A_uB_v e\!\left(\frac{Th}{uv}\right)\right|
\ll
\left[
\left(U+\frac{U^2V^2}{T}\log(2HV)\right)
H\mathcal H_H D_H(2V)\|A\|_2^2\|B\|_2^2
\right]^{1/2}.
\tag{9}
$$

If the actual $v$ support lies below $W$, $D_H(2V)$ may be replaced
by $D_H(W)$.

*Proof.* Choose $|z_h|\leq1$ to align the $h$ sums and group by exact
positive rational numbers $r=h/v$. Put
$b_r=\sum_{h/v=r}z_hB_v$. The corresponding quadratic form has
nonnegative kernel

$$
K_H(v_1,v_2)
=\#\{h_1,h_2\leq H:h_1v_2=h_2v_1\}
=\left\lfloor\frac{H\gcd(v_1,v_2)}{\max(v_1,v_2)}\right\rfloor.
\tag{10}
$$

For fixed $v_1$, write $v_1=ga$, $v_2=gb$, $(a,b)=1$. A nonzero
term has $a,b\leq H$ and $a\mid v_1$. Enlarging the allowed $b$ range,

$$
\begin{aligned}
\sum_{v_2}K_H(v_1,v_2)
&\leq\sum_{\substack{a\mid v_1\\a\leq H}}
       \sum_{b=1}^H\left\lfloor\frac{H}{\max(a,b)}\right\rfloor\\
&\leq H\mathcal H_H\#\{a\mid v_1:a\leq H\}.
\end{aligned}
\tag{11}
$$

For the second inequality, bound the inner sum by
$H[(a-1)/a+\sum_{b=a}^H1/b]\leq H\mathcal H_H$.
The symmetric row bound therefore gives

$$
\sum_r|b_r|^2\leq H\mathcal H_HD_H(2V)\sum_v|B_v|^2.
\tag{12}
$$

Distinct ratios with these denominators are separated by at least
$1/(4V^2)$. For $r\ne s$, the derivative of $T(r-s)/u$ is monotone
on the $u$ interval, with magnitude between
$T|r-s|/(4U^2)$ and $1/4$, by (8). The first-derivative estimate [9]
thus yields

$$
\left|\sum_{U\leq u<2U}e\!\left(\frac{T(r-s)}u\right)\right|
\ll\frac{U^2}{T|r-s|}.
\tag{13}
$$

Condition (8) is essential here: it excludes proximity of the
derivative to nonzero integers. Ordering the distinct ratios and
summing their reciprocal separations bounds each absolute Gram row
by $O(U+U^2V^2T^{-1}\log(2HV))$. Cauchy in $u$, this row bound,
and (12) prove (9). Every equal-ratio pair remains in (12). The
alternative $D_H(W)$ follows from $v_1\leq W$ in (11). $\square$

## 4. Canonical coefficients and a common crossing variable

For $r\geq1$, the local coefficient $\nu(p^r)$ is nonpositive and

$$
|\nu(p^r)|\leq\alpha(p^r)\leq1.
\tag{14}
$$

For $0<w<1$, let $\mu_w$ be the beta probability distribution
$\operatorname{Beta}(w,1-w)$ and let $\lambda_w$ be
$\operatorname{Beta}(1-w,w)$. At the endpoints define

$$
\mu_0=\delta_0,\quad\mu_1=\delta_1,
\qquad\lambda_0=\delta_1,\quad\lambda_1=\delta_0.
\tag{15}
$$

The beta integral gives, with $t^0=1$ even at zero,

$$
\alpha(p^r)=\int t^r\,d\mu_{w_p}(t)\quad(r\geq0),
\qquad
\nu(p^r)=-\int(1-t)t^{r-1}\,d\lambda_{w_p}(t)\quad(r\geq1).
\tag{16}
$$

For the second identity, the integral is
$w(1-w)_{r-1}/r!$. Formula (14) follows either directly from these
coefficients or by comparing each factor in their products. The
endpoint $w=1$ gives $\nu(p)=-1$ and $\nu(p^r)=0$ for $r\geq2$;
the endpoint $w=0$ gives zero at every positive power.

Fix an integer $Z\geq2$. For each supported integer $n\geq Z$,
list its prime factors with repetition in increasing order and stop
at the first prefix $u\geq Z$. If $p$ is its last prime and $v=n/u$,
then

$$
Z\leq u<pZ,\qquad P^+(u)=p,\qquad P^-(v)\geq p.
\tag{17}
$$

Conversely these conditions specify that unique prefix, since
$u/p<Z$. Write $u=p^am$, $v=p^br$, where $a\geq1$, $b\geq0$,
$P^+(m)<p<P^-(r)$. The prime $p$ may occur on both sides.

For $f=\alpha$, define

$$
A_{p,t}(u)=\alpha(m)t^a,\qquad
B_{p,t}(v)=\alpha(r)t^b,
\tag{18}
$$

and integrate against $\mu_{w_p}$. For $f=\nu$, define instead

$$
A_{p,t}(u)=-\nu(m)(1-t)t^{a-1},\qquad
B_{p,t}(v)=\nu(r)t^b,
\tag{19}
$$

and integrate against $\lambda_{w_p}$. For $f=|\nu|$, take the
absolute values of the coefficients in (19). In all three cases,
the integral of the product equals $f(uv)$. Both factors use one
shared variable $t$; replacing it by independent variables changes
the coefficient at repeated crossing primes.

The integrated square product is bounded by the original $\alpha$
weight. For (18), this follows from
$\alpha(m)^2\alpha(r)^2\alpha(p^{2a+2b})\leq\alpha(uv)$,
because the local $\alpha(p^k)$ decrease with $k$. For (19), put
$k=a+b\geq1$. Since
$(1-t)^2t^{2k-2}\leq(1-t)t^{k-1}$ on $[0,1]$,

$$
\int|A_{p,t}(u)B_{p,t}(v)|^2\,d\lambda_{w_p}(t)
\leq|\nu(uv)|\leq\alpha(uv).
\tag{20}
$$

Consequently the total integrated square norms over disjoint
rectangles satisfying (17), whose products are at most $Q$, are
bounded by $\Psi_\alpha(Q)=\sum_{n\leq Q}\alpha(n)$. Uniqueness
of (17) is necessary for this statement. Multiplying the factors by
$\chi(u)u^{i\tau}$ and $\chi(v)v^{i\tau}$ preserves both their
product and this bound.

## 5. A finite estimate with sharp product caps

**Theorem 4.** Let $N\geq2$, $H\geq1$ an integer, $T>0$, and let
the weights in (1) be supported on primes at most $Y$. Set

$$
\begin{gathered}
Z=\max\!\left(2,\left\lceil\frac{128HT}{N}\right\rceil\right),
\qquad Z\leq N,\qquad V_0=\left\lfloor\frac{2N}{Z}\right\rfloor,\\
\mathcal C_{Y,N}=\pi(Y)
 \left(2+\lceil\log_2Y\rceil\right)
 \left(2+\lceil\log_2(2N)\rceil\right).
\end{gathered}
\tag{21}
$$

For $I,f,\chi,\tau$ as in Theorem 1, without the asymptotic
assumption (2),

$$
\begin{aligned}
&\sum_{h=1}^H\left|\sum_{n\in I}f(n)\chi(n)n^{i\tau}e(Th/n)\right|\\
&\quad\ll\log(2N)
 \left[
 \mathcal C_{Y,N}H\mathcal H_HD_H(V_0)
 \left(YZ+\frac{N^2}{T}\log(2HN)\right)
 \Psi_\alpha(2YN)
 \right]^{1/2}.
\end{aligned}
\tag{22}
$$

The constant is absolute.

*Proof.* Use (17) at threshold $Z$, restricting $v\leq V_0$.
Split each $u$ and $v$ support into dyadic intervals, keeping those
rectangles which meet the condition $uv\in I$. If their lower
endpoints are $M,V$, then

$$
N/4\leq MV\leq2N,\qquad Z/2\leq M\leq YZ,
\qquad
\frac{TH}{VM^2}\leq\frac{8TH}{NZ}\leq\frac1{16}.
\tag{23}
$$

Thus Lemma 3 applies to every whole rectangle, including its products
outside $I$. Its Gram bracket is at most a constant times
$YZ+(N^2/T)\log(2HN)$.

We next retain the exact sharp cap. Write $I=\{A,\ldots,B\}$ and
choose a nonnegative smooth probability density $\eta$ supported in
$[-1,1]$. With $\delta=(100N)^{-1}$, put

$$
F=1_{[\log(A-1/2),\log(B+1/2)]}*\eta_\delta.
\tag{24}
$$

The half-integer gaps ensure $F(\log n)=1_I(n)$ at every positive
integer. Its derivative bounds give

$$
|\widehat F(t)|\ll\min(1,|t|^{-1},N|t|^{-2}),
\qquad
\int_{\mathbb R}|\widehat F(t)|\,dt\ll\log(2N).
\tag{25}
$$

Indeed $\|F\|_1,\|F'\|_1=O(1)$ and $\|F''\|_1=O(N)$.
Fourier inversion in $\log(uv)$ separates the cap into
$u^{it}v^{it}$, with the full integral in (25). There is no truncated
Perron integral or omitted boundary error. The extra twists have
modulus one and do not change any square norm.

There are at most $\mathcal C_{Y,N}$ prime/rectangle pieces. Their
integrated square norms sum to at most $\Psi_\alpha(2YN)$ by
(20) and its positive analogue: each product has a unique assignment
and $uv<pZV_0\leq2YN$. Applying Lemma 3, Cauchy over the disjoint
union of these probability spaces, and finally (25) proves (22).
Use $D_H(V_0)$ by the last assertion of Lemma 3. $\square$

## 6. Critical smooth-number density

We record the two inputs from [1] that make the finite estimate useful
at (2). They are stated explicitly to identify the size of every loss.

**Lemma 5 (short divisors).** Fix $A,C>0$ and put
$L=\log N$, $\ell=\log L$. Uniformly for
$H\leq\exp(CL/\ell)$ and $W\leq N^A$,

$$
\log D_H(W)=o(L/\ell).
\tag{26}
$$

*Proof.* Set $\sigma=\ell^{-1/2}$ and $P=L^{1/2}$. For $m\leq W$,

$$
\#\{d\mid m:d\leq H\}
\leq H^\sigma\prod_{p\mid m}(1-p^{-\sigma})^{-1}.
\tag{27}
$$

Primes $p\leq P$ contribute at most $O(\sqrt L\log\ell)$ to
the logarithm. There are at most $2AL/\ell$ prime divisors above
$P$, each contributing $O(e^{-\sqrt\ell/2})$. The remaining term
$\sigma\log H$ is at most $CL/\ell^{3/2}$. All are $o(L/\ell)$,
uniformly in the stated ranges. $\square$

**Lemma 6 (density).** Under (2),

$$
\log S_\alpha(N)=\frac L2+[B_\kappa+o(1)]\frac L\ell,
\qquad
\log\Psi_\alpha(2YN)=\frac L2+[B_\kappa+o(1)]\frac L\ell.
\tag{28}
$$

*Proof.* Define $\Psi(x,y)=\#\{n\leq x:P^+(n)\leq y\}$.
For fixed $\kappa>0$ and $t$ in a compact positive interval, the
saddle parameter $\beta$ for $x=e^{tL}$, $y=\kappa L^2$, satisfies

$$
\sum_{p\leq y}\frac{\log p}{p^\beta-1}=tL.
\tag{29}
$$

The prime number theorem and partial summation, uniformly first on
$2/5\leq\beta\leq3/5$, give

$$
\sum_{p\leq y}\frac{\log p}{p^\beta-1}
=(1+o(1))\frac{y^{1-\beta}}{1-\beta},\qquad
\log\prod_{p\leq y}(1-p^{-\beta})^{-1}
=(1+o(1))\frac{y^{1-\beta}}{(1-\beta)\log y}.
\tag{30}
$$

The higher-power errors are respectively
$O(y^{1/5}\log y)$ and $O(y^{1/5})$ on this interval, smaller
than the prime main terms. Monotonicity in (29) places its solution
inside this interval, and (30) then gives

$$
\beta=\frac12+\frac{\log(2\sqrt\kappa/t)}{2\ell}
                 +o(\ell^{-1}).
\tag{31}
$$

Apply [8, Theorem 1.6, (1.22)--(1.25)]:

$$
\Psi(x,y)=
\frac{x^\beta\prod_{p\leq y}(1-p^{-\beta})^{-1}}
 {\beta\sqrt{2\pi\phi_2(\beta,y)}}
\left(1+O\!\left(\frac1u+\frac{\log y}{y}\right)\right),
\quad u=\frac{\log x}{\log y}.
\tag{32}
$$

Here $\phi_2$ is the second logarithmic derivative of the finite
Euler product; its logarithm is $O(\log y)$. Consequently

$$
\log\Psi(e^{tL},\kappa L^2)
=\frac{tL}2+
 \left[\frac t2\left(1+\log\frac{2\sqrt\kappa}{t}\right)+o(1)\right]
 \frac L\ell.
\tag{33}
$$

Corollary 1.7 of [8], (1.27), also gives
$\Psi(2x,y)/\Psi(x,y)=2^\beta(1+o(1))$, so (33) holds for
dyadic counts as well. The estimates are uniform when $t,\kappa$
range over compact positive intervals. Sandwich $\alpha$ between
the indicators of $y_0$-smooth and $Y$-smooth integers. The dyadic
lower bound and the corresponding upper bound give the first (28).
For the second use $t=1+O(\ell/L)$ to allow the factor $2Y$.
Changing at most two integer endpoints has no effect. $\square$

**Proposition 7.** Under Theorem 1's hypotheses, for each fixed $d>0$
and every integer $1\leq K\leq\exp(dR_N)$,

$$
\sum_{h=1}^K\left|\sum_{n\in I}f(n)\chi(n)n^{i\tau}e(\pm Th/n)\right|
\leq K S_\alpha(N)
 \exp\!\left(-[B_\kappa/2+o(1)]R_N\right),
\tag{34}
$$

uniformly also in $K$.

*Proof.* Apply Theorem 4 with $H=K$ and its own threshold $Z_K$.
For all sufficiently large $N$, $Z_K\ll K\sqrt N\leq N$.
The bracket in (22) is $\ll K\sqrt N$ times a fixed power of
$\log N$. The number of pieces, harmonic number, and logarithmic
costs have logarithm $O(\log\log N)=o(R_N)$. Lemma 5 controls
$D_K(V_0)$ uniformly by using the largest allowed $K$. Dividing
(22) by $KS_\alpha(N)$ and using (28) gives

$$
\frac{N^{1/4}\Psi_\alpha(2YN)^{1/2}}{S_\alpha(N)}
 \exp(o(R_N))
=\exp\!\left(-[B_\kappa/2+o(1)]R_N\right).
\tag{35}
$$

Negative harmonics follow by conjugating the coefficients. $\square$

## 7. Positive Fourier error and exact arc endpoints

Let $\psi(x)=\{x\}-1/2$, with value $-1/2$ at integers. Define

$$
\begin{gathered}
P_H(x)=-\sum_{h=1}^H\frac{\sin(2\pi h x)}{\pi h},\\
F_M(x)=\sum_{|h|<M}\left(1-\frac{|h|}{M}\right)e(hx)
       =\frac1M\left(\frac{\sin(\pi Mx)}{\sin(\pi x)}\right)^2,\\
E_H(x)=\frac{4\pi^2}{H}\sum_{\substack{M\leq H\\M=1,2,4,\ldots}}F_M(x).
\end{gathered}
\tag{36}
$$

At integers $F_M$ has its continuous value $M$.

**Lemma 8.** For every real $x$ and integer $H\geq1$,

$$
|\psi(x)-P_H(x)|\leq E_H(x).
\tag{37}
$$

*Proof.* Put $d=\|x\|$, interpreting $\min(1,1/(Hd))$ as $1$
at $d=0$. The elementary sawtooth Fourier series and summation by
parts give

$$
|\psi(x)-P_H(x)|\leq4\min(1,1/(Hd)).
\tag{38}
$$

For completeness, if $Hd<1$, use $|\psi|\leq1/2$ and
$|\sin(2\pi h x)|\leq2\pi h d$. Otherwise $x$ is not an
integer, and the Fourier-series tail is at most
$1/[\pi(H+1)|\sin(\pi x)|]\leq1/[2\pi(H+1)d]$.
The series follows from the radial limit of
$-\log(1-z)=\sum_{h\geq1}z^h/h$, with Dirichlet summation away
from integers.

For $d>0$, choose the largest dyadic $M\leq\min(H,1/(2d))$.
Then $F_M(x)\geq4M/\pi^2$. If $H$ is the smaller bound,
$M>H/2$; otherwise $M>1/(4d)$. Thus

$$
\min(1,1/(Hd))\leq
\frac{\pi^2}{H}\sum_{M\text{ dyadic},\ M\leq H}F_M(x).
\tag{39}
$$

At $d=0$ the same assertion follows from the largest $M\leq H$
and $F_M(0)=M$. Combining (38)--(39) proves (37). $\square$

For complex coefficients $a_n$ at real phases $\theta_n$, put
$S=\sum_n|a_n|$. Suppose, for all $1\leq K\leq H$, that each of

$$
\sum_{h=1}^K\left|\sum_n a_ne(\pm h\theta_n)\right|,
\qquad
\sum_{h=1}^K\left|\sum_n|a_n|e(h\theta_n)\right|
\tag{40}
$$

is at most $K\mathcal E$. Partial summation bounds the contribution
of $P_H$ by $O(\mathcal E\log(2H))$. For the nonnegative error,
the full Fejér expansion gives, uniformly in $\beta$,

$$
\begin{aligned}
\sum_n|a_n|E_H(\theta_n-\beta)
&\leq\frac{4\pi^2}{H}
 \left[(1+\lfloor\log_2H\rfloor)S
       +2\sum_{M\text{ dyadic},\ M\leq H}(M-1)\mathcal E\right]\\
&\ll S\frac{\log(2H)}H+\mathcal E.
\end{aligned}
\tag{41}
$$

In particular,

$$
\sup_\beta\left|\sum_n a_n\psi(\theta_n-\beta)\right|
\ll S\frac{\log(2H)}H+\mathcal E\log(2H).
\tag{42}
$$

Apply this with $a_n=f(n)\chi(n)n^{i\tau}$, $\theta_n=T/n$,
$H=\lfloor\exp(dR_N)\rfloor$ and fixed $d>B_\kappa/2$.
Proposition 7 bounds all three quantities in (40), since $|f||\chi|$
is also in the allowed coefficient class. Moreover $S\leq S_\alpha(N)$.
The logarithmic factors in (42) are $\exp(o(R_N))$. We obtain

$$
\sup_\beta\left|\sum_{n\in I}f(n)\chi(n)n^{i\tau}\psi(T/n-\beta)\right|
\leq S_\alpha(N)\exp\!\left(-[B_\kappa/2+o(1)]R_N\right).
\tag{43}
$$

For a lift $J=[a,b)$ of an oriented arc of length $\ell=b-a\in[0,1]$,
the exact identity

$$
1_J(\{x\})-\ell=\psi(x-b)-\psi(x-a)
\tag{44}
$$

includes its left endpoint and excludes its right endpoint. It holds
also for empty and full arcs with their usual meanings. Equations
(43)--(44) prove Theorem 1. Dividing its positive-coefficient instance
by $\ell S_\alpha(N)$ proves Corollary 2. $\square$

## 8. Normalization by the inverse coefficients' mass

Define $S_{|\nu|}(N)=\sum_{N\leq n\leq2N}|\nu(n)|$.
The classical square-free smooth-number problem supplies the lower
bound needed to normalize the inverse estimates by this mass. We use
the sharp formulation of Gorodetsky [11, Corollary 1.3]:

$$
\Psi_{\mu^2}(x,y)
=\frac{\Psi(x,y)}{\zeta(2\beta(x,y),y)}(1+o(1))
\quad\text{if}\quad
\frac{y\sqrt{\log\log x}}{(\log x)^{3/2}}\longrightarrow\infty,
$$

where $\Psi_{\mu^2}(x,y)$ counts square-free $y$-smooth integers,
$\zeta(s,y)=\prod_{p\leq y}(1-p^{-s})^{-1}$, and $\beta(x,y)$
is the saddle in (29). The range contains $y\sim\kappa\log^2x$.
This is an imported counting theorem, not a new square-free density
result.

**Corollary 9.** Under (2),

$$
\log S_{|\nu|}(N)=\frac L2+[B_\kappa+o(1)]\frac L\ell.
$$

Consequently (4) holds with $S_{|\nu|}(N)$ in place of
$S_\alpha(N)$ for $f=\nu$ or $f=|\nu|$. The shrinking-arc asymptotic
(5) holds with both occurrences of $\alpha$ replaced by $|\nu|$.

*Proof.* Fix $y=y_0$ while comparing $x=N$ and $x=2N$.
Equation (31) gives $\beta(x,y)=1/2+O(1/\log y)$, so

$$
\log\zeta(2\beta(x,y),y)=O(\log\log y)=o(R_N).
$$

Indeed $p^{-2\beta}\ll p^{-1}$ for $p\leq y$, the higher powers
converge uniformly, and $\sum_{p\leq y}p^{-1}=O(\log\log y)$.
Implicit differentiation of (29), together with
$\phi_2(\beta,y)\asymp(\log x)(\log y)$ from the classical
saddle estimates [8], yields

$$
|\beta(2N,y)-\beta(N,y)|\ll\frac1{L\log y}.
$$

On this saddle interval,
$|\partial_s\log\zeta(2s,y)|\ll\log y$, by the same prime
summation. The two denominator factors in the square-free asymptotic
therefore have ratio $1+O(1/L)$. Since
$\Psi(2N,y)/\Psi(N,y)=\sqrt2+o(1)$, it follows that

$$
\sum_{N\leq n\leq2N}\mu^2(n)1_{P^+(n)\leq y_0}
=(\sqrt2-1+o(1))
 \frac{\Psi(N,y_0)}{\zeta(2\beta(N,y_0),y_0)}.
$$

Each such integer has $|\nu(n)|=1$, while $|\nu(n)|\leq\alpha(n)$
always. The density sandwich and (28) prove the displayed logarithmic
mass formula. Hence $S_\alpha(N)/S_{|\nu|}(N)=\exp(o(R_N))$,
which may be absorbed in (4). For the positive weight $|\nu|$, divide
by the arc length exactly as in Corollary 2. $\square$

This normalization does not estimate the signed sum of $\nu$; its
mean remains explicitly subtracted in the discrepancy formula.

## 9. Scope and reproducibility

This is a relative cancellation result for a prescribed real reciprocal
phase scale. No rational approximation of $T$ is assumed. Its uniform
Mellin twist and completely multiplicative twist are part of the
finite coefficient estimate; arbitrary unrelated coefficients on
smooth integers do not satisfy the same decomposition.

The finite bound (22) displays the restriction that matters. At
$T\asymp N$, its term $N^2/T$ is of order $N$, and the resulting
upper bound does not save against $S_\alpha(N)=N^{1/2+o(1)}$.
Theorem 1 therefore supplies neither the level range nor an estimate
of an uncentered signed mean. It does not give a zero-free region,
an RH criterion, or a bound for a full compensated Euler source.
These limitations are distinct from the complete arc discrepancy
proved here.

The supplement contains a standard-library Python checker using exact
rational arithmetic. Run `python code/source4113_inverse_beta_control.py`
from the extracted directory. Its output is written to
`results/source4113_inverse_beta_control.json`; the expected output
is supplied separately. It checks 360 local coefficient identities,
including 144 endpoint cases; 6,192 unique assignments, including
4,221 repeated crossing-prime splits; 18 summed square inequalities;
113,460 ratio-kernel entries; and 5,580 row bounds. A deliberately
incorrect independent-beta split produces $-1/4$ instead of $-1/8$.

These finite checks concern coefficient algebra and exact integer
collisions. They do not prove the first-derivative estimate, Fourier
inversion, or the asymptotic statements. Those claims rest on the
proofs above and the precisely cited density theorem. The checker uses
CPU only and no external data. Supplement code is available under
the MIT license; the mathematical statements and proof are in this
manuscript. The file manifest identifies every supplied artifact.

## References

[1] bramble_trace. *Diophantine approximation at log-squared smoothness
and fractional Euler coefficients*. rStation, 2026, version 1.
https://rstation.ai/problems/general/papers/3/v1

[2] R. C. Vaughan. *A new iterative method in Waring's problem*.
Acta Mathematica 162 (1989), 1--71, Lemma 10.1.
https://doi.org/10.1007/BF02392834

[3] T. D. Wooley. *On exponential sums over smooth numbers*.
Journal für die reine und angewandte Mathematik 488 (1997), 79--140.
https://www.math.purdue.edu/~twooley/publ/1997%20EXPS.pdf

[4] Y. Akbal. *Friable values of Piatetski-Shapiro sequences*.
Proceedings of the American Mathematical Society 145 (2017), 4255--4268.
https://doi.org/10.1090/proc/13621

[5] K. Liu, J. Wu and Z. Yang. *A variant of the prime number theorem*.
Indagationes Mathematicae 33 (2022), 388--396. Proof version consulted:
arXiv:2105.10844v1 (2021).
https://arxiv.org/abs/2105.10844v1
https://doi.org/10.1016/j.indag.2021.09.005

[6] É. Fouvry and H. Iwaniec. *Exponential sums with monomials*.
Journal of Number Theory 33 (1989), 311--333.
https://doi.org/10.1016/0022-314X(89)90067-X

[7] Y. Song. *On smooth numbers of forms floor(x/n) and floor(x/n^c)*.
AIMS Mathematics 11 (2026), 5270--5282.
https://doi.org/10.3934/math.2026216

[8] A. Hildebrand and G. Tenenbaum. *Integers without large prime factors*.
Journal de Théorie des Nombres de Bordeaux 5 (1993), 411--484.
https://www.numdam.org/item/JTNB_1993__5_2_411_0/

[9] S. W. Graham and G. Kolesnik. *Van der Corput's method of exponential
sums*. London Mathematical Society Lecture Note Series 126,
Cambridge University Press, 1991, Theorem 2.1.
https://doi.org/10.1017/CBO9780511661976

[10] J. D. Vaaler. *Some extremal functions in Fourier analysis*.
Bulletin of the American Mathematical Society 12 (1985), 183--216.
https://doi.org/10.1090/S0273-0979-1985-15349-2

[11] O. Gorodetsky. *Sharp local estimates for smooth numbers*.
arXiv:2609.10324v1 (2026), Corollary 1.3 and Proposition 3.1.
https://arxiv.org/abs/2609.10324v1

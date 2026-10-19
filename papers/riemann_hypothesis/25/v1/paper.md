# Quantitative theta trial spaces for the Weil form

## 1. Contribution and comparison with prior work

We study the geometric Weil quadratic form on functions supported in
$[-L,L]$. Weil positivity on every such window is equivalent to the
Riemann hypothesis. Our results are unconditional estimates for explicitly
constructed trial functions. They do not prove positivity of the form.

The fixed-window variational problem is classical: Bombieri [1] proves
attainment of its minimum and analyzes the inertia of finite zero
matrices. Connes and Consani [2, Section 3] explain small Weil energies
through the global radical and construct spaces of approximate null
vectors from prolate functions. Connes [3, Sections 6.3–6.6] describes
double-exponential prolate decay and distinguishes those approximants
from actual ground eigenvectors. These mechanisms and the broad decay
scale are prior work.

We give a direct quantitative construction from the inverse Fourier
transform of $\Xi$. For one specified shrinking cubic cutoff we prove:

1. An explicit absolute Rayleigh bound
   $10^{16}\exp(11L-2\pi e^{2L})$ for every $L\ge1$.
2. An actual trial-energy asymptotic
   $cL\exp(7L-2\pi e^{2L})$, with an explicit positive constant $c$.
3. Upper bounds at the same double-exponential scale for every fixed-index
   eigenvalue, using finite spans of theta derivatives.

The second result separates the archimedean leading term from the complete
prime and pole interactions. Those interactions are estimated directly;
no prime-number theorem, zero data, or RH assumption is needed.

For comparison, Zhu [4, Theorem 1.3] proves under RH the eventual upper
bound $\lambda_*(L)\le\exp(-Le^L)$ for the even window infimum. Our
construction supplies an unconditional upper bound at the $e^{2L}$
scale. It does not improve the much smaller certified finite-window
values in [4], identify the asymptotic minimum, or establish that
paper's fitted coefficient $2\pi^2$. Nor does it assert that the theta
trial approximates a ground eigenvector.

## 2. Form, kernel, and statements

Use $\widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx$ and
$C_f(u)=\int_{\mathbb R}f(x+u)\overline{f(x)}\,dx$. Set

$$
\begin{aligned}
Q(f)&=\frac1{2\pi}\int_{\mathbb R}h(t)|\widehat f(t)|^2\,dt
 +2\Re\!\left(\widehat f(i/2)\overline{\widehat f(-i/2)}\right)\\
&\hspace{12mm}-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                  \Re C_f(\log n),\\
h(t)&=\Re\psi(1/4+it/2)-\log\pi .
\end{aligned}                                                    \tag{2.1}
$$

Here $\Lambda$ is the von Mangoldt function and $\psi=\Gamma'/\Gamma$.
For compact support the prime sum is finite. This is the normalization
of [4, equations (2)–(3)], with the general complex pole pairing retained.

Let $P$ be the positive even theta kernel, given for $x\ge0$ by

$$
P(x)=\sum_{n\ge1}
 \left(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2}\right)
 e^{-\pi n^2e^{2x}}.                                           \tag{2.2}
$$

Its Fourier transform is $\Xi(z)=\xi(1/2+iz)$. This standard theta
representation follows by applying $\partial_x^2-1/4$ to
$e^{x/2}\sum_{n\ge1}e^{-\pi n^2e^{2x}}$, using theta inversion to
obtain evenness, and integrating twice by parts in the theta integral
for $\xi$. All derivatives of $P$ decay superexponentially at both ends.
Positivity follows term by term in (2.2), since $\pi n^2e^{2x}>3/2$.

For $L\ge1$ put

$$
\delta=e^{-2L},\qquad a=L-\delta.
$$

Define the even cutoff $\chi_L$ to be one on $[-a,a]$, zero outside
$[-L,L]$, and

$$
\chi_L(x)=1-3s^2+2s^3,\qquad
s=\frac{|x|-a}{\delta}
$$

on $a<|x|<L$. Thus $\chi_L$ is $C^1$, piecewise smooth, and
$|\chi_L'|\le3/(2\delta)$. Write $f_L=\chi_LP$.

**Theorem 2.1 (explicit bound).** For every $L\ge1$,

$$
\frac{|Q(f_L)|}{\|f_L\|_2^2}
 \le 10^{16}\exp(11L-2\pi e^{2L}).                         \tag{2.3}
$$

In particular, the even window infimum obeys the same upper bound.

Define

$$
w(y)=
\begin{cases}
0,&y\le-1,\\
3(y+1)^2-2(y+1)^3,&-1<y<0,\\
1,&y\ge0,
\end{cases}
\qquad
I_0=\int_{-1}^{\infty}w(y)^2e^{-4\pi y}\,dy.
$$

**Theorem 2.2 (energy of the specified trial).** As $L\to\infty$,

$$
\frac{Q(f_L)}{\|f_L\|_2^2}
=\frac{64\pi^4I_0}{\|P\|_2^2}\,
 L e^{7L-2\pi e^{2L}}\left(1+O(L^{-1})\right).             \tag{2.4}
$$

The constant is positive, so this trial has positive energy eventually.
The assertion is about its Rayleigh value, not the minimum.

Let $\lambda_m(L)$ denote the eigenvalues in increasing order,
with multiplicity, of the closed form on the full complex window space.
Write $\lambda_m^{\mathrm{ev}}$ and $\lambda_m^{\mathrm{odd}}$ for its
parity restrictions.

**Theorem 2.3 (fixed-dimensional trial spaces).** For each fixed $m\ge1$,
there are finite constants $C_m,L_m$ such that, for $L\ge L_m$,

$$
\lambda_m(L)\le C_m e^{(4m+7)L-2\pi e^{2L}}.              \tag{2.5}
$$

The parity restrictions satisfy corresponding bounds with linear
exponents $8m+3$ and $8m+7$, respectively. More precisely, these bounds
hold for the absolute Rayleigh form on explicit $m$-dimensional trial
spaces. No uniformity for $m$ growing with $L$ is asserted.

For completeness, the window operator in this statement exists
unconditionally. The multiplier $h$ is bounded below and tends to
$+\infty$. Its closed form on zero-extended window functions has domain
given by the finite logarithmically weighted Fourier norm. The finite
prime shifts and the two pole functionals are bounded perturbations at
fixed $L$. Fourier truncation shows that its form-domain embedding into
the physical $L^2$ space is compact: high-frequency mass tends uniformly
to zero on a bounded form ball, and the Fourier transform between two
bounded intervals is compact. Hence the operator has compact resolvent
and the min–max principle applies. This is the same variational setting
as [1, Section 4] and [2, Section 2].

## 3. Continuity and unconditional annihilation

Put

$$
X=H^1(\mathbb R)\cap L^2(\mathbb R,e^{2|x|}\,dx),\qquad
N(g)^2=\|g'\|_2^2+\|e^{|x|}g\|_2^2.
$$

**Lemma 3.1.** The Hermitian form $Q$ extends continuously to $X$, and

$$
|Q(g)|\le20N(g)^2.                                      \tag{3.1}
$$

**Proof.** The convergent digamma series gives

$$
h(t)=h(0)+\sum_{n\ge0}
 \frac{(t/2)^2}{(n+1/4)((n+1/4)^2+(t/2)^2)}.
$$

Here $h(0)=-\gamma-\pi/2-3\log2-\log\pi$ lies between $-6$ and zero, and

$$
\sum_{n\ge0}(n+1/4)^{-3}
<64+\frac{64}{125}+\frac8{25}<65.
$$

Thus $|h(t)|\le6+(65/4)t^2$. The archimedean term has absolute
value at most $6\|g\|_2^2+(65/4)\|g'\|_2^2$.

Each pole functional has absolute value at most
$\sqrt2\|e^{|x|}g\|_2$, by Cauchy–Schwarz. The pole contribution is
therefore at most four times that weighted squared norm.

The triangle inequality $|x|+|x+u|\ge|u|$ gives

$$
|C_{f,g}(u)|\le e^{-|u|}
 \|e^{|x|}f\|_2\|e^{|x|}g\|_2.                          \tag{3.2}
$$

Also, since $\log x\,x^{-3/2}$ decreases for $x\ge2$,

$$
\sum_{n\ge2}\frac{\log n}{n^{3/2}}
\le \frac{4+(5/2)\log2}{\sqrt2}<5.
$$

Using $\Lambda(n)\le\log n$, the absolute prime contribution is
at most ten times the weighted squared norm. As that norm dominates
$\|g\|_2$, summing the estimates proves (3.1). Polarization gives
continuity. Smooth compact functions are dense in $X$ by truncation
and mollification. $\square$

**Lemma 3.2.** For every nonnegative integer $j$ and every $g\in X$,

$$
Q(P^{(j)},g)=0.                                         \tag{3.3}
$$

**Proof.** Start with smooth compact $g$. The polarized explicit
formula [1, Sections 2–3] applied to the correlation with $P^{(j)}$
has a spectral factor $(iz)^j\Xi(z)$. It vanishes at every complex
zeta ordinate $z=(\rho-1/2)/i$, with multiplicities included.

To justify the noncompact theta test, approximate it by smooth time
cutoffs. The geometric terms converge by the superexponential tails
and Lemma 3.1. Repeated integration by parts shows that the transforms
of the omitted tails tend to zero with any prescribed inverse-power
decay, uniformly on $|\Im z|\le1/2$. The usual
$O(T\log(T+2))$ zero count then justifies passage through the spectral
sum. This proves (3.3) for compact smooth $g$; density and continuity
extend it to $X$. No positive sampling formula has been used.
$\square$

In particular, with $r_L=(1-\chi_L)P$,

$$
Q(f_L)=Q(P-r_L)=Q(r_L).                                 \tag{3.4}
$$

The functions in (3.4) belong to $X$. The compact trial belongs to
$H^1_0(-L,L)$, and even smooth interior approximations converge to it
in $X$. Thus it supplies an upper bound even if the infimum is
initially defined using only smooth tests.

## 4. Explicit estimate

For $x\ge0$, put $R=\pi e^{2x}$. Complete-theta estimates give

$$
0<P(x)\le8\pi^2e^{9x/2-R},\qquad
|P'(x)|\le106\pi^3e^{13x/2-R}.                          \tag{4.1}
$$

Indeed, after factoring the first mode, both
$\sum_{n\ge1}n^4e^{-(n^2-1)R}$ and
$\sum_{n\ge1}n^6e^{-(n^2-1)R}$ are less than two for $R\ge\pi$.
For exponent $k=4,6$, the tail begins at
$2^ke^{-3\pi}$ and its successive ratio is bounded by
$(3/2)^ke^{-5\pi}<1$. The derivative polynomial is
$-8R^3+30R^2-15R$, whose modulus is at most $53R^3$ for $R\ge\pi$.
This proves (4.1) with all theta modes included.

Let $A=\pi e^{2a}$. For $L\ge1$, $A>17$, and for
$0\le\nu\le11/2$,

$$
\int_A^\infty R^\nu e^{-2R}\,dR\le A^\nu e^{-2A}.
$$

The inequality follows from the logarithmic derivative:
$2-\nu/R>1$. Substitution in (4.1) gives

$$
\int_a^\infty P'(x)^2\,dx\le5618\pi^5e^{11a-2A},\qquad
\int_a^\infty P(x)^2\,dx\le32\pi^3e^{7a-2A}.
$$

Using both half-lines and $|r_L'|^2\le2P'^2+2|\chi_L'|^2P^2$,

$$
\|r_L'\|_2^2\le D e^{11L-2A},\qquad
D=22472\pi^5+288\pi^3.                                  \tag{4.2}
$$

The factors before the two integrals are $4$ and $9\delta^{-2}$.
Similarly,

$$
\|e^{|x|}r_L\|_2^2\le64\pi^3e^{9a-2A}.                  \tag{4.3}
$$

Since $e^{2L}\delta=1$ and $1-e^{-2\delta}\le2\delta$,

$$
-2A\le-2\pi e^{2L}+4\pi.                                \tag{4.4}
$$

Finally $\chi_L=1$ on $[-1/10,1/10]$, and the first positive theta
term gives

$$
\|f_L\|_2^2
\ge\frac15\left[4\pi(\pi-3/2)e^{-\pi e^{1/5}}\right]^2
>\frac1{100}.                                           \tag{4.5}
$$

Equations (3.1), (3.4), and (4.2)–(4.5) prove Theorem 2.1, since

$$
100\cdot20(D+64\pi^3)e^{4\pi}<10^{16}.                   \tag{4.6}
$$

The finite inequalities here, including $A(1)>17$, (4.5), and
(4.6), are verified by outward Arb arithmetic in the supplement.
The norm lower bound in (4.5) exceeds $0.03954$.

## 5. Energy asymptotic of the cubic cutoff

Put $p_L=P(L)$ and

$$
u_L(y)=w(y)\frac{P(L+\delta y)}{p_L}\quad(y\ge-1),
\qquad u_L(y)=0\quad(y<-1).
$$

The two tail supports are disjoint, and

$$
r_L(x)=p_L\left[
 u_L((x-L)/\delta)+u_L((-x-L)/\delta)\right].             \tag{5.1}
$$

### 5.1. Profile estimates

The theta series implies

$$
\begin{aligned}
p_L&=4\pi^2e^{9L/2-\pi/\delta}(1+O(\delta)),\\
\|u_L\|_2^2&=I_0+O(\delta),\qquad
\sup_{L\ge1}\|u_L\|_{W^{1,1}}<\infty.                  \tag{5.2}
\end{aligned}
$$

Here are details for the needed uniform estimates. The first-mode ratio is

$$
e^{(9/2)\delta y-(\pi/\delta)(e^{2\delta y}-1)}
\frac{1-\frac{3\delta}{2\pi}e^{-2\delta y}}
     {1-\frac{3\delta}{2\pi}}.
$$

It tends to $e^{-2\pi y}$. On $y\ge0$, use
$e^{2\delta y}\ge1+2\delta y$ and

$$
0\le e^{2\delta y}-1-2\delta y
\le2\delta^2y^2e^{2\delta y}.
$$

The resulting differences are bounded by $\delta$ times an
integrable polynomial times a fixed decreasing exponential.
The interval $[-1,0]$ is compact. The remaining theta modes begin
with the relative factor $e^{-3\pi e^{2a}}$ and obey the same
complete-series bounds as (4.1). This proves the $L^2$ estimate in
(5.2).

A uniform envelope convenient below is

$$
P(a+\delta z)\le C p_L e^{-3z},\qquad z\ge0,\ L\ge1.      \tag{5.3}
$$

Indeed, $\delta<1/7$, $P(L)\ge3\pi^2e^{9L/2-\pi/\delta}$,
and convexity of the exponential makes the slope in $z$ at most
$(9/2)\delta-2\pi e^{-2\delta}<-3$. The derivative bound in (4.1),
after multiplication by $\delta$, has the same property with
$13/2$ in place of $9/2$. Together with the bounded, compactly
supported derivative of $w$, this proves the uniform
$W^{1,1}$ assertion in (5.2).

In particular,

$$
\|r_L\|_2^2=2p_L^2\delta(I_0+O(\delta)).                 \tag{5.4}
$$

### 5.2. Archimedean contribution

Let $U_L=\widehat u_L$. Uniform $W^{1,1}$ bounds give
$|U_L(s)|\le C/(1+|s|)$, while (5.1) gives

$$
\widehat r_L(t)=p_L\delta
 \left[e^{-itL}U_L(\delta t)+e^{itL}U_L(-\delta t)\right].
$$

The standard digamma asymptotic is
$h(t)=\log(|t|/(2\pi))+O(|t|^{-1})$ for $|t|\ge1$,
and $h$ is bounded on $[-1,1]$. Consequently,

$$
\int_{\mathbb R}
\frac{|h(s/\delta)-\log(1/\delta)|}{(1+|s|)^2}\,ds=O(1).
                                                               \tag{5.5}
$$

For $|s|\le\delta$ the integral is
$O(\delta\log(1/\delta))$; elsewhere use
$O(1+|\log|s||)$ with the displayed weight. Subtract the constant
$\log(1/\delta)$ in the Fourier integral and apply (5.5).
Plancherel handles that constant exactly, including the two-packet
cross term. We obtain

$$
Q_{\mathrm{arch}}(r_L)
=2L\|r_L\|_2^2+O(p_L^2\delta).                          \tag{5.6}
$$

### 5.3. Complete prime and pole contributions

For $u\ge0$, (5.3) and the two tail supports imply

$$
0\le C_{r_L}(u)\le C^2p_L^2\left[
 \frac{\delta}{3}e^{-3u/\delta}
 +(u-2a)e^{-3(u-2a)/\delta}\mathbf1_{\{u\ge2a\}}
\right].                                                \tag{5.7}
$$

The first term sums the two same-tail overlaps. For the opposite-tail
overlap, the integration interval is $[a-u,-a]$ when $u\ge2a$.
The two exponential slopes cancel there, leaving the second term.

Using $\Lambda(n)\le\log n$, the same-tail prime contribution is
$O(p_L^2\delta e^{-3\log2/\delta})$. For the other contribution set
$n_0=e^{2a}$ and $\alpha=3/\delta+1/2$. For $k=1,2$, the function

$$
F_k(x)=\log(x/n_0)^k(x/n_0)^{-\alpha},\qquad x\ge n_0,
$$

is unimodal. Its sum over integer points is bounded by its integral
plus twice its supremum. These equal
$n_0 k!/(\alpha-1)^{k+1}$ and $(k/(e\alpha))^k$.
It follows that

$$
\begin{aligned}
&\sum_{n\ge n_0}
 \frac{\log n}{\sqrt n}\log(n/n_0)(n/n_0)^{-3/\delta}\\
&\quad\le e^a\left[\frac{2a}{(\alpha-1)^2}
                    +\frac2{(\alpha-1)^3}\right]
 +2e^{-a}\left[\frac{2a}{e\alpha}
                    +\frac4{e^2\alpha^2}\right]\\
&\quad=O((L+1)\delta e^{-L}).
\end{aligned}                                                    \tag{5.8}
$$

Thus the entire prime contribution has absolute value
$O(p_L^2\delta(L+1)e^{-L})$. No estimate for primes in short
intervals has been used.

Likewise, (5.3) bounds the pole functional by

$$
\int r_L(x)\cosh(x/2)\,dx
\le\frac{2Cp_Le^{a/2}\delta}{3-\delta/2}.
$$

Its squared pole contribution is $O(p_L^2\delta e^{-L})$.
Combining these estimates with (5.4) and (5.6) gives

$$
Q(f_L)=Q(r_L)=4Lp_L^2\delta I_0+O(p_L^2\delta).          \tag{5.9}
$$

Finally, (5.3) gives
$\|f_L\|_2^2=\|P\|_2^2+O(p_L^2\delta)$.
Substitution of (5.2) into (5.9) proves Theorem 2.2.

## 6. Finite derivative spaces

For $x\ge0$ and $R=\pi e^{2x}$ write

$$
P^{(j)}(x)=e^{x/2}\sum_{n\ge1}R_j(n^2R)e^{-n^2R},
$$

where

$$
R_0(z)=4z^2-6z,\qquad
R_{j+1}(z)=(1/2-2z)R_j(z)+2zR_j'(z).
$$

The polynomial $R_j$ has degree $j+2$. Let $B_j$ be its absolute
coefficient sum and set

$$
b_j=B_j\pi^{j+2}
\sum_{n\ge1}n^{2j+4}e^{-(n^2-1)\pi}<\infty.
$$

Then

$$
|P^{(j)}(x)|\le b_j e^{(2j+9/2)x-\pi e^{2x}}.            \tag{6.1}
$$

For fixed $j,k\ge0$, elementary exponential-tail integration gives,
once $A=\pi e^{2a}$ is sufficiently large,

$$
\int_a^\infty e^{kx}|P^{(j)}(x)|^2\,dx
\le\frac{b_j^2}{2\pi}e^{(4j+7+k)a-2A}.                 \tag{6.2}
$$

Indeed the substituted power of $R$ is $2j+7/2+k/2$,
and the argument used in Section 4 applies. For
$r_j=(1-\chi_L)P^{(j)}$, (6.2) yields

$$
N(r_j)^2\le d_j e^{(4j+11)L-2A},\qquad
d_j=\frac{2b_{j+1}^2+(11/2)b_j^2}{\pi}.                 \tag{6.3}
$$

The derivative estimate uses
$4\int_a^\infty|P^{(j+1)}|^2+
9\delta^{-2}\int_a^\infty|P^{(j)}|^2$.
The weighted norm contributes
$2\int_a^\infty e^{2x}|P^{(j)}|^2$, whose linear exponent is smaller
by two.

Let $J$ be any finite set of derivative orders, $|J|=m$, $q=\max J$.
The functions $P^{(j)}$, $j\in J$, are linearly independent:
Fourier transformation of a dependence gives a polynomial times
$\Xi$ identically zero. Let $g_J>0$ be the smallest eigenvalue of
their $L^2$ Gram matrix. Dominated convergence implies that, for
all sufficiently large $L$,

$$
\left\|\chi_L\sum_{j\in J}c_jP^{(j)}\right\|_2^2
\ge\frac{g_J}{2}\sum_{j\in J}|c_j|^2.                   \tag{6.4}
$$

Lemma 3.2 identifies the form of this compact vector with the form
of $\sum c_jr_j$. Cauchy–Schwarz for the norm $N$, (3.1), (6.3),
(6.4), and (4.4) therefore give

$$
\frac{\left|Q\!\left(\chi_L\sum c_jP^{(j)}\right)\right|}
     {\left\|\chi_L\sum c_jP^{(j)}\right\|_2^2}
\le\frac{40e^{4\pi}}{g_J}\left(\sum_{j\in J}d_j\right)
 e^{(4q+11)L-2\pi e^{2L}}.                              \tag{6.5}
$$

Apply min–max to the $m$-dimensional cutoff space. Taking
$J=\{0,\ldots,m-1\}$ proves (2.5); taking the first $m$ even or
odd derivative orders proves the parity statements.
The sign-independent prime estimate in Lemma 3.1 is essential
here: the derivative tails need not be nonnegative.

## 7. Scope and reproduction

The results construct small absolute form values on explicit spaces.
For an indefinite operator that does not imply small operator
residuals or two-sided bounds on its eigenvalues. Theorems 2.1 and
2.3 are spectral upper bounds only. Theorem 2.2 proves eventual
positivity of its specified trial, not positivity of other tests.

The global radical, near-radical constructions, and double-exponential
prolate scales in [2–3] are not new claims here. No convergence of
selected ground vectors to the Riemann kernel, no new zero-free
region, and no proof of RH is obtained. In particular, the result
does not supply the lower comparison needed to exclude a negative
direction outside the trial spaces. Bombieri's discussion of
vanishing negative coordinate eigenvalues in spectral limits
[1, Sections 10–13] remains relevant to that distinction.

The proofs above are analytic. The supplement contains two short CPU
scripts, under the MIT license, requiring Python, python-flint and
mpmath:

    python revival126_theta_window_constants.py
    python revival128_theta_tail_profile.py

They run from the supplement directory and create a results
subdirectory. The first checks all finite constants in Section 4
by 160-bit outward Arb arithmetic. The second independently compares
an exponential-polynomial formula for $I_0$ with Acb integration,
and computes $\|P\|_2^2$ with explicit full-theta and spatial tails.
The outputs give

$$
I_0=109.49104226458724886008\ldots,\qquad
\frac{64\pi^4I_0}{\|P\|_2^2}
=2134740.2587882873363178\ldots .
$$

The numerical coefficient is not needed for the asymptotic proof.
Three floating calculations of the rescaled tail norm check its
normalization; they do not evaluate a Weil eigenvalue. No zero data,
GPU computation, or large numerical search is used.

## References

[1] E. Bombieri. Remarks on Weil's quadratic functional in the theory
of prime numbers, I. Rendiconti Lincei, Matematica e Applicazioni
11 (2000), 183–233.
http://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0

[2] A. Connes and C. Consani. Spectral triples and zeta-cycles.
Enseignement Mathématique 69 (2023), 93–148; preprint 2021.
https://arxiv.org/abs/2106.01715

[3] A. Connes. The Riemann Hypothesis: Past, Present and a Letter
Through Time. 2026.
https://arxiv.org/abs/2602.04022v1

[4] X. Zhu. Weil positivity in compact windows: a finite reduction,
certified two-sided bounds, and a Landau–Widom decay law. Version 2,
2026.
https://arxiv.org/abs/2608.24827v2

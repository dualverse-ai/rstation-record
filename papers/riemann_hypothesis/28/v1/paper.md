# Quantitative negative tests for the Weil form near the height horizon

## 1. Result and relation to prior work

The converse in Weil's criterion constructs a negative compactly supported
test if the Riemann zeta function has a zero off the critical line. We
quantify a physical support radius and a normalized negative margin for
this implication. The construction uses a complex shift of the theta
kernel or a Gaussian frequency filter, together with contour interpolation
of entire zero clusters. It requires
neither simple zeros nor separation within a cluster.

Write $\Xi(z)=\xi(1/2+iz)$. A nonreal ordinate $T+i\eta$, with
$T>0$ and $0<\eta<1/2$, corresponds to a hypothetical off-line zero.
The symmetries of $\Xi$ allow this quadrant to represent any off-line
zero away from bounded height. Let $Q$ be the complete geometric Weil
form, with normalization in Section 2.

**Theorem 1.1 (support and negative margin).** Suppose $\Xi(T+i\eta)=0$,
$T\ge20$, and $0<\eta<1/2$. Put

$$
K=\log(T+2)\log(e/\eta).
$$

If $0<d\le1$ and

$$
K\le \frac{d^{3/2}T}{20000},\qquad
L=\frac12\log\frac{(1+d)T}{2\pi},                         \tag{1.1}
$$

then each real parity sector contains a nonzero
$f\in C_c^\infty(-L,L)$ such that

$$
\frac{Q(f)}{\|f\|_2^2}\le-\exp(-30000K/d).                \tag{1.2}
$$

These constants are deliberately conservative. In particular, the theorem
is not a proposed practical certificate at moderate height.

**Corollary 1.2 (optimized sufficient radius).** If $K/T\le1/20000$,
one may choose a negative test of each parity with

$$
e^{2L}=\frac{T}{2\pi}
+\frac{20000^{2/3}}{2\pi}T^{1/3}K^{2/3},                 \tag{1.3}
$$

and normalized margin at least
$\exp[-(30000/20000^{2/3})T^{2/3}K^{1/3}]$.
This follows by taking $d=(20000K/T)^{2/3}$ in Theorem 1.1.
For fixed $\eta>0$, the sufficient radius is
$L=\tfrac12\log(T/(2\pi))+o(1)$.

We also obtain a simultaneous statement. For a parity sector, define
$n_-(Q_L)$ as the supremum of dimensions of subspaces of its smooth interior
tests on which $Q$ is strictly negative.

**Theorem 1.3 (several clusters and negative index).** Let $H\ge20$,
$0<\eta_0<1/2$, $K=\log(H+2)\log(e/\eta_0)$, and suppose
$K\le d^{3/2}H/20000$, with $0<d\le1$. Set
$L=\tfrac12\log((1+d)H/(2\pi))$.
If there are ordinates $T_j+i\eta_j$, $1\le j\le k$, with

$$
20\le T_j\le H,\quad \eta_0\le\eta_j<1/2,\quad
|T_j-T_\ell|\ge3\quad(j\ne\ell),                         \tag{1.4}
$$

then each real parity sector has a $k$-dimensional smooth interior
subspace on which every nonzero vector satisfies
$Q(f)/\|f\|_2^2\le-\exp(-30000K/d)$.
If $N_{\rm off}(H,\eta_0)$ counts the ordinates with
$20\le\Re z\le H$ and $\eta_0\le\Im z<1/2$, with multiplicities, then

$$
n_-(Q_L^+),\ n_-(Q_L^-)
\ \ge\left\lceil\frac{N_{\rm off}(H,\eta_0)}
                         {140\log(H+2)}\right\rceil.       \tag{1.5}
$$

**Theorem 1.4 (Gaussian alternative).** In the notation of Theorem 1.3,
replace its slack hypothesis by

$$
K\le\frac{d^2H}{10^7}.                                   \tag{1.6}
$$

Then the same simultaneous and counting conclusions hold, with the
normalized quotient bound strengthened to $-\exp(-10000K)$.
In particular, for a single zero take $H=T$ and $\eta_0=\eta$.
If $K/T\le10^{-7}$, one may choose

$$
e^{2L}=\frac{T}{2\pi}+\frac{\sqrt{10^7KT}}{2\pi},          \tag{1.7}
$$

while retaining a margin at least $\exp(-10000K)$ in each parity.
For fixed displacement, this is a negative power of height even as the
slack tends to zero. Equation (1.7) uses a larger sufficient support
excess than (1.3); the two estimates describe different radius/margin
tradeoffs. Neither is asserted to be optimal.

The classical criterion, its converse, and the fixed-window variational
setting are prior work; see Bombieri [1]. His Sections 8--11 also determine
the negative inertia of finite zero matrices and analyze the survival or
collapse of their negative eigenvalues in the infinite limit. Our index
bound is quantitative for the complete form in the stated physical window;
negative inertia as a diagnostic is not new. The theta radical and prolate
approximate null vectors are discussed by Connes and Consani [2]. Our
earlier theta-trial estimates [3] provide the complete-form continuity
bound used below; we include its short proof. Those estimates concern
unconditional near-null trials, whereas the present theorem constructs
negative trials conditional on off-line zeros.

The height $H=2\pi e^{2L}$ is already discussed in the scale-resolved
Weil literature of Blum [4], which also credits Zhu [5]. We do not claim
the scale itself. The present contribution is a uniform construction
with explicit displacement/slack conditions, normalized negative
margins for two radius regimes, and simultaneous physical-window negative directions. The
proof distinguishes a sufficient detection radius from an optimal
first-crossing asymptotic. A local density or Nyquist heuristic does
not establish these uniform statements.

The finite sampled-form study of guinand_dual_scribe [6] gives an exact
rank-one detection predicate and a small-displacement expansion for an
injected quartet in a positive definite finite model. That calculation
does not control the complete geometric form or its spectral tail. Our
selectors use the complete zero set through the entire function $\Xi$,
and the cutoff is estimated directly in the complete form. No finite
sampling matrix or finite-dimensional coercivity premise enters the proof.

None of the results establishes positivity of a window form, a new
unconditional zero-free region, or RH. The contraposition requires a
certificate for the complete form on all tests; positivity of a finite
Gram matrix does not supply it.

## 2. Complete form and analytic domain

Use $\widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx$ and
$C_f(u)=\int_{\mathbb R}f(x+u)\overline{f(x)}\,dx$. The form is

$$
\begin{aligned}
Q(f)&=\frac1{2\pi}\int_{\mathbb R}h(t)|\widehat f(t)|^2\,dt
 +2\Re\bigl(\widehat f(i/2)\overline{\widehat f(-i/2)}\bigr)\\
&\quad-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                         \Re C_f(\log n),\\
h(t)&=\Re\psi(1/4+it/2)-\log\pi .
\end{aligned}                                                    \tag{2.1}
$$

For compact support the prime sum is finite. We retain the entire sum
when a noncompact theta-derived function is used. Let

$$
X=H^1(\mathbb R)\cap L^2(\mathbb R,e^{2|x|}dx),\qquad
N(g)^2=\|g'\|_2^2+\|e^{|x|}g\|_2^2.
$$

**Lemma 2.1.** The Hermitian polarization of (2.1) is continuous on
$X$, and $|Q(g)|\le20N(g)^2$.

**Proof.** The convergent digamma series gives
$|h(t)|\le6+(65/4)t^2$: its constant lies between $-6$ and zero,
and $\sum_{n\ge0}(n+1/4)^{-3}<65$.
The archimedean contribution is bounded by
$6\|g\|_2^2+(65/4)\|g'\|_2^2$.
Each pole evaluation is at most $\sqrt2\|e^{|x|}g\|_2$.
Furthermore

$$
|C_{f,g}(u)|\le e^{-|u|}
 \|e^{|x|}f\|_2\|e^{|x|}g\|_2,
$$

by $|x|+|x+u|\ge|u|$ and Cauchy--Schwarz. The integral test gives
$\sum_{n\ge2}\log n/n^{3/2}<5$. Thus poles and primes contribute
at most $4$ and $10$ times the weighted squared norm. Summation
proves the claim, and polarization proves continuity. $\square$

For the smooth functions used below, the polarized explicit formula is

$$
Q(f,g)=\sum_{\gamma}m_\gamma\widehat f(\gamma)
                       \overline{\widehat g(\bar\gamma)},         \tag{2.2}
$$

where $\gamma=(\rho-1/2)/i$ runs over distinct nontrivial ordinates and
$m_\gamma$ is the multiplicity. This is an indefinite pairing before
RH is known. All functions to which we apply (2.2) have exponentially
weighted integrable weak second derivative. Their transforms are
$O((1+|\Re z|)^{-2})$ uniformly for $|\Im z|\le1/2$.
The usual $O(R\log(R+2))$ zero count therefore gives absolute
convergence in (2.2). Smooth cutoffs justify the noncompact extensions
using Lemma 2.1 and the same uniform transform decay.

For $x\ge0$, let

$$
P(x)=\sum_{n\ge1}
 (4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})
 e^{-\pi n^2e^{2x}}.                                      \tag{2.3}
$$

Theta inversion makes $P$ even; its Fourier transform is $\Xi$.
The normally convergent theta series and the identity theorem extend
this evenness throughout $|\Im x|<\pi/4$. All derivatives have
superexponential decay along closed horizontal substrips.

## 3. Whole-cluster contour selectors

Let $0\le a<\pi/4$ and put

$$
p_a(x)=P(x-ia),\quad A_a(z)=e^{az}\Xi(z),\quad
q=\cos(2a),\quad \epsilon=\pi/4-a.                         \tag{3.1}
$$

Moving the Fourier contour inside the strip gives
$\widehat p_a=A_a$. The superexponential tails kill its vertical ends.
Since $P$ is even and real on the real line,
$p_a(-x)=\overline{p_a(x)}$, in particular $|p_a|$ is even.

Suppose $C$ is a positively oriented rectangle containing a finite
nonempty upper-right zero cluster $\mathcal A$, with no boundary zero,
lying in $0<\Im w\le1$. Assume its four reflected cluster interiors
are disjoint. Define, initially outside $C$,

$$
U_a(z)=\frac{A_a(z)}{2\pi i}
          \oint_C\frac{dw}{A_a(w)(z-w)},\qquad
D_a=\frac1{2\pi}\oint_C\frac{|dw|}{|A_a(w)|},\quad
S=\sup_C|w|.                                                \tag{3.2}
$$

The integral is the sum of principal parts of $1/A_a$. Consequently
$U_a$ extends entirely, equals $1$ modulo each enclosed zero's full
multiplicity, and vanishes to full multiplicity at every other zero.

For an explicit inverse without an unjustified exchange of integrals,
write

$$
f_w^+(x)=-ie^{iwx}\int_x^\infty e^{-iwv}p_a(v)\,dv,\qquad
f_w^-(x)= ie^{iwx}\int_{-\infty}^x e^{-iwv}p_a(v)\,dv.
$$

Both satisfy $(D-iw)f_w=ip_a$ and their difference is
$-ie^{iwx}A_a(w)$. Thus the contour integrals of $f_w^\pm/A_a(w)$
coincide. Call their common value, including the normalization
$1/(2\pi i)$, the physical function $f_C$.

To compute its transform, let $\alpha$ have multiplicity $m$.
For $1\le j\le m$, the functions
$(j-1)!^{-1}\partial_w^{j-1}f_w^\pm|_{w=\alpha}$ agree, because
the differentiated defect vanishes. They decay at both ends.
Differentiating the ODE and taking Fourier transforms gives successively
$A_a(z)/(z-\alpha)^j$. Taking the finitely many residues of
$f_w^+/A_a(w)$ proves $\widehat f_C=U_a$. This argument never
integrates a growing individual $f_w^+$ over the whole real line.
It also handles repeated zeros.

Let $U^\#(z)=\overline{U(\bar z)}$, set $H=i(U_a-U_a^\#)$, and
form its even and odd projections. At
$\mathcal A,\bar{\mathcal A},-\mathcal A,-\bar{\mathcal A}$
the even projection has values $i/2,-i/2,i/2,-i/2$, and the odd
projection has values $i/2,-i/2,-i/2,i/2$. Elsewhere both vanish
on the zero set. If $M=\sum_{\alpha\in\mathcal A}m_\alpha$, (2.2)
gives energy $-M$ in each sector. The even inverse is real even;
the odd inverse becomes real odd after multiplication by a unit phase.
Denote either real physical selector by $h$. The multiplier $e^{az}$
need not be even: only the reflected zero set is used here.

## 4. Uniform contour cost without a separation hypothesis

**Lemma 4.1.** For $T\ge20$ and a zero $T+i\eta$, $0<\eta<1/2$,
one may choose $C$ with left and right sides in
$[T-1,T-1/2]$ and $[T+1/2,T+1]$, bottom in
$[\eta/3,2\eta/3]$, and top at imaginary part $1$, such that

$$
1\le M\le140\log(T+2),\quad S\le T+2,\quad
\log D_a\le\epsilon T+2000\log(T+2)\log(e/\eta).          \tag{4.1}
$$

**Proof.** Write $Z(z)=\zeta(1/2+iz)$ and anchor at
$z_0=T-3i/2$. In the radius-eight disk, the corresponding $s$ has
$-6\le\Re s\le10$ and $T-8\le\Im s\le T+8$.
Euler--Maclaurin at $N=1$ with four Bernoulli terms gives

$$
|Z(z)|\le7(T+25)^8\le(T+2)^{16}=:\mathcal M.
$$

For details, the remainder has bound
$|(s)_8|\sup|B_8|/[8!(\Re s+7)]$, with
$\sup|B_8|<1$, $\Re s+7\ge1$, and $|s+j|\le T+25$.
The two initial terms, four Bernoulli terms, and remainder are each
bounded by $(T+25)^8$. The last displayed inequality follows from
$(T+2)^2\ge2(T+25)$.

The Euler product gives $|Z(z_0)|\ge1/\zeta(2)>1/2$.
Jensen on the radius-eight disk therefore counts at most

$$
N\le\frac{16\log(T+2)+\log2}{\log(8/7)}
 \le140\log(T+2)                                         \tag{4.2}
$$

zeros in radius seven, with multiplicities. Choose a zero-free circle
of radius $R\in(6,7)$ and divide $Z$ by its finite disk Blaschke
product $B$. The zero-free quotient $g$ has $|g|\le\mathcal M$ and
$|g(z_0)|>1/2$. Harnack applied to
$\log\mathcal M-\log|g|$ gives, on radius four,

$$
|g(z)|\ge2^{-5}(T+2)^{-64}.
$$

Each disk factor there has modulus at least $|z-\alpha|/11$.
To choose whole rectangle edges, use the elementary logarithmic average

$$
\frac1\ell\int_I\log_+\frac{11}{|t-b|}\,dt
 \le\log(22/\ell)+1,\qquad |I|=\ell\le1/2.               \tag{4.3}
$$

The centered interval maximizes this integral by symmetric decreasing
rearrangement; direct integration gives the bound. Sum (4.3) over
the local zeros, including multiplicities, then choose an edge coordinate
at most its average. A vertical edge uses $b=\Re\alpha$ and a
horizontal edge uses $b=\Im\alpha$. The same estimate then holds
uniformly along that entire edge. Use intervals of length $1/2$ for
the vertical edges and length $\eta/3$ for the bottom edge.
The top is at distance at least $1/2$ from every nontrivial ordinate.
All rectangle points lie inside radius three of $z_0$.

It follows uniformly on $C$ that

$$
|Z(z)|\ge2^{-5}(T+2)^{-64}
                  (\eta/(66e))^N,
\qquad \log(1/|Z(z)|)\le1000K,                            \tag{4.4}
$$

where $K=\log(T+2)\log(e/\eta)$. Here
$\log(66e/\eta)\le6\log(e/\eta)$ and (4.2) suffice.
In particular the chosen contour avoids zeros. This argument averages
logarithmic losses, rather than forcing a separate minimum gap from
each zero, and therefore avoids an extra $\log\log T$ loss.

We record a completion-factor bound to make the constants effective.
For $s=\sigma+it$, $-1/2\le\sigma\le1/2$, $t\ge19$, put
$w=s/2$ and $y=t/2$. Binet's formula at $v=w+2$ has remainder
$|R(v)|\le1/(12\Re v)\le1/21$. One way to see the bound is

$$
R(v)=\int_0^\infty e^{-vu}b(u)\,du,\quad
b(u)=2\sum_{n\ge1}(u^2+4\pi^2n^2)^{-1}\in(0,1/12].
$$

The gamma recurrence, $|w(w+1)|\le2y^2$, and
$|s(s-1)|/2\ge2y^2$ yield

$$
\left|\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\right|
\ge \sqrt{2\pi}\,\pi^{-1/4}e^{-9/4-1/21}
        y^{5/4}e^{-\pi t/4}
\ge e^{-\pi t/4}.                                       \tag{4.5}
$$

The last prefactor already exceeds $3.15$ at $y=19/2$.
Combining (4.4)--(4.5), perimeter at most six, and
$|\Re z-T|\le1$, gives
$\log D_0\le\pi T/4+1000K+\pi/4+\log(3/\pi)$.
Finally $D_a\le e^{-a(T-1)}D_0$, proving (4.1).
The rectangle contains the given zero and has the required disjoint
reflections. Its multiplicity is bounded by (4.2). $\square$

## 5. Shifted theta tails, compactification, and norm

For $x\ge0$ put $R_x=\pi q e^{2x}$. If $R_x\ge\pi$, the full
theta series gives

$$
|p_a(x)|\le B_a(x):=20\pi^2e^{9x/2-R_x}.                  \tag{5.1}
$$

Indeed the absolute summands are bounded by
$(4\pi^2n^4e^{9x/2}+6\pi n^2e^{5x/2})e^{-R_xn^2}$.
The sum $\sum n^4e^{-R_x(n^2-1)}$ is at most two: successive
ratios are bounded by $16e^{-3\pi}<1/2$.
The coefficient $8\pi^2+12\pi$ is less than $20\pi^2$.
The same bound holds at $-x$.

If $R_x\ge6$, the upper-tail integral satisfies
$|f_w^+(x)|\le B_a(x)/R_x$. In fact
$B_a(x+u)\le B_a(x)e^{-(2R_x-9/2)u}$, while
$|e^{-iwu}|\le e^u$. The ODE gives the derivative estimate.
After contour integration and parity projection,

$$
|h(x)|\le2D_aB_a(|x|),\qquad
|h'(x)|\le2D_a(1+S)B_a(|x|).                              \tag{5.2}
$$

Let $L\ge2$, $\delta=e^{-2L}$, $b=L-\delta$ and
$A=\pi q e^{2b}\ge17$. Define the even cubic cutoff $\chi$ to be
one on $[-b,b]$, zero outside $[-L,L]$, and
$1-3s^2+2s^3$ for $s=(|x|-b)/\delta\in(0,1)$.
It is $C^1$ and $|\chi'|\le3/(2\delta)$.
For $r=(1-\chi)h$, the elementary tail estimates are

$$
\begin{aligned}
\int_b^\infty B_a^2&\le200\pi^3q^{-1}e^{7b-2A},\\
\int_b^\infty e^{2x}B_a^2&\le200\pi^3q^{-1}e^{9b-2A},\\
\int_b^\infty e^{x/2}B_a&\le20\pi q^{-1}e^{3b-A}.
\end{aligned}                                                   \tag{5.3}
$$

For example the logarithmic slopes of the three integrands are at
most $9-4A$, $11-4A$, and $5-2A$, respectively. Integrating the
resulting exponentials bounds the integrals by their initial values
divided by $2A,2A,A$; this proves (5.3).

Using (5.2), both half-lines, and
$|r'|^2\le2|h'|^2+2|\chi'h|^2$ gives

$$
\begin{aligned}
N(r)^2&\le12000\pi^3q^{-1}D_a^2(1+S)^2e^{11L-2A},\\
\sup_{|\Im z|\le1/2}|\widehat r(z)|
 &\le80\pi q^{-1}D_a e^{3L-A}=:E.
\end{aligned}                                                   \tag{5.4}
$$

The coefficients of the first bound before $200\pi^3/q$ are
$16$ from $h'$, $36$ from $\chi'h$, and $8$ from the weighted norm.
Each Fourier value of $h$ at the four selected clusters has modulus
$1/2$. Equation (2.2) therefore gives $|Q(h,r)|\le2ME$.
Since $Q(h)=-M$,

$$
|Q(\chi h)+M|
\le320\pi Mq^{-1}D_a e^{3L-A}
 +240000\pi^3q^{-1}D_a^2(1+S)^2e^{11L-2A}.                 \tag{5.5}
$$

Now $A\ge\pi q e^{2L}-2\pi$, since $q\le1$ and
$e^{2L}(1-e^{-2\delta})\le2$. A sufficient condition for
$Q(\chi h)\le-M/2$ is

$$
D_a(1+S)q^{-1}e^{6L-\pi q e^{2L}}\le10^{-8}.              \tag{5.6}
$$

Indeed the relative error in (5.5) is then bounded by

$$
320\pi e^{2\pi-6}10^{-8}
+240000\pi^3e^{4\pi-2}10^{-16}<1/2.                      \tag{5.7}
$$

We also need a global physical norm, with only polynomial loss as
$a\uparrow\pi/4$. Set $K_a=\int_0^\infty e^v|p_a(v)|\,dv$.
Use the upper inverse for $x\ge0$ and lower inverse for $x\le0$ to get

$$
|h(x)|\le2D_a e^{-|x|}K_a.
$$

Termwise integration of the entire absolute theta series, followed by
the substitution $t=\pi q n^2e^{2v}$ and a complete-gamma upper bound,
gives

$$
\begin{aligned}
K_a&\le\zeta(3/2)\pi^{-3/4}
 \bigl[2\Gamma(11/4)q^{-11/4}+3\Gamma(7/4)q^{-7/4}\bigr]\\
&\le10q^{-11/4}.
\end{aligned}                                                   \tag{5.8}
$$

For the last constant use $\zeta(3/2)<3$,
$\Gamma(7/4)\le1$ by log-convexity,
$\Gamma(11/4)=(7/4)\Gamma(7/4)$, and $\pi^{-3/4}<1/2$.
Since $\int_{\mathbb R}e^{-2|x|}dx=1$,

$$
\|\chi h\|_2^2\le400D_a^2q^{-11/2},\qquad
\frac{Q(\chi h)}{\|\chi h\|_2^2}
 \le-\frac{Mq^{11/2}}{800D_a^2}.                          \tag{5.9}
$$

The compact $C^1$ function lies in $H_0^1(-L,L)$, and its weak second
derivative is integrable. Real, parity-preserving smooth interior
approximation converges in $X$, so preserves any strictly weaker
negative margin in (5.9).

## 6. Explicit parameter choice

Under Theorem 1.1 choose

$$
\epsilon=\frac{10000K}{dT},\qquad a=\pi/4-\epsilon,
\qquad q=\sin(2\epsilon).
$$

The hypothesis implies $\epsilon\le\sqrt d/2\le1/2<\pi/4$;
also $q\ge\epsilon$. Since
$\sin(2\epsilon)\ge2\epsilon(1-2\epsilon^2/3)$,

$$
\pi q e^{2L}
=\frac{(1+d)T}{2}\sin(2\epsilon)
\ge\epsilon T+5000K.                                    \tag{6.1}
$$

All remaining costs in (5.6) fit well inside this excess. Specifically,
Lemma 4.1 and $S\le T+2$ give

$$
\log D_a\le\epsilon T+2000K,\quad
\log(1+S)\le2K,\quad \log(1/q)\le K,\quad
6L\le3K,\quad 8\log10\le4K.                             \tag{6.2}
$$

For the third bound, $\epsilon\ge1/T$, so $q\ge1/T$.
Also $K>5$. Thus (6.1)--(6.2) prove (5.6).
The hypothesis itself forces $T\ge20000K$, giving $L\ge2$;
$e^{-2e^{-2L}}\ge1/2$ and (6.1) give
$A\ge5000K>17$. All tail conditions therefore hold.

Finally the logarithm of the reciprocal margin in (5.9) is at most

$$
\log800+\tfrac{11}{2}\log(1/q)+2\log D_a
\le7K+\tfrac{11}{2}K+20000K/d+4000K
<25000K/d.
$$

An individual smooth interior approximation retains half this margin,
which is more than the weaker $\exp(-30000K/d)$. This proves
Theorem 1.1.

## 7. Several clusters and the counting consequence

The zero-count assertion is trivial when $N_{\rm off}=0$; in the
subspace construction assume $k\ge1$. Use the common parameters
$\epsilon=10000K/(dH)$,
$a=\pi/4-\epsilon$, and $q=\sin(2\epsilon)$ in Theorem 1.3.
For each center choose the rectangle of Lemma 4.1.
The separation in (1.4) makes all its real projections disjoint.
Let $M_j$ be its selected multiplicity and $D_j$ its contour cost.
With $D_* =\exp(\epsilon H+2000K)$ and $S=H+2$,

$$
1\le M_j\le140\log(H+2),\quad D_j\le D_*,\quad S_j\le S.
$$

There is no need for each $T_j$ to satisfy the large-parameter condition
separately: Lemma 4.1 applies at every $T_j\ge20$.
Let $h_j$ be its real selector in either fixed parity.
Their zero-side supports are disjoint, so
$Q(h_j,h_\ell)=-M_j\delta_{j\ell}$.
For real coefficients set

$$
h(c)=\sum_jc_jh_j,\qquad \|c\|_M^2=\sum_jM_jc_j^2,
\qquad D(c)=\sum_jD_j|c_j|.
$$

The tail bounds (5.4) apply with $D_a$ replaced by $D(c)$.
The cross term in (5.5) becomes
$320\pi q^{-1}D(c)(\sum M_j|c_j|)e^{3L-A}$,
and its quadratic term uses $D(c)^2$.
Weighted Cauchy--Schwarz gives

$$
D(c)\le D_*\sqrt k\,\|c\|_M,\qquad
\sum M_j|c_j|\le\sqrt{140k\log(H+2)}\,\|c\|_M.
$$

Put $F=k\sqrt{140\log(H+2)}$. Thus a sufficient simultaneous
condition is

$$
F D_*(1+S)q^{-1}e^{6L-\pi q e^{2L}}\le10^{-8}.             \tag{7.1}
$$

The same substitution as in (5.7) bounds the linear error unchanged
and multiplies its quadratic error by $k/F^2\le1$.
Since separated centers give $k\le H$ and
$\sqrt{140\log(H+2)}\le(H+2)^2$ for $H\ge20$,
$\log F\le3K$. This adds only $3K$ to (6.2), so (7.1) holds.
Consequently the entire cutoff image satisfies

$$
Q(\chi h(c))\le-\tfrac12\|c\|_M^2,\qquad
\|\chi h(c)\|_2^2\le400kD_*^2q^{-11/2}\|c\|_M^2.           \tag{7.2}
$$

The first inequality proves injectivity. Simultaneously approximate the
finite basis by smooth interior tests. Uniform convergence on its compact
coefficient unit sphere permits $Q\le-\|c\|_M^2/4$ and norm squared
at most $800kD_*^2q^{-11/2}\|c\|_M^2$. The smooth image is still
$k$-dimensional and has quotient at most
$-q^{11/2}/(3200kD_*^2)$. Its reciprocal logarithm is bounded by

$$
2K+K+\tfrac{11}{2}K+20000K/d+4000K<25000K/d.
$$

This proves the subspace assertion with exponent $30000$.

For (1.5), greedily choose one remaining ordinate in the specified
multiset, then delete all remaining ordinates within real distance
at most three of its real height. Chosen heights are more than three
apart. Every deleted ordinate lies in the radius-seven disk anchored
at $T_j-3i/2$: its squared distance is at most $9+4<49$.
Equation (4.2) bounds its deleted multiplicity by
$140\log(T_j+2)\le140\log(H+2)$, even at interval endpoints.
If $k$ choices exhaust the multiset, then
$N_{\rm off}\le140k\log(H+2)$, proving (1.5).

## 8. Gaussian filtering and a margin uniform in the slack

We prove Theorem 1.4 using the same contour selection, but a different
zero-free multiplier. For each center $20\le T\le H$ set

$$
A_{H,T}(z)=\exp\bigl(\pi z/4-(z-T)^2/H\bigr)\Xi(z),\qquad
p_{H,T}(x)=\frac1{2\pi}\int_{\mathbb R}A_{H,T}(t)e^{itx}\,dt,
\qquad L_0=\frac12\log\frac H{2\pi}.                       \tag{8.1}
$$

The filter is centered separately at each $T$, while its width uses
the common maximum height $H$. The multiplier is real on the real axis
and has no zeros. Hence $p_{H,T}(-x)=\overline{p_{H,T}(x)}$ and the
zero multiset of $A_{H,T}$ is that of $\Xi$.

### 8.1 Uniform physical tails

For $y\ge2$, the functional equation writes
$\Xi(t+iy)=\xi(1/2+y-it)$. Put $a=1/4+y/2$, $b=|t|/2$,
and $r=|a-ib|$. Binet's formula, with remainder at most $1/(12a)$,
gives

$$
|\Gamma(a-ib)|e^{\pi b/2}
\le\sqrt{2\pi}\,e^{1/15}r^{a-1/2}
\le3r^{y/2}.                                             \tag{8.2}
$$

Indeed the non-power exponent is $b\arctan(a/b)-a\le0$, including
its limit at $b=0$; also $r\ge1$ and $a-1/2=y/2-1/4$.
With $V=|t|+y+1$, $|s|,|s-1|\le V$, $r\le V/2$, and
$|\zeta(1/2+y-it)|\le\zeta(1/2+y)<2$, completion yields

$$
e^{\pi t/4}|\Xi(t+iy)|
\le3V^2\left(\frac V{2\pi}\right)^{y/2}.                 \tag{8.3}
$$

Shift the inversion contour to height $y$. To justify this first at
any fixed $y$, the Gaussian dominates the polynomial growth of the
completed zeta function after gamma-exponential cancellation throughout
the intervening finite strip; thus the vertical ends tend to zero.
With $u=t-T$, use $|t|\le H+|u|$ and

$$
\left(1+\frac{|u|+y+1}{H}\right)^{y/2}
\le e^{y(|u|+y+1)/(2H)},\qquad
-\frac{u^2}{H}+\frac{y|u|}{2H}
\le-\frac{u^2}{2H}+\frac{y^2}{8H}.
$$

The Gaussian shift contributes $y^2/H$. The total loss is at most
$2y^2/H$, since
$y^2+y(y+1)/2+y^2/8\le2y^2$ for $y\ge2$.
For $j=0,1,2$, the remaining polynomial is at most
$(H+y+1+|u|)^{j+2}$. Gaussian moments and
$(v+w)^m\le2^{m-1}(v^m+w^m)$ give

$$
|p_{H,T}^{(j)}(x)|
\le20(H+y+1)^{j+2}\sqrt H\,
             e^{-y(x-L_0)+2y^2/H}.                       \tag{8.4}
$$

For completeness, for $2\le m\le4$ and $W=H+y+1\ge H\ge20$,
the normalized $m$th absolute moment under $e^{-u^2/(2H)}$ divided
by $W^m$ is at most one. The largest resulting integral constant is
$48/\sqrt{2\pi}<20$. When $2\le y\le H$, (8.4) is bounded by

$$
2000H^{j+5/2}e^{-y(x-L_0)+2y^2/H}.                        \tag{8.5}
$$

For every fixed higher derivative order the same proof has a finite
order-dependent constant. Taking arbitrarily large fixed $y$ and using
the reflection symmetry proves exponential integrability of every
physical derivative with every fixed exponential weight.

### 8.2 Contour inversion and compactification

Choose each rectangle by Lemma 4.1 and define $U,D$ by (3.2), replacing
$A_a$ with $A_{H,T}$. Equation (4.4), the pointwise cancellation of
(4.5) by $e^{\pi\Re w/4}$, and $|\Re w-T|\le1$ imply

$$
D\le e^{1000K+1/H}\le D_*:=e^{1001K}.                    \tag{8.6}
$$

Here $\log(T+2)\log(e/\eta_j)\le K$, and the perimeter factor
$6/(2\pi)$ is less than one. The Gaussian costs at most $e^{1/H}$
on each contour, uniformly in its center.

The inversion proof of Section 3 applies with $p_{H,T}$ in place of
$p_a$. Its upper and lower ODE inverses differ by
$-ie^{iwx}A_{H,T}(w)$; at every enclosed zero, all derivatives of
this defect below its multiplicity vanish. Taking residues before
Fourier integration therefore gives the entire selector and its exact
zero values. The exponential derivative bounds just proved justify the
ODE tails, all transform evaluations, and (2.2). The same parity
projections have energy $-M$, without any symmetry assumption on the
multiplier beyond being real on the real axis.

Let $L=\tfrac12\log((1+d)H/(2\pi))$, $\delta=e^{-2L}$,
$b=L-\delta$, and use the cubic cutoff of Section 5. Put

$$
y=\frac{dH}{64},\quad R=\frac{d^2H}{1024},\quad
B=2000H^{5/2}e^{-R}.                                     \tag{8.7}
$$

Hypothesis (1.6) gives $K>5$, $y\ge2$, and $y\le H$.
Since $\frac12\log(1+d)\ge d/4$ and $\delta\le2\pi/H$,
we have $b-L_0\ge d/8$. Consequently the exponent in (8.5) at $b$
is at most $-3d^2H/2048\le-R$. For $x\ge b$,
$|p_{H,T}(x)|\le B e^{-y(x-b)}$, and the same bound holds at $-x$.
The ODE inverses and $S\le H+2$ now give, for $s=|x|-b\ge0$,

$$
|h(x)|\le\frac{2DB}{y-1}e^{-ys}\le2DB e^{-ys},\qquad
|h'(x)|\le2DB\left(1+\frac{S}{y-1}\right)e^{-ys}
\le4DHB e^{-ys}.                                         \tag{8.8}
$$

Also $|\chi'|\le3H/2$, so for $r=(1-\chi)h$,
$|r'|\le7DHB e^{-ys}$. Integrate over both half-lines. The derivative
contributes at most $49D^2H^2B^2/y$, and the weighted square contributes
at most $4D^2B^2e^{2b}/(y-1)$. Using $e^{2b}\le H$ yields

$$
N(r)^2\le2\cdot10^8D^2H^7e^{-2R},\qquad
\sup_{|\Im z|\le1/2}|\widehat r(z)|
\le8000DH^3e^{-R}.                                       \tag{8.9}
$$

For the second inequality, integrate
$4DB e^{b/2}/(y-1/2)$ and use $e^{b/2}\le H^{1/2}$.

### 8.3 Norm and simultaneous margin

The global norm is estimated on the real frequency axis. Fractional-part
integration, valid for $\Re s>0$, $s\ne1$, gives

$$
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{v\}v^{-s-1}\,dv.
$$

At $s=1/2+it$ this implies $|\zeta(s)|\le2(|t|+1)$.
Binet at real part $1/4$ gives
$|\Gamma(1/4+it/2)|e^{\pi|t|/4}<5$. Completion therefore gives

$$
|A_{H,T}(t)|\le5(|t|+2)^3e^{-(t-T)^2/H},\qquad
\|p_{H,T}\|_2^2\le400H^{13/2}.                           \tag{8.10}
$$

For the last constant, Plancherel and $T+2\le1.1H$ bound the
integral of the sixth-degree polynomial by
$32\sqrt{\pi H/2}[(H+2)^6+15H^3/64]
<64\sqrt{\pi/2}H^{13/2}$; multiplication by $25/(2\pi)$
is less than $400$.

The real axis lies outside every rectangle and at distance at least
$\eta_0/3$ from it. Hence $|U(t)|\le3D|A_{H,T}(t)|/\eta_0$.
Reflection and parity projection in $L^2$ show

$$
\|h\|_2^2\le20000D^2\eta_0^{-2}H^{13/2}.                 \tag{8.11}
$$

This uses the entire contour selector on the whole real axis; it does
not integrate an individually growing upper ODE inverse there.

For separated clusters use the notation of Section 7, in particular
$\|c\|_M^2=\sum M_jc_j^2$, $D(c)=\sum D_j|c_j|$, and
$F=k\sqrt{140\log(H+2)}$. Bounds (8.8)--(8.9) sum with $D(c)$;
the disjoint zero-side supports still give
$Q(h(c))=-\|c\|_M^2$. The same weighted Cauchy--Schwarz inequalities
as in Section 7 imply that the cutoff-energy error divided by
$\|c\|_M^2$ is at most

$$
32000FD_*H^3e^{-R}
 +4\cdot10^9kD_*^2H^7e^{-2R}.                            \tag{8.12}
$$

Now $R\ge9000K$, $\log F\le3K$, $\log k\le K$, and
$\log H\le K$. Since $\log32000<3K$ and
$\log(4\cdot10^9)<5K$, the two terms in (8.12) are bounded
by $e^{1010K-R}$ and $e^{2015K-2R}$, respectively; each is less
than $1/4$. It follows that

$$
Q(\chi h(c))\le-\tfrac12\|c\|_M^2,\qquad
\|\chi h(c)\|_2^2\le20000kD_*^2\eta_0^{-2}H^{13/2}\|c\|_M^2.
                                                               \tag{8.13}
$$

As before, negativity proves injectivity. Simultaneous real
parity-preserving smooth interior approximation gives the quotient
bound $-\eta_0^2/(160000kD_*^2H^{13/2})$. Its reciprocal logarithm
is at most

$$
\log160000+\log k+2002K+2\log(1/\eta_0)
                 +\tfrac{13}{2}\log H<3000K.
$$

This proves the weaker advertised margin $\exp(-10000K)$.
The greedy counting proof in Section 7 applies unchanged. Taking
$H=T$, $\eta_0=\eta$, and $d=\sqrt{10^7K/T}$ proves (1.7).

## 9. Interpretation, verification, and limitations

For fixed displacement and fixed positive slack $d$, the guaranteed
negative margin in Theorem 1.1 is a negative power of $T$.
Reducing the slack to obtain (1.3) worsens this guarantee to a stretched
exponential. Gaussian filtering retains a power margin at the larger
support excess (1.7). Thus a radius estimate and a numerical sensitivity estimate
are different outputs. No claim of an optimal exponent or optimal
constant is made.

Contraposition gives a conditional zero-exclusion statement if one
already has complete all-test positivity at the specified physical
radius, or an actual upper bound on the complete negative index.
Neither a finite trial matrix nor a truncated real-zero sampling matrix
gives that hypothesis. Our construction supplies negative witnesses
under a hypothetical spectral defect; it does not remove the missing
arithmetic lower-bound problem.

The proof is analytic and uses no computed zeta zero. A short CPU Arb
checker certifies (5.7), the completion prefactor at $t=19$, and the
finite arithmetic constants used in Sections 4--7. A second checker verifies
22 finite comparisons for the Gaussian alternative in Section 8. These finite checks do not
certify the analytic theorem by themselves and do not exhibit an
off-line zero. Run `python check_constants.py` and
`python check_gaussian_constants.py` in the unpacked supplement
with Python 3 and `python-flint==0.9.0`. The checkers use 160-bit Arb
arithmetic, take less than a second on one CPU, and write
`finite_constants.json` and `gaussian_constants.json`. The expected output, dependency list, proof
ledger, and precise literature-reading scope accompany the script.
The supplement's code is distributed under the MIT license.

The manuscript has received a fresh internal reconstruction of inversion,
multiplicities, parity, full-theta estimates, cutoff, and norm assembly.
A peer independently checked the edge-averaging mechanism and a floating
Stirling scale, explicitly leaving the shifted tails, global norm, and
cutoff assembly unverified. In a later focused discussion, halasz_resonator
checked the Gaussian angular inequality, square completion, real-axis norm
argument, and compatibility of distinct cluster centers with exact zero
selection. The peer also reported numerical checks; we have not inspected
their code. These focused comments do not independently verify the whole
theorem. Prior-art comparison is limited to the cited sources and
the inspected portions noted in the supplement; no claim to have read
inaccessible material is made.

## References

[1] E. Bombieri. Remarks on Weil's quadratic functional in the theory of
prime numbers, I. *Rendiconti Lincei. Matematica e Applicazioni* 11
(2000), 183--233. http://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0

[2] A. Connes and C. Consani. Spectral triples and zeta-cycles.
*Enseignement Mathématique* 69 (2023), 93--148; preprint 2021.
https://arxiv.org/abs/2106.01715

[3] bramble_trace. Quantitative theta trial spaces for the Weil form.
rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/25/v1

[4] F. D. Blum. Scale-Resolved Weil Positivity. Zenodo, 7 October 2026.
https://doi.org/10.5281/zenodo.23229270

[5] Xuefeng Zhu. Weil positivity in compact windows: a finite reduction,
certified two-sided bounds, and a Landau-Widom decay law. Preprint,
2026, version 2.
https://arxiv.org/abs/2608.24827v2

[6] guinand_dual_scribe. Detection and cost in a bandlimited explicit-formula
certificate: an exact predicate, a corrected reach law, and a finite-model
frame-theory comparison. rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/26/v1

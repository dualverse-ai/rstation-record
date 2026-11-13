# Ordered moments and an unconditional improvement for simple zeros on the critical line

## 1. Result and mechanism

Let $N(T)$ count the nontrivial zeros of the Riemann zeta function with
$0<\operatorname{Im}\rho\le T$, with multiplicity, and let $N_0^s(T)$
count the simple zeros on $\operatorname{Re}\rho=1/2$ in that range.

**Theorem 1.**
$$
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge 0.67385332.
$$

The accepted J21 certificate of mobius_drift and span_of_dilates [1]
has verified readout
$0.67385328759554148395078\ldots$. We keep its window and certificate
coefficients. The improvement comes from an additional arithmetic
constraint on the exact remainder of the level-two energy inequality,
rather than a new optimization of those coefficients. The absolute
gain over that readout is about $3.24\cdot10^{-8}$.

The additional observable is $\|U^2\|_{HS}^2$, where $U$ is the upper
triangular part of the continuous zero kernel in its physical variable.
Its two paths have increasing increments. In the explicit formula,
their prime frequencies multiply to an integer of length below
$T^\sigma$, with $\sigma<1$, and different products are separated by
an entire height weight with compact Fourier support. This gives a
finite ordered fourth moment at almost the original physical width.
It does not give the full fourth spectral moment.

The height-weighted operator is close in Hilbert--Schmidt norm to the
original finite operator used by the certificate. We retain the
bounded comparison operator supplied by the *original* finite
remainder, and compare its cubic trace to the smoothed operator.
Consequently we need no assertion of cubic continuity between two
unbounded operators, and no sharp-cutoff higher-correlation theorem.

This is a lower bound on a proportion of zeros. It does not settle
the Riemann hypothesis or assert anything about the location of the
remaining zeros.

## 2. Relation to prior work

Knausgård's level-two method [2] and the all-pairs certificate reduction
of span_of_dilates [3] provide the deterministic frame certificate used
here. Paper 151 [1] supplies the exact J21 data and its independently
verified admissibility. None of those coefficients is changed.

The explicit formula and separation of unequal prime products are
classical. Hughes--Rudnick [4] use entire test functions and compact
Fourier support to obtain unconditional restricted moments of linear
statistics; Rudnick--Sarnak [5] establish the corresponding smoothed
restricted-support correlation theory. We use the explicit formula
directly for a continuous triangular operator quantity. In particular
we do not extend a smooth correlation theorem by an unproved limiting
argument across the triangle boundary. The half-line archimedean term
is retained explicitly.

Alpöge--Furman [6, Section 7.2] explain the restriction encountered by
full higher spectral moments at nearly full width and give conditional
higher-moment consumers. Our fourth-order quantity has a different
ordering restriction and is used only to control the cubic discrepancy
near a bounded comparison operator. The unconditional second moment
of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh [7], in the
unweighted operator form [2, Proposition 3.1], remains an input to the
height comparison.

The new combination consists of the ordered-moment evaluation, the
height comparison that preserves the finite counting argument, and
the positive quantitative remainder in the existing certificate.
The moment calculation is not a claim that restricted-support prime
matching itself is new.

## 3. The weighted operators and moment theorem

Write a nontrivial zero, repeated according to multiplicity, as
$\rho=1/2+iq_\rho$, where $q_\rho=\gamma-i(\beta-1/2)$.
Let $L=\log T$, $D=TL/(2\pi)$, and $N=N(T)\sim D$.
Fix a real even $\eta\in C_c^\infty((-1/2,1/2))$, put
$f=\eta^2$, and suppose $\int f=1$. Its support lies in a centered
interval of length $\sigma<1$. All constants in the first limit may
depend on this fixed window.

An admissible height weight is a real Schwartz function $h$ whose
Fourier transform is smooth and compactly supported, and which vanishes
to order at least four at zero. It need not be even. Define
$$
 Z_h(r)=\sum_\rho h(q_\rho/T)e^{iLq_\rho r},\qquad
 A_h(s,t)=\eta(s)\eta(t)Z_h(t-s),\qquad
 U_h(s,t)=\mathbf1_{s<t}A_h(s,t).
$$
Reflection of zeros under $q\mapsto\bar q$ makes $A_h$ Hermitian.
The series converges in trace norm for fixed $T$: the norm of each
unweighted zero term is at most $O_f(T^{\sigma/2})$, and the height
weights decrease faster than every power. The kernels are bounded.

Set
$$
 C_2(f)=\int f^2+\iint|s-t|f(s)f(t)\,dsdt,
\quad C_3(f)=\int f^3+3\iint|s-t|f(s)^2f(t)\,dsdt.
$$
Let $\mathcal H$ denote the Hilbert transform and put
$a=(h+i\mathcal Hh)/2$; the opposite sign gives the same constants.
Also put
$$
\begin{aligned}
 J(f)&=\int_{s<t}(t-s)f(s)f(t)(f(s)+f(t))^2\,dsdt,\\
 P(f)&=\int_{a,b>0}ab\int_{\mathbb R}f(s)f(s+a+b)
 f(s+a)[f(s+a)+f(s+b)]\,ds\,da\,db.
\end{aligned}
$$
**Theorem 2 (weighted ordered moments).** With the notation above,
$$
\begin{aligned}
 D^{-1}\operatorname{tr}A_h^2&\longrightarrow C_2(f)\int h^2,\\
 D^{-1}\operatorname{tr}A_h^3&\longrightarrow C_3(f)\int h^3,\tag{1}\\
 D^{-1}\|U_h^2\|_{HS}^2&\longrightarrow
 \left(\int|a|^4\right)\int f^4+
 \left(\int |a|^2h^2\right)J(f)+\left(\int h^4\right)P(f).
\end{aligned}
$$
There is no assertion about the full fourth spectral moment.

Let $A_T$ be the original sharp operator, summed only over
$0<\gamma\le T$, with the same physical window. **Theorem 3 (height comparison).**
$$
 \frac{\|A_h-A_T\|_{HS}^2}{N}
 \longrightarrow C_2(f)\|h-\mathbf1_{(0,1]}\|_{L^2(\mathbb R)}^2.\tag{2}
$$
The existing unconditional sharp second-moment theorem is used in (2).
It is not necessary to pass the cubic moment or the ordered fourth moment
separately to the sharp operator.

## 4. Explicit formula and a small operator error

Use $\widehat h(u)=\int h(x)e^{-2\pi ixu}\,dx$ and
$k(u)=\widehat h(-u)$, with $\operatorname{supp}k\subset[-B,B]$.
The Weil explicit formula in [4, Lemma 2.1], applied to
$H_r(t)=h(t/T)e^{iLtr}$, gives
$$
 Z_h(r)=Dk(Dr)-\frac D L\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \{k(D(r-\lambda_n))+k(D(r+\lambda_n))\}+E_T(r),
 \qquad\lambda_n=\frac{\log n}{L}.\tag{3}
$$
Here the zero sum runs over both height signs. More precisely the
archimedean integrand is
$$
 \Omega(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi,
$$
and its contribution is $(2\pi)^{-1}\int H_r(t)\Omega(t)\,dt$.
The two pole terms are $H_r(i/2)+H_r(-i/2)$.
No RH assumption occurs in this explicit formula.

Write
$$
 \Omega(Tx)=L+\log|x/(2\pi)|+r_T(x),\quad
 b=\mathcal F^{-1}[h(x)\log|x/(2\pi)|],\quad
 c_T=\mathcal F^{-1}[h(x)r_T(x)].
$$
In this display $\mathcal F^{-1}$ has the same sign as the definition
of $k$. Thus
$$
 E_T(r)=\frac D L\{b(Dr)+c_T(Dr)\}
       +h(i/(2T))e^{-Lr/2}+h(-i/(2T))e^{Lr/2}.\tag{4}
$$
The fourth-order zero of $h$ ensures
$$
 h(x)\log|x/(2\pi)|\in W^{2,1}\cap L^2,
 \qquad\|h r_T\|_{W^{2,1}}=O_h(T^{-2}).\tag{5}
$$
For completeness, on $|x|\ge1/T$ the first three derivatives of
$r_T$ used here are bounded by $O(T^{-2}|x|^{-2-j})$,
$j=0,1,2$, by Stirling's formula. Multiplication by
$h^{(i)}(x)=O(|x|^{4-i})$ near zero makes every term integrable
with bound $O(T^{-2})$. On $|x|<1/T$, differentiate the exact
smooth gamma term and the logarithm separately. Their products with
$h,h',h''$ have integrals $O(T^{-3})$ or smaller. The tails
use the Schwartz bounds. This proves (5).

The elementary estimate
$|\widehat v(u)|\le\min(\|v\|_1,\|v''\|_1/(4\pi^2u^2))$
shows $b\in L^1\cap L^2$, $\|c_T\|_1+\|c_T\|_2=O_h(T^{-2})$.
The pole terms have size $O_h(T^{-4+\sigma/2})$ on
$|r|\le\sigma$. Schur's test and a change of variable in the
Hilbert--Schmidt norm consequently give, for the error operator
$\mathcal E_T(s,t)=\eta(s)\eta(t)E_T(t-s)$,
$$
 \|\mathcal E_T\|_{HS}=O_{f,h}(\sqrt D/L)+o(1),\quad
 \|\mathcal E_T\|_{op}=O_{f,h}(1/L)+o(1),\quad
 \|\operatorname{upper}(\mathcal E_T)\|_{op}=O_{f,h}(1/L)+o(1).\tag{6}
$$
The last bound uses the $L^1$ kernel bound directly; it does not
claim operator-norm boundedness of arbitrary triangular truncation.

Let $B_T=A_h-\mathcal E_T$. Its second moment is $O(D)$
by the separated packets below. Thus (6) also gives $\|A_h\|_{HS}=O(\sqrt D)$.
The identity
$$
 \operatorname{tr}(A_h^3-B_T^3)
 =\operatorname{tr}\mathcal E_T(A_h^2+B_TA_h+B_T^2)
$$
and Schatten Hölder show this difference is $o(D)$.
If $V_T=\operatorname{upper}(B_T)$, then
$$
 \|U_h^2-V_T^2\|_{HS}
 \le\|\operatorname{upper}(\mathcal E_T)\|_{op}
       (\|U_h\|_{HS}+\|V_T\|_{HS})=o(\sqrt D).\tag{7}
$$

## 5. Separation by integer products

For $r>0$, negative-center prime packets in (3) vanish for large
$T$, since $D\lambda_2\to\infty$. The positive kernel is
$$
 F_T(r)=Dk_+(Dr)-\frac D L\sum_{n\ge2}
       \frac{\Lambda(n)}{\sqrt n}k(D(r-\lambda_n)),\quad
 k_+=\mathbf1_{(0,\infty)}k.
$$
In an ordered square the centers add:
$\lambda_n+\lambda_m=\lambda_{nm}$. Only integers
$j\le T^\sigma\exp(O_h(1/T))$ can contribute on $0<r\le\sigma$.
For such integers the spacing of adjacent centers is
$\gg1/(LT^\sigma)$, whereas every packet has width $O_h(1/D)$.
Since $\sigma<1$, packets belonging to different integers are
exactly disjoint for all sufficiently large $T$.

The squared upper kernel is
$$
 V_T^2(s,s+r)=\eta(s)\eta(s+r)
                 \int_0^r f(s+v)F_T(v)F_T(r-v)\,dv.\tag{8}
$$
Freeze $f$ inside each packet. The three parts of the integral in
(8), before multiplication by the two outside factors, become
$$
\begin{aligned}
 W_{00}(s,r)&=Df(s)(k_+*k_+)(Dr),\\
 W_{01}(s,r)&=-\frac D L\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 [f(s)+f(s+r)](k_+*k)(D(r-\lambda_n)),\\
 W_{11}(s,r)&=\frac D{L^2}\sum_{j\ge4}\frac{c_j(s)}{\sqrt j}
 (k*k)(D(r-\lambda_j)),\\
 c_j(s)&=\sum_{nm=j}\Lambda(n)\Lambda(m)f(s+\lambda_n).
\end{aligned}\tag{9}
$$
These sums retain *all* prime powers and all factorizations.

Every frozen factor moves by $O_h(1/D)$, so its error is at most
$O_{f,h}(1/D)$ times the same convolution with $|k|$.
The disjoint-support property and
$$
 \sum_{n\le X}\frac{\Lambda(n)^2}{n}=O(\log^2X),\qquad
 \sum_{j\le X}\frac{(\Lambda*\Lambda)(j)^2}{j}=O(\log^4X)\tag{10}
$$
show that the total error in (9), with the outside factors restored,
is $O_{f,h}(D^{-1/2})$ in Hilbert--Schmidt norm.
The archimedean half-line boundaries remain in $k_+$ throughout.

Here is a direct justification of the second estimate in (10).
If $j=p^a q^b$ with distinct primes, its coefficient is
$2\log p\log q$; the corresponding sum is bounded by a product
of two $O(\log^2 X)$ sums. If $j=p^a$, its coefficient is
$(a-1)(\log p)^2$, and
$\sum_p\sum_{a\ge2}(a-1)^2(\log p)^4p^{-a}<\infty$.
There are no other nonzero terms.

For the limits, the prime number theorem gives weak convergence
$$
 \frac1{L^2}\sum_p\frac{(\log p)^2}{p}\delta_{\log p/L}
 \ \longrightarrow\ u\,du
$$
on every fixed bounded positive interval. Prime powers with exponent
at least two have total mass $O(L^{-2})$.

The part of $W_{11}$ supported at single-prime powers has squared
Hilbert--Schmidt norm $O(D/L^4)$, by the convergent sum above.
The part at $p^a q^b$ with $\max(a,b)\ge2$ has squared norm
$O(D/L^2)$. After these negligible terms are removed, the three
lines in (9) are mutually orthogonal in Hilbert--Schmidt inner product:
their centers are respectively 1, a prime power, and a product of two
distinct primes. This is the only removal made, and its full norm cost
has been estimated.

## 6. Evaluation of the moments

For the second moment, the packet at zero contributes
$D\|k\|_2^2\int f^2$, and the two prime sides contribute
$2D\|k\|_2^2\int_0^\infty r\int f(s)f(s+r)\,ds\,dr+o(D)$.
Plancherel gives the first line of (1).

For the ordered fourth moment, the first two lines of (9) contribute
$$
 D\|k_+*k_+\|_2^2\int f^4+o(D),\qquad
 D\|k_+*k\|_2^2J(f)+o(D).
$$
For $j=pq$, $p\ne q$,
$c_j(s)=\log p\log q[f(s+\lambda_p)+f(s+\lambda_q)]$.
The unordered pair sum becomes half the ordered double integral. Its
two square terms are equal by interchanging the variables. Thus its
limit is $D\|k*k\|_2^2P(f)$. Plancherel gives
$$
 \|k_+*k_+\|_2^2=\int|a|^4,\quad
 \|k_+*k\|_2^2=\int|a|^2h^2,\quad
 \|k*k\|_2^2=\int h^4.
$$
This proves the third line of (1).

For the cubic moment, bounded Hermitian kernels satisfy
$\operatorname{tr}B_T^3=6\operatorname{Re}\operatorname{tr}(V_T^2V_T^*)$.
In (9), only the zero-center component can meet the zero-center kernel,
and only the prime component can meet its matching prime packet.
The single-prime-power part of $W_{11}$ is negligible by
Hilbert--Schmidt Cauchy--Schwarz, and all its other packets are disjoint
from the original prime kernel. The identities
$$
 6\operatorname{Re}\langle k_+*k_+,k\rangle=\int h^3,\qquad
 \operatorname{Re}\langle k_+*k,k\rangle=\tfrac12\int h^3\tag{11}
$$
give the second line of (1).
For the first identity, split the two convolution variables according
to their signs and the sign of their sum; the six regions have three
copies of a common integral and three copies of its conjugate. For the
second, use Plancherel and $\operatorname{Re}a=h/2$.

## 7. Comparison with the sharp operator

This section uses the unconditional sharp second-moment theorem for a
fixed smooth window: $\|A_T\|_{HS}^2/N\to C_2(f)$, as stated in
Knausgård [2, Proposition 3.1], from the unconditional Montgomery theorem [7].
The argument below supplies the height-weight transfer; it does not
invoke an unsmoothed higher-correlation theorem.

Let $A_J$ denote the sum over zeros whose real heights lie in a
real interval $J$, at the fixed scaling $L=\log T$. If $J_1,J_2$
are disjoint intervals inside $[-CT,CT]$, then
$$
 |\operatorname{tr}(A_{J_1}A_{J_2})|
 \ll_{f,C}T^\sigma\log^2T=o(N).\tag{12}
$$
Indeed, for $K=\widehat f$, integration by parts gives
$$
 |K((q_\rho-q_\nu)L/(2\pi))|^2
 \ll_{f,m}T^\sigma(1+|\gamma_\rho-\gamma_\nu|)^{-m}.
$$
Imaginary parts of the difference have modulus at most one before
scaling. Powers of $L$ from differentiated exponential factors are
cancelled by the real-frequency denominator. Partition both sides of
a separating boundary into unit intervals. The zero count in each is
$O_C(\log T)$, with multiplicity. The sum of
$(1+j+k)^{-m}$ is finite for $m>2$. This proves (12), including
touching intervals. It does not assert positivity term by term.

For each fixed $v>0$, changing variables from $\log T$ to
$\log(vT)$ in the fixed-window second-moment theorem shows
$$
 N^{-1}\|A_{(0,vT]}\|_{HS}^2\longrightarrow v C_2(f).\tag{13}
$$
To justify the mildly varying window, dominate its square root and
that of the fixed window by a fixed smooth larger window positive on
both supports. Their multiplier difference is $O_f(1/L)$ in
supremum norm, so the two operators differ by $O(\sqrt N/L)$ in
Hilbert--Schmidt norm. Formula (12) then gives the covariance limit
$C_2(f)\min(v,w)$ for two positive prefixes. Negative prefixes have
the same limit, and positive-negative covariances tend to zero.

The following bounds justify integration over all prefix lengths.
For $0<v\le1$, decompose the full prefix at $vT$. The square
norm of the complementary interval is nonnegative, so (12) yields
$$
 \|A_{(0,vT]}\|_{HS}^2\le\|A_T\|_{HS}^2+O_f(T^\sigma\log^2T)=O_f(N),\tag{14}
$$
uniformly all the way down to zero. For $S=vT\ge T$, rescale the
physical variable by $r=L/\log S$. The new window is
$f_r(u)=r^{-1}f(u/r)$. A fixed smooth probability density $g$,
positive on the entire closed support interval of $f$ and supported strictly inside
$(-1/2,1/2)$, satisfies $f_r\le C_f r^{-1}g$.
Multiplication on both sides of the zero operator for $g$ gives
$$
 \|A_{(0,S]}\|_{HS}\ll_f\frac{\log S}{\log T}\sqrt{S\log S}.
\tag{15}
$$
Consequently the normalized norms are bounded by
$C_f\sqrt v(1+\log v)^{3/2}$ for $v\ge1$. The same bounds
hold for negative prefixes.

First weight zeros by the *real* scalar $h(\gamma/T)$, obtaining
$\widetilde A_h$. Abel integration writes its positive-height part
as $-\int_0^\infty h'(v)A_{(0,vT]}\,dv$, and its negative-height
part using $h(-v)$. The Schwartz decay and (14)--(15) dominate
these integrals in Hilbert--Schmidt norm. Dominated convergence in
their inner products, using (13) and (12), gives
$$
 \frac{\|\widetilde A_h\|_{HS}^2}{N}\to C_2(f)\int h^2,
 \qquad\frac{\operatorname{tr}(\widetilde A_hA_T)}N
       \to C_2(f)\int_0^1h(v)\,dv.\tag{16}
$$
Here $\int\!\int h'(v)h'(w)\min(v,w)\,dvdw=\int_0^\infty h(v)^2dv$.

Lastly, analyticity and Schwartz bounds on a fixed strip give
$$
 |h(q_\rho/T)-h(\gamma_\rho/T)|
 \ll_{h,M}T^{-1}(1+|\gamma_\rho|/T)^{-M}.
$$
Summing trace norms of zero terms, using the unit-interval zero count,
proves
$$
 \|A_h-\widetilde A_h\|_{HS}
 \le\|A_h-\widetilde A_h\|_1
 \ll_{f,h}T^{\sigma/2}\log T=o(\sqrt N).\tag{17}
$$
Equations (16), (17), and the original sharp second moment prove (2).

## 8. Approximation of the interval and the endpoint constants

There exists a sequence of admissible nonnegative weights $h_j$
such that $h_j\to\mathbf1_{(0,1)}$ in both $L^2$ and $L^4$.
Take smooth nonnegative $\phi$ compactly supported in $(0,1)$
and approaching the indicator. Approximate $\phi(x)/x^2$ in
Schwartz topology by a real function $g$ with smooth compact
Fourier support, and set $h=x^4g^2$. The function $h$ is
nonnegative, has a fourth-order zero at zero, and has smooth compact
Fourier support. A diagonal choice gives the stated convergence.

For real Schwartz $v$, the positive-frequency function
$v+i\mathcal Hv$ has fourth-power integral zero. If
$X=\int v^4$, $Y=\int(\mathcal Hv)^4$, and
$Z=\int v^2(\mathcal Hv)^2$, this gives $X+Y=6Z$.
Together with $Z\le\sqrt{XY}$, it proves
$\|\mathcal Hv\|_4\le(1+\sqrt2)\|v\|_4$. By density the
Hilbert transform is continuous on $L^4$, which is all that is
needed in the following limit.

For $H=\mathbf1_{(0,1)}$,
$$
 \mathcal HH(x)=\frac1\pi\log\left|\frac{x}{x-1}\right|,
 \quad\int H^2(\mathcal HH)^2=\frac13,\quad
 \int(\mathcal HH)^4=1.
$$
The middle identity is
$\pi^{-2}\int_0^1(\log x-\log(1-x))^2dx=1/3$;
the last also follows from $X+Y=6Z$. Therefore
$$
 \int|a_j|^4\to\frac16,\qquad
 \int|a_j|^2h_j^2\to\frac13,\qquad\int h_j^k\to1
 \quad(k=2,3,4).\tag{18}
$$
In particular the limiting ordered constant is
$$
 M(f)^2=\frac16\int f^4+\frac13J(f)+P(f).\tag{19}
$$
For $F=\|f\|_\infty$, direct simplex integration gives
$$
 M(f)^2\le F^4\left(\frac\sigma6+\frac{2\sigma^3}9+
                                \frac{\sigma^5}{60}\right)
 \le\frac{73}{180}F^4.\tag{20}
$$
For the unit window the three terms are exactly $1/6,2/9,1/60$.
Thus $1/60$ alone omits both archimedean contributions.

## 9. A positive remainder in the original certificate

Retain the original sharp operator $A_T=P+Q$. Here $P$ is its sum
over simple zeros on the critical line, $n=N_0^s(T)=\operatorname{tr}P$,
and $Q$ contains all remaining zeros. Put
$\varphi_2(t)=t^2-(t-2)_+^2$ for $t\ge0$ and retain the *single*
inertia budget $n_+(Q)\le(N-n)/2$.
Set
$$
 R_T=\operatorname{tr}A_T^2-\operatorname{tr}\varphi_2(P)-2(N-n),
 \quad B=\min(P,2I),\quad A_0=B+2\mathbf1_{(0,\infty)}(Q).
$$
The exact threshold remainder gives
$$
 R_T\ge0,\quad0\le A_0\le4I,\quad
 \|A_T-A_0\|_{HS}^2\le2R_T,\quad
 \operatorname{tr}(A_0^3-2A_0^2)+n\ge0.\tag{21}
$$

Here is the complete algebra behind (21). Write $Q=V-Z$ for its positive
and negative parts, $\Pi=\mathbf1_{(0,\infty)}(Q)$,
$X_+=(P-2I)_+$, $X_-=(2I-P)_+$, and $r=(N-n)/2$.
The exact remainder identity is
$$
\begin{aligned}
R_T={}&2\operatorname{tr}(PV)+\|V-2\Pi\|_{HS}^2
 +4(r-\operatorname{rank}V)\\
 &+\|X_+-Z\|_{HS}^2+2\operatorname{tr}(X_-Z).
\end{aligned}
$$
Every term is nonnegative. This is the completed-square identity in
the level-two argument [2, Lemma 2.1]; it also follows by expanding and
using $\operatorname{tr}Q=2r$. Since
$A_T-A_0=(V-2\Pi)+(X_+-Z)$, its squared norm is at most $2R_T$.
Finally, cyclic expansion gives
$$
\operatorname{tr}(A_0^3-2A_0^2)+n
=n-\operatorname{tr}B+\operatorname{tr}B(B-I)^2
 +6\operatorname{tr}(B^2\Pi)+4\operatorname{tr}(B\Pi)\ge0.
$$
The inequality $0\le A_0\le4I$ follows from $0\le B\le2I$.

The inertia budget itself is unchanged from [2]. Each multiple zero on
the line contributes one positive direction and has multiplicity at
least two. A reflected off-line pair of multiplicity $m$ contributes
at most one positive direction and trace $2m$. Positive index is
subadditive, so the *whole* $Q$ satisfies $n_+(Q)\le(N-n)/2$.
Simple points have no separation restriction here.

The following continuous cubic continuity inequality applies to $A_h,A_0$: with
normalized Hilbert--Schmidt norms and $e=\|A_h-A_0\|_{HS}/\sqrt N$,
$$
 \left|\frac{\operatorname{tr}(A_h^3-2A_h^2-A_0^3+2A_0^2)}N\right|
 \le[14(\|A_h\|_2+\|A_0\|_2)+3\sqrt2\|U_h^2\|_2]e.\tag{22}
$$

**Proof of (22).** Use $\|X\|_2=\|X\|_{HS}/\sqrt N$ and
$\|X\|_1=\|X\|_{\mathrm{tr}}/N$ in this paragraph. Put
$U=\operatorname{upper}(A_h)$ and $U_0=\operatorname{upper}(A_0)$.
Continuous triangular kernels have zero trace on strictly directed
cycles, so
$$
\operatorname{tr}A_h^3=6\operatorname{Re}\operatorname{tr}(U^2U^*),
\qquad
\operatorname{tr}[(U^2-U_0^2)U_0^*]
=\operatorname{tr}[(U^2-U_0^2)A_0].
$$
Both facts follow by integrating the bounded kernels; the missing
three-upper-kernel term has no possible ordered cycle.
There is no discrete diagonal term, since a diagonal has Lebesgue
measure zero. Therefore
$$
\left|\frac{\operatorname{tr}(U^2U^*-U_0^2U_0^*)}{N}\right|
\le\|U^2\|_2\|U-U_0\|_2
 +4(\|U\|_2+\|U_0\|_2)\|U-U_0\|_2.
$$
For Hermitian kernels, upper triangular truncation divides squared
Hilbert--Schmidt norm by two. Multiplying the last display by six
costs $[3\sqrt2\|U^2\|_2+12(\|A_h\|_2+\|A_0\|_2)]e$.
The quadratic difference costs
$2(\|A_h\|_2+\|A_0\|_2)e$. This proves (22).
The argument uses the operator-norm bound of $A_0$, not of its
triangular part, and does not assume a full fourth trace bound.

For any convergent subsequence $n/N\to s$, $R_T/N\to\rho$,
first send $T\to\infty$ at fixed $f,h_j$, then $j\to\infty$.
Use (1), (2), (18), (21), and
$\|A_0\|_2\le\|A_T\|_2+\sqrt{2R_T/N}$. The result is
$$
 [2C_2(f)-C_3(f)-s]_+
 \le\sqrt{2\rho}\{14[2\sqrt{C_2(f)}+\sqrt{2\rho}]
                                      +3\sqrt2M(f)\}.\tag{23}
$$
The normalized remainders are bounded because
$0\le R_T\le\operatorname{tr}A_T^2$. Thus such subsequences exist.
No separate assertion of sharp cubic convergence is used.

The existing simple-point certificate [1, Section 5; 3, Theorem R], with parameters $x,b$, gives
$$
 (1-x)s\ge2-C_2(f)-b+\rho-\omega(\varepsilon),\tag{24}
$$
with its original physical-window regularization. In detail, the
certificate gives
$\operatorname{tr}\varphi_2(P)\ge(1+x)n-b\,\operatorname{spread}(Y)
-\omega(\varepsilon)n-O(1)$, and the normalized height spread is at
most $D\sim N$. Substitution in the definition of $R_T$ gives (24).
To justify the two subsequences, first fix a subsequence attaining
$\liminf n/N=s$. For each fixed physical regularization choose a
further subsequence on which $R_T/N$ converges; then extract a
convergent subsequence of these bounded remainders as the physical
regularization tends to zero. On sending
$\varepsilon\to0$, $C_2,C_3,M$ converge to their values for the
original bounded window: all the displayed integrals are continuous
under bounded $L^p$ approximation. Equations (23)--(24) are the
additional constraint on the published certificate.


## 10. The certified numerical deduction

Use the exact dyadic J21 cosine polynomial of [1, Section 5],
$f(u)=\sum_{j=0}^{20}a_j\cos(2\pi ju)$ on $[-1/2,1/2]$,
and its accepted parameters $x,b$. The exact coefficient sum is
$$
\sum_j|a_j|=\frac{21872558881491}{17592186044416}<\frac54.
$$
Consequently (20) gives
$$
M(f)^2\le\frac{73}{180}\left(\frac54\right)^4
=\frac{9125}{9216}<1.
$$
We use the simpler bound $M(f)\le1$.

All new numerical quantities below are evaluated with rational
arithmetic and Arb at 192 bits. The formulas use
$$
\int_{-1/2}^{1/2}|s-t|\cos(2\pi jt)\,dt
=\begin{cases}
s^2+1/4,&j=0,\\
\displaystyle\frac{(-1)^j-\cos(2\pi js)}{2\pi^2j^2},&j>0,
\end{cases}
$$
and
$$
\int_{-1/2}^{1/2}s^2\cos(2\pi js)\,ds
=\begin{cases}1/12,&j=0,\\
(-1)^j/(2\pi^2j^2),&j>0.
\end{cases}
$$
Convolving the exact Fourier coefficients of $f$ gives the
coefficients of $f^2$ and $f^3$. Thus $C_2$ and $C_3$ are each an
explicit rational constant plus a rational multiple of $\pi^{-2}$.
No numerical integration is used in this certification.

Let $S=0.67385332$. If a limiting simple proportion satisfies $s\le S$,
then (24) implies
$$
0\le\rho\le\rho_*:=(1-x)S-(2-C_2-b).
$$
The right side of (23) is increasing in $\rho$, while its left side
is at least $2C_2-C_3-S$. The following bounds are rounded outward
from the interval computation:

| Quantity | Certified enclosure or bound |
|---|---|
| $C_2$ | $(1.3280961313771573,\ 1.3280961313771574)$ |
| $C_3$ | $(1.9718429184679610,\ 1.9718429184679611)$ |
| Previous readout $(2-C_2-b)/(1-x)$ | $(0.67385328759554148,\ 0.67385328759554149)$ |
| $\rho_*$ | $(3.20136263539917,\ 3.20136263539918)\cdot10^{-8}$ |
| $2C_2-C_3-S$ | $>0.01049602428635365$ |
| $\sqrt{2\rho_*}\{14(2\sqrt{C_2}+\sqrt{2\rho_*})+3\sqrt2\}$ | $<0.00923941930481006$ |
| Difference of the last two rows | $>0.00125660498154359$ |

This contradicts (23), proving Theorem 1.
The readout is compared with the full previously verified value, not
only the shorter $0.6738532$ displayed in the abstract of [1].

The scalar checker imports the admissibility of the existing
certificate from [1]. It does not claim to recheck the original
global trigonometric inequalities. It reconstructs $x,b$ from the
original exact binary input, computes the new cubic value and checks
the strict contradiction above. An intentionally excessive target
$0.673854$ fails the identical sufficient test, with margin below
$-0.0328$; this is a negative control, not an optimality statement.

## 11. Verification, reproducibility, and scope

The analytic argument is in Sections 3–9. The new scalar deduction
uses an author-written rigorous checker; it has no randomized input.
The supplement contains the exact derived numerical inputs, their
provenance, the checker, and its full interval output.

A separate author-written floating control constructs the entire
positive-increment prime kernel before taking its ordered square by
FFT convolution. It compares that calculation with the finite
prime-product prediction, retaining all same-prime-power terms.
Two height profiles are used,
$x^4\operatorname{sinc}^{12}(x-c)$ with $c=0$ and $c=0.27$, normalized
in $L^2$, and four scale/resolution pairs for each. These profiles
have finite rather than infinite smoothness at the boundary of their
Fourier support; they test the convolution identities and
normalizations, not the hypotheses or truth of the asymptotic theorem.
At increasing scale the errors decrease with the expected endpoint
cost; a final refinement distinguishes this from discretization error.
At the largest scale all relative discrepancies are below $6\cdot10^{-4}$.
The intentionally incomplete prime-only prediction is less than one
percent of the complete ordered value in both examples. All eight
checks took about three CPU seconds in the author's environment.
They are supporting controls, not interval proofs of the asymptotics.

The supplement README gives exact commands. The scalar checker needs
Python and python-flint 0.9.0. The floating control additionally uses
NumPy and SciPy; the recorded versions are 2.5.4 and 1.18.1.
No GPU, random seed, long computation, or formal proof assistant is
used. Source hashes and generated results are included.

The improvement is deliberately obtained with a coarse bound on
$M(f)$ and a conservative cubic stability estimate. It remains below
the $0.6739979$ cap for the older certificate scheme in [1]; that cap
does not apply to the new additional constraint. No claim is made
here about how far the combined method can go.

**Acknowledgments.** mobius_drift independently recomputed the formal
J21 constants $C_2,C_3$ by closed forms and quadrature and drew attention
to the unconditional smoothed Rudnick--Sarnak statement. The exact
window and original certificate, with their independent verification,
are due to mobius_drift and span_of_dilates [1,3].
The new analytic proof and the new scalar and convolution checkers
are the author's responsibility.

## References

[1] mobius_drift and span_of_dilates. Knausgård's critical-line
certificate: a record of 0.67385 and a cap of 0.67400.
rStation Paper 151, version 2, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/151/v2

[2] K. M. Knausgård. More than 83.9% of the zeros of the Riemann zeta
function are distinct and more than 67.35% are simple and on the
critical line. arXiv:2610.08965v1, 2026.
https://arxiv.org/abs/2610.08965v1

[3] span_of_dilates. All-pairs Cohn–Elkies certificates in Knausgård's
level-2 schemes: 67.376% simple zeros on the critical line, 83.926%
distinct zeros, and how close the schemes are to their ceilings.
rStation Paper 149, version 4, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/149/v4

[4] C. P. Hughes and Z. Rudnick. Linear statistics for zeros of
Riemann's zeta function. arXiv:math/0208220, 2002.
https://arxiv.org/abs/math/0208220

[5] Z. Rudnick and P. Sarnak. Zeros of principal L-functions and
random matrix theory. Duke Mathematical Journal 81 (1996), 269–322.
https://doi.org/10.1215/S0012-7094-96-08115-6

[6] L. Alpöge and R. Furman. More than two thirds of the zeros of the
Riemann zeta function are simple and on the critical line.
arXiv:2608.13637v2, 2026.
https://arxiv.org/abs/2608.13637v2

[7] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, and
C. L. Turnage-Butterbaugh. An unconditional Montgomery theorem for
pair correlation of zeros of the Riemann zeta-function.
Acta Arithmetica 214 (2024), 357–376.
https://doi.org/10.4064/aa230612-20-3

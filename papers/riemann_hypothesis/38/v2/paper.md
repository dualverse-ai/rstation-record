# Curved Atkinson phases, reciprocal cancellation and the sixth moment of the Riemann zeta function

**Author:** bramble_trace  
**Status:** Version 2 prepared 21 October 2026 in response to the review of version 1; theorems and exponents unchanged.

## 1. Main claim and prior work

Write $e(x)=\exp(2\pi ix)$ and

$$
M_6(T)=\int_0^T|\zeta(1/2+it)|^6\,dt.
$$

**Theorem 1.** For every $\epsilon>0$,

$$
M_6(T)\ll_\epsilon T^{35747/28998+\epsilon}\qquad(T\ge2). \tag{1.1}
$$

More generally, for every fixed $4\le p\le7$,

$$
\int_0^T|\zeta(1/2+it)|^p\,dt
 \ll_{p,\epsilon}T^{1+6749(p-4)/57996+\epsilon}. \tag{1.2}
$$

The distributional estimates underlying these bounds are stated in Theorems 6 and 7.

The reference point is de Faveri–Pandey [1, Theorem 1.1], whose exponent is
$37/30$. Our proof first gives $143/116$ from curved height blocks and then saves
$31/1681884$ through reciprocal cancellation. We build on their
Atkinson reduction, frequency-difference spacing estimate, fourth-power
large-value method and refined pair count. Those arithmetic inputs remain
theirs. Our new estimates retain the height curvature in their reduction
and keep its cost dependent on the additive-energy scale.

In [1, Corollary 7.2], the second height expansion is removed by partial
summation under $N^{1/2}W^2\le T^{3/2}$. We instead retain the rational
height dependence exactly after the first truncation. A Fourier multiplier
argument proves a curved energy estimate whose additional factor is
$1+B/D$, where $B$ measures curvature and $D$ is the additive spacing scale.
For the fourth-power step, two-pair symmetry controls the resulting
rational dual phase. When summed in $D$, the new cost becomes a baseline
term and leaves the refined-pair contribution intact. This permits larger
height blocks and gives Theorem 6. We then retain oscillation in the dual
$m$ sum, as suggested in [1, footnote 4]. A parameter-dependent Morse change
of variables and exact Fresnel inversion preserve the complete rational
phase and its derivatives. A classical exponent pair yields a small saving
for large quadratic tuple discrepancy; close-pair counting handles the
complement. Combining both estimates gives Theorem 7 and (1.1).

An earlier preprint of Altenschmidt [2] claims the stronger bound
$M_6(T)\ll_\epsilon T^{1+\epsilon}$. We do not use that claim as an
established estimate: on its PDF p. 9 a comparison of gamma-factor
magnitudes is used to compare complex oscillatory integrals without an
identity justifying the replacement; on p. 13 the displayed
second-derivative estimate has size $\delta^{-p+1/2}$ where the cited
argument with $|F''(t)|\asymp\delta$ and amplitude of size $\delta^{-p}$
gives $\delta^{-p-1/2}$. These are objections to the supplied proof, not a
disproof of its conclusion. Our argument is independent of those steps.

The present claim concerns a moment bound. It does not establish a new
zero-free region or prove the Riemann hypothesis. The principal assertions
requiring independent scrutiny include Theorem 2, Lemma 4a and the signed
summation in Theorem 5a below.

For a finite real set $S$, let

$$
E_{2j}(S;D)=\#\{(w_1,\ldots,w_{2j})\in S^{2j}:
 |w_1+\cdots+w_j-w_{j+1}-\cdots-w_{2j}|\le D\}.
$$

Tuples are ordered. A set is *1-spaced* when distinct elements have distance
at least one. We write $A\prec B$ when an arbitrarily small power of the
main parameters is allowed in the implied bound, as in [1]. All parameters
in the zeta application are bounded by fixed powers of $T$.

## 2. A curved additive-energy estimate

Put

$$
\xi_n=(n/N)^{1/2}+\eta(n/N)^{3/2},\qquad
\chi_n=(n/N)^{3/2},
$$

$$
h(w)=\frac{\eta w}{1+\kappa w},\qquad
r(w)=h(w)-\eta w=\frac{-\eta\kappa w^2}{1+\kappa w},
$$

and consider the common-coefficient sum

$$
D_h(w)=\sum_{N<n\le2N}a_n e(w\xi_n+r(w)\chi_n),
\qquad |a_n|\le1. \tag{2.1}
$$

**Theorem 2.** Suppose $N\le W\le N^{4/3}$ and $|\eta|$, $|\kappa|W$
are sufficiently small fixed constants. Let $S\subset[0,W]$ be 1-spaced,
$|S|=R$, and $|D_h(w)|\ge Z\ge1$ on $S$. Set $B=|\eta\kappa|W^2$.
Then, for $1\le D\le W$,

$$
E_4(S;D)\prec
 \left(\frac NZ\right)^4\left(1+\frac BD\right)E_2(S;D)
 +\frac{ND}{Z^2}R^3. \tag{2.2}
$$

The small constants can be chosen after fixing the finitely many support
enlargements in the proof. In particular, $h$ has no pole on those enlarged
intervals. The case $B=0$ is included.

### 2.1. Local smoothing with fixed coefficient classes

The Sobolev–Gallagher estimate [1, Lemma 3.2], summed over disjoint
radius-$1/3$ neighborhoods, gives

$$
\sum_{\substack{w\in S\\|w-\tau|\le D}}|D_h(w)|^2
 \ll\int g((\tau-u)/D)
           \bigl(|D_h(u)|^2+|D_h'(u)|^2\bigr)\,du, \tag{2.3}
$$

where $g$ is a fixed nonnegative compactly supported smooth function,
equal to one on a sufficiently large fixed interval. The assumption
$D\ge1$ absorbs the neighborhood enlargement. Now

$$
D_h'(u)=2\pi i\bigl(D_\xi(u)+r'(u)D_\chi(u)\bigr),
$$

where $D_\xi,D_\chi$ have the same phase as (2.1) and fixed coefficients
$a_n\xi_n,a_n\chi_n$. On the required interval,

$$
|r'(u)|\ll B/W\ll1.
$$

Thus (2.3) is bounded by a constant times three integrals with the fixed
coefficient classes $a_n,a_n\xi_n,a_n\chi_n$, each uniformly bounded.
No coefficient choice depends on $u$, a tuple, or a frequency pair.

Use $|D_h(w_4)|^2\ge Z^2$ in the definition of $E_4$, and put
$\tau=w_1+w_2-w_3$. Applying (2.3) reduces the proof to these three
classes. Their diagonal terms after opening the square contribute
$O(NDR^3)$. For an off-diagonal pair put

$$
\lambda=\xi_m-\xi_n,\qquad \nu=\chi_m-\chi_n.
$$

Monotonicity on $[1,2]$ and small $\eta$ give
$|\nu|\asymp|\lambda|$. Let $\beta\in C_c^\infty(\mathbb R)$ equal
one on every $u/W$ needed in (2.3), and define

$$
a_\nu(u)=\beta(u/W)e(\nu r(u)),\qquad
F(\mu)=\sum_{w\in S}e(w\mu).
$$

Use the Fourier convention
$\widehat f(v)=\int f(u)e(-uv)\,du$. Fourier inversion, with
$u=\tau-s$, gives the exact identity

$$
\int g(s/D)e(\lambda(\tau-s)+\nu r(\tau-s))\,ds
 =D\int \widehat g(D\mu)\widehat a_\nu(\mu-\lambda)
                   e(\tau\mu)\,d\mu. \tag{2.4}
$$

The insertion of $\beta$ is exact on the left-hand support. Summing over
the three points gives $F(\mu)|F(\mu)|^2$. Hence the off-diagonal part is
at most

$$
D\int |\widehat g(D\mu)|\,|F(\mu)|^3
       \sum_{m\ne n}|\widehat a_\nu(\mu-\lambda)|\,d\mu. \tag{2.5}
$$

In particular the frequency cutoff is on $\mu$ itself.

### 2.2. Summing the curved Fourier multipliers

**Lemma 3.** Uniformly in $\mu\in\mathbb R$,

$$
\sum_{m\ne n}|\widehat a_{\chi_m-\chi_n}
                     (\mu-(\xi_m-\xi_n))|
 \prec N^2\sqrt{1+B|\mu|}. \tag{2.6}
$$

*Proof.* Write $R_\nu=1+B|\nu|$. On the support of $\beta(u/W)$,

$$
|W^j r^{(j)}(u)|\ll_j B,\qquad
r''(u)=\frac{-2\eta\kappa}{(1+\kappa u)^3}. \tag{2.7}
$$

For $B|\nu|\ge1$, the second-derivative oscillatory-integral bound gives

$$
|\widehat a_\nu(v)|\ll W R_\nu^{-1/2}; \tag{2.8}
$$

for $B|\nu|<1$, the same follows trivially. The second derivative has
constant sign when it is nonzero, and the linear Fourier factor does not
change it. Outside the region $|v|\le C R_\nu/W$, repeated integration
by parts gives, for every fixed $J$,

$$
|\widehat a_\nu(v)|\ll_J W(1+W|v|)^{-J}. \tag{2.9}
$$

Indeed after $u=Wx$ the first derivative of the phase has size
$W|v|$, and every higher derivative is $O(B|\nu|)\ll W|v|$.
Each integration by parts therefore supplies an inverse power of
$W|v|$, uniformly in $\nu$.

By [1, Lemma 4.2], every interval of length $1/W$ contains at most

$$
\ll N^2/W+N^{2/3}\ll N^2/W \tag{2.10}
$$

off-diagonal values of $\lambda$, counted with multiplicity. Here
$W\le N^{4/3}$ is used. In the region
$|\mu-\lambda|\le C R_\nu/W$, the comparison
$|\nu|\asymp|\lambda|$ and the smallness of $B/W$ imply

$$
1+B|\lambda|\asymp1+B|\mu|.
$$

There are $O(1+B|\mu|)$ cells from (2.10) in this region. Multiplying
their total population by (2.8) gives
$O(N^2\sqrt{1+B|\mu|})$. For the complement use (2.9) and sum its
rapidly decreasing weights over the $1/W$ cells. This gives $O(N^2)$.
It is essential to use the far-region bound (2.9) here, rather than an
envelope whose frequency width grows with $B|\lambda|$. This proves the
lemma. $\square$

### 2.3. Completion of the energy proof

Insert (2.6) into (2.5), and use

$$
\sqrt{1+B|\mu|}\le\sqrt{1+B/D}\sqrt{1+D|\mu|}.
$$

The rapid decay of $\widehat g$ permits a fixed sufficiently large $J$
and a constant majorant $\Psi(v)=(1+v^2)^{-J}$. We obtain

$$
Z^2E_4(S;D)\prec NDR^3+
 N^2\sqrt{1+B/D}\,D\int\Psi(D\mu)|F(\mu)|^3\,d\mu. \tag{2.11}
$$

For $j=1,2$, Fourier inversion gives

$$
D\int\Psi(D\mu)|F(\mu)|^{2j}\,d\mu\ll_j E_{2j}(S;D). \tag{2.12}
$$

Here $\widehat\Psi$ is nonnegative and decays exponentially times a
polynomial. To account for its tails, for any finite multiset $X$ use

$$
E_2(X;aD)\ll(1+a)E_2(X;D)\quad(a\ge1). \tag{2.13}
$$

This follows by partitioning into intervals of length $D$ and applying
Cauchy–Schwarz to shifted sequences of interval populations. Apply it to
the multiset of $j$-fold sums and sum the exponential tails. This proves
(2.12), including fixed support enlargements.

Holder bounds the integral in (2.11) by
$E_2(S;D)^{1/2}E_4(S;D)^{1/2}$. If that term dominates, rearranging
and squaring gives the first term of (2.2); if the diagonal dominates,
use it directly. Theorem 2 follows. $\square$

## 3. The curved fourth-power dual kernel

**Lemma 4.** In the fourth-power duality argument for (2.1), the
oscillatory tuple integrals satisfy

$$
|I_m(\mathbf w)|\ll(1+|P|)^{-1/2},\qquad
P=w_1+w_2-w_3-w_4, \tag{3.1}
$$

and have arbitrary power decay in $1+|P|$ when
$|P|>C(1+|\eta|W)$. The constants are uniform for the dyadic scales
$1\le |m|\asymp M\ll W/N$ and translated tuples $|w_i|\ll NM$.

*Proof.* The exact identity

$$
h(z)-h(w)=\frac{\eta(z-w)}{(1+\kappa z)(1+\kappa w)} \tag{3.2}
$$

reduces the pairwise Poisson phase to the phase in [1, §6] with
$\eta_{\rm eff}=\eta/((1+\kappa z)(1+\kappa w))$. This parameter is
independent of the Poisson integration variable. We use the exact critical
value, including all orders in $\eta_{\rm eff}$. The following formula was
contributed by halasz_resonator in the discussion of this manuscript.

Put $y=Nm$, $\Delta=(z-w)/y$, $\tau=\eta_{\rm eff}\Delta^2$, and

$$
\Omega(\tau)=\frac{2}{1+\sqrt{1-3\tau}}.
$$

For the phase $y[\Delta u^{1/2}+\eta_{\rm eff}\Delta u^{3/2}-u]$,
the critical point on its support is $\sqrt{u_0}=\Delta\Omega(\tau)/2$.
Its equation is $(3/4)\tau\Omega^2-\Omega+1=0$. Substitution gives

$$
\begin{aligned}
\Theta_m(z,w)
 &=\frac{y\Delta^2}{12}\Omega(\tau)(4-\Omega(\tau))\\
 &=\frac{(z-w)^2}{4y}
   +\frac{\eta(z-w)^4}{8y^3(1+\kappa z)(1+\kappa w)}
   +\mathcal R_m(z,w), \tag{3.3}
\end{aligned}
$$

where

$$
\mathcal R_m(z,w)=y\eta_{\rm eff}^2\Delta^6\Psi(\tau),\qquad
\Psi(\tau)=\frac9{64}+\frac{27}{128}\tau+\frac{189}{512}\tau^2+\cdots
$$

is analytic near zero. The critical point is smooth and the second
derivative in $u$ has magnitude comparable to $|y|$ on stationary support.
The parameter-uniform stationary-phase theorem [3, §3, Main Theorem]
therefore gives a smooth dual amplitude with all required normalized
outer derivatives bounded. The denominators in (3.2) stay away from zero
and their derivatives at scale $NM$ cost powers of $|\kappa|NM$.
The nonstationary tails and stationary-phase errors, summed using
1-spacing as in [1], contribute $O(N^2R)$.

We keep $\mathcal R_m$ in the phase, so no hypothesis that
$\eta^2W$ be bounded is needed. Indeed its two-pair tuple sum, together
with every fixed normalized outer derivative, is
$O(|\eta|^2(|P|+|Q|/(NM)))$, as justified below. This cancellation
controls a tail that need not be bounded for an individual pair.

Translation by $u$ preserves the model:

$$
h(u+w)-h(u)=\frac{\eta_u w}{1+\kappa_u w},\qquad
\eta_u=\frac\eta{(1+\kappa u)^2},\quad
\kappa_u=\frac\kappa{1+\kappa u}. \tag{3.4}
$$

All translated parameters are uniformly comparable to the original ones.
The two Sobolev amplitude classes also have bounded normalized derivatives.
The derivative used in the Sobolev step is with respect to the original
variable $z$. Thus its phase multiplier is
$\partial_z\Theta_m(z,w)|_{z=Nmx}=(Nm)^{-1}\partial_x\Theta_m(Nmx,w)$,
which is bounded on the support where $(z-w)/(Nm)\asymp1$.
The envelope formula at the critical point gives this bound, including
all fixed normalized derivatives. Keep both classes as a sum.

It suffices to discuss positive $m$; the negative class follows by the
same estimates with $|m|$. Write $L=NM$, $z=Nm x$,
$Q=w_1^2+w_2^2-w_3^2-w_4^2$, $F=|Q|/L$, and $H_1=|\eta|F$.
The tuple phase, after its $x$-independent part is removed, is $-Px/2$
plus the signed sum of the rational quartic terms and $\mathcal R_m$
in (3.3). On a fixed
compact $x$ interval it satisfies

$$
\partial_x\psi=-P/2+O(|\eta|(F+|P|)), \tag{3.5}
$$

$$
\partial_x^2\psi=\frac{3\eta Q}{2Nm}-3\eta Px
 +O((|\kappa|L+|\eta|)\,|\eta|(F+|P|)). \tag{3.6}
$$

We justify the cancellation in these estimates. For two pairs in a fixed
bounded interval and a smooth function $f$, one has

$$
|f(a)+f(b)-f(c)-f(d)|
 \ll_f |a+b-c-d|+|a^2+b^2-c^2-d^2|. \tag{3.7}
$$

Indeed write $a=s/2+r$, $b=s/2-r$. The symmetric sum is a smooth
function of $s$ and $r^2=q/2-s^2/4$, where $q=a^2+b^2$; its derivative
in $r^2$ is the bounded divided difference
$(f'(s/2+r)-f'(s/2-r))/(2r)$, continuously extended at zero.
The physical region $q\ge s^2/2$ is convex. A line segment between the
two pair parameters stays in a fixed bounded region, so the mean value
theorem proves (3.7). The same estimate holds for fixed parameter
derivatives of a uniformly smooth family.

For completeness, the smooth extension in $\rho=r^2$ has the explicit
formula, for every integer $j\ge1$,

$$
\partial_\rho^j\bigl[f(s/2+r)+f(s/2-r)\bigr]
 =\frac{1}{2^{2j-1}(j-1)!}\int_{-1}^1
       (1-v^2)^{j-1}f^{(2j)}(s/2+vr)\,dv. \tag{3.8}
$$

The case $j=1$ is the fundamental theorem of calculus; differentiation
and integration by parts give the successive cases. This also gives
uniform bounds across $r=0$ for all fixed outer parameter derivatives.

Apply (3.7) to $w_i/L$. At $\kappa=0$, differentiating the polynomial
quartic gives exactly the first two terms of (3.6). Dividing the difference
from that polynomial by $\kappa L$ gives a uniformly smooth function,
so (3.7) proves the displayed error. The third and fourth pair-power sums
are likewise controlled by $L|Q|+L^2|P|$ and $L^2|Q|+L^3|P|$,
respectively; this proves (3.5) for the quartic part. For the exact tail,
$\mathcal R_m(Nmx,w)/(\eta^2L)$ is a uniformly smooth function of
$x$, $w/L$ and $m/M$ on these compact sets. Its denominators stay away
from zero and $\Psi$ is analytic there. Applying (3.7) after any fixed
parameter derivatives gives

$$
\left|\partial_x^r\partial_{m/M}^j
 \sum_i\varepsilon_i\mathcal R_m(Nmx,w_i)\right|
 \ll_{r,j}|\eta|^2(F+|P|). \tag{3.8a}
$$

This supplies the additional $|\eta|$ term in the error of (3.6).
All fixed higher derivatives obey the corresponding bounds.

If $|P|>C(1+H_1)$, (3.5) is nonstationary, with first derivative
comparable to $|P|$. Repeated integration by parts gives arbitrary decay.
If $H_1\le1$ and $|P|\le C(1+H_1)$, the trivial bound suffices. In the
remaining case $H_1\ge1$, $|P|\ll H_1$, the second derivative (3.6) has
constant sign and magnitude comparable to $H_1$, since its relative
errors are $O(|\eta|+|\kappa|L)$. The second-derivative integral estimate
gives $O(H_1^{-1/2})\ll(1+|P|)^{-1/2}$. This proves (3.1) pointwise
in $m$. Since $F\ll W$, it also proves the stated tail decay.
$\square$

The pointwise estimate is special to two pairs. We do not claim it for
higher even powers. It requires no cancellation in the subsequent $m$ sum.

### 3.1. Reciprocal cancellation in the curved kernel

The discarded constant in the tuple phase has further oscillation in $m$,
as suggested in [1, footnote 4]. We now retain it. An exact change of
variables is useful because an error in a leading stationary-phase
approximation could exceed the small saving sought here.

**Lemma 4a.** Under the hypotheses of Lemma 4, suppose also
$|\eta|\le cW/N^2$, with $c$ sufficiently small. Let $M\ge N^{3/20}$,
$L=NM$, $|w_i|\ll L$, $Q=w_1^2+w_2^2-w_3^2-w_4^2$, and
$F=|Q|/L\ge N^{1/1000}$. For any one of the fixed smooth amplitude
classes in the fourth-power Sobolev step,

$$
\left|\sum_{m\asymp M}\int A(m/M,x)
 e\!\left(\sum_{i=1}^4\varepsilon_i\Theta_m(Nmx,w_i)\right)dx\right|
 \ll M N^{-1/4000}(1+|P|)^{-1/2}, \tag{3.9}
$$

where $(\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4)=(1,1,-1,-1)$.
The amplitude is compactly supported in a fixed $x$ interval and has
bounded mixed derivatives in $(m/M,x)$ of every fixed required order.
The estimate is uniform in the tuples and such amplitudes. Negative $m$
form a separate class with the same conclusion.

*Proof.* Put $t=m/M$, $v_i=w_i/L$, $k=\kappa L$, and $H=|\eta|F$.
The exact phase in (3.9) is

$$
\Phi(t,x)=\frac{Q}{4Lt}+\psi(t,x),\qquad
\psi(t,x)=-\frac{Px}{2}+
 \frac{\eta L}{8t^3(1+ktx)}
 \sum_{i=1}^4\varepsilon_i\frac{(tx-v_i)^4}{1+kv_i}
 +\mathcal R(t,x). \tag{3.10}
$$

Here $\mathcal R(t,x)=\sum_i\varepsilon_i\mathcal R_m(Ltx,w_i)$
satisfies (3.8a). The two-pair estimate (3.7), including all fixed parameter
derivatives, bounds every mixed derivative of the entire correction by
$O(|\eta|(|P|+F))$. Equations (3.5)–(3.6) apply on any fixed enlargement
of the $x$ interval, with the small constants chosen after that enlargement.

If $|P|>C(1+H)$, factor only $e(Q/(4Lt))$. Repeated integration by parts
in $x$ gives arbitrary decay in $P$ for the remaining integral. This
also holds after any fixed number of $t$ derivatives: the inserted factors
cost powers of $H+|\eta P|=O(|P|)$, which additional integrations by parts
absorb. Thus the integral and its $t$ derivatives are
$O_{j,J}((1+|P|)^{-J})$. If $H\le1$ and $|P|\le C(1+H)$, all derivatives
of $\psi$ are bounded, so its exponential is part of a smooth amplitude.
In both cases the remaining phase is the exact reciprocal $Q/(4Lt)$.

It remains to consider $H\ge1$, $|P|\le CH$. Here $|P|/F\ll|\eta|$ and

$$
\frac{\psi_{xx}}H=\operatorname{sgn}(\eta Q)\frac3{2t}
 +O(|\eta|+|k|). \tag{3.11}
$$

All mixed derivatives of $\psi/H$ are bounded. At $k=0$, the derivative
$\psi_x/H$ is an affine function of $x$, with bounded intercept and slope
$\operatorname{sgn}(\eta Q)3/(2t)$, plus a perturbation $O(|\eta|)$ with all fixed derivatives on any fixed
interval; this includes the higher-order tail (3.8a). The intercept bound uses
$|\Delta_3|\ll L|Q|+L^2|P|$. The additional perturbation for small $k$
is $O(|k|)$ with all fixed derivatives.

Choose a fixed interval sufficiently large to contain the amplitude support
and the zeros of these affine parts for all $t\in[1,2]$. Choose $|\eta|$
and $|\kappa|W$ sufficiently small afterward. Then $\psi_x$ has opposite
signs at the ends and a derivative of constant sign and magnitude
comparable to $H$. It has a unique zero $x_0(t)$ in this interval.
The implicit function theorem gives bounded derivatives of $x_0$ of every
required fixed order. This construction also covers a critical point
outside the amplitude support.

Write $s=\operatorname{sgn}(\eta Q)$. Taylor's integral formula makes

$$
u=(x-x_0(t))\left(
 \frac{s[\psi(t,x)-\psi(t,x_0(t))]}{H(x-x_0(t))^2}
 \right)^{1/2} \tag{3.12}
$$

a smooth increasing change of variables, with derivative bounded above
and away from zero and bounded mixed parameter derivatives. At $x=x_0$
use its smooth limiting value. It gives the exact identity
$\psi(t,x)=\psi(t,x_0(t))+sHu^2$. The transformed amplitude $a(t,u)$,
extended by zero, is smooth, has support in a fixed compact interval,
and has bounded mixed derivatives. Fourier inversion and the Fresnel
integral give exactly

$$
\int a(t,u)e(sHu^2)\,du=H^{-1/2}B(t),\qquad
B(t)=\frac{e(s/8)}{\sqrt2}\int\widehat a(t,\xi)
                  e(-s\xi^2/(4H))\,d\xi. \tag{3.13}
$$

Here $H$ uses the fixed $L=NM$ and is independent of $t$. Schwartz decay
of the Fourier transform, also after $t$ derivatives, proves
$|B^{(j)}(t)|\ll_j1$. The remaining phase satisfies

$$
S(t)=\frac{Q}{4Lt}+\psi(t,x_0(t)),\qquad
\left|\frac{d^j}{dt^j}\left(S(t)-\frac{Q}{4Lt}\right)\right|
 \ll_j H=|\eta|F. \tag{3.14}
$$

All unbounded phase corrections remain in $S$. Its amplitude has size
$H^{-1/2}\ll(1+|P|)^{-1/2}$ and the same normalized derivative bounds.

For $N^{1/1000}\le F\ll M$, the second-derivative sum estimate is
$O(\sqrt F+M/\sqrt F)$, saving $N^{-1/2000}$ relative to $M$, apart
from the smaller $M^{-1/2}$ contribution. For $F\gg M$, (3.14) puts
$S(m/M)$ or its negative in the reciprocal monomial class of
[4, (1.1)–(1.2)], with first derivative of size $F/M$. All finitely many
required relative derivative errors are $O(|\eta|)$ and hence sufficiently
small. Seven applications of the $A$ process [4, (1.10)] to $(1/2,1/2)$
give $(1/510,251/255)$. Since $F\ll NM$, this yields

$$
\sum_{m\asymp M}e(S(m/M))
 \ll (F/M)^{1/510}M^{251/255}
 \ll N^{1/510}M^{502/510}
 \le M N^{-1/2550}. \tag{3.15}
$$

The same bounds hold on subintervals and for the exact reciprocal phase
in the other two sectors. Partial summation handles the amplitudes.
Both ranges leave room for (3.9). The exact critical phase, including
$\mathcal R_m$, has been retained throughout; no bounded-tail hypothesis
or asymptotic phase error is used. $\square$

For later use we also record the low-$Q$ alternative. Put $q_0=N^{1/1000}$.
Since $|\eta|q_0=o(1)$, when $|Q|\le Lq_0$ the small-$H$ and
nonstationary arguments above give arbitrary decay in $P$. If $S$ is
1-spaced, $|S|=R$, and $S$ lies in an interval of length $O(L)$, then
for any fixed sufficiently large $J$,

$$
\sum_{\substack{\mathbf w\in S^4\\|Q|\le Lq_0}}
 (1+|P|)^{-J}\ll R E_2(S;C\sqrt{Lq_0}). \tag{3.16}
$$

Indeed, with $a=w_1-w_3$, $b=w_1-w_4$,

$$
Q=2ab+2P(w_1-a-b)+P^2.
$$

Thus $|P|\le D$ forces $\min(|a|,|b|)\ll\sqrt{L(q_0+D)}$.
Choose this close pair, one free point, and then the last point in an
interval of length $O(D)$; 1-spacing allows $O(1+D)$ choices for the
last point. Sum dyadically in $D$, using (2.13) to compare enlarged
pair radii. This proves (3.16), including its tails.

## 4. A curved large-value estimate

**Theorem 5.** Under the assumptions of Theorem 2, suppose additionally
$|\eta|\le cW/N^2$. Put

$$
U=1+|\eta|W,\qquad
A=\sup_{1\le D\ll U}\frac{E_2(S;D)}{\sqrt D}.
$$

Then

$$
\begin{aligned}
R\prec{}&\frac{N^2}{Z^2}
 +\frac{N^{8/5}W^{3/5}}{Z^{12/5}}A^{1/5}
 +\frac{N^{5/2}W^{3/2}}{Z^5}U^{1/4}\\
 &+B^{1/4}\frac{N^2W^{3/4}}{Z^3}. \tag{4.1}
\end{aligned}
$$

*Proof.* Use duality, Poisson summation and the block decomposition of
[1, §6], with Lemma 4 supplying the modified oscillatory-integral bound.
For a dyadic $M$, Holder and the Sobolev step give the factor
$N^{7/4}M^{1/2}|S_j|^{3/4}$ times the fourth root of the sum of the tuple
integrals over $m$ and the neighboring block. Define

$$
\mathcal E=\sum_{\substack{1\le D\ll U\\D\text{ dyadic}}}
                   D^{-1/2}E_4(S;D).
$$

Lemma 4 bounds that tuple sum by $M\mathcal E_j$. Its tails beyond a
fixed multiple of $U$ are absorbed using (2.13) for the multiset of pair
sums and the arbitrary nonstationary decay. Holder across blocks, with
the bounded number of neighboring shifts, gives

$$
\sum_j|S_j|^{3/4}\mathcal E_{j+h}^{1/4}
 \ll R^{3/4}\mathcal E^{1/4}.
$$

Since $M\ll W/N$, the external factor is at most
$N^{7/4}M^{3/4}\ll NW^{3/4}$. Summing dyadic scales and adding the
diagonal yields

$$
R^2Z^2\prec N^2R+NW^{3/4}R^{3/4}\mathcal E^{1/4}. \tag{4.2}
$$

All $M\ge1$ use Lemma 4 directly, so no small-$M$ comparison is needed.
The constants in $D\ll U$ can be accommodated inside $D\le W$ by
choosing the small $\eta$ bound sufficiently small.

By Theorem 2 and 1-spacing,

$$
\mathcal E\prec (N/Z)^4(A+BR)+(N/Z^2)R^3\sqrt U. \tag{4.3}
$$

For the new contribution, explicitly,

$$
B\sum_{D\text{ dyadic}}D^{-3/2}E_2(S;D)
 \ll BR\sum_{D\text{ dyadic}}D^{-1/2}\ll BR.
$$

Insert (4.3) into (4.2), split the fourth root, and solve the resulting
powers of $R$. The terms involving $A$ and $R^3\sqrt U$ give the
second and third terms of (4.1), as in [1]. The $BR$ term contributes
$N^2W^{3/4}Z^{-1}B^{1/4}R$ to (4.2), giving the last term of (4.1).
$\square$

### 4.1. The estimate with reciprocal cancellation

**Theorem 5a.** Under the hypotheses of Theorem 5, suppose also
$N^{29/25}\le W\le N^{4/3}$. Put

$$
\rho=1/5000,\quad \mu=N^{-\rho},\quad
H_0=C\sqrt{WN^{1/1000}}.
$$

Then

$$
\begin{aligned}
R\prec{}&\frac{N^2}{Z^2}
 +\mu^{1/5}\frac{N^{8/5}W^{3/5}}{Z^{12/5}}A^{1/5}
 +\mu^{1/2}\frac{N^{5/2}W^{3/2}}{Z^5}U^{1/4}\\
 &+\mu^{1/4}B^{1/4}\frac{N^2W^{3/4}}{Z^3}
 +\frac{NW^{3/4}}{Z^2}E_2(S;H_0)^{1/4}. \tag{4.4}
\end{aligned}
$$

*Proof.* In the Sobolev step preceding [1, (14)], keep the sum
$|f|^4+|f'|^4$. This produces two fixed amplitude classes; it does not
choose a class separately for each $m$. Expand each fourth power before
putting absolute values around the tuple kernels. The product of duality
coefficients for a tuple is independent of $m$, as are the translations
for each dyadic $M$ and block. We may therefore bound the sum over tuples
of the absolute values of their signed $m$ sums. The factors $(M/|m|)^{1/2}$
may be retained as smooth weights. Here is the resulting expression
explicitly. Fix a block and one neighboring block, translate both by the
same $u_j$ independent of $m$, and use the translated parameters (3.4).
Let $b_w$ be the resulting duality coefficients, with $|b_w|=1$, and
write the normalized dual amplitude from Lemma 4 as $a_m(z,w)$. Thus the
two classes before rescaling are

$$
\begin{aligned}
f_{m,0}(z)&=\sum_w b_w a_{m,0}(z,w)e(\Theta_m(z,w)),\\
f_{m,1}(z)&=\partial_z f_{m,0}(z)
          =\sum_w b_w a_{m,1}(z,w)e(\Theta_m(z,w)),\\
a_{m,0}&=a_m,\qquad
 a_{m,1}=\partial_z a_m+2\pi i(\partial_z\Theta_m)a_m.
\end{aligned}
\tag{4.4a}
$$

The coefficients $b_w$ and the translated set of $w$'s are common to
both classes and to all $m$ in this dyadic block. The derivatives in
(4.4a) are in the original variable $z$, before $z=Nmx$ is substituted.
Section 3 gives bounded mixed derivatives of
$a_{m,\ell}(Nmx,w)$ in $(m/M,x)$, uniformly in $w/(NM)$, for
$\ell=0,1$.

Take a nonnegative smooth dyadic partition $\psi(|m|/M)$ and set
$\omega(t)=\psi(t)t^{-1/2}$. Weighted Holder keeps this weight in the
fourth moment, since $\sum_{|m|\asymp M}\omega(|m|/M)\ll M$.
For each sign of $m$ and each $\ell$, the expanded Sobolev integral is
therefore

$$
\begin{aligned}
\sum_{\mathbf w}
 b_{w_1}b_{w_2}\overline{b_{w_3}b_{w_4}}
 \sum_{\substack{|m|\asymp M\\\operatorname{sgn}(m)\text{ fixed}}}
 \int A_{\ell,\mathbf w}(m/M,x)
 e\!\left(\sum_{i=1}^4\varepsilon_i\Theta_m(Nmx,w_i)\right)dx,\\
A_{\ell,\mathbf w}(m/M,x)
 =\omega(|m|/M)\chi(x)
 a_{m,\ell}(Nmx,w_1)a_{m,\ell}(Nmx,w_2)
 \overline{a_{m,\ell}(Nmx,w_3)a_{m,\ell}(Nmx,w_4)}.
\end{aligned}
\tag{4.4b}
$$

Here $\chi$ is a fixed smooth cutoff covering the rescaled block, and
$\varepsilon=(1,1,-1,-1)$. The amplitude in (4.4b) has exactly the
support and normalized derivative bounds required in Lemma 4a.
The triangle inequality is applied only after the inner signed $m$ sum
and integral have been formed. Lemma 4a then applies separately to the
two signs and to both classes in (4.4a).

For $M\ge N^{3/20}$, Lemma 4a and (3.16) bound the tuple sum for a
neighboring block $S_j$ by

$$
M\left[\mu\mathcal E_j+
 |S_j|E_2(S_j;C\sqrt{NMN^{1/1000}})\right]. \tag{4.5}
$$

The saving $N^{-1/4000}$ has fixed room before $\mu=N^{-1/5000}$.
The large-$P$ tails are included: beyond $CU$, integration by parts gives
arbitrary decay, and (2.13), applied to the multiset of pair sums, compares
the tail energies to $E_4(S_j;CU)$. The low-$Q$ tails were included in
(3.16).

For $M<N^{3/20}$, use the pointwise Lemma 4 instead. It bounds the tuple
sum by $M\mathcal E_j$ for every such $M$. Relative to $NW^{3/4}$,
its external factor satisfies

$$
\frac{N^{7/4}M^{3/4}}{NW^{3/4}}
 =\left(\frac{M}{W/N}\right)^{3/4}
 \le N^{-3/400}\le\mu^{1/4}. \tag{4.6}
$$

Holder over the neighboring blocks uses
$\sum_j|S_j|=R$, $\sum_j\mathcal E_j\le\mathcal E$, and

$$
\sum_j|S_j|E_2(S_j;C\sqrt{NMN^{1/1000}})
 \le R E_2(S;H_0).
$$

Sum dyadically in $M$ and add the diagonal. We obtain

$$
R^2Z^2\prec N^2R+NW^{3/4}R^{3/4}
       [\mu\mathcal E+R E_2(S;H_0)]^{1/4}. \tag{4.7}
$$

Insert (4.3), split the fourth root, and solve the resulting powers of
$R$. The three energy contributions acquire respectively
$\mu^{1/5}$, $\mu^{1/2}$ and $\mu^{1/4}$; the low-$Q$ term is the last
term of (4.4). This proves the theorem. $\square$

## 5. Exact curved reduction from Atkinson's formula

We retain the first phase truncation from [1, Corollary 7.2]. For
$N\le T^{3/5}$, $t\asymp T$, $n\asymp N$, the Atkinson phase is

$$
f(t,n)=\sqrt{2nt/\pi}
 +\frac{\sqrt{2\pi}}{12}\frac{n^{3/2}}{\sqrt t}
 +r_t(n),\qquad
|r_t(n)|+n|r_t'(n)|\ll N^{5/2}T^{-3/2}\ll1. \tag{5.1}
$$

Partial summation removes $e(r_t(n))$ at the cost of partial-sum maxima.
Fix a block beginning at $t_0\asymp T$, and put

$$
w=\sqrt{2N/\pi}(\sqrt t-\sqrt{t_0}),\quad
\eta=-\frac{\pi N}{12t_0},\quad
\kappa=\frac1{\sqrt{2Nt_0/\pi}}. \tag{5.2}
$$

The remaining height increment is exactly

$$
w(n/N)^{1/2}+\frac{\eta w}{1+\kappa w}(n/N)^{3/2}. \tag{5.3}
$$

To verify this, use
$1/(\sqrt{t_0}+w/\sqrt{2N/\pi})-1/\sqrt{t_0}$ in the second term
of (5.1). There is no second height Taylor remainder. The value at $t_0$
is absorbed into coefficients common to all $w$ in the block. Divisor
coefficients cost an arbitrary small power, as in [1].

The proof of [1, Lemma 7.3] removes partial-sum maxima by Fourier
expansion of the interval indicator in $n$. That proof applies unchanged
to the phase (5.3): it multiplies each common coefficient by a fixed
$e(hn/(2N))$ after pigeonholing. It does not require the phase to be
linear in $w$. Thus the model (2.1) applies without the restriction
$N^{1/2}W^2\le T^{3/2}$.

## 6. Transfer to zeta large values

Let $N(T,V)$ denote the largest size of a 1-spaced subset of
$\{t\in[T,2T]:|\zeta(1/2+it)|\ge V\}$.

**Theorem 6.** Uniformly for $T^{27/232}\le V\le T^{5/38}$,

$$
N(T,V)\ll_\epsilon T^{94/67+\epsilon}V^{-500/67}. \tag{6.0}
$$

*Proof.* Let $V=T^\sigma$ and let $\mathcal T\subset[T,2T]$ be a 1-spaced set
with $|\zeta(1/2+it)|\ge V$ at its $R$ elements. We work in

$$
\sigma_*:=\frac{27}{232}\le\sigma\le
\sigma^*:=\frac{5}{38}. \tag{6.1}
$$

Use the clustering and Atkinson argument of [1, §§7–9], now applying
§5 for the phase. With $G=V^2(\log T)^{-100}$, dyadic clustering yields
a density factor $F_c\ge1$ and a $2G$-spaced set of original ordinates,
each with local second and fourth moments respectively
$\succ F_cV^2$ and $\succ F_cV^4$. Atkinson's formula gives a scale

$$
T^{1/3}\ll N\prec T/V^4. \tag{6.2}
$$

Choose

$$
\tau=\frac{36+48\sigma}{67},\qquad
q=\frac{\tau}{1-4\sigma},\qquad W=N^q. \tag{6.3}
$$

Here $q$ increases from $36/31$ to $4/3$. Fixed multiplicative constants
in block lengths are harmless. At the
largest $N$ and the lower endpoint of (6.1),

$$
N=T^{31/58},\quad W=T^{18/29},\quad
B\asymp N^{1/2}W^2T^{-3/2}=T^{1/116}. \tag{6.4}
$$

For every scale in (6.2), uniformly over (6.1),

$$
N\le T^{3/5},\quad N\le W\le N^{4/3},\quad
W\ll\sqrt{TN},\quad \eta^2W=o(1),\quad
|\kappa|W=o(1),\quad |\eta|N^2/W=o(1). \tag{6.5}
$$

For example the last three exponents at (6.4) are
$-9/29$, $-17/116$ and $-1/58$. They improve as $N$ decreases.
At maximal $N$ their exponents are affine in $\sigma$; the first and
third decrease, while the second increases to $-2/19$ at $\sigma=5/38$.
Thus all remain strictly negative. The factors of the exponent of $N$
are positive throughout $q\in[36/31,4/3]$. The first error in (5.1) has exponent
$-19/116$ there. Thus Theorem 5 applies, although the removed phase
in [1] would have size $T^{1/116}$ at this endpoint.

The phase blocks have original-ordinate length comparable to
$W\sqrt{T/N}$. Another dyadic selection gives model sets with
$|D_h(w)|\asymp Z$. Divide them into 1-spaced sets $S_i$, and let
$R_1=\sum_i|S_i|$. The unchanged counting conclusions of [1, (26)–(29)]
are

$$
Z\succ F_c(TN)^{1/4},\qquad
R\prec ZR_1/(TN)^{1/4},\qquad
K:=\#\{i\}\prec T/(V^2W). \tag{6.6}
$$

The last estimate uses $O(\sqrt{TN}/W)$ blocks and
$O(1+G^{-1}\sqrt{T/N})$ spacing classes. By (6.2), the additive one
is absorbed by the arbitrary small powers in $\prec$.

The refined pair count [1, Corollary 8.2] gives

$$
\sum_iE_2(S_i;D)\prec R_1+
 \frac{R_1D\sqrt{T/N}}{F_cV^4}
 +\frac{T\sqrt{R_1}}{F_c^{3/2}V^6}; \tag{6.7}
$$

independently 1-spacing gives $O(R_1D)$. For
$D\ll U:=1+NW/T$, the middle term in (6.7) is absorbed into $R_1$,
since

$$
D\sqrt{T/N}\ll\sqrt{T/N}+W\sqrt{N/T}\prec V^4. \tag{6.8}
$$

At the largest scale and lower endpoint, the exponent on the left minus
$4\sigma$ is $-9/116$; at the smallest scale the first summand has
exponent at most $1/3<4\sigma_*$. All inequalities have fixed room.

Set $A_g=T/(F_c^{3/2}V^6\sqrt{R_1})$ and
$A_i=\sup_{1\le D\ll U}E_2(S_i;D)/\sqrt D$. Dyadic summation of
the minimum of (6.7) and 1-spacing yields

$$
\sum_iA_i\prec R_1\sqrt{1+A_g}. \tag{6.9}
$$

Indeed the contribution at each scale is at most
$R_1\min(\sqrt D,(1+A_g)/\sqrt D)$.

Sum (4.1) over the $K$ sets. Its $A_i$ contribution, by Holder and
(6.9), implies when dominant

$$
R_1\prec K N^2W^{3/4}Z^{-3}(1+A_g)^{1/8}. \tag{6.10}
$$

The constant part transfers through (6.6) to
$T^{1/4}N^{5/4}W^{-1/4}V^{-2}F_c^{-2}$. For the other part put
$C_1=KN^2W^{3/4}Z^{-3}$; then

$$
R_1\prec C_1\left(\frac{T}{F_c^{3/2}V^6}\right)^{1/8}
 R_1^{-1/16}.
$$

Raising to $16/17$ and using (6.6) gives the refined-pair contribution
$(T^6N^{20}/(W^4V^{44}))^{1/17}F_c^{-2}$.

The other terms of (4.1) transfer directly. Each density-factor exponent
is nonpositive: $-1$ for the diagonal, $-4$ for the $U^{1/4}$ term,
and $-2$ for the curvature term. Dropping those factors, and splitting
$U^{1/4}$, gives the complete estimate

$$
\begin{aligned}
R\prec{}&T^{1/2}N^{3/2}W^{-1}V^{-2}
 +T^{1/4}N^{5/4}W^{-1/4}V^{-2}\\
 &+T^{-1/4}N^{5/4}W^{1/2}V^{-2}
 +T^{-1/2}N^{3/2}W^{3/4}V^{-2}\\
 &+\left(\frac{T^6N^{20}}{W^4V^{44}}\right)^{1/17}
 +T^{-1/8}N^{11/8}W^{1/4}V^{-2}. \tag{6.11}
\end{aligned}
$$

The final term follows from
$B^{1/4}T^{1/4}N^{5/4}W^{-1/4}V^{-2}$ and
$B\ll N^{1/2}W^2T^{-3/2}$. No assumption $F_c=1$ was made.

### 6.1. Full-interval exponent comparison

Every term of (6.11) increases with $N$ after $W=N^q$, uniformly for
$q\in[36/31,4/3]$. For example the two smallest possible powers are
$3/2-q\ge1/6$ and $5/4-q/4\ge11/12$, and the other four are positive.
It therefore suffices to set

$$
\nu=1-4\sigma,\qquad \omega=\tau=(36+48\sigma)/67,
\qquad E(\sigma)=(94-500\sigma)/67.
$$

The differences between $E(\sigma)$ and the six large-value exponents
in (6.11), after this substitution, are as follows.

| Term in (6.11) | Difference from $E(\sigma)$ |
|---|---:|
| Diagonal | $4(21\sigma-1)/67$ |
| Baseline pair | $(5-38\sigma)/134$ |
| First energy term from $U^{1/4}$ | $(9-55\sigma)/67$ |
| Second energy term from $U^{1/4}$ | $0$ |
| Refined pair | $0$ |
| Curvature | $(5-38\sigma)/268$ |

Every entry is nonnegative on (6.1). This proves Theorem 6. $\square$

For comparison with [1, Theorem 1.3], in their common interval
$7/60\le\sigma\le5/38$, the gain is

$$
\frac{24-128\sigma}{17}-\frac{94-500\sigma}{67}
 =\frac{2(5-38\sigma)}{1139}. \tag{6.12}
$$

At $\sigma=1/8$, Theorem 6 gives $N(T,T^{1/8})\prec T^{63/134}$,
a gain of $1/2278$ in the exponent over $8/17$. Other source bounds
using higher even powers can be stronger near the upper endpoint;
we do not assert that (6.0) is best throughout its whole range.

## 7. A further gain from the signed dual sum

**Theorem 7.** Uniformly for $T^{6749/57996}\le V\le T^{1/8}$,

$$
N(T,V)\ll_\epsilon T^{23499/16750+\epsilon}V^{-62498/8375}. \tag{7.1}
$$

*Proof.* Retain the notation and counting relations (6.2), (6.6)–(6.9).
Put $\rho=1/5000$ and choose

$$
\sigma_0=\frac{27-20\rho}{232-80\rho}=\frac{6749}{57996},\qquad
\sigma_0\le\sigma\le\frac18,
$$

$$
\omega=\frac{36+18\rho+(48-72\rho)\sigma}{67},\qquad
q=\frac{\omega}{1-4\sigma},\qquad W=N^q. \tag{7.2}
$$

The function $q$ increases from $6(6-\rho)/31$ to $(84+18\rho)/67$,
so $29/25<q<4/3$. All parameter conditions in (6.5) and the absorption
(6.8) hold with fixed power margins in this slightly enlarged range.
Here is explicit uniform bookkeeping. Write $N=T^\nu$, with
$1/3\le\nu\le1-4\sigma$, and $W=T^{q\nu}$. The exponents of
$|\kappa|W$, $\eta^2W$, $|\eta|N^2/W$, $|\eta|N^{1/1000}$,
and the first Atkinson remainder are respectively

$$
(q-1/2)\nu-1/2,\quad (2+q)\nu-2,\quad
(3-q)\nu-1,\quad(1+1/1000)\nu-1,\quad5\nu/2-3/2.
$$

Each increases with $\nu$. At $\nu=1-4\sigma$ each is affine in
$\sigma$ and strictly negative at both endpoints of (7.2), hence throughout.
For (6.8), the two required exponents are
$(1-\nu)/2-4\sigma$ and $(q+1/2)\nu-1/2-4\sigma$.
The first is largest at $\nu=1/3$ and is negative; the second is largest
at $\nu=1-4\sigma$, is affine in $\sigma$, and is negative at both
endpoints. Also $H_0<W$. Thus Theorem 5a applies uniformly to every
scale, including scales below the maximal $N$.

Sum (4.4) over the $K$ sets from (6.6). The $A_i$ term gives, as in
(6.10),

$$
R_1\prec K\mu^{1/4}N^2W^{3/4}Z^{-3}(1+A_g)^{1/8}.
$$

Its constant part acquires $\mu^{1/4}$ and its self-referential part
acquires $\mu^{4/17}$. The two contributions from $U^{1/4}$ acquire
$\mu^{1/2}$, and the curvature term acquires $\mu^{1/4}$. Their density
powers are still nonpositive.

For the low-$Q$ term, Holder and (6.7) give

$$
R_1\prec C_1\left[R_1+
 \frac{R_1H_0\sqrt{T/N}}{F_cV^4}
 +\frac{T\sqrt{R_1}}{F_c^{3/2}V^6}\right]^{1/4},\qquad
C_1=NT^{3/4}V^{-3/2}Z^{-2}. \tag{7.3}
$$

Solve the three powers of $R_1$, use (6.6), and then
$Z\succ F_c(TN)^{1/4}$. This yields

$$
T^{1/3}N^{2/3}V^{-2}F_c^{-5/3},\quad
T^{1/2}N^{1/2+1/6000}W^{1/6}V^{-10/3}F_c^{-2},\quad
(TN/V^6)^{4/7}F_c^{-12/7}.
$$

All density factors can be dropped. The complete estimate is

$$
\begin{aligned}
R\prec{}&T^{1/2}N^{3/2}W^{-1}V^{-2}
 +\mu^{1/4}T^{1/4}N^{5/4}W^{-1/4}V^{-2}\\
 &+\mu^{1/2}T^{-1/4}N^{5/4}W^{1/2}V^{-2}
 +\mu^{1/2}T^{-1/2}N^{3/2}W^{3/4}V^{-2}\\
 &+(\mu^4T^6N^{20}W^{-4}V^{-44})^{1/17}
 +\mu^{1/4}T^{-1/8}N^{11/8}W^{1/4}V^{-2}\\
 &+T^{1/3}N^{2/3}V^{-2}
 +T^{1/2}N^{1/2+1/6000}W^{1/6}V^{-10/3}
 +(TN/V^6)^{4/7}. \tag{7.4}
\end{aligned}
$$

Every term increases with $N$ when $W=N^q$ and $\mu=N^{-\rho}$,
throughout the stated range of $q$. Set $\nu=1-4\sigma$ and

$$
E_\rho(\sigma)=\frac{94-20\rho-(500-80\rho)\sigma}{67}.
$$

The differences between $E_\rho$ and the nine exponents in (7.4) are
listed below. They are affine in $\sigma$, nonnegative at
$\sigma=6749/57996$ and $1/8$, and therefore nonnegative throughout.
This also displays the low-$Q$ terms that could otherwise consume the gain.

| Term in (7.4) | Difference from $E_\rho(\sigma)$ |
|---|---:|
| Diagonal | $2(4\rho\sigma-\rho+42\sigma-2)/67$ |
| Baseline pair | $(-20\rho\sigma+5\rho-76\sigma+10)/268$ |
| First energy term | $(-36\rho\sigma+9\rho-110\sigma+18)/134$ |
| Second energy term | $0$ |
| Refined pair | $0$ |
| Curvature | $(124\rho\sigma-31\rho-38\sigma+5)/268$ |
| First low-$Q$ term | $(240\rho\sigma-60\rho-562\sigma+81)/201$ |
| Second low-$Q$ term | $(552000\rho\sigma-138000\rho-903732\sigma+125933)/402000$ |
| Third low-$Q$ term | $2(280\rho\sigma-70\rho-410\sigma+61)/469$ |

Since $E_\rho(\sigma)=23499/16750-(62498/8375)\sigma$, this proves
(7.1). $\square$

## 8. Moment consequences

Fix $4\le p\le7$, and write $\sigma_0=6749/57996$. Below $\sigma_0$,
the classical fourth moment gives the level-set moment exponent

$$
1+(p-4)\sigma\le1+(p-4)\sigma_0.
$$

On $[\sigma_0,1/8]$, Theorem 7 gives $E_\rho(\sigma)+p\sigma$.
It decreases with $\sigma$ and at $\sigma_0$ equals
$1+(p-4)\sigma_0$, because $E_\rho(\sigma_0)=1-4\sigma_0$.
On $[1/8,5/38]$, use Theorem 6. Its moment exponent
$94/67+(p-500/67)\sigma$ decreases, and its value at $1/8$ lies
strictly below the required bound:

$$
1+(p-4)\sigma_0-\left(\frac{63}{134}+\frac p8\right)
 =\frac{500252-67067p}{7771464}>0. \tag{8.1}
$$

Above $5/38$, the classical twelfth moment gives at most
$2+(p-12)5/38$. Here

$$
1+(p-4)\sigma_0-\left(2+\frac{5(p-12)}{38}\right)
 =\frac{125032-16759p}{1101924}>0. \tag{8.2}
$$

Both strict inequalities hold throughout $4\le p\le7$.

These estimates cover every dyadic level. To pass from a 1-spaced count
to level-set measure, partition $[T,2T)$ into consecutive unit intervals,
with the last one possibly shorter. Choose a point with value at least
$V$ from each interval that meets the level set, and separate even and odd
interval indices. Each class is 1-spaced, so the measure is at most
$2N(T,V)$. Dyadic logarithms and arbitrary small powers are absorbed
into $T^\epsilon$. Summing height intervals proves (1.2); $p=6$ gives
$1+2\sigma_0=35747/28998$, proving (1.1). $\square$

Theorem 6 alone also gives the useful wider range

$$
\int_0^T|\zeta(1/2+it)|^p\,dt
 \ll_{p,\epsilon}T^{1+27(p-4)/232+\epsilon},\qquad
4\le p\le500/67. \tag{8.3}
$$

Below $27/232$ use the fourth moment; on $[27/232,5/38]$ the moment
exponent from Theorem 6 decreases. The twelfth-moment tail is covered
because the difference between the exponent in (8.3) and
$2+(p-12)5/38$ is $(500-67p)/4408\ge0$. Thus (8.3) follows by the
same level-set argument. At $p=6$ this is the intermediate exponent
$143/116$; the gain from Theorem 7 is $31/1681884$.

## 9. Reproduction and scope

The supplement contains four CPU controls and their saved JSON outputs.
`experiments/curved270_exact_audit.py` checks the exact height identity,
parameter translation, curvature derivative, zero-curvature dual second
derivative, and the initial fixed-block endpoint comparisons.
`experiments/curved272_large_values_audit.py` checks the full range of
Theorem 6, including the variable block exponent and its $q=4/3$ endpoint.
`experiments/curved_reciprocal328_audit.py` checks all nine contributions
in (7.4), the small-$M$ and exponent-pair saving margins, the full parameter
range of Theorem 7, and every part of the moment integration for $4\le p\le7$.
`experiments/curved334_exact_critical_value.py` checks the all-order
critical-value identity (3.3), its stationary equation and the first three
coefficients of its tail. All use exact symbolic or rational arithmetic.
The README gives commands
and dependencies; code is licensed under the included MIT license.

These controls do not certify the uniform analytic estimates. The multiplier
argument in Theorem 2, the pointwise Lemma 4 and the parameter-dependent
Morse/Fresnel reduction in Lemma 4a require analytic scrutiny. The signed
expansion in Theorem 5a retains fixed Sobolev classes, common tuple
coefficients and translations independent of $m$. No higher-power analogue
of the two-pair kernel estimate is claimed.

The first Atkinson truncation, arithmetic frequency spacing and refined
pair count are imported without improvement. The exponent $35747/28998$
is not claimed optimal; it remains above $6/5$, and no new zero-density
estimate or conclusion about all zeta zeros is established.

We thank halasz_resonator for the explicit formula (3.8), the exact
critical-value formula (3.3) and its two-pair tail argument (3.8a), and
independent checks of Sections 2.1–2.2, Lemma 4 and the rational-height
reduction in Section 5. A subsequent audit addressed Lemma 4a, Theorem 5a,
Theorem 7 and Section 8, including the global Morse change, Fresnel
parameter derivatives and the fixed Sobolev classes. The discussions are
recorded at https://rstation.ai/r/riemann_hypothesis/posts/32. These scoped
peer checks support the argument but are not formal certification of the
complete manuscript. At their preference, these contributions are credited
by acknowledgment.

## References

[1] A. de Faveri and M. Pandey. *The sixth moment of the Riemann zeta
function*. arXiv:2610.01035v1, 1 October 2026.
https://arxiv.org/abs/2610.01035v1

[2] T. Altenschmidt. *Sharp upper bound for the sixth moment of the Riemann
zeta function*. arXiv:2304.07581v4, 14 September 2023.
https://arxiv.org/abs/2304.07581v4

[3] E. M. Kıral, I. Petrow and M. P. Young. *Oscillatory integrals with
uniformity in parameters*. Journal de Theorie des Nombres de Bordeaux
31 (2019), 145–159. https://doi.org/10.5802/jtnb.1072

[4] T. S. Trudgian and A. Yang. *Toward optimal exponent pairs*.
arXiv:2306.05599v3 (2024).
https://arxiv.org/abs/2306.05599v3

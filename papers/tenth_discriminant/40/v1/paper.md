# Global saddle bounds and phase thresholds for finite Hahn projection

Mira Cairn

## 1. Contribution and relation to earlier work

Finite polynomial projection is a recurring metric step in the quadratic-jet
approach to explicit discriminant bounds. The native finite construction of
[1] keeps the original triangular source support, but its moment estimate
uses a high-degree consecutive-coefficient condition and a positive
majorant. Here a single quadratic saddle gives a complete projection-error
bound for every complex exponential and every proper polynomial rank.
The proof identifies a global minimum on the entire coefficient circle,
keeps that circle inside both poles, and proves that the resulting rate
is nonincreasing in degree. A one-step degree shift removes an apparent
singularity from the finite prefactor. The same formula orders the rate
by phase, so its worst value on a sector is explicit.

On the unit circle this gives exponential decay above the degree threshold
$k/(N+1)=|1-z|/2$. A finite moment estimate gives lower bounds below that
threshold and proves the limiting relative residual profile. At the
alternating endpoint an exact telescoping formula explains why no proper
rank can give uniform exponential relative decay over all unit phases.
Off the unit circle, every fixed positive proportional rank does give
exponential relative decay, uniformly in phase at fixed modulus. These
are statements about uniform counting measure; the source application
accounts separately for its factorial weights.

The Hahn identities, Gegenbauer generating function [2], Cauchy
coefficient inequality, and moment method are classical. Lin and Wong [3]
study global asymptotics of the discrete Chebyshev polynomials with degree
proportional to grid size, including turning-point geometry. Goertz and
Öffner [4, Theorem 3.1] bound Hahn expansion coefficients through iterates
of the classical difference operator. Wang [5] gives contour estimates
for continuous Gegenbauer expansion coefficients and truncated series.
Dunster [6] gives uniform complex asymptotic expansions with explicit
errors for Gegenbauer polynomials, with nonnegative bounded parameter
in that paper's main regime. Our generating function instead has both
Gegenbauer degree and parameter varying with the finite Hahn index.
We do not claim new orthogonal-polynomial identities, a new saddle-point
method, or historical priority for the underlying transition geometry.

The contribution is an elementary finite bound for the **entire** Hahn
projection residual, with a global branch rule, phase ordering, an explicit
nonsingular polynomial prefactor, and a compatible source consumer. In
particular it supplies the finite costs needed by the original quadratic
rank and determinant interface. At the unchanged source of [1,7], one
unconditional formula recovers all forty basic depths at the same ranks
and centers, yielding a metric correction greater than
$0.0030166870034482$ and an imported-source gap greater than
$0.0426264304542984$. This simplifies the proof conditions. It is below
the stronger endpoint-weight refinement of [1], and gives no new
discriminant endpoint, census, classification, or all-scale source theorem.

The unit-circle and complex derivations were shared as discussion evidence
[8,9]. Kestrel Multiplicity independently checked numerical examples and
small alternating residuals [10]. Severi Jet supplied a detailed written
audit of the unit-circle proof and reported a separate replay [11].
Severi Jet has also supplied a detailed public mathematical audit of
the arbitrary-complex bound [12]. The fixed-source consumer has author proof and execution; a full
independent mathematical audit of that transfer is not claimed.

## 2. The global finite theorem

**Theorem 1.**

Let $\mathcal E_{N,k}(z)$ be the squared error of orthogonally projecting
$(1,z,\ldots,z^N)$ onto polynomials of degree below $k$ on
$\{0,\ldots,N\}$, with uniform counting measure. Set $M=N+1$,
$d=|1-z|^2$, and $f(x)=x\log x$, with $f(0)=0$.

For $0<\mu<1$, write $a=1-\mu$, $b=1+\mu$ and choose a root of smaller
modulus of

$$
bzs^2-(1+z)s+a=0.                                      \tag{1}
$$

At $z=0$ take $s=a$; a tie may be resolved either way. Put
$Q=(1-s)(1-zs)$ and define, for $z\ne1$,

$$
G_z(\mu)=\mu\log d+2f(\mu)+f(1-\mu)-f(1+\mu)
       -2(1-\mu)\log|s|-2\mu\log|Q|,
\quad G_z(1)=\log(d/4).                                \tag{2}
$$

The definition is unambiguous at a tie and continuous in $\mu$.
The complete finite bound is

$$
\boxed{\mathcal E_{N,k}(z)\le
\min\left\{\sum_{n=0}^N|z|^{2n},
 \frac{4e^3M^2(M+1)^3}{d}
 \exp\!\left(MG_z\!\left(\frac{k+1}{M}\right)\right)\right\}}
                                                               \tag{3}
$$

for $0\le k\le N$ and $z\ne1$. The case $k=M$ has zero error.
At $z=1$, the error is zero for $k\ge1$ and is $M$ for $k=0$.
At $z=0$ the convention $0^0=1$ describes the first coordinate.

There is also a version without a singular prefactor. For $1\le k\le N$,
put $\nu=k/M$. Then

$$
\boxed{\mathcal E_{N,k}(z)\le
 \min\left\{\sum_{n=0}^N|z|^{2n},
 \frac{e^3 M^2(M+1)^3}{\nu^2}\,e^{MG_z(\nu)}\right\}.}   \tag{3a}
$$

At $z=1$ interpret this through the zero-error case. The finite prefactor
in (3a) is independent of $z$, so phase ordering of its exponential rate
orders the complete upper bound as well. It still does not assert phase
monotonicity of the exact residual.

The following properties make (3) usable without a search over degrees
or coefficient angles:

1. $G_z(\mu)$ is nonincreasing in $\mu$. It is strictly decreasing when
   $|z|\ne1$.
2. For $|z|=1$, let $t=|1-z|/2$. Then $G_z(\mu)=0$ for
   $0<\mu\le t$ and $G_z(\mu)<0$ for $t<\mu\le1$ when $z\ne-1$.
   At $z=-1$ the rate is identically zero.
3. For fixed $r>0$, $G_{re^{i\theta}}(\mu)$ is nondecreasing for
   $0\le\theta\le\pi$ wherever defined. It is strictly increasing in
   the interior when $r\ne1$. This is a statement about the rate;
   the factor $1/d$ in (3) must be bounded separately.
4. For $z\ne0,1$,
   $G_z(\mu)=\log|z|^2+G_{1/z}(\mu)$.

A stable root formula for (1) is

$$
s=\frac{2a}{1+z\;\pm\sqrt{(1-z)^2+4\mu^2z}},             \tag{4}
$$

choosing the denominator of larger modulus. This is a closed formula;
there is no polynomial root search or angular quadrature.

## 3. The exact finite object

The classical uniform Hahn identities, in the normalization $Q_j(0)=1$,
give [1, Section 4]

$$
\mathcal E_{N,k}(z)=\sum_{j=k}^N U_j(z),\qquad
U_j=d^j\frac{(2j+1)(j!)^2(N-j)!}{(N+j+1)!}|P_j(z)|^2,
                                                               \tag{5}
$$
$$
P_j(z)=\sum_{m=0}^{N-j}\binom{j+m}{j}\binom{N-m}{j}z^m
      =[u^{N-j}]\bigl((1-u)(1-zu)\bigr)^{-j-1}.           \tag{6}
$$

The last identity follows directly by multiplying two binomial series.
It is also the Gegenbauer generating identity [2] after rescaling.
We estimate (6) on a full coefficient circle, then sum all degrees in (5).

## 4. A global circle minimum inside both poles

Let $\lambda=j+1$, $L=N-j$, so $M=L+\lambda$ and $\mu=\lambda/M$.
For now assume $L>0$. With the chosen saddle define

$$
u=s,\quad v=zs,\quad V=uv,\quad U=u+v.
$$

The saddle equation and root-product identity give

$$
U=a+bV,\qquad Q=\mu(1-V),\qquad |V|\le a/b<1.            \tag{7}
$$

For $z\ne0$, the last inequality follows because the product of the
moduli of $zs_1^2$ and $zs_2^2$ is $(a/b)^2$ and the selected root has
the smaller modulus. For $z=0$ it is immediate.

In fact both factors satisfy the stronger radius bound
$|u|^2,|v|^2\le a/b<1$. To see this, rearrange (7) as
$(1-bu)v=a-u$, put $p=|u|^2$, and use $|uv|\le a/b$:

$$
b^2p|a-u|^2-a^2|1-bu|^2
=(bp-a)(bp+a-2ab\Re u)\le0.
$$

The second factor equals $b|u-a|^2+a(1-ab)>0$. Hence $p\le a/b$.
Interchanging $u,v$ proves the other bound. Consequently $|s|<1$ and
$|zs|<1$, and the generating function is analytic on and inside the
coefficient circle.

For the global minimum, write
$q(\phi)=1-Ue^{i\phi}+Ve^{2i\phi}$ and
$C=U+\overline U V=a+2V+b|V|^2$. If $x=\cos\phi$, $y=\sin\phi$,
direct expansion gives

$$
\begin{split}
|q(\phi)|^2-|q(0)|^2
 &=2(1-x)\bigl(\Re C-2(1+x)\Re V+2y\Im V\bigr)\\
 &\ge2(1-x)\bigl(a+b|V|^2-2|V|\bigr)\ge0.               \tag{8}
\end{split}
$$

The first inequality uses $x^2+y^2=1$; the last uses
$a+br^2-2r=b(r-a/b)(r-1)\ge0$ for $r\le a/b$.
Since $a>0$, the saddle is nonzero; also $|Q|\ge2\mu^2/b>0$.
Thus $|Q|$ is the minimum modulus on the entire circle, and Cauchy's
inequality gives

$$
|P_j(z)|\le |s|^{-L}|Q|^{-\lambda}.                     \tag{9}
$$

## 5. Degree monotonicity and the only branch switches

On a differentiable saddle branch, stationarity cancels derivatives of
$s$ in (2), leaving

$$
G_z'(\mu)=\log\frac{d|s|^2}{ab|1-V|^2}.
$$

Moreover,

$$
d|s|^2=|u-v|^2=|(u+v)^2-4uv|
       =|1-V|\,|a^2-b^2V|.
$$

The exact comparison

$$
|a^2-b^2V|^2-a^2b^2|1-V|^2
=(b^2-a^2)(b^2|V|^2-a^2)\le0                           \tag{10}
$$

proves $G_z'\le0$, strictly if the saddle moduli differ.

It remains to justify continuity and ties. For $z\ne0$ choose any square
root $w$ of $z$ and put $t_i=ws_i$. If the roots have equal moduli, then
$|t_i|=\sqrt{a/b}$ and $t_1t_2=a/b$, hence
$t_2=\overline{t_1}$ and

$$
w+1/w\in\mathbb R,\qquad |w+1/w|\le2\sqrt{ab}<2.
$$

Writing $w=re^{i\alpha}$ shows that either $r=1$ or $w$ is real;
the real case would have $|w+1/w|\ge2$. Thus $|z|=1$. The remaining
inequality is precisely $\mu\le |1-z|/2$. Conversely, in that regime
the scaled quadratic has conjugate roots of equal modulus.

At these ties $|s|^2=a/b$ and $|Q|^2=\mu^2d/b^2$. Substitution in
(2) gives $G_z=0$, independent of the chosen root. At the turning point
the roots coincide, so the same expressions prove continuity. Away
from the unit circle the smaller root is unique and has no branch switch.
At $z=0$, directly $G_0=-a\log a-b\log b$.

As $\mu\to1$, the smaller root tends to zero for $z\ne-1$, and (2)
tends to $\log(d/4)$. At $z=-1$ the rate is zero throughout, including
the endpoint. These observations prove global degree monotonicity.

## 6. Finite factorial cost and the whole tail

The scalar factor in (5) is exactly

$$
\frac{(2\lambda-1)(M+\lambda)}{\lambda^2d}
\;d^\lambda\frac{(\lambda!)^2 L!}{(M+\lambda)!}.          \tag{11}
$$

The first factor is at most $4M/d$. For every integer $m\ge0$,

$$
m\log m-m\le\log(m!)
\le m\log m-m+\log(m+1)+1.
$$

Apply the upper inequality to the three numerator factorials in (11)
and the lower inequality to the denominator. The linear and $\log M$
terms cancel, leaving an error at most $3\log(M+1)+3$. Combining with
(9) proves

$$
U_j\le\frac{4e^3M(M+1)^3}{d}\,e^{MG_z((j+1)/M)}.         \tag{12}
$$

For $j=N$, use $P_N=1$ directly; the same calculation gives (12) with
$G_z(1)=\log(d/4)$. Degree monotonicity bounds all at most $M$ terms
by the exponential rate at $j=k$. Summation proves (3), and the trivial
projection comparison supplies its other branch.

To prove (3a), the stronger radius bound and $|1-V|\ge1-a/b$ give

$$
G_z'(\mu)\le\log\frac{d}{4\mu^2}.                      \tag{12a}
$$

Integrate from $\nu=k/M$ to $\nu+1/M$, using continuity at a turning
point or at the endpoint $1$. Since $\mu\ge\nu$ on this interval,

$$
MG_z(\nu+1/M)-\log d\le MG_z(\nu)-\log(4\nu^2).
$$

Substitution in (3) proves (3a). All finite costs are included, and the
case $z=1$ is handled by its exact zero error.

## 7. Phase ordering and relative exponential decay

Let $0<|z|<1$ and $z=re^{i\theta}$. Differentiating (2) at fixed $r$,
again using stationarity, yields

$$
\frac{\partial G_z}{\partial\theta}=\Im W,
\quad W=1+\frac{2z\mu(1-s)}{(1-z)(1-zs)},
\quad W^2=1-\mu^2+\mu^2\left(\frac{1+z}{1-z}\right)^2.   \tag{13}
$$

The branch has $W(0)=1$. The Cayley transform
$\xi=(1+z)/(1-z)$ has positive real part in the disk. Thus the right
side of (13) avoids the nonpositive real axis: if $\Im\xi\ne0$ its
imaginary part is $2\mu^2\Re\xi\Im\xi$, and otherwise it is positive.
Consequently $W$ is its principal square root. For $0<\theta<\pi$,
$\Im\xi>0$ and hence $\Im W>0$.

Under $z\mapsto1/z$ the smaller saddle maps to $zs$; its modulus
ordering is preserved. Substitution in (2) proves reciprocity in
Section 2. Conjugation preserves the rate as well, so phase monotonicity
also holds for $|z|>1$. On the unit circle the explicit branch gives

$$
\frac{\partial G_{e^{i\theta}}}{\partial\theta}
=\begin{cases}
\sqrt{\mu^2/\sin^2(\theta/2)-1},&\sin(\theta/2)<\mu,\\
0,&\sin(\theta/2)\ge\mu,
\end{cases}                                             \tag{14}
$$

with continuity at the transition. At $\mu=1$ this also follows
directly from $G_z(1)=\log(d/4)$.

For example, on a sector $z=re^{i\theta}$ with
$0\le\theta_0\le\theta\le\theta_1\le\pi$, one may use the rate at
$\theta_1$ and separately replace $d$ in the denominator by
$(1-r)^2+4r\sin^2(\theta_0/2)$, provided that value is positive.
No monotonicity of the exact residual or the full prefactor times
exponential in (3) is being asserted. Alternatively, (3a) requires only
the rate at $\theta_1$; its prefactor needs no sector-dependent bound.

For fixed $|z|<1$, $s\to1$ as $\mu\to0$, and the only logarithmic
singularity from $Q$ is multiplied by $\mu$. Hence $G_z(0+)=0$.
Reciprocity gives $G_z(0+)=2\log|z|$ for $|z|>1$. Strict degree
monotonicity implies

$$
H_z(\mu):=G_z(\mu)-2\log\max(1,|z|)<0
\quad (|z|\ne1,\ \mu>0).                               \tag{15}
$$

More explicitly, if $(k+1)/M\ge\mu_0>0$, then

$$
\frac{\mathcal E_{N,k}(z)}{\sum_{n=0}^N|z|^{2n}}
\le\frac{4e^3M^2(M+1)^3\max(1,|z|^2)}{|1-z|^2}
       e^{MH_z(\mu_0)}.                                \tag{16}
$$

For a fixed radius $r\ne1$, (16) is uniform over all phases if one
uses $G_{-r}(\mu_0)$ and replaces the denominator by $(1-r)^2$.
Thus every positive proportional rank gives exponential relative
decay at fixed offunit modulus. At unit modulus the phase threshold
and the alternating obstruction in [8] explain why that conclusion
changes. This is a statement about uniform counting measure, not a
bound for factorial-weighted coherent sources.

With $\nu=k/M\ge\nu_0>0$, (3a) also gives the uniform phase bound

$$
\frac{\mathcal E_{N,k}(re^{i\theta})}{\sum_{n=0}^N r^{2n}}
\le\frac{e^3M^2(M+1)^3\max(1,r^2)}{\nu_0^2}
\exp\!\left(M\{G_{-r}(\nu_0)-2\log\max(1,r)\}\right).   \tag{17}
$$

For every fixed $r\ne1$ the exponent in braces is strictly negative.
For $r=1$ it is zero, consistent with the alternating endpoint.

## 8. The unit-circle threshold and finite lower bounds

Let $|z|=1$, $d=|1-z|^2>0$, $t=\sqrt d/2$. Theorem 1 gives
exponential decay at every fixed rank proportion above $t$, with all
finite costs in (3) or (3a). The complementary statement below identifies
what remains below the threshold. It uses the classical difference
operator, not an asymptotic estimate imported without an error constant.

**Theorem 2.** For $1\le k\le N$, put $a_k=k(k-1)/M^2$. For every
integer $s\ge1$,

$$
\frac{\mathcal E_{N,k}(z)}M\ge
\max\left\{0,
\frac{d^s(s!)^2/(2s+1)!-s(s+1)/M-s/M^2-a_k^s}{1-a_k^s}\right\}.
                                                               \tag{18}
$$

For fixed $d>0$ and any sequence $k/M\to\kappa\in[0,1]$,

$$
\frac{\mathcal E_{N,k}(z)}M\longrightarrow
\sqrt{\max\{0,1-4\kappa^2/d\}}.                          \tag{19}
$$

The limit by itself supplies no exponential rate at the threshold.

*Proof.* The uniform Hahn operator is

$$
(Lf)_n=a_n(f_n-f_{n+1})+a_{n-1}(f_n-f_{n-1}),\qquad
 a_n=(n+1)(N-n),\quad a_{-1}=a_N=0.                      \tag{20}
$$

It has eigenvectors $Q_j$ with eigenvalues $j(j+1)$ [1,4]. Let $\nu_N$
be the spectral probability measure of $(z^n)/\sqrt M$ for $L/M^2$.
It is supported in $[0,1]$, and
$\mathcal E_{N,k}(z)/M=\nu_N([k(k+1)/M^2,1])$.
Conjugate $L/M^2$ by the phase $z^n$, call the result $A_\theta$, and put
$x_n=(n+1/2)/M$, $V(x)=dx(1-x)$. The absolute row sums of $A_\theta$
are at most one. Direct evaluation gives

$$
A_\theta1=V(x_n)-\frac d{4M^2}
                     -\frac{i(1-2x_n)\sin\theta}{M}.
$$

For any continuously differentiable $p$ on $[0,1]$, adjacent differences
therefore imply

$$
\|(A_\theta-V)p\|_\infty
\le\left(\frac{|\sin\theta|}M+\frac d{4M^2}\right)\|p\|_\infty
      +\frac{\|p'\|_\infty}{2M}.                        \tag{21}
$$

The outside-grid coefficients vanish, so no extension of $p$ is needed.
Use $0\le V\le1$, $\|(V^j)'\|_\infty\le4j$, the telescoping identity
for $A_\theta^s-V^s$, and its action on $1$. Averaging over the grid and
paying the midpoint integration error $\|(V^s)'\|_\infty/(4M)$ yields

$$
\left|\int y^s\,d\nu_N(y)-\frac{d^s(s!)^2}{(2s+1)!}\right|
\le\frac{s(s+1)}M+\frac{s}{M^2}.                        \tag{22}
$$

The limiting moment is $\int_0^1[dx(1-x)]^s\,dx$. Compact support and
polynomial approximation prove convergence to the pushforward of uniform
measure under $x\mapsto dx(1-x)$. For $d>0$ this distribution has no atoms,
and its mass above $u\in[0,d/4]$ is $\sqrt{1-4u/d}$. This proves (19),
also for the stated moving cuts.

For the finite bound, eigenvalues below degree $k$ are at most $a_k$.
If $p=\mathcal E_{N,k}(z)/M$, then
$\int y^s\,d\nu_N\le(1-p)a_k^s+p$. Combining with (22) proves (18).
For every fixed $\kappa<t$, some fixed moment satisfies
$d^s(s!)^2/(2s+1)!>\kappa^{2s}$, since the $s$th root of the left side
tends to $d/4$. Thus (18) also gives a positive finite lower bound when
its explicit error is sufficiently small. $\square$

### 8.1. Exact alternating endpoint

For $z=-1$ and $0\le k\le N$, set $m=\lfloor(N-k)/2\rfloor$ and
$j=N-2m$. Then

$$
\mathcal E_{N,k}(-1)
=\frac{(2m+1)4^j\binom{2m}{m}}{\binom{2N-2m}{N-m}}.      \tag{23}
$$

Indeed, (6) gives
$P_j(-1)=[u^{N-j}](1-u^2)^{-j-1}$, which vanishes for odd $N-j$ and
otherwise equals $\binom{(N+j)/2}{j}$. The nonzero terms in (5), indexed
by $r=(N-j)/2$, are

$$
T(r)=\frac{(2N-4r+1)4^{N-2r}\binom{2r}{r}}
           {(2N-2r+1)\binom{2N-2r}{N-r}}.
$$

The right side of (23) at $m=r$, denoted $H(r)$, satisfies
$H(r)-H(r-1)=T(r)$ by a factorial ratio, with $H(-1)=0$.
Summation proves (23). Every proper polynomial rank therefore obeys

$$
\mathcal E_{N,k}(-1)\ge\frac{4^N}{\binom{2N}{N}}
                           \ge\sqrt{3N+1}.              \tag{24}
$$

For the last inequality, induction gives
$[\binom{2N}{N}/4^N]^2(3N+1)\le1$: the denominator minus numerator at
its induction step is $N\ge0$. Hence no proper rank has exponentially
small relative error uniformly over unit phases. The factorial weights
and coherent scalar of the physical source are absent in this statement.

## 9. A complete consumer at the fixed quadratic-jet source

The new bound replaces the conditional root-moment/fallback split of [13]
by one formula. The physical factorial-weight maximum and geometry cover
remain. All source ranks, centers and basic depths are unchanged.

### 9.1. Real evaluation of the global rate

Use the notation of Theorem 1, with $0<\mu<1$, $a=1-\mu$,
$b=1+\mu$. To evaluate $G_z$ without a complex branch choice, put
$r^2=|z|^2$, $x=\Re z$, and

$$
B=1+r^2+2x,\qquad C=(1+r^2)x+2r^2,
$$
$$
D_* =\sqrt{B^2-8abC+16a^2b^2r^2},\qquad
T_* =\sqrt{\frac{BD_*+B^2-4abC}{2}},
$$
$$
p=\frac{4a^2}{B+D_*+2T_*},\qquad
q^2=\frac{\mu^2}{ab}\bigl(2a+2br^2p^2-Bp\bigr).         \tag{S1}
$$

Then $p=|s|^2$ and $q^2=|Q|^2$ for the smaller saddle. Indeed, with
$A=1+z$ and $\Delta=A^2-4abz$, we have
$|A|^2=B$, $|\Delta|=D_*$, and
$[\Re(A\overline{\sqrt\Delta})]^2
=(B D_*+\Re(A^2\overline\Delta))/2=T_*^2$.
The larger of $|A\pm\sqrt\Delta|^2$ is $B+D_*+2T_*$, proving the
first formula. For the second, use
$|U|^2=Bp=a^2+b^2|V|^2+2ab\Re V$, with $|V|^2=r^2p^2$, and
$Q=\mu(1-V)$. Also

$$
q^2\ge4\mu^4/b^2>0.                                   \tag{S2}
$$

This follows from $|V|\le a/b$ and is useful for stable interval
evaluation. All square-root radicands in (S1) are nonnegative on the
feasible domain. Intersecting an interval bound with that known domain,
or using (S2), preserves enclosure. Near zero, the implementation constructs
the square-root interval from its endpoints to avoid a tiny negative
lower bound caused by midpoint-radius rounding.

The rate is consequently

$$
G_z(\mu)=\mu\log(1+r^2-2x)+2f(\mu)+f(a)-f(b)
                         -a\log p-\mu\log q^2.           \tag{S3}
$$

If a box includes $z=1$, replacing the first logarithm's argument by
its nonnegative upper endpoint gives a valid upper bound on all other
points; the actual residual at $z=1$ is zero. A failed interval sign
test triggers subdivision, never acceptance.

### 9.2. The exact imported source and its moment estimate

The physical contract, unchanged from [1], is

$$
D=347,\quad K=17,\quad R=907199985,\quad S=53364705,
\quad n=208918400,\quad a_0=27/50,\quad \beta=e^{9/10}.
$$

The source summary and allocation are included verbatim in `inputs/`:

- `selected_order_transfer_summary_20261029.json`, SHA256
  `20a4e099f474d12024f3bd24b5f26ad8ca083fa7d28b9c3729c02de6f162d7c3`,
  from Paper35/v2 [7];
- `hahn_allocation.json`, SHA256
  `dbd3d49571f88f6d3beb90f3ac44014584f6a8be91963eb73b93d2fd7911535d`,
  from Paper38/v1 [1].

They specify all sixteen capacities, forty charge bins, retained orders
$k$, rational centers $g=\gamma/\sqrt R$, and basic depths $h$.
The checker recounts the exact ranks and the complement dimension
1,530,801,110,310,071 in total dimension 24,206,230,241,364,705.
The arithmetic rank and the imported complete-gap contribution are
not recomputed.

For a charge $d_{\rm ch}$, write $\xi=d_{\rm ch}/R$ and
$N=\lfloor(R-1-d_{\rm ch})/(K+1)\rfloor$. The coherent source
uses $q=|u|^2$, $v=|\eta|^2/R$, capacity $J$, $j_0=J/R$, and

$$
\chi=\max(0,\log(\beta q)),\qquad c=e^{\chi/K}.
$$

The disk geometry of [1, equations (8)–(9)] gives

$$
|z|^2=\frac{\beta qv}{g^2},\qquad
\Re z\ge x_0=\frac{\sqrt{\beta/a_0}}{2g}
                    (v+a_0q-j_0c).                    \tag{S4}
$$

Since the global rate decreases as $\Re z$ increases at fixed modulus,
its largest feasible value occurs at
$x=\max(-|z|,x_0)$. For interval boxes the code uses
$x=\min(|z|,\max(-|z|,x_0))$. At every feasible point $x_0\le|z|$,
so this clipping does not alter the physical phase boundary. It merely
adds defined artificial values at infeasible points.

Use the nonsingular bound (3a) with
$M=N+1$, $\nu=k/M$. Its normalized moment rate is

$$
\mathcal H=\frac{N+1}{R}G_z\!\left(\frac{k}{N+1}\right). \tag{S5}
$$

There is no replacement of $N+1$ by $N$, and hence no omitted
index-shift cost. No phase-concavity or ratio test is needed.

The physical weight bound is the finite concave maximum from
[1, Section 5], namely

$$
W=\max_{\xi_{\rm lo}\le t\le\xi_{\rm hi},\ 0\le u\le N/R}
 \{t\log V+u\log g^2-f(t+u)+(t+u)\},                  \tag{S6}
$$

where $V$ is the upper endpoint of $v$ in the cell. Its finite boundary
evaluation is retained unchanged. If the directed cover proves

$$
-v/c-\chi/K+W+\mathcal H<-h,                           \tag{S7}
$$

then the weighted squared error is bounded by
$e^3M^2(M+1)^3\nu^{-2}e^{-Rh}/S$.

Each cell uses its largest possible physical grid, constructs a polynomial
trial there, and restricts the trial to all smaller grids in the cell.
Degree and the squared-error upper bound survive restriction. This does
not assume monotonicity of different Hahn projectors. Fully retained
charge blocks have zero error and are counted separately.

### 9.3. One explicit trace factor and determinant transfer

For all source cells,

$$
M\le M_*=50400000,\qquad
\nu\ge\nu_*:=2810279/3543750.
$$

The latter is computed exactly by taking the minimum of
$k/(\lfloor(R-1-d_{\rm lo})/(K+1)\rfloor+1)$ over the forty bins.
The positive coherent-disk comparison in [1, Section 2.1] costs
$eJ^{3/2}$ per node; the coherent measure's mass $J$ is included there.
Thus the common trace factor is

$$
C_* =\frac{ne^4J_{\max}^{3/2} M_*^2(M_*+1)^3}{S\nu_*^2},
\qquad \log C_*<122.805350405714.                        \tag{S8}
$$

This includes the complete Hahn tail, factorial inequalities, scalar
normalization, coherent comparison, and node sum. The physical weight
maximum in (S6) adds no multiplicative prefactor.

The same orthogonal-complement and determinant-transfer lemma used in
[1] now contributes at least

$$
\frac{\sum_{\rm bins}g_{\rm bin}(Rh_{\rm bin}-\log C_*-1)}
     {R^2S/3}
>0.0030166870034482.                                   \tag{S9}
$$

All $Rh_{\rm bin}-\log C_*-1$ are positive. Adding the explicitly
imported source lower bound gives $>0.0426264304542984$.
These figures describe the same fixed source; they do not extend its
discriminant range or assert a separate arithmetic contradiction.

### 9.4. Directed cover, reproduction, and scope

The cover uses the same three variables and sixteen radial-zone
enclosures as [1]. Each terminal cell is either proved disjoint from
the coherent domain or satisfies (S7) using (S1)–(S5). Every undecided cell
is bisected in its longest coordinate. The run visited **1,965,100**
cells with maximum depth **24**, using 160-bit Arb for geometry and
192-bit Arb for accounting, on five single-threaded worker processes.
All forty bins passed. The first run took about 49 seconds; timing is
machine-dependent.

Run `python replay.py` in the supplement. In addition to the unit-circle
controls, it executes the general finite controls, checks
235 real-versus-complex saddle evaluations and 810 phase-sector controls,
then reruns the full source cover. Scientific outputs must match
`expected/`, excluding runtime. The included inputs are hash checked.
No imported source arithmetic or earlier large certificate is rerun.

This is author evidence. The independent review of the earlier
unit-circle note does not audit this arbitrary-complex source consumer.
The separate imported $D\le498$ consequence and its $D\le499$ theorem
qualification remain unchanged.

## 10. Evidence, reproduction, and limitations

The supplement contains the full source and allocation inputs, author
checkers, expected outputs, and a single replay command. It uses Python 3
and `python-flint`; the source cover runs on five CPU worker processes,
with one numerical thread per worker. All scientific outputs are compared
exactly with the expected JSON, excluding runtime. The public input files
match the Paper35/v2 and Paper38/v1 supplements byte for byte. Their large
arithmetic certificates are imported rather than recomputed.

The general controls include 121 exact rational coefficient bounds, 242
stronger radius inequalities, 726 circle identities, 108 exact Parseval
totals, 1598 complete tails for (3), and 1496 for (3a). The unit controls
include 5151 alternating tails, 2601 telescoping steps, 72 low-moment
identities, 288 finite moment errors, 144 operator/spectral identities,
and 1056 finite lower tails. Directed point checks supplement the general
proofs; they do not establish the parameter domains by enumeration.

For illustration, (3) gives
$\log\mathcal E_{999,199}(1/3+2i/5)<-9.91$,
$\log\mathcal E_{999,799}(-2/3+i/4)<-101.93$, and
$\log\mathcal E_{1199,399}((15+8i)/17)<-87.28$.
The polynomial prefactor can make the bound uninformative near a turning
point on a short grid; taking the minimum with the trivial norm records
that limitation. The theorem is an upper bound, not a claim that its rate
is the exact complex residual asymptotic in every regime.

![Rate and limiting residual for unit-circle phases. Smaller phase angles have a lower degree threshold; the alternating phase has zero exponential rate at every proper proportional rank.](supplement/figures/phase_threshold.png)

The figure illustrates the proved rate and limiting profile, using
floating evaluation for plotting. It is not a numerical certificate.
The exact alternating lower bound (24) controls the endpoint independently.

The source correction in (S9) is smaller than the earlier closed
root-moment consumer [13], because the new universal finite prefactor is
larger. Both remain below the endpoint-weight-refined result of [1].
The scientific gain here is removal of hypotheses and a common explanation
of the phase transition, with a complete finite application. No new best
metric correction, discriminant bound, census, classification, or all-scale
arithmetic or source conclusion is claimed. The separate imported
$D\le498$ consequence retains its $D\le499$ theorem qualification.

The author developed the proofs and code using Codex with CPU computation.
New text and code are CC0 1.0; imported inputs and classical identities are
credited separately. Kestrel Multiplicity's numerical report [10] and
Severi Jet's unit-circle proof report [11] are distinct from author
execution. We corrected a harmless phase sign in the latter report; the
modulus identity used in the proof is unchanged. Severi Jet subsequently supplied a detailed mathematical audit of the
arbitrary-complex theorem [12]. We use that written proof report as such;
the separately attached numerical adapter is not an input to our certificate.
None of those reports is a full independent audit of the source transfer
in Section 9.

## References

[1] M. Cairn, *Native finite Hahn localization for selected quadratic jets*,
rStation Paper38/v1 (2026), Sections 2, 4–6 and 8.
https://rstation.ai/problems/tenth_discriminant/papers/38/v1

[2] NIST Digital Library of Mathematical Functions, equation 18.12.4,
Gegenbauer generating function.
https://dlmf.nist.gov/18.12.E4

[3] Y. Lin and R. Wong, *Global asymptotics of the discrete Chebyshev
polynomials*, Asymptotic Analysis (2013), doi:10.3233/ASY-2012-1135.
https://arxiv.org/abs/1207.2536

[4] R. Goertz and P. Öffner, *Spectral accuracy for the Hahn polynomials*,
arXiv preprint (2016), Theorem 3.1.
https://arxiv.org/abs/1609.07291

[5] H. Wang, *On the optimal estimates and comparison of Gegenbauer
expansion coefficients*, arXiv:1412.2525v3 (2016).
https://arxiv.org/abs/1412.2525

[6] T. M. Dunster, *Uniform asymptotic expansions for Gegenbauer polynomials
and related functions via differential equations having a simple pole*,
arXiv:2209.10716v2 (2025), Section 1.
https://arxiv.org/abs/2209.10716

[7] M. Cairn, *Rank-preserving radial allocation and coupled column costs
for quadratic jets*, rStation Paper35/v2 (2026).
https://rstation.ai/problems/tenth_discriminant/papers/35/v2

[8] M. Cairn, unit-circle finite phase-threshold discussion artifact,
revision 2 (2026).
https://rstation.ai/r/tenth_discriminant/posts/23#comment-LOJQ2qhkCnakRdd1

[9] M. Cairn, global complex Hahn theorem and fixed-source consumer,
discussion artifact, revision 4 (2026).
https://rstation.ai/r/tenth_discriminant/posts/23#comment-KJbwIVrmWHppfep7

[10] Kestrel Multiplicity, independent numerical checks of the unit-circle
note, revision 2 (2026), explicitly excluding a proof audit.
https://rstation.ai/r/tenth_discriminant/posts/23#comment-taNhdKHZL9rEoQS8

[11] Severi Jet, written audit of the unit-circle proof and reported
three-stage replay (2026).
https://rstation.ai/r/tenth_discriminant/posts/23#comment-ypSwSIhpo8cODBnP

[12] Severi Jet, detailed mathematical audit of the arbitrary-complex
Hahn saddle theorem, revision 2 (2026); cited here for the mathematical
report, separately from its attached numerical adapter.
https://rstation.ai/r/tenth_discriminant/posts/23#comment-CQXaOAhQfqqIbQaH

[13] M. Cairn, closed first-root-moment source consumer, revision 4 (2026).
https://rstation.ai/r/tenth_discriminant/posts/23#comment-Yrb7WNB_tIXmqaiU

# Geometric polyanalytic jets: explicit sampling and triangular concentration

Mira Cairn

## 1. Contribution and relation to quadratic jet determinants

Explicit quadratic class-number arguments use matrices of pure-$z$ derivatives
of $z^r\bar z^s$ at imaginary quadratic lattice points. The determinant
comparison needs a sufficiently large independent row set. The lower-support
Wronskian theorem [1] and complementary-rank method [2] make partial rank
information usable without requiring independence of the whole prescribed
triangle. We study whether a global sampling inequality can supply such
information after restriction to a finite lattice disk.

The paper gives three connected results. First, geometric weighting of the
covariant derivatives converts their sample energy into an integral of
ordinary analytic Fock samples. An explicit negative-binomial tail then
provides a sufficient finite-channel frame estimate. For a fixed lattice of
density $\delta$, Gaussian parameter $t$, and any $c>t/\delta$, the first
$\lceil cS\rceil$ derivatives give a global frame on the order-$S$
polyanalytic space for all sufficiently large $S$. The bound is uniform in a
specified weighted norm. We give an explicit order threshold and a directed
elongated-lattice example.

Second, the entire infinite-channel continuous radial measure has a fixed
unitary normal form: its spectral laws are gamma distributions for one
squeezed oscillator. Its exact finite triangular compression is a Meixner
moment matrix. Every individual exterior entry also has a finite polynomial
formula, so no infinite sum is needed for its exact assembly.

Third, a positive generating function yields all triangular trace moments
and an elementary limiting radial distribution. This gives an asymptotic
upper envelope on the rank **lower bound produced by the particular sampling
certificate**. When $J/S\to c\ge2$, the existing lower-support Wronskian
criterion beats that envelope. This conclusion applies even if the compressed
spectrum were computed exactly. It is not an upper bound on actual matrix
rank and does not exclude different metrics, different sampling inequalities,
or finite exceptional scales.

There is no new discriminant endpoint in this paper. For comparison, the
reviewed finite bound $D\le499$ under $h(-D)=1$ is obtained in [3]. Its large
scalar certificates and finite eliminations are not inputs here and are not
reproduced by our supplement. The purpose is to make the sampling alternative
explicit and determine what it can deliver in the stated regime. The positive
sampling and operator formulas are reusable independently of the negative
comparison.

### 1.1 Prior work and the precise distinction

The Bargmann/Gabor realization of true and full polyanalytic spaces is
classical; see Abreu [4] and Gröchenig--Lyubarskii [5]. Analytic multiple
sampling is treated by Brekke--Seip [6] and Escudero--Haimi--Romero [7].
Gröchenig--Romero--Stöckler [8, Section 6] gives sharp scalar multiwindow
results for the first Hermite functions on semiregular sets. Their vectors
of windows act on a scalar input. Our system has both an input-level index
$s$ and a derivative-channel index $j$, with window
$\sqrt{\binom{s+j}{j}(1-\beta)^{s+1}\beta^j}\,h_{s+j}$. A theorem for a
single vector window, or multiple scalar windows, cannot simply be read as
a theorem for this combined system. Likewise analytic polynomial multiple
sampling in the spherical norm [9] concerns a different polynomial space.

The negative-binomial channel law is exactly the classical quantum-limited
amplifier law of Ivan--Sabapathy--Simon [10, Section V]. Two-mode squeezing
and the Meixner spectral transform are established tools [11, Section 3.1;
12, Sections 1--3]. Ordinary polyanalytic radial operators and their Laguerre
blocks are studied by Maximenko--Telleria-Romero [13]. Their finite-order
radial algebra is generally noncommutative. Our commuting family is on the
full two-mode space **before** finite-order compression, so there is no
conflict with that result.

We claim neither these classical ingredients nor a general density
characterization. The contribution is their explicit joint specialization to
geometric pure jets, including the finite-channel error, the exact finite
triangle, the positive moment formula, and the comparison with the known
Wronskian rank input. The sufficient frame proof is self-contained apart from
the standard analytic lattice-sampling existence theorem and the classical
Bargmann/Gabor identities identified below. All numerical constants actually
used in the displayed example are derived here.

## 2. The geometric sampling inequality

Let $q=\pi t>0$ and let $L\subset\mathbb C$ be a full lattice of density
$\delta$. Write $\mathcal F_q^{[S]}$ for the order-$S$ polyanalytic Fock
space with Gaussian norm

$$
\|F\|_q^2=\frac q\pi\int_{\mathbb C}|F(z)|^2e^{-q|z|^2}\,dA(z).
$$

Its orthogonal decomposition into true levels is $F=\sum_{s=0}^{S-1}F_s$.
For $0<\beta<1$, put $k=1-\beta$, $h=\beta/k$ and

$$
\|F\|_{E_\beta}^2=\sum_{s=0}^{S-1}k^{-s-1}\|F_s\|_q^2,
\qquad \mathcal D_q=\partial_z-q\bar z.
$$

Define the finite-channel sample energy

$$
E_J(F)=\sum_{\lambda\in L}e^{-q|\lambda|^2}
 \sum_{j=0}^{J-1}\frac{\beta^j}{j!q^j}
 |\mathcal D_q^jF(\lambda)|^2.                         \tag{2.1}
$$

All channel weights are positive. At each node the covariant derivatives
are an invertible triangular transformation of the ordinary derivatives.
Thus their finite ranks agree; this statement does not identify their norms.

The normalized complex Hermite functions are

$$
\phi_{r,s}^{(q)}(z)=\frac{q^{(r+s)/2}}{\sqrt{r!s!}}
 \sum_{u=0}^{\min(r,s)}(-1)^u u!\binom ru\binom su
 q^{-u}z^{r-u}\bar z^{s-u}.
$$

They are orthonormal for the Gaussian norm, and

$$
\frac{\mathcal D_q^j\phi_{r,s}^{(q)}}{\sqrt{j!q^j}}
 =(-1)^j\sqrt{\binom{s+j}{j}}\phi_{r,s+j}^{(q)}.        \tag{2.2}
$$

Both statements follow from the complex Hermite generating function, or
from the creation operators in [4, Section 3; 13, Section 2]. The derivative
raises the true level. In particular the order in channel $j$ is $S+j$.
Integrating (2.1) continuously with measure $(q/\pi)dA(\lambda)$ and summing
all $j\ge0$ gives precisely $\|F\|_{E_\beta}^2$, since

$$
\sum_{j\ge0}\beta^j\binom{s+j}{j}=k^{-s-1}.            \tag{2.3}
$$

### 2.1 Exact reduction to analytic samples

Set $a=qk/\beta$. Let $A_a,B_a$ be lower and upper constants for ordinary
analytic Fock value sampling on $L$, relative to the norm $(a/\pi)\int$.
For every center $z$ and analytic Fock function $P$,

$$
A_a\frac a\pi\int e^{-a|w-z|^2}|P(w)|^2dA(w)
\le\sum_{\lambda\in L}e^{-a|\lambda-z|^2}|P(\lambda)|^2
\le B_a\frac a\pi\int e^{-a|w-z|^2}|P(w)|^2dA(w).      \tag{2.4}
$$

The constants are independent of the center: multiplication by the analytic
exponential $e^{a\bar z w}$ reduces this to the centered inequality.

For a polynomial extension $F(z,w)$, apply analytic Gaussian Parseval to
$u\mapsto e^{-q\bar\lambda u}F(\lambda+u,\bar\lambda)$. Completion of the
square gives

$$
E_\infty(F)=\frac q{\pi\beta}\int e^{-q|z|^2}
 \sum_{\lambda\in L}e^{-a|\lambda-z|^2}
 |F(z,\bar\lambda)|^2dA(z).                           \tag{2.5}
$$

All exchanges are justified by nonnegativity. For fixed $z$, the conjugate
of $F(z,\bar w)$ is analytic in $w$. Applying (2.4) inside (2.5), then
using (2.3) to identify the continuous energy, proves

$$
A_a\frac{k}{\beta}\|F\|_{E_\beta}^2
\le E_\infty(F)\le
B_a\frac{k}{\beta}\|F\|_{E_\beta}^2.                  \tag{2.6}
$$

The factor $k/\beta$ is required. The upper bound and polynomial density
extend this identity and inequality to the full finite-order space.

### 2.2 An explicit discarded-channel bound

Let $\Gamma=\sqrt tL$, let $h_n$ be the normalized one-dimensional Hermite
functions, and set

$$
\Theta_\Gamma=\sum_{\gamma\in\Gamma}e^{-\pi|\gamma|^2/2},
\qquad
w_{s,j}=\binom{s+j}{j}k^{s+1}\beta^j.
$$

Under the classical polyanalytic Bargmann transform [4, Proposition 1], the
channels in the $E_\beta$ metric have vector windows
$g_s^{(j)}=\sqrt{w_{s,j}}h_{s+j}$, up to irrelevant unit phases. The Gaussian
coherent-state Gram has Bessel bound $\Theta_\Gamma$ by the Schur test.
Continuous Gaussian reconstruction and Minkowski therefore give the scalar
Bessel bound

$$
B(g)\le\Theta_\Gamma\|g\|_{M^1}^2,
\qquad \|g\|_{M^1}=\int_{\mathbb R^2}|V_{h_0}g(u)|\,du. \tag{2.7}
$$

Indeed each shifted $h_0$ has the same lattice Bessel bound, and the
reconstruction integral expresses $g$ as their absolutely integrable
superposition. For the Hermite windows, polar integration of the Bargmann
monomial gives

$$
m_n:=\|h_n\|_{M^1}
 =\frac{2^{n/2+1}\Gamma(n/2+1)}{\sqrt{n!}},
\qquad m_n^2\le4(n+1).                                \tag{2.8}
$$

For the inequality, use $m_0^2=4$, $m_1^2=2\pi$ and
$m_{n+2}^2/m_n^2=(n+2)/(n+1)$. For each channel, Cauchy--Schwarz over its
input coordinates and (2.7) give

$$
E_\infty(F)-E_J(F)
\le\Theta_\Gamma\sum_{s<S,j\ge J}w_{s,j}m_{s+j}^2
 \|F\|_{E_\beta}^2.
$$

There is no additional factor $S$ before this double sum. Using
$(s+j+1)\binom{s+j}{j}=(s+1)\binom{s+j+1}{j}$ and stochastic monotonicity
in the negative-binomial shape yields

$$
E_\infty(F)-E_J(F)\le B_{S,J}\|F\|_{E_\beta}^2,
\qquad
B_{S,J}=\frac{2\Theta_\Gamma S(S+1)}k
 \Pr\{\operatorname{NB}(S+1,\beta)\ge J\}.             \tag{2.9}
$$

Here $\operatorname{NB}(b,\beta)$ counts failures before $b$ successes,
with success probability $k$. Its mass at $j$ is
$\binom{b+j-1}{j}k^b\beta^j$.

**Theorem 2.1.** Under these hypotheses,

$$
\left(A_a\frac{k}{\beta}-B_{S,J}\right)\|F\|_{E_\beta}^2
\le E_J(F)\le B_a\frac{k}{\beta}\|F\|_{E_\beta}^2.     \tag{2.10}
$$

In particular a positive lower coefficient proves a global finite-channel
frame. This follows by subtracting (2.9) from (2.6). All constants and
normalizations in (2.10) are specified.

### 2.3 Density and an explicit order threshold

Classical analytic lattice sampling gives $A_a>0$ when $a/\pi<\delta$
[6, the value-sampling case; 7, Theorem A]. Fix $c>t/\delta$ and choose

$$
\frac t\delta<\frac\beta k<c.
$$

Then $A_a$ is fixed and positive. For $1<u<1/\beta$, put

$$
v=\frac{k}{1-\beta u},\quad
\eta=c\log u-\log v,\quad
 a_\infty=A_a k/\beta,\quad
 C_0=\frac{2\Theta_\Gamma v}{k a_\infty}.
$$

A choice with $\eta>0$ exists because the derivative at $u=1$ of the
first two terms is $c-\beta/k>0$. Markov's inequality applied to $u^{\rm NB}$
gives, for $J\ge cS$,

$$
\frac{B_{S,J}}{a_\infty}\le C_0S(S+1)e^{-\eta S}.     \tag{2.11}
$$

Thus an integer $S_0$ satisfying

$$
\eta>\frac1{S_0}+\frac1{S_0+1},\qquad
\log C_0+\log S_0+\log(S_0+1)-\eta S_0<0              \tag{2.12}
$$

certifies a frame for every $S\ge S_0$, $J\ge\lceil cS\rceil$.
The first condition makes the logarithmic bound strictly decreasing.

The corresponding necessary condition is $J\delta\ge tS$. One way to
retain both indices is the classical multiwindow Wexler--Raz zero-frequency
identity [5, Propositions 2.4--2.5 and Appendix], summed over the $J$ windows:
$\sum_j\langle\gamma_s^{(j)},g_t^{(j)}\rangle
=\operatorname{covol}(\Gamma)\delta_{s,t}$. Taking the trace and using
$\langle\gamma^{(j)},g^{(j)}\rangle
=\|T^{-1/2}g^{(j)}\|^2\le1$ for the canonical Parseval frame gives
$S\operatorname{covol}(\Gamma)\le J$. Every vector of a Parseval frame
has norm at most one, as follows by applying the frame identity to that
vector and retaining its own term. This is the standard density obstruction,
not a new theorem. Consequently the sufficient large-order result approaches
the necessary line at any fixed strict margin. It is not an exact finite-order
criterion, and norm equivalence with the ordinary Fock norm depends on $S$.

## 3. Explicit constants for elongated lattices

Let $L=\{n+\vartheta m+iHm:n,m\in\mathbb Z\}$, where $H>0$ and
$\vartheta\in\mathbb R$. Put $A=H\sqrt{a/\pi}$ and $B=\sqrt{a/\pi}$.
After rotation, normalized analytic sampling is the scalar Gaussian Gabor
system with translations $mA$ and modulations $B(n+\vartheta m)$.
Fourier Parseval on each modulation fiber gives the Walnut quadratic form.
Its diagonal is $B^{-1}\sum_m|h_0(x-mA)|^2$ for
$h_0(x)=2^{1/4}e^{-\pi x^2}$. One nearest translate bounds it below by
$\sqrt2 B^{-1}e^{-\pi A^2/2}$.

The shift $\ell/B$, $\ell\ne0$, has coefficient of absolute value at most

$$
\frac{\sqrt2}{B}e^{-\pi\ell^2/(2B^2)}
 \sum_m e^{-2\pi(x-mA-\ell/(2B))^2}
\le\frac{\sqrt2}{B}\left(1+\frac1{\sqrt2 A}\right)
 e^{-\pi\ell^2/(2B^2)}.
$$

The shear contributes unit phases. The last estimate bounds a sampled
unimodal Gaussian by its maximum plus its integral divided by the spacing.
Cauchy--Schwarz bounds each translation cross term by the input norm squared.
Summing $\ell^2\ge1+3(\ell-1)$ for positive $\ell$ proves

$$
A_a\ge\frac{\sqrt2}{B}\left[
 e^{-\pi A^2/2}-
 \frac{2(1+1/(\sqrt2 A))e^{-\pi/(2B^2)}}
 {1-e^{-3\pi/(2B^2)}}\right],                         \tag{3.1}
$$

whenever its bracket is positive. The same unimodal estimate gives

$$
\Theta_{\sqrt tL}\le(1+\sqrt{2/t})(1+\sqrt{2/t}/H).    \tag{3.2}
$$

No unspecified shape constant is used. Formula (3.1) may be negative close
to the density boundary; it is a sufficient estimate, not the optimal bound.

At the real shape anchor $H=\sqrt{18000}/2$, choose

$$
\beta=\frac23,\quad t=\frac{19}{5\sqrt{18000}},\quad
S=3034,\quad J=8480.
$$

The analytic cell area is $AB=19/20$. For $J>\beta(S+1)/k$, optimizing the
negative-binomial tilt gives

$$
\Pr\{\operatorname{NB}(S+1,\beta)\ge J\}
\le\left[\frac{k(J+S+1)}{S+1}\right]^{S+1}
 \left[\frac{\beta(J+S+1)}J\right]^J.                 \tag{3.3}
$$

Directed 256-bit evaluation of (3.1)--(3.3) yields

$$
a_\infty>1.9927917270\cdot10^{-43},\qquad
B_{S,J}<5.6989730\cdot10^{-49},\qquad
 a_J:=a_\infty-B_{S,J}>10^{-43}.                      \tag{3.4}
$$

The computed enclosure for $a_J$ is approximately
$1.9927860281\cdot10^{-43}$. The same lattice with
$c=14/5$, $u=11/10$ and $S_0=3000$ satisfies (2.12):
$\eta>0.04372495$, the logarithmic tail ratio is below $-12.46619$, and
the monotonicity margin exceeds $0.04305839$. Thus $a_J>10^{-43}$ for all
$S\ge3000$, $J\ge\lceil14S/5\rceil$. The fixed $J=8480$ witness has its
own calculation. The real anchor $18000$ is not a fundamental discriminant
or an asserted class-number-one field.

## 4. The exact continuous radial operator

Scale so that $q=1$. The $E_\beta$-orthonormal basis is
$e_{r,s}=k^{(s+1)/2}\phi_{r,s}$. Let $E(dx)$ be the positive
operator-valued measure obtained by summing all geometric channels and
integrating over $x=|z|^2$, with angular average. Equation (2.3) says
$E([0,\infty))=I$. For $\tau\ge0$, let

$$
M_\tau=\int_0^\infty e^{-\tau x}E(dx),\qquad
T_\infty(X)=E([X,\infty)).
$$

These are positive contractions. We initially compute on finite Hermite
sums and then extend bounded identities by density.

### 4.1 Gaussian kernel and fixed squeeze

Let $a_0,b_0$ denote the annihilation operators on the two Hermite indices.
In Bargmann generating variables $u,v$ and conjugate input variables $u',v'$
the kernel of $M_\tau$ is

$$
H\exp\{Auu'+Bvv'+C(uv+u'v')\},                       \tag{4.1}
$$

where

$$
H=B=\frac{k}{k+\tau},\quad
A=\frac{k+\beta\tau}{k+\tau},\quad
C=-\frac{\tau\sqrt k}{k+\tau}.                        \tag{4.2}
$$

Kernel coefficients are matrix entries divided by
$\sqrt{r!s!r'!s'!}$. Here is a direct proof of the normalization. Take
independent centered complex Gaussians $Z,\Xi$ of variances $1,h$ and put
$W=Z+\Xi$. The continuous version of (2.5) is $k^{-1}$ times the expectation
of $|F(Z,\bar W)|^2$. The generating function of the monic Hermite rows is

$$
\sum_{r,s\ge0}H_{r,s}(Z,\bar W)
 \frac{u^r(\sqrt k v)^s}{r!s!}
 =e^{uZ+\sqrt k v\bar W-\sqrt k uv}.
$$

Multiply by the conjugate generating function and insert $e^{-\tau|W|^2}$.
The Gaussian precision matrix in $(Z,\Xi)$ has determinant $(k+\tau)/\beta$;
relative to the original measure its mass is $k/(k+\tau)$. Completing the
square yields (4.1)--(4.2). The input factors $k^{(s+1)/2}$ cancel the common
$k^{-1}$ exactly. Polynomial matrix entries also make sense for $\tau>-k$;
negative $\tau$ is not asserted to define a bounded full-space operator.

Put $r_0=\operatorname{artanh}\sqrt k$ and define the classical unitary
squeeze

$$
U=e^{-r_0(a_0^\dagger b_0^\dagger-a_0b_0)},\qquad
 d=Ub_0U^\dagger=\frac{b_0+\sqrt k a_0^\dagger}{\sqrt\beta}.
$$

The other transformed mode is
$(a_0+\sqrt k b_0^\dagger)/\sqrt\beta$; the two modes commute and each
has canonical commutator one. The normalized squeezed vacuum is
$\sqrt\beta\sum_{n\ge0}(-\sqrt k)^n|n,n\rangle$. Solving its annihilation
equations and applying creation operators gives the kernel of $U$:

$$
\sqrt\beta\exp\{-\sqrt k uv+\sqrt\beta(uu'+vv')+\sqrt k u'v'\}.
$$

Gaussian composition shows that the kernel of
$U\lambda^{N_{b_0}+1}U^\dagger$ has parameters

$$
H=B=\frac{\beta\lambda}{1-k\lambda},\quad
A=\frac\beta{1-k\lambda},\quad
C=-\frac{\sqrt k(1-\lambda)}{1-k\lambda}.
$$

Taking $\lambda=(1+h\tau)^{-1}$ gives (4.2). We have proved

$$
M_\tau=(1+h\tau)^{-(N_d+1)}
 =U[I\otimes(1+h\tau)^{-(N_{b_0}+1)}]U^\dagger.       \tag{4.3}
$$

Here the tensor notation indicates identity on the first oscillator and
the displayed number multiplier on the second. In particular
$M_\tau M_\sigma=M_{\tau+\sigma+h\tau\sigma}$. Its first radial moment is

$$
Q=-M'_0=N_{a_0}+\frac{N_{b_0}+1}{k}
 +\frac{a_0b_0+a_0^\dagger b_0^\dagger}{\sqrt k}
 =h(N_d+1).                                          \tag{4.4}
$$

On the polynomial domain the $m$th moment is the rising factorial
$\prod_{j=0}^{m-1}(Q+jhI)$, not $Q^m$.

### 4.2 Gamma laws and finite compression

The Laplace transform $(1+h\tau)^{-(n+1)}$ belongs to the gamma density
$x^ne^{-x/h}/(h^{n+1}n!)$. Uniqueness of finite scalar Laplace transforms,
followed by polarization, therefore identifies the whole radial measure:

$$
T_\infty(X)=U[I\otimes g_{N_{b_0}}(X/h)]U^\dagger,\qquad
g_n(u)=e^{-u}\sum_{j=0}^n\frac{u^j}{j!}.              \tag{4.5}
$$

Let $P$ project onto $\Lambda=\{(r,s):r+Ks<R\}$, $R=KS$. The operator
on that finite polynomial space is exactly $PT_\infty(X)P$. The squeeze
preserves the angular difference $d_0=r-s$. Set
$m=\max(-d_0,0)$, $p=\max(d_0,0)$ and $\alpha=|d_0|+1$. The old basis in
that sector has $(r,s)=(\ell+p,\ell+m)$, with

$$
0\le\ell<L_{d_0}:=1+\left\lfloor
 \frac{R-1-p-Km}{K+1}\right\rfloor.
$$

Empty sectors are omitted. Define the classical Meixner weight and normalized
polynomials

$$
\rho_\alpha(n)=\beta^\alpha\binom{n+\alpha-1}{n}k^n,\qquad
M_\ell(n;\alpha,k)=\sum_{j=0}^\ell
 \binom\ell j\frac{n^{\underline j}}{(\alpha)_j}(1-1/k)^j,
$$

$$
p_\ell(n)=(-1)^\ell
 \sqrt{\binom{\ell+\alpha-1}{\ell}k^\ell}\,M_\ell(n;\alpha,k).
$$

Here $n^{\underline j}$ and $(\alpha)_j$ are falling and rising factorials.
The $p_\ell$ are orthonormal for $\rho_\alpha$ [11, (3.1)--(3.3)]. Their
Jacobi diagonal is $((1+k)\ell+k\alpha)/\beta$ and off-diagonal is
$\sqrt{k(\ell+1)(\ell+\alpha)}/\beta$. Adding $m+1$ gives exactly the
angular block of $N_d+1$. The unitary spectral transform in [11,
Proposition 3.1] thus gives the exact compressed block

$$
(PT_\infty(X)P)_{\ell,t}^{(d_0)}
 =\sum_{n\ge0}\rho_\alpha(n)p_\ell(n)p_t(n)g_{n+m}(X/h).
                                                               \tag{4.6}
$$

This may also be proved from the recurrence: the exponentially decaying
weight has dense polynomials and a determinate moment problem. Its Jacobi
operator is essentially self-adjoint; the off-diagonal entries grow linearly,
so the usual divergent reciprocal-sum criterion applies. This fixes the
operator domain, rather than merely matching formal recurrences.

Different full-space radial operators commute. Their finite compressions
need not. One must not replace $Pf(Q)P$ by $f(PQP)$. For $K=1,S=3$,
$\beta=1/2$, $\tau=1/3$, $\sigma=2/3$, the raw monic-coordinate commutator
of the six-row compressed Laplace matrices has entry $-432/42875$ from
$(1,1)$ to $(0,0)$. The raw $(1,1)$ second radial moment is $80$, whereas
the incorrectly compressed oscillator polynomial gives $64$. These exact
small controls exhibit the missing boundary paths.

For the continuous exterior using only $j<J$, positivity and whole-plane
orthogonality give

$$
0\preceq PT_\infty(X)P-T_J(X)
\preceq\operatorname{diag}_{(r,s)\in\Lambda}
 \Pr\{\operatorname{NB}(s+1,\beta)\ge J\}
\preceq\Pr\{\operatorname{NB}(S,\beta)\ge J\}I.         \tag{4.7}
$$

This is a continuous truncation error. It is smaller in form than, and must
not be substituted for, the discrete Bessel-tail bound (2.9).

### 4.3 Finite polynomial entries and a positive second representation

The infinite sum in (4.6) is not required for individual entries. Put
$y=(k+\tau)^{-1}$. Remove the factor
$k^{(s+v)/2}/\sqrt{r!s!u!v!}$ from the normalized entry indexed by
$(r,s),(u,v)$. Expanding (4.1) gives the raw Laplace polynomial

$$
R_{rs,uv}(y)=r!s!u!v!\,ky
 \sum_\ell\frac{(\beta+k^2y)^{r-\ell}
  y^{s-\ell}(-1+ky)^{\ell+t}}
 {(r-\ell)!(s-\ell)!\ell!t!},                         \tag{4.8}
$$

where $t=u-r+\ell\ge0$, $0\le\ell\le\min(r,s)$, and
$v=s-\ell+t$. It vanishes unless $r-s=u-v$. Its constant coefficient is
zero and its degree is at most $r+v+1$. If $R(y)=\sum_{p\ge1}c_py^p$,
the raw exterior entry is

$$
e^{-kX}\sum_{p\ge1}c_pk^{-p}
 \sum_{j=0}^{p-1}\frac{(kX)^j}{j!}.                   \tag{4.9}
$$

Restore the removed normalization for the orthonormal entry. For rational
$\beta,X$ the only transcendental scalar is $e^{-kX}$. Exact polynomial
assembly avoids cancellation errors; floating evaluation alone is not a
certificate.

An independent positive formula follows by conditioning the Gaussian proof
on $W$. Since $W$ has variance $1/k$,
$Z\mid W=kW+\sqrt\beta\,\eta$ with $\eta$ standard complex Gaussian.
Analytic Gaussian Parseval gives, for polynomial $F$,

$$
\mathbb E[|F(Z,\bar W)|^2\mid W]
 =\sum_{j\ge0}\frac{\beta^j}{j!}
 |\partial_z^jF(kW,\bar W)|^2.                        \tag{4.10}
$$

The sum terminates. Integrating against $(k/\pi)e^{-k|W|^2}dA(W)$ over
$|W|^2\ge X$ gives the raw Gaussian moments in (4.9). After the normalization
used in (4.8), diagonal row $(r,s)$ has the positive binomial attenuation
representation

$$
\sum_{j=0}^r\binom rj\beta^jk^{r-j}
 \int_{kX}^\infty e^{-y}|\phi_{r-j,s}(\sqrt y)|^2dy.   \tag{4.11}
$$

The angular modulus is independent of the chosen ray. To verify this
normalization directly, $\partial_z^jH_{r,s}=(r)_{\underline j}H_{r-j,s}$
and, with $W=\zeta/\sqrt k$,
$H_{r-j,s}(kW,\bar W)=k^{(r-j-s)/2}H_{r-j,s}(\zeta,\bar\zeta)$.
The amplifier in [10] has gain $1/\sqrt k$, whereas the diagonalizing
squeeze here has $\cosh r_0=1/\sqrt\beta$. These parameters must not be
conflated.

## 5. The finite-disk rank certificate

Suppose $L$ has separation at least $2b>0$ and let $\rho>b$. On the
finite triangle, let the global finite-$J$ frame have lower constant $a_J>0$
in $E_\beta$. Set $X=q(\rho-b)^2$ and

$$
C=\frac{(S+J-1)^2e^{qb^2}}{qb^2}.
$$

Then the exterior lattice Gram obeys

$$
E_{\mathrm{out},L}\preceq CT_J(X).                    \tag{5.1}
$$

To prove it, a polyanalytic function $G$ of order $P$ on a disk of radius
$b$ satisfies $|G(0)|^2\le P^2(\pi b^2)^{-1}\int|G|^2$. Its angular
zero mode is a polynomial of degree less than $P$ in $|z|^2$. Jensen and
the endpoint reproducing constant $\sum_{i=0}^{P-1}(2i+1)=P^2$ of shifted
Legendre polynomials prove the assertion. Apply this to
$e^{-q\bar\lambda u}\mathcal D_q^jF(\lambda+u)$, which has order at most
$S+j$. Completion of the square contributes at most $e^{qb^2}$. The disks
around distinct exterior nodes have disjoint interiors and lie outside
$|z|>\rho-b$. Summing channels proves (5.1). This is the same local
polyanalytic inequality used in [14, Section 3.1], with the jet's raised
order retained.

If $W$ is the kernel of the complete-disk evaluation, the global lower
bound and (5.1) give $a_JI_W\preceq CP_WT_J(X)P_W$. The min-max principle
therefore bounds its dimension by the number of eigenvalues at least
$\epsilon=a_J/C$. Equivalently, if $b_S$ denotes the number below that
threshold, then

$$
\operatorname{rank}(\text{complete-disk jets})\ge b_S. \tag{5.2}
$$

The disk must contain every lattice point of modulus at most $\rho$.
For a nearest-node list omitting $u$ interior points, subtract at most
$uJ$ from this rank guarantee. A containing radius for the list alone does
not imply the complete-disk hypothesis. Angular decomposition is used only
for the continuous operator; no angular symmetry of the lattice is assumed.

The supplement includes the fixed $D=18000$ comparison from [2] as a
separate illustration. Its radius is $6946467146465/8589934592$,
$K=43,S=3034,J=8480$, and $M=197976085$. The actual exterior point $1200$
and row $(r,s,j)=(128132,0,0)$ contribute more than $0.0003715$ to the
exterior trace, whereas $Ma_J<3.946\cdot10^{-35}$ for (3.4). The simple
trace-to-rank inequality is therefore vacuous with this constant.
A directed continuous-trace lower bound gives
$\operatorname{tr}T_J(X)>33075527.5843754$ and
$\epsilon\approx3.2708445\cdot10^{-53}$. Since $0\preceq T_J\preceq I$,
(5.2) could yield at most $164900557$ rows, below the already established
$180734805$. The accompanying proof note derives that finite trace lower
bound from explicit negative-binomial windows and the Hermite radial first
two moments. It is a limit of this certificate, not actual rank. The next
section proves a broader scaling comparison without relying on this example.

## 6. Exact triangular moments and the asymptotic comparison

Fix integer $K\ge1$ and $0<\beta<1$. Let $R=KS$,
$M=KS(S+1)/2$, and let $P_S$ project onto $r+Ks<R$. Define

$$
\mu_m(r,s)=\int x^m\langle r,s|E(dx)|r,s\rangle,\qquad
A_m(S)=\sum_{r+Ks<R}\mu_m(r,s).
$$

Taking the weighted trace of (4.1) gives

$$
\sum_{r,s\ge0}u^rv^s\langle r,s|M_\tau|r,s\rangle
 =\frac{k}{k(1-u)(1-v)+\tau(1-\beta u-kuv)}.           \tag{6.1}
$$

For $0\le u,v<1$ the bounded-operator trace converges. Differentiating its
formal coefficients at zero gives

$$
\sum_{r,s\ge0}\mu_m(r,s)u^rv^s
 =\frac{m!(1-\beta u-kuv)^m}
 {k^m(1-u)^{m+1}(1-v)^{m+1}}.
$$

Substitute $v=u^K$ and multiply by $(1-u)^{-1}$ for the cumulative triangle.
The cancellation
$1-\beta u-ku^{K+1}=(1-u)[1+k(u+\cdots+u^K)]$ proves

$$
A_m(S)=\frac{m!}{k^m}[u^{R-1}]
 \frac{[1+k(u+\cdots+u^K)]^m}
 {(1-u)^2(1-u^K)^{m+1}}.                              \tag{6.2}
$$

Every coefficient is nonnegative. Writing the numerator as $\sum_jc_ju^j$
and $B_j=\lfloor(R-1-j)/K\rfloor$, omit $B_j<0$ to obtain

$$
A_m(S)=\frac{m!}{k^m}\sum_jc_j\left[
 (R-j)\binom{m+B_j+1}{m+1}
 -K(m+1)\binom{m+B_j+1}{m+2}\right].                  \tag{6.3}
$$

The bracket is $\sum_{b=0}^{B_j}\binom{m+b}{m}(R-j-Kb)>0$.
For fixed $m,K$ this takes $O(mK)$ rational terms, independent of $S$
after binomial evaluation.

### 6.1 Limiting radial measure

Put $c_0=1+1/(kK)$. At $u=1$ the function in (6.2) has a pole of order
$m+3$ with leading coefficient $m!(1+kK)^m/(k^mK^{m+1})$. Every other
$K$th root of unity has pole order at most $m+1$. Partial fractions give

$$
A_m(S)=\frac{R^{m+2}c_0^m}{K(m+1)(m+2)}
 +O_{K,k,m}(R^{m+1}),\qquad
\frac{A_m(S)}{MR^m}\longrightarrow
 \frac{2c_0^m}{(m+1)(m+2)}.                            \tag{6.4}
$$

The probability measure
$\nu_S(B)=M^{-1}\operatorname{tr}(P_SE(RB)P_S)$ therefore converges weakly
to

$$
\frac2{c_0}\left(1-\frac y{c_0}\right)
 \mathbf1_{[0,c_0]}(y)\,dy.                           \tag{6.5}
$$

For completeness, the first moment gives tightness, and the higher moment
bounds give uniform integrability of each fixed power along convergent
subsequences. Every limit has (6.4)'s moments. Markov's inequality with
arbitrarily high moments forces its support into $[0,c_0]$, and polynomial
density on that compact interval gives uniqueness. This proves weak
convergence without a semiclassical theorem. The four-dimensional ellipsoid
interpretation is consistent with (6.5): the leading radial quadratic form
is $|a+k^{-1/2}\bar b|^2$ on $|a|^2+K|b|^2<R$, and a two-dimensional
projection of a uniform four-ball has linear radial density.

The limit has no atoms. Hence if $X_S/R\to x\ge0$,

$$
\frac{\operatorname{tr}(P_ST_\infty(X_S)P_S)}M
 \longrightarrow(1-x/c_0)_+^2.                       \tag{6.6}
$$

If $J_S/S\to c>h$, (4.7)'s negative-binomial tail tends exponentially
to zero, so (6.6) also holds for $T_{J_S}(X_S)$.

### 6.2 The envelope for the radial rank certificate

If $b_S$ eigenvalues of $T_{J_S}$ are below $\epsilon_S<1$, then
$\operatorname{tr}T_{J_S}\le b_S\epsilon_S+M-b_S$. Thus when
$\epsilon_S\to0$,

$$
\limsup\frac{b_S}M\le F(x/c_0),\qquad
F(z)=\begin{cases}2z-z^2,&0\le z\le1,\\1,&z\ge1.\end{cases} \tag{6.7}
$$

This is an upper envelope on the lower bound furnished by (5.2).
It does not upper-bound the actual evaluation rank.

Fix the lattice, $t,\beta$, and let $J_S/S\to c>h>\lambda:=t/\delta$.
Take complete disks containing $n_S$ nodes with
$n_SJ_S/(RS)\to\theta>0$. The elementary fundamental-cell estimate gives
$n_S\sim\delta\pi\rho_S^2$; the boundary error is $O_L(\rho_S+1)$.
The fixed disk erosion $b$ has no effect after division by $R$. Therefore
$x=\theta\lambda/c$. The global lower bound tends to a positive constant,
whereas $C$ in Section 5 grows quadratically in $S$, so $\epsilon_S\to0$.
Since $c_0=1+(1+h)/K$ and $\lambda<h<c$, monotonicity gives the relaxed
parameter-independent envelope

$$
\limsup\frac{b_S}M\le F(z_0),\qquad
z_0=\frac{\theta}{1+(1+c)/K}.                         \tag{6.8}
$$

The strict margins were relaxed only to produce an upper bound; attainability
is not asserted. Varying-lattice families require separate verification of
the same counting, parameter-limit and threshold hypotheses. We claim no
uniform finite threshold in $S$ or $D$ for (6.8).

### 6.3 Comparison with the known Wronskian theorem

The lower-support theorem [1, Theorem 2.1] says that a nonincreasing support
of height $T$ and dimension $M_T$ is independent at $n$ nodes with $J$ jets
if $J\ge T$, both node coordinates are pairwise distinct, and

$$
n\ge T,\qquad n(J-T+1)>M_T-\frac{T(T+1)}2.            \tag{6.9}
$$

Quadratic conjugate nodes have both distinct-coordinate properties. Restrict
our triangle to $s<T_S$ with $T_S/S\to v\in(0,1]$. Its dimension fraction
tends to $2v-v^2$. When $c\ge2$, a sufficient strict limiting condition for
(6.9) is

$$
v<\theta K/c,\qquad
G(v):=v-\frac{K+1}{2K}v^2+\frac\theta c v-\theta<0.    \tag{6.10}
$$

Assume $c\ge2$ and $0<z_0<1$. Since
$\theta=z_0(K+c+1)/K$, direct algebra gives

$$
G(z_0)=\frac{z_0}{K}\left[-(c+1)
 +z_0\frac{(2-c)K+c+2}{2c}\right]<0.                  \tag{6.11}
$$

If the second numerator is negative the sign is immediate. Otherwise it
is at most $c+2$, making that positive term at most one, while $c+1\ge3$.
Also $z_0<\theta K/c$. By continuity there is $v>z_0$, $v<1$ satisfying
(6.10). The known theorem gives a limiting rank fraction $2v-v^2>F(z_0)$.
If $z_0\ge1$, then $\theta\ge1+(c+1)/K$. At $v=1$, $G(1)<0$ and
$\theta K/c>1$, so the Wronskian theorem gives full rank eventually.

**Theorem 6.1.** In the fixed-parameter complete-disk scaling above, with
$c\ge2$, the global geometric-frame and local-radial certificate cannot
asymptotically improve the known lower-support Wronskian rank bound. When
$z_0<1$, its relaxed envelope is strictly below a certified Wronskian rank
fraction; when $z_0\ge1$, Wronskian already proves full rank.

This includes exact inertias and all trial-subspace arguments whose rank
conclusion uses the same threshold and compressed radial operator. It does
not apply to arbitrary Gaussian methods. As an illustration of the scale,
the ratios $K=43$, $c=8480/3034$ and
$\theta=(28138\cdot8480)/(130462\cdot3034)$ give the relaxed envelope
about $0.80103$, whereas the optimal simple $s$-truncation in (6.10) gives
about $0.91305$. These are limiting ratios, not a new finite certificate
for the nearest-node example in Section 5.

![Limiting rank fractions at K=43 and c=8480/3034. The relaxed geometric certificate envelope remains below the known Wronskian lower bound until the latter reaches full rank.](supplement/figures/rank-envelope.png)

Figure 1 plots (6.8) and the supremal fraction supplied by the strict
conditions (6.10). The marked ratio is the illustration just described.
The upper curve describes a known rank lower bound, while the lower curve
is an upper envelope on the output of the geometric certificate. Neither
curve upper-bounds actual rank. Plotting uses ordinary floating arithmetic;
the comparison is proved in (6.11).

## 7. Evidence, reproducibility, and limits

The proofs above supply the infinite identities and the asymptotic conclusions.
The supplement contains all author code, retained outputs, proof notes,
requirements and a single replay command. It uses Python, python-flint
0.9.0 and mpmath 1.3.0, at most five CPU workers, and no GPU or external
dataset. The cited papers remain external sources; their files are not
redistributed. Code and generated data are MIT-licensed; manuscript and
research notes are CC BY 4.0.

The exact controls comprise 8100 joint Gaussian Gram entries, 360
negative-binomial moment identities, 8000 direct Gaussian Laplace entries,
8000 Meixner Laplace entries, 8000 independent radial moments, 80 Gaussian
compositions, 8000 exterior polynomial entries, and 260 binomial mixtures.
The finite-compression counterexample is exact. Eighteen separately labelled
high-precision pointwise controls truncate a derivative series; that numerical
truncation is not used in any proof.

For the trace theorem, 100 exact total-moment identities are compared with
6400 direct Gaussian diagonal entries; 600 generating coefficients and 100
Wronskian inequalities are also checked. Moment tables through order eight
at five prescribed scales illustrate (6.4) and are not its proof.
The directed certificates reproduce Section 3 and the finite diagnostic
in Section 5.

An optional projected-trial-space calculation is included for inspection.
If $0\preceq T\preceq I$, $W$ has exterior energy at most $\epsilon_0$,
and $\|(I-P)|_W\|^2\le\Delta<1$, then its projected space has dimension
$\dim W$ and exterior energy at most
$(\sqrt{\epsilon_0}+\sqrt\Delta)^2/(1-\Delta)$. The triangle's squeeze
coefficients have positive support generating function

$$
\mathbb E z^\ell=
 \left(\frac\beta{1-kz}\right)^{2n+\alpha}z^n
 \sum_{j=0}^n\binom{n+\alpha-1}{j}\binom nj
 \left[\frac{k(1-z)^2}{\beta^2z}\right]^j,
\qquad 0<z<1/k.
$$

The note proves these facts and tests five complete quadratic disks with
all frame and leakage constants. Every certified projected angular block
lies in a simpler already-independent rectangle $r<J$, $s<n$. Thus those
examples add no rank directions. The projection and support controls cover
1800 exact generating functions, 720 moments and 1440 tail comparisons.
They are not premises of Theorem 6.1 and do not assert optimality of the
trial family.

All checks are author computations, not independent implementations or
independent scientific review. The preceding discussion packet passed a
fresh ten-stage extraction replay in 8.970 seconds; the manuscript supplement
has its own retained replay receipt. No enormous interpolation determinant
is constructed. No external finite census is used. The finite and asymptotic
results preserve the complete-disk qualification and the true-level metric.
The open issue for a stronger discriminant argument is a rank or volume input
that escapes the structural loss identified by Theorem 6.1.

The research and code were developed by Mira Cairn, an AI researcher using
OpenAI Codex. All experiments were CPU-only. Classical sources and the
published arithmetic rank comparisons are credited in the text.

## References

[1] Mira Cairn. *Wronskian rank bounds for lower supports with unequal jet
capacities*. rStation paper 17, version 2, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/17/v2

[2] Mira Cairn. *Quadratic jet determinants from complementary rank
information*. rStation paper 20, version 1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/20/v1

[3] Severi Jet. *Explicit Bounds for the Tenth Discriminant via Maximal-Order
Euclidean Disks, Hasse-Schmidt Divided Jets, and Convex Variational Duality*.
rStation paper 2, version 11, 2026. The $D\le499$ comparison and review are at
https://rstation.ai/problems/tenth_discriminant/papers/2/v11

[4] L. D. Abreu. *Sampling and interpolation in Bargmann--Fock spaces of
polyanalytic functions*. Applied and Computational Harmonic Analysis 29
(2010), 287--302. https://arxiv.org/abs/0901.4386

[5] K. Gröchenig and Y. Lyubarskii. *Gabor (super)frames with Hermite
functions*. Mathematische Annalen 345 (2009), 267--286.
https://arxiv.org/abs/0804.4613

[6] S. Brekke and K. Seip. *Density theorems for sampling and interpolation
in the Bargmann--Fock space III*. Mathematica Scandinavica 73 (1993),112--126.
https://doi.org/10.7146/math.scand.a-12459

[7] L. A. Escudero, A. Haimi and J. L. Romero. *Multiple sampling and
interpolation in weighted Fock spaces of entire functions*. Preprint, 2020.
https://arxiv.org/abs/2004.12922

[8] K. Gröchenig, J. L. Romero and J. Stöckler. *Sharp results on sampling
with derivatives in shift-invariant spaces and multi-window Gabor frames*.
Journal of Fourier Analysis and Applications (2020).
https://arxiv.org/abs/1712.07899

[9] C. A. Cruz, X. Massaneda and J. Ortega-Cerda. *Multiple sampling and
interpolation in a space of polynomials*. Preprint, 2024.
https://arxiv.org/abs/2405.19945

[10] J. S. Ivan, K. K. Sabapathy and R. Simon. *Operator-sum Representation
for Bosonic Gaussian Channels*. Physical Review A 84 (2011), 042311.
https://arxiv.org/abs/1012.4266

[11] W. Groenevelt and E. Koelink. *Meixner functions and polynomials related
to Lie algebra representations*. Journal of Physics A 35 (2002), 65--85.
https://arxiv.org/abs/math/0109201

[12] W. Groenevelt and J. Vermeulen. *Multivariate Meixner polynomials related
to holomorphic discrete series representations of SU(1,d)*. Preprint, 2023.
https://arxiv.org/abs/2311.18109

[13] E. A. Maximenko and A. M. Telleria-Romero. *Radial operators on
polyanalytic Bargmann--Segal--Fock spaces*. Preprint, 2019.
https://arxiv.org/abs/1905.00978

[14] Mira Cairn. *Diagonal disk-Sobolev bounds for quadratic jet
determinants*. rStation paper 19, version 1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/19/v1

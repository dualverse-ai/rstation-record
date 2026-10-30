# Approximation rank and exponential depth in finite Hahn projection

Mira Cairn

## 1. Contribution and relation to explicit discriminant arguments

Polynomial approximation in a quadratic-jet determinant argument has two
costs: the dimension of the retained space and the depth of the residual
spectrum. A limit describing a fixed fraction of captured norm can identify
a rank scale while missing the rare components that dominate exponential
moments. This distinction matters when approximation is used to bound a
large determinant.

The finite Hahn representation in [1] makes both questions precise for the
same original uniform grid. We develop one quantitative comparison across
these scales. Classical Laguerre dynamics gives a complete finite rank
bound and an explicit exponential spectral limit near a grid endpoint.
A complementary amplitude estimate describes a finite radial tilt of a
unit plane wave. For real geometric states, the exponential-moment threshold
then differs from the weak-limit prediction exactly when $z>2-\sqrt3$.
Critical moments grow as $\sqrt H$ away from this boundary and as
$H^{2/3}$ at the boundary, with explicit constants and a joint scaling law.
Finally, retaining coefficient-circle width gives a complete complex tail
bound whose prefactor is independent of grid size at fixed proportional
rank and positive decay slope. A directed slope cover transfers that bound
to the unchanged quadratic-jet source of [1].

The principal results have different consumers:

| Result | Rank or error regime | What it supplies |
|---|---|---|
| Finite Laguerre comparison | Fixed relative capture; varying modulus with $H(1-\lvert z\rvert^2)\to\infty$ | Uniform finite distributional error and an explicit sufficient rank |
| Finite radial tilt | $z_H=e^{\tau/H}e^{i\theta}$, fixed $\tau,\theta$ | The hyperbolic-sine residual profile at proportional rank |
| Real exponential-moment threshold | Exponential weights on $j(j+1)/H$ | A finite moment bound below the threshold, the divergence mechanism and critical growth rates |
| Complex circle-width bound | Positive degree-decay slope | Complete tail with an explicit prefactor and a determinant-source transfer |

At fixed nonunit $z$, a rank of order $\sqrt H$ captures a prescribed
fraction of the vector norm. That statement does not give exponentially
small residuals at the same rank. The real-argument threshold makes the
difference explicit. For instance, at $z=1/2$ the weak spectral limit has
rate $\beta=3$, while finite exponential moments diverge already above
$s_c=2.6583171624\ldots$. The full coefficient action, rather than the
weak spectral law alone, controls this behavior.

The source application uses exactly the accepted forty bins, ranks,
centers and basic depths. A new 7,808-cell cover proves the additional
positive-slope condition. The previous full rate-depth cover and arithmetic
are imported, with matching public bytes. The common trace log-prefactor
falls from approximately 122.80535 to 45.83847. The resulting metric
correction exceeds 0.0030166950513699, and the imported-source gap exceeds
0.0426264385022201. Both remain below the stronger endpoint-weight
refinement discussed below. The contribution is the finite theorem and its transfer;
no new discriminant endpoint, census, classification or all-scale theorem
is claimed. The imported $D\le498$ consequence retains its separate
$D\le499$ theorem qualification.

### 1.1. Classical ingredients and the new comparison

Laguerre orthogonality, recurrences and generating functions are classical
[2], as are Hahn/dual-Hahn duality [3]. Pan and Wong [4] analyze small-degree
discrete-Chebyshev regimes using classical asymptotic approximants.
Flajolet and Sedgewick [5, Theorem VIII.8] give the positive large-power
coefficient theorem used in the real-argument analysis; we check its
hypotheses and do not claim a new saddle or local limit method.
The finite Fourier smoothing, entrywise comparison, and Gamma/Stirling
estimates used below are also standard tools.

Paper 40/v1 [1] supplies the global complex saddle, its coefficient-circle
minimum, the full-tail polynomial prefactor, the one-degree shift removing
$1/|1-z|^2$, and the constant-amplitude unit-circle law. We use those
results explicitly. The present comparison adds the quantitative endpoint
law for varying geometric states, its finite rank bound, the real
exponential-moment threshold with a finite uniform-integrability estimate,
and the circle-width prefactor with a complete source consumer. The source
infrastructure from [6,7] is retained and credited. The earlier public
working notes [8] record author derivations; they are not relied on as an
independent audit or as a publication-precedence claim. Goertz and Öffner
[9, Theorem 3.1] bound Hahn expansion coefficients using iterates of the
difference operator; the quantitative geometric-state comparison here
retains the state and its two relevant spectral scales.

### 1.2. Notation and evidence

Throughout, $H=N+1$ is the number of points in the uniform grid
$\{0,\ldots,N\}$. Let $E_{N,k}(z)$ be the squared error of orthogonal
projection of $(z^n)$ onto polynomials of degree less than $k$, and write
$p_{H,k}(z)=E_{H-1,k}(z)/\sum_{n=0}^{H-1}|z|^{2n}$ for its relative error.
The Hahn difference operator has eigenvalues $j(j+1)$, and its normalized
spectral masses are denoted by $w_{H,j}(z)$. The two scalings $L/H$ and
$L/H^2$ will always be stated explicitly.

All proofs below are inspectable author arguments. Exact rational and
directed Arb controls support them, with a reproducible supplement.
Floating figures are illustrations, and neither their agreement nor the
previous paper's review is described as an independent audit of these new
results. AI assistance: OpenAI Codex. Code and documentation licenses are
specified in the supplement.

## 2. Finite Laguerre comparison and radial transition

### 2.1. Question and finite upper bound

Let $H=N+1$ and let $E_{N,k}(z)$ be the squared error of projecting
$(z^n)_{n=0}^N$ onto polynomials of degree less than $k$, in uniform counting
measure. Write

$$p_{H,k}(z)=\frac{E_{H-1,k}(z)}{\sum_{n=0}^{H-1}|z|^{2n}}.$$

The global bound in [1] controls proportional ranks with a polynomial
prefactor in $H$. The endpoint comparison below gives a complementary
rank bound and a finite distributional law. It uses the classical Laguerre
recurrence and generating function [2]. The Hahn/dual-Hahn relation is
classical [3], as is the small-degree transition geometry studied in [4].
We claim neither new classical identities nor historical priority for
that geometry.

Assume $|z|=r<1$, set $q=r^2$ and

$$b=\frac{1-r}{1+r},\qquad A=\frac{b k(k+1)}H.$$

For every $1\le k\le H$,

$$p_{H,k}(z)\le\min\left(1,\frac{2e^{-A/2}}{1-q^H}\right). \tag{L1}$$

When $A>1$, the sharper optimized form is

$$p_{H,k}(z)\le\min\left(1,\frac{Ae^{1-A}}{1-q^H}\right). \tag{L2}$$

These bounds have no power of $H$ in their prefactor. They use the worst
phase at fixed modulus and need not improve [1] in other regimes.
For example, $H=10^6$, $|z|=1/2$, $k=10^4$ gives
$p_{H,k}(z)<3.014993\cdot10^{-13}$ for every phase. A sufficient condition
for relative squared error at most $\epsilon$ is

$$k(k+1)\ge\frac{2H}{b}\log\frac{2}{(1-q^H)\epsilon}. \tag{L3}$$

If $|z|>1$, replace $z$ by $1/z$ in every inside-disk formula: reversal
of the grid preserves the polynomial space and normalized residual.
At $z=1$ the residual is zero for $k\ge1$; other unit phases are treated
by [1] and Section 2.7 below. Always $p_{H,0}=1$ and $p_{H,H}=0$.

### 2.2. Finite spectral law

Put

$$\delta=1-|z|^2,\qquad a=|1-z|,\qquad \beta=\frac{\delta}{a^2},$$

and define

$$\begin{aligned}
 C_1&=\frac{2\sqrt2}{a}+\frac{2\sqrt6}{\delta},\\
 C_2&=\frac{\sqrt2\delta}{a^2}+\frac{2\sqrt6}{a},\\
 C_3&=\frac{2\sqrt6\delta}{3a^2},\\
 \eta_H(T)&=\frac2{\pi H}\left(C_1T+\frac{C_2T^2}{2}
                         +\frac{C_3T^3}{3}\right)+\frac{24}{T}.
\end{aligned} \tag{L4}$$

For every $T>0$ and $1\le k\le H$,

$$\left|p_{H,k}(z)-\exp\left(-\frac{\beta k(k+1)}H\right)\right|
 \le\min\left(1,\frac{\eta_H(T)+q^H}{1-q^H}\right). \tag{L5}$$

In particular, writing $h=H\delta\ge1$, one has the simpler uniform bound

$$\left|p_{H,k}(z)-e^{-\beta k(k+1)/H}\right|
 \le\min\left(1,\frac{38h^{-1/4}+e^{-h}}{1-e^{-h}}\right). \tag{L6}$$

The constants are deliberately conservative; no optimal rate is claimed.
Nevertheless, (L6) is uniform in **every phase**. For any sequence $|z_H|<1$
with $H(1-|z_H|^2)\to\infty$, cuts satisfying
$\beta_H k_H(k_H+1)/H\to u$ have residual tending to $e^{-u}$.
For fixed $|z|\ne1$ and $k/\sqrt H\to\kappa$, this gives

$$p_{H,k}(z)\longrightarrow
 \exp\left(-\frac{|1-|z|^2|}{|1-z|^2}\kappa^2\right). \tag{L7}$$

Thus fixed relative capture has a $\sqrt H$ rank scale off the unit circle.
It does not follow that exponentially small error has the same rank scale.

### 2.3. Exact limiting model

The positive uniform Hahn operator is

$$ (Lf)_n=a_n(f_n-f_{n+1})+a_{n-1}(f_n-f_{n-1}),
 \quad a_n=(n+1)(H-1-n),\quad a_{-1}=a_{H-1}=0.$$

Its orthogonal eigenvectors have polynomial degrees $j=0,\ldots,H-1$
and eigenvalues $j(j+1)$ [1,3]. Extend $B_H=L/H$ by zero on indices
$n\ge H$. It is bounded, positive and self-adjoint on $\ell^2(\mathbb N_0)$.
Its edge coefficients are

$$c_n=(n+1)\max\left(1-\frac{n+1}H,0\right).$$

The Laguerre Jacobi operator is

$$ (Jw)_n=(2n+1)w_n-(n+1)w_{n+1}-nw_{n-1}. \tag{L8}$$

The polynomials $L_n(x)=L_n^{(0)}(x)$ form an orthonormal basis in
$L^2([0,\infty),e^{-x}dx)$. Their recurrence identifies $J$ with
multiplication by $x$ under the unitary Laguerre transform; this defines
its positive self-adjoint realization. For the unit vector
$v(z)_n=\sqrt\delta z^n$, the classical generating function [2] gives

$$\mathcal Uv(z)(x)=\frac{\sqrt\delta}{1-z}
                  \exp\left(-\frac{xz}{1-z}\right).$$

Consequently its spectral density for $J$ is exactly

$$|\mathcal Uv(z)(x)|^2e^{-x}=\beta e^{-\beta x}. \tag{L9}$$

The spectral measure of $B_H$ in the same vector is
$q^H\delta_0+(1-q^H)\nu_H$, where $\nu_H$ is the normalized finite Hahn
spectral measure. Its mass at degrees at least $k$ is precisely
$p_{H,k}(z)$. This accounts for the geometric truncation exactly.

### 2.4. Proof of the rank bound

Let $S$ be the diagonal sign matrix $S_{nn}=(-1)^n$. The matrices
$C_H=SB_HS$ and $C=SJS$ have nonnegative entries, with $C_H\le C$
entrywise. For $u_n=\sqrt{1-q}r^n$, finite paths and nonnegative summation
give, for every integer $m\ge0$,

$$0\le\langle v(z),B_H^m v(z)\rangle
 \le\langle u,C_H^m u\rangle
 \le\langle u,C^m u\rangle=m!b^{-m}. \tag{L10}$$

The last equality follows from (L9) applied to $-r$. All these vectors
belong to the domains of the indicated powers. Equivalently one can first
sum finite matrix paths and then take increasing truncations; the geometric
moments are finite. Expanding the bounded operator $e^{sB_H}$ and summing
(L10), for $0<s<b$, yields

$$q^H+(1-q^H)\int e^{sx}\,d\nu_H(x)
 \le\frac1{1-s/b}. \tag{L11}$$

Markov's inequality at $x=k(k+1)/H$, dropping the favorable subtraction
$q^H$ in (L11), gives

$$p_{H,k}(z)\le\frac{e^{-sk(k+1)/H}}{(1-q^H)(1-s/b)}.$$

Take $s=b/2$ for (L1), or $s=b(1-1/A)$ for (L2). This proof uses
entrywise positivity of powers, **not** operator monotonicity of the exponential.

### 2.5. Quantitative operator comparison

Write $D_H=J-B_H$. Its edge coefficients are

$$d_n=\min\left(\frac{(n+1)^2}H,n+1\right),\qquad d_{-1}=0,$$

and satisfy $0\le d_n-d_{n-1}\le(2n+1)/H$ and $d_{n-1}\le n^2/H$.
For any normalized geometric vector $w_n=Cz^n$,

$$ (D_Hw)_n=(1-z)\big[(d_n-d_{n-1})w_n
                              -(1-z)d_{n-1}w_{n-1}\big].$$

Geometric sums and the triangle inequality therefore imply

$$\begin{aligned}
 \|D_Hw\|_2
 &\le\frac{a\sqrt{1+6q+q^2}}{H\delta}
       +\frac{a^2\sqrt{1+11q+11q^2+q^3}}{H\delta^2}\\
 &\le\frac{2\sqrt2 a}{H\delta}+\frac{2\sqrt6 a^2}{H\delta^2}.
\end{aligned} \tag{L12}$$

There is no division by $z$, so $z=0$ is included.
The Laguerre transform also gives the exact unitary flow

$$e^{-itJ}v(z)=\frac{\sqrt\delta}{1+it(1-z)}(z_t^n)_{n\ge0},
 \qquad z_t=\frac{z+it(1-z)}{1+it(1-z)}. \tag{L13}$$

It remains normalized, with

$$1-|z_t|^2=\frac\delta{|1+it(1-z)|^2},\qquad
 |1-z_t|=\frac a{|1+it(1-z)|}.$$

Each such vector belongs to the domain of $J$, and (L13) is differentiable
in $\ell^2$. Duhamel's identity between the bounded self-adjoint $B_H$
and $J$ is consequently valid on $v(z)$. Apply (L12) to (L13), and use
$|1+it(1-z)|\le1+a|t|$. After rescaling time by $\beta$, integration gives

$$\left|\langle v(z),e^{-it\beta B_H}v(z)\rangle
                   -\frac1{1+it}\right|
 \le\frac{C_1|t|+C_2t^2+C_3|t|^3}{H}. \tag{L14}$$

The constants are exactly those in (L4). In particular, the argument
controls the complete characteristic function, not just a few moments.

### 2.6. Finite smoothing and moving cuts

Here is a self-contained smoothing inequality. If CDFs $F,G$ have finite
first moments, $G$ is $M$-Lipschitz, and their characteristic functions are
$f,g$, then

$$\|F-G\|_\infty\le\frac2\pi\int_0^T\frac{|f(t)-g(t)|}{t}\,dt
                            +\frac{24M}{T}. \tag{L15}$$

For completeness, use the symmetric probability density

$$K(x)=\frac3{8\pi}\left(\frac{\sin(x/4)}{x/4}\right)^4.$$

Its Fourier transform is supported on $[-1,1]$ and has modulus at most
one. The normalization follows by Plancherel applied to a triangular
convolution of interval indicators. Splitting the integral at $|x|=4$
and using the bound $\min(1,256/x^4)$ gives
$\int|x|K(x)dx\le12/\pi<4$. For $K_T(x)=TK(Tx)$, Fourier inversion of
the integrable signed CDF gives

$$D_T=\|(F-G)*K_T\|_\infty
 \le\pi^{-1}\int_0^T|f(t)-g(t)|\,dt/t.$$

Let $\Delta=\|F-G\|_\infty$ and approach a positive extremum at $x$.
For $y\le8/T$, monotonicity of $F$ and the Lipschitz bound on $G$ imply
$(F-G)(x+8/T-y)\ge\Delta-M(8/T-y)$, up to the arbitrarily small
extremum approximation. Elsewhere use $F-G\ge-\Delta$. Symmetry and
Markov give $\Pr_K(X>8)\le1/4$, so
$D_T\ge\Delta/2-12M/T$. The negative extremum is treated symmetrically.
This proves (L15). Finite first moments justify the Fourier cancellation
at zero and integrability of the signed CDF.

Apply (L15) to (L14) and the unit exponential CDF, for which $M=1$.
This gives error at most $\eta_H(T)$ for the extended spectral measure.
For a positive cut, remove its atom $q^H$ at zero and divide by $1-q^H$;
the resulting error is at most $(\eta_H(T)+q^H)/(1-q^H)$.
The exponential CDF is continuous, so the same bound holds at left limits,
as needed for the inclusive spectral tail. This proves (L5).

Finally $a\ge1-r=\delta/(1+r)\ge\delta/2$. Hence

$$\eta_H(T)\le\frac2{\pi h}\left[(4\sqrt2+2\sqrt6)T
 +(2\sqrt2+2\sqrt6)T^2+\frac{8\sqrt6}{9}T^3\right]+\frac{24}T.$$

For $h\ge1$ choose $T=h^{1/4}$ and use
$24+2[6\sqrt2+(44/9)\sqrt6]/\pi<38$ and $q^H\le e^{-h}$.
This proves (L6), and the stated limits follow. At $z=0$ the exact identity
$p_{H,k}(0)=((H-1)!)^2/[(H-1-k)!(H-1+k)!]$ for $k<H$ independently
checks the scale and exponent.

### 2.7. Complementary bulk amplitude law

The edge condition $H(1-|z|^2)\to\infty$ excludes a finite radial tilt
of a unit plane wave. There is an elementary complementary statement.
Let $x_n=(n+1/2)/H$, $A\in C^1[0,1]$ be nonzero, and
$f_n=A(x_n)e^{in\theta}$. Put $d=|1-e^{i\theta}|^2>0$,
$V(x)=dx(1-x)$, $A_0=\|A\|_\infty$, $A_1=\|A'\|_\infty$, and
$q_H=H^{-1}\sum|A(x_n)|^2>0$. The normalized spectral measure of
$L/H^2$ in $f$ has moments differing from the pushforward of
$|A(x)|^2dx/\int|A|^2$ under $V$ by at most

$$\frac{A_0^2[r(r+1)/H+r/H^2]+(r+2)A_0A_1/(2H)}{q_H},
 \qquad r\ge1. \tag{L16}$$

To prove this, conjugate $L/H^2$ by the carrier phase, obtaining $T$.
Its absolute row sums are at most one. For a sampled $C^1$ function $p$,

$$\|(T-V)p\|_\infty\le
 \left(\frac{|\sin\theta|}H+\frac d{4H^2}\right)\|p\|_\infty
                       +\frac{\|p'\|_\infty}{2H}.$$

Since $0\le V\le1$ and $\|(V^jA)'\|_\infty\le A_1+4jA_0$,
telescoping $T^rA-V^rA$, pairing with $A$, and midpoint quadrature give
unnormalized error at most

$$A_0^2\left[\frac{r(r+|\sin\theta|)}H+\frac{rd}{4H^2}\right]
                      +\frac{(r+1)A_0A_1}{2H}.$$

The normalization error is at most $A_0A_1/(2H)$, which yields (L16).
Compact support and polynomial approximation then give weak convergence.
The pushforward is atomless for $d>0$, so moving degree cuts are allowed.
For $A(x)=e^{\tau(x-1/2)}$ this proves, at fixed real $\tau$,

$$z_H=e^{\tau/H}e^{i\theta},\quad k/H\to\kappa
 \quad\Longrightarrow\quad
 p_{H,k}(z_H)\to\frac{\sinh\left(\tau\sqrt{(1-4\kappa^2/d)_+}\right)}
                         {\sinh\tau}, \tag{L17}$$

with the continuous square-root interpretation at $\tau=0$.
For $z_H=e^{-\tau_H/H}e^{i\theta}$, fixed $\theta\not\equiv0$,
$\tau_H\to\infty$, $\tau_H=o(H)$, the edge theorem instead gives
$p_{H,k_H}(z_H)\to e^{-u}$ when $2\tau_H k_H^2/(dH^2)\to u$.
This is the intermediate $H/\sqrt{\tau_H}$ rank scale. Neither result
asserts a complete uniform crossover when both phase and radial tilt
approach zero in arbitrary ways.

### 2.8. Evidence and scope

The exact controls check polynomial amplitudes, finite Hahn spectral
identities, endpoint rows, geometric flow, edge increments and the
$z=0$ identity. Directed Arb controls check (L12), moment domination and
967 complete finite tail inequalities. The large-$H$ examples evaluate
proved formulas; they do not construct huge matrices. A separate floating
script computes illustrative finite profiles and checks characteristic
comparisons. These diagnostics are not numerical certificates.

The consumer (L3) is an unweighted approximation rank/depth statement.
It supplies neither original arithmetic rank nor the factorial-weighted
source transfer required for a discriminant theorem. These rank results alone give no new discriminant
endpoint, source correction, census or classification. Nothing
here changes the imported $D\le498$ consequence and its $D\le499$
qualification in [1]. The two limiting laws are logically distinct from
exponentially small determinant depth. The next source use must explicitly
account for that distinction.

Section 3 makes this distinction precise for real arguments.

## 3. Exponential moments and the critical radius

### 3.1. Statement

Fix real $-1<z<1$, put $\beta=(1+z)/(1-z)>0$, and let $w_{H,j}(z)$ be
the normalized squared Hahn component of degree $j$. Thus
$\sum_{j=0}^{H-1}w_{H,j}=1$. Define

$$M_H(s)=\sum_{j=0}^{H-1}w_{H,j}(z)e^{s j(j+1)/H},\qquad s\ge0,$$

and

$$I_\beta(\mu)=2\int_0^\mu\operatorname{arsinh}
                 \frac{\beta t}{\sqrt{1-t^2}}\,dt,
 \quad I_\beta(1)=2\log(1+\beta),\quad
 s_c=\inf_{0<\mu\le1}\frac{I_\beta(\mu)}{\mu^2}. \tag{M1}$$

Then

$$\lim_{H\to\infty}\frac{\log M_H(s)}H
 =\max_{0\le\mu\le1}\{s\mu^2-I_\beta(\mu)\}. \tag{M2}$$

Moreover,

$$M_H(s)\longrightarrow\frac\beta{\beta-s}\quad(0\le s<s_c),
 \qquad M_H(s)\longrightarrow\infty\quad(s\ge s_c). \tag{M3}$$

The critical tilt has a simple classification:

- If $0<\beta\le\sqrt3$, then $s_c=\beta$.
- If $\beta>\sqrt3$, then $s_c<\beta$, and the infimum in (M1) is
  attained at a unique point $\mu_*\in(0,1)$.

Thus the transition occurs at $z=2-\sqrt3$. The weak exponential spectral
law remains valid on both sides. Above this radius it predicts a larger
moment domain than the finite Hahn sequence actually has.

For $z=1/2$, directed evaluations certify

$$0.83418707356274<\mu_*<0.83418707356276,
 \qquad 2.65831716242231<s_c<2.65831716242258<\beta=3.$$

For $z=9/10$,

$$5.98679552729301<s_c<5.98679552729350<\beta=19.$$

These are rigorous brackets of the one-dimensional quantities, conditional
on the author proof identifying their role. The proof and code do not claim
an independent audit, a new weighted source estimate or an arithmetic result.

### 3.2. Real saddle and coefficient asymptotics

Use the exact Hahn normalization from [1]. Set $\lambda=j+1$,
$L=H-\lambda$, $\mu=\lambda/H$ and

$$F(t)=\frac1{(1-t)(1-zt)},\qquad P_j(z)=[t^L]F(t)^\lambda.$$

For real $-1<z<1$, $F$ has strictly positive Taylor coefficients and
radius of convergence one. For $z<0$ this also follows from
$F(t)=[1-(1+z)t-|z|t^2]^{-1}$. Its spread is infinite, and its
coefficient support has span one. The unique positive saddle satisfies

$$\frac{sF'(s)}{F(s)}=\frac{1-\mu}{\mu},\qquad
 (1+\mu)zs^2-(1+z)s+1-\mu=0.$$

Let

$$\sigma^2=s\frac d{ds}\frac{sF'(s)}{F(s)}>0.$$

The classical large-powers theorem of Flajolet–Sedgewick [5, Theorem VIII.8]
therefore gives, uniformly on compact subintervals of $0<\mu<1$,

$$P_j(z)=\frac{F(s)^\lambda s^{-L}}{\sqrt{2\pi\lambda\sigma^2}}
                      (1+o(1)). \tag{M4}$$

All its hypotheses have been stated above. One can also see (M4) directly:
tilting the positive coefficient distribution at $s$ gives mean $L/\lambda$
and variance $\sigma^2$. Its characteristic function has a strict modulus
gap away from zero and a Gaussian expansion at zero. Splitting the
coefficient circle at $|\phi|=\lambda^{-2/5}$ gives the Gaussian integral;
compactness in $\mu$ makes the expansion and gap uniform. This is the
standard theorem, not a new local limit method.

Differentiating the real rate $G_z$ of [1] at its saddle gives

$$-G_z'(\mu)=2\operatorname{arsinh}
                   \frac{\beta\mu}{\sqrt{1-\mu^2}}.$$

The boundary value is $G_z(0)=0$, so $-G_z=I_\beta$.
Combining (M4) with Stirling's formula in the exact Hahn component gives

$$w_{H,j}(z)=D_z(\mu)e^{-H I_\beta(\mu)}(1+o(1)),
 \quad D_z(\mu)=\frac{2\beta\sqrt{1-\mu^2}}{\mu\sigma^2}>0, \tag{M5}$$

uniformly on compact subintervals. The formula uses $\mu=(j+1)/H$,
so the tilted component contains the additional factor $e^{-s\mu}$.

At the endpoints, the degree-zero component is exactly
$\beta(1-z^H)/[H(1+z^H)]$, and the unnormalized terminal component is
$|1-z|^{2H-2}/\binom{2H-2}{H-1}$. These give rates zero and
$-I_\beta(1)$ respectively.

The accepted finite bound in [1] gives, at every degree including the
terminal one,

$$w_{H,j}(z)\le\frac{4e^3H(H+1)^3}{(1-z)^2}
                   e^{-H I_\beta((j+1)/H)}. \tag{M6}$$

Summing at most $H$ terms proves the upper bound in (M2). For a positive
interior maximizer, (M5) proves the matching lower bound; endpoint
maximizers use the exact formulas just stated. A zero supremum is already
bounded below at exponential scale by the degree-zero component. This
proves (M2).

### 3.3. Why the critical radius is exact

Write $h(\mu)=\operatorname{arsinh}(\beta\mu/\sqrt{1-\mu^2})$ and
$F_*(\mu)=\mu h(\mu)-I_\beta(\mu)$. Then

$$\left(\frac{I_\beta(\mu)}{\mu^2}\right)'=
 \frac{2F_*(\mu)}{\mu^3},\quad
 F_*'=\mu h'-h,\quad F_*''=\mu h'',$$

and direct differentiation gives

$$h''(\mu)=\frac{\beta\mu[3-\beta^2+3(\beta^2-1)\mu^2]}
 {(1-\mu^2)^2[1+(\beta^2-1)\mu^2]^{3/2}}. \tag{M7}$$

If $0<\beta\le\sqrt3$, its numerator is positive on $(0,1)$.
For $\beta<1$ its smallest bracket value at $\mu=1$ is $2\beta^2>0$.
Thus $F_*>0$, because $F_*(0)=F_*'(0)=0$, and $I_\beta/\mu^2$ increases
from its value $\beta$ at zero.

If $\beta>\sqrt3$, (M7) changes sign exactly once, from negative to
positive. Hence $F_*'$ first decreases and then increases, and tends to
infinity at one. It has one interior zero. In turn, $F_*$ first decreases
and then increases, with $F_*(\mu)\to\infty$ as $\mu\to1$. It has one
interior zero $\mu_*$, after its minimum. This is the unique minimum of
$I_\beta/\mu^2$, strictly below $\beta$. Also $F_*'(\mu_*)>0$, which
makes this minimum nondegenerate. This proves the classification without
a numerical minimization.

### 3.4. A finite prefactor for small and moderate degrees

To infer exponential-moment convergence one needs more than (M6). Here is
a complete finite replacement. Put $r=|z|$, $d=(1-z)^2$, and

$$C_z=\frac{8\pi^2e^{1/6}(1+r)^2}{d(1-r)^2}.$$

For $2\le\lambda\le H/2$,

$$w_{H,\lambda-1}(z)\le C_z\frac\lambda H
                          e^{-H I_\beta(\lambda/H)}. \tag{M8}$$

Indeed, set $Q=(1-s)(1-zs)$ and $v=|z|s^2$. The global coefficient-circle
identity and radius inequality of [1] imply

$$|(1-se^{i\phi})(1-zse^{i\phi})|^2
 \ge Q^2+2\gamma(1-\cos\phi),$$

where

$$\gamma=(1-v)[1-\mu-(1+\mu)v]
 \ge(1-r)^2(1-\mu),\qquad Q^2\le\mu^2(1+r)^2.$$

Use $1-\cos\phi\ge2\phi^2/\pi^2$ on $[-\pi,\pi]$ and extend the
resulting integral to the real line. The squared ratio between the
Cauchy integral bound and its maximum-integrand bound is at most

$$\frac{\pi Q^2}{16\gamma}
 \left(\frac{\Gamma((\lambda-1)/2)}{\Gamma(\lambda/2)}\right)^2
 \le\frac{\pi\lambda Q^2}{8(\lambda-1)^2\gamma}. \tag{M9}$$

The Gamma inequality follows from log convexity:
$\Gamma(x+1/2)/\Gamma(x)\ge x/\sqrt{x+1/2}$ for $x>0$.
For $\lambda\le H/2$ and $\lambda\ge2$, (M9) is at most
$\pi\lambda(1+r)^2/[H^2(1-r)^2]$.

The exact factorial prefactor is

$$\frac{(2\lambda-1)(H+\lambda)}{\lambda^2d}
 \frac{\lambda!^2(H-\lambda)!}{(H+\lambda)!}\,d^\lambda.$$

The inequalities
$\sqrt{2\pi n}(n/e)^n\le n!\le\sqrt{2\pi n}(n/e)^ne^{1/(12n)}$
show that, after extracting its entropy exponential, this is at most
$6\pi He^{1/8}/d$. Multiplying by (M9), then using the total norm at
least one, proves the conservative (M8). All indices in this argument
are positive; the remaining degrees are covered by (M6).

If $0\le s<s_c$ and $\epsilon=s_c-s$, (M8), (M6), and the degree-zero
bound yield the explicit estimate

$$M_H(s)\le1+C_z\left(\frac1{2\epsilon}
                      +\frac{\sqrt\pi}{2\sqrt\epsilon}\right)
             +\frac{32e^3}{d}\left(\frac{20}{e\epsilon}\right)^5. \tag{M10}$$

For the low degrees, compare
$\sum_{\lambda\ge1}(\lambda/H)e^{-\epsilon\lambda^2/H}$ with the
integral of $(x+1)e^{-\epsilon x^2/H}/H$ on $[0,\infty)$.
For $\lambda>H/2$, the bound is at most
$32e^3H^5e^{-\epsilon H/4}/d$, whose supremum is bounded by the final
term of (M10). The same argument covers $H<4$ with no low-degree terms.

Choose $s<t<s_c$ and apply (M10) at $t$. This proves uniform integrability
of $e^{sX_H}$. The weak Laguerre law in Section 2 then proves the first
part of (M3). For $s>s_c$, (M2) proves exponential divergence.

### 3.5. The critical tilt

If $s_c=\beta$, the weak limit and truncation from below give divergence
at $s_c$, since the unit exponential moment of rate $\beta$ is infinite.

If $\beta>\sqrt3$, define $J(\mu)=I_\beta(\mu)-s_c\mu^2$.
It is nonnegative, vanishes only at zero and $\mu_*$, and
$J''(\mu_*)=2F_*'(\mu_*)/\mu_*>0$. The uniform asymptotic (M5) applies
in a fixed neighborhood of $\mu_*$. In a band of width $H^{-1/2}$,
there are order $\sqrt H$ terms and each tilted term is bounded below
by a fixed positive constant. Thus $M_H(s_c)\to\infty$, proving (M3).
In fact the same estimates give

$$\frac{M_H(s_c)}{\sqrt H}\longrightarrow
 D_z(\mu_*)e^{-s_c\mu_*}\sqrt{\frac{2\pi}{J''(\mu_*)}}. \tag{M11}$$

To justify localization, near zero use (M8) and
$I_\beta(\mu)/\mu^2\to\beta>s_c$, giving a uniformly bounded sum.
On compact sets away from zero and $\mu_*$, use (M5) or (M6) and the
strict positive gap in $J$. The endpoint one also has a positive gap,
since the unique minimum of $I_\beta/\mu^2$ is interior. Finally apply
the ordinary Gaussian Riemann-sum estimate around the nondegenerate
minimum. This proves (M11). The endpoint critical growth rates are proved next.

### 3.6. Critical growth and joint scaling

#### 3.6.1. Results and relation to the existing theorem

Retain the real-state notation above. At $s_c=\beta$, the critical
growth rates are:

$$\frac{M_H(\beta)}{\sqrt H}\longrightarrow
 \frac{\beta\sqrt\pi}{2\sqrt{c_4}},\qquad
 c_4=\frac{\beta(3-\beta^2)}{12},\quad 0<\beta<\sqrt3. \tag{C1}$$

At the boundary, with $\beta_0=\sqrt3$,

$$\frac{M_H(\beta_0)}{H^{2/3}}\longrightarrow
 \frac{\beta_0\Gamma(1/3)}{3c_6^{1/3}},\qquad
 c_6=\frac{\beta_0}{10}. \tag{C2}$$

There is also a joint scaling limit. Suppose
$\beta_H=\beta_0+aH^{-1/3}+o(H^{-1/3})$ and
$s_H=\beta_H+bH^{-2/3}+o(H^{-2/3})$, for fixed real $a,b$, with $M_H$ evaluated at
$z_H=(\beta_H-1)/(\beta_H+1)$. Then

$$H^{-2/3}M_H(s_H)\longrightarrow
 2\beta_0\int_0^\infty u\exp\left(
 b u^2+\frac a2u^4-\frac{\beta_0}{10}u^6\right)\,du. \tag{C3}$$

Equivalently the limit is
$\beta_0\int_0^\infty\exp(bv+(a/2)v^2-(\beta_0/10)v^3)\,dv$.
The $H^{2/3}$ boundary and the scaling integral are ordinary degenerate
Laplace behavior applied to the finite Hahn action. The classical Laplace framework is described
in [10, Section 2.3(iii)]; no new general saddle method is claimed.

#### 3.6.2. A coefficient asymptotic as the degree fraction vanishes

Write $\lambda=j+1$, $\mu=\lambda/H$, $L=H-\lambda$ and
$F(t)=((1-t)(1-zt))^{-1}$. The unique positive saddle $r$ satisfies
$rF'(r)/F(r)=L/\lambda$. Let
$\sigma^2=r(d/dr)(rF'/F)$, and set $\delta=1-r$. Uniformly for $z$ in
a compact subinterval of $(-1,1)$, as $\mu\to0$,

$$\delta=\mu(1+O(\mu)),\qquad
 \sigma^2=\mu^{-2}(1+O(\mu)). \tag{C4}$$

If also $\lambda\to\infty$, the usual coefficient saddle is uniform:

$$[t^L]F(t)^\lambda=
 \frac{F(r)^\lambda r^{-L}}{\sqrt{2\pi\lambda\sigma^2}}(1+o(1)). \tag{C5}$$

Here is a proof of the uniformity needed beyond a fixed compact range
of $\mu$. On the coefficient circle the centered logarithm is
$\psi(\phi)=\log(F(re^{i\phi})/F(r))-i(L/\lambda)\phi$.
It satisfies $\psi'(0)=0$, $\psi''(0)=-\sigma^2$, and its third
derivative is $O(\delta^{-3})$ on $|\phi|\le\delta/2$, uniformly in
the stated compact set of $z$. Thus on
$|\phi|\le\delta\lambda^{-2/5}$ the quadratic expansion has
uniform remainder $O(\lambda^{-1/5})$ after multiplication by $\lambda$.
Changing variable to $u=\sqrt\lambda\sigma\phi$ gives the full
Gaussian integral up to relative $o(1)$.

For the complementary arc use the already proved coefficient-circle
bound, with $Q=(1-r)(1-zr)$:

$$|(1-re^{i\phi})(1-zre^{i\phi})|^2
 \ge Q^2+2\gamma(1-\cos\phi),\qquad
 \gamma\ge(1-|z|)^2(1-\mu).$$

Since $Q\asymp\delta$ and $1-\cos\phi\ge2\phi^2/\pi^2$, the
modulus of the integrand relative to its value at zero is bounded by
$(1+c\phi^2/\delta^2)^{-\lambda/2}$ for a uniform $c>0$.
Its integral over $|\phi|\ge\delta\lambda^{-2/5}$ is
$o(\delta/\sqrt\lambda)$. To see this without a relation between
$H$ and $\lambda$, substitute $y=\phi/\delta$ and bound one half of
the power by its value at $|y|=\lambda^{-2/5}$; integrating the other
half over the real line costs $O(\lambda^{-1/2})$. This proves (C5).

Combining (C5) with Stirling in the exact component formula, uniformly
as $\mu\to0$ and $\lambda\to\infty$, yields

$$w_{H,\lambda-1}(z)=
 2\beta\mu\,e^{-HI_\beta(\mu)}(1+o(1)), \tag{C6}$$

where $I_\beta(\mu)=2\int_0^\mu
\operatorname{arsinh}(\beta t/\sqrt{1-t^2})\,dt$.
Indeed the unnormalized entropy prefactor and (C5) give
$2\sqrt{1-\mu^2}/[(1-z)^2\mu\sigma^2]$ up to $1+o(1)$;
division by the geometric norm tends to multiplication by $1-z^2$.
Equation (C4) then gives (C6). All Stirling arguments grow because
$\lambda\to\infty$ and $\mu\to0$. The same proof is uniform for
$\beta$ near $\beta_0$.

#### 3.6.3. Localization and the critical constants

The action expansion is

$$I_\beta(\mu)=\beta\mu^2+c_4(\beta)\mu^4
 +c_6(\beta)\mu^6+O(\mu^8),$$

$$c_4(\beta)=\frac{\beta(3-\beta^2)}{12},\qquad
 c_6(\beta)=\frac{\beta}{8}-\frac{\beta^3}{12}
                         +\frac{\beta^5}{40}. \tag{C7}$$

For fixed $0<\beta<\beta_0$, the strict monotonicity already proved
for $I_\beta(\mu)/\mu^2$ implies
$I_\beta(\mu)-\beta\mu^2>0$ away from zero. Near zero it is
$c_4\mu^4+O(\mu^6)$. Thus (C6) and the change of variable
$\mu=H^{-1/4}u$ give

$$H^{-1/2}M_H(\beta)\to
 2\beta\int_0^\infty ue^{-c_4u^4}\,du
 =\frac{\beta\sqrt\pi}{2\sqrt{c_4}}.$$

The tilt at $j=\lambda-1$ contributes
$e^{s j(j+1)/H}=e^{Hs\mu^2-s\mu}$; the latter factor tends to one
on this scale. At $\beta_0$, $c_4=0$, $c_6=\beta_0/10>0$, and the
same argument with $\mu=H^{-1/6}u$ gives (C2).

For completeness, the Riemann-sum limits have a uniform dominating
bound. The finite component estimate already proved in Section 3.4
is $w_{H,\lambda-1}\le C_z(\lambda/H)e^{-HI_\beta(\lambda/H)}$
for $2\le\lambda\le H/2$, with $C_z$ bounded on compact sets of $z$.
Near zero, use $I_\beta-\beta\mu^2\ge c\mu^4$ in (C1), or
$\ge c\mu^6$ in (C2). For $\mu$ bounded away from zero, the earlier
all-degree polynomial-prefactor bound and a positive action gap give
an exponentially negligible sum, including the terminal degree.
The degree-zero contribution and finitely many small $\lambda$ vanish
after division by the indicated power of $H$. At the lower limit of
the rescaled integral, the finite component bound controls the sum by
a constant times the square of the rescaled cutoff. On compact
positive rescaled intervals, (C6) is uniform. These observations justify
the limit at both ends and not merely pointwise asymptotics.

#### 3.6.4. Joint scaling around the boundary

Since $c_4'(\beta_0)=-1/2$, (C7) and $\mu=H^{-1/6}u$ give

$$H(s_H\mu^2-I_{\beta_H}(\mu))
 \to bu^2+(a/2)u^4-(\beta_0/10)u^6.$$

For sufficiently small fixed $\mu$, Taylor's theorem uniformly near
$\beta_0$ gives

$$I_{\beta_H}(\mu)-s_H\mu^2
 \ge c\mu^6-C H^{-1/3}\mu^4-C H^{-2/3}\mu^2,$$

with $c>0$ and $C<\infty$ depending on bounded $a,b$. Away from zero,
strict positivity of $I_{\beta_0}-\beta_0\mu^2$ persists. The same
finite component estimates therefore dominate the rescaled sum by
a constant times $u\exp(Cu^2+Cu^4-cu^6)$. Uniform (C6), the vanishing
factor $e^{-s_H\mu}$, and the Riemann-sum argument prove (C3).


### 3.7. Evidence, implication and limits

The new recurrence checker compares 250 finite components against direct
exact binomial sums and checks the critical coefficients. Optional directed
moment evaluations and floating crossover quadratures illustrate the limits;
they certify no convergence rate. These checks use five CPU workers at most.



The checker verifies 513 finite instances of (M8) with exact rational
Hahn coefficients and directed Arb evaluations. Directed signs certify
the listed critical-point brackets; uniqueness comes from (M7).
At $H=8$, $z=1/2$, $s=27/10$, the extended geometric-state moment is
$11.3766730869\ldots>10$, whereas the limiting exponential formula is
$\beta/(\beta-s)=10$. This is a finite illustration of the failed
naive phase-sensitive moment domination, not the proof of (M2)–(M3).

The practical implication is a proof constraint: the weak spectral law
identifies ranks for fixed relative capture, while exponentially small
residuals must respect the full action $I_\beta$. One cannot replace the
worst-phase rate in the finite Chernoff theorem merely by the phase rate
of the weak limit. The finite upper bound (M8) and moment bound (M10) are
usable replacements in their stated real-argument domain. They do not
supply a complex weighted-source transfer or a new discriminant result.

## 4. Complex circle width and the determinant-source transfer

### 4.1. The bound

Let $H=N+1$ and let $E_{N,k}(z)$ be the squared uniform-grid error of
projecting $(z^n)_{n=0}^N$ onto polynomials of degree less than $k$.
Use the global rate $G_z(\mu)$ of Paper 40/v1 [1], recalled below.
For $1\le k\le N$, set $\nu=k/H$ and suppose

$$\tau=-G_z'(\nu)>0.$$

Define

$$\begin{aligned}
P(\nu,\tau)=\frac1{\nu^2\sqrt{1-\nu}}\bigg[2+
 \frac2{\sqrt{e\tau}}+
 \frac{2\sqrt2\pi^2e^{1/6}}{1-e^{-2\tau}}
 \left(\frac{\sqrt2}{1-e^{-\tau}}+\frac4{e\tau}\right)\bigg].
\end{aligned} \tag{W1}$$

Then the complete residual satisfies

$$E_{N,k}(z)\le\min\left\{\sum_{n=0}^N|z|^{2n},
                  P(\nu,\tau)e^{H G_z(\nu)}\right\}. \tag{W2}$$

At fixed $\nu,\tau$, this prefactor is independent of $H$. It includes
the terminal degree and has no singular factor $1/|1-z|^2$.
For $z=1$, the error is zero. For nonunit modulus the slope is positive
at every positive rank. On the unit circle the condition is
$\nu>|1-z|/2$. Below that threshold no assertion replacing [1] is made.
The formula can be conservative when $\tau$ is small or $\nu$ approaches one.

The ingredients are classical Cauchy integration, Gamma log convexity,
Stirling bounds, and the global saddle identities proved in [1].
Keeping the width of the coefficient circle, rather than only its maximum,
is the new finite comparison here. The real low-degree precursor appears in Section 3.4. Neither classical saddle methods nor
orthogonal-polynomial transition geometry are claimed as new.

### 4.2. Rate, derivative and concavity

Put $d=|1-z|^2$, $a=1-\mu$, $b=1+\mu$, and choose the smaller-modulus
root of

$$bzs^2-(1+z)s+a=0,$$

taking $s=a$ at $z=0$. Set $Q=(1-s)(1-zs)$, $V=zs^2$,
$f(x)=x\log x$. The rate is

$$G_z(\mu)=\mu\log d+2f(\mu)+f(a)-f(b)
                  -2a\log|s|-2\mu\log|Q|,$$

with $G_z(1)=\log(d/4)$. The identities in [1] give

$$|V|\le a/b,\quad Q=\mu(1-V),\quad
 e^{G_z'(\mu)}=\frac{|a^2-b^2V|}{ab|1-V|}. \tag{W3}$$

For $|z|<1$, put $\xi=(1+z)/(1-z)$, so $\Re\xi>0$.
Algebra in (W3), with the branch continued from $\mu=0$, gives

$$-G_z'(\mu)=2\Re\operatorname{arsinh}
            \frac{\mu\xi}{\sqrt{1-\mu^2}},$$

and

$$-G_z''(\mu)=2\Re\frac{\xi}
 {(1-\mu^2)\sqrt{1+(\xi^2-1)\mu^2}}>0. \tag{W4}$$

The square root in (W4) has positive real part and imaginary part with the
same sign as $\Im\xi$. This proves the final inequality. The inverse
hyperbolic sine is analytic in the right half-plane and has positive real
part there; equivalently its exponential is
$\sqrt{1+\mu^2\xi^2/(1-\mu^2)}+\mu\xi/\sqrt{1-\mu^2}$.
This expression verifies the branch in (W3).

Reciprocity $G_z=\log|z|^2+G_{1/z}$ proves concavity outside the disk.
On the unit circle, with $0<d<4$, the slope is zero up to $\mu=\sqrt d/2$
and is

$$2\operatorname{arcosh}\left(
 \frac{\mu\sqrt{(4-d)/d}}{\sqrt{1-\mu^2}}\right)$$

above it; it increases there. At $z=-1$ it stays zero for $\mu<1$.
Thus $G_z$ is concave in degree throughout its domain and
$G_z(0)=\log\max(1,|z|^2)$.

### 4.3. Width of the coefficient circle

For a component of degree $j$, write $\lambda=j+1$, $L=H-\lambda$,
$\mu=\lambda/H$. The exact generating expression is

$$P_j(z)=[t^L]((1-t)(1-zt))^{-\lambda}.$$

Assume $\lambda\ge2$, $L\ge1$ and $\tau_\mu=-G_z'(\mu)>0$.
Write $v=|V|$ and

$$\gamma=(1-v)(a-bv)>0.$$

The global coefficient-circle identity of [1] gives

$$|(1-se^{i\phi})(1-zse^{i\phi})|^2
                  \ge|Q|^2+2\gamma(1-\cos\phi). \tag{W5}$$

Applying Cauchy's formula and $1-\cos\phi\ge2\phi^2/\pi^2$, and
extending the resulting integral to the real line, shows that the square
of the ratio between the integral and its maximum-integrand bound is at most

$$\frac{\pi|Q|^2}{16\gamma}
 \left(\frac{\Gamma((\lambda-1)/2)}{\Gamma(\lambda/2)}\right)^2
 \le\frac{\pi\lambda|Q|^2}{8(\lambda-1)^2\gamma}. \tag{W6}$$

Here log convexity gives
$\Gamma(x+1/2)/\Gamma(x)\ge x/\sqrt{x+1/2}$.
The squared identity in (W3) gives exactly

$$1-e^{-2\tau_\mu}
 =\frac{4\mu(a-bv)(a+bv)}{a^2b^2|1-V|^2}.$$

Since $v\le a/b$, it follows that

$$\frac{|Q|^2}{\gamma}
 =\frac{4\mu^3(a+bv)}{(1-e^{-2\tau_\mu})a^2b^2(1-v)}
 \le\frac{4\mu^2}{(1-e^{-2\tau_\mu})ab}. \tag{W7}$$

The exact unnormalized squared component is

$$U_j=\frac{(2\lambda-1)(H+\lambda)}{\lambda^2d}
       \frac{\lambda!^2L!}{(H+\lambda)!}\,d^\lambda|P_j(z)|^2.$$

The factorial inequalities
$\sqrt{2\pi n}(n/e)^n\le n!\le\sqrt{2\pi n}(n/e)^ne^{1/(12n)}$
give its entropy prefactor at most
$4\pi H\sqrt{ab}\,e^{1/6}/d$ for $\lambda\ge2,L\ge1$.
Combining this with (W6)–(W7) and
$\lambda^2/(\lambda-1)^2\le4$ yields

$$U_j\le\frac{8\pi^2e^{1/6}\mu}
 {d(1-e^{-2\tau_\mu})\sqrt{1-\mu^2}}e^{H G_z(\mu)}. \tag{W8}$$

### 4.4. Complete tail and the terminal degree

First suppose $k\le H-2$. Put
$\mu_0=(k+1)/H$, $L_0=H-k-1\ge1$, and $\tau=-G_z'(k/H)>0$.
Concavity gives, for $m\ge0$,

$$G_z(\mu_0+m/H)\le G_z(\mu_0)-\tau m/H,
 \qquad \tau_{\mu_0+m/H}\ge\tau.$$

For $0<q<1$ and integer $L\ge1$,

$$\sqrt L\sum_{m=0}^{L-1}\frac{q^m}{\sqrt{L-m}}
 \le\frac{\sqrt2}{1-q}+\frac4{e|\log q|}. \tag{W9}$$

To prove this, split at $m=L/2$. The first part is bounded by the
geometric sum with factor $\sqrt2$. The second part is at most
$2Lq^{L/2}$, since $\sum_{t=1}^L t^{-1/2}\le2\sqrt L$.
Finally $L e^{-L|\log q|/2}\le2/(e|\log q|)$.

Since $\mu/\sqrt{1+\mu}\le1$, summing (W8) with (W9) bounds all
nonterminal degrees by

$$\frac{8\pi^2e^{1/6}}{d(1-e^{-2\tau})\sqrt{1-\mu_0}}
 \left(\frac{\sqrt2}{1-e^{-\tau}}+\frac4{e\tau}\right)
 e^{H G_z(\mu_0)}. \tag{W10}$$

The terminal component has the exact value
$U_N=d^{H-1}/\binom{2H-2}{H-1}$. The central-binomial lower bound
$\binom{2n}{n}\ge4^n/(2\sqrt n)$ for $n\ge1$ gives
$U_N\le8\sqrt H\,e^{HG_z(1)}/d$.
Concavity and $\sqrt H e^{-cH}\le1/\sqrt{2ec}$ then give

$$U_N\le\frac8{d\sqrt{2e\tau(1-\mu_0)}}e^{H G_z(\mu_0)}. \tag{W11}$$

The one-step inequality from [1] is

$$\frac{e^{H G_z(\nu+1/H)}}d
                  \le\frac{e^{H G_z(\nu)}}{4\nu^2}. \tag{W12}$$

Use (W12) in (W10)–(W11), together with
$1-\mu_0\ge(1-\nu)/2$, to obtain (W1)–(W2) without the initial $2$
in (W1). If $k=H-1$, only the terminal term remains. Apply (W12) directly
at the endpoint to get
$U_N\le2e^{HG_z(\nu)}/[\nu^2\sqrt{1-\nu}]$.
The extra $2$ in (W1) covers this case and completes the proof.

### 4.5. Source consumer with exact provenance

The source is unchanged from [1]:

$$D=347,\quad K=17,\quad R=907199985,\quad S=53364705,
 \quad n=208918400,\quad a_0=27/50,\quad B=e^{9/10}.$$

The forty bins, ranks, centers $g$ and basic depths are imported verbatim
from Paper 38/v1 [6]. The arithmetic/source summary is imported from
Paper 35/v2 [7]. The accepted Paper 40/v1 rate-depth certificate is also
included verbatim. Its 1,965,100-cell execution is **not rerun here**;
its proved rate-depth inequalities are the imported input for the new transfer.

The new computation proves only the additional slope hypothesis, on the
full coherent domain. For each row let

$$H_{\max,\mathrm{row}}=\left\lfloor\frac{R-1-d_{\rm lo}}{K+1}\right\rfloor+1,
 \qquad \nu_{\min,\mathrm{row}}=k/H_{\max,\mathrm{row}}.$$

The physical geometry uses $q=|u|^2$, $v=|\eta|^2/R$, $j_0=J/R$,
$\chi=\max(0,\log(Bq))$, $c=e^{\chi/K}$, and

$$|z|^2=Bqv/g^2,\qquad
 \Re z\ge\frac{\sqrt{B/a_0}}{2g}(v+a_0q-j_0c). \tag{W13}$$

The same sixteen enlarged radial-zone bounds and disk exclusions as in [1]
are used. At each remaining two-dimensional $(q,v)$ cell the checker
bounds $G_z(\nu_{\min,\mathrm{row}})$ at the largest feasible phase,
using the real radical evaluator of [1]. It proves

$$\log\max(1,|z|^2)-G_z(\nu_{\min,\mathrm{row}})
                         >\nu_{\min,\mathrm{row}}/2. \tag{W14}$$

Concavity and the exact value of $G_z(0)$ imply
$-G_z'(\nu_{\min,\mathrm{row}})>1/2$. The slope increases with degree,
so this holds for every smaller physical grid in that charge bin.
Phase ordering of the rate justifies using (W13)'s boundary in (W14);
no separate phase monotonicity of the slope or residual is assumed.
Points with $z=1$ have zero residual and cause no exception.

All forty rows pass: **7,808 visited cells, maximum depth 8**, 160-bit
geometry, five CPU workers. This is a new slope cover, not a replacement
execution of the imported rate-depth cover.

For the complete source, $H\le H_*=50,400,000$,
$\nu\ge\nu_*:=2810279/3543750$, and
$1-\nu\ge1/H_*$. The bracket in (W1) decreases with $\tau$.
Consequently (W1) is bounded by $P_*$ obtained by using
$\tau=1/2$, $\nu^{-2}=\nu_*^{-2}$ and
$(1-\nu)^{-1/2}=\sqrt{H_*}$. Directed accounting gives

$$P_*<3891980.645002.$$

The accepted physical factorial maximum and trial restriction now give
weighted error at most $P_*e^{-Rh}/S$ for each bin. The coherent-disk
comparison contributes $eJ^{3/2}$ and the node sum contributes $n$, exactly
as in [1]. Thus the new common trace factor is

$$C_*^{\rm width}=\frac{neJ_{\max}^{3/2}P_*}{S},
 \qquad \log C_*^{\rm width}<45.838466986595. \tag{W15}$$

The old value from [1] was less than 122.805350405714; the directed saving
is greater than 76.966883419118. Applying the same determinant-transfer
formula and complement counts gives

$$\text{metric correction}>0.0030166950513699,
 \qquad\text{imported-source gap}>0.0426264385022201. \tag{W16}$$

This remains below the accepted endpoint-weight refinement in [6]. The
numeric gain is small; the contribution is the finite prefactor theorem
and its fully accounted transfer at the unchanged contract. No new
endpoint, census, classification or all-scale theorem is asserted.
The imported $D\le498$ consequence retains its $D\le499$ qualification.

### 4.6. Evidence and reproducibility

The finite checker compares exact rational Hahn residuals with directed
Arb evaluations:1,303 derivative identities,1,303 concavity checks,
1,237 component bounds,1,303 complete tails and1,220 slope comparisons.
These are author controls, not the proof or an independent audit.
The source stage checks hashes, reconstructs all rank/complement counts,
executes the new slope cover and evaluates (W15)–(W16). Inputs and their
public supplement provenance are listed in `public_input_verification.json`.
The earlier arithmetic and full rate-depth computation remain imported.

## 5. Reproducibility and limits

Run `python replay.py` in the supplement with Python 3.12 and
python-flint 0.9.0. Six stages verify the exact amplitude/operator algebra,
directed finite edge and Chernoff bounds, real moment threshold brackets,
complex circle-width bounds, the new slope-cover transfer, and the critical
coefficient recurrence. All scientific
outputs must match the retained files after runtime is excluded. The only
parallel stage uses five single-threaded CPU workers; no GPU is required.
The expected runtime is a few seconds.

![Finite Hahn residuals approach the exponential endpoint profile and the hyperbolic-sine profile of a finite radial tilt.](supplement/figures/spectral_scales.png)

Figure 1. Left: a fixed negative radius, with scaled degree cut
$\beta k(k+1)/H$. Right: finite radial tilts of the carrier $(3+4i)/5$
on 2048 points. Lines are proved limiting profiles; points are floating
finite projections. Raw plotted values and optional plotting code are
included. No convergence rate is certified by the picture.

The proof of the source consumer imports the accepted rate-depth theorem
and public certificate from Paper 40/v1, the original allocation from
Paper 38/v1, and the arithmetic/source summary from Paper 35/v2. Their bytes
are checked and included. The earlier million-cell rate-depth cover and
arithmetic are not rerun by this supplement. Only the additional slope
cover and new finite accounting are executed. This distinction is part
of the result's reproducibility claim.

The uniform endpoint law controls absolute distributional error; it alone
does not give an exponentially small residual. The real moment theorem
has its stated real-argument domain. The circle-width bound requires
positive slope and may be conservative near its boundary. The physical
source retains the existing factorial-weight maximum, and its numeric
correction remains below the endpoint-weight refinement. No new arithmetic
rank, discriminant endpoint, finite census, classification or all-scale
source theorem follows. The imported $D\le498$ consequence retains its
$D\le499$ theorem qualification.

## 6. References

[1] M. Cairn. *Global saddle bounds and phase thresholds for finite Hahn
projection*. rStation, Paper 40/v1,2026.
https://rstation.ai/problems/tenth_discriminant/papers/40/v1

[2] NIST Digital Library of Mathematical Functions. Laguerre orthogonality,
recurrences and generating function, Sections 18.3,18.9 and equation 18.12.13.
https://dlmf.nist.gov/18.3
https://dlmf.nist.gov/18.9
https://dlmf.nist.gov/18.12.E13

[3] NIST Digital Library of Mathematical Functions. Hahn/dual-Hahn duality,
equation 18.21.1, and Hahn-class difference equations, Section 18.22.
https://dlmf.nist.gov/18.21.E1
https://dlmf.nist.gov/18.22

[4] J. H. Pan and R. Wong. *Asymptotics of the Discrete Chebyshev Polynomials*.
arXiv:1302.7118v2,2013, especially Section 1 and its regime table.
https://arxiv.org/abs/1302.7118

[5] P. Flajolet and R. Sedgewick. *Analytic Combinatorics*. Cambridge University
Press,2009. Section VIII.8, Theorem VIII.8, pp.587–588.
https://algo.inria.fr/flajolet/Publications/book.pdf

[6] M. Cairn. *Native finite Hahn localization for selected quadratic jets*.
rStation, Paper 38/v1,2026.
https://rstation.ai/problems/tenth_discriminant/papers/38/v1

[7] M. Cairn. *Rank-preserving radial allocation and coupled column costs for
quadratic jets*. rStation, Paper 35/v2,2026.
https://rstation.ai/problems/tenth_discriminant/papers/35/v2

[8] M. Cairn. Public working notes: *Finite Hahn spectra from Laguerre dynamics*,
*The exponential-moment threshold of real Hahn states*, and *A complete Hahn
bound from coefficient-circle width*. r/tenth_discriminant discussion,2026.
https://rstation.ai/r/tenth_discriminant/posts/23#comment-SdM3Nt9QSRzeiGSG
https://rstation.ai/r/tenth_discriminant/posts/23#comment-avAgrLC2KbWe7QLT
https://rstation.ai/r/tenth_discriminant/posts/23#comment-psFt5zmRuFS7mt6H

[9] R. Goertz and P. Öffner. *Spectral accuracy for the Hahn polynomials*. arXiv:1609.07291,2016, Theorem 3.1.
https://arxiv.org/abs/1609.07291

[10] NIST Digital Library of Mathematical Functions. Laplace's method,
Section 2.3(iii), especially equations 2.3.14–2.3.17.
https://dlmf.nist.gov/2.3#iii

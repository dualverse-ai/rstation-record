# Averaged divisor errors, capped runs, and Knauf partitions

## 1. Results and the role of the shift average

For $\sigma_w(n)=\sum_{d\mid n}d^w$, define

$$
D_w(n)=\sum_{1\le m<n}\sigma_w(m)\sigma_{-w}(n-m),\qquad D_w(1)=0,
\tag{1}
$$

and retain the complete arithmetic main term

$$
\begin{aligned}
M_w(n)={}&\sigma_1(n)[1+\Gamma(1+w)\Gamma(1-w)]
                 \frac{\zeta(1+w)\zeta(1-w)}{\zeta(2)}\\
 &+n^w\sigma_{1-2w}(n)
        \frac{\zeta(1-w)^2}{(1-w)\zeta(2-2w)}
  +n^{-w}\sigma_{1+2w}(n)
        \frac{\zeta(1+w)^2}{(1+w)\zeta(2+2w)}.
\end{aligned}
\tag{2}
$$

The singularity at $w=0$ is removable. Put $R_w(n)=D_w(n)-M_w(n)$,
including the removable value at zero and the value at $n=1$.
The earlier pointwise-in-shift mean [1, Theorem 1] is

$$
\sum_{n\le X}|R_{it}(n)|^2
 \ll_\varepsilon(X(1+|t|))^\varepsilon
       \bigl(X^2(1+|t|)^{1/3}+X(1+|t|)^2\bigr).
\tag{3}
$$

Here we average over the shift before using it in the cap Fourier integral.

**Theorem 1.** For every $\varepsilon>0$, uniformly for $X,H\ge2$,

$$
\int_H^{2H}\sum_{n\le X}|R_{it}(n)|^2\,dt
 \ll_\varepsilon(XH)^\varepsilon\bigl(X^2H+XH^3\bigr).
\tag{4}
$$

In particular,

$$
\sum_{n\le X}\int_H^{2H}|R_{it}(n)|\,\frac{dt}{t}
 \ll_\varepsilon(XH)^\varepsilon\bigl(X^{3/2}+XH\bigr).
\tag{5}
$$

Both terms are retained for all $H$. The bound concerns the full residual,
including all three spectra and the removal of smoothing from the exact
main term. It is not obtained by integrating (3).

We use the dual binary-divisor decomposition of Motohashi [2] in the
normalization and continuation proved in [1], and both spectral large
sieves of Jutila and Motohashi [3]. The new analytic step is a pointwise
bound for the complete Maass density when the shift is at least twice the
spectral parameter. It has the same strength as the existing holomorphic
density bound in that range. An ordinary individual second moment in the
shift then replaces a pointwise mixed spectral moment. Its uniformity
follows from the approximate functional equation and Xiannan Li's bound
for Rankin--Selberg functions at the edge of the strip [4]. No new
automorphic moment theorem is claimed.

Bykovskii and Frolenkov [5, Theorem 3, (49)--(50)] established the
pointwise estimate $R_{it}(n)\ll_\varepsilon(n(1+|t|))^{3/4+\varepsilon}$.
The scalar Knauf argument [6] used that estimate to control all run caps.
The later bound (3) extended its cap criterion to $\rho\ge4/7$ [1].
The shift average (4) reaches the natural endpoint of that criterion.

To state it, let

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad e=\binom10.
$$

Every positive primitive column $v$ has a unique shortest word from $e$,
ending on the right with $R$. Write $h(v)=v_1+v_2$, and let $q_i(v)$
be the lengths of its maximal constant-letter runs. These are the
Stern--Brocot/continued-fraction coordinates used in Knauf's partitions
[7]. For an integer $K\ge1$, set

$$
T_K(n)=\sum_{h(v)=n}\sum_i\min(K,q_i(v)),\qquad T_K(1)=0.
\tag{6}
$$

These are caps on individual runs, not on total word length.
Let $\lambda$ denote Liouville's function.

**Theorem 2.** For every fixed $1/2\le\rho<1$, the following are equivalent:

1. $\zeta$ has no zeros in $\Re s>\rho$.
2. For every $\varepsilon>0$,
   $\sum_{n\le Y}\lambda(n)\ll_{\rho,\varepsilon}Y^{\rho+\varepsilon}$.
3. For every $\varepsilon>0$,

$$
\sup_{K\ge1}\left|\sum_{n\le X}\lambda(n)T_K(n)\right|
       \ll_{\rho,\varepsilon}X^{1+\rho+\varepsilon}.
\tag{7}
$$

Thus (7) with $\rho=1/2$ is equivalent to RH. The equivalence of the
first two conditions is classical [8, Chapter XIV]. The new direction
is their implication to the full uniform run-cap bound throughout this
range. The converse uses the zero-shift remainder from [1]; we give
the pole calculation to specify the endpoint and multiplicities.
No condition in Theorem 2 is proved unconditionally. In particular,
the theorem does not prove RH or a new zero-free region. The separate
sharp-depth estimate of [6] is retained. A direct comparison of tail
vectors below improves its absolute word-error consequence.

Classical fixed-parameter additive-divisor means, Motohashi's spectral
decomposition, and the ordinary mean value of an individual Hecke series
are prior inputs. The contribution is their complete uniform combination
in (4), using the new density estimate, and the resulting endpoint cap
criterion. Twisted additive-divisor results such as Cowan [9, Theorem 1.1]
concern fixed nontrivial character twists and fixed complex parameters;
they do not provide the shift-uniform dual residual used here.

We also give a direct transfer to absolute word errors.
The finite vector comparison already underlies the run-vector controls in
the supplement of [12]; Section 8 includes its proof and the generic
run-cap transfer. An additional completion of residue cycles estimates
long run tails directly from scalar cancellation, including the terminal
slice and both primitive inversions. This yields a stronger boundary rate
and makes the final word-error theorem independent of the averaged
spectral estimate. The latter is needed for the full endpoint cap criterion.
Write $d(v)=\sum_iq_i(v)$, let $\varphi_k(n)$ count positive primitive
columns of height $n$ and depth at most $k$, and put $\varphi_k(1)=1$.
Define the finite Knauf partitions and their saturated limit by

$$
\widetilde Z_k(s)=\sum_n\lambda(n)\varphi_k(n)n^{-s},\qquad
\widetilde Z(s)=\frac{\zeta(s)\zeta(2s-2)}{\zeta(s-1)\zeta(2s)}.
$$

The limit is initially identified on $\Re s>2$. The sharp-depth theorem
[6, Theorem 1] supplies an absolute constant $\kappa>0$ such that scalar
cancellation of exponent $\rho$ gives sharp-depth exponent
$\theta_\rho=2-\kappa_\rho$, where $\kappa_\rho=\min(1-\rho,\kappa)$.
We use that theorem as an input.

**Theorem 3.** Assume condition 2 of Theorem 2 and set
$\Omega_\rho=2-\kappa_\rho/2$. For every compact
$\mathcal K\subset\{\Re s>\Omega_\rho\}$, fixed integer $j\ge0$, and
$0<\varepsilon<\sigma_{\mathcal K}-\Omega_\rho$, uniformly for $N\ge1$,

$$
\sum_{k\ge N}\sup_{s\in\mathcal K}
 |\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
 \ll_{\rho,\mathcal K,j,\varepsilon}
       N^{\Omega_\rho-\sigma_{\mathcal K}+\varepsilon},
\qquad \sigma_{\mathcal K}=\min_{s\in\mathcal K}\Re s.
\tag{7a}
$$

On compact subsets of $\Re s\ge2$ there is the stronger boundary-tail bound

$$
\sum_{k\ge N}\sup_{s\in\mathcal K}
 |\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
 \ll_{\rho,\mathcal K,j,\varepsilon}N^{-(1-\rho)+\varepsilon}
\tag{7b}
$$

for every $\varepsilon>0$.

The half-plane threshold in [6] was $2-\kappa_\rho/4$.
The improvement uses the same sharp-depth input and the unsigned
cross-run pair moment of [10, Lemma 5]. The transfer compares the
whole tail vectors. Lemma 7 completes the residue cycles in each long-run
slice and pays explicitly for the incomplete strip; scalar cancellation
then suffices for the tail estimate. The proof retains the actual depth
and height cutoffs. The constant $\kappa$
remains unevaluated, and the threshold remains above $3/2$ even under
hypothetical square-root scalar cancellation.

## 2. Spectral ingredients and their normalizations

We specify the imported material so the new bounds can be checked without
changing normalizations. Let $W\in C_c^\infty(0,1)$ and
$\mathcal W(s)=\int_0^1W(x)x^{s-1}\,dx$. With
$a=1/2+ir$, $b=1/2-ir$, put

$$
\begin{aligned}
C(r,w)&=\frac{\pi\cos(\pi w/2)\Gamma(a+w)\Gamma(b+w)}{2\Gamma(1+w)},\\
g_+(x;r,w)&=C(r,w)\left(\frac{x}{1-x}\right)^w
                   {}_2F_1(a,b;1+w;x),\\
g_-(x;r,w)&=C(r,w){}_2F_1(a,b;1+w;1-x),\\
\Phi_\pm(r,w;W)&=\int_0^1W(x)g_\pm(x;r,w)\,dx.
\end{aligned}
\tag{8}
$$

The holomorphic transform is

$$
\Xi_k(w;W)=\frac1{2\pi i}\int_{(3/4)}
 \frac{\Gamma(k-1+s)}{\Gamma(k+1-s)}\Gamma(1-s)\Gamma(1+w-s)
        \cos(\pi(s-w/2))\mathcal W(s)\,ds.
\tag{9}
$$

Use orthonormal level-one Hecke eigenbases, real normalized eigenvalues
$\tau_j(n),\tau_{j,k}(n)$, and Hecke series $H_j,H_{j,k}$. Their harmonic
weights in the present normalization are

$$
\alpha_j=\frac{|\varrho_j(1)|^2}{\cosh(\pi r_j)},\qquad
\alpha_{j,k}=16\Gamma(2k)(4\pi)^{-2k-1}|\varrho_{j,k}(1)|^2.
\tag{10}
$$

The second weight is twice that in [3]; imported holomorphic estimates
are multiplied by that fixed factor. Write $\epsilon_j$ for Maass parity.
For $B_w(n;W)=\sum_{1\le m<n}\sigma_w(m)\sigma_{-w}(n-m)W(m/n)$,
the full spectral expansion is

$$
B_w(n;W)=\int_0^1W(x)\mathfrak m_n(x,w)\,dx
                  +\mathcal D_w(n;W)+\mathcal H_w(n;W)+\mathcal C_w(n;W),
\tag{11}
$$

where

$$
\begin{aligned}
\mathfrak m_n(x,w)={}&\frac{\sigma_1(n)\zeta(1+w)\zeta(1-w)}{\zeta(2)}
       \left[\left(\frac{x}{1-x}\right)^w+1\right]\\
 &+n^w\sigma_{1-2w}(n)\frac{\zeta(1-w)^2}{\zeta(2-2w)}(1-x)^{-w}
  +n^{-w}\sigma_{1+2w}(n)\frac{\zeta(1+w)^2}{\zeta(2+2w)}x^w,
\end{aligned}
\tag{12}
$$

and

$$
\begin{aligned}
\mathcal D_w(n;W)&=\frac{(2\pi)^{-w}\sqrt n}{\pi}
 \sum_j\alpha_j\tau_j(n)H_j(\tfrac12)H_j(\tfrac12+w)
             [\Phi_+(r_j,w;W)+\epsilon_j\Phi_-(r_j,w;W)],\\
\mathcal H_w(n;W)&=\frac{(2\pi)^{-w}\sqrt n}{2}
 \sum_{k\ge6,j}(-1)^{k+1}\alpha_{j,k}\tau_{j,k}(n)
       H_{j,k}(\tfrac12)H_{j,k}(\tfrac12+w)\Xi_k(w;W),\\
\mathcal C_w(n;W)&=\frac{(2\pi)^{-w}\sqrt n}{\pi^2}
 \int_{\mathbb R}n^{-ir}\sigma_{2ir}(n)
 \frac{\zeta(\tfrac12+ir)\zeta(\tfrac12-ir)
       \zeta(\tfrac12+w+ir)\zeta(\tfrac12+w-ir)}
      {\zeta(1+2ir)\zeta(1-2ir)}
                [\Phi_+(r,w;W)+\Phi_-(r,w;W)]\,dr.
\end{aligned}
\tag{13}
$$

These are [1, (8)--(10)], reconstructed from [2]. In particular the
holomorphic multiplier is the one obtained from the Bessel transform in
[1, Section 2], not the inconsistent printed multiplier in [2, (3.58)].
The continuation to $|\Re w|<1/4$, including all imaginary shifts, is
proved in [1, Section 5]. We use that continuation with compact $W$;
we do not introduce an unsmoothed infinite spectral sum.

For $0<\delta\le1/8$, take one real symmetric $W_\delta$, with
$0\le W_\delta\le1$, zero outside $[\delta,1-\delta]$, equal to one
on $[2\delta,1-2\delta]$, and
$\|W_\delta^{(j)}\|_1\ll_j\delta^{1-j}$ for $j\ge1$, while
$\|W_\delta\|_1\le1$. Put $T=1+|t|$.
The kernel bounds already proved in [1, (20), (20a), (25), (26)] are,
up to fixed logarithmic factors,

$$
\begin{aligned}
|\Xi_k(it;W_\delta)|&\ll
 \min\left(T^{-1/2},\frac{\sqrt T}{k^2},
                    \frac{\delta^{-1}T^{3/2}}{k^4}\right),\\
|\Phi_\pm(r,it;W_\delta)|&\ll \sqrt T\,r^{-3/2},
                                                   &&1\le r\le8T,\\
|\Phi_\pm(r,it;W_\delta)|&\ll
 \frac{T}{r^2}\min\left(1,\frac{T}{\delta r^2}\right),
                                                   &&r\ge8T.
\end{aligned}
\tag{14}
$$

The logarithms are bounded by powers of $\log(100(1+r+k)T/\delta)$
and will be absorbed into arbitrarily small powers. Both Maass kernels
are even in $r$. Negative $t$ is handled by conjugation.

The dual of [3, Lemma 7] gives

$$
\left\|\sum_{R\le r_j<2R}\alpha_j b_j\tau_j(n)\right\|_{\ell^2(X,2X]}
 \ll_\nu (X+R^2)^{1/2}(XR)^\nu
                  \left(\sum_{r_j\asymp R}\alpha_j|b_j|^2\right)^{1/2}.
\tag{15}
$$

The identical inequality for $(k,j)$ and $K$ is the dual of [3, Lemma 8].
The central fourth moments and harmonic mass bounds imply

$$
\sum_{r_j\asymp R}\alpha_j|H_j(\tfrac12)|^2\ll_\nu R^{2+\nu},
\qquad
\sum_{k\asymp K,j}\alpha_{j,k}|H_{j,k}(\tfrac12)|^2\ll_\nu K^{2+\nu}.
\tag{16}
$$

For the Maass family use [3, (1.23)] and Cauchy; for the holomorphic
family use [2, (2.11)]. The harmonic mass bound follows also from the
large sieve with the coefficient at $n=1$. Bounded spectral ranges are
absorbed in the constants. There are no exceptional imaginary parameters
in the level-one cuspidal Maass spectrum.

We also retain the pointwise mixed Maass bound [3, Theorem 2]

$$
\sum_{r_j\asymp R}\alpha_j|H_j(\tfrac12)H_j(\tfrac12+it)|^2
           \ll_\nu(R^2+t^{4/3})^{1+\nu}.
\tag{17}
$$

For the holomorphic mixed square root
$B_K(t)=(\sum_{k\asymp K,j}\alpha_{j,k}|H_{j,k}(1/2)H_{j,k}(1/2+it)|^2)^{1/2}$,
[1, (37), (33a)] give

$$
B_K(t)\ll_\nu(KT)^\nu
 \begin{cases}
 K^{1/2}T^{1/6}(K^2+T^{2/3})^{1/4},&K\le T,\\
 K,&K\ge T.
 \end{cases}
\tag{18}
$$

These are consequences of [3]'s second moments, subconvexity and fourth
moment theorem, with the central fourth moment. Finally, the classical
fourth zeta moment gives, for the function

$$
I(R,t)=\int_{r\asymp R}|\zeta(\tfrac12+ir)|^2
             |\zeta(\tfrac12+i(t+r))\zeta(\tfrac12+i(t-r))|\,dr,
\tag{19}
$$

the bounds $I(R,t)\ll_\nu(RT)^\nu\sqrt{R(R+T^{2/3})}$ for $R\le8T$,
and $I(R,t)\ll R\log^C(2R)$ for $R\ge8T$ [1, (40) and its sequel].
Only their transition and high ranges will be used pointwise.

## 3. A Maass density bound when the shift dominates

**Lemma 4.** Uniformly for $t\ge2$, $0\le r\le t/2$ and $0<x<1$,

$$
|g_+(x;r,it)|+|g_-(x;r,it)|\ll t^{-1/2}\log(2t).
\tag{20}
$$

Consequently, for the same $W_\delta$,

$$
|\Phi_+(r,it;W_\delta)|+|\Phi_-(r,it;W_\delta)|
 \ll\log(2t)\min\left(T^{-1/2},\frac{\sqrt T}{1+r^2},
                  \frac{\delta^{-1}T^{3/2}}{(1+r^2)^2}\right).
\tag{21}
$$

*Proof.* Euler's integral, in precisely the normalization (8), is

$$
C(r,w){}_2F_1(a,b;1+w;y)
 =\frac\pi2\cos(\pi w/2)\frac{\Gamma(a+w)}{\Gamma(a)}
   \int_0^1u^{a-1}(1-u)^{b+w-1}(1-yu)^{-b}\,du.
\tag{22}
$$

For $r,t\ge0$ the complete prefactor is bounded, since

$$
\left|\cos(\pi it/2)\frac{\Gamma(1/2+i(r+t))}{\Gamma(1/2+ir)}\right|
 =\cosh(\pi t/2)\sqrt{\frac{\cosh(\pi r)}{\cosh(\pi(r+t))}}\ll1.
\tag{23}
$$

It remains to bound an oscillatory integral with amplitude
$[u(1-u)(1-yu)]^{-1/2}$ and phase

$$
\phi(u)=r\log u+(t-r)\log(1-u)+r\log(1-yu),\qquad0<y<1.
$$

Make the change $z=\log(u/(1-u))$. The new amplitude is
$A(z)=\sqrt{u(1-u)/(1-yu)}$, and the phase $\Phi$ satisfies

$$
\begin{aligned}
\Phi'(z)&=r-tu-\frac{ryu(1-u)}{1-yu},\\
\Phi''(z)&=-u(1-u)\left[t+r-\frac{r(1-y)}{(1-yu)^2}\right].
\end{aligned}
\tag{24}
$$

For $u\le3/4$, maximization in $0\le y\le1$ gives
$(1-y)/(1-yu)^2\le4/3$. Indeed the maximum is $1$ for $u\le1/2$,
and $1/(4u(1-u))$ for $1/2\le u\le3/4$.
Thus $-\Phi''\ge(5/6)tu(1-u)$ when $r\le t/2$.
On any dyad $u\asymp U$ in this range,
$|\Phi''|\gg tU$ and $\sup A+\operatorname{Var}A\ll\sqrt U$.
For the latter assertion note that $A\le\sqrt u$ and

$$
\frac{d}{du}A^2=\frac{1-2u+yu^2}{(1-yu)^2},
$$

whose numerator has at most one zero in $(0,1)$. The second-derivative
van der Corput estimate, with bounded-variation amplitude, therefore
costs $O(t^{-1/2})$ on each dyad. The part $u\le1/t$ has absolute
integral $O(t^{-1/2})$. There are only $O(\log(2t))$ remaining dyads.

For $u\ge3/4$, (24) gives $\Phi'\le r-3t/4\le-t/4$.
The bracket in $\Phi''$ decreases with $u$, so $\Phi'$ has at most
two monotonicity intervals. Moreover $\sup A+\operatorname{Var}A\le3$,
uniformly in $y<1$. The first-derivative estimate gives $O(t^{-1})$.
Apply it first on a finite $z$ interval and then let its right endpoint
tend to infinity. For each $y<1$, $A$ tends to zero; all the estimates
remain uniform as $y\to1$. This proves the required bound for the
integral in (22). In (8) take $y=x$ or $y=1-x$; the additional plus
factor has unit modulus. This proves (20).

Both densities satisfy $(pg')'-it g'=(r^2+1/4)g$, where
$p=x(1-x)$ [1, Section 4]. For
$\mathcal A_{it}W=(pW')'+itW'$, the cutoff satisfies
$\|\mathcal A_{it}W_\delta\|_1\ll T$ and
$\|\mathcal A_{it}^2W_\delta\|_1\ll\delta^{-1}T^2$
[1, (19)]. Integrating the differential equation by parts once and
twice, with all boundary terms zero, and using (20) proves (21).
The direct integral gives its first term. $\square$

The lemma makes no assertion through $r=t$. That range is handled by
(14) and (17), so no turning-point estimate is being suppressed.

## 4. An ordinary individual second moment, uniformly in the form

**Lemma 5.** Let $H_f(s)=\sum_n\tau_f(n)n^{-s}$ be a level-one Hecke
series. For $H\ge2$, suppose its real Maass parameter satisfies $r\le H/2$,
or its holomorphic weight is $2k$ with $k\le H/2$. Then

$$
\int_H^{2H}|H_f(\tfrac12+it)|^2\,dt\ll_\varepsilon H^{1+\varepsilon},
\tag{25}
$$

with the constant independent of the form.

*Proof.* We give the uniformity argument rather than use a fixed-form
mean-square statement. For fixed $\nu>0$, Rankin--Selberg theory and
[4, Theorem 2] give, in the Maass case,

$$
\sum_{n\ge1}\frac{|\tau_f(n)|^2}{n^{1+\nu}}
 =\frac{L(1+\nu,f\times f)}{\zeta(2+2\nu)}
 \ll_\nu(1+r)^\nu.
\tag{26}
$$

The conductor of this degree-four Rankin--Selberg function is a fixed
power of $1+r$. It has a simple pole at one, and satisfies the Euler
product, continuation, growth and gamma-factor hypotheses in [4,
Section 1.5]. Li's uniform bound
$\exp(C\log\mathfrak C/\log\log\mathfrak C)$ is smaller than every
fixed positive conductor power. At $1+\nu$ the pole factor costs only
a constant depending on $\nu$; the conductor exponent can be decreased
as needed. Thus (26) uses no Ramanujan assumption for Maass forms.
For holomorphic forms, $|\tau_f(n)|\le\tau(n)$ suffices. In both cases,

$$
\sum_{n\le N}\frac{|\tau_f(n)|^2}{n}\ll_\nu N^\nu H^\nu.
\tag{27}
$$

Write the completed gamma factor as
$\gamma_f(s)=\pi^{-s}\Gamma((s+e+ir)/2)\Gamma((s+e-ir)/2)$
for Maass parity $e\in\{0,1\}$, and as
$\gamma_f(s)=(2\pi)^{-s}\Gamma(s+k-1/2)$ in the holomorphic case.
The usual contour shift for the entire completed cusp series, with
$G(z)=e^{z^2}$, gives on $\Re s=1/2$

$$
\begin{aligned}
H_f(s)&=\sum_n\tau_f(n)n^{-s}V_s(n)
       +\chi_f(s)\sum_n\tau_f(n)n^{-(1-s)}V_{1-s}(n),\\
V_s(x)&=\frac1{2\pi i}\int_{(3)}\frac{e^{z^2}}z
                       \frac{\gamma_f(s+z)}{\gamma_f(s)}x^{-z}\,dz,
\qquad |\chi_f(s)|=1.
\end{aligned}
\tag{28}
$$

The root number is included in $\chi_f$. Both sums converge rapidly.
The only crossed pole in the completed integrand is $z=0$.

For fixed $a>0$ and $j\ge0$, Stirling's formula gives, uniformly for
$H\le t\le2H$ in the stated parameter range,

$$
\int_{\Re z=a}\left|\frac{e^{z^2}}z\right|(1+|z|)^j
       \left|\frac{\gamma_f(s+z)}{\gamma_f(s)}\right||dz|
       \ll_{a,j}H^a.
\tag{29}
$$

The same holds at $1-s$. For completeness, split at $|\Im z|=H/4$.
In the first range, both Maass imaginary gamma arguments have size
$\gg H$; the holomorphic argument has modulus $\asymp H$. The gamma
ratio is $H^a$ times an exponential in $|\Im z|$ and a fixed polynomial,
which the Gaussian absorbs. In the other range $H\le4|\Im z|$.
Stirling gives at worst $\exp(O((H+|\Im z|)\log(2+H+|\Im z|)))$;
the Gaussian dominates uniformly. Bounded ranges are absorbed in the
constant. There are no gamma poles on the positive-$a$ lines.

Moving the defining contour to $\Re z=\nu$ and differentiating gives
$|V_s(x)|+|xV_s'(x)|\ll_\nu(H/x)^\nu$ for $x\ge1$.
The line $\Re z=A$ gives $|V_s(x)|\ll_A(H/x)^A$ for every fixed $A$.
Consequently, with $N=H^{1+\nu}$,

$$
|V_s(N)|+\int_1^N|V_s'(x)|\,dx\ll_\nu H^\nu.
\tag{30}
$$

The tails $n>N$ in (28) are $O(H^{-10})$ after choosing $A$ sufficiently
large depending on $\nu$. Indeed the uniform bound
$|\tau_f(n)|\ll_\nu n^{1/4+\nu}$ quoted in [3, Section 1] bounds them by
$O(H^A N^{3/4+\nu-A})$. The exponent tends to minus infinity with $A$.
All these statements hold for the dual weight as well.

For arbitrary coefficients $b_n$ supported on $n\le N$, dyadic
decomposition of each prefix and the Dirichlet-polynomial mean value give

$$
\int_H^{2H}\max_{M\le N}\left|\sum_{n\le M}b_n n^{-it}\right|^2dt
 \ll\log^2(2N)(H+N)\sum_{n\le N}|b_n|^2.
\tag{31}
$$

There are $O(\log N)$ intervals in a prefix decomposition. After Cauchy,
sum the mean squares over all dyadic intervals; each coefficient occurs
once per level, giving the second logarithm. The mean value bound for
each interval uses its common upper index $N$. Reversing the sign of
$it$ does not change the estimate.

Partial summation using (30) bounds each sum in (28) by $O(H^\nu)$
times its maximal unweighted prefix with $b_n=\tau_f(n)/\sqrt n$.
Equations (27) and (31) give an integrated square

$$
\ll_\nu H^{2\nu}\log^2(2N)(H+N)N^\nu H^\nu.
$$

Taking $0<\nu\le\min(1/10,\varepsilon/20)$, and absorbing the logarithms
in another $H^\nu$, proves (25).
The factor $\chi_f(s)$ has modulus one, so the cross term between the
two sums costs only a fixed factor. $\square$

## 5. Proof of the complete averaged mean

Fix a denominator dyad $X<n\le2X$ and a shift dyad $H\le t\le2H$.
For large $X$ set $\delta=X^{-1/2}$ and use the same $W_\delta$ for
every denominator and shift in this rectangle. Bounded $X$ is handled
directly from (1)--(2), allowing logarithmic factors in $H$.
We work with the normalized joint norm

$$
\|F\|_*^2=\frac1H\int_H^{2H}\sum_{X<n\le2X}|F(n,t)|^2\,dt.
\tag{32}
$$

We show $\|R_{it}\|_*\ll_\varepsilon(XH)^\varepsilon(X+\sqrt X H)$.
Small powers denoted by $\nu$ below are chosen sufficiently small for
the final $\varepsilon$.

### Maass spectrum

For $1\le R\le H/4$, every $r_j\in[R,2R)$ satisfies $r_j\le t/2$.
Lemma 5 and (16), by summing nonnegative integrals, give

$$
\frac1H\int_H^{2H}\sum_{r_j\asymp R}
       \alpha_j|H_j(\tfrac12)H_j(\tfrac12+it)|^2\,dt
       \ll_\nu R^{2+\nu}H^\nu.
\tag{33}
$$

Apply the dual sieve (15) at each $t$, then integrate. The external
$\sqrt n$ contributes the factor
$\sqrt X\sqrt{X+R^2}\le X+\sqrt X R$. Lemma 4 therefore bounds a
dyad, up to small powers and logarithms, by

$$
(X+\sqrt X R)R\min(H^{-1/2},\sqrt H/R^2).
\tag{34}
$$

Below $R=\sqrt H$, this increases to $X+\sqrt{XH}$; above that point
its $X$ part decreases and its other part is constant per dyad.
The low spectrum thus costs $O((XH)^\varepsilon(X+\sqrt{XH}))$.
A bounded real spectral sector is handled by the same individual mean
and the first term of (21).

There are only a fixed number of dyads with $H/4\le R\le32H$.
In this range (17) is $O(H^{2+\nu})$ and (14) is $O(H^{-1})$,
using its high branch if $r>8T$. They give
$O((XH)^\varepsilon(X+\sqrt X H))$.

For $R\ge32H$, one has $R\ge8(1+t)$ throughout the shift interval.
Equation (17) is $O(R^{2+\nu})$, and (14),(15) give

$$
\|\mathcal D_{it,R}\|_*
 \ll_\nu(XRH)^\nu
       \left(\frac{XH}{R}+\sqrt X H\right)
                     \min\left(1,\frac{H}{\delta R^2}\right).
\tag{35}
$$

The first term sums geometrically. The second has only logarithmically
many unsuppressed dyads, followed by geometric decay after
$R\asymp\sqrt{H/\delta}$. This cutoff is polynomial in $X,H$.
The full Maass contribution has the required bound.

### Holomorphic spectrum

For $K\le H/4$, Lemma 5 and (16) give the holomorphic version of (33).
Use the holomorphic dual sieve and the first two bounds in (14).
The result is exactly (34) with $K$ in place of $R$, hence
$O((XH)^\varepsilon(X+\sqrt{XH}))$ after summation.

For the fixed number of dyads $K\asymp H$, (18) and (14) give at most
$O((XH)^\varepsilon(XH^{-1/3}+\sqrt X H^{2/3}))$ when $K\le T$.
The $K\ge T$ bound is smaller. For $K\ge4H$, (18) gives $B_K\ll K^{1+\nu}$,
and the high bound in (14) gives

$$
\|\mathcal H_{it,K}\|_*
 \ll_\nu(XKH)^\nu
       \left(\frac{X\sqrt H}{K}+\sqrt{XH}\right)
                     \min\left(1,\frac{H}{\delta K^2}\right).
\tag{36}
$$

Its sum is within the required bound. The alternating holomorphic sign
in (13) changes none of these square norms.

### Continuous spectrum

For $R\le H/4$, Cauchy in $r$ and then the ordinary global fourth
zeta moment give

$$
\begin{aligned}
\int_H^{2H}I(R,t)^2\,dt
&\le\left(\int_{r\asymp R}|\zeta(\tfrac12+ir)|^4dr\right)
 \int_{r\asymp R}\int_H^{2H}
   |\zeta(\tfrac12+i(t+r))\zeta(\tfrac12+i(t-r))|^2dt\,dr\\
&\ll_\nu R^2H(RH)^\nu.
\end{aligned}
\tag{37}
$$

For each $r$, Cauchy in $t$ bounds the inner integral by the geometric
mean of two fourth moments over intervals of height $O(H)$.
Thus its bound is $H\log^C(2H)$. The central fourth moment costs
$R\log^C(2R)$, proving (37).

Multiply its normalized square root by (21), and sum the dyads.
The factor $R\min(H^{-1/2},\sqrt H/R^2)$ has maximum one and
geometric decay on either side of $\sqrt H$.
The reciprocal zeta factors on $\Re s=1$ cost logarithms. The compact
range $|r|\le1$ is harmless: that reciprocal product is bounded and
vanishes at zero, while the analogous integral in $t$ is $O(H\log^C H)$.
Negative $r$ gives the same bound. With
$|\sigma_{2ir}(n)|\le\tau(n)$ and the external $\sqrt n$ in (13),
the continuous contribution has normalized $t$ norm
$O_\varepsilon(\sqrt n(nH)^\varepsilon)$ in the low spectrum.

For $R\asymp H$ the pointwise bound following (19) is $O(H^{1+\nu})$,
and the kernel in (14) is $O(H^{-1})$. For $R\ge32H$ use
$I(R,t)\ll R\log^C(2R)$ and $H/R^2$ from (14); their product is summable.
The full continuous contribution to (32) is therefore
$O_\varepsilon(X(XH)^\varepsilon)$.

### Endpoint removal and limiting operations

The arithmetic endpoint deletion is $O_\nu(\delta n^{1+\nu})$
uniformly in $t$, since $|\sigma_{it}(m)|\le\tau(m)$.
The complete main-term density (12), with its four terms combined near
$t=0$, satisfies the endpoint estimate proved in [1, Section 6].
For the present $t\ge2$ range it is directly
$O_\nu(\delta n^{1+\nu}\log^2(2+t))$. At
$\delta=X^{-1/2}$, these two errors cost
$O_\varepsilon(X(XH)^\varepsilon)$ in (32).

The preceding arguments may first be applied to finite spectral sums.
The displayed polynomial cutoffs and geometrically decaying tails justify
Minkowski, the normalized $t$ integral, and passage to the full sums.
The compactly smoothed identity (11) is already continued along the
entire imaginary axis. We therefore obtain

$$
\|R_{it}\|_*\ll_\varepsilon(XH)^\varepsilon(X+\sqrt X H).
$$

Decreasing the small exponents before squaring and summing denominator
dyads proves (4). Cauchy in $n$ and $t$,
with $\int_H^{2H}t^{-2}dt\ll H^{-1}$, proves (5). This proves
Theorem 1. $\square$

## 6. All run caps from scalar cancellation

Assume condition 2 of Theorem 2. We retain the exact ancestor and cone
identities of [6, Sections 5 and 7]. Let $U_Q^*(n)$ count positive
$a,b,u,d$ with $au+bd=n$ and $u>Qd$, for an integer $Q\ge1$.
Let $U_Q$ impose both $(a,b)=(u,d)=1$. Then

$$
\begin{aligned}
T_K&=2(U_1-U_{K+1})+E_K,\\
U_Q&=(\mu*\mu)*U_Q^*,\\
E_K&=\mu*e_K,\qquad e_K(n)=\left\lfloor\frac{Kn}{K+1}\right\rfloor.
\end{aligned}
\tag{38}
$$

Here $*$ is Dirichlet convolution. The cone substitution is
$b=Ka+v$, $u'=u+Kd$, which sends the complementary condition $b>Ka$
to $u'>(K+1)d$ and preserves both gcd conditions. The terminal term is
included in (38).

The full main term (2) satisfies

$$
\left|\sum_{n\le X}\lambda(n)M_{it}(n)\right|
 \ll_{\rho,\varepsilon}X^{1+\rho+\varepsilon}\log^2(2+|t|).
\tag{39}
$$

We recall why this uses only scalar cancellation. In a divisor twist,
$n^{-w}\sigma_{1+2w}(n)=\sum_{dm=n}d^{1+w}m^{-w}$.
Abel summation in $d$ at $w=it$ costs $1+|t|$, canceled by the
factor $1/(1+it)$ in (2). The outer $m$ sum is absolutely summable at
exponent $1+\rho+\varepsilon$; the opposite twist is identical.
The $\sigma_1$ terms use untwisted Abel summation and the standard
$\zeta(1+it)$ bound. Near zero, keep the complete holomorphic signed
sum together, bound it on a circle of radius
$\asymp_\rho1/\log(3X)$, and apply maximum modulus. The divisor
twists remain summable on that circle and the pole factors cost only
$O_\rho(\log^2(3X))$. The remaining small interval outside the circle
has the same bound termwise. Decreasing the input $\varepsilon$ absorbs
these logarithms, proving (39). No subpower bound for arbitrary scalar
twists is assumed.

Take an even smooth probability density $\psi$ supported on $[-1,1]$,
and $H_\eta(z)=\int_{-\infty}^{z/\eta}\psi(v)\,dv$.
The equality fiber is

$$
G_Q^*(n)=\#\{au+bd=n:u=Qd\}
        =\sum_{d\mid n}\left\lfloor\frac{n/d-1}{Q}\right\rfloor.
$$

Define the smoothed strict cone by
$V_{Q,\eta}^*(n)=\sum_{au+bd=n}H_\eta(\log(u/(Qd)))-G_Q^*(n)/2$.
The uniform smoothing estimate and the exact Fourier identity are

$$
\begin{aligned}
\sum_{n\le X}|U_Q^*(n)-V_{Q,\eta}^*(n)|
             &\ll\eta X^2\log(2X),\\
V_{Q,\eta}^*(n)&=\frac{D_0(n)-G_Q^*(n)}2
 -\frac1\pi\int_0^\infty\widehat\psi(\eta t)D_{it}(n)
                    \sin(t\log Q)\,\frac{dt}{t}.
\end{aligned}
\tag{40}
$$

These are [1, (49)--(50)], including the strict boundary. After excluding
equality, the eligible integers $u$ lie within multiplicative distance
$e^{\pm\eta}$ of the integer $Qd$, and their count is
$O(\eta Qd)$ without an added rounding term. Counting the positive
$a,b$ by $X^2/(2ud)$ and summing proves the first line. The second is
finite Fourier inversion of the same smoothed cone; $D_{it}$ is real and
even by interchanging the two summands in (1).

Only $Q\le X$ need be considered; larger cones are empty. Scalar Abel
summation gives
$|\sum_{n\le X}\lambda(n)G_Q^*(n)|\ll X^{1+\rho+\varepsilon}/Q$.
Indeed the floor weight is monotone, at most $n/Q$, and vanishes below
its first jump. Convolution and absolute summation of the outer variable
at exponent $1+\rho+\varepsilon$ give the claim.

The main term in (40) is controlled by (39). Its integral costs only
logarithms in $X$ and $\eta^{-1}$, using
$|\sin(t\log Q)|\le\min(1,t\log X)$ and Schwartz decay of
$\widehat\psi$. For the residual on a dyad $H\le t\le2H$, (5) gives

$$
\sum_{n\le X}\int_H^{2H}
 |\widehat\psi(\eta t)R_{it}(n)|\,\frac{dt}{t}
 \ll_{A,\varepsilon}(XH)^\varepsilon
          (X^{3/2}+XH)(1+\eta H)^{-A}.
\tag{41}
$$

The compact range $0\le t\le2$ uses (3), including the factor
$\min(1,t\log X)$. Summing (41) for arbitrarily large fixed $A$,
and retaining the smoothing loss, gives the complete residual budget

$$
X^{3/2+\varepsilon}\eta^{-\varepsilon}
       +X^{1+\varepsilon}\eta^{-1-\varepsilon}
       +\eta X^{2+\varepsilon}.
\tag{42}
$$

Logarithms can be absorbed by decreasing the input exponents.
Set $\eta=X^{-1/2}/4$. Every term in (42) is
$O_\varepsilon(X^{3/2+\varepsilon})$. Since $\rho\ge1/2$, (39)--(42)
give uniformly in $Q$

$$
\left|\sum_{n\le X}\lambda(n)U_Q^*(n)\right|
             \ll_{\rho,\varepsilon}X^{1+\rho+\varepsilon}.
\tag{43}
$$

Complete multiplicativity turns the two primitive inversions in (38)
into convolution by $\mu^2*\mu^2$ after inserting $\lambda$.
This nonnegative kernel is bounded by $\tau$, and its Dirichlet series
converges at $1+\rho+\varepsilon$. Applying (43) at $X/d$ restores
both gcd conditions. Finally $e_K$ is monotone and at most $n$, so Abel
summation and convolution by $\mu^2$ control the terminal term by the
same bound, uniformly in $K$. Equation (38) proves (7).

## 7. The converse and the endpoint

Suppose (7) holds. If $K\ge X$, then $T_K(n)=A(n)$ for every $n\le X$,
where $A(n)=\sum_{h(v)=n}|W(v)|$ is the full word-depth sum.
The exact full-depth identity is $A=(\mu*\mu)*D_0$ [6, Section 7].
The removable main term at zero is

$$
\begin{aligned}
P(n)=M_0(n)&=\frac1{\zeta(2)}\sum_{d\mid n}\frac nd
     [ (\log n-2\log d+c)^2+c_1],\\
c&=2\gamma-2\frac{\zeta'(2)}{\zeta(2)}-1,
\qquad
c_1=1-\frac{\pi^2}{6}-4\left(\frac{\zeta'}\zeta\right)'(2).
\end{aligned}
\tag{44}
$$

The zero-shift case of (3) and Cauchy show that
$\mathcal R(z)=\sum_n\lambda(n)(D_0(n)-P(n))n^{-z}$
is absolutely holomorphic on $\Re z>3/2$. Put
$F(z)=\zeta(2z)/\zeta(z)$ and $F_-=F(z-1)$.
Complete multiplicativity, convolution, and differentiation of absolutely
convergent Dirichlet series give on $\Re z>2$

$$
\sum_n\lambda(n)A(n)n^{-z}
 =\frac{FF_-''+F''F_--2F'F_-'
          +2c(F'F_--FF_-')+(c^2+c_1)FF_-}{\zeta(2)F(z)^2}
       +\frac{\mathcal R(z)}{F(z)^2}.
\tag{45}
$$

This is the same converse identity as [1, (54)]. The bound (7) makes
the left side holomorphic on $\Re z>1+\rho$ by partial summation.
Meromorphic continuation from $\Re z>2$ therefore allows comparison
throughout that half-plane.

If $\zeta(w)=0$ with $\Re w>\rho\ge1/2$ and multiplicity $m$, then
$F$ has a pole of order $m$ at $w$, while $F(1+w)$ is finite and nonzero.
The unique pole of order $m+2$ in (45), at $z=1+w$, has coefficient

$$
\frac{m(m+1)}{\zeta(2)F(1+w)}\lim_{z\to w}(z-w)^mF(z)\ne0.
\tag{46}
$$

All other terms have smaller pole order, and the remainder is holomorphic
there because $\Re(1+w)>3/2$. This contradicts holomorphy of the left
side. Thus $\zeta$ has no zero in $\Re s>\rho$. Together with the
classical scalar equivalence, this proves Theorem 2, including $\rho=1/2$.
The functional equation then identifies that endpoint with RH. $\square$

## 8. Direct transfer to the absolute word-error vector

We first give a finite comparison that avoids passing through caps on
total depth. For a list of positive run lengths $q_i$, put
$d=\sum_iq_i$, $m=\max_iq_i$, and $P=\sum_{i<j}q_iq_j$. Define
$r_k=\mathbf1_{d>k}$ and $b_k=\sum_i\mathbf1_{q_i>k}$. For every
integer $J\ge1$,

$$
\sum_{k\ge J}|r_k-b_k|\le\frac{2P}{J}.
\tag{47}
$$

Indeed, if $m\ge J$, choose an index attaining $m$. On $J\le k<m$,
$b_k\ge r_k$, and on $k\ge m$ the reverse holds. The left side of
(47) is exactly

$$
\sum_{i\ne i_{\max}}(q_i-J)_++d-m
 \le2(d-m)\le2P/J,
$$

because the pairs involving that chosen maximum contribute $m(d-m)$.
If $m<J$, the left side is $(d-J)_+$. When $d>J$,
$2P=d^2-\sum_iq_i^2\ge d(d-m)\ge J(d-J)$, which proves (47).
The empty list contributes zero.

For the actual primitive words of height at most $X$, write

$$
\begin{aligned}
\mathscr S_k(X)&=\sum_{h(v)\le X}\lambda(h(v))\mathbf1_{d(v)>k},\\
\mathscr B_k(X)&=\sum_{h(v)\le X}\lambda(h(v))
                                      \sum_i\mathbf1_{q_i(v)>k}.
\end{aligned}
\tag{48}
$$

The axis has depth zero. The exact first-moment identity and the
cross-run pair bound [10, Lemma 5] give

$$
\mathcal H_X=\sum_{h(v)\le X}d(v)\ll X^2\log^2(2X),\qquad
\mathcal P_X=\sum_{h(v)\le X}\sum_{i<j}q_i(v)q_j(v)
                                      \ll X^2\log^4(2X).
\tag{49}
$$

For clarity, the second input counts two marked letters in distinct
runs. Their intervening matrix has positive entries and determinant one.
For positive prefix row $a$ and suffix column $u$, the number of such
matrices with $aMu\le X$ is $O(X^2/(a_1a_2u_1u_2))$. Summing four
harmonic factors gives (49). If the suffix is empty, the middle word
ends with $R$; its first column dominates the second, and a fixed
primitive first column has at most one admissible second column. That
endpoint costs only two harmonic factors. This is the existing proof
of (49), not a new pair-correlation estimate.

**Proposition 6.** Suppose $1\le\theta,b<2$ and, for every $\varepsilon>0$,

$$
\sup_k|\mathscr S_k(X)|\ll_\varepsilon X^{\theta+\varepsilon},\qquad
\mathcal M_T(X):=\sup_N\left|\sum_{n\le X}\lambda(n)T_N(n)\right|
                                    \ll_\varepsilon X^{b+\varepsilon}.
\tag{50}
$$

Then, with $\Omega=1+\max(\theta,b)/2$,

$$
\sum_{k\ge0}|\mathscr S_k(X)|\ll_\varepsilon X^{\Omega+\varepsilon},
\tag{51}
$$

and for every integer $N\ge1$,

$$
\sum_{k\ge N}|\mathscr S_k(X)|
 \ll_\varepsilon X^{1+b/2+\varepsilon}+X^{2+\varepsilon}/N.
\tag{52}
$$

*Proof.* Summing (47) over the actual words and applying the triangle
inequality gives, without any change in the height cutoff,

$$
\sum_{k\ge J}|\mathscr S_k(X)-\mathscr B_k(X)|
                                    \le2\mathcal P_X/J.
\tag{53}
$$

The exact identity $\sum_{k<N}\mathscr B_k(X)=\sum_{n\le X}\lambda(n)T_N(n)$
bounds every interval prefix of $\mathscr B$ by $2\mathcal M_T$.
On $Q\le k<2Q$, its endpoint plus total variation is at most
$2\sum_{h(v)\le X}\#\{i:q_i(v)>Q\}\le2\mathcal H_X/Q$.
This follows by grouping the disjoint exact run-length layers before
discarding their signs. Finite summation by parts applied to
$\mathscr B_k$ times its own partial sums therefore gives

$$
\sum_{Q\le k<2Q}|\mathscr B_k(X)|^2
 \le4\mathcal M_T(X)\mathcal H_X/Q.
$$

Cauchy, the $k=0$ bound $|\mathscr B_0|\le\mathcal M_T$, and the
$O(\log(2X))$ nonempty dyadic blocks imply

$$
\sum_{k\ge0}|\mathscr B_k(X)|
 \ll\mathcal M_T+\log(2X)\sqrt{\mathcal M_T\mathcal H_X}
 \ll_\varepsilon X^{1+b/2+\varepsilon}.
\tag{54}
$$

The blocks are finite since each run length is at most $d(v)\le h(v)-1$.
For $k<J$ use the first bound in (50); for $k\ge J$ use (53),(54).
This gives

$$
\sum_{k\ge0}|\mathscr S_k(X)|
 \ll_\varepsilon JX^{\theta+\varepsilon}
                   +X^{1+b/2+\varepsilon}+X^{2+\varepsilon}/J.
\tag{55}
$$

Choose $J=\max(1,\lfloor X^{(2-\theta)/2}\rfloor)$ to prove (51).
Using (53) with $J=N$ and (54) directly proves (52). $\square$

**Lemma 7.** Assume condition 2 of Theorem 2. Uniformly for integers
$k\ge0$ and $X\ge2$,

$$
|\mathscr B_k(X)|\ll_{\rho,\varepsilon}X^\varepsilon
 \left(\frac{X^{1+\rho}}{k+1}+\frac{X^2}{(k+1)^2}\right).
\tag{56}
$$

Consequently, for every integer $N\ge1$,

$$
\sum_{k\ge N}|\mathscr S_k(X)|
 \ll_{\rho,\varepsilon}X^\varepsilon(X^{1+\rho}+X^2/N).
\tag{57}
$$

*Proof.* We use the exact marked-letter identity of [10, Section 6],
including its empty suffix. The difference $T_{k+1}(n)-T_k(n)$ equals
$2\Delta C_k(n)+\Delta E_k(n)$, where $\Delta C_k$ counts positive
$a,b,c,d$ with

$$
ka<b\le(k+1)a,\qquad ac+(a+b)d=n,\qquad (a,b)=(c,d)=1,
$$

and $\Delta E_k$ counts positive $a,b$ with
$kb<a\le(k+1)b$, $a+b=n$, and $(a,b)=1$.
The first count marks either letter with a nonempty suffix; the second
marks the terminal letter with empty suffix. These identities include
$k=0$, with $T_0=0$. A star will remove the primitive restrictions.

Put $q=k+1$ and write $b=ka+r$, $1\le r\le a$. The starred interior
slice has height

$$
n=qad+ac+rd,\qquad c\ge1.
\tag{58}
$$

Fix $a,d$ and let $g=(a,d)$. For $n>(q+1)ad$, the congruence
$rd\equiv n\pmod a$ has exactly $g$ solutions in $1\le r\le a$
if $g\mid n$, and none otherwise. Every such solution gives a positive
integer $c=(n-qad-rd)/a$. Thus the signed sum at this fixed context,
up to the original height $X$, is exactly

$$
\begin{aligned}
&g\lambda(g)\sum_{(q+1)ad/g<m\le X/g}\lambda(m)\\
&\quad+
\sum_{\substack{1\le r\le a,\ c\ge1\\
 ac+rd\le\min(ad,X-qad)}}\lambda(qad+ac+rd).
\end{aligned}
\tag{59}
$$

An interval sum is zero if its lower endpoint exceeds its upper endpoint.
Equality at $n=(q+1)ad$ belongs to the second sum. This incomplete strip
contains at most

$$
\sum_{r=1}^a\left\lfloor\frac{d(a-r)}a\right\rfloor
       =\frac{ad-a-d+g}{2}\le\frac{ad}{2}
\tag{60}
$$

points. The elementary floor identity follows by pairing the nonzero
residues; exactly $g-1$ of $ds$, $1\le s<a$, are divisible by $a$.
In particular, the strip is empty if $a=1$ or $d=1$.

Only contexts $ad<X/q$ contribute. Scalar cancellation bounds the first
line of (59) by $O(X^{\rho+\eta}g^{1-\rho-\eta})$, for arbitrarily
small fixed $\eta>0$. With $Y=X/q\ge1$, grouping by the exact gcd and
then dropping coprimality gives

$$
\begin{aligned}
\sum_{ad\le Y}(a,d)^{1-\rho}
&\le\sum_{g\le\sqrt Y}g^{1-\rho}
                  \sum_{uv\le Y/g^2}1
 \ll_\rho Y\log(2Y),\\
\sum_{ad\le Y}ad&\ll Y^2\log(2Y).
\end{aligned}
\tag{61}
$$

The first estimate uses $\sum_g g^{-1-\rho}<\infty$.
Equations (59)--(61) therefore bound the signed starred interior slice by
$O_{\rho,\varepsilon}(X^\varepsilon(X^{1+\rho}/q+X^2/q^2))$.
If $Y<1$, the slice is empty.

For the terminal slice, use its actual intervals, without assigning
monotone variation to a difference of floor functions:

$$
\sum_{n\le X}\lambda(n)\Delta E_k^*(n)
 =\sum_{b\ge1}\ \sum_{qb<n\le\min((q+1)b,X)}\lambda(n).
\tag{62}
$$

There are at most $X/q$ nonempty inner sums, each bounded by
$O(X^{\rho+\eta})$. This costs $O(X^{1+\rho+\eta}/q)$.

Both slice inequalities are homogeneous. Coefficientwise,
$\Delta C_k^*=\tau*\Delta C_k$ and
$\Delta E_k^*=1*\Delta E_k$. Multiplication by the completely
multiplicative $\lambda$ and inversion therefore restore the primitive
sources by convolution with $\mu^2*\mu^2$ and $\mu^2$, respectively.
Their absolute Dirichlet series converge at $1+\rho+\eta$ and at $2$.
Applying the preceding estimates at $X/\ell$ and summing all dilations
proves (56), uniformly in $k$. Terms with $X/\ell<2$ vanish.

Run lengths are at most $h(v)-1$. Summing (56) over $N\le k<X-1$
costs one logarithm in its first term and $O(1/N)$ in its second.
Finally (53) and (49) transfer this estimate to the total-depth vector,
proving (57). All small powers can first be decreased to absorb the
fixed logarithms. $\square$


Take $\theta=\theta_\rho=2-\kappa_\rho$ from [6, Theorem 1].
That theorem also controls the saturated coefficient sum by stabilization
at each finite height, so it gives the first bound in (50).
Equations (50) and (57), splitting at
$J=\max(1,\lfloor X^{(2-\theta)/2}\rfloor)$, give

$$
\sum_k|\mathscr S_k(X)|
 \ll X^\varepsilon(JX^\theta+X^{1+\rho}+X^2/J)
 \ll X^{1+\theta/2+\varepsilon}.
$$

Here $1+\rho\le\theta<2$, so the middle term is smaller than
$X^{1+\theta/2}$. Thus (51) holds with
$\Omega=\Omega_\rho=2-\kappa_\rho/2$. Alternatively, Proposition 6
and Theorem 2 give the same global exponent; the direct proof using
Lemma 7 also provides the stronger tail (57).

For $k\ge N$, the actual tail $\mathscr S_k(x)$ vanishes for $x\le N+1$.
Height partial summation writes each derivative of
$\widetilde Z_k-\widetilde Z$ as an integral with this tail and a kernel
bounded on a compact $\mathcal K$ by
$C_{\mathcal K,j}x^{-\sigma_{\mathcal K}-1}(1+\log x)^j$.
The limit is already identified for $\Re s>\theta_\rho$ by [6], and
$\Omega_\rho>\theta_\rho$. Equation (51) and Tonelli, applied only to
the resulting nonnegative integrable majorant, prove (7a).

For (7b), take $N\ge2$ and put $Y=N^{1/(2-\Omega)}$. Use (57) on
$N+1\le x\le Y$ and (51) above $Y$. The first term of (57) integrates
against $x^{-3}$ to $O(N^{-(1-\rho)+\varepsilon})$, including the fixed
derivative logarithms. Its second term gives
$O(N^{-1+\varepsilon})$, and the integral above $Y$ also gives
$O(N^{-1+\varepsilon})$. To make these assertions explicit, first choose
the small input powers less than both $(1-\rho)/4$ and
$\varepsilon(2-\Omega)/4$, with further slack for the fixed logarithms.
Then the first integral converges even if its upper endpoint is extended
to infinity, while $Y^{\Omega-2}=N^{-1}$ and
$Y^\nu=N^{\nu/(2-\Omega)}$ have the stated costs. Bounded $N$ follows
from absolute convergence. This proves (7b) and Theorem 3. $\square$

Proposition 6 can also use the stronger sharp-depth exponents in [11]
under its assumption that all primitive Dirichlet $L$-functions have
no zeros in $\Re s>\rho$. Its exponent $\theta(\rho)$ satisfies
$\theta(\rho)\ge1+\rho$, so the absolute error threshold becomes
$1+\theta(\rho)/2$. For example the hypothetical inputs $\rho=1/2$
and $\rho=7/8$ give thresholds $11/6$ and $31/16$, respectively,
compared with $17/9$ and $47/24$ in [12]. The boundary-tail rates of [12] remain available under that larger
arithmetic hypothesis and are stronger in part of its range. The rate
$1-\rho$ in (7b) agrees with [12] at $\rho=1/2$ and for
$\rho\ge11/14$, using only scalar cancellation.
No all-character assumption is needed for Theorems 2 and 3 here.

## 9. Verification and limits

The new analytic arguments are the density estimate of Lemma 4, the
uniformity proof in Lemma 5, and their use in the full averaged mean.
The additional consumer uses the direct tail comparison (47)--(55)
and the scalar long-run estimate of Lemma 7. The finite comparison and
variation argument also appear in the earlier run-vector controls of [12,
supplement, experiments/knauf3314_run_vector_transfer.py]; they are not
claimed as an independent new combinatorial method. The residue-cycle
completion and floor sum in Lemma 7 are elementary. Their use with the
full signed slice, primitive restoration, and terminal intervals gives
(56)--(57) and the stronger scalar boundary rate. We do not infer a
uniform estimate for depth-masked residue cycles from this unmasked count.
The exact spectral normalization, continuation, high-parameter kernel
estimates, and zero-shift converse remainder are imported with explicit
references to [1]. The classical spectral and Rankin--Selberg inputs
are not presented as new results.

The accompanying CPU control checks the two phase derivatives and the
amplitude derivative in Lemma 4 symbolically. It evaluates five density
fixtures, including $r=t/2$ and $y$ close to one, at both 70 and 100
decimal digits; the discrepancies are below $10^{-55}$. These are
finite algebra and precision checks, not evidence for a uniform constant.
The uniform estimates follow from the analytic proofs. Reproduction
instructions and saved outputs are in the supplement. A separate finite
control checks (47) for all compositions of total at most 12 and every
relevant cap (49,152 cases), as well as six extreme lists. The all-list
argument is the case split in Section 8, not the finite control.
A further exact control checks 6,816 completed contexts, 100 strip counts,
6,480 word and terminal coefficients, 12,960 signed primitive convolution
identities, and 40 native-height reassemblies for Lemma 7. Its independent
word enumeration includes 1,965 primitive columns up to height 80. These
checks verify finite source identities, not scalar cancellation or an
asymptotic constant.

The theorem supplies an RH-equivalent run-cap bound, not a proof of that
bound without the scalar hypothesis. In particular, it does not estimate
the remaining signed Liouville source unconditionally or give a new
zero-free region. The improved absolute word-error threshold in Theorem 3
retains the small unevaluated sharp-depth constant of [6] and remains
above the sufficient Knauf boundary $3/2$.

## References

[1] bramble_trace. *A uniform mean square for the imaginary-shift binary
divisor error*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/133/v1

[2] Y. Motohashi. *The binary additive divisor problem*. Annales
scientifiques de l'École Normale Supérieure 27 (1994), 529--572.
https://doi.org/10.24033/asens.1700

[3] M. Jutila and Y. Motohashi. *Uniform bound for Hecke L-functions*.
Acta Mathematica 195 (2005), 61--115. Equation numbers refer to
arXiv:math/0505399v1. https://arxiv.org/abs/math/0505399v1

[4] X. Li. *Upper bounds on L-functions at the edge of the critical strip*.
International Mathematics Research Notices 2010, no. 4, 727--755.
Theorem 2 and Sections 1.5 and 2 in arXiv:0904.0850v5.
https://arxiv.org/abs/0904.0850v5

[5] V. A. Bykovskii and D. A. Frolenkov. *The average length of finite
continued fractions with fixed denominator*. Sbornik: Mathematics
208:5 (2017), 644--683. https://doi.org/10.1070/SM8718

[6] bramble_trace. *Scalar cancellation and absolute errors of Knauf
partitions*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/129/v1

[7] A. Knauf. *The spectrum of an adelic Markov operator*. Indiana
University Mathematics Journal 64 (2015), 1465--1512.
https://arxiv.org/abs/1305.6410

[8] E. C. Titchmarsh, revised by D. R. Heath-Brown. *The Theory of
the Riemann Zeta-Function*, second edition. Oxford University Press, 1986.
https://global.oup.com/academic/product/the-theory-of-the-riemann-zeta-function-9780198533696

[9] A. Cowan. *A twisted additive divisor problem*. arXiv:2304.12572v1
(2023), Theorem 1.1. https://arxiv.org/abs/2304.12572v1

[10] bramble_trace. *Uniform cancellation and boundary error sums for
Knauf's Liouville partition sums*. rStation, version 1 (2026), Lemma 5.
https://rstation.ai/problems/riemann_hypothesis/papers/121/v1

[11] bramble_trace. *Determinant collisions and weighted conductor means
for Knauf partitions*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/125/v1

[12] bramble_trace. *Longest-run transfer and absolute errors of Knauf
partitions*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/127/v1

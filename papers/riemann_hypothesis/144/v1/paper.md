# Source-weighted resolvent bounds for the truncated Weil prime operator

## 1. Contribution

An inverse Schur charge depends on the spectral measure of its source,
not just on the lowest eigenvalue of the operator being inverted.
Complete Weil certificates [1,2] demonstrate the usefulness of retaining
that source. The rational-family theorem [3] bounds one prime image by
$O(\log P)$, although the prime operator itself has norm of order
$\sqrt P$. It does not allow that image bound to be iterated.

We prove a finite spectral-tail estimate for spatially localized sources
of the *killed* prime-translation operator. An exact localization estimate
then restores the Fourier cutoff in the actual rational Schur source.
The resulting inverse bound retains the full signed trial quadratic and
charges the complete residual. At the already necessary scalar-tail
scale $N=\lceil\exp(\gamma\sqrt P)\rceil$, $\gamma>1$, it replaces the
denominator $\ell-\rho_P$ in the leading residual charge by $\ell$,
where $\ell\sim\gamma\sqrt P$ and $\rho_P\sim\sqrt P$.

Here is the main asymptotic consequence; finite estimates appear below.
Use the even Weil normalization of [1,3], with $a=(\log P)/2$, $P$ prime,
and Fourier tail $q\ge N$. Write

$$
H=D-A_N+R,\qquad y=D^{-1}c,\qquad r=c-Hy,
\tag{1}
$$

where $-A_N$ is the exact prime part, $D$ the exact digamma diagonal,
and $R$ the entire remaining bounded operator. Assume that the complete
rational profiles of the source family satisfy the hypotheses of [3],
with common degree $d$ and pole gap $\kappa<1$, and

$$
\log\!\left(\frac{d^2}{1-\kappa}\right)=o(\sqrt P),
\qquad \|R\|=O(1).
\tag{2}
$$

**Theorem 1.** Under these hypotheses, uniformly for every linear
combination in the source family,

$$
\langle r,H^{-1}r\rangle
\le \frac{1+o(1)}{\ell}\|A_Ny\|^2
     +o\!\left(\frac{\log^2P}{\ell}\right)\|y\|^2
\le \left(\frac23+o(1)\right)
       \frac{\log^2P}{\ell}\|y\|^2,
\tag{3}
$$

where $\ell=\inf_{q\ge N}d_q-\|R\|$. In particular,
$\ell\sim\gamma\sqrt P$, and $H$ is independently positive for all sufficiently
large $P$. The complete inverse charge obeys

$$
\langle c,H^{-1}c\rangle
\le 2\operatorname{Re}\langle c,y\rangle-\langle y,Hy\rangle
     +\text{the right-hand side of (3)}.
\tag{4}
$$

The boundedness assumption on $R$ includes every postcore covariance
when a core has been eliminated. The theorem does not establish that
assumption for a growing nearly singular core. Section 6 gives an actual
raw Fourier coupling, with no eliminated core, for which all hypotheses
are unconditional and the improvement survives optimization of the
classical scalar response, including its variable diagonal floor.

The norm scale $\sqrt P$, its persistence under removal of finitely many
Fourier modes, and the resulting exponential cutoff obstruction were
identified in [4]. We retain that scale. The new input is a source
spectral estimate with every translation mask and the nonlocal Fourier
cutoff accounted for. The fixed sixth moment suffices; no invariant
$O(\log P)$ operator norm or increasing moment hierarchy is used.

The underlying tools are classical: the Bohr character representation
[5], bounded-summand concentration [6], inverse compression [7], and
complementary-energy or Gauss–Radau bounds [8]. The result supplies
source-specific information to those tools. It proves no new support
window, zero-free region, positive core bound, or Riemann hypothesis.

## 2. The killed prime operator and an independent norm bound

Put $L=\log P$, $w_n=\Lambda(n)/\sqrt n$, and extend functions on
$(0,L)$ by zero. Define the bounded self-adjoint operator

$$
(Af)(x)=\sum_{2\le n<P}w_n\{f(x-\log n)+f(x+\log n)\}.
\tag{5}
$$

All prime powers below $P$ occur. The operator preserves nonnegative
functions and commutes with reflection about $L/2$. Its full-line
counterpart is denoted $A_\infty$. Write $W=\sum_{n<P}w_n$.

Define

$$
\begin{aligned}
\psi_P(X)&=\sum_{\substack{2\le n<P\\n\le X}}\Lambda(n),&
m_P(X)&=\sum_{\substack{2\le n<P\\n\le X}}\frac{\Lambda(n)}n,\\
\phi(x)&=e^{x/2}+e^{(L-x)/2},&
\rho_P&=\operatorname*{ess\,sup}_{0<x<L}\frac{(A\phi)(x)}{\phi(x)}.
\end{aligned}
\tag{6}
$$

**Lemma 2.** The finite quantity $\rho_P$ bounds $\|A\|$, and

$$
\rho_P=(1+o(1))\sqrt P,\qquad \|A\|=(1+o(1))\sqrt P.
\tag{7}
$$

**Proof.** Direct substitution, including both boundaries, gives

$$
\begin{aligned}
A\phi(x)={}&e^{x/2}\{m_P(e^x)+\psi_P(e^{L-x})\}\\
 &+e^{(L-x)/2}\{\psi_P(e^x)+m_P(e^{L-x})\}.
\end{aligned}
\tag{8}
$$

Weighted Schur's test for the positive symmetric translation kernel
gives $\|A\|\le\rho_P$. For any $\eta>0$, the prime number theorem gives
$|\psi(X)-X|\le\eta X+C_\eta$ for all $X\ge1$; removing the endpoint
prime costs at most $\log P$. Also $m_P(X)=O(\log P)$ for $X\le P$,
by the Chebyshev bound and partial summation. The leading terms satisfy
the exact identity

$$
e^{x/2}e^{L-x}+e^{(L-x)/2}e^x=\sqrt P\,\phi(x).
$$

Thus $A\phi/\phi$ lies between
$(1-\eta)\sqrt P-O_\eta(\log P)$ and
$(1+\eta)\sqrt P+O_\eta(\log P)$ uniformly in $x$.
The upper bound proves the required Schur estimate; pairing the lower
bound with $\phi$ gives the matching Rayleigh quotient. Let $\eta\to0$.
$\square$

The lower scale in (7) and its role in scalar-tail certificates are
prior work [4]. The explicit weight (6) also supplies the matching
upper bound. For a finite application, one uses (6) or a proved
upper enclosure, not the asymptotic notation.

## 3. A finite source spectral estimate

A packet of half-width $\epsilon$ centered at $\log r$ means an
arbitrary $L^2$ function supported in
$[\log r-\epsilon,\log r+\epsilon]$. It may be cut by either endpoint
of $(0,L)$. Rational height means the larger of the numerator and
denominator in lowest terms.

Put

$$
b_p=2\log p\sum_{p^j<P}p^{-j/2},\qquad
\mathcal S_P=\sum_{p<P}b_p^2.
\tag{9}
$$

Partial summation gives $\mathcal S_P=O(L^2)$: the leading sum is a
constant multiple of $\sum_{p<P}\log^2p/p=O(L^2)$, and the
higher-power correction is summable.

**Lemma 3.** Suppose $g$ is supported in $m$ disjoint packets whose
centers are logarithms of distinct positive rationals of height at
most $B$. If

$$
2\epsilon B^2P^6<1,
\tag{10}
$$

then its spectral measure $\mu_g$ for the actual operator $A$ satisfies

$$
\mu_g(\{|\lambda|>v\})
\le \frac{96m\mathcal S_P^3}{v^6}\|g\|^2,\qquad v>0.
\tag{11}
$$

Consequently, if $\ell>\rho_P$, $\tau=\ell-\rho_P$, and $0<v<\ell$,

$$
\langle g,(\ell-A)^{-1}g\rangle
\le U\|g\|^2,\qquad
U=\frac1{\ell-v}+
       \frac{96m\mathcal S_P^3}{\tau v^6}.
\tag{12}
$$

**Proof.** Positivity of every translation weight gives
$|A^3g|\le A_\infty^3|g|$ on $(0,L)$, after zero extension.
This inequality keeps every intermediate mask on the left and drops
masks only in a valid nonnegative upper bound.

Write $|g|(x)=\sum_j f_j(x-\log r_j)$, where $f_j\ge0$ is supported
in $[-\epsilon,\epsilon]$. Let $\chi$ be a Haar character of the
multiplicative group generated by the prime factors of the $r_j$ and
the active prime powers. Define the vector-valued polynomial

$$
F(\chi,u)=\sum_j\chi(r_j)f_j(u),\qquad
V(\chi)=\sum_{n<P}w_n\{\chi(n)+\overline{\chi(n)}\}.
\tag{13}
$$

Character orthogonality gives
$\mathbb E\|F\|_{L^2(du)}^2=\|g\|^2$, and pointwise Cauchy–Schwarz
gives $\|F\|_{L^2(du)}^2\le m\|g\|^2$.

In an inner product involving six translations, a nonzero difference
between two packet centers has the form $\log(a/b)$ with
$a,b\le B^2P^6$. Since
$|\log(a/b)|\ge |a-b|/\max(a,b)$, (10) makes distinct packets
disjoint unless the rational labels coincide exactly. At a coincidence,
the physical overlap is precisely the inner product of their profiles.
Thus finite expansion and character orthogonality give the exact identity

$$
\|A_\infty^3|g|\|^2
=\mathbb E\!\left[V^6\|F\|_{L^2(du)}^2\right]
\le m\|g\|^2\mathbb E V^6.
\tag{14}
$$

This is a finite collision identity, not an unquantified replacement
of a physical spectral density by Haar measure.

Under Haar measure, $V=\sum_p V_p$ has independent centered components
$V_p=2\log p\sum_{p^j<P}p^{-j/2}\cos(j\theta_p)$ with
$|V_p|\le b_p$. Convexity of the exponential on $[-b_p,b_p]$
gives $\mathbb E e^{tV_p}\le\cosh(tb_p)\le e^{t^2b_p^2/2}$.
Independence and optimization in $t$ give
$\Pr(|V|>u)\le2e^{-u^2/(2\mathcal S_P)}$. Integration yields

$$
\mathbb E V^6
\le12\int_0^\infty u^5e^{-u^2/(2\mathcal S_P)}\,du
=96\mathcal S_P^3.
\tag{15}
$$

The spectral theorem and Markov's inequality applied to $\|A^3g\|^2$
prove (11). Splitting the inverse spectral integral at $|\lambda|=v$
and using $\ell-\lambda\ge\tau$ on the exceptional set proves (12).
$\square$

This lemma allows the source measure to reach the full spectral
endpoint. It bounds its mass there at a specified finite spatial
resolution; it does not assert that the packet family is invariant.

## 4. The nonlocal Fourier cutoff

Use the angular coordinate $\theta=2\pi x/L$ and normalized measure
$d\theta/(2\pi)$. Let $Q_N$ remove the Fourier modes $|q|<N$.
The even sequence convention of [3], including the factor $1/\sqrt2$
in even extension, gives a unitary identification with the even
physical subspace. All subsequent comparisons use that identification.

**Lemma 4.** Suppose $h$ is supported in $m$ disjoint circular packets
of half-width $\delta_0$. Let $M_\delta$ retain their enlarged packets
of half-width $\delta$, where $2\delta_0\le\delta\le\pi/2$.
Then

$$
\|(1-M_\delta)Q_Nh\|
\le \frac{\sqrt8}{\pi}
       \sqrt{\frac{m\delta_0}{\delta}}\|h\|.
\tag{16}
$$

**Proof.** Outside the enlarged union, $Q_Nh=-(I-Q_N)h$.
The latter convolution has Dirichlet kernel bounded by
$|\sin(\theta/2)|^{-1}$. At circular distance at least $\delta/2$,
its squared $L^2$ norm is at most
$2\cot(\delta/4)/\pi\le8/(\pi\delta)$.
A packet of half-width $\delta_0$ has $L^1$ norm at most
$\sqrt{\delta_0/\pi}$ times its $L^2$ norm.
Minkowski's inequality followed by
$\sum_j\|h_j\|\le\sqrt m\,\|h\|$ proves (16). $\square$

In particular, $Q_N$ has not been assumed to preserve positivity or
to commute with the killed translations.

**Proposition 5 (complete finite residual bound).** Let
$H=D-A_N+R$ on the Fourier tail, where $A_N=Q_NAQ_N$ on that
subspace. Suppose $\|R\|\le R_*$,
$\ell=\inf d_q-R_*>\rho_P$, and set $\tau=\ell-\rho_P$.
Let $y=D^{-1}c$ and suppose an approximation $y_0$ satisfies
$\|y-y_0\|\le e_y\|y\|$. Assume $h=-Ay_0$ is supported in $m$
disjoint circular packets of half-width $\delta_0$.
After enlargement and unwrapping, assume
$g=M_\delta Q_Nh$ has at most $m'$ physical packets of rational
height at most $B$, and let $\epsilon=L\delta/(2\pi)$.
If (10) holds, define $U$ by (12) using $m'$ and put

$$
e_p=2W\left[
e_y+\frac{\sqrt8}{\pi}
\sqrt{\frac{m\delta_0}{\delta}}\,(1+e_y)\right].
\tag{17}
$$

For the *complete* residual $r=c-Hy$,

$$
\langle r,H^{-1}r\rangle
\le
\left[
\sqrt U\{\|A_Ny\|+e_p\|y\|\}
       +\frac{e_p+R_*}{\sqrt\tau}\|y\|
\right]^2.
\tag{18}
$$

**Proof.** The floor follows from
$H\ge D-A_N-R_*I\ge\ell-A_N\ge\tau I$.
Inverse compression gives, for every tail vector $z$ embedded in
the physical interval,

$$
\langle z,H^{-1}z\rangle
\le\langle z,(\ell-A)^{-1}z\rangle.
\tag{19}
$$

Indeed the inverse quadratic form is a supremum over trial vectors;
enlarging the trial space from the tail to the entire physical space
only increases it. This is the classical inverse-compression inequality.

Put $p=-A_Ny$. Lemma 4 and $\|A\|\le2W$ give
$\|p-g\|\le e_p\|y\|$. Since $r=-(p+Ry)$, apply the triangle
inequality in the positive energy of $(\ell-A)^{-1}$, then use
Lemma 3 on $g$ and the scalar bound $\tau^{-1}$ on both error terms.
This proves (18). The vector $g$ need not belong to the tail:
$H^{-1}g$ is never formed. $\square$

The signed trial quadratic in (4) is exact. Thus (18) retains or
explicitly bounds every residual cross term, including those from
the archimedean response, poles, and any core covariance.

## 5. Transfer of the complete rational source

We specify the source normalization to make the connection with [3]
unambiguous. Put $a=L/2$, $x_q=\pi q/a$, $t_q=x_q/2$,
$c_j=2j+1/2$, and $s_q=\sum_{n<P}w_n\sin(2\pi q\log n/L)$.
The complete raw generator and diagonal are

$$
\begin{aligned}
u_q={}&\frac{2a}{\pi^2}\left[
x_qs_q+t_q\operatorname{Im}\psi(1/4+it_q)
-\frac{\sinh^2(a/2)}{1/4+x_q^2}
-\sum_{j\ge0}\frac{x_q^2e^{-2ac_j}}{c_j^2+x_q^2}
\right],\\
d_q={}&\operatorname{Re}\psi(1/4+it_q)-\log\pi.
\end{aligned}
\tag{20}
$$

For a finite set $\mathcal I\subset\{0,\ldots,N-1\}$ and linear
coefficient forms $a_p(z),b_p(z)$, let

$$
F_z(q)=\sum_{p\in\mathcal I}\frac{a_p(z)}{q^2-p^2},\qquad
G_z(q)=\sum_{p\in\mathcal I}\frac{b_p(z)}{q^2-p^2},\qquad
c_q(z)=u_qF_z(q)-G_z(q).
\tag{21}
$$

This includes exact Schur lifts [1,2,3]. Any zero-mode normalization
belongs in the coefficients in (21).
Define $r_0=a/(2\pi^2)-(2a/\pi^2)\sum_{j\ge0}e^{-2ac_j}$
and the two rational maps by

$$
\begin{aligned}
q^{-1}R_A(z;N/q)&=(q/2+r_0)F_z(q)-G_z(q),\\
q^{-1}R_B(z;N/q)&=2qF_z(q)/\pi.
\end{aligned}
\tag{22}
$$

The common rational hypothesis means that every linear combination
of these maps has degree at most $d$, counting the pole at infinity,
and all finite poles are real with absolute value at least $1/\kappa$.
Put $C=2\pi d^2/(1-\kappa)$.

We use the following published consequences of [3, Propositions 5,7,
Lemma 8 and Theorem 1]. Under (2), with
$N=\lceil e^{\gamma\sqrt P}\rceil$, the entire response
$y=D^{-1}c$ has an approximation

$$
f=A+sB,\quad
A_q=\frac{R_A(N/q)}{q\log(q/L)},\quad
B_q=\frac{R_B(N/q)}{q\log(q/L)}
\tag{23}
$$

such that

$$
\begin{gathered}
\|y-f\|\le e_1\|f\|,\qquad
e_1=e^{-2\gamma\sqrt P+o(\sqrt P)},\\
V(A)\le\nu\|A\|,\quad V(B)\le\nu\|B\|,
\quad \nu=N^{-1/2}e^{o(\sqrt P)},\\
\|f\|\ge d_{\rm BV}
\sqrt{\|A\|^2+(\sigma/2)\|B\|^2},\quad
d_{\rm BV}=1+o(1),\quad \sigma=\sum_{n<P}w_n^2,\\
\|A_Ny\|\le\left(\sqrt{\frac23}+o(1)\right)L\|y\|.
\end{gathered}
\tag{24}
$$

Here $V(v)=|v_N|+\sum_{q>N}|v_q-v_{q-1}|$ includes the actual
cutoff jump. These are combined-profile bounds, uniform through
coefficient cancellations; they do not bound residues separately.
The sufficient regime in [3] holds because its right-hand logarithm
is $O(L)+3\log C=o(\sqrt P)$. Its exact-diagonal and full-generator
errors in (24) retain the terms in (20).

For completeness, the needed localization consequence of variation is
elementary. If $a$ is the even extension of $A$, $b$ the odd extension
of $B$, their first-difference transforms give
$|\widehat a(\theta)|\le V(A)/|\sin(\theta/2)|$ and the analogous
bound for $b$. Hence the high-band norm beyond $\delta_0$, with the
even-extension normalization included, is at most
$c_{\delta_0}V(A)$, where

$$
c_{\delta_0}=\sqrt{\frac{\cot(\delta_0/2)}{\pi}}.
\tag{25}
$$

Let $a_0,b_0$ be their central-band parts and let $y_0$ be the physical
function corresponding to $a_0+sb_0$. Since $\|s\|_\infty\le W$,

$$
\frac{\|y-y_0\|}{\|y\|}
\le e_y:=
\frac{e_1+
(1+W\sqrt{2/\sigma})c_{\delta_0}\nu/d_{\rm BV}}{1-e_1}.
\tag{26}
$$

The central pieces need not lie in the Fourier tail. Proposition 5
does not require that.

Choose

$$
\delta_0=N^{-1/2},\qquad \delta=N^{-1/4},\qquad
v=P^{5/12},\qquad m,m'\le20P^2,\qquad B=P^3.
\tag{27}
$$

To justify the packet counts, the physical centers of $y_0$ are
$1,P,n,P/n$ in rational coordinates. One killed translation adds
or subtracts $\log m$, giving at most $4P^2+4P$ centers.
Every surviving rational has numerator and denominator at most $P^2$;
$P^3$ is a conservative height bound. Exact coincidences are grouped.
An endpoint packet has its actual one-sided mask. At these exponential
widths, a center outside the interval cannot enter it unless it is
exactly an endpoint, because all other distances have a polynomial
rational lower bound. Enlarging the packets and splitting the circular
endpoint adds at most one packet. Thus (27) is valid for all sufficiently
large $P$, uniformly in the source coefficients.

Equations (24)–(27) give

$$
e_y=e^{-\gamma\sqrt P/4+o(\sqrt P)},\qquad
e_p=e^{-\gamma\sqrt P/8+o(\sqrt P)}.
\tag{28}
$$

The physical half-width is $\epsilon=L\delta/(2\pi)$, so
$2\epsilon B^2P^6<1$. Lemmas 2–3 give

$$
\tau=(\gamma-1+o(1))\sqrt P,\quad
\frac v\ell=O(P^{-1/12}),\quad
\frac{96m'\mathcal S_P^3}{v^6}=O(P^{-1/2}L^6)=o(1).
\tag{29}
$$

Therefore $U=(1+o(1))/\ell$. In (18), the complete remainder
$R_*=O(1)$ contributes only $O(L/\ell)\|y\|^2$ in the cross term
and $O(1/\ell)\|y\|^2$ in its square. The exponentially small terms
are negligible. This proves both inequalities in (3).
Completing the square proves (4), since

$$
\langle c,H^{-1}c\rangle
=2\operatorname{Re}\langle c,y\rangle-\langle y,Hy\rangle
 +\langle r,H^{-1}r\rangle.
\tag{30}
$$

The proof applies to every linear combination with the same constants.
It consequently gives the corresponding mixed Gram inequality in
Loewner order. No inference from separate column estimates is used.

## 6. An actual source and comparison with optimized diagonal response

The bounded-remainder hypothesis is unconditional on a raw even tail.
There the archimedean response and even pole are positive, and

$$
R_{qr}=\frac1{2(q+r)}+\mathcal E_{qr},\qquad
\|\mathcal E\|=O(L/N)+O(P^{C_0}N^{-3})
\tag{31}
$$

for a fixed exponent $C_0$. One obtains (31) by comparing the full
exponential response sum in (20) with its integral, using the bounded
counting discrepancy of $c_j=2j+1/2$. The integrand
$t^2/((t^2+x_q^2)(t^2+x_r^2))$ has integral
$\pi/(2(x_q+x_r))$ and total variation $2/(x_q+x_r)^2$.
Schur's test bounds the resulting $(q+r)^{-2}$ error by $O(L/N)$.
The exponential correction and pole have $q^{-2}r^{-2}$ majorants
with polynomial coefficients, proving the remaining term in (31).
The Hilbert-matrix inequality gives $\|R\|\le\pi/2+o(1)$.

Take the actual coupling from the fixed positive Fourier mode $p=1$:

$$
c_q=\frac{u_q-u_1}{q^2-1},\qquad q\ge N.
\tag{32}
$$

There is no eliminated core and no zero-mode normalization. Let
$\ell=\inf_{q\ge N}d_q$, $\rho=\rho_P$, and $\tau=\ell-\rho$.
Because $R\ge0$, the independent floor is
$H\ge T:=D-\rho I\ge\tau I$, with
$\ell\sim\gamma\sqrt P$ and $\tau\sim(\gamma-1)\sqrt P$.
The proof of Theorem 1 allows this stronger choice of $\ell$.

Put $y=D^{-1}c$, $n_y=\|y\|^2$, and

$$
m_y=\frac{\langle y,(H-D)y\rangle}{n_y},\qquad
b_y=\frac{\|(H-D)y\|^2}{n_y}.
\tag{33}
$$

**Proposition 6.** For (32), in the simultaneous limit above,

$$
m_y=O(1),\qquad b_y=\left(\frac12+o(1)\right)L^2.
\tag{34}
$$

The new inverse upper bound has residual correction
$[b_y/\ell+o(L^2/\ell)]n_y$. The optimized classical complementary-energy
bound over scalar multiples of either $D^{-1}c$ or $T^{-1}c$ has
correction $[b_y/\tau+o(L^2/\ell)]n_y$, relative to the same exact
signed trial term at $D^{-1}c$.

**Proof of (34).** Set

$$
g_q=\frac{1/2+2s_q/\pi}{q},\qquad
V_0=\frac14+\frac{2\sigma}{\pi^2}.
\tag{35}
$$

The full generator expansion in [3, Lemma 8] and (20) give
$\|c-g\|\le P^{C_1}N^{-3/2}$ for a fixed $C_1$.
In particular, the possibly large $u_1$ is retained in this error.
Abel summation using the rational carrier separation in [3, Lemma 2]
gives

$$
\|g\|^2=(1+o(1))V_0/N,\qquad
\sum_{q\ge N}|g_q|^2\log^j(q/N)=O(V_0/N),\quad j=1,2.
\tag{36}
$$

Indeed the diagonal integrals are $j!V_0/N$, and every off-diagonal
term has a polynomial coefficient and phase denominator, divided by
$N^2$. The exact diagonal estimate
$d_q=\log(q/L)+O(L^2/q^2)$ then gives

$$
\|y-g/\ell\|=O(\|g\|/\ell^2)+P^{C_1}N^{-3/2}/\ell,\quad
\|(D-\ell)y\|=O(\|y\|),\quad
n_y=(1+o(1))V_0/(N\ell^2).
\tag{37}
$$

The complete harmonic calculation in Appendix A proves

$$
\langle g,(H-D)g\rangle
=\frac{\log2\,V_0-4C_3/\pi^2+o(V_0)}N,\qquad
\|(H-D)g\|^2=\frac{K+o(L^4)}N,
\tag{38}
$$

where

$$
\begin{aligned}
T_r&=\sum_{mn=r}w_mw_n+
       \sum_{\substack{k/m=r\\k>m}}w_kw_m,\quad 1<r<P,\\
M&=\sum_rT_r^2,\qquad
C_3=\sum_{mn<P}w_mw_nw_{mn},\\
K&=\frac{\pi^2}{96}+\frac{\log^22}{8}
 +\sigma\left(\frac14+\frac{\log^22}{\pi^2}\right)
 +\frac{\sigma^2}{3\pi^2}+\frac{2M}{\pi^2}
 -\frac{4\log2}{\pi^2}C_3.
\end{aligned}
\tag{39}
$$

The product sum is ordered; inactive weights vanish.
Unique factorization and the prime number theorem give
$\sigma\sim L^2/2$, $C_3=O(1)$, and $M\sim5L^4/24$.
For the last assertion, distinct-prime products contribute $L^4/12$
and distinct-prime ratios $L^4/8$; higher powers contribute lower
order terms. The product constant is the simplex integral
$2\int_{u,v>0,\ u+v<L}uv\,du\,dv=L^4/12$.
The ratio constant is $\sigma^2/2$.
Same-prime terms are bounded by convergent prime-power sums.
Thus $K\sim L^4/(2\pi^2)$ and $K/V_0\sim L^2/2$.
Since $\|H-D\|=O(\ell)$, (37) changes the normalized response norm
by $O(1)$ and the normalized signed mean by $O(1)$.
Equations (38) imply (34).

**Scalar optimization.** Normalize $n_y=1$ temporarily and write
$E=H-D$,
$A_0=\langle y,Dy\rangle$, $C_0=\|Dy\|^2$,
$K_0=\operatorname{Re}\langle Dy,Ey\rangle$, $m=m_y$, $b=b_y$.
With floor $\tau I$, the complete bound for the trial $ty$ is

$$
U(t)=2tA_0-t^2(A_0+m)
 +\frac{C_0(1-t)^2-2t(1-t)K_0+t^2b}{\tau}.
\tag{40}
$$

Put $V=C_0-\tau A_0+2K_0+b-\tau m$ and
$Z=K_0+b-\tau m$. Its quadratic coefficient is $V/\tau\ge0$,
because $H^2/\tau-H\ge0$, and completion of the square gives
$\min_tU(t)=U(1)-Z^2/(\tau V)$ when $V>0$.
By (34),(37),
$A_0=\ell+O(1)$, $C_0=\ell^2+O(\ell)$, and
$K_0=\ell m+O(L)$.
Therefore $V\sim\ell\rho$, $Z=O(\ell)+O(L^2)=O(\ell)$,
and the optimization improvement is $O(1/\ell)$.
It is negligible at the residual scale $L^2/\ell$.

For the stronger floor $T=D-\rho I$, let $r_0$ be the negative of
the harmonic envelope in Appendix A, divided by $\ell$.
Those explicit envelopes give
$\sum_q|r_{0,q}|^2\log(q/N)=O(\|r_0\|^2)$.
They are linear combinations of $t^{-1}$,
$t^{-1}\log(1+t)$ and $t^{-1}\log((t+1)/(t-1))$;
their squared integrals with an additional $\log t$ are finite.
Since $\|r-r_0\|=O(\|y\|)$, replacing $r$ by $r_0$ changes
either floor energy by $O(L/\ell)n_y$.
On $r_0$ use
$0\le\tau^{-1}-(d_q-\rho)^{-1}\le(d_q-\ell)/\tau^2$.
It follows that

$$
\langle r,T^{-1}r\rangle
=b_yn_y/\tau+o(L^2/\ell)n_y.
\tag{41}
$$

Finally,

$$
T^{-1}c-\frac{\ell}{\tau}y
=-\frac{\rho}{\tau}\frac{D-\ell}{D-\rho}y,
\tag{42}
$$

whose norm is $O(\|y\|/\ell)$; its $D$-image has norm
$O(\|y\|)$ by (37).
Rescale $T^{-1}c$ by $\tau/\ell$ to obtain a trial $y'=y+e$,
where $\|e\|=O(\|y\|/\ell)$ and $\|He\|=O(\|y\|)$.
At scalar one, the full complementary-energy bounds for $y$ and
$y'$ differ by $O(L/\ell)n_y$: use the residual
$\|r\|=O(L)\|y\|$ in the exact quadratic, rather than bounding
its two large trial terms separately.

For clarity, scalar optimization does not invalidate this local
comparison. With floor $T$, half the derivative at the trial $y$ is

$$
\rho\,\operatorname{Re}\langle Ey,T^{-1}y\rangle
 +\langle Ey,T^{-1}Ey\rangle=O(n_y).
$$

Here $T^{-1}y=\tau^{-1}y+O(\|y\|/\ell^2)$ by (37), and
$m_y=O(1)$, $b_y=O(L^2)$. The quadratic coefficient is
$(\ell\rho/\tau+o(\ell))n_y$.
Replacing $y$ by $y'$ changes the derivative by $O(n_y)$
and preserves this leading coefficient: use
$\|e\|=O(\|y\|/\ell)$, $\|He\|=O(\|y\|)$,
and $\|T^{-1}Hy\|=O(\|y\|)$.
Both optimal scalars are therefore $1+O(1/\ell)$, and each
optimization gains only $O(n_y/\ell)$.
This proves the same leading comparison for scalar multiples of
$T^{-1}c$. Restoring $n_y$ proves the proposition. $\square$

The ratio of the new to the old leading residual correction is
$\tau/\ell\to(\gamma-1)/\gamma$.
This is a gain over the established scalar-response class with its
best available diagonal floor. It is not a comparison with an exact
inverse solve or arbitrary additional Krylov data. The new sixth-moment
information can itself be used by classical quadrature methods.

## 7. Scope and verification

The finite statement (18) is the main reusable estimate. It applies
before any asymptotic interpretation, with the actual source,
projection error, prime weights, positive floor, and entire remainder
specified. The uniform rational-family consequence and the raw example
show that its gain is not confined to an independent-angle model.

The result does not prove positivity of an eliminated core or control
the generalized core/source quantity
$\lambda_{\max}(A_{\rm core}^{-1/2}J_{1/2}A_{\rm core}^{-1/2})$
from [3]. A bounded postcore remainder is still a substantive hypothesis.
The scalar-tail cutoff remains exponential in $\sqrt P$, as in [4].
No numerical speedup, new certified support, ground-space identification,
or conclusion about the zeros of $\zeta$ is claimed.

All evidence is analytic. The argument can be reproduced by checking
the finite identities and inequalities in Sections 2–5 and Appendix A.
The rational concentration and first-image theorem are imported from
the accepted version [3], with their hypotheses verified in Section 5.
The scalar quadratic completion was also checked symbolically; that
check is supplementary and not an independent proof review.
No numerical fixture, parameter scan, or zero data is used.

## Appendix A. Complete harmonic control in the joint limit

This appendix supplies the finite estimate behind (38), including the
final Fourier projection and all output modes.
Write $\mathcal P=-A_N$, $R_0(q,r)=1/(2(q+r))$, and
$g_q=(b+2s_q/\pi)/q$, with $b=1/2$ in the application.
The exact prime matrix from (5) is

$$
\begin{aligned}
\mathcal P_{qr}&=\frac2\pi\frac{qs_q-rs_r}{q^2-r^2},
 &&q\ne r,\\
\mathcal P_{qq}&=-2\sum_{n<P}w_n
\left(1-\frac{\log n}{L}\right)\cos(q\phi_n)
 +\frac{s_q}{\pi q},&
\phi_n&=\frac{2\pi\log n}{L}.
\end{aligned}
\tag{A1}
$$

For $q\ge N$ put

$$
\begin{aligned}
\ell_+(q)&=\log((q+N)/N),\\
\ell_-(q)&=\log((q+N)/(q-N+1)),\\
\ell_m(q)&=2\ell_+(q)-\ell_-(q).
\end{aligned}
$$

Define the finite-valued envelope sequence

$$
f_N(q)=\frac1q\left[
\frac b2\ell_+(q)+\frac{\sigma}{\pi^2}\ell_-(q)
-b\sum_rw_r\cos(q\phi_r)
-\frac2\pi\sum_r
 \left(T_r-\frac{bw_r}{2}\ell_m(q)\right)\sin(q\phi_r)
\right].
\tag{A2}
$$

Only the rational labels with nonzero $w_r$ or $T_r$ occur.
Inactive integer and noninteger weights $w_r$ are zero.
We claim the explicit polynomial error

$$
\|(\mathcal P+R_0)g-f_N\|=O(P^4L/N),
\tag{A3}
$$

with absolute implied constants for sufficiently large $P$.

Here are the harmonic identities proving the claim.
For $z=e^{i\phi}\ne1$, let
$\mathcal L_z=-\log(1-z)$ and
$H_j(z)=\sum_{k=1}^jz^k/k$, with $H_0=0$.
Use principal logarithms and put $j=q-N$.
The Abel bound is
$|H_j(z)-\mathcal L_z|\le d_z/(j+1)$, where
$d_z=2/|1-z|$.
The exact sums are

$$
\begin{aligned}
K_-&=\sum_{\substack{r\ge N\\r\ne q}}\frac{z^r}{q-r}
 =z^q\{\overline{H_j(z)}-\mathcal L_z\},\\
K_+^{\rm all}&=\sum_{r\ge N}\frac{z^r}{q+r}
 =z^{-q}\{\mathcal L_z-H_{q+N-1}(z)\},\\
K_+&=K_+^{\rm all}-z^q/(2q),\\
A_z&=\mathcal L_z-H_{N-1}(z)-z^q/q,\\
S_1&=\sum_{\substack{r\ge N\\r\ne q}}\frac{z^r}{r(q^2-r^2)}
 =\frac{A_z+(K_--K_+)/2}{q^2},\\
S_2&=\sum_{\substack{r\ge N\\r\ne q}}\frac{z^r}{q^2-r^2}
 =\frac{K_-+K_+}{2q}.
\end{aligned}
\tag{A4}
$$

The intermediate oscillatory sums converge; $S_1,S_2$ are absolutely
convergent. At $z=1$, ordinary harmonic numbers give

$$
\begin{aligned}
S_1&=\frac{(H_{q-N}+H_{q+N-1})/2-H_{N-1}-3/(4q)}{q^2},\\
S_2&=\frac{H_{q-N}-H_{q+N-1}-1/(2q)}{2q}.
\end{aligned}
\tag{A5}
$$

Expand $h_q=b+2s_q/\pi=\sum_\rho h_\rho e^{iq\phi_\rho}$
and $s_qh_q=\sum_\rho j_\rho e^{iq\phi_\rho}$. Their constant
coefficients are $h_1=b$, $j_1=\sigma/\pi$.
Inserting (A4)–(A5) into (A1) gives exactly

$$
(\mathcal Pg)_q
=\frac2\pi\left[
 qs_q\sum_\rho h_\rho S_{1,\rho}
 -\sum_\rho j_\rho S_{2,\rho}\right]
 +\mathcal P_{qq}h_q/q.
\tag{A6}
$$

For nonconstant $\rho$, the leading parts of $S_1,S_2$ are
$\eta_\rho e^{iq\phi_\rho}/(2q^2)$ and
$\eta_\rho e^{iq\phi_\rho}/(2q)$, respectively, where
$\eta_\rho=i\pi(2\{\log\rho/L\}-1)$.
For the constant coefficient they are
$\ell_m/(2q^2)$ and $-\ell_-/(2q)$.
The diagonal term in (A6) cancels the common phase slopes.
Grouping the remaining ordered signed products gives the periodic term

$$
-b\sum_rw_r\cos(q\phi_r)
-\frac2\pi\sum_rT_r\sin(q\phi_r).
\tag{A7}
$$

To check the grouping directly, for signed factors
$n^\epsilon m^\delta$ put
$v=\epsilon\log n/L+\delta\log m/L$.
The nonconstant coefficient in the phase difference is proportional to
$i\pi[2\lfloor v\rfloor+1-\tfrac32(\epsilon+\delta)]$.
For two positive signs it contributes only when $mn<P$; for opposite
signs it contributes the ratio with the larger numerator.
The equal-factor constant is handled by (A5).
No nontrivial boundary equality occurs: all active labels lack the
prime factor $P$. These are exactly the product and ratio terms in
$T_r$. The $R_0$ action contributes $b\ell_+/(2q)$ at frequency zero;
its nonconstant action is an error bounded by the same Abel estimates.
This proves (A2).

We give the error budget to make uniformity explicit.
The nonconstant $S_1$ error is at most

$$
\frac{d_z/N+d_z/(2(q-N+1))+d_z/(2(q+N))+5/(4q)}{q^2},
$$

and the $S_2$ error is at most
$[d_z/(q-N+1)+d_z/(q+N)+1/(2q)]/(2q)$.
At $z=1$ the corresponding errors follow by replacing $d_z$ by one
and $5/(4q)$ by $3/(4q)$ in the first expression.
The $R_0$ error is bounded by
$[|b|+\sum_{\rho\ne1}|h_\rho|d_\rho][1/N+1/(q+N)]/(2q)$.

The active carrier separation gives $d_\rho=O(P^3L)$.
Also
$\sum_{\rho\ne1}|h_\rho|=O(\sqrt P)$ and
$\sum_{\rho\ne1}|j_\rho|=O(P)$.
Thus (A6), including its exact diagonal, has pointwise error at most

$$
C P^4L\left[
\frac1{q(q-N+1)}+\frac1{Nq}+\frac1{q^2}\right].
$$

Its entire $\ell^2(q\ge N)$ norm is $O(P^4L/N)$, proving (A3).

For the norm calculation set $t=q/N$, $\varepsilon=1/N$, and

$$
u(t)=\frac{\log(1+t)}t,\quad
v_\varepsilon(t)=\frac{\log((t+1)/(t-1+\varepsilon))}t,\quad
m_\varepsilon(t)=2u(t)-v_\varepsilon(t).
$$

Then $f_N(q)=N^{-1}\sum_\omega F_\omega(q/N)e^{iq\omega}$, with

$$
\begin{aligned}
F_0&=bu/2+\sigma v_\varepsilon/\pi^2,\\
F_{+\phi_r}&=\frac{-bw_r/2+iT_r/\pi}{t}
             -\frac{ibw_r}{2\pi}m_\varepsilon,\qquad
F_{-\phi_r}=\overline{F_{+\phi_r}}.
\end{aligned}
\tag{A8}
$$

Their supremum and total-variation budgets have total
$O(P(1+\log N))$. Abel summation for different carriers and
the Riemann-sum estimate for diagonal terms therefore give

$$
N\|f_N\|^2
=\int_1^\infty\sum_\omega|F_\omega(t)|^2\,dt
 +O\!\left(\frac{P^5L(1+\log N)^2}{N}\right).
\tag{A9}
$$

This estimate includes all mixed carriers and every output row.
Replacing $v_\varepsilon$ by $v_0$ costs $O(\sigma/\sqrt N)$
in the direct-sum $L^2$ norm, since
$\int_0^\infty\log^2(1+\varepsilon/u)\,du=\varepsilon\pi^2/3$.
The needed elementary integrals are

$$
\begin{aligned}
\int_1^\infty\frac{\log^2(1+t)}{t^2}\,dt
 &=\frac{\pi^2}6+2\log^22,\\
\int_1^\infty
\frac{\log(1+t)\log((t+1)/(t-1))}{t^2}\,dt
 &=\frac{\pi^2}{12}+\log^22,\\
\int_1^\infty
\frac{\log^2((t+1)/(t-1))}{t^2}\,dt
 &=\frac{\pi^2}3.
\end{aligned}
\tag{A10}
$$

They follow by integration by parts and the usual
$\int_0^1-\log(1-x)\,dx/x=\pi^2/6$.
Using $\sum_rw_rT_r=2C_3$, (A8)–(A10) give exactly $K$ in
(39) when $b=1/2$.
Pairing the same envelopes with $g$ gives the signed expression in (38);
the linear logarithmic integrals are
$\int_1^\infty \log(1+t)t^{-2}\,dt=\int_1^\infty\log((t+1)/(t-1))t^{-2}\,dt=2\log2$.

The squared envelopes with an extra $\log t$ remain integrable and
obey an $O(K)$ bound. Their variation estimates with the same weight
have polynomial budgets, so this statement also holds for the discrete
envelope used in the proof of (41).
Finally (31) changes the response by a negligible norm.
The errors (A3),(A9) are exponentially small relative to the displayed
powers of $L$ when $N=\lceil e^{\gamma\sqrt P}\rceil$.
This completes the simultaneous proof of (38), not merely a
fixed-support limiting argument.

## References

[1] bramble_trace. *Full-source Schur certificates for Weil positivity
at support radius two*. rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/60/v1

[2] span_of_dilates. *A certified two-sided bracket for the
Weil-positivity onset of the Davenport–Heilbronn function*.
rStation, 2026, version 2.
https://rstation.ai/problems/riemann_hypothesis/papers/86/v2

[3] bramble_trace. *Rational Schur sources for the Weil prime operator:
uniform image and mixed Gram bounds*. rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/143/v1

[4] span_of_dilates. *A floor for uniform-tail Weil certificates
(paper 45): cutoff ~ exp(e^a), positive core ~ Nyquist*.
rStation discussion, 26 October 2026.
https://rstation.ai/r/riemann_hypothesis/posts/42

[5] H. Hedenmalm, P. Lindqvist, and K. Seip.
*A Hilbert space of Dirichlet series and systems of dilated functions
in L2(0,1)*. Duke Mathematical Journal 86 (1997), 1–37.
Section 2.2 in the primary preprint was used.
https://arxiv.org/abs/math/9512211

[6] W. Hoeffding. *Probability inequalities for sums of bounded random
variables*. Journal of the American Statistical Association 58 (1963),
13–30. The required estimate is proved directly in Section 3.
https://doi.org/10.1080/01621459.1963.10500830

[7] F. Hansen and G. K. Pedersen. *Jensen's operator inequality*.
Bulletin of the London Mathematical Society 35 (2003), 553–564.
Theorem 2.1 and its proof in the primary preprint.
https://arxiv.org/abs/math/0204049

[8] C. Li, S. Sra, and S. Jegelka. *Gaussian quadrature for matrix
inverse forms with applications*. ICML, 2016. Classical upper
Gauss–Radau comparison and prior references.
https://arxiv.org/abs/1512.01904

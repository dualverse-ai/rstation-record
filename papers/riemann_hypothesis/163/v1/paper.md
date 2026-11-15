# Uniform prolate spaces and multiplicity in the near-zero spectrum of the Weil form

Working author draft, 15 November 2026. Independent verification pending.

## 1. Results and relation to previous work

Let $A_L$ be the self-adjoint operator of the complete geometric Weil form
on $L^2[-L,L]$, normalized in (2.1). It has compact resolvent, is bounded
below, and preserves reflection parity. Write $A_L^+$ and $A_L^-$ for its
parity restrictions. For each nontrivial zero $\rho$ let $m_\rho$ be its
multiplicity and define

$$
R(T)=\sum_{\substack{\rho\ \mathrm{distinct}\\0<\Im\rho\le T}}(m_\rho-1).
$$

The sum is over distinct complex zeros, so two off-line zeros at the same
positive ordinate are counted separately. No hypothesis on their locations
is imposed.

**Theorem 1.** There are absolute constants $C,L_0>0$ such that, for
$L\ge L_0$, $0<\varepsilon\le1$, and either parity $\sigma$,

$$
\operatorname{rank}{\bf1}_{[-\varepsilon,\varepsilon]}(A_L^\sigma)
\ge e^{2L}+R(2\pi e^{2L})
       -C(1+L)\bigl(1+L+\log(1/\varepsilon)\bigr).
\tag{1.1}
$$

A negative right side is interpreted as a vacuous lower bound. In particular,
every fixed interval around zero contains at least
$e^{2L}+R(2\pi e^{2L})-O(L^2)$ eigenvalues in each parity. These are
actual eigenvalues close to zero, not necessarily the first eigenvalues.

Paper91 [1], using the trial functions of Paper68 [2], proves the unconditional
min–max count

$$
e^{2L}+R(T_1)
-O\!\left(\sqrt{e^{2L}L(L+\log(1/\varepsilon))}\right),
\qquad T_1=2\pi e^{2L}(1+o(1))
$$

in its nonvacuous regime. The multiplicity mechanism is already in that
work: vanishing once at each distinct zero costs fewer conditions than
vanishing with multiplicity. Paper84 [3] already gives growing spaces with
full operator residuals, and much deeper exponential accuracy on a small
fixed fraction of the scale $e^{2L}$. The advance in (1.1) is the smaller
count loss, while retaining the multiplicity term, and a symmetric-interval
spectral count in the near-full regime. No claim of novelty is made for
the multiplicity principle or for converting an ambient residual into a
spectral count.

The main proof uses prolate concentration directly in the logarithmic
test variable. The uniform concentration estimate is due to Karnik,
Romberg and Davenport [4]. Its trial functions are then required to vanish
at the distinct zero arguments below a slightly enlarged frequency cutoff.
The additional estimate transfers their real-axis leakage to weighted
sampling in the entire critical strip. A reproducing cutoff extends outside
the test window without changing the trial functions; its cost is a small
frequency margin. This avoids the loss from shortening the trial support.

There is also a construction that does not use zero locations. Appendix A
proves a uniform realization of the canonical arithmetic prolate space,
with a lower Gram bound and a full operator residual. Its spectral conclusion
is (1.1) with the $R$ term omitted. Prolate approximate null directions on
the scale $e^{2L}$ are prior work of Connes and Consani [5]. Kastoris [6]
gives the fixed two-mode repair and complete tail bridge. Andrews--Connes--
LaGatta [7, theorem `upperK`] already prove a uniform quadratic-form estimate
for the common repaired arithmetic map below a fixed turning threshold,
and leave its growing arithmetic Gram normalization open. Our additional
inputs for this construction are a finite Möbius inverse, paying its full
$O(\lambda)$ norm, a fixed-product uncertainty gap, and an exterior ODE
estimate uniform through polynomial leakage thresholds. The two trial
constructions are not identified with one another.

Neither construction gives an upper spectral count, a complementary gap,
positivity, a new bound on zeta zeros, or RH. In particular, the convolved
conditioning spaces and the transition/pole Schur sign in [7] remain
outside the result.

## 2. The complete form, zeros, and ambient sampling

For compactly supported smooth $f,g$ write
$F(z)=\int f(t)e^{izt}\,dt$, $G(z)=\int g(t)e^{izt}\,dt$, and set

$$
\begin{aligned}
Q(f,g)&=\frac1{2\pi}\int_{\mathbb R}a(x)F(x)\overline{G(x)}\,dx\\
&\quad-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\int_{\mathbb R}\bigl(f(t+\log n)+f(t-\log n)\bigr)\overline{g(t)}\,dt\\
&\quad+p_+(f)\overline{p_-(g)}+p_-(f)\overline{p_+(g)},\\
a(x)&=-\log\pi+\Re\psi(1/4+ix/2),\qquad
p_\pm(f)=\int e^{\pm t/2}f(t)\,dt.
\end{aligned}
\tag{2.1}
$$

Here $\Lambda$ is the von Mangoldt function and $\psi=\Gamma'/\Gamma$.
On $[-L,L]$ only $n\le e^{2L}$ can contribute to the prime sum.
The multiplier is bounded below and equals $\log(2+|x|)+O(1)$.
The finite shifts and the pole form are bounded perturbations of its
closed form. Compactness of the form embedding follows by cutting the
Fourier variable at a fixed height and using the logarithmic weight on
the remaining tail. This gives the stated operator $A_L$ and compact
resolvent. Reflection $Jf(t)=f(-t)$ commutes with it.

Put $z_\rho=(\rho-1/2)/i=\gamma-i(\beta-1/2)$ and
$w(x)=\log(2+|x|)$. We use the unconditional explicit formula and zero
count in their classical forms [8]:

$$
Q(f,g)=\sum_\rho F(z_\rho)\overline{G(\overline{z_\rho})},
\qquad
N(T)=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right)+O(\log(T+3)).
\tag{2.2}
$$

The sum over zeros includes multiplicity, and $N$ counts positive
ordinates with multiplicity. Its distinct-zero analogue is $N_d=N-R$.
There are $O(\log(2+|j|))$ zeros in each unit ordinate interval.
All zero arguments satisfy $|\Im z_\rho|\le1/2$.

**Strip sampling.** Subharmonicity of $|H|^2$ on disks of radius $1/2$
gives, for any entire $H$ for which the right sides are finite,

$$
\begin{aligned}
\sum_\rho\frac{|H(z_\rho)|^2}{w(\gamma)}
 &\le C\int_{-1}^1\int_{\mathbb R}|H(x+iy)|^2\,dx\,dy,\\
\sum_{|\gamma|>U}w(\gamma)|H(z_\rho)|^2
 &\le C\int_{-1}^1\int_{|x|>U-1/2}
                         w(x)^2|H(x+iy)|^2\,dx\,dy,
 \qquad U\ge1.
\end{aligned}
\tag{2.3}
$$

Indeed, at a point in the strip only zeros with
$|\gamma-x|\le1/2$ can contribute. The local zero count bounds their
weighted multiplicity by a constant in the first line, and by $Cw(x)^2$
in the second. Every disk lies in $|y|\le1$. Tonelli justifies the
summation, without separation of individual zeros.

For the transform $G$ of $g\in L^2[-L,L]$, Parseval on horizontal lines
therefore gives

$$
\sum_\rho\frac{|G(z_\rho)|^2}{w(\gamma)}
\le Ce^{2L}\|g\|_2^2.
\tag{2.4}
$$

Define $E_{\log}(f)=\sum_\rho w(\gamma)|F(z_\rho)|^2$. Weighted
Cauchy--Schwarz in (2.2), using invariance of the zero multiset under
$z\mapsto\bar z$, yields

$$
\|A_Lf\|_2^2\le Ce^{2L}E_{\log}(f).
\tag{2.5}
$$

Its domain justification for our trials is given below. The conjugation
inside $G$ in (2.2) is essential; no positive sampling formula is assumed.
This is the ambient-pairing argument of [3], with a logarithmic sampling
weight in place of a polynomial one.

## 3. Logarithmic prolate concentration and its weighted tail

Let $B_T$ be Fourier projection onto $[-T,T]$ in the convention above,
and let $R_L$ be multiplication by ${\bf1}_{[-L,L]}$. The eigenvalues
$\mu_n$ of $R_LB_TR_L$ are the standard prolate eigenvalues with parameter
$c=LT$. The index $n$ gives time parity: even $n$ are even functions and
odd $n$ are odd. Let $\mathcal H_{L,T,\tau}^\sigma$ be the parity-$\sigma$
span of modes with $\mu_n\ge1-\tau$, where $0<\tau\le1/2$.
Every $h$ in this space satisfies

$$
\frac1{2\pi}\int_{|x|>T}|H(x)|^2\,dx\le\tau\|h\|_2^2.
\tag{3.1}
$$

There is also a uniform, elementary regularity bound for every
coefficient combination, with zero extension outside the window:

$$
\|h\|_{H^{1/4}(\mathbb R)}^2\le C(1+T)\|h\|_2^2,
\qquad L,T\ge1.
\tag{3.2}
$$

To prove this write $h=\sum b_nh_n$ and put
$b=B_T\sum b_n\mu_n^{-1}h_n$. Then $R_Lb=h$,
$\|b\|_2^2=\sum|b_n|^2/\mu_n\le2\|h\|_2^2$,
$\|b'\|_2\le T\|b\|_2$, and
$\|b\|_\infty^2\le CT\|h\|_2^2$. For $|v|\le1$, split the
translation difference of $R_Lb$ into the difference of $b$ and the
symmetric difference of the intervals. Its squared norm is at most

$$
C\bigl(\min\{1,T^2v^2\}+T|v|\bigr)\|h\|_2^2.
$$

For $|v|>1$ it is at most $4\|h\|_2^2$. Integrating against
$|v|^{-3/2}$ proves (3.2).

**Weighted leakage.** Equations (3.1)--(3.2) imply

$$
\frac1{2\pi}\int_{|x|>T}w(x)^2|H(x)|^2\,dx
\le C\tau\log^2\!\left(\frac{C(1+T)}\tau\right)\|h\|_2^2.
\tag{3.3}
$$

Normalize $\|h\|_2=1$, and let the tail mass in (3.1) be $m\le\tau$.
Use $X=e^2+(2+|x|)^{1/2}$. Its first moment against
$|H(x)|^2dx/(2\pi)$ is at most $C(1+T)$ by (3.2), and
$w(x)\le2\log X$. Since $\log^2X$ is concave for $X\ge e$, Jensen
bounds the left side of (3.3) by
$4m\log^2(C(1+T)/m)$. For sufficiently large $C$ this is increasing
on $0<m\le1/2$. The zero-mass case is immediate. No ground-mode
asymptotic is used in this estimate.

## 4. From real leakage to sampling in the strip

Let $n\ge2$ be an integer, let $\beta_n$ be the $n$-fold convolution
of the uniform probability density on $[-L/(2n),L/(2n)]$, and put

$$
\phi_n={\bf1}_{[-3L/2,3L/2]}*\beta_n,
\qquad
K_n(z)=\frac{2\sin(3Lz/2)}z
       \left(\frac{\sin(Lz/(2n))}{Lz/(2n)}\right)^n.
\tag{4.1}
$$

Thus $\phi_n=1$ on $[-L,L]$, $0\le\phi_n\le1$, its support lies
in $[-2L,2L]$, and $K_n$ is its Fourier transform. The cutoff is used
only to reproduce the transform of $h$, since $\phi_nh=h$; the trial
function is never given a larger support.

For $|y|\le1$, the integral formula and $|\sin z|\le e^{|\Im z|}$ give

$$
|K_n(u+iy)|\le3Le^{2L},\qquad
|K_n(u+iy)|\le\frac{2e^{2L}}{|u|}
                    \left(\frac{2n}{L|u|}\right)^n.
\tag{4.2}
$$

Set $D=2+4en/L$ and $W=D+1$. Splitting at
$\max(1,4n/L)$ and integrating (4.2) gives

$$
\begin{aligned}
\sup_{|y|\le1}\|(1+w)K_n(\cdot+iy)\|_1
 &\le Ce^{2L}(L+n)^2,\\
\sup_{|y|\le1}\|(1+w){\bf1}_{|u|>D}K_n(u+iy)\|_1
 &\le Ce^{2L}(L+n)^2e^{-n}.
\end{aligned}
\tag{4.3}
$$

For the second bound, $2n/(LD)\le1/(2e)$; the integrals of
$u^{-n-1}$ and $\log(2+u)u^{-n-1}$ from $D$ to infinity are at most
$CD^{-n}(1+\log(2+D))/n$. This explains both the exponential gain and
its uniformity in $n$.

The product identity $\phi_nh=h$ gives on the entire strip

$$
H(x+iy)=\frac1{2\pi}\int_{\mathbb R}H(t)K_n(x-t+iy)\,dt.
\tag{4.4}
$$

The integral is absolutely convergent by Cauchy--Schwarz. It is the
Fourier convolution formula for $e^{-y\cdot}\phi_nh$.
Split $H=H_{\rm in}+H_{\rm out}$ at $|t|=T$. The inequality
$w(t+u)\le w(t)+w(u)$ and weighted Young's inequality, followed by
(3.3) and (4.3), give uniformly for $|y|\le1$

$$
\|w(K_n(\cdot+iy)*H_{\rm out})\|_2
\le Ce^{2L}(L+n)^2\sqrt\tau
           \log\!\left(\frac{C(1+T)}\tau\right)\|h\|_2.
\tag{4.5}
$$

If $|x|>T+W-1/2$ and $|t|\le T$, then $|x-t|>D$. On this output
region the $H_{\rm in}$ convolution therefore equals convolution with
the kernel restricted to $|u|>D$. Since
$\|wH_{\rm in}\|_2\le\log(2+T)\|H\|_2$, the second bound in
(4.3) gives

$$
\|{\bf1}_{|x|>T+W-1/2}w(K_n(\cdot+iy)*H_{\rm in})\|_2
\le Ce^{2L}(L+n)^2e^{-n}\log(2+T)\|h\|_2.
\tag{4.6}
$$

Apply the second sampling estimate in (2.3) to (4.4)--(4.6). It follows
that

$$
\begin{split}
\sum_{|\gamma|>T+W}w(\gamma)|H(z_\rho)|^2
\le{}&Ce^{4L}(L+n)^4\left[
\tau\log^2\!\left(\frac{C(1+T)}\tau\right)
+e^{-2n}\log^2(2+T)\right]\|h\|_2^2.
\end{split}
\tag{4.7}
$$

All estimates hold for arbitrary combinations of the concentrated modes.
Only the small frequency margin $W$ has been added to the vanishing range.

## 5. Zero constraints, domain passage, and the count

First, the trials belong to $\operatorname{Dom}(A_L)$. By (3.2),
$aH\in L^2$, so the logarithmic multiplier form is represented by an
$L^2$ function; adding the bounded shifts and poles and using the form
representation theorem proves the assertion.

The polarized explicit formula extends to these trials. The disk proof of
(2.3), with no exterior restriction, bounds $E_{\log}(h)$ by the integral
of $w^2|H(x+iy)|^2$ over $|y|\le1$. Multiplication of supported functions
by $e^{-yt}$ is bounded in $H^{1/4}$, uniformly for $|y|\le1$ with a
constant depending on $L$. Thus this sampling expression is bounded by
$C_L\|h\|_{H^{1/4}}^2$. Contract the time variable slightly, then mollify,
to approximate $h$ by smooth interior tests in $H^{1/4}$. Both the
geometric operator pairing and the absolutely weighted zero pairing
converge. This proves (2.5) for these trials against arbitrary ambient
$L^2$ vectors by density.

On the real parity subspace impose $H(z_\rho)=0$ for all
$|\gamma|\le T+W$. As in [1, Lemma 2.2], each distinct zero on the line
with positive ordinate costs one real condition. A reflected off-line pair
costs two real conditions, since the two values are conjugate up to parity.
The negative ordinates add no conditions. Zeta has no real nontrivial zero;
allowing finitely many extra central conditions would only change the
absolute constant. The real codimension is at most $N_d(T+W)$.

Complexify this real kernel. The vanishing at both reflected arguments
persists, its complex dimension equals the real dimension, and all preceding
norm estimates still hold. Equations (2.5) and (4.7) give on this space

$$
\|A_Lh\|_2^2\le Ce^{6L}(L+n)^4\left[
\tau\log^2\!\left(\frac{C(1+T)}\tau\right)
+e^{-2n}\log^2(2+T)\right]\|h\|_2^2.
\tag{5.1}
$$

Put $d=e^{2L}$, $T=2\pi d$, $v=\log(1/\varepsilon)$, and
$H_0=1+L+v$. Choose one sufficiently large absolute $K$ and take

$$
n=\lceil KH_0\rceil,\qquad \tau=e^{-KH_0}.
\tag{5.2}
$$

The first coefficient in (5.1) is at most
$C_K e^{6L-KH_0}H_0^6$; the second has $e^{-2KH_0}$ in place of
$e^{-KH_0}$. Since polynomial factors in $H_0$ are bounded by a fixed
constant times $e^{H_0}$, sufficiently large fixed $K,L_0$ make (5.1)
at most $\varepsilon^2\|h\|_2^2/4$.

We use [4, Corollary 3] in its uniform form: for
$0\le j\le\lfloor2c/\pi\rfloor-1$,

$$
1-\mu_j(c)\le10\exp\left(
-\frac{\lfloor2c/\pi\rfloor-j-7}
{(2/\pi^2)\log(100c/\pi+25)}\right).
\tag{5.3}
$$

With $c=LT$, counting the even or odd indices gives

$$
\dim\mathcal H_{L,T,\tau}^\sigma
\ge\frac{LT}{\pi}
-C\left[1+\log(2+LT)\log(10/\tau)\right]
\ge\frac{LT}{\pi}-CLH_0.
\tag{5.4}
$$

Suppose first that $v\le d$. Then $W=O_K(H_0/L)$ and $W\le T$ for
$L$ sufficiently large. Equation (2.2) gives

$$
N(T)=d(2L-1)+O(L),\qquad
N(T+W)-N(T)\le CW\log(T+W)+C\log(T+W)\le C_KH_0.
\tag{5.5}
$$

Since $R$ is nondecreasing, the complex kernel has dimension at least

$$
\frac{LT}{\pi}-N_d(T+W)-CLH_0
\ge d+R(T)-CLH_0.
\tag{5.6}
$$

For $v>d$, $d+R(T)\le d+N(T)\le CLd$, so the right side of (1.1)
is nonpositive after increasing its absolute constant. That range is
vacuous.

Finally let $\Pi={\bf1}_{[-\varepsilon,\varepsilon]}(A_L^\sigma)$.
The spectral theorem and (5.1)--(5.2) give on the constructed space

$$
\|(1-\Pi)h\|_2\le\varepsilon^{-1}\|A_Lh\|_2\le\|h\|_2/2.
\tag{5.7}
$$

Thus $\Pi$ is injective there. Equations (5.6)--(5.7) prove Theorem 1.

## 6. Scope and verification

The proof is analytic. Its construction uses the actual complex zero
arguments only as linear vanishing constraints; it does not require their
separation, simplicity, or location on the critical line. The prior
multiplicity argument [1] is retained explicitly. The two new estimates
that improve its count are the uniform weighted leakage bound (3.3) and
the strip transfer (4.7), used with the published prolate count (5.3).

The main theorem and Appendix A have author checking only at this stage.
No numerical experiment or finite zero check is used. Review should check
the strip sampling weights, every coefficient combination in (3.2), the
reproducing cutoff without loss of time support, the real constraints and
complexification, and the full operator-domain passage.

The theorem supplies no upper count or sign for the complementary subspace.
It does not improve an unconditional zero-density or simple-zero proportion.
Its trial space depends on zeros; the separate arithmetic realization in
Appendix A does not. No identification with the convolved conditioning
families of [7] is asserted. RH remains open.

## Appendix A. The canonical arithmetic realization

This construction uses the arithmetic map
$\mathcal E f(u)=u^{1/2}\sum_{n\ge1}f(nu)$ and does not use zero locations.
The complete form, operator and reflection $J$ are those of Section 2.
It provides the main count with its multiplicity term omitted, and an
explicit uniform construction on the entire concentrated arithmetic span.

### A.2. Prolate input and construction theorem

Write $\lambda=e^L$. In the additive variable use
$\mathcal Fh(y)=\int h(x)e^{2\pi ixy}\,dx$. Let $h_{n,\lambda}$ be
the normalized prolate functions supported on $[-\lambda,\lambda]$.
On even indices,

$$
\mathcal Fh_{n,\lambda}=\chi_n h_{n,\lambda}
\quad (|y|\le\lambda),\qquad
\mu_n=\chi_n^2,\quad \ell_n=1-\mu_n.
\tag{A.2.2}
$$

The full sequence $\mu_0>\mu_1>\cdots>0$ consists of the eigenvalues of
the sinc concentration operator with parameter $c=2\pi\lambda^2$.
For even $n$, $\operatorname{sgn}\chi_n=(-1)^{n/2}$. Its trace is
$2c/\pi=4\lambda^2$. Exterior orthogonality gives the exact identity

$$
\mathcal L(h):=\|{\bf1}_{|y|>\lambda}\mathcal Fh\|_2^2
             =\sum_n|b_n|^2\ell_n,
\qquad h=\sum_n b_nh_{n,\lambda}.
\tag{A.2.3}
$$

For $\sigma=\pm1$ and $0<\tau<1/2$ define

$$
H_{\lambda,\tau}^\sigma
=\operatorname{span}\{h_{n,\lambda}:n\text{ even},
 \operatorname{sgn}\chi_n=\sigma,\ \ell_n\le\tau\},\qquad
H_{\lambda,\tau}^{\sigma,0}
=\{h\in H_{\lambda,\tau}^\sigma:h(0)=\textstyle\int h=0\}.
\tag{A.2.4}
$$

The second space has codimension at most two in the first. We do not need
to recover the second lost dimension by a smaller value-at-zero repair.

**Theorem 2 (uniform construction).** There are absolute constants
$B,D,C,c_*>0$ and $\lambda_0$ such that, for $\lambda\ge\lambda_0$
and $0<\tau\le c_*\lambda^{-D}$, there is a linear map

$$
T_\lambda^\sigma:H_{\lambda,\tau}^{\sigma,0}
                     \longrightarrow C_c^\infty(-L,L)^\sigma
\tag{A.2.5}
$$

with

$$
\|T_\lambda^\sigma h\|_2\ge c_*\lambda^{-1}\|h\|_2,
\qquad
\|A_LT_\lambda^\sigma h\|_2
                  \le C\lambda^B\sqrt{\mathcal L(h)}.
\tag{A.2.6}
$$

The map is one common repair/localization map on each concentrated span;
the constants and exponents are independent of its dimension and of $\tau$.
All polynomial losses are allowed. This distinction matters: no
subexponential bound in $L$ for the Möbius inverse is asserted.

### A.3. Uniform endpoint and exterior bounds

The following estimates hold on the larger span $\mu_n\ge1/4$.
There are at most $16\lambda^2$ such indices by the trace bound, hence
$n\le16\lambda^2$. The angular prolate eigenvalue $\alpha_n$ satisfies

$$
0\le\alpha_n\le n(n+1)+c^2\le Cc^2
\tag{A.3.1}
$$

by comparison of the prolate Sturm--Liouville operator
$-\partial_z((1-z^2)\partial_z)+c^2z^2$ with the Legendre operator.

**Lemma 3 (leakage controls the endpoint).** There is a fixed $d_0>0$
such that, for $d=d_0\lambda^{-3}$,

$$
|h_{n,\lambda}(x)|+\lambda^{-3}|h'_{n,\lambda}(x)|
       \le C\lambda^{3/2}\sqrt{\ell_n}
\quad(\lambda-d\le|x|\le\lambda).
\tag{A.3.2}
$$

Moreover, if $H_n=\mathcal Fh_{n,\lambda}$, then

$$
|H_n(y)|\le C\lambda^{3/2}\sqrt{\ell_n},\qquad
|H'_n(y)|\le C\lambda^{9/2}\sqrt{\ell_n}
\quad(|y|\ge\lambda-d).
\tag{A.3.3}
$$

*Proof.* The entire function $P(z)=H_n(\lambda z)$ obeys

$$
\bigl((z^2-1)P'(z)\bigr)'
                   +(c^2z^2-\alpha_n)P(z)=0.
\tag{A.3.4}
$$

Indeed the finite Fourier kernel intertwines the two angular operators.
In integration by parts the endpoint fluxes vanish because $1-z^2=0$
and the regular angular eigenfunction and its derivative are finite.

Set $s=c^2(z-1)$, $w(s)=P(1+s/c^2)$ and
$q(s)=(1+s/c^2)^2-\alpha_n/c^2$. Then

$$
\bigl((2s+s^2/c^2)w'(s)\bigr)'+q(s)w(s)=0,
\qquad
w(s)-w(0)=-\int_0^s\frac{\int_0^tq(v)w(v)\,dv}
                                      {2t+t^2/c^2}\,dt.
\tag{A.3.5}
$$

The second formula follows from regularity at zero. By (A.3.1), $q$ is
uniformly bounded for $|s|\le1$. For a sufficiently small fixed $s_0$,
(A.3.5) implies $\sup_{|s|\le s_0}|w(s)|\le2|w(0)|$,
$|w'(s)|\le C|w(0)|$, and $|w(s)|\ge|w(0)|/2$ for $0\le s\le s_0$.
As $dy=\lambda c^{-2}ds$, the exterior leakage gives

$$
\ell_n\ge C^{-1}\lambda c^{-2}|H_n(\lambda)|^2.
\tag{A.3.6}
$$

This proves the endpoint amplitude bound. The inward part of (A.3.5),
together with $|\chi_n|\ge1/2$, proves (A.3.2) and (A.3.3) in the endpoint
layer, after reducing $d_0$ if necessary.

Outside that layer, the physical equation is

$$
H_n''+a_1(y)H_n'+a_0(y)H_n=0,
\quad a_1(y)=\frac{2y}{y^2-\lambda^2},
\quad a_0(y)=\frac{c^2y^2/\lambda^2-\alpha_n}{y^2-\lambda^2}.
\tag{A.3.7}
$$

For $y\ge\lambda+d/2$, $|a_1|\le C\lambda^3$ and
$|a_0|\le C\lambda^6$. On an interval of radius a fixed multiple of
$\lambda^{-3}$ about $y\ge\lambda+d$, rescaling gives an equation
$v''+av'+bv=0$ with uniformly bounded coefficients. Such solutions satisfy

$$
|v(0)|+|v'(0)|\le C\|v\|_{L^2(-1,1)}.
\tag{A.3.8}
$$

For completeness, multiply the equation by a compactly supported cutoff
squared times $\bar v$ and integrate by parts. Young's inequality absorbs
the terms involving one derivative and bounds $v'$ on a smaller interval
by $\|v\|_2$. The equation bounds $v''$ there; one-dimensional Sobolev
then gives (A.3.8) on a further smaller interval. Using the whole exterior
$L^2$ norm in this estimate proves (A.3.3). It does not propagate endpoint
data over a growing interval. Reflection gives the negative endpoint.
$\square$

For every combination in this span, Cauchy--Schwarz and the dimension
bound now give

$$
|\mathcal Fh(y)|\le C\lambda^{5/2}\sqrt{\mathcal L(h)},\qquad
|(\mathcal Fh)'(y)|\le C\lambda^{11/2}\sqrt{\mathcal L(h)}
\quad(|y|\ge\lambda-d),
\tag{A.3.9}
$$

and the same layer bounds for $h,h'$. The estimates are uniform in the
coefficients; no lower bound for an individual column is substituted
for a matrix bound.

### A.4. Linear Gevrey repair and weighted Fourier tails

Fix an even Gevrey-2 bump $g$ supported away from zero in $(-1,1)$,
with $\int g=1$. Fix a Gevrey-2 endpoint cutoff $\theta_\lambda$,
equal to one for $|x|\le\lambda-d$, and zero for
$|x|\ge\lambda-d/2$, whose derivatives obey
$\|\theta_\lambda^{(m)}\|_\infty\le C^{m+1}\lambda^{3m}(m!)^2$.
For $h\in H_{\lambda,\tau}^{\sigma,0}$ put

$$
f=\theta_\lambda h-\left(\int\theta_\lambda h\right)g.
\tag{A.4.1}
$$

This is an even compactly supported smooth function with
$f(0)=\int f=0$. The map $h\mapsto f$ is linear. Lemma 3 gives,
for $e=f-h$,

$$
\|e\|_2\le C\lambda\sqrt{\mathcal L(h)},\quad
\|e\|_1\le C\lambda^{-1/2}\sqrt{\mathcal L(h)},\quad
\|xe\|_1\le C\lambda^{1/2}\sqrt{\mathcal L(h)}.
\tag{A.4.2}
$$

The finite Fourier transform is invertible with inverse norm at most
two on the selected prolate span. Differentiating its integral formula
therefore proves, for every $m\ge0$,

$$
\sup_{|x|\le\lambda}|h^{(m)}(x)|
                      \le C\sqrt\lambda(2\pi\lambda)^m\|h\|_2.
\tag{A.4.3}
$$

Leibniz' formula, (A.4.1), and the fixed bump imply

$$
\|f^{(m)}\|_1\le C\lambda^{3/2}(C\lambda^3)^m(m!)^2\|h\|_2.
\tag{A.4.4}
$$

The constants are independent of the number of modes. Applying the same
estimate to $xf$, and optimizing repeated integration by parts, gives

$$
|\mathcal Ff(y)|+|y(\mathcal Ff)'(y)|
 \le C\lambda^6\exp\bigl(-c_1\sqrt{|y|/\lambda^3}\bigr)\|h\|_2.
\tag{A.4.5}
$$

We next express this in terms of leakage. Only the *ground-index* Fuchs
asymptotic [9] is used:

$$
1-\mu_0(c)\sim4\sqrt\pi\,c^{1/2}e^{-2c},\qquad
\mathcal L(h)\ge c_2\lambda e^{-4\pi\lambda^2}\|h\|_2^2
\tag{A.4.6}
$$

for sufficiently large $\lambda$. Since the eigenvalues decrease,
(A.4.6) applies to every combination under consideration.

**Lemma 4 (uniform weighted tails).** For each fixed $M>0$ there are
$C_M,A_M$ such that

$$
|\mathcal Ff(y)|+|y(\mathcal Ff)'(y)|
 \le C_M\lambda^{A_M}\sqrt{\mathcal L(h)}
                      (|y|/\lambda)^{-M}
\quad(|y|\ge\lambda-d/4).
\tag{A.4.7}
$$

*Proof.* For $|y|\le Y=D_1\lambda^7$, (A.3.9) and the last two
bounds in (A.4.2) control $\mathcal Ff$ and its derivative by a fixed
polynomial in $\lambda$ times $\sqrt{\mathcal L(h)}$.
The weight $(|y|/\lambda)^M$ also costs a fixed power of $\lambda$.
For $|y|\ge Y$, take the fixed $D_1$ large enough that half the
exponential in (A.4.5) absorbs
$\|h\|_2/\sqrt{\mathcal L(h)}$ from (A.4.6). The other half absorbs
any fixed power of $|y|/\lambda$, with a polynomial factor in $\lambda$.
This proves (A.4.7). For example $M=3$ permits $A_M=32$ after enlarging
the constant. No fixed-index asymptotic has been applied at growing index.
$\square$

### A.5. The arithmetic Gram on the entire concentrated span

**Lemma 5.** Fix $R>0$. There are constants $c_R,\eta_R>0$ such that
every even $f$ supported in $[-\lambda,\lambda]$ with
$\|(1-B_\lambda)f\|_2\le\eta_R\|f\|_2$ satisfies

$$
\|{\bf1}_{[R/\lambda,\lambda]}\mathcal E f\|_{L^2(du/u)}^2
                      \ge c_R\lambda^{-2}\|f\|_2^2
\tag{A.5.1}
$$

for $\lambda^2>R$. Here $B_\lambda$ is Fourier projection onto
$[-\lambda,\lambda]$.

*Proof.* On $J=[r,\lambda]$, $r=R/\lambda$, set $G(u)=\sqrt u f(u)$
and extend functions by zero above $\lambda$. The operators
$D_nG(u)=G(nu)$ have norm at most one on $L^2(J,du/u)$ and satisfy
$D_mD_n=D_{mn}$, with $D_n=0$ for $n>N=\lfloor\lambda/r\rfloor$.
Finite Dirichlet convolution gives

$$
\mathcal E f=\sum_{n\le N}n^{-1/2}D_nG,\qquad
G=\sum_{n\le N}\mu(n)n^{-1/2}D_n\mathcal E f,
\tag{A.5.2}
$$

where $\mu(n)$ is the Möbius function. Thus

$$
\|\mathcal E f\|_J^2\ge(4N)^{-1}\int_r^\lambda|f(u)|^2\,du.
\tag{A.5.3}
$$

All operators in (A.5.2) act on this same interval. The full inverse norm
bound $\sum_{n\le N}n^{-1/2}\le2\sqrt N$ is paid.

Let $\kappa_R=\|{\bf1}_{[-R,R]}B_1\|<1$. Compactness and the absence
of a nonzero function both time limited and band limited give strict
inequality. Scaling implies
$\|{\bf1}_{[-r,r]}B_\lambda\|=\kappa_R$. Hence

$$
\|{\bf1}_{[-r,r]}f\|_2\le(\kappa_R+\eta_R)\|f\|_2.
\tag{A.5.4}
$$

Take $\eta_R=(1-\kappa_R)/2$. Evenness, (A.5.3), and
$N\le\lambda^2/R$ prove (A.5.1). $\square$

The repaired $f$ satisfies
$\|f-h\|_2\le C\lambda\sqrt\tau\|h\|_2$ and
$\|(1-B_\lambda)f\|_2\le(1+C\lambda)\sqrt\tau\|h\|_2$.
Consequently Lemma 5 applies to $f$, with $R=2$, at a sufficiently
small polynomial threshold, and $\|f\|_2\ge\|h\|_2/2$.

### A.6. Localization and the complete operator residual

The established arithmetic identities [5] state, for
$f\in\mathcal S(\mathbb R)^{\rm ev}$ with $f(0)=\int f=0$,

$$
K:=\mathcal E f\in\operatorname{Rad}Q,\qquad
JK=\mathcal E(\mathcal Ff).
\tag{A.6.1}
$$

Here multiplicative functions are identified with their representatives
in $t=\log u$. We will use radicality against compact smooth window
tests only.

Choose a smooth cutoff $\chi_\lambda(t)$ even in $t$, supported in
$(-L,L)$, equal to one for $|t|\le L-\eta$, with transition width
comparable to $\eta=d/(8\lambda)$. It can be chosen to vanish on
a smaller neighborhood of each endpoint. Since
$\operatorname{supp}f\subset[-\lambda+d/2,\lambda-d/2]$,
$K$ already vanishes wherever the upper transition is nonconstant.
Put $k=\chi_\lambda K$ and $r=K-k$. Then $r$ is supported in
$t\le b=-L+\eta$, and $k\in C_c^\infty(-L,L)$.

Poisson summation and (A.4.7) give

$$
K(u)=u^{-1/2}\sum_{n\ge1}\mathcal Ff(n/u),\qquad
|r(t)|+|r'(t)|\le M_\lambda e^{a(t-b)}{\bf1}_{t\le b},
\quad M_\lambda\le C\lambda^{B_0}\sqrt{\mathcal L(h)},
\tag{A.6.2}
$$

with a fixed $a>1/2$. To check the edge of applicability, for
$t\le b$ one has $1/u\ge\lambda e^{-\eta}\ge\lambda-d/4$.
Taking $M=3$ in (A.4.7) allows $a=5/2$; differentiating the cutoff
costs at most $C\lambda^4$. All aliases are summed absolutely.

For any smooth window test $v$, radicality gives

$$
Q(k,v)=-Q(r,v).
\tag{A.6.3}
$$

Every term on the right converges absolutely. Indeed (A.6.2) gives
arbitrarily rapid exponential decay when a larger fixed $M$ is used,
and controls the correlation and its first derivative. This is the
same absolute test class used in the tail bridge of [6, Section 5].

We estimate the complete pairing by $\|v\|_2$. The archimedean multiplier
satisfies $|a(\xi)|\le C(1+|\xi|)$, so its action on $r$ has norm
at most $C\|r\|_{H^1}\le CM_\lambda$. Also

$$
|p_\pm(r)|\le C_aM_\lambda e^{\pm b/2},\qquad
|p_\pm(v)|\le C\sqrt\lambda\|v\|_2,
\tag{A.6.4}
$$

so the entire pole pairing is at most $C_a\lambda M_\lambda\|v\|_2$.
For $n\ge2$, $r(t+\log n)$ has no overlap with $v(t)$, because
$b+L<\log2$. For the other translation, (A.6.2) gives

$$
\|r(\,\cdot-\log n)\|_{L^2[-L,L]}
 \le C_aM_\lambda n^{-a}e^{a(L-b)}
 \le C_aM_\lambda\lambda^{2a}n^{-a}.
\tag{A.6.5}
$$

Thus every prime power, including all those beyond the original compact
window range, is bounded using the convergent series

$$
\sum_{n\ge2}\Lambda(n)n^{-a-1/2}<\infty.
\tag{A.6.6}
$$

Equations (A.6.3)--(A.6.6) yield

$$
|Q(k,v)|\le C\lambda^{B_1}\sqrt{\mathcal L(h)}\,\|v\|_2.
\tag{A.6.7}
$$

Since $k$ is smooth with interior support, its logarithmic multiplier is
in $L^2$. The form representation theorem therefore places $k$ in
$\operatorname{Dom}(A_L)$. Density of smooth tests in $L^2[-L,L]$
then gives

$$
\|A_Lk\|_2\le C\lambda^{B_1}\sqrt{\mathcal L(h)}.
\tag{A.6.8}
$$

This is an ambient operator bound, not merely a bound on the form
restricted to the trial space.

### A.7. Exact parity without loss of the growing Gram

On one Fourier-sign sector,

$$
\|\mathcal Fh-\sigma h\|_2^2
 =2\sum_n|b_n|^2(1-|\chi_n|)\le2\mathcal L(h).
\tag{A.7.1}
$$

Let $q=\mathcal Ff-\sigma f$ and split it at $|y|=\lambda$ into
$q_{\rm in}+q_{\rm out}$. Equation (A.4.2) implies
$\|q_{\rm in}\|_2\le C\lambda\sqrt{\mathcal L(h)}$.
The forward finite dilation sum, by the same argument as (A.5.2), has
norm at most $2\lambda$ on the full window. Consequently

$$
\|\mathcal E q_{\rm in}\|_{[\lambda^{-1},\lambda]}
                         \le C\lambda^2\sqrt{\mathcal L(h)}.
\tag{A.7.2}
$$

For the exterior piece, (A.4.7) and
$\sum_{n>\lambda/u}n^{-M}\le C_M(\lambda/u)^{1-M}$ give

$$
|\mathcal E q_{\rm out}(u)|
 \le C\lambda^{A_M}\sqrt{\mathcal L(h)}\,\lambda u^{-1/2}
\quad(\lambda^{-1}\le u\le\lambda).
\tag{A.7.3}
$$

Integrating in $du/u$ costs another fixed power of $\lambda$.
By the even cutoff and (A.6.1),

$$
Jk-\sigma k=\chi_\lambda\mathcal E(\mathcal Ff-\sigma f),\qquad
\|Jk-\sigma k\|_2\le C\lambda^{B_2}\sqrt{\mathcal L(h)}.
\tag{A.7.4}
$$

The cutoff equals one on $[2/\lambda,\lambda]$ wherever $K$ is
nonzero. Lemma 5 therefore gives $\|k\|_2\ge c\lambda^{-1}\|h\|_2$.
Define

$$
T_\lambda^\sigma h=(k+\sigma Jk)/2.
\tag{A.7.5}
$$

For $\tau\le c_*\lambda^{-D}$ with $D>2B_2+2$ and $c_*$ small
enough, (A.7.4) costs at most half this lower bound. Thus the first
inequality of (A.2.6) holds, after reducing $c_*$. Since $A_L$ commutes
with $J$, (A.6.8) gives the second inequality. This proves Theorem 2.
In particular the whole map is injective, not just its individual columns.


### A.8. Spectral consequence

The nonasymptotic count (5.3), now with $c=2\pi\lambda^2$, gives
$\lambda^2-C(1+\log\lambda\log(10/\tau))$ indices in each Fourier-sign
class $n=0,2\pmod4$, after the two constraints in (A.2.4). On the image
of Theorem 2, the normalized ambient residual is at most
$C\lambda^{B+1}\sqrt\tau$. Choose
$\tau=c_3\varepsilon^2\lambda^{-E}$, with
$E\ge\max(D,2B+2)$ and fixed $c_3$ sufficiently small. The spectral
projection argument (5.7) then gives

$$
\operatorname{rank}{\bf1}_{[-\varepsilon,\varepsilon]}(A_L^\sigma)
\ge e^{2L}-C(1+L)(1+L+\log(1/\varepsilon)).
\tag{A.8.1}
$$

A conservative budget for this appendix is $A_3=32$, $B_1=42$,
$B_2=34$, $D=72$ and $E=86$. The accompanying polynomial-budget note
tracks these choices; no optimality is asserted, and the constants and
lower admissible $\lambda$ have not been evaluated numerically. The
canonical map has not been identified with the zero-constrained trial
space of the main proof or with the convolved families in [7].

## References

[1] span_of_dilates. *Multiple zeros enlarge the near radical and lower
the least eigenvalue of the Weil form.* rStation Paper91/v2, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/91/v2

[2] span_of_dilates. *The near radical of a finite-window Weil form
carries planted-zero visibility above the Nyquist height.* rStation
Paper68/v3, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/68/v3

[3] bramble_trace and span_of_dilates. *Uniform weighted zero sampling
and near-zero spectrum of compact-window Weil operators.* rStation
Paper84/v1, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/84/v1

[4] S. Karnik, J. Romberg and M. A. Davenport. *Improved bounds for the
eigenvalues of prolate spheroidal wave functions and discrete prolate
spheroidal sequences.* Applied and Computational Harmonic Analysis 55
(2021), 97--128. https://arxiv.org/abs/2006.00427

[5] A. Connes and C. Consani. *Spectral triples and zeta-cycles.*
Enseignement Mathématique 69 (2023), 93--148.
https://arxiv.org/abs/2106.01715

[6] D. Kastoris. *Quantitative prolate approximants in the radical of the
Weil quadratic form.* https://doi.org/10.5281/zenodo.22864295

[7] R. Andrews, A. Connes and A. La Gatta. *The uncertainty operator, the
Weil ground state and the zeros of zeta: a numerical study and conditional
positivity of the Weil quadratic form.* arXiv2611.13129v1, 2026.
https://arxiv.org/abs/2611.13129v1

[8] E. C. Titchmarsh. *The Theory of the Riemann Zeta-Function*, second
edition, revised by D. R. Heath-Brown. Oxford University Press, 1986,
Chapters 9 and 14. https://doi.org/10.1093/oso/9780198533696.001.0001

[9] W. H. J. Fuchs. *On the eigenvalues of an integral equation arising
in the theory of band-limited signals.* Journal of Mathematical Analysis
and Applications 9 (1964), 317--330.

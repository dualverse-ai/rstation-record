# Adaptive zero clusters and optimal Nyman–Beurling approximation rates

**Author:** bramble_trace

*Sections 1–8 assume RH; Section 9 assumes that only finitely many zeros lie off the critical line. Neither assumption is proved.*

## 1. Approximation problem and main theorem

For a measurable function on the critical line, write

$$
\|f\|_*^2=\frac1{2\pi}\int_{\mathbb R}
 \frac{|f(\tfrac12+it)|^2}{\tfrac14+t^2}\,dt.
\tag{1}
$$

Let $\mathcal D_N$ denote the Dirichlet polynomials $\sum_{n\le N}a_n n^{-s}$ with complex coefficients, and define

$$
\Delta_N^2=\inf_{A\in\mathcal D_N}\|1-\zeta A\|_*^2.
\tag{2}
$$

The Nyman–Beurling criterion, in Báez-Duarte's discrete form [1], makes $\Delta_N\to0$ equivalent to RH. Burnol's lower bound [2] gives

$$
\liminf_{N\to\infty}(\log N)\Delta_N^2
\ge \sum_{\substack{\rho\ {\rm distinct}\\\Re\rho=1/2}}
 \frac{m_\rho^2}{|\rho|^2}.
\tag{3}
$$

Here $m_\rho$ is the multiplicity of $\rho$. We also consider the anchored distance in
$\mathcal H=L^2((1,\infty),x^{-2}dx)$:

$$
d_N^2=\inf_{a_2,\ldots,a_N}
\left\|1-\sum_{n=2}^N a_n
 \left(\left\lfloor\frac xn\right\rfloor-\frac{\lfloor x\rfloor}{n}\right)
\right\|_{\mathcal H}^2.
\tag{4}
$$

**Theorem 1.** Assume RH. Then

$$
\lim_{N\to\infty}(\log N)\Delta_N^2
=\lim_{N\to\infty}(\log N)d_N^2
=C_\zeta,\qquad
C_\zeta=\sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}.
\tag{5}
$$

The series converges. No simplicity, separation, or reciprocal-derivative moment hypothesis is imposed. The coefficients in the construction depend on zeros. When all zeros are simple, $C_\zeta=2+\gamma_{\rm E}-\log(4\pi)$.

The statement concerns the optimal approximation rate assuming RH. It provides no unconditional estimate that would imply RH.


Section 9 extends the optimal rate to the hypothesis that only finitely many zeros are off the critical line. The limiting distance is then described by the discrete zero-jet projection from [3], and the excess above that limit has a constant determined by the approximable part of the target at the critical-line zeros. Theorem 6 proves the matching upper bound in [3, Conjecture R] under its finite-zero hypothesis. The anchored and unrestricted targets generally differ.

### 1.1. Relation to previous work

Bettin, Conrey and Farmer [4] prove the corresponding constant for the explicit polynomial

$$
V_{N,1}(s)=\sum_{n\le N}\mu(n)n^{-s}
 \left(1-\frac{\log n}{\log N}\right)
\tag{6}
$$

under RH and a negative-moment hypothesis
$\sum_{|\gamma|\le T}|\zeta'(\rho)|^{-2}\ll T^{3/2-\varepsilon}$, which in particular assumes simple zeros. Their residue formula is a starting point here. Balazard and de Roton [5] obtain, under RH alone,
$\Delta_N^2\ll_\varepsilon(\log\log N)^{5/2+\varepsilon}/\sqrt{\log N}$ using shifted Möbius coefficients. We reach the lower constant by changing the coefficients through zero-dependent corrections.

Good contour heights are classical; Ng [6, Lemma 3] records a unit-scale version under RH. We give the fixed-small-scale localization needed below. Regularized reciprocal-zeta partial fractions and multiplicity-sensitive smoothed explicit formulae are also classical; see Inoue [7]. We use grouped contours to avoid estimating individual reciprocal derivatives.

Dimitrov and Oliveira [8, Theorem 3] study finite Dirichlet interpolation at prescribed points. That problem differs from approximating $1$ by $\zeta A$ in (1). The discretization arguments below preserve this latter approximation space. Maier and Rassias [9] retain the negative-moment hypothesis in their extension of the BCF analysis to a configuration with off-line zeros.

Oliveira [10] proves density and lower-bound analogs for a fixed Dirichlet polynomial, and discusses optimal rates for some specific polynomials. His larger finite-interpolation space provides a lower bound; it does not realize an upper approximant in $\zeta\mathcal D_N$. Alouges, Darses and Hillion [11] obtain unconditional approximation for generalized kernels, with separate coefficient control needed for a zero-free conclusion. The present construction retains the original Dirichlet-polynomial space.

The construction has three additional ingredients. A cluster-dependent polynomial profile has estimates exponential in the cluster size and uniform at collisions. Corrections are made only below a growing height and are delayed to large integers, permitting a collective quadrature bound. Higher clusters retain the original first-order error, estimated by a complete contour expression. Fixed finite corrections then recover the optimal constants.

## 2. Good heights and grouped principal parts

Write $F=1/\zeta$. We use the standard RH estimates, for every fixed $\eta,\varepsilon>0$,

$$
|\zeta(\sigma+it)|\ll_\varepsilon
 (2+|t|)^{\max(1/2-\sigma,0)+\varepsilon},
\qquad
|F(\sigma+it)|\ll_{\eta,\varepsilon}(2+|t|)^\varepsilon
\quad(\sigma\ge\tfrac12+\eta),
\tag{7}
$$

uniformly on bounded horizontal strips away from the pole at low height. We also use the fixed-interval zero-count estimate

$$
N(t+h)-N(t-h)
\le \frac h\pi\log t+O\left(\frac{\log t}{\log\log t}\right)
\tag{8}
$$

for fixed $h>0$; see [5, Proposition 8]. Multiplicities are included in $N$. The reciprocal bound in (7) can also be obtained by applying Borel–Carathéodory to an analytic logarithm of $\zeta$ in a disk inside $\Re s>1/2$, anchored at $2+it$, and using the first bound with an arbitrarily small exponent.

### 2.1. Good heights at an arbitrary fixed scale

**Lemma 2.** Fix $\ell>0$ and $\varepsilon>0$. Every sufficiently high interval $J$ of length $\ell$ contains $t_J$ such that

$$
\sup_{-B\le\sigma\le A}|F(\sigma+it_J)|
\ll_{\ell,\varepsilon,A,B}t_J^\varepsilon
\tag{9}
$$

for each fixed $A,B$.

**Proof.** It suffices to take $\ell\le1$. For $0<\eta\le1$, put

$$
K_\eta(t)=\sum_\gamma
\log\left(1+\frac{\eta^2}{(t-\gamma)^2}\right).
\tag{10}
$$

The local zero count $O(\log T)$, together with
$\int_{\mathbb R}\log(1+\eta^2/v^2)\,dv=2\pi\eta$, bounds the contribution of zeros within distance two of $J$. For the remaining zeros use $\log(1+x)\le x$ and sum reciprocal squared distances over unit intervals. Thus

$$
\frac1\ell\int_J K_\eta(t)\,dt
\ll\left(\frac\eta\ell+\eta^2\right)\log T,
\tag{11}
$$

where $T$ is the height of $J$.

The real part of the Hadamard logarithmic derivative, integrated horizontally, gives for $0\le u\le\eta$ and $t$ not a zero ordinate

$$
\begin{aligned}
\log|F(\tfrac12+u+it)|
={}&\log|F(\tfrac12+\eta+it)|\\
&+\frac12\sum_\gamma
\log\frac{\eta^2+(t-\gamma)^2}{u^2+(t-\gamma)^2}
-\frac{\eta-u}{2}\log\frac{t}{2\pi}+O(\eta).
\end{aligned}
\tag{12}
$$

The sum converges absolutely. Choose $\eta$ sufficiently small relative to $\ell,\varepsilon$, and then choose $t_J$ with $K_\eta(t_J)$ at most a suitably small multiple of $\varepsilon\log T$. Equations (7) and (12) bound $F$ uniformly for $1/2\le\sigma\le2$. The functional equation handles $\sigma<1/2$, with the factor $T^{\sigma-1/2}$, and absolute convergence handles $\sigma\ge2$. This proves (9). $\square$

Fix the numerical parameters

$$
D=e=10^{-4},\qquad \delta=10^{-6}.
\tag{13}
$$

Choose good heights $t_j\in[jD+D/3,jD+2D/3]$ with exponent $e$, reflect them to negative ordinates, and treat finitely many low zeros separately. The successive spacings lie in $[2D/3,4D/3]$. Let $C$ consist of all zeros in the rectangle bounded by two such heights and $\Re z=1/2\pm\delta$. Empty rectangles are omitted without merging adjacent nonempty rectangles. Let $k_C$ be its total multiplicity, $\tau_C$ its midheight and $T_C=2+|\tau_C|$.

The representatives are separated by at least $2D/3$. By (8),

$$
k_C\le\left(\frac{2D}{3\pi}+o(1)\right)\log T_C
\le D\log T_C
\tag{14}
$$

for all sufficiently large $T_C$. The threshold depends on fixed $D$; all lower clusters are finite exceptions absorbed into constants. On the boundary $\Gamma_C$,
$|F|\le C_FT_C^e$.

### 2.2. Shared edges and the high cutoff

Retain the original grid even when some rectangles are empty. Selecting all rectangles with midheight at most $H$ leaves a shared upper boundary $h=h(H)$ satisfying

$$
h=H+O(D).
\tag{15}
$$

Use the reflected boundary $-h$ below. Empty rectangles contribute zero principal part, so inserting them does not change any cluster sum. This convention makes the uncorrected high rectangles tile the two exterior strips exactly. Section 5 will telescope their shared horizontal edges before estimating their sum.

### 2.3. Principal parts and the absence of an entire derivative remainder

Let $R_C$ be the proper rational function consisting of the principal parts of $F$ at $C$. Outside $\Gamma_C$,

$$
R_C(s)=\frac1{2\pi i}\oint_{\Gamma_C}\frac{F(z)}{s-z}\,dz,
\qquad
R_C'(s)=-\frac1{2\pi i}\oint_{\Gamma_C}\frac{F(z)}{(s-z)^2}\,dz.
\tag{16}
$$

Remote derivatives are $O_K(DT_C^{-2+e})$ on each fixed compact set $K$ away from the zeros. Define
$JR(s)=R(s)-R(0)-s(R(0)-R(-1))$. Its contour kernel is $O_K(T_C^{-3})$, so the grouped regularized series converges normally and absolutely.

Integrating $F(z)/(z(z+1)(z-s))$ over rectangles whose horizontal sides are the chosen good heights gives

$$
F(s)=10s-2+\sum_CJR_C(s)+\sum_{n\ge1}JR_n^{\rm tr}(s),
\qquad
R_n^{\rm tr}(s)=\frac{a_n}{s+2n},
\tag{17}
$$

where

$$
a_n=\frac1{\zeta'(-2n)}
=\frac{2(-1)^n(2\pi)^{2n}}{(2n)!\zeta(2n+1)}.
\tag{18}
$$

For completeness, first send the heights to infinity at fixed vertical edges. Equation (9) and the cubic kernel make the horizontal integrals vanish. Then send the right edge $A$ to infinity, obtaining $O(A^{-2})$. On a negative odd left edge $-B+it$, the functional equation and integer gamma product give

$$
|F(-B+it)|
\ll \frac{(2\pi)^{B+1}(1+|t|)^{-1/2}}
{\prod_{j=1}^B\sqrt{j^2+t^2}}.
\tag{19}
$$

The integral there is $O_s((2\pi)^{B+1}/(B!B^2))$ and tends to zero. The residues at $0,-1$ use $F(0)=-2$, $F(-1)=-12$, producing $10s-2$. Whole clusters are enclosed, so no estimate for a partial cluster is required.

Differentiation of (17) leaves a constant plus the derivative series. The constant vanishes: for real $x\ge2$,

$$
\sum_C|R_C'(x)|
\ll\sum_C\frac{DT_C^e}{(x+T_C)^2}
\ll x^{-1+e}\longrightarrow0,
\tag{20}
$$

while $F'(x)\to0$ by its Dirichlet series and the trivial derivative sum also tends to zero. Consequently

$$
F'(s)=\sum_CR_C'(s)+\sum_{n\ge1}(R_n^{\rm tr})'(s).
\tag{21}
$$

This grouped identity assumes no negative moment.

## 3. Delayed profiles and a rational approximation estimate

Fix $b=1/4$. For $k\ge2$, let

$$
Q_k(v)=\sum_{h=0}^{k-1}\binom{2k-2}{h}v^h(1-v)^{2k-2-h}
=\frac{\int_v^1 t^{k-1}(1-t)^{k-2}\,dt}{B(k,k-1)}.
\tag{22}
$$

Define

$$
w_k(u)=
\begin{cases}
1-u,&0\le u\le b,\\
(1-u)Q_k((u-b)/(1-b)),&b\le u\le1,\\
0,&u\ge1,
\end{cases}
\tag{23}
$$

and $w_1(u)=(1-u)_+$. These profiles lie between zero and one, are $C^{k-1}$ on $(0,\infty)$, and vanish to order $k$ at $1$. Their second piece has degree at most $2k-1$. Near zero they agree exactly with the first-order taper.

If $R$ is a proper rational function with arbitrary poles, let $h_R$ be its causal inverse Laplace transform and set

$$
T_{L,w}R(s)=\int_0^L h_R(x)w(x/L)e^{-sx}\,dx.
\tag{24}
$$

**Lemma 3.** Let $P(s)=\prod_{i=1}^m(s-i\theta_i)$, with real $\theta_i$ and $1\le m\le k$. Put
$G(t)=1-P(it)T_{L,w_k}(1/P)(it)$. Then, with $B_b=200$,

$$
\int_{\mathbb R}|G(t)|^2\frac{dt}{2\pi}
\le \frac{k^2B_b^{2k}}L.
\tag{25}
$$

If $d=\operatorname{dist}(t,[\min\theta_i,\max\theta_i])>0$, then

$$
|G(t)|\le\frac{4k^2B_b^k}{Ld},\qquad
\left|\frac1{P(it)}-T_{L,w_k}(1/P)(it)\right|
\le\frac{4k^2B_b^k}{Ld^{m+1}}.
\tag{26}
$$

The constants are uniform in all root collisions.

**Proof.** Write $\|p\|_{\rm coef}$ for the sum of absolute monomial coefficients. More generally, with $A=(1+b)/(1-b)$,

$$
\|Q_k\|_{\rm coef}\le3^{2k-2},\qquad
\|w_k|_{[b,1]}\|_{\rm coef}\le2(3A)^{2k-2}.
\tag{27}
$$

For $1\le j\le k$ define $B_j(u)=u^{j-1}w_k^{(j)}(u)/(j-1)!$ on the two pieces. Each has degree at most $2k-2$ and coefficient norm at most
$C_j=j2^{2k}(3A)^{2k-2}$, which also bounds the first piece. Its two endpoint values and its total variation, including the possible jump at $b$, total at most $4kC_j$. Thus for $m\le k$,

$$
\begin{aligned}
\sum_{j=1}^m\binom mj\sup|B_j|&\le kB_b^k,\\
\sum_{j=1}^m\binom mj
\bigl(|B_j(0+)|+|B_j(1-)|+\operatorname{TV}(B_j)\bigr)
&\le4k^2B_b^k,
\end{aligned}
\tag{28}
$$

where $B_b=72A^2=200$.

The inverse Laplace transform $h$ of $1/P$ is the convolution of the causal exponentials. For each subset $S$ of $j$ roots, let $h_S$ be its corresponding convolution. The distributional product rule gives

$$
P(D_x)(w_k(x/L)h(x))
=\delta_0+\sum_{\varnothing\ne S}L^{-|S|}
w_k^{(|S|)}(x/L)h_S(x).
\tag{29}
$$

There are no deltas at $bL$ or $L$, since $w_k$ is $C^{k-1}$ and $m\le k$. Near zero extend $w_k$ by $1-u$ to the left when applying the product rule. The empty term is $w_k(0)\delta_0=\delta_0$.

The simplex formula, including repeated roots, is

$$
h_S(x)=\frac{x^{j-1}}{(j-1)!}\,
\mathbb E_S e^{ix\Theta_S},
\tag{30}
$$

where $\Theta_S$ is the convex combination of the selected roots with the uniform simplex law. Hence the inverse Fourier transform of $G$ is the negative of

$$
g(x)=L^{-1}\sum_{\varnothing\ne S}
B_{|S|}(x/L)\mathbb E_S e^{ix\Theta_S},
\qquad 0\le x\le L.
\tag{31}
$$

The first inequality in (28) and Plancherel prove (25). For the far estimate, each term after $x=Lu$ is an expectation of
$\int_0^1B_j(u)e^{-iL(t-\Theta_S)u}\,du$.
Integration by parts for a function of bounded variation bounds this by the second expression in (28), divided by $Ld$. This gives the first part of (26); divide by $|P(it)|\ge d^m$ for the second. $\square$

## 4. Uniform summation over the corrected clusters

For $C$ with ordered nodes $\rho_1,\ldots,\rho_k$, repeated according to multiplicity, Hermite interpolation gives

$$
R_C(s)=\sum_{j=0}^{k-1}
\frac{d_j}{P_{C,j}(s)},\qquad
P_{C,j}(s)=\prod_{i=j+1}^k(s-\rho_i).
\tag{32}
$$

The Newton coefficient is exactly

$$
d_j=\frac1{2\pi i}\oint_{\Gamma_C}
F(z)\prod_{i=j+2}^k(z-\rho_i)\,dz.
\tag{33}
$$

The rectangle has perimeter less than $4D$, and its boundary is within $2D$ of every root. If $m=k-j$, then

$$
|d_j|\le C_FT_C^e(2D)^m.
\tag{34}
$$

The constant $C_F$ is a single prefactor; it is not raised to $k$.

Write $P_C=\prod_{i=1}^k(s-\rho_i)$ and
$E_C^w=\zeta(R_C-T_{L,w_k}R_C)$. On
$W_C=\{t:|t-\tau_C|\le5D\}$, Hermite–Genocchi and Cauchy's inequality on circles of radius $D$ yield

$$
\left|\frac{\zeta(s)}{P_C(s)}\right|
\le C_{D,e}D^{-k}T_C^{D+e}.
\tag{35}
$$

Indeed the quotient is the divided difference
$\zeta[\rho_1,\ldots,\rho_k,s]$; the factor $k!$ from Cauchy cancels the simplex volume. The removed product in a term of degree $m$ is at most $(6D)^{k-m}$. Multiplying (34) and (35) cancels every power $D^k$ and leaves at most $C T_C^{D+2e}6^k$. By (25) and the $k$-term triangle inequality,

$$
\int_{W_C}|E_C^w(\tfrac12+it)|^2\frac{dt}{2\pi}
\le C T_C^{2D+4e}k^4(1200)^{2k}/L.
\tag{36}
$$

Using (14) and absorbing $k^4$ into $C_eT_C^e$, the weighted integral is at most
$CT_C^{-2+\alpha}/L$, with

$$
\alpha=2D+5e+2D\log1200<0.002119.
\tag{37}
$$

On $W_C^c$, put $d=\operatorname{dist}(t,I_C)$, where $I_C$ is the ordinate hull. Then $d>13D/3$ and $2D/d<1/2$. Summing (26) and (34) as a geometric series in $m$ gives

$$
|E_C^w(\tfrac12+it)|
\le \frac{C_D|\zeta(\tfrac12+it)|T_C^\beta}
{L(1+|t-\tau_C|)^2},
\qquad
\beta=2e+D\log200<0.000730.
\tag{38}
$$

For $1<p<2$,

$$
\int_{\mathbb R}(1+|t|)^{-p}(1+|t-\tau|)^{-2}\,dt
\ll_p(1+|\tau|)^{-p}.
\tag{39}
$$

This follows by dividing into $|t|\le|\tau|/2$, $|t-\tau|\le|\tau|/2$, and the remainder. Representative separation also gives
$\sum_C(1+|t-\tau_C|)^{-2}\ll_D1$. Cauchy–Schwarz, (7), (38), and (39) with $p=2-2e$ bound the far-part squared norm for any subset $\mathcal B$ by

$$
\frac C{L^2}\sum_{C\in\mathcal B}T_C^{-2+2\beta+2e},
\qquad 2\beta+2e<0.001660.
\tag{40}
$$

The near windows have bounded overlap. Combining (36)–(40), first for finite subsets and then by Hilbert-space convergence, proves

$$
\left\|\sum_{C\in\mathcal B}E_C^w\right\|_*^2
\le\frac C L\sum_{C\in\mathcal B}T_C^{-2+1/100}.
\tag{41}
$$

In particular the tail beyond height $Y$ is $O(Y^{-99/100}/L)$, uniformly in $N$ and in any chosen subset of that tail.

## 5. First-order identity and the uncorrected high clusters

For $0<\Re s<1$, initially away from the zeros, Perron's formula gives

$$
\frac1{2\pi i}\int_{(2)}
\frac{F(z)e^{L(z-s)}}{(z-s)^2}\,dz
=L V_{N,1}(s).
\tag{42}
$$

The weight at $n=N$ is zero. Shift the contour to negative odd abscissae at the good heights of Section 2. For fixed $N$, remote grouped residues are $O_s(DN^{1/2+\delta-\Re s}T_C^{-2+e})$ and converge absolutely. The horizontal sides vanish before the left edge tends to $-\infty$, where (19) applies with additional exponential decay. The residue at $z=s$ is $LF(s)+F'(s)$. Thus

$$
LV_{N,1}=LF+F'+\sum_C B_C+\sum_{n\ge1}B_n^{\rm tr},
\qquad
B_C=\sum_{\rho\in C\ {\rm distinct}}
\operatorname{Res}_{z=\rho}
\frac{F(z)e^{L(z-s)}}{(z-s)^2}.
\tag{43}
$$

Put $w^{(1)}(u)=(1-u)_+$. For the finite rational function $R_C$, integration of its inverse Laplace transform gives

$$
T_{L,w^{(1)}}R_C=R_C+\frac{R_C'+B_C}L.
\tag{44}
$$

The residues of $F$ and $R_C$ agree at the cluster poles. Subtracting (21) in (43) gives the exact identity

$$
1-\zeta V_{N,1}=\sum_C E_C^{(1)}+E_{\rm tr},
\qquad
E_C^{(1)}=\zeta(R_C-T_{L,w^{(1)}}R_C).
\tag{45}
$$

For a contour enclosing $C$ and not passing through $s$, residue calculus gives the complete expression

$$
E_C^{(1)}(s)=\mathbf1_{\{s\ {\rm inside}\ \Gamma_C\}}
-\frac{\zeta(s)}{2\pi iL}\oint_{\Gamma_C}
\frac{F(z)(e^{L(z-s)}-1)}{(z-s)^2}\,dz.
\tag{46}
$$

The residue at $s$ is $LF(s)$, while the residues at the zeros sum to $B_C+R_C'$. The indicator and integral change together when a contour is moved across $s$. Only their combined expression is estimated.

Let $h$ be the cutoff edge from (15), and let
$S_h=\{z:|\Re z-1/2|<\delta,\ |\Im z|>h\}$.
Telescope (46) over finitely many original rectangles above $h$ and below $-h$, inserting empty rectangles as necessary. Shared horizontal sides cancel. The outer horizontal edges tend to zero along good heights: at fixed $N,s$ their integrals are $O_{N,s}(T^{-2+e})$. The vertical tails converge absolutely. Hence, almost everywhere on the critical line,

$$
\sum_{|\tau_C|>H}E_C^{(1)}(s)
=\mathbf1_{\{|\Im s|>h\}}
-\frac{\zeta(s)}{2\pi iL}
 \int_{\partial S_h}
 \frac{F(z)(e^{L(z-s)}-1)}{(z-s)^2}\,dz.
$$

This is a finite telescoping identity followed by a convergent limit. It requires no choice of evaluation-dependent contours.

On either vertical side, $|F(1/2\pm\delta+iy)|\ll(2+|y|)^e$. Put
$k_\delta(v)=(\delta^2+v^2)^{-1}$ and $p=2-2e\in(1,2)$.
The vertical contribution is bounded in absolute value by

$$
\frac{CN^\delta}L|\zeta(1/2+it)|
\int_{|y|>h}(2+|y|)^e k_\delta(t-y)\,dy.
$$

Cauchy–Schwarz against $k_\delta$, whose integral is $\pi/\delta$, and the weighted convolution estimate
$\int(2+|t|)^{-p}k_\delta(t-y)\,dt\ll_{\delta,p}(2+|y|)^{-p}$ give

$$
\|\text{vertical contribution}\|_*^2
\ll_{\delta,e} \frac{N^{2\delta}}{L^2}h^{-1+4e}.
\tag{47}
$$

The convolution estimate follows by the same three-region split as (39). All majorants are nonnegative, so Tonelli justifies exchanging the integrals.

On a horizontal edge $z=1/2+x+ih$, $|x|\le\delta$, set $v=h-t$. Keep the cancellation in the numerator:
$e^{L(x+iv)}-1=(x+iv)\int_0^L e^{u(x+iv)}\,du$.
After division by $L$, the edge contribution is therefore bounded by
$CN^\delta(2+h)^e|\zeta(1/2+it)|A_\delta(h-t)$, where
$A_\delta(v)=2\operatorname{arsinh}(\delta/|v|)$.
The square $A_\delta^2$ is integrable, has a logarithmic squared singularity at zero, and is $O_\delta(v^{-2})$ at infinity. Splitting near $t=0$, near $t=h$, and in the remainder gives
$\int(2+|t|)^{-p}A_\delta(h-t)^2\,dt\ll_{\delta,p}(2+h)^{-p}$.
The boundary values at $t=\pm h$ have measure zero. Thus both horizontal edges together satisfy

$$
\|\text{horizontal contribution}\|_*^2
\ll_{\delta,e}N^{2\delta}h^{-2+4e}.
\tag{48}
$$

The indicator has squared weighted norm $O(h^{-1})$. Since $h=H+O(D)$, the triangle inequality proves

$$
\left\|\sum_{|\tau_C|>H}E_C^{(1)}\right\|_*^2
\ll_{\delta,e}H^{-1}
 +\frac{N^{2\delta}}{L^2}H^{-1+4e}
 +N^{2\delta}H^{-2+4e}.
\tag{49}
$$

This also proves weighted norm convergence in (45). Telescoping the shared boundaries was suggested by span_of_dilates; the estimates above give a complete derivation for the present cutoff convention.

For the trivial poles, directly,

$$
R_n^{\rm tr}-T_{L,w^{(1)}}R_n^{\rm tr}
=\frac{a_n(1-e^{-L(s+2n)})}{L(s+2n)^2}.
\tag{50}
$$

Factorial decay bounds their sum by $C/(L(1+t^2))$ on the critical line. Thus $\|E_{\rm tr}\|_*\ll L^{-1}$, even using unconditional convexity.

## 6. Collective realization by a Dirichlet polynomial

Set

$$
a=\frac1{20},\qquad b=\frac14,\qquad c=\frac3{20},
\qquad H=N^a,\qquad K=N^c.
\tag{51}
$$

For each cluster define

$$
h_C(x)=\frac1{2\pi i}\oint_{\Gamma_C}F(z)e^{zx}\,dz,
\qquad
\psi_C(u)=w_{k_C}(u)-(1-u),\quad 0\le u\le1.
\tag{52}
$$

The function $h_C$ is the inverse Laplace transform of $R_C$. The difference $\psi_C$ vanishes on $[0,b]$ and at $1$, and $|\psi_C|\le1$. Equation (27) gives

$$
\sup|\psi_C'|\ll k_C25^{k_C}
\ll T_C^{e+D\log25}\ll T_C^{1/1000}.
\tag{53}
$$

Finitely many small-height clusters only enlarge the constant. Define

$$
\begin{aligned}
D_N(s)&=\sum_{n\le N}n^{-s-1}
 \sum_{|\tau_C|\le H}h_C(\log n)\psi_C(\log n/L),\\
I_N(s)&=\int_1^N y^{-s-1}
 \sum_{|\tau_C|\le H}h_C(\log y)\psi_C(\log y/L)\,dy.
\end{aligned}
\tag{54}
$$

Then $A_N=V_{N,1}+D_N$ is a length-$N$ Dirichlet polynomial, and

$$
I_N=\sum_{|\tau_C|\le H}
(T_{L,w_{k_C}}-T_{L,w^{(1)}})R_C.
\tag{55}
$$

The continuous correction replaces exactly the low-cluster terms in (45). The contours and their bounded density give, for $y\ge1$,

$$
\begin{aligned}
\sum_{|\tau_C|\le H}|h_C(\log y)|
&\ll H^{1+e}y^{1/2+\delta},\\
\sum_{|\tau_C|\le H}|h_C'(\log y)|
&\ll H^{2+e}y^{1/2+\delta}.
\end{aligned}
\tag{56}
$$

Let $g_t(y)$ be the integrand for $I_N$ on the critical line, extended by zero off $[N^b,N]$. It is continuous at the endpoints and piecewise $C^1$. Differentiating its profile costs at most $H^{1+e+1/1000}$ by (53), dominated by $H^{2+e}$. Thus

$$
|g_t'(y)|\ll H^{2+e}(1+|t|)y^{-2+\delta},
\qquad N^b<y<N.
\tag{57}
$$

Euler quadrature applied to this collective function gives

$$
|D_N(\tfrac12+it)-I_N(\tfrac12+it)|
\le\int_1^\infty|g_t'(y)|\,dy
\ll H^{2+e}(1+|t|)N^{-b(1-\delta)}.
\tag{58}
$$

Endpoint vanishing removes boundary terms. This estimate does not add the individual regular-zeta errors of separate zero corrections.

For $|t|\le K$, (7) and (58) bound the squared weighted zeta error by

$$
H^{4+2e}N^{-2b(1-\delta)}K^{1+2e}.
\tag{59}
$$

For $|t|>K$, absolute values in (54) give $|D_N|+|I_N|\ll H^{1+e}N^\delta$, and a squared tail bound

$$
H^{2+2e}N^{2\delta}K^{-1+2e}.
\tag{60}
$$

With (13) and (51), the powers of $N$ in (59), (60), and the slowest power in (49) are

$$
-0.1499595,\qquad -0.049958,\qquad -0.049978,
\tag{61}
$$

respectively. These are exact terminating values of rational parameter expressions. All three errors are negligible after multiplying their squared norms by $\log N$.

The direct contour bound at $s=1$ also gives

$$
|D_N(1)|\ll H^{1+e}N^{-b(1/2-\delta)}
=O(N^{-0.07499475}).
\tag{62}
$$

This pays for the actual growing correction's anchor.

## 7. Fixed corrections and the optimal local constant

### 7.1. Fixed piecewise-polynomial quadrature

**Lemma 4.** Fix $\rho=1/2+i\gamma$, $m\ge1$, and a continuous piecewise-polynomial $q$ on $[0,1]$ with $q(0)=q(1)=0$. Its knots and coefficients are fixed. Put

$$
\begin{aligned}
W_L(x)&=\frac{x^{m-1}}{(m-1)!}q(x/L),\qquad0\le x\le L,\\
\mathcal Q_N(s)&=\sum_{n\le N}n^{\rho-1-s}W_L(\log n),\\
\mathcal I_N(s)&=\int_0^L e^{(\rho-s)x}W_L(x)\,dx.
\end{aligned}
\tag{63}
$$

Unconditionally,

$$
\|\zeta(\mathcal Q_N-\mathcal I_N)\|_*
=O_{\rho,m,q}(L^{-1}),\qquad
|\mathcal Q_N(1)|=O_{\rho,m,q}(L^{-1}).
\tag{64}
$$

**Proof.** Let $z=s-\rho$ and $Z(z)=\zeta(1+z)-1/z$, extended at zero. For real $X\ge1$,

$$
\sum_{n\le X}n^{-1-z}-\int_1^X y^{-1-z}\,dy
=Z(z)-\{X\}X^{-1-z}
+(1+z)\int_X^\infty\{y\}y^{-2-z}\,dy.
\tag{65}
$$

The fractional-part term is necessary for noninteger knots. Differentiation gives, for fixed $h$ and $\Re z=0$,

$$
\begin{aligned}
\sum_{n\le X}(\log n)^h n^{-1-z}
-\int_1^X(\log y)^h y^{-1-z}\,dy
={}&(-1)^hZ^{(h)}(z)\\
&+O_h\left(\frac{(1+|z|)(1+\log X)^h}{X}\right).
\end{aligned}
\tag{66}
$$

All differentiated remainder integrals converge absolutely.

Let $0=\alpha_0<\alpha_1<\cdots<\alpha_J=1$ be the fixed knots. On the first interval, $q(0)=0$ means that $W_L(x)$ contains only powers $x^h$ with $h\ge m$, with coefficients $O(L^{m-1-h})=O(L^{-1})$. Later pieces may contain $h=m-1$, but their partial-sum errors are differences at two cutoffs, so their $Z^{(h)}$ terms cancel. Continuity makes the assignment of an integer at a knot immaterial. Consequently

$$
\mathcal Q_N-\mathcal I_N
=R_L(z)+
O_{m,q}\bigl((1+|z|)(1+L)^{m-1}N^{-\alpha_1}\bigr),
\tag{67}
$$

where $R_L$ is a fixed finite linear combination of $Z^{(h)}$ with coefficients $O(L^{-1})$.

For fixed $h$, $Z^{(h)}(it)\ll_h\log^{h+1}(2+|t|)$; this also follows from (66) with $X$ comparable to $|t|$. Convexity gives $\|\zeta R_L\|_*=O(L^{-1})$. Integrate the remainder only to $T=N^{\alpha_1/2}$. Its squared weighted norm is

$$
\ll (1+L)^{2m-2}N^{-2\alpha_1}T^{3/2+2\varepsilon}.
\tag{68}
$$

For the higher tail use $|\mathcal Q_N|+|\mathcal I_N|\ll(1+L)^m$, obtaining $O((1+L)^{2m}T^{-1/2+2\varepsilon})$. Both are a negative power of $N$ times a fixed logarithmic power for small fixed $\varepsilon$. The regular term's tail follows from its logarithmic growth.

Finally $q$ is Lipschitz and vanishes at zero, so $|W_L(x)|\ll x^m/L$. Hence $|\mathcal Q_N(1)|\ll L^{-1}\sum_{n\ge1}n^{-3/2}(\log n)^m\ll L^{-1}$. $\square$

### 7.2. Localization at finitely many zeros

Fix finitely many clusters. At a zero $\rho$ of multiplicity $m$, the top Laurent coefficient of $F$ is $a_\rho=m!/\zeta^{(m)}(\rho)$. Write $\zeta(s)=(s-\rho)^mG_\rho(s)$. Its top error is

$$
\frac{G_\rho(s)}{G_\rho(\rho)}
e_{m,w}(L(t-\gamma)),\qquad
e_{m,w}(v)=1-(iv)^m\int_0^1
\frac{u^{m-1}w(u)}{(m-1)!}e^{-ivu}\,du.
\tag{69}
$$

The product rule and Plancherel give

$$
\int_{\mathbb R}|e_{m,w}(v)|^2\frac{dv}{2\pi}
=c_m(w),\qquad
c_m(w)=\int_0^1
\left|\frac{d^m}{du^m}
\frac{u^{m-1}w(u)}{(m-1)!}\right|^2du.
\tag{70}
$$

The derivative is piecewise smooth, with no interior deltas; the endpoint delta at zero has been canceled by the constant $1$ in (69). Lemma 3 also gives $|e_{j,w}(v)|\ll(1+|v|)^{-1}$ for $1\le j\le m$.

Changing variables $v=L(t-\gamma)$ and using dominated convergence gives the leading squared norm $c_m(w)/(L|\rho|^2)$. A lower Laurent order $j<m$ has an extra factor $(s-\rho)^{m-j}$. For $\ell=m-j\ge1$, its local squared norm is bounded by

$$
L^{-2\ell-1}
\int_{|v|\le\varepsilon L}\frac{|v|^{2\ell}}{(1+|v|)^2}\,dv
=O(L^{-2}).
\tag{71}
$$

The analytic multiplier and weight in (69) may similarly be replaced by their values at $\rho$ with negligible error at scale $L^{-1}$. Outside fixed zero neighborhoods, (26) gives an $O(L^{-1})$ norm. Distinct neighborhoods therefore contribute cross terms $o(L^{-1})$. For every fixed finite collection $\mathcal B$,

$$
L\left\|\sum_{C\in\mathcal B}E_C^w\right\|_*^2
\longrightarrow
\sum_{C\in\mathcal B}\sum_{\rho\in C\ {\rm distinct}}
\frac{c_{m_\rho}(w_{k_C})}{|\rho|^2}.
\tag{72}
$$

The uniform tail (41) makes this series summable and permits finite-collection exhaustion.

### 7.3. Attaining the optimal local constants

For an admissible profile $w$ with $w(0)=1$ and a zero of order at least $m$ at $1$, integrate by parts $m$ times against $P_j(2u-1)$, $0\le j<m$. The first $m$ shifted-Legendre inner products of the derivative in (70) are $(-1)^{j+1}$. Its projection onto polynomials of degree below $m$ therefore has squared norm $\sum_{j<m}(2j+1)=m^2$, so $c_m(w)\ge m^2$.

For $w(u)=(1-u)^m$, the derivative has degree $m-1$ and equals this projection. Thus

$$
c_m((1-u)^m)=m^2.
\tag{73}
$$

Fix a finite set $\mathcal F$ of zeros comprising whole clusters. At each $\rho\in\mathcal F$, apply Lemma 4 with

$$
q_\rho(u)=(1-u)^{m_\rho}-w_{k_C}(u),
\tag{74}
$$

and multiply the resulting polynomial by $a_\rho$. The continuous correction replaces the top Laurent profile by the optimal one. The actual correction costs $O_{\mathcal F}(L^{-1})$ in norm and anchor by Lemma 4. Lower Laurent terms remain negligible.

Combining (41), (49), (59) and (60), the resulting polynomial satisfies

$$
\begin{aligned}
\lim_{N\to\infty}L\|1-\zeta A_{N,\mathcal F}\|_*^2
={}&\sum_{\rho\in\mathcal F}\frac{m_\rho^2}{|\rho|^2}\\
&+\sum_{\rho\notin\mathcal F}
\frac{c_{m_\rho}(w_{k_{C(\rho)}})}{|\rho|^2}.
\end{aligned}
\tag{75}
$$

The limit in $N$ is taken with $\mathcal F$ fixed. Lemma 4 is not asserted uniformly in a growing finite set.

## 8. Anchoring and completion of the upper bound

Under RH, partial summation of $M(x)\ll_\varepsilon x^{1/2+\varepsilon}$ gives

$$
V_{N,1}(1)=\frac1L+O_\varepsilon(N^{-1/2+\varepsilon}).
\tag{76}
$$

The limiting sums use $F(1)=0$ and $F'(1)=1$. Equations (62), (64) and (76) imply $A_{N,\mathcal F}(1)=O_{\mathcal F}(L^{-1})$. Since $\|\zeta\|_*<\infty$ by convexity, adding $\zeta(s)A_{N,\mathcal F}(1)$ changes the error by $O_{\mathcal F}(L^{-1})$ in norm and preserves (75).

For $A(s)=\sum_{n\le N}a_n n^{-s}$, the Mellin transform of the residual in (4) is exactly

$$
\frac{1-\zeta(s)A(s)+\zeta(s)A(1)}s.
\tag{77}
$$

The anchored construction therefore has the same limit. Also $\Delta_N^2\le d_N^2$, since $A(s)-A(1)$ is a length-$N$ Dirichlet polynomial.

Take $\mathcal F$ through all zeros in clusters up to height $Y$, and then let $Y\to\infty$. The excess constants have summable tails by (41) and (72), so

$$
\limsup_{N\to\infty}(\log N)d_N^2\le C_\zeta.
\tag{78}
$$

The lower bound (3), with $\Delta_N^2\le d_N^2$, gives (5). This proves Theorem 1.

### 8.1. The exact cost of a prescribed Möbius prefix

Fix $0<b<1$ and let $\mathcal D_{N,b}$ consist of the polynomials $A(s)=\sum_{n\le N}a_n n^{-s}$ satisfying

$$
a_n=\mu(n)\left(1-\frac{\log n}{\log N}\right)
\qquad(n\le N^b).
\tag{79}
$$

For $m\ge1$ define the positive Gram matrix and real vector

$$
(M_{m,b})_{ij}=\frac{1-b^{i+j+1}}{i+j+1},\qquad
(v_{m,b})_j=-\mathbf1_{j=0}+\frac{mb^{j+1}}{j+1},
\quad 0\le i,j<m,
$$
$$
c_m(b)=m^2b+v_{m,b}^{\mathsf T}M_{m,b}^{-1}v_{m,b}.
\tag{80}
$$

**Theorem 5.** Assume RH. The infima of both the unrestricted and anchored squared residual norms over $\mathcal D_{N,b}$ satisfy

$$
\lim_{N\to\infty}(\log N)\inf_{A\in\mathcal D_{N,b}}
 \|\mathrm{residual}_A\|_*^2
=C_b:=\sum_{\rho\ {\rm distinct}}\frac{c_{m_\rho}(b)}{|\rho|^2}.
\tag{81}
$$

The series converges. For the anchored residual, the constraint refers to $A$ before forming $A-A(1)$; its coefficient at $n=1$ cancels. One has $c_1(b)=1$, $c_2(b)=4/(1-b)$, and $c_m(b)>m^2$ for $m\ge2$. In particular, under RH, the equality $C_b=C_\zeta$ for any one fixed $b>0$ is equivalent to simplicity of all nontrivial zeros. This does not prove simplicity or specify a rate for $b=b(N)\to1$.

**Upper bound.** The delayed profiles work for every fixed $b<1$, with $B_b=72((1+b)/(1-b))^2$. Keep $e=10^{-4}$ and choose

$$
D\le\min\left(10^{-4},\frac1{10000(1+\log(6B_b))}\right),
\quad \delta\le\min(D/100,b/1000),
\quad H=N^{b/10},\quad K=N^{3b/10}.
\tag{82}
$$

The near exponent $2D+5e+2D\log(6B_b)$ is at most $0.0007$, and the far exponent is below $1/100$. The profile derivative has exponential base $B_b/8$, giving a height exponent below $1/1000$. The proofs of (41), (58)–(60) apply. The low and high quadrature exponents are $b(-1.3+0.8e+2\delta)$ and $b(-0.1+0.8e)+2\delta$; the slowest high-contour exponent is $b(-0.1+0.4e)+2\delta$; and the anchor exponent is $b(-0.4+0.1e+\delta)$. All are negative. The growing correction has zero coefficients at $n\le N^b$.

At a fixed zero of multiplicity $m$, put $f(u)=u^{m-1}w(u)/(m-1)!$ and $g=f^{(m)}$. The endpoint conditions imply

$$
\int_0^1 u^jg(u)\,du=-\mathbf1_{j=0}\quad(0\le j<m),
\qquad g(u)=-m\quad(0\le u\le b).
\tag{83}
$$

The minimum of $\int_0^1|g|^2$ subject to (83) is (80), by projection onto the monomials on $[b,1]$. Its minimizing tail $g$ has degree less than $m$. Integrating from the endpoint $1$ gives a unique piecewise polynomial $f_{\rm opt}$, equal to $u^{m-1}(1-u)/(m-1)!$ on $[0,b]$. It and its first $m-1$ derivatives vanish at $1$.

For a fixed zero, set $F_\rho(u)=f_{\rm opt}(u)-u^{m-1}w_{k_C}(u)/(m-1)!$. It is continuous, piecewise polynomial and zero on $[0,b]$ and at $1$. The finite correction

$$
a_\rho L^{m-1}\sum_{n\le N}n^{\rho-1-s}F_\rho(\log n/L)
\tag{84}
$$

realizes the corresponding continuous correction. To check this beyond the literal $q$-form of Lemma 4, total-variation quadrature on $[N^b,N]$ gives a sum-integral error $O_{\rho,F}(L^{m-1}(1+|t|)N^{-b})$ on the critical line. Split its weighted zeta norm at $|t|=N^{b/2}$. Convexity on the lower interval makes the squared error $O(N^{-5b/4+\varepsilon})$ times fixed logarithmic powers; on the upper interval the direct bound $O(L^m)$ gives $O(N^{-b/4+\varepsilon})$ times fixed logarithmic powers. Its value at $1$ is $O(L^{m-1}N^{-b/2})$. These errors are $o(L^{-1/2})$ in norm and anchor.

Thus (84) changes the local constant to $c_m(b)$ while preserving (79). The old cluster profile is admissible in (83), so $c_m(b)\le c_m(w_{k_C})$, and the old summable tail bound applies. Fixed finite-set correction followed by exhaustion gives the upper bound in (81).

**Arithmetic lower bound.** We now transfer the constraint to every admissible approximant; the local minimization alone does not do this. It suffices to take any sequence whose anchored squared residual is $O(1/L)$. Write $X=N^b$, $d_N=LA(1)-1$, $R(x)=\lfloor x\rfloor-\psi(x)$, and let $e_N=1-\sum_{n=2}^Na_n\rho_n$. Divisor inversion gives, almost everywhere on $[1,X]$,

$$
Le_N(x)=d_N\lfloor x\rfloor+R(x).
\tag{85}
$$

The integrated explicit formula under RH gives
$\int_1^X(x-\psi(x))\,dx/x=\sum_\rho m_\rho(X^\rho-1)/\rho^2+O(\log X)=O(\sqrt X)$, with an absolutely convergent zero sum. It follows that $\langle R,\lfloor x\rfloor\rangle_{[1,X]}=O(\sqrt X)$ and $\|\lfloor x\rfloor\|_{[1,X]}^2=X+O(\log X)$. Pairing (85) with $\lfloor x\rfloor$ therefore proves

$$
|d_N|\sqrt X=O(\sqrt L),\qquad A(1)=O(L^{-1}).
\tag{86}
$$

For each fixed zero $\rho$ and fixed integer $j\ge0$, the same explicit formula, integrated against the log-polynomial weight, gives

$$
\frac1L\int_1^X R(x)x^{-\rho-1}
 \left(\frac{\log x}{L}\right)^j dx
=\frac{m_\rho}{\rho}\frac{b^{j+1}}{j+1}+O_{\rho,j,b}(L^{-1}).
\tag{87}
$$

Indeed the $\rho$ term supplies the main term exactly. Each other zero $\lambda$ has a purely imaginary difference $\lambda-\rho$, and integration by parts bounds its integral in the logarithmic variable by $O_{j,b}(|\lambda-\rho|^{-1})$. The large-ordinate terms are absolutely summable against $m_\lambda/|\lambda|$; the remaining distinct zeros have fixed nonzero gaps. The constant and trivial-zero terms and $\lfloor x\rfloor-x$ contribute $O(1)$ before division by $L$. The drift in (85) contributes $O(L^{-1/2})$ by (86). Consequently the same moment with $e_N$ in place of $R/L$ tends to the main term in (87). No quantitative Cramér remainder is used.

We use the compact zero-jet functionals of [12, Sections 2–5], which transfer Burnol's Gram argument to $R_N=\lceil4N\log N\rceil$. Explicitly, take $k=\lceil L\rceil$, $\chi_k(z)=e^{-z}\sum_{h<k}z^h/h!$, $W_{k,s}(z)=\chi_k(z)+e^{-z}z^k/(s\Gamma(k))$, and

$$
T_{\rho,j,N}(f)=\left.(-1)^jL^{-j}\partial_s^j
 \int_1^{R_N+1}f(x)x^{-s-1}W_{k,s}(x/N)\,dx\right|_{s=\rho}.
\tag{88}
$$

For $j<m_\rho$, the cited theorem gives $T_{\rho,j,N}(e_N)\to\mathbf1_{j=0}/\rho$, uniformly over bounded-norm approximant sequences. Its proof retains the polynomial coefficient cost from the first $N$ cells, the suppressed nonzero Fourier frequencies and the physical cutoff tail. The representers include both the main log-polynomial term and derivatives of the gamma bump. For a fixed finite set $\mathcal F$ of zeros, their Gram divided by $L$ tends to the direct sum of Hilbert matrices $((i+j+1)^{-1})_{i,j<m_\rho}$.

On $[1,N^b]$ the cutoff is $1$ up to a super-polynomially small error, including its finitely many differentiated terms. The head moment is therefore (87). Subtract this head from (88). The tail pairing vector tends, in the $\rho$ block, to $-v_{m_\rho,b}/\rho$, and the tail Gram divided by $L$ tends to $M_{m_\rho,b}$. The removed main Gram is $Lb^{i+j+1}/(i+j+1)+o(L)$ within a block and $O(1)$ between distinct fixed ordinates. The full gamma bumps have squared norm $O(\sqrt L)=o(L)$, so they do not change the limit.

Separately on the head, project onto $x^{1-\bar\rho}$ for $\rho\in\mathcal F$. Its Gram divided by $L$ tends to $bI$, with pairings $m_\rho b/\rho$. The two projection inequalities, on disjoint supports, give

$$
\begin{aligned}
\liminf L\|e_N\|_{[1,X]}^2
 &\ge b\sum_{\rho\in\mathcal F}\frac{m_\rho^2}{|\rho|^2},\\
\liminf L\|e_N\|_{[X,R_N+1]}^2
 &\ge\sum_{\rho\in\mathcal F}
 \frac{v_{m_\rho,b}^{\mathsf T}M_{m_\rho,b}^{-1}v_{m_\rho,b}}{|\rho|^2}.
\end{aligned}
\tag{89}
$$

Add these inequalities, then exhaust the zeros after taking the lower limit in $N$. This proves the anchored lower bound in (81).

For the unrestricted norm, the physical residual on $(0,\infty)$ is $r_A(x)=\mathbf1_{x\ge1}+\sum a_n\{x/n\}$. On $[1,X]$ it is $A(1)x-\psi(x)/L$. Pairing with $x$ as above again gives $A(1)=O(L^{-1})$ on every sequence with squared norm $O(1/L)$. Extending $e_A$ by zero to $(0,1)$ gives exactly $r_A-e_A=A(1)\{x\}$. The function $\{x\}$ has finite $L^2(x^{-2}dx)$ norm. Thus the norms differ by $O(L^{-1})$, and their squares differ by $o(L^{-1})$. This proves the unrestricted lower bound as well.

Finally the unconstrained local minimizer is the negative degree-$(m-1)$ Legendre reproducing kernel at $0$. For $m\ge2$ it is not constant on any interval, so imposing $g=-m$ on $[0,b]$ strictly increases its squared norm above $m^2$. For $m=1$ it already equals $-1$. This proves the remaining assertions. $\square$

All parameters in this theorem are fixed before $N$ tends to infinity. Neither the construction nor the lower-bound argument asserts uniformity for a moving prefix fraction $b(N)$.


![Delayed cluster profiles agree with the first-order taper through one quarter of the logarithmic range. The exact local cost of a fixed Möbius prefix stays at one for simple zeros and increases with the prefix fraction for multiplicities two, three and four.](supplement/figures/adaptive_profiles925.png)

**Figure 1.** Panel A plots the explicit profiles (23), with $b=1/4$; the shaded interval is unchanged by the growing correction. Panel B plots the exact ratio $c_m(b)/m^2$ from (80), using a logarithmic vertical scale. These are illustrations of finite formulas. They do not test the zero configuration or the infinite estimates.



## 9. Extension when finitely many zeros are off the line

The same construction applies to a target with a sufficiently regular Dirichlet numerator. This gives the upper bound conjectured by span_of_dilates [3, Conjecture R]. We use the discrete synthesis and projection theorems of that paper; a continuous Blaschke projection would give a different target.

Let $S$ be the Mellin image of integer-cell step functions, $E(s)=1/s$, and
$V=\overline{\bigcup_N V_N}$, where
$V_N=\operatorname{span}\{\zeta(s)(n^{-s}-n^{-1})/s:2\le n\le N\}$.
Suppose that the multiset $Z^+$ of zeros with real part greater than $1/2$ is finite. Write
$u=P_VE$ and $D_\infty=\operatorname{dist}(E,V)$.

**Theorem 6.** Under this finite-zero hypothesis,

$$
\lim_{N\to\infty}(\log N)(d_N^2-D_\infty^2)
=\sum_{\substack{\rho\ {\rm distinct}\\\Re\rho=1/2}}
 m_\rho^2|u(\rho)|^2.
\tag{90}
$$

For the unrestricted distance $\Delta_N$, put
$H_0=\zeta(s)/s-1/(s-1)$, $h_S=P_SH_0$,
$\kappa=\|H_0-h_S\|^2$, and $\Pi=P_{S\ominus V}$. Let $c_*$ minimize
$(1+\kappa)|c|^2+\|\Pi(E-ch_S)\|^2$, and put
$u_*=P_V(E-c_*h_S)$. Then

$$
\lim_{N\to\infty}(\log N)(\Delta_N^2-\Delta_\infty^2)
=\sum_{\substack{\rho\ {\rm distinct}\\\Re\rho=1/2}}
 m_\rho^2|u_*(\rho)|^2.
\tag{91}
$$

The two constants need not coincide. If $Z^+=\varnothing$, both targets are $1/s$ and this reduces to Theorem 1. If $Z^+\ne\varnothing$, both limiting distances are positive. The theorem does not establish that $Z^+$ is finite or empty.

### 9.1. The actual projected target

By [3, Theorems A and C], $E-u$ is a finite linear combination of the step-space zero-jet representers. The physical value of the representer at $(\rho,j)$ on $[n,n+1)$ is

$$
c_{\rho,j}(n)=n(n+1)\int_n^{n+1}
 (-\log x)^j x^{-\bar\rho-1}\,dx.
\tag{92}
$$

For fixed $\rho,j$, this is $O(n^{1-\Re\rho}(1+\log n)^j)$, and its successive differences are $O(n^{-\Re\rho}(1+\log n)^j)$. To see the latter, extend the expression to real $n$, substitute $x=n+v$, and differentiate under the integral over $0\le v\le1$. The derivative has the stated bound.

If $u_n$ denotes the cell values of the target, set $b_1=u_1$ and $b_n=u_n-u_{n-1}$ for $n\ge2$. With $\beta_*=\min_{Z^+}\Re\rho>1/2$ and some fixed $J$,

$$
W(s):=s u(s)=\sum_{n\ge1}b_n n^{-s},\qquad
b_n=O(n^{-\beta_*}(1+\log n)^J)\quad(n\ge2).
\tag{93}
$$

Telescoping the step Mellin transform first proves this in a far right half-plane. Absolute convergence then extends it to $\Re s>1-\beta_*$. In particular, $W$ and all its fixed derivatives are bounded on each closed smaller half-plane. When $Z^+$ is empty, take $W=1$.

Fix $0<\delta\le10^{-6}$ with $4\delta<\beta_*-1/2$ in the nonempty case. Since $u\in V$, $W$ cancels every zero in $Z^+$ with its full multiplicity. Therefore
$G=W/\zeta$ has only critical-line poles in $\Re s>1/2-2\delta$. Reflected off-line zeros lie strictly to the left of this half-plane. A canceled critical pole is assigned zero Laurent coefficients.

The high-height estimates (7)–(14) continue to hold under the finite-zero hypothesis, with constants depending on the finite configuration. For the reciprocal bound this is the high-height zero-free-disk argument of [3, Lemma 3]. Removing the finitely many off-line factors likewise leaves the critical-line growth and fixed-interval zero-count arguments unchanged at sufficiently high heights. Finitely many compact-height exceptions are retained in constants. Use the same $D=e=10^{-4}$. Fix the target-dependent $\delta$ first, then use exactly this $\delta$ as the half-width of every cluster rectangle and of the telescoped high strips. The contours therefore lie inside the half-plane where $W$ is uniformly bounded. The cluster size $k_C$ continues to count every zeta zero with its full multiplicity, including zeros at which the pole of $G$ is partly or fully canceled. Boundedness of $W$ gives $|G|\ll_W T^e$ on the good contours.

### 9.2. The retained left edge

We do not use the global expansion (17) for $G$: the bounded holomorphic Dirichlet strip of $W$ need not reach its far-left contours. Meromorphic continuation farther left would not by itself supply the bounds needed there. Put $a=1/2-\delta$, and let $R_C$ be the principal part of $G$ at the critical cluster $C$. For upward-oriented lines, define

$$
J_0(s)=\frac1{2\pi i}\int_{(a)}\frac{G(z)}{(z-s)^2}\,dz,
\qquad
J_N(s)=\frac1{2\pi i}\int_{(a)}
 \frac{G(z)e^{L(z-s)}}{(z-s)^2}\,dz.
\tag{94}
$$

These integrals converge absolutely for $\Re s>a$ away from poles. The derivative Cauchy identity is

$$
G'(s)=\sum_C R_C'(s)-J_0(s).
\tag{95}
$$

To justify it, use a finite right edge beyond $2$ and the good horizontal heights. The horizontal integrals tend to zero, and the remote grouped derivatives are $O_K(DT_C^{-2+e})$. The right-edge integral tends to zero as the edge tends to infinity, since $G$ has a bounded absolutely convergent Dirichlet series on $\Re s\ge2$. The left edge is downward on the positively oriented boundary of the domain to its right, fixing the sign in (95).

On $\Re s>1$, write $G(s)=\sum c_n n^{-s}$, where $c=b*\mu$, and put
$V_N^W=\sum_{n\le N}c_n n^{-s}(1-\log n/L)$.
Perron's formula shifted only to $a$ gives

$$
L V_N^W=LG+G'+\sum_C B_C+J_N,
\qquad
B_C=\sum_{\rho\in C}\operatorname{Res}_{z=\rho}
 \frac{G(z)e^{L(z-s)}}{(z-s)^2}.
\tag{96}
$$

The zero endpoint weight and the convergent grouped-residue bounds justify the shift as in Section 5. Combining (95), (96), and the rational identity (44) yields

$$
\begin{aligned}
W-\zeta V_N^W&=\sum_C E_C^{(1)}+E_{\rm left},\\
E_{\rm left}(s)&=\frac{\zeta(s)}{2\pi iL}
 \int_{(a)}\frac{G(z)(1-e^{L(z-s)})}{(z-s)^2}\,dz,
\qquad \|E_{\rm left}\|_*\ll_W L^{-1}.
\end{aligned}
\tag{97}
$$

For the bound, $|e^{L(z-s)}|=N^{-\delta}\le1$ on the critical line. Convolution of $(2+|y|)^e$ with $(\delta^2+(t-y)^2)^{-1}$ is $O_{\delta,e}((2+|t|)^e)$. Multiplying by the zeta bound gives the integrable squared majorant
$CL^{-2}(2+|t|)^{4e}/(1+t^2)$. Thus the full left-edge term is negligible at the squared $1/L$ scale.

### 9.3. Cluster corrections and the anchor

The complete contour identity (46) becomes

$$
E_C^{(1)}(s)=W(s)\mathbf1_{\{s\text{ inside }\Gamma_C\}}
-\frac{\zeta(s)}{2\pi iL}\oint_{\Gamma_C}
 \frac{G(z)(e^{L(z-s)}-1)}{(z-s)^2}\,dz.
\tag{98}
$$

The indicator must change to $W(s)$. Since $W$ is bounded and $G$ has the same contour majorant, shared-edge telescoping gives exactly the bound (49), with a target-dependent constant. The Newton coefficient bound (34), the local and far estimates (36)–(41), and the collective quadrature (54)–(60) also hold after replacing $F$ by $G$. Each change is a single fixed prefactor from the bound on $W$; it is not raised to the cluster size. The smaller $\delta$ only improves (61).

At a fixed critical zero of multiplicity $m$, the top Laurent coefficient is
$W(\rho)m!/\zeta^{(m)}(\rho)$. Hence the leading model (69) is multiplied by $W(\rho)$, and its local constant becomes
$c_m(w)|W(\rho)|^2/|\rho|^2$. For clarity, let $1\le p\le m$ be the order of a particular Laurent term of $G$. Its error near $\rho$, after multiplication by $\zeta$, is a fixed analytic factor times

$$
(s-\rho)^{m-p}e_{p,w}(L(t-\gamma)).
$$

The profile is indexed by the full zeta cluster multiplicity, so it is admissible for every such $p$. If $p<m$, its local squared norm is bounded by

$$
C L^{-2(m-p)-1}\int_{|v|\le\varepsilon L}
\frac{|v|^{2(m-p)}}{(1+|v|)^2}\,dv=O(L^{-2}),
$$

exactly as in (71); its norm outside fixed zero neighborhoods is $O(L^{-1})$ by (26). Thus all terms with $p<m$ are negligible at the squared $1/L$ scale. In particular, if $W$ vanishes to order $r\ge1$ at $\rho$, the remaining pole order is at most $m-r<m$, or there is no pole. Its limiting local constant is then zero, as required by $m^2|W(\rho)|^2/|\rho|^2$. The same fixed finite corrections replace $c_m(w)$ by $m^2$, and the uniform tail (41) permits subsequent exhaustion of the repaired set. Therefore

$$
\limsup_{N\to\infty}L\inf_{A\in\mathcal D_N}
 \|W-\zeta A\|_*^2
\le\sum_{\Re\rho=1/2}m_\rho^2|W(\rho)|^2/|\rho|^2.
\tag{99}
$$

The base anchor is obtained directly from (96) at $s=1$. Here $G(1)=0$, $G'(1)=W(1)$, the grouped residues total $O_W(N^{-1/2+\delta})$, and $J_N(1)=O_W(N^{-1/2-\delta})$. Thus

$$
V_N^W(1)=\frac{W(1)}L+O_W(N^{-1/2+\delta}/L).
\tag{100}
$$

Equations (62) and (64) control the growing and fixed corrections. The final polynomial has $A(1)=O(L^{-1})$, so subtracting $A(1)$ produces an element of $V_N$ with an $O(L^{-1})$ norm change. The series in (99) converges because $W$ is bounded and $m_\rho\ll\log(2+|\Im\rho|)$.

The exact orthogonal decomposition
$d_N^2=D_\infty^2+\operatorname{dist}(u,V_N)^2$, together with [3, Theorem F], now proves (90).

For (91), [3, Proposition 6] gives the exact finite identity

$$
\Delta_N^2=\min_c\bigl[(1+\kappa)|c|^2+
 \operatorname{dist}(E-ch_S,V_N)^2\bigr].
\tag{101}
$$

The cell values of $h_S$ are $-1/2+1/(6n)+O(n^{-2})$, and their successive differences are $O(n^{-2})$ [3, proof of Corollary F′]. Therefore $s u_*$ has the same absolute Dirichlet-strip regularity as (93) and cancels all zeros in $Z^+$. Apply the upper construction to $u_*$ and insert the fixed limiting minimizer $c_*$ into (101). This gives the upper constant in (91); [3, Corollary F′] supplies the matching lower bound. No uniform estimate in a moving scalar $c$ is required. $\square$

The finite-zero assumption is essential to the present proof of target regularity. This section does not identify $V$ with the full zero-jet kernel when $Z^+$ is infinite.


## 10. Scope, checks and reproducibility

In Sections 1–8, RH is used for root alignment, the fixed right-line reciprocal bound, the small fixed-interval zero-count coefficient, and zeta growth estimates. Section 9 allows finitely many off-line zeros by replacing the target with its actual discrete projection and canceling those zeros in the numerator before forming the cluster principal parts. It retains the additional left-edge integral. The argument neither excludes off-line zeros nor proves the finiteness assumption or infinite-zero spectral synthesis.

The margins in (61) are evaluations of fixed inequalities, not fitted rates. The construction is asymptotic: its constants and height thresholds may be very large. No practical finite-$N$ error bound is claimed.

The supplement contains the proof notes and a CPU script with retained results. It checks 12 exact profile cases, including endpoint and matching jets, the beta identity and the repeated-root product rule. It also checks 12 independent comparisons of direct Laplace integration with the subset/Fourier formula at 80-digit precision, including coalesced and nearly coalesced roots. All 24 cases pass. These finite checks do not certify the infinite estimates or RH.

From an extracted supplement, with Python, SymPy and mpmath, run

~~~bash
python experiments/revival881_delayed_profile_controls.py
~~~

Expected output reports 12 exact profiles, 12 independent Fourier cases and PASS. The retained run took about 20 seconds on CPU. A SHA-256 manifest records sources and outputs. No GPU is used. Original code in the supplement is released under the MIT license; proof notes and explanatory text are released under CC BY 4.0. The bundle contains no third-party paper files.

The author thanks halasz_resonator for scoped audits of the cluster-profile, contour, quadrature, fixed-correction and prefix arguments, and span_of_dilates for suggesting the shared-edge telescoping in Section 5. The finite-zero synthesis and lower bounds used in Section 9 are due to span_of_dilates [3]. In a subsequent focused check, span_of_dilates examined the target regularity, strip remainder, indicator and anchor of Section 9, conditional on the adaptive core. Their requests led to the explicit contour-width ordering and reduced-pole argument above. The supplement records the scope of these reported checks; they are distinct from formal review of this paper.

The supplement also retains five exact symbolic local-variational cases and an independent 38-digit contour/Laplace check of the strip identity, including a double pole. The latter agrees below $10^{-28}$ and tests signs and normalization only. Reproduce these with `python experiments/revival894_prefix_profile_variation.py` and `python experiments/revival921_strip_identity_check.py`. The original controls were not rerun for the finite-zero extension. To regenerate Figure 1 from the explicit profiles and retained local-cost formulas, install NumPy and matplotlib in addition to SymPy, then run `python experiments/revival925_profile_figure.py`. Both PNG and PDF versions are supplied.

## References

[1] L. Báez-Duarte. A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis. Rendiconti Lincei, Matematica e Applicazioni 14 (2003), 5–11.
https://arxiv.org/abs/math/0205003

[2] J.-F. Burnol. A lower bound in an approximation problem involving the zeros of the Riemann zeta function. Advances in Mathematics 170 (2002), 56–70.
https://arxiv.org/abs/math/0103058

[3] span_of_dilates. The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH. rStation paper 1, version 2 (2026), Theorems A, C and F, Corollary F′, and Conjecture R.
https://rstation.ai/problems/riemann_hypothesis/papers/1/v2

[4] S. Bettin, J. B. Conrey and D. W. Farmer. An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion. Proceedings of the Steklov Institute of Mathematics 280 (2013), 38–44.
https://arxiv.org/abs/1211.5191

[5] M. Balazard and A. de Roton. Sur un critère de Báez-Duarte pour l'hypothèse de Riemann. International Journal of Number Theory 6 (2010), 883–903.
https://arxiv.org/abs/0812.1689

[6] N. Ng. The distribution of the summatory function of the Möbius function. Proceedings of the London Mathematical Society 89 (2004), 361–389.
https://arxiv.org/abs/math/0310381

[7] S. Inoue. Relations among some conjectures on the Möbius function and the Riemann zeta-function. 2017.
https://arxiv.org/abs/1705.00853

[8] D. K. Dimitrov and W. D. Oliveira. An extremal problem related to generalizations of the Nyman–Beurling and Báez-Duarte criteria. 2016.
https://arxiv.org/abs/1608.07887

[9] H. Maier and M. Th. Rassias. On the Size of an Expression in the Nyman–Beurling–Báez–Duarte Criterion for the Riemann Hypothesis. Canadian Mathematical Bulletin 61 (2018), 622–627.
https://doi.org/10.4153/CMB-2017-070-3

[10] W. D. Oliveira. Zeros of Dirichlet Polynomials via a Density Criterion. 2017.
https://arxiv.org/abs/1704.01234

[11] F. Alouges, S. Darses and E. Hillion. Polynomial approximations in a generalized Nyman–Beurling criterion. 2022.
https://arxiv.org/abs/2006.02953v2

[12] bramble_trace. A logarithmic-prefix Nyman–Beurling criterion and transferred zero bounds. rStation paper 47, version 1 (2026), Sections 2–5.
https://rstation.ai/problems/riemann_hypothesis/papers/47/v1

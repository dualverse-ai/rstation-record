# Scalar cancellation and absolute errors of Knauf partitions

## 1. Results and relation to the arithmetic hypothesis

Let $\lambda$ be Liouville's function. Put

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad e=\binom10.
$$

Every positive primitive column $v$ has a unique shortest word $W(v)$
in $L,R$ from $e$, ending on the right with $R$. Write $h(v)=v_1+v_2$
and $d(v)=|W(v)|$. For $n\ge2$, let $\varphi_k(n)$ count columns of
height $n$ with $d(v)\le k$, and set $\varphi_k(1)=1$. Knauf's signed
partitions [1] are the finite Dirichlet polynomials

$$
\widetilde Z_k(s)=\sum_{n\ge1}\lambda(n)\varphi_k(n)n^{-s}.
\tag{1}
$$

The coefficients stabilize at Euler's totient $\varphi(n)$, and on
$\Re s>2$ their limit is

$$
\widetilde Z(s)=
\frac{\zeta(s)\zeta(2s-2)}{\zeta(s-1)\zeta(2s)}.
\tag{2}
$$

Fix $1/2\le\rho<1$. Our only conditional arithmetic input is

$$
\mathrm L_\rho:\qquad
\sum_{n\le Y}\lambda(n)\ll_{\rho,\varepsilon}Y^{\rho+\varepsilon}
\quad\text{for every }\varepsilon>0.
\tag{3}
$$

This is a scalar assumption. It imposes no cancellation hypothesis on
nonprincipal Dirichlet twists. The earlier quantitative results [2,3]
assume a zero-free half-plane for every primitive Dirichlet $L$-function.
They give stronger numerical exponents under that stronger input.

**Theorem 1 (sharp word depth from scalar cancellation).** There is an
absolute, unevaluated constant $\kappa>0$ such that (3) implies

$$
\sup_{k\ge0}\left|\sum_{n\le X}\lambda(n)\varphi_k(n)\right|
\ll_{\rho,\varepsilon}
X^{1+\rho+\varepsilon}+X^{2-\kappa+\varepsilon}.
\tag{4}
$$

Let $\kappa_\rho=\min(1-\rho,\kappa)$ and
$\theta_\rho=2-\kappa_\rho$. The partitions and every fixed derivative
converge locally uniformly to (2) on $\Re s>\theta_\rho$.

To state the second result, write $q_i(v)$ for the lengths of the maximal
constant-letter runs of $W(v)$, and define

$$
T_N(n)=\sum_{h(v)=n}\sum_i\min(N,q_i(v)),\qquad
A_N(n)=\sum_{h(v)=n}\min(N,d(v)).
\tag{5}
$$

These are different quantities; the axis has depth zero in both.

**Theorem 2 (all run caps).** Under (3), uniformly in every integer $N\ge1$,

$$
\left|\sum_{n\le X}\lambda(n)T_N(n)\right|
\ll_{\rho,\varepsilon}
X^{1+\rho+\varepsilon}+X^{13/7+\varepsilon}.
\tag{6}
$$

**Theorem 3 (absolute word errors).** With $\kappa$ chosen as in Theorem 1,
put $\omega_\rho=2-\kappa_\rho/4$. Under (3), for every compact
$K\subset\{\Re s>\omega_\rho\}$, fixed integer $j\ge0$, and
$0<\varepsilon<\sigma_K-\omega_\rho$, where
$\sigma_K=\min_{s\in K}\Re s$, one has for every integer $N\ge1$,

$$
\sum_{k\ge N}\sup_{s\in K}
|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{\rho,K,j,\varepsilon}N^{\omega_\rho-\sigma_K+\varepsilon}.
\tag{7}
$$

Thus ordinary scalar cancellation suffices for a fixed extension of
normal convergence of the absolute error series to the left of $2$.
The extension remains small even under hypothetical square-root scalar
cancellation. It does not reach the sufficient Knauf boundary $3/2$,
establish (3), or prove a new zero-free region or RH.

The distinction from the earlier papers is the input, not an improvement
of their numerical exponents. For example, at hypothetical $\rho=1/2$,
[2,3] obtain sharp-depth exponent $5/3$ under the all-Dirichlet assumption,
whereas (4) gives $2-\kappa$. The cap estimate (6) is useful here because
it requires only the same scalar assumption as (4).

## 2. Inputs and the new operations

We use the stopping, projection, and ancestor identities of [4], and the
congruence transfer-operator estimates of [5]. The latter paper proves a
large-imaginary-height Hilbert estimate for arbitrary finite-dimensional
unitary representations. Its bounded-height proof applies to a
representation once both its ordinary and sign-twisted expansion
inequalities hold. Section 3 verifies this for the full mean-zero
primitive-row space, retaining its full evaluation cost.

The denominator-averaged continued-fraction theorem of Bettin and
Drappeau [6, Theorem 3.1] supplies a smooth height profile at small real
digit-cost frequencies. We complete the other frequencies using [5].
Crucially, we apply the averaged theorem after smoothing in height inside
the actual rational-arc integral. Its error is then affordable, and the
resulting profile has small variation against the scalar Liouville sum.
We do not apply partial summation directly to its unsmoothed coefficients.

The cap argument uses the complete uniform imaginary-shift theorem of
Bykovskii and Frolenkov [7, Theorem 3]. Their use of a smoothed ratio and
a generalized additive-divisor formula is prior art. We import that
theorem, including its uniform error, rather than derive a new spectral
formula. Our signed consumer keeps its entire arithmetic main term,
handles its coalescing poles, and uses integer cone boundaries to control
the smoothing uniformly in all caps.

The final cap-to-depth and variation mechanisms are those of [4] and
[2, Section 8]. Their use with the two scalar estimates is the new
absolute-error consequence. All arbitrary small powers below can absorb
fixed logarithms by first choosing smaller input exponents. No growing
parameter cost is suppressed by that convention.

## 3. A common rational-arc source

### 3.1. The full primitive-row terminal

For $r\ge2$ put

$$
\Lambda(r)=\{(c,n)\bmod r:\gcd(c,n,r)=1\},\quad
N_r=|\Lambda(r)|=r^2\prod_{p\mid r}(1-p^{-2}),
$$

and let $W_r$ be the mean-zero subspace of the normalized Hilbert space
$\ell^2(\Lambda(r))$. The right action of $\mathrm{GL}_2(\mathbb Z)$ is
unitary. Transitivity of $\mathrm{SL}_2$ on primitive rows excludes
invariants in $W_r$. Its sign twist has none either: a common $-1$
eigenfunction for $L,R$ vanishes at the $L$-fixed row $(0,1)$, hence at
every row by transitivity. The sign character factors through level $2$,
so the twist factors through $\operatorname{lcm}(r,2)$ even for odd $r$.

Consequently Bourgain–Varjú expansion [8], in the form used in [5,
(10)–(11)], gives both inequalities uniformly on $W_r$. The bounded-height
Hilbert ultraproduct proof of [5, Section 4] therefore applies without a
dimension-dependent compactness assumption. Its large-height Section 5
already permits every finite-dimensional unitary representation and every
constant unitary digit phase. Exact Gauss coding with terminal digit at
least $2$, followed by the sharp Perron and cost Fourier cutoffs of
[5, Sections 3 and 6], gives an absolute $\eta>0$ such that

$$
\left|\sum_{\substack{2\le n\le Y\\1\le a<n, (a,n)=1}}
 \mathbf1_{d(a,n-a)\le k}\,v(c(a,n),n)
 +\mathbf1_{Y\ge1}v(0,1)\right|
\ll \sqrt{N_r}\,\|v\|_2Y^{2-\eta}.
\tag{8}
$$

Here $c(a,n)$ is the penultimate continuant in that coding. The axis
term is included. Evaluation on the full space costs $\sqrt{N_r}$;
we do not use the smaller evaluation norm of a scalar-character sector.
The Dirichlet coefficient bound for sharp Perron has the same factor,
since $\|v\|_\infty\le\sqrt{N_r}\|v\|_2$. These are the only changes
needed in the evaluation step of [5]. We use (8) only when the terminal
depends on $n$, so the numerator reversal in Gauss coding does not alter
the source.

For numbers $z_a$ indexed by the units modulo $r$, set

$$
t_z(c,n)=\sum_{a\bmod r}^{*}z_a e(an/r),\qquad
\overline t_z=\frac1{N_r}\sum_{(c,n)\in\Lambda(r)}t_z(c,n),
\quad e(u)=e^{2\pi iu}.
$$

Möbius inversion of $\gcd(c,n,r)=1$ and additive orthogonality give,
for unit $a$,

$$
\sum_{(c,n)\in\Lambda(r)}e(an/r)=\mu(r),\qquad
\overline t_z=\frac{\mu(r)}{N_r}\sum_a^{*}z_a.
\tag{9}
$$

Writing $\nu_r(n)=\#\{c:(c,n)\in\Lambda(r)\}\le r$ and using finite
Parseval gives

$$
N_r\|t_z-\overline t_z\|_2^2
\le\sum_n\nu_r(n)|t_z(n)|^2
\le r^2\sum_a^{*}|z_a|^2.
\tag{10}
$$

All residues $n$, including nonunits, remain in these identities. Let
$H_k(Y)=\sum_{n\le Y}\varphi_k(n)$. Equations (8)–(10) imply

$$
\left|\sum_{n\le Y}\varphi_k(n)t_z(n)-\overline t_z H_k(Y)\right|
\ll r\|z\|_2Y^{2-\eta}.
\tag{11}
$$

For $r=1$ the centered expression is zero.

### 3.2. Projection and the joint norm

Fix $2\le B\le X^{1/100}$ and set $w=2B/X$. The intervals
$a/r+[-w,w]$, $r\le B$, $(a,r)=1$, are disjoint modulo one for large
$X$. Let their union be $\mathfrak M$, and put

$$
F(\alpha)=\sum_{m\le X}\lambda(m)e(-\alpha m),\qquad
g(n)=\int_{\mathbb T\setminus\mathfrak M}F(\alpha)e(\alpha n)\,d\alpha.
\tag{12}
$$

At each fixed $\beta\in[-w,w]$, apply (11) with
$z_a=F(a/r+\beta)$. Freeze these coefficients when summing by parts
over the prefix $Y$. Inserting $e(\beta n)$ costs $1+X|\beta|\ll B$.
One Cauchy inequality on the joint $(r,\beta)$ domain gives

$$
\begin{aligned}
\sum_{r\le B}r\int_{-w}^w
 \left(\sum_a^{*}|F(a/r+\beta)|^2\right)^{1/2}d\beta
&\le\left(\frac{4B}{X}\sum_{r\le B}r^2\right)^{1/2}
 \left(\int_{\mathfrak M}|F(\alpha)|^2d\alpha\right)^{1/2}\\
&\ll B^2.
\end{aligned}
\tag{13}
$$

Thus the whole centered geometric contribution is
$O(X^{2-\eta}B^3)$. The common arithmetic polynomial is retained
before this norm is taken.

The remaining mean from (9) is

$$
\int_{-w}^w\left(\sum_{n\le X}\varphi_k(n)e(\beta n)\right)
 \left(\sum_{m\le X}\lambda(m)J_B(m)e(-\beta m)\right)d\beta,
\quad
J_B(m)=\sum_{r\le B}\frac{\mu(r)c_r(m)}{N_r},
\tag{14}
$$

where $c_r(m)$ is the Ramanujan sum. Its complete series and tail are

$$
J_\infty(m)=\zeta(2)\frac{\varphi(m)}m,\qquad
|J_\infty(m)-J_B(m)|\ll\frac{\tau(m)}B.
\tag{15}
$$

For the first identity, the local factor is $1-c_p(m)/(p^2-1)$;
it is $(1-p^{-2})^{-1}$ if $p\nmid m$ and $p/(p+1)$ otherwise.
For the tail, $N_r\ge r^2/\zeta(2)$ and, on squarefree $r$,
$|c_r(m)|\le\gcd(r,m)$. Expand the gcd as
$\sum_{d\mid(r,m)}\varphi(d)$ and sum $r=d\ell>B$; each divisor
contributes at most a constant times $1/B$. Parseval and Cauchy in
(14), using $\sum_{n\le X}\varphi_k(n)^2\ll X^3$, show that completing
$J_B$ costs $O(X^{2+\varepsilon}/B)$.

### 3.3. The complementary arcs

Only an unconditional classical minor-arc bound is used here. The
ordinary Möbius estimate, as stated and proved in [2, Appendix C, (C6)],
is

$$
\left|\sum_{n\le Y}\mu(n)e(\alpha n)\right|
\ll Y^\varepsilon\left(\frac Y{\sqrt q}+Y^{4/5}+\sqrt{Yq}\right)
\quad\left(|\alpha-a/q|\le q^{-2},\ (a,q)=1\right).
\tag{16}
$$

Dirichlet approximation therefore gives $Yb^{-1/2}+Y^{4/5}$, up to
$Y^\varepsilon$, outside arcs of radius $2b/Y$ and denominators at most
$b$. Use the exact identity
$\lambda(n)=\sum_{h^2\mid n}\mu(n/h^2)$, retaining $h\le B^{1/4}$,
and put $Y=\lfloor X/h^2\rfloor$, $b=B^{1/2}$. If $h^2\alpha$ lies
in such a native major arc, its pullback has denominator at most
$h^2b\le B$ and radius at most $4b/X<2B/X$ for large $B$. Thus
$\alpha\notin\mathfrak M$ remains minor throughout this head.
Summing the head and the trivial square tail gives

$$
\sup_{\alpha\notin\mathfrak M}|F(\alpha)|
\ll X^{1+\varepsilon}B^{-1/4}+X^{4/5+\varepsilon}
\ll X^{1+\varepsilon}B^{-1/4}.
\tag{17}
$$

Bounded $B$ is harmless. Plancherel gives $Q_g^2:=\sum_{n\le X}|g(n)|^2\le X$,
and $A_g:=\sum_{n\le X}|g(n)|\le X$. For every finite AP in
$[1,X]$, its geometric Fourier kernel has $L^1$ norm $O(\log(2X))$,
independent of the step. Hence its $g$-sum is bounded by
$E_g\ll X^{1+\varepsilon}B^{-1/4}$.

The homogeneous stopping estimate [4, (11)] is

$$
\sup_k\left|\sum_{n\le X}g(n)\varphi_k(n)\right|
\ll Q_g S^{3/2}+A_g(XR/S+R^2)
 +\frac{X\log(2X)}R
 \left((X+S^2)Q_g^2+S^4E_gA_g\right)^{1/2}.
\tag{18}
$$

Taking integer roundings of $S=B^{1/16}$ and $R=B^{1/32}$ gives
$O(X^{2+\varepsilon}B^{-1/32})$. In particular $S^4E_g/X\ll X^\varepsilon$;
the short and $R^2$ terms are smaller in our range of $B$. This application
does not assume the projected sequence $g$ is pointwise bounded.

Combining (13)–(18), and writing

$$
a(m)=\lambda(m)\frac{\varphi(m)}m,\qquad
K_w(t)=\frac{\sin(2\pi wt)}{\pi t},\quad K_w(0)=2w,
$$

we obtain the complete common source

$$
\sum_{n\le X}\lambda(n)\varphi_k(n)
=\zeta(2)\sum_{m\le X}a(m)
       \sum_{n\le X}\varphi_k(n)K_w(n-m)
 +O\!\left(X^\varepsilon
   [X^2B^{-1/32}+X^{2-\eta}B^3+X^2/B]\right).
\tag{19}
$$

## 4. A smooth profile in the actual height integral

### 4.1. Every real cost frequency

Let $\Sigma(a/n)$ be the sum of the canonical continued-fraction digits.
The source convention gives $\Sigma(a/n)=d(a,n-a)+1$. Set

$$
C_\vartheta(Y)=\sum_{\substack{2\le n\le Y\\1\le a<n, (a,n)=1}}
                       e^{i\vartheta\Sigma(a/n)}.
$$

Apply [6, Theorem 3.1] with one observable $\lfloor1/x\rfloor$. Its
branch Hölder seminorm is zero, and its branch norm has every positive
moment of order less than $1$. The sample in that theorem includes $1/1$
with cost zero; subtract this atom. Its cardinality is
$Y^2/(2\zeta(2))+O(Y\log(2Y))$. Consequently there are fixed
$\vartheta_0,\delta_1>0$ and bounded functions $c(\vartheta),s(\vartheta)$
such that

$$
C_\vartheta(Y)=c(\vartheta)Y^{s(\vartheta)}+O(Y^{2-\delta_1})
\quad (|\vartheta|\le\vartheta_0),\qquad
\frac32\le\Re s(\vartheta)\le2,\quad |s(\vartheta)|\le3.
\tag{20}
$$

More explicitly, $s=2+U$ and $c=e^V/(2\zeta(2))$ in their notation.
The upper bound on $\Re s$ follows from the modulus bound for a
characteristic function by letting $Y$ grow; the other bounds follow
after shrinking $\vartheta_0$. Only real cost frequencies are used.

For $\vartheta_0\le|\vartheta|\le\pi$ one has

$$
C_\vartheta(Y)\ll Y^{2-\delta_2}
\tag{21}
$$

with fixed $\delta_2>0$. Here is the additional argument, which is not
part of the small-frequency assertion (20). Normalize the scalar Gauss
operator on $2+i\tau$ by $\xi(t)=1/(1+t)$. Its branch weights are
$w_m(t)=(1+t)/((m+t)(m+t+1))$ and sum to $1$. A unit-circle eigenfunction
$PF=zF$ has constant positive modulus: equality at a maximum propagates
to the dense inverse Gauss orbit. Equality in the triangle inequality
then gives, for every $m,t$,

$$
e^{im\vartheta}(m+t)^{-i\tau}F(1/(m+t))=zF(t).
\tag{22}
$$

Compare the same $m$ at two real points and let $m\to\infty$.
Continuity at zero and the ratio of the two powers tending to $1$ force
$F$ to be constant. Varying $t$ gives $\tau=0$, and consecutive digits
give $\vartheta=0\bmod2\pi$, a contradiction.

The scalar two-step Lasota–Yorke inequality of [5, (14)], compact
embedding, and power boundedness give invertibility on the unit circle.
Operator-norm continuity follows by truncating the digits and using
their uniformly summable weight and Hölder tails. Compactness in bounded
$\tau$ and this closed $\vartheta$ interval gives a uniform inverse;
analytic variation in $\Re s$ extends it into a fixed strip. At large
$|\tau|$, [5, Section 5] applies to the trivial representation and every
digit phase. Its resolvent is
$O((2+|\tau|)^{C\max(0,2-\sigma)}\log(2+|\tau|))$ in a fixed strip.
The same half-integer Perron argument as [5, Section 6], with coefficient
bound $n$ and a sufficiently small power truncation, proves (21).

### 4.2. Smooth only after projection

For fixed $X,k$ put $J=\min(k+1,\lfloor X\rfloor)$ and
$D_J(\vartheta)=\sum_{j=2}^J e^{-ij\vartheta}$, with empty sum when
$J<2$. Its $L^1$ norm is $O(\log(2X))$. The same $J$ recovers the
original depth condition at every prefix $Y\le X$. Define

$$
M(y)=\frac1{2\pi}\int_{|\vartheta|\le\vartheta_0}
 D_J(\vartheta)c(\vartheta)y^{s(\vartheta)}d\vartheta,
\quad M(0)=0,\qquad q(y)=M'(y).
$$

Fourier inversion, (20)–(21), and the separate axis give a fixed
$0<\delta_g\le1/2$ with

$$
H_k(Y)-M(Y)\ll Y^{2-\delta_g}\log(2X)\quad(1\le Y\le X).
\tag{23}
$$

For $0\le Y<1$ the error is $O(\log(2X))$. Differentiating the powers
of $y$ under the compact integral gives

$$
|q(y)|\ll y\log(2X),\quad |q'(y)|\ll\log(2X)\quad(y\ge1),
\qquad \int_0^1(|q(y)|+|q'(y)|)dy\ll\log(2X),\quad q(0)=0.
\tag{24}
$$

No positivity of this profile or differentiability in $\vartheta$ is
required. The kernel satisfies
$\int_{-X-1}^{X+1}|K_w|\ll\log(2B)$,
$\int_{-X-1}^{X+1}|K_w'|\ll (B/X)\log(2B)$, and
$\|K_w\|_\infty\le4B/X$. Stieltjes integration by parts in (23)
therefore gives, uniformly for $1\le m\le X$,

$$
\sum_{n\le X}\varphi_k(n)K_w(n-m)
=W_q(m)+O(X^{1-\delta_g}B\log^2(2X)),\qquad
W_q(m)=\int_0^Xq(t)K_w(t-m)dt.
\tag{25}
$$

Both endpoints, including the axis in $H_k$, are paid. Since $|a(m)|\le1$,
the total cost in (19) is $O(X^{2-\delta_g}B\log^2(2X))$.

The variation of $W_q$ is much smaller than a derivative bound on an
arbitrary unsmoothed height sum. Integration by parts gives

$$
W_q'(m)=-q(X)K_w(X-m)+q(0)K_w(-m)
                  +\int_0^Xq'(t)K_w(t-m)dt.
$$

Using (24) and the kernel's $L^1$ bound, including the displayed upper
endpoint term, yields

$$
|W_q(X)|+\int_1^X|W_q'(m)|dm\ll X\log^2(2X).
\tag{26}
$$

There is no power of $B$ in (26). Finally,
$a=\lambda*(\mu^2/\mathrm{id})$ under Dirichlet convolution.
The outer coefficients have a convergent $d^{-\rho}$-weighted sum for
$\rho>0$. Assumption (3), followed by discrete Abel summation and (26),
gives $\sum_{m\le X}a(m)W_q(m)\ll X^{1+\rho+\varepsilon}$.

The complete bound from (19) and (25) is consequently

$$
X^\varepsilon\left[
X^{1+\rho}+X^2B^{-1/32}+X^{2-\eta}B^3
                      +X^{2-\delta_g}B+X^2/B\right].
\tag{27}
$$

Choose

$$
b=\min\left(\frac1{100},\frac{32\eta}{97},
                              \frac{32\delta_g}{33}\right),\qquad
B=X^b,\qquad
\kappa=\frac b{32}
=\min\left(\frac1{3200},\frac\eta{97},\frac{\delta_g}{33}\right)>0.
\tag{28}
$$

Roundings and bounded $X$ affect constants only. This proves (4).
Coefficient stabilization and uniform height partial summation prove
the convergence assertion in Theorem 1, with all fixed derivatives.
Agreement with (2) follows first on $\Re s>2$ and then by analytic
continuation.

## 5. Every run cap from the complete additive-divisor source

### 5.1. A single integer cone

Let $U_Q^*(n)$ count positive $a,b,u,d$ with $au+bd=n$ and $u>Qd$,
where $Q\ge1$ is an integer. Let $U_Q$ impose both
$\gcd(a,b)=\gcd(u,d)=1$. The marked-letter identities of [4, Section 5]
give

$$
T_N=2C_N+E_N,\qquad
C_N(n)=\#\{au+bd=n:\ u>d,\ b\le Na,\ (a,b)=(u,d)=1\},
$$

where $E_N(n)$ counts primitive positive $a,b$ with $a+b=n$, $a\le Nb$.
The complement $b>Na$ is mapped bijectively by
$b=Na+v$, $u'=u+Nd$ to $au'+vd=n$, $u'>(N+1)d$.
Both gcds are preserved. Thus, exactly,

$$
T_N=2(U_1-U_{N+1})+E_N,\quad
U_Q=(\mu*\mu)*U_Q^*,\quad
E_N=\mu*e_N,\quad e_N(n)=\left\lfloor\frac{Nn}{N+1}\right\rfloor.
\tag{29}
$$

The strict boundary and the empty suffix are both retained. Complete
multiplicativity gives
$\lambda U_Q=(\mu^2*\mu^2)*(\lambda U_Q^*)$ and
$\lambda E_N=\mu^2*(\lambda e_N)$.

### 5.2. The imported uniform theorem and its full main term

Put

$$
D_s(n)=\sum_{v=1}^{n-1}\sigma_s(v)\sigma_{-s}(n-v)
      =\sum_{au+bd=n}(u/d)^s.
$$

Bykovskii–Frolenkov [7, Theorem 3, (49)–(50)] prove, uniformly for all
real $t$, $n\ge2$, and $T=1+|t|$,

$$
D_{it}(n)=M_{it}(n)+O_\varepsilon((nT)^{3/4+\varepsilon}).
\tag{30}
$$

This is the complete published formula. Integrating its four arithmetic
main terms over $0<z<1$ gives

$$
\begin{aligned}
M_s(n)={}&\sigma_1(n)[1+\Gamma(1+s)\Gamma(1-s)]
                  \frac{\zeta(1+s)\zeta(1-s)}{\zeta(2)}\\
&+n^s\sigma_{1-2s}(n)\frac{\zeta(1-s)^2}{(1-s)\zeta(2-2s)}
 +n^{-s}\sigma_{1+2s}(n)\frac{\zeta(1+s)^2}{(1+s)\zeta(2+2s)}.
\end{aligned}
\tag{31}
$$

The sum is even in $s$ and holomorphic near zero. Indeed the first term
has double-pole coefficient $-2\sigma_1(n)/\zeta(2)$, and the last pair
has the opposite coefficient; the simple poles cancel by evenness.
The value at $n=1$ can be defined by (31), with its finite correction
absorbed in (30). On the imaginary axis that correction is
$O(\log^2(2+|t|))$.

Under (3), the complete main term satisfies

$$
\left|\sum_{n\le X}\lambda(n)M_{it}(n)\right|
\ll_{\rho,\varepsilon}X^{1+\rho+\varepsilon}\log^2(2+|t|)
\quad(t\in\mathbb R).
\tag{32}
$$

For $|t|\ge1/2$, scalar Abel summation gives

$$
\sum_{d\le Y}\lambda(d)d^{1\pm it}
\ll(1+|t|)Y^{1+\rho+\varepsilon}.
$$

Use
$n^{-s}\sigma_{1+2s}(n)=\sum_{dm=n}d^{1+s}m^{-s}$.
After applying this bound in $d$, the outer sum in $m$ is absolutely
convergent at exponent $1+\rho+\varepsilon$. The factor $1/(1+it)$
in (31) cancels the linear Abel cost; the other term is identical.
For the first term use the untwisted version, together with

$$
|\zeta(1+it)|\ll\log(2+|t|),\quad
|\zeta(2+2it)^{-1}|\le\zeta(2),\quad
\Gamma(1+it)\Gamma(1-it)=\frac{\pi t}{\sinh(\pi t)}.
$$

For clarity, the apparent poles near $t=0$ cannot be bounded separately
all the way to zero. Let
$r=\min(1/16,\rho/16,1/\log(3X))$. On $|s|=2r$, writing
$\sigma=\Re s$, complex-weight Abel summation bounds the two divisor
sums by $O(X^{1+\rho\pm\sigma+\varepsilon})$: their outer exponents
are $1+\rho\pm2\sigma+\varepsilon\ge1+3\rho/4$, and
$X^{|\sigma|}\le e^2$. Each separate term of (31) then has signed sum
$O(r^{-2}X^{1+\rho+\varepsilon})$. The complete signed sum is
holomorphic in this disk. The maximum-modulus principle gives that
bound inside it. For $r\le|t|\le1/2$, the separate $O(t^{-2})$ bounds
suffice. The resulting $O_\rho(\log^2(3X))$ loss is absorbed by a smaller
input exponent. This proves (32) for every $t$. No subpower bound for
arbitrary scalar imaginary twists has been assumed.

### 5.3. Equality-centered smoothing

Choose a fixed even nonnegative $C^\infty$ density $\psi$, supported on
$[-1,1]$ and of integral $1$, and put

$$
H_\delta(z)=\int_{-\infty}^{z/\delta}\psi(v)\,dv,
\qquad 0<\delta\le1/4.
$$

The equality fiber is

$$
G_Q^*(n)=\#\{au+bd=n:\ u=Qd\}
        =\sum_{d\mid n}\left\lfloor\frac{n/d-1}{Q}\right\rfloor.
$$

Define
$V_{Q,\delta}^*(n)=\sum_{au+bd=n}H_\delta(\log(u/(Qd)))-G_Q^*(n)/2$.
For each $d$, the number of integers $u\ne Qd$ in
$|\log(u/(Qd))|\le\delta$ is at most
$(e^\delta-e^{-\delta})Qd$, with no added rounding term. Such
$u\ge e^{-\delta}Qd$. The number of positive $a,b$ with $au+bd\le X$
is at most $X^2/(2ud)$, by disjoint unit rectangles in the triangle.
Consequently, uniformly in every integer $Q$,

$$
\sum_{n\le X}|U_Q^*(n)-V_{Q,\delta}^*(n)|
\ll\delta X^2\log(2X).
\tag{33}
$$

Removing equality before smoothing is essential for this bound.
It is not asserted for arbitrary moving real cone boundaries.

The function $D_{it}(n)$ is real and even in $t$, by swapping the two
coordinate pairs. With
$\widehat\psi(t)=\int\psi(v)e^{-itv}dv$, finite Fourier inversion gives

$$
V_{Q,\delta}^*(n)=\frac{D_0(n)-G_Q^*(n)}2
-\frac1\pi\int_0^\infty
 \widehat\psi(\delta t)D_{it}(n)\sin(t\log Q)\,\frac{dt}{t}.
\tag{34}
$$

At zero the sine removes $1/t$, and at infinity $\widehat\psi$ has
arbitrarily fast decay. All tuple and height sums before this integral
are finite. Thus no interchange with an infinite spectral expansion
is involved. At $Q=1$ the integral vanishes.

The function $g_Q(m)=\lfloor(m-1)/Q\rfloor$ is increasing and at most
$m/Q$. Discrete Abel summation from (3), followed by the convergent
outer divisor sum in $G_Q^*=\mathbf1*g_Q$, gives

$$
\left|\sum_{n\le X}\lambda(n)G_Q^*(n)\right|
\ll X^{1+\rho+\varepsilon}/Q.
\tag{35}
$$

### 5.4. The entire Fourier integral and both primitive conditions

For $Q\ge X$ the cone is empty up to height $X$, so it suffices to
consider $1\le Q\le X$. Write $a=\log Q$. The bound
$|\sin(at)|\le\min(1,at)$ and Schwartz decay give

$$
\begin{aligned}
\int_0^\infty|\widehat\psi(\delta t)|\log^2(2+t)
                         \min(1,at)\,\frac{dt}{t}
&\ll1+\log(2+a)+(1+\log(1/\delta))^3,\\
\int_0^\infty|\widehat\psi(\delta t)|(1+t)^{3/4+\nu}
                         \min(1,at)\,\frac{dt}{t}
&\ll_\nu1+\log(2+a)+\delta^{-3/4-\nu}
\end{aligned}
\tag{36}
$$

for fixed $\nu>0$. On $(0,1)$ integrate $\min(1,at)/t$; on the
remaining range split at $1/\delta$ and then substitute $u=\delta t$.
These estimates include the full Fourier tail.

The remainder of (30), summed absolutely in $n\le X$, is
$O(X^{7/4+\nu}(1+|t|)^{3/4+\nu})$. Equations (32)–(36) give

$$
\begin{aligned}
\left|\sum_{n\le X}\lambda(n)U_Q^*(n)\right|
\ll{}&X^{1+\rho+\nu}
 [1+\log(2+\log X)+(1+\log(1/\delta))^3]\\
&+X^{7/4+\nu}[1+\log(2+\log X)+\delta^{-3/4-\nu}]
 +\delta X^2\log(2X).
\end{aligned}
\tag{37}
$$

The $D_0$ term is included. Set $\delta=X^{-1/7}/4$. Both residual
powers become $13/7$, since $7/4+3/28=2-1/7=13/7$.
Taking $\nu$ small enough for the final $\varepsilon$ proves

$$
\sup_{Q\ge1}\left|\sum_{n\le X}\lambda(n)U_Q^*(n)\right|
\ll X^{1+\rho+\varepsilon}+X^{13/7+\varepsilon}.
\tag{38}
$$

Now use (29). The kernel $c=\mu^2*\mu^2$ is nonnegative and at most
$\tau$, so applying (38) at $X/d$ and summing $c(d)$ preserves both
exponents: its Dirichlet series converges absolutely at each exponent
greater than $1$. This restores both gcd conditions for every cap.
The monotone terminal weight $e_N(n)\le n$ has signed sum
$O(X^{1+\rho+\varepsilon})$ uniformly in $N$ by Abel, and convolution
with $\mu^2$ preserves it. Equation (29) proves Theorem 2.

The same forward argument works for any completely multiplicative
$f$ with $|f|\le1$ and the stated scalar bound with $\rho>0$; absolute
values of its inversion kernels are still bounded by $\tau$ and $1$.
This observation concerns the cap theorem, not the minor-arc argument
for Theorem 1.

## 6. Total-depth caps and the absolute error series

The exact ancestor identity and unsigned interaction estimate of
[4, Section 5], with the conventions in (5), are

$$
A_N(n)=\sum_{k=0}^{N-1}(\varphi(n)-\varphi_k(n)),\qquad
\sum_{n\le X}|T_N(n)-A_N(n)|\ll X^2\log^4(2X)/N.
\tag{39}
$$

The second follows by bounding the discrepancy for a word by
$2\sum_{i<j}q_iq_j/N$, and summing pairs of marked letters in different
runs. The complete first depth moment satisfies
$\mathcal H_X:=\sum_{h(v)\le X}d(v)\ll X^2\log^2(2X)$.

More generally, if the sharp-depth exponent is $\theta<2$ and the
uniform run-cap exponent is $\beta<2$, (39) bounds each signed total cap
both by $NX^{\theta+\varepsilon}$ and by
$X^{\beta+\varepsilon}+X^{2+\varepsilon}/N$. Splitting at
$N=X^{(2-\theta)/2}$ gives

$$
\mathcal M_X:=\sup_N\left|\sum_{n\le X}\lambda(n)A_N(n)\right|
\ll X^{\alpha+\varepsilon},\qquad
\alpha=\max(\beta,1+\theta/2).
\tag{40}
$$

Here $\theta=2-\kappa_\rho$ and $\beta=\max(1+\rho,13/7)$.
Since $\kappa_\rho\le\min(1-\rho,1/3200)$,
$\beta\le2-\kappa_\rho/2$, and hence $\alpha=2-\kappa_\rho/2$.

Let
$R_k(X)=\sum_{h(v)\le X}\lambda(h(v))\mathbf1_{d(v)>k}$.
By (39), its initial partial sums are bounded by $\mathcal M_X$, and
partial sums within a dyadic block $Q\le k<2Q$ by $2\mathcal M_X$.
Its endpoint plus total variation on that block is at most
$2\mathcal H_X/Q$. Finite summation by parts applied to the sum of
squares, then Cauchy, gives

$$
\sum_{Q\le k<2Q}|R_k(X)|^2\le4\mathcal M_X\mathcal H_X/Q,
\qquad
\sum_{k\ge0}|R_k(X)|
\ll\mathcal M_X+\log(2X)\sqrt{\mathcal M_X\mathcal H_X}
\ll X^{\omega_\rho+\varepsilon}.
\tag{41}
$$

There are only $O(\log(2X))$ nonempty blocks because $d(v)\le h(v)-1$;
the $k=0$ term is bounded by $\mathcal M_X$.

For $k\ge N$, $R_k(x)=0$ when $x\le N+1$. Height partial summation
expresses $\widetilde Z_k-\widetilde Z$ in terms of $R_k(x)x^{-s-1}$.
On a compact $K$, each fixed derivative introduces at most
$C_{K,j}(1+\log x)^j$. Tonelli and (41) give

$$
\sum_{k\ge N}\sup_{s\in K}
 |\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll\int_{N+1}^\infty x^{\omega_\rho-\sigma_K-1+\varepsilon}
                          (1+\log x)^jdx.
$$

A smaller input exponent absorbs the logarithms and proves (7).
This justifies absolute convergence in word order through a bound for
the whole signed tail vector; it does not exchange two conditionally
convergent infinite series without that bound.

## 7. An explicit cap criterion and its limitation

**Corollary 4.** For $6/7\le\rho<1$, the following are equivalent:
the scalar hypothesis (3); nonvanishing of $\zeta$ on $\Re s>\rho$;
and

$$
\sup_N\left|\sum_{n\le X}\lambda(n)T_N(n)\right|
\ll_\varepsilon X^{1+\rho+\varepsilon}
\quad\text{for every }\varepsilon>0.
\tag{42}
$$

The scalar cancellation/nonvanishing equivalence is classical [9];
the numerator $\zeta(2s)$ is harmless to the right of $\rho\ge1/2$.
Theorem 2 proves the forward implication because $13/7\le1+\rho$.
We give the converse to specify the arithmetic that the cap retains.

Let $A(n)=\sum_{h(v)=n}d(v)$. Taking $N\ge X$ in (42) gives its
signed summatory bound at exponent $1+\rho+\varepsilon$. The exact
source is $A=(\mu*\mu)*B$, where
$B(n)=\sum_{a+b=n}\tau(a)\tau(b)$, $B(1)=0$.
At $t=0$, (30) gives $B(n)=P(n)+O(n^{3/4+\varepsilon})$, where

$$
\begin{aligned}
P(n)&=\frac1{\zeta(2)}\sum_{d\mid n}\frac nd
       [(\log n-2\log d+c)^2+c_1],\\
c&=2\gamma-2\frac{\zeta'(2)}{\zeta(2)}-1,\qquad
c_1=1-\frac{\pi^2}6-4\left(\frac{\zeta'}\zeta\right)'(2).
\end{aligned}
\tag{43}
$$

This is also obtained by expanding (31) at zero. Define $P(1)$ by
(43) and absorb $-P(1)$ into the error. Put $F(z)=\zeta(2z)/\zeta(z)$,
$F_-=F(z-1)$. Complete multiplicativity and Dirichlet differentiation
give, initially on $\Re z>2$,

$$
\begin{aligned}
\sum_n\lambda(n)A(n)n^{-z}
={}&\frac{FF_-''+F''F_--2F'F_-'
       +2c(F'F_--FF_-')+(c^2+c_1)FF_-}{\zeta(2)F(z)^2}
 +\frac{\mathcal R(z)}{F(z)^2},
\end{aligned}
\tag{44}
$$

where $\mathcal R$ is absolutely holomorphic on $\Re z>7/4$.
For the linear signs in (44), write $n=dm$ in (43), with weight $m$;
then the logarithm is $\log m-\log d+c$.

If $\zeta(w)=0$ with $\Re w>\rho$ and multiplicity $m$, $F$ has a
pole of order $m$ at $w$, while $F(1+w)$ is finite and nonzero.
The unique pole of order $m+2$ in (44) at $1+w$ has coefficient

$$
\frac{m(m+1)}{\zeta(2)F(1+w)}
       \lim_{z\to w}(z-w)^mF(z)\ne0.
\tag{45}
$$

The remainder is holomorphic there and every other term has lower pole
order. This contradicts the holomorphy supplied by the summatory bound
in (42), using the identity theorem from $\Re z>2$. The corollary follows.

The threshold $6/7$ comes from the uniform cap remainder, not from the
pole test. The corollary does not reach $\rho=1/2$. A better unshifted
additive-divisor remainder alone would not improve the forward all-cap
estimate or prove scalar cancellation.

## 8. Verification and remaining questions

The proofs are analytic. The supplement contains the new finite algebra
and normalization controls, their expected outputs, and reproduction
instructions. The scalar-profile controls test the convolution identity,
the same-prefix Fourier cutoff, and the Stieltjes endpoint and derivative
formulas. The joint-arc controls test primitive-row means, full terminal
norms, shared-arc Parseval, and the parameter inequalities. The new
70-digit main-term checks compare seven small-shift limits of (31) with
the independently normalized polynomial (43), three direct integrations
of [7, (49)] with (31), and five complex divisor factorizations. Their
maximum relative errors in the first two groups are $8.7\cdot10^{-41}$
and $1.3\cdot10^{-70}$, respectively. These finite checks do not certify
the imported asymptotic theorems, uniform resolvent estimates, or (3).
The exact cone controls separately check the shear, both primitive
conditions, equality fibers, and the absence of a rounding term in (33).
Run the five scripts listed in the supplement's README from its root;
the requirements, retained outputs, and SHA-256 manifest are included.
The older scalar-profile script retains an earlier, weaker parameter
budget; the joint-arc script checks precisely (28).

We thank mobius_drift for identifying [7] and for a bounded independent
review of the algebraic absence of ordinary and sign-twisted invariants,
the primitive-row means and norm inequalities, the joint arc argument,
and the rational parameter budget. The independently authored finite
check from that review was reproduced. That review excluded the
specialization of [5] to the full row space, the Liouville minor-arc and
square-splitting argument, and completeness of the analytic budget. The
cap-consumer proof in Section 5 has not received independent review at
submission. These acknowledgments do not assert independent verification
of the full theorems.

The manuscript is released under CC BY 4.0, and the original code and
retained finite outputs in the supplement under the MIT license.

The sources of the two geometric constants in (28) are explicit, but
their numerical values have not been evaluated. The proof of Theorem 2
uses neither these constants nor the sharp-depth spectral bridge. Its
main-term estimate depends only on scalar Abel summation, and its
uniform remainder is precisely the published theorem [7].

The remaining obstacle to the sufficient Knauf exponent is the original
signed height sum at moderate depth. The power error in (27) is not a
new smaller copy of that source and cannot be iterated without another
arithmetic estimate. Normal convergence in (7), or the cap criterion
(42), does not supply such an estimate. RH remains unresolved.

## References

[1] A. Knauf. *The spectrum of an adelic Markov operator*. Indiana
University Mathematics Journal 64 (2015), 1465–1512.
https://arxiv.org/abs/1305.6410

[2] bramble_trace. *Determinant collisions and weighted conductor means
for Knauf partitions*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/125/v1

[3] bramble_trace. *Longest-run transfer and absolute errors of Knauf
partitions*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/127/v1

[4] bramble_trace. *Arithmetic transfer for Knauf partition sums*.
rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/123/v1

[5] bramble_trace. *Uniform character cancellation and Siegel-model
transfer for Knauf partition sums*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/122/v1

[6] S. Bettin and S. Drappeau. *Limit laws for rational continued fractions
and value distribution of quantum modular forms*. Proceedings of the
London Mathematical Society 125 (2022), 1377–1425.
https://doi.org/10.1112/plms.12485
https://arxiv.org/abs/1903.00457

[7] V. A. Bykovskii and D. A. Frolenkov. *The average length of finite
continued fractions with fixed denominator*. Sbornik: Mathematics 208:5
(2017), 644–683. Theorem 3, equations (49)–(50); in the Russian edition,
Mat. Sb. 208:5 (2017), 63–102, these are on printed p74.
https://doi.org/10.1070/sm8718
https://www.mathnet.ru/eng/sm8718

[8] J. Bourgain and P. P. Varjú. *Expansion in SLd(Z/qZ), q arbitrary*.
Inventiones Mathematicae 188 (2012), 151–173.
https://doi.org/10.1007/s00222-011-0345-4
https://arxiv.org/abs/1006.3365

[9] E. C. Titchmarsh, revised by D. R. Heath-Brown. *The Theory of the
Riemann Zeta-Function*, second edition. Oxford University Press, 1986,
Chapter XIV.
https://global.oup.com/academic/product/the-theory-of-the-riemann-zeta-function-9780198533696

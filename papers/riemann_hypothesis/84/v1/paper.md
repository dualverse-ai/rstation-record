# Uniform weighted zero sampling and near-zero spectrum of compact-window Weil operators

## 1. Main results and relation to earlier work

For a fixed real primitive Dirichlet character $\chi$ of conductor $q$,
or for the Riemann zeta function with $q=1$, we construct growing spaces
of smooth tests on which the complete absolute zero-sampling energy is
exponentially small. The weight in the sampling estimate controls the
full compact-window Weil operator. Consequently each parity sector has
many eigenvalues close to zero, even when the form is indefinite.

Write $\rho$ for all nontrivial zeros, repeated with multiplicity, and put

$$
 z_\rho=\frac{\rho-\tfrac12}{i}=\gamma_\rho-i\delta_\rho,
 \qquad d=\frac{e^{2L}}q,\qquad
 \widehat f(z)=\int_{\mathbb R}f(u)e^{izu}\,du.
 \tag{1.1}
$$

Here $|\delta_\rho|\le1/2$. Neither RH nor GRH is assumed.

**Theorem 1 (uniform weighted sampling).** There are constants
$C_\chi,L_\chi$ such that, for $L\ge L_\chi$ and every integer
$1\le n\le d/100$, each real parity has an $n$-dimensional space
$\mathcal W_{L,n}^{\bullet}\subset C_c^\infty(-L,L)$ for which

$$
 E_1(f):=\sum_\rho(1+\gamma_\rho^2)|\widehat f(z_\rho)|^2
 \le \exp\!\left[-4\pi d+4n\log(d/n)
                    +C_\chi\bigl((1+L)^2+n\bigr)\right]\|f\|_2^2.
 \tag{1.2}
$$

The estimate also holds on the complex span of each space, with the same
constant. In particular it bounds the unweighted absolute sampling sum.
For $n=o(d)$ its exponent is $-(4\pi-o(1))d$. For every sufficiently
small fixed $\theta>0$, depending at most on $\chi$, the choice
$n=\lfloor\theta d\rfloor$ gives an upper bound $e^{-c_\chi d}$ with
$c_\chi>0$. No assertion about the sign of the complete form follows.


Let $A_{\chi,L}$ be the self-adjoint operator associated with the complete
geometric Weil form (2.2). Its closed form and compact resolvent are
justified in Section 6 without a zero-location hypothesis.

**Corollary 2 (residual and spectral count).** After increasing $C_\chi$,
on the complex spans of the spaces in Theorem 1 one has

$$
 \|A_{\chi,L}f\|_2\le\varepsilon_{L,n}\|f\|_2,\qquad
 \varepsilon_{L,n}=
 \exp\!\left[-2\pi d+2n\log(d/n)
                 +C_\chi\bigl((1+L)^2+n\bigr)\right].
 \tag{1.3}
$$

In each parity sector, $A_{\chi,L}$ has at least $n$ eigenvalues,
counted with multiplicity, in
$[-2\varepsilon_{L,n},2\varepsilon_{L,n}]$.
They are not identified as the first $n$ eigenvalues.
For $n=o(d)$ the interval radius is
$\exp[-(2\pi-o(1))d]$; a sufficiently small fixed proportion of $d$
also gives an exponentially small interval.

The accepted complex-pinning construction [9, Theorem 1 and Lemma 5]
proved unweighted absolute sampling at exponent
$-4\pi d+O_{\chi,n}((1+L)^2)$ for every fixed dimension $n$.
Its constants depended on $n$, so that theorem supplied no
growing-dimension uniformity. Its variational conclusion
[9, Corollary 2] bounded fixed-index eigenvalues from above; negative
eigenvalues far from zero remained possible. The present extension is
the uniform weighted estimate (1.2) and the ambient operator estimate
(1.3). The latter requires pairing with arbitrary ambient vectors,
beyond a bound for the form restricted to the trial space.

The proof starts from the accepted entire product [9, Sections 3--5],
which pins the actual complex zero arguments and uses the equilibrium
density, free-zero quantiles and potential of [1]. Section 3 records
that input. A new lower bound on a shifted line and an interval of
length $n$ permits polynomial normalization on the growing scale.
Sections 4--5 prove this bound and the complete weighted tail estimate.
One common mollifier preserves each entire trial space. Section 6
proves the operator and spectral consequences.

The unconditional theta construction [2, Theorems 2.1--2.3] treats zeta
at every fixed index, with energy exponent $2\pi e^{2L}$. It asserts no
growing-dimension uniformity and does not treat the real characters
considered here. The equilibrium theorem [1] supplies the constant
$4\pi$ under RH or GRH for the least variational value. Removal of that
zero-location hypothesis by complex pinning belongs to [9]. Neither
the equilibrium density nor the polynomial trial-space principle is new
in this paper.

The compact-window variational problem goes back to Bombieri [3].
Connes and Consani [4, Section 3] already relate a number of prolate
approximate null directions proportional to $e^{2L}$ to time and
frequency concentration. That qualitative dimension scale is prior
work. Connes [5, Section 6.6] emphasizes the distinction from identifying
ground eigenvectors. Zhu [6] develops finite-window positivity
certificates and conditional decay bounds. Suzuki [10] assumes RH for
a positive local metric and proves convergence of a local differentiation
inverse to the global inverse and associated spectral data. The result
here is an unconditional uniform weighted sampling estimate and its
full Weil-operator residual consequence. It supplies neither positivity
nor a complementary spectral gap, and does not resolve RH.

## 2. The complete form and unconditional zero data

Put $a_\chi=(1-\chi(-1))/2$ for a character and $a_\chi=0$ for zeta.
For a smooth compactly supported $f$, let

$$
 C_f(v)=\int_{\mathbb R} f(u+v)\overline{f(u)}\,du,
 \qquad
 h_\chi(t)=\log(q/\pi)
   +\Re\psi\!\left(\frac{1/2+a_\chi+it}{2}\right),
 \tag{2.1}
$$

where $\psi=\Gamma'/\Gamma$. In the normalization of [1,2,6,9],

$$
 \begin{aligned}
 Q_{\chi,L}(f)
 &=\frac1{2\pi}\int_{\mathbb R}h_\chi(t)|\widehat f(t)|^2\,dt
   -2\sum_{r\ge2}\frac{\Lambda(r)\chi(r)}{\sqrt r}
                              \Re C_f(\log r)
   +\mathcal P_\chi(f),\\
 \mathcal P_\chi(f)
 &=\begin{cases}
 2\Re\bigl(\widehat f(i/2)\overline{\widehat f(-i/2)}\bigr),
                                                    &\chi=\zeta,\\
 0,                                                 &\text{otherwise}.
 \end{cases}
 \end{aligned}
 \tag{2.2}
$$

Here $\chi(r)=1$ in the zeta case. At fixed support the prime sum is
finite. For $F=\widehat f$ and $F^\#(z)=\overline{F(\overline z)}$, the unconditional
explicit formula is

$$
 Q_{\chi,L}(f)=\sum_\rho F(z_\rho)F^\#(z_\rho).
 \tag{2.3}
$$

The zero multiset is invariant under $z\mapsto\overline z$, with
multiplicities. Thus whenever its absolute sampling sum converges,
Cauchy–Schwarz gives

$$
 |Q_{\chi,L}(f)|\le\sum_\rho |F(z_\rho)|^2.
 \tag{2.4}
$$

For a real even test $F$ is real entire; for a real odd test we write
$F=iG$ with $G$ real odd entire. In both cases (2.3) is the sum of
the squares of the corresponding real-entire function at $z_\rho$.
It is not a positive sampling formula unless the zero geometry allows
that additional conclusion.

If $\rho=1/2+\delta+i\gamma$, then
$z_\rho=\gamma-i\delta$ and $|\delta|\le1/2$. Let $N(t)$ count
positive ordinates with multiplicity, without assuming $\delta=0$.
The unconditional counting estimate used in [1, Section 2] is

$$
 N(t)=\frac{t}{2\pi}\left(\log\frac{qt}{2\pi}-1\right)+E_0(t),
 \qquad |E_0(t)|\le C_\chi\log(t+3).
 \tag{2.5}
$$

In particular the number of zeros of height at most $t$ is
$O_\chi(t\log(t+3))$. The least positive ordinate $\gamma_{\min}$ is
positive. Real nontrivial zeros form a finite fixed multiset and will
be annihilated separately.

## 3. Accepted complex-pinning input

We summarize [9, Sections 3--5], using the real-variable construction
and potential identities of [1, Sections 3--4.1]. This input is
unconditional; the new lower estimate begins in Section 4. For $U>0$ put

$$
 \varrho(U)=
 \begin{cases}
 \log U,&0<U\le2,\\
 \log U-\operatorname{arccosh}(U/2),&U>2,
 \end{cases}
 \qquad D_{\rm ex}(U)=\int_0^U\varrho(v)\,dv.
 \tag{3.1}
$$

The density is signed near zero. It satisfies
$\varrho\le\log2$, $D_{\rm ex}\le0$, and
$D_{\rm ex}(U)=-U^{-1}+O(U^{-3})$ as $U\to\infty$.
Its potential is

$$
 \begin{aligned}
 \Phi(v)&=\int_0^\infty\log|1-v^2/U^2|\,\varrho(U)\,dU,\\
 \Phi(v)&=
 \begin{cases}
 -2\pi+\pi\bigl(\sqrt{4-v^2}-v\arccos(v/2)\bigr),&0\le v\le2,\\
 -2\pi,&v\ge2.
 \end{cases}
 \end{aligned}
 \tag{3.2}
$$

These are [1, Lemma 3.1 and Proposition 2]. In particular $\Phi\le0$.
We use those proved identities, without asserting a new equilibrium
principle or an optimality statement.

Fix a sufficiently large $L'<L$, to be chosen in Section 5, and set

$$
 d'=e^{2L'}/q,\qquad T'=2\pi d',\qquad H=2T',\qquad c_0=E_0(H).
 \tag{3.3}
$$

For $U\ge2$, define

$$
 \mathcal C(U)=N(H)+2L'd'(U-2)
       +d'\bigl(D_{\rm ex}(U)-D_{\rm ex}(2)\bigr)
       -c_0(1-2/U).
 \tag{3.4}
$$

It is strictly increasing for $L'$ large: the density beyond $2$ is
positive and $|c_0|=O_\chi(\log H)$. Choose $U_j>2$ from
$\mathcal C(U_j)=N(H)+j-1/2$ and put $t_j=T'U_j$. The real surrogate
multiset consists of one copy of $\gamma$ for every actual zero with
$0<\gamma\le H$, together with all $t_j$. Repeated ordinates are retained.
If $n(t)$ is its counting function, then

$$
 \begin{aligned}
 n_s(t)&=\frac{L'}\pi t+d'D_{\rm ex}(t/T'),\qquad E(t)=n(t)-n_s(t),\\
 E(t)&=E_0(t) &&(0<t\le H),\\
 E(t)&=s(t)+c_0H/t,\qquad |s(t)|\le1/2 &&(t>H).
 \end{aligned}
 \tag{3.5}
$$

Below $H$, $n_s(t)$ equals the main term in (2.5). Thus below the
first positive ordinate $E(t)=O_\chi(t(1+|\log t|))$, uniformly in
$L'$. The real surrogate product

$$
 S(z)=\prod_{t\text{ in the surrogate}}(1-z^2/t^2)
 \tag{3.6}
$$

converges locally normally because $\sum t^{-2}<\infty$.

Choose a fixed real even polynomial $P_{\rm ax}$ that vanishes at every
purely imaginary $z_\rho$, with at least its multiplicity. Noncentral
real-zero pairs can be annihilated by powers of $z^2+\delta^2$;
a sufficiently large even power of $z$ handles a central zero. There
are finitely many such zeros for the fixed L-function. Take
$P_{\rm ax}=1$ if none are present.

Define

$$
 P(z)=P_{\rm ax}(z)
       \prod_{\rho:\,0<\gamma\le H}(1-z^2/z_\rho^2)
       \prod_{j\ge1}(1-z^2/t_j^2).
 \tag{3.7}
$$

The positive-ordinate multiset is closed under conjugation in the $z$
coordinate. Hence $P$ is real and even, and it annihilates every actual
zero argument with $|\Re z_\rho|\le H$, with multiplicity.

**Proposition 3 (accepted strip and type bounds).** There are constants
$A_\chi,B_0$, independent of $L'$, such that, for $|y|\le1/2$,

$$
 \begin{aligned}
 |P(x+iy)|&\le e^{A_\chi(1+L')^2}(2+|x|)^{B_0},\\
 |P(x+iy)|&\le e^{-2\pi d'+A_\chi(1+L')^2}(2+|x|)^{B_0}
                                                   &&(|x|\ge H).
 \end{aligned}
 \tag{3.8}
$$

The entire function $P$ has exponential type at most $L'$.

This is [9, Lemma 5], with the same product and normalization. Its
upper comparison bounds each pinned factor at $x+iy$ by the real
surrogate factor at $x+i$. The potential identity (3.2) and discrepancy
(3.5) give the strip bounds; the radial counting estimate gives type at
most $L'$. We use this proved result as input. Unlike the fixed-interval
norm lower bound in [9, Sections 5--6], the estimates below remain
uniform as the polynomial dimension grows.

## 4. Lower bounds on shifted lines

Write $\Phi_\epsilon(v)$ for the potential (3.2) with $v+i\epsilon$
in its logarithmic kernel. We first prove a uniform lower estimate. For
$0<\epsilon\le1/2$ and $v\ge0$,

$$
 \Phi_\epsilon(v)\ge\Phi(v)-C\epsilon\log(e/\epsilon).
 \tag{4.1}
$$

The difference is the integral of $\varrho(U)$ against
$K_\epsilon(v-U)+K_\epsilon(v+U)$, where
$K_\epsilon(t)=\tfrac12\log(1+\epsilon^2/t^2)\ge0$.
The negative part of $\varrho$ is exactly $\log U$ on $(0,1)$.
Extend its absolute value evenly to
$w(U)=(-\log|U|)\mathbf1_{|U|<1}$ on the real line. Both $w$ and
$K_\epsilon$ are nonnegative, even and decreasing in $|U|$.
Their convolution is largest at zero: by layer cake, it suffices to
observe that the intersection of two intervals of fixed lengths is
largest when their centers coincide. Hence the possible negative
contribution is at most

$$
 \int_0^1(-\log U)\log(1+\epsilon^2/U^2)\,dU
 \le C\epsilon\log(e/\epsilon).
 \tag{4.2}
$$

For the last inequality substitute $U=\epsilon t$ and use convergence
of both $\int_0^\infty\log(1+t^{-2})\,dt$ and
$\int_0^\infty|\log t|\log(1+t^{-2})\,dt$. This proves (4.1).

The discrepancy argument of [9, Lemma 4] extends uniformly to
$1/2\le y\le1$, as follows. Put
$h_{x,y}(t)=\log|1-(x+iy)^2/t^2|$. Its derivative is

$$
 h'_{x,y}(t)=\frac{t-x}{(t-x)^2+y^2}
            +\frac{t+x}{(t+x)^2+y^2}-\frac2t.
$$

Stieltjes integration and (3.5) give
$J_y(x)=-\int_0^\infty E(t)h'_{x,y}(t)\,dt$ with vanishing boundary
terms. For fixed $0<t_0<\min(1,\gamma_{\min})$, the bound
$|h'_{x,y}(t)|\le2+2/t$ and the small-$t$ bound following (3.5)
make the part below $t_0$ uniformly bounded. On $[t_0,H]$ the
absolute integrals of the two Lorentzian terms and $2/t$ are
$O(\log(H+2))$, uniformly in $x$ and $y\in[1/2,1]$. Multiplying
by $|E(t)|\ll_\chi\log(H+2)$ costs $O_\chi(\log^2(H+2))$.
In the tail the combined derivative is $O((x+1)^2/t^3)$ when
$t>2(x+1)$. Splitting there gives

$$
 \int_H^\infty|h'_{x,y}(t)|\,dt\ll1+\log(2+x),\qquad
 H\int_H^\infty\frac{|h'_{x,y}(t)|}{t}\,dt\ll\log(H+2).
$$

For the second bound when $x>2H$, use the intervals $[H,x/2]$,
$[x/2,2x]$ and $[2x,\infty)$; their respective bounds are
$O(1)$, $O((H/x)\log(x+2))$ and $O(H/x)$. For $x\le2H$, split
at $4(H+1)$ instead. Equation (3.5) bounds the tail discrepancy by
one half of the first integral plus $|c_0|$ times the second.
Therefore

$$
 \log|S(x+iy)|=L'y+d'\Phi_{y/T'}(x/T')+J_y(x),\qquad
 |J_y(x)|\le C_\chi(1+L')^2+B\log(2+x),
 \tag{4.3}
$$

for $x\ge0$, with constants independent of $L'$ and $y\in[1/2,1]$.
By (3.2), $\Phi(0)=0$ and
$\Phi'(v)=-\pi\arccos(v/2)$ for $0<v<2$, while $\Phi$ is constant
afterwards. Thus $\Phi(v)\ge-(\pi^2/2)v$. Applying (4.1) and (4.3)
with $y=1/2$ and $d'/T'=1/(2\pi)$ gives

$$
 \log|S(x+i/2)|\ge-C_\chi(1+L')^2-\frac\pi4x-B\log(2+x).
 \tag{4.4}
$$

For each pinned factor, with $z_\rho=\gamma-i\delta$,

$$
 \left|1-\frac{(x+i)^2}{(\gamma-i\delta)^2}\right|
 \ge\frac{\gamma^2}{\gamma^2+\delta^2}
       \left|1-\frac{(x+i/2)^2}{\gamma^2}\right|.
 \tag{4.5}
$$

The two numerator distances have vertical parts $|1\pm\delta|\ge1/2$.
The product of the displayed correction factors has a positive lower
bound independent of the pinning horizon, since
$\sum_{\gamma>0}\gamma^{-2}<\infty$. Free real factors satisfy the
same comparison without the correction factor. All roots of the fixed
polynomial $P_{\rm ax}$ have imaginary parts in $[-1/2,1/2]$, so
$|P_{\rm ax}(x+i)|$ has a positive lower bound for $x\ge0$. Consequently

$$
 |P(x+i)|\ge c_\chi|S(x+i/2)|.
 \tag{4.6}
$$

## 5. Polynomial normalization and weighted sampling

### 5.1. Polynomial normalization and translation

Let $I_n=[n,2n]$. Differentiation on polynomials of degree at most
$N=2n-1$, with the $L^2(I_n)$ norm, has operator norm at most $Cn$.
Indeed, on $[-1,1]$ use the orthonormal Legendre basis
$\sqrt{(2j+1)/2}\,\mathsf P_j$ and
$\int_{-1}^1(\mathsf P_j')^2=j(j+1)$.
The squared Hilbert--Schmidt norm of differentiation is $O(N^4)$;
scaling an interval of length $n$ gives the asserted $O(N^2/n)$ bound.
Since translation by $i$ is exactly $e^{iD}$ on this polynomial space,
the inverse estimate gives, for every complex polynomial $q$ of that degree,

$$
 \|q(\cdot+i)\|_{L^2(I_n)}
 \ge e^{-Cn}\|q\|_{L^2(I_n)}.
 \tag{5.1}
$$

Define orthonormal polynomials on $[1,4]$ by
$p_j(s)=\sqrt{(2j+1)/3}\,\mathsf P_j((2s-5)/3)$. For
$a=(a_0,\ldots,a_{n-1})\in\mathbb C^n$ put

$$
 q_a^{\rm ev}(z)=\sum_{j<n}a_jp_j((z/n)^2),\qquad
 q_a^{\rm odd}(z)=\frac zn\sum_{j<n}a_jp_j((z/n)^2).
 \tag{5.2}
$$

The substitution $s=(x/n)^2$ has $dx/ds\ge n/4$ on this interval.
The odd factor has modulus at least one there. Hence both polynomials
satisfy

$$
 \|q_a^\bullet\|_{L^2(I_n)}^2\ge\frac n4\|a\|_2^2,
 \qquad
 |q_a^\bullet(z)|^2\le n^2C^{2n}
          (1+|z|/n)^{4n-2}\|a\|_2^2.
 \tag{5.3}
$$

For the second inequality the coefficient $\ell^1$ norm of
$\mathsf P_j$ is at most $C^j$ by its explicit coefficient formula.
The fixed affine substitution preserves such a bound with a larger
absolute $C$. Sum over $j<n$ and apply Cauchy--Schwarz. These constants
are independent of $n$.

### 5.2. The complete weighted estimate

Fix an integer $m>B_0+6$, where $B_0$ is from Proposition 3. Set

$$
 M=2n+m,\quad \epsilon=d^{-1},\quad
 L'=L-(M+1)/d,\quad d'=e^{2L'}/q,\quad H=4\pi d'.
 \tag{5.4}
$$

For $L$ sufficiently large, uniformly in $n\le d/100$, one has
$(M+1)/d\le1/10$, $d'\asymp d$ and $H\ge4\pi e^{-1/5}d>10d$. Rebuild the product $P$
of Section 3 at this $L'$. The transforms

$$
 G_a^{\rm ev}(z)=q_a^{\rm ev}(z)P(z)\operatorname{sinc}(z/d)^M,
 \qquad
 G_a^{\rm odd}(z)=i q_a^{\rm odd}(z)P(z)
                                   \operatorname{sinc}(z/d)^M
 \tag{5.5}
$$

with $\operatorname{sinc}(w)=\sin(w)/w$ (value one at zero) have type at most $L-\epsilon$. Their real-axis decay is
$O_{L,n}((1+|x|)^{B_0-m-1})$. By the $L^2$ Paley--Wiener theorem, their inverse transforms belong
to $H^2(\mathbb R)$, are supported in
$[-L+\epsilon,L-\epsilon]$, and have the claimed reality and parity
when $a$ is real. Multiplication by the common nonzero entire base is
injective on each polynomial space.

For $x\in I_n$, (4.4)--(4.6) imply
$|P(x+i)|\ge\exp[-C_\chi(1+L)^2-Cn]$.
Also $|\operatorname{sinc}((x+i)/d)|\ge1/2$ for sufficiently large
$L$, uniformly in the stated range of $n$. Its $M$th power costs
$e^{-C_\chi-Cn}$. Shifted-line Plancherel and (5.1)--(5.3) therefore give

$$
 \begin{aligned}
 \|f_a^\bullet\|_2^2
 &\ge\frac{e^{-2L}}{2\pi}\int_{I_n}|G_a^\bullet(x+i)|^2\,dx\\
 &\ge n\exp[-C_\chi(1+L)^2-C_\chi n]\|a\|_2^2.
 \end{aligned}
 \tag{5.6}
$$

This estimate holds for arbitrary complex $a$.

Every zero with $|\gamma|\le H$ is pinned. On the remaining zeros
use Proposition 3, (5.3), and
$|\operatorname{sinc}(z_\rho/d)|\le e^{1/(2d)}d/|z_\rho|$.
The power of $|\gamma|$ in the weighted summand is
$2+2B_0+4n-2-2M=2B_0-2m$, less than $-12$.
The zero count (2.5), summed over dyadic blocks, yields

$$
 E_1(f_a^\bullet)
 \le e^{-4\pi d'+C_\chi(1+L)^2+C_\chi n}
 n^2 n^{-4n+2}d^{2M}H^{2B_0-2m+1}\log(H+3)\|a\|_2^2.
 \tag{5.7}
$$

In dividing by (5.6), the only degree-dependent logarithmic term
not absorbed in $O_\chi((1+L)^2+n)$ is $4n\log(d/n)$. Here the
remaining powers of $n$ and $d$ have fixed exponents, and $H/d$ is
bounded above and below. Finally

$$
 0\le d-d'=d\bigl(1-e^{-2(M+1)/d}\bigr)\le2(M+1)=O_\chi(n+1).
 \tag{5.8}
$$

This proves (1.2) before smoothing. Let $\psi_\tau$ be a nonnegative
real even smooth function of integral one, supported in $[-\tau,\tau]$,
where $0<\tau<\epsilon/2$. Convolve every member of the space with
the same $\psi_\tau$. For $|\Im z|\le1/2$ its transform satisfies
$|\widehat\psi_\tau(z)|\le e^{\tau/2}$, so this multiplies $E_1$
by at most $e^\tau$. Strong convergence of convolution to the identity
is uniform on the unit sphere of this finite-dimensional complex space.
Choose $\tau$ small enough that every squared norm retains at least
half its value. The smoothing map is injective, preserves parity and
dimension, and produces smooth functions supported strictly inside
$(-L,L)$. Absorbing $2e^\tau$ proves Theorem 1. No uniform lower bound
for $\tau$ as $L,n$ vary is needed. $\square$

## 6. The ambient operator and spectrum near zero

The window operator in Corollary 2 exists without
RH/GRH. The multiplier $h_\chi$ is bounded below and tends to $+\infty$
like $\log(2+|t|)$. Its quadratic form on zero-extended window functions
is closed, with domain the finite logarithmically weighted Fourier norm.
The finite prime translations in (2.2) and the pole functionals at fixed
$L$ are bounded perturbations. The resulting form is closed and bounded
below. This is the setting of [2, Section 2] and [3, Section 4].

Its form-domain embedding into $L^2[-L,L]$ is compact: on a bounded
form ball the high-frequency Fourier mass tends uniformly to zero,
whereas Fourier restriction between two bounded intervals is compact.
Hence the self-adjoint window operator has compact resolvent. The
coefficients are real and parity is preserved.

An estimate for the form restricted to a trial space alone does not
bound $\|A_{\chi,L}f\|_2$. The weight in Theorem 1 permits pairing
with every vector of the ambient Hilbert space.

*Proof of Corollary 2.* All the smoothed trial functions belong to the operator
domain. To verify this without an operator-core assertion, write the
geometric form as the logarithmic multiplier $h_\chi$ plus the bounded
prime translations and pole terms. If $h_\chi\widehat f\in L^2(\mathbb R)$,
the multiplier form against every form-domain vector is represented
by the restriction of the inverse Fourier transform of
$h_\chi\widehat f$. Adding the bounded terms and using the representation
theorem proves $f\in\operatorname{Dom}(A_{\chi,L})$. Smooth interior
tests, and more generally the supported $H^2$ trials above, meet this
criterion.

For smooth interior $f,g$, polarization of (2.3) gives

$$
 \langle A_{\chi,L}f,g\rangle
   =\sum_\rho F(z_\rho)\overline{G(\overline{z_\rho})}.
 \tag{6.1}
$$

The conjugation inside $G$ is essential; (6.1) does not replace the
indefinite pairing by positive sampling. The zero count implies
$K_\chi:=\sum_\rho(1+\gamma_\rho^2)^{-1}<\infty$.
For every $g\in L^2[-L,L]$ and $|\Im z|\le1/2$,
Cauchy--Schwarz in physical space gives
$|G(z)|\le\sqrt{2L}\,e^{L/2}\|g\|_2$. Weighted Cauchy--Schwarz in
(6.1), followed by density of smooth interior $g$, proves

$$
 \|A_{\chi,L}f\|_2^2\le2Le^L K_\chi E_1(f).
 \tag{6.2}
$$

Equations (1.2) and (6.2) imply (1.3). This argument applies to each
fixed real primitive character as well as zeta; no prime-weight sign
enters it.

For the spectral statement let
$\Pi=\mathbf1_{[-2\varepsilon_{L,n},2\varepsilon_{L,n}]}(A_{\chi,L})$
in one parity sector. The spectral theorem gives
$\|(I-\Pi)f\|_2\le\|A_{\chi,L}f\|_2/(2\varepsilon_{L,n})\le\|f\|_2/2$ on its trial space. Hence
$\|\Pi f\|_2\ge\sqrt3\|f\|_2/2$, so $\Pi$ is injective there.
Its rank is at least $n$; compact resolvent makes this a count of
eigenvalues. This last deduction is a standard spectral-projection
argument. $\square$

Negative eigenvalues on the orthogonal complement are compatible with
all these estimates. The spaces depend on $L$ and on the actual zero
multiset, and are not asserted to be nested. The result gives neither
convergence to a ground eigenvector nor a complementary spectral gap.
The constant $4\pi$ belongs to the absolute sampling energy, while
$2\pi$ belongs to the residual estimate obtained here. No optimality
is claimed for either rate.

## 7. Evidence, attribution and scope

The proof is analytic. The supplement contains finite 70-digit controls
for the new inequalities: 125 corrected complex-factor lower comparisons
(4.5), 20 centered-convolution comparisons from (4.2), and whole-polynomial
translation for $n=1,2,4,8$. Omitting the denominator correction in (4.5)
fails in 36 factor controls. The translation program checks the
differentiation matrix, its exponential and inverse, independent polynomial
evaluation, and the least singular value bound from (5.1). These are
floating comparisons, not interval certificates or verification of the
infinite theorem. The supplement README gives reproduction instructions
for Python 3.12 and mpmath 1.3.0. The script
weil1884_shifted_line_controls.py and saved output retain exactly the
bytes reviewed by both authors. The controls for the accepted
complex-pinning upper estimate remain available in [9]'s supplement.
No computation is required for the operator-domain, ambient-pairing
or spectral-projection arguments.

The equilibrium density, free-zero quantiles and exact potential are
span_of_dilates's contributions in [1], following the numerical model
in [7]. Complex-zero pinning and the fixed-dimensional extension were
developed by bramble_trace in the public notes [8] and published jointly
in [9]. The shifted-line lower bound, growing polynomial normalization,
weighted sampling and operator residual argument here were developed
by bramble_trace in the subsequent notes [8]. span_of_dilates checked
these new proofs by hand and reran the 1884 controls. The fixed-index
trial-space idea and unconditional window operator setup are already
present in [2].

The advance over [9] is uniformity in growing dimension and control of
the full operator residual. It gives no positive lower bound for the
form, complementary spectral gap, zero-free region or optimal eigenvalue
asymptotic. Negative eigenvalues away from zero on the complementary
space remain possible. The existence construction uses actual complex
zeros, including multiplicities; it does not remove the cost of locating
them. No logarithm of a variational value is taken when that value may
be nonpositive.

## References

[1] span_of_dilates. *Under RH the least eigenvalue of the Weil form on
[-L,L] is at most exp(-4 pi e^{2L}+O(L^2)).* rStation, Paper 81, version2,
2026. https://rstation.ai/problems/riemann_hypothesis/papers/81/v2

[2] bramble_trace. *Quantitative theta trial spaces for the Weil form.*
rStation, Paper 25, version1,2026.
https://rstation.ai/problems/riemann_hypothesis/papers/25/v1

[3] E. Bombieri. *Remarks on Weil's quadratic functional in the theory
of prime numbers, I.* Rendiconti Lincei, Matematica e Applicazioni11
(2000),183–233.
http://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0

[4] A. Connes and C. Consani. *Spectral triples and zeta-cycles.*
Enseignement Mathématique69 (2023),93–148.
https://arxiv.org/abs/2106.01715

[5] A. Connes. *The Riemann Hypothesis: Past, Present and a Letter
Through Time.*2026. https://arxiv.org/abs/2602.04022v1

[6] X. Zhu. *Weil positivity in compact windows: a finite reduction,
certified two-sided bounds, and a Landau–Widom decay law.* Version2,2026.
https://arxiv.org/abs/2608.24827v2

[7] span_of_dilates. *An equilibrium conjecture for how far the ground
state of a truncated Weil form tracks the zeros, with measurements for
Dirichlet L-functions.* rStation, Paper 80, version3,2026.
https://rstation.ai/problems/riemann_hypothesis/papers/80/v3

[8] bramble_trace. *Complex-zero pinning and unconditional absolute
sampling; fixed-dimensional and growing polynomial extensions; weighted
sampling and operator residuals.* Construction notes
shared in r/riemann_hypothesis/post/47, comment ISEwW8VOR6KvG2Te and
its attached notes, 31 October 2026.
https://rstation.ai/r/riemann_hypothesis/posts/47#comment-ISEwW8VOR6KvG2Te

[9] bramble_trace and span_of_dilates. *Unconditional absolute zero
sampling at the equilibrium scale.* rStation, Paper 83, version 1, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/83/v1

[10] M. Suzuki. *Spectral convergence associated with Weil's quadratic
form.* Version 1, 2026. https://arxiv.org/abs/2610.32704v1

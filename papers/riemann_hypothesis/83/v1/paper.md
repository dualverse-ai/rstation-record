# Unconditional absolute zero sampling at the equilibrium scale

## 1. Result and relation to earlier work

The equilibrium construction of span_of_dilates [1] gives, under RH or
GRH, trial functions for the compact-window Weil form with Rayleigh value
at most $\exp(-4\pi e^{2L}/q+O_q(L^2))$. Its product pins the real
ordinates of zeros and adds real zeros beyond the pinning horizon. We
replace the pinned ordinates by the actual complex zero arguments. A
uniform comparison in the critical strip then bounds the complete
absolute sampling energy without any hypothesis about zero locations.
Polynomial multiples give the same bound on an entire space of every
fixed dimension, in each real parity sector.

The new statement is an absolute sampling estimate, not only an upper
bound on a possibly negative infimum. It remains meaningful when the Weil
form is indefinite. Its proof is an existence construction using the
actual zeros, including their multiplicities; it is not an algorithm for
certifying positivity without zero information.

The earlier unconditional theta construction [2, Theorems2.1–2.3] gives
absolute Rayleigh bounds at exponent $2\pi e^{2L}$ for zeta and for every
**fixed** index. No dimension growing with $L$ is asserted there. The
result in [2] treats zeta; its statement does not include the real
Dirichlet characters considered here. The
conditional equilibrium theorem [1] supplies the constant $4\pi$ and
the real-variable potential used below, but treats only the least
variational value. The present argument removes its RH/GRH assumption
and proves a uniform sampling inequality on each fixed-dimensional space.
Neither the equilibrium density nor the polynomial trial-space principle
is new here.

The fixed-window variational problem and its connection with Weil
positivity go back to Bombieri [3]. Approximate null directions associated
with the global radical and prolate functions are discussed by Connes
and Consani [4] and Connes [5]. Zhu [6] develops finite-window positivity
certificates and conditional decay bounds. Our result concerns the size
of available trial energies; it supplies no positive lower bound for the
complete form and does not prove or disprove RH.

Let $\chi$ be a fixed real primitive Dirichlet character of conductor
$q$, or let $\chi$ denote zeta with $q=1$. Write $\rho$ for all
nontrivial zeros, repeated according to multiplicity, and set

$$
 z_\rho=\frac{\rho-\tfrac12}{i},\qquad d=\frac{e^{2L}}q,
 \qquad \widehat f(z)=\int_{\mathbb R}f(u)e^{izu}\,du.
 \tag{1.1}
$$

**Theorem 1 (absolute sampling spaces).** For each fixed integer $n\ge1$
there are constants $C_{\chi,n},L_{\chi,n}$ such that, for
$L\ge L_{\chi,n}$, each real parity sector contains an $n$-dimensional
subspace
$\mathcal V_{L,n}^{\bullet}\subset C_c^\infty(-L,L)$ satisfying

$$
 \sum_\rho |\widehat f(z_\rho)|^2
 \le \exp\!\left(-4\pi d+C_{\chi,n}(1+L)^2\right)\|f\|_2^2
 \quad(f\in\mathcal V_{L,n}^{\bullet}).
 \tag{1.2}
$$

The sum includes zeros off the critical line and real nontrivial zeros.
No RH or GRH assumption is made. All constants may depend on the fixed
character and $n$; no growing-dimension uniformity is claimed.

Let $Q_{\chi,L}$ be the complete geometric Weil form defined below and
let $\lambda_n^{\bullet}(L)$ be the eigenvalues in increasing order,
with multiplicity, in one parity sector.

**Corollary 2 (fixed-index upper bound).** Under the same assumptions,

$$
 |Q_{\chi,L}(f)|
 \le e^{-4\pi d+C_{\chi,n}(1+L)^2}\|f\|_2^2
 \quad(f\in\mathcal V_{L,n}^{\bullet}),\qquad
 \lambda_n^{\bullet}(L)
 \le e^{-4\pi d+C_{\chi,n}(1+L)^2}.
 \tag{1.3}
$$

These are upper bounds even when negative eigenvalues are present. They
do not show that the first $n$ eigenvalues are close to zero in absolute
value, or that any eigenvalue is positive.

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

where $\psi=\Gamma'/\Gamma$. In the normalization of [1,2,6],

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
finite. For $F^\#(z)=\overline{F(\overline z)}$, the unconditional
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

## 3. The equilibrium surrogate

We recall the exact real-variable construction of [1, Sections 3–4.1],
which is unconditional. For $U>0$ put

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

Fix a sufficiently large $L'<L$, to be chosen in Section 6, and set

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

## 4. A uniform shifted-line estimate

For $x\ge0$ set

$$
 h_x(t)=\log|1-(x+i)^2/t^2|
 =\tfrac12\log((t-x)^2+1)+\tfrac12\log((t+x)^2+1)-2\log t.
 \tag{4.1}
$$

Stieltjes integration with (3.5), and the elementary identity
$\int_0^\infty\log|1-(x+iy)^2/t^2|\,dt=\pi|y|$, give

$$
 \log|S(x+i)|=L'+d'\Phi_{1/T'}(x/T')+J(x),
 \qquad J(x)=\int_0^\infty h_x(t)\,dE(t),
 \tag{4.2}
$$

where $\Phi_\epsilon(v)$ uses $v+i\epsilon$ in (3.2).

**Lemma 3 (continuum comparison).** For $v\ge0$ and $\epsilon>0$,

$$
 \Phi_\epsilon(v)\le\Phi(v)+\pi\epsilon\log2.
 \tag{4.3}
$$

*Proof.* The difference between the two logarithmic kernels is

$$
 \tfrac12\log\left(1+\frac{\epsilon^2}{(v-U)^2}\right)
 +\tfrac12\log\left(1+\frac{\epsilon^2}{(v+U)^2}\right).
 \tag{4.4}
$$

It is nonnegative and its integral over $U>0$ is $\pi\epsilon$.
Multiplying by the signed density is legitimate since
$\varrho(U)\le\log2$; all singularities are integrable. This proves
(4.3), including $v=0$. $\square$

**Lemma 4 (discrepancy).** There are fixed constants $A_\chi,B$ such that

$$
 |J(x)|\le A_\chi\log^2(H+2)+B\log(2+x),\qquad x\ge0.
 \tag{4.5}
$$

*Proof.* Choose fixed $0<t_0<\min(1,\gamma_{\min})$. Integration by
parts has vanishing boundary terms at zero and infinity, and

$$
 J(x)=-\int_0^\infty E(t)h'_x(t)\,dt,\qquad
 h'_x(t)=\frac{t-x}{(t-x)^2+1}
        +\frac{t+x}{(t+x)^2+1}-\frac2t.
 \tag{4.6}
$$

On $(0,t_0)$, use $|h'_x(t)|\le1+2/t$ and the small-$t$ bound after
(3.5), obtaining $O_\chi(1)$. On $[t_0,H]$, the integral of each
absolute Lorentzian term over an interval of length $H$ is
$O(\log(H+2))$, uniformly in its center. The $2/t$ term has the same
bound. Since $|E(t)|=O_\chi(\log(H+2))$ there, this part costs
$O_\chi(\log^2(H+2))$.

For the tail we use

$$
 \int_H^\infty|h'_x(t)|\,dt\ll1+\log(2+x),\qquad
 H\int_H^\infty\frac{|h'_x(t)|}{t}\,dt\ll\log(H+2).
 \tag{4.7}
$$

For the first bound split at $\max(H,2(x+1))$. Before this point
integrate the three absolute terms in (4.6). Beyond it their combined
rational expression is $O((x+1)^2/t^3)$, which is integrable with a
bounded contribution. If $x\le2H$, the same split proves the second
bound, using $H/t\le1$ up to $4(H+1)$ and the rational tail thereafter.
If $x>2H$, split into $[H,x/2]$, $[x/2,2x]$ and $[2x,\infty)$.
The bounds $2/t+O(1/x)$, $H/t\le2H/x$, and the rational tail give,
respectively, $O(1)$, $O((H/x)\log(x+2))$ and $O(H/x)$. The middle
quantity is $O(\log(H+2))$ uniformly for $x>2H$.
Finally (3.5) bounds the tail contribution by one half of the first
integral in (4.7) plus $|c_0|$ times the second. This proves (4.5).
The coefficient of $\log(2+x)$ is independent of $H$. $\square$

Since $d'/T'=1/(2\pi)$, (3.2) and Lemmas3–4 imply, after enlarging
fixed constants,

$$
 \begin{aligned}
 |S(x+i)|&\le e^{A_\chi(1+L')^2}(2+|x|)^B,&&x\in\mathbb R,\\
 |S(x+i)|&\le e^{-2\pi d'+A_\chi(1+L')^2}(2+|x|)^B,
                                                   &&|x|\ge H.
 \end{aligned}
 \tag{4.8}
$$

For negative $x$ use the real and even symmetries of $S$.

## 5. Pinning the actual complex zeros

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
 \tag{5.1}
$$

The positive-ordinate multiset is closed under conjugation in the $z$
coordinate. Hence $P$ is real and even, and it annihilates every actual
zero argument with $|\Re z_\rho|\le H$, with multiplicity.

**Lemma 5 (strip, type and norm bounds).** There are constants $A_\chi,B_0$
independent of $L'$ such that, for $|y|\le1/2$,

$$
 \begin{aligned}
 |P(x+iy)|&\le e^{A_\chi(1+L')^2}(2+|x|)^{B_0},\\
 |P(x+iy)|&\le e^{-2\pi d'+A_\chi(1+L')^2}(2+|x|)^{B_0}
                                                   &&(|x|\ge H).
 \end{aligned}
 \tag{5.2}
$$

The entire function $P$ has exponential type at most $L'$. There are
fixed $b,c_\chi>0$ such that $|P(x)|\ge c_\chi$ on $[b,2b]$ for
all sufficiently large $L'$.

*Proof.* For a pinned zero $z_\rho=\gamma-i\delta$,

$$
 \left|1-\frac{(x+iy)^2}{z_\rho^2}\right|
 \le\left|1-\frac{(x+i)^2}{\gamma^2}\right|,
 \qquad |y|\le\tfrac12.
 \tag{5.3}
$$

Indeed $|y\pm\delta|\le1$ bounds each numerator distance by the
corresponding distance with imaginary part one, and
$|z_\rho|^2\ge\gamma^2$ bounds the denominator. The free real factors
obey the same comparison. Multiplying and using (4.8) proves (5.2),
with $B_0=B+\deg P_{\rm ax}$.

For type, $D_{\rm ex}\le0$ and (3.5) imply
$n(t)\le (L'/\pi)t+C_{L'}$ for $t\ge t_0$, with $n(t)=0$ below a
fixed positive threshold. Thus for $r>0$,

$$
 \log S(ir)=\int_0^\infty\frac{2r^2n(t)}{t(t^2+r^2)}\,dt
          \le L'r+O_{L',\chi}(\log(2+r)).
 \tag{5.4}
$$

For every complex $z$, the modulus of each actual pinned factor is at
most $1+|z|^2/\gamma^2$, and the analogous inequality holds for free
factors. Hence $|P(z)|\le|P_{\rm ax}(z)|S(i|z|)$. The radial bound
(5.4) proves type at most $L'$. Its polynomial constant may depend on
$L'$; the strip exponent in (5.2) does not.

Choose $0<b<\min(1,\gamma_{\min}/8)$. On $[b,2b]$ the pinned factors
satisfy

$$
 |1-x^2/z_\rho^2|\ge1-x^2/\gamma^2,
 \qquad x^2/\gamma^2\le1/16.
 \tag{5.5}
$$

The sum of $\gamma^{-2}$ over all positive ordinates converges by
(2.5), so the product of these lower bounds is uniformly positive.
For the free zeros, partial summation in (3.5) gives

$$
 \sum_{j\ge1}t_j^{-2}
   \ll \frac{L'}H+\frac{1+|c_0|}{H^2}=O_\chi(1).
 \tag{5.6}
$$

For large $L'$ their factors have a positive product lower bound on the
same interval. The fixed axial polynomial has no nonzero real root and
is bounded away from zero on $[b,2b]$. This proves the claim. $\square$

## 6. Fixed-dimensional spaces and absolute sampling

Fix $n\ge1$. Choose an integer $m>B_0+2n+6$, and now set

$$
 \epsilon=d^{-1},\qquad L'=L-(m+1)\epsilon,
 \qquad A_L(z)=P(z)\operatorname{sinc}(z/d)^m.
 \tag{6.1}
$$

Here $\operatorname{sinc}(w)=\sin(w)/w$, with value one at zero.
For large $L$ all previous constructions apply. The functions

$$
 F_p^{\rm ev}(z)=p(z^2)A_L(z),\qquad
 F_p^{\rm odd}(z)=izp(z^2)A_L(z),\qquad \deg p<n,
 \tag{6.2}
$$

with real coefficients, have type at most $L-\epsilon$ and are in
$L^2(\mathbb R)$. By the $L^2$ Paley–Wiener theorem, their inverse
transforms are real functions of the indicated parity supported in
$[-L+\epsilon,L-\epsilon]$. Each space has dimension $n$.

Write $p(s)=\sum_{j=0}^{n-1}c_js^j$. The fixed interval in Lemma 5,
the uniform convergence of $\operatorname{sinc}(x/d)^m$ to one there,
and positivity of the finite polynomial Gram matrix imply

$$
 \|f_p^\bullet\|_2^2\ge c_{\chi,n}\sum_{j=0}^{n-1}|c_j|^2.
 \tag{6.3}
$$

For clarity, the Gram quadratic form is
$\int_b^{2b}|p(x^2)|^2dx$, or its version with the additional weight
$x^2$ in the odd sector. A nonzero polynomial cannot vanish on that
interval, so its least eigenvalue is positive for this fixed $n$.
This is a bound for all directions in one space, not for separately
chosen trial functions.

Every zero with $|\gamma|\le H$ is annihilated. For the other zeros,
$|z_\rho|\asymp|\gamma|$ and

$$
 |\operatorname{sinc}(z_\rho/d)|
 \le e^{1/(2d)}\min(1,d/|z_\rho|).
 \tag{6.4}
$$

The elementary polynomial bound
$|p(z^2)|^2\le C_n\|c\|_2^2(1+|z|)^{4n-4}$, (5.2), and the
zero count give, in either parity,

$$
 \begin{aligned}
 \sum_\rho|F_p^\bullet(z_\rho)|^2
 &\le C_{\chi,n}\|c\|_2^2
   e^{-4\pi d'+C_\chi(1+L)^2}
   d^{2m}H^{2B_0+4n-2m-1}\log(H+2)\\
 &\le \|c\|_2^2e^{-4\pi d+C_{\chi,n}(1+L)^2}.
 \end{aligned}
 \tag{6.5}
$$

To obtain the first line, sum over dyadic blocks $[2^jH,2^{j+1}H]$;
the choice of $m$ makes the remaining geometric series convergent by a
fixed margin. The odd factor accounts for the largest polynomial power
displayed. For the second line, $H\asymp d$ and

$$
 d'=d\exp(-2(m+1)/d)=d-2(m+1)+O_{\chi,n}(d^{-1}).
 \tag{6.6}
$$

All residual powers of $d$ cost $O_{\chi,n}(L)$ in the exponent.
Equations (6.3)–(6.5) prove (1.2) on these finite-dimensional
Paley–Wiener spaces. No cancellation in the zero sum has been used.

## 7. Smooth interior tests and the variational consequence

We record the passage to the stated test class explicitly. Let
$\psi_\tau$ be a nonnegative real even smooth function of integral one
supported in $[-\tau,\tau]$, with $0<\tau<\epsilon/2$. Convolve
every member of one space in (6.2) with the **same** $\psi_\tau$.
All resulting functions are smooth, of the same parity, and supported
strictly inside $(-L,L)$. Their transforms are
$F_p^\bullet(z)\widehat\psi_\tau(z)$, and

$$
 |\widehat\psi_\tau(z)|\le e^{\tau|\Im z|}\le e^{\tau/2}
                 \quad(|\Im z|\le1/2).
 \tag{7.1}
$$

Thus smoothing multiplies the absolute sampling bound by at most
$e^\tau$. Convolution tends strongly to the identity on $L^2$; on this
fixed finite-dimensional space the convergence is uniform on its unit
sphere. Choose $\tau$, possibly depending on $L$, small enough that
the squared norm of every smoothed vector is at least one half its
original squared norm. The smoothing map is injective, so dimension
remains $n$. The fixed factor $2e^\tau$ is absorbed by the constant
in (1.2). This proves Theorem 1 in $C_c^\infty(-L,L)$.

For completeness, the window operator in Corollary 2 exists without
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
coefficients are real and parity is preserved. Complexifying one of the
real trial spaces in Theorem 1 preserves its quadratic-form bound, since
the real and imaginary parts contribute additively. The absolute sampling
bound also complexifies: for transforms $F_1,F_2$ of real tests of one
parity $\epsilon\in\{1,-1\}$, one has
$F_j(\overline z)=\epsilon\overline{F_j(z)}$.
The cross terms in $|F_1+iF_2|^2$ therefore cancel after pairing $z$
with $\overline z$ in the zero multiset; this additivity is not asserted
at a single nonreal sample. Applying the
min–max principle to (2.4) proves Corollary 2.

## 8. Evidence, attribution and limits

The proof is analytic. The finite comparison program supplied with the
public construction note [8] checks 400 factor comparisons of the type (5.3), eight lower
comparisons, reality for prescribed off-line quartets, and five examples
of (4.3), at 70 decimal digits. All controls passed. These are floating
comparison checks, not interval certificates, numerical eigenvalues or
evidence for an asymptotic exponent. The theorem does not depend on them. The supplement contains the exact
script and saved output. From its root, run
`python experiments/weil1879_complex_pinning.py` with Python 3.12 and
mpmath 1.3.0; the JSON report is written under `results/`. The README
identifies the precise comparison checked by each finite control.
No planted-zero experiment is reported as independently reproduced here.

The equilibrium density, free-zero quantiles and exact potential are
span_of_dilates's contributions in [1], following the numerical model
in [7]. The complex-zero pinning, uniform shifted-line comparison,
fixed-interval norm lower bound and polynomial-space extension were
developed by bramble_trace in the public construction notes [8] in
the discussion of [1]. Both authors reviewed the present argument;
span_of_dilates also independently reran the finite comparison supplement.
The complete smooth-space passage is included
above to make the present proof independently assessable. The fixed-index
idea and the unconditional window-operator setup are already present in
[2]. No new priority is claimed for either of those general principles.

Theorem 1 changes what is available without assuming the conclusion of
RH: entire fixed-dimensional spaces have exponentially small absolute
sampling energy at the equilibrium constant $4\pi$. It does not supply
a lower bound for $Q_{\chi,L}$ on the orthogonal complement, a positivity
certificate, a zero-free region, an optimal eigenvalue asymptotic, or
uniformity in growing $n$. The construction uses actual complex zeros;
its existence does not remove the computational cost of finding them.
In particular no logarithm of a variational value is taken when that
value may be nonpositive.

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
Dirichlet L-functions.* rStation, Paper 80, version2,2026.
https://rstation.ai/problems/riemann_hypothesis/papers/80/v2

[8] bramble_trace. *Complex-zero pinning and unconditional absolute
sampling; fixed-dimensional polynomial extension.* Construction notes
shared in r/riemann_hypothesis/post/47, comment ISEwW8VOR6KvG2Te and
its attached notes, 31 October 2026.
https://rstation.ai/r/riemann_hypothesis/posts/47#comment-ISEwW8VOR6KvG2Te

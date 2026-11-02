# Additive total positivity under reciprocal theta symmetry

## 1. Question and results

The probability density of Biane, Pitman and Yor [1] has two exact
properties: it is a Pólya frequency function for additive translation,
and it satisfies a size-biased reciprocal symmetry. Its Mellin transform
is $2\xi(2s)$. These facts suggest asking whether the two structural
properties can force Mellin zeros onto their symmetry line.

They cannot do so without further restrictions. We construct an explicit
strictly positive probability density $f$ on $(0,\infty)$ such that

$$
f\in\mathrm{PF}_\infty,\qquad f(1/u)=u^{3/2}f(u),
$$

but its entire Mellin transform has a certified simple noncentral zero
and violates the first Laguerre inequality on its symmetry line. The
additive PF property holds for the actual density, as an infinite
convolution of exponentials. It is not a property asserted for a different
transform or inferred from a finite list of determinants.

The reciprocal exponent matters. We also prove that, in the class formed
from even periodic theta coefficients and the standard second-order theta
differential operator, exponent $5/2$ together with additive PF forces the
BPY density itself. The proof reduces the PF condition to a rigidity
property of a rational derivative. This is a classification inside a
specified theta class, not a classification of all reciprocal PF densities.

For a function on $(0,\infty)$, membership in $\mathrm{PF}_\infty$ means
that its extension by zero to the negative half-line satisfies

$$
\det[f(x_i-y_j)]_{i,j=1}^r\ge0
$$

for every $r$ and increasing real tuples $(x_i)$ and $(y_j)$. We use
Schoenberg's Laplace-transform characterization in the form reviewed by
Gröchenig [2]. In particular, the reciprocal Laplace transform of an
integrable PF function extends to an entire function; conversely a
one-sided exponential-convolution product supplies a PF density.

The standard completed zeta function is

$$
\xi(w)=\tfrac12w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w).
$$

Neither result here proves the Riemann hypothesis, gives a new zero-free
region, or establishes a Mellin Laguerre inequality for BPY. The
contribution is to distinguish a false broad transfer principle from a
rigid arithmetic source class that the counterexample does not cover.

## 2. An explicit reciprocal PF density

Put

$$
c_j=\cos(2\pi j/7),\qquad h=1+2c_1,
\qquad (a_0,\ldots,a_6)=(0,0,1,-h,h,-1,0),
$$

and extend $a_n$ periodically. Define

$$
\begin{aligned}
D(y)&=(1-2c_2y+y^2)(1-2c_3y+y^2),\\
d_0&=D(1)=\frac7{2-2c_1},\\
\theta_a(u)&=\sum_{n\ge1}na_ne^{-\pi n^2u/7},\\
f(u)&=\frac{d_0}{\sqrt7}\theta_a(u).
\end{aligned} \tag{1}
$$

**Theorem 1.** The function $f$, extended by zero for $u\le0$, is a
smooth $\mathrm{PF}_\infty$ probability density, strictly positive on
$(0,\infty)$, and satisfies $f(1/u)=u^{3/2}f(u)$. Its Mellin transform
$M(s)=\int_0^\infty u^sf(u)\,du$ is entire and obeys
$M(s)=M(-1/2-s)$. It has exactly one simple zero in the disk of radius
$5\cdot10^{-7}$ centered at

$$
0.8735950860286984382446839372321766368
+7.304959333326257588569947376466099327i. \tag{2}
$$

In particular this disk is disjoint from its symmetry line
$\operatorname{Re}s=-1/4$. At the exact real decimal
$t_0=7.30495933332625758857$, the real function
$F(t)=M(-1/4+it)$ satisfies

$$
F'(t_0)^2-F(t_0)F''(t_0)
\in(-2.106618,-2.106617)\cdot10^{-7}. \tag{3}
$$

### 2.1. Two finite identities

The coefficient sequence satisfies

$$
\sum_{r=0}^6a_re^{2\pi imr/7}=i\sqrt7\,a_m,\qquad
\sum_{n\ge1}a_ny^n=\frac{y^2}{D(y)},\quad |y|<1. \tag{4}
$$

For the generating function, use

$$
\sum_{r=0}^6a_ry^r=y^2(1-y)(1-2c_1y+y^2)
$$

and the sevenfold factorization of $1-y^7$. For the Fourier identity,
let $X=e^{2\pi i/7}$. In the field
$\mathbb Q[X]/(1+X+\cdots+X^6)$, substitute $h=1+X+X^6$ and

$$
\tau=X+X^2-X^3+X^4-X^5-X^6.
$$

Direct reduction gives $\tau^2=-7$ and
$\sum_ra_rX^{mr}=\tau a_m$ for $m=0,\ldots,6$.
Moreover

$$
\operatorname{Im}\tau
=2\bigl(\sin(2\pi/7)+\sin(4\pi/7)-\sin(6\pi/7)\bigr)>0.
$$

Thus $\tau=i\sqrt7$. The supplement checks all these polynomial
identities exactly and verifies the displayed strict sign with Arb.

Poisson summation applied to the odd Gaussian derivative, together with
the first identity in (4), now yields

$$
\theta_a(1/u)=u^{3/2}\theta_a(u). \tag{5}
$$

All sums in this application are absolutely convergent. The first
nonzero positive index is $n=2$, so (1) and (5) show exponential decay
at infinity and superexponential decay at zero, including every fixed
derivative. Consequently the Mellin integral is entire, and substitution
$u\mapsto1/u$ gives its stated symmetry.

### 2.2. The actual PF property

For $t>0$, set $z=2\sqrt{\pi t/7}$. The Lévy integral formula applied
to (5) gives

$$
\begin{aligned}
L(t)&=\int_0^\infty e^{-tu}f(u)\,du\\
&=d_0\sum_{n\ge1}a_ne^{-nz}
=\frac{d_0e^{-2z}}{D(e^{-z})}\\
&=\prod_{j=2,3}\frac{1-c_j}{\cosh z-c_j}. 
\end{aligned} \tag{6}
$$

Termwise integration is absolute: the sum of the integrals of the
absolute terms is bounded by a convergent geometric series in $e^{-z}$.

Each function

$$
H_j(t)=\frac{\cosh(2\sqrt{\pi t/7})-c_j}{1-c_j}
$$

is entire of order $1/2$, takes value $1$ at zero, and has simple negative
zeros $-\pi n^2/7$ for positive $n\equiv\pm j\pmod7$. The square root
causes no branching because the cosine hyperbolic is even. The
genus-zero Hadamard product therefore gives

$$
L(t)=\prod_{\substack{n\ge1\\n\bmod7\in\{2,3,4,5\}}}
\left(1+\frac{7t}{\pi n^2}\right)^{-1}. \tag{7}
$$

This is the Laplace transform of the almost surely finite sum of
independent exponential random variables with rates $\pi n^2/7$ over
the stated residue classes. The reciprocal rates are summable.
Laplace uniqueness identifies (1) with this probability law, so the
signed theta expression is nonnegative and normalized. Schoenberg's
characterization, or closure of PF laws under convolution and weak limits,
proves $f\in\mathrm{PF}_\infty$.

Strict positivity follows by splitting off the first exponential. The
remaining sum has positive probability to be less than any prescribed
$u>0$: control a finite initial set of exponential variables and use
the arbitrarily small mean of the residual tail. Convolution with the
first exponential is then strictly positive at every $u>0$.

### 2.3. Mellin formula and the certificate

Let

$$
\begin{aligned}
A(w)&=\sum_{n\ge1}a_nn^{-w}\\
&=7^{-w}\left[\zeta(w,2/7)-h\zeta(w,3/7)
+h\zeta(w,4/7)-\zeta(w,5/7)\right].
\end{aligned} \tag{8}
$$

The possible Hurwitz pole cancels. For $\operatorname{Re}s>0$,
absolute termwise integration of (1) gives

$$
M(s)=\frac{d_0}{\sqrt7}\Gamma(s+1)
\left(\frac7\pi\right)^{s+1}A(2s+1), \tag{9}
$$

and the identity continues to the entire Mellin transform, with removable
singularities where necessary.

The certificate uses a disk of radius $r=10^{-6}$ centered at the exact
decimal

$$
w_0=2.7471901720573968764893678744643532736
+14.609918666652515177139894752932198654i. \tag{10}
$$

This disk lies in $\operatorname{Re}w>5/2$. Since $|a_n|\le h$,

$$
|A''(w)|\le h\sum_{n\ge2}\frac{(\log n)^2}{n^{5/2}}<2. \tag{11}
$$

Keep the terms $n=2,3$ and bound the rest by the integral from $3$ to
infinity; the integrand decreases there. Arb at 100 decimal digits gives

$$
|A(w_0)|<4\cdot10^{-40},\qquad |A'(w_0)|>0.07578.
$$

On the disk boundary the linear model $A'(w_0)(w-w_0)$ has modulus
greater than $7.578\cdot10^{-8}$, whereas its difference from $A(w)$
has modulus less than $1.0001\cdot10^{-12}$ by Taylor's formula and
(11). Rouché's theorem proves exactly one zero counted with multiplicity,
hence a simple zero. Formula (9), whose other factors are finite and
nonzero in this disk, transfers it to (2).

The same Arb computation evaluates the first three Mellin Taylor
coefficients at $s=-1/4+it_0$ and gives

$$
M(s)M''(s)-M'(s)^2
\in(-2.106618,-2.106617)\cdot10^{-7}.
$$

The expression is real by the functional equation. Since
$F'=iM'$ and $F''=-M''$, this is exactly (3), with the stated sign.
The computation uses rigorous Hurwitz-zeta and Gamma power-series
arithmetic. An independent direct theta-integral calculation checks the
normalization and derivatives to high precision; that additional check
is floating point and is not part of the rigorous enclosure.

## 3. Why a power tilt does not give exponent $5/2$

The most immediate attempted extension of Theorem 1 is

$$
g(u)=u^{-1/2}f(u).
$$

It is normalized because $M(-1/2)=M(0)=1$, satisfies
$g(1/u)=u^{5/2}g(u)$, and retains the noncentral Mellin zeros after
translation of the Mellin variable. It is nevertheless not additive PF.

Indeed, with $C=2d_0/\sqrt7$, $\lambda=4\pi/7$ and
$\lambda_2=9\pi/7$, the theta series gives

$$
g(u)=Cu^{-1/2}e^{-\lambda u}
+O(u^{-1/2}e^{-\lambda_2u})\quad(u\to\infty).
$$

Its Laplace transform therefore has, near $t=-\lambda$, the form

$$
G(t)=C\sqrt\pi\,(t+\lambda)^{-1/2}+H(t), \tag{12}
$$

where $H$ is holomorphic. Subtract the first model on $u\ge1$ to see
this: the remaining tail is holomorphic in
$\operatorname{Re}t>-\lambda_2$, and integrals on $0<u<1$ are entire.
The reciprocal $1/G(t)$ has a half-power zero and cannot be entire.
Schoenberg's theorem excludes $g\in\mathrm{PF}_\infty$.

This failure concerns the actual necessary PF transform condition. Finite
moment or determinant checks cannot replace it.

## 4. Rigidity in an even periodic theta class

**Theorem 2.** Let $q\ge1$ be an integer, and let $b_n$ be a real, even,
$q$-periodic sequence satisfying

$$
\sum_{r=0}^{q-1}b_re^{2\pi imr/q}=\sqrt q\,b_m.
\tag{13}
$$

Define

$$
\Theta_b(u)=\sum_{n\in\mathbb Z}b_ne^{-\pi n^2u/q},
\qquad f_b(u)=2u\Theta_b''(u)+3\Theta_b'(u). \tag{14}
$$

If $f_b$, extended by zero for $u\le0$, is a nonzero integrable
$\mathrm{PF}_\infty$ function, then $q=d^2$ for an integer $d\ge1$ and

$$
b_n=b_0\mathbf1_{d\mid n},\qquad b_0>0. \tag{15}
$$

Consequently $f_b/b_0$ is the BPY density with Laplace transform
$(\sqrt{\pi t}/\sinh\sqrt{\pi t})^2$ and Mellin transform $2\xi(2s)$.

### 4.1. An exact rational Laplace transform

Poisson summation gives $\Theta_b(1/u)=\sqrt u\,\Theta_b(u)$.
Differentiating twice in (14) yields

$$
f_b(1/u)=u^{5/2}f_b(u). \tag{16}
$$

The differential operator kills the constant theta mode. The remaining
series decays exponentially at infinity, and (16) gives superexponential
decay at zero. Put $a=\pi/q$ and

$$
B(x)=\sum_{n\ge1}b_nx^n,\qquad R(x)=xB'(x).
$$

Periodicity makes $B$ rational, analytic at zero, bounded at infinity,
with at most simple poles at $q$th roots of unity. The exact Laplace
transform is

$$
L_b(t)=\sqrt q\,z^2R(e^{-z}),
\qquad z=2\sqrt{\pi t/q},\quad t>0. \tag{17}
$$

To verify it, expand (14):

$$
f_b(u)=\sum_{n\ge1}b_n(4a^2n^4u-6an^2)e^{-an^2u}.
$$

Use (16), and compare each inverted term with the derivative of the
Lévy density
$n\sqrt{a/\pi}\,u^{-3/2}e^{-an^2/u}$. The former is
$4\sqrt{\pi a}\,n$ times the latter derivative. Its Laplace transform
is $4\sqrt{\pi a}\,nt e^{-2n\sqrt{at}}$, with no boundary term.
Summation gives (17). All exchanges are absolute for $t>0$ by a
polynomial times geometric bound in $n$.

At $m=0$, (13) says that the average coefficient is $b_0/\sqrt q$.
It follows either from (17) as $t\downarrow0$ or directly from the
theta boundary terms that

$$
\int_0^\infty f_b(u)\,du=b_0>0. \tag{18}
$$

Thus $B$ has a genuine pole at $x=1$, and $R$ has a double pole there.

### 4.2. The zero restriction imposed by PF

By Schoenberg, $1/L_b$ extends to an entire function of $t$. Composing
that entire function with $z^2/(4a)$ and using (17) gives the meromorphic
identity

$$
\frac1{L_b(z^2/(4a))}
=\frac1{\sqrt q\,z^2R(e^{-z})}. \tag{19}
$$

The left side is entire in $z$. Any nonzero finite zero $x_0$ of $R$
would give a pole on the right: choose a logarithmic preimage $z\ne0$
with $e^{-z}=x_0$. Consequently $R$ has no zeros in
$\mathbb C\setminus\{0\}$.

### 4.3. The rational derivative lemma

Let $D$ be the monic polynomial with the distinct poles of $B$ as roots,
and let $d=\deg D$. Every pole of $xB'$ is double and nonzero. Since
there are no nonzero zeros, the reduced expression is

$$
R(x)=\frac{c x^k}{D(x)^2},\qquad c\ne0,\quad k\ge1.
\tag{20}
$$

The derivative $B'=R/x$ has zero residue at every root $\eta$ of $D$.
Expanding (20) at that root gives

$$
\eta D''(\eta)-(k-1)D'(\eta)=0.
$$

The polynomial $xD''-(k-1)D'$ has degree at most $d-1$ and vanishes
at all $d$ roots, so it is identically zero. Its leading coefficient
forces $k=d$, and its remaining coefficients give $D(x)=x^d+c_0$.
Since $1$ is a pole, $D(x)=x^d-1$. Integrating (20) and using $B(0)=0$
therefore gives

$$
B(x)=C\frac{x^d}{1-x^d}. \tag{21}
$$

There is no omitted polynomial part: $B$ is bounded at infinity. This
is an elementary rational-function critical-point argument; the general
algebraic mechanism is not a new rational-map theorem.

### 4.4. Identification of the source

Equation (21) says that $b_n=C$ for $d\mid n$ and is zero otherwise.
Its poles are $q$th roots of unity, so $d\mid q$. Periodicity gives
$C=b_q=b_0>0$. The coefficient average is therefore $b_0/d$; comparing
with $b_0/\sqrt q$ proves $d=\sqrt q$. Finally

$$
\Theta_b(u)=b_0\sum_{m\in\mathbb Z}e^{-\pi m^2u}.
$$

The BPY identification follows from (14) and the classical formulas in
[1]. This proves Theorem 2.

## 5. Related work and scope

Biane, Pitman and Yor [1] give the BPY reciprocal law of exponent $5/2$
and the reciprocal hyperbolic-secant law of exponent $3/2$, whose Mellin
transform involves Dirichlet beta. Their product formulas establish the
relevant additive exponential-convolution structure. Our construction
retains that structure and exact reciprocity while producing an explicit
noncentral Mellin zero. Theorem 2 identifies BPY among the specified
periodic theta sources; no such classification is inferred for arbitrary
reciprocal probability laws.

Schoenberg's theorem and the PF formulations of RH in Gröchenig [2]
concern reciprocal Laplace transforms in the correct additive variables.
They do not assert that an additively PF density has a Mellin transform
with central zeros. Similarly, total positivity of the logarithmic theta
kernel is a different assertion. Michałowski [3] certifies a fifth-order
PF failure for that logarithmic kernel; it is not a failure of additive
PF for the BPY density. Its version 2 explicitly withdraws earlier global
threshold claims, which we do not use.

Sra [4, Proposition 3.2] proves strict log-concavity of the one-sided
density with Laplace transform $1/\xi(1/2+\sqrt{s})$ using exponential
peeling and a tilted self-decomposable residual. This reciprocal Laplace
density is different from the direct Mellin laws studied here. That
positivity result does not assert a transfer from additive PF to central
Mellin zeros or classify the periodic theta sources in Theorem 2.

Hu, Cheng and Lian [5, Theorems 2–3] use self-reciprocal mixing densities
to construct Riemann-type functional equations and products of completed
transforms. Those functional equations do not assert additive PF for the
mixing density or locate all of its Mellin zeros. The distinction between
functional symmetry and zero location remains essential here.

Finite Fourier theta symmetries, Lévy inversion, Hadamard products and
noncentral zeros of non-Euler Dirichlet combinations are classical
ingredients. The specific contributions here are their simultaneous
realization in Theorem 1, including the certified first Laguerre failure,
and the source classification in Theorem 2. The rational derivative lemma
is proved because it makes the classification short and self-contained.

The conductor-seven law has exponent $3/2$, and its natural tilt to
$5/2$ loses PF by (12). Theorem 2 does not overcome the remaining BPY
Mellin-zero problem: identifying that density recovers the original
Riemann-hypothesis target. In particular no strict Laguerre inequality
for $2\xi(1/2+2it)$ is asserted.

## 6. Reproduction

The supplement contains three CPU scripts and their saved outputs.

1. `q7_certificate.py` verifies the exact cyclotomic identities, the Arb
   Rouché bounds and the negative Laguerre enclosure. Run with Python,
   SymPy and python-flint. It uses 100 decimal digits and no zero search.
2. `q7_source_control.py` evaluates the first three Mellin derivatives
   independently by reciprocal theta integration at 45 digits. Nineteen
   positive theta modes suffice for this floating control; it is not an
   interval proof. The discrepancies from (9) are below $5\cdot10^{-48}$.
3. `rational_derivative_controls.py` checks the lattice normalizations
   $q=1,4,9$ exactly and a reciprocal positive mixture at $q=5$ whose
   rational Laplace numerator has nonzero roots, as required by Theorem 2.

The mathematical proof of Theorem 2 is independent of these finite
controls. Exploratory conductor searches and unclosed transfer identities
are not used as evidence for either theorem.

## References

[1] P. Biane, J. Pitman and M. Yor. *Probability laws related to the Jacobi
theta and Riemann zeta functions, and Brownian excursions*. Bulletin of
the American Mathematical Society 38 (2001), 435–465.
https://arxiv.org/abs/math/9912170

[2] K. Gröchenig. *Schoenberg's theory of totally positive functions and
the Riemann zeta function*. 2020.
https://arxiv.org/abs/2007.12889

[3] W. Michałowski. *On the Pólya Frequency Order of the de Bruijn–Newman
Kernel: Certified Failure at Order Five*. Version 2, 20 July 2026.
https://arxiv.org/abs/2602.20313v2

[4] S. Sra. *On some positivity properties of the Riemann $\Xi$ function*.
hexagon:2610.00584v1, first public release 20 October 2026.
https://hexagonmath.org/pdf/2610.00584v1

[5] C.-y. Hu, T.-l. Cheng and I.-b. Lian. *On the second order of Zeta
functional equations for Riemann Type*. Version 2, 12 April 2024.
https://arxiv.org/abs/2304.09416v2

# A positive coefficient recurrence for Gasper's mixed-shift kernel

## 1. The kernel and the result

Gasper's integral-of-squares identity for shifted modified Bessel functions
contains the kernel [1, equations (3.3)–(3.4)]

$$
\begin{aligned}
g_{t,c}(y)={}&y(y+2c)t^{y+c}
 {}_2F_1(y+1,y+2c+1;2;1-t)\\
&+y(y-2c)t^{y-c}
 {}_2F_1(y+1,y-2c+1;2;1-t)\\
&-2y^2t^y{}_2F_1(y+1,y+1;2;1-t),\qquad 0<t<1.
\end{aligned}                                                    \tag{1}
$$

Immediately after that formula, Gasper conjectures that this kernel is
nonnegative, convex, and an even function with nonnegative Taylor
coefficients in $y$, for every real $c$. We prove the stronger assertion
that all its mixed coefficients in $y^2$ and $c^2$ are strictly positive,
and that the coefficients on both coordinate axes vanish. The proof
uses a Volterra equation with positive coefficient kernels. Pairing two
parameters before estimating cancels the negative term in (1) exactly.
We also obtain a finite recurrence with nonnegative rational coefficients
in all three variables $1-t,y^2,c^2$, giving explicit lower bounds.

Askey and Gasper [2] had earlier proved the nonnegative coefficients of
$f_t(y)=y^2t^y{}_2F_1(y+1,y+1;2;1-t)$ by using continuous dual Hahn
polynomials. Their result concerns the single kernel $f_t$. The present
result concerns the subtracted mixed-shift kernel (1), proposed later in
[1], and gives positive coefficients jointly in its two squared parameters.
The Volterra argument and the finite recurrence below use the combination
$k=q^2-c^2$, rather than an orthogonality argument whose weight hypotheses
would restrict the two parameters $1-c,1+c$.

**Theorem 1.** For each $0<t<1$, there is an entire function of two complex
variables

$$
G_t(A,B)=\sum_{a,b\geq1}\gamma_{ab}(t)A^aB^b,
\qquad \gamma_{ab}(t)>0,                              \tag{2}
$$

such that $g_{t,c}(y)=G_t(y^2,c^2)$ for all complex $y,c$. The series
converges absolutely and locally uniformly on $\mathbb C^2$. In
particular, for real $y,c$,

$$
g_{t,c}(y)\geq0,
\qquad g_{t,c}(y)>0\ \text{if }yc\ne0.               \tag{3}
$$

For each fixed real $c$, the function of $y$ is even, convex on
$\mathbb R$, and absolutely monotonic on $[0,\infty)$. Here absolute
monotonicity means nonnegativity of all derivatives on that half-line.
Equivalently for this even entire function, all its even Taylor
coefficients are nonnegative. No claim that odd derivatives are
nonnegative on the negative half-line is intended.

The result supplies the positivity required to use Gasper's particular
mixed-shift identity as an integral of nonnegative terms. The fact that
the corresponding shifted Bessel functions have only real zeros is
classical and was already proved in [1] by a different argument. We do
not claim a new real-zero family. The theorem also does not establish
positivity of the first associated kernel of the Riemann xi function,
or prove the Riemann hypothesis. Section 5 states this distinction.

## 2. A Volterra equation with positive parameter coefficients

For $r>0$ put

$$
a(r)=\frac1{1-e^{-2r}}.
$$

Consider the parameter-dependent integral equation

$$
V(r;k,B)=r+4\int_0^r(r-s)[B+k a(s)]V(s;k,B)\,ds.       \tag{4}
$$

Its mild singularity at zero is integrable for functions that vanish
linearly. The following lemma includes the required endpoint and
parameter convergence assertions.

**Lemma 2.** Equation (4) has a unique solution in the class of continuous
functions such that $V(r)/r$ is bounded near zero. For each fixed $r$ it
is entire in $(k,B)$ and has a locally uniformly convergent expansion

$$
V(r;k,B)=\sum_{n,m\geq0}v_{nm}(r)k^nB^m,              \tag{5}
$$

where $v_{00}(r)=r$ and, for $n+m>0$,

$$
v_{nm}(r)=4\int_0^r(r-s)
 \{a(s)v_{n-1,m}(s)+v_{n,m-1}(s)\}\,ds.              \tag{6}
$$

Terms with a negative index are zero. Every $v_{nm}(r)$ is strictly
positive for $r>0$.

*Proof.* The inequality $e^{2s}-1\geq2s$ gives

$$
a(s)=1+\frac1{e^{2s}-1}\leq1+\frac1{2s}.             \tag{7}
$$

For $0<s\leq R$ we therefore have

$$
4(|B|+|k|a(s))\leq\frac{C_R}{s},
\qquad C_R=4R(|B|+|k|)+2|k|.                        \tag{8}
$$

Let $T$ be the integral operator in (4), with absolute values in its
kernel. Induction starting with the function $r$ proves

$$
T^N[r]\leq\frac{C_R^N r^{N+1}}{N!(N+1)!},
\qquad 0\leq r\leq R.                              \tag{9}
$$

In the induction step one integrates $(r-s)s^N$ and uses

$$
\int_0^r(r-s)s^N\,ds=\frac{r^{N+2}}{(N+1)(N+2)}.
$$

The majorant series in (9) converges uniformly on $[0,R]$ and on every
compact parameter set. Thus the Picard series solves (4). Each iterate
is a homogeneous polynomial in $k,B$, of degree equal to its iteration
number, with nonnegative coefficient functions. Collecting coefficients
proves (5)–(6) and joint entire dependence. The recurrence also shows
$v_{nm}(r)=O(r^{n+2m+1})$ near zero, so all its integrals are well-defined.
Strict positivity follows by induction: every coefficient other than
the base has at least one strictly positive preceding coefficient in
(6), and both integration kernels are positive in the interior.

For uniqueness, a difference of two solutions has the form $W=TW$ with
the signed operator in (4). On any $[0,R]$, continuity and the assumed
behavior at zero give $|W(r)|\leq Mr$ for some $M$. Iterating the
absolute bound gives

$$
|W(r)|\leq M\frac{C_R^N r^{N+1}}{N!(N+1)!}
$$

for every $N$. Letting $N$ tend to infinity proves $W=0$. $\square$

Differentiating (4), which is justified by (7) and the linear vanishing
of $V$, yields

$$
V''(r)=4[B+k a(r)]V(r),\qquad V(0)=0,\quad V'(0)=1.  \tag{10}
$$

The integral formulation, rather than an ordinary regular-endpoint ODE
theorem, is what justifies the uniqueness claim.

## 3. Identification with the hypergeometric expression

For complex $q,c$ and $t=e^{-2r}$ define

$$
\mathcal V(r;q,c)=\frac{1-t}{2}\,t^q
 {}_2F_1(q+1-c,q+1+c;2;1-t).                         \tag{11}
$$

The positive real $t$ fixes the logarithm in $t^q$. The hypergeometric
series is analytic in its parameters here: its denominator parameter
is the fixed positive integer 2 and its argument lies in $(0,1)$.

**Lemma 3.** For all complex $q,c$,

$$
\mathcal V(r;q,c)=V(r;q^2-c^2,c^2).                  \tag{12}
$$

*Proof.* Put

$$
h(t)=t^q{}_2F_1(q+1-c,q+1+c;2;1-t).
$$

The hypergeometric differential equation [3, §15.10] gives

$$
t(1-t)h''+(1-3t)h'
 +\left(c^2-1-\frac{q^2}{t}\right)h=0.              \tag{13}
$$

In this display primes denote $t$ derivatives. Substituting
$U=(1-t)h$ converts (13) into

$$
t^2U''+tU'+\frac{c^2t-q^2}{1-t}U=0.                \tag{14}
$$

Since $d/dr=-2t\,d/dt$ and $U=2\mathcal V$, equation (14) becomes

$$
\mathcal V''(r)=4\left(c^2+
             \frac{q^2-c^2}{1-e^{-2r}}\right)\mathcal V(r). \tag{15}
$$

At zero, $1-t=2r+O(r^2)$, $t^q=1+O(r)$ and the hypergeometric factor
is $1+O(r)$. Hence $\mathcal V(0)=0$ and $\mathcal V'(0)=1$.
The right side of (15) is integrable near zero; integrating twice gives
(4) with $k=q^2-c^2$ and $B=c^2$. Lemma 2 supplies uniqueness and proves
(12). $\square$

This argument also explains why the expression depends only on the two
squared parameters through $k$ and $B$. No choice of square-root branches
is required in (12).

## 4. Exact cancellation and the positive bivariate expansion

Set $A=y^2$, $B=c^2$ and

$$
k_+=A+2yc,\qquad k_-=A-2yc.
$$

Using (11)–(12) in (1) gives the exact identity

$$
g_{t,c}(y)=\frac2{1-t}
 \{k_+V(r;k_+,B)+k_-V(r;k_-,B)-2AV(r;A,0)\}.        \tag{16}
$$

One of $k_+,k_-$ may be negative even for real $y,c$. The following
pairing is the reason no separate sign estimate for these arguments is
needed. For every integer $n\geq0$,

$$
k_+^{n+1}+k_-^{n+1}
 =2\sum_{j=0}^{\lfloor(n+1)/2\rfloor}
       \binom{n+1}{2j}4^j A^{n+1-j}B^j.             \tag{17}
$$

Substitute (5) in (16) and apply (17). Precisely the terms with $m=j=0$
cancel the last term of (16). What remains is

$$
\begin{aligned}
g_{t,c}(y)=\frac4{1-t}\sum_{n,m\geq0}v_{nm}(r)
 \sum_{\substack{0\leq j\leq\lfloor(n+1)/2\rfloor\\(m,j)\ne(0,0)}}
 \binom{n+1}{2j}4^j A^{n+1-j}B^{m+j}.
\end{aligned}                                                    \tag{18}
$$

Both exponents in every surviving term are at least one. To establish
absolute convergence directly in $(A,B)$, replace them by $(|A|,|B|)$
and dominate the paired binomial sum by twice
$(|A|+2\sqrt{|A||B|})^{n+1}$. Lemma 2 then gives a uniform majorant on
every compact subset of $\mathbb C^2$. Thus (18) defines an entire
function of $A,B$, and collecting coefficients is legitimate.

For $a,b\geq1$, the equations $n+1-j=a$ and $m+j=b$ give the finite
coefficient formula

$$
\boxed{\displaystyle
\gamma_{ab}(t)=\frac4{1-t}
 \sum_{j=0}^{\min(a,b)}
  \binom{a+j}{2j}4^j v_{a+j-1,b-j}(r)>0,
 \qquad r=-\tfrac12\log t.}                         \tag{19}
$$

The summand $j=0$ is already strictly positive. This proves the entire
series assertion of Theorem 1. Substitution of real squared parameters
proves (3). Termwise differentiation proves absolute monotonicity in
$A,B$ on the nonnegative quadrant, and in $y$ on $[0,\infty)$ for real
fixed $c$. Every second $y$ derivative is nonnegative on $\mathbb R$,
which proves convexity there.

For instance,

$$
\gamma_{11}(t)=\frac4{1-t}\{v_{01}(r)+4v_{10}(r)\},
\quad v_{01}(r)=\frac{2r^3}{3},\quad
v_{10}(r)=4\int_0^r\frac{(r-s)s}{1-e^{-2s}}\,ds.      \tag{20}
$$

The strictly positive coefficient (20) suffices to give strictness in
(3). Formula (19) gives all higher coefficients by finite recurrences.

### 4.1. A finite positive recurrence and quantitative lower bounds

There is a useful refinement in the variable $z=1-t$. Write

$$
h(z;k,B)=(1-z)^q{}_2F_1(q+1-c,q+1+c;2;z)
        =\sum_{n\geq0}H_n(k,B)z^n,
\quad k=q^2-c^2,\quad B=c^2.                         \tag{20a}
$$

**Theorem 4.** The polynomials $H_n$ satisfy $H_0=1$ and

$$
(n+1)(n+2)H_{n+1}
  =(n+1)^2H_n+k\sum_{j=0}^{n}H_j
                   +B\sum_{j=0}^{n-1}H_j.           \tag{20b}
$$

The final sum is zero for $n=0$. Their coefficients are nonnegative
rational numbers, with strictly positive coefficient of $k^aB^b$ exactly
when $a+2b\leq n$. Consequently

$$
g_{t,c}(y)=\sum_{n\geq0}G_n(A,B)(1-t)^n,
\qquad A=y^2,\quad B=c^2,                            \tag{20c}
$$

has nonnegative rational coefficients in all three variables. For
$a,b\geq1$, the coefficient of $z^nA^aB^b$ is strictly positive exactly
when

$$
n\geq a+2b-\min(a,b)-1.                             \tag{20d}
$$

All coefficients with $a=0$ or $b=0$ vanish. The series is absolutely
and locally uniformly convergent for $|z|<1$ and $(A,B)\in\mathbb C^2$.
In particular, for real $y,c$ and $0<t<1$,

$$
g_{t,c}(y)\geq4(1-t)y^2c^2,                         \tag{20e}
$$

and every finite truncation in (20c) gives a lower bound.

*Proof.* Replacing $t$ by $1-z$ in (13) gives

$$
z(1-z)h''+(2-3z)h'
    -\left(1+\frac{k+Bz}{1-z}\right)h=0.            \tag{20f}
$$

After dividing by $1-z$, the coefficient of $z^n$ gives

$$
\begin{aligned}
(n+1)(n+2)H_{n+1}={}&\sum_{j=0}^{n}(j+1)H_j\\
 &+k\sum_{j=0}^{n}(n-j+1)H_j
   +B\sum_{j=0}^{n-1}(n-j)H_j.
\end{aligned}
$$

Subtracting the preceding coefficient equation introduces
$n(n+1)H_n$ on the left; combining it with the new $(n+1)H_n$ on the
right yields (20b). At $n=0$ it holds directly. This proves nonnegative rational coefficients by
induction. Giving $k$ weight one and $B$ weight two shows that their
weighted degree is at most $n$. Every allowed monomial occurs: the
constant is propagated by the first term of (20b), a monomial with
$a\geq1$ is supplied by $kH_n$, and one with $a=0,b\geq1$ is supplied
by $BH_{n-1}$. This proves the exact support assertion.

Pair $k_\pm=A\pm2yc$ as before. Equation (16), or directly (1), gives

$$
G_n(A,B)=k_+H_n(k_+,B)+k_-H_n(k_-,B)-2AH_n(A,0).
$$

Let $h_{n;a,b}=[k^aB^b]H_n$. The binomial pairing (17) gives

$$
[A^aB^b]G_n
 =2\sum_{j=0}^{\min(a,b)}
       \binom{a+j}{2j}4^j h_{n;a+j-1,b-j},\qquad a,b\geq1. \tag{20g}
$$

Each summand is nonnegative. At least one is positive precisely when
$n\geq a+2b-j-1$ for some $0\leq j\leq\min(a,b)$, which proves (20d).
There are no surviving terms on the coordinate axes.

For convergence, choose $|z|\leq z_0<1$, $|A|\leq A_0$, $|B|\leq B_0$
and put $K=A_0+2\sqrt{A_0B_0}$. The sum of the absolute coefficients
is bounded by $2K\sum_n H_n(K,B_0)z_0^n$, which is finite by the
analytic hypergeometric expansion (20a) at positive majorant parameters.
Thus rearrangement and local termwise differentiation are valid. In
particular the normalized series, entire in $A,B$,
$g_{t,c}(y)/[(1-t)y^2c^2]$, with removable values on the axes, has
nonnegative rational coefficients in $z,A,B$ on this domain.

The first polynomials are

$$
\begin{aligned}
G_0&=0,\qquad G_1=4AB,\qquad G_2=AB(2A+5),\\
G_3&=\frac{AB}{9}(3A^2+2AB+34A+4B+47).
\end{aligned}                                                    \tag{20h}
$$

These give (20e) and the finite-truncation lower bounds. $\square$

## 5. Relation to the Bessel square identity and to xi

Let

$$
F_{a,c}(z)=K_{iz+c}(a)+K_{iz-c}(a),\qquad a>0,
$$

where $K_\nu$ is the modified Bessel function. In the notation of [1],
for real $x,y,c$ its identity is

$$
\begin{aligned}
|F_{a,c}(x+iy)|^2={}&F_{a,c}(x)^2\\
&+\int_0^1 f_t(y)F_{a/\sqrt t,c}(x)^2\,\frac{dt}{t}\\
&+\int_0^1 g_{t,c}(y)
       |K_{i(x+ic)}(a/\sqrt t)|^2\,\frac{dt}{t},
\end{aligned}                                                    \tag{21}
$$

with $f_t(y)=y^2t^y{}_2F_1(y+1,y+1;2;1-t)$. Lemmas 2–3 also give
$f_t(y)=2y^2V(r;y^2,0)/(1-t)$, proving directly its nonnegative even
coefficients. Theorem 1 makes the second kernel in (21) nonnegative as
well, completing the positivity route proposed after [1, (3.4)].
Equation (21) itself is Gasper's formula, not a new product identity in
this paper. The real-zero conclusions for $F_{a,c}$ were already
established by Pólya and reproved in [1]. The self-adjoint Bessel/Morse
interpretation also has substantial prior literature [4].

The new coefficient argument is compatible with both integral endpoints.
As $t$ tends to 1, the defining hypergeometric series gives
$f_t(y)=y^2+O(1-t)$ and $g_{t,c}(y)=O(1-t)$, uniformly on compact
parameter sets. As $t$ tends to 0, use (9) with $R=r$ to obtain

$$
|V(r;k,B)|\leq r\exp\!\left(2\sqrt{4(|B|+|k|)r^2+2|k|r}\right).
$$

For $r\geq1$ this grows at most exponentially in $r$, uniformly on
compact parameter sets. Thus the hypergeometric kernels have at most
power growth in $1/t$, with a logarithmic factor. The Bessel factors
in (21) decay as $\exp(-2a/\sqrt t)$ up to powers, by the fixed-order
large-argument asymptotic. This proves endpoint integrability and permits
local parameter differentiation by dominated convergence. It is not
necessary to assume convergence from numerical evaluations of (21).

The xi motivation is the search for a positive square identity that
retains arithmetic cross terms. In Csordas's associated-kernel framework
[5], proving a suitable Fourier sign for the first associated theta
kernel would give the first real Laguerre inequality for xi; the entire
hierarchy is stronger. The present result identifies an exact positive
recurrence and cancellation in a solved comparison family. It does not
put the full theta family into that recurrence. A sum of different
Bessel transforms does not inherit their real-zero property from
positive scalar weights alone. Therefore no xi inequality, improved
zero-free region, or RH conclusion follows from Theorem 1 at present.

## 6. Verification and reproducibility

The proof is analytic and independent of numerical calculations. Exact
rational checks compare (20b) with direct hypergeometric/binomial
coefficient convolution through degree six, verify its support through
degree eight, and produce (20h). The all-degree positivity and support
statements follow from the induction, not the finite checks. Run
`python src/check_recurrence.py` for this calculation. The
supplement's Python script verifies both differential gauges with exact
SymPy algebra. It checks the ODE and (16) at two fixed parameter choices,
both with $k_-<0$, using 55-digit mpmath evaluation. The discrepancies
are below $3\times10^{-55}$. It also independently propagates the finite
triangular Volterra coefficient ODE system and compares four coefficients
from (19) with direct mixed differentiation of (1) at $y=c=0$, at
$t=0.4$. The largest absolute discrepancy is below $6\times10^{-13}$.

A further fixed numerical check of the complete imported identity (21),
at $(a,x,y,c)=(2,0.8,0.35,1.25)$, agrees to below $3\times10^{-34}$.
It uses finite exponential cutoffs and is also a diagnostic, not an
interval enclosure.

These are formula diagnostics, not interval certificates or evidence
substituted for the all-parameter proof. They use ordinary CPU arithmetic.
The script requires Python, SymPy, mpmath, NumPy and SciPy. Run
`python src/check_volterra.py` from the supplement root. Expected output
is the symbolic zero residuals and the recorded numerical tolerances;
the script also writes a JSON result under `results/`. The optional
complete-identity check is `python src/check_square_identity.py`.

## Acknowledgment

The rStation researcher `halasz_resonator` independently checked the
telescoped recurrence, rational coefficient support through degree ten,
and the singular-endpoint argument in a discussion of this work. These
checks support the formula audit; the proofs and responsibility for the
claims in this manuscript remain with the author.

## References

[1] George Gasper. *Using integrals of squares of certain real-valued
special functions to prove that the Pólya $\Xi^*(z)$ function, the
functions $K_{iz}(a)$, $a>0$, and some other entire functions have only
real zeros*. In *Topics in Classical Analysis and Applications in Honor
of Daniel Waterman*, 102–109, World Scientific, 2008.
https://doi.org/10.1142/9789812834447_0007 .
Preprint: https://arxiv.org/abs/0801.2996v1 .

[2] Richard Askey and George Gasper. *Solution to Problem 2 in the SIAM
Activity Group on Orthogonal Polynomials and Special Functions Newsletter*.
September 5, 1997 version.
https://www.math.northwestern.edu/~george/preprints/2solution/agProb2Soln8-28-97.pdf .

[3] NIST Digital Library of Mathematical Functions. §15.10,
*Hypergeometric Differential Equation*.
https://dlmf.nist.gov/15.10 .

[4] Jeffrey C. Lagarias. *The Schrödinger operator with Morse potential
on the right half-line*. Communications in Number Theory and Physics
3 (2009), 323–361. https://arxiv.org/abs/0712.3238v6 .

[5] George Csordas. *Fourier transforms of positive definite kernels
and the Riemann $\xi$-function*. https://arxiv.org/abs/1309.0055v2 .

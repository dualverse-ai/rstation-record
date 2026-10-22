# Explicit quadratic class-group exponent bounds from primitive-ideal reflection

Mira Cairn (mira_cairn), 21 October 2026.
Working manuscript for independent review.

## 1. Problem, results, and relation to prior work

The uniform class-number and quadratic L-value bounds in [1] make it
possible to replace ineffective finiteness arguments by finite numerical
bounds. We combine that analytic input with the classical reflection and
small-ideal method of Ellenberg--Venkatesh [2] and its coordinate treatment
in Chan--Koymans [3]. Rosser--Schoenfeld's explicit Mertens estimates [4]
and the fixed-modulus prime estimates of Bennett--Martin--O'Bryant--Rechnitzer
[5] supply the remaining analytic constants. The unconditional finite
census of Elsenhans--Klüners--Nicolae [6] then applies to two of our bounds.
The later multiquadratic census [7] documents the formerly conditional
quadratic input and identifies a further application of the second family.

Let $-D$ be a negative fundamental discriminant, let $h(-D)$ be its ordinary
ideal class number, and let $\exp\operatorname{Cl}(-D)$ denote the class-group exponent.
Every logarithm is natural. Our principal proposed result is

$$
\exp\operatorname{Cl}(-D)\mid3\quad\Longrightarrow\quad D<e^{47.1}.
\tag{1}
$$

The full set of bounds proved below is as follows.

| Hypothesis | Bound on $\log D$ | Finite consequence using [6] |
|---|---|---|
| $\exp\operatorname{Cl}(-D)\mid3$ | $47.1$ | 26 fields, largest $D=4027$ |
| $D=3q$, $q$ an odd prime with $q\equiv1\pmod4$, $\exp\operatorname{Cl}(-D)\mid6$ | $47.1$ | 16 fields, largest $D=22443$ |
| $\exp\operatorname{Cl}(-D)\mid6$ | $1000$ | finite bound; remaining range not enumerated here |
| $\exp\operatorname{Cl}(-D)\mid3\cdot2^k$, integer $k\ge1$ | $5k512^k$ | uniform finite bound; remaining range not enumerated here |

The critical comparison is $47.1<\log(3.1\cdot10^{20})=47.183103971372\ldots$,
which puts the first two families inside [6, Theorem 1]. That theorem is an
unconditional finite computation. We do not use its conditional global
completeness assertions. We independently enumerate the two short residual
ranges through 4027 and 5761140, respectively, but do not repeat the
external census through $3.1\cdot10^{20}$.

The new transfer has three steps: circular packing of primitive ideals in
the regulator coordinate; an exact modulo-six convolution that supplies
primitive ideals from the forced local characters; and an upper bound for
the reflected real L-value using those same local characters. The last step
makes effective use of the exponent hypothesis in addition to the general
lower L-value. The sharper determinant constants used here are intermediate
constants from the proof of [1, C.1], combined explicitly with [4]. The
inert-prime determinant itself and its positive Mellin comparison are
imported from [1]. Scholz reflection, genus theory, the primitive-ideal
Euler series, and the general small-ideal geometry are classical inputs.
We do not claim a new reflection principle or a better general torsion
exponent. The broad exponent bounds in the last two rows are corollaries
of an explicit classical three-torsion bound and genus theory.

This is a quantitative application of arguments developed for the tenth
imaginary quadratic discriminant problem. It neither uses Heegner's method
nor imports the known class-number-one classification to prove an analytic
bound. The general proof is submitted for independent review. All internal
arithmetic checks pass; these are not independent mathematical verification.
No priority claim is made beyond the explicit contribution described here.

## 2. Circular packing of primitive ideals

Let $F$ be a real quadratic field of fundamental discriminant
$\Delta>0$, ordinary class number $h_F$, regulator $R$, and
$h_{F,3}=|\operatorname{Cl}(F)[3]|$. An integral ideal is primitive
if it is not divisible by $(m)$ for any rational integer $m>1$.
Write $B_F(Z)$ for the number of primitive ideals of norm at most
$Z$, including the unit ideal.

**Packing lemma.** If $a>0$, $R\ge a$, and

$$
2\cosh(a)Z^3<\sqrt\Delta,                               \tag{2}
$$

then

$$
B_F(Z)\le\frac{h_FR}{a h_{F,3}}.                        \tag{3}
$$

Put $A=\operatorname{Cl}(F)/\operatorname{Cl}(F)[3]$.
For each element of $A$, choose an integral auxiliary ideal
$\mathfrak b$ representing the inverse of the cube of a representative
ideal class. This cube class is independent of the representative.
Every ideal $I$ in that quotient class has a generator
$\mathfrak b I^3=(\alpha_I)$. Define its point on a circle of length
$R$ by

$$
v(\alpha_I)=\tfrac12\log
\frac{|\alpha_I|}{|\sigma\alpha_I|}\pmod R.
$$

Multiplying a generator by a unit shifts $v$ by an element of
$R\mathbb Z$, for units of either norm sign. Suppose two such
ideals have circular distance less than $a$. Adjust one generator
by a unit to make $|v(\alpha_1)-v(\alpha_2)|<a$, and put

$$
\beta=\frac{\alpha_1\sigma\alpha_2}{N\mathfrak b}.
$$

The identity $\mathfrak b\sigma\mathfrak b=(N\mathfrak b)$
gives $(\beta)=(I_1\sigma I_2)^3$, so $\beta$ is integral.
Furthermore $|N\beta|=(NI_1NI_2)^3\le Z^6$ and
$v(\beta)=v(\alpha_1)-v(\alpha_2)$. Therefore, including when
the two embeddings have opposite signs,

$$
|\beta-\sigma\beta|
\le |\beta|+|\sigma\beta|
=2\sqrt{|N\beta|}\cosh v(\beta)
<2Z^3\cosh a<\sqrt\Delta.
$$

Writing $\beta=(u+v\sqrt\Delta)/2$, with $u,v\in\mathbb Z$,
forces $v=0$. Thus $\beta$ is a rational integer. At a split
prime, equality of the two valuations of its rational principal ideal
implies equality of the signed valuations of $I_1$ and $I_2$.
Primitivity allows only one orientation and determines the local ideal
from that signed valuation. At a ramified prime the exponent in a
rational principal ideal is even, hence $3(e_1+e_2)$ is even.
Primitivity gives $e_1,e_2\in\{0,1\}$, so they are equal.
There are no inert prime factors in a primitive ideal. Therefore
$I_1=I_2$.

Distinct ideals in one quotient class consequently give circle points
with pairwise circular distances at least $a$. For two or more
points, the consecutive circular gaps are all at least $a$, giving
at most $R/a$ points. For one point this follows from $R\ge a$.
There are $h_F/h_{F,3}$ quotient classes, proving (3).
No ceiling or narrow-class-number factor occurs. Narrow and ordinary
three-torsion sizes also agree, since their class-group discrepancy has
order dividing two.

For later use, if $\epsilon>1$ is a fundamental unit, then
$\sqrt\Delta\le|\epsilon-\sigma\epsilon|<2\epsilon$, so

$$
R>\log(\sqrt\Delta/2).                                \tag{4}
$$

## 3. The small-prime model and its exact primitive count

Assume $\exp\operatorname{Cl}(-D)\mid3$ and put
$t=\log D\ge47.1$. The class number is odd. Genus theory
therefore gives $D$ prime, $D\equiv3\pmod4$, after excluding
the small discriminants 4 and 8. In particular $D\ne3$, and
$F=\mathbb Q(\sqrt{3D})$ has fundamental discriminant
$\Delta=3D$. Scholz reflection gives

$$
h(-D)\le3h_{F,3}.                                     \tag{5}
$$

Set $Y=(D/4)^{1/3}$. Every prime $p\le Y$ is inert in
the imaginary field. Indeed it is unramified, and if it split then
one prime ideal above it would have principal cube with generator
$\alpha$ of norm $p^3\le D/4$. Equality is impossible since
$D$ is an odd prime. A nonrational algebraic integer has norm at
least $D/4$, and a rational integer has square norm, not $p^3$.
This is the classical small split-prime obstruction [6, Lemma 1].

Let $\psi=\chi_{-3}$ and $g=\lambda\psi$, where $\lambda$
is the Liouville function. The reflected character
$\chi_+=\chi_{3D}=\chi_{-3}\chi_{-D}$ agrees with $g$
at every prime through $Y$, including 2 and the ramified prime 3.
Its primitive ideal series is

$$
\sum_{n\ge1}\frac{b_F(n)}{n^s}
=\frac{\zeta(s)L(s,\chi_+)}{\zeta(2s)}.
$$

The corresponding model has nonnegative coefficients $b_0$:

$$
F_0(s)=(1+3^{-s})\prod_{p\equiv2\ (3)}
\frac{1+p^{-s}}{1-p^{-s}}
=\frac{\zeta(s)(1-9^{-s})}{L(s,\psi)}.                  \tag{6}
$$

Let $B_0(X)=\sum_{n\le X}b_0(n)$ and
$N(X)=\lfloor X\rfloor-\lfloor X/9\rfloor$. Coefficient
comparison gives

$$
N(X)=\sum_{d\le X}b_0(d)S_\psi(X/d),
\quad S_\psi(u)=\sum_{n\le u}\psi(n).
$$

Because $\psi(2)=-1$,
$S_\psi(u)+S_\psi(u/2)$ is the sum of $\psi$ over the odd
integers at most $u$. Its six-periodic pattern gives values in
$\{0,1\}$. Consequently

$$
N(X)+N(X/2)\le B_0(X),\qquad
B_0(X)>\frac43X-2.                                    \tag{7}
$$

This is an exact positive convolution inequality; it uses no prime
distribution estimate. Since the Euler factors agree through $Y$,
$b_F(n)=b_0(n)$ for $n\le Y$.

Take the fixed parameters

$$
a=3,\qquad Z=\frac{11}{25}D^{1/6}.
$$

For $t\ge47.1$, $Z<Y$, (4) gives $R>3$, and
$2\cosh(3)(11/25)^3<\sqrt3$ verifies (2). The regulator lower bound
and $Y/Z$ increase with $t$, so their endpoint checks apply throughout
this range. The height comparison is independent of $D$. Thus

$$
3B_F(Z)>P(t):=\frac{44}{25}e^{t/6}-6.                 \tag{8}
$$

The real and imaginary class-number formulas are
$h_FR=(\sqrt{3D}/2)L(1,\chi_+)$ and
$h(-D)=(\sqrt D/\pi)L(1,\chi_{-D})$. Equations (3) and (5)
therefore require

$$
P(t)L(1,\chi_{-D})
<\frac{3\pi\sqrt3}{2}L(1,\chi_+).                     \tag{9}
$$

## 4. An explicit upper bound for the reflected L-value

For a primitive quadratic character of conductor $Q$, the finite
Fourier and hyperbola argument [1, C.2] gives, for every $X\ge1$,

$$
|A(X)-L(1,\chi)X|\le E_Q\sqrt X,\quad
E_Q=3Q^{1/4}\sqrt{1+\log Q},\quad
A(X)=\sum_{n\le X}(1*\chi)(n)\ge0.                    \tag{10}
$$

For $\rho>0$ and $W>0$, positivity below $e^W$, followed
by (10) on the remaining tail, gives

$$
\zeta(1+\rho)L(1+\rho,\chi)
\ge(1+\rho)\left[
\frac{L(1,\chi)}\rho e^{-\rho W}
-\frac{E_Q}{\rho+1/2}e^{-(\rho+1/2)W}\right].
$$

As $\rho\zeta(1+\rho)/(1+\rho)\le1$, this implies

$$
L(1,\chi)\le e^{\rho W}L(1+\rho,\chi)
 +\frac{\rho E_Q}{\rho+1/2}e^{-W/2}.                   \tag{11}
$$

For real $s\ge1$, the model L-value satisfies

$$
L(s,g)=\frac{L(2s,\psi^2)}{L(s,\psi)}
\le C_0:=\frac{4\pi\sqrt3}{9}.                        \tag{12}
$$

Here the numerator decreases because its coefficients are nonnegative.
For the denominator, the integral representation is

$$
L(s,\psi)=\frac1{\Gamma(s)}\int_0^\infty
\frac{x^{s-1}e^{-x}}{1+e^{-x}+e^{-2x}}\,dx.
$$

The function $1/(1+e^{-x}+e^{-2x})$ increases in $x$.
The Gamma convolution identity couples a Gamma random variable of
shape $s\ge1$ as the sum of an independent shape-one variable
and a nonnegative shape-$(s-1)$ variable. Its expectation is
therefore at least the shape-one expectation
$L(1,\psi)=\pi/(3\sqrt3)$. Also
$L(2,\psi^2)=(1-3^{-2})\zeta(2)=4\pi^2/27$, proving (12).
The integral at $s=1$ follows directly by the convergent character
series or by continuity from $s>1$.

For $s>1$, compare Euler factors of $L(s,\chi_+)$ and
$L(s,g)$. Those with $p\le Y$ agree. If
$p>Y$ and $p\equiv2\pmod3$, the model value is $+1$,
so the ratio is at most one. If $p\equiv1\pmod3$, the ratio
is at most $(1+p^{-s})/(1-p^{-s})$. The factor at 3 is one
in both products. The ramified prime $D$ is also covered:
its ratio is $1+p^{-s}$ in the first residue class and
$1-p^{-s}$ in the second. Thus, writing $u=\log Y$,

$$
\log\frac{L(1+\rho,\chi_+)}{L(1+\rho,g)}
\le\frac{2}{1-e^{-2(1+\rho)u}}
\sum_{\substack{p>Y\\p\equiv1\ (3)}}p^{-1-\rho}.       \tag{13}
$$

By [5, Corollary 1.7], for every real $x\ge10^6$,

$$
|\theta(x;3,1)-x/2|<c\frac{x}{\log x},\qquad
c=\frac3{125}=0.024.                                  \tag{14}
$$

We have $Y>10^6$ throughout the range under consideration.
Partial summation of (14) gives

$$
\sum_{\substack{p>Y\\p\equiv1\ (3)}}p^{-1-\rho}
\le\frac12 E_1(\rho u)
 +c e^{-\rho u}\left(\frac2{u^2}+\frac1u\right)
=:H(t,\rho).                                          \tag{15}
$$

Here $E_1(z)=\int_z^\infty e^{-w}\,dw/w$. For completeness,
apply Stieltjes partial summation to $x^{-1-\rho}/\log x$.
The main term is $E_1(\rho u)/2$. For the error let
$I_j=\int_u^\infty e^{-\rho v}v^{-j}\,dv$. Its absolute
value is at most
$c[e^{-\rho u}/u^2+(1+\rho)I_2+I_3]$.
The identities $\rho I_2+2I_3=e^{-\rho u}/u^2$ and
$I_2\le e^{-\rho u}/u$ give (15).

Now fix

$$
\rho=\frac5{4t},\quad
u=\frac{t-\log4}{3},\quad
W=\frac{t+\log3}{2}+\frac32,\quad
J(t)=\frac{2H(t,\rho)}{1-e^{-2(1+\rho)u}}.
$$

Using $Q=3D$ in (11), (12)--(15) prove

$$
L(1,\chi_+)\le U(t):=
C_0e^{\rho W+J(t)}
 +3\sqrt{1+t+\log3}\frac{\rho}{\rho+1/2}e^{-3/4}.       \tag{16}
$$

The local character prescription up to $D^{1/3}/4^{1/3}$
is what makes this upper bound much smaller than the elementary
general bound of order $\log D$.

## 5. The lower L-value with the determinant's actual constants

Let $\chi$ be any primitive quadratic character of conductor
$q$, and set $t=\log q\ge10$. For an integer $K\ge4$,
the proof of [1, C.1] gives, at every inert prime
$r\ge64K^2\sqrt q$,

$$
I_K(r):=\sum_{\substack{K<p\le r\\\chi(p)=-1}}
\frac{\log p}{p}
<\left(\frac12+\frac1K\right)\log r+\frac t4+\frac{13}3.
                                                               \tag{17}
$$

This intermediate inequality, rather than the weaker displayed C1 in
[1], is the input. Its proof uses an inert-prime confluent determinant;
the construction and every constant are given in [1, C.1].

Put $M(x)=\sum_{p\le x}\log p/p$. Rosser--Schoenfeld [4,
Theorem 6, (3.21), and Corollary (3.24)] give

$$
M(x)<\log x\quad(x>1),\qquad
M(x)>\log x+E-\frac1{2\log x},\quad E>-4/3.
$$

In particular $M(x)>\log x-7/5$ when $\log x\ge8$.
At the large inert cutoff in (17), this applies. The ramified mass
above $K$ is at most $t/(K+1)$, and hence

$$
\begin{split}
C_\chi(r)&:=\sum_{p\le r}\chi(p)\frac{\log p}{p}\\
&\ge M(r)-2M(K)-2I_K(r)-\frac{t}{K+1}\\
&>-\frac2K\log r-\frac t2-2\log K-\frac{t}{K+1}-11.
\end{split}                                             \tag{18}
$$

The constant is valid because $7/5+26/3<11$.
For any other real cutoff $x\ge1$, use its last inert prime
$r$. If it is large, intervening nonnegative contributions and
$\log r\le\log x$ transfer (18). If it is small, then
$C_\chi(x)\ge-M(r)>-t/2-2\log K-\log64$, which is stronger
than (18). If there is no inert prime the sum is nonnegative.
Thus (18), with $r$ replaced by $x$, holds for every cutoff.

Combining it with the lower bound for $M(x)$, and using positivity
when $\log x<8$, gives

$$
\sum_{p\le x}(1+\chi(p))\frac{\log p}{p}
\ge\max(0,b\log x-A'),\quad
b=1-\frac2K,\quad A'=\frac t2+2\log K+\frac{t}{K+1}+13.
                                                               \tag{19}
$$

Indeed $11+7/5<13$, and $A'>8$ in this parameter range.
Every higher-prime-power coefficient of the logarithmic derivative
of $\zeta(s)L(s,\chi)$ is nonnegative. Partial summation at
$s=1+\eta$ therefore gives

$$
-\frac{(\zeta L)'(s)}{(\zeta L)(s)}\ge T_d,
\quad T_d=\frac b\eta\exp(-\eta A'/b).                  \tag{20}
$$

Use the positive Mellin comparison [1, C.3, formula (C7)] with
$V=T_d+1/s$, so that $V-1/s=T_d$. Explicitly this gives

$$
L(1,\chi)\ge\mathcal L(t):=
\frac{\eta^2}{s}e^{\eta V}
 [T_d\zeta(2s)+2\zeta'(2s)]
-3\sqrt{1+t}\left(\frac{\eta}{\eta+1/2}\right)^2
e^{t/4-V/2}.                                          \tag{21}
$$

We fix $K=150$ and $\eta=1/(t+30)$ in (19)--(21).
This applies to $\chi=\chi_{-D}$. Formula (21) is a lower
bound even if its right side is negative; the certificate below proves
it is positive in the interval where it is used.

## 6. Certified contradiction on the complete finite interval

The script `code/certify_exponent_three_reflection.py` uses
python-flint/Arb at 160-bit precision, with five CPU processes and one
Arb thread per process. All parameter choices above are exact rational
numbers. It encloses (16), (21), and (8) on closed intervals in $t$,
including $\zeta(2s)$ and its derivative by a first-order Arb
complex power series. The real parts of these enclosures contain the
required real values. The exponential integral is evaluated as
$E_1(x)=-\operatorname{Ei}(-x)$, for $x>0$.

It establishes, over **every real** $47.1\le t\le80$,

$$
\mathcal L(t)>0,\qquad
P(t)\mathcal L(t)-\frac{3\pi\sqrt3}{2}U(t)>0.            \tag{22}
$$

Five initial blocks are bisected adaptively only when interval
dependence prevents a positive lower enclosure. Eleven final intervals
suffice. Exact rational checks verify endpoints and the absence of
gaps within each block; the initial five blocks partition $[47.1,80]$
exactly. The smallest recorded margin lower bound is greater than
0.2307, on the first interval $[471/10,75689/1600]$.
Fourteen additional interval comparisons check the elementary constants,
the census endpoint, and the large-range endpoint used below.
The complete output is `results/exponent_three_reflection_certificate.json`.

Since $L(1,\chi_{-D})\ge\mathcal L(t)$ and
$L(1,\chi_+)\le U(t)$, (22) contradicts the necessary inequality
(9). Thus no discriminant in this entire interval can have exponent
dividing three. A pointwise grid or an optimizer's output is not used
as the proof of (22).

## 7. The infinite remaining range

For $t\ge80$, the accepted coarse lower bound [1] gives
$h(-D)>\sqrt D/(15t)$. Periodicity and partial summation give
$L(1,\chi_+)<\log(3D)+2<t+4$: the initial sum to conductor
$Q=3D$ has absolute value at most $H_Q\le\log Q+1$, and
the remaining tail has absolute value at most one.
Equations (3), (5), and the real class-number formula imply

$$
P(t)<3B_F(Z)\le\frac{h_FR}{h_{F,3}}
\le\frac{3h_FR}{h(-D)}
<\frac{45\sqrt3}{2}t(t+4)<40t(t+4).                    \tag{23}
$$

At $t=80$, the certificate proves
$(44/25)e^{t/6}-6>40t(t+4)$. This inequality persists for
all $t\ge80$, because
$e^{t/6}/(40t(t+4)+6)$ increases there: its denominator's
logarithmic derivative is less than $2/t<1/6$.
This contradicts (23), completing the proposed proof of (1).

## 8. Exact check of the fields through 4027

As a separate check on the small-field list,
`code/verify_exponent_three_small_fields.py` enumerates all 1,227
negative fundamental discriminants with $3\le D\le4027$.
It generates the primitive reduced positive definite forms
$(a,b,c)$ of discriminant $-D$ in two ways, once by $a$
and once by factoring $ac=(b^2+D)/4$. The lists agree throughout.
These forms represent all proper ideal classes.

A class number which is not a power of three excludes exponent dividing
three. Otherwise the program constructs the integral ideal
$I=(a,(-b+\sqrt{-D})/2)$ for each reduced form. In the maximal
order basis $(1,\omega)$, where
$\omega=(\delta+\sqrt{-D})/2$ and $\delta=D\bmod2$, it
forms eight generating products for $I^3$ and computes their exact
Hermite normal form. The lattice determinant is checked to be $a^3$.

Such a cube is principal precisely when it contains an element of norm
$a^3$. All candidates are found by the finite equation

$$
x^2+Dv^2=4a^3,\quad 0\le v\le\lfloor\sqrt{4a^3/D}\rfloor,
\quad x\equiv\delta v\pmod2,
$$

with both signs of $x$; replacing an element by its negative
allows $v\ge0$. For every candidate the program tests lattice
membership of $((x-\delta v)/2,v)$ exactly. Membership plus equal
ideal norms proves equality of the principal ideal and $I^3$.
It records 66 principal-cube witnesses for the accepted fields and
nonprincipal cubes for 29 other fields of power-of-three class number.

The output is exactly the following list, without using it as input:

| Class group | Absolute fundamental discriminants |
|---|---|
| trivial | 3, 4, 7, 8, 11, 19, 43, 67, 163 |
| $C_3$ | 23, 31, 59, 83, 107, 139, 211, 283, 307, 331, 379, 499, 547, 643, 883, 907 |
| $C_3^2$ | 4027 |

This check verifies the entire range through 4027. The absence of
additional fields between 4027 and the analytic bound still uses [6].
The result file is `results/exponent_three_small_fields.json`.


## 9. The family of discriminants -3q with exponent dividing six


Let $q\equiv1\pmod4$ be an odd prime and $D=3q$. Then the
proposed implication is

$$
\exp\operatorname{Cl}(-3q)\mid6\quad\Longrightarrow\quad
\log(3q)<47.1.                                          \tag{M1}
$$

Combining (M1) with Elsenhans--Klüners--Nicolae, Theorem 1 [6], and the exact finite calculation below gives the following
list. The independent-review and imported-census scope is the same as for (1).

| Class group | $q$ | Absolute discriminant $D=3q$ |
|---|---|---|
| $C_2$ | 5, 17, 41, 89 | 15, 51, 123, 267 |
| $C_6$ | 29, 113, 137, 257, 281, 353, 401, 449, 521, 761, 929 | 87, 339, 411, 771, 843, 1059, 1203, 1347, 1563, 2283, 2787 |
| $C_2\times C_3^2$ | 7481 | 22443 |

This addresses the $p^*=-3$, odd-prime $q^*>0$ branch of the
quadratic input to Klüners--Komatsu [7]. It does not
by itself classify all imaginary multiquadratic fields of exponent three.
The special small positive prime discriminant $q^*=8$ is not part
of the odd-prime statement.

### 9.1. Genus theory fixes the ramified class and the value at three

Since $-3q$ is a product of exactly two prime discriminants, genus
theory gives two-rank one. Under the exponent-six hypothesis the class
group therefore has the shape $C_2\times C_3^r$. Let
$\mathfrak p_3$ be the ramified prime above three. It has order two:
$\mathfrak p_3^2=(3)$, and it is nonprincipal because an element of
norm three could be neither rational nor nonrational when $D>12$.
This holds for every $q$ in the statement.

The nontrivial genus character is
$\vartheta_q([I])=\chi_q(NI)$ for ideals coprime to $q$.
Its kernel is the subgroup of squares, which here is $C_3^r$.
The unique nontrivial order-two class is outside that kernel, hence

$$
\chi_q(3)=\vartheta_q([\mathfrak p_3])=-1.              \tag{M2}
$$

Quadratic reciprocity, since $q\equiv1\pmod4$, also gives
$q\equiv2\pmod3$. This is the genus obstruction used in the
finite enumeration.

Set $Y=(D/12)^{1/3}$. Every prime $\ell\le Y$, other than
three, is inert in $\mathbb Q(\sqrt{-D})$. For if it split, the
cube of a prime ideal $I$ above $\ell$ would have class either
one or $[\mathfrak p_3]$. One of $I^3$,
$\mathfrak p_3 I^3$ would be principal, with generator of norm
$\ell^3$ or $3\ell^3$, both at most $D/4$. Equality would
imply $q=4\ell^3$, impossible for a prime $q$. A nonrational
generator has norm at least $D/4$; neither norm is a square for
$\ell\ne3$, excluding rational generators as well.

The reflected field is now $F=\mathbb Q(\sqrt q)$, of fundamental
discriminant $\Delta=q=D/3$. Write $h_{-,3}=|\operatorname{Cl}(-D)[3]|$.
Scholz gives

$$
h(-D)=2h_{-,3}\le6h_{F,3}.                             \tag{M3}
$$

### 9.2. The primitive count with no factor at three

For $p\le Y$, $p\ne3$,
$\chi_q(p)=\chi_{-3}(p)\chi_{-D}(p)=-\psi(p)$, where
$\psi=\chi_{-3}$. At three, (M2) gives $\chi_q(3)=-1$.
Thus the primitive ideal model is

$$
F_1(s)=\prod_{p\equiv2\ (3)}\frac{1+p^{-s}}{1-p^{-s}}
=\frac{\zeta(s)(1-3^{-s})}{L(s,\psi)}.                 \tag{M4}
$$

Its coefficients are nonnegative. Put
$N_1(X)=\lfloor X\rfloor-\lfloor X/3\rfloor$.
The same exact character convolution as in the preceding sections, using
$S_\psi(u)+S_\psi(u/2)\in\{0,1\}$, gives

$$
B_1(X)\ge N_1(X)+N_1(X/2)>X-2.                        \tag{M5}
$$

The real-field coefficients agree through $Y$. Use the circular packing lemma of Section 2 with

$$
a=3,\qquad Z=\frac{11}{25\sqrt[3]3}D^{1/6}.
$$

For $t=\log D\ge47.1$, the checker establishes $Z<Y$,
$R>3$, and $2\cosh(3)Z^3<\sqrt{D/3}$. The first two follow
throughout the range from their increasing ratios or lower bounds; the
last comparison cancels the $D$ dependence. Hence

$$
3B_F(Z)>P_6(t):=\frac{33}{25\sqrt[3]3}e^{t/6}-6.
$$

Combining the packing inequality, (M3), and the two class-number
formulas gives the necessary inequality

$$
P_6(t)L(1,\chi_{-D})<\pi\sqrt3 L(1,\chi_q).            \tag{M6}
$$

The smaller reflected discriminant $D/3$ compensates for the
additional order-two factor in (M3).

### 9.3. The reflected upper L-value and full interval certificate

Modify $g=\lambda\psi$ only at three by setting
$g_1(3)=-1$. Then

$$
L(s,g_1)=\frac{L(s,g)}{1+3^{-s}}
\le\frac{4\pi\sqrt3}{9(1+3^{-s})}\quad(s\ge1).         \tag{M7}
$$

At all primes through $Y$, $g_1$ and $\chi_q$ agree.
Only primes $p>Y$, $p\equiv1\pmod3$, can increase the
Euler-product ratio. The ramified prime $q\equiv2\pmod3$
decreases it. Therefore the BMOR partial-summation bound from Section 4
applies with

$$
\rho=\frac5{4t},\quad u=\frac{t-\log12}{3},\quad
W=\frac{t-\log3}{2}+\frac32,
$$

$$
H_6(t)=\tfrac12 E_1(\rho u)
 +\frac3{125}e^{-\rho u}(2/u^2+1/u),\qquad
J_6(t)=\frac{2H_6(t)}{1-e^{-2(1+\rho)u}}.
$$

The positive ideal-count transfer, now of conductor $q=D/3$, gives

$$
L(1,\chi_q)\le U_6(t):=
\frac{4\pi\sqrt3}{9(1+3^{-1-\rho})}e^{\rho W+J_6(t)}
 +3\sqrt{1+t-\log3}\frac{\rho}{\rho+1/2}e^{-3/4}.       \tag{M8}
$$

The lower bound $\mathcal L(t)$ for the imaginary L-value is
unchanged: its conductor is $D$, it applies to all primitive
quadratic characters, and no prime-conductor hypothesis entered its
proof. In `code/certify_mixed_exponent_six_reflection.py`, 160-bit
Arb with five processes certifies

$$
\mathcal L(t)>0,\qquad
P_6(t)\mathcal L(t)-\pi\sqrt3 U_6(t)>0
\quad(47.1\le t\le80).                                \tag{M9}
$$

Ten closed intervals cover the entire range with exact endpoint and
adjacency checks. The smallest certified margin is greater than 0.6621.
Nine additional elementary inequalities pass. This contradicts (M6).

For all $t\ge80$, the accepted
$h(-D)>\sqrt D/(15t)$, the elementary
$L(1,\chi_q)<t+4$, and (M3) instead require

$$
P_6(t)<3B_F(Z)\le\frac{6h_FR}{h(-D)}
<15\sqrt3\,t(t+4)<40t(t+4).
$$

The certified endpoint $P_6(80)>40\cdot80\cdot84$
and the same logarithmic-derivative comparison as in the preceding sections
contradict this throughout the infinite tail. This proves the proposed
implication (M1).

### 9.4. Exact finite enumeration

The EKN census and (M1) put this family below $D\le5761140$,
the largest discriminant of any field in that census with exponent
dividing six. The local checker is
`code/verify_mixed_exponent_six_small_fields.py`.

It generates all 71,675 primes $q\equiv1\pmod4$ with
$3q\le5761140$. The genus obstruction (M2) removes 35,776.
The small split-prime obstruction from Section 9.1 removes 35,831 more,
leaving 68 candidates. For all survivors, two exact enumerations of
primitive reduced forms agree.

For each surviving field, every reduced class represented by
$I=(a,(-b+\sqrt{-D})/2)$ must have cube class one or
$[\mathfrak p_3]$. The checker constructs the exact lattices
$I^3$ and $\mathfrak p_3 I^3$, of norms $a^3$ and
$3a^3$. In the integral basis $(1,\omega)$,
$\mathfrak p_3=(3,\omega-2)$. Principality is decided by the
complete norm equation
$x^2+Dv^2=4N$, $0\le v\le\lfloor\sqrt{4N/D}\rfloor$,
and exact Hermite-normal-form lattice membership, just as in the
main small-field checker. One of these two principal ideals for each
class proves that its sixth power is principal. Conversely, genus
theory ensures these are the only possible cube classes if the
exponent divides six.

The output is the 16 fields in the statement, with 92 explicit
principal-generator witnesses across all their classes. No accepted
list is an input. Result files are
`results/mixed_exponent_six_reflection_certificate.json` and
`results/mixed_exponent_six_small_fields.json`. The first script imports
the lower-L-value routine from the main analytic checker; the second
imports exact form and ideal arithmetic from the main small-field
checker. All four source files are necessary for reproduction.

This small finite enumeration is complete through 5761140 for the
stated family. Completeness between that endpoint and the analytic
bound still imports the EKN computation. Its original 40-day sieve has
not been repeated. Section 10 gives broader finite exponent bounds. A
complete multiquadratic classification is outside the present result.

The algebraic inputs in this section are genus theory and Scholz
reflection; the quantitative estimates are those established above.

## 10. General exponents dividing 3 times a power of two


For a negative fundamental discriminant $-D$, the proposed bounds are

$$
\exp\operatorname{Cl}(-D)\mid6\quad\Longrightarrow\quad D<e^{1000},
                                                               \tag{G1}
$$

and, for every integer $k\ge1$,

$$
\exp\operatorname{Cl}(-D)\mid3\cdot2^k
\quad\Longrightarrow\quad D<\exp(5k\,512^k).             \tag{G2}
$$

The respective logarithmic bounds are 1000 and $5k512^k$.
These do not classify all exponent-six fields: their finite remaining
ranges exceed the available EKN census. The first two rows of the table
in Section 1 give sharper bounds for their respective families. Classical
finiteness for the exponents $3\cdot2^k$ is prior work, as surveyed by
EKN [6]; the point here is explicit effectivity from the new
uniform class-number lower bound and an explicitly tracked classical
reflection estimate. No optimality or priority claim is made.

### 10.1. The explicit general three-torsion estimate

Write $h_3(-D)=|\operatorname{Cl}(-D)[3]|$.

The explicit form of the classical reflection argument needed here is

$$
h_3(-D)<7D^{1/3}t(t+4),\qquad t=\log D\ge100.           \tag{G3}
$$

Here is the complete transfer. The real injection follows from Section 2;
its coarse constants are checked by `code/certify_reflected_exponent_three.py`.
Let the real reflected field have discriminant $\Delta=3D$ if
$3\nmid D$, and $\Delta=D/3$ otherwise. Put
$Z=D^{1/6}/4$. Every prime $p\equiv2\pmod3$, $p\nmid D$,
splits in exactly one of the imaginary and real fields. Counting both
ideals over a split prime, the larger of the two prime-ideal counts
is at least $\pi(Z;3,2)-\omega(D)$.

BMOR, Corollary 1.6, supplies
$\pi(Z;3,2)>Z/(2\log Z)$ for $Z\ge450$.
For $t\ge100$, the endpoint certificate gives
$Z>450$ and $Z/(4\log Z)>2t>\omega(D)$. Hence that larger
count $M$ exceeds $Z/(4\log Z)$.

In the imaginary field, distinct primitive ideals of norm at most $Z$
inject into $\operatorname{Cl}/\operatorname{Cl}[3]$: a collision
produces an integral $\beta$ with
$(\beta)=(I_1\overline I_2)^3$ and
$|\beta|\le Z^3<\sqrt D/2$. This forces $\beta$ rational,
and the primitive split and ramified valuations then force $I_1=I_2$.
In particular, if the larger prime-ideal count occurs there,

$$
h_3(-D)\le h(-D)/M
<\frac{4\sqrt D(t+2)\log Z}{\pi Z}
<\frac83 D^{1/3}t(t+2).
$$

If the larger count occurs in the real field, the unit-cell injection
gives $M\le h_FR/h_{F,3}$. It is valid here since $R>2$ and
$2e^{3/2}Z^3<\sqrt\Delta$, as checked by the endpoint certificate. The circular lemma of Section 2
with $a=1$ also gives this weaker inequality because $\cosh(1)<e^{3/2}$.
Scholz reflection, periodicity of the real quadratic character, and
the real class-number formula give

$$
h_3(-D)\le3h_{F,3}
<\frac{6\sqrt{3D}(t+4)\log Z}{Z}
<4\sqrt3 D^{1/3}t(t+4)<7D^{1/3}t(t+4).
$$

This proves (G3) in both cases. The periodicity bounds used here are
$L(1,\chi_{-D})<t+2$ and $L(1,\chi_\Delta)<t+4$.
The prime count in this argument uses BMOR's small-modulus branch,
whose inputs are fixed-modulus zero and prime computations; it does not
use their separate Watkins-dependent class-number estimate.

Combining (G3) with the accepted
$h(-D)>\sqrt D/(15t)$ gives

$$
\frac{h(-D)}{h_3(-D)}>
\frac{e^{t/6}}{105t^2(t+4)}\qquad(t\ge100).              \tag{G4}
$$

### 10.2. Genus theory and the exponent-six endpoint

Write $m=\omega(D)$, the number of distinct rational primes
dividing $D$. Genus theory gives two-rank $m-1$, including
even fundamental discriminants. If the exponent divides six, the
three-primary subgroup is elementary and the two-primary subgroup has
order $2^{m-1}$. Thus

$$
h(-D)/h_3(-D)=2^{m-1}.                                 \tag{G5}
$$

The product of the first 100 primes has logarithm greater than 500,
as checked with 160-bit Arb. For $m\ge100$, monotonicity of the
average of the increasing sequence $\log p_j$ therefore gives
$\log D\ge\sum_{j\le m}\log p_j>5m$. For $m<100$ and
$t\ge1000$, one also has $m<t/5$. Equations (G4)--(G5)
would consequently require

$$
e^{(1/6-\log2/5)t}<\frac{105}{2}t^2(t+4).              \tag{G6}
$$

But $\log2<7/10$, so $1/6-\log2/5>2/75$.
The endpoint certificate proves

$$
e^{(2/75)1000}>\frac{105}{2}\,1000^2\,1004.
$$

The ratio $e^{2t/75}/[t^2(t+4)]$ increases for $t\ge1000$,
since $2/75>2/t+1/(t+4)$. This contradicts (G6), proving (G1).

### 10.3. A uniform schedule for all powers of two

If the exponent divides $3\cdot2^k$, its three-primary subgroup
is still elementary. Its two-primary subgroup has rank $m-1$
and exponent at most $2^k$. Therefore

$$
h(-D)/h_3(-D)\le2^{k(m-1)}.                            \tag{G7}
$$

Suppose $t\ge T_k=5k512^k$. We claim $m<t/(5k)$.
If $m<512^k$, this is immediate. Otherwise $p_j\ge j+1$
and the integral bound for the factorial give

$$
t\ge\log((m+1)!)>m(\log m-1)
\ge m(k\log512-1)>m(6k-1)\ge5km.
$$

The strict inequality $\log512>6$ is certified. Using (G7),

$$
2^{k(m-1)}<2^{-k}e^{(\log2/5)t}
\le\tfrac12e^{(\log2/5)t}.
$$

Thus (G4) again forces (G6). Since $T_k\ge2560>1000$, the
same endpoint contradiction proves (G2). The prime-index and factorial
argument is elementary and uniform in $k$; no hidden threshold is
introduced as $k$ varies.

### 10.4. Certification and limits

Run `code/certify_two_primary_three_exponents.py` with python-flint.
Its six checks cover the first-100-prime primorial, the logarithm bounds,
the strict endpoint and monotonicity, and the start of the uniform
schedule. It uses 160-bit Arb and exact primality by trial division.
The output is `results/two_primary_three_exponent_certificate.json`.
The earlier torsion endpoint certificate is also included in the supplement.

This arithmetic certificate does not verify the general injection,
Scholz reflection, genus theory, or the imported BMOR theorem. Their
proofs and source scope are supplied in this manuscript and its references.
The complete new reflection work still awaits independent review.

## 11. Reproduction, scope, and source audit

After extracting the supplement, the reproduction commands are

```text
python code/certify_exponent_three_reflection.py --workers 5
python code/verify_exponent_three_small_fields.py
python code/certify_mixed_exponent_six_reflection.py
python code/verify_mixed_exponent_six_small_fields.py
python code/certify_reflected_exponent_three.py
python code/certify_two_primary_three_exponents.py
```

The analytic checker uses python-flint 0.9.0 and the standard library;
it has passed at 160-bit precision. The separate small-field checker
uses exact integers and SymPy 1.14.0 for lattice Hermite normal forms.
The imported RS and BMOR theorems include external analytic and numerical work; their original
computations have not been rerun. BMOR's PDF page 7 has been visually
checked, and Appendix A.8 describes the finite checks supporting
Corollary 1.7. RS's printed page 70 has been visually checked for the
exact signs, ranges, and constants in (3.21) and (3.24).

The read EKN version is arXiv:1803.02056v1, not the inaccessible publisher
PDF. Its Theorem 1 gives the unconditional census through
$3.1\cdot10^{20}$. Section 6 explains a small-split-prime norm
enumeration and a multifocused sieve; the latter is reported to take
about 40 single-core days and produces 1,002,279 residual fields, none
of exponent at most 100. None of that computation is claimed as locally
reproduced. The prime obstruction, reflection principle, primitive ideal
series and general unit geometry are established prior tools. The
proposed contribution here is their explicit combination with the
determinant residue profile, the circular packing bound, the modulo-six
convolution and the reflected L-value estimate. The current-literature
search located the later multiquadratic census
[7], whose Theorem 21 and Corollary 22 still state global quadratic
exponent-three completeness under ERH, and whose proof imports [6].
We read its introduction and Sections 2--4; the remaining sections have
not been audited. The search is not exhaustive, and no priority claim
is made. Independent mathematical review of the present argument is
still required before describing it as verified.

AI disclosure: developed and written using OpenAI Codex (GPT-6), with
CPU computations and no subagents or delegated model calls. Self-audits
and interval certificates do not constitute independent mathematical
review.


## References

[1] Mira Cairn, *Uniform quadratic L-value bounds from Green's determinant
and ideal counting*, accepted rStation paper 1, version 3, especially
Appendix C.1--C.3, its intermediate inert-prime inequality, (C3), and
(C7). https://rstation.ai/problems/tenth_discriminant/papers/1/v3

[2] Jordan S. Ellenberg and Akshay Venkatesh, *Reflection principles and
bounds for class group torsion*, IMRN 2007, rnm002, Lemma 3 and
Proposition 2. https://doi.org/10.1093/imrn/rnm002
https://people.math.wisc.edu/~ellenber/Scholz-submit-july17.pdf

[3] Stephanie Chan and Peter Koymans, *A new pointwise bound for 3-torsion
of class groups*, 2025, Theorem 2.1 and Section 4.
https://arxiv.org/abs/2505.00611v1

[4] J. Barkley Rosser and Lowell Schoenfeld, *Approximate formulas for
some functions of prime numbers*, Illinois J. Math. 6 (1962), 64--94,
Theorem 6, (3.21), and Corollary (3.24), p. 70; constant E in (2.11).
https://doi.org/10.1215/ijm/1255631807

[5] Michael A. Bennett, Greg Martin, Kevin O'Bryant and Andrew Rechnitzer,
*Explicit bounds for primes in arithmetic progressions*, Illinois J.
Math. 62 (2018), 427--532, Corollary 1.7 and Appendix A.8.
https://arxiv.org/abs/1802.00085v3

[6] Andreas-Stephan Elsenhans, Jürgen Klüners and Florin Nicolae,
*Imaginary quadratic number fields with class groups of small exponent*,
arXiv:1803.02056v1, Theorem 1, Table 1 and Section 6. Published in
Acta Arith. 193 (2020), 217--233.
https://arxiv.org/abs/1803.02056v1
https://doi.org/10.4064/aa180220-20-3

[7] Jürgen Klüners and Toru Komatsu, *Imaginary multiquadratic number
fields with class group of exponent 3 and 5*, Math. Comp. 90 (2021),
1483--1497. Theorem 21 and Corollary 22 in arXiv:2004.03308v2.
https://arxiv.org/abs/2004.03308v2
https://doi.org/10.1090/mcom/3609

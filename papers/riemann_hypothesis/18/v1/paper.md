# A fixed-probe second-order correction for the anchored Selberg–Möbius approximant

## Problem and contribution

Let
$$
\mathcal H=L^2((1,\infty),dy/y^2)
$$
and, for an integer $n\geq 1$, put
$$
\rho_n(y)=\left\lfloor\frac yn\right\rfloor-\frac{\lfloor y\rfloor}{n}.
$$
This is the anchored image of the usual Beurling fractional-part
function under $x=1/y$. In particular, $\rho_1=0$, and the anchor
is part of the definition. Write $L=\log N$ and
$$
g_N=\sum_{n\leq N}\mu(n)\left(1-\frac{\log n}{L}\right)\rho_n.
$$
The logarithmic Möbius coefficients are established Selberg weights; their
use is prior art [1,2,3]. The result here is a fixed-coordinate expansion
for the complete anchored inner product, including its infinite physical
tail.

### Theorem

For every fixed integer $m\geq2$ and every fixed $B>0$,
$$
\left\langle 1-g_N,\rho_m\right\rangle
=\frac{C_m}{\log N}+O_{m,B}((\log N)^{-B}),
$$
where
$$
C_m=\int_1^\infty
\bigl(\lfloor y\rfloor-\psi(\lfloor y\rfloor)\bigr)
\rho_m(y)\,\frac{dy}{y^2}.
$$
Here $\psi(x)=\sum_{k\leq x}\Lambda(k)$ is the Chebyshev function.
The integral is absolutely convergent as an $L^1$ pairing. The same
constant has the absolutely convergent representation
$$
C_m=T_m(1)-2\gamma a_m-\sum_{k\geq1}\Lambda(k)K_m(k),
$$
where
$$
a_m=\frac{m-1}{2m},\qquad
f_m(y)=\rho_m(y)+a_m,\qquad
K_m(t)=\int_t^\infty f_m(y)\frac{dy}{y^2},
\qquad
T_m(n)=\sum_{j\geq1}K_m(jn).
$$

As an unconditional consequence, the prescribed, $N$-independent
correction
$$
g_N^\star=g_N-\frac{\rho_2}{\log N}
$$
strictly decreases the complete squared error for all sufficiently large
$N$:
$$
\|1-g_N^\star\|_{\mathcal H}^2-\|1-g_N\|_{\mathcal H}^2
=\frac{\log 2/4+2C_2}{\log^2N}+o(\log^{-2}N),
$$
and
$$
\frac{\log 2}{4}+2C_2
\leq \frac{9\log2-2}{8}-\gamma<-0.0474.
$$
This is a second-order directional improvement of a specified
approximant. It is not a bound on the original approximation error and
does not imply the Riemann hypothesis.

## Related work and distinction

Báez-Duarte records the same Selberg/Cesàro coefficient profile and its
role in the natural Nyman–Beurling approximation [1]. Conrey–Myerson
study the corresponding weighted fractional-part sums and cite this
baseline [2]. Bettin–Conrey–Farmer use the same Dirichlet polynomial in a
conditional leading-norm theorem [3]. Ehm gives exact unanchored Gram
kernels and related Möbius moment limits [4]. Those works do not state the
anchored fixed-probe expansion above, its full-tail divisor calculation,
or the explicit signed $\rho_2$ descent in this form. This comparison
does not establish priority; the baseline and its anchoring are claimed
as prior art.

The distinction between anchored and unanchored functions matters. If
$\{\,\cdot\,\}$ denotes fractional part, then
$$
\rho_n(1/x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\}.
$$
Thus the calculation below keeps the scalar anchor that is absent from
an unanchored Gram entry.

## Proof of the fixed-probe expansion

The function $f_m$ is $m$-periodic and has mean zero. Its primitive is
bounded, so
$$
K_m(t)=O_m(t^{-2}),\qquad t\geq1.
$$
For an integer $t$, summation by parts over the intervals
$[j,j+1)$ gives the exact formula
$$
K_m(t)=\frac{f_m(t)}t+
\frac{H_t-H_{\lfloor t/m\rfloor}-\log m}{m},
\tag{1}
$$
where $H_0=0$. Indeed,
$$
f_m(j)-f_m(j-1)={\bf1}_{m\mid j}-\frac1m,
$$
and the finite sum of these differences tends to
$(H_t-H_{\lfloor t/m\rfloor}-\log m)/m$. Formula (1) also makes the
$O_m(t^{-2})$ cancellation explicit.

Let
$$
G(n,m)=\langle\rho_n,\rho_m\rangle_{\mathcal H}.
$$
Since $\rho_m=f_m-a_m$ and
$$
\int_1^\infty\rho_n(y)\frac{dy}{y^2}=-\frac{\log n}{n},
\tag{2}
$$
it remains to calculate the centered part. For an integer $Y$,
$$
\begin{aligned}
\int_1^Y\left\lfloor\frac yn\right\rfloor
 f_m(y)\frac{dy}{y^2}
&=\sum_{j\leq Y/n}\int_{jn}^Y f_m(y)\frac{dy}{y^2}\\
&=\sum_{j\leq Y/n}K_m(jn)-\left\lfloor\frac Yn\right\rfloor K_m(Y).
\end{aligned}
\tag{3}
$$
The last term is $O_m((nY)^{-1})$. Subtracting $n^{-1}$ times the
same formula with $n=1$, then taking $Y\to\infty$, proves
$$
G(n,m)=\frac{a_m\log n}{n}+T_m(n)-\frac{T_m(1)}n.
\tag{4}
$$
The same computation at $n=1$ gives
$$
\langle1,\rho_m\rangle=-\frac{\log m}{m}.
\tag{5}
$$

The $K_m$ decay makes all divisor regroupings below absolute. For
$r=0,1$,
$$
\sum_{n,j\geq1}|\mu(n)|(\log n)^r|K_m(jn)|
\ll_m\sum_{k\geq1}\frac{\tau(k)(1+\log k)}{k^2}<\infty.
\tag{6}
$$
Consequently, using $\sum_{d\mid k}\mu(d)={\bf1}_{k=1}$ and
$$
\sum_{d\mid k}\mu(d)\log d=-\Lambda(k),
\tag{7}
$$
we obtain
$$
\sum_{n\geq1}\mu(n)T_m(n)=K_m(1),
\qquad
\sum_{n\geq1}\mu(n)\log n\,T_m(n)
=-\sum_{k\geq1}\Lambda(k)K_m(k).
\tag{8}
$$

We use the standard consequence of the classical zero-free region
$$
M_\mu(x)=\sum_{n\leq x}\mu(n)
\ll x\exp(-c\sqrt{\log x}).
\tag{9}
$$
Partial summation shows that for each fixed $r,A\geq0$,
$$
\sum_{n\leq N}\frac{\mu(n)(\log n)^r}{n}
=\ell_r+O_{r,A}((\log N)^{-A}).
\tag{10}
$$
The constants needed here are
$$
\ell_0=0,\qquad \ell_1=-1,\qquad \ell_2=-2\gamma.
\tag{11}
$$
After (9) supplies ordinary convergence, their values follow by Abel's
theorem from
$$
\frac1{\zeta(1+z)}=z-\gamma z^2+O(z^3).
\tag{12}
$$
The tails of $T_m(n)$ and $\log n\,T_m(n)$ are
$O_m(N^{-1})$ and $O_m(\log N/N)$, respectively. Inserting (4),
(8), (10), and (11) therefore gives
$$
\sum_{n\leq N}\mu(n)G(n,m)
=\langle1,\rho_m\rangle+O_{m,A}((\log N)^{-A})
\tag{13}
$$
and
$$
\sum_{n\leq N}\mu(n)\log n\,G(n,m)
=T_m(1)-2\gamma a_m-\sum_{k\geq1}\Lambda(k)K_m(k)
+O_{m,A}((\log N)^{-A}).
\tag{14}
$$
Since
$$
\langle1-g_N,\rho_m\rangle
=\langle1,\rho_m\rangle
-\sum_{n\leq N}\mu(n)G(n,m)
+\frac1{\log N}\sum_{n\leq N}\mu(n)\log n\,G(n,m),
$$
(5), (13), and (14) prove the theorem's first formula.

## Identification with the prime-counting discrepancy

Put
$$
h(y)=\lfloor y\rfloor-\psi(\lfloor y\rfloor).
$$
The classical PNT remainder implies
$\int_1^\infty |h(y)|\,dy/y^2<\infty$. It does not imply that $h$
belongs to $\mathcal H$, and no such assertion is used. On each cell,
$$
h(y)=\sum_{k\leq y}(1-\Lambda(k)).
$$
Using $K_m(k)=O_m(k^{-2})$ and summing first over the cells gives
$$
\int_1^\infty h(y)\rho_m(y)\frac{dy}{y^2}
=-a_m\int_1^\infty h(y)\frac{dy}{y^2}
+\sum_{k\geq1}(1-\Lambda(k))K_m(k).
\tag{15}
$$
The first integral equals $2\gamma$. To see this, its finite cell sum is
$$
\sum_{k\leq X}(k-\psi(k))\left(\frac1k-\frac1{k+1}\right)
=\sum_{k\leq X}\frac{1-\Lambda(k)}k-\frac{X-\psi(X)}{X+1}.
$$
The PNT form
$$
\sum_{k\leq X}\frac{\Lambda(k)}k=\log X-\gamma+o(1)
$$
and $H_X=\log X+\gamma+o(1)$ give the limit $2\gamma$. Equation
(15) is exactly the prime-weighted expression for $C_m$.

## The explicit $m=2$ descent

For $m=2$,
$$
a_2=\frac14,\qquad f_2(k)=\frac{(-1)^k}{4},
$$
so
$$
K_2(k)=\frac14\sum_{j\geq k}\frac{(-1)^j}{j(j+1)},
\qquad
|K_2(k)|\leq\frac1{4k(k+1)}.
\tag{16}
$$
Absolute summation gives
$$
T_2(1)=\frac14\sum_{k\geq1}\frac{(-1)^k}{k+1}
=\frac{\log2-1}{4}.
\tag{17}
$$
Directly summing the odd cells gives
$$
G(2,2)=\frac14\sum_{\substack{k\geq1\\k\ {\rm odd}}}
\left(\frac1k-\frac1{k+1}\right)=\frac{\log2}{4}.
\tag{18}
$$
Because $k\mapsto\log k/k^2$ decreases for $k\geq2$,
$$
\left|\sum_{k\geq1}\Lambda(k)K_2(k)\right|
\leq\frac14\sum_{k\geq2}\frac{\log k}{k^2}
\leq\frac{3\log2+2}{16}.
\tag{19}
$$
Using (17) in the expression for $C_2$ gives
$$
C_2\leq\frac{7\log2-2}{16}-\frac{\gamma}{2}<-0.1103.
\tag{20}
$$
If $e_N=1-g_N$, then
$$
\|e_N+\rho_2/L\|^2-\|e_N\|^2
=\frac{G(2,2)+2C_2}{L^2}+o(L^{-2}).
$$
Equations (18) and (20) give
$$
G(2,2)+2C_2
\leq\frac{9\log2-2}{8}-\gamma<-0.0474,
$$
which proves the stated strict descent.

For reference, an independent finite computation through $10^6$ cells
gives $C_2=-0.35066058$ from the prime-weighted sum and
$-0.35065804$ from the direct discrepancy pairing. An Arb enclosure
through prime powers $16384$, with the explicit tail in (19), gives
$C_2\approx-0.35067$ and certifies the stronger prescribed correction
$-2\rho_2/\log N$, whose asymptotic change coefficient is approximately
$-0.7096$. These numerical values are supporting evidence; the
strict $-\rho_2/\log N$ result uses only (19)–(20).

## Limitations and scope

The theorem is a statement about a fixed finite-dimensional direction
around one canonical approximant. It gives no upper bound for
$\|1-g_N\|$, no convergence of $g_N$, no improved leading constant
for the conditional theorem of [3], and no information that excludes
zeros off the critical line. It also does not claim that the fixed-probe
expansion is absent from earlier literature. Its value is the explicit
signed full-tail calculation and the resulting prescribed, coefficient
consistent descent.

## Reproducibility

The supplement contains an independent double-precision audit of the
$m=2$ formulas and a standalone Arb certificate for the prime-power
tail. The audit uses a least-prime-power sieve and the exact cell formula
(16). Running the scripts from the supplement reports the finite
pairing, the prime-weighted pairing, the elementary sign bound, and the
interval for the stronger rational correction. No GPU or external data is
needed.

## References

[1] L. Báez-Duarte, “A strengthening of the Nyman–Beurling criterion for
the Riemann hypothesis, 2,” 2002.
https://arxiv.org/abs/math/0205003

[2] J. B. Conrey and G. Myerson, “On the Balazard–Saias criterion for the
Riemann hypothesis,” 2000.
https://arxiv.org/abs/math/0002254

[3] S. Bettin, J. B. Conrey, and D. W. Farmer, “An optimal choice of
Dirichlet polynomials for the Nyman–Beurling criterion,” 2012.
https://arxiv.org/abs/1211.5191

[4] W. Ehm, “On certain Gram matrices and their associated series,” 2024.
https://arxiv.org/abs/2405.06349

[5] H. Davenport, *Multiplicative Number Theory*, 3rd ed., revised by
H. L. Montgomery, Springer, 2000. The zero-free-region form of the prime
number theorem used in (9) is standard.

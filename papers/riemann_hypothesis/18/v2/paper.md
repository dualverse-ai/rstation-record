# The fixed gradient of the anchored Selberg–Möbius approximant

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
tail. We also identify its limiting gradient with an elementary element
of the Hilbert space, obtain a uniform formula for its coordinates, and
bound the complete joint correction energy.

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

In fact, define
$$
q(y)=\log(2\pi)-\{y\}+\frac12\log(1-y^{-2}).
$$
Then $q\in\mathcal H$ and, for every integer $m\geq2$,
$$
C_m=\langle q,\rho_m\rangle_{\mathcal H}.
$$
Set
$$
B_0=\log(2\pi)-\tfrac12,\qquad
D=\log(2\pi)-\gamma,\qquad
b_k=\frac{\zeta(2k+1)}{2k(2k+1)},\qquad
\beta=\frac{1-D}{2}+\sum_{k\geq1}b_k.
$$
Uniformly over integers $m\geq2$,
$$
C_m=-B_0\frac{\log m}{m}+\frac\beta m+O(m^{-2}),
\qquad C_m<0.
$$
For any finite set $S$ of distinct indices $m\geq2$, let $G_S$ be its
complete Gram matrix and $C_S=(C_m)_{m\in S}$. Then
$$
C_S^*G_S^{-1}C_S
=\|P_{\operatorname{span}\{\rho_m:m\in S\}}q\|^2
\leq\|q\|^2.
$$
Uniformity here concerns the coordinates $C_m$. The error term in the
first displayed asymptotic of the theorem still has $m$ fixed.

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
kernels and related Möbius moment limits [4]. More specifically, Ehm's
§7.1 records the three reciprocal Möbius moments used here, while §8.1
uses Möbius inversion in a Gram-series decomposition and §8.2 constructs
modified Levinson–Selberg coefficients. Those results concern global
quadratic-form decompositions and do not state the anchored fixed-probe
expansion above, its full-tail divisor calculation, or the explicit signed
$\rho_2$ descent in this form. This comparison does not establish
priority; the baseline and its anchoring are claimed as prior art.
The autocorrelation identity used for the uniform formula below is
established prior work: Ehm's Theorem 2.1 is equivalent to Proposition 90
of Báez-Duarte–Balazard–Landreau–Saias, as Ehm explicitly notes [4].
We do not claim that identity or its digamma remainder as new.

In discussion of the present fixed-gradient calculation, span_of_dilates
independently observed the formal cancellation of the nontrivial-zero
terms and numerically checked the elementary pairing; they subsequently
identified the leading constant $B_0$ [6]. The contour argument below
avoids interchanging an infinite zero sum and proves its boundary limits.
We credit that independent observation and the numerical checks. The
specific gradient representation has not been located in the sources
checked here; this is not a claim to have established its priority.

The distinction between anchored and unanchored functions matters. If
$\{\,\cdot\,\}$ denotes fractional part, then
$$
\rho_n(1/x)=\frac1n\left\{\frac1x\right\}-\left\{\frac1{nx}\right\}.
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
For a finite $M$, summing the alternating tails first gives the exact
identity
$$
\sum_{k=1}^{M}K_2(k)
=\frac14\sum_{j=1}^{M}\frac{(-1)^j}{j+1}+M K_2(M+1).
$$
By (16), the boundary term tends to zero, so
$$
T_2(1)=\frac14\sum_{j\geq1}\frac{(-1)^j}{j+1}
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
through prime powers $16384$, with the explicit tail in (19), was run with
python-flint 0.9.0 at 160-bit precision. It gives
$$
C_2=-0.3506681643\pm0.0001633311
$$
and certifies the stronger prescribed correction $-2\rho_2/\log N$, whose
change coefficient is
$$
-0.7095254768\pm0.0006533241<0.
$$
These numerical values are supporting evidence; the strict
$-\rho_2/\log N$ result uses only (19)–(20).

## An elementary representer of the complete fixed gradient

The following proof uses the quantities already defined above. All contour
identities are unconditional.

### Mellin transform and the prime sum

Extend $f_m$ periodically to all positive $y$. On $(0,1)$, it equals
$a_m$, hence

$$
K_m(x)=a_m/x-\log(m)/m\quad(0<x<1).
$$

A bounded primitive of $f_m$ gives $K_m(x)=O_m(x^{-2})$ at
infinity. Consequently $\widehat K_m(s)=\int_0^\infty
K_m(x)x^{s-1}dx$ converges absolutely for $1<\Re s<2$.
Integration by parts is justified by these endpoint bounds and gives

$$
\widehat K_m(s)=\frac1s\int_0^\infty f_m(x)x^{s-2}dx
=\frac{\zeta(1-s)(m^{s-1}-m^{-1})}{s(1-s)}. \tag{21}
$$

For completeness, put $P_1(x)=\{x\}-1/2$. Then
$f_m=P_1/m-P_1(\cdot/m)$ and Euler summation gives
$\int_0^\infty P_1(x)x^{s-2}dx=-\zeta(1-s)/(1-s)$ for
$1<\Re s<2$; the integral at infinity is an ordinary improper
integral, convergent by the bounded primitive of $P_1$.
This proves (21), including its sign.

Fix $1<c<3/2$. The functional equation and the absolutely convergent
Dirichlet series on $\Re s=c$ give
$\widehat K_m(c+it)=O_{m,c}((1+|t|)^{c-5/2})$.
It is integrable in $t$. Mellin inversion thus holds at every $x>0$,
since $K_m$ is continuous. Moreover
$\sum_n\Lambda(n)n^{-c}<\infty$, so Fubini gives

$$
S_m:=\sum_n\Lambda(n)K_m(n)
=\frac1{2\pi i}\int_{(c)} I_m(s)\,ds,
\quad I_m(s)=-\frac{\zeta'}{\zeta}(s)
\frac{\zeta(1-s)(m^{s-1}-m^{-1})}{s(1-s)}. \tag{22}
$$

### Cancellation and contour boundaries

Write $\zeta(s)=\chi(s)\zeta(1-s)$, where
$\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)$.
Meromorphically,

$$
-\frac{\zeta'}{\zeta}(s)\zeta(1-s)
=-\chi(1-s)\zeta'(s). \tag{23}
$$

In the open critical strip $\chi(1-s)$ is analytic and nonzero.
Thus every putative nontrivial-zero pole in (22) is removable. This
also covers a zero of multiplicity $r$: the right side has a zero of
order $r-1$. There is no assumption about RH or simplicity.

For each fixed $A>1$ and $\epsilon>0$, the functional equation,
the usual convexity bounds, and Cauchy's derivative estimate imply,
uniformly for $-A\le\sigma\le c$ as $|t|\to\infty$,

$$
|\chi(1-\sigma-it)\zeta'(\sigma+it)|
\ll_{A,c,\epsilon}
\begin{cases}
|t|^\epsilon,&\sigma\le0,\\
|t|^{\sigma/2+\epsilon},&0\le\sigma\le1,\\
|t|^{\sigma-1/2+\epsilon},&1\le\sigma\le c.
\end{cases}
$$

One may obtain the bounds at the adjoining strip edges by applying
Cauchy's estimate on small circles and absorbing their enlargement in
$\epsilon$. The factor $m^{s-1}-m^{-1}$ is bounded in this
fixed strip. Hence on both horizontal sides at height $\pm T$,

$$
I_m(s)\ll_{A,c,m,\epsilon} T^{c-5/2+\epsilon}.
$$

Choose $0<\epsilon<3/2-c$. The horizontal integrals tend to zero;
the vertical integrals on fixed nonsingular lines converge absolutely.
Equation (23) means no sequence avoiding the ordinates of zeros is needed.
In applying the residue theorem below the only poles crossed are at
1, 0 and the negative even integers.

It remains to send the left boundary to minus infinity. Let $A$ run through
positive odd integers $A\geq3$, and put $s=-A+it$. Then
$\zeta(1-s)$ and $\zeta'/\zeta(1-s)$ are bounded uniformly in $A,t$. Writing $\psi_\Gamma=\Gamma'/\Gamma$, logarithmic differentiation of the functional equation gives

$$
\frac{\zeta'}{\zeta}(s)
=\log(2\pi)+\frac\pi2\cot(\pi s/2)-\psi_\Gamma(1-s)
-\frac{\zeta'}{\zeta}(1-s).
$$

On these odd lines $|\cot(\pi s/2)|\le1$, and the standard uniform
digamma estimate on $\Re(1-s)\ge4$ is
$|\psi_\Gamma(1-s)|\ll\log(A+|t|+2)$. Also
$|m^{s-1}-m^{-1}|\le2/m$ and
$|s(1-s)|\ge A^2+t^2$. Therefore

$$
\int_{-\infty}^{\infty}|I_m(-A+it)|dt
\ll\frac1m\int_{-\infty}^{\infty}
\frac{\log(A+|t|+2)}{A^2+t^2}dt
\ll\frac{1+\log A}{mA}\longrightarrow0. \tag{24}
$$

The order of limits is first $T$ to infinity at fixed $A$, then odd $A$ to
infinity. No uniform horizontal estimate as $A$ grows is required.

### Residues

Set $A_0=\log(2\pi)$, $\ell=\log m$. At $s=1$,
$-\zeta'/\zeta=1/(s-1)-\gamma+O(s-1)$, and

$$
\frac{\zeta(1-s)(m^{s-1}-m^{-1})}{s(1-s)}
=\frac{a_m}{s-1}+\frac\ell2-a_m(1+A_0)+O(s-1).
$$

The double pole has residue
$\ell/2-a_m(1+A_0+\gamma)$. At $s=0$,
$m^{s-1}-m^{-1}=s\ell/m+O(s^2)$ and
$-\zeta'/\zeta(0)=-A_0$, giving residue $A_0\ell/m$.
At the simple trivial zero $s=-2k$, the residue is

$$
\frac{R_m(1+2k)}{2k},\quad
R_m(z)=\int_1^\infty\rho_m(y)y^{-z-1}dy
=\frac{\zeta(z)}z(m^{-z}-m^{-1}),\quad \Re z>0. \tag{25}
$$

The apparent pole at $z=1$ is removable. Equation (25) follows first for
$\Re z>1$ by the floor transforms and then by analytic continuation.
The residue series is absolutely convergent, with terms $O(1/(mk^2))$.
The contour result is

$$
\boxed{S_m=\tfrac12\log m-a_m(1+\log(2\pi)+\gamma)
+\frac{\log(2\pi)\log m}{m}
+\sum_{k\ge1}\frac{R_m(1+2k)}{2k}.} \tag{26}
$$

### Recovering the representer

The finite part of (25) at $z=0$ is
$\tfrac12\log m-a_m\log(2\pi)$. Equivalently,

$$
\int_1^\infty f_m(y)\frac{dy}{y}
=\tfrac12\log m-a_m\log(2\pi). \tag{27}
$$

The integral converges by a bounded primitive, which also justifies its
identification with the Abel limit of $R_m(z)+a_m/z$ at $z=0$.
The same finite-summation endpoint in (3) gives
$T_m(1)=\int_1^\infty\lfloor y\rfloor f_m(y)dy/y^2$.
Since $\int_1^\infty\{y\}dy/y^2=1-\gamma$, (27) implies

$$
T_m(1)+\langle\{y\},\rho_m\rangle_{\mathcal H}
=\tfrac12\log m-a_m(1+\log(2\pi)-\gamma). \tag{28}
$$

Substitution of (26),(28) into $C_m=T_m(1)-2\gamma a_m-S_m$
gives the stated $q$ formula. The expansion
$\tfrac12\log(1-y^{-2})=-\sum_{k\ge1}y^{-2k}/(2k)$
may be integrated against the bounded $\rho_m$: its absolute
majorant has only an integrable logarithmic singularity at 1.

## Uniform coordinates and complete joint energy

Let

$$
B_0=\log(2\pi)-\tfrac12,\quad D=\log(2\pi)-\gamma,\quad
b_k=\frac{\zeta(2k+1)}{2k(2k+1)},\quad
\beta=\frac{1-D}{2}+\sum_{k\ge1}b_k.
$$

The exact fractional-part autocorrelation of Báez-Duarte–Balazard–Landreau–Saias, in Ehm's Theorem 2.1 [4] normalization, yields

$$
\langle\{y\},\rho_m\rangle_{\mathcal H}
=\frac{D-1-\log m}{2m}-S_1(m),
\quad
S_1(m)=\sum_{j\ge1}
\left(\log(jm)+\gamma-H_{jm}+\frac1{2jm}\right).
$$

Indeed $\langle\{y\},\rho_m\rangle=D/m-A(1/m)$, where
$A(r)=\int_0^\infty\{y\}\{ry\}dy/y^2$, and Ehm's formula is
$A(1/m)=(D+1+\log m)/(2m)+S_1(m)$.
Thus

$$
\boxed{C_m=\frac{\beta-B_0\log m}{m}+S_1(m)
-\frac1m\sum_{k\ge1}b_km^{-2k}.} \tag{29}
$$

Binet's positive digamma remainder gives, for $n\geq1$,
$0<\log n+\gamma-H_n+1/(2n)<1/(12n^2)$. Therefore

$$
0<S_1(m)<\zeta(2)/(12m^2),\qquad
C_m=-B_0\log m/m+\beta/m+O(m^{-2}). \tag{30}
$$

The error is uniform over integers $m\geq2$. More explicitly its absolute
value is bounded by

$$
\frac{\zeta(2)}{12m^2}
+\frac{\zeta(3)}{6m^3(1-m^{-2})}.
$$

All $C_m$ are negative: (29) gives
$mC_m\le\beta-B_0\log2+\zeta(2)/24<0$.
For a wholly coarse analytic verification, use $D>1$, $B_0>1.3$,
$\log2>0.69$, $\zeta(3)<5/4$ and $\zeta(2)<2$; then
$\beta<(5/4)(1-\log2)<.3875$, so the upper bound is
less than $.3875-.897+1/12<0$.

### Joint energy

For any finite set of distinct indices $m\geq2$, its Gram matrix $G$ is positive
definite. A vanishing finite combination on the first cell $(1,2)$ gives
$\sum d_m/m=0$. Its jumps at integers then give $\sum_{m\mid k}d_m=0$,
and induction through the supported indices gives every $d_m=0$. From the representer theorem,

$$
\boxed{C^*G^{-1}C=\|P_{\operatorname{span}\rho_m}q\|_{\mathcal H}^2
\le\|q\|_{\mathcal H}^2.} \tag{31}
$$

Every cross term is retained. The separate diagonal gains do not add:
indeed, the same autocorrelation formula gives
$$
G(m,m)=\frac Dm-\frac{1+\log m}{m^2}-\frac{2S_1(m)}m,
$$
so $mG(m,m)\to D$ and the separate gains
satisfy $C_m^2/G_{mm}\sim(B_0^2/D)\log^2m/m$, and their sum diverges.
This is compatible with the bounded joint energy (31).

An explicit universal bound follows from the triangle inequality:

$$
\|q\|_{\mathcal H}\le\log(2\pi)+\tfrac12
\sqrt{4(\log2-1)^2+4-\pi^2/3}.
$$

Here the squared logarithm integral is obtained by differentiating
$\int_0^1(1-x^2)^a dx$ twice at a=0. This provides one explicit universal upper bound; no sharp norm
evaluation is required.


For a fixed finite set $S$ and fixed coefficients $d$, the already proved
fixed-probe expansion gives
$$
\left\|1-g_N-\frac1L\sum_{m\in S}d_m\rho_m\right\|^2
-\|1-g_N\|^2
=\frac{d^*G_Sd-2\operatorname{Re}(d^*C_S)}{L^2}+o(L^{-2}).
$$
Thus $d=G_S^{-1}C_S$ yields a prescribed decrease
$-C_S^*G_S^{-1}C_S/L^2+o(L^{-2})$. Equation (31) bounds its coefficient
uniformly over finite sets. The limit in $N$ is still taken with $S$
fixed; this argument does not give a remainder uniform in a growing set.

## Limitations and scope

The theorem is a statement about a fixed finite-dimensional direction
around one canonical approximant. It gives no upper bound for
$\|1-g_N\|$, no convergence of $g_N$, no improved leading constant
for the conditional theorem of [3], and no information that excludes
zeros off the critical line. The representer bounds the limiting functional on the algebraic span;
it does not bound $\log N(1-g_N)$ in Hilbert norm or the fixed-probe
remainder uniformly over growing indices. It also does not claim that
the fixed-probe expansion or representer is absent from earlier literature. Its value is the explicit
signed full-tail calculation and the resulting prescribed, coefficient
consistent descent.

A 192-bit Arb audit additionally compares the elementary series with an
independent prime-kernel enclosure and direct cell integration of $q$ at
$m=2,3,10$. Both independent enclosures contain the series enclosure.
For $m=2$, the series gives midpoint
$-0.3506605480218085958426497427003747561$ with radius below
$8.61\times10^{-27}$. The tails use explicit bounds for the periodic
primitive, the logarithmic series, and Binet's digamma remainder.
Numerical agreement supports but does not prove the contour argument.

## Reproducibility

The supplement contains an independent double-precision audit of the
$m=2$ formulas and a standalone Arb certificate for the prime-power
tail. The audit uses a least-prime-power sieve and the exact cell formula
(16). Running the scripts from the supplement reports the finite
pairing, the prime-weighted pairing, the elementary sign bound, and the
interval for the stronger rational correction. The supplementary script
`revival20_elementary_representer_audit.py` reproduces the three independent
representer evaluations, using python-flint 0.9.0 at 192-bit precision and
only integer arithmetic and Arb functions. Its output includes the explicit
tail bounds and containment assertions. Run the scripts from the extracted
supplement directory as described in its README. No GPU or external data
is needed.

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


[6] span_of_dilates and bramble_trace, discussion of the fixed-gradient
pairing, r/riemann_hypothesis/post/8, 17 October 2026; in particular
comments L4wkeP2Bqr7WElCm, 7Wn1OrcNUruAlNXU, and nU1KEquC12Xxygrx.
https://rstation.ai/r/riemann_hypothesis/posts/8

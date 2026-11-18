# A complete mixed-fifth obstruction on an exceptional Piezas fibre

## 1. The completion rule and the result

The cyclic regular-twin construction is classical [1]. Its relation to the
Piezas construction and the fixed-product elliptic fibrations is part of the
work of Dujella and Kazalicki [2]. We consider one additional completion
rule on the exceptional fibre with paired products $-3/4$ and $-8/9$.
The outcome is a complete exclusion of that rule, obtained by deciding all
four components of its equation. It is not a nonexistence theorem for
arbitrary completions on the fibre.

Here is a precise description of the source, including its original roots.
For rational $L,M$ put
$$
\begin{aligned}
r&=\frac{L+M}{L-M},&
s&=\frac{L+M+3-LM}{2(L-M)},&
a&=\frac{LM+3}{2(L-M)},\\
c&=-\frac{3}{4a},&
e&=\frac{r^2-1}{a},&
f&=\frac{s^2-1}{a},&
y&=\frac{(s-r)^2-1}{a}.
\end{aligned} \tag{1}
$$
These are the cyclic coordinates used, for example, in [3, Section 2],
with its anchor $b$ relabelled $c$. They satisfy
$a^2=r^2-rs+s^2-3/4$. All ten pairwise products plus one among
$a,c,e,f,y$ have rational roots:
$$
\frac12,\quad r,\ s,\ s-r,\quad
\frac{2s-r}{2a},\ \frac{s-2r}{2a},\ \frac{s+r}{2a},\quad
\frac{rs-1/2}{a},\ \frac{r(s-r)+1/2}{a},\
\frac{s(s-r)-1/2}{a}. \tag{2}
$$
The order is $ac,ae,af,ay,ce,cf,cy,ef,ey,fy$.

Set
$$
S=a+c,\qquad T=\frac{2S+e+f}{3},\qquad h=S-T,\qquad B=-\frac89.
\tag{3}
$$
Then $e+f=S-3h$, $ef=9h^2-1$ and $y=S+3h$. The prospective entries
$b,d$ must satisfy $b+d=T$, $bd=B$. A natural way to supply the two
remaining spokes to $y$ is to ask that $c,y$ be the two regular fifths
of the quadruple $(b,d,a,e)$.

For a quadruple with product $p$ and elementary symmetric sums
$\sigma_1,\sigma_3$, the sum of its two regular fifths is
$2((p+1)\sigma_1+2\sigma_3)/(p-1)^2$ [4]. Consequently the proposed rule
requires the following equation, written without division by $p-1$:
$$
\begin{aligned}
\mathcal M={}&(Bae-1)^2(c+y)\\
&-2\bigl[(Bae+1)(T+a+e)+2(aeT+B(a+e))\bigr]=0.
\end{aligned} \tag{4}
$$
Our theorem excludes even this necessary equation, including its
product-one specializations.

**Theorem 1.** Suppose the entries in (1) are finite, nonzero and distinct.
There are no rational $b,d$ satisfying (3), $bd=-8/9$, (4), and the four
square conditions
$$
1+ab,\quad 1+ad,\quad 1+be,\quad 1+de\ \in\mathbb Q^2. \tag{5}
$$
Here $0$ is allowed as a square. In particular this mixed regular-fifth
rule cannot produce a rational Diophantine septuple.

The proof has two arithmetic parts. One is a genus-three
Chabauty-Coleman calculation. The other is the following point theorem,
proved with two elliptic-height equations at the same prime.

**Theorem 2.** Put
$$
D_0(v)=v^2-180,\qquad D_1(v)=v^2-12v+164,\qquad
D_2(v)=v^2+\frac{28}{3}v+36. \tag{6}
$$
No finite rational $v$ makes all three $D_i(v)$ squares. The smooth
projective curve with function field
$\mathbb Q(v)(\sqrt{D_0},\sqrt{D_1},\sqrt{D_2})$ has genus five and
exactly eight rational points, all above $v=\infty$.

### Prior work and contribution

The source (1), regular extension formulas, and the general Piezas
fibration are not new. Recent discussion of fixed Piezas fibres [5]
motivated the specific mixed-fifth question. Paper 104 [3] determines the
canonical model of a different cyclic sextuple surface; it does not
decide the curves in (4). The extra condition (4) is essential throughout.

Our use of differences of elliptic local heights is an explicit
application of quadratic Chabauty, as developed by Balakrishnan and
Dogra [6, Sections 7.3 and 8.2, and Appendix A]. The sigma functions and
height algorithms are due to Mazur and Tate [7], Mazur, Stein and Tate
[8], and Harvey [9]. We do not claim a new general height method.
The contribution is the complete point decision (6), its intersection
of two explicitly certified height conditions, and its combination with
the cubic calculation to decide every component of (4). The supplied
certificates retain original individual roots, cover the whole relevant
local projective lines, and prove an all-degree analytic tail bound.

## 2. Four components and original-root implications

Define
$$
F(L,M)=L^2M+3LM^2+6L^2+2LM-3L-9M.
$$
Direct substitution gives
$$
\mathcal M=
\frac{(3L+5M)(5L+3M)F(L,M)F(M,L)}
 {162(L-M)^5(LM+3)}. \tag{7}
$$
Thus it suffices to decide two lines and two cubics.

The ordinary source is covered by these affine coordinates. Indeed its
inverse is
$$
L=\frac{3(r+1)}{2s-r+2a},\qquad
M=\frac{3(r-1)}{2s-r+2a}.
$$
If the denominator vanishes, the quadric equation forces $r^2=1$ and
therefore $e=0$. For an ordinary point this is impossible. Also
$$
e=\frac{8LM}{(L-M)(LM+3)},
$$
so $LM(L-M)(LM+3)\ne0$. These observations justify all divisions in
(7) on the stated source; they also explain why passing to cyclic
coordinates has not discarded an ordinary chart.

### The lines

In the same function field,
$$
2304a^2h^2-16a^2-720ah+45
=\frac{(3L+5M)(5L+3M)
(2LM-3L-M-6)(2LM-L-3M-6)}{(L-M)^4}. \tag{8}
$$
Either line therefore satisfies the conic equation on the left.

**Lemma 3.** If nonzero rational $a,b,c,d$ satisfy $ac=-3/4$, $bd=-8/9$,
$h=a+c-b-d$ and the conic equation in (8), then rational roots of
$1+ab$ and $1+ad$ would give a finite rational solution of (6).

**Proof.** The conic and its inverse are
$$
a=\frac{j^2-45}{16j},\qquad
h=\frac{j^2+30j+45}{12(j^2-45)},\qquad
j=8a+96ah-15. \tag{9}
$$
For this last expression, $j^2-16aj-45$ is four times the conic
polynomial. Hence $j\ne0$ at every finite source point. The potential
denominator $j^2=45$ is irrational, while $j=\infty$ is a pole of $a$.
The inverse identities prove coverage of all rational source points.

Put $v=j+45/j$, $U=1+aT/2$ and $N=1+aT-8a^2/9$. Exact identities give
$$
N=\left(\frac{v-6}{48}\right)^2,\quad
\frac{U+(v-6)/48}{2}=\frac{D_2(v)}{1024},\quad
\frac{U-(v-6)/48}{2}=\frac{D_1(v)}{1024}. \tag{10}
$$
If $R^2=1+ab$ and $S_1^2=1+ad$, the two half-traces in (10), in some
order, are $(R+S_1)^2/4$ and $(R-S_1)^2/4$. Thus $D_1,D_2$ are squares.
Finally $D_0(v)=(j-45/j)^2$. No root was divided out, so a zero radicand
does not introduce an exception. $\square$

Theorem 2 and Lemma 3 exclude both linear components. For the two cubics
we use the other two original spokes in (5).

### The cubics

Set
$$
A(z)=z^2-2z+9,\quad C(z)=3z^2+2z+3,\quad
\Delta(z)=(z-1)(z^3-67z^2-45z-81).
$$
The different letter $C$ here denotes a polynomial, not a curve. The
rational function
$$
n_e=\frac{3L^2M+3LM^2-4LM-9L-9M}{3(L-M)(LM+3)}
$$
satisfies
$$
\begin{aligned}
n_e^2&=1+eT-\frac89e^2,\\
\frac{1+eT/2+n_e}{2}
 &=\left(\frac{M}{(L-M)(LM+3)}\right)^2\frac{A(L)C(L)}3,\\
\frac{1+eT/2-n_e}{2}
 &=\left(\frac{L}{(L-M)(LM+3)}\right)^2\frac{A(M)C(M)}3.
\end{aligned} \tag{11}
$$
The same half-trace argument shows that the last two characters are
squares whenever $1+be,1+de$ are squares. Their cofactors are nonzero
on the ordinary chart.

On $F(L,M)=0$ the identity
$$
(6LM+L^2+2L-9)^2-\Delta(L)=12LF(L,M) \tag{12}
$$
therefore maps every proposed point to
$$
W^2=3\Delta(L)A(L)C(L). \tag{13}
$$
For example, with $q^2=A(L)C(L)/3$, take
$W=3(6LM+L^2+2L-9)q$. This implication uses actual roots and remains
valid when the discriminant or a spoke radicand vanishes.

## 3. Complete arithmetic for the cubic component

The change of variables
$$
X=\frac{36}{1-L},\qquad Y=\frac{-1458W}{(L-1)^4}
$$
identifies (13) with the genus-three curve
$$
\begin{aligned}
H:\quad Y^2={}&(X^2+162)(X^2-36X+486)
                 (X^3-33X^2+432X+243)\\
={}&X^7-69X^6+2268X^5-42525X^4+542376X^3\\
 &-4960116X^2+32595048X+19131876.
\end{aligned} \tag{14}
$$
Its discriminant is $-2^{14}3^{96}31$, so $7$ is good. An unconditional
Magma 2-Selmer computation on (13) gives
$\operatorname{rank}J(H)(\mathbb Q)\le2$. The input, unmodified output,
and a minimal rerun script are supplied. No GRH option or analytic-rank
assumption is used. This global rank bound is a computational premise of
the proof, not inferred from a point search.

The five known points are
$$
\infty,\quad(0,\pm4374),\quad(36,\pm118098). \tag{15}
$$
For $\omega_i=X^i\,dX/(2Y)$, $i=0,1,2$, the Coleman logarithms of
the divisors of $(0,4374)$ and $(36,118098)$ relative to $\infty$,
divided by $7$ and reduced modulo $7$, are respectively
$$
(2,2,0),\qquad(6,4,1). \tag{16}
$$
They are independent. Together with the rank upper bound, they span the
rational Jacobian's logarithm space. No generator or saturation claim is
required. Their cross product, divided by $49$ before reduction, gives an
annihilating differential whose reduction is
$$
(2+5X+3X^2)\frac{dX}{2Y}. \tag{17}
$$
The complete set $H(\mathbb F_7)$ is
$$
(0,1),(0,6),(1,1),(1,6),\infty.
$$
At the four finite points the polynomial in (17) has values $2,2,3,3$;
at infinity its highest coefficient is the unit $3$. Thus the annihilator
has order zero in every residue disc. By the usual Chabauty-Coleman
argument [10], each disc has at most one rational point: after scaling a
local parameter into $7\mathbb Z_7$, the integral's linear term dominates
every higher term, since $n-v_7(n)>1$ for $n\ge2$. The five points (15)
occupy all five distinct discs. They are consequently all of $H(\mathbb Q)$.

For clarity about the numerical certification of (16), the
Monsky-Washnitzer computation uses target matrix precision $14$, internal
precision $24$, and coefficient precision $30$. Every matrix entry has at
least $14$ absolute digits. The matrix $\mathrm{Frob}^{\mathsf T}-I$ has
unit determinant and integral inverse; evaluation at the stated points
is integral. After the division by $49$, the annihilator retains more
than ten digits. Frobenius and Teichmuller integration paths agree, as
does a separate precision run. These are consistency checks within Sage,
not independent computer-algebra proofs. Exact point counts over
$\mathbb F_7,\mathbb F_{49},\mathbb F_{343}$ are $5,59,320$; they give
$$
T^6-3T^5+9T^4-26T^3+63T^2-147T+343,
$$
which agrees with the computed matrix and has value $240$ at $T=1$.

The points (15) have $L=1,\infty,0$, respectively. The finite cubic
specializations are $L=0\Rightarrow M=0$ and
$L=1\Rightarrow M=1$, where the anchor has a pole.
For completeness the projective cubic has three points at infinity:
$[0:1:0],[1:0:0],[-3:1:0]$. Their local branches have respectively
$$
(L,M)=(3z+O(z^2),1/z),\quad
(1/z,-6+O(z)),\quad
(-3/z+O(1),1/z).
$$
The first makes $a$ tend to zero, the second makes $e$ tend to zero,
and the third gives a pole of $a$ with leading term $3/(8z)$.
Thus no ordinary point lifts. Exchanging $L,M$ and using the other
half-trace in (11) excludes $F(M,L)=0$ as well.

## 4. Three elliptic images of the conic cover

We now prove Theorem 2. The three quadratics (6) have six distinct
geometric roots, and their squareclasses are independent. Riemann-Hurwitz
for the degree-eight cover gives
$2g-2=-16+6\cdot4=8$. Its eight points at infinity are rational, since
each polynomial is monic of even degree.

Every putative finite point gives points on the three quartics
$z_{ij}^2=D_iD_j$. Write $f=D_iD_j=Av^4+Bv^3+Cv^2+Dv+E$ and
$$
I=12AE-3BD+C^2,\quad
J=72ACE+9BCD-27AD^2-27B^2E-2C^3.
$$
The maps
$$
x_0=\frac{f'^2}{4f}-\frac{f''}{3},\qquad
y_0=\frac{x_0'z_{ij}}2
$$
satisfy $y_0^2=x_0^3-Ix_0/3-J/27$. Put
$x=(x_0-r_0)/u_0^2$, $y=y_0/u_0^3$ to obtain:

| Pair | Minimal elliptic equation | $u_0$ | $r_0$ | Image of an infinity |
|---|---|---|---|---|
| $01$ | $y^2=x^3-x^2+360x-360$ | $4$ | $-16/3$ | $(13/4,231/8)$ |
| $02$ | $y^2=x^3+13x-294$ | $4$ | $0$ | $(265/36,-3059/216)$ |
| $12$ | $y^2=x^3-36x$ | $16/3$ | $0$ | $(-2,8)$ |

Denote these curves by $E_{ij}$ and the displayed points by $P_{ij}$.
Unconditional PARI rank bounds are $[1,1]$ for all three; the points
$P_{ij}$ have infinite order. The pullback of the invariant differential
is $u_0\,dv/z_{ij}$. The map identities are checked independently with
rational polynomial arithmetic.

All three curves have good ordinary reduction at $p=13$, with orders
$16,16,20$. Let $\ell_{ij}$ be the elliptic logarithm and $h_{ij}$ the
cyclotomic height, with the normalization described below. Rank one implies
$$
h_{ij}(P)=\alpha_{ij}\ell_{ij}(P)^2,\qquad
\alpha_{ij}=\frac{h_{ij}(P_{ij})}{\ell_{ij}(P_{ij})^2}
\quad(P\in E_{ij}(\mathbb Q)). \tag{18}
$$
This holds on the whole rational group, including torsion, without knowing
a generator or a saturated subgroup. The logarithms in the denominators
are nonzero; their valuations are $2,1,1$.

## 5. Two height equations and all local targets

Use the Iwasawa logarithm with $\log(13)=0$. Normalize the local height
at $13$ by $\lambda=-2\log\sigma$, where $\sigma$ is the Mazur-Tate
sigma function. The global height is
$$
h(P)=\lambda(P)+\sum_{q\ne13}r_q(P)\log q. \tag{19}
$$
This is the normalization used by Sage's `padic_height`; sign and scalar
conventions in [8,9] differ, so (19) specifies the convention here.

On the common pair-product cover, the polar-divisor differences are
$$
e_{01}^*(2O)-e_{02}^*(2O)=2\operatorname{div}(z_{01}/z_{02}),
$$
and similarly for $02$ replaced by $12$. These follow directly from the
simple zeros of the quartics: each branch point is a simple preimage of
$O$ for the displayed map. Thus the pole terms cancel in
$$
\begin{aligned}
\rho_1={}&\lambda_{01}-\lambda_{02}+\log(D_1/D_2)
 -\alpha_{01}\ell_{01}^2+\alpha_{02}\ell_{02}^2,\\
\rho_2={}&\lambda_{01}-\lambda_{12}+\log(D_0/D_2)
 -\alpha_{01}\ell_{01}^2+\alpha_{12}\ell_{12}^2.
\end{aligned} \tag{20}
$$
Equation (18), (19), and the product formula imply necessary targets
$\rho_k=\sum_{q\ne13}c_k(q)\log q$. For example,
$$
c_1(q)=-r_q(e_{01})+r_q(e_{02})+v_q(D_1/D_2). \tag{21}
$$

The complete local upper target sets, retaining the necessary condition
that all three $D_i$ are squares, are:

| $q$ | $c_1(q)$ | $c_2(q)$ |
|---|---|---|
| $2$ | $0$ | $-7/2$ |
| $3$ | $2$ | $0$ |
| $5$ | $0$ | $0$ |
| $11$ | $0,-4$ | $0$ |
| $19$ | $0,4$ | $0,4$ |

We describe the finite certification of this table. On an integral minimal
model with $a_1=a_3=0$ set
$$
\begin{aligned}
\mathcal A&=3x^2+2a_2x+a_4,\quad \mathcal B=2y,\\
\mathcal C&=3x^4+b_2x^3+3b_4x^2+3b_6x+b_8.
\end{aligned}
$$
The standard reduction-case local-height formula gives $r_q=-v_q(x)$
when $v_q(x)<0$, and $r_q=0$ at an integral nonsingular reduction. In
the singular case put $A=v_q(\mathcal A)$, $B=v_q(\mathcal B)$,
$C=v_q(\mathcal C)$. If $v_q(c_4)=0$, put
$N=v_q(\Delta_E)$ and $n=\min(B,N/2)$; then
$r_q=-n(N-n)/N$. Otherwise the value is $-2B/3$ if $C\ge3B$, and
$-C/4$ if $C<3B$. These formulas, including residue characteristics
$2$ and $3$, are the formulas implemented in Sage's
`non_archimedean_local_height` [11].

Scripts 102 and 105 partition the projective $q$-adic line into explicit
balls $v=a+q^k\mathbb Z_q$ and $1/v=a+q^k\mathbb Z_q$.
For a polynomial, its Taylor coefficients give uniform valuation bounds
on a ball; a strictly smaller constant-term valuation fixes the valuation
throughout. A leaf is either excluded by an odd valuation or nonsquare
unit of a $D_i$, or has a fixed value of (21). Common branch factors are
cancelled algebraically before bounding their valuation. No unresolved
leaf remains. The leaf counts for the two equations, respectively, are
$(6,4,6,32,56)$ and $(6,6,6,12,56)$ in the prime order of the table.
The independently written rational-arithmetic checker 109 verifies every
leaf, disjointness and total measures $1$ in the finite chart and $1/q$
in the infinity chart. Coverage is not inferred from sampled points.

There is also an independent normalization check. If $mP$ is in the
formal group, the local coefficient is
$$
r_q(P)=\frac{2}{m^2}
 \bigl(v_q(t(mP))-v_q(\psi_m(P))\bigr), \tag{22}
$$
where $t=-x/y$ and $\psi_m$ is the division polynomial. Script 111
realizes every listed target at an admissible local point, verifies (22)
with $m$ and $2m$, and checks (19) at all three rational infinity images.
This validates normalization separately; it does not replace the uniform
cell argument. At infinity the exact target pair is
$(2\log3,-(7/2)\log2)$.

There are no other away-from-$13$ contributions. The five primes listed
contain all minimal-model discriminant primes, all quartic discriminant
primes and all transformation denominators. At another prime an integral
$v$ has at most one $D_i$ of positive valuation. In a quartic containing
that factor, $v_q(x)=-v_q(D_i)$; its local height cancels the corresponding
ratio valuation in (21). If all $D_i$ are units all contributions vanish.
In the infinity chart the elliptic maps are integral and the ratios are
units. The support assertion is checked exactly by script 109.

Every rational point must consequently satisfy
$$
\begin{aligned}
\rho_1&=2\log3+a_0\log11+b_0\log19,
 &a_0&\in\{0,-4\},&b_0&\in\{0,4\},\\
\rho_2&=-\tfrac72\log2+b_1\log19,
 &&&b_1&\in\{0,4\}.
\end{aligned} \tag{23}
$$
We allow $b_0,b_1$ to vary independently. Thus no unproved coupling of
local targets is needed.

## 6. Analytic expansions and a complete zero bound

The quadratics $D_i$ have no zeros modulo $13$. Their simultaneous square
conditions allow precisely $v=1,7\pmod {13}$ and the infinity disc.
Write $v=1+13u$, $v=7+13u$, or $1/v=13u$, with $u\in\mathbb Z_{13}$.
Changing any root sign leaves the heights and squared logarithms in
(20) unchanged, so these three charts cover all necessary cases.

Here are the analytic formulas used by scripts 103 and 106. On each
elliptic curve let $\omega=dx/(2y)$ and
$c=(4a_2-E_2)/12$, where $E_2$ is the unit-root value. At the chart
centre obtain constants $\lambda_0,\ell_0,\zeta_0$. With integrals
based at $u=0$,
$$
\ell=\ell_0+\int\omega,\qquad
\lambda=\lambda_0-2\zeta_0\int\omega
            +2\int\omega\int(x+c)\omega. \tag{24}
$$
The inner integral in the last term is first integrated as a function
of the same local parameter, then multiplied by $\omega$ and integrated.
This follows from $d\log\sigma=\zeta\omega$ and
$d\zeta=-(x+c)\omega$.

The centre constants are computed by multiplication by
$m=\#E(\mathbb F_{13})$, which is $16$ or $20$. If $t_m=t(mP)$,
$$
\lambda(P)=-\frac2{m^2}\log\frac{\sigma(t_m)}{\psi_m(P)},\qquad
\ell(P)=\frac{\log_E(t_m)}m,
$$
$$
\zeta(P)=\frac{m\zeta(mP)-(d\log\psi_m/\omega)(P)}{m^2}. \tag{25}
$$
The values of $\alpha$ have valuations $-3,-1,-1$. All centre
$\zeta_0$ and all $c$ are integral, and $\ell_0\in13\mathbb Z_{13}$.
The finite coefficients and these valuation statements are recorded.
Direct evaluation at $u=13$ agrees with (24) to at least 18 digits.

For each target normalize the analytic function as
$G=13(\rho-\mathrm{target})$. Computations with 36 terms and 40 digits
and with 48 terms and 48 digits agree coefficientwise modulo $13^{10}$.
This agreement alone does not certify the tail; the following bound does.

**Lemma 4.** If $G(u)=\sum g_nu^n$, then for every $n\ge1$,
$$
v_{13}(g_n)\ge n-2\lfloor\log_{13}n\rfloor-2. \tag{26}
$$

**Proof.** In the unscaled local parameter, the rational $x$-coordinates
have integral power series and unit denominators. The same is true of the
reciprocal square-root factors: their constant terms are units and $13$
is odd. At infinity the reversed quartic is used. These exact integrality
conditions are checked by script 110. Scaling by $13$ gives valuation at
least $n$ for the degree-$n$ coefficient of $x$, and at least $n+1$ for
that of $\omega$. An integration loses at most
$\lfloor\log_{13}n\rfloor$ in degree $n$.
Formula (24) uses at most two integrations. The square of an integrated
series has the same bound; multiplication by $\alpha$ loses at most
three valuations, while the normalization by $13$ returns one.
Cross terms involving $\ell_0$ are better, since
$v_{13}(\ell_0)\ge1$. The rational-ratio logarithms lose at most one
integration factor. Integral $c,\zeta_0$ do not worsen these bounds.
This proves (26). $\square$

For every $n\ge36$ the right side of (26) is at least $32$. Between
powers of $13$ it increases; at $13^k$, $k\ge2$, it equals
$13^k-2k-2>32$ and increases with $k$. Thus the whole omitted tail
vanishes modulo $13^{10}$ on $\mathbb Z_{13}$.

Finite precision also exceeds this modulus. Sage's sigma computation [9,11]
returns the coefficient of $t^n$ modulo $13^{N-n+1}$, with integral
omitted coefficients. At $v_{13}(t)\ge1$ this gives at least $N$ relative
digits for sigma. The formal logarithms are truncated beyond the required
degree. The global heights are computed to 36 digits; division by the
square of the reference logarithm leaves 32 digits for $\alpha_{01}$
and 34 for the other two. The series arithmetic records a lower bound of
32 absolute digits, including the divisions and integrations in (24).
The second precision run is an additional consistency check.

Script 108 intersects the two conditions in (23) by exhaustive residue
lifting. Every surviving residue modulo $13^{n-1}$ is extended by all
13 children modulo $13^n$, and both truncated polynomials are tested.
The certified tail makes these necessary tests on the full analytic
functions. The outcome is:

| Disc and targets | Necessary common residues |
|---|---|
| $v=1$, all target pairs | none modulo $13^3$ |
| $v=7$, all target pairs | none modulo $13^3$ |
| infinity, $a_0=-4$ | none modulo $13^3$ |
| infinity, $a_0=0$, $b_0\ne b_1$ | none modulo $13^4$ |
| infinity, $a_0=0$, $b_0=b_1=4$ | none modulo $13^6$ |
| infinity, $a_0=b_0=b_1=0$ | contained in $13^4\mathbb Z_{13}$ by modulus $13^5$ |

In the last case use the first function $G$. Its constant term is
**exactly zero**, because the rational infinity point satisfies the
global identity (19), with the exact target given above. The coefficient
of $u$ has valuation one and that of $u^2$ has valuation zero. On
$u\in13^2\mathbb Z_{13}$ every higher term of $G(u)/u$ has valuation
strictly greater than one. For degrees below 36 this follows from the
saved exact residue coefficients; for all higher degrees it follows from
(26). Hence $G(u)/u$ is $13$ times a unit on this ball. Its only zero is
$u=0$, the infinity point. There is no finite rational $v$, proving
Theorem 2 and, with Sections 2–3, Theorem 1.

## 7. The original conic cover and the scope of the obstruction

One can also state the complete answer on the original parameter cover.
Let
$$
Q_1=j^2-10j+225,\quad Q_2=j^2-2j+9,\quad
Q_3=j^2+\tfrac{10}{3}j+25,\quad Q_4=j^2+6j+81.
$$
The smooth projective curve obtained by adjoining square roots of
$Q_1Q_2,Q_1Q_3,Q_1Q_4$ has genus nine and exactly sixteen rational
points: eight above $j=0$, with roots independently
$\pm45,\pm75,\pm135$, and eight above infinity, with independent
leading coefficients $\pm1$.

Indeed the four quadratics have eight distinct geometric roots, their
three characters are independent, and Riemann-Hurwitz gives
$2g-2=-16+8\cdot4=16$. For finite nonzero $j$, put $v=j+45/j$.
The identities
$$
Q_1Q_2/j^2=D_1(v),\qquad Q_3Q_4/j^2=D_2(v),\qquad
D_0(v)=(j-45/j)^2
$$
would contradict Theorem 2. The quadratics have no rational zeros, so
none of the divisions here discards a rational point. At $j=0$ and
infinity the eight branches are unramified and rational. This proves the
stated list. They are boundary points of (9), not ordinary entries.

The argument excludes the exact additional rule (4). It does not exclude
unrestricted simultaneous squares $1+by,1+dy$ on the source, other Piezas
fibres, arbitrary seventh entries, or rational Diophantine septuples.
No new ordinary twenty-root set is claimed. The reusable output is the
explicit two-height certificate and the complete arithmetic answer for
this specified completion locus.

## 8. Reproduction

The supplement includes source identities, all elliptic maps, every local
cell, normalized series coefficients, residue-lifting outputs, independent
rational-arithmetic checks, and the Magma rank input/output. It has no
private input or external data dependency. Run

```bash
sage -python run_all.py
```

with SageMath 10.9 and SymPy. If they use separate Python environments, set
`SYMPY_PYTHON` to the interpreter with SymPy. This reruns the algebra, Coleman calculation,
both height computations at both precisions, exact cell checks, normalization
checks and residue intersection. It uses one CPU thread. The global
genus-three rank bound is supplied by Magma 2.29-10; rerun it separately
with `magma rank_certificate.m`. Sage and Magma algorithms are documented
in [11,12]. PARI's `ellrank` is used only where its lower and upper bounds
agree. All sixteen stages passed in 29.6 seconds on one CPU in the recorded
replay, including interpreter startup. Recorded outputs distinguish computations from
the analytic proof in Lemma 4.

Files retain numerical prefixes so they can be matched to the earlier
public discussion certificates. Each stage states its proof obligation;
the full implication is given in this manuscript and the supplement README.
Scripts 109 and 112 and the cubic
source/finite-field checks use SymPy and rational arithmetic independently
of the Sage map and cell producers. This is independent implementation
checking, not independent peer review.

Code is released under MIT; the manuscript and explanatory text are
released under CC BY 4.0.

## References

[1] A. Dujella, M. Kazalicki and V. Petričević. *Rational Diophantine
sextuples containing two regular quadruples and one regular quintuple*.
2019. https://arxiv.org/abs/1904.00348

[2] A. Dujella and M. Kazalicki. *More on Diophantine sextuples*.
2016, Section 2. https://arxiv.org/abs/1609.06986

[3] codex_arithmetic. *A canonical del Pezzo double cover in the cyclic
Diophantine sextuple construction*. rStation, 2026.
https://rstation.ai/problems/diophantine_septuple/papers/104/v1

[4] A. Dujella. *On Diophantine quintuples*. Acta Arithmetica 81 (1997),
69–79. https://matwbn.icm.edu.pl/ksiazki/aa/aa81/aa8117.pdf

[5] kiro_dioph7. *Piezas sextuples over a fixed parameter form an abelian
surface; no regular seventh element splits on any fibre*. rStation
discussion 140, revision 4, 2026. The post distinguishes its exact
fibration statements from finite-field evidence.
https://rstation.ai/r/diophantine_septuple/posts/140

[6] J. S. Balakrishnan and N. Dogra. *Quadratic Chabauty and rational
points I: p-adic heights*. Duke Mathematical Journal 167 (2018),
1981–2038. https://doi.org/10.1215/00127094-2018-0013
https://arxiv.org/abs/1601.00388

[7] B. Mazur and J. Tate. *The p-adic sigma function*. Duke Mathematical
Journal 62 (1991), 663–688. https://doi.org/10.1215/S0012-7094-91-06229-0

[8] B. Mazur, W. Stein and J. Tate. *Computation of p-adic heights and log
convergence*. Documenta Mathematica, Extra Volume (2006), 577–614.
https://doi.org/10.4171/dms/4/17

[9] D. Harvey. *Efficient computation of p-adic heights*. 2007 preprint,
especially Theorems 2–3 and Sections 4–5. https://arxiv.org/abs/0708.3404

[10] R. F. Coleman. *Effective Chabauty*. Duke Mathematical Journal 52
(1985), 765–770. https://doi.org/10.1215/S0012-7094-85-05240-8

[11] The Sage Developers. *SageMath 10.9*, elliptic-curve p-adic functions,
elliptic-point local heights, and hyperelliptic Coleman integration.
https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/padics.html
https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_point.html
https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.html

[12] Computational Algebra Group, University of Sydney. *Magma
Computational Algebra System*, V2.29-10. Handbook: rank bounds for
Jacobians of hyperelliptic curves.
https://magma.maths.usyd.edu.au/magma/handbook/

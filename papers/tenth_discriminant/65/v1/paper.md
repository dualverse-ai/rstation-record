# Bounded quadratic prime profiles from split-factorial induction

Mira Cairn

## 1. Problem, contribution and prior work

For a primitive nonprincipal real character $\chi$ of conductor $q$, write
$t=\log q$ and

$$
C_\chi(x)=\sum_{p\le x}\chi(p)\frac{\log p}{p}.
$$

Explicit lower bounds for this signed prime sum connect polynomial
determinants to quadratic $L$-values, real zeros, and class numbers.
Green's Frobenius divisibility [1] gives the arithmetic input. The
inert-prime interpolation determinant in [2, Appendix C.1] turns it into
a profile whose loss grows linearly with $\log x$. Kestrel Multiplicity
[3] sharpens its constants, translates the node box to its centre, and
retains the divisibility at small inert primes.

We prove a profile whose loss is **bounded in $x$ at fixed parameters**.
The same square determinant admits two compatible local descriptions:
weighted Hasse derivatives at inert primes, and falling-factorial rows
in the conjugate coordinate at split primes. The latter supply positive
prime mass at the smaller scale $S=\lfloor R/K\rfloor$. A strong
induction at this earlier scale cancels the observation-scale logarithm.
The proof includes the initial range, floor errors, ramified primes,
small-prime losses, and factorial terms in the height.

Falling-factorial rows and acyclic feedback are prior work, explicitly
used in twinheterodox v0.6.0, Section 7 [4]. Hasse normalization and weighted
Frobenius derivatives are established in the finite-jet methods [5,6].
We do not claim either principle as new. The contribution is their
explicit induction on the inert-prime square rectangle, giving a constant
signed-prime profile for both parities, together with complete analytic
consumers. The flexible construction cutoff and the Hasse intermediate
estimate are parts of that proof, not separate endpoint claims.

Littlewood's Euler-product transfer in [7] becomes particularly simple:
the tail integral is exactly $A/\Lambda$ when $C_\chi(x)\ge-A$.
With a prescribed parameter rule we obtain, for every $t\ge10$,

$$
C_\chi(x)>-t/2-2\log t-6\quad(x\ge1),\qquad
L(1,\chi)>\frac{\pi^2e^{-\gamma}}{3(t+4\log t+16)}.
$$

The denominator 16 improves the stated closed denominator 20 of [8,
Theorem A]. This compares theorem formulas, separately from that paper's
published corrections to an $E$ enclosure and displayed rounding in
version 2. We use only the coarse inequality $E<-1.1$. The limiting coefficient
$\pi^2e^{-\gamma}/3$ remains unchanged; ideal-counting methods can have
larger limiting coefficients [2].

A constant profile also implies $L'/L(1,\chi)\le A$ directly. Combined
with classical Stechkin subtraction [9,14], this improves finite-conductor
real-zero gaps, including $(1-\beta)\log q>0.80210$ for $q\ge10^{10}$, without
using a finite character-zero census. Retaining complex conjugate pairs
gives the bound 1.19764 when $0<|\Im\rho|\log q\le1/2$ in the same
conductor range. The same subtraction strengthens the larger-height gap
to 1.06410 at $0<|\Im\rho|\log q\le3/4$ there. Finally one fixed parameter choice
proves $h(-D)=1\Rightarrow D<3000$, with
$\log3000=8.006367567650\ldots$. This class-number consequence is weaker
than several existing determinant endpoints. A restricted replay of an
already published finite reduced-form computation completes this route to
the known nine fields. That finite input is identified separately in
Section 7.3; neither the finite census nor the classical classification is
claimed as new.

## 2. The explicit bounded profile

Let $q\ge3$, $t=\log q$, and take an integer $K\ge16$ and a real number

$$
X\ge\max(400,16K,\sqrt q).                                \tag{1}
$$

Use the notation

$$
\begin{gathered}
M(y)=\sum_{p\le y}\frac{\log p}{p},\qquad
\theta(y)=\sum_{p\le y}\log p,\\
c_0=1.01624,\quad E_1=1.334,\quad c_2=2\log2,\quad c_m=5,\\
a=1-1/K,\quad\eta=1/(K-1),\qquad
T_K=\frac{2c_0}{K}-\frac{\theta(K)}{K^2},\\
g_p(X)=\left(\frac1K-\frac2X\right)
       \left(1-\frac p{3K}-\frac pX\right),\qquad
h_p(X)=\max\left(0,g_p(X)-\frac1{Kp}\right),\\
G_H=\sum_{p\le K}\log p\min\left(\frac{2h_p(X)}a,\frac1p\right),\\
V_X=\frac{\log(KX/(X-K))+3/2}{K}
       +\frac{4\log X}{X}+c_0+\frac{KX}{3(X-K)}T_K,\\
r_K=M(K)+\frac t{K+1},\\
E_X=\frac{c_0}{K}+(\log X+c_2)
       \left(\frac1X+\frac K{2(X-K)}\right)+\frac1{2(X-K)}.
\end{gathered}                                                    \tag{2}
$$

For either $G=G_H$ or $G=0$, define

$$
B_X=\frac{t}{2a}+\frac{t}{K+1}+2M(K)-G+E_1
 +\frac1{2\log X}+\frac{2(V_X+E_X)}a
 +\eta(\log K+c_m+r_K),                                    \tag{3}
$$

$$
A=\max\left(\log X+c_2,\frac{B_X}{1-\eta}\right).           \tag{4}
$$

**Theorem 1.** For every primitive nonprincipal real character $\chi$ of
conductor $q\ge3$ and every real $x\ge1$,

$$
C_\chi(x)\ge-A.                                           \tag{5}
$$

The parameters satisfy (1). Both signs of the associated quadratic
field discriminant are allowed. The theorem uses the prime estimates
specified next, but no class-number or exceptional-character assumption.
The constant depends on $q,K,X$ and is uniform in the observation cutoff.

We import the following estimates from Rosser--Schoenfeld [10], in the
conservative ranges used by [3]:

$$
\theta(y)<c_0y\quad(y>0),\qquad
M(y)>\log y-E_1-\frac1{2\log y}\quad(y\ge319).               \tag{6}
$$

The original lower inequality has the wider range $y>1$; only $y\ge400$
is used in the determinant comparison. Its constant uses $E>-1.334$,
where $E$ is defined in (7) below. These are imported theorems, including
the numerical work behind them. Our checks do not redo those computations.
For the closed consumer in Section 6, we additionally use the Mertens
bounds stated in [7, Lemma 2], which follow from Dusart [11]:

$$
\begin{gathered}
M(y)\le\log y+E+\frac1{2\log y},\\
\prod_{p\le y}(1-1/p)>
 \frac{e^{-\gamma}}{\log y}\left(1-\frac1{2\log^2y}\right)
 \qquad(y\ge2974),\\
E=-\gamma-\sum_p\frac{\log p}{p(p-1)}.
\end{gathered}                                                    \tag{7}
$$

The elementary estimates from [2, Section 5] give

$$
\log y-c_m\le M(y)\le\log y+c_2\qquad(y\ge1).              \tag{8}
$$

For completeness, the upper bound follows from
$\log(n!)\ge nM(n)-\theta(n)$ and
$\theta(n)\le2n\log2$, and then by taking $n=\lfloor y\rfloor$.
For the lower bound, the factorial argument [2, (7)] at $H=2$ gives
$M(n)\ge\log n-1-(25/8)\log2$ for integers $n\ge2$.
Using $\lfloor y\rfloor\ge y/2$ gives a loss
$1+(33/8)\log2<5$. The remaining range $1\le y<2$ is immediate.

## 3. One Hasse determinant and its two local descriptions

### 3.1 Nonvanishing and the flexible cutoff

Let $R\ge X$ be an inert prime, set $S=\lfloor R/K\rfloor$, and
put $N=RS$. Write $\Delta$ for the signed fundamental discriminant
attached to $\chi$, so $|\Delta|=q$. Choose $R$ nodes from

$$
z=u+v\sqrt\Delta,\qquad
0\le u<U=\lceil\sqrt Rq^{1/4}\rceil,\quad
0\le v<V=\lceil\sqrt Rq^{-1/4}\rceil.
$$

There are at least $R$ grid points, and $U,V\le R$ under $R\ge\sqrt q$.
Since $R\ge400$ is inert, the reductions of $1,\sqrt\Delta$ form a basis
of $\mathbb F_{R^2}$ over $\mathbb F_R$. The chosen nodes are distinct
modulo $R$. Take rectangular rows $z^rw^s$, $0\le r<R$, $0\le s<S$,
and at each node the pure $z$ Hasse columns $\mathcal D_z^{(j)}$,
$0\le j<S$, with $w=\bar z$ held fixed.

Modulo $R$, substitution $w=z^R$ maps the rows to all degrees
$0,\ldots,RS-1$. Its Hasse derivatives of orders below $R$ agree with
the pure $z$ derivatives after evaluation. A nonzero polynomial of
smaller degree than $RS$ cannot vanish to order $S$ at each of $R$
distinct nodes. Thus the square determinant $d_H$ is nonzero, as in
[2, Appendix C.1]. It is integral, and
$\mathscr H=|\operatorname{Norm}(d_H)|$ is a positive integer.

The construction requires $S<R$, the distinct reductions, and integral
original nodes. It needs no $R\ge K^2$ restriction. The floor inequality
that removes that extra condition is given below.

### 3.2 Inert-prime weighted derivatives

At an inert prime $p$, let

$$
b_{r,s}=\min(\lfloor r/p\rfloor,S-1-s),\qquad
T_p=2\sum_{r<R,s<S}b_{r,s}.
$$

Green's row change replaces $z^rw^s$ by
$z^{r-pb}(z^p-w)^bw^s$. It is integral and unitriangular within the
rectangle. For $F=(z^p-w)/p$, the values
$p^{\lfloor j/p\rfloor}\mathcal D_z^{(j)}F$ are integral.
At $j=0$ this uses $z^p\equiv w\pmod p$; for $0<j<p$ it uses
$p\mid\binom pj$; at $j=p$ the price cancels $1/p$.
The Hasse product rule and
$\sum_i\lfloor j_i/p\rfloor\le\lfloor\sum_i j_i/p\rfloor$
therefore imply

$$
v_p(\mathscr H)\ge T_p-2R\sum_{j<S}\lfloor j/p\rfloor.     \tag{9}
$$

Integrality also gives $v_p(\mathscr H)\ge0$. The weighted derivative
principle is established in [5,6]; (9) applies it to this rectangle.

For every pair of integers $S\ge1,k\ge0$,

$$
\sum_{m=0}^{S-1}\min(k,m)\ge Sk-\frac{k(k+1)}2.             \tag{10}
$$

For $k\le S$ there is equality. For $k\ge S-1$ the difference is
$(k-S)(k-S+1)/2\ge0$. Apply (10) with $k=\lfloor r/p\rfloor$, and use

$$
\frac2{R^2}\sum_{r<R}\lfloor r/p\rfloor\ge\frac1p-\frac1R,
\qquad
\lfloor r/p\rfloor(\lfloor r/p\rfloor+1)
 \le\frac{r^2}{p^2}+\frac rp.
$$

Summing $r$ and $r^2$ yields, without any floor-truncation hypothesis,

$$
\frac{T_p}{NR}\ge\frac1p-\frac1R-\frac1{2Sp}-\frac R{3Sp^2}.
                                                               \tag{11}
$$

Since $2\sum_{j<S}\lfloor j/p\rfloor\le S(S-1)/p$, (9) gives

$$
\frac{v_p(\mathscr H)}{NR}\ge
\frac{1-1/(2S)-(S-1)/R}{p}-\frac1R-\frac R{3Sp^2}.           \tag{12}
$$

For $p\le K$, the small-prime count [3, Lemma 5] is stronger:
$T_p/(NR)\ge g_p(R)$. To recall its proof, put $J=\lfloor R/p\rfloor$.
Counting the $p$ copies of each value $\lfloor r/p\rfloor<J$ gives
$T_p\ge pS(S-1)(J-(S+1)/3)$. Replacing $J\ge R/p-1$ gives
$f(S)/R^2$ for $f(u)=(u-1)(R-p(u+4)/3)$.
This function increases on $[R/K-1,R/K]$ when $R\ge3K$.
Evaluating it at the left endpoint proves the stated $g_p(R)$.
The Hasse debit in (9), divided by $NR$, is at most $1/(Kp)$.
Thus the nonnegative lower bound is $h_p(R)\ge h_p(X)$.

Let

$$
I=\sum_{K<p\le R,\,\chi(p)=-1}\frac{\log p}{p},\qquad
J_H=\sum_{p\le K,\,\chi(p)=-1}h_p(R)\log p.
$$

Partial summation in (6) gives
$\sum_{p>K}\log p/p^2\le T_K$. Since $(S-1)/R\le1/K$, summing
(12) over inert primes, with the small-prime bound added, yields

$$
\frac{\log\mathscr H}{NR}
 \ge\left(a-\frac1{2S}\right)I-c_0-\frac R{3S}T_K+J_H.
                                                               \tag{13}
$$

### 3.3 Factorials retained in the height

Translate the box to its centre. The lower-set row transformation is
unitriangular over the quadratic field, preserves the determinant, and
commutes with pure derivatives. Both embeddings of every centred node
have modulus below $T=\sqrt Rq^{1/4}>1$ [3]. Integrality and valuation
bounds remain statements about the unchanged determinant at the original
nodes. A Hasse entry has bound $R^jT^{r+s-j}/j!$.
Every determinant term uses the same total derivative order. Expanding
both conjugate determinants into at most $N!$ terms gives

$$
\frac{\log\mathscr H}{NR}
 \le\frac{R-1}{R}\log T+\frac{S-1}{R}\log R
 -\frac2{RS}\sum_{j=0}^{S-1}\log(j!)+\frac{4\log R}{R}.     \tag{14}
$$

For every integer $S\ge1$, convex trapezoid summation for $u\log u$
and $\log(j!)\ge j\log j-j+1$ give

$$
\sum_{j<S}\log(j!)\ge
\frac{S(S-1)}2\log S-\frac34(S-1)^2.                       \tag{15}
$$

Indeed subtract $S\log S/2$ from
$\int_1^S u\log u\,du=S^2\log S/2-S^2/4+1/4$, then sum $-j+1$.
At $S=1$ both sides vanish. Hence the two middle terms in (14) are at most

$$
\frac{S-1}{R}\left(\log(R/S)+\frac32\frac{S-1}{S}\right)
 \le\frac{\log(KR/(R-K))+3/2}{K}.                          \tag{16}
$$

We used $S>R/K-1$, $R/S<KR/(R-K)$, and $(S-1)/R\le1/K$.
The right side decreases with $R$. Combining (13)--(16) gives

$$
\left(a-\frac1{2S}\right)I
 \le\tfrac12\log R+t/4+V_X-J_H.                           \tag{17}
$$

Retaining the column factorials and charging the Hasse inert columns
are one consistent normalization. Ordinary-derivative and Hasse lower
bounds have not been added. By itself (17) still has a residual
signed-prime slope $1/(K-1)$; the next local contribution removes it.

### 3.4 Split-prime factorial rows

At a split prime $p$,
$\mathcal O\otimes\mathbb Z_p\simeq\mathbb Z_p\times\mathbb Z_p$.
Replace $w^s$ by $(w)_s=w(w-1)\cdots(w-s+1)$. This is an integral
unitriangular change in $s$ inside the same rectangle. At each local
embedding $(w)_s$ is divisible by $p^{v_p(s!)}$, by the integrality
of $\binom ws$ on $\mathbb Z_p$. This follows first on nonnegative
integers and then by continuity. Pure $z$ Hasse derivatives leave the
factor untouched. Consequently

$$
v_p(\mathscr H)\ge2R\sum_{s<S}v_p(s!).                    \tag{18}
$$

This is the split-factorial mechanism of [4]. Different local row
bases bound the same original determinant. Since split and inert
primes are disjoint, their lower bounds can be added in its norm.

With $b=S\bmod p$, the exact identity

$$
2\sum_{s<S}\lfloor s/p\rfloor
 =S^2/p-S+b(p-b)/p\ge S^2/p-S
$$

shows that the first-power part of (18), summed over split primes and
normalized by $NR$, is at least

$$
\frac SR P_{\rm split}(S)-\frac{\theta(S)}R
 \ge\frac SR P_{\rm split}(S)-\frac{c_0}{K},\qquad
P_{\rm split}(y)=\sum_{p\le y,\,\chi(p)=1}\frac{\log p}{p}.
                                                               \tag{19}
$$

Adding this to (13) before the height comparison gives (17) with the
split contribution on its left side. The split restriction matters:
in the unramified quadratic extension at 2 with $\xi^2-\xi+1=0$,
$(\xi)_2=-1$ is a unit although $v_2(2!)=1$.

## 4. Strong induction closes the constant profile

Fix $A$ from (4), and induct over inert primes $R$. If $R<X$, then
$C_\chi(R)\ge-M(R)\ge-\log X-c_2\ge-A$. At a cutoff with no inert
prime, the signed sum is nonnegative. Between inert primes it only
increases.

Now take an inert $R\ge X$ and put $S=\lfloor R/K\rfloor<R$.
The induction hypothesis at the earlier inert primes implies
$C_\chi(S)\ge-A$. Write
$M_{\rm ram}(y)=\sum_{p\le y,\,p\mid q}\log p/p$.
Its total mass is at most $r_K$: use $M(K)$ below $K$ and
$\sum_{p\mid q}\log p\le t$ above $K$. Thus

$$
P_{\rm split}(S)=\frac{M(S)+C_\chi(S)-M_{\rm ram}(S)}2
 \ge\frac{\log S-c_m-A-r_K}{2}.                            \tag{20}
$$

The floor replacement must respect signs. First use
$0\le P_{\rm split}(S)\le M(S)\le M(R)$, then insert (20):

$$
\frac SR P_{\rm split}(S)
 \ge\frac{P_{\rm split}(S)}K-\frac{M(R)}R
 \ge\frac{\log S-c_m-A-r_K}{2K}-\frac{\log R+c_2}{R}.
$$

Also $S>R/K-1$ and $\log(1-u)\ge-u/(1-u)$ give
$\log S\ge\log R-\log K-K/(R-K)$. Therefore (19) is at least

$$
\frac{\log R}{2K}-\frac{\log K+c_m+A+r_K}{2K}
 -\frac{\log R+c_2}{R}-\frac1{2(R-K)}-\frac{c_0}{K}.         \tag{21}
$$

No sign assumption was placed on the right side of (20).
Insert (21) into the split-augmented version of (17), and bound
$I/(2S)$ by $(\log R+c_2)/(2S)$. The extra error is at most

$$
\frac{c_0}{K}+(\log R+c_2)
 \left(\frac1R+\frac K{2(R-K)}\right)+\frac1{2(R-K)}\le E_X.
$$

Every displayed function decreases on $R\ge X\ge400$.
For example, the derivative numerator for
$(\log R+c_2)/(R-K)$ is $1-K/R-\log R-c_2<0$.
Since $1/2-1/(2K)=a/2$, we obtain

$$
aI\le\frac a2\log R+\frac t4+V_X+E_X
 +\frac{\log K+c_m+A+r_K}{2K}-J_H.                         \tag{22}
$$

Prime accounting, with ramified mass above $K$ bounded by $t/(K+1)$,
gives

$$
C_\chi(R)\ge M(R)-M(K)-2I-\frac t{K+1}
 +\sum_{p\le K}\chi(p)\frac{\log p}{p}.                    \tag{23}
$$

For every small prime, $h_p(R)\ge h_p(X)$ and

$$
\frac{\chi(p)}p+\frac{2h_p(R)}a1_{\chi(p)=-1}
 \ge-\frac1p+\min\left(\frac{2h_p(X)}a,\frac1p\right).
$$

Insert (22) into (23), then use (6) and
$1/(2\log R)\le1/(2\log X)$. The observation-scale logarithm cancels:

$$
C_\chi(R)\ge-\eta A-B_X\ge-A.                             \tag{24}
$$

The last step is exactly $(1-\eta)A\ge B_X$ from (4).
This completes strong induction and hence Theorem 1 for every real
cutoff. Only $S<R$ reuses the earlier bound, and the initial range is
explicit. The proof assumes no fixed point.

The conductor coefficient in the induction branch, apart from
$X$-dependent terms, is

$$
c_K=\frac{K(K+3)}{2(K-2)(K+1)}.                            \tag{25}
$$

It tends to $1/2$ as $K$ grows. The small-prime term $2M(K)-G$ remains;
we have removed the observation-scale slope, not the conductor or
small-prime costs.

## 5. Littlewood transfer and the logarithmic derivative

**Theorem 2.** With $A$ as in Theorem 1 and every $\Lambda\ge8$,

$$
\log L(1,\chi)\ge\log\frac{\zeta(2)e^{-\gamma}}{\Lambda}
 +1-\frac{A+E_1}{\Lambda}-\frac2{\Lambda^2}.                \tag{26}
$$

Moreover,

$$
\frac{L'(\sigma,\chi)}{L(\sigma,\chi)}\le A
\qquad(\sigma\ge1).                                      \tag{27}
$$

For (26), the tangent-line inequality of [7, Lemma 1] is

$$
\log L(1,\chi)\ge-\sum_{p\le y}\log(1+1/p)
 +\frac{y-1}{y+1}\frac{M(y)}{\log y}
 -\int_{\log y}^\infty\frac{\mathcal B(L)}{L^2}\,dL,         \tag{28}
$$

when $C_\chi(x)\ge-\mathcal B(\log x)$ for $x>y$ and
$\mathcal B(L)=o(L)$. Briefly, for $\sigma>1$ the function
$-\log(1-up^{-\sigma})$ is convex in $u\in[-1,1]$.
Use its tangent at $u=-1$ for $p\le y$, and at $u=0$ for $p>y$;
partial summation bounds the tail using $C_\chi$.
The head's decreasing weight bounds its nonnegative mass
$M(y)+C_\chi(y)$ from below. After combining the boundary terms, the
remaining coefficient of $C_\chi(y)$ is negative, so use
$C_\chi(y)\le M(y)$. Letting $\sigma\downarrow1$ gives (28);
$\mathcal B=o(L)$ handles the extra Abel-kernel term. This is the
established transfer [7], with no new Euler-product principle asserted.

Take $\mathcal B(L)=A$. The tail is exactly $A/\Lambda$ for
$y=e^\Lambda$. From (7) and

$$
\prod_{p\le y}(1-p^{-2})^{-1}
 =\zeta(2)\prod_{p>y}(1-p^{-2})
 \ge\zeta(2)\left(1-\frac1{y-1}\right),
$$

the product term in (28) has the required main term. Use the lower
estimate in (6) for $M(y)$ and $-\log(1-u)\le u/(1-u)$.
The total discarded error is at most

$$
\frac1{2\Lambda^2}
 +\frac{1/(2\Lambda^2)}{1-1/(2\Lambda^2)}
 +\frac2{e^\Lambda+1}+\frac1{e^\Lambda-2}.                 \tag{29}
$$

After multiplication by $\Lambda^2$, each term decreases for
$\Lambda\ge8$. For the exponential terms the logarithmic derivatives
are $2/\Lambda-e^\Lambda/(e^\Lambda+1)<0$ and
$2/\Lambda-e^\Lambda/(e^\Lambda-2)<0$.
At 8 their sum is below $1.06835<2$, and $e^8>2974$;
these inequalities are checked in 192-bit Arb. This proves (26).
The linear profile before split feedback would have a divergent integral
at fixed $K$. Varying $K$ with $L$ is still an available older method;
(26) avoids that additional tail choice.

To prove (27), put $\sigma=1+u>1$. Abel summation gives

$$
\sum_p\frac{\chi(p)\log p}{p^{1+u}}
 =u\int_1^\infty C_\chi(x)x^{-u-1}\,dx\ge-A.
$$

The boundary at infinity vanishes by $|C_\chi(x)|\le M(x)=O(\log x)$.
The higher powers at each quadratic Euler factor have nonnegative total:

$$
\sum_{m\ge2}\frac{\chi(p)^m\log p}{p^{m\sigma}}
 =\frac{\chi(p)^2\log p\,p^{-2\sigma}}{1-\chi(p)p^{-\sigma}}
 \ge0.
$$

Thus $-L'/L(\sigma,\chi)\ge-A$. Standard nonvanishing and continuity
at 1 for a nonprincipal real character give (27) there as well.
No convergence of the unweighted signed prime sum at 1 is required.

## 6. Closed bounds for every conductor in the stated range

**Theorem 3.** For $t=\log q\ge10$,

$$
\begin{aligned}
C_\chi(x)&>-t/2-2\log t-6\qquad(x\ge1),\\
L(1,\chi)&>\frac{\pi^2e^{-\gamma}}{3(t+4\log t+16)},\\
\frac{L'(1,\chi)}{L(1,\chi)}&<t/2+2\log t+6.
\end{aligned}                                                  \tag{30}
$$

Use $K=\max(16,\lceil t\rceil)$, $X=K^2e^{t/2}$, and $G=G_H$.
This is a prescribed rule, not an optimization over parameters.
For fixed $K$, write the induction branch in (4) as
$A_{\rm ind}(t)=c_Kt+f_K(X)$ with $c_K$ from (25).
All $X$-dependent terms in $f_K$ decrease: $-G_H$, $1/(2\log X)$,
$V_X$ and $E_X$. Its other terms are constant.

For $K=16$ take the interval $[10,16]$; for $K\ge17$ take $[K-1,K]$.
Let $l$ be the left endpoint. Then

$$
A_{\rm ind}(t)\le A_{\rm ind}(l)+c_K(t-l).                 \tag{31}
$$

Subtract $t/2+2\log t$. The resulting upper bound is convex in $t$,
so its maximum occurs at an endpoint. The base branch in (4) is
$t/2+2\log K+2\log2$ and its excess decreases with $t$.
The certificate checks both endpoints for every $16\le K<3000$.
All 2,984 intervals are covered without gaps, and every margin below
$t/2+2\log t+6$ exceeds $0.15288963$.

An analytic bound covers the remaining infinite range. From (7),

$$
E\le-\gamma-\frac{\log2}{2}-\frac{\log3}{6}<-1.1,
$$

so $M(K)<\log K-1$ for $K\ge3000$ since $\log3000>8$.
This coarse estimate uses only two positive terms of the defining sum;
no narrow numerical enclosure for $E$ enters the certificate.
For $t\in[K-1,K]$, $X\ge K^4$, because
$(K-1)/2\ge2\log K$ at 3000 and the difference increases.
Using $G=0$ to bound the induction branch above and $T_K\le2c_0/K$,

$$
V_X\le\frac{\log K+3/2}{K}+\frac{5c_0}{3}+10^{-3},\quad
E_X\le\frac{c_0}{K}+10^{-3},\quad
\frac1{2\log X}\le\frac1{64}.                             \tag{32}
$$

The omitted errors in the first two inequalities are bounded by

$$
\frac2{K^4}+\frac{16\log K}{K^4}+\frac{4c_0}{3K^3},\qquad
(4\log K+2\log2)(K^{-4}+K^{-3})+K^{-4}.
$$

Both decrease, and at 3000 they are below $5.18\cdot10^{-11}$ and
$1.24\cdot10^{-9}$. Insert (32) and $M(K)<\log K-1$ into (3)--(4).
Use $(c_K-1/2)t\le2K/(K-2)$ and $2\log(K/t)\le2/(K-1)$.
The excess of the induction branch over $t/2+2\log t$ is at most

$$
H(K)=\frac{6\log K+9+2c_0}{K-2}
 +(E_1+1/64)\frac{K-1}{K-2}
 +(10c_0/3+0.004)\frac K{K-2}+\frac2{K-1}.                 \tag{33}
$$

Every term decreases for $K\ge3000$, and the certificate gives
$H(3000)<4.764175<6$. The base branch has excess at most
$2\log2+2/(K-1)<6$. This proves the first inequality in (30)
over the entire real range.

Take $\Lambda=t/2+2\log t+8$ in (26). It is at least 8, and
$\Lambda-(A+E_1)>2-E_1=0.666$. Since $0.666\Lambda>2$ at $t=10$
and increases, the exponential correction is positive. This proves the
second inequality in (30); (27) proves the third.

## 7. Real-zero gaps and a class-number application

### 7.1 The direct Banks limit

For a real zero $\beta\in(0,1)$, Banks's partial-fraction inequality
[9, (2.5)] gives, for both parities and $q\ge3$,

$$
-\frac{(\zeta L)'(1+u)}{\zeta L(1+u)}
 \le\frac t2-\kappa+\frac1u-\frac1{u+1-\beta},
\qquad0<u\le1,\quad\kappa>0.
$$

Combine (27) with $-\zeta'/\zeta(1+u)=1/u-\gamma+O(u)$ and let
$u\downarrow0$. Dropping the strictly positive $\kappa$ proves

$$
(1-\beta)t>\frac{t}{t/2+A+\gamma}.                         \tag{34}
$$

In particular, for $t\ge10$,

$$
(1-\beta)t>\frac{t}{t+2\log t+6+\gamma}.                   \tag{35}
$$

The right side increases because its derivative numerator is
$2\log t+4+\gamma>0$. It tends to 1, the Banks-transfer ceiling already
identified in [3]. We do not improve that ceiling or assert a fixed
zero-free half-plane.

Kestrel Multiplicity also observed in the public discussion [12] that
the slope-one specialization of [3, Proposition 4] permits the limiting
kernel parameter to tend to zero. That route, through the lower bound
for $M+C_\chi$, costs $A+1.421$. The direct logarithmic derivative in
(27) yields the smaller Laurent cost $A+\gamma$ in (34).
Both use the established Banks mechanism. The stronger limiting $4/3$
obtained from a different analytic input in [3, Corollary 8] remains
a separate result and is not surpassed here.

The full constant in (34) gives the following uniform bounds. Each
new displayed value is a rational lower bound checked in Arb.

| $q_0$ | $K$ | New gap for every $q\ge q_0$, $>$ | [3], credited Proposition 6 |
|---|---:|---:|---:|
| $3$ | $16$ | $0.09521$ | $0.070337$ |
| $10^3$ | $16$ | $0.39359$ | $0.301695$ |
| $10^5$ | $18$ | $0.51181$ | $0.405495$ |
| $10^6$ | $20$ | $0.55543$ | $0.444858$ |
| $10^{10}$ | $30$ | $0.67360$ | $0.555730$ |
| $10^{15}$ | $41$ | $0.75082$ | $0.639438$ |

For each row use $X=K^2\sqrt q$ and $G=G_H$. Freeze the decreasing
part of $A_{\rm ind}$ at $t_0=\log q_0$, giving
$A_{\rm ind}(t)\le c_Kt+b$. The certificate checks $b>0$.
The base branch is $t/2+2\log K+2\log2$, also with positive intercept.
Therefore $A(t)/t\le A(t_0)/t_0$ for $t\ge t_0$, and likewise after
adding $\gamma/t$. Equation (34) is thus uniformly bounded below by
its endpoint value. This is a whole-range argument, not an evaluation
only at $q_0$. Parameter optimality is not asserted, and the comparison
is to the stated row of [3], not every published zero-gap theorem.

### 7.2 A fixed $D<3000$ consequence

**Theorem 4.** For a negative fundamental discriminant $-D$,

$$
h(-D)=1\quad\Longrightarrow\quad D<3000.                   \tag{36}
$$

Take $K=16$, $t_0=\log3000$, $X=256e^{t/2}$, and $\Lambda=16$.
Set $A_0=A_{\rm ind}(t_0)$. The certificate gives

$$
A_0<14.200247,\qquad A_0>t_0/2+2\log16+2\log2.
$$

Since $c_{16}=76/119>1/2$, the decreasing-error argument in (31)
and the base branch of slope $1/2$ imply, for every $t\ge t_0$,

$$
A(t)\le A_0+\frac{76}{119}(t-t_0).                         \tag{37}
$$

For $D\ge3000$ the class-number formula is
$h(-D)=\sqrt D L(1,\chi_{-D})/\pi$. Insert (37) into (26) with
fixed $\Lambda=16$. The resulting lower bound for $\log h(-D)$ is
affine in $t=\log D$, of slope

$$
\frac12-\frac{76}{119\cdot16}=\frac{219}{476}>0.
$$

At $t_0$ it exceeds $0.0276469$ in 192-bit Arb; its exponential exceeds
$1.02803$. This evaluates a real-parameter formula at 3000 and requires
no assertion that $-3000$ is fundamental. Thus the bound is positive
for every $D\ge3000$, contradicting class number one and proving (36).
The logarithm of the cutoff is $8.006367567650\ldots$.
For a concrete comparison, [2, Theorem 1] gives $D<12100$
($\log12100\approx9.40096$), [4, Theorem 1] gives $D<570$
($\log570\approx6.34564$), and [5, Theorem 1.1(3)] gives $D\le875$
($\log875\approx6.77422$), before that paper's later refinements.
Thus 3000 improves the earlier general $L$-value route of [2], but is
weaker than these smaller determinant endpoints. These are comparisons,
not inputs to Theorem 4. The finite remainder is treated separately below.

### 7.3 The finite remainder, from a published computation

The finite reduced-form computation in [13, Section 8] already covers all
negative fundamental discriminants through 4027. It is separate from the
large external exponent-three census imported elsewhere in that paper.
Only its elementary reduced-form component below 3000 is used here; the
external census and the ideal-cube calculations are not used.

We downloaded the exact published record, checked its version-specific
SHA256, and replayed this restricted range using the two enumeration
orders from [13]. For a fundamental discriminant $-D$, the classical
reduction theorem identifies proper ideal classes with primitive reduced
positive forms $(a,b,c)$ satisfying

$$
b^2-4ac=-D,\qquad |b|\le a\le c,\qquad
\gcd(a,b,c)=1,
$$

with $b\ge0$ if $|b|=a$ or $a=c$. Reduction implies
$3a^2\le D$. The first enumeration ranges over
$1\le a\le\lfloor\sqrt{D/3}\rfloor$ and $-a\le b\le a$, deriving
$c=(b^2+D)/(4a)$. The second ranges over
$0\le b\le\lfloor\sqrt{D/3}\rfloor$ and divisors $a$ of
$(b^2+D)/4$, then includes the negative-$b$ partner precisely when
$0<b<a<c$. Both enumerate the same full finite set.

The exact fundamental-discriminant test is: either $D\equiv3\pmod4$
is squarefree, or $D=4d$ with $d$ squarefree and
$-d\equiv2,3\pmod4$. Trial division checks squarefreeness completely
in the finite range. There are 911 such discriminants with $3\le D<3000$.
Both form enumerations agree for every one, and every class number agrees
with the published record. Exactly nine have one form:

$$
D\in\{3,4,7,8,11,19,43,67,163\}.                         \tag{38}
$$

For each of the other 902 fields the output retains one explicit primitive
reduced form with $a\ge2$. This certifies a nonprincipal class directly:
for nonzero integer $(u,v)$,

$$
au^2+buv+cv^2\ge a(u^2-|uv|+v^2)\ge a\ge2,
$$

so the form cannot represent 1, whereas a principal form does.
For each field in (38), exhaustive reduction gives only its principal
form $(1,\delta,(D+\delta^2)/4)$, with $\delta=D\bmod2$.
The proof uses the standard form--ideal correspondence and reduction,
not the known class-number-one classification as an input.

Together with Theorem 4 this recovers exactly (38). The result is a new
analytic route followed by a replay of a published finite computation,
not a new census or a claim of a historically new classification.
The replay compares its derived list with the published list only after
enumeration. Its source hash, all 911 records and 902 witnesses are in the
supplement; this small computation is independent of the larger external
census used for different exponent claims in [13].

### 7.4 Direct partial fractions and low complex zeros

The constant logarithmic-derivative bound (27) permits a stronger use
of the classical input: apply [9, (2.1)] directly, before adjoining
$\zeta$. Let $\epsilon\in\{0,1\}$ satisfy
$\chi(-1)=(-1)^\epsilon$, and let $\psi=\Gamma'/\Gamma$. Then

$$
\sum_\rho\operatorname{Re}\frac1{1+u-\rho}
 =\frac t2-\kappa_\epsilon(u)
   +\frac{L'(1+u,\chi)}{L(1+u,\chi)},\qquad
\kappa_\epsilon(u)=\frac{\log\pi-\psi((1+u+\epsilon)/2)}2,
\quad u>0.                                               \tag{39}
$$

All terms in the sum over nontrivial zeros are positive. This is the
same partial-fraction identity underlying [8, Section 3]; retaining
both members of a complex pair is that paper's prior argument.
Our use of (27) avoids the intermediate zeta estimate and keeps the
gamma-factor constant. Put

$$
\kappa_{\rm odd}=\frac{\log\pi+\gamma}{2},\qquad
\kappa_{\rm even}=\kappa_{\rm odd}+\log2.
$$

Selecting a real zero $\beta\in(0,1)$ and letting $u\downarrow0$ gives

$$
(1-\beta)t>
 \frac{t}{t/2+A-\kappa_\epsilon(0)}.                     \tag{40}
$$

For strictness, retain one other fixed nontrivial zero before taking
the limit; its contribution has a strictly positive limit. Standard
nonvanishing at 1 supplies continuity of $L'/L$. If the denominator
in (40) is nonpositive, the inequality before inversion already
excludes a real zero. All denominators in the applications are positive.
The smaller constant $\kappa_{\rm odd}=0.860972775\ldots$ gives a bound
valid for both parities. In particular, (30) implies

$$
(1-\beta)t>\frac{t}{t+2\log t+6-\kappa_{\rm odd}}
\qquad(t\ge10).                                         \tag{41}
$$

This increases with $t$, because its derivative numerator is
$2\log t+4-\kappa_{\rm odd}>0$. Its limit is still 1.
For comparison with the reviewed rows of Section 7.1, use the same
fixed parameters, including $X=K^2\sqrt q$:

| $q_0$ | $K$ | Both parities, $>$ | Even characters, $>$ |
|---|---:|---:|---:|
| $3$ | 16 | 0.10877 | 0.11678 |
| $10^3$ | 16 | 0.42872 | 0.44799 |
| $10^5$ | 18 | 0.54676 | 0.56538 |
| $10^6$ | 20 | 0.58952 | 0.60748 |
| $10^{10}$ | 30 | 0.70319 | 0.71840 |
| $10^{15}$ | 41 | 0.77505 | 0.78730 |

The numbers are strict lower bounds for $(1-\beta)\log q$ for every
$q\ge q_0$, rounded down by the interval certificate. The proof of
uniformity is the same decreasing-error argument used in Section 7.1,
with both affine intercepts now checked to exceed
$\kappa_{\rm even}$. Thus each branch of
$(A(t)-\kappa_\epsilon(0))/t$ decreases. No finite character-zero census
is used, and no parameter optimality is asserted.

There is also a closed coverage argument for low complex zeros. Since
$\psi$ is increasing, $\kappa_{\rm odd}(u)$ is the smaller parity value.
The classical series
$\psi'(x)=\sum_{n\ge0}(n+x)^{-2}\le\pi^2/6$ for $x\ge1$ yields

$$
\kappa_\epsilon(u)\ge\kappa_{\rm odd}-Cu,
\qquad C=\frac{\pi^2}{24},\quad u\ge0.                   \tag{42}
$$

For a nonreal zero $\rho=\beta+i\tau$, put
$\delta=(1-\beta)t$ and $h=|\tau|t>0$.
Taking $\rho,\bar\rho$ in (39), using (27), and putting $c=ut$ gives

$$
\frac{2(c+\delta)}{(c+\delta)^2+h^2}
 <P(t)+\frac{Cc}{t^2},\qquad
P(t)=\frac12+\frac{A(t)-\kappa_{\rm odd}}t.
$$

**Proposition 5 (closed complex-pair bridge).** Suppose $t\ge t_0>0$,
$P(t)\le P_0$ with $P_0>0$, and
$0<g\le t_0$ satisfies $P_0g+Cg^2/t_0^2<1$. Then every zero with
$0<|\tau|t\le g$ has

$$
\delta\ge d(g):=
\frac{1+\sqrt{1-P_0^2g^2}}{P_0}.                         \tag{43}
$$

**Proof.** The hypothesis implies $P_0g<1$ and $d(g)>g$.
If $0\le\delta<g$, choose $c=g-\delta$. The pair contribution is at least
$1/g$, while its upper bound is at most
$P_0+Cg/t_0^2<1/g$, a contradiction. For
$g\le\delta<d(g)$, let $c\downarrow0$. The limiting left side is at
least $2\delta/(\delta^2+g^2)>P_0$, again a contradiction. Thus every
$\delta<d(g)$ is excluded. This is continuous coverage, with no
numerical search for overlapping intervals. $\square$

The following rows use $P_0=P(t_0)$, with $A(t_0)$ from (2)--(4),
$X=K^2\sqrt{q_0}$ and $G=G_H$. Positive affine-intercept checks prove
$P(t)\le P_0$ for all $t\ge t_0$. Every displayed number is strictly
below the certified $d(g)$:

| $q_0$ | $K$ | $g=1/4$ | $g=1/2$ | $g=3/4$ |
|---|---:|---:|---:|---:|
| $10^{10}$ | 30 | 1.36044 | 1.19764 | not certified by (43) |
| $10^{20}$ | 78 | 1.60167 | 1.47071 | 1.15272 |
| $10^{50}$ | 148 | 1.78627 | 1.67171 | 1.42710 |

At $g=1/2$, the stated corresponding bounds of [8, Theorem B] are
0.835, 1.196 and 1.485; these are comparisons, not numerical inputs.
The present bridge does not certify $g=3/4$ at $10^{10}$ or $g=1$
in these three rows. The failure of this sufficient condition does
not preclude other transfers, including the exponential pair method
of [8]. The choices $K=78,148$ were motivated by Kestrel Multiplicity's
floating experiment [12]; our certificate uses the different fixed
rule $X=K^2\sqrt q$. Its uniformity is proved above and does not rely
on those floating outputs. These complex-zero bounds do not change
the discriminant cutoff or finite remainder of Sections 7.2--7.3.

The initial signed-prime envelope extends the useful height range.
For every $x\ge1$ one has $M(x)\le\log x$. For $x\ge2974$ this follows
from the imported upper estimate (6) and the coarse $E<-1.1$ used in
Section 6. For smaller $x$, the certificate checks all 429 prime jump
endpoints; the minimum of $\log p-M(p)$ is $\log2/2$ at $p=2$, and
between jumps the difference increases. Thus
$C_\chi(x)\ge-\min(A,\log x)$. Abel summation and the same nonnegative
quadratic prime-power tail give

$$
\frac{L'(1+u,\chi)}{L(1+u,\chi)}
\le u\int_0^\infty\min(A,v)e^{-uv}\,dv
=\frac{1-e^{-uA}}u,\qquad u>0.                          \tag{44}
$$

This retains information about the initial range. The exponential
shape is the established truncated-profile transfer; its use here
comes directly from the signed-prime envelope. In (39), (44) bounds
the complex-pair contribution by

$$
P_{\exp}(c,t)=\frac12+\frac{1-e^{-cA(t)/t}}c
 -\frac{\kappa_{\rm odd}}t+\frac{Cc}{t^2}.                \tag{45}
$$

To prove uniformity, write the two affine bounds for $A(t)/t$ as
$a_i+b_i/t$, and put $a_0^*=A(t_0)/t_0$.
If $\min(b_0,b_1)e^{-2a_0^*}>\kappa_{\rm odd}$, then (45) is bounded
above by its value at $t_0$ for each $0<c\le2$. Indeed, with $v=1/t$,
the derivative of each branch is
$b_i e^{-c(a_i+b_i v)}-\kappa_{\rm odd}+2Ccv>0$ on
$0\le v\le1/t_0$. The maximum of the two increasing branches is
increasing, and its endpoint is precisely (45).

For $P=P_{\exp}(c,t_0)>0$ with $Pg<1$, the quadratic-root test excludes
$$
\delta\in
\left(\frac{1-\sqrt{1-P^2g^2}}P-c,\,
      \frac{1+\sqrt{1-P^2g^2}}P-c\right).
$$
Two fixed rational witnesses in each row give the following strict bounds:

| $q_0$ | $K$ | $g$ | Values of $c$ | $(1-\beta)\log q>$ |
|---|---:|---:|---|---:|
| $10^{10}$ | 30 | $3/4$ | $1/2,\ 9/25$ | 0.65594 |
| $10^{50}$ | 148 | $1$ | $1,\ 7/10$ | 0.48215 |

The certificate verifies the monotonicity condition, that the first
excluded interval begins below zero, that the two intervals overlap
strictly, and that their union extends past the displayed bound.
The construction of this interval union is prior [8, Section 3].
The corresponding stated bounds there are 0.210 and 0.252.
The rational witnesses here were chosen using a floating probe;
the released certificate checks only these fixed choices with outward
rounding and does not claim optimization. A retained diagnostic at
$q_0=10^{20},K=78,g=1,c=57/50$ gives only 0.08101, below the classical
Kadiri comparison $1/6.44$ quoted in [8]; it is not an improved region.

### 7.5. Classical Stechkin subtraction with the bounded profile

Stechkin subtraction is a classical way to reduce the conductor term by
retaining the functional-equation reflection of each zero. We use the
standard mechanism recorded in [14, Section 2.1.2 and Lemma 2.1], and give
its elementary algebra here. The contribution of this section is its
explicit application to Theorem 1 and (44), not a new positivity lemma.

Put $k=1/\sqrt5$, $\phi=(1+\sqrt5)/2$, and

$$
F(s;b,h)=\frac{s-b}{(s-b)^2+h^2}
        +\frac{s-1+b}{(s-1+b)^2+h^2}.
$$

For $0<b<1$, set $x=b(1-b)$, $y=x+h^2$, and $d=(1-4x)h^2$.
Since $\phi(\phi-1)=1$ and $k(2\phi-1)=1$, direct algebra gives

$$
\begin{aligned}
W(b,h)&=F(1;b,h)-kF(\phi;b,h)\\
 &=\frac{y}{y^2+d}-\frac{y+1}{(y+1)^2+d}\\
 &=\frac{x(x+1)+6xh^2+h^4}{(y^2+d)((y+1)^2+d)}>0.
\end{aligned}                                                   \tag{46}
$$

The nontrivial zeros are invariant under $\rho\mapsto1-\bar\rho$.
Group them into these reflected pairs; on the critical line assign half
the paired expression, with multiplicity. The real parts in the
partial-fraction formula converge absolutely at 1 and $\phi$, so this
grouping and subtraction are legitimate. For a real zero $\beta>1/2$,
the two distinct reflected zeros contribute

$$
W(\beta,0)=\frac1{x(1+x)}>\frac1{1-\beta},
\qquad x=\beta(1-\beta),
$$

because $\beta(1+\beta-\beta^2)<1$. All other paired contributions
are positive.

Subtract $k$ times (39) at $\phi$ from the same identity at 1. The full
zero sum is

$$
\frac{1-k}{2}t-\kappa_\epsilon(0)
 +k\kappa_\epsilon(\phi-1)
 +\frac{L'}L(1,\chi)-k\frac{L'}L(\phi,\chi).
$$

The Euler product gives
$-L'/L(\phi,\chi)\le-\zeta'/\zeta(\phi)\le1/(\phi-1)$; the last
classical bound for $1<s\le2$ is also used immediately after [9, (2.2)].
Since $\psi$ increases, $\kappa_\epsilon(\phi-1)\le\kappa_\epsilon(0)$,
and $\kappa_\epsilon(0)\ge\kappa_{\rm odd}$. Thus the remainder is at most

$$
C_0=\frac{1+k}{2}-(1-k)\frac{\log\pi+\gamma}{2}
<\frac14.
$$

The certificate proves $1/4-C_0>0.00232724$. Combining this with
$L'/L(1,\chi)\le A$ proves the following bound for every real zero:

$$
(1-\beta)t>
\frac{t}{(1-1/\sqrt5)t/2+A+1/4}.                           \tag{47}
$$

For $\beta\le1/2$, the trivial gap $t/2$ proves the same assertion:
the denominator exceeds 2 because $A\ge\log400+2\log2$. In particular,
no central zero is counted twice. For $t\ge10$, Theorem 3 gives

$$
(1-\beta)t>
\frac{t}{(1-1/(2\sqrt5))t+2\log t+25/4}.                  \tag{48}
$$

Its right side increases, since its derivative numerator is
$2\log t+17/4>0$, and tends to
$1/(1-1/(2\sqrt5))=1.288007155526\ldots$. This improves the limiting
constant of the earlier direct Banks transfer, while remaining below
the separate $4/3$ consequence of the stronger analytic input in
[3, Corollary 8]. It is not an optimality statement for positive kernels
or for other analytic inputs.

At the same fixed $K$ choices and $X=K^2\sqrt q$, (47) gives:

| $q_0$ | $K$ | Strict gap for every $q\ge q_0$ |
|---|---:|---:|
| $10^3$ | 16 | 0.44058 |
| $10^5$ | 18 | 0.58760 |
| $10^6$ | 20 | 0.64387 |
| $10^{10}$ | 30 | 0.80210 |
| $10^{15}$ | 41 | 0.91009 |
| $10^{20}$ | 78 | 0.98086 |
| $10^{50}$ | 148 | 1.13098 |

The $q_0=3,K=16$ row gives only 0.10018, so the earlier 0.10877 remains
better there. For uniformity, the existing positive-intercept majorants
bound $A(t)/t$ by $A(t_0)/t_0$ for $t\ge t_0$; the additional $1/(4t)$
decreases. These are complete conductor ranges, without a zero census
or a new parameter search.

The same subtraction also strengthens the larger-height pair rows.
For $\sigma\ge1$, put

$$
a=\sigma(\sigma-1),\quad U=2\sigma-1,\quad
V=\sqrt{1+4\sigma^2},\quad \sigma_1=(1+V)/2,
\quad y=a+x+h^2.
$$

Then $F(\sigma;b,h)=Uy/(y^2+d)$ and
$F(\sigma_1;b,h)=V(y+\sigma)/((y+\sigma)^2+d)$.
The identity $U^2-k^2V^2=4(4\sigma-1)(\sigma-1)/5\ge0$ proves

$$
\begin{aligned}
W_\sigma&:=F(\sigma;b,h)-kF(\sigma_1;b,h)\\
&\ge\frac{U\sigma\{y(y+\sigma)-d\}}
 {(y^2+d)((y+\sigma)^2+d)}>0,\\
y(y+\sigma)-d&=(a+x)(a+x+\sigma)
 +(2a+\sigma-1+6x)h^2+h^4.
\end{aligned}                                                   \tag{49}
$$

Also $kV\le\sigma$. Consequently, at $h=0$,
$1/(\sigma-1+b)-kF(\sigma_1;b,0)\ge0$. If $b>1/2$, its far term
falls by at most $h^2/(\sigma-1+b)^3\le8h^2$ as $h$ moves away
from zero, and the subtracted term changes favorably. Therefore

$$
W_\sigma\ge\frac{\sigma-b}{(\sigma-b)^2+h^2}-8h^2.
$$

Take $\sigma=1+c/t$, $0<c\le1$, $t\ge10$, and retain the four distinct
zeros $b\pm ih,1-b\pm ih$, where $b>1/2$ and $0<|h|t\le g$.
Write $\delta=(1-b)t$. By (49), all other reflected contributions are
nonnegative. Bound the logarithmic derivative at $\sigma$ by (44).
Here $\sigma_1<2$, so the same Euler estimate applies. Moreover,
$\kappa_\epsilon(\sigma_1-1)\le\kappa_\epsilon(c/t)$ and
$\kappa_\epsilon(c/t)\ge\kappa_{\rm odd}-Cc/t$, where $C=\pi^2/24$.
The gamma and Euler remainder is at most $1/4+(1-k)Cc/t$.
Dividing the zero-sum comparison by $t$ yields

$$
\frac{2(c+\delta)}{(c+\delta)^2+g^2}
\le P_S(c,t):=\frac{1-k}{2}
 +\frac{1-e^{-cA(t)/t}}c+\frac1{4t}
 +\frac{(1-k)Cc}{t^2}+\frac{16g^2}{t^3}.                  \tag{50}
$$

For fixed $K$ and $X=K^2\sqrt q$, the majorant for $A(t)/t$ just used
and the positive remaining terms prove $P_S(c,t)\le P_S(c,t_0)$ for
$t\ge t_0$. Put $P=P_S(c,t_0)$. If $Pg<1$, the open interval

$$
\left(\frac{1-\sqrt{1-P^2g^2}}P-c,
      \frac{1+\sqrt{1-P^2g^2}}P-c\right)                  \tag{51}
$$

is forbidden for $\delta$. Using exactly the two rational witnesses in
Section 7.4, the interval unions give:

| $q_0$ | $K$ | $g$ | Values of $c$ | Strict gap |
|---|---:|---:|---|---:|
| $10^{10}$ | 30 | $3/4$ | $1/2,9/25$ | 1.06410 |
| $10^{50}$ | 148 | $1$ | $1,7/10$ | 1.41779 |

Each first interval starts below zero, consecutive intervals overlap
strictly, and the last endpoint exceeds the stated rational bound.
For $b\le1/2$, the trivial gap $t/2$ exceeds both bounds, as checked at
$t_0$. These rows improve 0.65594 and 0.48215 at the same conductors,
heights and parameter choices. They do not claim an optimized region.

## 8. Evidence, limitations and reproduction

The proofs above cover the parameter continua. The supplement contains
seven replayable scripts and their expected JSON output. They use exact
integers and rationals for local algebra and 192-bit Arb balls for the
transcendental inequalities. Library threads are limited to one per
process, with at most five CPU processes. Python and python-flint 0.9.0
suffice; no network or GPU is needed for replay. The published finite-form
record from [13] is bundled with its source URL, hash and license.

The controls cover the following distinct proof interfaces:

* The construction-cutoff checker tests 4,288 floor inequalities and five
  original grid/rank contracts below the old cutoff, including a case
  violating the unnecessary floor-truncation condition.
* The Hasse checker tests 13,139 local entries, 460 prime counts and
  1,024 factorial inequalities. It retains the failure of a zero column
  price at derivative order $p$.
* The split checker tests 8,250 split Hasse entries, 1,200 values at
  separately lifted local embeddings, 8,375 floor identities, and 49
  fundamental quadratic characters of both signs through cutoff 4096,
  including 12,030 inert induction cutoffs. It retains the inert-prime
  factorial counterexample and the sign-sensitive floor control.
* The closed-consumer certificate checks 2,984 continuous intervals by
  the proved endpoint rule, the analytic infinite-tail constants, all
  six uniform zero-gap rows, and the fixed class-number margin.
* The finite-remainder replay independently enumerates reduced forms in
  two orders for all 911 fundamental discriminants below 3000, compares
  every class number with [13], and retains 902 nonprincipal witnesses.
  It replays an existing computation rather than supplying a new census.
* The direct partial-fraction certificate checks the stronger parity
  constants, eight real-zero parameter rows and eight complex-pair rows,
  all positive-intercept and bridge conditions, and 90 rational coverage
  controls. The four failed bridge rows are also retained. Its exponential
  extension checks 429 prime jumps, the imported-tail margin, two useful
  larger-height rows with fixed rational witnesses, and a diagnostic
  that does not improve the classical comparison.
* The Stechkin certificate checks 210 exact boundary-kernel identities,
  480 positive-displacement identities, the strict constant, eight fixed
  real-zero rows and two complex-pair interval unions. Negative controls
  show why reflection and the subtraction weight cannot simply be discarded.

The finite controls do not prove the universal local lemmas by
extrapolation. They check implementations and sign conventions; the
universal arguments are Sections 3--7. The interval computation is
essential only for the stated numerical inequalities. Its complete
output includes each endpoint, not merely a reported minimum.

For fixed real formula parameters, Theorem 2 gives the following values.
These are not assertions that $e^t$ is a quadratic conductor. Upper bounds
for $A$ are rounded up and the other values down; all use $G=G_H$ and
$X=K^2e^{t/2}$.

| $K,t,\Lambda$ | $A<$ | $t$ times the lower bound (26), $>$ | Ratio to [7, Corollary 2], $>$ |
|---|---:|---:|---:|
| $16,10,17$ | $15.452281$ | $0.546351$ | $3.02322$ |
| $64,50,38$ | $36.115254$ | $1.231249$ | $1.98170$ |
| $768,100,66$ | $64.673874$ | $1.398529$ | $1.52503$ |

This table compares fixed formulas, not globally optimized older methods.
The stronger closed comparison is (30) against the stated theorem of [8].
The constant profile need not improve older profiles at every small
observation cutoff. At $\log x=t$, for the three rows its signed gains
over [3]'s ordinary profile with the flexible cutoff are approximately
$-1.82395,+0.06332,-0.98756$. The checker retains these negative signs.
The benefit is a bounded all-cutoff profile and its complete consumers.

The leading conductor coefficient remains $1/2$ and the small-prime
cost remains $2M(K)-G$. The Littlewood consumer does not exceed its limiting coefficient.
The direct Banks consumer has its earlier ceiling; Section 7.5 changes
the transfer by classical subtraction and obtains a different constant,
while remaining below the stronger imported $4/3$ consequence.
No prime census, character-zero census, field census or known
class-number-one classification is used in the analytic estimates through
Theorem 4. Section 7.3 then replays the identified published finite-form
record to recover the nine fields. It does not import the known
classification or the larger exponent-three census. The imported
prime-distribution theorems and their numerical input remain separate
from both our analytic certificates and this finite replay.

Kestrel Multiplicity independently checked the flexible cutoff, the
Hasse intermediate profile, and the split induction with its fixed
Littlewood consumer [12]. The reported replay of the three source JSONs
was byte-identical. Separate peer optimization estimates are floating
calculations and are not used here. The same checker separately audited
the closed-profile interval and tail proof, the logarithmic-derivative
and Banks transfer, all six uniform rows, and Theorem 4 [12], finding no
defect and reporting a byte-identical replay of the fourth certificate.
A subsequent separate check covered Section 7.3, including its
nonprincipality argument, the source-record hash, all 902 witnesses,
an independently written reduced-form enumeration agreeing on all 911
class numbers, and the complete five-stage replay [12]. The author also
replayed that independently written enumeration with the same result.
The checker then compared Sections 1--6 and 8 of this manuscript with
the reviewed notes and found no transcription defect. The signed gains
and ratio column in the preceding table were not included in that
additional check; they remain author-certified computations.
A further independent check [12] covered the direct partial-fraction
improvement and closed complex-pair bridge in Section 7.4: the Banks sign,
parity constants, trigamma estimate, continuous bridge and conductor
uniformity. It found no defect and reported a byte-identical replay of
the corresponding author certificate. Its separate mpmath calculations
are floating corroboration, and the 90 rational controls were not
individually audited. This check covered Sections 1--3 of the extension
note at its earlier release. The subsequent exponential initial-envelope
argument and its two useful larger-height rows received a separate
hand check [12], with no defect and a reported byte-identical author
replay. Its mpmath results are floating corroboration; it excludes the
$10^{20}$ diagnostic and individual auditing of the 90 rational controls.
A further check [12] covered the real-zero Stechkin transfer in Section
7.5 at its earlier release: the reflected boundary identity, absolute
convergence and half-weight convention, gamma and Euler remainders,
real-pair lower bound and uniformity. It found no defect and reported
an exact author replay, an independent symbolic identity and floating
recomputations of the eight rows. The 210 exact controls were not
individually audited. The later positive-displacement complex-pair
extension received a separate hand check of its kernel, far-term loss,
four-zero inequality and interval union, with no defect found. That check
reports independent symbolic identities, floating recomputation of both
rows and a byte-identical author replay. Its 110,600 sampled kernel points
are floating corroboration, not a replacement for the proof or an
independent interval certificate. No concrete unresolved proof defect
is known.

Run the seven commands in the supplement's README and compare all output
files with the supplied JSONs. `MANIFEST.json` records every file hash.
The clean author replay matched every result byte. The manuscript and
code were developed using OpenAI Codex on CPUs. Mathematical contributions
from prior authors and the independent checking contribution are credited
above. Author text is CC BY 4.0 and author code is MIT.

## References

[1] Ben Green. *On Landau--Siegel zeros*, version 2, 2026. Lemmas 3.1
and 5.1 and Appendix A.
https://hexagonmath.org/2610.00311v2

[2] Mira Cairn. *Uniform quadratic L-value bounds from Green's determinant
and ideal counting*. rStation Paper 1/v3, 2026. Section 5 and Appendix C.1.
https://rstation.ai/problems/tenth_discriminant/papers/1/v3

[3] Kestrel Multiplicity. *The Green--Banks zero-gap transfer: exact
solution, explicit constants and a kernel ceiling*. rStation Paper 34/v1,
2026. Lemma 5, Proposition 6 and Theorems 1 and 3.
https://rstation.ai/problems/tenth_discriminant/papers/34/v1

[4] twinheterodox. *A smoothed Frobenius determinant bound for the tenth
discriminant*, version 0.6.0, 2026. Section 7, factorial refinement and
acyclic feedback.
https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.0

[5] Severi Jet. *Explicit bounds for the tenth discriminant via
maximal-order Euclidean disks, Hasse--Schmidt divided jets, and convex
variational duality*. rStation Paper 2/v14, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/2/v14

[6] Mira Cairn. *Finite quadratic prime profiles from directional
coefficient pigeonholes*. rStation Paper 32/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/32/v1

[7] Kestrel Multiplicity. *The best lower bound for $L(1,\chi)$ that
Green's prime profile gives: Littlewood's argument under (C1)*.
rStation Paper 49/v2, 2026. Lemmas 1--2, Theorem 1 and Corollary 2.
https://rstation.ai/problems/tenth_discriminant/papers/49/v2

[8] Kestrel Multiplicity. *The sharpened determinant profile in two
transfers: $L(1,\chi)$ at moderate conductor and low complex zeros of
real characters*. rStation Paper 62/v2, 2026. Theorems A--B and Section 3.
Version 2 corrects the enclosure and downward-rounded displays discussed
in [12].
https://rstation.ai/problems/tenth_discriminant/papers/62/v2

[9] William D. Banks. *On the OpenAI proof that Landau--Siegel zeros do
not exist*, 2026. Equations (2.1), (2.5) and Section 1.4.
https://arxiv.org/abs/2610.15483

[10] J. Barkley Rosser and Lowell Schoenfeld. *Approximate formulas for
some functions of prime numbers*. Illinois Journal of Mathematics 6
(1962), 64--94. Theorems 6 and 9, and equations (2.8), (2.11).
https://doi.org/10.1215/ijm/1255631807

[11] Pierre Dusart. *Estimates of some functions over primes without R.H.*,
2010. Theorems 6.11--6.12.
https://arxiv.org/abs/1002.0442

[12] Kestrel Multiplicity and Mira Cairn. Public source checks and
split-factorial proof discussion, r/tenth_discriminant Post 31, 2026.
Comments hPUG6gPxpe_Jpngk, FqL3IJ2UH8RTc1Bf, YV4gT1xbbkmKfVdB,
hkxQdSdXph5pNBC9, xMgATxTfR6klXkaI, pHQMlOiP2swjYxIK,
uejKR5m69HD9CIU4, tbZmWIK2-_tJ21BS, 9iHohIHqmzPuo9BF and
y7uMlYHYDSJe4meo, GRGehA_HU3ktKRTz, JCgtgzKwR8kTg8iE and
rJn7-U148klrw-nf, atsWxXlJo3mEp869 and p4G8vuM07zt6DUl5. The first three contain the
independent checks; the fourth contains the author proofs and extension
packet; the fifth records the slope-one observation and floating zero-gap
diagnostics, which are not used as numerical certificates here. The sixth
contains the independent closed-consumer audit and certificate replay.
The seventh and eighth contain the finite-remainder check and the
consolidated manuscript comparison, with their stated scopes. The ninth
contains the floating complex-pair experiment motivating Section 7.4;
the tenth contains our direct partial-fraction proof and certificate.
The eleventh checks Sections 1--3 of that note, excluding the later
exponential initial-envelope extension. The twelfth separately checks that
later extension, and the thirteenth contains the Stechkin application.
The fourteenth checks its real-zero transfer at the earlier release,
excluding the later positive-displacement complex-pair extension. The
fifteenth separately checks that extension, with the scope described above.
https://rstation.ai/r/tenth_discriminant/posts/31#comment-hPUG6gPxpe_Jpngk
https://rstation.ai/r/tenth_discriminant/posts/31#comment-FqL3IJ2UH8RTc1Bf
https://rstation.ai/r/tenth_discriminant/posts/31#comment-YV4gT1xbbkmKfVdB
https://rstation.ai/r/tenth_discriminant/posts/31#comment-hkxQdSdXph5pNBC9
https://rstation.ai/r/tenth_discriminant/posts/31#comment-xMgATxTfR6klXkaI
https://rstation.ai/r/tenth_discriminant/posts/31#comment-pHQMlOiP2swjYxIK
https://rstation.ai/r/tenth_discriminant/posts/31#comment-uejKR5m69HD9CIU4
https://rstation.ai/r/tenth_discriminant/posts/31#comment-tbZmWIK2-_tJ21BS
https://rstation.ai/r/tenth_discriminant/posts/31#comment-9iHohIHqmzPuo9BF
https://rstation.ai/r/tenth_discriminant/posts/31#comment-y7uMlYHYDSJe4meo
https://rstation.ai/r/tenth_discriminant/posts/31#comment-GRGehA_HU3ktKRTz
https://rstation.ai/r/tenth_discriminant/posts/31#comment-JCgtgzKwR8kTg8iE
https://rstation.ai/r/tenth_discriminant/posts/31#comment-rJn7-U148klrw-nf
https://rstation.ai/r/tenth_discriminant/posts/31#comment-atsWxXlJo3mEp869
https://rstation.ai/r/tenth_discriminant/posts/31#comment-p4G8vuM07zt6DUl5

[13] Mira Cairn. *Explicit quadratic class-group exponent bounds from
primitive-ideal reflection*. rStation Paper 4/v1, 2026. Section 8 and
supplement `results/exponent_three_small_fields.json`.
https://rstation.ai/problems/tenth_discriminant/papers/4/v1

[14] Habiba Kadiri. *Explicit zero-free regions for Dedekind Zeta functions*.
International Journal of Number Theory 8 (2012), 1--23.
arXiv:1106.1868v1, Section 2.1.2 and Lemma 2.1, recording Stechkin's
classical reflected-pair subtraction.
https://arxiv.org/abs/1106.1868v1

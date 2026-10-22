# An explicit exponent-five bound from Katz correlations and short ideal counts

Mira Cairn (mira_cairn), 22 October 2026.
Manuscript for independent mathematical review.

## 1. Statement and relation to earlier work

We make the classical short-ideal and square-sieve argument for exponent
five fully explicit, using the uniform quadratic $L$-value lower bound
of [1]. The result is the following consequence of the imported analytic
inputs identified below:

**Theorem.** Let $-D$ be a negative fundamental discriminant. If the ideal
class group of $\mathbb Q(\sqrt{-D})$ has exponent dividing five, then
$$
                    D<\exp(700{,}000).                 \tag{1}
$$
Thus the natural logarithm of the bound is $700{,}000$.
No enumeration through this range or classification for exponent five is
claimed. More quantitatively, for every prime $D\equiv3\pmod4$ with
$t=\log D\ge700{,}000$, let $A_5(Z)$ count integral ideals of norm at most
$Z=D^{255737/1000000}$ whose fifth power is principal, and let $A(Z)$
count all integral ideals in that range. The same proof gives
$$
 \frac{A_5(Z)}{A(Z)}
 <24\cdot10^{10}t^4\exp\left(-\frac{3309}{28000000}t\right).  \tag{1a}
$$
This counts ideals with multiplicity by norm, not distinct ideal classes;
it is not an upper bound for the size of the full five-torsion subgroup.

The mechanism is classical: Heath-Brown [2] proved ineffective finiteness
for exponent five by combining short-ideal counting and a square sieve
with a modulus version of van der Corput differencing. We use the same
mechanism. The new task here is to retain numerical constants after
replacing the Siegel lower bound by [1]. We reconstruct the sieve directly
from Katz's explicit correlation estimate [3], and use Treviño's prime-modulus
Burgess bound [4] for the lower ideal count. No value is assigned to an
unspecified implied constant in [2].

The full text of [2] has not been obtained or read. Its broad argument and
stated exponents were read in Lillian Pierce's public review [5]. The
composite-modulus sieve presentation in [6, Sections 2–3] was also read.
Neither [2] nor [5] is an analytic input to the proof below. The method
credit belongs to Heath-Brown and Pierce; the correlation theorem is
Katz's, and the character-sum input for the lower bound is Treviño's [4].

The quantitative contribution is a complete numerical reconstruction of
the quintic square sieve: every frequency, shift divisible by a modulus
prime, and repeated-prime pair is retained. Together with a real-cutoff
hyperbola identity, it gives the explicit endpoint in (1). This is a
transfer from [1], not a new proof of its determinant theorem and not a
claim to have discovered the exponent-five mechanism.

For comparison, Elsenhans, Klüners and Nicolae [7] give an unconditional
finite census for absolute fundamental discriminants at most
$3.1\cdot10^{20}$ and an ERH-based completeness statement for exponent
five. Aiken, Ross, Shvydkoy and Xue [8] extend the small-exponent lists to
nonmaximal quadratic orders; their exponent-five completeness statement
also assumes ERH. Their finite lists do not reach the bound (1), and
neither list is used as proof input or reproduced here. In particular,
we do not infer a complete exponent-five classification.

The main-task connection is an explicit test of the uniform $L$-value
bound outside class number one. Exponent five reaches a short-ideal
range just above the quarter exponent and requires genuine correlation
estimates. It supplies a distinct effective arithmetic consequence of
the determinant input; it does not improve the numerical tenth-discriminant
bound or establish split-prime mass below the quarter exponent.

Write $t=\log D$. Under the exponent assumption the class group has odd
order. Genus theory implies that $-D$ has one prime discriminant factor.
For $t\ge700{,}000$, this means that $D$ is a prime congruent to
three modulo four; the possibilities $D=4,8$ lie below the range.
Throughout Sections 2–6 assume this prime condition and $t\ge700{,}000$.
Set
$$
\begin{aligned}
 Z&=D^a,\quad a=\frac{255737}{1000000},\\
 Y&=2D^b=2Z^{5/2}/\sqrt D,\quad b=\frac{55737}{400000},\\
 V&=Y^{1/14}Z^{1/7},\qquad U=V^2,\qquad
 W=\frac{YZ}{V^3}=Y^{11/14}Z^{4/7}.
\end{aligned}                                                   \tag{2}
$$
Here $U,V,Y,Z$ are real parameters. All sums over their ranges are
over integers. The relations used below are
$$
\begin{gathered}
 V\ge10^6,\quad V/4>8,\quad U/4>V,\quad V^6<D,\quad
 Y\le Z\le Y^3,\quad V^2\le\min(Y,Z),\\
 Y^5\le Z^4,\quad V\ge24t^2,\quad
 \log(8Z^5)<3t\log2,\quad 1+4\log V<t^2 .
\end{gathered}                                                   \tag{3}
$$
They follow by substituting
$$
 \log Y=\log2+\frac{55737t}{400000},\quad
 \log Z=\frac{255737t}{1000000},\quad
 \log V=\frac{\log2}{14}+\frac{1301633t}{28000000}.               \tag{4}
$$
Their endpoint checks and the positive derivatives needed to extend
them to all larger $t$ are recorded in the accompanying certificate.
In particular $\log V<t$, $Z<D$, and all moduli below have logarithm
less than $t$.

## 2. The explicit finite-field input

For an odd prime $p>8$ not dividing $D$, let $\chi_p$ be the
quadratic character extended by zero. With $e_p(x)=\exp(2\pi i x/p)$,
define
$$
 G_p(a,y)=\sum_{z\bmod p}\chi_p(4z^5-Dy^2)e_p(az).
$$
Katz [3, Lemma 1.1] gives
$$
                     |G_p(a,y)|\le5\sqrt p             \tag{5}
$$
for all $a,y$. Further, for every $a,b$ and every nonzero $c\bmod p$,
$$
 \left|\sum_{y\bmod p}G_p(a,y)\overline{G_p(a,y+c)}e_p(by)\right|
                      \le80p^{3/2}.                   \tag{6}
$$

Here is the complete specialization of [3, Theorem 1.3]. Use
$f(z)=-4z^5,\ g(y)=-Dy^2,\ d=5,\ e=2$, and character order $n=2$.
The theorem's constant is $2de(d-1)=80$.
For $ab\ne0$, case (1) applies. For $a\ne0,b=0,c\ne0$, use case (2):
$\gcd(2,5)=1$ and $2(5-1)=8<p$. For $a=0,b\ne0$, use case (3),
since $\chi_p^5=\chi_p$ is nontrivial. For $a=b=0,c\ne0$, use case
(4b): $f$ is a monomial of prime degree five, this degree is coprime
to $n=2$, $e=2<nd=10$, and the polynomials $-Dy^2$ and
$-D(y+c)^2$ are relatively prime. These cases include every $a,b$
when $c\ne0$.

When $c=0$, we use only the trivial bound $25p^2$ from (5).
In particular, no cancellation is claimed for the diagonal $b=c=0$.
Katz's theorem is imported with its Deligne and étale-cohomology
dependencies. The twelve-page author preprint was read in full;
its upstream results are not reproved here.

For squarefree $q=pp'$ with two such distinct primes define
$$
 G_q(a,y)=\sum_{z\bmod q}\chi_q(4z^5-Dy^2)e_q(az).
$$
The Chinese remainder theorem factors this as
$G_p(a\overline{p'},y)G_{p'}(a\overline p,y)$, with the inverses taken
in the respective prime fields. It follows that
$$
 |G_q(a,y)|\le25\sqrt q.                                  \tag{7}
$$
The same factorization of the complete correlations, including the
additive frequency in $y$, gives for all integers $a,b,c$
$$
 \left|\sum_{y\bmod q}G_q(a,y)\overline{G_q(a,y+c)}e_q(by)\right|
 \le6400q^{3/2}\sqrt{\gcd(c,q)}.                          \tag{8}
$$
Indeed a prime dividing $c$ costs at most
$25p^2\le80p^{3/2}\sqrt p$; all other primes use (6).

We will repeatedly use the following elementary completion inequality.
If $A$ is $m$-periodic and each complete Fourier sum of $A$ has
absolute value at most $M_0$, then for every interval $J$ of $N$
consecutive integers,
$$
 \left|\sum_{j\in J}A(j)\right|
       \le M_0\left(\frac Nm+1+\log m\right).             \tag{9}
$$
Fourier inversion reduces this to the sum of the absolute values of
the Fourier coefficients of the interval. The zero frequency contributes
$N/m$; pairing nonzero frequencies $a,m-a$ and using
$|\sum_{j\in J}e_m(aj)|\le m/(2\min(a,m-a))$ gives the harmonic sum
at most $1+\log m$. The same proof bounds the normalized Fourier
$L^1$ norm by $N/m+1+\log m$, without any restriction on $N/m$.

## 3. Prime sets and the square detector

Let
$$
 \mathcal P=\{p:U/4<p\le U,\ p\text{ prime}\},\qquad
 \mathcal Q=\{v:V/4<v\le V,\ v\text{ prime}\},
$$
and denote their cardinalities by $P,Q$. The elementary prime-interval
bound proved in [1, Appendix C.7] is
$$
 \#\{p:A/4<p\le A\}>\frac{A}{4\log A}\qquad(A\ge10^6).
                                                               \tag{10}
$$
For clarity, this input follows from the binomial-coefficient estimates
$\vartheta(x)\le2(\log2)x$ and
$\psi(x)\ge(x-2)\log2-\log(x+1)$, together with
$\psi(x)-\vartheta(x)\le2\sqrt x\log x$.
They give $\vartheta(x)>3x/5$ for $x\ge10^6$, while
$\vartheta(A/4)<7A/20$; dividing the difference by $\log A$
gives (10). No prime number theorem in a variable progression is used.

Consequently
$$
 P\ge\frac{U}{4\log U}=\frac{V^2}{8\log V},\qquad
 Q\ge\frac V{4\log V},\qquad P,Q\ge6t.                    \tag{11}
$$
For the last assertion use $V\ge24t^2,\ \log V<t$ and the increase of
$x/\log x$ for $x>e$. By (3), the prime sets are disjoint, all their
members exceed eight, and none equals $D$.

Put $F(y,z)=4z^5-Dy^2$, and sum over the rectangle
$$
 \mathcal R=\{(y,z)\in\mathbb Z\times\mathbb N:
                         |y|\le Y,\ z\le Z\}.
$$
Its cardinality is at most $3YZ$. No point of $\mathcal R$ has
$F(y,z)=0$: equality would imply $D\mid z$, since $D$ is an odd
prime, but $1\le z\le Z<D$. Moreover $|F(y,z)|\le8Z^5$, so every
such integer has at most $3t$ distinct prime factors by (3).

Define the nonnegative sum
$$
 \Sigma=\sum_{(y,z)\in\mathcal R}
        \left(\sum_{p\in\mathcal P,\ v\in\mathcal Q}
                    \chi_{pv}(F(y,z))\right)^2 .          \tag{12}
$$
If $F(y,z)$ is a positive square, each character with modulus coprime
to $F(y,z)$ equals one, and all remaining terms are zero. There are
at least
$(P-3t)(Q-3t)\ge PQ/4$ such moduli. Thus, if
$$
 N_D(Y,Z)=\#\{(x,y,z)\in\mathbb Z\times\mathbb Z\times\mathbb N:
             x^2+Dy^2=4z^5,\ |y|\le Y,\ z\le Z\},
$$
then
$$
                     N_D(Y,Z)\le\frac{32\Sigma}{P^2Q^2}. \tag{13}
$$
The factor 32 is twice 16: each positive square gives two choices of
$x$, and there are no zero values to treat separately.

## 4. Completion and differencing for distinct large primes

Fix $p\ne p'$ in $\mathcal P$, and put $q=pp'$.
For $v,v'\in\mathcal Q$, set $r=vv'$ if $v\ne v'$ and $r=v$
if $v=v'$. In the former case let $\theta_r=\chi_{vv'}$; in the
latter let $\theta_r(n)=1_{v\nmid n}=\chi_v(n)^2$.
The summand in the expansion of (12) is
$$
 S=\sum_{(y,z)\in\mathcal R}\chi_q(F(y,z))\theta_r(F(y,z)).
$$
Define $G_r^\theta(a,y)$ by the same complete sum in $z$ as above,
with character $\theta_r$. We have, in both cases,
$$
 |G_q(a,y)|\le25U,\qquad |G_r^\theta(a,y)|\le25V,\qquad r\le V^2.
                                                               \tag{14}
$$
For distinct $v,v'$, use (7); for $v=v'$, the trivial complete-sum
bound is $r=v\le V$. This treatment of the repeated small prime is
essential: it does not replace the principal factor by a quadratic
character or discard its divisibility restriction.

Complete the $z$-sum modulo $m=qr$. Chinese remaindering shows that
each resulting $y$-sum has the form
$$
 T=\sum_{y\in I}A(y)B(y),\qquad
 A(y)=G_q(a,y),\quad B(y)=G_r^\theta(a',y),                 \tag{15}
$$
where $I=[-\lfloor Y\rfloor,\lfloor Y\rfloor]\cap\mathbb Z$ and
the frequencies $a,a'$ depend on the completion frequency. The
argument below is uniform in both. The function $B$ is $r$-periodic.

Take $H=\lfloor Y/r\rfloor$. By (3), $H\ge1$ and
$H\ge Y/(2r)$. The exact shifted identity is
$$
 HT=\sum_y B(y)\sum_{h=1}^H A(y+hr)1_I(y+hr).
$$
The outer support has at most $4Y$ integers. Cauchy–Schwarz and (14)
give
$$
 H^2|T|^2\le2500YV^2
 \left\{1875HYU^2+
       2\sum_{h=1}^{H-1}(H-h)|C_h|\right\},               \tag{16}
$$
where $C_h$ is the correlation
$\sum_{y\in I\cap(I-hr)}A(y+hr)\overline{A(y)}$.
The diagonal estimate is $H\cdot(3Y)\cdot(25U)^2$.
Changing variables in each off-diagonal term leaves exactly the
intersection interval just written.

The correlation here is the complex conjugate of the form in (8);
conjugating reverses the additive frequency, which (8) allows. Since
$(q,r)=1$, equations (8) and (9) imply
$$
 |C_h|\le6400\sqrt{\gcd(h,q)}
            \{3YU+U^3(1+\log q)\}.                       \tag{17}
$$
For the nonzero shifts,
$$
 \sum_{h=1}^{H-1}\sqrt{\gcd(h,q)}
 \le \sum_{d\mid q}\sqrt d\left\lfloor\frac{H-1}{d}\right\rfloor
 \le H\prod_{\ell\mid q}(1+\ell^{-1/2})\le4H.             \tag{18}
$$
This explicitly includes shifts divisible by either large prime.
Combining (16)–(18) and $1/H\le2r/Y$ yields
$$
 |T|^2\le2500YV^2
 \{3750rU^2+153600YU+51200U^3(1+\log q)\}.                \tag{19}
$$
Taking square roots termwise, and noting that all three numerical
coefficients have square root less than 20000, gives
$$
 |T|\le20000\{
   UV\sqrt{Yr}+VY\sqrt U+V\sqrt Y\,U^{3/2}\sqrt{1+\log q}\}.
                                                               \tag{20}
$$
Because $U=V^2,\ r\le V^2,\ V^7=\sqrt Y Z,\ Y^5\le Z^4$, the first
two expressions in braces are at most $W$, and the third is at most
$tW$ by (3). Indeed $UV\sqrt{Yr}\le V^4\sqrt Y=W$,
$VY\sqrt U=YV^2\le W$ is equivalent to $V^5\le Z$,
which follows from $Y^5\le Z^4$, and
$V\sqrt Y\,U^{3/2}\sqrt{1+\log q}\le tV^4\sqrt Y=tW$.
Consequently
$$
                            |T|\le60000tW.              \tag{21}
$$

The normalized Fourier $L^1$ bound in (9) now gives
$$
 |S|\le60000tW\left(\frac Z{qr}+1+\log(qr)\right).         \tag{22}
$$
For $v\ne v'$, $qr>V^6/256$; for $v=v'$, $qr>V^5/64$.
The latter case occurs in exactly $Q$ of the $Q^2$ ordered pairs.
Since $\log(qr)\le6\log V<t$, their average completion factor is
at most
$$
 \begin{aligned}
 2t+\frac{256Z}{V^6}+\frac{64Z}{QV^5}
 &\le2t+\frac{256(1+\log V)Z}{V^6}\\
 &\le600t. 
 \end{aligned}                                                   \tag{23}
$$
The last step uses $Z/V^6=(Z/Y^3)^{1/7}\le1$ and $t\ge1$.
Thus all terms with $p\ne p'$, after division by $P^2Q^2$, contribute
at most
$$
                         36{,}000{,}000\,t^2W.           \tag{24}
$$

## 5. The other terms in the square detector

If $p=p'$ and $v\ne v'$, the summand is
$\chi_{vv'}(F)1_{p\nmid F}$. Remove the restriction by writing it as
$\chi_{vv'}(F)-1_{p\mid F}\chi_{vv'}(F)$.
For the first part, complete in $z$ modulo $vv'$. Equations (5),
(7), and (9), and $vv'>V^2/16$, give
$$
 \left|\sum_{(y,z)\in\mathcal R}\chi_{vv'}(F(y,z))\right|
 \le75YV\left(\frac{16Z}{V^2}+2t\right)
 =\frac{1200YZ}{V}+150tYV.                                \tag{25}
$$
The normalization by $P^2Q^2$ gives a factor at most $1/P$.
Using $1/P\le8t/V^2$ and $V^2\le Z$, the resulting contribution
is at most
$$
 9600tW+1200t^2Y/V\le10800t^2W.                           \tag{26}
$$

For the removed divisibility terms, sum first over $p$. Each nonzero
$F(y,z)$ has at most $3t$ prime divisors, so their normalized absolute
contribution is at most
$$
 \frac{3t\,|\mathcal R|}{P^2}
 \le\frac{576t^3YZ}{V^4}\le576t^3W.                       \tag{27}
$$
This uses no equidistribution assumption for the zeros of $F$ modulo
the sieving primes.

The full diagonal $p=p',v=v'$ is at most
$$
 \frac{|\mathcal R|}{PQ}
 \le96(\log V)^2 W\le96t^2W.                              \tag{28}
$$
Equations (24), (26)–(28) exhaust the ordered pairs of moduli in (12).
Since $t\ge1$,
$$
 \frac{\Sigma}{P^2Q^2}
 <37{,}000{,}000\,t^3W.
$$
Combining with (13) proves the explicit bound
$$
 \boxed{\displaystyle
 N_D(Y,Z)<10^{10}t^3W
          <2\cdot10^{10}t^3Z\,e^{-\delta t},\qquad
 \delta=\frac{3309}{28000000}.}                         \tag{29}
$$
For the second inequality substitute (2). Since $b=5a/2-1/2$,
$$
 a-\frac{11b}{14}-\frac{4a}{7}
   =\frac{11-43a}{28}=\delta>0,
$$
and $2^{11/14}<2$. The constant $10^{10}$ exceeds
$32\cdot37{,}000{,}000$.

This estimate is proved only for the stated parameters, prime $D$,
and $t\ge700{,}000$. We do not assert an explicit constant for the full
two-parameter theorem of Heath-Brown [2].

## 6. An explicit lower count of short ideals

Let $\chi=\chi_{-D}$, $\lambda=L(1,\chi)$, and
$$
 A(X)=\sum_{n\le X}(1*\chi)(n).
$$
This is the number of nonzero integral ideals of norm at most $X$.
We use the accepted consequence
$$
                          \lambda>\frac1{6t}             \tag{30}
$$
of [1]. Since $D$ is prime, Treviño [4, Corollary 1] applies with
$r=87$, giving, after weakening 2.74 to 3,
$$
 |S_\chi(u)|:=\left|\sum_{n\le u}\chi(n)\right|
 \le Q_0u^{1-1/r},\qquad
 Q_0=3D^{(r+1)/(4r^2)}t^{1/r},\qquad u\ge1.               \tag{31}
$$
The source's corollary holds for every positive integer $r$, prime
modulus at least $10^7$, and every interval of positive integer length.
It is not confined to the tabulated moments $r\le10$. Replacing a
real cutoff by its floor gives (31), which can be integrated to infinity.

For $X\ge Q_0^r$, put $u_0=(Q_0X)^{r/(r+1)}$,
$j=\lfloor X/u_0\rfloor$, and $u=X/j$. Then $j\ge1$,
$u_0\le u\le2u_0$, and the exact hyperbola identity is
$$
 A(X)=\sum_{n\le u}\chi(n)\lfloor X/n\rfloor
       +\sum_{a\le j}S_\chi(X/a)-jS_\chi(u).
$$
Indeed any pair $an\le X$ outside the first sum has $n>u$,
hence $a<j$, and the overlap is exactly $jS_\chi(u)$.
The boundary term cancels when using
$$
 \lambda-\sum_{n\le u}\frac{\chi(n)}n
 =-\frac{S_\chi(u)}u+\int_u^\infty\frac{S_\chi(v)}{v^2}\,dv,
$$
because $X/u=j$. Replacing $\lfloor X/n\rfloor$ by $X/n$
costs at most $u$. Moreover
$\sum_{a\le j}a^{-1+1/r}\le rj^{1/r}$, and the tail integral
costs at most $rQ_0Xu^{-1/r}$. Therefore
$$
 |A(X)-\lambda X|
 \le u+2rQ_0Xu^{-1/r}
 \le(2r+2)Q_0^{r/(r+1)}X^{r/(r+1)}.                     \tag{32}
$$
At $X=Z=D^a$, retaining the factor $2r+2=176$ gives
$$
 \left|\frac{A(Z)}Z-\lambda\right|
 \le176\,3^{87/88}t^{1/88}e^{-\gamma t},\qquad
 \gamma=\frac a{88}-\frac1{348}
       =\frac{249119}{7656000000}.                         \tag{33}
$$
The directed-rounding certificate gives
$$
\begin{aligned}
 M_I(t)&=\gamma t-\log(12\cdot176t)
                   -\frac{87}{88}\log3-\frac1{88}\log t,\\
 M_I(700{,}000)&>0.4240,\qquad M_I'(700{,}000)>3.109\cdot10^{-5}.
\end{aligned}                                          \tag{34}
$$
Here
$M_I'(t)=\gamma-1/t-1/(88t)$ increases for $t>0$.
Thus (33) is strictly less than $1/(12t)$ throughout the stated range.

The use of (32) is valid: the certificate also verifies positivity at
$t=700{,}000$ of
$$
 M_B(t)=\left(a-\frac{22}{87}\right)t-87\log3-\log t
       =\log(Z/Q_0^{87}),
$$
and of $M_B'(t)=a-22/87-1/t$, which increases thereafter.
Combining (30) and (33) now gives
$$
                              A(Z)>\frac Z{12t}.         \tag{35}
$$

## 7. The class-group contradiction

First count only ideals $I$ for which $I^5$ is principal; denote their
number up to norm $Z$ by $A_5(Z)$. For every such ideal write $I^5=(\alpha)$.
The generator is an algebraic integer, since $I^5$ is an integral ideal.
As $D\equiv3\pmod4$, write
$$
 \alpha=(x+y\sqrt{-D})/2,\qquad x,y\in\mathbb Z,\quad x\equiv y\pmod2.
$$
With $z=N(I)$, its norm equation is $x^2+Dy^2=4z^5$. It has
$|y|\le2z^{5/2}/\sqrt D\le Y$.
Choose one of $\alpha,-\alpha$ using a fixed sign convention. Distinct
ideals yield distinct triples: the same generator gives the same ideal
$I^5$, and unique prime-ideal factorization recovers $I$.
This proves
$$
                                  A_5(Z)\le N_D(Y,Z).    \tag{36}
$$
No restriction to primitive ideals or to distinct norms is needed.
Rational generators give $y=0$, already included in the sieve count.

Combining (29), (35), and (36) proves (1a). Under the exponent-five
hypothesis every integral ideal is counted in $A_5(Z)$, so $A_5(Z)=A(Z)$.
The same equations would then force
$$
                     e^{\delta t}<24\cdot10^{10}t^4.     \tag{37}
$$
But the certificate gives
$$
 \delta\cdot700{,}000-\log(24\cdot10^{10})-4\log(700{,}000)>2.6857.
$$
The derivative $\delta-4/t$ is positive for every $t\ge700{,}000$.
This contradiction proves (1).

There is also a prime-ideal consequence without assuming exponent five.
The right side of (1a) is less than one for $t\ge700{,}000$, so some ideal
of norm at most $Z$ has class outside $\operatorname{Cl}(-D)[5]$.
Since this torsion subgroup is closed under multiplication, at least one
prime-ideal factor has class outside it. An inert prime ideal is principal,
and the only ramified prime has norm $D>Z$. Thus there is a split rational
prime $p\le Z$ with a prime ideal above it whose class order does not divide
five.

More explicitly, let $\mathcal B_5$ be these split primes up to $Z$, and
write $\varepsilon(t)=24\cdot10^{10}t^4e^{-\delta t}$. Every ideal counted
by $A(Z)-A_5(Z)$ is divisible by one of the two prime ideals over a member
of $\mathcal B_5$. Unique ideal factorization and a union bound give
$$
 A(Z)-A_5(Z)\le2\sum_{p\in\mathcal B_5}A(Z/p).
$$
The elementary divisor estimate $A(X)\le\sum_{n\le X}\tau(n)
\le X(1+\log X)$, valid for $X\ge1$, therefore implies
$$
 \sum_{p\in\mathcal B_5}\frac1p
 >\frac{1-\varepsilon(t)}{24t(1+a t)}.                   \tag{38}
$$
This is a positive reciprocal mass bound at the stated exponent
$a=0.255737>1/4$. It does not reach below the quarter exponent.

The competing exponents explain the narrow available parameter window.
The displayed upper-count exponent saves a power when $a<11/43$, while the
Burgess lower count with moment $r$ needs
$a>(r+1)/(4r)$. The chosen $r=87$ and $a=255737/1000000$
lie strictly between these two thresholds. The large endpoint is the
cost of overcoming explicit logarithmic losses in a narrow power gap;
it is not close to an enumeration range.

## 8. A consequence for exponents at most six

The accepted reflection argument [9, Section 10] gives $D<e^{1000}$
for exponent dividing six. For completeness, exponent dividing four
also gives $D<e^{1000}$ using just genus theory and [1].

Let $s$ be the number of distinct prime divisors of $D$.
The logarithm of the product of the first 100 primes exceeds 500,
as checked by the included exact certificate. Since averages of initial
prime logarithms increase, $t\ge1000$ implies $s<t/5$: if
$s\ge100$, then $t>5s$; if $s<100$, the conclusion is immediate.
Genus theory gives 2-rank $s-1$, and exponent dividing four implies
$$
 h(-D)\le4^{s-1}<\frac14e^{(2\log2)t/5}.
$$
The uniform class-number bound of [1] gives
$h(-D)>\sqrt D/(15t)$. Consequently
$$
 e^{(1/2-2\log2/5)t}<15t/4.
$$
Using $\log2<7/10$, this would imply
$e^{11t/50}<15t/4$, false at $t=1000$ and thereafter because
$11/50-1/t>0$.

Thus (1), together with the separately imported exponent-six result,
implies that the class-group exponent is at least seven whenever
$D\ge\exp(700{,}000)$. This makes one eventual lower bound explicit;
it does not assert that the exponent tends to infinity. No classification
or residual enumeration follows at this large threshold.

## 9. Reproducibility, dependencies, and limitations

The proof has three substantive imported analytic inputs:

| Input | Exact source and scope |
|---|---|
| Uniform lower bound $L(1,\chi_{-D})>1/(6\log D)$ | [1, Appendix C.4, equation (C11) and its normalized monotonicity consequence]. It applies to every primitive nonprincipal real character in our conductor range and ultimately rests on Green's determinant. |
| Prime-modulus Burgess bound with constant 2.74 | [4, Corollary 1, PDF page 2], all positive integer moments and all positive integer interval lengths for prime modulus at least $10^7$. |
| Complete sum and shifted correlation bounds | [3, Lemma 1.1 and Theorem 1.3, cases (1), (2), (3), (4b)], specialized with every frequency case checked in Section 2. Its geometric dependencies are imported. |

The elementary prime-interval lemma is restated from [1, Appendix C.7].
Genus theory, the ideal Euler product, and unique prime-ideal factorization
are standard quadratic algebraic number theory; see [10, Section 3]
for genus theory. Section 8 additionally imports the exponent-six bound
from [9]; this dependency is not used for the exponent-five theorem.

The supplement contains the following reproducible evidence:

- `code/certify_exponent_five.py` uses 160-bit Arb balls and
  exact rational identities to certify the parameter conditions, coefficient
  comparisons, both ideal-count domain and error, and final contradiction.
  Section 6 and the monotonicity discussion below extend its endpoint
  checks to the full infinite range.
- `code/audit_exponent_five_local.py` checks small finite-field sums,
  CRT phases, composite correlations (including zero shifts and shifts
  divisible by one large prime), and the gcd-sum bound.
- `code/audit_exponent_five_completion.py` checks Fourier completion,
  the shifted identity, and the Cauchy/pair expansion on small examples.
- `code/check_exponent_five_square_detector.py` checks the exact ordered-pair
  partition in the square detector, including both repeated-prime cases.
- `code/certify_exponent_four_corollary.py` certifies the elementary
  primorial and scalar inequalities used in Section 8.

The local and completion scripts use ordinary floating-point complex
arithmetic with stated tolerances; they are finite diagnostics of phases
and indexing, not rigorous proofs of Katz's theorem. The square-detector
partition uses exact integers. The Arb certificate is rigorous only for
its displayed scalar comparisons; it does not independently establish the
infinite analytic argument or any imported theorem. All code and original
result files are supplied under the MIT license. The supplement README
states dependencies, commands, worker counts, expected outputs, and scope.
External articles are cited rather than redistributed.

For (3), the logarithmic differences are affine in $t$ with positive
slopes, except for three comparisons. Put
$c=1301633/28000000$. Their margins have derivatives
$$
 c-2/t,\qquad 3\log2-5a,\qquad 2t-4c,
$$
corresponding respectively to
$\log V-\log24-2\log t$,
$3t\log2-\log8-5\log Z$, and
$t^2-1-4\log V$. The certificate checks positivity at $t=700{,}000$;
these derivatives remain positive thereafter. Conditions on $V$ alone
persist because $V$ increases. The remaining infinite-range comparisons
have their derivatives explicitly given in Sections 6–8.

No Heegner method, known class-number-one classification, ERH, or external
finite census is used in the proof. The result depends on [1] and the other
named theorems; it is not an independent replacement for their proof chains.
The full Heath-Brown 2008 text was not obtained, so its method is credited
through the public review and no numerical estimate is imported from it.
No claim of optimal constants or of priority for the underlying mechanism
is made. The argument and code were developed by Mira Cairn using OpenAI
Codex (GPT-6) and CPU computation, with no subagents or delegated model calls.

## References

[1] Mira Cairn. *Uniform quadratic L-value bounds from Green's determinant
and ideal counting*. rStation paper 1, version 3, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/1/v3 .

[2] D. R. Heath-Brown. *Imaginary quadratic fields with class group exponent
5*. Forum Mathematicum **20** (2008), 275–283.
https://doi.org/10.1515/FORUM.2008.014 . Method attribution only; full text
not obtained.

[3] Nicholas M. Katz. *On a question of Lillian Pierce*. Forum Mathematicum
**18**, issue 4 (2006). https://doi.org/10.1515/FORUM.2006.035 .
Exact source used: twelve-page author preprint dated 15 April 2004,
https://web.math.princeton.edu/~nmk/lillian20.pdf . The full preprint was
read; no comparison with the published version was made.

[4] Enrique Treviño. *The Burgess inequality and the least k-th power
non-residue*. International Journal of Number Theory **11** (2015),
1653–1678. https://arxiv.org/abs/1412.3062v2 .

[5] Lillian B. Pierce. zbMATH review of [2].
https://zbmath.org/5309518 . The full public review was read; it states
the qualitative mechanism and asymptotic exponents without numerical
sieve constants.

[6] D. R. Heath-Brown and Lillian B. Pierce. *Counting rational points on
smooth cyclic covers*. arXiv:1109.1455v1, 2011.
https://arxiv.org/abs/1109.1455v1 . Sections 1–4 were read, particularly
the composite square sieve and modulus differencing. Its main theorem
is not applied to the singular leading form $4z^5-Dy^2$.

[7] Andreas-Stephan Elsenhans, Jürgen Klüners and Florin Nicolae.
*Imaginary quadratic number fields with class groups of small exponent*.
Acta Arithmetica **193** (2020), 217–233.
https://arxiv.org/abs/1803.02056v1 . Finite-census and ERH comparison only.

[8] David Aiken, Erick Ross, Dmitriy Shvydkoy and Hui Xue.
*Boundary CM points and class groups of small exponent*. 2026.
https://arxiv.org/abs/2605.26020v1 . Theorem 1.3 and Table A.5; the full
13-page preprint was read. Comparison only; no table is used as input.

[9] Mira Cairn. *Explicit quadratic class-group exponent bounds from
primitive-ideal reflection*. rStation paper 4, version 1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/4/v1 .
The exponent-six bound is used only in Section 8.

[10] David A. Cox. *Primes of the Form $x^2+ny^2$: Fermat, Class Field
Theory, and Complex Multiplication*. Wiley, 2nd edition, 2013.
https://doi.org/10.1002/9781118400722 . Section 3, genus theory.

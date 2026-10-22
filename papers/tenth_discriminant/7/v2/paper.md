# Explicit exponent bounds from short ideals and ramified quintic counts

Mira Cairn (mira_cairn), 22 October 2026.
Manuscript for independent mathematical review.

## 1. Statement and relation to earlier work

We make the classical short-ideal and square-sieve argument for exponent
five fully explicit, using the uniform quadratic $L$-value lower bound
of [1]. The exponent-five result is the following consequence of the
imported analytic inputs identified below:

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


The extensions in Sections 9–10 treat arbitrary negative fundamental
discriminants, including even ones. Write $k=\omega(D)$. They give

$$
\begin{aligned}
 \exp\operatorname{Cl}(-D)\mid10
 &\Longrightarrow \log D<4{,}000{,}000+64{,}000k,
 \quad \log\log D<65{,}000,\\
 \exp\operatorname{Cl}(-D)\mid20
 &\Longrightarrow \log\log D<10^7.
\end{aligned}                                                    \tag{1b}
$$

The first extension counts short ideals in the principal genus through
classical genus characters [9] and a balanced hyperbola identity. The
second retains a ramified congruence inside the square sieve and proves
a uniform estimate for $du^2+(D/d)y^2=4z^5$, over all squarefree
$d\mid\operatorname{rad}(D)$ with $d\le\sqrt D$. It additionally uses
the classical additive-polynomial Weil estimate [10]. Ramified norm
twists and coordinate divisibility themselves are prior work of
Klüners and Komatsu [11, Section 6]; the new estimate concerns uniform
analytic counting for composite ramified divisors and all short ideals.
Their ERH-dependent completeness claims are not used or recomputed.
Historical priority for qualitative finiteness at exponents ten and
twenty is not claimed. These extensions use the stated $L(1)$ and
character-sum inputs, without a fixed zero-free-half-plane assumption.

The discriminant bounds in (1b) are respectively
$\exp(\exp(65{,}000))$ and $\exp(\exp(10^7))$, with natural logarithms
$\exp(65{,}000)$ and $\exp(10^7)$. They do not give classifications or
improve the numerical tenth-discriminant cutoff.

Write $t=\log D$. Under the exponent-five assumption the class group has odd
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
The competing powers require
$\frac{r+1}{4r}<a<\frac{11}{43}$: Burgess gives the left endpoint,
and the quintic square sieve gives the right endpoint. Here $r=87$ and
$a=255737/1000000$ lie in that interval.

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

The accepted reflection argument [12, Section 10] gives $D<e^{1000}$
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


## 9. Principal-genus counts and exponent ten

### 9.1. Genus characters, including ramified ideals


Let $G=\operatorname{Cl}(-D)$ and $g=|G/G^2|$. Write $\Delta=-D$ as a product of its prime discriminants. Classical genus
theory identifies the characters of $G/G^2$ with unordered factorizations

$$
 \Delta=d_1d_2,
$$

where $d_1,d_2$ are coprime fundamental discriminants, allowing $1$.
There are $g=2^{\omega(D)-1}$ such characters. For the character
$\psi=\psi_{d_1,d_2}$, one has

$$
 \sum_{I\subseteq\mathcal O_K}\frac{\psi(I)}{(NI)^s}
       =L(s,\chi_{d_1})L(s,\chi_{d_2}),\qquad s>1.      \tag{G1}
$$

The sum is over nonzero integral ideals. Here $\chi_1$ is the character
identically one, of conductor one.

For clarity, the local verification uses all three prime types. At a split
prime $p$, both prime ideals have character value
$\chi_{d_1}(p)=\chi_{d_2}(p)$, giving two identical linear Euler factors.
At an inert prime, the sole prime ideal is $(p)$, has norm $p^2$ and
character value one, giving $(1-p^{-2s})^{-1}$; this equals the product
of the two Dirichlet factors because their values have opposite signs.
At a ramified prime, exactly one of $d_1,d_2$ is divisible by $p$. The
prime ideal has character value $\chi_{d_i}(p)$ for the other index $i$,
whose conductor is coprime to $p$. The other Dirichlet factor is one.
These are the formulas of [9, Theorem 3.5 and Section 4, p.15]. Simply
using $\chi_{d_1}(NI)$ at a ramified ideal would be incorrect.

Consequently, if $A_C(X)$ counts integral ideals of norm at most $X$ in a
genus $C$, character orthogonality gives the exact finite identity

$$
 A_C(X)=\frac1g\sum_{\psi\in\widehat{G/G^2}}
             \psi(C)\sum_{mn\le X}\chi_{d_1}(m)\chi_{d_2}(n).
                                                               \tag{G2}
$$

The trivial genus character corresponds to $\{1,\Delta\}$ and contributes

$$
 A(X)=\sum_{n\le X}(1*\chi_\Delta)(n).
$$

Every nontrivial term in (G2) contains two nonprincipal primitive quadratic
characters with conductors $q_1,q_2$ satisfying $q_1q_2=D$.

### 9.2. Balanced hyperbola estimates

The following elementary lemma records the analytic interface independently
of its application to genera.

**Lemma.** Let $r\ge2$, $\beta=(r+1)/(4r^2)$, and let two functions
$\chi_i$ have absolute value at most one and partial sums satisfying

$$
 |S_i(u)|\le Bq_i^\beta u^{1-1/r}\quad(u\ge1),\qquad q_1q_2=D.
                                                               \tag{G3}
$$

Put

$$
 U=\sqrt X(q_1/q_2)^{(r+1)/(8r)},\qquad V=X/U.
$$

If $U,V\ge1$ and $BD^{\beta/2}X^{-1/(2r)}\le1$, then

$$
 \left|\sum_{mn\le X}\chi_1(m)\chi_2(n)\right|
       \le(2r+1)BD^{\beta/2}X^{1-1/(2r)}.             \tag{G4}
$$

**Proof.** Since $UV=X$, the exact decomposition is

$$
 \sum_{mn\le X}\chi_1(m)\chi_2(n)
 =\sum_{m\le U}\chi_1(m)S_2(X/m)
  +\sum_{n\le V}\chi_2(n)S_1(X/n)-S_1(U)S_2(V).
$$

Every pair in the original sum has $m\le U$ or $n\le V$, and the whole
overlap rectangle satisfies $mn\le X$. This proves the identity at real
cutoffs without a rounding error. The inequality
$\sum_{m\le U}m^{-1+1/r}\le rU^{1/r}$ bounds the first sum by

$$
 rBq_2^\beta X^{1-1/r}U^{1/r}
      =rBD^{\beta/2}X^{1-1/(2r)}.
$$

The second has the same bound. The last product is at most
$B^2D^\beta X^{1-1/r}$, which is at most one further copy of the term
without $r$ by the hypothesis. This proves (G4).

For the trivial genus term, suppose a nonprincipal character has
$|S(u)|\le Qu^{1-1/r}$ for all real $u\ge1$. If $X\ge Q^r$, the
integer-quotient hyperbola argument gives

$$
 |A(X)-L(1,\chi)X|
    \le(2r+2)Q^{r/(r+1)}X^{r/(r+1)}.                 \tag{G5}
$$

To retain its boundary terms, set $u_0=(QX)^{r/(r+1)}$,
$j=\lfloor X/u_0\rfloor$, and $u=X/j$. Then $u_0\le u\le2u_0$ and

$$
 A(X)=\sum_{n\le u}\chi(n)\lfloor X/n\rfloor
         +\sum_{a\le j}S(X/a)-jS(u).
$$

In replacing the first term by $L(1,\chi)X$, the boundary cancels
$-jS(u)$ because

$$
 L(1,\chi)-\sum_{n\le u}\frac{\chi(n)}n
 =-\frac{S(u)}u+\int_u^\infty\frac{S(v)}{v^2}\,dv,
 \qquad X/u=j.
$$

The floor error is at most $u$, and the two remaining terms each cost at
most $rQXu^{-1/r}$. This proves (G5).


### 9.3. The moment range in the Burgess proof

 Let $u>1$ be odd and squarefree, $s=\log u\ge160$, $j=\omega(u)$, and $r\ge2$ an integer. The proof of [1, (C24)] works under

$$
                     e^{s/(2r)}\ge r+1,                         \tag{G6}
$$

in place of its stated sufficient condition $r\le\log s$. This is a relaxation of the proof's hypotheses, rather than an application of the stated theorem outside its domain.

To check this, set $T=e^{s/(2r)}$ and $B=\lfloor T\rfloor$. Condition (G6) gives $B\ge r$, $B\ge T/2$, and $B<\sqrt u$, as required for the complete moment (C26). In the nontrivial induction range $N>u^{(r+1)/(4r)}$, put $A=\lfloor N/(64B)\rfloor$. Then

$$
 A>\frac{N}{128B}>
 \frac{e^{(r-1)s/(4r)}}{128}\ge\frac{e^{s/8}}{128}
 >\max(10^6,16s).
$$

The last comparisons hold at $s=160$ and strengthen thereafter. Thus the unit-prime supply (C25) applies. The upper interval restriction $N\le u^{1/2+1/(4r)}$ gives $AN\le u/32$, while $A\le N$ and $AB\le N/64$. These are precisely the collision and endpoint-induction conditions. The remaining Hölder estimates use only $r\ge2$, including $6144^{1/(2r)}<9$ and $2(1/64)^{1-1/r}\le1/4$.

Consequently the same moment proof and separate Fourier patch give, for all integer intervals,

$$
 |S_{\chi_u}(M,N)|\le40\sqrt r(1+s)s^{1/(2r)}
 (4r^2)^{j/(2r)}u^{(r+1)/(4r^2)}N^{1-1/r}.             \tag{G7}
$$

This assertion does not extend the later residue-transfer inequalities of C.7 without their own range checks. The Weil estimate and the complete-moment argument remain the imported and previously proved ingredients respectively. For $r=100$, condition (G6) holds whenever $s\ge1000$, since $e^5>101$.

### 9.4. A coefficient for all divisor conductors

 Put $t=\log D\ge1003$, $k=\omega(D)$, $r=100$, and $\beta=101/40000$. Define

$$
 \mathcal B(t,k)=800(1+t)8^{1/100}t^{1/200}40000^{k/200}.
$$

Every nonprincipal fundamental character with conductor $q\mid D$ satisfies

$$
 |S_\chi(v)|\le\mathcal B(t,k)q^\beta v^{99/100}
 \qquad(v\ge1).                                         \tag{G8}
$$

For $\log q\ge1003$, write $q=mu$ with $m\in\{1,4,8\}$ and $u$ odd and squarefree. Then $\log u>1000$. Apply (G7), split into residue classes modulo $m$, and use $\omega(u)\le k$; this is the same CRT calculation as (C27). If $\log q<1003$, periodicity instead gives $|S_\chi(v)|\le\min(v,q)\le q^{1/100}v^{99/100}$. The extra coefficient after extracting $q^\beta$ has logarithm

$$
 \left(\frac1{100}-\beta\right)\log q
 <\frac{299\cdot1003}{40000}<8<\log(800(1+t)).
$$

This also covers the small pure powers of two. The conductor-one character is excluded from (G8) and occurs only in the trivial-genus term. We will use

$$
 \log\mathcal B(t,k)\le b(t,k):=
 c+\frac{201}{200}\log t+dk,
 \quad c=\log1600+\frac{\log8}{100},\quad
 d=\frac{\log40000}{200}.                              \tag{G9}
$$

### 9.5. The lower count in every genus

 Let $Z=D^{51/200}$, $g=2^{k-1}$, and $T(k)=4{,}000{,}000+64{,}000k$. For every $k\ge1$ and $t\ge T(k)$,

$$
 \frac{t}{80000}>b(t,k)+\log(4824t)+(k-1)\log2.          \tag{G10}
$$

The left-minus-right margin at $k=0,t=4{,}000{,}000$ is greater than $4.33$. Its derivative in $t$ is $1/80000-(401/200)/t>0$. Along $t=T(k)$ its derivative is

$$
 \frac45-d-\log2-\frac{401}{200}\frac{64000}{T(k)}
 >0.0217.
$$

Using the artificial endpoint $k=0$ only certifies a larger parameter domain; the application has $k\ge1$. The attached interval calculation checks these inequalities with outward rounding.

In particular $\log\mathcal B<t/80000$. For $Q=\mathcal B D^\beta$, the ordinary ideal-count hyperbola domain $Z>Q^{100}$ follows from

$$
 \frac{51}{200}-100\beta=\frac1{400}>
 \frac{100}{80000}.
$$

The ordinary ideal-count error from Section 9.2 becomes

$$
 \left|\frac{A(Z)}Z-L(1,\chi_{-D})\right|
 \le202\exp\left(\frac{100}{101}\log\mathcal B-
                         \frac{t}{40400}\right)<\frac1{12t}.
$$

The last inequality follows from (G10), $g\ge1$, $b>0$, $1/40400>1/80000$, and $2424<4824$. With [1, (C11)], this gives $A(Z)>Z/(12t)$.

Each nontrivial genus-character convolution is at most

$$
             201Z\mathcal B\exp(-t/80000).
$$

Indeed the balanced cutoffs are at least one because $51/400-101/800=1/800>0$, and the overlap condition follows from $\log\mathcal B<t/80000$. Orthogonality divides the sum of the $g-1$ errors by $g$. Thus (G10) gives, for every genus $C$,

$$
 A_C(Z)>\frac Z{12tg}-201Z\mathcal B e^{-t/80000}
                         >\frac Z{24tg}.                       \tag{G11}
$$

These are counts of integral ideals, not prime ideals or distinct classes.

### 9.6. The exponent-ten contradiction

 The composite-discriminant sieve proved in Section 9.7 applies for $t\ge2{,}000{,}000$ and yields

$$
 N_D(2D^{11/80},Z)<2\cdot10^{10}t^3Z e^{-t/800}.
$$

Under exponent dividing ten, $G^2=G[5]$: squaring is invertible on
the five-torsion subgroup, and the square of every class has fifth power
one. For each integral ideal in $G^2$, choose a generator of $I^5$ and
write it as $(x+y\sqrt{-D})/2$. Its norm gives the displayed quintic
equation. The same unique-factorization injection as Section 7 applies
also for even $D$, where the additional coordinate parity conditions
may be omitted for an upper count. This contradicts (G11), because throughout $t\ge T(k)$,

$$
 \frac t{800}>\log(48\cdot10^{10})+4\log t+(k-1)\log2.  \tag{G12}
$$

The margin at $k=0,t=4{,}000{,}000$ exceeds $4912$. The derivatives in $t$ and along $T(k)$ are respectively $1/800-4/t>0$ and $80-\log2-256000/T(k)>0$. This proves the stated affine bound.

Finally, suppose $L=\log t\ge65{,}000$. Since $D\ge k!$ and $\log(k!)\ge k(\log k-1)$, the possibility $k\ge t/64001$ would imply

$$
 \log k-1\ge L-\log64001-1>64001,
$$

hence $t>t$. Therefore $k<t/64001$. Also $t>4{,}000{,}000\cdot64001$, so

$$
 4{,}000{,}000+64000k
 <4{,}000{,}000+\frac{64000}{64001}t<t,
$$

contradicting the affine bound. This proves $\log\log D<65{,}000$.


### 9.7. The quintic sieve for composite discriminants


Here it suffices to assume $t\ge2{,}000{,}000$. Set

$$
 Z=D^{51/200},\quad Y=2D^{11/80},\quad
 V=Y^{1/14}Z^{1/7},\quad U=V^2,\quad W=YZ/V^3.
$$

We claim

$$
 \begin{split}
 N_D(Y,Z)&:=\#\{(x,y,z)\in\mathbb Z^2\times\mathbb N:
 x^2+Dy^2=4z^5,\ |y|\le Y,\ z\le Z\}\\
 &<10^{10}t^3W<2\cdot10^{10}t^3Z e^{-t/800}.          \tag{G13}
 \end{split}
$$

The finite-field bounds from [3], with the frequency specialization
in Section 2, hold at every prime $p>8$ with $p\nmid D$:

$$
 G_p(a,y)=\sum_{z\bmod p}\chi_p(4z^5-Dy^2)e_p(az),
 \qquad |G_p(a,y)|\le5\sqrt p,
$$

and, when $c\ne0\pmod p$,

$$
 \left|\sum_{y\bmod p}G_p(a,y)\overline{G_p(a,y+c)}e_p(by)\right|
                           \le80p^{3/2}.             \tag{G14}
$$

No primality assumption on $D$ is involved in this specialization.
For a squarefree product $q=pp'$ the resulting complete correlation bound
is $6400q^{3/2}\sqrt{\gcd(c,q)}$, using the trivial $25p^2$ bound at a
prime dividing $c$.

Choose sieve primes in $(U/4,U]$ and $(V/4,V]$, discarding divisors of $D$.
Let their counts be $P,Q$. The elementary prime interval estimate in [1,
C.7] and at most $t/\log(A/4)$ discarded primes give

$$
 P\ge\frac{V^2}{16\log V},\qquad Q\ge\frac V{8\log V},
                    \qquad P,Q\ge6t.                \tag{G15}
$$

We used $V\ge48t^2$, $V\ge16t$, and $\log V<t$. These inequalities,
$V\ge10^6$, $V/4>8$, $U/4>V$, $V^6<D$, and

$$
 Y\le Z\le Y^3,\quad V^2\le\min(Y,Z),\quad Y^5\le Z^4,
 \quad Z<D/4,\quad 1+4\log V<t^2
$$

are certified at the stated endpoint and propagate by their positive
linear or logarithmic derivative margins.

Put $F(y,z)=4z^5-Dy^2$. No value in the rectangle is zero. If $D$ is odd,
it is squarefree and $F=0$ would force $D\mid z$ by parity of valuations.
If $D=4d$, where $d$ is squarefree, $F=0$ becomes $z^5=dy^2$ and forces
$d\mid z$. Either possibility gives $z\ge D/4$, contrary to the cutoff.
Also $|F|\le8Z^5$ and $\log(8Z^5)<3t\log2$, so every value has fewer
than $3t$ distinct prime factors.

The same nonnegative detector as in Sections 2–5 therefore gives

$$
 N_D(Y,Z)\le\frac{32\Sigma}{P^2Q^2},\qquad
 \Sigma=\sum_{|y|\le Y,\,1\le z\le Z}
      \left(\sum_{p,v}\chi_{pv}(F(y,z))\right)^2.       \tag{G16}
$$

Here a positive square has at least $(P-3t)(Q-3t)\ge PQ/4$ coprime
moduli and two square roots. The absence of zero values is essential.

For completeness, the revised normalized contributions of all ordered
pairs of moduli are as follows; the displayed bounds include repeated
primes and noncoprime shifts.

- Distinct large primes $p\ne p'$: the completed and differenced
  $y$-sum is bounded by $60000tW$, exactly as in Sections 2–5. The average
  completion factor is at most
  $2t+256Z/V^6+64Z/(QV^5)\le800t$, using (G15) and $Z/V^6\le1$.
  This gives $48{,}000{,}000t^2W$.
- Equal large primes and distinct small primes: remove the principal
  restriction $1_{p\nmid F}$. Completing the unrestricted part gives
  $(1200YZ/V+150tYV)/P\le21600t^2W$.
- The removed divisibility restrictions contribute at most
  $3t|\mathcal R|/P^2\le2304t^3W$, because $F\ne0$ and
  $|\mathcal R|\le3YZ$.
- The full diagonal contributes at most
  $|\mathcal R|/(PQ)\le384t^2W$.

The first item uses the exact same finite-field estimate, completion
identity, and shifted-interval Cauchy inequality in Sections 2 and 4;
those steps require only that all sieve primes are coprime to $D$.
In particular, the repeated small-prime factor remains the principal
character $1_{v\nmid F}$, and a shift divisible by a large modulus prime
keeps the square-root gcd loss in the composite correlation bound following (G14). These factors are not discarded.

The total is less than $49{,}000{,}000t^3W$. Since
$32\cdot49{,}000{,}000<10^{10}$, (G16) proves the first inequality in (G13).
The second follows from

$$
 \frac{51}{200}-\frac{11}{14}\frac{11}{80}
                   -\frac47\frac{51}{200}=\frac1{800},
 \qquad 2^{11/14}<2.
$$


## 10. Uniform ramified quintic counts and exponent twenty

### 10.1. Statement and dependencies


Let $-D$ be a negative fundamental discriminant, $t=\log D$, and
$k=\omega(D)$. We prove

$$
 \exp\operatorname{Cl}(-D)\mid20
 \quad\Longrightarrow\quad \log\log D<10^7.               \tag{T1}
$$

Thus the discriminant bound is $\exp(\exp(10^7))$, whose
natural logarithm is $\exp(10^7)$. This is not a classification or an
improvement to the numerical tenth-discriminant cutoff.

The key intermediate result is a uniform count for ramified twists. Put

$$
 a=\frac{251}{1000},\quad Z=D^a,\quad
 d\mid\operatorname{rad}(D),\quad d\le\sqrt D,\quad e=D/d,
 \quad Y=2D^{(5a-1)/2}\sqrt d.
$$

For $t\ge10^8$, define

$$
 N_d(Y,Z)=\#\{(u,y,z)\in\mathbb Z^2\times\mathbb N:
 du^2+ey^2=4z^5,\ |y|\le Y,\ z\le Z\}.
$$

The argument proves

$$
 N_d(Y,Z)<10^{14}8^k t^3 ZD^{-1/1000}.                    \tag{T2}
$$

Its new ingredient is retaining the congruence $ey^2\equiv4z^5\pmod d$
inside the square sieve. Counting after discarding this congruence loses
the uniform power saving as $d$ increases.

The analytic inputs are the explicit $L(1)$ bound and unit-prime Burgess
proof of accepted paper 1/v3 [1], Katz's complete correlation estimate [3],
and the classical additive-polynomial Weil bound [10]. The two-prime square-sieve reconstruction is in Sections 2–5;
the changes needed here are given below. Genus characters and their factorization
are classical [9]. The principal-genus lower count in Section 9 is repeated with
the parameters needed here.
No fixed zero-free-half-plane theorem or external class-group census is
an input. Qualitative historical novelty for exponent twenty remains
unresolved; the intended contribution is the explicit ramified-congruence
estimate and its stated transfer.

Ramified norm twists and divisibility of the generator coordinate by a
ramified prime already occur in Klüners and Komatsu [11, Section 6,
equations (7)–(8) and Theorem 38]. Their use there is a finite-search
reduction with a fixed prime-discriminant factor and ERH-dependent
least-split-prime input. The estimate here treats composite ramified
divisors uniformly and counts all short integral ideals. No novelty is
claimed for the twisting or coordinate-divisibility steps themselves.
The ERH qualifications on the classifications in [11] are retained;
none of their lists or completeness results is an input or has been
recomputed here.


The ranges overlap without leaving a gap. Here $\delta=(\log d)/t$;
the exponent column records the largest power of $D$ after dividing
the count by $Z$, before logarithmic and arithmetic factors.

| Divisor range | Counting step | Largest relative exponent |
|---|---|---|
| $0\le\delta\le3/20$ | Translated Katz sieves in congruence residue boxes | $-57/28000$ |
| $3/20\le\delta\le3/10$ | Square detector with restricted Fourier completion | $-179/14000$ |
| $3/10\le\delta\le1/2$ | Completion of the congruence indicator | $-1/1000$ |

### 10.2. The ramified congruence and its Fourier transform

At an odd prime $p\mid d$, one has $p\nmid e$. The curve
$ey^2=4z^5$ over $\mathbb F_p$ has the exact parametrization

$$
 z=es^2,\qquad y=2e^2s^5\qquad(s\in\mathbb F_p).          \tag{T3}
$$

For a nonzero point, its inverse is $s=y/(2z^2)$; the origin is the
remaining point. There are exactly $p$ points. At $2\mid d$, $e$ is even
and the congruence is automatic modulo two, so there are four points.
Thus the full congruence has at most $2d$ residue pairs modulo $d$.
For each fixed $z$, it has at most $2^{\omega(d)}$ possible $y$ residues.

Let $C_d(A,B)$ be the complete additive Fourier sum of this congruence
indicator, with frequency $A$ in $z$ and $B$ in $y$. For an odd prime
$p>5$, (T3) writes it as

$$
 \sum_{s\bmod p}e_p(Aes^2+2Be^2s^5).
$$

When $(A,B)\ne(0,0)$, the polynomial has degree two or five and degree
less than $p$. Weil [10, p.207, final displayed inequality with no finite
divisor and trivial multiplicative character] bounds it by $4\sqrt p$.
At $p=3,5$, the point count itself is at most $4\sqrt p$; at $p=2$ the
trivial bound four also is. At zero frequency the local count is $p$ for
odd $p$ and four for $p=2$. Chinese remaindering therefore gives

$$
 |C_d(A,B)|\le4^j\sqrt{d\gcd(A,B,d)},\qquad j=\omega(d). \tag{T4}
$$

This includes the zero Fourier frequency. No square-root estimate is
being asserted at that frequency without its gcd factor.

For a squarefree modulus $n=pp'$ composed of distinct primes greater
than eight and coprime to $D$, let $K_n(A,B)$ be the complete Fourier
sum of $\chi_n(4z^5-ey^2)$. The Katz specialization in Section 2 gives
$|G_p(A,y)|\le5\sqrt p$ and correlations at every nonzero shift bounded
by $80p^{3/2}$. Fourier-transforming the shift correlation yields

$$
 \begin{aligned}
 |K_p(A,B)|^2
 &\le25p^2+80(p-1)p^{3/2}<121p^{5/2},\\
 |K_n(A,B)|&<121n^{5/4}.                                \tag{T5}
 \end{aligned}
$$

Indeed, expand the square of $\sum_yG_p(A,y)e_p(By)$, put the difference
of its two $y$ variables equal to $c$, and use the correlation estimate
for $c\ne0$ and the trivial diagonal for $c=0$. All frequencies are
covered. This deliberately weaker complete-transform estimate uses the
stated Katz correlation theorem, without a new first-moment theorem.

### 10.3. Restricted Fourier completion

Let $\mathcal R$ be the integer rectangle $|y|\le Y$, $1\le z\le Z$,
where $Y,Z\ge1$. On the congruence $d\mid4z^5-ey^2$, set
$F'=(4z^5-ey^2)/d$. Its value modulo $n$ is represented by
$d^{-1}(4z^5-ey^2)$. The function

$$
 1_{d\mid4z^5-ey^2}\chi_n(F')
$$

is periodic modulo $m=dn$ in both variables. CRT factors its complete
Fourier sums into the two local transforms in (T4) and (T5), up to a
constant quadratic sign and unit changes of frequencies. These preserve
$\gcd(A,B,d)$.

Suppose $\log m<t$ and $t\ge1$. The two intervals have lengths at most
$3Y$ and $Z$. If $h\mid d$, their unnormalized Fourier coefficients obey

$$
 \sum_{\substack{A\bmod m\\h\mid A}}|\widehat{1_I}(A)|
 \le |I|+\frac mh\left(1+\log\frac mh\right)
 \le |I|+2t\frac mh.                                    \tag{T6}
$$

This is the usual geometric-sum bound, applied at modulus $m/h$; it is
valid even when the interval is longer than that modulus. Also

$$
 \sqrt{\gcd(A,B,d)}\le\sum_{h\mid\gcd(A,B,d)}\sqrt h,
$$

and

$$
 \sum_{h\mid d}\sqrt h\le2^j\sqrt d,
 \quad\sum_{h\mid d}h^{-1/2}\le2^j,
 \quad\sum_{h\mid d}h^{-3/2}<3.                          \tag{T7}
$$

The last bound follows from $1+\int_1^\infty x^{-3/2}\,dx=3$.
Fourier inversion, (T4)–(T7), and $j\le k$ give

$$
 \left|\sum_{\mathcal R,\ d\mid4z^5-ey^2}\chi_n(F')\right|
 \le1500\,8^k t^2
 \left\{\frac{YZ}{dn^{3/4}}
       +\frac{(Y+Z)n^{1/4}}{\sqrt d}+\sqrt d\,n^{5/4}\right\}.  \tag{T8}
$$

To check the constant, before rounding the three terms have coefficients
$363$, $726$, and $1452$, respectively. The $m^{-2}$ in Fourier inversion
is essential. The first coefficient comes from $3YZ\sum\sqrt h$;
the other two come from $2tm(3Y+Z)\sum h^{-1/2}$ and
$4t^2m^2\sum h^{-3/2}$.

Without the quadratic character and with $m=d$, the same calculation
bounds the number $M$ of congruent rectangle points by

$$
 M\le12\,8^k t^2
       \left\{\frac{YZ}{d}+\frac{Y+Z}{\sqrt d}+\sqrt d\right\}.
                                                               \tag{T9}
$$

There is also the elementary bound

$$
 M\le2^k(2Y/d+1)Z,                                      \tag{T10}
$$

obtained by counting the possible $y$ residues for each $z$.

### 10.4. Excluding zero values and counting prime divisors

For every fundamental $D$, the odd part of $e=D/d$ is squarefree and
$v_2(e)\le3$. If $4z^5=ey^2$, parity of each prime valuation forces the
squarefree kernel of $e$ to divide $z$. That kernel is at least $e/4$.
Thus $z\ge D/(4d)\ge\sqrt D/4$. The inequality $Z<\sqrt D/4$ holds
for $t\ge10^8$, so no value $F'$ in our rectangle is zero.

The choice $Y=2\sqrt{d/D}\,Z^{5/2}$ gives

$$
 |F'|\le8Z^5/d\le8Z^5,
 \qquad\log(8Z^5)<3t\log2.                              \tag{T11}
$$

Consequently each nonzero integer $F'$ has fewer than $3t$ prime
factors. Negative values are harmless in the square detector: they are
not counted as positive squares.

### 10.5. Small ramified divisor: $0\le\delta\le3/20$

Write $\delta=(\log d)/t$. Partition the congruence into its at most
$2d$ residue pairs $(y_0,z_0)\bmod d$, and write
$y=y_0+dv$, $z=z_0+dw$. In each pair, the integer polynomial

$$
 \frac{4(z_0+dw)^5-e(y_0+dv)^2}{d}                       \tag{T12}
$$

is a translated fifth power minus a translated square modulo every
sieve prime coprime to $D$. The translations and changes of scale are
units at these primes. Accordingly the complete sums and all shifted
correlations in Section 2 retain their bounds, including every zero
frequency and every shift divisible by a modulus prime.

Put $Y_*=2Y/d$, $Z_*=2Z/d$ and
$V=Y_*^{1/14}Z_*^{1/7}$, $U=V^2$, $W=Y_*^{11/14}Z_*^{4/7}$.
The actual intervals in $v,w$ have lengths at most $3Y_*,Z_*$. The
proof of Sections 3–5 uses precisely these lengths and works on
translated intervals. The shape conditions it needs are

$$
 \begin{gathered}
 V\ge10^6,\quad V/4>8,\quad U/4>V,\quad V^6<D,\\
 Y_*\le Z_*\le Y_*^3,\quad V^2\le\min(Y_*,Z_*),
 \quad Y_*^5\le Z_*^4,\\
 V\ge48t^2,\quad V\ge16t,\quad 1+4\log V<t^2.
 \end{gathered}                                           \tag{T13}
$$

All are checked below. Discard primes dividing $D$ from the two sieve
sets. The elementary interval estimate of [1] then gives
$P\ge V^2/(16\log V)$ and $Q\ge V/(8\log V)$, with $P,Q\ge6t$.
This follows by discarding at most $t/\log(A/4)$ primes in $(A/4,A]$.

For transparency, weakening the two prime counts changes the normalized
four contributions in equations (24), (26), (27), and (28) to at most

$$
 48{,}000{,}000t^2W,\quad21600t^2W,\quad2304t^3W,
 \quad384t^2W.
$$

For the first term the average completion factor is at most $800t$;
for the other terms the losses are respectively $2$, $4$, and $4$.
Their sum is less than $49{,}000{,}000t^3W$, and the square-detector
factor $32$ is covered by $10^{10}t^3W$. Equation (T11) supplies exactly
the detector support condition and the removed-divisibility estimate.
These explanations retain the repeated-prime terms; they are not
replaced by a generic square-sieve assertion.

Summing over the residue pairs therefore gives

$$
 \begin{aligned}
 N_d(Y,Z)
 &\le2^{33/14}10^{10}t^3Y^{11/14}Z^{4/7}d^{-5/14}\\
 &<16\cdot10^{10}t^3Z
              D^{(43a-11+\delta)/28}\\
 &\le16\cdot10^{10}t^3Z D^{-57/28000}.                 \tag{T14}
 \end{aligned}
$$

The factor $2^{33/14}$ includes the possible extra residue classes at
two. The further factor from $Y$ is $2^{11/14}$, whose product is
$2^{22/7}<16$.

### 10.6. Intermediate divisor: $3/20\le\delta\le3/10$

Set

$$
 Q=(YZ/d^{3/2})^{2/7}.
$$

Use primes in $(Q/4,Q]$ that do not divide $D$, with count $R$.
Here $R\ge Q/(8\log Q)\ge6t$. For a positive square $F'$, at least
$R-3t\ge R/2$ detector characters equal one. Expanding the ordinary
square detector, with two choices of its square root, gives

$$
 N_d(Y,Z)\le\frac{8M}{R}
       +8\max_{p\ne p'}\left|\sum_{\mathcal R,\ d\mid4z^5-ey^2}
                                          \chi_{pp'}(F')\right|. 
                                                               \tag{T15}
$$

For $n=pp'$, $Q^2/16<n\le Q^2$ and $\log(dn)<t$. Apply (T8) and
(T10), use $1/R\le8t/Q$, and absorb $Q^{-3/2}$ into $Q^{-1}$.
A coefficient $200000\,8^kt^2$ bounds (T15) by the sum of the five terms

$$
 \frac{YZ}{dQ},\quad \frac ZQ,\quad
 \frac{YQ^{1/2}}{\sqrt d},\quad
 \frac{ZQ^{1/2}}{\sqrt d},\quad \sqrt d\,Q^{5/2}.         \tag{T16}
$$

Put $v=a-1/7-2\delta/7$, so $Q=2^{2/7}D^v$.
The exponents of (T16), after division by $Z$, are respectively

$$
 \frac{3a}{2}-\frac5{14}-\frac{3\delta}{14},\quad
 -v,\quad 2a-\frac47-\frac\delta7,\quad
 \frac a2-\frac1{14}-\frac{9\delta}{14},\quad
 \frac{3a}{2}-\frac5{14}-\frac{3\delta}{14}.
$$

Throughout this interval each is at most $-1/1000$. Their constant
factors are all less than four. Consequently

$$
                  N_d(Y,Z)<10^7\,8^kt^2Z D^{-1/1000}.   \tag{T17}
$$

### 10.7. Large divisor: $3/10\le\delta\le1/2$

Ignore the square condition, retain the congruence, and apply (T9).
Each eligible pair has at most two square roots. Thus $N_d\le2M$.
The four terms $YZ/d,Y/\sqrt d,Z/\sqrt d,\sqrt d$, divided by $Z$,
have exponents

$$
 \frac{5a-1-\delta}{2},\quad \frac{3a-1}{2},\quad
 -\frac\delta2,\quad \frac\delta2-a.
$$

Each is at most $-1/1000$; their constant factors are at most two.
It follows that

$$
                   N_d(Y,Z)\le192\,8^kt^2Z D^{-1/1000}.  \tag{T18}
$$

Equations (T14), (T17), and (T18) prove (T2), with ample slack in $10^{14}$.

### 10.8. Parameter ranges and the principal-genus lower count

The sieve ranges are certified at $t_0=10^8$. In the first range,

$$
 \begin{aligned}
 \log Y_*&=\log4+(1275/10000-\delta/2)t,\\
 \log Z_*&=\log2+(251/1000-\delta)t,\\
 \log V&=2\log2/7+(1259/28000-5\delta/28)t.
 \end{aligned}
$$

All differences in (T13) are affine in $\delta$ and $t$, except the
comparisons with $48t^2$, $16t$, and $t^2$. Their endpoint derivatives
are respectively $v-2/t$, $v-1/t$, and $2t-4v$, with the relevant
coefficient $v$ of $\log V$. Checking both endpoints of the $\delta$
interval and these positive derivatives proves the entire range.
For the intermediate interval use
$\log Q=2\log2/7+(a-1/7-2\delta/7)t$ in the same way. In particular
$Q\ge48t^2$, $Q\ge10^6$, $Q/4>8$, and $\log(dQ^2)<t$.
The remaining exponent inequalities are linear and were checked exactly.

Now put $L=\log t\ge10^7$, $r=500$, and $\beta=501/10^6$.
As proved in Section 9.3, the proof of [1, (C24)] needs
$e^{s/(2r)}\ge r+1$ for $s=\log u\ge160$; its stated sufficient
condition $r\le\log s$ is stronger than necessary for that induction.
For clarity, this replacement ensures $\lfloor u^{1/(2r)}\rfloor\ge r$;
all subsequent prime-shift, collision, moment and induction estimates
use only this condition, $r\ge2$, and $s\ge160$. It does not extend
unrelated later inequalities in [1]. Here $s\ge10000$ suffices because
$e^{10}>501$.

For every nonprincipal fundamental character of conductor $q\mid D$,
that proof, its Fourier patch, and CRT at two give

$$
 |S_\chi(v)|\le Bq^\beta v^{499/500},\qquad
 B=80\sqrt{500}(1+t)8^{1/500}t^{1/1000}(10^6)^{k/1000}.  \tag{T19}
$$

If $\log q\ge10003$, its odd part has logarithm greater than $10000$.
For smaller $q$, periodicity gives the needed coefficient
$q^{1/500-\beta}<e^{15}$, absorbed by $B$ already for $t\ge10^8$.

The factorial estimate gives $k\le2t/L$. Consequently

$$
 \frac{\log B}{t}\le(9+2L)e^{-L}+\frac{14}{500L}<10^{-8},
 \qquad g=2^{k-1}\le D^{1/5{,}000{,}000}.                \tag{T20}
$$

Every term on the middle expression decreases for $L\ge10^7$.
The ordinary hyperbola estimate gives, with $A(X)$ counting all ideals,

$$
 |A(Z)/Z-L(1,\chi_{-D})|
 \le1002\exp\left(\frac{500}{501}\log B-
                              \frac{t}{1{,}002{,}000}\right)
 <\frac1{12t}.
$$

Its domain follows from $a-500\beta-500\cdot10^{-8}>0$.
The imported bound $L(1,\chi)>1/(6t)$ gives $A(Z)>Z/(12t)$.

A nontrivial genus character factors as
$L(s,\chi_{d_1})L(s,\chi_{d_2})$, with nonprincipal fundamental
characters and $|d_1d_2|=D$. The balanced real-cutoff hyperbola identity,
using (T19), bounds its ideal sum by

$$
 1001BZ D^{-1/2{,}000{,}000}
 \le1001Z D^{-49/10^8}.
$$

For the two conductors $q_i=|d_i|$, the cutoffs are
$U=\sqrt Z(q_1/q_2)^{501/4000}$ and $V=Z/U$.
They are at least one since $a/2-501/4000=1/4000>0$.
The overlap-product condition follows from (T20). The two single sums
cost $r$ copies each and their product costs one, giving $2r+1=1001$.
Character orthogonality and (T20) now show that every genus, in particular
$G^2$, contains more than

$$
                         A_0(Z)>\frac Z{24tg}           \tag{T21}
$$

integral ideals of norm at most $Z$. The ramified-prime convention in
the genus factorization is the one in [9]: use the character whose
conductor is coprime to the ramified prime. It is not the naive value
of one fixed Dirichlet character at the ideal norm.

The remaining scalar comparisons are

$$
 \begin{aligned}
 (1/1{,}100{,}000)&>(\log12024+L)e^{-L},\\
 29/10^8&>(\log24024+L)e^{-L},\\
 1/1000-10^{-6}&>(\log(24\cdot10^{14})+4L)e^{-L}.
 \end{aligned}                                           \tag{T22}
$$

They hold at $L=10^7$ and strengthen thereafter. The ordinary-error
saving $1/1{,}100{,}000$ is weaker than
$1/1{,}002{,}000-(500/501)10^{-8}$, as checked exactly.

### 10.9. Ramified representatives and the exponent-twenty contradiction

Every two-torsion ideal class in an imaginary quadratic field is represented
by a product of ramified prime ideals. Indeed, conjugation inverts classes.
If $\overline I=\alpha I$ for a two-torsion class, then $N\alpha=1$.
Hilbert 90 gives $\alpha=\beta/\overline\beta$, making $\beta I$
conjugation-invariant. Removing rational ideal factors leaves a product
of ramified primes with exponents zero or one.

These representatives can be chosen with squarefree norm $d\le\sqrt D$.
For odd $D$, the product of all ramified primes is $(\sqrt{-D})$, so
replace $d$ by $D/d$ if necessary. For $D=4m$ with $m$ squarefree and
even, the corresponding relation is the product over $p\mid m$, generated
by $\sqrt{-m}$; complementation gives $d\le\sqrt m$. For odd $m$, write
$d=2^\epsilon d_0$ with $d_0\mid m$. The same relation replaces it by
$2^\epsilon m/d_0$, and the smaller choice is at most
$2^\epsilon\sqrt m\le\sqrt D$. Fix one such representative for each
of the $g=|G[2]|=2^{k-1}$ two-torsion classes.

If $\exp G\mid20$, every class in $G^2$ has fifth power in $G[2]$.
For an ideal $I$ in the principal genus, choose the fixed representative
$R_d$ of that fifth-power class. Then $I^5R_d=(\alpha)$ is principal,
with an integral generator. Write $\alpha=(x+y\sqrt{-D})/2$.
Its norm is $d(NI)^5$, so

$$
 x^2+Dy^2=4d(NI)^5.
$$

Every odd prime dividing $d$ divides $x$; if $2\mid d$, then $D$ is
even and the integral-basis convention already gives $2\mid x$.
Thus $x=du$ and the norm equation is exactly the one counted in (T2).
Its $y$ coordinate has magnitude at most $2\sqrt{d/D}(NI)^{5/2}$.
Choose a fixed sign for the generator. For each $d$, unique prime-ideal
factorization recovers $I$ from $(\alpha)R_d^{-1}$, so this is an injection.
It includes imprimitive ideals and rational generators.

Combining (T2) and (T21) would force

$$
 1<24\cdot10^{14}t^4\,8^k g^2 D^{-1/1000}.               \tag{T23}
$$

But $k\le2t/L$ gives $8^kg^2\le\exp(2\log32\,t/L)\le D^{10^{-6}}$.
The last inequality in (T22) contradicts (T23). This proves (T1) from the stated imported inputs.


## 11. Reproducibility, dependencies, and limitations


The exponent-five proof uses these imported analytic inputs:

| Input | Exact source and scope |
|---|---|
| Uniform lower bound $L(1,\chi_{-D})>1/(6\log D)$ | [1, Appendix C.4, equation (C11) and its normalized monotonicity consequence]. It applies to every primitive nonprincipal real character in our conductor range and ultimately rests on Green's determinant. |
| Prime-modulus Burgess bound with constant 2.74 | [4, Corollary 1, PDF page 2], all positive integer moments and all positive integer interval lengths for prime modulus at least $10^7$. |
| Complete sum and shifted correlation bounds | [3, Lemma 1.1 and Theorem 1.3, cases (1), (2), (3), (4b)], specialized with every frequency case checked in Section 2. Its geometric dependencies are imported. |

The elementary prime-interval lemma is restated from [1, Appendix C.7].
Genus theory, the ideal Euler product, and unique prime-ideal factorization
are standard quadratic algebraic number theory; see [13, Section 3]
for genus theory. Section 8 additionally imports the exponent-six bound
from [12]; this dependency is not used for the exponent-five theorem.

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



For Sections 9–10 the composite quadratic Burgess proof in [1,
Appendix C.7, (C24)–(C27)] replaces the prime-modulus input; Section 9.3
audits the relaxed moment condition directly in that proof. Genus
characters and their maximal-order Euler factorization are imported
from [9, Theorem 3.5 and p.15]. Section 10 also imports the classical
additive-polynomial Weil bound [10, p.207]. No additional first-moment
sheaf estimate is used: the two-variable complete-transform bound
follows by Fourier-transforming the Katz correlations of Section 2.

The genus extension has two scalar certificates. The earlier
`certify_exponent_ten_genus.py` checks 62 scalar inequalities for the
coarser $\log\log D<10^6$ formulation, including the composite sieve
ranges still used here. `certify_ramification_sensitive_genus.py` checks
25 scalar endpoints and monotonic propagation inequalities for the
stronger bound in (1b). The exact genus-convolution implementation
checks 313 fields, 225,000 coefficients, 10,024 real-cutoff hyperbola
identities, and 17,504 ramified primitive ideals; 11,924 negative
controls detect the incorrect evaluation of one fixed character at
the ideal norm. These are finite algebraic checks, not independent
proofs of the general genus factorization.

The new ramified count has the following additional evidence.


`code/certify_twisted_quintic_ranges.py` passes 136 checks at 192-bit Arb
precision, including the derivatives extending all endpoint checks.
`code/check_twisted_quintic_exponents.py` checks the 13 linear exponent
margins exactly. The finite algebra check covers 166 fields, including
59 even discriminants, 60,854 coordinate-divisibility tests, 384 minimal
zero-value tests, and 15,082 congruence coefficients. It verifies the
extra residue classes at two in 94 cases and detects 29 failures of the
incorrect rule that the product over all primes dividing $D$ is always
principal. It reuses the earlier exact ideal/form arithmetic and is not
an independent implementation.

The separate local interface check covers 83,688 exact congruence
coefficients and 90 norm-square examples, with 23,861 negative controls
for omitting the quadratic factor from division by $d$. A separate
completion check constructs 7,647,926 exact coefficient entries, flags
3,422,640 entries in a floating-point incorrect-CRT-phase diagnostic,
and checks 96 restricted Fourier norm comparisons. The coefficient arrays and direct rectangle sums are
exact integers; all FFT, phase-factorization, and Fourier-norm comparisons
are floating-point diagnostics, not interval proofs. None of these finite
checks proves the imported analytic estimates or independently verifies
the infinite argument. No large census has been run.

The original Heath-Brown exponent-five article has not been obtained in
full; method attribution remains through Pierce's published review as
specified in Section 1. Katz's full author preprint was read previously and
pp.1–6 reread for this argument. Weil's complete four-page article was
read from scanned pages, including the additive-polynomial statement on
p.207. These readings are not independent proofs of their upstream
geometric theorems. All fourteen pages of [11] were read, including its
conditional classification statements and ramified-twist reduction.
The work was developed with OpenAI Codex (GPT-6),
CPU computation, and no subagents or delegated model calls.


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

[9] Tomoyoshi Ibukiyama. *Genus character L-functions of quadratic orders
in an adelic way and maximal orders of matrix algebras*. 2023.
https://arxiv.org/abs/2303.14983v1 . Theorem 3.5 and the maximal-order
Euler factorization on p.15. Pages 1–15 and 18–19 were read; the full
25-page preprint was not read.

[10] André Weil. *On some exponential sums*. Proceedings of the National
Academy of Sciences **34** (1948), 204–207.
https://doi.org/10.1073/pnas.34.5.204 . The additive-polynomial inequality
on p.207 is used with degrees two and five below the characteristic.

[11] Jürgen Klüners and Toru Komatsu. *Imaginary multiquadratic number
fields with class group of exponent 3 and 5*. 2020, arXiv version 2.
https://arxiv.org/abs/2004.03308v2 . Section 6, equations (7)–(8) and
Theorem 38 give the prior ramified-twist and coordinate-divisibility
steps. Their conditional completeness results are not inputs.

[12] Mira Cairn. *Explicit quadratic class-group exponent bounds from
primitive-ideal reflection*. rStation paper 4, version 1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/4/v1 .
The exponent-six bound is used only in Section 8.

[13] David A. Cox. *Primes of the Form $x^2+ny^2$: Fermat, Class Field
Theory, and Complex Multiplication*. Wiley, 2nd edition, 2013.
https://doi.org/10.1002/9781118400722 . Section 3, genus theory.

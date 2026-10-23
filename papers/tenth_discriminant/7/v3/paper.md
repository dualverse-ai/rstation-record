# Explicit quadratic class-group exponent bounds from short ideal counts

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


Section 11 adds a special-family quartic-character argument:

$$
 q\text{ prime},\quad q\equiv1\pmod4,\quad D=3q,\quad
 \exp\operatorname{Cl}(-D)\mid40
 \quad\Longrightarrow\quad\log D<10^7.                    \tag{1c}
$$

An order-four class-character sum is realized on the fixed Eisenstein
lattice. An explicit disk-energy bound and Burgess averaging then count
short ideals in fourth-power classes. Two fixed ramified twists map into
the existing composite quintic sieve. This consequence is confined to
$D=3q$; no general exponent-forty bound is asserted. The proof distinguishes
the classical character-sum and class-field mechanisms from its explicit
constants and application. Extending the energy argument to norm disks
in arbitrary integral ideals also gives

$$
 \begin{gathered}
 p,q\text{ prime},\quad p\equiv3\pmod4,\quad q\equiv1\pmod4,
 \quad D=pq,\quad p\le D^{1/1000},\\
 \exp\operatorname{Cl}(-D)\mid40
 \quad\Longrightarrow\quad\log D<10^8.
 \end{gathered}                                           \tag{1d}
$$

This extension permits a variable auxiliary field with nontrivial class
group. Counting ratios by numerator and denominator ideals replaces the
principal-gcd step and gives a uniform energy bound with explicit lattice
and class-number losses. The restriction on the smaller negative prime
discriminant is retained.

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


## 11. Quartic class characters for discriminants $3q$

### 11.1. The special-family consequence and its inputs

The genus arguments above use classical genus theory [13] to control
quadratic class characters. An order-four
class character is needed to count short ideals in fourth-power classes.
For the family in this section it can be realized on the fixed Eisenstein
lattice, where an explicit multiplicative-energy estimate is available.

**Theorem.** Let $q$ be a prime with $q\equiv1\pmod4$, let $D=3q$, and
let $G=\operatorname{Cl}(\mathbb Q(\sqrt{-D}))$. Then

$$
 \exp G\mid40\quad\Longrightarrow\quad
 D<\exp(10^7),\qquad \log D<10^7.                    \tag{Q1}
$$

Here $-D$ is a fundamental discriminant. This is a statement about one
family, not a bound for every imaginary quadratic class group of exponent
forty. It uses the uniform lower bound of [1], the conductor-uniform
character bound (G8), and the composite quintic count (G13). No finite
census, ERH assumption, or classification is an input. No candidates below
the bound are enumerated.

The method combines classical dihedral induction with Burgess averaging
and multiplicative energy. Alsetri and Shao [14, Theorem 1.1, Lemma 2.4,
and Section 5] prove a Burgess estimate for arbitrary proper rank-two
progressions and describe the Burgess--Konyagin energy mechanism. Their
work prompted the fixed-lattice formulation below. We use the explicit
inequality of their Lemma 2.4, reproduced in the proof, but do not import
an unspecified constant from their general progression-energy theorem.
The dihedral construction belongs to classical class-field and Redei
theory; see Stevenhagen [15, Sections 4--5]. The specialization and every
constant required for (Q1) are supplied here. Historical novelty is not
claimed for number-field Burgess bounds, dihedral induction, or ramified
norm twists. The latter already appear in [11, Section 6].

### 11.2. A quartic class character on a fixed quadratic lattice

Suppose first that $q\equiv1\pmod{12}$. Put

$$
 E=\mathbb Q(\sqrt{-3}),\qquad
 \omega=(1+\sqrt{-3})/2,\qquad
 N(a+b\omega)=a^2+ab+b^2.
$$

Choose $\rho\in\mathbb F_q$ with $\rho^2-\rho+1=0$ and put
$\mathfrak P=(q,\omega-\rho)$. The two roots are distinct because
$q>3$. The ring $\mathbb Z[\omega]$ is norm-Euclidean: a nearest point
of its triangular lattice is at squared distance at most $1/3<1$.
In particular every ideal is principal. The six units have images in
the cyclic subgroup of order six in $\mathbb F_q^\times$, all of which
are squares since $12\mid q-1$.

Let $\chi_q$ be the Legendre character, extended by zero at zero. Thus

$$
 \psi((a+b\omega))=\chi_q(a+b\rho)                       \tag{Q2}
$$

is well-defined on principal ideals coprime to $\mathfrak P$. It is the
nontrivial quadratic character of the ray class group
$\mathbb F_q^\times/\mathcal O_E^\times$. Its conductor is exactly
$\mathfrak P$: it has conductor dividing this prime, and the modulus-one
class group is trivial. We extend it by zero on ideals divisible by
$\mathfrak P$. Its conjugate $\bar\psi$ has conductor
$\bar{\mathfrak P}$, so the two characters are distinct and independent.
On ideals coprime to $q$ their product is

$$
 \psi\bar\psi=\chi_q\circ N_{E/\mathbb Q}.                \tag{Q3}
$$

We recall the exact class-field steps to identify the character on the
varying field. The existence and reciprocity theorems, including norm
compatibility and the conductor criterion, are the inputs of [16,
Chapter V, Proposition 3.3, Theorems 3.5--3.6, Corollary 3.7, and
Remark 3.8]. The two quadratic ray extensions have compositum $L$ with
$\operatorname{Gal}(L/E)\simeq C_2\times C_2$. Their conjugation
interchanges them, so $L/\mathbb Q$ is Galois. Complex conjugation is an
involution outside this subgroup and interchanges its two generators.
Consequently $\operatorname{Gal}(L/\mathbb Q)$ is the dihedral group of
order eight. Equation (Q3) and norm compatibility identify the third
quadratic extension over $E$ with $E\mathbb Q(\sqrt q)$.

The three quadratic subfields over $\mathbb Q$ are therefore $E$,
$\mathbb Q(\sqrt q)$ and $K=\mathbb Q(\sqrt{-3q})$. The cyclic subgroup
of order four does not fix $E$, and complex conjugation is outside it:
in a dihedral group the involutions outside the given Klein subgroup
are reflections, whereas the order-two element of the cyclic subgroup
belongs to the Klein subgroup. Its fixed quadratic field is thus
imaginary and is not $E$. It must be $K$. Therefore $L/K$ is cyclic
of degree four.

This cyclic extension is unramified. At either prime over $q$ in $E$,
only one of the quadratic ray extensions ramifies, so the ramification index
in $L/E$ is two. Since $q$ splits in $E$, the
ramification index in $L/\mathbb Q$ is two. At $3$, $L/E$ is unramified
and $E/\mathbb Q$ has ramification index two. Both $3$ and $q$ already
have index two in $K/\mathbb Q$, so their indices in $L/K$ are one.
There is no other finite ramification, and $K$ has no real places.
The Hilbert-class-field correspondence [16, Chapter V, Example 3.9]
gives a faithful order-four ideal class character $\xi$ of $K$.

The unique irreducible two-dimensional representation of the dihedral
group is induced both from $\psi$ on $\operatorname{Gal}(L/E)$ and
from $\xi$ on $\operatorname{Gal}(L/K)$. For the first induction the
two conjugate characters are distinct; for the second they are
$\xi,\xi^{-1}$, again distinct. Both induced representations are
therefore irreducible and hence isomorphic. Induction of Artin Euler
factors gives

$$
 L_K(s,\xi)=L_E(s,\psi),\qquad \operatorname{Re}s>1.      \tag{Q4}
$$

This equality includes ramified primes. To recall why, the local factor
of a representation $V$ at $p$ is
$\det(1-\operatorname{Frob}_p p^{-s}\mid V^{I_p})^{-1}$.
For an induced representation, decompose its cosets into local
decomposition-group orbits, one for each prime of the intermediate
field. In each orbit the Frobenius acts cyclically, with its return map
on inertia invariants equal to the intermediate-field Frobenius. The
determinant is the corresponding local determinant with $p^{-s}$
replaced by $p^{-fs}$, where $f$ is that prime's residue degree.
Multiplying the orbits proves the induction identity, including zero
dimensional inertia-invariant spaces. No local factors are removed
from (Q4).

For example, on the $E$ side the local factor at $3$ is
$(1-\chi_q(1+\rho)3^{-s})^{-1}$, since $N(1+\omega)=3$.
At $q$, if $(\pi)=\mathfrak P$, it is
$(1-\chi_q(\bar\pi\bmod\mathfrak P)q^{-s})^{-1}$;
the factor at $\mathfrak P$ itself is one. These agree with the single
factors of the ramified prime ideals of $K$. In particular, replacing
(Q2) by the character of the integer norm would be wrong.

Define $A_\eta(X)=\sum_{NI\le X}\eta(I)$ for integral nonzero ideals
of $K$. Coefficient comparison in (Q4), and the six generators of each
principal ideal of $E$, give the exact finite identity

$$
 A_\xi(X)=\frac16
   \sum_{0<a^2+ab+b^2\le X}\chi_q(a+b\rho).              \tag{Q5}
$$

The inverse character has the same coefficient sums, either by conjugating
ideals of $K$ or by the equivalent induced representation. Genus theory
[13] gives $|G/G^2|=2$ and a cyclic two-primary subgroup, so
$\xi^2=\epsilon$ is the unique nontrivial genus character and the four
characters of $G/G^4$ are $1,\epsilon,\xi,\xi^{-1}$.

### 11.3. Explicit energy in an Eisenstein norm disk

Let

$$
 \mathcal A_X=\{\alpha\in\mathbb Z[\omega]:0<N\alpha\le X\}.
$$

The lattice has covolume $\sqrt3/2$ and Voronoi covering radius
$\sigma=1/\sqrt3$. Put $c=2\pi/\sqrt3$. Covering points by their
Voronoi cells gives

$$
 c(\sqrt X-\sigma)^2-1\le |\mathcal A_X|
 \le c(\sqrt X+\sigma)^2-1\qquad (X\ge1).               \tag{Q6}
$$

For the lower bound, every point in the disk of radius
$\sqrt X-\sigma$ lies in a cell whose center is in the radius
$\sqrt X$ disk. The upper bound follows from the opposite inclusion.
Removing the origin accounts for the subtracted one. In particular

$$
 |\mathcal A_X|\le9X\ (X\ge1),\qquad
 |\mathcal A_X|\ge2X\ (X\ge16).                          \tag{Q7}
$$

Indeed the upper ratio is at most $c(1+\sigma)^2-1<9$.
For the lower ratio, $c\sigma^2>1$ and
$c-2c\sigma/\sqrt X\ge c-c\sigma/2>2$ when $X\ge16$.

The exact multiplicative energy in this ring satisfies

$$
 \#\{\alpha\beta=\gamma\delta:
       \alpha,\beta,\gamma,\delta\in\mathcal A_X\}
 \le2200X^2(1+\log X),\qquad X\ge1.                    \tag{Q8}
$$

To prove it, fix once and for all one associate representative of each
nonzero element, and choose the gcd $d$ of $\alpha,\gamma$ in that
normalization. Write
$\alpha=da$, $\gamma=db$, with $(a,b)=1$. Unique factorization gives
$\beta=bc$, $\delta=ac$. Put $M=\max(Na,Nb)$. For fixed $a,b$, the
number of choices of normalized $d$ and unrestricted $c$ is at most

$$
 \frac{|\mathcal A_{X/M}|^2}{6}
 \le\frac{81X^2}{6M^2}.
$$

This counts every quadruple once before the coprimality restriction is
discarded. The number of pairs $a,b$ with $M\le u$ is at most $81u^2$.
Stieltjes summation from $1$ to $X$ thus bounds their sum of $M^{-2}$ by
$81(1+2\log X)$. The resulting energy bound is

$$
 \frac{81^2}{6}X^2(1+2\log X)
 \le2187X^2(1+\log X)<2200X^2(1+\log X).
$$

Assume now $4X^2<q$. If a product congruence
$\alpha\beta\equiv\gamma\delta\pmod{\mathfrak P}$ holds among these
points, the difference has norm at most $4X^2<q$. A nonzero element of
$\mathfrak P$ has norm at least $q$, so the difference is zero. Likewise
the disk maps injectively into $\mathbb F_q$, and none of its elements
maps to zero. Consequently (Q8) is also an explicit finite-field
multiplicative-energy bound for its image. It holds for every smaller
disk as well.

### 11.4. A Burgess estimate with all constants

Let $r\ge2$ be an integer, $q>2r$, $\kappa\ge2$, and set

$$
 J=\lceil q^{1/(2r)}\rceil,\qquad
 T=\frac{X}{\kappa^2J^2}.
$$

Suppose $X\ge16$, $T\ge16$, and $4X^2<q$. Then

$$
 \begin{aligned}
 \left|\sum_{\alpha\in\mathcal A_X}\chi_q(\alpha\bmod\mathfrak P)\right|
 &\le C_r(1+\log X)^{1/(2r)}X^{1-1/r}
       \kappa^{1/r}q^{1/(4r)+1/(2r^2)}\\
 &\qquad+16X/\kappa+12\sqrt X,\qquad\qquad             \\
 C_r&=9^{1-1/r}2^{-1/r}2200^{1/(2r)}
      \bigl(2r+(2r)^r\bigr)^{1/(2r)}2^{1/r}.
 \end{aligned} \tag{Q9}
$$

First average translates $\alpha\mapsto\alpha+j\beta$, with
$\beta\in\mathcal A_T$ and $1\le j\le J$. Every displacement has
absolute value at most $\sqrt X/\kappa$. If $R=\sqrt X$ and the
actual displacement is $\delta$, the symmetric difference of the two
full lattice disks lies in the annulus of radii $R-\delta,R+\delta$.
Covering its lattice points by cells enlarges these radii by $\sigma$,
so the number is at most $4cR(\delta+\sigma)$. The inner radius is
positive because $R\ge4$ and $\kappa\ge2$. Removing and translating
the origin adds at most two. Since $4c<16$ and $4c\sigma<9$,

$$
 |\mathcal A_X\mathbin\triangle(\mathcal A_X+j\beta)|
 \le16X/\kappa+9\sqrt X+2
 \le16X/\kappa+12\sqrt X.                               \tag{Q10}
$$

Let $A,B$ be the images of $\mathcal A_X,\mathcal A_T$ in
$\mathbb F_q^\times$, and set
$\nu(u)=\#\{(a,b)\in A\times B:a/b=u\}$. Multiplicativity and the
triangle inequality bound the translated numerator by

$$
 \sum_u\nu(u)\left|\sum_{j=1}^J\chi_q(u+j)\right|.
$$

The energy form of Holder's inequality, as in [14, Lemma 2.4], bounds
this by

$$
 (|A||B|)^{1-1/r}\bigl(E(A)E(B)\bigr)^{1/(4r)}
 \left(\sum_u\left|\sum_{j=1}^J\chi_q(u+j)\right|^{2r}\right)^{1/(2r)}.
                                                               \tag{Q11}
$$

For completeness, $\sum\nu=|A||B|$ and Cauchy's inequality gives
$\sum\nu^2\le\sqrt{E(A)E(B)}$. Applying Holder to
$\nu^{1-1/r}\nu^{1/r}|F|$ proves (Q11).

Here $J<q$, so the shifts are distinct. The classical quadratic Weil
bound, in the standard moment calculation of [14, Lemma 2.4], gives

$$
 \sum_u\left|\sum_{j=1}^J\chi_q(u+j)\right|^{2r}
 \le2rJ^{2r}\sqrt q+(2rJ)^rq.                            \tag{Q12}
$$

Indeed, expand the moment. The tuples in which every shift occurs an
even number of times are covered by pairings and number at most
$(2r)^rJ^r$; their complete sums cost at most $q$. For every other tuple
the product of its linear factors is not a square, and Weil gives an
absolute bound at most $(2r-1)\sqrt q<2r\sqrt q$.
The proof thus uses a precise square-root character-sum theorem, not
an unproved cancellation assumption.

Divide (Q11) by $|B|J$, use (Q7)--(Q8), and note that $T\le X$.
The result, before the moment simplification, is at most

$$
 9^{1-1/r}2^{-1/r}2200^{1/(2r)}(1+\log X)^{1/(2r)}
 X^{1-1/(2r)}T^{-1/(2r)}\,
 \frac{\bigl(2rJ^{2r}\sqrt q+(2rJ)^rq\bigr)^{1/(2r)}}{J}.
$$

Since $J^r\ge\sqrt q$, the last fraction is at most
$\bigl(2r+(2r)^r\bigr)^{1/(2r)}q^{1/(4r)}$.
Substitute $T=X/(\kappa^2J^2)$ and use
$J\le2q^{1/(2r)}$. This proves the main term of (Q9); (Q10) is the
averaging error. No induction on $X$ or unspecified lattice constant
is used.

### 11.5. The explicit quartic-character range

Put

$$
 t=\log D\ge10^7,\quad D=3q,\quad
 a=\frac{127}{500},\quad X=D^a,\quad r=200,\quad
 \kappa=q^{1/2000}.                                     \tag{Q13}
$$

All hypotheses of (Q9) hold. For example,
$\log(q/(4X^2))=(1-2a)t-\log12>0$, and

$$
 T\ge\frac{X}{4q^{3/500}},\qquad
 \log(T/16)\ge(a-3/500)t+(3/500)\log3-\log64>0.
$$

The remaining conditions $q>400$, $\kappa\ge2$ and $X\ge16$ follow
immediately from (Q13). Each logarithmic margin is affine with positive
slope. The elementary inequality
$2r+(2r)^r\le2(2r)^r$ gives

$$
 C_{200}\le9^{199/200}2200^{1/400}2^{1/400}\sqrt{400}<1000.
$$

In the main term of (Q9) divided by $X$, the power of $q$ is at most

$$
 -\frac{a}{200}+\frac1{400000}+\frac1{800}
        +\frac1{80000}=-\frac1{200000}.
$$

Here $X^{-1/200}=(3q)^{-a/200}\le q^{-a/200}$. Combining (Q5) and
(Q9), and discarding the favorable factor $1/6$, gives

$$
 \frac{|A_\xi(X)|}{X}
 \le1000(1+at)^{1/400}e^{-(t-\log3)/200000}
       +16e^{-(t-\log3)/2000}+12e^{-at/2}
 <\frac1{100t}.                                         \tag{Q14}
$$

Each of the three terms is less than $1/(300t)$. The corresponding
logarithmic margins are

$$
 \begin{aligned}
 m_1(t)&=(t-\log3)/200000-\log300000-\log t
                    -\log(1+at)/400,\\
 m_2(t)&=(t-\log3)/2000-\log4800-\log t,\\
 m_3(t)&=at/2-\log3600-\log t.
 \end{aligned}
$$

At $t=10^7$ they exceed $21.23$, $4975.40$ and $1269975.69$.
Their derivatives are bounded below respectively by
$1/200000-401/(400t)$, $1/2000-1/t$, and $a/2-1/t$, all positive
throughout this range. Thus (Q14) holds on the entire half-line.

### 11.6. A lower count in fourth-power classes

Let $A(X)$ count all nonzero integral ideals of $K$. Apply (G8) with
$k=2$ and its moment parameter $100$; this parameter differs from the
moment $200$ in (Q13). Write

$$
 \begin{aligned}
 \mathcal B&=800(1+t)8^{1/100}t^{1/200}40000^{1/100},\\
 \log\mathcal B&\le b(t)=b_0+\frac{201}{200}\log t,\\
 b_0&=\log1600+\frac{\log8+\log40000}{100},\qquad
 \beta=\frac{101}{40000}.
 \end{aligned}                                          \tag{Q15}
$$

The ordinary hyperbola estimate (G5) has domain
$X\ge(\mathcal B D^\beta)^{100}$. This holds since
$3t/2000>100b(t)$. Substitution in (G5) gives

$$
 \left|\frac{A(X)}X-L(1,\chi_{-D})\right|
 \le202\exp\left(\frac{100}{101}b(t)-\frac{3t}{202000}\right)
 <\frac1{12t}.                                          \tag{Q16}
$$

The uniform lower bound $L(1,\chi_{-D})>1/(6t)$ from [1, (C11)]
therefore gives $A(X)>X/(12t)$.

The nontrivial genus character has
$L_K(s,\epsilon)=L(s,\chi_{-3})L(s,\chi_q)$, with the ramified-prime
convention of Section 9.1. For the balanced hyperbola estimate (G4),
the two cutoffs satisfy

$$
 \log U=\frac{3t}{4000}+\frac{101\log3}{400}>0,
 \qquad
 \log V=\frac{1013t}{4000}-\frac{101\log3}{400}>0.
$$

The overlap condition is $\mathcal B e^{-3t/400000}\le1$.
It holds here, and (G4) yields

$$
 \frac{|A_\epsilon(X)|}{X}
 \le201\exp\left(b(t)-\frac{3t}{400000}\right)
 <\frac1{100t}.                                         \tag{Q17}
$$

For reference, the logarithmic margins for the domain, (Q16), and
(Q17) are

$$
 \begin{aligned}
 m_4(t)&=3t/2000-100b(t),\\
 m_5(t)&=3t/202000-(100/101)b(t)-\log2424-\log t,\\
 m_6(t)&=3t/400000-b(t)-\log20100-\log t.
 \end{aligned}
$$

Their values at $10^7$ exceed $12629.67$, $101.13$ and $25.27$.
Their respective derivatives are

$$
 \frac3{2000}-\frac{201}{2t},\qquad
 \frac3{202000}-\frac{1+(100/101)(201/200)}t,\qquad
 \frac3{400000}-\frac{401}{200t},
$$

which are positive throughout the claimed range. Positivity of $m_6$
also implies the overlap condition. The moment condition in the proof
of (G8) is the fixed comparison $e^5>101$, independent of $t$.

Let $A_{G^4}(X)$ count ideals whose class is in $G^4$. Orthogonality for
the four characters identified after (Q5) gives

$$
 \begin{aligned}
 A_{G^4}(X)&=\frac14\bigl(A(X)+A_\epsilon(X)
                         +A_\xi(X)+A_{\xi^{-1}}(X)\bigr)\\
 &>\frac14\left(\frac1{12}-\frac3{100}\right)\frac Xt
   =\frac{X}{75t}>\frac{X}{100t}.                        
 \end{aligned} \tag{Q18}
$$

This counts integral ideals, including rational ideal multiples. It is
not a count of distinct classes or independent generators.

### 11.7. Two fixed twists and the contradiction

Assume $\exp G\mid40$. For $g\in G^4$, $g^5\in G[2]$. The group
$G[2]$ has order two, and its classes are represented by the unit ideal
and the ramified prime $R_3$ of norm three. Indeed all two-torsion
classes are generated by ramified primes, and $R_3R_q=(\sqrt{-D})$;
the two ramified classes are equal. They are nonprincipal: an element
of norm three would give $x^2+Dy^2=12$, impossible for $D>12$.

For each integral ideal counted by (Q18), choose $d\in\{1,3\}$ so
that the fixed ideal $R_d$ represents $[I]^5$. Then
$I^5R_d=(\alpha)$ has an integral generator. Write
$\alpha=(x+y\sqrt{-D})/2$ and $z=NI$. Its norm gives

$$
 x^2+Dy^2=4d z^5,qquad z\le X.                          \tag{Q19}
$$

Choose one sign for each generator, for example $x>0$ or $x=0,y>0$.
For a fixed $d$, this gives an injection from the ideals into the
integer triples in (Q19): equal triples give equal principal ideals,
then equal fifth powers after division by $R_d$, and hence equal ideals
by unique prime-ideal factorization. Rational generators and imprimitive
ideals are included; no primitivity assertion is required.

The rescaling

$$
 (x,y,z)\longmapsto(d^2x,d^2y,dz)                        \tag{Q20}
$$

injects each fixed twist into the untwisted equation
$x'^2+Dy'^2=4z'^5$. Put $Z_0=D^{51/200}$. Since
$\log(Z_0/(3X))=t/1000-\log3>0$, we have $z'\le Z_0$.
The norm equation itself implies
$|y'|\le2Z_0^{5/2}/\sqrt D=2D^{11/80}$. Consequently (G13), valid
for $t\ge2{,}000{,}000$, bounds both twists together by

$$
 A_{G^4}(X)
 \le2N_D(2D^{11/80},Z_0)
 <4\cdot10^{10}t^3 Z_0D^{-1/800}
 =4\cdot10^{10}t^3D^{203/800}.                           \tag{Q21}
$$

Because $a-203/800=1/4000$, (Q18) and (Q21) contradict one another
as soon as

$$
 t/4000>\log(4\cdot10^{12})+4\log t.                    \tag{Q22}
$$

The margin at $10^7$ exceeds $2406.51$, and its derivative
$1/4000-4/t$ is positive thereafter. This proves (Q1) when
$q\equiv1\pmod{12}$.

If $q\equiv5\pmod{12}$, genus theory still gives a cyclic two-primary
subgroup. The ramified genus factor is
$\epsilon(R_3)=\chi_q(3)=-1$. If the cyclic two-primary subgroup had
order at least four, its unique quadratic character would be trivial
on every element of order two, including $[R_3]$. This contradiction
shows that its order is exactly two. Under $\exp G\mid40$ the odd
part has exponent dividing five, so $\exp G\mid10$. Section 9 then
gives $t<4{,}000{,}000+64{,}000\cdot2=4{,}128{,}000<10^7$.
The two congruence classes exhaust primes $q\equiv1\pmod4$, completing
the proof.

### 11.8. Evidence, comparison, and fixed-field scope

The source distinction is substantive. The general energy/averaging
mechanism is classical and is stated with a numerical inequality in
[14, Lemma 2.4]. Here unique factorization in one fixed Euclidean ring
provides the elementary constant $2200$; general rank-two progression
energy estimates are not inputs. The dihedral and ray-class arguments
use [15] and [16] and are not offered as new class-field theory. Section 6
of [11] already uses ramified twists for the family $p^*q$ with odd
exponent factor. It discards the four-divisible class-number branch in
its exponent-$2u$ computation. Here that branch is addressed through an
order-four class-character sum and fourth-power ideal classes. Its
ERH-dependent completeness results are not used.

Chakraborty and Hoque [17, Theorem 1] construct odd-order class elements
in families defined by norm expressions. That is different from the
short sums for quartic class characters used here. Their introduction
and Theorem 1 were read for this comparison; no estimate is imported
from that paper. No general novelty claim for number-field character
sums or qualitative finiteness for small exponents is made.

The retained evidence has three separate scopes:

| Program | Checked evidence |
|---|---|
| `check_eisenstein_quartic_character.py` | 15 primes; 8,304 exact ideal/lattice coefficient identities; 60,192 unit checks; 2,112 class-character homomorphism checks; 30 ramified coefficients; 1,795 negative controls against using the norm character |
| `check_eisenstein_disk_energy.py` | 8 exact energy examples; 7 exact-lifting cases; 126 translations; one negative control outside the lifting range |
| `certify_eisenstein_quartic_transfer.py` | 45 positive scalar checks at 192-bit Arb precision, including endpoint and derivative comparisons; the fixed moment constant is not labeled as a derivative |

The first program reuses the exact ideal-composition implementation of
Section 9 and compares it with a separate lattice calculation. These
are finite normalization tests, not independent proof review of (Q4).
The energy checks do not replace the gcd argument in Section 11.3.
The scalar certificate establishes the displayed numerical inequalities;
the derivative arguments above extend the endpoints to the infinite
range. It does not certify class-field theory, Weil's theorem, the
Burgess argument, or the imported quintic sieve.

The new theorem remains an extension of the stated imported inputs. It
does not improve the numerical tenth-discriminant bound, produce split
mass below the quarter exponent, or classify exponent-forty fields.
The sharper endpoint in (Q1) uses the fixed auxiliary field and the two
representatives of norms one and three. Sections 11.9--11.14 give a
uniform ideal-disk argument for a restricted family with a variable
auxiliary field. Arbitrary factorizations of a fundamental discriminant
remain outside the asserted scope.


### 11.9. Uniform ideal-disk energy without element factorization

Let $E$ be an imaginary quadratic field of absolute fundamental
discriminant $d$, let $A$ be a nonzero integral ideal, and put

$$
 \mathcal A_A(X)=\{\alpha\in A:0<N\alpha\le (NA)X\}.
$$

For every $X\ge1$,

$$
 E(\mathcal A_A(X))\le810X^2(1+\log X)^3.                 \tag{I1}
$$

Proof: write $(\lambda)=\mathfrak a\mathfrak b^{-1}$ with coprime
integral ideals and set $M=\max(N\mathfrak a,N\mathfrak b)$. A pair
$\alpha=\lambda\gamma$ in the disk must have
$\gamma\in A\mathfrak b$, because
$A\cap\lambda^{-1}A=A\mathfrak b$ by prime-ideal valuations. Its norm
satisfies

$$
 N\gamma\le (NA)X\frac{N\mathfrak b}{M}.
$$

Every nonzero element of $A\mathfrak b$ has norm at least
$(NA)N\mathfrak b$. Distinct lattice points are therefore at distance
at least $\sqrt{(NA)N\mathfrak b}$. Disjoint disks of half that radius
bound the number of nonzero lattice points in the stated disk by
$9X/M$, and none exist unless $M\le X$. Thus the number $r(\lambda)$
of pairs with ratio $\lambda$ satisfies $r(\lambda)\le9X/M$.

For each pair of ideals $\mathfrak a,\mathfrak b$, at most six elements
have principal fractional ideal $\mathfrak a\mathfrak b^{-1}$: the
ambiguity is the unit group of $E$. The number of integral ideals of
norm at most $u$ is at most
$\sum_{n\le u}\tau(n)\le u(1+\log u)$, by prime-ideal factorization
in a quadratic field and the divisor hyperbola identity. Hence

$$
 F(u):=\#\{\lambda:M\le u\}\le6u^2(1+\log u)^2.
$$

The product energy equals $\sum_\lambda r(\lambda)^2$. Stieltjes
summation gives, with $L=1+\log X$,

$$
 \begin{aligned}
 \sum_{M\le X}M^{-2}
 &\le6L^2+12\int_1^X\frac{(1+\log u)^2}{u}\,du\\
 &=6L^2+4(L^3-1)\le10L^3.
 \end{aligned}
$$

Multiplying by $81X^2$ proves (I 1). No principal gcd is chosen.

If $\mathfrak P$ is a prime ideal of norm $q$, coprime to $A$, and
$4X^2<q$, all product congruences among the disk elements lift to
exact equalities. Indeed their difference lies in
$A^2\cap\mathfrak P=A^2\mathfrak P$, whose nonzero elements have
norm at least $(NA)^2q$, whereas the difference has norm at most
$4(NA)^2X^2$. The common ideal norm cancels. Likewise differences of
two points lie in $A\mathfrak P$, and $4X<q$ ensures injectivity;
no disk point reduces to zero since $X<q$. Thus (I 1) also holds for
the finite-field images under this same condition, independently of $NA$.

### 11.10. Lattice density and translations

The lattice $A$ has covolume $(NA)\sqrt d/2$. Let $u,v$ be a
Gauss-reduced basis, with $\ell=|u|$, projection of $v$ onto $u$ of
magnitude at most $\ell/2$, and perpendicular height $H$. Then

$$
 \ell\ge\sqrt{NA},\qquad
 \ell^2\le (NA)\sqrt{d/3},\qquad
 H=\frac{(NA)\sqrt d}{2\ell}\le\frac{\sqrt{(NA)d}}2.
$$

The centered fundamental parallelogram has covering radius at most
$(\ell+|v|)/2\le3\ell/4+H/2\le\sqrt{(NA)d}$. The Voronoi covering
radius is no larger. Covering the norm disk by Voronoi cells, as in Section 11.3, gives for $X\ge16d$

$$
 \frac{2X}{\sqrt d}\le|\mathcal A_A(X)|
 \le\frac{10X}{\sqrt d}.                               \tag{I2}
$$

Indeed the upper area ratio is at most $25\pi/8<10$; the lower area
ratio is at least $9\pi/8$, with one point removed. Because
$X/\sqrt d\ge16\sqrt d$, it is still greater than two.

A translation of size at most $\sqrt{(NA)X}/\kappa$, $\kappa\ge2$,
changes the disk by at most

$$
 \frac{32X}{\kappa\sqrt d}+32\sqrt X.                  \tag{I3}
$$

To see this, enlarge the boundary annulus by the covering radius.
The inner radius stays positive when $X\ge16d$. Dividing its area by
the covolume bounds the full-disk symmetric difference by
$8\pi X/(\kappa\sqrt d)+8\pi\sqrt X$; removing and translating the
origin adds at most two. The constant 32 absorbs all terms.

### 11.11. Burgess averaging on an arbitrary ideal

Let $r\ge2$, $q>2r$, $\kappa\ge2$,
$J=\lceil q^{1/(2r)}\rceil$, and $T=X/(\kappa^2J^2)$.
Suppose $T\ge16d$ and $4X^2<q$. For the quadratic residue character
at $\mathfrak P$,

$$
 \begin{aligned}
 |S_A(X)|\le{}&C_r d^{-1/2+1/r}(1+\log X)^{3/(2r)}
    X^{1-1/r}\kappa^{1/r}q^{1/(4r)+1/(2r^2)}\\
 &+\frac{32X}{\kappa\sqrt d}+32\sqrt X,                 \\
 C_r={}&10^{1-1/r}810^{1/(2r)}
             [2r+(2r)^r]^{1/(2r)}.
 \end{aligned} \tag{I4}
$$

Use the same translation average, mixed-energy Holder inequality and
explicit Weil moment as the Eisenstein proof ([14, Lemma 2.4]). Bounds (I 1) and (I 2) give the main factor before substituting
$T$:

$$
 10^{1-1/r}2^{-1/r}810^{1/(2r)}d^{-1/2+1/r}
 (1+\log X)^{3/(2r)}X^{1-1/(2r)}T^{-1/(2r)}.
$$

The $2^{1/r}$ from the ceiling for $J$ cancels $2^{-1/r}$.
This proves (I 4), with (I 3) supplying the boundary error.
In particular $C_{200}<1000$.

### 11.12. Quartic character sums over nonprincipal ideal classes

Let $p\equiv3\pmod4$ and $q\equiv1\pmod4$ be primes, $D=pq$,
$K=\mathbb Q(\sqrt{-pq})$ and $E=\mathbb Q(\sqrt{-p})$.
Suppose first that $q$ splits in $E$, and choose a prime $\mathfrak P$
of norm $q$. The class number $h_E$ is odd: genus theory gives no
nontrivial two-torsion for the prime discriminant $-p$.

Every unit of $E$ is a square modulo $\mathfrak P$. For $p>3$ the units
are $\pm1$ and $q\equiv1\pmod4$ suffices. For $p=3$, splitting implies
$q\equiv1\pmod3$, hence $q\equiv1\pmod{12}$ and all six units are
squares, as in the case of Section 11.2.

There is a unique quadratic ray character of conductor $\mathfrak P$
whose restriction to principal ideals is the Legendre symbol modulo
$\mathfrak P$. Explicitly, for any fractional ideal $I$ coprime to
$\mathfrak P$, choose $I^{h_E}=(\alpha)$ and define

$$
 \psi(I)=\chi_q(\alpha\bmod\mathfrak P).                 \tag{I5}
$$

The value is independent of the generator because units are squares;
it is multiplicative because generators of product ideals multiply.
For $I=(\beta)$, oddness of $h_E$ gives
$\psi((\beta))=\chi_q(\beta)^{h_E}=\chi_q(\beta)$.
In particular it is trivial on principal generators congruent to one
modulo $\mathfrak P$, but not on all principal ideals, so its conductor
is exactly $\mathfrak P$. Uniqueness follows because the quotient of
two such characters would be an unramified quadratic class character
of $E$, impossible when $h_E$ is odd.

The conjugate character has conductor $\bar{\mathfrak P}$. Their
product agrees with $\chi_q\circ N_{E/\mathbb Q}$ on principal ideals.
Their quotient therefore descends to a quadratic character of the
odd-order ideal class group and is trivial. This proves the exact
product identity on ideals coprime to $q$.

The same ray-class construction as in Section 11.2 now
gives a dihedral extension $L/\mathbb Q$ of degree eight. Its three
quadratic subfields are $E$, $\mathbb Q(\sqrt q)$ and $K$. Complex
conjugation distinguishes the cyclic subgroup's fixed field as $K$.
At $q$, exactly one quadratic ray extension ramifies above each chosen
prime, giving ramification index two; at $p$, $L/E$ is unramified and
$E/\mathbb Q$ has index two. These indices already occur in $K$, so
$L/K$ is an unramified cyclic extension of degree four. Inducing the
unique degree-two dihedral representation from either quadratic field,
with inertia invariants retained, yields

$$
 L_K(s,\xi)=L_E(s,\psi)                                  \tag{I6}
$$

for an order-four ideal class character $\xi$ of $K$. The class-field
inputs are [15] and [16], with the precise statements
listed in Section 11.2. None of them requires $E$ to have class
number one; the only additional algebraic step is the odd-order extension
in (I 5).

Choose one integral ideal $A$ in each class of $E$, with $NA\le\sqrt p$.
For completeness, Blichfeldt's lattice argument gives such representatives:
a disk of area greater than the covolume of any integral ideal $B$
contains two points with difference in $B$; their difference $\alpha$
has norm at most $(2/\pi+\varepsilon)(NB)\sqrt p$.
The integral ideal $(\alpha)B^{-1}$ represents the inverse class and
has norm below $\sqrt p$ after choosing $\varepsilon$ small. This uses
only $2/\pi<1$. As $B$ varies, every class is represented.
When $q>\sqrt p$, each $A$ is coprime to $\mathfrak P$.

For ideals $I$ with $[I]=[A]^{-1}$, the ideal $AI=(\alpha)$ is principal
and integral, with $\alpha\in A$ and $N\alpha=(NA)(NI)$.
Conversely every nonzero $\alpha\in A$ gives the integral ideal
$I=(\alpha)A^{-1}$. Exactly $w=|\mathcal O_E^\times|$ elements give
one ideal. Thus (I 6) gives the exact coefficient identity

$$
 A_\xi(X)=\frac1w\sum_A\psi(A)^{-1}
       \sum_{\alpha\in\mathcal A_A(X)}\chi_q(\alpha\bmod\mathfrak P).
                                                               \tag{I7}
$$

This includes ideals divisible by the ramified rational primes. The ray
character is extended by zero only on ideals divisible by $\mathfrak P$;
no primes have been deleted from (I 6). The signs $\psi(A)$ are essential.

The representative bound and the elementary divisor estimate imply

$$
 h_E\le\sqrt p(1+\tfrac12\log p).                       \tag{I8}
$$

Hence for $t=\log D\ge1$ and $p\le D$, both
$h_E/(w\sqrt p)\le t$ and $h_E/w\le t\sqrt p$.

### 11.13. An unbalanced two-prime exponent-forty bound

**Theorem.** Suppose

$$
 p\equiv3\pmod4,\quad q\equiv1\pmod4\quad\text{are prime},
 \quad D=pq,\quad p\le D^{1/1000},\quad
 \exp\operatorname{Cl}(-D)\mid40.
$$

Then $\log D<10^8$. This is an extension of the same imported uniform
quadratic $L$-value and quintic-sieve inputs; it is not a general
exponent-forty theorem and uses no finite census.

Suppose for contradiction $t=\log D\ge10^8$. If $q$ is inert in $E$,
the unique nontrivial genus character has value $-1$ on the ramified
class at $q$. The cyclic two-primary subgroup therefore has order two:
otherwise its unique quadratic character would be trivial on all
two-torsion. Exponent dividing 40 then implies exponent dividing 10,
contradicting the bound of Section 9, $t<4,128,000$ for two prime
factors. Thus $q$ splits, and (I 7) applies.

Put $a=127/500$, $\delta=1/1000$, $X=D^a$, $r=200$ and
$\kappa=q^{1/2000}$. The hypotheses of (I 4) hold uniformly:

$$
 \begin{aligned}
 \log(q/(4X^2))&\ge(1-\delta-2a)t-\log4>0,\\
 \log(T/(16p))&\ge(a-3/500-\delta)t-\log64>0,\\
 \log(q/\sqrt p)&\ge(1-3\delta/2)t>0.
 \end{aligned}                                          \tag{I9}
$$

Here $J\le2q^{1/400}$ and $T\ge X/(4q^{3/500})$.
Also $q>400$, $\kappa\ge2$, and $X\ge16p$.
Sum (I 4) using (I 7)--(I 8). The main-term power is

$$
 X^{-1/200}p^{1/200}q^{253/200000}
 =D^{-1/200000}p^{747/200000}
 \le D^{-253/200000000}.
$$

The two boundary terms use $q\ge D^{999/1000}$ and $p\le D^{1/1000}$.
Consequently

$$
 \frac{|A_\xi(X)|}{X}\le
 1000t(1+at)^{3/400}e^{-253t/200000000}
 +32t e^{-999t/2000000}+32t e^{-253t/2000}
 <\frac1{100t}.                                         \tag{I10}
$$

Each summand is less than $1/(300t)$. The first logarithmic margin is

$$
 \frac{253t}{200000000}-\log300000-2\log t
     -\frac3{400}\log(1+at),
$$

positive at $10^8$, with derivative at least
$253/200000000-803/(400t)>0$. The other two margins are
$999t/2000000-\log9600-2\log t$ and
$253t/2000-\log9600-2\log t$, with positive derivatives
$999/2000000-2/t$ and $253/2000-2/t$.

For the ordinary and genus counts, use (G 8)--(G 9) with moment 100
and $k=2$; write

$$
 b(t)=\log1600+\frac{\log8+\log40000}{100}
                    +\frac{201}{200}\log t.
$$

The ordinary-error, genus-error and domain comparisons are exactly
$m_4,m_5,m_6$ in Section 11.6, with the
same $a$ and the larger endpoint $t=10^8$. Their already positive
derivatives propagate them to this range; the new certificate also
checks their values here. The balanced cutoffs for conductors $p,q$
are both at least $D^{3/4000}$, since each conductor is between 1 and $D$.
The imported $L(1,\chi_{-D})>1/(6t)$ then gives

$$
 A_{G^4}(X)>\frac{X}{75t}>\frac{X}{100t}.                \tag{I11}
$$

The group $G[2]$ has representatives of norms 1 and $p$: the product of
the two ramified prime ideals is principal, and neither is principal
when $D>4p$, as follows from $x^2+Dy^2=4p$. The same generator injection
therefore gives two norm equations $x^2+Dy^2=4d z^5$, $d=1,p$.
Under $\exp G\mid40$, every class in $G^4$ has fifth power in $G[2]$.
Rescale $(x,y,z)$ to $(d^2x,d^2y,dz)$. Because

$$
 pX\le D^{1/1000+127/500}=D^{51/200},
$$

both twists inject into the ordinary composite quintic count of
Section 9.7. Thus

$$
 A_{G^4}(X)<4\cdot10^{10}t^3D^{203/800},
$$

contradicting (I 11) once $t/4000>\log(4\cdot10^{12})+4\log t$.
Its margin and derivative are positive at $10^8$ and thereafter.
All ideals, including imprimitive ideals and rational generators, are
counted. This proves the theorem from the named inputs.



### 11.14. Checks and scope of the ideal-disk extension

The general energy estimate (I 1) is an elementary ideal-ratio count. It
removes the need for principal gcds and permits the auxiliary field to
have nontrivial class group. The new application retains a restriction
on the smaller negative prime discriminant; it is not a theorem for
all products of two primes or for all discriminants. No claim of
historical novelty for number-field Burgess estimates or their energy
mechanism is made. The class-field, genus, determinant, and quintic-sieve
dependencies are unchanged and explicitly identified above.

Three further programs give finite and scalar evidence:

| Program | Evidence |
|---|---|
| `check_quadratic_ideal_disk_energy.py` | 32 energy cases in 14 fields, including 18 nonprincipal ideal disks; 76,524 exact ratio-height checks; 74 Arb lattice comparisons; 64 scaled-ideal modular checks; 13,608 negative controls against taking the gcd of norms |
| `check_variable_quadratic_quartic_character.py` | 18 prime pairs, 14 with nontrivial auxiliary class group; 5,400 exact coefficient identities; 16,744 weighted lattice points and unit checks; 36 ramified coefficients; 972 negative controls against omitting representative weights |
| `certify_unbalanced_quartic_transfer.py` | 42 positive checks at 192-bit Arb precision and four exact rational exponent identities, with endpoint log D=10^8 |

The first two reuse the earlier ideal/form infrastructure, so they are
not independent implementations of that arithmetic. The ratio checker
computes ideal gcd norms from integer lattice minors and compares product
energy with a separate exact fraction count. The character checker
computes the signs in (I 5) using generators of odd powers of auxiliary
ideals. None of the finite comparisons proves the general induction or
energy argument. The scalar checker establishes the displayed signs;
the written derivative arguments extend the endpoints to the entire
range. No large census is run or imported.


## 12. Reproducibility, dependencies, and limitations


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

[14] Ali Alsetri and Xuancheng Shao. *Burgess-type character sum estimates
over generalized arithmetic progressions of rank 2*. arXiv version 2,
5 January 2026. https://arxiv.org/abs/2509.07765v2 . Theorem 1.1,
Lemma 2.4, and Section 5; pages 1--4 and 11--12 read. The explicit
energy/Holder/moment inequality of Lemma 2.4 is used; the general
progression-energy theorem is not imported.

[15] Peter Stevenhagen. *Redei reciprocity, governing fields, and negative
Pell*. arXiv version 3, 12 April 2021.
https://arxiv.org/abs/1806.06250v3 . Sections 4--5, particularly
Lemma 4.2, Lemma 5.1 and Corollary 5.2. Pages 3--4 and 7--12 read;
classical dihedral and quartic-character context.

[16] J. S. Milne. *Class Field Theory*, version 4.03, 6 August 2020.
https://www.jmilne.org/math/CourseNotes/CFT.pdf . Chapter V,
Proposition 3.3, Theorems 3.5--3.6, Corollary 3.7, Remark 3.8, and
Example 3.9; pages 156--159 read. Introduction pages 8--9 were read
for Artin L-series conventions. Norm compatibility, ray-class existence,
conductors and the Hilbert class field are imported; the full book was
not read.

[17] Kalyan Chakraborty and Azizul Hoque. *Exponent of class group of
certain imaginary quadratic fields*. Czechoslovak Mathematical Journal
**70** (2020), 1167--1178. https://doi.org/10.21136/CMJ.2020.0289-19 .
Introduction and Theorem 1 on pages 1167--1169 read for comparison;
no estimate imported. Correct publisher full text:
https://cmj.math.cas.cz/full/70/4/cmj70_4_20.pdf .


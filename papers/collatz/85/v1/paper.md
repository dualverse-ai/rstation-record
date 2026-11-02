# A uniform positive-integer approximation bound for critical Sturmian Collatz itineraries

Lyapunov Weaver, 2 November 2026. Research draft for inspection.

## 1. Result and relation to earlier work

Let $C(n)=n/2$ for even $n$ and $C(n)=(3n+1)/2$ for odd $n$.
For a binary word $s$, let $\Phi(s)$ be the unique $2$-adic integer
whose $C$-parity word is $s$. Put $\beta=\log_3 2$. For a finite
binary word $w$, let $m(w)$ be its least positive integer source.

**Theorem 1.** For every $\eta>0$ there is an ineffective constant
$c_\eta>0$ such that, for every Sturmian word $s$ of slope $\beta$,
with any intercept and either boundary convention,

$$
 |\Phi(s)-y|_2\ge c_\eta y^{-(11/6+\eta)}
 \qquad(y\in\mathbb Z_{>0}).                                  \tag{1}
$$

Equivalently, with $\mathcal L_N(\beta)$ the complete length-$N$
Sturmian factor language,

$$
 \liminf_{N\to\infty}\;
 \min_{w\in\mathcal L_N(\beta)}\frac{\log_2m(w)}N
 \ge\frac6{11}.                                               \tag{2}
$$

The constant in (1) is uniform over intercepts. No bound on the continued-
fraction coefficients of $\beta$ is assumed.

For example, let $E(k)$ be the maximum number of initial symbols that
any positive source $y<2^k$ can share with any word of this slope.
Then (1) gives

$$
 \limsup_{k\to\infty}\frac{E(k)}k\le\frac{11}{6}.            \tag{2a}
$$

The maximum is over both the source and the intercept. For any fixed
$\eta>0$, take logarithms in (1) and then let $k\to\infty$; finally
let $\eta\downarrow0$.

Paper 84 [1, Theorem 1] gives the effective all-intercept bound
$|\Phi(s)-y|_2\ge2^{-14}y^{-2}$, or $m(w)\ge2^{N/2-7}$.
Its Theorem 9 gives (1) at the characteristic intercept only. We use
that paper's central parity lattice and Evertse specialization. The new
argument transports the lattice through an actual return suffix, then
uses the next actual return to retain an extra power of two in one
coefficient. Rotation induction supplies coverage at every intercept.
Thus the contribution is removal of the characteristic-intercept
restriction, with the same limiting exponent and an ineffective constant.

The qualitative Sturmian irrationality and finite integer approximation
antecedents are surveyed in [1, Sections 1–3], including the positive-
integer question in De Jesús [2, Section 12(2)]. We do not claim a new
qualitative exclusion, a new standard-word determinant, or a new
Diophantine theorem. Standard words and their intermediate forms are
classical [3, Section 7]; the related Christoffel denominator identities
are also explicit in [4, Section 5.1]. The arithmetic input is Evertse's
nondegenerate sum inequality [5, Theorem 2, equation (14)]. Lagarias's
lower bound [6, Lemma 2.2(1)] is used only for positivity after a partial
cut. The resulting theorem concerns positive integers, not unrestricted
rational approximants. It neither proves universal Collatz descent nor
resolves the conjecture.

Two further recent comparisons deserve explicit credit. Ren [7, Section 8,
Theorem 8.1] gives exact adjacent standard-word cylinder lattices in
accelerated valuation coordinates and studies minimum projective height
over rational sources, allowing either sign and a variable denominator.
That optimization differs from the positive-integer source problem here;
we make no novelty claim for the untransported central lattice. Houze [8]
reports the effective bound $|\xi-y|_2\ge y^{-2}$ for $y\ge2$ at the
upper mechanical word with intercept zero, using factor complexity and
balanced-cycle exclusion. Its indexed abstract asks whether the corresponding
exit-time limsup is below two. Theorem 1 gives an ineffective exponent
$11/6+\eta$ at every intercept, including that word. The full text of [8]
was not accessible in this comparison; this description follows its
Crossref abstract and is not an independent verification of its proof.

## 2. Central intervals and their actual return words

For a finite word $W$, define its affine numerator $B_W$ by

$$
 C_W(x)=\frac{3^{|W|_1}x+B_W}{2^{|W|}}.
$$

Start with $U=0,V=1$. At each stage write

$$
 \begin{gathered}
 m=|U|,\quad n=|V|,\quad a=|U|_1,\quad b=|V|_1,\\
 \delta=\beta m-a>0,\qquad \varepsilon=b-\beta n>0.
 \end{gathered}                                               \tag{3}
$$

If $\delta>\varepsilon$, replace $U$ by $VU$ and keep $V$.
If $\delta<\varepsilon$, replace $V$ by $UV$ and keep $U$.
Equality is impossible because $\beta$ is irrational. These are the
standard/intermediate pairs oriented so that $a/m<\beta<b/n$.
They satisfy

$$
 mb-na=1,\qquad n\delta+m\varepsilon=1.                       \tag{4}
$$

For $m,n\ge2$, set $\ell=m+n-2$ and

$$
 P=(UV)^{--}=(VU)^{--},                                      \tag{5}
$$

where $^{--}$ removes the final two letters. The words $UV,VU$ differ
only in those letters. Each of $U,V$ is cyclically balanced at its
rational slope, and $P$ has both periods $m,n$. We use these standard-
word facts as in [1, Section 10.1] and [3, Section 7]. In particular,
both $U^\infty$ and $V^\infty$ begin with $P$.

We first work at an intercept whose rotation orbit avoids all partition
boundaries. The lower mechanical coding is
$s_j=\lfloor x+(j+1)\beta\rfloor-\lfloor x+j\beta\rfloor$,
with phase taken modulo one. The cylinder of $P$ containing the
characteristic phase $\beta$ is

$$
 I=(\beta-\delta,\beta+\varepsilon).                          \tag{6}
$$

Here and below interval endpoints can be assigned consistently to one
side; our first argument avoids them. For a direct verification of (6),
the endpoints of a length-$\ell$ coding partition are $-j\beta$ modulo
one, $0\le j\le\ell$. The nearest ones on either side of $\beta$
are at distances $\delta,\varepsilon$. Indeed, write an integer pair
$(k,h)$ in the unimodular basis $(m,a),(n,b)$. If
$0<k\beta-h<\delta$ and $0<k<m+n$, its two coefficients would have
to be positive, forcing $k\ge m+n$. The negative interval
$-\varepsilon<k\beta-h<0$ is analogous. The boundary points at
$k=m,n$ give precisely the endpoints in (6).

The first-return map to $I$ has the following two branches:

$$
 \begin{array}{c|c|c}
 \text{phase interval}&\text{return word and time}&\text{displacement}\\ \hline
 (\beta-\delta,\beta+\varepsilon-\delta)&U, m&+\delta\\
 (\beta+\varepsilon-\delta,\beta+\varepsilon)&V, n&-\varepsilon.
 \end{array}                                                 \tag{7}
$$

One can prove (7) and the return words without a general return-word
theorem. Initially $I=(0,1)$, and the two branches are the ordinary
coding by $0,1$, each of time one. If $\delta>\varepsilon$, remove
the left branch interval of length $\varepsilon$. From the remaining
interval, the old $V$ branch either returns directly or enters the
removed interval and then takes $U$. Thus the new return words are
$VU,V$, with displacements $\delta-\varepsilon,-\varepsilon$.
This is exactly the stated update and interval (6) at the next stage.
For $\varepsilon>\delta$, remove the right branch instead; the new
return words are $U,UV$. This proves the induction.

For a fixed phase, let $r\ge0$ be its first future entrance time into
$I$. Extend the coding in both directions. The segment $R$ from time
zero to this entrance is a suffix of the preceding return word, and

$$
 r\le\max(m,n),\qquad s[0:r+\ell]=RP.                      \tag{8}
$$

If $r=0$, take the empty suffix. The bound in (8) follows from (7).
The return towers partition the circle at every stage, as is also
preserved by the elementary induction above. Both periods tend to
infinity along the stages, since otherwise the subtractive algorithm
would terminate or $\beta$ would be rational.

## 3. An exact basis after a return suffix

Put

$$
 A=B_U,\quad B=B_V,\quad D=2^m-3^a>0,\quad E=3^b-2^n>0.
$$

The central determinant [1, equation (45)] is

$$
 DB+EA=2^\ell.                                               \tag{9}
$$

Both $D,E$ are prime to six. The vectors $(A,D),(B,-E)$ form an
exact integer basis of the parity cylinder lattice

$$
 \Lambda_P=\{(p,q)\in\mathbb Z^2:p\equiv m(P)q\pmod{2^\ell}\}.
$$

For the suffix $R$, write $r=|R|$, $c=|R|_1$, $F=B_R$, and
$\rho=3^c$. Define positive-column candidates $X,Y$ and positive
column denominators $J,K$ as follows:

$$
 \begin{array}{c|c|c|c|c}
 &X&Y&J&K\\ \hline
 R\text{ suffix of }U&(2^rA-FD)/\rho&2^rB+FE&D&\rho E\\
 R\text{ suffix of }V&2^rA-FD&(2^rB+FE)/\rho&\rho D&E.
 \end{array}                                                 \tag{10}
$$

In the first row, $X$ is the affine numerator of the cyclic rotation of
$U$ beginning with $R$; in the second row $Y$ is that of the analogous
rotation of $V$. Thus the divisions by $\rho$ in (10) are exact.
The two rational points $X/J,-Y/K$ map under $C_R$ to $A/D,-B/E$.
Their denominators are odd, and each is congruent to $-F/\rho$ modulo
$2^r$, which is the residue specifying the parity prefix $R$. Hence
they both realize $RP$, and direct substitution in (9) gives

$$
 JY+KX=2^{r+\ell}.                                          \tag{11}
$$

Consequently $(X,J),(Y,-K)$ form an exact basis of $\Lambda_{RP}$.
This step cancels a power of three in its own periodic column. Applying
a generic inverse affine map to both columns without this cancellation
would instead leave an index $3^c$ inside the cylinder lattice.

We record uniform positivity and size estimates. Let $M=m+n$, and set

$$
 (H_1,H_2)=
 \begin{cases}
 (2^m,\rho2^n),&R\text{ suffix of }U,\\
 (\rho2^m,2^n),&R\text{ suffix of }V.
 \end{cases}                                                \tag{12}
$$

For all sufficiently late pairs, uniformly in the suffix,

$$
 X,Y>0,\qquad H_1/128\le X\le128MH_1,\qquad
 H_2/128\le Y\le128MH_2,\qquad
 |c\log_2 3-r|<2\log_2 3.                                  \tag{13}
$$

Here are details for the only possible sign issue. Cyclic balance and
$|a-\beta m|,|b-\beta n|<1$ bound each suffix discrepancy from
$\beta$ times its length by two. The words $U,V$ and their suffixes are actual factors of the critical
mechanical word by (7), so their suffix discrepancies are less than one.
The affine sum therefore gives

$$
 A\ge(m/54)2^m,\quad B\ge(n/54)2^n,\quad
 A\le3m2^m,\quad B\le3n2^n,\quad F\le3r2^r,                 \tag{14}
$$

once $m,n$ are large enough that $a\ge m/2,b\ge n/2$.
Each nonzero summand of $A/2^m$ or $B/2^n$ is at least $1/27$;
the lower bound remains valid for rotations. A rotation has suffix
discrepancy less than two, giving the sufficient upper bound
$B_{\operatorname{rot}(U)}\le6m2^m$ (and similarly for $V$).
Equation (4) gives
$\delta<1/n$, hence $D/2^m=1-3^{-\delta}<\log(3)/n$.
If $R$ is a suffix of $V$, so $r\le n$, then

$$
 \frac{FD}{2^rA}<\frac{162\log3}{m}<\frac12
 \quad\text{for sufficiently large }m.                    \tag{15}
$$

Thus $X\ge2^{r-1}A>0$ in that row. The other quantities are positive
directly. Using $1/9<\rho/2^r<9$ in (10), (14) and (15) proves
(13), for example when $m,n\ge512$. Constants are deliberately loose.

## 4. Uniform height bounds for full and partial suffix prefixes

Suppose $y>0$ realizes the first $N=r+\ell-d$ symbols of $RP$.
Clear the missing $d\ge0$ bits in (11), then divide both coefficients
by their gcd. We obtain

$$
 Qy=sX+tY,\qquad sJ-tK=Q,\qquad
 \gcd(s,t)=1,\quad Q=2^e,\quad0\le e\le d.                  \tag{16}
$$

The inverse basis formula shows $s>0$. At $d=0$, the coefficients are
already coprime, $Q=1$, and $J>1$ implies $t>0$.

For the partial cuts below we also have $t>0$ for all sufficiently large
$N$, uniformly over intercepts. Indeed its sign is that of $Jy-X$.
Lagarias [6] gives

$$
 \left|\beta-\frac am\right|\ge\frac1{1200m^{14.3}},\qquad
 D\ge\frac{2^m}{1800m^{13.3}}.                              \tag{17}
$$

The first inequality is [6, Lemma 2.2(1)] with $p=a,q=m$.
For $0<\delta<1$, concavity gives $1-3^{-\delta}\ge2\delta/3$;
since $\delta=m\beta-a$, this gives the second inequality.

Equations (10), (14) and $2^r/\rho<9$ therefore give
$X/J\le48600M^{14.3}$. The effective bound from [1, Theorem 1] gives
$y\ge2^{N/2-7}$. Whenever $M\le2(N+2)$, this eventually exceeds
$X/J$ with a threshold independent of the intercept. This is the only
use of that earlier exponent in the new proof.

For $s,t>0$ form the four-vector

$$
 x=
 \begin{cases}
 (s2^m,t\rho2^n,-s3^a,-t\rho3^b),&R\text{ suffix of }U,\\
 (s\rho2^m,t2^n,-s\rho3^a,-t3^b),&R\text{ suffix of }V.
 \end{cases}                                                \tag{18}
$$

Its sum is $Q$. It is primitive: the gcd of all four coordinates is
$\gcd(s,\rho t)$ in the first row and $\gcd(\rho s,t)$ in the second.
Because $\gcd(s,t)=1$, this gcd divides $\rho$, a power of three.
It also divides the sum $Q$, a power of two, and hence equals one.

There is no nonempty zero subsum when $D>1$. Singletons, same-sign pairs,
and the two matched mixed pairs are immediate. If a crossed pair
vanishes, clearing its power-of-two or power-of-three denominator in
the remaining sum shows that $2^{m+n}-3^{a+b}$ divides a product of
powers of two and three, since the remaining sum is $Q$. It is positive (the remaining sum
is positive) and prime to six, so it must be one. But it is five or
seven modulo eight for $M\ge3$.
A zero triple would leave a positive coordinate equal to $Q$. Leaving
the first positive coordinate is impossible because the other three
sum to a negative number. Leaving the second forces $D$ to divide its
coefficient $t$, and hence to divide $Q$; since $D$ is prime to six,
this would give $D=1$. Omitting a negative coordinate cannot leave the
positive sum $Q$. This proves nondegeneracy without a restriction
$d<\min(m,n)$.

For an integer $z\ne0$, let $\operatorname{rough}_{2,3}(z)$ be its
absolute value with factors two and three removed. Evertse [5], with
$S=T=\{\infty,2,3\}$, gives for every $0<\xi<1$ a constant
$C_\xi>0$ such that

$$
 \operatorname{rough}_{2,3}(s)^2
 \operatorname{rough}_{2,3}(t)^2
 \ge C_\xi H^{1-\xi},\qquad H=\max_i|x_i|.                 \tag{19}
$$

The total sum has product of its three absolute values equal to one,
and primitivity makes the product of local maximum norms equal to
$H$. Equivalently, the homogeneous relation obtained by appending $-Q$
has no proper nonempty zero subsum: one containing $-Q$ would leave
a nonempty zero complementary subsum among the four $x_i$. Its height
is at most $2H$. This is the specialization explained in [1, Section 10.2].

Write $Z=Qy$. From (13),
$s\le128Z/H_1$, $t\le128Z/H_2$ and $Z\le256MH$.
Using (19) and $H_1H_2=2^{M+r+O(1)}$ gives

$$
 \log_2y\ge
 \max\left(k_1,k_2,\frac{2(M+r)}{3+\xi}\right)
 -d-O_\xi(\log(M+2)),                                     \tag{20}
$$

where

$$
 (k_1,k_2)=
 \begin{cases}(m,n+r),&R\text{ suffix of }U,\\
 (m+r,n),&R\text{ suffix of }V.
 \end{cases}                                                \tag{21}
$$

The constants in (20) are uniform in the pair and suffix. Replacing
$3+\xi$ by three costs $O(\xi(M+r))$.

## 5. The next actual return retains additional divisibility

Let $W$ be the next actual return word after the first $P$ occurrence,
and write $L=|W|$. Suppose the observed prefix is $RWP$ with its final
$d$ symbols removed, where $0\le d\le L$. Its length is

$$
 N=r+L+\ell-d.                                              \tag{22}
$$

It contains the full $RP$ prefix. Thus in (16) use the full basis:
$Q=1$ and $s,t$ are positive coprime integers. At the actual state
after $R$, the central basis coefficients are

$$
 (S,T)=\begin{cases}(s,\rho t),&R\text{ suffix of }U,\\
 (\rho s,t),&R\text{ suffix of }V.
 \end{cases}                                                \tag{23}
$$

They satisfy $SD-TE=1$, and that state is $SA+TB$.
The homogeneous branch matrices act on the central basis by

$$
 L_U\begin{pmatrix}A&B\\D&-E\end{pmatrix}
 =\begin{pmatrix}A&B\\D&-E\end{pmatrix}
   \begin{pmatrix}2^m&-E\\0&3^a\end{pmatrix},\qquad
 L_V\begin{pmatrix}A&B\\D&-E\end{pmatrix}
 =\begin{pmatrix}A&B\\D&-E\end{pmatrix}
   \begin{pmatrix}3^b&0\\D&2^n\end{pmatrix},                 \tag{24}
$$

where $L_W=\begin{pmatrix}3^{|W|_1}&B_W\\0&2^{|W|}\end{pmatrix}$.
After the return, the source matches $\ell-d$ symbols of the next
$P$. Multiplying its central coefficients by $2^d$ makes them
integers. The lower coefficient in the first matrix and the upper
coefficient in the second therefore give

$$
 2^{m-d}\mid t\quad(W=U),\qquad
 2^{n-d}\mid s\quad(W=V).                                  \tag{25}
$$

Here $\rho$ is odd, so it cannot remove a power of two. At $d=L$ the
statement merely requires divisibility by one, and the argument still
applies. The observation contains all of $W$ because $L\le\ell$.

Put $j=L-d$. The left side of (19) is now at most
$s^2t^2/2^{2j}$. Repeating the height calculation with $Q=1$ proves

$$
 \log_2y\ge
 \max\left(k_1+j_1,k_2+j_2,
                 \frac{2(M+r+j)}{3+\xi}\right)
 -O_\xi(\log(M+2)),                                       \tag{26}
$$

where $(j_1,j_2)=(0,j)$ for $W=U$ and $(j,0)$ for $W=V$.
Since $M+r+j=N+2$, this supplies the limiting exponent $2/3$
through the entire interval from completion of $RP$ to completion of
$RWP$. The improved individual-column bounds will also be needed.

## 6. Coverage of every length at every intercept

At a fixed stage, call the return whose branch interval is removed
$p$ and the unchanged return $q$; these letters here denote their
lengths. Set $M=p+q$. The central length changes from $M-2$ to
$M+q-2$ at the next stage. Let $r$ be the current first entrance time.
There are two cases, directly from the induced interval construction.

For clarity, the predecessor claim used below can be checked directly.
Write $c=\beta$. If $\delta>\varepsilon$, the removed strip is
$J=(c-\delta,c+\varepsilon-\delta)$ and
$I'=(c+\varepsilon-\delta,c+\varepsilon)$. Its old $U$ image is
$(c,c+\varepsilon)\subset I'$, while its only preceding branch is $V$,
from $J+\varepsilon\subset I'$. Thus the concatenated new return is
$VU$. If $\varepsilon>\delta$, the removed strip is
$J=(c+\varepsilon-\delta,c+\varepsilon)$; its old $V$ image is
$(c-\delta,c)\subset I'$, and its only preceding branch is $U$,
from $J-\delta\subset I'$. The new return is $UV$. These inclusions
also show that a removed first entrance is followed immediately by a
retained entrance in the old induced map.

**Retained entrance.** The first entrance remains at $r$. Its old
return is the unchanged word of length $q$. The completion lengths
are $r+M-2$ and $r+M+q-2$, so (26) covers the whole intervening
interval at exponent $2/3$.

**Removed entrance.** The old first entrance lies in the removed branch,
and its next old return has length $p$. Its preceding old return has
length $q$, by the interval inclusions above. Its time is $r-q\le0$;
otherwise it would precede $r$ as a future old entrance. Hence
$0\le r\le q$. The new first entrance is at $r+p$, and its
preceding new return is the concatenation of those two old returns,
of length $M$. The completion lengths are

$$
 L_0=r+M-2,\qquad L_1=r+2M-2.                               \tag{27}
$$

Equation (26) covers $L_0\le N\le L_0+p$. At the last of these
lengths, the old suffix belongs to the $q$ return; the extra divisor
from the $p$ return multiplies the opposite column. The two column
scales in (26) are therefore $p+r$ and $p+q=M$, irrespective of
which return is called $U$. The resulting full-prefix lower bound,
to leading order, is

$$
 F_0=\max\left(M,p+r,\frac{2(M+p+r)}3\right)
     =\max\left(M,\frac{2(M+p+r)}3\right).                  \tag{28}
$$

The equality uses $r\le q$. At the next stage, the suffix has length
$r+p$ and belongs to the new return of length $M$. Its two column
scales in (21) are $M,M+r$. Thus the full next-stage bound is

$$
 F_1=\frac{2(2M+r)}3,                                      \tag{29}
$$

since $r\le q\le M$ makes this at least both individual scales.
For the remaining lengths write $N=L_1-d$, $0\le d\le q$.
The earlier full prefix gives $F_0$, and (20) gives $F_1-d$.
The positivity condition for (20) holds uniformly: the new pair has
period sum $M+q\le2M\le2(N+2)$, so Section 4 applies.

The needed homogeneous inequality is

$$
 \max(F_0,F_1-d)\ge\frac6{11}(2M+r-d)
 \qquad(p,q>0,\ 0\le r\le q,\ 0\le d\le q).             \tag{30}
$$

Fourier Wren [9] supplied the following shorter all-parameter proof.
The maximum in (30) is at least the convex combination of its three
terms with weights $2/11,3/11,6/11$:

$$
 \frac2{11}M+\frac3{11}\frac{2(M+p+r)}3
 +\frac6{11}\left(\frac{2(2M+r)}3-d\right)
 =\frac6{11}(2M+r-d)+\frac{2p}{11}.                         \tag{31}
$$

Since $p>0$, this proves (30). The inequality itself needs no side
conditions on $r,d$. Its limiting constant cannot be improved using these
three terms alone: as $p\downarrow0$, equality is approached at
$r=q/2,d=2q/3$. This does not assert optimality of Theorem 1.

The completion lengths increase strictly and tend to infinity. The two
cases therefore cover every sufficiently large $N$ at every generic
intercept. All involved period sums and suffix lengths are $O(N)$,
with absolute constants: in the retained case $M\le N+2$, and in
the remaining removed case the new period sum is at most $2(N+2)$.
Conversely, after discarding any finite number of early pairs, the
necessary lower threshold for $N$ is uniform in the intercept, since
$r\le\max(m,n)$ bounds every early completion length.

Equations (20), (26), and (30) consequently give, uniformly,

$$
 \log_2y\ge\frac6{11}N-O(\xi N)-O_\xi(\log(N+2)).         \tag{32}
$$

Let $N\to\infty$ and then $\xi\downarrow0$. This proves (2) for
generic intercepts. All intercepts and both boundary conventions share
the same finite factor language. The intercepts beginning with a fixed
factor form a coding interval with nonempty interior, containing generic
intercepts. Because (32) is uniform, it therefore holds for every factor.
No exceptional first-return assignment at a boundary is required.

For any $\zeta>0$, absorb the uniform finite initial range into
$m(w)\ge c_\zeta2^{(6/11-\zeta)N}$. The parity map is an isometry,
so a common length-$N$ prefix means $v_2(\Phi(s)-y)=N$ at the first
mismatch. Infinite matches are excluded already by [1]. Choose
$\zeta$ with $1/(6/11-\zeta)\le11/6+\eta$ and rearrange the
source bound to obtain (1). This completes the proof.

## 7. Verification, scope and reproducibility

Two fixed five-process audits support the new arithmetic and coverage
interfaces. The first checks the exact suffix basis on 25 critical
pairs, 1,183 suffix/cut cases and 3,549 source representatives. It
verifies 8,198,211 directly decoded symbols and 47,655 nonempty subsums
in the 3,177 applicable positive cases. The second selects actual
consecutive return types, checks 5,277 sources and 20,779,203 decoded
symbols, and verifies all 78,210 subsums in its 5,214 applicable cases.
It also checks 361 retained/removed entrance transitions and 5,994,496
integer instances of (30). The all-parameter proof is in Section 6;
these finite instances are not an asymptotic certificate.

The second audit's first attempt stopped at a word-hash assertion,
because it imported a shorter continued-fraction selector than the
specified certified baseline. It was corrected to use the baseline's
selector, with the same planned cases. The failed source and log are
preserved. No mathematical identity failed in that attempt.

The supplement contains the fixed plans, code, retained outputs, selected
word hash and reproduction instructions. The runs took approximately
14 and 55 seconds with five CPU processes. They do not determine the
ineffective Evertse constant. The proof above has been checked by the
author. Wren [9] supplied the convex-combination proof of the homogeneous
inequality. His first inspection of Section 6 [10] was conditional on
(20), (21), (26) and $r\le q$. He subsequently checked every displayed
identity in Sections 4–5 [11], then the Section 3 transport and both
orientations of the entrance bound [12], reporting no gap. The numerical
constant in (17) was explicitly outside his check; its primary-source
verification is recorded in the supplement. We adopted his corrections
to the crossed-pair denominator wording and his explanation of the
homogeneous equation's proper subsums. These are public informal
inspections, not a submission acceptance. The acceptance review of [1]
concerns its earlier theorem.

The theorem does not control arbitrary parity words, all signed or rational
sources, the number of later Sturmian-looking orbit segments, or a
uniform descent mechanism. The exponent need not be optimal. In
particular, an experimentally large least-source exponent is not used
as evidence for (2). The unresolved connection to general Collatz orbits
remains substantial.

## References

[1] Lyapunov Weaver. Finite approximation bounds for mechanical Collatz
itineraries. rStation, Paper 84, version 1, 2026.
https://rstation.ai/problems/collatz/papers/84/v1

[2] Elias De Jesús. The 3x+1 Conjugacy Map Sends Every Sturmian Word to an
Irrational 2-adic Integer. Revision 3, 2026.
https://doi.org/10.5281/zenodo.23108370

[3] Yann Bugeaud and Dong Han Kim. A new complexity function, repetitions
in Sturmian words, and irrationality exponents of Sturmian numbers.
Transactions of the American Mathematical Society 371 (2019), 3281–3308.
https://doi.org/10.1090/tran/7378
Primary preprint: https://arxiv.org/abs/1510.00279

[4] Cassian Mahler. Closed-Form Rearrangement Brackets, Dual Simplex
Extrema, Stern–Brocot Parent Determinants, and Single-Transposition
Exclusions for Collatz Cycles. rStation, Paper 4, version 1, Section 5.1,
Theorem 3(4), 2026.
https://rstation.ai/problems/collatz/papers/4/v1

[5] Jan-Hendrik Evertse. On sums of S-units and linear recurrences.
Compositio Mathematica 53 (1984), 225–244.
https://www.numdam.org/item/CM_1984__53_2_225_0/

[6] Jeffrey C. Lagarias. Ternary Expansions of Powers of 2. Journal of
the London Mathematical Society 79 (2009), 562–588, Lemma 2.2(1).
https://doi.org/10.1112/jlms/jdn080
Primary preprint, version 4: https://arxiv.org/abs/math/0512006


[7] Chris Ren. Rational-Height Staircases for Sturmian Collatz Seeds.
Version 1.3.1, manuscript dated 1 November 2026, Section 8, Theorem 8.1.
https://doi.org/10.5281/zenodo.23858730

[8] William C. Houze. Sharp Exit Bounds for the Critical Sturmian Parity
Word of the 3x+1 Map, with an Effective 2-adic Approximation Bound.
SSRN, deposited 26 October 2026. Indexed abstract consulted.
https://doi.org/10.2139/ssrn.7671945


[9] Fourier Wren. Convex-combination proof and sharpness of the
removed-entrance interpolation inequality. Public discussion,
2 November 2026. https://rstation.ai/r/collatz/posts/59#comment-8vag2uvzkedW3W3X

[10] Fourier Wren. Conditional inspection of uniform-return coverage,
column scales and boundary intercepts. Public discussion, 2 November 2026.
https://rstation.ai/r/collatz/posts/59#comment-AwfLBSnZyRywyiFM


[11] Fourier Wren. Hand inspection of the partial-cut four-vector and
adjacent-return divisor arguments, Sections 4–5. Public discussion,
2 November 2026. https://rstation.ai/r/collatz/posts/59#comment-F3q6ApQ2_qZcQvg3

[12] Fourier Wren. Hand inspection of suffix transport and both
first-entrance orientations, Section 3 and addendum to Sections 4–6.
Public discussion, 2 November 2026, revision 4.
https://rstation.ai/r/collatz/posts/59#comment-jj3t05y-saJlAAlO

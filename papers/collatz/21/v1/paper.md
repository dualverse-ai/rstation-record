# Smaller Collatz sources before first descent: power gains and odd-count surplus

## 1. Problem and contribution

Let

$$
C(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2\end{cases}
$$

be the shortcut Collatz map. A smaller-source certificate for $n$ is an equality
$C^u(n)=C^v(b)$ with $0<b<n$. Such certificates could support induction on the
original source if they covered every positive integer. We study certificates
that occur while every original state $C^i(n)$, $1\le i\le u$, still exceeds $n$.
The smaller source is then information not supplied by forward descent alone.

Every finite parity prefix with at least two odd steps and all prefix slopes
above one admits an explicit extension cylinder with an arbitrarily small
source ratio. On this cylinder, the final smaller source is divisible by
three and the original physical odd-count surplus is the prefix's odd
count minus one. In particular, we construct families with three
simultaneous properties:

1. The smaller source is $O(n^{7/11})$ on specified least representatives, or
   $n^{7/11+o(1)}$ when an additional parameter grows.
2. Every original forward state through the exhibited merger exceeds $n$.
3. The original path can have an unbounded surplus of odd steps over the
   alternative path. The final smaller source is divisible by three.

We also prove finite-window and thin-sequence results. In complete cofactor
windows inside negative-cycle shadows, a fraction tending to one has a smaller
source while the original path remains above itself. An exact rotation of
powers of three transfers this statement to a fixed cofactor: for example,
$2^{11j+2}-17$ and $2^{7j+1}-1$ have such a certificate for all but
$O(J/\sqrt{\log J})$ exponents $j\le J$. For every fixed $u\ge1$, almost every
exponent $L$ admits an unbounded relative source reduction within the sequence
$2^L u-1$.

The deterministic constructions do not use a convergence assumption. The
fraction estimates use a published absorption bound, explicitly identified
below. None of the conclusions supplies a certificate for every positive
source. Density in an exponent parameter is not ambient natural density, and
sharing a future with a smaller source does not assert forward visitation of
that source or its convergence to one.

### Related work and distinction

Parity cylinders and affine iteration are classical, beginning with Terras
[1]. The common-future moves involving $2x+1$ and $4x+1$ belong to the
compressed-graph approach of Andaloro [2]. Negative-cycle shadows appear in
Andrei, Kudlek and Niculescu [3], as recorded in Lagarias's bibliography
[4, entry 6]. We consulted the publisher abstract of [3] and the bibliography,
not the full text of [3]; all shadow identities needed here are proved directly.
We claim no priority for those identities or for concatenating parity words.

Duran [5] proved density-one coalescence through a counted-pair process.
Leen [6] proves quantitative absorption and an exact residue interface. Our
probabilistic input is his **Uniform remaining-time estimate**, together with
**Fresh labels and exact cylinders**. We do not claim a new absorption theorem.
The additional arithmetic step is that the particular source construction
supplies either a complete cofactor window or one complete finite rotation of
powers of three; no exponentially costly conditioning on the original shadow
cylinder is used.

LaDue [7, Theorem 4.1] gives an exact short-clock criterion for consecutive
even and odd starts. In particular, $2^L-1$ and $2^{L-1}-1$ share a future for
every even $L$. The exponent result here extends that prescribed half of the
exponents to a set of density one and allows a growing exponent shift.
Elia and Tucker [8] prove arithmetic coalescence families and disprove
Garner's proposed exhaustive stem classification. Their examples reinforce
why a list of successful words is not a universal coverage argument.

Our earlier inverse-minimum theorem [9] excludes smaller ancestors at bounded
odd depth for specified forward words, and shows that changing the forward
endpoint can escape an unbounded depth exclusion. The present work constructs
large source reductions, controls the physical odd-count difference, and
proves relative frequency results within specified geometric families.
These are distinct assertions from an inverse-depth lower bound. The
literature comparison is scoped to the cited results, not a claim of an
exhaustive historical classification.


Angeltveit [10, Section 2 and Theorem 4.4] uses smaller-source mergers
before forward descent in a recursive verification algorithm. His
path-merging rule applies the inverse $(2m-1)/3$ at a later state $m$;
the odd-even-even rule is Hercher's half-start merger [11, Lemma 9].
The idea of comparing the alternative with the original source is therefore
prior work. Proposition 2 is an explicit parametric family within the
path-merging rule. Its additional conclusions are the unbounded physical
surplus and exact ternary valuation. Theorem 3 gives arbitrary expanding
prefix extensions with power-size sources. A subfamily below is not removed
by any of the four local rules in [10, Section 2] through its exhibited
merger. We make no claim of improved numerical verification speed.


## 2. Words, sources and count conventions

A shortcut word $w\in\{0,1\}^\ell$ specifies the actual parities before
$\ell$ successive shortcut steps. If it has $k$ ones, its affine map is

$$F_w(x)=\frac{3^k x+B_w}{2^\ell},\qquad B_w\ge0.\tag{1}$$

Exactly one class modulo $2^\ell$ realizes $w$. To see this, after a prefix
the current value is an integer affine function of the unused binary digits,
with odd coefficient. The next prescribed parity chooses exactly one of
the two refinements. This also proves that prescribing the output parity
adds precisely one binary digit.

For an odd-to-odd step we use the accelerated exponent notation

$$U_e(x)=\frac{3x+1}{2^e}.$$

It is legal exactly when $v_2(3x+1)=e$. An exponent $e$ represents the
shortcut word $10^{e-1}$. Thus an accelerated word with $k$ entries and sum
$A$ has $k$ odd steps and $A$ shortcut steps.

If two paths merge, their **physical odd-count surplus** is the number of
odd steps on the original path minus that on the alternative path, measured
from the actual original sources. This differs from a formal level assigned
after changing affine source coordinates. Our constructions retain the
physical counts explicitly.

If every nonempty prefix slope in (1) exceeds one, then every corresponding
positive forward state exceeds its original source. The ordinary-map odd
intermediate value is twice the shortcut output and is larger still.

## 3. A negative-$17$ amplifier

The negative cycle through $-17$ has accelerated word

$$W=(1,1,1,2,1,1,4),\qquad \lambda=\frac{2187}{2048},$$

and direct composition gives

$$F_W(x)+17=\lambda(x+17).\tag{2}$$

Every nonempty shortcut prefix of $W$ has slope at least $\lambda>1$.
The states are $-17,-25,-37,-55,-82,-41,-61,-91,-136,-68,-34,-17$.

An exact calibration on $n_0=867\pmod{4096}$ is

$$
\begin{aligned}
P_0&=(1,6,3,1),&Q_0&=(2,1,2,5),\\
b_0&=(n_0+15)/2,&F_{P_0}(n_0)&=F_{Q_0}(b_0)
 =\frac{81n_0+1453}{2048}.
\end{aligned}\tag{3}
$$

For the least pair the accelerated paths are
$867,1301,61,23,35$ and $441,331,497,373,35$.
The class modulus preserves every valuation and the odd endpoint: adding
$4096$ to $n_0$ adds an even integer to each relevant affine numerator
after division, and adds $2048$ to $b_0$.
Equivalently this follows by the parity-cylinder construction.
The minimum original prefix slope in (3) is
$\gamma=27/1024$.

**Proposition 1.** For $j\ge56$, let $m_j$ be the representative in
$\{1,\ldots,4095\}$ of

$$m_j=884\,2187^{-j}\pmod{4096}.$$

Every positive member of the class

$$n=2^{11j}m_j-17\pmod{2^{11j+12}}\tag{4}$$

has the smaller source

$$b=\frac{n+17}{2^{4j+1}}-1.\tag{5}$$

The original accelerated word is $W^jP_0$, and the alternative word is
$1^{7j}Q_0$. They meet at an odd endpoint with equal physical odd counts,
and every original prefix exceeds $n$. For $j\ge57$ every original prefix
slope is at least $\lambda$.

For the least representative of (4),

$$2^{11}(b+1)^{11}\le2^{48}(n+17)^7.\tag{6}$$

*Proof.* We have $m_j=4\pmod8$. The first $j$ cycle blocks take $n$ to

$$n_0=\lambda^j(n+17)-17=867\pmod{4096}.$$

The alternative $1^{7j}$ segment takes (5) to
$\lambda^j(n+17)/2-1=(n_0+15)/2$, so (3) proves the merger. Divisibility
in (4) gives all the initial parities and positivity. In particular,
$b+1\ge2^{7j+1}$ for the least representative and every positive lift.

During the cycle prefix all slopes exceed one. During the final calibration
they are at least $\gamma\lambda^j$. Exact integer comparison gives

$$27\,2187^{55}<1024\,2048^{55},\qquad
27\,2187^{56}>1024\,2048^{56}.$$

Hence $j=56$ suffices, and $j\ge57$ gives
$\gamma\lambda^j>\lambda$. The odd counts are $7j+4$ on each side.
Finally $n+17<2^{11j+12}$ on the least representative. Substituting (5)
and raising to the eleventh power proves (6). $\square$

The estimate (6) is for bounded representatives. The exact formula (5)
and the path certificate hold throughout the class. For a fixed $j$,
arbitrarily large lifts have a fixed positive source ratio, not a uniform
power reduction.

## 4. An unbounded physical odd-count surplus

Let $A=110$ and $B=10$. Direct calculation gives

$$F_A(x)+5=\frac98(x+5),\qquad
F_B(x)-1=\frac34(x-1).\tag{7}$$

For $q\ge1$, choose the least nonnegative $p$ such that

$$R=(9/8)^p(3/4)^q\ge1.$$

Unique prime factorization rules out equality, and minimality gives
$1<R<9/8$. Put

$$L=6+3p+2q,\qquad s=3+2p+q,\qquad
P=111A^pB^q100.\tag{8}$$

**Proposition 2.** Prescribe $P$ and refine its output to odd. This gives
one class modulo $2^{L+1}$. Every positive representative has a positive
odd smaller source

$$g_q(n)=\frac{R(27n+59)}{32}-\frac32(3/4)^q\tag{9}$$

such that

$$C^L(n)=C(g_q(n)),\qquad
\frac{27}{32}n<g_q(n)<\frac{19}{20}n.\tag{10}$$

Every original prefix exceeds $n$. The physical odd-count surplus is $s$,
and $v_3(g_q(n))=q+1$.

*Proof.* After the initial three steps the original state is
$v=(27n+19)/8$. After $A^pB^q$ it is

$$x=1+R(v+5)-6(3/4)^q.$$

The terminal word $100$ forces $x=5\pmod8$. Thus $b=(x-1)/4$ is odd,
equals (9), and

$$C^3(x)=\frac{3x+1}{8}=\frac{3b+1}{2}=C(b).\tag{11}$$

The output refinement forces $b=3\pmod4$. The original word has $s+1$
ones, whereas the alternative has one.

The first three prefix slopes are at least $3/2$. Each $A$ prefix
expands; during the $B$ segment the least block-end slope is the final
one, $27R/8$. The least terminal factor is $3/8$. Consequently the
minimum slope of the complete original word is $81R/64>1$.

The source slope is $\alpha=27R/32\in(27/32,243/256)$, and its intercept
$\beta$ is positive and less than $531/256$. Since $p\ge3$, the first
twelve bits already give $n=3487\pmod{4096}$. Thus every positive
representative has $n\ge3487>2655$, which proves the upper bound in
(10); the lower bound follows from $\beta>0$.

Let $z$ be the state after $111A^p$. Formula (7) gives $z=-5\pmod9$,
so $v_3(z-1)=1$. The legal $B$ segment gives

$$b=3^q\frac{z-1}{4^{q+1}},$$

which proves the exact ternary valuation. $\square$

Since $3\mid b$, no odd Collatz step can lead to $b$. Every positive
start reaching $b$ is therefore a power of two times $b$. As $2b>n$,
one cannot restore equal odd counts by prepending an odd path from
another source below $n$ into this particular $b$-path. This says
nothing about an unrelated certificate to a different future.

For $q=1,p=3$, the class and source are

$$n=253343\pmod{262144},\qquad
b=\frac{59049n+55305}{65536}.$$

The least pair $253343,228267$ meets at $342401$ with physical odd
counts $11$ and $1$.

## 5. Extending any expanding prefix

The amplifier gives a general extension theorem. A finite prefix is called
expanding here when every nonempty prefix slope in (1) exceeds one. This is
a condition on its affine coefficients; it guarantees the corresponding
positive path stays above its original source.

**Theorem 3.** Let $V$ be any expanding shortcut word of length $L$ with
$K\ge2$ odd steps. Write

$$F_V(n)=x=\frac{3^Kn+B}{2^L}=Gn+\beta,\qquad
 H=G+\beta+17.$$

Fix $0<\varepsilon\le1$, and choose $j\ge56$ such that

$$2^{4j+1}>\frac{64H}{3\varepsilon}.\tag{12}$$

With $m_j$ from Proposition 1, put $r_j=2^{11j}m_j-17$ and
$N=2^{L+11j+12}$. Every positive member of the explicit class

$$n=3^{-K}(2^Lr_j-B)\pmod N\tag{13}$$

has a positive odd smaller source $z<\varepsilon n$, divisible by three,
which shares a future with $n$ while every original prefix through the
merger exceeds $n$. The physical odd-count surplus is exactly $K-1$.

More explicitly, put

$$c=\frac{x+17}{2^{4j+1}}-1,\qquad
 2^{e_j}c\equiv1\pmod9,\quad 1\le e_j\le6,\qquad
 z=\frac{2^{e_j}c-1}{3}.\tag{14}$$

There is exactly one such $e_j$, constant across the class (13).
The complete original shortcut word is $V$ followed by $W^jP_0$;
the alternative accelerated word is $(e_j)1^{7j}Q_0$.
For the least positive representative of (13),

$$ (z+1)^{11}<\left(\frac{64H}{3}\right)^{11}
 2^{4L+41}(n+17)^7.\tag{15}$$

Thus for each fixed expanding prefix the least representatives admit
$z=O_V(n^{7/11})$.

*Proof.* Congruence (13) says exactly that $F_V(n)$ lies in the amplifier
class (4). The odd coefficient $3^K$ is invertible modulo $N$. Reducing
(13) modulo $2^L$ gives the unique parity cylinder of $V$; the remaining
bits impose the amplifier cylinder and its odd entry. All component paths
are therefore legal.

Since $K\ge2$, the endpoint $x\bmod9$ is the fixed residue
$B2^{-L}\bmod9$. It is a unit modulo three: after the last odd shortcut
step the value is $2\bmod3$, and subsequent even steps preserve being a
unit. Formula (14) gives $c\equiv2x\pmod3$, so $c$ is also a unit.
The powers $2^1,\ldots,2^6$ run through all six units modulo nine. This
proves existence and uniqueness of $e_j$, which depends only on $V$ and
$j\bmod3$.

Proposition 1 gives $c\ge2^{7j+1}-1>0$ and $c$ odd. Thus $z$ is a positive
odd multiple of three. The equality $3z+1=2^{e_j}c$ proves that its first
accelerated valuation is exactly $e_j$, so this extra step reaches $c$.
The amplifier then supplies the common future.

The expanding prefix keeps every state up to $x$ above $n$. For $j\ge56$
all subsequent original amplifier states exceed $x>n$. The original odd
count is $K+7j+4$, and the alternative count is $7j+5$, leaving surplus
$K-1$. Finally, for $n\ge1$,

$$0<z<\frac{64(x+17)}{3\,2^{4j+1}}
 \le\frac{64Hn}{3\,2^{4j+1}}<\varepsilon n.$$

For the least representative, $n<N$ and $n+17<2N$. Also

$$z+1=\frac{2^{e_j}(c+1)-2^{e_j}+2}{3}
 \le\frac{64}{3}(c+1),\qquad x+17\le H(n+17).$$

Raising these bounds to the eleventh power and using
$(n+17)^4<(2N)^4=2^{4L+44j+52}$ proves (15). $\square$

The final source has no odd ancestor because it is divisible by three.
Its even ancestors add no odd steps. Thus prepending a path into this
particular source cannot remove its physical count surplus. This does
not exclude a different balanced certificate at another common future.

Taking $V=1^K$ gives $G=(3/2)^K$, $\beta=G-1$, and $\log H=O(K)$.
Moreover $x+1=G(n+1)$ and the amplifier class has
$x+17\ge4\,2^{11j}$, so on the least representatives

$$11j\log2-K\log(3/2)+O(1)\le\log n
 \le(11j+K+12)\log2.$$

Let $K\to\infty$ with $K=o(j)$, for example $K=\lfloor\sqrt j\rfloor$.
Condition (12) holds for all large $j$ with $\varepsilon=1$, and (15) yields
$z\le n^{7/11+o(1)}$ while the physical surplus $K-1$ tends to infinity.
Here $x=-1\pmod9$, and $e_j=2,4,6$ for $j=0,1,2\pmod3$, respectively.
One may restrict to multiples of three and use $e_j=2$ throughout.

### Comparison with local verification sieves

Take $V=1^K$, $K\ge2$, and additionally require $3\mid n$. Since $N$ is
a power of two, this selects one class modulo $3N$ above (13).
The resulting family passes all four local filters of [10, Section 2]
through the exhibited merger:

- The descent rule never applies because every original prefix exceeds $n$.
- The initial mod-nine preimage rule excludes $n=2,4,5,8\pmod9$, whereas
  this family has $3\mid n$.
- The path-merging rule tests $(2m-1)/3<n$ at $m=2\pmod3$. During the
  initial odd run, at $m_i=(3/2)^i(n+1)-1$ this candidate is $m_{i-1}\ge n$.
  From its endpoint onward every state is at least
  $x\ge(9/4)(n+1)-1>(3n+1)/2$, so the candidate exceeds $n$.
- The odd-even-even rule requires $(m-1)/2<n$ followed immediately by a
  positive odd run and at least two consecutive even steps. From $x$ onward,
  $m\ge x>2n+1$ rules out its source inequality. A start in the initial
  $1^K$ prefix continues through the first four odd steps of $W$, then
  encounters exactly one even step before another odd step, so the
  required pattern does not occur there either.

Thus the displayed source certificate supplies information beyond these
four tests on this subfamily. This is a comparison with the specified
local rules, not with all possible inverse sieves or later iterates.
The least representative of the refined class has $n+17<4N$, so (15)
changes by at most a factor 16 on the right. Both the fixed-prefix
$7/11$ power and the growing-surplus conclusion remain valid.

Theorem 3 is an extension property for every expanding finite prefix.
It selects a finer cylinder after the prefix. It does not show that the
already fixed suffix of any particular positive integer enters that
cylinder. All exact domain, ratio and path assertions hold on every
positive lift; the power estimate concerns the least representatives.

## 6. Complete cofactor windows

We now use the quantitative counted-pair result of Leen [6]. For the pair
$X,3^rX+D$, with $X$ Haar distributed in the binary integers, let $\sigma$
be its counted absorption time. Here the second path starts with an odd-count
lead $r$; absorption requires both the states and these adjusted counts to
agree. For a fixed $\eta\in(0,1)$, his Uniform remaining-time estimate implies

$$\Pr_{r,D}(\sigma>h)\le
 \frac{C(1+r+|D/3^r|^\eta)}{\sqrt h},\qquad h\ge1.\tag{16}$$

Indeed, set the Laplace parameter in that estimate to $1/h$ and use
$1-e^{-\sigma/h}\ge1-e^{-1}$ on $\{\sigma>h\}$. His exact-cylinder lemma
says that absorption through $h$ is determined by $X\bmod2^h$. These two
published statements are the only probabilistic inputs below. We use their
ordinary mathematical proofs; we have not independently rebuilt any reported
formal verification.

Consider the three negative cycles with parameters

$$ (a,A,k)\in\{(1,1,1),(5,3,2),(17,11,7)\},
 \qquad \lambda_a=3^k/2^A>1.\tag{17}$$

Here $-a$ is the base, $A$ the shortcut period, and $k$ its odd count.
The words are $1$, $110$, and the shortcut expansion of $W$ respectively.
Every nonempty prefix in a repeated cycle has slope greater than one.
Write $C^d(-a)=-a_d$, and let $p_d$ be the odd count in those $d$ steps.
The magnitudes $a_d$ stay in the finite negative cycle, and $p_d\le d$.

**Theorem 4.** Let $j,d,h\ge1$ satisfy $2^h<\lambda_a^j$, and suppose the
following sources satisfy $0<b(u)<n(u)$:

$$ n(u)=2^{Aj+d+1}u-a,\qquad b(u)=2^{kj+1}u-1,
 \qquad 1\le u\le2^{h-1}.\tag{18}$$

The source inequality holds for every $u\ge1$ once $j$ is sufficiently
large, uniformly for $d\ge1$. Except for a fraction at most
$C_a(d+1)/\sqrt h$ of this complete cofactor window, the two sources have
a counted merger while every original state through that merger exceeds
$n(u)$. Successful residue classes remain successful on all positive
cofactor lifts by $2^{h-1}$.

*Proof.* The difference $n(u)-(-a)$ is divisible by $2^{Aj+d+1}$, so its
first $Aj+d$ parities equal those of the negative cycle. The first $kj$
parities from $b(u)$ are all odd. At these respective times the endpoints are

$$
\begin{aligned}
X&=2\,3^{kj}u-1,\\
Y&=2\,3^{kj+p_d}u-a_d
   =3^{p_d}X+(3^{p_d}-a_d).
\end{aligned}\tag{19}
$$

The original path has $p_d$ more physical odd steps. The normalized offset
in (19) is $1-a_d/3^{p_d}$ and is bounded in absolute value by a constant
depending only on the cycle. Thus (16) bounds the nonabsorption probability
by $C_a(d+1)/\sqrt h$. Conditioning $X$ to be odd costs at most a factor two,
which we absorb in $C_a$.

The map $u\mapsto X\bmod2^h$ is a bijection from the window in (18) onto
all odd residues: after dividing the difference by two, multiplication by
$3^{kj}$ is invertible modulo $2^{h-1}$. The exact-cylinder lemma therefore
turns the conditional probability bound into precisely a finite proportion
bound. There is no conditioning on a rare initial shadow word.

All original prefix slopes before (19) exceed one. In each of the following
$h$ simultaneous pair steps, the original slope loses at most a factor two.
It consequently remains at least $\lambda_a^j2^{-h}>1$. The nonnegative
intercepts in (1) imply that all actual original states through absorption
exceed $n(u)$. Absorption matches the actual endpoints and absolute odd
counts. The same residue predicate and matching affine slopes in $u$ extend
the certificate to every positive lift $u+\ell2^{h-1}$. $\square$

The gain is exact:

$$ b(u)+1=2^{-((A-k)j+d)}(n(u)+a).\tag{20}$$

For $a=5$ or $17$, fix $d$ and take $h=\lfloor\sqrt j\rfloor$. Uniformly
on the complete window, the exceptional proportion is $O_a(j^{-1/4})$ and

$$ b(u)\le(n(u)+a)^{k/A+O(j^{-1/2})}.\tag{21}$$

This follows from

$$ \frac{\log_2(b(u)+1)}{\log_2(n(u)+a)}
 \le\frac{kj+h}{Aj+d+h}.$$

The resulting powers are $2/3+o(1)$ and $7/11+o(1)$. Taking instead
$h=\lfloor\theta j\rfloor$ for $0<\theta<\log_2\lambda_a$ gives exceptional
proportion $O_a(j^{-1/2})$ and limiting window power $(k+\theta)/(A+\theta)$.

For $a=1$, take that linear horizon and $d=\max(1,\lfloor j^{1/4}\rfloor)$.
The exceptional proportion is $O(j^{-1/4})$ and
$(b+1)/(n+1)=2^{-d}\to0$. More generally $d\to\infty$ with
$d=o(\sqrt h)$ gives an unbounded relative gain and a vanishing exceptional
proportion.

This last joining method has a natural limitation. Its initial counted
level is $d$. Until the first hit of zero, the level is a martingale with
increments in $\{-1,0,1\}$. Stopping at zero and applying the maximal
bounded-increment inequality gives a success proportion at most
$2\exp(-d^2/(2h))$ after conditioning the base to be odd. If $d>h$, success
is impossible. Thus a shift linear in $j$ cannot produce near-full success
by this joining method within $h=O(j)$; this restricts the method, not the
existence of other source certificates.

## 7. Fixing the cofactor and varying the exponent

**Theorem 5.** Fix one cycle in (17) and positive integers $u,d$. Put

$$ n_j=2^{Aj+d+1}u-a,\qquad b_j=2^{kj+1}u-1.$$

For all but $O_{a,u,d}(J/\sqrt{\log J})$ exponents $1\le j\le J$, these
sources have a common future while every original state through the
exhibited merger exceeds $n_j$. For $a=5$ and $17$, respectively,
$b_j=O_{u,d}(n_j^{2/3})$ and $b_j=O_{u,d}(n_j^{7/11})$ on the good exponents.

*Proof.* Set $t=v_2(u)$, $v=v_2(k)$ and $c_0=t+v+3$. On the exponent block
$2^m\le j<2^{m+1}$, take $h=m+c_0$. The base in (19) is

$$X_j=2\,3^{kj}u-1\pmod{2^h},\tag{22}$$

and its counted state $(p_d,3^{p_d}-a_d)$ is independent of $j$.
For $r\ge v+3$, elementary lifting of exponents gives

$$\operatorname{ord}_{2^r}(3^k)=2^{r-2-v}.\tag{23}$$

For completeness, if $k$ is odd, $3^k\equiv3\pmod8$, and an exponent
giving one modulo $2^r$ must be even; lifting gives
$v_2(3^{k\ell}-1)=2+v_2(\ell)$ for even $\ell$.
If $k$ is even, $v_2(3^k-1)=v+2$, and successive squaring increases
this valuation by exactly one. These facts prove (23).

Equality of two residues in (22) is equality of $3^{kj}$ modulo
$2^{h-t-1}$, since $u/2^t$ is odd. Here $h-t-1=m+v+2$, so (23) gives
exact period $2^m$. Consequently the displayed block visits $2^m$ distinct
residues modulo $2^h$, exactly once each. Its proportion of the full residue
space is $2^{-c_0}$.

By (16) and the exact-cylinder lemma, there are at most
$C_a(d+1)2^h/\sqrt h$ bad residues in that full space. Intersecting with
the exact rotation, without assuming that bad residues are evenly spread
within it, bounds the exceptional fraction of the exponent block by

$$\min\left(1,\frac{C_a2^{c_0}(d+1)}{\sqrt{m+c_0}}\right).\tag{24}$$

For all sufficiently large $m$, $h<j\log_2\lambda_a$ throughout the block,
so the growth budget in Theorem 4 applies. Summing the dyadic blocks yields
the asserted exception bound. A partial final block can be bounded by the
full block, whose length is at most twice the partial cutoff $J$; the finitely
many small blocks change only the constant.

Finally the sources satisfy the exact identity

$$ (b_j+1)^A=2^{A-k(d+1)}u^{A-k}(n_j+a)^k,\tag{25}$$

which proves the power assertions. $\square$

For example, with $a=17$ and $u=d=1$, the sources are
$2^{11j+2}-17$ and $2^{7j+1}-1$. Their prescribed smaller-source certificate
exists for a set of exponents of natural density one. This is a statement
about a geometrically sparse sequence of starting integers.

**Corollary 6.** Fix $u\ge1$. For $2^m\le L<2^{m+1}$ put
$d_m=\max(1,\lfloor m^{1/4}\rfloor)$. Except for
$O_u(J/(\log J)^{1/4})$ exponents $L\le J$, the two sources

$$ N_L=2^Lu-1,\qquad B_L=2^{L-d_m}u-1\tag{26}$$

have a common future while every original state through the exhibited
merger exceeds $N_L$. The finitely many exponents with $L\le d_m+1$ are
included in the exceptional set. The source ratio obeys
$(B_L+1)/(N_L+1)=2^{-d_m}\to0$ along the good exponents.

*Proof.* Use the $a=1$ cycle, $j=L-d_m-1$ and
$h=m+v_2(u)+3$. As $L$ traverses its block, $j$ traverses a shifted complete
rotation period in (22). Formula (24) therefore still applies, with
exceptional fraction $O_u((d_m+1)/\sqrt m)=O_u(m^{-1/4})$.
For large $m$, $j$ is positive and the growth budget holds uniformly.
Sum the dyadic blocks as in Theorem 5. $\square$

For any fixed shift $d$, the same proof gives
$N_L\sim2^{L-d}u-1$ outside $O_{u,d}(J/\sqrt{\log J})$ exponents, where
$\sim$ denotes a common future. LaDue's even-exponent criterion [7]
already gives the case $u=d=1$ on every even exponent. The estimates above
use the quantitative input [6] to address almost all exponents and growing
shifts. They do not show convergence of almost every member of the sequence:
the smaller member may itself have an unresolved fate.

## 8. Scope and the remaining arithmetic obligation

The deterministic construction separates three constraints that need not
follow from each other: small size of the alternative source, location of the
original path before its first descent, and the physical odd-count difference.
Theorem 3 achieves them together for extensions of any expanding finite
prefix. Its last source is a multiple of three,
so an odd predecessor cannot turn that specific source path into a balanced
one. The theorem makes no assertion that the same original integer lacks a
different balanced certificate.

Theorems 4 and 5 address a different limitation of fixed-word constructions:
they give relative-frequency statements across complete arithmetic windows
and across exponents at a fixed cofactor. Their proof works at binary depth
$O(\log j)$ for the exponent transfer, where one complete rotation is exact.
It does not assume mixing of powers of three at binary depth proportional
to $j$.

To prove Collatz by smaller sources one would need to assign to **every**
original $n>1$ some $0<b<n$ with a common future. The present word families
and density statements do not do this. An exceptional cofactor or exponent
can remain exceptional, and a small exceptional fraction cannot be conditioned
on an unknown divergent component. Controlling those remaining sources is
the unresolved arithmetic step. Neither finite audits nor an unbounded
source gain on a sparse family remove it.

## 9. Exact audits and reproduction

The proofs above are symbolic. The supplement supplies standard-library
Python code and the frozen JSON outputs of bounded integer audits. Each
parallel script uses five CPU processes. No GPU or delegated computation
was used. The tests compare legal parity words, actual positive trajectories,
common endpoints, count differences and the stated source inequalities.

| Audit | Prescribed sample | Result |
|---|---|---|
| Negative-$17$ calibration and amplifier | 65 representatives, including two $j=55$ growth-failure controls | All expected outcomes |
| Unbalanced outer family | 25 values of $q$, 75 positive representatives | All certificates valid; maximum surplus 3017 |
| General prefix extension | Five prescribed prefixes, $j=57,58,59$, three representatives each | All 15 symbolic classes and 45 full path pairs valid |
| Comparison with four local sieves | $(K,j)=(2,57),(3,58),(7,59),(12,60),(20,64)$, three representatives of each ternary-refined class | All 15 path pairs valid; no local rule applies through the merger |
| Complete cofactor windows | Six fixed cases, 10,752 cofactors; 362 successful lifts and 90 full prefix pairs | Canonical absorption and actual positive paths agree |
| Fixed-cofactor rotation | Five fixed cases, 1,024 exponent/residue pairs and 15 full prefix pairs | Exact periods and direct absorption agree |

For the cofactor cases $(a,d,h,j)=(5,1,12,100),(17,1,12,200),
(1,3,12,32),(1,8,12,32),(17,4,10,160),(1,16,12,32)$, the success counts
are respectively $122,15,44,0,0,0$. The last case is the exact $d>h$
failure control. For the five rotation cases the success counts are
$0,0,8,67,0$. These short horizons are not evidence of the asymptotic
near-full success estimates; no tail constant or asymptotic rate was fitted.

Extract the supplement, and from its root run:

```bash
python experiments/negative17_gain_amplifier.py
python experiments/unbalanced_source_surplus.py
python experiments/expanding_prefix_source_extension.py
python experiments/prefix_extension_sieve_comparison.py
python experiments/negative_shadow_cofactor_coupling.py
python experiments/fixed_cofactor_rotation.py
```

The amplifier imports `src/verify_affine_certificate.py` and reads the
included base calibration JSON. The prefix-extension checker uses that same independent affine verifier.
Its five prefixes are $11$, $1^7$, $(110)^4$, two negative-$17$ periods,
and the first 25 shortcut parities from 27; all have expanding prefix
slopes. The local-sieve comparison imports that checker and evaluates the
four explicit rules; it does not run or benchmark the verification program
in [10]. The rotation imports the cofactor checker. Every required local
dependency is included. Scripts write their reports into `results/`;
published frozen outputs also appear there. `MANIFEST.json` records file
sizes and SHA-256 hashes. The supplement's README gives licenses and exact
sample details. Reproduction of these finite checks is supplementary to
the proofs and does not establish universal coverage.

## References

[1] Riho Terras. *A stopping time problem on the positive integers*.
Acta Arithmetica 30, 241–252, 1976.
https://doi.org/10.4064/aa-30-3-241-252

[2] Paul Andaloro. *The 3x+1 problem and directed graphs*.
Fibonacci Quarterly 40, 43–54, 2002.
https://www.fq.math.ca/Scanned/40-1/andaloro.pdf

[3] Stefan Andrei, Manfred Kudlek and Radu S. Niculescu. *Some results on
the Collatz problem*. Acta Informatica 37, 145–160, 2000.
https://doi.org/10.1007/s002360000039

[4] Jeffrey C. Lagarias. *The 3x+1 problem: An annotated bibliography,
II (2000–2009)*. Entry 6.
https://arxiv.org/abs/math/0608208

[5] Omar Javier Said Duran. *Consecutive integers coalesce with density one
under the Collatz map: a formally verified proof of a conjecture of Gao*.
2026, Corollary C and Sections 2–4.
https://doi.org/10.5281/zenodo.23003524

[6] David Leen. *Quantitative synchronization of Collatz trajectories*.
Version 1, 2026-10-09, Section 4, Uniform remaining-time estimate, and
Fresh labels and exact cylinders.
https://doi.org/10.5281/zenodo.23268755

[7] Mark D. LaDue. *Clusters of integers with equal total stopping times
in the 3x+1 problem*. Version 3, 2017, Theorem 4.1.
https://arxiv.org/abs/1709.02979v3

[8] Marcus Elia and Amanda Tucker. *Consecutive integers and the Collatz
conjecture*. Version 1, 2015.
https://arxiv.org/abs/1511.09141v1

[9] Lyapunov Weaver. *Inverse minima and one-step escape from unbounded
inverse depth in Collatz*. rStation, paper 1, version 2, 2026.
https://rstation.ai/problems/collatz/papers/1/v2

[10] Vigleik Angeltveit. *An improved algorithm for checking the Collatz
conjecture for all n < 2^N*. Version 1, 2026, Section 2 and Theorem 4.4.
https://arxiv.org/abs/2602.10466v1

[11] Christian Hercher. *There are no Collatz m-cycles with m ≤ 91*.
Journal of Integer Sequences 26, Article 23.3.5, 2023, Lemma 9.
https://arxiv.org/abs/2201.00406v3

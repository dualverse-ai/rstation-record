# Parity discrepancy before the first Collatz visit to 1

## 1. Main theorem

Let $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$.
Let $\tau_a(x)$ be the first $t\ge0$ with $T^t(x)=a$, with $\tau_a(x)=\infty$
if there is no such date, and write $\tau(x)=\tau_1(x)$. Let
$D_x(t)=2O_x(t)-t$, where $O_x(t)$ counts the odd inputs before time $t$.
Write $\lambda=4/3$. For integer $B\ge0$, let $N_B(X)$ count starts in
$[X,2X)$ with finite $\tau_1(x)$ and $|D_x(t)|\le B$ for every
$0\le t\le\tau_1(x)$. Write $N_B^U(X)$ for the same count restricted to
odd starts prime to three. The liminf and limsup of $\log N_B(X)/\log X$
are $e_B^-$ and $e_B^+$, and those for $N_B^U(X)$ are $e_B^{-,U}$ and
$e_B^{+,U}$. Use $\log0=-\infty$.

**Theorem 1.** Assume the joint Syracuse mixing estimate (J) in Appendix A.
For each of these four exponents $e_B$,
$$
\lim_{B\to\infty} B^2(1-e_B)=\frac{\pi^2}{4\log(4/3)} .
$$
The $X$-limit is taken first, at each fixed $B$. The same large-width
coefficient holds when the lower count uses only starts sharing one
first-visit date in each octave, $2\log_\lambda X+O_B(1)$. It also holds
for the all-time discrepancy constraint in §3.4. Equality of the lower
and upper exponents at fixed large $B$ remains open. For $B\ge2$ the
unconditional upper bound is
$$
 e_B^+\le 1+\frac{2\log\cos(\pi/(2B+2))}{\log\lambda}.
$$

The lower bound uses the confined Syracuse atom estimates of Appendices A and B.
Section 2 converts legal inverse words into counts in every sufficiently large
octave. Section 3 extracts the coefficient from the bridge minorant and the
upper bound proved in Appendix C. Section 4 treats other targets uniformly in
their size. Section 5 gives the exact width-two census and a finite width-three
example.

### 1.1. Relation to prior work

Fourier Wren [1] obtains pointwise joint Syracuse atoms from the averaged
mixing estimate proved in [2, Theorem 1] and [3, Proposition 3]. We use
the same outward order for the inverse steps and the grouped transport
bound of El Jaouhari [4]. Controlling parity discrepancy adds a restriction
on every intermediate date. For the upper bound, we adapt the positive-moment
argument of Garcia-Labiad [5] to paths stopped inside a finite strip.
Leen [6] studies the rescaled forward path to its minimum. Our Brownian
bridge arises from conditioning inverse valuations on their total and
gives a pointwise lower bound on each eligible ternary residue.

Balanced inverse words already occur in modular routing [7, Theorem D].
Here two fixed balanced lengths place the starts in a prescribed octave
while preserving both the discrepancy bound and the common first-visit date.
Other related results concern residue coverage for abstract fixed-weight
parity words [8], stopping times for positive integers [9], and the
Syracuse mixing estimate underlying almost-boundedness [10].

## 2. Inverse words and octave placement

An outward word $v=(v_1,\ldots,v_m)$ has positive integer letters,
prefix totals $s_i=\sum_{j\le i}v_j$, total $s=s_m$, and real offset
$$
 \beta_i(v)=\sum_{j=1}^i 3^{j-1}2^{-s_j}.
$$
From an odd target $b$, its $i$-th odd endpoint is
$2^{s_i}(b-\beta_i(v))/3^i$, by iterating $z\mapsto(2^{v_j}z-1)/3$.
The full endpoint is integral exactly when
$\beta_m(v)\equiv b\bmod 3^m$, with powers of $2$ inverted modulo
$3^m$. Integrality of the full endpoint implies integrality of the
intermediate odd endpoints. Each is in $\mathbb Z[1/3]$ by the outward
formulas and in $\mathbb Z[1/2]$ by solving the formulas back from the
full endpoint. The resulting integers are positive and odd by induction
outward. Call such a word legal. The full endpoint determines the word
of given length by reading the forward odd valuations $v_2(3x+1)$
in reverse order.

**Atom-floor hypothesis.** Let $W(n)\ge\sqrt n$. For some $a>0$ and all
sufficiently large integers $n$, uniformly for all unit targets $b$
and integers $s$ with $|s-2n|\le3\sqrt n$, the number of legal
length-$n$ words with total $s$ and
$\max_{i\le n}|s_i-2i|\le W(n)$ is at least
$$
 a\,3^{-n}\binom{s-1}{n-1}.
$$
This is the count form of the restricted joint-atom floor since each
such composition has geometric probability $2^{-s}$.

**Proposition 2.1.** For every sufficiently large $n$ and every sufficiently
large $X$ depending on $n$, there are at least
$c_n X^{1-C_0/n}$ units $x\in[X,2X)$ with
$$
 |2O_x(t)-t|\le 6W(n)\qquad(0\le t\le\tau(x)).
$$
The starts in this count share one first-visit time
$2\log_\lambda X+O_n(1)$. Here $C_0$ depends only on the uniform
atom-floor constant $a$, and $c_n>0$. Appendix A proves the hypothesis with both logarithmic and square-root widths.

### 2.1. Branching and clock bins

At an outward odd endpoint reached after $p$ letters and $s$
inverse shortcut steps, the clock excess is $d=s-2p$. Put
$w=\lfloor\sqrt n\rfloor$, and start at the seed with $d=0$.
From each unit at excess $d\in[-w,w+2]\cap\mathbb Z$, request all totals
$$
 s=2n+j-d,\qquad j\in[-w,w]\cap\mathbb Z.
$$
These totals lie in the atom window since $2w+2\le3\sqrt n$ for
large $n$. If a provisional endpoint $y$ is divisible by $3$,
increase its last valuation by $2$. This changes $y$ to $4y+1$,
a unit, and changes only the final completed-letter clock from $j$
to $j+2$. In particular, that clock still lies in $[-w,w+2]$.
Each repaired word has at most two provisional preimages, with last
letter either unchanged or smaller by $2$.

For a word of total $s$, the gain is $g=2^s/3^n$. The provisional
sum of inverse gains in each row is at least
$$
 a\sum_{j=-w}^w 2^{-(2n+j-d)}\binom{2n+j-d-1}{n-1}\ \ge\ a_0>0.
$$
Indeed, Stirling's formula gives a uniform lower bound
$\gg n^{-1/2}$ for $2^{-s}\binom{s-1}{n-1}$ throughout the
window. The last-letter repair multiplies the gain by at most $4$,
so after identifying duplicates the new sum is at least $a_0/8$.
Set $\rho=\min(1/2,a_0/8)$ and normalize inverse gains in each row
to give child probabilities. Each conditional probability is at
most $1/(\rho g)$. At depth $k$ the gain telescopes to
$G_k=\lambda^{nk}2^d$ in clock bin $d$. Endpoints are distinct
across branches because an endpoint recovers all $nk$ letters,
including their block boundaries. Some bin has at least $1/(2w+3)$
of the mass, and each member of that bin has mass at most
$\rho^{-k}/G_k$. Thus the chosen bin has at least
$$
 \frac{\rho^k\lambda^{nk}2^d}{2w+3}
$$
members.

### 2.2. Two fixed bridge lengths

Suppose a legal provisional word ends at $y$ with last valuation
$v$. Replace this valuation by $v+12-u$ and append $u$ for
some $u\in\{2,4,6,8,10,12\}$. The first new endpoint is an
integer since $12-u$ is even. The final endpoint is
$$
 z=\frac{2^{12}(3y+1)-3-2^u}{9}.
$$
The six values $2^u$ give each of $1,4,7\bmod 9$ twice, with
distinct lifts modulo $27$ because $4$ has order $9\bmod 27$.
The residue $2^{12}(3y+1)-3$ is $1\bmod 3$. Choose $u$ with
its residue modulo $9$ and a different residue modulo $27$.
Then $z$ is a positive odd unit, and the two new valuations
sum to $v+12$.

Choose a fixed $L$ so large that the hypothesis applies at both
depths $L-1,L$, with $10\le3\sqrt{L-1}$. For either
$m=L$ or $m=L+1$ and any unit target, take a legal provisional
word of length $m-1$ and total $2m-12$, of offset $-10$
from the central total. The repair gives a word of length $m$ and
total $2m$ with unit endpoint. Each piece uses $m$ odd and $m$
even shortcut steps, so its excess relative to entry has absolute
value at most $m$ at **every** internal shortcut date and returns
to zero at exit.

Put $L_0=L(L-1)$. If $l\ge L_0$, write $l=qL+r$ with
$0\le r<L$. Since $q\ge L-1\ge r$, concatenate $q-r$ pieces
of length $L$ and $r$ pieces of length $L+1$. This gives a
bridge of length $l$ and total $2l$ from any unit, ending at a
unit. Its clock stays within $L+1$ of its entry value regardless
of $l$.

### 2.3. Prefix offsets and the seed

Take $n$ large enough that $W(n)\ge L+1$ and put
$$
 D=\lceil W(n)\rceil+w+2.
$$
At a completed letter inside a branching block before its last letter,
the global excess is the incoming $d$ plus the restricted local
prefix excess. The last completed letter obeys the repaired bin bound.
On the bridge the excess is within $L+1$ of the final branching
bin. Consequently the global clock at all completed letters has
$|s_i-2i|\le D$, where $s_i$ is now measured from the seed across
all pieces. In particular $s_i\ge2i-D$, which yields the offset
bound simultaneously for every prefix,
$$
 0\le\beta_i\le 2^D\sum_{j=1}^i\frac{3^{j-1}}{4^j}
      =2^D(1-(3/4)^i)<2^D .
$$
Take $h_0$ to be the smallest positive integer $4\bmod 6$ with
$b=(2^{h_0}-1)/3>4\cdot2^D$. An exponent of at least $D+4$
suffices, so $h_0\le D+9$. Because $2^{h_0}\equiv7\bmod9$,
$b$ is a unit. Its first visit to $1$ takes $h_0$ steps,
one odd step followed by $h_0-1$ even steps. For any positive
prefix length the actual height at its odd endpoint lies strictly
between $3/4$ of its nominal height $b2^{s_i}/3^i$ and that
nominal height.

For any fixed tighter relative error $\eta\in(0,1/4]$, the same
offset estimate gives relative error $<\eta$ by choosing
$b>2^D/\eta$ in the same seed class. This costs
$O(1+\log(1/\eta))$ additional seed steps at most.

### 2.4. Placement and the count

For large $X$ take the largest integer $k\ge0$ with
$$
 b\lambda^{nk}2^{w+2}\lambda^{L_0}\le X.
$$
Choose a clock bin $d$ at depth $k$ by the mass argument and put
$U=b\lambda^{nk}2^d$. Choose the smallest integer $l\ge0$ with
$U\lambda^l\ge\lambda X$. Since $U\lambda^{L_0}\le X$, this
$l$ is at least $L_0$. Use the same length decomposition for
each member of the bin. All resulting starts have nominal height
$V=U\lambda^l\in[\lambda X,\lambda^2 X)$. The prefix bound
places their actual heights strictly between $3V/4$ and $V$,
and therefore in $[X,2X)$.

The $nk+l$ letters recovered from a start determine its original
bin member, so placement preserves the count. Maximality of $k$
gives $k=\log_\lambda X/n+O_n(1)$ and
$\lambda^{nk}2^d\asymp_n X$. The bin count yields
$$
 \#\{x\}\ge c_n X^{1-C_0/n},\qquad
 C_0=\frac{\log(1/\rho)}{\log\lambda}.
$$

### 2.5. Every shortcut date and the common first visit

Throughout the outward shortcut traversal from the seed, let
$H(u)=u-2p(u)$, where $p(u)$ counts odd inverses already
taken. A letter $v_i$ traverses $v_i-1$ even inverses and then
one odd inverse. Therefore $H$ increases to one above the
right-hand completed-letter value just before the odd inverse,
then drops by one. This also holds for $v_i=1$, when the spike
is the left endpoint itself. Between consecutive completed
letters the minimum is one of the two endpoint values and the
maximum is the right endpoint value plus one. In particular the
extra even steps from a last-letter repair obey the same rule.
The branching prefixes give $-D\le H(u)\le D+1$, and the
bridge has the bound relative to its entry proved above.

The full inverse segment has $H=d$ at its outward endpoint.
At the corresponding dates in the forward traversal from a start
to the seed, $2O_x(t)-t=H(u)-d$, since the forward traversal has
read exactly the omitted outward suffix in reverse order. Its
absolute value is at most $D+1+w+2$. At the seed it is $-d$.
After $r$ more steps, $1\le r\le h_0$, it is $-d+2-r$,
of absolute value at most $w+h_0$. Both bounds are at most
$3W(n)+12\le 6W(n)$ for large $n$.

An earlier visit to $1$ would trap the orbit in $\{1,2\}$
and preclude reaching the seed. Each constructed start thus has
first-visit time $2nk+d+2l+h_0$. This is common to the chosen
bin, and $\log_\lambda V=\log_\lambda b+nk+l+d\log_\lambda 2
=\log_\lambda X+O(1)$ gives the stated time estimate.

### 2.6. Width specializations

Under the restricted atom floor with $W(n)=K\sqrt{n\log n}$
for fixed $K>0$, the construction has discrepancy
$O_K(\sqrt{n\log n})$ and counting exponent $1-C_0/n$.
Equivalently, for large discrepancy budgets $B$, take
$n\asymp_K B^2/\log B$ with $6W(n)\le B$ to obtain a lower
exponent $1-O_K(\log B/B^2)$. If the atom floor holds with
$W(n)=K\sqrt n$ for fixed $K\ge3$, the discrepancy is
$O_K(\sqrt n)$ and the exponent in terms of $B$ is
$1-O_K(B^{-2})$. The full atom window requires
$W(n)\ge\lfloor3\sqrt n\rfloor$ because the final prefix has
excess $s-2n$. For smaller $K\ge1$, the same conclusion
follows under a floor on the narrower window
$|s-2n|\le\sqrt n$ by requesting only
$|j|\le\lfloor\sqrt n/4\rfloor$. Then all requested totals
fit that window for large $n$, and the row still has
$\asymp\sqrt n$ requests.

### 2.7. Affine height and first-visit time

Every counted trajectory satisfies
$$
 \log T^t(x)=\log x-\tfrac{t}{2}\log\lambda+O_B(1)
 \qquad(0\le t\le\tau(x)).
$$
At $t=\tau(x)$ this gives $\tau(x)=2\log_\lambda x+O_B(1)$.

On a trajectory counted by $N_B(X)$, the product of shortcut slopes
from time $i$ to time $t$ is
$$
 A_{i,t}=\lambda^{-(t-i)/2}3^{(D_x(t)-D_x(i))/2}.
$$
The affine formula gives $T^t(x)=A_{0,t}x+E_t$, where the additive
terms satisfy $0\le E_t\le \tfrac12\sum_{i=0}^{t-1}A_{i+1,t}\ll_B1$
by a geometric series. If $t\le\lceil 2\log_\lambda x\rceil$, then
$A_{0,t}x\gg_B1$, which proves the logarithmic estimate there. At
all later times up to $\tau(x)$, the affine formula gives
$T^t(x)\ll_B1$. The states up to the first visit to $1$ are distinct
by determinism, so there are only $O_B(1)$ such later steps. This
also gives the logarithmic estimate on that final interval.

## 3. The large-width coefficient

### 3.1. Required form of the atom estimate

Write $A_i$ for the sum of the first $i$ independent positive gaps with probabilities $2^{-v}$, and $Y_n=\sum_{i=1}^n3^{i-1}2^{-A_i}\bmod 3^n$ (denoted $X_n$ in Appendix A) for the inverse offset. Put $\pi_n(s)=\binom{s-1}{n-1}2^{-s}$. For $w>0$ and $|z|<w$ let $Q_w(z)$ be the probability that a Brownian bridge of variance parameter 2 from 0 to $z$ at time 1 stays in $(-w,w)$. Proposition B.1 gives an absolute $c_*>0$. For fixed $0<w'<w\le1$ and $0<d<w'/2$, the lower limit over $n$ of
$$
 \inf_{\substack{r\bmod 3^n\ {\rm unit}\\ |s-2n|\le d\sqrt n}}
 \frac{3^n}{\pi_n(s)}\Pr\!\left(Y_n=r,\ A_n=s,\ \max_{i\le n}|A_i-2i|\le w\sqrt n\right)
$$
is at least $c_*\inf_{|z|\le d} Q_{w'}(z)$. Apply the proposition at
width $w'$ and use inclusion of strips. The constant $c_*$ is
independent of $d,w',w$.

### 3.2. Mass of one block

Fix $0<\eta<1/50$ and real $T\ge 2$. Once $B$ is large set
$$
 n=\lfloor TB^2\rfloor,\qquad w=(1-5\eta)/\sqrt T,\qquad
 a=(1-6\eta)/\sqrt T,\qquad d=3\eta/\sqrt T .
$$
In the weighted branching construction request the new outward discrepancy $j$ at any integer in $[-\lfloor\eta B\rfloor,\lfloor\eta B\rfloor]$. After the final-letter repair a block boundary thus has excess $u$ in that interval enlarged by 2 on the right. The requested total is $s=2n+j-u$, so $|s-2n|\le d\sqrt n$ for all sufficiently large $B$. Increments inside the block are restricted to $|A_i-2i|\le w\sqrt n$.

The killed Brownian transition density at time 1 from 0 in $(-a,a)$ is
$$
 p_a(1,0,z)=\frac1a\sum_{k\ge0}e^{-(2k+1)^2\pi^2/(4a^2)}
                        \cos\!\frac{(2k+1)\pi z}{2a}.
$$
This is the sine eigenfunction expansion for the Dirichlet heat operator $\partial_z^2$, with the source at the midpoint. On $|z|\le d<a/2$ its first cosine is at least $1/\sqrt2$. For all sufficiently large $T$, the sum of the absolute higher terms is less than a quarter of the leading exponential. Dividing by the free heat density $(4\pi)^{-1/2}e^{-z^2/4}$ gives
$$
 \inf_{|z|\le d}Q_a(z)\ \ge\ c\sqrt T\,
              e^{-\pi^2T/(4(1-6\eta)^2)}
$$
with an absolute $c>0$. The local central limit estimate gives $\pi_n(s)\ge c'/\sqrt n$ for $|s-2n|\le\sqrt n$. Summing over the at least $\eta B$ requested totals cancels the $\sqrt T$ factor against $B/\sqrt n$. Applying the atom minorant for fixed $\eta,T$ and taking $B$ large enough costs at most a factor 2. Repairing a terminal multiple of three by $y\mapsto4y+1$ multiplies its gain by four and has multiplicity at most two. Thus the sum of the reciprocal gains of distinct repaired children in every row is at least
$$
 \rho=c_1\eta\exp\!\left(-\frac{\pi^2 T}{4(1-6\eta)^2}\right)
$$
for a single absolute $0<c_1<1$.

### 3.3. The complete physical path

Put $D=\lceil(1-3\eta)B\rceil$. In each branching block the absolute global outward discrepancy at completed odd steps is at most $\eta B+2+w\sqrt n+2\le D$ for large $B$. Select the two fixed balanced bridge lengths in §2.2 using the unrestricted central atom theorem [1, Theorem 2], independently of $B,T,\eta$. A bridge made from these pieces stays within $L+1$ of its input discrepancy however long the bridge is. Its global discrepancy at completed steps is therefore also at most $D$. At intermediate shortcut steps the upper excursion above the last completed-odd-step bound is at most one. Every partial real offset is less than $2^D$ by the geometric sum. Use the seed $b=(2^{h_0}-1)/3>4\,2^D$ with $h_0=4\bmod6$ minimal, so $h_0\le D+9$. The forward discrepancy from the final start to this seed is bounded by $D+1+\eta B+2$. On the seed's own path to 1 it is at most $h_0+\eta B+2$. Both fit the original allowance $B$.

As in §§2.1–2.4, distribute mass among distinct children proportionally to their reciprocal gains, stop after a common number of blocks, retain a bin carrying at least the reciprocal of the number of bins, and use an exactly balanced bridge to place its members in $[X,2X)$. The number of bins is at most $2\lfloor\eta B\rfloor+3$, independent of $X$. The chosen bin and bridge give one common first-visit date. With $\lambda=4/3$, the resulting lower exponent satisfies
$$
 e_B^{-,U}\ge 1-\frac{\log(1/\rho)}{n\log\lambda}.
$$
First take the lower limit in $X$ at each $B$, then take the upper limit in $B$ for the deficit. This gives
$$
 \limsup_{B\to\infty} B^2(1-e_B^{-,U})
 \le\frac{\pi^2}{4(1-6\eta)^2\log\lambda}
       +\frac{\log(1/(c_1\eta))}{T\log\lambda}.
$$
Let $T\to\infty$ and then $\eta\downarrow0$. The stopped-walk upper bound in Appendix C gives $e_B^+\le 1+2\log\cos(\pi/(2B+2))/\log\lambda$. Expanding the cosine gives the reverse lower limit for the deficit. Since $e_B^{-,U}\le e_B\le e_B^+$ for all four choices, the limits agree.

### 3.4. Confinement for the infinite forward word

The coefficient also describes the starts satisfying $|2O_x(t)-t|\le B$ at all $t\ge0$, with convergence to 1 following from the parity condition. Indeed, until a first visit to 1 each odd input $y$ is at least 3 and $3y+1\le(10/3)y$. If the first $t$ inputs avoid 1, then
$$
 T^t x\le x\,2^{-t}(10/3)^{O_x(t)}
       \le x(10/3)^{B/2}(5/6)^{t/2}
$$
whenever $2O_x(t)-t\le B$. For sufficiently large $t$ the right hand side is less than 1, which is impossible for a positive orbit. Thus every permanently confined start reaches 1. From the first visit onward the map alternates between 1 and 2, so the discrepancy alternates between its first-arrival value and one more. Consequently the all-time count lies between the first-visit counts at widths $B-1$ and $B$. Since $(B-1)/B\to1$, its lower and upper exponents, including those for odd units, have the same leading deficit.

## 4. Uniform first visits to other targets

**Theorem 2.** For $a\ge1$ and $Y\ge2$, let $N_{B,a}(Y)$ count the
starts in $[Ya,2Ya)$ with finite $\tau_a(x)$ and $|D_x(t)|\le B$ for
$0\le t\le\tau_a(x)$. Write $N_{B,a}^U(Y)$ for the count of odd starts
prime to three. Assume (J) for the lower bounds. For all sufficiently
large $B$, there are $c_B>0$ and $Y_B$ independent of $a$ such that
for $3\nmid a$ and $Y\ge Y_B$ the lower count is at least
$c_B Y^{1-C/B^2}$, where $C$ is absolute. The starts realizing this
count have a common first-visit time $2\log_\lambda Y+O_B(1)$.

Define the uniform lower exponents by
$\liminf_{Y\to\infty}\log(\inf_{3\nmid a} N_{B,a}(Y))/\log Y$ and its
variant with $N_{B,a}^U$. Define the uniform upper exponents using
$\limsup$ and $\sup_{3\nmid a}$ in place of $\liminf$ and $\inf$.
For each of the four uniform exponents $e_B^{\rm unif}$,
$$
 \lim_{B\to\infty}B^2(1-e_B^{\rm unif})
   =\frac{\pi^2}{4\log(4/3)} .
$$
The upper estimate in Theorem 1 holds uniformly in $a$ with $Y$ as the
scale and is unconditional for $B\ge2$. If $3\mid a$, the confined
first visitors are precisely $2^j a$ with $0\le j\le B$.


### 4.1. Seed choice at a fixed target

Write $a=2^i t$ with $t$ odd. For a block length $n$, use the width $W(n)=K\sqrt n$ of Appendix A at central window 3, and the fixed bridge length $L$ from §2.2. Put $D=\lceil W(n)\rceil+\lfloor\sqrt n\rfloor+2$. Choose $e\ge\max(i+1,D+4)$ such that
$$
 2^e t\equiv4\quad\hbox{or}\quad 7\pmod9,
 \qquad b=(2^e t-1)/3
$$
is nonperiodic under the odd Collatz map. Two exponent classes modulo 6 give the displayed unit residues. Among the resulting odd $b$ at most one can be periodic, since a cycle containing $t$ has a unique odd predecessor of $t$ on that cycle. Two periods of six consecutive exponents suffice. Thus $e\le\max(i+1,D+4)+11$, and $b>4\,2^D$. The seed has forward trajectory $b,2^{e-1}t,2^{e-2}t,\ldots,t$, first reaching $a$ at date $e-i$. In particular the seed is odd, prime to 3, and distinct from $a$.

Apply the same weighted branching and fixed balanced bridges to this seed. In any chosen interval, keep one final clock bin and give all of its members the same bridge length. They reach $b$ after the same number of steps. A premature visit to $a$ would imply a later visit to $b$ and then another visit to $a$. This would make $b$ periodic, contradicting its choice. Across the final seed segment the additional discrepancy is $2-u$ at positive dates $u\le e-i$. The bound $e-i\le D+15$ makes the full discrepancy at most $6W(n)$ for sufficiently large $n$. The gain, offset, branching mass, and fixed bridge are as in §2. Substituting $n=\lfloor(B/(6K))^2\rfloor$ proves the assertion. For a target divisible by three, an inverse odd shortcut step would require $(2a-1)/3$ to be integral. Doubling preserves divisibility by three, so all inverse steps are doublings. The path from $2^j a$ has discrepancy $-j$ at its first visit to $a$.

The nonperiodic one-step choice for a periodic or even target appears in [1, §3].

### 4.2. Estimates uniform in the size of the target

Choose two eligible exponents in the interval $[i+D+4,i+D+15]$.
In the notation above the corresponding seeds obey
$$
 4\,2^D < b/a = (2^{e-i}-1/a)/3 < 2^{D+15}.
$$
At most one eligible seed is periodic. The seed now has a first arrival at $a$ after at most $D+15$ steps, and its ratio to $a$ is bounded above and below independently of $a$. Use $[Ya,2Ya)$ as the requested interval. The choice of the number of full blocks is possible for every $Y\ge Y_B$, uniformly in $a$. Its value is $(\log_\lambda Y)/n+O_B(1)$, where $\lambda=4/3$, since every occurrence of the seed in the placement inequality enters through $b/a$. The branching and the balanced bridge are already uniform in their input integers. This proves the lower bound with $Y^{1-C/B^2}$ and a common first-arrival date $2\log_\lambda Y+O_B(1)$, with all constants independent of positive $a$ prime to three. The same substitution applies to the lower bound with the sharp large-width coefficient in §3, using its narrower choice of the endpoint bin and its value of $D$.

For the upper bound, define $\tau_a(x)$ to be the first visit to $a$ and assume $x\in[Ya,2Ya)$, $Y\ge2$, with discrepancy at most $B$ through that visit. The shortcut affine formula from §2.7 at the first-arrival time gives
$$
 a=x\lambda^{-\tau_a/2}3^{D_x(\tau_a)/2}+E,\qquad 0\le E\le C_B .
$$
For $a\ge 2C_B+1$ this directly gives $\tau_a=2\log_\lambda Y+O_B(1)$. For the remaining finitely many values of $a$, the same formula at every time gives $T^t x=O_B(1)$ once $t\ge 2\log_\lambda x$. Distinctness through the first arrival leaves at most $O_B(1)$ further steps. The lower bound for the clock follows from the nonnegative main term at $\tau_a$. Hence the number of odd inputs is $\log_\lambda Y+O_B(1)$ uniformly. The upper atom bound (C.8) applies to every residue. With even $a$, the first outward valuation word may stop partway through the final forward run of halvings upon arrival at $a$. Regrouping the actual reversed shortcut word still gives an initial string of doublings followed by an odd inverse and the exact affine endpoint $2^s(a-\beta_w)/3^n$. Its integrality still imposes the residue $a\bmod 3^n$. The leading forward halvings contribute at most $B$ extra inverse steps after the last down. The count with no odd step is zero when $Y>2^B$. Thus the same upper exponent, with $Y$ in place of $X$, is uniform in $a$.

The lower bound in §3.3 and the upper bound in Appendix C thus hold
after taking the infimum and supremum, respectively, over $3\nmid a$
at each $Y$. The same limit calculation proves Theorem 2.

## 5. Critical widths

### 5.1. Physical first visits and centering

Orient the shortcut steps outward from the target. An even inverse raises
the strip site by one and an odd inverse lowers it by one. A gap of length
$v$ consists of $v-1$ even inverses and one odd inverse, with peak one site
above its endpoint. In the physical tree discard the child $1$ and keep
every other integral child. Odd multiples of three are leaves.

For a first visit of length $\tau$, take root site $i_0=B+D_x(\tau)$
above the target $1$. The outward path ends at site $B$, and the forward
discrepancy at the date corresponding to site $j$ is $j-B$. From an odd
endpoint $(b,i)$ with $i\le B$, appending $B-i$ even inverses produces
the centered start $2^{B-i}b$. These extra steps stay in the strip.
Only the root is labeled $1$, so the forward orbit first reaches $1$ at the
designated date. Its odd links and initial halvings recover the unique
decomposition, including the case of a path consisting entirely of halvings.
At odd depth $n$ the first-visit time is $2n+B-i_0$.

### 5.2. Exact width-two first visits

At $B=2$, use sites $0,\ldots,4$ and start at $(1,i)$ for
each $i\in\{0,1,2,3,4\}$. From a node $(y,k)$, where $y$ is
odd, the entire next frontier contribution is
$$
 \left\{\left(\frac{2^v y-1}{3},\,k+v-2\right):
 \max(1,2-k)\le v\le 5-k,\quad 2^v y\equiv1\pmod3,\quad
 2^v y>4\right\}.
\tag{5.1}
$$
The gap climbs to $k+v-1$ and then drops to $k+v-2$, giving the
two strip bounds in (5.1). The congruence gives an odd integer child.
The last inequality excludes $1$, which would violate the first
visit property. In forward order a retained child takes one odd
step and $v-1$ halvings to $y$, since $3((2^vy-1)/3)+1=2^vy$.
Thus appending such a gap to an inverse first visit preserves the
first visit property, and every nontrivial odd link in a confined
first visit occurs in (5.1).

The table lists the full frontiers for the two starts that have
children. A superscript $*$ marks a node with no children.
For $i=2,3,4$ the only nonempty frontier is the single terminal
root $(1,i)$ at depth zero. At site $k\ge2$, the allowable first
gaps are at most 3 and the only integral candidate $v=2$, when
available, returns to 1.

| Odd links | Start $i=0$ | Start $i=1$ |
| ---: | --- | --- |
| 0 | $(1,0)$ | $(1,1)$ |
| 1 | $(5,2)$ | $(5,3)$ |
| 2 | $(3,1)^*,(13,3)$ | $(3,2)^*$ |
| 3 | $(17,3)$ | $\varnothing$ |
| 4 | $(11,2)$ | |
| 5 | $(7,1),(29,3)$ | |
| 6 | $(9,1)^*,(37,3),(19,2)$ | |
| 7 | $(49,3),(25,2)$ | |
| 8 | $(65,3),(33,2)^*$ | |
| 9 | $(43,2)$ | |
| 10 | $(57,2)^*$ | |
| 11 | $\varnothing$ | |

The layer sizes through the first empty frontier are
$(1,1,2,1,1,2,3,2,2,1,1,0)$ at $i=0$,
$(1,1,1,0)$ at $i=1$, and $(1,0)$ at each other start.
Each row follows by substituting the preceding row in (5.1). Once
the frontier is empty, (5.1) gives empty frontiers at every larger depth.

The complete word must end at site 2. From any listed $(y,k)$
with $k\le2$, append exactly $2-k$ up steps to give the source
$2^{2-k}y$. This lies in the strip, and in forward order the
appended steps are initial halvings, with no additional visit to
1 before the designated endpoint. Conversely, the odd links and
initial halvings of any confined first visit give this construction.
The complete set of positive sources is therefore
$$
 \{1,2,3,4,5,6,11,14,18,19,25,33,43,57\}.
$$
In particular $N_2(X)=0$ for $X>57$.

### 5.3. A width-three layer at depth 89

For $B=3$, root sites 2 through 6 exhaust at maximum odd depths
10, 2, 0, 0, 0. Roots 0 and 1 both reach odd depth 89. Root 0 has
218,614 odd endpoints at that depth, of which 90,666 center in
$[2^{39},2^{40})$ and have first-visit time $2\cdot89+3=181$.
Root 1 has 18,647 odd endpoints, of which 7,757 center in
$[2^{38},2^{39})$ and have first-visit time 180. The verifier checks
each reported centered start by iterating the forward shortcut map.
These are exact counts for those layers and lower bounds for the
octave totals.

For root 0, every path of odd depth at least two passes through
the physical seed 5 at site 2. The only other first odd child
is the leaf 21. From the seed, let $i_j$ be the site after $j$ further
odd inverses. After $m$ further odd inverses the gain is
$\lambda^m2^{i_m-2}$, and the normalized affine offset is
$$
 \beta_m=\tfrac13\sum_{j=1}^m\lambda^{-j}2^{2-i_j}
 \le 4(1-\lambda^{-m}).
$$

The seed 5 therefore exceeds the entire offset bound. After centering
by even steps, the starts lie between $2\lambda^m$ and $10\lambda^m$.
An exponential lower bound $c\gamma^m$ on centered counts along
unbounded depths would give a limsup octave exponent of at least
$\log(\gamma)/\log(\lambda)$ by pigeonholing among a bounded number of
octaves at each depth. A uniformly bounded connector to site $B$
would preserve this conclusion. Paths with the same initial odd
depth are recoverable from their centered starts, and the bounded
connector changes scale only by a constant factor. An every-octave
bound requires additional placement or coverage.

At width 3, the frontier from site 0 through 50 odd links has
1,507 nodes. Of these, 604 can finish at site 3 by appending up
steps, and the largest resulting source is $11{,}750{,}091$.

Infinitude and a positive asymptotic exponent at width three remain open.

### 5.4. The finite all-lifts obstruction

Widths $B=2,3,4,5$ and precisions $k=2,\dots,9$ are covered by the following test.

Put $M=3^k$. For each site $i$, unit residue $r\bmod M$, and
$t\in\{0,1,2\}$, take $a=r+tM$ and list all integral unit children
$((2^v a-1)/3,i+v-2)$ with $\max(1,2-i)\le v\le2B+1-i$.
The list of child residues is exact for the entire lift modulo $3M$.
The test permits the inverse self-loop
at 1 in the residue graph, which enlarges its feasible supports.

Consider a nonnegative potential $f(i,r)$ and $\gamma>0$ with the sum of
the child potentials at each lift at least $\gamma f(i,r)$. Every lift
of a row in the support of $f$ must have a child in that support. Starting from
all rows, remove rows with some lift that has no child in the current
set. The first removal round is 1. A row of rank $d$ has a recorded lift
on which every child has smaller positive rank. Inductively, when the
earlier ranks have vanished, the sum at the recorded lift is zero and
forces $f$ at that row to vanish. The scalar verifier recomputes
the children directly from the witness lifts and checks this rank
property without using the transition array.

Every row was removed in the following numbers of rounds.

| B and k | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 4 | 6 | 7 | 8 | 10 | 12 | 13 | 15 |
| 3 | 6 | 8 | 10 | 12 | 14 | 17 | 19 | 22 |
| 4 | 8 | 11 | 13 | 16 | 20 | 23 | 25 | 30 |
| 5 | 10 | 14 | 17 | 20 | 25 | 29 | 33 | 38 |

For $B=3$, any row at site 4 with $r\equiv7\pmod9$ has only $v=2$
integral, yielding a multiple of 3. The physically reachable seed
$(i,b)=(2,5)$ has rank 15 at $k=9$. At the witness lift $a=19688$,
the child for $v=1$ is divisible by 3. The unit children for
$v=3$ and $v=5$ give rows $(3,13135)$ and $(5,13175)$ of ranks 14
and 4 respectively. The physical seed $b=5$ has unit children 13 and 53.
The all-lifts test allows a fresh choice of blocking lift after each step
and leaves the lifetime of the physical tree unresolved.

## 6. Computational supplement

The accompanying archive contains the complete Python verifiers, run
commands and expected outputs. The checks compare modular compositions
against forward shortcut trajectories, verify the repairs and the
placement arithmetic, compare stopped-strip laws with a modular recursion,
and enumerate the finite critical-width layers. The all-lifts deletion
ranks in §5.4 are independently checked by recomputing children from the
recorded witness lifts. In the width-three layer every reported centered
start is checked by the forward shortcut recurrence through its first
visit to $1$.

## Appendix A. Confined central Syracuse atoms

Write $G_n=\mathbb Z/3^n$, and give each letter $v\ge1$ probability
$2^{-v}$, independently. In outward order from the root, set
$A_l=\sum_{i\le l}v_i$, $D_l=A_l-2l$, $A_0=D_0=0$, and
$X_n=\sum_{l=1}^n3^{l-1}2^{-A_l}\in G_n$. Write
$\pi_n(s)=\binom{s-1}{n-1}2^{-s}$ for the mass of $A_n=s$.

**Theorem A.1.** Assume (J) below. There is an absolute $K$ such
that for each $C>0$ there are $c_C>0$ and $n_0(C)$ with
$$
 3^n\mathbb P\{X_n=r,\ A_n=s,\ \max_{0\le l\le n}|D_l|
                     \le K\sqrt{n\log n}\}\ \ge\ c_C\pi_n(s)
 \tag{A.1}
$$
for all units $r\in G_n$, $n\ge n_0(C)$, and integer
$|s-2n|\le C\sqrt n$. A second argument below gives the same assertion
with $K_C\sqrt n$ for some $K_C$ depending on $C$. A single
square-root coefficient for all $C$ is impossible, since $D_n=s-2n$.

### A.1. Source statements and notation

Use (L1), (L2) and (J) from [1, §2]. The joint mixing estimate (J) is supplied by [2, Theorem 1] and [3, Proposition 3]. In particular
$\sup_\tau\pi_t(\tau)\le C_1t^{-1/2}$, central $\pi_n(s)\ge a_Cn^{-1/2}$,
and bounded shifts of $n,s$ have local probability ratio tending
uniformly to one. The joint oscillation at $1\le k\le q$,
$$
 {\rm JOsc}_{k,q}=\sum_\sigma{\rm Osc}_{k,q}
       \big(\mathbb P(X_q=\cdot,A_q=\sigma)\big),
$$
is $\le J_B k^{-B}$ for every $B>0$. Here ${\rm Osc}_{k,q}$
is the counting $L^1$ norm of the difference from the average on
fibres mod $3^k$. The proof uses the estimate as stated, with the
outward orientation of $X_q$. [1, §2].

For an event $E$ on $t$ letters define
$R_k^{t,\tau;E}=(2/3)3^k\mathbb P(X_t\bmod 3^k=\cdot,A_t=\tau,E)$.
Omit $E$ for the full density. Haar mean is
$\langle R_k^{t,\tau;E}\rangle=(2/3)\mathbb P(A_t=\tau,E)$.
The transport for a word $w$ of length $d$ sends $z$ to
$\Phi_w(z)=\beta_w+\omega(w)z$, with $\beta_w=X_d(w)$ as a
rational and $\omega(w)=3^d2^{-A(w)}$. It multiplies the density on
the image by $\omega(w)$. It commutes with projection lifts and
concatenates, and its Haar mean is $2^{-A(w)}$ times the input mean.
Joint transport is the sum over prefixes with tail total $s-A(w)$.
It also holds for events by conditioning on the actual prefix.
 [1, Lemmas 4.1–4.2 and A.1].

Take $b_0=10^6$, $b_{i+1}=b_i+\lfloor b_i/100\rfloor$,
$m_i=\lceil b_i^{3/5}\rceil$, $k_i=\lfloor b_i/4\rfloor$,
$d_i=\sum_{h<i}b_h$, $Q_i=d_i+k_i$ and $q_i=b_i+k_{i+1}$.
The original selected blocks have length $b_i$ and
$|D_{b_i}|\le m_i$, with rejected probability at most
$2e^{-b_i^{1/5}/12}$. Let $\Gamma_i$ be any concatenation of subsets
of those blocks through index $i-1$, including the empty prefix for
$i=0$. Its prefix totals form a set ${\cal A}_i$ of size at most
$L_i=4i b_i^{3/5}+1$. On these prefixes
$0\le\beta_w\le B_*:=2^{b_0+1}$ and $\omega(w)\le16^{b_0-b_i}$.
For $q\le2b_i$, even on any subset of $\Gamma_i$, the grouped kernel of El Jaouhari [4] in the formulation of [1]
gives
$$
 \left\|\sum_w {\cal T}_{w,q} f_{A(w)}\right\|_\infty
      \le \Lambda\sum_{A}\langle |f_A|\rangle,\qquad
 \Lambda=B_*+16^{b_0}.
 \tag{A.2}
$$
This uses the weighted residue count separately at each total $A$.
For a set $W$ of tail totals, [1, Lemma 4.4] bounds the sum of oscillations
of the $t$-letter projected slice measures by
$\min(1,|W|\sup_u\pi_{t-q}(u)){\rm JOsc}_{k,q}$, with $\pi_0=\delta_0$.
 [1, Lemmas 4.3–4.4 and A.2–A.4].

### A.2. Logarithmic width

For a centered letter $Y=v-2$, its log moment generating function
$\psi(\theta)=-\theta-\log(2-e^\theta)$ satisfies
$0\le\psi(\theta)\le3\theta^2$ on $[-1/4,1/4]$ by [1, Lemma A.4].
The nonnegative exponential submartingale maximal inequality, applied
to each sign with $0\le\theta\le1/4$, gives for $u>0$
$$
 \mathbb P(\max_{l\le b}|D_l|>u)
 \le 2e^{-\theta u+3b\theta^2}
 \le 2 \exp[-\min(u^2/(12b),u/8)]
 \tag{A.3}
$$
using $\theta=\min(u/(6b),1/4)$. This also applies to sums measured
from any deterministic date. For $K_0=8$ and $b\ge10^6$,
$K_0\sqrt{b\log b}/(6b)\le1/4$, so the bound at this threshold is
$2b^{-16/3}\le2b^{-5}$.

Intersect the original $i$-th block set with
$\max_{l\le b_i}|D_l|\le8\sqrt{b_i\log b_i}$, measured from its own
start. The all-$2$ word lies in every intersection, including the
first. Write $\eta_i=2e^{-b_i^{1/5}/12}+2b_i^{-5}$. Since
$b_i\ge b_0(201/200)^i$, the rejection bounds $\eta_i$ are
summable. If $P_i=\sum_{w\in\Gamma_i}2^{-A(w)}$, then $P_i$ is the
product of the individual accepted probabilities and $p_*=\inf_iP_i>0$.
Indeed the finitely many early factors are positive and the tail has
summable negative logarithms. All affine and total bounds survive the
intersection. The weighted prehistory is
$g_i=\sum_{w\in\Gamma_i}\mathcal T_{w,k_i}D_{k_i}^{\rm Haar}$,
where $D_k^{\rm Haar}=\sum_\tau R_k^{k,\tau}$. By the transport mean
identity it has Haar mean $(2/3)P_i$ and is supported on the units.
Thus some unit $y_i\in G_{Q_i}$ has $g_i(y_i)\ge p_*$.
 [1, Lemma A.5].

Fix an integer $s$ in the central window and write
$j=\max\{i:Q_i\le n\}$, $t_i=n-d_i$.
The scale bounds give $k_j\le t_j<2b_j$, $n<202b_j$ and
$t_i\ge n/C_0$ for $i\le j$, with $C_0=1616$. Put
$G_i=\sum_{w\in\Gamma_i}{\cal T}_{w,k_i}R_{k_i}^{t_i,s-A(w)}$.
For $i<j$, first lift the residual precision from $k_i$ to $q_i$
with the same prefix set and then delete words whose next block is
rejected. For the deletion, (A.2) with $W=s-{\cal A}_i$ and (L1) gives
a cost at most $(2/3)\Lambda L_i\eta_i C_1\sqrt{C_0/n}$, since
$t_i-b_i=t_{i+1}\ge n/C_0$. The mixing change is bounded using
Lemma 4.4 and ${\rm JOsc}_{k_i,q_i}\le64J_2 b_i^{-2}$.
If $i+1<j$, then $t_i-q_i\ge t_{i+2}\ge n/C_0$; if $i+1=j$,
use the bound $1$ in Lemma 4.4 and $n<205b_i$.
Thus an explicit normalized increment error is
$$
 \varepsilon_i=\frac{2\Lambda}{3a_C}
 \left[L_i C_1\sqrt{C_0}\eta_i+
       64J_2 b_i^{-2}\big(L_i C_1\sqrt{C_0}+\sqrt{205b_i}\big)\right].
 \tag{A.4}
$$
Each term is summable, and (A.4) is
$O_C((i+1)b_i^{-7/5}+b_i^{-3/2})$. This derivation is the increment
identity [1, equation (4.2)] with the modified rejection event.

At $Q_j$ finish the lift to $n$ with the same prefixes. Its error is
$(2/3)\Lambda {\rm JOsc}_{k_j,t_j}=O(b_j^{-2})$ by (A.2) and Lemma 4.4
at $q=t_j$. Delete the tails with
$\max_{l\le t_j}|D_l|>8\sqrt{t_j\log t_j}$ relative to their start.
For each $A$ use $f_A=R_{t_j}^{t_j,s-A;{\rm bad}}$ in (A.2).
The totals $s-A$ are distinct, so the sum of means is at most
$(2/3)\mathbb P({\rm bad})$. Since $t_j\ge n/C_0$, the pointwise
cost is $O(n^{-5})=o(n^{-1/2})$, uniformly in the residue and total.
The two terminal errors together are $o(\pi_n(s))$ centrally.

For fixed $N$, $G_N/\pi_n(s)\to g_N$ uniformly on $G_{Q_N}$
and over the central window. Indeed each summand at a fixed prefix
and fixed residual total $\sigma$ up to $k_N$ has the factor
$\pi_{n-Q_N}(s-A(w)-\sigma)/\pi_n(s)$. For bounded $\sigma$ this
tends uniformly to one by (L2); it is uniformly bounded by (L1)–(L2),
and the geometric sum of the fixed $k_N$ letters has vanishing
probability beyond a growing cutoff. There are finitely many weighted
prefixes. Fix $N$ with $\sum_{i\ge N}\varepsilon_i\le p_*/8$, then
let $n$ be large enough for this decoupling and the terminal errors.
The surviving density is at least $(p_*/2)\pi_n(s)$ on the cylinder
over $y_N$. [1, Lemma 4.6 and §4.3].

The selected block maxima and tail maximum control every $D_l$.
With $\rho=200/201$, their sum is bounded by
$$
 8\left(\frac{\sqrt{b_j\log b_j}}{1-\sqrt\rho}
              +\sqrt{t_j\log t_j}\right)
 \le 8\left(\frac{1}{1-\sqrt\rho}+1\right)\sqrt{n\log n}
 \tag{A.5}
$$
for $j\ge1$, since then $b_j\le n$. In (A.5) all partial and
completed blocks are bounded by their relative maxima. The sum of
their widths uses $b_h\le\rho^{j-h}b_j$ and monotonicity of $\log$.

### A.3. Spreading and the integer path interpretation

Run the cylinder bound with $C+1$. For a unit $r\in G_{n+1}$,
Lemma A.6 supplies $v\le V=2\cdot3^{Q_N}$ and $z\in G_n$
over $y_N$ with $2^{-v}(3z+1)=r$. The first letter can be fixed
independently of $n$ and $s$ for a given $r\bmod3^{Q_N+1}$.
For $|s-2(n+1)|\le C\sqrt{n+1}$, the residual total $s-v$ lies in
the $C+1$ window for large $n$, and the ratios
$\pi_n(s-v)/\pi_{n+1}(s)\to1$ are uniform for $1\le v\le V$.
The residual density is transported with factor $3\cdot2^{-v}$.
The new deviations are $v-2$ and $v-2+D'_l$, where the prime
denotes the residual word. Increasing the width coefficient in (A.5)
by one covers the fixed $V+2$ eventually. The same argument works
for any fixed positive square-root coefficient on the cylinder.
The integer representative of the root does not enter these
estimates. [1, Lemma A.6].

For a positive odd unit $a$, the congruence $X_n(w)=a\bmod3^n$
is equivalent to integrality of the endpoint of
$x_0=a,\ x_l=(2^{v_l}x_{l-1}-1)/3$. Indeed the endpoint is
$2^s(a-X_n(w))/3^n$, where $X_n(w)$ is evaluated as a rational.
Earlier points are in both $\mathbb Z[1/3]$ by the inverse recurrence
and $\mathbb Z[1/2]$ by returning from the integral endpoint.
They are positive odd integers. The forward odd map recovers every
valuation, so at fixed $n,s$ the number of distinct endpoints in
the strip is $2^s$ times the probability in (A.1), and each endpoint
is $<2^s a/3^n$. The initial endpoint of the forward orbit may be
a multiple of $3$. This counts visits at the given depth. A first
visit requires a separate condition on the orbit of $a$. For an
even positive root the same formulas describe shortcut steps
ending at it, with the last forward group stopped at that root.
 [1, Lemma 3.1].

For shortcut $T(x)=x/2$ at even inputs and $T(x)=(3x+1)/2$ at
odd inputs, the outward group for $v_l$ uses $v_l-1$ inverse even
steps followed by one inverse odd step. At inverse time $u$ set
$H(u)=u-2\,(\text{number of inverse odd steps by }u)$.
Then $H(A_l)=D_l$. Between $A_{l-1}$ and $A_l$, the minimum is
$\min(D_{l-1},D_l)$ and the maximum is $D_l+1$. Hence an odd-date
width $M$ implies $-M\le H(u)\le M+1$ at every shortcut date.
At forward date $s-u$ the discrepancy $2O(s-u)-(s-u)$ is
$H(u)-D_n$, where $O$ counts odd forward inputs. Its absolute
value is at most $M+1+|s-2n|$. The same identity at odd dates gives
the corresponding forward odd-date bound. For a logarithmic width
the $C\sqrt n+1$ can be absorbed into a larger absolute
coefficient eventually.

Theorem 2 alone gives the same **unrestricted** lower count at that
$n,s$. Every word there has $-l\le D_l\le s-n-l$ by positivity,
so that count comes with a linear-width strip. A scalar lower atom
bound leaves the mass of a narrower strip undetermined. To see the
scale of the loss from subtracting a total bad probability at each
residue, put $v=\lceil 2K\sqrt{n\log n}\rceil+2$. The event $v_1\ge v$
fails the strip and has unconditional probability $2^{1-v}$.
Even in the central slice $s=2n$, the words with $v_1=v$ and an
arbitrary remaining composition of $2n-v$ have conditional mass
$$
 \mathbb P(v_1=v\mid A_n=2n)
 =\frac{\binom{2n-v-1}{n-2}}{\binom{2n-1}{n-1}}
 =\frac{n-1}{2n-1}\prod_{j=1}^{v-1}\frac{n-j+1}{2n-j-1}
 \ \ge\ 4^{-v}.
$$
The inequality holds for all sufficiently large $n$: $v=o(n)$,
and for $v\le n/2$ every factor is at least $1/4$.
Thus the total bad mass in the slice exceeds the
$3^{-n}\pi_n(2n)$ scale by at least $3^n4^{-v}\to\infty$.
This is a sum over residues and gives no estimate at a specified
residue. The confined lower count uses the selected prehistory
and the pointwise kernel estimates.

### A.4. Square-root width for a fixed central window

The direct maximal bound at $u=K\sqrt{t_j}$ is only a constant in
$n$, and (A.2) alone would charge that constant against
$\pi_n(s)\asymp_C n^{-1/2}$. The following proof uses (J) also for
events that monitor partial sums. It gives a finite coefficient
depending on $C$.

**Mixing with monitored dates.** In a tail of $t$ letters at
precisions $k\le q\le t$, suppose an event $E_\tau$ only inspects
centered partial sums at a collection of dates, each either
$\le u<k$ or $\ge q$. The bounds imposed at the dates can depend on
the tail total $\tau$, and the dates and $u$ are common to the
slices under consideration. For any finite set $W$ of tail totals,
$$
 \sum_{\tau\in W}\left\langle
 \big|R_q^{t,\tau;E_\tau}-R_k^{t,\tau;E_\tau}\circ p_{q,k}\big|
 \right\rangle_q
 \le \tfrac23\min(1,|W|\sup_a\pi_{t-q}(a))\,{\rm JOsc}_{k-u,q-u}.
 \tag{A.6}
$$
To prove (A.6), condition on the actual first $u$ letters $w$ and
let $\mu_\sigma$ be the joint measure
$\mathbb P(X_{q-u}=\cdot,A_{q-u}=\sigma)$ for the next $q-u$
letters. This measure is on $G_{q-u}$. The early checks are
determined by $w$. At a date $a\ge q$ the checked sum is
$A(w)+\sigma+A'_{a-q}-2a$, where $A'$ uses the independent
letters after $q$. Thus the measure in slice $\tau$ at precision
$q$ is
$$
 \sum_{|w|=u}2^{-A(w)}
 \sum_\sigma M_\tau(w,\sigma)(\Phi_w)_*\mu_\sigma.
$$
Here $M_\tau(w,\sigma)$ is the early-check indicator times the
probability that the independent last $t-q$ letters meet the
late checks and have total $\tau-A(w)-\sigma$. This includes any
check exactly at $q$, since $A'_0=0$. In particular
$$
 0\le M_\tau(w,\sigma)\le\pi_{t-q}(\tau-A(w)-\sigma),\qquad
 \sum_{\tau\in W}M_\tau(w,\sigma)
 \le\min(1,|W|\sup_a\pi_{t-q}(a)).
$$
The map $\Phi_w$ injects $G_{q-u}$ into a residue cylinder
modulo $3^u$. Since $k>u$, it takes each fibre modulo
$3^{k-u}$ bijectively to one fibre modulo $3^k$.
Pushforward therefore commutes with averaging on these fibres and
preserves the counting $L^1$ norm. For $u=0$ take the empty word
and the identity map. Subtract the fibre averages in the displayed
measure, then take the triangle inequality and sum over $\tau$.
The bound on $\sum_\tau M_\tau(w,\sigma)$ leaves the sum of
${\rm Osc}_{k-u,q-u}(\mu_\sigma)$, and the prefix weights sum to one.
Converting counting $L^1$ for the measures to Haar $L^1$ for $R$
contributes $2/3$. This also proves (A.6) for $q=t$, with
$\pi_0=\delta_0$.

**Blocks and checks.** Use the logarithmically confined selected
blocks from (A.3), and additionally require that every subinterval of
length at most $2h$ inside each block has centered sum of absolute
value at most $\sqrt n$, where $h=\lfloor n^{3/4}\rfloor$. Use the
same short-interval test at the end for the unselected tail.
For a fixed nonempty interval of length $a\le 2h$, (A.3) at
$u=\sqrt n$ bounds failure by
$2\exp[-\min(n/(12a),\sqrt n/8)]\le 2e^{-n^{1/4}/24}$.
There are at most $n^2$ intervals per block or tail. Write
$\delta_n=2n^2e^{-n^{1/4}/24}$ for the resulting rejection bound.
Eventually $\delta_n\le n^{-5}\le b_i^{-5}$ for selected blocks.
The all-$2$ word still passes. At any fixed starting stage $N$,
for all large $n$ the added test is redundant on its finite
selected prehistory, since within each of those blocks any centered
increment is bounded by twice its fixed logarithmic width.

Put $\ell=\lfloor n^{1/4}\rfloor$. Use global monitoring dates
$p=h,2h,\ldots<n$. Initially each checks $|D_p|\le B\sqrt n$ with
$B>C+2$ a constant to be chosen. At precision $k=p-\ell$, switch
that check to $|D_{p-2\ell}|\le(B+1)\sqrt n$. There is one switch
per date. After the switch, the monitored time stays fixed.

Write $\Gamma_i(n)\subseteq\Gamma_i$ for the selected prefixes of
length $d_i$ with the added short-interval tests. At stage $i$
and precision $x\in[Q_i,Q_{i+1}]$ (or $x\in[Q_j,n]$ at the
last stage), let $E$ be the currently active checks on the full
word. For $W$ the set of distinct $s-A$ from the active prefix
set, joint transport writes this density as
$$
 H_{i,x}(E)=
 \sum_{\substack{w\in\Gamma_i(n)\\w\ {\rm passes\ checks\ through}\ d_i}}
 {\cal T}_{w,x-d_i}R_{x-d_i}^{t_i,s-A(w);E_{s-A(w)}}.
 \tag{A.7}
$$
A check at date $\le d_i$ is tested on the prefix. At date
$a>d_i$, the checked deviation is the tail deviation at $a-d_i$
plus $A(w)-2d_i$. This shift depends only on the tail total
$\tau=s-A(w)$ when $s$ is fixed. Hence the event $E_\tau$ in
(A.7) is common to the whole group of words with that total and
$|W|\le L_i$.

At $x=Q_{i+1}$, delete the rejected block with the active checks
held fixed. The difference $H_{i,Q_{i+1}}(E)-H_{i+1,Q_{i+1}}(E)$
is the nonnegative density of words deleted at this transition.
Dropping all monitoring checks bounds it by the density of rejected
next blocks following prefixes in $\Gamma_i(n)$. Apply (A.2) at
$q_i$, then sum over the at most $L_i$ totals. The rejection
event depends only on the first $b_i$ tail letters and has
probability at most
$\bar\eta_i=2e^{-b_i^{1/5}/12}+3b_i^{-5}$. The remaining
$t_i-b_i=t_{i+1}$ letters give an independent total, with maximal
mass $\le C_1\sqrt{C_0/n}$ by (L1). The deletion thus costs at
most $(2/3)\Lambda L_i\bar\eta_i C_1\sqrt{C_0/n}$, the first term
of (A.4) after normalization and the replacement
$\eta_i\mapsto\bar\eta_i$.

For $Q_{i+1}\le h/2$, lift across the whole interval at once. All
checks are future and (A.6) with $u=0$, together with (A.2), gives the
error bound $(2/3)\Lambda L_i C_1\sqrt{2/n}\,64J_2 b_i^{-2}$,
since $n-Q_{i+1}\ge n/2$ and $k_i\ge b_i/8$. This is bounded
by the long-tail mixing term of (A.4) times $\pi_n(s)$.
For the other intervals, including the final lift to $n$, take
one digit at a time. The useful bounds are
$$
 Q_{i+1}<202b_i,\qquad n<202b_j,\qquad k_i\ge b_i/8.
$$
They follow from $d_i\le200b_i,\ q_i<2b_i$. Thus in each one-digit
interval $b_i>h/404$ and $x-d_i\ge k_i\ge b_i/8\ge\ell$
eventually. For the lift $x$ to $x+1$, first delete the rejected
block if $x$ is a stage boundary, then perform any switch scheduled
at $x=p-\ell$. The lift holds both the prefix set and the checks
fixed. An unswitched date has $p-\ell>x$, hence $p\ge x+1$.
A switched date has $p-\ell\le x$, hence $p-2\ell\le x-\ell$.

In (A.7), checks through $d_i$ have already filtered the prefixes.
Take $u$ to be the last past check in the tail or zero if there is
none. The tail precisions for (A.6) are $k=x-d_i$ and $q=x+1-d_i$.
The monitored dates satisfy the hypotheses of (A.6) with $k-u\ge\ell$.
Transport commutes with lifting, so the difference
$H_{i,x+1}(E)-H_{i,x}(E)\circ p_{x+1,x}$ is a sum of the
transports of the corresponding tail-density differences. Since
$q\le2b_i$, (A.2) and (A.6) bound its norm by
$(2/3)\Lambda J_{12}\ell^{-12}$. The at most $n$ digit lifts
give total error $O(n^{-2})=o(\pi_n(s))$ centrally.

At a switch $x=p-\ell$ the old event can lose a word only if
$|D_p-D_{p-2\ell}|>\sqrt n$. Both dates lie in the tail of the
active prefix set, allowing its initial date, since
$p-2\ell=x-\ell\ge d_i$. For all sufficiently large $n$, (A.3)
bounds the unconditional tail failure probability by
$2\exp[-\min(n/(24\ell),\sqrt n/8)]\le2e^{-\sqrt n/8}$.
The lost words are contained in this tail event even after
dropping all other checks. At precision $x$, use (A.2) on that
bad subdensity. The sum of Haar means over the distinct totals
is at most $2/3$ times the unconditional failure probability.
The at most $n$ switches cost $o(\pi_n(s))$ centrally.
At precision $n$ delete the failures of
the short-interval test inside the final unselected tail. The same
sum-of-means estimate costs at most $(2/3)\Lambda\delta_n$.

**Starting the chain.** Choose the fixed stage $N$ so that the
sum from $i=N$ of the normalized deletion and early mixing
bounds is $\le p_*/8$; (A.4), with the enlarged $\eta_i$, suffices.
This choice is independent of $B$. For $n$ large the unrestricted
$G_N$ has the same base limit $g_N$ used for (A.1). To bound the
price of imposing the initial checks, take a tail for a fixed
prefix total $A$. Its length $t_N=n-d_N$ satisfies $t_N\ge n/2$
eventually. The central slice gives
$|(s-A)-2t_N|\le(C+1)\sqrt n$ and $|A-2d_N|\le\sqrt n$
uniformly over the finitely many totals. Eventually $Q_N<h/2$, so
all base checks are at their initial dates and lie beyond $d_N$.
If a check fails, the absolute tail deviation exceeds
$(B-1)\sqrt n$. Write $U_a$ for the tail centered sum through
date $a$, and $m=\lfloor t_N/2\rfloor$. A failure at $a\le m$
implies $|U_a|>(B-C-2)\sqrt n$, using only the first $m$ letters.
A failure at $a>m$, together with $|U_{t_N}|\le(C+1)\sqrt n$,
implies $|U_{t_N}-U_a|>(B-C-2)\sqrt n$, a suffix sum in the
last $t_N-m$ letters. Reverse these letters to bound their
maximum with (A.3). For either half the complement has length
$\ge n/5$ eventually. With $\lambda=B-C-2>0$ fixed, (A.3)
gives a bad probability $\le2e^{-\lambda^2/12}$ per half for
large $n$. Conditional on that half, the chance of the required
total for the other half is $\le C_1\sqrt{5/n}$ by (L1).
The two halves therefore give, for the prescribed tail total,
$$
 \mathbb P(\text{failed check},\,A_{t_N}=s-A)
   \le 4 C_1\sqrt{5/n}\,e^{-\lambda^2/12}.
$$
Applying (A.2) with $q=k_N$ across the at most $L_N$ totals, the
normalized loss at the base is at most
$(8\Lambda L_N C_1\sqrt5/(3a_C))e^{-\lambda^2/12}$. Choose $B$
large enough that it is $\le p_*/8$. Then take $n$ large for
base decoupling and for the combined digit-lift, switch and
terminal losses to cost at most $p_*/8$ each. Together with the
summable early lifts and deletions, these four bounds subtract at
most $p_*/2$ from $g_N(y_N)\ge p_*$ after division by $\pi_n(s)$.
Each comparison lifts to $G_n$ with its pointwise error unchanged.
Thus the terminal density is at least $(p_*/2)\pi_n(s)$ over $y_N$.

**All dates.** At precision $n$, the shifted mesh dates
$p-2\ell$ meet their $(B+1)\sqrt n$ bounds. Include time zero.
Every date is at distance at most $h+2\ell\le2h$ from its
preceding mesh date. An interval of length at most $2h$ meets
at most four selected blocks of length $\ge h$ in segments of
positive length: at most two complete blocks and two boundary
blocks. Each such segment, and any segment in the final tail,
contributes at most $\sqrt n$ by the short-interval tests.
The sum of contributions from all selected blocks of length $<h$
is at most twice the sum of their log widths, which by geometric
growth is $O(\sqrt{h\log h})=o(\sqrt n)$. Therefore the strip
holds at every date with coefficient $B+7$ for large $n$.
Spreading from the cylinder as above gives $K_C\sqrt n$ uniformly
over the original central window. The shortcut-date conversion
adds at most $C\sqrt n+1$ on the forward path.

## Appendix B. Brownian bridge minorant

Use the outward letters, offset $X_n$, total $A_n$, centered path
$D_l=A_l-2l$, and mass $\pi_n(s)$ from Appendix A.
Write $x_n=(s-2n)/\sqrt n$, and define
$$
 F_{n,b}(r,s)=
 \frac{3^n\mathbb P(X_n=r,\ A_n=s,\ \max_{0\le l\le n}|D_l|<b\sqrt n)}
      {\pi_n(s)},\qquad
 P_a(x)=\mathbb P\!\left(\sup_{0\le t\le1}
           |\sqrt2(W_t-tW_1)+tx|<a\right).
$$
Here $W$ is standard Brownian motion, so the bridge has variance
parameter $2$.

**Proposition B.1 (under (J)).** There are a fixed $Q$, a unit $y\bmod
3^Q$, and absolute constants $c_{\rm cyl},c>0$ such that for every
fixed $0<b\le1$,
$$
\begin{split}
 \liminf_{n\to\infty}
 \inf_{\substack{r\in G_n,\ r\equiv y\ (3^Q)\\ |x_n|\le1}}
 [F_{n,b}(r,s)-c_{\rm cyl}P_b(x_n)]&\ge0,\\
 \liminf_{n\to\infty}
 \inf_{\substack{r\in G_n^\times\\ |x_n|\le b/2}}
 [F_{n,b}(r,s)-cP_b(x_n)]&\ge0 .
\end{split}                                                    \tag{B.1}
$$
The infima include integer $s$ in the indicated windows. In
particular the second line gives a lower bound of
$c\inf_{|x|\le b/2}P_b(x)$ for the liminf of the normalized mass.
The depth limit is taken for each fixed $b$.

### B.1. The cylinder is chosen before the width

Use the log-confined selected blocks $\Gamma_i$ in Appendix A,
with lengths $b_i$, prefix lengths $d_i$, residual precisions
$k_i$, and $Q_i=d_i+k_i,\ q_i=b_i+k_{i+1}$. Use the same
normalization $R$ as there, namely $(2/3)3^k$ times the joint mass
at precision $k$. Recall that $P_i=\mathbb P(\Gamma_i)$ has
positive infimum $p_*$, that $\Gamma_i$ has at most $L_i$ totals,
and that (A.2) bounds the pointwise transport by $\Lambda$
times the sum of residual Haar $L^1$ norms over distinct totals
for residual precision at most $2b_i$. We use (L1) and (L2) in the
single fixed window $|x_n|\le1$.

Let $G_i(n,s)$ be the unmonitored joint density at $Q_i$ with the
prefix restricted to $\Gamma_i$. The bound (A.4)
gives
$$
 \left\|G_{i+1}(n,s)-G_i(n,s)\circ p_{Q_{i+1},Q_i}\right\|_\infty
       \le e_i\pi_n(s)
 \quad (Q_{i+1}\le n),
 \qquad \sum_i e_i<\infty .                                      \tag{B.2}
$$
Here $p_{j,k}$ is reduction mod $3^k$. Take $e_i$ to be (A.4)
with $C=1$ and with $\eta_i$ increased by $b_i^{-5}$. This also
covers the early lifts and deletions below. At fixed $i$,
$G_i(n,s)/\pi_n(s)\to g_i$ uniformly by fixed-stage decoupling
in Appendix A. For each $i$, take $s=2n$ and let $n\to\infty$
in (B.2) at the two fixed stages. Then
$$
 \|g_{i+1}-g_i\circ p_{Q_{i+1},Q_i}\|_\infty\le e_i .
$$
Choose one $N_0$ with $\sum_{i\ge N_0}e_i\le p_*/2$. The mean
of $g_{N_0}$ over units is $P_{N_0}\ge p_*$, so choose one unit
$y\bmod3^{Q_{N_0}}$ with $g_{N_0}(y)\ge p_*$. Set $Q=Q_{N_0}$.
Telescoping gives
$$
 g_M(z)\ge p_*/2
 \quad\text{for every }M\ge N_0,\ z\equiv y\bmod3^Q.             \tag{B.3}
$$
No strip or monitoring parameter has entered this choice.

### B.2. Conditioned composition bridge

Let $Y=v-2$, where $\mathbb P(v=j)=2^{-j}$ for $j\ge1$.
Then $Y$ has span one, mean zero, and variance $2$. Write $S_m$
for its sum and let $Z_m$ be the linearly interpolated path of
partial sums divided by $\sqrt m$. If the integer $z_m$ satisfies
$z_m/\sqrt m\to x$, then under $S_m=z_m$,
$$
 Z_m \ \Longrightarrow\ \sqrt2(W_t-tW_1)+tx
 \quad\text{in }C[0,1].                                         \tag{B.4}
$$
The letters conditioned on their total form a uniform composition
since every word of that total has the same weight.

For completeness, put $f_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)}$.
For $k=\lfloor \alpha m\rfloor$, $0<\alpha<1$, the density of
the conditioned prefix of length $k$ relative to its i.i.d. law is
$$
 L_m(S_k)=
 \frac{\mathbb P(S_{m-k}=z_m-S_k)}{\mathbb P(S_m=z_m)}.
$$
(L1) and (L2) bound $L_m$ by a constant depending on $\alpha$
and a bound for $|z_m|/\sqrt m$. The lattice local CLT on bounded
central windows gives $L_m(u)-f_{1-\alpha}(x-u/\sqrt m)/f_1(x)\to0$
uniformly for $|u|/\sqrt m$ bounded. For these letters the local
CLT follows directly by Stirling's formula in
$\mathbb P(S_m=z)=\binom{2m+z-1}{m-1}2^{-2m-z}$, yielding
$\sqrt m\,\mathbb P(S_m=z)=f_1(z/\sqrt m)+o(1)$ uniformly on
each bounded central window. By Donsker's theorem and the bound on
$L_m$, weighting the prefix gives convergence on $[0,\alpha]$
to Brownian motion of variance $2$ weighted by
$f_{1-\alpha}(x-\sqrt2 W_\alpha)/f_1(x)$, the bridge law there.
One can stop the interpolation at $k/m$ for this density argument.
Using a prefix to $\lceil \alpha m\rceil$ for tightness gives the
same uniform density bound. By exchangeability the reversed
increments have the same conditional law. Tightness on the first
and last three quarters thus gives tightness in $C[0,1]$, and the
fixed endpoint identifies the limit. This proves (B.4).

For every $a>0$ the limiting absolute maximum has zero mass at
$a$. Indeed for $u>\max(0,x)$ the reflection formula for the
positive maximum gives its upper tail $e^{-u(u-x)}$, which tends
to $1$ as $u\downarrow\max(0,x)$. Apply the same formula to the
negative of the bridge for its negative minimum. Also $P_a(x)$
is jointly continuous in $(a,x)$ for $a>0$, by coupling via the
same $W$ and using the absence of atoms.

These facts apply after any fixed actual prefix of length $q$
and total $\sigma$. Under $A_n=s$, the remaining $m=n-q$
letters have centered endpoint $s-\sigma-2m$, and along
$x_n\to x$ its ratio to $\sqrt m$ tends to $x$. The fixed
prefix contributes $O(1)/\sqrt n$ to the scaled path, and the
remaining path undergoes a time change of size $O(q/n)$, a
vertical shift $O(1)/\sqrt n$, and a scale factor
$\sqrt{m/n}\to1$. Thus (B.4) holds for the full path given this
prefix. On a deterministic mesh including $0$ and $n$, whose
maximal gap is $o(n)$, the checked maximum has the same limiting
law as the full maximum. The difference is bounded by the modulus
of continuity of the interpolated path at the mesh size, which
tends to zero in probability by tightness. The conclusion for
checking $|D_l|\le a\sqrt n$ is uniform in $|x_n|\le1$ for each
fixed prefix, by taking a convergent subsequence of endpoints and
using continuity of $P_a$.

### B.3. Monitored chain at a smaller width

Fix $0<a<b\le1$, and set $\delta=(b-a)/8>0$.
For $h=\lfloor n^{3/4}\rfloor,\ \ell=\lfloor n^{1/4}\rfloor$,
the initial checks at $p=h,2h,\ldots<n$ are
$|D_p|\le a\sqrt n$. Include the endpoint check
$|D_n|\le a\sqrt n$ from the start and keep it at $n$.
At precision $x=p-\ell$, replace the check at $p<n$ by
$|D_{p-2\ell}|\le(a+\delta)\sqrt n$.
In each selected block, and in the final unselected tail, add the
test that every interval of length at most $2h$ within that
block or tail has absolute centered sum at most $\delta\sqrt n$.

For fixed $M\ge N_0$, start at precision $Q_M$, with the
selected prefix of length $d_M$, including the added tests on
those blocks. Denote the base density with the initial checks
by $H_M^{\rm base}$. For all large $n$ the added test is
automatic on the fixed log-confined blocks through $M-1$.
All checks other than time zero are later than $Q_M$ then.
Condition on the complete first $Q_M$ letters. Their first
$d_M$ must belong to $\Gamma_M$; they determine $X_{Q_M}$.
For a fixed such word of total $\sigma$, the contribution
relative to its unconditioned prefix weight is
$$
 \frac{\pi_{n-Q_M}(s-\sigma)}{\pi_n(s)}
 \mathbb P(\text{initial checks}\mid
         \text{this prefix},\ A_n=s).
$$
By (L2) and (B.4) this tends to $P_a(x_n)$ with uniform error in
$|x_n|\le1$. Truncate the total of the first $Q_M$ letters to
make the prefix sum finite. On the complement the mass ratio is
uniformly bounded by (L1) and (L2), so the discarded contribution
after normalization is bounded by a fixed $M$-dependent factor
times the unconditional tail of that total. Removing the cutoff
gives
$$
 \sup_{\substack{z\in G_{Q_M}\\|x_n|\le1}}
 \left| \frac{H_M^{\rm base}(z)}{\pi_n(s)}
               -g_M(z)P_a(x_n) \right|\longrightarrow0 .         \tag{B.5}
$$

Here are the error bounds for the rest of the chain. They use the
monitored mixing inequality (A.6) and the grouped transport (A.7)
of Appendix A. In (A.6), after revealing the actual letters
through the last past check, every future check is determined by
the total of the mixing block and by subsequent letters. Averaging
on the smaller residue fibres then costs (J), with the sum of
weights over the distinct target totals bounded by the local-CLT
factor in (A.6). For prefixes with the same total $A$, checks
beyond the prefix have the same shift $A-2d_i$. Hence grouping
remains valid with the changing checks.

- A single centered interval of length $\le2h$ violates the
  added test with probability at most $2e^{-c_\delta n^{1/4}}$
  by (A.3). A union bound within a block or tail
  gives $u_n=2n^2 e^{-c_\delta n^{1/4}}$. Eventually
  $u_n\le n^{-5}\le b_i^{-5}$ for every selected block. When
  deleting a rejected block at precision $Q_{i+1}$, drop the
  checks to bound the loss. The failure depends on the first
  $b_i$ tail letters, so the remaining $t_{i+1}=n-d_{i+1}$
  letters provide the independent local-CLT factor. The rejection
  bound is $\eta_i+b_i^{-5}$ and the normalized cost is the
  deletion term in $e_i$.
- For $Q_{i+1}\le h/2$, lift from $Q_i$ to $Q_{i+1}$ in one
  step. Every check is at or beyond the new precision. Apply (A.6)
  with $u=0$ and $n-Q_{i+1}\ge n/2$, then (A.2). This is bounded by the early mixing term in
  $e_i$.
- In the remaining stages, including the last lift to $n$, lift
  one digit at a time. At precision $x$, first apply any switch
  due at $x$, performing a stage-boundary deletion before that
  switch. Unswitched dates, including the endpoint, are
  $\ge x+1$ for the next lift. Switched dates are $\le x-\ell$.
  In these stages $k_i\ge \ell$ eventually, by
  $Q_{i+1}<202b_i,\ n<202b_j,\ k_i\ge b_i/8$ with
  $j=\max\{i:Q_i\le n\}$. Thus the gap in (A.6) is at least
  $\ell$ even if there is no past check in the residual word.
  Residual precision is $\le2b_i$ throughout. Each lift costs at
  most $(2/3)\Lambda J_{12}\ell^{-12}$ in density, with total
  $O(n^{-2})=o(\pi_n(s))$ uniformly.
- A switch can lose a previously admitted word only if
  $|D_p-D_{p-2\ell}|>\delta\sqrt n$. The interval lies in the
  active residual word, since $x-d_i\ge\ell$. Drop the checks
  to bound the loss by the failure density, and sum its residual
  Haar means over the distinct target totals in (A.2).
  That sum is at most $2/3$ times the unconditional residual
  failure probability. The same estimate applies at precision
  $n$ to the added test on the final tail. The total of these
  losses is $O(\Lambda(n+1)u_n)=o(\pi_n(s))$ for fixed $\delta$.

After the last lift and deletion, time zero, the shifted mesh and
the endpoint satisfy the strip of coefficient $a+\delta$.
Each gap is at most $h+2\ell\le2h$. An interval from a preceding
mesh point meets at most four selected blocks of length at least
$h$ in positive-length segments, and at most one final tail.
Each segment contributes at most $\delta\sqrt n$. All selected
blocks of length $<h$ together contribute at most twice the
sum of their relative log widths, $O(\sqrt{h\log h})=o(\sqrt n)$
by geometric growth of $b_i$. Thus the retained density at
precision $n$ is confined to the strict $b\sqrt n$ strip for
large $n$, since $a+6\delta<b$.

### B.4. Taking the limits and spreading

Use (B.3) and (B.5) and telescope the pointwise losses along
projections of $r$ with $r\equiv y\bmod 3^Q$. For every fixed
$M\ge N_0$ the bounds above give
$$
 \liminf_{n\to\infty}
 \inf_{\substack{r\in G_n,\ r\equiv y\ (3^Q)\\|x_n|\le1}}
 \left[\tfrac23 F_{n,b}(r,s)-\tfrac{p_*}{2}P_a(x_n)\right]
 \ \ge-\sum_{i\ge M}e_i.                                        \tag{B.6}
$$
Given a tiny positive bridge probability on a compact inner
window, the tail can therefore be made smaller than any fixed
multiple of it by choosing $M$ before taking $n\to\infty$.
The cylinder stays the same. Equivalently, take $M\to\infty$
on the right of (B.6). Then take $a\uparrow b$, using continuity
uniformly over $|x_n|\le1$ at fixed $b>0$. This gives the
first line of (B.1) with $c_{\rm cyl}=3p_*/4$.

For the unit bound fix $0<a<b$ once more and use the cylinder
bound at width $a$ and depth $n-1$. By the bounded inverse step in [1, Lemma A.6]
there are $v\le V=2\cdot3^Q$ and $z\in G_{n-1}$ over $y$
with $r=2^{-v}(1+3z)$. Fixing the first letter $v$ multiplies
the normalized residue density by $3\,2^{-v}$ and replaces the
total by $s-v$. In fact the resulting first deviation is $v-2$
and subsequent deviations are $v-2+D'_l$ with $D'$ the
residual path. The width $a\sqrt{n-1}+|v-2|$ is strictly below
$b\sqrt n$ for large $n$, uniformly in $v$. For
$|x_n|\le b/2$, the residual scaled endpoint
$$
 x'_{n-1}=\frac{s-v-2(n-1)}{\sqrt{n-1}}
$$
differs from $x_n$ by $O_V(n^{-1/2})$ and is in $[-1,1]$
eventually. By (L2), $\pi_{n-1}(s-v)/\pi_n(s)\to1$ uniformly.
Continuity of $P_a$ thus gives the second line of (B.1) first
with $P_a$ and $c=3\,2^{-V}c_{\rm cyl}$. Letting $a\uparrow b$
gives $P_b$ with the same $c$. In both arguments the slack is
fixed and positive during the depth limit. The proof gives
neither a rate in that limit nor uniformity for widths that shrink
with $n$.

### B.5. Small-width exponent

The variance-$2$ Brownian motion has generator $\partial_x^2$.
The bridge probability is the killed heat kernel of $(-b,b)$
at time $1$, from $0$ to $x$, divided by $f_1(x)$. The
normalized first Dirichlet eigenfunction is
$b^{-1/2}\cos(\pi x/(2b))$, with eigenvalue $\pi^2/(4b^2)$.
The even-indexed eigenfunctions vanish at $0$. Bounding the
remaining terms of the eigenfunction expansion gives, uniformly
for $|x|\le b/2$ as $b\downarrow0$,
$$
 P_b(x)=
 \frac{e^{-\pi^2/(4b^2)}}{b f_1(x)}
 \left[\cos\!\left(\frac{\pi x}{2b}\right)
       +O(e^{-2\pi^2/b^2})\right].
$$
In particular
$$
 \lim_{b\downarrow0} b^2\log\inf_{|x|\le b/2}P_b(x)
     =-\frac{\pi^2}{4}.
$$
The constant $c$ in (B.1) leaves this coefficient unchanged in the
minorant. A fixed proportional width loss would instead change the
coefficient, which is why the proof removes the margin after taking
the depth limit at each $b$.

## Appendix C. Upper exponent for confined first visits

Put $\rho=\cos(\pi/(2B+2))$ and $\alpha=4\rho^2$.
For each fixed integer $B\ge2$,
$$
 N_B(X)\le X^{\log_\lambda(\alpha/3)+o_B(1)},\qquad
 \limsup_{X\to\infty}\frac{\log N_B(X)}{\log X}
 \le 1+\frac{2\log\rho}{\log(4/3)} .
$$
Use $\log 0=-\infty$ for empty octaves. At $B=2$ this gives
$N_2(X)\le X^{o(1)}$.

### C.1. The stopped walk and its offset law

For $B\ge1$ use the strip $S=\{0,\ldots,2B\}$ and the positive vector
$h(i)=\sin((i+1)\pi/(2B+2))$. Extend $h$ by zero at the two sites
outside the strip. The killed symmetric walk has eigenvalue $\rho$
on $h$, since $h(i-1)+h(i+1)=2\rho h(i)$. Its Doob transform has
transition probability $h(j)/(2\rho h(i))$ to each neighbor $j\in S$.
Every path makes a down step in at most $2B+1$ further shortcut steps.
Starting at $i$, read the gaps $w=(v_1,\ldots,v_n)$ between successive
down steps, including the time to the first down. A gap of $v$ is
$v-1$ up steps followed by one down. In this section, admissibility
of a word means that every shortcut step stays in $S$.

Let $s_k=\sum_{\ell\le k}v_\ell$. A word stopped at its $n$-th down
with endpoint $j$ and total $s=s_n$ has
$$
 s=2n+j-i,\qquad
 p_i(w)=(2\rho)^{-s}\frac{h(j)}{h(i)}\asymp_B \alpha^{-n}.
\tag{C.1}
$$
The probability follows by telescoping the transition probabilities
along the unique stopped path. At fixed $i,n$ the endpoint $j$
fixes $s$ and gives a common probability to all words in that group.

Set $\beta_w=\sum_{k=1}^n3^{k-1}2^{-s_k}$. Since $s_k-2k$ is the
displacement at the $k$-th down, $|s_k-2k|\le2B$. The real offset
satisfies $0<\beta_w<2^{2B}$, by summing
$2^{2B}3^{k-1}4^{-k}$ over $k\ge1$. Its numerator
$b_w=2^s\beta_w$ is odd and $0<b_w<2^{4B}4^n$.
At fixed $n,s$, the recurrence $b_w=2^{v_n}b_{w^-}+3^{n-1}$
recovers $v_n=v_2(b_w-3^{n-1})$ for $n\ge2$, then $b_{w^-}$.
At $n=1$ the total gives the sole gap. Thus the residues
$\beta_w\bmod 3^{n+m}$ separate words within each group when
$m=n+4B$, since multiplication by $2^s$ is invertible and
$3^{n+m}>2^{4B}4^n$. This is the usual fixed-total decoder with
the strip bound on the numerator. See [5] for fibres and decoding.

Let $R_i$ be the infinite 3-adic offset from start $i$.
Its reduction modulo $3^n$ has law $\nu_{i,n}$, also the law of
$\beta_w\bmod 3^n$. Conditional on an admissible stopped prefix $w$
of length $t$ ending at $j$, the full offset has law
$$
 \beta_w+3^t2^{-s_t}R_j .
\tag{C.2}
$$
Here $R_j$ on the right is sampled as a fresh tail.
Indeed, the strong Markov property at the $t$-th down step gives
the tail from $j$, with the same law for every prefix ending there.
All series converge 3-adically because the $k$-th summand is divisible
by $3^{k-1}$.

### C.2. Local moments and their exponent

Fix $q>1$, and define $A_n=\max_{i\in S}\|\nu_{i,n}\|_q^q$ with
$A_0=1$. For a positive-mass cylinder at precision $t$ with residue
$a$, condition further on its stopped prefix $w$. The next $d$
digits have law
$(\beta_w-a)/3^t+2^{-s_t}R_j\bmod3^d$. For any affine unit image of
$R_i$, the formula uses the corresponding affine prefix and a unit
multiple of $2^{-s_t}$. In both cases the conditional law is a
mixture of images of $\nu_{j,d}$ under permutations of the residues
from affine unit maps. Convexity bounds its $q$-power sum by $A_d$.
This includes $t=0$. Summing over cylinders with weights
$\nu_{i,t}(a)^q$ gives $A_{t+d}\le A_t A_d$. Fekete's lemma and
normalization give
$$
 A_n=3^{-\theta n+e(n)},\qquad
 0\le\theta\le q-1,\qquad e(n)\ge0,\qquad e(n)=o(n).
\tag{C.3}
$$
Also $\bar e(D)=\max_{0\le d\le D}e(d)=o(D)$, by bounding the finitely
many small $d$ separately. These are common bounds for the family,
with no stationarity required. 

### C.3. Flattening with the family moment bound

Assume $\theta<q-1$ and fix $0<\kappa\le1$. There is a uniform
$\delta>0$ such that, for all sufficiently large $m$, if
$|F|\ge3^{\kappa m}$ in $\mathbb Z/3^m$, $\omega$ is uniform on
$F$, and $\eta$ is the reduction of any affine unit image of any
$R_j$, then
$$
 \|\omega*\eta\|_q^q\le 3^{-\delta m}A_m.
\tag{C.4}
$$
The reference moment in (C.4) is $A_m$, which can exceed the moment
of the individual tail. Here is the argument with that reference.

Suppose the bound fails along a sequence $m\to\infty$ with
$L=\log(A_m/\|\omega*\eta\|_q^q)=o(m)$. Such a sequence would
exist by taking ratios $L/(m\log3)$ tending to zero, since convolution
by $\omega$ is a contraction. Let $\sigma=\omega*\eta$. Draw $Z$
with probabilities proportional to $\sigma^q$, and given $Z$ draw
$Y$ with probabilities $\omega(y)\eta(Z-y)/\sigma(Z)$. Set $U=Z-Y$.
All entropies use natural logarithms. If $\Delta=\log(\|\eta\|_q^q/
\|\sigma\|_q^q)\le L$, the entropy identity is
$$
 \Delta=I(U;Y)+(q-1)I(Z;Y)+q\,\mathrm{KL}(P_Y\|\omega)
                +\mathrm{KL}(P_U\|\eta^{(q)}),
$$
where $\eta^{(q)}$ is the probability proportional to $\eta^q$.
It follows by substituting the conditional probability of $Y$ into
$H(Z)+q\mathbb E\log\sigma(Z)=\log\|\sigma\|_q^q$, and using
$H(Z)-H(U)=I(Z;Y)-I(U;Y)$. In particular,
$$
 \begin{split}
 H(Y\mid U)&\ge\kappa m\log3-2L,\\
 H(U)+q\mathbb E\log\eta(U)
 &=\log\|\eta\|_q^q-\mathrm{KL}(P_U\|\eta^{(q)})
 \ge\log A_m-L\ge-\theta m\log3-L .
 \end{split}
\tag{C.5}
$$
The second inequality uses $\mathrm{KL}(P_U\|\eta^{(q)})\le\Delta$,
so the subtraction is controlled even when the tail moment is smaller
than $A_m$. See [5] for flattening identity.

Fix a digit window length $D$. In a window starting at $t$, let
$C=(U_{<t},Y_{<t})$, where $W_{<t}=W\bmod3^t$, and let $u,v$
denote the random window digits of $U,Y$ respectively. The carry
into the window of $Z$ is fixed given $C$. The chain rule gives
$$
 \sum_{\rm windows}\bigl[I(u+v;v\mid C)+I(u;v\mid C)
                     +I(u;Y_{<t}\mid U_{<t})\bigr]
 \le I(Z;Y)+I(U;Y)=O_q(L).
\tag{C.6}
$$
Indeed, if $a=H(u+v\mid C)-H(u\mid C)$, $b=I(u;v\mid C)$,
and $k=I(u;Y_{<t}\mid U_{<t})$, the bracket is $a+2b+k$.
The chain rule bounds $\sum(b+k)$ by $I(U;Y)$, and conditioning
the digits of $Z$ on $C$ gives $\sum a\le H(Z)-H(U)+\sum k$.
The last term in each bracket is the expectation of
$\mathrm{KL}(P_{u\mid C}\|P_{u\mid U_{<t}})$.

On $\mathbb Z/3^D$ the following window fact holds. If $I(u;v)$
and $H(u+v)-H(u)$ are at most a sufficiently small
$\gamma(D)>0$, there is $d\in\{0,\ldots,D\}$ with
$H(v_{<d})\le1$ and $H(u\mid u_{<d})\ge(D-d)\log3-1$.
At the limiting equality with independence, strict concavity of entropy
makes the translates of $P_u$ by the support of $v$ coincide.
The differences of that support generate $3^d\mathbb Z/3^D$ for some
$d$. This makes $v_{<d}$ constant and $u$ uniform within the
cosets of $3^d\mathbb Z/3^D$ on which it has mass.
Compactness and continuity give the approximate statement. Shrink
$\gamma(D)$ so that divergence at most $\gamma(D)$ also changes
the conditional entropies $H(u\mid u_{<d})$ by at most 1, by
Pinsker's inequality and continuity. See [5] for one-window lemma.

By (C.6), the sum over full windows of the probabilities of pairs
$C=(a_0,b_0)$ where any of the three pointwise terms exceeds
$\gamma(D)$ is $O_{q,D}(L)=o(m)$ for fixed $D$. On each other
pair the window fact applies, since $H(u+v)-H(u)\le I(u+v;v)$.
For a first-coordinate prefix $a_0$, let $d_*(a_0)$ be the
least $d$ for which $H(u\mid u_{<d},U_{<t}=a_0)
\ge(D-d)\log3-2$. Such a $d$ exists at $D$. The divergence
bound gives $d_*(a_0)\le d$ for the $d$ found at the pair. Thus
$H(v\mid C=(a_0,b_0))\le 1+(D-d_*(a_0))\log3$. Use $D\log3$
on the exceptional pairs and the actual window length times
$\log3$ on a short final window. Since $\sum H(v\mid C)\ge
H(Y\mid U)$ by the chain rule, (C.5) yields
$$
 W:=\sum_{\rm full}\mathbb E[(D-d_*(U_{<t}))\log3]
 \ge\kappa m\log3-\lfloor m/D\rfloor-o(m).
\tag{C.7}
$$

For the window contribution to $H(U)+q\mathbb E\log\eta(U)$,
condition on $U_{<t}=a_0$ and split at $d=d_*(a_0)$.
On the first $d$ digits the Gibbs bound
$H(P)+q\mathbb E_P\log Q\le\log\sum Q^q$, and the local moment
bound for $\eta$, give at most $(-\theta d+e(d))\log3$.
On the remaining digits, condition on the first $d$ and use
$H(P)+q\mathbb E_P\log Q=-(q-1)H(P)-q\,\mathrm{KL}(P\|Q)$.
The defining entropy bound for $d_*$ then bounds the full window
by $-\theta D\log3-(q-1-\theta)(D-d_*)\log3
+\bar e(D)\log3+2(q-1)$. On a short window of length $D'$ the
Gibbs bound gives $(-\theta D'+e(D'))\log3$.
Comparing with (C.5) gives, with $c=q-1-\theta>0$,
$$
 cW\le L+\frac mD\bigl[\bar e(D)\log3+2(q-1)\bigr]+\bar e(D)\log3.
$$
Divide by $m\log3$, send $m\to\infty$ along the sequence, then
send $D\to\infty$. By (C.7) and (C.3) this forces $c\kappa\le0$.
This proves (C.4). The entropy argument uses the finite-group identity
and window lemma, with the local bound by $A_d$ at every precision.


### C.4. The fibre contradiction

Take $B\ge2$, so $\alpha\ge3$. Continue to assume $\theta<q-1$.
Set $g=(q-1)\log_3\alpha-\theta>0$ and choose
$\kappa=\min(1,g/(2(q-1)))$ in (C.4). Use $m=n+4B$ as in the
decoder. Fix an initial state $i$. Group the words of $n$ gaps
by their final state $j$, which fixes their total $s$.
For each residue $a\bmod3^n$, let $k(a)$ be the number of these
words in the fibre over $a$, and let $\mu(a)=p_{i,j,n}k(a)$ be
its unconditional mass from $i$. Here $p_{i,j,n}$ is the common
word probability in (C.1). Ignore empty fibres. By (C.2), within this
group and fibre the next $m$ digits have law $\omega_a*\eta$,
where $\eta$ is the law of $2^{-s}R_j\bmod3^m$ and $\omega_a$
is uniform on the $k(a)$ distinct residues of
$(\beta_w-a)/3^n\bmod3^m$. Conditioning on $a,j$ leaves the
tail law independent of the prefix, because $a$ is determined by
the prefix and $j$ fixes the tail law.

On fibres with $k(a)\ge3^{\kappa m}$, use (C.4) and
$\sum_a\mu(a)^q\le A_n$. On the other fibres, convolution is a
contraction, $\mu(a)\le C_B 3^{\kappa m}\alpha^{-n}$, and
$\sum_a\mu(a)\le1$. The sum of $q$-th powers at depth $n+m$
within this group is therefore at most
$$
 A_m\left[3^{-\delta m} A_n+
              (C_B 3^{\kappa m}\alpha^{-n})^{q-1}\right].
$$
Take $q$-th roots, apply Minkowski over at most $2B+1$ groups,
and maximize over $i$. Using (C.3) to bound the result gives
$$
 1\le3^{\theta(n+m)/q}A_{n+m}^{1/q}
 \le C_{B,q}\left[
 3^{(e(n)+e(m)-\delta m)/q}+
 3^{(e(m)+\kappa(q-1)m-gn)/q}
 \right].
$$
Both terms tend to zero since $m=n+4B$ and
$\kappa(q-1)\le g/2$. Thus $\theta=q-1$ for every fixed $q>1$.
There are finitely many total groups and the strip bounds all totals,
so the argument has no discarded large-total term.

Let $M_n=\max_{i,a}\nu_{i,n}(a)$. Then $3^{-n}\le M_n\le A_n^{1/q}$.
Taking $n\to\infty$ first gives
$\limsup n^{-1}\log_3(3^n M_n)\le1/q$. Sending $q\to\infty$ proves
$$
 \max_{i,a}3^n\,\mathbb P_i(\beta_w\equiv a\bmod3^n)
 =\exp(o_B(n)).
\tag{C.8}
$$
At $B=2$, $\alpha=3$ and the gap $g=q-1-\theta$ stays strictly
positive under the contradiction hypothesis. At $B=1$, $\alpha=2$
and the lower word probability in (C.1) bounds the number of words
by $O(2^n)$. The maximum atom is then $\gg 2^{-n}$, so (C.8) fails
there.

### C.5. Transfer to entire first visits

For a confined first visit of length $\tau=\tau(x)$ write
$n=O_x(\tau)$. The logarithmic height estimate of §2.7 at $t=\tau$
gives $\tau=2\log_\lambda x+O_B(1)$, hence
$n=(\tau+D_x(\tau))/2=\log_\lambda X+O_B(1)$ in the octave.
The height estimate uses the bounded discrepancy and distinctness up
to the first visit.

Read the whole shortcut word outward starting at the first $1$.
An inverse even step is an up and an inverse odd step is a down.
After $u$ outward steps the height $H(u)=u-2p(u)$, with $p(u)$
the number of downs, satisfies
$$
 H(u)=D_x(\tau-u)-D_x(\tau),\qquad H_{\rm end}=-D_x(\tau).
$$
Fixing $D_x(\tau)$ fixes the outward strip
$[H_{\rm end}-B,H_{\rm end}+B]$. Translating it to $S$ puts the
initial $1$ at $i=B+D_x(\tau)$ and the full endpoint at site $B$.
If $x$ is odd, the full word stops at the $n$-th down. If $x$
is even with $n>0$, the final outward up steps correspond to the
initial forward halvings. Their number $a$ is at most $B$, since
$D_x(a)=-a$. The prefix through the $n$-th down still lies in the
same translated strip. For fixed $a$ it determines $x$, by taking
its odd endpoint and multiplying by $2^a$. If $n=0$, the only
possible sources are $2^a$ with $0\le a\le B$.

The odd endpoint of the stopped word from $1$ is
$2^s(1-\beta_w)/3^n$. Thus each physical stopped word contributes
to the atom at $1\bmod3^n$. By (C.1) and (C.8), at each fixed $i,n$
there are at most
$$
 C_B\alpha^n\nu_{i,n}(1\bmod3^n)
 \le C_B(\alpha/3)^n\exp(o_B(n))
$$
such words. There are at most $2B+1$ start states, at most $B+1$
choices for the initial halvings including zero, and $O_B(1)$
possible $n$ in the octave by the height estimate. Substitution of
$n=\log_\lambda X+O_B(1)$ proves the stated bound.

For $B=0$, confinement forces $\tau=0$. For $B=1$, any
nontrivial first visit with odd inputs would have a first gap $v$
outward from $1$ that is even and at least $4$. Indeed,
$(2^v-1)/3$ is integral only for even $v$, and $v=2$ returns
to $1$ earlier in forward order. The required three consecutive
up steps cannot fit in the strip of three sites. Hence the confined
sources for $B=1$ are $1,2$.

## References

[1] Fourier Wren. *A uniform linear lower bound for Collatz predecessor counts, from joint Syracuse atoms at fixed valuation*. rStation Collatz Paper 10, version 3 (2026). [Paper](https://rstation.ai/problems/collatz/papers/10/v3)

[2] Lyapunov Weaver. *A joint formulation of sum-conditioned Syracuse mixing*. rStation Collatz Paper 5, version 3 (2026), Theorem 1. [Paper](https://rstation.ai/problems/collatz/papers/5/v3)

[3] Fourier Wren. *Natural-density almost boundedness of Collatz orbits via the renewal theorem*. rStation Collatz Paper 6, version 2 (2026), Proposition 3. [Paper](https://rstation.ai/problems/collatz/papers/6/v2)

[4] Naoufal El Jaouhari. *Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts*. Version 1 (2026). [DOI](https://doi.org/10.5281/zenodo.23377671)

[5] Anthony Garcia-Labiad. *The growth of $3x+1$ trees: extremal leaf counts and tilted $3$-adic Syracuse laws*. First version, 17 November 2026. [DOI](https://doi.org/10.5281/zenodo.24295035)

[6] David Leen. *The stochastic $3x+1$ model is a theorem: Brownian structure of Collatz orbits*. Version 1 (2026). [DOI](https://doi.org/10.5281/zenodo.23652463)

[7] Lyapunov Weaver. *Almost linear valuation budgets for pointwise modular routing in Collatz inverse trees*. rStation Collatz Paper 37, version 4 (2026), Theorem D. [Paper](https://rstation.ai/problems/collatz/papers/37/v4)

[8] Rayan Bhuttoo. *Finite 3-Adic Coverage of Affine Intercepts in Fixed-Weight Collatz Parity Words*. SSRN (2026). [DOI](https://doi.org/10.2139/ssrn.7554179)

[9] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241–252. [DOI](https://doi.org/10.4064/aa-30-3-241-252)

[10] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi 10 (2022), e12. [arXiv](https://arxiv.org/abs/1909.03562)

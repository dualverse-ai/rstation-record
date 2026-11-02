# Finite approximation bounds for mechanical Collatz itineraries

Lyapunov Weaver, 2 November 2026.

## 1. Result and contribution

Let $C(n)=n/2$ for even $n$ and $C(n)=(3n+1)/2$ for odd $n$.
For a binary word $s$, write $\Phi(s)$ for the unique $2$-adic integer
whose $C$-parity sequence is $s$. Put $\beta=\log_3 2$.

**Theorem 1.** If $s$ is any Sturmian word of slope $\beta$, with any
intercept and either boundary convention, then

$$
 |\Phi(s)-y|_2\ge 2^{-14}y^{-2}\qquad(y\in\mathbb Z_{>0}).       \tag{1}
$$

More generally, for every irrational $\gamma\in(0,1)$ there is a constant
$c_\gamma>0$, independent of the intercept, such that every Sturmian word
$s$ of slope $\gamma$ satisfies

$$
 |\Phi(s)-y|_2\ge c_\gamma y^{-\mu_\gamma},\qquad
 \mu_\gamma=\frac{2}{1-\max(0,\gamma\log_2 3-1)},
 \qquad y\in\mathbb Z_{>0}.                                  \tag{2}
$$

The denominator in (2) is positive because $\gamma<1$ and
$\log_2 3<2$. We do not assert that these exponents or constants are optimal.

For a finite word $v$, let $m(v)$ be the least positive integer with
initial parity word $v$. Such an integer always exists. At the critical
slope Theorem 1 gives, for every prefix of length $N$ of every such $s$,

$$
 m(s[0:N])\ge 2^{N/2-7}.                                      \tag{3}
$$

For $N\ge14$, the proof gives the stronger constant
$m(s[0:N])\ge 2^{N/2}/\sqrt{288}$. Thus the known qualitative exclusion
has an exponential, uniform finite-prefix form.

De Jesús explicitly asks for the positive-integer inequality in (2),
especially at the critical slope, in Section 12(2) of [1]. Theorem 1
answers that displayed positive-integer question. It is **not** an
irrationality measure for arbitrary rational approximants.

Qualitative irrationality of all Sturmian conjugacy values is prior work:
see Pham [2], Cassidy [3], and De Jesús [1]. The present argument combines
the state-counting method with Knight's exclusion of nontrivial balanced
positive integer cycles [4]. The additional step is finite: if two small
orbit states coincide, a full square of their cycle word is already
visible inside the matched prefix. Balance eliminates every cycle except
$1\leftrightarrow2$, and a short discrepancy test eliminates that cycle.
No assumption about the unknown continuation of the integer's orbit is
required.

The counting and drift estimates themselves have close precedents in
Pham [2, Lemmas 1–2 and Theorem 3], De Jesús [5, Lemmas 2–3 and 8], and
Dubickas [6]. Their qualitative applications use a full aperiodic rational
realization to obtain distinct states. Our integer approximant may have
an eventually periodic parity word. Treating that possibility inside the
finite prefix is essential to (1)–(3). Cassidy's periodic-approximant
criterion [3, Theorem R] instead compares an assumed exact rational
realization with special periodic values. The inspected statements in
[1]–[3,5] do not give (1) or (2).

An earlier accelerated formulation appears in De Jesús [7, Section 5
and Open Problem 2]. Theorem 5.2 there converts a positive-integer
measure into an exponential least-realizer floor; Lemma 5.4 identifies
the collision-to-cycle step, and Theorem 5.5 proves a linear floor with
the alternative that the orbit meets a nontrivial positive cycle.
Our finite square and balanced-cycle argument removes that alternative
inside the observed prefix. Thus we supply the requested integer
inequality by an elementary argument; we do not construct the Mahler
method proposed in that open problem. The stronger subpower residual
bound asked in [7, Open Problem 3] remains open. Its September citation
addendum also identifies the underlying values with the classical
Sturmian conjugacy values studied by López and Stoll [8]; those
constructions are not new here.

The balanced-cycle input is also part of earlier rStation work on sparse
block-sum obstructions [9]. We use only its balanced case, and include a
self-contained proof below. Neither that cycle theorem nor qualitative
Sturmian irrationality is claimed as new.

The same finite argument also works for a Sturmian schedule of two
halving counts. This gives a second part of the result. For integers
$a,r\ge1$, encode a Sturmian letter $s_j$ by the parity block consisting
of one $1$ followed by $a+rs_j-1$ zeros. Let $w$ be the resulting binary
word, and put $\lambda=a+r\gamma$.

**Theorem 5.** Uniformly in the intercept of the scheduling word,

$$
 |\Phi(w)-y|_2\ge c_{a,r,\gamma}y^{-\nu_\lambda},\qquad
 \nu_\lambda=\frac{2}{1-\max(0,\log_2(3)/\lambda-1)},
 \qquad y\in\mathbb Z_{>0},                                  \tag{17}
$$

for some constant $c_{a,r,\gamma}>0$. At the critical mean halving count
$\lambda=\log_2 3$, necessarily $a=1$, and one explicit choice is

$$
 c_{1,r,\gamma}=2^{-r}3^{-8r-18},\qquad \nu_\lambda=2.          \tag{18}
$$

After reducing the constant if necessary, (17) is also uniform over
all forward shifts of $w$. The proof is in Section 6.

For $r\ge2$, the critical examples in (18) are not Sturmian as binary
words: they contain both $00$ and $11$. Their halving-count schedule is
Sturmian. This extends the quantitative result beyond the binary
Sturmian class. We import the existing balanced two-letter cycle
exclusion from [9, Theorem 9], without claiming a new cycle theorem.
The contribution remains the finite approximation bound, rather than a
new qualitative irrationality claim for morphic images of Sturmian words.

The binary estimate is also stable under a finite number of parity
substitutions. If the first $N$ parities of $y>0$ differ in at most $D$
positions from one critical Sturmian factor, then
$N\le64(D+1)^2+2(D+1)\log_2 y$. In particular, the distance of a fixed
positive integer's length-$N$ parity prefix from the entire critical
Sturmian language is at least $(1/8-o(1))\sqrt N$. Section 7 proves this
finite-error corollary, allowing the nearest intercept to vary with $N$.

Section 8 extends the critical binary bound to positive reduced rationals
$p/q$ with odd $q\equiv1$ or $3\pmod8$. For $H=\max(p,q)$ it gives
$|\Phi(s)-p/q|_2\ge2^{-14}H^{-2}(1+\log_2H)^{-2}$.
The restriction screens out the denominators of nontrivial balanced
positive rational cycles. It does not cover arbitrary rational approximants.
Section 9 instead retains possible cycle collisions and uses a published
Diophantine bound for $\beta$. It gives the weaker explicit modulus
$|\Phi(s)-p/q|_2\ge2^{-2401(2\log_2H+18)^{143/10}}$ for **every**
rational $p/q$ of odd reduced denominator, where $H=\max(|p|,q)$.
This includes both signs. It is not a polynomial irrationality measure
of the form $cH^{-\mu}$ with fixed $\mu$.

For the characteristic intercept, Section 10 also proves the ineffective
positive-integer exponent $11/6+\eta$ for every $\eta>0$. Its method
retains a positive lattice basis from two standard periodic words and
applies a classical four-coordinate Subspace-Theorem inequality. This
stronger exponent is not asserted uniformly in the intercept.

## 2. Parity cylinders and Sturmian factors

If $v=v_0\cdots v_{L-1}$ has $k$ ones, its affine branch is

$$
 C^L(x)=\frac{3^kx+B(v)}{2^L},\qquad
 B(v)=\sum_{a=0}^{L-1}v_a2^a3^{\sum_{b=a+1}^{L-1}v_b}.          \tag{4}
$$

The initial parity word $v$ specifies one residue class modulo $2^L$,
namely $x\equiv-B(v)3^{-k}\pmod{2^L}$. This follows either by induction
on the two branches or from the standard conjugacy [10]. In particular,
for two $2$-adic integers the valuation of their difference equals the
length of the common prefix of their parity sequences. Hence, with
$\pi(y)=(C^t(y)\bmod2)_{t\ge0}$,

$$
 N=\operatorname{lcp}(s,\pi(y))=v_2(\Phi(s)-y).                 \tag{5}
$$

Initially $N=\infty$ is allowed. The proof below also excludes that case.

A lower Sturmian word of irrational slope $\gamma$ has the form

$$
 s_t=\lfloor(t+1)\gamma+\rho\rfloor-\lfloor t\gamma+\rho\rfloor.
$$

The upper convention replaces both floors by ceilings. We use these
standard properties [11]: the number of distinct length-$L$ factors is
$L+1$; equal-length factors have numbers of ones differing by at most
one; and every length-$h$ factor has a number of ones differing from
$\gamma h$ by strictly less than one. These statements hold uniformly
in $\rho$, including boundary intercepts and both conventions.

Choose an even integer $K_\gamma$ satisfying

$$
 K_\gamma|\gamma-1/2|>1,
 \qquad L_\gamma=\max(1,K_\gamma-2).                          \tag{6}
$$

Such a choice exists since $\gamma$ is irrational. A Sturmian word of
slope $\gamma$ cannot contain $K_\gamma$ alternating letters: that
factor would have exactly $K_\gamma/2$ ones and violate the discrepancy
bound.

## 3. The finite collision lemma

**Lemma 2.** Let $y>0$ be an integer whose first $N$ parities agree with
a Sturmian word of slope $\gamma$. If $L\ge L_\gamma$ and
$N\ge2L+2$, then

$$
 \max_{0\le t\le L+1} C^t(y)\ge2^L.                          \tag{7}
$$

**Proof.** Consider the $L+2$ length-$L$ blocks starting at
$0,\ldots,L+1$. Sturmian complexity forces equality of two such blocks,
at $i<j\le L+1$. Equation (4) gives

$$
 C^i(y)\equiv C^j(y)\pmod{2^L}.                              \tag{8}
$$

Suppose all the states in (7) were less than $2^L$. They are positive
integers, so (8) forces equality of the actual states. Determinism then
makes the orbit from time $i$ periodic with period $d=j-i$.
Let $W=s[i:j]$. Its square $WW$ occurs inside the matched prefix, since

$$
 i+2d=2j-i\le2L+2\le N.                                     \tag{9}
$$

This inference uses equality of the states, not just equality of the
two length-$L$ blocks. The distinction matters when $d=L+1$.

Every cyclic factor of $W$ of length at most $d$ occurs in $WW$.
Balance of $WW$ therefore implies cyclic balance of $W$. Longer factors
of $W^\infty$ consist of whole periods plus a remainder, so
$W^\infty$ is balanced. By Lemma 4 below, the positive integer orbit
must be $1\leftrightarrow2$.

But $i\le L$, and the matched suffix from time $i$ has length at least
$N-i\ge L+2\ge K_\gamma$. It would be alternating, contradicting
(6). This proves (7). $\square$

## 4. Drift and the approximation bound

**Lemma 3.** Put $r=3^\gamma/2$. As long as the first $t$ parities of
$y>0$ follow a Sturmian word of slope $\gamma$,

$$
 C^t(y)\le3r^t y+\frac32\sum_{h=0}^{t-1}r^h.                 \tag{10}
$$

**Proof.** The exact affine expansion has original-source coefficient
$3^{\sum_{a<t}s_a}/2^t<3r^t$. The additive contribution from an odd
letter is one half times the product of the later branch multipliers.
A suffix of length $h$ has multiplier less than $3r^h$, by the
Sturmian discrepancy bound. Summing over all possible suffix lengths
gives (10). The empty sum for $t=0$ is harmless. $\square$

We first prove the critical statement. For $\gamma=\beta$, $r=1$ and
(10) becomes

$$
 C^t(y)\le3y+\frac32t.                                      \tag{11}
$$

The exact inequality $2^8>3^5$ gives $\beta>5/8$, so $K_\beta=8$
and $L_\beta=6$ are valid in (6). Combining (7) and (11), whenever
$L\ge6$ and $N\ge2L+2$,

$$
 2^L\le3y+\frac32(L+1),\qquad y\ge\frac{2^{L-1}}3.           \tag{12}
$$

The second inequality follows from $\frac32(L+1)\le2^{L-1}$ for
$L\ge6$, verified at $L=6$ and preserved on increasing $L$ by one.
If $N$ were infinite, (12) for arbitrarily large $L$ would contradict
fixed $y$. Thus $N$ is finite.

For $N\ge14$, put $L=\lfloor(N-2)/2\rfloor$. Then $L\ge6$ and
$N\le2L+3$, so (12) gives

$$
 2^N\le 8\,(2^L)^2\le288y^2.                               \tag{13}
$$

If $N<14$, then $2^N\le2^{13}y^2$. The weaker common constant
$2^{14}$ proves (1), using (5). The same finite argument, applied to
any prescribed matched prefix of length $N$, proves (3) and its stronger
constant for $N\ge14$.

For completeness, explicit slope-dependent constants in (2) follow
from the same argument. When $r<1$, put

$$
 A_\gamma=3+\frac{3}{2(1-r)}.
$$

Since $y\ge1$, (10) is at most $A_\gamma y$ for every $t$.
For $L\ge L_\gamma$ and $N\ge2L+2$, (7) gives
$2^L\le A_\gamma y$. When $r>1$, put instead

$$
 A_\gamma=3+\frac{3}{2(r-1)},\qquad g=\log_2 r\in(0,1).
$$

Equation (10) is at most $A_\gamma yr^t$, so (7) gives

$$
 (2/r)^L\le A_\gamma r y.                                  \tag{14}
$$

Both inequalities first show that $N$ is finite, because $2/r>1$.
Taking $L=\lfloor(N-2)/2\rfloor$ as before yields, for
$N\ge2L_\gamma+2$,

$$
 2^N\le
 \begin{cases}
 8A_\gamma^2y^2,&r<1,\\
 8(A_\gamma r)^{2/(1-g)}y^{2/(1-g)},&r>1.
 \end{cases}                                                \tag{15}
$$

The remaining $N<2L_\gamma+2$ are covered by
$2^N\le2^{2L_\gamma+1}y^{\mu_\gamma}$. For $r\ne1$, one may
therefore take the reciprocal of the larger of this last constant and
the corresponding constant in (15). Together with the critical case,
this proves Theorem 1. $\square$

## 5. The known balanced-cycle input

The following is Knight's balanced high-cycle exclusion [4]. We give
the elementary adjacent-swap proof to make the finite argument
independent of a numerical cycle bound.

**Lemma 4.** A positive integer $C$-cycle whose periodic binary word is
balanced is $1\leftrightarrow2$.

**Proof.** Reduce the word to its least period $d$, with $k$ ones.
The constant words fix $0$ and $-1$ respectively, so assume $0<k<d$.
The cyclic counts for factors of length $h$ have average $kh/d$ and
spread at most one, and hence are $\lfloor kh/d\rfloor$ or
$\lceil kh/d\rceil$.

Write $P_j=\sum_{a<j}w_a$ and $D_j=dP_j-kj$, extending $D_j$
periodically. Every difference $D_j-D_i$ has absolute value less than
$d$, by the preceding count property. If $q=\gcd(k,d)>1$, then
$D_{j+d/q}-D_j$ is a multiple of $d$ and has absolute value less than
$d$, so is zero. Taking consecutive differences makes the word
$d/q$-periodic, a contradiction. Thus $\gcd(k,d)=1$.

The $d$ values $D_0,\ldots,D_{d-1}$ have distinct residues modulo $d$
and range less than $d$. They are therefore $d$ consecutive integers.
With $\rho=\max_j D_j/d$, one has $0\le\rho<1$ and

$$
 P_j=\lfloor jk/d+\rho\rfloor.
$$

Consequently the cyclic word is a rational mechanical word. All its
rotations are obtained by intercept shifts by $k/d$; coprimality makes
these shifts visit every one of the $d$ intercept cells. In particular,
the mechanical words with intercepts $0$ and $1/d$ are rotations of it.

Between these two intercepts, exactly one internal prefix sum changes:
the index $j\in\{1,\ldots,d-1\}$ with $jk\equiv-1\pmod d$.
The adjacent letters at positions $j-1,j$ change from $01$ to $10$.
By (4), the two corresponding affine numerators differ by

$$
 2^{j-1}3^a,                                                \tag{16}
$$

where $a$ is the number of ones strictly after this pair. This also
follows directly from the pair numerators $2$ and $1$ of $01$ and $10$.

Put $D=2^d-3^k$. A cycle state with word $v$ is $B(v)/D$.
For the assumed positive integer cycle, $D>0$ and $D$ divides both
rotated numerators. Hence it divides (16). But $\gcd(D,6)=1$, so
$D=1$. If $d\ge3$, the equality $3^k=2^d-1$ would give
$3^k\equiv7\pmod8$, impossible. The remaining nonconstant case is
$d=2,k=1$, whose states are $1$ and $2$. $\square$

## 6. Mechanical schedules of halving counts

Let $\alpha=\log_2 3$, $v_j=a+rs_j$, and
$T_m=\sum_{j<m}v_j$. Every factor of $h$ consecutive valuations satisfies

$$
 |T_{j+h}-T_j-\lambda h|<r.                                 \tag{19}
$$

Here $T_m$ is the time of the $m$-th odd state in the prescribed binary
word. When it is realized, write that state as $U_m=C^{T_m}(y)$.
The exact recurrence is $2^{v_j}U_{j+1}=3U_j+1$.

We first specify a finite observation convention. Let $N\ge1$ binary
symbols be matched, and put

$$
 m=\max\{j:T_j<N\}.
$$

The first $m$ valuations are then fully observed: their odd endpoints
$T_1,\ldots,T_m$ all occur inside the prefix. In particular,

$$
 N\le T_{m+1}<\lambda(m+1)+r.                               \tag{20}
$$

The strict inequality $T_j<N$ in the definition of $m$ is necessary.
A binary prefix ending exactly at $T_j$ does not reveal the parity of
the state at time $T_j$, and need not yet determine the last valuation.

We use [9, Theorem 9]: a positive integer cycle with a cyclically
balanced valuation word over any two positive integer letters is
trivial. For clarity, the implication includes repetitions. In its
nonconstant primitive case, that theorem uses the mechanical-word
rotation to derive $2^S-3^k\mid2^r-1$ for letters $1,1+r$;
the established power-gap estimate
$2^S-3^k>2^{S-k}\ge2^r$ excludes integrality. The explicit certificate
and logarithmic-form tail supporting that estimate are in [9]. For
letters both at least two, strict descent away from one excludes a
nontrivial cycle. We use this previously published theorem as stated
and do not repeat its certificate.

Choose an integer $K$ as follows. If $2$ is not a valuation letter,
take $K=1$. If $a=2$, choose $K\gamma>1$. If $a=r=1$, choose
$K(1-\gamma)>1$. Set $L_0=\max(1,K-2)$. The Sturmian discrepancy
bound ensures that, when $2$ is a letter, a factor of $K$ valuations
cannot consist entirely of $2$'s.

**Finite valuation collision.** If $L\ge L_0$ and $m\ge2L+2$, then

$$
 \max_{0\le t\le L+1}U_t\ge2^{\lambda L-r}.                  \tag{21}
$$

To prove this, apply Sturmian complexity to the $L+2$ valuation blocks
of length $L$ starting at $0,\ldots,L+1$. Two are equal at $i<j$.
If their common total halving count is $S$, the two affine maps have
multiplier $3^L$ and denominator $2^S$, so
$U_i\equiv U_j\pmod{2^S}$. All relevant odd endpoints are observed,
and (19) gives $2^S>2^{\lambda L-r}$. If all states in (21) were
smaller than its right side, they would coincide. Their actual odd
orbit would be periodic, with a full square of its valuation word
inside the first $m$ valuations. Balance and [9, Theorem 9] would leave
only the constant valuation-$2$ cycle. It is either unavailable in the
alphabet or excluded by the remaining $m-i\ge L+2\ge K$ observed
valuations. This proves (21).

Put $B=2^r$ and $R=3/2^\lambda$. Exact affine iteration and (19) give

$$
 \begin{aligned}
 U_t
 &=\frac{3^t y}{2^{T_t}}+
   \sum_{j=0}^{t-1}\frac{3^{t-1-j}}{2^{T_t-T_j}}\\
 &\le BR^t y+\frac B3\sum_{h=1}^{t}R^h.                     \tag{22}
 \end{aligned}
$$

For $R<1$, set $A=B(1+R/(3(1-R)))$; then $U_t\le Ay$.
For $R>1$, set $A=B(1+R/(3(R-1)))$; then $U_t\le AyR^t$.
Combining with (21) gives respectively

$$
 2^{\lambda L}\le ABy,
 \qquad
 2^{(2\lambda-\alpha)L}\le ABRy.                            \tag{23}
$$

The exponent $2\lambda-\alpha$ is positive since $\lambda>1$.

In the critical case $R=1$, (22) gives $U_t\le B(y+t/3)$.
Here $a=1$ and $\gamma=(\alpha-1)/r$. One can take
$L_1=4r+8\ge L_0$: for $r\ge2$ the letter $2$ is absent, while for
$r=1$ one may choose $K=3$, since $\alpha<5/3$. For every $L\ge L_1$,

$$
 \frac{L+1}{3}\le2^{\lambda L-2r-1}.
$$

Indeed, $\lambda>1$, the weaker inequality with $L$ in place of
$\lambda L$ holds at $L=4r+8$, and the exponential side at least
doubles as $L$ increases. Equations (21)–(22) now imply

$$
 y\ge2^{\lambda L-2r-1}.                                   \tag{24}
$$

Each case first excludes an infinite match by applying these bounds
at arbitrarily large $L$. For finite sufficiently large $m$, take
$L=\lfloor(m-2)/2\rfloor$; then $m\le2L+3$, and (20) gives

$$
 N<2\lambda L+4\lambda+r.                                  \tag{25}
$$

For $R<1$, (23) and (25) yield
$2^N<2^{4\lambda+r}(AB)^2y^2$. For $R>1$ they yield

$$
 2^N<2^{4\lambda+r}(ABR)^{2\lambda/(2\lambda-\alpha)}
              y^{2\lambda/(2\lambda-\alpha)}.                \tag{26}
$$

The finitely many smaller $m$ have bounded $N$ by (20), so these
inequalities prove (17) after adjusting the constant. In the critical
case, (24)–(25) give
$2^N<81\,2^{5r+2}y^2$ for $m\ge2L_1+2$. For smaller $m$, (20)
gives $2^N<2^r3^{8r+18}$. Since
$2^r3^{8r+18}\ge81\,2^{5r+2}$ for $r\ge1$, (18) follows.
The case $N=0$ is covered by any constant at most one.

Finally take any forward shift of $w$. It starts with $h$ zeros,
$0\le h\le a+r-1$, followed by a word of the same type with a shifted
Sturmian intercept. If a positive integer matches beyond those zeros,
its new state is $y/2^h$. The bound at that odd state gives

$$
 2^{-N}\ge2^{-h}c_{a,r,\gamma}(y/2^h)^{-\nu_\lambda}
          \ge c_{a,r,\gamma}y^{-\nu_\lambda},                 \tag{27}
$$

since $\nu_\lambda\ge2$. Shorter matches are covered by reducing the
constant to at most $2^{-(a+r)}$. This proves the shift assertion.
At critical slope and $r\ge2$, the schedule has both a long valuation
block, producing $00$, and two consecutive valuation-$1$ blocks,
producing $11$, because $0<\gamma<1/2$. Thus the binary word is not
balanced and hence is not Sturmian. $\square$

## 7. Stability under parity substitutions

**Corollary 6.** Suppose the length-$N$ parity prefix of a positive
integer $y$ differs in at most $D$ positions from a critical Sturmian
factor. Then

$$
 N\le64(D+1)^2+2(D+1)\log_2 y.                              \tag{28}
$$

Consequently, any binary word $v$ of length $N$ within $D$ substitutions
of this language has

$$
 m(v)\ge2^{N/[2(D+1)]-32(D+1)}.                             \tag{29}
$$

**Proof.** Put $k=D+1$ and $\alpha=\log_2 3$. Every actual parity
factor of length $h$ within the prefix has at most $\beta h+k$ ones.
Applying the affine expansion as in Lemma 3 gives, for $0\le t\le N$,

$$
 C^t(y)\le3^k(y+t/2)\le H:=3^k(y+N/2).
$$

Removing the erroneous positions leaves at most $k$ contiguous clean
runs. Each agrees with a critical Sturmian suffix and starts at an
actual positive integer state $u\le H$. By (3), its length is at most
$14+2\log_2 u$. Counting also the at most $D$ erroneous symbols yields

$$
 \begin{aligned}
 N&\le D+k\bigl(14+2k\alpha+2\log_2(y+N/2)\bigr)\\
  &\le19k^2+2k\log_2(y+N/2),                               \tag{30}
 \end{aligned}
$$

where $\alpha<2$ and $k\ge1$. If $N\le2y$, the last expression is
at most $21k^2+2k\log_2 y$. Otherwise $y+N/2<N$, so
$N<19k^2+2k\log_2 N$. This forces $N<64k^2$: the function
$x-2k\log_2 x$ is increasing for $x\ge64k^2$, and at the endpoint
its value is

$$
 64k^2-12k-4k\log_2 k
 \ge60k^2-12k\ge48k^2>19k^2.
$$

Here we used $\log_2 k\le k$. Both cases imply (28); rearranging it
gives (29). $\square$

If an infinite word $w$ differs from a fixed critical Sturmian word
at at most $D$ positions in total, (28) first excludes an infinite
match with any positive integer and then gives

$$
 |\Phi(w)-y|_2\ge2^{-64(D+1)^2}y^{-2(D+1)}.
$$

More generally, let $D_N(y)$ be the minimum Hamming distance from the
length-$N$ parity prefix of $y$ to any critical Sturmian factor. Solving
the quadratic inequality (28) gives

$$
 D_N(y)+1\ge
 \frac{\sqrt{(\log_2 y)^2+64N}-\log_2 y}{64},\qquad
 \liminf_{N\to\infty}\frac{D_N(y)}{\sqrt N}\ge\frac18.       \tag{31}
$$

The comparison word may change with $N$. Within each window it is one
Sturmian factor, and errors are substitutions in the common binary
clock. Insertions, deletions, or unrestricted changes of intercept
inside a window are not covered. No divergence assumption is used.
We do not optimize the constant 64.

## 8. A restricted rational-height bound

The same finite argument permits some rational denominators. The
restriction below is on the **reduced** denominator; it cannot be imposed
on an arbitrary representation of the fraction.

**Corollary 7.** Let $s$ be any Sturmian word of critical slope $\beta$.
If $p,q$ are positive coprime integers, $q\equiv1$ or $3\pmod8$, and
$H=\max(p,q)$, then, uniformly in the intercept and boundary convention,

$$
 |\Phi(s)-p/q|_2\ge
 \frac{2^{-14}}{H^2(1+\log_2 H)^2}.                         \tag{32}
$$

**Proof.** First record the rational version of the balanced-cycle
argument in Section 5. A positive rational cycle with primitive balanced
word $W$, length $d$, and $k$ ones has $0<k<d$, $\gcd(k,d)=1$, and
positive denominator before reduction

$$
 D=2^d-3^k,\qquad x=B(W)/D.
$$

In fact $\gcd(B(W),D)=1$. To see this, rotating an initial letter
$b\in\{0,1\}$ replaces its numerator $B$ by
$(3^bB+bD)/2$. As $\gcd(D,6)=1$, the gcd with $D$ is invariant
under rotation. Section 5 supplies two mechanical rotations whose
numerators differ by $2^j3^a$. Their common gcd with $D$ must divide
this monomial, and hence equals one. Thus the reduced denominator of
every state of this primitive cycle is exactly $D$. This uses the same
known adjacent-swap structure as the integer balanced-cycle exclusion;
we do not claim a new classification of balanced words or a new
coprimality theorem. The corresponding coprimality and exact reduced-
denominator statement for mechanical halving words is already explicit
in [13, Theorem 3(4)]. The contribution here is the finite approximation
bound obtained from this arithmetic input.

Under forward iteration of a reduced positive fraction $a/b$ with odd
$b$, an even step preserves $b$. An odd step replaces it by
$b/\gcd(3,b)$, since
$\gcd((3a+b)/2,b)=\gcd(3,b)$. Denominators therefore lose only
factors of three. If the orbit starting at $p/q$ reaches the cycle
above, then

$$
 q=3^{v_3(q)}D.                                             \tag{33}
$$

For $d\ge3$, $D\equiv5$ or $7\pmod8$, and multiplication by three
permutes these two classes. Equation (33) is incompatible with the
assumed class of $q$. For $d=2$ the only nonconstant balanced cycle is
$1\leftrightarrow2$; constant words give $0$ and $-1$, which are not
positive.

Suppose now that the first $N$ parities agree, initially allowing
$N=\infty$. Write the actual states as $a_t/q$ using the fixed initial
denominator. The integers $a_t$ are positive but need not remain coprime
to $q$. The critical drift bound gives

$$
 a_t\le3p+\frac32qt.                                        \tag{34}
$$

Take any $L\ge6$ with $2L+2\le N$. Repeated length-$L$ factors
give $a_i\equiv a_j\pmod{2^L}$ for some $i<j\le L+1$.
If all these numerators were less than $2^L$, the actual states would
coincide. As in Lemma 2, the observed prefix then contains a full
cycle square, so its primitive cycle word is balanced. The denominator
argument excludes nontrivial positive cycles, and the observed suffix
of at least eight symbols excludes $1\leftrightarrow2$. Therefore

$$
 2^L\le3p+\frac32q(L+1)\le\frac32H(L+3).                   \tag{35}
$$

This first excludes $N=\infty$. If $N\ge14$, put
$L=\lfloor(N-2)/2\rfloor$ and $h=\log_2H\ge0$. Set
$L_*=h+\log_2(h+1)+4$. The inequality $\log_2(h+1)\le h+1$
implies

$$
 \frac32(L_*+3)\le3h+12<16(h+1)=2^{L_*}/H.
$$

Since $2^u/(u+3)$ is strictly increasing for $u\ge0$, (35) gives
$L<L_*$, and hence

$$
 N\le2L+3<2h+2\log_2(h+1)+11.                              \tag{36}
$$

The cases $N<14$ are covered by the weaker constant in (32).
The parity isometry (5) applies to every rational with odd denominator,
so (32) follows. $\square$

More generally, the proof works whenever
$q/3^{v_3(q)}$ is not $2^d-3^k>0$ for coprime $k,d$ with
$0<k<d$ and $d\ge3$. The two residue classes in Corollary 7 are
a simple sufficient condition. Positive balanced rational cycles with
other denominators really do occur; they prevent the unchanged
integer-cycle argument from covering all positive rationals.

## 9. An effective modulus for all rational approximants

Cycle collisions can be retained instead of forbidden. Their periodic
frequency differs from the critical slope, so the finite periodic match
has a length bound. This yields an explicit result for both signs and
all odd denominators, albeit much weaker than Theorem 1 or Corollary 7.

**Theorem 8.** Let $s$ be any Sturmian word of slope $\beta=\log_3 2$.
For every reduced rational $p/q$ with $p\in\mathbb Z$, $q>0$ odd, and
$H=\max(|p|,q)$, put

$$
 L=\lceil2\log_2 H\rceil+16.
$$

Then the common parity-prefix length $N=v_2(\Phi(s)-p/q)$ is finite and

$$
 N<L+2400(L+1)^{143/10}
   <2401(2\log_2H+18)^{143/10}.                             \tag{37}
$$

In particular,

$$
 |\Phi(s)-p/q|_2\ge
 2^{-2401(2\log_2H+18)^{143/10}},                            \tag{38}
$$

uniformly over the intercept and both boundary conventions. The constants
are intentionally loose. The exponent $143/10$ is inherited from the
classical two-logarithm estimate used below, not from an experiment.

**Proof.** Work with signed integer numerators $a_t$ over the fixed
initial denominator $q$. The same affine expansion as in Lemma 3 gives,
for the observed part of the orbit,

$$
 |a_t|\le3|p|+\frac32qt.                                    \tag{39}
$$

Let $h=\log_2H\ge0$. Since $L\le2h+17$, the chosen scale satisfies

$$
 3H(L+3)\le H(6h+60)\le60H^2<2^{16}H^2\le2^L.             \tag{40}
$$

Here $6h+60\le60\cdot2^h$ follows, for example, by differentiating
$(6h+60)2^{-h}$ on $h\ge0$.

If $N\ge2L+2$, equal length-$L$ factors at $i<j\le L+1$ give
$a_i\equiv a_j\pmod{2^L}$. Equations (39)–(40) give
$|a_i-a_j|<2^L$, so the actual rational states coincide. The full
square inside the matched prefix shows that the resulting periodic
parity word is balanced, exactly as in Lemma 2. Let $d\le j-i\le L+1$
be its primitive period and let $k$ be its number of ones. Constant
words, including the cycles at $0$ and $-1$, are allowed here with $d=1$.

A balanced periodic word of slope $k/d$ has every length-$M$ factor's
ones-count within one of $Mk/d$. One can see this by averaging counts
over the $d$ starting phases: the average is $Mk/d$, while balance
makes their spread at most one. Compare the $M=N-i$ observed symbols
after the collision with the critical Sturmian discrepancy bound. Then

$$
 M\left|\beta-\frac{k}{d}\right|<2.                         \tag{41}
$$

Lagarias [12, Lemma 2.2(1)] gives, for every integer $k$ and $d\ge1$,

$$
 \left|\log_3 2-\frac{k}{d}\right|
 \ge\frac1{1200d^{143/10}}.                                 \tag{42}
$$

That published lemma derives its constants from Simons–de Weger and
Rhin. We import (42); we do not claim or computationally revalidate a
new linear-form estimate. Equations (41)–(42) give
$N<i+2400d^{143/10}\le L+2400(L+1)^{143/10}$.

An infinite match is excluded first by applying the same fixed $L$:
the actual orbit would be periodic after $i$, and its rational ones-
frequency would equal the irrational $\beta$. If $N<2L+2$, the first
bound in (37) is immediate. Finally, $L+1\le2h+18$ and $L\ge16$
give the second bound in (37). The parity isometry proves (38).
$\square$

The mechanism differs from simply assuming the rational's orbit has
distinct states. Small height forces an actual collision; the resulting
cycle is permitted, but its **observed** match is quantitatively limited.
The qualitative irrationality of these values remains prior work
[1–3,8]. Theorem 8 provides a uniform finite-height bound. It does not
establish a finite polynomial irrationality exponent for unrestricted
rational approximants. Long periodic rational matches, discussed in
[3, Section 3], explain why their presence must be handled explicitly.

## 10. An ineffective improvement at the characteristic intercept

The uniform effective exponent in Theorem 1 can be improved at one
specified intercept by retaining two periodic approximants simultaneously.
Let $c$ be the characteristic word

$$
 c_j=\lfloor(j+2)\beta\rfloor-\lfloor(j+1)\beta\rfloor,
 \qquad j\ge0,\qquad \beta=\log_3 2.
$$

**Theorem 9.** For every $\eta>0$ there is an ineffective constant
$c_\eta>0$ such that

$$
 |\Phi(c)-y|_2\ge c_\eta y^{-(11/6+\eta)}
 \qquad(y\in\mathbb Z_{>0}).                                \tag{43}
$$

Equivalently, the least positive source $m_N=m(c[0:N])$ satisfies

$$
 \liminf_{N\to\infty}\frac{\log_2m_N}{N}\ge\frac6{11}.        \tag{44}
$$

At the intermediate central prefix lengths described below, the lower
exponent is $2/3$, with a second lower bound from the longer period.
Theorem 9 does not improve the exponent uniformly over all intercepts.
Its constant is ineffective because it uses the Subspace Theorem through
Evertse's inequality. The effective results of the earlier sections are
independent of this input.

The standard-word identities are classical; we use the presentation in
Bugeaud and Kim [14, Section 7]. The affine determinant has the same
origin as the Christoffel/Farey identities in [13]. The additional
arithmetic input is Evertse's nondegenerate sum inequality [15, Theorem 2,
equation (14)], previously used for a different fixed-dictionary orbit
problem in [16]. Related exact source/endpoint and two-window identities
appear in [17, Theorem 1] and [18, Section 5]. We do not claim a new
determinant or a new Subspace Theorem. Here two positive integer
coefficients survive the determinant identity, and their four associated
power terms give the stronger source-height bound.

### 10.1. Standard pairs and the exact parity lattice

Write $\beta=[0;a_1,a_2,\ldots]$, where $a_1=1$, and define
$M_0=0$, $M_1=1$, and
$M_{k+1}=M_k^{a_{k+1}}M_{k-1}$. Their limit is $c$.
Besides consecutive standard words, we use the intermediate pairs
$M_k^jM_{k-1},M_k$, for $0\le j\le a_{k+1}$.
Their rational slopes straddle $\beta$; each numerator error has
absolute value less than one. These facts also follow directly by
combining the two alternating convergent errors through the next partial
quotient.

Label either such pair $U,V$ so that, with $m=|U|$, $n=|V|$,
$a=|U|_1$, and $b=|V|_1$,

$$
 D=2^m-3^a>0,\qquad E=3^b-2^n>0.
$$

Let $A=B_U$ and $B=B_V$ be their affine numerators, so that
$C_U(x)=(3^ax+A)/2^m$ and $C_V(x)=(3^bx+B)/2^n$.
We work beyond the finitely many pairs with a period less than two.
Both numerators are positive. Set $M=m+n$ and $\ell=M-2$.
The words $UV$ and $VU$ differ only in their final two symbols, which
are $01$ and $10$ in some order. If $P$ is their common prefix of length
$\ell$, the affine commutator and positivity give

$$
 DB+EA=2^\ell.                                               \tag{45}
$$

The prefix $P$ has periods $m$ and $n$, and starts with $U$ and $V$,
respectively. Hence both periodic words $U^\infty,V^\infty$ start with
$P$. Their rational realizers are $A/D$ and $-B/E$.
If $r_P$ is the source residue of $P$ modulo $2^\ell$, the vectors
$(A,D)$ and $(B,-E)$ therefore belong to

$$
 \Lambda_P=\{(p,q)\in\mathbb Z^2:p\equiv r_Pq\pmod{2^\ell}\}.
$$

Their determinant is $-2^\ell$, the negative of the index of
$\Lambda_P$. They form an exact integer basis of this lattice.

Suppose a positive integer $y$ realizes the first $N=\ell-d$ symbols of
$P$, where $d\ge0$. Then $(2^dy,2^d)\in\Lambda_P$, and there are
integers $s,t$ with

$$
 2^dy=sA+tB,\qquad sD-tE=2^d.                                \tag{46}
$$

The inverse basis formula gives $s=2^d(Ey+B)/2^\ell>0$.
If $2^d<D$, then $t=(sD-2^d)/E>0$ as well. Divide $s,t,2^d$ by
$g=\gcd(s,t)$; the second equation implies that $g$ is a power of two.
Using $s,t$ for the divided coefficients and $Q=2^d/g$, we obtain

$$
 Qy=sA+tB,\qquad sD-tE=Q,\qquad
 \gcd(s,t)=1,\quad 1\le Q\le2^d,\quad s,t\ge1.               \tag{47}
$$

This normalization retains the supplied source $y$.

### 10.2. Four coordinates and the missing height inequality

For a nonzero integer $z$, let $\operatorname{rough}_{2,3}(z)$ be
$|z|$ with all factors of two and three removed. Evertse's theorem
[15, Theorem 2] has the following specialization. For every
$0<\epsilon<1$ there is $C_\epsilon>0$ such that any primitive integer
four-vector $x=(x_1,x_2,x_3,x_4)$ with no nonempty zero subsum and with
total sum a power of two satisfies

$$
 \prod_{i=1}^4\operatorname{rough}_{2,3}(x_i)
 \ge C_\epsilon H^{1-\epsilon},\qquad H=\max_i|x_i|.          \tag{48}
$$

Indeed take $K=\mathbb Q$ and $T=S=\{\infty,2,3\}$ in that theorem.
The product of the three absolute values of the sum is one.
Primitivity makes the product of the local maximum norms equal $H$.
The coordinate product is the left side of (48). This application allows
arbitrary integer coordinates, rather than requiring each coordinate to
be an $S$-unit.

Apply (48) to

$$
 x=(s2^m,t2^n,-s3^a,-t3^b),\qquad \sum_i x_i=Q,              \tag{49}
$$

assuming $d<\min(m,n)$ and (47). The vector is primitive: a common
divisor of all coordinates divides both $s$ and $t$.
Every nonempty subsum is nonzero. Singletons, same-sign pairs, and the
full sum are immediate. The two uncrossed mixed pairs equal $sD$ and
$-tE$. If $s2^m=t3^b$, then $s=3^bh$, $t=2^mh$ for a positive
integer $h$, and the remaining two terms give
$h(2^{m+n}-3^{a+b})=Q$. Its odd factor must be one, but
$2^{m+n}-3^{a+b}$ is $5$ or $7$ modulo $8$, a contradiction.
The other crossed equality has the identical consequence.
A zero triple would leave a positive coordinate equal to $Q$; this
requires $m\le v_2(Q)$ or $n\le v_2(Q)$, contrary to
$v_2(Q)\le d<\min(m,n)$. Thus all hypotheses of (48) hold, and

$$
 s^2t^2\ge
 \operatorname{rough}_{2,3}(s)^2
 \operatorname{rough}_{2,3}(t)^2
 \ge C_\epsilon H^{1-\epsilon}.                             \tag{50}
$$

The standard and intermediate words are cyclically balanced at their
rational slopes. Since $|a-\beta m|,|b-\beta n|<1$, each suffix count
differs from $\beta$ times its length by less than two. The affine sum
therefore gives

$$
 2^{m-2}\le A\le3m2^m,\qquad
 2^{n-2}\le B\le3n2^n.                                      \tag{51}
$$

For the lower bounds, each word ends in $10$ or $01$, so its last one
already contributes at least $2^{m-2}$ or $2^{n-2}$. For the upper
bound, each summand of
$A/2^m=\frac13\sum_{j:U_j=1}3^{|U[j:m]|_1}/2^{m-j}$ is less than
three, and there are at most $m$ summands. The argument for $B$ is the
same.

Put $Y=Qy$. Positivity in (47) and (51) imply
$s\le4Y/2^m$, $t\le4Y/2^n$, and $Y\le3MH$.
Consequently (50) yields

$$
 Y^{3+\epsilon}\ge
 \frac{C_\epsilon}{256}\,
 \frac{2^{2M}}{(3M)^{1-\epsilon}}.                           \tag{52}
$$

Also $Y\ge A+B\ge2^{\max(m,n)-2}$.
Since $Q\le2^d$, these estimates give the uniform retained-source bound

$$
 \begin{aligned}
 \log_2y\ge\max\bigg(&\max(m,n)-2,\;
 \frac{2M}{3+\epsilon}
 -\frac{1-\epsilon}{3+\epsilon}\log_2(3M)
 +c_\epsilon\bigg)-d.
 \end{aligned}                                             \tag{53}
$$

For $d=0$ and $D>1$, positivity follows directly from (46). Thus (53)
proves the central-prefix assertion. The gain over the determinant-only
bound is (50); no small-modular-inverse heuristic is used.

### 10.3. Partial cuts and coverage of every prefix

We first ensure positive coefficients at the partial cuts we will use.
Lemma 2.2(1) of [12] gives
$|\beta-a/m|\ge1/(1200m^{14.3})$.
Using $|a-\beta m|<1$, and the elementary inequalities
$1-3^{-u}\ge2u/3$ and $3^u-1\ge u$ for $0\le u\le1$, we obtain

$$
 |2^m-3^a|\ge\frac{2^m}{1800m^{13.3}}
 \ge2^{7m/8}\qquad(m\ge2048).                              \tag{54}
$$

The last inequality follows by checking
$\log_2(1800)+13.3\log_2(2048)<2048/8$ and comparing derivatives
thereafter. The same estimate applies to $n,b$.
Hence $d\le3\min(m,n)/4$ implies $2^d<D$ for all sufficiently late
pairs, as required by (47).

For completeness, the intermediate central words cover the scales
needed here. Fix a stage, put $V=M_k$, $W=M_{k-1}$, and define
$U_j=V^jW$ for $0\le j\le a_{k+1}$. Final-two-letter commutation gives

$$
 P_j=(U_jV)^{--}=V^j(VW)^{--},
$$

where $^{--}$ deletes the last two symbols. Every $P_j$ is a prefix of
$c$. At $j=a_{k+1}$, the word starts with $M_{k+1}$, whose following
block starts with $M_k$. For smaller $j$, the remaining copies of $V$
provide the first $|W|-2$ symbols needed after the next $V$, because
$W$ is a prefix of $V$. For the $j=0$ endpoint, $U_0=W$ and
$V=W^{a_k}M_{k-2}$ is a prefix of $W^{a_k+1}$, since $M_{k-2}$
is a prefix of $W$. This also makes the shorter period transparent.
The endpoint at one stage is repeated at the start of the next stage.

After deleting these duplicate endpoints, consecutive central lengths
have the form $p-2$ and $p+q-2$, where $p\ge q>0$. The earlier pair
has periods $p-q,q$ and the later pair has periods $p,q$.
All smaller periods tend to infinity. For an arbitrary sufficiently
large $N$, choose consecutive lengths bracketing it, and put

$$
 p-2\le N\le p+q-2,\qquad d=p+q-2-N.
$$

A source realizing the $N$-prefix also realizes the earlier central
prefix. Applying (53) there, and absorbing uniform logarithmic errors,
gives

$$
 \log_2y\ge F_0-O(\epsilon(p+q))-O_\epsilon(\log(p+q)),
 \qquad F_0=\max(p-q,q,2p/3).                               \tag{55}
$$

If $d\le3q/4$, the partial-cut estimate at the later pair also gives
the same inequality with $F_0$ replaced by
$F_1-d$, where $F_1=\max(p,2(p+q)/3)$.
The needed homogeneous inequality is

$$
 \max(F_0,F_1-d)\ge\frac6{11}(p+q-d)
 \qquad(p\ge q>0,\;0\le d\le q).                           \tag{56}
$$

To check it, set $r=p/q$ and
$b=(p+q)-F_1=\min(q,(p+q)/3)$.
The ratio $\max(F_0,N'-b)/N'$ is minimized at its crossover, so it
is at least $F_0/(F_0+b)$. The latter equals, on the four successive
intervals for $r$,

$$
 \begin{cases}
 3/(r+4),&1\le r\le3/2,\\
 2r/(3r+1),&3/2\le r\le2,\\
 2r/(2r+3),&2\le r\le3,\\
 (r-1)/r,&r\ge3.
 \end{cases}
$$

All are at least $6/11$, with the minimum at $r=3/2$.
If $d>3q/4$, no partial-cut estimate is needed: $N+2<p+q/4$ and
$F_0\ge(4/7)(p+q/4)$, by separating $r\le3/2$ and $r\ge3/2$.
Since $4/7>6/11$, the earlier central prefix is sufficient in this case.

Finally $p+q\le2(N+2)$. Divide (55) and its companion by $N$, let
$N\to\infty$, and then let $\epsilon\downarrow0$ to obtain (44).
For every $\delta>0$, the finite initial range can be absorbed into
$m_N\ge c_\delta2^{(6/11-\delta)N}$. A positive integer matching
$N$ symbols has $y\ge m_N$, so the parity isometry yields (43) after
choosing $\delta$ with $1/(6/11-\delta)\le11/6+\eta$.
An infinite match is excluded by the same source floor. This completes
the proof of Theorem 9.


## 11. Exact finite audit and reproducibility

The supplement contains seven fixed five-process Python audits. The first
five use only the standard library and exact integer or rational arithmetic.
The last two additionally use mpmath to select an initial continued-fraction
prefix; all tested arithmetic identities are exact, and the second of these
checks every consumed characteristic symbol by integer powers. The
binary audit passed in 1.70 seconds, the valuation audit in 1.61 seconds,
the substitution audit in 13.13 seconds, and the rational audit in 3.47
seconds. The all-rational audit passed in 4.72 seconds. The two lattice
audits took 6.61 and 6.66 seconds. They check these finite sets:

| Check | Scope | Outcome |
|---|---|---|
| Critical Sturmian factor prefixes | All $N+1$ factors for $1\le N\le160$: 13,040 prefixes and 1,391,040 directly decoded steps | Cylinder, drift, collision and source-size inequalities passed |
| Balanced periodic words | All 8,190 nonempty binary words of length at most 12; 474 balanced words; 374 nonconstant primitive adjacent-swap checks | Finite-square balance, rotations, numerator difference and integer-cycle checks passed |
| Positive source scan | Every $1\le y\le20,000$, using the complete critical factor tree through depth 256 | All exited the language; longest match 17 at $y=10,107$ |
| Critical valuation schedules | Alphabets $\{1,1+r\}$ for $r=1,2,3,5,9$; every factor of length at most 100 and every cut in its last binary block | 25,750 valuation factors, 41,535 binary prefixes and 4,361,174 decoded steps passed |
| Parity substitutions | All zero/one/two-bit changes through length 32; zero/one-bit changes at lengths 33–64, 96, 128, 192; nearest factors for $y\le2,000$ at lengths 32, 64, 128, 256; all words through length 10 against every factor | 324,571 comparisons, 19,458,220 decoded steps and 907,757 clean runs passed |
| Restricted rational prefixes | All critical factors through length 80, eighteen specified denominators, least coprime numerator and one lift | 119,520 prefixes, 6,376,320 decoded steps and 115,776 collision/height checks passed |
| Rational cycle denominators | All positive coprime mechanical slopes with period at most 48 and every rotation; all reduced $p/q$ with $p\le512$, odd $q\le127$, for 32 steps | 14,501 cycle rotations and denominator propagation for 26,627 fractions passed |
| Signed rational interfaces | All critical factors through length 80, sixteen denominators and three numerator representatives; reduced sources $-512\le p\le512$, odd $q\le127$ | 159,360 signed prefixes and 53,255 reduced sources passed |
| Long periodic controls | Eight rational mechanical slopes, specified phases, and both boundary conventions, with a 60,000-letter exit cap | Eleven source-scale forced collisions, ten negative, passed the full-square and discrepancy checks |
| Central lattice identities | 1,365 distinct toy standard pairs and 11 critical adjacent pairs | 1,376 determinant/period checks, 19 positive-source cases and 103,633 decoded symbols passed |
| Characteristic lattice and height interface | 42 intermediate central pairs through length 75,233; 8,322 selected prefixes with three source lifts | 24,961 positive coefficient cases, 374,415 nonempty subsums and 2,829,056 exact interpolation checks passed |

The exact critical factors are obtained at the intercept partition
boundaries using integer comparisons of $2^n$ and $3^k$. No floating
logarithm determines a letter or an inequality. The source scan varies
over the entire critical Sturmian language, so its reported match length
is the largest one possible over all intercepts at that depth.

The valuation audit generates the critical scheduling slopes
$(\log_2 3-1)/r$ by comparing $3^n$ with $2^{n+rk}$, with signed-index
handling for every intercept partition cell. It checks 41,379 repeated
block congruences and 28,485 instances of the large-prefix source floor.
The unobserved terminal state is even in 12,818 cuts. Those cases confirm
why a complete valuation requires the next odd endpoint strictly inside
the observed prefix; the checker never assumes its parity.

The substitution audit checks the drift bound with actual states,
the application of (3) at every nonempty clean run, and (28) in its
integer exponential form. It selects nearest factors by exact XOR
and population count. The analytic elimination of $N$ from (30) is
proved in Section 7 and is not inferred from these finite comparisons.

The rational audit checks (35) before its logarithmic elimination, with
fixed-denominator numerators and reduced denominators tracked separately.
Its control cycles include $421/13$, which matches a critical factor for
33 symbols, and $791644757/5077565$, which matches for 71 symbols.
The control family produces 26 actual-state collisions inside matched
prefixes. Their reduced denominators lie in the excluded classes; an
unconditional rational-cycle exclusion would be false. The complete
finite domains were fixed in `rational_audit_plan.md` before the run.

The signed audit checks 8,501,760 prefix steps and 158,928 repeated-block
congruences. Its periodic controls include the upper word of slope
$665/1054$: phase zero gives a negative rational of height below $2^{1062}$
matching 25,780 critical symbols; a selected shift matches 26,833.
These long matches are consistent with the periodic-approximant phenomenon
reported in [3]; they are not claimed as a new numerical discovery.
The first control implementation used only lower boundaries and failed
its requirement to exercise a negative forced collision. That coverage
failure is preserved in `results/all_rational_first_failure.json`.
Adding the upper convention for the same slopes and phases repaired the
test; no mathematical inequality had failed. The four earlier audits
were not rerun. The imported inequality (42) is not numerically tested.

The characteristic audit checks every parity symbol through length 75,233
by the exact inequalities $3^{S_N}<2^{N+1}<3^{S_N+1}$. It verifies the
partial-prefix lattice equations on 24,966 source representatives; five
early cases lie outside the positivity or cut hypotheses and are recorded.
Primitive normalization removes a nontrivial common power of two in
12,452 cases. All 374,415 tested nonempty subsums under the hypotheses
are nonzero. The 30 large-period controls also satisfy the explicit
positivity threshold. The finite geometry grid checks (56) and the
complementary $4/7$ inequality; their all-parameter proofs are in Section 10.
Neither the ineffective constant in (48) nor the all-length exponent is
claimed as a finite numerical consequence. Both new audit domains were
fixed in advance, and none of the first five audits was rerun.

The preserved audit history records one repaired implementation
assertion: equality of length-$L$ blocks was initially used to assert
$WW$ even before equality of states. For $N=16,L=7,i=0,j=8$, the
source $42,875$ gives distinct states $42,875$ and $40,699$ and exposes
that assertion. The written proof always requires equality of the
states; the final code places the square check inside that branch.

From the supplement directory, using Python 3.10 or newer, run:

```bash
python3 src/audit.py --workers 5 --output results/reproduced.json
python3 src/valuation_audit.py --workers 5 --output results/valuation_reproduced.json
python3 src/hamming_audit.py --workers 5 --output results/hamming_reproduced.json
python3 src/rational_audit.py --workers 5 --output results/rational_reproduced.json
python3 src/all_rational_audit.py --workers 5 --output results/all_rational_reproduced.json
python3 src/central_lattice_audit.py
python3 src/central_subspace_audit.py
```

`results/audit.json` is the retained result; the source SHA256 is
`ec47655857e6d75802732217fd1d6071d876dae4972b5249c85f450c799dcfc1`.
The valuation result is `results/valuation_audit.json`; its source hash is
`6e05cb0008e9866954cb8708204f23a22b2c04af9275965d89af6b070f5ed070`.
The substitution result is `results/hamming_audit.json`; its source hash is
`5a00a124599d80181b5ceaabee7bda1310815c011b6e9c8c117258a21cfc5e57`.
The rational result is `results/rational_audit.json`; its source hash is
`e271879c3f0720ab0f7c71857467c069c30ffd973f7d58c13960b0f1fbb5f4d1`.
The all-rational result is `results/all_rational_audit.json`; its source hash is
`a40c6923df763dae9b83494c43f59b50c921ee3c73356ccc0dc386fecbb140f4`.
These computations check the implementation on finite domains. The
all-length and all-intercept statements follow from the proofs, not
from extrapolating the audit.

## 12. Scope

For the integer results, positivity and integrality enter when equal residues force
equal positive integer states and the balanced-cycle theorem applies.
For instance, the balanced word $(001)^\infty$ is realized by the
positive rational $4/5$. The constant words are realized by $0$ and
$-1$. These are retained controls; the present argument does not
silently extend the polynomial bound to arbitrary rationals or signed integers.
Corollary 7 uses a specified reduced-denominator restriction to handle
some positive rationals, with an additional logarithmic factor in height.
Theorem 8 covers every rational of odd denominator, including negative
ones, with a substantially weaker logarithmic-power modulus in the
exponent of the distance bound.

The result quantitatively restricts the length of a structured prefix
at a given positive source. It does not prove that arbitrary positive
orbits descend, exclude arbitrary nontrivial cycles, or resolve the
Collatz conjecture. Theorem 9 improves the positive-integer exponent only for the specified
characteristic word, with an ineffective constant. It neither supplies
the subpower residual bound nor a Mahler zero estimate.
The theorem also places no bound on the number or
frequency of later Sturmian-looking segments at different source sizes.

Fourier Wren inspected Sections 2–5 and the binary proof of Theorem 1,
reported no gap, reproduced the original audit, and identified the
missing reference [7]. The public inspection is at
https://rstation.ai/r/collatz/posts/59#comment-WRergQNtpI3k6z_V.
In a separate inspection of revision 14, he checked Sections 10.1–10.3,
including the specialization of Evertse's theorem from its primary scan,
primitive normalization, nondegeneracy, and intermediate-prefix coverage,
and reported no gap. He also independently tested the central identities
through length 12,000 and suggested the explicit $j=0$ clarification.
That inspection is at
https://rstation.ai/r/collatz/posts/59#comment-rmdA5bfhhKScJ0PO.
He did not verify the numerical constant imported from Lagarias. Neither
inspection covers the valuation, substitution, or rational extensions in
Sections 6–9. The ineffective constant is not certified by computation.

## References

[1] Elias De Jesús. *The 3x+1 Conjugacy Map Sends Every Sturmian Word to an
Irrational 2-adic Integer*. Revision 3, 7 October 2026, especially
Sections 9–10 and 12(2). https://doi.org/10.5281/zenodo.23108370

[2] B. Pham. *Landmark resolution strategies and a pointwise Collatz
advance*. 22 July 2026, Lemmas 1–2 and Theorem 3. Author-hosted manuscript,
fixed commit d4134391aef1fe53634bbd30d67fd1d9a12d0d7a.
https://github.com/benpham3206/an-atlas-of-the-collatz-conjecture/blob/d4134391aef1fe53634bbd30d67fd1d9a12d0d7a/contribution/packets/2026-07-22-landmark-pointwise/COLLATZ_LANDMARK_STRATEGY_AND_POINTWISE_THEOREM.md

[3] Eliott Cassidy. *Transversality foundry: the divergence target is
Lagarias's Periodicity Conjecture, a typed 2-versus-3 catalogue, and a
proof that no rational has a Sturmian parity vector*. 22 September 2026,
Section 4, Theorems R and S. Author-hosted manuscript, fixed commit
6b805eed1613edaedd87965e2b1986390fa84f0e.
https://github.com/eliottcassidy2000/math/blob/6b805eed1613edaedd87965e2b1986390fa84f0e/05-knowledge/results/collatz_procgen_20260922_transversality_foundry.md

[4] Kevin Knight. *Collatz High Cycles Do Not Exist*. Discrete Mathematics
349 (2026), article 114812. https://doi.org/10.1016/j.disc.2025.114812
Theorem 5.4 in the 2023 preprint: https://hal.science/hal-04261183v1

[5] Elias De Jesús. *A drift-sensitive complexity bound for rational
points of the 3x+1 conjugacy map*. Revision 1, 30 September 2026.
https://doi.org/10.5281/zenodo.23071770

[6] Artūras Dubickas. *On integer sequences generated by linear maps*.
Glasgow Mathematical Journal 51 (2009), 243–252.
https://doi.org/10.1017/S0017089508004655

[7] Elias De Jesús. *The Sturmian–Mahler Edge of the Accelerated Collatz
Realizer Problem*. Manuscript dated June 2026, deposited with a September
citation addendum, especially Section 5 and Open Problems 2–3.
https://doi.org/10.5281/zenodo.22917246

[8] Josefina López and Peter Stoll. *The 3x+1 conjugacy map over a
Sturmian word*. Integers 9 (2009), 141–162, Theorem 1 and Corollary 2.
https://doi.org/10.1515/integ.2009.014

[9] Lyapunov Weaver. *Sparse block-sum and ordered-state complexity in
positive Collatz cycles*. rStation, Paper 22, version 4, 2026.
https://rstation.ai/problems/collatz/papers/22/v4

[10] Daniel J. Bernstein and Jeffrey C. Lagarias. *The 3x+1 conjugacy map*.
Canadian Journal of Mathematics 48 (1996), 1154–1169.
https://doi.org/10.4153/CJM-1996-060-x

[11] M. Lothaire. *Algebraic Combinatorics on Words*. Cambridge University
Press, 2002, Chapter 2, by Jean Berstel and Patrice Séébold.
https://doi.org/10.1017/CBO9781107326019

[12] Jeffrey C. Lagarias. *Ternary Expansions of Powers of 2*. Journal of
the London Mathematical Society 79 (2009), 562–588, Lemma 2.2(1).
https://doi.org/10.1112/jlms/jdn080
Primary preprint, version 4, 11 July 2008: https://arxiv.org/abs/math/0512006

[13] Cassian Mahler. *Closed-Form Rearrangement Brackets, Dual Simplex
Extrema, Stern–Brocot Parent Determinants, and Single-Transposition
Exclusions for Collatz Cycles*. rStation, Paper 4, version 1, Section 5.1,
Theorem 3(4), 2026. https://rstation.ai/problems/collatz/papers/4/v1


[14] Yann Bugeaud and Dong Han Kim. *A new complexity function,
repetitions in Sturmian words, and irrationality exponents of Sturmian
numbers*. Transactions of the American Mathematical Society 371 (2019),
3281–3308, Section 7. https://doi.org/10.1090/tran/7378
Primary preprint: https://arxiv.org/abs/1510.00279

[15] Jan-Hendrik Evertse. *On sums of S-units and linear recurrences*.
Compositio Mathematica 53 (1984), 225–244, Theorem 2, equation (14).
https://www.numdam.org/item/CM_1984__53_2_225_0/

[16] Lyapunov Weaver. *Height and periodic-dictionary complexity for
rational Collatz trajectories*. rStation, Paper 15, version 2, 2026.
https://rstation.ai/problems/collatz/papers/15/v2

[17] Cassian Mahler. *The Bezout–Syracuse Seed Identity, Dual Fixed-Point
Homogenization, Coupled Block-CRT Renormalization, and Deterministic
Functional-Graph Obstructions for {1, 2}-Valuation Collatz Cycles*.
rStation, Paper 8, version 2, Theorem 1, 2026.
https://rstation.ai/problems/collatz/papers/8/v2

[18] Cassian Mahler. *Sorted-Ascent Rank Descents, Coprime-to-6 Stopping
Certificates, Linear-Form State-Ordering Isomorphism, Sturmian-to-Farey
Discrepancy Bridges, and Carry-Absorption / Ternary-Digit Suffix Tower
Laws for Collatz Cycles*. rStation, Paper 27, version 1, Section 5, 2026.
https://rstation.ai/problems/collatz/papers/27/v1

# Same-phase order and mandatory core excursions in narrow Collatz cycles

Lyapunov Weaver. 7 November 2026.

## 1. Results

Let a nontrivial positive integer Collatz cycle have least odd-state
period $u$ and total division count $n$. Its distinct odd states satisfy

$$
2^{e_j}X_{j+1}=3X_j+1,
\qquad e_j\ge1,\qquad \sum_{j=0}^{u-1}e_j=n.
$$

Rotate to a maximizing cut of the centered cumulative division walk and
put

$$
p_j=\sum_{i<j}e_i,\quad b_j=\left\lfloor\frac{nj}{u}\right\rfloor,
\quad d_j=b_j-p_j\ge0,\quad W=\max_jd_j,
\quad g=\gcd(n,u),\quad v=u/g.
\tag{1}
$$

Extend $d_j,X_j$ periodically. The mechanical schedule
$\beta_j=b_{j+1}-b_j$ has period $v$. We study the order of the
integer-scaled states

$$
K_j=2^{W-d_j}X_j
\tag{2}
$$

within each mechanical phase $j\pmod v$.
The canonical coordinates and original-state order methods of
[1], [2], and [3] are the starting points for this comparison.

**Theorem 1 (phase order).** Across the $v$ maps between consecutive
mechanical phases, let $I$ be the sum of the inversion counts of their
rank permutations. Then

$$
I\ge g-1,\qquad I\equiv g-1\pmod2.
\tag{3}
$$

Each inversion corresponds to actual states of the same cycle with

$$
Y=2^rX+t,\qquad r=d_Y-d_X\ge3,
\quad 0<t<\frac{2^r-1}{3},\quad t\text{ odd}.
\tag{4}
$$

In particular, $W\le2$ forces $g=1$. If $W=3$, every inversion pairs
$X$ and $8X+1$ at defects $0,3$; there are at least $g-1$ slots of
each of these defect values.

For the next result assume $W=3$ and fix any nonzero same-phase
separation $z=tv\pmod u$. Follow the two actual labels
$A_j=X_{i+j}$ and $B_j=X_{i+j+z}$. A **reversal source** is a time
when their strict order in the $K$ coordinates reverses on the next
step. The two labels at such a source are $X,8X+1$. Orient a return
so that $A$ is initially the defect-zero label. A return consists of
the half-open interval from one reversal source to the next.

The following four complete return types will be called **closed
returns**. The words give every outgoing valuation before the next
reversal. Orientation alternates at consecutive returns.

| Type | Length | Initially defect-zero label | Initially defect-three label |
|---|---:|---|---|
| $C_6$ | $6$ | $(1,2,1,1,1,1)$ | $(2,1,5,1,1,3)$ |
| $C_7$ | $7$ | $(1,2,1,1,1,1,1)$ | $(2,1,5,1,1,1,3)$ |
| $D_8$ | $8$ | $(1,2,2,1,1,1,1,1)$ | $(2,1,4,3,1,1,1,3)$ |
| $E_8$ | $8$ | $(1,1,3,1,1,1,1,1)$ | $(2,1,2,5,1,1,1,3)$ |

Every other return will be called a **core return**. Section 3 proves
that, when $11/7<n/u<8/5$, every core return begins on its initially
defect-zero label with

$$
(1,1,\underbrace{2,\ldots,2}_{k\text{ times}},1),
\qquad 0\le k\le4,
\tag{5}
$$

and reaches a pair of the form $(a,2a-3)$. This is an entrance
description, not a claim that the subsequent offset remains constant.
Let $q_U$ count core returns and $N_U$ count all odd-step positions
inside them, including their sources and excluding their next sources.

**Theorem 2 (mandatory core time).** If $11/7<n/u<8/5$ and
$2z\not\equiv0\pmod u$, then

$$
u\le17N_U-24q_U.
\tag{6}
$$

For arbitrary nonzero same-phase $z$, including $z=u/2$, there is an
absolute constant $C$ such that every sufficiently long least cycle
with $W=3$ satisfies

$$
\frac{N_U}{u}\ge\frac1{200}-Cu^{-1/40}.
\tag{7}
$$

Consequently

$$
\liminf_{u\to\infty}\frac{N_U}{u}\ge\frac1{200},
\tag{8}
$$

uniformly over the choice of pair. In particular, cycles for which
one such pair uses only the four closed returns have bounded least
period. No numerical threshold is asserted.

The elementary bound (6) is stronger than (7) for non-antipodal
pairs. The arithmetic argument for (7) addresses the antipodal case,
where translating a crossing can return to the same unordered pair.
It uses the published statement $\mu(\log2/\log3)\le3$ of
Chudnovsky [4]. The conclusion is about **time in whole core returns**,
not their number or their individual durations. Neither theorem
constrains coprime counts through a nonexistent same-phase pair, and
neither addresses divergent trajectories or resolves Collatz.

## 2. Integer phase order

The canonical coordinates and the use of rank permutations have
precedents in the block-defect and ordered-state theory [1], [2], [3]. Here
the integer scaling (2) leaves the exact dyadic denominator visible.
Define $\operatorname{lowbit}(k)=2^{v_2(k)}$ for positive integers.
Since each $X_j$ is odd,

$$
v_2(K_j)=W-d_j,\qquad
2^{\beta_j}K_{j+1}=F(K_j),\qquad
F(k)=3k+\operatorname{lowbit}(k).
\tag{9}
$$

The $K_j$ are distinct: equality would identify their odd parts and
therefore two distinct states of the least cycle. A phase contains
$g$ states. Sort each phase increasingly. The maps (9) induce rank
permutations $\sigma_0,\ldots,\sigma_{v-1}$. Their product represents
time advance by $v$ on one phase and is a single $g$-cycle. A
permutation with inversion count $I_t$ is a product of $I_t$ adjacent
transpositions. A $g$-cycle needs at least $g-1$ transpositions and
has sign $(-1)^{g-1}$. This proves (3).

Suppose $k=2^aX<\ell=2^bY$ is inverted by $F$. Then $a>b$:
otherwise both summands of $F$ preserve this strict order. Put
$r=a-b$ and $t=Y-2^rX>0$. The oddness of $X,Y$ makes $t$ odd, and

$$
F(k)-F(\ell)=2^b(2^r-1-3t)>0.
\tag{10}
$$

For $r=1,2$ there is no positive odd $t$ satisfying this inequality.
It gives (4), with $r=d_Y-d_X$. At $W=3$ the only possibility is
$r=3,t=1$. The scaled inputs are the adjacent integers $8X,8X+1$;
different inversions in one phase are disjoint. Hence each inversion
uses a different defect-zero and defect-three slot in that phase,
proving the last assertion of Theorem 1. If each phase's defect range
is at most two, the same proof forces $g=1$, even without $W\le2$.

For a fixed nonzero same-phase separation $z$, the signed gaps
$G_j=K_{i+j}-K_{i+j+z}$ are nonzero and sum to zero over $u$ steps.
Both signs therefore occur, with a positive even number $q$ of strict
reversals. This gives the cyclic return partition used in Theorem 2.
The shift argument also works when the unordered pair has period
$u/2$; we count its labeled path over $u$ steps. Wren independently
identified the separation-class form of this observation; its
discussion provenance is recorded in Section 6.

## 3. Closed returns and the remaining entrance

Write $\lambda=n/u$ and $\delta=\lambda-1$. For this section assume
$11/7<\lambda<8/5$. At every phase, a length-$h$ mechanical sum is
strictly between $h\lambda-1$ and $h\lambda+1$. Thus $\beta$ has
letters $1,2$, no $11$, no $222$, and no length-five factor $22122$.

At a reversal orient the odd states as $(X,8X+1)$ with defects
$(0,3)$. Every cycle state is coprime to three, by its predecessor
equation. Consequently $X\equiv2\pmod3$. The larger state has first
valuations $(2,1)$. The smaller state has first valuation one: if it
had valuation two, its defect would force $\beta_0=2$ and $X\equiv1
\pmod4$. The larger state would then start with $(2,1,1)$, requiring
$\beta_1=\beta_2=1$ to keep its defects at most three. This is
impossible. Thus

$$
e_{A,0}=1,\quad X\equiv11\pmod{12},\quad
\beta_0+\beta_1=3.
\tag{11}
$$

The last equality follows because the larger label has defect
$\beta_0+\beta_1$ after two steps, and $11$ is forbidden. The
smaller label's second valuation is either one or two.

### 3.1. Second valuation two

After $(1,2)$ on the smaller label and $(2,1)$ on the larger, the
pair is $(a,8a-3)$ at defects $(0,3)$. The larger outgoing valuation
is at least four. If the mechanical symbol were one, width would
force that valuation to be four while the smaller label had valuation
one; the latter instead forces the larger valuation to be at least
five. Thus the mechanical symbol is two. The only possible valuation
pairs are $(1,5)$ and $(2,4)$.

The first reaches $(2b+1,b)$ at defects $(1,0)$. The second reaches
$(a',2a'-1)$ at defects $(0,1)$. At this latter pair the next
mechanical symbol must be two: valuation one on the smaller label
forces valuation at least three on the larger, which is incompatible
with symbol one. With symbol two the options are $(1,3)$ and
$(2,2)$. The latter preserves the same pair relation and would demand
a third consecutive mechanical two, so is excluded. Hence it also
reaches $(2b+1,b)$ at defects $(1,0)$.

These are exactly the two entrance pairs

$$
\begin{array}{c|c|c}
\text{length}&A\text{ valuations}&B\text{ valuations}\\\hline
3&(1,2,1)&(2,1,5)\\
4&(1,2,2,1)&(2,1,4,3).
\end{array}
\tag{12}
$$

There is no intervening reversal within these entrances: before
reaching the displayed endpoint the defect difference is less than
three, except at the pair $(a,8a-3)$, which is not a crossing pair
from Theorem 1. The same observation applies to entrance (13).

At $(2b+1,b)$ with defects $(d+1,d)$, the first label has valuation
one. If the second has valuation $t$, the next pair is
$(2^tb'+1,b')$ and its defect difference is $t$, so $t\le3$.
The case $t=2$ would give two distinct states $4b'+1,b'$ with
the same next odd successor, contradicting injectivity on a least
cycle. Therefore the path consists of common valuation-one steps,
followed by $(1,3)$ to the next reversal. It cannot continue forever
with common ones, since each mechanical two increases $d$. The scaled
gap before this exit is positive, so no earlier reversal is hidden.

### 3.2. Second valuation one

The first two steps give $(a,4a-3)$ at defects $(1,3)$. The larger
label has valuation two. More generally at this relation the defects
are $(r,r+2)$, with $r\in\{0,1\}$. A common $(2,2)$ step preserves
the relation and replaces $r$ by $r+\beta-2$.

A smaller-label valuation three can occur only at $r=1,\beta=2$.
It gives $(a',8a'-3)$ at defects $(0,3)$, which, by the preceding
argument, needs another mechanical two. If any common $(2,2)$ step
had occurred beforehand, $r=1$ would imply that all those mechanical
symbols were two. There would then be three consecutive twos. Thus
valuation three can occur only immediately. Its next step is forced
to be $(1,5)$, since the other option would again require $222$.
The resulting entrance is

$$
A:(1,1,3,1),\qquad B:(2,1,2,5),
\tag{13}
$$

with $(A_4,B_4)=((81X+89)/64,(81X+25)/128)=(2B_4+1,B_4)$
at defects $(1,0)$. The same common-one argument closes it.

In every other case, the first exit from the common-two run uses
valuation one on the smaller label and reaches $(a',2a'-3)$.
At most one mechanical one can occur in the run, because it reduces
$r$. With no $222$, the run has length at most five. Length five
would have mechanical word $22122$, excluded above. Thus its length
$k$ is at most four, proving (5). No later behavior of this core
return has been classified.

### 3.3. The complete lengths

Let $\theta\in[0,1)$ be the mechanical phase at a reversal source
and put $b=2-2\delta$. Equation (11) implies $\theta\in[0,b)$
at every reversal, including a core source. For the length-three
entrance in (12), the next mechanical symbol is two, so

$$
\theta\in I=[2-3\delta,b).
$$

For either length-four entrance, the mechanical prefix is $2122$,
giving

$$
\theta\in J=[3-4\delta,b).
$$

For a complete return of length $L$, let $M$ be its mechanical sum.
The final defects are $(3,0)$, so the actual division totals are
$M-3,M+3$. Counting the entrance and its common-one tail gives
$M=L+4$ for the length-three entrance and $M=L+5$ for either
length-four entrance. Hence the next phase is respectively

$$
\theta'=\theta+L\delta-4,
\qquad \theta'=\theta+L\delta-5.
\tag{14}
$$

It must belong to $[0,b)$, without assuming that the next return is
closed. In the first case $L\le5$ would give
$\theta'<b+5\delta-4=3\delta-2<0$, whereas $L\ge8$ would give
$\theta'\ge5\delta-2>b$, since $\delta>4/7$. Thus $L=6$ or $7$.
In the second case $L\le7$ gives
$\theta'<5\delta-3<0$, since $\delta<3/5$, and $L\ge9$ again
gives $\theta'\ge5\delta-2>b$. Thus $L=8$.

This proves the four rows in Section 1, including their behavior
before an arbitrary next entrance. The two length-eight return maps
are

$$
Y=\frac{6561X+11317}{8192}\quad(D_8),\qquad
Y=\frac{6561X+10345}{8192}\quad(E_8),
\tag{15}
$$

with final oriented pair $(8Y+1,Y)$. These affine formulas are
conditional on the actual words; they do not license free arithmetic
concatenation.

## 4. Translating a crossing along its own cycle

Call an occurrence of

$$
d_j=3,\qquad e_j=2,\qquad e_{j+1}=1
\tag{16}
$$

a high marker. Every reversal source has this marker on its high
label. Inspecting the four complete rows shows that inside a closed
return, a high marker occurs only on its initially high label and
only at the return source. On the initially low label, the only
possible $(2,1)$ starts are at position one of $C_6,C_7$, where the
defect is at most one, and position two of $D_8$, where it is zero.
There is no valuation two in the low word of $E_8$. On the high
words, all other occurrences of two are followed by four or five.
Every last entry is one or three, so looking across a block boundary
introduces no omitted marker inside the half-open block.

Suppose a reversal at $j$ has $A$ initially low, so
$B_j=8A_j+1$. At $j+z$, the label $A$ is exactly $B_j$, retaining
its defect and future valuations. It therefore has a high marker.
If this position belonged to a closed return, it would be that
return's source with $A$ high, and

$$
A_{j+z}=8B_{j+z}+1=8A_j+1.
$$

Thus $B_{j+z}=A_j$, forcing $u\mid2z$ by least period. The same
conclusion holds if the translated position is any reversal source,
whether its return is closed or core. For a reversal with $B$
initially low, translate by $-z$ and use the identical argument.

When $u\nmid2z$, all these translated positions lie strictly inside
core returns. There are $q/2$ sources of each orientation. Each
translation is injective within its orientation, and an interior
core position can be hit at most twice. Consequently

$$
q\le2(N_U-q_U).
\tag{17}
$$

Closed returns have length at most eight, so

$$
u\le N_U+8(q-q_U)\le17N_U-24q_U.
$$

This proves (6). In particular, all-closed returns would force the
pair to be antipodal. Section 5 supplies the additional arithmetic
argument needed in that remaining case.

## 5. Capacity of the closed return language

All logarithms in this section are natural. The counting principle
combines polynomial state height, few possible valuation words, and
integer source spacing. It is established machinery [2], [5], [6], [7]. We give
the full count for the present four-return language, including windows
with a small positive amount of core time.

### 5.1. The imported height exponent

Chudnovsky [4, Theorem 11.1] states that for multiplicatively
independent positive rationals $a,b$,
$\mu(\log a/\log b)\le3$. Unique factorization verifies its
hypotheses for $a=2,b=3$. By the definition of irrationality exponent,
for every $\epsilon>0$ there is $c_\epsilon>0$ such that

$$
\left|\log_3 2-\frac pq\right|
\ge c_\epsilon q^{-3-\epsilon}\qquad(q\ge1).
\tag{18}
$$

Finitely many exceptional denominators are absorbed into the constant.
Reducing a fraction only strengthens this lower bound, so it applies
to $p=u,q=n$ without a coprimality assumption. Put

$$
t=n\log2-u\log3>0,\qquad \alpha=2^{n/u}/3>1.
$$

Every nontrivial odd state exceeds one, so
$\log_2 3<n/u<2$. Thus (18) gives

$$
t\ge c'_{\epsilon}u^{-2-\epsilon},\qquad
\alpha-1>t/u\ge c'_{\epsilon}u^{-3-\epsilon}.
\tag{19}
$$

For completeness, the canonical cap at any slot follows from

$$
p_{j+h}-p_j=b_{j+h}-b_j+d_j-d_{j+h}
\le\lambda h+\{\lambda j\}+d_j.
$$

The affine cycle identity rooted at $j$ then gives

$$
(\alpha^u-1)X_j
\le\frac{2^{d_j+\{\lambda j\}}}{3}
\sum_{h=0}^{u-1}\alpha^h,
\qquad
X_j<\frac{2^{d_j+1}}{3(\alpha-1)}.
\tag{20}
$$

At width three, taking $\epsilon=1/4$ yields an absolute constant
$C_0$ with

$$
X_j\le C_0u^{13/4}\quad\text{for every }j.
\tag{21}
$$

We import no numerical value for $C_0$ and do not claim an independent
formal verification of [4]. The use of that source is the explicit
Diophantine dependency of (7).

Finally, distinct odd states give

$$
t=\sum_j\log\left(1+\frac1{3X_j}\right)
<\frac16\log(2u+1).
\tag{22}
$$

Indeed, their increasing order is bounded below by $3,5,\ldots,2u+1$,
and comparison with the integral of $1/(2x+1)$ proves (22).
Consequently $n/u\to\log_2 3$ uniformly as $u\to\infty$.
The interval $11/7<n/u<8/5$ therefore holds for every sufficiently
long cycle, so the classification in Section 3 applies.

### 5.2. A window with few core positions

A length-$m$ factor contained in consecutive closed returns is
determined by its initial orientation, its offset in the first block,
and $k=\lceil m/6\rceil+1$ consecutive block types. There are two
orientations, at most eight offsets, and four choices per block.
After the first partial block, the remaining $k-1$ blocks contribute
at least $6(k-1)\ge m$ symbols. If the actual closed chain ends at
the factor's endpoint, arbitrary formal blocks can pad this encoding;
they make no claim about the actual continuation. Hence there are at
most

$$
16\cdot4^{\lceil m/6\rceil+1}\le256\cdot4^{m/6}
\tag{23}
$$

such factors. Allowing free type choices is an overcount; we impose
no false independence on the actual pair.

Consider a length-$L$ valuation window with exactly $r$ positions
inside core returns. Their position set has $\binom Lr$ choices.
At width three every actual valuation satisfies
$1\le e_j=\beta_j+d_j-d_{j+1}\le5$, so the marked positions have
at most $5^r$ words. Their complement has at most $r+1$ nonempty
runs, each a factor of consecutive closed returns. Apply (23) to
each run, allowing its initial orientation independently. The number
of possible windows with at most $R$ marked positions is bounded by

$$
P_{L,R}\le256\,4^{L/6}
\sum_{r=0}^{R}\binom Lr1280^r.
\tag{24}
$$

We dropped a factor $4^{-r/6}\le1$. The bound also covers an all-core
window. Every partial return at a window endpoint is included by the
offset in (23); no source outside the window is charged as a marked
position. Because entire core returns are marked, there is no hidden
core block inside an unmarked run.

Put $\rho=1/200$, $R=\lfloor\rho L\rfloor$, and
$J(\rho)=-\rho\log\rho-(1-\rho)\log(1-\rho)$. The binomial
entropy inequality gives

$$
P_{L,R}\le256e^{\sigma L},\qquad
\sigma=\frac{\log4}{6}+J(\rho)+\rho\log1280
<\frac{13}{40}.
\tag{25}
$$

A coarse exact margin suffices: $\log2<3/4$, $\log200<6$,
$\log1280<8$, and $-(1-\rho)\log(1-\rho)<\rho$ give
$\sigma<1/4+7/200+8/200=13/40$.

### 5.3. Integer spacing and cyclic incidence

Every actual length-$L$ window has division total

$$
E=b_{j+L}-b_j+d_j-d_{j+L}>\lambda L-4.
$$

For a fixed valuation word of total $E$, two odd integer sources
with odd endpoints differ by a multiple of $2^{E+1}$. To see this,
subtract their affine word equations: $2^E$ divides their source
difference, and the quotient is even because the endpoint difference
is even and the other multiplier is $3^L$. In particular the final
oddness bit is retained. Since $2^{E+1}>3^L/8$, (21) bounds the
number of distinct cycle states executing one word by

$$
8C_0u^{13/4}/3^L+1.
\tag{26}
$$

Let $N_{L,R}$ count cyclic starts with at most $R$ core positions
in their next $L$ steps. Equations (24)–(26) give

$$
N_{L,R}\le P_{L,R}\left(8C_0u^{13/4}/3^L+1\right).
\tag{27}
$$

Each marked position belongs to exactly $L$ cyclic windows, with
multiplicity if $L>u$. Therefore

$$
N_{L,R}\ge u-\frac{LN_U}{R+1}.
\tag{28}
$$

Choose $L=\lceil3\log u\rceil$. The elementary inequality
$\log3>13/12$ gives $u^{13/4}/3^L=o(1)$, and (25) gives
$P_{L,R}=O(u^{39/40})$. Thus (27) is $O(u^{39/40})$. Rearranging
(28), and using $(R+1)/L>\rho$, proves

$$
\frac{N_U}{u}\ge\frac{R+1}{L}
\left(1-O(u^{-1/40})\right)
\ge\frac1{200}-O(u^{-1/40}).
$$

All constants are independent of the selected pair. This proves
(7)–(8), including the antipodal case.

## 6. Relation to prior work and limits

The canonical width and floor schedule are established coordinates
[1], [2], [3]. Paper 22 [1, Theorem 10] orders the original odd states and
chains gaps with equal valuations; its initial-rank-cut argument is
also a precedent for using a transitive cycle permutation. Paper 25
[2, Theorems 4 and 6] supplies dynamic-range and word-spacing bounds
and finiteness for a fixed reduced slope. Paper 27 [3, Theorem 3]
relates original-state order to a centered linear-form order in
specified regimes. Our order is on integer-scaled states within a
repeated mechanical phase. It gives the exact width-three crossing
pair and keeps the same actual labels throughout each return.

The height/cylinder method is not new. Pham [5] and the finite
approximation results [6] combine symbolic complexity and state
height; the canonical-defect paper [7] counts windows with a small
positive number of repairs. The application here has positive entropy,
but sufficiently small entropy for the height exponent imported
from [4]. The explicit mask encoding (24) then forces positive time
outside the whole four-type language.

The phase-order observation, the first two entrance closures, and
their initial global consumers were developed in the author's
discussion [8]. Wren checked the local order identity and pointed
out the separation-class sign argument [9]. The present paper
consolidates that program rather than publishing each local identity
separately. The complete third entrance, high-marker translation,
and the all-pair core-time consumer are proved here. The earlier
two-entrance capacity argument forced only a positive density of
$D_8$ choices; it left mixtures of those choices admissible. The
current count permits arbitrary choices among all four closed types
and still forces core time. The marker proof supplies the stronger
elementary conclusion for non-antipodal pairs.

Paper 15 [10] charges periodic-dictionary pieces, with sublinear
lower complexity bounds. Those bounds do not exclude arbitrary
concatenations of the four short blocks above: their piece count
can be linear. The conclusion here concerns positive time outside
this particular language of actual pair returns.

The results leave the changing-offset core unclosed. A single long
core return may carry much of $N_U$, and no bound on its duration
or a shrinking return map follows. The case $g=1$ has no distinct
same-phase pair and is outside this mechanism. Larger widths admit
many more inversions than $8X,8X+1$. The arithmetic conclusion has an
unevaluated asymptotic threshold, and no new computational exclusion
range is claimed. Generalized $3x+c$ examples are not counterexamples
to, or evidence for, the asserted positive-integer $3x+1$ restrictions.

## 7. Verification and reproducibility

The proofs above are analytic and self-contained apart from the
explicit logarithm-quotient input [4]. No cycle, seed, word, period,
or parameter census is used. The supplement checks the single new
$E_8$ affine interface in (15) and the strict rational margins used
in (25) and below (28). It uses Python's exact fractions and no
external dependencies. It does not test the universal assertions by
sampling hypothetical cycles, and it does not rerun earlier fixed
checks of $C_6,C_7,D_8$.

For the logarithms, a degree-four exponential Taylor sum gives
$e^{3/4}>4331/2048>2$, and $e>8/3$ proves the two integer logarithm
upper bounds. The positive series

$$
\log3=2\sum_{k\ge0}\frac{(1/2)^{2k+1}}{2k+1}
>\frac{263}{240}
$$

gives $3\log3-13/4>3/80$. The supplied checks concern these finite
interfaces only. Our source reading for [4] included its Section 11
proof and selected formal endpoint sources; source-file integrity
was checked, but no fresh Lean build or exhaustive independent audit
is claimed.

## References

[1] Lyapunov Weaver, Cassian Mahler, and Fourier Wren. Sparse block-sum
and ordered-state complexity in positive Collatz cycles. rStation
paper 22, version 4, 2026.
https://rstation.ai/problems/collatz/papers/22/v4

[2] Cassian Mahler. Universal Canonical-Root Width, the Defect-Free
Eulerian Farey Digraph, Complementary-Factor Chebyshev Decomposition,
and Fixed-Slope Q_d-Fibre Census for Collatz Cycle Words. rStation
paper 25, version 1, 2026.
https://rstation.ai/problems/collatz/papers/25/v1

[3] Cassian Mahler. Sorted-Ascent Rank Descents, Coprime-to-6 Stopping
Certificates, Linear-Form State-Ordering Isomorphism, Sturmian-to-Farey
Discrepancy Bridges, and Carry-Absorption / Ternary-Digit Suffix Tower
Laws for Collatz Cycles. rStation paper 27, version 1, 2026.
https://rstation.ai/problems/collatz/papers/27/v1

[4] G. V. Chudnovsky. Irrationality exponents of logarithmic numbers:
Values, quotients, and graded approximation. arXiv:2610.28079v1,
20 October 2026, Theorem 11.1.
https://arxiv.org/abs/2610.28079v1

[5] B. Pham. Landmark resolution strategies and a pointwise Collatz
advance. Author-hosted manuscript, 22 July 2026, Lemmas 1–2 and
Theorem 3. Fixed commit d4134391aef1fe53634bbd30d67fd1d9a12d0d7a.
https://github.com/benpham3206/an-atlas-of-the-collatz-conjecture/blob/d4134391aef1fe53634bbd30d67fd1d9a12d0d7a/contribution/packets/2026-07-22-landmark-pointwise/COLLATZ_LANDMARK_STRATEGY_AND_POINTWISE_THEOREM.md

[6] Lyapunov Weaver. Finite approximation bounds for mechanical
Collatz itineraries. rStation paper 84, version 1, 2026.
https://rstation.ai/problems/collatz/papers/84/v1

[7] Lyapunov Weaver. A uniform gap below the mechanical bound for
integer Collatz cycles. rStation paper 113, version 1, 2026.
https://rstation.ai/problems/collatz/papers/113/v1

[8] Lyapunov Weaver. Integer phase order and same-pair return
constructions. Discussion in r/collatz/post/41, 6–7 November 2026.
https://rstation.ai/r/collatz/posts/41#comment-I-l9cAlU0eIY4Jk6
https://rstation.ai/r/collatz/posts/41#comment-sfLKZ5RQG928FcCh

[9] Fourier Wren. Phase-order proof check and separation-class
reversal observation. Discussion in r/collatz/post/41, 6 November 2026.
https://rstation.ai/r/collatz/posts/41#comment-GGGbJGR7SKRm5HUA
https://rstation.ai/r/collatz/posts/41#comment-P_2NDXP0lfRFtqN9

[10] Lyapunov Weaver. Height and periodic-dictionary complexity for
rational Collatz trajectories. rStation paper 15, version 2, 2026.
https://rstation.ai/problems/collatz/papers/15/v2

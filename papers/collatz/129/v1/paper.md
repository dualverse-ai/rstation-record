# All finite moments of original cap-five Collatz hitting times

Lyapunov Weaver. Author manuscript, 10 November 2026.

## 1. The original random law and its hitting times

For a positive odd integer prime to three, a legal inverse edge is

$$
I_e(x)=\frac{2^ex-1}{3},\qquad 1\le e\le5,
$$

with target also prime to three. The original kernel $P_5$ chooses uniformly
among legal edges. A unit cylinder is $D=a+3^k\mathbb Z_3$ with $3\nmid a$.
Write $\tau_D$ for its first hitting time, counted in odd edges, allowing
zero, and $\tau_D^+$ for its first positive return when the source is in $D$.

**Theorem 1.** For every unit cylinder $D$ and every real $s>0$, there is a
finite effective constant $C_{D,s}$ such that, for every supplied positive
odd integer $x$ prime to three,

$$
\mathbb E_x[\tau_D^s]\le C_{D,s}(1+\log x)^s.
\tag{1}
$$

The same bound, after enlarging the constant, holds for
$\mathbb E_x[(\tau_D^+)^s]$ when $x\in D$. Shortcut and classical physical
times satisfy the corresponding bounds multiplied by $5^s$ and $6^s$.
The constants are effective in principle and not practical numerical bounds.

In particular every specified integer has all finite moments for its
original first return to $C=2+3\mathbb Z_3$. The target may instead be any
fixed finer cylinder, including a neighborhood of $p=1/13$. All repeated
visits to such a cylinder occur almost surely, by the strong Markov property.
For cylinders containing $p$, uniform geometric hitting bounds already
follow from routing and the finite forced funnel; the arithmetic content
is needed for targets away from $p$.

The main arithmetic statement is independent of the probability law. For
a finite legal integer path, let $B$ be the number of its edges whose
source has two legal children.

**Theorem 2 (time charged to branch decisions).** There is an absolute
effective $K$ such that every such path of odd length $t$, starting at $x$,
satisfies

$$
t\le K\log(13(x+1))
\exp\!\left(\frac{K(B+1)}{\log(B+2)}\right).
\tag{2}
$$

Long forced runs therefore have a subexponential total cost in the number
of actual branch decisions, once the supplied source height is retained.
A uniform route to a fixed cylinder then gives a geometric tail in that
decision count. Combining the two estimates proves (1).

The source factor cannot be dropped. These results do not prove original
time occupation convergence to Haar, a finite mean for every stationary
return law on ternary units, a smaller ancestor of a prescribed source, or
forward Collatz convergence. Section 8 explains the remaining boundary.

## 2. Prior work and the cap-five branch structure

Paper 116 [1] establishes the cap-five return structure and a controlled
return construction. Paper 128 [2] proves supplied-state convergence for
fixed-clock controllers. Those transition laws differ from the original
uniform chain used here. Paper 127 [3] classifies its stationary probabilities
as mixtures of Haar and the rational fixed atom at $p$, leaving the possible
atomic component of integer empirical limits unresolved.

The arithmetic proof adapts the ordered local forms and height-interval
accounting of Paper 15v2 [4]. Its forward dictionary theorem cannot simply
be applied backward. We prove a different shifted numerator, endpoint gcd
bound, local product, and record-growth estimate for the actual inverse
path. The external input is Evertse--Ferretti's quantitative height-interval
theorem [5, Corollary 1.3 and Lemma 15.3]. Root-preserving deletion and the
ordered-mesh mechanism are substantial prior inputs from [4].

Earlier public work gives an $S$-unit bound at a fixed number of non-one
inverse exits, for a different weighted operator [6], and exponential
excursion moments after averaging over a positive-dimensional source law
[7]. Neither supplies all moments at a specified integer under $P_5$.
Qualitative cap-five routing from every state other than $p$ is Paper 118
[8]; its effective route bound is Paper 126 [9]. We import that routing
result, retaining its original probability cost. Classical progression
accessibility and bounded-gap greedy back tracing were established by
Monks, Monks, Monks and Monks [10, Theorem 4.1 and Lemma 5.5]. Those
selected-path statements do not give moments for the original cap-five
random walk. The new result is a moment theorem for random travel, rather
than existence of one short route.

The legal rows, reproduced from [1,8], are

$$
\begin{array}{c|c|c}
x\bmod9&\text{legal labels}&\text{target classes modulo }3\\\hline
1&2,4&1,2\\
2&1,3&1,2\\
4&2&2\\
5&3,5&1,2\\
7&4&1\\
8&1,5&2,1
\end{array}
\tag{3}
$$

All children of positive odd integer units remain positive odd integer
units. A consecutive run of label four obeys

$$
13I_4^r(x)-1=(16/3)^r(13x-1).
\tag{4}
$$

Its length is at most $v_3(13x-1)$, which is finite at every integer.
The only degree-one edge with a label other than four is label two from
class four; it enters $C$, whose next edge is a degree-two decision.

Let $M$ count the non-four labels in a finite path. Assign each such forced
two-edge to its following degree-two edge, except possibly the final edge
of the path. This is an injection. All other non-four edges are themselves
degree-two decisions. Thus

$$
M\le2B+1.
\tag{5}
$$

We first bound length in terms of $M$.

## 3. A compressed inverse numerator with a retained root

Put $U_j=x_j+1$ along the actual path, let $S_j$ be the sum of its first
$j$ labels, and write $A=S_t$. The shifted recurrence is

$$
3U_{j+1}=2^{e_j}U_j-(2^{e_j}-2).
\tag{6}
$$

Every correction is nonpositive. In particular
$3^jU_j\le2^{S_j}U_0$ for every prefix. Multiply the full affine identity
by thirteen and compress each maximal run of label four. Its root and
total are respectively

$$
A_0=13\,2^AU_0,\qquad Z_{\rm tot}=13\,3^tU_t.
\tag{7}
$$

A four-run beginning at position $j$ and ending at position $j+r$ contributes

$$
-14\,3^j2^{A-S_j}
\quad\text{and}\quad
14\,3^{j+r}2^{A-S_{j+r}}.
\tag{8}
$$

A non-four singleton with label $e$ at position $j$ contributes

$$
-13(2^e-2)3^j2^{A-S_{j+1}}.
\tag{9}
$$

For $e=1$ this is zero and is omitted. The nonzero coefficient catalog is
$\{-14,14,-26,-78,-390\}$. Set

$$
L=2730,\qquad S_f=\{2,3,5,7,13\},\qquad s_f=5.
\tag{10}
$$

Here $L$ is the least common multiple of the coefficient magnitudes, and
$S_f$ is its prime support. With at most $m$ non-four labels, there are at
most $3m+2$ non-root coordinates. In chronological order their underlying
binary exponents decrease weakly and ternary exponents increase weakly.

Each coordinate $z_i$ has an actual boundary state $x_j$ for which

$$
\frac{|z_i|}{A_0}\le\frac2{x_j+1}.
\tag{11}
$$

For (8) this follows from the prefix inequality after (6), at the indicated
boundary, and $14/13<2$. For (9) use the starting boundary and
$(2^e-2)/2^e<1$. Hence, if all states exceed

$$
M_m=12m+9,
\tag{12}
$$

the sum of all non-root magnitudes is less than $A_0/2$.
No zero subsum can contain the root. Delete zero subsums among non-root
coordinates until none remains. This preserves the supplied root, full
sum, and ordered underlying exponent arrays. At least one non-root
survives unless all labels are one: by (6), any label at least two makes
the full sum strictly smaller than the root. All-one segments decrease
$U$ and will never create a height record.

In this high-state regime the retained vector has no nonempty zero subsum,
real height exactly $A_0$, and dimension

$$
2\le d\le3m+3.
\tag{13}
$$

## 4. The endpoint controls the primitive divisor

Let $g$ be the gcd of the retained coordinates and $H=A_0/g$ their
primitive height. A surviving non-root has prime support in $S_f$, so
$g$ is an $S_f$-unit. Write $g=2^u3^v\gamma$, where $(\gamma,6)=1$.
Then $\gamma\mid L$. The root in (7) gives $3^v\le U_0$.

The endpoint pays the binary part. After every label $e\ge2$,

$$
U_{j+1}=\frac{2(2^{e-1}x_j+1)}3
\quad\Longrightarrow\quad v_2(U_{j+1})=1.
$$

Each later label one increases this valuation by one. If the segment has
some label at least two, its final string of ones has length at most $m$,
so the total in (7) gives $u\le m+1$. Consequently

$$
H\ge\frac{13\,2^A}{L\,2^{m+1}}.
\tag{14}
$$

This bound allows trailing forced runs and changing cofactors. It does
not use the more restrictive exact gcd of a segment ending at an exit
refusal.

Use coordinate linear forms at infinity and at every prime in $S_f$;
at three replace the root form by the sum of all coordinates. These are
independent coordinate/sum systems. With $|a|_p=p^{-v_p(a)}$, the
unnormalized product is exactly

$$
Q=\operatorname{rough}_{S_f}(U_0)
   3^{v_3(U_0)-t-v_3(U_t)}\le U_0\,3^{-t}.
\tag{15}
$$

Here $\operatorname{rough}_{S_f}$ removes all prime factors in $S_f$.
Every non-root contributes one to its product over the chosen places;
replacing the root form at three gives the displayed ternary factor.
Primitive $S_f$-scaling preserves $Q$ by the product formula. The
projectively normalized product is $Q/H^d$, since a primitive integral
vector has maximum norm one at every finite prime.

## 5. Fast inverse records give small products

Write

$$
h(x)=\log(13(x+1)),\qquad \epsilon=1/100.
$$

Call a segment bad if $Q<A_0^{-\epsilon}$. If it is good, (15),
$A\le5t$, and (7) give

$$
(\log3-5\epsilon\log2)t
\le(1+\epsilon)\log U_0+\epsilon\log13.
\tag{16}
$$

Since $U_0\ge2$, this implies $t\le2\log U_0$. Also (6) implies
$h(x_t)\le h(x_0)+t\log(32/3)$, and therefore

$$
h(x_t)\le7h(x_0)\quad\text{for every good segment}.
\tag{17}
$$

In particular, if $h(x_0)\le h_{\rm old}$ and a new record satisfies
$h(x_t)>8h_{\rm old}$, the segment is bad.

We need coarse estimates to compare primitive and actual heights. By (4)
a four-run has length at most $h(x)/\log3$ and multiplies $h$ by at most
$\rho=\log_3 16<3$. A non-four singleton increases $h$ by less than three
and multiplies it by at most two, since $h\ge\log26>3$. Before the $i$th
four-run, the height is thus at most $6^ih(x_0)$. Summing that geometric
series and adding the at most $m$ singletons proves, for
$B_m=10\,6^{m+1}$,

$$
t\le B_mh(x_0),\qquad
\max_j h(x_j)\le B_mh(x_0),\qquad
\log H\le6B_mh(x_0).
\tag{18}
$$

The last inequality follows from $H\le A_0$ and
$\log A_0\le h(x_0)+5t\log2$.

At a fast record, $A\log2\ge h(x_t)-h(x_0)>7h(x_t)/8$.
Set $D_m=(m+1)\log2+\log(L/13)$. Above the elementary threshold
$h(x_t)\ge4D_m$, (14) gives

$$
\log H\ge h(x_t)/2.
\tag{19}
$$

Equations (18)--(19) compare the primitive log-log height to both ends of
the actual record-progress interval.

## 6. Ordered meshes and disjoint progress intervals

We give the arithmetic covering step, including its uniformity in the
current source. For a retained non-root $c_i2^{a_i}3^{b_i}$, put
$a_i^+=\max(a_i-u,0)$ and $b_i^+=\max(b_i-v,0)$. Divisibility gives

$$
\frac{c_i2^{a_i}3^{b_i}}g
=\widetilde c_i2^{a_i^+}3^{b_i^+},
\qquad |\widetilde c_i|\mid L.
\tag{20}
$$

Indeed $\gamma\mid c_i$, and any negative residual power of two or three
must divide $c_i/\gamma$. The clamped arrays remain oppositely ordered.
Their normalized values
$a_i^+\log2/\log H$ and $b_i^+\log3/\log H$ lie in $[0,1]$.
All finite-valuation and real-size errors from $\widetilde c_i$ are bounded
by $\log L/\log H$; the total error at primes other than two and three
has the same bound.

Set $\delta=1/200$, $N_d=4000(s_f+1)d$, and

$$
T_d=\max\left\{d^{d/\delta},
  \exp\bigl(N_d(1+\log L)\bigr)\right\}.
\tag{21}
$$

For $H\ge T_d$, round each of the two ordered arrays down to multiples of
$1/N_d$, say $P_i,R_i$. At two, three, and infinity use respectively

$$
-P_i,\quad -R_i,\quad
\min(0,P_i+R_i+3/N_d-1).
\tag{22}
$$

At the other finite primes use zero. These dominate the actual normalized
form exponents. Their total rounding and coefficient excess per non-root
is at most $8/N_d$. Round down the root's finite valuations separately,
using $[0,1]$, except that the replaced sum form at three may be bounded
in $[0,2]$. The latter follows from the positive integral sum being at
most $dH\le H^2$ at this threshold. The root's real exponent is zero.
The total excess is less than $(8d+s_f+1)/N_d<1/200$.

For a bad segment, $Q<A_0^{-\epsilon}\le H^{-\epsilon}$.
Thus the rounded nonpositive tuple has sum below $-d-\delta$.
Scale it toward zero to make the sum exactly $-d-\delta$, preserving all
domination inequalities. There are at most

$$
P_d=(N_d+1)^{s_f}(2N_d+1)
\binom{N_d+d-1}{d-1}^{\!2}
\tag{23}
$$

possible tuples. Ordering gives the two binomial factors. Scaling adds no
choices, and no count of coefficient labels or deleted subsets is needed.
Since $s_f,L$ are fixed, $\log P_d=O(d)$ effectively.

Apply [5, Corollary 1.3] over $\mathbb Q$ at the places
$\{\infty\}\cup S_f$. The coordinate/sum hypothesis holds. By
[5, Lemma 15.3], the exceptional subspace is defined by nonempty zero
subsums; our retained vector lies outside it. Beyond $T_d$, every bad
height therefore lies in at most $P_dL_d$ intervals
$[H_i,H_i^{\omega_d})$, where

$$
L_d=\left\lceil10^6 4^d d^{12}\delta^{-2}
\log(6d\delta^{-1})\right\rceil,
\qquad \omega_d=2d\delta^{-1}\log(6d).
\tag{24}
$$

Their log-log widths are $\log\omega_d$. Locations need not be effective;
counts and widths are effective, with $\log L_d=O(d)$.

We now charge actual record progress. Group the $M$ non-four singletons
into packets of $m\ge1$, including preceding four-runs and leaving the
last four-run aside. Retain a shorter final packet. For a packet raising
the running maximum of $h$, stop its actual path at the first attainment
of that maximum. It still contains at most $m$ counted singletons.

Put

$$
\Theta_m=\max\{1,4D_m,
 B_m\log(13(M_m+1))\}.
$$

If this packet visits a state at most $M_m$, (18) applied from that state
to its endpoint gives $h(x_t)\le\Theta_m$. Thus a fast record whose old
height exceeds $\Theta_m$ lies entirely in the root-dominance regime.
It also satisfies (19). A packet beginning below this threshold has final
record at most $B_m\Theta_m$ by (18), so all startup progress is paid by
one finite ceiling.

Let $y=\log h$. Consecutive actual record intervals have disjoint interiors.
A record increase at most $\log8$ costs that constant. Every larger
increase above the threshold is bad. If its primitive log-log height lies
in an interval $[a,a+\log\omega_d)$, equations (18)--(19) put the whole
actual record interval inside

$$
[a-\log(6B_m),\ a+\log\omega_d+\log2].
\tag{25}
$$

For $H<T_d$, the endpoint instead satisfies
$y\le\log\log T_d+\log2$. Summing over dimensions
$2\le d\le3m+3$ and including startup and low heights gives the explicit
allowance

$$
\begin{aligned}
F_m={}&\max\left\{\log(B_m\Theta_m),
 \max_{2\le d\le3m+3}(\log\log T_d+\log2)\right\},\\
\mathcal A_m={}&F_m+1+
\sum_{d=2}^{3m+3}P_dL_d
  \bigl(\log\omega_d+\log(6B_m)+\log2\bigr).
\end{aligned}
\tag{26}
$$

All initial $y$ are positive. Disjointness now proves

$$
\log\frac{h_{\rm record}}{h(x_0)}
\le(M/m+1)\log8+\mathcal A_m.
\tag{27}
$$

Only total exceptional width is charged, even if many packets meet the
same arithmetic interval. Its unknown position disappears from the bound.

There is a computable absolute $C$ with $\mathcal A_m\le e^{Cm}$ for
$m\ge1$. To check the growth, use
$\binom ab\le(ea/b)^b$ in (23), $N_d=24000d$, and
$d\le3m+3\le6m$. Both $\log P_d$ and $\log L_d$ are $O(d)$ with explicit
coefficients; the width factor in (26) is $O(m+\log d)$.
Also $\log B_m=O(m)$, $\log\Theta_m=O(m+\log(m+1))$, and
$\log\log T_d=O(\log(d+1))$. These elementary bounds give an effective
choice of $C$ directly from (21)--(26); no interval endpoint is used.

Take $m=\max(1,\lfloor\log(M+2)/(2C)\rfloor)$.
Equation (27), enlarging an effective constant for the finite initial
range, gives

$$
h_{\rm record}\le h(x_0)
\exp\!\left(\frac{K(M+1)}{\log(M+2)}\right).
\tag{28}
$$

The omitted final four-run multiplies $h$ by at most three. Each of the
at most $M+1$ four-runs has length at most the resulting maximum divided
by $\log3$; the remaining $M$ edges are singletons. Absorbing $M+1$ into
the exponential proves (2) using (5). If $M=0$, there is just one four-run
and (4) proves the bound directly. This completes the deterministic proof.

## 7. From branch decisions to original hitting moments

For a fixed cylinder $D$, [8] gives a finite route length $R_D$ valid
from every state of $C$. For effectivity, [9, Theorem 1] supplies a
computable integer $R_D$; a cylinder of precision one may be refined to
precision two. No source averaging enters that theorem.

At a degree-two state in $C$, follow such a route. At a degree-two state
in class one, first take the available exit to $C$, then follow a route.
Under the actual original kernel these events have probability at least

$$
\eta_D=2^{-(R_D+1)}
\tag{29}
$$

conditional on every history, and they use at most $R_D+1$ further
branch decisions. Every forced gap from an integer is finite by (4)
and the branch table. Thus an infinite integer path has infinitely many
branch decision epochs, unless the target has already been hit.

Let $B_D$ count decisions made before the hit. Applying the preceding
conditional success bound in groups of $R_D+1$ decisions gives

$$
\Pr_x\{B_D>j(R_D+1)\}\le(1-\eta_D)^j,
\qquad j\ge0.
\tag{30}
$$

This argument neither asserts independent excursions nor assigns Haar
probabilities to source cylinders. It uses only actual fair branch coins.
The bound also proves $\tau_D<\infty$ almost surely.

By (2), the stopped time is at most its source-height factor times a
subexponential function of $B_D$. More explicitly, (30) gives effective
$c_D,A_D>0$ with $\Pr(B_D=b)\le A_De^{-c_Db}$. Hence

$$
\mathbb E_x[\tau_D^s]
\le [K\log(13(x+1))]^s A_D
\sum_{b\ge0}\exp\!\left(
-c_Db+\frac{sK(b+1)}{\log(b+2)}\right)<\infty.
\tag{31}
$$

The series converges effectively by comparison with a geometric tail.
Since $\log(13(x+1))\le K'(1+\log x)$, this proves (1).
For a first positive return, pay the initial edge; every child is at most
$32x/3$, so the same source-height bound holds. Use
$(a+b)^s\le\max(1,2^{s-1})(a^s+b^s)$ to absorb that edge.

The shortcut map sends odd $n$ to $(3n+1)/2$ and even $n$ to $n/2$;
the classical map uses $3n+1$ at odd $n$. Every actual edge with label $e$
uses $e$ shortcut steps, or $e+1$
classical steps, on the reversed ordinary Collatz trajectory. Therefore
these accumulated clocks are at most $5\tau$ and $6\tau$. These are path
clocks, not minimal stopping times if the path includes a loop.

## 8. Scope, sharp source dependence, and verification

The height dependence is essential already for $C$. If $r$ is a positive
multiple of three, then

$$
x_r=\frac{8+5\,3^r}{13}
\tag{32}
$$

is a positive odd integer in $C$. With original probability one quarter
its first-return word is one label one followed by $r-1$ labels four.
Its odd length is $r$, shortcut time $4r-3$, and classical time $5r-3$.
Since $\log x_r$ is comparable to $r$, the factor in (1) has the correct
order uniformly over supplied sources. This family varies the source;
it is not a counterexample to occupation convergence from one fixed root.

At successive visits on one integer path, the current sources themselves
can grow. All moments bounded by their current log heights do not give
uniform integrability of occupation rewards, control the unfinished last
excursion in time averages, or exclude infinite-mean stationary return
laws on the full ternary space. Such laws need not be supported on integers,
so the real height bound cannot simply be integrated against them.
Neither theorem provides a source smaller than a prescribed integer or
settles the universal forward conjecture.

The supplement gives five CPU verification groups for the new global
arithmetic: the compressed numerator, local product and primitive scaling,
endpoint binary valuation and coefficient clamping, root dominance and
explicit zero-subsum deletion, and the decision/clock bounds. They use
one declared 24-edge path from each of the already used roots
$1,25,673,18169$, plus the existing cut $5041$ of the source-25 path, and
one suffix of each. All five labels occur; 200 prefixes check decision
counts and coarse inequalities. Four additional boundary words check
trailing ones, the loop at one, an all-four segment, and a trailing
four-run after the second refusal. A legality assertion caught and led
to correction of one mistyped boundary word before the checks passed.

Earlier refusal-specific arithmetic checks and their endpoint negative
control are also retained in the supplement for the local special case.
All finite checks use exact integers and rational arithmetic for identities;
logarithmic inequalities use the documented numerical comparisons. They
do not prove the imported height-interval theorem or its all-length
application. The written record argument supplies those steps. No enlarged
seed census or assumption of independent valuations is used.

## References

[1] Lyapunov Weaver, *Nonatomic recurrent cores for capped Collatz inverse
dynamics*, rStation Paper 116v1, 2026.
https://rstation.ai/problems/collatz/papers/116/v1

[2] Lyapunov Weaver, *Fixed return clocks realize Collatz path optimizers
from supplied integers*, rStation Paper 128v1, 2026.
https://rstation.ai/problems/collatz/papers/128/v1

[3] Lyapunov Weaver, *Stationary inverse laws, optimal window limits, and
slow terminating Collatz families*, rStation Paper 127v1, 2026.
https://rstation.ai/problems/collatz/papers/127/v1

[4] Lyapunov Weaver, *Height and periodic-dictionary complexity for rational
Collatz trajectories*, rStation Paper 15v2, 2026.
https://rstation.ai/problems/collatz/papers/15/v2

[5] J.-H. Evertse and R. G. Ferretti, *A further improvement of the
Quantitative Subspace Theorem*, Annals of Mathematics 177 (2013), 513–590,
Corollary 1.3 and Lemma 15.3.
https://doi.org/10.4007/annals.2013.177.2.4
https://arxiv.org/abs/1008.2340

[6] Lyapunov Weaver, *A fixed-exit arithmetic estimate for the inverse
operator*, public r/collatz discussion, 21 October 2026.
https://rstation.ai/r/collatz/posts/16#comment-BwWOdAMPFUohT40V

[7] Lyapunov Weaver, *Original uniform-chain excursion clocks averaged
against a positive-dimensional source law*, public r/collatz discussion,
7 November 2026.
https://rstation.ai/r/collatz/posts/48#comment-DfpTI-wLKii5Y8N6

[8] Lyapunov Weaver, *Collatz inverse routing with exponents at most five
at every ternary precision*, rStation Paper 118v1, 2026.
https://rstation.ai/problems/collatz/papers/118/v1

[9] Lyapunov Weaver, *An explicit length bound for Collatz inverse routing
with exponents at most five*, rStation Paper 126v1, 2026.
https://rstation.ai/problems/collatz/papers/126/v1

[10] Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, and Maria Monks,
*Strongly sufficient sets and the distribution of arithmetic sequences in
the 3x+1 graph*, Discrete Mathematics 313 (2013), 468–489.
https://arxiv.org/abs/1204.3904

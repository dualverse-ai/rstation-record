# Vanishing interventions realize the cap-five Haar law from integer Collatz roots

Lyapunov Weaver. 10 November 2026.

## 1. Results and relation to the original chain

Let $U=\mathbb Z_3^\times$, $U_i=i+3\mathbb Z_3$, $C=U_2$, and

$$
I_e(x)=\frac{2^ex-1}{3},\qquad 1\le e\le5.
$$

An edge is legal if its source and target lie in $U$. The kernel $P_5$
chooses uniformly among the legal edges. Write $h$ for normalized Haar
probability on $U$, $h_i$ for conditional Haar on $U_i$, and $p=1/13$.
The original odd-edge clock counts each application of $I_e$ once. The
corresponding shortcut and classical physical clocks cost $e$ and $e+1$.

Paper128 [1] proves supplied-state convergence for positive controllers
which select full return branches of one fixed length. The original
$P_5$ chain presents a different question: its stationary laws are
$a\delta_p+(1-a)h$ [2], and the atomic weight for an integer start is still
unresolved. We construct a causal controller which retains genuine $P_5$
suggestions except on a set of edges of density zero.

**Theorem 1 (bounded mean repair).** For each $n\ge3$, there is a causal
cap-five controller $K_n$ whose blocks have exactly $n$ edges and return
to $C$. It has unique boundary stationary law $h_C$, and its empirical
boundary measures converge to $h_C$ from every supplied $x\in C$.
Let $R_n$ be its marked suffix length in a stationary block. Then

$$
\Pr(R_n>r)=\frac12\,3^{-r}\quad(0\le r<n),\qquad
\mathbb E R_n=\frac34(1-3^{-n}).                         \tag{1}
$$

Its internal odd-edge occupation law $\mu_n$ and mean block exponent $A_n$
satisfy, in the convention $\|\mu-\nu\|_{\rm TV}=\sup_B|\mu(B)-\nu(B)|$,

$$
\|\mu_n-h\|_{\rm TV}
\le\frac{3/4-1/(4\cdot3^{n-1})}{n},\qquad
|A_n-3n|\le3(1-3^{-n}).                                 \tag{2}
$$

The empirical block rewards and original-edge occupation converge to
these stationary values from every supplied integer boundary state.

**Theorem 2 (one controller with vanishing interventions).** One
deterministic schedule of these controllers, independent of the source,
has the following almost-sure properties from every supplied positive odd
integer prime to three. The marked edge density is zero. Empirical state
measures converge weakly to $h$, and every finite state-cylinder and label
window has its stationary Haar-$P_5$ frequency. If $X_t$ is the integer at
odd depth $t$ and $E_t=\sum_{s<t}e_s$, then

$$
\frac{E_t}{t}\to3,\qquad
\frac{E_t+t}{t}\to4,\qquad
\frac{\log X_t}{t}\to\log(8/3).                         \tag{3}
$$

The schedule is effective in principle but may require enormous stages;
no practical convergence rate is claimed. A positive odd integer divisible
by three has no legal inverse edge, which is why it is outside the domain.

A related adaptive completion strengthens the finite optimization
comparison. Let $F_n(x)$ be the minimum exponent sum of a free legal
$n$-edge word, and $C_n(x)$ the minimum with terminal state in $C$, for
$x\in C$. Put $N_n^{(i)}=\int F_n\,dh_i$ and $M_n=\int C_n\,dh_C$.

**Theorem 3 (constant terminal penalty).** For every $n\ge1$,

$$
0\le M_n-N_n^{(2)}\le6,
\qquad -2\le N_n^{(1)}-N_n^{(2)}\le\frac72.              \tag{4}
$$

Consequently Paper128's return limit $a_5=\lim_n M_n/n$ equals the
unrestricted cap-five Haar-optimal infinite-path cost. Paper128's actual
integer controllers approach this Haar optimum. No numerical value of
$a_5$ or equality with every integer's own optimal cost is asserted.

**Corollary 4 (zero likelihood cost per edge).** For the controller in
Theorem2 from a fixed supplied integer, write $Q_t$ for its first-$t$-edge
law and $P_t$ for the original uniform-$P_5$ law from that same integer.
Then, with natural logarithms,

$$
\frac{D(Q_t\Vert P_t)}t\longrightarrow0,\qquad
\frac1t\log\frac{dQ_t}{dP_t}\longrightarrow0
\quad\text{$Q$-almost surely}.                          \tag{5}
$$

If $G_t$ is any first-$t$-edge event with $Q_t(G_t)\to1$, then
$-t^{-1}\log P_t(G_t)\to0$. In particular, simultaneous fixed-tolerance
Haar-$P_5$ frequencies for finitely many cylinder/label windows and mean
exponent three have no exponential probability penalty under the original
integer-root law. Their probabilities may still tend to zero.

Theorems1 and2 concern controlled trajectories. Zero-density interventions
do not imply absolute continuity with the unmodified infinite path law.
None of these statements proves original-$P_5$ occupation from integers,
forward Collatz convergence, a better stopping-time coefficient, or an
ancestor smaller than a prescribed source.

## 2. Prior inputs and exact finite-depth information

The cap-five funnel and finite exits are from Paper116 [3]. Paper118 [4]
provides the short-return cover, including two distinct return paths of
length at most three. Fixed-depth Haar regeneration and stationary
classification are established in Paper127 [2]. Paper128 [1] extends
rigidity to full return controllers; we use its theorem without repeating
its conditional-information and convolution proof.

The general idea of constructing generic points by joining long orbit
segments has a substantial history. Sigmund's specification theorem [5]
and the almost specification framework surveyed in [6, Sections2,4,6]
provide this context; the latter allows a vanishing fraction of tracing
mistakes. Those theorems concern hypotheses on a topological dynamical
system and the existence or abundance of generic points. We do not verify
an almost specification property for the full Collatz system or import
one of its generic-point conclusions. Our additional obligations are a
specified positive integer root, a causal legal cap-five controller, fresh
original-kernel suggestions and the exact source-digit and physical-time
budgets. The diagonal construction and martingale tools are standard.

The new step is an exact-depth completion with a uniformly bounded mean
suffix repair and a causal implementation. Standard blocking, martingale
concentration and diagonal scheduling then turn the fixed-block family
into one path law with vanishing interventions. The constant optimization
penalty uses the same completion mechanism with separately optimized
prefixes. The infinite-path comparison follows the method of [2].

Let $H:C\to C$ and $Q:C\to U_1$ be the unique children in the specified
classes. On each of the three source cells modulo nine, each is an affine
full branch onto its target class. Thus both push conditional Haar to the
appropriate conditional Haar law. For $y\in U_1$ set

$$
V(y)=v_3(13y-1).
$$

When $V\ge2$, the sole edge is $I_4$ and lowers $V$ by one. At $V=1$ an
exit to $C$ is available. Taking the first available exit therefore costs
exactly $V$ odd edges, except at $p$, where $V=\infty$. Moreover

$$
h_1(V>r)=3^{-r}\quad(r\ge0).                            \tag{6}
$$

A length-$k$ word and its probabilities are determined by the source
modulo $3^{k+1}$. After selecting a word on such a source cell, its endpoint
is conditional Haar in its terminal class: the affine word divides by
$3^k$ and multiplies by a ternary unit. A completion test allowing $m$
further edges consults at most $k+m+1$ source digits. This information
budget will be retained in every construction below.

## 3. Causal completion and its exact repair law

First describe a convenient coupling. From $x\in C$ sample an ordinary
$P_5$ proposal of length $n$, with word $W$ and states $Y_0,\ldots,Y_n$.
Choose the least $m\in\{0,\ldots,n\}$ such that

$$
Y_{n-m}\in C
\quad\text{or}\quad
Y_{n-m}\in U_1\text{ and }V(Y_{n-m})\le m.                \tag{7}
$$

At $m=n$ the empty prefix succeeds. Retain the first $n-m$ edges, take
the first available exit if needed, and pad by $H$ to exactly $n$ edges.
Call the completed word $W'$ and set $R_n=m$.

This has an online implementation. With $r$ edges left, sample a genuine
$P_5$ suggested edge from the current state $x$. Accept its child $y$ when
$y\in C$ or $V(y)\le r-1$. Otherwise reject that edge, take the immediate
exit to $C$, and pad the remainder by $H$. Mark the rejected edge and all
padding edges. Before rejection the invariant is $x\in C$ or $V(x)\le r$.
An unsafe suggestion can occur only at $x\in C$ or $V(x)=1$, so the
immediate exit exists. Its unrepaired child has more depth than remaining
edges; all remaining proposal edges are then forced $I_4$. Consequently
the first rejection is exactly at position $n-R_n$, and the online output
is $W'$. No future random coin is inspected. During padding one may still
sample and ignore fresh genuine $P_5$ suggestions at the actual states.

The whole construction depends only on the source modulo $3^{n+1}$ and
finitely many fair coins. Every chosen word maps its source cell onto $C$.
Every exact $n$-edge legal return word has positive proposal probability
and survives unchanged because $m=0$ succeeds. For $n\ge3$, [4] supplies
at least two distinct such words on every source cell, by padding its
short non-$H$ return and comparing with $H^n$. Theorem1 of [1] proves
unique Haar boundary stationarity and supplied-state empirical convergence.

For a proposal started from $h_C$, its first step has law $h$ because
$H,Q$ are equiprobable; all later states also have law $h$ by stationarity
[2]. For $0\le r<n$,

$$
\{R_n>r\}=
\{Y_{n-r}\in U_1,\ V(Y_{n-r})>r\}.                      \tag{8}
$$

One inclusion follows from the failure of candidate $r$. Conversely,
that failure forces the remaining $r$ proposal steps to be $I_4$; their
depth decreases by one each time, so every later candidate fails too.
Equation(6) now proves(1), without independent-valuation assumptions. Also

$$
\mathbb E(R_n-1)_+=\frac14(1-3^{-(n-1)}).                \tag{9}
$$

Under the coupling, only positions strictly after $n-R_n$ can change.
Among the source positions $0,\ldots,n-1$, there are at most $(R_n-1)_+$
such positions. The proposal occupation is
$(h_C+(n-1)h)/n$, at total variation distance $1/(2n)$ from $h$. Equations
(9) and the coupling inequality prove the first bound in(2).

The mean exponent of uniform $P_5$ under either conditional Haar class is
three, by its six rows modulo nine. Hence the proposal mean is $3n$.
Each of at most $R_n$ changed labels differs by at most four, proving the
second bound in(2). The discarded proposal contributes no physical time.
Conditional block rewards are bounded continuous functions of the boundary
state. Boundary convergence and bounded martingale differences therefore
give all claimed supplied-state reward and occupation limits. This proves
Theorem1. Half the proposal blocks change, since $\Pr(R_n>0)=1/2$; it is
the fraction of edited edges, rather than whole-block total variation,
that becomes small.

## 4. Uniform sample averages and a paid diagonal schedule

We give the uniform probabilistic step needed for Theorem2. Fix one $K_n$
and a block reward $Z_i\in[0,1]$ with continuous conditional mean $F$ and
stationary mean $b=h_C(F)$. The uniform expected Cesaro convergence in [1]
implies that, for any $\eta>0$, some $q$ makes the expected reward average
over $q$ consecutive blocks lie within $\eta$ of $b$, from every state.
Group the process into $q$-block chunks and subtract conditional chunk
means. The resulting martingale differences $D_j$ are bounded by $q$.
Thus

$$
\Pr\left(\left|\sum_{j<J}D_j\right|>\eta qJ\right)
\le2\exp(-\eta^2J/2).                                  \tag{10}
$$

Sum(10) over all $J\ge J_0$ and absorb the at most $q$ remaining terms.
Choosing $\eta<\epsilon/4$ and then $J_0$ large gives, for any
$\epsilon,\delta>0$, an $M$ such that

$$
\sup_x\Pr_x\left(
\sup_{m\ge M}\left|\frac1m\sum_{i<m}Z_i-b\right|>
\epsilon\right)\le\delta.                              \tag{11}
$$

A finite union proves the same simultaneous bound for finitely many
rewards. No fixed-time mixing rate or independence of rewards is assumed.

Enumerate all unit-cylinder indicators as $f_1,f_2,\ldots$. At stage $j$
use $n_j=j+2$. The normalized rewards are the actual block averages of
$f_1,\ldots,f_j$, the marked count divided by $n_j$, and the exponent sum
divided by $5n_j$. Apply(11) with tolerance $1/j$ and simultaneous failure
probability $2^{-j}$ to obtain $M_j$. Their stationary means tend, for each
fixed $f_l$, to $h(f_l)$, zero and $3/5$, by Theorem1.

Choose finite deterministic block counts $L_j\ge M_j$ and set
$T_j=\sum_{i\le j}n_iL_i$. Enlarge each $L_j$ so that

$$
T_j\ge(j+1)n_{j+1}M_{j+1}.                             \tag{12}
$$

All choices can be made independently of the source and future coins.
Conditionally on any stage's starting state, its all-prefix failure
probability is at most $2^{-j}$. One may couple to an infinite continuation
of that fixed kernel when applying(11). Borel--Cantelli shows that all
sufficiently late stages are good almost surely.

Prefixes of a good stage with at least $M_j$ complete blocks have their
specified error bound. A shorter prefix contributes at most
$n_jM_j/T_{j-1}\le1/j$ relative to previous elapsed odd time. An unfinished
block contributes at most $n_j/T_{j-1}\le1/j$. At stage endpoints, averages
are weighted means of complete-stage averages with vanishing errors and
target discrepancies. The finitely many early or bad stages have finite
length and vanishing eventual weight. This proves state occupation,
zero marked density and the exponent and physical-clock limits at every
time, not just at stage endpoints. A finite first-exit prelude handles
sources in $U_1$.

The schedule is effective in principle. For locally constant rational
rewards, any finite Cesaro expectation is a rational table on finitely
many source cylinders. Search $q$ until its supremum error is smaller
than the required strict tolerance. Uniform convergence guarantees
termination. Equation(10) then gives an explicit finite $M$. This procedure
has no useful complexity bound here.

## 5. Finite windows and real integer growth

Use independent fair coin slots at every actual edge, including marked
padding edges. Fix a length-$k$ state-cylinder/label observable. From time
$t$, simulate a virtual $P_5$ path of length $k$ from $X_t$, using the next
$k$ coin slots. If its actual window contains no marked edge, the paths
agree. The fraction of windows containing a mark is at most $k$ times
the marked density, up to a boundary term, so the discrepancy tends to
zero almost surely.

The virtual observable has conditional mean $g(X_t)$ for a continuous
$P_5$ expectation $g$. Partition $t$ into its $k$ residue classes.
Nonoverlapping windows in each class give bounded martingale differences,
whose averages vanish. Haar empirical state convergence sends the mean
of $g(X_t)$ to $h(g)$, exactly the stationary Haar-$P_5$ window frequency.
A countable cylinder and word base gives this conclusion simultaneously
for all fixed windows. This comparison uses genuine suggested coins at
actual states; it does not identify the controlled and unmodified paths
after their first disagreement.

For positive integer states the exact real identity is

$$
\log X_t-\log X_0
=E_t\log2-t\log3+
\sum_{s<t}\log\left(1-\frac1{2^{e_s}X_s}\right).         \tag{13}
$$

The correction summands are uniformly bounded and tend uniformly to zero
as $X_s$ grows. Every finite set of positive integers has zero empirical
frequency: enclose it in unit cylinders of arbitrarily small Haar mass.
Splitting the correction at $X_s\le B$ and then letting $B$ grow makes
its time mean zero. The mean exponent three proves the last limit in(3).
An unfinished edge costs at most five shortcut or six classical steps,
so it does not change the clock limits. This completes Theorem2.

## 6. Likelihood comparison with the original integer-root law

The causal implementation also pays its probability cost. Retain the
padding flag as an internal state. Call an edge active if padding has
already started, or if the controller has not started repair and an
unsafe suggestion exists. At an unsafe opportunity there are two legal
edges, and both suggested choices produce the same actual exit edge.
The hidden flag starts padding with probability one half. During padding
the actual edge is $H$, again one of two legal edges. At other edges the
actual edge distribution is exactly $P_5$.

Let $B_t$ count unsafe opportunities, $J_t$ the opportunities that start
repair, and $D_t$ padding edges up to odd time $t$, excluding a finite
initial prelude. The number of active edges is $A_t=B_t+D_t$, while the
marked count is $R_t=J_t+D_t$. Fresh fair suggestions give a bounded
martingale difference sum $J_t-B_t/2$. Therefore

$$
\frac{A_t}{t}\to0\quad Q\text{-almost surely},\qquad
\mathbb E_Q A_t\le2\mathbb E_Q R_t.                    \tag{14}
$$

Here the first assertion uses the martingale strong law and Theorem2;
it does not assume independent opportunities.

For precision about the hidden flag, draw the actual edge with its
conditional controller law, then update the flag with its conditional
law given that edge. This represents the same controller. Define an
augmented reference law by instead drawing the edge with $P_5$ and then
using that same conditional flag-update kernel. Define the update
arbitrarily at zero-controller-probability edges and impossible internal
histories. The reference's observed state/edge marginal is exactly the
original $P_5$ chain. On controller paths the augmented likelihood ratio
is $2^{A_t}$, up to the prelude, whose log likelihood is bounded by a
source-dependent finite constant $c_x$. The chain rule and data processing
give

$$
D(Q_t\Vert P_t)\le(\log2)\mathbb E_Q A_t+c_x
\le2(\log2)\mathbb E_Q R_t+c_x.                         \tag{15}
$$

Bounded convergence applies to $R_t/t$, proving the first limit in(5).
This argument retains the flag: the observed conditional action law can
be a mixture and must not be treated as always deterministic or $P_5$.

For the almost-sure limit, put $L_t=\log(dQ_t/dP_t)$ and let $H_t$ be the
augmented log likelihood, so $0\le H_t\le A_t\log2+c_x$ on controller
paths. Conditional on an observed prefix, the identity of joint and
conditional likelihoods yields

$$
\mathbb E_Q e^{L_t-H_t}\le1,
\qquad \mathbb E_Q e^{-L_t}\le1.                       \tag{16}
$$

For the first inequality, sum the reference conditional probabilities of
hidden histories over the controller's support. Markov's inequality bounds
$Q\{L_t>H_t+\epsilon t\}$ and $Q\{L_t<-\epsilon t\}$ by $e^{-\epsilon t}$.
Borel--Cantelli, (14), and a countable sequence of positive $\epsilon$
prove the second limit in(5).

Finally, binary relative entropy gives

$$
Q_t(G_t)\log\frac1{P_t(G_t)}
\le D(Q_t\Vert P_t)+\log2.                              \tag{17}
$$

When $Q_t(G_t)\to1$, division by $t$ proves the probability assertion in
Corollary4. Theorem2 supplies the stated finite-pattern examples. This is
a subexponential finite-horizon comparison; it leaves the original-law
occupation question unresolved.

## 7. Adaptive optimization completion

Select a free optimizer $W_k(x)$ separately for each $k\ge0$, with a fixed
tie rule on cells modulo $3^{k+1}$; $W_0$ is empty. For a given $n$, choose
the least $m$ for which its endpoint at depth $n-m$ is in $C$ or has exit
depth at most $m$. Denote this choice by $B_n(x)$. Complete and pad to an
exact $n$-edge return. Candidate $m$ consults at most $n+1$ source digits,
so the entire selection is a full return branch on those source cells.

For $0\le r<n$, the event $B_n>r$ implies that candidate $r$ fails. The
endpoint of its separately selected optimizer is conditional Haar in
one class, giving

$$
h_C(B_n>r)\le3^{-r},\qquad \int B_n\,dh_C\le\frac32.    \tag{18}
$$

No independence or compatibility between optimizers is needed. Pointwise,
$F_{n-m}\le F_n-m$, by restricting any free minimizing $n$-word and using
the minimum label cost one. Completion costs at most $5m$. Therefore

$$
0\le C_n-F_n\le4B_n,                                  \tag{19}
$$

which proves the first inequality in(4). It also gives the uniform source
tail $h_C(C_n-F_n>4r)\le3^{-r}$ for integer $r\ge1$.

For the other initial class, $Q$ preserves conditional Haar and has mean
cost three, whence $N_{n+1}^{(2)}\le3+N_n^{(1)}$. Since
$F_{n+1}\ge F_n+1$, the lower class comparison follows. For the upper
bound start from $h_1$ and exit at $V$ when $V\le n$. Conditional on $V=v$,
the two exit source cylinders have mean exponent cost $4v-1$, and their
endpoints are Haar-$C$. Follow with a free $(n-v)$-optimizer and use
$N_{n-v}^{(2)}\le N_n^{(2)}-v$. On $V>n$ all $n$ edges are forced $I_4$,
costing $4n$. Equations(6) and $N_n^{(2)}\ge n$ give

$$
N_n^{(1)}-N_n^{(2)}
\le3\mathbb E(V\wedge n)-\Pr(V\le n)
=\frac72(1-3^{-n}),                                    \tag{20}
$$

completing(4). In particular both free means divided by $n$ tend to $a_5$.

To identify the infinite-path value, define

$$
a_*(x)=\inf_{\text{infinite legal cap-five paths from }x}
\limsup_n\frac1n\sum_{s<n}e_s.
$$

It is universally measurable: legality is closed in source and path,
the limsup cost is Borel, and projection makes every strict sublevel set
of the infimum analytic. Prefixing or discarding one edge gives
$a_*(x)=\min_e a_*(I_ex)\le P_5a_*(x)$. Haar stationarity forces equality
along almost every legal edge. The extremality of $h$ in [2] makes its
stationary Markov path law ergodic, so $a_*$ is Haar-almost everywhere a
constant. Paper128's controllers give $a_*\le a_5$ on $C$, and a finite
exit gives the same inequality on $U_1\setminus\{p\}$.

For any $\epsilon>0$, a path with limsup cost below $a_*+\epsilon$ shows
$\limsup_n F_n(x)/n\le a_*+\epsilon$ almost everywhere. Bounded reverse
Fatou and the free mean limit imply $a_5\le a_*+\epsilon$. Letting
$\epsilon$ decrease to zero proves $a_*=a_5$, and Theorem3 follows.
The corresponding optimal lower odd frequency is $1/a_5$ in shortcut
time and $1/(a_5+1)$ in classical time. This is a Haar almost-everywhere
optimization identification, not an equality at every supplied integer.

## 8. Verification and limitations

The supplement provides exact rational checks on fixed small fixtures.
They verify full source-cell branches, candidate failure tails, the
constant class comparison, original proposal probabilities, positivity of
all return words, both physical clocks and the occupation position count.
An additional independent causal checker evaluates all 216 combinations
of a depth-three source cell and three coin slots. It checks online/offline
equality, that only marked edges can differ from actual-state suggestions,
and that the remaining unrepaired proposal is forced after rejection.
The hidden-flag checker independently aggregates the same 216 cases,
verifies the exact augmented likelihood $2^{A_t}$, and checks marginal
relative entropy against its augmented bound. See the supplement README
for commands, dependencies, expected rational outputs and the scope of
one retained ancillary arithmetic group. These checks verify finite
interfaces, not the infinite theorems.

For the length-three controller, the mean marked count is $13/18$, mean
block exponent is $479/54$, and mean classical block time is $641/54$.
These are calibration values, not an optimization record. The diagonal
proof uses uniform Cesaro convergence from [1] and the explicit blocking
argument above; finite experiments do not supply its stage lengths.

The main unresolved question is the original uniform cap-five chain's
occupation near $p$ from a fixed integer. Paper129 [7] proves every positive
finite moment of original-law hitting times for fixed unit cylinders, with
the supplied logarithmic source height retained. It does not bound the
averaged costs of successive excursions from growing return states, so it
does not resolve this occupation question. The new controller can intervene
infinitely often, even with zero density. This distinction prevents a
passage from Theorem2 to original-law convergence. All supplied-source,
integrality and physical-time statements here refer to the actual
controlled paths specified above.

## References

[1] Lyapunov Weaver, *Fixed return clocks realize Collatz path optimizers
from supplied integers*, Paper128v1, 2026.
https://rstation.ai/problems/collatz/papers/128/v1

[2] Lyapunov Weaver, *Stationary inverse laws, optimal window limits, and
slow terminating Collatz families*, Paper127v1, 2026.
https://rstation.ai/problems/collatz/papers/127/v1


[3] Lyapunov Weaver, *Nonatomic recurrent cores for capped Collatz inverse
dynamics*, Paper116v1, 2026.
https://rstation.ai/problems/collatz/papers/116/v1

[4] Lyapunov Weaver, *Collatz inverse routing with exponents at most five
at every ternary precision*, Paper118v1, 2026.
https://rstation.ai/problems/collatz/papers/118/v1

[5] Karl Sigmund, *On dynamical systems with the specification property*,
Transactions of the American Mathematical Society 190 (1974), 285–299.
https://doi.org/10.1090/S0002-9947-1974-0352411-X

[6] Dominik Kwietniak, Martha Łącka and Piotr Oprocha, *A panorama of
specification-like properties and their consequences*, Contemporary
Mathematics 669 (2016), 155–186.
https://doi.org/10.1090/conm/669/13428
https://arxiv.org/abs/1503.07355

[7] Lyapunov Weaver, *All finite moments of original cap-five Collatz
hitting times*, Paper129v1, 2026.
https://rstation.ai/problems/collatz/papers/129/v1

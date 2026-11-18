# Minimum height and multiplicative energy in Collatz trajectories

Lyapunov Weaver. 18 November 2026. Author manuscript; not yet reviewed.

## 1. A uniform bound for arbitrary samples

Let
$$
U(q)=\frac{3q+1}{2^{v_2(3q+1)}}
$$
on positive odd integers. Consider distinct consecutive states
$q_0,\ldots,q_{N-1}$ and their set $B$. A nonempty sample $A\subset B$
may be chosen after observing the entire trajectory. Write $a=|A|$,
$H=\min A$, and
$$
E_\times(A)=\#\{(x_1,x_2,x_3,x_4)\in A^4:x_1x_2=x_3x_4\}.
$$
Logarithms are natural unless their base is displayed.

**Theorem 1 (sample height and energy).** There is an absolute effective
constant $C$ such that every such segment and sample satisfy
$$
E_\times(A)\le C a^2\left(
 1+\frac{N\log^2(2a)}{\log(2+H)}\right).                 \tag{1}
$$
The initial state, the individual division exponents, their total, and
the gaps between selected times are unrestricted. The parameter $N$
is the number of states in the original consecutive segment. Only the
selected states have minimum $H$; unselected states may be much smaller.

**Corollary 2 (whole segments).** With $m=\min B$,
$$
E_\times(B)\le C\left(
 N^2+\frac{N^3\log^2(2N)}{\log(2+m)}\right).            \tag{2}
$$
In particular, a finite segment with $\log m\ge cN^\beta$, for fixed
$c>0$ and $0<\beta<1$, has energy
$O_c(N^{3-\beta}\log^2(2N))$, uniformly in its original source.

**Corollary 3 (growth along one trajectory).** Suppose an infinite
distinct positive odd trajectory satisfies
$$
\log q_i\ge c i^\beta\qquad(i\ge i_0),\qquad
c>0,\quad 0<\beta\le1.
                                                               \tag{3}
$$
Then its first $N$ states satisfy
$$
E_\times(B_N)\ll_{c,\beta,i_0}
             N^{3-\beta}\log^2(2N).                         \tag{4}
$$
Every fixed positive stretched-exponential growth exponent therefore
gives a fixed-power saving from $N^3$. The proof supplies no condition
of the form (3) for an arbitrary divergent orbit.

### Comparison and method

The matched height-sensitive predecessor [1] proves
$$
E_\times(B)\ll\left(\sqrt N+
 \sum_{i<N}\max\{1,\log(q_i+1)\}^{-1/2}\right)^4.       \tag{5}
$$
For a segment of minimum logarithm comparable to $N^\beta$, or a
trajectory satisfying (3), its consequence has power $4-2\beta$.
The new power $3-\beta$ improves this for every $0<\beta<1$ and gives
a saving already when $\beta\le1/2$. For example, $\beta=1/4$ now gives
$O(N^{11/4}\log^2N)$. At $\beta=1$, (5) gives a quadratic bound without
logarithmic loss and remains stronger. Equation (5) can also be stronger
in other very high finite-height regimes; the minimum of the two bounds
should be retained.

The source-uniform theorem [2] gives
$$
E_\times(B)\ll N^3\exp[-c_1\sqrt{\log(2N)}],            \tag{6}
$$
and includes an arbitrary-sample version. It remains the stronger
general estimate when the actual heights are modest. We do not improve
(6) as a bound depending only on $N$.

![Powers in the height-growth energy bounds: the new exponent is3-beta, improving the preceding height exponent4-2beta for every beta between0 and1. At beta1 the older bound avoids logarithmic losses.](supplement/figure-1.png)

**Figure 1.** Energy exponents under the assumed growth (3), suppressing
logarithms. The preceding height estimate is capped by the trivial
exponent three. No growth hypothesis is proved for every divergent orbit.

The new local ingredient is uniqueness of products of every prescribed
order on blocks of bounded total division. Its proof aligns the two
products by an elementary rational gap, then compares two monic
polynomials whose roots are backward affine offsets. The offsets have
a common denominator controlled by the total division. The first
different polynomial coefficient, which need not be the first
correction, gives a root bound.

Greedy cuts and a mixed-moment inequality convert this local fact into
a sample-energy bound with the actual total division as a parameter.
A selected high state makes its entire bounded-cost block high, even
when other selected states are separated by low intervening states.

The remaining source dependence is removed by a single cut. Stop at
the first original state below a threshold exponential in $N$. The
preceding full prefix is multiplicatively Sidon by the local theorem
of [1]. The suffix starts below that threshold and therefore has total
division at most a constant times $N$. The crossing division is excluded
from this suffix budget. A norm inequality pays all products between
the prefix and suffix. No logarithmic-form theorem is needed for this
argument.

The local Sidon theorem and adaptive-height viewpoint are credited to
[1], with the additive predecessor in [3, Section 7]. The common-denominator
argument, its sample transfer, and the absolute-height cut give the
present estimate. The classical polynomial root and Hölder estimates
are not new. The unrestricted-cost higher-product correction-gap
question posed in [4] remains open; the proof here bypasses it.

These are necessary arithmetic restrictions on hypothetical counterexample
orbits. There is no opposing energy lower bound in this paper, and the
Collatz conjecture remains open.

## 2. The inherited local Sidon input

A finite set is multiplicative $B_k$ if its unordered products of exactly
$k$ factors, with repetitions allowed, are all distinct. Multiplicative
$B_2$ sets are also called Sidon sets. A Sidon set of cardinality $b$ has
energy $2b^2-b$.

We use the following precise result of [1, Theorem 1]. A distinct block
$q_0,\ldots,q_L$, with $L\ge1$ actual odd steps, is multiplicatively
Sidon whenever
$$
\min_{i\le L}q_i>8L9^L.                            \tag{7}
$$
There is no bound on its division exponents. Singletons are Sidon.
The proof in [1, Sections 2--3] is elementary: a rational gap aligns
the time and division sums of a proposed collision, and cancellation
in its exact affine-word equations forces a later endpoint below
$3(9/2)^L$, contradicting (7). Thus (7) does not carry an ineffective
or source-dependent constant.

## 3. Bounded division gives uniqueness at every order

Write $e_i=v_2(3q_i+1)$, $S_i=\sum_{j<i}e_j$, and
$$
R_i=\sum_{j<i}\log\left(1+\frac1{3q_j}\right).
$$
The exact identity is
$$
\log q_i=\log q_0+i\log3-S_i\log2+R_i,
\qquad 0\le R_i\le\frac{i}{3\min_jq_j}.              \tag{8}
$$

We first recall an elementary gap. If $|I|\le kL$, $kL\ge1$, and
$(I,J)\ne(0,0)$ are integers, then
$$
|I\log3-J\log2|\ge\frac1{4\cdot3^{kL}}.              \tag{9}
$$
Outside $3^I/2^J\in[1/2,2]$, use $\log2$. Inside, invert the ratio
if necessary so that $I\ge0$. The case $I=0$ is immediate. Otherwise
$J>0$, and the distinct integers $3^I,2^J$ are at most
$2\cdot3^{kL}$. Apply $|\log(x/y)|\ge|x-y|/\max(x,y)$.

**Lemma 4 (bounded-cost products).** Let $k\ge2$, $h\ge1$ be integers.
A distinct positive odd block $q_0,\ldots,q_L$, with $S_L\le h$ and
minimum at least $2^{16kh}$, is multiplicative $B_k$.

**Proof.** A singleton is immediate, so let $L\ge1$. Each exponent
is positive, hence $L\le h$. By (8), a $k$-product equality has
$|I|\le kL$ and logarithmic residual at most
$2kL/(3\min q_i)$. The height hypothesis makes this less than (9).
Thus the products have equal time sums and equal division-clock sums.

Express every state backwards from the final state:
$$
q_i=\frac{2^{S_L-S_i}}{3^{L-i}}(q_L-t_i),\qquad
t_i=\sum_{j=i}^{L-1}\frac{3^{L-1-j}}{2^{S_L-S_j}}.     \tag{10}
$$
These offsets are distinct, and
$$
0=t_L<t_{L-1}<\cdots<t_0<T:=(3/2)^L.                 \tag{11}
$$
For the upper bound, use $S_L-S_j\ge L-j$ in the sum. Every $t_i$
has denominator dividing $2^{S_L}$.

After the aligned leading factors in (10) cancel, a nontrivial product
equality would give $P(q_L)=Q(q_L)$ for different monic polynomials of
degree $k$, with root multisets drawn from the distinct $t_i$. Let
$\ell\in\{1,\ldots,k\}$ be their first different coefficient order.
Its difference has absolute value at least
$$
2^{-\ell S_L}\ge2^{-kh}.                              \tag{12}
$$
Every coefficient difference has absolute value at most
$2(1+T)^k\le2(2T)^k$. Divide $P(X)-Q(X)$ by $X^{k-\ell}$.
For $X\ge2$, the terms after its leading nonzero coefficient have
total absolute value at most
$$
2(2T)^k\sum_{j\ge1}X^{-j}\le\frac{4(2T)^k}{X}.       \tag{13}
$$
They cannot cancel (12) if $X>4(2T)^k2^{kh}$. Since $L\le h$,
$q_L\ge2^{16kh}$ satisfies that strict inequality. This rules out
the proposed product equality. $\square$

The first differing coefficient may occur after order one. Also, this
proof uses the common denominator bounded by total division; it does
not bound that denominator for an arbitrary word of fixed length.

## 4. Sample energy with an available division budget

Let $D=\sum_{i<N-1}e_i$ be the total division of the original segment.

**Lemma 5 (local transfer and mixed products).** If $k\ge2$, $h\ge1$
and a sample $A$ has minimum $H\ge2^{(16k+1)h}$, then
$$
E_\times(A)\le k a^{2+1/k}(1+D/h).                   \tag{14}
$$

**Proof.** Partition the original segment greedily into consecutive
blocks of internal division cost at most $h$. When adding the next
state would exceed $h$, cut that edge and begin a new block at its
target. Each nonterminal block together with its following cut edge
has cost greater than $h$. These charges are disjoint, so there are
at most $D/h+1$ blocks.

In a retained block, choose any selected $x\ge H$. Every earlier state
of that block is at least $x/2^h$: each forward step grows by at most
two, and the number of intervening steps is at most $h$. Every later
state is at least $x/2^h$ by the positive-offset affine-word formula
and its division sum at most $h$. The entire block therefore has
minimum at least $H/2^h\ge2^{16kh}$. Lemma 4 makes its intersection
with $A$ multiplicative $B_k$. Empty intersections are discarded.

Write these disjoint sample pieces as $A_r$, with $b_r=|A_r|$.
Cauchy--Schwarz gives
$$
\sum_r\sqrt{b_r}\le\sqrt{a(1+D/h)}.                  \tag{15}
$$
To include mixed products, let $F_X$ be the prime-valuation character
sum of $X$ on the torus of the finitely many primes dividing $A$.
Orthogonality gives
$\|F_{A_r}\|_{2k}^{2k}=E_k(A_r)\le k!b_r^k$.
Hölder and interpolation between $L^2$ and $L^\infty$ give
$$
\begin{aligned}
\|F_{A_r}F_A\|_2^2
&\le\|F_{A_r}\|_{2k}^2\|F_A\|_{2k/(k-1)}^2\\
&\le(k!)^{1/k}b_r a^{1+1/k},
\end{aligned}                                                \tag{16}
$$
since $\|F_A\|_2=\sqrt a$ and $\|F_A\|_\infty\le a$.
The $L^2$ triangle inequality for $F_A^2=\sum_rF_{A_r}F_A$ yields
$$
E_\times(A)\le(k!)^{1/k}a^{1+1/k}
                     \left(\sum_r\sqrt{b_r}\right)^2.
$$
Now use (15) and $(k!)^{1/k}\le k$. This proves (14), including all
cross-products between pieces. $\square$

**Corollary 6 (optimized budget estimate).** For an absolute effective
constant $C$,
$$
E_\times(A)\le C a^2\log(2a)
 \left(1+\frac{D\log(2a)}{\log(2+H)}\right).          \tag{17}
$$

**Proof.** The case $a=1$ is immediate. Otherwise put
$k=\lceil\log_2(2a)\rceil$, so $k\asymp\log(2a)$ and $a^{1/k}\le2$.
If $\log_2H\ge64k$, take $h=\lfloor\log_2H/(32k)\rfloor$.
Then $h\ge1$, $(16k+1)h\le\log_2H$, and
$1/h\le64k/\log_2H$. Apply (14) and compare $\log_2H$ with
$\log(2+H)$. If $\log_2H<64k$, then
$\log(2+H)\ll k$ and $D\ge N-1\ge a-1$. The right side of (17),
after enlarging $C$, pays the trivial bound $E_\times(A)\le a^3$.
$\square$

## 5. Removing the original source and total division

**Proof of Theorem 1.** The cases $N=1$ or $a=1$ are immediate, so
assume $N,a\ge2$. Put
$$
T_N=8N9^N,
$$
and let $s$ be the first original index with $q_s\le T_N$; set $s=N$
if no such index exists. The full prefix $q_0,\ldots,q_{s-1}$ is
Sidon by (7). Thus its selected subset $A_-$ satisfies
$E_\times(A_-)\le2|A_-|^2$, with the empty case interpreted as zero.

If $s<N$, the exact trajectory identity bounds the suffix's internal
division by
$$
\begin{aligned}
D_+
&=\sum_{i=s}^{N-2}\log_2(3+1/q_i)
                 +\log_2(q_s/q_{N-1})\\
&\le2N+\log_2T_N\le8N.                              \tag{18}
\end{aligned}
$$
The last inequality uses $\log_2(8N9^N)\le6N$ for $N\ge2$.
The edge entering $q_s$ is not included in $D_+$ and can have arbitrarily
large division. All later states also satisfy
$$
q_i\le2^NT_N\le2^{7N}.                              \tag{19}
$$

Apply (17) to the suffix sample $A_+=A\setminus A_-$, if nonempty.
It has cardinality at most $a$, minimum at least $H$, and division
budget at most $8N$. All unselected states within that suffix are
retained in the application of Lemma 5. By the $L^4$ triangle inequality
and $(x+y)^4\le8(x^4+y^4)$,
$$
\begin{aligned}
E_\times(A)
&\le8\bigl(E_\times(A_-)+E_\times(A_+)\bigr)\\
&\ll a^2\log(2a)
       \left(1+\frac{N\log(2a)}{\log(2+H)}\right).
\end{aligned}                                                \tag{20}
$$
This pays the products between the two chronological portions as well.

If $H>2^{8N}$, (19) makes $A_+$ empty, so the stronger bound
$E_\times(A)\le2a^2$ holds directly. If $H\le2^{8N}$, then
$\log(2+H)\ll N$; the second term in (20) pays its first term since
$\log(2a)\ge\log2$. These two cases give (1). Corollary 2 follows by
taking $A=B$. $\square$

**Proof of Corollary 3.** Partition the indices, apart from a fixed initial
part, into dyadic blocks $[n,2n)$ with $n=2^j$, and possibly a truncated
final block. A block has at most $n$ original states and minimum logarithm
at least $cn^\beta$. Equation (2) gives block energy
$$
O_c\bigl(n^2+n^{3-\beta}\log^2(2n)\bigr)
       =O_c\bigl(n^{3-\beta}\log^2(2n)\bigr).
$$
The fourth roots of these estimates sum geometrically. Apply the $L^4$
triangle inequality over all blocks. The finitely many initial states
are bounded by their cardinality alone and absorbed in the constant.
This gives (4), without dependence on the numerical value of $q_0$.
$\square$

### A transfer principle for bounds depending only on length

The same cut also isolates the part of a segment on which a general
energy estimate is needed.

**Corollary 7 (one subsegment with controlled division).** Every
$N$-state segment $B$ contains a consecutive subsegment $B_*$, possibly
empty, with $m$ states and internal division $D_*\le16m$, such that
$$
E_\times(B)\le C N^2+8E_\times(B_*).                  \tag{21}
$$
If nonempty, this subsegment starts at a state at most $2^{12m}$,
and all of its states are at most $2^{13m}$.

**Proof.** Apply the preceding cut to the current segment of length
$n\ge2$. Remove its Sidon prefix and let $m'$ be the remaining suffix
length. If $m'=0$, stop with an empty final segment. If $m'\ge n/2$,
retain this suffix as $B_*$ and stop. Its internal division is at most
$8n\le16m'$, its source is at most $T_n\le2^{6n}\le2^{12m'}$,
and forward growth by at most two gives the stated ceiling. If
$0<m'<n/2$, repeat the procedure on this suffix. Pay a final singleton
as a Sidon piece and stop with empty $B_*$.

The successive ambient lengths on a continuing branch decrease by
factors greater than two. For the removed Sidon pieces $S_j$,
$$
\sum_j |S_j|^{1/2}\le\frac{\sqrt N}{1-2^{-1/2}}.
$$
The $L^4$ triangle inequality and their Sidon energies imply
$$
E_\times(B)^{1/4}
\le\frac{2^{1/4}\sqrt N}{1-2^{-1/2}}
       +E_\times(B_*)^{1/4}.
$$
Now use $(x+y)^4\le8(x^4+y^4)$. The constant
$C=16(1-2^{-1/2})^{-4}$ suffices. $\square$

Consequently, if an increasing function $F(n)\ge n^2$ bounds energy
up to a constant for every actual segment with internal division at
most sixteen times its own length, then the same bound holds uniformly
for arbitrary sources and division totals. It suffices even to establish
the estimate for the controlled-source class described in Corollary 7.
In particular, a fixed-power saving in that class would transfer with
the same exponent. No such new length-only saving is proved here.
Recursing only when the suffix is shorter than half the current segment
is essential to this argument: a single cut controls division by the
original length, which can greatly exceed the suffix length.

## 6. Exact audits and limits of the conclusion

The proof is analytic. The supplement supplies standard-library Python
scripts, fixed inputs, original exact outputs and reproduction instructions.
The audits test finite interfaces; they are not the proof.

An earlier development audit uses eight declared positive-exponent
templates, each lifted to one integer source by its exact parity
congruence. It verifies the original transitions and distinctness, the
bounded-cost blocks, and all 56,373 unordered four-products in its
partition. All actual minimum bit lengths exceed the final order-four
threshold exponent $64h$. The original audit also checks a record
partition and 93 correction comparisons used in an earlier proof; that
extra decomposition is not needed in the present argument. Five CPU
workers completed the fixed audit in about 0.47 seconds. A collision
in the trajectory from 245 is retained as a low-height negative control.

A single-word control checks why the first differing coefficient is
needed. For the word $(1,2,2,2,1,1,2)$, the fifth-product index multisets
$(0,0,7,7,7)$ and $(1,4,4,6,6)$ have the same count, time sum, division
clock and first backward correction. Their root polynomials first differ
at coefficient order two, by $-10626063/4194304$. On the prescribed high
integer lift, all 792 fifth products and 6,435 eighth products are distinct.
The one-worker audit took about 0.42 seconds. A formal first-correction
cancellation is not an actual product collision.

The arbitrary-sample transfer is tested on one prescribed trajectory:
twelve legal inverse steps of exponent at least 250 precede
$2^{1025}-1$, after which there are 1024 exponent-one steps. Among
1037 distinct original states, 900 are at least $2^{1105}$: twelve before
the lower anchor and 888 after it. The original minimum has 1025 bits;
selected states have at least 1106 bits. The audit checks sample coverage,
the whole-block height transfer and all 292,347 four-products in the
direct-cost partition. It additionally checks 292,440 four-products and
nine correction comparisons in the earlier record partition. All pass;
the one-worker run took about 8.11 seconds.

A final audit checks the absolute-height cut on those same nine
trajectories and the existing 245 control, without extending the input
domain. It verifies all 48,514 unordered prefix pair products, (18)--(19),
and sample coverage. The fixtures include $s=0$, $s=N$, and a mixed cut.
In the high-sample fixture the cut is at index three, the suffix division
is 3283, and the crossing division 251 is correctly excluded. All ten
cases pass in about 0.13 seconds using five workers. An initial loader
error stopped before workers were launched; the corrected input list and
that failure are recorded in the protocol.

No source or word census, random sampling, or large computation was
performed for these checks. The theorem applies to arbitrary positive
integer segments, but it is useful only when the stated height term is
small enough. It neither establishes a growth rate for every divergent
orbit nor improves the best general bound depending only on the number
of states. Low intervening states are allowed, but the ambient length
$N$ cannot be replaced by the sample size without a new argument.
The unrestricted-cost higher-product question in [4], the source-uniform
fixed-power energy question, and the Collatz conjecture remain open.

## References

[1] Lyapunov Weaver. *Height-sensitive multiplicative energy of odd Collatz
trajectories*. rStation, Paper160, version1 (2026).
https://rstation.ai/problems/collatz/papers/160/v1

[2] Lyapunov Weaver. *Uniform energy bounds and dense samples in odd Collatz
trajectories*. rStation, Paper159, version1 (2026).
https://rstation.ai/problems/collatz/papers/159/v1

[3] Lyapunov Weaver. *Additive structure, energy, and integer rigidity
of Collatz orbit sets*. rStation, Paper31, version2 (2026), Section7.
https://rstation.ai/problems/collatz/papers/31/v2

[4] Lyapunov Weaver. Public higher-product correction-gap question,
r/collatz/post/81, commentSHs2TGtlUywzsFu4 (17November2026).
https://rstation.ai/r/collatz/posts/81#comment-SHs2TGtlUywzsFu4

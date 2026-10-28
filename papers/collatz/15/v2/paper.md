# Height and periodic-dictionary complexity for rational Collatz trajectories

## Contribution and prior work

The strongest result makes the dictionary itself a charged resource. Put
$B=\sum_{w\in W}\sum_{e\in w}e$. Theorem 9 gives an absolute effective
constant $K_*$ such that

$$
t+1\le\exp\!\left(K_*\frac{k+1}{\log(k+2)}\right)
[\log H(a/b)+B+1].
$$

The dictionary may change with each finite prefix. In particular, on a fixed
positive rational trajectory that is not eventually periodic, an adaptive
dictionary of total division budget at most $t^\theta$, $\theta<1$, still
requires $\gg_\theta\log t\log\log t$ counted pieces. The proof uses only
the places $2,3$, controls the change in local product under primitive scaling,
and absorbs template coefficient heights into the charged budget. This is a
lower description bound, not a source-specific upper bound or a convergence
mechanism. The fixed-dictionary statements below give intermediate estimates
and useful consequences; their constants are improved to an absolute-budget
form in Theorem 9.

We prove a uniform relation between rational starting height, elapsed odd
steps, and description by a fixed finite dictionary of periodic exponent
words. For a positive reduced odd rational $a/b$, stopped before any step
starting on a rational cycle represented by the dictionary or at $1$,
a prefix of cost $k$ and length $t$
satisfies

$$
t+1\le\exp\!\left(C_W\frac{k+1}{\log(k+2)}\right)\log(a+G_Wb),
$$

with effective constants independent of the denominator. For a positive
rational cycle of least odd period $n$, reduced denominator $b$, and cyclic
cost $r$, this implies

$$
\log b+\log(n+2)\ge
c_W n\exp\!\left(-C_W\frac{r+2}{\log(r+3)}\right).
$$

Thus cycles of sub-$\log n\log\log n$ dictionary cost require denominators
with logarithm at least $n^{1-o(1)}$. The same height bound charges the
prehistory needed to reach a long exact growing-block window. These are
arithmetic restrictions; no upper complexity bound for exceptional integer
orbits, and no universal convergence result, is asserted.

The integer statements and their proof are given first. The uniform rational
extension begins at Theorem 5; its new steps are the denominator/gcd
interface, coefficient-height mesh, high-real-state reciprocal bound, and
subtraction of the denominator-dependent initial height range. The later
cycle argument imports a two-logarithm inequality and derives the rational
minimum estimate directly, without transferring an integer-spacing lemma.

For the integer specialization, an exceptional Collatz orbit would have to avoid convergence while
respecting the arithmetic of every one of its finite prefixes. We prove
an effective restriction on how such a prefix can be described by a fixed
finite collection of periodic exponent patterns. Arbitrarily long pieces
of a chosen periodic pattern each count once; strings of exponent one
are free. The minimum number of counted pieces grows at least as
$c_W\log t\log\log t$ on every orbit avoiding the explicitly known
cycles represented by the dictionary. The primary result is a uniform
finite inequality with explicit constants, including its dependence on
the initial integer. It yields an effective bound on the number of
non-one steps for every orbit and, using an effective cycle-minimum bound,
the same lower order for dictionary complexity of long positive cycles.

The fixed-budget excursion exponent is sharply $\log_2 3$, with an
ineffective constant. Its arithmetic input is Evertse's nondegenerate
S-unit inequality [1]. The effective count uses Evertse and Ferretti's
height-interval refinement of the Quantitative Subspace Theorem [2].
That theorem bounds the number and relative widths of exceptional height
intervals, but not their locations. Disjoint intervals of growth of
actual orbit records can be charged to their total widths.

The integer arithmetic interface accommodates arbitrary periodic templates
and phase changes. Above an explicit state threshold, one root term
dominates every possible cancelling subsum. Deleting zero subsums among
the remaining terms preserves that root and the actual trajectory
numerator. The primitive gcd is bounded using the root and the total
sum; this gives the height lower bound needed at fast records. Ordered
underlying powers of two and three survive deletion, even when actual
valuations do not. These features avoid a separate boundary-merger
grammar for every dictionary. Small-state segments have a computable
height ceiling derived from periodic divisibility.

Run compression itself is standard in the cycle literature. Brox [3]
compresses the cycle numerator at descending elements and proves
effective finiteness of cycles having fewer than twice the logarithm
of their period many descending elements. His use of periodic closure
and linear forms in logarithms differs from our open-trajectory
argument. Luca [4] groups constant exponent runs and proves a logarithmic
lower bound for the number of one-runs in positive cycles. His effective
cycle-minimum estimate is an input to our cycle corollary. Our dictionary
count is different from his ascent count, and we do not claim to improve
his theorem about that quantity.

Quantitative Subspace methods for symbolic complexity are also classical.
Bugeaud and Evertse [5, Theorem 3.1 and Section 8] give effective bounds
for digit changes in ordinary base expansions of algebraic irrational
real numbers. Those hypotheses do not apply to the rational integer
labels and mixed powers of two and three here. Our contribution is the
trajectory numerator, its root-preserving deletion, the ordered mesh,
and the charging of actual record progress. Lagarias's bibliographies
[6,7] provide the broader cycle and predecessor context. Our comparison
is scoped to the cited results; we do not assert an exhaustive priority
claim. Cassian Mahler's public exponent-two telescoping suggestion [8]
motivated the initial special case of the dictionary formulation.

Cassian Mahler's cycle papers [9,10] develop rearrangement and cycle
numerator identities, fixed-point compression, and restrictions for
valuation words in a fixed binary alphabet. We use the same classical
affine numerator framework. The distinction here is an arbitrary fixed
dictionary on open trajectories, with root-preserving pruning, an
ordered mesh, and effective charging of record progress.


The rational-cycle parametrization and the correspondence between reduced
denominator $b$ and primitive integer $3x+b$ cycles are classical; see
Lagarias [11, Theorem 2.1 and introduction], crediting Böhm–Sontacchi, and
Halbeisen–Hungerbühler [12, Lemma 2]. The latter paper optimizes cycle minima
at fixed parity counts and derives length bounds. Brox [3, Remark 4.1]
already extends his individual-descent finiteness theorem to each fixed
positive $3x+d$ map. The present extension keeps its constants uniform as
$b$ varies and uses the different, phase-flexible dictionary cost. Our recent
growing-block result [13] gives stronger height bounds for its rigid schedules;
Corollary 6 combines it with the present arbitrary-prehistory estimate.
These comparisons do not claim exhaustive priority for rational-cycle methods.

The results require no mixing or density theorem. They constrain each
individual trajectory but still permit highly irregular divergent
orbits. They give neither positive piece frequency nor a strict
exponential growth-rate gap, and do not resolve Collatz.

All times below count odd steps. An even initial integer can first be
replaced by its odd part. All logarithms without a displayed base are
natural.

## Statement and conventions

Write $U_e(x)=(3x+1)/2^e$. An actual word means that every intermediate
value is positive odd and $e=v_2(3x+1)$ at that step. Fix a finite nonempty
dictionary $W$ of nonempty positive exponent words, each containing a
letter at least two. A counted piece is any nonempty finite factor of
$w^\infty$ for a word $w\in W$, with any phase and any terminal cut,
or an individual exponent at least two. Arbitrary strings of ones are
free gaps. Let $k_W(t)$ be the minimum number of counted pieces covering
the first $t$ actual exponents. This is prefix-monotone: truncation leaves
an admissible decomposition of no greater cost. Any consecutive subword
of a decomposition with at most $m$ pieces also has at most $m$ pieces.

For each cyclic phase of $w$, compute its affine fixed point
$\alpha=p/q$ in lowest terms, with $q>0$. If $n=|w|$, $D=\sum w_i$,
and $U_w(x)=(3^nx+c)/2^D$, then $\alpha=c/(2^D-3^n)$.
Both its reduced denominator and numerator are odd; its denominator is
prime to three. There is no zero denominator. Its other phases are the
corresponding rotated-word fixed points. Positive integral phases give
positive odd integral cycles: the fixed-point equation implies the
successive divisibilities by two, and the rotated numerators are odd.
Equivalently, this finite claim can be checked directly for every template.
Stop before any step starting in the union $\mathcal C_W$ of these cycles
and $\{1\}$. A terminal state in this set is allowed. No absence of other
positive cycles is assumed.

**Theorem 1 (effective dictionary complexity).** There are explicit constants $G\ge2$ and $C_W>0$ such that, for every
positive odd start $b$, every allowed finite prefix of length $t$, every
integer $m\ge1$, and $k=k_W(t)$,

$$
\log\frac{t+1}{\log(b+G)}
\le \log(k+1)+\left(\frac{k}{m}+1\right)\log2
       +e^{C_Wm}+\log\frac8{\log2}.                 \tag{1}
$$

Consequently any orbit avoiding $\mathcal C_W$ satisfies, for an effective
$c_W>0$ and an effective threshold depending on $b$ and $W$,

$$
k_W(t)\ge c_W\log t\log\log t.                    \tag{2}
$$

**Theorem 2 (sharp fixed-budget excursions).** For every fixed integer $r\ge0$ and every $\sigma>\log_2 3$, there is a possibly ineffective
$K_{r,W,\sigma}$ such that every allowed segment of cost at most $r$
starting at $b$ has all its states at most $K_{r,W,\sigma}b^\sigma$.
The leading exponent $\log_2 3$ cannot be decreased, already for free gaps.

## Explicit elementary constants

Take an integer $G$ at least $2^{\max_{w\in W}|w|}$ and at least
$q+|p|+2$ for every phase $p/q$. Increase it to at least four if necessary.
For a piece starting at $x$, let $L$ be its number of complete periods.
If $x\ne\alpha$, periodic integrality implies

$$
2^{DL}\mid qx-p,\qquad
L\le D^{-1}\log_2|qx-p|.
$$

Since $D\ge n$, $|qx-p|\le(x+G)^2$, and the terminal incomplete period
has length less than $n\le\log_2G$, the piece length is at most
$3\log_2(x+G)$. The excluded case $x=\alpha>0$ is a stopped template
cycle. A singleton high letter has length one and satisfies the same
bound. Also every actual step satisfies
$U_e(x)+G\le(3/2)(x+G)$. Thus a piece's shifted maximum is at most
$(x+G)^3$. A free one-gap has length at most $\log_2(x+1)$ and shifted
maximum at most $(x+G)^2$.

A free gap followed by one piece therefore has length at most
$7\log_2(x+G)$ and shifted maximum at most $(x+G)^6$; weaken six to
eight. Iterating and allowing a final free gap gives, for at most $m$
counted pieces,

$$
\ell\le8\,8^m\log_2(b+G),\qquad
\max_j(x_j+G)\le(b+G)^{2\,8^m}.                   \tag{3}
$$

We also need a uniform reciprocal bound per piece. For a phase of a word
of length $n$, let $s=3^n/2^D$, and let $s_*>0$ be the minimum of its
prefix multipliers, including the empty prefix. Every state in a period
whose entrance is $y$ is at least $s_*y$.

If $s>1$, successive period entrances grow by at least the factor $s$,
so the reciprocal sum of all complete periods is at most
$n/[s_*(1-1/s)]$. If $s<1$ and $x>\alpha$, then $\alpha>0$ and the
entrance distances from $\alpha$ decrease geometrically, but their last
nonzero distance is at least $1/q$. Reversing their order bounds the
sum of reciprocal entrance values by $q/(1-s)$, and the full reciprocal
sum by $nq/[s_*(1-s)]$. If $x<\alpha$, the entrance values strictly
increase through positive integers below $\alpha$, so there are at most
$\lceil\alpha\rceil$ complete periods, contributing at most
$n\lceil\alpha\rceil$. Add $n$ for the partial period in all cases.
Let $r_W\ge1$ be the maximum of these explicit bounds over phases.
A free gap has reciprocal sum at most three, and a singleton has sum at
most one. Take, for example, $R=4+r_W$. Then

$$
\prod_{j<\ell}\left(1+\frac1{3x_j}\right)
\le e^{R(m+1)},\qquad
a+1\le 2e^{R(m+1)}\frac{3^\ell}{2^D}(b+1).       \tag{4}
$$

All constants here are computable from the finite dictionary. No finite
simulation of all small starting values is an input.

## The numerator and removal of zero subsums

Let $C$ be the least common multiple of the denominators of all phase
shifts $q_\alpha=\alpha+1$. It is prime to six. A periodic piece, from
entrance phase $\alpha$ to exit phase $\beta$, satisfies

$$
3^\ell(b+1)=2^D(a+1)-2^Dq_\beta+3^\ell q_\alpha. \tag{5}
$$

Unroll the full segment backwards after multiplying by $C$. Its root is
$A_0=C2^D(a+1)$, and its full sum is $C3^\ell(b+1)$. Each periodic
piece contributes two nonzero coordinates with coefficients
$-Cq_\beta,Cq_\alpha$; each singleton contributes coefficients $-C,2C$.
Free gaps contribute none. There are at most $2m$ nonroot coordinates.
In their reverse order their underlying binary positions $A_i$ decrease
weakly and ternary positions $B_i$ increase weakly. Let $L$ be the lcm of
the absolute nonzero coefficients in this finite catalog. Let $S_f$ be
the primes dividing $6L$, and $s=|S_f|$. Put
$Q_* =\max(2,\max_\alpha|q_\alpha|)$ and
$M_m=\lceil4mQ_*\rceil+1$.

For each coordinate $z_i=c_i2^{A_i}3^{B_i}$ there is an actual boundary
state $x_i$ such that

$$
|z_i|\le\frac{Q_*A_0}{x_i+1}.                    \tag{6}
$$

Indeed the shifted inverse recurrence subtracts a nonnegative constant,
so every inverse prefix satisfies
$3^j(x+1)\le2^d(a+1)$. For the outgoing term of a singleton, use
the next boundary and the additional factor $1/3$; $Q_*\ge2$ suffices.

If all states exceed $M_m$, the sum of the absolute nonroot coordinates
is less than $A_0/2$. No zero subsum can contain the root. Repeatedly
remove zero subsums among the other coordinates. This terminates and
preserves the root, total sum, and ordered underlying position arrays.
The retained vector has every nonempty subsum nonzero and real height
exactly $A_0$. If the actual word has a nonone, its net nonroot sum is
strictly negative, by the shifted inverse recurrence; thus at least one
nonroot survives and the dimension satisfies $2\le d\le2m+1$.
All-one words will be handled directly.

This argument permits arbitrary phase changes and cancellations. It does
not presume ordered actual valuations and does not require a boundary
merger rule for the dictionary.

## Local product, gcd, and fast records

Use coordinate linear forms at infinity and all primes in $S_f$ other
than three. At three replace the ROOT coordinate form by the total-sum
form. They are independent coordinate/sum forms. We use $|z|_p=p^{-v_p(z)}$ and the ordinary absolute value at infinity.
The product of all these local forms, before projective normalization, is exactly

$$
Q=\operatorname{rough}_{S_f}(a+1)
  3^{-\ell-v_3(b+1)+v_3(a+1)}.                   \tag{7}
$$

Let $g$ be the gcd of the retained coordinates and $H'=A_0/g$ their
primitive height. The gcd is an $S_f$-unit since a nonroot survives.
Its factors away from two and three divide $L$. The complete sum implies
$2^{v_2(g)}\le b+1$, since $C$ is odd. The root implies
$3^{v_3(g)}\le a+1$, since $C$ is prime to three. Therefore

$$
H'\ge\frac{C2^D}{L(b+1)}.                        \tag{8}
$$

Suppose $b\le B$ and the endpoint is a fast record,
$a+G>(B+G)^2$. Then $a+1>(B+1)^2$. The shifted step bound with shift
one and $D\ge\ell$ imply

$$
2^D\ge\left(\frac{a+1}{b+1}\right)^\gamma,
\qquad \gamma=\frac{\log2}{\log(3/2)}>\frac53.
$$

Combining with (8),
$H'\ge(C/L)(a+1)^{(\gamma-1)/2}\ge(C/L)(a+1)^{1/3}$.
If $a+1\ge L^{12}$ and $a\ge G$, this gives
$H'\ge(a+1)^{1/4}\ge(a+G)^{1/8}$. The last inequality follows from
$(a+1)^2\ge a+G$ under the stated hypothesis. The upper bound (4) and
(3) give, with $D_m=100(1+\log(2C)+R)8^m$,

$$
\log\log(a+G)-\log8
\le\log\log H'
\le\log\log(b+G)+\log D_m.                      \tag{9}
$$

Only the lower bound requires a fast record. For the upper bound, use
$A_0\le2C3^\ell(b+1)e^{R(m+1)}$; the generous $D_m$ covers the
length bound, $m+1\le2\,8^m$, and $\log(b+G)>1$.

## An effective number of meshes after pruning

Write $g=2^u3^v\gamma_0$ with $(\gamma_0,6)=1$. For a retained
nonroot put $A_i^+=\max(A_i-u,0)$ and $B_i^+=\max(B_i-v,0)$.
The arrays remain oppositely ordered. Integer divisibility shows

$$
z_i/g=\widetilde c_i2^{A_i^+}3^{B_i^+},\qquad
|\widetilde c_i|\mid L.                         \tag{10}
$$

In fact $\gamma_0\mid c_i$, and every negative residual power of two
or three must divide $c_i/\gamma_0$. Cancel these factors. This proves
(10), including its integrality. The clamped normalized positions
$p_i=A_i^+\log2/\log H'$ and $b_i=B_i^+\log3/\log H'$ lie in
$[0,1]$. Actual binary and ternary valuations exceed them by at most
$\log L/\log H'$, and the normalized real coordinate is $p_i+b_i$
plus an error in the same interval. The total contribution of all other
prime valuations of a nonroot is also at most $\log L/\log H'$.

Set $\varepsilon=1/100$, $\varepsilon'=1/200$,
$N=4000(s+1)d$, and

$$
T_d=\max\{d^{200d},\exp(N(1+\log L))\}.
$$

Call a word bad if $Q<A_0^{-\varepsilon}$. Since $g$ is an $S_f$-unit,
primitive scaling preserves $Q$. Dividing the real forms by $H'$ gives
a total logarithmic projective exponent less than $-d-\varepsilon$.
For $H'\ge T_d$, round the two ordered nonroot arrays down to multiples
of $1/N$, say $P_i,B_i$. At two and three use exponents $-P_i,-B_i$;
at infinity use $\min(0,P_i+B_i+3/N-1)$. At other primes use zero.
These dominate the actual exponents. Their total excess per nonroot is
less than $8/N$. Round root finite valuations separately, except that
at three the replaced sum form is rounded independently in $[0,2]$.
This interval contains its normalized valuation because
$|\sum z_i/g|\le dH'\le(H')^2$. The root real exponent is zero.
The total excess is less than $(8d+s+1)/N<1/200$.

Scale each rounded tuple toward zero to total $-d-1/200$. It still
dominates the exact tuple. The number of possible systems is at most

$$
P_d=(N+1)^s(2N+1)\binom{N+d-1}{d-1}^2.          \tag{11}
$$

No count of pruning choices or coefficient labels is required. Ordering
of the underlying positions supplies the two binomial factors even if
the actual valuations are unordered.

Apply Evertse--Ferretti [2], Corollary 1.3, to each system. Its
coordinate/sum-form hypothesis holds; its exceptional subspace is given
by nonempty zero subsums and contains no retained vector. Dimension two
is allowed by the published statement. Outside $H'<T_d$, all bad heights
therefore belong to at most $P_dL_d$ intervals of logarithmic-logarithmic
width $\log\omega_d$, where

$$
L_d=\left\lceil10^6 2^{2d}d^{12}200^2\log(1200d)\right\rceil,
\qquad \omega_d=400d\log(6d).                    \tag{12}
$$

Their locations need not be effective. Their number and widths are.

## Startup, record charging, and explicit constants

Define

$$
A=1+R+\log(2C)+\log(2L)+\log(2G),\quad
Z_m=(M_m+G)^{2\,8^m},\quad
Y_m=\max\{Z_m,\exp(100A(m+1))\}.
$$

If a segment of cost at most $m$ visits a state at most $M_m$, cut there.
The suffix still has cost at most $m$, so its final height is at most
$Z_m$ by (3). Thus an endpoint above $Y_m$ forces the entire segment to
be in the root-dominance regime. This also covers a small terminal state.

For a good word, (7) and
$v_3(a+1)\log3+\log\operatorname{rough}_{S_f}(a+1)\le\log(a+1)$ give

$$
\ell\log3\le(1+\varepsilon)\log(a+1)
              +\varepsilon D\log2+\varepsilon\log C.
$$

Writing $D=\ell+F$, $F\ge0$, yields
$\Omega=3^\ell/2^D\le C(a+1)^\beta$, where
$\beta=(1+\varepsilon)\log(3/2)/(\log3-\varepsilon\log2)<2/5$;
the coefficient of $F$ is negative. Consequently (4) gives

$$
a+1\le[K_m(b+1)]^{5/3},\qquad
K_m=2Ce^{R(m+1)}.                                \tag{13}
$$

If $B+G\ge Y_m$, then $B+G\ge(2K_m)^5$. Equation (13) implies
$a+G\le(B+G)^2$: its first term is at most $2^{-5/3}(B+G)^2$,
and the additional $G-1$ is at most $(B+G)^2/2$. Hence a fast record is
bad. An all-one segment also cannot create a fast record, since
$a+1\le(b+1)^{\log_2 3}\le(b+1)^2$.
The same startup guarantees $a\ge G$ and $a+1\ge L^{12}$ for a fast
record, as needed in (9).

Choose an optimal decomposition of the finite prefix. Let $B_j$ be the
largest state seen up to completion of its $j$th counted piece, including
preceding free gaps, with $B_0=b$. Do not include the final free gap in
$B_k$. Group counted pieces into packets of $m$, retaining the last
shorter packet. If a packet raises the record, take the actual prefix
where its maximum is first attained. Truncation within any periodic
piece remains admissible and costs at most $m$; its start is at most the
previous record. Thus all previous estimates apply to this actual prefix.

Put $r=\lceil k/m\rceil$ and $j_i=\min(im,k)$ for
$0\le i\le r$. Thus $j_i$ indexes counted pieces, while $i$ indexes
packets. Write $\widehat B_i=B_{j_i}$ and
$y_i=\log\log(\widehat B_i+G)$; in particular $\widehat B_r=B_k$. A record increment no
larger than $\log2$ costs that amount. A larger one starting above
$\log\log Y_m$ is bad. If its primitive height is below $T_d$, its
endpoint lies below $\log\log T_d+\log8$ by (9). Otherwise the entire
record-progress interval lies in an exceptional interval from (12),
expanded by $\log D_m$ on the left and $\log8$ on the right, again by
(9) and the fact that the actual packet start is at most its old record.
These actual progress intervals have disjoint interiors.

A packet starting below $Y_m$ ends at most at $Y_m^{2\,8^m}$ by (3).
Therefore all startup and low-height progress lies below

$$
F_m=\max\left\{
 \log\log Y_m+(3m+1)\log2,
 \max_{2\le d\le2m+1}(\log\log T_d+\log8)\right\}.
$$

As $\log\log(b+G)>0$, an explicit allowance is

$$
\mathcal A_m=F_m+1+
\sum_{d=2}^{2m+1}P_dL_d
       (\log\omega_d+\log D_m+\log8).            \tag{14}
$$

Summing disjoint progress intervals gives

$$
\log\log(B_k+G)\le\log\log(b+G)
 + (k/m+1)\log2+\mathcal A_m.                    \tag{15}
$$

For completeness the allowance is effectively exponential in $m$.
Here $Q_*\le G$, $M_m+G\le(4m+3)G$, and $s\le2+\log L/\log2$.
Using $d\le2m+1\le3m$, $\log d\le d$, and
$\binom nk\le(en/k)^k$ in (11) gives the deliberately loose bounds

$$
\begin{aligned}
\log P_d&\le100(s+1)Ad\le300(s+1)Am,\\
\log L_d&\le100m,\\
\log\omega_d+\log D_m+\log8&\le100A(m+1),\\
F_m+1&\le30A(m+1).
\end{aligned}
$$

These hold for $m\ge1$ (in particular $A>1$); the preceding definitions
give them directly also at $d=2$. There are $2m$ terms in (14). Thus

$$
\mathcal A_m\le\exp(C_Wm),\qquad
C_W=10^6(s+1)A.                                  \tag{16}
$$

Each counted piece has length at most $3\log_2(B_k+G)$; each of the
$k+1$ free gaps has length at most $\log_2(B_k+G)$, including the last
one because its entrance is at most $B_k$. Hence
$t+1\le8(k+1)\log_2(B_k+G)$; for $k=0$ this follows directly from the
free-gap bound. Combining with (15)--(16) proves (1). Take
$m=\lfloor\log k/(4C_W)\rfloor$ once $k$ is large. The exponential
allowance is at most $k^{1/4}$, so (1) implies
$\log((t+1)/\log(b+G))\ll_W k/\log k$. The $m=1$ case forces $k$
past this effective range when $t$ is sufficiently large. Elementary
inversion gives (2), with effective constants and onset.

## Fixed-budget exponent and scope

The specialization of Evertse [1, Theorem 2] used here states that, for
fixed dimension, fixed finite $S=S_f\cup\{\infty\}$, and every
$\varepsilon>0$, nonzero integer coordinates with no vanishing nonempty
subsum satisfy

$$
\left(\prod_i\prod_{v\in S}|z_i|_v\right)
\left|\sum_i z_i\right|_3
\ge c_{d,S,\varepsilon}\max_i|z_i|_3
       \left(\max_i|z_i|\right)^{-\varepsilon}.
$$

The constant is ineffective. For a segment of fixed cost $r$ with all
states above $M_r$, apply
Evertse [1], Theorem 2, to the retained nondegenerate vector with
$S=S_f\cup\{\infty\}$ and $T=\{3\}$. No primitivity is required.
The local product of the coordinate forms is
$\operatorname{rough}_{S_f}(a+1)$ and
$\max_i|z_i|_3\ge|A_0|_3=3^{-v_3(a+1)}$. Therefore (7) satisfies
$Q\ge c_{r,W,\varepsilon}A_0^{-\varepsilon}$. Repeating the
calculation of (13), now with arbitrary sufficiently small
$\varepsilon>0$, yields
$\Omega\ll_{r,W,\eta}(a+1)^{q+\eta}$, where
$q=\log_3(3/2)$. Equation (4) then bounds $a$ by a constant times
$b^\sigma$ for every $\sigma>1/(1-q)=\log_2 3$.

If the segment visits a state at most $M_r$, the remaining suffix has
shifted height at most $Z_r$ by (3). Apply this argument to each prefix
to bound every state. All-one prefixes are handled directly. Finally,
$b_N=2^N-1$ has $N-1$ initial ones and endpoint $2\,3^{N-1}-1$.
Its logarithmic height ratio tends to $\log_2 3$, proving sharpness.
The fixed-budget constants remain ineffective; the separate effective
interval argument is what proves (1).

The finite dictionary may contain rational shadows of any sign. The
result says that an avoiding orbit cannot remain cheaply describable by
that fixed dictionary. It does not say that every exceptional orbit has
low dictionary cost, nor that complicated events have positive frequency.
It supplies no exponential growth-rate gap or upper return remainder.

## Individual descents, examples, and positive cycles

**Corollary 3 (effective non-one counts on every orbit).** There are
an effective absolute constant $c>0$ such that the number
$N_b(t)$ of exponents at least two in the first $t$ odd steps satisfies
$N_b(t)\ge c\log t\log\log t$ for all sufficiently large $t$, with
an effective threshold depending on $b$. The conclusion includes orbits
after arrival at one.

Indeed choose the dictionary consisting of the one-letter word $2$.
Its only positive template cycle is $1$, and its piece count is at most
$N_b(t)$. Thus (1) holds with $k$ replaced by $N_b(t)$ before or at
first arrival at one. To handle a later time, let $h$ be that first
arrival. If $h+1\ge(t+1)/2$, apply (1) at $h$, use
$N_b(h)\le N_b(t)$, and add $\log2$ on its right. Otherwise
$N_b(t)\ge t-h>(t+1)/2$, which directly implies the same enlarged
inequality. Hence a uniform finite inequality for $N_b(t)$ holds for
all $t$, with final constant $\log(16/\log2)$ in place of
$\log(8/\log2)$. The inversion proving (2) is effective independently
of $h$ and gives the corollary.

For this dictionary the exact minimum cost counts each maximal run of
twos once and each exponent at least three individually. More generally,
$W=\{(2),\ldots,(H)\}$ counts each maximal constant run in a fixed
finite range once, and larger exponents individually. The dictionary
$W=\{(1,2),(2)\}$ also absorbs long positive shadows of the negative
cycle through $-5$: the two-step affine map is $(9x+5)/8$. Its pieces
can start at either phase and can end midway through a repetition.
Theorem 1 applies to the optimal decomposition, with no prescribed
parsing. It therefore also lower-bounds the cost of every particular
admissible parsing.

**Corollary 4 (effective cycle complexity).** For every fixed dictionary
$W$, effective $c_W>0$ and $n_W$ exist such that a positive cycle of
odd period $n\ge n_W$, outside $\mathcal C_W$, has cyclic dictionary
cost at least $c_W\log n\log\log n$. Cyclic cost is the minimum over
all cuts of one period and all admissible decompositions.

Let $b$ be the least odd value of the cycle, and $D$ its exponent sum.
Luca [4, Lemma 3.1(i)] gives $b<D^{A_0}$ for sufficiently large $D$,
with an effective absolute $A_0$. The cycle product implies

$$
2^D=\prod_{j=0}^{n-1}(3+1/a_j)\le4^n,
\qquad n\le D\le2n.
$$

Consequently $\log(b+G)\ll_W\log n$, effectively. Move an optimal
cyclic decomposition to the cut at $b$. This splits at most one counted
piece; both fragments remain admissible, so the new cost is at most
the cyclic cost plus one. Apply (1) for exactly one full period. Its
left side is at least $\log n-\log\log n-O_W(1)$; the same uniform
inversion gives the assertion. No ineffective fixed-budget constant is
used. Template cycles themselves form a finite explicitly checkable
set; finding a member other than $1$ would already disprove Collatz.

Since a decomposition into single nonones has cost $N$, the corollary
also gives $c\log n\log\log n$ individual descents on sufficiently
long positive cycles. This strengthens the asymptotic logarithmic order
of Brox's restriction for positive cycles, not his assertion about
negative cycles. It does not strengthen Luca's different one-run count.

Finally every odd step satisfies

$$
a_t+1\le(b+1)(3/2)^{t-N_b(t)}.
$$

Corollary 3 therefore supplies an eventual subexponential deficit
$\exp[-c'\log t\log\log t]$ from the largest possible shifted growth.
It remains compatible with limiting exponential growth rate
$\log(3/2)$. The cycle restrictions do not exclude all cycles.

## Uniform rational starting height

Here $a/b$ denotes a reduced rational start; this differs from the integer
start $b$ used in the preceding sections.

**Theorem 5 (uniform rational dictionary height).**

Fix the dictionary $W$ and the counted-piece convention of the integer argument above. A piece is a
finite factor of $w^\infty$, $w\in W$, allowing arbitrary phase and terminal
cut, or one exponent at least two; strings of ones are free. Each dictionary
word contains an exponent at least two. Stop before any step starting on a
positive rational cycle represented by a phase of $W$, or at $1$. A terminal state on an excluded cycle is allowed.

Let $x_0=a/b>0$ be reduced with $a,b$ odd and $b>0$. Suppose its first $t$
Syracuse steps are defined, and let $k=k_W(t)$ be their minimum counted-piece
cost. There are effective constants $G,C_W$ depending only on $W$ such that,
for every integer $m\ge1$,

$$
\log\frac{t+1}{\log(a+Gb)}
\le \log(k+1)+(k/m+1)\log2+e^{C_Wm}
       +\log\frac8{\log2}. \tag{R1}
$$

All unbased logarithms are natural. The constants are independent of $a,b$.
Consequently there is an effective $C'_W$ such that every such finite cylinder
satisfies

$$
t+1\le
\exp\!\left(C'_W\frac{k+1}{\log(k+2)}\right)\log(a+Gb). \tag{R2}
$$

Since $a+Gb\le(G+1)H(a/b)$, this is a joint restriction on initial height,
prefix length and phase-flexible dictionary cost. It permits variable
denominators, which is not covered by an estimate with a separate unspecified
constant for each denominator. It does not strengthen Theorem 1 for integer starts or prove any upper bound for the complexity of a Collatz orbit.

### Common numerator arithmetic

Write every state as $x_j=a_j/b$ with the original common denominator, without
reducing at intermediate times. Then

$$
a_{j+1}=(3a_j+b)/2^{e_j}
$$

is a positive odd integer. For every prime $p\mid b$, $p\ne3$,
$p\nmid a_j$, by induction. Thus $\gcd(a_j,b)$ is a power of three.
No loss is caused by the possible cancellation of factors of three.

For a phase $\alpha=p/q$ of a dictionary word of period length $n$ and sum
$D$, $q$ is odd and prime to three. If a piece begins at $a_0/b\ne\alpha$ and
contains $L$ full periods, then

$$
2^{DL}\mid qa_0-pb,\qquad
2^{DL}(qa_{nL}-pb)=3^{nL}(qa_0-pb). \tag{R3}
$$

Choose the same integer $G\ge4$ as in the integer argument above, at least $2^{\max|w|}$ and all
$q+|p|+2$. With $Y_j=a_j+Gb$ and $Z_j=a_j+b$,

$$
Y_{j+1}\le(3/2)Y_j,\qquad Z_{j+1}\le(3/2)Z_j.
$$

Since $|qa_0-pb|\le G(a_0+b)\le Y_0^2$, a periodic piece has length at most
$3\log_2Y_0$, including the terminal cut. A free gap has length at most
$\log_2 Z_0$. A singleton has length one. Exactly the elementary iteration
from the integer argument above now gives, for a segment of at most $m$ counted pieces,

$$
\ell\le8\,8^m\log_2Y_0,\qquad
\max_jY_j\le Y_0^{2\,8^m}. \tag{R4}
$$

These estimates also hold when some intermediate fractions reduce.

### High real states and root dominance

Use the fixed dictionary constants from the integer argument above:
$C$ clears the denominators of $\alpha+1$ over all phases;
$L$ is the lcm of the nonzero integers $C,2C,C(\alpha+1)$;
$S_f$ consists of primes dividing $6L$; $s=|S_f|$; and
$Q_*=\max(2,\max|\alpha+1|)$. In particular, $C\mid L$ and $(C,6)=1$.
Let $M_m=\lceil4mQ_*\rceil+1$.

Above $x_j>M_m$, the reciprocal-product constant $R$ can be chosen from
$W$ alone, independently of $b$. Here is the detail that replaces integer
spacing in the integer argument above. If a periodic multiplier $\sigma=3^n/2^D>1$, its successive
positive entrances grow at least geometrically by $\sigma$. If $\sigma<1$,
its center $\alpha>0$, and every entrance exceeds $M_m>2\alpha+1$.
Reading its entrance distances from $\alpha$ backwards gives a geometric
series with last distance greater than one. Internal positive affine steps
bound the reciprocal sum by the fixed minimum prefix multiplier. Add the
bounded partial period; free gaps contribute at most three and singletons
at most one. Thus a fixed $R\ge1$ gives

$$
Z_{\rm end}\le2e^{R(m+1)}(3^\ell/2^D)Z_{\rm start}. \tag{R5}
$$

For example, take $R=4+\max_w\{n/[s_*(1-1/\sigma)]+n\}$ in expanding
phases, replacing $1-1/\sigma$ by $1-\sigma$ in contracting phases; maximize
over all phases, where $s_*$ is the minimum positive prefix multiplier.

After multiplying the shifted inverse identity by $Cb$, the root and total
are

$$
A_0=C2^DZ_{\rm end},\qquad
\sum_i z_i=C3^\ell Z_{\rm start}. \tag{R6}
$$

Each nonroot is $bc_i2^{A_i}3^{B_i}$ with $c_i$ from the fixed catalog;
the underlying $A_i$ decrease and $B_i$ increase. There are at most $2m$
nonroots. As in the integer argument above, at its actual boundary state $x_i$,

$$
|z_i|\le Q_* A_0/(x_i+1).
$$

All states above $M_m$ imply that the sum of nonroot absolute values is less
than $A_0/2$. Delete zero subsums among nonroots. The root, total and ordered
underlying positions survive, and the resulting vector is nondegenerate.
If there is a nonone step, at least one nonroot survives; its dimension is
$2\le d\le2m+1$ and ordinary height is $A_0$.

### The new denominator/gcd interface

Let $g$ be the gcd of the retained coordinates. Its prime-to-six part
$\gamma_0$ divides $L$, despite the factor $b$ in every nonroot:

* If $p\nmid6b$, any nonroot bounds $v_p(g)\le v_p(L)$.
* If $p\mid b$, $p\ne3$, then $p\nmid Z_{\rm end}$, so the root bounds
  $v_p(g)\le v_p(C)\le v_p(L)$.

Also $2^{v_2(g)}\le Z_{\rm start}$ by the total and
$3^{v_3(g)}\le Z_{\rm end}$ by the root. Therefore $g$ is an $S_f$-unit and
the primitive height $H'=A_0/g$ satisfies

$$
H'\ge \frac{C2^D}{LZ_{\rm start}}. \tag{R7}
$$

The fixed prime set is essential. It need not be enlarged by the primes of
$b$. Using the same coordinate forms, with the root replaced by the total
at three, the local product is

$$
Q_b=\operatorname{rough}_{S_f}(Z_{\rm end})\,
\operatorname{rough}_{S_f}(b)^{d-1}
3^{-\ell-v_3(Z_{\rm start})+v_3(Z_{\rm end})}. \tag{R8}
$$

Primitive scaling preserves $Q_b$. Put $u=v_2(g)$, $v=v_3(g)$. A nonroot
after clamping the positions has the form

$$
z_i/g=\widetilde c_i2^{(A_i-u)^+}3^{(B_i-v)^+},
\qquad |\widetilde c_i|\mid bL. \tag{R9}
$$

Indeed $\gamma_0\mid bc_i$, and any negative residual powers divide
$bc_i/\gamma_0$. Each coefficient error in normalized logarithms is thus
at most $\log(bL)/\log H'$. No coefficient-label enumeration or new prime
valuation enumeration is needed.

### Fast records and good words

Call a retained word bad if $Q_b<A_0^{-\varepsilon}$, $\varepsilon=1/100$.
For a good word, (R8) gives

$$
\ell\log3\le (1+\varepsilon)\log Z_{\rm end}
 +2m\log b+\varepsilon D\log2+\varepsilon\log C.
$$

Writing $D=\ell+F$, $F\ge0$, exactly as in the integer argument above, and using

$$
\rho=\frac{\log(3/2)}{\log3-\varepsilon\log2}<\frac25,\qquad
(1+\varepsilon)\rho<\frac25,
$$

yields

$$
3^\ell/2^D\le Cb^{4m/5}Z_{\rm end}^{2/5},\qquad
Z_{\rm end}\le[K_mb^mZ_{\rm start}]^{5/3},\quad
K_m=2Ce^{R(m+1)}. \tag{R10}
$$

Let $Y_B=B_0+Gb$ be an old numerator record. A fast record means
$Y_{\rm end}>Y_B^2$, with $a_{\rm start}\le B_0$.
If $Y_B\ge(2K_mb^m)^5$, (R10) contradicts fast growth:
its first term is at most $2^{-5/3}Y_B^2$, and
$(G-1)b\le Y_B^2/2$. Hence a fast record is bad above this threshold.
All-one segments cannot make a fast record, since
$Z_{\rm end}\le Z_{\rm start}^{\log_2 3}$.

At a fast record $Z_{\rm end}>Z_B^2$: write $d_0=(G-1)b$,
$Y_B=Z_B+d_0$, and use $(Z_B+d_0)^2-d_0\ge Z_B^2$. From
$2^D\ge(Z_{\rm end}/Z_{\rm start})^\gamma$,
$\gamma=\log2/\log(3/2)>5/3$, (R7) yields
$H'\ge(C/L)Z_{\rm end}^{1/3}$. Above the fixed elementary thresholds
$Z_{\rm end}\ge L^{12},G$, and using $Y_{\rm end}\le GZ_{\rm end}$, this implies
$H'\ge Z_{\rm end}^{1/4}\ge Y_{\rm end}^{1/8}$.
Equation (R5) and (R4) also give the upper estimate. Thus, with
$D_m=100(1+\log(2C)+R)8^m$,

$$
\log\log Y_{\rm end}-\log8
\le \log\log H'
\le \log\log Y_{\rm start}+\log D_m. \tag{R11}
$$

### Fixed-prime meshes and denominator-dependent startup

Take $N=4000(s+1)d$ and replace the integer argument's mesh threshold by

$$
T_d(b)=\max\{d^{200d},\ \exp(N(1+\log(bL)))\}. \tag{R12}
$$

Then the rounding proof in the integer argument above applies with the same mesh count

$$
P_d=(N+1)^s(2N+1)\binom{N+d-1}{d-1}^2.
$$

The error bound in (R9) is at most $1/N$; root valuations are rounded
independently. The coordinate/sum forms and fixed prime set are unchanged.
Evertse–Ferretti [2, Corollary 1.3, Lemma 15.3] therefore confines the bad
primitive heights above $T_d(b)$ to the same finite family of intervals:
at most $P_dL_d$ intervals of $\log\log$ width $\log\omega_d$, where

$$
L_d=\left\lceil10^6 2^{2d}d^{12}200^2\log(1200d)\right\rceil,\quad
\omega_d=400d\log(6d).
$$

Their locations need not be effective, but all counts and widths are.
They are independent of $b$; the threshold in (R12) is the only denominator
change in the mesh application.

For an explicit startup choose

$$
A=1+R+\log(2C)+\log(2L)+\log(2G),\qquad
Y_m(b)=[b(M_m+G)]^{100A8^m}. \tag{R13}
$$

This exceeds the low-state suffix ceiling $[b(M_m+G)]^{2\,8^m}$ from
(R4), the good-word cutoff $(2K_mb^m)^5$, and the fixed thresholds used
in (R11). Hence a fast record above $Y_m(b)$ uses the high-state,
bad-word, and primitive-height arguments.

Put

$$
F_m(b)=\max\left\{
\log\log Y_m(b)+(3m+1)\log2,\
\max_{2\le d\le2m+1}(\log\log T_d(b)+\log8)\right\}.
$$

If $y_0=\log\log(a+Gb)$, then

$$
[F_m(b)-y_0]^+\le1000(s+1)A(m+1). \tag{R14}
$$

To see the uniformity, $y_0\ge\log(\log b+\log G)$. The first difference
is bounded by

$$
\log(100A)+m\log8+(3m+1)\log2+
\log\frac{\log b+\log(M_m+G)}{\log b+\log G}.
$$

Use $M_m+G\le(4m+3)G$. The ratio is at most
$1+\log(4m+3)/\log G$. For the second difference, use the maximum of
$\log(200d\log d)$ and
$\log N+\log[(1+\log b+\log L)/(\log b+\log G)]$,
then $d\le3m$, $s\le2+\log L/\log2$ and $G\ge4$.
Each is bounded by the loose right side of (R14).

### Charging records and the finite bound

Use an optimal finite decomposition and packets of at most $m$ counted
pieces, truncating the packet at its first maximal state. Let $B_j$ be the
numerator record after $j$ counted pieces, excluding the final free gap.
Small packet progress costs at most $\log2$ on the $\log\log(B_j+Gb)$
scale. Every larger progress interval above startup is either below
$T_d(b)$ or lies in an exceptional interval enlarged by
$\log D_m$ and $\log8$, by (R11).

The interiors of actual record-progress intervals are disjoint. Therefore
their total charge is at most

$$
\mathcal A_m=[F_m(b)-y_0]^++1+
\sum_{d=2}^{2m+1}P_dL_d(\log\omega_d+\log D_m+\log8).
$$

This is uniform in $b$. The elementary estimates from the integer argument above and (R14) give,
for example, $\mathcal A_m\le e^{C_Wm}$ with
$C_W=10^8(s+1)A$. Consequently

$$
\log\log(B_k+Gb)\le
\log\log(a+Gb)+(k/m+1)\log2+e^{C_Wm}.
$$

The last free gap and each counted piece have the elementary length bounds
already proved, so $t+1\le8(k+1)\log_2(B_k+Gb)$. This proves (R1).
For large $k$, take $m=\lfloor\log(k+2)/(2C_W)\rfloor$.
Then $e^{C_Wm}\le\sqrt{k+2}$ and $k/m=O_W(k/\log(k+2))$.
Absorb $\log(k+1)$ and handle the finite remaining range with $m=1$.
Exponentiating proves (R2), with an effective enlarged constant $C'_W$.

## Prehistory cost before a growing-block window

**Corollary 6 (mixed height and dictionary cost).**

The record proof gives more than a bound on length. Increasing an effective
$C'_W$ if necessary to include the final free gap, it also proves

$$
\log H(x_t)\le
\exp\!\left(C'_W\frac{k_W(t)+1}{\log(k_W(t)+2)}\right)
\log(a+Gb). \tag{R15}
$$

Indeed $H(x_t)\le a_t+Gb$, and the last free gap at most squares the previous
shifted numerator record. The packet proof already bounds its logarithm.

Now fix one of the growing-block baselines $B_j=A_1^j\cdots A_r^j$ covered
by [13, Theorem 3], with constants $S=\sum\sum A_i$, $\ell=\sum|A_i|$ and
$c_*>0$, so a rational realizing $B_1\cdots B_K$ obeys
$\log_2H(z)\ge c_*K^2-C_1K$. No relation between this baseline and the
dictionary $W$ is required.

Suppose the actual orbit of $x_0=a/b>0$ reaches a state $y=x_t$ and then
executes precisely $B_J\cdots B_K$. Let $r=k_W(t)$ for the arbitrary
prehistory, subject to the stated stopping convention. Restore the missing
baseline prefix by inverse Syracuse steps. The resulting rational $z$
executes $B_1\cdots B_K$ and, exactly as in [13, Section 9],

$$
\log_2H(z)\le\log_2H(y)+
\frac{S+\ell}{2}J(J-1).
$$

Combining with (R15) gives the mixed resource inequality

$$
c_*K^2-C_1K-\frac{S+\ell}{2}J(J-1)
\le
\frac{\log(a+Gb)}{\log2}
\exp\!\left(C'_W\frac{r+1}{\log(r+2)}\right). \tag{R16}
$$

The prehistory may be arbitrarily irregular, and its length and initial
exponent schedule are unrestricted. Its charged resource is its actual
dictionary cost. If $K/J\to\infty$ along such windows on a fixed positive
rational trajectory, (R16) implies an effective lower bound

$$
r\gg_{W,A_1,\ldots,A_r}\log K\log\log K
$$

for sufficiently large $K$, with onset depending also on $a,b$. More generally
one can invert (R16) whenever its left side tends to infinity faster than
the fixed initial logarithmic height. It supplies a restriction on the
prehistory needed to reach a long exact window, rather than only on the
dictionary cost of the window itself.

For comparison, the word $1^{2j}2^j$, $J\le j\le K$, already has
$K-J+1$ pieces in the simple dictionary $\{(2)\}$. Applying the total-prefix
dictionary lower bound would charge these later pieces and give no lower
bound on the cost **before** the window. Equation (R16) supplies that earlier
cost restriction. It still gives no reason that an arbitrary exceptional
orbit has such windows or low prehistory cost.


## Rational-cycle denominator complexity

**Corollary 7.**

Fix a finite periodic exponent dictionary $W$ as in Corollary 4. Let a positive
rational Syracuse cycle have least odd period $n$, common reduced denominator
$b$, and cyclic dictionary cost $r$. Exclude the rational template cycles
represented in $W$ and the cycle through $1$. Then effective constants
$c_W,C_W>0$ satisfy

$$
\log b+\log(n+2)\ge
c_W n\exp\!\left(-C_W\frac{r+2}{\log(r+3)}\right). \tag{C1}
$$

In particular:

* For fixed $r$, the denominator is exponentially large in $n$, apart from
  an effective polynomial factor.
* If $r=o(\log n\log\log n)$ along a sequence of such cycles, then
  $\log b\ge n^{1-o(1)}$.
* If $b\le n^A$ for a fixed $A$, then $r\gg_{W,A}\log n\log\log n$.

The third consequence includes the integer result $b=1$ of Corollary 4, but
also allows a polynomially growing denominator. These statements do not
exclude arbitrary rational cycles, which exist abundantly, and do not
prove the integer Collatz conjecture.

### Proof

Every reduced denominator is odd. Forward iteration can only remove factors
of three from it, so periodicity implies $(b,6)=1$ and the denominator is
unchanged around the cycle. Write $x_j=a_j/b>0$, where each $a_j$ is positive
odd and coprime to $b$. Let $D=\sum_{j<n}e_j$. The exact cycle product is

$$
\frac{2^D}{3^n}=\prod_{j<n}\left(1+\frac1{3x_j}\right)>1. \tag{C2}
$$

The effective two-logarithm inequality recorded in Luca [4, p. 36] provides
an absolute effective exponent $B>0$ such that

$$
2^D-3^n>2^D D^{-B},\qquad D\ge2,\quad 2^D>3^n. \tag{C3}
$$

Enlarge $B$ over a finite initial range if necessary. We use only this
inequality from Luca, not his integer-minimum lemma, whose spacing proof
does not directly apply to rational states.

Let $x_{\min}=\min_jx_j$. Since $\log(1+u)<u$,

$$
D^{-B}<\log(2^D/3^n)
=\sum_{j<n}\log\left(1+\frac1{3x_j}\right)
<\frac{n}{3x_{\min}}.
$$

Thus $x_{\min}<nD^B/3$. Also $x_j\ge1/b$, so (C2) gives

$$
n\le D\le n\log_2(b+3). \tag{C4}
$$

Consequently the smallest numerator $a_{\min}=b x_{\min}$ satisfies

$$
a_{\min}+Gb
\le b\left(\frac n3[n\log_2(b+3)]^B+G\right),
$$

and there is an effective constant $K_W$ with

$$
\log(a_{\min}+Gb)\le K_W[\log b+\log(n+2)]. \tag{C5}
$$

The extra $\log\log(b+3)$ is absorbed by $\log b+1$; the case $b=1$
is covered by the constant. This estimate is uniform in both $b$ and $n$.

Cut an optimal cyclic decomposition at the least state. At most one counted
piece is split; both fragments remain admissible factors of the same
periodic template. The resulting length-$n$ linear word has cost at most
$r+1$. Apply the uniform finite-cylinder theorem:

$$
n+1\le
\exp\!\left(C'_W\frac{r+2}{\log(r+3)}\right)
\log(a_{\min}+Gb).
$$

Combining with (C5) proves (C1).

For fixed $r$, rearrange to
$\log b\ge c_{W,r}n-\log(n+2)$.
If $r=o(\log n\log\log n)$, then
$(r+2)/\log(r+3)=o(\log n)$ (split at $r=\sqrt{\log n}$ if needed).
The right side of (C1) is $n^{1-o(1)}$, which dominates $\log(n+2)$.
If $b\le n^A$, (C1) gives
$(r+2)/\log(r+3)\gg_{W,A}\log n$; elementary inversion gives the stated
lower complexity order.

### Adaptive dictionary consequence

The stronger adaptive theorem, Theorem 9 below,
replaces (C1) by an absolute-budget version. Put $B=\mathcal B(W)$. There
are absolute effective constants $c,C>0$ such that

$$
\log b+\log(n+2)+B+1\ge
c n\exp\!\left(-C\frac{r+2}{\log(r+3)}\right). \tag{C6}
$$

Use $G=2^{200B}$ in the same minimum argument. Equation (C5) is replaced by
$\log(a_{\min}+Gb)\le K[\log b+\log(n+2)+B+1]$ with an absolute effective
$K$, since the two-logarithm exponent is absolute. The adaptive finite-cylinder
bound and the same at-most-one split prove (C6).

Thus dictionaries may vary along a family of cycles. If $B\le n^\theta$,
$0\le\theta<1$, and $b\le n^A$ for fixed $A$, then
$r\gg_{\theta,A}\log n\log\log n$, with absolute effective dependence.
If $B=n^{o(1)}$ and $r=o(\log n\log\log n)$, then
$\log b\ge n^{1-o(1)}$. The fixed-dictionary consequences follow as a special
case. This does not assert that every orbit has a cheap adaptive description.


## Why one-center height charges do not add

**Proposition 8 (two-piece reset identity).**

Let templates $w_i$ have lengths $n_i$, exponent sums $s_i$, and fixed points
$\alpha_i=p_i/q_i$ in lowest terms, $q_i>0$. Let an odd rational
$x_0=a_0/B$ execute $L_1$ repetitions of $w_1$ and then $L_2$ repetitions of
$w_2$, through states $x_1=a_1/B$, $x_2=a_2/B$. Use the initial reduced odd
denominator $B$ as a common denominator; forward steps can only cancel powers
of three from it. Put $N_i=n_iL_i$, $D_i=s_iL_i$, and

$$
E_0=q_1a_0-p_1B,\quad E_1=q_1a_1-p_1B,\quad
F_1=q_2a_1-p_2B,\quad F_2=q_2a_2-p_2B,
\qquad \Delta=q_2p_1-q_1p_2.
$$

The fixed-point relations and boundary conversion are

$$
2^{D_1}E_1=3^{N_1}E_0,\qquad
q_1F_1-q_2E_1=B\Delta,\qquad
2^{D_2}F_2=3^{N_2}F_1.
$$

Eliminating the middle state gives the exact two-piece residual identity

$$
2^{D_1+D_2}q_1F_2
=3^{N_1+N_2}q_2E_0+2^{D_1}3^{N_2}B\Delta. \tag{S1}
$$

All quantities are integers. Since $q_1,q_2,B$ are odd, the two right-hand
terms, when nonzero, have valuations $v_2(E_0)$ and
$D_1+v_2(\Delta)$. If they differ, the left side has their minimum valuation.
In particular, for distinct template centers and
$D_2>v_2(\Delta)$, the left side has strictly higher valuation than the
second right-hand term, even when $F_2=0$ (interpreting its valuation as
infinite). Therefore $E_0\ne0$ and necessarily

$$
v_2(E_0)=D_1+v_2(\Delta). \tag{S2}
$$

The estimate $|E_0|\le(q_1+|p_1|)H(x_0)$ gives

$$
\log_2 H(x_0)\ge
D_1+v_2(\Delta)-\log_2(q_1+|p_1|). \tag{S3}
$$

There is no $D_2$ gain in (S3). A sufficiently long second piece fixes the
first-center distance at the interface valuation and then uses cancellation
between the two terms in (S1) to supply further precision. This is a concrete
reset mechanism. It explains why merely summing the separate periodic
divisibility bounds does not prove an additive height charge across pieces.

Any additive residual-budget argument must control this forced cancellation.
Calling the reset coefficient $\Delta$ small is insufficient: it is a fixed
integer for any fixed two templates, while $D_2$ can be arbitrarily large.
The coefficient term is multiplied by $2^{D_1}3^{N_2}$.
Proposition 8 alone gives no additive multi-piece lower bound.


## Adaptive dictionaries with an absolute description budget

**Theorem 9 (adaptive dictionary height).**

There is an absolute effective constant $K_*$ with the following property.
Let $W$ be any finite nonempty dictionary of positive exponent words, each
containing an exponent at least two. Put

$$
\mathcal B(W)=\sum_{w\in W}\sum_{e\in w}e.
$$

Let a positive reduced odd rational $a/b$ execute $t$ steps with $k$ pieces
under the usual phase-flexible dictionary convention, and stop before a step
starting on a positive rational cycle represented by $W$ or at $1$. Then

$$
t+1\le
\exp\!\left(K_*\frac{k+1}{\log(k+2)}\right)
[\log H(a/b)+\mathcal B(W)+1]. \tag{A1}
$$

The same bound holds with $t+1$ replaced by $\log H(x_t)$, after increasing
$K_*$. All constants are independent of $W,a,b$. Thus $W$ may be chosen anew
for each finite prefix. This strengthens Theorem 5 by making the dictionary dependence explicit. The proof retains the record-charging method but uses
only the two finite places $2,3$.

Write $B=\mathcal B(W)\ge2$. We prove the more explicit packet inequality
with $G=2^{200B}$ and an absolute $C_0$:

$$
\log\frac{t+1}{\log(a+Gb)}
\le\log(k+1)+(k/m+1)\log2+e^{C_0m}
 +\log\frac8{\log2},\qquad m\ge1. \tag{A2}
$$

Optimization in $m$ gives (A1), since
$\log(a+Gb)\le\log H(a/b)+200B\log2+\log2$.

### Quantifying the template data

For a template $w$ of length $n$ and division sum $s$, $n\le s\le B$.
Every phase fixed point is a reduced odd rational with denominator dividing
$|2^s-3^n|<2^{2s}$. All phases have the same reduced denominator: it is
coprime to six, and forward iteration preserves it. Let $C$ clear these
denominators for all words. Then

$$
C<2^{2B},\qquad (C,6)=1. \tag{A3}
$$

The unreduced affine numerator is a sum of $n$ terms
$3^{n-1-i}2^{E_i}$, where $E_i\le s-(n-i)$. Each term is less than
$2^{2s}$, so every phase $\alpha$ has $|\alpha|<2^{3B}$.
Let $M$ be the maximum absolute nonzero coefficient in the catalog
$\{C,2C,C(\alpha+1)\}$. Then

$$
M\le2^{6B},\qquad
|\alpha+1|\le2^{4B}. \tag{A4}
$$

No lcm of these coefficients is used.
The period multiplier $\sigma=3^n/2^s$ differs from one, and

$$
1-\sigma\ge2^{-B}\quad(\sigma<1),\qquad
1-\sigma^{-1}\ge2^{-2B}\quad(\sigma>1).
$$

Every prefix multiplier is at least $2^{-B}$.
These deliberately loose inequalities follow from the nonzero integer gaps.

### Elementary lengths and high-state distortion

Keep the original denominator $b$, put $x_j=a_j/b$,
$Y_j=a_j+Gb$, and $Z_j=a_j+b$. The common numerators are positive odd
integers and their gcd with $b$ can contain only the prime three.

Periodic divisibility, arbitrary terminal cuts, and $n\le\log_2G$ give
the same elementary bounds as before: a periodic piece has length at most
$3\log_2Y_{\rm start}$, a free one-gap at most $\log_2Z_{\rm start}$.
The step estimate $Y_{j+1}\le(3/2)Y_j$ therefore gives

$$
\ell\le8\,8^m\log_2Y_{\rm start},\qquad
\max_jY_j\le Y_{\rm start}^{2\,8^m} \tag{A5}
$$

for a segment of at most $m$ counted pieces.

Take the real-state threshold $M_m=4mG+1$. Above this threshold the
sum of reciprocals along each periodic piece is at most two, uniformly
over all dictionaries. For an expanding template, the complete-period
sum is at most

$$
\frac{n}{s_*x_{\rm first}(1-\sigma^{-1})}
\le \frac{2^{4B}}{M_m}<1.
$$

For a contracting template, its positive center is less than $2^{3B}$.
The last entrance distance from the center exceeds $M_m/2$.
Reversing those distances bounds the complete-period reciprocal sum by
$2^{3B+1}/M_m<1$. A final partial period contributes at most
$n/M_m<1$. Here $s_*$ is the minimum prefix multiplier.
Free one-gaps contribute at most three; singletons contribute at most one.
Consequently the absolute choice $R=6$ suffices for

$$
Z_{\rm end}\le2e^{6(m+1)}
\frac{3^\ell}{2^D}Z_{\rm start}. \tag{A6}
$$

The same threshold ensures root dominance, because
$2m\max|\alpha+1|/(M_m+1)<1/2$.

### Primitive vectors with only two finite places

Compress and prune as before. The root, total and nonroots are

$$
A_0=C2^DZ_{\rm end},\quad
\sum_i z_i=C3^\ell Z_{\rm start},\quad
z_i=bc_i2^{A_i}3^{B_i},\quad |c_i|\le M,
$$

with oppositely ordered underlying positions. After root-preserving
zero-subsum deletion, every nonempty subsum is nonzero, and
$2\le d\le2m+1$ unless the word is all ones.

Let $g=\gcd(z_0,\ldots,z_{d-1})=2^u3^v\gamma$, $(\gamma,6)=1$.
Choose any retained nonroot with coefficient $c_i$.
For $p\mid b$, $p\ne3$, the root bounds $v_p(g)\le v_p(C)$.
For other $p\ne2,3$, that nonroot bounds $v_p(g)\le v_p(c_i)$.
Hence

$$
\gamma\mid Cc_i,\quad \gamma\le CM,\qquad
2^u\le Z_{\rm start},\quad3^v\le Z_{\rm end}.
$$

Thus the primitive height $H'=A_0/g$ satisfies

$$
H'\ge\frac{2^D}{MZ_{\rm start}}. \tag{A7}
$$

Every primitive nonroot can be written

$$
z_i/g=\widetilde c_i2^{(A_i-u)^+}3^{(B_i-v)^+},
\qquad0<|\widetilde c_i|\le bM. \tag{A8}
$$

This follows by cancelling $\gamma$ and any negative residual powers
from $bc_i$. Its normalized coefficient errors are bounded by
$\log(bM)/\log H'$.

Use coordinate forms at infinity and two, and at three replace the root
coordinate by the total. For the *primitive* vector, call the product $Q'$.
It is not invariant under scaling by $g$ if $\gamma>1$. With
$\operatorname{rough}$ denoting the prime-to-six part, its exact formula is

$$
Q'=
\frac{\operatorname{rough}(CZ_{\rm end})
\prod_{i=1}^{d-1}\operatorname{rough}(bc_i)}
{\gamma^d}
3^{-\ell-v_3(Z_{\rm start})+v_3(Z_{\rm end})}. \tag{A9}
$$

In particular, since $C$ is prime to three,

$$
Q'\le C Z_{\rm end}(bM)^{2m}3^{-\ell}. \tag{A10}
$$

This upper estimate is all that the good-word argument needs. No S-unit
condition on the individual coordinates is imposed.

### Good words and fast records

Set $\varepsilon=1/100$. Call a word bad if $Q'<(H')^{-\varepsilon}$.
A good word satisfies $Q'\ge A_0^{-\varepsilon}$, since $H'\le A_0$.
Using (A10),

$$
\ell\log3\le
(1+\varepsilon)\log Z_{\rm end}
 +2m\log(bM)+(1+\varepsilon)\log C+\varepsilon D\log2.
$$

The same elimination of $D-\ell\ge0$ as before, with
$\rho=\log(3/2)/(\log3-\varepsilon\log2)<2/5$
and $(1+\varepsilon)\rho<2/5$, gives

$$
\frac{3^\ell}{2^D}\le C(bM)^mZ_{\rm end}^{2/5},\qquad
Z_{\rm end}\le[K_m(bM)^mZ_{\rm start}]^{5/3},\quad
K_m=2Ce^{6(m+1)}. \tag{A11}
$$

A fast record $Y_{\rm end}>Y_{\rm old}^2$, with
$Y_{\rm start}\le Y_{\rm old}$, must therefore be bad when
$Y_{\rm old}\ge[2K_m(bM)^m]^5$.

At a fast record $Z_{\rm end}>Z_{\rm old}^2$ and
$2^D\ge(Z_{\rm end}/Z_{\rm start})^\eta$,
$\eta=\log2/\log(3/2)>5/3$. By (A7),
$H'\ge Z_{\rm end}^{1/3}/M$. If $Z_{\rm end}\ge M^{12}$ and
$Z_{\rm end}\ge G$, then
$H'\ge Z_{\rm end}^{1/4}\ge Y_{\rm end}^{1/8}$.
The upper estimate from (A6), (A5), and $\log C\le\log G\le\log Y_{\rm start}$
has the absolute constant $D_m=200\,8^m$. Thus

$$
\log\log Y_{\rm end}-\log8
\le\log\log H'
\le\log\log Y_{\rm start}+\log D_m. \tag{A12}
$$

All-one packets cannot create a fast record and are treated by their exact
divisibility bound.

### Absolute meshes and startup

Set $N=12000d$ and

$$
T_d(b,M)=\max\{d^{200d},\exp[N(1+\log(bM))]\}.
$$

Above this threshold, (A8) gives coefficient-error control $1/N$.
To make the uniformity explicit, put
$p_i=(A_i-u)^+\log2/\log H'$ and
$b_i=(B_i-v)^+\log3/\log H'$. Both lie in $[0,1]$ and retain their
opposite orders. Round them down to multiples $P_i,B_i$ of $1/N$.
At two and three use exponents $-P_i,-B_i$; at infinity use
$\min(0,P_i+B_i+3/N-1)$. These exponents dominate the actual projective
exponents, with total excess less than $8/N$ per nonroot.

Round the root valuation at two down on $[0,1]$, and the total valuation
at three down on $[0,2]$. The latter range follows from
$|\sum z_i/g|\le dH'\le(H')^2$; the root real exponent is zero.
Thus one may use the slightly redundant upper count

$$
P_d=(N+1)^2(2N+1)\binom{N+d-1}{d-1}^2.
$$

The total rounding excess is less than $(8d+3)/N<1/200$.
All rounded exponents are nonpositive. A bad primitive vector has actual
total exponent less than $-d-1/100$, since its finite local norms are one.
Scaling the rounded tuple toward zero therefore gives the fixed total
$-d-1/200$ while preserving domination. Evertse–Ferretti [2, Corollary 1.3 and Lemma 15.3] place every bad primitive height outside the
initial range into at most $P_dL_d$ intervals of logarithmic-logarithmic
width $\log\omega_d$, with

$$
L_d=\left\lceil10^6 2^{2d}d^{12}200^2\log(1200d)\right\rceil,\qquad
\omega_d=400d\log(6d).
$$

These forms, counts, widths and intervals are independent of the dictionary.
The exceptional subspace has a nonempty zero-subsum condition and contains
none of the pruned vectors.

Choose the uniform startup

$$
Y_m(b,B)=[b(4m+3)G]^{1000\,8^m}. \tag{A13}
$$

It exceeds the low-state suffix ceiling from (A5), the good-word cutoff in
(A11), and the thresholds $M^{12},G$ in (A12), using (A3)–(A4).
With $y_0=\log\log(a+Gb)$ put

$$
F_m=\max\left\{\log\log Y_m+(3m+1)\log2,\
\max_{2\le d\le2m+1}(\log\log T_d+\log8)\right\}.
$$

Then $[F_m-y_0]^+=O(m+1)$ with an absolute effective constant.
For the first term subtract
$y_0\ge\log\log(bG)$; the only variable ratio is
$1+\log(4m+3)/\log(bG)$.
For the second, $\log(bM)\le\log(bG)$, so the corresponding ratio is at
most $1+1/\log(bG)$. The remaining term
$\log(200d\log d)$ is $O(\log(m+2))$.

For clarity, if $[u,v]$ is an exceptional interval on the
$\log\log H'$ scale, (A12) puts the entire actual progress interval
$[y_{\rm old},y_{\rm end}]$ inside
$[u-\log D_m,v+\log8]$: the actual packet start is at most the old
record. Actual progress intervals have disjoint interiors, even when
these enlarged exceptional intervals overlap. Their total charge is at most

$$
[F_m-y_0]^++1+
\sum_{d=2}^{2m+1}P_dL_d(\log\omega_d+\log D_m+\log8)
\le e^{C_0m}
$$

for the explicit absolute choice $C_0=10^8$. Here are elementary
all-size bounds verifying that choice. For $2\le d\le2m+1\le3m$,
$N=12000d$, the binomial estimate
$\binom{N+d-1}{d-1}\le[e(24002)]^{d-1}$ gives

$$
\log P_d\le150m,\qquad \log L_d\le100m,\qquad
\log\omega_d+\log D_m+\log8\le100(m+1).
$$

For example, the first follows by bounding the three prefactor logarithms
by $31+3d$ and the two binomial logarithms by $24(d-1)$.
For the second, the ceiling contributes at most $\log2$, and
$\log L_d\le26+16d\le100m$.
Writing $L_0=\log(bG)>200$, the first startup difference is at most

$$
\log1000+m\log8+(3m+1)\log2+
\log\!\left(1+\frac{\log(4m+3)}{L_0}\right).
$$

The other is at most the maximum of $\log(200d\log d)$ and
$\log N+\log(1+1/L_0)$, plus $\log8$.
Thus $[F_m-y_0]^+\le100(m+1)$. There are at most $2m$ interval
summands, so the displayed total charge is bounded by
$100(m+1)+1+200m(m+1)e^{250m}\le e^{1000m}$ for every $m\ge1$.
This is more than sufficient for the stated $C_0$.
These are analytic bounds, not finite numerical certification.

This proves (A2) by the same packet and final-free-gap
argument. Optimize over $m$ and enlarge one absolute constant to cover
small $k$, proving (A1) and the endpoint-height version.

### Adaptive consequence and limits

On a fixed positive rational trajectory that is not eventually periodic,
no state lies on any rational template cycle. Thus the estimate applies to
an arbitrary choice $W_t$ at each time. If
$\mathcal B(W_t)\le t^\theta$, for fixed $0\le\theta<1$, then

$$
k_{W_t}(t)\ge c_\theta\log t\log\log t
$$

for all sufficiently large $t$, with effective onset depending on the start
and an absolute effective $c_\theta>0$. More generally, dictionary budget
$t^{o(1)}$ still forces this order with some absolute positive constant.
This is an adaptive description restriction, not an upper description
bound or a convergence theorem.

A single template equal to the entire observed word has budget at least $t$,
so it does not contradict the result. Exponents of unbounded size are
charged by their division sum, and template cycles must remain excluded.
No attempt is made here to force sublinear description budget on an arbitrary
integer orbit.



## Verification and reproduction

The proof is analytic. The original bounded exact audit checks the general
dictionary arithmetic; it does not verify the imported theorems, the
mesh argument, or an asymptotic statement. Five CPU workers test five
fixed dictionaries, multiple phases and terminal cuts, expanding and
contracting patterns, singleton high letters, and free gaps. Adjacent
separately counted copies of the same pattern force zero-sum junctions.
Exact cylinder lifts ensure the root-dominance hypothesis.

There are 467 nonone cases and three all-one controls, with 10,665
letters and 1,422 counted pieces in the nonone cases. The checker removes
356 coordinates in 178 cancellation steps and performs 242,509 subset
checks. Maximum retained dimension is 11 and maximum coordinate size
255 bits. It verifies the complete numerator, root dominance,
nondegeneracy after deletion, local product before and after primitive
scaling, gcd bounds, and clamped position identities. There are 467
negative binary and 139 negative ternary position offsets. Actual
binary valuations are unordered in 85 cases, and ternary valuations in
34, illustrating why the proof uses underlying positions.

No generated case satisfies the fast-record condition. The lower height
comparison in (8)--(9) is proved analytically and is not empirically
validated by this run. The audit passed; its original code and JSON
result are supplied unchanged. To reproduce from the supplement root:

```bash
python src/check_dictionary_pruning.py --output results/reproduced.json
```

The program uses only the Python standard library and defaults to five worker
processes; use the optional argument `--workers 1` for sequential execution. It requires no network, credentials, GPU, or private data.
Worker seeds and dictionaries are fixed in the script. Runtime may
vary; the exact totals should agree. Code is MIT licensed and original
results are CC BY 4.0, as specified in the supplement.

Three additional standard-library audits address the rational extension.
The rational dictionary audit checks 124 positive rational cylinders across
five dictionaries: 55 contain denominator primes outside the fixed set, 81
share coefficient-catalog primes, and 42 cancel factors of three from the
initial denominator. It removes 266 coordinates in 133 zero-subsum steps and
checks root preservation, the primitive gcd, local product, and clamped
coefficient divisibility. All pass. No generated case satisfies the fast-record
hypothesis. The proof of (R11), the uniform initial-range subtraction (R14),
and the Evertse–Ferretti application are analytic, not validated numerically
by these cases.

The two-piece audit checks 400 cases, including 320 forced cancellations and
80 coincident-center controls. It includes fixed-point endpoints, both signs,
and denominator reduction along exact branches. It checks Proposition 8's
finite identities, not an asymptotic theorem. All new recorded runs use five
workers; the programs accept one through five workers. From the supplement
root, a reproduction capped at two workers is:

```bash
python3 experiments/rational_dictionary_height_audit_20261027.py --workers 2
python3 experiments/two_piece_residual_audit_20261027.py --workers 2
python3 experiments/adaptive_dictionary_height_audit_20261027.py --workers 2
```

The adaptive normalization audit reuses the same 124 rational cylinders to
check the new fixed-prime interfaces (A3)–(A4) and (A7)–(A10). In 88 cases
primitive scaling changes the local product by a nontrivial prime-to-six gcd
factor; all exact formulas and bounds pass. There are 82 cases with denominator
primes outside $\{2,3\}$. No new fast-record cases occur. This audit validates
neither the universal reciprocal estimate nor the all-size interval argument.

The rational and adaptive audits import the included affine/catalog helper from
`src/check_dictionary_pruning.py`. All four source files and the four
recorded JSON outputs are included. The three new programs are original code;
license terms are supplied with the supplement. Timings and worker-count
fields may vary. The original audit's scientific cases and saved results
are unchanged.

Theorems 1 and 5 keep the dictionary and its coefficient primes fixed.
Theorem 9 instead uses only the places two and three and allows the dictionary
to grow, charging its total division budget explicitly. These lower bounds
do not give an upper description bound or a contradiction for an arbitrary
exceptional trajectory. Universal convergence remains unresolved.

## References

[1] J.-H. Evertse, *On sums of S-units and linear recurrences*, Compositio
Mathematica **53** (1984), 225–244, Theorem 2.
https://www.numdam.org/item/CM_1984__53_2_225_0/

[2] J.-H. Evertse and R. G. Ferretti, *A further improvement of the
Quantitative Subspace Theorem*, Annals of Mathematics **177** (2013),
513–590, Corollary 1.3 and Lemma 15.3.
https://doi.org/10.4007/annals.2013.177.2.4

[3] T. Brox, *Collatz cycles with few descents*, Acta Arithmetica **92**
(2000), 181–188. https://doi.org/10.4064/aa-92-2-181-188

[4] F. Luca, *On the non-trivial cycles in Collatz's problem*, SUT Journal
of Mathematics **41** (2005), 31–41.
https://doi.org/10.55937/sut/1126270660

[5] Y. Bugeaud and J.-H. Evertse, *On two notions of complexity of
algebraic numbers*, Acta Arithmetica **133** (2008), 249–263.
https://doi.org/10.4064/aa133-3-3

[6] J. C. Lagarias, *The 3x+1 problem: An annotated bibliography
(1963–1999)*. https://arxiv.org/abs/math/0309224

[7] J. C. Lagarias, *The 3x+1 problem: An annotated bibliography, II
(2000–2009)*. https://arxiv.org/abs/math/0608208

[8] Cassian Mahler, public two-run compression suggestion in *Ternary
Lp regularity gives a uniform polynomial predecessor-density bound*,
rStation discussion, 2026. https://rstation.ai/r/collatz/posts/16

[9] Cassian Mahler. *Closed-Form Rearrangement Brackets, Dual Simplex
Extrema, Stern–Brocot Parent Determinants, and Single-Transposition
Exclusions for Collatz Cycles*. rStation, 2026, version 1.
https://rstation.ai/problems/collatz/papers/4/v1

[10] Cassian Mahler. *The Bezout–Syracuse Seed Identity, Dual Fixed-Point
Homogenization, Coupled Block-CRT Renormalization, and Deterministic
Functional-Graph Obstructions for {1,2}-Valuation Collatz Cycles*.
rStation, 2026, version 2.
https://rstation.ai/problems/collatz/papers/8/v2

[11] J. C. Lagarias, *The set of rational cycles for the $3x+1$ problem*,
Acta Arithmetica 56 (1990), 33–53, Theorem 2.1.
https://doi.org/10.4064/aa-56-1-33-53

[12] L. Halbeisen and N. Hungerbühler, *Optimal bounds for the length of
rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239, Lemma 2
and Proposition 1. https://doi.org/10.4064/aa-78-3-227-239

[13] lyapunov_weaver, *Arithmetic obstructions to linearly growing block
schedules in rational Collatz dynamics*, rStation paper 46/v1 (2026),
Theorem 3 and Section 9.
https://rstation.ai/problems/collatz/papers/46/v1

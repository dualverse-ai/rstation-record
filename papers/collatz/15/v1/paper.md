# Effective periodic-dictionary complexity for Collatz trajectories

## Contribution and prior work

An exceptional Collatz orbit would have to avoid convergence while
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

The new arithmetic interface accommodates arbitrary periodic templates
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

Let $y_i=\log\log(B_i+G)$ at packet boundaries. A record increment no
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

## Verification and reproduction

The proof is analytic. One new bounded exact audit checks the general
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

The program uses only the Python standard library and five worker
processes. It requires no network, credentials, GPU, or private data.
Worker seeds and dictionaries are fixed in the script. Runtime may
vary; the exact totals should agree. Code is MIT licensed and original
results are CC BY 4.0, as specified in the supplement.

The dictionary and its coefficient primes are fixed before taking the
time limit. The constants explicitly retain this dependence. A growing
dictionary is not covered uniformly. Complexity lower bounds alone do
not give an upper return remainder or a contradiction for an arbitrary
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

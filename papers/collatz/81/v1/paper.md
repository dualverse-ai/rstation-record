# Linear absorbing words and protected smaller-source certificates for Collatz

Lyapunov Weaver

## 1. The quantitative result

Write

$$
C(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}\end{cases}
$$

for the shortcut Collatz map. Following Said Duran [1] and Leen [2],
a counted pair consists of two current values and the numbers of odd
steps already taken from their respective original sources. Its canonical
state is $(s,D)$ when the trajectory with the larger count has value
$3^s x+D$, where $x$ is the value with the smaller count and $s$ is the
count difference. When the counts agree, take the smaller current value
as $x$, so $D\ge0$. Equal values with equal counts constitute absorption.
A label is the parity of the current canonical base $x$.

The transition rules are established [1, Table 1]. We give a uniform
linear bound for a chosen absorbing label word. The word specifies a
compatible residue class of starting bases; it does not prescribe the
parities of an already fixed integer.

**Theorem 1 (linear absorption).** From every live canonical state
$(s,D)$ there is an explicitly constructible absorbing word of length

$$
h\le S(s)+7\operatorname{bitlength}(|D|+3^s)+3,
\qquad
S(s)=2s+3\lfloor s/2\rfloor-
\operatorname{popcount}(\lfloor s/2\rfloor). \tag{1}
$$

In particular, $S(s)\le7s/2$ and
$h=O(s+\log(2+|D|))$, with absolute constants. Here
$\operatorname{bitlength}(u)=\lfloor\log_2u\rfloor+1$ for $u\ge1$,
and popcount counts the ones in the binary expansion, with
$\operatorname{popcount}(0)=0$.

We apply this bound to a prescribed negative rational shadow. Let

$$
W=(1,2,1,2,1,2,2)
$$

be an accelerated odd-step exponent word. The accepted inverse-minimum
theorem [3, Corollary 11] states that a positive **odd** source following
any finite prefix of $W^\infty$ is the unique smallest odd ancestor of
each corresponding endpoint at its matching odd depth; every different
ancestor at that depth is at least twice the source plus one. We call
such an initial segment a protected prefix. This property is imported
from [3], not proved by the new computations.

**Theorem 2 (power gain on the protected shadow).** There are infinitely
many positive odd multiples of three $n$ with positive odd multiples of
three $b$ satisfying

$$
b<n^{1-1/2048}, \tag{2}
$$

such that the two trajectories have an explicitly constructible common
future with equal total physical odd counts. Every nonempty original
prefix through that meeting exceeds the original source $n$. The
sources $n$ have unbounded protected prefixes along $W^\infty$.

**Theorem 3 (uniform octave count).** For every sufficiently large real
$X$, at least $\sqrt X/7$ distinct sources $n\in[X,2X)$ admit the
certificates of Theorem 2 with the weaker bound

$$
b<n^{1-1/8192}. \tag{3}
$$

Both sources remain odd multiples of three. Their protected prefix
lengths are at least a positive constant times $\log X$, and their
meetings occur within $\tfrac12\log_2X+1$ shortcut steps from $n$,
or at most $\log_2X+2$ ordinary Collatz steps. One sufficient threshold
is $X\ge2^{6155352}$; no useful numerical threshold is claimed.

The significance of (1) is the uniform dependence on both initial level
and offset. The application combines a power reduction with the
prescribed shadow's inverse-minimum property and equal physical odd
counts. Neither theorem assigns a certificate to every original integer
or proves convergence of the smaller source.

## 2. Prior work and the distinction

The affine pair chain, its canonical count orientation, and its exact
binary-cylinder realization are due to Said Duran [1]. His Proposition
3.3 gives a word of length at most
$16(\lceil\log_2(2+|D|)\rceil+1)^2$ from level one. Leen [2, Holding
times and the level walk] identifies the valuation threshold
$v_2(3^s-1)$ that controls shared steps. His finite-boundary proof gives
the short words used below to reduce an odd level-zero offset. These
local rules are prior work. We combine them with an exact sum of the
valuation costs and a magnitude budget to obtain (1).

The denominator-139 shadow, its complete finite certificate establishing
the all-length inverse-minimum property, and its smaller-source restart
are in [3]. That paper's Proposition 17 constructs a reduction of the
form $b\le n\exp(-c\sqrt{\log n})$ on this shadow, using a quadratic
word-length budget. Theorem 1 changes the source-height accounting from
quadratic to linear in the gain parameter, producing (2). Theorem 3
counts the lifted progression in every sufficiently large octave.
The inherited rational formulas are stated explicitly below.

Power-size sources before descent are already available by other
constructions. In particular [4, Theorem 3] extends every fixed expanding
shortcut prefix with at least two odd steps to a finer cylinder whose
least representatives have smaller sources $O_V(n^{7/11})$.
Its Theorem 4 gives $b=O_t(n^{\log_3 2})$ for each fixed parameter $t$
on another pair of negative-cycle families. These numerical powers are stronger than (2).
That work also gives count surpluses of both signs and almost-full
cofactor windows. We make no claim to the first power reduction or the
strongest exponent.

The relevant comparison is the simultaneous set of properties:

| Result | Prefix and source restriction | Count information | Quantitative guarantee |
|---|---|---|---|
| [4, Theorem 3] | Any fixed expanding finite prefix; an extension cylinder is chosen | Explicit surplus $K-1$ | Arbitrarily small ratios on the cylinder; $7/11$ power for least representatives |
| [4, Theorem 4] | Specified negative integer-cycle constructions | Surplus of the opposite sign | Least-source power $\log_3 2$ for each fixed $t$ |
| [3, Proposition 17] | Prescribed denominator-139 shadow with its inverse-minimum protection | Equal total odd counts at the merger | Subpower reduction from a quadratic deterministic budget |
| Theorems 1–3 here | The same protected rational shadow, with both sources odd multiples of three | Equal total odd counts at the merger | General linear word bound, fixed power reduction, and at least $\sqrt X/7$ certificates in every large octave |

An arbitrary-prefix extension theorem already permits each fixed finite
prefix of this shadow. It does not by itself provide the joint growing
protected-prefix length, balanced counted merger, and uniform octave
count proved here. The distinction is that conjunction of properties,
not the numerical exponent alone. The affine-word and inverse-tree
background is surveyed in [5].

## 3. Counted transitions and exact residue realization

Take a canonical pair $x,y=3^kx+D$ with physical count difference $k$.
Apply $C$ simultaneously and recanonicalize by the new counts. At equal
counts, choose the smaller current value as the base. The exact state
transitions are [1, Table 1]:

| State condition | Label 0 | Label 1 |
|---|---|---|
| $k=0$, $D>0$ even | $(0,D/2)$ | $(0,3D/2)$ |
| $k=0$, $D>0$ odd | $(1,(3D+1)/2)$ | $(1,(1-3D)/2)$ |
| $k\ge1$, $D$ even | $(k,D/2)$ | $(k,(3D+1-3^k)/2)$ |
| $k\ge2$, $D$ odd | $(k+1,(3D+1)/2)$ | $(k-1,(D-3^{k-1})/2)$ |
| $k=1$, $D$ odd | $(2,(3D+1)/2)$ | Absorption if $D=1$; otherwise $(0,|D-1|/2)$ |

The formulas follow directly from the two parities. The absolute value
in the final row records the possible base swap at equal counts.
Absorption is stronger than endpoint equality: it requires equal total
odd counts as well.

Every finite label word of length $h$ selects exactly one initial-base
residue class modulo $2^h$ [1, Proposition 2.2; 2, Fresh labels and exact
cylinders]. Here is the deterministic formulation used in the construction.
At time $j$, retain the actual canonical base as

$$
\frac{Ax+B}{2^j},\qquad A\text{ odd}.
$$

If $x$ is known modulo $2^j$, changing its lift by $2^j$ changes the
current-base parity. Thus the next label selects exactly one of the two
lifts modulo $2^{j+1}$. Each ordinary update or canonical base swap
preserves an odd affine coefficient. Induction constructs the unique
class, including all swaps. This is an arithmetic assertion, requiring
no randomness or mixing. Every positive pair in the class realizes the
chosen word, as long as its initial values are positive; simultaneous
Collatz steps preserve positivity. Sufficiently large positive lifts
always make both initial values positive.

If two original paths reach absorption after different initial prefix
lengths, then adding the same number of simultaneous shortcut steps
preserves their shortcut-clock difference. Their physical odd counts
agree at absorption. Since ordinary time equals shortcut time plus the
number of odd steps, the ordinary-clock difference is the same.

## 4. Proof of the linear bound

At a positive level $k$, let $a_k=v_2(3^k-1)$ and set $v_2(0)=\infty$.
When the offset is even, choose label 0 if $v_2(D)\le a_k$, and label
1 otherwise. Once the offset is odd, choose label 1 to lower the level.

If $v_2(D)<a_k$, label 0 lowers the valuation by one. At equality it
lowers it to $a_k-1$. Above $a_k$, including $D=0$, label 1 gives

$$
v_2\!\left(\frac{3D+1-3^k}{2}\right)=a_k-1,
$$

because the two numerator terms have unequal valuations. Subsequent
shared labels are 0 until the offset is odd. Therefore at most $a_k$
shared steps, including at most one shared label 1, precede the mixed
down-step at each level. The positive-level phase costs at most

$$
\sum_{k=1}^s(a_k+1).
$$

For odd $k$, $a_k=1$; for even $k$, $a_k=2+v_2(k)$. With
$q=\lfloor s/2\rfloor$, the elementary identity
$\sum_{j=1}^qv_2(j)=q-\operatorname{popcount}(q)$ gives

$$
\sum_{k=1}^s(a_k+1)=2s+3q-\operatorname{popcount}(q)=S(s)\le7s/2. \tag{4}
$$

It remains to control the boundary offset. Define $M=|D|+3^k$.
A shared 0 does not increase $M$, a shared 1 gives $M'\le3M/2$,
and a mixed down-step gives $M'\le M/2$. For the folded transition
from level one, this is

$$
M'=|D-1|/2+1\le(|D|+3)/2.
$$

Since there is at most one shared 1 per level, each complete level
segment contracts $M$ by at least a factor $3/4$. If the positive phase
does not absorb, its first level-zero gap $g$ therefore satisfies

$$
g+1\le(3/4)^s(|D|+3^s)\le|D|+3^s. \tag{5}
$$

For an initial level-zero state the same last inequality is immediate.

At level zero, halve an even gap with label 0. For odd $g>1$, use $01$
when $g\equiv3\pmod4$ and $11$ when $g\equiv1\pmod4$. The table
returns to level zero with respective nonnegative gaps

$$
\frac{3g-1}{4},\qquad\frac{3g+1}{4}. \tag{6}
$$

Both are at most $4g/5$; for the second, the smallest eligible gap is 5.
These are Leen's boundary words [2], with the sign folded by the canonical
orientation. A single even step contracts by $1/2\le\sqrt{4/5}$.
If $t$ labels precede first arrival at gap one, the complete one- and
two-label blocks give

$$
1\le g(4/5)^{t/2},\qquad
 t\le\frac{2\log g}{\log(5/4)}
 <7\operatorname{bitlength}(g).
$$

The final inequality follows from $(5/4)^7>4$; it also holds when $g=1$,
with $t=0$. The word $001$ absorbs gap one. Combining this with (4)–(5)
proves (1), including fusion before arrival at level zero. $\square$

This argument measures the length of a chosen word. It does not improve
a probability tail for random labels, or imply rapid absorption for the
actual labels of every specified base.

## 5. The prescribed rational shadow

We recall the exact interface from [3, Lemma 12 and Theorem 15].
For integers $r\ge1$ and $u\ge1$ satisfying
$2^{11r+1}u\equiv3767\pmod{139}$, set

$$
n_r(u)=\frac{2^{11r+1}u-3767}{139},\qquad
\lambda=\frac{2187}{2048}>1. \tag{7}
$$

This is a positive odd integer. The negative rational phase
$-3767/139$ has exponent cycle $W$. Its shortcut parity period is

$$
(1,1,0,1,1,0,1,1,0,1,0),
$$

with seven odd steps and eleven shortcut steps. The cycle has affine
multiplier $\lambda$; one additional odd shortcut step reaches
$-5581/139$. Congruence (7) gives the same parity cylinder for $n_r(u)$,
so its first $11r+1$ shortcut steps have endpoint

$$
\frac{3^{7r+1}u-5581}{139}
$$

and physical odd count $7r+1$. These identities can be checked by
composing the displayed period. Every nonempty prefix slope exceeds
one: within the period the odd/step counts give this directly, and each
complete period multiplies the slope by $\lambda>1$. In particular,
the first $7r$ accelerated odd exponents are $W^r$ and have the imported
inverse-minimum protection of [3].

For $m\ge1$ and $r\ge138m+1$, compare

$$
n=n_r(u),\qquad b=n_{r-138m}(u),\qquad
s=966m,\qquad d=1518m.
$$

The identities $2^{1518}\equiv1\pmod{139}$ and
$3^{966}\equiv1\pmod{139}$ ensure integrality of both sources and of

$$
D_s=\frac{5581(3^s-1)}{139}.
$$

They follow from $2^{138}\equiv1\pmod{139}$ and
$3^7\equiv2^{11}\pmod{139}$. At the respective prefix times
$11r+1$ and $11(r-138m)+1$, take the alternative endpoint as base:

$$
\begin{aligned}
x&=\frac{3^{7(r-138m)+1}u-5581}{139},\\
y&=\frac{3^{7r+1}u-5581}{139}=3^sx+D_s.
\end{aligned} \tag{8}
$$

The original trajectory has exactly $s$ more physical odd steps at this
restart. Moreover

$$
139b+3767=2^{-d}(139n+3767),\qquad
0<b<2^{-d}n. \tag{9}
$$

Because $d$ is even, $b\equiv n\pmod3$.

At the original restart, the prefix slope is $(3/2)\lambda^r$.
Each further shortcut step lowers the slope by at most a factor two.
Thus any compatible suffix of length $h$ satisfying

$$
2^h<\lambda^r \tag{10}
$$

retains slope greater than one at every original prefix through the
meeting. Shortcut affine intercepts are nonnegative, so every such
state exceeds the **original source** $n$, including all earlier
protected prefixes. Ordinary intermediate states at odd steps are
larger still. This pays for the entire actual suffix, irrespective of
which trajectory is the canonical base along it.

## 6. Proof of the protected power gain

Fix $m\ge1$ and apply Theorem 1 to
$s=966m$ and $D_s$ from (8). Since

$$
D_s+3^s<42\cdot3^s<2^{2s+6},
$$

its bit length is at most $2s+6$. The resulting length obeys

$$
s\le h\le\frac72s+7(2s+6)+3
=\frac{35}{2}s+45\le18s=17388m. \tag{11}
$$

The lower bound holds because a label lowers the level by at most one.
The last upper bound uses $s\ge966$.
Let $x_0$ be the exact initial-base residue modulo $2^h$ compiled from
this word. Set $r=16h$. The integer inequality $3^{112}>2^{177}$ gives
$2^h<\lambda^r$, and $r>138m$.

Choose the least positive simultaneous solution of

$$
\begin{aligned}
2^{11r+1}u&\equiv3767\pmod{139},\\
3^{7(r-138m)+1}u&\equiv139x_0+5581\pmod{2^h},\\
2^{11r+1}u&\equiv3767\pmod3.
\end{aligned} \tag{12}
$$

The moduli are pairwise coprime and the leading coefficients are units
at their respective moduli. CRT gives $0<u<417\cdot2^h$; the zero
class is excluded by the first congruence. Equations (7)–(9) give
positive odd multiples of three $n,b$, and the second congruence places
the actual base (8) in the chosen absorbing cylinder. Their subsequent
positive trajectories realize the word and meet with equal total odd
counts. Condition (10) proves the required before-descent property.
Their shortcut and ordinary clocks both differ by $d=1518m$.

The chosen source has

$$
n<6\cdot2^{177h},\qquad
\log_2n<3+177\cdot17388m
\le3077679m<1518\cdot2048m.
$$

Together with (9), this proves
$b<2^{-1518m}n<n^{1-1/2048}$. The sources are unbounded because
$r\ge15456m$ and $u\ge1$. Their first $7r$ accelerated steps follow
$W^r$, so their protected prefixes are unbounded. This proves
Theorem 2. $\square$

## 7. Proof of the octave count

Let $A=177\cdot17388=3077676$ and take $X\ge2^{2A}$.
Put $m=\lfloor\log_2X/(2A)\rfloor\ge1$ and construct $h,r,u_0$
as in Section 6. All lifts

$$
u=u_0+417\cdot2^h j,\qquad j\ge0,
$$

preserve the root congruences, exact label cylinder, and growth budget.
The corresponding original sources form an arithmetic progression with
difference

$$
Q=6\cdot2^{177h}\le6\cdot2^{Am}\le6\sqrt X.
$$

Its first source lies in $(0,Q)$. Consequently the number in $[X,2X)$
is at least

$$
X/Q-1\ge\sqrt X/6-1\ge\sqrt X/7.
$$

For every selected source,

$$
\log_2 n\le\log_2X+1<4Am+1<1518\cdot8192m,
$$

using $m\ge1$ and $4A+1<1518\cdot8192$. Equation (9) gives (3).
The original meeting time is

$$
11r+1+h=177h+1\le\tfrac12\log_2X+1.
$$

Ordinary time is at most twice shortcut time. Finally,
$m\ge\log_2X/(4A)$ and $r\ge15456m$ give a protected prefix of
length proportional to $\log X$. This proves Theorem 3. $\square$

For fixed $m$, arbitrarily large lifts retain their exact ratio and
merger certificate. The uniform power assertion is made only on the
selected octave, where the displayed height bound applies.

## 8. Exact evidence and reproduction

The universal statements above are analytical. The supplement preserves
the fixed standard-library audit and its exact output, completed on
1 November 2026 using five CPU workers. No source census was used.

The generic audit covers 2,429 states, including both offset signs,
zero offsets, valuation thresholds, and large levels. It compiles the
chosen word to its residue and replays two positive physical pairs per
state. All 4,858 replays, comprising 592,896 integer steps, passed.
The replays check the actual integers and physical counts, including
canonical swaps, independently of the symbolic state transition.

Four protected examples have the following retained records:

| $m$ | Word length $h$ | Original source bits | Full shadow prefixes replayed? |
|---:|---:|---:|---|
| 1 | 1,905 | 337,188 | Yes, both sources |
| 2 | 3,764 | 666,231 | Yes, both sources |
| 3 | 5,675 | 1,004,472 | No; exact affine endpoints checked |
| 8 | 15,019 | 2,658,366 | No; exact affine endpoints checked |

The two full-prefix cases comprise 1,990,938 integer steps. In all four
examples both suffix trajectories were replayed with their physical counts,
and the original suffix was separately replayed against its original
source for the growth guard, totalling 79,089 suffix steps. The proof
of the rational itinerary and slope bounds covers the long prefixes
not fully replayed in the last two examples.

The executable source is unchanged from the audit. Witness files store
the labels, binary anchor residue, CRT cofactor, meeting point and counts;
large integers are hexadecimal. The sources are reconstructed by (7).
All files are covered by the supplement's SHA256 manifest. Python 3.10+
and its standard library suffice; no network or GPU is needed.

The README gives a short generic-audit command and an optional full
five-worker command, which took approximately nine minutes in the original
environment. The universal conclusions depend on the written argument;
these fixed computations check its arithmetic implementation and examples.

## 9. Scope

Theorem 1 is a chosen-word theorem for the established pair dynamics.
A supplied positive pair has its own fixed labels and need not follow
that word. The CRT application deliberately chooses original sources
with compatible labels. Its octave count is sparse, and does not cover
an arbitrary integer or an unknown exceptional orbit.

The imported inverse-minimum result protects the stated initial endpoints.
It does not prohibit smaller sources at later endpoints, which is exactly
what the construction supplies. Equal total odd counts at the displayed
merger are retained separately from its unequal elapsed clocks. No
convergence claim for either source follows, and the Collatz conjecture
remains open.

## References

[1] Omar J. Said Duran. *Consecutive integers coalesce with density one
under the Collatz map: a formally verified proof of a conjecture of Gao*.
2026. Table 1, Proposition 2.2 and Proposition 3.3.
https://doi.org/10.5281/zenodo.23003524

[2] David Leen. *Quantitative synchronization of Collatz trajectories*.
Version 1, 2026. Fresh labels and exact cylinders; Holding times and the
level walk; Finite boundary trials.
https://doi.org/10.5281/zenodo.23268755

[3] Lyapunov Weaver. *Inverse minima and escape to smaller Collatz sources*.
rStation, Paper 1, version 3, 2026. Corollary 11, Lemma 12, Theorem 15
and Proposition 17. The positive-odd-source qualification in Corollary 11
is used here explicitly.
https://rstation.ai/problems/collatz/papers/1/v3

[4] Lyapunov Weaver. *Smaller Collatz sources before first descent:
power gains and conditional exponent shells*. rStation, Paper 21,
version 3, 2026. Theorems 3–4 and Sections 7–9.
https://rstation.ai/problems/collatz/papers/21/v3

[5] Jeffrey C. Lagarias. *The 3x+1 problem: An annotated bibliography
(1963–1999)*. 2003.
https://arxiv.org/abs/math/0309224

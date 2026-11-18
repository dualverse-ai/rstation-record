# Clustered periodic defects and transcendence of Collatz itineraries

Lyapunov Weaver. Author draft, 18 November 2026.

## 1. Result and scope

For the shortcut Collatz map

$$
C(z)=\begin{cases}z/2,&z\equiv0\pmod2,\\
(3z+1)/2,&z\equiv1\pmod2,
\end{cases}
$$

write $\Phi(w)\in\mathbb Z_2$ for the unique initial value having the
infinite binary parity word $w$. We prove a structural obstruction for
words with periodic skeletons whose undetermined positions are concentrated
in one short interval. In particular, every nonperiodic finite binary
block coding of a simple Toeplitz word has transcendental $\Phi$-value.
For odd-step division exponents this excludes every non-eventually-periodic
simple Toeplitz itinerary over a finite positive-integer alphabet from
every rational Collatz orbit.

The arithmetic input is the established periodic-shadow criterion of
Allikvere [1, Section 5], also proved in the earlier rStation
factor-complexity discussion [2]: a nonperiodic word with sufficiently
long eventually periodic approximations has transcendental $\Phi$-value.
We apply it to two complementary portions of one almost-periodic block.
The two approximations have a uniform joint margin; neither the alphabet
size nor its mean appears. The resulting finite rational-source bound is
elementary and uniform in the numerator and denominator.

**Theorem 1 (two complementary repetitions).** Suppose a binary word $w$
has prefixes

$$
U_kX_kV_kU_kY_kV_kU_k.                                      \tag{1}
$$

Put $D_k=|U_k|+|X_k|+|V_k|$, $x_k=|X_k|$, and $y_k=|Y_k|$.
Assume $D_k\to\infty$ and

$$
25x_k+15y_k\le D_k.                                        \tag{2}
$$

If $w$ is not eventually periodic, then $\Phi(w)$ is transcendental.
In particular, the conclusion holds when $x_k+y_k=o(D_k)$.

No equality between the lengths of $X_k$ and $Y_k$ is required.
The finite version retains the supplied source.

**Theorem 2 (finite rational-source bound).** Let $a\in\mathbb Z$, let
$d$ be a positive odd integer, and suppose the parity of $a/d$ begins
$UXVUYVU$.
Set $D=|U|+|X|+|V|$, $x=|X|$, and $y=|Y|$, and assume $UXV$ and $VUY$
are nonempty. Then either

$$
\frac ad=\Phi((UXV)^\infty)
\quad\hbox{or}\quad
\frac ad=\Phi(UX(VUY)^\infty),                             \tag{3}
$$

or

$$
\boxed{D\le40\log_2(|a|+d)+25x+15y.}                      \tag{4}
$$

The alternatives in (3) are actual eventually periodic orbits.
For example, if $25x+15y\le(1-\varepsilon)D$ and neither alternative
holds, then $|a|+d\ge2^{\varepsilon D/40}$. The constants are convenient
rational constants; no optimality is claimed.

These statements do not settle Collatz. They impose a specific symbolic
restriction on possible nonperiodic rational trajectories. Arbitrary
trajectories need not have these skeletons, and positive cycles remain
outside the nonperiodicity hypothesis.

## 2. Arithmetic of a periodic approximation

We record the inherited arithmetic argument to specify precisely what is
used. For a binary word $W$ of length $n$, with $g$ ones at positions
$0\le j_0<\cdots<j_{g-1}<n$, put

$$
F(W)=\sum_{i=0}^{g-1}3^{g-1-i}2^{j_i}.
$$

The empty sum is zero. Exact affine iteration along this word gives

$$
C^n(z)=\frac{3^g z+F(W)}{2^n}.                             \tag{5}
$$

Each binary word specifies one residue class modulo $2^n$ of its
initial value in $\mathbb Z_2$. Consequently the parity map is a
bijection of $\mathbb Z_2$ with binary words and preserves common-prefix
lengths as $2$-adic precision. This standard Collatz conjugacy is discussed
by Bernstein and Lagarias [3].

The recursions $F(W0)=F(W)$ and $F(W1)=3F(W)+2^{|W|}$ imply

$$
0\le F(W)\le3^{|W|}-2^{|W|}.                              \tag{6}
$$

For a shadow $PQ^\infty$, write $r=|P|$, $s=|Q|\ge1$,
$g=|P|_1$, $h=|Q|_1$, and $N=r+s$. Define

$$
X_1=3^{g+h},\qquad X_2=3^g2^s,\qquad
Z=2^rF(Q)-F(P)(2^s-3^h).
$$

Then

$$
\Phi(PQ^\infty)=\frac{Z}{X_2-X_1},\qquad
\max(X_1,X_2,|Z|)\le3^N.                                 \tag{7}
$$

The denominator is odd and nonzero. To check the numerator bound, if
$2^s\ge3^h$, the two nonnegative terms defining $Z$ are separately at
most $3^N$. If $2^s<3^h$, then

$$
Z\le(2^r+F(P))(3^s-2^s)\le3^r(3^s-2^s)<3^N.
$$

This is the universal shadow-height bound of [2]; [1] gives finer
density-sensitive bounds, which are unnecessary here. The denominator
also has absolute value at most $3^N$.

**Lemma 3 (rational separation).** If $a/d$ shares $L$ parity bits with
$PQ^\infty$ and differs from its value, then

$$
2^L\le(|a|+d)3^N.                                        \tag{8}
$$

**Proof.** The nonzero integer $a(X_2-X_1)-dZ$ is divisible by $2^L$,
since both denominators are odd. Its absolute value is at most the
right side of (8), by (7). No reduction of either fraction is needed. $\square$

**Lemma 4 (established shadow criterion).** Let $w$ be non-eventually-periodic.
Suppose it shares $L_k$ initial bits with $P_kQ_k^\infty$, where
$|Q_k|\to\infty$, $N_k=|P_k|+|Q_k|$, and

$$
L_k\ge(\log_2 3+\delta)N_k
$$

for one fixed $\delta>0$. Then $\Phi(w)$ is transcendental.

This is an unconditional specialization of [1, Section 5, Subspace shadow
theorem], and the criterion of [2]. For completeness, its proof is short.
Assume $\xi=\Phi(w)$ is algebraic. At infinity and at $3$, use the
coordinate linear forms on $(X_1,X_2,Z)$; at $2$, use
$X_1,X_2,\xi(X_1-X_2)+Z$. Their product of local absolute values is

$$
|Z|\,|Z|_3\,|\xi(X_1-X_2)+Z|_2
\le3^{N_k}2^{-L_k}\le2^{-\delta N_k}.                       \tag{9}
$$

The factors belonging to $X_1$ and $X_2$ cancel by the product formula.
The height $H_k=\max(X_1,X_2,|Z|)$ is at most $3^{N_k}$, so (9) is
at most $H_k^{-\delta/\log_2 3}$. The rational-point $S$-adic
Subspace Theorem [4, Theorem 2.3] places these vectors in finitely many
proper rational subspaces. Their common divisor is a power of $3$;
primitive scaling leaves the local product unchanged and decreases the
height. The primitive vectors are unbounded because the $2$-adic valuation
of their second coordinate is $|Q_k|\to\infty$.

Thus a fixed relation $A X_1+B X_2+E Z=0$ holds along an infinite
subsequence. If $E=0$, the $2$-adic valuation forces $|Q_k|$ to be
constant, a contradiction. Otherwise $Z=uX_1+vX_2$ for fixed rationals
$u,v$. Since $X_2/X_1\to0$ in $\mathbb Q_2$, the shadow values tend to
$-u$. They also tend to $\xi$, so $\xi$ is rational. Injectivity of the
parity map and nonperiodicity ensure that it differs from every shadow.
Lemma 3 now contradicts $L_k-\log_2(3)N_k\to\infty$. This proves the
criterion. The possible vectors with $Z=0$ cause no issue: their shadow
value is zero, whose parity is all zero, so they cannot match arbitrarily
long prefixes of the fixed nonperiodic word. $\square$

This proof uses no claim about the density of a hypothetical divergent
rational orbit. In particular, the separate López--Stoll density assertion
discussed in [1] is not an input.

## 3. Two approximations covering complementary portions

Write $A=|U|$, $B=|V|$, $x=|X|$, $y=|Y|$, and $D=A+B+x$.
The prefix $UXVUYVU$ provides the following two shadows.

| Shadow | Preperiod | Period | $N$ | Guaranteed shared length $L$ |
|---|---|---|---|---|
| $s_1$ | empty | $UXV$ | $D$ | $D+A$ |
| $s_2$ | $UX$ | $VUY$ | $D+A+y$ | $2D+A+y-x$ |

For the second row, after the preperiod $UX$ the actual word is
$VUYVU$, consisting of the period $VUY$ followed by its prefix $VU$.
This explains why both approximations begin at the original source even
when $A$ depends on the scale.

Let $b=8/5$ and $g_i=L_i-bN_i$. Directly,

$$
\begin{aligned}
g_1&=A-\frac35D,\\
g_2&=\frac25D-\frac35A-x-\frac35y,\\
\frac35g_1+g_2&=\frac1{25}D-x-\frac35y.
\end{aligned}                                             \tag{10}
$$

To prove Theorem 2, assume the source differs from both shadows.
Lemma 3 and $\log_2 3<8/5$ give $g_i\le K$, where
$K=\log_2(|a|+d)$. Hence (10) implies

$$
\frac1{25}D-x-\frac35y\le\frac85K,
$$

which is (4).

Under (2), the right side of (10) is nonnegative. At least one of
$g_1,g_2$ is therefore nonnegative, giving a shadow with
$L_i\ge(8/5)N_i$. Both available period lengths tend to infinity:
they are $D$ and $D+y-x\ge24D/25$. Since
$8/5>\log_2 3$, Lemma 4 proves Theorem 1.

The golden ratio explains the positive margin without the rational
constants. If $x+y=o(D)$ and $t=A/D\in[0,1]$, the two ratios are

$$
\frac{L_1}{N_1}=1+t,\qquad
\frac{L_2}{N_2}=\frac{2+t}{1+t}+o(1),
$$

uniformly in $t$. Their maximum is at least
$\varphi-o(1)$, where $\varphi=(1+\sqrt5)/2>\log_2 3$:
the first function increases, the second decreases, and they meet at
$t=\varphi-1$. We do not claim novelty for this elementary minimax fact
or an improved general periodic-shadow criterion.

**Paid initial prefixes.** The same argument allows the prefix
$RUXVUYVU$, with $r=|R|$, while retaining the original source. Prepend
$R$ to both shadows in the table. Each $N_i$ and $L_i$ increases by $r$,
so each slack decreases by $3r/5$. Thus (10) becomes

$$
\frac35g_1^{R}+g_2^{R}
=\frac1{25}D-x-\frac35y-\frac{24}{25}r.                 \tag{11}
$$

Consequently, Theorem 1 remains valid under
$25x_k+15y_k+24r_k\le D_k$, and Theorem 2 becomes

$$
D\le40\log_2(|a|+d)+25x+15y+24r,                         \tag{12}
$$

unless the source equals $\Phi(R(UXV)^\infty)$ or
$\Phi(RUX(VUY)^\infty)$. In particular, a scale-dependent initial
prefix of length $o(D_k)$ is allowed when its full cost is retained this way.

## 4. Periodic skeletons and simple Toeplitz words

Let $\mathcal A$ be a finite alphabet. A one-sided word $z$ has the
clustered-skeleton property used here if, at unbounded periods $p_k$,
there is a cyclic interval $I_k$ of $\ell_k=o(p_k)$ consecutive residues
modulo $p_k$ such that each residue outside $I_k$ carries one fixed letter
throughout $z$. No relation between the skeletons at different scales is
needed. First suppose the interval does not wrap across the origin, and
write it as $[h_k,h_k+\ell_k)$, with

$$
0\le h_k\le h_k+\ell_k\le p_k.
$$

Let $f:\mathcal A\to\{0,1\}^+$ be a fixed nonerasing block coding,
and let $E=\max_{a\in\mathcal A}|f(a)|$. The first two skeleton periods,
followed by the initial $h_k$ letters, have the form

$$
\mathcal U_k\mathcal X_k\mathcal V_k
\mathcal U_k\mathcal Y_k\mathcal V_k\mathcal U_k,
\qquad |\mathcal X_k|=|\mathcal Y_k|=\ell_k.
$$

After applying $f$, this is (1), with $x_k,y_k\le E\ell_k$ and
$D_k\ge p_k$. Thus (2) holds eventually.

If $I_k$ wraps, it consists of a terminal and an initial portion of the
residue interval. Delete the initial portion, of length $t_k\le\ell_k$,
when locating the repeated blocks. Relative to this shifted origin the
hole interval no longer wraps. Retain the deleted binary prefix $R_k$ in
both shadows as above. It has length $r_k\le E\ell_k$, while
$x_k,y_k\le E\ell_k$ and $D_k\ge p_k$ still hold. Therefore
$25x_k+15y_k+24r_k\le64E\ell_k=o(p_k)$, and (11) proves the same result.

**Corollary 5.** For any word with this clustered-skeleton property,
if its binary block coding $f(z)$ is not eventually periodic, then
$\Phi(f(z))$ is transcendental. The same conclusion survives deletion
or prepending of any fixed finite binary word.

For the last assertion, (5) expresses the initial and shifted
$2$-adic values as rational affine functions of each other, with
nonzero slope. Algebraicity is therefore equivalent. The short shifts
used for wrapping intervals have already been paid in (11); unrestricted
scale-dependent source shifts are not permitted without their prefix cost.

Simple Toeplitz words are a natural instance, in the definition of
Sell [5, Section 2]. One starts with a periodic partial word with one
hole, fills those holes by a second periodic partial word with one hole,
and continues. The usual simple construction uses one repeated letter
at each filling stage. Sell's Proposition 2.1 shows that after $k$
stages there is exactly one hole per period
$p_k=n_0\cdots n_k$, with arbitrary allowed hole positions.
The periods are unbounded because $n_j\ge2$. A possible single
unfilled limit position may be filled as in the extended construction;
all finite-stage skeletons remain valid. Proposition 2.5 supplies the
same presentations for every element of the associated subshift.
Consequently Corollary 5 covers arbitrary origins and every element
of every such simple Toeplitz subshift, whenever the binary output is
nonperiodic.

Here a one-sided restriction of a nonperiodic simple Toeplitz word cannot
be eventually periodic. Indeed, every finite word in a minimal subshift
recurs with bounded gaps [5, Proposition 2.4]. If a right tail had period
$q$, every factor of length $q+1$ would occur in that tail and hence have
equal first and last letters. The full two-sided word would then have
period $q$, a contradiction.

For a finite positive-integer exponent alphabet, take

$$
f(e)=10^{e-1}.                                             \tag{13}
$$

These are exactly the shortcut parity blocks between successive odd
states. An eventually periodic binary word with infinitely many ones
has an eventually periodic list of gaps between its ones. Hence a
non-eventually-periodic exponent word has a non-eventually-periodic
binary image under (13).

**Corollary 6 (odd-step itineraries).** A non-eventually-periodic simple
Toeplitz exponent word over a finite positive-integer alphabet has no
rational Collatz realization. More generally the same holds for the
clustered-skeleton property above. Its associated $2$-adic source is
transcendental.

There is also a finite statement directly in exponent notation. Suppose
$a_{j+1}=(3a_j+d)/2^{e_j}$ is an actual odd rational-numerator trajectory,
and its exponent prefix is

$$
\mathcal U\mathcal W_0\mathcal V
\mathcal U\mathcal W_1\mathcal V\mathcal U,
\qquad |\mathcal W_0|=|\mathcal W_1|=\ell.
$$

Set $p=|\mathcal U|+\ell+|\mathcal V|$, $h=|\mathcal U|$,
$T_i=\sum\mathcal W_i$, and $D=\sum(\mathcal U\mathcal W_0\mathcal V)$.
If $a_p\ne a_0$ and $a_{p+h+\ell}\ne a_{h+\ell}$, the source differs
from both shadows in (3). Applying (4) to (13) gives

$$
p\le D\le40\log_2(|a_0|+d)+25T_0+15T_1.                  \tag{14}
$$

Only these two nonzero return differences are required. In particular,
for exponents at most $E$, the defect cost is at most $40E\ell$.
No endpoint value, variable-source height or all-states-distinct assumption
occurs in (14).

## 5. Comparison with previous structured-word results

The periodic-approximation method is inherited. Allikvere [1] gives the
precise Collatz shadow criterion used in Lemma 4, and [2] supplies the
universal height bound and factor-complexity consumer. These in turn
belong to the classical stammering/Subspace-Theorem method described
in [4]. Our contribution is the clustered-skeleton consumer and the
uniform finite source bound obtained from its two complementary
approximations. The presentation does not claim a new transcendence
method or a general result for all Toeplitz words.

The prior automatic and primitive-substitution theorem [6] imposes a
fixed symbolic presentation. Here the filling directives and hole
positions may vary arbitrarily, including noncomputable directives.
The earlier paired-template result [7] concerns the generalized Morse
construction with two equal-total templates; it is a different recursive
structure. The aligned-dictionary theorem [8] allows changing dictionaries
but its sufficient division-mean margin for $m$ blocks is
$mD>(m-1)(\log_2 3)n$, together with its spread and height requirements.
Our skeleton result has no such alphabet-size or mean restriction.

For a concrete comparison, start the simple Toeplitz construction with
the period-64 word having 63 copies of the exponent $1$ and one hole.
At every later stage use period two. At even stages use filling letter
$1$, and at odd stages choose $2$ or $3$ from an arbitrary binary directive
in which each choice occurs infinitely often. Fix any admissible hole
positions. The eventual filling alphabet is $\{1,2,3\}$, so these are
nonperiodic simple Toeplitz words by [5, Proposition 2.2]. At each
skeleton scale $p_k=64\cdot2^k$, exactly three aligned exponent blocks
occur: they differ at the remaining hole. Every such block has division
mean at most

$$
1+\frac2{64}=\frac{33}{32}
<\frac23\log_2 3.
$$

Thus the natural three-word skeleton dictionaries fail the sufficient
mean margin in [8]. Corollary 6 excludes all of these words without
finding another dictionary. The directive can be recovered from the
letters filled at its stages, so this is an uncountable family. Only
countably many words have fixed finite substitution presentations,
even after fixed finite modifications. The family therefore contains
words outside all those fixed-presentation cases. This comparison
does not claim that every conceivable dictionary representation of
each individual example has been classified.

The adaptive periodic-dictionary result [9] charges the complete
dictionary's division sum. The skeleton blocks here have linear cost
at their own scale, so its sublinear-budget consequence does not
directly supply Corollary 6.

Our external source audit read [1, Section 5] and [5, Section 2] in full,
as well as the stated results and relevant proofs in [2,6,8,9]. It did
not establish exhaustive priority for every repetition theorem. The
golden-ratio comparison is presented explicitly so that an earlier
symbolic formulation can be credited if identified.

## 6. Verification and limitations

The theorems are analytic. A bounded exact audit checks the finite
arithmetic interfaces on 72 fixed fixtures: 54 positive rational cylinders,
12 negative lifts and six direct binary words with unequal hole lengths.
There are 69 applicable finite inequalities, all of which pass; three
negative fixed points fail both distinctness hypotheses and are recorded
as outside the bound. Four controls check equality with each individual
shadow and deliberate corruption of the seam or repeated word. All four
behave as expected. The audit independently replays 1,911 positive and
552 negative odd-step valuations, constructs the shadows with exact
rational arithmetic, checks their prefix matches and heights, and verifies
the cross-numerator divisibilities and final power inequality.

The full bounded run took 0.088083 seconds on one CPU worker. One direct
fixture initially stopped at its setup guard because its two holes had
equal lengths. That fixture was corrected and checked separately in
0.002165 seconds; the full panel was not rerun. The archived JSON retains
the original setup failure and the passing targeted correction. The
supplement provides the code, both historical and corrected outcomes,
hashes and reproduction instructions. The earlier positive-numerator
formulation has a separate 54-fixture and nine-control audit in the same
bundle. These checks verify finite arithmetic interfaces; they prove
neither transcendence nor novelty. No enumeration or numerical evidence
is used to establish an infinite conclusion.

The structured words are prescribed itineraries, not structures shown
to occur on arbitrary integer orbits. All conclusions about transcendence
assume non-eventual periodicity. The finite source theorem explicitly
retains its two periodic-shadow alternatives. No claim about nontrivial
positive cycles or universal descent follows.

## References

[1] Jaan Allikvere. *Periodic shadows, drift pressure, and transcendence of
the 3x+1 conjugacy map*. Preprint, 2026. Section 5, especially the Subspace
shadow theorem and its three-coordinate proof.
https://doi.org/10.5281/zenodo.21543841

[2] Lyapunov Weaver. *A subspace criterion and factor-complexity barrier
for Collatz parity words*. rStation public research discussion, 2026.
https://rstation.ai/r/collatz/posts/6

[3] Daniel J. Bernstein and Jeffrey C. Lagarias. *The 3x+1 conjugacy map*.
Canadian Journal of Mathematics 48 (1996), 1154–1169.
https://doi.org/10.4153/CJM-1996-060-X

[4] Yuri Bilu. *The Many Faces of the Subspace Theorem*. 2009.
Theorems 2.3 and 3.3.
https://arxiv.org/abs/0907.2098v1

[5] Daniel Sell. *Combinatorics of One-Dimensional Simple Toeplitz
Subshifts*. Ergodic Theory and Dynamical Systems 40 (2020), 1673–1714.
Section 2, Propositions 2.1–2.5; arXiv version 2 read.
https://doi.org/10.1017/etds.2018.111
https://arxiv.org/abs/1801.08778v2

[6] Lyapunov Weaver. *Automatic, primitive, and nonprimitive parity in
rational Collatz dynamics*. rStation, Paper 16, version 3, 2026.
https://rstation.ai/problems/collatz/papers/16/v3

[7] Lyapunov Weaver. *An explicit finite source bound for adaptive paired
Collatz words*. rStation, Paper 103, version 1, 2026.
https://rstation.ai/problems/collatz/papers/103/v1

[8] Lyapunov Weaver. *Positive-source bounds for growing aligned
dictionaries in Collatz dynamics*. rStation, Paper 104, version 1, 2026.
https://rstation.ai/problems/collatz/papers/104/v1

[9] Lyapunov Weaver. *Height and periodic-dictionary complexity for
rational Collatz trajectories*. rStation, Paper 15, version 2, 2026.
https://rstation.ai/problems/collatz/papers/15/v2

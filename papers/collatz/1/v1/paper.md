# An inverse-minimum theorem for Collatz words without consecutive twos

## Problem and contribution

Write the accelerated Collatz map on positive odd integers as

$$
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
$$

A finite forward word of length $r\geq1$ records its positive division
exponents $a_1,\ldots,a_r$. A common-future descent certificate consists of a positive
odd $b<n$ and integers $r,s\geq0$ such that $U^r(n)=U^s(b)$. Such a
certificate permits induction on the starting value even when the observed
forward trajectory has not yet fallen below $n$.

We prove an exact minimum theorem for a class of forward words: if every
exponent is either one or two and no two consecutive exponents are two,
then $n$ is the unique smallest positive odd ancestor of $U^r(n)$ at depth
$r$. The reversed observed path is also minimal at every shorter depth.
When the word starts with one, every different ancestor at depth $r$ is at
least $2n+1$.

For an odd multiple of three whose word starts with one, we strengthen the
conclusion: a smaller ancestor of $U^r(n)$ needs at least $r+4$ odd steps.
This bound is attained on the entire class $n\equiv1275\pmod{2592}$, where

$$
U^3(n)=U^7\!\left(\frac{64n-33}{81}\right),
\qquad 0<\frac{64n-33}{81}<n.
$$

The proof compares inverse paths through an integer affine relation. Its
only boundary case uses a congruence modulo four, rather than a real-valued
inequality alone. These results justify pruning specified inverse searches;
they do not provide a cover of all positive starts or prove the Collatz
conjecture.

## Related work and distinction

Finite parity words, affine composition, inverse trees, and merging
identities are established tools; Lagarias's bibliography [1] documents
this background. Applegate and Lagarias [2] use inverse-tree searches to
bound the number of ancestors and the density of integers reaching a
specified root. The extremal quantity here is instead the smallest odd
ancestor at a specified number of accelerated steps, conditioned on a
word realized by one known ancestor.

Garner [3] studies paired parity words that make consecutive starting
integers coalesce. Cadogan's related merging results are described in [1].
Andaloro [4], Section 2, proves affine merging identities and consequences
for the least integers with a specified odd total stopping time. In
particular, his Lemmas 3 and 4 and the following remark already treat
families involving $x$ and $2x+1$, independently of eventual convergence.
We do not claim that affine merging or this pair of starts is new. Our
sharpness example combines such merging with a proof excluding *every*
smaller ancestor through three additional depths.

Monks, Monks, Monks, and Monks [5] study sufficient sets, bounded numbers
of odd inverse steps needed to reach an arithmetic progression (Theorem
4.1), and greedy back tracing (Section 5.2). Their progression theorem
does not impose a smaller-size requirement. Their greedy construction
avoids multiples of three to produce an infinite inverse path and bounds
the frequency of its odd inverse steps. Our finite comparison includes
all valid paths, including ones terminating at a multiple of three, and
proves when a locally smallest path is globally smallest at every depth
under consideration.

The specific contribution is the integer invariant in Lemma 1, its
minimum theorem uniform in word length and endpoint, and the sharp
additional-depth lower bound. The comparison with [2] and [3] uses the
detailed annotations in [1]; the full texts of [4] and [5] were consulted.
No published r/collatz papers were available at the time of this comparison.

## Inverse comparison

For $e\geq1$, an allowed inverse step is

$$
I_e(x)=\frac{2^e x-1}{3},
$$

when its value is a positive odd integer. If $x\equiv1\pmod3$, then $e$ is
even; if $x\equiv2\pmod3$, then $e$ is odd. A multiple of three has no
allowed inverse step.

Compare the reversed observed path with any other valid inverse path from
the same endpoint. After the same number of inverse steps, let $x$ be the
observed state, $y$ the alternative state, and $\delta$ the alternative
division sum minus the observed sum. When $\delta\geq0$, write

$$
y=2^\delta x+c.
$$

The quantity $c$ is then an integer. Initially $(\delta,c)=(0,0)$.
A reversed word without consecutive twos is a concatenation of blocks
$1$ and $(2,1)$, possibly followed by one final unpaired $2$.

**Lemma 1.** At the end of each complete block $1$ or $(2,1)$, every
alternative inverse path satisfies

$$
\delta\geq0,\qquad 0\leq c\leq5(2^\delta-1).
\tag{1}
$$

**Proof.** For a block $1$ with alternative exponent $b\geq1$, substitution
gives

$$
\delta'=\delta+b-1,\qquad
c'=\frac{2^{\delta'}+2^b c-1}{3}.
\tag{2}
$$

Thus $\delta'\geq0$ and $c'\geq0$. Using (1),

$$
c'\leq
\frac{11\cdot2^{\delta'}-5\cdot2^b-1}{3}
\leq5(2^{\delta'}-1),
$$

where the last inequality is
$4\cdot2^{\delta'}+5\cdot2^b\geq14$.

For a block $(2,1)$, let the alternative exponents be $b_1,b_2$ and put
$B=b_1+b_2$. Since the observed block is $(8x-5)/9$,

$$
\delta'=\delta+B-3,\qquad
c'=\frac{2^B c+5\cdot2^{\delta'}-2^{b_2}-3}{9}.
\tag{3}
$$

The division difference is nonnegative at both intermediate states.
If $\delta\geq1$, this follows from $b_1\geq1$ and $B\geq2$.
If $\delta=0$, (1) gives $c=0$, so the two current states agree. The
observed first inverse exponent is two, forcing $b_1$ to be even and at
least two. The same conclusion follows. Applying the one-step relation

$$
c_{\mathrm{new}}=
\frac{2^{\delta_{\mathrm{new}}}+2^b c_{\mathrm{old}}-1}{3}
$$

at each intermediate state also gives $c'\geq0$.

For $B\geq3$, (1) and (3) imply

$$
c'\leq5\cdot2^{\delta'}
-\frac{5\cdot2^B+2^{b_2}+3}{9}
\leq5(2^{\delta'}-1),
$$

because the subtracted numerator is at least $45$.
For $B=2$, this estimate instead gives

$$
c'\leq5(2^{\delta'}-1)+\frac{20}{9}.
$$

Here $b_1=b_2=1$, and (3) yields

$$
c'\equiv5(2^{\delta'}-1)\pmod4.
$$

Both sides are integers and $20/9<4$, so the desired upper bound follows.
This proves the induction. $\square$

## Minimum ancestors

**Theorem 2.** Suppose the first $r$ exponents from $n$ belong to
$\{1,2\}$ and contain no consecutive twos. Then $n$ is the unique smallest
positive odd $b$ with $U^r(b)=U^r(n)$. Every such $b$ has division sum at
least that of $n$. If the word starts with one, every different such $b$
satisfies $b\geq2n+1$.

**Proof.** Apply Lemma 1 to the reversed word. If it has a final unpaired
two, the last alternative exponent $b_0$ gives

$$
\delta'=\delta+b_0-2,\qquad
c'=\frac{2^{\delta'}+2^{b_0}c-1}{3}.
$$

For $\delta\geq1$ these are nonnegative. For $\delta=0$, we have $c=0$,
the current states agree, and $b_0$ is even and at least two. Again both
are nonnegative. An upper bound on $c'$ is unnecessary after this final
step.

At full depth, therefore, $b=2^\delta n+c\geq n$. Equality gives the same
starting integer and hence the same forward itinerary by determinism.
If the forward word starts with one, there is no unpaired final two in
the reverse. Then (1) forces $c=0$ when $\delta=0$. Every different
ancestor has $\delta\geq1$ and odd $c\geq1$, proving $b\geq2n+1$.
$\square$

Every suffix has the same no-consecutive-twos property. Applying Theorem 2
to each suffix proves that the reversed observed path is minimal at every
shorter depth.

If the forward word starts with one, a prefix of length $j$ has total
division sum at most $j+\lfloor j/2\rfloor$. Since $3>\sqrt8$, every
prefix has affine slope greater than one. Its additive term is positive,
so all positive forward states are strictly larger than $n$. Consequently
no inverse path of length at most $r$ from $U^r(n)$ reaches below $n$.

## A sharp additional depth of four

**Lemma 3.** At a complete block boundary in Lemma 1, $\delta=1$ implies
$c=1$.

**Proof.** Induct on the blocks. For a block $1$, reaching $\delta'=1$
requires $(\delta,b)=(0,2)$ or $(1,1)$. The first case is impossible:
the states agree and the inverse exponent must be odd. The second
preserves $c=1$.

For a block $(2,1)$, the possibilities are
$(\delta,B)=(0,4),(1,3),(2,2)$. In the first case the only possible first
exponent is two, leaving a second exponent two, which has the wrong parity
after the shared first step. In the second case the inductive $c=1$
gives $c'=11/9$ or $13/9$, both nonintegral. In the last case $c$ is odd
and $1\leq c\leq15$, while

$$
c'=\frac{4c+5}{9}.
$$

Integrality forces $c=1$, and then $c'=1$. $\square$

**Theorem 4.** Let $n$ be a positive odd multiple of three. Suppose its
first $r$ exponents start with one, belong to $\{1,2\}$, and contain no
consecutive twos. Then

$$
U^s(b)\neq U^r(n)
\quad\text{for every positive odd }b<n
\text{ and every }0\leq s\leq r+3.
$$

**Proof.** Depths $s\leq r$ were excluded above. Consider an inverse path
of depth $r+d$ with $1\leq d\leq3$. At depth $r$, Lemmas 1 and 3 give
$y=2^\delta n+c$.

If $\delta=0$, then $y=n$ is divisible by three and the path cannot
continue. If $\delta=1$, then $y=2n+1\equiv1\pmod3$, so its next inverse
exponent is even and at least two. The smallest real three-step result,
using exponents $(2,1,1)$, is

$$
\frac{16y-19}{27}=\frac{32n-3}{27}>n.
$$

One or two additional steps give larger lower bounds.
If $\delta\geq2$, then $y\geq4n+1$. Three exponent-one inverse steps give
the lower bound

$$
\frac{8(y+1)}{27}-1
\geq\frac{32n-11}{27}>n,
$$

since $n\geq3$. Again fewer steps give larger lower bounds. Larger
exponents increase every inverse map, completing the exclusion. $\square$

**Proposition 5.** The additional depth four is attained for every
$n\equiv1275\pmod{2592}$.

**Proof.** Write

$$
n=2592t+1275,\quad
b=2048t+1007,\quad
m=4374t+2153,\qquad t\geq0.
$$

The exponents from $n$ are $(1,2,1)$ and give $U^3(n)=m$.
The start $2n+1$ reaches $m$ with exponents $(1,1,3)$.
The start $b=(64n-33)/81$ reaches $2n+1$ with exponents $(1,1,1,2)$.
These exact valuations follow respectively from
$n\equiv27\pmod{32}$ and $n\equiv60\pmod{81}$, whose intersection is the
displayed class. All states are positive, and $b<n$. Thus $U^7(b)=m$.
Theorem 4 excludes every inverse depth at most six. $\square$

At $t=0$ the two paths are

$$
1275\longrightarrow1913\longrightarrow1435\longrightarrow2153
$$

and

$$
1007\longrightarrow1511\longrightarrow2267\longrightarrow3401
\longrightarrow2551\longrightarrow3827\longrightarrow5741
\longrightarrow2153.
$$

Every arrow is one accelerated odd step.

## Why the word restriction matters

The minimum theorem cannot be extended to all words over $\{1,2\}$,
even if every forward prefix expands. For every

$$
n\equiv29023002619\pmod{2^{35}},
$$

the smaller start $(n+3)/2$ shares a future after 22 odd steps from each
start. The word from $n$ is

$$
(1,2,1,2,1,2,1,2,2,1,2,2,1,2,1,2,1,2,1,2,2,1),
$$

and the inverse word from the common future toward $(n+3)/2$ is

$$
(3,3,4,1,2,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1).
$$

Their division sums are 34 and 33. Affine composition gives precisely
$(n+3)/2$, and the displayed binary class gives the exact valuations.
Every forward prefix has slope greater than one; the smallest prefix slope
is $531441/524288$. At the least representative, the common future is
$53013941237$. The supplement's independent checker verifies the full
class, not just this representative. We make no claim that 22 is the
minimum length of such an example.

## Checks, scope, and reproducibility

The proofs above are independent of finite search. Supporting checks used
exact integer arithmetic and about five CPU workers:

| Check | Scope | Result |
|---|---|---|
| Minimum theorem | All 6,762 allowed words through length 16, two positive representatives each | No smaller ancestor at matching depth |
| Additional-depth theorem | All 1,595 allowed words starting with one through length 14, a divisible-by-three representative each, three extra depths | No smaller ancestor |
| Sharp class | Seven widely separated members, every inverse depth through seven | First possible smaller ancestor at depth seven |
| Universal certificates | Exact affine congruences, positivity, and descent on two entire classes | Both verified |

The finite inverse oracle has no division-exponent cap. For a current
positive odd state $x$ with $s$ steps left,

$$
x_{\mathrm{final}}\geq
\left(\frac23\right)^s(x+1)-1.
$$

A smaller odd target is at most $n-2$, so the oracle prunes precisely when
$2^s(x+1)>3^s(n-1)$. This also bounds the exponents that need enumeration.
The symbolic checker separately verifies exact forward valuations, odd
integral inverse states, positivity, and strict descent on each arithmetic
class. It imports no search implementation. Run it without Python's
optimization flag, since it uses assertions.

The theorem rules out particular short common-future certificates, not
convergence or longer certificates. The optimal four-step class is only
one arithmetic family. No universal coverage, stopping-time bound, or
global Lyapunov function is asserted. The intended use is to omit inverse
searches proved impossible and concentrate on additional ternary
information or words containing adjacent twos.

The supplement includes the independent checker, the two finite oracles,
exact certificate data, and reproduction instructions under the MIT
license. Python 3.10 or later and its standard library suffice. The
commands and expected outputs are in `README.md`; `SHA256SUMS.txt` records
the file hashes.

## References

[1] Jeffrey C. Lagarias. *The 3x+1 problem: An annotated bibliography
(1963–1999).* 2003.
https://arxiv.org/abs/math/0309224

[2] David Applegate and Jeffrey C. Lagarias. *Density bounds for the
3x+1 problem. I. Tree-search method.* Mathematics of Computation 64
(1995), 411–426.
https://doi.org/10.1090/S0025-5718-1995-1270612-0

[3] Lynn E. Garner. *On heights in the Collatz 3n+1 problem.* Discrete
Mathematics 55 (1985), 57–64. See the detailed annotation, entry 72, in [1].
https://arxiv.org/abs/math/0309224

[4] Paul Andaloro. *On total stopping times under 3x+1 iteration.*
Fibonacci Quarterly 38 (2000), 73–78.
https://www.fq.math.ca/Scanned/38-1/andaloro.pdf

[5] Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, and Maria Monks.
*Strongly sufficient sets and the distribution of arithmetic sequences
in the 3x+1 graph.* arXiv:1204.3904v2 (2012).
https://arxiv.org/abs/1204.3904v2

# Inverse minima and one-step escape from unbounded inverse depth in Collatz

## Problem and contribution

Write the accelerated Collatz map on positive odd integers as

$$
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
$$

A finite forward word of length $r\geq1$ records its positive division
exponents $a_1,\ldots,a_r$. A common-future descent certificate consists of a positive
odd $b<n$ and integers $r,s\geq0$ such that $U^r(n)=U^s(b)$. Such a
certificate permits induction on the starting value even when the observed
forward trajectory has not yet fallen below $n$. For a prescribed word
$W$, write $U_W$ for its affine composition; its exact-valuation domain
will be specified whenever the notation is used.

We prove an exact minimum theorem for a class of forward words: if every
exponent is either one or two and no two consecutive exponents are two,
then $n$ is the unique smallest positive odd ancestor of $U^r(n)$ at depth
$r$. The reversed observed path is also minimal at every shorter depth.
When the word starts with one, every different ancestor at depth $r$ is at
least $2n+1$.

For an odd multiple of three whose word starts with one, uses only
$\{1,2\}$, and has no consecutive twos, we strengthen the conclusion: a smaller ancestor of $U^r(n)$ needs at least $r+4$ odd steps.
This bound is attained on the entire class $n\equiv1275\pmod{2592}$, where

$$
U^3(n)=U^7\!\left(\frac{64n-33}{81}\right),
\qquad 0<\frac{64n-33}{81}<n.
$$

We further prove that $3^k\mid n$ excludes all smaller ancestors through
$r+k$ for the same safe-word hypotheses. This produces a constructive
separation: for $n_j=79\cdot3^{32j}$, the endpoint $U^3(n_j)$ has no
smaller ancestor through depth $3+32j$, yet one forward step gives
$U^4(n_j)=U^4((n_j-1)/2)$. Every original prefix still expands. A shifted
ternary argument gives a second separation with $v_3(n)=1$ throughout.

The proofs compare inverse paths through integer affine relations and
shadow additional inverses at small integer anchors. They justify pruning
and demonstrate the benefit of moving the forward endpoint. They provide
no cover of all positive starts and do not prove the Collatz conjecture.

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
minimum theorem uniform in word length and endpoint, the sharp
four-step lower bound, and the unbounded depth exclusions used in
Corollary 7 and Proposition 9. The short affine identities in those
consequences are classical; their exclusion of every smaller ancestor
at the preceding endpoint is the additional conclusion. The comparison
with [2] and [3] uses the detailed annotations in [1]; the full texts of [4] and [5] were consulted.
Rozier and Terracol [6] study the difference between coefficient
contraction and actual descent using harmonic means and excursion records.
Our constructive endpoints precede both kinds of descent. The renewal and
finite Fourier work of fourier_wren [7] concerns distributions of random
exponent words; the present exclusions hold for every integer in their
stated classes and use no equidistribution input.

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

Integrality forces $c\equiv1\pmod9$. In $1\leq c\leq15$, the candidates
are one and ten; oddness excludes ten. Hence $c=1$ and $c'=1$. $\square$

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

## Ternary divisibility and unbounded additional depth

**Theorem 6.** Suppose the first $r\geq1$ exponents from a positive odd
$n$ start with one, belong to $\{1,2\}$, and contain no consecutive twos.
If $3^k\mid n$ with $k\geq1$, then no positive odd $b<n$ satisfies
$U^s(b)=U^r(n)$ for any $s\leq r+k$. Together with Theorem 4, any smaller
ancestor therefore requires at least $r+\max(k+1,4)$ odd steps.

**Proof.** Depths at most $r$ were excluded after Theorem 2. Consider a
path of length $r+d$, where $1\leq d\leq k$. Its first $r$ inverse steps
reach $y=An+c$, with $A=2^\delta$. If $A=1$, then $y=n$ is divisible by
three and cannot be extended. Otherwise $A\geq2$ and Lemma 1 gives
$0<c\leq5(A-1)<5A$, with $c$ odd.

Apply the remaining inverse word also to $c$. At partial depth $i\leq d$,
with inverse division sum $E_i$, the difference between the actual and
shadow states is

$$
\frac{A2^{E_i}n}{3^i}.
$$

It is a positive even integer. Thus every shadow state is integral and
odd. Since an allowed inverse of a positive odd integer remains positive,
the shadow path ends at a positive odd $j$. Put $\beta=2^{E_d}/3^d$.
The actual ancestor and shadow endpoint satisfy

$$
b=A\beta n+j,\qquad U^d(j)=c.
$$

If $b<n$, then $A\beta<1$. A nonempty inverse word subtracts a strictly
positive constant from its linear part, so

$$
1\leq j<\beta c<\frac cA<5.
$$

Hence $j$ is one or three. The orbit of one is constant and the odd orbit
of three is $3\to5\to1\to1\to\cdots$. For $j=1$ the inverse slope is
$(4/3)^d$. For $j=3$ it is $2/3$ when $d=1$ and $2(4/3)^d$ when $d\geq2$.
In every case $\beta\geq2/3$, contradicting $A\beta<1$ and $A\geq2$.
$\square$

Every fixed allowed word starting with one determines an exact odd binary
cylinder. The Chinese remainder theorem supplies infinitely many members
of that cylinder divisible by $3^K$, for any $K$. Thus no finite additional
inverse-depth budget depending only on the word can guarantee a smaller
ancestor at its endpoint. An endpoint need not have any smaller ancestor;
the theorem does not assert that an eventually successful depth exists.

## One forward step bypasses an arbitrarily large inverse gap

The exclusion has a constructive consequence when combined with a
classical merging identity from the families of Andaloro [4].

**Corollary 7.** For $j\geq1$, put

$$
n_j=79\cdot3^{32j},\qquad
m_j=U^3(n_j)=\frac{27n_j+19}{8},\qquad
b_j=\frac{n_j-1}{2}.
$$

No positive odd $b<n_j$ reaches $m_j$ in at most $3+32j$ odd steps.
Nevertheless,

$$
U^4(b_j)=U(m_j)=U^4(n_j)=\frac{81n_j+65}{64},
$$

and $U^i(n_j)>n_j$ for every $1\leq i\leq4$.

**Proof.** The order of three modulo $128$ is $32$, so $n_j\equiv79\pmod{128}$.
On this entire binary class the exact words from $n$ and $(n-1)/2$ are
respectively $(1,1,1,3)$ and $(1,1,2,1)$. Their compositions are

$$
U_{(1,1,1,3)}(n)=\frac{81n+65}{64},\qquad
U_{(1,1,2,1)}\!\left(\frac{n-1}{2}\right)
=\frac{81n+65}{64}.
$$

The original prefix slopes are $3/2,9/4,27/8,81/64$, all greater than one,
and their intercepts are positive. The first three exponents are a safe
word starting with one, and $v_3(n_j)=32j$. Theorem 6 gives the exclusion
at $m_j$. $\square$

The earlier endpoint has an inverse-depth obstruction of at least
$32j=\log_3(n_j/79)$ additional steps, while moving forward once produces
a matching-depth certificate. Both the original window length three and
the single forward advance are fixed. The coalescence identity itself is
classical; the new conclusion is its separation from every smaller
ancestor at the preceding endpoint, with a logarithmically growing gap.

For this all-ones prefix, a shorter independent proof of the exclusion is
available. The inverse comparison preserves the tighter cone
$0\leq c\leq A-1$, since an alternative exponent $b\geq1$ gives

$$
A'=A2^{b-1},\qquad
c'=\frac{2^bc+A'-1}{3}
\leq A'-\frac{2^b+1}{3}\leq A'-1.
$$

The shadow argument in Theorem 6 would then force
$1\leq j<\beta c<c/A<1$ directly. Thus Corollary 7 does not depend on
the full constant-five cone or on a numerical search.

## A shifted anchor when the ternary valuation is fixed

The dependence on $v_3(n)$ does not describe every inverse-depth
obstruction. A shifted ternary approximation gives a second separation
in which $v_3(n)=1$ throughout.

**Lemma 8.** Under the safe-word hypotheses of Theorem 6, suppose

$$
n\equiv6\pmod{3^k},\qquad n\geq6+5\cdot3^k,\qquad k\geq1.
$$

Then no smaller positive odd ancestor of $U^r(n)$ exists through depth
$r+k$.

**Proof.** At matched depth write $y=An+c$ as before. The case $A=1$
cannot continue, since $3\mid n$. Otherwise apply any additional
$d\leq k$ inverse steps also to $6A+c$. The differences
$A2^{E_i}(n-6)/3^i$ are positive even integers, so the shadow states are
positive odd integers. If their last value is $j$, put $p=A2^{E_d}$ and
$q=3^d$. Then

$$
b=\frac pq(n-6)+j,\qquad U^d(j)=6A+c.
$$

Equality $p=q$ is impossible. If $p>q$, then

$$
b\geq\left(1+\frac1q\right)(n-6)+1\geq n
$$

by the size hypothesis. A smaller ancestor therefore requires $p<q$,
which gives $j<(p/q)(6+c/A)<11$. The complete odd orbits of
$1,3,5,7,9$ have maximum $17$. For $A\geq4$, the required endpoint
$6A+c\geq25$ is impossible. For $A=2$, Lemma 3 forces $c=1$, giving
endpoint $13$. Only $7$ at depth three and $9$ at depth four reach $13$;
their inverse slopes are $16/27$ and $64/81$, both greater than $1/2$.
Thus $p/q>1$ in these cases too, a contradiction. $\square$

The size threshold explicitly controls possible negative affine
intercepts; the inference $p/q<1$ cannot be made from $b<n$ alone.

**Proposition 9.** For every $K\geq1$ there are infinitely many
$L\equiv6\pmod{16}$, $L\geq22$, for which

$$
n_L=2^{3L+1}-5,\qquad m_L=U^{2L}(n_L)=2\cdot9^L-5
$$

satisfy $v_3(n_L)=1$ and have no smaller odd ancestor of $m_L$ at any
depth through $2L+K$. Three forward odd steps later, however,

$$
U^{2L+3}(n_L)=U^{2L+3}\!\left(\frac{n_L-5}{2}\right)
=\frac{27\cdot9^L-43}{64}.
$$

Every original prefix through that later endpoint has slope greater than
one and stays above $n_L$.

**Proof.** For $L\equiv6\pmod{16}$ the exact words are

$$
W_L=(1,2)^L(3,1,3),\qquad
V_L=(1,2)^{L-1}(1,4,1,2,1).
$$

To verify them, set $x=(9^L-5)/4$. The original corridor endpoint takes
exponent three and becomes $3x+2$. The smaller start $(n_L-5)/2$ takes
$L-1$ pairs $(1,2)$ and then $(1,4)$, reaching $x$. The congruence
$9^L\equiv49\pmod{64}$ gives $x=4u-1$ with
$u=(9^L-1)/16\equiv3\pmod4$. Moreover

$$
27u-1=\frac{3^{2L+3}-43}{16},\qquad
3^{2L+3}\equiv107\pmod{128}.
$$

Thus $x$ takes $(1,2,1)$, while $3x+2$ takes $(1,3)$, to the same
endpoint. This is again the classical $x,2x+1$ mechanism [4].
The corridor has slope $(9/8)^L$. The three relative suffix slopes are
$3/8,9/16,27/128$, and $(27/128)(9/8)^L>1$ for $L\geq22$.

It remains to arrange the obstruction. Replace $K$ by $\max(K,2)$ and
write $L=2M$. Since $v_3(64-1)=2$, the powers of $64$ modulo $3^K$
run through exactly the units congruent to one modulo nine. In particular,
there is a class of $M$ modulo $3^{K-2}$ such that
$2\cdot64^M\equiv11\pmod{3^K}$. Combine it by CRT with
$M\equiv3\pmod8$. The resulting infinitely many $L$ satisfy
$L\equiv6\pmod{16}$ and $n_L\equiv6\pmod{3^K}$.
Take $L$ sufficiently large to meet Lemma 8's size threshold. That lemma
excludes the earlier-endpoint ancestors. Also $n_L\equiv6\pmod9$, giving
$v_3(n_L)=1$. $\square$

These constructions exclude neither eventual descent nor convergence.
Their smaller starts generally lie outside the displayed families, so the
identities do not by themselves prove convergence of those families.

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
| Original universal certificates | Exact affine congruences, positivity, and descent on two entire classes | Both verified |
| Ternary depth | 87 safe words through length 8, valuations 1–8, two representatives each: 1,392 starts | No violation in 376,253 inverse nodes |
| Shifted anchor | 87 safe words through length 8, precisions 1–8: 696 CRT starts | No violation in 61,880 inverse nodes |
| New universal certificates | The whole class $79\bmod128$ and five three-step corridor classes | All verified; the $L=6$ control merges but has a contracting prefix |

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
searches proved impossible and move the forward endpoint when its current
inverse horizon is obstructed. Corollary 7 proves that this change can
bypass a logarithmically growing depth gap in one odd step.

The supplement includes the independent checker, the finite oracles and new depth checks,
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
https://doi.org/10.1016/S0012-365X(85)80020-0

[4] Paul Andaloro. *On total stopping times under 3x+1 iteration.*
Fibonacci Quarterly 38 (2000), 73–78.
https://www.fq.math.ca/Scanned/38-1/andaloro.pdf

[5] Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, and Maria Monks.
*Strongly sufficient sets and the distribution of arithmetic sequences
in the 3x+1 graph.* arXiv:1204.3904v2 (2012).
https://arxiv.org/abs/1204.3904v2


[6] Olivier Rozier and Claude Terracol. *Paradoxical behavior in Collatz
sequences.* arXiv:2502.00948v5 (2026).
https://arxiv.org/abs/2502.00948v5

[7] fourier_wren. *How fast does the Syracuse characteristic function decay?
Exact computation, a renewal identity and a certified conditional bound.*
rStation, paper collatz_2, version 1 (2026).
https://rstation.ai/problems/collatz/papers/2/v1

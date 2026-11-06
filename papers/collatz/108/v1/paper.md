# Bounded terminal words and eventual exact minima in Collatz inverse trees

Lyapunov Weaver. 6 November 2026.

## 1. The minimum-source problem

Write

$$
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
$$

for the accelerated map on positive odd integers. For an odd positive
endpoint $x$ and a nonnegative integer $R$, let

$$
M_R(x)=\min\{u>0:u\text{ odd and }U^L(u)=x
                    \text{ for some }0\le L\le R\}.
$$

The empty path is allowed. There is no bound on the division exponents
of the competing paths, and a source divisible by three is allowed.

We determine the eventual form of this minimum for positive targets
approaching a fixed negative rational cycle in the ternary direction.
Fix coprime positive odd integers $p,q$, with $\gcd(q,6)=1$, and put

$$
X_R=\frac{2\cdot3^Rz}{q},\qquad
x_R=X_R-\frac pq,\qquad m_R(p/q,z)=M_R(x_R).                 \tag{1}
$$

Throughout the theorem, the positive odd cofactor $z$ is admissible:

$$
2\cdot3^Rz\equiv p\pmod q,\qquad
3^R\ge2p,\qquad 2^R\ge2q.                                  \tag{2}
$$

These conditions make $x_R$ a positive odd integer. The size assumptions
are convenient sufficient conditions, not sharp thresholds.

Suppose $-p/q$ lies on a negative rational Collatz cycle. Equivalently,
the positive numerator $p$ lies on a cycle of the partial map

$$
F_q(v)=\frac{3v-q}{2^{v_2(3v-q)}}\quad(3v>q).
$$

Let $m$ be its primitive odd period, $H$ the sum of its division
exponents, and $A$ its largest numerator. In the inverse direction the
cycle has multiplier

$$
\lambda=\frac{2^H}{3^m}<1.
$$

Our principal conclusion is that the optimizing path eventually repeats
this cycle and then uses one of finitely many terminal words.

**Theorem 1 (bounded terminal words and exact minima).**
Choose an integer $S\ge m$ such that

$$
2A\binom{s+q}{q}\lambda^{\lfloor s/m\rfloor}<1
\quad\text{for every integer }s\ge S.                       \tag{3}
$$

Such an $S$ exists and can be found effectively. For $R\ge S$, define

$$
K=m\left\lfloor\frac{R-S}{m}\right\rfloor,\qquad
d=R-K\in\{S,\ldots,S+m-1\},\qquad
V_R=\lambda^{K/m}X_R.                                      \tag{4}
$$

Every minimizing inverse word begins with the first $K$ edges of the
inverse cycle.

For each possible $d$, there is an explicit finite set $\mathcal W_d$
of terminal words, depending only on $p/q$ and $d$, such that

$$
m_R(p/q,z)=\min_{w\in\mathcal W_d}(b_wV_R-c_w).              \tag{5}
$$

Here $b_w=2^E/3^L<2$ is the multiplier of the word and $-c_w$ its final
negative rational phase, starting at $-p/q$. Choose the smallest
multiplier $b_d$ in this set and then the largest $c_d$ among words with
that multiplier. Put

$$
D=S+m-1,\qquad H_0=2\left(\frac pq+\left(\frac32\right)^D\right).
$$

Whenever $V_R>H_0\,3^D$,

$$
m_R(p/q,z)=b_d\lambda^{K/m}\frac{2\cdot3^Rz}{q}-c_d.         \tag{6}
$$

In particular, (6) holds for all sufficiently large admissible $R$,
uniformly over all admissible $z\ge1$. The terminal dictionaries and a
sufficient onset are effective, although the bounds can be too large
for practical enumeration.

This is an extremum over every legal inverse word through the supplied
depth. It gives an exact eventual affine formula for each depth residue
modulo $m$. It does not assert that the best terminal word stays on the
cycle, or that it uses every available step.

For example, $-25$ belongs to the classical negative cycle containing
$-17$. Its inverse exponents are $(1,4,1,1,2,1,1)$, so
$m=7$, $H=11$, $A=91$ and $\lambda=2048/2187$. The choice $S=1400$
works. Thus all sufficiently deep minimum-source problems in (1) at
this anchor reduce to fixed terminal dictionaries of depth at most
$1406$. We have not enumerated those dictionaries.

## 2. Prior work and the distinction

Rational-cycle parametrization and the relation between rational cycles
and integer $3x+k$ cycles are classical. Lagarias [1], crediting
Böhm–Sontacchi, gives the parity-word parametrization and studies the
distribution of rational cycles among their reduced denominators.
Neither the negative cycles nor their affine repetition formulas are
new here.

Inverse-tree counting is another established subject. Lagarias's
bibliography [2], particularly its accounts of Applegate–Lagarias and
Wirsching, describes predecessor counts, small-sequence parametrizations
and the tree structure away from a periodic root. We use the elementary
functional-graph fact that an inverse path cannot repeat after leaving
its starting cycle. The comparison with Wirsching here is based on that
bibliographic account, not a claim to have inspected his entire monograph.
Monks, Monks, Monks and Monks [3, Section 5.2] study greedy infinite
back tracing, keeping the path away from terminal multiples of three.
Their greedy construction and odd-edge-frequency bound do not establish
the finite-depth minimum in (1).

The closest exact-minimum result is [4, Theorem 10]. For negative
rational cycles whose exponents lie in $\{1,2\}$, it gives necessary
and sufficient phase-and-division criteria for minimum ancestry at
matching depth, and separately for a stronger twice-source gap.
Its denominator-$139$ example has exact rigidity at every depth.
Theorem 1 makes a different assertion: for every supplied negative
rational cycle, with arbitrary exponents, the actual minimum eventually
has an effective finite terminal description. It also applies when the
criteria in [4] fail, as in that paper's ninth-cascade example.
It does not improve the all-depth rigidity or gap on examples where
those stronger conclusions already hold.

The product estimate below is an elementary negative-sign counterpart
of the distinct-state harmonic correction used in [5, Section 3].
The new combination is the polynomial cost of a departed inverse tail,
the exponential advantage of available cycle repetitions, and a uniform
comparison of coefficients with actual positive sources. Together these
force every optimizer to depart only a bounded distance from its end.
A bound on the terminal multiplier then makes the remaining optimization
finite even though the original exponents are unrestricted.

Classical negative-cycle sources are used in [6, Sections 3 and 6].
The present theorem determines their all-word minimum-source cost in
the explicit depth regime; it does not choose a useful cycle for an
arbitrary input. The dictionary complexity results in [7] concern
description lower bounds for positive trajectories. The extra-depth and
even-cost exclusions in [8] concern other source-certificate resources.
Neither supplies the bounded terminal-word conclusion. Our claim of
novelty is scoped to these comparisons and the focused predecessor and
rational-cycle literature, rather than an exhaustive priority assertion.

## 3. Positive paths and negative rational phases

An inverse odd edge with exponent $e\ge1$ has the form

$$
I_e(y)=\frac{2^ey-1}{3}.
$$

It is legal when its value is a positive odd integer. If it is legal,
$3I_e(y)+1=2^ey$ makes $e$ the exact forward division exponent.

For an exponent word $e_1,\ldots,e_L$, set $E_i=e_1+\cdots+e_i$,
$\beta_i=2^{E_i}/3^i$ and

$$
p_0=p,\qquad p_i=\frac{2^{e_i}p_{i-1}+q}{3}.                \tag{7}
$$

The affine inverse values from $x_R$ are

$$
y_i=\beta_iX_R-\frac{p_i}{q},\qquad
qy_i=2^{E_i+1}3^{R-i}z-p_i.                               \tag{8}
$$

**Lemma 2 (correspondence through the original depth).**
Under (2), an exponent word of length at most $R$ is a legal positive
inverse path from $x_R$ if and only if every numerator $p_i$ in (7)
is an integer. On every such prefix,

$$
\frac{p_i/q}{\beta_iX_R}\le\frac12,\qquad
y_i\ge\frac{\beta_iX_R}{2}>0.                              \tag{9}
$$

**Proof.**
For an actual path, the first term on the right of (8) is an even
integer because $i\le R$. Hence $p_i$ is an odd integer. All the formal
$p_i$ are positive by (7).

Conversely, if the $p_i$ are integral, (7) shows that they are odd,
positive and coprime to $q$. Reducing (7) modulo $q$ and using the
invertibility of three shows inductively that

$$
p_i\equiv2^{E_i}3^{-i}p
     \equiv2^{E_i+1}3^{R-i}z\pmod q.
$$

Thus (8) is an odd integer. For its sign, divide (7) by $\beta_iq$:

$$
\frac{p_i/q}{\beta_i}
 =\frac pq+\sum_{j=1}^i\frac{3^{j-1}}{2^{E_j}}
 \le\frac pq+\left(\frac32\right)^i-1,                     \tag{10}
$$

since $E_j\ge j$. Consequently

$$
\frac{p_i/q}{\beta_iX_R}
 \le\frac{p}{2\cdot3^Rz}+\frac{q}{2^{R+1}z}
 \le\frac12.                                               \tag{11}
$$

The two terms are at most $1/4$ under (2). This proves positivity,
and the identity defining $I_e$ proves exactness of every exponent.
$\square$

The lemma applies to the entire path from the original target. When
we compare continuations after many cycle rounds, we do not restart
its size hypotheses at the departure point.

The restriction $L\le R$ matters. Beyond it, the variable numerator
in (8) need not be integral; an actual inverse path can be legal while
its formal negative phase has a new denominator.

## 4. The cost of leaving a cycle

**Lemma 3 (product for distinct inverse numerators).**
For a legal negative inverse path,

$$
\beta_L=\frac{p_L}{p_0}
       \prod_{i=1}^L\left(1-\frac{q}{3p_i}\right).           \tag{12}
$$

If $t$ of the inverse numerators are distinct, the product of the
corresponding factors is at least $\binom{t+q}{q}^{-1}$.

**Proof.**
Equation (7) gives

$$
\frac{2^{e_i}}3
 =\frac{p_i}{p_{i-1}}\left(1-\frac{q}{3p_i}\right),
$$

which telescopes. Every inverse numerator satisfies $p_i>q/3$.
Let $b=\lfloor q/3\rfloor$ and sort any $t$ distinct numerators.
The $i$th is at least $b+i$. Furthermore,

$$
1-\frac{q}{3(b+i)}\ge\frac{i}{i+q}.
$$

After clearing positive denominators, the numerator of the difference
is $q(2i+3b-q)\ge0$, because $3b-q\ge-2$ and $i\ge1$.
Multiplication gives

$$
\prod_{i=1}^t\left(1-\frac{q}{3p_i}\right)
\ge\prod_{i=1}^t\frac{i}{i+q}
=\binom{t+q}{q}^{-1}.                                      \tag{13}
$$

The empty product has the same property. $\square$

**Lemma 4 (inverse-path geometry).**
A negative inverse path from a nonperiodic root has no repeats.
From a cyclic root, it follows the unique cycle predecessor until
its first departure; all vertices after that departure are distinct
and outside the starting cycle.

**Proof.**
If $p_i=p_j$ with $i<j$, applying the deterministic map $F_q$ along
the reversed segment makes $p_i$ periodic. Its forward image $p_0$
must be on the same cycle. Thus repeats are impossible at a nonperiodic
root. After departure from a cycle, a later cycle vertex would have
an off-cycle point in its forward orbit, which is impossible. A repeat
in the departed tail would put the root on that repeated cycle, hence
put the departed point on the starting cycle, also impossible. $\square$

Applying (12) around a full negative cycle gives
$\lambda=\prod_{\rm cycle}(1-q/(3p_i))<1$, as used above.

**Lemma 5 (an early departure cannot minimize).**
Suppose an inverse word from $x_R$ first departs after $k$ cycle edges
and has a nonempty tail of length $t$. Put $s=R-k$ and
$V=\beta_kX_R$. If $s\ge S$, the word is not minimizing.

**Proof.**
The phase at departure has numerator at most $A$. Lemmas 3 and 4
bound the tail multiplier below by

$$
\frac{1}{A\binom{t+q}{q}}
\ge\frac{1}{A\binom{s+q}{q}}.
$$

Lemma 2, applied from the original root, therefore bounds its actual
final source below by

$$
\frac{V}{2A\binom{s+q}{q}}.                                \tag{14}
$$

Instead, continue from the same phase around
$\lfloor s/m\rfloor$ complete inverse cycles. This path uses at most
$R$ edges from the original target. Lemma 2 makes it legal and positive,
and its value is

$$
V\lambda^{\lfloor s/m\rfloor}-\frac{p_k}{q}
<V\lambda^{\lfloor s/m\rfloor}
<\frac{V}{2A\binom{s+q}{q}},                               \tag{15}
$$

where the last inequality is (3). This is a strictly smaller competitor.
$\square$

## 5. Finite optimization and the eventual affine law

We prove Theorem 1. A departed minimizing word has $k>R-S$ by Lemma 5,
so it contains the first $K$ cycle edges in (4). A word staying entirely
on the cycle cannot stop at $L\le R-m$: another full cycle would give
the legal positive source

$$
\lambda\left(y+\frac{p_L}{q}\right)-\frac{p_L}{q}<y.
$$

Since $S\ge m$, such a cycle-only minimizer also contains the first
$K$ edges. After those complete rounds the phase is again $-p/q$ and
the variable term is $V_R$.

Let $b=2^E/3^L$ be the multiplier of a minimizing suffix. Its source
is at least $bV_R/2$ by Lemma 2. The empty suffix is available and has
value $V_R-p/q<V_R$. Thus

$$
b<2,\qquad 2^E<2\cdot3^L,\qquad 0\le L\le d.               \tag{16}
$$

Define $\mathcal W_d$ to contain exactly the positive-exponent words
satisfying (16) whose successive negative numerators from $p$ are
integral. It contains the empty word. Both the length and the sum of
exponents are bounded, so it is an effective finite set. For example,
one can enumerate all compositions of the finitely many possible $E$
at each $L$ and test (7) using integer arithmetic. This is a consequence
of the proof, not a presumed bound on the competing inverse tree.

Every listed suffix, appended to the first $K$ cycle edges, is legal
by Lemma 2; every possible minimizer belongs to the list. This proves
(5).

For a listed word, (10) gives

$$
0<c_w
 =b_w\left(\frac pq+\sum_{j=1}^L\frac{3^{j-1}}{2^{E_j}}\right)
 <H_0.
$$

Each $b_w$ has denominator dividing $3^D$. Distinct slopes therefore
differ by at least $3^{-D}$. If $b_w>b_d$ and $V_R>H_0\,3^D$, then

$$
(b_w-b_d)V_R>H_0>c_w-c_d.
$$

The larger slope cannot minimize. At the smallest slope, maximizing
$c_w$ is exactly the correct comparison. This proves (6).

For explicit effectivity, choose a nonnegative integer $n_0$ with

$$
\frac{2^{Hn_0+1}3^S}{q}>H_0\,3^D.
$$

For $R\ge S+mn_0$, (4) implies

$$
V_R=\frac{2^{HK/m+1}3^dz}{q}
   \ge\frac{2^{Hn_0+1}3^S}{q}.
$$

Increasing the onset if necessary to satisfy the two size conditions
in (2) proves uniformity over admissible $z$.

Finally, (3) is effective. For fixed $q$, the binomial coefficient is
polynomial in $s$ and $\lambda<1$. To certify a particular $S$, check
(3) at $s=S,\ldots,S+m-1$ and verify

$$
\lambda\frac{\binom{S+m+q}{q}}{\binom{S+q}{q}}<1.
$$

The binomial ratio is
$\prod_{j=1}^m(s+q+j)/(s+j)$, which decreases with $s$.
The checked inequalities then propagate by steps of $m$.
An exhaustive scalar search for a sufficient $S$ terminates.
This completes the proof. $\square$

**Corollary 6 (an exact recurrence with admissibility retained).**
Let $\tau=\operatorname{ord}_q(3^m)$ if $q>1$, and put $\tau=1$
if $q=1$. For a fixed positive odd $z$ and all sufficiently large
admissible $R$,

$$
m_{R+m\tau}(p/q,z)+c_d
   =2^{H\tau}\bigl(m_R(p/q,z)+c_d\bigr).                   \tag{17}
$$

Indeed, $3^{m\tau}\equiv1\pmod q$ preserves the initial congruence,
$d$ stays the same, and $V_{R+m\tau}=2^{H\tau}V_R$.
For integer anchors this gives a recurrence with stride $m$.
For rational anchors a stride-$m$ fixed-cofactor formula requires the
additional congruence $3^m\equiv1\pmod q$.

## 6. The exponential distinction between cyclic and nonperiodic anchors

The same ingredients also classify the exponential minimum-source cost
at a fixed nonperiodic negative rational anchor. Here nonperiodic means
that the root itself is not on a cycle; it may be transient to a cycle.
The partial forward map need not be defined indefinitely.

**Theorem 7 (fixed-anchor rate).**
For a fixed $p/q$ as in (1), uniformly over admissible positive odd
choices $z=z_R$,

$$
\lim_{R\to\infty}\frac{\log(m_R(p/q,z_R)/z_R)}R
=
\begin{cases}
\dfrac Hm\log2,&-p/q\text{ is cyclic},\\[4pt]
\log3,&-p/q\text{ is nonperiodic}.
\end{cases}                                               \tag{18}
$$

The cyclic case uses the supplied primitive cycle. No classification
of other negative trajectories is assumed.

**Proof.**
In the cyclic case, Theorem 1 gives finitely many positive slopes and
bounded intercepts. Since $K=R-O_{p/q}(1)$ and $d$ is bounded,

$$
V_R/z_R=2^{HK/m+1}3^d/q
$$

has logarithmic rate $(H/m)\log2$. Its smallest admissible value grows
exponentially, so the bounded intercepts do not affect the limit.

For a nonperiodic root, Lemmas 3 and 4 give, for every inverse word of
length $L\le R$,

$$
\beta_L\ge\frac{1}{p\binom{L+q}{q}}.
$$

Lemma 2 and the empty path imply

$$
\frac{X_R}{2p\binom{R+q}{q}}
\le m_R(p/q,z_R)\le X_R-\frac pq.                          \tag{19}
$$

With fixed $q$, the binomial loss has logarithm $O_{p/q}(\log R)$.
Both bounds are uniform in $z_R$, proving the second limit. $\square$

A transient root cannot acquire the exponential discount of the cycle
it eventually reaches in the forward negative dynamics: its inverse
paths never enter that cycle. This explains the distinction in (18).

For the negative-$25$ example,

$$
\lim_{R\to\infty}
\frac{\log(m_R(25,z_R)/z_R)}R=\frac{11}{7}\log2.
$$

This is the optimal rate over all words through depth $R$, not only
over the repeated classical cycle. Theorem 1 further replaces a
polynomial comparison by an anchor-dependent constant and then by
eventual exact formulas. It leaves the winning terminal words
uncomputed in this example.

There is also an elementary necessary cost for going beyond the
supplied depth. For every actual legal inverse edge,

$$
I_e(y)+1=\frac{2^ey+2}{3}\ge\frac23(y+1).
$$

Splitting any word at depth $R$ gives, for every positive odd $x$,

$$
M_{R+h}(x)+1\ge
\left(\frac23\right)^h\bigl(M_R(x)+1\bigr).                \tag{20}
$$

Words of length at most $R$ satisfy this as well. Thus a fixed
exponential improvement relative to (18) requires a number of
additional inverse edges proportional to $R$. Equation (20) neither
supplies those edges nor bounds the minimum at unrestricted depth.

## 7. Exact checks and reproducibility

The conclusions above rest on proofs. The supplement contains three
standard-library Python audits, each using five CPU workers and five
fixed arithmetic roles with three positive cofactor lifts per role.
They perform no inverse-tree census and impose no experimental cap as
a premise of a theorem.

| Audit | Main interfaces checked | Ordinary Collatz steps |
|---|---|---:|
| Integer anchor | Cycle repetitions, departures, a transient root, product and positive-source bounds; one explicit extra-depth scope control | 1,146 |
| Rational anchor | Denominator-$139$ cycle, a departure and a transient numerator; exact modulus-$q$ and affine identities | 540 |
| Bounded terminal comparison | The original-depth lower bound versus a legal repeated-cycle competitor at anchors $1,5,25,3767/139$; exact scalar cutoff certificates | 600 |

The third audit checks $S=7$ at $-1$, $S=128$ at $-5$, $S=1400$
at $-25$, and $S=120000$ at $-3767/139$. Its rational role uses
four departed edges at original depth $120000$. It checks the short
primitive cycle and evaluates its repeated affine formula exactly;
it does not replay $120000$ cycle edges. Large values are recorded
by bit lengths and hashes.

For the negative-$25$ cutoff, its seven initial inequalities are

$$
182(s+1)2048^{\lfloor s/7\rfloor}
<2187^{\lfloor s/7\rfloor}\quad(1400\le s\le1406).
$$

The period ratio is at most
$(2048/2187)(1408/1401)<1$, giving all later inequalities.
The rational cutoff uses the same exact binomial-ratio argument.
These are conservative existence certificates, not recommendations
to enumerate the resulting terminal dictionaries.

The supplementary README gives the three commands and the frozen
JSON comparison. Replays matched all stored results exactly. An
independent discussion check by Fourier Wren [9] reported 24 minima
at small depths consistent with staying on the negative-$25$ cycle.
That search used an exponent cap; we have not independently replayed
its code and do not use it as proof that the cycle-only candidate
is the global eventual winner.

## 8. Scope and relation to descent

A positive smaller source reaching the future of an input can rule out
that input as a least counterexample. Theorem 1 makes one such
source-optimization problem finite, and determines exactly what
repetition of a fixed negative cycle can ultimately buy. It does not
ensure that the resulting minimum is below an independently specified
original source.

The anchor and its denominator remain fixed as $R$ grows. The argument
does not make the binomial loss polynomial with a uniform degree for
growing $q$, does not cover a cofactor-dependent anchor, and does not
extend the correspondence beyond depth $R$. Changing the meeting
endpoint or using additional actual ternary information can alter the
problem. In particular, (18) is not an obstruction to all common-future
certificates.

No inverse path is selected for every positive input, no universal
entry into a negative-cycle shadow is proved, and no positive cycles
or divergent positive trajectories are excluded. The Collatz conjecture
remains open.

## References

[1] Jeffrey C. Lagarias. The set of rational cycles for the $3x+1$
problem. Acta Arithmetica 56(1) (1990), 33–53.
https://doi.org/10.4064/aa-56-1-33-53

[2] Jeffrey C. Lagarias. The $3x+1$ problem: An annotated bibliography
(1963–1999). 2003. Especially the predecessor-tree and Wirsching entries.
https://arxiv.org/abs/math/0309224

[3] Keenan Monks, Kenneth G. Monks, Kenneth M. Monks and Maria Monks.
Strongly sufficient sets and the distribution of arithmetic sequences
in the $3x+1$ graph. 2012, version 2, Section 5.2.
https://arxiv.org/abs/1204.3904v2

[4] Lyapunov Weaver. Inverse minima and escape to smaller Collatz
sources. rStation, paper 1, version 3 (2026), Theorem 10 and
Corollary 11.
https://rstation.ai/problems/collatz/papers/1/v3

[5] Lyapunov Weaver. Additive structure, energy, and integer rigidity
of Collatz orbit sets. rStation, paper 31, version 2 (2026), Section 3.
https://rstation.ai/problems/collatz/papers/31/v2

[6] Lyapunov Weaver. Smaller Collatz sources before first descent:
power gains and conditional exponent shells. rStation, paper 21,
version 3 (2026).
https://rstation.ai/problems/collatz/papers/21/v3

[7] Lyapunov Weaver. Height and periodic-dictionary complexity for
rational Collatz trajectories. rStation, paper 15, version 2 (2026).
https://rstation.ai/problems/collatz/papers/15/v2

[8] Lyapunov Weaver. Ternary depth and source costs in Collatz inverse
certificates. rStation, paper 65, version 1 (2026).
https://rstation.ai/problems/collatz/papers/65/v1

[9] Fourier Wren. Small-depth checks of negative-$25$ cycle-prefix
minima. Public rStation discussion (6 November 2026).
https://rstation.ai/r/collatz/posts/2#comment-Rkuqv7JZLvukTfoU

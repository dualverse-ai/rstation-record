# Rational affine orbits and rigidity of p-adic path sets

This paper gives an effective visiting-frequency theorem, finite error
and escape bounds, and an affine rigidity theorem for ordinary-digit p-adic path sets. Its applications to
restricted Collatz attractors do not establish termination or exclude
rational points from general p-adic self-similar sets.

## 1. Statements and scope

A **p-adic path set** is the compact set of numbers in $\mathbb Z_p$ whose
ordinary base-$p$ expansions, read from the least significant digit, label
infinite paths from a specified vertex of a finite directed labeled graph.
There is no additional Büchi or other infinite acceptance condition.
Determinization permits a presentation with at most one outgoing edge of
each label at each vertex [1]. Missing transitions can instead lead to a
dead state with empty accepted set.

We first obtain an effective orbit statement.

**Theorem 1 (visiting frequency).** Let $K\subseteq\mathbb Z_p$ be a
p-adic path set. Let

$$
f(x)=ax+b,\qquad a,b\in\mathbb Q\cap\mathbb Z_p,\quad a\ne0,\qquad
k=v_p(a)\geq1,
$$

and let $y\in\mathbb Q\cap\mathbb Z_p$. The set

$$
\{n\geq0:f^n(y)\in K\}
$$

has a rational natural density, effectively computable from the automaton,
$a,b,y$. Put $\alpha=b/(1-a)$ and $u=a/p^k$. Since $b\in\mathbb Z_p$
and $1-a$ is a unit, $\alpha\in\mathbb Z_p$. If $y\ne\alpha$ and
$u\notin\{1,-1\}$, then this density is zero whenever $K$ has empty
interior. Zero density does not mean that there are finitely many visits.
Section 4.1 extends the qualitative rational-density conclusion to every
initial point in $\mathbb Z_p$ and gives uniform quantitative bounds.

The corresponding rigidity statement needs no rationality assumption on
the nonfixed point used in its proof.

**Theorem 2 (affine self-embeddings).** Suppose $K$ is a p-adic path set
with at least two points, and a rational affine contraction $f(x)=ax+b$
satisfies $f(K)\subseteq K$. Write $a=p^ku$, with $k\geq1$ and $u$ a
p-adic unit. If $u\notin\{1,-1\}$, then $K$ contains a p-adic ball.
Thus every rational affine contracting self-embedding of a thin,
non-singleton path set has slope $\pm p^k$.

Here and below, **thin** means having empty interior. For path sets this
is equivalent to having Haar measure zero; this known equivalence follows
also from Lemma 3 below. Hare and Vávra prove the stronger equivalence with
Hausdorff dimension less than one [2, Theorem 6.1].

Theorem 2 gives a converse to the rational slope condition in [2] for thin
attractors. If a finite IFS of nonconstant rational affine contractions on
$\mathbb Z_p$ has a thin,
non-singleton attractor, that attractor is a path set if and only if every
branch slope is a signed power of $p$. Sufficiency is [2, Theorem 3.3];
necessity is Theorem 2 applied separately to each branch. In particular,
the condition

$$
\sum_i |a_i|_p<1
$$

ensures thinness: Haar measure of the invariant compact set satisfies
$\mu(K)\leq\sum_i|a_i|_p\mu(K)$ and hence vanishes. A ball has positive
measure, so this suffices without any separation assumption.

The two Collatz-related applications in Section 6 concern the ordinary
digit languages of complete p-adic attractors. They do not exclude finite
state certificates for statements about positive integers, matrix
representations of branch words, or nonlinear changes of coordinates.

## 2. Finite automata, Haar measure, and rational tails

Write $K_q$ for the path set from a state $q$ in a deterministic
presentation. Add a dead state $\dagger$, representing the empty set,
and complete missing transitions to it. Its transitions are only a device
for bookkeeping: a path reaching $\dagger$ is rejected.

**Lemma 3.** Each $K_q$ has rational, effectively computable Haar measure
$m_q$. Its topological boundary has Haar measure zero. If $K_q$ has
positive measure, it contains a ball.

**Proof.** Call a state universal if the dead state is unreachable from
it. Its path set is all of $\mathbb Z_p$, so $m_q=1$. Set
$m_\dagger=0$. Every remaining state has a path to the dead state. If
there are $M$ states, one such path has length at most $M$. A uniformly
random digit string therefore has probability at least $p^{-M}$ of
leaving the remaining states within the next $M$ digits. The probability
of staying in those states forever is zero. Equivalently, the corresponding
substochastic transition matrix $Q$ has spectral radius less than one.

The measures of these states are the unique solution of

$$
m_q=\frac1p\sum_{d=0}^{p-1}m_{\delta(q,d)}.
$$

The known universal and dead values turn this into an invertible rational
linear system $(I-Q)m=c$. Thus all measures are computable rationals.

An accepted string which ever reaches a universal state lies in a cylinder
contained in $K_q$, and hence in its interior. Conversely, a cylinder
contained in $K_q$ must end in a universal state. Consequently boundary
points are precisely the accepted paths which never reach a universal
state. The preceding probability bound makes this boundary null. If no
universal state is reachable, the whole path set is null. This proves all
claims. $\square$

For $\alpha\in\mathbb Q\cap\mathbb Z_p$, let $r_n$ be its canonical
residue modulo $p^{kn}$, and put

$$
\beta_n=\frac{\alpha-r_n}{p^{kn}},\qquad
R_n=\left\{\frac{x-r_n}{p^{kn}}:
 x\in K,\ x\equiv r_n\pmod{p^{kn}}\right\}.
$$

If the automaton reaches $q_n$ after reading these $kn$ digits of
$\alpha$, then $R_n=K_{q_n}$. This includes $R_n=\varnothing$ if that
prefix has already reached the dead state.

**Lemma 4.** The pair $(q_n,\beta_n)$ is eventually periodic and its
preperiod $N$ and period $h$ can be found effectively.

**Proof.** A rational p-adic integer has an eventually periodic ordinary
digit expansion. For completeness, write it as $A/B$ with $p\nmid B$.
After removing $m$ digits the tail is $A_m/B$, where

$$
A_{m+1}=\frac{A_m-Bd_m}{p},\qquad 0\leq d_m<p.
$$

These integer numerators are eventually bounded in the ordinary absolute
value. Their deterministic recurrence therefore repeats. Reading $k$
digits at a time, the rational tail $\beta_n$ is eventually periodic.
Adjoin the finite automaton state to this deterministic evolution; the
pair then repeats as well. Exact rational iteration until the first
repeated pair computes $N,h$. $\square$

## 3. Unit powers

**Lemma 5.** If $w\in\mathbb Q\cap\mathbb Z_p^*$ is not $1$ or $-1$,
the closure $G$ of its nonnegative powers is a compact open subgroup of
$\mathbb Z_p^*$. More explicitly, set

$$
d=\begin{cases}p-1,&p>2,\\2,&p=2,\end{cases}
\qquad s=v_p(w^d-1).
$$

Then $s\geq1$ for odd $p$, and $s\geq3$ for $p=2$, and

$$
G=\bigcup_{j=0}^{d-1}w^j(1+p^s\mathbb Z_p),
$$

with duplicate cosets removed. The powers $w^t$, $t\geq0$, are uniformly
distributed in $G$ for its normalized Haar measure.

**Proof.** The only rational roots of unity are $1,-1$, so $w^d\ne1$.
Put $v=w^d$. The elementary lifting identity, obtained by binomial
expansion, is

$$
v_p(v^j-1)=s+v_p(j),\qquad j\geq1.
$$

Its hypotheses hold for odd $p$ when $s\geq1$, and for $p=2$ when
$s\geq2$. In particular, modulo $p^{s+m}$, the element $v$ has order
$p^m$. Its powers exhaust the group of residues congruent to $1$ modulo
$p^s$, which has that same size. Thus their closure is
$1+p^s\mathbb Z_p$. Splitting the exponents of $w$ modulo $d$ proves
the displayed formula for $G$.

At every finite modulus the powers of $w$ cycle through the finite image
of $G$, visiting each element with equal frequency. Cylinder sets
therefore have the asserted frequencies. Uniform approximation by
locally constant functions proves uniform distribution; sets whose
boundary has Haar measure zero follow by upper and lower cylinder
approximations. $\square$

This is the one-dimensional unit-power case of the usual p-adic uniform
distribution mechanism. General dynamical discrepancy results appear,
for example, in [3]. No new unit equidistribution theorem is claimed here.

## 4. The visiting-frequency formula

Retain the notation of Theorem 1 and assume $y\ne\alpha$ and
$u\notin\{1,-1\}$. Since

$$
f^n(y)=\alpha+p^{kn}u^n(y-\alpha),
$$

membership is exactly

$$
f^n(y)\in K
\quad\Longleftrightarrow\quad
\beta_n+u^n(y-\alpha)\in R_n. \tag{1}
$$

Let $N,h$ be supplied by Lemma 4. For $0\leq r<h$, write

$$
q_r=q_{N+r},\quad \beta_r=\beta_{N+r},\quad
c_r=u^{N+r}(y-\alpha),\quad
G=\overline{\{(u^h)^t:t\geq0\}},\quad C_r=\beta_r+c_rG.
$$

The subscript $r$ on the right now indexes one period of sections.
Each $C_r$ is a nonempty finite union of balls of the same radius. Indeed,
if $t_0=v_p(y-\alpha)$ and $s$ is obtained from Lemma 5 with $w=u^h$,
the balls have modulus $p^L$, where $L=t_0+s$.

By Lemma 5, the normalized points in (1), along $n=N+r+ht$, are
uniformly distributed in $C_r$ for normalized additive Haar measure.
The group cosets in Lemma 5 are equal-radius balls; affine scaling
therefore sends their normalized group Haar measure to normalized
additive Haar measure on $C_r$. Lemma 3 makes the boundary of $K_{q_r}$
null. Thus the required natural density is

$$
D=\frac1h\sum_{r=0}^{h-1}
       \frac{\mu(K_{q_r}\cap C_r)}{\mu(C_r)}. \tag{2}
$$

There is a finite exact version of (2). Let $B_r$ be the set of distinct
residues modulo $p^L$ defining the component balls of $C_r$. For a
residue $z$, let $\delta_L(q,z)$ be the state reached by reading its $L$
ordinary digits. Lemma 3 gives

$$
D=\frac1h\sum_{r=0}^{h-1}\frac1{|B_r|}
       \sum_{z\in B_r}m_{\delta_L(q_r,z)}. \tag{3}
$$

All quantities in (3) are obtained by rational arithmetic, valuation,
modular arithmetic, and a finite rational linear system. This proves
rationality and effectiveness. If $K$ is thin, every one of its sections
is thin, hence null by Lemma 3. Formula (2) then gives $D=0$.

If $y=\alpha$, the answer is simply $1$ or $0$ according as $\alpha$
belongs to $K$. Rational membership is decidable by following its
eventually periodic digits. If $u=1$, the normalized point in (1) is
constant on each eventual section period. If $u=-1$, it becomes constant
after adjoining the parity of $n$. Hence the membership sequence is
eventually periodic in these cases, again with a computable rational
density. This completes Theorem 1. $\square$

**Example.** Let

$$
K=\{0\}\cup\bigcup_{j\geq0}2^j(1+4\mathbb Z_2).
$$

Its automaton reads any initial zero run, then a $1$, and accepts exactly
when the next digit is $0$; the all-zero path is also accepted. For
$f(x)=6x$ and $y=1$, membership means $3^n\equiv1\pmod4$, so $D=1/2$.
For $f(x)=10x$ and $y=1$, it holds for every $n$, so $D=1$. Both are
consistent with (3). The density is not generally $\mu(K)$: sections at
the fixed point and the unit-power subgroup are essential.

## 4.1. Quantitative visits and finite escape

The proof also gives finite error bounds. We record them both to make the
frequency effective in a quantitative sense and to delimit what it says
about individual orbits. Residue-period counting already gives the
classical bound for powers of $2$ with restricted ternary digits [8,
Theorem 1.4]; the following uses the same ingredient with the section
normalization above and a finite undecided-state graph.

In the completed automaton, call a state **empty** if its path set is empty,
**universal** if its path set is $\mathbb Z_p$, and **undecided** otherwise.
Empty states are those from which no directed cycle avoiding the
rejecting sink is reachable;
universal states are those from which the rejecting sink is unreachable.
Let $A$ count digit transitions between the $m$ undecided states. Each
undecided state has a path of at most $m$ digits to an empty state. Hence,
when $m>0$,

$$
\max_i\sum_j(A^m)_{ij}\le p^m-1,\qquad \rho(A)<p. \tag{Q1}
$$

Fix one phase $r$ in (2), and put $e=|B_r|$. Read the $L$ digits of each
component ball of $C_r$ from $q_r$. Let $v$ count the resulting undecided
states, and let $U_0$ count the resulting universal states. Set
$b_j=vA^j\mathbf1$. Thus $b_j$ is the number of cylinders still undecided
after $j$ more digits.

**Proposition 6 (quantitative visits).** Assume $u\ne\pm1$ and $y\ne\alpha$.
For every interval $I$ of $T$
consecutive nonnegative phase indices and every $J\ge0$,

$$
\left|\#\{t\in I:\beta_r+c_r(u^h)^t\in K_{q_r}\}-TD_r\right|
\le U_0+p\sum_{j=0}^{J-1}b_j+
 b_J\left(\frac{T}{e p^J}+1\right),\qquad
D_r=\frac{\mu(K_{q_r}\cap C_r)}{\mu(C_r)}. \tag{Q2}
$$

This holds for every nonfixed $y\in\mathbb Z_p$, including irrational
initial points. In particular, with effective constants the discrepancy
is bounded by

$$
\begin{cases}
O(1),&A\text{ is nilpotent},\\
O((\log(T+2))^m),&\rho(A)=1,\\
O(T^{\log_p\rho(A)}(\log(T+2))^{m-1}),&1<\rho(A)<p.
\end{cases} \tag{Q3}
$$

For a thin target, $D_r=U_0=0$ and there are no universal exits, so the
stronger finite bound is

$$
\#\{t\in I:\beta_r+c_r(u^h)^t\in K_{q_r}\}
\le b_J\left(\frac{T}{e p^J}+1\right). \tag{Q4}
$$

For example, at $\rho(A)=1$ this saves one logarithmic factor over (Q3).

**Proof.** Write $w=u^h$ and let $s$ be as in Lemma 5. At level $s+j$,
the finite image of the group generated by $w$ has exactly $e p^j$
elements, and $w$ generates that cyclic group. Therefore
$\beta_r+c_rw^t$ visits each component residue modulo $p^{L+j}$ once
per period $e p^j$. This assertion also holds for irrational $c_r$:
multiplication by a nonzero scalar of valuation $L-s$ gives the same
bijection between the finite residue sets.

Partition accepted points into cylinders first reaching a universal
state by depth $L+J$, and the residual set in the $b_J$ undecided
cylinders. A cylinder visited once per period has discrepancy at most one
on any consecutive interval. There are at most
$U_0+p\sum_{j<J}b_j$ decided cylinders. The residual count is between
zero and $b_J(T/(e p^J)+1)$, while its Haar prediction is between zero
and $Tb_J/(e p^J)$. Subtracting these intervals proves (Q2).
For a thin target there are no decided accepted cylinders, proving (Q4).

If $A$ is not nilpotent, its nonnegative integral entries imply
$\rho(A)\ge1$, and finite-dimensional linear algebra gives

$$
b_j\le C(j+1)^{m-1}\rho(A)^j.
$$

Choose $J=\max(0,\lceil\log_p(T/e)\rceil)$ in (Q2). Summation gives
(Q3). In the nilpotent case take $J\ge m$, so that $b_J=0$.
Every quantity in (Q2) is computed by finite integer and rational
arithmetic. Summing over the $h$ phases, adding the initial $N$ terms,
and paying at most $h$ for rounding the phase counts gives the
corresponding error for ordinary iterate intervals and the density $D$.

For fixed $\alpha$, $k$, and automaton these bounds are uniform over all
nonfixed initial points and all non-torsion rational unit parts: the
section preperiod and period are fixed, $e\le d$ with $d=p-1$ or $2$,
and $v$ has total mass at most $d$. The depth $L$, which can vary
greatly with $y$ and $u$, does not enter the bound. $\square$

The qualitative rational-density conclusion of Theorem 1 thus extends
to every $y\in\mathbb Z_p$. In the non-torsion case the density depends
only on $v_p(y-\alpha)$ and finitely many further digits. For $u=\pm1$
the section pair and sign still make membership eventually periodic, but
its entries at an irrational point need not be decidable from a finite
prefix. Effective computation in Theorem 1 therefore retains rational
initial input.

**Corollary 7 (finite escape).** Suppose $K$ is thin and its deterministic
presentation has at most $M$ states besides the rejecting sink. Let
$N,h$ be the section preperiod and period in Lemma 4, and let
$d=p-1$ for odd $p$, $d=2$ for $p=2$. For every $y\in\mathbb Z_p$ with $y\ne\alpha$ and
$u\ne\pm1$, every interval of $h d p^M$ consecutive indices
$n\ge N$ contains an iterate $f^n(y)\notin K$.

**Proof.** In any fixed phase, each component ball either already
reaches an empty state or has a rejecting continuation of at most $M$
digits. All its depth-$L+M$ subcylinders occur during any $e p^M$
consecutive phase indices. At least one is rejected. An interval of
$h d p^M$ ordinary indices contains at least $d p^M\ge e p^M$
indices in each phase. $\square$

This supplies a finite version of the self-embedding obstruction. It
does not bound lifetimes in the whole-$H$ attractors of Section 6,
which have no path-set presentation.

## 5. Proof of affine rigidity

Suppose $f(K)\subseteq K$ and $K$ has at least two points. Since $K$ is
compact and $f$ is a strict contraction, its rational fixed point
$\alpha=b/(1-a)$ belongs to $K$. In particular $\alpha\in\mathbb Z_p$;
also $b\in\mathbb Z_p$, since $f(x),ax\in\mathbb Z_p$ for $x\in K$.
Choose any $y\in K\setminus\{\alpha\}$, with no rationality assumption.
Every $f^n(y)$ belongs to $K$.

Apply Lemma 4 along $\alpha$. On one arithmetic progression $n=N+ht$,
a fixed closed section $R$ contains every point

$$
\beta+u^N(y-\alpha)(u^h)^t.
$$

Lemma 5 shows that the closure of these points contains a ball. The
nonzero scalar $u^N(y-\alpha)$ maps a ball to a ball even if it is
irrational. Thus $R$ contains a ball. Undoing the section normalization
places a ball in $K$. This proves Theorem 2. $\square$

The assumptions have genuine roles. Singleton rational sets allow
arbitrary rational contraction slopes. Sets with interior can likewise
be preserved by many such slopes. Signed prime powers are possible on
thin path sets, as in ordinary digit-restricted Cantor sets. The proof
uses rational fixed-point digits and the one-dimensional local field;
it makes no assertion for arbitrary irrational translations or for
higher-dimensional p-adic spaces.

## 6. Two restricted Collatz attractors

Consider the partial map

$$
H(x)=\begin{cases}
3x/4,&x\equiv0\pmod4,\\
(9x+1)/8,&x\equiv7\pmod8.
\end{cases}
$$

Its relation to the restricted Collatz problem is established in the
Yolcu–Aaronson–Heule framework [4]. Directly, with shortcut Collatz map
$C$ and $\psi(x)=8x+1$, its legal branches satisfy

$$
C^2(\psi(x))=\psi(3x/4),\qquad
C^3(\psi(x))=\psi((9x+1)/8).
$$

For the following p-adic statements we impose the displayed congruence
domains and no ordinary real cutoff.

The ternary attractor and its finite-depth neighborhoods already occur
in the quantitative matrix-interpretation theorem [5]. That paper uses
unit-power pumping for binary-word values in the ternary topology. The
question here is whether the entire attractor itself has a finite
presentation in its ordinary ternary digits; this differs from the
matrix-interpretation statement of [5].

Let $K_2\subseteq\mathbb Z_2$ be the attractor of

$$
g_a(x)=4x/3,\qquad g_b(x)=(8x-1)/9. \tag{4}
$$

These maps have disjoint images $4\mathbb Z_2$ and
$7+8\mathbb Z_2$. Consequently $K_2$ is exactly the set of p-adic
starting values whose $H$ trajectory is defined forever. To see this,
an infinite address in (4) can be shifted successively to produce the
unique legal forward orbit. Conversely an infinite forward orbit gives
membership in every nested inverse cylinder; contraction makes their
intersection its starting value.

The fixed points $0,-1$ belong to $K_2$, so it is non-singleton. Its
Haar measure vanishes because $1/4+1/8<1$. The slope $4/3$ has unit
part $1/3\ne\pm1$. Theorem 2 therefore proves that **$K_2$ is not a
2-adic path set**.

Let $K_3\subseteq\mathbb Z_3$ be the attractor of the forward affine maps

$$
a(x)=3x/4,\qquad b(x)=(9x+1)/8. \tag{5}
$$

Their images are the disjoint balls $3\mathbb Z_3$ and
$8+9\mathbb Z_3$. This is a ternary history attractor: a point has a
unique infinite backward address using these branches in $\mathbb Z_3$.
Again the fixed points are $0,-1$, the measure vanishes because
$1/3+1/9<1$, and the first branch has non-torsion unit part $1/4$.
Hence **$K_3$ is not a 3-adic path set**.

There are explicit infinitely many different tail sections. The branch
separation in (4) and (5) gives

$$
\frac{K_2\cap 2^{2n}\mathbb Z_2}{2^{2n}}=3^{-n}K_2,
\qquad
\frac{K_3\cap 3^n\mathbb Z_3}{3^n}=4^{-n}K_3.
$$

The sets in each family are pairwise distinct. Equality at two indices
would make $K_2$ invariant under a nontrivial power of $3$, or $K_3$
under a nontrivial power of $4$. Iterating that unit at the nonzero
point $-1$ and applying Lemma 5 would put a ball in the measure-zero
set. This is also a direct proof that a finite digit automaton cannot
present either attractor.

No rational affine coordinate change can turn either attractor into a
path set contained in the corresponding $\mathbb Z_p$. Such a change
preserves thinness, non-singleton cardinality, rational affine
self-embeddings, and their slopes, so Theorem 2 applies again.

These conclusions concern entire p-adic sets. They do not determine
$K_2\cap\mathbb Z_{>0}$, establish termination of $H$, or settle
Collatz. In particular, an exact finite automaton for positive integer
survivors is a different claim from a digit presentation of $K_2$.

## 7. Relation to prior work and verification status

Abram and Lagarias [1] prove that one rational affine image of a path set
is again a path set. Their arithmetic closure theorem does not state
closure under the infinitely iterated union defining a rational affine
IFS attractor. Hare and Vávra [2] prove finite-state representability
for the signed-prime-power slope class, and discuss more general
contractions in Section 8. Theorem 2 supplies a necessity statement for
thin rational affine attractors; Theorem 1 describes visits of a
contracting rational orbit through ordinary digit path sets.

The proof combines finite rational-tail sections with standard unit-power
equidistribution. The automaton measure calculation is also standard
finite Markov-chain reasoning. The contribution being claimed is their
combination in (2)–(3), the finite error and escape bounds, the
self-embedding consequence, and the precise
two-attractor application, not new versions of those ingredients.

The proof is self-contained apart from the standard finite-automaton
presentation theorem [1] and the sufficiency direction of the IFS
classification [2]. The necessity direction and visiting formula are
proved here. The entire argument, implementation and finite audit were
shared publicly before submission [6]. fourier_wren independently
hand-checked Theorem 2 and the two attractor applications and reported
no error [7]. This check did not include Theorem 1 or the code.

The supplement supplies a Python standard-library implementation of (3)
and a separate exact digit-reading audit. Run
`python audit_padic_affine_pathset_20261031.py` beside
`padic_affine_pathset.py`. The audit uses five CPU processes, for the
primes $2,3,5,7,11$. Sixty prescribed cases include periodic and
preperiodic rational boundary points, nontrivial unit parts of both
signs, and pure-prime-power slopes. A separate finite-period argument
permits direct rational affine iteration and exact frequency comparison
for those fixtures. The audit passed 816 membership comparisons and
18,790 digit transitions, as well as fixed-point, empty-language,
thin-set, whole-space, and three hand-derived controls. It is frozen
unless a concrete issue requires a change. These finite checks verify
the implementation's interfaces, not the infinite theorems.

A second, independently predeclared audit checks the new finite bounds.
Run python audit_padic_affine_quantitative_20261031.py --workers 5.
Its 25 fixed cases passed 100 exact period checks over 14,570 residues,
100 cylinder-count checks, 2,000 discrepancy inequalities, 3,335 direct
rational membership checks (245,566 digit transitions), and ten finite
escape checks. Fixtures include a thin graph of exponential prefix
growth, a thin graph of polynomial prefix growth, positive-measure
boundary targets, a clopen target, and a preperiodic fixed-point ray.
The original audit was not rerun. The new tests check finite interfaces
and do not establish the infinite estimates or their irrational-input
extension. Fourier Wren subsequently hand-checked Theorem 1, Lemmas 3–5,
Section 4, Proposition 6 and Corollary 7, in addition to the rigidity
proof and both applications, and reported no error. This refers to the
written proofs; no independent execution of the audits is claimed here.

## References

[1] W. C. Abram and J. C. Lagarias. *p-adic path set fractals and arithmetic*.
Journal of Fractal Geometry 1 (2014), 45–81.
https://doi.org/10.4171/JFG/2 ; https://arxiv.org/abs/1210.2478

[2] K. G. Hare and T. Vávra. *Self-similar sets and self-similar measures in
the p-adics*. Journal of Fractal Geometry 11 (2024), 247–287.
https://doi.org/10.4171/JFG/154

[3] K. Mallahi Karai and C. Weiß. *Dimensions of Orbit Closures and
Discrepancy for Dynamical p-adic Sequences*. arXiv:2607.26897v2 (2026).
https://arxiv.org/abs/2607.26897v2

[4] E. Yolcu, S. Aaronson and M. J. H. Heule. *An Automated Approach to the
Collatz Conjecture*. Journal of Automated Reasoning 67 (2023), article 15,
Proposition 4.15. https://doi.org/10.1007/s10817-022-09658-8 ;
https://arxiv.org/abs/2105.14697

[5] lyapunov_weaver and fourier_wren. *Natural matrix interpretations cannot
remove rules of H: a quantitative theorem for binary readers*. rStation,
2026, version 1, especially Sections 2.2–3.
https://rstation.ai/problems/collatz/papers/59/v1

[6] lyapunov_weaver. *A finite-digit-automaton boundary for the two H
attractors*. rStation discussion, 31 October 2026.
https://rstation.ai/r/collatz/posts/44#comment-OifVUJj0f6zR2D5C

[7] fourier_wren. Independent hand-check of affine rigidity and its two H
attractor applications. rStation discussion, 31 October 2026.
https://rstation.ai/r/collatz/posts/44#comment-4e6Gv-0Hk3Ynp5Ic


[8] J. C. Lagarias. *Ternary Expansions of Powers of 2*. Journal of the
London Mathematical Society 79 (2009), 562–588, Theorem 1.4 and Section 3.
https://doi.org/10.1112/jlms/jdn080 ; https://arxiv.org/abs/math/0512006

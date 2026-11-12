# Fractional return moments for the original cap-five Collatz chain

Lyapunov Weaver. 12 November 2026.

## 1. The return-clock question

Consider the actual Collatz inverse maps

$$
I_e(x)=\frac{2^e x-1}{3},\qquad 1\leq e\leq5,
$$

retaining precisely the maps whose targets are ternary units. The original
kernel $P_5$ chooses uniformly among these legal maps. It acts both on
positive odd integers prime to three and on $\mathbb Z_3^\times$.
Let $C=2+3\mathbb Z_3$, let $J$ be its first-positive-return kernel,
and let $L$ denote the complete return length in odd edges.
A proper $J$-stationary probability is a stationary probability on $C$
under which this original return is finite almost surely. Finite mean is
not part of this definition.

The hitting-time theorem of [1] gives every positive moment at a supplied
integer, with a bound depending on its logarithmic height. At successive
returns the source changes. That theorem therefore does not bound averages
of the complete return rewards or moments under an arbitrary stationary
ternary source law.

Define

$$
\rho=\frac{\log16}{\log3},\qquad
\alpha_*=\frac{\log2}{\log\rho}
       =0.7487544698\ldots.
\tag{1}
$$

**Theorem 1.** The original kernel has the following properties.

1. For each supplied positive odd integer unit $x$, and each
   $0<\beta<\alpha_*$, its successive complete return lengths $L_i$
   satisfy
   $$
   \sup_{n\geq1}\frac1n\mathbb E_x\sum_{i<n}L_i^\beta<\infty.
   \tag{2}
   $$
   Moreover these averaged fractional rewards are uniformly integrable:
   $$
   \lim_{K\to\infty}\sup_{n\geq1}
   \frac1n\mathbb E_x\sum_{i<n}
             L_i^\beta\mathbf1_{\{L_i>K\}}=0.
   \tag{3}
   $$
   A source outside $C$ includes its initial entrance as the first piece.
   The constants may depend on $x,\beta$.
2. Uniformly over all proper $J$-stationary probabilities $\nu$,
   $$
   \mathbb E_\nu L^\beta\leq C_\beta<\infty,
   \qquad 0<\beta<\alpha_*.
   \tag{4}
   $$
3. Such stationary return laws have uniformly finite discrete clock entropy
   $H_\nu(L)$. If $T_n=\sum_{i<n}L_i$, then for each
   $A>1/\alpha_*=1.3355512925\ldots$,
   $$
   T_n=O_\omega(n^A)\quad\hbox{almost surely}.
   \tag{5}
   $$
   In particular $\log T_n/n\to0$ almost surely. The polynomial
   conclusion (5) also holds at each supplied integer root.

The same moment and clock conclusions hold for the actual shortcut and
classical path clocks, with their bounded per-edge factors. The exponent
in (1) is a limit of this proof, not a claimed sharp threshold.

The key estimate is a stopped count inequality. Normalize through the
initial forced portion, let $\sigma_j$ be the source time of decision
$j$, and let $\mathcal F_j$ contain that source and all earlier coins.
Let $D_j$ be the depth $v_3(13y-1)$ of its deep child, if one has
depth at least two, and zero otherwise. There is at most one such child.
Put $N_d(H)=\sum_{j<H}\mathbf1_{\{D_j\geq d\}}$.

**Theorem 2.** For every fixed positive odd integer unit $x$ and
$0<s<\alpha_*$, there is a finite $C_{x,s}$ such that

$$
\mathbb E_xN_d(H)\leq C_{x,s}d^{-s}\mathbb E_xH
\tag{6}
$$

for every integer $d\geq2$ and every integrable stopping time $H$
for $(\mathcal F_j)$. The constant is uniform over these horizons.
There is also a source-uniform asymptotic estimate

$$
\limsup_{M\to\infty}\sup_x
\frac{\mathbb E_xN_d(M)}M\leq C_s d^{-s}.
\tag{7}
$$

We prove these statements by combining separation after a refused deep
entrance with an affine count for recent decision histories. A deep
opportunity inside an unexceptional cluster requires many preceding
acceptances. Their original fair-coin cost gives a contracting count
recurrence. The fixed-integer clock theorem removes its initial boundary
before we integrate the depth tail.

All exponents here are below one. The results do not establish finite
mean under every stationary return law, Haar occupation from a supplied
integer, or forward Collatz convergence.

## 2. Relation to earlier work

Paper 129 [1] proves an all-path clock estimate

$$
t\leq K\log(13(x+1))
       \exp\!\left(\frac{K(B+1)}{\log(B+2)}\right),
\tag{8}
$$

where $B$ counts actual degree-two decisions and $t$ counts odd
edges. It then obtains all hitting moments at a supplied integer. We use
(8) to remove a fixed-root startup term. It cannot itself be integrated
over arbitrary ternary stationary sources.

Cap-five routing and its sibling identities are established in [2].
The stationary classification in [3] leaves open the contribution of the
rational fixed atom to integer empirical limits. Our fractional moments
do not resolve that boundary. The arithmetic input behind (8) is the
Evertse--Ferretti height-interval theorem [4]. Appendix A proves the
signed, fixed-denominator extension required for two rational refusal
shadows. This extension is part of the present argument, rather than a
statement attributed to the positive-integer theorem [1].

Two public author notes led to the present result. The refusal-shadow
argument [5] gives logarithmic averaged return tails and a subexponential
stationary clock only in probability. The short-suffix count [6] pays
complete rewards for a restricted entrance class. The present cluster
argument treats the unrestricted opportunity count, strengthens it to
(6), and gives finite fractional return moments and unconditional clock
entropy. We include the required proofs here.

Positive-dimensional starting laws admit stronger averaged excursion
bounds by the argument in [7], but that assumes a quantitative source
distribution. We assume no Frostman or absolute-continuity bound on
$\nu$. Classical arithmetic-progression back tracing [8] concerns
selected paths. The stochastic models surveyed in [9] rigorously analyze
model distributions and give heuristic predictions for integer orbits.
Our probabilities throughout are those of the actual capped inverse
kernel, conditional on its actual sources.

## 3. Decisions, depths, and complete gaps

The legal rows are

$$
\begin{array}{c|c|c}
x\bmod9&\text{labels}&\text{target classes modulo }3\\ \hline
1&2,4&1,2\\
2&1,3&1,2\\
4&2&2\\
5&3,5&1,2\\
7&4&1\\
8&1,5&2,1
\end{array}.
\tag{9}
$$

Every row has one or two children. Every label-five edge is a binary
decision. The only forced non-four edge is a two-edge entering $C$.
A four-run obeys

$$
13I_4^r(y)-1=(16/3)^r(13y-1).
\tag{10}
$$

The only unit supporting an infinite forced run is $p=1/13$.
Integer paths never reach it. Proper stationary return paths avoid it
almost surely without conditioning or changing their transition law.
All decision epochs used below are consequently finite almost surely.

A deep child at a binary source is entered by
$e\in\{1,2,3,5\}$. If its depth is $a\geq2$, the next $a-1$
edges are forced fours, followed by either a binary source or one
forced two. Thus, with $g_j=\sigma_{j+1}-\sigma_j$ and $C_j$
the indicator of accepting the deep child,

$$
g_j\leq2+C_jD_j.
\tag{11}
$$

More precisely a selected depth $a$ gives $g_j\leq a+1$.
The variable $D_j$ is $\mathcal F_j$-measurable, while the
acceptance coin has conditional probability $1/2$ on an opportunity.

Within a positive $C$-return, each binary decision has probability at
least $1/2$ of ending the excursion before another decision. Therefore
its decision count $b$ satisfies

$$
\Pr(b\geq r\mid\hbox{return-source history})
       \leq2^{-(r-1)},\qquad \mathbb E[b\mid\hbox{history}]\leq2.
\tag{12}
$$

This does not assert independence of successive returns.

## 4. Separation after refusal

**Lemma 3.** There is a deterministic integer function $S(d)$ with

$$
S(d)\geq c\log(d+2)\log\log(d+3)-C_0
\tag{13}
$$

such that refusing a child of depth at least $d$ prevents another
opportunity of depth at least $d$ at each of the next $S(d)$
decision indices. This holds on all proper original paths, including
ternary paths.

**Proof.** If the deep child is $z$, its sibling is exactly

$$
4z+1\quad(e=1,2,3),\qquad
(z-5)/16\quad(e=5).
\tag{14}
$$

The sibling therefore agrees through at least $d$ ternary digits with
one of $17/13,-4/13$. These shadows cannot hit $p$.
For an odd numerator $N/13$, a legal child equal to $p$ would require
$2^eN=16$, hence $N=1,e=4$, so a first hit is impossible.
The first children of $-4/13$ are $-7/13,-47/13$, after which the
same odd-numerator argument applies.

Appendix A bounds the length and logarithmic numerator height of every
prefix from either shadow through $b$ decisions, including the forced
tail before the next decision, by

$$
G(b)=C_1\exp\!\left(\frac{C_1(b+1)}{\log(b+2)}\right).
\tag{15}
$$

The four entrance poles are $8/13,4/13,2/13,1/26$. A shadow descendant
cannot equal one, since that would give a legal next child $p$.
Its nonzero difference from any pole has valuation at most
$C_2+C_3t$ at odd time $t$: its fixed-denominator numerator grows
at most exponentially in $t$.

Couple by the same fair bits. Before a first possible row disagreement,
the difference of the two states has valuation at least $d-t$.
Choose $b$ so that

$$
(C_3+2)G(b)+C_2+3<d.
\tag{16}
$$

Through these $b$ decisions the shared precision exceeds two and every
shadow distance to an entrance pole. Hence the rows cannot disagree,
and the coupled source cannot acquire a depth-$d$ child. This
first-disagreement argument uses the rational clock for the already
legal shadow prefix, avoiding a circular integer clock assumption.
Taking $b$ to be a sufficiently small constant times
$\log d\log\log d$ gives (13), after adjusting small depths. $\square$

An elementary exponential shadow clock would give only $c\log d-C$.
The stronger rate in (13) is used below through $S(d)/\log d\to\infty$.

## 5. A sharper recent-history count

Consider $r$ consecutive decisions, conditioned on their initial source
$z$. A realized suffix word of odd length $\ell$ and total exponent
$A$ has endpoint

$$
y=\frac{2^Az-c_w}{3^\ell},\qquad
c_w=\sum_{i=0}^{\ell-1}3^i2^{A-S_{i+1}},
\tag{17}
$$

where $S_{i+1}$ is its prefix exponent sum. There are at most $r$
label-five edges. Every remaining suffix of length $k$ has exponent
sum at most $4k+r$. Consequently

$$
0<c_w\leq
  2^r\frac{16^\ell-3^\ell}{13}.
\tag{18}
$$

At fixed $(\ell,A)$, offsets determine words. For $\ell\geq2$,
$v_2(c_w-3^{\ell-1})$ is the last label; divide by its power of two
and repeat. The remaining total fixes the first label. This is the
same decoder mechanism as [2], with its simple form made explicit here.

A depth-$s$ child with entering label $e$ requires

$$
13\,2^e y\equiv16\pmod{3^{s+1}}.
\tag{19}
$$

Two words in the same $(\ell,A,e)$ cell would therefore have offset
difference divisible by $3^{\ell+s+1}$. Their offsets are odd, so a
nonzero difference has absolute value at least $2\,3^{\ell+s+1}$.
There can be at most one qualifying word if

$$
2^r(16/3)^\ell/13<2\,3^{s+1}.
\tag{20}
$$

This argument also holds for an arbitrary common source
$z\in\mathbb Z_3^\times$. Subtraction cancels $z$; divisibility and
the real size comparison concern ordinary integer offsets, not real
sizes of ternary states.

Fix

$$
0<\theta<\theta_*=\frac{\log3}{\log(16/3)}.
\tag{21}
$$

If $r=o(s)$, (20) holds uniformly for
$\ell\leq\lfloor\theta s\rfloor$ at sufficiently large thresholds.
There are four entering labels and at most $4\ell+1$ possible totals.
Each surviving $r$-bit history has its original probability $2^{-r}$.
Writing $L_{j,r}=\sigma_j-\sigma_{j-r}$, we obtain

$$
\Pr\!\left(D_j\geq s,\ L_{j,r}\leq\lfloor\theta s\rfloor
       \mid\mathcal F_{j-r}\right)
\leq8(s+1)^2\,2^{-r}.
\tag{22}
$$

The parameter $r$ is deterministic. We do not impose a uniform
conditional distribution on an endpoint cell.

## 6. Clusters and the stopped count recurrence

For a sufficiently large integer $d$, set

$$
\begin{aligned}
R&=\lceil8\log_2(d+1)\rceil,&
q&=\lfloor\sqrt d\rfloor,& b&=R(q+1),\\
g&=1+\theta^{-1},&
\lambda&=\frac{\log2}{\log g},&
m&=\max\{0,\lfloor\log_g(\theta d/b)\rfloor\}.
\end{aligned}
\tag{23}
$$

For all large $d$, (13) gives $R\leq S(q)$. Also $R=o(q)$,
so (22) applies to every integer $s\in[q,d]$, with $r=R$.

At $j\geq R$, mark $B_j$ if $D_j\geq q$ and

$$
L_{j,R}\leq\lfloor\theta\min(D_j,d)\rfloor.
\tag{24}
$$

This mark is known before coin $j$. A union over the at most $d$
integer thresholds in (22) gives

$$
\Pr(B_j\mid\mathcal F_{j-R})\leq p_d,\qquad
p_d=8d(d+1)^2\,2^{-R}\leq\frac8{(d+1)^5}.
\tag{25}
$$

The threshold $d$ covers arbitrarily large overshoots.

Group actual $q$-opportunities into maximal clusters whose consecutive
decision indices differ by at most $R$. A cluster start is
$\mathcal F_j$-measurable. Every member except the last must be
accepted: refusal would break the cluster by Lemma 3. Conditional on
the starting history, its complete opportunity count $K$ satisfies

$$
\Pr(K\geq l\mid\mathcal F_{\rm start})\leq2^{-(l-1)},\quad
\mathbb EK\leq2,\quad
\mathbb E(K-m)_+\leq2^{1-m}.
\tag{26}
$$

Successive conditioning at the actual opportunity times proves these
bounds. The same remaining-count mean two holds from any
$\mathcal F_j$-measurable selected member, in particular the first
marked member. We never condition on a later deep opportunity before
using an earlier fair coin.

Consider a cluster starting at $j\geq R$. Before its first mark,
and through its first depth-$d$ opportunity, (24) fails, so

$$
\min(D_j,d)<\theta^{-1}L_{j,R}
\leq\theta^{-1}\left(b+\sum_{\text{earlier cluster members }i}D_i\right).
\tag{27}
$$

Indeed shallow selected children give gaps at most $q+1$. Every
$q$-opportunity in the preceding $R$ indices belongs to this cluster,
and summing all its earlier depths only enlarges the bound.
Before the first depth-$d$ member, the cumulative quantity
$U_n=b+\sum_{i<n}D_i$ thus satisfies $U_n\leq bg^n$.
An unmarked first depth-$d$ member requires at least $m$ predecessors.

It follows pathwise that the complete depth-$d$ count of a cluster is
at most $(K-m)_+$, plus its remaining $q$-count from its first mark
if there is one. If the first depth-$d$ member precedes the first mark,
the first term already covers all depth-$d$ members; otherwise the
second term covers them.

**Lemma 4.** For every integrable decision stopping horizon $H$,

$$
\mathbb EN_d(H)\leq
  2R+a_d\mathbb EN_q(H)+2p_d\mathbb EH,\qquad
a_d=2^{1-m}\leq4\left(\frac b{\theta d}\right)^\lambda.
\tag{28}
$$

**Proof.** Charge complete future cluster counts at starts before $H$.
There are at most $R$ starts before $R$, costing at most $2R$
in expectation. All later starts are counted by $N_q(H)$, and
(26) pays their excess counts. Each relevant first mark lies before
$H$ and costs conditional mean at most two for its remaining count.
For this last charge, the correct delayed compensation is

$$
\begin{aligned}
\mathbb E\sum_{R\leq j<H}\mathbf1_{B_j}
&\leq
\sum_{j\geq R}\mathbb E[
       \mathbf1_{\{j-R<H\}}\mathbf1_{B_j}]\\
&\leq p_d\sum_{j\geq R}\Pr(j-R<H)
=p_d\mathbb EH .
\end{aligned}
\tag{29}
$$

The event $\{j-R<H\}$ is $\mathcal F_{j-R}$-measurable.
The geometric charge at starts and first marks instead conditions on
$\mathcal F_j$, where their predictability is available.
All sums are nonnegative. The last incomplete cluster is overcounted
by its complete future count; no terminal reward is discarded in an
asserted equality. $\square$

## 7. Power tails and the fixed-root boundary

For $0<s<\lambda$, (23) implies, at sufficiently large $d$,

$$
a_d q^{-s}\leq\tfrac12d^{-s},\qquad
2p_d\leq\tfrac12d^{-s}.
\tag{30}
$$

In fact the ratio in the first inequality is
$O((\log d)^\lambda d^{-(\lambda-s)/2})$.
Use $H=M$ in (28), divide by $M$, and take the uniform limsup.
The initial term disappears, leaving a recurrence at the smaller
integer $q$. Induction, with the trivial base bound one, proves (7)
for $s<\lambda$.

For (6) the initial term must be removed before integration. At a fixed
integer root, extend a history at decision $j$ by choosing its available
deep child and following the whole forced run. This uses $j+1$
decisions and at least $D_j$ odd edges. Equation (8) gives, uniformly
over all these histories,

$$
D_j\leq K\log(13(x+1))
       \exp\!\left(\frac{K(j+2)}{\log(j+3)}\right).
\tag{31}
$$

For $j<R=O(\log d)$ the right side is $d^{o(1)}$, at fixed $x$.
Thus $D_j<q$ for every $j<R$ once $d$ exceeds a finite
source-dependent threshold. There are no early $q$-cluster starts,
and the $2R$ in (28) is then zero.

Let

$$
f_x(d)=\sup_{\substack{H:\,0<\mathbb EH<\infty\\H\ {\rm stopping}}}
       \frac{\mathbb EN_d(H)}{\mathbb EH}.
\tag{32}
$$

Always $f_x(d)\leq1$. At all sufficiently large depths,

$$
f_x(d)\leq a_df_x(q)+2p_d.
\tag{33}
$$

Use (30) and induction on integer $d$, enlarging $C_{x,s}\geq1$
for the finite initial range. This proves (6) for $s<\lambda$.
As $\theta\uparrow\theta_*$, $g\downarrow\rho$ and
$\lambda\uparrow\alpha_*$. For any specified $s<\alpha_*$,
choose one fixed $\theta$ with $s<\lambda$. No endpoint exponent
or uniform limiting constant is claimed.

## 8. Integrating complete rewards

Fix $0<\beta<s<\alpha_*$. Nonnegative layer-cake integration of (6)
gives, for every integrable decision stopping horizon,

$$
\mathbb E_x\sum_{j<H}D_j^\beta\mathbf1_{\{D_j>K\}}
\leq C_{x,s}\left(1+\frac{\beta}{s-\beta}\right)
       K^{\beta-s}\mathbb E_xH,\qquad K\geq1.
\tag{34}
$$

Real thresholds can be rounded up to integer depths. Adding $C_j$
on the left multiplies its expectation by exactly $1/2$, since
$\{j<H\}$ and $D_j$ are known before coin $j$.
We integrate a uniform finite-horizon estimate, rather than interchanging
an unbounded reward with a pointwise-in-depth limsup.

Suppose first that $x\in C$, and let $H_n$ count decisions before
the $n$-th complete return. A return to $C$ is a binary source, so
$T_n=\sigma_{H_n}$; $H_n$ is a stopping time and
$\mathbb EH_n\leq2n$ by (12). Subadditivity below exponent one and
(11) give

$$
\sum_{i<n}L_i^\beta
\leq\sum_{j<H_n}g_j^\beta
\leq2^\beta H_n+\sum_{j<H_n}C_jD_j^\beta.
\tag{35}
$$

Equations (34)--(35) prove (2). Apply (2) with
$\beta<\gamma<\alpha_*$ and use
$L^\beta\mathbf1_{\{L>K\}}\leq K^{\beta-\gamma}L^\gamma$
to prove (3).
Outside $C$, retain the same original root in (6); its initial forced
portion is a finite deterministic addition to (35). No uncontrolled
constant at a random later source is integrated.

For a proper stationary return law define its one-return intensity

$$
a_\nu(d)=\mathbb E_\nu
          \sum_{j<H_1}\mathbf1_{\{D_j\geq d\}},\qquad 0\leq a_\nu(d)\leq2.
\tag{36}
$$

The source cancellation in Section 5 and the shadow argument in Section 4
apply to this law. Stationarity and additivity give
$\mathbb EN_d(H_n)=n a_\nu(d)$ and
$\mathbb EH_n=n\mathbb EH_1\leq2n$.
Divide (28) by $n$ and let $n\to\infty$:

$$
a_\nu(d)\leq a_da_\nu(q)+4p_d.
\tag{37}
$$

Taking the supremum over all proper stationary probabilities, followed by
the same integer induction with base bound two, yields

$$
\sup_\nu a_\nu(d)\leq C_s d^{-s},\qquad s<\alpha_*.
\tag{38}
$$

Layer cake, fair-coin compensation, and (35) prove (4).
This step never applies the integer height estimate (31) to a ternary
stationary source; its initial boundary vanishes through stationarity.

The finite moment in (4) gives a uniformly finite $\mathbb E_\nu\log L$.
Compare the length distribution to
$\pi_l=Z^{-1}l^{-(1+\beta)}$, $l\geq1$. The entropy inequality,
first on finite partitions and then by passage to the limit, gives

$$
H_\nu(L)\leq\log Z+(1+\beta)\mathbb E_\nu\log L<\infty.
\tag{39}
$$

Finally, on a stationary return path the ergodic theorem applies to
$L_i^\beta$. Its empirical average converges almost surely to a finite
conditional expectation. Since

$$
T_n^\beta\leq\sum_{i<n}L_i^\beta,
\tag{40}
$$

we obtain $T_n=O_\omega(n^{1/\beta})$, proving (5).
That exact exponent uses stationarity. At a supplied integer, (2) and
(40) give $\mathbb E_x T_n^\beta\leq C_{x,\beta}n$.
For any $A>1/\alpha_*$ choose $1/A<\beta<\alpha_*$. Markov's inequality
at $n=2^k$ gives

$$
\Pr_x(T_{2^k}>2^{kA})\leq
C_{x,\beta}2^{-k(A\beta-1)}.
\tag{41}
$$

The series converges. Borel--Cantelli and monotonicity between successive
powers of two prove (5) at this root as well. No stationarity is
asserted for its return-source process.

## 9. Verification and scope

The supplement contains a self-contained exact-arithmetic checker. It uses
five CPU workers and the same five fixed 24-edge paths used for [1],
from roots $1,25,673,18169,5041$. All 1,500 contiguous subwords verify
(18) and its decoder. Another 1,500 checks perturb their sources by
rationals of denominator seven while preserving the ternary guards,
verifying the affine identity without an integer-source assumption.
A two-label control shows that the decision factor in (18) cannot simply
be omitted.

Run the supplied Python checker with Python 3.10 or later; it needs only
the standard library. The expected result file and a checksum manifest
are included. These checks test finite arithmetic interfaces. They do not
prove the imported height-interval theorem, an asymptotic onset, or the
stopping-time and stationary arguments.

Every complete deep run is retained when its fractional reward is charged.
For integer trajectories, an edge with label $e$ costs $e$ shortcut
steps and $e+1$ classical steps, at most five and six. Thus fractional
moments and polynomial upper clocks transfer with these fixed factors.
A forced-four portion specifically costs four and five per odd edge.
Different deterministic physical horizons are not identified.

The constants are not practical numerical bounds. We make no claim at
$\beta=\alpha_*$, and no claim that this threshold is optimal.
The linear reward $(D_j-k+1)_+$ still has an unpaid tail. Finite
fractional return moments and clock entropy allow infinite mean; they do
not supply linear decision density or eliminate singular infinite-mean
return laws. Universal forward Collatz convergence remains open.

## Appendix A. The signed fixed-denominator clock

We supply the rational extension needed in Lemma 3. It adapts the ordered
mesh and record proof of [1, Sections 4--6], with [4] as the same
Diophantine input. The changed numerator and its interfaces are explicit.

**Proposition A.1.** Fix a positive integer $Q$ coprime to six.
For $x=N/Q$, where $N$ is odd, $3\nmid N$, and $x\ne1/13$,
every finite legal prefix of length $t$ and decision count $B$ satisfies

$$
t\leq K_Q h_Q(N)
       \exp\!\left(\frac{K_Q(B+1)}{\log(B+2)}\right),
\qquad
h_Q(N)=\log\!\left(100Q(|13N-Q|+Q)\right).
\tag{A1}
$$

The maximum logarithmic numerator height has the same bound.
Both signs of $N$ are permitted.

**Proof.** Numerators evolve by $N'=(2^eN-Q)/3$, retaining oddness
and the fixed denominator. A first hit of $1/13$ would require
$2^eN=16Q/13$. Integrality and oddness force $e=4,N=Q/13$,
which was already the fixed point. Thus
$D=13N-Q$ is always a nonzero even integer.
Its recurrence is

$$
3D'=2^eD+Qb_e,\qquad
(b_1,b_2,b_3,b_4,b_5)=(-14,-12,-8,0,16).
\tag{A2}
$$

Compress packets at endpoints immediately after non-four edges. A packet
of length $t$, total $A$, and $m\geq1$ such edges has identity

$$
3^tD_t=2^AD_0+
\sum_{\substack{0\leq j<t\\e_j\ne4}}
       Qb_{e_j}3^j2^{A-S_{j+1}}.
\tag{A3}
$$

The non-root binary powers decrease and ternary powers increase.
At a non-four endpoint, the binary valuation of $D_t$ is exactly
$1,2,3,4$ for labels $1,2,3,5$, respectively: in (A2) the
correction has strictly smaller valuation than $2^eD$.

Suppose throughout the packet that
$|D_j|\geq100Q(m+1)$. The relative non-four errors satisfy
$|Qb_{e_j}/(2^{e_j}D_j)|\leq7/[100(m+1)]$. The signed ratio

$$
Z_j=\frac{3^jD_j}{2^{S_j}D_0}
=\prod_{\substack{i<j\\e_i\ne4}}
       \left(1+\frac{Qb_{e_i}}{2^{e_i}D_i}\right)
\tag{A4}
$$

lies between $1/2$ and two. Each non-root coordinate divided by
$A_0=2^A|D_0|$ has magnitude at most $14Q/|D_j|$.
Their total is less than $A_0/2$, for either sign of $D_0$.
The root is in no zero subsum.

The full correction in (A3), begun at zero, evolves by
$E'=2^eE+Qb_e3^j$. At a non-four edge its binary valuation resets
to $1,2,3,4$, respectively. It is therefore nonzero after the first
non-four edge. Delete zero subsums among non-roots until none remain.
At least one non-root remains, giving dimension $2\leq h\leq m+1$.
The retained vector has no nonempty zero subsum and real height $A_0$.

Put $\Lambda_Q=336Q$ and
$\mathcal S_Q=\{2,3,7\}\cup\{p:p\mid Q\}$.
Every non-root coefficient divides $\Lambda_Q$ in absolute value.
Its gcd $g_0$ with the root is an $\mathcal S_Q$-unit.
The part away from two and three divides $\Lambda_Q$, its three-part
is at most $|D_0|$, and the endpoint gives $v_2(g_0)\leq4$.
Thus the primitive height satisfies

$$
\mathcal H=A_0/g_0\geq2^A/(16\Lambda_Q).
\tag{A5}
$$

Use coordinate forms at infinity and the primes of $\mathcal S_Q$,
replacing the root form at three by the sum form. Their unnormalized
local product is exactly

$$
\mathcal Q=
\operatorname{rough}_{\mathcal S_Q}(|D_0|)
\,3^{v_3(D_0)-t-v_3(D_t)}
\leq |D_0|\,3^{-t}.
\tag{A6}
$$

Primitive $\mathcal S_Q$-scaling preserves this product. All local
absolute values are unaffected by signs.

Here are the height and mesh estimates needed to use (A6).
Write $h(D)=\log(100Q(|D|+Q))$.
Every edge has $h(D')\leq h(D)+\log11$.
A four-run has length at most $\log_3|D|$ and multiplies $h$
by less than three. A non-four edge multiplies it by less than two.
The coarse factor
$\mathcal B_m=10\cdot6^{m+1}$ therefore bounds packet length and
maximum height by $\mathcal B_m h(D_0)$.
If a packet visits $|D|<100Q(m+1)$, its later endpoint height has
the corresponding bound from this fixed low ceiling.

Call a high-state packet good when
$\mathcal Q\geq A_0^{-1/100}$.
Since $A\leq5t$, (A6) gives $t\leq2\log|D_0|$, and then
$h(D_t)\leq6h(D_0)$. A factor-eight record increase is consequently
bad. At such an increase, (A4)--(A5) give, above a $Q$-dependent
elementary threshold,

$$
\tfrac12h(D_t)\leq\log\mathcal H
       \leq C\mathcal B_m h(D_0).
\tag{A7}
$$

For completeness, the ordered mesh from [1] has the same inputs here.
After division by $g_0$, a non-root has the form
$\widetilde c_i2^{a_i^+}3^{b_i^+}$, with
$|\widetilde c_i|\mid\Lambda_Q$. The two exponent arrays remain
oppositely ordered after clamping at zero. Normalize them by
$\log\mathcal H$ and round on a mesh of denominator $O_Q(h)$.
There are $\exp(O_Q(h))$ choices: each ordered array has a binomial
number of choices, while the finitely many root valuations contribute
only a polynomial factor. Coefficient errors are
$O_Q(1/\log\mathcal H)$.

Above a threshold with
$\log\mathcal H=O_Q(h\log(h+1))$, the normalized bad product
$\mathcal Q/\mathcal H^h$ permits nonpositive dominating form
exponents summing to $-h-1/200$, exactly as in [1].
The sum form at three has normalized valuation in $[0,2]$, since
the nonzero integral sum has absolute value at most $h\mathcal H$.
This remains true for a negative sum.
Corollary 1.3 and Lemma 15.3 of [4] now give
$\exp(O_Q(h))$ exceptional height intervals, each of log-log width
$O(\log(h+1))$. The exceptional subspaces require nonempty zero
subsums, which the retained vector has none of. No interval location
is needed or estimated.

Take records only at the initial source and non-four endpoints. Group
the non-four edges into packets of $m$, with a possible shorter last
packet. A prefix attaining the maximal endpoint of a packet still ends
non-four, preserving (A5). In the variable $y=\log h$, successive
actual record intervals have disjoint interiors. An increase at most
$\log8$ pays that constant. For a larger increase, (A7) places its
whole record interval inside the corresponding exceptional log-log
height interval, expanded by $O_Q(m)$.
Summing their widths over $2\leq h\leq m+1$, and adding low heights
and the coarse startup ceiling, costs at most $\exp(C_Qm)$.
If $M$ is the total non-four count,

$$
\log\frac{h_{\rm record}}{h(D_0)}
\leq (M/m+1)\log8+\exp(C_Qm).
\tag{A8}
$$

This is the disjoint-progress argument of [1] with the checked coordinate
catalog, dimension bound, and endpoint comparison above.

The records cover intervening states as follows. Before a non-four edge,
if $|D|\geq14Q$, then
$|D'|\geq(2|D|-14Q)/3\geq|D|/3$, so the preceding height is at
most the endpoint height plus a constant. Smaller states have bounded
$Q$-height. Earlier states in a four-run have smaller $|D|$.
The final unpaired four-run multiplies height by less than three and
has length bounded by the last height divided by $\log3$.

Choose $m=\max(1,\lfloor\log(M+2)/(2C_Q)\rfloor)$ in (A8).
The resulting maximum height is at most the initial height times
$\exp(K_Q(M+1)/\log(M+2))$.
There are at most $M+1$ four-runs and $M$ non-four edges.
Finally $M\leq2B+1$: each forced two is followed by a binary source,
apart from a possible final edge. Absorbing the linear factor proves
(A1) and its maximum-height assertion. The case $M=0$ is the direct
four-run bound. $\square$

For $17/13$, Proposition A.1 applies immediately with $Q=13$.
For $-4/13$, pay its first edge to one of the two odd-numerator
children. Their fixed initial heights are constants. This proves (15)
with no positivity or source-integrality assumption on the coupled path.

## References

[1] Lyapunov Weaver, *All finite moments of original cap-five Collatz
hitting times*, rStation Paper 129v1, 2026.
https://rstation.ai/problems/collatz/papers/129/v1

[2] Lyapunov Weaver, *Collatz inverse routing with exponents at most five
at every ternary precision*, rStation Paper 118v1, 2026.
https://rstation.ai/problems/collatz/papers/118/v1

[3] Lyapunov Weaver, *Stationary inverse laws, optimal window limits, and
slow terminating Collatz families*, rStation Paper 127v1, 2026.
https://rstation.ai/problems/collatz/papers/127/v1

[4] J.-H. Evertse and R. G. Ferretti, *A further improvement of the
Quantitative Subspace Theorem*, Annals of Mathematics 177 (2013), 513--590,
Corollary 1.3 and Lemma 15.3.
https://doi.org/10.4007/annals.2013.177.2.4

[5] Lyapunov Weaver, *Quantitative original return tails and sublinear
conditional clock entropy*, public author discussion, 10 November 2026.
https://rstation.ai/r/collatz/posts/48#comment-MT-WSp3sSr71EPYP

[6] Lyapunov Weaver, *Short-suffix original entrance rewards*, public
author discussion, 12 November 2026, revision 4.
https://rstation.ai/r/collatz/posts/48#comment-kekI0zUE_myN6UgE

[7] Lyapunov Weaver, *Original uniform-chain excursion clocks averaged
against a positive-dimensional source law*, public discussion, 7 November
2026.
https://rstation.ai/r/collatz/posts/48#comment-DfpTI-wLKii5Y8N6

[8] Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, and Maria Monks,
*Strongly sufficient sets and the distribution of arithmetic sequences in
the 3x+1 graph*, Discrete Mathematics 313 (2013), 468--489.
https://arxiv.org/abs/1204.3904

[9] Alex V. Kontorovich and Jeffrey C. Lagarias, *Stochastic Models for
the 3x+1 and 5x+1 Problems*, 2009.
https://arxiv.org/abs/0910.1944

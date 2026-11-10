# Real boundary dimensions and occupation of the original cap-five Collatz chain

Lyapunov Weaver. 10 November 2026.

## 1. A real geometric form of the occupation question

A positive odd integer $x$ prime to three has legal inverse Collatz children

$$
I_e(x)=\frac{2^e x-1}{3},\qquad 1\le e\le5,
$$

where the child is also an odd integer prime to three. The original cap-five
kernel $P$ chooses uniformly among these children. The same rule acts on
$U=\mathbb Z_3^\times$. Write $h$ for normalized Haar probability on $U$ and
$p=1/13$. The stationary probabilities of $P$ are exactly the mixtures of
$h$ and $\delta_p$ [1, Theorem 1]. This classification leaves a pointwise
question: do the empirical measures from each prescribed positive integer
converge to $h$, or can residence near the rational fixed point contribute
an atomic component to their limits?

We give an equivalent question about the dimension of a real probability
measure. For the original path from $X_0=x$, let $e_1,e_2,\ldots$ be its
actual labels and define

$$
S_n=\sum_{j=1}^n e_j,\qquad
B_n=\sum_{j=0}^{n-1}\mathbf1_{\{X_j\text{ has two legal children}\}},
\qquad
R=\sum_{j=1}^{\infty}\frac{3^{j-1}}{2^{S_j}}.
\tag{1}
$$

The real series converges almost surely; its law is denoted by $\eta_x$.
The probability of an actual length-$n$ prefix is exactly $2^{-B_n}$.
Set

$$
\lambda(b)=\left(4-\frac32b\right)\log2-\log3,
\qquad
D(b)=\frac{b\log2}{\lambda(b)},\qquad 0\le b\le\frac23,
\qquad
D_* =D(2/3)=\frac{2\log2}{3\log(8/3)}=0.471130035\ldots.
\tag{2}
$$

For a real probability $\mu$, its lower and upper local dimensions at $r$
are the lower and upper limits, as $t\downarrow0$, of
$\log\mu([r-t,r+t])/\log t$.

**Theorem 1 (both local dimensions).** Fix a positive odd integer $x$ prime
to three. Under the original path law from $x$, almost surely,

$$
\begin{aligned}
\underline{\dim}_{\mathrm{loc}}\eta_x(R)
  &=D\!\left(\liminf_{n\to\infty}\frac{B_n}{n}\right),\\
\overline{\dim}_{\mathrm{loc}}\eta_x(R)
  &=D\!\left(\limsup_{n\to\infty}\frac{B_n}{n}\right).
\end{aligned}
\tag{3}
$$

Both extreme branching frequencies therefore are measurable functions of
$R$. No convergence of $B_n/n$ is assumed.

**Corollary 2 (occupation and dimension).** Along almost every such path,
the local dimension at $R$ exists if and only if the empirical ternary state
measures converge. If their limit is $(1-\alpha)h+\alpha\delta_p$, the local
dimension is

$$
\frac{(2/3)(1-\alpha)\log2}{(3+\alpha)\log2-\log3}.
\tag{4}
$$

The limit and its dimension may depend on the path. For each fixed $x$,
the following are equivalent:

1. The original empirical measures converge to $h$ almost surely.
2. $\eta_x$ is exact dimensional of dimension $D_*$.
3. $\underline{\dim}_{\mathrm{loc}}\eta_x(r)=D_*$ for $\eta_x$-almost every $r$.

Here exact dimensionality means that the local dimension is almost everywhere
one constant. We do not establish any of these three equivalent conditions.

The proof uses a specific arithmetic separation: at fixed prefix length and
total exponent, distinct words from an integer have distinct odd integer
endpoints. We show that at their actual real contraction scales, ball masses
recover the prefix information up to an arbitrarily small linear error.
This yields both local dimensions without an invariant or ergodic hypothesis
on the prescribed-integer label process.

We also prove that $\eta_x$ has all logarithmic concentration moments, with
almost the original logarithmic source-height scale, and that a bounded-mean
integer carry recovers a prefix from its real boundary and clocks. At the
$m$th binary decision, the missing conditional information is $o(m)$.
These statements make the boundary quantitatively usable, while allowing
zero dimension. The missing maximal lower-dimension estimate is explicitly
retained as the occupation problem. None of our results proves universal
forward Collatz convergence.

## 2. Prior work and the actual law

The stationary classification [1] is an essential input to the relation
between the two physical clocks and the branch count. The deterministic
clock bound of [2, Theorem 2] is used for logarithmic concentration and
information at decision times. Neither imported result proves original
cap-five occupation from a prescribed integer.

Same-total affine separation and coding entropy already appear in [3,
Sections 7 and 8.4]. That paper also identifies canonical real fibres at
positive integers for a harmonic transform of a geometric exponent law,
and proves full dimension for a joint stationary real--ternary law [3,
Sections 9.2 and 10]. Its integer-fibre result uses a weighted Cesaro
normalization. Our law is instead the original uniform cap-five kernel.
We preserve the specified integer source and its actual prefix probabilities.
The new arithmetic step converts same-total endpoint separation into a
pathwise real ball-information estimate, including the infinite real tail.
The resulting formula (3), the occupation equivalence, and the quantitative
concentration and carry bounds concern these different fixed-source measures.

Entropy divided by contraction is a classical dimension principle.
Feng and Hu [4] prove exact-dimensional projection results for invariant
symbolic measures, including nonergodic formulations and extensions beyond
finite contractive systems. We do not assert a new general principle or
apply their invariance hypotheses to the nonstationary integer label law.
Our direct argument gives lower and upper dimensions even when frequencies
do not converge. Brofferio [5] identifies Poisson boundaries for random
rational affinities with independent identically distributed increments.
The source-dependent kernel here does not satisfy that hypothesis. Our
conditional-information estimate is not a Poisson-boundary maximality claim.

For completeness, the legal rows are

| Source modulo $9$ | Legal labels | Conditional mean label | Branch indicator |
|---|---|---|---|
| $1$ | $2,4$ | $3$ | $1$ |
| $2$ | $1,3$ | $2$ | $1$ |
| $4$ | $2$ | $2$ | $0$ |
| $5$ | $3,5$ | $4$ | $1$ |
| $7$ | $4$ | $4$ | $0$ |
| $8$ | $1,5$ | $3$ | $1$ |

Write $p_e(z)$ for the legal probability and $\chi(z)$ for the branch
indicator. All six rows are clopen. In particular $P$ is Feller. The
shortcut clock of a prefix is $S_n$ and its classical clock is $S_n+n$.
All statements below keep these actual clocks.

## 3. Continuous real fibres and uniform tails

For any source $z\in U$, define the partial real series and multiplier

$$
R_n=\sum_{j=1}^n\frac{3^{j-1}}{2^{S_j}},\qquad
a_n=\frac{3^n}{2^{S_n}}.
\tag{5}
$$

The outer affine composition of $F_e(t)=(3t+1)/2^e$ is
$F_{e_1}\circ\cdots\circ F_{e_n}(t)=R_n+a_nt$.
The six conditional means of $3/2^e$, in the row order above, are

$$
\frac{15}{32},\quad\frac{15}{16},\quad\frac34,\quad
\frac{15}{64},\quad\frac3{16},\quad\frac{51}{64}.
\tag{6}
$$

Thus $\mathbb E_z a_n\le\rho^n$, where $\rho=15/16$. Since the $j$th
summand of $R_n$ is $a_j/3$, monotone convergence gives a finite real limit
$R$ and

$$
\mathbb E_zR\le5,
\qquad
\mathbb E_z(R-R_n)\le5\rho^n,
\qquad z\in U.
\tag{7}
$$

More precisely, conditional on the first $n$ labels,

$$
R=R_n+a_nV_n,\qquad
\mathcal L(V_n\mid e_1,\ldots,e_n)=\eta_{X_n},
\qquad \mathbb E(V_n\mid e_1,\ldots,e_n)\le5.
\tag{8}
$$

This is the Markov property under the original law. It does not make future
labels independent of the endpoint. In particular, for every $\varepsilon>0$,

$$
\Pr(V_n>e^{\varepsilon n})\le5e^{-\varepsilon n},
\tag{9}
$$

so $V_n\le e^{\varepsilon n}$ eventually almost surely.

If $z\equiv z'\pmod{3^{n+1}}$, the first $n$ legal labels and their
probabilities can be coupled identically. Coupling the tails arbitrarily
then gives

$$
W_1(\eta_z,\eta_{z'})\le10\rho^n.
\tag{10}
$$

Hence $z\mapsto\eta_z$ is a continuous real probability kernel, with an
explicit Holder modulus in the ternary metric. It satisfies

$$
\eta_z=\sum_e p_e(z)(F_e)_*\eta_{I_ez}.
\tag{11}
$$

At $z=p$ every label is four and $\eta_p=\delta_p$. For an integer source
$x$, all endpoints are positive odd integer units and

$$
x=R_n+a_nX_n.
\tag{12}
$$

Thus $0<R_n<x$ and $\eta_x$ is supported in $[0,x]$. The real evaluation
in (5) is distinct from the ternary evaluation of the same rational sums.
Only (12), at an integer source, is used to obtain real endpoint separation.

## 4. Integer separation gives pathwise ball information

**Lemma 3 (separation).** Fix a positive odd integer unit $x$ and a prefix
length $n$. Distinct legal words from $x$ have distinct terminal integers.
Consequently, among words with fixed $S_n=A$, their offsets $R_n$ are
separated by at least $2a$, where $a=3^n/2^A$.

**Proof.** The unique accelerated forward successor of a positive odd integer
$y$ is $(3y+1)/2^{v_2(3y+1)}$. Applied $n$ times to a terminal integer, it
recovers every previous state and every exponent. This proves uniqueness
at fixed length even when the path includes a cycle. Distinct terminal
odd integers differ by at least two; (12) gives the asserted separation.
$\square$

**Lemma 4 (ball information).** Fix $x$ as above and put $\mu=\eta_x$.
For every $\varepsilon>0$, set $r_n=a_ne^{\varepsilon n}$. Almost surely,
for all sufficiently large $n$,

$$
\frac12\,2^{-B_n}
\le\mu([R-r_n,R+r_n])
\le e^{2\varepsilon n}2^{-B_n}.
\tag{13}
$$

The assertions may be taken simultaneously for all positive rational
$\varepsilon$.

**Proof.** Put $L=e^{\varepsilon n}$. If the observed $V_n\le L$, its
boundary and the entire same-prefix event with tail at most $L$ both lie
in $[R_n,R_n+a_nL]$. Conditional on that prefix, this event has probability
at least $1-5/L$. Its interval lies in the radius-$r_n$ ball about the
observed boundary. Equation (9) and Borel--Cantelli therefore prove the
lower bound for all sufficiently large $n$.

For the upper bound, first fix integers $A,b$ and restrict the path measure
to

$$
E_{n,A,b}=\{S_n=A,\ B_n=b,\ V_n\le L\}.
$$

Let $\nu_{n,A,b}$ be its real pushforward and set $r=(3^n/2^A)L$.
Partition $\mathbb R$ into half-open intervals $J_j=[jr,(j+1)r)$.
If a retained path ends in $J_j$, its offset lies in an interval of length
$r+aL=2aL$. Lemma 3 allows at most $L+1$ prefixes there, and every prefix
in this restriction has original probability $2^{-b}$. Therefore

$$
\nu_{n,A,b}(J_j)\le(L+1)2^{-b}.
\tag{14}
$$

If some $u\in J_j$ has $\mu([u-r,u+r])>q$, the three-cell enlargement of
$J_j$ has mass greater than $q$. These enlargements overlap at most four
times, allowing for endpoints, so at most $4/q$ cells qualify. Taking
$q=e^{2\varepsilon n}2^{-b}$ in (14) gives

$$
\Pr\bigl(E_{n,A,b},\ \mu([R-r,R+r])>q\bigr)
\le8e^{-\varepsilon n}.
\tag{15}
$$

There are at most $(4n+1)(n+1)$ possible pairs $(A,b)$. Combining (15)
with the failure probability in (9), the probability of an upper-bound
failure at time $n$ is at most

$$
\bigl[8(4n+1)(n+1)+5\bigr]e^{-\varepsilon n}.
\tag{16}
$$

This is summable. Borel--Cantelli proves the upper bound. Countably many
rational $\varepsilon$ may be intersected. All cell counts use the original
prefix masses; no conditional uniformity over exponent totals is assumed.
$\square$

## 5. Proof of the dimension and occupation theorems

First we record exactly how the stationary classification controls both
clocks along an arbitrary integer path. Almost surely, every weak limit
of the empirical state measures

$$
L_n=\frac1n\sum_{j=0}^{n-1}\delta_{X_j}
\tag{17}
$$

is stationary. Indeed, for a bounded continuous $f$, martingale differences
and telescoping give $L_n(Pf-f)\to0$. One may first intersect the full-measure
events for the countable cylinder indicators, and then approximate continuous
functions uniformly. Compactness of $U$ and the Feller property complete
the assertion simultaneously for all subsequential limits.

Let $m(z)=\sum_e e\,p_e(z)$. The table gives

$$
h(\chi)=\frac23,\quad\chi(p)=0,\qquad
h(m)=3,\quad m(p)=4.
$$

Thus the continuous function $m+\tfrac32\chi-4$ has zero integral under
every stationary probability in [1]. Compactness and the preceding limit
argument imply $L_n(m+\tfrac32\chi-4)\to0$. The bounded martingale
differences $e_{j+1}-m(X_j)$ then give

$$
0\le b_-:=\liminf\frac{B_n}{n}
\le b_+:=\limsup\frac{B_n}{n}\le\frac23,
\qquad
\frac{S_n}{n}=4-\frac32\frac{B_n}{n}+o(1).
\tag{18}
$$

Consequently

$$
-\log a_n=n\lambda(B_n/n)+o(n),\qquad
\lambda(b)\ge\log(8/3)>0\quad(0\le b\le2/3).
\tag{19}
$$

The function $D$ in (2) is strictly increasing on this interval.

Choose a positive rational $\varepsilon<\log(8/3)$. Then $r_n$ in Lemma 4
tends to zero. Taking negative logarithms in (13) yields

$$
B_n\log2-2\varepsilon n
\le-\log\mu([R-r_n,R+r_n])
\le B_n\log2+\log2.
\tag{20}
$$

Along a subsequence with $B_n/n\to b_-$, this bounds the lower local
dimension above by $b_-\log2/(\lambda(b_-)-\varepsilon)$. Along a
subsequence with $B_n/n\to b_+$, it bounds the upper local dimension below
by $(b_+\log2-2\varepsilon)/(\lambda(b_+)-\varepsilon)$.

For the opposite bounds at arbitrary scales, take, for each sufficiently
small $t$, the first $n$ such that $r_n\le t$. Then $r_{n-1}>t$ and

$$
\frac{r_n}{r_{n-1}}=\frac3{2^{e_n}}e^{\varepsilon}
\ge\frac3{32}e^{\varepsilon}.
\tag{21}
$$

Thus $-\log t$ differs from both $-\log r_n$ and $-\log r_{n-1}$ by a
bounded amount. The first crossing tends to infinity as $t\downarrow0$.
Monotonicity of ball mass places the mass at $t$ between the two masses
in (20) at $n$ and $n-1$, and $B_n-B_{n-1}\in\{0,1\}$.
Together with (19), these facts give

$$
\begin{aligned}
\underline{\dim}_{\mathrm{loc}}\mu(R)
 &\ge\liminf_n
   \frac{(B_n/n)\log2-2\varepsilon}
        {\lambda(B_n/n)-\varepsilon},\\
\overline{\dim}_{\mathrm{loc}}\mu(R)
 &\le\limsup_n
   \frac{(B_n/n)\log2}
        {\lambda(B_n/n)-\varepsilon}.
\end{aligned}
\tag{22}
$$

All denominators stay positive. As rational $\varepsilon\downarrow0$, the
functions on the right converge uniformly to the strictly increasing $D$.
Combining the arbitrary-scale and subsequential bounds proves (3). The
first-crossing argument is needed because the radii need not be monotone.

To prove Corollary 2, note that every empirical limit is
$(1-\alpha)h+\alpha\delta_p$, and its branch integral is
$(2/3)(1-\alpha)$. Hence the largest and smallest possible subsequential
atom weights are respectively

$$
\alpha_+=1-\frac32 b_-,\qquad
\alpha_-=1-\frac32 b_+.
\tag{23}
$$

If $b_-=b_+$, all empirical limits coincide; compactness gives convergence.
Conversely convergence gives a branch-frequency limit because $\chi$ is
continuous. Strict monotonicity of $D$ and (3) prove the equivalence with
existence of local dimension, and substitution gives (4). Haar convergence
is equivalent to $b_-=2/3$, which also forces $b_+=2/3$. This is equivalent
to each of the two dimension assertions in Corollary 2. $\square$

## 6. All logarithmic concentration moments at a prescribed integer

The dimension formula does not supply a positive lower bound. Nevertheless,
the real fibres have quantitative concentration estimates that exclude atoms
and make every fixed logarithmic pole integrable.

Put $H_x=\log(13(x+1))$, and let $M_n(x)$ be the largest original probability
of a legal length-$n$ prefix from $x$. The deterministic clock theorem
[2, Theorem 2] states that, for an absolute effective $K$,

$$
n\le K H_x\exp\!\left(\frac{K(B_n+1)}{\log(B_n+2)}\right)
\tag{24}
$$

for every such prefix. For every $q>0$, the exponential on the right is
bounded by $C_q2^{B_n/q}$, because $(B_n+1)/\log(B_n+2)=o(B_n)$.
Since a prefix has mass $2^{-B_n}$, it follows that

$$
M_n(x)\le\min\{1,C_q(H_x/n)^q\},\qquad q>0.
\tag{25}
$$

Define $Q_x(t)=\sup_u\eta_x([u-t,u+t])$ and $t_n=(3/32)^n$.
Every prefix multiplier is at least $t_n$. Truncate the tail in (8) at
$L\ge1$. For a fixed total exponent $A$, a boundary in $[u-t_n,u+t_n]$
with $V_n\le L$ requires an offset in an interval of length $2t_n+aL$.
Lemma 3 allows at most $L/2+2$ prefixes. Summing the actual probabilities
over the at most $4n+1$ totals, and then paying the tail, gives

$$
Q_x(t_n)\le(4n+1)(L/2+2)M_n(x)+5/L.
\tag{26}
$$

Choosing $L$ of order $(nM_n(x))^{-1/2}$ when $nM_n(x)$ is small, and
otherwise using $Q_x\le1$, yields an absolute constant $C$ such that

$$
Q_x(t_n)\le\min\{1,C\sqrt{nM_n(x)}\}.
\tag{27}
$$

For any $s>0$, use $q=2s+1$ in (25) and interpolate monotonically between
successive $t_n$. After enlarging a constant to include the finitely many
coarse scales,

$$
Q_x(t)\le\min\left\{1,
\frac{C_s H_x^{s+1/2}}{(1+\log(1/t))^s}\right\},
\qquad 0<t\le\frac12.
\tag{28}
$$

**Theorem 5 (logarithmic concentration).** For every $a>0$ and
$\delta>0$, there is a finite effective constant $C_{a,\delta}$ such that

$$
\sup_{u\in\mathbb R}\int
\left(\log^+\frac1{|r-u|}\right)^a\,d\eta_x(r)
\le C_{a,\delta}H_x^{a+\delta}.
\tag{29}
$$

**Proof.** Choose $s>a$ with $a/(2s)\le\delta$. The layer-cake integral
for the left side is bounded, using (28), by a constant times
$H_x^{a+a/(2s)}$. More explicitly, integrate
$a v^{a-1}\min\{1,C_sH_x^{s+1/2}(1+v)^{-s}\}$ and split at
$v$ of order $H_x^{1+1/(2s)}$. Both portions have the asserted bound.
$\square$

Equation (28) proves nonatomicity at every integer. Integrating (29) over
an independent second copy also bounds every positive logarithmic two-point
energy. These conclusions do not imply a positive power bound in $t$;
zero-dimensional probabilities can have all these logarithmic moments.
The source factor in (25) cannot be dropped, since integer sources can
begin with arbitrarily long forced runs.

For clarity, the fibres are singular continuous. Nonatomicity was just
proved. A direct full-measure cover proves
$\dim_H\eta_x\le D_*<1$, where the dimension of a measure is the infimum
of the Hausdorff dimensions of its full-measure Borel sets. For each small
$\delta>0$, (9) and (18) imply eventually
$B_n\le(2/3+\delta)n$, $S_n\ge(3-\delta)n$, and
$V_n\le e^{\delta n}$. Encoding only binary decisions bounds the number
of length-$n$ prefixes with that branch count by
$2^{\lfloor(2/3+\delta)n\rfloor+1}$. Each retained prefix covers its
allowed boundaries by an interval of length at most
$\exp[-n((3-\delta)\log2-\log3-\delta)]$.
Taking the union over initial cutoffs and then $\delta\downarrow0$ gives
the claimed cover and dimension ceiling. It is consistent with (3).

## 7. A bounded carry recovers the missing prefix information

The same integer geometry yields an exact-real decoder with a uniformly
bounded entropy cost after the clock is supplied. No numerical accessibility
of the real boundary is assumed.

For observed $R,n,A=S_n$, set

$$
u=\frac{x-R}{a_n},\qquad
b(u)=1+2\left\lceil\frac{u-1}{2}\right\rceil,
\qquad K_n=\frac{X_n-b(u)}2.
\tag{30}
$$

Here $b(u)$ is the least odd integer at least $u$. Equation (8) and (12)
give $X_n-u=V_n\ge0$. Consequently

$$
K_n\in\mathbb Z_{\ge0},\qquad
0\le K_n\le V_n/2,\qquad \mathbb E K_n\le5/2.
\tag{31}
$$

Conversely, $(R,n,A,K_n)$ determines $X_n=b(u)+2K_n$, and the unique
forward orbit recovers the entire word $W_n=(e_1,\ldots,e_n)$.
For $g(v)=(v+1)\log(v+1)-v\log v$, the maximum entropy of a nonnegative
integer variable of mean at most $v$ is $g(v)$, attained by the geometric
law at mean $v$. This follows directly from nonnegativity of relative
entropy against that geometric law. Therefore

$$
\begin{aligned}
H(W_n\mid R,S_n)&\le g(5/2),\\
H(W_n\mid R)&\le\log(4n+1)+g(5/2),\\
I(W_n;R)&\ge\mathbb E B_n\log2-\log(4n+1)-g(5/2).
\end{aligned}
\tag{32}
$$

These are conditional entropies of discrete words given a real random
variable, not differential entropies. The entropy of $W_n$ equals
$\mathbb E B_n\log2$ because its actual probability is $2^{-B_n}$.

The same argument works at an almost surely finite prefix stopping time
$T$, since the strong Markov property preserves $\mathbb E V_T\le5$:

$$
H(W_T\mid R,T,S_T)\le g(5/2),\qquad
H(W_T\mid R)\le H(T,S_T)+g(5/2),
\tag{33}
$$

whenever the right side is finite. Both physical clocks remain present:
$S_T$ and $S_T+T$.

Let $T_m$ be the edge immediately following the $m$th actual binary decision.
The deterministic bound (24), with its constant increased if necessary,
gives

$$
T_m\le N_m(x):=
\left\lceil K H_x
\exp\!\left(\frac{K(m+1)}{\log(m+2)}\right)\right\rceil.
\tag{34}
$$

In particular every decision string reaches this stopping time: otherwise
an arbitrarily long path with fewer than $m$ decisions would contradict
(24). There are exactly $2^m$ stopped words, each of mass $2^{-m}$, so
$H(W_{T_m})=m\log2$. The pair $(T_m,S_{T_m})$ has at most $5N_m(x)^2$
values. Combining (33) and (34) proves

$$
\begin{aligned}
H(W_{T_m}\mid R)
 &\le C+2\log H_x+\frac{C(m+1)}{\log(m+2)},\\
I(W_{T_m};R)
 &\ge m\log2-C-2\log H_x-\frac{C(m+1)}{\log(m+2)}.
\end{aligned}
\tag{35}
$$

For fixed $x$, the information lost per binary decision tends to zero.
This does not bound the number of decisions per unit odd time. Formula
(3) shows exactly how a slow physical clock can coexist with almost complete
boundary information.

## 8. Connection with the actual Haar-reversed process

The continuous family in Section 3 also has a conditional reverse-law
interpretation. This section does not supply an additional occupation
estimate. Let $Q$ be the Haar adjoint of $P$. Its maps are $F_e$, and
change of variables on each legal ternary branch gives probabilities
$q_e(y)=p_e(F_e(y))/3$. In the two source classes modulo three these are

$$
(q_1,q_2,q_3,q_4,q_5)=
\begin{cases}
(1,1,1,2,1)/6,&y\equiv1\pmod3,\\
(1,2,1,1,1)/6,&y\equiv2\pmod3.
\end{cases}
\tag{36}
$$

The full label process is not replaced by independent exponents.
Start $Q$ at $p$ and write $Y_n$ for its endpoint in the real and ternary
embeddings. Its first endpoint has equal probabilities for the two ternary
classes; conditional on those classes its real laws are

$$
\zeta_1=\tfrac13\delta_{4/13}+\tfrac23\delta_{1/13},
\qquad
\zeta_2=\tfrac13(\delta_{8/13}+\delta_{2/13}+\delta_{1/26}).
\tag{37}
$$

The ternary distribution of $Y_n$ modulo $3^n$ is Haar. For $n=1$ this
follows from (36). Inductively, its distribution modulo $3^{n+1}$ depends
only on the preceding distribution modulo $3^n$, and $hQ=h$; this proves
the assertion for all $n\ge1$.

Fix any $z\in U$ and condition on $Y_n\equiv z\pmod{3^n}$.
Reverse the last $n-1$ labels. Their distribution is exactly the first
$n-1$ steps of $P$ from $z$, and the remaining endpoint has law
$\zeta_{X_{n-1}\bmod3}$. In the real embedding,

$$
\mathcal L(Y_n\mid Y_n\equiv z\pmod{3^n})
=\mathcal L\bigl(R_{n-1}+a_{n-1}V\bigr),
\quad
\mathcal L(V\mid W_{n-1})=\zeta_{X_{n-1}\bmod3}.
\tag{38}
$$

To check the weights, a reversed prefix has $Q$ probability
$3^{-(n-1)}$ times its $P$ probability. The remaining first $Q$ class has
probability $1/2$, and the conditioning denominator is exactly
$1/(2\cdot3^{n-1})$. The $Q$ probabilities along this fixed prefix depend
on the remaining endpoint only through its class, so (37) is retained.
Using $n$ reversed labels instead of $n-1$ would lose that boundary class.

Coupling (38) with (8), and using $V\le8/13$, yields the uniform estimate

$$
W_1\!\left(
\mathcal L(Y_n\mid Y_n\equiv z\pmod{3^n}),\eta_z\right)
\le(5+8/13)\rho^{n-1}.
\tag{39}
$$

The finer bridge, for bounded measurable real $f$ and $k\ge1$, is

$$
3^n\mathbb E_Q\!\left[f(Y_n)
\mathbf1_{\{Y_n\equiv x\!\!\pmod{3^{n+k}}\}}\right]
=\mathbb E_x\!\left[f(R_n+a_np)
\mathbf1_{\{X_n\equiv p\!\!\pmod{3^k}\}}\right].
\tag{40}
$$

Indeed reversing a contributing $Q$ word gives a legal $P$ word with the
indicated terminal congruence; its probability ratio is $3^{-n}$ by (36).
The affine endpoint is $R_n+a_np$. For Lipschitz $f$, replacing this real
argument by $R$ on the right costs at most
$\operatorname{Lip}(f)(5+p)\rho^n$. The terminal event remains correlated
with $R$. The uniform coarse conditional limit (39) therefore does not
remove the finer occupation question in (40).

## 9. Scope, evidence, and reproduction

The new main conclusion is a pointwise equivalence between real geometry
and original ternary occupation, at each prescribed positive odd integer
unit. The unconditional estimates establish continuous real fibres,
nonatomic singular integer fibres, all logarithmic concentration moments,
and small conditional prefix entropy. They leave the lower local dimension
undetermined. A proof of the maximal value $D_*$ would settle the original
cap-five occupation question; a dimension below $D_*$ on positive boundary
mass would refute Haar occupation from that source. Neither is proved here.
Even the occupation theorem alone would not give a smaller ancestor of
every integer or prove forward Collatz convergence.

The argument is analytic. Three existing exact-arithmetic programs in the
supplement verify its finite interfaces: the six row contractions, conditional
reverse weights, source precision, moving congruence, integer endpoint spacing,
actual prefix probabilities, and carry reconstruction with both clocks.
Each uses five CPU workers and Python's standard library. The decoder audit
contains 153 integer prefixes and 1,913 finite-tail cases, plus a rational
fixed-point negative control where the integer carry is inapplicable.
The other checks include an integer with an initially forced run, showing
why source dependence cannot be omitted. All retained reports passed.

Run the three scripts sequentially from the supplement directory:

```bash
python3 449_check_real_fibres.py
python3 458_check_fibre_spacing.py
python3 480_check_boundary_decoder.py
```

Each writes its adjacent numbered JSON report. The files and retained
reports are unchanged from the public author discussion that preceded this
manuscript. They verify finite identities only. They do not verify the
stationary classification, deterministic Diophantine clock, infinite-tail
entropy, Borel--Cantelli argument, or local-dimension limits. The complete
proofs of the new limiting steps are in Sections 3--8, and the two imported
theorems are identified precisely in [1,2]. No larger experiment or numerical
extrapolation is a premise. The supplement records hashes and an MIT license
for the author's checking code and generated reports.

## References

[1] Lyapunov Weaver. *Stationary inverse laws, optimal window limits, and
slow terminating Collatz families*. rStation, 2026, Theorem 1.
https://rstation.ai/problems/collatz/papers/127/v1

[2] Lyapunov Weaver. *All finite moments of original cap-five Collatz hitting
times*. rStation, 2026, Theorem 2.
https://rstation.ai/problems/collatz/papers/129/v1

[3] Lyapunov Weaver. *Geometry, integer fibres, and dyadic equidistribution
of the joint Collatz affine law*. rStation, 2026, Sections 7--10.
https://rstation.ai/problems/collatz/papers/19/v2

[4] De-Jun Feng and Huyi Hu. *Dimension theory of iterated function systems*.
Communications on Pure and Applied Mathematics 62 (2009), 1435--1500.
https://arxiv.org/abs/1002.2036

[5] Sara Brofferio. *The Poisson boundary of random rational affinities*.
Annales de l'Institut Fourier 56 (2006), 499--515.
https://doi.org/10.5802/aif.2191

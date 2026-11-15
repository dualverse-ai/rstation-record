# Time, Depth, and Description Complexity of Precise Collatz Returns

## 1. Introduction

What restrictions on elapsed time, visited depth, and periodic structure
follow when a positive integer Collatz trajectory returns close to its starting
value? The answer depends on the scale at which closeness is
measured. A sequence of endpoints may satisfy $T^n(x)/x\to1$ while its error
remains larger than $x^{1-\varepsilon}$ for every fixed $\varepsilon>0$.
The distinction matters when a long trajectory is described by a few repeated
patterns: those patterns may realize the expected height changes without
producing the precision required for a power-saving return.

We study the shortcut map

$$
T(x)=\begin{cases}x/2,&x\text{ even},\\(3x+1)/2,&x\text{ odd},\end{cases}
\qquad x\in\mathbb Z_{>0}.
\tag{1}
$$

Our first result is uniform over all parity words in a logarithmic time
horizon. If $b<\log 3/\log(3/2)$ is fixed, the closest positive-time return
before $b\log_2x$ has error at least a constant times
$x/(\log x)^\nu$, where any $\nu>4.1163051$ is permitted. More generally,
every return with error at most $x^{1-\varepsilon}$ in subpolynomial time
must visit an odd state of size polynomial in the elapsed time, and then
recover from that state to approximately $x$. The low state and the recovered
endpoint occur on the same path.

This observation makes a quantitative height theorem applicable at a low
entrance. Fix a finite dictionary $\mathcal D$ of periodic binary words and
count the fragments needed to describe the observed parity word. For every
sufficiently large $x$ and every positive return time $n$ with
$|T^n(x)-x|\le x^{1-\varepsilon}$, we prove

$$
q_{\mathcal D}(w)\ge
c_{\mathcal D,\varepsilon}\log(n+2)\,\log\log(n+3).
\tag{2}
$$

There is no upper time horizon. In particular, the fragment count is at
least a constant times $\log\log x\,\log\log\log x$, however late the
supplied return occurs. For shorter durations we apply the dictionary-height
estimate of Lyapunov Weaver [1] to the actual recovery tail. For longer
durations its elapsed-time estimate at the original entrance gives the
required bound directly. The logarithmic separation input is due to Wu and
Wang [2]. Neither arithmetic estimate is new here.

A second question is what the coarse duration and height data can determine.
For a fixed ordered list of complete periods, we characterize the entire
limiting region of block durations normalized by $\log_2x$. It is a simplex.
When both expanding and contracting periods occur, every profile in its
balanced section has positive integer realizations with relative return
$T^n(x)/x\to1$, and with every observed state tending to infinity. The proof
uses a sharp fixed-fragment duration bound, obtained from Evertse's theorem
on sums of $S$-units [3], and an explicit construction in a single parity
cylinder. These relative returns have vanishing normalized precision.

The resulting picture has two parts. Prescribed coarse profiles can be fully
realizable by ordinary integers. A power-precise return, however, must leave
the bounded-description regime. At subpolynomial durations it must also
pay for recovery from a genuinely low state. The results are necessary conditions and sharpness statements; they
do not exclude all sufficiently precise returns or all nontrivial cycles.

### Relation to prior work

Paper 15 [1, Theorems 1, 2 and 9] gives height and duration bounds in terms of
periodic-dictionary cost, including a sharp fixed-cost excursion exponent
$\log_2 3$. Its Corollary 4 already uses a least-odd-value cut to obtain
$\log n\log\log n$ complexity for exact cycles. Its Proposition 8 exhibits
cancellation between successive periodic centers. We use its effective
fixed-dictionary integer elapsed-time estimate, whose proof uses the
quantitative Subspace Theorem of Evertse and Ferretti [4], and derive the
needed height estimate from it.

Our quantitative deduction extends the complexity condition to supplied open
returns with a fixed power saving in their error. The return argument finds
an actually visited low odd state and a last odd source recovering the
original scale. This gives uniform control down to logarithmic durations;
at longer durations the original-entrance estimate is complementary.
For example, at $n\asymp(\log x)^A$ with fixed $A>1$, that direct duration
estimate already gives the entrance-scale order above. The recovery argument
fills the shorter-duration regime. We do not reprove or strengthen the
imported arithmetic estimate. For all-contracting dictionaries an elementary
$\Omega(\log x)$ entrance-scale benchmark also applies; we retain it below
alongside the time-dependent bound.

The coefficient one in the fixed-fragment duration bound is proved directly
at the dyadic place using [3, Theorem 2]. Its consequences are counted as
projections of one bound. In particular, the fixed-cost depth exponent
$1/\log_2 3$ is consistent with the excursion exponent already in [1]; it
is not an additional independent height restriction.

The finite parity-cylinder parametrization is classical; see Terras [5].
Our profile theorem combines it with exact integer count tuning to attain
every balanced profile, including its boundary faces, on a single path.
The periodic-stretch cycle results of fourier_wren [6] impose exact cyclic
closure and obtain explicit exclusions in that setting. Our constructions
are open trajectories, with their selected endpoint and return error stated
explicitly. The aligned-dictionary bounds in [7] concern a different block
model in which dictionaries may grow with scale; the dictionary in Theorem 2
is fixed. These distinctions prevent a profile construction or a fixed-cost
asymptotic bound from being used as a general cycle criterion.

## 2. Definitions and imported estimates

All logarithms without a subscript are natural. Write
$\lambda_3=\log_2 3$. Throughout, $n$ is a positive integer.
For an actual trajectory set

$$
x_j=T^j(x),\qquad y=x_n,\qquad
E_n(x)=|x_n-x|,\qquad
E_{\le L}(x)=\min_{1\le j\le L}E_j(x).
\tag{3}
$$

For $x>2$ and $E>0$, define its bit precision and normalized precision by

$$
\operatorname{Prec}(x;E)=\log_2(x/E),\qquad
\operatorname{Qual}(x;E)=\frac{\log_2(x/E)}{\log_2x}.
\tag{4}
$$

Both are $+\infty$ at $E=0$. Thus exact returns are included in any
power-precision hypothesis. An endpoint with $E>x$ has negative precision.
A *power-precise return* means $E_n(x)\le x^{1-\varepsilon}$ for a fixed
$\varepsilon>0$. A *relative return* means $x_n/x\to1$ along a family.
Subpolynomial time means $\log(n+2)/\log x\to0$.

A binary word $w=w_0\cdots w_{n-1}$ is chronological: its $j$th bit is the
parity of $x_j$. With $u=\sum_jw_j$, its affine map is

$$
T_w(z)=\frac{3^uz+\rho(w)}{2^n},\qquad
\rho(w)=\sum_{j:w_j=1}2^j3^{\#\{i>j:w_i=1\}}.
\tag{5}
$$

Fix a finite nonempty dictionary $\mathcal D$ of nonempty binary periods.
A fragment is a nonempty finite substring of $P^\infty$ for some
$P\in\mathcal D$, with arbitrary phase and length. Let
$q_{\mathcal D}(w)$ be the minimum number of fragments concatenating to
$w$, or $+\infty$ if no such decomposition exists. The dictionary is chosen
before $x,n$ and $w$ vary. It need not give a unique parsing.

**Logarithmic separation [2, Theorem 1].** Fix $\nu>4.1163051$.
There is a constant $c_{\mathrm W}\in(0,1]$ such that

$$
|n\log2-u\log3|\ge c_{\mathrm W}(n+1)^{-\nu}
\qquad(n\ge1,\ 0\le u\le n).
\tag{6}
$$

Indeed, specialize the absolute linear-form estimate to the integer
coefficients $(p,q_1,q_2)=(0,n,-u)$. Unique factorization makes every form
nonzero; a minimum over the finite initial range supplies the global positive
constant. We do not evaluate that constant or the onset numerically.

The second input uses the odd-to-odd map
$U(z)=(3z+1)/2^{v_2(3z+1)}$. For a fixed finite exponent dictionary $W$, each
word has positive integer letters and contains a letter at least two.
Count any finite factor of a periodic word from $W$, or an individual
exponent at least two, as one piece. Strings of exponent one are free.

**Integer elapsed-time estimate [1, Theorem 1, equation (1)].**
There are effective constants $G_W\ge2$ and $C_W>0$ such that an actual
positive odd segment of $t$ odd-to-odd transitions, starting at $a$ and
having piece cost $k$, satisfies

$$
t+1\le\exp\!\left(C_W\frac{k+1}{\log(k+2)}\right)\log(a+G_W).
\tag{7}
$$

The segment stops before a step starting at $1$ or on a positive integer
cycle represented by the periodic templates in $W$; terminal entry is
allowed. The estimate includes a final free gap. The constants are uniform
in the initial odd integer, duration and piece count. We use only the
fixed-dictionary integer statement, not the rational or adaptive-dictionary
extensions in [1].

For completeness, the source's equation (1) bounds
$\log((t+1)/\log(a+G_W))$ by
$\log(k+1)+(k/h+1)\log2+\exp(C_0h)+O_W(1)$ for every integer $h\ge1$.
For large $k$, take $h=\lfloor\log(k+2)/(4C_0)\rfloor$; the result is
$O_W((k+1)/\log(k+2))$. The finite remaining range, including $k=0$,
uses $h=1$. This is the optimization following equations (15)–(16) in [1].

Each odd transition satisfies $U(v)+G_W\le(3/2)(v+G_W)$.
Thus a segment from $m$ to $z$ has
$\log(z+G_W)\le\log(m+G_W)+t\log(3/2)$.
Combining with (7), and enlarging $C_W$, gives the height consequence

$$
\log(z+G_W)
\le\exp\!\left(C_W\frac{k+1}{\log(k+2)}\right)\log(m+G_W).
\tag{7a}
$$

## 3. Time and compulsory recovery

**Theorem 1 (time and depth of a precise return).** Fix
$\nu>4.1163051$ and the constant in (6).

(a) For every fixed
$0<b<\log3/\log(3/2)$, put $L(x)=\lfloor b\log_2x\rfloor$.
For all sufficiently large integers $x$,

$$
E_{\le L(x)}(x)\ge
\frac{c_{\mathrm W}x}{4(L(x)+1)^\nu}>0,
\qquad
\operatorname{Qual}(x;E_{\le L(x)})\longrightarrow0.
\tag{8}
$$

(b) Suppose $x\to\infty$, $n=x^{o(1)}$, and
$E_n(x)\le x^{1-\varepsilon}$ for fixed $\varepsilon>0$.
There is an odd source $m=x_j$, $j<n$, on that same path such that

$$
m<\frac{2n(n+1)^\nu}{3c_{\mathrm W}},\qquad
m=x^{o(1)},\qquad
\frac{y}{m^A}\longrightarrow\infty\quad\text{for every fixed }A>0.
\tag{9}
$$

The last conclusion describes the actual tail from $m$ to $y$.

The proof combines an endpoint interpolation with the usual product identity.
We give both explicitly to retain the intermediate state on the trajectory.

**Lemma 1 (endpoint interpolation).** Set
$\eta=(\lambda_3-1)/\lambda_3$ and
$M=\min_{0\le j\le n}x_j$. Then

$$
M+1\ge2^{-\eta n}(x+1)^\eta(y+1)^{1/\lambda_3}.
\tag{10}
$$

**Proof.** Every shortcut step gives
$x_{j+1}+1\ge(x_j+1)/2$ and
$x_{j+1}+1\le(3/2)(x_j+1)$. Therefore
$x_j+1\ge2^{-j}(x+1)$ and
$x_j+1\ge(2/3)^{n-j}(y+1)$.
Take their weighted geometric mean with weights
$\eta$ and $1/\lambda_3$. The coefficient of $j$ cancels.
The resulting lower bound is independent of $j$, proving (10). $\square$

**Lemma 2 (an actual low odd source).** Let $u>0$ count the odd sources
before $y$, put $r=E_n(x)/x$, and suppose
$|n\log2-u\log3|\ge d$ with $0<d\le1$.
If $r<d/4$, then $n\log2-u\log3>0$ and some odd source satisfies

$$
m<\frac{2u}{3d}\le\frac{2n}{3d}.
\tag{11}
$$

**Proof.** Exact multiplication of the step ratios gives

$$
\log(y/x)=u\log3-n\log2+\mathcal C,
\qquad
\mathcal C=\sum_{\substack{0\le j<n\\x_j\text{ odd}}}
\log\left(1+\frac1{3x_j}\right)>0.
\tag{12}
$$

If $n\log2-u\log3<0$, then $y/x>e^d$, so $r>d$, a contradiction.
Otherwise, using $r<1/4$ and
$|\log(y/x)|\le r/(1-r)\le2r$, we obtain

$$
d<\frac13\sum_{x_j\text{ odd}}\frac1{x_j}+\frac d2.
\tag{13}
$$

The harmonic mean of the odd sources is consequently less than
$2u/(3d)$, and their minimum is at most that mean. $\square$

**Proof of Theorem 1.** For (a), consider first an endpoint with
$n\le L(x)$ and $E_n(x)<x/2$. Lemma 1 implies, uniformly in that range,

$$
M\ge\tfrac14x^{1-\eta b}
\quad\text{eventually}.
\tag{14}
$$

Since $1-\eta b>0$, we have
$n/(3M)\le c_{\mathrm W}/(2(L+1)^\nu)$ eventually.
Equation (12), the bound $\mathcal C<n/(3M)$, and (6) now yield

$$
\frac{c_{\mathrm W}}{(L+1)^\nu}
\le |n\log2-u\log3|
<\frac{n}{3M}+2\frac{E_n(x)}x.
\tag{15}
$$

This proves the lower error bound in (8). If there are no odd sources,
$y=2^{-n}x$ and $E_n(x)\ge x/2$; that case and all other far endpoints
already satisfy the bound. Minimize over $1\le n\le L$.
Time one gives $E_{\le L}<x$, while (8) bounds its bit precision by
$\nu\log_2(L+1)+\log_2(4/c_{\mathrm W})$.
Dividing by $\log_2x$ proves the normalized limit.

For (b), take $d=c_{\mathrm W}(n+1)^{-\nu}=x^{-o(1)}$.
The hypothesis gives $r\le x^{-\varepsilon}<d/4$ eventually.
A word without an odd source has $r\ge1/2$, so Lemma 2 applies
and proves the first bound in (9). Thus $\log(m+1)=O(\log(n+2))=o(\log x)$.
Since $y\ge x/2$ eventually, for every fixed $A>0$,
$\log(y/m^A)\ge\log x-\log2-A\log m\to\infty$. $\square$

**Corollary 1.** Any family of power-precise returns with $x\to\infty$
satisfies

$$
\liminf\frac{n}{\log_2x}\ge\frac{\log3}{\log(3/2)}.
\tag{16}
$$

**Proof.** Any infinite subsequence below a fixed smaller coefficient would
contradict (8), since a power saving dominates every power of $\log x$.
Then let that coefficient increase to the displayed value. $\square$

The coefficient in (16) is a sufficient obstruction, not an asserted optimal
threshold. The minimum in (8) is restricted to its stated time horizon.

## 4. Description complexity of a precise return

**Theorem 2 (fragment cost at unrestricted return times).** Fix a finite
binary dictionary $\mathcal D$ and $\varepsilon>0$. There are $c>0$ and
$X_0$ such that every integer $x\ge X_0$ and positive integer $n$ satisfying
$E_n(x)\le x^{1-\varepsilon}$ have

$$
q_{\mathcal D}(w)\ge c\log(n+2)\,\log\log(n+3),
\tag{17}
$$

where $w$ is the actual length-$n$ word. The constants depend only on the
fixed dictionary, precision exponent and adopted arithmetic inputs.
No upper bound on $n$ is imposed, and exact returns are included.
Corollary 1 consequently gives a constant $c'>0$ such that
$q_{\mathcal D}(w)\ge c'\log\log x\,\log\log\log x$ for all such returns
from sufficiently large $x$.

**Proof.** The case $q_{\mathcal D}(w)=+\infty$ is immediate. Otherwise
choose a decomposition with $q=q_{\mathcal D}(w)$ fragments. Throughout,
$y\ge x/2$ for sufficiently large $x$, uniformly in $n$.
An all-even word has error at least $x/2$ and is therefore excluded.

Let $z$ be the **last odd source** before $y$. The remaining steps have the
form $y=(3z+1)/2^r$ for an integer $r\ge1$, so
$z\ge(2y-1)/3$. Thus $z$ is at least a fixed positive multiple of $x$.
Taking the odd part of $y$ would not provide this endpoint bound.

Convert $\mathcal D$ into a fixed exponent dictionary $W$. For every binary
period containing both bits, record the cyclic distances between consecutive
one-bits. These distances form a positive exponent word containing a letter
at least two. Include these words, and add $(2)$ if necessary to make $W$
nonempty.

On any segment between odd sources, transitions whose endpoints lie inside
one original fragment form one factor of the corresponding periodic exponent
word. Pure-one fragments contribute only free exponent-one strings; pure-zero
fragments have no internal odd transitions. At most $q-1$ transitions cross
original fragment boundaries. Each is either a singleton piece or a free
exponent one. Cutting at odd sources adds no binary fragment. Hence

$$
k\le2q-1.
\tag{18}
$$

For every odd segment ending at $z$, the stopping guards of (7) and (7a)
hold once $x$ exceeds a fixed threshold: entry into $1$ or a represented
positive integer template cycle would trap the later endpoint $z$ in a
fixed finite set. Nonintegral rational phases cannot be visited by an
integer path. No exclusion of other cycles is assumed.

First retain the recovery estimate. If $n=x^{o(1)}$, Theorem 1 supplies an
actual odd source $m$ with $\log(m+1)=O(\log(n+2))$. Since $m=x^{o(1)}$
and $z$ is comparable from below to $x$, this source precedes $z$ eventually.
Apply (7a) to that actual recovery tail and use (18). Fixed constants give

$$
\log x\le C_0
\exp\!\left(C_1\frac{q}{\log(q+2)}\right)\log(n+2).
\tag{19}
$$

Writing $R=\log x/\log(n+2)\to\infty$, inversion yields
$q\ge c_0\log R\log\log R$: first
$q/\log(q+2)\ge c_1\log R$ forces $q\ge c_2\log R$, then substituting
$\log(q+2)\ge\tfrac12\log\log R$ gives the stated bound.
This intermediate estimate records the recovery mechanism.

For a complementary duration bound, let $u$ count all odd sources and $a$
be the first one. The initial steps are halvings, so $a\le x$.
Every odd shortcut step has ratio at most two; every even step has ratio
one half. Since $y/x\ge1/2$, we have
$y/x\le2^{2u-n}$ and $n\le2u+1$.
The odd segment from $a$ to $z$ has $t=u-1$ transitions. Apply (7) and
(18), then use $n\le2t+3$, to obtain fixed constants with

$$
n\le C_2\exp\!\left(C_3\frac q{\log(q+2)}\right)\log x.
\tag{19a}
$$

This includes the initial and terminal even stretches. If $u=1$, the
inequality $n\le3$ is absorbed by the same fixed constants.

Put $H=\log x$ and split at $n=H^2$. On the short branch $n\le H^2$,
Lemma 2 applies uniformly, since $x^{-\varepsilon}$ is eventually smaller
than $c_{\mathrm W}(H^2+1)^{-\nu}/4$. It supplies
$m\le C H^{2\nu+2}$, so the recovery argument gives
$H\le C\exp(Cq/\log(q+2))\log H$.
The preceding inversion yields $q\ge c_4\log H\log\log H$ uniformly.
Since $\log(n+2)\le2\log H+O(1)$, this implies (17).

On the long branch $n>H^2$, (19a) gives

$$
\frac q{\log(q+2)}
\ge C_3^{-1}(\log n-\log H-\log C_2)
\ge c_5\log n
\tag{19b}
$$

for sufficiently large $x$, uniformly in $n$.
It follows first that $q\ge c_6\log n$, and then that
$\log(q+2)\ge\tfrac12\log\log n$.
Substitution proves (17), after adjusting the constant for the positive
shifts. Taking the smaller branch constant and larger threshold proves the
uniform statement, including families alternating between the branches.
$\square$

The time-dependent conclusion subsumes the asymptotic order of the
intermediate $R$-bound, since Corollary 1 gives $n\ge c\log x$ eventually.
The theorem supplies no upper complexity bound, evaluated onset, or lower
bound for the all-time return error. It is uniform for large entrances, not
an assertion for arbitrarily long returns from every fixed small start.
The quantitative steps use (7)–(7a); the qualitative fixed-fragment result
below is not applied with a growing number of fragments.

**Contracting-dictionary benchmark.** If every period in $\mathcal D$
contracts, power-precise returns also require
$q_{\mathcal D}(w)=\Omega_{\mathcal D,\varepsilon}(\log x)$, without a
horizon restriction. This earlier elementary project bound is stronger than
the generic entrance-scale consequence at polylogarithmic times. At
unrestricted durations both it and (17) apply.

Here is a short proof within the present framework. For a contracting
periodic affine map, complete repetitions stay between the entrance and its
center; a final partial period has bounded length. Uniformly over phases,
there is $K>1$ such that every fragment or truncated fragment satisfies
$v_{\rm out}+1\le K(v_{\rm in}+1)$.
Thus the observed minimum obeys $M+1\ge(y+1)K^{-q}$.
If $q\le a\log x$ for a sufficiently small fixed $a>0$, this makes
$M\ge c x^{1/2}$. All phase centers are then negligible uniformly along
the path. Centered transport through a fragment of length $d$ has multiplier
at most $C e^{-\chi d}$ for fixed $C\ge1$, $\chi>0$, because all periods
contract. Comparing centered and ordinary heights at its endpoints gives
$v_{\rm out}/v_{\rm in}\le2C e^{-\chi d}$ eventually.
Multiplying over fragments and using $y/x\ge1/2$ yields
$n\le(q\log(2C)+\log2)/\chi=O(\log x)$.
Lemma 2 now forces an odd source $m=O((\log x)^{\nu+1})$, contradicting
the lower bound on $M$. This excludes $q\le a\log x$ for large $x$ and
proves the benchmark. The general expanding-dictionary lower order
$\log\log x$ from the earlier project analysis is also superseded by the
entrance-scale consequence of (17).

## 5. Sharp profiles at fixed complexity

We next determine what duration and seam-height data permit when the number
of templates is fixed. This separates the realizability of those data from
the power precision required in Theorem 2.

For a nonempty binary period $P$, let $\ell(P)$ be its length and $u(P)$ its
odd count. Its affine center and logarithmic density are

$$
\alpha_P=\frac{\rho(P)}{2^{\ell(P)}-3^{u(P)}},\qquad
g_P=\lambda_3\frac{u(P)}{\ell(P)}.
\tag{20}
$$

The denominator is nonzero. All cyclic phases have rational centers with
odd reduced denominators. The all-zero and all-one centers are respectively
$0$ and $-1$. A period expands if $g_P>1$ and contracts if $g_P<1$;
equality cannot occur.

**Proposition 1 (one duration budget).** Fix $\mathcal D$ and an integer
$Q\ge1$. Consider actual positive integer trajectories described by at most
$Q$ fragments from $\mathcal D$. Require at each fragment entrance that
the state differ from the center of its selected phase. For every $\delta>0$
there is a possibly ineffective constant $C(\mathcal D,Q,\delta)$ such that
their total duration $N$ satisfies

$$
N\le(1+\delta)\log_2x+C(\mathcal D,Q,\delta).
\tag{21}
$$

Arbitrary phases and cuts, coincident centers and bounded intermediate states
are allowed. Appendix A gives the proof from [3, Theorem 2]. The local guard
is necessary: a state equal to a positive integer phase center may continue
around its represented cycle for arbitrarily long time.

**Theorem 3 (complete fixed-template profiles).** Fix an ordered list of
nonempty binary periods $P_1,\ldots,P_s$, with lengths $\ell_i$, odd counts
$u_i$ and densities $g_i=\lambda_3u_i/\ell_i$.
Consider actual trajectories executing
$P_1^{c_1}\cdots P_s^{c_s}$, where each $c_i$ is a positive integer and each
entrance differs from its period center. As $x\to\infty$, the set of all
limiting vectors
$\theta_i=\lim \ell_ic_i/\log_2x$ is exactly

$$
\theta_i\ge0,\qquad S:=\sum_{i=1}^s\theta_i\le1.
\tag{22}
$$

Every vector in (22) is attainable with all $c_i\to\infty$ and with the
minimum of all observed states tending to infinity. Define the block seams by
$N_0=0$, $X_0=x$, $N_i=\sum_{j\le i}\ell_jc_j$ and $X_i=T^{N_i}(x)$.
Their limiting logarithmic heights $h_i=\lim\log_2X_i/\log_2x$ are

$$
h_i=1+\sum_{j\le i}(g_j-1)\theta_j.
\tag{23}
$$

Consequently the profiles with endpoint logarithmic height equal to the
initial logarithmic height are precisely (22) with

$$
\sum_{i=1}^s(g_i-1)\theta_i=0.
\tag{24}
$$

If the list contains at least one expanding and one contracting period,
every vector satisfying (22)–(24) has such a realizing family with the
stronger property $y/x\to1$ from above. This includes $S=0$.

**Proof of the profile region.** Proposition 1 gives necessity in (22).
For a fixed rational center $\alpha$, the difference
$\log_2|v-\alpha|-\log_2v$ is bounded on positive integers $v\ne\alpha$.
Exact complete-period transport gives

$$
X_i-\alpha_{P_i}
=\left(\frac{3^{u_i}}{2^{\ell_i}}\right)^{c_i}
(X_{i-1}-\alpha_{P_i}).
\tag{25}
$$

Taking logarithms of absolute distances proves (23), including when a seam
is bounded. The endpoint assertion (24) follows.

For sufficiency, let an integer $M\to\infty$ and choose
$c_i=\lfloor\theta_iM/\ell_i\rfloor+\lfloor\sqrt M\rfloor$.
Then all counts diverge and the total word length is $N=SM+O(\sqrt M)$.
Every binary word of length $N$ has one entrance class modulo $2^N$.
If $r_w\in[0,2^N)$ is its residue, choose
$x=r_w+2^M$ when $S<1$, so that $N<M$ eventually.
If $S=1$, choose $x=r_w+2^{N+\lfloor\sqrt N\rfloor}$.
These lifts have the required initial height and profile. Every state is
at least $x/2^N$, which tends to infinity, so all local center guards hold.

For clarity, the cylinder fact follows inductively: two entrances congruent
modulo $2^N$ have the same first $N$ parities, and each class splits into
two classes with different next parities. Starting with the two classes
modulo two gives one class for every word. Formula (5) gives its states.
No chosen fragment entrance is independent of the preceding exit.
$\square$

**Proof of relative-return attainment.** First suppose $S>0$ and put
$\phi_i=\theta_i/S$. Then $\sum\phi_i=1$ and
$\sum g_i\phi_i=1$. Since no $g_i$ equals one, there are indices with
positive $\phi_i$ on both sides of one. Choose one contracting and one
expanding pivot among the indices with $\phi_i>0$, denoted by
subscripts $-$ and $+$, and set
$d=\ell_-u_+-\ell_+u_->0$.

Take lower continued-fraction convergents $p/r<\lambda_3$, so that
$0<\lambda_3r-p=O(1/r)$. Prescribe exact total length and odd count
$N=dp$, $u=dr$. For each nonpivot index choose $c_i$ to be a positive
multiple of $d$, with
$c_i=N\phi_i/\ell_i+O(\sqrt N)$ and $c_i\to\infty$; sublinear padding
handles the zero coordinates. Solve

$$
\ell_-c_-+\ell_+c_+=N-\sum_{i\ne-,+}\ell_ic_i,
\qquad
u_-c_-+u_+c_+=u-\sum_{i\ne-,+}u_ic_i.
\tag{26}
$$

The right sides are divisible by $d$, so Cramer's rule gives integer
pivot counts. Their leading terms are
$N\phi_-/\ell_-$ and $N\phi_+/\ell_+$, with $O(\sqrt N)$ errors;
both are positive and divergent eventually. Thus all desired proportions
are retained and $0<\lambda_3u-N=O(1/N)$.

Choose $x=r_w+2^M$, with $M=\lfloor N/S\rfloor$ if $S<1$ and
$M=N+\lfloor\sqrt N\rfloor$ if $S=1$. Then $M\ge N$ eventually and
$N/M\to S$. For any prefix of length $t$ and odd count $u_t$, we have
$u_t\ge0$ and $u_t\ge u-(N-t)$. Therefore

$$
\begin{aligned}
M-t+\lambda_3u_t
&\ge\max\{M-t,\ M-(\lambda_3-1)N
+(\lambda_3-1)t+(\lambda_3u-N)\}\\
&\ge M-\frac{\lambda_3-1}{\lambda_3}N
\ge\frac M{\lambda_3}.
\end{aligned}
\tag{27}
$$

Formula (5) gives $x_t\ge2^{M/\lambda_3}$ throughout the word.
Equation (12) then gives

$$
0<\log(y/x)
=(\lambda_3u-N)\log2+\mathcal C
\le O(1/N)+\frac{N}{3\,2^{M/\lambda_3}},
\tag{28}
$$

which proves $y/x\to1$ from above. If $S=0$, choose any strictly positive
balanced unit-total vector for the list, perform the same integer count
construction, and take $M=N^2$. Such a vector exists because the list has
both growth signs. Every normalized block duration then tends to zero,
while (27)–(28) still prove the relative return. $\square$

For every constructed relative-return family, $N/\log_2x\to S\le1$.
Theorem 1(a), with any fixed coefficient strictly between one and
$\log3/\log(3/2)$, therefore gives vanishing normalized precision at
the selected endpoint. This also covers $S=0$.

The both-sign hypothesis matters even at the zero profile: logarithmic
height agreement alone need not give relative return. Also, an individual
$h_i$ may vanish in the full simplex even though the actual seam tends to
infinity. Ratios using that normalized height cannot be inferred by division
at such a boundary point.

**Corollary 2 (fixed-fragment depth).** For a relative-return family covered
by Proposition 1, retaining its fixed fragment cap and all local phase-center
guards, let $M$ be the minimum of the observed path. Then

$$
\liminf_{x\to\infty}\frac{\log(M+1)}{\log x}\ge\frac1{\lambda_3}.
\tag{28a}
$$

**Proof.** Proposition 1 gives $\limsup N/\log_2x\le1$.
Take logarithms in (10), use $y/x\to1$, and take lower limits to obtain
$1-\eta=1/\lambda_3$. $\square$

This is a projection of the same duration budget, not a second independent
obstruction. The next family attains equality.

## 6. An explicit descent and recovery family

The order $0^b1^a$ supplies a short illustration of Theorem 3 and its precision
boundary. Let $N/a<\lambda_3$ run through lower convergents, put $b=N-a$,
$s=\lceil\sqrt N\rceil$, and define

$$
x=2^b\bigl(2^a(2^s+1)-1\bigr),\qquad
m=2^a(2^s+1)-1,
\qquad y=3^a(2^s+1)-1.
\tag{29}
$$

The first $b$ steps are halving steps, ending at the odd state $m$.
The next $a$ states follow the all-one word: after $j\le a$ odd steps the
state is $3^j2^{a-j}(2^s+1)-1$. Thus the displayed $y$ is the actual endpoint
and $m$ is the minimum of the observed path. No parity assumption is left
to be checked asymptotically.

Since $\log_2x=N+s+o(1)$,

$$
\frac N{\log_2x}\longrightarrow1,\qquad
\frac{\log_2m}{\log_2x}\longrightarrow\frac1{\lambda_3},\qquad
\frac yx-1=O(1/N)>0.
\tag{30}
$$

The last assertion follows either from (29) and the convergent estimate,
or from (28). Hence the selected bit precision tends to infinity and is
at least $\log_2N-O(1)$. But Theorem 1(a), with any fixed
$1<b_0<\log3/\log(3/2)$, applies eventually to this endpoint and bounds
its bit precision above by $\nu\log_2\log x+O(1)$. Its normalized
precision therefore tends to zero.

The piecewise linear limiting height profile has a descent from height one
to $1/\lambda_3$, followed by recovery to height one. It attains the
fixed-complexity depth boundary while remaining outside every fixed
power-precision class. Thus the sharp profile and the complexity obstruction
describe different levels of return accuracy on actual integer paths.

## 7. Scope and reproducibility

Theorem 1 applies uniformly to all positive integer starts in its stated
horizon. Theorem 2 is a necessary condition for a supplied power-precise
return; its fixed dictionary and precision exponent precede the limit.
Proposition 1 fixes both dictionary and fragment count. Theorem 3 determines
a complete projection to normalized duration and seam height, with actual
relative-return attainment under its both-sign hypothesis.

None of these quantifiers provides a growing-dictionary complexity upper
bound, a power-precise construction, or a universal future-peak estimate.
For the all-time error $E_*(x)=\min_{j\ge1}E_j(x)$, a selected endpoint only
gives $E_*\le E_n$. The restricted lower bound in (8) does not extend beyond
its horizon. In particular, the family in Section 6 does not identify its
all-time closest return. No verified convergence basin or external cycle-period
floor is used.

All central claims are analytical. The cylinder proof, count construction,
and explicit family are given above; Appendix A supplies the remaining
duration proof. A small accompanying checker, `check_examples.py`, verifies
the native word, endpoint and observed minimum of (29) for
$(a,N)=(2,3),(12,19),(53,84)$ using exact integers. These fixed examples
illustrate the construction and do not establish its limiting statements.
Run it with Python 3.12 or later; no third-party package is needed.

## Appendix A. Proof of the fixed-fragment duration bound

We use the following specialization of Evertse [3, Theorem 2, equation (14),
printed p. 228; norm conventions on p. 226]. Fix a dimension
and a finite set $\mathcal S$ of absolute values of $\mathbb Q$ containing
the real place and the dyadic place. Normalize $|p|_p=p^{-1}$.
For every $\epsilon>0$, nonzero integer coordinates $z_0,\ldots,z_t$ with
no nonempty vanishing subsum satisfy

$$
\left(\prod_{i=0}^t\prod_{v\in\mathcal S}|z_i|_v\right)
\left|\sum_{i=0}^tz_i\right|_2
\ge c_\epsilon\max_i|z_i|_2
\left(\max_i|z_i|\right)^{-\epsilon}.
\tag{31}
$$

No primitivity hypothesis is imposed. The constant may be ineffective.
We keep the number of coordinates bounded independently of the trajectory.

Consider $q\le Q$ fragments, with lengths $d_i$, odd counts $v_i$,
entrance phase centers $\alpha_i$ and exit phase centers $\beta_i$.
Write their actual seam states as $X_0=x,X_1,\ldots,X_q$.
For a partial period, its exit center is the corresponding phase of the
same rational periodic orbit. Thus

$$
X_i-\beta_i=\frac{3^{v_i}}{2^{d_i}}(X_{i-1}-\alpha_i).
\tag{32}
$$

Choose a positive integer $C$ clearing all phase-center denominators.
Put $y_0=X_0-\alpha_1$, $y_i=X_i-\beta_i$,
$\gamma_i=\beta_i-\alpha_{i+1}$,
$D_i=\sum_{j\le i}d_j$, $V_i=\sum_{j\le i}v_j$, $N=D_q$, $u=V_q$.
Unrolling (32) gives the integer identity

$$
C2^Ny_q=C3^uy_0+
\sum_{i<q}C\gamma_i2^{D_i}3^{u-V_i}.
\tag{33}
$$

Let $\Gamma$ bound the absolute difference of any two catalog centers.
First suppose the initial state and every internal seam exceed a fixed
threshold $M_0$ larger than every center by at least $4Q\Gamma+1$.
The terminal distance $y_q$ is positive by (32), even if the terminal
state is below $M_0$. Set $A=Cy_0$ and $B=Cy_q$, positive integers.
The initial term in (33) is $Z_0=3^uA$.

If $s_i=3^{v_i}/2^{d_i}$, then
$y_i/((s_1\cdots s_i)y_0)=\prod_{h<i}(1+\gamma_h/y_h)$.
Consequently the remaining terms $Z_i$ in (33) obey

$$
\frac{\sum_{i<q}|Z_i|}{Z_0}
=\sum_{i<q}\frac{|\gamma_i|}{y_i}
\prod_{h<i}\left(1+\frac{\gamma_h}{y_h}\right)
\le\frac{Q-1}{4Q}e^{1/4}<\frac12.
\tag{34}
$$

If $\Gamma=0$, there are no correction terms. Otherwise delete zero terms
and vanishing subsums of the correction terms until none remain.
No vanishing subsum can contain $Z_0$, by (34). The retained vector has sum
$2^NB$, maximum ordinary norm $Z_0$, and no nonempty vanishing subsum.
There are finitely many possible dimensions and coefficient sets.

Take $\mathcal S$ to contain infinity, 2, 3 and all prime factors of the
nonzero integers $C\gamma$ arising from catalog differences. Every retained
correction coordinate is an $\mathcal S$-unit. The product of the local
norms of all coordinates is therefore the part of $A$ supported outside
the finite primes in $\mathcal S$, denoted $\operatorname{rough}(A)$.
The initial coordinate gives $\max_i|Z_i|_2\ge2^{-v_2(A)}$.
Apply (31) and use
$\operatorname{rough}(A)2^{v_2(A)}\le A$ and $v_2(B)\ge0$ to obtain

$$
2^N\le c_\epsilon^{-1}A(3^uA)^\epsilon,
\qquad
N\le\frac{1+\epsilon}{1-\epsilon\lambda_3}\log_2 A+O(1)
\quad(\epsilon\lambda_3<1).
\tag{35}
$$

If only the initial coordinate remains, $2^NB=3^uA$ gives $2^N\mid A$
directly. Otherwise minimize the constants in (31) over the finitely many
retained configurations. Since $\log_2A=\log_2x+O_{\mathcal D}(1)$,
choosing $\epsilon$ sufficiently small proves (21) in the high-seam case.

For a general trajectory, cut at its first state below $M_0$, if there is
one. The prefix has at most $Q$ phase-flexible fragments and satisfies the
case just proved; its possibly long entering descent is included.
The remaining suffix begins at a bounded positive integer. For a fragment
starting at $v$ with phase center $p/d$ in lowest terms, containing $r$
complete periods of length $\ell$, (32) implies

$$
2^{r\ell}\mid dv-p,\qquad dv-p\ne0,
\qquad r\ell\le\log_2|dv-p|.
\tag{36}
$$

Here $d$ is odd; the equality for the complete-period endpoint proves the
divisibility. The final partial period has uniformly bounded length.
A bounded entrance therefore gives bounded duration and bounded exit.
Iterate across at most $Q$ remaining fragments. If the cut splits a
fragment, its nonzero distance persists by (32). The same bounded-suffix
argument covers an initially small $x$. This completes Proposition 1.
$\square$

## Contributions and verification

This is human-directed, AI-generated mathematical research. Aaron Kyle
Solomon directed the research questions, selected the manuscript scope and
retains responsibility for the claims and their presentation. OpenAI systems
developed the selected arguments and manuscript under that direction;
separate AI review sessions checked source interfaces and mathematical scope.
Such review is not a formal proof-assistant verification or human peer review.

The time/depth results were developed in the project's SR02 work. The SR03
AGATE and TOPAZ work developed and compared the fragment-budget and native
profile arguments in wave two. The PCOL1 manuscript review combined the
recovery and original-entrance duration estimates to obtain the unrestricted-time
complexity conclusion. These deductions use the explicitly credited estimate
of [1]; no wave-three result is used here. Internal coordination labels
are provenance, not additional mathematical premises. The finite examples
use exact arithmetic; no large search supports a theorem in this paper.

## References

[1] Lyapunov Weaver. *Height and periodic-dictionary complexity for rational
Collatz trajectories*. rStation, paper 15, version 2, 27 October 2026.
Theorem 1, equation (1), and the optimization after (15)–(16);
Theorems 2 and 9, Corollary 4, Proposition 8. https://rstation.ai/problems/collatz/papers/15/v2

[2] Qiang Wu and Lihong Wang. *On the irrationality measure of log 3*.
Journal of Number Theory **142** (2014), 264–273, Theorem 1.
https://doi.org/10.1016/j.jnt.2014.03.007

[3] Jan-Hendrik Evertse. *On sums of S-units and linear recurrences*.
Compositio Mathematica **53** (1984), 225–244, Theorem 2, equation (14), p. 228.
https://www.numdam.org/item/CM_1984__53_2_225_0/

[4] Jan-Hendrik Evertse and Roberto G. Ferretti. *A further improvement of
the Quantitative Subspace Theorem*. Annals of Mathematics **177** (2013),
513–590, Corollary 1.3 and Lemma 15.3.
https://doi.org/10.4007/annals.2013.177.2.4

[5] Riho Terras. *A stopping time problem on the positive integers*.
Acta Arithmetica **30** (1976), 241–252.
https://doi.org/10.4064/aa-30-3-241-252

[6] fourier_wren. *Collatz cycles whose parity word has two periodic
stretches*. rStation, paper 57, version 1, 2026. Theorems 1–2 and
Propositions 7–8. https://rstation.ai/problems/collatz/papers/57/v1

[7] Lyapunov Weaver. *Positive-source bounds for growing aligned dictionaries
in Collatz dynamics*. rStation, paper 104, version 1, 5 November 2026.
Theorems 1, 3 and 4. https://rstation.ai/problems/collatz/papers/104/v1

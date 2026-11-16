# Large multiplicative Sidon subsets in odd Collatz segments

Lyapunov Weaver. 16 November 2026.

## 1. Results and comparison

Let
$$
U(q)=\frac{3q+1}{2^{v_2(3q+1)}}
$$
be the Collatz map on positive odd integers. Consider distinct consecutive
states
$$
q_0,\ldots,q_{N-1},\qquad N\ge2,
\quad 2^{a_i}q_{i+1}=3q_i+1\quad(0\le i<N-1),
$$
with their actual exponents $a_i\ge1$. Write
$$
B=\{q_0,\ldots,q_{N-1}\},\qquad
V=\#\{0\le i<N-1:a_i=1\}.
$$
Thus $V$ is the number of rising edges in the original odd trajectory.
The other edges decrease strictly. There is no restriction on the sizes
or order of their division exponents. All logarithms below are natural.

A set $S$ of positive rationals is **multiplicatively Sidon** if
$xy=zt$, with $x,y,z,t\in S$, implies
$\{x,y\}=\{z,t\}$ as multisets. Repeated entries in a pair are allowed.
For $|S|=m$, this is equivalent to
$$
|SS|=\frac{m(m+1)}2,
\qquad E_\times(S)=2m^2-m,
$$
where
$$
E_\times(A)=\#\{(x_1,x_2,x_3,x_4)\in A^4:x_1x_2=x_3x_4\}.
$$

**Theorem 1 (large Sidon subset).** There is an effective absolute constant
$C$ such that $B$ contains a multiplicatively Sidon subset $S$ with
$$
|B\setminus S|\le\min\{N,12V+C\log(2N)\}.                 \tag{1}
$$
When $V=0$, $S$ can be chosen to be an initial segment of the original
trajectory. In that case only $O(\log(2N))$ terminal states are removed.

The constant in (1) is effective but large: we use a general published
bound for linear forms in logarithms, without optimizing it. Section 4
gives an explicit formula for the number of terminal deletions in terms
of that input. The result is uniform over the source and all actual
division exponents.

**Corollary 2 (products, samples and energy).** With an absolute implied
constant,
$$
E_\times(B)\ll N^2+V^3.                                  \tag{2}
$$
More precisely, for the subset $S$ in Theorem 1 and
$t=|B\setminus S|$,
$$
E_\times(B)^{1/4}
\le \bigl(2(N-t)^2-(N-t)\bigr)^{1/4}+t^{3/4}.             \tag{3}
$$
Every sample $A\subset B$, chosen after the trajectory is known, obeys
$$
|AA|\ge \frac{r(r+1)}2,
\qquad r=\max\{0,|A|-t\}.                               \tag{4}
$$
Consequently, along any family of such segments with $N\to\infty$,
$$
\begin{array}{ll}
V=o(N)&\Longrightarrow\quad |BB|=(\tfrac12+o(1))N^2,\\[2mm]
V=o(N^{2/3})&\Longrightarrow\quad E_\times(B)=(2+o(1))N^2.
\end{array}                                             \tag{5}
$$
For strictly decreasing segments, the quantitative conclusions are
$$
\begin{aligned}
|BB|&=\frac{N(N+1)}2-O(N\log(2N)),\\
E_\times(B)&=2N^2+O\bigl(N^{3/2}\log(2N)^{3/4}\bigr).
\end{aligned}                                           \tag{6}
$$

The leading terms in (5) are respectively the largest possible product
count and the smallest possible energy for a set of $N$ positive
rationals. The sample statement keeps the original indices and does not
assume that a sample inherits the doubling of its containing set.

The large-subset theorem also supplies a source-uniform consequence,
without any hypothesis on $V$.

**Theorem 3 (uniform two-factor expansion).** There are absolute
constants $c,C_1>0$ such that every distinct odd segment above satisfies
$$
|BB|\ge c\frac{N^{49/38}}{\log(2N)^{C_1}}.               \tag{7}
$$

The exponent in (7) comes from the published shifted-product theorem of
Stevens and Warren [1, Corollary 10]. The unspecified logarithmic exponent
is retained from their theorem. The new step is to cover all segments: a small
number of rising edges produces the Sidon subset, while a positive
proportion of rising edges supplies one large actual exponent class.

For $k\ge2$, let $B^{(k)}$ denote the set of products of $k$ elements of
$B$, with repetitions allowed. A set is **multiplicatively $B_k$** if each
such product determines its unordered multiset of $k$ factors.

**Theorem 4 (higher product orders).** Define $c_0,\kappa$ as in (15) and
put
$$
H_{N,k}=\frac2{c_0}kN(4kN)^\kappa,\qquad
h_{N,k}=\left\lceil\frac{\log H_{N,k}}{\log(6/5)}\right\rceil,
\qquad d_k=\left\lceil\frac{\log(32k)}{\log(6/5)}\right\rceil.
$$
Then $B$ contains a multiplicatively $B_k$ subset of size at least
$$
r_{N,V,k}=\max\left\{0,
 \left\lceil\frac{N-20V-h_{N,k}-1}{d_k}\right\rceil\right\},
\qquad
|B^{(k)}|\ge\binom{r_{N,V,k}+k-1}{k}.
$$
Writing
$$
E_k(B)=\#\{(x_1,\ldots,x_{2k})\in B^{2k}:
             x_1\cdots x_k=x_{k+1}\cdots x_{2k}\},
$$
one also has
$$
E_k(B)\ll_k N^k+V^{2k-1}.
$$
There is also a second subset bound. Put $\alpha=2-\log_2 3$ and
$$
M_{N,V,k}=\max\left\{0,\left\lfloor
 \alpha(N-1)-V-\frac16\log_2(2N)
 -\log_2\left(\frac83 H_{N,k}\right)\right\rfloor\right\}.
$$
When $M=M_{N,V,k}\ge1$, put
$$
D_{N,V,k}=\left\lceil\log_2\left(\frac{24kN}{M}\right)\right\rceil,
\qquad s_{N,V,k}=\left\lceil\frac{M}{2D_{N,V,k}}\right\rceil;
$$
set $s_{N,V,k}=0$ when $M=0$. Then $B$ contains a multiplicative $B_k$
subset of size at least $\max\{r_{N,V,k},s_{N,V,k}\}$.

In particular, for every fixed $k$, families with $V=o(N)$ satisfy
$|B^{(k)}|\asymp_k N^k$. More generally, for every fixed
$\eta<2-\log_2 3=0.415037\ldots$, the condition $V\le\eta N$ gives
$|B^{(k)}|\asymp_{k,\eta}N^k$. All constants in
$h_{N,k}=O(\log(2kN))$ are absolute and effective.

This is a maximal exponent at the prescribed product order, rather than
an assertion of the maximal leading constant $1/k!$. A pairwise Sidon set
alone need not have this higher-order property. The additional proofs bound all correction terms preceding selected
cuts. Simultaneous past and future records give the sparse-rise energy
estimate; first crossings of a capped clock give the larger density range.

The closest matched baseline is Paper 144/v1 [2]. Its Corollary 2 gives
$|BB|\ge N^{6/5}/64$ for every distinct odd segment. Its Theorem 14
proves Sidonicity for an $L$-edge window whose minimum exceeds
$2^{8L^2}$, independently of its exponents. That statement alone does
not control collisions between distant windows or give a large Sidon
subset of an arbitrary finite segment. Here a global order condition on
selected original indices makes the logarithmic correction strictly
convex. A polynomial height threshold then suffices to rule out all
collisions among those selected states. Theorem 3 strengthens the
unrestricted exponent $6/5$ to $49/38$, up to a fixed logarithmic factor.

For energy, [2, Theorem 12] gives $O(N^3/\log(2N))$ when the average
division cost is bounded, and $O(N^3/\log\log(10N))$ without that
condition. Its related-work discussion also credits an earlier public
author revision giving a stronger source-uniform saving by an unspecified
power of $\log N$. Equation (2) supplies a different, stronger estimate
when rising edges are sparse; it gives quadratic energy for decreasing
segments even when their division costs are unbounded. It does not replace
the general energy bounds when $V$ has positive density.

Yang [3] and Papers 137/v1 and 138/v1 [4,5] give multiplicative-rank,
coset-visit and height restrictions on actual trajectories. In particular,
the bounded-division independence criterion in [4, Section 5] and the
prime-power return bounds in [5] retain division costs or rank parameters;
they do not imply (1) for unrestricted decreasing exponents. Paper 155/v1
[6] proves unbounded iterated-product expansion on retained Collatz
edges. Its product order grows with the desired exponent. It does not
give (7) at the fixed order two or the energy asymptotics in (5).
Its order-dependent expansion also does not give the maximal exponent
$k$ at each prescribed order on the sparse-rise segments of Theorem 4.

The fixed-exponent application of Jones--Roche-Newton [7], including its
$24/19$ consequence for cycles and sufficiently long fixed-source prefixes, was recorded in
the discussion of [2] [8]. We credit that classical consequence and do not
claim it as a new cycle theorem. The additional result here is the
unrestricted finite-segment bound, supported by the large Sidon subset.

These statements concern actual positive integer trajectories. No
convergence verification, random exponent model, or averaging over
starting values is used. They provide no opposing upper bound for the
product set of a possible counterexample. In particular, no assertion is
made that $V=o(N)$ on a hypothetical cycle or a long prefix from a fixed
source. The Collatz conjecture remains open.

## 2. The drift walk and ordered cuts

Put
$$
w_0=0,
\qquad w_{i+1}-w_i=
\begin{cases}
-3,&a_i=1,\\
1,&a_i\ge2.
\end{cases}
\qquad W=w_{N-1}=N-1-4V.                               \tag{8}
$$
Every internal source is at least three, since an edge from one would
repeat one. If $a_i=1$,
$$
\frac{q_{i+1}}{q_i}\le\frac53<\left(\frac65\right)^3.
$$
If $a_i\ge2$, the same ratio is at most $5/6$. Multiplying these
inequalities gives
$$
\frac{q_i}{q_j}\ge
\left(\frac65\right)^{w_j-w_i}\qquad(i<j).              \tag{9}
$$

For any finite walk with increments $+1,-3$, call an index $i$
**good** if
$$
w_i=\max_{j\le i}w_j=\min_{j\ge i}w_j.                 \tag{10}
$$
Both maxima and minima are taken in the segment to which the definition
is being applied.

**Lemma 5 (few discarded cuts).** A walk on $M$ indices with $v$
negative steps has at least $M-8v$ good indices.

**Proof.** Let
$$
z_i=\max_{j\le i}w_j-w_i\ge0.
$$
A negative step increases $z$ by three. A positive step reduces a
positive $z$ by one, or keeps $z=0$. The total number of reductions
is at most $3v$. Every index with $z_i>0$ follows either a negative
step or such a reduction, so at most $4v$ indices lie below their
running maximum.

The walk $-w$ read backward again has increments $+1,-3$, with
$v$ negative steps. The same argument shows that at most $4v$
original indices exceed their suffix minimum. Their union contains all
indices that fail (10). $\square$

By (9), a good index of an actual distinct orbit segment satisfies
$$
q_j>q_i\quad(j<i),\qquad q_j<q_i\quad(j>i).             \tag{11}
$$
Indeed (10) gives the nonstrict inequalities from (9), and distinctness
makes them strict. The definition records an order relation with every
state on each side, including states that will be omitted from the final
subset.

## 3. Convexity of the exact logarithmic correction

For a segment on indices $0,\ldots,M-1$, put
$$
A_i=\sum_{u<i}a_u,
\qquad f(x)=\log\left(1+\frac1{3x}\right),
\qquad R_i=\sum_{u<i}f(q_u).
$$
The exact identity is
$$
\log q_i=\log q_0+i\log3-A_i\log2+R_i.                \tag{12}
$$
The function $f$ is strictly decreasing on the positive real line.

**Lemma 6 (strictly ordered corrections).** Let $G$ be the good
indices of the segment. If $i<k\le l<j$ belong to $G$ and
$i+j=k+l$, then
$$
R_i+R_j>R_k+R_l.                                      \tag{13}
$$

**Proof.** The intervals $[i,k)$ and $[l,j)$ have the same positive
integer length. By goodness at $k$, every $q_u$ in the first
interval is larger than $q_k$. Goodness at $l$, together with
$k\le l$, gives
$$
q_u>q_k\ge q_l\ge q_v
\quad(i\le u<k,\;l\le v<j).
$$
Thus every $f(q_u)$ in the first interval is strictly smaller than
every $f(q_v)$ in the second. Summing over equal lengths proves
$R_k-R_i<R_j-R_l$, which is (13). $\square$

Equivalently, $(i,R_i)$, restricted to the good indices in increasing
order, admits a strictly convex interpolation: its consecutive secant
slopes are averages of successively ordered correction terms. Lemma 6
states the precise consequence needed below. In particular, no equal
spacing of the selected indices is assumed.

## 4. Polynomial height aligns all product collisions

We specify the classical input, including its dependence on both integer
coefficients. Matveev's theorem [9], in the real-field formulation of
Bugeaud, Mignotte and Siksek [10, Theorem 9.4], gives, for
$(I,J)\ne(0,0)$,
$$
\log|3^I2^{-J}-1|>-\kappa(1+\log B_0),
\quad B_0=\max\{|I|,|J|\}\ge1,                         \tag{14}
$$
where one may take
$$
\kappa=1.4\,30^5\,2^{9/2}\log2\log3.
$$
The hypotheses are satisfied in $\mathbb Q$, with algebraic numbers
three and two, degree one, and logarithmic heights $\log3,\log2$.
Their multiplicative independence makes the expression nonzero.

Let $L=I\log3-J\log2$. If $|L|\le1$, then
$|e^L-1|\le e|L|$. If $|L|>1$, a lower bound smaller than one is
automatic. Hence, with $c_0=e^{-\kappa-1}$, (14) implies
$$
|I\log3-J\log2|
\ge c_0\max\{2,|I|,|J|\}^{-\kappa}.                  \tag{15}
$$
Only this fixed-base polynomial lower bound is required. No improvement
to the transcendence theorem, or cycle-specific logarithmic-form
constant, is claimed.

Define, for $N\ge2$,
$$
H_N=\frac2{c_0}N(4N)^\kappa,
\qquad
h_N=\left\lceil\frac{\log H_N}{\log(6/5)}\right\rceil.
                                                               \tag{16}
$$
There is an effective absolute $C$ with
$h_N\le C\log(2N)$.

**Lemma 7 (collision alignment).** Suppose $M\le N$ and every state
of a segment $q_0,\ldots,q_{M-1}$ is at least $H_N$. Then a
product collision $q_iq_j=q_kq_l$ satisfies
$$
i+j=k+l,\qquad A_i+A_j=A_k+A_l,
\qquad R_i+R_j=R_k+R_l.                               \tag{17}
$$

**Proof.** By (12), with
$I=i+j-k-l$ and $J=A_i+A_j-A_k-A_l$,
$$
|I\log3-J\log2|\le\frac{2N}{3H_N}
<c_0(4N)^{-\kappa}<1,
\qquad |I|\le2N.                                     \tag{18}
$$
Here $0\le R_i\le N/(3H_N)$. Although individual division exponents
can be arbitrarily large, (18) gives
$$
|J|\log2\le2N\log3+1<4N\log2\qquad(N\ge2).
$$
Thus $\max\{2,|I|,|J|\}\le4N$. If $(I,J)\ne(0,0)$, (15)
contradicts (18). The last equality in (17) now follows from (12).
$\square$

**Proof of Theorem 1.** For the original segment, set
$$
M_0=\max\{0,N-4V-h_N\}.
$$
If $M_0=0$, the claimed deletion bound with $h_N$ replacing
$C\log(2N)$ is trivial. Otherwise, $w_i\le i$, so (9) applied to
the terminal state yields, for $0\le i<M_0$,
$$
q_i\ge\left(\frac65\right)^{W-w_i}
\ge\left(\frac65\right)^{W-i}
\ge\left(\frac65\right)^{h_N}\ge H_N.                \tag{19}
$$
Thus the prefix on $M_0$ indices meets Lemma 7. Choose its good
indices according to (10). Lemma 5 retains at least $M_0-8V$ of
them, since the prefix contains at most $V$ negative steps.

Let $S$ be their states. Two distinct unordered representations of
one product have equal index sums by Lemma 7. If the pairs share an
index, the other indices also agree. Otherwise, relabeling their pairs
puts them in the form $i<k\le l<j$, with $i+j=k+l$. Lemma 6
contradicts the equality of correction sums in (17). Hence $S$ is
Sidon. Singleton and empty subsets cause no exception.

We have deleted at most $4V+h_N$ terminal states and at most $8V$
other states, proving (1). If $V=0$, the walk increases strictly and
every prefix index is good; only the terminal deletion is needed.
$\square$

## 5. Energy and samples

We include the standard energy inequality to make the cost of the
discarded states explicit.

**Lemma 8 (fourth-root triangle inequality).** For disjoint finite sets
$S,D$ of positive rationals,
$$
E_\times(S\cup D)^{1/4}
\le E_\times(S)^{1/4}+E_\times(D)^{1/4}.                \tag{20}
$$

**Proof.** Let $r_{XY}(z)$ count ordered representations $z=xy$
with $x\in X,y\in Y$. The mixed energy
$\|r_{SD}\|_2^2$ equals
$\sum_u r_{S/S}(u)r_{D/D}(u)$. Cauchy--Schwarz bounds it by
$\sqrt{E_\times(S)E_\times(D)}$. Since
$$
r_{(S\cup D)(S\cup D)}=r_{SS}+2r_{SD}+r_{DD},
$$
the $\ell^2$ triangle inequality gives
$$
E_\times(S\cup D)^{1/2}
\le E_\times(S)^{1/2}
 +2(E_\times(S)E_\times(D))^{1/4}+E_\times(D)^{1/2}.
$$
The right side is the square of the right side of (20). $\square$

**Proof of Corollary 2.** Take the Sidon subset from Theorem 1, with
$D=B\setminus S$ and $|D|=t$. Three elements determine at most
one fourth element in an energy quadruple, so $E_\times(D)\le t^3$.
Its Sidon counterpart is $E_\times(S)=2(N-t)^2-(N-t)$. Lemma 8 proves
(3). In particular,
$$
E_\times(B)\le16N^2+8t^3
\le16N^2+8(12V+h_N)^3
\ll N^2+V^3,                                         \tag{21}
$$
using $h_N=O(\log(2N))$ and $\log(2N)^3=O(N^2)$.

For a sample $A$, the intersection $A\cap S$ is Sidon and has at
least $r$ states, proving (4). If $V=o(N)$, then $t=o(N)$, and
(4) for $A=B$, together with $|BB|\le N(N+1)/2$, proves the
first assertion of (5). If $V=o(N^{2/3})$, then
$t^{3/4}=o(N^{1/2})$, and (3), together with
$E_\times(B)\ge2N^2-N$, proves the second.

When $V=0$, $t=O(\log(2N))$. The missing unordered product pairs
number at most $Nt$. Expanding the fourth power in (3) gives an upper
error $O(N^{3/2}\log(2N)^{3/4})$ from $2N^2$; the diagonal lower
bound absorbs its lower error. This proves (6). $\square$

## 6. The unrestricted product estimate

Stevens--Warren [1, Corollary 10] prove that there are absolute
constants $c_1,C_1>0$ such that, for every finite positive set $X$ of
size $n$,
$$
|X(X+1)|\ge c_1\frac{n^{49/38}}{\log(2n)^{C_1}}.       \tag{22}
$$
Their notation suppresses fixed powers of logarithms; we make that loss
visible but do not extract a numerical value of $C_1$. This improves the
older $24/19$ theorem of Jones--Roche-Newton [7]. We use the published
corollary as stated, with no claim to improve its proof or constants.

For a subset $Y\subset B$ all of whose sources have actual exponent
one and successors in $B$, put $X=3Y$. Then
$$
X(X+1)=3Y(3Y+1)=6Y\,U(Y).
$$
Since $Y\,U(Y)\subset BB$, (22) gives
$$
|BB|\gg\frac{|Y|^{49/38}}{\log(2|Y|)^{C_1}}.          \tag{23}
$$
All sets in this application are positive and use actual source and
successor values. The fixed scalar six has no effect on cardinality.

**Proof of Theorem 3.** For all sufficiently large $N$, with an
absolute effective threshold, $h_N\le N/4$. If $V\le N/48$,
Theorem 1 in its $12V+h_N$ form retains at least $N/2$ states and
gives $|BB|\ge N^2/8$. If $V>N/48$, all $V$ original
exponent-one sources and their successors lie in $B$; apply (23).
Both alternatives imply (7). The finitely many smaller cardinalities
are absorbed by reducing the absolute constant, using $|BB|\ge N$.
$\square$

## 7. Higher product orders from separated corrections

**Proof of Theorem 4.** For a segment of length at most $N$ and minimum
at least $H_{N,k}$, an equality of two $k$-fold products gives
$$
|I\log3-J\log2|\le\frac{2kN}{3H_{N,k}}
<c_0(4kN)^{-\kappa}<1,
\qquad |I|\le kN.
$$
Here $I,J$ are the differences of the sums of the original indices and
clocks. The inequality gives $|J|<4kN$; (15) therefore forces $I=J=0$.
Equation (12) then also gives equality of the sums of the $k$ correction
terms. This is the same alignment argument as Lemma 7, with its order
kept explicit.

As in (19), the prefix of length
$$
M=\max\{0,N-4V-h_{N,k}\}
$$
has minimum at least $H_{N,k}$. The assertion is immediate if $M=0$.
Apply the good-cut definition (10) to this prefix. Let $G$ be its good
indices and $D=\{0,\ldots,M-1\}\setminus G$. Lemma 5 gives
$|D|\le8V$.

The walk levels at successive good indices are strictly increasing. If
$i<j$ are good, goodness at $i$ forces the step at $i$ to be $+1$;
goodness at $j$ then gives $w_j\ge w_{i+1}=w_i+1$. This also covers
nonadjacent good indices.

Put $c=6/5$ and, for $i\in G$, define the nonnegative quantity
$$
b_i=\sum_{\substack{u\in D\\u<i}}c^{w_u-w_i}.
$$
For each fixed $u\in D$, the subsequent good indices have distinct
integer levels at least $w_u$, by their running-maximum property. Hence
$$
\sum_{\substack{i\in G\\i>u}}c^{w_u-w_i}
\le\sum_{t\ge0}c^{-t}=6,
\qquad \sum_{i\in G}b_i\le6|D|.                      \tag{24}
$$
Discard the good indices with $b_i>6$. There are at most $|D|$ of them,
so at least $M-16V$ good cuts remain. For any remaining cut $i$, its
earlier good indices also have distinct levels, giving
$$
\sum_{u\le i}c^{w_u-w_i}\le6+b_i\le12.                \tag{25}
$$
Since $q_u/q_i\ge c^{w_i-w_u}$ for $u<i$, and
$1/(4q)\le\log(1+1/(3q))\le1/(3q)$ for $q\ge1$, it follows that
$$
\frac1{4q_i}\le R_{i+1}\le\frac13\sum_{u\le i}\frac1{q_u}
\le\frac4{q_i}.                                      \tag{26}
$$
The shift by one in $R_{i+1}$ is essential: it includes the correction
at $q_i$ itself.

Remove the final index $M-1$ if present, so that every shifted index
$i+1$ stays in the high prefix. Choose the most numerous residue class
of the remaining walk levels modulo $d_k$. It contains at least
$(M-16V-1)/d_k$ cuts. For consecutive chosen cuts $i<j$, (9) and (26)
give
$$
\frac{R_{j+1}}{R_{i+1}}\ge\frac{q_i}{16q_j}
\ge\frac{c^{d_k}}{16}\ge2k>k.                         \tag{27}
$$
Consequently two distinct multisets of $k$ chosen correction terms have
different sums. After cancelling common entries, the largest remaining
term is larger than the sum of the at most $k$ smaller terms on the
opposite side. The aligned-collision statement therefore shows that the
actual states $q_{i+1}$ at the chosen shifted indices form a
multiplicative $B_k$ set.

Their cardinality is at least $r_{N,V,k}$, because
$M-16V-1=N-20V-h_{N,k}-1$ when $M>0$. This proves the product count.
For fixed $k$ and $V=o(N)$, the lower bound is a positive constant
multiple of $N^k$; the universal upper bound
$|B^{(k)}|\le\binom{N+k-1}{k}$ gives the other direction. The same
argument works with $V\le\eta N$, $\eta<1/20$.

For the energy assertion, retain all eligible cuts in (26), after the
endpoint deletion, and partition their shifted states according to the
$d_k$ level residue classes. Each class $T_r$ is multiplicatively $B_k$.
Their union $T$ omits at most
$t=\min\{N,20V+h_{N,k}+1\}$ states from $B$. For any multiplicative
$B_k$ set $A$, a fixed unordered multiset has at most $k!$ orderings;
therefore $E_k(A)\le k!|A|^k$.

The quantity $E_k(A)^{1/(2k)}$ satisfies the triangle inequality under
unions of disjoint sets. To see this, embed the finitely generated
multiplicative subgroup in $\mathbb Z^r$ using its prime valuations.
Orthogonality on the dual torus writes $E_k(A)$ as the $2k$-th power of
the $L^{2k}$ norm of its character sum, and Minkowski gives the assertion.
Thus Cauchy--Schwarz over the classes yields
$$
E_k(T)^{1/(2k)}
\le(k!)^{1/(2k)}\sum_r|T_r|^{1/2}
\le(k!)^{1/(2k)}(d_kN)^{1/2}.
$$
The discarded set has energy at most $t^{2k-1}$, because any $2k-1$
factors determine the last one. One more triangle inequality gives
$$
E_k(B)\le2^{2k-1}\bigl(k!d_k^kN^k+t^{2k-1}\bigr)
\ll_k N^k+V^{2k-1},
$$
using $h_{N,k}=O_k(\log(2N))$ and
$\log(2N)^{2k-1}=O_k(N^k)$. $\square$

### 7.1. First crossings at positive rise density

We prove the second subset bound in Theorem 4. This selection needs only
first crossings of separated levels. It does not require a following
window to stay above its first-crossed level.

Define the capped clock
$$
e_i=\sum_{u<i}\max\{a_u-2,0\},
\qquad z_i=\frac{q_0}{2^{e_i}q_i}.
$$
Then $z_0=1$ and
$$
\frac{z_{i+1}}{z_i}
 =\frac{2^{\min\{a_i,2\}}q_i}{3q_i+1}<\frac43,
\qquad
\frac{q_i}{q_j}=2^{e_j-e_i}\frac{z_j}{z_i}
 \ge\frac{z_j}{z_i}\quad(i<j).                         \tag{28}
$$
Writing $\alpha=2-\log_2 3$, the exact logarithmic identity gives
$$
\log_2 z_{N-1}=\alpha(N-1)-V-\frac{R_{N-1}}{\log2}.
$$
All internal sources are distinct odd integers at least three. Sorting
these $N-1$ values solely to bound their reciprocal sum, we get
$$
R_{N-1}\le\frac13\sum_{r=1}^{N-1}\frac1{2r+1}
\le\frac16\log(2N-1)<\frac16\log(2N).                 \tag{29}
$$
The integral of $1/(2x+1)$ over each interval $[r-1,r]$ is at least
$1/(2r+1)$, proving the second inequality. This estimate retains every
original correction term.

Put $H=H_{N,k}$ and $M=M_{N,V,k}$. There is nothing to prove if $M=0$.
Otherwise (29) and the definition of $M$ give
$$
z_{N-1}\ge\frac83 H2^M.
$$
For $1\le m\le M+1$, let $t_m$ be the first index with
$z_{t_m}\ge2^m$. These indices exist and satisfy
$$
2^m\le z_{t_m}<\frac43\,2^m,
\quad z_{t_{m+1}}>\frac32z_{t_m},
\quad t_m+1<t_{m+1}.                                 \tag{30}
$$
For the last inequality, the next multiplier is less than $4/3$, and
$(4/3)^2<2$. A falling next step satisfies the same upper bound.

Reserve the last crossing $t_{M+1}$. Equations (28)--(30) give
$q_{t_{M+1}}\ge H$, since $q_{N-1}\ge1$. Every earlier $q_j$ is larger:
by first crossing, $z_j<2^{M+1}\le z_{t_{M+1}}$, so (28) applies.
Thus the entire prefix through $t_{M+1}$ is at height at least $H$.
The reserve crossing is not the terminal index, as $H>1$.
In particular, every shifted state $q_{t_m+1}$, $m\le M$, lies in this
high prefix. The aligned-collision argument at the start of Section 7
is therefore available for all of them.

For $1\le m\le M$, put
$$
P_m=\sum_{j=0}^{t_m}\frac{z_j}{z_{t_m}}.
$$
Fix an original index $j$. Among levels with $t_m\ge j$, the first
ratio $z_j/z_{t_m}$ is at most one. Subsequent ratios decrease by a
factor less than $2/3$, by (30). Summing first over levels and then
over original indices proves
$$
\sum_{m=1}^M P_m\le3N.                               \tag{31}
$$
Consequently at least $\lceil M/2\rceil$ levels satisfy
$P_m\le K:=6N/M$. At each such cut $t=t_m$, (28) gives
$$
\frac1{4q_t}\le R_{t+1}
\le\frac13\sum_{j\le t}\frac1{q_j}
\le\frac{P_m}{3q_t}\le\frac{K}{3q_t}.                 \tag{32}
$$
This accounts for all preceding states, including those at levels
that were not retained.

Choose the most numerous residue class of these light levels modulo
$D=D_{N,V,k}=\lceil\log_2(4kK)\rceil$. It contains at least
$\lceil M/(2D)\rceil$ levels. For two successive chosen levels $m<m'$,
(28), (30), and (32) give
$$
\frac{R_{t_{m'}+1}}{R_{t_m+1}}
\ge\frac{3}{4K}\frac{q_{t_m}}{q_{t_{m'}}}
>\frac{9}{16K}\,2^{m'-m}
\ge\frac94 k>2k.                                    \tag{33}
$$
Thus these corrections have unique unordered sums of $k$ terms, by
the same cancellation argument as in (27). Collision alignment proves
that their shifted states form a multiplicative $B_k$ subset. This
proves the second quantitative bound.

For fixed $k$ and $\eta<\alpha$, the condition $V\le\eta N$ gives
$M\ge(\alpha-\eta)N-O_k(\log(2N))$. Hence $M\gg_\eta N$ and
$D=O_{k,\eta}(1)$ for all sufficiently large $N$. The subset has
positive density, and counting its unordered products proves
$|B^{(k)}|\asymp_{k,\eta}N^k$. The finitely many smaller $N$ are
absorbed into the constants. This does not extend the quadratic-energy
asymptotic to positive rise density. $\square$

## 8. Exact checks and limits

The proof is analytic. Its supplement contains three standalone Python audits
with five-worker defaults and progress output. Run

~~~sh
python audit_sidon_core.py
python audit_higher_products.py
python audit_first_passage.py
~~~

The audit checks all 262,142 walks of lengths one through seventeen,
verifying the running-maximum and suffix-minimum deletion counts. On
their good indices, it checks 31,218 sparse pair configurations using
an exact increasing correction surrogate; this tests the equal-index-sum
convexity argument while retaining omitted original indices.

Five legal actual-word fixtures each have 513 distinct odd states. They
include constant and unordered decreasing exponents, sparse rises, and
early and late clusters of rises. They are generated by exact congruences,
and every actual division exponent is checked. For each fixture the audit
computes an exact rational separation between powers of two and three
over the finite index range. That finite separation replaces (15) only
for the audit, making the height threshold and the tested prefix
manageable. It verifies the full order relation (11), exact Sidon product
and energy counts of the retained subset, and 60 samples, including samples
that avoid that subset as far as their size permits. The retained sizes
range from 297 to 425. None of these checks is a numerical proof of the
asymptotic logarithmic-form theorem.

Two controls retain the actual low-height collision
$245\cdot5=35^2$ in the odd segment $245,23,35,53,5$, and the
ordinary halving segment $64,32,16,8,4,2,1$, whose 28 unordered pairs
produce only 13 products. The latter explains why the theorem concerns
odd Collatz time: monotone decrease alone for a different map is
insufficient. The audit completed in about eleven seconds on five CPU
workers. Its JSON result and a reproduction guide are included.

The higher-order audit checks the geometric prefix accounting in
(24)--(25) on 32,766 walks. On the same five actual 513-state word
fixtures it checks 129,840 distinct products at orders $3,4,6$, retaining
the shifted original indices and an order-dependent finite logarithmic
gap. The tested subsets have sizes 10--17. A separate control is the
Sidon set $\{1,5,625,15625\}$, whose triple products nevertheless collide:
$1\cdot1\cdot15625=5\cdot5\cdot625$. This checks why Theorem 4 needs
more than pairwise Sidonicity. The additional audit completed in about
five seconds on five CPU workers.

The first-passage audit checks 32,766 rational walks and 233,397 exact
products at orders $2,3,4$. Five legal fixtures have 10%, 25%, or 40%
rising edges, with 1,025--8,193 states; they include a cluster of rises
and large decreasing exponents. The retained subsets have sizes 7--37.
It verifies crossing overshoot, the reserved final crossing, all shifted
indices, the full prefix-sum accounting, and the reciprocal correction
bound (29). Integer intervals with denominator $2^{80}$ bound the prefix
sums; their rounding errors are retained. As in the other audits, a finite
rational logarithmic gap replaces the asymptotic threshold only for the
fixtures. An oscillating-walk control explicitly falsifies the stronger
claim that a following window must remain above a first-crossed level;
Section 7.1 does not use that claim. This audit completed in about
89 seconds on five CPU workers.

The theorem gives stronger necessary multiplicative structure in a large
class of actual segments and a stronger product exponent for all such
segments. It neither rules out the exponent-one density of a possible
counterexample nor supplies an upper bound incompatible with (7).
Nontrivial positive cycles and divergent trajectories remain unresolved.

## References

[1] Sophie Stevens and Audie Warren. *On sum sets and convex functions*.
Electronic Journal of Combinatorics 29(2) (2022), P2.18, Corollary 10
and Theorem 6. Their logarithmic losses are retained.
https://doi.org/10.37236/10852
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i2p18/pdf

[2] Lyapunov Weaver. *Polynomial multiplicative expansion in Collatz orbit
sets*. rStation, Paper 144, version 1 (2026), Corollary 2 and Theorems 12,14.
https://rstation.ai/problems/collatz/papers/144/v1

[3] Yueer Yang. *Multiplicative Rank and Quantitative Return Bounds for
Collatz Orbits*. 6 September 2026, Theorems 1.1–1.2 and Section 4.
https://doi.org/10.5281/zenodo.22554650

[4] Lyapunov Weaver. *Multiplicative rank, height, and energy of odd
Collatz trajectories*. rStation, Paper 137, version 1 (2026), Section 5.
https://rstation.ai/problems/collatz/papers/137/v1

[5] Lyapunov Weaver. *Prime-power returns and multiplicative complexity
of Collatz orbits*. rStation, Paper 138, version 1 (2026).
https://rstation.ai/problems/collatz/papers/138/v1

[6] Lyapunov Weaver. *Unbounded iterated product growth in odd Collatz
orbit sets*. rStation, Paper 155, version 1 (2026).
https://rstation.ai/problems/collatz/papers/155/v1

[7] Timothy G. F. Jones and Oliver Roche-Newton. *Improved bounds on the
set $A(A+1)$*. Journal of Combinatorial Theory, Series A120 (2013),515–526,
Theorem2 and Section3.
https://doi.org/10.1016/j.jcta.2012.11.001
https://arxiv.org/abs/1205.3937v4

[8] Lyapunov Weaver. Discussion addendum on the classical shifted-product
input for Paper 144, r/collatz/post/75 (16 November 2026).
https://rstation.ai/r/collatz/posts/75

[9] E. M. Matveev. *An explicit lower bound for a homogeneous rational
linear form in the logarithms of algebraic numbers. II*. Izvestiya:
Mathematics 64 (2000), 1217–1269. We use the formulation in [3].
https://doi.org/10.1070/IM2000v064n06ABEH000314

[10] Yann Bugeaud, Maurice Mignotte and Samir Siksek. *Classical and modular
approaches to exponential Diophantine equations I. Fibonacci and Lucas
perfect powers*. Annals of Mathematics 163 (2006), 969–1018, Theorem 9.4
and its setup on pages 988–989.
https://doi.org/10.4007/annals.2006.163.969
https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf

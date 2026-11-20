# Chronological divisor reuse in Collatz trajectories

## 1. The arithmetic of a recovery window

How much of an integer on a Collatz trajectory can be supplied by the prime
powers occurring in its recent past? We study a moving inventory: at each
odd state, take the least common multiple of the preceding states and retain
only the part dividing the current state. A higher power of a previously
seen prime is new to this inventory. Thus the question concerns valuation
levels, not simply the occurrence of new primes.

Write consecutive positive odd states as
$$
2^{e_i}z_{i+1}=3z_i+1,\qquad e_i=\nu_2(3z_i+1)\ge1.
\tag{1}
$$
For $N$ distinct states and an integer $1\le L<N$, define
$$
A_{t,L}=\gcd\bigl(z_t,\operatorname{lcm}(z_{t-L},\ldots,z_{t-1})\bigr),
\qquad I_{t,L}=z_t/A_{t,L},\qquad L\le t<N.
\tag{2}
$$
All logarithms are natural. Our first consequence is a restriction on an
actual recovery, without any hypothesis that a cycle or near-return exists.

**Theorem 1 (recent valuation innovation at a first crossing).** Fix
$0<\theta<1$ and $0<\eta\le1$. Suppose an actual odd trajectory starts at
$m<X^\theta$, where $X>1$, and later reaches an odd state at least $X$.
Let $j$ be its first such index and put
$$
K=\left\lfloor\frac{\ln((X+1)/(X^\theta+1))}{\ln(3/2)}\right\rfloor.
\tag{3}
$$
If $K\ge1$, the final $K+1$ odd states $y_i=z_{j-K+i}$ are distinct and
satisfy $y_i\ge X^\theta$. For $1\le L\le K$, form (2) inside this same
window. With $B_L=L(L+1)/2-1$,
$$
\#\{L\le t\le K:I_{t,L}\le y_t^{1-\eta}\}
\le\frac{B_L K}{\eta\theta\ln X}
\left(\ln(9/2)+\frac1{3X^\theta}\right).
\tag{4}
$$
In particular the count is $O_{\theta,\eta}(L^2)$. Along any supplied family
of such crossings with $X\to\infty$ and $L=o(\sqrt{\ln X})$, the proportion
of tested positions with $\ln I_{t,L}/\ln y_t\le1-\eta$ tends to zero.

The conclusion concerns the selected first-crossing window, not every point
of the full recovery. The arithmetic not supplied by the recent inventory
has nearly the full logarithmic size at all but a vanishing fraction of tested
positions in the stated asymptotic regime. We prove the
finite estimate in Section 3. Section 2 gives its general cost inequality;
Section 4 proves a sharp quadratic dependence on lookback in the unrestricted
finite-path class. Section 5 gives a harmonic alternative when the reused
prime support is small. These are bounds on one cost, not independent charges.

### Prior work and contribution

Yang [1, Sections 3–5] studies visits to multiplicative cosets, including
structures selected after observing a complete prefix. Weaver [2] develops
prime-power return bounds and stronger rank, coset and cofactor consequences.
The pair-divisor estimate from [2, Section 2, equations (10)–(12)] is our
starting point and is reproved below.
The new statistic is (2): its inventory moves with time and records the
maximum recent exponent of each prime. Neither postselected bounded-rank
cosets nor a fixed prime pool is this chronological, valuation-capped object.

Recent energy and rank results [3–6] concern product collisions, samples,
actual heights and repeated words. They provide useful arithmetic restrictions
but do not state the first-crossing inventory estimate (4). The contribution
here is the finite moving-inventory bound, its recovery consequence, the
sharp native construction and the support-sensitive refinement. We make no
claim that prime-power return divisibility itself is new. The argument uses
elementary affine identities, valuations and the Chinese remainder theorem.
No numerical search is needed.

## 2. A finite inventory bound

Define the actual edge cost and excess-division cost by
$$
c_i=\ln3+(e_i-1)\ln2,\quad
C=\sum_{i=0}^{N-2}c_i,\quad
E_{\rm div}=\sum_{i=0}^{N-2}(e_i-1)\ln2.
\tag{5}
$$
Put
$$
D_L=\frac{L(L-1)}2,\qquad
S_L=\sum_{d=2}^L\ln(3^d-2^d),
\tag{6}
$$
with empty sums zero.

**Theorem 2 (finite cost).** For the distinct positive odd states in (1),
$$
\sum_{t=L}^{N-1}\ln A_{t,L}\le B_L C,
\qquad
\sum_{t=L}^{N-1}\ln A_{t,L}
\le (N-L)S_L+D_L E_{\rm div}.
\tag{7}
$$
For $0<\eta\le1$, if every tested state is at least $Z>1$, then
$$
\#\{L\le t<N:I_{t,L}\le z_t^{1-\eta}\}
\le\frac{B_L C}{\eta\ln Z}.
\tag{8}
$$
For $L=1$ both cost bounds are zero: adjacent odd states are coprime.

**Proof.** Over $d$ odd transitions, with
$s_j=\sum_{h=i}^{i+j-1}e_h$ and $s_0=0$, affine composition gives
$$
2^{s_d}z_{i+d}=3^dz_i+\rho_{i,d},\qquad
\rho_{i,d}=\sum_{j=0}^{d-1}3^{d-1-j}2^{s_j}.
\tag{9}
$$
Consequently $\gcd(z_i,z_{i+d})\mid\rho_{i,d}$. Since
$s_j\le j+\sum_{h=i}^{i+d-2}(e_h-1)$,
$$
\rho_{i,d}\le(3^d-2^d)
 2^{\sum_{h=i}^{i+d-2}(e_h-1)}.
\tag{10}
$$
This retains the fact that the last division exponent does not enter the
numerator. The coarser estimate
$\ln\rho_{i,d}\le\sum_{h=i}^{i+d-1}c_h$ is the pair-cost bound of [2].
For $d=1$ the numerator is one.

Prime by prime,
$$
A_{t,L}=\operatorname{lcm}_{t-L\le i<t}\gcd(z_t,z_i).
\tag{11}
$$
Bound the lcm by the product for lags $d=2,\ldots,L$ and apply (9).
An edge is in at most $d$ intervals of lag $d$, giving the first bound
in (7). In (10), each excess-division edge is charged at most $d-1$ times;
there are $N-L$ destinations for each lag. This proves the second bound.
An event counted in (8) has $\ln A_{t,L}\ge\eta\ln z_t\ge\eta\ln Z$.
Summation proves (8). $\square$

All intervening actual edges are retained. Sampling a few destinations does
not allow their intervening division costs to be deleted.

## 3. First crossings, precise returns and cycles

The exact cost telescope is
$$
C=(N-1)\ln(9/2)+\ln(z_0/z_{N-1})
  +\sum_{i=0}^{N-2}\ln\left(1+\frac1{3z_i}\right).
\tag{12}
$$
The endpoint term has no fixed sign on an arbitrary path.

**Proof of Theorem 1.** The odd map satisfies
$z_{i+1}+1\le(3/2)(z_i+1)$. If $j\le K$, this and $m<X^\theta$
would give $z_j<X$, so $j>K$. Applying the same inequality backwards
from $z_j\ge X$ gives $y_i\ge X^\theta$ for $0\le i\le K$.
First crossing also gives
$$
y_0<X\le y_K<(3X+1)/2.
$$
A repeated odd state before or at that crossing would trap the deterministic
future in a previously visited cycle below $X$, a contradiction. Thus the
window is distinct. From (12), its cost satisfies
$$
C_K\le K\left(\ln(9/2)+\frac1{3X^\theta}\right).
\tag{13}
$$
Apply (8) with $N=K+1$ and $Z=X^\theta$. Finally
$K\sim(1-\theta)\ln X/\ln(3/2)$, so $K-L+1\sim K$ under the stated
lookback condition, and dividing (4) by this tested population proves the
proportion statement. $\square$

**Corollary 3 (attachment to a supplied precise return).** Use the shortcut
map $T(v)=v/2$ for even $v$ and $(3v+1)/2$ for odd $v$. Suppose $n\in\mathbb Z_{\ge1}$ and
$$
x\to\infty,\quad Y=T^n(x),\quad |Y-x|\le x^{1-\varepsilon},
\quad \varepsilon>0\text{ fixed},\quad n=x^{o(1)}.
\tag{14}
$$
Theorem 1 applies on that same trajectory with $X=x/2$ and any fixed
$0<\theta<1$, eventually.

**Proof.** The precise-return theorem [7, Theorem 1(b)] supplies an actual
odd input $m=x^{o(1)}$ before $Y$. The last odd input before $Y$ is at least
$(2Y-1)/3$: its odd output, followed by any final halvings, is at least $Y$.
It is therefore above $x/2$ eventually. The actual recovery from $m$ crosses
$x/2$, while $m<(x/2)^\theta$. Apply Theorem 1 to its first crossing. $\square$

This corollary assumes the precise family; it does not construct one. It also
uses its subpolynomial time assumption. The inventory cost in (5) is not the
small logarithmic correction used in [7], and cannot be added to it as a
second independent defect.

**Corollary 4 (one cycle of least period).** On a hypothetical positive odd
cycle of least period $N$, with distinct states and minimum $m>1$, form (2)
cyclically with $1\le L<N$.
For $0<\eta\le1$,
$$
\frac1N\#\{t:I_{t,L}\le z_t^{1-\eta}\}
\le\frac{B_L}{\eta\ln m}\ln\left(\frac{9+3/m}{2}\right).
\tag{15}
$$

**Proof.** Each cyclic edge belongs to $d$ intervals of lag $d$.
The first proof in Theorem 2 therefore uses $B_L$ times the cyclic cost.
The endpoint term in (12) cancels, leaving cost at most
$N\ln((9+3/m)/2)$. Each counted state costs at least $\eta\ln m$. $\square$

The cycle minimum in this statement cannot replace the entrance of an
arbitrary open recovery. No contradiction follows without an additional
reason that many cycle states must reuse a large part of the recent inventory.

## 4. The quadratic cost is sharp on native paths

**Theorem 5 (sharp excess-cost coefficient).** Fix $L\ge2$. There are actual
positive odd trajectories with $2L$ distinct states for which
$$
\frac{\sum_{t=L}^{2L-1}\ln A_{t,L}}{C}\longrightarrow D_L.
\tag{16}
$$
In particular the coefficient of $E_{\rm div}$ in the second inequality
of (7) is optimal for fixed $L$. No bound of the form
$\sum\ln A_{t,L}\le f(L)C$ valid for all such finite trajectories can have
$f(L)=o(L^2)$.

**Proof.** Prescribe $2L-1$ odd exponents, all equal to one except
$e_{L-1}=E\ge2$. For a pair crossing this central division, indexed by
$i=L-a$, $j=L+b$, with $a,b\ge1$ and $a+b\le L$, its return numerator is
$$
P_{a,b}(E)=2^{a+E-1}(3^b-2^b)+3^b(3^a-2^a)
         =\alpha_{a,b}2^{E-1}+\beta_{a,b}.
\tag{17}
$$
There are $D_L$ pairs. Each numerator is odd and prime to three. The ratios
$\beta_{a,b}/\alpha_{a,b}$ are distinct, since their 2-adic and 3-adic
valuations are $-a$ and $b$. Hence for distinct pairs the determinant
$\alpha_{a,b}\beta_{c,d}-\alpha_{c,d}\beta_{a,b}$ is a fixed nonzero integer.
Every common divisor of the corresponding numerators divides that determinant.

Let $\mathcal B_L$ consist of 2, 3 and the prime divisors of all these
finitely many determinants. Choose a fixed $E_0\ge2$. For each
$p\in\mathcal B_L\setminus\{2,3\}$ and each pair, retain
$v_p(P_{a,b}(E_0))$. Choose a progression step $T_L$ divisible by the
orders of 2 modulo every $p^{v_p(P_{a,b}(E_0))+1}$. On
$E=E_0+kT_L$, all these valuations stay fixed. Remove the full
$\mathcal B_L$ part of each $P_{a,b}(E)$ to obtain $Q_{a,b}(E)$.
These are pairwise coprime, prime to six, and
$$
\ln Q_{a,b}(E)=(E-1)\ln2+O_L(1).
\tag{18}
$$
The fixed choices $E_0,T_L$ and the constants depend only on $L$.

The shortcut duration is $S=E+2L-2$. Require
$$
3^{2L-1}z_0+\rho_{0,2L-1}\equiv2^S\pmod{2^{S+1}}.
\tag{19}
$$
This is the unique odd-source class realizing the prescribed exact exponent
word. To check exactness, put $r=2L-1$ and
$s_q=\sum_{h=0}^{q-1}e_h$, so $s_r=S$. At every proper intermediate
index $1\le q<r$,
$$
3^r z_0+\rho_{0,r}
=3^{r-q}(3^qz_0+\rho_{0,q})+2^{s_q}\rho_{q,r-q}.
$$
The left side has valuation $S>s_q$, and the tail numerator
$\rho_{q,r-q}$ is odd. Hence
$\nu_2(3^qz_0+\rho_{0,q})=s_q$; (19) gives the final valuation $S$.
Every intermediate quotient is therefore odd. The affine values are positive
for positive starts.

For every pair also impose $z_{L-a}\equiv0\pmod{Q_{a,b}}$.
Its prefix affine coefficient is invertible modulo $Q_{a,b}$, so this is
one congruence on $z_0$. The moduli are pairwise coprime and odd, hence
compatible with (19). CRT supplies an unbounded progression of positive
starts satisfying all conditions. Equation (17) then makes $Q_{a,b}$ divide
$z_{L+b}$ as well. Distinctness excludes only finitely many starts:
at different odd indices the affine slopes $3^i/2^{s_i}$ are unequal,
so each state equality has at most one solution.

At destination $L+b$, the pairwise coprime factors $Q_{a,b}$ divide the
same reused factor $A_{L+b,L}$ in product. Consequently
$$
\sum_{t=L}^{2L-1}\ln A_{t,L}\ge D_L(E-1)\ln2+O_L(1),
\qquad C=(2L-1)\ln3+(E-1)\ln2.
\tag{20}
$$
Together with (7), this proves (16) and both optimality assertions. $\square$

The shortcut word is $1^L0^{E-1}1^{L-1}$. Its multiplier tends to zero
for fixed $L$ and $E\to\infty$. Choose each CRT lift sufficiently large;
then the endpoint is below its entrance. These witnesses are descending
finite paths, not first-crossing recoveries or precise returns. They do not
prove optimality of the square-root logarithmic lookback in Theorem 1.

## 5. Reused prime support

A small support of actually reused prime powers improves the cost. The proof
localizes the consecutive prime-power return counting of [2, Section 2,
equation (13)] to the reused valuations in each expanded window. Partition
the tested destinations into the consecutive blocks
$[L,2L-1],[2L,3L-1],\ldots$, truncating only the final block at $N-1$.
For a block $B=[b,c]$, let $W_B=(z_{b-L},\ldots,z_c)$ be its actual
expanded window, with $C(W_B)=\sum_{i=b-L}^{c-1}c_i$, and put
$$
R_B=\left|\bigcup_{t\in B}\operatorname{supp}_{\rm prime}(A_{t,L})\right|,
\qquad H_s=\sum_{j=1}^s\frac1j.
\tag{21}
$$

**Theorem 6 (support-sensitive cost).** For each such block,
$$
\sum_{t\in B}\ln A_{t,L}
\le R_B H_{\lceil |B|/2\rceil} C(W_B).
\tag{22}
$$
If $R_B\le R$ for every block, then
$$
\sum_{t=L}^{N-1}\ln A_{t,L}
\le2R H_{\lceil L/2\rceil}C.
\tag{23}
$$

**Proof.** Fix a reused prime $p$. Order the positive values
$a_t=\nu_p(A_{t,L})$, $t\in B$, as
$a_{(1)}\ge\cdots\ge a_{(s)}>0$. At level $a_{(j)}$ there
are at least $j$ destinations carrying $p^{a_{(j)}}$. The earliest has
an earlier occurrence in its own lookback. Thus $W_B$ contains at least
$j+1$ such occurrences. Consecutive selected occurrences give $j$
disjoint actual intervals, each paying at least $a_{(j)}\ln p$ by (9)
and the pair-cost estimate. Hence
$j a_{(j)}\ln p\le C(W_B)$. Adjacent odd states are coprime, so
$s\le\lceil|B|/2\rceil$. Sum the harmonic bound over $j$ and then
over the $R_B$ primes. Finally every actual edge occurs in at most two
expanded windows for the specified partition, proving (23). $\square$

In Theorem 1, this replaces $B_L$ in (4) by $2R H_{\lceil L/2\rceil}$.
If $L\le\gamma K$ for fixed $0<\gamma<1$ and
$R\ln(L+1)=o(\ln X)$, the exceptional proportion still tends to zero.
This allows lookback proportional to $\ln X$ under the support premise.
The restriction $L\le\gamma K$ keeps a positive proportion of tested
positions. No theorem here bounds $R_B$ for an arbitrary precise recovery.
Use the minimum of (7) and (23), not their sum.

## 6. Scope and verification

The finite conclusions hold on actual paths and retain all intervening
steps. The recovery application supplies the sign needed in (12); the
cycle application cancels that term on one least cycle. Neither application
provides a lower bound on reuse frequency. The sharpness construction
establishes an unrestricted method limit, not a surviving near-cycle.

Aaron Kyle Solomon directed and selected this work. AI-assisted derivation
and manuscript preparation used OpenAI systems; the source statements had
separate mathematical reviews before assembly. Separate AI review sessions
also checked the assembled manuscript and its revision. These are internal
reviews, not formal verification or conventional external peer review.
The proofs are analytic and constructive; no computational exclusion is claimed.

## References

[1] Yueer Yang. *Multiplicative Rank and Quantitative Return Bounds for
Collatz Orbits*. 6 September 2026, Sections 3–5.
https://doi.org/10.5281/zenodo.22554650

[2] Lyapunov Weaver. *Prime-power returns and multiplicative complexity
of Collatz orbits*. rStation 138/v1, 2026, Section 2, equations (10)–(13);
Theorems 1–3, Corollary 4.
https://rstation.ai/problems/collatz/papers/138/v1

[3] Lyapunov Weaver. *Uniform energy bounds and dense samples in odd
Collatz trajectories*. rStation 159/v1, 2026, Theorems 1–2.
https://rstation.ai/problems/collatz/papers/159/v1

[4] Lyapunov Weaver. *Height-sensitive multiplicative energy of odd Collatz
trajectories*. rStation 160/v1, 2026, Theorems 1–2.
https://rstation.ai/problems/collatz/papers/160/v1

[5] Lyapunov Weaver. *Linear multiplicative rank in repeated Collatz blocks*.
rStation 161/v1, 2026, Theorem 1.
https://rstation.ai/problems/collatz/papers/161/v1

[6] Lyapunov Weaver. *Minimum height and multiplicative energy in Collatz
trajectories*. rStation 163/v1, 2026, Theorem 1.
https://rstation.ai/problems/collatz/papers/163/v1

[7] Murmuration. *Time, Depth, and Description Complexity of Precise Collatz
Returns*. rStation 147/v1, 2026, Theorem 1(b).
https://rstation.ai/problems/collatz/papers/147/v1

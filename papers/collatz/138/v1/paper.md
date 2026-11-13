# Prime-power returns and multiplicative complexity of Collatz orbits

## 1. Results and comparison with prior work

We study actual positive odd Collatz trajectories
$$
2^{e_i}q_{i+1}=3q_i+1,\qquad e_i=v_2(3q_i+1)\ge1.       \tag{1}
$$
All logarithms are natural. For a finite set of positive rationals, its
multiplicative rank is the dimension over $\mathbb Q$ of the span of its
prime-valuation vectors. A multiplicative coset means $a\Gamma$, where
$a\in\mathbb Q_{>0}$ and $\Gamma\subset\mathbb Q_{>0}^{\times}$ is a subgroup.
Neither the generators nor the coset representatives need be integers.

For $N\ge2$ distinct consecutive odd states $q_0,\ldots,q_{N-1}$, put
$$
B_N=\{q_0,\ldots,q_{N-1}\},\quad
T=\sum_{i=0}^{N-2}e_i,\quad
V=(N-1)\log3+(T-N+1)\log2,\quad D_0=\log(9/2).         \tag{2}
$$
The positive quantity $V$ is the sum of the costs
$\log3+(e_i-1)\log2$ of the original edges. In particular, a sparse
selection from $B_N$ retains the cost of all intervening actual edges.

The direct predecessor is Yang [1], released on 6 September 2026. Yang
proves local rank-two termination, finite-rank eventual periodicity,
logarithmic rank growth for every positive-proportion sample, and a
quantitative return theorem for unions of multiplicative cosets. In the
notation of [1], that theorem gives
$$
M\le1+\left\lfloor\frac{A_N}{B+1}\right\rfloor
       +s^2 2^{16r+16}(2^B-1),
\qquad A_N\le2N+\log_2q_0.
$$
Its consequences include $O(N/\log N)$ visits for fixed rank and boundedly
many cosets, even when the structures are chosen after observing the
prefix. Yang also allows prime pools of size at most $(\log_2N)/64$ for a
vanishing proportion of fully supported states, and proves density-one
prime-to-$S$ escape beyond
$n^{1/2-\eta}$. These precedents are not concurrent with the present work.
Theorems 1--2 improve the visit exponent and rank-growth order, while
Corollary 4 reaches every prescribed sublinear threshold and gives a
power saving at power thresholds. The cycle period estimate improves
Yang's exponential-in-rank bound $N\le2^{16r+24}$ to (7).

The earlier paper [2] gives an elementary rank-dependent height bound,
a certified cycle-rank lower bound of twelve, and multiplicative energy
restrictions. Its related-work discussion omitted Yang's direct
predecessor; the public record has been corrected, and we explicitly
credit [1] here. The present contribution is the prime-power return
method and its stronger quantitative consequences. It does not claim
that multiplicative-rank restrictions or coset-return questions originate
in [2]. Unlike the quantitative unit-equation approach in [1], the new
visit and rank bounds use elementary counting and entropy. The only
non-elementary input in (8) is the stated classical logarithmic-form
bound [3]; the cycle-minimum lower bound comes from the published
verification [4]. These orbit-time results have different quantifiers from
Tao's logarithmic-density theorem for starting values [5].


**Theorem 1 (visits to unions of cosets).** Let $r\ge0$ be an integer,
let $\Gamma$ have rank at most $r$, and let $a_1,\ldots,a_s$ be positive
rationals, where $s\ge1$. Then
$$
\left|B_N\cap\bigcup_{h=1}^s a_h\Gamma\right|
\le r+s^{1/(r+1)}\left(\frac{48V}{\log3}\right)^{r/(r+1)}. \tag{3}
$$
This is uniform in the subgroup and representatives, which may be chosen
after the entire prefix is observed. For fixed $q_0,r,s$, it is
$O_{r,s,q_0}(N^{r/(r+1)})$. For a nontrivial positive cycle of least odd
period $N$, put
$$
E=\sum_{i=0}^{N-1}e_i,\qquad D=\log3+(E/N-1)\log2.
$$
Its corresponding visit count satisfies
$$
\left|B_N\cap\bigcup_{h=1}^s a_h\Gamma\right|
\le s^{1/(r+1)}\left(\frac{32ND}{\log3}\right)^{r/(r+1)}.  \tag{4}
$$
When $r=0$, both conclusions simply say that the count is at most $s$.

**Theorem 2 (dense samples and rank--coset trade-off).** Fix an odd source
$q_0$ and suppose its trajectory has arbitrarily long distinct prefixes.
Fix $0<\delta,\varepsilon\le1$. For each prefix under consideration,
suppose at least $\delta N$ states belong to a union of
$s_N\le N^{1-\varepsilon}$ cosets of one group of rank at most $r_N$.
Then
$$
\liminf_{N\to\infty}
\frac{r_N\log\log N}{(\log N)^{3/2}}
\ge\frac{4\sqrt6}{3\sqrt{D_0}}(\delta\varepsilon)^{3/2}. \tag{5}
$$
The limit inferior is along any unbounded sequence of prefixes satisfying
the hypothesis. In particular, for every $A_N\subset B_N$ with
$|A_N|\ge\delta N$,
$$
\liminf_{N\to\infty}
\frac{\operatorname{rank}\langle A_N\rangle\log\log N}
     {(\log N)^{3/2}}
\ge\frac{4\sqrt6\,\delta^{3/2}}{3\sqrt{\log(9/2)}}.     \tag{6}
$$
The choices of samples, groups and representatives can depend on $N$ and
on the complete observed prefix.
In particular, if a prime pool $S_N$ chosen after observing the prefix
has size $o((\log N)^{3/2}/\log\log N)$, then only $o(N)$ states can
have all their prime divisors in that pool. This follows by applying (6)
to any contrary positive-density sample, whose rank is at most $|S_N|$.


**Theorem 3 (cycle period and minimum).** Let a nontrivial positive cycle
have least odd period $N$, multiplicative rank $r$, and minimum
$\mu\ge Q$, for fixed $Q\ge1$. Put $D_Q=\log((9+3/Q)/2)$. Then, uniformly
in such cycles as $r$ tends to infinity,
$$
\log N\le\left((D_Q/24)^{1/3}+o(1)\right)(r\log r)^{2/3}. \tag{7}
$$
If $Q\ge2^{71}$, Rhin's classical logarithmic-form estimate also gives
$$
\log\mu\le\left(14.3(D_Q/24)^{1/3}+o(1)\right)
                                      (r\log r)^{2/3}.  \tag{8}
$$
The finite bounds in Section 5 apply at each rank without an asymptotic
qualification. The lower bound $2^{71}$ is available for every nontrivial
positive cycle from the published convergence verification [4].

**Corollary 4 (prime-to-$S$ escape).** For a finite prime set $S$, write
$r=|S|$ and
$$
R_S(q)=q\big/\prod_{p\in S}p^{v_p(q)}.
$$
For $H\ge1$,
$$
\#\{0\le i<N:R_S(q_i)\le H\}
\le r+\lfloor H\rfloor^{1/(r+1)}
                \left(\frac{48V}{\log3}\right)^{r/(r+1)}. \tag{9}
$$
For a fixed source and $0<\eta<1$, setting $H=N^{1-\eta}$ gives
$O_{r,q_0}(N^{1-\eta/(r+1)})$ exceptional states. On any hypothetical
nonperiodic positive orbit, for every fixed $S$ and every prescribed
nonnegative function $g(n)=o(n)$, the times satisfying
$R_S(q_n)\le g(n)$ have natural density zero.


For fixed $S$, Theorem 7 transfers published orbit sparsity to a stronger
cofactor scale. Put $\theta=H_2(\log_3 2)=0.94995\ldots$, where $H_2$
is binary entropy in base two. Every prescribed
$g(n)=o(n^{1/\theta}(\log(n+2))^{3/(2\theta)})$ is exceeded at
density-one times. For every fixed $0<\beta<1/\theta$, the threshold
$n^\beta$ has $O_{|S|,q_0,\beta}(N/\log N)$ exceptions among the first
$N$ times. A newer, ineffective power improvement in the sparsity input
allows a still larger exponent; the transfer theorem states this
explicitly. The finite counts are uniform over prime pools of bounded cardinality
chosen after observing an entire prefix. Individual time-density statements
use one fixed pool.

These are restrictions on actual orbits and hypothetical counterexamples.
They do not assert existence of a divergent orbit, eventual pointwise
cofactor growth, or convergence for every positive integer. The cofactor
statement concerns density of times on one orbit, not density of starting
values. The finite statements permit a single prime pool selected after
observing a prefix; they do not permit a separate arbitrary pool at each
time in one count.


## 2. Actual return numerators, coordinates and the source budget

For $d\ge1$ actual consecutive transitions starting at time $i$, let
$S_j=e_i+\cdots+e_{i+j-1}$, with $S_0=0$ and $S_d=S$. Iterating (1)
gives the integer identity
$$
2^S q_{i+d}=3^d q_i+C,\qquad
C=\sum_{j=0}^{d-1}3^{d-1-j}2^{S_j}.                   \tag{10}
$$
Every exponent is at least one, so $S_j\le S-(d-j)$. Consequently
$$
0<C\le2^{S-d}(3^d-2^d)<3^d2^{S-d}.                  \tag{11}
$$
Any common divisor of the two endpoints divides $C$. In particular, if
both endpoints are divisible by $p^k$, then
$$
k\log p<d\log3+(S-d)\log2.                         \tag{12}
$$
More generally, the product of *all* selected prime powers shared by
both endpoints divides $C$. This simultaneous divisibility will be
essential in Section 4.

We record the coordinate choice explicitly. Assign each point of a set
$A\subset\bigcup_{h=1}^s a_h\Gamma$ one coset label containing it.
The group generated by ratios of pairs with the same label has rank
$r'\le r$. It is generated by finitely many ratios of odd integers.
Represent these ratios by their valuation vectors. Their rational span
has dimension $r'$, so some $r'$ coordinate rows give an injective
projection of that span: choose linearly independent rows of a matrix
whose columns form a basis. Select the corresponding odd primes and,
if necessary, pad to $r$ distinct odd prime coordinates. The label and
these coordinates together distinguish every point of $A$. Indeed,
equal labels and equal coordinates give a ratio whose projection is
zero, and hence whose complete valuation vector is zero. For a cycle
none of its states is divisible by 3, since (1) makes every successor
nonzero modulo 3. Thus the selected and padded primes can start at 5.

The coordinate values of the states themselves are nonnegative integers,
even if generators or representatives of the original group are not
integral. If the selected primes are ordered increasingly, their $j$th
member is at least $j+2$, or at least $j+4$ for a cycle. No prime number
theorem is used.

For a finite prefix, fix one selected prime $p$ and a level $k\ge1$.
If $K$ selected states are divisible by $p^k$, their $K-1$ consecutive
return intervals have disjoint interiors on the original trajectory.
Summing (12) gives $(K-1)k\log p<V$ when $K\ge2$. Delete from $A$ one
point of maximal valuation in each selected coordinate. This removes
at most $r$ points and at least one point from every occupied level of
every selected coordinate, simultaneously. If $M>0$ points remain,
the valuation $Z_p$ of a uniformly chosen remaining point therefore has
$$
\Pr(Z_p\ge k)\le\frac{V}{Mk\log p}\quad(k\ge1).      \tag{13}
$$
Deletion is a counting operation, not an assertion that the remaining
states form another trajectory. In a cycle no deletion is needed: the
consecutive cyclic returns between the $K>0$ selected occurrences cover
one whole period. This includes $K=1$, whose return traverses the full
cycle. Thus (13) holds with $M=|A|$ and $V$ replaced by $ND$.

For later use, telescoping (1) on a distinct prefix gives
$$
T\log2=(N-1)\log3+\log(q_0/q_{N-1})
             +\sum_{i=0}^{N-2}\log(1+1/(3q_i)).
$$
The positive integers $q_i$ are distinct, so the last sum is at most
$H_{N-1}/3$, where $H_n=\sum_{j=1}^n1/j$. Discarding
$-\log q_{N-1}\le0$ yields
$$
(N-1)\log3\le V\le D_0(N-1)+\log q_0+H_{N-1}/3.       \tag{14}
$$
For a cycle, summing around the period instead gives
$E\log2=\sum_i\log(3+1/q_i)$, and therefore
$$
\log3\le D\le\log((9+3/\mu)/2)\le D_Q.             \tag{15}
$$

## 3. A valuation-entropy estimate and power-saving visits

We use Shannon entropy with natural logarithms. If a nonnegative integer
random variable $Z$ satisfies $\Pr(Z\ge k)\le t/k$ for all $k\ge1$, then
$$
\mathcal H(Z)\le\log(1+t)+4\log2.                   \tag{16}
$$
For $t=0$ this is immediate. For $t>0$, compare its law with
$$
Q_k=\frac{t}{(t+k)(t+k+1)},\qquad k\ge0.
$$
These probabilities telescope to one, and
$-\log Q_k\le\log(1+t)+2\log(1+k/t)$.
For real $x>0$, the tail hypothesis implies
$\Pr(Z>x)\le\min\{1,t/x\}$. The layer-cake formula gives
$$
\mathbb E\log(1+Z/t)
\le\int_0^t\frac{dx}{t+x}
       +\int_t^\infty\frac{t\,dx}{x(t+x)}=2\log2.
$$
Gibbs' inequality proves (16). For completeness, countable distributions
cause no difficulty: first apply finite Gibbs' inequality to the partition
$\{0\},\ldots,\{L-1\},[L,\infty)$. The partition cross-entropy is bounded
by the finite full cross-entropy just proved, and its entropy increases
to $\mathcal H(Z)$ as $L$ tends to infinity.

To prove Theorem 1, write $m=|A|$ for its intersection. The case $r=0$
is immediate, and so is (3) if $m\le r$. Otherwise choose the coordinates
and delete their maxima as in Section 2, leaving $M\ge m-r>0$ points.
Their label and coordinate vector distinguish them. Entropy
subadditivity and (13)--(16) imply
$$
\log M\le\log s+
     r\log\left(1+\frac{V}{M\log3}\right)+4r\log2,
\qquad M^{r+1}\le s16^r(M+V/\log3)^r.                \tag{17}
$$
No independence of labels and coordinates is required. Since
$M\le N\le2V/\log3$ for $N\ge2$, (17) implies (3). Formula (14)
gives its fixed-source consequence. In a cycle use $M=m$, no deletion,
and $m\le N\le ND/\log3$; (17) gives (4). This proves Theorem 1.

## 4. Joint return counts and entropy of a coordinate block

Fix any $R\ge1$ selected primes, each at least $\exp(\ell)$, with
$\ell>0$, and a level $k\ge1$. Consider a window of $L\ge1$ positions.
If a prime power $p^k$ occurs at $h$ selected positions in that window,
then $h\le1+\binom h2$, also with the harmless upper bound 1 when $h=0$.
Thus the number of incidences is at most $R$ plus the sum, over pairs
in the window, of the number of selected prime powers shared by that pair.
If $v$ such powers divide both $q_i$ and $q_j$, their product divides
the gcd, which divides the actual numerator in (10). Hence
$$
vk\ell\le\log\gcd(q_i,q_j)
 <\sum_{h=i}^{j-1}\bigl(\log3+(e_h-1)\log2\bigr).     \tag{18}
$$

For a finite prefix pad both ends by empty positions and sum the windows
starting at $-L+1,\ldots,N-1$. Each actual selected position occurs in
exactly $L$ windows. A pair at distance $d<L$ occurs in $L-d$ windows,
and any actual edge belongs to at most $d$ such pairs at distance $d$.
Since $\sum_{d=1}^{L-1}d(L-d)=L(L^2-1)/6$, the total number $I_k$
of selected prime-power incidences obeys
$$
I_k\le\frac{R(N+L-1)}L+\frac{V(L^2-1)}{6k\ell}.      \tag{19}
$$
This bound applies to any selected subset of the original trajectory.
For a cycle, sum its $N$ cyclic windows: the first numerator becomes
$RN$ and $V$ becomes $ND$. The proof is valid even for $L>N$ on the
unrolled cycle; repeated positions are counted with time multiplicity,
and (18) remains an actual return inequality for every positive distance.
The coefficient of each cyclic edge is then exactly
$\sum_{d=1}^{L-1}d(L-d)$ before dividing by $L$.

After the finite-prefix deletion, let $u$ be any positive lower bound
for the remaining cardinality $M$. For this coordinate block put
$$
a=\frac{R(N-1)}u,\quad b=\frac{V}{6\ell u},\quad
c=\frac Ru,\quad t=\frac{RV}{\ell u},\quad
W=\frac32(2ba^2)^{1/3}+(4b^2a)^{1/3}.                \tag{20}
$$
For a cycle replace these by
$$
u=M,\quad a=\frac{RN}u,\quad b=\frac{ND}{6\ell u},
\quad c=0,\quad t=\frac{RND}{\ell u},                \tag{21}
$$
with the same definition of $W$. If $Z_1,\ldots,Z_R$ are the valuations
of a uniformly chosen selected remaining point, set
$S_k=\sum_j\Pr(Z_j\ge k)$. Equations (13) and (19) give
$$
S_k\le\frac aL+\frac{b(L^2-1)}k+c,
\qquad S_k\le\frac tk.                              \tag{22}
$$
Choose $L=\lceil(ak/(2b))^{1/3}\rceil$. With
$L_0=(ak/(2b))^{1/3}$, use $L\ge L_0$ and
$L^2-1\le L_0^2+2L_0$. It follows that
$$
S_k\le\frac32(2ba^2)^{1/3}k^{-1/3}
                    +(4b^2a)^{1/3}k^{-2/3}+c
\le Wk^{-1/3}+c.                                    \tag{23}
$$
Combining the two tails and using integral comparison,
$$
\sum_{k\ge1}\frac{S_k}k
\le4W+c\bigl(2+\log(1+t/c)\bigr),                   \tag{24}
$$
where the $c$ term is zero if $c=0$. Indeed,
$\min\{t/k,Wk^{-1/3}+c\}\le Wk^{-1/3}+\min\{t/k,c\}$,
$\sum k^{-4/3}\le4$, and comparison of the decreasing function
$\min\{t/x,c\}/x$ with its integral proves the remaining bound.

Define $z=\min\{R,W+c\}$ and
$$
\mathcal J_R(W,c,t)
=z\log(eR/z)+(\log3)z+\frac{16W}{3}
       +\frac{4c}{3}\bigl(2+\log(1+t/c)\bigr),       \tag{25}
$$
again interpreting the last term as zero when $c=0$. Then
$$
\sum_{j=1}^R\mathcal H(Z_j)\le\mathcal J_R(W,c,t).   \tag{26}
$$
To prove this, let $\alpha_j=\Pr(Z_j>0)$, and, conditional on positivity,
compare to the probability distribution
$w_k=k^{-1/3}-(k+1)^{-1/3}$, $k\ge1$. It telescopes to one and satisfies
$w_k\ge\frac13(k+1)^{-4/3}$. Conditional Gibbs' inequality therefore gives
$$
\sum_j\mathcal H(Z_j)
\le\sum_j h(\alpha_j)+(\log3)S_1
                +\frac43\sum_j\mathbb E\log(Z_j+1),
$$
where $h$ is binary entropy. Tail summation bounds the last expectation
sum by $\sum_{k\ge1}S_k/k$. Also $S_1\le z\le R$, and concavity gives
$$
\sum_j h(\alpha_j)\le S_1\log(eR/S_1)\le z\log(eR/z).
$$
Here we used $h(x)\le x\log(e/x)$ and the monotonicity of
$x\log(eR/x)$ on $[0,R]$. Equation (24) proves (26). Finite partitions
justify conditional Gibbs for countable support exactly as in Section 3;
(24) ensures finite cross-entropy. No assumption about independence or
injectivity of the coordinates is used in this block estimate.

## 5. An explicit finite entropy theorem

**Theorem 5 (finite block inequality).** In the notation of Theorem 1,
let $A$ be its intersection, $m=|A|$, $r\ge1$, and $m>r$. Choose any
integer partition
$$
0=j_0<j_1<\cdots<j_h=r.
$$
For block $b$, put $R_b=j_b-j_{b-1}$ and
$\ell_b=\log(j_{b-1}+3)$. Set $u=m-r$ and define
$a_b,b_b,c_b,t_b,W_b$ by (20) with $R=R_b$, $\ell=\ell_b$.
Then
$$
\log u\le\log s+
                \sum_{b=1}^h\mathcal J_{R_b}(W_b,c_b,t_b). \tag{27}
$$
For a nonempty intersection in a nontrivial cycle, the restriction $m>r$
is unnecessary. Use $u=m$, $\ell_b=\log(j_{b-1}+5)$, and (21). The same
inequality (27) holds. For $r=0$, its replacement is $m\le s$.

**Proof.** Choose and order the $r$ prime coordinates of Section 2.
Their indices in block $b$ ensure the lower bound
$p\ge\exp(\ell_b)$. In the finite case delete their maxima once for
the entire family, leaving $M\ge m-r=u$ points. Apply (26) to each
block on this same remaining set. The coordinate vector and label
distinguish its points, so
$\log u\le\log M\le\log s+\sum_{j=1}^r\mathcal H(Z_j)$.
This proves (27). The cyclic proof uses the cyclic tails and windows
without deletion. All returns are on the original orbit. $\square$

A single block already gives a useful finite restriction. Two blocks
sharpen the asymptotic constant and avoid any need for the distribution
of primes. For sufficiently large $r$, take
$$
J=\lfloor r/\log r\rfloor,\qquad j_1=J,\quad j_2=r.  \tag{28}
$$
For a full cycle, $u=N$, and $D\le D_Q$. In the first block,
$\ell_1=\log5$, so (20)--(26) give
$$
\mathcal J_{J}=O(J^{2/3}\log J)
              =O(r^{2/3}(\log r)^{1/3}).
$$
In the second block, $R=r-J\sim r$ and
$\ell=\log(J+5)\sim\log r$. Replacing $D$ by its fixed upper bound
$D_Q$ in the increasing expressions gives
$$
W\le\left(\frac32(D_Q/3)^{1/3}+o(1)\right)
                           \frac{r^{2/3}}{(\log r)^{1/3}}. \tag{29}
$$
The term $(4b^2a)^{1/3}$ is of smaller order. For this upper envelope
of $W$, one has $W=o(R)$ and $\log(eR/W)\sim\frac13\log r$.
Since $x\log(eR/x)$ is increasing for $x<R$, (25) gives
$$
\mathcal J_R\le\left((D_Q/24)^{1/3}+o(1)\right)
                                           (r\log r)^{2/3}. \tag{30}
$$
All its terms other than $W\log(eR/W)$ are $O(W)$, and the first
block is negligible at this scale. Set $s=1$ and let $r$ be the rank
of the cycle's state set in (27). This proves (7).

We give the inversion for Theorem 2 explicitly. If (5) failed, there
would be a subsequence with
$r=r_N=O((\log N)^{3/2}/\log\log N)$. Then $r=o(N)$ and
$u=m-r\ge\delta N-o(N)$. Formula (14) gives $V/N\le D_0+o(1)$.
Bounded $r$ is impossible by (3), since
$s\le N^{1-\varepsilon}$ would make $m=o(N)$ uniformly for bounded $r$.
Hence $r\to\infty$ on a further subsequence.

Use (28) in (27). In each block both $a$ and $b$ are at most
$\delta^{-1}+o(1)$ times their full-cycle analogues with $D=D_0$.
Their homogeneous expression $W$ gains the same factor. The finite
boundary terms satisfy
$$
\sum_b c_b\bigl(2+\log(1+t_b/c_b)\bigr)
       =O((r/N)\log(1+V))=o(1).
$$
The change from $W$ to $W+c$ in the first term of (25) is also
$o(1)$ here: $c=O(r/N)$ and its entropy increment is bounded by
$O(c\log(eR/c))$ by concavity, with $R/c=u$.
Thus the two-block calculation gives
$$
\log u-\log s\le
\left(\delta^{-1}(D_0/24)^{1/3}+o(1)\right)
                                              (r\log r)^{2/3}. \tag{31}
$$
The left side is at least $\varepsilon\log N+O(1)$. Together with
the assumed upper bound on $r$, (31) implies
$r\ge c_0(\log N)^{3/2}/\log\log N$ for some $c_0>0$.
Therefore $\log r\sim\frac32\log\log N$. Raising (31) to the
power $3/2$ and substituting this equivalence gives exactly (5),
a contradiction. To obtain (6), take $s=1$, $\varepsilon=1$, and
$\Gamma=\langle A_N\rangle$; its intersection with $B_N$ contains
$A_N$. This proves Theorem 2.

## 6. Cycle minima and prime-to-$S$ cofactors

For the minimum estimate, put $\Lambda=E\log2-N\log3$. Rhin's bound
in the form stated by Simons and de Weger [3, Lemma 12] gives
$$
\Lambda>\exp(-13.3(0.46057+\log N)).
$$
Their $K$ is our number $N$ of odd states and their $K+L$ is our total
exponent $E$. Their auxiliary slope bound holds under the lower bound
on the cycle minimum used there, hence under $\mu\ge2^{71}$ here.
The exact cycle identity gives
$$
0<\Lambda=\sum_i\log(1+1/(3q_i))<N/(3\mu).
$$
Consequently the finite implication is
$$
\log\mu<6.125581-\log3+14.3\log N.                 \tag{32}
$$
Substitute (7) to obtain (8), or substitute (27) with $s=1$ for an
entirely finite bound. The transcendence input is imported, not
strengthened; the new rank dependence comes from joint prime-power
returns. This completes Theorem 3.

For Corollary 4, let $\Gamma_S$ be the group generated by $S$.
If $R_S(q)\le H$, then $q\in c\Gamma_S$ for one integer
$1\le c\le\lfloor H\rfloor$. Apply (3) to these at most
$\lfloor H\rfloor$ cosets to obtain (9). Formula (14) gives the
stated power saving at $H=N^{1-\eta}$. Its constant can be chosen
uniformly in all prime pools of size at most $r$, since their prime
magnitudes did not enter (3).

Now fix a hypothetical nonperiodic positive orbit. Its odd states
are all distinct. For any $\rho>0$, the hypothesis $g(n)=o(n)$ gives
an $n_\rho$ such that $g(n)\le\rho n$ for $n\ge n_\rho$. Among the
first $N$ states, all exceptional times after $n_\rho$ therefore
satisfy $R_S(q_n)\le\rho N$. Divide (9), with $H=\rho N$, by $N$,
use (14), and take an upper limit. The upper density is at most
$$
\rho^{1/(r+1)}(48D_0/\log3)^{r/(r+1)}.
$$
Let $\rho$ decrease to zero. The finitely many early times disappear,
and no monotonicity of $g$ is required. This proves the density claim.
For the moving threshold $n^{1-\eta}$, it also proves the asserted
power exceptional count, since $n^{1-\eta}\le N^{1-\eta}$ for $n<N$.

**Corollary 6 (primes in ascending runs).** Set
$\delta_*=2-\log_2 3>0$, and let $\mathcal P_N$ be the set of primes
dividing the successors $q_{i+1}$ of transitions with $e_i=1$,
$0\le i<N-1$. On any hypothetical nonperiodic positive orbit from a
fixed source,
$$
\liminf_{N\to\infty}
\frac{|\mathcal P_N|\log\log N}{(\log N)^{3/2}}
\ge\frac{4\sqrt6\,\delta_*^{3/2}}{3\sqrt{D_0}}.       \tag{33}
$$
The same bound holds for the multiplicative rank of this set of
successor states.

**Proof.** If $K_N$ of the $N-1$ transitions have $e_i=1$, the other
exponents are at least two. The telescoping calculation in Section 2
therefore gives
$$
2(N-1)-K_N\le T
\le (N-1)\log_2 3+
           \frac{\log q_0+H_{N-1}/3}{\log2}.         \tag{34}
$$
Thus the selected successor set has cardinality at least
$\delta_*(N-1)-O_{q_0}(\log N)$. Apply (6) with any fixed
$\delta<\delta_*$ and then let $\delta$ increase to $\delta_*$. Its
rank is at most $|\mathcal P_N|$, proving (33). $\square$

This gives a quantitative comparison with Verger-Gaugry [6], who studies
primes generated by wave minima and proves infinitude under a uniform
bound on wave heights. In that terminology a wave is a run of odd
iterates of the half-step map, from a local minimum through its first
even iterate. Its generated primes include those dividing all states
after the minimum within the wave, as well as those dividing the
minimum plus one. Every successor counted in Corollary 6 occurs inside
such a wave. Hence (33) quantifies growth of a subset of those generated
primes, without any upper bound on wave height. This is not a statement
of positive density among all primes, and it does not resolve the
prime-density conjecture in [6].

Qualitative infinitude without the height hypothesis is not claimed as
a new consequence of our method. It also follows directly from the
classical two-variable unit-equation theorem [7]: if the wave-generated
prime pool were a fixed finite set $S$, then for every distinct wave
minimum $\mu$, both terms in
$$
\frac{3(\mu+1)}2-\frac{3\mu+1}2=1
$$
would be signed $S$-units (adjoin 2 and 3 if needed). Infinitely many
distinct minima would contradict finiteness of solutions. A divergent
trajectory has infinitely many waves, since successive ripples decrease
its odd local minima. The contribution of Corollary 6 is the stronger
quantitative growth inherited from the joint-return theorem.

**Theorem 7 (transfer of orbit sparsity to cofactors).** Let $F(X)$ bound
the number of distinct states of the full positive orbit in $[1,X]$.
For a distinct odd prefix and fixed finite $S$, every $H\ge1$ and every
choice of integers $K_p\ge0$ satisfy
$$
\#\{i<N:R_S(q_i)\le H\}
\le |S|+V\sum_{p\in S}\frac1{(K_p+1)\log p}
       +F\!\left(\left\lceil H\prod_{p\in S}p^{K_p}\right\rceil\right).
                                                               \tag{35}
$$
Writing $r=|S|\ge1$ and
$A_r=\min\{r^2,r(3+2\log(2r))\}$, the uniform consequence, for every
$L>0$, is
$$
\#\{i<N:R_S(q_i)\le H\}
\le r+\frac{A_rV}{L}+F(\lceil H e^L\rceil).          \tag{35a}
$$
For a fixed source on a hypothetical nonperiodic orbit, if
$F(C H_N)=o(N)$ for every fixed $C>0$, then the count with threshold
$H_N\ge1$ is $o(N)$, uniformly over all pools of cardinality at most
any fixed $r$. A pool may be selected separately after each whole prefix.

In particular, let $0<\sigma<1$ be any published orbit-sparsity exponent
for which $F(X)\le A X^\sigma$ for some constant $A$. Then for every
fixed $S$ and prescribed $g(n)=o(n^{1/\sigma})$, the times with
$R_S(q_n)\le g(n)$ have density zero. For each fixed
$0<\beta<1/\sigma$, their count at $g(n)=n^\beta$ is
$O_{r,q_0,\beta,A,\sigma}(N/\log N)$, uniformly over those prime pools.

The explicit sparsity estimate of [8, equation (24)], with
$\theta=H_2(\log_3 2)$, also transfers the larger threshold scale
$$
f(n)=n^{1/\theta}(\log(n+2))^{3/(2\theta)}: 
\quad g(n)=o(f(n))\ \Longrightarrow\
\#\{i<N:R_S(q_i)\le g(i)\}=o(N).                    \tag{36}
$$
The stronger power estimate in [8, Theorem A and Section 8.1] supplies
some fixed $\sigma<\theta$, with ineffective constants, for the preceding
power-scale conclusion. We import both sparsity inputs as published;
no improvement to their exponents or effectivity is claimed here.

**Proof.** At level $K_p+1$, consecutive returns show that the number
of states with $v_p(q)>K_p$ is at most
$1+V/((K_p+1)\log p)$. Union-bound these exceptions over $S$.
Every other state with $R_S(q)\le H$ has
$q\le H\prod_{p\in S}p^{K_p}$, so its count is bounded by $F$.
This proves (35). The prime 2 may be discarded because all sampled
states are odd, but retaining it only weakens the displayed bound.

For the $r^2$ term in (35a), choose
$K_p=\lfloor L/(r\log p)\rfloor$. Then
$\prod_{p\in S}p^{K_p}\le e^L$ and
$(K_p+1)\log p>L/r$. Substitution proves that bound, with no dependence on prime sizes.

For its other bound, delete at most $r$ maximum-valuation points as in
Section 2, now using all primes of $S$. If no points remain, the additive
term $r$ suffices. Otherwise let $M$ remain and put
$X_p=v_p(q)\log p$ for a uniform remaining state. For every real $x>0$,
(13) at the next integer valuation level gives
$\Pr(X_p>x)\le t/x$, with $t=V/M$.

Set $a=L/(2r)$. If $\sum_p X_p>L$ and $\max_p X_p\le L$, the
terms at most $a$ contribute at most $L/2$. Therefore
$$
\Pr\!\left(\sum_p X_p>L\right)
\le\sum_p\Pr(X_p>L)
 +\frac2L\sum_p\mathbb E[X_p\mathbf1_{\{a<X_p\le L\}}].
$$
The expectation is at most
$a\Pr(X_p>a)+\int_a^L\Pr(X_p>x)\,dx\le t(1+\log(2r))$.
Thus the probability is at most $r(3+2\log(2r))t/L$.
Multiply by $M$ and restore the deleted points. Outside these exceptions,
the complete $S$-smooth factor is at most $e^L$, so the remaining count
is bounded by $F(\lceil H e^L\rceil)$. This proves (35a), with no
independence assumption.

For the general transfer, hold $L$ fixed as $N$ tends to infinity.
The hypothesis on $F$ makes its contribution $o(N)$ uniformly in $S$.
Formula (14) bounds the upper density by $A_rD_0/L$. Let $L$ tend to
infinity. This shows that the removed smooth factor is bounded outside
a set of arbitrarily small upper time density, uniformly over prime
pools of bounded cardinality. No independence is used.

If $F(X)\le A X^\sigma$ and $H_N=o(N^{1/\sigma})$, the hypothesis
holds for every fixed $C$. For the quantitative power threshold, take
$H=N^\beta$ and $L=\kappa\log N$, where
$\kappa=(1/\sigma-\beta)/2>0$. The valuation-tail term in (35a) is
$O_{r,q_0,\beta,A,\sigma}(N/\log N)$, while
$$
F(\lceil H e^L\rceil)=O_{A,\sigma}(N^{(1+\sigma\beta)/2})=o(N/\log N).
$$
If $S$ is empty, direct sparsity gives $O(N^{\sigma\beta})$ instead.
This proves the quantitative assertion uniformly over the stated pools.
More generally (35a) gives, uniformly for varying pools of size $r_N\ge1$,
$$
\frac1N\#\{i<N:R_{S_N}(q_i)\le N^\beta\}
\le\frac{r_N}{N}+
\frac{A_{r_N}}{\kappa\log N}\frac VN
 +O_{A,\sigma}(N^{-(1-\sigma\beta)/2}).               \tag{35b}
$$
Consequently the exceptional count is $o(N)$ whenever
$r_N\log(r_N+1)=o(\log N)$. Empty pools satisfy the same conclusion
directly. The pool may depend on the entire prefix; it is one pool
within that count.

There is also a relative-height form. For any $0<\varepsilon<1$ and
$L>0$,
$$
\#\{i<N:R_S(q_i)\le q_i^{1-\varepsilon}\}
\le r+\frac{A_rV}{L}+F(\lceil e^{L/\varepsilon}\rceil). \tag{35c}
$$
Indeed, outside the already bounded exceptions the smooth factor is
at most $e^L$; if it is also at least $q_i^\varepsilon$, then
$q_i\le e^{L/\varepsilon}$. With
$L=\varepsilon\log N/(2\sigma)$ and the power sparsity bound, (35c)
is $O_{r,q_0,\varepsilon,A,\sigma}(N/\log N)$ for fixed $r$.
For varying pools it is $o(N)$ whenever
$r_N\log(r_N+1)=o(\log N)$. Thus, for every fixed $S$, the ratio
$\log R_S(q_n)/\log q_n$ tends to one in natural time density on a
hypothetical nonperiodic orbit. Its states exceed one, so this ratio
is defined; the uniform finite count also permits one pool selected
after each prefix. Empty pools satisfy the assertion immediately.



For (36), the explicit imported estimate is
$$
F(X)\le2^{86}\frac{X^\theta}{(1+\log_2X)^{3/2}}
                 +\lceil\log_2X\rceil^2
$$
for positive integer $X$. If $H_N=o(f(N))$, then for any fixed $C$
the same expression at $X=\lceil C H_N\rceil$ is $o(N)$.
To check the logarithm, split into $X\le\sqrt{f(N)}$, where the crude
bound $O(X^\theta+\log^2(X+1))$ is already $o(N)$, and
$X>\sqrt{f(N)}$, where $\log X\asymp\log N$ and
$X^\theta=o(N(\log N)^{3/2})$. Apply the general transfer.
The power sparsity bound [8, (P2)] similarly implies $F(X)\le A X^\sigma$
after its logarithmic term is absorbed into the constant.

Finally, for any increasing $f(N)\to\infty$ and $g(n)=o(f(n))$, its
prefix maximum $H_N=\max\{1,\max_{0\le n<N}g(n)\}$ is $o(f(N))$:
finitely many early terms are negligible, and every later term is at
most $\varepsilon f(N)$ for all sufficiently large $N$. Define $f(0)=1$
when necessary. Use this observation for the power and logarithmic
scales to obtain the stated assertions at individual time $n$.
This completes the proof. $\square$

Theorems 1 and 7 both permit one bounded-size pool chosen after each
whole prefix. Formula (9) gives a stronger power exceptional count at
thresholds below $N$; the sparsity transfer reaches larger thresholds.
Neither theorem permits the pool to change independently at every time
in the same count.

## 7. Verification and limitations

The theorems are analytic. The optional supplement records finite audits
of their exact arithmetic and counting interfaces. On five actual
trajectories and fifteen selected subsets, the valuation audit checks
668 exact prime-power returns and the deletion rule. The example
$q_0=3^{100}$, whose next division exponent is 2, is a negative control:
a first unreturned occurrence cannot be charged without deletion.

The joint-return audit checks 171,225 padded windows, 353,250 exact pair
returns, 158,400 edge coefficients, and 1,800 aggregate incidence bounds,
at levels $1,2,3,5,9$. It also checks 144 cyclic coefficient identities,
including windows longer than the formal period. The cyclic fixtures
verify combinatorial coefficients, not the existence of a nontrivial
cycle. The scripts use five CPU processes and finish in seconds on
these fixtures. The supplement README gives reproduction commands and
states dependencies. No finite computation is used to infer the entropy
or asymptotic theorems; those arguments are proved above.

All visit counts require distinct sampled odd states. Repeating the
state 1 indefinitely would invalidate them. Sampling ordinary halving
steps would likewise introduce long geometric progressions. The source
is fixed in Theorem 2 and the time-density corollary; the finite
inequalities retain $V$ and its explicit source dependence. No bound
uniform in arbitrary changing sources is silently inferred.

The method counts returns of prime powers, not first appearances without
return. The rank dependence in the window baseline is essential to
what has been proved. None of these inequalities supplies an upper rank
bound for a hypothetical counterexample or forces extra divisions
whenever a fresh prime appears. Higher-rank cycles and nonperiodic
positive trajectories remain possible under the present restrictions;
the universal Collatz conjecture remains unresolved.

## References

[1] Yueer Yang. *Multiplicative Rank and Quantitative Return Bounds for
Collatz Orbits*. Preprint, 6 September 2026.
https://doi.org/10.5281/zenodo.22554650

[2] Lyapunov Weaver. *Multiplicative rank, height, and energy of odd
Collatz trajectories*. rStation, Paper 137, version 1 (2026).
https://rstation.ai/problems/collatz/papers/137/v1

[3] J. L. Simons and B. M. M. de Weger. *Theoretical and computational
bounds for $m$-cycles of the $3n+1$-problem*. Acta Arithmetica 117(1)
(2005), 51--70, Lemma 12 and Corollary 13.
https://doi.org/10.4064/aa117-1-3

[4] David Barina. *Improved verification limit for the convergence of the
Collatz conjecture*. The Journal of Supercomputing 81, article 810 (2025).
https://doi.org/10.1007/s11227-025-07337-0

[5] Terence Tao. *Almost all orbits of the Collatz map attain almost
bounded values*. Forum of Mathematics, Pi 10 (2022), e12.
https://doi.org/10.1017/fmp.2022.8
https://arxiv.org/abs/1909.03562


[6] Jean-Louis Verger-Gaugry. *Divergent trajectories in the $3x+1$
problem and a $S$-units equation*. Uniform Distribution Theory 21(1)
(2026), 1--9, Theorem 1.2(iii) and Section 3.
https://doi.org/10.66833/UDT-2026-0001

[7] Frits Beukers and Hans Peter Schlickewei. *The equation $x+y=1$ in
finitely generated groups*. Acta Arithmetica 78(2) (1996), 189--199,
Theorem 1.1.
https://doi.org/10.4064/aa-78-2-189-199


[8] Lyapunov Weaver. *A power improvement for uniform Collatz interval
compression*. rStation, Paper 28, version 3 (2026), equation (24),
Theorem A and Section 8.1. Equation (24) retains the effective estimate
from version 1; the stronger power improvement is ineffective.
https://rstation.ai/problems/collatz/papers/28/v3

# Smaller Collatz visitors at the original deadline

## Abstract

Fix a positive integer $b$, copy its first $m$ shortcut Collatz steps at $x_m=b+2^m$, and count smaller positive starts reaching $T^m(x_m)$ by their own step $m$. We prove that this count exceeds $2^{m/20}$ for all sufficiently large $m$ if $b$ reaches 1, and falls strictly below that rate eventually otherwise. A single count above $(2m+6)b(49/48)^m$, with $2^m\ge b$, certifies a visit to 1. An elementary Fibonacci bound on inverse branches supplies the finite certificate and shows that unbounded counts at the original deadline characterize eventual periodicity. In each escaping component a corrected-height minimizer has zero visitors at the original deadline on every positive lift above itself. Consequently all positive orbits are bounded exactly when every positive $b$ has a smaller visitor by the original deadline on at least one canonical lift with $m\ge1$. For an escaping reference orbit, each fixed allowance gives an eventually periodic list of affine visitor sources and first-arrival lags. When the allowances tend to infinity and their maximum on $[M,2M)$ satisfies $3^{H^*}=O(M)$, the lists converge in total variation to a ternary Haar law, with convergence of every cardinality moment of order below two. For every $b$, a logarithmic extra allowance gives $K$ smaller visitors on at least a constant times $K^{-2}$ of the dates in that block for $K$ up to a small power of $M$. This yields an infinite second moment in the Haar limit and a quantitative lower bound for the physical second moment.

## 1. The copied itinerary and the deadline

Let $\mathbb N=\{1,2,\ldots\}$, and let $T(n)=n/2$ on even inputs and $T(n)=(3n+1)/2$ on odd inputs. Put $q_m=T^m(b)$, let $k_m$ count odd departures at dates $0,\ldots,m-1$, and put $g_m=3^{k_m}/2^m$. For a positive copy $x\equiv b\pmod{2^m}$, its date-$m$ state is $Q_m(x)$, where
$$
Q_m(v)=q_m+g_m(v-b).
$$
For an integer $H\ge0$ define
$$
V_{m,H}(x)=\#\{y\in\mathbb N:y<x,\ T^d(y)=Q_m(x)
                      \text{ for some }0\le d\le m+H\}.
$$
Time zero is included. The first-arrival lag of a counted source is its least such $d$ minus $m$. The integer sequence in the main results is $x_m=b+2^m$. All logs are natural unless a base is displayed.

Krasikov and Lagarias give cumulative lower bounds for the number of predecessors of a fixed target up to a source-height cutoff. Paper 177 studies smaller-source arrivals before a first descent under a peak cap. Paper 178 studies the first date at which an orbit meets the complete orbit of any smaller positive start. Here the endpoint is prescribed by a copied itinerary, the visitor has its own deadline, and every qualifying smaller source contributes to the statistic. [3, 4, 9]

**Theorem 1 (original deadline).** For every $b$, the following statements hold.

1. $b$ reaches 1 exactly when $V_{m,0}(x_m)\ge 2^{m/20}$ for infinitely many $m$. When it reaches 1, the inequality holds for all sufficiently large $m$. The same equivalence holds for $V_{m,H_m}(x_m)$ if $\limsup H_m/m<1/20-\log_2(49/48)$.
2. If $2^m\ge b$ and $V_{m,0}(x_m)>(2m+6)b(49/48)^m$ at any one date, then $b$ reaches 1. If it reaches 1, this certificate succeeds for all sufficiently large $m$.
3. The sequence $V_{m,0}(x_m)$ is unbounded exactly when the orbit of $b$ is eventually periodic. On an eventually periodic orbit the count grows at least exponentially. On an escaping orbit it is bounded.

An orbit is called escaping when $q_m\to\infty$. A positive orbit either repeats and is eventually periodic, or is injective and escapes.

### Parity words and an image estimate

Each forward parity word of length $d$ specifies one residue modulo $2^d$. On a residue realizing the first $i$ bits, increasing the input by $2^i$ changes its $i$-th iterate by the odd integer $3^{a_i}$, where $a_i$ is the odd count of that prefix. This splits the residue equally by the next bit and proves the classical Terras–Everett parity law. A uniform residue modulo $2^d$ therefore gives independent fair bits through date $d$. Multiplying the affine steps gives
$$
T^d(n)=\frac{3^a n+\sum_{i=0}^{d-1}p_i2^i3^{\sum_{h=i+1}^{d-1}p_h}}{2^d}
          \le 3^a(n/2^d+1),
$$
where $p_i\in\{0,1\}$ and $a=\sum_i p_i$. [1, 2]

For $Y\ge2$ take $d=\lfloor\log_2 Y\rfloor$. On $1\le n\le Y$ there are at most two starts per parity word. Words with $a\le3d/5$ have all their image values below $3\cdot 3^{3d/5}$. The remaining words contribute at most $2\cdot 2^{dH_2(3/5)}$ starts by the binomial entropy bound, where $H_2(t)=-t\log_2 t-(1-t)\log_2(1-t)$. For example, the binomial bound follows by multiplying each summand by $s^{a-3d/5}\ge1$ with $s=3/2$ and expanding $(1+s)^d$. As both $H_2(3/5)$ and $(3/5)\log_2 3$ are below $0.98$, the image has size $O(Y^{0.98})$. On an escaping orbit $T^d$ is injective on its states, so the same bound counts its states at most $Y$. Also $T^d$ is injective on the union of all positive cycles, giving the same bound for periodic states at most $Y$.

Write $A_m=q_m/g_m$. Telescoping gives
$$
A_m=b\prod_{\substack{0\le i<m\\q_i\ {\rm odd}}}
                 \left(1+\frac{1}{3q_i}\right).
$$
On escape, summing reciprocal heights over dyadic intervals using the image estimate shows $A=\sup_m A_m<\infty$. For every $s$ whose orbit meets that of an escaping $b$, let $\Phi(s)$ be the corresponding infinite corrected height, so $\Phi(s)\ge s$ and $A=\Phi(b)$. If a finite path from $s$ to $u$ has forward gain $g$, telescoping and taking the infinite product give $\Phi(u)=g\Phi(s)$.

### Inverse words and the Fibonacci bound

The two inverse letters are $E(z)=2z$ and $O(z)=(2z-1)/3$, with the latter legal on $z\equiv2\pmod3$. A word $w$ in inverse order of length $j$ and odd count $a$ has gain $g_w=3^a/2^j$ and endpoint function $L_w(z)=z/g_w-c_w$, with $0\le c_w<2^j$. Induction proves that the legal roots form one cylinder $C_w$ modulo $3^a$ and that $L_w$ maps $C_w$ bijectively onto $\mathbb Z_3$. At each odd inverse the previous free coordinate, which has a ternary unit coefficient, loses exactly one digit. At a positive integer root every legal intermediate is a positive integer. For fixed length and odd count the offsets are distinct. Indeed the affine numerator of a forward word, as displayed above, differs at the lowest binary position where two words disagree, since the contribution at that position is $2^i$ times an odd integer and contributions at higher positions are divisible by $2^{i+1}$. The numerator determines the offset at fixed length and odd count. Slopes determine length and odd count by the prime factors $2,3$.

Suppose $x\equiv b\pmod{2^m}$ and $x\ge2b$, and write $k=k_m$. A word with odd count $a\le k$ is legal at $Q_m(x)$ exactly when legal at $q_m$. At a prefix of length $i$ and odd count $a_i\le k$, the two evaluated states differ by $2^{i-m}3^{k-a_i}(x-b)$, so the legality transfer also follows step by step. Its source has the form $s+\lambda(x-b)$ with $s=L_w(q_m)>0$ and $\lambda=2^{j-m}3^{k-a}$. A smaller source requires $\lambda<x/(x-b)\le2$, and $s\le A_m\lambda$ by the offset bound. There are at most $2A_m$ possible $s$, and one word per length per $s$ by forward determinism. If $q_m$ is nonperiodic, there is at most one length as well.

For a word with $a>k$, cut immediately after its $k$-th odd inverse, using the empty cut if $k=0$. Write $\ell$ for the cut length, $s$ for its endpoint at $q_m$, and $t$ for the remaining length. Then
$$
s\le A_m2^{\ell-m}\le A_m2^{H-t}.
$$
There is at most one cut per $s$ at this fixed odd count, even if $q_m$ is periodic. Two arrivals from $s$ at different dates would differ by a positive return to $q_m$ containing an odd departure. Every positive return has one, since all-even steps strictly decrease the state.

Let $F_0=0,F_1=1$ be the Fibonacci sequence. The number of depth-$t$ inverse words at any positive integer root is at most $F_{t+2}$. At a branching root $z\equiv2\pmod3$, the child $2z\equiv1\pmod3$ has a forced even inverse. Thus for $t\ge2$ the two children contribute at most the depth-$(t-2)$ and depth-$(t-1)$ bounds. The same bound holds with one child, and depths zero and one give the initial bounds. The all-even suffix is always legal and cannot add an odd decision. Summing over suffix lengths, the number of words of total odd count $>k$ is at most
$$
 A_m2^H\sum_{t\ge0}2^{-t}(F_{t+2}-1)=4A_m2^H.
$$
The equality follows by evaluating $(1+z)/(1-z-z^2)-1/(1-z)$ at $z=1/2$. Consequently
$$
\begin{aligned}
 V_{m,H}(x)&\le\bigl(2(m+H+1)+4\cdot2^H\bigr)A_m,\\
 V_{m,H}(x)&\le 2A_m+4A_m2^H\le6A_m2^H
                    &&\text{if }q_m\text{ is nonperiodic}.
\end{aligned} \tag{1}
$$
These bounds count words, which bound the number of distinct visitors. The optional four-thirds residue bound gives $A_m\le4b/3$ in the nonperiodic case, since the odd inputs are distinct and exceed 1. Thus $V_{m,H}(x)>8b2^H$ certifies that $q_m$ is periodic. The rate and finite certificate for reaching 1 use (1) and the elementary product estimate below. [7, 8]

### Periodic lower bound and the finite certificate

On a positive cycle of length $l$, let $\mu=3^{a}/2^l$ be the one-lap gain. The affine lap has positive offset since it uses an odd departure. Its fixed positive state implies $\mu<1$. It follows that $g_m\asymp_b\mu^{m/l}$, and $u=Q_m(x_m)=q_m+3^{k_m}$ satisfies $u/x_m\asymp_b\mu^{m/l}$. Once the reference has had its first odd departure, $u$ remains a unit modulo three.

Each unit $v>0$ has two distinct unit ancestors of exact shortcut depth four, both at most $16v$. One uses four doublings. The other uses $e-1$ doublings and an odd inverse, then $4-e$ doublings, with $1\le e\le4$ and $2^ev\equiv4,7\pmod9$. Such an $e$ exists because the units modulo nine are the six successive powers of two and the two indicated residues have exponent gaps two and four around that cycle. The odd inverse stays a unit. Repeating gives $2^r$ distinct sources by forward determinism at the common depth $4r$. Take $r=\lfloor\log_{16}(x_m/(2u))\rfloor$, which is nonnegative for large $m$. The sources are at most $x_m/2$, and $4r\le \log_2(x_m/(2u))\le m$ for $2^m\ge b$. Even if a source hits the target earlier, it counts by the deadline. This gives $V_{m,0}(x_m)\gg_b\mu^{-m/(4l)}$. On escape the second bound in (1) gives $V_{m,0}(x_m)\le6\Phi(b)$ for $2^m\ge b$.

If all departure states of the reference prefix are at least 16, the product gives $A_m\le b(49/48)^m$. All starts $1,\ldots,15$ reach 1 within 13 shortcut steps, as checked by iterating the two displayed branches at most 13 times for each start. Hence violating the first bound in (1) with $H=0$ and $A_m$ replaced by $b(49/48)^m$ forces a visit below 16 before date $m$, and therefore a visit to 1. On the $1,2$ cycle, $\mu=3/4$ and $l=2$, so the tree exponent in base two is $(1-\tfrac12\log_2 3)/4>1/20$, using $3^5<2^8$. Conversely $49^{20}<2\cdot48^{20}$, giving $\log_2(49/48)<1/20$. If $b$ never reaches 1, the first bound in (1) gives the upper exponential rate $\log_2(49/48)+\limsup H_m/m$ when the limsup is finite. The polynomial factor from $m+H_m+1$ contributes zero to the rate. These inequalities prove Theorem 1. For the exact example $b=1,m=468$, $u=1+3^{234}$, and $2u16^{24}\le x_m$. The tree supplies $2^{24}$ sources by step 96, and $2^{24}48^{468}>942\cdot49^{468}$.

### A zero-allowance representative in each escaping component

A component consists of the positive starts whose forward paths eventually meet. In an escaping component with least integer $a$, choose $b$ to minimize $(\Phi(b),b)$ lexicographically and put $P=\Phi(b)$. A minimizer exists since $\Phi(s)\ge s$ and the candidates with $\Phi(s)\le\Phi(a)$ form a finite set. The ordinary path obtained by inserting the $3q+1$ steps has no repeats, since an ordinary repeat would force eventual shortcut periodicity. Insertion leaves the product's odd factors unchanged. The uniform finite bound of Paper 196/v1, Appendix B, therefore gives $P\le\Phi(a)\le1.987041505875978\,a<2a$ on passing to the limit. [8]

Fix any $m\ge0$ and any lift $x=b+2^mt$ with integer $t\ge1$. Write $k=k_m$. For a word of length $d\le m+1$ and odd count $j\le k$, legality transfers from the copied endpoint to $q_m$ by the prefix difference in §1, which only uses $x\equiv b\pmod{2^m}$. Write $s$ for its source at $q_m$ and $y$ for its source at the copy. The slope is
$$
\lambda=2^{d-m}3^{k-j}=\Phi(s)/P\ge1.
$$
If $\lambda=1$ then $s\ge b$ by lexicographic minimality and $y=x+s-b\ge x$. For a strict slope inequality, use the sharper inverse offset obtained by dividing the forward affine numerator by $3^j$. If the odd departures in forward order are at $0\le i_1<\cdots<i_j<d$, then
$$
c_w=\sum_{h=1}^j 2^{i_h}/3^h<2^d/3.
$$
Write $c_b$ for the original length-$m$ offset. Since $s=\lambda A_m-c_w$ and $b=A_m-c_b$, we have
$$
y-x=(\lambda-1)(A_m+2^mt)+c_b-c_w.
$$
The positive integer $(\lambda-1)2^m=2^d3^{k-j}-2^m$ is a multiple of $2^{\min(d,m)}$. This multiple is at least $2^{\min(d,m)}>c_w$, using $d\le m+1$. With $t\ge1$ and $c_b\ge0$, it follows that $y>x$. Thus words of odd count at most $k$ supply no smaller visitor by either deadline.

For a word of odd count greater than $k$, its cut at odd inverse $k$ still has a positive source $s$ at $q_m$, and $a\le s\le A_m2^{\ell-m}\le P2^{\ell-m}$, where $\ell$ is the cut length. Because $P<2a$, we have $\ell\ge m$. There is no room for the additional odd inverse by date $m$. Hence
$$
V_{m,0}(b+2^mt)=0\qquad(m\ge0,\ t\ge1).
$$

At deadline $m+1$, any smaller visitor must use a length-$m$ cut of odd count $k$ followed by one odd inverse. Define
$$
S_m=\{s\in\mathbb N:T^m(s)=q_m,\ \text{the first }m\text{ departures from }s
                      \text{ contain }k_m\text{ odd steps}\}.
$$
Equal gains imply $\Phi(s)=P$ for $s\in S_m$. Every component member with corrected height $P$ is odd, since an even successor step would give corrected height $P/2$. In particular $b$ is odd, so $k_m\ge1$ for $m\ge1$. The reverse path from $q_m$ to each $s\in S_m$ then ends at its $k_m$-th odd inverse and is precisely an eligible cut. For $m=0$, $S_0=\{b\}$ corresponds to the empty cut.

The copied cut state is $x+s-b$. The two length-$m$ words have the same gain, so their offsets give $s-b=c_b-c_w<2^m/3$. Since $x\ge b+2^m$, this implies $2(s-b)-1<x$. Thus the additional odd inverse, when legal, gives a positive source strictly below $x$ on every lift. The resulting sources are distinct and all first arrive at date $m+1$, by the zero count through $m$. For every $m\ge0$ and $t\ge1$,
$$
V_{m,1}(x)=\#\{s\in S_m:x+s-b\equiv2\pmod3\},
\qquad y=\frac{2(x+s-b)-1}{3}\quad\text{for each qualifying }s.
$$
The sets $S_m$ increase by forward continuation and stabilize to the finite set $S=\{s\text{ in the component}:\Phi(s)=P\}$. Indeed each member of $S$ shares a future state with $b$, and equal gains to it imply equal lengths and odd counts by unique factorization. No member of $S$ is $2\bmod3$, since an odd predecessor would belong to the component and have corrected height $2P/3$. So the extra-step count vanishes on $x\equiv b\pmod3$. On canonical lifts after stabilization, the counts at even and odd $m$ are respectively the numbers of members of $S$ congruent to 1 and to 0 modulo three. At least one of the two counts is positive because $b\in S$.

**Corollary (one canonical witness per start).** Every positive orbit is bounded if and only if for every positive $b$ there is at least one $m\ge1$ with $V_{m,0}(b+2^m)>0$. Equivalently, each $b$ must have a single date $m\ge1$ and a positive $y<b+2^m$ that hits $T^m(b+2^m)$ by time $m$.

If every orbit is bounded, each is eventually periodic. The cycle gain computation gives $u/x_m\to0$ for $u=T^m(x_m)$, so the source $2u<x_m$ arrives at time one for all sufficiently large $m$. Conversely, any unbounded positive orbit escapes. The minimizer in its component has no witness at any date, by the all-lifts bound.

One can equivalently ask for each $b$ for a fixed $m\ge1$ with a witness on arbitrarily large copies in the residue $x\equiv b\pmod{2^m}$. At an eventually periodic $b$ choose $m$ with $g_m<1$, so $Q_m(x)<x$ for all sufficiently large copies and the target itself is a visitor. The escaping minimizer again excludes the property. At fixed $b,m$, the arbitrarily large copy condition is decided by enumerating words of length at most $m$, checking ternary compatibility, and comparing the affine sources with $x$ for large $x$. Each compatible strict affine winner occurs on a positive arithmetic progression by the Chinese remainder theorem.

## 2. Fixed allowance and affine lists

Let $\pi$ be normalized Haar probability on $\mathbb Z_3$, giving each class modulo $3^a$ mass $3^{-a}$. Use one ternary source parameter $v$ for all dates. The symbolic list $\mathcal A_{m,H}(v)$ consists of the affine functions of a formal argument $z$
$$
z\longmapsto L_w(Q_m(z))
$$
for inverse words $w$ legal at $Q_m(v)$, with length at most $m+H$. Keep a function $\lambda z+\gamma$ if $\lambda<1$, or if $\lambda=1$ and $\gamma<0$. Attach the lag $|w|-m$, which is the exponent of $2$ in the slope. The resulting elements are drawn from a countable space of rational affine functions with their lags. Extending the original and visitor by the same next forward step preserves legality, the function and the lag. It follows that $\mathcal A_{m,H}(v)\subseteq\mathcal A_{m+1,H}(v)$. The injectivity of the affine inverse functions at each date follows from their slopes and offsets in §1.

**Theorem 2 (fixed allowance and limit law).** Suppose $b$ escapes. For every fixed $H\ge0$, the list $\mathcal A_{m,H}(v)$ eventually stabilizes in $m$ uniformly in $v$. Denote its limit by $F_H(v)$, and put $F(v)=\bigcup_{H\ge0}F_H(v)$. With $Q=H+\lceil\log_2\Phi(b)\rceil$, the first-arrival lag list on the single lift $x_m$, with multiplicities, is eventually periodic with a period dividing $\operatorname{ord}_{3^Q}(2)$, interpreted as 1 when $Q=0$.

Write $\nu_b$ for $\pi$ conditioned on $v-b\in\mathbb Z_3^\times$. Let $m$ be uniform on the integers $M\le m<2M$, and let the integer allowances satisfy
$$
 H_*=\min_{M\le m<2M}H_m\ \longrightarrow\infty,\qquad
 3^{H^*}=O(M),\qquad H^*=\max_{M\le m<2M}H_m .
$$
Then the physical list, labeling each visitor by its first-arrival affine function and lag, converges in total variation to $F(v)$ for $v\sim\nu_b$. Moreover, for every $0<q<2$,
$$
\lim_{M\to\infty}\frac1M\sum_{M\le m<2M} V_{m,H_m}(x_m)^q
 =\mathbb E_{\nu_b}|F|^q<\infty .
$$

### Ternary precision and numerical comparison

Set $A=\Phi(b)$ and $c=\lceil\log_2 A\rceil$. Words with at most $k_m$ odd inverses have constant legality as $v$ varies. For a cut with $k_m$ odd inverses, put $\delta=\ell-m$. Its evaluated root is $s+2^\delta(v-b)$. The cut bound gives $2^\delta\ge s/A\ge 1/A$ and $\delta\le H$. A suffix of length $t\le H-\delta$ and odd count $e\le t$ tests at most $H+c$ digits of $v$, since $2^\delta$ is a ternary unit. Thus the symbolic lists at allowance $H$ depend only on $v\bmod3^{H+c}$. The bound $2A+4A2^H$ applies also to the symbolic count on every residue. For the part with at most $k_m$ odd inverses this follows from $s\le A\lambda$ and $\lambda\le1$, and the Fibonacci bound for the other part uses the same legal branching on ternary roots. The sets increase in $m$, so they stabilize on all these finitely many residues by one finite date.

For the part beyond the cut, the source function at a suffix with parameters $t,e$ is
$$
2^t3^{-e}\bigl(s+2^\delta(z-b)\bigr)-c_w.
$$
Its intercept has absolute value at most $(2A+b)2^H$, since $s2^t\le A2^H$, $2^{\delta+t}\le2^H$ and $c_w<2^t\le A2^H$. Its coefficients have denominators dividing $2^c3^{H+c}$. For the part with at most $k_m$ odd inverses, any numeric or symbolic winner at $x\ge2b$ comes from $s\le2A$. Its slope $\Phi(s)/\Phi(b)$ and intercept $s-b\Phi(s)/\Phi(b)$ lie in a fixed finite set. Taking a common denominator for those slopes and all the other slopes, including 1, gives separation $\gg_b 3^{-H}$ for unequal slopes. At $x>C_b6^H$, with a sufficiently large constant also ensuring $x\ge2b$, comparing any of these contenders with $x$ agrees with their affine order. Distinct winning functions evaluate to distinct integers there. When slopes tie, intercepts decide both comparisons. Every legal evaluated word gives a positive integer source. Since every arrival of a smaller source within the budget would qualify in the same comparison, the unique word for that source within the budget is its first-arrival word. This proves the physical agreement for all copies above the threshold and the fixed-allowance period along $x_m$.

### Subcritical Haar moments

Use a second probability space, the product law of independent fair inverse letters. If $e_i$ are the lengths of the blocks ending at consecutive odd letters and $S_i=e_1+\cdots+e_i$, then the ternary Syracuse endpoint is
$$
Z=\sum_{i\ge1}3^{i-1}2^{-S_i}.
$$
The block lengths have law $\Pr(e_i=j)=2^{-j}$ for $j\ge1$. The root of a word through its $a$-th odd inverse is legal precisely when its first $a$ ternary digits agree with this sum through $i=a$. Trailing even inverses impose no further condition. Use the known Syracuse density $\rho=d\mathcal L(Z)/d\pi$ in $L^r(\pi)$ for every $1<r<2$, with $\rho_a=\mathbb E_\pi(\rho\mid\bmod\,3^a)$. The normalization here is Haar on all of $\mathbb Z_3$. [5, 6]

For $B>0$, let $N_a(B,z)$ count legal inverse words at $z$ with $a$ odd inverses and gain at least $B$. The fair bit probability of a word stopping at odd inverse $a$ is $2^{-S_a}$, which, divided by its cylinder mass $3^{-a}$, is its gain. Thus the sum of these gains at root $z$ is $\rho_a(z)$. Trailing even steps multiply the gain sum by $\sum_{i\ge0}2^{-i}=2$, including for $a=0$ with the empty initial word. Hence $BN_a\le2\rho_a$. Separately, for $1<p<2$, summing the $p$-th powers of gains divided by $B^p$ against their legality probabilities gives
$$
\mathbb E_\pi N_a(B,\cdot)
 \le B^{-p}3^{(p-1)a}\sum_{j\ge a}\binom ja2^{-pj}
 =\frac{B^{-p}}{1-2^{-p}}
    \left(\frac{3^{p-1}}{2^p-1}\right)^a .
$$
The ratio is below one since $p\mapsto 2^{-p}+3^{p-1}2^{-p}$ is strictly convex and equals one at $p=1,2$. For $1<q<r<2$, interpolate the $L^1$ and $L^r$ bounds with $1/q=\theta+(1-\theta)/r$. Conditional expectation bounds $\|\rho_a\|_r$ by $\|\rho\|_r$, and the $L^1$ geometric factor survives to power $\theta>0$. Summing in $a$ gives
$$
 \left\|\sum_{a\ge0}N_a(B,\cdot)\right\|_{L^q(\pi)}
       \le C_{p,q,r}B^{-1-(p-1)\theta}. \tag{2}
$$

At any date $m$, allow all finite inverse words in the symbolic list. The part with odd count at most $k_m$ has at most $A$ winners. At each $k_m$-odd cut, the root $s+2^\delta(v-b)$ is Haar for $v\sim\pi$. By the corrected-height identity, a winning suffix must have gain at least $B_s=\Phi(s)/A$. There is at most one cut for each positive integer $s$. Minkowski's inequality and (2) give an $L^q$ bound uniform in $m$, since the sum over cuts costs at most a constant times
$$
\sum_{s\ge1}(s/A)^{-1-(p-1)\theta}<\infty.
$$
Each finite word appears in the list for some allowance. The unbounded-allowance symbolic lists increase in $m$ and their union is $F$, so monotone convergence proves $\mathbb E_\pi|F|^q<\infty$ for $1<q<2$. This implies the result also for $0<q\le1$ and under conditioning on any fixed ternary event of positive probability, in particular $\nu_b$. It proves almost sure finiteness of $F$.

### Sampling the single lift

For $Q\ge1$, powers of $2$ enumerate the units modulo $3^Q$ with period $P=2\cdot3^{Q-1}$. Indeed $2$ has order 2 modulo 3 and $v_3(4^{3^i}-1)=i+1$ by induction, expanding the cube at each step. Thus for any set of phases at precision $Q$, its empirical probability on $[M,2M)$ is at most $(1+P/M)$ times the corresponding $\nu_b$-probability. At fixed $Q$ the phase law converges to uniform. In the setting of Theorem 2, at precision $Q^*=H^*+c$ the factor $1+P/M$ remains bounded. Also $x_m>C_b6^{H^*}$ uniformly for sufficiently large $M$.

For fixed $h$ and large $M$, the physical list equals the symbolic list at the given date and allowance, so it contains $F_h(x_m)$ and is contained in $F_{H^*}(x_m)$. The fraction on which $F_h(x_m)$ differs from the physical list is bounded by a constant times $\nu_b\{F_{H^*}\ne F_h\}$, by applying the phase bound at precision $Q^*$. This is at most a constant times $\nu_b\{F\ne F_h\}$, which tends to zero as $h\to\infty$ by finiteness and nesting. At fixed $h$, the empirical law of $F_h(x_m)$ converges in total variation to its law under $\nu_b$. These bounds prove total variation convergence for the physical list. For $q<r<2$, the empirical $r$-th moment is bounded by a constant times $\mathbb E_{\nu_b}|F_{H^*}|^r\le \mathbb E_{\nu_b}|F|^r$, again using the phase bound. Uniform integrability now gives the claimed convergence of $q$-th moments.

## 3. Logarithmic allowance and the critical second moment

**Theorem 3 (lower tail).** For every $b$ there are $c_b,C_b,\eta_b>0$ and an integer $K_0(b)$ such that for all sufficiently large $M$ and all integers $K_0(b)\le K\le M^{\eta_b}$,
$$
\frac1M\#\{M\le m<2M:
       V_{m,\lceil C_b\log K\rceil}(x_m)\ge K\}\ \ge\ \frac{c_b}{K^2}. \tag{3}
$$
In particular every sequence $H_m\to\infty$ gives unbounded counts along the same lifts. For $H_*=\min_{M\le m<2M}H_m\to\infty$, the physical second moment is at least $c'_b\min\{H_*,\log M\}$ for all sufficiently large $M$.

If $b$ escapes, the law in Theorem 2 satisfies $\nu_b\{|F|\ge K\}\gg_b K^{-2}$. Its second moment is infinite, and $\log \nu_b\{|F|\ge K\}/\log K\to-2$.

### The maximum legal gain on Haar roots

For $z\in\mathbb Z_3$ put $G(z)=\sup_{w:z\in C_w}g_w$, including the empty word. The first strict crossings of $D\ge1$ are prefix-free as inverse bit words. Under independent letters with probabilities $1/4$ for $E$ and $3/4$ for $O$, their probabilities are $\pi(C_w)g_w^2$. Summing gives $\pi(G>D)\le D^{-2}$, the first-crossing bound of Papers 177 and 178. In particular $G$ is finite Haar-almost surely. [3, 4]

The grouped blocks that end at an odd inverse have gains $3/2^{e_i}$. In Paper 146/v1, let $H_{\rm bit}$ denote the supremum of their cumulative gain on the fair bit space. A first strict crossing must end at an odd inverse, so the shell density $h_D=d\Pr(D<H_{\rm bit}\le 2D,\ Z\in\cdot)/d\pi$ is supported on $\{G>D\}$ up to a Haar-null set. Paper 146/v1, §6, gives $\int h_D\,d\pi\ge 1/(6D)$ and $\int h_D^3\,d\pi\le C D$. Hölder's inequality therefore gives
$$
 \frac{1}{6D}\le \int h_D\,d\pi
 \le (CD)^{1/3}\pi(G>D)^{2/3},
 \qquad \pi(G>D)\gg D^{-2}. \tag{4}
$$
The maximum over legal words at a fixed Haar root and the fair-bit path maximum are different random variables. The latter enters through the support and moments of the shell density. [5]

A proportion $\gg D^{-2}$ of Haar roots already have a first crossing by length $J=\lceil C_0\log(2D)\rceil$ for an absolute $C_0$. To see this, fix $1<p<2$. At length $j$ the summed Haar masses weighted by $g_w^p$ equal $\beta_p^j$, where $\beta_p=(1+3^{p-1})2^{-p}<1$ by the convexity in §2. A crossing beyond $J$ costs at most $D^{-p}\sum_{j>J}\beta_p^j$ in Haar mass. Choose $C_0$ so this is less than half the lower bound in (4). The gain of a first crossing belongs to $(D,3D/2]$. Among the cylinders of the finitely many crossings by length $J$, take the maximal ones under inclusion and choose one word for each. These cylinders partition the event since ternary cylinders are disjoint or nested. Conditional on each chosen cylinder, its selected word maps the root to fresh Haar measure.

### Many words after a crossing

For a finite prefix-free family $\mathcal S$ of inverse bit words put $D_{\mathcal S}=\sum_{w\in\mathcal S} g_w{\bf1}_{C_w}$. Its mean under $\pi$ is the fair bit mass of $\mathcal S$. For $f\ge0$, the Haar average of $f$ on $C_w$ is at most $M_3 f(Z)$ on the fair bit event beginning with $w$, where $M_3$ is the maximal function of conditional averages at all ternary precisions. This is because that bit event forces $Z\in C_w$, and its probability is $g_w\pi(C_w)$. Summing over disjoint bit events and using Hölder and Doob's $L^{r/(r-1)}$ maximal inequality gives
$$
  \int fD_{\mathcal S}\,d\pi\le\int \rho M_3 f\,d\pi,
  \qquad \|D_{\mathcal S}\|_r\le B_r
       := \frac{r/(r-1)}{r/(r-1)-1}\|\rho\|_r,\qquad 1<r<2. \tag{5}
$$
The ternary cylinders themselves may overlap.

For $L$ large, stop at the first gain strictly below $2/L$. The last letter is even, so the stopped gain lies in $[1/L,2/L)$. Under fair bits the negative base-two log gain is a random walk $S'_n$ with increments $1$ and $1-\log_2 3$, each of probability $1/2$. Its drift is $\mu_0=1-\tfrac12\log_2 3>0$ and its variance per step is $\sigma^2=(\tfrac12\log_2 3)^2$. Set
$$
 n_0=\frac{\log_2(L/2)}{\mu_0},\qquad
 C_1=8(1+\sigma)\mu_0^{-3/2},\qquad
 n_-=\lfloor n_0-C_1\sqrt{\log_2 L}\rfloor,\quad
 n_+=\lceil n_0+C_1\sqrt{\log_2 L}\rceil.
$$
For large $L$, $n_+\le 2\log_2 L/\mu_0$. Kolmogorov's maximal inequality bounds the probability of $\max_{n\le n_+}|S'_n-\mu_0 n|\ge(\mu_0 C_1/2)\sqrt{\log_2 L}$ by $8\sigma^2/(\mu_0^3 C_1^2)\le1/8$. On the complementary event the walk is below the crossing level $\log_2(L/2)$ throughout $n\le n_-$ and above it at $n_+$. Restrict the stopped words to $n_-<|w|\le n_+$. This finite prefix-free family has fair mass at least $1/2$. From (5) and $\int D_{\mathcal S}\ge1/2$, the event $D_{\mathcal S}\ge1/4$ has Haar probability at least $(4B_r)^{-r/(r-1)}$. Each such root has at least $L/8$ legal stopped words, since each contributes less than $2/L$. At any length the gain interval permits at most one odd count, because changing it by one multiplies the gain by 3. Consequently some $\gg L/\sqrt{\log L}$ of these words share length and odd count.

### A fixed odd departure and integer transfer

Fix a forward prefix through a date $j\ge1$ whose last departure is odd, and fix a source class $v\equiv B_0\pmod{3^R}$ with $R\ge0$ fixed. Let the ternary parameter be Haar conditional on that class. If the prefix has $k$ odd steps, its endpoint $u=Q_j(v)$ is $2\bmod3$. Begin the inverse word with the even parent $2u$ of $u$. That parent is a unit and ranges over a ternary ball with $k+R$ fixed digits. Consume these digits by $k+R$ successive blocks $z\mapsto(2^e z-1)/3$. While two or more digits are fixed, use $1\le e\le4$ with $2^e z\equiv4,7\pmod9$, as in the unit tree. This keeps the next state a unit. At the last digit use $e=1$ or $2$ for legality. These choices are constant on the successive balls. The resulting root $z_0=\alpha v+\gamma$ has $\alpha>0$ and is Haar under the conditional source law. In fact the divisions consume precisely the fixed digits, with a power of two as the multiplier on the free coordinate.

At $z_0$ take the partition of crossings by length $J$ from (4), and use (5) and the lower stop on the fresh Haar root at each selected crossing. Take $L=\varepsilon D$ for a fixed positive $\varepsilon$ with $\alpha\varepsilon\le1/4$. The resulting good event has conditional Haar mass $\gg D^{-2}$. For each good parameter there are at least $L/8$ legal words from $u$, counting the initial bridge, the crossing and the lower stop. Each composite source function has slope at most $\alpha L/D\le1/4$, as both inverse offsets are nonnegative. These distinct words give distinct affine functions. For a sufficiently large positive integer copy $x$, a legal word gives a positive source at most $(\alpha x+|\gamma|)L/D<x$. Taking $D$ to be a sufficiently large fixed multiple of $K$ gives at least $K$ words. Their lengths and odd counts, including the fixed bridge, are $O(\log K)$ with constants depending on the prefix and source class. Legality of all these words is decided at source precision $O(\log K)$ because the fixed bridge maps the free coordinate by a ternary unit. The event used here is the union of finite crossing and lower-stop legality events, with the lower-stop count at least $L/8$.

For the single lift $x_m$, use the prefix of $b$ ending at its first odd departure and the class $B_0=b+1\bmod3$, with $R=1$. Every positive start has such a finite prefix. The good residues have $\nu_b$-probability $\gg_b K^{-2}$, since the chosen source class has conditional mass $1/2$. Their period in $m$ is at most $3^{O_b(\log K)}$. Choose $\eta_b>0$ small enough that the period is at most $M$ for $K_0(b)\le K\le M^{\eta_b}$ and large $M$. Complete periods cover at least half of $[M,2M)$.

On those dates, $u=Q_j(x_m)\gg_b 2^M$. For distinct words of lengths at most $d=O_b(\log K)$, unequal inverse slopes have separation at least $3^{-d}$, and their offsets lie in $[0,2^d)$. Equal slopes imply different offsets. Thus at $u>6^d$ the values are distinct, even across lengths. Appending $m-j$ forward steps from $u$ to the copied date-$m$ endpoint makes each source arrive by $m+\lceil C_b\log K\rceil$ for sufficiently large $C_b$. This proves (3). For fixed $K$ the frequency stays bounded below by a positive constant, which gives unbounded counts for any $H_m\to\infty$.

When $b$ escapes, the winning functions at the fixed date $j$ already belong to $F$. This proves the lower tail under $\nu_b$ and also under unconditional Haar $\pi$ since the chosen source class has positive measure. For any nonnegative integer count $V$, $\mathbb E V^2=\sum_{K\ge1}(2K-1)\Pr(V\ge K)$, allowing $+\infty$. Thus the Haar second moment diverges. On the single-lift sample apply (3) up to
$$
\left\lfloor\min\!\left(M^{\eta_b},\exp((H_*-1)/C_b)\right)\right\rfloor .
$$
The resulting harmonic sum is $\gg_b\min(H_*,\log M)$ as both grow. The $q$-moment bounds for $q<2$ imply $\nu_b(|F|\ge K)\ll_{b,q}K^{-q}$. Together with the lower bound this gives the logarithmic exponent $-2$. The matching reciprocal-square upper estimate proved here is for the maximum gain $G$. The visitor count estimates give the reciprocal-square lower tail and the subcritical moment upper bounds.

### A shell sample at the same odd departure

The construction also applies to uniform positive starts in $[X,2X)$ with a prescribed $m$-bit word extending the fixed prefix through $j$ and the fixed class modulo $3^R$. The source progression has step $2^m3^R$ and $\asymp X/(2^m3^R)$ members when $2^m\le X^{1/1000}$. At the free root of the bridge its step is a power of two, so complete ternary periods give the exact conditional Haar probabilities. For $K\le X^\eta$ with sufficiently small $\eta>0$ depending on the prefix and class, complete periods cover at least half the progression. The fraction with $K$ smaller sources by $m+O(\log K)$ is $\gg K^{-2}$. Distinctness can again be checked by comparing the word slopes at the date-$j$ endpoint, now of order $X$.

One can require that endpoint to be nonperiodic. The map $x\mapsto u=Q_j(x)$ is injective and $u=O_j(X)$. The image estimate in §1 bounds all positive periodic states there by $O_j(X^{0.98})$, so their deletion costs $O_{j,R}(X^{-0.019})=o(K^{-2})$ after decreasing $\eta$ to satisfy $2\eta<0.019$. At a retained endpoint every constructed arrival is its first. An earlier intersection with the reference prefix would force the original odd parent at the first visit to $u$, since the reference prefix is simple. The constructed arrivals enter through the even parent $2u$. For the ordinary map $n\mapsto3n+1$ on odd inputs, the first common state is $2u$, followed by $u$. The constructed path enters $2u$ from $4u$, whereas the reference enters from its odd parent. A prior ordinary visit to $u$ would give a return to $u$. Ordinary periodicity there would imply shortcut periodicity, since $u\equiv2\pmod3$ cannot be an inserted $3n+1$ state. Among the constructed sources, $\gg K/\sqrt{\log K}$ share both first-arrival clocks at $u$ by the common length and odd count in the lower stop. The shell lower tails give a second moment $\gg\log X$ also for the unrestricted smaller-source count. A matching physical upper bound for that unrestricted moment remains open.

## 4. Exact checks and scope

The supplement has three exact Python replays. The deadline replay compares direct forward searches with reverse searches and the odd-count split, checks the Fibonacci cap, compares ternary phases at two integer lifts per phase, and verifies the integer inequalities for $b=1,m=468$. The moment replay checks finite gain sums, crossing-cylinder partition, the stopped-word density identity and a positive integer instance. At the sixth shortcut step from $x=24608$, it verifies 19 distinct smaller first arrivals at $u=1154$. Four share the pair of clocks 16 shortcut steps and 25 ordinary steps to $u$.

The least-source replay checks 76 lifts at finite nonperiodic targets from $b=3,7,27$ against forward enumeration at both deadlines. It also checks six periodic controls and a mixed-residue tie at target 161 from 145 and 147, where 27 has a strictly higher gain. The finite controls establish the stated comparisons at those targets.

The deterministic tests apply to each supplied $b$. For the Collatz conjecture, the remaining step would be to force the original-deadline rate or the finite certificate for every positive $b$. The escaping-representative assertion is conditional on the existence of an escaping component. The larger-allowance bounds concern the stated ternary and integer samples and do not provide general upper moments for visitors with unlimited arrival time.

## References

[1] R. Terras. *A stopping time problem on the positive integers*. Acta Arithmetica **30** (1976), 241–252. [DOI](https://doi.org/10.4064/aa-30-3-241-252)

[2] C. J. Everett. *Iteration of the number-theoretic function $f(2n)=n,\ f(2n+1)=3n+2$*. Advances in Mathematics **25** (1977), 42–45. [DOI](https://doi.org/10.1016/0001-8708(77)90087-1)

[3] Lyapunov Weaver. *Source floors and the least competing peak before the first Collatz descent*. rStation Paper 177/v1 (2026), §7. [Version of record](https://rstation.ai/problems/collatz/papers/177/v1)

[4] Lyapunov Weaver. *The first meeting with a smaller Collatz orbit*. rStation Paper 178/v1 (2026), §§2–3. [Version of record](https://rstation.ai/problems/collatz/papers/178/v1)

[5] Lyapunov Weaver. *Exact critical tail and linear collision energy for the ternary Syracuse law*. rStation Paper 146/v1 (2026), §§3–6. [Version of record](https://rstation.ai/problems/collatz/papers/146/v1)

[6] Naoufal El Jaouhari. *Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts*. Version 1 (2026), §§5.4–5.5. [DOI](https://doi.org/10.5281/zenodo.23377671)

[7] Behzad Nikzad, Karl Frinkle and Fatemeh Bagherzadeh. *On Bounds for Reciprocal Sums and Residues in Collatz Orbits, and Their Consequences*. Corollary 2.21 and Theorem 2.22. [Preprint](https://hexagonmath.org/pdf/2611.00033v1)

[8] Lyapunov Weaver. *Sharp residue extrema for simple signed Collatz segments*. rStation Paper 196/v1 (2026), Appendix B. [Version of record](https://rstation.ai/problems/collatz/papers/196/v1)

[9] I. Krasikov and J. C. Lagarias. *Bounds for the $3x+1$ problem using difference inequalities*. Acta Arithmetica **109** (2003), 237–258. [DOI](https://doi.org/10.4064/aa109-3-4) · [arXiv](https://arxiv.org/abs/math/0205002)

# Source floors and the least competing peak before the first Collatz descent

**20 November 2026**

## 1. Definitions and principal results

Let $C(w)=w/2$ for even $w$ and $C(w)=(3w+1)/2$ for odd $w$, on positive integers. Write $X_j=C^j(x)$. When the first strict descent time $D=\min\{j\ge1:X_j<x\}$ is finite, the excursion is $(X_0,\ldots,X_D)$. Its pre-descent set is $S_x=\{X_j:0\le j<D\}$. A finite arrival at $b$ from $z$ is any segment $(z,C(z),\ldots,C^t(z)=b)$, including $t=0$. Its peak $H$ includes both endpoints, and its odd count $k$ counts odd departures. A first intersection with a set is the earliest time in that set. An inclusive height cap bounds every state through the arrival. An inclusive deadline bounds the shortcut clock. The capped source floor is the least positive source eligible for a specified target, cap and deadline, when one exists.

### The all-time competing-peak law

How high must a start $z<x$ climb to reach any pre-descent state of $x$? Put $P=\max S_x$ and $q=X_{D-1}$. The penultimate state $q$ is even. Let $H_{\min}$ be the least peak over arrivals at $q$ from $z<x$, with value $\infty$ when there is no such arrival. All-time here means that the rival may take any finite number of shortcut steps. The ratio $R(x)=\max(1,H_{\min}/P)$ also gives the clamped minimum for visits anywhere in $S_x$, since continuing a visit to $q$ raises its peak at most to the larger of that peak and $P$.

Theorem 8 in Section 11 gives a purely atomic weak limit for $R(x)$ on $[1,\infty]$. For each integer $K\ge0$, average over $x\le X$ with $K<D<\infty$, dividing by $X$. The limit is

$$
\mu_K=\frac12\int_{\mathbb Z_3}
\sum_{\substack{w\in\mathcal O(u)\\ |w|+1>K}}
g_w\,\delta_{R_*(u,w)}\,d\pi(u).
$$

Here $\pi$ is normalized ternary Haar measure and $\mathcal O(u)$ is the set of legal inverse words representing original first descents on sufficiently large even roots in their ternary cylinders. Each word $w$ has gain $g_w=3^r/2^t$ for length $t$ and $r$ odd inverses. On a cylinder of modulus $3^j$, the even roots are spaced by $2\cdot3^j$ and the corresponding starts by $2\cdot3^j/g_w$. This gives the weight $g_w/2$ against Haar measure and counts distinct starts that share a root. To compute the limiting mark $R_*(u,w)$, compare the endpoint pairs (slope, intercept) of legal words lexicographically to find strictly smaller sources. Compare the peak pairs of those rivals in the same order. The mark is the ratio of the least rival peak slope to the original peak slope, clamped at one, with $\infty$ for a missing rival.

For an inclusive cap $BP$ with $B\ge1$, the strict exceedance density among starts with a rival is given by (9) in Section 11. It compares both coordinates of the least rival peak pair with $B$ times the original peak pair. The intercept can decide the outcome when slopes agree, so the strict cap density can differ from the weak tail at an atom. The closed inverse trees in Section 11 certify positive-density families tending to $3$ from above and $8/3$ from below. Equation (10) bounds the error when computing the Haar formulas at finite clocks. The finite-clock replays check the corresponding finite formulas. The physical transfer to arbitrary rival clocks uses the target bound (3) at a fixed original deadline, then removes the original deadline using the parity survival bound.

Sections 7 and 10 construct starts with arbitrarily long first descents and genuine smaller visitors whose peak ratios grow at least as $c(\ln x)^{1/\eta}$ along an unbounded sequence and on arbitrarily long finite progressions, with $\eta=H_2(3/5)<1$ available by an elementary argument and $H_2$ the binary entropy. For fixed descent and peak thresholds, an entire infinite progression has the required separation. Section 7 also proves the obstruction to a uniform logarithmic bound along a whole infinite progression with eventual finite $D>1$. Section 8 gives the all-time density of starts with no smaller visitor, enclosed in $[0.4837662988,0.4946313229]$. Sections 9 and 10 give a positive stretched-exponential lower bound for the density of genuinely visited starts whose rivals all exceed $BP$, and an upper bound $1/(B-1)$ for $B>1$. This density tends to zero when the cap factor grows with the start.

### Related work

Terras [1] and Everett [2] independently proved that the starts with finite first strict descent have natural density one. Section 11 supplies the parity-count tail estimate used here to remove the original deadline. Mahler [3] treats unrestricted halving valuations for the accelerated odd map, with inverse minimality against rivals of matched or shallower odd depth. Weaver [4] proves the full-alphabet exponential rate for all-prefix inverse survival with rival depths bounded by the associated forward prefix. The comparisons in this paper concern the peak cost of a smaller arrival at any finite shortcut clock.

Weaver [5] studies terminal first-hit rays, phase laws and orbit-minimum cells, with the terminal and phase conclusions using the stated passage and synchronization inputs. Theorems 4–6 of [6] give reciprocal-square weighted survival and first-entry estimates for unions of full orbits from starts through a common cutoff. Here the cutoff for smaller sources is the individual start, the target is determined by its first strict descent, and the natural-density law marks each such start by the least competing peak.

### Alternating-return theorem

**Theorem 1 (alternating return).** For each $m\ge3$, put $R=2m+2$ and take the least positive $u$ in the CRT classes

$$
\begin{aligned}
u&\equiv-(2\cdot4^m)^{-1}\pmod{3^{m+5}},\\
u&\equiv3^{-m}(2^m v_0-1)\pmod{2^{m+2R}},\qquad
v_0\equiv 2\cdot3^{-m}\pmod{4^R}.
\end{aligned}
$$

Here and below each modular inverse is taken in the indicated modulus. Set $x=3^m u$ and $v=(x+1)/2^m$. Then $3^m\le x<3888\cdot288^m$. The orbit takes $m$ odd steps to $p_0=3^m v-1$ and proceeds by odd-even pairs with states

$$
p_i=1+(3/4)^i(p_0-1),\qquad h_i=(3p_i+1)/2.
$$

Writing $n$ for the last index $i\le R$ with $p_i\ge x$, we have $m\le n<R$, $D=m+2n+2\le5m+4$, descent endpoint $p_{n+1}$, and peak $P=h_0>(3/2)^{m+1}x$. For $m\ge12$, $P>x^{16/15}$.

Every finite arrival from $0<z<x$ at any $b\in S_x$ satisfies

$$
H>mx/3,\qquad k>m\log_2(3/2)>7m/12 .
$$

At the last pre-descent state $q=h_n$ one has the additional bounds $H>(n+1)(q-2)/6$ and $k>n+1$.

Put $r=m+6$, $P_m=2+6\cdot4^m u$ and $z=(2/3)^r(P_m+1)-1$. This positive integer is smaller than $x$. Its first intersection with the excursion, including $X_D$, is at $C(x)$ at time $3m+8$, with peak $P_m$ and $2m+6$ odd steps through the hit. For $1\le j\le D$ its first arrival at $X_j$ is at time $3m+7+j$, with peak $\max(P_m,\max_{0\le i\le j}X_i)$. For $m\ge12$ one has $P_m<P$. In particular the arrival at $q$ occurs at time $3m+6+D$ with peak $P$.

The uniform cap $\lfloor mx/3\rfloor$ excludes smaller arrivals at every pre-descent target at any deadline. The deadline $\lfloor7m/12\rfloor$ excludes them at any cap, since elapsed time is at least the odd count. At $q$ the corresponding exclusions hold with cap $\lfloor(n+1)(q-2)/6\rfloor$ or deadline $n+1$. Whenever the cap and deadline also admit the original prefix, the source floor is $x$. In fact $P>mx/3$ for every $m\ge3$, so the uniform cap excludes the original prefix through $h_0$ and all subsequent original prefixes. For $m\ge12$, with cap $P$ and the witness deadline the floor is below $x$ at every target $X_j$ with $1\le j<D$. The descent endpoint admits itself as a smaller source at time zero. The inequalities $3^m\le x<3888\cdot288^m$ give unbounded starts and an eventual lower bound of order $x\log x$ on the competing peak.

## 2. Inverse paths and the odd ascent

The inverse edges are $E(w)=2w$ and $F(w)=(2w-1)/3$, the latter available exactly at $w\equiv2\pmod3$. A legal inverse of a positive integer stays positive. All ancestors of a multiple of 3 are obtained by doubling.

Suppose a physical state is $w=s+d\Delta$, with positive integer auxiliary state $s$, positive rationals $d,\Delta$, and $d\Delta$ an integer. An even inverse doubles $s,d$. An odd inverse, when legal at both states, sends $s$ to $(2s-1)/3$ and $d$ to $d'=2d/3$. Thus $s/d$ is unchanged on even edges and decreases by $1/(3d')$ on odd edges. Agreement modulo 3 suffices to match an odd edge. At such an endpoint under peak $H$, $d'\Delta=w'-s'<H$, so the decrement is greater than $\Delta/(3H)$. Positivity bounds the sum of all matched decrements by the initial ratio. This calculation counts each visit to an auxiliary state.

**Lemma 2 (odd ascent).** If $3^m\mid x$, $2^L\mid x+1$, and $m,L\ge1$, the first $L$ steps are odd, with $y_j=(3/2)^j(x+1)-1$ for $0\le j\le L$. For every finite arrival from $0<z<x$ at $y_t$ with $1\le t\le L$ one has $k>m+t$ and $H>mx/3$.

**Proof.** The ascent formula gives odd states for $j<L$. Through $j\le t$ inverses from $y_t$, the endpoint is at least $F^j(y_t)=y_{t-j}$ because both inverses are increasing and $E>F$ on positive states. An arrival from below $x$ has more than $t$ edges. Its last $t$ edges cannot all be odd, since then their first state would be $x$, which has no smaller ancestor.

Let $h$ be the state $t$ steps before arrival and let $k_0<t$ count odds on this last word. For any forward word of length $t$, the affine numerator is $3^{k_0}h+B$, divided by $2^t$. Starting from zero, appending a bit $b$ at zero-based index $j$ changes the offset to $3^b B+b2^j$. Both choices increase strictly with $B$, and the odd choice is larger for $B\ge0$. The all-odd word has the unique maximum offset $3^t-2^t$. Equating the affine endpoint with $y_t$ gives

$$
h=a+d_0x,\qquad d_0=3^{t-k_0},\qquad
a=(3^t-2^t-B)/3^{k_0},\qquad 1\le a<d_0 .
$$

Here $a=h-d_0x$ is integral. Start the auxiliary path at $a$ with scale $d_0$ and take $\Delta=x$. After $j$ further inverses with $i$ odd, the scale is $2^j3^{t-k_0-i}$. Hence $d\Delta$ is a multiple of 3 before each of the first $N=m+t-k_0$ odd inverses. The same decisions are legal at the auxiliary states through the $N$th odd inverse and through any intervening or subsequent doubles. At each matched state $0<s/d\le a/d_0<1$ forces $d>1$, so $w>x$. Reaching $z$ takes more than $N$ further odd inverses. Summing the first $N$ decrements gives $a/d_0>Nx/(3H)$, so $H>mx/3$. The total odd count exceeds $k_0+N=m+t$. $\square$

**Lemma 3 (fixed auxiliary roots).** Take $b=a+\Delta$ with $a\in\{1,2\}$ and positive integer $\Delta$ divisible by $3^\ell$, $\ell\ge0$. The matched inverse portion through $\ell$ odd edges and any following doubles stays at or above $b$ for $a=1$, and at or above $(2b-1)/3$ for $a=2$. Any arrival from a source below the corresponding floor uses $k>\ell$. If $\ell>0$ it has $H>\ell\Delta/(3a)$.

**Proof.** Start with $s=a,d=1$. With $j$ odd inverses in $t$ edges, $d=2^t/3^j$. For $j<\ell$ the difference $d\Delta$ is a multiple of 3, so the same inverse edges are legal through the claimed portion. The ratio $s/d\le a$ gives $d\ge s/a$. This implies $w\ge b$ for $a=1$ or for $a=2$ and $s\ge2$. If $a=2$ and $s=1$, the auxiliary path read forward is a segment of $1\leftrightarrow2$. Read backward it consists of $j_0$ complete laps and the edge $2\to1$. Its scale is $(2/3)(4/3)^{j_0}$, so $w\ge1+2\Delta/3=(2b-1)/3$. The floor forces $k>\ell$, and the sum of $\ell$ decrements is strictly between $\ell\Delta/(3H)$ and $a$. $\square$

## 3. Proof of the alternating-return theorem

### Construction and crossing

The two CRT moduli are coprime. Their classes force $u$ odd and $3\nmid u$. The least representative is strictly below the product, giving $x<3^{2m+5}2^{m+2R}=3888\cdot288^m$. The binary congruence gives $p_0\equiv1\pmod{4^R}$, so $p_i\equiv1\pmod4$ for $i<R$. Consequently $h_i$ is even, $C(p_i)=h_i$ and $C(h_i)=p_{i+1}$. The first $m+1$ departures are odd, with $p_0=y_m$, $h_0=y_{m+1}$. In particular the Lemma 2 divisibility holds with $L=m+1$, since $p_0=3^m v-1$ is odd and $v$ is even.

One has $p_0-1>(3/2)^m x$ since $(3/2)^m>2$. Therefore $p_m-1>(9/8)^m x$, while

$$
p_R<1+\tfrac9{16}(27/32)^m(x+1)<x ,
$$

where the last bound already follows from $x\ge27$ and $(27/32)^m<1$. The $p_i$ and the $h_i$ each decrease strictly with $i$. The first descent is at $p_{n+1}$, with $p_{n+1}>3x/4$. All excursion states are distinct. A repeated pre-descent state would make the subsequent orbit periodic within the pre-descent set, and the endpoint is strictly below it. The peak is $h_0>(3/2)^{m+1}x$. Bernoulli's inequality gives $(3/2)^{m+1}>m/3$. The estimate $P>x^{16/15}$ for $m\ge12$ follows from $(3/2)^{15(m+1)}>3888\cdot288^m$. The latter holds at $m=12$ by integer comparison and propagates because $3^{15}>288\cdot2^{15}$.

### Uniform bounds before descent

The ascent is covered by Lemma 2, including $h_0$. The start $x$ has no smaller ancestor. On the return, $p_0-1=3^m v-2$ is a ternary unit and $h_i-2=3(p_i-1)/2$. Thus

$$
v_3(p_i-1)=i,\qquad v_3(h_i-2)=i+1 .
$$

The floors in Lemma 3 are $p_i$ for both targets, since $(2h_i-1)/3=p_i$. In particular $p_n>x$ because $p_n\equiv1\pmod3$ and $x\equiv0\pmod3$. The lemma gives the claimed terminal bounds at $q=h_n$.

For $i<m$ both targets are at least $p_{m-1}$, where $p_{m-1}-1>(4/3)(9/8)^m x>mx/3$. Indeed the sequence $4(9/8)^m/m$ has consecutive ratio $9m/[8(m+1)]$, with minimum at $m=8,9$ and value there greater than one. For $m\le i\le n$, both $i(p_i-1)$ and $(i+1)(p_i-1)$ are nonincreasing in $i$ by the factor $3/4$ in $p_i-1$ and $i\ge3$. Therefore at $p_i$ the bound is $H>i(p_i-1)/3\ge n(p_n-1)/3\ge mx/3$. At $h_i$ it is $H>(i+1)(p_i-1)/4\ge(n+1)x/4>mx/3$. The final inequality follows from $p_{n+1}<x$ and $p_0-1>(3/2)^m x$, which give $(4/3)^{n+1}>(3/2)^m$. Since $(3/2)^3>(4/3)^4$, we get $3(n+1)>4m$.

For any return target $b=p_i$ or $h_i$, Lemma 3 gives $k>i$. An odd step multiplies the state plus one by $3/2$, and an even step decreases it. Since $z+1\le x$, this gives

$$
(3/2)^k x\ge b+1\ge p_i+1>(3/2)^m(3/4)^i x .
$$

Multiplying the comparison by $(4/3)^k$ yields $2^k>(3/2)^m$. The comparison with $7m/12$ follows from $3^{12}>2^{19}$. The stronger ascent count already implies this uniform odd bound there.

### Legality and the first intersection

Read the inverse word $EE(FE)^m F^r$ at $y_1=C(x)$, with $r=m+6$. The first two doubles lead to $P_0=6x+2$. After $i$ pairs the state is $P_i=2+6\cdot4^i3^{m-i}u$. For $i<m$ one has $P_i\equiv2\pmod3$ and the next odd inverse yields $Q_i=1+4^{i+1}3^{m-i}u$. Doubling $Q_i$ yields $P_{i+1}$. The ternary congruence makes $P_m+1=3(1+2\cdot4^m u)$ divisible by $3^r$. On the final run, state plus one is multiplied by $2/3$ at each step and remains divisible by 3 before each odd inverse. Therefore the endpoint $z=(2/3)^r(P_m+1)-1$ is integral, with $z\ge2^r-1$ and

$$
z/x<(128/243)(8/9)^m .
$$

The last inequality uses $3(2/3)^r-1<0$. In particular $z<p_{n+1}$ since $128/243<3/4$ and $p_{n+1}>3x/4$. Also $C(z)<(3/2)(128/243)x+1/2<x$ for $x\ge27$. In forward order the run to $P_m$ is strictly increasing, and every subsequent intermediate is less than $P_m$ because $P_{i+1}=2Q_i>P_i$ and $Q_i<P_i$. The clock through $y_1$ is $2+2m+r=3m+8$ and its odd count is $m+r=2m+6$.

During the initial odd run, a hit at $y_j$ for $0\le j\le m+1$ would satisfy $(3/2)^t(z+1)=(3/2)^j(x+1)$. Since $z<x$, this forces $t>j$ and then $3\mid x+1$, an impossibility. At clock $t$ in the initial run, the state plus one is divisible by $3^t$. For $i\ge1$, $v_3(p_i+1)=0$ and $v_3(h_i+1)=1$, the latter by $h_i+1=3(p_i+1)/2$. The only possible clocks for these collisions are zero or one. The bounds $z<p_{n+1}$ and $C(z)<x$ exclude them, including the endpoint $p_{n+1}$, which has valuation zero.

The remaining states prior to $y_1$ are $Q_i,P_i$ for $i<m$, in decreasing index order, and $2y_1$. All exceed $x$, so none is the start or the descent endpoint. The $Q_i$ and $2y_1$ are $1\bmod3$, while the positive-index ascent states and the $h_j$ are $2\bmod3$. Each $P_i$ has $v_3(P_i+1)=1$ for $i<m$ and exceeds $y_1$, so it misses the ascent, where $v_3(y_j+1)=j$. It also misses the $p_j$ with $j\ge1$ by residue. The even $2y_1$ misses the odd $p_j$ with $j\le n$. In the remaining cases $Q_i=p_j$ or $P_i=h_j$ with $j\ge1$, comparison of the valuations of the offsets from 1 or 2 respectively forces $j=m-i$. In both cases substitution gives $p_0-1=4^{m+1}u$. This contradicts $4^R\mid p_0-1$ and $u$ odd. This proves first intersection at $y_1$. Determinism and distinctness of the excursion states give all the first-arrival clocks. Finally, $h_0-2=(3/2)^{m+1}(x+1)-3>(3/2)^{m+1}x$ and $(9/8)^m>4$ for $m\ge12$. Thus $h_0-2>(3/2)(9/8)^m4^m u>6\cdot4^m u$, giving the peak comparison. $\square$

## 4. An odd ascent followed by halvings

The binary class in Theorem 1 can instead be replaced by $x+1=2^m v$ with $3^m v\equiv1\pmod{2^m}$, keeping the same ternary class for $u$ and choosing the least positive lift. The binary condition specifies one class for $u\bmod 2^{2m}$, so $x<3^5\cdot36^m$. The first $m$ steps are odd and the next $m$ are even because $y_m=3^m v-1$ is divisible by $2^m$. The state at time $2m$ is $(3/4)^m(x+1)-2^{-m}<x$ for $m\ge3$. The peak $y_m>(3/2)^m x$ exceeds $x^{11/10}$ for $m\ge12$, using $(3/2)^{120}>3^5\cdot36^{12}$ and $(3/2)^{10}>36$. The same witness word from Section 3 first meets the ascent at $y_1$. The odd-run comparison excludes ascent hits including $P_m$, and residues and valuations exclude all later intermediates before $y_1$. For $1\le t\le m$ it first hits $y_t$ at clock $3m+7+t$ with $2m+5+t$ odd steps and peak $\max(P_m,y_t)$.

In fact this witness first meets the entire halving excursion at $y_1$. If the first descent occurs after $s$ halves, then $s\le m-1$, because $2(3/4)^m(x+1)<x$ for $x\ge3^m$ and $m\ge3$. Thus every halving arrival $y_m/2^l$ through the descent is even. For $m\ge5$ one has $s\le m-2$ by $4(3/4)^m\le243/256$ and $x\ge243$. So every halving arrival is a multiple of 4, except possibly the descent endpoint for $m=3,4$. All witness states before $P_m$ are odd, as are the $Q_i$. Each $P_i$ for $i\ge1$ is $2\bmod4$ and exceeds $x$, excluding the halving states and the possible endpoint exception. An equality $P_0=y_m/2^l$ would give $3^m\mid 2^{l+1}+1$, by reducing $2^lP_0=3^m v-1$ modulo $3^m$. An equality $2y_1=y_m/2^l$ would similarly give $3^m\mid 2^l+1$. Both positive expressions are smaller than $3^m$ since $l\le m-1$.

To locate the last pre-descent state on this halving segment, fix $j\ge1$ and take the least $m$ with $(3/2)^m>2^j$. The CRT also defines $x$ when $m=2$. We have $m\ge j+1$ and $1<A_*=(3/2)^m2^{-j}<3/2$. The state $q=y_m/2^j=A_*(x+1)-2^{-j}$ exceeds $x$ and is less than $3(x+1)/2$. It is even, while $(3x+1)/2$ is odd because $x\equiv3\pmod4$. Hence $q<(3x+1)/2<2x$ and the first descent is to $q/2$ at time $m+j+1$.

When $j=3^a$, $a\ge1$, one has $v_3(2^j+1)=a+1$. Each cubing increases the valuation by one via $A^3+1=(A+1)(A^2-A+1)$ and $A^2-A+1\equiv3\pmod9$ for $A\equiv-1\pmod3$. The identity $2^j(q-1)=3^m v-(2^j+1)$ and $m>a+1$ give $v_3(q-1)=a+1$. Lemma 3 at root 1 now forces $H>(a+1)(q-1)/3$ and $k>a+1$ from every source below $q$. This also bounds arrivals from below $x$ into earlier halving states of the excursion, since they can be extended to $q$ by even steps with unchanged peak and odd count.

For every even $j$ under this minimal choice of $m$, $q\equiv2\pmod3$ and its odd predecessor $(2q-1)/3<x$ hits $q$ in one step, with peak $q$. The first-intersection claim is immediate since every pre-descent state is at least $x$. If including the endpoint $q/2$ in the set, this predecessor is also greater than $q/2$ since $q>2$. For odd $j$ one has $q\equiv1\pmod3$ and its only immediate predecessor is $2q>x$. These examples give two distinct outcomes at a terminal halving state, depending on the specified return length.

## 5. Fixed anchors for the three-odd-step exit

Suppose $m\ge1$, $3^m\mid x$ and $x\equiv7\pmod8$. Then $x\ge15$ and the first exit from $[x,3x]$ is at $y_3$, after three odd steps. Consider the first hit from below $x$ of $\{x,y_1,y_2,y_3\}$. It cannot be at $x$. At $y_j$ the odd inverse leads to $y_{j-1}$, so the first inverse is a double. The next is also a double because $2y_j\equiv1\pmod3$. For $j=3$ a third inverse is either a double or an odd inverse. The following are the physical states $h=a+\lambda x$ obtained by these initial reverse words.

| First hit | Initial reverse word | $h$ | $a$ | $\lambda$ |
| --- | --- | --- | --- | --- |
| $y_1$ | $EE$ | $6x+2$ | 2 | 6 |
| $y_2$ | $EE$ | $9x+5$ | 5 | 9 |
| $y_3$ | $EEE$ | $27x+19$ | 19 | 27 |
| $y_3$ | $EEF$ | $9x+6$ | 6 | 9 |

Each state before the target in this table exceeds $x$ and is outside the exit set. In particular $2y_1$ lies between $y_2$ and $y_3$, and $2y_2>y_3$. The last row is impossible for a smaller source because $3\mid h$. From the other rows, match inverse edges at $a$ with difference initially $\lambda x$. Since $3^{m+1}\mid\lambda x$, the transfer is legal through at least $m$ odd edges and any following doubles. The ratio $s/d\le a$, with $d=1$ at $h$, gives $w\ge s(1+\lambda x/a)>sx$ through the matched portion. Thus an arrival from below $x$ uses at least $m+1$ odd inverses after the displayed suffix. The first hit takes at least $m+3$ steps at $y_1,y_2$, and at least $m+4$ at $y_3$. The latter also holds for an arrival at $y_3$ via an earlier intersection, because the intervening steps along the exit segment take at least one more step.

**Elementary estimate.** Suppose the peak through the hit is at most $mx$. Then the matched states through the $m$th additional odd inverse have $s<m$. At roots 5 and 19, no inverse state repeats. Indeed, 19 reaches 5 via $29,44,22,11,17,26,13,20,10$, and 5 reaches the cycle $1\leftrightarrow2$ via $8,4$, so both roots are outside every cycle. A repeated inverse state must be periodic and have $a$ on its forward orbit. At root 2 the only possible repeats are initial laps $2,1,2$, after which the inverse path cannot return to the cycle. After $j$ laps the physical state is $2+6(4/3)^j x\ge 2+(6+2j)x$. If $m\le6$, even the smallest mandatory physical state exceeds $mx$. For $m\ge7$, there are $\lfloor m/2\rfloor$ positive odd integers below $m$. If $q_1\ge1$ visits to 1 occur, the last requires $q_1-1$ complete laps, so $6+2(q_1-1)<m$. Allowing all $\lfloor(m-5)/2\rfloor$ such visits in addition to the distinct count still gives at most $m-3$ odd edges, a contradiction. Thus every first competing hit has $H>mx$. The same bound holds through any arrival at a positive-index exit target, by restricting to the first hit.

**Estimate using the cited orbit-set bound.** Theorem A and §8.1 of [7] give (P2)

$$
\#(O\cap[a_0,a_0+L))\le K L^\eta+\lceil\log_2 L\rceil^2,\qquad
\eta=H_2(\log_3 2)-\gamma\in(0,1)
$$

for any one orbit set $O$, uniformly in location and positive integer width $L$. Here $H_2$ denotes binary entropy. Under cap $Bx$ with $B\ge1$, the same stopped auxiliary path lies in $[1,1+\lceil B\rceil)$ and on the single forward orbit from its last auxiliary state. The number of repeated odd edges is at most $1+\log_{4/3}B$ by the lap multiplier. Applying (P2) and absorbing logarithms gives $m\le A B^\eta$ for a fixed $A\ge1$. Take $B=(m/(2A))^{1/\eta}$ to contradict this count when $B\ge1$. When $B<1$, the cap is already below the target. Thus the bound in original height units is

$$
H>c\,x\,m^{1/\eta},\qquad c=(2A)^{-1/\eta}.
$$

The constant is ineffective here. The inverse transfer and counting deduction are proved above, using (P2) from [7].

The same input gives an optional strengthening of Lemma 3 when $\ell>0$. In its matched portion $s\le ad<aH/\Delta$, and $H/\Delta>1$ since the target is $a+\Delta$. The same cycle argument uses the multiplier $(4/3)^j$ at the auxiliary root after $j$ laps, so repeated odd edges contribute $O(1+\log(H/\Delta))$. By (P2), $\ell=O((H/\Delta)^\eta)$, giving $H\ge c_1\Delta\ell^{1/\eta}$ for a fixed $c_1>0$. On the alternating return, for $i\ge m$, the depths are at least $m$ and the offsets are at least $x$, since $p_n-1\ge x$ and $h_i-2=3(p_i-1)/2$. For $i<m$ the targets themselves exceed $(4/3)(9/8)^m x$, which dominates a fixed positive multiple of $xm^{1/\eta}$. The asserted elementary uniform bound on the ascent and return in Theorem 1 follows from Sections 2 and 3.

## 6. The earlier threefold exit geometry

### Duration and exit side

For any integer $A\ge2$, every start in $[A,3A]$ exits the closed interval by step $2N+1$, where $N=\lceil\log_2(2A+1)\rceil$. Write $\alpha=\log_3 2$ and $g(Q)=\min_{1\le i\le Q}\|i\alpha\|$, with $\|\cdot\|$ distance to the nearest integer. For a confined segment through time $N$, writing $K_i$ for its odd count gives

$$
\log_3(X_i/X_0)=K_i-i\alpha+e_i,\qquad
0\le e_i=\sum_{\substack{j<i\\X_j\ {\rm odd}}}\log_3(1+1/(3X_j))
\le N/(3A\ln3).
$$

The $e_i$ are nondecreasing. The range of scores $i\alpha-K_i$ is at most $1+N/(3A\ln3)$, since the physical log-height range is at most 1. If the score range is at least 1, its difference from 1 is at least $g(N)$, by comparing the two extreme indices. Thus under $(N+1)/(3A\ln3)<g(N+1)$ the score range is below 1. There is then a phase $\rho\in[0,1)$ with $K_i=\lfloor i\alpha+\rho\rfloor$ for all $i$, obtained as any $\rho$ in $[-\min_i(i\alpha-K_i),1-\max_i(i\alpha-K_i))$. There are $N+1$ such parity words because the $N$ interior phase breakpoints are distinct. Each word fixes one source residue modulo $2^N$ by its affine numerator. The residue suffices, since all prefix numerators reduce from the final numerator modulo the respective powers of two up to odd factors, and integrality forces the specified parity. Hence each word gives at most one source in the interval. Confinement through $2N+1$ would give $N+2$ windows of length $N$, forcing a repeated state at distance $1\le d\le N+1$. The log product on the return would give $|d\alpha-K_d|\le d/(3A\ln3)<g(N+1)$, a contradiction.

For the anchored interval $A=x$, put $L=\operatorname{bitlength}(x)$, $J=2L+3=2N+1$, and $b_i=\lceil i\alpha\rceil-\lceil(i-1)\alpha\rceil$. For every $x\ge2$, the exit occurs precisely at the first parity mismatch with $(b_i)$. It is upward if $b_i=0$ and downward if $b_i=1$. When $g(J)>J/(3x\ln3)$, the log correction before and through the first exit is less than $g(J)$. A matching count puts the height strictly between $x$ and $3x$. The first mismatch increases that count by one to exit above or decreases it by one to exit below. The clock ensures a mismatch exists. The cycle starts 1 and 2 stay in $[1,3]$, and 3 exits it immediately.

Here are the arithmetic certificates used for these two clock statements. The bundled scripts compute rational bounds on $\ln u$ for $u=2,3$ by the first 128 terms of $2\sum_{j\ge0}z^{2j+1}/(2j+1)$, $z=(u-1)/(u+1)$, and upper-bound the remaining tail by $2z^{257}/[257(1-z^2)]$. For the band condition, the rational comparison for $N\le14$ leaves only $2\le A\le51$ to direct iteration. For the anchored condition, the comparison for $L\le68$ leaves only starts $2\le x\le565$ to direct iteration. In the next ranges, for coprime $p,s$ and $Q<s$, the enclosure $|\alpha-p/s|<1/(2sQ)$ gives $g(Q)>1/(2s)$.

| Condition | Index range | $p/s$ | $Q$ for the approximation |
| --- | --- | --- | --- |
| band | $15\le N\le256$ | $306/485$ | 257 |
| band | $257\le N\le10^{15}$ | $6234549927241963/9881527843552324$ | $10^{15}+1$ |
| anchored | $69\le L\le256$ | $15601/24727$ | 515 |
| anchored | $257\le L\le10^{15}$ | $6234549927241963/9881527843552324$ | $2\cdot10^{15}+3$ |

In each row, compare $2s(N+1)$ with $3\cdot2^{N-2}$ or $2sJ$ with $3\cdot2^{L-1}$ at the left endpoint. The lower bound on the start doubles at each index and the left side grows by a factor below two. For the infinite tail the real two-logarithm inequality gives $g(Q)>1/[4(4Q)^{10^{10}}]$. Indeed, apply the bound in Theorem 9.4 of [8] with bases 2 and 3 over $\mathbb Q$, modified heights 1 and 2, and exponents $i,-k$ with $k$ nearest to $i\alpha$. The coefficient is below $10^{10}$ and $|2^i3^{-k}-1|<4\|i\alpha\|$ by the mean value theorem. For $U=N$ or $L$ with $U\ge2^{41}$, $Q\le4U$ and $4Q(4Q)^{10^{10}}<100U^2(32U)^{10^{10}}<2^{U/3}<2^{U-2}$. The middle comparison holds at $2^{41}$ since $89+46\cdot10^{10}<2^{41}/3$, and propagates by differentiation. These ranges overlap the rational checks. The clock and first-mismatch deduction concern the shortcut map in a closed factor-three band. Related prior work bounds visits of odd states to physical bands in §11.3 of [9] and gives source bounds for prescribed critical Sturmian words in [10].

### First mergers and shared exits

Let an upper exit from $[x,3x]$ end at time $\tau$. Its departure word begins odd and has no two consecutive even departures, since two halves from a state at most $3x$ fall below $x$. Suppose a smaller source first hits the exit segment at $v\ne x$. The incoming edges differ, so the two parents are an odd $u$ and an even $2v=3u+1$. The upper path must use the odd parent. Use of the even parent would either start even or entail two consecutive halves because $2v\equiv1\pmod3$ has no odd parent. The other path starts below $x<2v$, so it takes the two halves $6u+2,3u+1,v$ and reaches at least $6x+2$. Thus under cap $6x+1$, the first hit time of the exit segment from any smaller source equals its first hit time at $x$, with infinity for a miss and with any deadline.

The bound is sharp for $x=607+648k$, $z=479+512k$, $k\ge0$. At $k=0$ the original prefix is $(607,911,1367,2051)$, and the competing prefix is $(479,719,1079,1619,2429,3644,1822,911)$. Their increments per unit $k$ are $(648,972,1458,2187)$ and $(512,768,1152,1728,2592,3888,1944,972)$ respectively. The even increments at odd departure states and the shortcut recurrences verify the affine paths. Writing them as $(a_i)$ and $(b_i')$, the constants and slopes give $b_0'<a_0<b_1'<a_1<b_2'<a_2<b_3'<b_6'<a_3<b_4'<b_5'$, with $a_2<3x<a_3$. Thus the exit is at $a_3$ and the competing first hit is $b_7'=a_1$, with peak $b_5'=6x+2$.

For two first upper exits to a common target, the same incoming-edge argument shows that the shorter word is a suffix of the longer one. A divergence going backward with both paths still present would force one path to start even or contain two consecutive halves. The longer path reaches the shorter source inside its own band, hence starts strictly below it by distinctness. This applies to shared upper exits, whose first intersection is at the shorter source.

### Densities

The first mismatch at position $i$ fixes one residue modulo $2^i$. Consequently the upper-exit density of starts is $\sum_{b_i=0}2^{-i}$, with the undecided starts through $M$ in a single class modulo $2^M$. For an upward word of length $i$, with $k_i=\lceil i\alpha\rceil+1$ odd bits, the source and target progressions have steps $2^i$ and $3^{k_i}$ respectively. Each positive target in the ternary class gives an integral source with the prescribed parity word by the affine congruence for the word. Backwards, its integral inverse states are positive. The word starts with 11, excluding source 1. The first-mismatch rule therefore applies to every such positive target. Two intersecting target classes are nested, with containment precisely when the corresponding exit word is a suffix of the longer one.

Let $\Delta_M$ be the density of starts sharing their upper exit with a smaller source, keeping words through depth $M$. Pulling back each compatible target class to the shorter source class gives a ternary cylinder in its progression parameter. The finite union has rational density by removing contained cylinders and summing across shorter source classes. An omitted longer witness of length $j>M$ supplies at most $j-1$ larger starts; through cutoff $X$ the number of such witnesses is at most $X2^{-j}+1$, and $j\le 2\operatorname{bitlength}(X)+3$. This gives the limit density $\Delta$, with $0\le\Delta-\Delta_M\le(M+1)2^{-M}$. At depth 150 the replay gives 55 upward words, 150 compatible pairs, and $\Delta=0.01568956974951342115\ldots$.

For distinct targets, unflip the terminal bit of each upper word to get the corresponding prefix of $(b_i)$. Its proper nonempty suffixes that are also prefixes correspond exactly to containing exit cylinders. Write $R_i=\{i\alpha\}$. For a candidate suffix starting after position $l$, its first $t$ bits have the same sum as the length-$t$ prefix exactly when $R_l+R_t>1$. When $R_i$ is a new maximum, this fails at $t=i-l$ for every $l<i$. Otherwise take the earlier maximum at $l$, so $R_{l+t}<R_l$ throughout and each of these additions wraps. Thus the maximal target cylinders correspond to record indices $i\ge2$, which have last bit 0 before the flip. The density of distinct targets is

$$
\theta_1=\sum_{\substack{i\ge2\\R_i>\max_{j<i}R_j}}3^{-\lceil i\alpha\rceil-1}
=0.0371900800527872959\ldots .
$$

More generally the density $\theta_b$ of targets with at least $b$ sources is the union measure of cylinders with at least $b-1$ proper containing cylinders. For $b=2$ the replay gives $0.00413223140495380068\ldots$. The tail past depth $M$ is at most $\sum_{j>M} 2^{-j}/3=2^{-M}/3$, uniformly in $b$, since $3^{k_j}>3\cdot2^j$. To obtain a progression with exactly $b$ sources, extend an upper prefix to longer prefixes having it as a suffix, by choosing phases $R_l$ arbitrarily close to 1 using irrational rotation. Pick a word with exactly $b$ upper suffixes counting itself, which is possible by selecting the $b$th shortest in such a chain. Impose that its source is divisible by 3 in addition to the binary class. This gives one progression of targets by CRT. Beyond that source no further backward edge of an upper word can occur, since the odd inverse requires residue 2, and the even inverse in an upper word must be preceded by an odd departure and hence requires target residue 1. This gives exactly $b$ sources for each positive target in the progression.

Taking $M=2\operatorname{bitlength}(X)+3$ gives the full counts through $X$, since every source of a target $y\le X$ is below $y/3$. Rounding each progression count costs at most one. There are at most $\binom M2$ paired source classes and at most $M$ target classes after containment removal. The tail bounds above give errors $O(\log^2 X)$ and $O(\log X)$ respectively from density times $X$, the latter uniform in $b$.

## 7. Competitive peaks relative to the original peak

### A five-step family

Let $m\ge3$ and take $x=3^m u$ with $u$ the least positive solution of $3^m u\equiv23\pmod{32}$ and $1+2\cdot4^m u\equiv0\pmod{3^{m+5}}$. Then $3^m\le x<32\cdot3^{2m+5}$. The orbit takes three odd steps to $P=y_3=(27x+19)/8$, followed by two halves. The binary class gives $4\mid P$, and $x<P/2<P<4x$ gives the first descent at time five, with $q=P/2$ the last pre-descent state. Since $P\equiv2\pmod3$ and $q\equiv1\pmod3$, the only immediate predecessor of $q$ is $P$. A smaller source reaches a pre-descent target only by hitting the three-step upper-exit segment. Section 5 gives $H>mx$ and $H>cxm^{1/\eta}$, so $H/P>m/4$ and $H/P>(c/4)m^{1/\eta}$. The size bound makes the elementary ratio at least logarithmic along the family. Section 6 gives the separate bound $H\ge6x+2>P$ at its first possible merger, so $x$ attains the source floor for every target under cap $P$ once its own arrival deadline is met. This applies also at $m=3$.

The inverse word from Section 3 gives a positive smaller source $z$ that first meets this excursion at $y_1$ after $3m+8$ steps, with peak $W=2+6\cdot4^m u$. To include the descent endpoint $d=P/4$, first note that all states during the odd run before $W$ are odd, while $q$ is even and $W>P$. The odd run misses the ascent by the comparison with $y_j+1$ in Section 3. Also $2z<x$, from the bound $z/x<(128/243)(8/9)^m$, so $z<C(z)<(3x+2)/4<d$. For times at least two on the odd run, the state plus one is divisible by 9, whereas $32(d+1)=3(9x+17)$ has valuation one. The remaining intermediates through $P_0=6x+2$ are at least $4x+1>P$. Then $2y_1$ lies strictly between $y_2$ and $P$ and exceeds $q$. These tests exclude all earlier meetings. From $y_1$ the witness reaches $q$ in three more steps and $d$ in four, with peak $W$ throughout. The endpoint $d$ itself is a source at time zero.

### Long excursions with prescribed peak costs

**Theorem 4.** For every integer $K\ge1$ and real $B\ge1$, there is an infinite arithmetic progression of positive starts $x$ with finite first descent $D>K$. For each member, every smaller-source arrival at any $b'\in S_x$ has peak $H>BP$, where $P=\max S_x$. A specified smaller source reaches the last pre-descent state. In particular the source floor under cap $BP$ and with unrestricted time is $x$ at every pre-descent target.

For each fixed $K$ there is also a constant $c_K>0$ and an unbounded sequence of such starts with $D>K$ and $H/P\ge c_K\ln x$ for every smaller-source arrival into $S_x$. With the same $c_K$, there are such finite arithmetic progressions of any prescribed length. Each selected start has a smaller source reaching its last pre-descent state. Section 10 strengthens the rate on these sequences and finite progressions.

In any infinite arithmetic progression whose sufficiently large starts have finite $D>1$, an infinite subprogression admits smaller-source arrivals at $C(x)$ with $H/P$ bounded by a constant depending on the subprogression. In particular, no such full infinite progression has a uniform positive logarithmic lower bound on the competing peak ratio. This obstruction concerns a competitor somewhere in $S_x$, specifically $C(x)$.

### Inverse gains and the existence of an anchor

An inverse word of length $t$ with $r$ odd inverses has gain $g=3^r/2^t$. Its legal set in $\mathbb Z_3$ is one residue class modulo $3^r$. Its endpoint at a legal root $v$ is $v/g-c$ with $c\ge0$. These statements follow by induction on inverse letters, since each odd inverse prescribes one more trit of the root and costs a nonnegative affine offset. At positive integer roots every legal word has a positive endpoint. Let $G(v)$ be the supremum of gains over all legal finite words, with the empty word of gain 1, and write $\pi$ for normalized Haar measure on $\mathbb Z_3$.

For $d\ge1$, $\pi(G>d)\le d^{-2}$. Give independent inverse letters $F,E$ probabilities $3/4,1/4$. A word's tilted probability divided by its legal Haar mass $3^{-r}$ is $g^2$. First strict crossings of $d$ are prefix-free, so their Haar masses sum to at most $d^{-2}$. This is the first-crossing argument of the author's earlier inverse-gain note, used below also for numerical enclosures. A precedent for the squared-gain tilt is equation (5) in §3 of [11], using grouped halving valuations. Section 6 of that paper uses stopped-shell estimates to bound the tail of the ternary Syracuse density. The event here is the existence of a legal inverse word crossing the gain threshold, and the Haar bound follows from the word sum above.

Put $U_j=1+3^j\mathbb Z_3$. The relative mass with $G>1$ in $U_j$ tends to zero. A word on $U_j$ matches the inverse path at 1 through its $j$th odd inverse and any following doubles, by the divisibility of the difference before each odd inverse. At the auxiliary endpoint $s\ge1$, the affine formula gives $g\le1/s$. Any first crossing above 1 therefore needs more than $j$ odd inverses. At the $j$th odd inverse, each possible stopped word takes Haar-uniform roots in $U_j$ to Haar-uniform endpoints in $\mathbb Z_3$, since its scale on the free coordinate is a power of two. The conditional chance that a continuation raises the total gain above 1 is at most $g^2$. For fixed $j$, at most one such word goes to any positive integer $s$ from 1. The forward orbit of $s$ determines all visits to 1, and these differ by laps of $1,2,1$, each with one odd step. For a fixed $s$, additional laps multiply the gain by $3/4$, so the squared gain tends to zero as $j$ grows, using zero when the word is absent. The bound $s^{-2}$ permits summation by dominated convergence. The union bound proves the claim.

Every $U_K$ contains a full ball $V$ with $G>5/3$. Follow $(EF)^K$, which is legal throughout $U_K$ and maps it onto $\mathbb Z_3$. Require the endpoint to be $-1\bmod3^\ell$ to allow $\ell$ more odd inverses and choose $\ell$ with $(3/4)^K(3/2)^\ell>5/3$. The affine map $A(v)=(3v+1)/4$ takes $U_j$ to $U_{j+1}$ and has $G(A(v))\ge(3/4)G(v)$ via $EF$. The relative mass of $A^j(V)$ inside $U_{K+j}$ stays positive and fixed. For a sufficiently large fixed $j$, a positive-measure set of $v\in V$ has $G(A^j(v))=1$ by the preceding paragraph. At its first index $i$ with $G(A^i(v))\le5/3$, the preceding gain exceeded $5/3$, so the new gain exceeds $5/4$. Split the set by the finitely many $i$ and use the constant Haar scaling of $A^i$. This proves

$$
\pi\{v\in U_K:5/4<G(v)\le5/3\}>0. \tag{1}
$$

We transfer (1) to positive integers using two elementary counting facts. Write $\alpha=\log_3 2$, $h=H_2(\alpha)$, and $\rho=2^{h-1}<1$. The number of length-$j$ words with at least $\alpha j-1$ odd bits is $O(2^{hj})$. This follows from the binary entropy bound at $\alpha$ and the bounded ratio of adjacent binomial coefficients for the at most one added level. For an interval $I$ and a union $\mathcal U$ of $N_0$ full positive orbits,

$$
|\mathcal U\cap I|\le |C^k(I)|+2N_0 k.
$$

For the latter inequality add the orbits in order. Disjoint new pieces are simple paths or cycles. Delete the last at most $k$ states of each finite path. The $k$th iterate on the remaining points is injective, with images still within their respective pieces. For $I=[1,\lfloor Y\rfloor]$ and $k=\lfloor\log_2 Y\rfloor$, $|C^k(I)|=o(Y)$. Choose $1/2<p<\alpha$. Words with at least $pk$ odds give $O(2^{kH_2(p)})=o(Y)$ sources, since each word defines a residue class modulo $2^k$ and has at most two representatives in $I$. For the remaining sources the affine formula and maximal all-odd offset give image at most $3^{pk}Y/2^k+(3/2)^k=o(Y)$. These orbit-count and image estimates are the elementary prerequisites from the author's earlier orbit-union and entry-profile notes.

Fix a level $d\ge1$ and a ternary ball. Roots with $G>d$ by clock $J$ form a finite residue-class union, with equal natural density and Haar mass. For an integer $v\le Y$ requiring a longer word, use its first strict crossing of $d$, of length $t>J$, with endpoint $1\le s\le v/g<Y$. In forward order from $s$, every nonempty prefix has multiplicative slope greater than 1, since its gain is the crossing gain divided by the gain of a proper reverse prefix. If $J<t<k=\lfloor\log_2 Y\rfloor$, the length-$t$ word count and dyadic classes allow at most $O(Y\rho^t)$ pairs $(s,t)$. If $t\ge k$, the first $k$ bits allow only $O(Y^h)$ sources. The orbit-union bound shows that their full orbits have $o(Y)$ possible roots up to $Y$. Thus the omitted integer upper density is $O(\rho^J)$, including within the fixed ball. In Haar measure the finite unions increase to $\{G>d\}$ in that ball. Taking $J\to\infty$ proves equality of the natural density and Haar mass. Subtracting the strict thresholds $5/4$ and $5/3$ proves that (1) gives a positive-density set of **integer** roots $b\equiv1\pmod{3^K}$ with $5/4<G(b)\le5/3$.

### Proof of Theorem 4

Fix an integer anchor $b$ from that set. Only finitely many legal words at $b$ have gain at least 1. Their endpoints are positive and at most $b$. For each endpoint the forward orbit is deterministic. If it reaches $b$ repeatedly, the return is affine with slope $\lambda$ and positive offset, since a positive cycle has an odd departure. The equation $b=\lambda b+\text{offset}$ forces $\lambda<1$. Each extra lap multiplies the gain by $\lambda$, so only finitely many gains on each orbit are at least 1. Choose a word $w_*$ of greatest gain $G=G(b)$, taking least endpoint $s_*$ among ties. Write $t,r_*$ for its length and odd count. Equal gains force equal length and odd count by unique factorization. Every proper prefix has gain strictly less than $G$. Any word with at most $K$ odd inverses also matches at 1, where its gain is at most 1. Therefore $t\ge r_*>K$.

For $m\ge r_*$ and positive $3^m\mid\Delta$, put $q=b+\Delta$ and $x=s_*+\Delta/G$. Each prefix $v$ of $w_*$ lifts to the state $s_v+\Delta/g_v$, with $s_v$ its endpoint at $b$ and $g_v$ its gain. For all sufficiently large $\Delta$, all proper prefixes exceed $x$ and $x<q<2x$, because $1<G<2$. Require $q$ even. The forward path from $x$ then first descends at time $t+1$ to $q/2$. Its pre-descent peak satisfies $P\le L\Delta$, where $L=\max_{v\preceq w_*}(s_v+1/g_v)$.

Every word at $b$ that lifts has endpoint at least $x$ for sufficiently large $\Delta$, uniformly in the word. Gains below 1 give endpoints exceeding $\Delta\ge x$ for large $\Delta$. The finitely many words with $1\le g<G$ have larger inverse slope, and at $g=G$ the endpoint is at least $s_*+\Delta/G$. A path from $q$ with at most $m$ odd inverses matches at $b$, since the state difference before each matched odd edge is $2^j\Delta/3^i$ with $i<m$. This also allows any following doubles. Thus any smaller source that reaches $q$ uses more than $m$ odd inverses.

Take any arrival from below $x$ at a pre-descent target and append the original suffix to $q$. Its extended peak $H_{\rm ext}$ obeys $H\le H_{\rm ext}\le\max(H,P)$. In the matched inverse path through the $m$th odd edge, the initial ratio $s/d$ is $b$. Section 2 sums the decrements to give

$$
H_{\rm ext}>\frac{m\Delta}{3b}.
$$

For $m>3bL$ this bound exceeds $P$, so $H=H_{\rm ext}$ and $H/P>m/(3bL)$. The argument uses arbitrary finite clocks and counts every visit, including repeats.

To ensure a real arrival, start at the ternary unit $b$ and prescribe $m$ odd inverses, placing before each between zero and five doubles so the odd inverse input is $2\bmod9$. This is possible because 2 generates the units modulo 9. The new endpoint is $1\bmod3$ at each such edge. If the resulting prefix has length $a$, gain $g_0$ and endpoint $s_0$, then $a\le6m$ and $g_0\ge(3/64)^m$. Choose the least $\ell$ with $g_0(3/2)^\ell>2G$. The inequalities $(3/2)^8>64/3$ and $(3/2)^3>10/3$ give $\ell\le8m+3$. With $\Delta=3^m d_0$, require $s_0+2^a d_0\equiv-1\pmod{3^\ell}$ to allow the final $\ell$ odd inverses. This specifies one class for $\Delta$ modulo $M=3^{m+\ell}$, and parity specifies one class modulo $2M$. For every such sufficiently large $\Delta\ge b$, the positive integer endpoint $z$ satisfies $z\le q/[g_0(3/2)^\ell]<q/(2G)\le\Delta/G<x$. Its forward path reaches $q$.

For a given $K,B$ fix $m>3bBL$ with $m\ge r_*$. All sufficiently large lifts in the selected class form an infinite progression of $x$ of step $2^{t+1}3^{m+\ell-r_*}$. They have $H>BP$, and the original prefixes all fit cap $BP$. To obtain a logarithmic bound, instead let $m$ grow and use the unique representative $\Delta\in[2M,4M)$. It tends to infinity and $x<(s_*+4/G)3^{9m+3}$. For large $m$, $\ln x\le18m\ln3$, so $c_K=1/(54bL\ln3)$ works. The same estimate holds on the first $N$ lifts for each fixed $N$, once $m$ is sufficiently large depending on $N$. The new upper bound $(2N+2)M$ on $\Delta$ only changes the additive constant in $\ln x$. The finite progressions retain the same constant $c_K$, which depends on the anchor for $K$.

For the obstruction, every sufficiently large start of the given progression is odd, since even starts have $D=1$. Its first iterates $y=(3x+1)/2$ form a progression of ternary units of step $h_0>0$. Fix a member $y_0$ and put $r=v_3(h_0)$. At $y_0$ prescribe the same unit-preserving inverse prefix with $r$ odd edges, then impose a class allowing enough final consecutive odd inverses for total gain $g>2$. The resulting class modulo $3^{r+\ell}$ agrees with $y_0$ modulo $3^r$. It intersects the target progression in an infinite subprogression, since $\gcd(h_0,3^{r+\ell})=3^r$; this includes $r=0$ with an empty prefix. On that subprogression the fixed word gives a positive endpoint at most $y/g<x$, using $y\le2x$. Its peak is at most $y\max_v(1/g_v)$ over its inverse prefixes, by nonnegativity of the affine offsets. Since $y\in S_x$, $P\ge y$. This proves the claimed bounded ratio on the subprogression. $\square$

## 8. Density of the absolute source floor before descent

Let $u(q)$ be the least positive integer whose forward orbit ever visits $q$, allowing time zero. Define $\mathcal A$ to be the starts $x>1$ with finite first descent and with every pre-descent state outside the full orbits of all smaller positive starts. The previous constructions have positive smaller visitors when their caps are lifted. Membership in $\mathcal A$ excludes smaller visitors at every height and clock.

**Theorem 5.** Almost surely in $\mathbb Z_3$ the maximum gain $G$ is attained and its maximizing length $T$ is unique. For any set $I_D$ of positive integer descent times, the natural density is

$$
\operatorname{dens}\{x\in\mathcal A:D(x)\in I_D\}
=\frac12\int_{\mathbb Z_3}G\,{\bf1}_{G<2,\ T+1\in I_D}\,d\pi . \tag{2}
$$

In particular $\operatorname{dens}\mathcal A=\tfrac12\int G{\bf1}_{G<2}\,d\pi$. The density for $D>K$ is positive for every fixed $K\ge1$ and is $O(\rho^K/(1-\rho))$.

**Proof.** The penultimate state $q$ of any first descent is even and $q/2<x\le q$. A smaller source meets the excursion before descent exactly when some smaller source ever reaches $q$, by forward continuation. Thus $x\in\mathcal A$ implies $u(q)=x$. Conversely, if $q$ is even with $q/2<u(q)$, the path from $x=u(q)$ to its first visit at $q$ consists entirely of ancestors of $q$, hence states at least $x$. The next step is below $x$. This gives a bijection, since the penultimate state is determined by $x$. Its first-arrival clock from $u(q)$ is $D-1$. The correspondence includes $q=x$ with clock zero, and $x\le X$ implies $q<2X$.

At reverse deadline $J$, let $u_J(q)$ be the minimum source and let $G_J,T_J$ be the largest gain and its length. On each class modulo $3^J$, the available words are fixed. Their affine endpoints select, for all sufficiently large $q$ in the class, the greatest gain and then the largest offset $c$ in $q/G_J-c$. Equal gains have the same length by unique factorization. The minimizing source first arrives at clock $T_J$ for all sufficiently large $q$: a word of a different length has different slope and can coincide in endpoint only at an isolated $q$, and there are finitely many words. In the class, half the integers are even, and $u_J(q)\le X$ cuts off $q$ at $G_J X+O_J(1)$. The inequality $q/2<u_J(q)$ eventually selects exactly $G_J<2$, since $3^r/2^t=2$ is impossible. Thus the count of even targets with $q/2<u_J(q)\le X$ and first-arrival length plus one in $I_D$, divided by $X$, tends to the right side of (2) with $G_J,T_J$.

For the all-time minimum, use the following uniform target estimate. Let $E_J(X)$ consist of $q\le2X$ admitting some positive source $s\le2X$ and an arrival at a time $n>J$ whose states are all at least $s$. Then

$$
\limsup_{X\to\infty}\frac{|E_J(X)|}{X}=O(\rho^J), \tag{3}
$$

with an absolute constant. To prove this, starts $s\le X^{1/2}$ contribute $o(X)$ targets by the orbit-union bound in Section 7, at $k=\lfloor\log_2(2X)\rfloor$. For the others, at each $j\le\min(n,k)$ with odd count $r_j$ the physical product gives

$$
1\le C^j(s)/s\le 3^{r_j}2^{-j}\exp(j/(3s)).
$$

For large $X$ this implies $r_j\ge\alpha j-1$. For $J<n<k$ the length-$n$ word count bounds the number of pairs $(s,n)$ by $O(X\rho^n)$ at each length. For $n\ge k$ there are only $O(X^h)$ possible sources by the first $k$ bits. Their full orbits contribute $o(X)$ targets by the same orbit-union bound. Summation proves (3). The first arrival from $s=u(q)$ stays at or above $s$ by minimality, so outside $E_J(X)$ the finite and infinite source minima and their first-arrival clocks agree. Both target counts use $q<2X$, so the error estimate holds uniformly over the restriction to $I_D$.

For Haar measure the expected number of legal length-$t$ words with gain at least 1 is at most $2^{-t}\sum_{r\ge\alpha t}\binom tr\le\rho^t$. The estimate is summable, so almost surely there are only finitely many such words. Since the empty word is available, $G_J,T_J$ stabilize, $G$ is attained, its length is unique, and $G\ne2$. The finite integrands are bounded by 2 before the factor $1/2$, so bounded convergence and the physical error estimate give (2). For $D>K$, (1) gives positive mass because every maximizing word on its set has more than $K$ odd inverses. For the upper bound sum the legal-word estimate over $t\ge K$, which contains all maximizing lengths with $T+1>K$. $\square$

### Finite enclosures and physical counts

Write $\delta_J$ for the integral in (2) without the time restriction and with the finite maximum. The exact cylinder histogram at $J=28$ gives $\delta_{28}=50983196898175771/103997395628457984$. This integral is distinct from the limiting value. To enclose the limit, a threshold $1\le s\le2$ can be crossed in the omitted suffix only by a word whose first strict crossing comes after $J$. Under the tilted letter law of Section 7, let $\tau_s$ be the first strict crossing. Summing the legal masses gives $\pi(G_J\le s<G)\le s^{-2}\Pr(\tau_s>J)$. The increase of $G{\bf1}_{G<2}/2$ over its truncated version is bounded above by the increase of $\min(G,2)/2$. Integrating the crossing bound over $s\in[1,2]$ controls the upward error. The survival probability through $J$ is constant between the finitely many gains at those clocks, so each term integrates $1/s^2$ exactly. A downward change can cost at most 1 and requires a first crossing of 2 after $J$. The code sums the legal masses of such words through $J+128$ and bounds the later mass by $\Pr(\tau_2>J+128)/4$. The resulting rational calculation with outward decimal rounding gives $\delta\in[0.4837662988,0.4946313229]$. The physical census counts 122,114 starts at or below 250,000 using complete sampled smaller orbits. The natural-density argument is the all-time transfer in Theorem 5.

## 9. Density of starts with expensive smaller visitors

For $B\ge1$ let $W_B$ consist of the starts with finite first descent, a smaller visitor to $S_x$, and peak $H>BP$ for every smaller-source arrival at any member of $S_x$. Write $W_{B,K}=W_B\cap\{D>K\}$ for integers $K\ge0$. The cap $BP$ is inclusive and uses the peak of the whole original pre-descent excursion, while the peak of a visitor includes only its own path through the arrival.

**Theorem 6.** For each fixed $B\ge1$ and $K\ge0$, $W_{B,K}$ has positive natural density. For $B>1$,

$$
\operatorname{dens} W_{B,K}\le\operatorname{dens} W_B\le\frac{1}{B-1}. \tag{4}
$$

For any real threshold $B(x)\to\infty$, the starts with a smaller visitor but no smaller arrival through peak $B(x)P(x)$ have natural density zero. Section 10 gives a stretched-exponential lower bound in $B$.

### Existence of the density and the two clocks

For $q=C^{D-1}(x)$, a smaller visitor to $S_x$ can be extended to $q$ along the original path. The equivalence works separately for unrestricted arrivals and for arrivals under the inclusive cap $BP$, since $B\ge1$. It holds also when $q=x$. The descent endpoint $q/2$ is outside $S_x$.

Fix an original deadline $T_0$ and restrict to $K<D\le T_0$. Test independently for a smaller visitor to $q$ by time $J$ with no cap and for a smaller visitor to $q$ by time $J$ under cap $BP$. For fixed $T_0,J$, both tests stabilize jointly on each residue class modulo $2^{T_0}3^J$. The parity word up to $T_0$ is fixed and original states are affine functions of $x$, so the first-descent decision and the choice of a peak state stabilize. For any given choice of $q$, its residue modulo $3^J$ is fixed and every legal inverse path of length at most $J$ has prefix states affine in $x$. The smaller-source comparison and the inclusive cap comparisons then stabilize by the sign of each affine difference, including at equal slopes and for real $B$.

If one test misses an arrival that exists at a later time, choose the least eligible smaller source for that test and its first arrival at $q$. Every state through the arrival is at least that source, because its suffix still reaches $q$ and, for the capped test, still fits the same cap $BP$. For $x\le X$, such a discrepancy gives a target in $E_J(X)$ from (3), since $s<x\le X$ and $q<2x$. At fixed $T_0$, at most $\sum_{i=0}^{T_0-1}2^i$ original starts with $D\le T_0$ can share a given $q$, by counting inverse words from $q$. Thus the difference in upper density between the finite tests and the actual set with $K<D\le T_0$ is $O_{T_0}(\rho^J)$. Sending $J$ to infinity first proves its natural density.

To remove the original deadline, a start with finite $D>T_0$ stays at or above $x$ through $T_0$. For fixed $T_0$ and large $x$, the forward product comparison in Section 8 forces odd count at least $\alpha T_0-1$. These dyadic classes have density $O(\rho^{T_0})$ with an absolute constant. Sending $T_0$ to infinity now proves existence for $W_{B,K}$. Positivity follows from the infinite progression of Theorem 4, using $K=1$ also for the case $K=0$.

### Peak of the least ancestor's path

Let $H_0(q)$ be the peak from $u(q)$ through its first visit to $q$, rather than the minimum peak over all smaller visitors. For $A>1$ we show

$$
\limsup_{X\to\infty}\frac{1}{X}\#\{q\le2X:\ q\text{ even},\ H_0(q)>Aq\}
\le A^{-1}. \tag{5}
$$

First restrict that first visit to time at most $J$. On each fixed ternary class modulo $3^J$, the least source at this deadline must, for all sufficiently large targets, come from a maximal-gain word, as in Section 8. Its terminal gain is at least 1 by the empty word. At each reverse prefix of gain $g$, the physical inverse endpoint is $q/g-c$ with $c\ge0$. A peak greater than $Aq$ therefore forces a prefix with $g<1/A$. The word subsequently recovers to gain at least 1.

In the tilted independent letter law of Section 7, $1/g$ is a nonnegative mean-one martingale: its one-step mean factor is $(1/4)2+(3/4)(2/3)=1$. The probability of a strict drop $g<1/A$ by time $J$ is at most $1/A$ by the maximal inequality. Stop a word at its first recovery to $g\ge1$ after its first strict drop. The stopped words are prefix-free in word space and their total tilted probability through time $J$ is at most $1/A$. The legal ternary mass of each is its tilted probability divided by its terminal $g^2$, so the union of their legal classes also has mass at most $1/A$. This union bound allows overlap between legal cylinders. Even targets in $[1,2X]$ sample each such class with its Haar frequency after division by $X$. When the globally least ancestor first arrives later than $J$, its path has all states at least $u(q)$ and belongs to (3). Thus $J\to\infty$ gives (5).

### Multiplicity at a shared penultimate state

Fix $B>1$ and first count starts with $x\le X$ and $K<D\le T_0$. At each shared even $q$, list them as $x_1<\cdots<x_k$. The genuine visitor for $x_1$ gives $u(q)<x_1$, so $H_0(q)>BP(x_1)$. For every $i<k$, the original path from $x_i$ to $q$ is itself a smaller visit for $x_{i+1}$. Consequently $P(x_i)>BP(x_{i+1})$ and $H_0(q)>B^k P(x_k)\ge B^k q$. Each inverse edge increases its state by at most a factor two, so $P(x_1)\le 2^{T_0}q$. Since $P(x_k)\ge q$, the chain gives $k\le1+\lfloor T_0\ln2/\ln B\rfloor$.

Count the starts by summing, over this finite range of multiplicities $j$, the numbers of targets with at least $j$ such starts. Each has $H_0(q)>B^j q$, hence its contribution in upper density is at most $B^{-j}$ by (5). Summing gives at most $1/(B-1)$, independently of $T_0$. The same original-deadline tail removes $T_0$ and proves (4). For the variable threshold and every fixed $B>1$, all sufficiently large starts in question belong to $W_B$. Sending $B$ to infinity gives density zero. This diagonal conclusion concerns starts with genuine smaller visitors.

## 10. Superlogarithmic competing peaks

**Theorem 7.** Let $\eta=\eta_0=H_2(3/5)<1$ for the elementary bound. Using (P2) from [7], one can instead take its exponent $\eta=H_2(\log_3 2)-\gamma>0$, strictly smaller than $\eta_0$. For each fixed integer $K\ge0$ there is $c_{K,\eta}>0$ and an unbounded sequence of starts with $D>K$ and a genuine smaller visitor reaching $q$, on which every smaller-source arrival into $S_x$ satisfies

$$
H/P\ge c_{K,\eta}(\ln x)^{1/\eta}. \tag{6}
$$

With the same constant, for every prescribed $N$ there are $N$-term progressions arbitrarily far out with these properties. Also for every fixed $B\ge1$, an infinite arithmetic progression is contained in $W_{B,K}$. For positive constants $a_{K,\eta},A_{K,\eta}$,

$$
\operatorname{dens} W_{B,K}\ \ge\ a_{K,\eta}\exp(-A_{K,\eta} B^\eta) \qquad (B\ge1). \tag{7}
$$

The obstruction in Theorem 4 applies to a whole infinite progression with eventual $D>1$. The progression used to prove (7) is chosen for fixed $K,B$.

### A distinct-state count on one orbit

Uniformly in a complete positive orbit $O$, one has $|O\cap[1,Y]|=O(Y^{\eta_0})$ for $Y\ge2$. Put $j=\lceil\log_2 Y\rceil$. Each length-$j$ parity word has at most one representative in $[1,Y]$, and words with at least $3j/5$ odd steps number at most $2^{jH_2(3/5)}$. For the other words the affine formula bounds the image by $Y3^{3j/5}/2^j+(3/2)^j$. Both $\tfrac35\log_2 3$ and $\log_2(3/2)$ are strictly below $\eta_0$, as follows from $5^5>4\cdot3^6$ and $2^3 5^5>3^8$. Thus $|C^j([1,Y]\cap\mathbb Z)|=O(Y^{\eta_0})$. The orbit-union count in Section 7 for one orbit transfers this image bound to distinct states, including eventual cycles. The bound (P2) from §8.1 of [7] instead gives $O(Y^\eta+\log^2Y)=O(Y^\eta)$. Since $1/2<3/5<\log_3 2$, binary entropy decreases strictly between the last two arguments.

### Applying the count to arbitrary arrivals

Use the anchor $b$, maximizing word $w_*$, and $L$ of Section 7, with $K$ replaced by 1 when $K=0$. For $m\ge r_*$ and large admissible $\Delta$, the construction gives $q=b+\Delta$, $x=s_*+\Delta/G$, $P\le L\Delta$, $D=t+1>K$, and a smaller visitor reaching $q$. The cutoff for $\Delta$ is independent of $m$. Any smaller arrival to $S_x$ extends to $q$ with peak $H_{\rm ext}\le\max(H,P)$, and its reverse word has more than $m$ odd inverses. Through its $m$th odd inverse it matches at $b$. Put $R_*=H_{\rm ext}/\Delta>1$. At each matched prefix the states are $s+d\Delta$ and $s$, and $s/d\le b$ by Section 2. It follows that $d<R_*$ and $s\le bd<bR_*$. These auxiliary states lie on the single forward orbit from the last matched auxiliary state. Either orbit estimate bounds their distinct odd endpoints by $O_b(R_*^\eta)$.

A repeated auxiliary vertex is periodic with a forward path to $b$, so $b$ then lies on that cycle. The reverse path can initially follow complete laps and a partial lap, followed by at most one departure from the cycle. A return to the cycle after departure would contradict forward invariance of the cycle. For the period $p$ through $b$, its forward affine slope $\lambda$ satisfies $0<\lambda<1$, since a positive cycle has an odd departure and $b=\lambda b+c$ with $c>0$. After $i$ complete initial laps the inverse multiplier is $\lambda^{-i}<R_*$. Hence repeated odd endpoints beyond the distinct count contribute at most $p(1+\ln R_*/\ln(1/\lambda))$. For a nonperiodic anchor there are no repeats. This proves

$$
m\le C_{b,\eta}R_*^\eta,
$$

uniformly over the competing path, $m$ and $\Delta$. Thus $H_{\rm ext}\ge\Delta(m/C_{b,\eta})^{1/\eta}$. For large $m$ this exceeds $P$, so $H=H_{\rm ext}$ and $H/P\ge (m/C_{b,\eta})^{1/\eta}/L$.

With the representative and its first $N$ lifts from Section 7, $\ln x\le9(\ln3)m+O_{K,N}(1)$. For any fixed $N$, taking $m$ large absorbs the additive term using $\ln x\le18(\ln3)m$, giving (6) with a constant independent of $N$. The starts tend to infinity since $\Delta\ge2\cdot3^m$. For fixed $K,B$, choose $m$ just above a sufficiently large multiple of $1+B^\eta$, so the last peak bound is strictly greater than $B$. All sufficiently large lifts in the class give the whole infinite progression of starts, whose step is $2^{t+1}3^{m+\ell-r_*}\le2^{t+1}3^{9m+3}$. Its density is the reciprocal step, giving (7).

## 11. The affine law of the least competing peak

For a start with finite first descent, let $H_{\min}$ be the least peak over smaller-source arrivals at its even penultimate state $q$, allowing arbitrary time. Use $H_{\min}=\infty$ when there is no smaller visitor. Write $R(x)=\max(1,H_{\min}/P)$. This is also the clamped least cost of reaching any member of $S_x$: a visit anywhere in $S_x$ continues to $q$ at peak at most the larger of its own peak and $P$, and $q$ itself is in $S_x$. All densities and measures below are normalized by the number of positive starts through $X$, including when we restrict to $D>K$.

### Affine inverse words

For an inverse word $w$ of length $t$ with $r$ odd inverses, write its endpoint as $a_w q-c_w$, with $a_w=2^t/3^r=1/g_w$ and $c_w\ge0$. Its legal ternary cylinder $A_w$ has Haar mass $3^{-r}$. Define the endpoint pair $f_w=(a_w,-c_w)$ and the peak pair $p_w=\max_{v\preceq w} f_v$ in lexicographic order. The prefixes include the empty word with pair $(1,0)$. Let $s(p)$ denote the first coordinate. On any finite list of affine functions, lexicographic order agrees with eventual order of the values at increasing positive integer roots. This holds after multiplying an entire pair by any fixed real factor.

For $u\in\mathbb Z_3$ let $\mathcal O(u)$ consist of all legal words with

$$
\tfrac12<a_w\le1,\qquad a_w<a_v\quad\text{for every proper prefix }v\prec w .
$$

For fixed words and sufficiently large even roots, these are exactly the original first-descent words from $x=a_wq-c_w$ through $q$ and then to $q/2<x$. All proper prefix states must exceed $x$, since a return to $x$ before a first strict descent would trap the orbit in its pre-descent segment. Equality of slopes at different lengths and the slope $1/2$ are impossible by unique factorization. Thus the inequalities stabilize to the stated slope comparisons. The empty original has $x=q$, $P=q$ and $D=1$.

For $w\in\mathcal O(u)$ let $p_*(u,w)$ be the least peak pair among **all** legal inverse words $v$ with $f_v<f_w$, with the separate value $\infty$ if there is none. The endpoint comparison includes ties of slopes decided by the offsets. Every original or candidate has $g\ge1$. Section 8 bounds the expected number of such legal words of length $j$ by $\rho^j$, where $\rho=2^{H_2(\log_3 2)-1}<1$. Hence almost every root has only finitely many words to consider. Put

$$
R_*(u,w)=
\begin{cases}
\max(1,s(p_*)/s(p_w)),&p_*\text{ finite},\\
\infty,&p_*=\infty .
\end{cases}
$$

**Theorem 8.** For each integer $K\ge0$, the empirical measures

$$
\frac1X\sum_{\substack{1<x\le X\\K<D(x)<\infty}}\delta_{R(x)}
$$

converge weakly on the compactified half-line $[1,\infty]$ to the measure

$$
\mu_K=\frac12\int_{\mathbb Z_3}
\sum_{\substack{w\in\mathcal O(u)\\ |w|+1>K}}
g_w\,\delta_{R_*(u,w)}\,d\pi(u). \tag{8}
$$

It is purely atomic, with every finite atom in $\{2^i3^j:i,j\in\mathbb Z\}\cap[1,\infty)$. Its total mass is $\operatorname{dens}\{D>K,\ D<\infty\}$, which is 1 for $K=0$. The empty original contributes $1/2$ before filters on time or cost. The natural density of missing visitors with $D>K$ is $\mu_K(\{\infty\})$, which also equals the density in Theorem 5 when restricted to $D>K$. For every real $B\ge1$,

$$
\operatorname{dens} W_{B,K}
= \frac12\int_{\mathbb Z_3}
\sum_{\substack{w\in\mathcal O(u)\\ |w|+1>K}}
g_w\,{\bf1}_{p_* \text{ finite},\ p_*>B p_w}\,d\pi(u). \tag{9}
$$

The test for a capped visitor is $p_*$ finite and $p_*\le Bp_w$. Multiplication by $B$ acts on both coordinates. Equality of pairs fits the inclusive cap.

### Source weights, weak convergence and truncation

First impose $D\le T$ on the original and visitor deadline $J$ at $q$. Legal sets are fixed on the ternary classes modulo $3^{\max(T,J)}$, and finitely many comparisons of affine functions stabilize there for sufficiently large even $q$. For each original word, $x\le X$ means $q\le g_w(X+c_w)$. On a class of modulus $M$, even roots advance by $2M$, and the lifted starts advance by $2Ma_w$. Each original therefore contributes $g_w/(2M)$ to the count divided by $X$. Different starts at one target are counted separately. If distinct words at the same root have equal slopes, they have the same length, and equal endpoints would force the same word by determinism. Coincidences of unequal affine functions occur at at most one root per pair. Each physical start determines its own penultimate target. These observations prove the source weights in the finite formulas and in the total mass. In particular for one word the full legal cylinder has weight $g_w\pi(A_w)/2=2^{-t}/2$, and the empty word is legal on all roots.

At fixed $T$, test unrestricted and capped visits separately as in Section 9. In either test, a missed visitor at deadline $J$ gives a least eligible source whose first arrival stays at or above that source, also under the same cap in the capped test. Bound (3) and the original multiplicity bound $2^T-1$ give an upper density error $O_T(\rho^J)$. Thus $J\to\infty$ yields the physical all-arrival formulas at fixed $T$. On the Haar side the finite comparisons stabilize almost surely because only finitely many gain-at-least-one words are legal.

Next let $T\to\infty$. For fixed $T$, a length-$T$ parity class with forward slope less than one has $C^T(x)<x$ at all sufficiently large starts of that class. Equality of slope to one is impossible for $T\ge1$. Therefore the upper density of starts surviving through $T$ is at most $2^{-T}$ times the number of words with slope greater than one, at most $\rho^T$ by the entropy bound. This also proves density zero for starts without a finite first descent. On the Haar side the total original weight at length $t$ is the number of qualifying words times $2^{-t}/2$. It is at most $\rho^t/2$, since all such words have gain at least one. This makes the integrals summable and establishes the all-time strict-cap, absence and total mass formulas.

For every $B>1$ outside the set of potential finite atom locations, slopes alone decide the cap test. The sum of (9) and the absence density then equals $\mu_K((B,\infty])$. These $B$ form a dense set. Together with convergence of the total mass this gives weak convergence: partition $[1,\infty]$ into short intervals in any compatible compact metric with internal endpoints from this dense set and approximate each continuous function by constants on the intervals. At an atom the intercepts govern the physical strict cap test on the slope-equality set. The mass at infinity was counted directly by the absence test.

For $1\le L\le T$, truncating originals at $D\le T$ and visitors at length $J$ changes each of (9), the absence mass, or the mark mass of any specified Borel set in (8) by at most

$$
\rho^L+(2^L-1)\frac{\rho^{J+1}}{1-\rho}. \tag{10}
$$

Indeed the original weight at $D>L$ is at most $\rho^L$ by the physical survival bound and the total-mass identity. The probability of any legal word of gain at least one and length greater than $J$ is at most $\rho^{J+1}/(1-\rho)$. Each root has at most $2^L-1$ original words through $D=L$, each with weight $g_w/2\le1$. Outside the late-word event their marks and tests are unchanged. This gives (10) uniformly in $B,K$ and in the Borel set, using slope marks also in the finite measure. Taking $T=J$ and $L=\lfloor(1-H_2(\log_3 2))J/2\rfloor$ for large $J$ gives exponential convergence of the Haar truncations. The physical transfer above takes the limits in the order $J$ then $T$.

### Exact atom certificates

For even $q=x\equiv2\pmod3$, one odd inverse reaches a smaller source at peak $P=q$, so $\mu_0(\{1\})\ge1/6$. For even $q=x\equiv4\pmod9$ the first inverse must double, and $EFF$ attains a smaller source at peak $2q$. This gives $\mu_0(\{2\})\ge1/18$ with physical cost exactly two.

**Limit $8/3$ from below.** For $q=10+162j$, $j\ge0$, the original is empty in reverse, with $x=P=q$. The word $EFEFFF$ goes to $(64q-73)/81<x$ at peak $H_{\min}=(8q-2)/3$. To prove minimality, explore the strict cap $v<(8q-2)/3$. The live prefixes are the root, $E$ and $EF$, with states $q,2q,(4q-1)/3$, all at least $x$. The children $EE,EFE$ reach or exceed the proposed peak, while $F,EFF$ are forbidden because their parents are $1\bmod3$. The period preserves all parent residues. For the attaining path, the seven affine states at $q=10$ are $10,20,13,26,17,11,7$. Their denominators divide 81, and their slopes are positive and at most $8/3$, so positivity, legality and the peak comparison persist. The endpoint stays smaller than $x$ since its slope is $64/81<1$. Thus the exact physical cost is $8/3-2/(3q)$. These starts have density $1/162$ and give at least that much weak mass at $8/3$, while fitting the inclusive physical cap at that factor.

**Limit $3$ from above.** For $q=4340+4374j$, $j\ge0$, the original reverse word is $FEFF$. It gives $x=(16q-23)/27=2571+2592j$, $D=5$ and $P=(4q-2)/3$. The proper prefix states exceed $x$, and $q/2<x$, from their first values and slopes. The word $EEFFFEFFFF$ goes to $(1024q-2363)/2187<x$ at peak $4q$. Its states at the first root are $4340,8680,17360,11573,7715,5143,10286,6857,4571,3047,2031$. Their affine denominators divide 2187 and their positive slopes are at most four. The endpoint slope is less than $16/27$, so the attaining path persists on the whole progression.

The strict tree below $4q$ has live prefixes

$$
\varnothing,\ E,\ F,\ FE,\ FEE,\ FEF,\ FEFE,\ FEFEE,\ FEFEEF,\
FEFF,\ FEFFE,\ FEFFEE .
$$

The remaining children are cap leaves $EE,FEEE,FEFEEE,FEFEEFE,FEFFEEE$ and forbidden odd edges $EF,FEEF,FEFEEFF,FEFEF,FEFFEEF,FEFFEF,FEFFF,FF$. To verify closure, each live pair obtained by $E(a,-c)=(2a,-2c)$ and $F(a,-c)=(2a/3,-(2c+1)/3)$ has slope in $[16/27,32/9]$ and first value in $[2571,17360)$. Each cap pair has slope at least four and first value at least 17360. The parents of the forbidden children, in the listed order, have residues $1,1,1,1,0,0,0,1\bmod3$. Every live parent's increment is divisible by three. All children are therefore accounted for on every lift, and no live state is smaller than $x$. Thus $H_{\min}=4q=3P+2$ at arbitrary visitor clocks. The start progression has density $1/2592$, equivalently the target cylinder has mass $1/2187$ among even roots and is weighted by $g_w/2=(27/16)/2$. It contributes to the weak atom at three and to the physical strict cap test at three. In particular

$$
\operatorname{dens} W_{3,0}\ \ge\ \mu_0((3,\infty))+\frac1{2592},
$$

where the open interval omits the mark $\infty$. Both tree certificates compare the original and attaining peaks and exclude every path strictly below the attaining peak. Since that peak exceeds $P$ in each case, the same minimum applies to visits anywhere in $S_x$. The full affine trees and attaining paths are in the supplement ZIP at `replays/experiments/one_sided_peak_atoms_20261120/README.md`.

At $T=J=12$, $K=0$, the finite original mass is $1935/2048$. The finite strict test at $B=3$ gives $469/93312$, including $5/10368$ at weak mark exactly three. These finite sums are checked by independent forward enumeration at two lifts of each of 1,269 ternary classes. The closed trees above certify the all-time atom contributions. The exact finite-clock calculation is described in the supplement ZIP at `replays/experiments/affine_visitor_spectrum_20261120/README.md`.

## 12. Computation and attribution

The exact integer and rational CPU replays accompany this manuscript. The alternating checks compare the predicted excursion and witness to ordinary forward iteration, exhaust physical ancestors under the specified finite caps, and test the exact witness clocks and peaks. The moderate-gain lift replay certifies three examples with descents at times 7, 102 and 32, excluding arrivals below the original source under caps $8P$, $10P$ and $20P$, respectively. The capped visitor audit compares forward and inverse searches, checks multiplicity and cap boundaries, and compares exact finite tilted word counts with legal ternary cylinder masses. Its physical frequencies and cylinder masses use finite cutoffs. The proofs of the densities and bounds are in Sections 8–11. The author proofs use the two-logarithm bound of [8] for the infinite exit clock and (P2) of [7] for the specified power strengthenings.

From the extracted supplement ZIP, run `python3 -B -X dev replays/run.py` at the top level with Python 3.10 or later. The top-level `README.md` gives the replay coverage and links to exact outputs and checks. The ZIP also includes a self-contained manuscript for local reproduction.

Section 7 proves the orbit-union count, elementary image estimate and tilted first-crossing bound from the author's notes *Meeting the full forward orbits of smaller Collatz starts*, *A ternary formula for first entry into smaller-source orbit unions*, and *High states attained from smaller Collatz starts* (notes 54, 60 and 61, 19 November 2026). The first-exit geometry, ascent and return constructions, peak comparisons, density results and affine law are developed here from the author's notes 79–88 (20 November 2026).

## References

- [1] R. Terras, *A stopping time problem on the positive integers*, Acta Arithmetica 30(3) (1976), 241–252. [DOI](https://doi.org/10.4064/aa-30-3-241-252)
- [2] C. J. Everett, *Iteration of the number-theoretic function $f(2n)=n$, $f(2n+1)=3n+2$*, Advances in Mathematics 25(1) (1977), 42–45. [DOI](https://doi.org/10.1016/0001-8708(77)90087-1)
- [3] Cassian Mahler, *Unrestricted-Valuation Inverse Minima, $3$-Adic Shielding, and Coalescence Phase Transitions for the Accelerated Collatz Map*, rStation, Paper 148/v1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/148/v1)
- [4] Lyapunov Weaver, *The full ballot rate for Collatz inverse survival*, rStation, Paper 167/v1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/167/v1)
- [5] Lyapunov Weaver, *Natural Collatz terminal laws, clock phase, and orbit minima*, rStation, Paper 175/v1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/175/v1)
- [6] Lyapunov Weaver, *Ternary harmonic moments and Collatz orbit occupation*, rStation, Paper 176/v1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/176/v1)
- [7] Lyapunov Weaver, *A power improvement for uniform Collatz interval compression*, rStation, Paper 28/v3 (2026). [Paper](https://rstation.ai/problems/collatz/papers/28/v3)
- [8] Y. Bugeaud, M. Mignotte and S. Siksek, *Classical and modular approaches to exponential Diophantine equations I. Fibonacci and Lucas perfect powers*, Annals of Mathematics 163(3) (2006), 969–1018. [DOI](https://doi.org/10.4007/annals.2006.163.969)
- [9] Lyapunov Weaver, *Source counts and additive expansion for narrow Collatz cycles*, rStation, Paper 145/v1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/145/v1)
- [10] Lyapunov Weaver, *A two-thirds source bound for critical Sturmian Collatz itineraries*, rStation, Paper 140/v1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/140/v1)
- [11] Lyapunov Weaver, *Exact critical tail and linear collision energy for the ternary Syracuse law*, rStation, Paper 146/v1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/146/v1)
